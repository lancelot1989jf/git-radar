# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-07

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：`iFixAi` 以 24h +725 星、7d +4698 星位居榜首，反映 AI Agent 经济中“如何验证 Agent 是否在做该做的事”正成为刚需。对金融/交易 Agent 尤其重要。
  2. **本地优先的 AI 推理与微调基础设施**：`colibri`（纯 C 流式 MoE 推理）、`ds4`（Metal/CUDA/ROCm 本地推理）、`Soup`（低显存微调）等持续走热，说明“在自有硬件上跑前沿模型”正在成为量化研究的基础能力。
  3. **AI 交易 Agent 与研究工作台**：`TradingAgents`、`Vibe-Trading`、`Kronos`、`tick-stock-panel`、`daily_stock_analysis` 等项目保持稳定涨星，多智能体 LLM 金融交易框架与 A 股 LLM 投研工作台是持续热点。

- **是否出现新趋势**：出现“AI Agent 可审计性/对齐/治理”与“本地推理引擎”两条明显上升曲线。`iFixAi` 的爆发式涨星尤其值得注意，说明市场从“能跑 Agent”转向“能证明 Agent 可靠”。

- **是否出现值得复刻/参考的工程架构**：
  - `iFixAi` 的“120 秒内审计 Agent 行为”定位，可复刻为交易 Agent 的 pre-trade/post-trade 校验层。
  - `colibri` 的“纯 C、零依赖、专家从磁盘流式加载”思路，对低延迟本地推理有参考价值。
  - `headroom` 的“LLM 前 token 压缩”可作为高频行情/日志喂给 LLM 时的成本优化组件。
  - `tick-stock-panel` 的 DuckDB + Polars + FastAPI + React 组合，是轻量自托管量化工作台的典型范式。

- **是否有明显骗局、过度营销或高风险项目**：
  - `Financial_freedom`（“最全赚钱投资指南”）属于典型“赚钱教程”类内容，风险标记为 crypto_related，应视为营销/内容聚合而非工程参考。
  - `QuantDinger` 描述包含“launch your own multi-tenant trading SaaS with billing/payments/settlement”，营销色彩较强，且涉及 crypto、forex、live trading，需谨慎。
  - 多个 awesome-list 类项目因关键词误匹配进入候选（如 `awesome-selfhosted`、`build-your-own-x`、`awesome-vue`），并非真正金融/交易项目，需过滤。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | iFixAi | 22435 | +725 | +4698 | Python | AI 治理/风控 | AI Agent 独立审计，120 秒内回答“Agent 是否在做该做的事” | 高：交易 Agent 审计层 | 低 |
| 2 | public-apis | 486836 | +234 | +1950 | Python | API 聚合 | 免费 API 集合列表 | 中：数据源发现 | 中 |
| 3 | ui-ux-pro-max-skill | 133901 | +238 | +1805 | Python | AI 设计技能 | 多平台 UI/UX 设计智能技能 | 中：交易面板 UI 生成 | 低 |
| 4 | awesome-selfhosted | 324732 | +276 | +1700 | 无 | 自托管列表 | 可自托管网络服务列表 | 低：误匹配 | 中 |
| 5 | colibri | 40387 | +280 | +1678 | C | 本地推理 | 纯 C 流式 MoE 推理引擎，零依赖 | 高：低延迟本地推理 | 低 |
| 6 | awesome-python | 325966 | +249 | +1561 | Python | 资源列表 | Python 工具精选列表 | 低：误匹配 | 低 |
| 7 | awesome-go | 187449 | +158 | +1105 | Go | 资源列表 | Go 框架/库精选列表 | 低：误匹配 | 中 |
| 8 | build-your-own-x | 552096 | +170 | +1160 | Markdown | 教程列表 | 从零复刻技术教程集合 | 中：复刻交易系统教学 | 中 |
| 9 | awesome-design-md | 119981 | +136 | +970 | 无 | 设计系统 | DESIGN.md 品牌设计系统集合 | 中：Agent 生成 UI | 中 |
| 10 | open-design | 99918 | +158 | +948 | TypeScript | AI 设计 | 本地优先 AI 设计引擎，导出 HTML/PDF/PPTX/MP4 | 中：交易报告可视化 | 低 |
| 11 | TradingAgents | 110181 | +156 | +777 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高：多 Agent 投研架构 | 低 |
| 12 | ds4 | 23678 | +49 | +861 | C | 本地推理 | DeepSeek 4 Flash/PRO 本地推理引擎 | 中：本地模型推理 | 低 |
| 13 | awesome-dsh-plugin | 18032 | +88 | +550 | JavaScript | 插件列表 | DeepSeek Harness 插件精选 | 低：误匹配 | 低 |
| 14 | Vibe-Trading | 34962 | +70 | +564 | Python | AI 交易/回测 | “Vibe-Trading”个人交易 Agent | 高：LLM 交易 Agent 范式 | 中 |
| 15 | headroom | 74631 | +95 | +428 | Python | LLM 上下文压缩 | 工具输出/日志/RAG 压缩，省 20-95% token | 高：LLM 成本优化 | 低 |
| 16 | ruflo | 74097 | +77 | +503 | TypeScript | Agent 框架 | 多玩家 swarm、自适应记忆、联邦 RAG | 中：Agent 编排 | 低 |
| 17 | Kronos | 40262 | +164 | +548 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融 LLM 研究方向 | 低 |
| 18 | unsloth | 77418 | +131 | +315 | Python | LLM 微调 | 本地 LLM 训练/微调 UI | 中：金融模型微调 | 低 |
| 19 | free-for-dev | 139372 | +67 | +372 | HTML | 资源列表 | SaaS/PaaS/IaaS 免费层列表 | 低：误匹配 | 低 |
| 20 | atomic-agent | 3026 | +83 | +460 | TypeScript | 本地 Agent | 本地优先 AI Agent，llama.cpp 跑开源模型 | 中：本地交易 Agent | 中 |
| 21 | needle | 13407 | +38 | +504 | Python | 端侧模型 | 2-bit、8-29MB 端侧自动化基础模型 | 中：端侧工具调用 | 中 |
| 22 | OpenStock | 19869 | +69 | +347 | TypeScript | 行情产品 | 开源实时行情/警报/公司洞察平台 | 中：行情产品架构 | 低 |
| 23 | Soup | 8338 | +46 | +465 | Python | LLM 微调 | 一个 YAML 微调 LLM，4GB 显存训 8B | 中：低资源微调 | 低 |
| 24 | Financial_freedom | 5980 | +62 | +570 | 无 | 投资指南 | “最全赚钱投资指南” | 低：营销内容 | 中 |
| 25 | awesome-claude-code | 55225 | +50 | +355 | Python | Agent 资源 | Claude Code 资源精选 | 低：误匹配 | 低 |
| 26 | OpenBot | 6185 | +44 | +411 | TypeScript | Agent 治理 | 开源 AI 协作者，每个 Agent 独立电脑环境 | 中：Agent 沙箱/审计 | 中 |
| 27 | gbrain | 30669 | +62 | +203 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent 大脑 | 中：Agent 编排 | 低 |
| 28 | tick-stock-panel | 5700 | +43 | +351 | Python | A 股量化工作台 | 自托管 A 股选股+监控+回测，LLM 驱动 | 高：轻量量化工作台 | 低 |
| 29 | daily_stock_analysis | 66021 | +41 | +205 | Python | A 股投研 | LLM 多市场股票分析，零成本定时运行 | 高：LLM 投研流水线 | 低 |
| 30 | agentic-awesome-skills | 47344 | +39 | +210 | Python | Agent 技能库 | 2400+ agentic skills 控制平面 | 中：技能目录 | 低 |
| 31 | OpenBB | 73958 | +31 | +250 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高：数据层参考 | 中 |
| 32 | oh-my-openagent | 69887 | +35 | +185 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 低：误匹配 | 低 |
| 33 | logo-design-skill | 2308 | +116 | 无 | HTML | 设计技能 | Logo 设计 Agent 技能 | 低：误匹配 | 低 |
| 34 | awesome-mcp-servers | 95916 | +29 | +185 | 无 | MCP 列表 | MCP server 集合 | 中：MCP 生态 | 低 |
| 35 | locally-uncensored | 2027 | +70 | +169 | TypeScript | 本地 AI 工作室 | 本地聊天/图像/视频/编码 Agent | 低：误匹配 | 低 |
| 36 | prompt-master | 14168 | +46 | +257 | 无 | 提示工程 | 精准提示词生成技能 | 低：误匹配 | 低 |
| 37 | QuantDinger | 12544 | +34 | +196 | Python | AI 交易 OS | 开源 AI 交易 OS，多租户交易 SaaS | 中：交易 SaaS 架构 | 中 |
| 38 | awesome-public-datasets | 79376 | +31 | +116 | 无 | 数据集列表 | 高质量开放数据集列表 | 中：数据源发现 | 中 |
| 39 | skill | 7649 | +35 | +207 | Python | 技能商店 | AI Agent 技能商店，自动抓取 GitHub 技能 | 低：误匹配 | 低 |
| 40 | awesome-cpp | 73678 | +19 | +122 | 无 | 资源列表 | C/C++ 库精选 | 低：误匹配 | 低 |
| 41 | easy-stock | 1353 | +27 | +242 | Go | A 股投研 | A 股行情分析与 AI 投研桌面工作台 | 中：Go+Electron 投研 | 低 |
| 42 | awesome-jev | 2215 | +25 | +178 | Python | Jev 生态 | Jev 类型化决策模型项目列表 | 中：类型化决策 | 中 |
| 43 | ai-hedge-fund | 63901 | +20 | +87 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高：多 Agent 投研 | 低 |
| 44 | awesome-rust | 59710 | +11 | +87 | Rust | 资源列表 | Rust 代码/资源精选 | 低：误匹配 | 低 |
| 45 | awesome-machine-learning | 74543 | +11 | +36 | Python | 资源列表 | ML 框架/库精选 | 低：误匹配 | 低 |
| 46 | cs-video-courses | 83640 | +7 | +50 | 无 | 课程列表 | CS 视频课程列表 | 低：误匹配 | 中 |
| 47 | anti-gambling-trader-tw | 898 | +195 | 无 | Python | 反诈/交易统计 | 投资反诈、交易统计与自动化交易工具 | 高：反诈/幸存者偏差 | 中 |
| 48 | awesome-vue | 73525 | -5 | -14 | 无 | 资源列表 | Vue 资源精选 | 低：误匹配 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi（AI Agent 审计）

- **解决什么问题**：AI Agent 经济中最关键的问题——“Agent 是否在做它该做的事”。支持人工或 Agent 自审计，120 秒内给出答案。
- **为什么值得关注**：24h +725 星、7d +4698 星，是本期涨星最猛的项目。AI Agent 治理、对齐、安全、合规（EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM）等 topic 高度集中。
- **技术栈/架构亮点**：Python + CLI，Apache-2.0。覆盖 prompt injection、幻觉检测、LLM 安全、风险评级等评估维度。
- **是否适合借鉴到 AI/自动化交易**：非常适合。可将其审计思路复刻为交易 Agent 的 pre-trade 校验层（策略是否符合授权范围、是否触碰风控红线、输出是否幻觉）和 post-trade 复盘层。
- **可能风险**：项目本身风险低，但若直接用于实时交易决策审计，需注意审计规则本身可能被 prompt injection 绕过；审计结论不应替代人工风控。

### 3.2 colibri（本地 MoE 推理引擎）

- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，纯 C、零依赖、专家从磁盘流式加载。
- **为什么值得关注**：24h +280 星、7d +1678 星。对量化研究而言，本地推理意味着策略数据不出域、延迟可控、成本可预测。
- **技术栈/架构亮点**：C 语言，Apache-2.0。核心思路是“小引擎 + 大模型”，专家流式加载降低内存占用。
- **是否适合借鉴**：适合作为本地金融 LLM 推理底座的原型参考，尤其是对数据合规要求高的场景。
- **可能风险**：项目较新（2026-07 创建），open issues 80，生态和稳定性待观察；纯 C 实现可能牺牲易用性。

### 3.3 TradingAgents（多智能体 LLM 交易框架）

- **解决什么问题**：用多智能体 LLM 框架做金融交易决策，模拟投研团队分工。
- **为什么值得关注**：110k stars，7d +777，是 AI 交易领域标杆项目之一。Apache-2.0，Python。
- **技术栈/架构亮点**：多 Agent 协作（agent、multiagent、llm、finance、trading），研究工具属性明确。
- **是否适合借鉴**：适合借鉴其多 Agent 角色分工（如基本面分析、情绪分析、风险评估、交易决策）的编排模式，用于企业级投研 Agent 框架。
- **可能风险**：研究工具属性强，回测结果可能过拟合；LLM 决策存在幻觉风险；不应直接用于实盘。

### 3.4 Vibe-Trading（个人交易 Agent）

- **解决什么问题**：定位“Vibe-Trading: Your Personal Trading Agent”，将 LLM、MCP、多 Agent 与算法交易结合。
- **为什么值得关注**：HKUDS 出品，34.9k stars，7d +564。topic 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent、quantitative-finance。
- **技术栈/架构亮点**：Python + MCP + 多 Agent，强调“vibe trading”这种低门槛、对话式交易体验。
- **是否适合借鉴**：适合研究“对话式交易 Agent”的产品交互与 MCP 工具接入模式。
- **可能风险**：crypto_related，风险等级中。“vibe trading”概念本身容易诱导非理性交易；不建议直接实盘。

### 3.5 Kronos（金融市场基础模型）

- **解决什么问题**：构建“金融市场语言”的基础模型，属于金融 LLM 研究方向。
- **为什么值得关注**：40.2k stars，24h +164。虽然近 30 天无 push（pushed_at 2026-04-13），但涨星仍活跃，说明研究社区持续关注。
- **技术栈/架构亮点**：Python，MIT。定位为金融领域 foundation model。
- **是否适合借鉴**：适合作为金融 LLM 预训练/微调的研究方向参考，关注其数据构建、评估方法。
- **可能风险**：维护活跃度下降（近 6 个月无 push）；金融基础模型存在数据时效性、幻觉、合规等固有问题。

### 3.6 headroom（LLM 上下文压缩）

- **解决什么问题**：在工具输出、日志、文件、RAG chunk 进入 LLM 前压缩，编码 Agent 省 20% token，JSON 省 60-95% token。
- **为什么值得关注**：74.6k stars，7d +428。对金融场景中“把大量行情/日志/研报喂给 LLM”的成本优化极具价值。
- **技术栈/架构亮点**：Python，Apache-2.0。提供 library、proxy、MCP server 三种形态，支持 FastAPI、LangChain、MCP。
- **是否适合借鉴**：非常适合。可作为交易 Agent 的上下文工程中间层，降低 LLM 推理成本、提升上下文利用率。
- **可能风险**：压缩可能丢失关键信息，金融场景需验证压缩后决策质量不下降。

### 3.7 tick-stock-panel（A 股量化工作台）

- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，LLM 驱动策略定制、个股分析、复盘。
- **为什么值得关注**：5.7k stars，7d +351。技术栈清晰：DuckDB + Polars + FastAPI + React + LLM。
- **技术栈/架构亮点**：Python，MIT。强调“自由接入第三方数据源与个性化扩展数据”，个人开源。
- **是否适合借鉴**：非常适合作为轻量级自托管量化工作台的 MVP 参考，尤其是 DuckDB + Polars 的本地数据处理组合。
- **可能风险**：A 股数据合规与数据源稳定性；个人项目维护持续性；回测过拟合风险。

### 3.8 daily_stock_analysis（LLM 多市场投研）

- **解决什么问题**：LLM 驱动的多市场股票智能分析，多源行情、实时新闻、决策看板、自动推送，支持零成本定时运行。
- **为什么值得关注**：66k stars，forks 高达 55k，说明被大量二次开发。topic 覆盖 a-stock、ai-agent、llm、quant。
- **技术栈/架构亮点**：Python，MIT。强调“零成本定时运行”，适合个人/小团队自动化投研。
- **是否适合借鉴**：适合借鉴其“定时运行 + 多源数据 + LLM 决策看板 + 自动推送”的投研流水线模式。
- **可能风险**：LLM 生成的“决策”不可作为投资依据；新闻数据源时效性和版权需注意。

### 3.9 ai-hedge-fund（AI 对冲基金团队）

- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作做投资决策。
- **为什么值得关注**：63.9k stars，是 AI 交易领域经典项目。虽然 7d 仅 +87，但仍是重要参考。
- **技术栈/架构亮点**：Python，MIT。多 Agent 角色模拟（如分析师、研究员、交易员、风控）。
- **是否适合借鉴**：适合借鉴其 Agent 角色分工与决策流程，用于企业级投研 Agent 框架设计。
- **可能风险**：研究/教育属性强，回测结果不代表实盘；LLM 决策存在幻觉和过拟合风险。

### 3.10 anti-gambling-trader-tw（投资反诈与交易统计）

- **解决什么问题**：投资反诈、交易统计与自动化交易工具，预设 PaperBroker，提供 14 种券商/交易所选项，交易记录分析在本机执行。
- **为什么值得关注**：24h +195 星（基数小但增速快），topic 包含 anti-fraud、anti-gambling、scam-detection、survivorship-bias，定位独特。
- **技术栈/架构亮点**：Python，MIT。强调 paper trading、本机分析、反诈、幸存者偏差检测。
- **是否适合借鉴**：非常适合借鉴其“反诈 + 交易统计 + 幸存者偏差检测”思路，可作为交易风控与投资者保护工具的参考。
- **可能风险**：项目较新、stars 基数小；涉及 crypto 和 broker API，需注意 API key 安全；不建议直接实盘。

## 4. 趋势归纳

- **技术趋势**：
  - **本地优先 AI 推理**：colibri、ds4、Soup、unsloth、needle 等项目共同指向“在自有硬件上跑模型、做微调”的趋势。对金融场景意味着数据不出域、成本可控、延迟可预测。
  - **LLM 上下文工程**：headroom 等 token 压缩工具兴起，说明上下文窗口管理和成本优化正成为 Agent 工程的核心环节。
  - **轻量数据栈**：tick-stock-panel 的 DuckDB + Polars + FastAPI 组合，反映量化工作台从重型数据库向嵌入式分析栈演进。

- **产品趋势**：
  - **AI Agent 治理与审计产品化**：iFixAi 的爆发说明“Agent 可审计性”正从研究话题变成产品需求。
  - **对话式/vibe trading**：Vibe-Trading、QuantDinger 等项目推动交易从专业工具向对话式 Agent 体验演进。
  - **自托管投研工作台**：tick-stock-panel、daily_stock_analysis、easy-stock 等 A 股项目反映个人/小团队自托管投研需求旺盛。

- **量化/交易策略趋势**：
  - **多智能体 LLM 投研**：TradingAgents、ai-hedge-fund、Vibe-Trading 持续走热，多 Agent 分工协作成为主流范式。
  - **金融基础模型**：Kronos 等项目探索金融领域 foundation model，但维护活跃度需关注。
  - **反诈与幸存者偏差意识**：anti-gambling-trader-tw 的出现说明社区开始重视策略过拟合、幸存者偏差和投资反诈。

- **AI Agent 与自动化交易结合趋势**：
  - **MCP 成为标准工具接入层**：Vibe-Trading、headroom、OpenBot、awesome-mcp-servers 等项目均涉及 MCP，说明 MCP 正成为 Agent 连接数据源和交易工具的通用协议。
  - **Agent 沙箱与审计**：OpenBot（每个 Agent 独立电脑环境）、iFixAi（Agent 审计）反映“Agent 行为可控”成为自动化交易的前提。
  - **本地 Agent**：atomic-agent、locally-uncensored 等项目强调 local-first，与金融数据合规需求契合。

- **值得后续做原型验证的方向**：
  1. 交易 Agent 的 pre-trade 审计层（借鉴 iFixAi）。
  2. LLM 投研流水线的 token 压缩中间层（借鉴 headroom）。
  3. 基于 DuckDB + Polars 的轻量自托管回测工作台（借鉴 tick-stock-panel）。
  4. 多 Agent 投研角色编排框架（借鉴 TradingAgents / ai-hedge-fund）。
  5. 本地金融 LLM 推理底座（借鉴 colibri / ds4）。

## 5. 今日灵感清单

1. **MVP：交易 Agent 审计网关**。借鉴 iFixAi，做一个 pre-trade 校验层：在交易 Agent 下单前，用规则 + LLM 双重校验订单是否符合策略授权范围、风控红线、仓位限制，输出 pass/block/review 三态。可先做 paper trading 场景。

2. **MVP：LLM 投研 token 压缩代理**。借鉴 headroom，做一个 FastAPI 代理，把行情 JSON、新闻流、研报 PDF 在进入 LLM 前压缩，对比压缩前后投研结论一致性。可量化 token 节省比例和决策质量损失。

3. **调研：MCP 在交易数据接入中的标准化程度**。调研 awesome-mcp-servers 中金融相关 MCP server 的覆盖度、维护活跃度、安全风险，评估是否值得在企业 Agent 框架中引入 MCP 作为统一数据接入层。

4. **Demo：DuckDB + Polars 轻量回测工作台**。借鉴 tick-stock-panel，用 DuckDB 存日线/分钟线，Polars 做因子计算，FastAPI 暴露回测接口，React 做看板。目标是单机零运维跑通“选股 + 回测 + 监控”。

5. **Demo：多 Agent 投研角色编排**。借鉴 TradingAgents / ai-hedge-fund，用 Codex/Claude Code 自动生成一个最小多 Agent 投研框架：基本面 Agent、情绪 Agent、风控 Agent、决策 Agent，输出结构化投研报告。

6. **调研：本地金融 LLM 推理底座**。调研 colibri、ds4 在金融文本任务（情感分析、事件抽取、研报摘要）上的推理速度、显存占用、输出质量，评估是否可作为合规要求高的本地投研推理层。

7. **原型：Agent 行为审计日志**。借鉴 iFixAi + OpenBot，为交易 Agent 设计结构化审计日志：记录每次工具调用、输入输出摘要、决策依据、风控检查结果，支持事后回溯和合规审查。

8. **Watchlist：anti-gambling-trader-tw**。关注其反诈、幸存者偏差检测、交易统计功能的实现方式，评估是否可将“幸存者偏差检测”模块复用到自有回测框架中。

9. **调研：金融基础模型 Kronos 的评估方法**。调研 Kronos 如何评估“金融市场语言”建模能力，其数据构建和评估基准是否可复用到自有金融 LLM 微调项目中。

10. **原型：零成本定时投研推送**。借鉴 daily_stock_analysis，用 GitHub Actions 定时触发 + 免费数据源 + LLM 生成每日投研摘要 + 推送通知，验证“零成本自动化投研”的可行性和数据源稳定性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计/治理赛道爆发，对交易 Agent 风控有直接借鉴价值 |
| TradingAgents | 多智能体 LLM 交易框架标杆，持续活跃 |
| Vibe-Trading | HKUDS 出品，MCP + 多 Agent 交易范式，关注其演进 |
| Kronos | 金融基础模型方向，关注其评估方法和后续维护 |
| headroom | LLM 上下文压缩对金融场景成本优化价值高 |
| tick-stock-panel | 轻量自托管量化工作台范式，技术栈清晰 |
| daily_stock_analysis | LLM 投研流水线，forks 极高，社区活跃 |
| ai-hedge-fund | 多 Agent 投研经典项目，适合架构参考 |
| anti-gambling-trader-tw | 反诈 + 幸存者偏差检测，定位独特，值得跟踪 |
| OpenBB | 金融数据平台，面向 AI Agent 的数据层参考 |
| colibri | 本地 MoE 推理引擎，适合合规要求高的本地推理场景 |
| OpenStock | 开源行情产品，产品架构参考 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次数据提供了 `baseline_1d`（2026-10-06）和 `baseline_7d`（2026-09-30），1 日和 7 日涨星数据基本完整。
- **缺失数据**：`star_delta_30d` 在所有项目中均为 `null`，无法分析 30 日趋势。部分项目（如 `logo-design-skill`、`anti-gambling-trader-tw`）的 `star_delta_7d` 为 `null`，可能是新项目或基线缺失。
- **样本偏差**：候选列表包含大量 awesome-list 类项目（如 `awesome-selfhosted`、`awesome-python`、`awesome-go`、`build-your-own-x`、`awesome-vue` 等），这些项目因关键词误匹配进入候选，并非真正的金融/量化/交易项目，分析时需过滤。真正与金融/交易直接相关的项目约占三分之一。
- **采集失败**：未发现明显采集失败迹象，但 `star_delta_30d` 全为空，可能为采集配置未启用 30 日基线。
- **风险提示**：部分项目的 `risk_flags` 和 `category_guess` 来自自动分类，可能存在误判；项目 description、topics 等字段仅作为被分析文本，未经验证。
