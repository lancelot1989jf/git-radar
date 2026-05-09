# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-06

## 1. 今日摘要

- 本轮按要求标记为 `2026-05-06` 报告落盘；实际采集生成时间为 `2026-05-07T00:57:00+00:00`。
- 完整采集使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3816 个去重候选、0 个采集错误。
- 已有 1 日基线：当前 snapshot 为 `2026-05-06.json`，1 日基线为 `2026-05-05.json`；7 日基线仍缺失。
- 今日涨星最明显的候选包括 `nexu-io/open-design +4292`、`ruvnet/ruflo +2677`、`TauricResearch/TradingAgents +1662`、`public-apis/public-apis +854`、`VoltAgent/awesome-design-md +848`。
- 金融/量化/交易相关性较高的重点项目包括 `TradingAgents`、`daily_stock_analysis`、`OpenBB`、`Kronos`、`FinceptTerminal`、`Vibe-Trading`、`freqtrade`、`QuantDinger`。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 432733 | +854 | N/A | Python | crypto_trading, quant_research | 数据源目录化参考，金融相关性需二次确认 | 中 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 72101 | +848 | N/A | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性弱 | 中 |
| 3 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 296260 | +210 | N/A | Python | backtesting, quant_research | Python 生态选型索引 | 低 |
| 4 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 290617 | +313 | N/A | 信息不足 | trading_bot | 自托管工具索引，交易相关性弱 | 中 |
| 5 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 34262 | +218 | N/A | Python | ai_trading, quant_research | LLM 股票分析流水线与推送闭环 | 低 |
| 6 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 171987 | +121 | N/A | Go | backtesting, crypto_trading, trading_bot | Go 工具生态索引，需降噪 | 中 |
| 7 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 30448 | +4292 | N/A | TypeScript | fintech_product | Agent 生成应用/原型参考，涨星极快 | 低 |
| 8 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 56197 | +324 | N/A | TypeScript | quant_research | Agent harness 架构参考 | 低 |
| 9 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 108679 | +317 | N/A | C++ | ai_trading, quant_research | 本地 LLM 推理基础设施参考 | 低 |
| 10 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 121248 | +106 | N/A | HTML | fintech_product, quant_research | 免费服务索引，金融相关性弱 | 低 |

## 3. 重点项目深度分析

### TauricResearch/TradingAgents

`TradingAgents` 24h 涨星约 +1662，仍是本轮最值得关注的金融/Agent 交叉项目之一。项目描述为多 Agent LLM 金融交易框架，适合研究“信息收集、观点生成、交叉质询、结论解释”的 Agent 编排。工程启发在于角色分工、研究链路记录、任务状态管理和结论可追溯。风险在于项目语义靠近交易，不应直接迁移为自动下单系统，也不应接入真实交易 API key。

### ZhuLinsen/daily_stock_analysis

`daily_stock_analysis` 24h 涨星约 +218，描述中包含多数据源行情、实时新闻、LLM 决策仪表盘、多渠道推送和定时运行。它的产品闭环清晰：采集数据、生成分析、展示仪表盘、推送摘要。可借鉴方向是低成本自动化金融观察系统；风险是股票分析内容容易被误读为投资建议，必须保留数据来源审计和强风险声明。

### nexu-io/open-design

`open-design` 24h 涨星约 +4292，是本轮涨星最高候选。它不是金融/量化核心项目，但对“Agent 生成金融研究终端、报告页、数据仪表盘原型”有工程启发。后续若构建金融 Radar Web UI 或报告可视化，可以参考其本地优先、沙箱预览、多格式导出的产品形态。

### ruvnet/ruflo

`ruflo` 24h 涨星约 +2677，描述为 agent orchestration platform。它和金融相关性需要二次确认，但对金融 Agent 工作流有明显启发：多 Agent 编排、RAG 集成、Claude/Codex 集成、自学习 swarm 等能力可以映射到项目雷达、研究助理、风控审查等场景。

### OpenBB-finance/OpenBB

`OpenBB` 24h 涨星约 +70，是成熟金融数据平台，面向 analyst、quant 和 AI agents。它适合作为“金融数据平台 + Agent 工具入口”的参考。后续本项目可以借鉴它的数据源组织、统一接口和终端体验，把 GitHub Radar 扩展为可查询的金融开源项目知识库。

### shiyu-coder/Kronos

`Kronos` 24h 涨星约 +341，描述为金融市场语言的 foundation model。它代表“市场数据 + 基础模型”的方向，值得关注模型训练数据、推理接口、研究复现和评测方式。风险是金融模型容易被误解成收益预测工具，报告中必须强调研究用途。

### Fincept-Corporation/FinceptTerminal

`FinceptTerminal` 24h 涨星约 +328，是现代 finance application，覆盖 market analytics、investment research 和 economic data tools。它更像金融分析终端产品参考，适合观察数据探索、交互界面和研究工作台如何组合。

### HKUDS/Vibe-Trading

`Vibe-Trading` 24h 涨星约 +256，描述为 personal trading agent。它值得观察 AI trading 产品叙事，但风险等级偏中：personal trading agent 容易越过“研究辅助”和“交易执行”的边界。适合看产品和 Agent 交互，不适合直接运行或实盘。

### brokermr810/QuantDinger

`QuantDinger` 24h 涨星约 +325，分类包含 `ai_trading`、`backtesting`、`crypto_trading`。这是一个更贴近金融/量化语义的新增关注点，值得后续加入 watchlist 观察连续涨星和真实项目定位。风险来自 crypto 和交易语义，仍然只适合架构观察。

## 4. 趋势归纳

- 技术趋势：Agent orchestration、LLM 本地推理、金融数据平台和量化研究框架正在同一批查询中反复交叉出现。
- 产品趋势：LLM 股票分析、金融终端、Agent 工具入口、自动推送系统正在形成可复刻产品形态。
- 涨星趋势：高增速项目并不一定金融相关，`open-design`、`ruflo` 等项目说明需要引入更强的 `relevance_score`。
- 交易策略趋势：trading bot、crypto、prediction market、market maker、backtesting 项目持续出现，应单独放入高风险观察区。
- 数据工程趋势：公共 API、金融数据平台、交易所 adapter、研究终端仍是 AI 金融应用的重要底座。

## 5. 今日灵感清单

1. 增加 `relevance_score`，将 awesome 列表、课程、通用 Agent/UI 项目降权。
2. 增加 `watchlist.yml`，把 `TradingAgents`、`daily_stock_analysis`、`OpenBB`、`Kronos`、`FinceptTerminal`、`Vibe-Trading`、`QuantDinger` 放入长期观察。
3. 输出单独的 “AI Trading / Agent” 榜，避免和通用工具榜混在一起。
4. 输出单独的 “高风险交易 bot” 榜，集中标记 arbitrage、market maker、trading bot、crypto、leverage。
5. 增加 README 摘要 enrichment，但只读文件和 API，不 clone、不运行候选仓库代码。
6. 连续运行 7 天后生成真正的 7d growth 榜。
7. 给报告增加“噪音样本”小节，帮助人工调关键词和风险规则。

## 6. Watchlist 建议

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：24h +1662，多 Agent 金融框架，强趋势信号。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析和推送闭环。
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)：金融市场 foundation model 方向。
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)：金融分析终端产品参考。
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)：personal trading agent 产品形态，需风险隔离。
- [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger)：量化/AI/backtesting/crypto 交叉候选，需连续观察。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：crypto bot 框架，观察架构但不直接运行。
- [ccxt/ccxt](https://github.com/ccxt/ccxt)：多交易所 API adapter 设计参考。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- 24h delta 基于 `2026-05-06.json` 与 `2026-05-05.json`，但本轮实际采集发生在 2026-05-07 早上，文件名按用户要求标记为 2026-05-06。
- 7d delta 仍为 N/A，因为还没有 7 日历史基线。
- 今日有 trading bot、crypto、market maker、personal trading agent 等项目进入候选，只能做风险观察和架构分析。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-06.json`，生成时间 `2026-05-07T00:57:00+00:00`。
- 1 日基线：`2026-05-05.json`，生成时间 `2026-05-05T12:47:20+00:00`。
- 7 日基线：缺失。
- 采集配置：完整 `config/keywords.yml`。
- 采集结果：59 个查询，118 次请求，3816 个去重候选，0 个采集错误。
- 排名输出：52 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程、安全工具和设计系统项目，后续必须加入相关性评分和更细的金融分类。
