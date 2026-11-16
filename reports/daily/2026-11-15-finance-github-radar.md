# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-15

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的股票分析与交易 Agent 技能包**：`daily_stock_analysis`、`claude-trading-skills`、`day-trader-skill`、`trader-skill` 等项目集中爆发，反映“用 Claude/Codex 技能包封装投研流程”成为新的产品形态。
  2. **AI Agent 治理与审计**：`iFixAi` 以“120 秒审计 Agent 是否在做该做的事”为卖点，结合 EU AI Act、ISO 42001、NIST AI RMF 等合规框架，显示 Agent 可观测性/合规审计正在成为独立赛道。
  3. **本地优先的 AI 工作台与多 Agent 编排**：`OpenBot`、`gbrain`、`Orkas`、`ruflo` 等项目强调 local-first、AG-UI、MCP、多 Agent 协作，为构建企业级 Agent 框架提供工程参考。

- **是否出现新趋势**：出现。**“Claude/Codex Skills 即金融产品”** 的趋势非常明显——多个高增长项目本质上是把行情分析、技术图表、经济日历、选股器、交易策略开发封装成可安装的 Agent 技能包，而非传统意义上的独立交易系统。

- **是否出现值得复刻/参考的工程架构**：出现。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“自托管 + DuckDB + Polars + FastAPI + React + LLM 策略定制”组合，都是值得复刻的轻量级量化工作台范式。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中混入大量与金融/量化无关的 awesome-list、UI 设计、安全工具项目，属于查询匹配噪声而非骗局。需要警惕的是 `Turnitout-Humanizer` 这类“绕过 Turnitin/GPTZero 检测”的项目，虽然与交易无关，但存在学术诚信与合规风险。未发现明显以“稳赚策略”为卖点的诈骗型交易项目，但所有带 `trading_bot` 标记的项目都应默认视为高风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 72610 | +297 | +4259 | Python | AI 交易/数据工程/量化研究 | LLM 驱动的多市场股票分析系统，多源行情、新闻、看板与推送 | 高：零成本定时运行 + 决策看板架构 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 150078 | +469 | +3037 | Python | 金融科技产品（噪声） | AI UI/UX 设计技能包 | 低：与金融核心无关 | 低 |
| 3 | JustVugg/colibri | 51438 | +254 | +2268 | C | 量化研究（噪声） | MoE 模型分层推理引擎，GPU/RAM/NVMe 分层加载 | 中：本地推理资源调度思路 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 337501 | +321 | +2250 | 无 | 交易机器人（噪声） | 自托管网络服务列表 | 低：可检索自托管金融工具 | 中 |
| 5 | public-apis/public-apis | 499388 | +289 | +2015 | Python | 加密交易/量化研究（噪声） | 免费 API 合集 | 中：可发现金融数据 API | 中 |
| 6 | tradermonty/claude-trading-skills | 5805 | +806 | +2103 | Python | 回测 | Claude Code 股票投资与交易技能包 | 高：技能包化投研流程 | 低 |
| 7 | CopilotKit/OpenBot | 12482 | +170 | +1973 | TypeScript | 金融科技产品/交易机器人 | 开源 AI 同事，每个 Agent 拥有浏览器、文件与工具 | 高：Agent 治理与动作审计 | 中 |
| 8 | codecrafters-io/build-your-own-x | 562974 | +375 | +1812 | Markdown | 交易机器人（噪声） | 从零重建技术的教程合集 | 低：可学习构建交易系统 | 中 |
| 9 | Jakeschincariol/day-trader-skill | 8062 | +201 | +1826 | Python | 回测/风险管理 | 11 个日内交易 Claude 技能 | 高：交易决策流程技能化 | 低 |
| 10 | ifixai-ai/iFixAi | 45960 | +240 | +1724 | Python | AI 交易/金融科技/风控 | AI Agent 独立审计，120 秒判断 Agent 是否合规 | 高：Agent 审计与合规框架 | 低 |
| 11 | vinta/awesome-python | 335073 | +237 | +1571 | Python | 量化研究（噪声） | Python 工具精选列表 | 低 | 低 |
| 12 | VoltAgent/awesome-design-md | 127714 | +136 | +1505 | 无 | 加密交易/金融科技（噪声） | 品牌设计系统 DESIGN.md 合集 | 低 | 中 |
| 13 | TauricResearch/TradingAgents | 122766 | +138 | +1338 | Python | AI 交易/回测/量化研究 | 多 Agent LLM 金融交易框架 | 高：多 Agent 投研决策架构 | 低 |
| 14 | avelino/awesome-go | 194150 | +167 | +1266 | Go | 回测/加密交易/风控（噪声） | Go 框架与库精选列表 | 低：可检索 Go 交易基础设施 | 中 |
| 15 | garrytan/gbrain | 33112 | +77 | +1314 | TypeScript | 金融科技产品 | OpenClaw/Hermes Agent Brain | 中：Agent 编排参考 | 低 |
| 16 | nexu-io/open-design | 107811 | +126 | +1103 | TypeScript | 金融科技产品/交易基础设施 | 协作式 AI 设计 Agent 工作台 | 低：与金融核心无关 | 低 |
| 17 | elementalsouls/Claude-BugHunter | 6762 | +900 | +1263 | Python | 金融科技产品（噪声） | Claude 漏洞挖掘与红队技能包 | 中：金融系统安全测试思路 | 低 |
| 18 | awesome-dsh-plugin/awesome-dsh-plugin | 24829 | +120 | +934 | JavaScript | 交易基础设施（噪声） | DeepSeek Harness 插件列表 | 低 | 低 |
| 19 | TGrpg/awesome-telegram | 1617 | +97 | +956 | JavaScript | 量化研究/交易机器人（噪声） | Telegram 频道/群组/机器人导航 | 低：可发现交易信号频道 | 中 |
| 20 | ripienaar/free-for-dev | 142951 | +77 | +645 | HTML | 金融科技/量化研究（噪声） | 开发者免费 SaaS/PaaS/IaaS 列表 | 低 | 低 |
| 21 | ruvnet/ruflo | 81838 | +99 | +533 | TypeScript | AI 交易/回测 | Agent harness，多智能体 swarm 编排 | 高：多 Agent 编排与记忆架构 | 低 |
| 22 | headroomlabs-ai/headroom | 79771 | +87 | +588 | Python | AI 交易/风控 | 压缩工具输出、日志、RAG 块以降低 token 消耗 | 高：降低 Agent 上下文成本 | 低 |
| 23 | kaankiziltug/logo-design-skill | 7022 | +81 | +653 | HTML | 金融科技产品（噪声） | Logo 设计技能包 | 低 | 低 |
| 24 | jaywcjlove/awesome-mac | 118629 | +72 | +550 | Swift | 交易基础设施（噪声） | macOS 软件精选 | 低 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 58105 | +78 | +532 | Python | AI 交易/量化研究（噪声） | Claude Code 资源精选 | 中：可发现交易相关技能 | 低 |
| 26 | shy3130/tick-stock-panel | 7893 | +92 | +513 | Python | AI 交易/回测/量化研究 | A 股自托管量化工作台，DuckDB+Polars+FastAPI+React | 高：轻量级量化工作台架构 | 低 |
| 27 | HKUDS/Vibe-Trading | 38348 | +91 | +424 | Python | AI 交易/回测/金融科技 | “Vibe-Trading”个人交易 Agent | 高：学术机构多 Agent 交易框架 | 低 |
| 28 | PurpleDoubleD/locally-uncensored | 4289 | +33 | +676 | TypeScript | AI 交易/量化研究（噪声） | 本地 AI 工作室，聊天/图像/视频/编码 Agent | 低 | 低 |
| 29 | punkpeye/awesome-remote-mcp-servers | 3288 | +61 | +457 | 无 | AI 交易/加密交易/交易基础设施 | 远程 MCP 服务器合集 | 中：可发现金融数据 MCP | 中 |
| 30 | sickn33/agentic-awesome-skills | 49776 | +53 | +390 | Python | 回测 | 2955+ 可复用 AI Agent 技能库 | 中：技能目录与发现机制 | 低 |
| 31 | AhmadHassan-BTed/Turnitout-Humanizer | 12308 | +39 | +336 | HTML | 风控/交易机器人（噪声） | 绕过 Turnitin/GPTZero 检测的“降 AI”工具 | 低：学术诚信风险 | 中 |
| 32 | GoogleChrome/modern-web-guidance | 18503 | +2613 | 信息不足 | 无 | 风控（噪声） | 让编码 Agent 跟上最新 Web 最佳实践 | 低 | 低 |
| 33 | nidhinjs/prompt-master | 16036 | +45 | +300 | 无 | AI 交易/金融科技产品 | 为任意 AI 工具生成精准提示词的 Claude 技能 | 中：提示词工程自动化 | 低 |
| 34 | punkpeye/awesome-mcp-servers | 97748 | +30 | +245 | 无 | 金融科技产品（噪声） | MCP 服务器合集 | 中：可发现金融数据 MCP | 低 |
| 35 | awesomedata/awesome-public-datasets | 80159 | +37 | +170 | 无 | 加密交易（噪声） | 高质量开放数据集列表 | 中：可发现金融数据集 | 中 |
| 36 | openbq-org/OpenBB | 75460 | +27 | +206 | Python | 加密交易/量化研究 | 面向分析师、量化与 AI Agent 的开放数据平台 | 高：金融数据基础设施 | 中 |
| 37 | anbeime/skill | 9606 | +29 | +282 | Python | AI 交易/量化研究 | 技能商店，自动抓取 GitHub 上万个 Skills 项目 | 中：技能分发与发现机制 | 低 |
| 38 | Orkas-AI/Orkas | 9389 | +28 | +269 | JavaScript | 回测 | 本地优先 AI 团队，Commander 协调 16 个内置 Agent | 高：本地多 Agent 编排 | 低 |
| 39 | rust-unofficial/awesome-rust | 60574 | +29 | +161 | Rust | AI 交易/回测/加密交易（噪声） | Rust 代码与资源精选 | 低：可检索 Rust 交易基础设施 | 中 |
| 40 | Jakeschincariol/trader-skill | 1854 | +33 | +277 | Python | 股票市场 | 11 个 Claude 技能，复制信任投资者、跟踪新闻与国会 | 高：投资决策流程技能化 | 低 |
| 41 | code-yeongyu/oh-my-openagent | 70935 | +21 | +141 | TypeScript | 量化研究（噪声） | 图工程 Agent 工具 | 低 | 低 |
| 42 | fffaraz/awesome-cpp | 74450 | +25 | +126 | 无 | 量化研究/交易基础设施（噪声） | C/C++ 框架与库精选 | 低：可检索 C++ 交易基础设施 | 低 |
| 43 | virattt/ai-hedge-fund | 64702 | +20 | +120 | Python | 回测/风控 | AI 对冲基金团队 | 高：多 Agent 对冲基金模拟 | 低 |
| 44 | bex-co/beancount-io | 496 | +158 | 信息不足 | TypeScript | 金融科技产品 | 复式记账，面向人类与 AI Agent 的纯文本会计 | 中：AI Agent 可读的记账系统 | 低 |
| 45 | Developer-Y/cs-video-courses | 84861 | +9 | +125 | 无 | 量化研究/交易机器人（噪声） | 计算机科学视频课程列表 | 低 | 中 |
| 46 | josephmisiti/awesome-machine-learning | 74837 | +6 | +52 | Python | AI 交易（噪声） | 机器学习框架与库精选 | 低 | 低 |
| 47 | vuejs/awesome-vue | 73473 | -1 | -11 | 无 | 量化研究（噪声） | Vue.js 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么最近值得关注**：7 日涨星 +4259，是本次候选集中金融属性最强、涨星最猛的项目，说明“LLM + 股票分析 + 自动化推送”的需求非常旺盛。
- **技术栈/架构亮点**：Python + LLM，多源数据接入，决策看板与自动推送分离，强调零成本定时运行，适合个人开发者低成本搭建。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“数据采集 → LLM 分析 → 看板展示 → 自动推送”的流水线可作为企业级投研 Agent 的原型参考。
- **可能的风险**：金融合规风险（自动推送可能被解读为投资建议）；LLM 输出幻觉可能导致错误分析；数据源稳定性与授权问题；维护活跃度需持续观察。

### 3.2 tradermonty/claude-trading-skills
- **解决什么问题**：为股票投资者和交易者提供 Claude Code 技能包，覆盖市场分析、技术图表、经济日历、选股器和交易策略开发。
- **为什么最近值得关注**：24h 涨星 +806，7d +2103，虽然总 star 仅 5805，但增速极快，代表“技能包化投研”这一新兴产品形态。
- **技术栈/架构亮点**：Python + Claude Skills 机制，将投研流程拆分为可组合的技能模块。
- **是否适合借鉴**：非常适合。企业可以将内部投研 SOP 封装为 Agent 技能包，实现标准化、可审计的投研流程。
- **可能的风险**：策略过拟合风险；技能包可能诱导用户过度依赖 LLM 判断；API key 安全；回测结果可能被夸大。

### 3.3 Jakeschincariol/day-trader-skill
- **解决什么问题**：11 个日内交易 Claude 技能，扫描数千张图表、跟踪突发新闻、计时进出场、在冒险前重放每次结果。
- **为什么最近值得关注**：7d +1826，与 `trader-skill` 同作者，形成“日内交易技能包”系列，反映短线交易者正在积极采用 Agent 技能。
- **技术栈/架构亮点**：Python + Claude Skills，强调“先重放结果再冒险”，有回测/复盘意识。
- **是否适合借鉴**：部分适合。其“扫描 → 跟踪 → 计时 → 重放”的流程可抽象为通用交易决策流水线，但日内交易本身风险极高。
- **可能的风险**：日内交易策略极易过拟合；高频决策依赖实时数据质量；可能诱导用户进行高风险短线交易；金融合规风险。

### 3.4 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，声称 120 秒内给出答案。
- **为什么最近值得关注**：7d +1724，总 star 45960，结合 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架，是 AI Agent 治理赛道的代表性项目。
- **技术栈/架构亮点**：Python + Apache-2.0，覆盖 agent-evaluation、hallucination-detection、prompt-injection、llm-security 等主题，支持人工或 Agent 自审计。
- **是否适合借鉴**：非常适合。在金融交易 Agent 场景中，审计 Agent 行为、检测幻觉与提示注入是刚需，可将其审计思路集成到交易 Agent 风控层。
- **可能的风险**：审计本身的准确性依赖 LLM，可能存在误判；合规框架映射可能流于表面；需验证其审计方法在金融场景的有效性。

### 3.5 TauricResearch/TradingAgents
- **解决什么问题**：多 Agent LLM 金融交易框架，模拟分析师、研究员、交易员等多角色协作进行交易决策。
- **为什么最近值得关注**：总 star 122766，7d +1338，是“多 Agent 交易”方向的标杆项目，学术与研究属性强。
- **技术栈/架构亮点**：Python + Apache-2.0，多 Agent 架构，topic 包含 agent、finance、llm、multiagent、trading。
- **是否适合借鉴**：非常适合。其多 Agent 角色分工（分析师/研究员/交易员）可作为企业级投研 Agent 团队的架构蓝本。
- **可能的风险**：策略过拟合；多 Agent 协作可能放大 LLM 幻觉；回测结果不代表实盘表现；维护活跃度需观察。

### 3.6 shy3130/tick-stock-panel
- **解决什么问题**：A 股自托管、零运维的“自建策略 + 监控 + 回测”量化工作台，支持 LLM 策略定制、个股分析与复盘。
- **为什么最近值得关注**：7d +513，虽然总 star 仅 7893，但技术栈现代（DuckDB、Polars、FastAPI、React），是轻量级量化工作台的优秀范例。
- **技术栈/架构亮点**：Python + DuckDB + Polars + FastAPI + React，自托管零运维，支持第三方数据源接入与个性化扩展。
- **是否适合借鉴**：非常适合。其“本地数据引擎 + 现代 Web 前端 + LLM 策略定制”的组合是构建个人/小团队量化工作台的高性价比方案。
- **可能的风险**：A 股数据合规与授权；策略过拟合；自托管环境的数据安全；LLM 生成策略的可靠性。

### 3.7 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“你的个人交易 Agent”，由香港大学数据科学实验室（HKUDS）推出，结合 LLM、MCP、多 Agent 与回测。
- **为什么最近值得关注**：总 star 38348，7d +424，学术机构背景增加了其研究参考价值。
- **技术栈/架构亮点**：Python + MIT，topic 覆盖 ai-agent、algorithmic-trading、backtesting、fintech、llm、mcp、multi-agent。
- **是否适合借鉴**：适合。学术机构的多 Agent 交易框架通常有较清晰的研究动机与实验设计，可作为研究原型参考。
- **可能的风险**：学术项目可能缺乏生产级稳定性；策略过拟合；MCP 集成可能引入安全风险。

### 3.8 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 扮演不同角色进行投资决策。
- **为什么最近值得关注**：总 star 64702，是“AI 对冲基金”概念的开源代表作，长期受关注。
- **技术栈/架构亮点**：Python + MIT，多 Agent 角色模拟，强调回测与研究属性。
- **是否适合借鉴**：适合作为多 Agent 投研决策的参考实现，但应仅用于研究，不应直接用于实盘。
- **可能的风险**：策略过拟合；回测幸存者偏差；多 Agent 决策可能放大错误；不应将 star 数解读为策略有效性。

### 3.9 CopilotKit/OpenBot
- **解决什么问题**：开源 AI 同事，每个 Agent 拥有自己的浏览器、文件和工具，每个动作在执行前被决定、执行后被记录，支持任意 AG-UI Agent。
- **为什么最近值得关注**：7d +1973，总 star 12482，强调 agent-governance、browser-automation、generative-ui、MCP，是 Agent 治理与可观测性的重要参考。
- **技术栈/架构亮点**：TypeScript + MIT，AG-UI 协议，动作前置决策与后置记录，适合构建可审计的 Agent 工作流。
- **是否适合借鉴**：非常适合。其“动作前置决策 + 后置记录”的治理模式可直接借鉴到交易 Agent 的审计与风控中。
- **可能的风险**：浏览器自动化可能触发网站反爬；Agent 动作记录可能包含敏感信息；与金融交易结合时需额外风控。

### 3.10 ruvnet/ruflo
- **解决什么问题**：Agent harness，部署智能多玩家 swarm，协调自主工作流，构建对话式 AI 系统，支持自适应记忆、自学习、联邦、向量 RAG。
- **为什么最近值得关注**：总 star 81838，7d +533，是多 Agent 编排与记忆架构的成熟参考。
- **技术栈/架构亮点**：TypeScript + MIT，agent-memory、agent-orchestration、swarm-intelligence、MCP、vector-search 等主题。
- **是否适合借鉴**：适合。其自适应记忆与多 Agent 编排机制可为企业级交易 Agent 的上下文管理与协作提供参考。
- **可能的风险**：项目复杂度高，依赖多；自学习机制可能引入不可控行为；与金融交易结合需谨慎。

## 4. 趋势归纳

### 技术趋势
- **Agent Skills 成为新的分发单元**：多个高增长项目以“Claude/Codex Skills”形式封装投研、交易、设计、安全等能力，技能包正在成为 AI Agent 时代的“App Store”单元。
- **MCP 生态持续扩张**：`awesome-mcp-servers`、`awesome-remote-mcp-servers`、`OpenBot`、`Vibe-Trading` 等项目均涉及 MCP，金融数据 MCP 服务器有望成为连接 Agent 与市场数据的标准接口。
- **本地优先与自托管**：`tick-stock-panel`、`Orkas`、`locally-uncensored`、`OpenBot` 等项目强调 local-first、零运维、自托管，反映用户对数据主权与成本控制的关注。
- **轻量级数据栈**：DuckDB、Polars、FastAPI、React 的组合在量化工作台中出现，替代传统重型数据库与后端框架。

### 产品趋势
- **从“交易机器人”到“投研 Agent 技能包”**：产品形态从直接执行交易转向辅助决策、分析、复盘，降低用户对“自动交易”的恐惧，同时规避部分合规风险。
- **Agent 审计与合规成为独立卖点**：`iFixAi` 将 AI Agent 审计产品化，结合 EU AI Act、ISO 42001 等框架，显示 Agent 治理正在从技术话题转向合规刚需。
- **决策看板与自动推送**：`daily_stock_analysis` 等项目的“看板 + 推送”模式，将 LLM 分析结果产品化为可消费的信息流。

### 量化/交易策略趋势
- **多 Agent 角色分工**：分析师、研究员、交易员、风控等角色分工成为主流架构，`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 均采用此模式。
- **回测与复盘前置**：`day-trader-skill` 强调“在冒险前重放每次结果”，反映回测/复盘意识正在被嵌入技能包。
- **A 股量化工作台兴起**：`daily_stock_analysis`、`tick-stock-panel` 均聚焦 A 股，显示中文市场对自托管量化工具的需求旺盛。

### AI Agent 与自动化交易结合趋势
- **动作审计与可观测性**：`OpenBot` 的“动作前置决策 + 后置记录”模式，为交易 Agent 的审计与风控提供了工程范式。
- **上下文成本优化**：`headroom` 通过压缩工具输出、日志、RAG 块降低 token 消耗，对高频调用 LLM 的交易 Agent 具有直接价值。
- **技能包化投研 SOP**：将投研流程拆分为可组合技能，实现标准化、可审计的 Agent 工作流。

### 值得后续做原型验证的方向
- 基于 DuckDB + Polars + FastAPI + React 的轻量级量化研究工作台。
- 将投研 SOP 封装为 Claude/Codex Skills 的标准化流程。
- 交易 Agent 的动作审计与合规检查层（参考 `iFixAi` 与 `OpenBot`）。
- 金融数据 MCP 服务器的标准化接口设计。
- LLM 输出压缩在交易 Agent 上下文管理中的应用。

## 5. 今日灵感清单

1. **MVP：轻量级 A 股投研看板**：参考 `daily_stock_analysis` 与 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭建一个自托管 A 股分析看板，集成 LLM 生成每日摘要与自动推送。
2. **MVP：投研 Agent 技能包**：参考 `claude-trading-skills` 与 `trader-skill`，将“数据采集 → 技术分析 → 新闻跟踪 → 决策建议”封装为可安装的 Claude/Codex 技能包，强调“只辅助决策，不自动下单”。
3. **调研：Agent 审计框架**：深入研究 `iFixAi` 的审计方法，评估其在金融交易 Agent 场景中的适用性，重点关注幻觉检测、提示注入防护与合规框架映射。
4. **调研：MCP 金融数据接口标准化**：分析 `awesome-mcp-servers` 与 `awesome-remote-mcp-servers` 中金融相关 MCP 服务器的接口设计，探索标准化金融数据 MCP 的可行性。
5. **Codex/Agent 自动复现 demo：多 Agent 投研决策**：参考 `TradingAgents` 与 `ai-hedge-fund`，让 Codex 自动搭建一个多角色（分析师/研究员/风控）投研决策 demo，仅用于研究，不接实盘。
6. **原型：交易 Agent 动作审计层**：参考 `OpenBot` 的“动作前置决策 + 后置记录”模式，为交易 Agent 设计一个审计日志层，记录每个动作的输入、决策依据与执行结果。
7. **原型：LLM 上下文压缩**：参考 `headroom`，在交易 Agent 中集成工具输出与日志压缩，降低 token 消耗，验证对决策质量的影响。
8. **Watchlist：`tick-stock-panel`**：关注其 DuckDB + Polars 数据栈的演进，作为轻量级量化工作台的参考实现。
9. **Watchlist：`Vibe-Trading`**：关注 HKUDS 的多 Agent 交易框架后续研究产出，尤其是 MCP 集成与回测方法。
10. **调研：本地优先 Agent 工作台**：分析 `Orkas` 与 `gbrain` 的本地多 Agent 编排架构，评估其在金融数据敏感场景下的应用潜力。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 金融属性最强、涨星最猛，LLM 股票分析流水线值得持续跟踪 |
| tradermonty/claude-trading-skills | “技能包化投研”新形态代表，增速极快 |
| Jakeschincariol/day-trader-skill | 日内交易技能包，观察短线交易者如何采用 Agent 技能 |
| ifixai-ai/iFixAi | Agent 审计与合规赛道代表，金融交易 Agent 风控刚需 |
| TauricResearch/TradingAgents | 多 Agent 交易框架标杆，学术参考价值高 |
| shy3130/tick-stock-panel | 轻量级 A 股量化工作台，现代数据栈范例 |
| HKUDS/Vibe-Trading | 学术机构多 Agent 交易框架，MCP 集成值得关注 |
| virattt/ai-hedge-fund | AI 对冲基金概念代表作，多 Agent 投研参考 |
| CopilotKit/OpenBot | Agent 治理与动作审计范式，可借鉴到交易 Agent 风控 |
| ruvnet/ruflo | 多 Agent 编排与自适应记忆架构，企业级 Agent 框架参考 |
| headroomlabs-ai/headroom | LLM 上下文压缩，对高频交易 Agent 成本优化有直接价值 |
| openbq-org/OpenBB | 金融数据开放平台，可作为 Agent 数据基础设施 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-11-14.json`，与 `current_snapshot` 日期 `2026-11-15` 匹配，1 日涨星数据可信度较高。
- **7 日基线**：存在，`baseline_7d` 为 `2026-11-08.json`，与当前快照间隔 7 天，7 日涨星数据可信度较高。
- **30 日基线**：缺失，所有项目的 `star_delta_30d` 均为 `null`，无法评估中期涨星趋势。
- **采集失败/异常**：`GoogleChrome/modern-web-guidance` 的 7 日涨星为 `null`，但 24h 涨星 +2613，可能存在基线缺失或数据异常；`bex-co/beancount-io` 的 7 日涨星为 `null`，仅 24h 涨星 +158，可能因项目较新或基线未覆盖。
- **样本偏差**：候选集中混入大量与金融/量化无关的 awesome-list、UI 设计、安全工具项目（如 `ui-ux-pro-max-skill`、`awesome-design-md`、`logo-design-skill`、`Claude-BugHunter` 等），这些项目因查询关键词误匹配进入候选集，分析时需注意区分真实金融/量化项目与噪声项目。
