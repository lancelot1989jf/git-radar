# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-05

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：iFixAi 以 7 日 +5690 星爆发，聚焦 AI Agent 独立审计、幻觉检测、prompt injection 检测，直接回应 AI Agent 经济中“Agent 是否在做该做的事”这一核心问题。
  2. **LLM 多智能体金融交易框架**：TradingAgents 7 日 +2447 星，Kronos 7 日 +2887 星，Vibe-Trading 7 日 +567 星，显示“LLM 多 Agent 交易/金融基础模型”仍是量化研究热点。
  3. **Claude/Codex 交易技能包**：day-trader-skill 7 日 +2304 星、trader-skill 7 日 +468 星，说明“把交易流程封装成 AI 技能”正在快速产品化。

- **是否出现新趋势**：出现。AI Agent 的**审计、对齐、治理**开始与金融交易场景交汇；同时“AI 技能包”作为交易工作流的最小交付单元快速升温。

- **是否出现值得复刻/参考的工程架构**：是。iFixAi 的 Agent 审计流水线、TradingAgents 的多角色 LLM 决策架构、Kronos 的金融基础模型、tick-stock-panel 的 DuckDB + Polars + FastAPI 本地量化工作台，都值得拆解。

- **是否有明显骗局、过度营销或高风险项目**：本次候选列表大量混入 awesome-list、UI 设计、通用 Agent 框架等**非交易项目**，属于关键词误匹配，不是骗局，但会稀释信号。真正需要警惕的是 day-trader-skill、trader-skill 这类“Claude 交易技能包”，其描述带有明显营销语气，且涉及日内交易决策，存在策略过拟合与误导风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 496501 | +313 | +3159 | Python | API 资源列表 | 免费 API 合集 | 数据源发现 | 中 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 145852 | +489 | +3202 | Python | AI 技能/UI | AI 驱动的 UI/UX 设计技能 | Agent 前端生成 | 低 |
| 3 | JustVugg/colibri | 48234 | +364 | +3217 | C | 推理引擎 | MoE 模型分层推理引擎 | 本地推理架构 | 低 |
| 4 | ifixai-ai/iFixAi | 43703 | +116 | +5690 | Python | AI 审计/风控 | AI Agent 独立审计 | Agent 治理/风控 | 低 |
| 5 | TauricResearch/TradingAgents | 120875 | +180 | +2447 | Python | 多 Agent 交易 | LLM 多智能体金融交易框架 | 交易 Agent 架构 | 低 |
| 6 | codecrafters-io/build-your-own-x | 560225 | +311 | +2819 | Markdown | 教程列表 | 从零构建技术项目教程 | 工程学习 | 中 |
| 7 | awesome-selfhosted/awesome-selfhosted | 334216 | +371 | +2321 | 无 | 自托管列表 | 自托管服务列表 | 基础设施选型 | 中 |
| 8 | shiyu-coder/Kronos | 46974 | +104 | +2887 | Python | 金融基础模型 | 金融市场语言基础模型 | 金融 LLM | 低 |
| 9 | Jakeschincariol/day-trader-skill | 5627 | +262 | +2304 | Python | 交易技能包 | 11 个 Claude 日内交易技能 | 交易工作流封装 | 低 |
| 10 | Orkas-AI/Orkas | 9047 | +22 | +4626 | JavaScript | 本地 Agent 团队 | 本地优先桌面 AI 团队 | Agent 编排 | 低 |
| 11 | CopilotKit/OpenBot | 10287 | +96 | +1980 | TypeScript | Agent 治理 | 开源 AI 协作者，自带浏览器/文件/工具 | Agent 沙箱 | 中 |
| 12 | vinta/awesome-python | 332833 | +234 | +1584 | Python | Python 资源列表 | Python 工具精选 | 工具选型 | 低 |
| 13 | awesome-dsh-plugin/awesome-dsh-plugin | 22974 | +523 | +1436 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | Agent 插件生态 | 低 |
| 14 | ripienaar/free-for-dev | 142014 | +102 | +1309 | HTML | 免费资源列表 | SaaS/PaaS/IaaS 免费层 | 成本优化 | 低 |
| 15 | nexu-io/open-design | 106184 | +184 | +1261 | TypeScript | AI 设计工作台 | 协作式 AI 设计 Agent 工作区 | 产品原型 | 低 |
| 16 | VoltAgent/awesome-design-md | 125827 | +155 | +1272 | 无 | 设计系统列表 | DESIGN.md 设计系统分析 | Agent UI 一致性 | 中 |
| 17 | avelino/awesome-go | 192310 | +166 | +1226 | Go | Go 资源列表 | Go 框架/库精选 | 交易基础设施选型 | 中 |
| 18 | ruvnet/ruflo | 81015 | +102 | +831 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | Agent 编排 | 低 |
| 19 | Fractal-Compute-Orchestrations/FractalWorkspace | 9249 | -9 | +1455 | Python | 联邦学习 | 大规模联邦学习工作区 | 分布式训练 | 低 |
| 20 | shy3130/tick-stock-panel | 7171 | +101 | +700 | Python | A 股量化工作台 | 自托管 A 股策略+监控+回测 | 本地量化栈 | 低 |
| 21 | headroomlabs-ai/headroom | 78963 | +79 | +673 | Python | Token 压缩 | LLM 输出/日志压缩 | 上下文工程 | 低 |
| 22 | kaankiziltug/logo-design-skill | 6082 | +56 | +779 | HTML | AI 技能 | Logo 设计技能 | Agent 技能封装 | 低 |
| 23 | HKUDS/Vibe-Trading | 37745 | +71 | +567 | Python | AI 交易 | 个人交易 Agent | 交易 Agent 产品化 | 低 |
| 24 | aardappel/goose | 3101 | +86 | +567 | C++ | 编程语言 | Goose 编程语言 | 系统语言 | 低 |
| 25 | jaywcjlove/awesome-mac | 117832 | +61 | +472 | Swift | macOS 软件列表 | macOS 软件精选 | 工具选型 | 低 |
| 26 | hesreallyhim/awesome-claude-code | 57354 | +71 | +463 | Python | Claude Code 资源 | Claude Code 资源精选 | Agent 工具链 | 低 |
| 27 | sickn33/agentic-awesome-skills | 49233 | +63 | +462 | Python | AI 技能库 | 2926+ 可复用 Agent 技能 | Agent 技能复用 | 低 |
| 28 | PurpleDoubleD/locally-uncensored | 3446 | +119 | +409 | TypeScript | 本地 AI 工作室 | 本地 AI 聊天/图像/视频/编码 | 本地 AI 栈 | 低 |
| 29 | Jakeschincariol/trader-skill | 1391 | +88 | +468 | Python | 交易技能包 | 11 个 Claude 投资技能 | 投资工作流封装 | 低 |
| 30 | punkpeye/awesome-remote-mcp-servers | 2678 | +59 | +446 | 无 | MCP 列表 | 远程 MCP 服务器合集 | MCP 生态 | 中 |
| 31 | ZhuLinsen/daily_stock_analysis | 67628 | +48 | +352 | Python | 股票分析 | LLM 多市场股票分析系统 | 数据工程/推送 | 低 |
| 32 | MakazhanAlpamys/Soup | 10221 | +48 | +416 | Python | LLM 微调 | 单 YAML 微调 LLM | 本地微调 | 低 |
| 33 | jesdga95/basalt | 670 | +78 | +352 | C++ | 本地推理 | Qwen3.8-Flash-Next 本地推理 | 低延迟推理 | 低 |
| 34 | Developer-Y/cs-video-courses | 84602 | +41 | +328 | 无 | 课程列表 | CS 视频课程列表 | 学习资源 | 中 |
| 35 | punkpeye/awesome-mcp-servers | 97353 | +35 | +298 | 无 | MCP 列表 | MCP 服务器合集 | MCP 生态 | 低 |
| 36 | nidhinjs/prompt-master | 15575 | +53 | +312 | 无 | Prompt 技能 | 精准 Prompt 生成技能 | Prompt 工程 | 低 |
| 37 | garrytan/gbrain | 31562 | +27 | +219 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | Agent 架构 | 低 |
| 38 | openbq-org/OpenBB | 75125 | +21 | +237 | Python | 开放数据平台 | 分析师/量化/AI Agent 数据平台 | 金融数据层 | 中 |
| 39 | code-yeongyu/oh-my-openagent | 70738 | +16 | +248 | TypeScript | Agent 编排 | 图工程 Agent 编排 | Agent 编排 | 低 |
| 40 | fffaraz/awesome-cpp | 74265 | +23 | +165 | 无 | C++ 资源列表 | C++ 框架/库精选 | 低延迟系统选型 | 低 |
| 41 | virattt/ai-hedge-fund | 64512 | +13 | +154 | Python | AI 对冲基金 | AI 对冲基金团队 | 多 Agent 投研 | 低 |
| 42 | rust-unofficial/awesome-rust | 60350 | +13 | +151 | Rust | Rust 资源列表 | Rust 代码/资源精选 | 低延迟系统选型 | 中 |
| 43 | awesomedata/awesome-public-datasets | 79958 | +7 | +111 | 无 | 数据集列表 | 高质量开放数据集 | 数据源发现 | 中 |
| 44 | josephmisiti/awesome-machine-learning | 74765 | +11 | +74 | Python | ML 资源列表 | ML 框架/库精选 | ML 选型 | 低 |
| 45 | vuejs/awesome-vue | 73482 | -6 | -15 | 无 | Vue 资源列表 | Vue 生态精选 | 前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，可在 120 秒内给出结论。覆盖幻觉检测、prompt injection、AI 对齐、EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等治理框架。
- **为什么值得关注**：7 日 +5690 星，是本期涨星最猛的项目之一。AI Agent 经济越扩张，审计与治理需求越刚性，尤其当 Agent 开始接触交易、资金、合规场景时。
- **技术栈/架构亮点**：Python + CLI，topic 覆盖 agent-evaluation、ai-governance、llm-security、risk-assessment。可视为“Agent 风控层”的参考实现。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。可将其审计思路抽象为交易 Agent 的**前置合规检查、行为监控、事后审计**三层风控组件。
- **可能风险**：项目较新，审计标准与覆盖范围需自行验证；不能替代真实金融合规审查。

### 3.2 TauricResearch/TradingAgents
- **解决什么问题**：用多智能体 LLM 框架模拟金融交易决策，将分析师、研究员、交易员、风控等角色拆分为多个 Agent 协作。
- **为什么值得关注**：7 日 +2447 星，总星 12 万+，是“LLM 多 Agent 交易”方向最具代表性的开源项目之一。
- **技术栈/架构亮点**：Python + Apache-2.0，topic 为 agent、finance、llm、multiagent、trading。核心价值在于**角色化决策流水线**，而非单一模型预测。
- **是否适合借鉴**：适合。可借鉴其多角色辩论/协作机制，用于企业级投研 Agent、策略评审 Agent、风控 Agent 的架构设计。
- **可能风险**：标记为 likely_research_tool，回测结果可能过拟合；LLM 决策存在幻觉与不可复现性；不应直接用于实盘。

### 3.3 shiyu-coder/Kronos
- **解决什么问题**：构建“金融市场语言”基础模型，尝试用 foundation model 方式统一处理金融时序、文本、交易信号。
- **为什么值得关注**：7 日 +2887 星，总星 4.7 万。金融基础模型是量化研究的前沿方向。
- **技术栈/架构亮点**：Python + MIT，topic 为空，信息有限。从描述看是模型层创新，而非交易执行框架。
- **是否适合借鉴**：适合作为研究方向跟踪。可关注其数据表示、预训练任务、下游回测接口设计。
- **可能风险**：信息不足，无法判断模型真实能力；金融基础模型容易陷入“看起来通用、实盘不可用”的陷阱。

### 3.4 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析、复盘，可接入第三方数据源。
- **为什么值得关注**：7 日 +700 星，总星 7171，是本期少见的**真正面向 A 股本地量化工作台**的项目。
- **技术栈/架构亮点**：Python + MIT，topic 包含 duckdb、polars、fastapi、react、llm、backtesting、screener。DuckDB + Polars 的组合适合本地大规模行情数据处理，FastAPI + React 提供轻量交互层。
- **是否适合借鉴**：非常适合。可作为“本地优先、数据工程扎实、LLM 辅助”的量化工作台 MVP 参考。
- **可能风险**：A 股数据源合规性、策略过拟合、个人开源项目维护持续性。

### 3.5 Jakeschincariol/day-trader-skill
- **解决什么问题**：11 个 Claude 技能，用于日内交易：扫描数千张图表、跟踪突发新闻、计时进出场、回放每次结果。
- **为什么值得关注**：7 日 +2304 星，总星仅 5627，属于“小项目大爆发”。代表“交易流程技能化”的产品趋势。
- **技术栈/架构亮点**：Python + MIT，topic 为 backtesting、claude、claude-skills、day-trading、stock-market。核心是把交易决策拆成可复用的 Claude 技能。
- **是否适合借鉴**：可借鉴其“技能包”产品形态，但**不建议直接用于实盘交易**。
- **可能风险**：日内交易本身高风险；描述带有营销语气；技能逻辑不透明；回测可能幸存者偏差；用户可能误以为“技能=收益”。

### 3.6 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多 Agent 做算法交易与回测。
- **为什么值得关注**：HKUDS 出品，7 日 +567 星，总星 3.7 万。学术背景 + 交易 Agent 产品化。
- **技术栈/架构亮点**：Python + MIT，topic 包含 ai-agent、algorithmic-trading、backtesting、llm、mcp、multi-agent、quantitative-finance。MCP 的引入值得关注，可能用于连接数据源与交易接口。
- **是否适合借鉴**：适合。可研究其 MCP 在交易 Agent 中的边界设计，以及多 Agent 如何分工。
- **可能风险**：标记为 likely_research_tool；MCP 连接真实交易接口时存在安全风险；不应输入真实 API key。

### 3.7 virattt/ai-hedge-fund
- **解决什么问题**：模拟“AI 对冲基金团队”，用多个 Agent 扮演不同投研角色。
- **为什么值得关注**：总星 6.4 万，是 AI 多 Agent 投研的经典项目，虽然本期涨星放缓，但架构仍有参考价值。
- **技术栈/架构亮点**：Python + MIT，topic 为空。核心是角色化 Agent 团队 + 回测。
- **是否适合借鉴**：适合作为多 Agent 投研工作流的入门参考。
- **可能风险**：研究工具属性强，回测结果不代表实盘；Agent 决策可复现性差。

### 3.8 openbq-org/OpenBB
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、期权、加密、固定收益、宏观等数据。
- **为什么值得关注**：总星 7.5 万，是金融数据层的重要开源基础设施。
- **技术栈/架构亮点**：Python，topic 包含 ai、crypto、derivatives、equity、fixed-income、options、quantitative-finance。可作为 AI Agent 的金融数据接入层。
- **是否适合借鉴**：适合。可将其作为交易 Agent 的标准化数据层，避免每个 Agent 各自对接数据源。
- **可能风险**：数据源质量与延迟需自行验证；加密相关数据存在合规风险。

### 3.9 CopilotKit/OpenBot
- **解决什么问题**：开源 AI 协作者，每个 Agent 拥有自己的浏览器、文件与工具，动作执行前先决策、执行后记录，支持 AG-UI Agent。
- **为什么值得关注**：7 日 +1980 星，总星 1 万+。其“动作前决策 + 动作后审计”的设计对交易 Agent 安全执行有直接启发。
- **技术栈/架构亮点**：TypeScript + MIT，topic 包含 ag-ui、agent-governance、browser-automation、mcp、generative-ui。
- **是否适合借鉴**：适合。可借鉴其**执行前审批、执行后留痕**的治理机制，用于交易 Agent 的订单审批与审计。
- **可能风险**：浏览器自动化与交易场景结合时，需防止误操作与越权。

### 3.10 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 接收前压缩工具输出、日志、文件、RAG 块，编码 Agent 可减少 20% token，JSON 可减少 60-95% token。
- **为什么值得关注**：总星 7.9 万，7 日 +673。对高频调用 LLM 的交易 Agent，token 成本与上下文窗口是真实瓶颈。
- **技术栈/架构亮点**：Python + Apache-2.0，提供 library、proxy、MCP server 三种形态，topic 包含 context-engineering、token-optimization、rag。
- **是否适合借鉴**：适合。可将其作为交易 Agent 的上下文压缩中间层，降低长行情序列、日志、新闻流的 token 消耗。
- **可能风险**：压缩可能丢失关键信号，需在交易场景中验证信息保真度。

## 4. 趋势归纳

- **技术趋势**：
  - **Agent 治理与审计**从通用 AI 向金融交易渗透，iFixAi、OpenBot 都强调“执行前决策、执行后审计”。
  - **本地优先**成为量化工作台与 Agent 框架的共同选择：tick-stock-panel、Orkas、locally-uncensored、colibri 均强调本地运行。
  - **上下文工程**成为 Agent 成本控制的关键：headroom 的 token 压缩、prompt-master 的精准 prompt。
  - **MCP 生态**持续扩张，awesome-mcp-servers、awesome-remote-mcp-servers、awesome-dsh-plugin 均反映工具接入标准化趋势。

- **产品趋势**：
  - **交易技能包**快速产品化：day-trader-skill、trader-skill 把交易流程封装为 Claude 技能。
  - **AI 设计/UI 技能**与金融产品原型结合：ui-ux-pro-max-skill、open-design、awesome-design-md 可用于快速生成交易看板与风控界面。
  - **多 Agent 交易框架**从研究走向产品化：TradingAgents、Vibe-Trading、ai-hedge-fund 都在探索角色化 Agent 团队。

- **量化/交易策略趋势**：
  - LLM 多 Agent 决策仍是主流叙事，但**实盘价值未被证明**。
  - 金融基础模型（Kronos）尝试统一金融语言，但距离可交易信号仍有距离。
  - A 股本地量化工作台（tick-stock-panel）显示**本地数据工程 + LLM 辅助**的务实路线。

- **AI Agent 与自动化交易结合趋势**：
  - 从“单 Agent 预测”走向“多 Agent 角色协作 + 审计 + 治理”。
  - MCP 成为连接数据源、工具与交易接口的标准协议。
  - 执行安全与审计日志成为交易 Agent 的必备组件。

- **值得后续做原型验证的方向**：
  - 交易 Agent 的**执行前审批 + 执行后审计**沙箱。
  - 基于 DuckDB + Polars 的本地行情回测工作台。
  - 金融数据 MCP server 标准化。
  - LLM 交易决策的**可复现性与幻觉检测**。

## 5. 今日灵感清单

1. **MVP：交易 Agent 审计沙箱**。参考 iFixAi + OpenBot，做一个最小可用的“交易 Agent 执行前审批、执行后留痕”沙箱，不接真实交易所，只用模拟盘验证。
2. **MVP：本地 A 股量化工作台**。参考 tick-stock-panel，用 DuckDB + Polars + FastAPI 搭建本地行情存储、回测、监控一体工作台，LLM 只做辅助分析。
3. **调研：MCP 在金融数据接入中的标准化**。对比 awesome-mcp-servers、awesome-remote-mcp-servers 中金融相关 MCP server 的接口设计，提炼统一数据 schema。
4. **调研：LLM 交易决策的可复现性**。对 TradingAgents、Vibe-Trading、ai-hedge-fund 的决策流程做可复现性测试，记录同一输入下输出方差。
5. **Demo：上下文压缩中间层**。参考 headroom，为交易 Agent 的行情序列、新闻流、日志做 token 压缩，验证信息保真度与成本节省。
6. **Demo：交易技能包产品化**。参考 day-trader-skill 的形态，但把“技能”限定为**研究辅助**而非下单，例如财报摘要、新闻情绪、图表扫描。
7. **原型：多 Agent 投研辩论**。参考 TradingAgents，做一个“分析师 vs 风控”的辩论式投研 Agent，输出结构化风险清单。
8. **Watchlist：Kronos**。跟踪金融基础模型的预训练任务与下游回测接口，评估是否值得复现小规模版本。
9. **Watchlist：OpenBB**。评估其作为交易 Agent 标准化数据层的可行性，尤其是期权、固定收益、加密数据覆盖。
10. **原型：Agent 执行审计日志**。参考 OpenBot 的“动作前决策、动作后记录”，为自研 Agent 增加不可篡改的决策日志，便于事后复盘与合规。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | Agent 审计与治理是交易 Agent 的刚性需求，7 日爆发式增长，值得跟踪其审计标准与工具链演进。 |
| TauricResearch/TradingAgents | LLM 多 Agent 交易框架的代表项目，适合持续观察其架构迭代与实盘化尝试。 |
| shiyu-coder/Kronos | 金融基础模型前沿方向，适合跟踪其数据表示与下游任务设计。 |
| shy3130/tick-stock-panel | 本地 A 股量化工作台，DuckDB + Polars + FastAPI 栈务实，适合作为本地量化 MVP 参考。 |
| CopilotKit/OpenBot | Agent 执行治理机制清晰，对交易 Agent 的审批与审计有直接借鉴价值。 |
| headroomlabs-ai/headroom | 上下文压缩对高频 LLM 调用场景有实际成本价值，适合跟踪其压缩算法演进。 |
| openbq-org/OpenBB | 金融数据层标准化的重要候选，适合评估作为 Agent 数据接入层。 |
| HKUDS/Vibe-Trading | 学术背景 + MCP + 多 Agent 交易，适合观察 MCP 在交易场景的边界设计。 |
| virattt/ai-hedge-fund | 经典 AI 多 Agent 投研项目，适合作为入门参考与对比基准。 |
| Jakeschincariol/day-trader-skill | 交易技能包产品形态值得观察，但需警惕其营销语气与实盘误导风险。 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

- **GitHub star 不是投资建议**：star 增长只反映关注度，不反映策略收益或项目质量。
- **不运行未知 trading bot**：day-trader-skill、trader-skill、Vibe-Trading 等项目均不应直接用于实盘。
- **不泄露交易所 API key**：任何涉及 MCP、交易接口的项目，都应使用模拟盘与只读权限。
- **注意马丁、网格、套利、杠杆类项目的爆仓风险**：本次候选未直接出现此类项目，但相关关键词匹配显示生态中存在此类风险。
- **注意回测幸存者偏差和过拟合**：TradingAgents、Kronos、ai-hedge-fund、day-trader-skill 等项目的回测结果可能不可复现，不应作为实盘依据。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-11-04）与 `baseline_7d`（2026-10-29），1 日与 7 日涨星数据可用。
- **30 日基线缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法判断 30 日趋势。
- **采集失败**：未发现明确采集失败标记，但部分项目 `language` 为 `null`，部分项目 `topics` 为空，信息不完整。
- **样本偏差**：候选列表大量混入 awesome-list、UI 设计、通用 Agent 框架等**非金融/交易项目**，属于关键词误匹配，会稀释真实交易信号。真正与金融/量化/交易直接相关的项目约占三分之一。
- **风险标记偏差**：部分项目因关键词误匹配被标记为 `trading_bot` 或 `crypto_related`，实际并非交易机器人或加密项目，需人工甄别。
