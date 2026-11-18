# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-17

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的股票分析与交易 Agent 技能包**：`daily_stock_analysis`、`claude-trading-skills`、`day-trader-skill` 等项目显示，Claude/Codex 技能化正在快速渗透到股票分析、技术图表、日内交易复盘等场景。
  2. **AI Agent 治理与审计**：`iFixAi` 以“AI Agent 独立审计”为切入点，覆盖 AI 对齐、幻觉检测、提示注入、ISO 42001、NIST AI RMF 等治理维度，对金融场景中的 Agent 风控有直接借鉴意义。
  3. **本地优先 / 自托管 AI 基础设施**：`colibri`、`kimi-k3-in-c`、`locally-uncensored` 等项目体现“在自有硬件上运行前沿模型”的趋势，对量化研究中的数据隐私与低成本推理有工程参考价值。

- **是否出现新趋势**：  
  出现。候选集中大量项目以 **“Claude/Codex Skill”** 形态发布，将交易分析、回测、风控、UI 设计、安全测试封装为可被编码 Agent 调用的技能包。这标志着 AI Agent 与金融工具的结合正从“框架级”走向“技能/插件级”的模块化复用。

- **是否出现值得复刻/参考的工程架构**：  
  出现。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `tick-stock-panel` 的“自托管 + DuckDB + Polars + FastAPI + React + LLM 策略定制”组合，适合作为轻量级量化研究工作台原型参考。

- **是否有明显骗局、过度营销或高风险项目**：  
  候选集中存在少量高风险信号，例如 `Turnitout-Humanizer` 宣称绕过 Turnitin、GPTZero 等检测，属于学术诚信灰色地带；`purffle-copybot` 涉及 Hyperliquid 跟单交易，且仓库极新、无 license、无 fork，需谨慎对待。另有多个项目因匹配到 “trading bot” 关键词而被标记为中风险，但实际内容为 awesome-list 或通用工具，需人工甄别。

---

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 73191 | +258 | +3556 | Python | AI 交易/数据工程/量化研究 | LLM 驱动的多市场股票智能分析系统 | 高：多源数据融合与自动推送架构 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 151056 | +462 | +3138 | Python | 金融科技产品 | 多平台 UI/UX 设计智能技能 | 中：Agent 生成金融看板 UI | 低 |
| 3 | elementalsouls/Claude-BugHunter | 9984 | +2162 | +4462 | Python | 金融科技产品 | Claude 漏洞挖掘与红队技能包 | 中：金融系统安全测试自动化 | 低 |
| 4 | tradermonty/claude-trading-skills | 6942 | +337 | +3185 | Python | 回测 | 股票投资者与交易者的 Claude 技能包 | 高：交易分析技能化 | 低 |
| 5 | awesome-selfhosted/awesome-selfhosted | 338194 | +356 | +2282 | 无 | 交易机器人 | 自托管网络服务清单 | 低：自托管金融数据服务选型 | 中 |
| 6 | JustVugg/colibri | 51815 | +185 | +1996 | C | 量化研究 | 分层 MoE 推理引擎 | 中：本地低成本 LLM 推理 | 低 |
| 7 | codecrafters-io/build-your-own-x | 563555 | +303 | +1894 | Markdown | 交易机器人 | 从零复刻技术的教程合集 | 低：复刻交易系统组件 | 中 |
| 8 | public-apis/public-apis | 499945 | +253 | +1891 | Python | 加密交易/量化研究/风控 | 免费 API 合集 | 中：金融数据 API 选型 | 中 |
| 9 | CopilotKit/OpenBot | 12786 | +134 | +1939 | TypeScript | 金融科技产品/交易机器人 | 开源可自托管 AI Bot 替代品 | 高：企业级 Agent 编排参考 | 中 |
| 10 | vinta/awesome-python | 335556 | +227 | +1638 | Python | 量化研究 | Python 工具精选清单 | 低：量化 Python 工具选型 | 低 |
| 11 | ifixai-ai/iFixAi | 46368 | +182 | +1617 | Python | AI 交易/金融科技产品/风控 | AI Agent 独立审计工具 | 高：Agent 治理与风控 | 低 |
| 12 | Jakeschincariol/day-trader-skill | 8459 | +205 | +1692 | Python | 回测/风控 | 11 个日内交易 Claude 技能 | 高：交易复盘与入场时机技能化 | 低 |
| 13 | VoltAgent/awesome-design-md | 128035 | +162 | +1488 | 无 | 加密交易/金融科技产品 | 品牌设计系统 DESIGN.md 合集 | 低：金融产品 UI 设计规范 | 中 |
| 14 | avelino/awesome-go | 194547 | +189 | +1332 | Go | 回测/加密交易/风控/交易机器人 | Go 框架与库精选清单 | 低：Go 交易基础设施选型 | 中 |
| 15 | nexu-io/open-design | 108179 | +180 | +1098 | TypeScript | 金融科技产品/交易基础设施 | 协作式 AI 设计 Agent 工作台 | 中：金融看板协作设计 | 低 |
| 16 | TauricResearch/TradingAgents | 123015 | +125 | +1097 | Python | AI 交易/回测/量化研究/风控 | 多 Agent LLM 金融交易框架 | 高：多 Agent 交易决策架构 | 低 |
| 17 | awesome-dsh-plugin/awesome-dsh-plugin | 25038 | +88 | +797 | JavaScript | 交易基础设施 | DeepSeek Harness 插件精选 | 低：DeepSeek 生态插件 | 低 |
| 18 | kaankiziltug/logo-design-skill | 7223 | +104 | +678 | HTML | 金融科技产品 | Logo 设计 Agent 技能 | 低：品牌设计自动化 | 低 |
| 19 | headroomlabs-ai/headroom | 79957 | +88 | +626 | Python | AI 交易/风控 | LLM 上下文压缩工具 | 高：降低金融 Agent token 成本 | 低 |
| 20 | ripienaar/free-for-dev | 143100 | +88 | +557 | HTML | 金融科技产品/量化研究 | 开发者免费资源清单 | 低：免费金融数据服务 | 低 |
| 21 | jaywcjlove/awesome-mac | 118791 | +80 | +550 | Swift | 交易基础设施 | macOS 软件精选 | 低：交易终端工具选型 | 低 |
| 22 | ruvnet/ruflo | 81992 | +85 | +541 | TypeScript | AI 交易/回测 | Agent 编排与多智能体集群 | 高：多 Agent 工作流编排 | 低 |
| 23 | garrytan/gbrain | 33245 | +62 | +666 | TypeScript | 金融科技产品 | OpenClaw/Hermes Agent Brain | 中：Agent 记忆与编排 | 低 |
| 24 | sickn33/agentic-awesome-skills | 49921 | +84 | +413 | Python | 回测 | 2955+ 可复用 AI Agent 技能库 | 中：技能目录与发现机制 | 低 |
| 25 | punkpeye/awesome-remote-mcp-servers | 3457 | +80 | +493 | 无 | AI 交易/加密交易/交易机器人 | 远程 MCP 服务器合集 | 低：远程 MCP 金融数据源 | 中 |
| 26 | hesreallyhim/awesome-claude-code | 58260 | +64 | +523 | Python | AI 交易/量化研究 | Claude Code 资源精选 | 低：Claude Code 生态 | 低 |
| 27 | HKUDS/Vibe-Trading | 38468 | +64 | +445 | Python | AI 交易/回测/金融科技产品/量化研究/风控 | 个人交易 Agent | 高：LLM 交易 Agent 参考 | 低 |
| 28 | shy3130/tick-stock-panel | 8026 | +72 | +452 | Python | AI 交易/回测/量化研究 | A 股自托管量化工作台 | 高：DuckDB+Polars+FastAPI 架构 | 低 |
| 29 | PurpleDoubleD/locally-uncensored | 4373 | +41 | +656 | TypeScript | AI 交易/量化研究 | 本地一体化 AI 桌面应用 | 中：本地 AI 推理与隐私 | 低 |
| 30 | Open-Dev-Society/OpenStock | 21680 | +176 | +267 | TypeScript | 未分类 | 开源市场行情平台 | 中：实时行情与告警产品 | 低 |
| 31 | microsoft/BitNet | 41814 | +223 | +297 | C++ | AI 交易/量化研究 | 1-bit LLM 官方推理框架 | 中：低比特量化推理 | 低 |
| 32 | punkpeye/awesome-mcp-servers | 97834 | +43 | +248 | 无 | 金融科技产品 | MCP 服务器合集 | 低：MCP 金融工具集成 | 低 |
| 33 | TGrpg/awesome-telegram | 1763 | +11 | +569 | JavaScript | 量化研究/交易机器人 | Telegram 频道/群组/机器人导航 | 低：交易信号分发渠道 | 中 |
| 34 | GoogleChrome/modern-web-guidance | 22364 | +1115 | 信息不足 | 无 | 风控 | 编码 Agent 最新 Web 最佳实践 | 低：Web 前端规范 | 低 |
| 35 | FareedKhan-dev/kimi-k3-in-c | 12317 | +89 | 信息不足 | C | AI 交易/量化研究/风控 | 单 CPU 运行 2.78T 参数模型 | 中：极致内存优化推理 | 低 |
| 36 | GoogleChrome/modern-web-guidance-src | 8572 | +398 | 信息不足 | TypeScript | 风控 | Web 最佳实践源码 | 低：前端工程规范 | 低 |
| 37 | AhmadHassan-BTed/Turnitout-Humanizer | 12390 | +31 | +290 | HTML | 风控/交易机器人 | 学术查重规避工具 | 低：学术诚信灰色地带 | 中 |
| 38 | nidhinjs/prompt-master | 16116 | +38 | +303 | 无 | AI 交易/金融科技产品 | 精准 Prompt 生成技能 | 中：降低 Agent 提示成本 | 低 |
| 39 | aardappel/goose | 3681 | +40 | +268 | C++ | 交易基础设施 | Goose 编程语言 | 低：系统级交易基础设施 | 低 |
| 40 | openbq-org/OpenBB | 75513 | +30 | +194 | Python | 加密交易/量化研究 | 面向分析师与 Agent 的开放数据平台 | 高：金融数据平台架构 | 中 |
| 41 | localai-org/depth-anything.cpp | 1287 | +129 | +150 | C++ | 量化研究 | Depth Anything 2/3 的 C++ 移植 | 低：边缘推理 | 低 |
| 42 | rust-unofficial/awesome-rust | 60624 | +27 | +170 | Rust | AI 交易/回测/加密交易/量化研究/风控 | Rust 资源精选 | 低：Rust 量化基础设施 | 中 |
| 43 | code-yeongyu/oh-my-openagent | 70984 | +25 | +156 | TypeScript | 量化研究 | 图工程 Agent 编排 | 低：Agent 编排 TUI | 低 |
| 44 | awesomedata/awesome-public-datasets | 80187 | +10 | +164 | 无 | 加密交易 | 高质量开放数据集清单 | 中：金融数据集选型 | 中 |
| 45 | fffaraz/awesome-cpp | 74486 | +16 | +129 | 无 | 量化研究/交易基础设施 | C/C++ 资源精选 | 低：低延迟交易基础设施 | 低 |
| 46 | virattt/ai-hedge-fund | 64738 | +21 | +108 | Python | 回测/风控 | AI 对冲基金团队 | 高：多 Agent 投资决策参考 | 低 |
| 47 | agustrisna170892-afk/alpaca-0dte-trading-terminal | 153 | +153 | 信息不足 | HTML | 金融科技产品/交易基础设施 | Alpaca 0DTE 期权交易终端 | 低：期权执行与分析 | 低 |
| 48 | ParthNavadiya888/purffle-copybot | 153 | +153 | 信息不足 | Rust | 回测/交易机器人 | Hyperliquid 社区跟单交易 | 低：跟单交易机制 | 中 |
| 49 | Developer-Y/cs-video-courses | 84881 | +9 | +73 | 无 | 量化研究/交易机器人 | 计算机科学视频课程清单 | 低：量化基础课程 | 中 |
| 50 | josephmisiti/awesome-machine-learning | 74848 | +5 | +57 | Python | AI 交易 | 机器学习框架精选 | 低：ML 工具选型 | 低 |
| 51 | vuejs/awesome-vue | 73474 | +2 | -6 | 无 | 量化研究 | Vue.js 资源精选 | 低：前端框架选型 | 低 |

---

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：7 日涨星 +3556，是本次候选集中金融垂直领域涨星最猛的项目之一，说明“LLM + 股票分析 + 自动推送”的产品形态有强需求。
- **技术栈/架构亮点**：Python + LLM，多源行情与新闻融合，决策看板与自动推送分离，强调零成本定时运行，适合个人研究者低成本部署。
- **是否适合借鉴**：适合。其“数据采集 → LLM 分析 → 看板展示 → 自动推送”的流水线可作为 AI 投研助手 MVP 的参考架构。
- **可能风险**：金融合规风险（自动推送可能被解读为投资建议）；数据源稳定性；LLM 输出幻觉导致的错误分析。

### 3.2 tradermonty/claude-trading-skills
- **解决什么问题**：将市场分析、技术图表、经济日历、筛选器、交易策略开发封装为 Claude Code 技能。
- **为什么值得关注**：7 日涨星 +3185，体现“交易分析技能化”趋势，降低非工程背景交易者使用 AI 的门槛。
- **技术栈/架构亮点**：Python + Claude Skills，模块化技能包，覆盖从数据获取到策略开发的完整链路。
- **是否适合借鉴**：适合。可借鉴其技能拆分方式，将投研流程拆成可被 Agent 调用的原子技能。
- **可能风险**：策略过拟合；技能依赖 Claude 生态；回测结果可能被误读为实盘收益。

### 3.3 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，覆盖幻觉检测、提示注入、AI 对齐、ISO 42001、NIST AI RMF 等。
- **为什么值得关注**：7 日涨星 +1617，AI Agent 治理是金融场景落地前的关键缺口，该项目直接切入合规与风控。
- **技术栈/架构亮点**：Python + CLI，支持人工或 Agent 自审计，120 秒内给出结论，覆盖多个治理标准。
- **是否适合借鉴**：非常适合。金融企业部署交易 Agent 前，可参考其审计维度构建内部 Agent 风控关卡。
- **可能风险**：审计标准覆盖度与准确性需验证；不能替代正式合规审计。

### 3.4 TauricResearch/TradingAgents
- **解决什么问题**：多 Agent LLM 金融交易框架，模拟多个分析师/交易员角色协作决策。
- **为什么值得关注**：总 star 123015，是 LLM 多 Agent 交易领域的标杆项目之一，7 日仍涨 +1097。
- **技术栈/架构亮点**：Python + Apache-2.0，多 Agent 角色分工，结合 LLM 与金融数据。
- **是否适合借鉴**：适合。其多 Agent 角色设计（如基本面、技术面、情绪面分析师）可迁移到企业级投研 Agent 框架。
- **可能风险**：策略过拟合；LLM 决策不可解释；回测与实盘差距大。

### 3.5 shy3130/tick-stock-panel
- **解决什么问题**：A 股自托管、零运维的“自建策略 + 监控 + 回测”量化工作台，支持 LLM 策略定制与个股分析。
- **为什么值得关注**：技术栈现代（DuckDB + Polars + FastAPI + React），是轻量级量化工作台的良好参考。
- **技术栈/架构亮点**：DuckDB 做本地分析、Polars 做数据处理、FastAPI 做服务、React 做前端，LLM 驱动策略定制。
- **是否适合借鉴**：非常适合。可作为“本地优先量化研究平台”的原型参考，尤其适合数据敏感场景。
- **可能风险**：A 股数据合规；策略过拟合；个人开源项目维护活跃度。

### 3.6 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多个 Agent 协作完成投资决策。
- **为什么值得关注**：总 star 64738，是 AI 交易 Agent 的经典参考项目。
- **技术栈/架构亮点**：Python + 多 Agent 角色，模拟对冲基金团队协作。
- **是否适合借鉴**：适合。可借鉴其 Agent 角色分工与决策流程，但需注意其研究工具属性。
- **可能风险**：策略过拟合；回测幸存者偏差；不可直接用于实盘。

### 3.7 CopilotKit/OpenBot
- **解决什么问题**：开源、可自托管的 AI Bot 替代品，支持任意 Agent、任意模型、任意工具。
- **为什么值得关注**：7 日涨星 +1939，体现企业对“不锁定封闭 AI Bot”的需求。
- **技术栈/架构亮点**：TypeScript + MIT，支持 AG-UI、Agent 治理、浏览器自动化、生成式 UI、MCP。
- **是否适合借鉴**：适合。其“任意 Agent/模型/工具”的插件化设计可迁移到企业级 Agent 编排平台。
- **可能风险**：项目较新，生态成熟度需观察；与 trading_bot 关键词匹配但实际为通用 Agent 框架。

### 3.8 headroomlabs-ai/headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前进行压缩，降低 token 消耗。
- **为什么值得关注**：总 star 79957，对金融 Agent 高频调用场景的成本控制有直接价值。
- **技术栈/架构亮点**：Python + Apache-2.0，提供库、代理、MCP server 三种形态，宣称 JSON 可减少 60-95% token。
- **是否适合借鉴**：适合。金融数据量大，Agent 上下文窗口紧张，可借鉴其压缩策略降低推理成本。
- **可能风险**：压缩可能损失关键信息；需验证在金融数据上的准确性。

### 3.9 openbq-org/OpenBB
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台。
- **为什么值得关注**：总 star 75513，是金融数据平台的重要开源项目，覆盖股票、期权、加密、固定收益等。
- **技术栈/架构亮点**：Python，统一数据接口，支持 AI Agent 调用。
- **是否适合借鉴**：适合。可作为金融数据层参考，避免重复造轮子。
- **可能风险**：数据源许可与稳定性；与 crypto 相关，需注意数据合规。

### 3.10 JustVugg/colibri
- **解决什么问题**：分层 MoE 推理引擎，热专家在 GPU、温专家在 RAM、冷专家从 NVMe 流式加载，用 C 语言在自有硬件上运行前沿 MoE 模型。
- **为什么值得关注**：7 日涨星 +1996，体现“本地低成本推理”趋势，对量化研究中的数据隐私与推理成本有参考价值。
- **技术栈/架构亮点**：C + Apache-2.0，分层专家管理，CUDA/Vulkan 支持。
- **是否适合借鉴**：适合。可借鉴其分层推理思想，在本地部署金融 LLM 时降低硬件门槛。
- **可能风险**：项目较新，稳定性与模型兼容性需验证。

---

## 4. 趋势归纳

### 技术趋势
- **Agent 技能化/模块化**：大量项目以 “Claude/Codex Skill” 形式发布，将交易分析、回测、风控、UI 设计、安全测试封装为可复用技能包。
- **本地优先与低成本推理**：`colibri`、`kimi-k3-in-c`、`BitNet`、`locally-uncensored` 等项目体现“在自有硬件上运行前沿模型”的趋势，强调隐私与成本控制。
- **上下文压缩与 token 优化**：`headroom` 等项目聚焦降低 LLM 推理成本，对金融 Agent 高频调用场景尤为重要。
- **现代数据栈**：`tick-stock-panel` 使用 DuckDB + Polars + FastAPI + React，体现轻量级本地量化工作台的现代技术选型。

### 产品趋势
- **从框架到技能包**：产品形态从“大而全的交易框架”转向“小而美的技能包”，降低用户上手门槛。
- **自托管与开源替代**：`OpenBot`、`OpenStock`、`OpenBB` 等项目强调开源、自托管、免费，替代封闭商业产品。
- **AI Agent 治理产品化**：`iFixAi` 将 Agent 审计、对齐、合规打包为产品，预示金融 Agent 落地前的治理需求。

### 量化/交易策略趋势
- **LLM 多 Agent 决策**：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 等项目持续演进，多 Agent 角色分工成为主流范式。
- **研究工具属性强化**：多数交易相关项目被标记为 `likely_research_tool`，强调回测与研究，而非直接实盘。
- **A 股与多市场覆盖**：`daily_stock_analysis`、`tick-stock-panel` 等项目显示 A 股量化工具需求旺盛。

### AI Agent 与自动化交易结合趋势
- **技能化交易分析**：`claude-trading-skills`、`day-trader-skill` 将交易分析拆成原子技能，Agent 可按需调用。
- **Agent 审计与风控前置**：`iFixAi` 等治理工具的出现，说明 Agent 自动化交易前需要先解决“如何审计 Agent”的问题。
- **MCP 生态扩展**：`awesome-mcp-servers`、`awesome-remote-mcp-servers` 等项目显示 MCP 正成为 Agent 连接金融数据与工具的标准接口。

### 值得后续做原型验证的方向
- **本地优先量化研究工作台**：参考 `tick-stock-panel`，用 DuckDB + Polars + FastAPI 构建本地回测与监控平台。
- **交易分析技能包**：参考 `claude-trading-skills`，将投研流程拆成可被 Codex/Claude 调用的原子技能。
- **Agent 审计关卡**：参考 `iFixAi`，在交易 Agent 流水线中插入审计与对齐检查。
- **上下文压缩中间层**：参考 `headroom`，在金融数据进入 LLM 前做无损/有损压缩，降低 token 成本。

---

## 5. 今日灵感清单

1. **MVP：本地优先 A 股量化研究工作台**  
   参考 `tick-stock-panel`，用 DuckDB 存本地行情、Polars 做因子计算、FastAPI 暴露回测接口、React 做看板，LLM 生成策略代码。先做“数据导入 → 因子计算 → 回测 → 看板”闭环。

2. **MVP：交易分析技能包**  
   参考 `claude-trading-skills` 和 `day-trader-skill`，将“技术指标计算”“新闻情绪分析”“经济日历”“回测报告生成”封装为 Codex/Claude 可调用的技能，验证 Agent 辅助投研的可行性。

3. **调研：AI Agent 审计与对齐**  
   调研 `iFixAi` 的审计维度（幻觉检测、提示注入、ISO 42001、NIST AI RMF），设计一套适用于金融交易 Agent 的轻量级审计 checklist。

4. **调研：LLM 上下文压缩**  
   调研 `headroom` 的压缩策略，验证在金融新闻、行情 JSON、回测日志等场景下的 token 节省率与信息保真度。

5. **Demo：多 Agent 投资决策模拟**  
   参考 `TradingAgents` 和 `ai-hedge-fund`，用 Codex 复现一个简化版多 Agent 投研团队（基本面、技术面、情绪面、风控），仅用于研究，不接实盘。

6. **调研：本地低成本 LLM 推理**  
   调研 `colibri`、`kimi-k3-in-c`、`BitNet` 的量化与分层推理方案，评估在本地部署金融 LLM 的可行性与成本。

7. **MVP：金融数据 API 聚合层**  
   参考 `OpenBB` 和 `public-apis`，构建一个统一接口的金融数据聚合层，屏蔽多源数据差异，供 Agent 调用。

8. **调研：MCP 金融工具生态**  
   调研 `awesome-mcp-servers` 和 `awesome-remote-mcp-servers` 中与金融数据、交易、风控相关的 MCP server，评估集成可行性。

9. **Demo：Agent 生成金融看板 UI**  
   参考 `ui-ux-pro-max-skill` 和 `open-design`，让 Codex 根据金融数据自动生成决策看板 UI，验证“数据 → 看板”的自动化链路。

10. **Watchlist：OpenBot 与 ruflo**  
    将 `CopilotKit/OpenBot` 和 `ruvnet/ruflo` 加入 watchlist，观察企业级 Agent 编排与多智能体集群的演进，寻找可复用的编排模式。

---

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 金融垂直领域涨星最猛，产品形态清晰，适合跟踪 LLM 投研助手演进 |
| tradermonty/claude-trading-skills | 交易分析技能化代表，观察技能包生态发展 |
| ifixai-ai/iFixAi | AI Agent 治理与审计的标杆，金融 Agent 落地前必看 |
| TauricResearch/TradingAgents | 多 Agent 交易框架标杆，观察 LLM 交易决策演进 |
| shy3130/tick-stock-panel | 现代技术栈的本地量化工作台，适合复刻 |
| CopilotKit/OpenBot | 开源可自托管 Agent 框架，观察企业级 Agent 编排 |
| headroomlabs-ai/headroom | LLM 上下文压缩，金融 Agent 成本控制关键 |
| openbq-org/OpenBB | 金融数据平台，观察 Agent 数据层标准化 |
| virattt/ai-hedge-fund | AI 对冲基金团队模拟，经典参考项目 |
| JustVugg/colibri | 本地低成本 MoE 推理，观察前沿模型本地化部署 |

---

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

---

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-11-16.json`，与 `current_snapshot` 日期 `2026-11-17` 相差 1 天，1 日涨星数据可用。
- **7 日基线**：存在，`baseline_7d` 为 `2026-11-10.json`，与 `current_snapshot` 日期 `2026-11-17` 相差 7 天，7 日涨星数据可用。
- **采集失败/缺失**：部分项目 `star_delta_7d` 为 `null`（如 `modern-web-guidance`、`kimi-k3-in-c`、`alpaca-0dte-trading-terminal`、`purffle-copybot`），可能因项目创建时间晚于 7 日基线或基线数据缺失，表中已标注“信息不足”。
- **样本偏差**：候选集由多个关键词查询合并而成，包含大量 awesome-list 和通用工具项目，这些项目因 README 或描述中命中金融/交易关键词而被纳入，并非全部为金融垂直项目。分析时需人工甄别。`star_delta_30d` 字段全部为 `null`，30 日涨星信息缺失。
- **风险标记偏差**：部分项目因匹配到 “trading bot” 等关键词被标记为中风险，但实际内容可能为教程、清单或通用工具，风险等级需结合项目实际内容判断。
