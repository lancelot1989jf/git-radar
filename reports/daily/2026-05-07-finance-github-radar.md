# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-07

## 1. 今日摘要

- 本轮按要求标记为 `2026-05-07` 报告落盘；实际采集生成时间为 `2026-05-08T03:24:10+00:00`。
- 完整采集使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3809 个去重候选、0 个采集错误。
- 已有 1 日基线：当前 snapshot 为 `2026-05-07.json`，1 日基线为 `2026-05-06.json`；7 日基线仍缺失。
- 今日 24h 涨星最强的候选包括 `nexu-io/open-design +2044`、`ruvnet/ruflo +980`、`TauricResearch/TradingAgents +876`、`VoltAgent/awesome-design-md +807`、`nextlevelbuilder/ui-ux-pro-max-skill +508`。
- 金融/量化/AI Trading 相关性较高的重点项目包括 `TradingAgents`、`daily_stock_analysis`、`Vibe-Trading`、`QuantDinger`、`OpenBB`、`Kronos`、`FinceptTerminal`、`OpenAlice`、`freqtrade`。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 433109 | +376 | N/A | Python | crypto_trading, quant_research | API 目录化与数据源发现参考，金融相关性需二次确认 | 中 |
| 2 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 296440 | +180 | N/A | Python | backtesting, quant_research | Python 生态选型索引，可辅助量化工具链调研 | 低 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 72908 | +807 | N/A | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性偏弱 | 中 |
| 4 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 290827 | +210 | N/A | 信息不足 | trading_bot | 自托管服务索引，交易语义可能来自关键词噪音 | 中 |
| 5 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 34492 | +230 | N/A | Python | ai_trading, quant_research | LLM 股票分析、行情新闻聚合、推送闭环参考 | 低 |
| 6 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 32492 | +2044 | N/A | TypeScript | fintech_product | 金融研究终端、报告页、仪表盘原型生成参考 | 低 |
| 7 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 56481 | +284 | N/A | TypeScript | quant_research | Agent harness 和工作流组织参考 | 低 |
| 8 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 108895 | +216 | N/A | C++ | ai_trading, quant_research | 本地 LLM 推理基础设施参考 | 低 |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 121498 | +250 | N/A | HTML | fintech_product, quant_research | 免费服务索引，适合工具链预算参考 | 低 |
| 10 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 71211 | +876 | N/A | Python | ai_trading, backtesting, quant_research, risk_management | 多 Agent 金融交易研究框架，本轮核心观察对象 | 低 |

## 3. 重点项目深度分析

### TauricResearch/TradingAgents

`TradingAgents` 本轮 24h 涨星约 +876，仍是 AI Trading 与金融 Agent 交叉方向里最醒目的项目之一。它的价值不在于“拿来交易”，而在于观察多 Agent 如何拆分研究、辩论、风控和结论生成流程。后续可重点看角色编排、过程记录、状态追踪和输出可解释性。

### ZhuLinsen/daily_stock_analysis

`daily_stock_analysis` 本轮 24h 涨星约 +230，描述覆盖 A/H/美股行情、新闻、LLM 决策仪表盘、多渠道推送和定时运行。它适合作为“自动化金融观察系统”的产品参考，但报告和 UI 必须持续强调研究用途，避免把自动摘要包装成投资建议。

### HKUDS/Vibe-Trading

`Vibe-Trading` 本轮 24h 涨星约 +301，描述为 personal trading agent，分类覆盖 AI trading、backtesting、crypto trading、fintech product 和 quant research。它适合观察个人交易助理的交互形态和研究链路，但风险等级为中，不能接入真实交易 API key，也不能直接运行未知策略。

### brokermr810/QuantDinger

`QuantDinger` 本轮 24h 涨星约 +378，分类同时命中 AI trading、backtesting、crypto trading、data engineering、quant research、trading bot 和 trading infra。它的语义非常贴近本项目雷达目标，也因此需要放入高风险观察区：可以看架构和模块边界，不应运行其交易功能或使用真实资金环境。

### OpenBB-finance/OpenBB

`OpenBB` 本轮 24h 涨星约 +46，是更成熟的金融数据平台参考，描述明确面向 analysts、quants 和 AI agents。它适合长期观察数据源组织、统一接口、终端体验和 Agent 数据入口设计。

### shiyu-coder/Kronos

`Kronos` 本轮 24h 涨星约 +282，描述为面向金融市场语言的 foundation model。它代表“市场数据 + 基础模型”的研究方向，适合关注训练数据、评测方式、推理接口和复现边界。不要把模型热度或短期涨星理解为收益预测能力。

### Fincept-Corporation/FinceptTerminal

`FinceptTerminal` 本轮 24h 涨星约 +114，定位是现代 finance application，覆盖 market analytics、investment research 和 economic data tools。它更像金融分析终端产品参考，适合观察研究工作台、数据探索和可视化体验如何组合。

### nexu-io/open-design 与 ruvnet/ruflo

`open-design` 本轮 24h 涨星约 +2044，是本轮涨星最高候选；`ruflo` 本轮 24h 涨星约 +980，描述为 agent orchestration platform。两者不是金融/量化核心项目，但对金融 Radar 的 UI 原型、报告生成、Agent 编排和研究自动化有间接工程价值。它们也提醒我们：当前关键词召回会混入大量通用 Agent/UI 项目，后续必须增加相关性评分。

## 4. 趋势归纳

- AI Trading 与 Agent 金融研究继续升温，`TradingAgents`、`Vibe-Trading`、`OpenAlice`、`QuantDinger` 这类项目反复进入候选。
- 金融数据平台和研究终端仍是稳定方向，`OpenBB`、`FinceptTerminal`、`daily_stock_analysis` 可作为产品闭环样本。
- 通用 Agent、UI 生成、awesome 索引和开发工具仍会大量进入结果，需要用 `relevance_score` 把它们和真正金融项目拆开。
- Crypto trading、trading bot、personal trading agent 相关项目持续出现，适合单独做风险榜，而不是和研究工具混在一个榜里。
- 1 日涨星已经可用，但 7 日趋势仍然缺基线；连续运行到 7 天后，趋势判断会明显更可靠。

## 5. 今日灵感清单

1. 增加 `relevance_score`，降低通用 awesome 列表、课程、安全工具、UI/设计系统项目的排名权重。
2. 增加长期 `watchlist.yml`，固定跟踪 `TradingAgents`、`daily_stock_analysis`、`OpenBB`、`Kronos`、`FinceptTerminal`、`Vibe-Trading`、`QuantDinger`、`OpenAlice`。
3. 拆分 “AI Trading / Agent” 榜、“金融数据平台” 榜和 “高风险交易 bot” 榜。
4. 对 `trading_bot`、`crypto_related`、`market maker`、`arbitrage`、`leverage` 等风险标记增加单独摘要。
5. 增加噪音样本输出，把明显不相关但高分的候选暴露出来，便于调关键词。
6. 连续采集满 7 天后，新增 7d growth 榜和“连续上榜项目”小节。
7. 后续如做 README enrichment，只读取 GitHub API/README 文本，不 clone、不安装、不运行候选仓库代码。

## 6. Watchlist 建议

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：多 Agent LLM 金融交易研究框架，24h +876，仍是核心观察对象。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析和推送闭环，24h +230。
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)：personal trading agent，24h +301，需风险隔离。
- [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger)：AI/量化/backtesting/crypto/trading bot 多重命中，24h +378。
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口，成熟度较高。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)：金融市场 foundation model，24h +282。
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)：金融分析终端产品参考，24h +114。
- [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice)：AI trading agent，风险等级中，适合观察产品叙事与边界控制。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：成熟 crypto trading bot 框架，只适合架构观察和风险标记，不建议运行未知策略。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格、套利和做市类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- 24h delta 基于 `2026-05-07.json` 与 `2026-05-06.json`，但本轮实际采集发生在 2026-05-08，文件名按用户要求标记为 2026-05-07。
- 7d delta 仍为 N/A，因为还没有 7 日历史基线。
- 今日有 personal trading agent、crypto trading、trading bot 等项目进入候选，只能做风险观察和架构分析。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-07.json`，生成时间 `2026-05-08T03:24:10+00:00`。
- 1 日基线：`2026-05-06.json`，生成时间 `2026-05-07T00:57:00+00:00`。
- 7 日基线：缺失。
- 采集配置：完整 `config/keywords.yml`。
- 采集结果：59 个查询，118 次请求，3809 个去重候选，0 个采集错误。
- 排名输出：50 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程、安全工具、UI/设计系统和自托管索引项目。后续需要更强的金融相关性评分、watchlist 加权和风险榜分流。
