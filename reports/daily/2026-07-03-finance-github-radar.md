# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-07-03

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI 驱动的价值投资与多市场分析**：以 `ai-berkshire` 和 `daily_stock_analysis` 为代表，将 LLM 深度融入基本面研究、多源数据整合与决策看板，标志着 AI 在金融分析领域的应用正从简单的行情播报向深度投研框架演进。
    2.  **“Vibe” 式交互与 Agent 化交易**：`Vibe-Trading` 和 `TradingAgents` 等项目持续火爆，强调通过自然语言或多智能体协作来完成策略构建、回测与执行，降低了量化交易的使用门槛，但同时也带来了策略黑箱化的风险。
    3.  **AI Agent 工程基础设施的爆发**：大量项目聚焦于 Agent 的“技能 (Skills)”、“子智能体 (Subagents)”、“规划 (Planning)”和“评估 (Evaluation)”，如 `planning-with-files`、`iFixAi` 和各种 `awesome-` 列表。这表明业界正在从单点 Agent 应用转向构建更稳健、可观测、可治理的 Agent 系统工程框架，这对构建企业级 AI 交易员至关重要。
- **新趋势**：出现了专门针对 AI Agent 输出进行风险与合规评估的工具 (`iFixAi`)，以及将 AI 设计工具 (`open-design`) 与金融产品原型快速搭建结合的可能性。
- **值得复刻/参考的工程架构**：`tickflow-stock-panel` 的“自托管、零运维”量化工作台架构，以及 `planning-with-files` 的“崩溃安全”持久化规划模式，为构建个人或小团队的稳健量化系统提供了优秀范本。
- **高风险/过度营销项目**：今日榜单中未发现明显的骗局项目，但需警惕 `Vibe-Trading` 等“Vibe”概念项目可能过度简化交易风险，以及 `QuantDinger` 等多合一平台在未充分验证前直接实盘交易的风险。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|:---:|:---|:---:|:---:|:---:|:---:|:---|:---|:---|:---:|
| 1 | nexu-io/open-design | 74747 | +369 | +3037 | TypeScript | fintech_product | AI 驱动的本地优先设计工作台，可导出代码 | 为金融仪表盘、原型设计提供新工具范式 | 低 |
| 2 | ZhuLinsen/daily_stock_analysis | 53895 | +303 | +3711 | Python | ai_trading, quant_research | LLM 驱动的多市场股票智能分析系统 | 多源数据融合与 AI 决策看板的工程参考 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 100444 | +433 | +3533 | Python | fintech_product | 为 AI 编码代理提供专业 UI/UX 设计智能的技能包 | 如何将设计规范“技能化”以指导 AI Agent | 低 |
| 4 | ripienaar/free-for-dev | 128016 | +140 | +4216 | HTML | fintech_product, quant_research | 面向开发者的免费 SaaS/PaaS/IaaS 资源列表 | 发现可用于量化系统的免费数据/计算资源 | 低 |
| 5 | HKUDS/Vibe-Trading | 17696 | +249 | +4258 | Python | ai_trading, backtesting, crypto_trading | “Vibe-Trading”：你的个人交易代理 | 探索自然语言驱动的交易 Agent 交互模式 | 中 |
| 6 | xbtlin/ai-berkshire | 9214 | +441 | +5991 | Python | ai_trading, fintech_product, quant_research | AI 时代的伯克希尔：多大师方法论的价值投资研究框架 | 多 Agent 并行、对抗性分析在投研中的应用 | 低 |
| 7 | codecrafters-io/build-your-own-x | 522224 | +296 | +2204 | Markdown | trading_bot | 通过从零重建技术来掌握编程的教程集合 | 从零构建交易系统、数据库等核心组件的学习路径 | 中 |
| 8 | public-apis/public-apis | 446368 | +237 | +1950 | Python | crypto_trading, quant_research | 免费 API 的集体列表 | 寻找另类数据、市场数据 API 的入口 | 中 |
| 9 | VoltAgent/awesome-design-md | 95537 | +213 | +1917 | null | crypto_trading, fintech_product | 流行品牌设计系统的 DESIGN.md 文件分析集合 | 学习如何为 Agent 定义设计系统以生成一致 UI | 中 |
| 10 | TauricResearch/TradingAgents | 90645 | +193 | +1704 | Python | ai_trading, backtesting, quant_research | 多智能体 LLM 金融交易框架 | 多 Agent 协作在交易决策中的架构参考 | 低 |
| 11 | antirez/ds4 | 17464 | +122 | +1603 | C | quant_research | DeepSeek 4 的本地高性能推理引擎 | 为量化研究提供本地化、低延迟的 LLM 推理方案 | 低 |
| 12 | awesome-selfhosted/awesome-selfhosted | 302660 | +209 | +1340 | null | trading_bot | 可自托管的免费软件网络服务列表 | 寻找可自托管的交易后端、监控或数据服务 | 中 |
| 13 | vinta/awesome-python | 306162 | +130 | +1164 | Python | backtesting, quant_research | 精选的 Python 框架、库和工具列表 | 发掘用于回测、数据分析的 Python 新库 | 低 |
| 14 | ruvnet/ruflo | 62882 | +191 | +1239 | TypeScript | ai_trading, backtesting | 领先的 Agent 元框架，用于部署智能群体和自主工作流 | 多 Agent 群体协作框架在交易系统中的应用 | 低 |
| 15 | code-yeongyu/oh-my-openagent | 64747 | +117 | +998 | TypeScript | quant_research | 面向复杂代码库的编码 Agent 框架 | 为管理复杂量化代码库提供 Agent 编排思路 | 低 |
| 16 | ggml-org/llama.cpp | 119175 | +105 | +876 | C++ | ai_trading, quant_research | 在 C/C++ 中进行 LLM 推理 | 为低延迟、本地化的 AI 交易信号生成提供基础 | 低 |
| 17 | shy3130/tickflow-stock-panel | 1394 | +161 | +1011 | TypeScript | ai_trading, backtesting, quant_research | 自托管、零运维的 A 股量化工作台 | 个人量化工作站的完整架构参考（选股+监控+回测） | 低 |
| 18 | garrytan/gbrain | 24967 | +92 | +727 | TypeScript | fintech_product | 一个固执己见的 Agent 大脑 | 观察顶级投资者如何定制个人 AI Agent 大脑 | 低 |
| 19 | simonlin1212/a-stock-data | 6361 | +90 | +685 | null | risk_management, trading_infra | A股全栈数据工具包，覆盖 13 个数据源 | 构建 A 股多源数据管道的工程参考 | 低 |
| 20 | avelino/awesome-go | 177071 | +69 | +600 | Go | backtesting, crypto_trading, trading_bot | 精选的 Go 框架、库和软件列表 | 寻找用 Go 构建高性能交易系统的组件 | 中 |
| 21 | ai-boost/awesome-harness-engineering | 2632 | +151 | +602 | Python | backtesting | AI Agent 工程精选列表：工具、模式、评估、记忆等 | 系统性学习如何构建稳健的 AI Agent 系统 | 低 |
| 22 | ifixai-ai/iFixAi | 1139 | +507 | +569 | Python | ai_trading, risk_management, trading_bot | 在客户或监管机构之前发现 AI 的错误和盲点 | AI Agent 输出风控与合规评估的工程化实现 | 中 |
| 23 | ByteByteGoHq/system-design-101 | 85125 | +34 | +1288 | null | fintech_product | 用可视化解释复杂系统，帮助准备系统设计面试 | 为设计高可用、低延迟交易系统提供基础知识 | 低 |
| 24 | OthmanAdi/planning-with-files | 24454 | +80 | +456 | Python | ai_trading, risk_management | 为 AI 编码代理提供持久化、防崩溃的文件规划 | 为长时间运行的交易 Agent 提供状态持久化方案 | 低 |
| 25 | langfuse/langfuse | 30385 | +52 | +537 | TypeScript | ai_trading, fintech_product | 开源 AI 工程平台：LLM 评估、可观测性、提示管理 | 为 AI 交易 Agent 构建可观测性和评估管线 | 低 |
| 26 | Fincept-Corporation/FinceptTerminal | 27919 | +63 | +390 | C++ | ai_trading, fintech_product, quant_research | 现代金融应用，提供高级市场分析和投资研究工具 | 类似 Bloomberg 的综合性金融终端产品参考 | 低 |
| 27 | punkpeye/awesome-mcp-servers | 90254 | +46 | +406 | null | ai_trading, backtesting, crypto_trading | MCP 服务器集合列表 | 发现用于连接市场数据、交易接口的 MCP 服务器 | 中 |
| 28 | AlexsJones/llmfit | 29042 | +45 | +381 | Rust | ai_trading, quant_research | 一个命令找出能在你硬件上运行的模型 | 为本地化 AI 交易策略选择最优模型提供工具 | 低 |
| 29 | VoltAgent/awesome-claude-code-subagents | 22807 | +59 | +360 | Shell | fintech_product, quant_research | 100+ 个专门的 Claude Code 子智能体集合 | 学习如何将复杂金融任务分解给多个子 Agent | 低 |
| 30 | vnpy/vnpy | 42618 | +38 | +498 | Python | fintech_product, quant_research | 基于 Python 的开源量化交易平台开发框架 | 成熟的量化交易系统架构参考 | 低 |
| 31 | brokermr810/QuantDinger | 9177 | +53 | +333 | Python | ai_trading, backtesting, crypto_trading | 面向加密、股票和外汇的 AI 量化交易平台 | 多市场、多资产类别的 AI 交易平台架构参考 | 中 |
| 32 | OpenBB-finance/OpenBB | 70010 | +51 | +277 | Python | crypto_trading, quant_research | 面向分析师、量化分析师和 AI Agent 的开放数据平台 | 为 AI Agent 提供标准化的金融数据访问接口 | 中 |
| 33 | chengzuopeng/stock-sdk | 1464 | +183 | +203 | TypeScript | backtesting | 为前端设计的、无需后端的股票数据 JavaScript SDK | 纯前端量化应用的数据获取方案 | 低 |
| 34 | Developer-Y/cs-video-courses | 82246 | +30 | +291 | null | quant_research, trading_bot | 计算机科学视频课程列表 | 系统学习量化交易所需的基础知识 | 中 |
| 35 | hesreallyhim/awesome-claude-code | 47918 | +93 | - | Python | ai_trading, quant_research | 精选的 Claude Code 资源列表 | 发掘用于金融分析的 Claude Code 技能和插件 | 低 |
| 36 | nidhinjs/prompt-master | 10179 | +30 | +366 | null | ai_trading, fintech_product | 为任何 AI 工具编写精确提示的 Claude 技能 | 提升与金融 AI Agent 的交互效率 | 低 |
| 37 | AtomicBot-ai/atomic-agent | 563 | +22 | +459 | TypeScript | ai_trading, quant_research, trading_bot | 本地优先、为本地 AI 模型优化的 AI Agent | 探索隐私优先的本地化 AI 交易 Agent 方案 | 中 |
| 38 | NVIDIA/skills | 2215 | +35 | +320 | Python | backtesting, quant_research | NVIDIA 发布的 AI Agent 技能 | 学习硬件厂商如何定义 Agent 能力，可能涉及 GPU 加速的量化计算 | 低 |
| 39 | VoltAgent/awesome-codex-subagents | 5471 | +61 | +130 | null | fintech_product | 130+ 个专门的 Codex 子智能体集合 | 参考如何为 OpenAI Codex 构建金融领域子 Agent | 低 |
| 40 | RyanCodrai/turbovec | 12517 | +23 | +282 | Python | quant_research | 基于 TurboQuant 的向量索引，Rust 编写 | 为量化因子研究提供高性能向量搜索能力 | 低 |
| 41 | Orchestra-Research/AI-Research-SKILLs | 10356 | +32 | +205 | TeX | ai_trading, quant_research | 全面的 AI 研究和工程技能开源库 | 将量化研究流程“技能化”，让 Agent 自动执行 | 低 |
| 42 | Andyyyy64/whichllm | 5542 | +22 | +224 | Python | ai_trading, quant_research | 找出在你硬件上实际运行最佳的本地 LLM | 为本地化 AI 交易策略选择最优模型提供基准 | 低 |
| 43 | freqtrade/freqtrade | 52029 | +12 | +154 | Python | backtesting, crypto_trading, trading_bot | 免费、开源的加密货币交易机器人 | 成熟的加密交易机器人架构，含回测和实盘 | 中 |
| 44 | rust-unofficial/awesome-rust | 58150 | +19 | +117 | Rust | ai_trading, quant_research, risk_management | 精选的 Rust 代码和资源列表 | 寻找用 Rust 构建高性能、低延迟交易系统的库 | 低 |
| 45 | virattt/ai-hedge-fund | 60796 | +35 | - | Python | backtesting, quant_research, risk_management | 一个 AI 对冲基金团队 | 多 Agent 协作模拟对冲基金决策流程的参考实现 | 低 |
| 46 | josephmisiti/awesome-machine-learning | 73179 | +15 | +113 | Python | ai_trading | 精选的机器学习框架、库和软件列表 | 发掘用于构建交易策略的 ML 新框架 | 低 |
| 47 | fffaraz/awesome-cpp | 72077 | +10 | +101 | null | quant_research | 精选的 C++ 框架、库和资源列表 | 寻找用于构建极速交易系统的 C++ 组件 | 低 |
| 48 | vuejs/awesome-vue | 73560 | -2 | -2 | null | quant_research | 精选的 Vue.js 相关资源列表 | 为构建量化系统前端界面寻找组件库 | 低 |
| 49 | Z4nzu/hackingtool | 77955 | +16 | +115 | Python | risk_management | 黑客工具大全 | 从攻击者视角理解交易系统的潜在安全风险 | 低 |

## 3. 重点项目深度分析

### 1. `xbtlin/ai-berkshire` (AI 时代的伯克希尔)
- **项目解决什么问题**：将巴菲特、芒格等四位投资大师的方法论工程化为 AI Agent 可执行的研究框架，旨在自动化和深化价值投资流程。
- **为什么最近值得关注**：7 日涨星 +5991，增速极快。它代表了 AI 在金融领域从数据处理向深度逻辑推理和决策支持的重大转变，是“AI 分析师”概念的一个具体落地。
- **技术栈/架构亮点**：基于 Claude Code / Codex，采用多 Agent 并行与对抗性分析架构。这种架构允许不同“大师”Agent 从不同角度审视同一投资标的，最终汇总决策，模拟了投资委员会的运作模式。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其多 Agent 对抗性分析模式可直接应用于风险管理、策略评审等环节，避免单一模型偏见。
- **可能的风险**：策略过拟合（基于历史成功案例的方法论未必适用于未来）、信息不足（仅依赖公开数据）、维护活跃度（依赖个人开发者）。

### 2. `HKUDS/Vibe-Trading` (Vibe-Trading)
- **项目解决什么问题**：旨在通过自然语言交互（“Vibe”）让用户创建和管理交易策略，极大地降低量化交易的门槛。
- **为什么最近值得关注**：7 日涨星 +4258，代表了“Vibe Coding”思潮向金融交易领域的渗透。它探索了一种全新的人机交互范式。
- **技术栈/架构亮点**：结合了 LLM、MCP、多 Agent 和回测框架。用户可能只需描述交易想法，Agent 即可生成代码、回测并执行。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：交互模式值得借鉴，但核心决策逻辑需要更严格的工程化约束。可用于快速原型验证交易想法。
- **可能的风险**：**高风险**。策略黑箱化严重，用户可能在不理解底层逻辑的情况下进行实盘交易。回测造假风险高，自然语言描述的策略可能无意中引入未来函数。API key 安全风险。

### 3. `shy3130/tickflow-stock-panel` (A 股量化工作台)
- **项目解决什么问题**：为个人用户提供一个自托管、零运维的 A 股“选股 + 监控 + 回测”一体化工作台。
- **为什么最近值得关注**：24 小时涨星 +161，对于一个较新的项目（stars 1394）来说增速显著。它精准地解决了个人量化爱好者希望拥有一个集成化、低维护成本工具的需求。
- **技术栈/架构亮点**：采用 DuckDB + Polars 作为数据处理核心，FastAPI 作为后端，React 作为前端，并集成了 LLM 能力用于策略定制和个股分析。架构现代、轻量且高效。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其“自托管、零运维”的设计哲学，以及 DuckDB + Polars 的数据处理组合，是构建个人或小团队量化系统的绝佳范本。
- **可能的风险**：依赖 TickFlow 数据源，存在数据断供风险。项目较新，社区和文档可能尚不完善。

### 4. `ifixai-ai/iFixAi` (AI 输出风控)
- **项目解决什么问题**：在 AI 系统的输出触达客户或监管机构之前，自动发现其中的错误、盲点和前沿风险（如破坏、隐藏、逃避监管）。
- **为什么最近值得关注**：24 小时涨星 +507，爆发力极强。它精准地切入了 AI 治理和合规这一日益重要的领域，特别是对于金融行业。
- **技术栈/架构亮点**：运行 45 项检查，并在 5 分钟内返回一个字母等级。这种自动化、标准化的 AI 输出评估流程，为 AI 系统的上线提供了“安全阀”。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：**必须借鉴**。这是构建负责任、可信任的 AI 交易 Agent 的关键基础设施。可以将其理念集成到交易指令下达前的风控环节。
- **可能的风险**：项目本身较新，评估标准的权威性和全面性有待验证。可能无法覆盖所有金融领域的特定合规要求。

### 5. `OthmanAdi/planning-with-files` (持久化规划)
- **项目解决什么问题**：解决 AI 编码 Agent 在长时间运行任务中因上下文丢失或崩溃导致进度丢失的问题，提供一种基于文件的、防崩溃的规划方法。
- **为什么最近值得关注**：它代表了一种重要的 Agent 工程范式——“上下文工程”。对于需要运行数小时甚至数天的复杂金融分析或回测任务，状态持久化至关重要。
- **技术栈/架构亮点**：使用 Markdown 文件作为规划载体，实现了确定性的完成检查和磁盘上的多 Agent 共享状态。这种简单、可靠、与模型无关的方法非常实用。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。可直接用于管理长时间运行的量化研究任务、自动化回测流程和复杂报告生成。
- **可能的风险**：技术本身风险低，但需注意文件 I/O 可能成为高频交易场景下的性能瓶颈。

### 6. `TauricResearch/TradingAgents` (多智能体交易框架)
- **项目解决什么问题**：提供一个开箱即用的多智能体 LLM 金融交易框架，用于模拟和分析不同交易角色（如分析师、交易员、风控经理）的协作。
- **为什么最近值得关注**：总 star 数高达 90645，是该领域的标杆项目之一。它系统性地展示了如何将复杂的交易决策过程分解给多个专业 Agent。
- **技术栈/架构亮点**：Python 编写，集成了 LLM 和多 Agent 协作逻辑。其架构为构建更复杂的、角色分明的 AI 交易团队提供了蓝图。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其多角色协作架构是企业级 AI 交易系统的核心思想，可用于构建从研究、决策到执行、风控的完整 Agent 流水线。
- **可能的风险**：作为研究框架，其策略表现可能未经过严格的实盘检验，存在回测过拟合风险。

### 7. `ZhuLinsen/daily_stock_analysis` (多市场股票分析)
- **项目解决什么问题**：构建一个 LLM 驱动的、支持多市场、多源数据融合的股票智能分析系统，并提供决策看板和自动推送。
- **为什么最近值得关注**：7 日涨星 +3711，需求旺盛。它展示了如何将行情、新闻、财务等异构数据源整合，并通过 LLM 生成结构化分析报告。
- **技术栈/架构亮点**：强调“零成本定时运行”，说明其在资源调度和成本控制上有巧妙设计。多源数据融合和 LLM 分析结果的看板化展示是其亮点。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其数据融合、定时任务调度和结果推送的工程模式，可直接用于构建自动化的投研日报、周报生成 Agent。
- **可能的风险**：分析结果依赖于 LLM 的生成质量，可能存在幻觉风险。数据源稳定性是潜在问题。

## 4. 趋势归纳
- **技术趋势**：
    - **Agent 工程化**：从单 Agent 走向多 Agent 协作、子智能体分解、持久化规划和标准化评估 (`iFixAi`, `planning-with-files`, `ruflo`)。
    - **本地优先与隐私计算**：LLM 本地推理 (`llama.cpp`, `ds4`, `whichllm`) 和本地数据存储 (`tickflow-stock-panel`) 成为趋势，满足金融领域对数据隐私和低延迟的需求。
    - **高性能数据处理**：DuckDB、Polars、Rust 等技术在量化数据工程中加速普及。
- **产品趋势**：
    - **“Vibe” 交互泛化**：从“Vibe Coding”到“Vibe Trading”、“Vibe Design”，自然语言驱动的交互模式正在渗透到各个专业领域。
    - **一体化工作台**：集数据、选股、回测、监控于一体的自托管解决方案 (`tickflow-stock-panel`) 受到个人开发者的青睐。
    - **AI 原生投研工具**：不再是简单的数据展示，而是融入深度分析逻辑的 AI 原生应用 (`ai-berkshire`, `daily_stock_analysis`)。
- **量化/交易策略趋势**：
    - **多 Agent 模拟决策**：利用多个 LLM Agent 模拟分析师、交易员、风控官等角色进行协作或对抗性辩论，以形成最终决策。
    - **基本面量化融合**：AI 开始深度介入价值投资、基本面分析等传统主观领域，尝试将其逻辑工程化、自动化。
- **AI Agent 与自动化交易结合趋势**：
    - **从“替代人手”到“增强人脑”**：Agent 的角色更多是辅助研究和决策，而非完全自主交易，人机协同是当前主流。
    - **Agent 技能市场**：出现了大量 Agent 技能 (`skills`)、子智能体 (`subagents`) 和 MCP 服务器的集合列表，一个围绕 Agent 能力的生态系统正在形成。
- **值得后续做原型验证的方向**：
    - 基于 `planning-with-files` 模式，构建一个可长时间运行的自动化回测与参数优化 Agent。
    - 利用 `iFixAi` 的理念，为交易指令下达 Agent 设计一个前置的风控与合规评估模块。
    - 参考 `tickflow-stock-panel` 架构，使用 DuckDB + Polars 复现一个轻量级的个人量化数据中台。

## 5. 今日灵感清单
1.  **MVP 灵感**：构建一个“AI 交易策略评审委员会”MVP。借鉴 `ai-berkshire` 和 `TradingAgents` 的多 Agent 架构，让多个 LLM Agent 扮演不同风格的交易员，对用户输入的交易想法进行交叉验证和风险点评。
2.  **调研方向**：深入研究 `planning-with-files` 的源码，调研如何将其“崩溃安全”的文件规划模式与 `langfuse` 的可观测性结合，为交易 Agent 构建一个可靠的“黑匣子”。
3.  **Demo 复现**：让 Codex/Agent 自动复现 `tickflow-stock-panel` 的核心数据处理管线（DuckDB + Polars），并尝试替换为其他数据源，验证其架构的通用性。
4.  **Watchlist 加入**：将 `iFixAi` 加入 Watchlist，持续关注其在 AI 风险评估方面的进展，特别是其检查项是否能覆盖金融交易场景。
5.  **工具集成**：探索将 `awesome-mcp-servers` 列表中的金融数据 MCP 服务器集成到 `daily_stock_analysis` 项目中，扩展其数据覆盖范围。
6.  **安全研究**：基于 `hackingtool` 的工具集，对自建的交易系统进行渗透测试和安全审计，识别潜在漏洞。
7.  **架构设计**：参考 `FinceptTerminal` 的产品形态，设计一个模块化、可扩展的 AI 金融终端架构，允许以插件形式集成不同的分析和交易 Agent。
8.  **技能开发**：参考 `NVIDIA/skills` 和 `Orchestra-Research/AI-Research-SKILLs`，为 Claude Code 或 Codex 开发一个专门用于分析订单簿流动性和市场微观结构的技能包。
9.  **前端创新**：利用 `stock-sdk` 和 `open-design` 的理念，快速搭建一个无需后端、纯前端的个人投资仪表盘原型。
10. **性能基准**：使用 `whichllm` 和 `llmfit` 对本地部署的 LLM 进行基准测试，找出在特定量化分析任务（如金融文本情感分析）上性价比最高的模型。

## 6. Watchlist 建议
- **`xbtlin/ai-berkshire`**：AI 深度投研框架的先行者，观察其多 Agent 对抗性分析模式的演进。
- **`ifixai-ai/iFixAi`**：AI 治理与风控的工程化工具，是构建负责任 AI 系统的关键组件，未来可能成为金融 AI 的标配。
- **`shy3130/tickflow-stock-panel`**：个人量化工作站的优秀范本，其轻量级、自托管的架构理念值得长期关注。
- **`OthmanAdi/planning-with-files`**：代表了 Agent 上下文工程的重要方向，其设计模式可能成为未来 Agent 框架的标准实践。
- **`ai-boost/awesome-harness-engineering`**：系统性学习 Agent 工程的最佳入口，其内容更新反映了行业的最新共识和最佳实践。
- **`HKUDS/Vibe-Trading`**：尽管风险较高，但其探索的自然语言驱动交易交互模式是未来方向，值得观察其如何解决安全性和可靠性问题。

## 7. 风险提醒
- **GitHub star 不是投资建议**：高星和高涨星仅代表社区关注度，不代表项目的盈利能力或策略的有效性。
- **不运行未知 trading bot**：对于 `Vibe-Trading`、`QuantDinger`、`freqtrade` 等可直接执行交易的项目，切勿在未完全理解其代码逻辑和风险的情况下连接实盘账户。
- **不泄露交易所 API key**：任何要求输入 API key 的开源项目都存在密钥泄露风险，应优先使用测试网或只读权限的 Key。
- **注意策略风险**：马丁、网格、套利、杠杆类策略存在巨大爆仓风险。AI 生成的策略可能存在过拟合、未来函数等问题，回测结果不代表未来表现。
- **注意回测幸存者偏差**：许多项目的回测结果光鲜，但可能只展示了表现最好的参数组合，或未考虑滑点、手续费、市场冲击等现实因素。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
- **基线数据**：本次报告使用了 `2026-07-02` 的 1 日基线和 `2026-06-26` 的 7 日基线数据，涨星数据可靠。
- **数据缺失**：部分项目（如 `awesome-claude-code`、`ai-hedge-fund`）缺少 7 日涨星数据，可能因基线文件中不存在该项目或采集失败。
- **样本偏差**：候选项目列表由特定关键词和 topic 匹配生成，可能偏向于描述中包含相关术语的项目，无法完全代表 GitHub 上所有金融科技项目的全貌。部分项目（如 `open-design`）因描述或 readme 中命中关键词而被收录，其核心功能并非金融领域，分析时需注意区分。
