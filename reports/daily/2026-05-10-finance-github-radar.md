# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-10

## 1. 今日摘要

- 本轮按要求标记为 `2026-05-10` 报告落盘；实际采集生成时间为 `2026-05-11T00:46:31+00:00`。
- 完整采集使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3844 个去重候选、1 个采集错误。
- 当前 snapshot 为 `2026-05-10.json`；由于本地没有 `2026-05-09.json`，1 日基线缺失，所有 24h delta 均为 `N/A`。
- 7 日字段基线为 `2026-05-04.json`。按文件日期看，它更接近 6 日跨度；本报告只把它作为当前可用历史下的近似 7d 趋势字段。
- 近 7d 字段中最强的候选包括 `nexu-io/open-design +13310`、`ruvnet/ruflo +7790`、`TauricResearch/TradingAgents +6409`、`VoltAgent/awesome-design-md +4009`、`public-apis/public-apis +2677`。
- 金融/量化/AI Trading 相关性较高的重点项目包括 `TradingAgents`、`Vibe-Trading`、`QuantDinger`、`daily_stock_analysis`、`Kronos`、`FinceptTerminal`、`qlib`、`OpenBB`、`freqtrade`。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 433855 | N/A | +2677 | Python | crypto_trading, quant_research | API 目录化与数据源发现参考，金融相关性需二次确认 | 中 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 74841 | N/A | +4009 | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性偏弱 | 中 |
| 3 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 36186 | N/A | +13310 | TypeScript | fintech_product | 金融研究终端、报告页、仪表盘原型生成参考 | 低 |
| 4 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 73204 | N/A | +6409 | Python | ai_trading, backtesting, quant_research, risk_management | 多 Agent 金融交易研究框架，本轮核心观察对象 | 低 |
| 5 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 48480 | N/A | +7790 | TypeScript | ai_trading, backtesting | Agent 编排平台，适合映射到金融研究自动化流程 | 低 |
| 6 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 76470 | N/A | +2658 | Python | fintech_product | UI/UX agent skill 参考，偏产品原型而非金融核心 | 低 |
| 7 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | 73440 | N/A | +2175 | Python | risk_management | 安全工具样本，金融相关性弱但提示噪音问题 | 低 |
| 8 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 6780 | N/A | +1859 | Python | ai_trading, backtesting, crypto_trading, fintech_product, quant_research | personal trading agent 产品形态，需风险隔离 | 中 |
| 9 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | 4458 | N/A | +1502 | Python | ai_trading, backtesting, crypto_trading, data_engineering, quant_research, trading_bot, trading_infra | AI 量化/交易基础设施候选，高风险观察对象 | 中 |
| 10 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 57004 | N/A | +1277 | TypeScript | quant_research | Agent harness 和工作流组织参考 | 低 |

## 3. 重点项目深度分析

### TauricResearch/TradingAgents

`TradingAgents` 本轮 7d 字段约 +6409，仍是 AI Trading 与金融 Agent 交叉方向的核心观察对象。它的价值在于观察多 Agent 如何拆分研究、观点生成、交叉质询、风控判断和结论记录。不要把它当作可直接执行的交易系统，更适合作为研究流程编排、审计链路和报告生成的架构参考。

### HKUDS/Vibe-Trading

`Vibe-Trading` 本轮 7d 字段约 +1859，描述为 personal trading agent，分类同时覆盖 AI trading、backtesting、crypto trading、fintech product 和 quant research。它说明 AI trading 叙事正在从“研究辅助”靠近“个人交易助理”。这个方向值得观察交互边界、状态解释和风险提示，但不应接入真实交易 API key。

### brokermr810/QuantDinger

`QuantDinger` 本轮 7d 字段约 +1502，分类命中 AI trading、backtesting、crypto trading、data engineering、quant research、trading bot 和 trading infra。它和本 Radar 的主题高度相关，也因此更需要风险隔离。可以研究模块划分、回测/实盘边界、数据流和多 Agent 研究链路，不能直接运行其交易功能。

### ZhuLinsen/daily_stock_analysis

`daily_stock_analysis` 本轮 7d 字段约 +1046，覆盖 A/H/美股行情、实时新闻、LLM 分析仪表盘、多渠道推送和定时运行。它是自动化金融观察系统的产品闭环样本，但输出内容容易被误读为投资建议，必须保留数据来源、时间戳、模型说明和免责声明。

### shiyu-coder/Kronos

`Kronos` 本轮 7d 字段约 +1173，描述为面向金融市场语言的 foundation model。它代表市场数据与基础模型结合的方向，后续值得关注训练数据、评测协议、推理接口、复现方式和误用边界。

### Fincept-Corporation/FinceptTerminal

`FinceptTerminal` 本轮 7d 字段约 +1032，是金融分析终端产品参考，覆盖 market analytics、investment research 和 economic data tools。它适合观察金融数据探索、研究工作台、可视化和用户体验如何组合。

### microsoft/qlib 与 OpenBB-finance/OpenBB

`qlib` 本轮 7d 字段约 +522，`OpenBB` 本轮 7d 字段约 +375。两者是更稳定的金融/量化基础设施样本：`qlib` 偏 AI-oriented quant research 和建模生产化，`OpenBB` 偏金融数据平台和 AI agent 数据入口。它们适合进入长期 watchlist，不一定需要依赖短期热度排序。

### nexu-io/open-design 与 ruvnet/ruflo

`open-design` 本轮 7d 字段约 +13310，`ruflo` 本轮 7d 字段约 +7790，是热度最强的两类通用 Agent/UI 候选。它们不是金融/量化核心项目，但对金融 Radar 的报告生成、研究终端原型、Agent 编排和工作流可视化有间接工程价值。它们也再次证明：当前排名需要把“热度”与“金融相关性”拆开。

## 4. 趋势归纳

- 本轮没有可审计的 24h delta，因为缺少 `2026-05-09.json`；报告不补算、不猜测、不编造 24h 涨星。
- AI Trading 和 Agent 金融研究继续保持热度，`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`OpenAlice` 仍是连续观察对象。
- 通用 Agent、UI 生成、awesome 索引和安全工具继续进入 Top 区域，说明 `hot_score` 需要引入更强的金融相关性权重。
- 金融数据平台、量化研究框架和研究终端仍然稳定存在，`qlib`、`OpenBB`、`Kronos`、`FinceptTerminal` 更适合作为长期基础设施样本。
- Trading bot、crypto trading、personal trading agent 项目持续出现，应单独拆为高风险榜，而不是和研究工具混排。

## 5. 今日灵感清单

1. 补齐连续日期采集，避免缺少 `2026-05-09.json` 时无法计算 24h delta。
2. 增加 `relevance_score`，将通用 UI、awesome 列表、安全工具、课程索引和自托管清单从金融榜中降权。
3. 在报告中拆分三张榜：AI Trading/Agent、金融数据与量化基础设施、高风险 trading bot/crypto。
4. 对 7d 字段增加基线说明，显示实际 baseline 文件和距离目标 7 日的偏差。
5. 增加 `watchlist.yml`，固定跟踪 `TradingAgents`、`Vibe-Trading`、`QuantDinger`、`Kronos`、`qlib`、`OpenBB`。
6. 对 `trading_bot`、`crypto_related`、`personal trading agent` 等 risk_flags 输出单独汇总。
7. 后续如做 README enrichment，只读取 GitHub API/README 文本，不 clone、不安装、不运行候选仓库代码。

## 6. Watchlist 建议

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：多 Agent LLM 金融交易研究框架，7d 字段 +6409。
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)：personal trading agent，7d 字段 +1859，需风险隔离。
- [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger)：AI/量化/backtesting/crypto/trading bot 多重命中，7d 字段 +1502。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)：金融市场 foundation model，7d 字段 +1173。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析和推送闭环，7d 字段 +1046。
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)：金融分析终端产品参考，7d 字段 +1032。
- [microsoft/qlib](https://github.com/microsoft/qlib)：AI-oriented quant research 平台，7d 字段 +522。
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口，7d 字段 +375。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：成熟 crypto trading bot 框架，只适合架构观察和风险标记，不建议运行未知策略。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star、24h 涨星或 7d 涨星视为收益信号。自动交易、杠杆、马丁、网格、套利和做市类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- 24h delta 为 `N/A`，因为缺少 `2026-05-09.json` 作为 1 日基线。
- 7d delta 字段基于 `2026-05-10.json` 与 `2026-05-04.json`，这是当前可用历史中被 ranking 脚本选中的容忍窗口基线，不代表严格完整七个自然日。
- 今日仍有 personal trading agent、crypto trading、trading bot 项目进入候选，只能做风险观察和架构分析。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-10.json`，生成时间 `2026-05-11T00:46:31+00:00`。
- 1 日基线：缺失，本地没有 `2026-05-09.json`。
- 7 日字段基线：`2026-05-04.json`，生成时间 `2026-05-04T16:47:08+00:00`。
- 采集配置：完整 `config/keywords.yml`。
- 采集结果：59 个查询，118 次请求，3844 个去重候选，1 个采集错误。
- 采集错误：`"algorithmic trading" in:name,description,readme archived:false fork:false pushed:>2024-11-11` 在 `stars` 排序请求中 Read timed out。
- 排名输出：49 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程、安全工具、UI/设计系统和自托管索引项目。后续需要更强的金融相关性评分、watchlist 加权和风险榜分流。
