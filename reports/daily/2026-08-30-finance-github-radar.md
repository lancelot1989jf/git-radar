# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-30

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 多智能体金融交易框架**：以 `TauricResearch/TradingAgents` 为代表，7 日涨星 +2400，总 star 突破 10 万，说明“多 Agent 协作完成投研/交易决策”正在成为量化开源社区的主流叙事。
  2. **A 股 AI Agent 数据与研究工作台**：`daily_stock_analysis`、`tick-stock-panel`、`HiThink-Tech/Financial-API`、`a-stock-data` 等项目集中出现，围绕 A 股行情、财务数据、MCP 接口、LLM 决策看板形成完整工具链。
  3. **AI Agent 治理、审计与上下文工程**：`iFixAi`（AI Agent 独立审计）、`headroom`（token 压缩）、`planning-with-files`（文件化规划）等项目涨星明显，反映市场对“Agent 可信、可控、可审计”的工程需求快速上升。

- **是否出现新趋势**：出现。候选项目中大量出现“AI skill / Claude Code / Codex / MCP / agent harness”类项目，且与金融数据、投研、交易决策结合。传统“交易 bot”项目占比下降，取而代之的是“研究型 Agent + 数据接口 + 审计/治理”的组合。

- **是否出现值得复刻/参考的工程架构**：是。`TradingAgents` 的多 Agent 投研流水线、`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送”架构、`nautilus_trader` 的 Rust 事件驱动交易引擎、`iFixAi` 的 Agent 审计框架，均具备较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选项目中未发现明显骗局，但存在大量“awesome-list / 资源聚合”类项目因关键词误匹配进入榜单，实际与金融交易无关。另有部分项目描述带有明显营销化措辞（如 “undisputed champion”“tokenmaxxers”），需降低信息权重。`Vibe-Trading`、`QuantDinger` 等 crypto 相关项目风险等级为中，需注意策略过拟合与 API key 安全问题。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 473404 | +510 | +4152 | Python | API 资源列表 | 免费 API 聚合列表 | 低，通用资源 | 中 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 123280 | +269 | +3022 | Python | AI UI 设计技能 | 面向多平台的 UI/UX 设计智能技能 | 中，Agent UI 生成 | 低 |
| 3 | TauricResearch/TradingAgents | 101911 | +164 | +2400 | Python | AI 交易/多 Agent | 多智能体 LLM 金融交易框架 | 高，多 Agent 投研架构 | 低 |
| 4 | nexu-io/open-design | 92902 | +231 | +2137 | 信息不足 | AI 设计工具 | 本地优先的 AI 设计引擎 | 中，Agent 设计工作流 | 低 |
| 5 | VoltAgent/awesome-design-md | 111790 | +499 | +1907 | 信息不足 | 设计系统资源 | DESIGN.md 设计系统集合 | 中，Agent UI 一致性 | 中 |
| 6 | awesome-dsh-plugin/awesome-dsh-plugin | 13762 | +188 | +1863 | Python | 插件资源列表 | DeepSeek Harness 插件精选 | 低，插件生态观察 | 低 |
| 7 | codecrafters-io/build-your-own-x | 544147 | +205 | +1770 | Markdown | 教程资源 | 从零复刻技术的教程集合 | 中，交易系统复刻练习 | 中 |
| 8 | awesome-selfhosted/awesome-selfhosted | 316248 | +208 | +1686 | 信息不足 | 自托管资源 | 自托管网络服务列表 | 低，交易系统部署参考 | 中 |
| 9 | vinta/awesome-python | 317238 | +182 | +1529 | Python | Python 资源 | Python 工具精选列表 | 低，量化 Python 生态 | 低 |
| 10 | ripienaar/free-for-dev | 136017 | +109 | +1544 | HTML | 免费资源 | 开发者免费 SaaS/PaaS 列表 | 低，数据源成本优化 | 低 |
| 11 | CopilotKit/OpenBot | 3564 | +107 | +1053 | TypeScript | AI Agent/浏览器自动化 | 开源 AI 协作者，自带浏览器/文件/工具 | 高，Agent 治理与操作留痕 | 中 |
| 12 | cactus-compute/needle | 9803 | +113 | +1046 | Python | 端侧模型 | 14MB 端侧基础模型 | 中，端侧推理 | 中 |
| 13 | headroomlabs-ai/headroom | 68129 | +98 | +831 | Python | 上下文压缩 | 压缩工具输出/日志/RAG 块以省 token | 高，Agent 上下文工程 | 低 |
| 14 | ruvnet/ruflo | 69883 | +133 | +782 | TypeScript | Agent 编排 | Agent 元 harness，多智能体 swarm | 中，Agent 编排框架 | 低 |
| 15 | punkpeye/awesome-mcp-servers | 93458 | +386 | +735 | 信息不足 | MCP 资源 | MCP server 集合 | 中，金融数据 MCP 生态 | 低 |
| 16 | unslothai/unsloth | 75296 | +96 | +765 | Python | LLM 微调 | 本地 LLM 训练/微调 UI | 中，本地模型微调 | 低 |
| 17 | avelino/awesome-go | 182748 | +90 | +687 | Go | Go 资源 | Go 框架/库精选 | 低，Go 交易系统生态 | 中 |
| 18 | ifixai-ai/iFixAi | 11863 | +431 | +608 | Python | AI Agent 审计 | AI Agent 独立审计与合规评估 | 高，Agent 风控/审计 | 低 |
| 19 | ZhuLinsen/daily_stock_analysis | 64346 | +64 | +626 | Python | A 股 AI 分析 | LLM 驱动多市场股票分析系统 | 高，投研 Agent 产品化 | 低 |
| 20 | HKUDS/Vibe-Trading | 32137 | +63 | +569 | Python | AI 交易/回测 | 个人交易 Agent | 中，LLM 交易决策 | 中 |
| 21 | JustVugg/colibri | 26492 | +57 | +514 | C | 端侧推理 | 纯 C 零依赖 MoE 推理引擎 | 中，端侧推理 | 低 |
| 22 | vnpy/vnpy | 44992 | +99 | +280 | Python | 量化交易平台 | Python 开源量化交易平台框架 | 高，事件驱动交易架构 | 低 |
| 23 | nidhinjs/prompt-master | 12085 | +75 | +426 | 信息不足 | Prompt 工程 | 生成精准 prompt 的 Claude skill | 中，Prompt 优化 | 低 |
| 24 | HiThink-Tech/Financial-API | 2040 | +45 | +604 | TypeScript | A 股数据服务 | 同花顺官方 A 股金融数据 API/MCP/CLI | 高，金融数据基础设施 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 53257 | +51 | +373 | Python | Claude Code 资源 | Claude Code 资源精选 | 低，Agent 生态观察 | 低 |
| 26 | nautechsystems/nautilus_trader | 28167 | +54 | +638 | Rust | 交易引擎 | Rust 原生事件驱动交易引擎 | 高，低延迟交易架构 | 中 |
| 27 | shy3130/tick-stock-panel | 4001 | +36 | +457 | Python | A 股量化工作台 | 自托管 A 股选股/监控/回测工作台 | 高，自托管量化工作台 | 低 |
| 28 | garrytan/gbrain | 29332 | +36 | +343 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中，Agent 框架 | 低 |
| 29 | bbfamily/abu | 18491 | +212 | +280 | Python | 量化交易系统 | 阿布量化交易系统 | 中，机器学习量化 | 低 |
| 30 | OpenBB-finance/OpenBB | 72519 | +54 | +303 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高，金融数据中台 | 中 |
| 31 | Developer-Y/cs-video-courses | 83310 | +60 | +150 | 信息不足 | 课程资源 | 计算机科学视频课程列表 | 低，学习资源 | 中 |
| 32 | perixtar/Tech-OA-Interview-Questions | 4729 | +27 | +482 | Python | 面试题库 | 科技公司 OA/面试题 | 低，无关金融 | 低 |
| 33 | OthmanAdi/planning-with-files | 26475 | +59 | +159 | Shell | Agent 规划 | 基于文件的 AI Agent 持久化规划 | 高，长时任务可靠性 | 低 |
| 34 | RyanCodrai/turbovec | 16556 | +32 | +275 | Rust | 向量索引 | 基于 TurboQuant 的向量索引 | 中，量化向量检索 | 低 |
| 35 | MakazhanAlpamys/Soup | 4012 | +373 | 信息不足 | Python | LLM 微调 | 单 YAML 微调 LLM，低显存训练 | 中，本地模型微调 | 低 |
| 36 | simonlin1212/a-stock-data | 9382 | +41 | +236 | 信息不足 | A 股数据工具包 | A 股全栈数据工具包，零鉴权 | 高，金融数据聚合 | 低 |
| 37 | xbtlin/ai-berkshire | 16019 | +32 | +231 | Python | 价值投资研究 | 多 Agent 价值投资研究框架 | 高，投研 Agent 方法论 | 低 |
| 38 | code-yeongyu/oh-my-openagent | 68532 | +18 | +232 | TypeScript | Agent harness | 复杂代码库的 Agent harness | 中，Agent 编排 | 低 |
| 39 | elementalsouls/Claude-BugHunter | 3900 | +60 | +144 | Python | 安全审计 | Claude Code 漏洞挖掘技能包 | 中，交易系统安全测试 | 低 |
| 40 | OpenByteInc/QuantDinger | 11250 | +33 | +238 | Python | AI 量化交易平台 | 加密/股票/外汇 AI 量化平台 | 中，多资产 AI 交易 | 中 |
| 41 | questflowai/investorskills | 1698 | +53 | +240 | Swift | 投资技能库 | 将投资判断结构化为可移植格式 | 高，投研知识结构化 | 低 |
| 42 | fffaraz/awesome-cpp | 73047 | +38 | +148 | 信息不足 | C++ 资源 | C++ 框架/库精选 | 低，低延迟系统生态 | 低 |
| 43 | antirez/ds4 | 21932 | +13 | +246 | C | 本地推理引擎 | DeepSeek 4 本地推理引擎 | 中，本地推理 | 低 |
| 44 | rust-unofficial/awesome-rust | 59071 | +18 | +121 | Rust | Rust 资源 | Rust 代码/资源精选 | 低，Rust 交易系统生态 | 低 |
| 45 | josephmisiti/awesome-machine-learning | 74223 | +10 | +92 | Python | ML 资源 | 机器学习框架/库精选 | 低，ML 生态 | 低 |
| 46 | awesomedata/awesome-public-datasets | 78735 | +26 | 信息不足 | 信息不足 | 数据集资源 | 高质量开放数据集列表 | 中，金融数据集 | 中 |
| 47 | virattt/ai-hedge-fund | 63102 | +14 | +93 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高，多 Agent 投研 | 低 |
| 48 | vuejs/awesome-vue | 73549 | 0 | +12 | 信息不足 | Vue 资源 | Vue.js 资源精选 | 低，无关金融 | 低 |
| 49 | fmzquant/strategies | 5495 | +105 | +113 | 信息不足 | 策略库 | 多语言量化交易策略 | 中，策略参考 | 中 |
| 50 | ByteByteGoHq/system-design-101 | 87740 | +19 | +273 | 信息不足 | 系统设计 | 系统设计图解 | 中，交易系统架构 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将金融交易决策拆分为多个 LLM Agent 协作完成，覆盖研究、分析、交易决策等环节，降低单模型决策偏差。
- **为什么值得关注**：7 日涨星 +2400，总 star 超 10 万，是当前“LLM 多智能体交易”方向最具代表性的开源项目之一。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 编排；topic 包含 agent、finance、llm、multiagent、trading。架构上强调角色分工与协作流水线。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色划分、投研流水线编排、决策留痕等设计，用于企业级投研 Agent 或自动化交易研究框架。
- **可能风险**：作为研究工具，策略表现未经实盘验证；LLM 输出存在幻觉风险；金融合规边界不清晰；需避免直接接入真实交易。

### 3.2 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股/多市场的 LLM 驱动股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：总 star 64346，7 日涨星 +626，是 A 股 AI 投研产品化程度较高的项目。
- **技术栈/架构亮点**：Python + MIT；topic 包含 a-stock、ai-agent、llm、quant、quantitative-finance。架构覆盖数据接入、新闻处理、LLM 分析、看板展示、自动推送全链路。
- **是否适合借鉴**：非常适合。其“数据 + 新闻 + LLM + 看板 + 推送”的产品形态可直接复刻为内部投研助手或客户报告生成系统。
- **可能风险**：依赖第三方数据源稳定性；LLM 生成的“决策”不可作为投资依据；定时任务需注意数据延迟与合规。

### 3.3 nautechsystems/nautilus_trader
- **解决什么问题**：提供生产级 Rust 原生交易引擎，采用确定性事件驱动架构，面向加密、股票、外汇、期货、期权等多资产。
- **为什么值得关注**：Rust 语言、事件驱动、生产级定位，在量化交易基础设施中具有较高工程参考价值。
- **技术栈/架构亮点**：Rust + LGPL-3.0；topic 包含 algorithmic-trading-engine、crypto-trading、equity-trading、forex、futures-trading、options-trading。强调确定性事件驱动，适合回测与实盘一致性。
- **是否适合借鉴**：适合。可借鉴其事件驱动内核、回测/实盘统一架构、多资产适配层设计，用于自建低延迟交易系统。
- **可能风险**：LGPL 许可证需注意合规；涉及杠杆/网格相关标记，实盘风险高；Rust 学习曲线陡峭。

### 3.4 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，支持人工或 Agent 自审计，120 秒内给出结论。
- **为什么值得关注**：24 小时涨星 +431，是本次候选项目中单日涨星最高的项目之一，反映 AI Agent 治理/审计需求爆发。
- **技术栈/架构亮点**：Python + Apache-2.0；topic 覆盖 agent-evaluation、ai-governance、ai-safety、eu-ai-act、iso-42001、nist-ai-rmf、owasp-llm、prompt-injection、risk-management。将合规框架与 Agent 评估结合。
- **是否适合借鉴**：非常适合。金融交易 Agent 尤其需要审计与合规，可将其评估思路引入交易 Agent 上线前的安全检查。
- **可能风险**：审计结论依赖评估标准设计；不能替代正式合规审查；需防止审计工具本身被 prompt injection 绕过。

### 3.5 HiThink-Tech/Financial-API
- **解决什么问题**：提供同花顺官方 A 股金融数据服务，覆盖实时行情、历史行情、财务报表、指数、板块、涨停等数据，支持 API、MCP、CLI、Python。
- **为什么值得关注**：官方背景 + MCP 接口 + AI Agent 定位，是金融数据基础设施与 Agent 生态结合的典型案例。
- **技术栈/架构亮点**：TypeScript + MIT；topic 包含 a-share、ai-agent、duckdb、financial-data、mcp、quantitative-finance、rest-api。MCP 支持使其可被 Claude Code/Codex 等 Agent 直接调用。
- **是否适合借鉴**：适合。可借鉴其“官方数据 + MCP 标准化接口 + 多端访问”的设计，构建内部金融数据服务。
- **可能风险**：数据覆盖范围与授权边界需确认；依赖官方服务稳定性；TypeScript 生态与量化 Python 生态的衔接成本。

### 3.6 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，支持 LLM 策略定制、个股分析、复盘，可接入第三方数据源。
- **为什么值得关注**：7 日涨星 +457，总 star 4001，是近期 A 股自托管量化工作台方向的新兴项目。
- **技术栈/架构亮点**：Python + MIT；topic 包含 a-stock、ai-agent、backtesting、duckdb、fastapi、llm、polars、react、self-hosted、screener。技术选型现代（DuckDB + Polars + FastAPI + React），强调自托管与个性化扩展。
- **是否适合借鉴**：适合。其“选股 + 监控 + 回测 + LLM 定制”一体化工作台形态，可作为内部量化研究平台的 MVP 参考。
- **可能风险**：个人开源项目，维护持续性存疑；回测结果可能存在幸存者偏差；自托管需注意数据源合规。

### 3.7 OpenBB-finance/OpenBB
- **解决什么问题**：面向分析师、量化研究员和 AI Agent 的开放数据平台，聚合多资产、多来源金融数据。
- **为什么值得关注**：总 star 72519，是金融数据平台方向成熟项目，近期仍保持增长。
- **技术栈/架构亮点**：Python；topic 覆盖 ai、crypto、derivatives、economics、equity、fixed-income、machine-learning、options、quantitative-finance。定位为数据中台，强调 AI Agent 友好。
- **是否适合借鉴**：适合。可借鉴其数据标准化、多资产覆盖、AI Agent 接口设计，构建企业级金融数据中台。
- **可能风险**：许可证为 Other，需注意商业使用限制；数据源授权与延迟需评估；crypto 相关数据需注意合规。

### 3.8 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，通过多 Agent 协作完成投研与交易决策。
- **为什么值得关注**：总 star 63102，是“AI 对冲基金”概念的开源代表项目。
- **技术栈/架构亮点**：Python + MIT；topic 信息不足。强调多角色 Agent 模拟对冲基金团队。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色模拟、投研流程设计，用于教学或内部研究原型。
- **可能风险**：研究工具属性强，策略未经实盘验证；回测可能过拟合；不可作为投资依据。

### 3.9 xbtlin/ai-berkshire
- **解决什么问题**：基于 Claude Code/Codex 的价值投资研究框架，整合巴菲特、芒格、段永平、李录四套方法论，支持多 Agent 对抗式分析。
- **为什么值得关注**：将价值投资方法论结构化为 Agent 可执行的研究流程，是“投研方法论产品化”的代表。
- **技术栈/架构亮点**：Python + MIT；topic 包含 ai-agent、claude-code、fundamental-analysis、mcp、portfolio-management、value-investing。强调多 Agent 并行与对抗分析。
- **是否适合借鉴**：适合。可借鉴其“方法论结构化 + 多 Agent 对抗”思路，构建内部投研知识库与 Agent 研究流程。
- **可能风险**：价值投资方法论本身存在主观性；LLM 分析可能产生偏差；需注意版权与数据合规。

### 3.10 CopilotKit/OpenBot
- **解决什么问题**：开源 AI 协作者，每个 Agent 拥有自己的浏览器、文件和工具，所有动作事前决策、事后记录，支持任意 AG-UI Agent。
- **为什么值得关注**：7 日涨星 +1053，总 star 3564，是“Agent 操作留痕与治理”方向的新兴项目。
- **技术栈/架构亮点**：TypeScript + MIT；topic 包含 ag-ui、agent-governance、ai-agents、browser-automation、generative-ui、mcp。强调动作可审计、可回放。
- **是否适合借鉴**：适合。交易 Agent 尤其需要操作留痕与审计，可借鉴其“事前决策 + 事后记录”的治理机制。
- **可能风险**：项目较新，生态与稳定性待验证；浏览器自动化在金融场景需注意安全边界。

## 4. 趋势归纳

- **技术趋势**：
  - **多智能体 LLM 框架成为金融交易研究主流**：TradingAgents、ai-hedge-fund、Vibe-Trading、ai-berkshire 等项目均采用多 Agent 协作架构。
  - **MCP 成为金融数据接入标准**：HiThink-Tech/Financial-API、a-stock-data、QuantDinger 等项目均提供 MCP 接口，使金融数据可被 Claude Code/Codex 等 Agent 直接调用。
  - **Rust 在低延迟交易基础设施中持续渗透**：nautilus_trader、turbovec 等项目采用 Rust，强调性能与确定性。
  - **上下文工程与 Agent 治理工具兴起**：headroom（token 压缩）、planning-with-files（文件化规划）、iFixAi（Agent 审计）反映 Agent 工程化需求。

- **产品趋势**：
  - **A 股 AI 投研工作台集中爆发**：daily_stock_analysis、tick-stock-panel、ai-berkshire 等项目将 LLM 分析、数据看板、自动推送产品化。
  - **自托管与零成本运行成为卖点**：多个项目强调 self-hosted、zero-auth、cost-free scheduled runs。
  - **“AI skill / 插件”生态快速扩张**：ui-ux-pro-max-skill、awesome-dsh-plugin、prompt-master 等项目反映 Agent 技能市场正在形成。

- **量化/交易策略趋势**：
  - **从单一策略转向多 Agent 投研流水线**：策略本身不再是核心，研究流程、数据整合、决策留痕成为重点。
  - **回测与实盘一致性受重视**：nautilus_trader 强调确定性事件驱动，体现对回测可信度的关注。
  - **价值投资与基本面分析被 LLM 结构化**：ai-berkshire、investorskills 将投资方法论转化为可执行 Agent 流程。

- **AI Agent 与自动化交易结合趋势**：
  - **Agent 审计与合规成为刚需**：iFixAi、OpenBot 等项目聚焦 Agent 治理，金融场景对可审计性要求更高。
  - **数据接入标准化**：MCP 成为金融数据与 Agent 之间的桥梁。
  - **本地/端侧推理降低数据外泄风险**：needle、colibri、ds4、unsloth 等项目反映本地推理需求，对金融数据隐私敏感场景有参考价值。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据服务 + 多 Agent 投研流水线。
  - 交易 Agent 操作留痕与审计系统。
  - 自托管 A 股量化工作台（选股 + 监控 + 回测 + LLM 定制）。
  - 本地 LLM 推理在金融数据分析中的应用。

## 5. 今日灵感清单

1. **MVP：A 股投研 Agent 工作台**：参考 `daily_stock_analysis` + `tick-stock-panel`，用 FastAPI + DuckDB + Polars + React 搭建自托管选股/监控/回测面板，接入 LLM 生成每日分析报告并自动推送。
2. **MVP：金融数据 MCP Server**：参考 `HiThink-Tech/Financial-API` 和 `a-stock-data`，将内部行情/财务数据封装为 MCP server，使 Claude Code/Codex 可直接调用，验证 Agent 驱动投研流程。
3. **调研：多 Agent 投研流水线编排**：深入阅读 `TradingAgents` 和 `ai-hedge-fund` 的 Agent 角色划分与消息传递设计，提炼可复用的投研流水线模板。
4. **调研：交易 Agent 审计与合规**：研究 `iFixAi` 的评估框架与 `OpenBot` 的操作留痕机制，设计交易 Agent 上线前的安全检查清单。
5. **Demo：Agent 上下文压缩**：用 `headroom` 的思路，对金融新闻、财报、行情日志等长文本做 token 压缩，验证在投研 Agent 中降低上下文成本的效果。
6. **Demo：文件化长时任务规划**：参考 `planning-with-files`，为量化研究 Agent 增加基于 Markdown 的持久化规划与断点恢复能力，提升长时回测/研究任务可靠性。
7. **原型：本地 LLM 金融数据分析**：基于 `unsloth` 或 `Soup` 微调小型模型，验证在本地对财报/公告做结构化抽取的可行性，降低数据外泄风险。
8. **Watchlist：Rust 交易引擎**：将 `nautilus_trader` 加入 watchlist，研究其事件驱动架构与回测/实盘一致性设计，为自建低延迟系统积累参考。
9. **调研：投资方法论结构化**：研究 `ai-berkshire` 和 `investorskills` 如何将价值投资方法论转化为 Agent 可执行流程，探索内部投研知识库建设。
10. **安全测试：交易系统红队技能**：参考 `Claude-BugHunter` 的技能包设计，为自建交易系统构建 AI 辅助的安全审计/漏洞挖掘流程。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多 Agent 金融交易框架代表，持续高增长，架构值得深入研究 |
| nautechsystems/nautilus_trader | Rust 事件驱动交易引擎，低延迟与回测一致性设计有长期参考价值 |
| ifixai-ai/iFixAi | AI Agent 审计/治理方向新兴项目，单日涨星高，金融 Agent 合规刚需 |
| HiThink-Tech/Financial-API | 官方 A 股数据 + MCP 接口，金融数据基础设施与 Agent 生态结合样本 |
| shy3130/tick-stock-panel | 自托管 A 股量化工作台，技术选型现代，产品形态完整 |
| CopilotKit/OpenBot | Agent 操作留痕与治理机制，适合交易 Agent 安全设计参考 |
| OpenBB-finance/OpenBB | 成熟金融数据平台，数据标准化与 AI Agent 接口设计值得跟踪 |
| xbtlin/ai-berkshire | 投资方法论结构化 + 多 Agent 对抗分析，投研知识库建设参考 |
| headroomlabs-ai/headroom | Agent 上下文压缩，降低投研 Agent token 成本的关键技术 |
| OthmanAdi/planning-with-files | 文件化长时任务规划，提升量化研究 Agent 可靠性的实用方案 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-08-29）和 `baseline_7d`（2026-08-23），1 日与 7 日涨星数据基本完整。
- **30 日基线缺失**：所有项目的 `star_delta_30d` 均为 null，无法评估 30 日涨星趋势。
- **7 日涨星缺失**：`MakazhanAlpamys/Soup` 和 `awesomedata/awesome-public-datasets` 的 `star_delta_7d` 为 null，可能因项目创建时间晚于 7 日基线或采集失败。
- **样本偏差**：候选项目通过关键词匹配筛选，大量“awesome-list / 资源聚合”类项目因描述或 README 中命中关键词而进入榜单，实际与金融交易无关，可能稀释真正金融项目的信号。部分项目 `language` 字段为 null，语言信息不足。
- **分类噪声**：`category_guess` 与 `risk_flags` 为自动推断结果，存在误分类可能，例如 `build-your-own-x`、`awesome-selfhosted` 被标记为 trading_bot，实际并非交易机器人。
