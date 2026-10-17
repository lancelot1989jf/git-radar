# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-16

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：以 `iFixAi` 为代表，聚焦 AI Agent 的独立审计、对齐、安全与合规，7 日涨星 +5675，是本期最强信号之一。
  2. **AI 交易与量化研究框架**：`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`ai-hedge-fund` 等项目持续活跃，LLM 多智能体交易、回测与策略研究仍是热点。
  3. **本地化/自托管金融数据与推理基础设施**：`CNEquity`（A 股数据基础设施）、`colibri`（本地 MoE 推理）、`project-maya`（本地大模型推理）显示“数据自托管 + 本地推理 + Agent 化”的工程趋势。

- **是否出现新趋势**：
  - 出现明显的 **AI Agent 审计/对齐/治理** 趋势，且与金融风控场景高度相关。
  - **Agent Skills / 设计智能** 类项目大量进入榜单（`ui-ux-pro-max-skill`、`open-design`、`logo-design-skill`、`ux-ui-agent-skills`），说明“用 Agent 生成专业 UI/UX”正在成为独立产品方向。
  - **本地优先、零 API Token、自托管** 的金融数据与推理工具开始冒头。

- **是否出现值得复刻/参考的工程架构**：
  - `CNEquity` 的“行级溯源 + PIT 语义 + 复权与历史成分内置 + MCP 原生 + DuckDB/Parquet/Polars”是高质量金融数据工程参考。
  - `nautilus_trader` 的 Rust 原生、确定性事件驱动交易引擎，适合作为低延迟交易系统架构参考。
  - `iFixAi` 的 Agent 审计/评估思路，可迁移到交易 Agent 的合规与风控层。

- **是否有明显骗局、过度营销或高风险项目**：
  - 本期未发现明显骗局项目，但大量 `awesome-*` 列表类项目因关键词误匹配进入榜单，实际与金融/量化交易关联较弱。
  - `Financial_freedom` 描述为“最全赚钱投资指南”，属于典型内容营销/投资指南类项目，信息价值有限，需谨慎看待。
  - 多个 `trading_bot` 相关项目（`freqtrade`、`QuantDinger`、`Vibe-Trading` 等）带有 crypto、杠杆/网格相关风险标记，不应直接用于实盘。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 489537 | +351 | +2490 | Python | API 列表 | 免费 API 合集 | 数据源发现 | 中 |
| 2 | ifixai-ai/iFixAi | 28803 | +405 | +5675 | Python | AI 审计/风控 | AI Agent 独立审计与对齐 | Agent 治理/风控 | 低 |
| 3 | awesome-selfhosted/awesome-selfhosted | 327396 | +376 | +2339 | 无 | 自托管列表 | 自托管服务列表 | 自托管架构选型 | 中 |
| 4 | nextlevelbuilder/ui-ux-pro-max-skill | 136624 | +320 | +2328 | Python | AI 设计技能 | AI UI/UX 设计智能 | Agent 产品化 | 低 |
| 5 | LosaLosSantos/aurelio-finance | 3946 | +308 | +2390 | Python | 个人财务/AI 顾问 | 自托管个人财务 + AI 顾问 | 个人财务 Agent | 低 |
| 6 | vinta/awesome-python | 328024 | +285 | +1802 | Python | Python 列表 | Python 工具列表 | 技术选型 | 低 |
| 7 | VoltAgent/awesome-design-md | 121817 | +175 | +1736 | 无 | 设计系统 | DESIGN.md 设计系统合集 | Agent UI 生成 | 中 |
| 8 | JustVugg/colibri | 42454 | +235 | +1598 | C | 本地推理 | 本地 MoE 模型推理引擎 | 本地推理基础设施 | 低 |
| 9 | codecrafters-io/build-your-own-x | 553868 | +354 | +1610 | Markdown | 教程 | 从零构建技术 | 工程学习 | 中 |
| 10 | nexu-io/open-design | 101687 | +294 | +1422 | TypeScript | AI 设计工作台 | 协作式 AI 设计 Agent 工作台 | 协作 Agent 产品 | 低 |
| 11 | ruvnet/ruflo | 75706 | +465 | +1487 | TypeScript | Agent 框架 | 多智能体 swarm 框架 | 多 Agent 编排 | 低 |
| 12 | avelino/awesome-go | 188793 | +158 | +1179 | Go | Go 列表 | Go 框架/库列表 | 技术选型 | 中 |
| 13 | TauricResearch/TradingAgents | 111559 | +141 | +1136 | Python | AI 交易 | 多智能体 LLM 金融交易框架 | 交易 Agent 架构 | 低 |
| 14 | kaankiziltug/logo-design-skill | 3537 | +80 | +1062 | HTML | AI 设计技能 | Logo 设计 Agent 技能 | Agent 技能化 | 低 |
| 15 | awesome-dsh-plugin/awesome-dsh-plugin | 19035 | +119 | +785 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | Agent 插件生态 | 低 |
| 16 | headroomlabs-ai/headroom | 75538 | +71 | +681 | Python | 上下文压缩 | LLM 输出/token 压缩 | 成本优化 | 低 |
| 17 | MakazhanAlpamys/Soup | 9201 | +76 | +750 | Python | LLM 微调 | 低显存 LLM 微调 | 本地模型微调 | 低 |
| 18 | hesreallyhim/awesome-claude-code | 55865 | +78 | +529 | Python | Claude 资源 | Claude Code 资源列表 | Agent 工具链 | 低 |
| 19 | HKUDS/Vibe-Trading | 35656 | +59 | +565 | Python | AI 交易 | 个人交易 Agent | 交易 Agent 产品化 | 中 |
| 20 | punkpeye/awesome-mcp-servers | 96490 | +69 | +477 | 无 | MCP 列表 | MCP server 合集 | MCP 生态 | 低 |
| 21 | codeman008/Financial_freedom | 7387 | +105 | +635 | 无 | 投资指南 | 赚钱投资指南 | 低 | 中 |
| 22 | mw00/project-maya | 964 | +52 | +731 | C++ | 本地推理 | 本地 GLM MoE 推理 | 本地推理基础设施 | 低 |
| 23 | ripienaar/free-for-dev | 139670 | +51 | +388 | HTML | 免费资源 | 开发者免费资源 | 成本优化 | 低 |
| 24 | ZhuLinsen/daily_stock_analysis | 66483 | +50 | +364 | Python | 股票分析 | LLM 多市场股票分析 | 金融分析 Agent | 低 |
| 25 | plugin87/ux-ui-agent-skills | 2018 | +71 | +454 | JavaScript | AI 设计技能 | UX/UI Agent 技能 | Agent 技能化 | 低 |
| 26 | microsoft/BitNet | 41179 | +4 | +803 | C++ | 模型推理 | 1-bit LLM 推理框架 | 模型压缩/推理 | 低 |
| 27 | nautechsystems/nautilus_trader | 30210 | +108 | +430 | Rust | 交易引擎 | Rust 事件驱动交易引擎 | 低延迟交易架构 | 中 |
| 28 | punkpeye/awesome-remote-mcp-servers | 1362 | +59 | +363 | 无 | MCP 列表 | 远程 MCP server 合集 | MCP 生态 | 中 |
| 29 | sickn33/agentic-awesome-skills | 47737 | +40 | +334 | Python | Agent 技能 | Agent 技能目录/控制面 | Agent 技能管理 | 低 |
| 30 | anbeime/skill | 8176 | +45 | +420 | Python | Agent 技能 | 技能商店 | Agent 技能生态 | 低 |
| 31 | rootSunc/CNEquity | 579 | +105 | +233 | Python | 金融数据 | A 股数据基础设施 | 金融数据工程 | 低 |
| 32 | freqtrade/freqtrade | 55479 | +39 | +294 | Python | 交易机器人 | 开源加密交易机器人 | 交易系统参考 | 中 |
| 33 | lukasz-madon/awesome-remote-job | 49579 | +62 | +242 | 无 | 远程工作 | 远程工作资源 | 低 | 低 |
| 34 | AIPentest/CyberStrikeAI | 7853 | +18 | +495 | Go | AI 安全 | AI 原生网络安全 | 安全 Agent | 低 |
| 35 | CopilotKit/OpenBot | 6571 | +39 | +286 | TypeScript | Agent 自动化 | 开源 AI 数字员工 | 浏览器自动化 Agent | 中 |
| 36 | openbq-org/OpenBB | 74311 | +29 | +268 | Python | 金融数据平台 | 开放数据平台 | 金融数据平台 | 中 |
| 37 | shiyu-coder/Kronos | 40849 | +36 | +459 | Python | 金融基础模型 | 金融市场基础模型 | 金融大模型 | 低 |
| 38 | cactus-compute/needle | 14059 | +32 | +304 | Python | 端侧模型 | 微型设备自动化模型 | 端侧 Agent | 中 |
| 39 | wilsonfreitas/awesome-quant | 30154 | +61 | +133 | HTML | 量化列表 | 量化资源列表 | 量化技术选型 | 中 |
| 40 | nidhinjs/prompt-master | 14531 | +29 | +295 | 无 | 提示工程 | 提示词优化技能 | 提示工程 | 低 |
| 41 | code-yeongyu/oh-my-openagent | 70119 | +31 | +195 | TypeScript | Agent 编排 | 图工程 Agent | Agent 编排 | 低 |
| 42 | awesomedata/awesome-public-datasets | 79562 | +38 | +154 | 无 | 数据集列表 | 开放数据集列表 | 数据源发现 | 中 |
| 43 | shy3130/tick-stock-panel | 5920 | +40 | +178 | Python | 量化工作台 | A 股自建策略/监控/回测 | 量化工作台 | 低 |
| 44 | OpenByteInc/QuantDinger | 12846 | +26 | +240 | Python | AI 交易 OS | AI 交易 OS/SaaS | 交易 SaaS 架构 | 中 |
| 45 | fffaraz/awesome-cpp | 73850 | +19 | +137 | 无 | C++ 列表 | C++ 资源列表 | 技术选型 | 低 |
| 46 | rust-unofficial/awesome-rust | 59900 | +15 | +153 | Rust | Rust 列表 | Rust 资源列表 | 技术选型 | 低 |
| 47 | virattt/ai-hedge-fund | 64040 | +19 | +122 | Python | AI 交易 | AI 对冲基金团队 | 多 Agent 交易研究 | 低 |
| 48 | josephmisiti/awesome-machine-learning | 74597 | +7 | +37 | Python | ML 列表 | ML 资源列表 | 技术选型 | 低 |
| 49 | Developer-Y/cs-video-courses | 83687 | +4 | +45 | 无 | 课程列表 | CS 视频课程 | 学习资源 | 中 |
| 50 | vuejs/awesome-vue | 73516 | 0 | -1 | 无 | Vue 列表 | Vue 资源列表 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi — AI Agent 独立审计与对齐

- **解决什么问题**：回答“AI Agent 是否在做它该做的事”，提供 120 秒内完成的 Agent 审计/评估。
- **为什么值得关注**：7 日涨星 +5675，是本期最强涨星项目之一；topic 覆盖 AI 治理、AI 安全、幻觉检测、提示注入、ISO 42001、NIST AI RMF、OWASP LLM、EU AI Act 等，说明其定位是 AI Agent 合规与风控基础设施。
- **技术栈/架构亮点**：Python + Apache-2.0；CLI 形态；强调“由人或 Agent 自身运行”的审计流程。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。交易 Agent 上线前需要审计、对齐、幻觉检测、提示注入防护，iFixAi 的思路可直接迁移为“交易 Agent 上线前审计门禁”。
- **可能风险**：项目较新（2026-04 创建），需观察维护活跃度；审计标准本身可能尚未成熟；不能替代真实金融合规审查。

### 3.2 TauricResearch/TradingAgents — 多智能体 LLM 金融交易框架

- **解决什么问题**：用多个 LLM Agent 协作完成金融交易研究与决策。
- **为什么值得关注**：总 star 111559，7 日 +1136，持续活跃；是“LLM 多智能体交易”方向的代表性项目。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 架构；topic 含 agent、finance、llm、multiagent、trading。
- **是否适合借鉴**：适合研究多 Agent 交易决策流程、信号生成、风险讨论机制；但不应直接用于实盘。
- **可能风险**：策略过拟合、回测幸存者偏差、LLM 幻觉导致错误交易信号；金融合规风险；API key 安全。

### 3.3 HKUDS/Vibe-Trading — 个人交易 Agent

- **解决什么问题**：定位为“Vibe-Trading: Your Personal Trading Agent”，将 LLM、MCP、多 Agent 与交易结合。
- **为什么值得关注**：HKUDS 出品，总 star 35656，7 日 +565；topic 覆盖 algorithmic-trading、backtesting、fintech、llm、mcp、multi-agent。
- **技术栈/架构亮点**：Python + MIT；MCP 集成；多 Agent；回测能力。
- **是否适合借鉴**：适合研究“个人交易 Agent”的产品形态与 MCP 工具调用模式。
- **可能风险**：crypto_related、likely_research_tool；存在策略过拟合、回测造假、API key 泄露风险；不建议直接实盘。

### 3.4 rootSunc/CNEquity — A 股数据基础设施

- **解决什么问题**：提供中国 A 股 55 个日更数据集，覆盖行情、基本面、期货、资金面、公告事件、指数行业、宏观与风险；强调行级溯源、PIT 语义、复权与历史成分内置、MCP 原生、自托管、零注册、零 API Token。
- **为什么值得关注**：虽然 star 仅 579，但 24h +105，且架构描述非常专业，是高质量金融数据工程样本。
- **技术栈/架构亮点**：Python + Apache-2.0；DuckDB、Parquet、Polars；MCP 原生；PIT（point-in-time）语义；自托管。
- **是否适合借鉴**：非常适合。金融数据工程的 PIT、行级溯源、复权处理、MCP 化是构建量化研究平台的关键。
- **可能风险**：项目较新、star 较低，需验证数据质量与维护持续性；数据源合规性需自行评估。

### 3.5 nautechsystems/nautilus_trader — Rust 原生事件驱动交易引擎

- **解决什么问题**：提供生产级 Rust 原生交易引擎，确定性事件驱动架构，支持回测与实盘。
- **为什么值得关注**：总 star 30210，7 日 +430；是少数 Rust 写的交易引擎，适合低延迟场景。
- **技术栈/架构亮点**：Rust + LGPL-3.0；确定性事件驱动；支持 crypto、equity、forex、futures、options、sports betting。
- **是否适合借鉴**：适合研究低延迟交易系统架构、事件溯源、回测与实盘一致性设计。
- **可能风险**：crypto_related、leverage_or_grid_related；LGPL 许可证需注意；实盘交易风险高。

### 3.6 OpenByteInc/QuantDinger — AI 交易 OS / 多租户交易 SaaS

- **解决什么问题**：定位为“开源 AI Trading OS”，支持 agent trading、vibe trading、策略研究、回测、paper/live 交易，并可启动多租户交易 SaaS。
- **为什么值得关注**：总 star 12846，7 日 +240；产品化思路清晰，集成 Jev System One、用户管理、计费、支付、结算。
- **技术栈/架构亮点**：Python + Apache-2.0；MCP server；支持 crypto、stocks、forex；SaaS 多租户架构。
- **是否适合借鉴**：适合研究“交易 SaaS 产品架构”与“AI 交易 OS”的产品边界。
- **可能风险**：crypto_related；涉及实盘交易、多租户资金结算，合规与安全风险高；不建议直接运行。

### 3.7 virattt/ai-hedge-fund — AI 对冲基金团队

- **解决什么问题**：用多个 AI Agent 模拟对冲基金团队的研究与决策流程。
- **为什么值得关注**：总 star 64040，是 AI 交易领域的知名项目；7 日 +122。
- **技术栈/架构亮点**：Python + MIT；多 Agent 角色分工。
- **是否适合借鉴**：适合研究多 Agent 投研流程、信号生成与组合管理思路。
- **可能风险**：likely_research_tool；策略过拟合、回测偏差；不应视为真实收益信号。

### 3.8 freqtrade/freqtrade — 开源加密交易机器人

- **解决什么问题**：免费开源加密交易机器人，支持回测与实盘。
- **为什么值得关注**：总 star 55479，是加密交易 bot 领域的成熟项目；7 日 +294。
- **技术栈/架构亮点**：Python + GPL-3.0；Telegram bot；策略回测。
- **是否适合借鉴**：适合研究交易 bot 的模块化设计、策略接口、回测框架。
- **可能风险**：crypto_related、trading_bot；实盘资金风险高；GPL 许可证需注意。

### 3.9 ZhuLinsen/daily_stock_analysis — LLM 多市场股票分析系统

- **解决什么问题**：LLM 驱动的多市场股票智能分析，多源行情、实时新闻、决策看板、自动推送，支持零成本定时运行。
- **为什么值得关注**：总 star 66483，7 日 +364；是“LLM + 股票分析 + 自动化推送”的典型产品。
- **技术栈/架构亮点**：Python + MIT；AI Agent；A 股；量化金融 topic。
- **是否适合借鉴**：适合研究金融分析 Agent 的产品形态、数据源整合、定时任务与推送机制。
- **可能风险**：分析结果可能存在幻觉；不应作为投资决策依据。

### 3.10 colibri / project-maya — 本地 MoE 模型推理

- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，强调纯 C、零依赖、专家流式加载；project-maya 则支持 GLM-5.3-Flash 本地推理。
- **为什么值得关注**：colibri 总 star 42454，7 日 +1598；project-maya 虽小但 7 日 +731。两者都指向“本地大模型推理”趋势。
- **技术栈/架构亮点**：colibri 用 C、Apache-2.0；project-maya 用 C++、MIT，支持 CUDA/ROCm、OpenAI/Anthropic 兼容 API、量化工具。
- **是否适合借鉴**：适合研究本地推理基础设施，尤其是金融数据敏感场景下的私有化部署。
- **可能风险**：硬件门槛高；模型授权与合规需确认。

## 4. 趋势归纳

- **技术趋势**：
  - **AI Agent 治理/审计/对齐**成为独立赛道，且与金融风控天然契合。
  - **本地优先、自托管、零 API Token** 的金融数据与推理基础设施兴起。
  - **MCP（Model Context Protocol）** 成为 Agent 工具连接的事实标准，多个项目原生支持 MCP。
  - **Agent Skills 生态**爆发：UI/UX、Logo、Prompt、设计系统等技能包大量出现。
  - **低显存/本地模型微调与推理**（Soup、BitNet、colibri、project-maya）持续升温。

- **产品趋势**：
  - “AI 交易 OS / 交易 SaaS”产品化尝试增多（QuantDinger、Vibe-Trading）。
  - 个人财务 + AI 顾问（aurelio-finance）显示 AI 金融顾问产品化方向。
  - 协作式 AI 设计工作台（open-design）展示多 Agent 协作产品形态。

- **量化/交易策略趋势**：
  - LLM 多智能体交易框架仍是主流研究方向。
  - 金融基础模型（Kronos）尝试用大模型直接建模金融市场。
  - A 股量化工作台（tick-stock-panel、CNEquity）显示中文市场量化工具链在完善。

- **AI Agent 与自动化交易结合趋势**：
  - 交易 Agent 从“单 Agent 决策”向“多 Agent 协作 + 审计 + 风控”演进。
  - MCP 成为交易 Agent 连接数据源、交易所、风控模块的标准接口。
  - Agent 审计（iFixAi）与交易 Agent 结合，可能形成“交易 Agent 上线前审计门禁”。

- **值得后续做原型验证的方向**：
  - 交易 Agent 的审计/对齐/幻觉检测门禁。
  - 基于 MCP 的金融数据服务层。
  - 本地化金融数据 + 本地 LLM 推理的私有化投研助手。
  - 多 Agent 投研流程的确定性回测与归因。

## 5. 今日灵感清单

1. **MVP：交易 Agent 上线前审计门禁**：参考 iFixAi，做一个针对交易 Agent 的审计 checklist，包含幻觉检测、提示注入测试、策略合规检查、API key 安全扫描。
2. **MVP：MCP 金融数据服务**：参考 CNEquity，用 DuckDB + Parquet + Polars 构建一个 MCP 原生的 A 股数据服务，支持 PIT 查询与行级溯源。
3. **调研：本地 LLM 推理在金融数据敏感场景的可行性**：调研 colibri、project-maya、BitNet 的部署成本、延迟与精度，评估私有化投研助手方案。
4. **Demo：多 Agent 投研流程回测**：用 TradingAgents 或 ai-hedge-fund 的架构，让 Codex/Agent 自动复现一个“分析师-风控-交易员”多 Agent 回测 demo，重点验证回测一致性。
5. **MVP：个人财务 AI 顾问**：参考 aurelio-finance，做一个自托管个人财务追踪 + AI 顾问，强调本地数据、无第三方依赖。
6. **调研：Agent Skills 生态与交易 Agent 的结合**：调研 awesome-claude-code、agentic-awesome-skills、skill 等技能库，筛选可复用到金融分析/交易研究的技能。
7. **Demo：交易 SaaS 多租户架构原型**：参考 QuantDinger，设计一个 paper trading 优先、多租户、带计费与结算模块的交易 SaaS 架构图，不接实盘。
8. **MVP：LLM 输出压缩代理**：参考 headroom，为金融新闻/行情数据构建 token 压缩代理，降低 LLM 投研成本。
9. **调研：Rust 事件驱动交易引擎**：调研 nautilus_trader 的确定性事件驱动架构，评估是否适合作为内部回测/仿真引擎。
10. **Watchlist：CNEquity、iFixAi、TradingAgents、nautilus_trader、QuantDinger**，持续观察其架构演进与社区活跃度。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计/对齐/治理赛道代表，涨星极快，可迁移到交易 Agent 风控 |
| rootSunc/CNEquity | 高质量 A 股数据工程样本，PIT + MCP + 自托管架构值得深入研究 |
| TauricResearch/TradingAgents | LLM 多智能体交易框架代表，持续活跃 |
| nautechsystems/nautilus_trader | Rust 事件驱动交易引擎，低延迟架构参考 |
| OpenByteInc/QuantDinger | AI 交易 OS / 多租户 SaaS 产品化尝试，架构思路值得观察 |
| HKUDS/Vibe-Trading | 个人交易 Agent 产品形态，MCP + 多 Agent 集成 |
| virattt/ai-hedge-fund | 多 Agent 投研流程经典项目，适合研究角色分工 |
| JustVugg/colibri | 本地 MoE 推理引擎，金融数据私有化部署潜在基础设施 |
| mw00/project-maya | 本地大模型推理 + 量化工具，适合私有化投研场景 |
| ZhuLinsen/daily_stock_analysis | LLM 股票分析 + 自动推送产品形态，适合研究金融分析 Agent |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次数据提供了 `baseline_1d`（2026-10-15）和 `baseline_7d`（2026-10-09），1 日与 7 日涨星数据完整。
- **30 日基线**：所有项目的 `star_delta_30d` 均为 `null`，因此无法提供 30 日涨星趋势，长期趋势判断受限。
- **采集失败**：未发现明显采集失败字段；但部分项目 `language` 为 `null`，部分项目 `topics` 为空。
- **样本偏差**：候选列表包含大量 `awesome-*` 列表类项目（如 awesome-python、awesome-go、awesome-selfhosted 等），这些项目因关键词误匹配进入榜单，与金融/量化/交易直接相关性较弱，可能稀释真实信号。报告已尽量区分“直接相关项目”与“泛技术/列表类项目”。
- **分类噪声**：`category_guess` 与 `matched_queries` 存在明显误匹配（例如 UI 设计项目被归为 fintech/crypto_trading），分析时已基于项目实际描述与 topics 进行人工校正。
