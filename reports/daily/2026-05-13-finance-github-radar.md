# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-13

## 1. 今日摘要

- 本轮按要求标记为 `2026-05-13` 报告落盘；实际采集生成时间为 `2026-05-14T00:57:12+00:00`。
- 完整采集使用 GitHub CLI 认证 token 跑通：59 个查询、118 次请求、3830 个去重候选、2 个采集错误。
- 当前 snapshot 为 `2026-05-13.json`，1 日基线为 `2026-05-12.json`，7 日基线为 `2026-05-06.json`。
- 今日 24h 涨星最强的候选包括 `VoltAgent/awesome-design-md +1218`、`ruvnet/ruflo +619`、`TauricResearch/TradingAgents +569`、`shiyu-coder/Kronos +364`、`public-apis/public-apis +346`。
- 7d 字段最强的候选包括 `nexu-io/open-design +8916`、`VoltAgent/awesome-design-md +5687`、`ruvnet/ruflo +5096`、`TauricResearch/TradingAgents +4633`、`nextlevelbuilder/ui-ux-pro-max-skill +3433`。
- 金融/量化/AI Trading 相关性较高的重点项目包括 `TradingAgents`、`Vibe-Trading`、`QuantDinger`、`daily_stock_analysis`、`Kronos`、`FinceptTerminal`、`qlib`、`OpenBB`、`freqtrade`。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h | 7d | 语言 | 分类 | 灵感价值 | 风险 |
|---:|---|---:|---:|---:|---|---|---|---|
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 77788 | +1218 | +5687 | 信息不足 | crypto_trading, fintech_product | Agent 生成 UI/设计系统参考，金融相关性偏弱 | 中 |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 74968 | +569 | +4633 | Python | ai_trading, backtesting, quant_research, risk_management | 多 Agent 金融交易研究框架，本轮核心观察对象 | 低 |
| 3 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 50361 | +619 | +5096 | TypeScript | ai_trading, backtesting | Agent 编排平台，适合映射到金融研究自动化流程 | 低 |
| 4 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 434853 | +346 | +2120 | Python | crypto_trading, quant_research | API 目录化与数据源发现参考，金融相关性需二次确认 | 中 |
| 5 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 39364 | N/A | +8916 | TypeScript | fintech_product | 金融研究终端、报告页、仪表盘原型生成参考 | 低 |
| 6 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 78057 | N/A | +3433 | Python | fintech_product | UI/UX agent skill 参考，偏产品原型而非金融核心 | 低 |
| 7 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 7249 | +123 | +1949 | Python | ai_trading, backtesting, crypto_trading, fintech_product, quant_research | personal trading agent 产品形态，需风险隔离 | 中 |
| 8 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | 74104 | +204 | +1794 | Python | risk_management | 安全工具样本，金融相关性弱但提示噪音问题 | 低 |
| 9 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 501224 | +271 | +1719 | Markdown | trading_bot | 通用学习索引，交易语义可能来自关键词噪音 | 中 |
| 10 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | 4996 | +192 | +1677 | Python | ai_trading, backtesting, crypto_trading, data_engineering, quant_research, trading_bot, trading_infra | AI 量化/交易基础设施候选，高风险观察对象 | 中 |

## 3. 重点项目深度分析

### TauricResearch/TradingAgents

`TradingAgents` 本轮 24h 涨星约 +569，7d 字段约 +4633，仍是 AI Trading 与金融 Agent 交叉方向的核心观察对象。它的价值在于观察多 Agent 如何拆分研究、观点生成、交叉质询、风控判断和结论记录。它不应被当作可直接执行的交易系统，更适合做研究流程编排、审计链路和报告生成的架构参考。

### HKUDS/Vibe-Trading

`Vibe-Trading` 本轮 24h 涨星约 +123，7d 字段约 +1949，描述为 personal trading agent。它说明 AI trading 叙事仍在从“研究辅助”靠近“个人交易助理”。这个方向值得观察交互边界、状态解释和风险提示，但不应接入真实交易 API key，也不应运行未知策略。

### brokermr810/QuantDinger

`QuantDinger` 本轮 24h 涨星约 +192，7d 字段约 +1677，分类命中 AI trading、backtesting、crypto trading、data engineering、quant research、trading bot 和 trading infra。它和本 Radar 的主题高度相关，也因此更需要风险隔离。可以研究模块划分、回测/实盘边界、数据流和多 Agent 研究链路，不能直接运行其交易功能。

### ZhuLinsen/daily_stock_analysis

`daily_stock_analysis` 本轮 24h 涨星约 +179，7d 字段约 +1508，覆盖 A/H/美股行情、实时新闻、LLM 分析仪表盘、多渠道推送和定时运行。它是自动化金融观察系统的产品闭环样本，但输出内容容易被误读为投资建议，必须保留数据来源、时间戳、模型说明和免责声明。

### shiyu-coder/Kronos

`Kronos` 本轮 24h 涨星约 +364，7d 字段约 +1218，描述为面向金融市场语言的 foundation model。它代表市场数据与基础模型结合的方向，后续值得关注训练数据、评测协议、推理接口、复现方式和误用边界。

### Fincept-Corporation/FinceptTerminal

`FinceptTerminal` 本轮 24h 涨星约 +94，7d 字段约 +893，是金融分析终端产品参考，覆盖 market analytics、investment research 和 economic data tools。它适合观察金融数据探索、研究工作台、可视化和用户体验如何组合。

### microsoft/qlib 与 OpenBB-finance/OpenBB

`qlib` 本轮 24h 涨星约 +87，7d 字段约 +722；`OpenBB` 本轮 24h 涨星约 +59，7d 字段约 +422。两者是更稳定的金融/量化基础设施样本：`qlib` 偏 AI-oriented quant research 和建模生产化，`OpenBB` 偏金融数据平台和 AI agent 数据入口。它们适合进入长期 watchlist，不一定需要依赖短期热度排序。

### ruvnet/ruflo 与 VoltAgent/awesome-design-md

`ruflo` 本轮 24h 涨星约 +619，7d 字段约 +5096；`awesome-design-md` 本轮 24h 涨星约 +1218，7d 字段约 +5687。它们不是金融/量化核心项目，但对金融 Radar 的 Agent 编排、报告 UI 和研究终端原型有间接工程价值。它们也继续提示：当前排名需要把“热度”与“金融相关性”拆开。

### nexu-io/open-design

`open-design` 本轮 7d 字段约 +8916，但 24h 为 N/A，说明它在 `2026-05-12.json` 的候选输出中没有可比的 1 日基线记录。它仍是通用 UI/原型生成方向的强热度信号，适合作为金融 Radar 前端体验参考，而不是金融核心项目结论。

## 4. 趋势归纳

- 24h 和 7d delta 都有可用基线，但个别项目仍可能因为未进入上一日候选而出现 24h N/A。
- AI Trading 和 Agent 金融研究继续保持热度，`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`OpenAlice` 仍是连续观察对象。
- 通用 Agent、UI 生成、本地推理、安全工具、awesome 索引仍在 Top 区域反复出现，说明 `hot_score` 需要引入更强的金融相关性权重。
- 金融数据平台、量化研究框架和研究终端仍然稳定存在，`qlib`、`OpenBB`、`Kronos`、`FinceptTerminal` 更适合作为长期基础设施样本。
- Trading bot、crypto trading、personal trading agent 项目持续出现，应单独拆为高风险榜，而不是和研究工具混排。

## 5. 今日灵感清单

1. 增加 `relevance_score`，将通用 UI、awesome 列表、安全工具、本地推理引擎和课程索引从金融榜中降权。
2. 在报告中拆分三张榜：AI Trading/Agent、金融数据与量化基础设施、高风险 trading bot/crypto。
3. 对 24h N/A 做更细说明：区分“无 1 日基线”和“项目未出现在上一日候选输出中”。
4. 对 `trading_bot`、`crypto_related`、`personal trading agent` 等 risk_flags 输出单独汇总。
5. 增加 `watchlist.yml`，固定跟踪 `TradingAgents`、`Vibe-Trading`、`QuantDinger`、`Kronos`、`qlib`、`OpenBB`。
6. 增加“连续上榜项目”小节，降低单日热度波动对人工判断的干扰。
7. 后续如做 README enrichment，只读取 GitHub API/README 文本，不 clone、不安装、不运行候选仓库代码。

## 6. Watchlist 建议

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：多 Agent LLM 金融交易研究框架，24h +569，7d 字段 +4633。
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)：personal trading agent，24h +123，7d 字段 +1949，需风险隔离。
- [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger)：AI/量化/backtesting/crypto/trading bot 多重命中，24h +192，7d 字段 +1677。
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：LLM 股票分析和推送闭环，24h +179，7d 字段 +1508。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)：金融市场 foundation model，24h +364，7d 字段 +1218。
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)：金融分析终端产品参考，24h +94，7d 字段 +893。
- [microsoft/qlib](https://github.com/microsoft/qlib)：AI-oriented quant research 平台，24h +87，7d 字段 +722。
- [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)：金融数据平台和 AI agent 数据入口，24h +59，7d 字段 +422。
- [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)：成熟 crypto trading bot 框架，只适合架构观察和风险标记，不建议运行未知策略。

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star、24h 涨星或 7d 涨星视为收益信号。自动交易、杠杆、马丁、网格、套利和做市类项目可能存在重大资金风险、合规风险和安全风险。

特别注意：

- 24h delta 基于 `2026-05-13.json` 与 `2026-05-12.json`。
- 7d delta 字段基于 `2026-05-13.json` 与 `2026-05-06.json`。
- 今日仍有 personal trading agent、crypto trading、trading bot 项目进入候选，只能做风险观察和架构分析。

## 8. 数据质量说明

- 本次输入文件：`data/latest_candidates.json`。
- 当前 snapshot：`2026-05-13.json`，生成时间 `2026-05-14T00:57:12+00:00`。
- 1 日基线：`2026-05-12.json`，生成时间 `2026-05-13T00:32:27+00:00`。
- 7 日基线：`2026-05-06.json`，生成时间 `2026-05-07T00:57:00+00:00`。
- 采集配置：完整 `config/keywords.yml`。
- 采集结果：59 个查询，118 次请求，3830 个去重候选，2 个采集错误。
- 采集错误：`topic:algorithmic-trading archived:false fork:false pushed:>2024-11-14` 在 `stars` 排序请求中遇到 proxy 503，在 `updated` 排序请求中 Read timed out。
- 排名输出：50 个候选。
- 样本偏差：README 关键词搜索会命中通用 awesome 列表、AI 工具、课程、安全工具、UI/设计系统、本地推理引擎和自托管索引项目。后续需要更强的金融相关性评分、watchlist 加权和风险榜分流。
