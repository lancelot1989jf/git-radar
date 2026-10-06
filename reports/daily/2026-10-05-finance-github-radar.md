# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-10-05

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 治理与审计**：`iFixAi` 以 24h +771 星、7d +4918 星位居榜首，聚焦 AI Agent 的独立审计、对齐、安全与合规，反映“Agent 经济”中可信性验证成为刚需。
  2. **AI 交易 Agent 与多智能体框架**：`TradingAgents`、`Vibe-Trading`、`QuantDinger`、`ai-hedge-fund` 等项目持续活跃，LLM 多智能体交易、回测、模拟/实盘一体化成为主流叙事。
  3. **本地化/边缘化 LLM 推理与微调**：`colibri`、`ds4`、`Soup`、`needle`、`unsloth` 等项目强调在消费级硬件、本地优先、低 VRAM 条件下运行或微调模型，为金融数据隐私和低延迟推理提供工程参考。

- **是否出现新趋势**：
  - 出现明显的 **“AI Agent 可审计性/合规性”** 趋势，`iFixAi` 的爆发式涨星说明市场对 Agent 行为验证、幻觉检测、提示注入防护、ISO/NIST/欧盟 AI 法案对齐的关注快速上升。
  - **“Vibe Trading / Vibe Coding”向交易域渗透**：`Vibe-Trading`、`QuantDinger` 将自然语言策略生成、Agent 交易、回测与多租户 SaaS 结合，形成“AI 交易操作系统”产品化趋势。
  - **本地优先 + BYOK（自带密钥）**：`open-design`、`atomic-agent`、`colibri` 等项目强调本地运行、自带模型密钥，降低数据外泄和 API 成本。

- **是否出现值得复刻/参考的工程架构**：
  - `iFixAi` 的“120 秒内回答 Agent 是否在做该做的事”审计架构，值得借鉴到企业级 Agent 风控与合规流水线。
  - `TradingAgents` 的多智能体 LLM 金融交易框架，可作为 AI 交易决策系统的参考架构。
  - `tick-stock-panel` 的“自托管、零运维 A 股选股 + 监控 + 回测工作台”，结合 DuckDB、Polars、FastAPI、React，是轻量量化工作台的优秀范本。
  - `headroom` 的“LLM 输入前压缩工具输出/日志/JSON”架构，对高频行情、订单簿、回测日志等 token 密集场景有直接借鉴价值。

- **是否有明显骗局、过度营销或高风险项目**：
  - `Financial_freedom`（“最全赚钱投资指南”）描述带有强烈收益暗示，且无 license、无 topics，需警惕内容质量与营销性质。
  - 多个项目描述中出现“vibe trading”“AI Trading OS”“multi-tenant trading SaaS”等营销化表述，需区分工程参考与收益承诺。
  - 本批候选包含大量 `awesome-*` 列表类项目，它们因关键词命中进入榜单，但并非直接交易系统，需避免误读为量化策略信号。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | iFixAi | 21325 | +771 | +4918 | Python | AI 审计/风控 | AI Agent 独立审计，120 秒验证 Agent 行为 | 高：Agent 合规与行为验证架构 | 低 |
| 2 | public-apis | 486380 | +258 | +2219 | Python | API 列表 | 免费 API 集合 | 中：数据源发现 | 中 |
| 3 | ui-ux-pro-max-skill | 133422 | +332 | +2092 | Python | AI 设计技能 | 多平台 UI/UX 设计智能技能 | 中：Agent 前端生成 | 低 |
| 4 | awesome-selfhosted | 324195 | +244 | +1645 | 无 | 自托管列表 | 可自托管网络服务列表 | 中：交易基础设施自托管 | 中 |
| 5 | colibri | 39845 | +241 | +1656 | C | 本地推理 | 纯 C、零依赖、从磁盘流式加载 MoE 模型 | 高：低资源本地推理 | 低 |
| 6 | awesome-python | 325464 | +222 | +1551 | Python | Python 资源 | Python 工具精选列表 | 低 | 低 |
| 7 | build-your-own-x | 551760 | +175 | +1267 | Markdown | 教程列表 | 从零复刻技术项目教程 | 中：复刻交易系统组件 | 中 |
| 8 | open-design | 99606 | +150 | +1067 | TypeScript | AI 设计 | 本地优先 AI 设计引擎，BYOK | 中：Agent 生成交易看板 | 低 |
| 9 | awesome-design-md | 119715 | +136 | +1063 | 无 | 设计系统 | DESIGN.md 品牌设计系统集合 | 低 | 中 |
| 10 | awesome-go | 187150 | +159 | +1085 | Go | Go 资源 | Go 框架/库精选列表 | 中：Go 交易基础设施选型 | 中 |
| 11 | Financial_freedom | 5861 | +69 | +1254 | 无 | 投资指南 | “最全赚钱投资指南” | 低：需警惕收益营销 | 中 |
| 12 | TradingAgents | 109908 | +105 | +763 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高：AI 交易决策架构 | 低 |
| 13 | ds4 | 23584 | +95 | +815 | C | 本地推理 | DeepSeek 4 本地推理引擎 | 中：本地模型推理 | 低 |
| 14 | awesome-dsh-plugin | 17856 | +75 | +665 | JavaScript | 插件列表 | DeepSeek Harness 插件精选 | 低 | 低 |
| 15 | Soup | 8219 | +75 | +723 | Python | LLM 微调 | 单 YAML 微调 LLM，4GB GPU 训练 8B | 高：低资源微调 | 低 |
| 16 | Vibe-Trading | 34818 | +86 | +553 | Python | AI 交易/回测 | “Vibe-Trading：个人交易 Agent” | 高：自然语言交易 Agent | 中 |
| 17 | ruflo | 73951 | +66 | +489 | TypeScript | Agent 框架 | 多智能体 swarm、自适应记忆、RAG | 高：企业级 Agent 编排 | 低 |
| 18 | free-for-dev | 139243 | +55 | +427 | HTML | 免费资源 | SaaS/PaaS/IaaS 免费层列表 | 低 | 低 |
| 19 | needle | 13301 | +64 | +478 | Python | 边缘 AI | 2-bit、8-29MB 设备端基础模型 | 中：边缘推理 | 中 |
| 20 | Kronos | 40041 | +88 | +417 | Python | 金融基础模型 | 金融市场语言基础模型 | 高：金融时序基础模型 | 低 |
| 21 | headroom | 74465 | +31 | +420 | Python | 上下文压缩 | LLM 输入前压缩日志/JSON/RAG | 高：行情/日志 token 优化 | 低 |
| 22 | OpenBot | 6093 | +51 | +399 | TypeScript | Agent 治理 | 每个 AI 协作者拥有独立计算机环境 | 中：Agent 操作审计 | 中 |
| 23 | OpenStock | 19744 | +70 | +290 | TypeScript | 行情平台 | 开源实时行情、警报、公司洞察 | 中：行情产品原型 | 低 |
| 24 | tick-stock-panel | 5623 | +48 | +313 | Python | A 股量化工作台 | 自托管选股+监控+回测，LLM 驱动 | 高：轻量量化工作台 | 低 |
| 25 | awesome-claude-code | 55122 | +31 | +346 | Python | Claude Code 资源 | Claude Code 技能/插件精选 | 低 | 低 |
| 26 | unsloth | 77249 | +39 | +264 | Python | LLM 微调 | 本地 UI 运行/训练 LLM | 中：本地模型训练 | 低 |
| 27 | prompt-master | 14094 | +51 | +290 | 无 | 提示工程 | 为任意 AI 工具生成准确提示 | 低 | 低 |
| 28 | daily_stock_analysis | 65938 | +36 | +157 | Python | AI 股票分析 | LLM 多市场股票分析、自动推送 | 中：AI 投研流水线 | 低 |
| 29 | agentic-awesome-skills | 47285 | +27 | +231 | Python | Agent 技能库 | 2400+ Agent 技能目录与控制面 | 中：Agent 技能治理 | 低 |
| 30 | oh-my-openagent | 69834 | +30 | +196 | TypeScript | Agent 编排 | 图工程化 Agent 编排 | 中：Agent 工作流图化 | 低 |
| 31 | hexstrike-ai | 12444 | +71 | +221 | Python | 安全 MCP | AI Agent 自主运行 150+ 安全工具 | 中：安全测试自动化 | 低 |
| 32 | skill | 7579 | +37 | +242 | Python | 技能商店 | 自动抓取 GitHub 技能项目 | 低 | 低 |
| 33 | awesome-mcp-servers | 95858 | +20 | +211 | 无 | MCP 列表 | MCP 服务器集合 | 中：MCP 生态选型 | 低 |
| 34 | V3SP3R | 1620 | +177 | +180 | Java | 风控 | “AI Flipper control” | 信息不足 | 低 |
| 35 | gbrain | 30583 | +24 | +160 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent Brain | 中：Agent 记忆/决策 | 低 |
| 36 | atomic-agent | 2817 | +20 | +296 | TypeScript | 本地 Agent | 本地优先 AI Agent，llama.cpp | 中：本地 Agent 架构 | 中 |
| 37 | QuantDinger | 12477 | +26 | +180 | Python | AI 交易 OS | 开源 AI 交易 OS，多租户 SaaS | 高：交易系统产品化 | 中 |
| 38 | awesome-jev | 2161 | +23 | +221 | Python | Jev 生态 | Jev 类型化决策模型项目列表 | 中：类型化决策 | 中 |
| 39 | easy-stock | 1304 | +27 | +250 | Go | A 股 AI 投研 | A 股行情分析与 AI 投研桌面工作台 | 中：桌面投研工具 | 低 |
| 40 | Financial-API | 4046 | +41 | +152 | TypeScript | 金融数据 API | 同花顺官方 A 股数据服务 | 高：A 股数据基础设施 | 低 |
| 41 | awesome-cpp | 73639 | +16 | +112 | 无 | C++ 资源 | C++ 框架/库精选 | 低 | 低 |
| 42 | OpenBB | 73890 | +36 | 信息不足 | Python | 开放数据平台 | 分析师/量化/AI Agent 开放数据平台 | 高：金融数据平台 | 中 |
| 43 | awesome-public-datasets | 79322 | +9 | +95 | 无 | 数据集列表 | 高质量开放数据集列表 | 中：数据源发现 | 中 |
| 44 | cs-video-courses | 83625 | +11 | +47 | 无 | 课程列表 | 计算机科学视频课程 | 低 | 中 |
| 45 | awesome-rust | 59685 | +9 | +92 | Rust | Rust 资源 | Rust 代码与资源精选 | 中：Rust 交易系统选型 | 低 |
| 46 | ai-hedge-fund | 63862 | +4 | +76 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高：多 Agent 投研决策 | 低 |
| 47 | awesome-machine-learning | 74528 | +6 | +43 | Python | ML 资源 | 机器学习框架/库精选 | 低 | 低 |
| 48 | awesome-vue | 73532 | -1 | -11 | 无 | Vue 资源 | Vue.js 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi
- **解决什么问题**：AI Agent 行为是否按预期执行、是否产生幻觉、是否被提示注入攻击、是否符合 ISO 42001/NIST AI RMF/欧盟 AI 法案等治理要求。
- **为什么值得关注**：24h +771、7d +4918 的爆发式涨星，说明“Agent 经济”中审计与可信性验证需求急剧上升。对金融场景中 AI 交易 Agent 的合规审计有直接参考价值。
- **技术栈/架构亮点**：Python、Apache-2.0、CLI 形态，支持人工或 Agent 自审计，声称 120 秒内给出结论。Topics 覆盖 agent-evaluation、ai-alignment、ai-governance、hallucination-detection、prompt-injection、llm-security 等。
- **是否适合借鉴**：非常适合。可将其审计思路引入 AI 交易 Agent 的事前/事后验证流水线，例如在策略执行前验证 Agent 是否偏离既定风控规则。
- **可能风险**：项目较新（2026-04 创建），需关注审计标准本身的权威性；金融场景需额外补充交易合规与资金安全审计。

### 3.2 TradingAgents
- **解决什么问题**：用多智能体 LLM 框架模拟金融交易决策流程，覆盖研究、分析、交易等环节。
- **为什么值得关注**：109k stars，持续活跃，是“LLM 多智能体交易”方向的代表性项目。
- **技术栈/架构亮点**：Python、Apache-2.0，多智能体协作，topics 含 agent、finance、llm、multiagent、trading。
- **是否适合借鉴**：适合。可作为 AI 交易决策系统的参考架构，尤其是多角色分工（分析师、交易员、风控）的 Agent 编排。
- **可能风险**：研究工具属性强，策略过拟合、回测偏差、实盘泛化能力存疑；不应直接用于真实资金交易。

### 3.3 Vibe-Trading
- **解决什么问题**：将自然语言“vibe”转化为交易策略，提供个人交易 Agent。
- **为什么值得关注**：HKUDS 出品，34.8k stars，topics 含 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent，是“Vibe Trading”叙事的代表。
- **技术栈/架构亮点**：Python、MIT，集成 MCP、多智能体、回测。
- **是否适合借鉴**：适合研究自然语言策略生成与 Agent 交易闭环，但需警惕“vibe”策略的过拟合与不可解释性。
- **可能风险**：crypto_related、likely_research_tool；自然语言策略易产生虚假回测收益，需严格样本外验证。

### 3.4 QuantDinger
- **解决什么问题**：提供开源 AI 交易操作系统，支持研究、Python 策略、回测、模拟/实盘交易，并可启动多租户交易 SaaS。
- **为什么值得关注**：将交易系统与 SaaS 化、用户管理、计费、支付、结算结合，是交易系统产品化的参考。
- **技术栈/架构亮点**：Python、Apache-2.0，集成 Alpaca、Binance、MCP server，覆盖 crypto、stocks、forex。
- **是否适合借鉴**：适合研究交易系统产品化架构，尤其是多租户、计费与结算模块。
- **可能风险**：crypto_related；多交易所、多资产实盘接入带来 API key 安全与合规风险；SaaS 化交易系统需关注监管边界。

### 3.5 tick-stock-panel
- **解决什么问题**：A 股“选股 + 监控 + 回测”量化工作台，LLM 驱动策略定制、个股分析与复盘，支持第三方数据源接入。
- **为什么值得关注**：轻量、自托管、零运维，技术栈现代（DuckDB、Polars、FastAPI、React），是个人量化工作台的优秀范本。
- **技术栈/架构亮点**：Python、MIT，topics 含 a-stock、ai-agent、backtesting、duckdb、polars、fastapi、react、screener。
- **是否适合借鉴**：非常适合。可直接复刻其“本地数据 + 回测 + LLM 分析”的轻量架构，用于 A 股研究原型。
- **可能风险**：likely_research_tool；A 股数据质量与复权处理需自行验证；LLM 生成的策略存在过拟合风险。

### 3.6 Kronos
- **解决什么问题**：构建“金融市场语言”基础模型，面向金融时序建模。
- **为什么值得关注**：40k stars，定位为金融基础模型，是量化研究向基础模型方向探索的代表。
- **技术栈/架构亮点**：Python、MIT，topics 为空，信息有限。
- **是否适合借鉴**：适合作为金融时序基础模型的研究方向参考，但需自行验证模型能力与数据覆盖。
- **可能风险**：likely_research_tool；基础模型在金融时序上的泛化性与因果性存疑；项目近 30 天无 push，维护活跃度需关注。

### 3.7 headroom
- **解决什么问题**：在 LLM 输入前压缩工具输出、日志、文件、RAG 分块，降低 token 消耗。
- **为什么值得关注**：对金融场景中订单簿、行情、回测日志等 token 密集输入有直接优化价值。
- **技术栈/架构亮点**：Python、Apache-2.0，提供库、代理、MCP server 三种形态，支持 FastAPI、LangChain、OpenAI、Anthropic。
- **是否适合借鉴**：非常适合。可将压缩层引入 AI 交易 Agent 的上下文工程，降低高频数据输入成本。
- **可能风险**：压缩可能损失关键金融信息，需验证压缩后决策一致性。

### 3.8 ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作完成投研决策。
- **为什么值得关注**：63.8k stars，是 AI 多智能体投研的经典参考项目。
- **技术栈/架构亮点**：Python、MIT，多 Agent 团队模拟。
- **是否适合借鉴**：适合研究多 Agent 投研分工与决策流程，但近期涨星放缓（24h +4），热度下降。
- **可能风险**：likely_research_tool；模拟环境与实盘差距大，策略过拟合风险高。

### 3.9 OpenBB
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台。
- **为什么值得关注**：73.9k stars，覆盖 equity、crypto、derivatives、fixed-income、economics 等，是金融数据基础设施的重要参考。
- **技术栈/架构亮点**：Python，topics 含 ai、crypto、quantitative-finance、machine-learning。
- **是否适合借鉴**：适合作为金融数据接入层的参考，尤其是多资产数据标准化。
- **可能风险**：crypto_related；7d 涨星数据缺失，需关注数据源许可与稳定性。

### 3.10 Financial-API
- **解决什么问题**：同花顺官方 A 股金融数据服务，提供实时/历史行情、财务报表、指数、板块、涨停数据，支持 API、MCP、CLI、Python。
- **为什么值得关注**：官方数据源 + MCP 支持，对 A 股 AI Agent 与量化研究是重要基础设施。
- **技术栈/架构亮点**：TypeScript、MIT，topics 含 a-share、ai-agent、duckdb、mcp、rest-api。
- **是否适合借鉴**：非常适合。可直接作为 A 股数据接入层，结合 MCP 让 Agent 获取行情与财务数据。
- **可能风险**：likely_research_tool；数据服务条款、频率限制与商业使用边界需确认。

## 4. 趋势归纳

- **技术趋势**：
  - **本地优先与边缘推理**：`colibri`、`ds4`、`needle`、`atomic-agent`、`unsloth` 共同指向“在自有硬件上运行/微调模型”，降低数据外泄与推理成本。
  - **上下文工程与 token 优化**：`headroom` 代表 LLM 输入压缩成为 Agent 规模化落地的关键基础设施。
  - **MCP 生态成熟**：`awesome-mcp-servers`、`Financial-API`、`Vibe-Trading`、`QuantDinger` 均集成 MCP，工具调用标准化趋势明显。
  - **类型化决策模型**：`awesome-jev`、`QuantDinger` 提及 Jev System One，显示“类型化决策”作为 AI 决策可靠性手段开始出现。

- **产品趋势**：
  - **AI 交易操作系统/SaaS 化**：`QuantDinger` 将交易系统与多租户 SaaS、计费、结算结合，交易工具从单机脚本走向平台化。
  - **AI Agent 审计与治理产品化**：`iFixAi` 将 Agent 行为验证产品化，未来可能成为金融 Agent 合规的标配。
  - **设计智能与 Agent 前端生成**：`ui-ux-pro-max-skill`、`open-design`、`awesome-design-md` 显示 Agent 生成交易看板、仪表盘的能力快速增强。

- **量化/交易策略趋势**：
  - **LLM 多智能体交易**：`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 持续演进，多角色 Agent 协作成为主流范式。
  - **金融基础模型**：`Kronos` 探索金融市场语言基础模型，显示量化研究向预训练模型方向延伸。
  - **A 股量化工作台轻量化**：`tick-stock-panel`、`easy-stock`、`daily_stock_analysis` 显示 A 股个人量化工具向自托管、低运维、LLM 驱动方向发展。

- **AI Agent 与自动化交易结合趋势**：
  - **Agent 行为审计与交易合规结合**：`iFixAi` 的审计能力可前置到交易 Agent 决策链路，形成“决策-审计-执行”闭环。
  - **本地 Agent + 交易数据隐私**：`atomic-agent`、`colibri` 的本地推理能力适合处理敏感金融数据。
  - **MCP 作为交易工具标准接口**：多个交易项目通过 MCP 暴露行情、下单、回测工具，降低 Agent 集成成本。

- **值得后续做原型验证的方向**：
  - 基于 `tick-stock-panel` 架构复刻轻量 A 股量化工作台，并接入 `Financial-API` 数据源。
  - 基于 `headroom` 构建行情/日志压缩层，验证 AI 交易 Agent 的 token 成本与决策一致性。
  - 基于 `iFixAi` 思路设计交易 Agent 的事前风控审计模块。
  - 基于 `TradingAgents` 或 `ai-hedge-fund` 复现多智能体投研决策流程，并加入严格样本外验证。

## 5. 今日灵感清单

1. **MVP：A 股轻量量化工作台**：复刻 `tick-stock-panel` 的 DuckDB + Polars + FastAPI + React 架构，接入 `Financial-API`，实现选股、监控、回测三合一。
2. **MVP：AI 交易 Agent 上下文压缩层**：基于 `headroom` 构建订单簿/行情/日志压缩代理，量化 token 节省与决策一致性损失。
3. **调研：AI Agent 审计标准**：深入研究 `iFixAi` 的审计维度（幻觉检测、提示注入、对齐、ISO/NIST/欧盟 AI 法案），评估其在金融交易 Agent 中的适用性。
4. **Demo：多智能体投研决策流水线**：用 Codex/Agent 复现 `TradingAgents` 或 `ai-hedge-fund` 的多角色分工，并加入样本外回测与过拟合检测。
5. **原型：本地优先金融数据 Agent**：结合 `atomic-agent` 或 `colibri` 的本地推理能力，构建不依赖云 API 的金融数据分析 Agent。
6. **调研：MCP 金融工具生态**：梳理 `awesome-mcp-servers` 中与行情、交易、风控相关的 MCP server，评估标准化接入可行性。
7. **Demo：Agent 生成交易看板**：利用 `open-design` 或 `ui-ux-pro-max-skill`，让 Agent 自动生成实时行情仪表盘与风控看板。
8. **原型：交易 Agent 操作审计沙箱**：参考 `OpenBot` 的“每个 Agent 独立计算机环境”思路，为交易 Agent 构建可回放、可审计的操作沙箱。
9. **调研：金融基础模型能力边界**：研究 `Kronos` 的模型架构与训练数据，评估金融时序基础模型在预测、异常检测上的实用性。
10. **Watchlist：`QuantDinger`**：关注其多租户交易 SaaS 架构演进，尤其是计费、结算与多交易所接入模块。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| iFixAi | AI Agent 审计与治理爆发式增长，金融 Agent 合规刚需 |
| TradingAgents | LLM 多智能体交易代表项目，持续活跃 |
| Vibe-Trading | 自然语言交易 Agent 与 MCP 集成，HKUDS 出品 |
| QuantDinger | AI 交易 OS 与多租户 SaaS 产品化架构 |
| tick-stock-panel | 轻量 A 股量化工作台，技术栈现代，适合复刻 |
| Kronos | 金融基础模型方向，需观察后续维护与能力验证 |
| headroom | LLM 上下文压缩，对金融 token 密集场景价值高 |
| Financial-API | 同花顺官方 A 股数据服务，MCP 支持，基础设施价值 |
| OpenBB | 多资产金融数据平台，AI Agent 数据接入参考 |
| ai-hedge-fund | 多智能体投研经典项目，关注其后续演进 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **基线数据**：本次报告使用 `baseline_1d: 2026-10-04.json` 与 `baseline_7d: 2026-09-28.json`，1 日与 7 日涨星数据总体可用。
- **缺失数据**：`OpenBB` 的 `star_delta_7d` 为 null，7 日涨星信息不足；所有项目的 `star_delta_30d` 均为 null，30 日涨星无法评估。
- **采集失败**：未发现明确采集失败标记，但 `OpenBB` 7 日基线缺失可能由基线文件未覆盖导致。
- **样本偏差**：候选列表由关键词匹配生成，包含大量 `awesome-*` 列表类项目（如 `public-apis`、`awesome-selfhosted`、`awesome-python`、`awesome-go` 等），它们因描述或 README 命中金融/交易关键词而进入榜单，并非直接交易系统。分析时需区分“资源列表”与“实际交易/量化项目”。此外，`category_guess` 与 `risk_flags` 为自动推断，可能存在误分类。
