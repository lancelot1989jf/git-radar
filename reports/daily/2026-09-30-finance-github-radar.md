# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-30

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：`iFixAi` 以 24h +1031 星的增速位居真实项目榜首，聚焦 AI Agent 行为审计、幻觉检测、提示注入检测，直接回应 AI Agent 经济中的信任问题。
  2. **AI 交易 Agent 框架**：`TradingAgents`、`Vibe-Trading`、`QuantDinger` 等持续高增长，多智能体 LLM 交易框架仍是量化领域最活跃的工程方向。
  3. **AI 辅助 UI/设计工程**：`ui-ux-pro-max-skill`、`open-design`、`awesome-design-md` 等设计类项目大量进入榜单，反映 coding agent 生态正在向"设计智能"延伸，对金融产品前端快速原型有直接价值。

- **是否出现新趋势**：出现。AI Agent 的"可审计性/合规性"开始成为独立赛道，`iFixAi` 的爆发说明市场从"能跑通 Agent"转向"能证明 Agent 做对了"。同时，`Jev` 生态（`awesome-jev`、`jev-trader`）作为"类型安全决策模型"在交易场景中快速冒头，值得关注。

- **是否出现值得复刻/参考的工程架构**：是。`iFixAi` 的 Agent 审计架构、`headroom` 的 LLM 上下文压缩（60-95% token 节省）、`planning-with-files` 的崩溃恢复式文件规划、`hyperswitch` 的 Rust 支付编排架构，均有较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：`Financial_freedom`（"最全赚钱投资指南"）以 24h +388 星异常增长，但内容为投资指南类仓库，无代码、无 license，营销属性强，需警惕。多个 `awesome-*` 列表类项目因关键词误匹配进入榜单，实际与金融/量化关联度低，属于样本噪声而非骗局。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 484886 | +420 | +2281 | Python | API 列表 | 免费 API 合集 | 低（非金融核心） | 中 |
| 2 | ifixai-ai/iFixAi | 17737 | +1031 | +2025 | Python | AI 审计/风控 | AI Agent 独立审计工具 | 高 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 132096 | +385 | +1898 | Python | AI 设计技能 | 多平台 UI/UX 设计智能 | 中高 | 低 |
| 4 | vinta/awesome-python | 324405 | +251 | +1788 | Python | 资源列表 | Python 工具精选列表 | 低 | 低 |
| 5 | codecrafters-io/build-your-own-x | 550936 | +213 | +1812 | Markdown | 教程列表 | 从零复刻技术项目 | 中 | 中 |
| 6 | awesome-selfhosted/awesome-selfhosted | 323032 | +244 | +1683 | 无 | 自托管列表 | 自托管服务列表 | 低 | 中 |
| 7 | VoltAgent/awesome-design-md | 119011 | +162 | +1439 | 无 | 设计系统 | DESIGN.md 设计系统合集 | 中 | 中 |
| 8 | JustVugg/colibri | 38709 | +187 | +1329 | C | 模型推理 | 纯 C 零依赖 MoE 推理引擎 | 中 | 低 |
| 9 | nexu-io/open-design | 98970 | +185 | +1109 | TypeScript | AI 设计 | 本地优先 AI 设计引擎 | 中高 | 低 |
| 10 | codeman008/Financial_freedom | 5410 | +388 | +1430 | 无 | 投资指南 | 赚钱投资指南 | 低 | 中 |
| 11 | TauricResearch/TradingAgents | 109404 | +109 | +1055 | Python | AI 交易/多智能体 | 多智能体 LLM 金融交易框架 | 高 | 低 |
| 12 | avelino/awesome-go | 186344 | +148 | +1009 | Go | 资源列表 | Go 框架库精选 | 低 | 中 |
| 13 | juspay/hyperswitch | 45271 | +9 | +1434 | Rust | 支付/金融科技 | 开源可组合支付平台 | 高 | 低 |
| 14 | ripienaar/free-for-dev | 139000 | +97 | +901 | HTML | 资源列表 | 开发者免费资源 | 低 | 低 |
| 15 | awesome-dsh-plugin/awesome-dsh-plugin | 17482 | +128 | +714 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | 低 | 低 |
| 16 | MakazhanAlpamys/Soup | 7873 | +163 | +804 | Python | LLM 微调 | 单 YAML 微调 LLM | 中 | 低 |
| 17 | career-ops-hq/career-ops | 73172 | +77 | +621 | JavaScript | AI Agent | AI 求职 Agent | 中 | 低 |
| 18 | headroomlabs-ai/headroom | 74203 | +76 | +539 | Python | LLM 压缩 | LLM 上下文压缩 | 高 | 低 |
| 19 | HKUDS/Vibe-Trading | 34398 | +57 | +484 | Python | AI 交易 | 个人交易 Agent | 高 | 中 |
| 20 | ruvnet/ruflo | 73594 | +57 | +431 | TypeScript | Agent 框架 | 多智能体编排框架 | 中高 | 低 |
| 21 | Open-Dev-Society/OpenStock | 19522 | +34 | +588 | TypeScript | 行情平台 | 开源行情追踪平台 | 中 | 低 |
| 22 | unslothai/unsloth | 77103 | +46 | +439 | Python | LLM 微调 | 本地 LLM 训练/推理 UI | 中 | 低 |
| 23 | yibie/awesome-jev | 2037 | +44 | +507 | Python | AI 决策模型 | Jev 类型安全决策模型生态 | 中 | 中 |
| 24 | cactus-compute/needle | 12903 | +33 | +460 | Python | 边缘 AI | 微型设备自动化基础模型 | 中 | 中 |
| 25 | code-yeongyu/oh-my-openagent | 69702 | +37 | +354 | TypeScript | Agent 编排 | 图工程 Agent 编排 | 中 | 低 |
| 26 | hesreallyhim/awesome-claude-code | 54870 | +43 | +348 | Python | 资源列表 | Claude Code 资源精选 | 低 | 低 |
| 27 | jarrodwatts/jev-trader | 2714 | +21 | +502 | TypeScript | AI 交易 | Jev 驱动的链上交易 | 中 | 低 |
| 28 | punkpeye/awesome-mcp-servers | 95731 | +40 | +259 | 无 | MCP 列表 | MCP 服务器合集 | 中 | 低 |
| 29 | CopilotKit/OpenBot | 5774 | +39 | +298 | TypeScript | Agent 治理 | AI 协作者计算机环境 | 中 | 中 |
| 30 | nidhinjs/prompt-master | 13911 | +46 | +325 | 无 | Prompt 工程 | 精准 Prompt 生成技能 | 低 | 低 |
| 31 | ZhuLinsen/daily_stock_analysis | 65816 | +16 | +269 | Python | 股票分析 | LLM 多市场股票分析 | 高 | 低 |
| 32 | anbeime/skill | 7442 | +44 | +285 | Python | 技能商店 | AI Agent 技能库 | 中 | 低 |
| 33 | shy3130/tick-stock-panel | 5349 | +11 | +410 | Python | 量化工作台 | A 股选股/监控/回测 | 高 | 低 |
| 34 | samugit83/redamon | 2870 | +43 | +294 | Python | 安全/红队 | AI 红队自动化框架 | 中 | 低 |
| 35 | shiyu-coder/Kronos | 39714 | +49 | +318 | Python | 金融基础模型 | 金融市场语言基础模型 | 高 | 低 |
| 36 | garrytan/gbrain | 30466 | +20 | +185 | TypeScript | Agent 框架 | 个人 Agent 大脑 | 中 | 低 |
| 37 | OpenByteInc/QuantDinger | 12348 | +18 | +269 | Python | AI 交易 OS | 开源 AI 交易操作系统 | 高 | 中 |
| 38 | antirez/ds4 | 22817 | +30 | +145 | C | 模型推理 | DeepSeek 4 本地推理引擎 | 中 | 低 |
| 39 | TNT-Likely/PanWatch | 1910 | +23 | +296 | Python | AI 盯盘 | A/港/美股 AI 盯盘 | 高 | 中 |
| 40 | OthmanAdi/planning-with-files | 27216 | +30 | +120 | Shell | Agent 规划 | 文件式持久化 Agent 规划 | 高 | 低 |
| 41 | fffaraz/awesome-cpp | 73556 | +18 | +117 | 无 | 资源列表 | C++ 资源精选 | 低 | 低 |
| 42 | awesomedata/awesome-public-datasets | 79260 | +9 | +132 | 无 | 数据集列表 | 公开数据集精选 | 中 | 中 |
| 43 | virattt/ai-hedge-fund | 63814 | +12 | +115 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 44 | josephmisiti/awesome-machine-learning | 74507 | +11 | +79 | Python | 资源列表 | ML 资源精选 | 低 | 低 |
| 45 | Developer-Y/cs-video-courses | 83590 | +10 | +41 | 无 | 课程列表 | CS 视频课程列表 | 低 | 中 |
| 46 | openbq-org/OpenBB | 73708 | 信息不足 | 信息不足 | Python | 金融数据平台 | 分析师/量化/AI Agent 开放数据平台 | 高 | 中 |
| 47 | vuejs/awesome-vue | 73539 | -4 | -6 | 无 | 资源列表 | Vue 资源精选 | 低 | 低 |
| 48 | ByteByteGoHq/system-design-101 | 90143 | +31 | +271 | 无 | 系统设计 | 系统设计可视化教程 | 中 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi — AI Agent 独立审计框架

- **解决什么问题**：回答 AI Agent 经济中最核心的问题——"Agent 是否在做它应该做的事"。支持人工或 Agent 自审计，声称 120 秒内给出结论。
- **为什么值得关注**：24h +1031 星、7d +2025 星，是本期真实项目中增速最快的。随着 AI 交易 Agent 和自动化工作流增多，Agent 行为审计从"可选"变为"刚需"。
- **技术栈/架构亮点**：Python + Apache-2.0；topics 覆盖 AI 对齐、幻觉检测、提示注入检测、ISO 42001、NIST AI RMF、OWASP LLM、EU AI Act，说明其审计维度对齐主流 AI 治理框架。
- **是否适合借鉴到 AI/自动化交易**：非常适合。可将其审计思路迁移到交易 Agent 场景：在下单前对 Agent 决策做合规检查、异常行为检测、幻觉识别，形成"决策-审计-执行"闭环。
- **可能的风险**：项目较新（2026-04 创建），审计标准本身可能不成熟；"120 秒"的营销表述需谨慎验证；若用于真实交易审计，误报/漏报都可能带来资金风险。

### 3.2 TauricResearch/TradingAgents — 多智能体 LLM 交易框架

- **解决什么问题**：用多智能体 LLM 框架模拟金融交易决策流程，将分析师、研究员、交易员等角色拆分为独立 Agent 协作。
- **为什么值得关注**：109k stars，7d +1055，是 AI 交易领域最具影响力的开源框架之一，且持续活跃（近 30 天有 push）。
- **技术栈/架构亮点**：Python + Apache-2.0；多智能体架构，topics 明确标注 agent、finance、llm、multiagent、trading。其角色分工设计是核心架构价值。
- **是否适合借鉴**：适合。多角色 Agent 协作模式可直接迁移到企业级投研 Agent、风控 Agent、合规 Agent 的编排中。`PanWatch` 已基于 TradingAgents 构建了 A/港/美股盯盘应用，验证了其可扩展性。
- **可能的风险**：研究工具属性强，回测结果不代表实盘；LLM 决策存在幻觉风险；多 Agent 协作的延迟和成本可能不适合高频场景。

### 3.3 juspay/hyperswitch — Rust 支付编排平台

- **解决什么问题**：开源可组合支付平台，连接多个支付、风控、vault、tokenization 提供商，提供智能路由、收入恢复、成本可观测性和对账。
- **为什么值得关注**：7d +1434 星（24h 仅 +9，说明涨星集中在某几天），Rust 编写，是金融基础设施领域少有的高质量开源项目。
- **技术栈/架构亮点**：Rust + Apache-2.0；PCI 合规；SaaS 和自托管双模式；智能路由和支付编排是核心架构亮点。
- **是否适合借鉴**：适合。支付编排中的"多提供商智能路由 + 成本可观测 + 对账"模式，可直接类比到交易执行中的"多交易所智能路由 + 滑点成本分析 + 交易对账"。
- **可能的风险**：支付领域合规门槛高；自托管部署复杂；open issues 2265 个，维护压力较大。

### 3.4 headroomlabs-ai/headroom — LLM 上下文压缩

- **解决什么问题**：在工具输出、日志、文件、RAG 片段到达 LLM 之前进行压缩，coding agent 节省 20% token，JSON 场景节省 60-95% token，且答案质量不变。
- **为什么值得关注**：74k stars，7d +539。对 AI 交易 Agent 而言，行情数据、订单簿、新闻流都是高 token 消耗场景，压缩能力直接影响成本和延迟。
- **技术栈/架构亮点**：Python + Apache-2.0；提供 library、proxy、MCP server 三种形态，可无缝接入现有 Agent 栈。
- **是否适合借鉴**：非常适合。交易 Agent 处理大量结构化 JSON（订单簿、K 线、账户信息）时，可引入类似压缩层降低 LLM 调用成本。
- **可能的风险**：压缩可能丢失关键信息（如极端行情中的异常值）；对金融数据的有损压缩需谨慎验证。

### 3.5 HKUDS/Vibe-Trading — 个人交易 Agent

- **解决什么问题**：定位为"Vibe-Trading: Your Personal Trading Agent"，将 LLM 多智能体与 MCP 结合，面向个人交易场景。
- **为什么值得关注**：34k stars，来自 HKUDS（香港大学数据科学实验室），学术背景 + 交易场景结合，7d +484。
- **技术栈/架构亮点**：Python + MIT；topics 覆盖 ai-agent、algorithmic-trading、backtesting、fintech、llm、mcp、multi-agent、quantitative-finance。MCP 集成是亮点，意味着可标准化接入外部数据源和工具。
- **是否适合借鉴**：适合。MCP 在交易 Agent 中的应用值得深入研究，可作为构建标准化交易工具接口的参考。
- **可能的风险**：crypto_related 标记；"Vibe Trading"概念本身暗示低严谨性；学术项目回测与实盘差距大；不建议直接用于真实资金。

### 3.6 shiyu-coder/Kronos — 金融市场语言基础模型

- **解决什么问题**：构建"金融市场语言"的基础模型，试图用 foundation model 范式统一金融时序、文本、结构化数据的建模。
- **为什么值得关注**：39k stars，7d +318。金融基础模型是量化研究的前沿方向，若成功将改变策略开发范式。
- **技术栈/架构亮点**：Python + MIT；项目定位为 Foundation Model，架构细节需进一步调研。
- **是否适合借鉴**：适合作为研究方向跟踪。可关注其模型输入表示、预训练任务设计、下游任务适配方式。
- **可能的风险**：研究属性强，实盘价值未验证；金融数据非平稳性可能导致模型快速失效；维护活跃度需关注（最近 push 在 2026-04）。

### 3.7 OpenByteInc/QuantDinger — AI 交易 OS

- **解决什么问题**：定位为"开源 AI Trading OS"，集成研究、Python 策略构建、回测、模拟/实盘交易，覆盖 crypto、股票、外汇，并支持多租户交易 SaaS。
- **为什么值得关注**：12k stars，7d +269。试图做"交易操作系统"级别的整合，架构野心大。
- **技术栈/架构亮点**：Python + Apache-2.0；集成 Jev System One、MCP server、多交易所（Binance、Alpaca）、多租户 SaaS（用户管理、计费、支付、结算）。
- **是否适合借鉴**：适合研究其"策略开发-回测-模拟-实盘"全链路整合架构，以及多租户交易 SaaS 的设计。
- **可能的风险**：crypto_related；涉及真实交易所 API；多租户 + 交易 + 结算的组合意味着极高的安全和合规要求；不建议直接部署使用。

### 3.8 OthmanAdi/planning-with-files — 文件式持久化 Agent 规划

- **解决什么问题**：为 AI coding agent 和长时运行任务提供基于文件的持久化规划，解决 /clear 和 compaction 后的会话丢失、上下文腐烂问题。
- **为什么值得关注**：27k stars，7d +120。长时运行 Agent 的状态管理是 AI 交易 Agent 落地的关键工程难题。
- **技术栈/架构亮点**：Shell + MIT；崩溃安全的 Markdown 计划、会话恢复、每轮重注入、确定性完成门控。支持 Claude Code、Codex、Cursor 等 60+ Agent。
- **是否适合借鉴**：非常适合。交易 Agent 需要跨天、跨会话保持策略状态和决策上下文，文件式持久化规划是轻量且可靠的方案。
- **可能的风险**：文件并发写入冲突；敏感交易计划若存储在文件中需注意加密和权限管理。

### 3.9 ZhuLinsen/daily_stock_analysis — LLM 多市场股票分析

- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板和自动推送，支持零成本定时运行。
- **为什么值得关注**：65k stars，7d +269。中文项目，A 股场景，实用性强。
- **技术栈/架构亮点**：Python + MIT；topics 覆盖 a-stock、ai-agent、aigc、llm、quant、quantitative-finance、quantitative-trading。多源数据整合 + 定时自动化是核心。
- **是否适合借鉴**：适合。可作为"LLM + 多源金融数据 + 定时自动化报告"的参考实现，尤其适合研究 A 股数据源整合方案。
- **可能的风险**：分析结果不构成投资建议；数据源稳定性依赖第三方；零成本方案可能在数据质量上妥协。

### 3.10 shy3130/tick-stock-panel — A 股量化工作台

- **解决什么问题**：自托管、零运维的 A 股"选股 + 监控 + 回测"量化工作台，LLM 驱动策略定制和个股分析。
- **为什么值得关注**：5.3k stars，7d +410。技术栈现代（DuckDB、Polars、FastAPI、React），是 A 股量化工具链的优质参考。
- **技术栈/架构亮点**：Python + MIT；DuckDB + Polars 的组合适合本地量化数据分析；FastAPI + React 前后端分离；LLM 集成用于策略定制和复盘。
- **是否适合借鉴**：非常适合。DuckDB + Polars 的本地量化数据栈值得复刻；"选股-监控-回测"一体化工作台是很好的 MVP 参考。
- **可能的风险**：A 股数据源合规性；回测过拟合风险；个人开源项目维护持续性。

## 4. 趋势归纳

### 技术趋势
- **AI Agent 治理与审计成为独立技术栈**：iFixAi 的爆发标志着 Agent 审计从理念走向工具化，对齐 ISO 42001、NIST AI RMF、EU AI Act 等框架。
- **LLM 上下文工程持续深化**：headroom（压缩）、planning-with-files（持久化规划）代表两个方向——降低 token 成本和增强长时记忆。
- **本地/边缘推理加速**：colibri（纯 C MoE）、ds4（Metal/CUDA/ROCm）、needle（微型设备）显示推理引擎向极致效率和边缘部署演进。
- **MCP 成为 Agent 工具集成标准**：Vibe-Trading、QuantDinger、awesome-mcp-servers 均围绕 MCP 构建生态。

### 产品趋势
- **"AI Trading OS"概念兴起**：QuantDinger 试图整合研究、回测、交易、SaaS 全链路，从单点工具走向平台化。
- **设计智能与金融产品结合**：ui-ux-pro-max-skill、open-design 等工具可显著加速金融产品前端原型开发。
- **自托管金融工具需求增长**：OpenStock、tick-stock-panel、PanWatch 均强调自托管，反映用户对数据主权和成本控制的关注。

### 量化/交易策略趋势
- **多智能体 LLM 交易框架持续主导**：TradingAgents、Vibe-Trading、ai-hedge-fund 均采用多角色 Agent 协作模式。
- **金融基础模型探索**：Kronos 代表"金融市场语言"建模方向，值得长期跟踪。
- **A 股 + LLM 场景活跃**：daily_stock_analysis、tick-stock-panel、PanWatch 显示中文社区在 A 股 AI 分析场景的活跃度。

### AI Agent 与自动化交易结合趋势
- **从"生成交易信号"到"审计交易决策"**：iFixAi 的出现提示下一阶段重点可能是交易 Agent 的可信度和合规性。
- **类型安全决策模型进入交易**：Jev 生态（awesome-jev、jev-trader、QuantDinger 集成）试图用类型安全约束 LLM 决策，降低幻觉风险。
- **长时运行 Agent 的状态管理成为关键**：planning-with-files 的流行说明 Agent 从"单次任务"走向"持续运行"。

### 值得后续做原型验证的方向
1. 交易 Agent 决策审计层（借鉴 iFixAi 思路）
2. 金融数据 LLM 上下文压缩（借鉴 headroom）
3. DuckDB + Polars 本地量化数据栈（借鉴 tick-stock-panel）
4. MCP 标准化交易工具接口（借鉴 Vibe-Trading）
5. 文件式持久化的长时交易 Agent 状态管理（借鉴 planning-with-files）

## 5. 今日灵感清单

1. **MVP：交易 Agent 决策审计中间层**——在现有 LLM 交易 Agent 的下单环节前插入审计层，检查决策是否符合预设风控规则、是否存在幻觉（如引用不存在的价格）、是否偏离策略授权范围。可参考 iFixAi 的审计维度设计。

2. **调研：MCP 在交易工具链中的标准化实践**——深入调研 Vibe-Trading 和 QuantDinger 的 MCP server 实现，评估将行情获取、订单执行、持仓查询标准化为 MCP 工具的可行性。

3. **Codex/Agent 自动复现：DuckDB + Polars 量化数据管道**——让 Codex 基于 tick-stock-panel 的架构，复现一个最小化的"数据导入 → DuckDB 存储 → Polars 分析 → 回测"管道，验证本地量化数据栈的性能。

4. **MVP：金融数据 LLM 上下文压缩器**——基于 headroom 的思路，构建针对订单簿、K 线、账户信息的专用压缩器，在保留关键异常值的前提下降低交易 Agent 的 token 消耗。

5. **调研：Jev 类型安全决策模型在交易中的应用**——研究 awesome-jev 和 jev-trader，评估"类型安全决策"是否能有效约束 LLM 交易决策的输出格式和合法性。

6. **MVP：文件式持久化的交易 Agent 状态管理器**——借鉴 planning-with-files，为交易 Agent 设计跨会话的策略状态、持仓快照、决策日志的 Markdown 持久化方案。

7. **Watchlist：Kronos 金融基础模型**——持续跟踪其模型架构和预训练方法，评估是否值得投入资源复现或微调。

8. **调研：hyperswitch 的智能路由架构**——研究其多提供商智能路由和成本可观测性设计，思考如何类比到多交易所交易执行路由。

9. **MVP：AI Agent 技能商店的金融专项版**——参考 anbeime/skill 的模式，构建一个专注于金融分析、量化研究、风控的 Agent 技能包集合。

10. **调研：OpenBot 的 Agent 治理模式**——研究其"每个动作先决策后执行、全程记录"的治理架构，评估是否适合作为交易 Agent 的沙箱环境。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计赛道爆发，交易 Agent 合规化关键参考 |
| TauricResearch/TradingAgents | AI 交易多智能体框架标杆，持续活跃 |
| shiyu-coder/Kronos | 金融基础模型前沿方向，长期跟踪价值高 |
| OpenByteInc/QuantDinger | AI Trading OS 整合架构，观察其演进 |
| headroomlabs-ai/headroom | LLM 上下文压缩，交易 Agent 降本关键 |
| OthmanAdi/planning-with-files | 长时 Agent 状态管理，交易 Agent 落地必需 |
| shy3130/tick-stock-panel | DuckDB + Polars 量化栈，A 股工作台参考 |
| juspay/hyperswitch | 支付编排架构，交易路由类比参考 |
| HKUDS/Vibe-Trading | MCP 交易集成，学术 + 工程结合 |
| yibie/awesome-jev | Jev 类型安全决策生态，新兴方向 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：存在（baseline_1d: 2026-09-29.json），大部分项目有 24h 涨星数据。
- **7 日基线**：存在（baseline_7d: 2026-09-23.json），大部分项目有 7d 涨星数据。
- **30 日基线**：缺失。所有项目的 `star_delta_30d` 均为 null，无法评估中期趋势。
- **采集失败/数据缺失**：`OpenBB` 的 1d/7d 涨星均为 null，可能因基线快照中缺失该项目或数据采集失败；`awesome-vue` 出现负涨星（-4/-6），可能因 star 撤回或数据修正。
- **样本偏差**：大量 `awesome-*` 列表类项目（public-apis、awesome-python、awesome-go、awesome-selfhosted 等）因关键词误匹配进入候选集，实际与金融/量化关联度低，稀释了信号密度。真正与金融/交易直接相关的项目约占候选集的 40%。
- **分类噪声**：部分项目的 `category_guess` 与 `matched_queries` 存在明显不一致（如 build-your-own-x 被标记为 trading_bot 但实际是编程教程列表），分析时需以项目实际内容为准。
