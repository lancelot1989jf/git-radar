# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-31

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 多智能体交易框架**：以 `TauricResearch/TradingAgents` 为代表，多 Agent 投研/交易框架持续高速涨星，说明“LLM 协作式投研”正在成为量化研究的主流实验方向。
  2. **AI Agent 治理与审计**：`ifixai-ai/iFixAi` 以“AI Agent 独立审计”切入，覆盖 AI 对齐、EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架，反映 Agent 进入生产环境前的治理需求快速上升。
  3. **本地化/自托管量化工作台**：`QuantMind`、`tick-stock-panel`、`daily_stock_analysis` 等项目强调 Docker 私有化部署、数据本地化、零成本定时运行，显示个人开发者和投研团队对“数据隐私 + 低门槛”的量化工具需求明显。

- **是否出现新趋势**：  
  出现。AI Agent 正在从“通用编码助手”向“金融投研/交易专用 Agent”分化，同时“Agent 审计/合规”作为配套基础设施开始独立成赛道。另一个明显趋势是“设计智能 + 编码 Agent”项目大量进入榜单，但多数与金融交易无直接关系，属于匹配噪声。

- **是否出现值得复刻/参考的工程架构**：  
  是。`TradingAgents` 的多 Agent 投研编排、`QuantMind` 的“因子挖掘 + 模型工场 + 回测 + 实盘模拟”闭环、`nautilus_trader` 的 Rust 原生确定性事件驱动交易引擎、`iFixAi` 的 Agent 审计框架，均具有较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：  
  本次候选集中未发现明显骗局项目，但存在大量“awesome-list”类高星项目因关键词误匹配进入榜单，实际与金融交易无关。`fmzquant/strategies` 等策略库包含 crypto、套利、做市等关键词，需注意策略过拟合和实盘风险。部分项目描述存在明显营销化措辞，如“零门槛无限制”“零成本定时运行”，应保持审慎。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 473894 | +490 | +3988 | Python | API 资源列表 | 免费 API 聚合列表 | 低，通用资源 | 中 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 123611 | +331 | +3012 | Python | AI 设计技能 | 多平台 UI/UX 设计智能技能 | 中，Agent 设计能力 | 低 |
| 3 | TauricResearch/TradingAgents | 102070 | +159 | +2333 | Python | AI 交易/多智能体 | 多 Agent LLM 金融交易框架 | 高，多 Agent 投研架构 | 低 |
| 4 | nexu-io/open-design | 93125 | +223 | +2008 | 信息不足 | AI 设计工具 | 本地优先的 AI 设计引擎 | 中，Agent 设计工作流 | 低 |
| 5 | VoltAgent/awesome-design-md | 112120 | +330 | +1955 | 信息不足 | 设计系统资源 | DESIGN.md 设计系统集合 | 中，Agent UI 生成 | 中 |
| 6 | codecrafters-io/build-your-own-x | 544393 | +246 | +1730 | Markdown | 编程教程 | 从零复刻技术的教程集合 | 中，工程学习 | 中 |
| 7 | awesome-selfhosted/awesome-selfhosted | 316416 | +168 | +1606 | 信息不足 | 自托管资源 | 自托管网络服务列表 | 中，自托管基础设施 | 中 |
| 8 | vinta/awesome-python | 317463 | +225 | +1578 | Python | Python 资源 | Python 工具精选列表 | 低，通用资源 | 低 |
| 9 | awesome-dsh-plugin/awesome-dsh-plugin | 13940 | +178 | +1645 | Python | 插件资源 | DeepSeek Harness 插件列表 | 中，Agent 插件生态 | 低 |
| 10 | ripienaar/free-for-dev | 136135 | +118 | +1055 | HTML | 免费资源 | SaaS/PaaS/IaaS 免费层列表 | 低，通用资源 | 低 |
| 11 | ifixai-ai/iFixAi | 12236 | +373 | +978 | Python | AI 审计/风控 | AI Agent 独立审计工具 | 高，Agent 治理/合规 | 低 |
| 12 | punkpeye/awesome-mcp-servers | 93615 | +157 | +861 | 信息不足 | MCP 资源 | MCP 服务器集合 | 中，Agent 工具生态 | 低 |
| 13 | cactus-compute/needle | 9909 | +106 | +934 | Python | 端侧模型 | 14MB 端侧基础模型 | 中，端侧 AI | 中 |
| 14 | headroomlabs-ai/headroom | 68233 | +104 | +803 | Python | Token 压缩 | LLM 输出/日志压缩工具 | 高，Agent 上下文工程 | 低 |
| 15 | ruvnet/ruflo | 70042 | +159 | +738 | TypeScript | Agent 编排 | Agent 元编排/多智能体群 | 高，Agent 编排框架 | 低 |
| 16 | unslothai/unsloth | 75385 | +89 | +759 | Python | LLM 微调 | 本地 LLM 训练/微调 UI | 中，本地模型微调 | 低 |
| 17 | CopilotKit/OpenBot | 3625 | +61 | +946 | TypeScript | AI 工作者 | 开源 AI 工作者/浏览器自动化 | 高，Agent 治理/自动化 | 中 |
| 18 | avelino/awesome-go | 182833 | +85 | +675 | Go | Go 资源 | Go 框架/库精选列表 | 低，通用资源 | 中 |
| 19 | qusong0627/QuantMind | 1252 | +219 | +702 | Python | 量化平台 | AI 原生多市场量化交易平台 | 高，量化闭环架构 | 低 |
| 20 | ZhuLinsen/daily_stock_analysis | 64412 | +66 | +629 | Python | AI 股票分析 | LLM 驱动多市场股票分析 | 高，LLM 投研自动化 | 低 |
| 21 | HKUDS/Vibe-Trading | 32195 | +58 | +549 | Python | AI 交易 | 个人交易 Agent | 高，AI 交易 Agent | 中 |
| 22 | JustVugg/colibri | 26557 | +65 | +466 | C | 端侧推理 | 纯 C 零依赖 MoE 推理引擎 | 中，端侧推理 | 低 |
| 23 | garrytan/gbrain | 29387 | +55 | +362 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中，Agent 框架 | 低 |
| 24 | nidhinjs/prompt-master | 12145 | +60 | +418 | 信息不足 | Prompt 工程 | 精准 Prompt 生成技能 | 中，Prompt 工程 | 低 |
| 25 | shiyu-coder/Kronos | 38238 | +100 | +371 | Python | 金融基础模型 | 金融市场语言基础模型 | 高，金融基础模型 | 低 |
| 26 | shy3130/tick-stock-panel | 4064 | +63 | +388 | Python | 量化工作台 | A 股选股+监控+回测工作台 | 高，自托管量化工作台 | 低 |
| 27 | HiThink-Tech/Financial-API | 2084 | +44 | +479 | TypeScript | 金融数据 API | 同花顺 A 股金融数据服务 | 高，金融数据基础设施 | 低 |
| 28 | xbtlin/ai-berkshire | 16080 | +61 | +239 | Python | 价值投资研究 | 多 Agent 价值投资研究框架 | 高，投研 Agent 方法论 | 低 |
| 29 | nautechsystems/nautilus_trader | 28230 | +63 | +524 | Rust | 交易引擎 | Rust 原生事件驱动交易引擎 | 高，交易系统架构 | 中 |
| 30 | code-yeongyu/oh-my-openagent | 68572 | +40 | +241 | TypeScript | Agent 编排 | 复杂代码库编码 Agent | 中，Agent 编排 | 低 |
| 31 | elementalsouls/Claude-BugHunter | 3970 | +70 | +204 | Python | 安全测试 | Claude 漏洞挖掘技能包 | 中，安全测试 | 低 |
| 32 | perixtar/Tech-OA-Interview-Questions | 4754 | +25 | +485 | Python | 面试题库 | 科技公司 OA/面试题 | 低，通用资源 | 低 |
| 33 | questflowai/investorskills | 1761 | +63 | +303 | Swift | 投资技能库 | 结构化投资判断技能库 | 高，投研知识结构化 | 低 |
| 34 | Developer-Y/cs-video-courses | 83356 | +46 | +184 | 信息不足 | 课程资源 | CS 视频课程列表 | 低，通用资源 | 中 |
| 35 | antirez/ds4 | 21966 | +34 | +252 | C | 本地推理 | DeepSeek 4 本地推理引擎 | 中，本地推理 | 低 |
| 36 | RyanCodrai/turbovec | 16600 | +44 | +247 | Rust | 向量索引 | 基于 TurboQuant 的向量索引 | 中，向量检索/量化 | 低 |
| 37 | OthmanAdi/planning-with-files | 26525 | +50 | +186 | Shell | Agent 规划 | 基于文件的 Agent 持久规划 | 高，Agent 长期任务 | 低 |
| 38 | anbeime/skill | 6009 | +42 | +283 | Python | 技能商店 | Skills 技能包商店 | 中，Agent 技能生态 | 低 |
| 39 | MakazhanAlpamys/Soup | 4233 | +221 | 信息不足 | Python | LLM 微调 | 单 YAML 微调 LLM | 中，低资源微调 | 低 |
| 40 | OpenBB-finance/OpenBB | 72544 | +25 | +298 | Python | 金融数据平台 | 分析师/量化/AI Agent 开放数据平台 | 高，金融数据基础设施 | 中 |
| 41 | fffaraz/awesome-cpp | 73060 | +13 | +141 | 信息不足 | C++ 资源 | C/C++ 框架库精选 | 低，通用资源 | 低 |
| 42 | rust-unofficial/awesome-rust | 59085 | +14 | +123 | Rust | Rust 资源 | Rust 代码/资源精选 | 低，通用资源 | 低 |
| 43 | josephmisiti/awesome-machine-learning | 74229 | +6 | +83 | Python | ML 资源 | ML 框架/库精选 | 低，通用资源 | 低 |
| 44 | virattt/ai-hedge-fund | 63115 | +13 | +88 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高，多 Agent 投研 | 低 |
| 45 | awesomedata/awesome-public-datasets | 78751 | +16 | 信息不足 | 信息不足 | 数据集资源 | 高质量开放数据集列表 | 中，数据资源 | 中 |
| 46 | IDouble/Market-Overview-Indexes-Forex-Metals-Crypto | 329 | +79 | +78 | HTML | 市场概览 | 联邦基金利率与市场概览 | 低，市场数据可视化 | 中 |
| 47 | fmzquant/strategies | 5612 | +117 | +229 | 信息不足 | 策略库 | 多语言量化交易策略库 | 中，策略参考 | 中 |
| 48 | vuejs/awesome-vue | 73550 | +1 | +14 | 信息不足 | Vue 资源 | Vue.js 精选资源 | 低，通用资源 | 低 |
| 49 | ByteByteGoHq/system-design-101 | 87767 | +27 | +260 | 信息不足 | 系统设计 | 系统设计图解 | 中，系统设计参考 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，把投研流程拆分为多个 Agent 角色，模拟团队式分析与决策。
- **为什么最近值得关注**：7 日涨星 +2333，总 star 已超 10 万，是当前“LLM 多智能体交易框架”方向中热度最高的项目之一，且近 30 天持续有 push。
- **技术栈/架构亮点**：Python + Apache-2.0；以 `agent`、`multiagent`、`llm`、`trading` 为核心主题，架构上强调多 Agent 分工与协作。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其多 Agent 编排思路可迁移到企业级投研 Agent、风控 Agent、研报生成等场景。
- **可能的风险**：作为研究工具，策略表现未经实盘验证；多 Agent 决策链路过长可能引入一致性与延迟问题；金融合规方面需注意 LLM 输出不可直接作为交易依据。

### 3.2 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，覆盖 AI 对齐、幻觉检测、提示注入、合规框架等。
- **为什么最近值得关注**：24h 涨星 +373，在中小体量项目中增速突出；主题覆盖 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM，契合企业级 Agent 治理需求。
- **技术栈/架构亮点**：Python + Apache-2.0；提供 CLI 与诊断工具，支持人工或 Agent 自审计，宣称 120 秒内给出结论。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。交易类 Agent 上线前需要审计与合规检查，该项目的审计思路可作为风控 Agent 的参考组件。
- **可能的风险**：项目较新，审计覆盖深度和准确性需进一步验证；不能替代正式合规审查。

### 3.3 qusong0627/QuantMind
- **解决什么问题**：面向个人开发者与投研团队的 AI 原生多市场量化交易平台，覆盖因子挖掘、模型训练、回测、舆情分析、实盘模拟等完整闭环。
- **为什么最近值得关注**：24h 涨星 +219，虽然总 star 仅 1252，但增速极快；描述中深度集成 Qlib、RD-Agent、TradingAgents，架构整合度高。
- **技术栈/架构亮点**：Python + AGPL-3.0；Docker Compose 一键私有化部署，数据与模型本地化；集成 300+ 维因子、13 种 ML/DL 模型、Optuna 调参、Qlib 回测、通达信联动。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其“因子挖掘 + 模型工场 + 回测 + 实盘模拟”的闭环设计可作为自建量化平台的参考蓝图。
- **可能的风险**：AGPL 协议对商业闭源使用有限制；描述中“零门槛无限制”存在营销化倾向；实盘模拟与真实交易之间存在显著差距；项目较新，维护稳定性待观察。

### 3.4 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，提供多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么最近值得关注**：总 star 64412，7 日涨星 +629，是“LLM 投研自动化”方向中体量较大的项目；近 30 天有 push。
- **技术栈/架构亮点**：Python + MIT；主题覆盖 A 股、AI Agent、AIGC、LLM、量化金融；强调多源数据与自动推送。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“多源数据 + LLM 分析 + 自动推送”的流水线可作为投研日报自动化的 MVP 参考。
- **可能的风险**：LLM 生成的股票分析可能存在幻觉与偏差；自动推送若被误用为交易信号，存在误导风险。

### 3.5 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 与交易流程结合，提供 AI Agent 驱动的交易体验。
- **为什么最近值得关注**：总 star 32195，7 日涨星 +549；来自 HKUDS，具备学术背景；主题覆盖 MCP、多 Agent、回测、量化金融。
- **技术栈/架构亮点**：Python + MIT；集成 MCP、多 Agent、回测等能力，强调“Vibe-Trading”的轻量化交互体验。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合作为“AI 交易 Agent 产品化”的参考，尤其是 MCP 工具集成与多 Agent 协作模式。
- **可能的风险**：crypto 相关，存在市场与合规风险；“Vibe-Trading”概念偏营销化，策略有效性未经严格验证；不建议直接用于实盘。

### 3.6 nautechsystems/nautilus_trader
- **解决什么问题**：提供生产级 Rust 原生交易引擎，采用确定性事件驱动架构，面向算法交易、做市、回测等场景。
- **为什么最近值得关注**：总 star 28230，7 日涨星 +524；是本次候选中少有的“交易基础设施”级项目，工程成熟度较高。
- **技术栈/架构亮点**：Rust + LGPL-3.0；确定性事件驱动架构，支持 crypto、equity、forex、futures、options 等多资产类别。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其确定性事件驱动设计、回测与实盘一致性思路，可作为自建交易系统的重要参考。
- **可能的风险**：LGPL 协议需注意链接方式；涉及杠杆/网格/做市等关键词，实盘风险较高；Rust 技术栈学习曲线较陡。

### 3.7 shiyu-coder/Kronos
- **解决什么问题**：构建“金融市场语言”基础模型，尝试用基础模型方法建模金融时序与市场语言。
- **为什么最近值得关注**：总 star 38238，24h 涨星 +100；是“金融基础模型”方向的代表性项目。
- **技术栈/架构亮点**：Python + MIT；定位为 Foundation Model for Financial Markets，属于研究导向项目。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合作为研究方向参考，尤其是金融时序基础模型的预训练与微调思路。
- **可能的风险**：研究属性强，距生产可用距离较远；金融基础模型的评估基准与过拟合风险需重点关注。

### 3.8 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，支持 LLM 策略定制与个股分析。
- **为什么最近值得关注**：24h 涨星 +63，7 日涨星 +388；技术栈现代，主题覆盖 DuckDB、Polars、FastAPI、React、LLM。
- **技术栈/架构亮点**：Python + MIT；采用 DuckDB + Polars 做本地数据工程，FastAPI + React 构建界面，支持第三方数据源扩展。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其“本地数据 + 现代数据栈 + LLM 策略定制”的组合是轻量级量化工作台的优秀范式。
- **可能的风险**：项目较新，总 star 仅 4064，维护活跃度待观察；A 股数据合规与接口稳定性需注意。

### 3.9 HiThink-Tech/Financial-API
- **解决什么问题**：同花顺官方 A 股金融数据服务，提供实时/历史行情、财务报表、指数、板块、涨停等数据，支持 API、MCP、CLI、Python。
- **为什么最近值得关注**：7 日涨星 +479，总 star 2084；官方背景 + MCP 支持，对 AI Agent 数据接入具有直接价值。
- **技术栈/架构亮点**：TypeScript + MIT；主题覆盖 DuckDB、MCP、REST API、量化金融；强调面向 AI Agent 的数据服务。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。MCP 化的金融数据服务可直接作为 Agent 的数据工具层。
- **可能的风险**：依赖官方数据服务，数据覆盖与稳定性受上游影响；需关注数据使用条款与合规限制。

### 3.10 virattt/ai-hedge-fund
- **解决什么问题**：模拟“AI 对冲基金团队”，用多 Agent 方式复刻对冲基金投研流程。
- **为什么最近值得关注**：总 star 63115，是“AI 对冲基金”方向的知名项目；虽近期涨星放缓，但架构参考价值仍高。
- **技术栈/架构亮点**：Python + MIT；多 Agent 模拟投研团队，覆盖 alpha 模型、回测、风控等关键词。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“多角色 Agent 投研团队”思路与 TradingAgents 互补，可作为 Agent 角色设计的参考。
- **可能的风险**：研究/模拟属性强，策略表现不代表真实收益；回测存在过拟合与幸存者偏差风险。

## 4. 趋势归纳

- **技术趋势**：
  - LLM 多智能体框架加速渗透金融投研与交易场景，`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund`、`ai-berkshire` 等项目形成明显集群。
  - 本地化/自托管量化工具栈兴起，DuckDB、Polars、FastAPI、Docker Compose 成为轻量级量化工作台的常见组合。
  - Rust 在交易基础设施中的地位上升，`nautilus_trader` 是典型代表。
  - Agent 治理、审计、上下文工程（Token 压缩、持久规划）成为配套基础设施热点。

- **产品趋势**：
  - 从“策略库”向“AI 原生量化平台”演进，强调因子挖掘、模型工场、回测、实盘模拟的闭环。
  - 金融数据服务开始原生支持 MCP，面向 AI Agent 提供数据接入。
  - 投研方法论产品化，如 `ai-berkshire` 将价值投资大师方法论结构化为多 Agent 研究框架。

- **量化/交易策略趋势**：
  - LLM 驱动的多 Agent 投研策略成为主流实验方向。
  - 金融基础模型（如 `Kronos`）尝试从模型层面建模市场语言。
  - 传统策略库（如 `fmzquant/strategies`）仍保持一定热度，但增速相对平缓。

- **AI Agent 与自动化交易结合趋势**：
  - Agent 角色分工日益细化：数据分析、舆情、风控、决策、审计等角色分离。
  - MCP 成为 Agent 连接金融数据与交易工具的标准接口。
  - Agent 审计与合规（`iFixAi`）开始独立成赛道，反映生产化需求。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据 Agent 工具层。
  - 多 Agent 投研流水线（数据 → 分析 → 风控 → 决策 → 审计）。
  - 本地化量化工作台（DuckDB + Polars + LLM）。
  - Agent 上下文压缩与持久规划在长周期投研任务中的应用。

## 5. 今日灵感清单

1. **MVP：LLM 投研日报 Agent**  
   参考 `daily_stock_analysis`，用 MCP 接入金融数据，自动生成多市场日报并推送，先做研究用途，不接实盘。

2. **MVP：多 Agent 投研沙盒**  
   参考 `TradingAgents` 与 `ai-hedge-fund`，用 Codex/Claude Code 复现一个最小多 Agent 投研流程，角色包括数据分析、策略、风控、审计。

3. **调研：MCP 金融数据生态**  
   调研 `HiThink-Tech/Financial-API`、`OpenBB`、`awesome-mcp-servers` 中金融相关 MCP server 的覆盖范围与接入成本。

4. **调研：Agent 审计与合规框架**  
   深入研究 `iFixAi` 的审计维度，评估能否将 EU AI Act、NIST AI RMF、OWASP LLM 等框架映射到交易 Agent 的风控检查清单。

5. **Demo：本地量化工作台原型**  
   参考 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭建一个本地 A 股选股/回测原型，验证现代数据栈在量化场景的可行性。

6. **Demo：Agent 上下文压缩**  
   参考 `headroom`，在长周期投研 Agent 中引入输出/日志压缩，验证 token 成本与上下文保持效果。

7. **Demo：持久规划 Agent**  
   参考 `planning-with-files`，为投研 Agent 增加基于文件的持久规划与崩溃恢复能力，验证长任务稳定性。

8. **Watchlist：Rust 交易引擎**  
   将 `nautilus_trader` 加入 watchlist，研究其确定性事件驱动架构与回测/实盘一致性设计。

9. **Watchlist：金融基础模型**  
   将 `Kronos` 加入 watchlist，跟踪金融时序基础模型的预训练与评估方法。

10. **调研：投资方法论结构化**  
    调研 `investorskills` 与 `ai-berkshire`，评估将投资大师方法论结构化为 Agent 可执行技能包的可行性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多 Agent 交易框架标杆，持续高速涨星，架构参考价值高 |
| ifixai-ai/iFixAi | Agent 审计/治理新兴赛道，24h 涨星突出，合规方向值得跟踪 |
| qusong0627/QuantMind | 量化闭环架构完整，增速快，但需观察维护稳定性 |
| nautechsystems/nautilus_trader | 生产级 Rust 交易引擎，交易基础设施参考价值高 |
| shiyu-coder/Kronos | 金融基础模型方向代表，研究价值高 |
| shy3130/tick-stock-panel | 现代数据栈量化工作台范式，轻量级架构值得借鉴 |
| HiThink-Tech/Financial-API | 官方金融数据 MCP 服务，Agent 数据层直接相关 |
| HKUDS/Vibe-Trading | AI 交易 Agent 产品化参考，但需注意 crypto 风险 |
| headroomlabs-ai/headroom | Agent 上下文工程关键组件，token 优化方向 |
| OthmanAdi/planning-with-files | Agent 持久规划与长任务稳定性，适合投研 Agent 借鉴 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-08-30）与 `baseline_7d`（2026-08-24），1 日与 7 日涨星数据基本完整。
- **缺失字段**：部分项目的 `star_delta_7d` 为 null（如 `Soup`、`awesome-public-datasets`），可能因 7 日基线中不存在该项目或采集失败；`star_delta_30d` 全部为 null，无法提供 30 日趋势。
- **样本偏差**：候选集由关键词搜索生成，存在大量“awesome-list”类通用资源因关键词误匹配进入榜单，与金融/量化/交易主题相关性参差不齐。部分项目 `language` 为 null，语言信息不足。
- **数据可信度**：项目描述、topics、matched_queries 均视为不可信分析材料，仅用于识别主题与风险标记，不作为事实依据。
