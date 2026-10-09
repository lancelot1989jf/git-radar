# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-08

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：iFixAi 以 24h +334、7d +4081 的涨星领跑，聚焦“AI Agent 是否在做它该做的事”，直接切入 AI Agent 经济中的可信、合规与风控问题。
  2. **本地化/边缘化大模型推理**：colibri（纯 C、零依赖、MoE 专家从磁盘流式加载）和 needle（2-bit、8–29 MB 的微型自动化基础模型）显示“在自有硬件上跑前沿模型”正在成为强趋势。
  3. **AI 原生设计/UI 生成与 Agent 技能生态**：ui-ux-pro-max-skill、open-design、awesome-design-md 等大量涨星，说明“让 coding agent 直接产出可交付 UI/设计文件”的产品化路径非常活跃。

- **是否出现新趋势**：出现。AI Agent 的**可审计性、可观测性、可治理性**开始成为独立赛道；同时“本地优先、BYOK、零云依赖”的 Agent 与模型推理工具明显升温。

- **是否出现值得复刻/参考的工程架构**：是。iFixAi 的“120 秒内回答 Agent 是否按预期工作”的审计架构、colibri 的“磁盘流式加载 MoE 专家”的推理架构、headroom 的“LLM 上下文压缩代理/MCP server”架构，都值得工程化借鉴。

- **是否有明显骗局、过度营销或高风险项目**：有疑似过度营销项目。`polymarket-trading-bot-quant-course` 描述中大量重复“Polymarket trading bot”，且为“Paid VIP program”，stars 仅 121、forks 仅 1，存在付费课程导流嫌疑，应谨慎对待。`Financial_freedom` 描述为“最全赚钱投资指南”，24h 涨星 +402 但内容与工程价值存疑，属于高营销风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | iFixAi | 22769 | +334 | +4081 | Python | AI 审计/风控 | 对 AI Agent 进行独立审计，120 秒内判断 Agent 是否按预期工作 | 高：Agent 治理、合规审计 | 低 |
| 2 | colibri | 40622 | +235 | +1717 | C | 本地推理 | 纯 C、零依赖，在自有硬件上运行前沿 MoE 模型 | 高：边缘推理、资源受限部署 | 低 |
| 3 | ui-ux-pro-max-skill | 133985 | +84 | +1587 | Python | AI 设计技能 | 为多平台 UI/UX 提供设计智能的 AI skill | 中：Agent 技能化产品 | 低 |
| 4 | awesome-selfhosted | 324775 | +43 | +1500 | 无 | 自托管清单 | 可自托管的免费网络服务与 Web 应用列表 | 中：自托管基础设施选型 | 中 |
| 5 | public-apis | 486843 | +7 | +1511 | Python | API 清单 | 免费 API 集合列表 | 中：数据源发现 | 中 |
| 6 | open-design | 100097 | +179 | +989 | TypeScript | AI 设计工具 | 本地优先桌面应用，让 coding agent 成为设计引擎 | 高：Agent 驱动交付物生成 | 低 |
| 7 | awesome-python | 325968 | +2 | +1391 | Python | Python 清单 | Python 工具选型权威列表 | 低：通用资源 | 低 |
| 8 | TradingAgents | 110316 | +135 | +826 | Python | AI 交易/多 Agent | 多 Agent LLM 金融交易框架 | 高：多 Agent 交易研究 | 低 |
| 9 | needle | 13626 | +219 | +694 | Python | 边缘 AI | 面向微型设备的 2-bit 自动化基础模型 | 高：端侧 Agent 能力 | 中 |
| 10 | awesome-dsh-plugin | 18131 | +99 | +557 | JavaScript | 插件清单 | DeepSeek Harness 插件精选列表 | 中：Agent 插件生态 | 低 |
| 11 | Financial_freedom | 6382 | +402 | +829 | 无 | 投资指南 | “最全赚钱投资指南” | 低：营销内容，工程价值低 | 中 |
| 12 | headroom | 74781 | +150 | +521 | Python | LLM 上下文压缩 | 压缩工具输出、日志、RAG 块，降低 token 消耗 | 高：Agent 成本优化 | 低 |
| 13 | ds4 | 23716 | +38 | +865 | C | 本地推理 | DeepSeek 4 Flash/PRO 本地推理引擎 | 中：本地模型推理 | 低 |
| 14 | Vibe-Trading | 35040 | +78 | +601 | Python | AI 交易/回测 | “Vibe-Trading：你的个人交易 Agent” | 高：LLM 交易 Agent 框架 | 中 |
| 15 | awesome-go | 187440 | -9 | +945 | Go | Go 清单 | Go 框架、库与软件精选列表 | 低：通用资源 | 中 |
| 16 | unsloth | 77559 | +141 | +435 | Python | LLM 微调 | 本地 UI 运行和训练 LLM 与扩散模型 | 中：本地模型训练 | 低 |
| 17 | build-your-own-x | 552067 | -29 | +955 | Markdown | 教程清单 | 从零重建你喜欢的技术的教程集合 | 低：通用学习资源 | 中 |
| 18 | awesome-design-md | 119945 | -36 | +747 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 文件集合 | 中：Agent 设计规范 | 中 |
| 19 | atomic-agent | 3105 | +79 | +540 | TypeScript | 本地 Agent | 本地优先 AI Agent，通过 llama.cpp 运行开源权重模型 | 高：本地 Agent 架构 | 中 |
| 20 | ruflo | 74158 | +61 | +479 | TypeScript | Agent 框架 | 部署多玩家 swarm、协调自主工作流 | 高：多 Agent 编排 | 低 |
| 21 | awesome-claude-code | 55292 | +67 | +372 | Python | Claude Code 资源 | Claude Code 技能、插件、工具精选 | 中：Agent 工具生态 | 低 |
| 22 | Kronos | 40328 | +66 | +530 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融时序基础模型 | 低 |
| 23 | OpenBot | 6241 | +56 | +406 | TypeScript | Agent 治理 | 开源 AI 同事，每个 Agent 拥有自己的计算机 | 高：Agent 操作审计 | 中 |
| 24 | Soup | 8388 | +50 | +412 | Python | LLM 微调 | 一个 YAML 微调 LLM，4GB 笔记本 GPU 训练 8B 模型 | 中：低成本微调 | 低 |
| 25 | langfuse | 35555 | +49 | +263 | TypeScript | LLM 可观测性 | 开源 Agent evals 与可观测性平台 | 高：Agent 监控与评估 | 低 |
| 26 | OpenStock | 19911 | +42 | +333 | TypeScript | 行情终端 | 开源实时行情、个性化提醒、公司洞察平台 | 中：行情产品化 | 低 |
| 27 | daily_stock_analysis | 66059 | +38 | +217 | Python | AI 股票分析 | LLM 驱动的多市场股票智能分析系统 | 高：LLM 金融分析流水线 | 低 |
| 28 | OpenBB | 73996 | +38 | +256 | Python | 金融数据平台 | 面向分析师、量化与 AI Agent 的开放数据平台 | 高：金融数据基础设施 | 中 |
| 29 | tick-stock-panel | 5725 | +25 | +366 | Python | A 股量化工作台 | 自托管 A 股选股+监控+回测量化工作台 | 高：A 股量化工作台 | 低 |
| 30 | locally-uncensored | 2097 | +70 | +216 | TypeScript | 本地 AI 工作室 | 桌面端一体化本地 AI 工作室 | 中：本地 AI 应用 | 低 |
| 31 | agentic-awesome-skills | 47378 | +34 | +210 | Python | Agent 技能控制面 | 本地、agent-first 的控制面，2400+ agentic skills | 中：Agent 技能编排 | 低 |
| 32 | skill | 7702 | +53 | +228 | Python | 技能商店 | 最全 AI Agent 技能商店，自动抓取 GitHub 技能项目 | 中：技能分发 | 低 |
| 33 | gbrain | 30700 | +31 | +212 | TypeScript | Agent 大脑 | Garry 的 OpenClaw/Hermes Agent Brain | 中：Agent 个性化配置 | 低 |
| 34 | awesome-mcp-servers | 95946 | +30 | +189 | 无 | MCP 清单 | MCP server 集合 | 中：MCP 生态 | 低 |
| 35 | oh-my-openagent | 69914 | +27 | +165 | TypeScript | Agent 编排 | 图工程化 Agent 编排工具 | 中：Agent 工作流编排 | 低 |
| 36 | logo-design-skill | 2392 | +84 | 无 | HTML | 设计技能 | 面向 Claude/Gemini/Codex 的 logo 设计技能 | 低：垂直设计技能 | 低 |
| 37 | QuantDinger | 12571 | +27 | +205 | Python | AI 交易 OS | 开源 AI Trading OS，支持策略研究、回测、模拟/实盘 | 高：交易系统产品化 | 中 |
| 38 | awesome-cpp | 73701 | +23 | +137 | 无 | C++ 清单 | C/C++ 框架、库与资源精选 | 低：通用资源 | 低 |
| 39 | prompt-master | 14196 | +28 | +248 | 无 | Prompt 技能 | 为任意 AI 工具编写准确 prompt 的 Claude skill | 中：Prompt 工程 | 低 |
| 40 | free-for-dev | 139235 | -137 | +187 | HTML | 免费资源 | 面向开发者的免费 SaaS/PaaS/IaaS 列表 | 低：通用资源 | 低 |
| 41 | trading-terminal | 497 | +39 | +258 | TypeScript | AI 交易终端 | Hyperliquid 自托管 AI 交易终端 | 高：交易终端产品化 | 低 |
| 42 | CyberStrikeAI | 7228 | +48 | +99 | Go | AI 安全 | AI 原生网络安全的行动系统 | 中：Agent 安全治理 | 低 |
| 43 | awesome-public-datasets | 79387 | +11 | +112 | 无 | 数据集清单 | 主题中心的高质量开放数据集列表 | 中：数据源发现 | 中 |
| 44 | awesome-rust | 59730 | +20 | +91 | Rust | Rust 清单 | Rust 代码与资源精选 | 低：通用资源 | 低 |
| 45 | awesome-remote-mcp-servers | 949 | +48 | 无 | 无 | MCP 清单 | 远程 MCP server 集合 | 中：远程 MCP 生态 | 中 |
| 46 | project-maya | 153 | +75 | 无 | C++ | 本地推理 | 在自有 NVIDIA GPU 上运行 GLM-5.3-Flash | 中：本地大模型推理 | 低 |
| 47 | ai-hedge-fund | 63909 | +8 | +77 | Python | AI 对冲基金 | AI 对冲基金团队 | 高：多 Agent 投研 | 低 |
| 48 | awesome-machine-learning | 74550 | +7 | +46 | Python | ML 清单 | 机器学习框架、库与软件精选 | 低：通用资源 | 低 |
| 49 | cs-video-courses | 83641 | +1 | +42 | 无 | 课程清单 | 带视频讲座的计算机科学课程列表 | 低：学习资源 | 中 |
| 50 | awesome-vue | 73521 | -4 | -16 | 无 | Vue 清单 | Vue.js 相关精选列表 | 低：通用资源 | 低 |
| 51 | polymarket-trading-bot-quant-course | 121 | +47 | 无 | 无 | 付费课程 | 付费 VIP 课程：Polymarket 交易机器人开发 | 低：疑似付费导流 | 中 |

## 3. 重点项目深度分析

### 3.1 iFixAi — AI Agent 独立审计

- **解决什么问题**：回答“AI Agent 是否在做它该做的事”。在 AI Agent 经济中，Agent 可能产生幻觉、被 prompt 注入、偏离目标或产生不合规行为，iFixAi 试图在 120 秒内给出审计结论。
- **为什么值得关注**：24h +334、7d +4081 的涨星说明市场对 Agent 可信度、AI 治理、AI 对齐的需求正在爆发。其 topics 覆盖 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM，说明它把合规框架工程化了。
- **技术栈/架构亮点**：Python + CLI，Apache-2.0。从 topics 看，包含 agent-evaluation、hallucination-detection、prompt-injection、llm-security、risk-assessment 等模块，是一套面向 Agent 的评估与诊断工具链。
- **是否适合借鉴到 AI/自动化交易**：非常适合。交易 Agent 的决策可审计性、幻觉检测、prompt 注入防护、合规留痕，都可以参考其评估框架。可将其思路改造成“交易 Agent 决策审计器”。
- **风险**：作为审计工具本身风险较低。但需注意其审计结论的可靠性、评估基准是否可被操纵，以及是否真正覆盖金融场景的合规要求。

### 3.2 colibri — 纯 C 零依赖 MoE 本地推理

- **解决什么问题**：在用户已有硬件上运行前沿 MoE 模型，专家从磁盘流式加载，避免把整个大模型装入内存。
- **为什么值得关注**：24h +235、7d +1717，stars 40622。纯 C、零依赖、磁盘流式加载专家的架构，对量化研究中的本地模型部署、低资源环境推理非常有参考价值。
- **技术栈/架构亮点**：C 语言实现，Apache-2.0。核心是“小引擎 + 大模型”的分离设计，专家按需从磁盘加载，降低内存占用。
- **是否适合借鉴**：适合。量化团队若希望在本地跑大模型做因子挖掘、研报解析、新闻情绪分析，又不想依赖云 API，可以参考其“按需加载专家”的思路，构建低成本的本地推理层。
- **风险**：低。但需关注其维护活跃度、模型格式兼容性，以及磁盘 I/O 可能成为推理延迟瓶颈。

### 3.3 TradingAgents — 多 Agent LLM 金融交易框架

- **解决什么问题**：用多个 LLM Agent 协作完成金融交易决策，模拟投研团队的分工。
- **为什么值得关注**：stars 110316，24h +135、7d +826。是“LLM 多 Agent 交易”方向最具代表性的开源项目之一。
- **技术栈/架构亮点**：Python，Apache-2.0。topics 为 agent、finance、llm、multiagent、trading。架构上采用多 Agent 分工，可能包含基本面、技术面、情绪面、风控等角色。
- **是否适合借鉴**：适合作为多 Agent 交易研究的参考框架。但应将其视为研究工具，而非直接实盘系统。
- **风险**：策略过拟合、回测幸存者偏差、LLM 幻觉导致错误交易信号。其 risk_flags 包含 likely_research_tool，说明定位是研究而非生产。

### 3.4 Vibe-Trading — 个人交易 Agent

- **解决什么问题**：提供“Vibe-Trading”个人交易 Agent，结合 LLM、MCP、多 Agent 与回测能力。
- **为什么值得关注**：stars 35040，24h +78、7d +601。HKUDS 出品，topics 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent、quantitative-finance，是学术机构在 AI 交易 Agent 方向的代表项目。
- **技术栈/架构亮点**：Python，MIT。集成 MCP 与多 Agent，强调回测与量化金融。
- **是否适合借鉴**：适合研究“LLM 交易 Agent 的模块化设计”和“MCP 在交易工具调用中的应用”。但不应直接用于实盘。
- **风险**：crypto_related、likely_research_tool。加密市场波动大，LLM 交易信号可能不稳定，存在策略过拟合与资金风险。

### 3.5 headroom — LLM 上下文压缩

- **解决什么问题**：在工具输出、日志、文件、RAG 块进入 LLM 前进行压缩，降低 token 消耗，同时保持回答质量。
- **为什么值得关注**：stars 74781，24h +150、7d +521。对交易 Agent 这种需要大量行情、订单簿、新闻输入的场景，上下文压缩能直接降低成本、提升上下文利用率。
- **技术栈/架构亮点**：Python，Apache-2.0。提供 library、proxy、MCP server 三种形态，覆盖 FastAPI、LangChain、OpenAI、Anthropic 等生态。
- **是否适合借鉴**：非常适合。交易 Agent 的上下文窗口常被行情数据、历史订单、新闻淹没，可引入其压缩层作为“上下文工程”基础设施。
- **风险**：低。但需验证压缩是否丢失关键金融信息，尤其在订单簿、价格跳变等细节上。

### 3.6 Kronos — 金融市场语言基础模型

- **解决什么问题**：构建金融市场的语言基础模型，试图用统一模型理解金融时序、新闻、价格等“市场语言”。
- **为什么值得关注**：stars 40328，24h +66、7d +530。是“金融基础模型”方向的代表性尝试，对量化研究有长期参考价值。
- **技术栈/架构亮点**：Python，MIT。具体架构信息不足，但从定位看属于预训练金融基础模型。
- **是否适合借鉴**：适合作为研究方向跟踪。若其模型权重或训练方法开放，可研究金融时序 token 化、跨资产表示学习。
- **风险**：likely_research_tool。金融基础模型可能过拟合历史数据，且近期 push 时间为 2026-04-13，维护活跃度需关注。

### 3.7 daily_stock_analysis — LLM 多市场股票分析系统

- **解决什么问题**：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：stars 66059，forks 55034，24h +38、7d +217。是“LLM + 金融数据 + 自动推送”的完整产品化范例，尤其适合 A 股场景。
- **技术栈/架构亮点**：Python，MIT。topics 覆盖 a-stock、ai-agent、llm、quant、quantitative-finance。强调多源数据、自动推送、零成本定时运行。
- **是否适合借鉴**：适合。可作为“LLM 金融分析流水线”的参考，学习其数据接入、新闻处理、决策看板与推送机制。
- **风险**：低。但需注意数据源合规性、新闻情绪分析的准确性，以及“决策看板”不应被误读为投资建议。

### 3.8 OpenBB — 开放金融数据平台

- **解决什么问题**：为分析师、量化与 AI Agent 提供统一的开放数据平台，覆盖股票、加密、衍生品、固定收益、期权等。
- **为什么值得关注**：stars 73996，24h +38、7d +256。是金融数据基础设施的重要开源项目，且明确面向 AI Agent。
- **技术栈/架构亮点**：Python。topics 覆盖 ai、crypto、derivatives、equity、fixed-income、options、quantitative-finance。
- **是否适合借鉴**：适合。可作为交易 Agent 的数据层，统一接入多资产数据，避免每个 Agent 单独对接数据源。
- **风险**：crypto_related。数据质量、延迟、许可协议需关注。

### 3.9 tick-stock-panel — A 股量化工作台

- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，LLM 驱动策略定制与个股分析。
- **为什么值得关注**：stars 5725，24h +25、7d +366。topics 包含 duckdb、polars、fastapi、react、backtesting，技术栈现代，适合 A 股量化场景。
- **技术栈/架构亮点**：Python，MIT。DuckDB + Polars 做本地分析，FastAPI + React 做界面，LLM 做策略定制与个股分析。
- **是否适合借鉴**：适合。可作为“本地优先量化工作台”的参考，尤其 DuckDB + Polars 的组合对中小规模量化数据工程很有借鉴意义。
- **风险**：likely_research_tool。A 股数据合规、策略过拟合、回测偏差需注意。

### 3.10 ai-hedge-fund — AI 对冲基金团队

- **解决什么问题**：用多个 AI Agent 模拟对冲基金团队，覆盖投研、决策、风控等角色。
- **为什么值得关注**：stars 63909，是“AI 对冲基金”方向的经典项目，虽然近期涨星放缓（24h +8、7d +77），但架构思路仍有参考价值。
- **技术栈/架构亮点**：Python，MIT。多 Agent 协作模拟对冲基金团队。
- **是否适合借鉴**：适合研究多 Agent 投研分工，但不应视为可实盘的系统。
- **风险**：likely_research_tool。策略过拟合、回测偏差、LLM 决策不稳定。

## 4. 趋势归纳

- **技术趋势**：
  - **本地优先与边缘推理**：colibri、needle、ds4、project-maya、atomic-agent、locally-uncensored 等项目共同指向“在自有硬件上运行模型与 Agent”，减少云依赖。
  - **LLM 上下文工程**：headroom 的上下文压缩、prompt-master 的 prompt 优化，说明“如何更高效地利用上下文窗口”成为 Agent 基础设施层的新焦点。
  - **Agent 可观测性与治理**：iFixAi、langfuse、OpenBot、CyberStrikeAI 显示 Agent 的审计、监控、评估、安全正在形成独立技术栈。

- **产品趋势**：
  - **AI 原生设计工具**：ui-ux-pro-max-skill、open-design、awesome-design-md、logo-design-skill 等大量项目将设计能力产品化为“Agent 技能”，让 coding agent 直接产出可交付的 UI/设计文件。
  - **交易终端产品化**：trading-terminal、QuantDinger、OpenStock 显示“自托管交易终端/交易 OS”的产品化路径在加速。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 交易框架**：TradingAgents、Vibe-Trading、ai-hedge-fund、QuantDinger 均采用多 Agent 架构，模拟投研团队分工。
  - **金融基础模型**：Kronos 代表“用基础模型理解金融市场语言”的方向，值得长期跟踪。
  - **A 股本地量化工作台**：daily_stock_analysis、tick-stock-panel 显示 A 股场景下“LLM + 本地数据 + 回测”的组合正在成熟。

- **AI Agent 与自动化交易结合趋势**：
  - **MCP 成为交易工具调用标准**：Vibe-Trading、QuantDinger、trading-terminal、awesome-mcp-servers、awesome-remote-mcp-servers 均涉及 MCP，说明 MCP 正在成为交易 Agent 接入数据与执行工具的标准协议。
  - **Agent 治理进入交易场景**：iFixAi、langfuse、OpenBot 的审计与可观测性能力，可被改造成交易 Agent 的决策留痕与合规审计层。

- **值得后续做原型验证的方向**：
  - 交易 Agent 决策审计器（参考 iFixAi + langfuse）。
  - 本地优先的量化研究工作台（参考 tick-stock-panel 的 DuckDB + Polars + FastAPI）。
  - LLM 上下文压缩层用于行情/新闻密集场景（参考 headroom）。
  - 基于 MCP 的交易数据接入层（参考 OpenBB + MCP）。

## 5. 今日灵感清单

1. **MVP：交易 Agent 决策审计器**。参考 iFixAi 的审计思路，构建一个轻量级工具，记录交易 Agent 的每一步决策、输入输出、模型置信度，并自动检测幻觉、prompt 注入、偏离策略约束的行为。可先做 Python CLI 原型。

2. **MVP：本地优先 A 股量化工作台**。参考 tick-stock-panel，用 DuckDB + Polars 做本地数据存储与因子计算，FastAPI 提供 API，React 做看板，LLM 做策略解释与个股分析。先跑通“选股 + 回测 + 监控”最小闭环。

3. **调研：MCP 在交易 Agent 中的标准化接入**。调研 awesome-mcp-servers、awesome-remote-mcp-servers、Vibe-Trading、QuantDinger 中 MCP 的使用方式，总结交易场景下 MCP server 的设计模式。

4. **调研：LLM 上下文压缩对金融文本的影响**。用 headroom 的思路，测试压缩行情、新闻、研报、订单簿文本后，LLM 在情绪分析、事件抽取、交易信号生成上的质量损失。

5. **Codex/Agent 自动复现 demo：多 Agent 投研流水线**。参考 TradingAgents 或 ai-hedge-fund，让 Codex 自动生成一个最小多 Agent 投研 demo：基本面 Agent、技术面 Agent、情绪 Agent、风控 Agent，输出一份结构化投研报告。

6. **MVP：Agent 技能化的金融分析技能包**。参考 ui-ux-pro-max-skill、skill、agentic-awesome-skills 的技能化思路，把“财报解读”“技术指标分析”“新闻情绪打分”封装成可被 Claude Code/Codex 调用的 skill。

7. **调研：本地边缘模型在金融文本处理中的可行性**。调研 needle、colibri、ds4 等本地推理方案，评估在消费级硬件上跑小型模型做金融文本分类、实体抽取、情绪分析的延迟与准确率。

8. **加入 watchlist：Kronos**。跟踪金融基础模型的进展，关注其是否开放模型权重、训练数据、评估基准，评估未来用于因子挖掘或市场状态识别的可能性。

9. **MVP：交易 Agent 的上下文预算管理器**。参考 headroom 的 proxy 形态，构建一个交易 Agent 的上下文预算管理器，自动决定哪些行情、新闻、历史订单进入上下文，哪些被压缩或丢弃。

10. **调研：Agent 治理与金融合规的映射**。调研 iFixAi 的 EU AI Act、ISO 42001、NIST AI RMF 相关实现，梳理这些合规框架如何映射到自动化交易 Agent 的审计与留痕要求。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计与治理赛道领跑者，7d +4081，合规框架工程化，适合长期跟踪 |
| colibri | 纯 C 零依赖 MoE 本地推理，架构独特，适合跟踪边缘推理进展 |
| TradingAgents | 多 Agent LLM 交易框架代表，适合跟踪 LLM 交易 Agent 的架构演进 |
| Vibe-Trading | HKUDS 出品，MCP + 多 Agent + 回测，学术与工程结合，适合跟踪 |
| Kronos | 金融基础模型方向，长期研究价值高，需关注维护活跃度 |
| headroom | LLM 上下文压缩基础设施，对交易 Agent 成本优化有直接价值 |
| OpenBB | 面向 AI Agent 的开放金融数据平台，适合作为数据层参考 |
| tick-stock-panel | A 股本地量化工作台，DuckDB + Polars + FastAPI 技术栈现代 |
| langfuse | Agent 可观测性与评估平台，适合作为交易 Agent 监控层参考 |
| trading-terminal | Hyperliquid 自托管 AI 交易终端，虽然 stars 低但产品化思路清晰 |
| QuantDinger | AI Trading OS，多租户交易 SaaS 架构，适合研究交易系统产品化 |
| OpenBot | Agent 治理与操作审计，每个 Agent 拥有独立计算机，适合跟踪 Agent 安全 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

特别提醒：

- `polymarket-trading-bot-quant-course` 为付费 VIP 课程，描述中大量重复“Polymarket trading bot”，stars 仅 121、forks 仅 1，存在付费导流嫌疑，不建议付费参与。
- `Financial_freedom` 描述为“最全赚钱投资指南”，24h 涨星 +402 但工程价值低，营销属性强，应谨慎对待。
- 涉及 crypto、杠杆、套利、马丁、网格的项目（如 Vibe-Trading、QuantDinger、awesome-go 中相关条目）存在爆仓与合规风险，不应直接用于实盘。
- 回测数据可能存在幸存者偏差、前视偏差、过拟合，GitHub star 与短期涨星不代表策略收益。

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-10-07.json`，与 `current_snapshot` 日期 `2026-10-08` 相差 1 天，数据有效。
- **7 日基线**：存在，`baseline_7d` 为 `2026-10-01.json`，与 `current_snapshot` 日期 `2026-10-08` 相差 7 天，数据有效。
- **采集失败**：本次数据中未发现明确的采集失败标记。但部分项目 `star_delta_7d` 为 `null`（如 logo-design-skill、awesome-remote-mcp-servers、project-maya、polymarket-trading-bot-quant-course），说明这些项目缺少 7 日基线数据，可能是新项目或基线快照中不存在。
- **样本偏差**：候选项目通过关键词匹配（如 quant、backtesting、crypto trading、fintech、risk management 等）筛选，导致大量“awesome-*”清单类项目（如 awesome-python、awesome-go、awesome-cpp、awesome-rust、awesome-vue）因 README 或 topics 命中关键词而进入候选，稀释了金融/量化/交易项目的纯度。报告已尽量区分“直接相关项目”与“清单/通用资源项目”。
- **分类噪声**：部分项目的 `category_guess` 与 `matched_queries` 存在明显误匹配，例如 colibri（本地推理引擎）被归为 quant_research，needle（边缘 AI 模型）被归为 trading_bot，awesome-selfhosted 被归为 trading_bot。这些分类仅作为参考，不应视为项目的真实用途。
