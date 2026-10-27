# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-26

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 多智能体金融交易框架**：以 `TauricResearch/TradingAgents` 为代表，24h 涨星 +1584，7d 涨星 +4284，总 star 116,448，是本期绝对头部。多 Agent 协作做交易决策的范式正在快速升温。
  2. **AI Agent 审计与对齐**：`ifixai-ai/iFixAi` 7d 涨星 +5000，聚焦“Agent 是否在做它该做的事”，把 AI 治理、风控、合规评估产品化，对金融场景的 Agent 落地有直接参考价值。
  3. **Claude/Codex Skills 生态向交易场景渗透**：`day-trader-skill`、`trader-skill`、`quantskills`、`Vibe-Trading` 等项目显示，基于 Claude Code / Codex 的“技能包”正在成为个人交易研究、回测、复盘的新载体。

- **是否出现新趋势**：出现。**“Agent Skills 即交易产品”** 的趋势明显——多个项目不再做完整交易系统，而是把交易研究、图表扫描、新闻跟踪、仓位管理拆成可被 Claude/Codex 调用的技能包。这降低了 AI 交易工具的构建门槛，但也放大了策略质量与安全边界的不确定性。

- **是否出现值得复刻/参考的工程架构**：是。`nautilus_trader` 的 Rust 事件驱动确定性交易引擎、`TradingAgents` 的多 Agent 决策编排、`iFixAi` 的 Agent 审计流水线、`tick-stock-panel` 的 DuckDB + Polars + FastAPI 轻量量化工作台，都具备工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本期未发现明显骗局，但存在若干**过度营销倾向**项目，例如 `ruflo` 自称“original agent harness”、`QuantDinger` 宣称可“launch your own multi-tenant trading SaaS”，描述明显超出可验证范围。`day-trader-skill`、`trader-skill` 等直接面向日内交易决策的技能包，存在策略过拟合与误导性收益预期风险。所有 `trading_bot` 标记项目均需按高风险对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TauricResearch/TradingAgents | 116,448 | +1584 | +4284 | Python | AI 交易/多智能体 | LLM 多智能体金融交易框架 | 高：多 Agent 决策编排 | 低 |
| 2 | ifixai-ai/iFixAi | 35,187 | +671 | +5000 | Python | AI 治理/风控 | AI Agent 独立审计与对齐工具 | 高：Agent 审计流水线 | 低 |
| 3 | awesome-selfhosted/awesome-selfhosted | 330,816 | +338 | +2367 | 无 | 自托管清单 | 自托管网络服务清单 | 中：交易基础设施选型 | 中 |
| 4 | ruvnet/ruflo | 79,598 | +274 | +2265 | TypeScript | Agent 框架 | 多智能体集群与工作流编排 | 中：Agent 编排参考 | 低 |
| 5 | public-apis/public-apis | 492,488 | +297 | +1883 | Python | API 清单 | 免费 API 集合 | 中：数据源发现 | 低 |
| 6 | shiyu-coder/Kronos | 43,882 | +100 | +2060 | Python | 量化研究 | 金融市场语言基础模型 | 高：金融基础模型 | 低 |
| 7 | vinta/awesome-python | 330,518 | +217 | +1730 | Python | Python 清单 | Python 工具精选 | 低 | 低 |
| 8 | codecrafters-io/build-your-own-x | 556,494 | +244 | +1855 | Markdown | 教程清单 | 从零复刻技术项目 | 中：交易系统教学 | 中 |
| 9 | aardappel/goose | 2,267 | +163 | +1648 | C++ | 交易基础设施 | Goose 编程语言 | 中：高性能语言探索 | 低 |
| 10 | awesome-dsh-plugin/awesome-dsh-plugin | 20,959 | +226 | +1373 | JavaScript | 插件清单 | DeepSeek Harness 插件列表 | 中：Agent 插件生态 | 低 |
| 11 | avelino/awesome-go | 190,549 | +165 | +1242 | Go | Go 清单 | Go 框架与库精选 | 中：Go 交易基础设施 | 中 |
| 12 | JustVugg/colibri | 44,090 | +164 | +1167 | C | 量化研究 | 纯 C 本地 MoE 推理引擎 | 中：本地模型推理 | 低 |
| 13 | HKUDS/Vibe-Trading | 36,795 | +93 | +827 | Python | AI 交易/回测 | 个人交易 Agent | 高：MCP 交易 Agent | 低 |
| 14 | hesreallyhim/awesome-claude-code | 56,630 | +77 | +579 | Python | Claude 生态 | Claude Code 资源精选 | 中：Agent 技能发现 | 低 |
| 15 | sickn33/agentic-awesome-skills | 48,563 | +58 | +595 | Python | Agent 技能 | 本地 Agent 控制平面 | 中：技能目录架构 | 低 |
| 16 | goldmansachs/gs-quant | 13,716 | +93 | +484 | Python | 量化/风控 | 高盛量化金融工具包 | 高：机构级风控建模 | 低 |
| 17 | punkpeye/awesome-remote-mcp-servers | 2,031 | +84 | +469 | 无 | MCP 清单 | 远程 MCP 服务器集合 | 中：MCP 数据接入 | 低 |
| 18 | ZhuLinsen/daily_stock_analysis | 67,126 | +62 | +366 | Python | AI 交易/数据工程 | LLM 多市场股票分析系统 | 高：零成本定时分析 | 低 |
| 19 | freqtrade/freqtrade | 56,011 | +53 | +358 | Python | 加密交易/回测 | 开源加密交易机器人 | 中：回测与实盘架构 | 中 |
| 20 | Fincept-Corporation/FinceptTerminal | 33,169 | +45 | +396 | C++ | 金融终端 | 现代金融分析终端 | 中：终端产品形态 | 低 |
| 21 | plugin87/ux-ui-agent-skills | 3,030 | +23 | +618 | JavaScript | Agent 技能 | Claude 设计架构技能 | 低 | 低 |
| 22 | anbeime/skill | 8,726 | +63 | +365 | Python | Agent 技能 | AI Agent 技能商店 | 中：技能分发模式 | 低 |
| 23 | Open-Dev-Society/OpenStock | 20,889 | +18 | +514 | TypeScript | 股票市场 | 开源市场行情平台 | 中：行情产品形态 | 低 |
| 24 | openbq-org/OpenBB | 74,764 | +45 | +301 | Python | 量化研究 | 分析师与 AI Agent 数据平台 | 高：Agent 数据层 | 中 |
| 25 | nautechsystems/nautilus_trader | 30,912 | +57 | +552 | Rust | 交易引擎/回测 | Rust 事件驱动交易引擎 | 高：确定性回测架构 | 中 |
| 26 | ripienaar/free-for-dev | 140,079 | +32 | +256 | HTML | 免费资源 | 开发者免费资源清单 | 低 | 低 |
| 27 | code-yeongyu/oh-my-openagent | 70,379 | +44 | +169 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中：Agent 编排 UI | 低 |
| 28 | Jakeschincariol/day-trader-skill | 2,107 | +391 | 信息不足 | Python | 交易技能 | 11 个 Claude 日内交易技能 | 中：交易技能拆解 | 低 |
| 29 | mudler/LocalAI | 49,991 | +31 | +250 | Go | 本地 AI | 本地 AI 推理引擎 | 中：本地模型部署 | 低 |
| 30 | MakazhanAlpamys/Soup | 9,704 | +38 | +265 | Python | 模型微调 | 单 YAML 微调 LLM | 中：低资源微调 | 低 |
| 31 | microsoft/qlib | 49,742 | +30 | +205 | Python | 量化平台 | 微软 AI 量化投资平台 | 高：ML 量化范式 | 低 |
| 32 | Jakeschincariol/trader-skill | 729 | +101 | 信息不足 | Python | 交易技能 | 11 个 Claude 投资技能 | 中：投资研究技能化 | 低 |
| 33 | Orchestra-Research/AI-Research-SKILLs | 13,986 | +37 | +254 | TeX | AI 研究技能 | AI 研究工程技能库 | 中：研究 Agent 化 | 低 |
| 34 | cactus-compute/needle | 14,342 | +32 | +223 | Python | 端侧模型 | 微型设备自动化基础模型 | 低 | 中 |
| 35 | fffaraz/awesome-cpp | 74,055 | +23 | +153 | 无 | C++ 清单 | C++ 框架与库精选 | 中：低延迟基础设施 | 低 |
| 36 | shy3130/tick-stock-panel | 6,355 | +29 | +185 | Python | 量化工作台 | A 股自托管量化工作台 | 高：DuckDB+Polars 架构 | 低 |
| 37 | virattt/ai-hedge-fund | 64,278 | +18 | +171 | Python | AI 交易/回测 | AI 对冲基金团队模拟 | 高：多角色 Agent 模拟 | 低 |
| 38 | lightningpixel/modly | 8,418 | +35 | +161 | TypeScript | 3D 生成 | 本地 AI 3D 模型生成 | 低 | 低 |
| 39 | rust-unofficial/awesome-rust | 60,146 | +17 | +174 | Rust | Rust 清单 | Rust 资源精选 | 中：Rust 交易栈 | 低 |
| 40 | antirez/ds4 | 24,109 | +21 | +145 | C | 本地推理 | DeepSeek 本地推理引擎 | 中：本地推理性能 | 低 |
| 41 | serhii-londar/open-source-mac-os-apps | 51,060 | +20 | +164 | 无 | macOS 清单 | macOS 开源应用清单 | 低 | 低 |
| 42 | cporter202/API-mega-list | 8,220 | +16 | +263 | JavaScript | API 清单 | API 大合集 | 中：数据源发现 | 中 |
| 43 | OpenByteInc/QuantDinger | 13,146 | +16 | +203 | Python | AI 交易/回测 | 开源 AI 交易操作系统 | 中：多租户交易 SaaS | 中 |
| 44 | simonlin1212/Vibe-Research | 2,992 | +12 | +243 | TypeScript | 投研工作台 | A/美/港股投研工作台 | 高：多市场投研 Agent | 低 |
| 45 | fasiondog/hikyuu | 3,631 | +54 | +65 | C++ | 量化回测 | C++/Python 高性能量化框架 | 中：高性能回测 | 低 |
| 46 | quantskills/quantskills | 2,313 | +25 | +163 | JavaScript | 量化技能 | 量化 Skill 与 Agent 生态导航 | 高：量化技能生态 | 低 |
| 47 | xbtlin/ai-berkshire | 16,898 | +14 | +93 | HTML | 价值投资 | 价值投资多 Agent 研究框架 | 高：多大师方法论 Agent | 低 |
| 48 | josephmisiti/awesome-machine-learning | 74,666 | +7 | +48 | Python | ML 清单 | 机器学习资源精选 | 低 | 低 |
| 49 | Developer-Y/cs-video-courses | 83,771 | +1 | +62 | 无 | 课程清单 | CS 视频课程列表 | 低 | 中 |
| 50 | tradesdontlie/tradingview-mcp | 6,962 | +16 | +83 | JavaScript | 交易 MCP | TradingView 图表分析 MCP | 中：图表分析自动化 | 中 |
| 51 | charlax/professional-programming | 51,660 | +7 | +25 | Python | 工程学习 | 软件工程师学习资源 | 低 | 中 |
| 52 | akullpp/awesome-java | 49,366 | +12 | +64 | 无 | Java 清单 | Java 框架与库精选 | 低 | 中 |
| 53 | vuejs/awesome-vue | 73,506 | -3 | -7 | 无 | Vue 清单 | Vue 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：把金融交易决策拆解为多个 LLM Agent 协作完成，覆盖基本面、技术面、情绪面、风险管理等角色，输出结构化交易信号。
- **为什么值得关注**：24h 涨星 +1584，是本期涨星绝对第一；总 star 116,448，说明“多 Agent 交易决策”已从实验走向大众关注。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 编排是核心，适合研究 Agent 间如何分工、如何汇总冲突信号、如何做最终决策。
- **是否适合借鉴**：适合。可借鉴其 Agent 角色划分与决策汇总机制，用于企业级投研 Agent 或风控 Agent 的架构设计。
- **可能风险**：作为研究工具，其信号质量未经实盘验证；多 Agent 输出可能存在“集体幻觉”或过度自信；不可直接用于实盘。

### 3.2 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 的行为进行独立审计，回答“Agent 是否在做它该做的事”，覆盖幻觉检测、提示注入、AI 对齐、合规评估等。
- **为什么值得关注**：7d 涨星 +5000，增速极快；在 AI Agent 经济中，审计与治理是金融场景落地的关键缺口。
- **技术栈/架构亮点**：Python + Apache-2.0；提供 CLI 与诊断工具，覆盖 ISO 42001、NIST AI RMF、OWASP LLM、EU AI Act 等标准。
- **是否适合借鉴**：非常适合。金融企业部署交易 Agent 前，可参考其审计流水线构建内部 Agent 合规检查层。
- **可能风险**：审计标准本身仍在演进；对金融交易 Agent 的审计深度可能不足；需验证其检测准确率。

### 3.3 shiyu-coder/Kronos
- **解决什么问题**：构建“金融市场语言”基础模型，试图用统一模型理解价格、订单流、新闻等金融序列。
- **为什么值得关注**：7d 涨星 +2060，总 star 43,882；金融基础模型是量化研究的前沿方向。
- **技术栈/架构亮点**：Python + MIT；模型导向，具体架构信息不足。
- **是否适合借鉴**：适合作为研究方向跟踪，可关注其输入表示、预训练任务、下游微调方式。
- **可能风险**：金融基础模型容易过拟合历史模式；模型输出不可解释；研究工具属性强，离实盘很远。

### 3.4 HKUDS/Vibe-Trading
- **解决什么问题**：提供“个人交易 Agent”，结合 LLM、MCP、多 Agent 做交易研究与回测。
- **为什么值得关注**：香港大学团队出品，总 star 36,795；将 MCP 协议引入交易 Agent，是 AI 交易工具化的典型样本。
- **技术栈/架构亮点**：Python + MIT；topics 包含 ai-agent、mcp、multi-agent、backtesting，说明其架构围绕 MCP 工具调用与多 Agent 协作展开。
- **是否适合借鉴**：适合。可重点研究其 MCP 工具如何封装行情、回测、组合优化等能力。
- **可能风险**：研究工具属性强；策略表现未经独立验证；MCP 工具链若接入真实交易接口，存在 API key 泄露风险。

### 3.5 nautechsystems/nautilus_trader
- **解决什么问题**：提供生产级 Rust 原生交易引擎，强调确定性事件驱动架构，支持回测与实盘。
- **为什么值得关注**：Rust 在交易系统领域的高性能与内存安全优势明显；7d 涨星 +552，持续活跃。
- **技术栈/架构亮点**：Rust + LGPL-3.0；事件驱动、确定性回测是其核心卖点，适合对回测准确性要求高的场景。
- **是否适合借鉴**：适合。若团队计划自建交易引擎或回测平台，其事件驱动与确定性设计值得深入研究。
- **可能风险**：LGPL 许可证对闭源商用有约束；涉及加密、杠杆、网格等标记，实盘风险高；学习曲线陡峭。

### 3.6 goldmansachs/gs-quant
- **解决什么问题**：高盛开源的量化金融 Python 工具包，覆盖衍生品定价、风险管理、交易策略。
- **为什么值得关注**：机构级背景，Apache-2.0；是理解投行级风控与定价建模的窗口。
- **技术栈/架构亮点**：Python；topics 包含 derivatives、risk-management、trading-strategies，说明其重点在衍生品与风控。
- **是否适合借鉴**：适合。可借鉴其风险模型与衍生品定价模块的设计，用于企业级风控原型。
- **可能风险**：机构工具往往依赖内部数据与假设；直接套用到个人或小团队场景可能不适用。

### 3.7 shy3130/tick-stock-panel
- **解决什么问题**：A 股自托管量化工作台，集成自建策略、监控、回测，支持 LLM 驱动策略定制与个股分析。
- **为什么值得关注**：技术栈现代且轻量，DuckDB + Polars + FastAPI + React 的组合适合个人或小团队快速搭建。
- **技术栈/架构亮点**：Python + MIT；DuckDB 做本地分析、Polars 做数据处理、FastAPI 做服务层，是低成本量化工作台的优秀范式。
- **是否适合借鉴**：非常适合。可作为内部量化研究 MVP 的架构参考，尤其是本地数据栈的选择。
- **可能风险**：A 股数据源合规性需确认；LLM 生成的策略存在过拟合风险；个人开源项目维护持续性不确定。

### 3.8 virattt/ai-hedge-fund
- **解决什么问题**：模拟一个 AI 对冲基金团队，多个 Agent 扮演不同角色做投资决策。
- **为什么值得关注**：总 star 64,278，是 AI 交易模拟类项目的标杆；概念直观，易于理解多 Agent 投资决策流程。
- **技术栈/架构亮点**：Python + MIT；多角色 Agent 模拟是其核心，适合教学与原型验证。
- **是否适合借鉴**：适合。可借鉴其角色设计与决策流程，用于内部投研 Agent 的概念验证。
- **可能风险**：模拟结果不代表真实收益；角色输出可能高度依赖提示词质量；不可直接用于实盘。

### 3.9 microsoft/qlib
- **解决什么问题**：微软开源的 AI 量化投资平台，覆盖数据、因子、模型训练、回测、组合优化全流程。
- **为什么值得关注**：机构级背景，总 star 49,742；是 AI 量化研究的完整参考实现。
- **技术栈/架构亮点**：Python + MIT；支持监督学习、市场动态建模、强化学习，并集成 RD-Agent 自动化研发。
- **是否适合借鉴**：适合。可借鉴其 ML 量化研究流水线与 RD-Agent 的自动化研发思路。
- **可能风险**：平台较重，学习成本高；AI 模型存在过拟合风险；需自行验证数据质量。

### 3.10 xbtlin/ai-berkshire
- **解决什么问题**：基于 Claude Code / Codex 的价值投资研究框架，融合巴菲特、芒格、段永平、李录四套方法论，多 Agent 并行研究。
- **为什么值得关注**：总 star 16,898；将价值投资方法论显式编码为 Agent 流程，是“投研方法论产品化”的典型案例。
- **技术栈/架构亮点**：HTML + MIT；多 Agent 对抗分析是其特色，适合研究如何把主观投资框架结构化。
- **是否适合借鉴**：适合。可借鉴其方法论编码方式，用于内部投研知识库与 Agent 结合。
- **可能风险**：价值投资方法论难以完全量化；Agent 输出可能流于表面；不可作为投资建议。

## 4. 趋势归纳

- **技术趋势**：
  - **多智能体协作成为 AI 交易主流范式**：TradingAgents、Vibe-Trading、ai-hedge-fund、ai-berkshire 均采用多 Agent 分工。
  - **MCP 成为交易工具接入标准**：Vibe-Trading、tradingview-mcp、QuantDinger、Vibe-Research 均涉及 MCP。
  - **本地化与轻量化推理**：colibri、LocalAI、ds4、needle 等项目显示本地模型推理在金融场景的可行性提升。
  - **Rust 与 C++ 在交易基础设施中持续受关注**：nautilus_trader、hikyuu、FinceptTerminal、goose 代表高性能路线。

- **产品趋势**：
  - **从“完整交易系统”转向“Agent Skills 技能包”**：day-trader-skill、trader-skill、quantskills、AI-Research-SKILLs 等将交易能力拆分为可复用技能。
  - **投研工作台产品化**：Vibe-Research、tick-stock-panel、daily_stock_analysis、FinceptTerminal 均以工作台形态呈现。
  - **AI 治理与审计产品化**：iFixAi 将 Agent 审计作为独立产品，预示金融 AI 合规需求上升。

- **量化/交易策略趋势**：
  - **金融基础模型探索**：Kronos 代表“金融市场语言模型”方向。
  - **价值投资与主观方法论的结构化**：ai-berkshire 将大师方法论编码为 Agent 流程。
  - **多市场覆盖**：daily_stock_analysis、Vibe-Research 覆盖 A 股、美股、港股。

- **AI Agent 与自动化交易结合趋势**：
  - Agent 不再只是“聊天机器人”，而是具备**研究、回测、监控、决策、审计**全链路的执行体。
  - **技能包 + MCP + 本地模型**的组合正在降低个人构建交易 Agent 的门槛，但也带来策略质量与安全边界的新挑战。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的投研数据接入层。
  - 多 Agent 投研决策的对抗式验证机制。
  - Agent 交易行为的审计与合规检查流水线。
  - DuckDB + Polars 的轻量量化回测工作台。
  - 金融基础模型在下游预测任务上的微调效果。

## 5. 今日灵感清单

1. **MVP：本地投研 Agent 工作台**：参考 `tick-stock-panel` 的 DuckDB + Polars + FastAPI 架构，搭建一个本地运行的投研工作台，集成行情数据、新闻、LLM 分析，输出每日研究报告。
2. **MVP：Agent 交易行为审计层**：参考 `iFixAi`，为内部交易 Agent 构建一个审计模块，记录每次决策的输入、输出、工具调用，检测提示注入与异常行为。
3. **调研：MCP 在交易数据接入中的标准化程度**：对比 `Vibe-Trading`、`tradingview-mcp`、`QuantDinger` 的 MCP 工具设计，评估是否可抽象出一套通用的交易数据 MCP 接口。
4. **调研：金融基础模型 Kronos 的输入表示与预训练任务**：阅读其论文与代码，评估是否可将类似思路用于内部数据。
5. **Codex/Agent 自动复现 demo：多角色对冲基金模拟**：参考 `ai-hedge-fund`，让 Codex 自动生成一个简化版多角色投研 Agent，验证角色分工与决策汇总逻辑。
6. **MVP：价值投资方法论 Agent 模板**：参考 `ai-berkshire`，将一种投资方法论编码为 Claude Code 技能包，验证方法论结构化的可行性。
7. **调研：Rust 确定性回测引擎的事件驱动设计**：以 `nautilus_trader` 为样本，研究其事件排序、时钟同步、回测与实盘一致性方案。
8. **Watchlist：gs-quant 的衍生品风控模块**：研究其风险模型与定价接口，评估是否可用于内部风控原型。
9. **MVP：零成本定时股票分析推送**：参考 `daily_stock_analysis`，用 GitHub Actions 定时运行 LLM 分析，推送到 IM，验证零成本投研自动化。
10. **调研：Agent Skills 的分发与版本管理**：对比 `anbeime/skill`、`agentic-awesome-skills`、`awesome-dsh-plugin`，研究技能包的目录结构、版本管理与分发模式。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多 Agent 交易决策的头部项目，观察其架构演进与社区反馈 |
| ifixai-ai/iFixAi | AI Agent 审计与治理的快速崛起项目，金融 AI 合规关键参考 |
| shiyu-coder/Kronos | 金融基础模型前沿方向，值得长期跟踪研究进展 |
| HKUDS/Vibe-Trading | MCP + 多 Agent 交易的代表，观察其工具链设计 |
| nautechsystems/nautilus_trader | Rust 确定性交易引擎，高性能回测与实盘架构参考 |
| goldmansachs/gs-quant | 机构级风控与衍生品建模，企业级风控原型参考 |
| shy3130/tick-stock-panel | 轻量量化工作台，DuckDB + Polars 架构值得复刻 |
| microsoft/qlib | 微软 AI 量化平台，ML 量化研究流水线参考 |
| xbtlin/ai-berkshire | 价值投资方法论 Agent 化，投研知识结构化参考 |
| quantskills/quantskills | 量化 Skill 生态导航，观察技能包生态演进 |
| virattt/ai-hedge-fund | 多角色对冲基金模拟，教学与原型验证参考 |
| OpenBB | 面向分析师与 AI Agent 的数据平台，数据层设计参考 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-10-25.json`，1 日涨星数据完整。
- **7 日基线**：已提供 `baseline_7d: 2026-10-19.json`，7 日涨星数据基本完整。
- **缺失数据**：`day-trader-skill` 与 `trader-skill` 的 7 日涨星为 null，原因是项目创建时间晚于 7 日基线，无法计算 7 日增量，已在表格中标注“信息不足”。
- **30 日涨星**：所有项目的 `star_delta_30d` 均为 null，本次报告未包含 30 日涨星分析。
- **采集失败**：未发现明显采集失败。
- **样本偏差**：候选项目通过关键词匹配（backtest、backtesting、quant、trading bot、order book、risk model 等）筛选，导致大量 awesome-list 类项目因 README 命中关键词而进入候选，与金融/量化/交易主题的相关性参差不齐。报告已尽量区分核心项目与泛化清单项目，但样本偏差仍可能影响趋势判断。
