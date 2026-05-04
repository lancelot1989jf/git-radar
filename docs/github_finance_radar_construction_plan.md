# GitHub 金融/量化/自动化交易项目雷达：Codex 施工计划文档

版本：v0.1  
日期：2026-05-04  
默认时区：Asia/Tokyo  
目标仓库建议名称：`github-finance-radar`

---

## 0. 一句话目标

构建一个自动化系统，每天定时收集 GitHub 上金融、量化、自动化交易、回测、投资组合优化、风控、市场微结构、加密交易、AI Trading 等相关开源项目，识别“最火”和“涨星最快”的项目，生成中文 Markdown 报告，帮助用户获得工程、产品、Agent、数据系统和交易基础设施方面的灵感。

本系统只做开源项目情报分析，不提供投资建议，不运行未知交易机器人，不处理真实交易所 API Key。

---

## 1. 系统边界

### 1.1 系统要做什么

1. 每日定时从 GitHub API 收集候选仓库。
2. 按关键词、topic、语言、活跃度、stars、forks、创建时间、更新时间等筛选金融圈相关项目。
3. 保存每日 snapshot。
4. 通过 snapshot 差分计算：
   - 24 小时 star 增量
   - 7 日 star 增量
   - 30 日 star 增量，可后续加入
   - 综合热度分数
5. 生成 `data/latest_candidates.json`。
6. 调用 Codex 读取结构化数据，生成中文 Markdown 报告。
7. 将报告保存到 `reports/YYYY-MM-DD-finance-github-radar.md`。
8. 自动 commit/push 到仓库。
9. 可选：推送到邮件、企业微信、Slack、Notion、Obsidian 或 Telegram。

### 1.2 系统暂时不做什么

1. 不自动 clone 并运行未知仓库代码。
2. 不接入真实交易账户。
3. 不存储交易所 API Key。
4. 不对项目做投资收益预测。
5. 不把 GitHub star 解释为投资信号。
6. 不绕过 GitHub API 限流。
7. 不使用 Codex 直接漫游网页作为主要采集方式。

---

## 2. 总体架构

```text
GitHub Search API / Repository API
        ↓
scripts/collect_github.py
        ↓
data/snapshots/YYYY-MM-DD.json
        ↓
scripts/rank_projects.py
        ↓
data/latest_candidates.json
        ↓
Codex GitHub Action 或 codex exec
        ↓
reports/YYYY-MM-DD-finance-github-radar.md
        ↓
GitHub commit / notification / downstream knowledge base
```

关键原则：

- Python 负责确定性采集、清洗、差分、排名。
- Codex 负责阅读结构化结果、归纳趋势、写报告、提出工程灵感。
- 所有中间数据落盘，保证可审计、可复现、可调试。
- 报告必须包含风险提示，避免把热门项目误读为可直接交易的策略。

---

## 3. 推荐仓库结构

```text
github-finance-radar/
├── .github/
│   ├── workflows/
│   │   ├── daily-radar.yml
│   │   └── weekly-radar.yml                  # 后续可选
│   └── codex/
│       ├── prompts/
│       │   ├── daily_finance_radar.md
│       │   ├── weekly_finance_radar.md       # 后续可选
│       │   └── triage_candidate_repo.md      # 后续可选
│       └── instructions.md
├── .agents/
│   └── skills/
│       └── github-finance-radar/
│           └── SKILL.md                      # 后续可选
├── config/
│   ├── keywords.yml
│   ├── scoring.yml
│   └── risk_rules.yml
├── scripts/
│   ├── collect_github.py
│   ├── rank_projects.py
│   ├── enrich_repos.py                       # 后续可选
│   ├── validate_report.py                    # 后续可选
│   └── run_daily.sh
├── data/
│   ├── snapshots/
│   │   └── YYYY-MM-DD.json
│   ├── latest_candidates.json
│   ├── watchlist.yml
│   └── ignorelist.yml
├── reports/
│   ├── daily/
│   │   └── YYYY-MM-DD-finance-github-radar.md
│   ├── weekly/
│   └── ideas/
├── tests/
│   ├── test_collect_github.py
│   ├── test_rank_projects.py
│   └── fixtures/
├── docs/
│   ├── data_schema.md
│   ├── scoring_method.md
│   └── operations.md
├── requirements.txt
├── README.md
└── pyproject.toml                            # 可选
```

---

## 4. 外部依据与约束

### 4.1 Codex 自动化

Codex 可通过两条路径进入自动化流程：

1. GitHub Actions 内使用 `openai/codex-action@v1`。
2. 本地或服务器 cron 内使用 `codex exec` 非交互模式。

施工时优先使用 GitHub Actions，因为它更适合每天定时、自动提交报告和保留执行日志。

参考：

- Codex GitHub Action: https://developers.openai.com/codex/github-action
- Codex non-interactive mode: https://developers.openai.com/codex/noninteractive
- Codex CLI reference: https://developers.openai.com/codex/cli/reference
- Codex sandboxing: https://developers.openai.com/codex/concepts/sandboxing

### 4.2 GitHub Actions 定时

GitHub Actions 支持 `on.schedule` 使用 cron 语法定时触发。施工时按 JST 早上执行，建议先使用 UTC 换算，避免时区混乱。

建议默认时间：

```yaml
# 23:30 UTC = 08:30 JST
- cron: "30 23 * * *"
```

参考：

- GitHub Actions workflow syntax: https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions

### 4.3 GitHub API 限流

GitHub REST API 有 rate limit；认证请求额度高于匿名请求。搜索类端点通常更严格。因此采集脚本必须：

1. 使用认证 token。
2. 串行请求。
3. 每次请求之间 sleep。
4. 处理 `403`、`429`、`retry-after`、`x-ratelimit-reset`。
5. 保存 snapshot，不重复拉取无意义数据。
6. 不让 Codex 自己无限搜索。

参考：

- REST API rate limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- REST API best practices: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api

### 4.4 GH Archive 后续增强

第一版使用 GitHub API + 本地 snapshot 差分即可。若后续要做更接近“真实 24 小时涨星榜”的小时级统计，可接入 GH Archive 或 BigQuery。GH Archive 记录 GitHub public timeline，并提供 hourly archives；其 BigQuery 数据集也可用于更大规模分析。

参考：

- GH Archive: https://www.gharchive.org/
- GH Archive BigQuery README: https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md

---

## 5. 分阶段施工路线

## Phase 0：仓库初始化

### 目标

建立最小可运行项目骨架，让后续 Codex 能稳定修改。

### Codex 任务

1. 创建目录结构。
2. 创建 `README.md`。
3. 创建 `requirements.txt`。
4. 创建 `config/keywords.yml`。
5. 创建 `config/scoring.yml`。
6. 创建 `config/risk_rules.yml`。
7. 创建空的 `data/snapshots/.gitkeep` 和 `reports/daily/.gitkeep`。

### 验收标准

- `tree` 结构与第 3 节一致。
- `README.md` 说明项目用途、运行方式、风险声明。
- `requirements.txt` 至少包含：
  - `requests`
  - `pyyaml`
  - `python-dateutil`
  - `pydantic`，可选
  - `pytest`，可选

---

## Phase 1：关键词与分类配置

### 目标

把“金融圈项目”的搜索边界配置化，减少硬编码。

### 文件：`config/keywords.yml`

```yaml
topics:
  - algorithmic-trading
  - algo-trading
  - quantitative-finance
  - quant
  - trading-bot
  - backtesting
  - portfolio-optimization
  - market-making
  - arbitrage
  - crypto-trading
  - orderbook
  - risk-management
  - fintech
  - finance
  - stock-market
  - options-trading
  - forex
  - high-frequency-trading
  - machine-learning-trading
  - reinforcement-learning-trading

keywords:
  - quant
  - quantitative finance
  - algorithmic trading
  - algo trading
  - trading bot
  - backtest
  - backtesting
  - portfolio optimization
  - factor model
  - alpha model
  - risk model
  - market making
  - order book
  - orderbook
  - arbitrage
  - crypto trading
  - ai trading
  - reinforcement learning trading
  - options trading
  - volatility
  - fintech

languages:
  - Python
  - TypeScript
  - JavaScript
  - Rust
  - Go
  - C++
  - Java
  - Julia
  - R

exclude_keywords:
  - gambling
  - casino
  - get rich quick
  - guaranteed profit
  - paid signal
  - paid signals
  - signal group
  - martingale only
  - binary options
  - free money
  - pump
  - ponzi
  - referral
```

### Codex 注意事项

- 不要只搜索 crypto bot；要覆盖传统金融、量化研究、回测框架、数据工具、风控工具。
- `exclude_keywords` 不代表完全删除，而是用于风险标记和降权。
- 后续可以将关键词分组：`quant_research`、`trading_infra`、`risk`、`crypto`、`ai_agent`、`data_engineering`。

### 验收标准

- 配置文件 YAML 语法正确。
- 至少覆盖 15 个 topic、20 个关键词、8 种语言。
- 包含排除/风险关键词。

---

## Phase 2：GitHub 采集脚本

### 目标

实现 `scripts/collect_github.py`，从 GitHub Search API 拉取候选项目并保存 snapshot。

### 输入

```bash
python scripts/collect_github.py \
  --config config/keywords.yml \
  --out data/snapshots/2026-05-04.json
```

### 输出

`data/snapshots/YYYY-MM-DD.json`

### Snapshot schema

```json
{
  "generated_at": "2026-05-04T23:30:00+00:00",
  "query_count": 42,
  "count": 350,
  "items": [
    {
      "id": 123456,
      "full_name": "owner/repo",
      "owner": "owner",
      "name": "repo",
      "html_url": "https://github.com/owner/repo",
      "description": "...",
      "stars": 1234,
      "forks": 123,
      "watchers": 1234,
      "open_issues": 10,
      "language": "Python",
      "topics": ["trading", "backtesting"],
      "license": "MIT",
      "archived": false,
      "fork": false,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2026-05-04T00:00:00Z",
      "pushed_at": "2026-05-03T00:00:00Z",
      "matched_queries": ["topic:backtesting", "trading bot in:name,description,readme"]
    }
  ]
}
```

### 采集策略

1. 对每个 topic 生成查询：
   ```text
   topic:<topic> archived:false fork:false pushed:>YYYY-MM-DD
   ```
2. 对每个 keyword 生成查询：
   ```text
   <keyword> in:name,description,readme archived:false fork:false pushed:>YYYY-MM-DD
   ```
3. 按多个 sort 维度采集：
   - `stars`
   - `updated`
   - 可选：`forks`
4. 每个查询限制 `per_page=50` 或 `per_page=100`。
5. 使用 `full_name` 去重。
6. 同一个仓库若被多个 query 命中，合并到 `matched_queries`。
7. 默认只保留过去 18 个月内有 push 的仓库，可配置。

### 限流处理

采集脚本必须：

- 读取 `GITHUB_TOKEN`。
- 每次请求带：
  - `Accept: application/vnd.github+json`
  - `X-GitHub-Api-Version: 2022-11-28`
  - `Authorization: Bearer <token>`，如果 token 存在
- 解析响应头：
  - `x-ratelimit-remaining`
  - `x-ratelimit-reset`
  - `retry-after`
- 遇到 `403` / `429` 时等待或降级。
- 每个请求间隔 1-3 秒。
- 所有失败查询写入 `errors` 字段，但不要让单个失败导致全流程失败，除非结果为空。

### 伪代码

```python
def main():
    config = load_yaml(args.config)
    queries = build_queries(config)
    repos = {}
    errors = []

    for query in queries:
        for sort in ["stars", "updated"]:
            try:
                data = search_repositories(query=query, sort=sort, order="desc")
            except RateLimitError as e:
                wait_and_retry(e)
            except Exception as e:
                errors.append({"query": query, "sort": sort, "error": str(e)})
                continue

            for item in data["items"]:
                normalized = normalize_repo(item)
                merge_repo(repos, normalized, matched_query=query)

            sleep(config.request_sleep_seconds)

    write_snapshot(repos, errors)
```

### 验收标准

- 无 token 时可运行，但输出警告。
- 有 token 时使用认证请求。
- 输出 JSON 可被 `jq` 读取。
- 仓库去重正确。
- `matched_queries` 合并正确。
- 失败查询不会中断整体流程。

---

## Phase 3：排名和差分脚本

### 目标

实现 `scripts/rank_projects.py`，读取最近的 snapshot，计算涨星和综合热度，输出 `data/latest_candidates.json`。

### 输入

```bash
python scripts/rank_projects.py \
  --snapshot-dir data/snapshots \
  --out data/latest_candidates.json
```

### 输出 schema

```json
{
  "generated_at": "2026-05-04T23:40:00+00:00",
  "current_snapshot": "2026-05-04.json",
  "baseline_1d": "2026-05-03.json",
  "baseline_7d": "2026-04-27.json",
  "count": 80,
  "ranking_config": {
    "version": "v0.1"
  },
  "items": [
    {
      "rank": 1,
      "full_name": "owner/repo",
      "html_url": "https://github.com/owner/repo",
      "description": "...",
      "stars": 1234,
      "forks": 100,
      "star_delta_1d": 20,
      "star_delta_7d": 130,
      "star_delta_30d": null,
      "language": "Python",
      "topics": ["backtesting", "quant"],
      "created_at": "2024-01-01T00:00:00Z",
      "pushed_at": "2026-05-03T00:00:00Z",
      "matched_queries": ["topic:backtesting"],
      "category_guess": ["backtesting", "trading_infra"],
      "risk_flags": ["trading_bot", "crypto_related"],
      "hot_score": 52.3,
      "ranking_reasons": [
        "7 日涨星明显",
        "近期有 push",
        "与 backtesting topic 匹配"
      ]
    }
  ]
}
```

### 排名分类

最终候选集合从以下列表合并去重：

1. `top_by_total_stars`：总 star 最高。
2. `top_by_1d_growth`：24h 涨星最高。
3. `top_by_7d_growth`：7d 涨星最高。
4. `top_new_projects`：创建时间较近且增速明显。
5. `top_active_projects`：近期 push、issues 或 releases 活跃。
6. `watchlist_hits`：用户指定关注项目。

### 差分逻辑

如果昨日 snapshot 不存在：

- `star_delta_1d = null`
- 排名仍可依据总 stars 和活跃度生成。
- 报告中声明“暂无 1 日差分基线”。

如果 7 日前 snapshot 不存在：

- 使用最接近 7 日前的 snapshot。
- 若仍不存在，`star_delta_7d = null`。

### 建议评分公式 v0.1

`config/scoring.yml`：

```yaml
version: v0.1
weights:
  total_stars_log: 0.25
  forks_log: 0.10
  star_delta_1d: 0.25
  star_delta_7d: 0.25
  activity: 0.10
  freshness: 0.05

caps:
  star_delta_1d: 100
  star_delta_7d: 500
  activity_days: 90

penalties:
  archived: 100
  fork: 30
  no_push_over_365_days: 20
  suspicious_keyword: 15
  no_description: 5
```

示例：

```python
score = 0
score += 0.25 * log10(stars + 1) * 20
score += 0.10 * log10(forks + 1) * 20
score += 0.25 * min(star_delta_1d or 0, 100)
score += 0.25 * min((star_delta_7d or 0) / 5, 100)
score += 0.10 * activity_score
score += 0.05 * freshness_score
score -= risk_penalty
```

### 风险标记

`config/risk_rules.yml`：

```yaml
risk_keywords:
  high:
    - guaranteed profit
    - get rich quick
    - casino
    - binary options
    - pump
    - ponzi
  medium:
    - martingale
    - leverage
    - futures
    - crypto bot
    - grid trading
    - arbitrage bot
    - signal
  low:
    - backtesting
    - paper trading
    - sandbox

risk_flags:
  trading_bot:
    include_any:
      - trading bot
      - bot
      - auto trading
  crypto_related:
    include_any:
      - crypto
      - binance
      - bybit
      - okx
      - ccxt
  likely_research_tool:
    include_any:
      - backtest
      - research
      - factor
      - portfolio
```

### 验收标准

- 能处理只有 1 个 snapshot 的情况。
- 能正确计算 1d 和 7d 差分。
- 输出候选项目数量默认 50-100 个。
- 输出每个项目的 `ranking_reasons` 和 `risk_flags`。
- 排名结果稳定、可解释。

---

## Phase 4：Codex 报告生成 Prompt

### 目标

让 Codex 读取 `data/latest_candidates.json` 并生成一份中文 Markdown 报告。

### 文件：`.github/codex/prompts/daily_finance_radar.md`

```md
你是一个金融科技、量化交易、自动化交易、开源项目情报和工程架构分析助手。

请读取仓库中的 `data/latest_candidates.json`，生成一份中文 Markdown 报告。

报告目标：
帮助我从 GitHub 上近期最火、涨星最快、最值得关注的金融/量化/自动化交易项目中获取产品、技术架构、AI Agent、交易系统、数据工程和风控方面的灵感。

重要限制：
- 只基于 JSON 中的数据和仓库内已有文件分析。
- 不要编造 JSON 中不存在的 stars、涨星、语言、topic、URL。
- 如果信息不足，请明确写“信息不足”。
- 不要给投资建议。
- 不要建议直接运行未知 trading bot。
- 不要建议输入真实交易所 API key。
- 重点是工程灵感、产品灵感、架构灵感、研究方向灵感。

请严格输出 Markdown，结构如下：

# GitHub 金融/量化/自动化交易开源项目雷达 - {{今日日期}}

## 1. 今日摘要
- 今日最值得关注的 3 个方向
- 是否出现新趋势
- 是否出现值得复刻/参考的工程架构
- 是否有明显骗局、过度营销或高风险项目

## 2. 今日 Top 项目表
字段：
- 排名
- 项目
- stars
- 24h 涨星
- 7d 涨星
- 语言
- 主题/分类
- 一句话说明
- 灵感价值
- 风险等级

## 3. 重点项目深度分析
对 5～10 个最值得关注项目逐个分析：
- 项目解决什么问题
- 为什么最近值得关注
- 技术栈/架构亮点
- 是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中
- 可能的风险：金融合规、策略过拟合、API key 安全、回测造假、维护活跃度、依赖风险

## 4. 趋势归纳
从候选项目中总结：
- 技术趋势
- 产品趋势
- 量化/交易策略趋势
- AI Agent 与自动化交易结合趋势
- 值得后续做原型验证的方向

## 5. 今日灵感清单
给出 5～10 个可执行灵感，例如：
- 可以做一个什么 MVP
- 可以调研什么技术
- 可以让 Codex/Agent 自动复现什么 demo
- 哪些项目值得加入 watchlist

## 6. Watchlist 建议
列出建议加入 watchlist 的项目，并说明原因。

## 7. 风险提醒
必须强调：
- GitHub star 不是投资建议。
- 不运行未知 trading bot。
- 不泄露交易所 API key。
- 注意马丁、网格、套利、杠杆类项目的爆仓风险。
- 注意回测幸存者偏差和过拟合。

## 8. 数据质量说明
说明本次报告是否缺失 1 日/7 日基线，是否有采集失败，是否有样本偏差。
```

### Codex 输出要求

- 输出文件：`reports/daily/YYYY-MM-DD-finance-github-radar.md`
- 不要输出解释性前言。
- 不要包含 Codex 自己的运行日志。
- Markdown 表格不要过宽，必要时压缩字段。
- 对高风险项目要明确标记。

### 验收标准

- 报告存在。
- 报告标题包含日期。
- 报告至少包含 8 个章节。
- 报告包含风险提醒。
- 报告不编造不存在的涨星数据。
- 报告可被 Markdown 渲染器正常显示。

---

## Phase 5：GitHub Actions 自动化

### 目标

每天自动采集、排名、生成报告并提交到仓库。

### 文件：`.github/workflows/daily-radar.yml`

```yaml
name: Daily GitHub Finance Radar

on:
  schedule:
    # 23:30 UTC = 08:30 JST
    - cron: "30 23 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  radar:
    runs-on: ubuntu-latest

    env:
      TZ: Asia/Tokyo
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

    steps:
      - name: Checkout
        uses: actions/checkout@v5

      - name: Set date
        id: date
        run: echo "today=$(date +%F)" >> "$GITHUB_OUTPUT"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Collect GitHub repositories
        run: |
          python scripts/collect_github.py \
            --config config/keywords.yml \
            --out data/snapshots/${{ steps.date.outputs.today }}.json

      - name: Rank candidate projects
        run: |
          python scripts/rank_projects.py \
            --snapshot-dir data/snapshots \
            --out data/latest_candidates.json

      - name: Generate report with Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/daily_finance_radar.md
          output-file: reports/daily/${{ steps.date.outputs.today }}-finance-github-radar.md
          sandbox: workspace-write
          safety-strategy: drop-sudo

      - name: Commit report and data
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add data reports
          git commit -m "daily finance radar ${{ steps.date.outputs.today }}" || exit 0
          git push
```

### 必要 secrets

在 GitHub 仓库设置中添加：

- `OPENAI_API_KEY`

GitHub Actions 自带：

- `GITHUB_TOKEN`

### 验收标准

- 手动触发 `workflow_dispatch` 能成功执行。
- 生成 snapshot。
- 生成 `data/latest_candidates.json`。
- 生成 daily report。
- 自动 commit。
- 不把 API key 打印到日志中。

---

## Phase 6：本地或服务器 cron 备选方案

### 目标

如果不用 GitHub Actions，可以在本地 Mac、Ubuntu、EC2、VPS 或 NAS 上定时运行。

### 文件：`scripts/run_daily.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

export TZ=Asia/Tokyo
TODAY=$(date +%F)

mkdir -p logs data/snapshots reports/daily

git pull --rebase || true

python scripts/collect_github.py \
  --config config/keywords.yml \
  --out data/snapshots/${TODAY}.json

python scripts/rank_projects.py \
  --snapshot-dir data/snapshots \
  --out data/latest_candidates.json

codex exec \
  --cd . \
  --sandbox workspace-write \
  "读取 data/latest_candidates.json，并按照 .github/codex/prompts/daily_finance_radar.md 生成中文 Markdown 报告，写入 reports/daily/${TODAY}-finance-github-radar.md。"

git add data reports
git commit -m "daily finance radar ${TODAY}" || true
git push || true
```

### crontab

```bash
30 8 * * * cd /opt/github-finance-radar && bash scripts/run_daily.sh >> logs/daily.log 2>&1
```

### 验收标准

- `bash scripts/run_daily.sh` 本地可跑。
- `logs/daily.log` 有日志。
- 输出文件路径正确。

---

## Phase 7：测试与质量门槛

### 目标

减少每日任务因为小错误中断。

### 单元测试建议

`tests/test_rank_projects.py`：

1. 只有当天 snapshot 时不崩溃。
2. 有昨天 snapshot 时能算 `star_delta_1d`。
3. 有 7 天前 snapshot 时能算 `star_delta_7d`。
4. 仓库在昨天不存在时，delta 处理合理。
5. 风险关键词能正确标记。
6. archived/fork 项目被降权或过滤。

`tests/test_collect_github.py`：

1. query 构造正确。
2. normalize repo 正确。
3. matched_queries 能合并。
4. rate limit 解析不报错。

### 报告验证脚本：`scripts/validate_report.py`

检查：

1. 文件存在。
2. 标题存在。
3. 至少包含 8 个章节。
4. 包含“不是投资建议”或类似风险提示。
5. 不含明显空模板，如 `{{今日日期}}`。

### GitHub Actions 中加入测试

```yaml
- name: Run tests
  run: pytest -q

- name: Validate report
  run: |
    python scripts/validate_report.py \
      reports/daily/${{ steps.date.outputs.today }}-finance-github-radar.md
```

---

## Phase 8：通知与知识库集成，可选

### 目标

让报告不只停留在 GitHub 仓库里，而是主动推送给用户。

### 选项

1. 邮件：SendGrid、AWS SES、Gmail SMTP。
2. 企业微信/飞书/Slack webhook。
3. Telegram bot。
4. Notion database。
5. Obsidian vault：通过 git sync。
6. RSS：生成 `reports/feed.xml`。

### 建议优先级

第一优先：GitHub report。  
第二优先：Telegram 或企业微信短摘要。  
第三优先：Obsidian/Notion 长期知识库。

### 通知内容建议

```text
今日 GitHub 金融/量化雷达已生成：
- 新增候选项目：N 个
- 24h 涨星最高：owner/repo +X
- 今日最值得关注方向：...
- 报告链接：...
```

---

## Phase 9：GH Archive / BigQuery 增强，可选

### 目标

用 GH Archive 的 WatchEvent 数据更准确地计算过去 24 小时 star 增长。

### 适合什么时候做

- GitHub Search API + 本地 snapshot 不够精确。
- 想发现“今天刚爆”的项目。
- 想统计全 GitHub 范围的 star 事件，而不是只看关键词搜索结果。

### 增强思路

1. 用 BigQuery 查询最近 24 小时 `WatchEvent`。
2. 按 repo 聚合 star 事件数量。
3. 用关键词/topic/README 二次过滤金融相关项目。
4. 与现有候选项目合并。

### 风险

- BigQuery 有成本。
- WatchEvent 中 repo 需要再 enrichment。
- 金融相关性过滤更复杂。
- 首版不建议引入。

---

## 6. 数据模型细节

### 6.1 RepoSnapshotItem

建议用 Pydantic 或 dataclass 定义：

```python
class RepoSnapshotItem(BaseModel):
    id: int
    full_name: str
    owner: str
    name: str
    html_url: str
    description: str | None = None
    stars: int = 0
    forks: int = 0
    watchers: int = 0
    open_issues: int = 0
    language: str | None = None
    topics: list[str] = []
    license: str | None = None
    archived: bool = False
    fork: bool = False
    created_at: str
    updated_at: str
    pushed_at: str | None = None
    matched_queries: list[str] = []
```

### 6.2 CandidateItem

```python
class CandidateItem(RepoSnapshotItem):
    rank: int
    star_delta_1d: int | None = None
    star_delta_7d: int | None = None
    star_delta_30d: int | None = None
    category_guess: list[str] = []
    risk_flags: list[str] = []
    hot_score: float
    ranking_reasons: list[str] = []
```

---

## 7. 分类逻辑建议

### 7.1 分类标签

建议 Codex 和 Python 都围绕以下类别理解项目：

```yaml
categories:
  backtesting:
    keywords: [backtest, backtesting, strategy test]
  trading_bot:
    keywords: [trading bot, bot, auto trading, automated trading]
  quant_research:
    keywords: [quant, factor, alpha, research, portfolio]
  trading_infra:
    keywords: [order book, market data, execution, exchange, broker]
  risk_management:
    keywords: [risk, var, volatility, exposure, hedge]
  crypto_trading:
    keywords: [crypto, binance, bybit, okx, ccxt]
  ai_trading:
    keywords: [ai trading, machine learning, reinforcement learning, llm]
  data_engineering:
    keywords: [market data, data pipeline, etl, feature store]
  fintech_product:
    keywords: [fintech, payment, banking, personal finance]
```

### 7.2 分类依据

分类时从以下字段聚合文本：

```text
full_name + description + topics + matched_queries + README 摘要，后续可选
```

---

## 8. 风险控制与安全约束

### 8.1 对 Codex 的硬性安全要求

Codex 在本项目中必须遵守：

1. 不 clone 并运行未知 trading bot。
2. 不执行候选仓库中的安装脚本。
3. 不读取、不生成、不提交任何真实交易 API key。
4. 不把项目热度解释为投资收益可能性。
5. 不建议用户直接使用高杠杆、马丁、网格、套利类项目实盘。
6. 不隐藏数据不足问题。
7. 不编造涨星数据。

### 8.2 报告中的风险等级

建议分为：

- `低`：研究框架、数据工具、回测框架、教育工具。
- `中`：自动交易工具、交易所 SDK、crypto bot、策略生成器。
- `高`：声称稳赚、马丁、杠杆、信号群、套利机器人、需要 API key 的闭源/不透明项目。

### 8.3 风险提示模板

每份报告末尾必须包含：

```md
> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。
```

---

## 9. Codex 可直接执行的任务拆分

下面这些 prompt 可以逐条交给 Codex 执行。

### Task 1：初始化项目

```text
请在当前仓库中初始化 github-finance-radar 项目骨架：创建 .github/workflows、.github/codex/prompts、config、scripts、data/snapshots、reports/daily、tests、docs 等目录；创建 README.md、requirements.txt、config/keywords.yml、config/scoring.yml、config/risk_rules.yml。要求所有文件内容符合 docs/github_finance_radar_construction_plan.md 的 Phase 0 和 Phase 1 规范。
```

### Task 2：实现采集脚本

```text
请实现 scripts/collect_github.py。它需要读取 config/keywords.yml，调用 GitHub Search API 搜索金融、量化、自动交易相关仓库，保存 data/snapshots/YYYY-MM-DD.json。要求支持 GITHUB_TOKEN、限流处理、错误记录、仓库去重、matched_queries 合并、命令行参数 --config 和 --out。不要运行任何候选仓库代码。
```

### Task 3：实现排名脚本

```text
请实现 scripts/rank_projects.py。它需要读取 data/snapshots 下的快照，选择当前快照、1 日基线、7 日基线，计算 star_delta_1d、star_delta_7d、hot_score、risk_flags、category_guess、ranking_reasons，并输出 data/latest_candidates.json。要求只有一个 snapshot 时也能运行。
```

### Task 4：实现测试

```text
请为 collect_github.py 和 rank_projects.py 添加 pytest 测试。重点测试 query 构造、仓库去重、matched_queries 合并、缺少基线时的差分处理、风险关键词标记、hot_score 排序稳定性。使用 tests/fixtures 中的假数据，不要调用真实 GitHub API。
```

### Task 5：实现 Codex 报告 prompt

```text
请创建 .github/codex/prompts/daily_finance_radar.md。这个 prompt 要求 Codex 读取 data/latest_candidates.json，生成中文 Markdown 报告，结构包括今日摘要、Top 项目表、重点项目分析、趋势归纳、今日灵感清单、Watchlist 建议、风险提醒、数据质量说明。要求明确禁止编造 JSON 中不存在的数据，禁止投资建议。
```

### Task 6：实现 GitHub Actions

```text
请创建 .github/workflows/daily-radar.yml。工作流每天 JST 08:30 运行，也支持 workflow_dispatch。步骤包括 checkout、setup-python、install requirements、collect、rank、用 openai/codex-action@v1 生成报告、commit data 和 reports。使用 secrets.OPENAI_API_KEY，不要打印密钥。
```

### Task 7：实现报告验证

```text
请实现 scripts/validate_report.py，并把它加入 GitHub Actions。验证报告文件存在、标题包含日期、包含 8 个主要章节、包含风险提醒、不含未替换模板变量。验证失败时让 workflow 失败。
```

### Task 8：README 和运维文档

```text
请完善 README.md 和 docs/operations.md，说明如何本地运行、如何配置 GitHub Secrets、如何手动触发 workflow、如何查看报告、如何调整关键词、如何处理 GitHub API 限流、如何排查 Codex 生成失败。
```

---

## 10. Codex Skill 可选配置

如果需要让 Codex 长期稳定维护本项目，可添加 Skill。

文件：`.agents/skills/github-finance-radar/SKILL.md`

```md
---
name: github-finance-radar
description: 用于维护和运行每日 GitHub 金融、量化、自动化交易项目雷达，包含采集、排名、去噪、风险标记和 Markdown 报告生成。
---

当用户要求生成、维护或调试 GitHub 金融/量化/自动化交易项目雷达时：

1. 优先阅读 docs/github_finance_radar_construction_plan.md、config/keywords.yml、config/scoring.yml、config/risk_rules.yml。
2. 使用 scripts/collect_github.py 采集候选项目。
3. 使用 scripts/rank_projects.py 计算 star_delta_1d、star_delta_7d 和 hot_score。
4. 读取 data/latest_candidates.json。
5. 生成 reports/daily/YYYY-MM-DD-finance-github-radar.md。
6. 报告必须强调工程灵感，不输出投资建议。
7. 不运行未知仓库代码，不克隆可疑 trading bot，不读取任何交易所 API key。
8. 若数据不足，明确写数据不足，不编造。
```

---

## 11. README 初稿结构

`README.md` 应包含：

~~~md
# GitHub Finance Radar

每日 GitHub 金融、量化、自动化交易开源项目雷达。

## 功能

- 收集 GitHub 金融/量化/自动化交易相关项目
- 计算 24h / 7d 涨星
- 识别热门项目、快速增长项目、新项目
- 用 Codex 生成中文 Markdown 报告
- 自动保存到 reports/daily

## 快速开始

```bash
pip install -r requirements.txt
python scripts/collect_github.py --config config/keywords.yml --out data/snapshots/$(date +%F).json
python scripts/rank_projects.py --snapshot-dir data/snapshots --out data/latest_candidates.json
```

## GitHub Actions

设置 secret：

- OPENAI_API_KEY

然后手动运行 Daily GitHub Finance Radar workflow。

## 风险声明

本项目不构成投资建议。不要直接运行未知 trading bot，不要泄露交易所 API Key。
~~~

---

## 12. 运行与排错手册

### 12.1 手动运行采集

```bash
export GITHUB_TOKEN=ghp_xxx
python scripts/collect_github.py \
  --config config/keywords.yml \
  --out data/snapshots/$(date +%F).json
```

### 12.2 手动运行排名

```bash
python scripts/rank_projects.py \
  --snapshot-dir data/snapshots \
  --out data/latest_candidates.json
```

### 12.3 手动运行 Codex 报告

```bash
codex exec \
  --cd . \
  --sandbox workspace-write \
  "读取 data/latest_candidates.json，按照 .github/codex/prompts/daily_finance_radar.md 生成中文 Markdown 报告。"
```

### 12.4 常见问题

#### 问题：GitHub API rate limit

处理：

1. 确认 `GITHUB_TOKEN` 存在。
2. 降低 query 数量。
3. 增加 sleep。
4. 减少 `per_page`。
5. 查看响应头 `x-ratelimit-reset`。

#### 问题：没有 1d / 7d 差分

原因：snapshot 历史不足。  
处理：继续运行几天即可。报告中需要说明“暂无基线”。

#### 问题：Codex 报告编造数据

处理：强化 prompt，加入“只基于 JSON 输出，不得编造”。加入 `validate_report.py` 只能做结构验证，不能完全防止语义编造；必要时让 Codex 在报告末尾输出“数据字段来源说明”。

#### 问题：crypto bot 噪音过多

处理：

1. 提高 `exclude_keywords` 权重。
2. 把 `crypto_trading` 单独分组。
3. 在报告中分离“研究/基础设施”和“高风险交易机器人”。

---

## 13. 最小可用版本定义

MVP 完成标准：

1. 手动运行能生成 snapshot。
2. 手动运行能生成 `latest_candidates.json`。
3. GitHub Actions 手动触发成功。
4. Codex 能生成中文日报。
5. 报告中包含 Top 项目、趋势、灵感、风险提醒。
6. 仓库至少连续运行 7 天后，能看到 7 日涨星榜。

---

## 14. 后续增强路线

### v0.2

- 增加 README 摘要抓取。
- 增加 release 活跃度。
- 增加 issue/PR 活跃度。
- 增加 watchlist/ignorelist。
- 增加报告验证。

### v0.3

- 接入 GH Archive 或 BigQuery。
- 增加真实 24 小时 WatchEvent 排行。
- 增加项目趋势曲线。
- 增加周报。

### v0.4

- 增加通知系统。
- 推送到 Obsidian/Notion。
- 对重点项目生成单独深度分析。

### v0.5

- 构建“灵感 backlog”：把报告中的 MVP 灵感自动转成 GitHub issues。
- 让 Codex 对某个灵感生成 proof-of-concept 项目骨架。
- 增加安全沙箱，只允许分析代码，不允许运行候选项目。

---

## 15. 交付物清单

Codex 最终应交付：

```text
.github/workflows/daily-radar.yml
.github/codex/prompts/daily_finance_radar.md
config/keywords.yml
config/scoring.yml
config/risk_rules.yml
scripts/collect_github.py
scripts/rank_projects.py
scripts/validate_report.py
data/snapshots/.gitkeep
reports/daily/.gitkeep
tests/test_collect_github.py
tests/test_rank_projects.py
README.md
docs/operations.md
docs/data_schema.md
docs/scoring_method.md
```

---

## 16. 最终给 Codex 的总控 Prompt

当你准备让 Codex 一次性开始施工时，可以使用下面这段：

```text
你现在要在当前仓库中实现一个名为 GitHub Finance Radar 的自动化系统。请完整阅读 docs/github_finance_radar_construction_plan.md，然后按 Phase 0 到 Phase 5 实现 MVP。

目标：每天自动收集 GitHub 上金融、量化、自动化交易、回测、投资组合优化、风控、AI Trading 等相关开源项目，保存 snapshot，计算 24h/7d 涨星和 hot_score，然后使用 Codex 生成中文 Markdown 报告。

硬性要求：
1. Python 负责采集、清洗、差分、排名。
2. Codex 只负责读取 data/latest_candidates.json 并生成报告。
3. 不运行未知候选仓库代码。
4. 不处理真实交易 API key。
5. 不提供投资建议。
6. 所有输出必须可复现、可审计。
7. GitHub Actions 需要支持 workflow_dispatch 和每天 JST 08:30 定时运行。
8. 使用 secrets.OPENAI_API_KEY 和 GITHUB_TOKEN。
9. 添加基本 pytest 测试。
10. 完成后运行测试，并总结改动、运行方式和后续建议。
```

---

## 17. 施工优先级总结

优先做：

1. `keywords.yml`
2. `collect_github.py`
3. `rank_projects.py`
4. `daily_finance_radar.md`
5. `daily-radar.yml`
6. `README.md`

后做：

1. GH Archive
2. README 摘要 enrichment
3. 通知系统
4. Watchlist/ignorelist UI
5. 自动生成 issues/MVP backlog

最终判断标准：

> 每天早上打开仓库，就能看到一份结构化中文报告，知道最近金融/量化/自动化交易开源生态里哪些项目变热、为什么值得看、可以给自己的工程和产品带来什么灵感、哪些东西不能碰。
