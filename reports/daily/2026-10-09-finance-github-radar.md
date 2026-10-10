# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-09

## 1. 今日摘要

- **今日最值得关注的 3 个方向**
  1. **AI Agent 治理与审计**：iFixAi 以 24h +359 星、7d +3804 星领跑，聚焦 AI Agent 的独立审计、对齐与合规评估，反映“Agent 经济”中可信执行验证的迫切需求。
  2. **本地化/边缘侧模型推理**：colibri（纯 C、零依赖、MoE 专家从磁盘流式加载）与 needle（2-bit、8–29MB 端侧自动化基础模型）同时上榜，显示“在自有硬件上跑前沿模型”的工程路线正在升温。
  3. **AI 辅助设计系统与 Agent Skills 生态**：ui-ux-pro-max-skill、open-design、awesome-design-md 等大量上榜，说明“用 Agent 生成专业 UI/设计资产”已成为高活跃赛道，对金融终端、交易看板等产品原型有直接借鉴价值。

- **是否出现新趋势**
  出现。本次榜单中“AI Agent 审计/对齐/治理”类项目首次占据榜首，且与金融风控关键词高度重合；同时“本地优先、零依赖、端侧推理”的模型工程路线明显走强。

- **是否出现值得复刻/参考的工程架构**
  有。iFixAi 的“Agent 自审计/人工审计”闭环、colibri 的“MoE 专家流式加载”纯 C 推理引擎、TradingAgents 的多智能体金融决策框架、QuantDinger 的“多租户交易 SaaS + 内置计费/结算”架构，均具备复刻或拆解价值。

- **是否有明显骗局、过度营销或高风险项目**
  本次样本中未发现明确骗局项目，但需注意：
  - `Financial_freedom`（24h +370 星）描述为“最全赚钱投资指南”，属于典型高营销话术，且无 license、无 topics，信息透明度低。
  - 多个项目因匹配到 `trading_bot`、`crypto_related` 被标记为中风险，但多数实为 awesome-list 或研究工具，误报率较高。
  - `QuantDinger`、`Vibe-Trading` 等涉及实盘/纸面交易与多租户 SaaS，需重点审查 API key 安全与合规边界。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | iFixAi | 23128 | +359 | +3804 | Python | AI 审计/风控 | AI Agent 独立审计与合规评估 | 高：Agent 治理闭环 | 低 |
| 2 | colibri | 40856 | +234 | +1725 | C | 量化研究/推理 | 纯 C 零依赖流式加载 MoE 模型 | 高：本地推理架构 | 低 |
| 3 | ui-ux-pro-max-skill | 134296 | +311 | +1688 | Python | 金融产品/设计 | AI 设计智能 Skill | 中：金融 UI 原型 | 低 |
| 4 | awesome-selfhosted | 325057 | +282 | +1568 | 无 | 自托管清单 | 自托管网络服务列表 | 中：交易系统自托管选型 | 中 |
| 5 | public-apis | 487047 | +204 | +1442 | Python | API 清单 | 免费 API 集合 | 中：金融数据源 | 中 |
| 6 | awesome-python | 326222 | +254 | +1438 | Python | 量化研究 | Python 工具清单 | 中：量化栈选型 | 低 |
| 7 | open-design | 100265 | +168 | +1052 | TypeScript | 金融产品/设计 | 本地优先 AI 设计引擎 | 高：交易看板原型 | 低 |
| 8 | awesome-go | 187614 | +174 | +959 | Go | 交易基础设施 | Go 框架/库清单 | 中：低延迟交易栈 | 中 |
| 9 | build-your-own-x | 552258 | +191 | +1006 | Markdown | 交易机器人 | 从零复刻技术教程集 | 中：复刻交易组件 | 中 |
| 10 | TradingAgents | 110423 | +107 | +870 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高：Agent 决策架构 | 低 |
| 11 | Financial_freedom | 6752 | +370 | +1159 | 无 | 加密交易 | 赚钱投资指南 | 低：营销话术样本 | 中 |
| 12 | awesome-design-md | 120081 | +136 | +787 | 无 | 设计系统 | DESIGN.md 品牌设计系统集合 | 中：Agent UI 规范 | 中 |
| 13 | needle | 13755 | +129 | +766 | Python | 端侧 AI | 2-bit 端侧自动化基础模型 | 高：边缘 Agent | 中 |
| 14 | awesome-dsh-plugin | 18250 | +119 | +611 | JavaScript | 交易基础设施 | DeepSeek Harness 插件清单 | 中：Agent 插件生态 | 低 |
| 15 | unsloth | 77662 | +103 | +510 | Python | AI 训练 | 本地 LLM 训练/微调 UI | 中：金融 LLM 微调 | 低 |
| 16 | headroom | 74857 | +76 | +553 | Python | AI 上下文压缩 | LLM 上下文压缩库/代理 | 高：降低 Agent token 成本 | 低 |
| 17 | Vibe-Trading | 35091 | +51 | +638 | Python | AI 交易/回测 | 个人交易 Agent | 高：多智能体交易参考 | 中 |
| 18 | atomic-agent | 3208 | +103 | +537 | TypeScript | 本地 Agent | 本地优先 AI Agent | 中：本地 Agent 架构 | 中 |
| 19 | ds4 | 23745 | +29 | +754 | C | 量化研究/推理 | DeepSeek 4 本地推理引擎 | 中：GPU 推理优化 | 低 |
| 20 | ruflo | 74219 | +61 | +474 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | 高：Agent 工作流 | 低 |
| 21 | Kronos | 40390 | +62 | +562 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融时序建模 | 低 |
| 22 | Soup | 8451 | +63 | +414 | Python | LLM 微调 | 单 YAML 低显存微调 | 中：低资源微调 | 低 |
| 23 | daily_stock_analysis | 66119 | +60 | +263 | Python | 股票分析 | LLM 多市场股票分析系统 | 高：数据工程+看板 | 低 |
| 24 | awesome-mcp-servers | 96013 | +67 | +246 | 无 | MCP 清单 | MCP 服务器集合 | 中：Agent 工具接入 | 低 |
| 25 | CyberStrikeAI | 7358 | +130 | +226 | Go | 风控/安全 | AI 原生安全运营系统 | 中：Agent 安全治理 | 低 |
| 26 | awesome-claude-code | 55336 | +44 | +359 | Python | Agent 资源 | Claude Code 资源清单 | 中：Agent 工具链 | 低 |
| 27 | OpenBot | 6285 | +44 | +380 | TypeScript | Agent 治理 | 开源 AI 数字员工 | 高：Agent 操作审计 | 中 |
| 28 | OpenBB | 74043 | +47 | +275 | Python | 金融数据平台 | 分析师/量化/AI Agent 数据平台 | 高：金融数据中台 | 中 |
| 29 | OpenStock | 19956 | +45 | +338 | TypeScript | 股票平台 | 开源行情/预警/公司洞察 | 中：行情终端产品 | 低 |
| 30 | free-for-dev | 139282 | +47 | +188 | HTML | 免费资源 | 开发者免费 SaaS/PaaS 清单 | 低：基础设施选型 | 低 |
| 31 | skill | 7756 | +54 | +262 | Python | Agent Skills | AI Agent 技能商店 | 中：金融 Skill 包 | 低 |
| 32 | gbrain | 30735 | +35 | +236 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中：Agent 编排 | 低 |
| 33 | modly | 8074 | +97 | 信息不足 | TypeScript | 量化研究 | 本地 3D 模型生成 | 低：非金融 | 低 |
| 34 | aurelio-finance | 1556 | +855 | 信息不足 | Python | 个人金融 | 开源个人财务 AI 顾问 | 高：财富管理 MVP | 低 |
| 35 | agentic-awesome-skills | 47403 | +25 | +201 | Python | Agent Skills | Agent 技能目录与控制面 | 中：Agent 技能治理 | 低 |
| 36 | tick-stock-panel | 5742 | +17 | +311 | Python | 量化工作台 | A 股自建策略+监控+回测 | 高：DuckDB/Polars 架构 | 低 |
| 37 | QuantDinger | 12606 | +35 | +217 | Python | AI 交易 OS | 多租户 AI 交易 SaaS | 高：交易 SaaS 架构 | 中 |
| 38 | trading-terminal | 545 | +48 | +285 | TypeScript | AI 交易终端 | Hyperliquid 自托管交易终端 | 中：策略验证闭环 | 低 |
| 39 | prompt-master | 14236 | +40 | +241 | 无 | 提示工程 | Claude 提示词 Skill | 低：提示词优化 | 低 |
| 40 | logo-design-skill | 2475 | +83 | 信息不足 | HTML | 设计 Skill | Logo 设计 Agent Skill | 低：品牌资产生成 | 低 |
| 41 | awesome-public-datasets | 79408 | +21 | +131 | 无 | 数据集清单 | 高质量公开数据集 | 中：金融数据集 | 中 |
| 42 | oh-my-openagent | 69924 | +10 | +162 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中：Agent 工作流 | 低 |
| 43 | awesome-cpp | 73713 | +12 | +129 | 无 | 量化研究 | C/C++ 资源清单 | 中：低延迟组件 | 低 |
| 44 | project-maya | 233 | +80 | 信息不足 | C++ | 量化研究/推理 | GLM-5.3-Flash 本地推理 | 中：MoE 本地部署 | 低 |
| 45 | awesome-rust | 59747 | +17 | +90 | Rust | 风控/量化 | Rust 资源清单 | 中：高性能风控 | 低 |
| 46 | ai-hedge-fund | 63918 | +9 | +83 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高：多 Agent 投研 | 低 |
| 47 | awesome-machine-learning | 74560 | +10 | +48 | Python | AI 交易 | ML 资源清单 | 中：ML 选型 | 低 |
| 48 | cs-video-courses | 83642 | +1 | +42 | 无 | 量化研究 | CS 视频课程清单 | 低：学习资源 | 中 |
| 49 | awesome-vue | 73517 | -4 | -21 | 无 | 量化研究 | Vue 资源清单 | 低：前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi
- **解决什么问题**：对 AI Agent 的行为进行独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审计，声称 120 秒内给出结论。
- **为什么值得关注**：24h +359、7d +3804，是本期涨星最猛的项目；topic 覆盖 AI 对齐、AI 治理、欧盟 AI 法案、ISO 42001、NIST AI RMF、OWASP LLM、提示注入检测等，说明其定位是“Agent 经济”中的合规与风控基础设施。
- **技术栈/架构亮点**：Python + CLI，Apache-2.0；从 topics 推断其包含诊断工具、幻觉检测、LLM 安全评估、风险评分等模块，适合作为 Agent 上线前的自动化审计层。
- **是否适合借鉴到 AI/自动化交易**：非常适合。可将其审计思路迁移到“交易 Agent 决策留痕、策略偏离检测、提示注入防护、合规检查”等场景，作为企业级 Agent 风控网关的参考架构。
- **可能风险**：项目较新（2026-04 创建），审计标准与评估基准的权威性尚未验证；若用于金融场景，需自行补充交易合规与资金安全审计维度。

### 3.2 colibri
- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，纯 C 实现、零依赖，专家从磁盘流式加载，以极小引擎承载超大模型。
- **为什么值得关注**：24h +234、7d +1725，总星 40856；代表“去中心化/本地化大模型推理”的工程趋势，对金融数据隐私敏感场景有吸引力。
- **技术栈/架构亮点**：纯 C、Apache-2.0、零依赖；核心是 MoE 专家流式加载与磁盘 I/O 优化，适合嵌入式或低资源环境。
- **是否适合借鉴**：适合。可借鉴其“按需加载专家权重”的思路，设计本地化金融 LLM 推理节点，降低显存与部署成本；也可用于边缘风控或本地研报解析。
- **可能风险**：topics 为空，文档与生态成熟度未知；纯 C 实现维护门槛高；与金融场景结合时需自行评估推理延迟与吞吐。

### 3.3 TradingAgents
- **解决什么问题**：多智能体 LLM 金融交易框架，模拟分析师、研究员、交易员等多角色协作完成交易决策。
- **为什么值得关注**：总星 110423，7d +870；是“AI Agent + 量化交易”方向的高星代表，且近 30 天有 push。
- **技术栈/架构亮点**：Python、Apache-2.0；topics 为 agent、finance、llm、multiagent、trading，核心是多角色 Agent 协作与 LLM 决策链路。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色分工、辩论/复核机制，用于企业级投研 Agent 或交易信号生成流程；也可作为 Agent 编排框架的金融领域参考实现。
- **可能风险**：属于研究工具，回测结果可能过拟合；LLM 决策存在幻觉与不可复现性；不应直接用于实盘。

### 3.4 QuantDinger
- **解决什么问题**：开源 AI 交易 OS，支持 Agent 交易、vibe trading、策略研究、Python 策略编写、回测、纸面/实盘交易，覆盖加密、股票、外汇，并可启动多租户交易 SaaS。
- **为什么值得关注**：7d +217，总星 12606；架构完整度较高，是“交易系统产品化”的典型样本。
- **技术栈/架构亮点**：Python、Apache-2.0；topics 含 alpaca、binance、mcp-server、saas、typesafe-ai 等，说明其集成了交易所接口、MCP 服务与多租户计费/结算能力。
- **是否适合借鉴**：适合。可重点研究其“多租户 SaaS + 内置用户管理/计费/结算”的架构，以及“研究→回测→纸面→实盘”的工程流水线设计。
- **可能风险**：涉及实盘交易与交易所 API，存在资金与密钥安全风险；多租户 SaaS 涉及金融合规与牌照问题；crypto_related 标记提示需谨慎评估。

### 3.5 daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：总星 66119，7d +263；是“LLM + 数据工程 + 决策看板”的完整落地案例，且为中文项目，对 A 股场景有直接参考价值。
- **技术栈/架构亮点**：Python、MIT；topics 含 a-stock、ai-agent、llm、quant、quantitative-finance，强调多源数据接入与定时自动化。
- **是否适合借鉴**：适合。可借鉴其“多源行情 + 新闻 + LLM 分析 + 看板 + 推送”的数据流水线，用于企业级投研日报或舆情监控 MVP。
- **可能风险**：数据源稳定性与合规性需自行验证；LLM 生成的“分析结论”不应直接作为交易依据。

### 3.6 tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 策略定制、个股分析与复盘。
- **为什么值得关注**：7d +311，总星 5742；技术栈现代，适合作为轻量级量化工作台原型。
- **技术栈/架构亮点**：Python、MIT；topics 含 duckdb、polars、fastapi、react、backtesting、quant，说明其采用“DuckDB + Polars 本地分析 + FastAPI 服务 + React 前端”的现代数据栈。
- **是否适合借鉴**：非常适合。可复刻其“本地 DuckDB 存储 + Polars 向量化计算 + FastAPI + React”的轻量量化工作台架构，用于策略研究或数据探索 MVP。
- **可能风险**：个人开源项目，维护持续性不确定；回测与实盘一致性需自行验证。

### 3.7 OpenBB
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，覆盖股票、加密、衍生品、固定收益、经济数据等。
- **为什么值得关注**：总星 74043，7d +275；是金融数据中台方向的成熟开源项目。
- **技术栈/架构亮点**：Python；topics 含 ai、crypto、derivatives、equity、fixed-income、machine-learning、quantitative-finance，强调多资产数据接入与 AI 友好接口。
- **是否适合借鉴**：适合。可作为企业级金融数据中台或 Agent 数据接入层的参考实现，避免重复造轮子。
- **可能风险**：license 为 Other，商用需审查；数据源许可与延迟需自行评估。

### 3.8 ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，通过多个 Agent 角色协作完成投资研究与决策。
- **为什么值得关注**：总星 63918，是“AI 对冲基金”概念的代表性项目，近 30 天有 push。
- **技术栈/架构亮点**：Python、MIT；topics 为空，但从描述推断为多 Agent 投研模拟。
- **是否适合借鉴**：适合。可借鉴其“多角色投研团队”的 Agent 分工与决策流程，用于投研自动化或信号生成原型。
- **可能风险**：研究/教育属性强，回测结果不代表实盘；LLM 决策存在过拟合与幻觉风险。

### 3.9 aurelio-finance
- **解决什么问题**：开源个人财务应用，内置 AI 财务顾问，可跟踪净资产、投资、ETF、现金与债务。
- **为什么值得关注**：24h +855 星（基数小、爆发力强），创建于 2026-10-06，属于全新项目；是“AI + 个人财富管理”的轻量 MVP 样本。
- **技术栈/架构亮点**：Python、MIT；topics 含 ai、etf、finance、llm、net-worth、portfolio-tracker、self-hosted，强调本地自托管与 AI 顾问。
- **是否适合借鉴**：适合。可复刻其“本地优先 + AI 财务顾问 + 资产跟踪”的产品形态，用于财富管理或家庭资产负债表 MVP。
- **可能风险**：项目极新，代码质量与安全未经验证；涉及个人财务数据，需注意隐私与本地存储安全。

### 3.10 headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前进行压缩，减少 token 消耗，同时保持回答质量。
- **为什么值得关注**：总星 74857，7d +553；是“上下文工程/成本优化”方向的高星项目，对高频调用 LLM 的金融 Agent 有直接降本价值。
- **技术栈/架构亮点**：Python、Apache-2.0；topics 含 mcp、proxy、rag、token-optimization、context-engineering，支持库、代理与 MCP 服务器三种形态。
- **是否适合借鉴**：非常适合。可将其作为金融 Agent 的上下文压缩中间层，降低研报解析、行情摘要、日志审计等场景的 token 成本。
- **可能风险**：压缩可能损失关键信息，金融场景需验证压缩后决策一致性。

## 4. 趋势归纳

- **技术趋势**
  - **本地化/边缘侧模型推理**：colibri、needle、ds4、project-maya 等集中出现，显示“自有硬件跑前沿模型”的工程路线正在加速。
  - **上下文工程与 token 优化**：headroom 等项目的走红，说明 Agent 规模化落地后，成本控制成为关键工程问题。
  - **现代数据栈进入量化工作台**：tick-stock-panel 采用 DuckDB + Polars + FastAPI + React，反映轻量、零运维、本地优先的量化工具链趋势。

- **产品趋势**
  - **AI Agent 治理与审计产品化**：iFixAi 的爆发说明“Agent 可信执行验证”正在成为独立产品品类。
  - **AI 设计系统与 Agent Skills 生态**：ui-ux-pro-max-skill、open-design、awesome-design-md 等大量上榜，显示“Agent 生成专业 UI/设计资产”已成为高活跃赛道。
  - **个人财富管理 AI 化**：aurelio-finance 的快速起量，反映“本地优先 + AI 财务顾问”的产品形态受到关注。

- **量化/交易策略趋势**
  - **多智能体 LLM 交易框架**：TradingAgents、Vibe-Trading、ai-hedge-fund 等持续活跃，多角色协作与辩论式决策成为主流范式。
  - **金融基础模型**：Kronos 等“金融市场语言基础模型”项目保持热度，显示金融时序建模与 LLM 的融合仍在探索。
  - **交易系统产品化/SaaS 化**：QuantDinger 的多租户交易 SaaS 架构，反映“交易系统即产品”的趋势。

- **AI Agent 与自动化交易结合趋势**
  - **Agent 审计与风控前置**：iFixAi、CyberStrikeAI、OpenBot 等项目显示，Agent 治理、操作审计与安全执行正在成为自动化交易的前置条件。
  - **MCP 与插件生态**：awesome-mcp-servers、awesome-dsh-plugin、agentic-awesome-skills 等上榜，说明 Agent 工具接入与技能治理生态正在快速扩张。
  - **本地优先 Agent**：atomic-agent、needle 等项目强调本地运行与隐私保护，适合金融数据敏感场景。

- **值得后续做原型验证的方向**
  - 交易 Agent 决策留痕与审计网关
  - 本地化金融 LLM 推理节点
  - 基于 DuckDB/Polars 的轻量量化工作台
  - 多智能体投研与信号生成框架
  - 金融 Agent 上下文压缩与成本优化中间层

## 5. 今日灵感清单

1. **MVP：交易 Agent 审计网关**  
   参考 iFixAi，做一个轻量级“交易 Agent 决策留痕 + 策略偏离检测 + 提示注入扫描”的审计服务，输出风险评分与合规报告。

2. **MVP：本地金融 LLM 推理节点**  
   参考 colibri/needle，用纯 C 或轻量运行时在本地 GPU 上部署一个金融领域小模型，用于研报解析或舆情分类，验证隐私与成本优势。

3. **MVP：DuckDB + Polars 量化工作台**  
   参考 tick-stock-panel，用 DuckDB 存本地行情、Polars 做因子计算、FastAPI 暴露接口、React 做看板，快速搭建一个零运维策略研究环境。

4. **调研：多智能体投研决策框架**  
   拆解 TradingAgents、ai-hedge-fund、Vibe-Trading 的 Agent 角色分工与决策流程，提炼可复用的“分析师-研究员-交易员-风控”协作模板。

5. **调研：Agent 上下文压缩中间层**  
   验证 headroom 在金融场景（研报、行情摘要、日志审计）中的 token 节省率与决策一致性，评估是否可作为企业级 Agent 的标配组件。

6. **Codex/Agent 自动复现：AI 设计系统生成交易看板**  
   参考 open-design、ui-ux-pro-max-skill，让 Codex 自动生成一套金融交易看板或风控仪表盘原型，验证“Agent 生成专业 UI”的可行性。

7. **MVP：个人财富管理 AI 顾问**  
   参考 aurelio-finance，做一个本地优先的“净资产跟踪 + AI 财务顾问”应用，重点验证本地数据隐私与 LLM 建议的可解释性。

8. **调研：金融数据中台选型**  
   对比 OpenBB、public-apis、awesome-public-datasets 的数据覆盖与接入成本，为 Agent 数据层选型提供依据。

9. **加入 watchlist：QuantDinger**  
   观察其多租户交易 SaaS 架构与 MCP 集成方式，作为“交易系统产品化”的参考样本。

10. **加入 watchlist：Kronos**  
    跟踪金融基础模型的进展，评估其在金融时序预测与异常检测中的可用性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计/治理赛道爆发，金融风控可借鉴其审计闭环 |
| TradingAgents | 多智能体金融交易框架高星代表，适合拆解 Agent 决策架构 |
| QuantDinger | 交易系统产品化/多租户 SaaS 架构完整，值得长期跟踪 |
| tick-stock-panel | 现代数据栈量化工作台，DuckDB/Polars 架构可复刻 |
| Kronos | 金融基础模型方向，关注其后续演进与可用性 |
| headroom | Agent 上下文压缩与成本优化，金融场景降本潜力大 |
| OpenBB | 金融数据中台成熟项目，适合作为 Agent 数据层参考 |
| aurelio-finance | 新项目爆发力强，观察“AI + 个人财富管理”产品形态 |
| colibri | 本地化 MoE 推理架构，关注其生态与文档成熟度 |
| Vibe-Trading | 个人交易 Agent 与 MCP 集成，观察其实盘安全边界 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-10-08）与 `baseline_7d`（2026-10-02），1 日与 7 日涨星数据基本完整。
- **缺失数据**：部分项目（如 modly、aurelio-finance、logo-design-skill、project-maya）的 `star_delta_7d` 为 null，已在表格中标注“信息不足”；所有项目的 `star_delta_30d` 均为 null，无法提供 30 日趋势。
- **采集失败**：未发现明显采集失败，但 `Financial_freedom`、`colibri`、`ds4`、`Kronos`、`gbrain` 等项目 topics 为空，分类与用途判断依赖描述文本，存在误判可能。
- **样本偏差**：候选集由关键词匹配生成，大量 awesome-list 与通用 AI 项目因命中“quant”“trading bot”“fintech”等关键词被纳入，导致金融/交易相关项目的真实占比被稀释；`risk_flags` 中的 `trading_bot`、`crypto_related` 标记存在明显误报（如 awesome-selfhosted、build-your-own-x 被标记为 trading_bot），风险等级仅供参考。
