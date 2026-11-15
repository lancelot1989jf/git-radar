# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-14

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的股票分析/交易 Agent 技能包**：`daily_stock_analysis`、`day-trader-skill`、`claude-trading-skills` 等项目集中爆发，反映“用 Claude/Codex 技能包封装交易研究流程”成为新范式。
  2. **AI Agent 治理与审计**：`iFixAi` 以“120 秒审计 Agent 是否按预期工作”切入，结合 EU AI Act、ISO 42001、NIST AI RMF 等合规框架，代表 Agent 风控从“提示词约束”走向“可验证审计”。
  3. **本地优先/自托管 AI 工作台**：`OpenBot`、`Orkas`、`locally-uncensored` 等项目强调“每个 Agent 拥有自己的电脑/浏览器/文件”，与金融场景中“数据不出域、策略本地运行”的诉求高度契合。

- **是否出现新趋势**：出现。**“AI Skill 即产品”** 趋势明显——大量项目不再提供完整交易系统，而是提供可插拔的 Claude/Codex/Cursor 技能包（skills），覆盖选股、图表扫描、新闻跟踪、回测复盘等环节。这降低了金融 AI 工具的构建门槛，但也带来策略质量参差不齐的问题。

- **是否出现值得复刻/参考的工程架构**：出现。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“DuckDB + Polars + FastAPI + React”本地量化工作台架构，都值得作为轻量级金融数据产品的参考模板。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但存在**大量“awesome-list”类项目因关键词误匹配进入金融雷达**（如 `awesome-selfhosted`、`public-apis`、`build-your-own-x`、`awesome-go` 等），它们本身不是交易项目，需在分析时剔除噪声。另有个别项目（如 `Turnitout-Humanizer`）与金融/量化完全无关，属于匹配噪声。`day-trader-skill`、`claude-trading-skills` 等交易技能包虽标注“低风险”，但其“扫描数千图表、择时进出场”的营销话术需警惕策略过拟合与幸存者偏差。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 72313 | +444 | +4444 | Python | AI 交易/数据工程/量化研究 | LLM 驱动的多市场股票分析系统，多源行情+新闻+看板+推送 | 高：轻量级金融数据产品架构 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 149609 | +413 | +2991 | Python | 金融科技产品（误匹配） | AI UI/UX 设计技能包 | 低：与金融核心无关 | 低 |
| 3 | JustVugg/colibri | 51184 | +263 | +2382 | C | 量化研究（误匹配） | MoE 模型分层推理引擎 | 中：本地推理基础设施 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 337180 | +332 | +2272 | 无 | 交易机器人（误匹配） | 自托管服务列表 | 低：资源导航 | 中 |
| 5 | public-apis/public-apis | 499099 | +250 | +2006 | Python | 加密交易/量化研究（误匹配） | 免费 API 合集 | 中：金融数据 API 来源 | 中 |
| 6 | CopilotKit/OpenBot | 12312 | +156 | +1894 | TypeScript | 金融科技产品/交易机器人 | 开源 AI 同事，每个 Agent 拥有浏览器/文件/工具 | 高：Agent 治理与浏览器自动化 | 中 |
| 7 | codecrafters-io/build-your-own-x | 562599 | +209 | +1751 | Markdown | 交易机器人（误匹配） | 从零复刻技术的教程合集 | 低：学习资源 | 中 |
| 8 | Jakeschincariol/day-trader-skill | 7861 | +204 | +1829 | Python | 回测/风险管理 | 11 个 Claude 日内交易技能包 | 高：交易研究流程产品化 | 低 |
| 9 | ifixai-ai/iFixAi | 45720 | +271 | +1701 | Python | AI 交易/金融科技/风控 | AI Agent 独立审计，120 秒验证行为 | 高：Agent 合规与审计框架 | 低 |
| 10 | vinta/awesome-python | 334836 | +217 | +1560 | Python | 量化研究（误匹配） | Python 工具精选列表 | 低：资源导航 | 低 |
| 11 | VoltAgent/awesome-design-md | 127578 | +148 | +1518 | 无 | 加密交易/金融科技（误匹配） | 设计系统 DESIGN.md 合集 | 低：与金融核心无关 | 中 |
| 12 | TauricResearch/TradingAgents | 122628 | +140 | +1400 | Python | AI 交易/回测/量化研究 | 多 Agent LLM 金融交易框架 | 高：多 Agent 交易决策架构 | 低 |
| 13 | garrytan/gbrain | 33035 | +154 | +1409 | TypeScript | 金融科技产品（误匹配） | OpenClaw/Hermes Agent Brain | 中：Agent 编排参考 | 低 |
| 14 | avelino/awesome-go | 193983 | +168 | +1307 | Go | 回测/加密交易/风控（误匹配） | Go 框架与库精选列表 | 低：资源导航 | 中 |
| 15 | nexu-io/open-design | 107685 | +131 | +1164 | TypeScript | 金融科技产品/交易基础设施（误匹配） | 协作式 AI 设计工作台 | 低：与金融核心无关 | 低 |
| 16 | tradermonty/claude-trading-skills | 4999 | +690 | +1311 | Python | 回测 | Claude Code 股票交易技能包 | 高：交易技能包产品化 | 低 |
| 17 | awesome-dsh-plugin/awesome-dsh-plugin | 24709 | +104 | +1087 | JavaScript | 交易基础设施（误匹配） | DeepSeek Harness 插件列表 | 低：插件生态导航 | 低 |
| 18 | TGrpg/awesome-telegram | 1520 | +230 | +878 | JavaScript | 量化研究/交易机器人（误匹配） | Telegram 频道/群组/机器人导航 | 低：信号渠道风险 | 中 |
| 19 | ripienaar/free-for-dev | 142874 | +85 | +668 | HTML | 金融科技/量化研究（误匹配） | 开发者免费资源列表 | 低：资源导航 | 低 |
| 20 | jaywcjlove/awesome-mac | 118557 | +66 | +612 | Swift | 交易基础设施（误匹配） | macOS 软件精选 | 低：与金融核心无关 | 低 |
| 21 | ruvnet/ruflo | 81739 | +80 | +540 | TypeScript | AI 交易/回测 | Agent 编排框架，多智能体 swarm | 中：多 Agent 编排参考 | 低 |
| 22 | headroomlabs-ai/headroom | 79684 | +69 | +585 | Python | AI 交易/风控 | LLM 输出压缩，节省 token | 中：降低 Agent 推理成本 | 低 |
| 23 | kaankiziltug/logo-design-skill | 6941 | +69 | +657 | HTML | 金融科技产品（误匹配） | Logo 设计技能包 | 低：与金融核心无关 | 低 |
| 24 | hesreallyhim/awesome-claude-code | 58027 | +66 | +525 | Python | AI 交易/量化研究（误匹配） | Claude Code 资源精选 | 低：资源导航 | 低 |
| 25 | PurpleDoubleD/locally-uncensored | 4256 | +52 | +685 | TypeScript | AI 交易/量化研究（误匹配） | 本地 AI 桌面工作室 | 中：本地推理与隐私 | 低 |
| 26 | HKUDS/Vibe-Trading | 38257 | +70 | +399 | Python | AI 交易/回测/金融科技/量化研究/风控 | 个人交易 Agent | 高：学术机构多 Agent 交易框架 | 低 |
| 27 | elementalsouls/Claude-BugHunter | 5862 | +95 | +374 | Python | 金融科技产品（误匹配） | Claude 漏洞挖掘技能包 | 中：安全审计思路 | 低 |
| 28 | shy3130/tick-stock-panel | 7801 | +59 | +519 | Python | AI 交易/回测/量化研究 | A 股自托管量化工作台 | 高：DuckDB+Polars 本地量化架构 | 低 |
| 29 | punkpeye/awesome-remote-mcp-servers | 3227 | +59 | +442 | 无 | AI 交易/加密交易/交易基础设施 | 远程 MCP 服务器合集 | 中：MCP 生态观察 | 中 |
| 30 | sickn33/agentic-awesome-skills | 49723 | +47 | +386 | Python | 回测 | 2955+ 可复用 AI Agent 技能库 | 中：技能库产品化 | 低 |
| 31 | shiyu-coder/Kronos | 47817 | +49 | +542 | Python | 回测/量化研究 | 金融市场基础模型 | 高：金融基础模型研究方向 | 低 |
| 32 | Soniavasseur/Wallet-Risk-Scanner | 914 | 0 | +722 | Python | 加密交易/金融科技/风控 | 多链加密钱包 AML/KYT 风险扫描 | 高：链上风控与合规 | 中 |
| 33 | nidhinjs/prompt-master | 15991 | +48 | +313 | 无 | AI 交易/金融科技（误匹配） | Prompt 优化技能包 | 低：与金融核心无关 | 低 |
| 34 | punkpeye/awesome-mcp-servers | 97718 | +32 | +268 | 无 | 金融科技产品（误匹配） | MCP 服务器合集 | 低：资源导航 | 低 |
| 35 | AhmadHassan-BTed/Turnitout-Humanizer | 12269 | +30 | +367 | HTML | 风控/交易机器人（误匹配） | 学术文本“降重”工具 | 低：与金融无关，且用途存疑 | 中 |
| 36 | GoogleChrome/modern-web-guidance | 15890 | +4151 | 无 | 无 | 风控（误匹配） | Web 最佳实践指南 | 低：与金融核心无关 | 低 |
| 37 | openbq-org/OpenBB | 75433 | +30 | +213 | Python | 加密交易/量化研究 | 面向分析师/量化/AI Agent 的开放数据平台 | 高：金融数据基础设施 | 中 |
| 38 | aardappel/goose | 3543 | +31 | +276 | C++ | 交易基础设施（误匹配） | Goose 编程语言 | 低：与金融核心无关 | 低 |
| 39 | Developer-Y/cs-video-courses | 84852 | +17 | +189 | 无 | 量化研究/交易机器人（误匹配） | CS 视频课程列表 | 低：学习资源 | 中 |
| 40 | Orkas-AI/Orkas | 9361 | +19 | +264 | JavaScript | 回测 | 本地优先 AI 团队桌面应用 | 中：本地多 Agent 编排 | 低 |
| 41 | rust-unofficial/awesome-rust | 60545 | +20 | +151 | Rust | AI 交易/回测/加密交易/量化研究/风控（误匹配） | Rust 资源精选 | 低：资源导航 | 中 |
| 42 | code-yeongyu/oh-my-openagent | 70914 | +16 | +143 | TypeScript | 量化研究（误匹配） | 图工程 Agent 工具 | 低：与金融核心无关 | 低 |
| 43 | fffaraz/awesome-cpp | 74425 | +20 | +125 | 无 | 量化研究/交易基础设施（误匹配） | C/C++ 资源精选 | 低：资源导航 | 低 |
| 44 | virattt/ai-hedge-fund | 64682 | +19 | +129 | Python | 回测/风控 | AI 对冲基金团队模拟 | 高：多角色 Agent 投研流程 | 低 |
| 45 | awesomedata/awesome-public-datasets | 80122 | +11 | +143 | 无 | 加密交易（误匹配） | 公开数据集精选 | 中：金融数据集来源 | 中 |
| 46 | josephmisiti/awesome-machine-learning | 74831 | +11 | +48 | Python | AI 交易（误匹配） | ML 框架与库精选 | 低：资源导航 | 低 |
| 47 | brainbytes-dev/everything-claude-trading | 240 | +101 | +106 | JavaScript | 回测/量化研究 | Claude Code 完整交易系统：18 agents/82 skills/20 commands | 高：交易技能包集成范式 | 低 |
| 48 | vuejs/awesome-vue | 73474 | 0 | -8 | 无 | 量化研究（误匹配） | Vue.js 资源精选 | 低：与金融核心无关 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis（rank 1）

- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：24h 涨星 +444、7d 涨星 +4444，是本次候选集中金融属性最强、涨势最猛的项目。其“零成本定时运行”定位切中了个人投资者对低成本、自动化投研工具的需求。
- **技术栈/架构亮点**：Python + LLM 驱动；多源数据接入 + 决策看板 + 自动推送的流水线架构。从描述看，核心价值在于“数据聚合 + LLM 解读 + 定时触达”的闭环。
- **是否适合借鉴**：适合。可借鉴其“多源数据标准化 → LLM 分析 → 看板/推送”的轻量级金融数据产品架构，尤其适合构建内部投研日报、舆情监控等 MVP。
- **可能风险**：描述与 topics 均来自项目方，需自行核验数据源合规性；LLM 生成的“决策”存在幻觉风险；自动推送若接入实盘信号需谨慎。

### 3.2 CopilotKit/OpenBot（rank 6）

- **解决什么问题**：提供“开源 AI 同事”，每个 Agent 拥有独立的浏览器、文件和工具，所有动作在执行前决策、执行后记录，支持接入任意 AG-UI Agent。
- **为什么值得关注**：7d 涨星 +1894，代表“Agent 拥有计算机”这一范式的落地。对金融场景而言，浏览器自动化 + 动作留痕是构建可审计交易/研究 Agent 的基础设施。
- **技术栈/架构亮点**：TypeScript；AG-UI 协议、MCP、生成式 UI、浏览器自动化、Agent 治理。核心是“决策前置 + 动作记录”的治理模型。
- **是否适合借鉴**：适合。其“动作前决策、动作后记录”的机制可直接借鉴到企业级 Agent 风控框架中，用于交易指令审计、合规留痕。
- **可能风险**：被标记为 trading_bot，但本身不是交易系统；若用于自动化交易，需额外构建风控层；浏览器自动化存在凭据泄露风险。

### 3.3 Jakeschincariol/day-trader-skill（rank 8）

- **解决什么问题**：提供 11 个 Claude 日内交易技能，覆盖图表扫描、突发新闻跟踪、进出场择时、结果回放复盘。
- **为什么值得关注**：7d 涨星 +1829，是“交易技能包”趋势的代表。将交易研究流程拆解为可复用的 Claude skills，降低了个人搭建交易研究工具的门槛。
- **技术栈/架构亮点**：Python + Claude skills；模块化技能设计，覆盖“扫描→跟踪→择时→复盘”全流程。
- **是否适合借鉴**：适合作为产品灵感。可借鉴其“技能包”形态，将投研流程标准化为可插拔模块，但不宜直接用于实盘。
- **可能风险**：营销话术“在冒险投入一美元前回放每个结果”存在过度承诺；日内交易策略极易过拟合；回测结果不代表未来表现。

### 3.4 ifixai-ai/iFixAi（rank 9）

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，声称 120 秒内给出答案。
- **为什么值得关注**：7d 涨星 +1701，且 topics 覆盖 EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM、prompt injection 等，代表 Agent 治理从“开发期约束”走向“运行期审计”。
- **技术栈/架构亮点**：Python + Apache-2.0；CLI 诊断工具；覆盖幻觉检测、提示注入、LLM 安全、风险评估。
- **是否适合借鉴**：非常适合。金融场景中，交易 Agent 的行为审计是刚需。可借鉴其“Agent 行为可验证性”思路，构建交易指令的事前/事后审计层。
- **可能风险**：审计本身的准确性依赖评估基准质量；120 秒的审计深度可能有限；需自行核验其评估方法是否扎实。

### 3.5 TauricResearch/TradingAgents（rank 12）

- **解决什么问题**：多 Agent LLM 金融交易框架，将交易决策拆解为多个协作 Agent。
- **为什么值得关注**：stars 122628，7d 涨星 +1400，是“多 Agent 交易决策”方向的成熟参考项目。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 协作；LLM 驱动；覆盖交易决策流程。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色分工（如分析师、交易员、风控）的架构，用于构建企业级投研 Agent 团队。
- **可能风险**：被标记为 likely_research_tool，定位偏研究；多 Agent 决策链路过长可能引入延迟与不一致；策略有效性需独立验证。

### 3.6 HKUDS/Vibe-Trading（rank 26）

- **解决什么问题**：定位为“个人交易 Agent”，由香港大学团队（HKUDS）出品。
- **为什么值得关注**：学术机构背景 + 多 Agent + MCP + 回测，stars 38257。学术项目通常更注重方法可复现性。
- **技术栈/架构亮点**：Python + MIT；topics 覆盖 ai-agent、algorithmic-trading、backtesting、fintech、llm、mcp、multi-agent。
- **是否适合借鉴**：适合。学术背景使其更适合作为多 Agent 交易框架的研究基线，可复现其架构用于教学或原型验证。
- **可能风险**：学术项目可能缺乏生产级稳定性；策略表现可能基于特定回测区间；不宜直接实盘。

### 3.7 shy3130/tick-stock-panel（rank 28）

- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 策略定制、个股分析、复盘，可接入第三方数据源。
- **为什么值得关注**：7d 涨星 +519，技术栈明确（DuckDB、Polars、FastAPI、React），是本地优先量化工作台的典型代表。
- **技术栈/架构亮点**：Python + DuckDB + Polars + FastAPI + React；本地数据存储与计算，强调自托管与零运维。
- **是否适合借鉴**：非常适合。DuckDB + Polars 的组合适合中小规模金融数据的本地分析，可作为轻量级量化研究平台的参考架构。
- **可能风险**：A 股数据源合规性需自行核验；LLM 策略定制存在过拟合风险；自托管需注意数据安全。

### 3.8 Soniavasseur/Wallet-Risk-Scanner（rank 32）

- **解决什么问题**：多链加密钱包风险扫描，用于 AML/KYT 筛查，对地址进行 0–100 评分，覆盖制裁、风险合约、资金追踪，集成 6 个情报源，支持 15+ 链。
- **为什么值得关注**：7d 涨星 +722（但 24h 涨星为 0，需注意涨星集中度），是本次候选集中少有的链上风控/合规工具。
- **技术栈/架构亮点**：Python + MIT；多情报源 failover；批量筛查；多格式报告输出。
- **是否适合借鉴**：适合。链上风控、地址评分、资金追踪是加密交易基础设施的关键环节，可借鉴其多源情报集成与评分模型思路。
- **可能风险**：被标记为 crypto_related，风险等级中；项目较新（stars 914），需核验数据源可靠性与评分模型有效性；AML/KYT 合规要求因地区而异。

### 3.9 virattt/ai-hedge-fund（rank 44）

- **解决什么问题**：模拟“AI 对冲基金团队”，由多个 AI Agent 扮演不同角色协作完成投研。
- **为什么值得关注**：stars 64682，是“多角色 Agent 投研流程”的经典参考项目，虽然近期涨星放缓（24h +19），但架构仍具参考价值。
- **技术栈/架构亮点**：Python + MIT；多角色 Agent 协作；回测支持。
- **是否适合借鉴**：适合。可借鉴其角色分工（如分析师、研究员、交易员、风控）的 Agent 编排模式，用于构建内部投研流水线。
- **可能风险**：被标记为 likely_research_tool，定位偏教育/研究；策略表现不代表真实收益；不宜直接实盘。

### 3.10 shiyu-coder/Kronos（rank 31）

- **解决什么问题**：金融市场基础模型（Foundation Model for the Language of Financial Markets）。
- **为什么值得关注**：7d 涨星 +542，代表“金融基础模型”这一研究方向，与通用 LLM 做金融任务形成差异化。
- **技术栈/架构亮点**：Python + MIT；定位为金融语言基础模型。
- **是否适合借鉴**：适合作为研究方向跟踪。可关注其模型架构、训练数据、评估方法，思考金融领域专用基础模型的可行性。
- **可能风险**：被标记为 likely_research_tool；金融基础模型的评估基准和实际效用仍需验证；项目近期 push 时间较早（2026-04），维护活跃度需关注。

## 4. 趋势归纳

### 技术趋势
- **“AI Skill 即产品”**：交易研究流程被拆解为可插拔的 Claude/Codex/Cursor 技能包（`day-trader-skill`、`claude-trading-skills`、`everything-claude-trading`、`agentic-awesome-skills`），降低金融 AI 工具构建门槛。
- **本地优先与自托管**：`tick-stock-panel`（DuckDB + Polars）、`OpenBot`、`Orkas`、`locally-uncensored` 等项目强调数据不出域、本地运行，契合金融数据合规需求。
- **Agent 治理与审计**：`iFixAi`、`OpenBot` 的“动作留痕/事前决策”机制，反映 Agent 从“能跑”走向“可审计”。
- **MCP 生态扩张**：`awesome-mcp-servers`、`awesome-remote-mcp-servers`、`awesome-dsh-plugin` 等项目显示 MCP 正成为 Agent 工具接入的标准协议。

### 产品趋势
- **从“完整交易系统”转向“模块化技能包”**：用户不再需要一个庞大的交易平台，而是需要能嵌入现有 Agent 工作流的轻量技能。
- **决策看板 + 自动推送**：`daily_stock_analysis` 代表的“分析→看板→推送”闭环，是个人投研工具的产品化方向。
- **风控产品化**：`Wallet-Risk-Scanner`、`iFixAi` 显示风控/合规正成为独立产品赛道。

### 量化/交易策略趋势
- **多 Agent 协作决策**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 均采用多角色 Agent 分工，模拟投研团队。
- **LLM 与结构化数据结合**：`tick-stock-panel` 用 DuckDB/Polars 处理结构化行情，再用 LLM 做策略定制与解读，是“结构化数据 + LLM”的典型范式。
- **金融基础模型探索**：`Kronos` 代表从“通用 LLM 做金融”向“金融专用基础模型”的探索。

### AI Agent 与自动化交易结合趋势
- **技能包 + Agent 运行时**：交易技能包（skills）与 Claude Code/Codex 等 Agent 运行时结合，形成“研究 Agent”而非“自动下单 Agent”。
- **审计先行**：`iFixAi`、`OpenBot` 的治理机制显示，Agent 自动化交易的前提是行为可验证、动作可留痕。
- **本地推理降低合规风险**：本地优先架构让金融数据与策略留在用户侧，降低数据出境与合规风险。

### 值得后续做原型验证的方向
1. **投研日报 Agent**：借鉴 `daily_stock_analysis`，构建“多源数据 → LLM 分析 → 定时推送”的内部投研日报 MVP。
2. **交易技能包标准化**：借鉴 `day-trader-skill`、`claude-trading-skills`，将投研流程拆解为可复用技能模块。
3. **Agent 行为审计层**：借鉴 `iFixAi`，为交易 Agent 构建事前决策校验 + 事后动作留痕的审计框架。
4. **本地量化工作台**：借鉴 `tick-stock-panel`，用 DuckDB + Polars + FastAPI 构建轻量级本地回测与监控平台。
5. **链上风控评分**：借鉴 `Wallet-Risk-Scanner`，探索地址风险评分与 AML 筛查的原型。

## 5. 今日灵感清单

1. **MVP：内部投研日报 Agent**  
   用 `daily_stock_analysis` 的架构思路，构建一个“多源行情 + 新闻 + LLM 摘要 + 定时推送”的内部投研日报工具，数据源可先用公开 API，推送用企业微信/Slack。

2. **MVP：交易研究技能包**  
   参考 `day-trader-skill` 和 `claude-trading-skills`，将“数据获取→技术指标→新闻情绪→回测复盘”拆解为 5–8 个 Claude/Codex 技能，封装成可插拔模块，供内部研究员使用。

3. **调研：Agent 行为审计框架**  
   深入研究 `iFixAi` 的审计方法（幻觉检测、提示注入、行为验证），思考如何为交易 Agent 构建“事前决策校验 + 事后动作留痕”的轻量审计层。

4. **调研：DuckDB + Polars 本地量化架构**  
   复现 `tick-stock-panel` 的技术栈，验证 DuckDB + Polars 在中小规模金融数据上的查询性能与开发效率，评估是否适合作为内部量化研究平台的基础。

5. **Demo：多 Agent 投研团队模拟**  
   用 `TradingAgents` 或 `ai-hedge-fund` 的架构，让 Codex/Agent 自动搭建一个“分析师 + 交易员 + 风控”的多角色投研 demo，重点观察角色间信息传递与决策冲突处理。

6. **调研：MCP 在金融数据接入中的应用**  
   浏览 `awesome-mcp-servers` 和 `awesome-remote-mcp-servers`，筛选与行情、新闻、链上数据相关的 MCP 服务器，评估用 MCP 标准化金融数据接入的可行性。

7. **原型：链上地址风险评分**  
   参考 `Wallet-Risk-Scanner`，用公开链上数据源构建一个简化的地址风险评分原型，聚焦制裁名单匹配与可疑合约交互检测。

8. **调研：金融基础模型**  
   跟踪 `Kronos` 的模型架构与评估方法，思考“金融专用基础模型”与“通用 LLM + 金融数据微调”两条路线的优劣。

9. **Watchlist：OpenBot 的 Agent 治理机制**  
   关注 `OpenBot` 的“动作前决策、动作后记录”机制，评估其是否可复用到企业级 Agent 风控框架中。

10. **调研：本地优先 AI 工作台**  
    对比 `Orkas`、`locally-uncensored`、`OpenBot` 的本地优先架构，思考金融场景中“数据不出域”的 Agent 工作台应如何设计。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 金融属性最强、涨势最猛，轻量级金融数据产品架构值得持续跟踪 |
| CopilotKit/OpenBot | Agent 治理与浏览器自动化机制，对交易 Agent 审计有参考价值 |
| ifixai-ai/iFixAi | Agent 审计与合规框架，金融 Agent 风控的关键基础设施 |
| TauricResearch/TradingAgents | 多 Agent 交易决策框架的成熟参考，适合研究角色分工与协作 |
| HKUDS/Vibe-Trading | 学术背景的多 Agent 交易框架，适合作为研究基线 |
| shy3130/tick-stock-panel | DuckDB + Polars 本地量化架构，轻量级量化工作台的代表 |
| Soniavasseur/Wallet-Risk-Scanner | 链上风控/AML 工具，加密交易合规方向值得关注 |
| shiyu-coder/Kronos | 金融基础模型研究方向，需观察其后续维护与评估进展 |
| virattt/ai-hedge-fund | 多角色 Agent 投研流程的经典参考，适合教学与原型验证 |
| tradermonty/claude-trading-skills | 交易技能包产品化代表，24h 涨星 +690，需观察其持续性 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

此外需特别注意：

- **大量误匹配噪声**：本次候选集中约半数项目（如 `awesome-selfhosted`、`public-apis`、`build-your-own-x`、`awesome-go`、`awesome-python` 等）是 awesome-list 或通用工具，因关键词误匹配进入金融雷达，分析时需剔除。
- **交易技能包的过度承诺**：`day-trader-skill`、`claude-trading-skills` 等项目的营销话术（如“在冒险投入一美元前回放每个结果”）需警惕，回测结果不代表未来表现，日内交易策略极易过拟合。
- **涨星集中度异常**：`Wallet-Risk-Scanner` 7d 涨星 +722 但 24h 涨星为 0，`modern-web-guidance` 24h 涨星 +4151 但 7d 数据缺失，需警惕涨星异常或数据采集问题。
- **API Key 与凭据安全**：任何涉及浏览器自动化、交易所接入、钱包扫描的项目，都存在凭据泄露风险，切勿在未审计代码的情况下输入真实 API Key 或私钥。
- **合规风险**：链上风控、AML/KYT、跨境数据等场景的合规要求因地区而异，原型验证前需咨询专业法律意见。

## 8. 数据质量说明

- **基线数据**：本次报告使用了 `baseline_1d`（2026-11-13）和 `baseline_7d`（2026-11-07），1 日与 7 日涨星数据基本完整。
- **缺失数据**：`star_delta_30d` 在所有项目中均为 `null`，无法进行 30 日趋势分析。`modern-web-guidance` 的 `star_delta_7d` 为 `null`，无法判断其 7 日涨星。
- **采集异常**：`Wallet-Risk-Scanner` 的 24h 涨星为 0 但 7d 涨星为 +722，可能存在涨星集中或采集时点问题；`modern-web-guidance` 24h 涨星 +4151 异常偏高，需核实是否为数据采集错误。
- **样本偏差**：候选集通过关键词匹配生成，导致大量 awesome-list 和通用工具项目因 README/描述中偶然出现“quant”“trading bot”“fintech”等词而被纳入，金融相关性被稀释。真正与金融/量化/交易直接相关的项目约占候选集的 30%–40%。
- **分类可信度**：`category_guess` 为自动推断，部分项目（如 `colibri` 被归为 quant_research、`Turnitout-Humanizer` 被归为 risk_management）明显属于误分类，需人工复核。
- **风险等级**：`risk_level` 为自动标注，仅基于关键词与用途标记，不代表实际安全风险，使用前需自行审计代码。
