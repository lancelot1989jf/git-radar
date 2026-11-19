# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-18

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的股票分析与交易 Agent 技能包**：`daily_stock_analysis`、`claude-trading-skills`、`day-trader-skill` 等项目显示，Claude/Codex 等编码 Agent 正在被包装成“交易技能包”，以市场分析、图表扫描、新闻跟踪、回测复盘为核心卖点。
  2. **AI Agent 治理与审计**：`iFixAi` 以“120 秒审计 Agent 是否在做该做的事”为卖点，结合 ISO 42001、NIST AI RMF、EU AI Act 等合规框架，显示 Agent 可观测性与风控正在成为独立产品方向。
  3. **本地化/自托管推理与数据工程**：`colibri`、`kimi-k3-in-c`、`project-maya` 等项目聚焦在消费级硬件上运行 MoE 大模型，对量化研究中的低成本本地推理、数据隐私和离线部署有直接借鉴意义。

- **是否出现新趋势**：出现明显的“**Agent Skills 即产品**”趋势。大量项目不再提供完整交易系统，而是以 Claude Code/Codex/Cursor 的 skill 包形式分发交易分析、回测、安全审计、UI 设计等能力。这与传统“交易 bot 仓库”形态明显不同。

- **是否出现值得复刻/参考的工程架构**：
  - `daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，适合作为轻量级研究看板 MVP 参考。
  - `tick-stock-panel` 的“自托管 + DuckDB + Polars + FastAPI + React + LLM 策略定制”组合，是较完整的本地量化工作台架构。
  - `headroom` 的“工具输出/日志/RAG 分块在进入 LLM 前压缩 token”思路，对高频调用 LLM 的金融 Agent 有直接降本价值。

- **是否有明显骗局、过度营销或高风险项目**：
  - `Turnitout-Humanizer` 声称可绕过 Turnitin、GPTZero 等学术查重系统，属于明显规避学术诚信检测的工具，与金融科技无关，且存在伦理与合规风险。
  - 多个项目因关键词误匹配进入候选集（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-mac` 等），并非真正的交易项目，需注意样本噪声。
  - 未发现明确要求输入真实交易所 API key 的项目，但所有带 `trading_bot` 标记的项目仍应默认视为高风险，不建议直接实盘运行。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 73413 | +222 | +2678 | Python | AI 交易/数据工程/量化研究 | LLM 驱动的多市场股票分析系统，含看板与自动推送 | 高：多源数据融合与零成本定时运行架构 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 151484 | +428 | +3145 | Python | 金融产品/Agent Skill | 面向多平台的 UI/UX 设计智能 skill | 中：金融看板与产品原型 UI 生成 | 低 |
| 3 | elementalsouls/Claude-BugHunter | 11598 | +1614 | +6069 | Python | 金融产品/安全审计 | Claude Code 漏洞挖掘与红队 skill 包 | 高：交易系统与 Agent 安全审计自动化 | 低 |
| 4 | tradermonty/claude-trading-skills | 7125 | +183 | +3346 | Python | 回测/交易研究 | 面向股票投资者的 Claude 交易技能包 | 高：交易研究流程的 Agent 化封装 | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 338479 | +285 | +2234 | 无 | 交易 bot/自托管 | 自托管网络服务与 Web 应用列表 | 低：误匹配，非交易项目 | 中 |
| 6 | JustVugg/colibri | 52050 | +235 | +2001 | C | 量化研究/推理引擎 | 分层 MoE 推理引擎，GPU/RAM/NVMe 混合调度 | 高：低成本本地大模型推理 | 低 |
| 7 | codecrafters-io/build-your-own-x | 563761 | +206 | +1804 | Markdown | 交易 bot/教程 | 从零重建技术的教程合集 | 低：误匹配，非交易项目 | 中 |
| 8 | public-apis/public-apis | 500151 | +206 | +1806 | Python | 加密交易/量化研究 | 免费 API 合集 | 中：金融数据 API 资源发现 | 中 |
| 9 | CopilotKit/OpenBot | 12901 | +115 | +1752 | TypeScript | 金融产品/交易 bot | 开源可自托管 AI bot 替代品 | 高：Agent 治理与生成式 UI 架构 | 中 |
| 10 | vinta/awesome-python | 335759 | +203 | +1599 | Python | 量化研究 | Python 工具精选列表 | 低：误匹配，通用资源列表 | 低 |
| 11 | ifixai-ai/iFixAi | 46657 | +289 | +1628 | Python | AI 交易/风控 | AI Agent 独立审计工具 | 高：Agent 合规与行为审计 | 低 |
| 12 | Jakeschincariol/day-trader-skill | 8660 | +201 | +1475 | Python | 回测/风控 | 11 个日内交易 Claude skills | 高：交易决策流程的 skill 化 | 低 |
| 13 | avelino/awesome-go | 194722 | +175 | +1311 | Go | 加密交易/回测 | Go 框架与库精选列表 | 低：误匹配，通用资源列表 | 中 |
| 14 | nexu-io/open-design | 108399 | +220 | +1125 | TypeScript | 金融产品/交易基础设施 | 协作式 AI 设计 Agent 工作区 | 中：金融产品原型与看板协作设计 | 低 |
| 15 | VoltAgent/awesome-design-md | 128188 | +153 | +1111 | 无 | 加密交易/金融产品 | 品牌设计系统 DESIGN.md 合集 | 低：误匹配，设计资源 | 中 |
| 16 | TauricResearch/TradingAgents | 123112 | +97 | +939 | Python | AI 交易/回测/量化研究 | 多 Agent LLM 金融交易框架 | 高：多 Agent 交易决策架构 | 低 |
| 17 | awesome-dsh-plugin/awesome-dsh-plugin | 25135 | +97 | +759 | JavaScript | 交易基础设施 | DeepSeek Harness 插件列表 | 低：误匹配，插件资源 | 低 |
| 18 | headroomlabs-ai/headroom | 80127 | +170 | +718 | Python | AI 交易/风控 | LLM 输入前压缩工具输出与日志 | 高：金融 Agent token 成本优化 | 低 |
| 19 | punkpeye/awesome-mcp-servers | 98159 | +325 | +528 | 无 | 金融产品 | MCP server 合集 | 中：金融数据 MCP 集成资源 | 低 |
| 20 | kaankiziltug/logo-design-skill | 7315 | +92 | +640 | HTML | 金融产品 | AI logo 设计 skill | 低：误匹配，设计工具 | 低 |
| 21 | ruvnet/ruflo | 82069 | +77 | +547 | TypeScript | AI 交易/回测 | 多智能体 swarm 编排框架 | 高：多 Agent 协调与记忆架构 | 低 |
| 22 | punkpeye/awesome-remote-mcp-servers | 3550 | +93 | +516 | 无 | AI 交易/加密交易 | 远程 MCP server 合集 | 中：远程金融数据服务集成 | 中 |
| 23 | jaywcjlove/awesome-mac | 118861 | +70 | +536 | Swift | 交易基础设施 | macOS 软件精选列表 | 低：误匹配，非交易项目 | 低 |
| 24 | ripienaar/free-for-dev | 143169 | +69 | +518 | HTML | 金融产品/量化研究 | 开发者免费资源列表 | 低：误匹配，资源列表 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 58334 | +74 | +515 | Python | AI 交易/量化研究 | Claude Code 资源精选 | 中：Agent 技能与工具发现 | 低 |
| 26 | microsoft/BitNet | 42118 | +304 | +573 | C++ | AI 交易/量化研究 | 1-bit LLM 官方推理框架 | 高：低比特量化推理 | 低 |
| 27 | garrytan/gbrain | 33294 | +49 | +568 | TypeScript | 金融产品 | OpenClaw/Hermes Agent Brain | 中：Agent 编排与记忆 | 低 |
| 28 | sickn33/agentic-awesome-skills | 49974 | +53 | +396 | Python | 回测 | 2955+ 可复用 AI Agent skills | 中：交易 skill 资源发现 | 低 |
| 29 | HKUDS/Vibe-Trading | 38509 | +41 | +429 | Python | AI 交易/回测/风控 | 个人交易 Agent | 高：LLM 交易 Agent 研究框架 | 低 |
| 30 | shy3130/tick-stock-panel | 8066 | +40 | +448 | Python | AI 交易/回测/量化研究 | 自托管 A 股量化工作台 | 高：本地量化工作台架构 | 低 |
| 31 | PurpleDoubleD/locally-uncensored | 4413 | +40 | +501 | TypeScript | AI 交易/量化研究 | 本地 AI studio | 低：误匹配，本地 AI 应用 | 低 |
| 32 | FareedKhan-dev/kimi-k3-in-c | 12423 | +106 | 信息不足 | C | AI 交易/量化研究/风控 | 单 CPU 运行 2.78T 参数 MoE 推理 | 高：极致内存效率的本地推理 | 低 |
| 33 | GoogleChrome/modern-web-guidance | 23044 | +680 | 信息不足 | 无 | 风控 | 编码 Agent 的 Web 最佳实践 | 低：误匹配，Web 开发资源 | 低 |
| 34 | TGrpg/awesome-telegram | 1774 | +11 | +504 | JavaScript | 量化研究/交易 bot | Telegram 频道/群组/机器人导航 | 低：误匹配，Telegram 资源 | 中 |
| 35 | GoogleChrome/modern-web-guidance-src | 8937 | +365 | 信息不足 | TypeScript | 风控 | 编码 Agent 的 Web 最佳实践源码 | 低：误匹配，Web 开发资源 | 低 |
| 36 | openbq-org/OpenBB | 75548 | +35 | +191 | Python | 加密交易/量化研究 | 面向分析师与 AI Agent 的开放数据平台 | 高：金融数据平台与 Agent 集成 | 中 |
| 37 | AhmadHassan-BTed/Turnitout-Humanizer | 12423 | +33 | +261 | HTML | 风控/交易 bot | 学术查重规避工具 | 低：伦理风险，非金融项目 | 中 |
| 38 | mw00/project-maya | 3048 | +43 | +234 | C++ | AI 交易/量化研究 | 自托管多模型 MoE 推理引擎 | 高：本地多模型推理与统一 API | 低 |
| 39 | aardappel/goose | 3718 | +37 | +269 | C++ | 交易基础设施 | Goose 编程语言 | 低：误匹配，编程语言项目 | 低 |
| 40 | rust-unofficial/awesome-rust | 60646 | +22 | +177 | Rust | AI 交易/回测/加密交易 | Rust 资源精选列表 | 低：误匹配，通用资源列表 | 中 |
| 41 | bangtutorial/bang-motion | 2698 | +163 | 信息不足 | HTML | 金融产品 | 浏览器动效 Agent skill | 低：误匹配，动效设计工具 | 低 |
| 42 | awesomedata/awesome-public-datasets | 80197 | +10 | +147 | 无 | 加密交易 | 开放数据集精选列表 | 中：金融数据集资源发现 | 中 |
| 43 | fffaraz/awesome-cpp | 74503 | +17 | +137 | 无 | 量化研究/交易基础设施 | C/C++ 资源精选列表 | 低：误匹配，通用资源列表 | 低 |
| 44 | code-yeongyu/oh-my-openagent | 70996 | +12 | +132 | TypeScript | 量化研究 | 图工程 Agent 工具 | 低：误匹配，Agent 工具 | 低 |
| 45 | virattt/ai-hedge-fund | 64751 | +13 | +111 | Python | 回测/风控 | AI 对冲基金团队模拟 | 高：多角色 Agent 投资决策模拟 | 低 |
| 46 | Developer-Y/cs-video-courses | 84885 | +4 | +63 | 无 | 量化研究/交易 bot | 计算机科学视频课程列表 | 低：误匹配，教育资源 | 中 |
| 47 | josephmisiti/awesome-machine-learning | 74850 | +2 | +47 | Python | AI 交易 | 机器学习资源精选列表 | 低：误匹配，通用资源列表 | 低 |
| 48 | vuejs/awesome-vue | 73473 | -1 | -6 | 无 | 量化研究 | Vue.js 资源精选列表 | 低：误匹配，前端资源 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis

- **解决什么问题**：将多源行情、实时新闻、LLM 分析和决策看板整合为一个可定时运行的股票分析系统，降低个人投资者搭建研究看板的门槛。
- **为什么值得关注**：24h 涨星 +222、7d 涨星 +2678，是候选集中涨星最猛的金融分析项目之一；同时覆盖 A 股、AI Agent、量化研究等多个热点方向。
- **技术栈/架构亮点**：Python + LLM 驱动；描述中提到“多源行情、实时新闻、决策看板、自动推送、零成本定时运行”，架构上强调数据融合与自动化调度。
- **是否适合借鉴**：适合。其“多源数据 + 定时任务 + 推送”模式可直接复刻为轻量级研究看板或企业级投研 Agent 的数据采集层。
- **可能风险**：LLM 生成的分析结论可能存在幻觉；自动推送可能放大错误信号；需注意数据源合规与授权。

### 3.2 elementalsouls/Claude-BugHunter

- **解决什么问题**：将漏洞挖掘和红队测试能力封装为 Claude Code skill 包，覆盖 24 类漏洞、681 个披露报告模式。
- **为什么值得关注**：24h 涨星 +1614，是候选集中单日涨星最高的项目之一，显示安全审计 Agent 化需求旺盛。
- **技术栈/架构亮点**：82 个 skills、15 个 slash commands，以“技能包”形式分发安全能力，强调企业身份与基础设施攻击矩阵。
- **是否适合借鉴**：适合。交易系统和金融 Agent 在上线前需要安全审计，此类 skill 包可作为自动化红队测试的参考架构。
- **可能风险**：红队工具可能被滥用；在未授权系统上运行存在法律风险；skill 内容需人工审核。

### 3.3 tradermonty/claude-trading-skills

- **解决什么问题**：为股票投资者和交易者提供市场分析、技术图表、经济日历、筛选器和策略开发的 Claude Code skills。
- **为什么值得关注**：7d 涨星 +3346，显示“交易研究流程 Agent 化”是当前强需求。
- **技术栈/架构亮点**：以 skill 包形式封装交易研究流程，而非提供完整交易系统，降低了维护复杂度。
- **是否适合借鉴**：适合。可将投研流程拆解为可复用的 Agent skills，用于企业级研究 Agent 的原型验证。
- **可能风险**：标记为 `likely_research_tool`，仅适合研究，不应直接用于实盘；策略开发存在过拟合风险。

### 3.4 TauricResearch/TradingAgents

- **解决什么问题**：提供多 Agent LLM 金融交易框架，模拟多个角色的交易决策团队。
- **为什么值得关注**：stars 123112，是候选集中最成熟的 AI 交易研究框架之一，且近期仍有 push。
- **技术栈/架构亮点**：Python + 多 Agent 架构，将交易决策拆分为多个 LLM 角色协作。
- **是否适合借鉴**：适合。多 Agent 决策架构可直接借鉴到企业级投研 Agent 框架中，尤其是角色分工与决策链设计。
- **可能风险**：标记为 `likely_research_tool`；多 Agent 决策可能产生一致性问题；回测结果可能过拟合。

### 3.5 ifixai-ai/iFixAi

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做该做的事”，支持人工或 Agent 自审。
- **为什么值得关注**：24h 涨星 +289，7d 涨星 +1628；结合 ISO 42001、NIST AI RMF、EU AI Act 等合规框架，是 Agent 治理赛道的代表性项目。
- **技术栈/架构亮点**：Python + CLI；覆盖幻觉检测、提示注入、LLM 安全、风险评估等维度。
- **是否适合借鉴**：非常适合。金融 Agent 的合规审计与行为监控是刚需，可借鉴其审计维度设计企业级 Agent 风控层。
- **可能风险**：审计结果依赖评估框架的完备性；不能替代人工合规审查。

### 3.6 JustVugg/colibri

- **解决什么问题**：在消费级硬件上运行前沿 MoE 模型，通过 GPU/RAM/NVMe 分层调度降低推理门槛。
- **为什么值得关注**：24h 涨星 +235，7d 涨星 +2001；C 语言实现，强调在现有硬件上运行。
- **技术栈/架构亮点**：分层推理引擎，热专家在 GPU、温专家在 RAM、冷专家从 NVMe 流式加载。
- **是否适合借鉴**：适合。量化研究中本地运行大模型可降低数据外泄风险与推理成本，其分层调度思路可借鉴到本地研究 Agent 架构。
- **可能风险**：性能依赖硬件配置；C 语言实现维护门槛较高。

### 3.7 headroomlabs-ai/headroom

- **解决什么问题**：在工具输出、日志、文件和 RAG 分块进入 LLM 前进行压缩，降低 token 消耗。
- **为什么值得关注**：24h 涨星 +170；对高频调用 LLM 的金融 Agent 有直接降本价值。
- **技术栈/架构亮点**：提供库、代理和 MCP server 三种形态；声称编码 Agent 减少 20% token，JSON 减少 60-95% token。
- **是否适合借鉴**：非常适合。金融 Agent 常需处理大量行情、新闻和日志数据，token 压缩可显著降低运营成本。
- **可能风险**：压缩可能损失关键信息，需验证对金融数据精度的影响。

### 3.8 shy3130/tick-stock-panel

- **解决什么问题**：提供自托管、零运维的 A 股量化工作台，支持自建策略、监控、回测和 LLM 策略定制。
- **为什么值得关注**：技术栈明确（DuckDB + Polars + FastAPI + React + LLM），是较完整的本地量化工作台参考。
- **技术栈/架构亮点**：自托管 + 零运维；DuckDB 与 Polars 适合本地分析型负载；支持第三方数据源接入。
- **是否适合借鉴**：适合。可作为本地量化研究 MVP 的架构蓝本，尤其是数据层选型。
- **可能风险**：标记为 `likely_research_tool`；自托管数据源质量与延迟需自行验证。

### 3.9 HKUDS/Vibe-Trading

- **解决什么问题**：提供个人交易 Agent，结合 LLM、MCP 和多 Agent 架构。
- **为什么值得关注**：来自 HKUDS，stars 38509，近期仍有 push，是学术机构在 AI 交易 Agent 方向的代表性工作。
- **技术栈/架构亮点**：Python + MCP + 多 Agent；强调 LLM 驱动的交易决策。
- **是否适合借鉴**：适合。学术机构的多 Agent 交易框架可作为研究方向参考，尤其是 MCP 在金融工具集成中的应用。
- **可能风险**：标记为 `likely_research_tool`；学术研究框架不应直接用于实盘。

### 3.10 virattt/ai-hedge-fund

- **解决什么问题**：模拟 AI 对冲基金团队，通过多角色 Agent 进行投资决策。
- **为什么值得关注**：stars 64751，是 AI 交易 Agent 领域的知名项目，近期仍有 push。
- **技术栈/架构亮点**：Python + 多角色 Agent 模拟，角色包括基金经理、研究员等。
- **是否适合借鉴**：适合。多角色决策模拟可作为投研流程 Agent 化的原型参考。
- **可能风险**：标记为 `likely_research_tool`；模拟结果不代表真实收益；存在过拟合风险。

## 4. 趋势归纳

- **技术趋势**：
  - **Agent Skills 成为分发单元**：交易分析、安全审计、UI 设计等能力以 Claude Code/Codex/Cursor 的 skill 包形式分发，而非完整应用。
  - **本地推理与量化压缩**：`colibri`、`kimi-k3-in-c`、`BitNet`、`project-maya` 等项目显示，在消费级硬件上运行大模型的技术持续升温。
  - **MCP 生态扩展**：多个项目涉及 MCP server 集成，金融数据源与工具正在通过 MCP 标准化接入 Agent。

- **产品趋势**：
  - **从“交易 bot”到“研究 Agent”**：热门项目更多定位为研究工具和决策辅助，而非自动执行交易。
  - **Agent 治理与审计产品化**：`iFixAi` 等项目将 Agent 合规、行为审计作为独立产品方向。
  - **自托管与本地优先**：`tick-stock-panel`、`OpenBot`、`locally-uncensored` 等项目强调自托管和本地运行，反映数据隐私需求。

- **量化/交易策略趋势**：
  - **LLM 驱动的多 Agent 决策**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 等项目持续探索多角色 LLM 协作决策。
  - **研究工具与回测分离**：多数项目将回测作为研究环节，而非直接连接实盘交易。

- **AI Agent 与自动化交易结合趋势**：
  - **交易研究流程的 skill 化**：市场分析、图表扫描、新闻跟踪、回测复盘被拆分为可复用 skills。
  - **Agent 审计与风控前置**：在 Agent 执行交易前引入独立审计层，是值得关注的方向。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据源标准化接入层。
  - 本地量化研究工作台（DuckDB + Polars + FastAPI + LLM）。
  - 交易 Agent 的 token 压缩与成本优化层。
  - 多 Agent 投研决策的审计与可观测性框架。

## 5. 今日灵感清单

1. **MVP：本地投研看板**：参考 `daily_stock_analysis` 和 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭建一个自托管投研看板，集成 LLM 生成每日摘要，支持定时推送。
2. **MVP：金融 Agent 审计层**：参考 `iFixAi`，为内部投研 Agent 设计一个轻量级审计模块，覆盖幻觉检测、提示注入、行为偏离等维度。
3. **调研：MCP 金融数据源标准化**：调研 `awesome-mcp-servers` 和 `awesome-remote-mcp-servers` 中与金融数据相关的 MCP server，评估标准化接入的可行性。
4. **调研：本地 MoE 推理**：调研 `colibri`、`kimi-k3-in-c`、`project-maya` 的分层推理与量化方案，评估在本地研究环境中运行大模型的成本与性能。
5. **Demo：交易研究 skill 包**：参考 `claude-trading-skills` 和 `day-trader-skill`，用 Codex/Claude Code 复现一个“市场扫描 + 新闻跟踪 + 回测复盘”的 skill 包原型。
6. **Demo：多 Agent 投研决策模拟**：参考 `TradingAgents` 和 `ai-hedge-fund`，用 Codex 自动搭建一个多角色投研决策模拟，重点验证角色分工与决策链设计。
7. **调研：Agent token 压缩**：调研 `headroom` 的压缩策略，评估在金融新闻、行情日志等场景下的 token 节省效果与信息损失。
8. **Watchlist：OpenBB**：关注 `OpenBB` 作为金融数据平台与 AI Agent 集成的进展，评估其作为数据层的可行性。
9. **Watchlist：OpenBot**：关注 `CopilotKit/OpenBot` 的 Agent 治理与生成式 UI 架构，评估其在金融 Agent 产品中的应用。
10. **安全审计自动化**：参考 `Claude-BugHunter`，为内部交易系统搭建自动化红队测试 skill 包，作为上线前安全检查的一部分。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 涨星迅猛，多源数据融合与定时推送架构值得持续跟踪 |
| TauricResearch/TradingAgents | 多 Agent 交易决策框架的成熟参考，学术与工程价值兼具 |
| ifixai-ai/iFixAi | Agent 审计与合规赛道代表，金融 Agent 风控刚需 |
| headroomlabs-ai/headroom | 金融 Agent token 成本优化的关键基础设施 |
| openbq-org/OpenBB | 金融数据平台与 AI Agent 集成的长期观察对象 |
| CopilotKit/OpenBot | Agent 治理与生成式 UI 架构，适合金融产品化借鉴 |
| HKUDS/Vibe-Trading | 学术机构在 AI 交易 Agent 方向的最新工作 |
| shy3130/tick-stock-panel | 本地量化工作台的完整架构参考 |
| JustVugg/colibri | 本地 MoE 推理的分层调度方案，适合量化研究本地化部署 |
| virattt/ai-hedge-fund | 多角色 AI 对冲基金模拟的知名项目，适合研究参考 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **基线数据**：本次报告使用了 `baseline_1d`（2026-11-17）和 `baseline_7d`（2026-11-11）两个基线文件，1 日与 7 日涨星数据基本完整。
- **缺失数据**：部分项目的 `star_delta_7d` 为 `null`（如 `kimi-k3-in-c`、`modern-web-guidance`、`modern-web-guidance-src`、`bang-motion`），可能因项目创建时间晚于 7 日基线或基线数据缺失，相关涨星数据标注为“信息不足”。
- **样本偏差**：候选集存在明显的**关键词误匹配噪声**。大量项目（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-mac`、`awesome-python`、`awesome-go`、`awesome-rust`、`awesome-cpp`、`awesome-vue`、`cs-video-courses`、`awesome-machine-learning` 等）因 README 或描述中偶然包含“trading bot”“quant”“order book”等关键词而被纳入，并非真正的金融/量化/交易项目。分析时应重点参考 `category_guess` 与 `topics` 字段，并结合项目实际内容判断。
- **风险标记**：`risk_flags` 中的 `trading_bot`、`crypto_related` 等标记来自关键词匹配，不代表项目本身一定存在风险，但应默认对涉及自动交易和加密资产的项目保持谨慎。
- **采集完整性**：本次快照共 48 个项目，`ranking_config.output_count` 为 80，说明候选集可能未达到预期输出数量，或存在采集上限。
