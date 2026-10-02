# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-01

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：iFixAi 以 24h +951 星、7d +2969 星位居第二，反映市场对 AI Agent 可审计性、合规性、安全性的强烈需求，尤其与 EU AI Act、ISO 42001、NIST AI RMF 等监管框架直接挂钩。
  2. **AI 交易框架与多智能体金融决策**：TradingAgents、Vibe-Trading、QuantDinger、ai-hedge-fund 等项目持续活跃，LLM 多智能体交易决策、回测、模拟盘/实盘一体化成为明确趋势。
  3. **AI 编码/设计 Agent 基础设施**：ui-ux-pro-max-skill、open-design、awesome-design-md 等设计智能项目涨星显著，显示 coding agent 正在从“写代码”扩展到“生成可交付 UI/UX 资产”，对金融终端、交易看板、风控仪表盘的产品化有直接借鉴价值。

- **是否出现新趋势**：出现。AI Agent 的“审计/对齐/合规”从概念走向可执行工具（iFixAi），且与金融风控场景天然契合；同时“vibe trading”类项目（Vibe-Trading、QuantDinger）将 LLM 决策与交易执行、SaaS 多租户能力结合，值得警惕其工程成熟度与真实风险。

- **是否出现值得复刻/参考的工程架构**：是。iFixAi 的 Agent 审计流水线、TradingAgents 的多智能体辩论式决策、hyperswitch 的 Rust 支付编排、tick-stock-panel 的 DuckDB+Polars+FastAPI 本地量化工作台，均具备可复刻的架构价值。

- **是否有明显骗局、过度营销或高风险项目**：`codeman008/Financial_freedom` 描述为“最全赚钱投资指南”，7 日涨星 +1570 但内容与量化/交易工程关联弱，存在内容营销与误导风险。`QuantDinger`、`Vibe-Trading`、`jev-trader` 等涉及 crypto/实盘交易的项目需高度警惕 API key 安全、策略过拟合与资金风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 485332 | +446 | +2365 | Python | API 资源 | 免费 API 集合 | 数据源发现 | 中 |
| 2 | ifixai-ai/iFixAi | 18688 | +951 | +2969 | Python | AI 治理/风控 | AI Agent 独立审计 | Agent 合规审计 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 132398 | +302 | +1937 | Python | AI 设计 | 多平台 UI/UX 设计智能 | 金融终端 UI | 低 |
| 4 | vinta/awesome-python | 324577 | +172 | +1748 | Python | 资源列表 | Python 工具精选 | 技术选型 | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 323275 | +243 | +1692 | 无 | 自托管 | 自托管服务列表 | 交易系统部署 | 中 |
| 6 | codecrafters-io/build-your-own-x | 551112 | +176 | +1728 | Markdown | 教程 | 从零复刻技术 | 交易系统复刻 | 中 |
| 7 | VoltAgent/awesome-design-md | 119198 | +187 | +1414 | 无 | 设计系统 | DESIGN.md 设计系统 | Agent 生成 UI | 中 |
| 8 | JustVugg/colibri | 38905 | +196 | +1336 | C | 模型推理 | 本地 MoE 推理引擎 | 低资源推理 | 低 |
| 9 | codeman008/Financial_freedom | 5553 | +143 | +1570 | 无 | 投资指南 | 赚钱投资指南 | 低 | 中 |
| 10 | nexu-io/open-design | 99108 | +138 | +1106 | TypeScript | AI 设计 | 开源设计引擎 | 交易看板生成 | 低 |
| 11 | avelino/awesome-go | 186495 | +151 | +1028 | Go | 资源列表 | Go 框架精选 | 交易基础设施 | 中 |
| 12 | TauricResearch/TradingAgents | 109490 | +86 | +980 | Python | AI 交易 | 多智能体交易框架 | 多 Agent 决策 | 低 |
| 13 | juspay/hyperswitch | 45274 | +3 | +1338 | Rust | 支付 | 开源支付编排 | 支付/结算架构 | 低 |
| 14 | MakazhanAlpamys/Soup | 7976 | +103 | +827 | Python | LLM 微调 | 低显存微调 | 本地模型训练 | 低 |
| 15 | awesome-dsh-plugin/awesome-dsh-plugin | 17574 | +92 | +729 | JavaScript | 插件列表 | DeepSeek Harness 插件 | Agent 插件生态 | 低 |
| 16 | career-ops-hq/career-ops | 73264 | +92 | +625 | JavaScript | AI Agent | AI 求职 Agent | Agent 工作流 | 低 |
| 17 | ripienaar/free-for-dev | 139048 | +48 | +713 | HTML | 资源列表 | 免费开发者资源 | 基础设施选型 | 低 |
| 18 | ruvnet/ruflo | 73679 | +85 | +451 | TypeScript | Agent 框架 | 多智能体 swarm | Agent 编排 | 低 |
| 19 | headroomlabs-ai/headroom | 74260 | +57 | +518 | Python | 上下文压缩 | LLM token 压缩 | 降本增效 | 低 |
| 20 | HKUDS/Vibe-Trading | 34439 | +41 | +443 | Python | AI 交易 | 个人交易 Agent | 交易 Agent 原型 | 中 |
| 21 | code-yeongyu/oh-my-openagent | 69749 | +47 | +360 | TypeScript | Agent 编排 | 图工程 Agent | Agent 编排 | 低 |
| 22 | Open-Dev-Society/OpenStock | 19578 | +56 | +397 | TypeScript | 股票平台 | 开源行情平台 | 行情产品 | 低 |
| 23 | heyreallyhim/awesome-claude-code | 54920 | +50 | +340 | Python | 资源列表 | Claude Code 资源 | Agent 工具链 | 低 |
| 24 | shiyu-coder/Kronos | 39798 | +84 | +375 | Python | 金融模型 | 金融市场基础模型 | 金融 LLM | 低 |
| 25 | CopilotKit/OpenBot | 5835 | +61 | +306 | TypeScript | AI Agent | 开源 AI 同事 | 浏览器自动化 | 中 |
| 26 | unslothai/unsloth | 77124 | +21 | +396 | Python | LLM 微调 | 本地训练/推理 | 模型微调 | 低 |
| 27 | yibie/awesome-jev | 2070 | +33 | +436 | Python | 资源列表 | Jev 类型决策生态 | 类型安全决策 | 中 |
| 28 | cactus-compute/needle | 12932 | +29 | +378 | Python | 边缘 AI | 微型设备自动化模型 | 边缘推理 | 中 |
| 29 | ZhuLinsen/daily_stock_analysis | 65842 | +26 | +226 | Python | 股票分析 | LLM 多市场股票分析 | 研究 Agent | 低 |
| 30 | punkpeye/awesome-mcp-servers | 95757 | +26 | +259 | 无 | MCP | MCP 服务器集合 | Agent 工具接入 | 低 |
| 31 | nidhinjs/prompt-master | 13948 | +37 | +311 | 无 | Prompt | 精准 Prompt 技能 | Prompt 工程 | 低 |
| 32 | anbeime/skill | 7474 | +32 | +289 | Python | Skills 商店 | AI Agent 技能库 | 技能复用 | 低 |
| 33 | jarrodwatts/jev-trader | 2734 | +20 | +359 | TypeScript | AI 交易 | Monad 区块 AI 交易 | 链上交易 Agent | 低 |
| 34 | shy3130/tick-stock-panel | 5359 | +10 | +345 | Python | 量化工作台 | A 股选股/监控/回测 | 本地量化栈 | 低 |
| 35 | antirez/ds4 | 22851 | +34 | +162 | C | 模型推理 | DeepSeek 本地推理 | 本地推理 | 低 |
| 36 | OthmanAdi/planning-with-files | 27253 | +37 | +145 | Shell | Agent 规划 | 文件持久化规划 | 长任务 Agent | 低 |
| 37 | garrytan/gbrain | 30488 | +22 | +177 | TypeScript | Agent 大脑 | 个人 Agent 大脑 | Agent 记忆 | 低 |
| 38 | samugit83/redamon | 2894 | +24 | +304 | Python | AI 渗透测试 | 自主渗透测试框架 | 安全审计 | 中 |
| 39 | HiThink-Tech/Financial-API | 3969 | +36 | +207 | TypeScript | 金融数据 | 同花顺 A 股数据服务 | 数据 API/MCP | 低 |
| 40 | OpenByteInc/QuantDinger | 12366 | +18 | +236 | Python | AI 交易 OS | 多租户交易 SaaS | 交易 SaaS 架构 | 中 |
| 41 | bbfamily/abu | 18818 | +76 | +123 | Python | 量化交易 | 阿布量化交易系统 | 策略框架 | 低 |
| 42 | awesomedata/awesome-public-datasets | 79275 | +15 | +126 | 无 | 数据集 | 公开数据集列表 | 数据源 | 中 |
| 43 | virattt/ai-hedge-fund | 63832 | +18 | +87 | Python | AI 交易 | AI 对冲基金团队 | 多 Agent 投研 | 低 |
| 44 | openbq-org/OpenBB | 73740 | +32 | 信息不足 | Python | 金融数据 | 开放数据平台 | 数据平台 | 中 |
| 45 | fffaraz/awesome-cpp | 73564 | +8 | +110 | 无 | 资源列表 | C++ 框架精选 | 低延迟系统 | 低 |
| 46 | Developer-Y/cs-video-courses | 83599 | +9 | +45 | 无 | 课程 | CS 视频课程 | 学习资源 | 中 |
| 47 | josephmisiti/awesome-machine-learning | 74504 | -3 | +61 | Python | 资源列表 | ML 框架精选 | ML 选型 | 低 |
| 48 | Superior-Trade/trading-terminal | 239 | +46 | +85 | TypeScript | AI 交易终端 | Hyperliquid 交易终端 | 交易终端 | 低 |
| 49 | vuejs/awesome-vue | 73537 | -2 | -7 | 无 | 资源列表 | Vue 资源 | 前端选型 | 低 |
| 50 | ByteByteGoHq/system-design-101 | 90162 | +19 | +246 | 无 | 系统设计 | 系统设计图解 | 架构学习 | 低 |

## 3. 重点项目深度分析

### 3.1 ifixai-ai/iFixAi

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，可在 120 秒内给出结论。面向 AI Agent 经济中的对齐、安全、合规问题。
- **为什么最近值得关注**：24h +951 星、7d +2969 星，是本期涨星最快的非资源类项目。随着 AI Agent 进入金融、交易、企业决策场景，Agent 行为审计成为刚需。
- **技术栈/架构亮点**：Python + Apache-2.0，CLI 形态，覆盖 hallucination detection、prompt injection、LLM security、EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等评估维度。支持人工或 Agent 自审计。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。可将类似审计层嵌入交易 Agent 的决策链路，作为 pre-trade 风控闸门，记录 Agent 决策依据、检测幻觉与 prompt 注入。
- **可能的风险**：项目较新，评估标准与金融场景的适配度需验证；审计本身可能被绕过；不能替代真实交易合规与人工审批。

### 3.2 TauricResearch/TradingAgents

- **解决什么问题**：多智能体 LLM 金融交易框架，模拟分析师、研究员、交易员等多角色协作完成交易决策。
- **为什么最近值得关注**：109k stars，7d +980，是 AI 交易方向最成熟的参考实现之一，持续有 push。
- **技术栈/架构亮点**：Python + Apache-2.0，多 Agent 架构，topic 覆盖 agent、finance、llm、multiagent、trading。强调研究、辩论、决策分离。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其多角色辩论式决策可迁移到投研、风控、组合管理场景，作为企业级 Agent 的参考架构。
- **可能的风险**：标记为 likely_research_tool，不应直接用于实盘；LLM 决策存在幻觉与过拟合风险；回测结果不代表未来收益。

### 3.3 HKUDS/Vibe-Trading

- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 与交易决策结合，覆盖 crypto、order book、portfolio optimization、risk model 等关键词。
- **为什么最近值得关注**：HKUDS 出品，34k stars，7d +443，是学术机构在 AI 交易方向的代表性项目。
- **技术栈/架构亮点**：Python + MIT，topic 包含 ai-agent、algorithmic-trading、backtesting、fintech、llm、mcp、multi-agent、quantitative-finance。MCP 集成值得关注。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：可借鉴其 MCP 工具接入与多 Agent 交易流程，但应作为研究原型而非生产系统。
- **可能的风险**：crypto_related，风险等级中；涉及真实交易接口时存在 API key 泄露与资金风险；策略可能过拟合。

### 3.4 OpenByteInc/QuantDinger

- **解决什么问题**：开源 AI Trading OS，支持 agent trading、vibe trading、Jev System One 集成，覆盖 crypto、股票、外汇的研究、策略编写、回测、模拟/实盘，并可启动多租户交易 SaaS。
- **为什么最近值得关注**：将“交易系统”与“SaaS 多租户、用户管理、计费、支付、结算”结合，是交易基础设施产品化的典型样本。
- **技术栈/架构亮点**：Python + Apache-2.0，集成 Alpaca、Binance、MCP server、Jev 类型安全决策。架构上从研究到实盘到 SaaS 全链路。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合借鉴其多租户交易 SaaS 架构与 MCP 工具层设计，但不宜直接复用其实盘交易逻辑。
- **可能的风险**：crypto_related，风险等级中；涉及交易所 API key；多租户交易 SaaS 存在合规、结算、资金安全等重大风险。

### 3.5 juspay/hyperswitch

- **解决什么问题**：开源可组合支付平台，支持 PCI 合规、SaaS 与自托管，连接多个支付、支付风控、vault、tokenization 提供商，提供智能路由、收入恢复、成本可观测性与对账。
- **为什么最近值得关注**：7d +1338 星，Rust 编写，是金融基础设施中少有的高增长工程型项目。
- **技术栈/架构亮点**：Rust + Apache-2.0，支付编排、智能路由、对账、成本观测。架构上强调高性能与可组合性。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合借鉴其支付编排、风控路由、对账与成本可观测性设计，尤其对交易 SaaS 的结算与资金链路有参考价值。
- **可能的风险**：支付合规复杂，自托管需自行承担 PCI 与资金安全责任；与交易系统集成需谨慎。

### 3.6 shy3130/tick-stock-panel

- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析与复盘，可接入第三方数据源。
- **为什么最近值得关注**：7d +345，技术栈现代，是本地量化工作台的良好参考。
- **技术栈/架构亮点**：Python + MIT，DuckDB + Polars + FastAPI + React，topic 包含 backtesting、screener、stock-analysis、tickflow。强调本地化与零运维。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。DuckDB+Polars 的本地数据栈、FastAPI 服务层、LLM 策略生成，可作为轻量级量化研究 MVP 的参考架构。
- **可能的风险**：标记为 likely_research_tool，回测结果需警惕过拟合；A 股数据源合规与稳定性需验证。

### 3.7 virattt/ai-hedge-fund

- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 扮演不同角色进行投资研究与决策。
- **为什么最近值得关注**：63k stars，是 AI 投研 Agent 的经典参考项目，持续有 push。
- **技术栈/架构亮点**：Python + MIT，多 Agent 投研流程，强调角色分工与决策链。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合借鉴其多 Agent 投研工作流，可作为企业级投研 Agent 的原型。
- **可能的风险**：likely_research_tool，不应直接用于实盘；LLM 输出不稳定；回测与实盘差距大。

### 3.8 HiThink-Tech/Financial-API

- **解决什么问题**：同花顺官方 A 股金融数据服务，提供实时行情、历史行情、财务报表、指数、板块、涨停等数据，支持 API、MCP、CLI、Python。
- **为什么最近值得关注**：官方背景 + MCP 支持，对 AI Agent 与量化研究的数据接入有直接价值。
- **技术栈/架构亮点**：TypeScript + MIT，DuckDB、MCP、REST API、npm package。数据服务与 Agent 工具化结合。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。可作为 A 股数据 MCP server 的参考实现，接入研究 Agent。
- **可能的风险**：数据合规与授权范围需确认；官方服务稳定性与限流需评估。

### 3.9 shiyu-coder/Kronos

- **解决什么问题**：定位为“金融市场语言的基础模型”，面向金融时序与文本的 foundation model。
- **为什么最近值得关注**：39k stars，7d +375，是金融 LLM 方向的代表性项目。
- **技术栈/架构亮点**：Python + MIT，topic 信息不足，但从描述看聚焦金融语言建模。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：可调研其模型能力与训练数据，作为金融领域 LLM 的候选底座。
- **可能的风险**：likely_research_tool；模型能力与真实交易决策之间存在鸿沟；需警惕金融文本模型的幻觉与偏差。

### 3.10 Open-Dev-Society/OpenStock

- **解决什么问题**：开源股票市场平台，提供实时价格、个性化提醒、公司洞察，定位为昂贵市场平台的免费替代。
- **为什么最近值得关注**：19k stars，7d +397，是行情终端产品化的轻量参考。
- **技术栈/架构亮点**：TypeScript + AGPL-3.0，Next.js + shadcn-ui + TailwindCSS + Inngest。前端与实时数据流架构清晰。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合借鉴其行情终端 UI 与实时提醒机制，可作为交易看板 MVP 参考。
- **可能的风险**：AGPL 协议对商业闭源集成有限制；数据源授权需确认。

## 4. 趋势归纳

- **技术趋势**：
  - AI Agent 治理、审计、对齐工具快速崛起（iFixAi、redamon、OpenBot 的 agent-governance）。
  - MCP 成为 Agent 工具接入的事实标准，金融数据服务开始原生提供 MCP（HiThink-Tech/Financial-API、QuantDinger、Vibe-Trading）。
  - 本地化、低资源推理与微调持续升温（colibri、Soup、unsloth、ds4、needle）。
  - 现代量化工作台采用 DuckDB + Polars + FastAPI 轻量栈（tick-stock-panel、Financial-API）。

- **产品趋势**：
  - 交易系统从单机脚本走向多租户 SaaS（QuantDinger）。
  - 行情终端与投研平台开源化、产品化（OpenStock、daily_stock_analysis）。
  - AI 设计技能与 coding agent 深度结合，加速金融终端 UI 生成（ui-ux-pro-max-skill、open-design、awesome-design-md）。

- **量化/交易策略趋势**：
  - LLM 多智能体辩论式决策成为主流范式（TradingAgents、ai-hedge-fund、Vibe-Trading）。
  - 类型安全决策模型（Jev）开始渗透交易系统（QuantDinger、jev-trader、awesome-jev）。
  - 回测、模拟盘、实盘一体化，但多数项目仍定位研究工具。

- **AI Agent 与自动化交易结合趋势**：
  - 从“LLM 生成策略”向“Agent 执行研究-决策-风控-执行全链路”演进。
  - Agent 审计与风控闸门开始被引入，但成熟度低。
  - 链上交易 Agent（jev-trader）与区块级决策出现，风险极高。

- **值得后续做原型验证的方向**：
  - 交易 Agent 的 pre-trade 审计与决策留痕系统。
  - 基于 MCP 的金融数据服务层。
  - DuckDB+Polars 本地量化研究 MVP。
  - 多 Agent 投研工作流的企业级封装。

## 5. 今日灵感清单

1. **MVP：交易 Agent 决策审计闸门**。参考 iFixAi，为现有 LLM 交易 Agent 增加 pre-trade 审计层，记录决策依据、检测幻觉与 prompt 注入，输出结构化审计报告。
2. **MVP：金融数据 MCP server**。参考 HiThink-Tech/Financial-API，封装一个支持 MCP 的行情/财务数据服务，供 Claude Code/Codex 等 Agent 调用。
3. **调研：DuckDB + Polars 量化工作台**。参考 tick-stock-panel，验证 DuckDB+Polars 在分钟级行情回测中的性能与开发效率。
4. **调研：多 Agent 投研辩论架构**。对比 TradingAgents、ai-hedge-fund、Vibe-Trading 的 Agent 角色设计与决策流程，提炼可复用的投研 Agent 模板。
5. **Demo：AI 生成交易看板 UI**。参考 ui-ux-pro-max-skill 与 open-design，让 Codex/Agent 自动生成一个带实时行情、风控指标的交易看板原型。
6. **调研：支付编排与交易 SaaS 结算**。参考 hyperswitch，研究智能路由、对账、成本可观测性在交易 SaaS 中的应用。
7. **Demo：本地金融 LLM 微调**。参考 Soup/unsloth，在消费级 GPU 上微调一个金融领域小模型，用于研报摘要或情绪分类。
8. **调研：Agent 长任务规划与上下文压缩**。参考 planning-with-files 与 headroom，验证长周期投研 Agent 的上下文管理与 token 成本优化。
9. **Watchlist：OpenStock、tick-stock-panel、QuantDinger、iFixAi、TradingAgents**，持续观察其架构演进与社区活跃度。
10. **原型：类型安全交易决策层**。调研 Jev 相关项目（awesome-jev、QuantDinger、jev-trader），验证类型化决策在交易系统中的可行性与收益。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计/合规工具，涨星极快，金融 Agent 风控刚需 |
| TauricResearch/TradingAgents | 多智能体交易框架标杆，架构可借鉴 |
| HKUDS/Vibe-Trading | 学术机构 AI 交易 Agent，MCP 集成值得跟踪 |
| OpenByteInc/QuantDinger | 交易 SaaS 全链路架构，产品化参考 |
| shy3130/tick-stock-panel | DuckDB+Polars 轻量量化工作台，技术栈现代 |
| HiThink-Tech/Financial-API | 官方 A 股数据 MCP 服务，数据接入参考 |
| juspay/hyperswitch | Rust 支付编排，交易结算基础设施参考 |
| Open-Dev-Society/OpenStock | 开源行情终端，产品化与 UI 参考 |
| shiyu-coder/Kronos | 金融基础模型，金融 LLM 底座候选 |
| virattt/ai-hedge-fund | 多 Agent 投研经典项目，持续活跃 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-09-30.json`，1 日涨星数据完整。
- **7 日基线**：已提供 `baseline_7d: 2026-09-24.json`，7 日涨星数据完整。
- **30 日基线**：未提供，所有 `star_delta_30d` 均为 null，30 日趋势无法评估。
- **采集失败**：`OpenBB` 的 `star_delta_7d` 为 null，7 日涨星缺失，可能因基线数据缺失或项目在基线快照中不存在。
- **样本偏差**：候选项目由关键词搜索与 topic 匹配生成，大量 awesome-list、资源列表类项目因关键词误匹配进入候选，真实金融/量化/交易项目占比被稀释。部分项目（如 ui-ux-pro-max-skill、career-ops、system-design-101）与金融/量化直接关联较弱，属于关键词误命中。报告中的分类与风险判断仅基于 JSON 提供的元数据，未对项目源码进行独立验证。
