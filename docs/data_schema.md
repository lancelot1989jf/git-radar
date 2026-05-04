# Data Schema

本项目所有中间结果都落盘为 JSON，便于复现、审计和调试。Python 负责生成这些结构化数据；Codex 只读取 `data/latest_candidates.json` 生成报告。

## Snapshot

路径：`data/snapshots/YYYY-MM-DD.json`

字段：

- `generated_at`：UTC ISO 时间。
- `query_count`：构造出的 GitHub Search 查询数量。
- `request_count`：实际请求次数，等于 query 与 sort 组合数。
- `count`：去重后的仓库数量。
- `items`：仓库元数据列表。
- `errors`：失败查询列表。单个查询失败不阻断整体流程，除非最终没有任何候选仓库。

`items[]` 主要字段：

- `id`
- `full_name`
- `owner`
- `name`
- `html_url`
- `description`
- `stars`
- `forks`
- `watchers`
- `open_issues`
- `language`
- `topics`
- `license`
- `archived`
- `fork`
- `created_at`
- `updated_at`
- `pushed_at`
- `matched_queries`

## Latest Candidates

路径：`data/latest_candidates.json`

字段：

- `generated_at`：UTC ISO 时间。
- `current_snapshot`：当前参与排名的 snapshot 文件名。
- `baseline_1d`：1 日基线 snapshot 文件名，缺失时为 `null`。
- `baseline_7d`：7 日基线 snapshot 文件名，缺失时为 `null`。
- `count`：输出候选数量。
- `ranking_config`：评分配置摘要。
- `items`：排名后的候选项目。

`items[]` 在 snapshot 字段基础上增加：

- `rank`
- `star_delta_1d`
- `star_delta_7d`
- `star_delta_30d`
- `category_guess`
- `risk_flags`
- `risk_level`
- `hot_score`
- `ranking_reasons`

## Data Safety

- 不 clone、不安装、不运行候选仓库代码。
- 不读取、不生成、不提交真实交易 API key。
- 不将 GitHub star 或涨星解释为收益信号。
