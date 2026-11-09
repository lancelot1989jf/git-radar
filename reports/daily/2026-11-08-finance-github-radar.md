# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-08

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 技能化交易**：`day-trader-skill`、`trader-skill` 等将交易决策封装为 Claude Skills，强调“人工确认后才下单”，代表 AI 交易从“全自动黑盒”向“可审计、人在环中”的转变。
  2. **LLM 多智能体金融框架**：`TradingAgents`、`Vibe-Trading`、`QuantDinger` 等持续高增长，多 Agent 分工（研究、风控、交易）成为主流架构范式。
  3. **本地优先的 AI 基础设施**：`colibri`（MoE 分层推理引擎）、`headroom`（LLM 上下文压缩）、`Soup`（低显存微调）等反映“在自有硬件上跑 AI”的工程趋势，对金融数据隐私和成本控制有直接借鉴意义。

- **是否出现新趋势**：出现。AI Agent 的“技能化封装”（Skills）与“审计/治理”正在融合，`iFixAi` 将 Agent 审计压缩到 120 秒内，`OpenBot` 强调“每个动作先决策、后记录”，这与金融交易对可追溯性的要求高度契合。

- **是否出现值得复刻/参考的工程架构**：是。`QuantDinger` 提出“研究—回测—优化—纸面/实盘执行—风控—监控—MCP—多租户 SaaS”的一体化可审计栈；`colibri` 的 GPU/RAM/NVMe 分层推理对量化研究中的本地大模型部署有参考价值。

- **是否有明显骗局、过度营销或高风险项目**：`Turnitout-Humanizer` 声称可绕过 Turnitin、GPTZero 等检测，属于学术不端工具，与金融/量化无关，应直接排除。其余项目未见明显骗局，但多个 `trading_bot` 标记项目需按高风险对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nextlevelbuilder/ui-ux-pro-max-skill | 147041 | +423 | +2160 | Python | AI 设计技能 | 跨平台 UI/UX 设计智能技能 | 中 | 低 |
| 2 | awesome-selfhosted/awesome-selfhosted | 335251 | +343 | +1735 | 无 | 自托管清单 | 可自托管网络服务清单 | 低 | 中 |
| 3 | JustVugg/colibri | 49170 | +368 | +1759 | C | 推理引擎 | MoE 模型分层推理引擎 | 高 | 低 |
| 4 | codecrafters-io/build-your-own-x | 561162 | +314 | +1637 | Markdown | 教程清单 | 从零复刻技术的教程合集 | 中 | 中 |
| 5 | awesome-dsh-plugin/awesome-dsh-plugin | 23895 | +273 | +1598 | JavaScript | 插件清单 | DeepSeek Harness 插件精选 | 中 | 低 |
| 6 | public-apis/public-apis | 497373 | +280 | +1449 | Python | API 清单 | 免费 API 合集 | 中 | 中 |
| 7 | vinta/awesome-python | 333502 | +226 | +1190 | Python | Python 清单 | Python 工具精选 | 低 | 低 |
| 8 | Jakeschincariol/day-trader-skill | 6236 | +204 | +1212 | Python | 交易技能 | 11 个日内交易 Claude Skills | 高 | 低 |
| 9 | TauricResearch/TradingAgents | 121428 | +200 | +977 | Python | 多智能体交易 | LLM 多智能体金融交易框架 | 高 | 低 |
| 10 | ifixai-ai/iFixAi | 44236 | +217 | +969 | Python | Agent 审计 | AI Agent 独立审计工具 | 高 | 低 |
| 11 | avelino/awesome-go | 192884 | +208 | +916 | Go | Go 清单 | Go 框架与库精选 | 低 | 中 |
| 12 | nexu-io/open-design | 106708 | +187 | +887 | TypeScript | 协作设计 | 协作式 AI 设计工作台 | 中 | 低 |
| 13 | ZhuLinsen/daily_stock_analysis | 68351 | +482 | +833 | Python | 股票分析 | LLM 多市场股票分析系统 | 高 | 低 |
| 14 | VoltAgent/awesome-design-md | 126209 | +149 | +697 | 无 | 设计系统 | DESIGN.md 设计系统合集 | 低 | 中 |
| 15 | ripienaar/free-for-dev | 142306 | +100 | +521 | HTML | 免费资源 | 开发者免费资源清单 | 低 | 低 |
| 16 | ruvnet/ruflo | 81305 | +106 | +484 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | 高 | 低 |
| 17 | shiyu-coder/Kronos | 47366 | +91 | +740 | Python | 金融基础模型 | 金融市场语言基础模型 | 高 | 低 |
| 18 | jaywcjlove/awesome-mac | 118079 | +134 | +378 | Swift | macOS 清单 | macOS 软件精选 | 低 | 低 |
| 19 | CopilotKit/OpenBot | 10509 | +91 | +445 | TypeScript | Agent 治理 | 开源 AI 数字员工 | 高 | 中 |
| 20 | headroomlabs-ai/headroom | 79183 | +84 | +403 | Python | 上下文压缩 | LLM 输出/日志压缩工具 | 高 | 低 |
| 21 | shy3130/tick-stock-panel | 7380 | +98 | +380 | Python | 量化工作台 | A 股自建策略+监控+回测工作台 | 高 | 低 |
| 22 | kaankiziltug/logo-design-skill | 6369 | +85 | +440 | HTML | 设计技能 | Logo 设计 AI 技能 | 低 | 低 |
| 23 | garrytan/gbrain | 31798 | +172 | +290 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | 中 | 低 |
| 24 | hesreallyhim/awesome-claude-code | 57573 | +71 | +363 | Python | Claude 清单 | Claude Code 资源精选 | 中 | 低 |
| 25 | HKUDS/Vibe-Trading | 37924 | +66 | +335 | Python | 交易 Agent | 个人交易 Agent | 高 | 低 |
| 26 | Developer-Y/cs-video-courses | 84736 | +73 | +187 | 无 | 课程清单 | CS 视频课程清单 | 低 | 中 |
| 27 | aardappel/goose | 3329 | +62 | +367 | C++ | 编程语言 | Goose 编程语言 | 低 | 低 |
| 28 | punkpeye/awesome-mcp-servers | 97503 | +53 | +233 | 无 | MCP 清单 | MCP 服务器合集 | 中 | 低 |
| 29 | sickn33/agentic-awesome-skills | 49386 | +49 | +268 | Python | 技能库 | 2926+ AI Agent 技能库 | 高 | 低 |
| 30 | PurpleDoubleD/locally-uncensored | 3613 | +42 | +391 | TypeScript | 本地 AI | 桌面本地 AI 工作室 | 中 | 低 |
| 31 | nidhinjs/prompt-master | 15736 | +58 | +261 | 无 | 提示词技能 | 精准提示词生成技能 | 低 | 低 |
| 32 | punkpeye/awesome-remote-mcp-servers | 2831 | +46 | +283 | 无 | MCP 清单 | 远程 MCP 服务器合集 | 中 | 中 |
| 33 | Jakeschincariol/trader-skill | 1577 | +49 | +374 | Python | 交易技能 | 11 个投资者复刻 Claude Skills | 高 | 低 |
| 34 | openbq-org/OpenBB | 75254 | +34 | +187 | Python | 数据平台 | 分析师/量化/AI Agent 开放数据平台 | 高 | 中 |
| 35 | MakazhanAlpamys/Soup | 10334 | +39 | +223 | Python | 模型微调 | 单 YAML 低显存微调 LLM | 中 | 低 |
| 36 | AhmadHassan-BTed/Turnitout-Humanizer | 11972 | +70 | 无 | HTML | 学术不端工具 | 抄袭检测绕过工具 | 无 | 中 |
| 37 | virattt/ai-hedge-fund | 64582 | +29 | +110 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 38 | code-yeongyu/oh-my-openagent | 70794 | +23 | +110 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中 | 低 |
| 39 | fffaraz/awesome-cpp | 74324 | +24 | +103 | 无 | C++ 清单 | C/C++ 框架与库精选 | 低 | 低 |
| 40 | OpenByteInc/QuantDinger | 13644 | +28 | +142 | Python | 交易 OS | 自托管 Agentic 交易 OS | 高 | 中 |
| 41 | rust-unofficial/awesome-rust | 60413 | +19 | +95 | Rust | Rust 清单 | Rust 代码与资源精选 | 低 | 中 |
| 42 | Orkas-AI/Orkas | 9120 | +23 | +127 | JavaScript | Agent 团队 | 本地优先桌面 AI 团队 | 中 | 低 |
| 43 | awesomedata/awesome-public-datasets | 79989 | +10 | +46 | 无 | 数据集清单 | 高质量开放数据集清单 | 中 | 中 |
| 44 | josephmisiti/awesome-machine-learning | 74785 | +2 | +42 | Python | ML 清单 | 机器学习框架精选 | 低 | 低 |
| 45 | vuejs/awesome-vue | 73484 | +2 | -6 | 无 | Vue 清单 | Vue.js 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，模拟研究、分析、风控、交易等角色的分工。
- **为什么值得关注**：总 star 121428，7 日涨星 +977，是当前 LLM 金融 Agent 方向最具代表性的框架之一，Apache-2.0 许可，近 30 天有 push。
- **技术栈/架构亮点**：Python，多 Agent 架构，topics 包含 `agent`、`finance`、`llm`、`multiagent`、`trading`。核心价值在于将交易流程拆解为可协作、可替换的 Agent 角色。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色分工模式，用于企业级投研 Agent 框架设计，尤其是“研究—风控—决策”分离的治理结构。
- **可能风险**：策略过拟合、回测与实盘差异、LLM 输出不确定性；作为研究工具使用，不应直接实盘。

### 3.2 Jakeschincariol/day-trader-skill
- **解决什么问题**：将日内交易流程（图表扫描、新闻跟踪、进出场时机、结果复盘）封装为 11 个 Claude Skills。
- **为什么值得关注**：24 小时涨星 +204，7 日 +1212，虽然总 star 仅 6236，但增速极快，代表“技能化交易”这一新兴产品形态。
- **技术栈/架构亮点**：Python + Claude Skills，强调“在冒险投入一美元之前先演练每个结果”，即回测/复盘优先。
- **是否适合借鉴**：非常适合。可借鉴其“技能封装 + 人工确认”模式，构建可审计的 AI 辅助交易工作流，避免全自动黑盒。
- **可能风险**：日内交易策略本身高风险；技能描述中的收益暗示不可信；需注意 API key 安全。

### 3.3 OpenByteInc/QuantDinger
- **解决什么问题**：提供一站式自托管 Agentic 交易操作系统，覆盖 AI 研究、Python 策略、因子发现、回测、优化、纸面/实盘多资产执行、风控、监控、MCP 和多租户 SaaS。
- **为什么值得关注**：架构完整性在候选项目中最高，Apache-2.0，近 30 天有 push，topics 覆盖 `agentic-ai`、`backtesting`、`risk-management`、`mcp` 等。
- **技术栈/架构亮点**：Python，强调“可审计栈”（auditable stack），将研究到实盘的全链路纳入统一框架，并支持 MCP 集成。
- **是否适合借鉴**：非常适合。其“全链路可审计”理念可直接用于企业级量化平台架构设计，尤其是风控与监控模块的边界划分。
- **可能风险**：涉及 crypto 和实盘执行，风险等级中；自托管部署复杂；需警惕回测造假和策略过拟合。

### 3.4 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析，整合多源行情、实时新闻、决策看板和自动推送，支持零成本定时运行。
- **为什么值得关注**：24 小时涨星 +482，为全表最高单日涨幅之一；总 star 68351；聚焦 A 股，中文生态，MIT 许可。
- **技术栈/架构亮点**：Python，topics 包含 `a-stock`、`ai-agent`、`llm`、`quant`、`quantitative-trading`。核心是将 LLM 分析能力与多源数据管道结合。
- **是否适合借鉴**：适合。可借鉴其“多源数据 + LLM 决策看板 + 自动推送”的轻量级投研产品形态，适合做 MVP 验证。
- **可能风险**：A 股数据合规、新闻源稳定性、LLM 分析结论不可作为投资依据。

### 3.5 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，可在 120 秒内给出结论。
- **为什么值得关注**：24 小时涨星 +217，7 日 +969，总 star 44236；topics 覆盖 `ai-governance`、`ai-safety`、`prompt-injection`、`iso-42001`、`nist-ai-rmf`、`owasp-llm` 等，与金融 Agent 合规需求高度相关。
- **技术栈/架构亮点**：Python，Apache-2.0，支持人工或 Agent 自审计，覆盖幻觉检测、提示注入、风险评估等。
- **是否适合借鉴**：非常适合。金融交易 Agent 的合规审计是刚需，可将其审计理念集成到交易 Agent 的发布前检查流程。
- **可能风险**：审计工具本身可能存在误报/漏报；不能替代正式合规审查。

### 3.6 JustVugg/colibri
- **解决什么问题**：为前沿 MoE 模型提供分层推理引擎——热专家在 GPU（CUDA/Vulkan）、温专家在 RAM、冷专家从 NVMe 流式加载，用现有硬件运行大模型。
- **为什么值得关注**：24 小时涨星 +368，7 日 +1759，总 star 49170；C 语言实现，Apache-2.0，近 30 天有 push。
- **技术栈/架构亮点**：C 语言，GPU/RAM/NVMe 三级分层推理，对硬件资源受限场景极具工程价值。
- **是否适合借鉴**：适合。量化研究常需在本地跑大模型做文本分析或因子挖掘，分层推理可显著降低硬件门槛和成本。
- **可能风险**：C 语言项目维护难度高；与金融业务无直接耦合，需自行集成。

### 3.7 shiyu-coder/Kronos
- **解决什么问题**：构建金融市场语言的基础模型（Foundation Model for the Language of Financial Markets）。
- **为什么值得关注**：总 star 47366，7 日涨星 +740，Python，MIT 许可。金融基础模型是当前量化研究的前沿方向。
- **技术栈/架构亮点**：Python，聚焦金融语言建模，topics 为空，说明项目定位专注。
- **是否适合借鉴**：适合作为研究方向参考。可调研其模型架构和训练数据构建方式，用于金融 NLP 因子挖掘。
- **可能风险**：模型效果未经独立验证；金融基础模型可能存在数据泄露和过拟合问题；最近 push 在 2026-04，维护活跃度需关注。

### 3.8 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 接收前压缩工具输出、日志、文件和 RAG 块，编码 Agent 可减少 20% token，JSON 可减少 60-95%，答案不变。
- **为什么值得关注**：总 star 79183，7 日涨星 +403，Python，Apache-2.0，近 30 天有 push。
- **技术栈/架构亮点**：提供库、代理和 MCP 服务器三种形态，topics 覆盖 `context-engineering`、`token-optimization`、`rag`、`mcp`。
- **是否适合借鉴**：非常适合。金融数据（行情、公告、研报）体量大，上下文压缩可显著降低 LLM 投研成本，提升 Agent 吞吐。
- **可能风险**：压缩可能丢失关键信息，金融场景需验证压缩后决策质量。

### 3.9 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作进行投资决策。
- **为什么值得关注**：总 star 64582，是 AI 交易领域的经典项目，MIT 许可，近 30 天有 push。
- **技术栈/架构亮点**：Python，多 Agent 模拟对冲基金团队结构。
- **是否适合借鉴**：适合作为教学和研究参考，理解多 Agent 投研协作的基本范式。
- **可能风险**：模拟环境与实盘差异大；策略过拟合风险高；不应直接用于实盘。

### 3.10 CopilotKit/OpenBot
- **解决什么问题**：开源 AI 数字员工，每个 Agent 拥有自己的浏览器、文件和工具，每个动作先决策、后记录，支持任意 AG-UI Agent。
- **为什么值得关注**：总 star 10509，7 日涨星 +445，TypeScript，MIT，近 30 天有 push。其“先决策、后记录”的治理理念对金融 Agent 有直接借鉴意义。
- **技术栈/架构亮点**：TypeScript，topics 包含 `agent-governance`、`browser-automation`、`generative-ui`、`mcp`。
- **是否适合借鉴**：适合。可借鉴其动作审计和记录机制，用于交易 Agent 的操作留痕。
- **可能风险**：浏览器自动化在金融场景可能触发风控；需注意权限隔离。

## 4. 趋势归纳

### 技术趋势
- **AI Agent 技能化**：交易逻辑被封装为可复用 Skills（`day-trader-skill`、`trader-skill`、`agentic-awesome-skills`），降低使用门槛，提升可组合性。
- **本地优先 AI 基础设施**：`colibri` 分层推理、`Soup` 低显存微调、`locally-uncensored` 本地 AI 工作室，反映金融场景对数据隐私和成本控制的诉求。
- **上下文工程**：`headroom` 等工具将 token 优化作为独立工程问题，对高频 LLM 调用的金融 Agent 至关重要。
- **MCP 生态扩张**：`awesome-mcp-servers`、`awesome-remote-mcp-servers` 持续增长，MCP 正成为 Agent 工具接入的事实标准。

### 产品趋势
- **从全自动到人在环中**：`day-trader-skill`、`trader-skill` 强调“未经确认不下单”，`OpenBot` 强调动作审计，产品设计从黑盒自动化转向可审计辅助。
- **一体化交易 OS**：`QuantDinger` 试图将研究、回测、执行、风控、监控整合为单一可审计栈，替代碎片化工具链。
- **Agent 治理产品化**：`iFixAi` 将 Agent 审计产品化，金融合规可能成为 Agent 治理的率先落地场景。

### 量化/交易策略趋势
- **LLM 多智能体框架成为主流**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 均采用多 Agent 分工，传统单策略回测向多角色协作演进。
- **金融基础模型探索**：`Kronos` 代表“金融语言基础模型”方向，可能改变因子挖掘和文本分析范式。
- **A 股 LLM 分析工具崛起**：`daily_stock_analysis`、`tick-stock-panel` 反映中文市场对 LLM 投研工具的强需求。

### AI Agent 与自动化交易结合趋势
- **审计与治理前置**：`iFixAi`、`OpenBot` 表明 Agent 审计不再是事后补救，而是产品设计的一部分。
- **技能化降低集成成本**：交易策略以 Skills 形式分发，便于 Claude Code、Codex、Cursor 等编码 Agent 直接调用。
- **MCP 作为交易工具接入层**：多个项目支持 MCP，未来交易数据、下单、风控可能通过 MCP 标准化接入。

### 值得后续做原型验证的方向
1. **可审计的 AI 交易辅助工作流**：借鉴 `day-trader-skill` + `iFixAi`，构建“技能封装 + 人工确认 + 自动审计”的 MVP。
2. **本地化金融 LLM 推理**：基于 `colibri` 分层推理 + `Soup` 微调，在消费级硬件上跑金融领域模型。
3. **LLM 投研上下文压缩管道**：用 `headroom` 压缩行情、公告、研报数据，验证压缩后决策质量。
4. **多 Agent 投研协作框架**：参考 `TradingAgents` 角色分工，构建企业级投研 Agent 原型。

## 5. 今日灵感清单

1. **MVP：可审计的 AI 交易信号助手**：封装 3-5 个 Claude Skills（行情扫描、新闻跟踪、信号生成、风险检查），每个信号必须经人工确认才进入模拟盘，集成 `iFixAi` 做自动审计。参考 `day-trader-skill` + `iFixAi`。

2. **MVP：本地金融 LLM 推理服务**：用 `colibri` 的分层推理思路，在单张消费级 GPU 上部署一个金融领域微调模型（可参考 `Soup` 微调），提供本地 API 供投研 Agent 调用。

3. **调研：金融 Agent 的上下文压缩效果**：用 `headroom` 对行情 JSON、财报文本、新闻流做压缩，对比压缩前后 LLM 投研结论的一致性和 token 成本。

4. **调研：多 Agent 交易框架的角色边界设计**：对比 `TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 的 Agent 角色划分，总结“研究—风控—决策—执行”的最佳边界。

5. **Codex/Agent 自动复现 demo：A 股 LLM 分析看板**：参考 `daily_stock_analysis`，让 Codex 自动搭建一个“多源行情 + LLM 分析 + 决策看板 + 定时推送”的轻量级原型。

6. **调研：MCP 在交易工具链中的标准化潜力**：梳理 `awesome-mcp-servers` 中与金融数据、交易、风控相关的 MCP 服务器，评估用 MCP 统一交易工具接入的可行性。

7. **MVP：Agent 动作审计日志系统**：借鉴 `OpenBot` 的“先决策、后记录”机制，为交易 Agent 构建不可篡改的操作留痕系统。

8. **调研：金融基础模型 Kronos 的架构与数据**：深入调研 `Kronos` 的模型架构、训练数据和评估方法，评估其在金融 NLP 因子挖掘中的应用潜力。

9. **Watchlist：QuantDinger 架构拆解**：将 `QuantDinger` 加入 watchlist，重点跟踪其“研究—回测—执行—风控—监控”全链路可审计架构的演进。

10. **原型：Agent 技能目录与选择器**：参考 `agentic-awesome-skills` 的本地目录发现和 Agent 自主选择机制，为金融场景构建一个技能目录，让 Agent 根据任务自动选择合适技能。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | LLM 多智能体交易框架标杆，持续高增长，适合跟踪多 Agent 架构演进 |
| OpenByteInc/QuantDinger | 一体化可审计交易 OS，架构完整性高，适合跟踪全链路交易平台设计 |
| Jakeschincariol/day-trader-skill | 技能化交易新形态，增速极快，适合观察“人在环中”产品趋势 |
| ifixai-ai/iFixAi | Agent 审计产品化代表，与金融合规需求高度契合 |
| JustVugg/colibri | 分层推理引擎，对本地金融 LLM 部署有直接工程价值 |
| shiyu-coder/Kronos | 金融基础模型方向，适合跟踪金融 NLP 前沿 |
| headroomlabs-ai/headroom | 上下文压缩工具，对 LLM 投研成本控制有实用价值 |
| ZhuLinsen/daily_stock_analysis | A 股 LLM 分析工具代表，中文生态，增速快 |
| CopilotKit/OpenBot | Agent 治理与动作审计机制，适合跟踪 Agent 合规设计 |
| HKUDS/Vibe-Trading | 学术背景的交易 Agent 项目，适合跟踪研究型实现 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-11-07）和 `baseline_7d`（2026-11-03），涨星数据完整。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法进行 30 日趋势分析。
- **采集失败**：`Turnitout-Humanizer` 的 `star_delta_7d` 为 `null`，可能因基线数据缺失或项目创建时间过短。
- **样本偏差**：候选项目通过关键词匹配（如 `fintech`、`quant`、`trading bot`、`backtesting`、`order book` 等）筛选，导致大量 `awesome-*` 清单类项目被纳入，这些项目与金融/量化的直接相关性较弱，可能稀释了真正交易/量化项目的信号。报告已尽量区分直接相关项目与清单类项目。
- **分类噪声**：部分项目的 `category_guess` 与 `matched_queries` 存在明显不匹配（如 `awesome-selfhosted` 被标记为 `trading_bot`），说明关键词匹配存在误报，分析时需结合项目实际内容判断。
