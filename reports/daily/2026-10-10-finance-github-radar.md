# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-10

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：iFixAi 以 24h +481 星、7d +3558 星领跑，聚焦 AI Agent 行为审计、幻觉检测、提示注入检测，直接回应 AI Agent 经济中“Agent 是否在做它该做的事”这一核心问题。
  2. **AI 交易 Agent 与多智能体金融框架**：TradingAgents、Vibe-Trading、QuantDinger、ai-hedge-fund 等项目持续活跃，LLM 多智能体交易、回测、paper/live trading 一体化成为明显趋势。
  3. **本地化/边缘化 LLM 推理基础设施**：colibri、ds4、BitNet、needle、project-maya 等项目围绕“在自有硬件上运行前沿 MoE/量化模型”快速涨星，反映量化研究对低成本、本地化推理能力的需求。

- **是否出现新趋势**：出现。AI Agent 的“可审计性”和“治理”正在成为独立赛道，iFixAi 将 AI 审计产品化（120 秒内给出 Agent 行为结论），与金融交易场景中的风控、合规需求高度契合。同时，“vibe trading”概念从营销话语逐步沉淀为可运行的多智能体交易框架。

- **是否出现值得复刻/参考的工程架构**：是。iFixAi 的 Agent 审计流水线、Vibe-Trading 的 MCP + 多智能体交易架构、QuantDinger 的多租户交易 SaaS 架构、headroom 的 LLM 上下文压缩代理层，均具备工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：`Financial_freedom`（“最全赚钱投资指南”）描述带有明显营销色彩，且无 license、无 topics，需谨慎对待。多个 `trading_bot` 标记项目（awesome-selfhosted、build-your-own-x 等）实为资源列表，并非真实交易机器人，分类噪声明显。所有涉及 crypto、杠杆、自动交易的项目均需按高风险对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | iFixAi | 23609 | +481 | +3558 | Python | AI 审计/风控 | AI Agent 独立审计，120 秒内回答“Agent 是否在做该做的事” | 高：Agent 治理、合规审计 | 低 |
| 2 | ui-ux-pro-max-skill | 134588 | +292 | +1736 | Python | AI 设计技能 | 多平台 UI/UX 设计智能技能包 | 中：Agent 前端生成 | 低 |
| 3 | awesome-selfhosted | 325410 | +353 | +1697 | 无 | 自托管资源 | 自托管网络服务列表 | 低：基础设施选型 | 中 |
| 4 | colibri | 41073 | +217 | +1697 | C | 本地推理 | 纯 C 零依赖流式运行 MoE 模型 | 高：边缘推理架构 | 低 |
| 5 | public-apis | 487341 | +294 | +1423 | Python | API 资源 | 免费 API 集合 | 中：数据源调研 | 中 |
| 6 | awesome-python | 326450 | +228 | +1446 | Python | Python 资源 | Python 工具精选列表 | 低：技术选型 | 低 |
| 7 | open-design | 100445 | +180 | +1106 | TypeScript | AI 设计 | 本地优先的 AI 设计引擎 | 中：Agent 设计工作流 | 低 |
| 8 | awesome-go | 187780 | +166 | +964 | Go | Go 资源 | Go 框架与库精选列表 | 低：交易系统选型 | 中 |
| 9 | Financial_freedom | 6870 | +118 | +1219 | 无 | 投资指南 | “最全赚钱投资指南” | 低：内容质量存疑 | 中 |
| 10 | build-your-own-x | 552429 | +171 | +1004 | Markdown | 教程资源 | 从零复刻技术的教程集合 | 中：交易系统复刻 | 中 |
| 11 | TradingAgents | 110538 | +115 | +874 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高：多 Agent 交易架构 | 低 |
| 12 | awesome-design-md | 120198 | +117 | +751 | 无 | 设计系统 | DESIGN.md 设计系统集合 | 中：Agent UI 规范 | 中 |
| 13 | headroom | 74973 | +116 | +602 | Python | LLM 压缩 | LLM 上下文压缩库/代理/MCP | 高：降低 Agent token 成本 | 低 |
| 14 | awesome-dsh-plugin | 18332 | +82 | +632 | JavaScript | 插件资源 | DeepSeek Harness 插件列表 | 低：Agent 插件生态 | 低 |
| 15 | Vibe-Trading | 35162 | +71 | +650 | Python | AI 交易/回测 | “Vibe-Trading”个人交易 Agent | 高：MCP 多智能体交易 | 中 |
| 16 | unsloth | 77742 | +80 | +558 | Python | LLM 微调 | 本地 LLM 训练/微调 UI | 中：金融 LLM 微调 | 低 |
| 17 | ruflo | 74307 | +88 | +492 | TypeScript | Agent 框架 | 多智能体 swarm 编排框架 | 高：Agent 编排 | 低 |
| 18 | needle | 13819 | +64 | +666 | Python | 边缘 AI | 微型设备自动化基础模型 | 中：端侧 Agent | 中 |
| 19 | Kronos | 40482 | +92 | +602 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融时序模型 | 低 |
| 20 | CyberStrikeAI | 7552 | +194 | +415 | Go | AI 安全 | AI 原生网络安全行动系统 | 中：Agent 安全治理 | 低 |
| 21 | awesome-claude-code | 55408 | +72 | +376 | Python | Claude 资源 | Claude Code 资源精选 | 低：Agent 工具链 | 低 |
| 22 | awesome-mcp-servers | 96087 | +74 | +284 | 无 | MCP 资源 | MCP 服务器集合 | 中：数据/工具接入 | 低 |
| 23 | Soup | 8515 | +64 | +435 | Python | LLM 微调 | 单 YAML 微调 LLM，4GB 显存训练 8B | 中：低成本微调 | 低 |
| 24 | ds4 | 23764 | +19 | +550 | C | 本地推理 | DeepSeek 4 本地推理引擎 | 中：本地推理 | 低 |
| 25 | OpenStock | 20003 | +47 | +369 | TypeScript | 行情平台 | 开源实时行情与提醒平台 | 高：行情产品架构 | 低 |
| 26 | BitNet | 40586 | +210 | +224 | C++ | 量化推理 | 1-bit LLM 官方推理框架 | 中：模型量化 | 低 |
| 27 | daily_stock_analysis | 66153 | +34 | +282 | Python | AI 股票分析 | LLM 多市场股票分析系统 | 高：LLM 投研流水线 | 低 |
| 28 | atomic-agent | 3232 | +24 | +494 | TypeScript | 本地 Agent | 本地优先 AI Agent，llama.cpp 运行 | 中：本地 Agent | 中 |
| 29 | OpenBB | 74087 | +44 | +264 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高：金融数据层 | 中 |
| 30 | free-for-dev | 139327 | +45 | +190 | HTML | 免费资源 | SaaS/PaaS/IaaS 免费层列表 | 低：基础设施选型 | 低 |
| 31 | skill | 7809 | +53 | +293 | Python | Agent 技能库 | AI Agent 技能商店 | 中：Agent 技能复用 | 低 |
| 32 | OpenBot | 6315 | +30 | +338 | TypeScript | Agent 治理 | 开源 AI 同事，每步行动前决策、后记录 | 高：Agent 行动审计 | 中 |
| 33 | agentic-awesome-skills | 47441 | +38 | +213 | Python | Agent 技能 | 2400+ Agent 技能控制平面 | 中：Agent 技能管理 | 低 |
| 34 | aurelio-finance | 2095 | +539 | 信息不足 | Python | 个人金融 | 开源个人财务 + AI 顾问 | 中：个人金融 Agent | 低 |
| 35 | QuantDinger | 12649 | +43 | +231 | Python | AI 交易 OS | 开源 AI 交易 OS，多租户交易 SaaS | 高：交易 SaaS 架构 | 中 |
| 36 | logo-design-skill | 2670 | +195 | 信息不足 | HTML | 设计技能 | Logo 设计 Agent 技能 | 低：设计自动化 | 低 |
| 37 | gbrain | 30756 | +21 | +238 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中：Agent 框架 | 低 |
| 38 | prompt-master | 14283 | +47 | +258 | 无 | 提示工程 | 精准提示词生成技能 | 中：提示词优化 | 低 |
| 39 | tick-stock-panel | 5767 | +25 | +257 | Python | A 股量化 | A 股自建策略+监控+回测工作台 | 高：A 股量化工作台 | 低 |
| 40 | oh-my-openagent | 69950 | +26 | +170 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中：Agent 编排 | 低 |
| 41 | locally-uncensored | 2176 | +39 | +264 | TypeScript | 本地 AI | 桌面端本地 AI 工作室 | 低：本地 AI 应用 | 低 |
| 42 | awesome-cpp | 73731 | +18 | +132 | 无 | C++ 资源 | C++ 框架与库精选 | 低：低延迟系统选型 | 低 |
| 43 | project-maya | 317 | +84 | 信息不足 | C++ | 本地推理 | GLM-5.3-Flash MoE 本地推理 | 中：MoE 本地部署 | 低 |
| 44 | awesome-public-datasets | 79419 | +11 | +117 | 无 | 数据集资源 | 高质量公开数据集列表 | 中：金融数据源 | 中 |
| 45 | awesome-rust | 59767 | +20 | +98 | Rust | Rust 资源 | Rust 代码与资源精选 | 低：低延迟系统选型 | 低 |
| 46 | ai-hedge-fund | 63929 | +11 | +82 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高：多 Agent 投研 | 低 |
| 47 | awesome-machine-learning | 74568 | +8 | +52 | Python | ML 资源 | 机器学习框架与库精选 | 低：ML 选型 | 低 |
| 48 | cs-video-courses | 83651 | +9 | +47 | 无 | 课程资源 | CS 视频课程列表 | 低：学习资源 | 中 |
| 49 | awesome-vue | 73515 | -2 | -21 | 无 | Vue 资源 | Vue.js 资源精选 | 低：前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi（AI Agent 审计）

- **解决什么问题**：AI Agent 经济中“Agent 是否在做它该做的事”的验证问题。支持人工或 Agent 自审计，120 秒内给出结论。
- **为什么值得关注**：24h +481 星、7d +3558 星，是本期涨星最猛的项目。AI Agent 审计正从概念走向产品化，与金融交易场景中的合规、风控、行为监控需求直接相关。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 覆盖 agent-evaluation、ai-governance、hallucination-detection、prompt-injection、owasp-llm、nist-ai-rmf、iso-42001、eu-ai-act 等，说明其审计维度对齐主流 AI 治理框架。CLI 形态，适合嵌入 CI/CD 或 Agent 流水线。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。可将“Agent 行为审计”作为交易 Agent 上线前的强制关卡，检测幻觉、提示注入、越权操作，形成“决策-执行-审计”闭环。
- **可能的风险**：审计结论的可靠性依赖底层检测规则和模型，存在误报/漏报；金融场景需额外定制合规规则，不能直接照搬通用审计。

### 3.2 TradingAgents（多智能体 LLM 金融交易框架）

- **解决什么问题**：用多智能体 LLM 框架模拟金融交易决策流程。
- **为什么值得关注**：110k+ stars，7d +874，是 AI 交易领域标杆项目之一。Apache-2.0，Python，topics 明确包含 agent、finance、llm、multiagent、trading。
- **技术栈/架构亮点**：多智能体分工（如基本面、技术面、情绪面、风控等角色），LLM 驱动决策。适合研究多 Agent 协作在金融决策中的信息融合与冲突消解。
- **是否适合借鉴**：适合。可借鉴其多角色 Agent 编排模式，构建企业级投研 Agent 团队。但需注意其决策链路与真实交易执行之间的鸿沟。
- **可能的风险**：策略过拟合、回测幸存者偏差、LLM 幻觉导致错误决策；项目定位偏研究工具，不应直接用于实盘。

### 3.3 Vibe-Trading（个人交易 Agent）

- **解决什么问题**：将“vibe trading”概念落地为可运行的 AI 交易 Agent，支持回测与策略研究。
- **为什么值得关注**：HKUDS 出品，35k+ stars，7d +650。topics 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent、quantitative-finance。
- **技术栈/架构亮点**：Python + MIT。MCP 集成意味着可接入外部数据源和工具，多智能体架构支持策略研究。与 TradingAgents 形成“学术框架 vs 工程框架”的互补。
- **是否适合借鉴**：适合。MCP 集成模式值得在交易 Agent 中推广，便于数据源和交易接口的标准化接入。
- **可能的风险**：crypto_related 标记，涉及加密货币交易；vibe trading 概念本身带有非理性决策色彩，需警惕策略过拟合和情绪化交易。

### 3.4 QuantDinger（AI 交易 OS / 多租户交易 SaaS）

- **解决什么问题**：提供开源 AI 交易操作系统，支持研究、Python 策略构建、回测、paper/live 交易，覆盖 crypto、股票、外汇，并可启动多租户交易 SaaS。
- **为什么值得关注**：12.6k stars，7d +231。架构野心大，直接对标交易 SaaS 平台。
- **技术栈/架构亮点**：Python + Apache-2.0。内置用户管理、计费、支付、结算，MCP server 集成，支持 Alpaca、Binance 等。多租户 SaaS 架构是区别于其他交易框架的亮点。
- **是否适合借鉴**：适合借鉴其“交易策略 + SaaS 化”的产品架构，尤其是多租户隔离、计费结算模块。但不应直接运行或接入真实 API。
- **可能的风险**：crypto_related、涉及 live trading、多交易所接入，API key 安全风险高；多租户架构若隔离不当可能引发资金安全问题。

### 3.5 Kronos（金融市场语言基础模型）

- **解决什么问题**：构建金融市场专用基础模型，学习“金融市场语言”。
- **为什么值得关注**：40k+ stars，7d +602。金融基础模型是量化研究的前沿方向，若其模型能力属实，可显著降低金融时序建模门槛。
- **技术栈/架构亮点**：Python + MIT。定位为 Foundation Model，面向金融时序数据。但 topics 为空，且最近 push 在 2026-04-13，维护活跃度存疑。
- **是否适合借鉴**：适合作为研究方向跟踪，探索金融基础模型在预测、异常检测、策略生成中的应用。
- **可能的风险**：模型能力未经独立验证，存在过度宣传可能；金融基础模型的训练数据和评估方法不透明，需警惕回测造假。

### 3.6 headroom（LLM 上下文压缩）

- **解决什么问题**：在工具输出、日志、文件、RAG 块到达 LLM 前进行压缩，降低 token 消耗（编码 Agent 省 20%，JSON 省 60-95%），同时保持答案质量。
- **为什么值得关注**：75k stars，7d +602。直接解决 Agent 规模化中的 token 成本瓶颈，对金融数据密集型 Agent 尤其有价值。
- **技术栈/架构亮点**：Python + Apache-2.0。提供库、代理、MCP server 三种形态，支持 Claude Code、Cursor、LangChain 等。压缩与上下文工程结合，是 Agent 基础设施层的关键组件。
- **是否适合借鉴**：非常适合。金融 Agent 常需处理大量行情、新闻、财报数据，上下文压缩可显著降低成本、提升吞吐。
- **可能的风险**：压缩可能损失关键信息，金融场景需验证压缩后决策质量不下降。

### 3.7 OpenStock（开源行情平台）

- **解决什么问题**：替代昂贵市场平台的免费开源方案，提供实时价格、个性化提醒、公司洞察。
- **为什么值得关注**：20k stars，7d +369。TypeScript + AGPL-3.0，topics 含 nextjs、shadcn-ui、tailwindcss、inngest，技术栈现代。
- **技术栈/架构亮点**：Next.js + Inngest（事件驱动）+ shadcn-ui。前后端一体化，适合快速搭建行情类产品。
- **是否适合借鉴**：适合。可作为金融数据产品的前端架构参考，尤其是实时行情推送和提醒系统。
- **可能的风险**：AGPL-3.0 许可证对商业闭源使用有限制；数据源合规性需自行核实。

### 3.8 daily_stock_analysis（LLM 多市场股票分析）

- **解决什么问题**：LLM 驱动的多市场股票智能分析，多源行情、实时新闻、决策看板、自动推送，支持零成本定时运行。
- **为什么值得关注**：66k stars，7d +282。topics 含 a-stock、ai-agent、quant、quantitative-finance，聚焦 A 股场景。
- **技术栈/架构亮点**：Python + MIT。多源数据接入 + LLM 分析 + 自动推送，形成完整的投研自动化流水线。
- **是否适合借鉴**：适合。其“数据采集-LLM 分析-决策看板-自动推送”的流水线模式可直接复用到企业级投研 Agent。
- **可能的风险**：LLM 分析结论的可靠性存疑，不应作为投资决策依据；A 股数据源合规性需关注。

### 3.9 ai-hedge-fund（AI 对冲基金团队）

- **解决什么问题**：模拟 AI 对冲基金团队的多 Agent 决策流程。
- **为什么值得关注**：63.9k stars，是 AI 交易领域的知名项目。Python + MIT。
- **技术栈/架构亮点**：多 Agent 角色模拟（如分析师、交易员、风控），适合研究 Agent 协作模式。
- **是否适合借鉴**：适合作为多 Agent 投研流程的教学和原型参考。
- **可能的风险**：定位为研究/教育工具，不应直接用于实盘；策略过拟合和回测偏差风险高。

### 3.10 OpenBot（AI 同事 + 行动审计）

- **解决什么问题**：开源 AI 同事，每个 Agent 拥有独立浏览器、文件和工具，每步行动前决策、后记录。
- **为什么值得关注**：CopilotKit 出品，6.3k stars，7d +338。topics 含 agent-governance、ag-ui、generative-ui、mcp。
- **技术栈/架构亮点**：TypeScript + MIT。AG-UI 协议 + 行动前决策/后记录，与 iFixAi 形成互补：一个管行动审计，一个管行为审计。
- **是否适合借鉴**：适合。其“行动前决策、行动后记录”的治理模式可引入交易 Agent，形成可追溯的操作日志。
- **可能的风险**：trading_bot 标记，若用于交易场景需额外风控；Agent 自主操作浏览器的安全边界需谨慎。

## 4. 趋势归纳

### 技术趋势
- **本地化/边缘化 LLM 推理加速**：colibri（纯 C 流式 MoE）、ds4（Metal/CUDA/ROCm）、BitNet（1-bit LLM）、needle（微型设备）、project-maya（GLM MoE 本地部署）共同指向“在自有硬件上运行大模型”的趋势，量化研究对数据隐私和推理成本敏感，本地推理需求上升。
- **LLM 上下文工程**：headroom 的上下文压缩、prompt-master 的提示词优化，反映 Agent 规模化中的 token 成本优化成为基础设施层刚需。
- **MCP 标准化**：Vibe-Trading、QuantDinger、OpenBot、headroom 等均集成 MCP，工具/数据接入标准化趋势明显。

### 产品趋势
- **AI Agent 治理产品化**：iFixAi、OpenBot 将 Agent 审计和行动治理产品化，从“能做什么”转向“做得对不对”。
- **交易 SaaS 化**：QuantDinger 的多租户交易 SaaS 架构，反映交易工具从单机脚本向平台化演进。
- **个人金融 AI 化**：aurelio-finance 将 AI 顾问嵌入个人财务追踪，金融 AI 从机构场景向个人场景下沉。

### 量化/交易策略趋势
- **多智能体 LLM 交易框架成为主流形态**：TradingAgents、Vibe-Trading、ai-hedge-fund、QuantDinger 均采用多 Agent 架构，角色分工（分析、决策、风控）成为标配。
- **金融基础模型探索**：Kronos 尝试构建金融市场专用基础模型，若成功将改变策略研发范式。
- **A 股量化工作台兴起**：daily_stock_analysis、tick-stock-panel 聚焦 A 股，结合 LLM 与回测，反映本土化量化工具需求。

### AI Agent 与自动化交易结合趋势
- **从“AI 辅助决策”到“AI 自主执行 + 审计”**：Vibe-Trading、QuantDinger 支持 paper/live trading，iFixAi、OpenBot 提供审计和治理，形成“决策-执行-审计”闭环。
- **本地优先 Agent**：atomic-agent、locally-uncensored 强调本地运行，契合金融数据隐私需求。

### 值得后续做原型验证的方向
- Agent 行为审计嵌入交易流水线
- MCP 标准化的金融数据接入层
- 本地化 LLM 推理 + 金融时序模型
- 多租户交易 SaaS 的最小可行架构
- LLM 上下文压缩在金融数据分析中的效果验证

## 5. 今日灵感清单

1. **MVP：交易 Agent 行动审计中间件**。参考 iFixAi + OpenBot，构建一个轻量级审计层，在交易 Agent 执行前检查指令合法性、执行后记录操作日志，输出审计报告。可先做 Python CLI 原型。

2. **调研：MCP 金融数据接入标准化**。调研 Vibe-Trading、QuantDinger、OpenBB 的 MCP 集成方式，设计统一的金融数据 MCP server 接口规范，覆盖行情、新闻、财报、链上数据。

3. **Demo：本地化金融 LLM 推理**。用 colibri 或 ds4 在本地 GPU 上运行量化模型，验证金融时序预测任务的推理延迟和精度，对比云端 API 的成本差异。

4. **原型：LLM 上下文压缩用于财报分析**。用 headroom 压缩长财报、新闻流，测试压缩后 LLM 分析结论的一致性，量化 token 节省比例。

5. **复现：多智能体投研流程**。基于 TradingAgents 或 ai-hedge-fund 的架构，用 Codex/Agent 自动复现一个简化版多角色投研 Agent（分析师、风控、决策），输出研究报告。

6. **调研：金融基础模型 Kronos**。深入调研 Kronos 的模型架构、训练数据、评估方法，验证其在波动率预测、异常检测等任务上的实际能力。

7. **MVP：A 股量化工作台**。参考 tick-stock-panel 的架构（DuckDB + Polars + FastAPI + React），搭建一个轻量级 A 股策略回测与监控面板，集成 LLM 策略生成。

8. **原型：Agent 技能商店的金融技能包**。参考 skill、agentic-awesome-skills，构建金融领域专用 Agent 技能包（财报解析、技术指标计算、风险评分），验证技能复用模式。

9. **调研：OpenStock 的实时行情架构**。研究其 Next.js + Inngest 的实时推送架构，评估能否复用到自建行情监控系统。

10. **Watchlist 候选**：iFixAi、Vibe-Trading、QuantDinger、Kronos、headroom、OpenBot、tick-stock-panel、aurelio-finance。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计赛道领跑者，涨星迅猛，治理/合规方向与金融场景高度契合 |
| Vibe-Trading | HKUDS 出品，MCP + 多智能体交易，工程架构值得持续跟踪 |
| QuantDinger | 交易 SaaS 化架构独特，多租户、计费、结算模块有参考价值 |
| Kronos | 金融基础模型前沿探索，若验证成功将改变量化研究范式 |
| headroom | LLM 上下文压缩基础设施，金融数据密集型 Agent 的降本关键 |
| OpenBot | Agent 行动治理模式，与 iFixAi 互补，适合交易 Agent 操作审计 |
| tick-stock-panel | A 股量化工作台，DuckDB + Polars 技术栈现代，本土化场景明确 |
| aurelio-finance | 个人金融 + AI 顾问，新项目涨星快，产品方向值得观察 |
| OpenStock | 开源行情平台，实时推送架构可参考 |
| colibri | 本地 MoE 推理，纯 C 零依赖架构，边缘推理方向代表 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-10-09）和 `baseline_7d`（2026-10-03），1 日和 7 日涨星数据基本完整。
- **缺失数据**：部分项目（aurelio-finance、logo-design-skill、project-maya）的 `star_delta_7d` 为 null，原因是项目创建时间晚于 7 日基线或基线数据缺失，已在表格中标注“信息不足”。
- **采集失败**：未发现明显采集失败迹象，但 `star_delta_30d` 字段全部为 null，说明 30 日基线未纳入本次采集。
- **样本偏差**：候选列表包含大量 awesome-list 类资源项目（awesome-selfhosted、awesome-python、awesome-go、build-your-own-x 等），这些项目因关键词匹配进入候选，但并非金融/量化/交易专用项目，分类噪声明显。真正聚焦金融/量化/交易的项目占比有限，分析时需注意区分。
