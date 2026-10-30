# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-29

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：iFixAi 以 24h +763 星、7d +4725 星的速度爆发，聚焦 AI Agent 的独立审计、幻觉检测、提示注入检测，并映射到 EU AI Act、ISO 42001、NIST AI RMF 等合规框架。这代表 AI Agent 从“能跑”走向“可审计、可治理”。
  2. **LLM 多智能体交易框架**：TradingAgents 7d +5326 星，是候选中最强的量化/AI 交易信号之一。其“多智能体金融交易框架”形态值得重点研究，但需严格区分研究工具与实盘系统。
  3. **Claude Skills 生态向交易场景渗透**：day-trader-skill 以 24h +608 星、7d +2724 星快速上升，将日内交易扫描、新闻跟踪、进出场时机、结果回放封装为 11 个 Claude skills。这标志着“技能包”正在成为 AI 交易工作流的新交付单元。

- **是否出现新趋势**：出现。AI Agent 的“可审计性”和“技能化封装”成为新热点；同时，大量非金融项目（UI/UX skill、设计系统、本地 AI 桌面应用）因关键词误匹配进入候选，说明当前雷达的查询召回存在明显噪声。

- **是否出现值得复刻/参考的工程架构**：是。TradingAgents 的多智能体协作、iFixAi 的 Agent 审计流水线、Orkas 的本地优先多智能体桌面编排、Vibe-Research 的 168 数据端点投研工作台，均具备可复刻的架构参考价值。

- **是否有明显骗局、过度营销或高风险项目**：候选列表中未发现可直接判定为骗局的项目，但存在明显**关键词误匹配**和**营销化描述**。例如 awesome-selfhosted、public-apis、build-your-own-x 等通用 awesome 列表因描述或 README 中偶然出现“trading bot”等词被召回，并非交易项目。day-trader-skill 的“replay every outcome before you risk a dollar”等表述带有营销色彩，需谨慎对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | awesome-selfhosted | 331895 | +353 | +2489 | null | 自托管列表 | 自托管网络服务与 Web 应用列表 | 低，误匹配 | 中 |
| 2 | ui-ux-pro-max-skill | 142650 | +459 | +3557 | Python | AI UI/UX 技能 | 多平台专业 UI/UX 设计智能技能 | 中，Agent 技能化 | 低 |
| 3 | TradingAgents | 118428 | +427 | +5326 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高，多智能体架构 | 低 |
| 4 | iFixAi | 38013 | +763 | +4725 | Python | AI 审计/治理 | AI Agent 独立审计与合规评估 | 高，Agent 治理 | 低 |
| 5 | day-trader-skill | 3323 | +608 | +2724 | Python | 日内交易技能 | 11 个 Claude 日内交易技能包 | 中，交易工作流 | 低 |
| 6 | FractalWorkspace | 7794 | +574 | +4152 | Python | 联邦学习 | 大规模联邦学习统一工作区 | 低，误匹配 | 低 |
| 7 | Orkas | 4421 | +1126 | +2269 | JavaScript | 多智能体桌面 | 本地优先 AI 团队桌面编排 | 高，Agent 编排 | 低 |
| 8 | public-apis | 493342 | +265 | +1863 | Python | 公共 API 列表 | 免费 API 集合列表 | 低，误匹配 | 中 |
| 9 | awesome-python | 331249 | +245 | +1707 | Python | Python 资源列表 | Python 工具精选列表 | 低，误匹配 | 低 |
| 10 | build-your-own-x | 557406 | +364 | +1868 | Markdown | 教程列表 | 从零复刻技术的教程集合 | 低，误匹配 | 中 |
| 11 | ruflo | 80184 | +164 | +1648 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | 高，Agent 框架 | 低 |
| 12 | colibri | 45017 | +243 | +1582 | C | MoE 推理引擎 | 纯 C 零依赖 MoE 模型推理 | 中，本地推理 | 低 |
| 13 | awesome-design-md | 124555 | +225 | +1548 | null | 设计系统 | 品牌设计系统 DESIGN.md 集合 | 低，误匹配 | 中 |
| 14 | open-design | 104923 | +224 | +1514 | TypeScript | 协作设计 | 协作式 AI 设计 Agent 工作区 | 中，协作 Agent | 低 |
| 15 | awesome-dsh-plugin | 21538 | +157 | +1330 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | 低，误匹配 | 低 |
| 16 | OpenBot | 8307 | +607 | +1346 | TypeScript | AI 浏览器自动化 | 开源 AI 协作者，自带浏览器/文件/工具 | 中，Agent 治理 | 中 |
| 17 | awesome-go | 191084 | +171 | +1233 | Go | Go 资源列表 | Go 框架与库精选列表 | 低，误匹配 | 中 |
| 18 | goose | 2534 | +72 | +1331 | C++ | 编程语言 | Goose 编程语言 | 低，误匹配 | 低 |
| 19 | logo-design-skill | 5303 | +231 | +1106 | HTML | 设计技能 | Logo 设计 AI 技能包 | 低，误匹配 | 低 |
| 20 | Vibe-Trading | 37178 | +116 | +823 | Python | AI 交易 | 个人交易 Agent | 高，AI 交易 | 中 |
| 21 | free-for-dev | 140705 | +212 | +761 | HTML | 免费资源 | SaaS/PaaS/IaaS 免费层列表 | 低，误匹配 | 低 |
| 22 | headroom | 78290 | +113 | +706 | Python | Token 压缩 | LLM 上下文压缩库/代理/MCP | 中，上下文工程 | 低 |
| 23 | awesome-claude-code | 56891 | +103 | +607 | Python | Claude 资源 | Claude Code 资源精选 | 低，误匹配 | 低 |
| 24 | cs-video-courses | 84274 | +84 | +530 | null | 课程列表 | 计算机科学视频课程列表 | 低，误匹配 | 中 |
| 25 | Kronos | 44087 | +56 | +843 | Python | 金融基础模型 | 金融市场语言基础模型 | 高，金融 LLM | 低 |
| 26 | agentic-awesome-skills | 48771 | +82 | +426 | Python | Agent 技能库 | 2877+ 可复用 AI Agent 技能 | 中，技能生态 | 低 |
| 27 | locally-uncensored | 3037 | +80 | +553 | TypeScript | 本地 AI 桌面 | 本地 AI 工作室桌面应用 | 低，误匹配 | 低 |
| 28 | awesome-remote-mcp-servers | 2232 | +64 | +473 | null | MCP 列表 | 远程 MCP 服务器集合 | 低，误匹配 | 中 |
| 29 | Vibe-Research | 3404 | +28 | +623 | TypeScript | 投研工作台 | A/美/港股投研工作台，168 数据端点 | 高，投研数据工程 | 低 |
| 30 | tick-stock-panel | 6471 | +93 | +237 | Python | A 股量化工作台 | 自托管 A 股策略+监控+回测 | 高，量化工作台 | 低 |
| 31 | daily_stock_analysis | 67276 | +42 | +368 | Python | 股票分析 | LLM 多市场股票分析系统 | 中，LLM 分析 | 低 |
| 32 | skill | 8912 | +65 | +375 | Python | 技能商店 | AI Agent 技能商店 | 中，技能生态 | 低 |
| 33 | OpenBB | 74888 | +42 | +322 | Python | 开放数据平台 | 分析师/量化/AI Agent 开放数据平台 | 高，数据平台 | 中 |
| 34 | prompt-master | 15263 | +46 | +364 | null | 提示工程 | 精准提示词生成技能 | 低，误匹配 | 低 |
| 35 | awesome-mcp-servers | 97055 | +41 | +286 | null | MCP 列表 | MCP 服务器集合 | 低，误匹配 | 低 |
| 36 | oh-my-openagent | 70490 | +39 | +208 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中，Agent 编排 | 低 |
| 37 | gbrain | 31343 | +27 | +259 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | 中，Agent 框架 | 低 |
| 38 | CyberStrikeAI | 8237 | +50 | +244 | Go | AI 安全 | AI 原生网络安全行动系统 | 中，Agent 治理 | 低 |
| 39 | awesome-mac | 117360 | +67 | null | Swift | macOS 软件列表 | macOS 软件精选列表 | 低，误匹配 | 低 |
| 40 | ai-hedge-fund | 64358 | +26 | +195 | Python | AI 对冲基金 | AI 对冲基金团队 | 高，多智能体交易 | 低 |
| 41 | awesome-public-datasets | 79847 | +17 | +157 | null | 数据集列表 | 高质量开放数据集列表 | 低，误匹配 | 中 |
| 42 | awesome-rust | 60199 | +22 | +162 | Rust | Rust 资源列表 | Rust 代码与资源精选 | 低，误匹配 | 低 |
| 43 | awesome-cpp | 74100 | +17 | +147 | null | C++ 资源列表 | C/C++ 框架与库精选 | 低，误匹配 | 低 |
| 44 | awesome-machine-learning | 74691 | +5 | +46 | Python | ML 资源列表 | 机器学习框架与库精选 | 低，误匹配 | 低 |
| 45 | awesome-vue | 73497 | -2 | -18 | null | Vue 资源列表 | Vue.js 相关资源精选 | 低，误匹配 | 低 |

## 3. 重点项目深度分析

### 3.1 TradingAgents（TauricResearch/TradingAgents）

- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，试图用多个角色化 Agent（如分析师、交易员、风控）共同完成交易研究与决策。
- **为什么最近值得关注**：7d +5326 星，是候选中最强的量化/AI 交易信号；Apache-2.0 许可，Python 实现，近 30 天有 push，维护活跃。
- **技术栈/架构亮点**：多智能体编排、LLM 驱动、topic 覆盖 agent/finance/llm/multiagent/trading。架构上可参考其角色分工与消息传递设计。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合作为**研究型多智能体框架**参考，尤其是角色化 Agent 的职责划分、决策流水线设计。但不应直接用于实盘。
- **可能的风险**：策略过拟合、回测幸存者偏差、LLM 幻觉导致错误交易信号、API key 安全、金融合规边界模糊。风险标记为 likely_research_tool，风险等级低，但实盘化风险极高。

### 3.2 iFixAi（ifixai-ai/iFixAi）

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，覆盖幻觉检测、提示注入、AI 对齐、合规评估。
- **为什么最近值得关注**：24h +763 星、7d +4725 星，爆发力极强；Apache-2.0，Python；topic 覆盖 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM，直接对接监管框架。
- **技术栈/架构亮点**：CLI 工具、诊断工具、LLM 评估、风险评分。其“120 秒内给出审计答案”的定位暗示了自动化审计流水线。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。交易 Agent 尤其需要可审计性、幻觉检测、提示注入防护和合规映射。可将 iFixAi 的审计思路引入交易 Agent 的 pre-trade/post-trade 检查环节。
- **可能的风险**：审计工具本身依赖 LLM，存在“用 LLM 审计 LLM”的循环依赖问题；合规映射的准确性需人工复核；项目较新，长期维护活跃度待观察。

### 3.3 day-trader-skill（Jakeschincariol/day-trader-skill）

- **解决什么问题**：将日内交易工作流封装为 11 个 Claude skills，包括图表扫描、突发新闻跟踪、进出场时机、结果回放。
- **为什么最近值得关注**：24h +608 星、7d +2724 星，项目创建于 2026-10-20，极新且增速极快；MIT 许可。
- **技术栈/架构亮点**：基于 Claude Skills 的模块化封装，将交易决策拆分为可复用技能单元。这种“技能包”形态是 AI 交易工作流的新交付方式。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合借鉴其**技能化拆分**思路，将行情扫描、新闻分析、信号生成、复盘等环节封装为独立技能，便于组合与审计。但不应直接用于实盘。
- **可能的风险**：营销化描述明显（“replay every outcome before you risk a dollar”）；日内交易策略本身高风险；技能质量与信号有效性未经独立验证；可能诱导用户输入真实交易凭证。

### 3.4 Orkas（Orkas-AI/Orkas）

- **解决什么问题**：本地优先的桌面 AI 团队，Commander 将目标拆解为待办，协调 16 个内置专家 Agent 及 Claude Code、Codex、OpenCode 等。
- **为什么最近值得关注**：24h +1126 星，是候选中单日涨星最高的项目之一；MIT 许可，JavaScript；近 30 天有 push。
- **技术栈/架构亮点**：本地优先、多智能体编排、项目/定时自动化/连接器。其“Commander + 专家 Agent”架构可作为企业级 Agent 编排的参考。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。交易研究团队可借鉴其“Commander 拆解目标 + 专家 Agent 执行”的模式，构建本地优先的投研 Agent 团队。
- **可能的风险**：项目较新，生态成熟度低；多智能体协作的可靠性与成本控制待验证；本地优先架构在数据同步与安全上需额外设计。

### 3.5 Vibe-Trading（HKUDS/Vibe-Trading）

- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多智能体与回测，提供 AI 驱动的交易决策。
- **为什么最近值得关注**：HKUDS 出品，7d +823 星；MIT 许可，Python；topic 覆盖 ai-agent、algorithmic-trading、backtesting、fintech、mcp、multi-agent。
- **技术栈/架构亮点**：MCP 集成、多智能体、回测模块。其“Vibe-Trading”命名暗示了轻量化、对话式交易交互。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合作为 AI 交易 Agent 的产品形态参考，尤其是 MCP 与多智能体的结合。但需严格区分研究用途与实盘。
- **可能的风险**：crypto_related 标记，加密货币交易合规风险高；策略有效性未经验证；可能诱导用户连接真实交易所 API。

### 3.6 Kronos（shiyu-coder/Kronos）

- **解决什么问题**：构建“金融市场语言基础模型”，试图用基础模型方法建模金融时间序列。
- **为什么最近值得关注**：7d +843 星，总 star 44087；MIT 许可，Python；定位独特，是金融 LLM 方向的代表性项目。
- **技术栈/架构亮点**：基础模型路线，面向金融时间序列的预训练与微调。可参考其数据预处理、序列建模与评估方法。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合作为**研究方向**参考，尤其是金融时序基础模型的训练与评估。但距离可部署的交易系统较远。
- **可能的风险**：pushed_at 为 2026-04-13，近 6 个月无 push，维护活跃度存疑；基础模型在金融场景的泛化性与过拟合风险需警惕。

### 3.7 Vibe-Research（simonlin1212/Vibe-Research）

- **解决什么问题**：A 股、美股、港股的投研工作台，提供自选与持仓、每日复盘、产业资讯、个股深挖、回测、研报库，168 个数据端点。
- **为什么最近值得关注**：7d +623 星，TypeScript，MIT；topic 覆盖 a-stock、hk-stocks、us-stocks、mcp、claude-code、codex。
- **技术栈/架构亮点**：多市场数据整合、168 个数据端点、MCP 集成、支持 Claude Code/Codex/WorkBuddy。数据工程与 Agent 集成的结合是亮点。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其“多市场数据端点 + 投研工作台 + Agent 集成”模式可作为企业级投研 Agent 的原型参考。
- **可能的风险**：数据源合规性与稳定性；A 股数据接入的合规边界；项目较新，生态与文档成熟度待观察。

### 3.8 tick-stock-panel（shy3130/tick-stock-panel）

- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析、复盘。
- **为什么最近值得关注**：24h +93 星，Python，MIT；topic 覆盖 duckdb、polars、fastapi、react、backtesting、quant。
- **技术栈/架构亮点**：DuckDB + Polars + FastAPI + React 的现代数据栈，LLM 驱动策略定制。自托管与零运维定位适合个人量化研究。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“DuckDB + Polars 本地数据引擎 + LLM 策略生成”的组合可作为轻量级量化研究 MVP 的技术选型参考。
- **可能的风险**：A 股数据合规；策略过拟合；LLM 生成策略的可靠性；项目规模较小，维护活跃度需观察。

### 3.9 ai-hedge-fund（virattt/ai-hedge-fund）

- **解决什么问题**：模拟 AI 对冲基金团队，用多智能体协作完成投资决策。
- **为什么最近值得关注**：总 star 64358，7d +195；MIT 许可，Python；是 AI 多智能体交易领域的知名参考项目。
- **技术栈/架构亮点**：多智能体角色分工（如分析师、研究员、交易员、风控），回测模块。架构清晰，适合学习多智能体交易系统设计。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合作为**教学与研究参考**，尤其是多智能体角色设计与决策流水线。但不应直接用于实盘。
- **可能的风险**：策略过拟合、回测偏差、LLM 幻觉、金融合规风险。风险标记为 likely_research_tool。

### 3.10 OpenBB（openbq-org/OpenBB）

- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、期权、加密、固定收益、经济数据等。
- **为什么最近值得关注**：总 star 74888，7d +322；Python；topic 覆盖 ai、crypto、derivatives、equity、fixed-income、quantitative-finance。
- **技术栈/架构亮点**：统一数据访问层，面向 AI Agent 的数据接口设计。可作为量化数据工程的基础设施参考。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“统一数据平台 + AI Agent 接口”思路可借鉴到企业级投研数据中台建设。
- **可能的风险**：crypto_related 标记；数据源合规与稳定性；平台依赖风险。

## 4. 趋势归纳

### 技术趋势

1. **多智能体编排成为 AI 交易/投研的主流架构**：TradingAgents、Vibe-Trading、ai-hedge-fund、ruflo、Orkas 均采用多智能体协作模式，角色分工（分析师/交易员/风控）成为共识。
2. **MCP（Model Context Protocol）成为 Agent 数据接入标准**：Vibe-Trading、Vibe-Research、headroom、awesome-mcp-servers 等均涉及 MCP，数据源与工具接入正在标准化。
3. **本地优先与自托管趋势明显**：Orkas、tick-stock-panel、locally-uncensored 强调本地优先、零运维、隐私保护，反映对云端依赖和 API key 安全的担忧。
4. **上下文工程与 Token 优化**：headroom 聚焦 LLM 上下文压缩，说明 Agent 工作流中的 token 成本与上下文窗口管理成为工程重点。
5. **AI Agent 审计与治理技术兴起**：iFixAi 的爆发表明，Agent 的可审计性、幻觉检测、提示注入防护、合规映射正在成为独立技术赛道。

### 产品趋势

1. **“技能包”成为 AI 工作流交付单元**：day-trader-skill、ui-ux-pro-max-skill、logo-design-skill、agentic-awesome-skills 均以“skills”形态交付，交易、设计、提示工程等领域均在技能化。
2. **投研工作台产品化**：Vibe-Research、tick-stock-panel、daily_stock_analysis 将数据、回测、LLM 分析、看板整合为一体化工作台。
3. **AI Agent 治理产品化**：iFixAi、OpenBot、CyberStrikeAI 将 Agent 治理、审计、安全作为产品核心。

### 量化/交易策略趋势

1. **LLM 多智能体决策替代单一策略模型**：从单一信号模型转向多角色 Agent 协作决策。
2. **金融基础模型探索**：Kronos 代表金融时序基础模型方向，试图用预训练模型建模市场语言。
3. **回测与 LLM 结合**：多个项目将回测模块与 LLM 策略生成结合，形成“LLM 生成策略 + 回测验证”的闭环。
4. **A 股量化工作台兴起**：Vibe-Research、tick-stock-panel、daily_stock_analysis 均聚焦 A 股，反映中文市场量化工具需求。

### AI Agent 与自动化交易结合趋势

1. **从“AI 辅助分析”走向“AI 多智能体决策”**：交易 Agent 不再只是分析工具，而是具备角色分工、协作决策能力的系统。
2. **审计与治理成为交易 Agent 的必备组件**：iFixAi 的爆发表明，交易 Agent 的可审计性、合规性正在成为核心需求。
3. **技能化封装降低交易 Agent 开发门槛**：day-trader-skill 将交易工作流封装为技能，使非专业开发者也能快速搭建交易 Agent 原型。

### 值得后续做原型验证的方向

1. **交易 Agent 审计中间层**：在交易 Agent 的决策流水线中插入审计节点，检测幻觉、提示注入、异常信号。
2. **本地优先投研工作台**：基于 DuckDB + Polars + FastAPI + React 构建轻量级投研 MVP。
3. **多智能体交易决策沙箱**：参考 TradingAgents/ai-hedge-fund，构建角色化多智能体交易研究沙箱，严格隔离实盘。
4. **金融数据 MCP 网关**：参考 OpenBB/Vibe-Research，构建统一金融数据 MCP 网关，供多个 Agent 复用。
5. **技能化交易工作流**：将行情扫描、新闻分析、信号生成、复盘封装为可复用技能包。

## 5. 今日灵感清单

1. **MVP：交易 Agent 审计中间层**。参考 iFixAi，构建一个轻量级审计服务，对交易 Agent 的每一条决策输出做幻觉检测、提示注入扫描、风险关键词检查，输出审计报告。可先做 CLI 原型。
2. **MVP：本地优先投研工作台**。参考 tick-stock-panel 与 Vibe-Research，用 DuckDB + Polars + FastAPI + React 搭建一个本地投研 MVP，接入 1-2 个公开数据源，支持自选股、回测、LLM 复盘。
3. **调研：MCP 在金融数据接入中的标准化程度**。对比 OpenBB、Vibe-Research、Vibe-Trading 的 MCP 实现，总结金融数据 MCP 网关的最佳实践。
4. **调研：多智能体交易框架的角色分工设计**。对比 TradingAgents、ai-hedge-fund、Vibe-Trading 的 Agent 角色定义与消息传递机制，提炼可复用的角色模板。
5. **Codex/Agent 自动复现 demo：Claude Skills 交易工作流**。参考 day-trader-skill，让 Codex 自动生成一个“行情扫描 + 新闻分析 + 信号生成”的技能包骨架，验证技能化交易工作流的可行性。
6. **Codex/Agent 自动复现 demo：Agent 审计流水线**。参考 iFixAi，让 Codex 自动生成一个基于 LLM 的幻觉检测与提示注入扫描脚本，集成到现有 Agent 工作流中。
7. **加入 watchlist：TradingAgents、iFixAi、Vibe-Research、tick-stock-panel、Kronos**。这些项目在架构、数据工程、审计治理方面有持续跟踪价值。
8. **原型验证：金融时序基础模型微调**。参考 Kronos，调研金融时序基础模型的微调成本与效果，评估是否值得在内部数据上做小规模验证。
9. **原型验证：本地多智能体投研团队**。参考 Orkas，构建一个本地优先的投研 Agent 团队，Commander 拆解投研任务，专家 Agent 执行数据获取、分析、报告生成。
10. **调研：AI Agent 合规映射**。参考 iFixAi 的 EU AI Act、ISO 42001、NIST AI RMF 映射，调研交易 Agent 的合规要求与审计要点。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多智能体金融交易框架，7d +5326 星，架构参考价值高，需持续观察其演进与风险控制设计 |
| ifixai-ai/iFixAi | AI Agent 审计与治理赛道爆发项目，24h +763 星，合规映射与审计流水线值得跟踪 |
| simonlin1212/Vibe-Research | 多市场投研工作台，168 数据端点，数据工程与 Agent 集成结合紧密 |
| shy3130/tick-stock-panel | A 股自托管量化工作台，DuckDB + Polars 现代数据栈，轻量级量化 MVP 参考 |
| shiyu-coder/Kronos | 金融时序基础模型方向，虽近期维护活跃度存疑，但研究方向值得跟踪 |
| virattt/ai-hedge-fund | AI 多智能体对冲基金参考项目，角色分工设计清晰，适合教学与研究 |
| HKUDS/Vibe-Trading | HKUDS 出品，MCP + 多智能体 + 回测结合，产品形态值得观察 |
| Orkas-AI/Orkas | 本地优先多智能体桌面编排，24h +1126 星，企业级 Agent 编排参考 |
| openbq-org/OpenBB | 开放金融数据平台，面向 AI Agent 的数据接口设计值得跟踪 |
| Jakeschincariol/day-trader-skill | 技能化交易工作流代表，虽营销色彩明显，但技能包形态值得观察 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-10-28.json）和 `baseline_7d`（2026-10-22.json），1 日与 7 日涨星数据完整，未缺失基线。
- **30 日基线**：所有项目的 `star_delta_30d` 均为 null，说明本次数据未提供 30 日涨星基线，无法分析中期趋势。
- **采集失败**：未发现明显采集失败迹象，但 `awesome-mac` 的 `star_delta_7d` 为 null，可能存在 7 日基线缺失或计算异常。
- **样本偏差**：候选列表存在明显的**关键词误匹配噪声**。大量通用 awesome 列表（awesome-selfhosted、public-apis、awesome-python、build-your-own-x、awesome-go、awesome-cpp 等）因描述或 README 中偶然出现“trading bot”“quant”“order book”等词被召回，并非真正的金融/量化/交易项目。这导致 Top 45 中真正相关的交易/量化/AI Agent 项目占比偏低，分析结论需结合人工筛选。
- **分类偏差**：`category_guess` 字段存在过度分类现象，例如 FractalWorkspace 被标记为 quant_research，但实际是联邦学习项目；colibri 被标记为 quant_research，但实际是 MoE 推理引擎。分类结果不可直接采信。
- **风险标记偏差**：部分项目因 README 中出现“trading bot”等词被标记为 trading_bot 风险，但实际并非交易系统（如 awesome-selfhosted、build-your-own-x），风险等级需人工复核。
