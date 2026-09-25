# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-24

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 交易框架**：TradingAgents、Vibe-Trading、QuantDinger、PanWatch 等项目持续高增长，多 Agent 决策、LLM 驱动选股/盯盘成为明确热点。
  2. **AI 设计/UI 生成与 Agent 技能生态**：ui-ux-pro-max-skill、open-design、awesome-design-md 等以“让 coding agent 生成专业 UI/设计系统”为核心的项目涨星极快，说明 Agent 工具链正在从“写代码”扩展到“产品化交付”。
  3. **本地/边缘模型推理与微调**：colibri、needle、magnitude、Soup、unsloth 等项目聚焦“在自有硬件上跑前沿模型、低显存微调”，为金融场景的私有化 AI 能力提供基础设施灵感。

- **是否出现新趋势**：出现。围绕 **Jev / System One 类型化决策模型** 的生态项目（jev-trader、awesome-jev、awesome-jev-projects、awesome-jev-gallery）在极短时间内集中出现，形成一个小型但快速增长的“类型安全 AI 决策”生态，值得观察其是否从概念走向可复用工程框架。

- **是否出现值得复刻/参考的工程架构**：是。OpenStock 的实时行情 + 个性化提醒 + 公司洞察架构；PanWatch 的“自托管 AI 盯盘 + TradingAgents 多 Agent 决策 + 全渠道推送”；QuantDinger 的“研究/回测/模拟/实盘 + 多租户交易 SaaS”一体化设计；hyperswitch 的 Rust 支付编排与智能路由，均有较高参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明确骗局项目，但存在大量 **awesome-list / 资源聚合类项目** 因关键词误匹配进入榜单，实际与金融/量化交易无关。部分项目描述带有明显营销语气（如“forever free”“immense model”），需以代码和架构为准。所有 crypto、trading bot 类项目默认按高风险处理。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OpenStock | 19181 | +247 | +3568 | TypeScript | 行情/自托管 | 开源实时行情、提醒与公司洞察平台 | 高 | 低 |
| 2 | ui-ux-pro-max-skill | 130461 | +263 | +1588 | Python | AI 设计技能 | 为 coding agent 提供跨平台 UI/UX 设计智能 | 高 | 低 |
| 3 | public-apis | 482967 | +362 | +1498 | Python | API 聚合 | 免费 API 集合列表 | 中 | 中 |
| 4 | awesome-selfhosted | 321583 | +234 | +1369 | 无 | 自托管列表 | 可自托管网络服务列表 | 中 | 中 |
| 5 | colibri | 37569 | +189 | +1368 | C | 本地推理 | 纯 C、零依赖的 MoE 模型本地推理引擎 | 高 | 低 |
| 6 | jev-trader | 2375 | +163 | +1448 | TypeScript | AI 交易 | 每个 Monad 区块产生一次 AI 交易决策 | 高 | 低 |
| 7 | awesome-python | 322829 | +212 | +1234 | Python | Python 资源 | Python 工具精选列表 | 低 | 低 |
| 8 | awesome-design-md | 117784 | +212 | +1203 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 文件集合 | 中 | 中 |
| 9 | build-your-own-x | 549384 | +260 | +1269 | Markdown | 教程列表 | 从零复刻技术的教程集合 | 中 | 中 |
| 10 | needle | 12554 | +111 | +1192 | Python | 边缘 AI | 面向微型设备的自动化基础模型 | 高 | 中 |
| 11 | open-design | 98002 | +141 | +1031 | TypeScript | AI 设计 | 本地优先的 AI 设计引擎 | 高 | 低 |
| 12 | TradingAgents | 108510 | +161 | +1000 | Python | 多 Agent 交易 | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 13 | awesome-go | 185467 | +132 | +763 | Go | Go 资源 | Go 框架与库精选列表 | 低 | 中 |
| 14 | headroom | 73742 | +78 | +765 | Python | Token 压缩 | 压缩工具输出、日志、RAG 块以降低 token 消耗 | 高 | 低 |
| 15 | PanWatch | 1777 | +163 | +852 | Python | AI 盯盘 | 自托管 AI 盯盘助手，集成 TradingAgents | 高 | 中 |
| 16 | free-for-dev | 138335 | +236 | +584 | HTML | 免费资源 | 开发者免费 SaaS/PaaS/IaaS 列表 | 低 | 低 |
| 17 | career-ops | 72639 | +88 | +554 | JavaScript | AI 求职 | 开源 AI 求职扫描与简历定制工具 | 低 | 低 |
| 18 | awesome-dsh-plugin | 16845 | +77 | +635 | JavaScript | 插件列表 | DeepSeek Harness 插件精选列表 | 低 | 低 |
| 19 | hyperswitch | 43936 | +99 | +320 | Rust | 支付编排 | 开源可组合支付平台 | 高 | 低 |
| 20 | Vibe-Trading | 33996 | +82 | +331 | Python | AI 交易 | 个人交易 Agent 框架 | 高 | 中 |
| 21 | ruflo | 73228 | +65 | +418 | TypeScript | Agent 框架 | 多玩家 swarm 与自主工作流 Agent 框架 | 高 | 低 |
| 22 | daily_stock_analysis | 65616 | +69 | +351 | Python | 股票分析 | LLM 驱动多市场股票智能分析系统 | 高 | 低 |
| 23 | magnitude | 5045 | +87 | +397 | TypeScript | 本地推理 | 硬件画像与本地模型推荐/调优引擎 | 中 | 低 |
| 24 | unsloth | 76728 | +64 | +326 | Python | 模型微调 | 本地 LLM/扩散模型训练与运行 UI | 中 | 低 |
| 25 | Soup | 7149 | +80 | +328 | Python | 模型微调 | 一个 YAML 完成 LLM 微调，低显存训练 | 中 | 低 |
| 26 | QuantDinger | 12130 | +51 | +410 | Python | AI 交易 OS | 开源 AI 交易 OS，支持多租户交易 SaaS | 高 | 中 |
| 27 | OpenBot | 5529 | +53 | +388 | TypeScript | Agent 自动化 | 每个 AI coworker 拥有独立浏览器/文件/工具 | 高 | 中 |
| 28 | tick-stock-panel | 5014 | +75 | +212 | Python | A 股量化 | 自托管 A 股选股/监控/回测工作台 | 高 | 低 |
| 29 | awesome-jev-projects | 505 | +47 | +459 | JavaScript | Jev 生态 | Jev 开源生态雷达与项目发现 | 中 | 低 |
| 30 | ai-hedge-fund | 63745 | +46 | +245 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 31 | prompt-master | 13637 | +51 | +284 | 无 | Prompt 技能 | 为任意 AI 工具生成准确 prompt 的 Claude skill | 中 | 低 |
| 32 | oh-my-openagent | 69389 | +41 | +191 | TypeScript | Agent 编排 | 图工程与 Agent 编排工具 | 中 | 低 |
| 33 | awesome-mcp-servers | 95498 | +26 | +255 | 无 | MCP 列表 | MCP server 集合 | 中 | 低 |
| 34 | awesome-jev | 1634 | +104 | 信息不足 | Python | Jev 生态 | Jev 公共项目与集成列表 | 中 | 中 |
| 35 | OpenBB | 73447 | +26 | +227 | Python | 数据平台 | 面向分析师、量化与 AI Agent 的开放数据平台 | 高 | 中 |
| 36 | gbrain | 30311 | +30 | +192 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | 中 | 低 |
| 37 | kvmem-llama.cpp | 602 | +42 | +385 | C++ | 本地推理 | llama.cpp 的 KV 内存优化变体 | 中 | 低 |
| 38 | skill | 7185 | +28 | +250 | Python | 技能商店 | AI Agent 技能商店与聚合 | 中 | 低 |
| 39 | awesome-public-datasets | 79149 | +21 | +119 | 无 | 数据集列表 | 高质量开放数据集列表 | 中 | 中 |
| 40 | awesome-cpp | 73454 | +15 | +105 | 无 | C++ 资源 | C/C++ 框架与库精选列表 | 低 | 低 |
| 41 | system-design-101 | 89916 | +44 | +536 | 无 | 系统设计 | 用可视化解释复杂系统 | 中 | 低 |
| 42 | awesome-machine-learning | 74443 | +15 | +74 | Python | ML 资源 | 机器学习框架与库精选列表 | 低 | 低 |
| 43 | awesome-jev-gallery | 338 | +74 | 信息不足 | JavaScript | Jev 论文 | System One/Jev 论文与复现集合 | 中 | 低 |
| 44 | cs-video-courses | 83554 | +5 | +18 | 无 | 课程列表 | 计算机科学视频课程列表 | 低 | 中 |
| 45 | awesome-vue | 73544 | -1 | -4 | 无 | Vue 资源 | Vue.js 精选资源列表 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 OpenStock
- **解决什么问题**：替代昂贵的市场行情平台，提供实时价格、个性化提醒和公司洞察，且开源免费。
- **为什么值得关注**：24h +247、7d +3568，是本次候选集中金融产品类涨星最猛的项目之一；AGPL-3.0 协议，TypeScript/Next.js 技术栈，活跃 push。
- **技术栈/架构亮点**：Next.js + shadcn-ui + TailwindCSS + Inngest，说明采用现代 Web 全栈 + 事件驱动/后台任务架构；coderabbit 出现在 topics 中，可能用于自动化代码审查。
- **是否适合借鉴**：非常适合。可作为“自托管行情终端 + 提醒引擎”的 MVP 参考，尤其适合想构建内部投研看板或轻量级市场监控产品的团队。
- **可能风险**：AGPL-3.0 传染性协议，商用需注意；实时行情数据源授权与稳定性未在 JSON 中体现，需自行核实。

### 3.2 TradingAgents
- **解决什么问题**：用多 Agent LLM 框架模拟金融交易决策流程。
- **为什么值得关注**：108k stars，7d +1000，Apache-2.0，Python，近 30 天有 push；是 AI 交易领域最成熟的参考框架之一。
- **技术栈/架构亮点**：多 Agent 协作，topics 包含 agent、finance、llm、multiagent、trading；被 PanWatch 等项目直接集成，说明其架构具备一定可复用性。
- **是否适合借鉴**：适合。可作为企业级“多角色投研 Agent 协作”的架构蓝本，重点借鉴其 Agent 角色划分、决策流程编排和 LLM 调用抽象。
- **可能风险**：标记为 likely_research_tool，说明定位偏研究而非生产交易；策略过拟合、回测偏差、LLM 输出不稳定是主要风险；不应直接用于实盘。

### 3.3 PanWatch
- **解决什么问题**：自托管 AI 盯盘助手，覆盖 A 股/港股/美股实时监控、持仓管理、智能分析和全渠道推送。
- **为什么值得关注**：24h +163、7d +852，虽然总 star 仅 1777，但增速极快；MIT 协议，Python，近 30 天有 push。
- **技术栈/架构亮点**：集成 TradingAgents 多 Agent 决策，使用 akshare 数据源、FastAPI、LangGraph、MCP、PWA，支持 DeepSeek/OpenAI；自托管 + 全渠道推送设计完整。
- **是否适合借鉴**：非常适合。是“AI 盯盘 + 多 Agent 决策 + 自托管 + 推送”组合的典型 MVP，可直接参考其模块划分和 MCP 集成方式。
- **可能风险**：trading_bot 标记，存在自动交易相关风险；A 股数据源合规性、API key 安全、策略有效性均需谨慎；不建议直接输入真实券商/交易所凭证。

### 3.4 QuantDinger
- **解决什么问题**：开源 AI 交易 OS，覆盖研究、策略编写、回测、模拟/实盘交易，并支持多租户交易 SaaS。
- **为什么值得关注**：12k stars，7d +410，Apache-2.0，Python；描述中明确提到“agent trading”“vibe trading”“Jev System One integration”。
- **技术栈/架构亮点**：集成 Alpaca、Binance、MCP server，支持 crypto、股票、外汇；内置用户管理、计费、支付和结算，说明其架构目标是“可商业化的交易平台底座”。
- **是否适合借鉴**：适合。其“研究-回测-模拟-实盘”全链路 + 多租户 SaaS 设计，对想构建交易平台或内部量化工作台的团队有直接参考价值。
- **可能风险**：crypto_related、likely_research_tool 标记；多市场、多资产、多租户架构复杂度高；实盘交易、杠杆、API key 管理风险显著；不建议直接运行。

### 3.5 Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，提供 AI 驱动的交易决策框架。
- **为什么值得关注**：34k stars，HKUDS 出品，MIT 协议，Python；topics 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent。
- **技术栈/架构亮点**：多 Agent + MCP + 回测集成，学术机构背景使其在方法设计上可能更规范。
- **是否适合借鉴**：适合。可作为“个人 AI 交易 Agent”的研究原型参考，重点借鉴其回测与 Agent 决策的耦合方式。
- **可能风险**：crypto_related、likely_research_tool；策略过拟合、回测幸存者偏差、实盘滑点/流动性问题；不应将 star 视为策略有效信号。

### 3.6 ai-hedge-fund
- **解决什么问题**：模拟一个 AI 对冲基金团队，用多个 Agent 扮演不同角色进行投资决策。
- **为什么值得关注**：63k stars，MIT，Python，持续活跃；是 AI 金融决策模拟的经典项目。
- **技术栈/架构亮点**：多角色 Agent 协作，强调研究/决策流程模拟而非真实交易执行。
- **是否适合借鉴**：适合。可作为“AI 投研团队模拟”的教学和原型参考，适合用于理解多 Agent 决策流程。
- **可能风险**：likely_research_tool；模拟结果不代表真实收益；回测偏差和过拟合风险高。

### 3.7 hyperswitch
- **解决什么问题**：开源可组合支付平台，支持多支付/付款/欺诈/金库/令牌化提供商连接，提供智能路由、成本可观测性和对账。
- **为什么值得关注**：43k stars，Rust，Apache-2.0，juspay 出品；是本次候选集中少有的企业级金融基础设施项目。
- **技术栈/架构亮点**：Rust 高性能、PCI 合规、支付编排、智能路由、收入恢复、成本可观测性、对账；架构设计成熟。
- **是否适合借鉴**：非常适合。对构建金融交易系统的团队，其支付编排、路由、对账和风控模块设计具有直接参考价值。
- **可能风险**：金融合规要求高；项目复杂度高，open_issues 2222，维护成本大；与量化交易无直接关系，但可作为金融基础设施参考。

### 3.8 OpenBB
- **解决什么问题**：面向分析师、量化研究员和 AI Agent 的开放数据平台。
- **为什么值得关注**：73k stars，Python，持续活跃；topics 覆盖 crypto、derivatives、equity、fixed-income、options、quantitative-finance。
- **技术栈/架构亮点**：统一数据访问层，覆盖多资产类别，支持 AI Agent 使用。
- **是否适合借鉴**：适合。可作为量化研究数据层的基础设施参考，尤其适合需要统一多源金融数据的团队。
- **可能风险**：crypto_related 标记；数据源授权和合规需自行核实；license 为 Other，商用需注意。

### 3.9 jev-trader
- **解决什么问题**：每个 Monad 区块产生一次 AI 交易决策，针对 Kuru MON-USDC 交易对。
- **为什么值得关注**：24h +163、7d +1448，虽然总 star 仅 2375，但增速极快；TypeScript，MIT。
- **技术栈/架构亮点**：将 AI 决策与区块级事件绑定，体现“类型化决策 + 高频触发”的设计思路；与 Jev/System One 生态相关。
- **是否适合借鉴**：适合作为“AI 决策与链上事件结合”的原型参考，但需谨慎评估其策略有效性。
- **可能风险**：crypto 交易、区块级自动决策，风险极高；不建议直接运行或输入真实 API key。

### 3.10 colibri
- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，纯 C、零依赖，专家从磁盘流式加载。
- **为什么值得关注**：37k stars，7d +1368，Apache-2.0，C 语言；体现“小引擎跑大模型”的工程趋势。
- **技术栈/架构亮点**：纯 C、零依赖、专家流式加载，架构极简但性能导向。
- **是否适合借鉴**：适合。对金融场景中“私有化部署大模型、降低推理成本”有直接启发，尤其适合资源受限环境。
- **可能风险**：与量化交易无直接关系；作为底层推理引擎，需自行评估模型精度和推理性能。

## 4. 趋势归纳

- **技术趋势**：
  - **本地/边缘模型推理与微调**成为热点：colibri、needle、magnitude、Soup、unsloth、kvmem-llama.cpp 等项目集中出现，反映“在自有硬件上跑模型、降低 token 成本、保护数据隐私”的强烈需求。
  - **Token 压缩与上下文工程**：headroom 等项目专注于在 LLM 调用前压缩工具输出、日志和 RAG 块，说明 Agent 场景下的成本优化正在成为独立技术方向。
  - **类型化 AI 决策模型**：Jev/System One 生态项目集中出现，强调 calibrated probabilities、typed decisions、structured outputs，可能代表“从自由文本输出到可验证结构化决策”的演进。

- **产品趋势**：
  - **AI 设计/UI 生成**：ui-ux-pro-max-skill、open-design、awesome-design-md 等项目涨星极快，说明“让 coding agent 直接生成专业 UI/设计系统”正在成为产品化交付的关键能力。
  - **自托管 AI 盯盘/分析助手**：PanWatch、daily_stock_analysis、tick-stock-panel 等项目表明，面向 A 股/多市场的自托管 AI 分析工具需求旺盛。
  - **一体化交易 OS**：QuantDinger 等试图将研究、回测、模拟、实盘、多租户 SaaS 整合到一个平台。

- **量化/交易策略趋势**：
  - **多 Agent LLM 决策框架**持续演进：TradingAgents、Vibe-Trading、ai-hedge-fund 等项目表明，多角色 Agent 协作已成为 AI 交易研究的主流范式。
  - **AI 决策与高频/区块级事件结合**：jev-trader 将 AI 决策绑定到区块事件，显示 AI 交易正在向更高频、更自动化的方向探索。
  - **回测与模拟仍是核心**：多数项目强调 backtesting，但需警惕过拟合和幸存者偏差。

- **AI Agent 与自动化交易结合趋势**：
  - **MCP 成为标准集成方式**：PanWatch、Vibe-Trading、QuantDinger、OpenBot 等项目均涉及 MCP，说明 MCP 正在成为 Agent 与数据/交易工具连接的事实标准。
  - **Agent 治理与可观测性**：OpenBot 强调“每个动作在发生前决定、发生后记录”，反映 Agent 自动化场景对审计和治理的需求。
  - **多租户交易 SaaS**：QuantDinger 的定位显示，AI 交易能力正在被产品化为可商业化的 SaaS 服务。

- **值得后续做原型验证的方向**：
  - 自托管 AI 投研看板 + 多 Agent 决策 + MCP 数据接入。
  - 本地模型推理 + Token 压缩，构建低成本私有化金融 Agent。
  - 类型化决策模型在风控规则引擎中的应用。
  - 支付编排/智能路由架构在交易系统资金链路中的借鉴。

## 5. 今日灵感清单

1. **MVP：自托管 AI 盯盘助手**：参考 PanWatch，用 FastAPI + LangGraph + MCP 构建一个最小化“行情监控 + 多 Agent 分析 + 推送”系统，先接一个数据源和一个 LLM。
2. **MVP：AI 投研决策看板**：参考 OpenStock + TradingAgents，构建一个实时行情 + 公司洞察 + 多角色 Agent 决策的 Web 看板，重点验证 Agent 角色划分和决策流程。
3. **调研：Token 压缩与上下文工程**：深入研究 headroom 的压缩策略，评估在金融数据密集场景下降低 LLM 调用成本的效果。
4. **调研：本地模型推理引擎**：评估 colibri、magnitude、needle 在金融文本分析、结构化提取任务上的性能与部署成本。
5. **Codex/Agent 自动复现 demo**：让 Codex 复现 ai-hedge-fund 的多 Agent 决策流程，替换为本地模型，验证私有化部署可行性。
6. **原型：类型化决策风控引擎**：参考 Jev/System One 的 typed decisions 思路，设计一个输出结构化、可校准概率的风控规则引擎。
7. **原型：支付编排/智能路由**：参考 hyperswitch，设计一个交易系统资金链路的支付编排与对账模块，重点借鉴其路由和成本可观测性设计。
8. **加入 watchlist**：OpenStock、TradingAgents、PanWatch、QuantDinger、Vibe-Trading、ai-hedge-fund、hyperswitch、OpenBB、headroom、colibri。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| OpenStock | 金融产品类涨星最猛，自托管行情终端架构值得持续跟踪 |
| TradingAgents | AI 多 Agent 交易框架的成熟参考，生态集成度高 |
| PanWatch | 增速极快，自托管 AI 盯盘 + 多 Agent 决策的典型 MVP |
| QuantDinger | 一体化 AI 交易 OS + 多租户 SaaS 架构，商业化潜力高 |
| Vibe-Trading | 学术背景的 AI 交易 Agent 框架，方法设计值得关注 |
| ai-hedge-fund | AI 投研团队模拟的经典项目，适合教学和原型验证 |
| hyperswitch | 企业级支付编排基础设施，金融系统架构参考价值高 |
| OpenBB | 统一金融数据平台，适合作为量化数据层基础设施 |
| headroom | Token 压缩方向代表项目，Agent 成本优化关键 |
| colibri | 本地 MoE 推理引擎，私有化 AI 部署的潜力项目 |
| jev-trader | 类型化 AI 决策与区块级事件结合的新兴方向，值得观察 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-09-23）和 `baseline_7d`（2026-09-18），基线完整。
- **采集失败**：JSON 中未提供明确的采集失败信息；但部分项目 `star_delta_7d` 为 null（如 awesome-jev、awesome-jev-gallery），可能因项目创建时间晚于 7 日基线或基线数据缺失，表中已标注“信息不足”。
- **样本偏差**：本次候选集存在明显的 **关键词误匹配偏差**。大量 awesome-list、资源聚合、AI 设计、模型推理类项目因描述或 readme 中命中“quant”“fintech”“trading bot”等关键词而进入榜单，实际与金融/量化交易无直接关系。分析时需结合项目实际内容判断，不应仅依据 matched_queries 或 category_guess 进行分类。
- **风险等级说明**：JSON 中的 `risk_level` 为候选生成阶段的初步判断，本报告在深度分析中已结合项目性质进行二次评估；所有 crypto、trading bot 类项目默认按高风险处理。
