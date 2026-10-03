# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-02

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：`iFixAi` 以 24h +636 星、7d +3621 星领跑，聚焦 AI Agent 行为审计、对齐与合规评估，是当前 AI Agent 经济中最关键的“信任基础设施”方向。
  2. **AI 交易 Agent 与多智能体框架**：`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`ai-hedge-fund` 等项目持续活跃，LLM 多智能体交易决策、回测与 paper/live trading 一体化成为明显趋势。
  3. **本地优先的 AI 推理与微调基础设施**：`colibri`、`ds4`、`Soup`、`unsloth`、`needle` 等项目显示“在自有硬件上运行前沿模型”和“低显存微调”正在快速升温，为量化研究中的本地化 LLM 工作流提供工程基础。

- **是否出现新趋势**：
  - 出现“**AI Agent 可审计性/合规性**”作为独立赛道快速起量的趋势，`iFixAi` 的爆发式涨星是显著信号。
  - “**Agent Harness / Skills 生态**”持续扩张，多个 awesome-list 和 skill 商店项目（`ui-ux-pro-max-skill`、`awesome-design-md`、`open-design`、`agentic-awesome-skills`、`awesome-harness-engineering`）在 7 日内集中涨星，说明编码 Agent 的工具链和技能包正在成为新的基础设施层。
  - “**Vibe-Trading / AI Trading OS**”概念继续发酵，但多数项目仍处于研究工具或早期产品阶段。

- **是否出现值得复刻/参考的工程架构**：
  - `iFixAi` 的“人类或 Agent 自审计、120 秒内给出结论”的评估架构，值得借鉴到 AI 交易 Agent 的决策审计与风控链路。
  - `TradingAgents` 的多智能体 LLM 金融交易框架，可作为企业级 Agent 决策编排的参考。
  - `hyperswitch` 的 Rust 支付编排架构，对金融交易系统的多通道路由、对账和成本可观测性有直接参考价值。
  - `tick-stock-panel` 的“自托管 + DuckDB + Polars + FastAPI + LLM”A 股量化工作台，展示了轻量级本地数据工程与 LLM 分析结合的可行路径。

- **是否有明显骗局、过度营销或高风险项目**：
  - 本次候选集中未发现明显骗局项目，但需注意：
    - `Financial_freedom`（“最全赚钱投资指南”）7 日涨星 +1604，但 24h 仅 +40，且无 license、无 topics，内容性质偏向投资营销，应谨慎对待。
    - 多个 `crypto_related` 和 `trading_bot` 标记项目（如 `QuantDinger`、`Vibe-Trading`、`awesome-jev`、`jev-trader`）涉及加密货币、自动交易和套利概念，存在资金与合规风险，不应直接用于实盘。
    - 大量 awesome-list 类项目因关键词命中进入候选，实际与金融/量化交易的相关性较弱，存在样本噪声。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | iFixAi | 19324 | +636 | +3621 | Python | AI 审计/风控 | AI Agent 独立审计与合规评估 | 高：Agent 决策审计架构 | 低 |
| 2 | public-apis | 485605 | +273 | +2301 | Python | API 列表 | 免费 API 集合 | 中：数据源发现 | 中 |
| 3 | ui-ux-pro-max-skill | 132608 | +210 | +1917 | Python | AI 设计技能 | 多平台 UI/UX 设计智能 | 中：Agent 前端生成 | 低 |
| 4 | awesome-python | 324784 | +207 | +1729 | Python | 资源列表 | Python 工具精选 | 低：工具发现 | 低 |
| 5 | awesome-selfhosted | 323489 | +214 | +1666 | 无 | 自托管列表 | 自托管服务精选 | 中：自托管交易基础设施 | 中 |
| 6 | build-your-own-x | 551252 | +140 | +1614 | Markdown | 教程列表 | 从零复刻技术 | 中：交易系统复刻教程 | 中 |
| 7 | colibri | 39131 | +226 | +1456 | C | 本地推理 | 纯 C 零依赖 MoE 推理引擎 | 高：本地 LLM 推理 | 低 |
| 8 | awesome-design-md | 119294 | +96 | +1324 | 无 | 设计系统 | DESIGN.md 设计系统集合 | 中：Agent UI 一致性 | 中 |
| 9 | open-design | 99213 | +105 | +1097 | TypeScript | AI 设计工具 | 本地优先 AI 设计引擎 | 中：Agent 生成原型 | 低 |
| 10 | awesome-go | 186655 | +160 | +1035 | Go | 资源列表 | Go 框架与库精选 | 中：Go 交易基础设施 | 中 |
| 11 | Financial_freedom | 5593 | +40 | +1604 | 无 | 投资指南 | 赚钱投资指南 | 低：内容营销 | 中 |
| 12 | TradingAgents | 109553 | +63 | +896 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高：Agent 决策编排 | 低 |
| 13 | hyperswitch | 45271 | -3 | +1176 | Rust | 支付/金融 | 开源可组合支付平台 | 高：支付编排与对账 | 低 |
| 14 | awesome-dsh-plugin | 17639 | +65 | +727 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | 中：Agent 插件生态 | 低 |
| 15 | Soup | 8037 | +61 | +826 | Python | LLM 微调 | 单 YAML 低显存微调 | 高：本地模型微调 | 低 |
| 16 | free-for-dev | 139094 | +46 | +553 | HTML | 资源列表 | 开发者免费资源 | 低：基础设施选型 | 低 |
| 17 | ruflo | 73745 | +66 | +454 | TypeScript | Agent 框架 | 多智能体 swarm 编排 | 高：Agent 编排框架 | 低 |
| 18 | ds4 | 22991 | +140 | +282 | C | 本地推理 | DeepSeek 本地推理引擎 | 中：本地 LLM 推理 | 低 |
| 19 | headroom | 74304 | +44 | +479 | Python | 上下文压缩 | LLM 上下文压缩 | 高：降低 Agent token 成本 | 低 |
| 20 | OpenBot | 5905 | +70 | +338 | TypeScript | AI 自动化 | 开源 AI 数字员工 | 中：浏览器自动化 Agent | 中 |
| 21 | awesome-claude-code | 54977 | +57 | +355 | Python | 资源列表 | Claude Code 资源精选 | 中：编码 Agent 工具链 | 低 |
| 22 | needle | 12989 | +57 | +346 | Python | 边缘 AI | 微型设备自动化模型 | 中：边缘推理 | 中 |
| 23 | tick-stock-panel | 5431 | +72 | +255 | Python | A 股量化 | 自托管 A 股量化工作台 | 高：本地量化数据栈 | 低 |
| 24 | atomic-agent | 2671 | +106 | +168 | TypeScript | 本地 Agent | 本地优先 AI Agent | 中：本地 Agent 架构 | 中 |
| 25 | unsloth | 77152 | +28 | +356 | Python | LLM 微调 | 本地 LLM 训练/微调 UI | 中：模型微调 | 低 |
| 26 | Vibe-Trading | 34453 | +14 | +405 | Python | AI 交易 | 个人交易 Agent | 中：交易 Agent 产品化 | 中 |
| 27 | OpenStock | 19618 | +40 | +360 | TypeScript | 行情平台 | 开源实时行情与提醒 | 中：行情产品 | 低 |
| 28 | prompt-master | 13995 | +47 | +325 | 无 | 提示工程 | Claude 提示词技能 | 低：提示工程 | 低 |
| 29 | oh-my-openagent | 69762 | +13 | +334 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中：Agent 编排 | 低 |
| 30 | awesome-jev | 2091 | +21 | +401 | Python | 资源列表 | Jev 类型化决策项目列表 | 中：类型化决策 | 中 |
| 31 | daily_stock_analysis | 65856 | +14 | +202 | Python | 股票分析 | LLM 多市场股票分析 | 中：LLM 投研自动化 | 低 |
| 32 | Kronos | 39828 | +30 | +376 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融基础模型 | 低 |
| 33 | awesome-mcp-servers | 95767 | +10 | +234 | 无 | MCP 列表 | MCP 服务器集合 | 中：Agent 工具接入 | 低 |
| 34 | jev-trader | 2749 | +15 | +321 | TypeScript | AI 交易 | Monad 区块 AI 交易决策 | 中：链上 Agent 交易 | 低 |
| 35 | skill | 7494 | +20 | +271 | Python | 技能商店 | AI Agent 技能商店 | 中：技能生态 | 低 |
| 36 | QuantDinger | 12389 | +23 | +207 | Python | AI 交易 OS | 开源 AI 交易操作系统 | 中：交易 SaaS 架构 | 中 |
| 37 | TradingView-API | 5484 | +52 | +115 | TypeScript | 行情 API | TradingView 实时行情 | 中：行情数据接入 | 中 |
| 38 | gbrain | 30499 | +11 | +162 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | 中：Agent 认知架构 | 低 |
| 39 | awesome-harness-engineering | 4676 | +35 | +148 | Python | 资源列表 | Agent harness 工程资源 | 高：Agent 工程模式 | 低 |
| 40 | redamon | 2905 | +11 | +308 | Python | AI 安全 | 自托管 AI 渗透测试框架 | 中：Agent 安全测试 | 中 |
| 41 | awesome-cpp | 73584 | +20 | +108 | 无 | 资源列表 | C/C++ 资源精选 | 低：高性能系统 | 低 |
| 42 | agentic-awesome-skills | 47202 | +34 | 无 | Python | 技能库 | Agent 技能控制平面 | 中：技能管理 | 低 |
| 43 | awesome-rust | 59657 | +18 | +100 | Rust | 资源列表 | Rust 资源精选 | 中：Rust 交易系统 | 低 |
| 44 | awesome-public-datasets | 79277 | +2 | +118 | 无 | 数据集列表 | 公开数据集精选 | 中：量化数据源 | 中 |
| 45 | OpenBB | 73768 | +28 | 无 | Python | 开放数据平台 | 分析师/量化/AI Agent 数据平台 | 高：量化数据平台 | 中 |
| 46 | awesome-machine-learning | 74512 | +8 | +59 | Python | 资源列表 | ML 资源精选 | 低：ML 工具发现 | 低 |
| 47 | ai-hedge-fund | 63835 | +3 | +85 | Python | AI 对冲基金 | AI 对冲基金团队 | 高：多 Agent 投研 | 低 |
| 48 | cs-video-courses | 83600 | +1 | +39 | 无 | 课程列表 | CS 视频课程 | 低：学习资源 | 中 |
| 49 | awesome-vue | 73538 | +1 | -6 | 无 | 资源列表 | Vue 资源精选 | 低：前端生态 | 低 |
| 50 | Janus | 100 | +49 | 无 | Go | AI 路由 | Go AI 模型 API 路由 | 中：模型路由 | 低 |
| 51 | system-design-101 | 90185 | +23 | +219 | 无 | 系统设计 | 系统设计图解 | 中：交易系统架构 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi
- **解决什么问题**：AI Agent 行为审计与合规评估，回答“Agent 是否在做它应该做的事”，可在 120 秒内给出结论。
- **为什么值得关注**：24h +636、7d +3621 的涨星速度极快，说明 AI Agent 治理需求正在爆发。在 AI 交易 Agent 场景中，决策可审计性是上线前必须解决的问题。
- **技术栈/架构亮点**：Python + Apache-2.0，覆盖 agent-evaluation、ai-governance、ai-safety、prompt-injection、hallucination-detection、NIST AI RMF、ISO 42001、EU AI Act 等主题，说明其评估维度兼顾技术安全与监管合规。
- **是否适合借鉴**：非常适合。可将其审计思路迁移到 AI 交易 Agent 的决策日志、提示注入检测、幻觉检测和合规检查链路中，作为交易前风控闸门。
- **可能风险**：项目较新，评估标准的权威性和稳定性仍需观察；不能将其审计结论直接等同于金融合规认证。

### 3.2 TradingAgents
- **解决什么问题**：用多智能体 LLM 框架模拟金融交易团队，进行基本面、技术面、情绪面等分工分析并形成交易决策。
- **为什么值得关注**：109k stars，7d +896，是 AI 交易多智能体方向的代表性项目，且近期仍有 push。
- **技术栈/架构亮点**：Python + Apache-2.0，多智能体协作、LLM 决策、金融数据分析。架构上强调角色分工与协作流程，适合研究 Agent 编排模式。
- **是否适合借鉴**：适合。可借鉴其多角色 Agent 编排、决策汇总和风险讨论机制，用于企业级投研 Agent 或交易决策支持系统。但不应直接用于实盘。
- **可能风险**：研究工具属性明显，策略有效性未经验证；LLM 决策存在幻觉和过拟合风险；回测结果可能无法反映真实市场冲击。

### 3.3 hyperswitch
- **解决什么问题**：开源可组合支付平台，支持多支付、多 payout、欺诈、vault 和 tokenization 提供商连接，提供智能路由、收入恢复、成本可观测性和对账能力。
- **为什么值得关注**：7d +1176，Rust 实现，是金融交易系统中支付与结算环节的成熟工程参考。
- **技术栈/架构亮点**：Rust + Apache-2.0，PCI 合规，SaaS 与自托管双模式。其多通道编排、智能路由和对账架构对交易系统的资金链路设计有直接参考价值。
- **是否适合借鉴**：适合。若构建涉及资金结算、多交易所资金路由或支付对账的交易系统，可参考其模块化 provider 抽象和可观测性设计。
- **可能风险**：项目本身是支付基础设施，与量化交易无直接关系；引入 PCI 合规复杂度较高。

### 3.4 tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析和复盘。
- **为什么值得关注**：24h +72，虽然总 star 仅 5431，但其技术栈组合非常务实：DuckDB + Polars + FastAPI + React + LLM，展示了轻量级本地量化数据栈的可行路径。
- **技术栈/架构亮点**：Python + MIT，自托管、第三方数据源接入、个性化扩展。DuckDB 做本地分析、Polars 做数据处理、FastAPI 做服务层，架构清晰且低运维。
- **是否适合借鉴**：非常适合。可作为“本地优先量化研究平台”的 MVP 参考，尤其适合不想依赖重型数据库和云服务的个人或小团队。
- **可能风险**：A 股数据源合规与稳定性需自行验证；LLM 生成的策略存在过拟合风险；项目个人开源，长期维护活跃度不确定。

### 3.5 colibri
- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，纯 C 实现、零依赖、专家从磁盘流式加载。
- **为什么值得关注**：24h +226、7d +1456，显示本地推理需求旺盛。对量化研究而言，本地运行 LLM 可避免数据外泄和 API 成本。
- **技术栈/架构亮点**：C + Apache-2.0，零依赖、磁盘流式加载专家，架构极简。对资源受限环境下的模型推理有工程参考价值。
- **是否适合借鉴**：适合。若需要在本地或边缘环境部署 LLM 进行金融文本分析、研报解读或策略生成，可调研其流式加载和内存管理思路。
- **可能风险**：项目较新，模型兼容性和稳定性需验证；纯 C 实现可能牺牲部分生态兼容性。

### 3.6 QuantDinger
- **解决什么问题**：开源 AI Trading OS，支持 agent trading、vibe trading、策略研究、回测、paper/live 交易，并可启动多租户交易 SaaS。
- **为什么值得关注**：覆盖 crypto、stocks、forex，集成 Jev System One，是“AI 交易操作系统”产品化方向的代表。
- **技术栈/架构亮点**：Python + Apache-2.0，内置用户管理、计费、支付和结算，说明其架构目标是可运营的 SaaS 而不仅是研究工具。
- **是否适合借鉴**：可借鉴其“研究-回测-模拟-实盘”一体化产品架构和多租户 SaaS 设计。但不应直接运行或接入真实交易所 API。
- **可能风险**：涉及 crypto 和自动交易，资金风险高；多市场实盘对接存在合规风险；项目较新，策略质量和安全审计未知。

### 3.7 ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，由多个 Agent 扮演不同角色进行投资分析和决策。
- **为什么值得关注**：63k stars，是 AI 多智能体投研的经典参考项目，近期仍有 push。
- **技术栈/架构亮点**：Python + MIT，多 Agent 角色分工，强调研究流程而非实盘执行。
- **是否适合借鉴**：适合作为多 Agent 投研工作流的教学和原型参考，可复现其角色分工和决策汇总逻辑。
- **可能风险**：研究工具属性，策略未经验证；回测存在幸存者偏差和过拟合风险；不应视为收益信号。

### 3.8 Kronos
- **解决什么问题**：金融市场语言基础模型，试图用 foundation model 方式建模金融时间序列和市场语言。
- **为什么值得关注**：39k stars，7d +376，是金融基础模型方向的重要探索。
- **技术栈/架构亮点**：Python + MIT，但 topics 为空，且最近 push 在 2026-04-13，维护活跃度存疑。
- **是否适合借鉴**：可调研其模型架构和训练思路，作为金融时序基础模型的研究方向参考。
- **可能风险**：金融基础模型的可解释性和泛化性存疑；项目近期维护不活跃；模型输出不应直接用于交易决策。

### 3.9 OpenBB
- **解决什么问题**：面向分析师、量化研究员和 AI Agent 的开放数据平台，覆盖股票、衍生品、加密、固定收益、经济数据等。
- **为什么值得关注**：73k stars，是量化数据接入层的重要开源项目，近期仍有 push。
- **技术栈/架构亮点**：Python，统一数据接口，支持 AI Agent 接入。对构建量化数据中台有直接参考价值。
- **是否适合借鉴**：适合。可调研其数据 provider 抽象和标准化接口设计，用于自建量化数据层。
- **可能风险**：数据源合规性和延迟需自行验证；部分数据源可能需要付费或授权。

### 3.10 headroom
- **解决什么问题**：在 LLM 接收前压缩工具输出、日志、文件和 RAG 块，降低 token 消耗，同时保持答案质量。
- **为什么值得关注**：74k stars，7d +479，对 AI Agent 运行成本优化有直接价值。
- **技术栈/架构亮点**：Python + Apache-2.0，提供库、代理和 MCP server 三种形态，支持 JSON 60-95% token 压缩。
- **是否适合借鉴**：非常适合。在 AI 交易 Agent 处理大量行情、订单簿和日志数据时，可显著降低上下文成本。
- **可能风险**：压缩可能丢失关键信息，需在交易场景中谨慎验证；过度压缩可能影响决策准确性。

## 4. 趋势归纳

### 技术趋势
- **本地优先 AI 推理**：`colibri`、`ds4`、`needle`、`atomic-agent` 等项目显示，在自有硬件上运行 LLM 成为明确趋势，驱动因素是数据隐私、成本和低延迟。
- **低显存微调与本地训练**：`Soup`、`unsloth` 等项目让个人开发者能在消费级 GPU 上微调模型，为垂直领域（如金融文本、研报）定制模型提供可能。
- **Agent Harness 与 Skills 生态**：大量项目围绕 Claude Code、Codex、DeepSeek Harness 构建技能包和插件生态，Agent 工程正在形成标准化工具链。
- **上下文工程与 token 优化**：`headroom` 等项目聚焦上下文压缩，反映 Agent 规模化部署中的成本压力。

### 产品趋势
- **AI Agent 治理产品化**：`iFixAi` 的爆发说明“Agent 审计与合规”正在从概念走向产品。
- **AI Trading OS / Vibe Trading**：`QuantDinger`、`Vibe-Trading` 等项目试图将 AI 交易从研究工具升级为可运营产品，但成熟度普遍不足。
- **开源金融基础设施**：`hyperswitch`、`OpenBB` 等项目显示支付、数据等金融基础设施的开源化趋势。

### 量化/交易策略趋势
- **多智能体 LLM 决策**：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 等项目共同指向“用多 Agent 模拟投研团队”的策略研究范式。
- **金融基础模型**：`Kronos` 代表用 foundation model 建模金融市场的探索方向。
- **本地量化数据栈**：`tick-stock-panel` 展示 DuckDB + Polars 的轻量级本地量化工作流。

### AI Agent 与自动化交易结合趋势
- **决策可审计性成为前置条件**：AI 交易 Agent 的合规与审计需求正在上升。
- **链上 Agent 交易**：`jev-trader`、`awesome-jev` 显示 AI Agent 与区块链交易结合的新方向，但风险极高。
- **Agent 工具标准化**：MCP 成为 Agent 接入外部工具和数据的主流协议。

### 值得后续做原型验证的方向
- 本地优先的 LLM 量化研究平台（参考 `tick-stock-panel` + `colibri`）。
- AI 交易 Agent 决策审计与风控闸门（参考 `iFixAi`）。
- 多智能体投研工作流的可复现 demo（参考 `TradingAgents`、`ai-hedge-fund`）。
- 量化数据中台与 AI Agent 数据接入层（参考 `OpenBB`）。

## 5. 今日灵感清单

1. **MVP：AI 交易 Agent 决策审计面板**：参考 `iFixAi` 的审计思路，构建一个轻量级面板，记录 AI 交易 Agent 的每一次决策输入、输出、提示注入检测和幻觉标记，作为交易前风控闸门。
2. **MVP：本地优先量化研究工作台**：参考 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + 本地 LLM 搭建一个零运维的股票筛选、监控和回测工作台，数据不出本地。
3. **调研：Agent Harness 工程模式**：深入 `awesome-harness-engineering` 和 `ruflo`，梳理 Agent 编排、记忆、权限、可观测性的最佳实践，形成内部 Agent 框架选型报告。
4. **调研：本地 LLM 推理引擎**：对比 `colibri`、`ds4`、`needle` 的架构和性能，评估在量化研究环境中本地部署 LLM 的可行性。
5. **Codex/Agent 自动复现 demo：多智能体投研流程**：让 Codex 复现 `ai-hedge-fund` 或 `TradingAgents` 的多角色投研流程，但仅使用模拟数据，不接入真实交易。
6. **MVP：LLM 上下文压缩代理**：参考 `headroom`，为 AI 交易 Agent 构建一个上下文压缩代理，降低处理大量行情和日志数据时的 token 成本。
7. **调研：支付编排与对账架构**：研究 `hyperswitch` 的多通道路由和对账设计，评估在交易系统资金链路中的借鉴价值。
8. **Watchlist：金融基础模型**：跟踪 `Kronos` 的后续进展，评估金融时序基础模型在策略研究中的潜在应用。
9. **MVP：Agent 技能商店**：参考 `skill` 和 `agentic-awesome-skills`，构建内部金融领域的 Agent 技能包，封装研报解读、财务分析、风险提示等能力。
10. **调研：MCP 在量化数据接入中的应用**：研究 `awesome-mcp-servers` 中与金融数据相关的 MCP server，评估用 MCP 标准化量化数据接入的可行性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计与合规赛道爆发，架构思路可直接迁移到交易 Agent 风控 |
| TradingAgents | 多智能体 LLM 交易框架代表，持续活跃，适合研究 Agent 编排 |
| tick-stock-panel | 轻量级本地量化工作台，技术栈务实，适合 MVP 参考 |
| colibri | 本地 MoE 推理引擎，涨星快，适合跟踪本地 LLM 推理进展 |
| hyperswitch | Rust 支付编排架构，对交易系统资金链路有参考价值 |
| QuantDinger | AI Trading OS 产品化方向，观察其 SaaS 架构和策略研究流程 |
| Kronos | 金融基础模型探索，关注其后续模型发布和研究进展 |
| OpenBB | 量化数据平台，适合作为数据接入层参考 |
| headroom | LLM 上下文压缩，对 Agent 成本优化有直接价值 |
| ai-hedge-fund | 多 Agent 投研经典项目，适合教学和原型复现 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-10-01.json`，1 日涨星数据基本完整。
- **7 日基线**：已提供 `baseline_7d: 2026-09-25.json`，但部分项目（如 `agentic-awesome-skills`、`OpenBB`、`Janus`）的 `star_delta_7d` 为 null，可能因项目创建时间晚于 7 日基线或基线数据缺失导致。
- **30 日涨星**：所有项目的 `star_delta_30d` 均为 null，本次报告无法提供 30 日趋势分析。
- **样本偏差**：候选集通过关键词匹配生成，包含大量 awesome-list 类通用项目（如 `awesome-python`、`awesome-go`、`awesome-vue`、`cs-video-courses`），这些项目因 readme 或 topics 中命中“quant”“trading”等关键词而进入候选，实际与金融/量化交易的相关性较弱，可能稀释真正交易相关项目的信号。
- **分类噪声**：部分项目的 `category_guess` 与实际情况存在偏差，例如 `public-apis` 被标记为 crypto_trading/quant_research，但实际是通用 API 列表；`ui-ux-pro-max-skill` 被标记为 fintech_product，但实际是 UI 设计技能。分析时已尽量基于项目实际内容判断。
- **采集失败**：本次数据中未发现明确的采集失败标记，但 `star_delta_7d` 的 null 值提示部分基线对比可能缺失。
