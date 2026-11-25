# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-24

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能包（Skills）生态爆发**：Claude Code / Codex / Cursor 的“技能包”成为新的分发单元，覆盖 UI 设计、安全测试、交易分析、日内交易等场景。`Claude-BugHunter` 单日涨星 +1547，`ui-ux-pro-max-skill` 单日 +392，说明“可复用 Agent 技能”正在成为高增长品类。
  2. **LLM 驱动的股票/交易分析工作台**：`daily_stock_analysis`（+292/日）、`tick-stock-panel`、`Vibe-Trading`、`TradingAgents` 等项目持续走热，核心模式是“多源行情 + LLM 决策看板 + 回测/监控”，且大量面向 A 股。
  3. **本地优先与推理基础设施**：`colibri`（MoE 分层推理引擎，+167/日）、`kimi-k3-in-c`（单 CPU 跑 2.78T 参数模型）显示“在自有硬件上跑前沿模型”的工程路线受到强烈关注，对量化研究中的低成本本地推理有直接借鉴意义。

- **是否出现新趋势**：出现。候选集中大量项目并非传统交易 bot，而是 **“Agent 技能包 + 金融数据接口 + 本地推理”** 的组合。金融/量化项目与通用 AI Agent 基础设施的边界正在模糊。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“DuckDB + Polars + FastAPI + React + LLM 策略定制”架构，都值得作为轻量级量化研究工作台原型参考。

- **是否有明显骗局、过度营销或高风险项目**：候选集中存在明显噪声项目，例如 `Turnitout-Humanizer`（宣称绕过 Turnitin/GPTZero 的“AI 降重/抄袭规避”工具），与金融量化无关，且存在学术诚信与合规风险。另有多个 `awesome-*` 列表类项目因关键词误匹配进入候选，不应视为交易系统。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 153915 | +392 | +2859 | Python | fintech_product | AI 技能包，提供跨平台 UI/UX 设计智能 | 中：Agent 技能包产品化思路 | 低 |
| 2 | elementalsouls/Claude-BugHunter | 22034 | +1547 | +12050 | Python | fintech_product | Claude Code 漏洞挖掘/红队技能包 | 高：Agent 安全审计与风控自动化 | 低 |
| 3 | GoogleChrome/modern-web-guidance | 26010 | +314 | +3646 | 无 | risk_management | 为编码 Agent 提供最新 Web 最佳实践 | 中：Agent 知识注入机制 | 低 |
| 4 | GoogleChrome/modern-web-guidance-src | 10916 | +245 | +2344 | TypeScript | risk_management | 上述项目的源码版 | 中：同上 | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 340305 | +291 | +2111 | 无 | trading_bot | 自托管网络服务列表 | 低：误匹配，非交易项目 | 中 |
| 6 | codecrafters-io/build-your-own-x | 565389 | +257 | +1834 | Markdown | trading_bot | 从零复刻技术的教程合集 | 中：可复刻交易系统组件 | 中 |
| 7 | JustVugg/colibri | 53386 | +167 | +1571 | C | quant_research | MoE 模型分层推理引擎 | 高：低成本本地推理 | 低 |
| 8 | vinta/awesome-python | 337008 | +208 | +1452 | Python | quant_research | Python 工具精选列表 | 低：误匹配 | 低 |
| 9 | public-apis/public-apis | 501298 | +170 | +1353 | Python | crypto_trading/quant | 免费 API 合集 | 中：金融数据源发现 | 中 |
| 10 | avelino/awesome-go | 195866 | +187 | +1319 | Go | backtesting/crypto | Go 框架库列表 | 低：误匹配 | 中 |
| 11 | ZhuLinsen/daily_stock_analysis | 74463 | +292 | +1272 | Python | ai_trading/quant | LLM 驱动多市场股票分析系统 | 高：LLM 决策看板架构 | 低 |
| 12 | tradermonty/claude-trading-skills | 8371 | +180 | +1429 | Python | backtesting/risk | Claude 交易技能包 | 高：交易 Agent 技能化 | 低 |
| 13 | nexu-io/open-design | 109402 | +155 | +1223 | TypeScript | fintech_product | 协作式 AI 设计 Agent 工作区 | 中：Agent 协作产品形态 | 低 |
| 14 | Jakeschincariol/day-trader-skill | 9545 | +164 | +1086 | Python | backtesting/risk | 11 个日内交易 Claude 技能 | 中：交易决策流程模板化 | 低 |
| 15 | VoltAgent/awesome-design-md | 128992 | +138 | +957 | 无 | crypto_trading/fintech | 品牌设计系统 DESIGN.md 合集 | 低：误匹配 | 中 |
| 16 | ifixai-ai/iFixAi | 47270 | +202 | +902 | Python | ai_trading/risk | AI Agent 独立审计工具 | 高：Agent 治理与合规审计 | 低 |
| 17 | headroomlabs-ai/headroom | 80812 | +114 | +855 | Python | ai_trading/risk | LLM 上下文压缩工具 | 高：降低 Agent token 成本 | 低 |
| 18 | CopilotKit/OpenBot | 13462 | +112 | +676 | TypeScript | fintech_product/trading_bot | 开源可自托管 AI bot 替代品 | 中：Agent 编排框架 | 中 |
| 19 | TauricResearch/TradingAgents | 123729 | +74 | +714 | TypeScript | ai_trading/quant | 面向 Agentic 金融研究的多 Agent 框架 | 高：多 Agent 投研架构 | 低 |
| 20 | ripienaar/free-for-dev | 143609 | +88 | +509 | HTML | fintech_product | 开发者免费资源列表 | 低：误匹配 | 低 |
| 21 | punkpeye/awesome-remote-mcp-servers | 4021 | +90 | +564 | 无 | ai_trading/crypto | 远程 MCP 服务器合集 | 中：MCP 生态观察 | 中 |
| 22 | jaywcjlove/awesome-mac | 119317 | +80 | +526 | Swift | trading_infra | macOS 软件精选 | 低：误匹配 | 低 |
| 23 | ashishpatel26/500-AI-Agents-Projects | 40726 | +50 | +656 | Python | risk_management/trading_bot | 500 个 AI Agent 用例合集 | 中：Agent 用例灵感 | 中 |
| 24 | punkpeye/awesome-mcp-servers | 98481 | +29 | +647 | 无 | fintech_product | MCP 服务器合集 | 中：MCP 生态观察 | 低 |
| 25 | kaankiziltug/logo-design-skill | 7697 | +85 | +474 | HTML | fintech_product | Logo 设计 Agent 技能 | 低：误匹配 | 低 |
| 26 | HKUDS/Vibe-Trading | 38842 | +85 | +374 | Python | ai_trading/backtesting | “Vibe-Trading”个人交易 Agent | 高：LLM 交易 Agent 研究 | 低 |
| 27 | hesreallyhim/awesome-claude-code | 58763 | +57 | +503 | Python | ai_trading/quant | Claude Code 资源精选 | 低：误匹配 | 低 |
| 28 | sickn33/agentic-awesome-skills | 50300 | +64 | +379 | Python | backtesting | 3000+ 可复用 Agent 技能库 | 中：技能库工程化 | 低 |
| 29 | ruvnet/ruflo | 82394 | +48 | +402 | TypeScript | ai_trading/backtesting | 多 Agent 编排框架 | 中：多 Agent 系统参考 | 低 |
| 30 | lukasz-madon/awesome-remote-job | 51099 | +85 | +368 | 无 | fintech_product | 远程工作资源列表 | 低：误匹配 | 低 |
| 31 | garrytan/gbrain | 33566 | +54 | +321 | TypeScript | fintech_product | OpenClaw/Hermes Agent Brain | 中：Agent 记忆/编排 | 低 |
| 32 | awesomedata/awesome-public-datasets | 80403 | +67 | +216 | 无 | crypto_trading | 公开数据集列表 | 中：另类数据源 | 中 |
| 33 | microsoft/BitNet | 42465 | +12 | +651 | C++ | ai_trading/quant | 1-bit LLM 推理框架 | 高：低比特量化推理 | 低 |
| 34 | bangtutorial/bang-motion | 3032 | +49 | +497 | HTML | fintech_product | 浏览器动效 Agent 技能 | 低：误匹配 | 低 |
| 35 | FareedKhan-dev/kimi-k3-in-c | 12657 | +30 | +340 | C | ai_trading/quant | 单 CPU 跑 2.78T 参数 MoE 模型 | 高：极致本地推理 | 低 |
| 36 | Developer-Y/cs-video-courses | 84986 | +57 | +105 | 无 | quant_research/trading_bot | CS 视频课程列表 | 低：误匹配 | 中 |
| 37 | PurpleDoubleD/locally-uncensored | 4683 | +32 | +310 | TypeScript | ai_trading/quant | 本地 AI 工作室桌面应用 | 中：本地 AI 工作台 | 低 |
| 38 | shy3130/tick-stock-panel | 8264 | +31 | +238 | Python | ai_trading/backtesting | A 股自建策略+监控+回测工作台 | 高：DuckDB+Polars 轻量架构 | 低 |
| 39 | AhmadHassan-BTed/Turnitout-Humanizer | 12632 | +34 | +242 | HTML | risk_management/trading_bot | 宣称可绕过查重的“AI 降重”工具 | 低：学术诚信风险，噪声 | 中 |
| 40 | openbq-org/OpenBB | 75717 | +25 | +204 | Python | crypto_trading/quant | 面向分析师/量化/AI Agent 的开放数据平台 | 高：金融数据平台参考 | 中 |
| 41 | Hithink-Tech-Org/Financial-API | 4613 | +13 | +363 | TypeScript | data_engineering/quant | 同花顺官方 A 股金融数据服务 | 高：A 股数据 API/MCP | 低 |
| 42 | rust-unofficial/awesome-rust | 60798 | +24 | +174 | Rust | ai_trading/backtesting | Rust 资源列表 | 低：误匹配 | 中 |
| 43 | fffaraz/awesome-cpp | 74616 | +20 | +130 | 无 | quant_research/trading_infra | C/C++ 资源列表 | 低：误匹配 | 低 |
| 44 | Orkas-AI/Orkas | 9593 | +26 | +151 | JavaScript | backtesting | 本地优先桌面多 Agent 团队 | 中：本地 Agent 编排 | 低 |
| 45 | off-grid-ai/OGAM | 3582 | +33 | +191 | TypeScript | ai_trading/quant | 离线 AI 瑞士军刀 | 中：端侧 AI 能力 | 低 |
| 46 | code-yeongyu/oh-my-openagent | 71101 | +7 | +117 | TypeScript | quant_research | 图工程 Agent 工具 | 低：误匹配 | 低 |
| 47 | virattt/ai-hedge-fund | 64848 | +8 | +110 | Python | backtesting/risk | AI 对冲基金团队模拟 | 高：多 Agent 投研决策 | 低 |
| 48 | josephmisiti/awesome-machine-learning | 74907 | +4 | +59 | Python | ai_trading/fintech | ML 资源列表 | 低：误匹配 | 低 |
| 49 | vuejs/awesome-vue | 73460 | -2 | -14 | 无 | quant_research | Vue 资源列表 | 低：误匹配 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股/多市场的每日股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：单日 +292 星、7 日 +1272 星，总星 74k，是候选集中少数真正聚焦“LLM + 股票分析”且增长强劲的项目。其“零成本定时运行”定位降低了个人研究者使用门槛。
- **技术栈/架构亮点**：Python + LLM；多源行情与新闻聚合；决策看板；自动推送。架构上强调“定时、低成本、自动化”，适合作为个人投研助手原型。
- **是否适合借鉴**：适合。可借鉴其“数据聚合 → LLM 分析 → 看板/推送”的流水线，用于企业级投研 Agent 或内部研究工具。
- **可能风险**：LLM 输出可能存在幻觉，需人工复核；行情数据源合规性需确认；不可将分析结果直接视为交易信号。

### 3.2 TauricResearch/TradingAgents
- **解决什么问题**：面向 Agentic 金融研究的多 Agent 框架，模拟投研团队协作。
- **为什么值得关注**：总星 123k，7 日 +714，是“AI Agent + 金融研究”方向的代表性项目，持续活跃。
- **技术栈/架构亮点**：TypeScript；多 Agent 协作；LLM 驱动；topic 含 multiagent、finance、trading。
- **是否适合借鉴**：非常适合。其多 Agent 分工（如分析师、交易员、风控）可作为企业级投研 Agent 框架的参考原型。
- **可能风险**：研究工具属性强，策略有效性未经验证；多 Agent 系统复杂度高，需注意 token 成本与决策一致性。

### 3.3 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多 Agent 与回测。
- **为什么值得关注**：HKUDS 出品，总星 38k，7 日 +374，是学术机构在“LLM 交易 Agent”方向的探索。
- **技术栈/架构亮点**：Python；MCP；multi-agent；backtesting；quantitative-finance。
- **是否适合借鉴**：适合作为研究方向参考，尤其是 MCP 在交易工具链中的接入方式。
- **可能风险**：学术原型，不可直接实盘；回测结果可能存在过拟合；需警惕“vibe-trading”概念被误读为收益承诺。

### 3.4 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 协作完成投研决策。
- **为什么值得关注**：总星 64k，是“AI 对冲基金”概念的开源标杆，长期受关注。
- **技术栈/架构亮点**：Python；多 Agent 模拟；回测/风险管理关键词命中。
- **是否适合借鉴**：适合作为多 Agent 投研决策流程的教学与原型参考。
- **可能风险**：模拟环境不等于实盘；策略表现不可外推；需避免将 star 数误解为策略有效性。

### 3.5 shy3130/tick-stock-panel
- **解决什么问题**：A 股“自建策略 + 监控 + 回测”量化工作台，强调自托管、零运维、LLM 驱动策略定制与个股分析。
- **为什么值得关注**：总星 8.2k，7 日 +238，技术栈现代且轻量，适合个人量化研究者。
- **技术栈/架构亮点**：Python；DuckDB + Polars + FastAPI + React；LLM 能力用于策略定制、个股分析、复盘；支持第三方数据源。
- **是否适合借鉴**：非常适合。DuckDB + Polars 的轻量数据栈是个人/小团队量化工作台的高性价比选择。
- **可能风险**：自托管数据质量与延迟需自行保障；LLM 生成策略需严格回测与风控；不可直接实盘。

### 3.6 tradermonty/claude-trading-skills
- **解决什么问题**：为 Claude Code 提供股票投资与交易技能包，覆盖市场分析、技术图表、经济日历、筛选器与策略开发。
- **为什么值得关注**：7 日 +1429 星，总星 8.3k，是“交易能力技能化”的典型代表。
- **技术栈/架构亮点**：Python；以 Claude Code 技能包形式分发；模块化交易分析能力。
- **是否适合借鉴**：适合。可借鉴其将交易分析流程拆解为可复用技能的设计，用于企业内部 Agent 工具链。
- **可能风险**：技能包内容需审计，避免注入恶意指令；分析结果不可直接作为交易依据。

### 3.7 Jakeschincariol/day-trader-skill
- **解决什么问题**：11 个日内交易 Claude 技能，覆盖图表扫描、新闻跟踪、进出场时机与结果回放。
- **为什么值得关注**：7 日 +1086 星，总星 9.5k，日内交易场景的技能化尝试。
- **技术栈/架构亮点**：Python；Claude 技能包；强调“先回放再冒险”。
- **是否适合借鉴**：可借鉴其“交易决策流程模板化”思路，但需警惕日内交易策略的高风险属性。
- **可能风险**：日内交易策略极易过拟合；技能包可能隐含高风险操作；不可直接用于实盘。

### 3.8 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审。
- **为什么值得关注**：总星 47k，单日 +202，契合 AI Agent 治理、合规与风控需求。
- **技术栈/架构亮点**：Python；CLI；覆盖 AI 对齐、幻觉检测、提示注入、ISO 42001、NIST AI RMF、OWASP LLM 等。
- **是否适合借鉴**：非常适合。金融场景中 Agent 审计与合规是刚需，可将其审计思路引入交易 Agent 风控体系。
- **可能风险**：审计工具本身需验证可靠性；不能替代正式合规审计。

### 3.9 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 前压缩工具输出、日志、文件与 RAG 片段，降低 token 消耗。
- **为什么值得关注**：总星 80k，7 日 +855，对高频调用 LLM 的量化/投研 Agent 有直接降本价值。
- **技术栈/架构亮点**：Python；库/代理/MCP 服务器形态；宣称编码 Agent 减少 20% token，JSON 减少 60-95%。
- **是否适合借鉴**：适合。可将其作为 Agent 上下文工程组件，降低投研 Agent 的长期运行成本。
- **可能风险**：压缩可能损失关键信息，需在金融场景中验证准确性。

### 3.10 JustVugg/colibri 与 FareedKhan-dev/kimi-k3-in-c
- **解决什么问题**：前者是 MoE 模型分层推理引擎（GPU/RAM/NVMe 分层）；后者在单 CPU 上以 8.24GB RAM 跑 2.78T 参数模型。
- **为什么值得关注**：两者均体现“在自有硬件上跑前沿模型”的工程趋势，对量化研究中低成本本地推理有直接意义。
- **技术栈/架构亮点**：C 语言；colibri 采用 CUDA/Vulkan + RAM + NVMe 分层；kimi-k3-in-c 采用 C99、SIMD、MXFP4 量化、零依赖。
- **是否适合借鉴**：适合作为本地推理基础设施的调研对象，尤其是数据隐私敏感或成本敏感的量化场景。
- **可能风险**：工程复杂度高；推理性能与精度需自行验证；非金融专用，需二次开发。

## 4. 趋势归纳

- **技术趋势**：
  - **Agent 技能包成为新分发单元**：大量项目以“Claude Code / Codex / Cursor 技能包”形式发布，覆盖设计、安全、交易、数据分析。
  - **本地优先与边缘推理**：从 `colibri`、`kimi-k3-in-c`、`BitNet` 到 `OGAM`、`locally-uncensored`，本地推理与隐私优先成为明确方向。
  - **轻量数据栈**：`tick-stock-panel` 采用 DuckDB + Polars + FastAPI，替代传统重型数据库，适合个人/小团队量化工作台。
  - **MCP 生态扩张**：多个项目涉及 MCP 服务器与远程 MCP，工具接入标准化趋势明显。

- **产品趋势**：
  - **从“交易 bot”转向“投研/分析工作台”**：`daily_stock_analysis`、`tick-stock-panel`、`OpenBB` 等强调分析、看板、推送，而非自动下单。
  - **Agent 治理与审计产品化**：`iFixAi` 代表 AI Agent 审计/合规工具的兴起。
  - **协作式 AI 工作区**：`open-design`、`Orkas` 等强调本地优先、多 Agent 协作。

- **量化/交易策略趋势**：
  - **LLM 辅助策略生成与个股分析**：`tick-stock-panel`、`Vibe-Trading` 将 LLM 用于策略定制与复盘。
  - **多 Agent 投研决策**：`TradingAgents`、`ai-hedge-fund` 模拟团队协作，但策略有效性仍属研究范畴。
  - **A 股数据接口开放**：`Hithink-Tech-Org/Financial-API` 提供官方 A 股数据 API/MCP/CLI，降低数据获取门槛。

- **AI Agent 与自动化交易结合趋势**：
  - 结合点集中在“分析、监控、回测、推送”，而非“自动下单”。
  - 交易能力被拆解为可复用技能包，但风险控制与人工复核仍是关键缺口。
  - Agent 审计、上下文压缩、本地推理等基础设施正在补齐自动化交易的工程短板。

- **值得后续做原型验证的方向**：
  - 基于 DuckDB + Polars 的轻量 A 股研究/回测工作台。
  - 交易分析流程的 Agent 技能包化，并加入审计与风控层。
  - 本地推理引擎在量化数据隐私场景中的应用。
  - MCP 标准下的金融数据接口与工具链集成。

## 5. 今日灵感清单

1. **MVP：轻量 A 股投研工作台**：参考 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭建“数据导入 → 指标计算 → 回测 → LLM 复盘”的最小闭环，先跑通日线数据。
2. **MVP：交易分析技能包**：参考 `claude-trading-skills` 与 `day-trader-skill`，将“行情摘要、技术指标、新闻情绪、风险提示”拆成 5-8 个可复用 Agent 技能，并加入只读约束。
3. **调研：MCP 金融数据接入**：调研 `Hithink-Tech-Org/Financial-API` 与 `OpenBB` 的 MCP/API 设计，评估能否作为内部 Agent 的统一数据层。
4. **调研：Agent 审计与风控**：研究 `iFixAi` 的审计思路，设计一个针对交易 Agent 的“决策日志 + 越权检测 + 幻觉检测”原型。
5. **Demo：本地推理跑通小模型**：用 `kimi-k3-in-c` 或 `colibri` 的思路，在本地 CPU/GPU 环境跑通一个小型量化模型，验证隐私敏感场景的可行性。
6. **Demo：上下文压缩降本**：将 `headroom` 的思路用于投研 Agent 的新闻/财报长文本输入，测试 token 节省与信息保真度。
7. **Watchlist：多 Agent 投研框架**：持续跟踪 `TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 的架构演进，提取可复用的 Agent 分工模式。
8. **原型：Agent 技能库工程化**：参考 `agentic-awesome-skills`，建立内部技能目录、版本管理与选择机制，避免技能包失控。
9. **调研：低比特量化推理**：关注 `BitNet` 与 MXFP4 量化在金融 NLP 任务上的精度损失，评估是否可用于舆情分析。
10. **安全审计：技能包供应链**：对引入的第三方 Agent 技能包做静态扫描与行为审计，防止提示注入或恶意指令。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | LLM 股票分析工作台代表，增长快，架构可参考 |
| TauricResearch/TradingAgents | 多 Agent 金融研究标杆，持续活跃 |
| HKUDS/Vibe-Trading | 学术机构探索 LLM 交易 Agent，研究方向价值高 |
| shy3130/tick-stock-panel | DuckDB+Polars 轻量量化工作台，工程参考价值高 |
| tradermonty/claude-trading-skills | 交易能力技能化代表，适合拆解复用 |
| ifixai-ai/iFixAi | Agent 审计/治理工具，金融合规场景刚需 |
| headroomlabs-ai/headroom | Agent token 降本，长期运行成本优化 |
| Hithink-Tech-Org/Financial-API | 官方 A 股数据 API/MCP，数据层候选 |
| openbq-org/OpenBB | 面向量化与 AI Agent 的开放数据平台 |
| JustVugg/colibri | 本地 MoE 推理引擎，隐私与成本敏感场景参考 |
| FareedKhan-dev/kimi-k3-in-c | 极致本地推理，工程极限探索 |
| virattt/ai-hedge-fund | AI 对冲基金模拟，多 Agent 决策教学原型 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次数据提供 `baseline_1d: 2026-11-23.json` 与 `baseline_7d: 2026-11-17.json`，基线文件存在，涨星数据可用。
- **30 日涨星**：所有项目的 `star_delta_30d` 均为 `null`，本次报告无法提供 30 日趋势。
- **采集失败**：JSON 中未显式标注采集失败项，但存在明显误匹配与噪声项目。
- **样本偏差**：候选集由多组关键词查询合并而成，包含大量 `awesome-*` 列表类项目与 UI/设计类项目，金融/量化/交易相关项目占比有限。部分项目因关键词误匹配进入候选（如 `Turnitout-Humanizer`、`awesome-mac`、`awesome-vue`），分析时需人工过滤。`category_guess` 与 `risk_flags` 为自动推断，可能与实际项目性质存在偏差。
