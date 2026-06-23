# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-06-22

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI Agent 与设计/前端深度融合**：以 `open-design`、`ui-ux-pro-max-skill` 为代表，AI 驱动的 UI/UX 生成工具持续火爆，强调本地优先、多 Agent 协作和设计系统化。
    2.  **LLM 驱动的多市场智能分析**：`daily_stock_analysis` 等项目展示了利用大语言模型整合多源行情、新闻，构建决策看板与自动推送的成熟模式，且强调零成本运行。
    3.  **多 Agent 金融交易框架**：`TradingAgents` 和 `Vibe-Trading` 等项目持续受到关注，表明业界正在积极探索将多智能体协作框架应用于复杂金融决策。
- **新趋势**：出现了“Vibe-Trading”（氛围交易）概念，以及将价值投资大师方法论（如巴菲特、芒格）与 AI Agent 结合的研究框架（`ai-berkshire`），这代表了 AI 在主观投资策略上的新尝试。
- **值得复刻/参考的工程架构**：`nautilus_trader` 的 Rust 原生、确定性事件驱动交易引擎架构，为构建高性能、低延迟交易系统提供了极佳参考。`a-stock-data` 的 7 层全栈数据架构也为金融数据工程提供了清晰蓝图。
- **高风险/过度营销项目**：今日榜单中未发现明显骗局项目，但需警惕部分项目（如 `QuantDinger`、`Vibe-Trading`）将“AI 交易”概念过度简化，可能掩盖真实交易中的复杂性和风险。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 69.4k | +642 | +3770 | TypeScript | fintech_product | 本地优先的开源设计工具，替代 Figma，支持多种 AI 编码代理。 | AI Agent 与设计工具结合的工程范式。 | 低 |
| 2 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 46.1k | +1202 | +3392 | Python | ai_trading, quant_research | LLM 驱动的多市场股票智能分析系统，支持零成本定时运行。 | 多源数据融合、LLM 决策看板与自动推送的架构。 | 低 |
| 3 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 95.2k | +389 | +3011 | Python | fintech_product | 为构建专业多平台 UI/UX 提供设计智能的 AI 技能包。 | AI Skill 模块化设计，赋能编码代理生成专业界面。 | 低 |
| 4 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 518.6k | +380 | +2493 | Markdown | trading_bot | 通过从零重建热门技术来掌握编程的教程集合。 | 从零构建交易系统、数据库等核心组件的学习路径。 | 中 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 92.3k | +228 | +1788 | 无 | crypto_trading, fintech_product | 流行品牌设计系统的 DESIGN.md 文件集合，用于指导 AI 代理生成 UI。 | 设计令牌化、设计系统与 AI Agent 的标准化集成方案。 | 中 |
| 6 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 443.6k | +195 | +1681 | Python | crypto_trading, quant_research | 免费 API 的集体列表。 | 发现可用于金融数据、另类数据源的免费 API。 | 中 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 88.0k | +165 | +1534 | Python | ai_trading, backtesting | 多智能体 LLM 金融交易框架。 | 多 Agent 协作在交易决策、风险管理中的架构设计。 | 低 |
| 8 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 300.7k | +175 | +1238 | 无 | trading_bot | 可自托管的免费软件网络服务和 Web 应用列表。 | 寻找可自托管的金融数据、监控、自动化工具。 | 中 |
| 9 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 304.4k | +165 | +1222 | Python | backtesting, quant_research | 精选的 Python 框架、库、工具和资源列表。 | 发现 Python 在量化、回测、数据分析领域的优秀库。 | 低 |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 61.0k | +164 | +1289 | TypeScript | ai_trading, backtesting | 领先的 Claude 代理元框架，用于部署智能多智能体群。 | 多智能体群、自适应记忆、自学习群智能的工程实现。 | 低 |
| 11 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 117.7k | +118 | +996 | C++ | ai_trading, quant_research | C/C++ 实现的 LLM 推理引擎。 | 在本地或边缘设备部署量化金融模型的推理加速方案。 | 低 |
| 12 | [antirez/ds4](https://github.com/antirez/ds4) | 15.0k | +128 | +983 | C | quant_research | DeepSeek 4 的本地推理引擎，支持 Metal, CUDA, ROCm。 | 高性能 LLM 本地推理在金融数据分析中的应用潜力。 | 低 |
| 13 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 63.3k | +120 | +907 | TypeScript | quant_research | 面向复杂代码库的编码代理框架。 | 复杂金融系统代码库的 AI 辅助开发与维护范式。 | 低 |
| 14 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | 23.8k | +102 | +879 | TypeScript | fintech_product | 固执己见的 OpenClaw/Hermes Agent 大脑。 | 个人 AI Agent 大脑的架构设计，可集成金融信息处理。 | 低 |
| 15 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 13.1k | +139 | +788 | Python | ai_trading, backtesting | “Vibe-Trading: 你的个人交易代理”。 | “氛围交易”概念，探索非结构化数据与 AI 交易决策的结合。 | 中 |
| 16 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 176.2k | +95 | +610 | Go | backtesting, crypto_trading | 精选的 Go 框架、库和软件列表。 | 发现用 Go 构建高性能交易、回测系统的优秀库。 | 中 |
| 17 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | 5.2k | +88 | +556 | 无 | trading_infra | A股全栈数据工具包，7层架构，28端点，13数据源。 | 金融数据工程的分层架构设计，多源异构数据整合方案。 | 低 |
| 18 | [NVIDIA/skills](https://github.com/NVIDIA/skills) | 1.7k | +203 | +451 | Python | quant_research | NVIDIA 发布的 AI Agent 技能。 | 硬件厂商官方发布的 Agent 技能，可集成到金融分析 Agent 中。 | 低 |
| 19 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 30.9k | +81 | +554 | Python | backtesting, quant_research | 金融市场语言的基础模型。 | 金融领域的专用基础模型，用于市场预测和策略生成。 | 低 |
| 20 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | 8.6k | +66 | +484 | Python | ai_trading, backtesting | 面向加密货币、股票和外汇的 AI 量化交易平台。 | 集回测、实盘、数据、多 Agent 研究于一体的平台架构。 | 中 |

## 3. 重点项目深度分析

### 1. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) (排名 2)
- **解决问题**：为投资者提供一个零成本、全自动的多市场股票智能分析工具，整合行情、新闻，并生成决策看板。
- **为何值得关注**：24小时涨星 +1202，7日涨星 +3392，增长迅猛。它代表了 LLM 在个人投资决策辅助上的成熟应用，强调“零成本定时运行”，降低了使用门槛。
- **技术栈/架构亮点**：Python 构建，集成多源行情和实时新闻，利用 LLM 进行分析，并通过看板和自动推送呈现结果。其架构模式（数据采集 -> LLM 分析 -> 决策呈现 -> 自动推送）非常清晰，值得借鉴。
- **借鉴价值**：高。其“多源数据融合 + LLM 分析 + 自动化报告”的流水线模式，可直接应用于企业级投研 Agent 的构建。
- **可能的风险**：LLM 分析结果可能存在幻觉，直接用于投资决策有风险。依赖的外部数据源可能不稳定。

### 2. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) (排名 7)
- **解决问题**：提供一个多智能体协作的 LLM 金融交易框架，模拟不同角色的分析师共同决策。
- **为何值得关注**：总 star 数高达 88k，持续受到关注。它是多 Agent 架构在金融交易领域的标杆项目，探索了超越单一模型决策的复杂协作模式。
- **技术栈/架构亮点**：Python 编写，基于 LangChain 等框架，定义了多个 Agent 角色（如基本面分析师、技术分析师、交易员、风控经理），通过辩论和协作生成最终交易信号。
- **借鉴价值**：极高。其多 Agent 角色定义、协作流程、消息传递机制，是构建企业级 AI 交易决策系统的核心参考。
- **可能的风险**：策略过拟合风险，回测表现可能无法在实盘中复现。多 Agent 交互增加了系统复杂度和延迟。

### 3. [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) (排名 15)
- **解决问题**：提出“Vibe-Trading”（氛围交易）概念，旨在利用 AI 捕捉市场情绪、新闻等非结构化数据中的交易机会。
- **为何值得关注**：概念新颖，代表了 AI 交易从结构化数据向非结构化“氛围”数据拓展的趋势。由学术机构（HKUDS）发布，具有一定研究价值。
- **技术栈/架构亮点**：Python 项目，集成了 MCP、多 Agent 和回测功能。其核心在于如何定义和量化“氛围”，并将其转化为交易信号。
- **借鉴价值**：高。为探索另类数据（新闻情绪、社交媒体舆情）在量化策略中的应用提供了新思路和原型。
- **可能的风险**：“氛围”的定义和量化非常主观，策略有效性难以验证，存在严重的过拟合风险。项目较新，成熟度有待观察。

### 4. [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) (排名 35)
- **解决问题**：提供一个生产级的、基于 Rust 的高性能、确定性事件驱动交易引擎。
- **为何值得关注**：7日涨星 +605，增长显著。Rust 语言在金融交易基础设施领域的应用是明确的趋势，该项目是这一趋势的杰出代表，强调“生产级”和“确定性”。
- **技术栈/架构亮点**：核心由 Rust 编写，保证了内存安全和极致性能。采用确定性事件驱动架构，这对于回测的准确性和实盘的一致性至关重要。支持 Python 绑定，兼顾开发效率。
- **借鉴价值**：极高。对于需要构建低延迟、高可靠性交易系统的团队，其架构设计、事件处理机制和 Rust 实现是顶级参考。
- **可能的风险**：Rust 学习曲线陡峭。项目复杂度高，二次开发难度大。

### 5. [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) (排名 17)
- **解决问题**：为 A 股市场提供一套全栈数据工具包，解决多源数据获取、清洗和整合的痛点。
- **为何值得关注**：24h 涨星 +88，7d 涨星 +556，对于一个较新的项目增长迅速。其“7层架构 · 28端点 · 13数据源”的设计理念非常清晰，是金融数据工程的优秀范例。
- **技术栈/架构亮点**：明确的分层架构设计，覆盖行情、研报、资金面、筹码、公告等多种数据类型。这种架构化思维对于构建任何金融数据平台都至关重要。
- **借鉴价值**：极高。其分层架构和端点设计可直接作为构建金融数据中台的蓝图，无论是针对 A 股还是其他市场。
- **可能的风险**：数据源可能涉及合规性问题。项目较新，长期维护的稳定性有待观察。

### 6. [microsoft/qlib](https://github.com/microsoft/qlib) (排名 22)
- **解决问题**：提供一个面向 AI 的量化投资平台，覆盖从研究到生产的全流程。
- **为何值得关注**：微软出品，长期维护，生态完善。它不仅是回测框架，更是一个集数据、模型、策略、执行于一体的平台，并已集成 `RD-Agent` 实现自动化研发。
- **技术栈/架构亮点**：Python 生态，支持多种 ML 建模范式（监督学习、市场动态建模、强化学习）。其数据框架和模型管理设计是工业级标准。
- **借鉴价值**：极高。是构建企业级量化投研平台的直接参考，特别是其将 AI 自动化研发流程（RD-Agent）集成的思路，代表了未来方向。
- **可能的风险**：项目庞大，学习成本高。部分高级功能可能与其内部生态绑定。

### 7. [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) (排名 48)
- **解决问题**：将巴菲特、芒格等价值投资大师的方法论与 AI Agent 结合，创建一个基于 Claude Code 的价值投资研究框架。
- **为何值得关注**：24h 涨星 +70，对于一个仅 106 star 的项目来说增速惊人。它代表了 AI 在主观投资策略上的创新应用，尝试将非结构化的投资哲学系统化、自动化。
- **技术栈/架构亮点**：基于 Claude Code，利用多 Agent 并行研究，模拟大师的分析视角。这是一个将领域知识与 AI Agent 深度结合的典范。
- **借鉴价值**：高。为如何将复杂的、经验驱动的投资框架（如基本面分析、护城河分析）转化为 AI Agent 可执行的任务提供了原型。
- **可能的风险**：价值投资理念的量化难度极高，AI 可能只是机械地套用模板，无法真正理解商业本质。项目极度依赖 Claude Code。

## 4. 趋势归纳
- **技术趋势**：
    - **Rust 在交易基础设施中的崛起**：`nautilus_trader` 等项目表明，Rust 因其性能和安全性，正成为构建交易引擎、回测系统等底层设施的首选语言之一。
    - **本地 LLM 推理的加速**：`llama.cpp`、`ds4`、`Rapid-MLX` 等项目持续火热，显示在本地/边缘设备上高效运行大模型的需求旺盛，这对金融数据隐私和低延迟应用至关重要。
    - **AI Agent 技能化、模块化**：`NVIDIA/skills`、`Orchestra-Research/AI-Research-SKILLs` 等项目显示，AI Agent 的能力正在被封装为可复用、可组合的“技能”，这将成为构建复杂金融 Agent 的基础。
- **产品趋势**：
    - **“Vibe-Coding” 向 “Vibe-Trading” 延伸**：从 AI 辅助编程到 AI 辅助交易，概念正在迁移，强调用自然语言和直觉驱动复杂任务。
    - **设计系统与 AI Agent 的深度融合**：`open-design`、`awesome-design-md` 等项目火爆，表明将设计令牌、设计系统标准化，让 AI Agent 生成一致、专业的 UI，已成为成熟的产品模式，可被金融类产品借鉴。
- **量化/交易策略趋势**：
    - **多 Agent 协作决策成为主流**：`TradingAgents`、`Vibe-Trading` 等项目均采用多 Agent 架构，模拟团队分工与协作，以应对复杂市场。
    - **非结构化数据策略化**：从“氛围交易”到“价值投资 AI 化”，业界正积极探索将新闻情绪、社交舆情、投资哲学等非结构化信息转化为可执行的交易策略。
- **AI Agent 与自动化交易结合趋势**：
    - **从单点分析到全流程覆盖**：`OpenAlice` 等项目尝试覆盖从研究、入场、管理到退出的交易全生命周期。
    - **Agent 大脑与工具分离**：`gbrain` 等项目专注于构建 Agent 的“大脑”（决策逻辑），而将工具（数据获取、订单执行）作为可插拔模块，架构更清晰。
- **值得后续做原型验证的方向**：
    - 基于 `a-stock-data` 的分层架构，构建一个支持多市场的金融数据中台 MVP。
    - 参考 `TradingAgents` 的架构，设计一个专注于特定策略（如套利、趋势跟踪）的多 Agent 协作原型。
    - 利用 `llama.cpp` 或 `ds4`，探索在本地部署量化金融微调模型，进行隐私敏感的策略研究。

## 5. 今日灵感清单
1.  **构建“金融数据中台”MVP**：参考 `a-stock-data` 的 7 层架构，用 Python 快速搭建一个支持 A 股/美股的多源数据聚合、清洗和存储原型，对外提供统一 API。
2.  **复现“多 Agent 投研会议”Demo**：借鉴 `TradingAgents`，用 LangChain/CrewAI 创建 3-4 个角色（宏观分析师、行业分析师、技术分析师、风控官），针对同一标的进行辩论并生成报告。
3.  **调研“氛围交易”因子**：基于 `Vibe-Trading` 的概念，利用 `public-apis` 中的新闻 API，设计一个简单的新闻情绪评分因子，并在 `qlib` 或 `freqtrade` 中进行单因子回测。
4.  **为 Codex/Agent 编写金融数据技能包**：参考 `NVIDIA/skills` 和 `Orchestra-Research/AI-Research-SKILLs` 的格式，为你的编码 Agent 编写一个 `financial-data-fetcher` 技能，使其能直接获取行情数据。
5.  **体验 Rust 交易引擎**：克隆 `nautilus_trader` 仓库，运行其示例回测和模拟交易，深入理解其事件驱动架构和 Rust 在金融领域的应用优势。
6.  **设计一个“AI 价值投资”研究模板**：参考 `ai-berkshire`，为 Claude Code 或 Codex 设计一套提示词模板，引导 AI 从护城河、管理层、财务健康度等维度分析一家公司。
7.  **搭建本地量化 LLM 推理环境**：使用 `llmfit` 或 `whichllm` 工具，在你的本地硬件上寻找并部署一个最适合金融文本分析的小型 LLM，测试其推理速度和准确性。
8.  **将 `open-design` 模式用于金融 Dashboard**：研究 `open-design` 如何将设计系统与 AI Agent 结合，思考如何为你的量化策略快速生成一个专业的监控 Dashboard。
9.  **集成 `langfuse` 监控 AI 交易决策**：如果你正在开发 AI 交易 Agent，将 `langfuse` 集成进去，用于追踪 LLM 的每次调用、延迟、成本和决策逻辑，实现可观测性。
10. **调研 `OpenBB` 的 Agent 集成方案**：`OpenBB` 已将自己定位为分析师和 AI Agent 的数据平台，深入研究其如何为 Agent 提供标准化的金融数据接口。

## 6. Watchlist 建议
- **[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**：LLM 在个人投研自动化上的标杆项目，增长极快，架构清晰，值得长期跟踪其功能演进。
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)**：多 Agent 金融交易框架的标杆，是研究 AI 协作决策机制的重要参考。
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)**：概念新颖，代表了非结构化数据策略化的前沿探索，具有学术研究价值。
- **[nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader)**：Rust 在金融交易基础设施领域的顶级实践，是学习高性能、高可靠性系统设计的绝佳案例。
- **[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**：金融数据工程的优秀架构范例，其分层设计思想具有普适性，项目处于早期，发展潜力大。
- **[xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)**：AI 与主观投资策略结合的创新尝试，虽然早期但方向独特，值得关注其能否将投资哲学有效量化。
- **[NVIDIA/skills](https://github.com/NVIDIA/skills)**：硬件巨头官方发布的 Agent 技能，其标准和规范可能成为未来 AI Agent 能力定义的事实标准。
- **[shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)**：金融领域的专用基础模型，如果成功，可能会像 LLaMA 对 NLP 一样，深刻改变金融 AI 的研发范式。

## 7. 风险提醒
- **GitHub star 不是投资建议**：高星项目不代表其策略能盈利，star 数更多反映的是社区关注度和项目热度。
- **不运行未知 trading bot**：对于榜单中出现的 `freqtrade`、`QuantDinger` 等交易机器人，切勿在未完全理解其代码逻辑和风险的情况下直接连接交易所进行实盘交易。
- **不泄露交易所 API key**：任何要求提供交易所 API key 的开源项目都存在极高的安全风险，可能导致资产被盗。
- **注意策略风险**：马丁、网格、套利、杠杆类策略（`nautilus_trader` 等项目中可能涉及）存在巨大爆仓风险，回测表现优异不等于实盘有效。
- **注意回测幸存者偏差和过拟合**：`TradingAgents`、`Vibe-Trading` 等 AI 策略框架极易产生过拟合，回测结果可能无法在未来的未知市场中复现。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
- **基线数据**：本次报告使用了 `2026-06-21` 的 1 日基线和 `2026-06-15` 的 7 日基线数据，涨星数据可靠。
- **采集状态**：本次共采集 53 个项目，数据采集成功，未发现明显失败或异常。
- **样本偏差**：项目筛选基于关键词匹配和 topic 过滤，可能偏向于近期活跃、描述中包含特定术语的项目，对于低调但高质量的项目可能存在遗漏。部分项目因关键词匹配（如 `build-your-own-x` 匹配到 "trading bot"）而被收录，其核心主题可能并非金融/量化，分析时已做区分。
