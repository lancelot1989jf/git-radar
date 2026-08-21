# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-20

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：`iFixAi` 以 7 日 +2511 星快速上升，聚焦 AI Agent 的独立审计、幻觉检测、提示注入检测，直接对应金融场景中 Agent 行为合规与风控需求。
  2. **多 Agent 金融投研框架**：`TradingAgents`（99k stars）、`Vibe-Trading`（31k stars）、`ai-berkshire`、`TradingAgents-astock` 等持续升温，LLM 多角色辩论式投研成为明确产品化方向。
  3. **本地优先 / 端侧 AI 推理**：`unsloth`、`needle`、`colibri`、`ds4` 等项目反映“小模型 + 本地推理 + 低资源部署”趋势，对金融数据隐私和低延迟推理有借鉴意义。

- **是否出现新趋势**：出现。AI Agent 的“可审计性”开始成为独立赛道，`iFixAi` 的快速涨星说明市场从“能跑 Agent”转向“能证明 Agent 做对了”。同时，A 股本地化多 Agent 投研工具（`daily_stock_analysis`、`tickflow-stock-panel`、`a-stock-data`、`TradingAgents-astock`）形成集群，中文金融 AI 工具链正在快速成熟。

- **是否出现值得复刻/参考的工程架构**：是。`nautilus_trader` 的 Rust 原生确定性事件驱动交易引擎、`TradingAgents` 的多 Agent 辩论决策架构、`headroom` 的 LLM 上下文压缩代理、`turbovec` 的 Rust + Python 绑定向量索引，均具备工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但存在大量“awesome-list”类项目因关键词误匹配进入榜单（如 `public-apis`、`build-your-own-x`、`awesome-go` 等），其实际与金融交易无关。`Financial_freedom` 描述为“最全赚钱投资指南”，属典型营销话术，需谨慎对待。所有标注 `trading_bot`、`crypto_related` 的项目均不应直接实盘运行。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 467276 | +1154 | +11274 | Python | API 资源列表 | 免费 API 合集，非交易项目 | 低，误匹配 | 中 |
| 2 | nexu-io/open-design | 89778 | +428 | +4158 | TypeScript | AI 设计工具 | 本地优先 AI 设计引擎，可导出 HTML/PDF/PPTX | 中，Agent 生成金融看板 UI | 低 |
| 3 | unslothai/unsloth | 74109 | +229 | +2995 | Python | LLM 微调/推理 | 本地运行和训练 LLM 的 UI | 高，本地化金融 LLM | 低 |
| 4 | nextlevelbuilder/ui-ux-pro-max-skill | 118839 | +565 | +2353 | Python | AI 设计技能 | 多平台 UI/UX 设计智能技能 | 中，金融产品原型 | 低 |
| 5 | cactus-compute/needle | 8140 | +303 | +3119 | Python | 端侧模型 | 14MB 端侧基础模型 | 高，低延迟端侧推理 | 中 |
| 6 | ifixai-ai/iFixAi | 11043 | +68 | +2511 | Python | AI Agent 审计 | 120 秒内审计 AI Agent 行为 | 极高，Agent 风控/合规 | 低 |
| 7 | codecrafters-io/build-your-own-x | 541626 | +295 | +2134 | Markdown | 教程合集 | 从零复刻技术的教程列表 | 低，误匹配 | 中 |
| 8 | awesome-selfhosted/awesome-selfhosted | 313986 | +197 | +1495 | 无 | 自托管列表 | 自托管服务列表 | 低，误匹配 | 中 |
| 9 | vinta/awesome-python | 315168 | +186 | +1338 | Python | Python 资源列表 | Python 工具精选 | 低，误匹配 | 低 |
| 10 | VoltAgent/awesome-design-md | 109463 | +148 | +1158 | 无 | 设计系统 | DESIGN.md 设计系统合集 | 中，Agent UI 规范 | 中 |
| 11 | RyanCodrai/turbovec | 15967 | +313 | +1208 | Rust | 向量索引 | Rust 向量索引，Python 绑定 | 高，金融 RAG/向量检索 | 低 |
| 12 | JustVugg/colibri | 25621 | +103 | +1079 | C | MoE 推理引擎 | 纯 C 零依赖 MoE 模型推理 | 中，低资源推理 | 低 |
| 13 | TauricResearch/TradingAgents | 99071 | +102 | +1038 | Python | 多 Agent 交易 | LLM 多 Agent 金融交易框架 | 极高，投研 Agent 架构 | 低 |
| 14 | nautechsystems/nautilus_trader | 26720 | +259 | +1250 | Rust | 交易引擎 | Rust 原生事件驱动交易引擎 | 极高，交易系统架构 | 中 |
| 15 | ZhuLinsen/daily_stock_analysis | 63512 | +120 | +751 | Python | A 股分析 | LLM 多市场股票分析系统 | 高，A 股数据管道 | 低 |
| 16 | headroomlabs-ai/headroom | 67016 | +107 | +766 | Python | 上下文压缩 | LLM 输出压缩，省 token | 高，降低 Agent 成本 | 低 |
| 17 | avelino/awesome-go | 181731 | +132 | +726 | Go | Go 资源列表 | Go 框架库精选 | 低，误匹配 | 中 |
| 18 | ripienaar/free-for-dev | 132404 | +172 | +688 | HTML | 免费资源 | 开发者免费资源列表 | 低，误匹配 | 低 |
| 19 | ruvnet/ruflo | 68514 | +142 | +708 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | 高，Agent 工作流 | 低 |
| 20 | codeman008/Financial_freedom | 3159 | +34 | +1166 | 无 | 投资指南 | “最全赚钱投资指南” | 低，营销话术 | 中 |
| 21 | HKUDS/Vibe-Trading | 31359 | +65 | +560 | Python | AI 交易 Agent | 个人交易 Agent | 高，Agent 交易闭环 | 中 |
| 22 | shy3130/tickflow-stock-panel | 3301 | +94 | +468 | Python | A 股量化工作台 | 自托管选股+监控+回测 | 高，A 股量化 MVP | 低 |
| 23 | hesreallyhim/awesome-claude-code | 52725 | +66 | +458 | Python | Claude 资源 | Claude Code 资源精选 | 中，Agent 技能 | 低 |
| 24 | langfuse/langfuse | 33485 | +77 | +414 | TypeScript | LLM 可观测性 | LLM 评估、监控、指标 | 高，Agent 生产监控 | 低 |
| 25 | garrytan/gbrain | 28825 | +60 | +428 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 框架 | 中，Agent 编排 | 低 |
| 26 | questflowai/investorskills | 1461 | +197 | +488 | Swift | 投资技能库 | 投资判断结构化技能库 | 高，投研知识结构化 | 低 |
| 27 | lukasz-madon/awesome-remote-job | 47779 | +120 | +250 | 无 | 远程工作 | 远程工作资源 | 低，误匹配 | 低 |
| 28 | code-yeongyu/oh-my-openagent | 68179 | +60 | +337 | TypeScript | Agent 编排 | 复杂代码库 Agent 编排 | 中，Agent 基础设施 | 低 |
| 29 | punkpeye/awesome-mcp-servers | 92627 | +49 | +362 | 无 | MCP 资源 | MCP 服务器合集 | 中，Agent 工具生态 | 低 |
| 30 | shiyu-coder/Kronos | 37647 | +56 | +536 | Python | 金融基础模型 | 金融市场语言基础模型 | 高，金融时序模型 | 低 |
| 31 | nidhinjs/prompt-master | 11524 | +62 | +391 | 无 | 提示词技能 | 精准提示词生成技能 | 中，降低 token 浪费 | 低 |
| 32 | awesome-dsh-plugin/awesome-dsh-plugin | 10690 | +599 | 信息不足 | Python | 插件列表 | DeepSeek Harness 插件列表 | 低，误匹配 | 低 |
| 33 | perixtar/Tech-OA-Interview-Questions | 4176 | +28 | +481 | Python | 面试题库 | 科技公司面试题 | 低，误匹配 | 低 |
| 34 | antirez/ds4 | 21608 | +30 | +278 | C | 本地推理引擎 | DeepSeek 4 本地推理引擎 | 中，本地推理 | 低 |
| 35 | DataTalksClub/ai-dev-tools-zoomcamp | 1347 | +118 | +131 | Python | AI 开发课程 | AI 开发工具实战课程 | 中，Agent 工程训练 | 低 |
| 36 | OpenByteInc/QuantDinger | 10890 | +39 | +249 | Python | AI 量化平台 | 加密/股票/外汇 AI 量化平台 | 中，多资产回测 | 中 |
| 37 | AtomicBot-ai/atomic-agent | 2443 | +23 | +378 | TypeScript | 本地 Agent | 本地优先 AI Agent | 中，隐私 Agent | 中 |
| 38 | freqtrade/freqtrade | 53473 | +28 | +209 | Python | 加密交易机器人 | 开源加密交易机器人 | 中，策略框架参考 | 中 |
| 39 | OpenBB-finance/OpenBB | 72086 | +29 | +239 | Python | 金融数据平台 | 分析师/量化/AI Agent 数据平台 | 高，金融数据层 | 中 |
| 40 | simonlin1212/a-stock-data | 8937 | +22 | +227 | 无 | A 股数据工具包 | 11 层架构 54 端点 19 数据源 | 高，A 股数据基础设施 | 低 |
| 41 | Orchestra-Research/AI-Research-SKILLs | 11899 | +61 | +219 | TeX | AI 研究技能 | AI 研究工程技能库 | 中，研究 Agent 技能 | 低 |
| 42 | xbtlin/ai-berkshire | 15723 | +16 | +210 | Python | 价值投研框架 | 四大师方法论多 Agent 投研 | 高，投研 Agent 范式 | 低 |
| 43 | TraderAlice/OpenAlice | 6615 | +29 | +119 | TypeScript | AI 交易 Agent | 全资产 AI 交易 Agent | 中，全流程交易 Agent | 中 |
| 44 | simonlin1212/TradingAgents-astock | 3040 | +8 | +213 | Python | A 股多 Agent 投研 | 7 分析师辩论决策 | 高，A 股 Agent 适配 | 低 |
| 45 | fffaraz/awesome-cpp | 72850 | +11 | +91 | 无 | C++ 资源 | C++ 资源列表 | 低，误匹配 | 低 |
| 46 | elementalsouls/Claude-BugHunter | 3706 | +17 | +162 | Python | 安全审计技能 | 82 个漏洞猎手技能 | 中，金融系统安全审计 | 低 |
| 47 | virattt/ai-hedge-fund | 62969 | +4 | +131 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高，多角色投研 | 低 |
| 48 | rust-unofficial/awesome-rust | 58910 | +11 | +85 | Rust | Rust 资源 | Rust 资源列表 | 低，误匹配 | 低 |
| 49 | josephmisiti/awesome-machine-learning | 74088 | +11 | +64 | Python | ML 资源 | ML 资源列表 | 低，误匹配 | 低 |
| 50 | Developer-Y/cs-video-courses | 83137 | +8 | +94 | 无 | 课程列表 | CS 视频课程 | 低，误匹配 | 中 |
| 51 | vuejs/awesome-vue | 73538 | -1 | -14 | 无 | Vue 资源 | Vue 资源列表 | 低，误匹配 | 低 |
| 52 | ByteByteGoHq/system-design-101 | 87364 | +29 | +335 | 无 | 系统设计 | 系统设计图解 | 中，交易系统设计参考 | 低 |

## 3. 重点项目深度分析

### 3.1 ifixai-ai/iFixAi — AI Agent 独立审计

- **解决什么问题**：回答“AI Agent 是否在做它该做的事”，在 120 秒内对 Agent 行为进行独立审计，覆盖幻觉检测、提示注入、AI 对齐、EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架。
- **为什么值得关注**：7 日 +2511 星，是本次候选集中增速最快的“真金融相关”项目之一。AI Agent 进入金融交易场景后，行为可审计性从“可选”变为“刚需”。
- **技术栈/架构亮点**：Python + CLI，支持人类或 Agent 自审计，内置多标准风险映射。
- **是否适合借鉴**：非常适合。可直接将审计模块嵌入企业级交易 Agent 的 pre-trade / post-trade 检查环节，形成“Agent 决策 + 独立审计”双层架构。
- **可能风险**：项目较新（2026-04 创建），审计标准覆盖广但深度未知；不能替代真实合规审查。

### 3.2 TauricResearch/TradingAgents — 多 Agent 金融交易框架

- **解决什么问题**：用多个 LLM Agent 模拟分析师、研究员、交易员、风控等角色，通过辩论和协作完成交易决策。
- **为什么值得关注**：99k stars，是当前最主流的开源 LLM 多 Agent 交易框架，且衍生出多个 A 股适配版本（`TradingAgents-astock`）。
- **技术栈/架构亮点**：Python + LangGraph 风格多 Agent 编排，角色分工明确，支持多数据源。
- **是否适合借鉴**：非常适合。其“多角色辩论 + 风险提示”架构可直接迁移到企业级投研 Agent 框架中，作为决策层参考实现。
- **可能风险**：研究工具属性强，策略过拟合风险高；LLM 输出不稳定，不可直接实盘；需注意 API key 安全。

### 3.3 nautechsystems/nautilus_trader — Rust 原生交易引擎

- **解决什么问题**：提供生产级、确定性的 Rust 原生事件驱动交易引擎，覆盖回测、模拟和实盘。
- **为什么值得关注**：24h +259 星，是本次候选集中少有的“真交易基础设施”项目，Rust 内存安全 + 确定性回测对金融系统极具价值。
- **技术栈/架构亮点**：Rust 核心 + Python API，事件驱动架构，支持多资产（加密、股票、外汇、期货、期权）。
- **是否适合借鉴**：非常适合。若自建交易系统，其事件溯源、确定性回测、订单状态机设计值得深入研读。
- **可能风险**：LGPL-3.0 许可证对闭源商用有限制；学习曲线陡峭；实盘需自行承担市场风险。

### 3.4 ZhuLinsen/daily_stock_analysis — A 股 LLM 分析系统

- **解决什么问题**：LLM 驱动的多市场股票智能分析，整合多源行情、实时新闻、决策看板和自动推送，支持零成本定时运行。
- **为什么值得关注**：63k stars，是 A 股 AI 分析工具中 star 数最高的项目之一，中文金融 AI 工具链的代表。
- **技术栈/架构亮点**：Python，多源数据聚合 + LLM 分析 + 看板 + 推送，强调零成本定时运行。
- **是否适合借鉴**：适合。其“数据聚合 → LLM 分析 → 决策看板 → 推送”的流水线可作为 A 股投研 Agent 的 MVP 模板。
- **可能风险**：数据源稳定性与合规性需自行验证；LLM 分析结论不可作为投资依据。

### 3.5 headroomlabs-ai/headroom — LLM 上下文压缩

- **解决什么问题**：在工具输出、日志、文件、RAG 块进入 LLM 前进行压缩，编码 Agent 省 20% token，JSON 省 60-95% token，答案质量不变。
- **为什么值得关注**：67k stars，直接解决金融 Agent 处理大量行情、订单、日志数据时 token 成本爆炸的问题。
- **技术栈/架构亮点**：Python，提供库、代理、MCP server 三种形态，可无缝接入现有 Agent 栈。
- **是否适合借鉴**：非常适合。金融数据（订单簿、tick 数据、日志）体积大，压缩层可显著降低 Agent 运行成本。
- **可能风险**：压缩可能丢失关键信息，金融场景需验证压缩后决策质量不下降。

### 3.6 RyanCodrai/turbovec — Rust 向量索引

- **解决什么问题**：基于 TurboQuant 的向量索引，Rust 编写，Python 绑定，支持 SIMD（AVX512/NEON）加速。
- **为什么值得关注**：24h +313 星，增速快。金融 RAG、相似 K 线检索、新闻语义搜索都依赖高性能向量检索。
- **技术栈/架构亮点**：Rust + Python，对标 FAISS，强调 SIMD 和量化。
- **是否适合借鉴**：适合。若构建金融文档 RAG 或历史行情相似性检索，可作为向量索引候选方案。
- **可能风险**：项目较新，生态和稳定性待验证。

### 3.7 HKUDS/Vibe-Trading — 个人交易 Agent

- **解决什么问题**：定位“Vibe-Trading”，即个人交易 Agent，覆盖研究、决策、执行闭环。
- **为什么值得关注**：31k stars，港大团队出品，与 TradingAgents 形成学术派 AI 交易工具矩阵。
- **技术栈/架构亮点**：Python，多 Agent + MCP，支持回测。
- **是否适合借鉴**：适合作为 Agent 交易闭环的产品原型参考，但不应直接实盘。
- **可能风险**：加密相关，策略过拟合，研究工具属性强。

### 3.8 langfuse/langfuse — LLM 可观测性

- **解决什么问题**：LLM 评估、可观测性、指标、提示词管理、数据集管理，集成 OpenTelemetry、LangChain、OpenAI SDK 等。
- **为什么值得关注**：33k stars，YC W23 项目，是 LLM 应用生产化的核心基础设施。
- **技术栈/架构亮点**：TypeScript，自托管，覆盖 trace、eval、prompt 管理。
- **是否适合借鉴**：非常适合。金融 Agent 上线前必须建立 LLM 可观测性和评估体系，langfuse 是成熟选择。
- **可能风险**：自托管运维成本；金融数据需注意隐私合规。

### 3.9 shiyu-coder/Kronos — 金融市场基础模型

- **解决什么问题**：定位“金融市场语言的基础模型”，面向金融时序建模。
- **为什么值得关注**：37k stars，是金融领域少有的“基础模型”方向尝试。
- **技术栈/架构亮点**：Python，模型细节需进一步调研。
- **是否适合借鉴**：适合作为研究方向跟踪，关注其是否真正具备跨市场泛化能力。
- **可能风险**：金融基础模型易过拟合历史数据，需警惕幸存者偏差。

### 3.10 simonlin1212/a-stock-data — A 股数据工具包

- **解决什么问题**：A 股全栈数据工具包，11 层架构、54 端点、19 数据源、零鉴权，面向 AI Agent。
- **为什么值得关注**：8.9k stars，专为 AI Agent 设计的 A 股数据层，降低数据获取门槛。
- **技术栈/架构亮点**：Apache-2.0，强调零鉴权、多源聚合，适合 Agent 直接调用。
- **是否适合借鉴**：适合。可作为 A 股投研 Agent 的数据层参考，但需验证数据源合法性和稳定性。
- **可能风险**：零鉴权数据源可能存在合规风险；数据质量需自行校验。

## 4. 趋势归纳

### 技术趋势
- **Rust 进入金融交易基础设施**：`nautilus_trader`、`turbovec` 均以 Rust 为核心，强调内存安全、确定性和性能。
- **本地优先 / 端侧推理**：`unsloth`、`needle`、`colibri`、`ds4`、`atomic-agent` 共同指向“数据不出本地”的推理范式，契合金融数据隐私需求。
- **LLM 上下文工程**：`headroom` 的压缩代理、`prompt-master` 的提示词优化，反映 token 成本优化成为 Agent 工程核心议题。

### 产品趋势
- **AI Agent 审计产品化**：`iFixAi` 将 Agent 审计从概念变为 120 秒可用的 CLI 工具。
- **A 股 AI 工具链成熟**：从数据层（`a-stock-data`）到分析层（`daily_stock_analysis`）到投研层（`ai-berkshire`、`TradingAgents-astock`），形成完整中文金融 AI 栈。
- **设计系统与 Agent 结合**：`open-design`、`ui-ux-pro-max-skill`、`awesome-design-md` 反映“Agent 生成金融看板/产品 UI”的工程化趋势。

### 量化/交易策略趋势
- **多 Agent 辩论式决策**成为主流范式：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading`、`TradingAgents-astock` 均采用多角色协作。
- **研究工具与实盘工具分离**：多数高星项目定位研究/回测，真正生产级实盘引擎（`nautilus_trader`）star 数相对较低，反映社区对实盘风险的谨慎。

### AI Agent 与自动化交易结合趋势
- **Agent 全流程闭环**：从数据获取 → 研究分析 → 决策 → 执行 → 审计，各环节均有开源项目覆盖。
- **MCP 成为 Agent 工具标准**：`awesome-mcp-servers`、`headroom`、`Vibe-Trading` 等均支持 MCP，金融数据源和交易接口的 MCP 化是明确方向。

### 值得后续做原型验证的方向
- A 股多 Agent 投研 + 独立审计层的组合原型。
- 基于 `headroom` 的金融数据压缩层，验证压缩对决策质量的影响。
- 基于 `turbovec` 的历史行情相似性检索。
- 基于 `nautilus_trader` 事件驱动架构的简化版回测引擎。

## 5. 今日灵感清单

1. **MVP：A 股投研 Agent 审计看板** — 结合 `TradingAgents-astock` 的投研输出和 `iFixAi` 的审计思路，做一个“投研结论 + 审计报告”双栏看板，验证 Agent 决策可追溯性。
2. **调研：金融数据 LLM 压缩** — 用 `headroom` 对订单簿、tick 数据、交易日志做压缩实验，量化 token 节省率和决策质量损失。
3. **Codex 复现 demo：多 Agent 辩论决策** — 让 Codex 基于 `TradingAgents` 的架构，复现一个 3 角色（分析师/风控/交易员）的最小辩论决策 demo。
4. **MVP：本地隐私投研 Agent** — 结合 `unsloth` 本地推理和 `a-stock-data` 数据层，构建一个数据不出本地的 A 股分析 Agent 原型。
5. **调研：Rust 交易引擎事件溯源** — 深入 `nautilus_trader` 的事件驱动和确定性回测设计，输出架构笔记，评估自建简化版可行性。
6. **MVP：金融 RAG 向量检索** — 用 `turbovec` 构建金融文档/研报的语义检索层，对比 FAISS 的性能和内存占用。
7. **调研：Agent 可观测性接入** — 将 `langfuse` 接入现有 Agent 工作流，建立 trace、eval、prompt 版本管理的最小闭环。
8. **Codex 复现 demo：投资技能结构化** — 基于 `investorskills` 的思路，让 Codex 将一套投资判断规则转化为结构化、可被 Agent 调用的技能格式。
9. **MVP：金融看板生成器** — 结合 `open-design` 或 `ui-ux-pro-max-skill`，做一个输入金融数据自动生成仪表盘 UI 的原型。
10. **Watchlist：Kronos 金融基础模型** — 持续跟踪其模型发布和基准测试结果，评估是否值得作为金融时序预训练底座。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计赛道先行者，金融 Agent 合规刚需，增速快 |
| nautechsystems/nautilus_trader | 生产级 Rust 交易引擎，架构参考价值极高 |
| TauricResearch/TradingAgents | 多 Agent 交易框架事实标准，衍生生态丰富 |
| headroomlabs-ai/headroom | 金融数据 token 压缩，直接降低 Agent 成本 |
| RyanCodrai/turbovec | Rust 向量索引，金融 RAG 基础设施候选 |
| shiyu-coder/Kronos | 金融基础模型方向，需长期跟踪验证 |
| simonlin1212/a-stock-data | A 股 Agent 数据层，中文金融 AI 基础设施 |
| langfuse/langfuse | LLM 可观测性标准组件，金融 Agent 上线必备 |
| HKUDS/Vibe-Trading | 学术派 Agent 交易闭环，产品设计参考 |
| questflowai/investorskills | 投资判断结构化，投研 Agent 知识层新思路 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-08-19.json`，与当前快照 `2026-08-20.json` 相差 1 天，1 日涨星数据可信。
- **7 日基线**：存在，`baseline_7d` 为 `2026-08-13.json`，与当前快照相差 7 天，7 日涨星数据可信。
- **采集失败**：`awesome-dsh-plugin/awesome-dsh-plugin` 的 `star_delta_7d` 为 null，7 日涨星信息不足，可能因项目创建时间晚于 7 日基线。
- **样本偏差**：本次候选集存在显著关键词误匹配问题。大量 awesome-list 类项目（`public-apis`、`build-your-own-x`、`awesome-go`、`awesome-python`、`awesome-selfhosted`、`awesome-cpp`、`awesome-rust`、`awesome-vue`、`cs-video-courses`、`Tech-OA-Interview-Questions`、`awesome-remote-job` 等）因 README 或描述中偶然包含“trading”“quant”“fintech”等词被纳入，实际与金融交易无关。分析时应重点聚焦 `category_guess` 含 `ai_trading`、`backtesting`、`crypto_trading`、`quant_research`、`trading_infra`、`risk_management` 且描述真实相关的项目。
- **30 日涨星**：所有项目 `star_delta_30d` 均为 null，30 日趋势信息不足。
