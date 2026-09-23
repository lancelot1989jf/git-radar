# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-22

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 与交易决策系统融合**：`jev-trader`、`TradingAgents`、`PanWatch`、`Vibe-Trading` 等项目显示，LLM 多 Agent 框架正在从“研究 demo”走向“可部署的盯盘/决策/推送系统”。
  2. **A 股本地化投研数据与 Agent 生态**：`a-stock-data`、`TradingAgents-astock`、`daily_stock_analysis` 等项目集中出现，反映中文市场对“免 Key 数据源 + 多 Agent 投研 + 自托管”的强需求。
  3. **AI 辅助工程基础设施泛化**：`headroom`、`colibri`、`needle`、`Soup` 等项目虽非直接交易系统，但涉及 token 压缩、本地 MoE 推理、端侧模型、低显存微调，对构建低成本、本地化的量化 Agent 基础设施有直接借鉴价值。

- **是否出现新趋势**：出现“Jev / System One”相关生态项目（`jev-trader`、`awesome-jev`、`awesome-jev-projects`、`QuantDinger`），围绕“类型化 AI 决策模型”形成小型生态，但项目普遍很新、star 基数低，需谨慎观察。

- **是否出现值得复刻/参考的工程架构**：`PanWatch` 的“自托管 AI 盯盘助手 + TradingAgents 多 Agent 决策 + 全渠道推送”架构较完整；`a-stock-data` 的“15 层 / 87 端点 / 34 数据源”数据工程抽象值得参考；`OpenStock` 的实时行情 + 个性化提醒 + 公司洞察产品形态清晰。

- **是否有明显骗局、过度营销或高风险项目**：本次候选列表中未发现明确骗局项目，但 `QuantDinger`、`Vibe-Trading`、`jev-trader` 等涉及 crypto、自动交易、SaaS 多租户交易系统的项目，存在明显营销化描述和资金风险，应视为高风险研究对象而非可直接运行的工具。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Open-Dev-Society/OpenStock | 18436 | +481 | +2823 | TypeScript | 股票市场产品 | 开源实时行情、提醒与公司洞察平台 | 高 | 低 |
| 2 | nextlevelbuilder/ui-ux-pro-max-skill | 129939 | +291 | +1066 | Python | AI 设计技能 | 面向多平台的 UI/UX 设计智能技能 | 中 | 低 |
| 3 | jarrodwatts/jev-trader | 2092 | +204 | +1165 | TypeScript | AI 交易 | 每个 Monad 区块生成一个 AI 交易决策 | 高 | 低 |
| 4 | public-apis/public-apis | 482394 | +263 | +925 | Python | API 列表 | 免费 API 集合列表 | 中 | 中 |
| 5 | JustVugg/colibri | 37178 | +261 | +977 | C | 本地 MoE 推理 | 纯 C、零依赖、从磁盘流式加载专家的 MoE 推理引擎 | 高 | 低 |
| 6 | awesome-selfhosted/awesome-selfhosted | 321118 | +237 | +904 | 无 | 自托管列表 | 可自托管网络服务与 Web 应用列表 | 中 | 中 |
| 7 | vinta/awesome-python | 322388 | +199 | +793 | Python | Python 资源列表 | Python 工具选型权威列表 | 中 | 低 |
| 8 | VoltAgent/awesome-design-md | 117370 | +235 | +789 | 无 | 设计系统 | 品牌设计系统 DESIGN.md 文件集合 | 中 | 中 |
| 9 | cactus-compute/needle | 12251 | +164 | +889 | Python | 端侧基础模型 | 面向微型设备的自动化基础模型 | 高 | 中 |
| 10 | nexu-io/open-design | 97691 | +180 | +720 | TypeScript | AI 设计工具 | 本地优先的 AI 设计引擎 | 中 | 低 |
| 11 | codecrafters-io/build-your-own-x | 548865 | +187 | +750 | Markdown | 编程教程 | 从零重建技术的教程集合 | 中 | 中 |
| 12 | TauricResearch/TradingAgents | 108191 | +194 | +681 | Python | 多 Agent 交易框架 | LLM 多 Agent 金融交易框架 | 高 | 低 |
| 13 | headroomlabs-ai/headroom | 73553 | +126 | +576 | Python | Token 压缩 | 压缩工具输出、日志、文件与 RAG 块 | 高 | 低 |
| 14 | avelino/awesome-go | 185197 | +130 | +493 | Go | Go 资源列表 | Go 框架与库精选列表 | 中 | 中 |
| 15 | awesome-dsh-plugin/awesome-dsh-plugin | 16649 | +94 | +439 | Python | 插件列表 | DeepSeek Harness 插件精选列表 | 中 | 低 |
| 16 | career-ops-hq/career-ops | 72461 | +89 | +376 | JavaScript | AI 求职工具 | 开源 AI 求职扫描与简历优化工具 | 低 | 低 |
| 17 | TNT-Likely/PanWatch | 1324 | +108 | +399 | Python | AI 盯盘助手 | 自托管 AI 盯盘助手，集成 TradingAgents | 高 | 中 |
| 18 | CopilotKit/OpenBot | 5401 | +110 | +260 | TypeScript | AI Agent 治理 | 每个 AI 协作者拥有独立浏览器、文件与工具 | 高 | 中 |
| 19 | ruvnet/ruflo | 73094 | +75 | +284 | TypeScript | Agent 编排框架 | 多智能体 swarm 与自主工作流框架 | 高 | 低 |
| 20 | ZhuLinsen/daily_stock_analysis | 65515 | +58 | +250 | Python | 股票分析系统 | LLM 驱动多市场股票智能分析系统 | 高 | 低 |
| 21 | magnitudedev/magnitude | 4872 | +93 | +224 | TypeScript | 本地推理引擎 | 面向消费级硬件的开源推理引擎 | 中 | 低 |
| 22 | ripienaar/free-for-dev | 138020 | +49 | +269 | HTML | 免费资源列表 | DevOps 免费层服务列表 | 低 | 低 |
| 23 | OpenByteInc/QuantDinger | 12026 | +63 | +306 | Python | AI 交易 OS | 开源 AI 交易 OS、agent 交易与多租户交易 SaaS | 高 | 中 |
| 24 | HKUDS/Vibe-Trading | 33861 | +59 | +196 | Python | AI 交易 Agent | 个人交易 Agent | 高 | 中 |
| 25 | simonlin1212/TradingAgents-astock | 3521 | +92 | +148 | Python | A 股多 Agent 投研 | 7 位分析师辩论决策的 A 股投研框架 | 高 | 低 |
| 26 | unslothai/unsloth | 76604 | +55 | +202 | Python | LLM 微调 | 本地运行与训练 LLM 的 UI | 中 | 低 |
| 27 | logicrw/awesome-jev-projects | 400 | +65 | +354 | JavaScript | Jev 生态雷达 | Jev 开源生态项目雷达 | 中 | 低 |
| 28 | punkpeye/awesome-mcp-servers | 95444 | +36 | +201 | 无 | MCP 服务器列表 | MCP 服务器集合 | 中 | 低 |
| 29 | simonlin1212/a-stock-data | 10171 | +147 | +227 | Python | A 股数据工具包 | 15 层、87 端点、34 数据源的 A 股数据包 | 高 | 中 |
| 30 | yibie/awesome-jev | 1347 | +291 | 信息不足 | Python | Jev 生态列表 | Jev 公共项目与集成列表 | 中 | 中 |
| 31 | OpenBB-finance/OpenBB | 73391 | +35 | +171 | Python | 开放数据平台 | 面向分析师、量化与 AI Agent 的开放数据平台 | 高 | 中 |
| 32 | ByteByteGoHq/system-design-101 | 89802 | +121 | +422 | 无 | 系统设计 | 用可视化解释复杂系统 | 中 | 低 |
| 33 | calesthio/Crucix | 11947 | +77 | +194 | JavaScript | 智能情报 Agent | 多数据源监控与变化提醒的个人情报 Agent | 高 | 低 |
| 34 | garrytan/gbrain | 30248 | +34 | +129 | TypeScript | Agent 大脑 | OpenClaw/Hermes Agent 大脑 | 中 | 低 |
| 35 | code-yeongyu/oh-my-openagent | 69306 | +36 | +108 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中 | 低 |
| 36 | MakazhanAlpamys/Soup | 7017 | +39 | +196 | Python | LLM 微调 | 一个 YAML 微调 LLM，4GB 显存训练 8B 模型 | 高 | 低 |
| 37 | kvmem/kvmem-llama.cpp | 514 | +57 | +297 | C++ | 本地推理 | llama.cpp 相关 KV 内存项目 | 中 | 低 |
| 38 | virattt/ai-hedge-fund | 63673 | +15 | +173 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 39 | fffaraz/awesome-cpp | 73424 | +19 | +75 | 无 | C++ 资源列表 | C/C++ 框架与库精选列表 | 中 | 低 |
| 40 | josephmisiti/awesome-machine-learning | 74410 | +20 | +41 | Python | ML 资源列表 | 机器学习框架与库精选列表 | 中 | 低 |
| 41 | awesomedata/awesome-public-datasets | 79106 | +13 | +76 | 无 | 数据集列表 | 高质量开放数据集列表 | 中 | 中 |
| 42 | Developer-Y/cs-video-courses | 83554 | +8 | +18 | 无 | 课程列表 | 计算机科学视频课程列表 | 低 | 中 |
| 43 | vuejs/awesome-vue | 73547 | +1 | -1 | 无 | Vue 资源列表 | Vue.js 相关资源精选列表 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 Open-Dev-Society/OpenStock

- **解决什么问题**：替代昂贵的市场数据平台，提供实时价格、个性化提醒和公司洞察，强调“永久免费、开放构建”。
- **为什么值得关注**：24h +481、7d +2823，是本次候选中最强的产品型涨星项目；AGPL-3.0 协议、TypeScript/Next.js 技术栈，产品形态清晰。
- **技术栈/架构亮点**：Next.js + TailwindCSS + shadcn-ui + Inngest，说明采用现代 Web 全栈 + 事件驱动任务调度；Inngest 适合定时行情抓取、提醒触发等场景。
- **是否适合借鉴**：适合。可作为“开源金融信息产品”的参考架构，尤其是实时行情、提醒系统、公司洞察的产品分层。
- **可能风险**：AGPL-3.0 对商业闭源集成有传染性；行情数据源合规性需自行核实；项目较新，长期维护活跃度待观察。

### 3.2 jarrodwatts/jev-trader

- **解决什么问题**：每个 Monad 区块生成一个 AI 交易决策，针对 Kuru 上的 MON-USDC 交易对。
- **为什么值得关注**：7d +1165，创建仅约一周，是“AI 交易 + 区块级决策”的极端实验性项目。
- **技术栈/架构亮点**：TypeScript；将 AI 决策频率与区块链出块频率绑定，体现“事件驱动 + 高频决策”的架构思路。
- **是否适合借鉴**：可借鉴其“外部事件触发 AI 决策”的框架，但不建议直接复刻交易逻辑。
- **可能风险**：项目极新、star 基数低；描述过于简单，策略有效性未知；涉及链上资产，存在资金风险；不应输入真实私钥或 API key。

### 3.3 TauricResearch/TradingAgents

- **解决什么问题**：提供 LLM 多 Agent 金融交易框架，模拟分析师、交易员、风控等多角色协作。
- **为什么值得关注**：108k stars，7d +681，是 AI 交易研究领域的标杆项目；Apache-2.0 协议，适合二次开发。
- **技术栈/架构亮点**：Python；多 Agent 架构，topic 包含 agent、finance、llm、multiagent、trading。
- **是否适合借鉴**：非常适合。可作为企业级 Agent 投研框架的参考，尤其是多角色辩论、决策流程、风控角色设计。
- **可能风险**：研究工具属性强，回测结果不代表实盘；策略过拟合风险；不应直接用于真实资金交易。

### 3.4 TNT-Likely/PanWatch

- **解决什么问题**：自托管 AI 盯盘助手，集成 TradingAgents 多 Agent 投资决策，支持 A 股/港股/美股实时监控、持仓管理、智能分析、全渠道推送。
- **为什么值得关注**：虽然 star 仅 1324，但 24h +108、7d +399，增速快；是“TradingAgents 工程化落地”的代表。
- **技术栈/架构亮点**：Python + FastAPI + LangGraph + MCP + PWA；集成 akshare、DeepSeek、OpenAI；自托管架构。
- **是否适合借鉴**：非常适合。其“多 Agent 决策 + 实时监控 + 推送”的闭环设计，可直接作为 AI 盯盘/投研助手 MVP 的参考。
- **可能风险**：涉及 trading-bot 标记，存在自动交易风险；A 股数据源稳定性与合规性需关注；不应输入真实券商 API key。

### 3.5 simonlin1212/a-stock-data

- **解决什么问题**：提供 A 股全栈数据工具包，覆盖行情 K 线、逐笔、研报、资金面、新闻、财务、公告、期权、宏观、期货等 15 层、87 端点、34 数据源，除 iwencai 外免 Key。
- **为什么值得关注**：24h +147、7d +227，增速快；对 AI Agent 友好的数据层设计是量化投研的基础设施。
- **技术栈/架构亮点**：Python；分层数据抽象；多数据源聚合；面向 AI Agent 和 Claude Code 的接口设计。
- **是否适合借鉴**：非常适合。可作为“金融数据工程 + AI Agent 数据接入层”的参考，尤其是多源聚合、免 Key 数据源选型。
- **可能风险**：数据源合规性与稳定性风险；涉及杠杆/网格相关标记，需注意数据用途边界；不应将数据直接用于自动交易决策。

### 3.6 OpenByteInc/QuantDinger

- **解决什么问题**：开源 AI 交易 OS，支持 agent 交易、vibe trading、Jev System One 集成，可研究、构建 Python 策略、回测、paper/live 交易，并支持多租户交易 SaaS。
- **为什么值得关注**：7d +306，功能覆盖面广，是“AI 交易 OS + SaaS 化”的典型尝试。
- **技术栈/架构亮点**：Python + Apache-2.0；集成 Alpaca、Binance、MCP server；多市场、多租户、计费支付结算。
- **是否适合借鉴**：可借鉴其“策略研究-回测-模拟-实盘”全流程产品化思路，以及多租户 SaaS 架构。
- **可能风险**：涉及 crypto、自动交易、多租户资金结算，风险极高；不应直接运行或输入真实 API key；营销化描述明显，需谨慎评估。

### 3.7 HKUDS/Vibe-Trading

- **解决什么问题**：个人交易 Agent，强调“Vibe-Trading”概念。
- **为什么值得关注**：33.8k stars，HKUDS 出品，学术背景较强；7d +196。
- **技术栈/架构亮点**：Python + MIT；topic 包含 ai-agent、algorithmic-trading、backtesting、llm、mcp、multi-agent。
- **是否适合借鉴**：适合作为“学术研究型 AI 交易 Agent”的参考，尤其是多 Agent 与 MCP 集成。
- **可能风险**：涉及 crypto 与自动交易；研究工具属性强，回测结果不代表实盘；不应输入真实 API key。

### 3.8 virattt/ai-hedge-fund

- **解决什么问题**：模拟 AI 对冲基金团队，多角色协作进行投资决策。
- **为什么值得关注**：63.7k stars，是 AI 交易领域的知名教育/研究项目；7d +173。
- **技术栈/架构亮点**：Python + MIT；多 Agent 对冲基金团队模拟。
- **是否适合借鉴**：适合作为“多角色 Agent 投研流程”的教学与原型参考。
- **可能风险**：研究工具属性强；策略过拟合与回测幸存者偏差风险；不应直接用于实盘。

### 3.9 headroomlabs-ai/headroom

- **解决什么问题**：在 LLM 接收前压缩工具输出、日志、文件、RAG 块，降低 token 消耗。
- **为什么值得关注**：73.5k stars，7d +576；对构建高频调用 LLM 的量化 Agent 系统有直接成本优化价值。
- **技术栈/架构亮点**：Python + Apache-2.0；支持 library、proxy、MCP server 三种形态；FastAPI、LangChain 集成。
- **是否适合借鉴**：非常适合。可作为“AI Agent 上下文工程与成本控制”的基础组件，尤其适合行情数据、日志、研报等长文本场景。
- **可能风险**：压缩可能损失关键信息，需在金融场景中谨慎验证；依赖 LLM 生态变化。

### 3.10 JustVugg/colibri

- **解决什么问题**：在已有硬件上运行前沿 MoE 模型，纯 C、零依赖、专家从磁盘流式加载。
- **为什么值得关注**：37.2k stars，7d +977；为本地化、低成本运行大模型提供新路径。
- **技术栈/架构亮点**：C + Apache-2.0；流式专家加载，降低内存占用。
- **是否适合借鉴**：适合。可用于构建本地化、低成本的量化研究 LLM 推理环境，减少对云端 API 的依赖。
- **可能风险**：项目较新，兼容性与稳定性待观察；与金融场景无直接绑定，需自行验证推理质量。

## 4. 趋势归纳

- **技术趋势**：
  - **多 Agent 金融决策框架工程化**：从 `TradingAgents` 到 `PanWatch`、`TradingAgents-astock`，多 Agent 投研正在从研究框架走向可部署系统。
  - **本地化与低成本 LLM 推理**：`colibri`、`needle`、`magnitude`、`Soup`、`unsloth` 等项目集中出现，反映“本地推理 + 低显存微调 + 端侧部署”趋势。
  - **上下文工程与 token 优化**：`headroom` 等项目显示，Agent 系统的成本与上下文管理成为独立技术方向。
  - **MCP 生态扩展**：`awesome-mcp-servers`、`a-stock-data`、`QuantDinger` 等均涉及 MCP，说明 MCP 正在成为金融数据与工具接入的标准接口。

- **产品趋势**：
  - **自托管 AI 盯盘/投研助手**：`PanWatch`、`daily_stock_analysis` 等强调自托管、零成本定时运行、全渠道推送。
  - **开源金融信息产品**：`OpenStock` 以“免费替代昂贵市场平台”为卖点，产品形态清晰。
  - **AI 交易 OS 与 SaaS 化**：`QuantDinger` 尝试将 AI 交易能力产品化为多租户 SaaS。

- **量化/交易策略趋势**：
  - **AI 决策与事件驱动结合**：`jev-trader` 将 AI 决策与区块事件绑定，体现“事件驱动 + AI 决策”的策略框架。
  - **A 股本地化策略研究**：`TradingAgents-astock`、`a-stock-data` 显示 A 股数据源与多 Agent 投研的本地化需求强烈。
  - **研究工具与实盘边界模糊**：多个项目同时提供回测、paper trading、live trading，需警惕策略过拟合与实盘风险。

- **AI Agent 与自动化交易结合趋势**：
  - **Agent 治理与可观测性**：`OpenBot` 强调“每个动作决定前记录、执行后审计”，为自动化交易 Agent 提供治理思路。
  - **多 Agent 协作与角色分工**：分析师、交易员、风控等角色分工成为主流设计。
  - **本地优先与 BYOK**：多个项目强调本地优先、自带 Key，降低数据泄露风险。

- **值得后续做原型验证的方向**：
  - 基于 `TradingAgents` + `a-stock-data` 的 A 股多 Agent 投研 MVP。
  - 基于 `headroom` 的金融数据 token 压缩层。
  - 基于 `colibri` 或 `magnitude` 的本地量化研究 LLM 推理环境。
  - 基于 `OpenBot` 的 Agent 治理与审计框架，用于自动化交易决策留痕。

## 5. 今日灵感清单

1. **MVP：A 股多 Agent 投研助手**：参考 `PanWatch` 与 `TradingAgents-astock`，用 `a-stock-data` 作为数据层，构建“数据采集 → 多 Agent 分析 → 决策看板 → 推送”的最小闭环。
2. **MVP：金融数据 token 压缩代理**：基于 `headroom` 构建一个面向行情数据、研报、公告的压缩代理，验证在量化 Agent 场景下的 token 节省与信息保真度。
3. **调研：本地 MoE 推理在量化研究中的可行性**：调研 `colibri` 与 `magnitude`，评估在消费级硬件上运行本地 LLM 进行财报分析、新闻情绪提取的可行性。
4. **调研：MCP 在金融数据接入中的标准化**：调研 `awesome-mcp-servers` 与 `a-stock-data`，梳理金融数据 MCP server 的接口设计与安全边界。
5. **Demo：Agent 决策审计与治理**：参考 `OpenBot` 的“决定前记录、执行后审计”思路，为自动化交易 Agent 构建决策留痕与回放 demo。
6. **Demo：事件驱动 AI 决策框架**：参考 `jev-trader` 的“外部事件触发 AI 决策”思路，构建一个基于行情事件或新闻事件的 AI 决策原型。
7. **调研：低显存 LLM 微调在金融文本任务中的应用**：调研 `Soup` 与 `unsloth`，评估在 4GB 显存环境下微调金融情感分类或研报摘要模型的可行性。
8. **Watchlist：`OpenStock`**：观察其产品化路径与实时行情架构，作为开源金融信息产品的参考。
9. **Watchlist：`QuantDinger`**：观察其 AI 交易 OS 与多租户 SaaS 架构演进，但不建议直接运行或投入资金。
10. **原型：自托管 AI 盯盘系统**：参考 `daily_stock_analysis` 的“零成本定时运行 + 自动推送”设计，构建一个自托管、低成本的盯盘原型。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| Open-Dev-Society/OpenStock | 产品形态清晰，涨星强劲，适合观察开源金融信息产品演进 |
| TauricResearch/TradingAgents | AI 多 Agent 交易框架标杆，适合持续跟踪架构演进 |
| TNT-Likely/PanWatch | TradingAgents 工程化落地代表，适合观察自托管 AI 盯盘助手方向 |
| simonlin1212/a-stock-data | A 股数据工程基础设施，适合观察金融数据层与 AI Agent 集成 |
| OpenByteInc/QuantDinger | AI 交易 OS 与多租户 SaaS 尝试，适合观察产品化路径，但风险高 |
| HKUDS/Vibe-Trading | 学术背景的 AI 交易 Agent，适合观察研究趋势 |
| virattt/ai-hedge-fund | AI 对冲基金团队模拟，适合作为教学与研究参考 |
| headroomlabs-ai/headroom | token 压缩基础设施，适合观察 Agent 成本优化方向 |
| JustVugg/colibri | 本地 MoE 推理引擎，适合观察本地化 LLM 推理趋势 |
| CopilotKit/OpenBot | Agent 治理与审计框架，适合观察自动化 Agent 安全与可观测性方向 |
| jarrodwatts/jev-trader | 事件驱动 AI 交易实验，适合观察新范式，但风险高 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：已提供 `baseline_1d: 2026-09-21.json`，1 日涨星数据完整。
- **7 日基线**：已提供 `baseline_7d: 2026-09-18.json`，但 `yibie/awesome-jev` 的 `star_delta_7d` 为 null，可能因项目创建时间晚于 7 日基线或基线数据缺失，该项 7 日涨星信息不足。
- **30 日涨星**：所有项目的 `star_delta_30d` 均为 null，本次报告无法提供 30 日涨星数据。
- **采集失败**：未发现明确采集失败标记，但 `kvmem/kvmem-llama.cpp` 的 description 为 null，信息不足。
- **样本偏差**：候选列表由关键词匹配生成，包含大量 awesome-list、通用 API 列表、设计工具等非直接金融项目，说明关键词匹配存在噪声；同时，高 star 通用项目可能挤占垂直金融项目的排名空间。报告中的“主题/分类”来自 `category_guess` 与 `matched_queries`，仅作为参考，不代表项目真实定位。
