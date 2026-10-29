# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-28

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：iFixAi 以 24h +1135 星的增速领跑，反映市场对“Agent 是否按预期执行”的审计需求正在爆发，与金融交易场景中的合规、风控高度相关。
  2. **多智能体金融交易框架**：TradingAgents 24h +517、7d +5372，持续高增长，说明 LLM 多 Agent 协作做交易研究/决策的范式仍是当前最热主线。
  3. **本地优先的 Agent 编排与桌面工作台**：Orkas、OpenBot、ruflo 等项目显示“本地优先 + 多 Agent 编排 + 可观测/可治理”正在成为新的工程底座趋势。

- **是否出现新趋势**：出现。AI Agent 的“审计/对齐/治理”从概念走向可运行工具（iFixAi、langfuse、OpenBot 的 agent-governance），与金融交易场景天然契合。另一个趋势是“Skill 商店/技能包”生态快速膨胀，大量项目以 Claude/Codex/Gemini 技能包形式分发能力。

- **是否出现值得复刻/参考的工程架构**：是。TradingAgents 的多 Agent 金融决策框架、iFixAi 的 Agent 审计闭环、QuantDinger 的“研究-回测-模拟-实盘”一体化交易 OS、hyperswitch 的 Rust 支付编排架构，均具备较高参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但需注意：
  - `day-trader-skill` 描述包含“在冒险投入一美元前回放每一次结果”等强营销话术，且项目创建仅约 8 天、7d 基线缺失，需谨慎对待。
  - `QuantDinger` 同时涉及 crypto、多租户交易 SaaS、billing/payments/settlement，工程复杂度高，若直接实盘存在较大资金与合规风险。
  - 多个项目因关键词命中被归入 trading_bot/crypto 分类，但实际是 awesome-list 或通用工具，分类噪声明显。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 142191 | +495 | +3609 | Python | AI 技能/UI 设计 | 面向多平台的 UI/UX 设计智能技能包 | 中：Agent 技能化封装 | 低 |
| 2 | TauricResearch/TradingAgents | 118001 | +517 | +5372 | Python | AI 交易/多 Agent | 多智能体 LLM 金融交易框架 | 高：多 Agent 决策架构 | 低 |
| 3 | awesome-selfhosted/awesome-selfhosted | 331542 | +366 | +2423 | 无 | 自托管清单 | 自托管网络服务与 Web 应用清单 | 低：基础设施选型参考 | 中 |
| 4 | ifixai-ai/iFixAi | 37250 | +1135 | +5297 | Python | AI 审计/风控 | 独立审计 AI Agent 是否按预期执行 | 高：Agent 治理与合规 | 低 |
| 5 | public-apis/public-apis | 493077 | +293 | +1907 | Python | API 清单 | 免费 API 集合清单 | 低：数据源发现 | 中 |
| 6 | vinta/awesome-python | 331004 | +255 | +1688 | Python | Python 清单 | Python 工具选型权威清单 | 低：技术选型参考 | 低 |
| 7 | ruvnet/ruflo | 80020 | +188 | +1765 | TypeScript | Agent 编排 | 多玩家 swarm 与自主工作流编排框架 | 高：Agent 编排底座 | 低 |
| 8 | codecrafters-io/build-your-own-x | 557042 | +322 | +1785 | Markdown | 教程清单 | 从零重建流行技术的教程集合 | 中：系统学习路径 | 中 |
| 9 | nexu-io/open-design | 104699 | +241 | +1554 | TypeScript | AI 设计工作台 | 本地优先的协作式 AI 设计 Agent 工作区 | 中：本地优先协作架构 | 低 |
| 10 | VoltAgent/awesome-design-md | 124330 | +226 | +1540 | 无 | 设计系统清单 | 品牌设计系统 DESIGN.md 文件集合 | 中：Agent 生成 UI 规范 | 中 |
| 11 | JustVugg/colibri | 44774 | +351 | +1526 | C | 模型推理 | 纯 C 零依赖流式 MoE 模型推理引擎 | 中：边缘推理工程 | 低 |
| 12 | awesome-dsh-plugin/awesome-dsh-plugin | 21381 | +197 | +1415 | JavaScript | 插件清单 | DeepSeek Harness 插件精选列表 | 低：插件生态观察 | 低 |
| 13 | avelino/awesome-go | 190913 | +178 | +1238 | Go | Go 清单 | Go 框架与库精选清单 | 低：Go 技术选型 | 中 |
| 14 | Orkas-AI/Orkas | 3295 | +704 | +1149 | JavaScript | 桌面 Agent 团队 | 本地优先桌面 AI 团队，16 个内置专家 Agent | 高：本地 Agent 编排 | 低 |
| 15 | kaankiziltug/logo-design-skill | 5072 | +223 | +1028 | HTML | AI 技能/设计 | Logo 设计技能包，含 1400+ 参考库 | 低：技能包模式 | 低 |
| 16 | HKUDS/Vibe-Trading | 37062 | +122 | +828 | Python | AI 交易/回测 | “Vibe-Trading”个人交易 Agent | 高：LLM 交易 Agent 范式 | 中 |
| 17 | headroomlabs-ai/headroom | 78177 | +115 | +818 | Python | 上下文压缩 | 压缩工具输出/日志/RAG 块以降低 token | 中：Agent 上下文工程 | 低 |
| 18 | CopilotKit/OpenBot | 7700 | +253 | +827 | TypeScript | Agent 治理 | 每个 AI coworker 拥有独立浏览器/文件/工具 | 高：Agent 治理与操作审计 | 中 |
| 19 | shiyu-coder/Kronos | 44031 | +63 | +1093 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融时序基础模型 | 低 |
| 20 | ripienaar/free-for-dev | 140493 | +364 | +591 | HTML | 免费资源清单 | SaaS/PaaS/IaaS 免费层清单 | 低：基础设施成本优化 | 低 |
| 21 | hesreallyhim/awesome-claude-code | 56788 | +89 | +576 | Python | Claude Code 清单 | Claude Code 技能/插件/工具精选 | 中：编码 Agent 生态 | 低 |
| 22 | simonlin1212/Vibe-Research | 3376 | +181 | +607 | TypeScript | 投研工作台 | A 股/美股/港股投研工作台，168 个数据端点 | 高：多市场投研数据工程 | 低 |
| 23 | Developer-Y/cs-video-courses | 84190 | +397 | +465 | 无 | 课程清单 | 计算机科学视频课程清单 | 低：学习资源 | 中 |
| 24 | PurpleDoubleD/locally-uncensored | 2957 | +128 | +498 | TypeScript | 本地 AI 工作室 | 本地全功能 AI 桌面应用 | 中：本地 AI 部署 | 低 |
| 25 | punkpeye/awesome-remote-mcp-servers | 2168 | +76 | +474 | 无 | MCP 清单 | 远程 MCP 服务器集合 | 中：MCP 生态观察 | 中 |
| 26 | langfuse/langfuse | 36670 | +46 | +512 | TypeScript | LLM 可观测 | 开源 Agent eval 与可观测平台 | 高：Agent 可观测/评估 | 低 |
| 27 | ZhuLinsen/daily_stock_analysis | 67234 | +52 | +390 | Python | 股票分析 | LLM 驱动多市场股票智能分析系统 | 高：LLM 投研自动化 | 低 |
| 28 | sickn33/agentic-awesome-skills | 48689 | +57 | +403 | Python | 技能目录 | 2750+ Agentic 技能目录与控制平面 | 中：技能目录架构 | 低 |
| 29 | juspay/hyperswitch | 45522 | +101 | +127 | Rust | 支付编排 | 开源可组合支付平台，PCI 合规 | 高：支付编排与风控 | 低 |
| 30 | punkpeye/awesome-mcp-servers | 97014 | +58 | +291 | 无 | MCP 清单 | MCP 服务器集合 | 低：MCP 生态观察 | 低 |
| 31 | nidhinjs/prompt-master | 15217 | +46 | +399 | 无 | 提示词技能 | 为任意 AI 工具生成准确提示词的技能 | 低：提示词工程 | 低 |
| 32 | goldmansachs/gs-quant | 13795 | +15 | +551 | Python | 量化金融 | Goldman Sachs 量化金融 Python 工具包 | 高：机构级量化工具 | 低 |
| 33 | anbeime/skill | 8847 | +53 | +362 | Python | 技能商店 | 中文 AI Agent 技能商店，自动抓取 GitHub 技能 | 中：技能分发模式 | 低 |
| 34 | OpenByteInc/QuantDinger | 13263 | +63 | +259 | Python | AI 交易 OS | 开源 AI 交易 OS，支持多租户交易 SaaS | 高：交易系统一体化架构 | 中 |
| 35 | openbq-org/OpenBB | 74846 | +35 | +314 | Python | 开放数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高：金融数据平台 | 中 |
| 36 | AIPentest/CyberStrikeAI | 8187 | +72 | +236 | Go | AI 安全 | AI 原生网络安全行动系统 | 中：Agent 安全治理 | 低 |
| 37 | jaywcjlove/awesome-mac | 117293 | +80 | 无 | Swift | macOS 清单 | 高质量 macOS 软件清单 | 低：工具选型 | 低 |
| 38 | garrytan/gbrain | 31316 | +34 | +247 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent Brain | 中：Agent 认知架构 | 低 |
| 39 | Jakeschincariol/day-trader-skill | 2715 | +324 | 无 | Python | 日内交易技能 | 11 个 Claude 日内交易技能 | 中：交易技能封装 | 低 |
| 40 | Orchestra-Research/AI-Research-SKILLs | 14070 | +51 | +270 | TeX | AI 研究技能 | AI 研究与工程技能库 | 中：研究 Agent 技能 | 低 |
| 41 | code-yeongyu/oh-my-openagent | 70451 | +32 | +197 | TypeScript | Agent 编排 | 图工程与 Agent 编排 TUI | 中：Agent 编排交互 | 低 |
| 42 | MakazhanAlpamys/Soup | 9773 | +39 | +236 | Python | LLM 微调 | 单 YAML 微调 LLM，4GB GPU 训练 8B 模型 | 中：低成本微调 | 低 |
| 43 | virattt/ai-hedge-fund | 64332 | +28 | +197 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高：多 Agent 投研模拟 | 低 |
| 44 | Fractal-Compute-Orchestrations/FractalWorkspace | 7220 | +636 | 无 | Python | 联邦学习 | 大规模联邦学习工作区 | 中：分布式学习架构 | 低 |
| 45 | awesomedata/awesome-public-datasets | 79830 | +22 | +164 | 无 | 数据集清单 | 高质量开放数据集清单 | 低：数据源发现 | 中 |
| 46 | rust-unofficial/awesome-rust | 60177 | +19 | +163 | Rust | Rust 清单 | Rust 代码与资源精选 | 低：Rust 技术选型 | 低 |
| 47 | fffaraz/awesome-cpp | 74083 | +15 | +146 | 无 | C++ 清单 | C/C++ 框架与库精选 | 低：C++ 技术选型 | 低 |
| 48 | josephmisiti/awesome-machine-learning | 74686 | +10 | +48 | Python | ML 清单 | 机器学习框架与库精选 | 低：ML 技术选型 | 低 |
| 49 | vuejs/awesome-vue | 73499 | -5 | -15 | 无 | Vue 清单 | Vue.js 精选资源 | 低：前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，用多个角色化 Agent（如研究员、交易员、风控）共同完成分析、决策与复盘。
- **为什么值得关注**：7d +5372 星、24h +517 星，是当前金融 AI Agent 方向增速最快的项目之一；Apache-2.0 协议，近 30 天有 push，维护活跃。
- **技术栈/架构亮点**：Python + 多 Agent 编排；将交易决策拆分为可分工、可辩论的 Agent 角色，天然适合引入审计与制衡机制。
- **是否适合借鉴**：非常适合。可借鉴其“角色化多 Agent + 决策制衡”架构，用于企业级投研 Agent、自动化交易决策支持系统；也可与 iFixAi 类审计工具结合，形成“决策-审计”闭环。
- **可能风险**：作为研究工具，策略有效性未经实盘验证；LLM 决策存在幻觉与过拟合风险；若接入实盘需严格隔离权限。

### 3.2 ifixai-ai/iFixAi
- **解决什么问题**：独立审计 AI Agent 是否按预期执行，回答“Agent 是否在做它该做的事”，可在 120 秒内给出结论。
- **为什么值得关注**：24h +1135 星、7d +5297 星，增速极快；topic 覆盖 AI 治理、ISO 42001、NIST AI RMF、OWASP LLM、提示注入检测等，直击 Agent 合规痛点。
- **技术栈/架构亮点**：Python + CLI；支持人工或 Agent 自审计；覆盖幻觉检测、提示注入、风险评估等维度。
- **是否适合借鉴**：非常适合。金融场景中，任何自动化交易/投研 Agent 都需要审计层；可将其审计思路集成到交易 Agent 的 pre-trade/post-trade 检查环节。
- **可能风险**：审计结论的可靠性依赖评估基准质量；作为较新项目，长期维护与社区成熟度待观察。

### 3.3 HKUDS/Vibe-Trading
- **解决什么问题**：提供“个人交易 Agent”，将 LLM、MCP、多 Agent 与回测结合，降低 AI 交易策略开发门槛。
- **为什么值得关注**：HKUDS 出品，topic 明确覆盖 algorithmic-trading、backtesting、quantitative-finance；7d +828 星，近 30 天有 push。
- **技术栈/架构亮点**：Python + MCP + 多 Agent；将“vibe coding”思路迁移到交易领域，强调快速构建与迭代。
- **是否适合借鉴**：可借鉴其 MCP 集成方式与“研究-回测”快速验证闭环；但“vibe trading”本身带有较强实验性质，不宜直接用于实盘。
- **可能风险**：crypto_related 标记；策略过拟合、回测幸存者偏差；若接入真实交易所 API 存在资金与安全风险。

### 3.4 OpenByteInc/QuantDinger
- **解决什么问题**：提供开源 AI 交易 OS，覆盖研究、Python 策略编写、回测、模拟/实盘交易，并支持多租户交易 SaaS（用户管理、计费、支付、结算）。
- **为什么值得关注**：架构完整度在候选项目中突出，是少见的“交易系统 + SaaS 商业化”一体化开源项目。
- **技术栈/架构亮点**：Python + Apache-2.0；集成 MCP server、Binance、Stripe、Jev System One；模块化覆盖策略全生命周期。
- **是否适合借鉴**：适合借鉴其“策略全生命周期管理 + 多租户 SaaS”架构，用于企业级交易平台原型；但建议先研究其回测与风控模块，而非直接实盘。
- **可能风险**：涉及 crypto、多租户、支付结算，复杂度与合规风险高；若直接运行未知交易逻辑或输入真实 API key，存在重大资金风险。

### 3.5 simonlin1212/Vibe-Research
- **解决什么问题**：面向 A 股、美股、港股的投研工作台，提供自选/持仓、每日复盘、产业资讯、个股深挖、回测、研报库，168 个数据端点。
- **为什么值得关注**：多市场覆盖 + 本地 Agent + MCP，是中文金融投研场景中较完整的开源工作台；24h +181 星。
- **技术栈/架构亮点**：TypeScript + React + Python + MCP；支持 Claude Code、Codex、WorkBuddy 或任意模型 API；强调本地 Agent。
- **是否适合借鉴**：非常适合。可借鉴其“多市场数据端点 + 投研工作台 + 本地 Agent”架构，用于企业级投研数据工程与 Agent 化研究流程。
- **可能风险**：数据端点质量与合规性需自行验证；作为较新项目，生态与维护活跃度待观察。

### 3.6 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，用多 Agent 协作完成投资研究与决策。
- **为什么值得关注**：64k+ stars，是 AI 多 Agent 投研的经典参考项目；近 30 天有 push。
- **技术栈/架构亮点**：Python + 多 Agent 角色分工；强调研究、回测与决策流程。
- **是否适合借鉴**：适合作为多 Agent 投研流程的教学与原型参考；可结合 langfuse 做可观测，结合 iFixAi 做审计。
- **可能风险**：研究/教育属性强，策略有效性未经实盘验证；存在过拟合与幸存者偏差风险。

### 3.7 goldmansachs/gs-quant
- **解决什么问题**：Goldman Sachs 开源的量化金融 Python 工具包，覆盖衍生品、风险管理和交易策略。
- **为什么值得关注**：机构级背景，7d +551 星；近 30 天有 push。
- **技术栈/架构亮点**：Python + Apache-2.0；topic 覆盖 derivatives、risk-management、trading-strategies。
- **是否适合借鉴**：适合借鉴其风险管理和衍生品建模的工程化思路，用于企业级风控模块设计。
- **可能风险**：学习曲线较陡；部分功能可能依赖 GS 生态。

### 3.8 juspay/hyperswitch
- **解决什么问题**：开源可组合支付平台，支持 PCI 合规、多支付/欺诈/金库/令牌化提供商连接、智能路由与对账。
- **为什么值得关注**：Rust 实现的高性能支付编排，是金融基础设施的优质参考；24h +101 星。
- **技术栈/架构亮点**：Rust + Apache-2.0；强调支付编排、成本可观测、收入恢复、对账。
- **是否适合借鉴**：适合借鉴其支付编排与风控路由架构，用于金融产品支付层设计；与交易系统结算模块有直接关联。
- **可能风险**：支付合规要求高，自托管需自行承担 PCI 合规责任。

### 3.9 langfuse/langfuse
- **解决什么问题**：开源 LLM 应用追踪、评估与可观测平台。
- **为什么值得关注**：Agent 可观测是金融 AI Agent 落地的关键基础设施；7d +512 星，维护活跃。
- **技术栈/架构亮点**：TypeScript + 自托管；覆盖 trace、evaluate、prompt 管理、LLMOps。
- **是否适合借鉴**：非常适合。任何 AI 交易/投研 Agent 都应接入可观测与评估层，langfuse 是现成参考。
- **可能风险**：自托管运维成本；与金融合规审计的集成需二次开发。

### 3.10 CopilotKit/OpenBot
- **解决什么问题**：为每个 AI coworker 提供独立浏览器、文件与工具，所有动作在执行前决策、执行后记录，支持任意 AG-UI Agent。
- **为什么值得关注**：24h +253 星；topic 明确包含 agent-governance，是 Agent 操作审计的工程化探索。
- **技术栈/架构亮点**：TypeScript + AG-UI + MCP + browser-automation；强调动作决策前置与事后记录。
- **是否适合借鉴**：可借鉴其“动作决策前置 + 执行后记录”的治理模式，用于交易 Agent 的操作审计与回放。
- **可能风险**：浏览器自动化在金融场景存在安全边界问题；项目较新，稳定性待验证。

## 4. 趋势归纳

- **技术趋势**：
  - **Agent 治理与审计从概念走向工具化**：iFixAi、OpenBot、langfuse 共同指向“可观测、可评估、可审计”的 Agent 基础设施。
  - **本地优先 + 桌面 Agent 工作台**：Orkas、open-design、locally-uncensored 强调本地运行、隐私与自主可控。
  - **Skill/技能包生态爆发**：大量项目以 Claude/Codex/Gemini 技能包形式分发能力，形成“技能商店”模式。
  - **上下文工程成为 Agent 性能关键**：headroom 等项目专注 token 压缩与上下文优化。

- **产品趋势**：
  - **从单 Agent 到多 Agent 协作团队**：TradingAgents、ai-hedge-fund、Orkas 均采用角色化多 Agent 架构。
  - **交易系统一体化**：QuantDinger 覆盖研究-回测-模拟-实盘-SaaS 全链路。
  - **多市场投研工作台**：Vibe-Research 覆盖 A 股/美股/港股，强调本地 Agent 与 MCP 集成。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 决策框架**成为主流研究范式，但多数仍停留在研究/回测阶段。
  - **金融基础模型**（Kronos）尝试用 foundation model 建模金融市场语言。
  - **机构级工具开源化**：gs-quant 等降低机构量化工具门槛。

- **AI Agent 与自动化交易结合趋势**：
  - 交易 Agent 正在从“单模型生成信号”向“多角色协作 + 审计 + 可观测”演进。
  - MCP 成为连接行情、新闻、回测、交易执行的标准接口。
  - 风险治理需求前置：Agent 审计、操作回放、权限隔离成为交易 Agent 落地的必要条件。

- **值得后续做原型验证的方向**：
  - “多 Agent 投研 + 审计闭环”原型：TradingAgents 架构 + iFixAi 审计 + langfuse 可观测。
  - “本地优先投研工作台”原型：参考 Vibe-Research 的多市场数据端点 + 本地 Agent。
  - “交易策略全生命周期管理”原型：参考 QuantDinger 的模块化设计，但剥离实盘与支付模块。

## 5. 今日灵感清单

1. **MVP：多 Agent 投研决策沙箱**。用 TradingAgents 的角色化架构 + langfuse 可观测 + iFixAi 审计思路，搭建一个只读、不接实盘的投研决策沙箱，输出决策报告与审计日志。
2. **调研：MCP 在金融数据接入中的标准化程度**。对比 awesome-mcp-servers、awesome-remote-mcp-servers 中金融相关 MCP 的覆盖度与质量，评估是否可统一行情/新闻/回测接口。
3. **Codex/Agent 自动复现：本地投研工作台骨架**。参考 Vibe-Research，让 Codex 自动生成一个“多市场数据端点 + 每日复盘 + 个股深挖”的本地工作台骨架，重点验证数据端点抽象层。
4. **原型：Agent 操作审计与回放模块**。借鉴 OpenBot 的“决策前置 + 执行后记录”模式，为交易 Agent 增加操作审计与回放能力，形成合规证据链。
5. **调研：金融基础模型 Kronos 的输入输出范式**。研究其如何建模金融时序，评估是否可作为投研 Agent 的底层信号编码器。
6. **MVP：支付编排与结算参考实现**。参考 hyperswitch 的 Rust 架构，设计一个交易系统结算/对账模块的原型，重点验证智能路由与成本可观测。
7. **调研：Skill 商店的分发与版本管理机制**。分析 anbeime/skill、agentic-awesome-skills 等项目的技能打包、版本管理与自动抓取机制，评估企业级技能治理方案。
8. **原型：上下文压缩代理**。参考 headroom，为投研 Agent 增加日志/行情/RAG 块的 token 压缩代理，验证在金融长文本场景下的压缩率与信息保真度。
9. **调研：gs-quant 的风险管理模块**。研究其衍生品与风险建模 API，评估是否可抽取为独立风控服务。
10. **Watchlist 候选**：TradingAgents、iFixAi、Vibe-Research、QuantDinger、Kronos、OpenBot、langfuse、hyperswitch。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多 Agent 金融交易框架标杆，增速快，架构可借鉴 |
| ifixai-ai/iFixAi | Agent 审计/治理新兴方向，与金融合规高度相关 |
| simonlin1212/Vibe-Research | 多市场投研工作台，数据端点与本地 Agent 架构值得跟踪 |
| OpenByteInc/QuantDinger | 交易系统全生命周期 + SaaS 架构，工程参考价值高 |
| shiyu-coder/Kronos | 金融基础模型方向，长期研究价值 |
| CopilotKit/OpenBot | Agent 操作治理与审计的工程化探索 |
| langfuse/langfuse | Agent 可观测/评估基础设施，金融 Agent 落地必备 |
| juspay/hyperswitch | Rust 支付编排与风控路由，金融基础设施参考 |
| goldmansachs/gs-quant | 机构级量化与风控工具，持续跟踪 API 演进 |
| HKUDS/Vibe-Trading | LLM 交易 Agent 范式，观察其 MCP 与回测集成方式 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-10-27.json`，大部分项目具备 24h 涨星数据。
- **7 日基线**：已提供 `baseline_7d: 2026-10-21.json`，但部分项目 `star_delta_7d` 为 `null`（如 awesome-mac、day-trader-skill、FractalWorkspace），可能因项目创建时间晚于 7 日基线或基线数据缺失，导致 7d 涨星不可比。
- **30 日基线**：所有项目 `star_delta_30d` 均为 `null`，本次报告无法提供 30 日趋势判断。
- **采集失败/样本偏差**：
  - 候选集中包含大量 awesome-list、通用工具、设计/技能类项目，它们因关键词命中（如 “fintech”、“trading bot”、“quant”）被纳入，但实际与金融/量化/交易关联度低，分类噪声明显。
  - `category_guess` 与 `risk_flags` 为自动推断结果，存在误分类可能；例如 awesome-selfhosted 被归为 trading_bot，public-apis 被归为 crypto_trading，均与项目实际内容不符。
  - 部分项目 `language` 为 `null`，无法判断技术栈。
  - 报告仅基于 49 个候选项目，不代表 GitHub 全量金融/量化/交易项目趋势。
