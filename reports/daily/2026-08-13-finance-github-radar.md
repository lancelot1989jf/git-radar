# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-13

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的多 Agent 金融研究与交易框架**：以 `TradingAgents`、`Vibe-Trading`、`ai-berkshire` 为代表，多 Agent 协作、对抗式分析、价值投资方法论数字化成为明显热点。
  2. **AI Agent 治理与审计**：`iFixAi` 以 7 日 +2205 星的增速进入前列，聚焦 Agent 行为审计、AI 对齐、合规评估，反映 AI Agent 进入生产环境后的风控需求。
  3. **本地优先的 AI 基础设施**：`colibri`（纯 C 的 MoE 推理引擎）、`unsloth`（本地 LLM 训练/推理 UI）、`atomic-agent`（本地优先 Agent）等持续走强，显示“本地运行、零依赖、低成本”成为工程趋势。

- **是否出现新趋势**：出现。AI Agent 从“能对话、能写代码”向“可审计、可治理、可合规”演进，`iFixAi` 的快速涨星是明确信号；同时，金融数据工程从“云端 API”向“本地缓存 + 增量同步 + 自托管”迁移，如 `free-stockdb`、`a-stock-data`、`tickflow-stock-panel`。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，以及 `TradingAgents` 的多 Agent 分工（研究、分析、交易、风控）值得拆解复刻。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但存在大量“awesome-list”类项目因关键词误匹配进入榜单（如 `build-your-own-x`、`awesome-selfhosted`、`public-apis`），其与金融/量化交易的实际关联度低，需注意甄别。`TG-Polymarket-bot` 涉及预测市场跟单交易，风险较高。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | build-your-own-x | 539492 | +319 | +2579 | Markdown | 教程/清单 | 从零复刻技术的教程合集 | 低（误匹配） | 中 |
| 2 | daily_stock_analysis | 62761 | +167 | +2484 | Python | AI 交易/数据工程 | LLM 驱动的多市场股票分析系统 | 高 | 低 |
| 3 | ui-ux-pro-max-skill | 116486 | +335 | +2265 | Python | 设计工具 | AI UI/UX 设计技能包 | 中 | 低 |
| 4 | iFixAi | 8532 | +164 | +2205 | Python | AI 治理/风控 | AI Agent 独立审计工具 | 高 | 低 |
| 5 | TradingAgents | 98033 | +144 | +2089 | Python | AI 交易/多 Agent | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 6 | colibri | 24542 | +196 | +1503 | C | 推理引擎 | 纯 C 零依赖 MoE 推理引擎 | 中 | 低 |
| 7 | awesome-selfhosted | 312491 | +214 | +1413 | 无 | 清单 | 自托管服务清单 | 低（误匹配） | 中 |
| 8 | open-design | 85620 | +247 | +1386 | TypeScript | 设计工具 | 开源 Claude Design 替代品 | 中 | 低 |
| 9 | unsloth | 71114 | +437 | +1457 | Python | LLM 工具 | 本地 LLM 训练/推理 UI | 中 | 低 |
| 10 | public-apis | 456002 | +258 | +1223 | Python | API 清单 | 免费 API 合集 | 低（误匹配） | 中 |
| 11 | awesome-python | 313830 | +189 | +1240 | Python | 清单 | Python 资源清单 | 低（误匹配） | 低 |
| 12 | awesome-design-md | 108305 | +179 | +1244 | 无 | 设计系统 | DESIGN.md 设计系统合集 | 中 | 中 |
| 13 | headroom | 66250 | +145 | +991 | Python | 上下文压缩 | LLM 输出/日志压缩工具 | 中 | 低 |
| 14 | Kronos | 37111 | +142 | +1002 | Python | 量化研究 | 金融市场基础模型 | 高 | 低 |
| 15 | awesome-go | 181005 | +91 | +671 | Go | 清单 | Go 资源清单 | 低（误匹配） | 中 |
| 16 | Vibe-Trading | 30799 | +84 | +718 | Python | AI 交易/多 Agent | 个人交易 Agent | 高 | 中 |
| 17 | free-for-dev | 131716 | +119 | +510 | HTML | 清单 | 开发者免费资源清单 | 低（误匹配） | 低 |
| 18 | gbrain | 28397 | +84 | +520 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 19 | atomic-agent | 2065 | +293 | +564 | TypeScript | 本地 Agent | 本地优先 AI Agent | 中 | 中 |
| 20 | ruflo | 67806 | +59 | +593 | TypeScript | Agent 框架 | Agent 元编排框架 | 中 | 低 |
| 21 | 500-AI-Agents-Projects | 36385 | +119 | +446 | Python | Agent 案例 | 500 个 AI Agent 项目合集 | 中 | 中 |
| 22 | awesome-mcp-servers | 92265 | +91 | +360 | 无 | MCP 清单 | MCP 服务器合集 | 中 | 低 |
| 23 | ds4 | 21330 | +59 | +510 | C | 推理引擎 | DeepSeek 4 本地推理引擎 | 中 | 低 |
| 24 | oh-my-openagent | 67842 | +62 | +456 | TypeScript | Agent 框架 | 复杂代码库 Agent 编排 | 中 | 低 |
| 25 | langfuse | 33071 | +76 | +420 | TypeScript | LLM 可观测性 | LLM 评估/监控平台 | 高 | 低 |
| 26 | awesome-claude-code | 52267 | +47 | +459 | Python | 清单 | Claude Code 资源合集 | 低（误匹配） | 低 |
| 27 | ai-berkshire | 15513 | +37 | +382 | Python | 价值投资/多 Agent | 价值投资研究框架 | 高 | 低 |
| 28 | QuantDinger | 10641 | +55 | +310 | Python | AI 量化平台 | 多市场 AI 量化交易平台 | 中 | 中 |
| 29 | OpenBB | 71847 | +38 | +335 | Python | 金融数据平台 | 开放金融数据平台 | 高 | 中 |
| 30 | a-stock-data | 8710 | +44 | +285 | 无 | 金融数据 | A 股全栈数据工具包 | 高 | 低 |
| 31 | MicroWorld | 1070 | +45 | +403 | Python | 市场模拟 | 美股多 Agent 世界模型 | 高 | 低 |
| 32 | SenseNova-U1 | 4763 | +48 | +252 | Python | 多模态模型 | 原生统一范式模型 | 低 | 低 |
| 33 | needle | 5021 | +703 | 信息不足 | Python | 端侧模型 | 14MB 端侧基础模型 | 中 | 中 |
| 34 | freqtrade | 53264 | +28 | +243 | Python | 加密交易 | 开源加密交易机器人 | 中 | 中 |
| 35 | ai_quant_trade | 6220 | +75 | +105 | Jupyter Notebook | 量化学习 | 股票 AI 操盘手学习平台 | 中 | 中 |
| 36 | tickflow-stock-panel | 2833 | +34 | +203 | Python | 量化工作台 | A 股选股/监控/回测工作台 | 高 | 低 |
| 37 | TG-Polymarket-bot | 1047 | +2 | +393 | JavaScript | 预测市场 | Polymarket 鲸鱼跟单机器人 | 低 | 中 |
| 38 | Claude-BugHunter | 3544 | +30 | +221 | Python | 安全审计 | Claude Code 漏洞挖掘技能包 | 中 | 低 |
| 39 | planning-with-files | 26159 | +28 | +137 | Shell | Agent 规划 | 文件持久化 Agent 规划 | 中 | 低 |
| 40 | free-stockdb | 2028 | +19 | +239 | HTML | 量化数据 | A 股本地量化数据引擎 | 高 | 低 |
| 41 | NVIDIA/skills | 2921 | +44 | +106 | Python | Agent 技能 | NVIDIA 产品 Agent 技能包 | 中 | 中 |
| 42 | awesome-machine-learning | 74024 | +13 | +105 | Python | 清单 | ML 资源清单 | 低（误匹配） | 低 |
| 43 | ai-hedge-fund | 62838 | +9 | +140 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 44 | turbovec | 14759 | +19 | +104 | Rust | 向量索引 | Rust 向量索引库 | 中 | 低 |
| 45 | awesome-cpp | 72759 | +9 | +122 | 无 | 清单 | C++ 资源清单 | 低（误匹配） | 低 |
| 46 | awesome-rust | 58825 | +10 | +110 | Rust | 清单 | Rust 资源清单 | 低（误匹配） | 低 |
| 47 | cs-video-courses | 83043 | +11 | +97 | 无 | 课程清单 | CS 视频课程清单 | 低（误匹配） | 中 |
| 48 | system-design-101 | 87029 | +57 | +300 | 无 | 系统设计 | 系统设计图解 | 中 | 低 |
| 49 | awesome-vue | 73552 | -1 | -1 | 无 | 清单 | Vue 资源清单 | 低（误匹配） | 低 |

## 3. 重点项目深度分析

### 3.1 daily_stock_analysis（ZhuLinsen/daily_stock_analysis）

- **解决什么问题**：面向多市场股票分析的 LLM 驱动系统，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：7 日涨星 +2484，总 star 62761，是本次候选集中金融垂直领域增速最快的项目之一。其“零成本定时运行”的定位切中了个人开发者和研究者的痛点。
- **技术栈/架构亮点**：Python + LLM + 多源数据接入 + 自动推送。架构上采用“数据采集 → LLM 分析 → 看板展示 → 自动推送”的流水线模式，适合作为 AI 投研工作流的参考实现。
- **是否适合借鉴**：非常适合。其“多源数据 + 定时任务 + 决策看板”的架构可直接迁移到企业级投研 Agent 或自动化报告生成系统中。
- **可能的风险**：依赖外部数据源稳定性；LLM 输出可能存在幻觉，需人工校验；若接入实盘交易，存在策略误判风险。

### 3.2 iFixAi（ifixai-ai/iFixAi）

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，可在 120 秒内给出审计结果。
- **为什么值得关注**：7 日涨星 +2205，总 star 8532，增速极快。AI Agent 治理、对齐、合规是当前 AI 进入生产环境的核心瓶颈，该项目精准切入这一需求。
- **技术栈/架构亮点**：Python + CLI，覆盖 agent-evaluation、ai-governance、hallucination-detection、prompt-injection、ISO-42001、NIST-AI-RMF、OWASP-LLM 等主题。架构上强调“由人或 Agent 自身运行”的双模式审计。
- **是否适合借鉴**：非常适合。在 AI 交易 Agent 中，可引入类似的审计层，对 Agent 的决策行为、输出一致性、合规性进行持续监控。
- **可能的风险**：审计标准本身可能不完善；对复杂 Agent 行为的评估可能存在误判；项目较新，长期维护活跃度待观察。

### 3.3 TradingAgents（TauricResearch/TradingAgents）

- **解决什么问题**：多 Agent LLM 金融交易框架，将交易决策拆分为多个 Agent 协作完成。
- **为什么值得关注**：总 star 98033，7 日涨星 +2089，是 AI 交易领域最具代表性的开源项目之一。多 Agent 架构在金融决策中的应用是当前研究热点。
- **技术栈/架构亮点**：Python + LLM + 多 Agent 协作。架构上采用“研究 Agent + 分析 Agent + 交易 Agent + 风控 Agent”的分工模式，体现了“决策分离、相互制衡”的设计思想。
- **是否适合借鉴**：非常适合。其多 Agent 分工与制衡机制可直接借鉴到企业级 AI 交易系统或投研决策系统中。
- **可能的风险**：策略过拟合风险；LLM 决策的可解释性不足；若直接用于实盘交易，存在资金风险。项目定位为研究工具，不应直接用于实盘。

### 3.4 Kronos（shiyu-coder/Kronos）

- **解决什么问题**：金融市场语言基础模型，旨在为金融 NLP 和量化研究提供预训练模型。
- **为什么值得关注**：总 star 37111，7 日涨星 +1002。金融领域基础模型是量化研究的前沿方向，该项目代表了“金融 + 大模型”的深度融合趋势。
- **技术栈/架构亮点**：Python，定位为 Foundation Model。具体架构细节需进一步调研，但其“金融语言基础模型”的定位本身具有重要参考价值。
- **是否适合借鉴**：适合作为研究方向参考。可调研其模型架构、训练数据、下游任务适配方式，评估是否可用于金融文本分析、情绪因子提取等场景。
- **可能的风险**：模型可能存在金融领域偏见；训练数据质量与合规性需关注；作为研究工具，不应直接用于交易决策。

### 3.5 Vibe-Trading（HKUDS/Vibe-Trading）

- **解决什么问题**：个人交易 Agent，结合 LLM、MCP、多 Agent 架构，支持回测与交易。
- **为什么值得关注**：总 star 30799，7 日涨星 +718。HKUDS 团队出品，将“Vibe Coding”理念引入交易领域，代表了 AI 交易 Agent 的产品化探索。
- **技术栈/架构亮点**：Python + LLM + MCP + 多 Agent。架构上强调“个人化交易 Agent”，支持回测与策略定制。
- **是否适合借鉴**：适合作为 AI 交易 Agent 产品化参考。其 MCP 集成方式、多 Agent 协作模式值得拆解。
- **可能的风险**：涉及加密交易，存在资金风险；策略过拟合风险；API key 安全风险。不建议直接用于实盘。

### 3.6 ai-berkshire（xbtlin/ai-berkshire）

- **解决什么问题**：基于 Claude Code / Codex 的价值投资研究框架，融合巴菲特、芒格、段永平、李录四大师方法论，支持多 Agent 对抗式分析。
- **为什么值得关注**：总 star 15513，7 日涨星 +382。将价值投资方法论数字化、Agent 化，是 AI 投研的差异化方向。
- **技术栈/架构亮点**：Python + Claude Code / Codex + 多 Agent 对抗分析。架构上强调“多大师方法论 + 对抗式研究”，体现了知识驱动的 Agent 设计思路。
- **是否适合借鉴**：非常适合。其“方法论数字化 + 多 Agent 对抗”的思路可迁移到企业级投研 Agent 中，用于基本面分析、风险评估等场景。
- **可能的风险**：价值投资方法论本身存在主观性；LLM 输出可能存在偏差；作为研究工具，不应直接用于投资决策。

### 3.7 MicroWorld（hongjin-he/MicroWorld）

- **解决什么问题**：美股市场的多 Agent 世界模型，模拟机构参与者、信息不对称和涌现价格动态。
- **为什么值得关注**：总 star 仅 1070，但 7 日涨星 +403，增速显著。市场微观结构模拟是量化研究的前沿方向，该项目代表了“Agent-based 市场模拟”的探索。
- **技术栈/架构亮点**：Python，多 Agent 世界模型。架构上模拟机构参与者与信息不对称，可用于研究市场微观结构、价格发现机制。
- **是否适合借鉴**：适合作为研究方向参考。可调研其 Agent 建模方式、信息不对称模拟机制，评估是否可用于策略压力测试、市场影响分析等场景。
- **可能的风险**：模拟结果可能与真实市场存在较大偏差；项目较新，成熟度待观察。

### 3.8 OpenBB（OpenBB-finance/OpenBB）

- **解决什么问题**：面向分析师、量化研究员和 AI Agent 的开放数据平台。
- **为什么值得关注**：总 star 71847，7 日涨星 +335。OpenBB 是金融数据平台领域的重要开源项目，其“面向 AI Agent”的定位与当前趋势高度契合。
- **技术栈/架构亮点**：Python，覆盖股票、加密、衍生品、固定收益、期权等多资产类别。架构上强调数据标准化与可扩展性。
- **是否适合借鉴**：非常适合。其数据标准化、多资产覆盖、AI Agent 接口设计值得借鉴到企业级金融数据平台中。
- **可能的风险**：数据源合规性需关注；作为数据平台，不直接涉及交易，风险相对较低。

### 3.9 a-stock-data（simonlin1212/a-stock-data）

- **解决什么问题**：A 股全栈数据工具包，覆盖行情、研报、资金面、筹码、公告、打板、ETF 期权、舆情互动等 15 个数据源、43 个端点。
- **为什么值得关注**：总 star 8710，7 日涨星 +285。A 股数据获取一直是量化研究的痛点，该项目提供了系统化的数据接入方案。
- **技术栈/架构亮点**：10 层架构、43 端点、备用源降级机制。架构上强调“全覆盖 + 降级容错”，体现了工程化的数据层设计。
- **是否适合借鉴**：非常适合。其“多源数据 + 备用源降级”的架构可直接借鉴到企业级金融数据工程中。
- **可能的风险**：数据源合规性需关注；数据质量与时效性需验证。

### 3.10 tickflow-stock-panel（shy3130/tickflow-stock-panel）

- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，基于 TickFlow 数据源，支持 LLM 策略定制与个股分析。
- **为什么值得关注**：总 star 2833，7 日涨星 +203。将选股、监控、回测整合到自托管工作台，代表了量化工具的产品化方向。
- **技术栈/架构亮点**：Python + FastAPI + DuckDB + Polars + React + LLM。架构上采用“数据层 + 计算层 + 展示层 + LLM 层”的分层设计，技术选型现代。
- **是否适合借鉴**：非常适合。其“自托管 + 零运维 + LLM 策略定制”的架构可直接借鉴到企业级量化工作台或投研工具中。
- **可能的风险**：依赖 TickFlow 数据源；作为个人开源项目，维护活跃度需关注。

## 4. 趋势归纳

### 技术趋势

1. **多 Agent 架构成为 AI 金融应用的主流范式**：`TradingAgents`、`Vibe-Trading`、`ai-berkshire`、`MicroWorld` 均采用多 Agent 协作或对抗式架构，体现了“决策分离、相互制衡”的设计思想。
2. **本地优先与零依赖推理**：`colibri`（纯 C 零依赖 MoE 推理）、`ds4`（本地推理引擎）、`atomic-agent`（本地优先 Agent）持续走强，反映了“本地运行、低成本、隐私保护”的工程趋势。
3. **AI Agent 治理与审计成为新赛道**：`iFixAi` 的快速涨星表明，Agent 行为审计、AI 对齐、合规评估正在成为独立的技术方向。
4. **金融数据工程向本地化、自托管演进**：`free-stockdb`、`a-stock-data`、`tickflow-stock-panel` 均强调本地缓存、增量同步、自托管，反映了金融数据工程的“去云端化”趋势。

### 产品趋势

1. **从“交易机器人”向“投研工作台”演进**：`daily_stock_analysis`、`tickflow-stock-panel`、`ai-berkshire` 均定位为研究/分析工具，而非直接交易机器人，反映了产品定位的成熟化。
2. **“零成本 + 定时运行”成为个人工具的关键卖点**：`daily_stock_analysis` 强调零成本定时运行，切中了个人开发者和研究者的需求。
3. **AI Agent 技能包（Skills）生态快速扩张**：`ui-ux-pro-max-skill`、`Claude-BugHunter`、`NVIDIA/skills` 等技能包项目大量涌现，反映了 Agent 能力模块化的趋势。

### 量化/交易策略趋势

1. **LLM 驱动的策略定制与个股分析**：`tickflow-stock-panel`、`Vibe-Trading` 均支持 LLM 策略定制，反映了“自然语言驱动策略生成”的趋势。
2. **多 Agent 对抗式研究**：`ai-berkshire` 采用多 Agent 对抗式分析，体现了“多视角制衡”的研究方法论。
3. **市场微观结构模拟**：`MicroWorld` 探索 Agent-based 市场模拟，代表了量化研究向微观结构深入的趋势。

### AI Agent 与自动化交易结合趋势

1. **Agent 审计与风控成为自动化交易的必要组件**：`iFixAi` 的崛起表明，AI Agent 进入交易场景后，审计与风控需求迫切。
2. **MCP 成为 Agent 与金融数据/交易系统的标准接口**：`Vibe-Trading`、`QuantDinger`、`awesome-mcp-servers` 均涉及 MCP，反映了 MCP 作为 Agent 工具调用标准的趋势。
3. **本地优先 Agent 与交易结合**：`atomic-agent` 强调本地优先，可能推动“本地运行交易 Agent”的方向。

### 值得后续做原型验证的方向

1. **多 Agent 投研工作台**：结合 `TradingAgents` 的多 Agent 架构与 `daily_stock_analysis` 的数据流水线，构建企业级投研 Agent。
2. **Agent 审计层**：参考 `iFixAi`，为 AI 交易 Agent 增加行为审计与合规检查层。
3. **本地优先金融数据引擎**：参考 `free-stockdb` 和 `a-stock-data`，构建本地缓存 + 增量同步的金融数据层。
4. **LLM 策略生成 + 回测验证闭环**：参考 `tickflow-stock-panel`，实现“自然语言策略 → 代码生成 → 回测 → 监控”的闭环。

## 5. 今日灵感清单

1. **MVP：多 Agent 投研报告生成器**：参考 `daily_stock_analysis` 和 `TradingAgents`，构建一个多 Agent 协作的投研报告生成工具，输入股票代码，输出多视角分析报告。可让 Codex 自动复现基础架构。
2. **调研：AI Agent 审计框架**：深入研究 `iFixAi` 的审计机制，评估是否可将其审计逻辑集成到企业级 AI 交易 Agent 的风控层。
3. **Demo：本地优先 A 股数据引擎**：参考 `free-stockdb` 和 `a-stock-data`，用 DuckDB + Polars 构建一个本地 A 股数据缓存与增量同步引擎，验证“零运维”数据层可行性。
4. **原型：LLM 策略生成 + 回测闭环**：参考 `tickflow-stock-panel`，实现“自然语言策略描述 → LLM 生成代码 → 回测 → 结果可视化”的闭环原型。
5. **调研：金融基础模型 Kronos**：调研 `Kronos` 的模型架构、训练数据与下游任务适配方式，评估是否可用于金融文本情绪因子提取。
6. **Demo：多 Agent 对抗式价值投资分析**：参考 `ai-berkshire`，构建一个多 Agent 对抗式分析框架，模拟“多头 vs 空头”的辩论式研究流程。
7. **原型：Agent 行为监控看板**：参考 `langfuse` 和 `iFixAi`，为 AI 交易 Agent 构建行为监控与审计看板，记录 Agent 的决策轨迹、输出一致性与合规性。
8. **调研：MCP 在金融数据接入中的应用**：调研 `Vibe-Trading` 和 `QuantDinger` 的 MCP 集成方式，评估是否可将 MCP 作为企业级金融数据接入的标准接口。
9. **Demo：市场微观结构模拟器**：参考 `MicroWorld`，构建一个简化的多 Agent 市场模拟器，用于策略压力测试与市场影响分析。
10. **Watchlist 候选**：将 `iFixAi`、`Kronos`、`MicroWorld`、`tickflow-stock-panel`、`ai-berkshire` 加入 watchlist，持续跟踪其架构演进与社区活跃度。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计与治理是新兴赛道，增速极快，值得持续跟踪其审计方法论与合规框架演进 |
| Kronos | 金融基础模型是量化研究前沿方向，需关注其模型迭代与下游任务适配 |
| MicroWorld | Agent-based 市场模拟是量化研究的新方向，项目较新但增速显著，值得跟踪 |
| tickflow-stock-panel | 自托管量化工作台的产品化思路清晰，技术选型现代，值得跟踪其功能迭代 |
| ai-berkshire | 价值投资方法论数字化 + 多 Agent 对抗式分析，差异化明显，值得跟踪 |
| TradingAgents | AI 交易多 Agent 框架的代表性项目，需持续关注其架构演进与社区生态 |
| daily_stock_analysis | 金融垂直领域增速最快项目之一，其数据流水线与推送架构值得跟踪 |
| Vibe-Trading | HKUDS 团队出品，AI 交易 Agent 产品化探索，需关注其 MCP 集成与策略定制能力 |
| OpenBB | 金融数据平台的重要开源项目，其 AI Agent 接口设计值得持续跟踪 |
| free-stockdb | 本地优先 A 股数据引擎，技术选型务实，值得跟踪其数据层架构演进 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告使用了 `baseline_1d`（2026-08-12）和 `baseline_7d`（2026-08-06）两个基线文件，1 日与 7 日涨星数据完整。
- **30 日基线缺失**：所有项目的 `star_delta_30d` 均为 `null`，无法提供 30 日涨星数据。
- **采集失败**：`needle` 项目的 `star_delta_7d` 为 `null`，7 日涨星数据缺失，已在表格中标注“信息不足”。
- **样本偏差**：本次候选集中存在大量“awesome-list”类项目（如 `build-your-own-x`、`awesome-selfhosted`、`public-apis`、`awesome-python`、`awesome-go` 等），这些项目因关键词误匹配进入候选集，与金融/量化交易的实际关联度低，可能稀释了真正金融垂直项目的信号。建议后续优化匹配逻辑，减少清单类项目的误匹配。
- **分类偏差**：部分项目的 `category_guess` 与实际情况存在偏差，如 `colibri`（MoE 推理引擎）被标记为 `quant_research`，`ui-ux-pro-max-skill`（设计工具）被标记为 `fintech_product`，需结合项目实际内容进行人工甄别。
