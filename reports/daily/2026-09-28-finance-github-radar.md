# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-28

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 交易框架**：TradingAgents、Vibe-Trading、QuantDinger 等 LLM 多智能体交易框架持续高增长，AI 与量化交易的结合正在从“研究 demo”走向“可部署系统”。
  2. **AI Agent 治理与审计**：iFixAi 以 24h +396 的涨星速度异军突起，聚焦 AI Agent 的独立审计、对齐与风险管理，反映市场对“Agent 是否在做它该做的事”这一问题的强烈需求。
  3. **本地化/边缘推理引擎**：colibri、magnitude、needle、ds4 等项目集中出现，强调“在自有硬件上运行前沿模型”，与金融场景中数据隐私、低延迟、本地部署需求高度契合。

- **是否出现新趋势**：出现。AI Agent 的“可审计性”和“治理”开始成为独立赛道，不再只是交易策略的附属品；同时“本地优先 + 小模型 + 工具调用”的架构正在渗透到金融数据分析和交易决策场景。

- **是否出现值得复刻/参考的工程架构**：是。TradingAgents 的多智能体分工（研究/风险/交易）、QuantDinger 的“研究-回测-模拟-实盘”一体化 SaaS 架构、iFixAi 的 Agent 审计流水线、OpenBB 的开放数据平台，都具备较高的工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：部分项目存在明显营销化命名（如 “Vibe-Trading”）、短期暴涨但缺乏实质内容（如 awesome-jev 仅 1940 stars 但 7d +884）、以及 crypto 相关 trading bot 类项目（如 jev-trader、QuantDinger）需要谨慎对待。未发现明确骗局证据，但多个项目存在“研究工具被包装成实盘工具”的倾向。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 484161 | +279 | +2030 | Python | API 资源列表 | 免费 API 聚合列表 | 数据源发现 | 中 |
| 2 | vinta/awesome-python | 323913 | +287 | +1724 | Python | Python 资源列表 | Python 工具精选列表 | 技术选型参考 | 低 |
| 3 | codecrafters-io/build-your-own-x | 550493 | +282 | +1815 | Markdown | 教程列表 | 从零复刻技术项目教程 | 工程能力训练 | 中 |
| 4 | awesome-selfhosted/awesome-selfhosted | 322550 | +243 | +1669 | 无 | 自托管列表 | 自托管服务精选 | 本地化部署参考 | 中 |
| 5 | nextlevelbuilder/ui-ux-pro-max-skill | 131330 | +262 | +1682 | Python | AI 设计技能 | AI 驱动的 UI/UX 设计技能 | Agent 前端生成 | 低 |
| 6 | VoltAgent/awesome-design-md | 118652 | +244 | +1517 | 无 | 设计系统列表 | DESIGN.md 设计系统集合 | Agent UI 一致性 | 中 |
| 7 | juspay/hyperswitch | 45195 | +254 | +1508 | Rust | 支付平台 | 开源可组合支付平台 | 支付编排架构 | 低 |
| 8 | JustVugg/colibri | 38189 | +191 | +1272 | C | 推理引擎 | 纯 C 零依赖 MoE 推理引擎 | 本地推理架构 | 低 |
| 9 | TauricResearch/TradingAgents | 109145 | +201 | +1148 | Python | AI 交易框架 | 多智能体 LLM 金融交易框架 | 多 Agent 交易架构 | 低 |
| 10 | Open-Dev-Society/OpenStock | 19454 | +46 | +1499 | TypeScript | 股票平台 | 开源实时行情与预警平台 | 行情产品架构 | 低 |
| 11 | nexu-io/open-design | 98539 | +163 | +1028 | TypeScript | AI 设计工具 | 本地优先 AI 设计引擎 | Agent 设计工作流 | 低 |
| 12 | avelino/awesome-go | 186065 | +141 | +998 | Go | Go 资源列表 | Go 框架与库精选 | Go 技术选型 | 中 |
| 13 | ripienaar/free-for-dev | 138816 | +89 | +845 | HTML | 免费资源列表 | SaaS/PaaS 免费层列表 | 基础设施选型 | 低 |
| 14 | ifixai-ai/iFixAi | 16407 | +396 | +738 | Python | AI 审计 | AI Agent 独立审计框架 | Agent 治理与风控 | 低 |
| 15 | yibie/awesome-jev | 1940 | +82 | +884 | Python | AI 模型生态 | Jev 模型项目精选 | 类型化决策模型 | 中 |
| 16 | awesome-dsh-plugin/awesome-dsh-plugin | 17191 | +104 | +636 | JavaScript | 插件列表 | DeepSeek Harness 插件列表 | Agent 插件生态 | 低 |
| 17 | career-ops-hq/career-ops | 73017 | +73 | +645 | JavaScript | AI 求职工具 | 开源 AI 求职代理 | Agent 工作流参考 | 低 |
| 18 | magnitudedev/magnitude | 5428 | +135 | +649 | Rust | 推理引擎 | 本地硬件推理引擎 | 本地推理优化 | 低 |
| 19 | headroomlabs-ai/headroom | 74045 | +74 | +618 | Python | Token 压缩 | LLM 输出压缩工具 | 上下文成本优化 | 低 |
| 20 | HKUDS/Vibe-Trading | 34265 | +87 | +463 | Python | AI 交易 | 个人交易 Agent | 交易 Agent 产品化 | 中 |
| 21 | cactus-compute/needle | 12823 | +48 | +736 | Python | 边缘 AI | 微型设备自动化基础模型 | 边缘 Agent 架构 | 中 |
| 22 | unslothai/unsloth | 76985 | +93 | +436 | Python | 模型微调 | 本地 LLM 微调框架 | 模型定制能力 | 低 |
| 23 | jarrodwatts/jev-trader | 2666 | +49 | +778 | TypeScript | AI 交易 | Monad 区块级 AI 交易决策 | 高频 Agent 决策 | 低 |
| 24 | codeman008/Financial_freedom | 4607 | +142 | +641 | 无 | 投资指南 | 赚钱投资指南 | 信息不足 | 中 |
| 25 | MakazhanAlpamys/Soup | 7496 | +72 | +518 | Python | 模型微调 | 单 YAML 微调 LLM | 低成本微调 | 低 |
| 26 | ruvnet/ruflo | 73462 | +50 | +443 | TypeScript | Agent 框架 | 多智能体 swarm 框架 | 多 Agent 编排 | 低 |
| 27 | TNT-Likely/PanWatch | 1869 | +32 | +653 | Python | AI 盯盘 | A股/港股/美股 AI 盯盘 | 多市场监控 | 中 |
| 28 | ZhuLinsen/daily_stock_analysis | 65781 | +48 | +324 | Python | AI 股票分析 | LLM 多市场股票分析 | 数据工程流水线 | 低 |
| 29 | shiyu-coder/Kronos | 39624 | +113 | +298 | Python | 金融基础模型 | 金融市场语言基础模型 | 金融 LLM 方向 | 低 |
| 30 | code-yeongyu/oh-my-openagent | 69638 | +32 | +368 | TypeScript | Agent 编排 | 图工程 Agent 编排 | Agent 编排模式 | 低 |
| 31 | CopilotKit/OpenBot | 5694 | +38 | +403 | TypeScript | Agent 计算机 | 开源 AI 数字员工 | Agent 治理架构 | 中 |
| 32 | OpenBB-finance/OpenBB | 73609 | +55 | +253 | Python | 金融数据平台 | 开放金融数据平台 | 数据平台架构 | 中 |
| 33 | nidhinjs/prompt-master | 13804 | +69 | +305 | 无 | Prompt 工程 | Claude 提示词技能 | Prompt 优化 | 低 |
| 34 | OpenByteInc/QuantDinger | 12297 | +50 | +334 | Python | AI 交易 OS | 开源 AI 交易操作系统 | 交易 SaaS 架构 | 中 |
| 35 | shy3130/tick-stock-panel | 5310 | +24 | +442 | Python | A股量化 | 自托管 A股量化工作台 | 本地量化工作台 | 低 |
| 36 | samugit83/redamon | 2777 | +81 | +234 | Python | 安全测试 | AI 红队自动化框架 | 安全测试自动化 | 低 |
| 37 | punkpeye/awesome-mcp-servers | 95647 | +37 | +239 | 无 | MCP 列表 | MCP 服务器集合 | MCP 生态参考 | 低 |
| 38 | anbeime/skill | 7337 | +50 | +266 | Python | 技能商店 | AI Agent 技能库 | 技能包管理 | 低 |
| 39 | garrytan/gbrain | 30423 | +30 | +209 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | Agent 认知架构 | 低 |
| 40 | awesomedata/awesome-public-datasets | 79227 | +37 | +134 | 无 | 数据集列表 | 高质量公开数据集 | 数据源发现 | 中 |
| 41 | antirez/ds4 | 22769 | +25 | +153 | C | 推理引擎 | DeepSeek 本地推理引擎 | 本地推理架构 | 低 |
| 42 | jundizhou/easy-stock | 1054 | +83 | 信息不足 | Go | A股分析 | A股 AI 投研桌面工作台 | 桌面端投研工具 | 低 |
| 43 | fffaraz/awesome-cpp | 73527 | +21 | +122 | 无 | C++ 资源列表 | C++ 框架与库精选 | 高性能技术选型 | 低 |
| 44 | virattt/ai-hedge-fund | 63786 | +10 | +128 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 多 Agent 投研 | 低 |
| 45 | josephmisiti/awesome-machine-learning | 74485 | +12 | +95 | Python | ML 资源列表 | 机器学习框架精选 | ML 技术选型 | 低 |
| 46 | atilaahmettaner/tradingview-mcp | 4769 | +99 | +163 | Python | MCP 交易 | TradingView MCP 服务器 | 行情数据接入 | 中 |
| 47 | Developer-Y/cs-video-courses | 83578 | +5 | +32 | 无 | 课程列表 | 计算机科学视频课程 | 学习资源 | 中 |
| 48 | vuejs/awesome-vue | 73543 | 0 | -3 | 无 | Vue 资源列表 | Vue 生态精选 | 前端技术选型 | 低 |
| 49 | ByteByteGoHq/system-design-101 | 90086 | +29 | +405 | 无 | 系统设计 | 系统设计图解 | 架构设计参考 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents

- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，通过多个专职 Agent（如研究、风险、交易）分工完成分析、风险评估和交易决策。
- **为什么值得关注**：109k stars，7d +1148，是当前 AI 交易框架中规模最大、增长最稳的项目之一。Apache-2.0 协议，近 30 天持续 push，维护活跃。
- **技术栈/架构亮点**：Python + LLM + 多 Agent 编排。核心价值在于将交易决策拆解为可独立评估的 Agent 角色，降低单点决策风险。
- **是否适合借鉴**：非常适合。其多 Agent 分工模式可直接迁移到企业级投研 Agent、风控 Agent 和自动化交易决策系统中。
- **可能风险**：作为研究工具，回测结果可能存在过拟合；LLM 决策的可解释性和一致性不足；不应直接用于实盘。

### 3.2 ifixai-ai/iFixAi

- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，覆盖 AI 对齐、幻觉检测、提示注入、ISO 42001、NIST AI RMF 等治理维度。
- **为什么值得关注**：24h +396 涨星，是今日涨星最快的项目之一。AI Agent 治理正在成为独立赛道，与金融场景中的合规审计需求高度契合。
- **技术栈/架构亮点**：Python + CLI，支持人工或 Agent 自审计，声称 120 秒内给出审计结论。覆盖 EU AI Act、OWASP LLM 等标准。
- **是否适合借鉴**：非常适合。金融交易 Agent 的合规审计、行为监控、异常检测都可以参考其审计框架。
- **可能风险**：项目较新（2026-04 创建），审计深度和准确性尚未得到充分验证；不应将其审计结论作为唯一合规依据。

### 3.3 OpenByteInc/QuantDinger

- **解决什么问题**：提供“研究-策略构建-回测-模拟-实盘”一体化的 AI 交易操作系统，支持 crypto、股票、外汇，并可启动多租户交易 SaaS。
- **为什么值得关注**：Apache-2.0，12k stars，7d +334。其“交易 SaaS 化”的架构思路在开源交易项目中较为少见。
- **技术栈/架构亮点**：Python + MCP Server + 多交易所接入（Binance、Alpaca 等），内置用户管理、计费、支付和结算模块。
- **是否适合借鉴**：架构层面值得参考，尤其是“研究到实盘”的完整链路和 SaaS 化设计。但实盘交易部分风险较高。
- **可能风险**：crypto 相关，涉及真实交易所 API；多租户 SaaS 模式可能带来合规和资金安全风险；不应直接运行或输入真实 API key。

### 3.4 HKUDS/Vibe-Trading

- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 能力与交易决策结合，支持回测和多市场分析。
- **为什么值得关注**：HKUDS 出品，34k stars，MIT 协议。项目名称和定位反映了“vibe trading”这一新兴但争议较大的概念。
- **技术栈/架构亮点**：Python + LLM + MCP + 多 Agent。强调“个人化”交易体验。
- **是否适合借鉴**：产品定位和交互设计值得参考，但“vibe trading”概念本身缺乏严谨的策略支撑。
- **可能风险**：研究工具属性明显，但命名容易诱导用户将其视为实盘工具；策略过拟合风险高；不应直接用于实盘。

### 3.5 OpenBB-finance/OpenBB

- **解决什么问题**：为分析师、量化研究员和 AI Agent 提供统一的开放金融数据平台，覆盖股票、加密、衍生品、固定收益、宏观经济等。
- **为什么值得关注**：73k stars，持续活跃。作为金融数据基础设施，其“为 AI Agent 提供数据”的定位与当前趋势高度契合。
- **技术栈/架构亮点**：Python 为主，模块化数据接入架构，支持多种资产类别和数据源。
- **是否适合借鉴**：非常适合。可作为企业级投研 Agent 和量化系统的数据层参考。
- **可能风险**：数据质量和延迟依赖上游数据源；license 为 Other，商用需注意。

### 3.6 JustVugg/colibri

- **解决什么问题**：在自有硬件上运行前沿 MoE 模型，纯 C 实现、零依赖，专家从磁盘流式加载。
- **为什么值得关注**：38k stars，7d +1272。其“小引擎 + 大模型”的架构思路对金融场景中的本地推理需求有直接参考价值。
- **技术栈/架构亮点**：纯 C、零依赖、磁盘流式加载专家，极致轻量。
- **是否适合借鉴**：适合。金融数据隐私和低延迟场景下，本地推理引擎是重要基础设施。
- **可能风险**：项目较新，生态和文档可能不完善；性能需自行验证。

### 3.7 juspay/hyperswitch

- **解决什么问题**：开源可组合支付平台，支持多支付、支付、欺诈、金库和代币化提供商连接，提供智能路由和成本可观测性。
- **为什么值得关注**：45k stars，7d +1508，Rust 编写，Apache-2.0。是金融科技基础设施中少有的高增长开源项目。
- **技术栈/架构亮点**：Rust 高性能，支付编排、智能路由、对账、欺诈检测一体化。
- **是否适合借鉴**：适合。支付编排和风控架构对金融科技产品有直接参考价值。
- **可能风险**：PCI 合规复杂，自托管需承担合规责任。

### 3.8 ZhuLinsen/daily_stock_analysis

- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，支持多源行情、实时新闻、决策看板和自动推送，支持零成本定时运行。
- **为什么值得关注**：65k stars，forks 高达 54898，说明有大量用户实际部署和二次开发。MIT 协议。
- **技术栈/架构亮点**：Python + LLM + 多源数据 + 定时任务。强调“零成本”运行，适合个人和小团队。
- **是否适合借鉴**：适合。其数据工程流水线和自动报告生成模式可直接复用到企业级投研 Agent。
- **可能风险**：数据源稳定性；LLM 分析结论的可靠性；不应作为投资决策唯一依据。

### 3.9 shiyu-coder/Kronos

- **解决什么问题**：构建“金融市场语言的基础模型”，试图用 foundation model 的方式建模金融数据。
- **为什么值得关注**：39k stars，24h +113。金融基础模型是量化研究的前沿方向。
- **技术栈/架构亮点**：Python，具体架构信息不足。
- **是否适合借鉴**：研究方向值得关注，但项目细节和可复现性信息不足。
- **可能风险**：金融基础模型的理论基础尚不成熟；回测过拟合风险极高；维护活跃度存疑（最近 push 在 2026-04）。

### 3.10 virattt/ai-hedge-fund

- **解决什么问题**：模拟 AI 对冲基金团队，通过多个 AI Agent 扮演不同角色进行投资决策。
- **为什么值得关注**：63k stars，是 AI 交易领域的经典项目，持续有更新。
- **技术栈/架构亮点**：Python + 多 Agent 角色扮演。概念简洁但影响力大。
- **是否适合借鉴**：适合作为多 Agent 投研流程的教学和原型参考。
- **可能风险**：研究工具属性，回测结果不代表实盘表现；不应直接用于实盘。

## 4. 趋势归纳

### 技术趋势

1. **本地推理引擎崛起**：colibri、magnitude、needle、ds4 等项目集中出现，强调在自有硬件上运行模型，反映金融场景对数据隐私和低延迟的强烈需求。
2. **MCP 生态快速扩张**：awesome-mcp-servers、tradingview-mcp、QuantDinger 等项目表明 MCP 正在成为 AI Agent 与金融数据、交易系统连接的标准协议。
3. **Rust 在金融基础设施中的渗透**：hyperswitch、magnitude 等项目采用 Rust，高性能和内存安全成为金融基础设施的优先选择。
4. **Token 压缩与上下文工程**：headroom 等项目专注于降低 LLM 推理成本，对高频金融分析场景有直接价值。

### 产品趋势

1. **AI 交易从“框架”走向“OS”和“SaaS”**：QuantDinger 的“交易 OS”定位、多租户 SaaS 架构，表明 AI 交易正在产品化。
2. **AI Agent 治理独立成赛道**：iFixAi 的爆发说明市场对 Agent 审计、对齐、合规的需求正在形成独立产品类别。
3. **本地优先 + 自托管**：OpenStock、tick-stock-panel、PanWatch 等项目强调自托管和本地优先，反映用户对数据控制权的重视。
4. **设计系统与 Agent 结合**：ui-ux-pro-max-skill、awesome-design-md、open-design 等项目表明“让 Agent 生成一致 UI”正在成为新的产品方向。

### 量化/交易策略趋势

1. **LLM 多智能体决策**：TradingAgents、Vibe-Trading、ai-hedge-fund 等项目持续增长，多 Agent 分工成为主流范式。
2. **金融基础模型探索**：Kronos 等项目尝试用 foundation model 方法建模金融市场，是值得关注的研究方向。
3. **A股/港股/美股多市场覆盖**：PanWatch、daily_stock_analysis、easy-stock 等项目集中出现，反映中文市场对 AI 投研工具的需求。

### AI Agent 与自动化交易结合趋势

1. **Agent 决策 + 人工监督**：iFixAi 的审计框架与交易 Agent 的结合，可能成为未来合规自动化交易的标准架构。
2. **MCP 作为交易数据接入标准**：tradingview-mcp、QuantDinger 等项目表明 MCP 正在成为 Agent 获取行情和执行交易的标准接口。
3. **边缘 Agent 决策**：needle 等项目探索在微型设备上运行自动化决策模型，可能催生低延迟、分布式交易决策架构。

### 值得后续做原型验证的方向

1. **交易 Agent 审计流水线**：参考 iFixAi，构建针对交易 Agent 的行为审计和合规检查系统。
2. **本地推理 + 金融数据分析**：参考 colibri/magnitude，验证在本地硬件上运行金融分析模型的可行性。
3. **MCP 金融数据网关**：参考 tradingview-mcp，构建统一的金融数据 MCP 服务器。
4. **多 Agent 投研工作台**：参考 TradingAgents + PanWatch，构建多市场、多角色的投研 Agent 系统。

## 5. 今日灵感清单

1. **MVP：交易 Agent 行为审计器**：参考 iFixAi，构建一个轻量级工具，监控交易 Agent 的决策日志，检测异常行为、偏离策略和潜在合规问题。可先支持日志分析和规则引擎，再逐步引入 LLM 审计。

2. **MVP：本地金融数据分析 Agent**：参考 colibri + OpenBB，构建一个完全本地运行的金融数据分析 Agent，使用本地推理引擎处理行情数据，确保数据不出本机。

3. **调研：MCP 在金融数据接入中的标准化程度**：调研 awesome-mcp-servers 中金融相关 MCP 服务器的覆盖范围、数据质量和维护活跃度，评估是否值得构建统一的金融 MCP 网关。

4. **调研：金融基础模型的可行性**：深入研究 Kronos 的技术路线，评估“金融市场语言基础模型”是否具备可复现性，以及与传统量化模型的差异。

5. **Codex/Agent 自动复现 demo：多 Agent 投研流水线**：参考 TradingAgents 和 ai-hedge-fund，让 Codex 自动生成一个简化的多 Agent 投研 demo，包含研究、风险、交易三个角色，输出结构化决策报告。

6. **MVP：自托管 A股量化工作台**：参考 tick-stock-panel 和 PanWatch，构建一个自托管的 A股选股 + 监控 + 回测工作台，使用 DuckDB/Polars 处理数据，LLM 生成分析报告。

7. **调研：Token 压缩在金融分析中的应用**：评估 headroom 的压缩技术是否能在不损失关键信息的前提下降低金融数据分析的 LLM 成本。

8. **Watchlist：iFixAi、QuantDinger、TradingAgents、OpenBB、colibri**：这些项目代表了 AI 交易、Agent 治理、数据基础设施和本地推理的前沿方向，值得持续跟踪。

9. **MVP：支付编排模拟器**：参考 hyperswitch 的架构，构建一个简化的支付编排模拟器，验证智能路由和成本可观测性的设计思路。

10. **调研：边缘 Agent 在交易决策中的可行性**：研究 needle 的微型设备自动化模型，评估在低延迟交易场景中使用边缘 Agent 的技术可行性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | AI 交易多 Agent 框架的标杆，持续高增长，架构可借鉴 |
| ifixai-ai/iFixAi | AI Agent 治理赛道爆发点，金融合规审计直接相关 |
| OpenByteInc/QuantDinger | 交易 SaaS 化架构独特，研究到实盘完整链路 |
| OpenBB-finance/OpenBB | 金融数据基础设施，AI Agent 数据层参考 |
| JustVugg/colibri | 本地推理引擎，金融数据隐私场景关键基础设施 |
| juspay/hyperswitch | 支付编排架构，金融科技基础设施高增长项目 |
| HKUDS/Vibe-Trading | AI 交易产品化方向，需观察其策略严谨性 |
| shiyu-coder/Kronos | 金融基础模型前沿探索，研究方向值得跟踪 |
| ZhuLinsen/daily_stock_analysis | 数据工程流水线参考，中文市场 AI 投研代表 |
| atilaahmettaner/tradingview-mcp | MCP 金融数据接入标准化趋势代表 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供（baseline_1d: 2026-09-27.json），1 日涨星数据完整。
- **7 日基线**：已提供（baseline_7d: 2026-09-21.json），7 日涨星数据完整。
- **30 日基线**：未提供，所有项目的 star_delta_30d 均为 null，无法评估 30 日趋势。
- **采集失败**：未发现明显采集失败，但部分项目（如 easy-stock）的 7 日涨星为 null，可能是新项目或基线缺失。
- **样本偏差**：候选项目通过特定查询词（如 “algorithmic trading”、“crypto trading”、“quant” 等）筛选，导致大量 awesome-list 类项目（如 awesome-python、awesome-go）因 README 或 topic 命中而进入候选，实际与金融/量化交易的直接相关性参差不齐。报告已尽量区分“直接相关”和“间接相关”项目。
- **分类偏差**：部分项目的 category_guess 与项目实际内容存在偏差（如 build-your-own-x 被标记为 trading_bot），分析时已基于项目实际描述进行判断。
