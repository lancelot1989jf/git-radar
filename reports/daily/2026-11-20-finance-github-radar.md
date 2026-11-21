# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-20

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能包 / Claude Code Skills 生态**：多个高热度项目围绕 Claude Code、Codex、Cursor 等编码 Agent 提供可复用技能包，其中交易类技能包（`claude-trading-skills`、`day-trader-skill`）直接切入股票分析、技术图表、策略开发场景。
  2. **LLM 多智能体金融交易框架**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 等项目持续活跃，反映“多 Agent 协作完成市场分析—策略生成—回测—风控”的架构正在成为主流研究方向。
  3. **A 股数据服务与量化工作台**：`daily_stock_analysis`、`Financial-API`、`tick-stock-panel` 等项目显示，面向 A 股市场的 AI Agent 数据接入、自托管量化工作台正在快速升温。

- **是否出现新趋势**：出现。**“Claude Code Skills 即产品”** 的趋势非常明显——大量项目不再提供完整交易系统，而是以“技能包 / 提示词工程 / Agent 能力扩展”的形式交付，降低使用门槛，同时把策略逻辑、数据源接入、风控判断都封装为 Agent 可调用的技能。另一个新趋势是 **AI Agent 审计与治理**（`iFixAi`）开始进入金融场景视野。

- **是否出现值得复刻/参考的工程架构**：是。`TradingAgents` 的多智能体协作框架、`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送”流水线、`tick-stock-panel` 的“自建策略 + 监控 + 回测”自托管工作台，以及 `headroom` 的“LLM 上下文压缩代理”都具备较高的工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明确骗局，但存在明显**关键词误匹配**问题——大量 awesome-list、UI 设计、本地 LLM 推理、学术抄袭规避工具等项目因描述或 README 中偶然出现 “fintech”“quant”“trading bot”“volatility” 等词而被纳入，实际与金融/量化无关。其中 `Turnitout-Humanizer` 属于学术不端辅助工具，应明确规避。`awesome-telegram` 等列表类项目存在引流到未知 Telegram 群组/机器人的风险，需谨慎。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 152249 | +337 | +3053 | Python | AI 技能/UI 设计 | 跨平台 UI/UX 设计智能技能包 | 低（与金融弱相关） | 低 |
| 2 | elementalsouls/Claude-BugHunter | 14756 | +1737 | +8989 | Python | AI 安全/红队 | Claude Code 漏洞挖掘技能包 | 中（Agent 安全审计） | 低 |
| 3 | GoogleChrome/modern-web-guidance | 24076 | +442 | +12337 | 无 | Web 最佳实践 | 编码 Agent 的 Web 最佳实践指南 | 低（与金融弱相关） | 低 |
| 4 | tradermonty/claude-trading-skills | 7480 | +172 | +3171 | Python | 交易技能/回测 | Claude Code 股票交易技能包 | 高（交易 Agent 技能化） | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 339056 | +298 | +2208 | 无 | 自托管列表 | 自托管网络服务列表 | 中（自托管基础设施） | 中 |
| 6 | codecrafters-io/build-your-own-x | 564196 | +190 | +1806 | Markdown | 教程列表 | 从零复刻技术的教程合集 | 中（系统学习） | 中 |
| 7 | public-apis/public-apis | 500541 | +160 | +1692 | Python | API 列表 | 免费公共 API 合集 | 中（数据源发现） | 中 |
| 8 | JustVugg/colibri | 52532 | +225 | +1611 | C | MoE 推理引擎 | 分层 MoE 模型本地推理引擎 | 中（本地 LLM 基础设施） | 低 |
| 9 | ZhuLinsen/daily_stock_analysis | 73585 | +73 | +1716 | Python | AI 交易/量化 | LLM 驱动多市场股票分析系统 | 高（AI 股票分析流水线） | 低 |
| 10 | vinta/awesome-python | 336116 | +174 | +1497 | Python | Python 列表 | Python 工具精选列表 | 低（与金融弱相关） | 低 |
| 11 | avelino/awesome-go | 195082 | +195 | +1267 | Go | Go 列表 | Go 框架与库精选列表 | 低（与金融弱相关） | 中 |
| 12 | nexu-io/open-design | 108735 | +148 | +1181 | TypeScript | AI 设计工作台 | 协作式 AI 设计 Agent 工作台 | 中（Agent 协作 UI） | 低 |
| 13 | Jakeschincariol/day-trader-skill | 8956 | +131 | +1299 | Python | 日内交易/回测 | 11 个 Claude 日内交易技能 | 高（交易决策 Agent 化） | 低 |
| 14 | ifixai-ai/iFixAi | 46506 | +294 | +1057 | Python | AI 审计/风控 | AI Agent 独立审计工具 | 高（Agent 治理与风控） | 低 |
| 15 | VoltAgent/awesome-design-md | 128464 | +127 | +1034 | 无 | 设计系统 | DESIGN.md 设计系统合集 | 低（与金融弱相关） | 中 |
| 16 | TauricResearch/TradingAgents | 123327 | +114 | +839 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高（多 Agent 交易架构） | 低 |
| 17 | CopilotKit/OpenBot | 13093 | +91 | +937 | TypeScript | AI Bot 框架 | 开源可自托管 AI Bot 框架 | 中（Agent 编排） | 中 |
| 18 | punkpeye/awesome-mcp-servers | 98336 | +50 | +650 | 无 | MCP 列表 | MCP 服务器合集 | 中（MCP 生态） | 低 |
| 19 | jaywcjlove/awesome-mac | 119004 | +75 | +513 | Swift | macOS 软件列表 | macOS 软件精选列表 | 低（与金融弱相关） | 低 |
| 20 | hesreallyhim/awesome-claude-code | 58485 | +81 | +524 | Python | Claude Code 列表 | Claude Code 资源精选 | 中（Agent 技能生态） | 低 |
| 21 | microsoft/BitNet | 42353 | +70 | +777 | C++ | 1-bit LLM 推理 | 1-bit LLM 官方推理框架 | 中（低资源 LLM 推理） | 低 |
| 22 | headroomlabs-ai/headroom | 80226 | +42 | +611 | Python | LLM 上下文压缩 | LLM 工具输出压缩代理 | 高（降低 Agent 推理成本） | 低 |
| 23 | ripienaar/free-for-dev | 143291 | +53 | +502 | HTML | 免费资源列表 | 开发者免费资源列表 | 低（与金融弱相关） | 低 |
| 24 | ruvnet/ruflo | 82182 | +54 | +523 | TypeScript | Agent 编排 | 多智能体集群编排框架 | 中（Agent 基础设施） | 低 |
| 25 | punkpeye/awesome-remote-mcp-servers | 3701 | +67 | +533 | 无 | MCP 列表 | 远程 MCP 服务器合集 | 中（MCP 生态） | 中 |
| 26 | kaankiziltug/logo-design-skill | 7435 | +58 | +563 | HTML | AI 技能/设计 | Logo 设计 AI 技能包 | 低（与金融弱相关） | 低 |
| 27 | Hithink-Tech-Org/Financial-API | 4535 | +168 | +397 | TypeScript | 金融数据/量化 | 同花顺官方 A 股金融数据服务 | 高（A 股数据基础设施） | 低 |
| 28 | HKUDS/Vibe-Trading | 38631 | +57 | +444 | Python | AI 交易/回测 | 个人交易 Agent 框架 | 高（LLM 交易 Agent） | 低 |
| 29 | sickn33/agentic-awesome-skills | 50065 | +50 | +389 | Python | AI 技能库 | 3000+ 可复用 AI Agent 技能 | 中（技能库生态） | 低 |
| 30 | garrytan/gbrain | 33354 | +30 | +473 | TypeScript | Agent 框架 | 个人 Agent 大脑框架 | 中（Agent 编排） | 低 |
| 31 | shy3130/tick-stock-panel | 8123 | +27 | +381 | Python | 量化工作台 | 自托管 A 股量化工作台 | 高（自托管量化平台） | 低 |
| 32 | TGrpg/awesome-telegram | 1791 | +10 | +501 | JavaScript | Telegram 列表 | Telegram 频道/群组/机器人导航 | 低（引流风险） | 中 |
| 33 | AhmadHassan-BTed/Turnitout-Humanizer | 12494 | +44 | +255 | HTML | 学术规避工具 | 学术抄袭规避工具 | 无（应规避） | 中 |
| 34 | PurpleDoubleD/locally-uncensored | 4519 | +42 | +315 | TypeScript | 本地 AI 工作室 | 本地 AI 桌面工作室 | 低（与金融弱相关） | 低 |
| 35 | GoogleChrome/modern-web-guidance-src | 9613 | +309 | 无 | TypeScript | Web 最佳实践 | Web 最佳实践源码版 | 低（与金融弱相关） | 低 |
| 36 | mw00/project-maya | 3129 | +43 | +248 | C++ | 本地 LLM 推理 | 本地多模型 LLM 推理 | 中（本地 LLM 基础设施） | 低 |
| 37 | openbq-org/OpenBB | 75611 | +24 | +208 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高（金融数据基础设施） | 中 |
| 38 | rust-unofficial/awesome-rust | 60694 | +28 | +169 | Rust | Rust 列表 | Rust 资源精选列表 | 低（与金融弱相关） | 中 |
| 39 | nidhinjs/prompt-master | 16191 | +29 | +248 | 无 | 提示词工程 | 精准提示词生成技能 | 中（提示词工程） | 低 |
| 40 | code-yeongyu/oh-my-openagent | 71037 | +24 | +139 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中（Agent 编排） | 低 |
| 41 | fffaraz/awesome-cpp | 74538 | +18 | +133 | 无 | C++ 列表 | C++ 资源精选列表 | 低（与金融弱相关） | 低 |
| 42 | awesomedata/awesome-public-datasets | 80226 | +14 | +115 | 无 | 数据集列表 | 高质量公开数据集列表 | 中（数据源发现） | 中 |
| 43 | virattt/ai-hedge-fund | 64783 | +17 | +120 | Python | AI 交易/回测 | AI 对冲基金团队模拟 | 高（多 Agent 投研模拟） | 低 |
| 44 | Developer-Y/cs-video-courses | 84901 | +10 | +66 | 无 | 课程列表 | 计算机科学视频课程列表 | 低（与金融弱相关） | 中 |
| 45 | josephmisiti/awesome-machine-learning | 74866 | +11 | +46 | Python | ML 列表 | 机器学习资源精选列表 | 低（与金融弱相关） | 低 |
| 46 | Veloresearch/kinetic | 256 | +64 | 无 | Rust | 本地 LLM 推理 | 本地 AI 推理引擎 | 中（本地 LLM 基础设施） | 低 |
| 47 | vuejs/awesome-vue | 73469 | -2 | -5 | 无 | Vue 列表 | Vue.js 资源精选列表 | 低（与金融弱相关） | 低 |

## 3. 重点项目深度分析

### 3.1 tradermonty/claude-trading-skills
- **解决什么问题**：将股票投资与交易流程（市场分析、技术图表、经济日历、筛选器、策略开发）封装为 Claude Code 可调用的技能包，让编码 Agent 直接参与投研与策略开发。
- **为什么最近值得关注**：7 日涨星 +3171，是交易类技能包中增速最快的项目之一，反映“用 Agent 技能包替代传统量化终端”的需求正在形成。
- **技术栈/架构亮点**：以 Python 技能包形式交付，依赖 Claude Code 的 skill 机制；将数据获取、图表生成、策略开发拆分为独立技能，便于组合调用。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。可借鉴其“技能原子化 + Agent 编排”的思路，将行情获取、技术指标计算、新闻分析、策略回测分别封装为可审计、可组合的技能单元。
- **可能的风险**：策略逻辑未经严格回测验证；技能包可能诱导用户直接生成交易信号；数据源质量与合规性未知；需避免直接接入真实交易 API。

### 3.2 TauricResearch/TradingAgents
- **解决什么问题**：提供多智能体 LLM 金融交易框架，将市场分析、研报解读、交易决策等任务分配给不同角色的 Agent 协作完成。
- **为什么最近值得关注**：总 star 123327，7 日 +839，是“多 Agent 金融交易”方向的代表性项目，且持续有 push。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 角色分工（分析师、交易员、风控等）；LLM 作为决策核心，结合金融数据接口。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其多 Agent 角色分工、Agent 间信息传递、决策链审计等设计可直接迁移到企业级投研 Agent 框架。
- **可能的风险**：策略过拟合风险；LLM 输出不稳定导致交易信号不可复现；回测结果可能无法反映真实交易成本与滑点；需避免直接实盘。

### 3.3 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么最近值得关注**：总 star 73585，7 日 +1716，是 A 股 AI 分析方向的高热度项目，且更新频繁。
- **技术栈/架构亮点**：Python + MIT；多源行情接入、实时新闻处理、LLM 分析、决策看板、自动推送的完整流水线；强调零成本定时运行，适合个人开发者。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“数据采集—新闻分析—LLM 决策—看板展示—自动推送”的流水线设计可作为企业级投研 Agent 的 MVP 参考。
- **可能的风险**：数据源合规性与稳定性；LLM 分析结论不可作为投资依据；自动推送可能放大市场噪音；需注意 A 股数据授权问题。

### 3.4 Hithink-Tech-Org/Financial-API
- **解决什么问题**：同花顺官方提供的 A 股金融数据服务，覆盖实时行情、历史行情、财务报表、指数、板块、涨停等数据，支持 API、MCP、CLI 和 Python。
- **为什么最近值得关注**：24h 涨星 +168，是 A 股数据基础设施方向的新兴项目；官方背景降低了数据合规风险。
- **技术栈/架构亮点**：TypeScript + MIT；支持 REST API、MCP、CLI、Python 多形态接入；明确面向 AI Agent 和量化研究场景；集成 DuckDB。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其“官方数据服务 + MCP 接入”模式可直接作为企业级 Agent 的数据层参考，尤其是 MCP 标准化数据接入方式。
- **可能的风险**：数据服务条款与使用限制；免费额度与商业授权边界；依赖官方 API 的稳定性。

### 3.5 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，支持人工或 Agent 自审计，声称 120 秒内给出结论。
- **为什么最近值得关注**：24h 涨星 +294，7 日 +1057，是 AI Agent 治理与风控方向的新兴项目，与金融场景的合规需求高度契合。
- **技术栈/架构亮点**：Python + Apache-2.0；覆盖 AI 对齐、幻觉检测、提示注入、风险评估等；对齐 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等标准。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。金融场景中 Agent 决策的可审计性、幻觉检测、提示注入防护是刚需，该项目提供了可参考的审计框架。
- **可能的风险**：审计结论的准确性依赖底层检测能力；标准对齐可能存在营销成分；需验证其对金融领域 Agent 的实际覆盖度。

### 3.6 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 与算法交易、回测、组合优化结合，提供个人化的交易 Agent 框架。
- **为什么最近值得关注**：总 star 38631，7 日 +444，来自 HKUDS（香港大学数据科学实验室），学术背景较强。
- **技术栈/架构亮点**：Python + MIT；集成 MCP、多 Agent、回测、组合优化；强调 LLM 驱动的个性化交易体验。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“LLM + 回测 + 组合优化 + MCP”的组合可作为研究型交易 Agent 的原型参考。
- **可能的风险**：策略过拟合；学术项目与实盘差距较大；LLM 决策的可解释性与稳定性不足；需避免直接实盘。

### 3.7 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，通过多个 AI Agent 扮演不同角色（如分析师、交易员、风控）完成投研与交易决策。
- **为什么最近值得关注**：总 star 64783，是“AI 对冲基金”方向的知名项目，持续有更新。
- **技术栈/架构亮点**：Python + MIT；多 Agent 角色模拟；强调投研流程的 Agent 化。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“AI 对冲基金团队”的角色分工与决策流程可作为企业级投研 Agent 的参考。
- **可能的风险**：模拟环境与实盘差距大；策略过拟合；LLM 决策不可复现；需避免直接实盘。

### 3.8 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析、复盘，可自由接入第三方数据源。
- **为什么最近值得关注**：7 日 +381，是 A 股自托管量化工作台方向的新兴项目，技术栈现代（DuckDB、Polars、FastAPI、React）。
- **技术栈/架构亮点**：Python + MIT；DuckDB + Polars 数据处理、FastAPI 后端、React 前端；支持 LLM 策略定制与个股分析；强调自托管与个性化扩展。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“自托管 + 现代数据栈 + LLM 策略定制”的架构可作为中小型量化团队的工作台原型。
- **可能的风险**：个人开源项目维护活跃度不确定；数据源接入需自行验证；回测质量与实盘差距需谨慎评估。

### 3.9 headroomlabs-ai/headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 分块到达 LLM 之前进行压缩，降低 token 消耗，声称编码 Agent 减少 20% token、JSON 场景减少 60-95% token。
- **为什么最近值得关注**：总 star 80226，7 日 +611，是 LLM 上下文工程方向的高热度项目，对金融 Agent 的成本控制有直接价值。
- **技术栈/架构亮点**：Python + Apache-2.0；提供库、代理、MCP 服务器三种形态；支持 FastAPI、LangChain、OpenAI、Anthropic 等生态。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。金融 Agent 常需处理大量行情、新闻、日志数据，上下文压缩可显著降低推理成本并提升响应速度。
- **可能的风险**：压缩可能丢失关键信息，需验证对金融数据的保真度；代理层引入额外延迟；依赖上游 LLM 生态变化。

### 3.10 openbq-org/OpenBB
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、期权、加密、固定收益、宏观经济等数据。
- **为什么最近值得关注**：总 star 75611，是金融数据平台方向的成熟项目，持续更新。
- **技术栈/架构亮点**：Python；覆盖多资产类别；明确面向 AI Agent 场景；提供统一数据接口。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“统一金融数据接口 + AI Agent 友好”的设计可作为企业级数据层的参考。
- **可能的风险**：数据源授权与合规；平台依赖；部分数据可能需要商业订阅。

## 4. 趋势归纳

### 技术趋势
- **Claude Code Skills / Agent 技能包成为交付新形态**：交易、设计、安全、提示词工程等领域均出现“技能包”式项目，将复杂能力封装为 Agent 可调用的原子技能。
- **MCP（Model Context Protocol）成为数据接入标准**：`Financial-API`、`headroom`、`awesome-mcp-servers`、`awesome-remote-mcp-servers` 等项目显示，MCP 正在成为 AI Agent 连接数据源与工具的标准协议。
- **本地 LLM 推理基础设施持续升温**：`colibri`、`BitNet`、`project-maya`、`kinetic` 等项目聚焦低资源、本地化 LLM 推理，为金融场景的数据隐私与成本控制提供基础。
- **LLM 上下文工程成为降本关键**：`headroom` 等项目通过压缩工具输出降低 token 消耗，反映 Agent 规模化落地中的成本优化需求。

### 产品趋势
- **从“交易机器人”转向“交易 Agent 技能包”**：产品交付形态从完整 bot 转向可组合的技能包，降低使用门槛，同时规避部分合规风险。
- **自托管量化工作台兴起**：`tick-stock-panel`、`daily_stock_analysis` 等项目强调自托管、零运维、个性化扩展，满足中小团队与个人开发者的数据隐私需求。
- **AI Agent 审计与治理产品化**：`iFixAi` 将 Agent 审计作为独立产品，反映 AI Agent 经济中对可信度与合规性的需求上升。

### 量化/交易策略趋势
- **多智能体协作成为主流架构**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 均采用多 Agent 角色分工，模拟投研团队协作。
- **LLM 与回测、组合优化结合**：多个项目将 LLM 用于策略生成与个股分析，同时保留传统回测与组合优化模块。
- **A 股市场成为 AI 量化新热点**：`daily_stock_analysis`、`Financial-API`、`tick-stock-panel` 均聚焦 A 股，反映中文金融 AI 生态的快速成长。

### AI Agent 与自动化交易结合趋势
- **Agent 技能化 + MCP 数据接入 + 多智能体协作** 正在形成完整的自动化交易技术栈。
- **风控与审计开始嵌入 Agent 框架**：`iFixAi` 的出现表明，Agent 治理正在从概念走向工程实践。
- **成本控制成为 Agent 规模化落地的关键约束**：上下文压缩、本地推理等技术的兴起与此直接相关。

### 值得后续做原型验证的方向
- 基于 MCP 的 A 股数据接入层 + Claude Code 交易技能包。
- 多智能体投研框架（分析师/交易员/风控角色分工）的企业级改造。
- LLM 上下文压缩在金融新闻与行情流中的应用。
- AI Agent 审计与幻觉检测在交易决策链中的集成。

## 5. 今日灵感清单

1. **MVP：A 股投研 Agent 技能包**：参考 `claude-trading-skills` 与 `Financial-API`，封装“行情获取—技术指标—新闻分析—策略回测”为 Claude Code 可调用的技能，先做离线投研场景。
2. **MVP：多智能体投研沙盒**：参考 `TradingAgents` 与 `ai-hedge-fund`，用 Codex/Agent 自动复现“分析师—交易员—风控”三角色协作的投研 demo，仅使用模拟数据。
3. **调研：MCP 在金融数据接入中的标准化程度**：对比 `Financial-API`、`OpenBB`、`awesome-mcp-servers` 中金融相关 MCP 服务器的覆盖度与可用性。
4. **调研：LLM 上下文压缩对金融数据的保真度**：基于 `headroom` 的思路，测试行情、新闻、财报文本压缩前后的关键信息保留率。
5. **Demo：AI Agent 审计集成**：参考 `iFixAi`，为交易 Agent 的决策链增加幻觉检测与提示注入防护，输出审计日志。
6. **Demo：自托管 A 股量化工作台原型**：参考 `tick-stock-panel` 的 DuckDB + Polars + FastAPI + React 架构，搭建最小可用的“策略 + 监控 + 回测”工作台。
7. **调研：本地 LLM 推理在金融数据隐私场景的可行性**：评估 `colibri`、`BitNet`、`project-maya` 在低资源环境下运行金融分析任务的效果。
8. **Watchlist：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund`**：持续跟踪多智能体交易框架的架构演进与回测方法改进。
9. **Watchlist：`Financial-API`、`OpenBB`**：关注金融数据基础设施的 MCP 化与标准化进展。
10. **Watchlist：`iFixAi`、`headroom`**：关注 Agent 治理与成本控制技术的成熟度，评估企业级引入时机。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多智能体金融交易框架的代表，架构演进值得持续跟踪 |
| HKUDS/Vibe-Trading | 学术背景的 LLM 交易 Agent，关注其回测与组合优化方法 |
| virattt/ai-hedge-fund | AI 对冲基金团队模拟的知名项目，关注其角色分工与决策链设计 |
| tradermonty/claude-trading-skills | 交易技能包的代表，关注“技能化交易”的产品形态演进 |
| Jakeschincariol/day-trader-skill | 日内交易技能包，关注其扫描、新闻跟踪、进出场时机设计 |
| Hithink-Tech-Org/Financial-API | 官方 A 股数据服务，关注其 MCP 接入与数据覆盖扩展 |
| openbq-org/OpenBB | 成熟金融数据平台，关注其 AI Agent 友好接口的演进 |
| ifixai-ai/iFixAi | AI Agent 审计与治理的新兴项目，关注其标准对齐与金融场景覆盖 |
| headroomlabs-ai/headroom | LLM 上下文压缩，关注其在金融数据场景的保真度与成本收益 |
| shy3130/tick-stock-panel | 自托管 A 股量化工作台，关注其现代数据栈架构与 LLM 策略定制 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-11-19.json`，大部分项目具备 24h 涨星数据；个别项目（如 `modern-web-guidance-src`、`kinetic`）7 日涨星缺失，可能因项目较新或基线快照未覆盖。
- **7 日基线**：已提供 `baseline_7d: 2026-11-13.json`，多数项目具备 7 日涨星数据；`modern-web-guidance-src` 与 `kinetic` 的 7 日涨星为 null，属于数据缺失。
- **采集失败**：本次未发现明确采集失败，但 `star_delta_30d` 对所有项目均为 null，说明 30 日基线未纳入本次快照。
- **样本偏差**：候选集存在明显的**关键词误匹配偏差**——大量 awesome-list、UI 设计、本地 LLM 推理、学术工具等项目因描述或 README 中偶然出现 “fintech”“quant”“trading bot”“volatility” 等词而被纳入，实际与金融/量化无关。这导致候选集的金融相关性被稀释，分析时应重点聚焦真正与金融/量化/交易相关的项目。
- **风险标记偏差**：部分项目（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`）因 README 中出现 “trading bot” 等词被标记为 `trading_bot` 风险，但实际并非交易机器人项目，风险等级可能被高估。
