# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-03

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：`iFixAi` 以 7 日 +7152 星成为本次样本中涨星最高的项目，聚焦 AI Agent 的独立审计、对齐与合规评估，直接回应金融场景中“Agent 是否按预期执行”的核心问题。
  2. **LLM 多智能体金融交易框架**：`TradingAgents`（7 日 +2967）与 `Vibe-Trading`、`ai-hedge-fund` 等形成“多 Agent 分工 + 回测 + 研究”的持续热点，说明 LLM 驱动的交易决策框架仍是量化开源社区最活跃的方向之一。
  3. **本地优先的 AI 工作台与 Agent 编排**：`Orkas`（7 日 +6402）、`OpenBot`、`ruflo` 等项目显示“桌面端/本地优先 + 多 Agent 编排 + 自带浏览器/文件/工具”正在成为新的产品形态，对构建企业级 Agent 工作台有直接参考价值。

- **是否出现新趋势**：出现。本次样本中“AI Agent 技能包 / Skills 商店”类项目大量涌入（如 `ui-ux-pro-max-skill`、`day-trader-skill`、`agentic-awesome-skills`、`skill`），说明围绕 Claude/Codex/Cursor 的可复用技能生态正在快速扩张，其中已出现面向日内交易、金融分析的垂直技能包。

- **是否出现值得复刻/参考的工程架构**：是。`colibri` 提出“GPU 热专家 / RAM 温专家 / NVMe 冷专家”的分层 MoE 推理引擎，对低资源环境下部署大型金融 LLM 有参考价值；`headroom` 的“LLM 前 token 压缩”思路可用于降低金融新闻、行情日志、RAG 上下文的推理成本。

- **是否有明显骗局、过度营销或高风险项目**：本次样本中未发现明显骗局，但存在大量“awesome-list”类项目因关键词误匹配进入候选（如 `public-apis`、`build-your-own-x`、`awesome-selfhosted`），其与金融/量化交易的实际关联度很低，需谨慎解读。`day-trader-skill`、`QuantDinger`、`Vibe-Trading` 等直接涉及交易执行或实盘接入的项目，存在策略过拟合、API key 安全与资金风险，应仅作研究参考。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 495924 | 信息不足 | +3140 | Python | API 资源列表 | 免费 API 集合列表 | 低，与量化关联弱 | 中 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 144881 | 信息不足 | +3185 | Python | AI 技能/UI | 多平台 UI/UX 设计智能技能 | 中，Agent 前端生成 | 低 |
| 3 | JustVugg/colibri | 47411 | 信息不足 | +2988 | C | 推理引擎 | 分层 MoE 推理引擎，GPU/RAM/NVMe 混合 | 高，低成本 LLM 推理 | 低 |
| 4 | TauricResearch/TradingAgents | 120451 | 信息不足 | +2967 | Python | AI 交易/多 Agent | LLM 多智能体金融交易框架 | 高，多 Agent 交易决策 | 低 |
| 5 | ifixai-ai/iFixAi | 43267 | 信息不足 | +7152 | Python | AI 审计/风控 | AI Agent 独立审计与合规评估 | 高，Agent 治理与风控 | 低 |
| 6 | CopilotKit/OpenBot | 10064 | 信息不足 | +2617 | TypeScript | Agent 编排 | 开源 AI 协作者，自带浏览器/文件/工具 | 高，Agent 工作台 | 中 |
| 7 | codecrafters-io/build-your-own-x | 559525 | 信息不足 | +2805 | Markdown | 教程列表 | 从零复刻技术的教程集合 | 低，与量化关联弱 | 中 |
| 8 | Jakeschincariol/day-trader-skill | 5024 | 信息不足 | +2633 | Python | 交易技能/回测 | 11 个 Claude 日内交易技能 | 中，交易 Agent 技能化 | 低 |
| 9 | awesome-selfhosted/awesome-selfhosted | 333516 | 信息不足 | +2340 | 信息不足 | 自托管列表 | 自托管网络服务列表 | 低，与量化关联弱 | 中 |
| 10 | Orkas-AI/Orkas | 8993 | 信息不足 | +6402 | JavaScript | 本地 AI 团队 | 本地优先桌面 AI 团队，16 个内置 Agent | 高，本地 Agent 编排 | 低 |
| 11 | Fractal-Compute-Orchestrations/FractalWorkspace | 9267 | 信息不足 | +2683 | Python | 联邦学习 | 大规模联邦学习工作区 | 中，分布式训练 | 低 |
| 12 | shiyu-coder/Kronos | 46626 | 信息不足 | +2658 | Python | 金融基础模型 | 金融市场语言基础模型 | 高，金融 LLM 底座 | 低 |
| 13 | ripienaar/free-for-dev | 141785 | 信息不足 | +1656 | HTML | 免费资源列表 | SaaS/PaaS/IaaS 免费层列表 | 低，与量化关联弱 | 低 |
| 14 | vinta/awesome-python | 332312 | 信息不足 | +1563 | Python | Python 资源列表 | Python 工具精选列表 | 低，与量化关联弱 | 低 |
| 15 | VoltAgent/awesome-design-md | 125512 | 信息不足 | +1408 | 信息不足 | 设计系统 | 品牌设计系统 DESIGN.md 集合 | 中，Agent UI 生成 | 中 |
| 16 | nexu-io/open-design | 105821 | 信息不足 | +1363 | TypeScript | 协作设计 | 协作式 AI 设计 Agent 工作区 | 中，协作 Agent 产品 | 低 |
| 17 | avelino/awesome-go | 191968 | 信息不足 | +1233 | Go | Go 资源列表 | Go 框架与库精选列表 | 低，与量化关联弱 | 中 |
| 18 | awesome-dsh-plugin/awesome-dsh-plugin | 22297 | 信息不足 | +1113 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | 低，与量化关联弱 | 低 |
| 19 | kaankiziltug/logo-design-skill | 5929 | 信息不足 | +1080 | HTML | AI 技能/设计 | Logo 设计技能包 | 低，与量化关联弱 | 低 |
| 20 | ruvnet/ruflo | 80821 | 信息不足 | +989 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | 高，Agent 编排底座 | 低 |
| 21 | Developer-Y/cs-video-courses | 84549 | 信息不足 | +756 | 信息不足 | 课程列表 | 计算机科学视频课程列表 | 低，与量化关联弱 | 中 |
| 22 | headroomlabs-ai/headroom | 78780 | 信息不足 | +718 | Python | LLM 压缩 | LLM 前 token 压缩，降低上下文成本 | 高，金融 LLM 降本 | 低 |
| 23 | HKUDS/Vibe-Trading | 37589 | 信息不足 | +649 | Python | AI 交易 | 个人交易 Agent，多市场回测 | 高，交易 Agent 产品化 | 中 |
| 24 | shy3130/tick-stock-panel | 7000 | 信息不足 | +636 | Python | A 股量化 | 自托管 A 股策略+监控+回测工作台 | 高，A 股量化工作台 | 低 |
| 25 | jaywcjlove/awesome-mac | 117701 | 信息不足 | +488 | Swift | macOS 软件列表 | macOS 软件精选列表 | 低，与量化关联弱 | 低 |
| 26 | hesreallyhim/awesome-claude-code | 57210 | 信息不足 | +511 | Python | Claude 资源 | Claude Code 资源精选 | 中，Agent 工具链 | 低 |
| 27 | sickn33/agentic-awesome-skills | 49118 | 信息不足 | +486 | Python | AI 技能库 | 2884+ 可复用 Agent 技能库 | 中，技能生态 | 低 |
| 28 | aardappel/goose | 2962 | 信息不足 | +581 | C++ | 编程语言 | Goose 编程语言 | 低，与量化关联弱 | 低 |
| 29 | ZhuLinsen/daily_stock_analysis | 67518 | 信息不足 | +336 | Python | 股票分析 | LLM 多市场股票智能分析系统 | 高，LLM 投研流水线 | 低 |
| 30 | punkpeye/awesome-remote-mcp-servers | 2548 | 信息不足 | +456 | 信息不足 | MCP 列表 | 远程 MCP 服务器集合 | 中，MCP 生态 | 中 |
| 31 | punkpeye/awesome-mcp-servers | 97270 | 信息不足 | +314 | 信息不足 | MCP 列表 | MCP 服务器集合 | 中，MCP 生态 | 低 |
| 32 | MakazhanAlpamys/Soup | 10111 | 信息不足 | +377 | Python | LLM 微调 | 单 YAML 微调 LLM，低显存训练 | 中，本地金融 LLM | 低 |
| 33 | code-yeongyu/oh-my-openagent | 70684 | 信息不足 | +265 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中，Agent 编排 | 低 |
| 34 | openbq-org/OpenBB | 75067 | 信息不足 | +256 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高，金融数据底座 | 中 |
| 35 | PurpleDoubleD/locally-uncensored | 3222 | 信息不足 | +393 | TypeScript | 本地 AI | 本地 AI 工作室，聊天/图像/视频/编码 | 低，与量化关联弱 | 低 |
| 36 | OpenByteInc/QuantDinger | 13502 | 信息不足 | +302 | Python | AI 交易 OS | 开源 AI 交易 OS，多租户 SaaS | 高，交易系统产品化 | 中 |
| 37 | anbeime/skill | 9124 | 信息不足 | +330 | Python | 技能商店 | 技能 Skills 商店，含金融技能 | 中，金融技能包 | 低 |
| 38 | garrytan/gbrain | 31508 | 信息不足 | +226 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent Brain | 中，Agent 编排 | 低 |
| 39 | nidhinjs/prompt-master | 15475 | 信息不足 | +304 | 信息不足 | 提示词技能 | 精准提示词生成技能 | 低，与量化关联弱 | 低 |
| 40 | virattt/ai-hedge-fund | 64472 | 信息不足 | +168 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高，多 Agent 投研 | 低 |
| 41 | fffaraz/awesome-cpp | 74221 | 信息不足 | +153 | 信息不足 | C++ 资源列表 | C/C++ 库与资源精选 | 低，与量化关联弱 | 低 |
| 42 | awesomedata/awesome-public-datasets | 79943 | 信息不足 | +135 | 信息不足 | 数据集列表 | 高质量开放数据集列表 | 中，金融数据源 | 中 |
| 43 | rust-unofficial/awesome-rust | 60318 | 信息不足 | +160 | Rust | Rust 资源列表 | Rust 代码与资源精选 | 低，与量化关联弱 | 中 |
| 44 | josephmisiti/awesome-machine-learning | 74743 | 信息不足 | +67 | Python | ML 资源列表 | 机器学习框架与库精选 | 低，与量化关联弱 | 低 |
| 45 | vuejs/awesome-vue | 73490 | 信息不足 | -14 | 信息不足 | Vue 资源列表 | Vue.js 资源精选 | 低，与量化关联弱 | 低 |

## 3. 重点项目深度分析

### 3.1 ifixai-ai/iFixAi

- **项目解决什么问题**：对 AI Agent 的行为进行独立审计，回答“Agent 是否在做它应该做的事”。支持由人类或 Agent 自身运行审计，声称 120 秒内给出结论。
- **为什么最近值得关注**：7 日涨星 +7152，是本次样本中涨星最高的项目。在 AI Agent 开始进入金融、交易、企业自动化等高风险场景时，Agent 的可审计性、对齐与合规评估成为刚需。
- **技术栈/架构亮点**：Python + CLI，topics 覆盖 `agent-evaluation`、`ai-governance`、`ai-safety`、`hallucination-detection`、`prompt-injection`、`nist-ai-rmf`、`iso-42001`、`eu-ai-act`、`owasp-llm` 等，说明其审计维度不仅限于功能正确性，还涉及安全、幻觉、提示注入与监管框架映射。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。可将其审计思路引入交易 Agent 的事前/事后检查，例如：下单前校验 Agent 是否偏离授权策略、是否产生幻觉式行情解读、是否触发 prompt injection 风险。
- **可能的风险**：项目较新，审计标准与覆盖范围尚未经过大规模验证；若用于实盘交易 Agent 审计，误判或漏判可能导致合规或资金风险。

### 3.2 TauricResearch/TradingAgents

- **项目解决什么问题**：提供 LLM 多智能体金融交易框架，将交易决策拆分为多个 Agent 协作完成。
- **为什么最近值得关注**：7 日涨星 +2967，总 star 120451，是金融 LLM Agent 方向的高热度代表。Apache-2.0 许可，具备研究复现基础。
- **技术栈/架构亮点**：Python，topics 为 `agent`、`finance`、`llm`、`multiagent`、`trading`。多 Agent 分工模式可参考用于构建“分析师 Agent + 风控 Agent + 执行 Agent”的决策流水线。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其多 Agent 协作模式可作为企业级投研 Agent 的架构蓝本，但应重点借鉴其决策流程设计，而非直接用于实盘。
- **可能的风险**：标记为 `likely_research_tool`，说明定位是研究工具；LLM 交易决策存在幻觉、过拟合与不可解释性风险；缺乏实盘验证信息。

### 3.3 Orkas-AI/Orkas

- **项目解决什么问题**：本地优先的桌面 AI 团队，一个 Commander 将目标拆解为待办，协调 16 个内置专家 Agent 及 Claude Code、Codex 等外部 Agent。
- **为什么最近值得关注**：7 日涨星 +6402，总 star 8993，涨星速度极快。代表“本地优先 + 多 Agent 编排 + 桌面端”的新产品形态。
- **技术栈/架构亮点**：JavaScript，MIT 许可，topics 覆盖 `agent-orchestration`、`multi-agent`、`local-first`、`self-evolving-agents`、`task-automation`。强调本地运行、项目制、定时自动化与连接器。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其“Commander 拆解目标 + 专家 Agent 执行 + 定时自动化”的模式可直接映射到投研任务编排、定时行情监控、自动报告生成等场景。
- **可能的风险**：项目较新，维护活跃度与长期稳定性待观察；若接入交易执行，需严格隔离研究与实盘环境。

### 3.4 JustVugg/colibri

- **项目解决什么问题**：为前沿 MoE 模型提供分层推理引擎，将热专家放在 GPU、温专家放在 RAM、冷专家从 NVMe 流式加载，用 C 语言实现，可在现有硬件上运行。
- **为什么最近值得关注**：7 日涨星 +2988，总 star 47411。在金融 LLM 推理成本高企的背景下，低资源推理方案具有直接工程价值。
- **技术栈/架构亮点**：C 语言，Apache-2.0，支持 CUDA 与 Vulkan。分层专家调度思路可降低大模型部署门槛。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。若企业需要在本地或边缘环境部署金融 LLM，可参考其分层加载与调度策略，降低 GPU 依赖。
- **可能的风险**：项目较新，topics 为空，生态与文档成熟度未知；C 语言实现可能带来维护与集成成本。

### 3.5 HKUDS/Vibe-Trading

- **项目解决什么问题**：定位为“个人交易 Agent”，支持研究、Python 策略构建、回测与模拟/实盘交易，覆盖加密、股票与外汇市场。
- **为什么最近值得关注**：7 日涨星 +649，总 star 37589，来自 HKUDS，具备学术背景。topics 覆盖 `ai-agent`、`algorithmic-trading`、`backtesting`、`mcp`、`multi-agent`。
- **技术栈/架构亮点**：Python，MIT 许可，集成 MCP 与多 Agent，强调“vibe trading”与 LLM 驱动策略生成。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：可借鉴其“研究-策略-回测-交易”的一体化产品设计，以及 MCP 在交易工具链中的接入方式。
- **可能的风险**：标记为 `crypto_related` 与 `likely_research_tool`；涉及实盘交易与加密市场，存在资金风险、API key 安全风险与策略过拟合风险。

### 3.6 shy3130/tick-stock-panel

- **项目解决什么问题**：自托管、零运维的 A 股量化工作台，支持自建策略、监控、回测，LLM 驱动策略定制、个股分析与复盘，可接入第三方数据源。
- **为什么最近值得关注**：7 日涨星 +636，总 star 7000，是本次样本中少有的专注 A 股的中文量化项目，且近期有持续 push。
- **技术栈/架构亮点**：Python，MIT 许可，topics 覆盖 `duckdb`、`polars`、`fastapi`、`react`、`llm`、`backtesting`、`quant`。DuckDB + Polars 的组合适合本地量化数据分析，FastAPI + React 提供工作台界面。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其“本地数据引擎 + LLM 策略定制 + 回测 + 监控”的架构可作为 A 股量化工作台 MVP 的参考。
- **可能的风险**：个人开源项目，维护持续性存在不确定性；A 股数据源合规性与数据质量需自行验证。

### 3.7 OpenByteInc/QuantDinger

- **项目解决什么问题**：开源 AI 交易 OS，支持研究、Python 策略构建、回测、模拟/实盘交易，覆盖加密、股票、外汇，并提供多租户交易 SaaS 能力（用户管理、计费、支付、结算）。
- **为什么最近值得关注**：7 日涨星 +302，总 star 13502。其“交易系统 + SaaS 多租户”的产品化思路在开源交易项目中较为少见。
- **技术栈/架构亮点**：Python，Apache-2.0，topics 覆盖 `agent`、`backtesting`、`binance`、`mcp-server`、`saas`、`stripe`、`typesafe-ai`。集成交易所、支付与结算模块。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：可借鉴其交易系统产品化与多租户架构，但应重点研究其权限隔离、计费与结算设计。
- **可能的风险**：标记为 `crypto_related`；涉及实盘交易、交易所 API 与支付系统，存在资金安全、合规与密钥泄露风险。不建议直接运行或接入真实 API key。

### 3.8 virattt/ai-hedge-fund

- **项目解决什么问题**：模拟 AI 对冲基金团队，通过多个 Agent 协作完成投资研究与决策。
- **为什么最近值得关注**：总 star 64472，是 AI 投研 Agent 方向的经典项目，近期仍有 push。
- **技术栈/架构亮点**：Python，MIT 许可。多 Agent 模拟对冲基金团队的分工模式具有教学与原型价值。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合作为多 Agent 投研流程的教学与原型参考，但应定位为研究工具。
- **可能的风险**：标记为 `likely_research_tool`；模拟结果不代表真实收益，存在过拟合与幸存者偏差风险。

### 3.9 openbq-org/OpenBB

- **项目解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、加密、衍生品、固定收益、经济数据等。
- **为什么最近值得关注**：总 star 75067，是金融数据基础设施方向的重要开源项目，近期有 push。
- **技术栈/架构亮点**：Python，topics 覆盖 `ai`、`crypto`、`derivatives`、`equity`、`fixed-income`、`machine-learning`、`quantitative-finance`。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合作为金融数据底座，为 Agent 提供统一的数据访问接口，减少多源数据接入成本。
- **可能的风险**：标记为 `crypto_related`；数据源许可与合规性需自行评估。

### 3.10 headroomlabs-ai/headroom

- **项目解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前进行压缩，声称编码 Agent 可减少 20% token，JSON 可减少 60-95% token，同时保持答案质量。
- **为什么最近值得关注**：7 日涨星 +718，总 star 78780。金融场景中行情、新闻、日志等上下文量巨大，token 压缩具有直接降本价值。
- **技术栈/架构亮点**：Python，Apache-2.0，提供库、代理与 MCP server 三种形态，topics 覆盖 `context-engineering`、`token-optimization`、`rag`、`mcp`。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。可将其作为金融 LLM 上下文工程的一环，降低长上下文推理成本。
- **可能的风险**：压缩可能损失关键信息，金融场景需验证压缩后是否影响决策准确性。

## 4. 趋势归纳

- **技术趋势**：
  - **本地优先与低资源推理**：`colibri` 的分层 MoE 推理、`Orkas` 的本地优先桌面 Agent、`Soup` 的低显存微调，共同指向“降低 AI 部署门槛”的趋势。
  - **上下文工程与 token 优化**：`headroom` 的 LLM 前压缩表明，上下文成本控制正在成为 Agent 工程的重要环节。
  - **MCP 生态扩张**：多个项目（`Vibe-Trading`、`QuantDinger`、`headroom`、`awesome-mcp-servers`）集成或围绕 MCP 构建，MCP 正在成为 Agent 工具接入的事实标准。

- **产品趋势**：
  - **Agent 技能包 / Skills 商店**：`ui-ux-pro-max-skill`、`day-trader-skill`、`agentic-awesome-skills`、`skill` 等项目显示，可复用技能正在从代码库向“技能市场”演进，并出现金融交易垂直技能。
  - **本地优先 AI 工作台**：`Orkas`、`OpenBot`、`open-design` 等项目强调桌面端、本地运行与多 Agent 协作，反映用户对数据隐私与自主可控的需求。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 投研与交易**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund`、`Kronos` 等项目持续活跃，LLM 在金融决策中的角色从“辅助分析”向“多 Agent 协作决策”演进。
  - **A 股本地量化工作台**：`tick-stock-panel`、`daily_stock_analysis` 显示中文社区对自托管、LLM 驱动的 A 股量化工具需求上升。

- **AI Agent 与自动化交易结合趋势**：
  - **Agent 审计与治理成为新焦点**：`iFixAi` 的高涨星表明，随着 Agent 进入交易等高风险场景，可审计性、对齐与合规评估正在成为独立赛道。
  - **交易 Agent 产品化**：`QuantDinger` 的多租户 SaaS 设计显示，开源交易系统正在从单用户工具向可运营产品演进。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据与交易工具接入层。
  - 本地优先的 A 股量化工作台（DuckDB + Polars + LLM）。
  - 交易 Agent 的事前/事后审计与合规检查模块。
  - 金融 LLM 的上下文压缩与低资源推理方案。

## 5. 今日灵感清单

1. **MVP：本地优先的 A 股投研 Agent 工作台**：参考 `tick-stock-panel` 与 `Orkas`，用 DuckDB + Polars 做本地数据层，FastAPI + React 做界面，LLM 做策略生成与个股复盘，先跑通“数据接入 → 策略回测 → 报告生成”闭环。
2. **MVP：交易 Agent 审计模块**：参考 `iFixAi`，为现有交易 Agent 增加“下单前策略符合性检查 + 下单后行为审计”，输出结构化审计报告，先用于模拟盘。
3. **调研：MCP 在金融数据接入中的标准化程度**：对比 `Vibe-Trading`、`QuantDinger`、`OpenBB` 的 MCP 接入方式，评估是否可抽象出统一的金融数据 MCP 层。
4. **调研：LLM 上下文压缩对金融决策准确性的影响**：基于 `headroom` 的思路，用金融新闻、行情日志、研报片段做压缩前后对比实验，验证 token 压缩是否损害关键信息。
5. **Codex/Agent 自动复现 demo：多 Agent 投研流水线**：参考 `TradingAgents` 与 `ai-hedge-fund`，让 Codex 自动搭建“分析师 Agent + 风控 Agent + 决策 Agent”的最小可运行 demo，仅使用模拟数据。
6. **原型：低资源金融 LLM 推理**：参考 `colibri` 的分层加载思路，评估在单机 GPU 上运行金融领域 MoE 模型的可行性，输出部署方案与成本对比。
7. **MVP：金融 Agent 技能包**：参考 `day-trader-skill` 与 `skill`，将“行情扫描、新闻跟踪、入场/出场时机、结果复盘”封装为可复用的 Claude/Codex 技能包，先用于模拟交易研究。
8. **调研：交易系统多租户 SaaS 架构**：分析 `QuantDinger` 的用户管理、计费、支付、结算设计，评估开源交易系统产品化的可行性与合规边界。
9. **原型：金融数据管道 + RAG 压缩**：结合 `OpenBB` 与 `headroom`，构建“多源金融数据 → 统一接口 → 压缩 → LLM 分析”的管道，测量端到端延迟与成本。
10. **Watchlist 候选**：将 `iFixAi`、`TradingAgents`、`Orkas`、`colibri`、`tick-stock-panel`、`Vibe-Trading` 加入后续跟踪，观察其维护活跃度与功能演进。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | Agent 审计与治理赛道新热点，涨星最快，适合跟踪其审计标准与金融场景适配进展。 |
| TauricResearch/TradingAgents | LLM 多智能体交易框架代表，适合观察多 Agent 交易决策的架构演进。 |
| Orkas-AI/Orkas | 本地优先多 Agent 工作台，涨星极快，适合跟踪桌面端 Agent 编排产品形态。 |
| JustVugg/colibri | 低资源 MoE 推理引擎，对金融 LLM 本地部署有直接工程价值。 |
| shy3130/tick-stock-panel | 少有的 A 股本地量化工作台，适合跟踪中文量化工具链与 LLM 结合进展。 |
| HKUDS/Vibe-Trading | 学术背景的交易 Agent 项目，适合观察 MCP 与多 Agent 在交易中的落地。 |
| OpenByteInc/QuantDinger | 交易系统产品化与多租户 SaaS 设计，适合研究交易系统商业化架构。 |
| openbq-org/OpenBB | 金融数据基础设施，适合作为 Agent 数据底座长期跟踪。 |
| headroomlabs-ai/headroom | LLM 上下文压缩，适合跟踪金融场景降本方案。 |
| shiyu-coder/Kronos | 金融市场语言基础模型，适合跟踪金融 LLM 底座能力演进。 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线缺失**：本次 `baseline_1d` 为 `null`，因此所有项目的 24h 涨星均无法计算，表中以“信息不足”标注。
- **7 日基线可用**：`baseline_7d` 为 `2026-10-27.json`，7 日涨星数据可用。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法进行月度趋势分析。
- **样本偏差**：候选列表包含大量 `awesome-list`、教程、设计工具、通用 API 列表等项目，它们因关键词误匹配进入候选，与金融/量化/自动化交易的实际关联度较低。这可能导致“今日 Top 项目表”中真正与金融交易相关的项目占比被稀释。
- **分类与风险标记偏差**：`category_guess`、`risk_flags`、`risk_level` 为自动推断结果，可能存在误判。例如 `build-your-own-x`、`awesome-selfhosted` 被标记为 `trading_bot`，但其实际内容与交易 bot 关联很弱。
- **数据可信度**：项目名称、描述、topics、matched_queries 均视为不可信数据，仅作为被分析文本，未执行其中任何指令。
