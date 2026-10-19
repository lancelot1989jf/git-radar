# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-18

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：iFixAi 以 24h +492、7d +5781 的涨星速度领跑，聚焦 AI Agent 的独立审计、对齐与合规评估，直接回应 AI Agent 经济中“Agent 是否在做它该做的事”这一核心问题。
  2. **AI 交易 Agent 与多智能体框架**：TradingAgents、Vibe-Trading、ruflo 等项目持续高热，LLM 多智能体交易框架与通用 Agent harness 正在融合，交易决策、回测、风控被拆分为可编排的 Agent 角色。
  3. **本地化/自托管金融数据与终端**：CNEquity、tick-stock-panel、aurelio-finance 等新项目强调自托管、零 API Token、PIT 语义、DuckDB/Parquet 数据湖，显示金融数据基础设施正在向本地优先、MCP 原生方向演进。

- **是否出现新趋势**：出现。AI Agent 的“审计/对齐/合规”从概念走向可运行工具（iFixAi），且与金融风控场景天然契合；同时“AI 技能包（skills）”生态爆发，大量项目以 Claude/Codex/Gemini 技能库形式出现，金融场景开始被包装为可安装的 Agent 技能。

- **是否出现值得复刻/参考的工程架构**：是。iFixAi 的 Agent 审计流水线、CNEquity 的 PIT 语义 + Parquet/DuckDB 数据湖、tick-stock-panel 的 FastAPI + Polars + DuckDB + React 自托管量化工作台、TradingAgents 的多角色 LLM 交易决策框架，均具备较高参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本批数据中未发现明确骗局，但需警惕以下高风险信号：
  - `Financial_freedom` 描述为“最全赚钱投资指南”，属于典型营销话术，且无 license、无 topics，信息透明度低。
  - 多个项目描述中包含“vibe trading”“AI Trading OS”“launch your own multi-tenant trading SaaS”等强营销措辞，需谨慎对待其真实能力。
  - 大量“awesome-list”类项目因关键词误匹配进入候选集，实际与金融/量化交易关联较弱，存在样本噪声。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 490148 | +322 | +2453 | Python | API 资源列表 | 免费 API 合集 | 数据源发现 | 中 |
| 2 | awesome-selfhosted/awesome-selfhosted | 328101 | +330 | +2411 | 无 | 自托管资源列表 | 自托管网络服务列表 | 自托管金融工具选型 | 中 |
| 3 | ifixai-ai/iFixAi | 29661 | +492 | +5781 | Python | AI 审计/风控 | AI Agent 独立审计工具 | Agent 治理与合规架构 | 低 |
| 4 | nextlevelbuilder/ui-ux-pro-max-skill | 137312 | +375 | +2395 | Python | AI 设计技能 | UI/UX 设计智能技能 | 金融产品前端生成 | 低 |
| 5 | ruvnet/ruflo | 76663 | +510 | +2287 | TypeScript | Agent 框架 | 多智能体 swarm 编排框架 | 交易 Agent 编排底座 | 低 |
| 6 | vinta/awesome-python | 328532 | +269 | +1830 | Python | Python 资源列表 | Python 工具精选 | 量化 Python 栈选型 | 低 |
| 7 | VoltAgent/awesome-design-md | 122136 | +169 | +1747 | 无 | 设计系统列表 | DESIGN.md 设计系统合集 | 金融 UI 设计规范 | 中 |
| 8 | nexu-io/open-design | 102266 | +267 | +1633 | TypeScript | AI 设计工作台 | 协作式 AI 设计 Agent 工作区 | 金融仪表盘原型 | 低 |
| 9 | codecrafters-io/build-your-own-x | 554391 | +228 | +1768 | Markdown | 教程列表 | 从零重建技术 | 交易系统教学 | 中 |
| 10 | JustVugg/colibri | 42774 | +146 | +1457 | C | MoE 推理引擎 | 本地运行 MoE 模型 | 本地 LLM 推理 | 低 |
| 11 | TauricResearch/TradingAgents | 111958 | +179 | +1257 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 交易决策 Agent 架构 | 低 |
| 12 | avelino/awesome-go | 189141 | +167 | +1199 | Go | Go 资源列表 | Go 框架与库精选 | Go 交易系统选型 | 中 |
| 13 | LosaLosSantos/aurelio-finance | 3963 | +12 | +1548 | Python | 个人金融/AI 顾问 | 自托管个人金融 AI 顾问 | 个人财富管理 MVP | 低 |
| 14 | awesome-dsh-plugin/awesome-dsh-plugin | 19383 | +186 | +943 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | Agent 插件生态 | 低 |
| 15 | headroomlabs-ai/headroom | 75923 | +316 | +835 | Python | LLM 上下文压缩 | 压缩 LLM 输入 token | 金融数据降本 | 低 |
| 16 | kaankiziltug/logo-design-skill | 3703 | +83 | +908 | HTML | AI 设计技能 | Logo 设计技能包 | 金融品牌生成 | 低 |
| 17 | MakazhanAlpamys/Soup | 9366 | +83 | +790 | Python | LLM 微调 | 低显存 LLM 微调 | 金融 LLM 微调 | 低 |
| 18 | HKUDS/Vibe-Trading | 35851 | +112 | +595 | Python | AI 交易/回测 | 个人交易 Agent | 多 Agent 交易框架 | 中 |
| 19 | plugin87/ux-ui-agent-skills | 2325 | +285 | +745 | JavaScript | AI 设计技能 | UX/UI Agent 技能 | 金融 UI 可访问性 | 低 |
| 20 | sickn33/agentic-awesome-skills | 47910 | +121 | +433 | Python | Agent 技能库 | Agent 技能目录与控制面 | Agent 技能管理 | 低 |
| 21 | shiyu-coder/Kronos | 41206 | +288 | +635 | Python | 金融基础模型 | 金融市场基础模型 | 金融 LLM 预训练 | 低 |
| 22 | ZhuLinsen/daily_stock_analysis | 66709 | +59 | +507 | Python | A 股分析/LLM | LLM 多市场股票分析 | 股票分析 Agent | 低 |
| 23 | hesreallyhim/awesome-claude-code | 55980 | +63 | +509 | Python | Claude Code 资源 | Claude Code 资源精选 | Agent 开发资源 | 低 |
| 24 | punkpeye/awesome-mcp-servers | 96584 | +51 | +436 | 无 | MCP 服务器列表 | MCP 服务器合集 | 金融 MCP 集成 | 低 |
| 25 | shy3130/tick-stock-panel | 6069 | +124 | +283 | Python | A 股量化工作台 | 自托管 A 股策略/监控/回测 | 量化工作台架构 | 低 |
| 26 | ripienaar/free-for-dev | 139772 | +40 | +394 | HTML | 免费资源列表 | 开发者免费资源 | 金融工具成本优化 | 低 |
| 27 | anbeime/skill | 8295 | +58 | +431 | Python | 技能商店 | AI Agent 技能商店 | 金融技能包 | 低 |
| 28 | Fincept-Corporation/FinceptTerminal | 32726 | +66 | +325 | C++ | 金融终端 | 现代金融分析终端 | 金融终端产品 | 低 |
| 29 | punkpeye/awesome-remote-mcp-servers | 1485 | +54 | +410 | 无 | 远程 MCP 列表 | 远程 MCP 服务器合集 | 远程金融数据 MCP | 中 |
| 30 | freqtrade/freqtrade | 55587 | +55 | +302 | Python | 加密交易机器人 | 开源加密交易机器人 | 交易机器人架构 | 中 |
| 31 | openbq-org/OpenBB | 74416 | +49 | +284 | Python | 金融数据平台 | 面向分析师与 Agent 的数据平台 | 金融数据中台 | 中 |
| 32 | mw00/project-maya | 1042 | +28 | +531 | C++ | 本地 LLM 推理 | 本地运行 GLM-5.3 MoE | 本地金融 LLM | 低 |
| 33 | codeman008/Financial_freedom | 7507 | +48 | +551 | 无 | 投资指南 | 赚钱投资指南 | 信息不足 | 中 |
| 34 | rootSunc/CNEquity | 708 | +63 | +354 | Python | A 股数据基础设施 | A 股数据湖 + MCP | 金融数据工程 | 低 |
| 35 | CopilotKit/OpenBot | 6646 | +46 | +281 | TypeScript | AI 同事/浏览器自动化 | 开源 AI 同事 | Agent 治理与操作记录 | 中 |
| 36 | nidhinjs/prompt-master | 14609 | +48 | +272 | 无 | 提示词技能 | 精准提示词生成 | 金融提示词工程 | 低 |
| 37 | microsoft/BitNet | 41199 | +15 | +486 | C++ | 1-bit LLM 推理 | 1-bit LLM 推理框架 | 低资源 LLM 推理 | 低 |
| 38 | code-yeongyu/oh-my-openagent | 70173 | +24 | +205 | TypeScript | Agent 编排 | 图工程 Agent 编排 | Agent 工作流编排 | 低 |
| 39 | awesomedata/awesome-public-datasets | 79608 | +29 | +173 | 无 | 公开数据集列表 | 高质量公开数据集 | 金融数据集发现 | 中 |
| 40 | OpenByteInc/QuantDinger | 12906 | +33 | +217 | Python | AI 交易 OS | AI 交易 OS/多租户 SaaS | 交易 SaaS 架构 | 中 |
| 41 | Orchestra-Research/AI-Research-SKILLs | 13684 | +41 | +222 | TeX | AI 研究技能 | AI 研究技能库 | 金融研究 Agent | 低 |
| 42 | Superior-Trade/trading-terminal | 887 | +48 | +266 | TypeScript | AI 交易终端 | Hyperliquid 自托管交易终端 | 交易终端集成 | 低 |
| 43 | rust-unofficial/awesome-rust | 59949 | +21 | +155 | Rust | Rust 资源列表 | Rust 代码与资源精选 | Rust 交易系统选型 | 低 |
| 44 | virattt/ai-hedge-fund | 64081 | +16 | +140 | Python | AI 对冲基金 | AI 对冲基金团队 | 多 Agent 投资决策 | 低 |
| 45 | fffaraz/awesome-cpp | 73885 | +12 | +130 | 无 | C++ 资源列表 | C++ 框架与库精选 | C++ 交易系统选型 | 低 |
| 46 | Developer-Y/cs-video-courses | 83696 | +7 | +39 | 无 | 课程列表 | CS 视频课程列表 | 量化课程资源 | 中 |
| 47 | josephmisiti/awesome-machine-learning | 74611 | +6 | +38 | Python | ML 资源列表 | ML 框架与库精选 | 金融 ML 选型 | 低 |
| 48 | vuejs/awesome-vue | 73511 | -3 | -1 | 无 | Vue 资源列表 | Vue 资源精选 | 金融前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 ifixai-ai/iFixAi

- **项目解决什么问题**：解决 AI Agent 经济中最关键的问题——“Agent 是否在做它该做的事”。提供由人或 Agent 自身运行的独立审计，声称 120 秒内给出答案。
- **为什么最近值得关注**：24h +492、7d +5781，涨星速度在候选集中排名前列。AI Agent 治理、对齐、安全正从学术概念走向工程工具，且与金融风控场景高度契合。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 覆盖 agent-evaluation、ai-governance、ai-safety、hallucination-detection、prompt-injection、NIST AI RMF、ISO 42001、EU AI Act、OWASP LLM 等，说明其审计维度覆盖幻觉检测、提示注入、合规框架映射，架构上可能是“评估器 + 合规规则引擎 + CLI”的组合。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。可借鉴其审计流水线设计，为交易 Agent 增加“决策前审计”与“决策后复盘”环节，例如在 Agent 下单前自动检查策略是否符合预设风控规则、是否出现幻觉或异常输出。
- **可能的风险**：项目较新（2026-04 创建），审计标准本身可能不成熟；若用于真实交易 Agent 审计，需验证其评估指标是否足够严格，避免“审计通过”造成虚假安全感。

### 3.2 TauricResearch/TradingAgents

- **项目解决什么问题**：提供多智能体 LLM 金融交易框架，将交易决策拆分为多个 Agent 角色协同完成。
- **为什么最近值得关注**：111958 stars，7d +1257，是候选集中最成熟的 AI 交易框架之一。LLM 多智能体交易正从实验走向可复现框架。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 为 agent、finance、llm、multiagent、trading。架构核心是多角色 Agent 协同，典型设计可能包括基本面分析 Agent、技术分析 Agent、情绪分析 Agent、风控 Agent、决策 Agent 等，通过 LLM 汇总形成交易信号。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其多角色分工模式可直接迁移到企业级投研 Agent 框架，例如将“研究员—风控—决策—执行”角色化，并加入审计与留痕机制。
- **可能的风险**：LLM 交易信号存在幻觉与过拟合风险；多 Agent 框架的决策链路越长，延迟与不确定性越高；回测结果可能因 LLM 的非确定性而难以复现。

### 3.3 HKUDS/Vibe-Trading

- **项目解决什么问题**：定位为“个人交易 Agent”，融合 AI Agent、回测、MCP、多智能体与量化金融。
- **为什么最近值得关注**：35851 stars，7d +595。HKUDS 出品，学术背景较强，且 topics 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent，是“AI Agent + 交易 + MCP”融合的典型样本。
- **技术栈/架构亮点**：Python + MIT。MCP 集成意味着其数据源、交易接口可能以 MCP server 形式接入，架构上更模块化、可扩展。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。可重点研究其 MCP 集成方式与多 Agent 交易决策流程，作为企业级交易 Agent 的参考实现。
- **可能的风险**：crypto_related 标记，涉及加密交易；“vibe trading”概念本身偏营销，需警惕策略过拟合与回测美化；不建议直接用于实盘。

### 3.4 rootSunc/CNEquity

- **项目解决什么问题**：中国 A 股数据基础设施，提供 55 个日更数据集，覆盖行情、基本面、期货、资金面、公告事件、指数行业、宏观与风险，强调行级溯源、PIT 语义、复权与历史成分内置，MCP 原生，自托管、零注册、零 API Token。
- **为什么最近值得关注**：虽然 stars 仅 708，但 7d +354，增速快。其“PIT 语义 + Parquet/DuckDB + MCP 原生”的设计直击量化回测中数据偏差与未来函数痛点。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 包含 duckdb、parquet、polars、point-in-time、mcp、akshare、tushare。架构上以 Parquet 为存储、DuckDB 为查询引擎、Polars 为计算层，MCP 原生支持 Agent 直接调用，是典型的现代本地优先数据湖架构。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。PIT 语义与行级溯源是量化数据工程的关键能力，可借鉴其数据模型设计，为 Agent 提供可信、可追溯的金融数据底座。
- **可能的风险**：项目较新，数据源依赖 akshare/tushare 等第三方，数据质量与稳定性需验证；stars 基数低，社区维护活跃度待观察。

### 3.5 shy3130/tick-stock-panel

- **项目解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，LLM 能力驱动策略定制、个股分析与复盘，支持自由接入第三方数据源。
- **为什么最近值得关注**：6069 stars，24h +124，增速较快。其“自托管 + LLM + 回测 + 监控”一体化设计是个人量化工作台的典型形态。
- **技术栈/架构亮点**：Python + MIT。topics 包含 duckdb、fastapi、polars、react、backtesting、ai-agent。架构为 FastAPI 后端 + React 前端 + DuckDB/Polars 数据层，LLM 用于策略定制与个股分析，是轻量级全栈量化工作台。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。可借鉴其“LLM 辅助策略生成 + 本地回测 + 监控面板”的产品形态，快速搭建内部投研工具原型。
- **可能的风险**：A 股数据合规与接口稳定性风险；LLM 生成的策略需严格回测验证，避免过拟合；自托管部署对用户技术能力有一定要求。

### 3.6 virattt/ai-hedge-fund

- **项目解决什么问题**：模拟“AI 对冲基金团队”，用多个 AI Agent 扮演不同投资角色协同决策。
- **为什么最近值得关注**：64081 stars，是 AI 投资决策 Agent 的标杆项目之一。虽然近期涨星放缓（7d +140），但架构思想仍具参考价值。
- **技术栈/架构亮点**：Python + MIT。无 topics 信息，但项目核心是“多 Agent 角色扮演 + 投资决策”，通常包括价值投资、成长投资、量化分析、风控等角色。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。可借鉴其角色分工与决策汇总机制，但需注意其定位更偏研究/教育，而非生产级交易系统。
- **可能的风险**：likely_research_tool 标记，定位为研究工具；LLM 决策存在幻觉与过拟合风险；不建议直接用于实盘交易。

### 3.7 OpenByteInc/QuantDinger

- **项目解决什么问题**：定位为“开源 AI Trading OS”，支持 agent trading、vibe trading，可研究、构建 Python 策略、回测、paper/live 交易，覆盖 crypto、stocks、forex，并可启动多租户交易 SaaS。
- **为什么最近值得关注**：12906 stars，7d +217。其“交易 OS + 多租户 SaaS”定位在候选集中较为独特，展示了交易系统产品化的思路。
- **技术栈/架构亮点**：Python + Apache-2.0。topics 包含 alpaca、binance、mcp-server、saas、backtesting、typesafe-ai。架构上集成了多交易所接口、MCP server、回测与 SaaS 多租户能力。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：可借鉴其“交易能力产品化 + 多租户 SaaS”思路，但需注意其描述中“vibe trading”“launch your own SaaS”等营销措辞，实际能力需代码级验证。
- **可能的风险**：crypto_related，涉及加密交易；多交易所 API key 管理风险；SaaS 多租户涉及资金结算与合规，风险较高；不建议直接用于实盘。

### 3.8 freqtrade/freqtrade

- **项目解决什么问题**：免费开源加密交易机器人，支持回测与实盘交易。
- **为什么最近值得关注**：55587 stars，是加密交易机器人领域最成熟的开源项目之一，持续活跃（近 30 天有 push）。
- **技术栈/架构亮点**：Python + GPL-3.0。topics 包含 algorithmic-trading、telegram-bot、trading-bot。架构成熟，支持策略回测、Telegram 控制、多交易所接入。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：可借鉴其策略抽象、回测框架与交易所适配层设计，但 GPL-3.0 许可证对企业闭源使用有限制。
- **可能的风险**：crypto_related + trading_bot，涉及加密交易；实盘交易存在资金风险；GPL-3.0 许可证合规风险；不建议输入真实交易所 API key。

### 3.9 openbq-org/OpenBB

- **项目解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、加密、衍生品、固定收益、经济数据等。
- **为什么最近值得关注**：74416 stars，7d +284。作为金融数据中台，其“面向 AI Agent”的定位与当前 Agent 化趋势契合。
- **技术栈/架构亮点**：Python。topics 覆盖 ai、crypto、derivatives、equity、fixed-income、options、quantitative-finance。架构上提供统一数据接口，支持多种资产类别。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。可作为企业级投研 Agent 的数据层参考，研究其数据标准化与多资产接入方式。
- **可能的风险**：crypto_related；数据源依赖第三方，稳定性与许可需关注；许可证为 Other，企业使用需确认条款。

### 3.10 CopilotKit/OpenBot

- **项目解决什么问题**：开源 AI 同事，每个 Agent 拥有自己的计算机（浏览器、文件、工具），每个动作在执行前被决定、执行后被记录，支持任意 AG-UI Agent。
- **为什么最近值得关注**：6646 stars，7d +281。其“动作前决策 + 动作后记录”的治理机制对金融 Agent 的审计与合规有直接借鉴意义。
- **技术栈/架构亮点**：TypeScript + MIT。topics 包含 ag-ui、agent-governance、browser-automation、generative-ui、mcp。架构强调 Agent 治理与操作留痕。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。可借鉴其“决策前审批 + 操作后审计”机制，为交易 Agent 增加操作留痕与合规审计能力。
- **可能的风险**：trading_bot 标记，但实际更偏通用 Agent 框架；浏览器自动化在金融场景中可能触发反爬与合规问题。

## 4. 趋势归纳

### 技术趋势

1. **MCP 原生金融数据层**：CNEquity、Vibe-Trading、QuantDinger 等项目将 MCP 作为数据与交易能力的标准接入方式，金融数据基础设施正在向 Agent 友好型演进。
2. **本地优先 + 零信任数据工程**：DuckDB、Parquet、Polars 成为新一批金融数据项目的事实标准，强调自托管、零 API Token、PIT 语义与行级溯源。
3. **LLM 推理轻量化**：colibri（纯 C MoE 推理）、BitNet（1-bit LLM）、project-maya（本地 GLM-5.3 MoE）等项目显示，本地运行大模型的门槛正在降低，为金融场景的私有化 LLM 部署提供可能。
4. **Agent 技能包生态爆发**：大量项目以“skills”形式出现（ui-ux-pro-max-skill、agentic-awesome-skills、AI-Research-SKILLs 等），Agent 能力正在被标准化、模块化、可复用化。

### 产品趋势

1. **AI Agent 审计与治理产品化**：iFixAi 将 Agent 审计从概念变为可运行工具，未来金融 Agent 产品可能内置审计与合规模块。
2. **自托管个人金融终端**：aurelio-finance、tick-stock-panel、FinceptTerminal 等项目显示，个人金融管理与量化工作台正在向自托管、本地优先方向演进。
3. **交易系统 SaaS 化**：QuantDinger 提出“多租户交易 SaaS”概念，交易能力正在被产品化。

### 量化/交易策略趋势

1. **LLM 多智能体交易决策**：TradingAgents、Vibe-Trading、ai-hedge-fund 等项目持续演进，LLM 多角色协同决策成为主流范式。
2. **金融基础模型**：Kronos 定位为“金融市场语言的基础模型”，显示金融领域正在尝试预训练专用模型。
3. **回测与数据质量并重**：CNEquity 的 PIT 语义、tick-stock-panel 的回测集成，显示行业对回测数据质量与未来函数问题的重视。

### AI Agent 与自动化交易结合趋势

1. **从“AI 辅助交易”到“AI Agent 交易 OS”**：QuantDinger、Vibe-Trading 等项目试图将 AI Agent 作为交易系统的核心，而非辅助工具。
2. **Agent 治理与交易风控融合**：iFixAi 的审计能力与 OpenBot 的操作留痕机制，为交易 Agent 的合规与风控提供了新思路。
3. **MCP 成为 Agent 与金融数据/交易接口的标准桥梁**：多个项目同时支持 MCP，显示 Agent 与金融系统的集成正在标准化。

### 值得后续做原型验证的方向

1. **交易 Agent 决策审计流水线**：借鉴 iFixAi，为交易 Agent 增加“决策前审计 + 决策后复盘”模块。
2. **PIT 语义金融数据湖**：借鉴 CNEquity，构建支持 PIT 语义、行级溯源的本地金融数据底座。
3. **MCP 原生量化工作台**：借鉴 tick-stock-panel + Vibe-Trading，构建以 MCP 为集成标准的自托管量化工作台。
4. **多角色 LLM 投研 Agent**：借鉴 TradingAgents + ai-hedge-fund，构建企业级多角色投研 Agent 框架。

## 5. 今日灵感清单

1. **MVP：交易 Agent 决策审计器**。借鉴 iFixAi，做一个轻量级 CLI 工具，对交易 Agent 的每次决策输出进行规则检查（如是否违反预设风控规则、是否出现幻觉、是否偏离策略目标），输出审计报告。可先用 Python + 规则引擎实现，后续接入 LLM 评估。

2. **MVP：PIT 语义金融数据湖**。借鉴 CNEquity，用 DuckDB + Parquet + Polars 构建一个本地 A 股数据湖，重点实现 PIT 语义与行级溯源，验证“无未来函数”回测数据底座。可先覆盖日线行情与基本面数据。

3. **调研：MCP 在金融数据与交易接口中的标准化程度**。调研 awesome-mcp-servers、awesome-remote-mcp-servers 中与金融相关的 MCP server，评估其数据质量、接口稳定性与安全风险，形成内部选型报告。

4. **Demo：多角色 LLM 投研 Agent**。借鉴 TradingAgents，用 Codex/Claude 复现一个简化版多角色投研 Agent（研究员、风控、决策三角色），输入股票代码，输出结构化投研报告与决策建议，全程留痕。

5. **原型：自托管个人金融 AI 顾问**。借鉴 aurelio-finance，做一个本地优先的个人净值追踪 + AI 财务顾问 MVP，重点验证“本地数据 + LLM 分析”的产品体验，不接入真实交易。

6. **调研：本地 LLM 推理在金融场景的可行性**。调研 colibri、BitNet、project-maya 等本地推理方案，评估在消费级硬件上运行金融分析 LLM 的可行性与成本，形成技术选型报告。

7. **Demo：Agent 操作留痕与审计**。借鉴 OpenBot，为现有 Agent 框架增加“动作前审批 + 动作后记录”机制，用 Codex 复现一个带审计日志的浏览器自动化 Agent demo。

8. **Watchlist：iFixAi、CNEquity、tick-stock-panel、TradingAgents、Vibe-Trading**。这些项目在 Agent 治理、数据工程、量化工作台、多智能体交易等方向具有持续跟踪价值。

9. **原型：金融数据 MCP server**。借鉴 CNEquity 的 MCP 原生设计，将内部金融数据封装为 MCP server，验证 Agent 直接调用金融数据的能力与安全性。

10. **调研：AI 技能包（skills）在金融场景的复用性**。调研 agentic-awesome-skills、AI-Research-SKILLs、anbeime/skill 等技能库中与金融相关的技能，评估其质量与可复用性，筛选可引入内部 Agent 框架的技能。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计与治理的标杆项目，涨星极快，与金融风控场景高度契合，值得持续跟踪其审计维度与合规框架演进。 |
| TauricResearch/TradingAgents | 最成熟的 LLM 多智能体交易框架之一，持续活跃，是研究 AI 交易 Agent 架构的首选参考。 |
| HKUDS/Vibe-Trading | 学术背景 + MCP 集成 + 多智能体交易，是“AI Agent + 交易 + MCP”融合的典型样本。 |
| rootSunc/CNEquity | PIT 语义 + Parquet/DuckDB + MCP 原生的 A 股数据基础设施，直击量化数据质量痛点，虽 stars 低但架构思想先进。 |
| shy3130/tick-stock-panel | 自托管 A 股量化工作台，FastAPI + Polars + DuckDB + React 全栈架构清晰，适合作为内部工具原型参考。 |
| virattt/ai-hedge-fund | AI 多角色投资决策的标杆项目，虽涨星放缓，但架构思想仍具长期参考价值。 |
| CopilotKit/OpenBot | Agent 治理与操作留痕机制对金融 Agent 合规有直接借鉴意义。 |
| openbq-org/OpenBB | 面向 AI Agent 的金融数据平台，数据标准化与多资产接入方式值得跟踪。 |
| freqtrade/freqtrade | 最成熟的加密交易机器人之一，策略抽象与回测框架设计值得长期跟踪。 |
| OpenByteInc/QuantDinger | “交易 OS + 多租户 SaaS”定位独特，可观察交易系统产品化趋势，但需谨慎验证其真实能力。 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-10-17）与 `baseline_7d`（2026-10-11），1 日与 7 日涨星数据完整，未缺失基线。
- **30 日基线**：所有项目的 `star_delta_30d` 均为 null，说明本次采集未提供 30 日涨星数据，无法进行月度趋势分析。
- **采集失败**：未发现明确的采集失败标记，但部分项目（如 Financial_freedom、BitNet）的 `pushed_at` 超过 30 天，仅满足“近 90 天有 push”条件，其近期活跃度需谨慎解读。
- **样本偏差**：候选集存在明显的关键词误匹配噪声。大量“awesome-list”类项目（public-apis、awesome-selfhosted、awesome-python、awesome-go、build-your-own-x 等）因描述或 readme 中偶然出现“trading bot”“quant”“crypto trading”等关键词而被纳入，实际与金融/量化交易关联较弱。这导致 Top 榜单中资源列表类项目占比偏高，真实金融/量化项目被稀释。分析时应重点关注 category_guess 与 topics 中明确包含 trading、quant、finance、backtesting 等字段的项目。
- **风险标记**：部分项目的 `risk_flags` 包含 `crypto_related`、`trading_bot`、`likely_research_tool` 等标记，这些标记来自采集方的自动分类，仅作为风险提示参考，不代表项目本身存在安全问题。
