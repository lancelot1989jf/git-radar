#!/usr/bin/env python3
"""Rank collected GitHub finance radar snapshots.

Ranking is deterministic from local snapshots and config files. It does not
clone or execute candidate repositories.
"""

from __future__ import annotations

import argparse
import json
import math
from copy import deepcopy
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Mapping

import yaml
from dateutil import parser as datetime_parser


DEFAULT_OUTPUT_COUNT = 80
DEFAULT_GROUP_SIZE = 25
DEFAULT_BASELINE_TOLERANCE_DAYS = 3


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return loaded


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as fh:
        loaded = json.load(fh)
    if not isinstance(loaded, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return loaded


def write_json(path: str | Path, payload: Mapping[str, Any]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime_parser.isoparse(value)
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def parse_snapshot_date(path: Path) -> date | None:
    try:
        return date.fromisoformat(path.stem)
    except ValueError:
        return None


def list_snapshot_paths(snapshot_dir: str | Path) -> list[Path]:
    paths: list[Path] = []
    for path in Path(snapshot_dir).glob("*.json"):
        if parse_snapshot_date(path) is not None:
            paths.append(path)
    return sorted(paths, key=lambda item: parse_snapshot_date(item) or date.min)


def load_snapshots(snapshot_dir: str | Path) -> list[dict[str, Any]]:
    snapshots = []
    for path in list_snapshot_paths(snapshot_dir):
        snapshot_date = parse_snapshot_date(path)
        if snapshot_date is None:
            continue
        snapshots.append({"date": snapshot_date, "path": path, "payload": load_json(path)})
    if not snapshots:
        raise FileNotFoundError(f"no snapshot JSON files found in {snapshot_dir}")
    return snapshots


def select_current_snapshot(snapshots: list[dict[str, Any]]) -> dict[str, Any]:
    return max(snapshots, key=lambda item: item["date"])


def select_baseline_snapshot(
    snapshots: list[dict[str, Any]],
    *,
    current_date: date,
    days_back: int,
    tolerance_days: int = DEFAULT_BASELINE_TOLERANCE_DAYS,
) -> dict[str, Any] | None:
    target = current_date - timedelta(days=days_back)
    by_date = {item["date"]: item for item in snapshots if item["date"] < current_date}

    if days_back == 1:
        return by_date.get(target)

    candidates = list(by_date.values())
    if not candidates:
        return None

    closest = min(candidates, key=lambda item: abs((item["date"] - target).days))
    distance = abs((closest["date"] - target).days)
    if distance <= tolerance_days:
        return closest
    return None


def index_snapshot_items(snapshot: Mapping[str, Any] | None) -> dict[str, Mapping[str, Any]]:
    if not snapshot:
        return {}
    indexed: dict[str, Mapping[str, Any]] = {}
    for item in snapshot.get("items", []) or []:
        full_name = str(item.get("full_name") or "")
        if full_name:
            indexed[full_name] = item
    return indexed


def star_delta(
    current_item: Mapping[str, Any],
    baseline_index: Mapping[str, Mapping[str, Any]],
) -> int | None:
    if not baseline_index:
        return None
    full_name = str(current_item.get("full_name") or "")
    baseline_item = baseline_index.get(full_name)
    if baseline_item is None:
        return None
    return int(current_item.get("stars") or 0) - int(baseline_item.get("stars") or 0)


def aggregate_text(item: Mapping[str, Any]) -> str:
    parts = [
        item.get("full_name"),
        item.get("name"),
        item.get("description"),
        item.get("language"),
        " ".join(item.get("topics") or []),
        " ".join(item.get("matched_queries") or []),
    ]
    return " ".join(str(part) for part in parts if part).lower()


def contains_any(text: str, terms: list[str]) -> bool:
    lowered_terms = [str(term).strip().lower() for term in terms if str(term).strip()]
    return any(term in text for term in lowered_terms)


def category_guess(item: Mapping[str, Any], keywords_config: Mapping[str, Any]) -> list[str]:
    text = aggregate_text(item)
    categories = keywords_config.get("categories") or {}
    output = []
    for category, rule in categories.items():
        if not isinstance(rule, Mapping):
            continue
        if contains_any(text, list(rule.get("keywords") or [])):
            output.append(str(category))
    return sorted(output)


def risk_flags(item: Mapping[str, Any], risk_rules: Mapping[str, Any]) -> list[str]:
    text = aggregate_text(item)
    output: set[str] = set()

    for level, terms in (risk_rules.get("risk_keywords") or {}).items():
        if contains_any(text, list(terms or [])):
            output.add(f"risk_keyword_{level}")

    for flag_name, rule in (risk_rules.get("risk_flags") or {}).items():
        if not isinstance(rule, Mapping):
            continue
        if contains_any(text, list(rule.get("include_any") or [])):
            output.add(str(flag_name))

    return sorted(output)


def risk_level(flags: list[str]) -> str:
    if "risk_keyword_high" in flags:
        return "高"
    if "risk_keyword_medium" in flags or "leverage_or_grid_related" in flags:
        return "中"
    if "trading_bot" in flags or "crypto_related" in flags:
        return "中"
    return "低"


def days_since(value: str | None, now: datetime) -> float | None:
    parsed = parse_datetime(value)
    if parsed is None:
        return None
    return max((now - parsed).total_seconds() / 86400, 0.0)


def decaying_score(days: float | None, cap_days: int) -> float:
    if days is None or cap_days <= 0:
        return 0.0
    return max(100.0 * (1.0 - min(days, cap_days) / cap_days), 0.0)


def score_repo(
    item: Mapping[str, Any],
    *,
    star_delta_1d: int | None,
    star_delta_7d: int | None,
    flags: list[str],
    keywords_config: Mapping[str, Any],
    scoring_config: Mapping[str, Any],
    now: datetime,
) -> float:
    weights = scoring_config.get("weights") or {}
    caps = scoring_config.get("caps") or {}
    penalties = scoring_config.get("penalties") or {}

    stars = int(item.get("stars") or 0)
    forks = int(item.get("forks") or 0)
    activity_days = int(caps.get("activity_days", 90))
    freshness_days = int(caps.get("freshness_days", 365))

    pushed_days = days_since(item.get("pushed_at"), now)
    created_days = days_since(item.get("created_at"), now)
    activity_score = decaying_score(pushed_days, activity_days)
    freshness_score = decaying_score(created_days, freshness_days)

    score = 0.0
    score += float(weights.get("total_stars_log", 0.25)) * math.log10(stars + 1) * 20
    score += float(weights.get("forks_log", 0.10)) * math.log10(forks + 1) * 20
    score += float(weights.get("star_delta_1d", 0.25)) * min(
        max(star_delta_1d or 0, 0), int(caps.get("star_delta_1d", 100))
    )
    score += float(weights.get("star_delta_7d", 0.25)) * min(
        max(star_delta_7d or 0, 0) / 5, int(caps.get("star_delta_7d", 500))
    )
    score += float(weights.get("activity", 0.10)) * activity_score
    score += float(weights.get("freshness", 0.05)) * freshness_score

    if item.get("archived"):
        score -= float(penalties.get("archived", 100))
    if item.get("fork"):
        score -= float(penalties.get("fork", 30))
    if pushed_days is None or pushed_days > 365:
        score -= float(penalties.get("no_push_over_365_days", 20))
    if not item.get("description"):
        score -= float(penalties.get("no_description", 5))

    text = aggregate_text(item)
    suspicious_terms = list(keywords_config.get("exclude_keywords") or [])
    if contains_any(text, suspicious_terms) or any(
        flag in flags for flag in ("risk_keyword_high", "risk_keyword_medium")
    ):
        score -= float(penalties.get("suspicious_keyword", 15))

    return round(score, 2)


def ranking_reasons(
    item: Mapping[str, Any],
    *,
    star_delta_1d: int | None,
    star_delta_7d: int | None,
    categories: list[str],
    flags: list[str],
    now: datetime,
) -> list[str]:
    reasons: list[str] = []
    if star_delta_1d is not None and star_delta_1d > 0:
        reasons.append(f"24 小时涨星 +{star_delta_1d}")
    if star_delta_7d is not None and star_delta_7d > 0:
        reasons.append(f"7 日涨星 +{star_delta_7d}")
    if int(item.get("stars") or 0) >= 1000:
        reasons.append("总 star 数较高")

    pushed_days = days_since(item.get("pushed_at"), now)
    if pushed_days is not None and pushed_days <= 30:
        reasons.append("近 30 天有 push")
    elif pushed_days is not None and pushed_days <= 90:
        reasons.append("近 90 天有 push")

    if categories:
        reasons.append("匹配分类：" + "、".join(categories[:3]))
    if flags:
        reasons.append("包含风险或用途标记：" + "、".join(flags[:3]))
    if not reasons:
        reasons.append("基础热度稳定")
    return reasons


def current_snapshot_now(current_snapshot: Mapping[str, Any], current_date: date) -> datetime:
    generated = parse_datetime(current_snapshot.get("generated_at"))
    if generated is not None:
        return generated
    return datetime.combine(current_date, time(12, 0), tzinfo=timezone.utc)


def enrich_items(
    current_snapshot: Mapping[str, Any],
    *,
    baseline_1d: Mapping[str, Any] | None,
    baseline_7d: Mapping[str, Any] | None,
    keywords_config: Mapping[str, Any],
    risk_rules_config: Mapping[str, Any],
    scoring_config: Mapping[str, Any],
    current_date: date,
) -> list[dict[str, Any]]:
    baseline_1d_index = index_snapshot_items(baseline_1d)
    baseline_7d_index = index_snapshot_items(baseline_7d)
    now = current_snapshot_now(current_snapshot, current_date)

    enriched: list[dict[str, Any]] = []
    for raw_item in current_snapshot.get("items", []) or []:
        item = deepcopy(dict(raw_item))
        delta_1d = star_delta(item, baseline_1d_index)
        delta_7d = star_delta(item, baseline_7d_index)
        categories = category_guess(item, keywords_config)
        flags = risk_flags(item, risk_rules_config)
        item["star_delta_1d"] = delta_1d
        item["star_delta_7d"] = delta_7d
        item["star_delta_30d"] = None
        item["category_guess"] = categories
        item["risk_flags"] = flags
        item["risk_level"] = risk_level(flags)
        item["hot_score"] = score_repo(
            item,
            star_delta_1d=delta_1d,
            star_delta_7d=delta_7d,
            flags=flags,
            keywords_config=keywords_config,
            scoring_config=scoring_config,
            now=now,
        )
        item["ranking_reasons"] = ranking_reasons(
            item,
            star_delta_1d=delta_1d,
            star_delta_7d=delta_7d,
            categories=categories,
            flags=flags,
            now=now,
        )
        enriched.append(item)
    return enriched


def sort_by_hot_score(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        items,
        key=lambda item: (
            -float(item.get("hot_score") or 0),
            -int(item.get("stars") or 0),
            str(item.get("full_name") or "").lower(),
        ),
    )


def select_candidates(
    items: list[dict[str, Any]],
    *,
    scoring_config: Mapping[str, Any],
    now: datetime,
) -> list[dict[str, Any]]:
    output_count = int(scoring_config.get("output_count", DEFAULT_OUTPUT_COUNT))
    group_size = int(scoring_config.get("group_size", DEFAULT_GROUP_SIZE))
    recent_project_days = int(scoring_config.get("recent_project_days", 365))
    activity_days = int((scoring_config.get("caps") or {}).get("activity_days", 90))

    selected: dict[str, dict[str, Any]] = {}

    def add_bucket(bucket: list[dict[str, Any]]) -> None:
        for item in bucket[:group_size]:
            full_name = str(item.get("full_name") or "")
            if full_name:
                selected[full_name] = item

    add_bucket(sorted(items, key=lambda item: (-int(item.get("stars") or 0), item["full_name"])))
    add_bucket(
        sorted(
            [item for item in items if item.get("star_delta_1d") is not None],
            key=lambda item: (
                -int(item.get("star_delta_1d") or 0),
                -float(item.get("hot_score") or 0),
                item["full_name"],
            ),
        )
    )
    add_bucket(
        sorted(
            [item for item in items if item.get("star_delta_7d") is not None],
            key=lambda item: (
                -int(item.get("star_delta_7d") or 0),
                -float(item.get("hot_score") or 0),
                item["full_name"],
            ),
        )
    )
    add_bucket(
        sort_by_hot_score(
            [
                item
                for item in items
                if days_since(item.get("created_at"), now) is not None
                and (days_since(item.get("created_at"), now) or 0) <= recent_project_days
            ]
        )
    )
    add_bucket(
        sort_by_hot_score(
            [
                item
                for item in items
                if days_since(item.get("pushed_at"), now) is not None
                and (days_since(item.get("pushed_at"), now) or 0) <= activity_days
            ]
        )
    )

    final_items = sort_by_hot_score(list(selected.values()))[:output_count]
    for index, item in enumerate(final_items, start=1):
        item["rank"] = index
    return final_items


def build_latest_candidates(
    *,
    snapshot_dir: str | Path,
    keywords_config: Mapping[str, Any],
    scoring_config: Mapping[str, Any],
    risk_rules_config: Mapping[str, Any],
    generated_at: str | None = None,
) -> dict[str, Any]:
    snapshots = load_snapshots(snapshot_dir)
    current = select_current_snapshot(snapshots)
    current_date = current["date"]
    tolerance_days = int(
        scoring_config.get("baseline_tolerance_days", DEFAULT_BASELINE_TOLERANCE_DAYS)
    )
    baseline_1d = select_baseline_snapshot(
        snapshots,
        current_date=current_date,
        days_back=1,
        tolerance_days=tolerance_days,
    )
    baseline_7d = select_baseline_snapshot(
        snapshots,
        current_date=current_date,
        days_back=7,
        tolerance_days=tolerance_days,
    )

    current_payload = current["payload"]
    baseline_1d_payload = baseline_1d["payload"] if baseline_1d else None
    baseline_7d_payload = baseline_7d["payload"] if baseline_7d else None
    now = current_snapshot_now(current_payload, current_date)

    enriched = enrich_items(
        current_payload,
        baseline_1d=baseline_1d_payload,
        baseline_7d=baseline_7d_payload,
        keywords_config=keywords_config,
        risk_rules_config=risk_rules_config,
        scoring_config=scoring_config,
        current_date=current_date,
    )
    candidates = select_candidates(enriched, scoring_config=scoring_config, now=now)

    return {
        "generated_at": generated_at or utc_now_iso(),
        "current_snapshot": current["path"].name,
        "baseline_1d": baseline_1d["path"].name if baseline_1d else None,
        "baseline_7d": baseline_7d["path"].name if baseline_7d else None,
        "count": len(candidates),
        "ranking_config": {
            "version": scoring_config.get("version", "unknown"),
            "output_count": int(scoring_config.get("output_count", DEFAULT_OUTPUT_COUNT)),
            "baseline_tolerance_days": tolerance_days,
        },
        "items": candidates,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rank GitHub finance radar snapshots.")
    parser.add_argument("--snapshot-dir", required=True, help="Directory with YYYY-MM-DD.json files")
    parser.add_argument("--out", required=True, help="Output latest candidates JSON path")
    parser.add_argument("--config", default="config/keywords.yml", help="Keyword config path")
    parser.add_argument("--scoring", default="config/scoring.yml", help="Scoring config path")
    parser.add_argument("--risk-rules", default="config/risk_rules.yml", help="Risk rules config path")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    payload = build_latest_candidates(
        snapshot_dir=args.snapshot_dir,
        keywords_config=load_yaml(args.config),
        scoring_config=load_yaml(args.scoring),
        risk_rules_config=load_yaml(args.risk_rules),
    )
    write_json(args.out, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
