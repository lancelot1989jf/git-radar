# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-07-18

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI Agent 驱动的交易与研究框架**：以 `Vibe-Trading`、`TradingAgents` 为代表，多智能体（Multi-Agent）与大语言模型（LLM）深度结合，从策略生成、回测到实时交易决策的全流程自动化成为绝对热点。
    2.  **AI 原生设计工具与 Agent 技能生态**：`ui-ux-pro-max-skill`、`open-design`、`awesome-design-md` 等项目展示了 AI Agent 在 UI/UX 设计领域的强大生产力，其“技能包”和“设计系统”理念对金融交易界面的快速搭建有直接启发。
    3.  **高性能量化基础设施**：`turbovec`（基于 Rust 的向量索引）和 `ds4`（本地推理引擎）等项目，反映了量化研究对底层计算性能（SIMD、量化加速）和本地化部署的持续追求。
- **新趋势**：AI Agent 的“技能（Skills）”和“子智能体（Subagents）”生态正在形成标准，如 `Agent-Skills-for-Context-Engineering` 和 `NVIDIA/skills`，这为构建模块化、可扩展的金融 AI Agent 提供了新范式。
- **值得复刻的工程架构**：`Vibe-Trading` 的 MCP（Model Context Protocol）集成与多 Agent 协作架构，以及 `daily_stock_analysis` 的零成本定时运行与多源数据融合看板，是值得深入研究的工程样板。
- **高风险项目警示**：`MIgHTy-alIeN/Trading-Bot` 是一个仅创建 1 天、涉及 Solidity 套利和 MEV 的机器人，具有极高的安全风险和诈骗嫌疑，应高度警惕。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|:---:|---|---:|---:|---:|---|---|---|---|:---:|
| 1 | codecrafters-io/build-your-own-x | 528.4k | +859 | +4014 | Markdown | 教程/编程 | 通过复刻技术来学习编程的教程集合 | 学习交易系统核心组件构建 | 中 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 107.4k | +374 | +3005 | Python | AI设计/Agent技能 | 为AI编程Agent提供专业UI/UX设计智能的技能包 | 快速生成交易仪表盘原型 | 低 |
| 3 | HKUDS/Vibe-Trading | 25.0k | +336 | +5201 | Python | AI交易/多Agent | 个人AI交易Agent，支持多智能体协作 | 多Agent交易决策框架参考 | 中 |
| 4 | nexu-io/open-design | 79.6k | +219 | +2179 | TypeScript | AI设计/本地优先 | 开源AI设计引擎，替代Claude Design | 金融产品原型与报告生成 | 低 |
| 5 | public-apis/public-apis | 451.2k | +202 | +2147 | Python | API/资源列表 | 免费API集合列表 | 发现另类金融数据源 | 中 |
| 6 | VoltAgent/awesome-design-md | 103.0k | +289 | +1957 | - | 设计系统/Agent | 流行品牌设计系统文件集合，供Agent生成UI | 为交易工具生成品牌级界面 | 中 |
| 7 | awesome-selfhosted/awesome-selfhosted | 306.6k | +303 | +1829 | - | 自托管/资源列表 | 可自托管的网络服务和应用列表 | 搭建私有量化数据/交易服务 | 中 |
| 8 | vinta/awesome-python | 309.0k | +185 | +1340 | Python | Python/资源列表 | Python框架、库、工具和资源列表 | 寻找量化开发Python库 | 低 |
| 9 | TauricResearch/TradingAgents | 93.6k | +113 | +1162 | Python | AI交易/多Agent | 多智能体LLM金融交易框架 | 多Agent交易框架学术参考 | 低 |
| 10 | ZhuLinsen/daily_stock_analysis | 57.8k | +142 | +1099 | Python | AI分析/股票 | LLM驱动的多市场股票智能分析系统 | 零成本自动化投研看板 | 低 |
| 11 | ruvnet/ruflo | 65.1k | +174 | +1010 | TypeScript | Agent框架/多智能体 | 领先的Agent元框架，用于部署智能群体 | 构建复杂交易Agent工作流 | 低 |
| 12 | ggml-org/llama.cpp | 120.9k | +115 | +789 | C++ | LLM推理/量化 | C/C++实现的LLM推理引擎 | 本地化部署量化交易LLM | 低 |
| 13 | ripienaar/free-for-dev | 129.8k | +103 | +775 | HTML | 免费资源/DevOps | 对开发者有免费套餐的SaaS/PaaS/IaaS列表 | 寻找免费金融数据/算力资源 | 低 |
| 14 | RyanCodrai/turbovec | 13.5k | +173 | +882 | Python | 向量索引/量化 | 基于TurboQuant的向量索引，Rust编写 | 高性能量化因子向量检索 | 低 |
| 15 | virattt/ai-hedge-fund | 62.3k | +36 | +1056 | Python | AI交易/对冲基金 | 一个AI对冲基金团队模拟 | 多Agent投研决策流程参考 | 低 |
| 16 | avelino/awesome-go | 178.6k | +99 | +666 | Go | Go/资源列表 | Go语言框架、库和软件精选列表 | 寻找高性能交易系统Go组件 | 中 |
| 17 | garrytan/gbrain | 26.6k | +71 | +638 | TypeScript | Agent大脑/个人助手 | 个人定制的OpenClaw/Hermes Agent大脑 | 个人AI交易助手架构参考 | 低 |
| 18 | code-yeongyu/oh-my-openagent | 66.1k | +83 | +548 | TypeScript | Agent框架/CLI | 为复杂代码库设计的Agent框架 | 管理复杂量化策略代码库 | 低 |
| 19 | ashishpatel26/500-AI-Agents-Projects | 34.8k | +82 | +637 | Python | AI Agent/案例集 | 500个AI Agent用例集合 | 寻找金融AI Agent应用灵感 | 中 |
| 20 | hesreallyhim/awesome-claude-code | 50.4k | +79 | +528 | Python | Claude/资源列表 | Claude Code的精选资源列表 | 学习Claude Code在量化中的应用 | 低 |
| 21 | quantskills/quantskills | 560 | +115 | +544 | JavaScript | 量化/导航 | QuantSkills组织的全景导航 | 量化学习路径参考 | 低 |
| 22 | antirez/ds4 | 18.8k | +55 | +544 | C | LLM推理/本地 | DeepSeek 4的本地推理引擎 | 本地化运行量化分析大模型 | 低 |
| 23 | xbtlin/ai-berkshire | 13.3k | +46 | +556 | Python | AI投研/价值投资 | AI时代的伯克希尔价值投资研究框架 | 多Agent价值投资分析框架 | 低 |
| 24 | OpenSenseNova/SenseNova-U1 | 4.0k | +99 | +331 | Python | AI模型/统一范式 | 原生统一范式的AI模型 | 多模态金融数据分析潜力 | 低 |
| 25 | mudler/depth-anything.cpp | 664 | +126 | +404 | C++ | 计算机视觉/推理 | Depth Anything 3的C++移植版 | 非结构化金融数据分析潜力 | 低 |
| 26 | simonlin1212/a-stock-data | 7.4k | +35 | +518 | - | A股/数据工具 | A股全栈数据工具包，43端点 | A股多源数据采集架构参考 | 低 |
| 27 | ByteByteGoHq/system-design-101 | 86.2k | +54 | +889 | - | 系统设计/教程 | 用可视化方式解释复杂系统 | 学习交易系统架构设计 | 低 |
| 28 | punkpeye/awesome-mcp-servers | 90.9k | +48 | +321 | - | MCP/资源列表 | MCP服务器集合列表 | 为交易Agent发现MCP工具 | 低 |
| 29 | OpenBB-finance/OpenBB | 70.7k | +31 | +284 | Python | 金融数据/分析平台 | 面向分析师、量化研究员和AI Agent的开放数据平台 | 一站式金融数据与AI Agent集成 | 中 |
| 30 | handy-computer/transcribe.cpp | 337 | +131 | +174 | C++ | 语音识别/推理 | 支持16+模型族的ggml语音转文字推理 | 财报电话会等音频分析 | 低 |
| 31 | VoltAgent/awesome-claude-code-subagents | 23.5k | +30 | +279 | Shell | Claude/子智能体 | 100+ Claude Code子智能体集合 | 构建专业化金融分析子Agent | 低 |
| 32 | josephmisiti/awesome-machine-learning | 73.6k | +15 | +265 | Python | 机器学习/资源列表 | 精选机器学习框架、库和软件列表 | 寻找量化策略ML模型 | 低 |
| 33 | OthmanAdi/planning-with-files | 25.5k | +18 | +269 | Python | Agent规划/持久化 | 为AI Agent提供基于文件的持久化规划 | 实现交易Agent的长期任务规划 | 低 |
| 34 | freqtrade/freqtrade | 52.4k | +35 | +168 | Python | 加密货币/交易机器人 | 免费开源的加密货币交易机器人 | 经典策略回测与实盘架构参考 | 中 |
| 35 | brokermr810/QuantDinger | 9.7k | +24 | +261 | Python | AI量化/多资产 | AI量化交易平台，支持回测、实盘和多Agent研究 | 多资产AI交易平台架构参考 | 中 |
| 36 | shy3130/tickflow-stock-panel | 2.3k | +23 | +244 | Python | A股/量化工作台 | 自托管A股选股+监控+回测量化工作台 | A股本地化量化工作台原型 | 低 |
| 37 | rust-unofficial/awesome-rust | 58.4k | +28 | +132 | Rust | Rust/资源列表 | Rust代码和资源精选列表 | 寻找低延迟交易系统Rust库 | 低 |
| 38 | muratcankoylan/Agent-Skills-for-Context-Engineering | 17.3k | +10 | +245 | Python | Agent技能/上下文工程 | 用于上下文工程和多Agent架构的Agent技能集合 | 优化交易Agent的上下文管理 | 低 |
| 39 | fffaraz/awesome-cpp | 72.3k | +18 | +118 | - | C++/资源列表 | C/C++框架、库和资源精选列表 | 寻找高性能交易系统C++组件 | 低 |
| 40 | Open-Dev-Society/OpenStock | 13.9k | +39 | +94 | TypeScript | 股票/市场平台 | 开源股票市场平台，替代昂贵产品 | 构建免费股票行情与预警系统 | 低 |
| 41 | Orchestra-Research/AI-Research-SKILLs | 10.8k | +23 | +221 | TeX | AI研究/技能包 | 为AI模型提供AI研究和工程技能的开源库 | 为交易Agent注入深度研究能力 | 低 |
| 42 | TraderAlice/OpenAlice | 6.1k | +18 | +163 | TypeScript | AI交易/多资产 | 覆盖股票、加密货币、外汇等的AI交易Agent | 全资产类别AI交易Agent参考 | 中 |
| 43 | tradesdontlie/tradingview-mcp | 4.5k | +24 | +135 | JavaScript | TradingView/MCP | 将Claude Code连接到TradingView桌面端 | 图表分析与AI Agent结合 | 中 |
| 44 | Developer-Y/cs-video-courses | 82.5k | +10 | +101 | - | 计算机科学/课程 | 带有视频讲座的计算机科学课程列表 | 系统学习量化交易基础知识 | 中 |
| 45 | NVIDIA/skills | 2.6k | +22 | +153 | Python | Agent技能/NVIDIA | NVIDIA发布的AI Agent技能 | 官方级Agent技能开发标准参考 | 低 |
| 46 | Z4nzu/hackingtool | 78.4k | +32 | +147 | Python | 安全/渗透测试 | 黑客工具大全 | 交易系统安全测试参考 | 低 |
| 47 | vuejs/awesome-vue | 73.6k | +4 | +3 | - | Vue/资源列表 | Vue.js相关精选列表 | 寻找交易前端UI组件 | 低 |
| 48 | MIgHTy-alIeN/Trading-Bot | 300 | +121 | - | Solidity | 套利/MEV机器人 | 一个由外部脚本控制的套利机器人智能合约 | 无（高风险） | 中 |

## 3. 重点项目深度分析

### 3.1 HKUDS/Vibe-Trading
- **解决问题**：旨在提供一个“个人交易Agent”，将复杂的多Agent LLM框架应用于实际交易，覆盖从研究、策略生成到执行的环节。
- **为何值得关注**：7日涨星高达5201，是本周最火爆的金融AI项目。它由学术机构（HKUDS）发布，结合了MCP、多Agent等前沿技术，代表了AI交易框架的最新探索方向。
- **技术栈/架构亮点**：Python编写，明确集成了`mcp`（模型上下文协议）和`multi-agent`架构。Topics中包含`ai-agent`, `llm`, `backtesting`，表明其是一个集大成的框架。
- **借鉴价值**：其多Agent协作架构和MCP集成方式，可直接为构建企业级AI交易Agent框架提供设计参考，特别是如何让多个专业Agent（如分析师、交易员、风控）协同工作。
- **潜在风险**：作为研究型项目，策略在实盘中的有效性未经验证，存在过拟合风险。`crypto_related`标签提示其可能涉及高风险市场。

### 3.2 TauricResearch/TradingAgents
- **解决问题**：提供一个标准化的“多智能体LLM金融交易框架”，旨在模拟一个分工明确的交易团队。
- **为何值得关注**：拥有93.6k stars，是该领域的标杆项目。持续的高活跃度表明社区对其架构的认可。
- **技术栈/架构亮点**：Python编写，专注于`agent`, `multiagent`, `llm`和`trading`。其架构核心是让多个扮演不同角色（如基本面分析师、技术分析师、交易员）的LLM Agent进行辩论和决策。
- **借鉴价值**：其多Agent角色分工和辩论机制，是设计复杂决策支持系统的绝佳范本，可应用于投研、风控等场景。
- **潜在风险**：风险较低，主要作为研究工具。但需注意，其模拟的交易决策流程可能与真实市场压力下的决策存在巨大差异。

### 3.3 ZhuLinsen/daily_stock_analysis
- **解决问题**：为个人投资者提供一个零成本、可定时运行的A股智能分析系统，整合多源行情、新闻和LLM分析。
- **为何值得关注**：57.8k stars，7日涨星1099，是A股量化领域的热门项目。其“零成本定时运行”的特性极具吸引力。
- **技术栈/架构亮点**：Python编写，集成了`ai-agent`, `llm`。架构上强调多源数据融合、决策看板和自动推送，是一个完整的个人投研工作流。
- **借鉴价值**：其数据融合、定时任务调度和LLM分析看板的工程实现，是快速搭建个人或小型团队自动化投研系统的优秀蓝本。
- **潜在风险**：依赖第三方数据源，稳定性存在风险。LLM生成的“分析”可能包含幻觉，不能直接作为交易依据。

### 3.4 virattt/ai-hedge-fund
- **解决问题**：模拟一个完整的AI对冲基金团队运作流程，从数据分析到最终决策。
- **为何值得关注**：62.3k stars，7日涨星1056，是AI在金融领域应用的经典模拟项目，常被用于教学和概念验证。
- **技术栈/架构亮点**：Python编写，模拟了基金经理、分析师、交易员等多个角色。其价值在于展示了一个完整的、可运行的AI驱动决策流水线。
- **借鉴价值**：是理解如何用代码构建一个端到端的AI投研决策流程的最佳入门项目，其角色定义和交互逻辑值得参考。
- **潜在风险**：纯粹是模拟环境，不连接真实市场，所有决策和收益均为虚构，切勿将其逻辑直接用于实盘。

### 3.5 RyanCodrai/turbovec
- **解决问题**：为大规模向量搜索提供高性能解决方案，特别针对量化金融中的向量化因子和相似性搜索场景。
- **为何值得关注**：24小时涨星173，增长迅速。其核心是Rust编写并提供Python绑定，兼顾性能与易用性，直接对标FAISS。
- **技术栈/架构亮点**：基于`TurboQuant`，利用`AVX512`, `SIMD`等指令集进行硬件加速。Topics中的`quantization`和`vector-search`表明其专为高性能计算场景设计。
- **借鉴价值**：在量化研究中，可用于海量因子向量的快速检索、相似K线模式匹配等，是构建高频因子挖掘系统的潜在核心组件。
- **潜在风险**：项目较新（创建于2026年3月），社区和文档可能尚不完善，依赖风险较高。

### 3.6 xbtlin/ai-berkshire
- **解决问题**：将巴菲特、芒格等四位投资大师的方法论，通过多Agent框架实现为自动化的价值投资研究工具。
- **为何值得关注**：7日涨星556，概念独特。它将价值投资的定性分析与AI Agent的定量能力结合，探索了一种新的投研范式。
- **技术栈/架构亮点**：Python编写，基于`Claude Code / Codex`，采用多Agent并行和对抗分析架构。Topics中包含`value-investing`, `fundamental-analysis`。
- **借鉴价值**：其“大师方法论数字化”和“多Agent对抗分析”的思路，可应用于任何需要深度、多角度研究的领域，如上市公司尽调、产业链分析。
- **潜在风险**：价值投资依赖于长期判断，AI模型可能无法真正理解商业本质，分析结果可能流于表面。

### 3.7 brokermr810/QuantDinger
- **解决问题**：提供一个覆盖加密货币、股票、外汇的全品类AI量化交易平台，集成回测、实盘、数据和多Agent研究。
- **为何值得关注**：试图打造一个“All-in-One”的AI量化平台，功能全面，符合个人开发者对一体化工具的需求。
- **技术栈/架构亮点**：Python编写，集成了`mcp-server`，支持`binance`, `coinbase`等主流交易所。架构上强调多资产、多策略的统一管理。
- **借鉴价值**：其统一的多资产、多策略管理平台架构，以及MCP服务器的集成方式，对设计综合交易平台有参考意义。
- **潜在风险**：项目涉及实盘交易和交易所API，存在安全风险。`crypto_related`标签提示其涉及高风险市场。功能过于全面可能导致每个模块都不够深入。

### 3.8 MIgHTy-alIeN/Trading-Bot (高风险警示)
- **解决问题**：声称是一个由外部脚本控制的链上套利机器人。
- **为何值得关注**：作为反面案例值得关注。该项目创建仅1天，star数仅300，但24小时涨星121，增长异常。
- **技术栈/架构亮点**：使用Solidity编写智能合约。Topics中包含`mev`, `mevbots`，是典型的区块链套利机器人。
- **潜在风险**：**风险极高**。此类项目通常是诈骗（Rug Pull）或蜜罐（Honeypot），旨在窃取用户的私钥或资金。代码中极有可能包含后门。**强烈不建议运行、编译或与之交互**。

## 4. 趋势归纳
- **技术趋势**：
    - **AI Agent 技能化与模块化**：从`ui-ux-pro-max-skill`到`NVIDIA/skills`，Agent的能力正在被封装为可复用、可组合的“技能包”，这将成为构建复杂金融Agent的标准方式。
    - **多Agent协作框架成熟**：`Vibe-Trading`、`TradingAgents`等项目表明，多Agent分工与辩论机制已成为AI交易框架的主流架构。
    - **高性能计算与AI推理本地化**：`turbovec`、`llama.cpp`、`ds4`等项目反映了量化交易对低延迟、高吞吐和本地化部署的持续追求。
- **产品趋势**：
    - **AI原生设计工具赋能金融UI**：`open-design`等工具让快速生成专业的交易仪表盘、研究报告成为可能，降低了金融产品的UI开发门槛。
    - **“一人华尔街”式全能Agent涌现**：`OpenAlice`、`QuantDinger`等项目试图打造覆盖全资产、全流程的个人AI交易助手。
- **量化/交易策略趋势**：
    - **LLM与经典策略深度融合**：AI不再仅用于因子挖掘，而是开始扮演“基金经理”、“分析师”等角色，参与顶层决策。
    - **另类数据与非结构化数据分析**：`transcribe.cpp`（语音转文字）、`depth-anything.cpp`（深度估计）等项目暗示，对财报电话会、卫星图像等非传统数据的分析能力正在增强。
- **AI Agent 与自动化交易结合趋势**：
    - **MCP成为Agent连接工具的通用标准**：`Vibe-Trading`、`QuantDinger`、`tradingview-mcp`等项目都集成了MCP，使其成为Agent与外部数据源、交易接口交互的通用协议。
    - **从决策支持到自动执行**：项目正从简单的“分析建议”向“研究-决策-执行-管理”的全流程自动化演进。
- **值得后续做原型验证的方向**：
    - 基于MCP协议，构建一个可插拔的金融数据与交易工具Agent生态。
    - 利用`planning-with-files`的思想，为交易Agent实现跨会话的长期任务规划和状态管理。

## 5. 今日灵感清单
1.  **MVP：AI交易仪表盘生成器**：结合`ui-ux-pro-max-skill`和`open-design`，做一个能根据自然语言描述，自动生成加密货币或股票实时监控仪表盘原型的工具。
2.  **调研：MCP在量化交易中的最佳实践**：深入研究`Vibe-Trading`和`QuantDinger`的MCP集成方式，总结一套为交易Agent开发MCP Server的规范。
3.  **Demo复现：多Agent价值投资分析**：参考`ai-berkshire`的架构，用LangChain或类似框架，快速搭建一个模拟巴菲特、芒格和彼得·林奇对话讨论某只股票的多Agent Demo。
4.  **原型验证：基于`turbovec`的因子相似性搜索**：将历史行情数据转化为因子向量，利用`turbovec`构建索引，验证其在“寻找相似历史行情片段”任务上的速度优势。
5.  **工具开发：Agent长期任务规划器**：借鉴`planning-with-files`，为交易Agent开发一个基于Markdown文件的任务规划器，使其能记住并持续执行“每周五分析持仓风险”这类长期指令。
6.  **加入Watchlist：`NVIDIA/skills`**：关注NVIDIA官方发布的Agent技能，了解行业巨头对Agent能力封装的标准和方向。
7.  **加入Watchlist：`Orchestra-Research/AI-Research-SKILLs`**：该项目旨在为AI Agent提供深度研究技能，未来可能包含金融分析模块，值得持续跟踪。
8.  **安全审计：`MIgHTy-alIeN/Trading-Bot`**：将其作为反面教材，分析其代码和宣传模式，总结识别区块链交易机器人骗局的方法论。

## 6. Watchlist 建议
- **HKUDS/Vibe-Trading**：当前最前沿的AI多Agent交易框架，其架构演进方向值得持续关注。
- **RyanCodrai/turbovec**：高性能向量搜索是量化研究的基础设施，该项目有潜力成为重要组件。
- **xbtlin/ai-berkshire**：独特的“AI+价值投资”方法论，其多Agent对抗分析模式具有启发性。
- **NVIDIA/skills**：官方发布的Agent技能，是事实上的行业标准风向标。
- **Orchestra-Research/AI-Research-SKILLs**：专注于为Agent注入深度研究能力，未来可能成为金融AI Agent的重要技能来源。
- **TraderAlice/OpenAlice**：全资产类别的AI交易Agent，其产品化思路和架构值得观察。

## 7. 风险提醒
- **GitHub star 不是投资建议**：高星项目不代表其策略能盈利，仅代表其社区关注度高。
- **不运行未知 trading bot**：特别是`MIgHTy-alIeN/Trading-Bot`这类新创建、描述模糊、涉及区块链套利的项目，极有可能是骗局。
- **不泄露交易所 API key**：任何要求输入API Key的第三方开源工具，在使用前都必须进行彻底的安全审计。
- **注意策略风险**：马丁、网格、套利、杠杆类策略存在巨大爆仓风险。回测结果可能存在幸存者偏差和过拟合，不能代表未来表现。
- **注意合规风险**：自动化交易可能违反交易所服务条款或当地金融法规。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
- **基线数据**：本次报告使用了 `2026-07-17` 的1日基线和 `2026-07-11` 的7日基线数据，涨星数据可靠。
- **数据缺失**：所有项目的 `star_delta_30d` 字段均为 `null`，无法提供30日涨星数据。
- **样本偏差**：候选项目列表由特定关键词和topic搜索生成，可能偏向于AI交易、回测和加密货币方向，未能完全覆盖传统金融科技的所有领域。
- **分类偏差**：部分项目（如 `build-your-own-x`）因描述或readme中包含匹配关键词而被归类为 `trading_bot`，其实际内容与金融交易无关，分析时已进行甄别。
