# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-06-25

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI Agent 驱动的投资研究框架**：以 `ai-berkshire` 和 `daily_stock_analysis` 为代表，将 LLM 多智能体协作应用于价值投资、多市场股票分析，形成决策看板与自动推送。
    2.  **量化交易与回测平台**：`TradingAgents`、`Vibe-Trading`、`QuantDinger` 等项目持续火热，强调多智能体、多市场（股票/加密货币/外汇）覆盖，以及回测与实盘一体化。
    3.  **AI 辅助设计/开发工具**：`open-design`、`ui-ux-pro-max-skill` 等本地优先、Agent 驱动的设计工具增长迅猛，虽非直接金融项目，但其“Vibe Coding”和 Agent Skills 架构对金融终端 UI 和自动化工作流有重要借鉴意义。
- **新趋势**：出现了将“价值投资大师方法论”与“多 Agent 对抗分析”深度结合的 AI 原生研究框架（`ai-berkshire`），以及专门针对信用风险的 AI Agent（`marvis-risk-agent`），标志着 AI 在金融领域的应用从通用交易向专业细分领域（风控、基本面研究）渗透。
- **值得复刻/参考的工程架构**：
    -   `daily_stock_analysis` 的“零成本定时运行”多源数据聚合与 LLM 分析架构。
    -   `ai-berkshire` 的多 Agent 并行研究、对抗分析框架。
    -   `tickflow-stock-panel` 的“自托管、零运维”量化工作台设计，结合 DuckDB 和 Polars 的现代数据处理栈。
- **高风险项目警示**：`Polymarket-Arbitrage-Trading-Bot-Python` 存在明显的过度营销（描述中关键词大量重复堆砌），且为典型的预测市场套利机器人，风险极高，应避免使用。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|:---:|:---|:---:|:---:|:---:|:---:|:---|:---|:---|:---:|
| 1 | codecrafters-io/build-your-own-x | 519.7k | +388 | +2569 | Markdown | 教程/列表 | 通过复现技术来学习编程的教程集合 | 学习交易系统、数据库等底层实现 | 中 |
| 2 | nexu-io/open-design | 71.3k | +524 | +3734 | TypeScript | AI设计/Agent | 本地优先的开源 AI 设计工具，支持多种 Agent | AI 驱动的金融终端 UI/原型设计 | 低 |
| 3 | ZhuLinsen/daily_stock_analysis | 49.7k | +855 | +6533 | Python | AI交易/量化 | LLM 驱动的多市场股票智能分析与决策看板 | 零成本自动化投研与信号推送架构 | 低 |
| 4 | nextlevelbuilder/ui-ux-pro-max-skill | 96.6k | +402 | +2894 | Python | AI设计/Agent | 为构建专业 UI/UX 提供设计智能的 AI Skill | 金融产品 UI 生成与 Agent 技能设计 | 低 |
| 5 | xbtlin/ai-berkshire | 2.2k | +843 | +2190 | Python | AI交易/金融产品 | 基于 Claude Code 的价值投资多 Agent 研究框架 | 大师方法论驱动的 Agent 投研框架 | 低 |
| 6 | VoltAgent/awesome-design-md | 93.3k | +390 | +1926 | - | 设计系统/Agent | 品牌设计系统分析集合，供编码 Agent 生成 UI | 为金融 Agent 注入品牌级 UI 生成能力 | 中 |
| 7 | public-apis/public-apis | 444.3k | +198 | +1627 | Python | API/资源 | 免费 API 集合列表 | 发现金融数据、另类数据 API | 中 |
| 8 | TauricResearch/TradingAgents | 88.6k | +212 | +1312 | Python | AI交易/回测 | 多智能体 LLM 金融交易框架 | 多 Agent 协作的交易策略研发范式 | 低 |
| 9 | awesome-selfhosted/awesome-selfhosted | 301.2k | +182 | +1242 | - | 自托管/列表 | 可自托管的免费软件网络服务列表 | 自建金融数据、监控、自动化服务 | 中 |
| 10 | ruvnet/ruflo | 61.5k | +189 | +1290 | TypeScript | AI Agent/框架 | 领先的 Agent 元框架，用于部署多智能体集群 | 构建复杂金融 Agent 工作流的框架参考 | 低 |
| 11 | vinta/awesome-python | 304.8k | +149 | +1191 | Python | 资源/列表 | Python 框架、库、工具和资源列表 | 寻找量化交易、数据分析相关 Python 库 | 低 |
| 12 | ggml-org/llama.cpp | 118.2k | +148 | +943 | C++ | LLM推理 | C/C++ 实现的 LLM 推理引擎 | 金融领域本地化、低延迟 LLM 部署 | 低 |
| 13 | code-yeongyu/oh-my-openagent | 63.6k | +102 | +916 | TypeScript | AI Agent/工具 | 面向复杂代码库的编码 Agent 工具 | 复杂量化系统代码的 Agent 辅助开发 | 低 |
| 14 | garrytan/gbrain | 24.1k | +99 | +728 | TypeScript | AI Agent | 个人定制的 Agent 大脑 | 个性化金融 Agent 助手的设计思路 | 低 |
| 15 | antirez/ds4 | 15.4k | +83 | +836 | C | LLM推理 | DeepSeek 4 本地推理引擎 | 高性能、本地化的金融 LLM 应用部署 | 低 |
| 16 | avelino/awesome-go | 176.4k | +90 | +606 | Go | 资源/列表 | Go 语言框架、库和软件精选列表 | 寻找高性能交易系统、订单簿相关 Go 库 | 中 |
| 17 | simonlin1212/a-stock-data | 5.6k | +142 | +672 | - | 交易基础设施 | A股全栈数据工具包，覆盖行情/研报/资金面等 | A股多源数据聚合与标准化处理架构 | 低 |
| 18 | HKUDS/Vibe-Trading | 13.3k | +79 | +713 | Python | AI交易/回测 | “Vibe-Trading”个人交易 Agent | 探索自然语言驱动的交易 Agent 交互模式 | 中 |
| 19 | shiyu-coder/Kronos | 31.3k | +88 | +609 | Python | 量化研究/基础模型 | 金融市场语言的基础模型 | 金融时序数据的预训练模型应用 | 低 |
| 20 | imbue-bit/AlphaGPT | 2.5k | +130 | +336 | Python | 量化研究 | 基于深度强化学习的开源自动因子工厂 | 自动化因子挖掘与强化学习结合 | 低 |
| 21 | langfuse/langfuse | 29.8k | +63 | +434 | TypeScript | AI工程/LLMOps | 开源 AI 工程平台，LLM 评估与可观测性 | 金融 AI Agent 的追踪、评估与监控 | 低 |
| 22 | punkpeye/awesome-mcp-servers | 89.8k | +59 | +379 | - | MCP/资源 | MCP 服务器集合 | 为金融 Agent 发现和集成数据、工具 | 中 |
| 23 | brokermr810/QuantDinger | 8.8k | +43 | +535 | Python | AI交易/回测 | AI 量化交易平台，支持多市场与多 Agent 研究 | 多市场、多资产类别的统一交易平台架构 | 中 |
| 24 | ripienaar/free-for-dev | 123.5k | +69 | +263 | HTML | 资源/列表 | 面向开发者的免费 SaaS/PaaS/IaaS 列表 | 寻找金融应用开发可用的免费云资源 | 低 |
| 25 | OthmanAdi/planning-with-files | 24.0k | +58 | +368 | Python | AI Agent/规划 | 为 AI 编码 Agent 设计的持久化文件规划系统 | 金融 Agent 长周期任务的可靠规划与状态管理 | 低 |
| 26 | NVIDIA/skills | 1.9k | +37 | +543 | Python | AI Agent/技能 | NVIDIA 发布的 AI Agent 技能集 | 官方 Agent 技能设计规范与最佳实践 | 低 |
| 27 | AlexsJones/llmfit | 28.6k | +40 | +339 | Rust | LLM工具 | 一键查找适合你硬件的模型 | 为本地化金融 LLM 应用选择最优模型 | 低 |
| 28 | VoltAgent/awesome-claude-code-subagents | 22.4k | +49 | +340 | Shell | AI Agent/资源 | 100+ 专业 Claude Code 子 Agent 集合 | 金融领域专用子 Agent 的设计灵感 | 低 |
| 29 | OpenBB-finance/OpenBB | 69.7k | +45 | +284 | Python | 金融数据/量化 | 面向分析师、量化研究员和 AI Agent 的金融数据平台 | 统一的金融数据获取与分析平台 | 中 |
| 30 | Fincept-Corporation/FinceptTerminal | 27.5k | +32 | +382 | C++ | 金融终端/量化 | 现代金融应用，提供高级市场分析和投资研究工具 | 类似 Bloomberg 的开源金融终端架构 | 低 |
| 31 | microsoft/qlib | 45.2k | +40 | +387 | Python | 量化投资/AI | 微软开源的 AI 量化投资平台 | 从研究到生产的全流程 AI 量化框架 | 低 |
| 32 | freqtrade/freqtrade | 51.8k | +29 | +247 | Python | 加密货币/交易机器人 | 免费开源的加密货币交易机器人 | 成熟的策略回测与实盘交易框架参考 | 中 |
| 33 | Orchestra-Research/AI-Research-SKILLs | 10.1k | +42 | +266 | TeX | AI研究/技能 | 全面的 AI 研究和工程技能库 | 将 Agent 武装成 AI 研究员的知识库设计 | 低 |
| 34 | Andyyyy64/whichllm | 5.3k | +32 | +303 | Python | LLM工具 | 查找并运行最适合你硬件的本地 LLM | 为本地量化分析选择最佳性价比模型 | 低 |
| 35 | edison7009/EchoBird | 2.6k | +31 | +331 | Rust | 工具 | 一键安装所有 | 简化开发环境部署的工具思路 | 低 |
| 36 | RyanCodrai/turbovec | 12.2k | +26 | +265 | Python | 向量索引/量化 | 基于 TurboQuant 构建的向量索引 | 高性能向量搜索在量化因子/相似K线中的应用 | 低 |
| 37 | nidhinjs/prompt-master | 9.8k | +25 | +277 | - | AI/提示工程 | 为任何 AI 工具编写精准提示的 Claude Skill | 提升金融 Agent 指令精准度与效率 | 低 |
| 38 | lsdefine/GenericAgent | 13.1k | +29 | +129 | Python | AI Agent/自动化 | 自进化 Agent，从种子代码成长为全系统控制 | 自进化 Agent 在动态金融市场中的适应能力 | 低 |
| 39 | Developer-Y/cs-video-courses | 81.9k | +26 | +80 | - | 课程/资源 | 计算机科学视频课程列表 | 系统学习量化金融、算法交易相关 CS 基础 | 中 |
| 40 | josephmisiti/awesome-machine-learning | 73.0k | +20 | +117 | Python | 机器学习/资源 | 精选机器学习框架、库和软件列表 | 寻找适用于金融预测的 ML 工具和库 | 低 |
| 41 | elementalsouls/Claude-BugHunter | 2.7k | +34 | +165 | Python | 安全/Agent | 用于漏洞挖掘和红队工作的 Claude Code 技能包 | 金融系统安全测试与 Agent 驱动的渗透测试 | 低 |
| 42 | shy3130/tickflow-stock-panel | 308 | +83 | - | TypeScript | 量化/回测 | 自托管、零运维的 A 股量化工作台 | 现代数据栈（DuckDB/Polars）在量化中的应用 | 低 |
| 43 | eddyzzl/marvis-risk-agent | 315 | +99 | - | Python | 风控/Agent | 全能信用风险 Agent，覆盖模型开发到策略工作流 | 专业风控领域的 AI Agent 架构设计 | 低 |
| 44 | Z4nzu/hackingtool | 77.8k | +34 | +196 | Python | 安全/工具 | 黑客工具集合 | 了解系统安全与攻击面，增强交易系统防护意识 | 低 |
| 45 | ByteByteGoHq/system-design-101 | 83.8k | +128 | +237 | - | 系统设计/教育 | 用可视化和简单术语解释复杂系统 | 学习高可用、低延迟交易系统的设计原则 | 低 |
| 46 | rust-unofficial/awesome-rust | 58.0k | +13 | +97 | Rust | 资源/列表 | Rust 代码和资源精选列表 | 寻找用 Rust 构建高性能交易组件的库 | 低 |
| 47 | fffaraz/awesome-cpp | 72.0k | +5 | +106 | - | 资源/列表 | C/C++ 框架、库和资源精选列表 | 寻找低延迟交易系统开发所需的 C++ 库 | 低 |
| 48 | charlax/professional-programming | 51.2k | -1 | +41 | Python | 资源/学习 | 面向软件工程师的学习资源集合 | 提升金融软件工程素养与实践 | 中 |
| 49 | Rolymarket/Polymarket-Arbitrage-Trading-Bot-Python | 251 | +92 | - | - | 套利/交易机器人 | Polymarket 套利交易机器人 | 无（高风险过度营销项目） | 中 |
| 50 | vuejs/awesome-vue | 73.6k | +1 | -5 | - | 资源/列表 | Vue.js 相关精选列表 | 为金融数据看板寻找 Vue.js 生态组件 | 低 |

## 3. 重点项目深度分析

### 3.1. `ZhuLinsen/daily_stock_analysis` (排名 3)
-   **项目解决什么问题**：解决散户或小型机构缺乏多源市场数据整合、实时新闻分析及自动化决策辅助工具的问题。它利用 LLM 对 A 股等多市场股票进行智能分析，生成决策看板并自动推送。
-   **为什么最近值得关注**：24 小时涨星 +855，7 日涨星 +6533，增长极为迅猛。其“零成本定时运行”的特性降低了使用门槛，契合了当前 AI 赋能个人投资者的热潮。
-   **技术栈/架构亮点**：Python 编写，集成了多源行情、实时新闻、LLM 分析、决策看板与自动推送。架构上强调数据聚合、AI 分析、结果分发的一体化流程。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其“多源数据聚合 -> LLM 分析 -> 决策辅助”的管道架构，可直接复刻为企业级投研 Agent 的基础工作流。零成本运行方案对成本敏感型创业项目有参考价值。
-   **可能的风险**：依赖外部数据源和 LLM 接口的稳定性；分析结果可能存在幻觉，直接用于交易决策有风险；需注意数据合规性。

### 3.2. `xbtlin/ai-berkshire` (排名 5)
-   **项目解决什么问题**：将巴菲特、芒格等四位投资大师的方法论系统化、代码化，通过多 Agent 并行研究和对抗分析，辅助用户进行深度价值投资研究。
-   **为什么最近值得关注**：24 小时涨星 +843，对于一个较新的项目（2026年4月创建）来说增速惊人。它代表了 AI 在投资领域从量化交易向基本面深度研究的范式拓展。
-   **技术栈/架构亮点**：基于 Claude Code 构建，采用多 Agent 并行与对抗分析架构。核心是将投资哲学转化为 Agent 可执行的指令和协作流程。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：极具借鉴意义。其“大师方法论 + 多 Agent 对抗”的模式，可以推广到任何需要深度分析和多方论证的金融决策场景，如信用评估、项目尽调等。
-   **可能的风险**：方法论的有效性高度依赖于提示词工程和 Agent 协作逻辑的设计；分析结果可能过于理论化，与市场短期行为脱节；存在策略过拟合历史案例的风险。

### 3.3. `TauricResearch/TradingAgents` (排名 8)
-   **项目解决什么问题**：提供一个多智能体 LLM 金融交易框架，旨在模拟不同角色的交易员（如基本面分析师、技术分析师、风险管理者）协同工作，以做出更全面的交易决策。
-   **为什么最近值得关注**：作为多智能体交易框架的先行者，持续保持高热度（总 star 88.6k），7 日涨星 +1312，表明市场对复杂 Agent 交易系统的需求旺盛。
-   **技术栈/架构亮点**：Python 编写，Apache-2.0 协议。核心是定义多个具有不同专长和分析视角的 Agent，并设计它们之间的协作与通信机制。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：是研究多 Agent 协作交易系统的绝佳范本。其角色定义、消息传递、决策融合等机制可直接用于构建更复杂的金融 Agent 集群。
-   **可能的风险**：多 Agent 系统复杂度高，调试困难；LLM 的幻觉和不确定性可能在多轮协作中被放大；回测结果可能无法反映真实市场中的 Agent 交互延迟和成本。

### 3.4. `HKUDS/Vibe-Trading` (排名 18)
-   **项目解决什么问题**：探索一种更直观、自然的交易交互方式，用户可能通过自然语言描述交易想法（“Vibe”），由 Agent 解析并执行策略研究、回测甚至交易。
-   **为什么最近值得关注**：代表了“Vibe Coding”思想在交易领域的延伸，降低了量化交易的门槛。由香港大学（HKUDS）开发，具有一定的学术背景。
-   **技术栈/架构亮点**：Python 编写，集成了 LLM、MCP、回测和多 Agent 技术。其核心是将非结构化的自然语言意图转化为结构化的交易操作。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其自然语言到交易策略的转换接口设计，是下一代智能交易终端的核心交互范式，值得深入研究。
-   **可能的风险**：自然语言理解的歧义性可能导致非预期的交易行为；策略生成过程不透明，难以进行风险归因；过度简化可能导致用户忽视交易风险。

### 3.5. `shy3130/tickflow-stock-panel` (排名 42)
-   **项目解决什么问题**：提供一个自托管、零运维的 A 股量化工作台，集成了选股、监控和回测功能，旨在降低个人量化投资者的基础设施成本。
-   **为什么最近值得关注**：虽然总 star 数不高（308），但 24 小时涨星 +83，显示出强劲的初期增长势头。其“自托管、零运维”的理念和现代技术栈选型非常吸引人。
-   **技术栈/架构亮点**：TypeScript 编写，技术栈非常现代化，使用了 DuckDB（嵌入式分析数据库）、Polars（高性能 DataFrame 库）、FastAPI 和 React。基于 TickFlow 数据。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其“DuckDB + Polars”的组合是构建轻量级、高性能本地量化分析平台的绝佳范例，可以替代笨重的传统数据库和 Pandas，值得在原型验证中采用。
-   **可能的风险**：项目非常早期，功能可能不完善，存在较多 Bug；依赖 TickFlow 数据生态，数据源可能受限；社区较小，维护活跃度有待观察。

### 3.6. `eddyzzl/marvis-risk-agent` (排名 43)
-   **项目解决什么问题**：专注于信用风险领域，提供一个覆盖模型开发、验证、数据处理、特征工程和策略工作流的全能 AI Agent。
-   **为什么最近值得关注**：24 小时涨星 +99，是榜单中唯一一个专门针对“信用风险”这一垂直领域的 AI Agent 项目。这标志着 AI Agent 在金融领域的应用开始走向深度专业化。
-   **技术栈/架构亮点**：Python 编写。其架构亮点在于将信用风险管理中碎片化的工作流（开发、验证、特征、策略）整合到一个统一的 Agent 框架中。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常有价值。它为如何构建面向特定金融业务领域（如风控、合规、投行）的“全流程 Agent”提供了设计蓝图。
-   **可能的风险**：项目极度早期（Forks 为 0），代码成熟度低；信用风险模型对准确性和可解释性要求极高，Agent 的“黑箱”特性可能成为应用障碍；合规风险高。

### 3.7. `imbue-bit/AlphaGPT` (排名 20)
-   **项目解决什么问题**：利用深度强化学习技术，自动化地挖掘和生成有效的量化交易因子（Alpha），旨在解决传统人工挖因子效率低、覆盖度不足的问题。
-   **为什么最近值得关注**：24 小时涨星 +130，增长迅速。自动化因子挖掘是量化投资领域的圣杯之一，结合深度强化学习的方法代表了前沿方向。
-   **技术栈/架构亮点**：Python 编写，基于深度学习（Transformer 等）和强化学习。其核心是一个“因子工厂”的自动化流水线。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其自动化因子挖掘的流程可以集成为一个专业的“因子挖掘 Agent”，挂载到更庞大的量化投研 Agent 系统中。
-   **可能的风险**：强化学习训练不稳定，容易挖掘出过拟合、无经济学意义的“噪音”因子；计算资源消耗巨大；因子有效性衰减快，需要持续迭代。

### 3.8. `brokermr810/QuantDinger` (排名 23)
-   **项目解决什么问题**：试图构建一个覆盖加密货币、股票、外汇的全品类 AI 量化交易平台，提供回测、实盘、市场数据和多 Agent 研究的一站式解决方案。
-   **为什么最近值得关注**：其“大一统”的平台野心和多市场覆盖吸引了关注，7 日涨星 +535。整合了多个热门概念（AI、多Agent、多市场）。
-   **技术栈/架构亮点**：Python 编写，集成了 Alpaca、Binance、Coinbase、MT5 等多个交易所接口。架构上强调插件化和多市场适配。
-   **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其多交易所、多资产类别的统一接口抽象层设计值得参考，可以简化开发跨市场交易策略的复杂度。
-   **可能的风险**：项目试图覆盖过多功能，可能导致每个部分都不够深入和稳定；依赖众多第三方交易所 API，维护成本高，断连风险大；策略在多个差异巨大的市场间迁移可能存在严重过拟合。

## 4. 趋势归纳
-   **技术趋势**：
    -   **多 Agent 协作架构成为主流**：从 `TradingAgents` 到 `ai-berkshire`，再到 `Vibe-Trading`，通过多个角色分工的 LLM Agent 协同完成复杂金融任务已成为共识。
    -   **现代数据处理栈兴起**：以 `tickflow-stock-panel` 为代表，DuckDB、Polars 等新兴高性能、嵌入式数据分析工具开始替代传统 Pandas + 重型数据库组合。
    -   **本地优先与零成本部署**：`daily_stock_analysis` 和 `tickflow-stock-panel` 强调自托管和零运维，利用免费资源和本地 LLM（`llama.cpp`, `ds4`）降低使用门槛。
-   **产品趋势**：
    -   **从工具到工作台**：项目不再满足于提供单一功能（如回测），而是向集成数据、分析、决策、执行、监控的一体化“工作台”演进。
    -   **AI 设计工具赋能金融 UI**：`open-design`、`ui-ux-pro-max-skill` 等项目的火爆，预示着金融终端产品的 UI/UX 将迎来 AI 驱动的快速迭代时代。
    -   **Agent Skills 生态化**：`NVIDIA/skills`、`Orchestra-Research/AI-Research-SKILLs` 等项目表明，可复用、可组合的 Agent 技能包正在形成一个新生态。
-   **量化/交易策略趋势**：
    -   **AI 驱动的基本面研究**：`ai-berkshire` 的出现，将 AI 的应用从技术面和另类数据拓展到深度基本面分析。
    -   **自动化因子挖掘**：`AlphaGPT` 代表了利用深度强化学习自动发现 Alpha 的前沿方向。
    -   **“Vibe Trading”**：自然语言驱动的策略开发模式开始萌芽，旨在进一步降低量化交易门槛。
-   **AI Agent 与自动化交易结合趋势**：
    -   **Agent 角色深度专业化**：出现了专门负责信用风险的 Agent（`marvis-risk-agent`）、专门负责安全测试的 Agent（`Claude-BugHunter`），分工越来越细。
    -   **Agent 长周期任务规划**：`planning-with-files` 项目关注 Agent 在长周期、多步骤任务中的状态保持和崩溃恢复，这对需要持续运行的交易 Agent 至关重要。
-   **值得后续做原型验证的方向**：
    -   复刻 `ai-berkshire` 的多 Agent 对抗分析框架，应用于 A 股或美股财报分析。
    -   基于 DuckDB + Polars 构建轻量级本地量化研究平台原型。
    -   利用 `langfuse` 为现有交易 Agent 增加 LLM 调用链路的可观测性。

## 5. 今日灵感清单
1.  **MVP 灵感：财报分析 Agent 团队**：借鉴 `ai-berkshire` 的多 Agent 对抗架构，创建一个由“财务分析师”、“业务专家”、“竞争对手分析师”和“风险专家”组成的 Agent 团队，自动分析上市公司财报并生成辩论式研究报告。
2.  **技术调研：DuckDB 在量化回测中的应用**：深入研究 `tickflow-stock-panel` 的技术栈，验证使用 DuckDB 替代 MySQL/PostgreSQL 作为回测数据存储和计算引擎的性能与便利性。
3.  **Demo 复现：自然语言策略生成器**：参考 `Vibe-Trading` 的理念，利用 Codex/Claude Code 实现一个简单的 Demo，让用户输入“当茅台市盈率低于 25 且突破 20 日均线时买入”，自动生成 `freqtrade` 或 `qlib` 的策略代码。
4.  **Agent 技能设计：金融数据获取 Skill**：参照 `NVIDIA/skills` 的格式，为 Claude Code 或 Codex 设计一个标准的金融数据 Skill，封装 `OpenBB` 或 `public-apis` 中的数据接口，让 Agent 能自主获取行情、基本面等数据。
5.  **架构设计：交易 Agent 的可观测性平台**：基于 `langfuse` 搭建一个专门针对交易 Agent 的监控看板，追踪 Agent 的思考链路、工具调用、API 消耗和决策逻辑，用于调试和优化。
6.  **Watchlist 添加：`marvis-risk-agent`**：持续关注该项目，观察其如何将复杂的信用风控流程 Agent 化，为构建其他金融风控 Agent（如市场风险、操作风险）积累经验。
7.  **安全实践：Agent 驱动渗透测试**：参考 `Claude-BugHunter`，探索使用 AI Agent 对自建的交易系统进行自动化安全漏洞扫描和渗透测试，提升系统健壮性。
8.  **UI 原型：AI 生成金融终端界面**：利用 `open-design` 或 `ui-ux-pro-max-skill`，快速生成一个集行情展示、策略回测、风险监控于一体的现代化金融终端高保真原型。
9.  **模型调研：本地金融 LLM 选型**：使用 `whichllm` 和 `llmfit` 工具，在自己的硬件上评测不同开源 LLM（如 DeepSeek 4 等）在金融情感分析、实体识别等任务上的性能与延迟。
10. **因子研究：探索 `AlphaGPT` 的因子挖掘流程**：部署并运行 `AlphaGPT`，研究其深度强化学习模型的设计，尝试在 A 股或加密货币市场复现其自动化因子挖掘过程。

## 6. Watchlist 建议
-   **`xbtlin/ai-berkshire`**：AI 与价值投资结合的先锋项目，其多 Agent 对抗分析框架极具启发性，增长迅速，值得长期跟踪其方法论演进。
-   **`shy3130/tickflow-stock-panel`**：代表了量化工作台的现代化技术栈方向（DuckDB, Polars），项目虽早期但理念先进，是观察下一代量化工具形态的窗口。
-   **`eddyzzl/marvis-risk-agent`**：金融风控领域垂直 Agent 化的先行者，填补了市场空白，其架构设计和功能迭代对构建企业级风控 Agent 有重要参考价值。
-   **`HKUDS/Vibe-Trading`**：探索了下一代人机交易交互范式，其自然语言驱动的策略开发模式一旦成熟，将彻底改变交易工具的用户体验。
-   **`imbue-bit/AlphaGPT`**：自动化因子挖掘是量化领域的长期热点，该项目结合了深度强化学习，技术前沿，值得关注其模型效果和迭代进展。
-   **`Orchestra-Research/AI-Research-SKILLs`**：作为 Agent Skills 生态的重要贡献者，其提供的技能库可以作为构建专业金融 Agent 的知识基础。

## 7. 风险提醒
-   **GitHub star 不是投资建议**：项目的高关注度不代表其策略能盈利，Star 数更多反映的是开发者和使用者的兴趣，而非金融绩效。
-   **不运行未知 trading bot**：尤其是像 `Polymarket-Arbitrage-Trading-Bot-Python` 这类描述堆砌、过度营销的项目，极有可能存在恶意代码、后门或严重逻辑缺陷，直接运行可能导致资金损失。
-   **不泄露交易所 API key**：任何要求输入真实交易所 API Key 的开源项目都存在 Key 泄露风险，应仅在充分代码审计和隔离环境下使用，并严格限制 API 权限（禁止提币）。
-   **注意马丁、网格、套利、杠杆类项目的爆仓风险**：`freqtrade` 等项目中可能包含马丁格尔、网格等高风险策略，`Polymarket-Arbitrage-Trading-Bot-Python` 涉及套利，在极端行情下存在巨大资金风险。
-   **注意回测幸存者偏差和过拟合**：`TradingAgents`、`Vibe-Trading`、`AlphaGPT` 等项目展示的回测结果可能经过精心挑选或存在过拟合，实盘表现可能大相径庭。AI 生成的策略尤其需要警惕“幻觉”和过度优化。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
-   **基线数据**：本次报告使用了 `2026-06-24` 的 1 日基线和 `2026-06-18` 的 7 日基线数据，涨星计算准确。
-   **数据缺失**：部分项目（如 `tickflow-stock-panel`、`marvis-risk-agent`）由于创建时间较晚，缺少 7 日涨星数据，标记为 `-`。所有项目均缺少 30 日涨星数据。
-   **采集状态**：本次共采集 50 个候选项目，数据采集过程正常，无失败记录。
-   **样本偏差**：候选项目通过关键词和 Topic 匹配筛选，可能偏向于近期活跃、描述中包含特定术语的项目，无法完全代表整个金融/量化开源生态。部分项目（如 `build-your-own-x`、`open-design`）因描述或 Readme 中偶然包含匹配词而被收录，其核心领域并非金融科技，分析时已做区分。
