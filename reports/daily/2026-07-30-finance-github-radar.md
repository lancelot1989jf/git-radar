# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-07-30

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI Agent 与量化交易的深度融合**：以 `Vibe-Trading`、`TradingAgents` 为代表的多智能体交易框架持续火爆，AI 正在从辅助分析工具演变为交易决策的核心参与者。
    2.  **金融数据工程与本地化工具链**：`free-stockdb`、`a-stock-data` 等项目表明，面向特定市场（如A股）的本地化、一站式数据获取与回测工具需求旺盛。
    3.  **AI 治理与风控工具萌芽**：`iFixAi` 这类专注于 AI Agent 审计、对齐与安全评估的项目开始崭露头角，预示着 AI 交易系统的合规与风控将成为下一个焦点。
- **是否出现新趋势**：出现了“AI Agent 审计”这一细分方向，旨在解决 AI 代理在金融等高风险领域的行为可信度问题。同时，将 Claude Code、Codex 等编程 Agent 直接应用于金融分析（如 `ai-berkshire`）和交易图表交互（如 `tradingview-mcp`）的模式正在固化。
- **是否出现值得复刻/参考的工程架构**：`Vibe-Trading` 和 `TradingAgents` 的多智能体协作架构，以及 `daily_stock_analysis` 的 LLM 驱动多源数据聚合与推送架构，值得深入研究。
- **是否有明显骗局、过度营销或高风险项目**：`TG-Polymarket-bot` 属于典型的“跟单/喊单”机器人，风险极高。多数项目为研究型工具，但 `freqtrade`、`QuantDinger` 等直接连接交易所的实盘交易 Bot 需警惕 API Key 泄露和策略失效风险。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|:---:|:---|:---:|:---:|:---:|:---:|:---|:---|:---|:---:|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 111.9k | +387 | +2419 | Python | AI设计技能 | 为多平台提供专业UI/UX设计智能的AI技能包 | 低：非金融项目 | 低 |
| 2 | codecrafters-io/build-your-own-x | 533.1k | +298 | +2190 | Markdown | 教程集合 | 通过复刻热门技术来掌握编程的教程大全 | 低：非金融项目 | 中 |
| 3 | awesome-selfhosted/awesome-selfhosted | 309.5k | +279 | +1774 | - | 自托管服务列表 | 可自托管的免费软件网络服务和Web应用列表 | 低：非金融项目 | 中 |
| 4 | HKUDS/Vibe-Trading | 28.8k | +219 | +1816 | Python | AI交易/回测 | 个人AI交易代理，多智能体框架 | **高**：多Agent交易架构 | 中 |
| 5 | nexu-io/open-design | 82.8k | +208 | +1726 | TypeScript | AI设计工具 | 开源AI设计引擎，本地优先，支持多种编程Agent | 低：非金融项目 | 低 |
| 6 | shiyu-coder/Kronos | 35.1k | +136 | +1981 | Python | 量化研究 | 金融市场语言的基础模型 | **高**：金融基础模型 | 低 |
| 7 | ifixai-ai/iFixAi | 3.7k | +112 | +1723 | Python | AI风控/审计 | 独立审计AI Agent，确保其行为符合预期 | **极高**：AI交易风控新范式 | 低 |
| 8 | public-apis/public-apis | 453.7k | +307 | +1447 | Python | API列表 | 免费API集合列表 | 低：非金融项目 | 中 |
| 9 | VoltAgent/awesome-design-md | 105.6k | +164 | +1433 | - | 设计系统 | 流行品牌设计系统分析集合，供编程Agent生成UI | 低：非金融项目 | 中 |
| 10 | vinta/awesome-python | 311.3k | +191 | +1315 | Python | Python资源列表 | Python框架、库、工具和资源大全 | 低：非金融项目 | 低 |
| 11 | ZhuLinsen/daily_stock_analysis | 59.6k | +90 | +1138 | Python | AI股票分析 | LLM驱动的多市场股票智能分析系统 | **高**：LLM金融分析应用 | 低 |
| 12 | ruvnet/ruflo | 66.6k | +106 | +889 | TypeScript | AI Agent框架 | 领先的Agent元框架，部署智能多玩家群体 | **高**：Agent协作架构 | 低 |
| 13 | xbtlin/ai-berkshire | 14.8k | +50 | +1005 | Python | AI价值投资 | 基于Claude/Codex的价值投资研究框架 | **高**：AI驱动的投研框架 | 低 |
| 14 | TauricResearch/TradingAgents | 95.1k | +89 | +749 | Python | AI交易/回测 | 多智能体LLM金融交易框架 | **高**：经典多Agent交易框架 | 低 |
| 15 | ripienaar/free-for-dev | 130.9k | +96 | +635 | HTML | 开发者资源 | 对开发者和运维有吸引力的免费SaaS/PaaS/IaaS列表 | 低：非金融项目 | 低 |
| 16 | avelino/awesome-go | 179.7k | +83 | +679 | Go | Go资源列表 | Go框架、库和软件的精选列表 | 低：非金融项目 | 中 |
| 17 | hello245m/free-stockdb | 1.6k | +34 | +1015 | HTML | 量化数据/回测 | 面向A股的本地量化引擎，集成数据同步与回测 | **高**：本地化量化数据方案 | 低 |
| 18 | hesreallyhim/awesome-claude-code | 51.4k | +79 | +571 | Python | Claude资源 | Claude Code相关资源精选集合 | 低：非金融项目 | 低 |
| 19 | unslothai/unsloth | 69.2k | +107 | +430 | Python | 模型训练 | 本地UI，用于训练和运行多种大语言模型 | 低：非金融项目 | 低 |
| 20 | quantskills/quantskills | 1.7k | +67 | +693 | JavaScript | 量化导航 | QuantSkills组织的全景导航 | 低：非金融项目 | 低 |
| 21 | code-yeongyu/oh-my-openagent | 66.9k | +80 | +400 | TypeScript | AI Agent框架 | 面向复杂代码库的编程Agent框架 | 低：非金融项目 | 低 |
| 22 | garrytan/gbrain | 27.4k | +62 | +476 | TypeScript | AI Agent大脑 | 一个固执己见的OpenClaw/Hermes Agent大脑 | 低：非金融项目 | 低 |
| 23 | karanpratapsingh/system-design | 45.0k | +113 | +365 | - | 系统设计 | 学习大规模系统设计及面试准备 | 低：非金融项目 | 低 |
| 24 | langfuse/langfuse | 32.2k | +76 | +445 | TypeScript | LLM运维 | 开源AI工程平台：LLM评估、可观测性、提示管理 | **中**：LLM应用监控 | 低 |
| 25 | ashishpatel26/500-AI-Agents-Projects | 35.4k | +81 | +378 | Python | AI Agent案例 | 500个AI Agent用例集合，含金融等领域 | 低：非金融项目 | 中 |
| 26 | RyanCodrai/turbovec | 14.5k | +23 | +593 | Rust | 向量搜索 | 基于TurboQuant的向量索引，Rust编写，Python绑定 | **中**：高性能金融向量搜索 | 低 |
| 27 | simonlin1212/a-stock-data | 8.1k | +41 | +457 | - | A股数据工具 | A股全栈数据工具包，43个端点，15个数据源 | **高**：A股数据工程方案 | 低 |
| 28 | antirez/ds4 | 19.5k | +46 | +348 | C | 模型推理 | DeepSeek 4 Flash/PRO本地推理引擎 | 低：非金融项目 | 低 |
| 29 | Fincept-Corporation/FinceptTerminal | 29.3k | +30 | +462 | C++ | 金融终端 | 现代金融应用，提供高级市场分析和投资研究工具 | **高**：开源金融终端参考 | 低 |
| 30 | punkpeye/awesome-mcp-servers | 91.6k | +41 | +321 | - | MCP服务器 | MCP服务器集合 | 低：非金融项目 | 低 |
| 31 | headroomlabs-ai/headroom | 63.4k | +201 | - | Python | Token优化 | 压缩工具输出、日志、文件，为LLM节省Token | **中**：降低LLM金融分析成本 | 低 |
| 32 | OpenBB-finance/OpenBB | 71.2k | +26 | +256 | Python | 金融数据平台 | 面向分析师、量化分析师和AI Agent的开放数据平台 | **高**：金融数据平台标杆 | 中 |
| 33 | nidhinjs/prompt-master | 10.9k | +70 | +195 | - | 提示工程 | 为任何AI工具编写准确提示的Claude技能 | 低：非金融项目 | 低 |
| 34 | calesthio/Crucix | 11.0k | +22 | +473 | JavaScript | 情报Agent | 个人情报代理，监控多数据源并在变化时通知 | **中**：事件驱动型监控Agent | 低 |
| 35 | tradesdontlie/tradingview-mcp | 5.4k | +29 | +240 | JavaScript | 交易图表MCP | 将Claude Code连接到TradingView桌面端，实现工作流自动化 | **高**：AI+图表分析交互 | 中 |
| 36 | freqtrade/freqtrade | 52.8k | +21 | +187 | Python | 加密交易机器人 | 免费、开源的加密货币交易机器人 | **中**：经典交易Bot架构参考 | 中 |
| 37 | josephmisiti/awesome-machine-learning | 73.8k | +26 | +137 | Python | ML资源列表 | 精选机器学习框架、库和软件列表 | 低：非金融项目 | 低 |
| 38 | OthmanAdi/planning-with-files | 25.9k | +23 | +179 | Python | Agent规划 | 为AI编程Agent设计的持久化文件规划系统 | **中**：Agent任务持久化与恢复 | 低 |
| 39 | 0x4m4/hexstrike-ai | 10.7k | +69 | +201 | Python | 安全Agent | 让AI Agent自主运行150+网络安全工具的MCP服务器 | 低：非金融项目 | 低 |
| 40 | OpenByteInc/QuantDinger | 10.1k | +17 | +195 | Python | AI量化平台 | 面向加密、股票、外汇的AI量化交易平台 | **中**：多市场AI交易平台 | 中 |
| 41 | fffaraz/awesome-cpp | 72.5k | +17 | +118 | - | C++资源列表 | 精选C/C++框架、库和资源列表 | 低：非金融项目 | 低 |
| 42 | rust-unofficial/awesome-rust | 58.6k | +22 | +116 | Rust | Rust资源列表 | 精选Rust代码和资源列表 | 低：非金融项目 | 低 |
| 43 | virattt/ai-hedge-fund | 62.5k | +16 | +110 | Python | AI对冲基金 | 一个AI对冲基金团队模拟 | **高**：AI投研决策模拟 | 低 |
| 44 | Orchestra-Research/AI-Research-SKILLs | 11.3k | +30 | +228 | TeX | AI研究技能 | 面向任何AI模型的AI研究和工程技能开源库 | 低：非金融项目 | 低 |
| 45 | TraderAlice/OpenAlice | 6.3k | +25 | +139 | TypeScript | AI交易Agent | 覆盖股票、加密、商品等全资产的AI交易代理 | **高**：全资产AI交易Agent | 中 |
| 46 | mothparkzo6249/TG-Polymarket-bot | 89 | +88 | - | JavaScript | 交易机器人 | 捕捉Polymarket鲸鱼交易并一键跟单的Telegram机器人 | **极低**：高风险跟单 | 中 |
| 47 | Developer-Y/cs-video-courses | 82.8k | +10 | +147 | - | CS课程 | 计算机科学视频课程列表 | 低：非金融项目 | 中 |
| 48 | elementalsouls/Claude-BugHunter | 3.3k | +10 | +218 | Python | 安全技能 | 用于漏洞挖掘和红队工作的Claude Code技能包 | 低：非金融项目 | 低 |
| 49 | alvinreal/awesome-opensource-ai | 4.4k | +7 | +182 | Python | AI资源列表 | 精选真正开源的AI项目、模型、工具和基础设施列表 | 低：非金融项目 | 低 |
| 50 | vuejs/awesome-vue | 73.6k | -3 | -7 | - | Vue资源列表 | Vue.js相关精选资源列表 | 低：非金融项目 | 低 |
| 51 | ByteByteGoHq/system-design-101 | 86.6k | +32 | +192 | - | 系统设计 | 用视觉和简单术语解释复杂系统 | 低：非金融项目 | 低 |

## 3. 重点项目深度分析

### 3.1 HKUDS/Vibe-Trading
- **项目解决什么问题**：旨在打造一个“个人AI交易代理”，通过多智能体框架实现从市场分析到交易执行的自动化。
- **为什么最近值得关注**：7日涨星高达1816，是AI交易领域最火的项目之一。它代表了从单一策略机器人向多Agent协作交易系统演进的趋势。
- **技术栈/架构亮点**：Python编写，集成了LLM、MCP（Model Context Protocol）和多Agent架构。其架构允许不同Agent扮演分析师、交易员、风控官等角色，协同工作。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**非常适合**。其多Agent角色分工和协作模式是构建复杂交易系统的优秀参考，可以借鉴其Agent间通信和决策机制。
- **可能的风险**：作为研究工具，其策略在实盘中的有效性未知，存在过拟合风险。直接用于实盘交易可能导致资金损失。

### 3.2 shiyu-coder/Kronos
- **项目解决什么问题**：构建一个“金融市场语言的基础模型”，试图用统一的模型来理解和预测金融市场的复杂行为。
- **为什么最近值得关注**：7日涨星高达1981，是金融大模型方向的明星项目。它代表了将基础模型范式应用于金融时序数据的尝试。
- **技术栈/架构亮点**：Python项目，具体模型架构信息不足，但从其定位来看，很可能基于Transformer或其变体，在海量金融数据上进行预训练。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**非常适合作为研究方向**。可以借鉴其思路，探索用预训练模型生成通用金融特征，或作为下游交易策略的输入。
- **可能的风险**：金融信噪比极低，基础模型可能学到的是噪声而非真实规律。模型可能过度依赖历史模式，在市场风格切换时失效。维护活跃度存疑（最近push在4月）。

### 3.3 ifixai-ai/iFixAi
- **项目解决什么问题**：解决AI Agent经济中最关键的问题：“Agent是否在做它应该做的事？”。提供对AI Agent的独立审计，可在120秒内给出答案。
- **为什么最近值得关注**：7日涨星1723，是AI治理和风控领域的一匹黑马。随着AI Agent在金融交易中的应用增多，对其行为的审计和约束变得至关重要。
- **技术栈/架构亮点**：Python项目，集成了AI评估、幻觉检测、提示注入检测、合规性检查（如EU AI Act, ISO 42001）等功能。其“由人或Agent自身运行”的设计非常灵活。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**极具借鉴价值**。这是构建可信AI交易系统的关键一环。可以将其审计功能作为交易Agent流水线中的一个强制步骤，在执行高风险操作前进行行为合规性检查。
- **可能的风险**：审计本身的准确性和完备性是关键，可能存在漏报或误报。项目较新，成熟度有待观察。

### 3.4 ZhuLinsen/daily_stock_analysis
- **项目解决什么问题**：提供一个LLM驱动的多市场股票智能分析系统，整合多源行情、实时新闻，并生成决策看板与自动推送。
- **为什么最近值得关注**：7日涨星1138，是LLM在金融分析领域落地的成功案例。它展示了如何将AI与数据工程结合，为投资者提供一站式分析服务。
- **技术栈/架构亮点**：Python项目，架构上集成了多源数据（行情、新闻）、LLM分析引擎、决策看板（Dashboard）和自动推送通知。支持零成本定时运行，体现了良好的工程化设计。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**非常适合**。其数据聚合、LLM分析、结果展示与推送的完整流水线设计，是构建AI投研助手或交易信号生成器的优秀模板。
- **可能的风险**：LLM生成的“决策”可能存在幻觉或偏见，不能直接作为投资依据。数据源的稳定性和时效性会影响系统可靠性。

### 3.5 xbtlin/ai-berkshire
- **项目解决什么问题**：将巴菲特、芒格等四位投资大师的方法论与多Agent并行研究相结合，构建一个AI时代的价值投资研究框架。
- **为什么最近值得关注**：7日涨星1005，是将经典投资思想与前沿AI技术结合的创新尝试。它探索了用AI Agent模拟不同投资风格的分析师，进行对抗性研究。
- **技术栈/架构亮点**：Python项目，基于Claude Code/Codex。其核心是“多Agent对抗分析”，让不同Agent代表不同投资哲学，对同一标的进行分析和辩论，最终形成综合判断。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**极具借鉴价值**。其“多角色对抗”的Agent架构是提升AI决策鲁棒性的有效方法，可以应用于风险管理、策略评估等场景。
- **可能的风险**：价值投资本身需要长期验证，AI模拟的有效性存疑。项目依赖商业LLM的API，存在成本和安全风险。

### 3.6 TauricResearch/TradingAgents
- **项目解决什么问题**：提供一个成熟的多智能体LLM金融交易框架，用于模拟和实现基于多Agent协作的交易策略。
- **为什么最近值得关注**：总星数高达95k，是该领域的标杆项目。其持续的星数增长（7d +749）表明市场对多Agent交易框架的持续关注。
- **技术栈/架构亮点**：Python项目，拥有清晰的Agent角色定义和协作流程。作为一个框架，它提供了回测和模拟环境，方便研究人员快速实验。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**非常适合**。它是研究多Agent交易系统架构、Agent间通信协议和决策融合机制的绝佳参考。
- **可能的风险**：框架本身不提供盈利策略，用户需自行开发。回测环境可能与实盘存在差异，导致策略迁移失败。

### 3.7 hello245m/free-stockdb
- **项目解决什么问题**：为A股量化研究者提供一个本地化的量化引擎，解决了数据获取、存储、复权和回测的一站式需求。
- **为什么最近值得关注**：7日涨星高达1015，对于一个仅1.6k星的项目来说增速惊人。它精准地抓住了A股量化社区对免费、可靠、本地化数据工具的痛点。
- **技术栈/架构亮点**：项目描述为HTML，但核心应是Python后端。架构亮点在于“本地优先”，集成增量同步、本地缓存、复权、批量查询等功能，并支持MCP协议，方便AI Agent调用。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**非常适合**。其“本地数据引擎+MCP接口”的模式，是构建AI量化交易系统的理想数据层解决方案，可以方便地被AI Agent集成和调用。
- **可能的风险**：数据源可能存在合规风险。项目较新，数据质量和系统稳定性需要时间检验。

### 3.8 virattt/ai-hedge-fund
- **项目解决什么问题**：模拟一个由AI Agent组成的对冲基金团队，展示如何利用多Agent协作进行投资决策。
- **为什么最近值得关注**：总星数高达62.5k，是AI金融领域的经典模拟项目。它生动地展示了AI Agent在投资分析、决策和风险管理中的潜力。
- **技术栈/架构亮点**：Python项目，通过定义不同角色的Agent（如基本面分析师、技术分析师、交易员、风控官）来模拟对冲基金的决策流程。
- **是否适合借鉴到AI/自动化交易/企业级Agent框架中**：**非常适合作为教学和原型验证**。其Agent角色定义和交互流程是理解AI投研团队协作的绝佳起点。
- **可能的风险**：这是一个模拟项目，其决策不能直接用于实盘。模拟环境简化了市场复杂性，可能导致对AI能力的过度乐观。

## 4. 趋势归纳
- **技术趋势**：
    - **多智能体协作**：`Vibe-Trading`、`TradingAgents`、`ai-berkshire` 等项目共同指向了多Agent分工、对抗与协作的架构趋势。
    - **MCP协议成为AI Agent交互标准**：`free-stockdb`、`tradingview-mcp` 等项目通过MCP将数据、工具与AI Agent连接，MCP正成为AI应用生态的通用接口。
    - **金融基础模型**：`Kronos` 的出现预示着金融领域也开始探索自己的基础模型，试图从海量数据中学习通用表征。
- **产品趋势**：
    - **AI原生投研工具**：`daily_stock_analysis`、`ai-berkshire` 等不再是简单的数据展示，而是由AI驱动分析、生成洞察的“AI原生”产品。
    - **本地化与一站式**：`free-stockdb`、`a-stock-data` 等项目强调本地部署、数据自有、功能一站式，满足对数据隐私和定制化有高要求的专业用户。
- **量化/交易策略趋势**：
    - **从策略到系统**：关注点从寻找单一“圣杯”策略，转向构建鲁棒的、多Agent协作的复杂交易系统。
    - **AI驱动的非结构化数据分析**：利用LLM分析新闻、研报、舆情等非结构化数据，并将其融入决策流程。
- **AI Agent 与自动化交易结合趋势**：
    - **Agent审计与风控**：`iFixAi` 的出现是标志性事件，意味着AI Agent在交易中的应用开始从“能不能做”转向“做得对不对、安不安全”。
    - **人机协作新范式**：`tradingview-mcp` 展示了AI Agent如何融入现有交易员工作流，辅助而非取代人类进行图表分析。
- **值得后续做原型验证的方向**：
    - 集成 `iFixAi` 审计功能的交易Agent沙箱。
    - 基于 `free-stockdb` 和 `Vibe-Trading` 架构的A股多Agent交易原型。
    - 利用 `Kronos` 模型生成的特征进行策略回测。

## 5. 今日灵感清单
1.  **构建一个“AI交易风控官”MVP**：参考 `iFixAi` 的思路，为 `freqtrade` 或 `Vibe-Trading` 开发一个插件，在交易指令执行前，由另一个LLM Agent进行合规性、风险度和行为一致性审计。
2.  **复现“多Agent价值投资辩论”Demo**：借鉴 `ai-berkshire` 的架构，用LangGraph或CrewAI快速搭建一个让巴菲特风格Agent、芒格风格Agent和段永平风格Agent对同一只股票进行辩论的原型。
3.  **调研金融基础模型 `Kronos`**：深入研究其论文和代码，评估其生成的Embedding在A股市场的选股或行业轮动策略中的有效性。
4.  **开发一个“MCP数据网关”**：参考 `free-stockdb` 和 `a-stock-data`，将多个金融数据源（如Tushare、AkShare、WindPy）封装成统一的MCP Server，供任何AI Agent调用。
5.  **为 `TradingView` 开发AI分析技能包**：基于 `tradingview-mcp` 项目，开发一套Claude Code Skills，让AI能自动识别图表形态、计算技术指标并生成分析报告。
6.  **搭建一个“LLM金融分析成本优化器”**：利用 `headroom` 项目的技术，对 `daily_stock_analysis` 等项目的LLM输入进行压缩，在保持分析质量的同时，大幅降低API调用成本。
7.  **设计一个“事件驱动型情报Agent”**：参考 `Crucix` 的设计，构建一个专注于金融市场的Agent，监控特定股票、行业的新闻、公告、社交媒体异动，并通过企微/钉钉实时推送。
8.  **将 `OpenBB` 集成到Agent工作流中**：`OpenBB` 是强大的金融数据平台，可以将其作为数据源，集成到 `TradingAgents` 或自定义的交易Agent中，替代简单的数据爬虫。

## 6. Watchlist 建议
- **HKUDS/Vibe-Trading**：AI多Agent交易框架的当红项目，其架构演进和社区贡献值得持续追踪。
- **ifixai-ai/iFixAi**：AI Agent审计赛道的开拓者，其发展将直接影响AI交易系统的可信度，是风控领域的前沿。
- **shiyu-coder/Kronos**：金融基础模型的重要探索，其模型能力和后续应用值得关注。
- **hello245m/free-stockdb**：A股本地量化数据解决方案的黑马，其MCP集成模式是AI+数据工程的优秀范例。
- **xbtlin/ai-berkshire**：将经典投资思想与多Agent技术结合的创新项目，其方法论和架构有很高的参考价值。
- **tradesdontlie/tradingview-mcp**：AI Agent与现有交易工具结合的桥梁，代表了人机协作的新方向。
- **TraderAlice/OpenAlice**：覆盖全资产类别的AI交易Agent，其全市场视角和TypeScript技术栈值得关注。

## 7. 风险提醒
- **GitHub star 不是投资建议**：高星数仅代表社区关注度，不代表项目盈利能力或策略有效性。
- **不运行未知 trading bot**：`TG-Polymarket-bot` 等来源不明的交易机器人存在极高的资金盗窃和策略欺诈风险。
- **不泄露交易所 API key**：任何要求输入交易所API Key的开源项目，在使用前都必须进行严格的代码审计，防止Key泄露。
- **注意马丁、网格、套利、杠杆类项目的爆仓风险**：`freqtrade`、`QuantDinger` 等项目支持高风险策略，不当使用可能导致本金全部损失。
- **注意回测幸存者偏差和过拟合**：`Vibe-Trading`、`TradingAgents` 等项目的回测结果可能过于乐观，实盘表现可能大相径庭。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
- **基线数据**：本次报告使用了 `2026-07-29` 的1日基线和 `2026-07-23` 的7日基线数据，涨星数据完整。
- **采集失败**：部分项目（如 `headroomlabs-ai/headroom`、`mothparkzo6249/TG-Polymarket-bot`）缺少7日涨星数据，可能是由于项目创建时间过短或基线数据中不存在。
- **样本偏差**：候选项目列表由关键词匹配和Topic筛选生成，可能偏向于描述中包含特定术语的项目，无法完全代表GitHub上所有金融科技项目的全貌。部分项目（如 `build-your-own-x`）因描述或Readme中包含匹配词而被收录，但其本身并非金融项目，请注意甄别。
