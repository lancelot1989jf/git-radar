# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-05

## 1. 今日摘要

- 今日完整采集已使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3832 个去重候选、0 个采集错误。
- 今日最值得关注的方向是：AI + 金融研究、金融数据平台、量化研究框架、交易基础设施。
- 值得深入看的工程项目包括 `OpenBB-finance/OpenBB`、`microsoft/qlib`、`TauricResearch/TradingAgents`、`QuantConnect/Lean`、`ccxt/ccxt`、`freqtrade/freqtrade`。
- 样本中也出现大量 awesome 列表、通用 AI/设计/课程项目，说明 README 关键词搜索需要继续做相关性降噪。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 431178 | N/A | N/A | Python | crypto_trading, quant_research | 数据源目录化参考，但金融相关性需二次确认 | 中 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 70832 | N/A | N/A | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性弱 | 中 |
| 3 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 295950 | N/A | N/A | Python | backtesting, quant_research | Python 生态选型索引 | 低 |
| 4 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 290149 | N/A | N/A | 信息不足 | trading_bot | 自托管工具索引，交易相关性弱 | 中 |
| 5 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 33951 | N/A | N/A | Python | ai_trading, quant_research | LLM 股票分析流水线与推送形态 | 低 |
| 6 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 171789 | N/A | N/A | Go | backtesting, crypto_trading, trading_bot | Go 工具生态索引，需降噪 | 中 |
| 7 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 55727 | N/A | N/A | TypeScript | quant_research | Agent harness 架构参考 | 低 |
| 8 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 108229 | N/A | N/A | C++ | ai_trading, quant_research | 本地 LLM 推理基础设施参考 | 低 |
| 9 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 121155 | N/A | N/A | HTML | fintech_product, quant_research | 免费服务索引，相关性弱 | 低 |
| 10 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 22876 | N/A | N/A | TypeScript | fintech_product | Agent 生成应用/原型参考 | 低 |

## 3. 重点项目深度分析

### ZhuLinsen/daily_stock_analysis

这是一个 LLM 驱动的 A/H/美股智能分析器，描述中包含多数据源行情、实时新闻、LLM 决策仪表盘和多渠道推送。它最值得借鉴的是“数据源聚合 + LLM 分析 + 定时运行 + 通知”的产品闭环。风险在于股票分析内容容易被用户误解为投资建议，任何复用都应保留强风险提示和数据来源审计。

### TauricResearch/TradingAgents

`TradingAgents` 是多 Agent LLM 金融交易框架。工程价值在于把金融研究流程拆成多个角色，适合研究“信息收集、观点生成、交叉质询、结论解释”的 Agent 编排方式。风险是此类项目靠近交易语义，不应直接迁移为自动下单系统。

### OpenBB-finance/OpenBB

`OpenBB` 是面向分析师、quants 和 AI agents 的金融数据平台。它适合观察数据源接入、统一 API、终端体验和 Agent 工具接口如何结合。对本项目的后续启发是：把雷达从日报扩展为可查询的金融开源项目知识库。

### microsoft/qlib

`qlib` 是 AI-oriented quant research 平台，适合参考数据、特征、模型、实验、回测和研发自动化的分层方式。它的价值在研究工作流，而不是收益承诺。后续可以把它列入 watchlist，连续观察 star 增长和 release 活跃度。

### QuantConnect/Lean

`Lean` 是算法交易引擎，工程亮点在策略生命周期、数据订阅、回测/实盘一致抽象、订单模型和多语言支持。风险等级偏中，因为它靠近真实执行层；本项目不能运行未知策略或处理交易 API key。

### freqtrade/freqtrade

`freqtrade` 是 crypto trading bot，包含回测、策略、配置、运行监控等模块。它可以作为自动交易框架结构参考，但风险边界最需要强调：不能直接运行未知策略，不能输入真实交易所 API key，不能把 stars 当成收益信号。

### ccxt/ccxt

`ccxt` 是多交易所 API 抽象层。工程亮点是 connector/adapter 设计、统一市场数据接口和跨语言生态。它对交易基础设施设计有参考价值，但也最接近真实账户接入，必须避免在本项目中处理任何真实 key。

### hummingbot/hummingbot

`hummingbot` 是高频 crypto trading bot 基础设施。适合观察策略模板、交易所连接器、配置系统和运行方式。风险来自高频、做市、crypto、自动执行等组合，不适合作为普通用户实盘建议。

## 4. 趋势归纳

- 技术趋势：金融/量化项目正在向平台化、Agent 化、自动化研究流程靠拢。
- 产品趋势：金融数据平台、研究终端、LLM 分析仪表盘和多渠道推送形成了清晰产品闭环。
- 交易基础设施趋势：交易所 API 抽象、回测引擎、策略框架仍是高热主题，但必须和真实交易隔离。
- AI Agent 趋势：Agent harness、MCP、LLM 本地推理、金融研究平台之间开始出现交叉。
- 数据质量趋势：完整 README 搜索会带来大量通用项目噪音，下一步需要 `relevance_score` 或 README 摘要二次分类。

## 5. 今日灵感清单

1. 为 `latest_candidates.json` 增加 `relevance_score`，将 awesome 列表、课程列表、通用 AI 项目降权。
2. 增加 watchlist：`OpenBB`、`qlib`、`TradingAgents`、`Lean`、`ccxt`、`freqtrade`、`hummingbot`。
3. 做一个“金融开源项目能力图谱”，按 data、research、backtest、execution、risk、agent 分类。
4. 增加 README 摘要只读 enrichment，不 clone、不运行候选仓库代码。
5. 将 trading bot、crypto、leverage、signal、martingale 相关项目单独输出风险榜。
6. 让周报聚焦“工程架构可复用模式”，例如 adapter、plugin、workflow、experiment tracking。
7. 增加趋势曲线，连续 7 天后输出真正的 7d star growth 榜。

## 6. Watchlist 建议

- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口。
- [microsoft/qlib](https://github.com/microsoft/qlib)：AI-oriented quant research 平台。
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：多 Agent 金融研究/交易框架概念。
- [QuantConnect/Lean](https://github.com/QuantConnect/Lean)：算法交易引擎和回测/执行抽象。
- [ccxt/ccxt](https://github.com/ccxt/ccxt)：多交易所 API adapter 设计参考。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：crypto bot 框架，适合观察架构但不建议直接运行。
- [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot)：做市/高频/连接器架构观察对象。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析与通知流水线形态。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- `24h` 和 `7d` 涨星目前均为 N/A，因为仓库还没有历史 snapshot 基线。
- crypto bot、交易 API、自动执行框架只适合做架构观察，不适合直接实盘。
- 高 star 项目不等于金融相关性高，也不等于策略有效。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-05.json`。
- 1 日基线：缺失。
- 7 日基线：缺失。
- 采集方式：完整配置 `config/keywords.yml`，使用 GitHub CLI 认证 token。
- 采集结果：59 个查询，118 次请求，3832 个去重候选，0 个采集错误，排名输出 48 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程和设计系统项目，需要后续加入相关性评分。
