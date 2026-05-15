# Operations

## Local Python Environment

本项目的独立 Python 虚拟环境放在外置盘，实体路径：

```bash
/Volumes/贾帆工作/devtools/envs/git-radar
```

仓库内 `.venv` 是指向该目录的 symlink。

推荐运行前设置外置盘 pip 缓存：

```bash
export PIP_CACHE_DIR=/Volumes/贾帆工作/devtools/pip-cache
source .venv/bin/activate
```

安装依赖：

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Manual Run

采集：

```bash
export GITHUB_TOKEN=ghp_xxx
.venv/bin/python scripts/collect_github.py \
  --config config/keywords.yml \
  --out data/snapshots/$(date +%F).json
```

也可以使用 GitHub CLI 登录。本地未设置 `GITHUB_TOKEN` 时，采集脚本会自动尝试读取 `gh auth token`，不打印 token：

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth status
```

排名：

```bash
.venv/bin/python scripts/rank_projects.py \
  --snapshot-dir data/snapshots \
  --out data/latest_candidates.json
```

测试：

```bash
.venv/bin/python -m pytest -q
PYTHONPYCACHEPREFIX=.pycache_runtime .venv/bin/python -m compileall scripts tests
```

## GitHub Actions

需要设置 secret：

- `DEEPSEEK_API_KEY`：每日云端定时报告生成使用。
- `OPENAI_API_KEY`：可选，仅手动运行旧 Codex workflow 时使用。

`GITHUB_TOKEN` 由 GitHub Actions 自动提供，并映射给采集脚本使用。

工作流：

- `.github/workflows/daily-radar.yml`：DeepSeek V4Pro 路径，支持 `workflow_dispatch`，并每天 `30 0 * * *` 触发，即北京时间 08:30；默认报告日期为前一天。
- `.github/workflows/manual-codex-radar.yml`：旧 OpenAI/Codex 路径，仅支持手动 `workflow_dispatch`。

DeepSeek 报告生成脚本也可以本地调用：

```bash
export DEEPSEEK_API_KEY=sk-xxx
.venv/bin/python scripts/generate_report_deepseek.py \
  --input data/latest_candidates.json \
  --prompt .github/deepseek/prompts/daily_finance_radar.md \
  --out reports/daily/$(date +%F)-finance-github-radar.md \
  --metadata-out data/report_runs/$(date +%F)-deepseek.json
```

## Common Issues

### GitHub API rate limit

处理：

- 确认 `GITHUB_TOKEN` 存在。
- 减少 `config/keywords.yml` 中的关键词或 topic。
- 增大 `request_sleep_seconds`。
- 降低 `per_page`。

### Missing 1d or 7d baseline

原因是 snapshot 历史不足。系统会继续输出候选项目，对应 delta 为 `null`，报告需要说明数据不足。

### Report has invented data

报告 prompt 已要求只基于 `data/latest_candidates.json`。如果仍出现编造，需要收紧 DeepSeek/Codex prompt，并在人工 review 时以 JSON 为准。

### DeepSeek API key missing

如果云端日志显示 `missing required environment variable: DEEPSEEK_API_KEY`，需要在 GitHub 仓库 Settings -> Secrets and variables -> Actions 中添加 repository secret `DEEPSEEK_API_KEY`。
