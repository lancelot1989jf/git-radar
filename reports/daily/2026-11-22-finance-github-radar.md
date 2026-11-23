# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-22

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能包（Skills）生态爆发**：Claude/Codex/Cursor 等编码 Agent 的“技能包”成为新的分发形态，覆盖 UI/UX、安全测试、交易分析、日内交易等场景。
  2. **LLM 驱动的股票/交易分析系统**：多源行情 + 实时新闻 + 决策看板 + 自动推送的“零成本定时运行”模式持续升温，A 股场景尤其活跃。
  3. **AI Agent 治理与审计**：针对 Agent 行为合规、幻觉检测、风险管理的独立审计工具开始出现，反映企业级 Agent 落地的合规需求。

- **是否出现新趋势**：出现。传统“交易 bot”热度被“AI Agent 技能包 + 交易研究工具”取代，更多项目以研究工具、分析看板而非自动下单为定位。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源数据 + LLM 决策看板 + 定时推送”架构、`tick-stock-panel` 的“自托管 + DuckDB/Polars + FastAPI + React”工作台架构、`iFixAi` 的 Agent 独立审计架构均值得参考。

- **是否有明显骗局、过度营销或高风险项目**：有。`metatrader-5-pro-win` 与 `quickbooks-premier-win` 两个项目创建于 2026-11-21，24 小时涨星异常（+278/+260），但 forks 为 0、无实质代码，且 topics 中出现 “crack”“mod”“installer” 等关键词，疑似软件分发/破解类营销仓库，风险极高。`Turnitout-Humanizer` 涉及学术抄袭规避，与金融科技无关且存在伦理风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 153003 | +415 | +2925 | Python | fintech_product | AI 技能包，提供跨平台 UI/UX 设计智能 | 中 | 低 |
| 2 | elementalsouls/Claude-BugHunter | 18469 | +2015 | +11707 | Python | fintech_product | Claude Code 漏洞挖掘/红队技能包 | 高 | 低 |
| 3 | GoogleChrome/modern-web-guidance | 25217 | +502 | +6714 | 无 | risk_management | 为编码 Agent 提供最新 Web 最佳实践 | 中 | 低 |
| 4 | GoogleChrome/modern-web-guidance-src | 10314 | +340 | +2824 | TypeScript | risk_management | 同上，源码仓库 | 中 | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 339657 | +318 | +2156 | 无 | trading_bot | 自托管网络服务列表 | 低 | 中 |
| 6 | codecrafters-io/build-your-own-x | 564831 | +303 | +1857 | Markdown | trading_bot | 从零复刻技术的教程合集 | 中 | 中 |
| 7 | tradermonty/claude-trading-skills | 7850 | +179 | +2045 | Python | backtesting/risk | Claude 股票投资与交易技能包 | 高 | 低 |
| 8 | public-apis/public-apis | 500920 | +227 | +1532 | Python | crypto/quant | 免费 API 合集 | 中 | 中 |
| 9 | JustVugg/colibri | 52998 | +250 | +1560 | C | quant_research | MoE 模型分层推理引擎 | 中 | 低 |
| 10 | vinta/awesome-python | 336555 | +225 | +1482 | Python | quant_research | Python 工具精选列表 | 低 | 低 |
| 11 | avelino/awesome-go | 195490 | +204 | +1340 | Go | backtesting/crypto | Go 框架与库精选列表 | 低 | 中 |
| 12 | nexu-io/open-design | 109055 | +175 | +1244 | TypeScript | fintech_product | 协作式 AI 设计 Agent 工作台 | 中 | 低 |
| 13 | ZhuLinsen/daily_stock_analysis | 73788 | +135 | +1178 | Python | ai_trading/quant | LLM 多市场股票智能分析系统 | 高 | 低 |
| 14 | Jakeschincariol/day-trader-skill | 9226 | +141 | +1164 | Python | backtesting | Claude 日内交易技能包 | 高 | 低 |
| 15 | VoltAgent/awesome-design-md | 128692 | +136 | +978 | 无 | crypto/fintech | DESIGN.md 设计系统合集 | 低 | 中 |
| 16 | ifixai-ai/iFixAi | 46895 | +169 | +935 | Python | ai_trading/risk | AI Agent 独立审计工具 | 高 | 低 |
| 17 | headroomlabs-ai/headroom | 80581 | +299 | +810 | Python | ai_trading/risk | LLM 输入 token 压缩工具 | 中 | 低 |
| 18 | TauricResearch/TradingAgents | 123535 | +124 | +769 | Python | ai_trading/backtesting | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 19 | CopilotKit/OpenBot | 13241 | +86 | +759 | TypeScript | fintech/trading_bot | 开源可自托管 AI Bot 替代品 | 中 | 中 |
| 20 | ashishpatel26/500-AI-Agents-Projects | 40589 | +153 | +649 | Python | risk/trading_bot | 500 个 AI Agent 用例合集 | 中 | 中 |
| 21 | jaywcjlove/awesome-mac | 119171 | +78 | +542 | Swift | trading_infra | macOS 软件精选列表 | 低 | 低 |
| 22 | hesreallyhim/awesome-claude-code | 58630 | +73 | +525 | Python | ai_trading/quant | Claude Code 资源精选 | 低 | 低 |
| 23 | microsoft/BitNet | 42431 | +49 | +843 | C++ | ai_trading/quant | 1-bit LLM 官方推理框架 | 中 | 低 |
| 24 | punkpeye/awesome-remote-mcp-servers | 3835 | +68 | +547 | 无 | ai_trading/crypto | 远程 MCP 服务器合集 | 中 | 中 |
| 25 | punkpeye/awesome-mcp-servers | 98398 | +28 | +650 | 无 | fintech_product | MCP 服务器合集 | 中 | 低 |
| 26 | ripienaar/free-for-dev | 143407 | +50 | +456 | HTML | fintech/quant | 开发者免费资源列表 | 低 | 低 |
| 27 | kaankiziltug/logo-design-skill | 7544 | +59 | +522 | HTML | fintech_product | AI Logo 设计技能包 | 低 | 低 |
| 28 | ruvnet/ruflo | 82296 | +52 | +458 | TypeScript | ai_trading/backtesting | 多 Agent 编排框架 | 中 | 低 |
| 29 | sickn33/agentic-awesome-skills | 50173 | +60 | +397 | Python | backtesting | 3000+ AI Agent 技能合集 | 中 | 低 |
| 30 | HKUDS/Vibe-Trading | 38718 | +57 | +370 | Python | ai_trading/backtesting | “Vibe-Trading”个人交易 Agent | 高 | 低 |
| 31 | garrytan/gbrain | 33446 | +64 | +334 | TypeScript | fintech_product | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 32 | shy3130/tick-stock-panel | 8201 | +43 | +308 | Python | ai_trading/backtesting | A 股自托管量化工作台 | 高 | 低 |
| 33 | off-grid-ai/OGAM | 3504 | +95 | +122 | TypeScript | ai_trading/quant | 离线 AI 瑞士军刀 | 中 | 低 |
| 34 | Hithink-Tech-Org/Financial-API | 4585 | +25 | +432 | TypeScript | data_engineering/quant | 同花顺官方 A 股金融数据服务 | 高 | 低 |
| 35 | TGrpg/awesome-telegram | 1945 | +44 | +328 | JavaScript | quant/trading_bot | Telegram 频道/群组/机器人导航 | 低 | 中 |
| 36 | PurpleDoubleD/locally-uncensored | 4606 | +41 | +317 | TypeScript | ai_trading/quant | 本地 AI 工作室 | 低 | 低 |
| 37 | AhmadHassan-BTed/Turnitout-Humanizer | 12561 | +41 | +253 | HTML | risk/trading_bot | 学术抄袭规避工具 | 无 | 中 |
| 38 | openbq-org/OpenBB | 75652 | +21 | +192 | Python | crypto/quant | 面向分析师/量化/AI Agent 的开放数据平台 | 高 | 中 |
| 39 | rust-unofficial/awesome-rust | 60744 | +28 | +170 | Rust | ai_trading/backtesting | Rust 资源精选 | 低 | 中 |
| 40 | aardappel/goose | 3815 | +31 | +250 | C++ | trading_infra | Goose 编程语言 | 低 | 低 |
| 41 | fffaraz/awesome-cpp | 74579 | +22 | +129 | 无 | quant/trading_infra | C/C++ 资源精选 | 低 | 低 |
| 42 | nidhinjs/prompt-master | 16252 | +28 | +216 | 无 | ai_trading/fintech | 精准 Prompt 编写技能 | 低 | 低 |
| 43 | loudonline/metatrader-5-pro-win | 423 | +278 | 无 | 无 | 无 | MetaTrader 5 Pro 软件分发 | 无 | 高 |
| 44 | committreeloop/quickbooks-premier-win | 417 | +260 | 无 | 无 | 无 | QuickBooks Premier 软件分发 | 无 | 高 |
| 45 | code-yeongyu/oh-my-openagent | 71068 | +17 | +133 | TypeScript | quant_research | 图工程 Agent 工具 | 低 | 低 |
| 46 | virattt/ai-hedge-fund | 64822 | +18 | +120 | Python | backtesting/risk | AI 对冲基金团队模拟 | 高 | 低 |
| 47 | josephmisiti/awesome-machine-learning | 74890 | +13 | +53 | Python | ai_trading | ML 框架与库精选 | 低 | 低 |
| 48 | awesomedata/awesome-public-datasets | 80246 | +4 | +87 | 无 | crypto_trading | 高质量开放数据集列表 | 中 | 中 |
| 49 | Developer-Y/cs-video-courses | 84914 | +10 | +53 | 无 | quant/trading_bot | CS 视频课程列表 | 低 | 中 |
| 50 | vuejs/awesome-vue | 73465 | -1 | -8 | 无 | quant_research | Vue.js 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis（rank 13）
- **解决什么问题**：LLM 驱动的多市场股票智能分析，聚合多源行情、实时新闻，生成决策看板并自动推送，支持零成本定时运行。
- **为什么值得关注**：73.7k stars，7 日涨星 +1178，A 股 + LLM 场景的典型代表，说明“AI 分析辅助决策”而非“AI 自动下单”是当前更被接受的形态。
- **技术栈/架构亮点**：Python + LLM + 多源数据聚合 + 定时任务 + 推送通知。架构上强调“零成本定时运行”，适合个人研究者。
- **是否适合借鉴**：非常适合。可借鉴其“数据聚合层 → LLM 分析层 → 看板/推送层”的分层设计，用于企业级投研 Agent 或内部决策辅助系统。
- **可能风险**：数据源合规性、LLM 输出幻觉导致的错误分析、新闻情绪信号的过拟合；需注意其分析结果不应直接作为交易信号。

### 3.2 TauricResearch/TradingAgents（rank 18）
- **解决什么问题**：多 Agent LLM 金融交易框架，将交易决策拆分为多个角色 Agent 协作。
- **为什么值得关注**：123.5k stars，是“LLM 多 Agent 交易”方向的开源标杆，7 日仍保持 +769 涨星。
- **技术栈/架构亮点**：Python + LangGraph 风格多 Agent 编排 + 回测集成。核心价值在于角色分工（分析师、研究员、交易员、风控等）的 Agent 架构。
- **是否适合借鉴**：适合。其多 Agent 角色分工模式可直接迁移到企业级投研 Agent、风控 Agent 或合规审查 Agent。
- **可能风险**：策略过拟合、回测幸存者偏差、LLM 决策不可解释性；不应直接用于实盘。

### 3.3 tradermonty/claude-trading-skills（rank 7）
- **解决什么问题**：面向 Claude Code 的股票投资与交易技能包，覆盖市场分析、技术图表、经济日历、选股器和策略开发。
- **为什么值得关注**：7 日涨星 +2045，增速极快，代表“Agent 技能包 + 交易研究”的新分发形态。
- **技术栈/架构亮点**：Python + Claude Skills 格式，将交易研究能力封装为可被编码 Agent 调用的技能模块。
- **是否适合借鉴**：非常适合。可将内部投研流程、数据查询、图表生成封装为 Agent 技能，提升 AI 辅助投研的可复用性。
- **可能风险**：研究工具定位，风险较低；但需注意技能包中若包含下单逻辑则风险升高。

### 3.4 HKUDS/Vibe-Trading（rank 30）
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多 Agent 与回测。
- **为什么值得关注**：HKUDS 出品，38.7k stars，学术背景 + 工程实现结合，是“Vibe-Trading”概念的代表。
- **技术栈/架构亮点**：Python + MCP + 多 Agent + 回测。MCP 的引入使其工具调用更标准化。
- **是否适合借鉴**：适合。可借鉴其 MCP 标准化工具接入方式，构建可插拔的金融数据/交易工具层。
- **可能风险**：学术研究项目，回测结果可能过拟合；不建议直接实盘。

### 3.5 shy3130/tick-stock-panel（rank 32）
- **解决什么问题**：A 股“自建策略 + 监控 + 回测”量化工作台，强调自托管、零运维，LLM 驱动策略定制与个股分析。
- **为什么值得关注**：技术栈现代（DuckDB、Polars、FastAPI、React），是 A 股量化工作台的良好工程参考。
- **技术栈/架构亮点**：DuckDB + Polars 做本地数据工程，FastAPI + React 做前后端，LLM 做策略定制与复盘。
- **是否适合借鉴**：非常适合。其“本地优先 + 列式数据 + 现代 Web 框架”的组合适合构建低成本的内部量化研究平台。
- **可能风险**：A 股数据合规、策略过拟合、自托管环境的数据安全。

### 3.6 ifixai-ai/iFixAi（rank 16）
- **解决什么问题**：AI Agent 独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审，120 秒内给出结论。
- **为什么值得关注**：46.9k stars，7 日 +935，反映企业级 Agent 治理与合规的迫切需求。
- **技术栈/架构亮点**：Python + CLI，覆盖幻觉检测、提示注入、AI 对齐、ISO 42001、NIST AI RMF、OWASP LLM 等标准。
- **是否适合借鉴**：非常适合。金融场景中，可将其审计思路用于交易 Agent 的行为监控、合规检查和异常检测。
- **可能风险**：审计工具本身可能产生误报；需结合人工复核。

### 3.7 virattt/ai-hedge-fund（rank 46）
- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作进行投资决策与回测。
- **为什么值得关注**：64.8k stars，是“AI 对冲基金”概念的开源代表，长期热度稳定。
- **技术栈/架构亮点**：Python + 多 Agent 角色（价值投资、成长投资、量化、风控等）+ 回测。
- **是否适合借鉴**：适合。其 Agent 角色定义和决策流程可作为企业级投研 Agent 的原型参考。
- **可能风险**：模拟环境，回测结果不代表实盘；策略可能过拟合。

### 3.8 Hithink-Tech-Org/Financial-API（rank 34）
- **解决什么问题**：同花顺官方 A 股金融数据服务，提供实时/历史行情、财报、指数、板块、涨停数据，支持 API、MCP、CLI、Python。
- **为什么值得关注**：官方背景 + MCP 支持，是 A 股量化数据基础设施的重要补充。
- **技术栈/架构亮点**：TypeScript + REST API + MCP + CLI + DuckDB。
- **是否适合借鉴**：适合。可作为 A 股数据层的标准化接入方案，尤其 MCP 接口适合 Agent 直接调用。
- **可能风险**：数据许可与合规、API 稳定性、依赖第三方数据源。

### 3.9 openbq-org/OpenBB（rank 38）
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、期权、加密、衍生品、宏观等。
- **为什么值得关注**：75.6k stars，是金融数据平台的开源标杆，持续演进。
- **技术栈/架构亮点**：Python + 多资产数据标准化 + AI 集成。
- **是否适合借鉴**：适合。可作为企业级金融数据中台的参考架构，尤其其数据标准化思路。
- **可能风险**：数据源合规、平台依赖、维护活跃度需持续观察。

### 3.10 loudonline/metatrader-5-pro-win 与 committreeloop/quickbooks-premier-win（rank 43/44）
- **解决什么问题**：声称提供 MetaTrader 5 Pro 与 QuickBooks Premier 软件，但实际为 2026-11-21 新建仓库，forks 为 0，无实质代码。
- **为什么值得关注**：作为反面案例。24 小时涨星异常（+278/+260），topics 含 “crack”“mod”“installer” 等关键词，疑似破解软件分发或 SEO 营销仓库。
- **技术栈/架构亮点**：无。
- **是否适合借鉴**：不适合。
- **可能风险**：极高。可能包含恶意软件、许可证违规、钓鱼风险；不应下载或运行。

## 4. 趋势归纳

- **技术趋势**：
  - **Agent Skills 成为新的能力分发单元**：大量项目以 “Claude/Codex/Cursor Skills” 形式封装专业能力，从 UI 设计到安全测试到交易分析。
  - **MCP（Model Context Protocol）成为 Agent 工具接入标准**：多个金融数据与交易项目支持 MCP，标准化工具调用。
  - **本地优先 + 列式数据**：DuckDB、Polars 在量化工作台中出现频率上升，强调自托管与零运维。
  - **LLM 输入优化**：token 压缩、上下文工程成为独立工具方向（如 headroom）。

- **产品趋势**：
  - **从“自动交易 bot”转向“AI 辅助决策看板”**：更多项目定位为分析、监控、复盘，而非自动下单。
  - **自托管与隐私优先**：本地 AI、离线 AI、自托管工作台受到关注。
  - **Agent 治理与审计产品化**：iFixAi 等工具将 Agent 合规审计作为独立产品。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 协作**：TradingAgents、ai-hedge-fund、Vibe-Trading 均采用多角色 Agent 分工。
  - **A 股场景活跃**：daily_stock_analysis、tick-stock-panel、Financial-API 均聚焦 A 股，中文社区贡献显著。
  - **研究工具与回测为主**：多数项目强调回测与研究，而非实盘执行。

- **AI Agent 与自动化交易结合趋势**：
  - **技能包 + 交易研究**：claude-trading-skills、day-trader-skill 将交易研究能力封装为 Agent 技能。
  - **Agent 审计与风控**：iFixAi 代表 Agent 行为审计方向，与金融合规需求天然契合。
  - **MCP 标准化金融工具**：Financial-API、Vibe-Trading 等通过 MCP 暴露金融数据与工具。

- **值得后续做原型验证的方向**：
  1. 企业级投研 Agent 技能包（数据查询、研报生成、图表分析）。
  2. 基于 MCP 的金融数据标准化接入层。
  3. 交易 Agent 行为审计与合规监控系统。
  4. 本地优先的 A 股量化研究工作台（DuckDB + Polars + FastAPI）。
  5. LLM 多 Agent 风控决策流程（角色分工 + 投票/制衡机制）。

## 5. 今日灵感清单

1. **MVP：投研 Agent 技能包**：参考 `claude-trading-skills`，将内部数据查询、技术指标计算、图表生成封装为 Claude/Codex 可调用的技能，先做 3-5 个核心技能验证。
2. **MVP：交易 Agent 行为审计器**：参考 `iFixAi`，为内部交易 Agent 构建行为日志审计模块，检测异常指令、越权操作、幻觉输出。
3. **调研：MCP 金融数据接入标准化**：研究 `Financial-API`、`Vibe-Trading` 的 MCP 实现，评估将内部行情/财报数据通过 MCP 暴露给 Agent 的可行性。
4. **调研：DuckDB + Polars 量化数据管道**：参考 `tick-stock-panel`，验证用 DuckDB + Polars 替代传统 pandas + SQL 数据库的本地量化数据管道性能。
5. **Codex 自动复现 demo：多 Agent 交易决策流程**：基于 `TradingAgents` 或 `ai-hedge-fund` 的 Agent 角色定义，让 Codex 自动生成一个简化的多角色投研决策 demo（仅回测，不实盘）。
6. **MVP：LLM 输入 token 压缩代理**：参考 `headroom`，为内部投研 Agent 构建日志/行情数据压缩代理，降低 LLM 调用成本。
7. **调研：Agent Skills 分发与版本管理**：研究 `agentic-awesome-skills`、`awesome-claude-code` 的技能目录结构，设计内部技能库的版本管理与分发机制。
8. **加入 watchlist：`OpenBB`**：作为金融数据平台参考，持续观察其数据标准化与 AI 集成演进。
9. **加入 watchlist：`iFixAi`**：观察 Agent 审计与合规工具的产品化路径。
10. **反面案例研究：`metatrader-5-pro-win`**：作为异常涨星与疑似恶意仓库的检测案例，完善内部开源项目风险评估规则。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | A 股 + LLM 分析看板代表，观察其数据聚合与推送架构演进 |
| TauricResearch/TradingAgents | 多 Agent 交易框架标杆，观察其 Agent 编排与回测集成 |
| tradermonty/claude-trading-skills | Agent 技能包 + 交易研究的新形态，观察技能包设计模式 |
| HKUDS/Vibe-Trading | 学术 + 工程结合的 Vibe-Trading 概念，观察 MCP 集成 |
| shy3130/tick-stock-panel | 现代技术栈的 A 股量化工作台，观察 DuckDB/Polars 应用 |
| ifixai-ai/iFixAi | Agent 审计与合规工具，观察企业级 Agent 治理需求 |
| Hithink-Tech-Org/Financial-API | 官方 A 股数据服务 + MCP，观察金融数据标准化接入 |
| openbq-org/OpenBB | 金融数据平台标杆，观察多资产数据标准化与 AI 集成 |
| virattt/ai-hedge-fund | AI 对冲基金模拟，观察多 Agent 投资决策流程 |
| headroomlabs-ai/headroom | LLM 输入压缩，观察 token 优化与上下文工程 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告包含 `baseline_1d`（2026-11-21）与 `baseline_7d`（2026-11-15），1 日与 7 日涨星数据完整。
- **30 日基线**：所有项目的 `star_delta_30d` 均为 `null`，30 日涨星数据缺失，无法评估中期趋势。
- **采集失败**：`metatrader-5-pro-win` 与 `quickbooks-premier-win` 的 `star_delta_7d` 为 `null`，可能因项目创建时间晚于 7 日基线，属正常现象。
- **样本偏差**：候选项目通过关键词匹配（fintech、quant、trading bot、backtesting、volatility 等）筛选，导致大量 “awesome-*” 列表类项目进入候选，真实金融/量化项目占比被稀释。部分项目（如 UI/UX 技能包、Web 指南、学术抄袭工具）与金融科技关联较弱，属于关键词误匹配。
- **分类可信度**：`category_guess` 为自动推断，存在误分类（如 `awesome-selfhosted` 被标为 trading_bot），需结合项目实际内容判断。
