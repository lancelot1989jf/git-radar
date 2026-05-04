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

- `OPENAI_API_KEY`

`GITHUB_TOKEN` 由 GitHub Actions 自动提供，并映射给采集脚本使用。

工作流：

- 手动触发：`workflow_dispatch`
- 定时触发：`30 23 * * *`，即 JST 08:30

## Common Issues

### GitHub API rate limit

处理：

- 确认 `GITHUB_TOKEN` 存在。
- 减少 `config/keywords.yml` 中的关键词或 topic。
- 增大 `request_sleep_seconds`。
- 降低 `per_page`。

### Missing 1d or 7d baseline

原因是 snapshot 历史不足。系统会继续输出候选项目，对应 delta 为 `null`，报告需要说明数据不足。

### Codex report has invented data

报告 prompt 已要求只基于 `data/latest_candidates.json`。如果仍出现编造，需要收紧 prompt，并在人工 review 时以 JSON 为准。

### Current directory is not a git repository

本地目录当前没有 `.git`。GitHub Actions 的 commit/push 逻辑只有在该目录进入真实 GitHub 仓库后才能端到端验证。
