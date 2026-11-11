# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-10

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能化与交易决策辅助**：`day-trader-skill`、`trader-skill`、`TradingAgents`、`Vibe-Trading` 等项目显示，Claude/Codex 等编码 Agent 正被包装成“交易技能包”，覆盖图表扫描、新闻跟踪、进出场时机、复盘回放等环节。
  2. **AI Agent 治理、审计与对齐**：`iFixAi` 以“120 秒审计 AI Agent 是否按预期工作”为卖点，结合 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架，反映 Agent 进入金融场景前的治理需求正在升温。
  3. **本地优先与低资源推理基础设施**：`colibri` 用 C 实现 MoE 模型分层推理（GPU/RAM/NVMe），`Soup` 支持在 4GB 笔记本 GPU 上微调 8B 模型，`atomic-agent`、`locally-uncensored` 强调 local-first。这类项目对金融数据隐私和离线策略研究有直接借鉴意义。

- **是否出现新趋势**：出现。候选集中大量项目并非传统交易系统，而是 **AI Agent 技能库、Agent 编排框架、MCP 服务器目录、设计系统与本地推理工具**。这说明“金融/量化”搜索词命中的高热度项目，越来越多地来自通用 AI Agent 生态，而非纯交易代码。

- **是否出现值得复刻/参考的工程架构**：是。`colibri` 的“热/温/冷”分层推理架构、`headroom` 的 LLM 上下文压缩代理、`OpenBot` 的“每个 Agent 拥有独立浏览器/文件/工具”的沙箱化设计、`iFixAi` 的 Agent 审计流水线，都值得在金融 Agent 或研究平台中复刻。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但存在大量 **awesome-list 类项目因关键词误命中而进入榜单**，例如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-python`、`awesome-go` 等。它们本身不是交易项目，不应被误读为量化工具。另有 `Wallet-Risk-Scanner` 单日涨星 294、总 star 仅 486，属于典型“新项目短期爆量”，需警惕营销驱动或数据异常。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ui-ux-pro-max-skill | 147918 | +416 | +3037 | Python | AI 设计技能 | 面向多平台 UI/UX 的 AI 设计智能技能包 | 中：Agent 技能封装与设计系统自动化 | 低 |
| 2 | awesome-selfhosted | 335912 | +314 | +2396 | 无 | 自托管清单 | 可自托管的免费网络服务清单 | 低：关键词误命中，非交易项目 | 中 |
| 3 | colibri | 49819 | +298 | +2408 | C | 推理引擎 | MoE 模型分层推理：GPU/RAM/NVMe | 高：低资源本地推理架构 | 低 |
| 4 | build-your-own-x | 561661 | +230 | +2136 | Markdown | 教程清单 | 从零重建技术的教程合集 | 低：关键词误命中 | 中 |
| 5 | public-apis | 498054 | +316 | +2130 | Python | API 清单 | 免费 API 合集 | 中：金融数据 API 来源参考 | 中 |
| 6 | daily_stock_analysis | 69635 | +368 | +2117 | Python | AI 股票分析 | LLM 多市场股票分析、新闻、看板、推送 | 高：LLM 金融决策看板与定时任务 | 低 |
| 7 | awesome-dsh-plugin | 24241 | +128 | +1944 | JavaScript | 插件清单 | DeepSeek Harness 插件精选 | 低：关键词误命中 | 低 |
| 8 | awesome-python | 333918 | +235 | +1606 | Python | Python 清单 | Python 工具精选 | 低：关键词误命中 | 低 |
| 9 | day-trader-skill | 6767 | +298 | +1743 | Python | 交易技能 | 11 个 Claude 日内交易技能 | 高：交易决策 Agent 技能化 | 低 |
| 10 | TradingAgents | 121918 | +193 | +1467 | Python | 多 Agent 交易 | 多 Agent LLM 金融交易框架 | 高：多 Agent 投研/交易决策架构 | 低 |
| 11 | iFixAi | 44751 | +263 | +1484 | Python | Agent 审计 | AI Agent 独立审计与对齐 | 高：Agent 治理、风控与合规 | 低 |
| 12 | open-design | 107081 | +168 | +1260 | TypeScript | 协作设计 | 本地优先协作 AI 设计工作台 | 中：金融看板/原型协作 | 低 |
| 13 | awesome-go | 193215 | +166 | +1247 | Go | Go 清单 | Go 框架与库精选 | 低：关键词误命中 | 中 |
| 14 | awesome-design-md | 126547 | +164 | +1035 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 合集 | 中：Agent 生成 UI 的设计约束 | 中 |
| 15 | gbrain | 32579 | +257 | +1071 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | 中：Agent 编排与记忆 | 低 |
| 16 | free-for-dev | 142543 | +137 | +758 | HTML | 免费资源 | SaaS/PaaS/IaaS 免费层清单 | 低：关键词误命中 | 低 |
| 17 | Kronos | 47594 | +134 | +968 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融时序基础模型 | 低 |
| 18 | OpenBot | 10847 | +249 | +783 | TypeScript | Agent 沙箱 | 每个 Agent 独立浏览器/文件/工具 | 高：Agent 操作审计与沙箱 | 中 |
| 19 | logo-design-skill | 6545 | +101 | +616 | HTML | 设计技能 | Logo 设计 Agent 技能 | 低：关键词误命中 | 低 |
| 20 | tick-stock-panel | 7574 | +108 | +574 | Python | A 股量化工作台 | 自托管 A 股策略/监控/回测 | 高：DuckDB+Polars+FastAPI 本地量化栈 | 低 |
| 21 | ruflo | 81451 | +65 | +630 | TypeScript | Agent 编排 | 多智能体 swarm 与自适应记忆 | 中：多 Agent 工作流 | 低 |
| 22 | awesome-claude-code | 57737 | +80 | +527 | Python | Claude 清单 | Claude Code 资源精选 | 低：关键词误命中 | 低 |
| 23 | awesome-mac | 118241 | +68 | +540 | Swift | macOS 清单 | macOS 软件精选 | 低：关键词误命中 | 低 |
| 24 | headroom | 79331 | +58 | +551 | Python | 上下文压缩 | LLM 输出/日志/RAG 压缩 | 高：降低金融 Agent token 成本 | 低 |
| 25 | 500-AI-Agents-Projects | 39673 | +119 | +384 | Python | Agent 案例 | 500 个 AI Agent 用例合集 | 中：金融 Agent 场景参考 | 中 |
| 26 | agentic-awesome-skills | 49508 | +66 | +390 | Python | 技能库 | 2955+ 可复用 Agent 技能 | 中：技能目录与选择机制 | 低 |
| 27 | awesome-remote-mcp-servers | 2964 | +63 | +416 | 无 | MCP 清单 | 远程 MCP 服务器合集 | 中：金融数据 MCP 接入 | 中 |
| 28 | Vibe-Trading | 38023 | +42 | +434 | Python | 交易 Agent | 个人交易 Agent | 高：LLM 交易 Agent 框架 | 低 |
| 29 | locally-uncensored | 3717 | +48 | +495 | TypeScript | 本地 AI 工作室 | 桌面本地 AI 聊天/图像/视频/编码 | 中：本地隐私 AI 工作台 | 低 |
| 30 | Soup | 10457 | +62 | +346 | Python | LLM 微调 | 一个 YAML 微调 LLM，4GB GPU 训 8B | 高：低资源领域模型微调 | 低 |
| 31 | Wallet-Risk-Scanner | 486 | +294 | +294 | Python | 钱包风控 | 多链加密钱包 AML/KYT 风险扫描 | 高：链上风控与 AML 评分 | 中 |
| 32 | awesome-mcp-servers | 97586 | +35 | +316 | 无 | MCP 清单 | MCP 服务器合集 | 中：金融工具 MCP 化 | 低 |
| 33 | goose | 3413 | +34 | +451 | C++ | 编程语言 | Goose 编程语言 | 低：关键词误命中 | 低 |
| 34 | trader-skill | 1653 | +38 | +450 | Python | 投资技能 | 11 个 Claude 投资技能 | 高：13F/新闻/仓位管理 Agent | 低 |
| 35 | prompt-master | 15813 | +37 | +338 | 无 | 提示词技能 | 生成准确提示词的 Claude 技能 | 低：关键词误命中 | 低 |
| 36 | atomic-agent | 3549 | +153 | +52 | TypeScript | 本地 Agent | 基于 llama.cpp 的本地优先 Agent | 中：本地金融 Agent 隐私 | 中 |
| 37 | OpenBB | 75319 | +29 | +252 | Python | 开放数据平台 | 面向分析师/量化/AI Agent 的数据平台 | 高：金融数据基础设施 | 中 |
| 38 | cs-video-courses | 84808 | +25 | +259 | 无 | 课程清单 | 计算机科学视频课程 | 低：关键词误命中 | 中 |
| 39 | Orkas | 9205 | +49 | +212 | JavaScript | 桌面 Agent 团队 | 本地优先多 Agent 桌面团队 | 中：多 Agent 任务编排 | 低 |
| 40 | awesome-telegram | 1194 | +161 | 无 | JavaScript | Telegram 清单 | Telegram 频道/群组/机器人导航 | 低：关键词误命中 | 中 |
| 41 | ai-hedge-fund | 64630 | +27 | +158 | Python | AI 对冲基金 | AI 对冲基金团队 | 高：多 Agent 投研决策参考 | 低 |
| 42 | oh-my-openagent | 70828 | +16 | +144 | TypeScript | Agent 编排 | 图工程化 Agent 编排 | 中：Agent 工作流图化 | 低 |
| 43 | awesome-rust | 60454 | +20 | +136 | Rust | Rust 清单 | Rust 资源精选 | 低：关键词误命中 | 中 |
| 44 | awesome-cpp | 74357 | +11 | +136 | 无 | C++ 清单 | C/C++ 库与资源精选 | 低：关键词误命中 | 低 |
| 45 | awesome-public-datasets | 80023 | +18 | +80 | 无 | 数据集清单 | 高质量公开数据集 | 中：金融数据集来源 | 中 |
| 46 | awesome-machine-learning | 74791 | +3 | +48 | Python | ML 清单 | 机器学习框架与库精选 | 低：关键词误命中 | 低 |
| 47 | awesome-vue | 73480 | +1 | -10 | 无 | Vue 清单 | Vue.js 资源精选 | 低：关键词误命中 | 低 |

## 3. 重点项目深度分析

### 3.1 colibri — MoE 模型分层推理引擎

- **解决什么问题**：让前沿 MoE 模型在消费级硬件上运行，通过把“热专家”放 GPU（CUDA/Vulkan）、“温专家”放 RAM、“冷专家”从 NVMe 流式加载，降低显存门槛。
- **为什么值得关注**：7 日涨星 +2408，24h +298，总 star 约 5 万，且持续 push。对金融领域本地部署大模型、保护行情与策略数据隐私有直接价值。
- **技术栈/架构亮点**：C 语言实现，Apache-2.0。分层存储 + 按需流式加载是典型的“异构存储推理”架构，类似思路可迁移到金融时序模型或风控模型的边缘部署。
- **是否适合借鉴**：适合。可借鉴其“热/温/冷”分层思想，设计本地量化研究环境的模型服务层，避免把所有模型常驻显存。
- **可能风险**：项目较新，open_issues 188，生态和文档可能不成熟；C 实现调试门槛高；与金融业务无直接绑定，需自行验证推理精度和吞吐。

### 3.2 daily_stock_analysis — LLM 多市场股票分析系统

- **解决什么问题**：用 LLM 聚合多源行情、实时新闻，生成决策看板并自动推送，支持零成本定时运行。
- **为什么值得关注**：24h +368、7d +2117，总 star 约 7 万，近期 push 活跃。是“LLM + 金融决策看板”的典型产品形态。
- **技术栈/架构亮点**：Python + MIT。多源数据接入、实时新闻、决策看板、自动推送、定时任务。架构上强调“零成本定时运行”，适合个人研究者。
- **是否适合借鉴**：适合。可复刻其“数据采集 → LLM 分析 → 看板 → 推送”的流水线，替换为自己的数据源和提示词模板。
- **可能风险**：金融合规风险，尤其是自动推送“决策”内容可能被误读为投资建议；LLM 输出存在幻觉，需人工校验；依赖外部新闻与行情 API 的稳定性。

### 3.3 day-trader-skill / trader-skill — Claude 交易技能包

- **解决什么问题**：把日内交易或投资流程封装成 11 个 Claude 技能，包括扫描图表、跟踪新闻、择时进出场、复盘结果、复制信任投资者、跟踪国会交易、按预算调整仓位等。
- **为什么值得关注**：`day-trader-skill` 24h +298、7d +1743；`trader-skill` 24h +38、7d +450。两者均来自同一作者，说明“交易技能包”正在快速涨星。
- **技术栈/架构亮点**：Python + MIT，基于 Claude Skills 机制。核心不是策略本身，而是把交易流程拆成可复用、可组合的技能单元。
- **是否适合借鉴**：适合。可借鉴其“技能化交易流程”的思路，把研究、风控、下单前确认等环节封装为 Agent 技能，并强制“未经确认不下单”的人机协作边界。
- **可能风险**：策略有效性未经验证；技能描述中存在“复制你信任的投资者”“跟踪国会”等表述，可能涉及合规灰色地带；不可直接接入真实交易账户。

### 3.4 TradingAgents — 多 Agent LLM 金融交易框架

- **解决什么问题**：用多个 LLM Agent 模拟投研团队，进行基本面、技术面、情绪面分析，并输出交易决策。
- **为什么值得关注**：总 star 约 12 万，7d +1467，是“多 Agent 金融决策”方向的高知名度项目。
- **技术栈/架构亮点**：Python + Apache-2.0。多 Agent 分工、辩论或协作机制，适合研究 Agent 间信息传递与决策融合。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色划分和决策流程，但更适合作为研究框架，而非直接实盘。
- **可能风险**：策略过拟合、回测幸存者偏差；LLM 决策可解释性差；金融合规风险；维护活跃度需观察。

### 3.5 iFixAi — AI Agent 独立审计

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审，声称 120 秒内给出结论。
- **为什么值得关注**：24h +263、7d +1484，总 star 约 4.5 万。契合金融场景对 Agent 可审计、可治理、可对齐的强需求。
- **技术栈/架构亮点**：Python + Apache-2.0。覆盖 agent-evaluation、ai-governance、hallucination-detection、prompt-injection、EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等主题。
- **是否适合借鉴**：非常适合。金融 Agent 上线前需要审计流水线，可借鉴其评估维度、CLI 诊断工具和合规映射思路。
- **可能风险**：审计结论的可靠性依赖评估集质量；可能被误用为“合规洗白”工具；需结合人工复核。

### 3.6 tick-stock-panel — 自托管 A 股量化工作台

- **解决什么问题**：提供 A 股“自建策略 + 监控 + 回测”的本地量化工作台，支持 LLM 驱动策略定制、个股分析和复盘。
- **为什么值得关注**：24h +108、7d +574，近期持续 push。技术栈明确：DuckDB、Polars、FastAPI、React、LLM。
- **技术栈/架构亮点**：Python + MIT。DuckDB + Polars 适合本地分析型负载，FastAPI + React 提供看板，LLM 用于策略定制和个股分析。
- **是否适合借鉴**：适合。可作为“本地优先、零运维”量化研究平台的参考架构，尤其是 DuckDB + Polars 的组合值得复刻。
- **可能风险**：A 股数据合规与接口稳定性；LLM 生成策略存在过拟合风险；个人开源项目维护持续性需观察。

### 3.7 Kronos — 金融市场语言基础模型

- **解决什么问题**：构建金融市场的“语言”基础模型，可能用于金融时序建模或跨资产表示学习。
- **为什么值得关注**：总 star 约 4.8 万，7d +968。是“金融基础模型”方向的代表性项目。
- **技术栈/架构亮点**：Python + MIT。具体架构信息不足，但定位为 Foundation Model，适合关注其输入表示、预训练任务和下游适配方式。
- **是否适合借鉴**：适合作为研究方向跟踪，尤其是金融时序 token 化、跨市场预训练、少样本策略迁移。
- **可能风险**：信息不足，无法判断模型实际能力；金融基础模型存在数据泄漏、过拟合和不可解释性风险。

### 3.8 OpenBot — 每个 Agent 拥有独立计算机

- **解决什么问题**：为 AI Agent 提供独立浏览器、文件和工具环境，所有动作在执行前决定、执行后记录，支持任意 AG-UI Agent。
- **为什么值得关注**：24h +249、7d +783，近期活跃。其“动作前决策 + 动作后记录”的设计对金融 Agent 操作审计很有价值。
- **技术栈/架构亮点**：TypeScript + MIT。AG-UI、MCP、browser-automation、agent-governance。强调沙箱化和可记录性。
- **是否适合借鉴**：适合。金融 Agent 操作交易终端、浏览器或内部系统时，可借鉴其“决策留痕 + 动作记录”的治理模式。
- **可能风险**：浏览器自动化存在账号安全风险；若用于交易相关操作，需严格隔离权限；项目较新，生态待观察。

### 3.9 Wallet-Risk-Scanner — 多链钱包风险扫描

- **解决什么问题**：对加密钱包地址进行 AML/KYT 筛查，输出 0–100 风险评分，集成 6 个情报源，支持 15+ 链、批量筛查和多种报告格式。
- **为什么值得关注**：24h +294，但总 star 仅 486，属于新项目短期爆量。功能描述具体，覆盖制裁、风险合约、资金追踪、诈骗/黑客/混币器/钓鱼检测。
- **技术栈/架构亮点**：Python + MIT。多情报源 failover、批量筛查、TXT/JSON/CSV/HTML/PDF 报告。
- **是否适合借鉴**：适合。可借鉴其“多源情报 + 风险评分 + 报告输出”的链上风控流水线，尤其适合合规/反洗钱场景。
- **可能风险**：总 star 低、单日涨星占比过高，需警惕营销或刷星；加密地址标注数据质量参差；不可作为唯一合规依据。

### 3.10 headroom — LLM 上下文压缩

- **解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前压缩，声称编码 Agent 减少 20% token，JSON 减少 60–95% token，且答案不变。
- **为什么值得关注**：总 star 约 8 万，7d +551。金融 Agent 常需处理大量行情、公告、日志，token 成本是现实瓶颈。
- **技术栈/架构亮点**：Python + Apache-2.0。提供库、代理和 MCP server 三种形态，支持 Claude Code、Cursor、LangChain、OpenAI 等。
- **是否适合借鉴**：适合。可将其作为金融 Agent 数据管道的中间层，降低上下文成本，同时需验证压缩是否丢失关键风险信息。
- **可能风险**：压缩可能丢失关键数字或风险信号；需在金融场景做严格回归测试；依赖上游模型兼容性。

## 4. 趋势归纳

- **技术趋势**：
  - **本地优先与低资源推理**：`colibri`、`Soup`、`atomic-agent`、`locally-uncensored` 共同指向“在自有硬件上跑模型”，契合金融数据隐私需求。
  - **Agent 技能化与模块化**：大量项目以“skills”形式封装能力，支持 Claude、Codex、Cursor、Gemini CLI 等多平台。
  - **MCP 成为工具接入标准**：`awesome-mcp-servers`、`awesome-remote-mcp-servers`、`headroom`、`OpenBot` 均涉及 MCP，金融数据源和交易工具 MCP 化是明确方向。
  - **Agent 治理与审计**：`iFixAi`、`OpenBot` 强调动作记录、审计、对齐，反映 Agent 进入生产环境前的合规需求。

- **产品趋势**：
  - **从“交易机器人”到“决策辅助 Agent”**：`daily_stock_analysis`、`day-trader-skill`、`trader-skill`、`Vibe-Trading` 更强调分析、看板、推送和人工确认，而非全自动下单。
  - **本地量化工作台**：`tick-stock-panel` 代表“自托管、零运维、DuckDB+Polars+FastAPI”的轻量量化产品形态。
  - **设计系统与 Agent 生成 UI 结合**：`ui-ux-pro-max-skill`、`open-design`、`awesome-design-md` 显示金融看板和原型的 AI 生成正在标准化。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 投研**：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 持续受关注，但多数定位为研究框架。
  - **金融基础模型**：`Kronos` 代表“金融语言模型”方向，值得跟踪其是否真正解决金融时序建模问题。
  - **链上风控与 AML**：`Wallet-Risk-Scanner` 显示加密风控工具正在向“多源情报 + 风险评分”产品化发展。

- **AI Agent 与自动化交易结合趋势**：
  - 结合点正从“Agent 直接下单”转向“Agent 辅助决策 + 人工确认 + 动作审计”。
  - 技能化交易流程、MCP 数据接入、本地模型推理、上下文压缩，构成金融 Agent 的四个基础设施层。

- **值得后续做原型验证的方向**：
  - 本地金融研究 Agent：DuckDB + Polars + 本地 LLM + MCP 数据源。
  - 交易决策技能包：把研究、风控、下单前确认封装为可审计技能。
  - Agent 操作审计流水线：借鉴 `iFixAi` 和 `OpenBot`，为金融 Agent 增加动作留痕与合规检查。
  - 金融数据上下文压缩：验证 `headroom` 类方案在行情/公告数据上的信息保真度。

## 5. 今日灵感清单

1. **MVP：本地金融研究看板**：用 DuckDB + Polars 存储日线/分钟数据，FastAPI 提供接口，React 展示，接入本地 LLM 生成每日摘要。参考 `tick-stock-panel` 和 `daily_stock_analysis`。
2. **MVP：交易决策技能包**：把“数据获取 → 技术面分析 → 新闻情绪 → 风险评估 → 人工确认”封装为 5–8 个 Claude/Codex 技能，强制最后一步人工确认。参考 `day-trader-skill`、`trader-skill`。
3. **调研：MCP 金融数据服务器**：梳理 `awesome-mcp-servers` 和 `awesome-remote-mcp-servers` 中与行情、基本面、新闻、链上数据相关的 MCP server，评估可复用性。
4. **调研：低资源本地推理**：验证 `colibri` 的分层推理思路能否用于本地部署金融情感分析或风险分类模型，记录显存/延迟/精度 trade-off。
5. **Demo：Agent 操作审计**：用 `OpenBot` 或 `iFixAi` 的思路，给一个简单的“Agent 读取行情并生成报告”流程增加动作前决策记录和动作后日志，输出审计报告。
6. **Demo：金融数据上下文压缩**：用 `headroom` 对财报、公告、订单簿快照等长文本做压缩，对比压缩前后 LLM 抽取关键风险信息的能力。
7. **原型：链上钱包风险评分**：参考 `Wallet-Risk-Scanner`，用公开地址标签数据做一个最小版 0–100 风险评分 API，输出 JSON 报告。
8. **调研：金融基础模型**：跟踪 `Kronos` 的输入表示、预训练任务和下游任务，评估是否适合做波动率预测或跨资产表示学习。
9. **Watchlist：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading`**：作为多 Agent 投研框架的对比研究对象，重点看其 Agent 角色划分和决策融合机制。
10. **Watchlist：`iFixAi`、`OpenBot`**：作为金融 Agent 治理与审计的基础设施候选，关注其是否出现金融行业适配版本。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| colibri | 低资源本地推理架构，适合金融隐私场景，技术独特性强 |
| daily_stock_analysis | LLM 金融决策看板的产品形态清晰，适合复刻流水线 |
| day-trader-skill / trader-skill | 交易流程技能化，适合研究 Agent 辅助决策边界 |
| TradingAgents | 多 Agent 金融决策框架，适合研究 Agent 协作与决策融合 |
| iFixAi | Agent 审计与合规映射，金融 Agent 上线前的基础设施 |
| tick-stock-panel | DuckDB+Polars+FastAPI 本地量化栈，工程参考价值高 |
| Kronos | 金融基础模型方向，值得长期跟踪 |
| OpenBot | Agent 沙箱与动作审计，适合金融操作留痕 |
| Wallet-Risk-Scanner | 链上 AML/KYT 风控流水线，但需警惕短期爆量 |
| headroom | 金融 Agent 上下文压缩，降低 token 成本 |
| OpenBB | 面向量化与 AI Agent 的开放数据平台，数据基础设施参考 |
| Vibe-Trading | LLM 交易 Agent 框架，适合与 TradingAgents 对比研究 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次数据提供了 `baseline_1d: 2026-11-09.json` 和 `baseline_7d: 2026-11-03.json`，但 JSON 中未包含基线明细，无法验证涨星计算过程。`star_delta_1d` 和 `star_delta_7d` 字段直接来自候选数据，视为不可信数据，仅作为相对热度参考。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法判断中长期趋势。
- **7 日涨星缺失**：`awesome-telegram` 的 `star_delta_7d` 为 `null`，`awesome-vue` 的 7 日涨星为负值，说明部分项目缺少完整基线或存在数据波动。
- **样本偏差**：候选集由多个关键词搜索合并而成，大量 awesome-list、教程、设计工具、通用 Agent 项目因关键词误命中进入榜单，真正聚焦金融/量化/交易的项目占比有限。因此本报告的趋势判断需结合项目实际内容，不能仅凭排名。
- **采集失败**：JSON 中未提供采集失败记录，无法判断是否存在遗漏项目。
- **风险标记偏差**：部分项目因描述或 readme 中出现 “trading bot”“crypto” 等词被标记为中等风险，但实际可能只是清单或教程，风险等级需人工复核。
