# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-27

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 交易框架**：TradingAgents、Vibe-Trading、OpenAlice、QuantDinger 等 LLM 多智能体交易框架持续高热，说明“用 LLM 组织投研/交易决策流程”已成为独立赛道。
  2. **AI Agent 工程基础设施**：OpenBot、ruflo、headroom、planning-with-files、iFixAi 等项目聚焦 Agent 治理、上下文压缩、审计与规划，反映 Agent 从“能跑”走向“可治理、可审计、可恢复”。
  3. **A 股数据与研究工作台**：daily_stock_analysis、a-stock-data、tick-stock-panel、ai-berkshire 等中文项目集中出现，显示 A 股本地化数据工程 + LLM 投研正在形成独立生态。

- **是否出现新趋势**：出现。传统“交易 bot”热度被“AI Agent 交易/投研框架”和“Agent 工程治理”明显分流；同时出现大量“awesome-list”类项目因关键词误匹配进入榜单，真实交易基础设施项目占比下降。

- **是否出现值得复刻/参考的工程架构**：是。`nautilus_trader` 的 Rust 事件驱动交易引擎、`itchbook` 的 NASDAQ ITCH 5.0 订单簿重建与队列感知回测、`headroom` 的 LLM 上下文压缩代理、`iFixAi` 的 Agent 审计框架，均具备较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：有。`Polymarket-Telegram-Bot` 为当日新建、无描述、24h 涨星 80 的 Telegram 交易 bot，属于典型高风险/疑似营销项目；`Financial_freedom` 标题为“最全赚钱投资指南”，营销属性强；多个“awesome-list”项目因关键词误匹配进入榜单，实际与金融/量化无关，需过滤。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 472028 | 697 | 4752 | Python | API 列表 | 免费 API 合集 | 低 | 中 |
| 2 | nexu-io/open-design | 92255 | 332 | 2477 | 未知 | AI 设计 | 本地优先 AI 设计引擎 | 中 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 122334 | 735 | 3495 | Python | AI 设计 | UI/UX 设计智能 skill | 中 | 低 |
| 4 | ripienaar/free-for-dev | 135684 | 221 | 3280 | HTML | 资源列表 | 开发者免费资源 | 低 | 低 |
| 5 | awesome-dsh-plugin/awesome-dsh-plugin | 13328 | 222 | 2638 | Python | 插件列表 | DeepSeek Harness 插件列表 | 低 | 低 |
| 6 | TauricResearch/TradingAgents | 101527 | 705 | 2456 | Python | AI 交易 | 多智能体 LLM 金融交易框架 | 高 | 低 |
| 7 | codecrafters-io/build-your-own-x | 543576 | 268 | 1950 | Markdown | 教程 | 从零构建技术教程合集 | 低 | 中 |
| 8 | awesome-selfhosted/awesome-selfhosted | 315697 | 202 | 1711 | 未知 | 自托管 | 自托管服务列表 | 低 | 中 |
| 9 | VoltAgent/awesome-design-md | 111001 | 222 | 1538 | 未知 | 设计系统 | DESIGN.md 设计系统合集 | 低 | 中 |
| 10 | vinta/awesome-python | 316648 | 288 | 1480 | Python | 资源列表 | Python 工具精选 | 低 | 低 |
| 11 | CopilotKit/OpenBot | 3240 | 138 | 1562 | TypeScript | AI Agent | 开源 AI 数字员工框架 | 高 | 中 |
| 12 | cactus-compute/needle | 9510 | 137 | 1370 | Python | 端侧模型 | 14MB 端侧基础模型 | 中 | 中 |
| 13 | ruvnet/ruflo | 69603 | 90 | 1089 | TypeScript | Agent 框架 | Agent 元编排框架 | 高 | 低 |
| 14 | headroomlabs-ai/headroom | 67879 | 122 | 863 | Python | 上下文压缩 | LLM 输出压缩代理 | 高 | 低 |
| 15 | unslothai/unsloth | 75027 | 93 | 918 | Python | 模型训练 | 本地 LLM 训练/推理 UI | 中 | 低 |
| 16 | avelino/awesome-go | 182501 | 103 | 770 | Go | 资源列表 | Go 框架库精选 | 低 | 中 |
| 17 | nautechsystems/nautilus_trader | 27990 | 74 | 1270 | Rust | 交易引擎 | Rust 事件驱动交易引擎 | 高 | 中 |
| 18 | ZhuLinsen/daily_stock_analysis | 64186 | 100 | 674 | Python | A 股分析 | LLM 多市场股票分析系统 | 高 | 低 |
| 19 | HKUDS/Vibe-Trading | 31934 | 92 | 575 | Python | AI 交易 | 个人交易 Agent | 高 | 中 |
| 20 | JustVugg/colibri | 26331 | 61 | 710 | C | 模型推理 | 纯 C 零依赖 MoE 推理引擎 | 中 | 低 |
| 21 | goldmansachs/gs-quant | 12770 | 28 | 702 | Python | 量化工具 | 高盛量化金融工具包 | 高 | 低 |
| 22 | garrytan/gbrain | 29229 | 64 | 404 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent 大脑 | 中 | 低 |
| 23 | punkpeye/awesome-mcp-servers | 92936 | 67 | 309 | 未知 | MCP 列表 | MCP 服务器合集 | 中 | 低 |
| 24 | ifixai-ai/iFixAi | 11284 | 93 | 241 | Python | Agent 审计 | AI Agent 独立审计工具 | 高 | 低 |
| 25 | langfuse/langfuse | 33856 | 60 | 371 | TypeScript | LLM 可观测 | LLM 评估与可观测平台 | 高 | 低 |
| 26 | RyanCodrai/turbovec | 16482 | 30 | 515 | Rust | 向量索引 | TurboQuant 向量索引 | 中 | 低 |
| 27 | perixtar/Tech-OA-Interview-Questions | 4648 | 62 | 472 | Python | 面试题 | 科技公司面试题合集 | 低 | 低 |
| 28 | nidhinjs/prompt-master | 11877 | 47 | 353 | 未知 | Prompt | Claude skill 提示词工具 | 中 | 低 |
| 29 | coding-kitties/investing-algorithm-framework | 1937 | 110 | 227 | Python | 量化框架 | 量化交易开发框架 | 中 | 中 |
| 30 | code-yeongyu/oh-my-openagent | 68462 | 35 | 283 | TypeScript | Agent 框架 | 复杂代码库 Agent 编排 | 中 | 低 |
| 31 | cinar/indicator | 1440 | 144 | 213 | Go | 技术指标 | Go 技术指标与回测库 | 中 | 低 |
| 32 | antirez/ds4 | 21873 | 40 | 265 | C | 模型推理 | DeepSeek 4 本地推理引擎 | 中 | 低 |
| 33 | OpenBB-finance/OpenBB | 72394 | 36 | 308 | Python | 数据平台 | 开放金融数据平台 | 高 | 中 |
| 34 | simonlin1212/a-stock-data | 9279 | 15 | 342 | 未知 | A 股数据 | A 股全栈数据工具包 | 高 | 低 |
| 35 | TraderAlice/OpenAlice | 6802 | 51 | 187 | TypeScript | AI 交易 | 全资产 AI 交易 Agent | 高 | 中 |
| 36 | OpenByteInc/QuantDinger | 11152 | 29 | 262 | Python | AI 量化 | AI 量化交易平台 | 高 | 中 |
| 37 | lsdefine/GenericAgent | 14071 | 24 | 246 | Python | Agent 框架 | 自进化 Agent 技能树 | 中 | 低 |
| 38 | xbtlin/ai-berkshire | 15943 | 18 | 220 | Python | 价值投资 | 多 Agent 价值投资研究框架 | 高 | 低 |
| 39 | codeman008/Financial_freedom | 3573 | 11 | 414 | 未知 | 投资指南 | 赚钱投资指南 | 低 | 中 |
| 40 | rust-unofficial/awesome-rust | 59017 | 29 | 107 | Rust | 资源列表 | Rust 资源精选 | 低 | 低 |
| 41 | fffaraz/awesome-cpp | 72975 | 19 | 125 | 未知 | 资源列表 | C/C++ 资源精选 | 低 | 低 |
| 42 | josephmisiti/awesome-machine-learning | 74192 | 16 | 104 | Python | 资源列表 | ML 框架库精选 | 低 | 低 |
| 43 | ai-boost/awesome-harness-engineering | 3850 | 23 | 188 | Python | Agent 工程 | Agent 编排工程精选 | 中 | 低 |
| 44 | shy3130/tick-stock-panel | 3894 | 50 | 未知 | Python | A 股量化 | A 股选股监控回测工作台 | 高 | 低 |
| 45 | OthmanAdi/planning-with-files | 26397 | 12 | 132 | Shell | Agent 规划 | 基于文件的 Agent 规划 | 高 | 低 |
| 46 | Orchestra-Research/AI-Research-SKILLs | 12121 | 31 | 222 | TeX | AI 研究 | AI 研究技能库 | 中 | 低 |
| 47 | awesomedata/awesome-public-datasets | 78688 | 20 | 未知 | 未知 | 数据集 | 公开数据集精选 | 低 | 中 |
| 48 | KareemJandali/itchbook | 78 | 77 | 77 | C++ | 订单簿回测 | NASDAQ ITCH 订单簿重建 | 高 | 低 |
| 49 | virattt/ai-hedge-fund | 63071 | 6 | 102 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 50 | Developer-Y/cs-video-courses | 83189 | 2 | 52 | 未知 | 课程 | CS 视频课程列表 | 低 | 中 |
| 51 | Cleverfuxaqo1668/Polymarket-Telegram-Bot | 167 | 80 | 未知 | JavaScript | 交易 bot | Polymarket Telegram Bot | 低 | 中 |
| 52 | vuejs/awesome-vue | 73547 | 5 | 9 | 未知 | 资源列表 | Vue 资源精选 | 低 | 低 |
| 53 | ByteByteGoHq/system-design-101 | 87686 | 27 | 322 | 未知 | 系统设计 | 系统设计图解 | 中 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将金融交易决策拆解为多个 LLM Agent 协作，覆盖基本面、技术面、情绪面、风控等角色，输出交易决策。
- **为什么值得关注**：24h 涨星 705、7d 涨星 2456，总 star 超 10 万，是当前“LLM 多智能体交易”方向最具代表性的开源项目之一。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 角色分工；将 LLM 推理与金融数据结合。
- **是否适合借鉴**：适合借鉴其“多角色投研决策流水线”设计，用于企业级投研 Agent 或风控 Agent 框架。
- **可能风险**：策略过拟合、回测幸存者偏差；LLM 输出不稳定；研究工具属性强，不宜直接实盘。

### 3.2 nautechsystems/nautilus_trader
- **解决什么问题**：提供生产级、确定性的 Rust 原生事件驱动交易引擎，支持回测与实盘。
- **为什么值得关注**：7d 涨星 1270，是少数真正面向生产环境的开源交易基础设施项目。
- **技术栈/架构亮点**：Rust 核心 + Python 接口；确定性事件驱动架构；支持多资产、多交易所。
- **是否适合借鉴**：非常适合借鉴其事件溯源、确定性回测、订单簿建模思路，用于自建交易系统或回测平台。
- **可能风险**：LGPL-3.0 许可证；涉及杠杆/网格相关标记，实盘需谨慎；学习曲线陡峭。

### 3.3 CopilotKit/OpenBot
- **解决什么问题**：为 AI Agent 提供独立“电脑”——浏览器、文件、工具，所有动作可事前决策、事后记录，支持 AG-UI Agent。
- **为什么值得关注**：7d 涨星 1562，项目创建仅约 10 天，增长极快，代表“Agent 治理 + 浏览器自动化”新方向。
- **技术栈/架构亮点**：TypeScript + MIT；AG-UI、MCP、生成式 UI；动作决策与记录分离。
- **是否适合借鉴**：适合借鉴其“Agent 动作审计/记录”机制，用于企业级 Agent 合规与可观测性。
- **可能风险**：项目过新，维护活跃度待观察；浏览器自动化存在安全边界问题。

### 3.4 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 接收前压缩工具输出、日志、文件、RAG 片段，降低 token 消耗。
- **为什么值得关注**：7d 涨星 863，总 star 6.7 万，解决 Agent 上下文成本与上下文窗口瓶颈。
- **技术栈/架构亮点**：Python + Apache-2.0；库、代理、MCP server 三种形态；针对 JSON 可压缩 60-95% token。
- **是否适合借鉴**：非常适合借鉴到高频调用 LLM 的投研/交易 Agent 中，降低上下文成本。
- **可能风险**：压缩可能损失关键信息，需在金融场景验证信息保真度。

### 3.5 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析，集成多源行情、实时新闻、决策看板与自动推送。
- **为什么值得关注**：总 star 6.4 万，7d 涨星 674，是 A 股 LLM 投研方向的高热度项目。
- **技术栈/架构亮点**：Python + MIT；多源数据、定时任务、决策看板；强调零成本运行。
- **是否适合借鉴**：适合借鉴其“数据采集 + LLM 分析 + 推送”的轻量级投研流水线。
- **可能风险**：数据源稳定性；LLM 分析结论不可作为投资依据；需注意合规。

### 3.6 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多 Agent 进行交易研究与决策。
- **为什么值得关注**：HKUDS 出品，7d 涨星 575，总 star 3.1 万，学术背景 + 交易 Agent 结合。
- **技术栈/架构亮点**：Python + MIT；MCP、多 Agent、回测集成。
- **是否适合借鉴**：适合借鉴其 MCP 工具接入与多 Agent 交易研究流程。
- **可能风险**：研究工具属性；策略过拟合；不宜直接实盘。

### 3.7 goldmansachs/gs-quant
- **解决什么问题**：高盛开源的量化金融 Python 工具包，覆盖衍生品、风控、交易策略。
- **为什么值得关注**：机构级工具包，7d 涨星 702，适合学习机构量化工程实践。
- **技术栈/架构亮点**：Python + Apache-2.0；衍生品定价、风险管理、策略模块。
- **是否适合借鉴**：适合借鉴其风控与衍生品建模思路，用于企业级量化研究。
- **可能风险**：部分功能可能依赖高盛服务；学习成本高。

### 3.8 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审。
- **为什么值得关注**：24h 涨星 93，7d 涨星 241，定位 AI 治理/安全，与金融 Agent 合规需求高度契合。
- **技术栈/架构亮点**：Python + Apache-2.0；对齐评估、幻觉检测、提示注入检测、ISO 42001/NIST AI RMF 对齐。
- **是否适合借鉴**：非常适合借鉴到金融 Agent 的合规审计与风控流程。
- **可能风险**：审计框架本身依赖 LLM，存在误判可能。

### 3.9 KareemJandali/itchbook
- **解决什么问题**：NASDAQ ITCH 5.0 限价订单簿重建、匹配引擎与队列感知回测。
- **为什么值得关注**：24h 涨星 77，项目极新但方向专业，是订单簿级回测基础设施的稀缺样本。
- **技术栈/架构亮点**：C++20 + MIT；订单簿重建、匹配引擎、队列感知回测。
- **是否适合借鉴**：适合借鉴其订单簿重建与队列建模思路，用于高频/市场微观结构研究。
- **可能风险**：项目极新，star 基数低，维护活跃度未知。

### 3.10 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作完成投研与交易决策。
- **为什么值得关注**：总 star 6.3 万，是 AI 交易 Agent 方向的经典参考项目。
- **技术栈/架构亮点**：Python + MIT；多角色 Agent 模拟。
- **是否适合借鉴**：适合借鉴其 Agent 角色设计与决策流程。
- **可能风险**：研究/教学属性强，策略过拟合风险高。

## 4. 趋势归纳

- **技术趋势**：
  - Rust 在交易基础设施中持续渗透（nautilus_trader、turbovec、itchbook）。
  - LLM 上下文工程成为 Agent 基础设施热点（headroom、planning-with-files、ruflo）。
  - MCP 成为 Agent 工具接入事实标准（OpenBot、Vibe-Trading、QuantDinger、awesome-mcp-servers）。

- **产品趋势**：
  - “AI 投研工作台”产品化：daily_stock_analysis、tick-stock-panel、ai-berkshire 均以“数据 + LLM + 看板/推送”形态出现。
  - A 股本地化数据工具链独立成赛道：a-stock-data、tick-stock-panel 强调零鉴权、多源数据、自托管。

- **量化/交易策略趋势**：
  - 从单一策略 bot 转向多 Agent 投研决策框架。
  - 订单簿级回测与市场微观结构研究开始受到关注（itchbook、nautilus_trader）。

- **AI Agent 与自动化交易结合趋势**：
  - Agent 治理、审计、可观测性成为交易 Agent 落地的关键配套（iFixAi、langfuse、OpenBot）。
  - “研究 Agent”与“执行 Agent”分离的趋势明显，执行层仍以传统交易引擎为主。

- **值得后续做原型验证的方向**：
  - LLM 投研 Agent + 确定性回测引擎的混合架构。
  - 基于 MCP 的金融数据工具标准化。
  - Agent 动作审计与合规日志系统。
  - A 股数据管道 + DuckDB/Polars 的轻量级量化工作台。

## 5. 今日灵感清单

1. **MVP：LLM 投研流水线**：参考 TradingAgents + daily_stock_analysis，用 Codex/Agent 自动生成“数据采集 → 多角色分析 → 决策看板”的最小闭环，仅做研究，不接实盘。
2. **调研：MCP 金融数据工具标准化**：调研 awesome-mcp-servers 中金融相关 MCP server，评估能否统一行情、新闻、基本面数据接口。
3. **Demo：Agent 动作审计系统**：参考 iFixAi + OpenBot，为内部 Agent 增加动作前决策记录与动作后审计日志，验证合规可行性。
4. **原型：订单簿重建回测**：参考 itchbook，用 C++/Rust 实现简化版订单簿重建与队列回测，验证市场微观结构研究可行性。
5. **调研：LLM 上下文压缩**：评估 headroom 在金融研报、行情 JSON 场景下的压缩率与信息保真度。
6. **MVP：A 股数据管道**：参考 a-stock-data + tick-stock-panel，用 DuckDB + Polars 构建零鉴权 A 股数据管道，供 Agent 调用。
7. **Demo：多 Agent 价值投资研究**：参考 ai-berkshire，用 Claude Code/Codex 复现“多大师方法论 + 对抗式分析”的研究框架。
8. **调研：Rust 交易引擎架构**：深入 nautilus_trader 的事件驱动与确定性回测设计，评估自建交易系统的可行性。
9. **Watchlist：OpenBot、iFixAi、headroom**：三者代表 Agent 治理、审计、上下文工程三个关键方向，值得持续跟踪。
10. **验证：Agent 规划持久化**：参考 planning-with-files，为长时运行投研 Agent 增加崩溃恢复与上下文防衰减机制。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | LLM 多智能体交易框架标杆，持续高热 |
| nautechsystems/nautilus_trader | 生产级 Rust 交易引擎，架构参考价值高 |
| CopilotKit/OpenBot | Agent 治理 + 浏览器自动化新方向，增长极快 |
| headroomlabs-ai/headroom | LLM 上下文压缩，降低 Agent 成本的关键技术 |
| ifixai-ai/iFixAi | AI Agent 审计/合规，金融 Agent 落地必备 |
| goldmansachs/gs-quant | 机构级量化工具包，风控与衍生品建模参考 |
| HKUDS/Vibe-Trading | 学术背景的 MCP + 多 Agent 交易研究 |
| KareemJandali/itchbook | 订单簿级回测稀缺样本，市场微观结构方向 |
| ZhuLinsen/daily_stock_analysis | A 股 LLM 投研流水线代表 |
| simonlin1212/a-stock-data | A 股数据工具链，Agent 数据层参考 |
| langfuse/langfuse | LLM 可观测性，交易 Agent 监控配套 |
| OpenBB-finance/OpenBB | 开放金融数据平台，数据层参考 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-08-26）和 `baseline_7d`（2026-08-20），但部分项目（如 tick-stock-panel、awesome-public-datasets、Polymarket-Telegram-Bot）的 `star_delta_7d` 为 null，说明 7 日基线数据缺失或项目在基线日期不存在。
- **采集失败**：未发现明确采集失败标记，但 `star_delta_30d` 对所有项目均为 null，说明 30 日基线未采集。
- **样本偏差**：候选列表包含大量“awesome-list”类项目（public-apis、free-for-dev、awesome-python、awesome-go 等），这些项目因关键词误匹配进入榜单，与金融/量化/交易主题相关性低，导致真实交易/量化项目占比被稀释。分析时应重点过滤此类噪声。
- **语言字段**：部分项目 `language` 为 null，无法判断技术栈，相关分析需谨慎。
- **风险标记**：多个项目带有 `crypto_related`、`trading_bot`、`leverage_or_grid_related` 等标记，但标记本身来自不可信数据，仅作为风险提示参考，不作为事实依据。
