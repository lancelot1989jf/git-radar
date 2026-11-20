# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-19

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent Skills 生态爆发**：以 Claude Code / Codex / Cursor 为载体的“技能包”项目大量涌现，覆盖 UI 设计、安全测试、交易分析、日内交易等场景，成为新的开源分发形态。
  2. **LLM 驱动的股票分析与交易 Agent**：`daily_stock_analysis`、`TradingAgents`、`Vibe-Trading`、`claude-trading-skills` 等项目持续高增长，显示“LLM + 多源行情 + 决策看板”正在成为个人量化研究的主流范式。
  3. **AI Agent 治理与审计**：`iFixAi` 等项目聚焦 AI Agent 的独立审计、合规与风险管理，反映 Agent 进入生产环境后对可观测性和对齐性的需求上升。

- **是否出现新趋势**：出现。**“Agent Skill 即产品”** 的趋势非常明显——大量项目不再提供完整应用，而是以“技能包 / 指令集 / 提示词工程”的形式分发能力，直接嵌入 Claude Code、Codex、Cursor 等编码 Agent。这降低了分发成本，但也带来质量参差和供应链风险。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“自托管 + DuckDB + Polars + FastAPI + React”本地量化工作台架构，都值得作为轻量级研究工具的参考模板。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中存在明显**关键词误匹配**项目，例如 `Turnitout-Humanizer`（学术抄袭规避工具）被归入“risk_management / trading_bot”，`awesome-selfhosted`、`build-your-own-x`、`public-apis` 等通用清单项目因描述中包含“trading bot”等词被误匹配。这些项目本身不是骗局，但**不应被视为金融/量化项目**。另有少量新建仓库（如 `vectorbt-avoria-analysis`、`quantconnect-lean-selvon-research`）24 小时涨星异常（+94，但总 star 仅 94），存在刷星或营销嫌疑，需谨慎对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 151912 | +428 | +3094 | Python | fintech_product | AI 驱动的多平台 UI/UX 设计技能包 | 中：Agent Skill 产品化参考 | 低 |
| 2 | elementalsouls/Claude-BugHunter | 13019 | +1421 | +7373 | Python | fintech_product | Claude Code 红队/漏洞挖掘技能包 | 高：安全审计 Agent 化 | 低 |
| 3 | GoogleChrome/modern-web-guidance | 23634 | +590 | +15558 | 无 | risk_management | 编码 Agent 的 Web 最佳实践指南 | 中：Agent 知识注入机制 | 低 |
| 4 | ZhuLinsen/daily_stock_analysis | 73512 | +99 | +2374 | Python | ai_trading/quant | LLM 多市场股票智能分析系统 | 高：LLM 投研工作流 | 低 |
| 5 | tradermonty/claude-trading-skills | 7308 | +183 | +3480 | Python | backtesting | Claude Code 股票交易技能包 | 高：交易研究 Agent 化 | 低 |
| 6 | awesome-selfhosted/awesome-selfhosted | 338758 | +279 | +2211 | 无 | trading_bot | 自托管服务清单（误匹配） | 低：非金融项目 | 中 |
| 7 | codecrafters-io/build-your-own-x | 564006 | +245 | +1805 | Markdown | trading_bot | 从零构建技术教程清单（误匹配） | 低：非金融项目 | 中 |
| 8 | public-apis/public-apis | 500381 | +230 | +1785 | Python | crypto/quant | 免费 API 清单（误匹配） | 中：数据源发现 | 中 |
| 9 | JustVugg/colibri | 52307 | +257 | +1753 | C | quant_research | MoE 模型分层推理引擎 | 中：本地 LLM 推理基建 | 低 |
| 10 | vinta/awesome-python | 335942 | +183 | +1542 | Python | quant_research | Python 工具清单（误匹配） | 低：非金融项目 | 低 |
| 11 | avelino/awesome-go | 194887 | +165 | +1271 | Go | backtesting/crypto | Go 框架清单（误匹配） | 低：非金融项目 | 中 |
| 12 | Jakeschincariol/day-trader-skill | 8825 | +165 | +1353 | Python | backtesting | Claude 日内交易技能包 | 高：交易决策 Agent 化 | 低 |
| 13 | nexu-io/open-design | 108587 | +188 | +1159 | TypeScript | fintech_product | 协作式 AI 设计 Agent 工作区 | 中：协作 Agent 架构 | 低 |
| 14 | CopilotKit/OpenBot | 13002 | +101 | +1152 | TypeScript | fintech/trading_bot | 开源可自托管 AI Bot 框架 | 中：通用 Agent 框架 | 中 |
| 15 | VoltAgent/awesome-design-md | 128337 | +149 | +1036 | 无 | crypto/fintech | 品牌设计系统 DESIGN.md 清单 | 低：非金融项目 | 中 |
| 16 | TauricResearch/TradingAgents | 123213 | +101 | +854 | Python | ai_trading/quant | 多 Agent LLM 金融交易框架 | 高：多 Agent 投研架构 | 低 |
| 17 | punkpeye/awesome-mcp-servers | 98286 | +127 | +615 | 无 | fintech_product | MCP 服务器清单 | 中：Agent 工具生态 | 低 |
| 18 | ifixai-ai/iFixAi | 46212 | -445 | +1048 | Python | ai_trading/risk | AI Agent 独立审计工具 | 高：Agent 治理与合规 | 低 |
| 19 | microsoft/BitNet | 42283 | +165 | +711 | C++ | ai_trading/quant | 1-bit LLM 官方推理框架 | 中：低资源 LLM 推理 | 低 |
| 20 | headroomlabs-ai/headroom | 80184 | +57 | +665 | Python | ai_trading/risk | LLM 上下文压缩工具 | 高：降低 Agent 推理成本 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股等多市场的 LLM 驱动股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：总 star 73,512，7 日涨星 +2,374，是本次候选集中最直接面向“LLM 投研”场景的高增长项目。其“零成本定时运行”设计降低了个人研究门槛。
- **技术栈/架构亮点**：Python + LLM + 多源行情 + 新闻流 + 决策看板 + 自动推送。架构上强调“数据采集—LLM 分析—看板呈现—推送触达”的闭环。
- **是否适合借鉴**：非常适合。可作为“AI 投研日报 Agent”的参考架构，尤其适合企业级研究助理、晨报自动化、多市场监控等场景。
- **可能风险**：LLM 输出可能存在幻觉，行情数据源质量与延迟未经验证；自动推送若接入实盘决策，存在误导风险；需注意数据合规与 API 限流。

### 3.2 TauricResearch/TradingAgents
- **解决什么问题**：多 Agent LLM 金融交易框架，将交易决策拆分为多个协作 Agent。
- **为什么值得关注**：总 star 123,213，是“LLM 多 Agent 交易”方向的标杆项目之一，7 日仍保持 +854 增长。
- **技术栈/架构亮点**：Python + 多 Agent 编排 + LLM。核心价值在于将分析师、交易员、风控等角色拆分为独立 Agent，形成决策流水线。
- **是否适合借鉴**：适合。多 Agent 角色分工模式可迁移到企业级投研、信用评估、合规审查等场景。但需注意其决策过程的可解释性和确定性。
- **可能风险**：策略过拟合、回测幸存者偏差、LLM 输出不稳定；作为研究框架尚可，直接实盘风险极高。

### 3.3 tradermonty/claude-trading-skills
- **解决什么问题**：面向 Claude Code 的股票交易技能包，覆盖市场分析、技术图表、经济日历、选股器和策略开发。
- **为什么值得关注**：7 日涨星 +3,480，增速显著。代表了“交易研究能力以 Skill 形式嵌入编码 Agent”的新范式。
- **技术栈/架构亮点**：Python + Claude Code Skills 机制。将交易研究工具封装为可被 Agent 调用的技能模块。
- **是否适合借鉴**：适合。可借鉴其“技能包”设计思路，将内部投研工具、数据接口、图表能力封装为 Agent 可调用的标准化技能。
- **可能风险**：技能包内容质量未经审计，可能包含误导性策略；依赖 Claude Code 生态，存在平台锁定风险。

### 3.4 Jakeschincariol/day-trader-skill
- **解决什么问题**：11 个 Claude 日内交易技能，用于扫描图表、跟踪新闻、择时进出场和复盘。
- **为什么值得关注**：7 日涨星 +1,353，总 star 8,825，是“日内交易 + Agent Skill”的典型代表。
- **技术栈/架构亮点**：Python + Claude Skills。强调“扫描—跟踪—择时—复盘”的日内交易闭环。
- **是否适合借鉴**：可借鉴其“交易复盘自动化”思路，用于构建内部交易日志、决策复盘和绩效归因工具。
- **可能风险**：日内交易策略本身高风险；技能包中的择时逻辑可能过拟合；不建议直接用于实盘。

### 3.5 ifixai-ai/iFixAi
- **解决什么问题**：AI Agent 的独立审计，回答“Agent 是否在做它应该做的事”，支持人工或 Agent 自审，120 秒内给出结论。
- **为什么值得关注**：总 star 46,212，7 日涨星 +1,048。虽然 24h 涨星为 -445，但整体仍处于高关注区间。其定位直击 Agent 生产化的核心痛点——治理与对齐。
- **技术栈/架构亮点**：Python + Agent 评估 + 合规框架（EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM）。将合规标准工程化为可执行审计工具。
- **是否适合借鉴**：非常适合。金融场景中，任何自动化交易或投研 Agent 都需要审计与对齐机制。可借鉴其“审计即代码”的思路，构建内部 Agent 合规检查流水线。
- **可能风险**：审计标准本身可能滞后于 Agent 技术演进；24h 涨星为负，需关注维护活跃度和社区稳定性。

### 3.6 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多 Agent 与回测。
- **为什么值得关注**：总 star 38,574，7 日涨星 +446。由 HKUDS 出品，学术背景较强，是“Vibe-Trading”概念的典型项目。
- **技术栈/架构亮点**：Python + LLM + MCP + 多 Agent + 回测。MCP 的引入使其工具调用更标准化。
- **是否适合借鉴**：适合作为“LLM 交易 Agent + MCP 工具链”的研究原型。可借鉴其 MCP 集成方式，将行情、回测、风控等能力标准化为 MCP 服务。
- **可能风险**：策略过拟合、回测偏差；学术项目向实盘迁移风险高；需注意 MCP 工具调用中的权限与安全边界。

### 3.7 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 策略定制、个股分析和复盘。
- **为什么值得关注**：总 star 8,096，7 日涨星 +417。技术栈现代（DuckDB + Polars + FastAPI + React），是轻量级本地量化工作台的代表。
- **技术栈/架构亮点**：Python + DuckDB + Polars + FastAPI + React + LLM。强调本地化、零运维和第三方数据源自由接入。
- **是否适合借鉴**：非常适合。可作为“本地优先量化研究平台”的参考架构，尤其适合数据敏感、需要离线分析的场景。
- **可能风险**：个人开源项目，维护持续性存疑；数据源接入需自行验证合规性；回测结果可能存在偏差。

### 3.8 Hithink-Tech-Org/Financial-API
- **解决什么问题**：同花顺官方 A 股金融数据服务，提供实时/历史行情、财报、指数、板块、涨停等数据，支持 API、MCP、CLI 和 Python。
- **为什么值得关注**：总 star 4,367，7 日涨星 +237。官方背景 + MCP 支持，使其成为 AI Agent 接入 A 股数据的重要基础设施。
- **技术栈/架构亮点**：TypeScript + REST API + MCP + CLI + Python + DuckDB。多接口形态降低了不同技术栈的接入成本。
- **是否适合借鉴**：适合。可借鉴其“数据服务多接口化”的设计，将内部数据平台同时暴露为 REST、MCP、CLI，提升 Agent 可调用性。
- **可能风险**：数据合规与授权范围需确认；依赖官方服务稳定性；MCP 接口的安全边界需审慎设计。

### 3.9 virattt/ai-hedge-fund
- **解决什么问题**：模拟“AI 对冲基金团队”，将投资决策拆分为多个 AI Agent。
- **为什么值得关注**：总 star 64,766，是“AI 对冲基金”概念的开源标杆。虽然近期增速放缓（7d +114），但架构思想仍有参考价值。
- **技术栈/架构亮点**：Python + 多 Agent 角色模拟。强调将基金经理、分析师、交易员等角色 Agent 化。
- **是否适合借鉴**：适合作为多 Agent 投研决策的入门参考。可借鉴其角色分工和决策流程设计。
- **可能风险**：策略过拟合、回测偏差；项目定位偏教育/研究，不适合实盘；需注意其决策透明度和可解释性不足。

### 3.10 headroomlabs-ai/headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 片段进入 LLM 前进行压缩，减少 token 消耗。
- **为什么值得关注**：总 star 80,184，7 日涨星 +665。对于高频调用 LLM 的金融 Agent，token 成本是核心瓶颈之一。
- **技术栈/架构亮点**：Python + 压缩代理 + MCP 服务器。支持库、代理、MCP 三种集成形态。
- **是否适合借鉴**：适合。可将其上下文压缩思路引入投研 Agent，降低长上下文场景（如财报、研报、行情日志）的推理成本。
- **可能风险**：压缩可能损失关键信息，金融场景需谨慎评估；依赖上游 LLM 生态变化。

## 4. 趋势归纳

- **技术趋势**：
  - **Agent Skills 成为新的分发单元**：大量项目以“技能包”形式发布，直接嵌入 Claude Code、Codex、Cursor 等编码 Agent。
  - **MCP（Model Context Protocol）加速渗透**：数据服务、工具、审计、压缩等项目普遍提供 MCP 接口，标准化 Agent 工具调用。
  - **本地优先与自托管**：`tick-stock-panel`、`colibri`、`project-maya` 等项目强调本地运行、隐私和零运维，反映金融场景对数据主权的重视。
  - **上下文工程**：`headroom` 等项目聚焦 token 压缩与上下文优化，降低 Agent 推理成本。

- **产品趋势**：
  - **从“完整应用”到“能力插件”**：产品形态从独立平台向可嵌入 Agent 的技能/工具包转变。
  - **投研工作台轻量化**：以 DuckDB、Polars、FastAPI 为代表的轻量技术栈替代重型数据平台。
  - **Agent 治理产品化**：`iFixAi` 等将审计、合规、对齐能力产品化，面向 Agent 生产化需求。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 投研**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 等项目持续演进，角色分工和决策流水线成为主流架构。
  - **日内交易与技能包结合**：`day-trader-skill`、`claude-trading-skills` 将交易研究能力封装为 Agent 技能。
  - **A 股量化工具链活跃**：`daily_stock_analysis`、`tick-stock-panel`、`Financial-API` 等项目显示 A 股数据与 LLM 结合的需求旺盛。

- **AI Agent 与自动化交易结合趋势**：
  - **从“策略执行”到“研究辅助”**：多数高增长项目定位为研究工具或决策辅助，而非直接自动下单，风险意识有所提升。
  - **审计与对齐成为刚需**：Agent 进入交易场景后，可观测性、合规审计、幻觉检测等需求上升。
  - **工具调用标准化**：MCP 成为连接 Agent 与行情、回测、风控工具的主流协议。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的本地量化研究 Agent，整合 DuckDB + Polars + LLM。
  - 交易决策复盘自动化工具，将交易日志、行情快照、新闻事件关联分析。
  - Agent 合规审计流水线，将 EU AI Act、NIST AI RMF 等标准工程化为可执行检查。
  - 面向金融场景的上下文压缩与 token 成本优化。

## 5. 今日灵感清单

1. **MVP：本地量化研究 Agent**：参考 `tick-stock-panel` 架构，用 DuckDB + Polars + FastAPI + MCP 搭建一个本地优先的 A 股研究 Agent，支持自然语言查询、策略回测和可视化。
2. **MVP：交易复盘自动化工具**：参考 `day-trader-skill` 的复盘思路，构建一个自动关联交易记录、行情快照和新闻事件的复盘报告生成器。
3. **调研：MCP 在金融数据服务中的标准化**：研究 `Hithink-Tech-Org/Financial-API` 和 `awesome-mcp-servers`，评估将内部数据平台暴露为 MCP 服务的可行性与安全边界。
4. **调研：Agent Skills 的分发与治理机制**：分析 `claude-trading-skills`、`Claude-BugHunter` 等技能包的结构，设计内部技能包的版本管理、审计和权限控制方案。
5. **Codex/Agent 自动复现 demo：多 Agent 投研流水线**：基于 `TradingAgents` 或 `ai-hedge-fund` 的角色分工，用 Codex 自动生成一个简化版多 Agent 投研 demo，重点验证角色间信息传递和决策可解释性。
6. **原型：Agent 合规审计检查器**：参考 `iFixAi`，为内部自动化交易或投研 Agent 构建一个轻量级审计检查器，覆盖幻觉检测、越权操作、异常输出等。
7. **原型：金融上下文压缩代理**：参考 `headroom`，针对财报、研报、行情日志等长文本场景，验证压缩对 LLM 分析质量和 token 成本的影响。
8. **加入 watchlist：`JustVugg/colibri` 和 `microsoft/BitNet`**：关注本地 LLM 推理和 1-bit 量化进展，评估在金融数据敏感场景下的本地部署可行性。
9. **调研：同花顺 Financial-API 的 MCP 接口设计**：分析其 API、MCP、CLI 多形态设计，提炼可复用的数据服务接口规范。
10. **警惕：新建仓库异常涨星**：对 `vectorbt-avoria-analysis`、`quantconnect-lean-selvon-research` 等 24h 涨星与总 star 接近的项目保持警惕，避免将其作为可靠参考。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | LLM 投研工作流标杆，持续高增长，适合跟踪多源数据整合与自动推送架构 |
| TauricResearch/TradingAgents | 多 Agent 交易框架代表，适合研究角色分工与决策流水线 |
| tradermonty/claude-trading-skills | 交易研究技能包范式，适合观察 Agent Skill 在金融场景的演进 |
| ifixai-ai/iFixAi | Agent 审计与治理的先行项目，适合跟踪合规工程化趋势 |
| HKUDS/Vibe-Trading | 学术背景的 LLM 交易 Agent，适合研究 MCP 与多 Agent 集成 |
| shy3130/tick-stock-panel | 本地优先量化工作台，技术栈现代，适合作为轻量级研究平台参考 |
| Hithink-Tech-Org/Financial-API | 官方 A 股数据服务，MCP 支持，适合跟踪金融数据 Agent 化接入 |
| headroomlabs-ai/headroom | 上下文压缩对金融 Agent 成本优化有直接价值 |
| JustVugg/colibri | 本地 MoE 推理引擎，适合关注金融数据敏感场景的本地 LLM 部署 |
| microsoft/BitNet | 1-bit LLM 推理框架，适合跟踪低资源量化推理进展 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告使用了 `baseline_1d: 2026-11-18.json` 和 `baseline_7d: 2026-11-12.json`，基线数据完整，1 日和 7 日涨星数据可用。
- **30 日基线缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法提供 30 日涨星趋势，长期趋势判断受限。
- **采集失败**：部分项目 `star_delta_7d` 为 `null`（如 `modern-web-guidance-src`、`bang-motion`、`vectorbt-avoria-analysis`、`quantconnect-lean-selvon-research`），可能因项目创建时间晚于 7 日基线或采集失败。
- **样本偏差**：候选集存在明显的**关键词误匹配**问题。大量通用清单项目（如 `awesome-selfhosted`、`build-your-own-x`、`public-apis`、`awesome-python`、`awesome-go` 等）因描述或 README 中包含“trading bot”“quant”“volatility”等词被纳入，实际并非金融/量化项目。这导致 Top 榜单中非金融项目占比偏高，分析时需人工过滤。
- **异常涨星**：`vectorbt-avoria-analysis` 和 `quantconnect-lean-selvon-research` 两个新建仓库 24h 涨星 +94，但总 star 仅 94，存在刷星或营销嫌疑，不应作为可靠参考。
- **分类可信度**：`category_guess` 字段为自动推断，部分分类（如将 `Turnitout-Humanizer` 归为 risk_management/trading_bot）明显错误，需结合项目实际内容判断。
