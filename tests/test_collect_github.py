from __future__ import annotations

from datetime import date

from scripts import collect_github


def test_build_queries_cover_topic_keyword_language_and_pushed_window() -> None:
    config = {
        "active_months": 18,
        "topics": ["backtesting"],
        "keywords": ["ai trading"],
        "languages": ["Python"],
        "language_query_keywords": ["quant"],
    }

    queries = collect_github.build_queries(config, today=date(2026, 5, 4))

    assert "topic:backtesting archived:false fork:false pushed:>2024-11-04" in queries
    assert '"ai trading" in:name,description,readme archived:false fork:false pushed:>2024-11-04' in queries
    assert "quant in:name,description,readme language:Python archived:false fork:false pushed:>2024-11-04" in queries


def test_normalize_repo_and_merge_matched_queries() -> None:
    raw = {
        "id": 123,
        "full_name": "owner/repo",
        "owner": {"login": "owner"},
        "name": "repo",
        "html_url": "https://github.com/owner/repo",
        "description": "Backtesting toolkit",
        "stargazers_count": 10,
        "forks_count": 2,
        "watchers_count": 10,
        "open_issues_count": 1,
        "language": "Python",
        "topics": ["backtesting", "quant"],
        "license": {"spdx_id": "MIT"},
        "archived": False,
        "fork": False,
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2026-05-01T00:00:00Z",
        "pushed_at": "2026-05-01T00:00:00Z",
    }
    normalized = collect_github.normalize_repo(raw)

    assert normalized["full_name"] == "owner/repo"
    assert normalized["stars"] == 10
    assert normalized["license"] == "MIT"
    assert normalized["topics"] == ["backtesting", "quant"]

    repos: dict[str, dict] = {}
    collect_github.merge_repo(repos, normalized, matched_query="topic:backtesting")

    updated = dict(normalized)
    updated["stars"] = 12
    updated["topics"] = ["risk-management"]
    collect_github.merge_repo(repos, updated, matched_query="risk model in:name,description,readme")

    merged = repos["owner/repo"]
    assert merged["stars"] == 12
    assert merged["topics"] == ["backtesting", "quant", "risk-management"]
    assert merged["matched_queries"] == [
        "risk model in:name,description,readme",
        "topic:backtesting",
    ]


def test_parse_rate_limit_wait_seconds() -> None:
    assert collect_github.parse_rate_limit_wait_seconds({"Retry-After": "7"}) == 7
    assert collect_github.parse_rate_limit_wait_seconds(
        {"x-ratelimit-remaining": "0", "x-ratelimit-reset": "110"}, now=100
    ) == 11
    assert collect_github.parse_rate_limit_wait_seconds({}) is None


class FakeResponse:
    status_code = 200
    headers: dict[str, str] = {}
    text = ""

    def json(self) -> dict:
        return {
            "items": [
                {
                    "id": 1,
                    "full_name": "owner/repo",
                    "owner": {"login": "owner"},
                    "name": "repo",
                    "html_url": "https://github.com/owner/repo",
                    "description": "Quant backtesting",
                    "stargazers_count": 100,
                    "forks_count": 10,
                    "watchers_count": 100,
                    "open_issues_count": 3,
                    "language": "Python",
                    "topics": ["quant"],
                    "license": {"spdx_id": "Apache-2.0"},
                    "archived": False,
                    "fork": False,
                    "created_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2026-05-01T00:00:00Z",
                    "pushed_at": "2026-05-01T00:00:00Z",
                }
            ]
        }


class FakeSession:
    def __init__(self) -> None:
        self.calls = []

    def get(self, url: str, **kwargs) -> FakeResponse:
        self.calls.append((url, kwargs))
        return FakeResponse()


def test_collect_snapshot_uses_fake_session_without_network() -> None:
    session = FakeSession()
    snapshot = collect_github.collect_snapshot(
        config={
            "topics": ["quant"],
            "keywords": [],
            "languages": [],
            "sorts": ["stars"],
            "request_sleep_seconds": 0,
        },
        token="token",
        generated_at="2026-05-04T00:00:00+00:00",
        session=session,
    )

    assert snapshot["query_count"] == 1
    assert snapshot["request_count"] == 1
    assert snapshot["count"] == 1
    assert snapshot["items"][0]["matched_queries"][0].startswith("topic:quant")
    assert session.calls[0][1]["headers"]["Authorization"] == "Bearer token"
