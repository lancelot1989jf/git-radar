# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-27

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能包与审计治理**：Claude/Codex 技能包（UI/UX、安全审计、交易分析）成为涨星主力，反映“用技能包封装领域知识”的工程范式正在爆发。
  2. **LLM 驱动的股票/交易分析系统**：`daily_stock_analysis`、`Vibe-Trading`、`TradingAgents` 等项目持续高增长，多源行情 + LLM 决策看板 + 自动推送成为热门产品形态。
  3. **本地优先的 AI 推理与 Agent 编排**：`colibri`、`magnitude`、`ruflo`、`Orkas` 等项目强调本地推理、多 Agent 协作、桌面端编排，显示“去中心化/本地化 AI 工作台”趋势。

- **是否出现新趋势**：出现。**“AI Agent 技能包（Skills）”** 成为跨领域通用增长引擎，从 UI 设计、安全审计到交易分析都在以“技能包”形式分发；同时 **AI Agent 审计/治理**（iFixAi）开始独立成类，值得关注。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“自托管 + DuckDB/Polars + FastAPI + React + LLM 策略定制”组合，都是可复刻的轻量级量化工作台范式。

- **是否有明显骗局、过度营销或高风险项目**：本次候选列表中未发现明显骗局，但存在**大量误匹配项目**（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-go` 等被关键词误命中为 trading_bot/crypto_trading）。高风险项目集中在 **Solana 交易 API/路由**（`solana-swap-api`，风险等级“高”）和 **Telegram 交易信号/机器人导航**（`awesome-telegram`、`voice-notes-pipeline`）等方向，需警惕 API key 泄露与信号欺诈风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 155316 | +520 | +3067 | Python | AI 技能包/UI | 多平台 UI/UX 设计智能技能包 | 高：技能包封装领域知识 | 低 |
| 2 | elementalsouls/Claude-BugHunter | 26498 | +1332 | +11742 | Python | AI 安全/审计 | 85 个漏洞猎捕技能 + 681 披露报告模式 | 高：Agent 安全审计框架 | 低 |
| 3 | GoogleChrome/modern-web-guidance | 27150 | +308 | +3074 | 无 | Web 最佳实践 | 让编码 Agent 保持最新 Web 实践 | 中：Agent 知识更新机制 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 341210 | +298 | +2154 | 无 | 自托管清单 | 自托管网络服务清单 | 低：误匹配 | 中 |
| 5 | codecrafters-io/build-your-own-x | 566063 | +210 | +1867 | Markdown | 教程清单 | 从零复刻技术项目教程 | 低：误匹配 | 中 |
| 6 | GoogleChrome/modern-web-guidance-src | 11514 | +179 | +1901 | TypeScript | Web 最佳实践 | 同上源码版 | 中：Agent 知识更新机制 | 低 |
| 7 | vinta/awesome-python | 337623 | +201 | +1507 | Python | Python 清单 | Python 工具精选清单 | 低：误匹配 | 低 |
| 8 | ZhuLinsen/daily_stock_analysis | 75075 | +146 | +1490 | Python | AI 交易/量化 | LLM 多市场股票分析系统 | 高：多源数据 + LLM 看板 | 低 |
| 9 | public-apis/public-apis | 501865 | +141 | +1324 | Python | API 清单 | 免费 API 合集 | 低：误匹配 | 中 |
| 10 | avelino/awesome-go | 196424 | +191 | +1342 | Go | Go 清单 | Go 框架/库精选 | 低：误匹配 | 中 |
| 11 | JustVugg/colibri | 53795 | +160 | +1263 | C | 推理引擎 | 分层 MoE 推理引擎（GPU/RAM/NVMe） | 高：本地推理架构 | 低 |
| 12 | ifixai-ai/iFixAi | 47779 | +236 | +1273 | Python | AI 审计/治理 | AI Agent 独立审计，120 秒回答“Agent 是否在做该做的事” | 高：Agent 治理/风控 | 低 |
| 13 | nexu-io/open-design | 109931 | +201 | +1196 | TypeScript | AI 设计工作台 | 协作式 AI 设计 Agent 工作区 | 中：多 Agent 协作 UI | 低 |
| 14 | tradermonty/claude-trading-skills | 8769 | +115 | +1289 | Python | 交易技能包 | 股票投资者/交易员的 Claude 技能包 | 高：交易分析技能化 | 低 |
| 15 | VoltAgent/awesome-design-md | 129488 | +182 | +1024 | 无 | 设计系统清单 | DESIGN.md 品牌设计系统合集 | 中：设计系统驱动 Agent | 中 |
| 16 | Jakeschincariol/day-trader-skill | 9938 | +116 | +982 | Python | 日内交易技能包 | 11 个日内交易 Claude 技能 | 高：交易决策流程化 | 低 |
| 17 | perixtar/Tech-OA-Interview-Questions | 7096 | +178 | +961 | Python | 面试题库 | 科技公司 OA/面试题 | 低：误匹配 | 低 |
| 18 | ripienaar/free-for-dev | 143976 | +184 | +685 | HTML | 免费资源清单 | SaaS/PaaS/IaaS 免费层清单 | 低：误匹配 | 低 |
| 19 | CopilotKit/OpenBot | 13843 | +131 | +750 | TypeScript | AI Bot 框架 | 开源可自托管 AI Bot 替代品 | 高：Agent 编排框架 | 中 |
| 20 | jaywcjlove/awesome-mac | 119714 | +95 | +710 | Swift | macOS 软件清单 | macOS 软件精选 | 低：误匹配 | 低 |
| 21 | headroomlabs-ai/headroom | 81035 | +69 | +809 | Python | Token 压缩 | 压缩工具输出/日志/RAG 块，节省 token | 高：上下文工程 | 低 |
| 22 | TauricResearch/TradingAgents | 123971 | +92 | +644 | TypeScript | AI 交易/多 Agent | 面向 Agentic 金融研究的多 Agent 框架 | 高：多 Agent 金融研究 | 低 |
| 23 | punkpeye/awesome-remote-mcp-servers | 4305 | +86 | +604 | 无 | MCP 清单 | 远程 MCP 服务器合集 | 中：MCP 生态观察 | 中 |
| 24 | HKUDS/Vibe-Trading | 39114 | +84 | +483 | Python | AI 交易/回测 | “Vibe-Trading”个人交易 Agent | 高：LLM 交易 Agent 范式 | 低 |
| 25 | ashishpatel26/500-AI-Agents-Projects | 40829 | +38 | +684 | Python | AI Agent 清单 | 500 个 AI Agent 用例合集 | 中：Agent 用例灵感 | 中 |
| 26 | hesreallyhim/awesome-claude-code | 58958 | +59 | +473 | Python | Claude Code 清单 | Claude Code 资源精选 | 中：Agent 工具生态 | 低 |
| 27 | kaankiziltug/logo-design-skill | 7957 | +54 | +522 | HTML | 设计技能包 | Logo 设计技能包 | 低：误匹配 | 低 |
| 28 | ruvnet/ruflo | 82572 | +47 | +390 | TypeScript | Agent 编排 | 多玩家 swarm 部署与协调 | 高：多 Agent 编排 | 低 |
| 29 | sickn33/agentic-awesome-skills | 50463 | +41 | +398 | Python | 技能包合集 | 3000+ 可复用 AI Agent 技能 | 中：技能包生态 | 低 |
| 30 | suoha888/Trader-Archives | 538 | +144 | +282 | HTML | 交易员推文归档 | 推特实战交易员推文收录 | 中：交易认知数据湖 | 中 |
| 31 | awesomedata/awesome-public-datasets | 80544 | +24 | +318 | 无 | 数据集清单 | 高质量公开数据集 | 中：数据源灵感 | 中 |
| 32 | garrytan/gbrain | 33672 | +25 | +318 | TypeScript | Agent 大脑 | Garry 的 OpenClaw/Hermes Agent Brain | 中：Agent 架构参考 | 低 |
| 33 | magnitudedev/magnitude | 9118 | +120 | 信息不足 | Rust | 推理引擎 | 跨 GPU/RAM/SSD 的推理引擎 | 高：本地推理架构 | 低 |
| 34 | punkpeye/awesome-mcp-servers | 98587 | +27 | +251 | 无 | MCP 清单 | MCP 服务器合集 | 中：MCP 生态观察 | 低 |
| 35 | TGrpg/awesome-telegram | 2086 | +50 | +295 | JavaScript | Telegram 导航 | Telegram 频道/群组/机器人导航 | 低：信号风险 | 中 |
| 36 | Orkas-AI/Orkas | 8135 | +283 | -1356 | JavaScript | 桌面 Agent 团队 | 本地优先 AI 团队桌面应用 | 高：本地多 Agent 编排 | 低 |
| 37 | FareedKhan-dev/kimi-k3-in-c | 12762 | +39 | +248 | C | 推理引擎 | 单 CPU 8.24GB 运行 2.78T 参数模型 | 高：极致推理优化 | 低 |
| 38 | vybenetwork/solana-swap-api | 3089 | +141 | +368 | JavaScript | Solana 交易 API | Solana Swap API 与路由 | 中：DEX 路由参考 | 高 |
| 39 | rust-unofficial/awesome-rust | 60886 | +32 | +192 | Rust | Rust 清单 | Rust 代码/资源精选 | 低：误匹配 | 中 |
| 40 | openbq-org/OpenBB | 75810 | +25 | +199 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高：金融数据基础设施 | 中 |
| 41 | shy3130/tick-stock-panel | 8364 | +22 | +241 | Python | A 股量化工作台 | 自托管 A 股策略+监控+回测工作台 | 高：轻量量化工作台 | 低 |
| 42 | AhmadHassan-BTed/Turnitout-Humanizer | 12710 | +21 | +216 | HTML | 文本工具 | 抄袭移除/相似度规避工具 | 低：误匹配/伦理风险 | 中 |
| 43 | fffaraz/awesome-cpp | 74665 | +16 | +127 | 无 | C++ 清单 | C/C++ 框架/库精选 | 低：误匹配 | 低 |
| 44 | hazelthepoetry/metaid-file-system | 148 | +148 | 信息不足 | HTML | 链上存储 | MetaID 链上存储与索引 | 低：样本过小 | 低 |
| 45 | code-yeongyu/oh-my-openagent | 71161 | +11 | +124 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中：Agent 编排参考 | 低 |
| 46 | GhufranNaseer/alpaca-0dte-terminal | 147 | +147 | 信息不足 | HTML | 期权终端 | Alpaca 0DTE 期权分析终端 | 中：期权分析 UI | 低 |
| 47 | Developer-Y/cs-video-courses | 85009 | +10 | +108 | 无 | 课程清单 | CS 视频课程清单 | 低：误匹配 | 中 |
| 48 | josephmisiti/awesome-machine-learning | 74927 | +5 | +61 | Python | ML 清单 | ML 框架/库精选 | 低：误匹配 | 低 |
| 49 | virattt/ai-hedge-fund | 64878 | +8 | +95 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高：多 Agent 投研流程 | 低 |
| 50 | vuejs/awesome-vue | 73458 | +1 | -11 | 无 | Vue 清单 | Vue 资源精选 | 低：误匹配 | 低 |
| 51 | gda394995-design/voice-notes-pipeline | 151 | +151 | 信息不足 | HTML | 语音信号管道 | 语音笔记到信号/任务/日历同步 | 低：样本过小 | 中 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：将多源行情、实时新闻、LLM 分析与决策看板整合为多市场股票智能分析系统，支持零成本定时运行与自动推送。
- **为什么值得关注**：7 日涨星 +1490，总 star 75k+，是“LLM + 多源数据 + 决策看板”这一产品形态的典型代表，且明确面向 A 股等多市场。
- **技术栈/架构亮点**：Python + LLM 驱动；多源行情与新闻聚合；决策看板 + 自动推送；强调“零成本定时运行”，暗示轻量级、可自托管的架构设计。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。其“数据聚合 → LLM 分析 → 看板展示 → 自动推送”的流水线可作为企业级投研 Agent 的 MVP 蓝本。
- **可能风险**：LLM 生成内容可能存在幻觉，需人工校验；行情数据源合规性需确认；自动推送若接入实盘信号可能引发误导。

### 3.2 TauricResearch/TradingAgents
- **解决什么问题**：面向 Agentic 金融研究的多 Agent 框架，将金融研究流程拆分为多个协作 Agent。
- **为什么值得关注**：总 star 123k+，是“多 Agent 金融研究”方向的标杆项目，持续有 push。
- **技术栈/架构亮点**：TypeScript 实现；多 Agent 协作；LLM 驱动；Apache-2.0 许可。
- **是否适合借鉴**：非常适合。其多 Agent 角色分工（如分析师、交易员、风控等）可直接映射到企业级投研 Agent 框架。
- **可能风险**：研究工具属性强，策略有效性未经验证；多 Agent 协调成本高；需注意 LLM 输出稳定性。

### 3.3 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 与算法交易、回测、组合优化结合。
- **为什么值得关注**：HKUDS 出品，总 star 39k+，7 日 +483，是学术机构在 LLM 交易 Agent 方向的代表性开源项目。
- **技术栈/架构亮点**：Python；集成 MCP、多 Agent、回测、量化金融模块；MIT 许可。
- **是否适合借鉴**：适合作为“LLM 交易 Agent”的研究原型参考，尤其是 MCP 集成与多 Agent 设计。
- **可能风险**：研究工具属性，回测结果可能存在过拟合；不应直接用于实盘。

### 3.4 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，120 秒内给出结论。
- **为什么值得关注**：24h 涨星 +236，总 star 47k+，是“AI Agent 治理/审计”这一新兴方向的代表。
- **技术栈/架构亮点**：Python；覆盖 AI 对齐、幻觉检测、提示注入、ISO 42001、NIST AI RMF、OWASP LLM 等标准；CLI 工具。
- **是否适合借鉴**：非常适合。在金融/交易 Agent 场景中，审计与风控是刚需，可借鉴其评估框架构建交易 Agent 的合规审计层。
- **可能风险**：审计标准覆盖广但深度未知；对金融交易场景的适配性需验证。

### 3.5 tradermonty/claude-trading-skills 与 Jakeschincariol/day-trader-skill
- **解决什么问题**：将市场分析、技术图表、经济日历、选股器、交易策略开发、日内交易决策流程封装为 Claude Code 技能包。
- **为什么值得关注**：两者 7 日涨星均超 +980，反映“交易分析技能化”趋势，且创建时间短、增长快。
- **技术栈/架构亮点**：Python；以 Claude Skills 形式分发；覆盖扫描、新闻跟踪、进出场时机、结果回放等流程。
- **是否适合借鉴**：适合。可将交易分析流程标准化为技能包，供 Codex/Claude 等 Agent 调用，快速搭建投研助手。
- **可能风险**：技能包内容质量参差；交易信号类技能若被误用可能导致资金风险；需注意 API key 安全。

### 3.6 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 策略定制与个股分析。
- **为什么值得关注**：技术栈现代（DuckDB、Polars、FastAPI、React），是轻量级量化工作台的优秀参考。
- **技术栈/架构亮点**：Python + DuckDB + Polars + FastAPI + React；LLM 驱动策略定制；支持第三方数据源接入。
- **是否适合借鉴**：非常适合。可作为“本地优先量化工作台”的工程蓝本，尤其适合中小团队快速搭建内部研究工具。
- **可能风险**：A 股数据合规性；LLM 策略生成可能存在过拟合；自托管需注意数据安全。

### 3.7 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，将投研流程拆分为多个 AI Agent。
- **为什么值得关注**：总 star 64k+，是“AI 对冲基金”概念的开源标杆，长期受关注。
- **技术栈/架构亮点**：Python；多 Agent 模拟投研团队；MIT 许可。
- **是否适合借鉴**：适合作为多 Agent 投研流程的教学与原型参考。
- **可能风险**：模拟性质，策略有效性未经验证；不应直接用于实盘。

### 3.8 JustVugg/colibri 与 magnitudedev/magnitude
- **解决什么问题**：将大型 MoE 模型分层部署在 GPU/RAM/NVMe 上，实现消费级硬件上的本地推理。
- **为什么值得关注**：colibri 总 star 53k+，magnitude 24h 涨星 +120，反映“本地优先 AI 推理”趋势。
- **技术栈/架构亮点**：colibri 用 C 实现，支持 CUDA/Vulkan；magnitude 用 Rust，跨 Apple Silicon/NVIDIA/AMD/Intel。
- **是否适合借鉴**：适合。在金融数据敏感场景下，本地推理可降低数据外泄风险，值得关注其分层推理架构。
- **可能风险**：推理性能与精度需验证；与交易系统的集成成本较高。

### 3.9 ruvnet/ruflo 与 Orkas-AI/Orkas
- **解决什么问题**：多 Agent 编排与本地优先 AI 团队协作。
- **为什么值得关注**：ruflo 总 star 82k+，Orkas 24h 涨星 +283（但 7d 为 -1356，需注意波动），反映 Agent 编排框架的活跃竞争。
- **技术栈/架构亮点**：ruflo 用 TypeScript，支持 swarm、自适应记忆、向量 RAG、MCP；Orkas 用 JavaScript，本地优先桌面应用，协调 16 个内置专家 Agent。
- **是否适合借鉴**：适合。可借鉴其多 Agent 协调、记忆管理、本地优先设计，构建企业级 Agent 工作台。
- **可能风险**：Orkas 7d 涨星为负，需关注维护活跃度；多 Agent 系统复杂度高，调试与治理成本大。

### 3.10 vybenetwork/solana-swap-api
- **解决什么问题**：Solana 链上 Swap API 与路由，集成 Jupiter、Raydium、Meteora、PumpFun 等 DEX。
- **为什么值得关注**：24h 涨星 +141，是候选列表中少数的链上交易基础设施项目。
- **技术栈/架构亮点**：JavaScript/TypeScript；DEX 聚合与路由；Web3。
- **是否适合借鉴**：可借鉴其 DEX 路由与聚合架构，但风险等级为“高”。
- **可能风险**：加密资产交易风险高；API key 与私钥安全；智能合约风险；合规风险。

## 4. 趋势归纳

- **技术趋势**：
  - **AI Agent 技能包（Skills）成为知识分发的主流形态**：UI 设计、安全审计、交易分析等领域均在以技能包形式封装专业知识。
  - **本地优先 AI 推理与 Agent 编排**：colibri、magnitude、kimi-k3-in-c、Orkas、ruflo 等项目强调本地推理、消费级硬件部署、多 Agent 协作。
  - **上下文工程与 Token 优化**：headroom 等项目聚焦压缩工具输出与 RAG 块，降低 LLM 成本。
  - **MCP 生态持续扩张**：awesome-mcp-servers、awesome-remote-mcp-servers 等清单项目活跃，MCP 成为 Agent 工具连接的事实标准。

- **产品趋势**：
  - **“LLM + 多源数据 + 决策看板 + 自动推送”成为金融分析产品标配**：daily_stock_analysis、tick-stock-panel 等均采用此形态。
  - **AI Agent 审计与治理产品化**：iFixAi 将 Agent 审计打包为 120 秒可用的 CLI 工具，显示治理需求正在产品化。
  - **自托管/本地优先工作台**：tick-stock-panel、Orkas、OpenBot 等强调自托管与本地优先，契合金融数据敏感场景。

- **量化/交易策略趋势**：
  - **LLM 驱动的策略定制与个股分析**：tick-stock-panel、daily_stock_analysis 将 LLM 用于策略生成与个股分析。
  - **多 Agent 投研流程**：TradingAgents、ai-hedge-fund、Vibe-Trading 将投研流程拆分为多 Agent 协作。
  - **交易分析技能化**：claude-trading-skills、day-trader-skill 将交易决策流程封装为可复用技能。

- **AI Agent 与自动化交易结合趋势**：
  - **从“单 Agent 交易”向“多 Agent 投研 + 审计 + 治理”演进**：TradingAgents、iFixAi、Vibe-Trading 等显示 Agent 交易正在从单一决策向协作、审计、治理全流程扩展。
  - **MCP 成为交易 Agent 的工具连接层**：Vibe-Trading、ruflo 等项目集成 MCP，显示交易 Agent 的工具生态正在标准化。

- **值得后续做原型验证的方向**：
  - 基于技能包的投研助手 MVP。
  - 本地优先的量化研究工作台（DuckDB + Polars + FastAPI + React + LLM）。
  - 交易 Agent 的审计与风控层。
  - 多 Agent 投研流程的编排框架。

## 5. 今日灵感清单

1. **MVP：本地优先的 A 股/美股投研看板**：参考 `daily_stock_analysis` 与 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭建自托管投研看板，集成 LLM 生成每日摘要与自动推送。
2. **MVP：交易分析技能包**：参考 `claude-trading-skills` 与 `day-trader-skill`，将“数据获取 → 技术分析 → 新闻扫描 → 决策建议”封装为 Claude/Codex 技能包，供 Agent 调用。
3. **调研：AI Agent 审计框架**：深入研究 `iFixAi` 的审计维度（幻觉检测、提示注入、ISO 42001、NIST AI RMF），评估如何将其适配到金融交易 Agent 的合规审计。
4. **调研：本地推理引擎在金融数据敏感场景的可行性**：关注 `colibri`、`magnitude`、`kimi-k3-in-c` 的分层推理架构，评估在本地运行 LLM 进行研报分析的成本与性能。
5. **Demo：多 Agent 投研流程编排**：参考 `TradingAgents` 与 `ai-hedge-fund`，用 Codex/Claude 复现一个“分析师 → 交易员 → 风控”多 Agent 投研 demo。
6. **调研：MCP 在交易数据接入中的应用**：浏览 `awesome-mcp-servers` 与 `awesome-remote-mcp-servers`，筛选适合金融数据接入的 MCP 服务器，评估构建交易 Agent 工具层的可行性。
7. **MVP：Token 优化代理**：参考 `headroom`，为投研 Agent 构建一个输出压缩代理，降低 LLM 调用成本。
8. **Watchlist：OpenBB**：作为金融数据基础设施，关注其数据源覆盖与 AI Agent 集成能力，评估作为投研数据层的可行性。
9. **调研：DEX 聚合路由架构**：参考 `solana-swap-api` 的 DEX 聚合与路由设计，但仅做技术调研，不直接用于实盘交易。
10. **Demo：Agent 知识更新机制**：参考 `GoogleChrome/modern-web-guidance`，为投研 Agent 构建“最佳实践知识库 + 定期更新”机制，保持 Agent 知识新鲜度。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | LLM 多市场股票分析系统，产品形态成熟，适合作为投研看板 MVP 蓝本 |
| TauricResearch/TradingAgents | 多 Agent 金融研究标杆，适合研究 Agent 角色分工与协作 |
| HKUDS/Vibe-Trading | 学术机构 LLM 交易 Agent 代表，适合跟踪 MCP 集成与多 Agent 设计 |
| ifixai-ai/iFixAi | AI Agent 审计/治理新兴方向，适合跟踪金融 Agent 合规审计 |
| shy3130/tick-stock-panel | 轻量级量化工作台，技术栈现代，适合作为自托管研究工具参考 |
| virattt/ai-hedge-fund | AI 对冲基金概念标杆，适合教学与原型参考 |
| openbq-org/OpenBB | 金融数据基础设施，适合作为投研数据层候选 |
| tradermonty/claude-trading-skills | 交易分析技能包代表，适合跟踪交易分析技能化趋势 |
| JustVugg/colibri | 本地分层推理引擎，适合跟踪本地优先 AI 推理趋势 |
| ruvnet/ruflo | 多 Agent 编排框架，适合跟踪 Agent 编排与记忆管理 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-11-26）与 `baseline_7d`（2026-11-20），但部分项目（如 `magnitudedev/magnitude`、`hazelthepoetry/metaid-file-system`、`GhufranNaseer/alpaca-0dte-terminal`、`gda394995-design/voice-notes-pipeline`）的 `star_delta_7d` 为 `null`，可能因项目创建时间晚于 7 日基线或基线数据缺失，导致 7 日涨星信息不足。
- **采集失败**：未发现明确采集失败，但 `star_delta_30d` 对所有项目均为 `null`，说明 30 日基线数据缺失。
- **样本偏差**：本次候选列表存在**显著误匹配**，大量项目（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-go`、`awesome-python`、`awesome-mac`、`cs-video-courses` 等）因关键词命中被错误归类为 trading_bot/crypto_trading/quant_research，实际与金融/量化/交易无关。这导致 Top 表中“主题/分类”字段的准确性下降，分析时应以项目实际描述与 topics 为准。
- **风险等级偏差**：部分误匹配项目（如 `awesome-selfhosted`、`build-your-own-x`）因命中 `trading_bot` 关键词被标记为“中”风险，但实际风险较低；反之，部分真实交易基础设施项目（如 `solana-swap-api`）风险等级为“高”，需重点关注。
- **样本量**：本次候选共 51 个项目，覆盖 AI 技能包、Agent 编排、量化研究、交易基础设施、数据清单等多个方向，但金融/量化/交易核心项目占比有限，趋势判断需结合更广泛数据源验证。
