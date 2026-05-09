# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-08

## 1. 今日摘要

- 本轮按要求标记为 `2026-05-08` 报告落盘；实际采集生成时间为 `2026-05-09T00:31:47+00:00`。
- 完整采集使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3802 个去重候选、0 个采集错误。
- 当前 snapshot 为 `2026-05-08.json`，1 日基线为 `2026-05-07.json`；7 日字段已可计算，基线为 `2026-05-04.json`。
- 需要注意：`2026-05-04.json` 是当前历史窗口内最接近 7 日目标的可用基线，因此本报告中的 7d 数据应理解为“近 7 日窗口字段”，不是完整七个自然日的严格样本。
- 今日 24h 涨星最强的候选包括 `nexu-io/open-design +1476`、`VoltAgent/awesome-design-md +682`、`ruvnet/ruflo +637`、`TauricResearch/TradingAgents +577`、`HKUDS/Vibe-Trading +471`。
- 近 7 日字段中最强的候选包括 `nexu-io/open-design +11092`、`ruvnet/ruflo +6192`、`TauricResearch/TradingAgents +4993`、`VoltAgent/awesome-design-md +2758`、`public-apis/public-apis +2156`。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 73590 | +682 | +2758 | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性偏弱 | 中 |
| 2 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 33968 | +1476 | +11092 | TypeScript | fintech_product | 金融研究终端、报告页、仪表盘原型生成参考 | 低 |
| 3 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 71788 | +577 | +4993 | Python | ai_trading, backtesting, quant_research, risk_management | 多 Agent 金融交易研究框架，本轮核心观察对象 | 低 |
| 4 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 46882 | +637 | +6192 | TypeScript | ai_trading, backtesting | Agent 编排平台，适合映射到研究自动化流程 | 低 |
| 5 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 433334 | +225 | +2156 | Python | crypto_trading, quant_research | API 目录化与数据源发现参考，金融相关性需二次确认 | 中 |
| 6 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 75586 | +454 | +1774 | Python | fintech_product | UI/UX agent skill 参考，偏产品原型而非金融核心 | 低 |
| 7 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | 72974 | +273 | +1709 | Python | risk_management | 安全工具样本，金融相关性弱但可提示噪音问题 | 低 |
| 8 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 6072 | +471 | +1151 | Python | ai_trading, backtesting, crypto_trading, fintech_product, quant_research | personal trading agent 产品形态，需风险隔离 | 中 |
| 9 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 56656 | +175 | +929 | TypeScript | quant_research | Agent harness 和工作流组织参考 | 低 |
| 10 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 290992 | +165 | +843 | 信息不足 | trading_bot | 自托管服务索引，交易语义可能来自关键词噪音 | 中 |

## 3. 重点项目深度分析

### TauricResearch/TradingAgents

`TradingAgents` 本轮 24h 涨星约 +577，7d 字段约 +4993，仍然是 AI Trading 与金融 Agent 交叉方向里的核心观察对象。它的主要价值是观察多 Agent 如何拆分研究、观点生成、交叉质询、风险判断和结论记录。它不应被当成可直接执行的交易系统，更适合做研究流程编排和可追溯报告生成的架构参考。

### HKUDS/Vibe-Trading

`Vibe-Trading` 本轮 24h 涨星约 +471，7d 字段约 +1151，描述为 personal trading agent。它的信号很清晰：AI trading 产品正在从“研究工具”向“个人交易助理”叙事靠近。这个方向值得观察交互设计、状态解释和用户边界提示，但风险等级为中，不应接入真实交易 API key，也不应运行未知策略。

### brokermr810/QuantDinger

`QuantDinger` 本轮 24h 涨星约 +268，7d 字段约 +1009，分类同时命中 AI trading、backtesting、crypto trading、data engineering、quant research、trading bot 和 trading infra。它是本项目语义上很相关的候选，但也应该放入高风险观察区。可以看模块划分、回测/实盘隔离和数据流设计，不能把它作为实盘模板直接使用。

### shiyu-coder/Kronos

`Kronos` 本轮 24h 涨星约 +189，7d 字段约 +963，描述为面向金融市场语言的 foundation model。它代表市场数据和基础模型结合的方向。后续值得观察训练数据披露、评测协议、推理接口、复现说明和误用边界。

### ZhuLinsen/daily_stock_analysis

`daily_stock_analysis` 本轮 24h 涨星约 +162，7d 字段约 +703。它覆盖行情、实时新闻、LLM 分析仪表盘、多渠道推送和定时运行，是自动化金融观察系统的产品闭环样本。风险点在于股票分析内容容易被用户误读为投资建议，报告和 UI 必须持续保留数据来源、时间戳和免责声明。

### OpenBB-finance/OpenBB 与 microsoft/qlib

`OpenBB` 本轮 24h 涨星约 +69，7d 字段约 +245；`microsoft/qlib` 本轮 24h 涨星约 +97，7d 字段约 +276。两者都是更成熟的金融/量化基础设施参考：前者偏金融数据平台和 Agent 数据入口，后者偏 AI-oriented quant research、建模和生产化流程。它们适合做长期 watchlist 的稳定锚点。

### nexu-io/open-design 与 ruvnet/ruflo

`open-design` 本轮 24h 涨星约 +1476，7d 字段约 +11092，是本轮涨星最强候选；`ruflo` 本轮 24h 涨星约 +637，7d 字段约 +6192。它们不是金融/量化核心项目，但对金融 Radar 的报告生成、研究终端原型、Agent 编排和工作流可视化有间接工程价值。它们也再次说明，当前召回结果需要更强的金融相关性评分。

## 4. 趋势归纳

- AI Trading 和 Agent 金融研究继续保持高热度，`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`OpenAlice` 这类项目已经形成连续观察价值。
- 通用 Agent/UI 工具在 hot_score 中明显受益于 7d 涨星，说明 ranking 需要区分“热度”与“金融相关性”。
- 金融数据平台和量化基础设施仍然稳定存在，`OpenBB`、`qlib`、`FinceptTerminal`、`Kronos` 是更适合长期研究的样本。
- Trading bot、crypto trading、personal trading agent 项目持续出现，应该单独放入高风险榜，避免和研究工具混排后弱化风险提示。
- 7d 字段开始出现后，报告从“单日涨星观察”进入“短周期趋势观察”，但当前历史仍短，结论要保守。

## 5. 今日灵感清单

1. 增加 `relevance_score`，将通用 UI、awesome 列表、安全工具、课程索引和自托管清单从金融榜中降权。
2. 在报告中拆分三张榜：AI Trading/Agent、金融数据与量化基础设施、高风险 trading bot/crypto。
3. 对 7d 字段增加基线说明，显示实际 baseline 文件和距离目标 7 日的偏差。
4. 增加 “连续上榜项目” 小节，观察 `TradingAgents`、`Kronos`、`OpenBB`、`QuantDinger` 的趋势稳定性。
5. 增加 `watchlist.yml`，固定跟踪重点项目，不完全依赖关键词召回。
6. 对 `trading_bot`、`crypto_related`、`personal trading agent` 等 risk_flags 输出单独汇总。
7. 后续如做 README enrichment，只读取 GitHub API/README 文本，不 clone、不安装、不运行候选仓库代码。

## 6. Watchlist 建议

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：多 Agent LLM 金融交易研究框架，24h +577，7d 字段 +4993。
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)：personal trading agent，24h +471，7d 字段 +1151，需风险隔离。
- [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger)：AI/量化/backtesting/crypto/trading bot 多重命中，24h +268，7d 字段 +1009。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)：金融市场 foundation model，24h +189，7d 字段 +963。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析和推送闭环，24h +162，7d 字段 +703。
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)：金融分析终端产品参考，24h +79，7d 字段 +658。
- [microsoft/qlib](https://github.com/microsoft/qlib)：AI-oriented quant research 平台，24h +97，7d 字段 +276。
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口，24h +69，7d 字段 +245。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：成熟 crypto trading bot 框架，只适合架构观察和风险标记，不建议运行未知策略。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star、24h 涨星或 7d 涨星视为收益信号。自动交易、杠杆、马丁、网格、套利和做市类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- 24h delta 基于 `2026-05-08.json` 与 `2026-05-07.json`。
- 7d delta 字段基于 `2026-05-08.json` 与 `2026-05-04.json`，这是当前可用历史中被 ranking 脚本选中的容忍窗口基线，不代表完整七个自然日。
- 今日仍有 personal trading agent、crypto trading、trading bot 项目进入候选，只能做风险观察和架构分析。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-08.json`，生成时间 `2026-05-09T00:31:47+00:00`。
- 1 日基线：`2026-05-07.json`，生成时间 `2026-05-08T03:24:10+00:00`。
- 7 日字段基线：`2026-05-04.json`，生成时间 `2026-05-04T16:47:08+00:00`。
- 采集配置：完整 `config/keywords.yml`。
- 采集结果：59 个查询，118 次请求，3802 个去重候选，0 个采集错误。
- 排名输出：51 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程、安全工具、UI/设计系统和自托管索引项目。后续需要更强的金融相关性评分、watchlist 加权和风险榜分流。
