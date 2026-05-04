#!/usr/bin/env python3
"""Collect GitHub repositories for the finance radar snapshot.

The collector only reads GitHub metadata through the REST API. It never clones,
installs, imports, or executes candidate repository code.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from copy import deepcopy
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import requests
import yaml
from dateutil.relativedelta import relativedelta


GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
DEFAULT_SORTS = ("stars", "updated")
DEFAULT_PER_PAGE = 50
DEFAULT_MAX_RETRIES = 2
DEFAULT_MAX_RETRY_SLEEP_SECONDS = 60


@dataclass
class RateLimitError(RuntimeError):
    """Raised when GitHub asks us to slow down beyond the retry budget."""

    message: str
    wait_seconds: float | None = None

    def __str__(self) -> str:
        if self.wait_seconds is None:
            return self.message
        return f"{self.message}; retry_after_seconds={self.wait_seconds:.0f}"


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return loaded


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def pushed_after_date(config: Mapping[str, Any], today: date | None = None) -> str:
    base = today or datetime.now(timezone.utc).date()
    months = int(config.get("active_months", 18))
    return (base - relativedelta(months=months)).isoformat()


def quote_search_term(term: str) -> str:
    normalized = " ".join(str(term).strip().split())
    if not normalized:
        return normalized
    if any(char.isspace() for char in normalized):
        return f'"{normalized}"'
    return normalized


def language_qualifier(language: str) -> str:
    normalized = str(language).strip()
    if " " in normalized:
        return f'language:"{normalized}"'
    return f"language:{normalized}"


def dedupe_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        normalized = " ".join(value.split())
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        output.append(normalized)
    return output


def build_queries(config: Mapping[str, Any], today: date | None = None) -> list[str]:
    pushed_after = pushed_after_date(config, today=today)
    suffix = f"archived:false fork:false pushed:>{pushed_after}"
    queries: list[str] = []

    for topic in config.get("topics", []) or []:
        topic_value = str(topic).strip()
        if topic_value:
            queries.append(f"topic:{topic_value} {suffix}")

    for keyword in config.get("keywords", []) or []:
        term = quote_search_term(str(keyword))
        if term:
            queries.append(f"{term} in:name,description,readme {suffix}")

    languages = [str(item).strip() for item in config.get("languages", []) or [] if str(item).strip()]
    seed_keywords = [
        str(item).strip()
        for item in config.get("language_query_keywords", []) or []
        if str(item).strip()
    ]
    for seed in seed_keywords:
        term = quote_search_term(seed)
        for language in languages:
            queries.append(
                f"{term} in:name,description,readme {language_qualifier(language)} {suffix}"
            )

    max_queries = config.get("max_queries")
    deduped = dedupe_preserve_order(queries)
    if max_queries is not None:
        return deduped[: int(max_queries)]
    return deduped


def header_value(headers: Mapping[str, str], name: str) -> str | None:
    target = name.lower()
    for key, value in headers.items():
        if key.lower() == target:
            return value
    return None


def parse_rate_limit_wait_seconds(
    headers: Mapping[str, str], now: float | None = None
) -> float | None:
    retry_after = header_value(headers, "retry-after")
    if retry_after:
        try:
            return max(float(retry_after), 0.0)
        except ValueError:
            return None

    remaining = header_value(headers, "x-ratelimit-remaining")
    reset_at = header_value(headers, "x-ratelimit-reset")
    if remaining == "0" and reset_at:
        try:
            return max(float(reset_at) - (now if now is not None else time.time()) + 1, 0.0)
        except ValueError:
            return None
    return None


def github_headers(token: str | None) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "github-finance-radar",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def search_repositories(
    session: requests.Session,
    *,
    query: str,
    sort: str,
    order: str,
    per_page: int,
    token: str | None,
    timeout_seconds: int = 30,
    max_retries: int = DEFAULT_MAX_RETRIES,
    max_retry_sleep_seconds: int = DEFAULT_MAX_RETRY_SLEEP_SECONDS,
) -> dict[str, Any]:
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
        "page": 1,
    }

    for attempt in range(max_retries + 1):
        response = session.get(
            GITHUB_SEARCH_URL,
            headers=github_headers(token),
            params=params,
            timeout=timeout_seconds,
        )

        if response.status_code in {403, 429}:
            wait_seconds = parse_rate_limit_wait_seconds(response.headers)
            if (
                wait_seconds is not None
                and wait_seconds <= max_retry_sleep_seconds
                and attempt < max_retries
            ):
                time.sleep(wait_seconds)
                continue
            raise RateLimitError(
                f"GitHub rate limit or abuse protection returned {response.status_code}",
                wait_seconds,
            )

        if response.status_code >= 400:
            body = response.text[:500]
            raise RuntimeError(f"GitHub API returned {response.status_code}: {body}")

        payload = response.json()
        if not isinstance(payload, dict):
            raise RuntimeError("GitHub API response root is not an object")
        return payload

    raise RuntimeError("unreachable retry state")


def normalize_repo(item: Mapping[str, Any]) -> dict[str, Any]:
    owner = item.get("owner") or {}
    license_info = item.get("license") or {}
    license_name = None
    if isinstance(license_info, Mapping):
        license_name = license_info.get("spdx_id") or license_info.get("name")
        if license_name == "NOASSERTION":
            license_name = license_info.get("name")

    full_name = str(item.get("full_name") or "")
    if "/" in full_name:
        owner_name, repo_name = full_name.split("/", 1)
    else:
        owner_name = str(owner.get("login") or "")
        repo_name = str(item.get("name") or "")

    topics = item.get("topics") or []
    if not isinstance(topics, list):
        topics = []

    return {
        "id": int(item.get("id") or 0),
        "full_name": full_name,
        "owner": owner_name,
        "name": repo_name,
        "html_url": item.get("html_url") or "",
        "description": item.get("description"),
        "stars": int(item.get("stargazers_count") or 0),
        "forks": int(item.get("forks_count") or 0),
        "watchers": int(item.get("watchers_count") or 0),
        "open_issues": int(item.get("open_issues_count") or 0),
        "language": item.get("language"),
        "topics": sorted({str(topic) for topic in topics if str(topic)}),
        "license": license_name,
        "archived": bool(item.get("archived", False)),
        "fork": bool(item.get("fork", False)),
        "created_at": item.get("created_at") or "",
        "updated_at": item.get("updated_at") or "",
        "pushed_at": item.get("pushed_at"),
        "matched_queries": [],
    }


def merge_repo(
    repos: dict[str, dict[str, Any]],
    repo: Mapping[str, Any],
    *,
    matched_query: str,
) -> None:
    key = str(repo.get("full_name") or "")
    if not key:
        return

    if key not in repos:
        merged = deepcopy(dict(repo))
        merged["matched_queries"] = [matched_query]
        repos[key] = merged
        return

    existing = repos[key]
    for field in ("stars", "forks", "watchers", "open_issues"):
        existing[field] = max(int(existing.get(field) or 0), int(repo.get(field) or 0))

    for field in (
        "id",
        "owner",
        "name",
        "html_url",
        "description",
        "language",
        "license",
        "created_at",
        "updated_at",
        "pushed_at",
    ):
        if not existing.get(field) and repo.get(field):
            existing[field] = repo[field]

    for field in ("archived", "fork"):
        existing[field] = bool(existing.get(field)) or bool(repo.get(field))

    existing_topics = set(existing.get("topics") or [])
    existing_topics.update(repo.get("topics") or [])
    existing["topics"] = sorted(existing_topics)

    queries = set(existing.get("matched_queries") or [])
    queries.add(matched_query)
    existing["matched_queries"] = sorted(queries)


def collect_snapshot(
    *,
    config: Mapping[str, Any],
    token: str | None,
    generated_at: str | None = None,
    session: requests.Session | None = None,
) -> dict[str, Any]:
    queries = build_queries(config)
    sorts = tuple(config.get("sorts") or DEFAULT_SORTS)
    per_page = int(config.get("per_page") or DEFAULT_PER_PAGE)
    request_sleep_seconds = float(config.get("request_sleep_seconds") or 0)
    max_retries = int(config.get("max_retries", DEFAULT_MAX_RETRIES))
    max_retry_sleep_seconds = int(
        config.get("max_retry_sleep_seconds", DEFAULT_MAX_RETRY_SLEEP_SECONDS)
    )

    repos: dict[str, dict[str, Any]] = {}
    errors: list[dict[str, Any]] = []
    request_count = 0
    active_session = session or requests.Session()

    for query in queries:
        for sort in sorts:
            request_count += 1
            try:
                payload = search_repositories(
                    active_session,
                    query=query,
                    sort=str(sort),
                    order="desc",
                    per_page=per_page,
                    token=token,
                    max_retries=max_retries,
                    max_retry_sleep_seconds=max_retry_sleep_seconds,
                )
                for raw_item in payload.get("items", []) or []:
                    merge_repo(repos, normalize_repo(raw_item), matched_query=query)
            except Exception as exc:  # noqa: BLE001 - errors are persisted for audit.
                errors.append({"query": query, "sort": sort, "error": str(exc)})

            if request_sleep_seconds > 0:
                time.sleep(request_sleep_seconds)

    items = sorted(
        repos.values(),
        key=lambda item: (-int(item.get("stars") or 0), str(item.get("full_name") or "").lower()),
    )
    return {
        "generated_at": generated_at or utc_now_iso(),
        "query_count": len(queries),
        "request_count": request_count,
        "count": len(items),
        "items": items,
        "errors": errors,
    }


def write_json(path: str | Path, payload: Mapping[str, Any]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect GitHub finance radar snapshot.")
    parser.add_argument("--config", required=True, help="Path to config/keywords.yml")
    parser.add_argument("--out", required=True, help="Output snapshot JSON path")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_yaml(args.config)
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(
            "warning: GITHUB_TOKEN is not set; unauthenticated GitHub API limits are lower",
            file=sys.stderr,
        )

    snapshot = collect_snapshot(config=config, token=token)
    write_json(args.out, snapshot)
    if snapshot["count"] == 0 and snapshot["errors"]:
        print("error: collection produced no repositories; see snapshot errors", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
