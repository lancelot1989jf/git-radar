# Scoring Method

评分配置位于 `config/scoring.yml`，当前版本为 `v0.1`。排名只基于本地 snapshot 和配置文件，保证同一输入可以复现同一输出。

## Inputs

每个候选仓库使用以下字段参与评分：

- `stars`
- `forks`
- `star_delta_1d`
- `star_delta_7d`
- `pushed_at`
- `created_at`
- `description`
- `archived`
- `fork`
- 聚合文本中的风险关键词

## Hot Score

评分由以下部分组成：

- 总 star 的 log 分。
- fork 的 log 分。
- 24h 涨星分。
- 7d 涨星分。
- 近期 push 活跃度分。
- 创建时间新鲜度分。
- archived、fork、长期无 push、无描述、风险关键词等扣分。

缺少 1 日或 7 日基线时，对应 delta 为 `null`，该项按 0 分处理，报告的数据质量说明应明确基线缺失。

## Candidate Buckets

最终候选集合从多个榜单合并去重：

- 总 star 最高。
- 24h 涨星最高。
- 7d 涨星最高。
- 创建时间较近的新项目。
- 近期 push 活跃项目。

合并后按 `hot_score`、`stars`、`full_name` 稳定排序。

## Risk Flags

风险规则位于 `config/risk_rules.yml`。风险标记只用于报告和降权，不代表项目一定不可用，也不代表任何投资判断。

风险等级口径：

- `高`：包含明显高风险或过度营销词，例如稳赚、pump、ponzi。
- `中`：包含自动交易、crypto、杠杆、网格、套利 bot 等风险上下文。
- `低`：偏研究、回测、数据、工具类项目。
