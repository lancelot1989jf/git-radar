# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-16

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的股票分析与交易 Agent 技能包**：以 `daily_stock_analysis`、`claude-trading-skills`、`day-trader-skill` 为代表，正在把“行情分析 + 新闻解读 + 决策看板 + 自动推送”打包成可复用的 Claude/Codex skill。
  2. **AI Agent 治理与审计**：`iFixAi` 提出对 AI Agent 行为进行独立审计，覆盖幻觉检测、prompt injection、ISO 42001、NIST AI RMF 等，对金融场景中的 Agent 合规性有直接借鉴意义。
  3. **本地优先 / 自托管 AI 基础设施**：`colibri` 的 MoE 分层推理引擎、`OpenBot` 的自托管 Agent 框架、`headroom` 的 token 压缩，反映出金融场景对数据隐私、推理成本和本地部署的强需求。

- **是否出现新趋势**：  
  出现。一个明显趋势是“**交易能力被封装为 AI Agent Skill**”，而不是传统的一体化交易平台。多个高增长项目都以 Claude Code / Codex / Gemini CLI 的 skill 形式交付，强调“先研究、后回测、再决策”，而非直接下单。

- **是否出现值得复刻/参考的工程架构**：  
  有。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“自托管 + DuckDB + Polars + FastAPI + React”组合，都适合作为轻量级量化研究工作台的参考。

- **是否有明显骗局、过度营销或高风险项目**：  
  本次候选集中混入大量与金融/量化无关的 awesome-list、UI 设计、安全工具项目，属于关键词误匹配，不是骗局，但会稀释信号。`Turnitout-Humanizer` 描述涉及绕过 Turnitin 等学术查重系统，与金融无关且存在学术诚信风险，不应纳入金融工程参考。未发现明确的金融骗局项目，但所有带 `trading_bot` 标记的项目都应默认视为高风险，不应直接运行。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 72933 | +323 | +3666 | Python | AI 交易/数据工程/量化研究 | LLM 驱动的多市场股票分析系统，含新闻、看板、自动推送 | 高：多源数据融合与零成本定时任务架构 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 150594 | +516 | +3092 | Python | 金融科技产品 | AI UI/UX 设计 skill，跨平台生成专业界面 | 中：金融产品前端快速原型 | 低 |
| 3 | tradermonty/claude-trading-skills | 6605 | +800 | +2881 | Python | 回测 | Claude Code 股票交易技能包：行情、图表、日历、筛选、策略开发 | 高：交易研究流程的 Agent 化封装 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 337838 | +337 | +2240 | 无 | 交易机器人 | 自托管网络服务与 Web 应用列表 | 中：自托管金融数据/监控组件选型 | 中 |
| 5 | elementalsouls/Claude-BugHunter | 7822 | +1060 | +2312 | Python | 金融科技产品 | Claude Code 漏洞挖掘与红队 skill 包 | 中：金融 API/交易系统安全测试思路 | 低 |
| 6 | JustVugg/colibri | 51630 | +192 | +2109 | C | 量化研究 | MoE 模型分层推理引擎：GPU/RAM/NVMe 分级加载 | 高：本地大模型推理成本优化 | 低 |
| 7 | public-apis/public-apis | 499692 | +304 | +1954 | Python | 加密交易/量化研究/风控 | 免费 API 集合列表 | 中：金融数据 API 选型 | 中 |
| 8 | CopilotKit/OpenBot | 12652 | +170 | +2054 | TypeScript | 金融科技产品/交易机器人 | 开源自托管 AI Bot 替代方案，支持任意 Agent/模型/工具 | 高：企业级 Agent 编排框架参考 | 中 |
| 9 | codecrafters-io/build-your-own-x | 563252 | +278 | +1821 | Markdown | 交易机器人 | 从零复刻技术的教程集合 | 中：自建交易系统/数据库/解释器教程 | 中 |
| 10 | vinta/awesome-python | 335329 | +256 | +1646 | Python | 量化研究 | Python 工具精选列表 | 中：量化 Python 技术栈选型 | 低 |
| 11 | Jakeschincariol/day-trader-skill | 8254 | +192 | +1785 | Python | 回测/风控 | 11 个 Claude 日内交易 skill：扫描图表、跟踪新闻、计时进出场 | 高：日内交易研究流程自动化 | 低 |
| 12 | ifixai-ai/iFixAi | 46186 | +226 | +1698 | Python | AI 交易/金融科技产品/风控 | AI Agent 独立审计工具，120 秒内回答 Agent 是否按预期工作 | 高：Agent 合规与行为审计 | 低 |
| 13 | VoltAgent/awesome-design-md | 127873 | +159 | +1490 | 无 | 加密交易/金融科技产品 | 品牌设计系统 DESIGN.md 文件集合 | 低：与金融核心无关 | 中 |
| 14 | avelino/awesome-go | 194358 | +208 | +1309 | Go | 回测/加密交易/风控/交易机器人 | Go 框架与库精选列表 | 中：Go 交易系统组件选型 | 中 |
| 15 | TauricResearch/TradingAgents | 122890 | +124 | +1165 | Python | AI 交易/回测/量化研究 | 多 Agent LLM 金融交易框架 | 高：多 Agent 投研决策架构 | 低 |
| 16 | nexu-io/open-design | 107999 | +188 | +1086 | TypeScript | 金融科技产品/交易基础设施 | 协作式 AI 设计 Agent 工作区 | 低：与金融核心无关 | 低 |
| 17 | awesome-dsh-plugin/awesome-dsh-plugin | 24950 | +121 | +837 | JavaScript | 交易基础设施 | DeepSeek Harness 插件精选列表 | 中：Agent 插件生态观察 | 低 |
| 18 | garrytan/gbrain | 33183 | +71 | +861 | TypeScript | 金融科技产品 | Garry 的 OpenClaw/Hermes Agent Brain | 中：Agent 记忆与决策架构 | 低 |
| 19 | headroomlabs-ai/headroom | 79869 | +98 | +596 | Python | AI 交易/风控 | 压缩工具输出、日志、RAG 块，降低 LLM token 消耗 | 高：金融 Agent 上下文成本优化 | 低 |
| 20 | kaankiziltug/logo-design-skill | 7119 | +97 | +675 | HTML | 金融科技产品 | AI Logo 设计 skill | 低：与金融核心无关 | 低 |
| 21 | TGrpg/awesome-telegram | 1752 | +135 | +719 | JavaScript | 量化研究/交易机器人 | Telegram 频道、群组、机器人导航合集 | 低：信号渠道观察，需警惕诱导 | 中 |
| 22 | hesreallyhim/awesome-claude-code | 58196 | +91 | +539 | Python | AI 交易/量化研究 | Claude Code 资源精选列表 | 中：Agent 工具链选型 | 低 |
| 23 | jaywcjlove/awesome-mac | 118711 | +82 | +538 | Swift | 交易基础设施 | macOS 软件精选列表 | 低：与金融核心无关 | 低 |
| 24 | ripienaar/free-for-dev | 143012 | +61 | +606 | HTML | 金融科技产品/量化研究 | SaaS/PaaS/IaaS 免费层列表 | 中：零成本金融数据/算力资源 | 低 |
| 25 | ashishpatel26/500-AI-Agents-Projects | 40039 | +99 | +485 | Python | 风控/交易机器人 | 500 个 AI Agent 用例集合 | 中：金融 Agent 用例灵感 | 中 |
| 26 | ruvnet/ruflo | 81907 | +69 | +521 | TypeScript | AI 交易/回测 | Agent harness：多玩家 swarm、自适应记忆、向量 RAG | 高：多 Agent 编排与记忆架构 | 低 |
| 27 | punkpeye/awesome-remote-mcp-servers | 3377 | +89 | +476 | 无 | AI 交易/加密交易/交易机器人 | 远程 MCP 服务器集合 | 中：金融数据 MCP 服务发现 | 中 |
| 28 | PurpleDoubleD/locally-uncensored | 4332 | +43 | +663 | TypeScript | AI 交易/量化研究 | 本地 AI 工作室：聊天、图像/视频生成、编码 Agent | 中：本地 AI 推理环境 | 低 |
| 29 | shy3130/tick-stock-panel | 7954 | +61 | +488 | Python | AI 交易/回测/量化研究 | 自托管 A 股量化工作台：策略+监控+回测，DuckDB+Polars | 高：轻量级自托管量化工作台 | 低 |
| 30 | HKUDS/Vibe-Trading | 38404 | +56 | +423 | Python | AI 交易/回测/金融科技产品 | “Vibe-Trading”个人交易 Agent | 高：LLM 交易 Agent 研究框架 | 低 |
| 31 | sickn33/agentic-awesome-skills | 49837 | +61 | +395 | Python | 回测 | 2955+ 可复用 AI Agent skills 集合 | 中：交易研究 skill 库 | 低 |
| 32 | Soniavasseur/Wallet-Risk-Scanner | 915 | +1 | +723 | Python | 加密交易/金融科技产品/风控 | 多链加密钱包风险扫描器，AML/KYT 评分 | 高：链上风控与 AML 筛查 | 中 |
| 33 | AhmadHassan-BTed/Turnitout-Humanizer | 12359 | +51 | +335 | HTML | 风控/交易机器人 | 学术查重规避工具 | 低：与金融无关，存在学术诚信风险 | 中 |
| 34 | aardappel/goose | 3641 | +76 | +262 | C++ | 交易基础设施 | Goose 编程语言 | 低：与金融核心无关 | 低 |
| 35 | punkpeye/awesome-mcp-servers | 97791 | +43 | +240 | 无 | 金融科技产品 | MCP 服务器集合 | 中：金融数据 MCP 生态 | 低 |
| 36 | GoogleChrome/modern-web-guidance | 21249 | +2746 | 无 | 无 | 风控 | 让编码 Agent 跟上最新 Web 最佳实践 | 低：与金融核心无关 | 低 |
| 37 | nidhinjs/prompt-master | 16078 | +42 | +302 | 无 | AI 交易/金融科技产品 | 为任意 AI 工具生成准确 prompt 的 Claude skill | 中：金融 Agent prompt 工程 | 低 |
| 38 | GoogleChrome/modern-web-guidance-src | 8174 | +684 | 无 | TypeScript | 风控 | modern-web-guidance 源码 | 低：与金融核心无关 | 低 |
| 39 | openbq-org/OpenBB | 75483 | +23 | +193 | Python | 加密交易/量化研究 | 面向分析师、量化与 AI Agent 的开放数据平台 | 高：金融数据平台架构 | 中 |
| 40 | awesomedata/awesome-public-datasets | 80177 | +18 | +172 | 无 | 加密交易 | 高质量开放数据集列表 | 中：金融数据集选型 | 中 |
| 41 | code-yeongyu/oh-my-openagent | 70959 | +24 | +147 | TypeScript | 量化研究 | 图形工程 Agent 工具 | 低：与金融核心无关 | 低 |
| 42 | rust-unofficial/awesome-rust | 60597 | +23 | +163 | Rust | AI 交易/回测/加密交易/量化研究 | Rust 代码与资源精选列表 | 中：低延迟交易系统技术选型 | 中 |
| 43 | fffaraz/awesome-cpp | 74470 | +20 | +124 | 无 | 量化研究/交易基础设施 | C/C++ 框架与库精选列表 | 中：低延迟交易系统技术选型 | 低 |
| 44 | bex-co/beancount-io | 653 | +157 | 无 | TypeScript | 金融科技产品 | 复式记账移动应用，React Native + Expo | 高：面向 AI Agent 的 plain-text accounting | 低 |
| 45 | virattt/ai-hedge-fund | 64717 | +15 | +114 | Python | 回测/风控 | AI 对冲基金团队模拟 | 高：多 Agent 投研决策模拟 | 低 |
| 46 | Developer-Y/cs-video-courses | 84872 | +11 | +89 | 无 | 量化研究/交易机器人 | 计算机科学视频课程列表 | 低：与金融核心无关 | 中 |
| 47 | josephmisiti/awesome-machine-learning | 74843 | +6 | +55 | Python | AI 交易 | 机器学习框架与库精选列表 | 中：金融 ML 技术选型 | 低 |
| 48 | vuejs/awesome-vue | 73472 | -1 | -7 | 无 | 量化研究 | Vue.js 资源精选列表 | 低：与金融核心无关 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：把多市场股票分析流程自动化，整合多源行情、实时新闻、决策看板和自动推送，并支持零成本定时运行。
- **为什么值得关注**：7 日涨星 +3666，是本次候选集中金融属性最强、涨星最快的项目之一。它把“数据采集 → 新闻解读 → 决策呈现 → 推送”串成一条完整链路。
- **技术栈/架构亮点**：Python + LLM；多源行情与新闻融合；决策看板；定时任务。架构上强调“零成本运行”，说明对免费数据源和轻量调度有工程化处理。
- **是否适合借鉴**：非常适合。可以借鉴其“多源数据融合 + LLM 解读 + 看板 + 推送”的流水线，改造成企业内部的研究助手或投研日报生成器。
- **可能风险**：数据源合规性、新闻版权、LLM 输出幻觉、A 股数据准确性；自动推送可能放大错误信号。

### 3.2 tradermonty/claude-trading-skills
- **解决什么问题**：把股票投资者的市场分析、技术图表、经济日历、筛选器和策略开发封装成 Claude Code skills。
- **为什么值得关注**：24h +800、7d +2881，增速极快。代表“交易研究能力产品化”的新形态。
- **技术栈/架构亮点**：以 skill 为粒度组织能力，强调可组合、可复用；Python 实现；面向 Claude Code 生态。
- **是否适合借鉴**：适合。可以把内部投研流程拆成多个 skill，让 Codex/Claude 按需调用，形成可审计的研究工作流。
- **可能风险**：研究工具属性明显，策略开发容易过拟合；skill 质量参差不齐；依赖 Claude 生态。

### 3.3 TauricResearch/TradingAgents
- **解决什么问题**：用多 Agent LLM 框架模拟金融交易决策，覆盖分析、研究、交易等角色。
- **为什么值得关注**：star 基数高（122890），持续活跃，是“多 Agent 金融决策”方向的代表性项目。
- **技术栈/架构亮点**：Python + LLM + 多 Agent 编排；Apache-2.0；topic 包含 multiagent、finance、trading。
- **是否适合借鉴**：适合。可借鉴其多角色 Agent 分工，用于企业级投研 Agent 框架设计。
- **可能风险**：研究工具属性，回测结果可能过拟合；多 Agent 决策链路复杂，难审计；不应直接用于实盘。

### 3.4 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，把 LLM 与交易流程结合。
- **为什么值得关注**：来自 HKUDS，具备学术背景；topic 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent。
- **技术栈/架构亮点**：Python + LLM + MCP + 多 Agent；强调 backtesting 与 fintech。
- **是否适合借鉴**：适合作为“LLM 交易 Agent”的学术参考实现，尤其是 MCP 工具接入和回测闭环。
- **可能风险**：研究工具属性；策略过拟合；不应直接用于实盘。

### 3.5 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，覆盖幻觉检测、prompt injection、ISO 42001、NIST AI RMF 等。
- **为什么值得关注**：金融场景中 Agent 合规性越来越重要，该项目把审计流程压缩到 120 秒内，工程化程度高。
- **技术栈/架构亮点**：Python + Apache-2.0；topic 覆盖 agent-evaluation、ai-governance、ai-safety、llm-security、risk-management。
- **是否适合借鉴**：非常适合。可借鉴其审计维度，为金融 Agent 建立行为审计、合规检查和风险评估层。
- **可能风险**：审计结果依赖评估集质量；不能替代正式合规审查。

### 3.6 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股量化工作台，支持自建策略、监控、回测，LLM 驱动策略定制与个股分析。
- **为什么值得关注**：技术栈现代且轻量：DuckDB + Polars + FastAPI + React；强调自托管和第三方数据源接入。
- **技术栈/架构亮点**：DuckDB 做本地分析、Polars 做数据处理、FastAPI 做服务、React 做前端，是典型的轻量级量化工作台架构。
- **是否适合借鉴**：非常适合。可作为“本地优先量化研究工作台”的 MVP 参考，尤其适合不想依赖重型数据库的小团队。
- **可能风险**：A 股数据源稳定性；策略过拟合；个人开源项目维护活跃度需观察。

### 3.7 virattt/ai-hedge-fund
- **解决什么问题**：模拟一个 AI 对冲基金团队，用多个 Agent 扮演不同投研角色。
- **为什么值得关注**：star 基数高（64717），是“AI 对冲基金”概念的经典参考实现。
- **技术栈/架构亮点**：Python + 多 Agent 角色分工；MIT 许可。
- **是否适合借鉴**：适合作为多 Agent 投研决策的教学和原型参考。
- **可能风险**：研究工具属性；回测幸存者偏差；不应直接用于实盘。

### 3.8 headroomlabs-ai/headroom
- **解决什么问题**：在内容到达 LLM 前压缩工具输出、日志、文件和 RAG 块，降低 token 消耗。
- **为什么值得关注**：金融 Agent 通常要处理大量行情、新闻、日志数据，token 成本是瓶颈。该项目声称 JSON 可减少 60-95% token。
- **技术栈/架构亮点**：Python + Apache-2.0；提供 library、proxy、MCP server 三种形态；topic 覆盖 context-engineering、token-optimization、rag。
- **是否适合借鉴**：非常适合。可将其作为金融 Agent 的上下文工程层，降低长上下文成本。
- **可能风险**：压缩可能丢失关键信息；需验证对金融数值数据的保真度。

### 3.9 Soniavasseur/Wallet-Risk-Scanner
- **解决什么问题**：多链加密钱包风险扫描，AML/KYT 筛查，0-100 评分，集成 6 个情报提供商，支持 15+ 链。
- **为什么值得关注**：7d +723，虽然绝对 star 低，但方向明确：链上风控、欺诈检测、制裁筛查。
- **技术栈/架构亮点**：Python + 多情报源 failover；支持批量筛查和多种报告格式。
- **是否适合借鉴**：适合。可借鉴其多源情报聚合和风险评分模型，用于加密交易风控或合规筛查。
- **可能风险**：加密相关；情报源质量与覆盖率；合规要求因地区而异。

### 3.10 bex-co/beancount-io
- **解决什么问题**：面向人类和 AI Agent 的复式记账，plain-text accounting，React Native + Expo 移动端。
- **为什么值得关注**：24h +157，虽然 star 基数小，但“AI Agent 可读的 plain-text accounting”方向与金融 Agent 自动化记账高度相关。
- **技术栈/架构亮点**：TypeScript + React Native + Expo + GraphQL；基于 beancount/ledger 生态。
- **是否适合借鉴**：适合。可借鉴其“人类与 AI Agent 共用一套 plain-text 账本”的思路，构建可审计的自动化记账系统。
- **可能风险**：项目较新，生态和社区小；移动端记账的合规与数据安全需注意。

## 4. 趋势归纳

- **技术趋势**：
  - **交易研究能力 skill 化**：多个高增长项目把行情分析、图表、筛选、回测封装成 Claude/Codex skill，强调可组合、可复用。
  - **本地优先与自托管**：`colibri`、`tick-stock-panel`、`locally-uncensored`、`OpenBot` 都强调本地部署、隐私和成本控制。
  - **上下文工程**：`headroom` 等 token 压缩工具进入金融 Agent 视野，说明长上下文成本正在成为工程瓶颈。
  - **轻量数据栈**：DuckDB + Polars + FastAPI 组合在量化工作台中出现，替代重型数据库。

- **产品趋势**：
  - 从“一体化交易平台”转向“研究助手 + 决策看板 + 自动推送”的轻量产品形态。
  - AI Agent 审计与治理工具开始独立成产品，金融场景合规需求驱动。

- **量化/交易策略趋势**：
  - 多 Agent LLM 投研框架仍是主流研究方向，但多数项目定位为研究工具，而非实盘系统。
  - 回测仍是核心能力，但需警惕过拟合和幸存者偏差。

- **AI Agent 与自动化交易结合趋势**：
  - 结合点集中在“研究、分析、回测、监控、推送”，而非“自动下单”。
  - MCP 成为金融数据接入和工具编排的通用接口。
  - Agent 行为审计、幻觉检测、prompt injection 防护开始被纳入金融 Agent 设计。

- **值得后续做原型验证的方向**：
  - 本地优先的量化研究工作台（DuckDB + Polars + FastAPI + React）。
  - 金融 Agent 的上下文压缩与 token 成本优化。
  - 多 Agent 投研决策的审计与合规层。
  - 链上钱包风险评分与 AML 筛查。

## 5. 今日灵感清单

1. **MVP：本地量化研究工作台**  
   参考 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭一个自托管的研究看板，支持本地 CSV/Parquet 行情数据、策略回测和 LLM 解读。

2. **MVP：投研日报 Agent**  
   参考 `daily_stock_analysis`，做一个“多源新闻 + 行情 + LLM 摘要 + 定时推送”的投研日报生成器，先跑通数据采集和推送链路。

3. **调研：交易研究 skill 的封装方式**  
   对比 `claude-trading-skills`、`day-trader-skill`、`agentic-awesome-skills`，总结如何把投研流程拆成可复用 skill，并评估在 Codex/Claude 中的可移植性。

4. **调研：金融 Agent 的上下文压缩**  
   验证 `headroom` 在金融 JSON、日志、RAG 块上的压缩率和信息保真度，评估是否能降低长上下文成本。

5. **原型：Agent 行为审计层**  
   参考 `iFixAi`，为内部金融 Agent 建立幻觉检测、prompt injection 防护和行为审计的最小可行层。

6. **原型：链上钱包风险评分**  
   参考 `Wallet-Risk-Scanner`，用公开链上数据做一个简化版地址风险评分 demo，聚焦欺诈、混币器和制裁地址筛查。

7. **调研：MCP 金融数据生态**  
   浏览 `awesome-mcp-servers` 和 `awesome-remote-mcp-servers`，筛选可用的行情、新闻、链上数据 MCP server，评估接入成本。

8. **调研：多 Agent 投研决策框架**  
   对比 `TradingAgents`、`Vibe-Trading`、`ai-hedge-fund`，总结多角色 Agent 分工、回测闭环和 MCP 工具接入的异同。

9. **MVP：AI Agent 可读的 plain-text 记账**  
   参考 `beancount-io`，做一个最小可用的 plain-text accounting 接口，让 Agent 能生成和读取 beancount/ledger 格式账本。

10. **Watchlist：低延迟交易系统技术选型**  
    关注 `awesome-rust`、`awesome-cpp`、`awesome-go` 中与 order book、回测、低延迟相关的库，为后续交易基础设施选型做准备。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 金融属性强、涨星快，多源数据融合与自动推送架构值得持续跟踪 |
| tradermonty/claude-trading-skills | 交易研究 skill 化的代表，增速极快，适合观察 skill 生态演进 |
| TauricResearch/TradingAgents | 多 Agent 金融交易框架的长期参考项目 |
| HKUDS/Vibe-Trading | 学术背景的 LLM 交易 Agent，适合跟踪研究进展 |
| ifixai-ai/iFixAi | Agent 审计与治理方向，金融合规价值高 |
| shy3130/tick-stock-panel | 轻量级自托管量化工作台，技术栈现代，适合复刻 |
| headroomlabs-ai/headroom | 金融 Agent 上下文成本优化的关键工具 |
| Soniavasseur/Wallet-Risk-Scanner | 链上风控与 AML 筛查方向，值得观察其模型和情报源 |
| bex-co/beancount-io | AI Agent 可读的 plain-text accounting，方向新颖 |
| virattt/ai-hedge-fund | AI 对冲基金模拟的经典参考，适合教学和原型验证 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-11-15.json`，大部分项目具备 24h 涨星数据。
- **7 日基线**：已提供 `baseline_7d: 2026-11-09.json`，但部分项目（如 `modern-web-guidance`、`modern-web-guidance-src`、`beancount-io`）的 `star_delta_7d` 为 null，说明这些项目在 7 日基线中缺失或无法匹配，7 日涨星数据不完整。
- **30 日基线**：所有项目的 `star_delta_30d` 均为 null，本次报告无法提供 30 日涨星趋势。
- **样本偏差**：候选集中混入大量与金融/量化无关的 awesome-list、UI 设计、安全工具、编程语言项目，属于关键词误匹配（如 `fintech in:name,description,readme`、`"trading bot" in:name,description,readme` 等宽泛查询），会稀释金融信号。分析时已尽量过滤，但 Top 表中仍保留了这些项目以反映原始候选集情况。
- **采集失败**：未发现明确的采集失败标记，但部分项目 `star_delta_7d` 缺失，可能与基线匹配失败有关。
- **风险标记**：部分项目带 `trading_bot`、`crypto_related` 等风险标记，已在表中标注；这些标记来自候选集生成逻辑，仅作为风险提示，不代表项目本身一定存在安全问题。
