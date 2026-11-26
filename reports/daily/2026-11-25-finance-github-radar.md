# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-25

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent Skills 生态爆发**：以 Claude Code / Codex / Cursor 为载体的“技能包”项目大量涌现，覆盖 UI 设计、安全测试、交易分析等场景，涨星速度极快。
  2. **LLM 驱动的股票/交易分析系统**：多源行情 + 实时新闻 + 决策看板 + 自动推送的形态趋于成熟，且强调“零成本定时运行”。
  3. **本地化 LLM 推理引擎**：在消费级硬件上运行大规模 MoE 模型成为热点，C/Rust 实现、GPU/RAM/NVMe 分层推理架构值得关注。

- **是否出现新趋势**：出现。AI Agent 从“通用编码助手”向“垂直领域技能包”演进，金融/交易领域开始出现专门的 Claude skills（如 `claude-trading-skills`、`day-trader-skill`），这是本次快照最显著的新趋势。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源行情 + LLM 决策看板 + 自动推送”架构、`tick-stock-panel` 的“自托管 + DuckDB/Polars + FastAPI + React”量化工作台架构、`colibri` 的 GPU/RAM/NVMe 分层推理架构，均具备较高参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次快照中未发现明确骗局，但存在明显**关键词误匹配**问题——大量 awesome-list、UI 设计、面试题库、学术反抄袭工具因 README 中出现“fintech”“trading bot”“volatility”等词被错误纳入，实际与金融/量化无关。`Turnitout-Humanizer` 属于学术不端工具，不应作为灵感来源。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 154375 | +460 | +2891 | Python | AI 技能/UI | AI 驱动的跨平台 UI/UX 设计技能包 | 中 | 低 |
| 2 | elementalsouls/Claude-BugHunter | 23549 | +1515 | +11951 | Python | AI 安全/红队 | 85 个漏洞挖掘技能的 Claude Code 技能包 | 高 | 低 |
| 3 | GoogleChrome/modern-web-guidance | 26390 | +380 | +3346 | 无 | Web 最佳实践 | 让编码 Agent 保持最新 Web 最佳实践 | 中 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 340597 | +292 | +2118 | 无 | 自托管清单 | 自托管网络服务清单 | 低 | 中 |
| 5 | GoogleChrome/modern-web-guidance-src | 11132 | +216 | +2195 | TypeScript | Web 最佳实践 | 同上项目源码版 | 中 | 低 |
| 6 | codecrafters-io/build-your-own-x | 565633 | +244 | +1872 | Markdown | 教程清单 | 从零重建技术的教程合集 | 低 | 中 |
| 7 | vinta/awesome-python | 337212 | +204 | +1453 | Python | 资源清单 | Python 工具精选清单 | 低 | 低 |
| 8 | JustVugg/colibri | 53529 | +143 | +1479 | C | LLM 推理 | GPU/RAM/NVMe 分层 MoE 推理引擎 | 高 | 低 |
| 9 | public-apis/public-apis | 501545 | +247 | +1394 | Python | API 清单 | 免费公共 API 合集 | 低 | 中 |
| 10 | avelino/awesome-go | 196037 | +171 | +1315 | Go | 资源清单 | Go 框架与库精选清单 | 低 | 中 |
| 11 | ZhuLinsen/daily_stock_analysis | 74654 | +191 | +1241 | Python | AI 交易/量化 | LLM 多市场股票智能分析系统 | 高 | 低 |
| 12 | tradermonty/claude-trading-skills | 8509 | +138 | +1384 | Python | 交易技能包 | 股票投资者/交易员的 Claude 技能包 | 高 | 低 |
| 13 | nexu-io/open-design | 109576 | +174 | +1177 | TypeScript | AI 设计 | 协作式 AI 设计 Agent 工作台 | 中 | 低 |
| 14 | VoltAgent/awesome-design-md | 129132 | +140 | +944 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 合集 | 低 | 中 |
| 15 | Jakeschincariol/day-trader-skill | 9661 | +116 | +1001 | Python | 交易技能包 | 11 个日内交易 Claude 技能 | 高 | 低 |
| 16 | ifixai-ai/iFixAi | 47392 | +122 | +735 | Python | AI 审计/风控 | AI Agent 独立审计工具 | 高 | 低 |
| 17 | headroomlabs-ai/headroom | 80895 | +83 | +768 | Python | LLM 上下文压缩 | 压缩工具输出/日志/RAG 以节省 token | 高 | 低 |
| 18 | TauricResearch/TradingAgents | 123807 | +78 | +695 | TypeScript | AI 交易/多 Agent | 面向 Agentic 金融研究的多 Agent 框架 | 高 | 低 |
| 19 | CopilotKit/OpenBot | 13560 | +98 | +659 | TypeScript | AI Bot | 开源可自托管 AI Bot 替代品 | 中 | 中 |
| 20 | jaywcjlove/awesome-mac | 119406 | +89 | +545 | Swift | macOS 软件清单 | macOS 软件精选清单 | 低 | 低 |
| 21 | punkpeye/awesome-remote-mcp-servers | 4122 | +101 | +572 | 无 | MCP 清单 | 远程 MCP 服务器合集 | 中 | 中 |
| 22 | ripienaar/free-for-dev | 143692 | +83 | +523 | HTML | 免费资源清单 | 开发者免费 SaaS/PaaS 清单 | 低 | 低 |
| 23 | HKUDS/Vibe-Trading | 38954 | +112 | +445 | Python | AI 交易/回测 | 个人交易 Agent 框架 | 高 | 低 |
| 24 | kaankiziltug/logo-design-skill | 7807 | +110 | +492 | HTML | AI 设计技能 | Logo 设计 AI 技能包 | 低 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 58834 | +71 | +500 | Python | Claude 资源清单 | Claude Code 资源精选 | 中 | 低 |
| 26 | ashishpatel26/500-AI-Agents-Projects | 40757 | +31 | +660 | Python | AI Agent 案例 | 500 个 AI Agent 用例合集 | 中 | 中 |
| 27 | Open-Dev-Society/OpenStock | 22118 | +204 | +360 | TypeScript | 股票平台 | 开源实时行情与公司洞察平台 | 高 | 低 |
| 28 | sickn33/agentic-awesome-skills | 50356 | +56 | +382 | Python | AI 技能库 | 3000+ 可复用 AI Agent 技能 | 中 | 低 |
| 29 | ruvnet/ruflo | 82439 | +45 | +370 | TypeScript | Agent 编排 | 多 Agent 集群编排框架 | 中 | 低 |
| 30 | punkpeye/awesome-mcp-servers | 98522 | +41 | +363 | 无 | MCP 清单 | MCP 服务器合集 | 中 | 低 |
| 31 | garrytan/gbrain | 33607 | +41 | +313 | TypeScript | Agent 框架 | 个人 Agent Brain 框架 | 中 | 低 |
| 32 | perixtar/Tech-OA-Interview-Questions | 6274 | +123 | +148 | Python | 面试题库 | 科技公司 OA 面试题合集 | 低 | 低 |
| 33 | magnitudedev/magnitude | 8738 | +422 | 信息不足 | Rust | LLM 推理 | 跨 GPU/RAM/SSD 的本地推理引擎 | 高 | 低 |
| 34 | openbq-org/OpenBB | 75753 | +36 | +205 | Python | 金融数据平台 | 面向分析师/量化/AI Agent 的开放数据平台 | 高 | 中 |
| 35 | TGrpg/awesome-telegram | 2018 | +53 | +244 | JavaScript | Telegram 清单 | Telegram 频道/群组/机器人导航 | 低 | 中 |
| 36 | awesomedata/awesome-public-datasets | 80427 | +24 | +230 | 无 | 数据集清单 | 高质量开放数据集清单 | 中 | 中 |
| 37 | shy3130/tick-stock-panel | 8301 | +37 | +235 | Python | 量化工作台 | 自托管 A 股策略+监控+回测工作台 | 高 | 低 |
| 38 | FareedKhan-dev/kimi-k3-in-c | 12686 | +29 | +263 | C | LLM 推理 | 单 CPU 8.24GB 运行 2.78T 参数模型 | 高 | 低 |
| 39 | PurpleDoubleD/locally-uncensored | 4717 | +34 | +304 | TypeScript | 本地 AI | 桌面本地 AI 工作室 | 低 | 低 |
| 40 | AhmadHassan-BTed/Turnitout-Humanizer | 12660 | +28 | +237 | HTML | 学术反抄袭 | 学术抄袭规避工具 | 无 | 中 |
| 41 | RustingStudio/RustingStrata | 475 | +62 | +187 | Rust | LLM 推理 | 纯 Rust GGUF 推理引擎 | 中 | 低 |
| 42 | code-yeongyu/oh-my-openagent | 71128 | +27 | +132 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中 | 低 |
| 43 | rust-unofficial/awesome-rust | 60817 | +19 | +171 | Rust | 资源清单 | Rust 资源精选 | 低 | 中 |
| 44 | fffaraz/awesome-cpp | 74634 | +18 | +131 | 无 | 资源清单 | C/C++ 资源精选 | 低 | 低 |
| 45 | Developer-Y/cs-video-courses | 84994 | +8 | +109 | 无 | 课程清单 | CS 视频课程清单 | 低 | 中 |
| 46 | virattt/ai-hedge-fund | 64856 | +8 | +105 | Python | AI 交易/回测 | AI 对冲基金团队模拟 | 高 | 低 |
| 47 | josephmisiti/awesome-machine-learning | 74912 | +5 | +62 | Python | ML 资源清单 | 机器学习框架精选 | 低 | 低 |
| 48 | vuejs/awesome-vue | 73457 | -3 | -16 | 无 | 资源清单 | Vue.js 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis（排名 11）

- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：7 日涨星 +1241，总 star 74654，是本次快照中少数真正聚焦金融分析且涨星强劲的项目。LLM 与股票分析的结合点清晰，产品形态完整。
- **技术栈/架构亮点**：Python + LLM 驱动，多源数据接入，决策看板 + 自动推送。强调“零成本定时运行”，说明在成本控制上有工程考量。
- **是否适合借鉴**：非常适合。其“数据采集 → LLM 分析 → 看板呈现 → 自动推送”的流水线可直接迁移到企业级投研 Agent 或自动化报告生成场景。
- **可能风险**：LLM 输出可能存在幻觉，需注意分析结论的可靠性；A 股数据源合规性需确认；自动推送若涉及投资建议可能触及合规边界。

### 3.2 tradermonty/claude-trading-skills（排名 12）

- **解决什么问题**：为股票投资者和交易员提供 Claude Code 技能包，覆盖市场分析、技术图表、经济日历、选股器和策略开发。
- **为什么值得关注**：7 日涨星 +1384，是“AI Agent 技能包 + 交易”交叉领域的代表项目，增长极快。
- **技术栈/架构亮点**：以 Claude Code skills 形式封装交易工作流，将专业交易知识转化为可复用的 Agent 能力模块。
- **是否适合借鉴**：非常适合。这种“领域知识技能化”的思路可推广到风控、合规、研报生成等企业级 Agent 场景。
- **可能风险**：技能包质量依赖上游模型能力；交易分析类技能若被误用为自动交易信号，存在策略过拟合和资金风险。

### 3.3 TauricResearch/TradingAgents（排名 18）

- **解决什么问题**：面向 Agentic 金融研究的多 Agent 框架，模拟交易团队协作。
- **为什么值得关注**：总 star 123807，是 AI 多 Agent 金融研究方向的标杆项目之一，持续活跃。
- **技术栈/架构亮点**：TypeScript 实现，多 Agent 架构，将金融研究拆分为多个协作角色。
- **是否适合借鉴**：适合。多 Agent 角色分工（如分析师、风控、交易员）的架构模式可迁移到企业级投研 Agent 系统。
- **可能风险**：研究工具属性明显，不应直接用于实盘；多 Agent 系统的决策一致性和可审计性需要额外设计。

### 3.4 HKUDS/Vibe-Trading（排名 23）

- **解决什么问题**：个人交易 Agent 框架，整合算法交易、回测、组合优化等能力。
- **为什么值得关注**：HKUDS 出品，总 star 38954，匹配了大量量化相关查询，是学术机构在 AI 交易方向的代表性开源项目。
- **技术栈/架构亮点**：Python + LLM + MCP + 多 Agent，支持回测与组合优化。
- **是否适合借鉴**：适合作为研究原型参考，尤其是 MCP 在交易工具链中的集成方式。
- **可能风险**：研究工具属性，策略过拟合风险高；不应直接用于实盘交易。

### 3.5 shy3130/tick-stock-panel（排名 37）

- **解决什么问题**：自托管、零运维的 A 股量化工作台，支持自建策略、监控、回测，LLM 驱动策略定制与个股分析。
- **为什么值得关注**：技术栈现代且务实——DuckDB + Polars + FastAPI + React，是数据工程与量化结合的优质参考。
- **技术栈/架构亮点**：DuckDB 做本地分析型存储，Polars 做高性能数据处理，FastAPI 提供 API 层，React 做前端。LLM 用于策略定制和个股分析。
- **是否适合借鉴**：非常适合。这套“本地优先 + 列式存储 + 高性能 DataFrame + 轻量 API”的架构可直接复用到企业级量化研究平台。
- **可能风险**：A 股数据源合规性；LLM 生成策略的过拟合风险；自托管部署的维护成本。

### 3.6 virattt/ai-hedge-fund（排名 46）

- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作完成投资决策。
- **为什么值得关注**：总 star 64856，是 AI 多 Agent 投资决策的经典开源项目，虽然近期涨星放缓但生态影响力大。
- **技术栈/架构亮点**：Python 多 Agent 架构，模拟基金经理、分析师等角色。
- **是否适合借鉴**：适合作为多 Agent 投资决策流程的教学和研究参考。
- **可能风险**：纯研究/教育属性，回测结果不代表实盘表现；不应直接用于真实资金管理。

### 3.7 ifixai-ai/iFixAi（排名 16）

- **解决什么问题**：AI Agent 的独立审计，回答“Agent 是否在做它应该做的事”，120 秒内给出结论。
- **为什么值得关注**：总 star 47392，7 日涨星 +735，AI Agent 治理与审计是当前企业级落地的关键缺口。
- **技术栈/架构亮点**：Python + CLI，覆盖 AI 对齐、幻觉检测、提示注入、NIST AI RMF、ISO 42001、EU AI Act 等合规框架。
- **是否适合借鉴**：非常适合。金融场景中 AI Agent 的可审计性、合规性需求强烈，该项目的审计思路可直接借鉴到交易 Agent 的监控与风控层。
- **可能风险**：审计工具本身依赖 LLM 判断，可能存在误判；需结合人工复核。

### 3.8 headroomlabs-ai/headroom（排名 17）

- **解决什么问题**：在工具输出、日志、文件、RAG 块进入 LLM 前进行压缩，节省 20%-95% token。
- **为什么值得关注**：总 star 80895，7 日涨星 +768。在金融数据密集型 Agent 场景中，上下文成本是核心瓶颈。
- **技术栈/架构亮点**：Python，提供库、代理和 MCP 服务器三种形态，支持 FastAPI、LangChain 等生态。
- **是否适合借鉴**：非常适合。量化 Agent 需要处理大量行情、订单簿、新闻数据，上下文压缩能显著降低成本并提升响应速度。
- **可能风险**：压缩可能丢失关键信息，需在金融场景中验证压缩后决策质量不下降。

### 3.9 JustVugg/colibri（排名 8）

- **解决什么问题**：在消费级硬件上运行大规模 MoE 模型，热专家在 GPU、温专家在 RAM、冷专家从 NVMe 流式加载。
- **为什么值得关注**：总 star 53529，7 日涨星 +1479，C 语言实现，是本地化 LLM 推理的代表性工程。
- **技术栈/架构亮点**：分层推理架构（GPU/RAM/NVMe），C 语言实现，支持 CUDA 和 Vulkan。
- **是否适合借鉴**：适合。金融场景对数据隐私和本地部署有强需求，分层推理架构可降低本地 LLM 部署的硬件门槛。
- **可能风险**：C 语言项目的维护复杂度高；性能优化依赖特定硬件。

### 3.10 Open-Dev-Society/OpenStock（排名 27）

- **解决什么问题**：开源股票市场平台，提供实时行情、个性化提醒和公司洞察。
- **为什么值得关注**：24h 涨星 +204，总 star 22118，TypeScript + Next.js + shadcn-ui 技术栈，是金融数据产品 UI/UX 的优质参考。
- **技术栈/架构亮点**：Next.js + shadcn-ui + TailwindCSS + Inngest，现代前端与后台任务架构。
- **是否适合借鉴**：适合。金融数据产品的信息架构、实时行情展示、提醒系统设计均可参考。
- **可能风险**：数据源授权和实时性需确认；AGPL-3.0 许可证对商业化有约束。

## 4. 趋势归纳

### 技术趋势
- **AI Agent 技能包化**：从通用 Agent 向垂直领域技能包演进，交易、安全、设计等领域均出现专门技能包。
- **本地化 LLM 推理**：C/Rust 实现的分层推理引擎（GPU/RAM/NVMe）成为热点，降低本地部署门槛。
- **上下文工程**：token 压缩、上下文管理成为 Agent 基础设施的关键组件。
- **MCP 生态扩张**：远程 MCP 服务器清单项目快速增长，MCP 正在成为 Agent 工具接入的事实标准。

### 产品趋势
- **LLM 驱动的投研工作台**：从单一分析工具向“数据 + 分析 + 看板 + 推送”的一体化产品演进。
- **自托管优先**：金融数据产品强调自托管、本地优先、零运维，反映数据隐私和成本诉求。
- **AI Agent 审计与治理**：随着 Agent 在金融场景落地，独立审计和合规工具需求上升。

### 量化/交易策略趋势
- **多 Agent 协作研究**：TradingAgents、Vibe-Trading、ai-hedge-fund 均采用多 Agent 角色分工模式。
- **LLM 辅助策略开发**：从 LLM 直接生成交易信号，转向 LLM 辅助策略定制、个股分析和复盘。
- **回测与监控一体化**：tick-stock-panel 等将回测、监控、策略管理整合到统一工作台。

### AI Agent 与自动化交易结合趋势
- **技能包形态的交易辅助**：claude-trading-skills、day-trader-skill 将交易分析能力封装为 Agent 技能，而非直接执行交易。
- **研究辅助优先于自动执行**：当前主流项目定位为“研究工具”而非“自动交易 bot”，风险意识较强。
- **可审计性成为刚需**：iFixAi 等项目的兴起表明，Agent 在金融场景的落地需要审计和治理能力支撑。

### 值得后续做原型验证的方向
- 基于 MCP 的金融数据 Agent 工具链
- LLM 投研报告自动生成流水线
- 本地化 LLM 推理 + 金融数据隐私保护方案
- Agent 交易决策的可审计日志系统
- 上下文压缩在金融数据密集型 Agent 中的效果验证

## 5. 今日灵感清单

1. **MVP：金融投研日报 Agent**：参考 `daily_stock_analysis` 架构，用 Codex/Claude 自动采集多源行情 + 新闻，生成结构化投研日报并推送。可先做单市场、单资产类别的最小闭环。

2. **MVP：交易技能包**：参考 `claude-trading-skills` 和 `day-trader-skill`，将技术指标计算、图表生成、经济日历查询封装为 Claude Code skills，验证“领域知识技能化”的可行性。

3. **调研：MCP 金融数据服务器生态**：基于 `awesome-remote-mcp-servers` 和 `awesome-mcp-servers`，梳理现有金融数据 MCP 服务器的覆盖范围和缺口，形成选型报告。

4. **调研：本地化 LLM 推理在金融场景的可行性**：基于 `colibri`、`magnitude`、`kimi-k3-in-c`，评估在消费级硬件上运行本地 LLM 进行金融文本分析的性能与成本。

5. **Demo：Agent 决策审计日志**：参考 `iFixAi` 的审计思路，为 TradingAgents 或 Vibe-Trading 的多 Agent 决策流程增加可审计日志层，记录每个 Agent 的输入、输出和决策依据。

6. **Demo：上下文压缩在金融数据管道中的应用**：用 `headroom` 对订单簿、行情、新闻等金融数据流进行压缩，对比压缩前后的 token 消耗和下游分析质量。

7. **原型：DuckDB + Polars 量化研究工作台**：参考 `tick-stock-panel`，用 DuckDB 做本地行情存储、Polars 做因子计算、FastAPI 暴露 API，搭建轻量量化研究环境。

8. **Watchlist：OpenBB**：作为金融数据平台，其“面向分析师、量化、AI Agent”的定位与当前 Agent 化趋势高度契合，值得持续跟踪其 AI Agent 集成能力演进。

9. **Watchlist：TradingAgents**：多 Agent 金融研究的标杆项目，关注其架构演进和 MCP 集成进展。

10. **Watchlist：OpenStock**：金融数据产品 UI/UX 参考，关注其数据源扩展和功能迭代。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | LLM 股票分析产品形态完整，涨星强劲，适合跟踪产品演进 |
| tradermonty/claude-trading-skills | 交易技能包代表项目，验证 Agent 技能化趋势 |
| TauricResearch/TradingAgents | 多 Agent 金融研究标杆，学术影响力大 |
| HKUDS/Vibe-Trading | 学术机构 AI 交易框架，MCP 集成值得关注 |
| shy3130/tick-stock-panel | DuckDB + Polars 量化工作台架构优秀 |
| ifixai-ai/iFixAi | AI Agent 审计与治理，金融合规刚需 |
| headroomlabs-ai/headroom | 上下文压缩，金融数据密集型 Agent 的成本优化关键 |
| JustVugg/colibri | 本地化 LLM 推理，金融数据隐私场景有潜力 |
| openbq-org/OpenBB | 金融数据平台，AI Agent 集成方向值得跟踪 |
| Open-Dev-Society/OpenStock | 金融数据产品 UI/UX 参考 |
| virattt/ai-hedge-fund | AI 多 Agent 投资决策经典项目，教学价值高 |
| Jakeschincariol/day-trader-skill | 日内交易技能包，与 claude-trading-skills 互补 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次快照提供了 `baseline_1d`（2026-11-24）和 `baseline_7d`（2026-11-18），1 日和 7 日涨星数据基本完整。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 null，无法评估中期涨星趋势。
- **7 日涨星缺失**：`magnitudedev/magnitude`（排名 33）的 `star_delta_7d` 为 null，仅有 24h 涨星数据，7 日趋势信息不足。
- **关键词误匹配严重**：大量项目因 README 或描述中偶然出现“fintech”“trading bot”“volatility”“quant”等词被纳入，实际与金融/量化无关。典型如 `awesome-selfhosted`、`build-your-own-x`、`awesome-mac`、`Tech-OA-Interview-Questions`、`Turnitout-Humanizer`、`cs-video-courses` 等。这导致本次候选集的**信噪比较低**，真正与金融/量化/交易相关的项目约占三分之一。
- **样本偏差**：候选集偏向高 star、高涨星的“热门项目”，且大量 awesome-list 类项目占据排名，可能掩盖中小型但更聚焦的金融/量化项目。
- **分类标签不可全信**：`category_guess` 和 `risk_flags` 由匹配规则自动生成，存在明显误判（如将 `awesome-selfhosted` 标记为 trading_bot），需结合项目实际内容人工判断。
