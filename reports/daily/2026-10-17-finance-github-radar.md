# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-17

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：iFixAi 以 24h +366、7d +5560 的涨星速度位居实质项目榜首，聚焦 AI Agent 的独立审计、对齐与合规评估，是当前 AI Agent 经济中最关键的信任基础设施方向。
  2. **多智能体交易框架**：TradingAgents、Vibe-Trading、ai-hedge-fund 等 LLM 多 Agent 交易框架持续活跃，显示“用多角色 LLM 模拟投研团队”的范式仍在快速扩散。
  3. **本地化/自托管金融数据与 AI 基础设施**：CNEquity（A 股数据基础设施）、aurelio-finance（本地个人财务 AI 顾问）、project-maya（本地 MoE 推理）等反映“数据主权 + 本地推理 + 零 API Token”的工程趋势。

- **是否出现新趋势**：出现。AI Agent 的**可审计性、对齐评估、合规映射（EU AI Act、ISO 42001、NIST AI RMF）**开始成为独立高增长赛道，不再只是交易策略的附属品。同时，**Agent Skills 生态**（ui-ux-pro-max-skill、logo-design-skill、agentic-awesome-skills 等）正在快速膨胀，但多数与金融交易无直接关系，属于泛 Agent 工具链。

- **是否出现值得复刻/参考的工程架构**：是。iFixAi 的“120 秒 Agent 审计”产品化思路、CNEquity 的“行级溯源 + PIT 语义 + MCP 原生 + 零 Token”数据工程架构、QuantDinger 的“多租户交易 SaaS + 内置计费/结算”架构，都值得深入研究。

- **是否有明显骗局、过度营销或高风险项目**：本次候选池中未发现明显骗局，但存在大量**关键词误匹配**项目（如 public-apis、awesome-selfhosted、build-your-own-x 等被归入 trading_bot/crypto_trading 分类，实际并非交易项目）。`Financial_freedom`（“最全赚钱投资指南”）具有较强营销色彩，应谨慎对待。所有 crypto_related 项目均需注意资金与合规风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 489826 | +289 | +2485 | Python | API 资源列表 | 免费 API 合集，非交易项目，关键词误匹配 | 低 | 中 |
| 2 | ifixai-ai/iFixAi | 29169 | +366 | +5560 | Python | AI Agent 审计/风控 | 120 秒内审计 AI Agent 是否按预期运行 | 高 | 低 |
| 3 | awesome-selfhosted/awesome-selfhosted | 327771 | +375 | +2361 | 无 | 自托管列表 | 自托管服务列表，非交易项目，关键词误匹配 | 低 | 中 |
| 4 | nextlevelbuilder/ui-ux-pro-max-skill | 136937 | +313 | +2349 | Python | AI 设计技能 | 跨平台 UI/UX 设计智能技能 | 中 | 低 |
| 5 | vinta/awesome-python | 328263 | +239 | +1813 | Python | Python 资源列表 | Python 工具精选列表，关键词误匹配 | 低 | 低 |
| 6 | ruvnet/ruflo | 76153 | +447 | +1846 | TypeScript | 多 Agent 框架 | 多智能体集群与自主工作流编排 | 高 | 低 |
| 7 | VoltAgent/awesome-design-md | 121967 | +150 | +1769 | 无 | 设计系统 | DESIGN.md 设计系统集合，关键词误匹配 | 低 | 中 |
| 8 | codecrafters-io/build-your-own-x | 554163 | +295 | +1734 | Markdown | 教程合集 | 从零复刻技术项目教程，关键词误匹配 | 低 | 中 |
| 9 | nexu-io/open-design | 101999 | +312 | +1554 | TypeScript | 协作 AI 设计 | 本地优先的协作式 AI 设计工作台 | 中 | 低 |
| 10 | JustVugg/colibri | 42628 | +174 | +1555 | C | 本地 MoE 推理 | 纯 C 零依赖流式 MoE 推理引擎 | 中 | 低 |
| 11 | LosaLosSantos/aurelio-finance | 3951 | +5 | +1856 | Python | 个人财务 AI | 本地自托管个人财务 AI 顾问 | 高 | 低 |
| 12 | TauricResearch/TradingAgents | 111779 | +220 | +1241 | Python | 多 Agent 交易 | 多智能体 LLM 金融交易框架 | 高 | 低 |
| 13 | avelino/awesome-go | 188974 | +181 | +1194 | Go | Go 资源列表 | Go 框架库精选，关键词误匹配 | 低 | 中 |
| 14 | awesome-dsh-plugin/awesome-dsh-plugin | 19197 | +162 | +865 | JavaScript | DSH 插件列表 | DeepSeek Harness 插件精选 | 中 | 低 |
| 15 | kaankiziltug/logo-design-skill | 3620 | +83 | +950 | HTML | Logo 设计技能 | AI Agent Logo 设计技能包 | 低 | 低 |
| 16 | MakazhanAlpamys/Soup | 9283 | +82 | +768 | Python | LLM 微调 | 单 YAML 低显存微调 8B 模型 | 中 | 低 |
| 17 | ZhuLinsen/daily_stock_analysis | 66650 | +167 | +497 | Python | A 股分析 | LLM 多市场股票智能分析系统 | 高 | 低 |
| 18 | HKUDS/Vibe-Trading | 35739 | +83 | +577 | Python | AI 交易 Agent | 个人交易 Agent，多 Agent + MCP | 高 | 中 |
| 19 | headroomlabs-ai/headroom | 75607 | +69 | +634 | Python | Token 压缩 | LLM 上下文压缩库/代理/MCP | 中 | 低 |
| 20 | mw00/project-maya | 1014 | +50 | +697 | C++ | 本地 MoE 推理 | 私有化运行 GLM-5.3-Flash 321B MoE | 中 | 低 |
| 21 | ripienaar/free-for-dev | 139732 | +62 | +405 | HTML | 免费资源列表 | 开发者免费套餐列表，关键词误匹配 | 低 | 低 |
| 22 | hesreallyhim/awesome-claude-code | 55917 | +52 | +509 | Python | Claude Code 资源 | Claude Code 技能/插件精选 | 中 | 低 |
| 23 | punkpeye/awesome-mcp-servers | 96533 | +43 | +446 | 无 | MCP 服务器列表 | MCP 服务器集合 | 中 | 低 |
| 24 | codeman008/Financial_freedom | 7459 | +72 | +589 | 无 | 投资指南 | “最全赚钱投资指南”，营销色彩强 | 低 | 中 |
| 25 | punkpeye/awesome-remote-mcp-servers | 1431 | +69 | +392 | 无 | 远程 MCP 列表 | 远程 MCP 服务器集合 | 中 | 中 |
| 26 | anbeime/skill | 8237 | +61 | +428 | Python | Skills 商店 | AI Agent 技能商店，含 finance-skill | 中 | 低 |
| 27 | sickn33/agentic-awesome-skills | 47789 | +52 | +348 | Python | Agent 技能控制面 | 本地 Agent-first 技能目录控制面 | 中 | 低 |
| 28 | Fincept-Corporation/FinceptTerminal | 32660 | +70 | +290 | C++ | 金融终端 | 现代金融分析终端，类 Bloomberg | 高 | 低 |
| 29 | openbq-org/OpenBB | 74367 | +56 | +280 | Python | 开放数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高 | 中 |
| 30 | freqtrade/freqtrade | 55532 | +53 | +296 | Python | 加密交易机器人 | 开源加密交易机器人 | 高 | 中 |
| 31 | shiyu-coder/Kronos | 40918 | +69 | +436 | Python | 金融基础模型 | 金融市场语言基础模型 | 高 | 低 |
| 32 | rootSunc/CNEquity | 645 | +66 | +293 | Python | A 股数据基础设施 | 55 个日更 A 股数据集，PIT 语义，MCP 原生 | 高 | 低 |
| 33 | microsoft/BitNet | 41184 | +5 | +598 | C++ | 1-bit LLM 推理 | 微软 1-bit LLM 官方推理框架 | 中 | 低 |
| 34 | plugin87/ux-ui-agent-skills | 2040 | +22 | +468 | JavaScript | UI/UX Agent 技能 | 设计架构师 Agent 技能，50 个客观门禁 | 中 | 低 |
| 35 | CopilotKit/OpenBot | 6600 | +29 | +285 | TypeScript | AI 数字员工 | 每个 Agent 拥有独立浏览器/文件/工具的 AI 同事 | 高 | 中 |
| 36 | nidhinjs/prompt-master | 14561 | +30 | +278 | 无 | Prompt 工程 | 为任意 AI 工具生成准确 Prompt 的技能 | 低 | 低 |
| 37 | garrytan/gbrain | 30960 | +31 | +204 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 38 | code-yeongyu/oh-my-openagent | 70149 | +30 | +199 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中 | 低 |
| 39 | OpenByteInc/QuantDinger | 12873 | +27 | +224 | Python | AI 交易 OS | 开源 AI 交易 OS，多租户交易 SaaS | 高 | 中 |
| 40 | rust-unofficial/awesome-rust | 59928 | +28 | +161 | Rust | Rust 资源列表 | Rust 资源精选，关键词误匹配 | 低 | 低 |
| 41 | AIPentest/CyberStrikeAI | 7869 | +16 | +317 | Go | AI 网络安全 | AI 原生网络安全行动系统 | 中 | 低 |
| 42 | elementalsouls/Claude-BugHunter | 5149 | +19 | +277 | Python | 安全技能包 | Claude Code 漏洞挖掘/红队技能包 | 中 | 低 |
| 43 | awesomedata/awesome-public-datasets | 79579 | +17 | +160 | 无 | 公开数据集 | 高质量公开数据集列表，关键词误匹配 | 低 | 中 |
| 44 | fffaraz/awesome-cpp | 73873 | +23 | +142 | 无 | C++ 资源列表 | C++ 框架库精选，关键词误匹配 | 低 | 低 |
| 45 | virattt/ai-hedge-fund | 64065 | +25 | +136 | Python | AI 对冲基金 | 多 Agent AI 对冲基金团队模拟 | 高 | 低 |
| 46 | josephmisiti/awesome-machine-learning | 74605 | +8 | +37 | Python | ML 资源列表 | 机器学习资源精选，关键词误匹配 | 低 | 低 |
| 47 | Developer-Y/cs-video-courses | 83689 | +2 | +38 | 无 | CS 课程列表 | 计算机科学视频课程列表，关键词误匹配 | 低 | 中 |
| 48 | nicorobinreal/llmspeed | 85 | +77 | 信息不足 | TypeScript | LLM 推理基准 | 购买硬件前测试本地 LLM 推理速度 | 中 | 低 |
| 49 | vuejs/awesome-vue | 73514 | -2 | -1 | 无 | Vue 资源列表 | Vue 资源精选，关键词误匹配 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 ifixai-ai/iFixAi

- **解决什么问题**：AI Agent 经济中最核心的信任问题——“Agent 是否在做它该做的事”。提供由人或 Agent 自身运行的独立审计，声称 120 秒内给出答案。
- **为什么最近值得关注**：7 天涨星 +5560，是本次候选池中除大型资源列表外涨星最快的实质项目。AI Agent 从“能跑”进入“可审计、可合规”阶段，这是企业级 Agent 落地的关键缺口。
- **技术栈/架构亮点**：Python + Apache-2.0；topics 覆盖 agent-evaluation、ai-alignment、ai-governance、ai-safety、hallucination-detection、prompt-injection、llm-security；显式映射 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架。提供 CLI 与诊断工具形态。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。交易 Agent 的决策审计、幻觉检测、prompt 注入防护、合规留痕，都可以参考其“审计即产品”的思路。可将其评估门禁集成到交易 Agent 的 pre-trade/post-trade 流程中。
- **可能的风险**：项目较新（2026-04 创建），审计标准本身的可信度与覆盖率需验证；120 秒审计的深度可能有限；合规映射的准确性需专业法务复核。

### 3.2 TauricResearch/TradingAgents

- **解决什么问题**：用多智能体 LLM 框架模拟金融投研团队，覆盖分析师、研究员、交易员、风控等多角色协作，辅助交易决策。
- **为什么最近值得关注**：总 star 111779，24h +220，7d +1241，是“LLM 多 Agent 交易”范式的代表性项目，持续活跃。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 角色分工 + LLM 决策链；topics 含 agent、finance、llm、multiagent、trading。架构上强调角色化 Agent 协作而非单模型端到端预测。
- **是否适合借鉴**：适合。其“多角色辩论/分工”模式可迁移到企业级投研 Agent、风控 Agent、合规 Agent 的编排中。但应将其定位为研究工具，而非直接实盘系统。
- **可能的风险**：策略过拟合、回测幸存者偏差、LLM 幻觉导致错误信号、API key 安全、金融合规。项目自身标记为 likely_research_tool，不应直接用于实盘。

### 3.3 rootSunc/CNEquity

- **解决什么问题**：中国 A 股数据基础设施。55 个日更数据集，覆盖行情、基本面、期货、资金面、公告事件、指数行业、宏观与风险；强调行级溯源、PIT（Point-in-Time）语义、复权与历史成分内置、MCP 原生、自托管、零注册零 API Token。
- **为什么最近值得关注**：虽然 star 仅 645，但 24h +66、7d +293，增速极快。其“数据工程 + MCP 原生 + 零 Token”的组合精准命中量化数据工程的痛点。
- **技术栈/架构亮点**：Python + Apache-2.0；topics 含 duckdb、parquet、polars、mcp、point-in-time、akshare、tushare。PIT 语义是避免回测前视偏差的关键设计，行级溯源是数据治理的亮点。
- **是否适合借鉴**：非常适合。企业级量化数据平台、AI Agent 的数据访问层、回测数据治理，都可以参考其 PIT + 行级溯源 + MCP 的设计。是本次候选池中数据工程价值最高的项目之一。
- **可能的风险**：项目较新，数据源稳定性与合规性需验证；A 股数据授权边界需注意；维护活跃度待观察。

### 3.4 LosaLosSantos/aurelio-finance

- **解决什么问题**：开源个人财务应用，内置 AI 财务顾问，在本地追踪净资产、投资、ETF、现金与债务。
- **为什么最近值得关注**：7d +1856 的涨星对仅 3951 star 的项目来说非常突出，说明“本地优先 + AI 财务顾问”的需求正在爆发。
- **技术栈/架构亮点**：Python + MIT；topics 含 self-hosted、portfolio-tracker、net-worth、llm、financial-planning、wealth-management。强调本地运行，数据不出本机。
- **是否适合借鉴**：适合。其“本地自托管 + LLM 财务顾问”的产品形态可迁移到企业级财富管理、个人金融数据聚合、隐私优先的 AI 投顾 MVP。
- **可能的风险**：AI 财务建议的合规风险；本地数据安全；LLM 幻觉导致的错误财务建议；项目较新，维护活跃度待观察。

### 3.5 OpenByteInc/QuantDinger

- **解决什么问题**：开源 AI 交易 OS，支持 Agent 交易、vibe trading、Python 策略研究、回测、模拟/实盘交易，覆盖 crypto、股票、外汇；并可启动多租户交易 SaaS，内置用户管理、计费、支付与结算。
- **为什么最近值得关注**：将“交易系统”与“SaaS 多租户商业化”结合，是交易基础设施产品化的典型样本。
- **技术栈/架构亮点**：Python + Apache-2.0；topics 含 alpaca、binance、mcp-server、saas、typesafe-ai、jev。多租户 + 内置计费/结算的架构设计值得研究。
- **是否适合借鉴**：适合作为“交易 SaaS 产品架构”参考，但不应直接用于实盘。其多租户、计费、结算模块对金融科技产品设计有参考价值。
- **可能的风险**：crypto_related、likely_research_tool；多交易所 API key 管理风险；多租户下的资金隔离与合规风险；vibe trading 概念本身存在过度营销风险。

### 3.6 ZhuLinsen/daily_stock_analysis

- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么最近值得关注**：总 star 66650，24h +167，是 A 股 AI 分析领域的高活跃项目。
- **技术栈/架构亮点**：Python + MIT；topics 含 a-stock、ai-agent、llm、quant、quantitative-finance。强调多源数据融合 + 自动推送 + 零成本定时运行。
- **是否适合借鉴**：适合。其“多源数据 + LLM 分析 + 决策看板 + 自动推送”的流水线可复刻为个人或企业级投研日报 MVP。
- **可能的风险**：LLM 分析结果的可靠性；A 股数据合规；自动推送可能放大错误信号；策略过拟合风险。

### 3.7 HKUDS/Vibe-Trading

- **解决什么问题**：定位为“你的个人交易 Agent”，结合 LLM、多 Agent、MCP，支持算法交易、回测与量化金融研究。
- **为什么最近值得关注**：HKUDS 出品，总 star 35739，7d +577，是学术机构在 AI 交易 Agent 方向的代表性工作。
- **技术栈/架构亮点**：Python + MIT；topics 含 ai-agent、algorithmic-trading、backtesting、llm、mcp、multi-agent、quantitative-finance。MCP 集成是亮点，便于工具调用与数据接入。
- **是否适合借鉴**：适合作为研究原型参考，尤其是 MCP 在交易 Agent 工具链中的应用。但“vibe trading”定位偏营销，需谨慎。
- **可能的风险**：crypto_related、likely_research_tool；策略过拟合；回测造假风险；不应直接实盘。

### 3.8 Fincept-Corporation/FinceptTerminal

- **解决什么问题**：现代金融终端，提供市场分析、投资研究与经济数据工具，定位类 Bloomberg Terminal 的开源替代。
- **为什么最近值得关注**：总 star 32660，C++ 实现，topics 含 bloomberg-terminal、qt、algorithmic-trading、quantitative-finance。是开源金融终端方向的重要项目。
- **技术栈/架构亮点**：C++ + Qt；topics 含 ai-agents、machine-learning、python、cpp。桌面端 + 多资产分析的产品形态。
- **是否适合借鉴**：适合。金融终端的产品交互、数据组织、多资产分析模块设计值得参考，尤其是桌面端高性能金融应用架构。
- **可能的风险**：C++ 项目维护成本高；数据源授权；AI 分析模块的可靠性；license 为 Other，商用需注意。

### 3.9 virattt/ai-hedge-fund

- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作进行投资研究与决策。
- **为什么最近值得关注**：总 star 64065，是“AI 对冲基金”概念的开源标杆项目。
- **技术栈/架构亮点**：Python + MIT；多 Agent 角色模拟。项目自身标记为 likely_research_tool。
- **是否适合借鉴**：适合作为多 Agent 投研流程的教学与研究原型，不应视为可实盘系统。
- **可能的风险**：策略过拟合、回测幸存者偏差、LLM 幻觉、金融合规风险。

### 3.10 CopilotKit/OpenBot

- **解决什么问题**：开源 AI 数字员工，每个 Agent 拥有独立浏览器、文件与工具，所有动作在执行前被决定、执行后被记录，支持任意 AG-UI Agent。
- **为什么最近值得关注**：总 star 6600，7d +285。其“动作前决策 + 动作后记录”的治理模式对交易 Agent 的审计与合规有直接启发。
- **技术栈/架构亮点**：TypeScript + MIT；topics 含 ag-ui、agent-governance、browser-automation、generative-ui、mcp。强调 Agent 治理与可观测性。
- **是否适合借鉴**：适合。其“每个 Agent 独立计算环境 + 全动作记录”的架构可迁移到交易 Agent 的沙箱化执行与审计留痕。
- **可能的风险**：trading_bot 标记；浏览器自动化在金融场景的安全风险；Agent 治理机制的实际强度需验证。

## 4. 趋势归纳

### 技术趋势
- **AI Agent 治理与审计成为独立赛道**：iFixAi、OpenBot 等项目显示，Agent 的可审计性、对齐评估、合规映射正在从附属功能变为核心产品。
- **MCP 成为金融数据与工具接入的事实标准**：CNEquity、Vibe-Trading、QuantDinger、awesome-mcp-servers 等均以 MCP 为数据/工具接入层。
- **本地优先与零 Token 数据基础设施**：CNEquity、aurelio-finance、project-maya、colibri 均强调自托管、零 API Token、本地推理，反映数据主权与成本控制诉求。
- **PIT 语义与行级溯源进入开源量化数据工程**：CNEquity 的 PIT + 行级溯源设计是回测数据治理的重要进步。

### 产品趋势
- **从“交易机器人”到“AI 交易 OS / 交易 SaaS”**：QuantDinger 的多租户交易 SaaS 形态显示交易基础设施正在产品化。
- **个人财务 AI 顾问本地化**：aurelio-finance 代表“隐私优先 + AI 投顾”的产品方向。
- **金融终端开源化**：FinceptTerminal 对标 Bloomberg，开源金融终端持续演进。

### 量化/交易策略趋势
- **多 Agent LLM 投研框架持续扩散**：TradingAgents、Vibe-Trading、ai-hedge-fund 均采用多角色 Agent 协作范式。
- **金融基础模型出现**：Kronos 定位“金融市场语言基础模型”，显示从通用 LLM 到金融专用基础模型的探索。
- **研究工具与实盘系统边界模糊化**：多个项目同时提供回测与实盘接口，需警惕“研究工具直接实盘化”的风险。

### AI Agent 与自动化交易结合趋势
- **Agent 审计 + 交易决策链**：iFixAi 的审计能力与交易 Agent 的 pre-trade/post-trade 流程结合是明确方向。
- **Agent 沙箱化执行**：OpenBot 的“独立计算环境 + 全动作记录”模式可降低交易 Agent 的失控风险。
- **Skills 生态与金融技能包**：anbeime/skill 已出现 finance-skill 分类，金融领域的 Agent Skills 将快速增长。

### 值得后续做原型验证的方向
- 交易 Agent 的决策审计与合规留痕系统
- PIT 语义的 A 股回测数据管道
- 本地自托管个人财务 AI 顾问 MVP
- 多租户交易 SaaS 的计费与结算架构
- 金融基础模型的微调与评估

## 5. 今日灵感清单

1. **MVP：交易 Agent 决策审计日志系统**。参考 iFixAi 与 OpenBot，为现有交易 Agent 增加“动作前决策记录 + 动作后结果回传 + 合规规则门禁”的审计层，输出可追溯的决策日志。
2. **MVP：PIT 回测数据管道**。参考 CNEquity，用 DuckDB + Parquet + Polars 构建一个带 PIT 语义和行级溯源的 A 股日频数据管道，暴露 MCP 接口供 Agent 调用。
3. **调研：MCP 在金融数据接入中的标准化程度**。对比 awesome-mcp-servers、awesome-remote-mcp-servers、CNEquity、Vibe-Trading 的 MCP 实现，评估是否可抽象出统一的金融数据 MCP 规范。
4. **Demo：本地个人财务 AI 顾问**。参考 aurelio-finance，用本地 LLM + 自托管数据构建一个隐私优先的个人净值追踪与 AI 财务分析 MVP。
5. **调研：多 Agent 交易框架的过拟合与回测偏差**。对 TradingAgents、Vibe-Trading、ai-hedge-fund 的回测方法做横向对比，识别幸存者偏差与前视偏差风险点。
6. **Demo：交易 Agent 沙箱化执行环境**。参考 OpenBot，为交易 Agent 构建独立浏览器/文件/工具沙箱，所有动作执行前审批、执行后记录。
7. **调研：金融基础模型 Kronos 的能力边界**。评估 Kronos 在金融时序预测、情绪分析等任务上的表现，判断是否值得微调用于内部投研。
8. **Watchlist：CNEquity、iFixAi、QuantDinger、aurelio-finance、OpenBot**。这些项目在数据工程、Agent 治理、交易 SaaS、本地财务 AI、Agent 沙箱化方向具有高参考价值。
9. **调研：Agent Skills 生态中的金融技能包**。跟踪 anbeime/skill 的 finance-skill 分类，评估可复用的金融 Agent 技能。
10. **原型：交易 SaaS 多租户计费架构**。参考 QuantDinger，设计一个支持多租户、内置计费与结算的交易策略托管平台架构图，验证其可行性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计与合规赛道的标杆，涨星极快，企业级 Agent 治理关键参考 |
| rootSunc/CNEquity | PIT 语义 + 行级溯源 + MCP 原生的 A 股数据基础设施，数据工程价值极高 |
| LosaLosSantos/aurelio-finance | 本地优先个人财务 AI 顾问，产品形态新颖，增速突出 |
| OpenByteInc/QuantDinger | 交易 OS + 多租户 SaaS 架构，交易基础设施产品化样本 |
| CopilotKit/OpenBot | Agent 沙箱化执行与治理，对交易 Agent 审计有直接启发 |
| TauricResearch/TradingAgents | 多 Agent LLM 交易框架代表，持续活跃，适合研究跟踪 |
| HKUDS/Vibe-Trading | 学术机构 AI 交易 Agent，MCP 集成值得关注 |
| shiyu-coder/Kronos | 金融基础模型方向，值得跟踪其能力演进 |
| Fincept-Corporation/FinceptTerminal | 开源金融终端，产品交互与多资产分析参考 |
| mw00/project-maya | 本地 MoE 推理 + 量化工具，适合关注本地推理基础设施演进 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-10-16）与 `baseline_7d`（2026-10-10），1 日与 7 日涨星数据完整，未缺失基线。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 null，无法提供 30 日趋势判断。
- **采集失败**：未发现明显采集失败，但 `llmspeed` 项目缺少 7 日涨星数据（`star_delta_7d` 为 null），可能因项目过新或基线缺失。
- **样本偏差**：候选池存在大量**关键词误匹配**项目，如 public-apis、awesome-selfhosted、build-your-own-x、awesome-python、awesome-go、awesome-vue 等资源列表被归入 trading_bot/crypto_trading/quant_research 分类，实际与金融交易无直接关系。这会导致 Top 表中资源列表类项目占比偏高，真实金融/量化项目的信号被稀释。分析时应重点过滤此类误匹配。
- **分类可信度**：`category_guess` 为自动推断，部分项目（如 colibri、project-maya、Soup）因描述中含 “quant” 等关键词被误归入 quant_research，实际为 LLM 推理/微调项目，需人工甄别。
