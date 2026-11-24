# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-23

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent Skills 生态爆发**：Claude Code / Codex / Cursor 的“技能包”成为新的分发形态，从 UI 设计、安全测试到交易分析都在被封装为可复用 skill。
  2. **LLM 驱动交易研究工具链**：多个项目将 LLM 与回测、新闻情绪、多智能体决策结合，形成“研究型交易 Agent”而非直接下单 bot。
  3. **本地优先与低资源推理**：MoE 模型分层推理、纯 C 推理引擎等项目显示“在自有硬件上跑前沿模型”成为热点，对金融数据隐私场景有借鉴意义。

- **是否出现新趋势**：出现。AI Agent 的“技能包化”与“审计/治理化”是本次样本中最明显的新趋势；同时，交易类项目开始强调“防未来函数”“point-in-time 回测”等研究严谨性。

- **是否出现值得复刻/参考的工程架构**：是。`risk-aware-trading-agents` 的 point-in-time 新闻回测与 look-ahead 检查、`colibri` 的 GPU/RAM/NVMe 分层 MoE 推理、`headroom` 的 LLM 上下文压缩代理，均具备工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：有。`raydium-meteora-sniper-bot-x64` 为 1 天内新建、0 fork、预编译 Windows x64 二进制、Solana 抢跑/狙击 bot，风险标记为“高”，应视为高风险项目，不建议运行。另有 `Turnitout-Humanizer` 属于学术作弊工具，与金融无关且存在合规风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 153523 | +520 | +2929 | Python | fintech_product | AI 驱动的跨平台 UI/UX 设计技能包 | 中 | 低 |
| 2 | elementalsouls/Claude-BugHunter | 20487 | +2018 | +12665 | Python | fintech_product | Claude Code 漏洞挖掘与红队技能包 | 高 | 低 |
| 3 | GoogleChrome/modern-web-guidance | 25696 | +479 | +4447 | 无 | risk_management | 为编码 Agent 提供最新 Web 最佳实践 | 中 | 低 |
| 4 | GoogleChrome/modern-web-guidance-src | 10671 | +357 | +2497 | TypeScript | risk_management | 上述项目的源码版 | 中 | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 340014 | +357 | +2176 | 无 | trading_bot | 自托管网络服务与 Web 应用清单 | 低 | 中 |
| 6 | codecrafters-io/build-your-own-x | 565132 | +301 | +1880 | Markdown | trading_bot | 从零重建技术的教程合集 | 低 | 中 |
| 7 | JustVugg/colibri | 53219 | +221 | +1589 | C | quant_research | MoE 模型分层推理引擎（GPU/RAM/NVMe） | 高 | 低 |
| 8 | public-apis/public-apis | 501128 | +208 | +1436 | Python | crypto_trading/quant | 免费 API 清单 | 中 | 中 |
| 9 | vinta/awesome-python | 336800 | +245 | +1471 | Python | quant_research | Python 工具精选清单 | 低 | 低 |
| 10 | tradermonty/claude-trading-skills | 8191 | +341 | +1586 | Python | backtesting/risk | Claude Code 股票交易分析技能包 | 高 | 低 |
| 11 | avelino/awesome-go | 195679 | +189 | +1321 | Go | backtesting/crypto | Go 框架与库精选清单 | 低 | 中 |
| 12 | nexu-io/open-design | 109247 | +192 | +1248 | TypeScript | fintech_product | 协作式 AI 设计 Agent 工作台 | 中 | 低 |
| 13 | ZhuLinsen/daily_stock_analysis | 74171 | +383 | +1238 | Python | ai_trading/quant | LLM 驱动多市场股票分析系统 | 高 | 低 |
| 14 | Jakeschincariol/day-trader-skill | 9381 | +155 | +1127 | Python | backtesting/risk | 11 个日内交易 Claude 技能 | 高 | 低 |
| 15 | VoltAgent/awesome-design-md | 128854 | +162 | +981 | 无 | crypto_trading/fintech | 品牌设计系统 DESIGN.md 合集 | 低 | 中 |
| 16 | ifixai-ai/iFixAi | 47068 | +173 | +882 | Python | ai_trading/risk | AI Agent 独立审计工具 | 高 | 低 |
| 17 | headroomlabs-ai/headroom | 80698 | +117 | +829 | Python | ai_trading/risk | LLM 工具输出与日志压缩 | 高 | 低 |
| 18 | TauricResearch/TradingAgents | 123655 | +120 | +765 | Python | ai_trading/backtesting | 面向 Agentic 金融研究的多智能体框架 | 高 | 低 |
| 19 | CopilotKit/OpenBot | 13350 | +109 | +698 | TypeScript | fintech_product/trading_bot | 开源可自托管 AI bot 替代方案 | 中 | 中 |
| 20 | ripienaar/free-for-dev | 143521 | +114 | +509 | HTML | fintech_product | 开发者免费资源清单 | 低 | 低 |
| 21 | ashishpatel26/500-AI-Agents-Projects | 40676 | +87 | +637 | Python | risk_management/trading_bot | 500 个 AI Agent 用例合集 | 中 | 中 |
| 22 | punkpeye/awesome-remote-mcp-servers | 3931 | +96 | +554 | 无 | ai_trading/crypto | 远程 MCP 服务器清单 | 中 | 中 |
| 23 | punkpeye/awesome-mcp-servers | 98452 | +54 | +661 | 无 | fintech_product | MCP 服务器清单 | 中 | 低 |
| 24 | jaywcjlove/awesome-mac | 119237 | +66 | +526 | Swift | trading_infra | macOS 软件精选清单 | 低 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 58706 | +76 | +510 | Python | ai_trading/quant | Claude Code 资源精选清单 | 中 | 低 |
| 26 | kaankiziltug/logo-design-skill | 7612 | +68 | +493 | HTML | fintech_product | AI Agent Logo 设计技能包 | 低 | 低 |
| 27 | microsoft/BitNet | 42453 | +22 | +862 | C++ | ai_trading/quant | 1-bit LLM 官方推理框架 | 高 | 低 |
| 28 | sickn33/agentic-awesome-skills | 50236 | +63 | +399 | Python | backtesting | 3000+ 可复用 AI Agent 技能库 | 中 | 低 |
| 29 | ruvnet/ruflo | 82346 | +50 | +439 | TypeScript | ai_trading/backtesting | 多智能体 swarm 编排框架 | 中 | 低 |
| 30 | garrytan/gbrain | 33512 | +66 | +329 | TypeScript | fintech_product | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 31 | awesomedata/awesome-public-datasets | 80336 | +90 | +159 | 无 | crypto_trading | 高质量公开数据集清单 | 中 | 中 |
| 32 | HKUDS/Vibe-Trading | 38757 | +39 | +353 | Python | ai_trading/backtesting | “Vibe-Trading”个人交易 Agent | 高 | 低 |
| 33 | FareedKhan-dev/kimi-k3-in-c | 12627 | +39 | +399 | C | ai_trading/quant | 纯 C99 单 CPU 推理 Kimi K3 | 高 | 低 |
| 34 | bangtutorial/bang-motion | 2983 | +44 | +530 | HTML | fintech_product | 浏览器动效设计 Agent 技能 | 低 | 低 |
| 35 | bex-co/beancount-io | 859 | +105 | +206 | TypeScript | fintech_product | 复式记账移动应用 | 中 | 低 |
| 36 | PurpleDoubleD/locally-uncensored | 4651 | +45 | +319 | TypeScript | ai_trading/quant | 本地 AI 桌面工作室 | 中 | 低 |
| 37 | openbq-org/OpenBB | 75692 | +40 | +209 | Python | crypto_trading/quant | 面向分析师与 Agent 的开放数据平台 | 高 | 中 |
| 38 | shy3130/tick-stock-panel | 8233 | +32 | +279 | Python | ai_trading/backtesting | A 股自托管量化工作台 | 高 | 低 |
| 39 | Hithink-Tech-Org/Financial-API | 4600 | +15 | +439 | TypeScript | data_engineering/quant | 同花顺官方 A 股金融数据服务 | 高 | 低 |
| 40 | AhmadHassan-BTed/Turnitout-Humanizer | 12598 | +37 | +239 | HTML | risk_management/trading_bot | 学术查重规避工具 | 低 | 中 |
| 41 | rust-unofficial/awesome-rust | 60774 | +30 | +177 | Rust | ai_trading/backtesting | Rust 资源精选清单 | 低 | 中 |
| 42 | paperswithbacktest/awesome-systematic-trading | 15619 | +97 | +217 | Python | backtesting/crypto | 系统化交易资源精选清单 | 高 | 中 |
| 43 | code-yeongyu/oh-my-openagent | 71094 | +26 | +135 | TypeScript | quant_research | 图工程 Agent 工具 | 低 | 低 |
| 44 | jackson-cmd/risk-aware-trading-agents | 475 | +40 | +266 | Python | ai_trading/backtesting | 防未来函数的美股 LLM 交易 Agent 榜单 | 高 | 中 |
| 45 | fffaraz/awesome-cpp | 74596 | +17 | +126 | 无 | quant_research | C/C++ 资源精选清单 | 低 | 低 |
| 46 | virattt/ai-hedge-fund | 64840 | +18 | +123 | Python | backtesting/risk | AI 对冲基金团队模拟 | 高 | 低 |
| 47 | Developer-Y/cs-video-courses | 84929 | +15 | +57 | 无 | quant_research/trading_bot | 计算机科学视频课程清单 | 低 | 中 |
| 48 | josephmisiti/awesome-machine-learning | 74903 | +13 | +60 | Python | ai_trading/fintech | 机器学习资源精选清单 | 低 | 低 |
| 49 | vuejs/awesome-vue | 73462 | -3 | -10 | 无 | quant_research | Vue.js 资源精选清单 | 低 | 低 |
| 50 | keptaduona/wickline | 192 | +110 | 信息不足 | JavaScript | backtesting/crypto | 开源多市场图表与回测应用 | 中 | 中 |
| 51 | dmitry-k-code19w1/raydium-meteora-sniper-bot-x64 | 103 | +103 | 信息不足 | Jupyter Notebook | quant_research/trading_bot | Solana Raydium/Meteora 狙击 bot | 低 | 高 |

## 3. 重点项目深度分析

### 3.1 elementalsouls/Claude-BugHunter
- **解决什么问题**：将漏洞挖掘与红队测试能力封装为 Claude Code 技能包，覆盖 24 类漏洞、681 个披露报告模式。
- **为什么值得关注**：24h 涨星 +2018、7d +12665，是本次样本中涨星最快的项目之一，说明“安全审计技能包”需求强烈。
- **技术栈/架构亮点**：84 个 skills、15 个 slash commands，将攻击矩阵与身份/基础设施攻击面结构化。
- **是否适合借鉴**：非常适合。金融科技企业可将类似思路用于交易系统安全审计、API 权限矩阵检查、智能合约漏洞扫描的 Agent 化。
- **可能风险**：技能包内容可能被滥用于未授权测试；金融场景需注意合规边界。

### 3.2 tradermonty/claude-trading-skills
- **解决什么问题**：为股票投资者和交易者提供 Claude Code 技能，覆盖市场分析、技术图表、经济日历、筛选器和策略开发。
- **为什么值得关注**：24h +341、7d +1586，在较小 star 基数上增速显著，代表“交易研究技能包”这一细分方向。
- **技术栈/架构亮点**：以 skill 形式组织交易研究工作流，而非直接执行交易。
- **是否适合借鉴**：适合。可作为企业级“研究型 Agent”的参考，将数据获取、图表生成、策略构思拆分为可审计的 skill。
- **可能风险**：研究工具定位，但若接入实盘需注意策略过拟合与信号可靠性。

### 3.3 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：74k stars、24h +383，是 A 股 AI 分析类项目的头部代表。
- **技术栈/架构亮点**：多源数据 + LLM + 定时任务 + 推送，形成闭环研究流水线。
- **是否适合借鉴**：适合。其“零成本定时运行”与“决策看板”思路可复刻到企业内部投研日报自动化。
- **可能风险**：LLM 生成的分析可能存在幻觉；新闻情绪信号需注意时点偏差。

### 3.4 TauricResearch/TradingAgents
- **解决什么问题**：面向 Agentic 金融研究的多智能体框架，模拟交易团队协作。
- **为什么值得关注**：123k stars，是“多智能体金融研究”方向的标杆项目。
- **技术栈/架构亮点**：多 agent 协作、LLM 驱动、研究导向而非直接下单。
- **是否适合借鉴**：适合。可借鉴其多智能体角色分工（如分析师、风控、交易员）来构建企业级投研 Agent 框架。
- **可能风险**：研究工具，实盘化需大量工程加固；多 agent 决策可能放大一致性与过拟合问题。

### 3.5 jackson-cmd/risk-aware-trading-agents
- **解决什么问题**：美股 LLM 交易 Agent 的公开榜单，强调 point-in-time 新闻回测、防未来函数、look-ahead 检查。
- **为什么值得关注**：虽然 star 仅 475，但 24h +40、7d +266，且工程严谨性思路突出。
- **技术栈/架构亮点**：冻结 2020/2022/2026 时点市场数据、每次运行做 look-ahead 检查、LLM agents over MCP、10 家券商 paper/live 交易。
- **是否适合借鉴**：非常值得。其“防未来函数”与“point-in-time 回测”是量化研究工程化的关键实践，可直接借鉴到内部回测平台。
- **可能风险**：涉及 paper/live 交易，需注意 API key 安全与券商合规。

### 3.6 JustVugg/colibri
- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，热专家在 GPU、温专家在 RAM、冷专家从 NVMe 流式加载。
- **为什么值得关注**：53k stars、24h +221，纯 C 实现，代表“本地推理”与“资源分层”趋势。
- **技术栈/架构亮点**：CUDA/Vulkan + RAM + NVMe 分层推理，C 语言实现。
- **是否适合借鉴**：适合。金融数据隐私场景下，本地推理是刚需；分层推理思路可降低自建 LLM 推理成本。
- **可能风险**：与交易无直接关系，但作为基础设施组件有参考价值。

### 3.7 headroomlabs-ai/headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 块进入 LLM 前进行压缩，降低 token 消耗。
- **为什么值得关注**：80k stars、24h +117，上下文工程是 Agent 成本控制的核心。
- **技术栈/架构亮点**：库 + 代理 + MCP server 三种形态，宣称 JSON 可减少 60-95% token。
- **是否适合借鉴**：适合。交易 Agent 需要处理大量行情、订单簿、新闻数据，上下文压缩可显著降低成本与延迟。
- **可能风险**：压缩可能丢失关键信息，金融场景需验证压缩后决策一致性。

### 3.8 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”。
- **为什么值得关注**：47k stars、24h +173，AI 治理与审计是金融场景刚需。
- **技术栈/架构亮点**：支持人工或 Agent 自审计，覆盖幻觉检测、提示注入、NIST AI RMF、ISO 42001、EU AI Act 等框架。
- **是否适合借鉴**：非常适合。金融企业部署 Agent 前需要审计与对齐验证，可借鉴其评估维度与 CLI 工具形态。
- **可能风险**：审计工具本身可能产生误报，需结合人工复核。

### 3.9 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多智能体与回测。
- **为什么值得关注**：38k stars，HKUDS 出品，学术背景较强。
- **技术栈/架构亮点**：多智能体 + MCP + 回测，研究导向。
- **是否适合借鉴**：适合作为多智能体交易研究的参考实现。
- **可能风险**：“Vibe-Trading”命名暗示低门槛，需警惕用户误以为可直接实盘。

### 3.10 dmitry-k-code19w1/raydium-meteora-sniper-bot-x64
- **解决什么问题**：Solana Raydium V4 与 Meteora DLMM 狙击 bot，宣称 Sub-50ms 执行。
- **为什么值得关注**：作为高风险样本警示。1 天内新建、0 fork、预编译 Windows x64 二进制、Jupyter Notebook 语言标记异常。
- **技术栈/架构亮点**：信息不足，且预编译二进制无法审计。
- **是否适合借鉴**：不建议借鉴。此类项目常见于诈骗或恶意软件分发。
- **可能风险**：极高。预编译二进制可能包含恶意代码；狙击/抢跑类 bot 在 DeFi 场景存在重大资金与合规风险。

## 4. 趋势归纳

- **技术趋势**：
  - AI Agent “技能包化”：Claude Code / Codex / Cursor 的 skill 成为主流分发单元。
  - 本地优先推理：MoE 分层推理、纯 C 推理引擎、1-bit LLM 框架。
  - 上下文工程：LLM 输入压缩、token 优化成为独立工具品类。
  - MCP 生态持续扩张：远程 MCP 服务器清单、MCP 服务器清单均保持高增长。

- **产品趋势**：
  - “研究型交易 Agent”多于“自动下单 bot”：多数高价值项目定位为分析、回测、决策辅助，而非直接执行交易。
  - AI Agent 治理与审计产品化：iFixAi 等将审计能力做成 CLI 工具。
  - 自托管与本地优先：从 AI 设计工具到交易面板，均强调 local-first。

- **量化/交易策略趋势**：
  - 防未来函数与 point-in-time 回测成为差异化卖点。
  - LLM 新闻情绪与多智能体决策结合。
  - A 股数据服务与量化工作台活跃：同花顺官方 Financial-API、tick-stock-panel、daily_stock_analysis。

- **AI Agent 与自动化交易结合趋势**：
  - 多智能体协作框架（TradingAgents、Vibe-Trading、ruflo）与交易研究结合。
  - MCP 作为 Agent 连接行情、新闻、交易接口的标准协议。
  - 审计与风控 Agent 开始出现，形成“交易 Agent + 审计 Agent”的配对趋势。

- **值得后续做原型验证的方向**：
  - Point-in-time 新闻回测框架。
  - 交易研究 skill 包的标准化结构。
  - LLM 上下文压缩在行情数据处理中的效果。
  - 本地推理引擎在金融数据隐私场景的可行性。

## 5. 今日灵感清单

1. **MVP：防未来函数新闻回测沙箱**。参考 `risk-aware-trading-agents`，构建一个最小可用的 point-in-time 新闻回测环境，冻结历史时点数据，每次运行自动做 look-ahead 检查。
2. **MVP：交易研究 Skill 包模板**。参考 `claude-trading-skills` 与 `day-trader-skill`，设计一套标准化的交易研究 skill 结构（数据获取、图表、筛选、策略构思），供 Codex/Claude Code 调用。
3. **调研：LLM 上下文压缩对金融决策一致性的影响**。参考 `headroom`，测试压缩前后 LLM 在财报摘要、新闻情绪判断上的输出一致性。
4. **调研：MCP 在交易数据接入中的标准化程度**。参考 `awesome-remote-mcp-servers` 与 `awesome-mcp-servers`，梳理现有金融数据 MCP server 的覆盖与缺口。
5. **Demo：本地推理引擎跑金融情感分析**。参考 `colibri` 与 `kimi-k3-in-c`，验证在无 GPU 环境下用分层推理跑轻量金融 NLP 任务的可行性。
6. **Demo：AI Agent 审计清单集成**。参考 `iFixAi`，将幻觉检测、提示注入检查、NIST AI RMF 维度集成到内部 Agent 发布流水线。
7. **Watchlist：`risk-aware-trading-agents`**。虽然 star 少，但工程严谨性思路值得持续跟踪。
8. **Watchlist：`Hithink-Tech-Org/Financial-API`**。官方 A 股数据服务，若稳定维护，可作为内部数据源备选。
9. **原型：A 股投研日报自动化**。参考 `daily_stock_analysis`，用 LLM + 多源行情 + 定时任务生成每日投研摘要，输出到看板。
10. **调研：Agent skill 的版本管理与审计**。参考 `agentic-awesome-skills` 与 `awesome-claude-code`，研究如何对第三方 skill 做安全审计与版本锁定。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| jackson-cmd/risk-aware-trading-agents | 防未来函数与 point-in-time 回测思路突出，star 低但工程价值高 |
| Hithink-Tech-Org/Financial-API | 官方 A 股数据服务，MCP/CLI/API 多形态，适合作为数据源备选 |
| tradermonty/claude-trading-skills | 交易研究 skill 包代表，增速快，可观察 skill 标准化演进 |
| TauricResearch/TradingAgents | 多智能体金融研究标杆，适合跟踪 Agent 架构演进 |
| ifixai-ai/iFixAi | AI Agent 审计工具，金融场景刚需，值得跟踪治理框架落地 |
| headroomlabs-ai/headroom | 上下文压缩对交易 Agent 成本控制有直接价值 |
| JustVugg/colibri | 本地分层推理引擎，金融数据隐私场景有潜力 |
| shy3130/tick-stock-panel | A 股自托管量化工作台，DuckDB + Polars + FastAPI 技术栈值得参考 |
| virattt/ai-hedge-fund | AI 对冲基金团队模拟，经典研究项目，适合观察多 agent 决策模式 |
| paperswithbacktest/awesome-systematic-trading | 系统化交易资源清单，适合定期扫描新工具与策略 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

特别警示：
- `raydium-meteora-sniper-bot-x64` 为高风险项目：1 天内新建、0 fork、预编译 Windows x64 二进制，存在恶意软件风险，不建议下载或运行。
- `Turnitout-Humanizer` 属于学术作弊工具，与金融无关，且存在学术诚信与合规风险。
- 多个清单类项目（awesome-*）因关键词误匹配进入候选，其“trading_bot”等风险标记不代表项目本身是交易 bot，需注意分类噪声。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-11-22.json`，1 日涨星数据可用。
- **7 日基线**：已提供 `baseline_7d: 2026-11-16.json`，7 日涨星数据可用。
- **30 日涨星**：所有项目 `star_delta_30d` 均为 null，30 日趋势无法分析。
- **采集失败**：`wickline` 与 `raydium-meteora-sniper-bot-x64` 的 `star_delta_7d` 为 null，可能因项目过新或基线缺失导致。
- **样本偏差**：候选列表包含大量 awesome-* 清单类项目，因关键词误匹配（如 readme 中出现 “trading bot”“quant”“volatility”）进入候选，实际与金融/量化交易直接相关的项目占比有限。分类标签（如 `category_guess`）为启发式推断，存在噪声。
- **风险提示**：`risk_flags` 与 `risk_level` 为自动标记，可能将清单类项目误标为“trading_bot”或“crypto_related”，需结合项目实际内容判断。
