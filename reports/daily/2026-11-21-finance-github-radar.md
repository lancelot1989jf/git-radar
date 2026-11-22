# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-21

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **Claude Code / AI Agent Skills 生态爆发**：`Claude-BugHunter`（24h +1698）、`claude-trading-skills`（24h +191）、`day-trader-skill`（24h +129）等“技能包”项目涨星极快，说明市场正在从“通用 Agent 框架”转向“可复用、可组合的垂直领域技能包”。
  2. **LLM 驱动的股票分析与交易 Agent**：`daily_stock_analysis`（7d +1340）、`TradingAgents`（7d +783）、`Vibe-Trading`（7d +404）、`risk-aware-trading-agents`（7d +275）等持续走热，多智能体、新闻回测、风险感知成为关键词。
  3. **AI Agent 治理与审计**：`iFixAi`（24h +220）聚焦“AI Agent 是否在做它该做的事”，结合 ISO 42001、NIST AI RMF、OWASP LLM 等治理框架，反映企业级 Agent 落地对可审计性的需求上升。

- **是否出现新趋势**：出现。**“Claude/Codex Skills 即产品”** 成为明显趋势——大量项目不再发布完整应用，而是发布可被编码 Agent 直接调用的技能包、提示词库、设计规范（如 `ui-ux-pro-max-skill`、`modern-web-guidance`、`awesome-design-md`）。这改变了开源项目的分发和消费方式。

- **是否出现值得复刻/参考的工程架构**：出现。`risk-aware-trading-agents` 提出“冻结时间点市场 + 新闻回测 + 每次运行前视偏差检查 + LLM Agent over MCP + 10 家券商 paper/live 交易”的架构，是当前候选中最值得研究的交易 Agent 工程范式。`colibri` 的“GPU 热专家 / RAM 温专家 / NVMe 冷专家”分层推理引擎也值得关注。

- **是否有明显骗局、过度营销或高风险项目**：本次候选池中混入大量**误匹配的 awesome-list 和通用工具项目**（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-python`、`awesome-go` 等），它们并非金融/量化项目，只是因关键词命中而被纳入。另有 `Turnitout-Humanizer` 这类“AI 查重规避工具”，与金融无关且存在学术诚信风险，应剔除观察范围。未发现明显金融骗局项目，但多个 trading bot 类项目需按高风险对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ui-ux-pro-max-skill | 152588 | +339 | +2979 | Python | AI 技能/UI 设计 | 面向多平台的 UI/UX 设计智能技能包 | 中 | 低 |
| 2 | Claude-BugHunter | 16454 | +1698 | +10592 | Python | AI 安全/红队 | 82 个漏洞挖掘技能的 Claude Code 技能包 | 高 | 低 |
| 3 | modern-web-guidance | 24715 | +639 | +8825 | 无 | Web 最佳实践 | 让编码 Agent 跟上最新 Web 最佳实践 | 中 | 低 |
| 4 | claude-trading-skills | 7671 | +191 | +2672 | Python | 交易技能/研究 | 面向股票投资者的 Claude 交易技能包 | 高 | 低 |
| 5 | awesome-selfhosted | 339339 | +283 | +2159 | 无 | 自托管清单 | 自托管网络服务清单（误匹配） | 低 | 中 |
| 6 | build-your-own-x | 564528 | +332 | +1929 | Markdown | 教程清单 | 从零复刻技术的教程清单（误匹配） | 低 | 中 |
| 7 | public-apis | 500693 | +152 | +1594 | Python | API 清单 | 免费 API 合集（误匹配） | 低 | 中 |
| 8 | colibri | 52748 | +216 | +1564 | C | 推理引擎 | 分层 MoE 推理引擎，GPU/RAM/NVMe 混合 | 高 | 低 |
| 9 | awesome-python | 336330 | +214 | +1494 | Python | Python 清单 | Python 工具清单（误匹配） | 低 | 低 |
| 10 | awesome-go | 195286 | +204 | +1303 | Go | Go 清单 | Go 框架库清单（误匹配） | 低 | 中 |
| 11 | open-design | 108880 | +145 | +1195 | TypeScript | 协作设计 | 本地优先的协作式 AI 设计 Agent 工作区 | 中 | 低 |
| 12 | daily_stock_analysis | 73653 | +68 | +1340 | Python | AI 股票分析 | LLM 驱动的多市场股票智能分析系统 | 高 | 低 |
| 13 | day-trader-skill | 9085 | +129 | +1224 | Python | 日内交易技能 | 11 个日内交易 Claude 技能 | 高 | 低 |
| 14 | iFixAi | 46726 | +220 | +1006 | Python | AI 审计/治理 | AI Agent 独立审计，120 秒内回答 Agent 是否合规 | 高 | 低 |
| 15 | awesome-design-md | 128556 | +92 | +978 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 文件合集 | 中 | 中 |
| 16 | TradingAgents | 123411 | +84 | +783 | Python | 多智能体交易 | 多智能体 LLM 金融交易框架 | 高 | 低 |
| 17 | OpenBot | 13155 | +62 | +843 | TypeScript | Agent 机器人 | 开源可自托管 AI Bot 替代品 | 中 | 中 |
| 18 | awesome-mac | 119093 | +89 | +536 | Swift | macOS 清单 | macOS 软件清单（误匹配） | 低 | 低 |
| 19 | 500-AI-Agents-Projects | 40436 | +291 | +555 | Python | AI Agent 案例 | 500 个 AI Agent 用例合集 | 中 | 中 |
| 20 | headroom | 80282 | +56 | +598 | Python | 上下文压缩 | 在 LLM 前压缩工具输出/日志/RAG 块 | 高 | 低 |
| 21 | awesome-claude-code | 58557 | +72 | +530 | Python | Claude 资源 | Claude Code 资源清单 | 中 | 低 |
| 22 | free-for-dev | 143357 | +66 | +483 | HTML | 免费资源 | SaaS/PaaS/IaaS 免费层清单（误匹配） | 低 | 低 |
| 23 | awesome-mcp-servers | 98370 | +34 | +652 | 无 | MCP 清单 | MCP 服务器合集 | 中 | 低 |
| 24 | ruflo | 82244 | +62 | +505 | TypeScript | Agent 编排 | 多玩家 swarm、自适应记忆、向量 RAG 的 Agent harness | 高 | 低 |
| 25 | awesome-remote-mcp-servers | 3767 | +66 | +540 | 无 | MCP 清单 | 远程 MCP 服务器合集 | 中 | 中 |
| 26 | awesome-telegram | 1901 | +110 | +381 | JavaScript | Telegram 清单 | Telegram 频道/群组/机器人导航 | 低 | 中 |
| 27 | logo-design-skill | 7485 | +50 | +544 | HTML | 设计技能 | Logo 设计 AI 技能包 | 低 | 低 |
| 28 | BitNet | 42382 | +29 | +797 | C++ | 推理框架 | 微软 1-bit LLM 官方推理框架 | 中 | 低 |
| 29 | agentic-awesome-skills | 50113 | +48 | +390 | Python | 技能库 | 3000+ 可复用 AI Agent 技能 | 中 | 低 |
| 30 | Vibe-Trading | 38661 | +30 | +404 | Python | AI 交易 | “Vibe-Trading”个人交易 Agent | 高 | 低 |
| 31 | gbrain | 33382 | +28 | +347 | TypeScript | Agent 大脑 | Garry 的 OpenClaw/Hermes Agent Brain | 中 | 低 |
| 32 | tick-stock-panel | 8158 | +35 | +357 | Python | A 股量化工作台 | 自托管 A 股策略+监控+回测工作台 | 高 | 低 |
| 33 | easy-stock | 1997 | +96 | +126 | Go | A 股 AI 投研 | A 股 AI 投研桌面应用 | 中 | 低 |
| 34 | locally-uncensored | 4565 | +46 | +309 | TypeScript | 本地 AI | 本地 AI 工作室，聊天/图像/视频/编码 | 低 | 低 |
| 35 | FinGPT | 21672 | +76 | +98 | Jupyter Notebook | 金融 LLM | 开源金融大语言模型 | 高 | 低 |
| 36 | Financial-API | 4560 | +25 | +410 | TypeScript | 金融数据 API | 同花顺官方 A 股金融数据服务 | 高 | 低 |
| 37 | modern-web-guidance-src | 9974 | +361 | 信息不足 | TypeScript | Web 最佳实践 | modern-web-guidance 源码版 | 低 | 低 |
| 38 | risk-aware-trading-agents | 416 | +62 | +275 | Python | 风险感知交易 | 带新闻回测和前视偏差检查的 LLM 交易 Agent | 高 | 中 |
| 39 | Turnitout-Humanizer | 12520 | +26 | +251 | HTML | 学术规避 | AI 查重规避工具（与金融无关） | 低 | 中 |
| 40 | OpenBB | 75631 | +20 | +198 | Python | 开放数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高 | 中 |
| 41 | prompt-master | 16224 | +33 | +233 | 无 | 提示词技能 | 为任意 AI 工具生成准确提示词的 Claude 技能 | 中 | 低 |
| 42 | awesome-rust | 60716 | +22 | +171 | Rust | Rust 清单 | Rust 资源清单（误匹配） | 低 | 中 |
| 43 | awesome-cpp | 74557 | +19 | +132 | 无 | C++ 清单 | C/C++ 资源清单（误匹配） | 低 | 低 |
| 44 | awesome-public-datasets | 80242 | +16 | +120 | 无 | 数据集清单 | 高质量开放数据集清单 | 中 | 中 |
| 45 | oh-my-openagent | 71051 | +14 | +137 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中 | 低 |
| 46 | ai-hedge-fund | 64804 | +21 | +122 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 47 | awesome-machine-learning | 74877 | +11 | +46 | Python | ML 清单 | 机器学习资源清单（误匹配） | 低 | 低 |
| 48 | cs-video-courses | 84904 | +3 | +52 | 无 | 课程清单 | 计算机科学视频课程清单（误匹配） | 低 | 中 |
| 49 | awesome-vue | 73466 | -3 | -8 | 无 | Vue 清单 | Vue 资源清单（误匹配） | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 Claude-BugHunter（rank 2，24h +1698）

- **解决什么问题**：将漏洞挖掘/红队工作流封装为 Claude Code 可调用的技能包，包含 82 个技能、15 个 slash 命令、681 个披露报告模式，覆盖 24 类漏洞，并提供企业身份与基础设施攻击矩阵。
- **为什么值得关注**：24h 涨星 +1698、7d +10592，是本次候选池中涨星最快的项目之一。它验证了“安全专家知识 → 可复用 Agent 技能包”的产品化路径。
- **技术栈/架构亮点**：基于 Claude Code Skills 机制，将攻击矩阵、漏洞模式、披露报告模板结构化，供 Agent 按需调用。
- **是否适合借鉴到 AI/自动化交易**：非常适合。可借鉴其“领域知识结构化 + 技能包分发”模式，构建**交易合规审计技能包**、**策略回测审查技能包**、**API key 安全审计技能包**。
- **可能风险**：安全类技能可能被滥用；技能内容质量依赖维护者持续更新；与金融交易无直接关系，需自行迁移。

### 3.2 claude-trading-skills（rank 4，24h +191）

- **解决什么问题**：为股票投资者和交易者提供 Claude Code 技能，覆盖市场分析、技术图表、经济日历、筛选器和交易策略开发。
- **为什么值得关注**：7d +2672，说明“交易技能包”需求旺盛。它把传统量化研究工具链（图表、筛选、策略开发）转化为 Agent 可调用的自然语言工作流。
- **技术栈/架构亮点**：Python + Claude Skills，以技能包形式组织交易研究能力。
- **是否适合借鉴**：适合。可借鉴其“交易研究任务拆解为技能”的思路，构建企业内部的**投研 Agent 技能库**，例如财报解读、波动率监控、事件驱动策略生成。
- **可能风险**：标记为 `likely_research_tool`，仅适合研究，不应直接用于实盘；策略开发技能可能诱导过拟合；需注意数据源合规。

### 3.3 daily_stock_analysis（rank 12，7d +1340）

- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板和自动推送，支持零成本定时运行。
- **为什么值得关注**：7d +1340，是 A 股/多市场 LLM 分析方向的代表项目。中文描述、A 股场景、AI Agent 标签，说明国内个人开发者在快速跟进 LLM 投研。
- **技术栈/架构亮点**：Python，多源行情 + 实时新闻 + 决策看板 + 自动推送，强调“零成本定时运行”。
- **是否适合借鉴**：适合。可借鉴其“多源数据聚合 + LLM 决策看板 + 定时推送”的轻量级投研 Agent 架构，尤其适合个人或小团队快速搭建投研日报系统。
- **可能风险**：LLM 生成的分析可能存在幻觉；数据源稳定性与合规性需验证；不应将分析结果直接作为交易信号。

### 3.4 iFixAi（rank 14，24h +220）

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，可在 120 秒内给出答案。
- **为什么值得关注**：24h +220，且 topics 覆盖 ISO 42001、NIST AI RMF、OWASP LLM、EU AI Act、prompt injection、hallucination detection 等企业级治理关键词。这代表 **AI Agent 从“能跑”走向“可审计、可治理”** 的转折。
- **技术栈/架构亮点**：Python + CLI，支持人类或 Agent 自身运行审计，覆盖对齐、安全、幻觉检测、提示注入等维度。
- **是否适合借鉴**：非常适合。在自动化交易 Agent 中，可借鉴其审计思路，构建**交易 Agent 行为审计层**：下单前检查、策略偏离检测、异常行为告警、合规留痕。
- **可能风险**：审计框架本身可能被绕过；对金融场景的适配需要额外开发；不应将审计通过等同于策略安全。

### 3.5 TradingAgents（rank 16，7d +783）

- **解决什么问题**：多智能体 LLM 金融交易框架，将交易决策拆分为多个 Agent 协作。
- **为什么值得关注**：123k stars，是 LLM 多智能体交易方向的标杆项目之一，持续有 push。
- **技术栈/架构亮点**：Python + Apache-2.0，多 Agent 架构，topics 包含 agent、finance、llm、multiagent、trading。
- **是否适合借鉴**：适合。可借鉴其多智能体角色分工（如基本面分析 Agent、技术面 Agent、风控 Agent、决策 Agent）的架构，用于企业级投研 Agent 框架设计。
- **可能风险**：标记为 `likely_research_tool`，仅适合研究；多 Agent 协作可能放大幻觉和错误传播；回测结果可能过拟合；不应直接用于实盘。

### 3.6 risk-aware-trading-agents（rank 38，7d +275）

- **解决什么问题**：面向美股的风险感知 AI 交易 Agent，提供新闻回测、冻结时间点市场、前视偏差检查、LLM Agent over MCP、10 家券商 paper/live 交易。
- **为什么值得关注**：虽然 stars 仅 416，但架构设计是本次候选池中**最严谨的交易 Agent 工程范式**。它显式处理了 LLM 交易回测中最常见的前视偏差问题，并提供公开 LLM 交易 Agent 排行榜（rta-bench-1）。
- **技术栈/架构亮点**：Python，冻结 2020/2022/2026 时间点市场（价格、VIX、新闻），每次运行前视偏差检查，LLM Agent over MCP，支持 Alpaca、Interactive Brokers 等 10 家券商。
- **是否适合借鉴**：非常适合。这是**企业级 AI 交易 Agent 回测基础设施**的直接参考：时间点冻结、新闻回测、前视偏差自动检查、paper/live 分离、公开基准。
- **可能风险**：标记为 `trading_bot`，风险等级中；涉及真实券商接口，API key 安全是核心风险；策略可能过拟合；不应直接用于实盘。

### 3.7 tick-stock-panel（rank 32，7d +357）

- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，LLM 能力驱动策略定制、个股分析和复盘。
- **为什么值得关注**：topics 包含 duckdb、polars、fastapi、react、ai-agent、backtesting，技术栈现代且完整，是 A 股个人量化工作台的代表。
- **技术栈/架构亮点**：Python + DuckDB + Polars + FastAPI + React，强调自托管和零运维，支持第三方数据源接入。
- **是否适合借鉴**：适合。可借鉴其“DuckDB + Polars 本地数据栈 + FastAPI 服务 + React 前端”的轻量级量化工作台架构，适合个人或小团队快速搭建研究环境。
- **可能风险**：标记为 `likely_research_tool`；A 股数据源合规性需注意；LLM 生成的策略需严格回测验证。

### 3.8 ai-hedge-fund（rank 46，7d +122）

- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 扮演不同角色进行投资决策。
- **为什么值得关注**：64k stars，是 AI 多智能体投资决策的经典参考项目，持续有更新。
- **技术栈/架构亮点**：Python，多 Agent 角色模拟（如价值投资 Agent、成长投资 Agent、风控 Agent）。
- **是否适合借鉴**：适合。可借鉴其多角色 Agent 协作的投资决策流程，用于投研 Agent 框架设计。
- **可能风险**：标记为 `likely_research_tool`；模拟结果不代表真实收益；多 Agent 决策可能过拟合；不应直接用于实盘。

### 3.9 OpenBB（rank 40，7d +198）

- **解决什么问题**：面向分析师、量化研究员和 AI Agent 的开放数据平台，覆盖股票、期权、加密、固定收益、经济数据等。
- **为什么值得关注**：75k stars，是金融数据基础设施的重要开源项目，topics 包含 ai、quantitative-finance、options、crypto 等。
- **技术栈/架构亮点**：Python，统一数据访问层，支持多种资产类别。
- **是否适合借鉴**：适合。可借鉴其“统一金融数据访问接口”的设计，作为 AI 交易 Agent 的数据层基础设施。
- **可能风险**：标记为 `crypto_related`；数据源许可和合规需注意；作为数据层依赖，需评估其维护活跃度和 API 稳定性。

### 3.10 colibri（rank 8，24h +216）

- **解决什么问题**：面向前沿 MoE 模型的分层推理引擎，热专家在 GPU（CUDA、Vulkan）、温专家在 RAM、冷专家从 NVMe 流式加载。
- **为什么值得关注**：24h +216、7d +1564，C 语言编写，强调“在你已有的硬件上运行”。虽然不是金融项目，但其分层推理架构对量化场景中**本地部署 LLM 投研 Agent** 有直接参考价值。
- **技术栈/架构亮点**：C + Apache-2.0，GPU/RAM/NVMe 三级分层推理。
- **是否适合借鉴**：适合。可调研其分层推理思路，用于降低本地 LLM 投研 Agent 的硬件门槛，尤其适合对数据隐私敏感的金融场景。
- **可能风险**：与金融无直接关系；C 语言项目维护和集成成本较高；需评估实际推理性能。

## 4. 趋势归纳

### 技术趋势
- **“Skills 即产品”**：Claude Code / Codex / Cursor 技能包成为新的开源分发形态，项目不再发布完整应用，而是发布可被 Agent 调用的结构化知识。
- **MCP 成为 Agent 数据/工具接入标准**：多个项目（`risk-aware-trading-agents`、`Financial-API`、`headroom`、`OpenBot`）都涉及 MCP，MCP 正在成为 AI Agent 与金融数据、交易接口连接的事实标准。
- **本地优先与自托管**：`open-design`、`tick-stock-panel`、`locally-uncensored`、`colibri` 都强调本地优先、自托管、隐私保护，反映金融场景对数据主权的需求。
- **上下文工程**：`headroom` 聚焦在 LLM 前压缩工具输出/日志/RAG 块，减少 token 消耗，这对高频调用 LLM 的投研 Agent 有直接成本价值。

### 产品趋势
- **从“交易机器人”到“投研 Agent 工作台”**：`daily_stock_analysis`、`tick-stock-panel`、`easy-stock` 等项目更强调分析、监控、复盘，而非自动下单，产品重心从执行转向决策支持。
- **AI Agent 治理产品化**：`iFixAi` 代表 Agent 审计/治理从概念走向产品，企业级 Agent 落地需要可审计、可对齐、可合规。
- **设计系统与 Agent 协作**：`open-design`、`awesome-design-md`、`ui-ux-pro-max-skill` 显示 AI Agent 正在进入设计协作领域，金融产品 UI 也可受益。

### 量化/交易策略趋势
- **LLM 多智能体交易框架持续演进**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 等项目持续更新，多角色 Agent 协作成为主流范式。
- **新闻回测与前视偏差检查**：`risk-aware-trading-agents` 显式处理前视偏差，这是 LLM 交易回测走向严谨化的重要信号。
- **A 股 LLM 投研生态活跃**：`daily_stock_analysis`、`tick-stock-panel`、`easy-stock`、`Financial-API` 等项目显示国内开发者在快速构建 A 股 LLM 投研工具链。

### AI Agent 与自动化交易结合趋势
- **Agent 技能包 + 交易研究**：`claude-trading-skills`、`day-trader-skill` 将交易研究能力封装为 Agent 技能，降低使用门槛。
- **MCP 连接交易接口**：`risk-aware-trading-agents` 通过 MCP 连接 LLM Agent 和券商接口，是 Agent 与交易系统集成的参考架构。
- **Agent 审计与风控**：`iFixAi` 的审计思路可迁移到交易 Agent 的下单前检查、行为监控和合规留痕。

### 值得后续做原型验证的方向
1. **交易 Agent 前视偏差自动检查器**：参考 `risk-aware-trading-agents`，构建一个可复用的回测前视偏差检测模块。
2. **投研 Agent 技能包**：参考 `claude-trading-skills`，构建企业内部的财报解读、波动率监控、事件驱动策略生成技能包。
3. **Agent 行为审计层**：参考 `iFixAi`，为自动化交易 Agent 构建下单前检查、策略偏离检测、异常行为告警的审计层。
4. **本地 LLM 投研 Agent**：参考 `colibri` 的分层推理思路，探索在消费级硬件上部署本地投研 Agent 的可行性。
5. **MCP 金融数据网关**：参考 `Financial-API` 和 `OpenBB`，构建统一的 MCP 金融数据接入层。

## 5. 今日灵感清单

1. **MVP：交易 Agent 前视偏差检查器**。参考 `risk-aware-trading-agents` 的 look-ahead check 思路，做一个独立的 Python 库，输入回测配置和历史数据，自动检测策略是否使用了未来信息。可让 Codex 自动复现其核心检查逻辑。

2. **MVP：投研 Agent 技能包生成器**。参考 `claude-trading-skills` 和 `day-trader-skill`，做一个模板化工具，让用户把自己的投研工作流（如财报解读、技术指标分析）快速打包成 Claude Code 技能。

3. **调研：MCP 金融数据网关的标准化**。对比 `Financial-API`、`OpenBB`、`risk-aware-trading-agents` 的 MCP 实现，总结金融数据 MCP server 的最佳实践，输出一份内部技术调研报告。

4. **Demo：Agent 行为审计层**。参考 `iFixAi`，为现有交易 Agent 加一层审计：记录每次决策的输入、输出、工具调用，检测提示注入、幻觉、策略偏离。可让 Agent 自动生成审计报告。

5. **原型：本地 LLM 投研 Agent**。参考 `colibri` 的分层推理思路，调研在 16GB/32GB 消费级硬件上运行本地 LLM 做财报摘要和情绪分析的可行性。

6. **调研：Claude Code Skills 的工程化规范**。对比 `Claude-BugHunter`、`claude-trading-skills`、`agentic-awesome-skills` 的技能包结构，总结一套企业内部技能包开发规范。

7. **MVP：A 股投研日报 Agent**。参考 `daily_stock_analysis`，用 DuckDB + Polars + LLM 搭建一个轻量级 A 股投研日报生成器，支持定时运行和推送。

8. **调研：LLM 交易回测的幸存者偏差与过拟合**。结合 `TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 的回测实现，总结 LLM 交易回测中常见的偏差来源和缓解方法。

9. **Demo：交易策略合规审计技能包**。参考 `Claude-BugHunter` 的“领域知识结构化”模式，构建一个交易策略合规审计技能包，覆盖杠杆限制、持仓集中度、马丁/网格风险识别。

10. **Watchlist 候选**：`risk-aware-trading-agents`（严谨的回测架构）、`iFixAi`（Agent 审计）、`tick-stock-panel`（现代 A 股量化工作台）、`Financial-API`（官方 A 股数据 MCP）、`headroom`（上下文压缩降本）。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| risk-aware-trading-agents | 最严谨的 LLM 交易 Agent 回测架构，显式处理前视偏差，提供公开基准，值得持续跟踪其演进 |
| iFixAi | AI Agent 审计/治理的代表项目，可迁移到交易 Agent 风控，企业级 Agent 落地的重要参考 |
| claude-trading-skills | 交易技能包的代表，验证了“领域知识 → Agent 技能”的产品化路径，适合跟踪技能包生态演进 |
| daily_stock_analysis | A 股 LLM 投研代表，多源数据 + 决策看板 + 定时推送，适合跟踪国内 LLM 投研产品形态 |
| tick-stock-panel | 现代 A 股量化工作台，DuckDB + Polars + FastAPI + React 技术栈完整，适合跟踪个人量化工具链演进 |
| TradingAgents | LLM 多智能体交易标杆，持续更新，适合跟踪多 Agent 交易框架的架构演进 |
| Financial-API | 同花顺官方 A 股金融数据服务，支持 MCP，是 A 股 AI Agent 数据基础设施的重要项目 |
| headroom | LLM 上下文压缩，对高频调用 LLM 的投研 Agent 有直接降本价值，适合跟踪上下文工程技术 |
| colibri | 分层 MoE 推理引擎，对本地部署 LLM 投研 Agent 有参考价值，适合跟踪本地推理技术 |
| OpenBB | 统一金融数据访问平台，是 AI 交易 Agent 数据层的潜在基础设施，适合跟踪其 MCP/AI 集成进展 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-11-20）和 `baseline_7d`（2026-11-14），1 日和 7 日涨星数据基本完整。
- **30 日基线缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法提供 30 日涨星趋势，长期趋势判断受限。
- **7 日涨星缺失**：`modern-web-guidance-src`（rank 37）的 `star_delta_7d` 为 `null`，仅能提供 24h 涨星。
- **样本偏差**：候选池中混入大量**误匹配的 awesome-list 和通用工具项目**（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-python`、`awesome-go`、`awesome-mac`、`awesome-rust`、`awesome-cpp`、`awesome-vue`、`cs-video-courses` 等），这些项目并非金融/量化项目，仅因关键词命中而被纳入，稀释了金融/量化项目的信号密度。
- **分类噪声**：`category_guess` 存在明显误分类，例如 `Turnitout-Humanizer`（学术查重规避工具）被标记为 `risk_management` 和 `trading_bot`，`modern-web-guidance`（Web 最佳实践）被标记为 `risk_management`。分析时应以项目实际描述和 topics 为准。
- **采集失败**：未发现明显采集失败，但 `star_delta_30d` 全量缺失表明 30 日基线数据未纳入本次采集。
