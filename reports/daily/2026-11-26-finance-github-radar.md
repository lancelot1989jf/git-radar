# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-26

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能包与审计框架**：Claude Code / Codex 技能包正在从“通用编码”向“垂直金融场景”渗透，例如 `claude-trading-skills`、`day-trader-skill`、`iFixAi`。
  2. **LLM 驱动的股票分析与交易研究**：`daily_stock_analysis`、`TradingAgents`、`Vibe-Trading` 等项目持续高增长，显示“多智能体 + 金融研究”仍是热门方向。
  3. **本地化/自托管 AI 推理与数据基础设施**：`colibri`、`magnitude`、`kimi-k3-in-c` 等项目表明，在消费级硬件上运行大模型推理正在成为工程热点，对量化研究的数据处理与模型部署有间接借鉴意义。

- **是否出现新趋势**：出现。AI Agent 的“技能化”趋势明显——大量项目以 skill bundle 形式发布，强调可插拔、可组合、面向 Claude Code / Codex / Cursor 等编码代理。金融场景中，这类技能包开始覆盖行情分析、技术图表、回测、交易策略开发。

- **是否出现值得复刻/参考的工程架构**：是。`iFixAi` 的“AI Agent 独立审计”思路、`headroom` 的“LLM 上下文压缩”方案、`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送”架构，都值得在金融 Agent 产品中参考。

- **是否有明显骗局、过度营销或高风险项目**：有。`Turnitout-Humanizer` 宣称可绕过 Turnitin、GPTZero 等学术查重系统，属于明显学术不端工具，不应借鉴。`polymarket-perp-dex-hyperliquid-vault-market-maker-saceron` 与 `solana-swap-api` 涉及预测市场做市、DEX 聚合与套利，风险等级较高，需谨慎对待。

---

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ui-ux-pro-max-skill | 154796 | +421 | +2884 | Python | AI 技能/UI 设计 | 面向多平台的 UI/UX 设计智能技能包 | 中 | 低 |
| 2 | Claude-BugHunter | 25166 | +1617 | +12147 | Python | AI 安全/红队 | Claude Code 漏洞挖掘与红队技能包 | 高 | 低 |
| 3 | modern-web-guidance | 26842 | +452 | +3208 | 无 | Web 最佳实践 | 为编码代理提供最新 Web 最佳实践 | 中 | 低 |
| 4 | awesome-selfhosted | 340912 | +315 | +2154 | 无 | 自托管清单 | 自托管网络服务与应用清单 | 中 | 中 |
| 5 | build-your-own-x | 565853 | +220 | +1847 | Markdown | 教程清单 | 从零重建技术的教程合集 | 中 | 中 |
| 6 | modern-web-guidance-src | 11335 | +203 | +2031 | TypeScript | Web 最佳实践 | 编码代理 Web 最佳实践源项目 | 中 | 低 |
| 7 | awesome-python | 337422 | +210 | +1480 | Python | Python 清单 | Python 工具与库精选清单 | 中 | 低 |
| 8 | daily_stock_analysis | 74929 | +275 | +1417 | Python | AI 交易/量化 | LLM 多市场股票智能分析系统 | 高 | 低 |
| 9 | public-apis | 501724 | +179 | +1343 | Python | API 清单 | 免费公共 API 合集 | 中 | 中 |
| 10 | awesome-go | 196233 | +196 | +1346 | Go | Go 清单 | Go 框架与库精选清单 | 中 | 中 |
| 11 | colibri | 53635 | +106 | +1328 | C | 推理引擎 | 分层 MoE 推理引擎，GPU/RAM/NVMe 混合 | 高 | 低 |
| 12 | iFixAi | 47543 | +151 | +1331 | Python | AI 审计/风控 | AI Agent 独立审计与合规评估 | 高 | 低 |
| 13 | claude-trading-skills | 8654 | +145 | +1346 | Python | 交易技能/回测 | Claude Code 股票投资与交易技能包 | 高 | 低 |
| 14 | open-design | 109730 | +154 | +1143 | TypeScript | AI 设计协作 | 协作式 AI 设计 Agent 工作区 | 中 | 低 |
| 15 | awesome-design-md | 129306 | +174 | +969 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 合集 | 中 | 中 |
| 16 | day-trader-skill | 9822 | +161 | +997 | Python | 日内交易/回测 | 11 个 Claude 日内交易技能 | 高 | 低 |
| 17 | awesome-mac | 119619 | +213 | +690 | Swift | macOS 软件清单 | macOS 高质量软件清单 | 低 | 低 |
| 18 | OpenBot | 13712 | +152 | +710 | TypeScript | AI Bot 框架 | 开源可自托管 AI Bot 替代方案 | 高 | 中 |
| 19 | headroom | 80966 | +71 | +782 | Python | LLM 上下文压缩 | 压缩工具输出、日志、RAG 片段以降低 token | 高 | 低 |
| 20 | Tech-OA-Interview-Questions | 6918 | +644 | +786 | Python | 面试题库 | 科技公司 OA 与面试题每日更新 | 低 | 低 |
| 21 | free-for-dev | 143792 | +100 | +554 | HTML | 免费资源清单 | SaaS/PaaS/IaaS 免费层清单 | 低 | 低 |
| 22 | TradingAgents | 123879 | +72 | +666 | TypeScript | AI 交易/多智能体 | 面向 Agentic 金融研究的多智能体框架 | 高 | 低 |
| 23 | awesome-remote-mcp-servers | 4219 | +97 | +585 | 无 | MCP 清单 | 远程 MCP 服务器合集 | 中 | 中 |
| 24 | OpenStock | 22312 | +194 | +523 | TypeScript | 股票行情 | 开源实时行情与公司洞察平台 | 高 | 低 |
| 25 | logo-design-skill | 7903 | +96 | +526 | HTML | AI 设计技能 | Claude/Gemini/Codex 的 Logo 设计技能 | 低 | 低 |
| 26 | Vibe-Trading | 39030 | +76 | +456 | Python | AI 交易/回测 | “Vibe-Trading”个人交易 Agent | 高 | 低 |
| 27 | ruflo | 82525 | +86 | +397 | TypeScript | Agent 编排 | 多智能体 swarm 编排与自适应记忆 | 高 | 低 |
| 28 | awesome-claude-code | 58899 | +65 | +495 | Python | Claude Code 清单 | Claude Code 资源与技能精选 | 中 | 低 |
| 29 | 500-AI-Agents-Projects | 40791 | +34 | +660 | Python | AI Agent 案例 | 500 个 AI Agent 行业用例合集 | 中 | 中 |
| 30 | awesome-remote-job | 51274 | +112 | +457 | 无 | 远程工作清单 | 远程工作与资源清单 | 低 | 低 |
| 31 | awesome-public-datasets | 80520 | +93 | +308 | 无 | 数据集清单 | 高质量开放数据集清单 | 中 | 中 |
| 32 | agentic-awesome-skills | 50422 | +66 | +407 | Python | AI 技能库 | 3000+ 可复用 AI Agent 技能 | 高 | 低 |
| 33 | gbrain | 33647 | +40 | +323 | TypeScript | Agent 框架 | Garry 的 OpenClaw/Hermes Agent Brain | 中 | 低 |
| 34 | awesome-mcp-servers | 98560 | +38 | +274 | 无 | MCP 清单 | MCP 服务器合集 | 中 | 低 |
| 35 | awesome-systematic-trading | 15823 | +117 | +360 | Python | 系统化交易清单 | 系统化交易库、策略、书籍清单 | 高 | 中 |
| 36 | magnitude | 8998 | +260 | 信息不足 | Rust | 推理引擎 | 跨 GPU/RAM/SSD 的本地推理引擎 | 高 | 低 |
| 37 | tick-stock-panel | 8342 | +41 | +246 | Python | A 股量化工作台 | 自托管 A 股策略+监控+回测工作台 | 高 | 低 |
| 38 | kimi-k3-in-c | 12723 | +37 | +242 | C | 推理引擎 | 单 CPU 8.24GB 内存运行 Kimi K3 | 高 | 低 |
| 39 | OpenBB | 75785 | +32 | +198 | Python | 金融数据平台 | 面向分析师、量化与 AI Agent 的开放数据平台 | 高 | 中 |
| 40 | awesome-rust | 60854 | +37 | +188 | Rust | Rust 清单 | Rust 代码与资源精选 | 中 | 中 |
| 41 | Turnitout-Humanizer | 12689 | +29 | +239 | HTML | 学术不端工具 | 宣称可绕过 Turnitin/GPTZero 的查重工具 | 低 | 中 |
| 42 | Financial-API | 4647 | +26 | +280 | HTML | A 股数据服务 | 同花顺官方 A 股金融数据 API/MCP/CLI | 高 | 低 |
| 43 | quantconnect-lean-selvon-research | 200 | +152 | +106 | Go | 回测/量化 | QuantConnect Lean 策略实验与回测环境 | 中 | 中 |
| 44 | locally-uncensored | 4740 | +23 | +263 | TypeScript | 本地 AI 工作室 | 本地 AI 聊天/图像/视频/编码代理 | 中 | 低 |
| 45 | oh-my-openagent | 71150 | +22 | +137 | TypeScript | Agent 编排 | 图形工程 Agent 编排工具 | 中 | 低 |
| 46 | solana-swap-api | 2948 | +167 | +243 | JavaScript | Solana 交易 | Solana Swap API 与 Router | 中 | 高 |
| 47 | awesome-cpp | 74649 | +15 | +129 | 无 | C++ 清单 | C/C++ 框架与库精选 | 中 | 低 |
| 48 | cs-video-courses | 84999 | +5 | +108 | 无 | 课程清单 | 计算机科学视频课程清单 | 低 | 中 |
| 49 | ai-hedge-fund | 64870 | +14 | +104 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 50 | awesome-machine-learning | 74922 | +10 | +67 | Python | ML 清单 | 机器学习框架与库精选 | 中 | 低 |
| 51 | awesome-vue | 73457 | 0 | -14 | 无 | Vue 清单 | Vue.js 资源精选 | 低 | 低 |
| 52 | polymarket-perp-dex-hyperliquid-vault-market-maker-saceron | 188 | +179 | 信息不足 | HTML | 预测市场做市 | Polymarket/perp DEX/Hyperliquid 金库做市 | 低 | 中 |

---

## 3. 重点项目深度分析

### 3.1 daily_stock_analysis
- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：24h +275、7d +1417，总 star 74929，是本次候选中金融属性最强、增长最稳的项目之一。它把“LLM + 多源数据 + 决策看板 + 自动推送”打包成一个可运行产品，而不是单纯的研究代码。
- **技术栈/架构亮点**：Python；多源行情接入；实时新闻；决策看板；自动推送；零成本定时运行。架构上强调“数据采集—LLM 分析—看板展示—通知触达”的闭环。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：适合。其“多源数据 + LLM 决策 + 看板 + 推送”的闭环非常适合企业级投研 Agent 的 MVP 设计。但要注意，它更偏分析辅助，不应直接当作自动下单系统。
- **可能的风险**：金融合规风险；LLM 输出可能包含幻觉；行情数据源稳定性；若扩展为自动交易，存在策略过拟合与资金风险。

### 3.2 TradingAgents
- **解决什么问题**：面向 Agentic 金融研究的多智能体框架，模拟交易研究流程。
- **为什么值得关注**：总 star 123879，7d +666，是“多智能体 + 金融”方向的代表性项目。TypeScript 实现，说明其工程化程度较高。
- **技术栈/架构亮点**：TypeScript；多智能体（multiagent）；LLM；finance；trading。强调 Agent 之间的分工与协作。
- **是否适合借鉴**：非常适合。多智能体分工、研究流程编排、金融领域 Agent 设计都值得参考。可作为企业级投研 Agent 的架构蓝本。
- **可能的风险**：研究工具属性强，不应直接用于实盘；LLM 决策存在不可解释性；策略过拟合风险。

### 3.3 Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多智能体与回测。
- **为什么值得关注**：HKUDS 出品，总 star 39030，7d +456。项目名“Vibe-Trading”反映了当前“氛围编码/氛围交易”的文化趋势，但工程上仍包含回测与多智能体设计。
- **技术栈/架构亮点**：Python；ai-agent；algorithmic-trading；backtesting；llm；mcp；multi-agent。
- **是否适合借鉴**：适合作为“LLM + 回测 + 多智能体”组合的研究原型。MCP 的引入值得关注，可能用于工具调用标准化。
- **可能的风险**：研究工具属性；策略过拟合；回测幸存者偏差；“Vibe”定位可能弱化风控严肃性。

### 3.4 iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，可在 120 秒内给出结果。
- **为什么值得关注**：7d +1331，总 star 47543。AI Agent 审计、对齐、治理是当前 AI 经济中的关键缺口，尤其对金融场景的 Agent 合规至关重要。
- **技术栈/架构亮点**：Python；agent-evaluation；ai-governance；hallucination-detection；prompt-injection；risk-assessment；支持 NIST AI RMF、ISO 42001、EU AI Act、OWASP LLM 等框架。
- **是否适合借鉴**：非常适合。金融企业如果部署 AI Agent，必须引入类似的审计与合规层。可将其思路复刻为“交易 Agent 行为审计”模块。
- **可能的风险**：审计工具本身可能存在误报/漏报；对复杂 Agent 行为的覆盖度有限；不应替代正式合规审查。

### 3.5 claude-trading-skills
- **解决什么问题**：为 Claude Code 提供股票投资与交易技能，包括市场分析、技术图表、经济日历、筛选器与交易策略开发。
- **为什么值得关注**：7d +1346，虽然总 star 仅 8654，但增速极高，说明“Claude Code + 交易技能”这一细分方向正在快速升温。
- **技术栈/架构亮点**：Python；以 skill 形式组织；覆盖分析、图表、日历、筛选、策略开发。
- **是否适合借鉴**：适合。可借鉴其“技能包”设计，将投研流程拆分为可复用、可组合的 Agent 技能。
- **可能的风险**：研究工具属性；技能包可能诱导用户直接实盘；策略开发缺乏严格风控。

### 3.6 day-trader-skill
- **解决什么问题**：11 个 Claude 日内交易技能，扫描数千张图表、跟踪突发新闻、计时进出场、回放结果。
- **为什么值得关注**：24h +161、7d +997，总 star 9822。日内交易技能包是“AI + 交易”最激进的方向之一。
- **技术栈/架构亮点**：Python；claude-skills；backtesting；day-trading；stock-market。
- **是否适合借鉴**：可借鉴其“扫描—跟踪—计时—回放”的日内交易工作流设计，但不应直接用于实盘。
- **可能的风险**：日内交易本身高风险；技能包可能鼓励高频操作；回测结果可能过度乐观；缺乏真实滑点与手续费建模。

### 3.7 headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 片段进入 LLM 前进行压缩，降低 token 消耗，同时保持答案质量。
- **为什么值得关注**：总 star 80966，7d +782。对金融 Agent 而言，行情数据、新闻、日志等上下文往往非常庞大，上下文压缩是控制成本与延迟的关键。
- **技术栈/架构亮点**：Python；library、proxy、MCP server 三种形态；支持 Claude Code、Cursor、LangChain、OpenAI 等。
- **是否适合借鉴**：非常适合。金融 Agent 通常需要处理大量行情与新闻数据，可引入类似压缩层以降低 token 成本。
- **可能的风险**：压缩可能丢失关键信息；对数值型金融数据的压缩需谨慎验证。

### 3.8 OpenStock
- **解决什么问题**：开源替代昂贵市场平台，提供实时价格、个性化提醒与公司洞察。
- **为什么值得关注**：24h +194，总 star 22312。作为产品型项目，其“实时行情 + 提醒 + 公司洞察”的组合对金融产品设计有直接参考价值。
- **技术栈/架构亮点**：TypeScript；Next.js；shadcn-ui；TailwindCSS；Inngest；Coderabbit。
- **是否适合借鉴**：适合。可作为金融数据产品的前端与产品体验参考，尤其是实时行情与提醒机制。
- **可能的风险**：数据源授权与合规；实时行情延迟；产品定位偏零售用户。

### 3.9 tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析与复盘。
- **为什么值得关注**：7d +246，总 star 8342。A 股量化工作台 + LLM 能力 + DuckDB/Polars 数据栈，工程组合较新颖。
- **技术栈/架构亮点**：Python；FastAPI；DuckDB；Polars；React；LLM；backtesting；screener。
- **是否适合借鉴**：非常适合。DuckDB + Polars 的本地量化数据栈、FastAPI + React 的工作台架构、LLM 辅助策略定制，都值得复刻。
- **可能的风险**：A 股数据合规；策略过拟合；自托管环境的数据更新与运维成本。

### 3.10 ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 协作进行投资研究。
- **为什么值得关注**：总 star 64870，是“AI 对冲基金”方向的经典项目。虽然近期增速放缓，但架构仍具参考价值。
- **技术栈/架构亮点**：Python；多 Agent 协作；回测。
- **是否适合借鉴**：适合作为多 Agent 投研流程的教学与原型参考。
- **可能的风险**：研究工具属性；策略过拟合；不应直接用于实盘。

---

## 4. 趋势归纳

### 技术趋势
- **AI Agent 技能化**：大量项目以 skill bundle 形式发布，面向 Claude Code、Codex、Cursor、Gemini CLI 等编码代理，强调可插拔、可组合。
- **本地推理引擎兴起**：`colibri`、`magnitude`、`kimi-k3-in-c` 等项目聚焦在消费级硬件上运行大模型，采用 GPU/RAM/NVMe 分层、量化、SIMD 等技术。
- **上下文压缩成为基础设施**：`headroom` 等项目将 LLM 上下文压缩作为独立基础设施层，对金融 Agent 的成本控制有重要意义。
- **MCP 生态扩张**：`awesome-mcp-servers`、`awesome-remote-mcp-servers` 等清单项目持续增长，MCP 正在成为 Agent 工具调用的标准接口。

### 产品趋势
- **从“交易机器人”到“投研 Agent”**：项目重心从自动下单转向研究、分析、决策辅助，例如 `daily_stock_analysis`、`TradingAgents`、`OpenStock`。
- **自托管与本地优先**：`OpenStock`、`tick-stock-panel`、`locally-uncensored` 等项目强调自托管、本地运行、隐私保护。
- **AI Agent 审计与治理产品化**：`iFixAi` 代表了一个新品类——Agent 审计与合规工具。

### 量化/交易策略趋势
- **LLM 辅助策略开发**：`claude-trading-skills`、`tick-stock-panel`、`Vibe-Trading` 等项目将 LLM 引入策略开发、筛选与复盘。
- **多智能体投研流程**：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 均采用多智能体分工。
- **回测仍是核心组件**：多数交易相关项目都包含 backtesting 模块，但需警惕过拟合与幸存者偏差。

### AI Agent 与自动化交易结合趋势
- **技能包 + 交易场景**：Claude Code 技能包开始覆盖市场分析、技术图表、日内交易、策略开发。
- **MCP 作为交易工具接口**：`Vibe-Trading`、`Financial-API` 等项目引入 MCP，可能成为未来交易 Agent 工具标准化的方向。
- **审计与风控 Agent 化**：`iFixAi` 表明，Agent 审计本身也可以由 Agent 执行，形成“Agent 审计 Agent”的闭环。

### 值得后续做原型验证的方向
- 基于 MCP 的金融数据服务标准化。
- LLM 上下文压缩在金融 Agent 中的应用。
- 多智能体投研流程的工程化编排。
- 本地推理引擎在量化研究中的部署可行性。
- AI Agent 行为审计与金融合规的结合。

---

## 5. 今日灵感清单

1. **MVP：金融投研 Agent 技能包**  
   参考 `claude-trading-skills` 和 `day-trader-skill`，做一个面向 A 股/美股的 Claude Code 技能包，包含行情摘要、技术图表、新闻情绪、回测建议四个技能，先做研究辅助，不做自动下单。

2. **MVP：Agent 行为审计看板**  
   参考 `iFixAi`，为内部 AI Agent 构建一个轻量审计看板，记录 Agent 的输入、输出、工具调用、异常行为，输出风险评分。可先用于投研 Agent 的合规监控。

3. **调研：MCP 在金融数据服务中的标准化**  
   调研 `Financial-API`、`Vibe-Trading`、`awesome-remote-mcp-servers`，评估用 MCP 封装行情、财报、新闻数据源的可行性。

4. **调研：LLM 上下文压缩对金融 Agent 成本的影响**  
   参考 `headroom`，测试在行情数据、新闻流、日志等场景下，上下文压缩对 token 成本和分析质量的影响。

5. **Demo：本地推理引擎运行量化研究模型**  
   参考 `colibri`、`magnitude`、`kimi-k3-in-c`，验证在本地消费级硬件上运行小型金融 NLP 模型或因子模型的可行性。

6. **Demo：DuckDB + Polars 本地量化数据工作台**  
   参考 `tick-stock-panel`，用 DuckDB + Polars 构建一个本地 A 股/美股数据工作台，支持快速筛选、回测与 LLM 辅助分析。

7. **Codex/Agent 自动复现：多智能体投研流程**  
   参考 `TradingAgents` 和 `ai-hedge-fund`，让 Codex 自动复现一个简化版多智能体投研流程，包含“数据采集—分析—辩论—决策”四个 Agent。

8. **Watchlist：OpenStock**  
   关注其产品化路径，尤其是实时行情、提醒机制与公司洞察的交互设计。

9. **Watchlist：iFixAi**  
   关注 AI Agent 审计与合规工具的产品化进展，评估是否可集成到金融 Agent 平台。

10. **Watchlist：headroom**  
    关注上下文压缩技术的演进，评估其在金融 Agent 成本优化中的长期价值。

---

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| daily_stock_analysis | 金融属性强、增长稳，LLM + 多源数据 + 看板 + 推送的闭环值得持续跟踪 |
| TradingAgents | 多智能体金融研究代表项目，架构演进值得关注 |
| Vibe-Trading | HKUDS 出品，LLM + MCP + 回测组合，学术与工程结合 |
| iFixAi | AI Agent 审计与合规新品类，金融 Agent 落地的关键基础设施 |
| claude-trading-skills | 交易技能包增速极高，代表“Claude Code + 金融”细分方向 |
| headroom | LLM 上下文压缩基础设施，对金融 Agent 成本控制有直接价值 |
| tick-stock-panel | DuckDB + Polars + LLM 的 A 股量化工作台，工程组合新颖 |
| OpenStock | 开源金融数据产品，产品体验与实时行情机制值得参考 |
| colibri / magnitude | 本地推理引擎，可能影响量化研究的模型部署方式 |
| Financial-API | 同花顺官方 A 股数据服务，支持 API/MCP/CLI，数据源标准化方向 |

---

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

特别提醒：
- `solana-swap-api`、`polymarket-perp-dex-hyperliquid-vault-market-maker-saceron` 等涉及 DEX、预测市场、做市、套利的项目风险等级较高，不要直接使用真实资金或 API Key。
- `Turnitout-Humanizer` 属于学术不端工具，不应借鉴或使用。
- 任何回测结果都可能存在幸存者偏差、过拟合、未建模滑点与手续费等问题。
- GitHub star 和涨星只反映社区关注度，不反映策略收益或项目安全性。

---

## 8. 数据质量说明

- **基线情况**：本次报告使用了 `baseline_1d: 2026-11-25.json` 和 `baseline_7d: 2026-11-19.json`，1 日与 7 日基线均存在。
- **缺失字段**：部分项目的 `star_delta_30d` 为 null，`magnitude` 与 `polymarket-perp-dex-hyperliquid-vault-market-maker-saceron` 的 `star_delta_7d` 为 null，报告已标注“信息不足”。
- **样本偏差**：候选项目由关键词匹配生成，大量项目为 awesome-list、教程、设计工具等非金融项目，真正与金融/量化/交易直接相关的项目占比有限。部分项目因关键词误匹配进入候选，例如 `Turnitout-Humanizer`、`Tech-OA-Interview-Questions`、`awesome-mac` 等。
- **分类噪声**：`category_guess` 与 `risk_flags` 为自动推断结果，存在误分类可能。例如 `awesome-selfhosted`、`build-your-own-x` 被标记为 trading_bot，但实际并非交易机器人。
- **采集失败**：本次数据未显示明显采集失败，但 `star_delta_30d` 普遍缺失，说明 30 日基线未纳入本次计算。
