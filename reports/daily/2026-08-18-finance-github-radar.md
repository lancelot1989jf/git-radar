# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-18

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 审计与治理**：`iFixAi` 以 24h +699 星、7d +2356 星快速上升，聚焦 AI Agent 的独立审计、幻觉检测、提示注入检测与合规映射（EU AI Act、ISO 42001、NIST AI RMF），对金融场景中的 Agent 可信度与风控有直接借鉴价值。
  2. **多 Agent 金融交易框架**：`TradingAgents`（98.8k stars）、`Vibe-Trading`（31.2k stars）、`QuantDinger`（10.8k stars）等持续高增长，显示“LLM 多分析师辩论 + 回测 + 交易执行”的研究型框架仍是热点。
  3. **A 股本地化 AI 投研工具链**：`daily_stock_analysis`（63.3k stars）、`tickflow-stock-panel`、`ai-berkshire`、`TradingAgents-astock`、`a-stock-data` 等形成“数据源 + 多 Agent 投研 + 自托管面板”的本地化生态，值得关注其数据工程与 Agent 编排方式。

- **是否出现新趋势**：
  出现。候选集中明显出现“**AI Agent 可审计性/合规性**”与“**本地优先、BYOK 的 Agent 设计/研究工具**”两条新线索。`iFixAi` 的快速涨星说明市场开始从“能跑 Agent”转向“能证明 Agent 行为正确、安全、可审计”。

- **是否出现值得复刻/参考的工程架构**：
  是。`nautilus_trader` 的 Rust 原生、确定性事件驱动交易引擎；`headroom` 的 LLM 上下文压缩代理/MCP server；`planning-with-files` 的崩溃可恢复、基于文件的长期 Agent 规划机制；`tickflow-stock-panel` 的 DuckDB + Polars + FastAPI + React 自托管量化工作台，均具备较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：
  本次候选集中未发现可直接判定为骗局的项目，但需警惕：
  - `Financial_freedom`（“最全赚钱投资指南”）名称与描述带有强营销色彩，且无 license、无 topics，信息透明度低。
  - 多个项目因命中 `trading_bot`、`crypto_related`、`leverage_or_grid_related` 等关键词被标记为中风险，不应直接用于实盘。
  - 大量 `awesome-*` 列表类项目因关键词误命中进入候选，并非真正交易项目，需在分析中剔除噪音。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 464637 | +1381 | +9111 | Python | API 列表 | 免费 API 合集 | 低，通用资源 | 中 |
| 2 | nexu-io/open-design | 88931 | +574 | +3780 | TypeScript | AI 设计 | 本地优先 AI 设计桌面应用 | 中，Agent 设计引擎 | 低 |
| 3 | unslothai/unsloth | 73608 | +356 | +3313 | Python | LLM 微调 | 本地训练/运行 LLM 与扩散模型 | 中，本地模型底座 | 低 |
| 4 | cactus-compute/needle | 7533 | +379 | +3778 | Python | 端侧模型 | 14MB 端侧基础模型 | 中，端侧推理 | 中 |
| 5 | ifixai-ai/iFixAi | 10701 | +699 | +2356 | Python | AI 审计/风控 | AI Agent 独立审计与合规评估 | 高，Agent 治理 | 低 |
| 6 | nextlevelbuilder/ui-ux-pro-max-skill | 117956 | +306 | +2226 | Python | AI 设计技能 | UI/UX 设计智能技能 | 中，Agent 技能 | 低 |
| 7 | codecrafters-io/build-your-own-x | 540922 | +364 | +2067 | Markdown | 教程合集 | 从零复刻技术项目 | 低，通用教程 | 中 |
| 8 | awesome-selfhosted/awesome-selfhosted | 313545 | +228 | +1453 | 无 | 自托管列表 | 自托管服务列表 | 低，通用资源 | 中 |
| 9 | JustVugg/colibri | 25441 | +98 | +1324 | C | 模型推理 | 纯 C 零依赖 MoE 推理引擎 | 中，推理性能 | 低 |
| 10 | vinta/awesome-python | 314721 | +207 | +1249 | Python | Python 资源 | Python 工具精选 | 低，通用资源 | 低 |
| 11 | VoltAgent/awesome-design-md | 109175 | +227 | +1266 | 无 | 设计系统 | DESIGN.md 设计系统合集 | 中，Agent UI 生成 | 中 |
| 12 | TauricResearch/TradingAgents | 98839 | +158 | +1228 | Python | 多 Agent 交易 | LLM 多 Agent 金融交易框架 | 高，Agent 交易研究 | 低 |
| 13 | ZhuLinsen/daily_stock_analysis | 63308 | +122 | +1093 | Python | A 股分析 | LLM 多市场股票分析系统 | 高，投研数据管道 | 低 |
| 14 | codeman008/Financial_freedom | 3086 | +139 | +1145 | 无 | 投资指南 | 赚钱投资指南 | 低，营销色彩强 | 中 |
| 15 | headroomlabs-ai/headroom | 66800 | +115 | +817 | Python | 上下文压缩 | LLM 工具输出压缩代理 | 高，Agent 上下文工程 | 低 |
| 16 | ripienaar/free-for-dev | 132155 | +102 | +638 | HTML | 免费资源 | 开发者免费资源列表 | 低，通用资源 | 低 |
| 17 | avelino/awesome-go | 181442 | +103 | +621 | Go | Go 资源 | Go 框架与库精选 | 低，通用资源 | 中 |
| 18 | HKUDS/Vibe-Trading | 31235 | +111 | +600 | Python | AI 交易 | 个人交易 Agent | 高，Agent 交易框架 | 中 |
| 19 | RyanCodrai/turbovec | 15326 | +506 | +603 | Rust | 向量索引 | 基于 TurboQuant 的向量索引 | 中，量化向量检索 | 低 |
| 20 | ruvnet/ruflo | 68235 | +142 | +555 | TypeScript | Agent 编排 | 多智能体 swarm 编排框架 | 中，Agent 编排 | 低 |
| 21 | shiyu-coder/Kronos | 37538 | +83 | +860 | Python | 金融基础模型 | 金融市场语言基础模型 | 高，金融 LLM | 低 |
| 22 | nautechsystems/nautilus_trader | 26260 | +299 | +829 | Rust | 交易引擎 | Rust 原生事件驱动交易引擎 | 高，交易基础设施 | 中 |
| 23 | garrytan/gbrain | 28700 | +77 | +469 | TypeScript | Agent 大脑 | 个人 Agent 大脑框架 | 中，Agent 框架 | 低 |
| 24 | shy3130/tickflow-stock-panel | 3135 | +147 | +398 | Python | A 股量化工作台 | 自托管选股/监控/回测工作台 | 高，量化数据栈 | 低 |
| 25 | hesreallyhim/awesome-claude-code | 52584 | +78 | +428 | Python | Claude Code 资源 | Claude Code 资源精选 | 低，通用资源 | 低 |
| 26 | AtomicBot-ai/atomic-agent | 2345 | +49 | +658 | TypeScript | 本地 Agent | 本地优先 AI Agent | 中，本地 Agent | 中 |
| 27 | perixtar/Tech-OA-Interview-Questions | 4093 | +324 | +422 | Python | 面试题库 | 科技公司 OA 题库 | 低，无关 | 低 |
| 28 | punkpeye/awesome-mcp-servers | 92543 | +55 | +432 | 无 | MCP 资源 | MCP server 合集 | 中，MCP 生态 | 低 |
| 29 | ashishpatel26/500-AI-Agents-Projects | 36665 | +47 | +468 | Python | AI Agent 案例 | 500 个 AI Agent 项目合集 | 中，Agent 案例 | 中 |
| 30 | nidhinjs/prompt-master | 11386 | +176 | +276 | 无 | 提示词技能 | Claude 提示词生成技能 | 低，提示工程 | 低 |
| 31 | code-yeongyu/oh-my-openagent | 68043 | +36 | +326 | TypeScript | Agent 编排 | 复杂代码库 Agent 编排 | 中，Agent 编排 | 低 |
| 32 | antirez/ds4 | 21541 | +42 | +335 | C | 本地推理 | DeepSeek 本地推理引擎 | 中，本地推理 | 低 |
| 33 | awesome-dsh-plugin/awesome-dsh-plugin | 9016 | +1343 | 无 | Python | 插件列表 | DeepSeek Harness 插件列表 | 低，插件生态 | 低 |
| 34 | xbtlin/ai-berkshire | 15681 | +34 | +247 | Python | 价值投研 | 多 Agent 价值投资研究框架 | 高，投研 Agent | 低 |
| 35 | OpenByteInc/QuantDinger | 10820 | +27 | +320 | Python | AI 量化平台 | 加密/股票/外汇 AI 量化平台 | 中，量化平台 | 中 |
| 36 | simonlin1212/a-stock-data | 8891 | +37 | +267 | 无 | A 股数据 | A 股全栈数据工具包 | 高，金融数据源 | 低 |
| 37 | OpenBB-finance/OpenBB | 72013 | +32 | +231 | Python | 金融数据平台 | 分析师/量化/AI Agent 开放数据平台 | 高，金融数据平台 | 中 |
| 38 | QAI-brain/awesome-QAI-Papers-QRL | 425 | +136 | +244 | 无 | 量化 RL 论文 | 量化 AI/强化学习论文列表 | 中，研究方向 | 低 |
| 39 | freqtrade/freqtrade | 53416 | +22 | +219 | Python | 加密交易机器人 | 开源加密交易机器人 | 中，交易机器人 | 中 |
| 40 | virattt/ai-hedge-fund | 62951 | +22 | +149 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高，多 Agent 投研 | 低 |
| 41 | elementalsouls/Claude-BugHunter | 3667 | +30 | +179 | Python | 安全技能 | Claude 漏洞挖掘技能包 | 中，安全审计 | 低 |
| 42 | simonlin1212/Vibe-Research | 2123 | +40 | +152 | TypeScript | 投研 Agent | 个人投研 Agent 面板 | 高，投研产品 | 低 |
| 43 | OthmanAdi/planning-with-files | 26237 | +23 | +130 | Shell | Agent 规划 | 基于文件的 Agent 长期规划 | 高，Agent 可靠性 | 低 |
| 44 | Developer-Y/cs-video-courses | 83109 | +37 | +103 | 无 | 课程列表 | CS 视频课程列表 | 低，通用资源 | 中 |
| 45 | josephmisiti/awesome-machine-learning | 74067 | +23 | +71 | Python | ML 资源 | ML 框架与库精选 | 低，通用资源 | 低 |
| 46 | simonlin1212/TradingAgents-astock | 3020 | +18 | +218 | Python | A 股多 Agent | A 股多 Agent 投研框架 | 高，本地化 Agent | 低 |
| 47 | rust-unofficial/awesome-rust | 58891 | +21 | +88 | Rust | Rust 资源 | Rust 资源精选 | 低，通用资源 | 低 |
| 48 | fffaraz/awesome-cpp | 72821 | +17 | +94 | 无 | C++ 资源 | C++ 资源精选 | 低，通用资源 | 低 |
| 49 | ByteByteGoHq/system-design-101 | 87304 | +43 | +380 | 无 | 系统设计 | 系统设计图解 | 中，架构参考 | 低 |
| 50 | vuejs/awesome-vue | 73541 | -3 | -11 | 无 | Vue 资源 | Vue 资源精选 | 低，通用资源 | 低 |

## 3. 重点项目深度分析

### 3.1 iFixAi — AI Agent 独立审计与合规评估

- **解决什么问题**：回答“AI Agent 是否在做它该做的事”，提供 Agent 行为审计、幻觉检测、提示注入检测、AI 对齐与合规评估，声称 120 秒内给出结论。
- **为什么值得关注**：24h +699 星、7d +2356 星，增速显著。在金融交易 Agent 场景中，“Agent 是否按预期执行”是上线前必须解决的问题，该项目直接切入这一痛点。
- **技术栈/架构亮点**：Python + CLI，topics 覆盖 `agent-evaluation`、`ai-governance`、`ai-safety`、`hallucination-detection`、`prompt-injection`、`owasp-llm`、`nist-ai-rmf`、`iso-42001`、`eu-ai-act`，说明其将技术检测与合规框架映射结合。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架**：非常适合。可将其审计思想引入交易 Agent 的决策前检查、交易后复盘、提示注入防护与合规留痕。
- **可能风险**：项目较新（2026-04 创建），审计结论的可靠性、覆盖范围与误报率需自行验证；Apache-2.0 但生态成熟度未知；不应将“审计通过”等同于“策略安全”。

### 3.2 TauricResearch/TradingAgents — LLM 多 Agent 金融交易框架

- **解决什么问题**：用多个 LLM Agent 模拟分析师、研究员、交易员等角色，对股票进行基本面、技术面、情绪面等多维度分析并给出交易决策。
- **为什么值得关注**：98.8k stars，7d +1228 星，是当前“多 Agent 金融交易”方向的标杆项目，且为 Apache-2.0 开源。
- **技术栈/架构亮点**：Python，topics 为 `agent`、`finance`、`llm`、`multiagent`、`trading`。核心是多角色 Agent 协作与辩论式决策。
- **是否适合借鉴**：适合。可作为企业级投研 Agent 的参考架构，尤其是多分析师辩论、风险提示与决策留痕机制。
- **可能风险**：定位为研究工具（`likely_research_tool`），回测结果可能过拟合；LLM 决策存在幻觉与不可复现性；不应直接用于实盘或输入真实 API key。

### 3.3 nautechsystems/nautilus_trader — Rust 原生事件驱动交易引擎

- **解决什么问题**：提供生产级、确定性的 Rust 原生交易引擎，支持回测与实盘，覆盖加密、股票、外汇、期货、期权等。
- **为什么值得关注**：24h +299 星、7d +829 星，在交易基础设施类项目中增速突出；Rust 实现带来性能与内存安全优势。
- **技术栈/架构亮点**：Rust + Python 绑定，LGPL-3.0。强调“deterministic event-driven architecture”，适合对回测一致性和低延迟有要求的场景。
- **是否适合借鉴**：适合。其事件驱动、确定性回测、多资产支持的设计可作为自研交易引擎的架构参考。
- **可能风险**：被标记 `crypto_related`、`leverage_or_grid_related`，涉及杠杆/网格类策略时资金风险高；LGPL 协议在商业集成时需注意合规；学习曲线较陡。

### 3.4 ZhuLinsen/daily_stock_analysis — LLM 多市场股票分析系统

- **解决什么问题**：提供多源行情、实时新闻、决策看板与自动推送的股票分析系统，支持零成本定时运行。
- **为什么值得关注**：63.3k stars，7d +1093 星，是 A 股 AI 分析方向的高星项目，MIT 协议。
- **技术栈/架构亮点**：Python，topics 含 `a-stock`、`ai-agent`、`llm`、`quant`、`quantitative-finance`。核心价值在于多源数据整合与 LLM 决策看板。
- **是否适合借鉴**：适合。其“多源数据 + 实时新闻 + 决策看板 + 自动推送”的产品形态可直接复刻为内部投研工具。
- **可能风险**：数据源稳定性与合规性需自行验证；LLM 生成的“决策”不应直接作为交易信号；需注意 A 股数据授权问题。

### 3.5 headroomlabs-ai/headroom — LLM 上下文压缩代理

- **解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前进行压缩，降低 token 消耗，同时保持回答质量。
- **为什么值得关注**：66.8k stars，7d +817 星。对金融 Agent 而言，行情、新闻、研报等长文本输入的成本与上下文窗口是核心瓶颈。
- **技术栈/架构亮点**：Python，提供 library、proxy、MCP server 三种形态，topics 含 `context-engineering`、`token-optimization`、`mcp`、`rag`。
- **是否适合借鉴**：非常适合。可将其作为交易 Agent 的数据预处理层，降低长上下文成本并提升上下文稳定性。
- **可能风险**：压缩可能丢失关键信息，金融场景需验证压缩后决策一致性；依赖上游 LLM 行为，需做回归测试。

### 3.6 shy3130/tickflow-stock-panel — 自托管 A 股量化工作台

- **解决什么问题**：提供 A 股“选股 + 监控 + 回测”的自托管量化工作台，基于 TickFlow 数据源，支持 LLM 策略定制与个股分析。
- **为什么值得关注**：24h +147 星，虽然总 star 仅 3.1k，但增速快，且技术栈现代。
- **技术栈/架构亮点**：Python + React，topics 含 `duckdb`、`polars`、`fastapi`、`llm`、`backtesting`、`self-hosted`。DuckDB + Polars 的组合适合本地量化数据分析。
- **是否适合借鉴**：适合。其“本地数据 + 现代分析栈 + LLM 辅助 + 自托管面板”的架构可作为轻量级量化工作台原型。
- **可能风险**：项目声明为个人开源、非 TickFlow 官方项目，数据源可持续性存疑；回测结果需独立验证；自托管部署涉及数据合规。

### 3.7 xbtlin/ai-berkshire — 多 Agent 价值投资研究框架

- **解决什么问题**：基于 Claude Code / Codex，整合巴菲特、芒格、段永平、李录四套方法论，用多 Agent 并行与对抗分析进行价值投资研究。
- **为什么值得关注**：15.7k stars，7d +247 星。将“投资大师方法论”显式编码为 Agent 提示词/流程，是投研 Agent 产品化的有趣尝试。
- **技术栈/架构亮点**：Python，topics 含 `ai-agent`、`claude-code`、`mcp`、`portfolio-management`、`value-investing`。核心是方法论模板 + 多 Agent 对抗分析。
- **是否适合借鉴**：适合。可借鉴其“将投研方法论结构化、模板化”的思路，构建企业内部投研知识库与 Agent 流程。
- **可能风险**：方法论模板可能过于简化，结论不代表真实投资能力；依赖 Claude Code/Codex 生态；需警惕“大师方法论”营销化。

### 3.8 virattt/ai-hedge-fund — AI 对冲基金团队模拟

- **解决什么问题**：模拟一个 AI 对冲基金团队，多个 Agent 扮演不同角色进行投资决策。
- **为什么值得关注**：62.9k stars，是“AI 对冲基金”概念的代表性开源项目，MIT 协议。
- **技术栈/架构亮点**：Python，topics 为空，但描述明确为多 Agent 团队模拟。
- **是否适合借鉴**：适合作为多 Agent 投研决策流程的教学与原型参考。
- **可能风险**：定位为研究/教学工具，回测结果不可作为收益预期；Agent 决策缺乏真实市场冲击成本、流动性与合规约束。

### 3.9 OthmanAdi/planning-with-files — 基于文件的 Agent 长期规划

- **解决什么问题**：为 AI 编码 Agent 和长时任务提供持久化、基于文件的规划，支持崩溃恢复、会话恢复、上下文防衰减与确定性完成门控。
- **为什么值得关注**：26.2k stars，7d +130 星。对长时间运行的交易/研究 Agent，状态持久化与崩溃恢复是关键工程问题。
- **技术栈/架构亮点**：Shell + Markdown 规划文件，topics 含 `context-engineering`、`session-recovery`、`long-running-agents`、`multi-agent-systems`。
- **是否适合借鉴**：非常适合。可将其规划文件机制引入交易 Agent 的任务编排，提升可恢复性与可审计性。
- **可能风险**：本身不是交易系统，需自行与交易执行层集成；文件规划机制需防止敏感信息泄露。

### 3.10 OpenBB-finance/OpenBB — 开放金融数据平台

- **解决什么问题**：为分析师、量化研究员和 AI Agent 提供统一的开放金融数据平台。
- **为什么值得关注**：72k stars，是金融数据平台方向的重要开源项目，支持股票、加密、衍生品、固定收益等。
- **技术栈/架构亮点**：Python，topics 含 `ai`、`crypto`、`derivatives`、`equity`、`fixed-income`、`machine-learning`、`quantitative-finance`。
- **是否适合借鉴**：适合。可作为 AI 投研 Agent 的标准化数据接入层，减少多源数据适配成本。
- **可能风险**：被标记 `crypto_related`；数据源授权与合规需自行确认；平台依赖较重，定制成本需评估。

## 4. 趋势归纳

- **技术趋势**：
  - **Rust 进入交易基础设施**：`nautilus_trader`、`turbovec` 等项目显示 Rust 在低延迟、确定性回测、向量检索等场景的渗透。
  - **本地优先与端侧推理**：`unsloth`、`needle`、`colibri`、`ds4`、`atomic-agent` 等反映“本地运行、BYOK、端侧模型”趋势，契合金融数据隐私需求。
  - **上下文工程成为 Agent 基础设施**：`headroom`、`planning-with-files` 等项目聚焦 token 压缩、上下文防衰减、会话恢复，是长时金融 Agent 的关键使能技术。

- **产品趋势**：
  - **自托管投研工作台**：`tickflow-stock-panel`、`Vibe-Research`、`daily_stock_analysis` 等将数据、回测、LLM 分析、看板整合为本地化产品。
  - **AI Agent 审计与治理产品化**：`iFixAi` 将 Agent 合规、幻觉检测、提示注入检测打包为可执行工具，预示“Agent 可信度”将成为独立产品品类。
  - **设计/UI 生成与 Agent 技能生态**：`open-design`、`ui-ux-pro-max-skill`、`awesome-design-md` 等虽非金融核心，但可用于快速搭建投研面板与可视化原型。

- **量化/交易策略趋势**：
  - **多 Agent 辩论式投研**：`TradingAgents`、`ai-hedge-fund`、`ai-berkshire`、`TradingAgents-astock` 均采用多角色、多视角、对抗式分析，而非单一模型输出。
  - **金融基础模型**：`Kronos` 提出“金融市场语言基础模型”，显示从通用 LLM 向金融专用模型的探索。
  - **量化强化学习研究**：`awesome-QAI-Papers-QRL` 虽小，但反映 QRL（Quant RL）方向的研究兴趣。

- **AI Agent 与自动化交易结合趋势**：
  - 从“单 Agent 下单”转向“多 Agent 研究 + 审计 + 执行分离”的架构。
  - 强调 BYOK、本地优先、可审计、可恢复，而非直接托管资金或 API key。
  - MCP 生态（`awesome-mcp-servers`、`headroom`、`Vibe-Trading`）成为 Agent 与数据/工具连接的标准接口。

- **值得后续做原型验证的方向**：
  - 本地优先的 A 股/加密投研 Agent 工作台（DuckDB + Polars + FastAPI + React + LLM）。
  - 交易 Agent 的决策审计与合规留痕模块。
  - 基于 Rust 的确定性回测引擎最小实现。
  - LLM 上下文压缩在金融长文本场景的效果验证。
  - 多 Agent 对抗式投研流程的提示词模板化与评估。

## 5. 今日灵感清单

1. **MVP：本地投研 Agent 工作台**：参考 `tickflow-stock-panel` 与 `Vibe-Research`，用 DuckDB + Polars + FastAPI + React 搭建一个自托管投研面板，接入本地 LLM，实现“选股 + 监控 + 回测 + 复盘”闭环。
2. **MVP：交易 Agent 决策审计器**：借鉴 `iFixAi`，为现有交易 Agent 增加决策前检查与交易后审计模块，记录 Agent 输入、输出、风险提示与合规状态。
3. **调研：Rust 确定性回测引擎**：以 `nautilus_trader` 为参考，调研事件驱动、确定性回测、多资产撮合的最小实现方案，评估自研可行性。
4. **调研：LLM 上下文压缩在金融场景的效果**：基于 `headroom` 的思路，测试行情、新闻、研报长文本压缩前后对投研 Agent 决策一致性的影响。
5. **Codex/Agent 自动复现 demo**：让 Codex 复现 `planning-with-files` 的基于文件规划机制，并集成到一个长时运行的投研 Agent 中，验证崩溃恢复与上下文防衰减。
6. **原型：多 Agent 对抗式投研流程**：参考 `TradingAgents` 与 `ai-berkshire`，将“分析师 + 反对者 + 风控”三角色辩论流程模板化，用于内部研报生成。
7. **调研：金融基础模型 Kronos**：调研 `Kronos` 的模型架构、训练数据与评估方式，评估其在金融文本理解与预测任务上的可迁移性。
8. **原型：MCP 金融数据网关**：参考 `OpenBB` 与 `awesome-mcp-servers`，构建一个统一的 MCP 金融数据网关，屏蔽多源数据差异，供 Agent 调用。
9. **安全调研：Agent 提示注入防护**：结合 `iFixAi` 与 `Claude-BugHunter`，调研交易 Agent 的提示注入攻击面与防护方案。
10. **Watchlist 候选**：将 `iFixAi`、`nautilus_trader`、`headroom`、`tickflow-stock-panel`、`Kronos`、`planning-with-files` 加入 watchlist，持续跟踪其架构演进与社区活跃度。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ifixai-ai/iFixAi | AI Agent 审计与合规是金融 Agent 上线的关键缺口，增速快，值得跟踪其检测能力与合规映射演进。 |
| nautechsystems/nautilus_trader | Rust 原生确定性交易引擎，架构参考价值高，适合跟踪其回测一致性与多资产支持进展。 |
| headroomlabs-ai/headroom | LLM 上下文压缩对金融长文本 Agent 成本与稳定性影响大，值得跟踪其压缩算法与 MCP 集成。 |
| shy3130/tickflow-stock-panel | 现代 A 股量化工作台，DuckDB + Polars + FastAPI 技术栈清晰，适合作为本地量化原型参考。 |
| shiyu-coder/Kronos | 金融基础模型方向，若其模型能力得到验证，可能改变金融 LLM 应用范式。 |
| OthmanAdi/planning-with-files | 长时 Agent 的崩溃恢复与上下文防衰减机制，对交易/研究 Agent 可靠性有直接价值。 |
| TauricResearch/TradingAgents | 多 Agent 金融交易框架标杆，适合跟踪其 Agent 角色设计与决策流程演进。 |
| OpenBB-finance/OpenBB | 金融数据平台标准化方向，适合跟踪其数据源覆盖与 AI Agent 集成能力。 |
| virattt/ai-hedge-fund | AI 对冲基金团队模拟的代表项目，适合跟踪多 Agent 投研流程的教学化与工程化进展。 |
| xbtlin/ai-berkshire | 方法论模板化投研 Agent，适合跟踪“投研知识结构化 + 多 Agent 对抗”的产品化路径。 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-08-17）与 `baseline_7d`（2026-08-11），1 日与 7 日涨星数据基本完整。
- **缺失字段**：`star_delta_30d` 在所有项目中均为 `null`，无法进行 30 日趋势分析；`awesome-dsh-plugin` 的 `star_delta_7d` 为 `null`，7 日涨星缺失。
- **样本偏差**：候选集由关键词搜索生成，存在明显误命中，大量 `awesome-*` 列表、教程、面试题库、设计工具等非金融/交易项目因关键词命中进入候选，稀释了真实金融/量化项目比例。分析时已尽量剔除噪音，但 Top 表中仍保留部分低相关项目以反映原始数据情况。
- **分类可信度**：`category_guess`、`risk_flags`、`ranking_reasons` 为自动生成，存在误分类可能，例如 `needle` 被标记为 `trading_bot` 但实际为端侧模型项目，`build-your-own-x`、`awesome-selfhosted` 等被标记为 `trading_bot` 属于关键词误命中。
- **数据时点**：报告日期取自 `current_snapshot` 文件名 `2026-08-18`，`generated_at` 为 `2026-08-19T02:10:38+00:00`，两者存在约 1 天差异，涨星数据以快照时点为准。
