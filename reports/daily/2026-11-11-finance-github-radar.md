# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-11

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的股票分析与 AI Trading Agent**：`daily_stock_analysis` 以 24h +1100 星、7d +3155 星领跑，`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 等持续活跃，说明“LLM + 多 Agent + 交易决策”仍是当前最热主线。
  2. **AI Agent 技能与编排基础设施**：`ui-ux-pro-max-skill`、`day-trader-skill`、`trader-skill`、`agentic-awesome-skills` 等项目显示，Claude/Codex/Cursor 的“skill”生态正在快速膨胀，交易类 skill 开始出现。
  3. **AI Agent 治理、审计与风控**：`iFixAi` 聚焦 AI Agent 独立审计、幻觉检测、ISO 42001/NIST AI RMF 对齐，`Wallet-Risk-Scanner` 聚焦链上钱包 AML/KYT 风险评分，说明“Agent 可信度”和“链上风控”正在成为新焦点。

- **是否出现新趋势**：出现。候选集中大量项目并非传统量化库，而是 **AI Agent skill、MCP server、本地优先 Agent 工作台、Agent 审计/治理工具**。这反映出金融科技开源热点正从“策略库”转向“可被编码 Agent 调用的能力单元”和“Agent 运行安全”。

- **是否出现值得复刻/参考的工程架构**：是。`daily_stock_analysis` 的“多源行情 + 实时新闻 + 决策看板 + 自动推送 + 零成本定时运行”架构，`TradingAgents` 的多 Agent 金融交易框架，`iFixAi` 的 Agent 审计流水线，`Wallet-Risk-Scanner` 的多情报源 failover 风控扫描，均具备工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但存在大量 **awesome-list 类项目因关键词误匹配进入榜单**（如 `awesome-selfhosted`、`public-apis`、`build-your-own-x`、`awesome-go` 等），它们并非真正的金融/量化项目，属于样本噪声。另需注意 `day-trader-skill`、`trader-skill` 等“Claude 交易技能”项目营销话术较强，实际策略有效性与安全性未经验证。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ZhuLinsen/daily_stock_analysis | 70735 | +1100 | +3155 | Python | AI 交易/数据工程/量化研究 | LLM 驱动的多市场股票分析系统，含行情、新闻、看板、推送 | 高：多源数据融合 + LLM 决策看板 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 148339 | +421 | +2976 | Python | 金融科技产品 | AI UI/UX 设计 skill | 中：Agent 生成金融产品界面 | 低 |
| 3 | awesome-selfhosted/awesome-selfhosted | 336245 | +333 | +2400 | 无 | 交易机器人（误匹配） | 自托管服务列表 | 低：非金融项目 | 中 |
| 4 | public-apis/public-apis | 498345 | +291 | +2157 | Python | 加密交易/量化研究（误匹配） | 免费 API 列表 | 中：可发现金融数据 API | 中 |
| 5 | JustVugg/colibri | 50049 | +230 | +2179 | C | 量化研究 | MoE 模型分层推理引擎，GPU/RAM/NVMe 分层 | 高：本地大模型推理成本优化 | 低 |
| 6 | codecrafters-io/build-your-own-x | 561957 | +296 | +2043 | Markdown | 交易机器人（误匹配） | 从零复刻技术的教程集合 | 中：可复刻交易系统组件 | 中 |
| 7 | awesome-dsh-plugin/awesome-dsh-plugin | 24376 | +135 | +1925 | JavaScript | 交易基础设施 | DeepSeek Harness 插件列表 | 中：Agent 插件生态 | 低 |
| 8 | Jakeschincariol/day-trader-skill | 7185 | +418 | +1820 | Python | 回测/风控 | 11 个 Claude 日内交易 skill | 中：交易决策 Agent 化 | 低 |
| 9 | vinta/awesome-python | 334160 | +242 | +1561 | Python | 量化研究（误匹配） | Python 工具精选列表 | 低：非金融项目 | 低 |
| 10 | TauricResearch/TradingAgents | 122173 | +255 | +1478 | Python | AI 交易/回测/量化研究 | 多 Agent LLM 金融交易框架 | 高：多 Agent 交易决策架构 | 低 |
| 11 | VoltAgent/awesome-design-md | 127077 | +530 | +1405 | 无 | 加密交易/金融科技产品（误匹配） | 品牌设计系统 DESIGN.md 集合 | 中：Agent 生成金融 UI | 中 |
| 12 | ifixai-ai/iFixAi | 45029 | +278 | +1442 | Python | AI 交易/金融科技产品/风控 | AI Agent 独立审计工具 | 高：Agent 治理与合规审计 | 低 |
| 13 | nexu-io/open-design | 107274 | +193 | +1274 | TypeScript | 金融科技产品/交易基础设施 | 协作式 AI 设计 Agent 工作台 | 中：金融仪表盘原型 | 低 |
| 14 | avelino/awesome-go | 193411 | +196 | +1267 | Go | 回测/加密交易/风控（误匹配） | Go 框架与库精选列表 | 低：非金融项目 | 中 |
| 15 | garrytan/gbrain | 32726 | +147 | +1191 | TypeScript | 金融科技产品 | OpenClaw/Hermes Agent Brain | 中：Agent 编排参考 | 低 |
| 16 | CopilotKit/OpenBot | 11149 | +302 | +958 | TypeScript | 金融科技产品/交易机器人 | 开源 AI 数字员工，自带浏览器/文件/工具 | 高：Agent 操作审计与治理 | 中 |
| 17 | ripienaar/free-for-dev | 142651 | +108 | +739 | HTML | 金融科技产品/量化研究（误匹配） | 开发者免费资源列表 | 低：非金融项目 | 低 |
| 18 | kaankiziltug/logo-design-skill | 6675 | +130 | +649 | HTML | 金融科技产品 | Logo 设计 Agent skill | 低：非金融项目 | 低 |
| 19 | jaywcjlove/awesome-mac | 118325 | +84 | +554 | Swift | 交易基础设施（误匹配） | macOS 软件精选列表 | 低：非金融项目 | 低 |
| 20 | ruvnet/ruflo | 81522 | +71 | +609 | TypeScript | AI 交易/回测 | 多智能体 swarm 编排框架 | 高：多 Agent 协调与记忆 | 低 |
| 21 | PurpleDoubleD/locally-uncensored | 3912 | +195 | +585 | TypeScript | AI 交易/量化研究 | 本地 AI 工作室，桌面端一站式 | 中：本地 LLM 交易研究环境 | 低 |
| 22 | headroomlabs-ai/headroom | 79409 | +78 | +525 | Python | AI 交易/风控 | LLM 上下文压缩工具 | 高：降低 Agent token 成本 | 低 |
| 23 | hesreallyhim/awesome-claude-code | 57819 | +82 | +536 | Python | AI 交易/量化研究（误匹配） | Claude Code 资源精选 | 中：Agent 工具链调研 | 低 |
| 24 | shiyu-coder/Kronos | 47655 | +61 | +785 | Python | 回测/量化研究 | 金融市场基础模型 | 高：金融时序基础模型 | 低 |
| 25 | sickn33/agentic-awesome-skills | 49578 | +70 | +408 | Python | 回测 | 2955+ 可复用 AI Agent skills | 中：交易 skill 库 | 低 |
| 26 | ashishpatel26/500-AI-Agents-Projects | 39745 | +72 | +435 | Python | 风控/交易机器人 | 500 个 AI Agent 用例集合 | 中：金融 Agent 用例调研 | 中 |
| 27 | shy3130/tick-stock-panel | 7618 | +44 | +548 | Python | AI 交易/回测/量化研究 | A 股自托管量化工作台 | 高：DuckDB+Polars+FastAPI 架构 | 低 |
| 28 | HKUDS/Vibe-Trading | 38080 | +57 | +406 | Python | AI 交易/回测/金融科技产品 | 个人交易 Agent | 高：MCP + 多 Agent 交易 | 低 |
| 29 | punkpeye/awesome-remote-mcp-servers | 3034 | +70 | +415 | 无 | AI 交易/加密交易/交易基础设施 | 远程 MCP server 列表 | 中：金融数据 MCP 调研 | 中 |
| 30 | punkpeye/awesome-mcp-servers | 97631 | +45 | +313 | 无 | 金融科技产品 | MCP server 列表 | 中：金融 MCP 生态 | 低 |
| 31 | Jakeschincariol/trader-skill | 1712 | +59 | +409 | Python | 未分类 | 11 个 Claude 投资者跟踪 skill | 中：13F/新闻/国会交易跟踪 | 低 |
| 32 | aardappel/goose | 3449 | +36 | +434 | C++ | 交易基础设施 | Goose 编程语言 | 低：非金融项目 | 低 |
| 33 | Orkas-AI/Orkas | 9271 | +66 | +246 | JavaScript | 回测 | 本地优先 AI 团队桌面应用 | 中：多 Agent 任务编排 | 低 |
| 34 | nidhinjs/prompt-master | 15862 | +49 | +340 | 无 | AI 交易/金融科技产品 | Claude prompt 优化 skill | 低：非金融项目 | 低 |
| 35 | openbq-org/OpenBB | 75357 | +38 | +253 | Python | 加密交易/量化研究 | 分析师/量化/AI Agent 开放数据平台 | 高：金融数据基础设施 | 中 |
| 36 | MakazhanAlpamys/Soup | 10485 | +28 | +312 | Python | AI 交易/量化研究 | 单 YAML 微调 LLM，低显存训练 | 中：金融 LLM 微调 | 低 |
| 37 | Developer-Y/cs-video-courses | 84822 | +14 | +261 | 无 | 量化研究/交易机器人（误匹配） | CS 视频课程列表 | 低：非金融项目 | 中 |
| 38 | code-yeongyu/oh-my-openagent | 70864 | +36 | +142 | TypeScript | 量化研究 | 图工程 Agent 工具 | 低：非金融项目 | 低 |
| 39 | Soniavasseur/Wallet-Risk-Scanner | 914 | +428 | 信息不足 | Python | 加密交易/金融科技产品/风控 | 多链钱包 AML/KYT 风险扫描器 | 高：链上风控与情报融合 | 中 |
| 40 | AtomicBot-ai/atomic-agent | 3614 | +65 | +116 | TypeScript | AI 交易/量化研究/交易机器人 | 本地优先 AI Agent，llama.cpp 运行开源模型 | 中：本地 Agent 隐私架构 | 中 |
| 41 | awesomedata/awesome-public-datasets | 80050 | +27 | +99 | 无 | 加密交易（误匹配） | 高质量公开数据集列表 | 中：金融数据集调研 | 中 |
| 42 | TGrpg/awesome-telegram | 1270 | +76 | 信息不足 | JavaScript | 量化研究/交易机器人 | Telegram 频道/群组/机器人导航 | 低：非金融项目 | 中 |
| 43 | virattt/ai-hedge-fund | 64640 | +10 | +141 | Python | 回测/风控 | AI 对冲基金团队 | 高：多 Agent 投研决策 | 低 |
| 44 | rust-unofficial/awesome-rust | 60469 | +15 | +132 | Rust | AI 交易/回测/加密交易/量化研究（误匹配） | Rust 资源精选列表 | 低：非金融项目 | 中 |
| 45 | fffaraz/awesome-cpp | 74366 | +9 | +124 | 无 | 量化研究/交易基础设施（误匹配） | C/C++ 资源精选列表 | 低：非金融项目 | 低 |
| 46 | josephmisiti/awesome-machine-learning | 74803 | +12 | +49 | Python | AI 交易（误匹配） | 机器学习资源精选列表 | 低：非金融项目 | 低 |
| 47 | vuejs/awesome-vue | 73479 | -1 | -9 | 无 | 量化研究（误匹配） | Vue.js 资源精选列表 | 低：非金融项目 | 低 |

## 3. 重点项目深度分析

### 3.1 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：面向 A 股等多市场的股票智能分析，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么值得关注**：24h +1100 星、7d +3155 星，是本次候选集中涨星最猛的金融项目；MIT 协议、Python 实现，适合直接研究其数据流与 LLM 集成方式。
- **技术栈/架构亮点**：多源行情 + 实时新闻 + LLM 决策看板 + 自动推送 + 定时任务。其“零成本定时运行”暗示可能采用免费数据源与轻量调度，适合个人开发者复刻。
- **是否适合借鉴**：适合。其“数据采集 → LLM 分析 → 看板展示 → 推送”流水线可迁移到企业级投研 Agent 或自动化报告系统。
- **可能风险**：金融合规风险（个股分析可能涉及投资建议）；LLM 输出幻觉；数据源稳定性；策略未经验证。

### 3.2 TauricResearch/TradingAgents
- **解决什么问题**：提供多 Agent LLM 金融交易框架，将交易决策拆分为多个协作 Agent。
- **为什么值得关注**：122k stars，Apache-2.0，是“LLM 多 Agent 交易”方向的标杆项目，7d 仍 +1478 星。
- **技术栈/架构亮点**：多 Agent 协作、LLM 决策、金融数据分析。其 Agent 角色拆分思路值得研究。
- **是否适合借鉴**：适合。可借鉴其多 Agent 角色设计（如分析师、交易员、风控员）到企业级投研 Agent 框架。
- **可能风险**：策略过拟合；LLM 决策不可解释；回测与实盘差距；API key 安全。

### 3.3 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，支持人工或 Agent 自审，宣称 120 秒内给出结论。
- **为什么值得关注**：45k stars，Apache-2.0，7d +1442 星。在 AI Agent 经济中，审计与合规是刚需，尤其对金融 Agent。
- **技术栈/架构亮点**：Agent 评估、幻觉检测、prompt injection 检测、ISO 42001/NIST AI RMF/OWASP LLM 对齐、CLI 诊断工具。
- **是否适合借鉴**：非常适合。金融交易 Agent 尤其需要“决策前审计”和“行为回放”，可将其审计思路集成到交易 Agent 风控层。
- **可能风险**：审计工具本身可能误报/漏报；对复杂金融 Agent 的评估覆盖度有限。

### 3.4 Soniavasseur/Wallet-Risk-Scanner
- **解决什么问题**：多链加密钱包风险扫描，用于 AML/KYT 筛查，0–100 评分，覆盖制裁、风险合约、资金追踪，集成 6 个情报源并支持 failover。
- **为什么值得关注**：24h +428 星，虽然总 star 仅 914，但单日增速极高，说明链上风控需求正在爆发。
- **技术栈/架构亮点**：多情报源 failover、15+ 链支持、批量筛查、TXT/JSON/CSV/HTML/PDF 报告、Python 跨平台。
- **是否适合借鉴**：适合。其“多源情报融合 + failover + 风险评分”架构可迁移到传统金融反欺诈、交易对手风险监控。
- **可能风险**：加密领域合规复杂；情报源质量与覆盖率；误报导致业务中断；项目较新，维护活跃度待观察。

### 3.5 shy3130/tick-stock-panel
- **解决什么问题**：A 股自托管、零运维的“自建策略 + 监控 + 回测”量化工作台，LLM 驱动策略定制、个股分析与复盘。
- **为什么值得关注**：7d +548 星，MIT 协议，技术栈现代（DuckDB、Polars、FastAPI、React）。
- **技术栈/架构亮点**：DuckDB + Polars 本地分析、FastAPI 后端、React 前端、LLM 策略定制、第三方数据源接入。
- **是否适合借鉴**：适合。其“本地优先 + 列式分析 + LLM 辅助策略”架构适合构建低延迟研究环境。
- **可能风险**：A 股数据合规；策略过拟合；个人开源项目维护风险。

### 3.6 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，由 HKUDS 出品，结合 LLM、MCP、多 Agent。
- **为什么值得关注**：38k stars，MIT 协议，学术背景，7d +406 星。
- **技术栈/架构亮点**：MCP 集成、多 Agent、LLM 交易、回测。
- **是否适合借鉴**：适合。MCP 与交易 Agent 的结合是当前热点，可研究其工具调用与 Agent 编排。
- **可能风险**：策略有效性未验证；学术项目与实盘差距；API key 安全。

### 3.7 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，多 Agent 协作完成投研决策。
- **为什么值得关注**：64.6k stars，是“AI 对冲基金”概念的代表项目，长期活跃。
- **技术栈/架构亮点**：多 Agent 角色模拟、回测、Python。
- **是否适合借鉴**：适合。可借鉴其 Agent 角色分工与投研流水线。
- **可能风险**：策略过拟合；回测幸存者偏差；不可直接用于实盘。

### 3.8 JustVugg/colibri
- **解决什么问题**：面向前沿 MoE 模型的分层推理引擎，热专家放 GPU、温专家放 RAM、冷专家从 NVMe 流式加载，用 C 编写。
- **为什么值得关注**：50k stars，Apache-2.0，7d +2179 星。虽然不是金融项目，但对本地运行大模型做量化研究极具价值。
- **技术栈/架构亮点**：CUDA/Vulkan/RAM/NVMe 分层推理，C 实现，硬件利用率高。
- **是否适合借鉴**：适合。金融领域常需在本地跑 LLM 处理敏感数据，该架构可降低推理成本。
- **可能风险**：与金融业务无直接关系；底层推理引擎复杂度高。

### 3.9 CopilotKit/OpenBot
- **解决什么问题**：开源 AI 数字员工，每个 Agent 拥有自己的浏览器、文件和工具，所有动作在执行前决策、执行后记录，支持 AG-UI Agent。
- **为什么值得关注**：11k stars，MIT，24h +302 星。其“动作前决策 + 动作后记录”对交易 Agent 审计极具参考价值。
- **技术栈/架构亮点**：AG-UI、Agent 治理、浏览器自动化、生成式 UI、MCP。
- **是否适合借鉴**：适合。可借鉴其“决策留痕 + 行为回放”机制，增强交易 Agent 可观测性。
- **可能风险**：浏览器自动化风险；Agent 权限控制；与金融交易结合需额外风控。

### 3.10 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 接收前压缩工具输出、日志、文件和 RAG chunk，宣称编码 Agent 减少 20% token，JSON 减少 60–95% token。
- **为什么值得关注**：79k stars，Apache-2.0，7d +525 星。对高频调用 LLM 的金融 Agent 可显著降低成本。
- **技术栈/架构亮点**：库、代理、MCP server 三种形态，FastAPI、LangChain、OpenAI/Anthropic 集成。
- **是否适合借鉴**：适合。金融数据量大，上下文压缩可降低交易 Agent 成本与延迟。
- **可能风险**：压缩可能丢失关键信息；对金融数值精度的影响需验证。

## 4. 趋势归纳

- **技术趋势**：
  - **LLM + 多 Agent 交易框架**持续主导，`TradingAgents`、`Vibe-Trading`、`ai-hedge-fund` 均属此类。
  - **MCP（Model Context Protocol）成为 Agent 工具连接标准**，多个项目围绕 MCP server 构建金融数据与交易能力。
  - **本地优先与低资源推理**兴起，`colibri`、`locally-uncensored`、`atomic-agent`、`Soup` 均强调本地运行、隐私与低成本。
  - **Agent 审计与治理**成为新基建，`iFixAi`、`OpenBot` 强调决策留痕、行为审计、合规对齐。

- **产品趋势**：
  - 从“策略库”转向“AI Agent skill”，交易能力被封装为 Claude/Codex/Cursor 可调用的 skill。
  - 金融产品 UI 与设计系统开始由 Agent 自动生成，`ui-ux-pro-max-skill`、`awesome-design-md`、`open-design` 反映这一趋势。
  - 自托管、零运维的量化工作台受到个人开发者欢迎，如 `tick-stock-panel`。

- **量化/交易策略趋势**：
  - LLM 驱动的个股分析、新闻情绪、决策看板成为主流形态。
  - 回测仍是核心，但越来越多项目将 LLM 作为策略生成与复盘工具。
  - 链上风控（AML/KYT、钱包风险评分）成为加密量化新焦点。

- **AI Agent 与自动化交易结合趋势**：
  - 交易决策被拆分为多 Agent 协作，角色包括分析师、交易员、风控员。
  - Agent 的“决策前审计、执行后记录”机制开始受到重视。
  - 交易 skill 化：`day-trader-skill`、`trader-skill` 将交易流程封装为可复用 skill。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据 Agent 工具层。
  - 带审计留痕的交易 Agent 框架。
  - 本地 LLM + 分层推理的量化研究环境。
  - 多源情报融合的链上/传统金融风控扫描器。

## 5. 今日灵感清单

1. **MVP：LLM 投研日报 Agent**：参考 `daily_stock_analysis`，构建“多源行情 + 新闻 + LLM 摘要 + 定时推送”的个人投研日报工具，使用免费数据源与轻量调度。
2. **MVP：交易 Agent 决策审计层**：参考 `iFixAi` 与 `OpenBot`，为现有交易 Agent 增加“决策前规则检查 + 执行后行为回放”模块，输出审计日志。
3. **调研：MCP 金融数据生态**：基于 `awesome-mcp-servers`、`awesome-remote-mcp-servers`，梳理可用的行情、新闻、链上数据 MCP server，评估接入成本。
4. **调研：本地 LLM 推理成本优化**：研究 `colibri` 的 GPU/RAM/NVMe 分层推理思路，评估在本地量化研究环境中运行开源 LLM 的可行性。
5. **Demo：链上钱包风险评分器**：参考 `Wallet-Risk-Scanner`，用 Python 实现一个简化版多源情报融合的钱包风险评分原型，输出 0–100 分与风险标签。
6. **Demo：A 股本地量化工作台**：参考 `tick-stock-panel`，用 DuckDB + Polars + FastAPI + React 搭建本地回测与监控面板，验证列式分析性能。
7. **Demo：Claude 交易 skill 复现**：研究 `day-trader-skill` 与 `trader-skill` 的 skill 结构，复现一个“新闻事件驱动交易信号”skill，但仅用于研究，不接实盘。
8. **调研：Agent 上下文压缩**：评估 `headroom` 在金融数据场景下的 token 压缩效果与信息保真度，测试 JSON 行情数据压缩率。
9. **Watchlist：TradingAgents、Vibe-Trading、ai-hedge-fund**：持续跟踪多 Agent 交易框架的架构演进与 Agent 角色设计。
10. **Watchlist：iFixAi、OpenBot**：关注 Agent 审计与治理工具的标准化进展，为金融 Agent 合规做准备。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| ZhuLinsen/daily_stock_analysis | 涨星最快，LLM 股票分析流水线值得拆解 |
| TauricResearch/TradingAgents | 多 Agent 交易框架标杆，架构演进值得跟踪 |
| HKUDS/Vibe-Trading | 学术背景，MCP + 多 Agent 交易结合 |
| virattt/ai-hedge-fund | AI 对冲基金概念代表，长期活跃 |
| ifixai-ai/iFixAi | Agent 审计与合规工具，金融 Agent 刚需 |
| CopilotKit/OpenBot | Agent 决策留痕与行为回放机制 |
| shy3130/tick-stock-panel | 现代 A 股量化工作台，DuckDB+Polars 架构 |
| Soniavasseur/Wallet-Risk-Scanner | 链上风控新方向，单日增速极高 |
| JustVugg/colibri | 本地 LLM 分层推理，降低研究成本 |
| headroomlabs-ai/headroom | Agent token 压缩，降低高频 LLM 成本 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-11-10）与 `baseline_7d`（2026-11-04），1 日与 7 日涨星数据基本完整。
- **缺失数据**：`star_delta_30d` 在所有项目中均为 `null`，无法进行 30 日趋势分析。`Wallet-Risk-Scanner` 与 `awesome-telegram` 的 `star_delta_7d` 为 `null`，7 日涨星信息不足。
- **样本偏差**：候选集由多个关键词查询合并而成，导致大量 **awesome-list 类通用项目**（如 `awesome-selfhosted`、`public-apis`、`build-your-own-x`、`awesome-go`、`awesome-python` 等）因 README 或描述中偶然出现“trading bot”“quant”“fintech”等词而被误匹配，并非真正的金融/量化项目。分析时应剔除这些噪声。
- **分类可信度**：`category_guess` 为自动推断，部分项目分类可能不准确；`risk_flags` 与 `risk_level` 为规则生成，仅作参考。
- **数据时间**：报告日期取自 `current_snapshot` 文件名 `2026-11-11`。
