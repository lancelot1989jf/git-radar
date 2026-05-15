# GitHub Finance Radar

每日 GitHub 金融、量化、自动化交易开源项目雷达。

本项目自动收集 GitHub 上金融、量化、自动化交易、回测、投资组合优化、风控、AI Trading 等相关开源项目，保存每日 snapshot，计算 24h/7d 涨星与 `hot_score`，再交给 DeepSeek V4Pro 基于 `data/latest_candidates.json` 生成中文 Markdown 报告。旧的 OpenAI/Codex 报告生成方式保留为手动 workflow。

## 功能

- 使用 Python 采集、清洗、去重 GitHub Search API 结果。
- 保存 `data/snapshots/YYYY-MM-DD.json`，保留查询命中与失败信息。
- 计算 `star_delta_1d`、`star_delta_7d`、`hot_score`、分类与风险标记。
- 使用 DeepSeek V4Pro 只读取结构化 JSON，生成中文日报到 `reports/daily/`。
- 保留 OpenAI/Codex 手动报告生成路径，便于按需对比。
- GitHub Actions 支持手动触发和每天北京时间 08:30 自动运行。

## 快速开始

本项目的本地虚拟环境放在外置盘：

```bash
/Volumes/贾帆工作/devtools/envs/git-radar/bin/python -m pip install -r requirements.txt
source .venv/bin/activate
```

仓库内的 `.venv` 是指向 `/Volumes/贾帆工作/devtools/envs/git-radar` 的便捷链接，不存放真实环境内容。安装依赖时建议使用外置盘 pip 缓存：

```bash
export PIP_CACHE_DIR=/Volumes/贾帆工作/devtools/pip-cache
```

```bash
.venv/bin/python scripts/collect_github.py --config config/keywords.yml --out data/snapshots/$(date +%F).json
.venv/bin/python scripts/rank_projects.py --snapshot-dir data/snapshots --out data/latest_candidates.json
.venv/bin/python -m pytest -q
```

无 `GITHUB_TOKEN` 时，可用小样本 smoke 配置检查端到端链路：

```bash
.venv/bin/python scripts/collect_github.py --config config/keywords.smoke.yml --out data/snapshots/$(date +%F).json
```

有 `GITHUB_TOKEN` 时会使用认证请求，额度更稳定：

```bash
export GITHUB_TOKEN=ghp_xxx
```

也可以使用 GitHub CLI 登录。本地未设置 `GITHUB_TOKEN` 时，采集脚本会自动尝试读取 `gh auth token`，但不会打印 token：

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth status
```

## GitHub Actions

在 GitHub 仓库设置中添加：

- `DEEPSEEK_API_KEY`：每日云端定时报告生成使用。
- `OPENAI_API_KEY`：可选，仅手动运行旧 Codex workflow 时使用。

工作流 `.github/workflows/daily-radar.yml` 会使用 GitHub 自动提供的 `GITHUB_TOKEN`，并在每天北京时间 08:30 或手动 `workflow_dispatch` 时运行采集、排名、DeepSeek 报告生成和自动提交。

旧方法保留在 `.github/workflows/manual-codex-radar.yml`，只支持手动 `workflow_dispatch`，使用 `OPENAI_API_KEY` 和原有 Codex prompt。

## 输出文件

- `data/snapshots/YYYY-MM-DD.json`：每日原始候选仓库 snapshot。
- `data/latest_candidates.json`：排名后的候选项目，供 DeepSeek 或 Codex 报告读取。
- `data/report_runs/YYYY-MM-DD-deepseek.json`：DeepSeek 报告生成审计元数据。
- `reports/daily/YYYY-MM-DD-finance-github-radar.md`：中文日报。

## 文档

- `docs/data_schema.md`：snapshot 和候选项目 JSON 结构。
- `docs/scoring_method.md`：`hot_score`、delta 和风险标记口径。
- `docs/operations.md`：本地运行、GitHub Actions 和排错说明。

## 风险声明

本项目只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。
