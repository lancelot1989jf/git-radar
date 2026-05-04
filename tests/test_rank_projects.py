from __future__ import annotations

import json
from pathlib import Path

from scripts import rank_projects


KEYWORDS_CONFIG = {
    "exclude_keywords": ["guaranteed profit"],
    "categories": {
        "backtesting": {"keywords": ["backtest", "backtesting"]},
        "trading_bot": {"keywords": ["trading bot", "bot"]},
        "risk_management": {"keywords": ["risk", "leverage"]},
    },
}

SCORING_CONFIG = {
    "version": "test",
    "output_count": 10,
    "group_size": 10,
    "baseline_tolerance_days": 3,
    "recent_project_days": 365,
    "weights": {
        "total_stars_log": 0.25,
        "forks_log": 0.10,
        "star_delta_1d": 0.25,
        "star_delta_7d": 0.25,
        "activity": 0.10,
        "freshness": 0.05,
    },
    "caps": {
        "star_delta_1d": 100,
        "star_delta_7d": 500,
        "activity_days": 90,
        "freshness_days": 365,
    },
    "penalties": {
        "archived": 100,
        "fork": 30,
        "no_push_over_365_days": 20,
        "suspicious_keyword": 15,
        "no_description": 5,
    },
}

RISK_RULES_CONFIG = {
    "risk_keywords": {
        "high": ["guaranteed profit"],
        "medium": ["leverage", "crypto bot"],
        "low": ["backtesting"],
    },
    "risk_flags": {
        "trading_bot": {"include_any": ["trading bot", "bot"]},
        "crypto_related": {"include_any": ["crypto", "ccxt"]},
        "likely_research_tool": {"include_any": ["backtest", "research"]},
        "leverage_or_grid_related": {"include_any": ["leverage"]},
    },
}


def repo(
    full_name: str,
    *,
    stars: int,
    description: str,
    created_at: str = "2025-01-01T00:00:00Z",
    pushed_at: str = "2026-05-04T00:00:00Z",
) -> dict:
    owner, name = full_name.split("/", 1)
    return {
        "id": abs(hash(full_name)) % 100000,
        "full_name": full_name,
        "owner": owner,
        "name": name,
        "html_url": f"https://github.com/{full_name}",
        "description": description,
        "stars": stars,
        "forks": max(stars // 10, 0),
        "watchers": stars,
        "open_issues": 1,
        "language": "Python",
        "topics": ["backtesting"],
        "license": "MIT",
        "archived": False,
        "fork": False,
        "created_at": created_at,
        "updated_at": pushed_at,
        "pushed_at": pushed_at,
        "matched_queries": ["topic:backtesting"],
    }


def write_snapshot(path: Path, items: list[dict]) -> None:
    payload = {
        "generated_at": "2026-05-04T12:00:00+00:00",
        "query_count": 1,
        "request_count": 1,
        "count": len(items),
        "items": items,
        "errors": [],
    }
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_only_current_snapshot_outputs_null_deltas(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "snapshots"
    snapshot_dir.mkdir()
    write_snapshot(snapshot_dir / "2026-05-04.json", [repo("owner/alpha", stars=10, description="Backtesting toolkit")])

    payload = rank_projects.build_latest_candidates(
        snapshot_dir=snapshot_dir,
        keywords_config=KEYWORDS_CONFIG,
        scoring_config=SCORING_CONFIG,
        risk_rules_config=RISK_RULES_CONFIG,
        generated_at="2026-05-04T12:05:00+00:00",
    )

    assert payload["baseline_1d"] is None
    assert payload["baseline_7d"] is None
    assert payload["items"][0]["star_delta_1d"] is None
    assert payload["items"][0]["star_delta_7d"] is None
    assert payload["items"][0]["category_guess"] == ["backtesting"]


def test_baselines_calculate_deltas_and_new_repo_uses_null_delta(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "snapshots"
    snapshot_dir.mkdir()
    write_snapshot(snapshot_dir / "2026-04-27.json", [repo("owner/alpha", stars=5, description="Backtesting toolkit")])
    write_snapshot(snapshot_dir / "2026-05-03.json", [repo("owner/alpha", stars=10, description="Backtesting toolkit")])
    write_snapshot(
        snapshot_dir / "2026-05-04.json",
        [
            repo("owner/alpha", stars=15, description="Backtesting toolkit"),
            repo("owner/beta", stars=20, description="Crypto trading bot with leverage"),
        ],
    )

    payload = rank_projects.build_latest_candidates(
        snapshot_dir=snapshot_dir,
        keywords_config=KEYWORDS_CONFIG,
        scoring_config=SCORING_CONFIG,
        risk_rules_config=RISK_RULES_CONFIG,
        generated_at="2026-05-04T12:05:00+00:00",
    )
    items = {item["full_name"]: item for item in payload["items"]}

    assert payload["baseline_1d"] == "2026-05-03.json"
    assert payload["baseline_7d"] == "2026-04-27.json"
    assert items["owner/alpha"]["star_delta_1d"] == 5
    assert items["owner/alpha"]["star_delta_7d"] == 10
    assert items["owner/beta"]["star_delta_1d"] is None
    assert items["owner/beta"]["star_delta_7d"] is None


def test_risk_flags_and_hot_score_sorting_are_stable(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "snapshots"
    snapshot_dir.mkdir()
    write_snapshot(
        snapshot_dir / "2026-05-04.json",
        [
            repo("owner/low", stars=100, description="Backtesting research toolkit"),
            repo("owner/high", stars=100, description="Guaranteed profit crypto bot leverage"),
        ],
    )

    payload = rank_projects.build_latest_candidates(
        snapshot_dir=snapshot_dir,
        keywords_config=KEYWORDS_CONFIG,
        scoring_config=SCORING_CONFIG,
        risk_rules_config=RISK_RULES_CONFIG,
        generated_at="2026-05-04T12:05:00+00:00",
    )
    items = {item["full_name"]: item for item in payload["items"]}

    assert "risk_keyword_high" in items["owner/high"]["risk_flags"]
    assert "trading_bot" in items["owner/high"]["risk_flags"]
    assert items["owner/high"]["risk_level"] == "高"
    assert items["owner/low"]["hot_score"] > items["owner/high"]["hot_score"]
    assert payload["items"][0]["full_name"] == "owner/low"
