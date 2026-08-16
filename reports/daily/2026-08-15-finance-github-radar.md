# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-15

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 与投研/交易工作流深度融合**：`TradingAgents`、`Vibe-Trading`、`ai-berkshire`、`daily_stock_analysis` 等项目显示，多 Agent 框架正在从“聊天机器人”形态转向“可执行投研流水线”，覆盖数据获取、新闻分析、决策看板、自动推送等环节。
  2. **本地优先 / 本地推理基础设施**：`unsloth`、`colibri`、`ds4`、`needle` 等项目聚焦在消费级硬件上运行前沿模型，这对金融场景中“数据不出域、模型本地部署”的合规需求有直接借鉴价值。
  3. **A 股数据工程与自托管量化工作台**：`a-stock-data`、`free-stockdb`、`tickflow-stock-panel`、`Vibe-Research` 等项目集中出现，显示中文社区正在快速补齐 A 股数据获取、本地缓存、回测、LLM 分析的一体化工具链。

- **是否出现新趋势**：出现。候选集中“AI Agent + 金融数据 + 本地优先”三者交汇的趋势明显，尤其是以 Claude Code / Codex 作为 Agent 执行环境、以 MCP 作为数据接入层的项目数量显著增加。

- **是否出现值得复刻/参考的工程架构**：是。`TradingAgents` 的多 Agent 辩论式决策框架、`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送”流水线、`headroom` 的 LLM 上下文压缩代理、`planning-with-files` 的持久化文件规划机制，都具备可复刻的工程价值。

- **是否有明显骗局、过度营销或高风险项目**：候选集中存在若干需要警惕的项目。`Financial_freedom`（“最全赚钱投资指南”）名称和描述带有明显营销色彩，且 star 基数低、24h 涨星异常偏高，需谨慎对待。`ritmex-bot` 为 Perp DEX 交易机器人，star 基数仅 542，且 24h 涨星（+84）超过 7d 涨星（+83），属于典型短期脉冲，杠杆永续合约交易风险极高。此外，多个项目因关键词误匹配进入候选集（如 `public-apis`、`build-your-own-x`、`awesome-selfhosted`），并非真正的金融/量化项目，分析时需剔除噪声。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 460228 | +1619 | +5115 | Python | API 资源列表 | 免费 API 合集，非金融项目，关键词误匹配 | 低 | 中 |
| 2 | nexu-io/open-design | 86966 | +602 | +2388 | TypeScript | AI 设计工具 | 本地优先的 AI 设计桌面应用，可导出 HTML/PDF/PPTX | 中 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 117069 | +302 | +2302 | Python | AI 设计技能 | 面向多平台的 UI/UX 设计智能技能包 | 中 | 低 |
| 4 | unslothai/unsloth | 72069 | +545 | +2334 | Python | LLM 训练/微调 | 本地运行和训练 LLM/扩散模型的 UI | 高 | 低 |
| 5 | codecrafters-io/build-your-own-x | 540023 | +260 | +2161 | Markdown | 编程教程合集 | 从零重建技术的教程合集，非交易项目 | 低 | 中 |
| 6 | ZhuLinsen/daily_stock_analysis | 62971 | +88 | +2183 | Python | AI 股票分析 | LLM 驱动的多市场股票分析系统，支持零成本定时运行 | 高 | 低 |
| 7 | TauricResearch/TradingAgents | 98346 | +162 | +1823 | Python | 多 Agent 交易框架 | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 8 | JustVugg/colibri | 25060 | +313 | +1693 | C | 本地模型推理 | 纯 C、零依赖的 MoE 模型本地推理引擎 | 高 | 低 |
| 9 | awesome-selfhosted/awesome-selfhosted | 312920 | +218 | +1480 | 无 | 自托管列表 | 自托管服务列表，非交易项目 | 低 | 中 |
| 10 | VoltAgent/awesome-design-md | 108603 | +180 | +1275 | 无 | 设计系统列表 | DESIGN.md 文件合集，供编码 Agent 生成 UI | 中 | 中 |
| 11 | vinta/awesome-python | 314173 | +182 | +1241 | Python | Python 资源列表 | Python 框架/库/工具精选列表 | 低 | 低 |
| 12 | ifixai-ai/iFixAi | 8671 | +90 | +1286 | Python | AI Agent 审计 | AI Agent 独立审计工具，120 秒内评估 Agent 行为 | 高 | 低 |
| 13 | shiyu-coder/Kronos | 37304 | +113 | +1111 | Python | 金融基础模型 | 金融市场语言基础模型 | 高 | 低 |
| 14 | headroomlabs-ai/headroom | 66457 | +79 | +911 | Python | LLM 上下文压缩 | 压缩工具输出/日志/RAG 块，减少 token 消耗 | 高 | 低 |
| 15 | avelino/awesome-go | 181159 | +91 | +617 | Go | Go 资源列表 | Go 框架/库精选列表，非交易项目 | 低 | 中 |
| 16 | ripienaar/free-for-dev | 131908 | +95 | +572 | HTML | 免费资源列表 | SaaS/PaaS/IaaS 免费层列表 | 低 | 低 |
| 17 | HKUDS/Vibe-Trading | 30930 | +67 | +553 | Python | AI 交易 Agent | “Vibe-Trading”个人交易 Agent | 高 | 中 |
| 18 | ruvnet/ruflo | 67940 | +68 | +530 | TypeScript | Agent 编排框架 | 多玩家 swarm 协作的 Agent 元编排框架 | 中 | 低 |
| 19 | hesreallyhim/awesome-claude-code | 52388 | +77 | +448 | Python | Claude Code 资源 | Claude Code 技能/插件/工具精选 | 中 | 低 |
| 20 | codeman008/Financial_freedom | 2400 | +195 | +467 | 无 | 投资指南 | “最全赚钱投资指南”，营销色彩浓 | 低 | 中 |
| 21 | garrytan/gbrain | 28499 | +49 | +477 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 的定制化“大脑” | 中 | 低 |
| 22 | punkpeye/awesome-mcp-servers | 92393 | +64 | +416 | 无 | MCP 服务器列表 | MCP 服务器合集 | 中 | 低 |
| 23 | AtomicBot-ai/atomic-agent | 2226 | +55 | +569 | TypeScript | 本地优先 Agent | 本地优先 AI Agent，优化本地模型和长上下文 | 高 | 中 |
| 24 | antirez/ds4 | 21440 | +47 | +456 | C | 本地推理引擎 | DeepSeek 4 Flash/PRO 本地推理引擎，支持 Metal/CUDA/ROCm | 高 | 低 |
| 25 | code-yeongyu/oh-my-openagent | 67917 | +45 | +401 | TypeScript | 编码 Agent 编排 | 面向复杂代码库的编码 Agent 编排工具 | 中 | 低 |
| 26 | ashishpatel26/500-AI-Agents-Projects | 36532 | +39 | +481 | Python | AI Agent 案例集 | 500 个 AI Agent 用例合集 | 中 | 中 |
| 27 | AmazingAng/old-coder | 584 | +129 | +246 | Python | Agent 测试技能 | “证据优先”的编码 Agent 测试技能 | 高 | 低 |
| 28 | xbtlin/ai-berkshire | 15581 | +43 | +330 | Python | 价值投资研究 | 基于 Claude Code/Codex 的价值投资研究框架 | 高 | 低 |
| 29 | simonlin1212/a-stock-data | 8780 | +37 | +303 | 无 | A 股数据工具包 | A 股全栈数据工具包，43 端点、15 数据源 | 高 | 低 |
| 30 | OpenBB-finance/OpenBB | 71895 | +32 | +274 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高 | 中 |
| 31 | cactus-compute/needle | 6084 | +456 | 信息不足 | Python | 端侧基础模型 | 14MB 端侧基础模型，面向手机/可穿戴/机器人 | 中 | 中 |
| 32 | freqtrade/freqtrade | 53316 | +33 | +227 | Python | 加密交易机器人 | 免费开源加密交易机器人 | 中 | 中 |
| 33 | OpenSenseNova/SenseNova-U1 | 4829 | +38 | +260 | Python | 统一模型范式 | SenseNova-U 系列原生统一范式模型 | 低 | 低 |
| 34 | OpenByteInc/QuantDinger | 10700 | +22 | +299 | Python | AI 量化平台 | 加密/股票/外汇 AI 量化交易平台 | 中 | 中 |
| 35 | calesthio/Crucix | 11400 | +70 | +206 | JavaScript | 情报监控 Agent | 多数据源监控的个人情报 Agent | 中 | 低 |
| 36 | elementalsouls/Claude-BugHunter | 3608 | +26 | +272 | Python | 安全测试技能 | Claude Code 漏洞挖掘/红队技能包 | 中 | 低 |
| 37 | virattt/ai-hedge-fund | 62876 | +24 | +137 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 38 | discountry/ritmex-bot | 542 | +84 | +83 | TypeScript | Perp DEX 交易机器人 | 永续合约 DEX 交易机器人 | 低 | 中 |
| 39 | shy3130/tickflow-stock-panel | 2864 | +18 | +186 | Python | A 股量化工作台 | 自托管 A 股选股+监控+回测工作台 | 高 | 低 |
| 40 | OthmanAdi/planning-with-files | 26182 | +14 | +127 | Shell | Agent 规划技能 | 基于文件的持久化规划，防上下文丢失 | 高 | 低 |
| 41 | simonlin1212/Vibe-Research | 2057 | +32 | +135 | TypeScript | 投研 Agent | A 股/美股/港股个人投研 Agent | 高 | 低 |
| 42 | josephmisiti/awesome-machine-learning | 74046 | +13 | +90 | Python | ML 资源列表 | 机器学习框架/库精选列表 | 低 | 低 |
| 43 | ByteByteGoHq/system-design-101 | 87139 | +79 | +346 | 无 | 系统设计教程 | 系统设计图解教程 | 中 | 低 |
| 44 | fffaraz/awesome-cpp | 72780 | +12 | +115 | 无 | C++ 资源列表 | C/C++ 框架/库精选列表 | 低 | 低 |
| 45 | hello245m/free-stockdb | 2055 | +16 | +214 | HTML | A 股本地量化引擎 | A 股日 K/分钟 K/ETF 本地量化引擎 | 高 | 低 |
| 46 | rust-unofficial/awesome-rust | 58844 | +11 | +90 | Rust | Rust 资源列表 | Rust 代码/资源精选列表 | 低 | 低 |
| 47 | Developer-Y/cs-video-courses | 83055 | +10 | +98 | 无 | CS 课程列表 | 计算机科学视频课程列表 | 低 | 中 |
| 48 | vuejs/awesome-vue | 73544 | 0 | -13 | 无 | Vue 资源列表 | Vue.js 资源精选列表 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents

- **项目解决什么问题**：将 LLM 多 Agent 框架引入金融交易决策，通过多个专业 Agent（如基本面分析、技术分析、情绪分析、风险管理等）协作完成交易信号生成。
- **为什么最近值得关注**：7 日涨星 +1823，总 star 接近 10 万，是当前“AI Agent + 交易”方向最具代表性的开源项目之一。Apache-2.0 许可，适合二次开发。
- **技术栈/架构亮点**：Python 实现，多 Agent 协作架构，将交易决策拆解为可独立评估的子任务，再由汇总 Agent 形成最终决策。这种“辩论式/分工式”Agent 架构对降低单一 LLM 决策偏差有参考价值。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其多 Agent 分工模式可迁移到企业级投研流水线，例如将“数据获取、因子分析、风险审核、合规检查”拆分为独立 Agent，并引入对抗性审查环节。
- **可能的风险**：策略过拟合风险高；LLM 生成的交易信号缺乏可解释性和稳定性；回测结果可能受提示词和数据窗口影响显著；作为研究工具，不应直接用于实盘。

### 3.2 ZhuLinsen/daily_stock_analysis

- **项目解决什么问题**：提供 LLM 驱动的多市场股票智能分析，整合多源行情、实时新闻、决策看板和自动推送，支持零成本定时运行。
- **为什么最近值得关注**：7 日涨星 +2183，总 star 6.3 万，是 A 股 AI 分析方向的热门项目。MIT 许可，中文社区活跃。
- **技术栈/架构亮点**：Python 实现，多源数据接入 + LLM 分析 + 看板展示 + 自动推送的完整流水线。“零成本定时运行”的设计思路对个人开发者有吸引力。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其“数据采集 → LLM 分析 → 可视化 → 自动推送”的流水线模式可直接复刻为内部投研日报系统，也可作为 Agent 定时任务的参考实现。
- **可能的风险**：数据源稳定性依赖第三方接口；LLM 分析结果可能存在幻觉；自动推送若接入实盘决策，需严格人工复核。

### 3.3 HKUDS/Vibe-Trading

- **项目解决什么问题**：定位为“个人交易 Agent”，将 LLM 能力与交易流程结合，覆盖回测、组合优化、风险模型等环节。
- **为什么最近值得关注**：来自 HKUDS（香港大学数据科学实验室），具备学术背景。7 日涨星 +553，总 star 3.1 万。MIT 许可。
- **技术栈/架构亮点**：Python 实现，集成 MCP、多 Agent、回测框架。项目描述中明确提及 order book、portfolio optimization、risk model 等关键词，显示其试图覆盖从数据到风控的完整链路。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合作为研究参考。其“学术机构 + 开源 Agent 交易框架”的组合模式值得关注，尤其是 MCP 在金融数据接入层的应用。
- **可能的风险**：crypto_related 标记，涉及加密交易场景；作为研究工具，策略有效性未经长期验证；回测与实盘差距可能较大。

### 3.4 xbtlin/ai-berkshire

- **项目解决什么问题**：将巴菲特、芒格、段永平、李录四位投资人的方法论编码为多 Agent 研究框架，用于价值投资分析。
- **为什么最近值得关注**：7 日涨星 +330，总 star 1.6 万。将“投资哲学”转化为可执行的 Agent 工作流，是 AI 投研领域一个独特的产品化方向。
- **技术栈/架构亮点**：Python 实现，基于 Claude Code / Codex，采用多 Agent 并行研究和对抗性分析。将主观投资方法论结构化，是“专家知识 + LLM”结合的典型案例。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其“多大师方法论 + 多 Agent 对抗分析”的思路可迁移到企业级研究框架，例如将不同分析师的逻辑框架编码为独立 Agent，再进行交叉验证。
- **可能的风险**：价值投资方法论本身具有主观性，LLM 的模拟可能流于表面；研究结论不应直接作为投资决策依据。

### 3.5 simonlin1212/a-stock-data

- **项目解决什么问题**：提供 A 股全栈数据工具包，覆盖行情、研报、资金面、筹码、公告、打板、ETF 期权、舆情互动等 43 个端点、15 个数据源，并支持备用源降级。
- **为什么最近值得关注**：7 日涨星 +303，总 star 8780。A 股数据获取一直是中文量化社区的核心痛点，该项目试图提供一站式解决方案。
- **技术栈/架构亮点**：Apache-2.0 许可，强调“10 层架构”和“备用源降级”，显示其在数据工程层面有较完整的设计。支持 AI Agent / Claude Code 集成。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。数据源多样性和降级机制是生产级金融数据管道的关键设计，可直接作为 A 股数据层的参考实现。
- **可能的风险**：数据源合规性和稳定性风险；部分数据源可能涉及非官方接口；维护活跃度需持续观察。

### 3.6 hello245m/free-stockdb

- **项目解决什么问题**：面向 A 股日 K、分钟 K 与 ETF 分钟数据的本地量化引擎，集成增量同步、本地缓存、复权、批量查询、回测与指标计算。
- **为什么最近值得关注**：7 日涨星 +214，总 star 2055。本地优先的 A 股数据引擎，契合“数据不出域”的合规需求。
- **技术栈/架构亮点**：强调本地缓存、增量同步、复权处理，支持 MCP 接入。将数据获取、存储、回测、指标计算整合在一个本地引擎中，降低了个人量化研究的部署门槛。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其“本地优先 + 增量同步 + MCP 接入”的设计可作为企业级金融数据本地化部署的轻量参考。
- **可能的风险**：数据源稳定性；分钟级数据的存储和查询性能；回测引擎的准确性和过拟合风险。

### 3.7 ifixai-ai/iFixAi

- **项目解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，可在 120 秒内完成评估。
- **为什么最近值得关注**：7 日涨星 +1286，总 star 8671。AI Agent 治理和审计是当前企业级 Agent 落地的关键缺口，该项目直接切入这一痛点。
- **技术栈/架构亮点**：Python 实现，Apache-2.0 许可。覆盖 AI 对齐、幻觉检测、提示注入、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架，定位为企业级 AI 治理工具。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。在金融交易 Agent 场景中，对 Agent 行为的审计和合规检查是刚需。该项目的评估框架可迁移到交易 Agent 的“行为合规性检查”环节。
- **可能的风险**：审计覆盖度依赖规则库的完善程度；对复杂金融 Agent 的评估可能不够深入；需结合具体业务场景定制。

### 3.8 headroomlabs-ai/headroom

- **项目解决什么问题**：在工具输出、日志、文件和 RAG 块到达 LLM 之前进行压缩，减少 token 消耗，同时保持回答质量。
- **为什么最近值得关注**：7 日涨星 +911，总 star 6.6 万。LLM 上下文窗口管理是 Agent 系统的核心工程挑战，尤其在金融场景中，行情数据、新闻流、研报等输入量巨大。
- **技术栈/架构亮点**：Python 实现，提供库、代理和 MCP 服务器三种形态。宣称对编码 Agent 减少 20% token，对 JSON 减少 60-95% token。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。在金融 Agent 中，可将该压缩层用于行情数据、新闻流、日志等高频输入的预处理，降低上下文成本和噪声。
- **可能的风险**：压缩可能丢失关键信息，尤其在金融数据中，细微的数值变化可能影响决策；需在压缩率和信息保真度之间权衡。

### 3.9 OthmanAdi/planning-with-files

- **项目解决什么问题**：为 AI 编码 Agent 和长时运行任务提供基于文件的持久化规划，防止上下文丢失和会话中断导致的任务失败。
- **为什么最近值得关注**：7 日涨星 +127，总 star 2.6 万。长时运行 Agent 的状态管理是 Agent 工程的核心难题，该项目的“文件即状态”思路简洁有效。
- **技术栈/架构亮点**：Shell 实现，MIT 许可。通过 Markdown 计划文件实现崩溃恢复、会话恢复、上下文轮换注入和确定性完成门控。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。在交易 Agent 中，长时运行的任务（如持续监控、定时分析）需要可靠的状态持久化机制。该项目的文件规划模式可作为轻量级状态管理方案。
- **可能的风险**：文件并发访问和一致性问题；在分布式 Agent 场景中可能需要更强的状态管理方案。

### 3.10 AmazingAng/old-coder

- **项目解决什么问题**：为编码 Agent 提供“证据优先”的测试技能，强调不读代码而是让代码通过测试“闯关”，灵感来自 Uncle Bob。
- **为什么最近值得关注**：24h 涨星 +129，7 日涨星 +246，总 star 仅 584，属于早期高增长项目。将 TDD、变异测试、性质测试引入 Agent 开发流程，是 Agent 工程质量的差异化方向。
- **技术栈/架构亮点**：Python 实现，MIT 许可。覆盖变异测试、性质测试、规格驱动开发等测试方法论。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。在金融交易 Agent 中，策略逻辑的正确性验证至关重要。将“证据优先”的测试理念引入交易 Agent 开发，可降低策略实现错误的风险。
- **可能的风险**：项目处于早期阶段，star 基数低，维护活跃度和社区成熟度需观察。

## 4. 趋势归纳

### 技术趋势

1. **本地优先推理成为金融 AI 的基础设施方向**：`unsloth`、`colibri`、`ds4`、`needle` 等项目显示，在消费级硬件上运行前沿模型的技术正在快速成熟。对金融场景而言，这意味着“数据不出域、模型本地部署”的合规方案越来越可行。
2. **MCP 成为金融数据接入的标准接口**：`Vibe-Trading`、`a-stock-data`、`free-stockdb`、`QuantDinger`、`headroom` 等项目均集成或提及 MCP，显示 MCP 正在成为 Agent 与金融数据源之间的标准连接层。
3. **上下文工程成为 Agent 系统的核心关注点**：`headroom`（压缩）、`planning-with-files`（持久化规划）、`old-coder`（测试驱动）等项目从不同角度解决 Agent 的上下文管理和可靠性问题。

### 产品趋势

1. **从“交易机器人”转向“投研工作台”**：`daily_stock_analysis`、`Vibe-Research`、`ai-berkshire`、`tickflow-stock-panel` 等项目显示，产品重心正在从自动执行交易转向辅助研究和决策，人机协作模式更受青睐。
2. **A 股工具链快速补全**：`a-stock-data`、`free-stockdb`、`tickflow-stock-panel`、`Vibe-Research` 等项目集中出现，显示中文社区正在系统性地解决 A 股数据获取、存储、分析和可视化的完整链路。
3. **AI Agent 治理和审计产品化**：`iFixAi` 的出现表明，随着 Agent 在金融等高风险场景的部署，对 Agent 行为的审计、合规检查和安全评估正在成为独立的产品类别。

### 量化/交易策略趋势

1. **LLM 多 Agent 辩论式决策成为主流范式**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 等项目均采用多 Agent 分工/辩论架构，试图通过角色分工降低单一 LLM 的决策偏差。
2. **价值投资方法论的结构化编码**：`ai-berkshire` 将主观投资哲学转化为可执行的 Agent 工作流，显示量化与主观投资的边界正在模糊。
3. **研究工具与实盘交易的边界更加清晰**：多数项目明确标记为研究工具，显示社区对“LLM 直接驱动实盘交易”的风险有更清醒的认识。

### AI Agent 与自动化交易结合趋势

1. **Agent 从“生成信号”走向“全流程编排”**：从数据获取、分析、决策到推送，Agent 正在覆盖投研全流程，而非仅生成交易信号。
2. **本地 Agent 与云端模型混合部署**：`atomic-agent`、`unsloth` 等项目显示，敏感数据在本地处理、非敏感任务调用云端模型的混合架构正在形成。
3. **Agent 可靠性和可审计性成为落地前提**：`iFixAi`、`old-coder`、`planning-with-files` 等项目从审计、测试、状态管理三个维度解决 Agent 可靠性问题，这是 Agent 进入金融生产环境的必要条件。

### 值得后续做原型验证的方向

1. **基于 MCP 的 A 股数据接入层**：参考 `a-stock-data` 和 `free-stockdb`，构建标准化的 MCP 数据服务，统一行情、研报、公告等数据源。
2. **多 Agent 投研流水线**：参考 `TradingAgents` 和 `ai-berkshire`，构建“数据采集 → 多维度分析 → 对抗性审查 → 报告生成”的投研 Agent 流水线。
3. **本地优先的金融 LLM 推理**：参考 `unsloth` 和 `colibri`，验证在本地硬件上运行金融领域微调模型的可行性。
4. **Agent 行为审计层**：参考 `iFixAi`，为交易 Agent 构建行为合规性检查模块。

## 5. 今日灵感清单

1. **MVP：A 股投研日报 Agent**：参考 `daily_stock_analysis` 的流水线设计，构建一个基于 MCP 数据接入 + LLM 分析 + 定时推送的 A 股投研日报系统。核心功能：多源行情采集、新闻情绪分析、持仓监控、自动生成 Markdown 日报并推送。

2. **MVP：多 Agent 对抗性投研框架**：参考 `TradingAgents` 和 `ai-berkshire`，构建一个包含“基本面分析 Agent、技术分析 Agent、风险审查 Agent、汇总决策 Agent”的最小多 Agent 框架，重点验证对抗性审查对决策质量的影响。

3. **调研：MCP 在金融数据接入中的标准化程度**：对比 `Vibe-Trading`、`a-stock-data`、`free-stockdb`、`QuantDinger` 等项目的 MCP 实现方式，评估是否值得构建一个统一的金融数据 MCP 标准。

4. **调研：本地 LLM 推理在金融合规场景的可行性**：基于 `unsloth`、`colibri`、`ds4` 的技术路线，评估在消费级硬件上运行金融领域微调模型的性能、成本和合规收益。

5. **Codex/Agent 自动复现：LLM 上下文压缩代理**：参考 `headroom` 的实现思路，让 Codex 自动复现一个针对金融数据（行情 JSON、新闻流、研报文本）的上下文压缩代理，验证 token 节省率和信息保真度。

6. **Codex/Agent 自动复现：文件持久化规划机制**：参考 `planning-with-files`，让 Agent 自动实现一个基于 Markdown 文件的长时任务状态管理模块，用于交易 Agent 的定时监控任务。

7. **MVP：Agent 行为审计仪表盘**：参考 `iFixAi` 的审计思路，构建一个针对交易 Agent 的行为审计仪表盘，监控 Agent 的输入输出、决策依据、异常行为，并生成合规报告。

8. **调研：A 股数据源稳定性与合规性**：基于 `a-stock-data` 和 `free-stockdb` 的数据源列表，调研各数据源的稳定性、更新频率、合规风险，形成一份 A 股数据源评估报告。

9. **MVP：本地优先的 A 股量化工作台**：参考 `tickflow-stock-panel` 和 `free-stockdb`，构建一个自托管的 A 股选股 + 监控 + 回测工作台，重点验证 DuckDB/Polars 在本地量化数据处理的性能。

10. **Watchlist 候选**：将 `TradingAgents`、`Vibe-Trading`、`ai-berkshire`、`a-stock-data`、`free-stockdb`、`iFixAi`、`headroom`、`planning-with-files`、`old-coder`、`tickflow-stock-panel` 加入 watchlist，持续跟踪其架构演进和社区活跃度。

## 6. Watchlist 建议

| 项目 | 加入原因 | 关注重点 |
|---|---|---|
| TauricResearch/TradingAgents | 多 Agent 交易框架的代表作，star 接近 10 万 | 多 Agent 协作架构的演进，是否有实盘风控模块 |
| HKUDS/Vibe-Trading | 学术背景的 AI 交易 Agent，集成 MCP | MCP 在金融数据接入中的应用模式 |
| xbtlin/ai-berkshire | 投资方法论结构化的独特方向 | 多 Agent 对抗性分析的实现细节 |
| simonlin1212/a-stock-data | A 股数据工具包，43 端点、15 数据源 | 数据源稳定性、降级机制、维护活跃度 |
| hello245m/free-stockdb | 本地优先的 A 股量化引擎 | 增量同步、复权处理、回测准确性 |
| ifixai-ai/iFixAi | AI Agent 审计工具，切入治理痛点 | 审计规则库的覆盖度、金融场景适配性 |
| headroomlabs-ai/headroom | LLM 上下文压缩，金融数据场景价值高 | 压缩率与信息保真度的平衡 |
| OthmanAdi/planning-with-files | 长时 Agent 状态管理的轻量方案 | 并发一致性、分布式场景扩展性 |
| AmazingAng/old-coder | 早期高增长，Agent 测试方法论差异化 | 测试方法论在交易策略验证中的应用 |
| shy3130/tickflow-stock-panel | 自托管 A 股量化工作台，技术栈现代 | DuckDB/Polars 在量化数据处理的性能 |
| virattt/ai-hedge-fund | AI 对冲基金团队模拟，star 6.3 万 | 多 Agent 角色分工与决策流程 |
| OpenBB-finance/OpenBB | 面向 AI Agent 的开放金融数据平台 | 数据覆盖度、Agent 集成能力 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

**特别警示**：

- `ritmex-bot` 为 Perp DEX 永续合约交易机器人，杠杆交易存在爆仓风险，且该项目 star 基数极低（542），24h 涨星（+84）超过 7d 涨星（+83），属于典型短期脉冲，不建议投入真实资金。
- `Financial_freedom` 项目名称和描述带有明显营销色彩（“最全赚钱投资指南”），star 基数低但 24h 涨星异常偏高（+195），需警惕过度营销或刷星行为。
- `freqtrade` 是成熟的加密交易机器人，但加密交易本身具有高波动性和合规风险，任何自动化交易策略都应经过充分的模拟盘验证。
- 多个候选项目因关键词误匹配进入列表（如 `public-apis`、`build-your-own-x`、`awesome-selfhosted`、`awesome-go` 等），这些并非金融/量化项目，不应作为交易工具参考。

## 8. 数据质量说明

- **1 日基线**：已提供，`baseline_1d` 为 `2026-08-14.json`，当前快照为 `2026-08-15.json`，1 日涨星数据完整。
- **7 日基线**：已提供，`baseline_7d` 为 `2026-08-08.json`，7 日涨星数据基本完整。
- **30 日基线**：未提供，所有项目的 `star_delta_30d` 均为 `null`，无法评估 30 日趋势。
- **采集失败/缺失**：`needle` 项目的 `star_delta_7d` 为 `null`，7 日涨星数据缺失，可能因项目创建时间晚于 7 日基线或采集失败。
- **样本偏差**：候选集通过关键词匹配生成，存在明显的误匹配问题。48 个项目中，约 15-20 个为通用资源列表（awesome-* 系列）、编程教程或非金融项目，真正与金融/量化/交易直接相关的项目约 25-30 个。分析时应剔除噪声项目。
- **分类偏差**：`category_guess` 字段为自动推断，部分项目的分类可能不准确。例如 `unsloth` 被标记为 `ai_trading` 和 `quant_research`，但其实际是 LLM 训练/推理工具，与交易无直接关系。
- **风险标记偏差**：`risk_flags` 中的 `crypto_related`、`trading_bot` 等标记基于关键词匹配，可能将非交易项目误标记为交易相关（如 `build-your-own-x` 被标记为 `trading_bot`），也可能遗漏实际风险。
