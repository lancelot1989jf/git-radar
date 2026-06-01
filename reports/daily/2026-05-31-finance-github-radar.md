# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-05-31

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI Agent 与设计/前端工程深度融合**：以 `open-design`、`ui-ux-pro-max-skill` 为代表，AI Agent 不再局限于代码生成，而是深度介入 UI/UX 设计、原型生成、设计系统管理，形成“Vibe Design”新范式。
    2.  **多 Agent 协作框架持续升温**：`ruflo`、`TradingAgents` 等项目展示了从单 Agent 到多 Agent 集群（Swarm）的演进，强调自主工作流编排、自学习智能，架构上向企业级、可扩展方向收敛。
    3.  **金融基础模型与专用推理引擎出现**：`Kronos` 提出“金融市场语言基础模型”，`turbovec` 基于 TurboQuant 构建高性能向量索引，`ds4` 为特定模型提供本地推理引擎，显示量化研究正走向更深层的模型定制与硬件适配。
- **是否出现新趋势**：是。“Vibe Coding”向“Vibe Design”延伸，AI Agent 的能力边界从逻辑层扩展到表现层；金融领域出现专用基础模型（Foundation Model）的尝试。
- **是否出现值得复刻/参考的工程架构**：是。`ruflo` 的多 Agent 编排架构、`TradingAgents` 的多 Agent 金融交易框架、`a-stock-data` 的 7 层全栈数据工具包架构，均具有较高的工程参考价值。
- **是否有明显骗局、过度营销或高风险项目**：`polymarket-trading-bot` 描述高度重复关键词堆砌，存在过度营销嫌疑，且缺乏 License，风险极高。多数交易类项目风险等级为“中”，需警惕。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|------|------|-------|----------|---------|------|-----------|------------|----------|----------|
| 1 | VoltAgent/awesome-design-md | 86229 | +296 | +2558 | - | 设计系统 | 品牌设计系统 DESIGN.md 文件集合，供 AI Agent 生成匹配 UI | AI 辅助设计工程化 | 中 |
| 2 | nexu-io/open-design | 56591 | +561 | +5151 | TypeScript | AI设计/本地优先 | 本地优先的开源 Claude Design 替代品，支持多 Agent 集成 | 本地化 AI 设计工具架构 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 85670 | +442 | +3291 | Python | AI技能/UI设计 | 为构建专业多平台 UI/UX 提供设计智能的 AI SKILL | AI Agent 技能模块化设计 | 低 |
| 4 | codecrafters-io/build-your-own-x | 509568 | +1198 | +5188 | Markdown | 教程/编程 | 通过从零复刻技术来掌握编程 | 系统构建方法论 | 中 |
| 5 | ruvnet/ruflo | 57026 | +309 | +2179 | TypeScript | 多Agent编排 | 领先的 Agent 编排平台，支持多 Agent 集群和自主工作流 | 企业级 Agent 架构参考 | 低 |
| 6 | TauricResearch/TradingAgents | 81330 | +273 | +2033 | Python | 多Agent/金融交易 | 多 Agent LLM 金融交易框架 | 多 Agent 交易决策架构 | 低 |
| 7 | shiyu-coder/Kronos | 27824 | +174 | +1974 | Python | 金融基础模型 | 金融市场语言基础模型 | 金融领域专用模型思路 | 低 |
| 8 | awesome-selfhosted/awesome-selfhosted | 296530 | +218 | +1470 | - | 自托管 | 可自托管的免费软件网络服务列表 | 自托管金融数据/工具栈 | 中 |
| 9 | garrytan/gbrain | 20195 | +246 | +1436 | TypeScript | Agent大脑 | 个人定制的 OpenClaw/Hermes Agent 大脑 | Agent 个性化配置思路 | 低 |
| 10 | public-apis/public-apis | 438281 | +303 | +1252 | Python | API集合 | 免费 API 集合列表 | 金融数据 API 资源发现 | 中 |
| 11 | ggml-org/llama.cpp | 114058 | +172 | +1267 | C++ | LLM推理 | C/C++ 实现的 LLM 推理引擎 | 量化交易中的本地模型部署 | 低 |
| 12 | vinta/awesome-python | 300646 | +191 | +1197 | Python | Python资源 | Python 框架、库、工具和资源列表 | 量化研究工具链参考 | 低 |
| 13 | RyanCodrai/turbovec | 4060 | +165 | +1370 | Python | 向量索引/量化 | 基于 TurboQuant 的 Rust 向量索引，带 Python 绑定 | 高性能量化数据检索 | 低 |
| 14 | Fincept-Corporation/FinceptTerminal | 24850 | +133 | +1330 | C++ | 金融终端 | 现代金融应用，提供高级市场分析和投资研究工具 | 金融终端产品架构 | 低 |
| 15 | code-yeongyu/oh-my-openagent | 60487 | +147 | +1192 | TypeScript | Agent编排 | 最佳 Agent 驾驭工具 | Agent 管理与编排界面设计 | 低 |
| 16 | ZhuLinsen/daily_stock_analysis | 39674 | +145 | +918 | Python | AI股票分析 | LLM 驱动的 A/H/美股智能分析系统 | AI 驱动的投研自动化 | 低 |
| 17 | simonlin1212/a-stock-data | 3098 | +92 | +1002 | - | A股数据工具包 | A股全栈数据工具包，7层架构，零第三方依赖 | 数据工程架构设计 | 低 |
| 18 | Open-Dev-Society/OpenStock | 12832 | +21 | +1254 | TypeScript | 股票平台 | 开源市场数据平台，替代昂贵商业方案 | 金融数据产品化思路 | 低 |
| 19 | antirez/ds4 | 12636 | +68 | +924 | C | 推理引擎 | DeepSeek 4 Flash 本地推理引擎 | 专用模型推理优化 | 低 |
| 20 | avelino/awesome-go | 174235 | +134 | +653 | Go | Go资源 | Go 框架、库和软件精选列表 | 高性能交易系统技术选型 | 中 |
| 21 | HKUDS/Vibe-Trading | 9218 | +153 | +657 | Python | AI交易/回测 | “Vibe-Trading”个人交易 Agent | 对话式交易 Agent 原型 | 中 |
| 22 | emmabostian/developer-portfolios | 23496 | +368 | +614 | Python | 开发者作品集 | 开发者作品集灵感列表 | 量化研究员作品集参考 | 低 |
| 23 | brokermr810/QuantDinger | 7054 | +66 | +615 | Python | AI量化平台 | 面向加密、股票、外汇的 AI 量化交易平台 | 多资产 AI 交易平台架构 | 中 |
| 24 | AlexsJones/llmfit | 26971 | +90 | +320 | Rust | 模型适配 | 查找适合你硬件的模型 | 本地模型部署工具链 | 低 |
| 25 | microsoft/qlib | 43850 | +93 | +405 | Python | AI量化平台 | 微软 AI 量化投资平台，支持多种 ML 范式 | 标准化 AI 量化研究流程 | 低 |
| 26 | VoltAgent/awesome-claude-code-subagents | 20977 | +60 | +501 | Shell | Agent子代理 | 100+ Claude Code 子代理集合 | Agent 功能模块化拆分 | 低 |
| 27 | Z4nzu/hackingtool | 76825 | +131 | +389 | Python | 黑客工具 | 一体化黑客工具 | 安全测试与风控意识 | 低 |
| 28 | OthmanAdi/planning-with-files | 22438 | +63 | +430 | Python | Agent规划 | 实现 Manus 风格持久化 Markdown 规划的 Claude Code 技能 | Agent 规划与状态管理 | 低 |
| 29 | QuantConnect/Lean | 19585 | +57 | +473 | C# | 算法交易引擎 | QuantConnect 算法交易引擎 | 成熟交易引擎架构参考 | 中 |
| 30 | punkpeye/awesome-mcp-servers | 88257 | +45 | +426 | - | MCP服务器 | MCP 服务器集合 | Agent 工具集成生态 | 中 |
| 31 | OpenBB-finance/OpenBB | 68355 | +68 | +316 | Python | 金融数据平台 | 面向分析师、Quant 和 AI Agent 的金融数据平台 | 金融数据中台架构 | 中 |
| 32 | freqtrade/freqtrade | 50999 | +56 | +267 | Python | 加密交易机器人 | 免费开源加密交易机器人 | 交易机器人策略框架 | 中 |
| 33 | nidhinjs/prompt-master | 8593 | +49 | +406 | - | 提示工程 | 为任何 AI 工具编写精准提示的 Claude 技能 | 提示工程自动化 | 低 |
| 34 | ashishpatel26/500-AI-Agents-Projects | 31482 | +79 | +369 | - | AI Agent项目 | 500 个 AI Agent 项目精选集 | Agent 应用场景灵感库 | 中 |
| 35 | ripienaar/free-for-dev | 122849 | +46 | +239 | HTML | 免费资源 | SaaS、PaaS、IaaS 免费层列表 | 零成本金融工具栈搭建 | 低 |
| 36 | muratcankoylan/Agent-Skills-for-Context-Engineering | 16208 | +38 | +278 | Python | Agent技能 | 上下文工程和多 Agent 架构的 Agent 技能集合 | Agent 上下文管理工程化 | 低 |
| 37 | edison7009/EchoBird | 1412 | +33 | +425 | Rust | 一键安装 | 一键安装工具 | 环境部署自动化 | 低 |
| 38 | TraderAlice/OpenAlice | 4645 | +20 | +397 | TypeScript | AI交易代理 | 覆盖研究、入场、管理、退出的全流程 AI 交易代理 | 全流程交易 Agent 设计 | 中 |
| 39 | Orchestra-Research/AI-Research-SKILLs | 9167 | +50 | +292 | TeX | AI研究技能 | AI 研究和工程技能开源库 | 量化研究 Agent 技能包 | 低 |
| 40 | tradesdontlie/tradingview-mcp | 3314 | +51 | +178 | JavaScript | TradingView MCP | 将 Claude Code 连接到 TradingView 桌面端 | 交易工作流自动化 | 中 |
| 41 | fffaraz/awesome-cpp | 71550 | +14 | +118 | - | C++资源 | C/C++ 框架、库和资源列表 | 低延迟交易系统技术选型 | 低 |
| 42 | rust-unofficial/awesome-rust | 57651 | +14 | +136 | Rust | Rust资源 | Rust 代码和资源精选列表 | 高性能安全交易系统选型 | 低 |
| 43 | Developer-Y/cs-video-courses | 81670 | +19 | +111 | - | 计算机课程 | 计算机科学视频课程列表 | 量化金融基础知识补充 | 中 |
| 44 | NoFxAiOS/nofx | 12506 | +34 | +39 | Go | AI交易终端 | 面向美股、商品、外汇、加密的 AI 交易终端助手 | 多市场 AI 交易终端设计 | 中 |
| 45 | chengzuopeng/stock-sdk | 1064 | +19 | +268 | TypeScript | 股票SDK | 前端专用、无需后端的股票数据 JavaScript SDK | 前端金融数据获取方案 | 低 |
| 46 | josephmisiti/awesome-machine-learning | 72643 | +12 | +87 | Python | 机器学习资源 | 机器学习框架、库和软件列表 | 量化策略 ML 技术选型 | 低 |
| 47 | BlackCandleLab/polymarket-trading-bot | 396 | +114 | - | JavaScript | 预测市场机器人 | Polymarket 交易与套利机器人 | 预测市场自动化交易 | 中 |
| 48 | charlax/professional-programming | 51037 | +5 | +21 | Python | 编程资源 | 软件工程师学习资源集合 | 量化开发工程素养提升 | 中 |
| 49 | akullpp/awesome-java | 48092 | +8 | +61 | - | Java资源 | Java 框架、库和软件列表 | 企业级交易系统技术选型 | 中 |
| 50 | vuejs/awesome-vue | 73576 | -2 | -17 | - | Vue资源 | Vue.js 相关精选列表 | 交易前端界面技术选型 | 低 |
| 51 | ByteByteGoHq/system-design-101 | 82934 | +16 | +140 | - | 系统设计 | 用可视化解释复杂系统 | 交易系统架构设计参考 | 低 |

## 3. 重点项目深度分析

### 项目：nexu-io/open-design
- **项目解决什么问题**：解决 AI 辅助设计工具对云端服务的依赖，提供本地优先、开源、可集成多种 AI Agent 的设计工具，替代 Figma 等商业软件。
- **为什么最近值得关注**：7 日涨星超 5000，增速极快。它代表了“Vibe Design”趋势，将 AI Agent 能力从代码生成拓展到 UI/UX 设计、原型、视频等多模态输出。
- **技术栈/架构亮点**：TypeScript 编写的原生桌面应用，支持 259+ Skills 和 142+ Design Systems，集成 Claude Code、Codex、Cursor 等 17+ CLI，架构上强调本地优先和沙箱预览。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其“Skills + Design Systems”的模块化架构可借鉴用于构建交易 Agent 的策略模板库、可视化回测报告生成器或金融仪表盘自动生成工具。
- **可能的风险**：项目较新，长期维护活跃度待观察；与特定 AI 模型（Claude）绑定较深，存在依赖风险。

### 项目：ruvnet/ruflo
- **项目解决什么问题**：解决复杂 AI 工作流中多 Agent 协作、编排和自学习的问题，提供企业级多 Agent 集群部署和对话式 AI 系统构建能力。
- **为什么最近值得关注**：7 日涨星超 2000，是 Agent 编排领域的头部项目。其“Swarm Intelligence”和“Self-learning”特性代表了 Agent 架构的前沿方向。
- **技术栈/架构亮点**：TypeScript 实现，集成 RAG、MCP Server、Claude Code/Codex。架构上强调“Agentic Workflow”和“Multi-Agent Systems”，支持通过 npm 包形式分发 Skills。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其多 Agent 编排模式可直接应用于构建“多分析师 Agent 协作”的量化研究系统，例如将宏观分析、技术分析、风控、执行等角色分配给不同 Agent 协同工作。
- **可能的风险**：项目 Open Issues 数量较多（589），可能存在稳定性问题；多 Agent 系统的调试和监控复杂度高。

### 项目：TauricResearch/TradingAgents
- **项目解决什么问题**：利用多 Agent LLM 框架模拟人类交易团队的协作决策过程，进行金融交易。
- **为什么最近值得关注**：总星数超 8 万，7 日涨星超 2000，是“AI Agent + 金融交易”方向最成熟、最受关注的开源项目之一。
- **技术栈/架构亮点**：Python 实现，采用多 Agent 架构，每个 Agent 可能扮演不同角色（如分析师、交易员、风控官）。项目明确标记为研究工具，强调框架的灵活性和可扩展性。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：核心参考价值在于其多 Agent 角色分工与协作的架构设计。可以借鉴其思路，构建企业内部的多角色 AI 投研团队。
- **可能的风险**：作为研究框架，其策略有效性未经实盘验证；多 Agent 决策可能存在一致性问题；回测可能存在过拟合风险。

### 项目：shiyu-coder/Kronos
- **项目解决什么问题**：尝试构建一个专门理解金融市场“语言”的基础模型，而非通用 LLM 在金融领域的简单应用。
- **为什么最近值得关注**：7 日涨星近 2000，代表了量化研究从“应用 LLM”到“构建金融专用基础模型”的范式转变。
- **技术栈/架构亮点**：Python 实现，具体模型架构信息不足，但从定位看可能涉及金融时序数据的预训练、金融文本理解等。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：提供了一种新思路：为交易 Agent 构建专用的、更懂市场的“大脑”，而非仅依赖通用 LLM。值得关注其模型架构和训练数据构建方法。
- **可能的风险**：项目处于早期，模型效果和实用性未经验证；金融基础模型的构建需要海量高质量数据和巨大算力，复现门槛极高。

### 项目：RyanCodrai/turbovec
- **项目解决什么问题**：解决量化研究中大规模向量检索的性能问题，基于 TurboQuant 技术，提供高性能的近似最近邻搜索。
- **为什么最近值得关注**：7 日涨星超 1300，增速相对于其总星数（4060）非常惊人。结合了 Rust 的性能和 Python 的易用性，是量化基础设施领域的潜力项目。
- **技术栈/架构亮点**：核心由 Rust 编写，提供 Python 绑定。利用 SIMD（AVX512/NEON）指令集加速，对标 FAISS，专注于量化场景下的向量搜索。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。可集成到量化回测或实时交易系统中，用于快速检索相似历史行情模式、因子向量等，提升策略研发效率。
- **可能的风险**：项目较新，社区和文档可能不完善；依赖特定硬件指令集，部署环境受限。

### 项目：simonlin1212/a-stock-data
- **项目解决什么问题**：为 AI 编程助手提供一套全栈、零第三方依赖的 A 股数据获取工具包，解决金融数据获取碎片化、依赖复杂的问题。
- **为什么最近值得关注**：7 日涨星超 1000，增速极快。其“7 层架构 · 28 端点 · 13 数据源”的设计理念非常清晰，直击金融数据工程的痛点。
- **技术栈/架构亮点**：强调全栈和零第三方依赖，架构上分层设计（可能包括数据源层、清洗层、存储层、API 层等），专为 AI 编程助手优化。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其分层架构设计是构建任何金融数据中台的优秀参考。可以直接作为 AI 交易 Agent 的数据接口层，让 Agent 通过标准化端点获取数据。
- **可能的风险**：数据源可能来自非官方渠道，数据质量和合规性需验证；项目较新，长期维护和数据源稳定性是关键。

### 项目：HKUDS/Vibe-Trading
- **项目解决什么问题**：将“Vibe Coding”理念引入交易，旨在通过自然语言对话驱动交易 Agent 执行策略。
- **为什么最近值得关注**：24 小时涨星 153，概念新颖，由香港大学团队开发，具有一定的学术背景。
- **技术栈/架构亮点**：Python 实现，集成 LLM、MCP、多 Agent 架构，支持回测。核心是将用户模糊的交易“感觉”或指令转化为具体的交易逻辑。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其“对话即交易”的交互模式值得借鉴，可用于构建面向非专业用户的交易助手原型，或作为专业交易员的快速策略验证工具。
- **可能的风险**：“Vibe”交易概念过于模糊，策略有效性存疑；存在严重的策略过拟合和误解用户意图的风险；风险等级标记为“中”。

### 项目：TraderAlice/OpenAlice
- **项目解决什么问题**：提供一个覆盖从研究、入场、持续管理到退出的全流程 AI 交易代理，试图成为“一个人的华尔街”。
- **为什么最近值得关注**：7 日涨星近 400，概念宏大，试图打造全流程自动化的交易 Agent。
- **技术栈/架构亮点**：TypeScript 实现，覆盖股票、加密、商品、外汇等多资产。架构上强调全流程闭环管理。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其全流程闭环的设计思想非常有价值，可以作为设计企业级交易 Agent 系统的蓝图，明确各个阶段（研究、决策、执行、风控）的 Agent 职责和交互接口。
- **可能的风险**：全流程自动化难度极高，项目可能处于早期阶段；AGPL-3.0 协议有传染性，商用需谨慎；多资产、全流程的策略风险控制是巨大挑战。

## 4. 趋势归纳
- **技术趋势**：
    - **Agent 编排与集群化**：从单 Agent 走向多 Agent 协作（Swarm），强调自主工作流和自学习。
    - **AI 与设计深度融合**：AI Agent 的能力边界扩展到 UI/UX 设计、原型生成，形成“Vibe Design”工具链。
    - **金融专用模型**：出现针对金融市场语言的基础模型尝试，以及针对特定模型的本地高性能推理引擎。
    - **高性能量化基础设施**：Rust 与 Python 结合，利用 SIMD 等技术加速量化数据检索与处理。
- **产品趋势**：
    - **本地优先与开源替代**：从设计工具（open-design）到金融终端（OpenStock），开源项目试图替代昂贵的商业软件。
    - **全流程 AI 交易代理**：产品概念从单一策略机器人向覆盖研究、决策、执行、风控的全流程 Agent 演进。
    - **AI 编程助手的数据工具包**：出现专为 AI Agent 设计的、零依赖、分层架构的数据获取工具。
- **量化/交易策略趋势**：
    - **多 Agent 角色扮演**：模拟人类分析师、交易员、风控官的团队协作模式。
    - **对话式/意图式交易**：“Vibe-Trading”概念兴起，探索自然语言驱动的策略生成。
- **AI Agent 与自动化交易结合趋势**：
    - **MCP 协议成为 Agent 工具集成标准**：大量项目通过 MCP 连接外部数据源和工具。
    - **Agent 技能（Skills）模块化**：交易策略、分析逻辑、风控规则被封装为可复用的 Skills。
- **值得后续做原型验证的方向**：
    - 基于多 Agent 框架（如 ruflo）构建一个角色分工的 AI 投研团队原型。
    - 利用 a-stock-data 的分层架构思想，为 AI 交易 Agent 构建标准化的数据接口层。
    - 验证 turbovec 在量化因子检索场景下的性能提升。

## 5. 今日灵感清单
1.  **构建“AI 投研团队”MVP**：参考 `TradingAgents` 和 `ruflo`，用 LangGraph 或类似框架快速搭建一个包含“宏观分析师”、“技术分析师”、“新闻情绪分析师”和“风控官”四个角色的多 Agent 系统，对同一标的进行辩论式分析。
2.  **调研金融专用基础模型**：深入研究 `Kronos` 项目的论文或技术文档，分析其模型架构和训练数据构成，评估将金融领域知识预训练进模型对下游交易任务的实际提升。
3.  **复现“Vibe-Trading”Demo**：基于 `Vibe-Trading` 的思路，利用 OpenAI 或 Claude API，结合 `tradingview-mcp` 或 `a-stock-data` 的数据，实现一个简单的对话式图表分析或策略生成 Demo。
4.  **设计 Agent 交易技能包**：参考 `ui-ux-pro-max-skill` 和 `AI-Research-SKILLs` 的模块化设计，将常用的量化策略（如双均线、动量）封装为标准的 Agent Skills，使其能被不同 Agent 框架调用。
5.  **搭建零成本金融数据中台原型**：利用 `free-for-dev` 列表中的免费资源，结合 `a-stock-data` 的分层架构思想，设计一个面向 AI Agent 的轻量级金融数据服务。
6.  **评估 turbovec 性能**：在量化因子库上，对 `turbovec` 和 FAISS 进行基准测试，评估其在相似 K 线形态检索、因子向量搜索等场景下的性能差异。
7.  **开发 TradingView AI 插件**：基于 `tradingview-mcp` 项目，开发一个更完善的 Claude Code 或本地 LLM 插件，实现自动识别图表形态、生成交易备注等功能。
8.  **分析 OpenAlice 全流程架构**：仔细阅读 `OpenAlice` 的源码，梳理其从研究到退出的全流程状态管理、事件驱动机制和 Agent 间通信协议，作为设计复杂交易系统的参考。
9.  **加入 Watchlist**：将 `Kronos`、`turbovec`、`a-stock-data`、`Vibe-Trading` 加入 Watchlist，持续跟踪其发展。

## 6. Watchlist 建议
- **shiyu-coder/Kronos**：金融基础模型的开创性尝试，代表未来方向，需长期跟踪其技术演进。
- **RyanCodrai/turbovec**：高性能量化基础设施，若成熟可大幅提升策略研发效率，关注其生态建设。
- **simonlin1212/a-stock-data**：解决 A 股数据获取痛点的创新方案，架构设计优秀，关注其数据源稳定性和社区贡献。
- **HKUDS/Vibe-Trading**：概念新颖的对话式交易 Agent，学术背景，关注其能否将概念落地为有效工具。
- **TraderAlice/OpenAlice**：全流程 AI 交易代理的野心之作，架构设计值得学习，关注其功能完整度和实盘表现。
- **ruvnet/ruflo**：Agent 编排领域的领先项目，关注其多 Agent 协作和自学习机制的成熟度。
- **nexu-io/open-design**：AI 设计工具的代表，其 Skills 和 Design Systems 的模块化架构对 Agent 工具设计有启发。

## 7. 风险提醒
- **GitHub star 不是投资建议**：高星数和涨星速度仅代表社区关注度，不代表项目盈利能力或策略有效性。
- **不运行未知 trading bot**：尤其对于描述模糊、代码质量不明、无 License 或过度营销的项目（如 `polymarket-trading-bot`），严禁直接运行。
- **不泄露交易所 API key**：任何要求输入真实交易所 API Key 的开源项目都存在极高的资产被盗风险。
- **注意策略风险**：马丁、网格、套利、杠杆类策略在极端行情下存在巨大爆仓风险。回测表现优秀不等于实盘盈利，需警惕幸存者偏差和过拟合。
- **注意合规风险**：自动化交易可能违反交易所服务条款，或涉及特定地区的金融监管法规。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
- **基线数据**：本次报告使用了 1 日基线（2026-05-30）和 7 日基线（2026-05-24）进行涨星计算，数据完整。
- **采集状态**：所有 51 个候选项目均成功采集，无缺失。
- **样本偏差**：候选项目来源于特定关键词和 topic 的搜索结果，可能偏向于近期活跃、描述中包含热门术语的项目，不代表整个金融/量化开源生态的全貌。部分项目（如 `awesome-design-md`）因描述或 topic 中命中关键词而被收录，与金融/量化直接相关性较弱，分析时需注意甄别。
