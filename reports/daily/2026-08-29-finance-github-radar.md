# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-29

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 交易框架**：TradingAgents、Vibe-Trading、QuantDinger、OpenAlice 等项目持续高增，多智能体 LLM 交易框架成为最热主线。
  2. **AI 投研与数据工作台**：daily_stock_analysis、a-stock-data、Vibe-Research、ai-berkshire 等项目显示“AI Agent + 金融数据 + 投研流程”正在快速产品化。
  3. **Agent 工程基础设施**：OpenBot、ruflo、headroom、iFixAi、planning-with-files 等项目反映 Agent 治理、上下文压缩、审计与规划能力正在成为通用底座，并外溢到金融场景。

- **是否出现新趋势**：出现。AI Agent 正在从“通用编码助手”向“金融投研/交易专用 Agent”分化，同时“Agent 审计/治理/上下文工程”成为独立热点。A 股本地化数据工具与投研 Agent 项目明显增多。

- **是否出现值得复刻/参考的工程架构**：是。TradingAgents 的多智能体辩论式决策、nautilus_trader 的 Rust 事件驱动交易引擎、OpenBot 的“每个 Agent 一台电脑”的治理模型、headroom 的 LLM 上下文压缩代理、iFixAi 的 Agent 独立审计，均具备较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明确骗局，但存在大量“vibe coding / AI skill / awesome list”类项目因关键词误匹配进入榜单，与金融交易无直接关系。部分 AI 交易项目（如 Vibe-Trading、QuantDinger、OpenAlice）营销话术较强，需警惕策略过拟合与实盘风险。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 472894 | +402 | +4233 | Python | API 资源 | 免费 API 合集 | 数据源发现 | 中 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 123011 | +341 | +3118 | Python | AI 设计 | AI UI/UX 设计技能 | 金融产品前端 | 低 |
| 3 | TauricResearch/TradingAgents | 101747 | +120 | +2448 | Python | AI 交易 | 多智能体 LLM 交易框架 | 高 | 低 |
| 4 | nexu-io/open-design | 92671 | +201 | +2215 | 未知 | AI 设计 | 本地优先 AI 设计引擎 | 金融看板原型 | 低 |
| 5 | awesome-dsh-plugin/awesome-dsh-plugin | 13574 | +130 | +2032 | Python | 插件列表 | DeepSeek Harness 插件列表 | 工具链调研 | 低 |
| 6 | ripienaar/free-for-dev | 135908 | +107 | +1970 | HTML | 资源列表 | SaaS/PaaS 免费层列表 | 基础设施选型 | 低 |
| 7 | codecrafters-io/build-your-own-x | 543942 | +175 | +1801 | Markdown | 教程 | 从零复刻技术 | 交易系统复刻 | 中 |
| 8 | awesome-selfhosted/awesome-selfhosted | 316040 | +186 | +1668 | 未知 | 自托管 | 自托管服务列表 | 自托管交易栈 | 中 |
| 9 | VoltAgent/awesome-design-md | 111291 | +152 | +1572 | 未知 | 设计系统 | DESIGN.md 设计系统集合 | Agent UI 规范 | 中 |
| 10 | vinta/awesome-python | 317056 | +222 | +1515 | Python | 资源列表 | Python 工具精选 | 量化工具选型 | 低 |
| 11 | CopilotKit/OpenBot | 3457 | +119 | +1120 | TypeScript | Agent 治理 | 每个 Agent 一台电脑 | Agent 安全架构 | 中 |
| 12 | cactus-compute/needle | 9690 | +91 | +1097 | Python | 端侧模型 | 14MB 端侧基础模型 | 低延迟推理 | 中 |
| 13 | unslothai/unsloth | 75200 | +105 | +793 | Python | LLM 训练 | 本地 LLM 训练/微调 | 金融 LLM 微调 | 低 |
| 14 | ruvnet/ruflo | 69750 | +78 | +882 | TypeScript | Agent 框架 | Agent 元编排框架 | 多 Agent 编排 | 低 |
| 15 | headroomlabs-ai/headroom | 68031 | +82 | +826 | Python | 上下文压缩 | LLM 输出压缩 | 降低 token 成本 | 低 |
| 16 | avelino/awesome-go | 182658 | +89 | +675 | Go | 资源列表 | Go 框架精选 | Go 交易系统选型 | 中 |
| 17 | HKUDS/Vibe-Trading | 32074 | +77 | +594 | Python | AI 交易 | 个人交易 Agent | 多 Agent 交易 | 中 |
| 18 | ZhuLinsen/daily_stock_analysis | 64282 | +52 | +642 | Python | AI 投研 | 多市场股票分析系统 | 投研 Agent 产品化 | 低 |
| 19 | JustVugg/colibri | 26435 | +59 | +566 | C | 模型推理 | 纯 C 的 MoE 推理引擎 | 低资源推理 | 低 |
| 20 | nautechsystems/nautilus_trader | 28113 | +68 | +793 | Rust | 交易引擎 | Rust 事件驱动交易引擎 | 高 | 中 |
| 21 | nidhinjs/prompt-master | 12010 | +85 | +394 | 未知 | Prompt 工程 | 精准 Prompt 生成 | 投研提示词 | 低 |
| 22 | punkpeye/awesome-mcp-servers | 93072 | +58 | +371 | 未知 | MCP | MCP Server 合集 | 金融 MCP 工具 | 低 |
| 23 | hesreallyhim/awesome-claude-code | 53206 | +50 | +374 | Python | Agent 资源 | Claude Code 资源 | Agent 技能调研 | 低 |
| 24 | ifixai-ai/iFixAi | 11432 | +92 | +180 | Python | Agent 审计 | AI Agent 独立审计 | 交易 Agent 风控 | 低 |
| 25 | goldmansachs/gs-quant | 12818 | +22 | +586 | Python | 量化金融 | 高盛量化工具包 | 衍生品定价 | 低 |
| 26 | garrytan/gbrain | 29296 | +39 | +354 | TypeScript | Agent 框架 | 个人 Agent 大脑 | Agent 记忆架构 | 低 |
| 27 | vnpy/vnpy | 44893 | +58 | +205 | Python | 量化平台 | Python 量化交易框架 | 国内量化生态 | 低 |
| 28 | OpenBB-finance/OpenBB | 72465 | +44 | +299 | Python | 金融数据 | 开放金融数据平台 | 数据层标准化 | 中 |
| 29 | simonlin1212/a-stock-data | 9341 | +42 | +295 | 未知 | A 股数据 | A 股全栈数据工具包 | A 股数据接入 | 低 |
| 30 | perixtar/Tech-OA-Interview-Questions | 4702 | +26 | +473 | Python | 面试题 | 科技公司 OA 题集 | 无关 | 低 |
| 31 | cinar/indicator | 1566 | +62 | +338 | Go | 技术指标 | Go 技术指标与回测 | 轻量回测 | 低 |
| 32 | code-yeongyu/oh-my-openagent | 68514 | +24 | +263 | TypeScript | Agent 工具 | 编码 Agent 编排 | Agent 编排 | 低 |
| 33 | OpenByteInc/QuantDinger | 11217 | +39 | +268 | Python | AI 交易 | AI 量化交易平台 | 多市场交易 | 中 |
| 34 | Developer-Y/cs-video-courses | 83250 | +52 | +99 | 未知 | 课程 | CS 视频课程列表 | 无关 | 中 |
| 35 | RyanCodrai/turbovec | 16524 | +27 | +287 | Rust | 向量索引 | Rust 向量索引 | 因子向量检索 | 低 |
| 36 | antirez/ds4 | 21919 | +24 | +252 | C | 模型推理 | DeepSeek 本地推理引擎 | 本地推理 | 低 |
| 37 | xbtlin/ai-berkshire | 15987 | +26 | +224 | Python | AI 投研 | 价值投资多 Agent 框架 | 投研方法论 | 低 |
| 38 | fffaraz/awesome-cpp | 73009 | +25 | +131 | 未知 | 资源列表 | C++ 资源精选 | 低延迟系统选型 | 低 |
| 39 | questflowai/investorskills | 1645 | +47 | +186 | Swift | 投研技能 | 投资判断结构化技能库 | 投研知识工程 | 低 |
| 40 | ai-boost/awesome-harness-engineering | 3900 | +23 | +202 | Python | Agent 工程 | Agent harness 工程列表 | Agent 架构调研 | 低 |
| 41 | rust-unofficial/awesome-rust | 59053 | +21 | +109 | Rust | 资源列表 | Rust 资源精选 | Rust 交易栈 | 低 |
| 42 | TraderAlice/OpenAlice | 6836 | +16 | +195 | TypeScript | AI 交易 | 全资产 AI 交易 Agent | 全流程交易 Agent | 中 |
| 43 | josephmisiti/awesome-machine-learning | 74213 | +10 | +94 | Python | 资源列表 | ML 资源精选 | ML 选型 | 低 |
| 44 | shy3130/tick-stock-panel | 3965 | +45 | 信息不足 | Python | A 股量化 | A 股选股/监控/回测工作台 | A 股量化工作台 | 低 |
| 45 | simonlin1212/Vibe-Research | 2242 | +35 | +78 | TypeScript | AI 投研 | 个人投研 Agent | 投研 Agent 产品化 | 低 |
| 46 | OthmanAdi/planning-with-files | 26416 | +7 | +127 | Shell | Agent 规划 | 文件式 Agent 规划 | 长任务可靠性 | 低 |
| 47 | virattt/ai-hedge-fund | 63088 | +10 | +88 | Python | AI 交易 | AI 对冲基金团队 | 多角色投研 | 低 |
| 48 | awesomedata/awesome-public-datasets | 78709 | +14 | 信息不足 | 未知 | 数据集 | 公开数据集列表 | 数据源发现 | 中 |
| 49 | vuejs/awesome-vue | 73549 | +2 | +9 | 未知 | 资源列表 | Vue 资源精选 | 无关 | 低 |
| 50 | ByteByteGoHq/system-design-101 | 87721 | +23 | +285 | 未知 | 系统设计 | 系统设计图解 | 交易系统架构 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，通过多个专业 Agent（如基本面、技术面、情绪面、风控等）辩论式分析，生成交易信号。
- **为什么值得关注**：7 日涨星 +2448，总 star 超 10 万，是当前“AI 交易 Agent”方向最具代表性的开源项目之一。Apache-2.0 协议，适合研究。
- **技术栈/架构亮点**：Python + 多 Agent 框架，topic 包含 agent、finance、llm、multiagent、trading。核心价值在于“多角色辩论 + 决策合成”的架构模式。
- **是否适合借鉴**：适合。其多 Agent 角色分工与辩论机制可迁移到企业级投研 Agent、风控委员会模拟、策略评审等场景。
- **可能风险**：定位为研究工具，策略有效性未经实盘验证；LLM 决策存在幻觉与过拟合风险；open_issues 392，维护活跃度需观察。

### 3.2 nautechsystems/nautilus_trader
- **解决什么问题**：提供生产级 Rust 原生交易引擎，强调确定性事件驱动架构，覆盖回测与实盘。
- **为什么值得关注**：7 日涨星 +793，Rust 语言，LGPL-3.0。在 AI 交易项目泛滥的背景下，它是少数聚焦“交易引擎正确性”的底层基础设施项目。
- **技术栈/架构亮点**：Rust 实现核心引擎，Python 作为上层接口；确定性事件驱动架构有利于回测与实盘一致性；覆盖 crypto、equity、forex、futures、options 多资产。
- **是否适合借鉴**：非常适合。若自建交易系统，其“回测与实盘同一事件循环”的设计是避免回测偏差的关键工程实践。
- **可能风险**：LGPL-3.0 协议对闭源商用有约束；涉及杠杆/网格相关标记，实盘风险高；学习曲线陡峭。

### 3.3 HKUDS/Vibe-Trading
- **解决什么问题**：定位“个人交易 Agent”，将 AI Agent 直接用于交易决策与执行。
- **为什么值得关注**：7 日涨星 +594，HKUDS 出品，topic 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent，是学术机构向应用层延伸的代表。
- **技术栈/架构亮点**：Python + MCP + 多 Agent，强调“vibe trading”的低门槛体验。
- **是否适合借鉴**：部分适合。其 MCP 集成与多 Agent 交易流程可参考，但“vibe trading”定位本身偏营销，不宜直接作为策略依据。
- **可能风险**：crypto_related，策略过拟合风险高；MIT 协议但学术项目维护持续性存疑；不建议直接实盘。

### 3.4 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：7 日涨星 +642，forks 高达 53898，说明存在大量二次开发与部署需求。A 股场景 + LLM 分析的产品化程度较高。
- **技术栈/架构亮点**：Python，topic 覆盖 a-stock、ai-agent、llm、quant。核心价值在于“数据聚合 + LLM 分析 + 定时推送”的闭环。
- **是否适合借鉴**：适合。可作为“AI 投研日报/监控 Agent”的 MVP 参考，尤其是零成本定时运行与推送机制。
- **可能风险**：数据源稳定性与合规性需关注；LLM 分析结论不可作为投资依据；forks 高但需甄别是否被用于灰产或营销。

### 3.5 CopilotKit/OpenBot
- **解决什么问题**：为每个 AI Agent 提供独立的“电脑”——浏览器、文件、工具，所有动作先决策后执行并记录，支持任意 AG-UI Agent 接入。
- **为什么值得关注**：7 日涨星 +1120，虽然总 star 仅 3457，但增速极快。它代表“Agent 治理与可观测性”这一新兴基础设施方向。
- **技术栈/架构亮点**：TypeScript，topic 包含 ag-ui、agent-governance、browser-automation、mcp、generative-ui。核心是“动作预决策 + 事后记录”的治理模型。
- **是否适合借鉴**：非常适合。交易 Agent 尤其需要“先决策、后执行、全记录”的审计链路，OpenBot 的治理思路可直接迁移到自动化交易系统的权限与审计层。
- **可能风险**：项目较新，生态与稳定性待验证；浏览器自动化在金融场景存在合规与安全边界问题。

### 3.6 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 处理前压缩工具输出、日志、文件与 RAG 分块，降低 token 消耗，同时保持回答质量。
- **为什么值得关注**：7 日涨星 +826，总 star 68031。在金融 Agent 需要处理大量行情、新闻、研报数据的场景下，上下文成本是核心瓶颈。
- **技术栈/架构亮点**：Python，提供库、代理与 MCP server 三种形态；宣称 JSON 场景可减少 60-95% token。
- **是否适合借鉴**：适合。可用于金融数据管道与 Agent 之间的“上下文压缩层”，降低长上下文投研 Agent 的成本。
- **可能风险**：压缩可能损失关键信息，金融场景需验证压缩后决策一致性；依赖上游 LLM 行为。

### 3.7 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审，120 秒内给出结论。
- **为什么值得关注**：7 日涨星 +180，但 24h 涨星 +92，短期热度高。topic 覆盖 ai-governance、ai-safety、iso-42001、nist-ai-rmf、prompt-injection，直接对应企业级 Agent 合规需求。
- **技术栈/架构亮点**：Python，Apache-2.0。将 AI 治理、安全评估、幻觉检测、提示注入检测整合为可执行审计工具。
- **是否适合借鉴**：非常适合。自动化交易 Agent 上线前需要独立审计与持续监控，iFixAi 的审计框架可作为风控 Agent 的参考实现。
- **可能风险**：审计本身依赖 LLM，存在误判；金融场景需结合业务规则而非仅依赖通用审计。

### 3.8 goldmansachs/gs-quant
- **解决什么问题**：高盛开源的 Python 量化金融工具包，覆盖衍生品定价、风险与交易策略。
- **为什么值得关注**：7 日涨星 +586，机构级背景，Apache-2.0。在 AI 交易项目泛滥时，它是少数具备机构定价与风控能力的参考实现。
- **技术栈/架构亮点**：Python，topic 覆盖 derivatives、risk-management、trading-strategies。核心价值在于衍生品定价与风控模型的工程化。
- **是否适合借鉴**：适合。可用于衍生品定价、风险指标计算、结构化产品分析等场景的原型验证。
- **可能风险**：与高盛平台深度绑定，部分功能可能依赖其服务；学习曲线较陡。

### 3.9 xbtlin/ai-berkshire
- **解决什么问题**：基于 Claude Code / Codex 的价值投资研究框架，整合巴菲特、芒格、段永平、李录四套方法论，多 Agent 并行研究。
- **为什么值得关注**：7 日涨星 +224，将“投资方法论”显式化为 Agent 可执行的研究流程，是“投研知识工程”的代表。
- **技术栈/架构亮点**：Python，topic 覆盖 ai-agent、claude-code、mcp、fundamental-analysis、value-investing。核心是“多大师方法论 + 多 Agent 对抗分析”。
- **是否适合借鉴**：适合。其“方法论结构化 + 多 Agent 对抗”思路可迁移到企业投研流程、尽调 Agent、投资备忘录自动生成等场景。
- **可能风险**：价值投资方法论本身主观性强，LLM 输出可能流于表面；需警惕“伪深度研究”。

### 3.10 OpenByteInc/QuantDinger
- **解决什么问题**：面向 crypto、股票、外汇的 AI 量化交易平台，集成回测、实盘、行情与多 Agent 研究。
- **为什么值得关注**：7 日涨星 +268，topic 覆盖 alpaca、binance、coinbase、mcp-server，体现“多市场 + 多交易所 + MCP”的集成趋势。
- **技术栈/架构亮点**：Python，Apache-2.0。核心价值在于多市场数据与交易接口的统一抽象。
- **是否适合借鉴**：部分适合。其多交易所适配与 MCP server 设计可参考，但整体偏“全家桶”式平台，耦合度可能较高。
- **可能风险**：crypto_related，涉及真实交易所接口，API key 安全风险高；策略有效性未经验证；不建议直接实盘。

## 4. 趋势归纳

- **技术趋势**：
  - **多智能体 LLM 交易框架成为主流范式**：TradingAgents、Vibe-Trading、QuantDinger、OpenAlice、ai-hedge-fund 均采用多 Agent 分工协作。
  - **Rust 在交易基础设施中地位上升**：nautilus_trader、turbovec 等项目显示 Rust 正从“高性能替代”走向“交易引擎默认选择”。
  - **MCP 成为金融 Agent 的标准接口**：Vibe-Trading、QuantDinger、ai-berkshire、awesome-mcp-servers 均围绕 MCP 构建工具生态。
  - **上下文工程与 Agent 治理独立成层**：headroom、planning-with-files、iFixAi、OpenBot 显示“压缩、规划、审计、治理”正在形成 Agent 基础设施栈。

- **产品趋势**：
  - **从“策略库”转向“投研工作台”**：daily_stock_analysis、Vibe-Research、tick-stock-panel 强调看板、推送、复盘、持仓管理，而非单纯回测。
  - **A 股本地化工具链快速成熟**：a-stock-data、tick-stock-panel、daily_stock_analysis 显示 A 股数据接入与 Agent 化需求旺盛。
  - **“方法论即产品”**：ai-berkshire、investorskills 将投资方法论结构化为可复用技能，形成差异化产品。

- **量化/交易策略趋势**：
  - **LLM 信号与传统量化融合**：多数项目仍以 LLM 分析为主，真正与统计套利、因子模型深度融合的案例较少。
  - **回测与实盘一致性受重视**：nautilus_trader 的确定性事件驱动架构是这一趋势的代表。
  - **多资产覆盖成为标配**：crypto、股票、外汇、期货、期权多资产支持成为新项目的默认能力。

- **AI Agent 与自动化交易结合趋势**：
  - **“研究 Agent”与“执行 Agent”分离**：ai-berkshire、Vibe-Research 聚焦研究，OpenAlice、QuantDinger 覆盖执行，分层趋势明显。
  - **Agent 审计与风控开始被纳入交易流程**：iFixAi、OpenBot 的治理能力为交易 Agent 上线提供了合规基础。
  - **本地化与端侧推理**：needle、ds4、colibri 等项目显示低延迟、低资源推理可能成为交易 Agent 的边缘部署方向。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据 Agent 工具层。
  - 多 Agent 投研辩论 + 独立审计风控的闭环。
  - Rust 事件驱动回测引擎与 Python 策略层的混合架构。
  - LLM 上下文压缩在金融长文档分析中的效果验证。

## 5. 今日灵感清单

1. **MVP：AI 投研日报 Agent**：参考 daily_stock_analysis，用 MCP 接入行情与新闻，定时生成多市场日报并推送，先做“只读分析、不执行交易”的版本。
2. **调研：MCP 金融工具生态**：基于 awesome-mcp-servers 与 a-stock-data，梳理可复用的金融数据 MCP server，评估数据质量与合规性。
3. **Demo：多 Agent 辩论式策略评审**：参考 TradingAgents，让 Codex 复现“基本面/技术面/风控三 Agent 辩论 + 投票”的决策流程，仅用于研究。
4. **原型：交易 Agent 审计层**：参考 iFixAi 与 OpenBot，为自动化交易 Agent 增加“动作预决策 + 事后记录 + 独立审计”的治理模块。
5. **验证：LLM 上下文压缩对金融分析的影响**：用 headroom 对研报、新闻、行情 JSON 做压缩，对比压缩前后 LLM 分析结论的一致性。
6. **架构：Rust 回测引擎 + Python 策略层**：调研 nautilus_trader 的事件驱动架构，评估是否可抽取其“确定性回测”设计用于内部原型。
7. **产品：投资方法论技能包**：参考 ai-berkshire 与 investorskills，将一套内部投研方法论结构化为 Agent 可执行的 skill 文件。
8. **数据：A 股数据管道标准化**：参考 a-stock-data 的“11 层架构、54 端点、19 数据源”，设计统一的数据接入层，避免多源数据格式不一致。
9. **Watchlist：OpenBot、iFixAi、headroom**：这三个项目代表 Agent 治理、审计与上下文工程的前沿，值得持续跟踪其架构演进。
10. **安全：API Key 隔离与权限最小化**：针对 QuantDinger、OpenAlice 等多交易所项目，设计“只读 API + 白名单 + 人工确认执行”的安全沙箱。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | 多智能体交易框架标杆，架构演进值得持续跟踪 |
| nautechsystems/nautilus_trader | 生产级 Rust 交易引擎，回测/实盘一致性设计优秀 |
| CopilotKit/OpenBot | Agent 治理与可观测性新方向，增速极快 |
| ifixai-ai/iFixAi | AI Agent 独立审计，直接对应交易 Agent 合规需求 |
| headroomlabs-ai/headroom | LLM 上下文压缩，金融长文档场景成本优化关键 |
| goldmansachs/gs-quant | 机构级衍生品定价与风控参考 |
| HKUDS/Vibe-Trading | 学术机构 AI 交易 Agent 应用化样本 |
| ZhuLinsen/daily_stock_analysis | A 股 AI 投研产品化程度高，forks 活跃 |
| simonlin1212/a-stock-data | A 股数据工具包，数据层标准化参考 |
| xbtlin/ai-berkshire | 投资方法论结构化与多 Agent 对抗研究 |
| OpenByteInc/QuantDinger | 多市场多交易所 AI 交易平台，集成趋势样本 |
| virattt/ai-hedge-fund | 经典 AI 对冲基金多角色架构，社区活跃 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d: 2026-08-28.json` 与 `baseline_7d: 2026-08-22.json`，基线文件存在，1 日与 7 日涨星数据基本完整。
- **缺失数据**：`star_delta_30d` 在所有项目中均为 `null`，无法提供 30 日涨星趋势。部分项目（tick-stock-panel、awesome-public-datasets）的 `star_delta_7d` 为 `null`，7 日涨星信息不足。
- **采集失败**：未发现明确采集失败标记，但 `language` 字段存在多个 `null` 值，部分项目语言信息缺失。
- **样本偏差**：候选集由关键词搜索生成，存在明显误匹配。大量 awesome-list、AI 设计、面试题、系统设计类项目因描述或 readme 中偶然出现“quant”“fintech”“trading bot”等词被纳入，与金融/量化交易无直接关系。真正与交易直接相关的项目约占候选集的 30-40%。此外，候选集偏向高 star、高增速项目，可能遗漏低 star 但技术价值高的早期项目。
