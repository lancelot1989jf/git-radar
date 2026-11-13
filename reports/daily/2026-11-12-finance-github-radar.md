# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-12

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的多市场股票分析系统**：`ZhuLinsen/daily_stock_analysis` 以 24h +403、7d +3510 的涨星领跑，融合多源行情、实时新闻、决策看板与自动推送，是 AI 交易分析产品化的典型样本。
  2. **AI Agent 技能生态爆发**：`day-trader-skill`、`trader-skill`、`ui-ux-pro-max-skill` 等项目显示“Claude/Codex Skill”正在成为新的分发单元，交易决策、UI 设计、安全审计都被打包成可复用技能。
  3. **AI Agent 治理与审计**：`iFixAi` 以“AI Agent 独立审计”切入，覆盖 EU AI Act、ISO 42001、NIST AI RMF 等合规框架，反映 Agent 进入生产环境后的治理需求。

- **是否出现新趋势**：是。出现明显的“**Agent Skill 化**”趋势——交易策略、研究流程、UI 生成、安全审计都被封装为可插拔的 Claude/Codex Skill，而非传统单体应用。同时，“**本地优先 + 零成本定时运行**”成为个人量化工具的新卖点。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的多源数据融合 + LLM 决策看板 + 定时推送架构；`colibri` 的 MoE 模型分层推理引擎（GPU/RAM/NVMe 三级缓存）；`headroom` 的 LLM 上下文压缩代理；`OpenBot` 的“每个 Agent 一台电脑”的浏览器自动化治理架构，均值得深入研究。

- **是否有明显骗局、过度营销或高风险项目**：本次候选列表中未发现明显骗局项目。但需注意：`day-trader-skill` 与 `trader-skill` 的营销话术较强（“never place an order without your yes”），且属于交易决策辅助工具，存在被误用为自动交易信号源的风险。`Wallet-Risk-Scanner` 7 日涨星 +722 但 24h 涨星为 0，需警惕短期热度异常。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 71138 | +403 | +3510 | Python | AI交易/数据工程 | LLM 驱动的多市场股票分析系统 | 高 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 148818 | +479 | +2966 | Python | 金融产品/AI技能 | 多平台 UI/UX 设计智能技能 | 中 | 低 |
| 3 | awesome-selfhosted/awesome-selfhosted | 336547 | +302 | +2331 | 无 | 自托管清单 | 自托管网络服务清单 | 低 | 中 |
| 4 | JustVugg/colibri | 50554 | +505 | +2320 | C | 量化研究 | MoE 模型分层推理引擎 | 高 | 低 |
| 5 | public-apis/public-apis | 498596 | +251 | +2095 | Python | 数据工程 | 免费 API 集合清单 | 中 | 中 |
| 6 | codecrafters-io/build-your-own-x | 562201 | +244 | +1976 | Markdown | 教程清单 | 从零重建技术的教程集合 | 低 | 中 |
| 7 | Jakeschincariol/day-trader-skill | 7472 | +287 | +1845 | Python | 回测/风控 | 11 个日内交易 Claude 技能 | 高 | 低 |
| 8 | vinta/awesome-python | 334400 | +240 | +1567 | Python | 量化研究 | Python 工具精选清单 | 低 | 低 |
| 9 | awesome-dsh-plugin/awesome-dsh-plugin | 24499 | +123 | +1525 | JavaScript | 交易基础设施 | DeepSeek Harness 插件清单 | 中 | 低 |
| 10 | CopilotKit/OpenBot | 11850 | +701 | +1563 | TypeScript | 金融产品/交易机器人 | 开源 AI 同事，每个 Agent 一台电脑 | 高 | 中 |
| 11 | VoltAgent/awesome-design-md | 127301 | +224 | +1474 | 无 | 金融产品 | 品牌设计系统 DESIGN.md 集合 | 中 | 中 |
| 12 | TauricResearch/TradingAgents | 122359 | +186 | +1484 | Python | AI交易/回测 | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 13 | ifixai-ai/iFixAi | 45164 | +135 | +1461 | Python | AI交易/风控 | AI Agent 独立审计工具 | 高 | 低 |
| 14 | avelino/awesome-go | 193616 | +205 | +1306 | Go | 交易基础设施 | Go 框架与库精选清单 | 低 | 中 |
| 15 | nexu-io/open-design | 107428 | +154 | +1244 | TypeScript | 金融产品 | 协作式 AI 设计 Agent 工作区 | 中 | 低 |
| 16 | garrytan/gbrain | 32805 | +79 | +1243 | TypeScript | 金融产品 | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 17 | ripienaar/free-for-dev | 142723 | +72 | +709 | HTML | 金融产品 | 开发者免费 SaaS/PaaS 清单 | 低 | 低 |
| 18 | kaankiziltug/logo-design-skill | 6769 | +94 | +687 | HTML | 金融产品 | Logo 设计 AI 技能 | 低 | 低 |
| 19 | headroomlabs-ai/headroom | 79519 | +110 | +556 | Python | AI交易/风控 | LLM 上下文压缩代理 | 高 | 低 |
| 20 | jaywcjlove/awesome-mac | 118412 | +87 | +580 | Swift | 交易基础设施 | macOS 软件精选清单 | 低 | 低 |
| 21 | PurpleDoubleD/locally-uncensored | 4119 | +207 | +673 | TypeScript | AI交易/量化研究 | 本地 AI 工作室桌面应用 | 中 | 低 |
| 22 | ruvnet/ruflo | 81595 | +73 | +580 | TypeScript | AI交易/回测 | 多智能体 swarm 编排框架 | 高 | 低 |
| 23 | hesreallyhim/awesome-claude-code | 57893 | +74 | +539 | Python | AI交易/量化研究 | Claude Code 资源精选清单 | 低 | 低 |
| 24 | shiyu-coder/Kronos | 47711 | +56 | +737 | Python | 回测/量化研究 | 金融市场基础模型 | 高 | 低 |
| 25 | shy3130/tick-stock-panel | 7679 | +61 | +508 | Python | AI交易/回测 | A 股自托管量化工作台 | 高 | 低 |
| 26 | punkpeye/awesome-remote-mcp-servers | 3100 | +66 | +422 | 无 | AI交易/交易基础设施 | 远程 MCP 服务器集合 | 中 | 中 |
| 27 | HKUDS/Vibe-Trading | 38128 | +48 | +383 | Python | AI交易/回测 | 个人交易 Agent 框架 | 高 | 低 |
| 28 | sickn33/agentic-awesome-skills | 49624 | +46 | +391 | Python | 回测 | 2955+ 可复用 AI Agent 技能库 | 中 | 低 |
| 29 | elementalsouls/Claude-BugHunter | 5646 | +117 | +196 | Python | 金融产品 | Claude 漏洞挖掘技能包 | 中 | 低 |
| 30 | punkpeye/awesome-mcp-servers | 97671 | +40 | +318 | 无 | 金融产品 | MCP 服务器集合 | 中 | 低 |
| 31 | Soniavasseur/Wallet-Risk-Scanner | 914 | 0 | +722 | Python | 加密交易/风控 | 多链加密钱包风险扫描器 | 高 | 中 |
| 32 | Jakeschincariol/trader-skill | 1760 | +48 | +369 | Python | 金融产品 | 11 个投资者复刻 Claude 技能 | 中 | 低 |
| 33 | Orkas-AI/Orkas | 9315 | +44 | +268 | JavaScript | 回测 | 本地优先 AI 团队桌面应用 | 中 | 低 |
| 34 | nidhinjs/prompt-master | 15896 | +34 | +321 | 无 | AI交易/金融产品 | 精准提示词生成技能 | 低 | 低 |
| 35 | aardappel/goose | 3475 | +26 | +374 | C++ | 交易基础设施 | Goose 编程语言 | 低 | 低 |
| 36 | openbq-org/OpenBB | 75381 | +24 | +256 | Python | 加密交易/量化研究 | 分析师与 AI Agent 开放数据平台 | 高 | 中 |
| 37 | awesomedata/awesome-public-datasets | 80092 | +42 | +134 | 无 | 加密交易 | 高质量公开数据集清单 | 中 | 中 |
| 38 | MakazhanAlpamys/Soup | 10511 | +26 | +290 | Python | AI交易/量化研究 | 单 YAML 微调 LLM 工具 | 中 | 低 |
| 39 | zandy700/supply-chain-shock-map | 328 | +35 | +325 | JavaScript | 回测 | 供应链冲击传导预测与事件研究 | 高 | 低 |
| 40 | code-yeongyu/oh-my-openagent | 70887 | +23 | +149 | TypeScript | 量化研究 | 图工程 Agent 编排工具 | 中 | 低 |
| 41 | rust-unofficial/awesome-rust | 60496 | +27 | +146 | Rust | 量化研究 | Rust 资源精选清单 | 低 | 中 |
| 42 | Developer-Y/cs-video-courses | 84824 | +2 | +222 | 无 | 量化研究 | CS 视频课程清单 | 低 | 中 |
| 43 | fffaraz/awesome-cpp | 74389 | +23 | +124 | 无 | 量化研究 | C/C++ 资源精选清单 | 低 | 低 |
| 44 | virattt/ai-hedge-fund | 64652 | +12 | +140 | Python | 回测/风控 | AI 对冲基金团队模拟 | 高 | 低 |
| 45 | josephmisiti/awesome-machine-learning | 74813 | +10 | +48 | Python | AI交易 | ML 框架与库精选清单 | 低 | 低 |
| 46 | vuejs/awesome-vue | 73475 | -4 | -7 | 无 | 量化研究 | Vue.js 资源精选清单 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：24h +403、7d +3510 的涨星速度极快，说明“LLM + 股票分析 + 定时推送”的产品形态有强需求。MIT 协议、Python 实现，适合直接研究。
- **技术栈/架构亮点**：多源行情接入、实时新闻流、LLM 决策生成、看板可视化、定时任务调度。零成本运行的设计思路值得借鉴。
- **是否适合借鉴**：非常适合。可借鉴其“数据采集 → LLM 分析 → 看板/推送”的流水线架构，用于构建企业级投研 Agent 或自动化研报生成系统。
- **可能风险**：金融合规风险（个股分析可能涉及投资建议）；LLM 输出幻觉可能导致错误决策；数据源稳定性与授权问题。

### 3.2 JustVugg/colibri
- **解决什么问题**：在消费级硬件上运行前沿 MoE 模型，通过 GPU/RAM/NVMe 三级分层推理降低显存门槛。
- **为什么值得关注**：24h +505 涨星，C 语言实现，Apache-2.0 协议。对量化研究中的本地 LLM 部署有直接价值。
- **技术栈/架构亮点**：分层推理引擎——热专家驻留 GPU（CUDA/Vulkan）、温专家驻留 RAM、冷专家从 NVMe 流式加载。这种“分层缓存 + 按需加载”思想可迁移到金融数据缓存、策略参数管理。
- **是否适合借鉴**：适合。可借鉴其分层存储思想，设计量化研究中的“热数据/温数据/冷数据”缓存架构，或本地 LLM 推理的降本方案。
- **可能风险**：项目较新（2026-07 创建），维护活跃度待观察；C 语言实现复杂度高，二次开发门槛高。

### 3.3 Jakeschincariol/day-trader-skill
- **解决什么问题**：将日内交易流程拆解为 11 个 Claude 技能，包括图表扫描、新闻跟踪、进出场时机、交易复盘。
- **为什么值得关注**：7d +1845 涨星，是“交易 Skill 化”趋势的代表。营销话术强调“never place an order without your yes”，即保留人工确认环节。
- **技术栈/架构亮点**：基于 Claude Skills 的模块化设计，每个技能独立负责一个交易环节。这种“技能即流程节点”的设计值得研究。
- **是否适合借鉴**：适合。可借鉴其将复杂交易流程拆解为可组合技能的方法，用于构建企业级投研 Agent 的技能库。但需注意其“人工确认”设计是风控关键，不应移除。
- **可能风险**：策略过拟合风险；用户可能误将其输出作为自动交易信号；技能质量依赖 Claude 模型能力，存在幻觉风险。

### 3.4 TauricResearch/TradingAgents
- **解决什么问题**：多 Agent LLM 金融交易框架，模拟分析师、研究员、交易员等多角色协作。
- **为什么值得关注**：122k stars，Apache-2.0，是 AI 交易 Agent 领域的标杆项目。7d +1484 涨星显示持续热度。
- **技术栈/架构亮点**：多 Agent 角色分工（分析师、研究员、交易员、风控），LLM 驱动的决策链。架构清晰，适合作为多 Agent 交易系统的参考实现。
- **是否适合借鉴**：非常适合。可借鉴其多 Agent 角色设计与决策流程，用于构建企业级投研 Agent 或风控 Agent 框架。
- **可能风险**：研究工具属性强，不应直接用于实盘；LLM 决策的不可解释性；回测结果可能过拟合。

### 3.5 ifixai-ai/iFixAi
- **解决什么问题**：AI Agent 独立审计，回答“Agent 是否在做它该做的事”，覆盖 EU AI Act、ISO 42001、NIST AI RMF 等合规框架。
- **为什么值得关注**：45k stars，7d +1461 涨星。AI Agent 治理是 2026 年的重要主题，尤其对金融领域 Agent 的合规审计有直接价值。
- **技术栈/架构亮点**：支持人工或 Agent 自审计，120 秒内给出结论。覆盖幻觉检测、提示注入、LLM 安全等维度。Apache-2.0 协议。
- **是否适合借鉴**：非常适合。金融交易 Agent 的合规审计是刚需，可借鉴其审计维度设计，构建交易 Agent 的“上线前审计”流程。
- **可能风险**：审计标准仍在演进；对复杂金融 Agent 的审计深度可能不足；需结合具体业务场景定制。

### 3.6 CopilotKit/OpenBot
- **解决什么问题**：开源 AI 同事框架，每个 Agent 拥有独立的浏览器、文件和工具，所有动作在执行前决策、执行后记录。
- **为什么值得关注**：24h +701 涨星（今日最高），TypeScript 实现，MIT 协议。AG-UI 标准、MCP 集成、agent-governance 是其核心标签。
- **技术栈/架构亮点**：“动作前决策 + 动作后记录”的治理模式，浏览器自动化 + 生成式 UI。这种“可审计的 Agent 执行环境”对金融自动化交易有重要参考价值。
- **是否适合借鉴**：适合。可借鉴其 Agent 治理与审计机制，设计交易 Agent 的“决策留痕 + 执行审计”架构。但需注意其定位是通用 Agent 框架，非交易专用。
- **可能风险**：浏览器自动化在金融场景中的安全风险；Agent 权限过大可能导致误操作；需严格限制交易相关权限。

### 3.7 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 处理前压缩工具输出、日志、文件和 RAG 块，减少 token 消耗（编码 Agent 省 20%，JSON 省 60-95%）。
- **为什么值得关注**：79k stars，7d +556 涨星。对金融量化场景中大量 JSON 行情数据、日志数据的 LLM 处理有直接降本价值。
- **技术栈/架构亮点**：库 + 代理 + MCP 服务器三种形态，支持 FastAPI、LangChain、OpenAI、Anthropic 等生态。上下文工程是 AI Agent 成本控制的关键。
- **是否适合借鉴**：非常适合。量化研究中的 LLM 分析（如新闻情感、财报解读）可集成此压缩层，降低 token 成本。
- **可能风险**：压缩可能损失关键信息，需验证对金融数据精度的影响；依赖上游 LLM 生态变化。

### 3.8 shy3130/tick-stock-panel
- **解决什么问题**：A 股自托管、零运维的“自建策略 + 监控 + 回测”量化工作台，LLM 驱动策略定制与个股分析。
- **为什么值得关注**：7d +508 涨星，DuckDB + Polars + FastAPI + React 技术栈，是 A 股量化工具现代化的代表。
- **技术栈/架构亮点**：DuckDB 做本地分析、Polars 做数据处理、FastAPI 做后端、React 做前端，LLM 驱动策略定制。技术栈现代且轻量。
- **是否适合借鉴**：非常适合。可借鉴其“本地优先 + 零运维 + LLM 辅助”的设计，构建个人或小团队量化研究工作台。
- **可能风险**：A 股数据合规问题；LLM 生成策略的过拟合风险；自托管环境的数据安全。

### 3.9 Soniavasseur/Wallet-Risk-Scanner
- **解决什么问题**：多链加密钱包风险扫描，AML/KYT 筛查，0-100 评分，集成 6 个情报提供商，支持 15+ 链。
- **为什么值得关注**：7d +722 涨星但 24h 为 0，热度异常需关注。AML/KYT 是加密交易合规的刚需。
- **技术栈/架构亮点**：多情报源 failover、制裁筛查、欺诈合约检测、资金追踪、批量筛查、多格式报告。Python 跨平台。
- **是否适合借鉴**：适合。可借鉴其多源情报融合与风险评分模型，用于构建交易对手方风险筛查或合规检查工具。
- **可能风险**：项目较新（2026-09 创建），stars 仅 914，维护活跃度待验证；情报源质量与授权问题；24h 涨星为 0 可能暗示热度不可持续。

### 3.10 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作进行投资决策。
- **为什么值得关注**：64k stars，是 AI 交易 Agent 的经典教学项目。虽然近期涨星放缓（24h +12），但架构仍有参考价值。
- **技术栈/架构亮点**：多 Agent 角色模拟（如基金经理、分析师、交易员），Python 实现，MIT 协议。
- **是否适合借鉴**：适合作为教学参考，理解多 Agent 交易决策的基本架构。但不宜直接用于实盘。
- **可能风险**：模拟环境与实盘差距大；策略过拟合；缺乏真实风控模块。

## 4. 趋势归纳

### 技术趋势
1. **Agent Skill 化**：交易策略、研究流程、UI 生成、安全审计都被封装为可插拔的 Claude/Codex Skill，成为新的软件分发单元。
2. **本地优先 + 零成本运行**：`daily_stock_analysis`、`tick-stock-panel`、`locally-uncensored` 等项目强调本地运行、零运维、零成本，反映个人开发者和中小团队对成本敏感的需求。
3. **LLM 上下文工程**：`headroom` 的 token 压缩、`colibri` 的分层推理，都在解决 LLM 应用的成本与性能瓶颈。
4. **Agent 治理与审计**：`iFixAi`、`OpenBot` 的 agent-governance 标签显示，Agent 进入生产环境后的可审计性成为刚需。

### 产品趋势
1. **从工具到工作台**：`daily_stock_analysis`、`tick-stock-panel` 不再是单一策略脚本，而是集数据、分析、看板、推送于一体的工作台。
2. **技能市场生态**：`agentic-awesome-skills`（2955+ 技能）、`awesome-claude-code`、`awesome-dsh-plugin` 等项目显示技能发现与分发成为独立赛道。
3. **AI 设计协作**：`open-design`、`ui-ux-pro-max-skill`、`awesome-design-md` 显示 AI Agent 正在进入 UI/UX 设计领域，对金融产品的前端开发有间接影响。

### 量化/交易策略趋势
1. **LLM 多 Agent 决策**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 均采用多 Agent 角色分工，LLM 驱动的决策链成为主流范式。
2. **事件驱动研究**：`supply-chain-shock-map` 将新闻事件与供应链冲击传导结合，做事件研究回测，显示量化研究正在向“新闻驱动 + 图分析”方向扩展。
3. **基础模型进入金融领域**：`Kronos` 定位为“金融市场语言基础模型”，显示金融领域的专用基础模型探索仍在继续。

### AI Agent 与自动化交易结合趋势
1. **人工确认作为风控关键**：`day-trader-skill` 强调“never place an order without your yes”，显示 AI 交易 Agent 的设计正在从“全自动”向“人机协作”回摆。
2. **Agent 审计前置**：`iFixAi` 的兴起表明，交易 Agent 上线前的合规审计正在成为标准流程。
3. **MCP 成为数据接入标准**：`awesome-mcp-servers`、`awesome-remote-mcp-servers` 的持续增长显示，MCP 正在成为 Agent 连接金融数据源的标准协议。

### 值得后续做原型验证的方向
1. **交易 Agent 技能库**：将交易研究流程拆解为可组合的 Claude/Codex Skill，支持人工确认环节。
2. **LLM 上下文压缩在金融数据中的应用**：验证 `headroom` 类压缩对行情 JSON、财报文本的 token 节省效果与信息保真度。
3. **Agent 审计流水线**：基于 `iFixAi` 的审计维度，构建交易 Agent 的“上线前审计 + 运行中监控”流水线。
4. **本地优先量化工作台**：参考 `tick-stock-panel` 的 DuckDB + Polars + FastAPI 架构，构建轻量级个人量化研究环境。

## 5. 今日灵感清单

1. **MVP：投研 Agent 技能包**：参考 `day-trader-skill` 和 `trader-skill`，将“新闻扫描 → 情感分析 → 标的筛选 → 人工确认”封装为 5-8 个 Claude/Codex Skill，做一个面向 A 股或美股的投研辅助技能包。
2. **调研：MCP 金融数据服务器生态**：基于 `awesome-mcp-servers` 和 `awesome-remote-mcp-servers`，梳理现有金融数据 MCP 服务器的覆盖范围、数据质量与授权模式，寻找空白点。
3. **Demo：LLM 上下文压缩在财报分析中的应用**：用 `headroom` 的思路，对 SEC EDGAR 财报文本做压缩后再送入 LLM，对比 token 消耗与分析质量。
4. **原型：交易 Agent 审计看板**：参考 `iFixAi` 的审计维度，设计一个交易 Agent 的“决策留痕 + 合规检查”看板，记录每次 LLM 决策的输入、输出、风险标记。
5. **复现：多 Agent 交易决策链**：用 `TradingAgents` 的架构，让 Codex/Agent 自动复现一个简化版的多角色交易决策 demo（分析师、风控、交易员三角色）。
6. **调研：MoE 分层推理在量化本地 LLM 部署中的可行性**：研究 `colibri` 的分层推理架构，评估在消费级 GPU 上运行金融 LLM 的可行性。
7. **MVP：供应链冲击事件研究工具**：参考 `supply-chain-shock-map`，做一个基于 GDELT + SEC EDGAR 的供应链冲击事件研究 MVP，验证新闻事件对股价的传导效应。
8. **Watchlist：Wallet-Risk-Scanner**：关注其后续维护与情报源更新，评估是否可集成到加密交易合规流程中。
9. **调研：Agent Skill 分发与版本管理**：研究 `agentic-awesome-skills` 的目录发现、Agent 自主选择与计划预览机制，思考企业级技能库的管理方案。
10. **原型：本地优先 A 股研究工作台**：参考 `tick-stock-panel` 的 DuckDB + Polars 架构，构建一个本地运行的 A 股数据下载、存储、回测一体化环境。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 涨星最快，LLM 股票分析产品形态值得持续跟踪 |
| Jakeschincariol/day-trader-skill | 交易 Skill 化趋势代表，关注其技能设计演进 |
| TauricResearch/TradingAgents | 多 Agent 交易框架标杆，关注其架构迭代 |
| ifixai-ai/iFixAi | AI Agent 审计赛道，金融合规刚需 |
| CopilotKit/OpenBot | Agent 治理与审计机制，24h 涨星最高 |
| headroomlabs-ai/headroom | LLM 上下文压缩，金融数据降本潜力大 |
| shy3130/tick-stock-panel | A 股本地量化工作台，技术栈现代 |
| Soniavasseur/Wallet-Risk-Scanner | 加密 AML/KYT 工具，但需验证热度可持续性 |
| shiyu-coder/Kronos | 金融基础模型探索，长期研究方向 |
| zandy700/supply-chain-shock-map | 事件驱动量化研究新方向，早期项目 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **基线数据**：本次报告使用了 `baseline_1d`（2026-11-11）和 `baseline_7d`（2026-11-05）两个基线文件，1 日与 7 日涨星数据完整。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法提供 30 日趋势分析。
- **采集失败**：未发现明显的采集失败迹象，46 个候选项目均有完整的 stars、涨星、语言等字段。
- **样本偏差**：候选列表由关键词匹配（如 "quant"、"trading bot"、"backtesting"、"fintech" 等）生成，存在明显的**关键词匹配偏差**——大量 awesome-list 类项目（如 `awesome-selfhosted`、`awesome-python`、`awesome-go`）因 README 中包含匹配关键词而被纳入，实际与金融/量化交易的直接相关性较低。这导致 Top 榜单中“清单类”项目占比偏高，真正聚焦金融交易的项目被稀释。
- **分类偏差**：`category_guess` 字段为自动推断，部分项目的分类可能不准确（如 `awesome-selfhosted` 被标记为 trading_bot，但其实际是自托管服务清单）。
- **热度异常**：`Wallet-Risk-Scanner` 的 7d 涨星 +722 但 24h 涨星为 0，可能存在热度不可持续或数据波动，需谨慎解读。
