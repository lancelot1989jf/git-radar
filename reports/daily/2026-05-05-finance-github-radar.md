# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-05

## 1. 今日摘要

- 今日完整采集已使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3809 个去重候选。
- 已形成 1 日基线：当前 snapshot 为 `2026-05-05.json`，1 日基线为 `2026-05-04.json`；7 日基线仍缺失。
- 今日涨星最明显的候选包括 `nexu-io/open-design +3280`、`ruvnet/ruflo +1898`、`TauricResearch/TradingAgents +1878`、`public-apis/public-apis +701`、`VoltAgent/awesome-design-md +421`。
- 金融/量化/交易相关性较高的重点项目包括 `TradingAgents`、`Vibe-Trading`、`OpenBB`、`Kronos`、`FinceptTerminal`、`freqtrade`、`ccxt`、`ai-market-maker`。
- 数据里仍有明显噪音：awesome 列表、通用 Agent/UI 工具、课程和安全工具会被 README 关键词命中，后续需要相关性评分。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 431879 | +701 | N/A | Python | crypto_trading, quant_research | 数据源目录化参考，金融相关性需二次确认 | 中 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 71253 | +421 | N/A | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性弱 | 中 |
| 3 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 296050 | +100 | N/A | Python | backtesting, quant_research | Python 生态选型索引 | 低 |
| 4 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 290304 | +155 | N/A | 信息不足 | trading_bot | 自托管工具索引，交易相关性弱 | 中 |
| 5 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 55873 | +146 | N/A | TypeScript | quant_research | Agent harness 架构参考 | 低 |
| 6 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 26156 | +3280 | N/A | TypeScript | fintech_product | Agent 生成应用/原型参考，涨星极快 | 低 |
| 7 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 108362 | +133 | N/A | C++ | ai_trading, quant_research | 本地 LLM 推理基础设施参考 | 低 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 34044 | +93 | N/A | Python | ai_trading, quant_research | LLM 股票分析流水线与推送形态 | 低 |
| 9 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 68673 | +1878 | N/A | Python | ai_trading, backtesting, quant_research | 多 Agent 金融研究/交易框架 | 低 |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 42588 | +1898 | N/A | TypeScript | ai_trading, backtesting | Agent orchestration 参考，金融相关性需确认 | 低 |

## 3. 重点项目深度分析

### TauricResearch/TradingAgents

`TradingAgents` 24h 涨星约 +1878，是今天最值得关注的金融/Agent 交叉项目之一。它的描述是多 Agent LLM 金融交易框架，适合研究“信息收集、观点生成、交叉质询、结论解释”的 Agent 编排方式。工程启发在于角色分工、任务状态、讨论记录和研究结论追踪。风险是交易语义很强，不能把 demo 结果当成可执行策略，也不能接入真实交易 API key。

### ZhuLinsen/daily_stock_analysis

`daily_stock_analysis` 24h 涨星约 +93，描述中包含多数据源行情、实时新闻、LLM 决策仪表盘、多渠道推送和定时运行。它的产品闭环很清楚：采集数据、生成分析、展示仪表盘、推送摘要。可借鉴方向是“低成本自动化金融观察系统”。风险是股票分析内容容易被误读为投资建议，必须保留数据来源和风险边界。

### OpenBB-finance/OpenBB

`OpenBB` 24h 涨星约 +60，是成熟金融数据平台，面向 analyst、quant 和 AI agents。它适合作为“金融数据平台 + Agent 工具入口”的参考。后续本项目可以借鉴它的数据源组织、统一接口和终端体验，把 GitHub 雷达扩展成可查询的开源项目知识库。

### shiyu-coder/Kronos

`Kronos` 24h 涨星约 +151，描述为金融市场语言的 foundation model。它代表“市场数据 + 基础模型”的方向。值得关注的是模型训练数据、推理接口、研究复现和评测方式。风险是金融模型容易被误读成预测收益工具，报告中必须强调研究用途。

### Fincept-Corporation/FinceptTerminal

`FinceptTerminal` 24h 涨星约 +137，是现代 finance application，覆盖 market analytics、investment research 和 economic data tools。它更像金融分析终端产品形态参考，适合观察数据探索、交互界面和研究工作台如何组合。

### HKUDS/Vibe-Trading

`Vibe-Trading` 24h 涨星约 +123，描述为 personal trading agent。它值得观察 AI trading 产品叙事，但风险等级偏中：personal trading agent 很容易越过“研究辅助”和“交易执行”的边界。适合看产品和 Agent 交互，不适合直接运行或实盘。

### freqtrade/freqtrade

`freqtrade` 24h 涨星约 +48，是 crypto trading bot。它可作为回测、策略插件、配置和运行监控的架构参考。风险也很明确：不直接运行未知策略，不输入真实交易所 API key，不把 stars 或涨星视为收益信号。

### ccxt/ccxt

`ccxt` 是多交易所 API 抽象层，今天仍在候选中。工程亮点是 connector/adapter 设计、统一市场数据接口和跨语言生态。它靠近真实交易账户接入，因此本项目只做架构观察，不处理任何真实 key。

### bestpracticaI/kalshi-ai-trading-bot 与 Composio-HQ/polymarket-kalshi-arbitrage-bot

这两个项目都出现约 +95 的 24h 涨星，且名称直接包含 trading bot、arbitrage bot 或预测市场交易语义。它们说明“预测市场 + AI/自动化交易”正在吸引注意，但风险等级应保持中到高：套利、自动交易、API key、合规和资金风险都需要明确隔离。

## 4. 趋势归纳

- 技术趋势：AI Agent、金融研究平台、LLM 推理基础设施和交易基础设施开始互相靠近。
- 产品趋势：LLM 股票分析、金融终端、Agent 工具入口、自动推送系统正在形成可复刻产品形态。
- 涨星趋势：今天最高增速并不全是金融项目，说明热点搜索需要引入相关性评分，而不能只看 `hot_score`。
- 交易策略趋势：crypto bot、预测市场 bot、market maker 仍持续出现，但必须放入高风险观察区。
- 数据工程趋势：公共 API、金融数据平台、交易所 adapter 仍是金融 Agent 的重要底座。

## 5. 今日灵感清单

1. 增加 `relevance_score`，将 awesome 列表、通用 Agent/UI/课程项目降权。
2. 增加 `watchlist.yml`，把 `TradingAgents`、`OpenBB`、`Kronos`、`FinceptTerminal`、`freqtrade`、`ccxt`、`hummingbot` 放入长期观察。
3. 输出单独的“AI Trading / Agent”榜，避免和通用工具榜混在一起。
4. 输出单独的“高风险交易 bot”榜，集中标记 arbitrage、market maker、trading bot、leverage、signal。
5. 增加 README 摘要 enrichment，但只读文件和 API，不 clone、不运行候选仓库代码。
6. 连续运行 7 天后生成真正 7d growth 榜。
7. 给报告增加“噪音样本”小节，帮助人工调关键词和风险规则。

## 6. Watchlist 建议

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：24h +1878，多 Agent 金融框架，强趋势信号。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析和推送闭环。
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口。
- [microsoft/qlib](https://github.com/microsoft/qlib)：AI-oriented quant research 平台。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)：金融市场 foundation model 方向。
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)：金融分析终端产品参考。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：crypto bot 框架，观察架构但不直接运行。
- [ccxt/ccxt](https://github.com/ccxt/ccxt)：多交易所 API adapter 设计参考。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- 24h delta 基于当前 `2026-05-05.json` 与保留的 `2026-05-04.json`，实际间隔约 20 小时，接近但不是严格 24 小时。
- 7d delta 仍为 N/A，因为还没有 7 日历史基线。
- 今日有预测市场 bot、arbitrage bot、market maker、crypto bot 等项目进入候选，只能做风险观察和架构分析。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-05.json`，生成时间 `2026-05-05T12:47:20+00:00`。
- 1 日基线：`2026-05-04.json`，生成时间 `2026-05-04T16:47:08+00:00`。
- 7 日基线：缺失。
- 采集配置：完整 `config/keywords.yml`。
- 采集结果：59 个查询，118 次请求，3809 个去重候选。
- 采集错误：1 个，查询为 `arbitrage in:name,description,readme` 的 `stars` 排序，错误是 GitHub 403 rate/abuse protection；其他查询正常完成。
- 排名输出：49 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程、安全工具和设计系统项目，后续必须加入相关性评分和更细的金融分类。
