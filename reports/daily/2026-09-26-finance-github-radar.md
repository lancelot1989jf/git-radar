# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-26

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 与交易决策融合**：TradingAgents、Vibe-Trading、PanWatch、QuantDinger 等项目持续高速涨星，多 Agent LLM 交易框架正在从研究原型走向可自托管产品形态。
  2. **A 股量化数据与工作台生态爆发**：tick-stock-panel、a-stock-data、vibe-astock、daily_stock_analysis 等中文项目密集出现，围绕 A 股数据获取、选股、监控、回测和 LLM 复盘形成完整工具链。
  3. **AI 驱动的 UI/设计工程化**：ui-ux-pro-max-skill、open-design、awesome-design-md 等项目涨星极快，反映 coding agent 生态正在向"设计智能"延伸，对金融终端、交易看板的产品化有直接借鉴价值。

- **是否出现新趋势**：出现。Jev/System One 生态（jev-trader、awesome-jev、awesome-jev-projects）作为"类型化决策模型"的新概念在 7 日内快速冒头，虽然总量尚小，但增长斜率陡峭，值得观察其是否从概念炒作走向可验证的工程框架。

- **是否出现值得复刻/参考的工程架构**：是。OpenStock 的实时行情 + 个性化告警 + 公司洞察的 TypeScript/Next.js 架构；hyperswitch 的 Rust 支付编排与智能路由；tick-stock-panel 的 DuckDB + Polars + FastAPI 本地量化工作台；headroom 的 LLM token 压缩代理层，均可作为工程参考。

- **是否有明显骗局、过度营销或高风险项目**：本批数据中未发现明确骗局，但需警惕：
  - `Financial_freedom`（"最全赚钱投资指南"）24h 涨星 +205 但 7d 仅 +270，且无 license、无 topics，内容性质接近营销/投资指南，信息价值存疑。
  - 多个项目描述中出现 "vibe trading"、"AI Trading OS" 等营销化措辞，需区分工程实质与概念包装。
  - `awesome-selfhosted`、`build-your-own-x`、`public-apis` 等大型 awesome 列表因关键词误匹配进入候选，并非真正的交易项目，分析时需剔除噪音。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OpenStock | 19324 | +66 | +3106 | TypeScript | 行情终端 | 开源实时行情、告警与公司洞察平台 | 高 | 低 |
| 2 | public-apis | 483627 | +323 | +1950 | Python | API 列表 | 免费 API 集合，含金融数据源 | 中 | 中 |
| 3 | ui-ux-pro-max-skill | 130884 | +193 | +1765 | Python | AI 设计技能 | 为 coding agent 提供 UI/UX 设计智能 | 高 | 低 |
| 4 | awesome-selfhosted | 322075 | +252 | +1640 | — | 自托管列表 | 自托管服务列表，关键词误匹配 | 低 | 中 |
| 5 | awesome-python | 323371 | +316 | +1582 | Python | Python 列表 | Python 工具精选，关键词误匹配 | 低 | 低 |
| 6 | build-your-own-x | 549955 | +317 | +1665 | Markdown | 教程列表 | 从零构建技术教程，关键词误匹配 | 低 | 中 |
| 7 | awesome-design-md | 118198 | +228 | +1480 | — | 设计系统 | DESIGN.md 品牌设计系统集合 | 中 | 中 |
| 8 | colibri | 37807 | +132 | +1361 | C | 推理引擎 | 纯 C 零依赖 MoE 模型本地推理 | 中 | 低 |
| 9 | TradingAgents | 108808 | +151 | +1159 | Python | AI 交易 | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 10 | open-design | 98229 | +113 | +1097 | TypeScript | AI 设计 | 本地优先的 AI 设计引擎 | 中 | 低 |
| 11 | jev-trader | 2518 | +90 | +1174 | TypeScript | AI 交易 | 每区块一个 AI 交易决策 | 中 | 低 |
| 12 | awesome-go | 185774 | +154 | +951 | Go | Go 列表 | Go 框架精选，关键词误匹配 | 低 | 中 |
| 13 | free-for-dev | 138658 | +117 | +853 | HTML | 免费资源 | 开发者免费资源列表，误匹配 | 低 | 低 |
| 14 | needle | 12726 | +83 | +1051 | Python | 边缘 AI | 微型设备自动化基础模型 | 中 | 中 |
| 15 | hyperswitch | 44412 | +317 | +796 | Rust | 支付平台 | 开源可组合支付编排平台 | 高 | 低 |
| 16 | headroom | 73898 | +73 | +767 | Python | LLM 压缩 | 压缩 LLM 输入 token 的代理/MCP | 高 | 低 |
| 17 | awesome-dsh-plugin | 16996 | +84 | +685 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | 低 | 低 |
| 18 | career-ops | 72883 | +53 | +697 | JavaScript | AI 求职 | AI 求职代理，误匹配 | 低 | 低 |
| 19 | Soup | 7335 | +124 | +447 | Python | LLM 微调 | 单 YAML 低显存微调 LLM | 中 | 低 |
| 20 | oh-my-openagent | 69518 | +90 | +313 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中 | 低 |
| 21 | magnitude | 5189 | +67 | +480 | TypeScript | 推理引擎 | 硬件自适应开源推理引擎 | 中 | 低 |
| 22 | tick-stock-panel | 5248 | +72 | +431 | Python | A 股量化 | 自托管 A 股选股+监控+回测工作台 | 高 | 低 |
| 23 | ruflo | 73339 | +48 | +464 | TypeScript | Agent 框架 | 多智能体 swarm 编排框架 | 中 | 低 |
| 24 | PanWatch | 1816 | +17 | +787 | Python | AI 盯盘 | 自托管 AI 盯盘助手，集成 TradingAgents | 高 | 中 |
| 25 | unsloth | 76841 | +45 | +386 | Python | LLM 微调 | 本地 LLM 训练与微调 UI | 中 | 低 |
| 26 | Vibe-Trading | 34090 | +42 | +389 | Python | AI 交易 | 个人交易 Agent 框架 | 高 | 中 |
| 27 | OpenBot | 5612 | +45 | +426 | TypeScript | Agent 自动化 | 给 AI coworker 独立电脑环境 | 中 | 中 |
| 28 | daily_stock_analysis | 65688 | +34 | +352 | Python | 股票分析 | LLM 多市场股票智能分析系统 | 高 | 低 |
| 29 | QuantDinger | 12211 | +29 | +453 | Python | AI 交易 OS | 开源 AI 交易 OS，多租户 SaaS | 中 | 中 |
| 30 | Financial_freedom | 4194 | +205 | +270 | — | 投资指南 | 赚钱投资指南，营销性质 | 低 | 中 |
| 31 | awesome-mcp-servers | 95560 | +27 | +260 | — | MCP 列表 | MCP 服务器集合 | 中 | 低 |
| 32 | awesome-jev-projects | 563 | +28 | +434 | JavaScript | Jev 生态 | Jev 开源生态雷达 | 低 | 低 |
| 33 | OpenBB | 73491 | +23 | +219 | Python | 金融数据 | 分析师/量化/AI Agent 开放数据平台 | 高 | 中 |
| 34 | awesome-jev | 1773 | +83 | — | Python | Jev 列表 | Jev 类型化决策项目列表 | 低 | 中 |
| 35 | gbrain | 30354 | +17 | +200 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 36 | system-design-101 | 90023 | +57 | +588 | — | 系统设计 | 系统设计图解，误匹配 | 低 | 低 |
| 37 | ai-hedge-fund | 63765 | +15 | +201 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 38 | prompt-master | 13688 | +18 | +297 | — | Prompt 技能 | 精准 prompt 编写技能 | 低 | 低 |
| 39 | a-stock-data | 10374 | +38 | +409 | Python | A 股数据 | A 股全栈数据工具包，15 层 87 端点 | 高 | 中 |
| 40 | skill | 7240 | +17 | +265 | Python | 技能商店 | AI Agent 技能商店 | 低 | 低 |
| 41 | awesome-cpp | 73490 | +14 | +127 | — | C++ 列表 | C++ 框架精选，误匹配 | 低 | 低 |
| 42 | awesome-public-datasets | 79169 | +10 | +123 | — | 数据集 | 公开数据集列表，误匹配 | 低 | 中 |
| 43 | awesome-machine-learning | 74465 | +12 | +88 | Python | ML 列表 | ML 框架精选，误匹配 | 低 | 低 |
| 44 | vibe-astock | 553 | +69 | — | Python | A 股复盘 | A 股短线复盘看板，本地计算情绪指标 | 高 | 低 |
| 45 | cs-video-courses | 83564 | +3 | +21 | — | 课程列表 | CS 视频课程，误匹配 | 低 | 中 |
| 46 | awesome-vue | 73542 | -2 | -5 | — | Vue 列表 | Vue 资源精选，误匹配 | 低 | 低 |
| 47 | awesome-sre | 13621 | +68 | +94 | — | SRE 列表 | SRE 资源精选，误匹配 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 OpenStock（Open-Dev-Society/OpenStock）

- **解决什么问题**：提供昂贵的市场数据平台的免费开源替代，覆盖实时价格、个性化告警和公司洞察。
- **为什么值得关注**：7 日涨星 +3106，是本期金融方向涨星最猛的项目；AGPL-3.0 协议，TypeScript/Next.js 技术栈，活跃度极高（近 30 天有 push）。
- **技术栈/架构亮点**：Next.js + TailwindCSS + shadcn-ui 构建前端，inngest 做事件驱动后台任务，coderabbit 做代码审查。架构上适合作为实时行情终端的产品化参考。
- **是否适合借鉴**：非常适合。实时行情推送、告警系统、公司基本面数据聚合的产品形态可直接迁移到 AI 交易看板或投研工作台。
- **可能风险**：AGPL-3.0 协议对商业闭源集成有限制；数据源合规性和稳定性需自行验证。

### 3.2 TradingAgents（TauricResearch/TradingAgents）

- **解决什么问题**：用多 Agent LLM 框架模拟金融交易团队的分工决策流程。
- **为什么值得关注**：108k stars，7 日 +1159，是 AI 交易方向最成熟的研究型框架之一；Apache-2.0 协议，学术机构背景（TauricResearch）。
- **技术栈/架构亮点**：Python 多 Agent 架构，将分析师、研究员、交易员、风控等角色拆分为独立 LLM Agent，通过协作完成交易决策。topics 明确标注 agent、finance、llm、multiagent、trading。
- **是否适合借鉴**：适合。多 Agent 角色分工 + 辩论/协作机制可直接迁移到企业级投研 Agent 框架；其风控 Agent 的设计思路值得单独研究。
- **可能风险**：研究工具属性强，实盘可靠性未经验证；LLM 决策存在幻觉和过拟合风险；不应直接用于真实资金交易。

### 3.3 tick-stock-panel（shy3130/tick-stock-panel）

- **解决什么问题**：A 股"选股 + 监控 + 回测"一体化自托管量化工作台，强调零运维和 LLM 驱动的策略定制与个股分析。
- **为什么值得关注**：2026 年 6 月创建，5.2k stars，7 日 +431，增长稳健；MIT 协议，个人开源项目但工程完整度高。
- **技术栈/架构亮点**：DuckDB + Polars + FastAPI + React 的组合非常现代——DuckDB 做本地分析型存储，Polars 做高性能数据处理，FastAPI 提供 API 层，LLM 负责策略生成和复盘。支持第三方数据源自由接入。
- **是否适合借鉴**：非常适合。DuckDB + Polars 的本地量化数据栈是轻量级、低成本、可复现的工程范式，值得在 AI 交易数据工程中原型验证。
- **可能风险**：A 股数据源合规性；LLM 生成策略的过拟合风险；个人项目长期维护不确定性。

### 3.4 hyperswitch（juspay/hyperswitch）

- **解决什么问题**：开源可组合支付编排平台，连接多个支付、风控、金库和 tokenization 提供商，通过智能路由和收入恢复提升授权率。
- **为什么值得关注**：44k stars，24h 涨星 +317（本期单日涨星最高之一），Rust 编写，Apache-2.0，是金融基础设施方向的高质量工程样本。
- **技术栈/架构亮点**：Rust 保证高性能和内存安全；PCI 合规；支付编排、智能路由、成本可观测性、对账自动化等模块化设计。对金融交易系统的可靠性工程有直接参考价值。
- **是否适合借鉴**：适合。支付编排的智能路由和降级策略可类比到交易执行路由；其对账和成本可观测性设计可迁移到交易系统的资金管理模块。
- **可能风险**：与交易系统无直接关系，借鉴需抽象；Rust 学习曲线陡峭。

### 3.5 headroom（headroomlabs-ai/headroom）

- **解决什么问题**：在 LLM 输入前压缩工具输出、日志、文件和 RAG 块，减少 token 消耗（coding agent 省 20%，JSON 省 60-95%）。
- **为什么值得关注**：73.9k stars，7 日 +767；解决的是 AI Agent 规模化落地的核心成本问题，对金融 AI Agent 高频调用场景尤其相关。
- **技术栈/架构亮点**：提供 library、proxy、MCP server 三种形态，Python + TypeScript 双语言，FastAPI 集成。上下文工程（context engineering）思路清晰。
- **是否适合借鉴**：非常适合。金融 AI Agent 需要处理大量行情数据、新闻、研报，token 压缩层可直接降低推理成本；MCP server 形态可无缝接入现有 Agent 框架。
- **可能风险**：压缩可能损失关键信息，金融场景需验证压缩后决策质量不下降。

### 3.6 PanWatch（TNT-Likely/PanWatch）

- **解决什么问题**：自托管 AI 盯盘助手，集成 TradingAgents 多 Agent 投资决策，覆盖 A 股/港股/美股实时监控、持仓管理和全渠道推送。
- **为什么值得关注**：1.8k stars，7 日 +787（增速远超其体量），是 TradingAgents 从研究框架走向产品化应用的典型案例。
- **技术栈/架构亮点**：Python + FastAPI + LangGraph + MCP + PWA，集成 akshare 数据源和 DeepSeek/OpenAI 模型。将多 Agent 决策与实时监控、推送通知结合。
- **是否适合借鉴**：适合。展示了如何把研究型 Agent 框架包装成可自托管的盯盘产品；MCP 集成模式值得参考。
- **可能风险**：trading_bot 标记，存在实盘误用风险；依赖 TradingAgents 上游框架的稳定性；A 股数据源合规性。

### 3.7 Vibe-Trading（HKUDS/Vibe-Trading）

- **解决什么问题**：定位为"个人交易 Agent"，将 LLM 多 Agent 框架应用于交易决策。
- **为什么值得关注**：34k stars，HKUDS（香港大学数据科学实验室）背景，MIT 协议；与 TradingAgents 形成学术派 AI 交易框架的竞争格局。
- **技术栈/架构亮点**：Python + MCP + multi-agent，topics 覆盖 algorithmic-trading、backtesting、fintech、quantitative-finance。强调回测能力。
- **是否适合借鉴**：适合作为 TradingAgents 的对比研究对象，观察不同学术团队在多 Agent 交易框架上的设计取舍。
- **可能风险**：crypto_related 标记；"Vibe Trading"概念本身带有营销色彩，需区分学术实质与概念包装；回测结果可能存在幸存者偏差。

### 3.8 a-stock-data（simonlin1212/a-stock-data）

- **解决什么问题**：A 股全栈数据工具包，15 层 87 端点 34 数据源，覆盖 K 线、逐笔、研报、资金面、新闻、财务、期权、期货、可转债等，除 iwencai 外免 Key。
- **为什么值得关注**：10.4k stars，7 日 +409；解决 A 股量化最痛的数据获取问题，对 AI Agent 友好。
- **技术栈/架构亮点**：Python + Apache-2.0，面向 AI Agent 设计的数据接口层；多数据源聚合和标准化是核心工程价值。
- **是否适合借鉴**：适合。可作为 A 股 AI 交易 Agent 的数据层基础设施；其数据源聚合和标准化思路可复用到其他市场。
- **可能风险**：leverage_or_grid_related 标记；数据源稳定性和合规性需验证；免费数据源可能存在质量和延迟问题。

### 3.9 ai-hedge-fund（virattt/ai-hedge-fund）

- **解决什么问题**：模拟 AI 对冲基金团队，多个 AI Agent 扮演不同角色进行投资决策。
- **为什么值得关注**：63.8k stars，是 AI 交易方向的标志性项目之一；MIT 协议，持续维护。
- **技术栈/架构亮点**：Python 多 Agent 架构，与 TradingAgents 思路类似但更轻量，适合快速理解和二次开发。
- **是否适合借鉴**：适合作为多 Agent 交易决策的入门参考和原型基础。
- **可能风险**：研究工具属性，实盘风险高；策略过拟合和回测偏差需警惕。

### 3.10 vibe-astock（simonlin1212/vibe-astock）

- **解决什么问题**：A 股短线复盘看板，涨停池、连板梯队、龙虎榜、板块资金一屏展示；情绪指标（赚钱效应、晋级率、梯队断层、情绪周期）纯本地计算，AI 只负责叙事生成。
- **为什么值得关注**：仅 553 stars 但 24h 涨星 +69，增速极高；设计理念清晰——"派生指标本地计算，AI 只写叙事"，避免了 LLM 幻觉污染量化指标。
- **技术栈/架构亮点**：Python + FastAPI + React + TypeScript，akshare 数据源，支持 Claude/Codex 订阅免 API key。本地计算 + AI 叙事的架构分离是重要工程洞察。
- **是否适合借鉴**：非常适合。这种"确定性计算 + LLM 叙事"的分离模式应成为金融 AI Agent 的设计原则，值得在更多场景推广。
- **可能风险**：项目极早期，维护持续性未知；A 股数据源依赖。

## 4. 趋势归纳

### 技术趋势

1. **DuckDB + Polars 成为轻量量化数据栈标配**：tick-stock-panel 等项目展示了下游分析型数据库 + 高性能 DataFrame 库替代传统重型数据仓库的趋势。
2. **MCP（Model Context Protocol）成为 AI 金融工具的事实标准接口**：PanWatch、Vibe-Trading、QuantDinger、headroom 等项目均集成 MCP，金融数据源和交易工具的 MCP 化是明确方向。
3. **Rust 在金融基础设施中持续渗透**：hyperswitch 展示 Rust 在支付/交易基础设施中的性能和安全性优势。
4. **本地优先 + 自托管成为金融 AI 工具的默认形态**：OpenStock、tick-stock-panel、PanWatch、vibe-astock 均强调自托管和本地运行。

### 产品趋势

1. **从"回测框架"到"AI 交易工作台"**：产品形态从单一回测工具演进为选股 + 监控 + 回测 + 复盘 + 推送的一体化工作台。
2. **AI 盯盘助手成为新品类**：PanWatch、daily_stock_analysis 等项目定义了"AI 盯盘"这一产品形态，融合实时监控、多 Agent 分析和全渠道推送。
3. **设计智能与金融终端融合**：ui-ux-pro-max-skill、open-design 等 AI 设计工具的高速增长，预示金融终端和交易看板的 UI 生成将加速。

### 量化/交易策略趋势

1. **多 Agent LLM 决策框架成为研究热点**：TradingAgents、Vibe-Trading、ai-hedge-fund 形成学术派三足鼎立，角色分工和辩论机制是共同特征。
2. **A 股量化工具链快速成熟**：从数据获取（a-stock-data）到工作台（tick-stock-panel）到复盘（vibe-astock），A 股量化生态在 2026 年出现爆发式增长。
3. **情绪周期和短线情绪指标受到关注**：vibe-astock 的赚钱效应、晋级率、梯队断层等指标反映了 A 股特有的短线情绪量化需求。

### AI Agent 与自动化交易结合趋势

1. **"确定性计算 + LLM 叙事"的架构分离成为最佳实践**：vibe-astock 的设计理念值得推广——量化指标必须本地确定性计算，LLM 只负责解释和叙事。
2. **Jev/System One 类型化决策模型作为新兴概念出现**：jev-trader、awesome-jev 等项目引入"类型化决策"概念，试图用类型系统约束 AI 交易决策，值得观察但尚需验证。
3. **Token 成本优化成为 Agent 规模化落地的关键瓶颈**：headroom 等项目的高速增长表明，金融 AI Agent 的高频调用场景对 token 压缩有刚性需求。

### 值得后续做原型验证的方向

1. 基于 DuckDB + Polars 的本地量化数据栈 MVP
2. 金融数据源 MCP server 标准化封装
3. "确定性指标计算 + LLM 叙事"分离的复盘看板
4. 多 Agent 交易决策框架中的风控 Agent 独立化设计
5. 金融 AI Agent 的 token 压缩层效果验证

## 5. 今日灵感清单

1. **MVP：本地 A 股情绪复盘看板**：参考 vibe-astock 的架构，用 DuckDB 存储日线数据，Polars 计算涨停池、连板梯队、晋级率等指标，LLM 仅生成盘面叙事。可在一周内用 Codex 复现核心功能。

2. **调研：MCP 金融数据源标准化**：调研 a-stock-data、OpenBB、PanWatch 的 MCP 集成方式，总结金融数据 MCP server 的接口设计规范，形成可复用的数据源接入模板。

3. **原型验证：多 Agent 风控独立化**：从 TradingAgents 和 ai-hedge-fund 中提取风控 Agent 的设计，验证将风控从决策流程中独立为可插拔模块的可行性。

4. **Demo：Token 压缩对金融分析质量的影响**：用 headroom 对研报、行情数据、新闻流进行压缩，对比压缩前后 LLM 分析结论的一致性和成本差异，量化 token 压缩在金融场景的收益。

5. **架构参考：支付编排到交易执行路由的映射**：研究 hyperswitch 的智能路由和降级策略设计，抽象出可应用于交易执行路由的架构模式。

6. **Watchlist 加入：Jev 生态观察**：将 jev-trader、awesome-jev、awesome-jev-projects 加入 watchlist，跟踪"类型化决策模型"是否从概念走向可验证的工程实践。

7. **复刻：OpenStock 的告警系统架构**：用 Codex 复刻 OpenStock 的实时价格告警 + 推送通知模块，作为 AI 盯盘产品的告警基础设施。

8. **调研：A 股数据源合规性**：系统梳理 a-stock-data 列出的 34 个数据源，评估各数据源的使用条款、稳定性和合规风险，形成数据源选型指南。

9. **原型：AI 交易工作台的多租户 SaaS 架构**：参考 QuantDinger 的多租户设计，验证在自托管 AI 交易工作台中引入用户管理、计费和结算模块的可行性。

10. **实验：本地小模型在金融情绪分析中的可行性**：用 needle 或 colibri 的轻量推理方案，测试在边缘设备上运行金融情绪分析模型的性能和准确性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| OpenStock | 金融行情终端产品化参考，涨星势头强劲，架构清晰 |
| TradingAgents | AI 多 Agent 交易框架的学术标杆，持续演进 |
| tick-stock-panel | DuckDB + Polars 量化工作台范式，工程完整度高 |
| PanWatch | TradingAgents 产品化落地案例，观察 Agent 框架如何走向实用 |
| Vibe-Trading | 与 TradingAgents 形成对比，观察学术派框架的设计差异 |
| a-stock-data | A 股数据基础设施，AI Agent 数据层的关键依赖 |
| vibe-astock | "确定性计算 + LLM 叙事"架构分离的早期样本，增速极高 |
| jev-trader | Jev/System One 类型化决策概念的代表项目，观察新概念演进 |
| headroom | 金融 AI Agent token 成本优化的关键基础设施 |
| hyperswitch | 金融基础设施的 Rust 工程参考，智能路由设计值得跟踪 |
| QuantDinger | AI 交易 OS 和多租户 SaaS 架构的实验样本 |
| ai-hedge-fund | 多 Agent 交易决策的轻量参考实现 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

**特别强调**：

- **GitHub star 不是投资建议**：本报告中所有 star 和涨星数据仅反映开源社区关注度，与任何投资回报无关。
- **不运行未知 trading bot**：PanWatch、QuantDinger、jev-trader 等项目虽为开源，但未经审计的自动交易代码可能导致资金损失。
- **不泄露交易所 API key**：任何涉及实盘交易的项目，严禁直接输入真实交易所 API 密钥；应使用模拟盘或独立测试账户。
- **警惕马丁、网格、套利、杠杆类策略**：此类策略在回测中可能表现优异，但实盘存在爆仓风险；a-stock-data 等项目的 leverage_or_grid_related 标记提示需格外谨慎。
- **回测幸存者偏差和过拟合**：LLM 生成策略和 AI 交易框架的回测结果可能存在严重幸存者偏差和过拟合，历史表现不代表未来收益。

## 8. 数据质量说明

- **1 日基线**：已提供（baseline_1d: 2026-09-25.json），1 日涨星数据完整。
- **7 日基线**：已提供（baseline_7d: 2026-09-19.json），大部分项目 7 日涨星数据完整；但 `awesome-jev`（rank 34）和 `vibe-astock`（rank 44）的 7 日涨星为 null，可能因项目创建时间晚于 7 日基线或基线数据缺失。
- **30 日基线**：所有项目的 `star_delta_30d` 均为 null，30 日涨星数据完全缺失，无法评估中长期趋势。
- **采集失败**：未发现明确采集失败，但 `awesome-vue` 出现负涨星（24h -2，7d -5），可能是基线数据波动或 star 回撤，需注意数据噪声。
- **样本偏差**：
  - 候选列表包含大量 awesome 列表类项目（public-apis、awesome-python、awesome-go、build-your-own-x 等），这些项目因关键词误匹配进入候选，并非真正的金融/量化/交易项目，分析时已剔除其噪音影响。
  - 候选项目偏向高 star 项目，低 star 但高增速的早期项目可能被低估。
  - 中文 A 股项目占比显著，反映数据采集关键词对中文金融生态的倾斜。
  - `Financial_freedom` 等项目无 license、无 topics，数据完整性不足，分析价值有限。
