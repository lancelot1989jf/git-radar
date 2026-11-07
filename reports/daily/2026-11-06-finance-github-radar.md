# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-06

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能化交易工具**：以 `day-trader-skill`、`trader-skill` 为代表，将 Claude/Codex 等编码 Agent 转化为“日内交易研究助手”，通过技能包封装图表扫描、新闻跟踪、仓位测算和交易复盘。
  2. **多 Agent 金融交易框架**：`TradingAgents`、`Vibe-Trading`、`QuantDinger` 等项目持续升温，LLM 多角色协作（研究员、交易员、风控官）正在成为开源量化研究的主流范式。
  3. **AI Agent 治理与审计**：`iFixAi` 以 7 日 +5793 星的高速增长进入视野，聚焦 AI Agent 行为审计、对齐、合规评估，对金融场景中的 Agent 安全具有直接借鉴意义。

- **是否出现新趋势**：出现。传统“交易 bot”热度正在被“Agent 技能包 + 本地优先 + 可审计 Agent”取代。多个项目不再直接下单，而是强调“研究、回测、复盘、人工确认”，风险叙事明显增强。

- **是否出现值得复刻/参考的工程架构**：是。`QuantDinger` 提出“自托管 Agentic Trading OS”的一体化架构（研究、因子发现、回测、优化、纸面/实盘执行、风控、监控、MCP、多租户 SaaS），值得作为企业级 Agent 交易平台的参考蓝图。`colibri` 的 MoE 分层推理引擎（GPU/RAM/NVMe 三级缓存）对本地化运行金融 LLM 有工程启发。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局项目，但存在大量“awesome-list”类聚合仓库因关键词误匹配进入榜单，实际与金融/量化关联度低。`day-trader-skill`、`trader-skill` 等技能包营销话术较强（“never place an order without your yes”），需警惕将研究工具误当实盘信号源。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 496803 | +302 | +3461 | Python | API 聚合 | 免费 API 合集 | 数据源发现 | 中 |
| 2 | awesome-selfhosted/awesome-selfhosted | 334600 | +384 | +2705 | 无 | 自托管清单 | 自托管服务列表 | 交易系统部署参考 | 中 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 146259 | +407 | +3609 | Python | AI 技能 | UI/UX 设计智能技能 | 金融产品前端灵感 | 低 |
| 4 | JustVugg/colibri | 48533 | +299 | +3516 | C | 推理引擎 | MoE 分层推理引擎 | 本地金融 LLM 推理 | 低 |
| 5 | TauricResearch/TradingAgents | 121061 | +186 | +2633 | Python | AI 交易 | 多 Agent LLM 金融交易框架 | 多角色 Agent 架构 | 低 |
| 6 | ifixai-ai/iFixAi | 43806 | +103 | +5793 | Python | Agent 审计 | AI Agent 独立审计 | Agent 风控与合规 | 低 |
| 7 | codecrafters-io/build-your-own-x | 560510 | +285 | +3104 | Markdown | 教程 | 从零复刻技术 | 交易系统复刻学习 | 中 |
| 8 | Jakeschincariol/day-trader-skill | 5817 | +190 | +2494 | Python | 交易技能 | 11 个日内交易 Claude 技能 | 交易研究 Agent 化 | 低 |
| 9 | shiyu-coder/Kronos | 47104 | +130 | +3017 | Python | 金融模型 | 金融市场基础模型 | 金融时序基础模型 | 低 |
| 10 | Orkas-AI/Orkas | 9074 | +27 | +4653 | JavaScript | Agent 编排 | 本地优先 AI 团队桌面应用 | 多 Agent 编排参考 | 低 |
| 11 | awesome-dsh-plugin/awesome-dsh-plugin | 23408 | +434 | +1870 | JavaScript | 插件清单 | DeepSeek Harness 插件列表 | Agent 插件生态 | 低 |
| 12 | vinta/awesome-python | 333050 | +217 | +1801 | Python | 清单 | Python 工具精选 | 量化技术选型 | 低 |
| 13 | CopilotKit/OpenBot | 10342 | +55 | +2035 | TypeScript | Agent 治理 | 开源 AI 协作者 | Agent 行为治理 | 中 |
| 14 | nexu-io/open-design | 106361 | +177 | +1438 | TypeScript | AI 设计 | 协作式 AI 设计工作台 | 金融仪表盘设计 | 低 |
| 15 | ripienaar/free-for-dev | 142120 | +106 | +1415 | HTML | 清单 | 开发者免费资源 | 低成本工具链 | 低 |
| 16 | avelino/awesome-go | 192483 | +173 | +1399 | Go | 清单 | Go 框架精选 | 低延迟交易基建 | 中 |
| 17 | VoltAgent/awesome-design-md | 125946 | +119 | +1391 | 无 | 设计系统 | DESIGN.md 文件合集 | Agent 生成 UI 规范 | 中 |
| 18 | ruvnet/ruflo | 81098 | +83 | +914 | TypeScript | Agent 框架 | 多智能体 swarm 框架 | Agent 编排架构 | 低 |
| 19 | kaankiziltug/logo-design-skill | 6188 | +106 | +885 | HTML | AI 技能 | Logo 设计技能 | 品牌自动化 | 低 |
| 20 | Fractal-Compute-Orchestrations/FractalWorkspace | 9241 | -8 | +1447 | Python | 联邦学习 | 大规模联邦学习工作区 | 分布式模型训练 | 低 |
| 21 | headroomlabs-ai/headroom | 79041 | +78 | +751 | Python | 上下文压缩 | LLM 工具输出压缩 | 降低 Agent token 成本 | 低 |
| 22 | aardappel/goose | 3190 | +89 | +656 | C++ | 编程语言 | Goose 编程语言 | 高性能系统语言 | 低 |
| 23 | HKUDS/Vibe-Trading | 37802 | +57 | +624 | Python | AI 交易 | 个人交易 Agent | 交易 Agent 产品化 | 低 |
| 24 | shy3130/tick-stock-panel | 7217 | +46 | +746 | Python | A 股量化 | 自托管 A 股量化工作台 | A 股数据工程 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 57429 | +75 | +538 | Python | 清单 | Claude Code 资源精选 | Agent 工具链 | 低 |
| 26 | sickn33/agentic-awesome-skills | 49296 | +63 | +525 | Python | 技能库 | 2926+ AI Agent 技能 | 技能复用模式 | 低 |
| 27 | Jakeschincariol/trader-skill | 1474 | +83 | +551 | Python | 交易技能 | 11 个投资者复刻技能 | 投资研究 Agent 化 | 低 |
| 28 | PurpleDoubleD/locally-uncensored | 3529 | +83 | +492 | TypeScript | 本地 AI | 本地 AI 工作室 | 本地化 AI 部署 | 低 |
| 29 | freqtrade/freqtrade | 56576 | +65 | +430 | Python | 交易 bot | 开源加密交易 bot | 交易系统参考 | 中 |
| 30 | jaywcjlove/awesome-mac | 117872 | +40 | +512 | Swift | 清单 | macOS 软件精选 | 交易终端工具 | 低 |
| 31 | punkpeye/awesome-remote-mcp-servers | 2734 | +56 | +502 | 无 | MCP | 远程 MCP 服务器合集 | 数据 MCP 接入 | 中 |
| 32 | MakazhanAlpamys/Soup | 10267 | +46 | +462 | Python | 微调 | 单 YAML 微调 LLM | 金融 LLM 微调 | 低 |
| 33 | punkpeye/awesome-mcp-servers | 97400 | +47 | +345 | 无 | MCP | MCP 服务器合集 | Agent 工具接入 | 低 |
| 34 | ZhuLinsen/daily_stock_analysis | 67661 | +33 | +385 | Python | 股票分析 | LLM 多市场股票分析 | 新闻情绪分析 | 低 |
| 35 | openbq-org/OpenBB | 75179 | +54 | +291 | Python | 数据平台 | 开放数据平台 | 量化数据基建 | 中 |
| 36 | Developer-Y/cs-video-courses | 84632 | +30 | +358 | 无 | 课程 | CS 视频课程列表 | 量化知识学习 | 中 |
| 37 | nidhinjs/prompt-master | 15616 | +41 | +353 | 无 | 提示工程 | 精准提示词技能 | Agent 提示优化 | 低 |
| 38 | garrytan/gbrain | 31599 | +37 | +256 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | Agent 记忆架构 | 低 |
| 39 | code-yeongyu/oh-my-openagent | 70757 | +19 | +267 | TypeScript | Agent 编排 | 图工程 Agent | Agent 工作流 | 低 |
| 40 | OpenByteInc/QuantDinger | 13586 | +30 | +289 | Python | 交易 OS | Agentic Trading OS | 一体化交易平台 | 中 |
| 41 | fffaraz/awesome-cpp | 74283 | +18 | +183 | 无 | 清单 | C++ 资源精选 | 低延迟系统 | 低 |
| 42 | rust-unofficial/awesome-rust | 60371 | +21 | +172 | Rust | 清单 | Rust 资源精选 | 高性能交易系统 | 中 |
| 43 | virattt/ai-hedge-fund | 64529 | +17 | +171 | Python | AI 对冲基金 | AI 对冲基金团队 | 多 Agent 投研 | 低 |
| 44 | awesomedata/awesome-public-datasets | 79971 | +13 | +124 | 无 | 数据集 | 公开数据集列表 | 另类数据源 | 中 |
| 45 | josephmisiti/awesome-machine-learning | 74773 | +8 | +82 | Python | 清单 | ML 资源精选 | 量化 ML 选型 | 低 |
| 46 | vuejs/awesome-vue | 73483 | +1 | -14 | 无 | 清单 | Vue 资源精选 | 前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents

- **解决什么问题**：将金融交易决策拆解为多个 LLM Agent 协作，模拟研究员、交易员、风控官等多角色讨论，输出交易信号。
- **为什么值得关注**：7 日 +2633 星，总星 12.1 万，是当前多 Agent 金融交易框架中规模最大、社区最活跃的项目之一。Apache-2.0 许可，适合二次开发。
- **技术栈/架构亮点**：Python + LLM 多 Agent 编排；topics 显示 `agent`、`finance`、`llm`、`multiagent`、`trading`。核心价值在于角色分工和辩论式决策流程，而非单一模型预测。
- **是否适合借鉴**：非常适合。可借鉴其“多角色辩论 + 结构化输出”模式，构建企业内部的投研 Agent 工作流，将研究员、风控、合规角色显式化。
- **可能风险**：作为研究工具，其回测结果可能受 LLM 随机性影响；策略过拟合风险高；不应直接连接实盘账户。

### 3.2 ifixai-ai/iFixAi

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，支持人工或 Agent 自审，120 秒内给出结论。
- **为什么值得关注**：7 日 +5793 星，是本次候选集中 7 日涨星最高的项目。AI Agent 经济中“信任”问题日益突出，金融场景尤其敏感。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 覆盖 `agent-evaluation`、`ai-governance`、`ai-safety`、`eu-ai-act`、`iso-42001`、`nist-ai-rmf`、`owasp-llm`、`prompt-injection`、`risk-management`，说明其审计维度涵盖对齐、幻觉检测、提示注入、合规框架。
- **是否适合借鉴**：强烈建议。金融 Agent 上线前可集成此类审计能力，作为“Agent 上线门禁”。其合规框架映射（EU AI Act、ISO 42001、NIST AI RMF）对企业级落地有直接参考价值。
- **可能风险**：审计工具本身可能产生误报/漏报；不能替代人工合规审查；需验证其对金融领域 Agent 的覆盖深度。

### 3.3 Jakeschincariol/day-trader-skill

- **解决什么问题**：将日内交易研究流程封装为 11 个 Claude 技能，包括扫描数千张图表、跟踪突发新闻、择时进出场、交易前复盘。
- **为什么值得关注**：创建仅约 2 周即获 5817 星，7 日 +2494 星。代表了“交易研究 Agent 化”的新产品形态：不直接下单，而是辅助决策。
- **技术栈/架构亮点**：Python + MIT。topics 为 `backtesting`、`claude`、`claude-skills`、`day-trading`、`stock-market`。核心是技能包（skill）模式，将交易流程拆解为可复用、可组合的 Agent 能力。
- **是否适合借鉴**：适合。可借鉴其“技能包”设计思路，将投研流程（数据获取、图表分析、新闻监控、仓位测算、复盘）标准化为 Agent 技能，便于团队协作和版本管理。
- **可能风险**：营销话术较强；日内交易策略本身高风险；技能包可能依赖外部数据源，存在数据质量和可用性风险；不应将研究输出直接用于实盘。

### 3.4 shiyu-coder/Kronos

- **解决什么问题**：构建金融市场语言的基础模型（Foundation Model），面向金融时序数据的预训练模型。
- **为什么值得关注**：7 日 +3017 星，总星 4.7 万。金融基础模型是当前量化研究的前沿方向，若其模型能力得到验证，可能改变传统因子挖掘范式。
- **技术栈/架构亮点**：Python + MIT。项目描述为“A Foundation Model for the Language of Financial Markets”，暗示将金融时间序列建模为语言任务。具体架构细节在 JSON 中信息不足。
- **是否适合借鉴**：适合作为研究方向跟踪。可关注其模型输入表示、预训练任务设计、下游任务适配方式。
- **可能风险**：金融基础模型存在过拟合、分布漂移、回测幸存者偏差等风险；模型权重和训练数据透明度需进一步验证；维护活跃度需观察（最近 push 为 2026-04-13，距今约 7 个月）。

### 3.5 OpenByteInc/QuantDinger

- **解决什么问题**：提供完整的自托管 Agentic Trading OS，覆盖 AI 研究、Python 策略、因子发现、回测、优化、纸面/实盘多资产执行、风控、监控、MCP、多租户 SaaS。
- **为什么值得关注**：虽然总星仅 1.36 万，但其架构蓝图完整，是本次候选中“最接近企业级 Agent 交易平台”的项目。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 覆盖 `agentic-ai`、`backtesting`、`mcp`、`multi-agent`、`portfolio-management`、`risk-management`、`self-hosted`。强调“可审计栈”（auditable stack），符合金融合规趋势。
- **是否适合借鉴**：非常适合作为架构参考。其“研究-回测-优化-纸面-实盘”的分层设计、MCP 集成、多租户 SaaS 思路，可直接映射到企业级 Agent 交易平台的产品规划。
- **可能风险**：涉及实盘执行和加密资产，风险等级中；需严格审查其风控模块和 API key 管理；自托管部署的运维复杂度高；不应直接使用真实交易所 API key。

### 3.6 HKUDS/Vibe-Trading

- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 能力与算法交易、回测、组合优化结合。
- **为什么值得关注**：来自 HKUDS（香港大学数据科学实验室），学术背景较强。7 日 +624 星，总星 3.78 万。
- **技术栈/架构亮点**：Python + MIT。topics 覆盖 `ai-agent`、`algorithmic-trading`、`backtesting`、`fintech`、`llm`、`mcp`、`multi-agent`、`quantitative-finance`。MCP 集成表明其支持工具化扩展。
- **是否适合借鉴**：适合。学术机构出品的项目通常在方法论上更严谨，可关注其 Agent 决策流程和回测框架设计。
- **可能风险**：研究工具属性强，实盘适用性未经验证；策略过拟合风险；需关注学术项目向生产级演进的维护持续性。

### 3.7 shy3130/tick-stock-panel

- **解决什么问题**：面向 A 股的自托管、零运维量化工作台，支持自建策略、监控、回测，LLM 驱动策略定制、个股分析和复盘。
- **为什么值得关注**：A 股量化工具在开源生态中相对稀缺，该项目 7 日 +746 星，且技术栈现代（DuckDB、Polars、FastAPI、React）。
- **技术栈/架构亮点**：Python + MIT。topics 显示 `duckdb`、`polars`、`fastapi`、`react`、`llm`、`backtesting`、`quant`。DuckDB + Polars 的组合适合本地化、高性能的金融数据处理。
- **是否适合借鉴**：适合。其“本地优先 + 现代数据栈 + LLM 辅助分析”的模式，可作为 A 股或本地化量化研究工具的参考。DuckDB 在金融时序数据上的应用值得深入调研。
- **可能风险**：A 股数据源合规性和稳定性需关注；个人开源项目维护持续性存疑；LLM 生成的策略需严格回测验证。

### 3.8 virattt/ai-hedge-fund

- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 扮演不同角色进行投资研究和决策。
- **为什么值得关注**：总星 6.45 万，是 AI 交易领域的知名项目。虽然近期涨星放缓（7 日 +171），但仍是多 Agent 投研的经典参考。
- **技术栈/架构亮点**：Python + MIT。JSON 中 topics 为空，架构细节信息不足，但从项目定位看，核心是多角色 Agent 协作。
- **是否适合借鉴**：适合作为多 Agent 投研流程的入门参考，尤其适合理解“研究员-交易员-风控”角色分工的工程实现。
- **可能风险**：研究工具属性强；策略表现可能被过度解读；不应直接用于实盘。

### 3.9 JustVugg/colibri

- **解决什么问题**：为前沿 MoE 模型提供分层推理引擎，热专家驻留 GPU（CUDA/Vulkan），温专家驻留 RAM，冷专家从 NVMe 流式加载。
- **为什么值得关注**：7 日 +3516 星，总星 4.85 万。虽然并非金融项目，但其“在现有硬件上运行大模型”的能力对本地化金融 LLM 部署有直接价值。
- **技术栈/架构亮点**：C 语言 + Apache-2.0。核心是 GPU/RAM/NVMe 三级缓存的分层推理架构，强调在消费级硬件上运行前沿 MoE 模型。
- **是否适合借鉴**：适合。若企业希望在本地运行金融 LLM（如 Kronos 类模型）以保护数据隐私，colibri 的分层推理思路可降低硬件门槛。
- **可能风险**：与金融场景无直接关联；C 语言项目的集成成本较高；需评估模型兼容性。

### 3.10 Orkas-AI/Orkas

- **解决什么问题**：本地优先的桌面 AI 团队，Commander 将目标拆解为待办，协调 16 个内置专家 Agent 及 Claude Code、Codex 等外部 Agent。
- **为什么值得关注**：7 日 +4653 星，是本次候选中 7 日涨星第二高的项目。代表了“本地优先 + 多 Agent 编排 + 桌面应用”的新趋势。
- **技术栈/架构亮点**：JavaScript + MIT。topics 覆盖 `agent-orchestration`、`local-first`、`multi-agent`、`self-evolving-agents`、`task-automation`。强调本地运行和自带模型或 BYOK。
- **是否适合借鉴**：适合。其“Commander + 专家 Agent”的编排模式可迁移到金融投研团队协作场景；本地优先架构对数据敏感的金融场景有吸引力。
- **可能风险**：与金融无直接关联；桌面应用形态在企业级场景的扩展性有限；需关注 Agent 自主执行任务时的安全边界。

## 4. 趋势归纳

### 技术趋势

1. **Agent 技能包（Skill Pack）成为新交付单元**：`day-trader-skill`、`trader-skill`、`ui-ux-pro-max-skill`、`logo-design-skill`、`agentic-awesome-skills` 等项目表明，将 Agent 能力封装为可复用、可组合的技能包，正在成为 AI 应用分发的新范式。
2. **本地优先（Local-First）架构加速**：`Orkas`、`locally-uncensored`、`tick-stock-panel`、`colibri` 等项目强调本地运行、数据隐私和低硬件门槛，反映了金融场景对数据主权的强烈需求。
3. **MCP（Model Context Protocol）成为 Agent 工具接入标准**：`QuantDinger`、`Vibe-Trading`、`awesome-mcp-servers`、`awesome-remote-mcp-servers` 等项目均集成或围绕 MCP 构建，MCP 正在成为 Agent 连接数据源和交易工具的事实标准。
4. **现代数据栈进入量化工具**：`tick-stock-panel` 使用 DuckDB + Polars + FastAPI，表明轻量级、高性能的本地数据处理栈正在替代传统重型数据库方案。

### 产品趋势

1. **从“交易 bot”到“交易研究 Agent”**：新项目更强调研究、回测、复盘和人工确认，而非自动下单。`day-trader-skill` 明确“never place an order without your yes”。
2. **Agent 治理与审计产品化**：`iFixAi` 的快速增长表明，Agent 审计、对齐、合规正在成为独立产品品类，金融场景是首要落地领域。
3. **一体化 Agentic Trading OS**：`QuantDinger` 代表的全栈式交易操作系统，将研究、回测、执行、风控、监控整合为单一可审计平台。

### 量化/交易策略趋势

1. **LLM 多角色辩论式决策**：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 均采用多 Agent 角色分工和辩论式决策，替代单一模型预测。
2. **金融基础模型探索**：`Kronos` 代表的方向是将金融时序数据预训练为基础模型，可能改变传统因子挖掘范式。
3. **A 股本地化量化工具兴起**：`tick-stock-panel`、`daily_stock_analysis` 表明 A 股量化工具链正在开源生态中补位。

### AI Agent 与自动化交易结合趋势

1. **人工确认成为默认安全边界**：多个项目明确将“人工确认”作为下单前置条件，反映了对 Agent 自主交易风险的共识。
2. **Agent 审计嵌入交易流程**：`iFixAi` 的审计能力与 `QuantDinger` 的“可审计栈”理念相呼应，Agent 行为审计正在成为交易系统的标配。
3. **技能包降低交易 Agent 门槛**：通过预封装技能，非专业开发者也能快速搭建交易研究 Agent，但这也带来了误用风险。

### 值得后续做原型验证的方向

1. **投研 Agent 技能包框架**：将数据获取、图表分析、新闻监控、仓位测算、复盘等投研流程标准化为可复用技能包。
2. **Agent 审计门禁系统**：在 Agent 上线前集成行为审计、对齐检查、合规映射能力。
3. **本地优先的量化研究工作台**：基于 DuckDB + Polars + FastAPI 构建轻量级、隐私友好的研究环境。
4. **MCP 金融数据网关**：将多源金融数据封装为 MCP 服务器，供不同 Agent 框架统一调用。

## 5. 今日灵感清单

1. **MVP：投研 Agent 技能包**：参考 `day-trader-skill` 和 `trader-skill`，将“数据获取 → 图表分析 → 新闻情绪 → 仓位测算 → 复盘报告”封装为 5-8 个 Claude/Codex 技能，做一个本地运行的投研助手 MVP。
2. **调研：Agent 审计框架**：深入研究 `iFixAi` 的审计维度（对齐、幻觉检测、提示注入、合规映射），评估将其集成到金融 Agent 上线流程的可行性。
3. **原型：MCP 金融数据网关**：参考 `QuantDinger` 和 `awesome-mcp-servers`，将 2-3 个公开金融数据源封装为 MCP 服务器，验证 Agent 统一调用多源数据的能力。
4. **复现：多角色辩论式投研**：基于 `TradingAgents` 的架构思路，用 Codex/Claude 复现一个简化的“研究员-风控-交易员”三角色辩论 demo，验证多 Agent 决策质量。
5. **调研：DuckDB 金融时序性能**：参考 `tick-stock-panel`，测试 DuckDB + Polars 在分钟级行情数据上的查询性能，评估替代传统时序数据库的可行性。
6. **原型：本地金融 LLM 推理**：调研 `colibri` 的分层推理架构，评估在消费级 GPU 上运行 Kronos 类金融基础模型的可行性。
7. **MVP：Agent 交易复盘工具**：参考 `day-trader-skill` 的“replay every outcome”理念，做一个自动记录 Agent 交易决策、回放结果、生成复盘报告的 MVP。
8. **调研：Agent 技能包分发模式**：分析 `agentic-awesome-skills` 的 2926+ 技能库结构，研究技能包的版本管理、依赖解析和发现机制。
9. **原型：本地优先投研工作台**：参考 `Orkas` 的本地优先架构，设计一个数据不出本地的投研 Agent 工作台原型。
10. **Watchlist：金融基础模型**：将 `Kronos` 加入 watchlist，跟踪其模型更新、下游任务适配和社区反馈。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多 Agent 金融交易框架的标杆，社区活跃，适合持续跟踪架构演进 |
| ifixai-ai/iFixAi | Agent 审计赛道高速增长项目，金融 Agent 合规的关键基础设施 |
| shiyu-coder/Kronos | 金融基础模型前沿方向，需观察模型能力和维护活跃度 |
| OpenByteInc/QuantDinger | 最接近企业级 Agentic Trading OS 的架构蓝图，值得跟踪产品化进展 |
| HKUDS/Vibe-Trading | 学术背景的多 Agent 交易框架，方法论参考价值高 |
| shy3130/tick-stock-panel | A 股本地化量化工作台，现代数据栈应用值得关注 |
| Jakeschincariol/day-trader-skill | 交易研究 Agent 技能包的代表，观察技能包模式的演进 |
| JustVugg/colibri | 分层推理引擎，对本地化金融 LLM 部署有潜在价值 |
| Orkas-AI/Orkas | 本地优先多 Agent 编排，观察桌面 Agent 产品形态 |
| virattt/ai-hedge-fund | 经典多 Agent 投研项目，适合作为入门参考和对比基准 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

**额外风险提示**：

- **技能包营销话术风险**：`day-trader-skill`、`trader-skill` 等项目描述具有较强的营销色彩，其“辅助决策”定位可能被误读为“交易信号”，需保持警惕。
- **回测幸存者偏差**：所有回测类项目（`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`tick-stock-panel` 等）的回测结果可能受幸存者偏差、前视偏差和过拟合影响，不应直接作为策略有效性的证据。
- **API Key 安全**：涉及实盘执行的项目（`freqtrade`、`QuantDinger` 等）需严格审查 API key 的存储和权限管理，建议仅使用纸面交易或最小权限测试网。
- **加密资产风险**：`freqtrade`、`QuantDinger`、`OpenBB` 等涉及加密资产的项目，需注意市场波动、流动性、交易所合规和资金安全风险。
- **维护活跃度风险**：`Kronos` 最近 push 为 2026-04-13，距今约 7 个月，需关注其维护状态；`day-trader-skill` 和 `trader-skill` 创建时间极短，长期维护存疑。

## 8. 数据质量说明

- **基线数据**：本次报告使用了 `baseline_1d`（2026-11-05）和 `baseline_7d`（2026-10-29）两个基线文件，1 日和 7 日涨星数据均可用。
- **30 日基线缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法提供 30 日涨星趋势分析。
- **采集失败**：本次候选集中未发现明显的采集失败标记，但部分项目（如 `Kronos`、`day-trader-skill`）的 `pushed_at` 时间较早，需注意其近期活跃度。
- **样本偏差**：候选集通过关键词匹配生成，存在明显的“awesome-list”类聚合仓库误匹配问题（如 `public-apis`、`awesome-selfhosted`、`build-your-own-x`、`awesome-python`、`awesome-go` 等），这些项目与金融/量化直接关联度低，但因其总 star 数高而占据榜单前列。实际金融/量化相关项目的信号可能被稀释。
- **分类噪声**：`category_guess` 字段存在误分类，如 `awesome-selfhosted` 被标记为 `trading_bot`，`build-your-own-x` 被标记为 `trading_bot`，`colibri` 被标记为 `quant_research`，这些分类仅基于关键词匹配，不代表项目真实属性。
- **风险标记噪声**：`risk_flags` 中的 `crypto_related`、`trading_bot` 等标记同样基于关键词匹配，可能对非交易类项目产生误报。
