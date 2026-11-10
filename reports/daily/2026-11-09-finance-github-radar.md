# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-11-09

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **LLM 驱动的多市场股票分析系统**：以 `daily_stock_analysis` 为代表，24h 涨星 +916，将多源行情、实时新闻、决策看板与自动推送整合为“零成本定时运行”的 AI 分析工作台。
  2. **AI Agent 审计与治理**：`iFixAi` 提出“AI Agent 独立审计”概念，覆盖 AI alignment、EU AI Act、ISO 42001、NIST AI RMF、OWASP LLM 等合规框架，对金融场景中的 Agent 治理有直接借鉴价值。
  3. **AI Agent 技能生态与设计智能**：`ui-ux-pro-max-skill`、`open-design`、`agentic-awesome-skills` 等项目显示“Agent Skills”正在成为新的可复用能力单元，金融产品 UI、交易看板、风控面板可借此快速生成。

- **是否出现新趋势**：出现。候选集中大量项目围绕 **Claude/Codex/Cursor 的“Skill”生态**展开，说明 AI Agent 能力正在从“通用对话”转向“可复用、可审计、可组合的技能包”。同时，**本地优先（local-first）** 与 **自托管（self-hosted）** 在 AI 工具中明显升温。

- **是否出现值得复刻/参考的工程架构**：出现。`colibri` 的 MoE 分层推理引擎（GPU/RAM/NVMe 三级缓存）展示了在消费级硬件上运行大模型的高效架构；`headroom` 的 token 压缩代理/MCP server 对降低金融数据喂给 LLM 的成本有直接工程价值。

- **是否有明显骗局、过度营销或高风险项目**：候选集中存在明显**误匹配**项目，如 `Turnitout-Humanizer`（学术抄袭规避工具）被归入 risk_management/trading_bot，实际与金融无关且用途存疑。另有多个 `awesome-*` 列表类项目因关键词命中被误分类为 trading_bot，需谨慎解读。未发现直接诱导输入真实 API key 的明显骗局，但所有 trading_bot 标记项目均不应直接实盘运行。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ui-ux-pro-max-skill | 147502 | +461 | +2621 | Python | fintech_product | AI 驱动的跨平台 UI/UX 设计技能包 | 金融产品 UI 快速生成 | 低 |
| 2 | awesome-selfhosted | 335598 | +347 | +2082 | 无 | trading_bot(误匹配) | 自托管网络服务列表 | 自托管金融工具选型 | 中 |
| 3 | colibri | 49521 | +351 | +2110 | C | quant_research | MoE 模型分层推理引擎 | 消费级硬件跑大模型 | 低 |
| 4 | build-your-own-x | 561431 | +269 | +1906 | Markdown | trading_bot(误匹配) | 从零复刻技术的教程合集 | 复刻交易系统组件 | 中 |
| 5 | public-apis | 497738 | +365 | +1814 | Python | crypto/quant/risk | 免费 API 合集 | 金融数据源调研 | 中 |
| 6 | awesome-dsh-plugin | 24113 | +218 | +1816 | JavaScript | trading_infra | DeepSeek Harness 插件列表 | Agent 插件生态参考 | 低 |
| 7 | daily_stock_analysis | 69267 | +916 | +1749 | Python | ai_trading/data_eng/quant | LLM 多市场股票分析系统 | AI 投研工作台架构 | 低 |
| 8 | awesome-python | 333683 | +181 | +1371 | Python | quant_research | Python 工具精选列表 | 量化工具链选型 | 低 |
| 9 | day-trader-skill | 6469 | +233 | +1445 | Python | backtesting/risk | 11 个日内交易 Claude 技能 | 交易决策 Agent 技能化 | 低 |
| 10 | TradingAgents | 121725 | +297 | +1274 | Python | ai_trading/backtesting | 多 Agent LLM 金融交易框架 | 多 Agent 投研架构 | 低 |
| 11 | iFixAi | 44488 | +252 | +1221 | Python | ai_trading/risk | AI Agent 独立审计工具 | Agent 合规与风控 | 低 |
| 12 | open-design | 106913 | +205 | +1092 | TypeScript | fintech_product | 协作式 AI 设计工作台 | 金融看板/原型协作 | 低 |
| 13 | awesome-go | 193049 | +165 | +1081 | Go | trading_bot(误匹配) | Go 框架与库精选列表 | 低延迟交易基础设施选型 | 中 |
| 14 | awesome-design-md | 126383 | +174 | +871 | 无 | crypto/fintech | 品牌设计系统 DESIGN.md 合集 | 金融产品设计规范 | 中 |
| 15 | gbrain | 32322 | +524 | +814 | TypeScript | fintech_product | OpenClaw/Hermes Agent 大脑 | Agent 编排框架参考 | 低 |
| 16 | free-for-dev | 142406 | +100 | +621 | HTML | fintech/quant | 开发者免费资源列表 | 低成本金融工具栈 | 低 |
| 17 | Kronos | 47460 | +94 | +834 | Python | backtesting/quant | 金融市场基础模型 | 金融时序基础模型 | 低 |
| 18 | ruflo | 81386 | +81 | +565 | TypeScript | ai_trading/backtesting | 多智能体 swarm 编排框架 | Agent 集群编排 | 低 |
| 19 | awesome-mac | 118173 | +94 | +472 | Swift | trading_infra(误匹配) | macOS 软件精选列表 | 交易终端工具选型 | 低 |
| 20 | headroom | 79273 | +90 | +493 | Python | ai_trading/risk | LLM 上下文 token 压缩 | 金融数据喂 LLM 降本 | 低 |
| 21 | OpenBot | 10598 | +89 | +534 | TypeScript | fintech/trading_bot | 开源 AI 数字员工 | 浏览器自动化 Agent | 中 |
| 22 | awesome-claude-code | 57657 | +84 | +447 | Python | ai_trading/quant | Claude Code 资源精选 | Agent 工具链调研 | 低 |
| 23 | tick-stock-panel | 7466 | +86 | +466 | Python | ai_trading/backtesting | A 股自建策略+监控+回测工作台 | A 股量化工作台架构 | 低 |
| 24 | logo-design-skill | 6444 | +75 | +515 | HTML | fintech_product | AI Logo 设计技能包 | 金融品牌视觉生成 | 低 |
| 25 | 500-AI-Agents-Projects | 39554 | +106 | +265 | Python | risk/trading_bot | 500 个 AI Agent 用例合集 | 金融 Agent 用例灵感 | 中 |
| 26 | Vibe-Trading | 37981 | +57 | +392 | Python | ai_trading/backtesting | 个人交易 Agent | 交易 Agent 产品化 | 低 |
| 27 | awesome-remote-mcp-servers | 2901 | +70 | +353 | 无 | ai_trading/crypto | 远程 MCP server 合集 | 金融数据 MCP 接入 | 中 |
| 28 | agentic-awesome-skills | 49442 | +56 | +324 | Python | backtesting | 2955+ 可复用 Agent 技能 | 技能目录与发现机制 | 低 |
| 29 | locally-uncensored | 3669 | +56 | +447 | TypeScript | ai_trading/quant | 本地 AI 一体化桌面应用 | 本地化 AI 工作台 | 低 |
| 30 | awesome-mcp-servers | 97551 | +48 | +281 | 无 | fintech_product | MCP server 合集 | 金融工具 MCP 化 | 低 |
| 31 | goose | 3379 | +50 | +417 | C++ | trading_infra | Goose 编程语言 | 高性能系统语言调研 | 低 |
| 32 | Soup | 10395 | +61 | +284 | Python | ai_trading/quant | 单 YAML 微调 LLM | 低资源金融模型微调 | 低 |
| 33 | cs-video-courses | 84783 | +47 | +234 | 无 | quant/trading_bot(误匹配) | CS 视频课程列表 | 量化/ML 基础学习 | 中 |
| 34 | trader-skill | 1615 | +38 | +412 | Python | 无 | 11 个投资者复刻 Claude 技能 | 投研决策技能化 | 低 |
| 35 | OpenBB | 75290 | +36 | +223 | Python | crypto/quant | 分析师/量化/AI Agent 开放数据平台 | 金融数据平台架构 | 中 |
| 36 | prompt-master | 15776 | +40 | +301 | 无 | ai_trading/fintech | 精准 prompt 编写技能 | 金融 prompt 工程 | 低 |
| 37 | awesome-telegram | 1033 | +372 | 无 | JavaScript | quant/trading_bot | Telegram 频道/群/机器人导航 | 交易信号渠道调研 | 中 |
| 38 | Orkas | 9156 | +36 | +163 | JavaScript | backtesting | 本地优先 AI 团队桌面应用 | 多 Agent 任务编排 | 低 |
| 39 | ai-hedge-fund | 64603 | +21 | +131 | Python | backtesting/risk | AI 对冲基金团队 | 多角色投研 Agent | 低 |
| 40 | awesome-cpp | 74346 | +22 | +125 | 无 | quant/trading_infra | C++ 资源精选 | 低延迟系统选型 | 低 |
| 41 | oh-my-openagent | 70812 | +18 | +128 | TypeScript | quant_research | 图工程 Agent 编排 | Agent 工作流编排 | 低 |
| 42 | awesome-rust | 60434 | +21 | +116 | Rust | ai_trading/backtesting | Rust 资源精选 | 高性能量化系统选型 | 中 |
| 43 | Turnitout-Humanizer | 12024 | +52 | 无 | HTML | risk/trading_bot(误匹配) | 学术抄袭规避工具 | 无（与金融无关） | 中 |
| 44 | awesome-public-datasets | 80005 | +16 | +62 | 无 | crypto_trading | 高质量开放数据集列表 | 金融数据集调研 | 中 |
| 45 | awesome-machine-learning | 74788 | +3 | +45 | Python | ai_trading | ML 框架与库精选 | 金融 ML 工具链 | 低 |
| 46 | awesome-vue | 73479 | -5 | -11 | 无 | quant_research(误匹配) | Vue.js 资源精选 | 金融前端选型 | 低 |

## 3. 重点项目深度分析

### 3.1 daily_stock_analysis（ZhuLinsen/daily_stock_analysis）
- **解决什么问题**：将多源行情、实时新闻、LLM 分析与决策看板整合为多市场股票智能分析系统，支持零成本定时运行。
- **为什么值得关注**：24h 涨星 +916，为候选集中单日涨星最高；topics 同时覆盖 `ai-agent`、`llm`、`quant`、`quantitative-trading`，是“LLM + 量化投研”落地的典型样本。
- **技术栈/架构亮点**：Python + LLM 驱动，多源数据接入，自动推送与定时任务。可作为“AI 投研工作台”的参考架构。
- **是否适合借鉴**：适合。其“多源数据 → LLM 分析 → 决策看板 → 自动推送”的流水线可直接映射到企业级投研 Agent 框架。
- **可能风险**：金融合规风险（自动推送可能被解读为投资建议）；LLM 输出稳定性；数据源授权与延迟；策略过拟合风险。

### 3.2 TradingAgents（TauricResearch/TradingAgents）
- **解决什么问题**：提供多 Agent LLM 金融交易框架，将交易决策拆分为多个协作 Agent。
- **为什么值得关注**：stars 121725，7d 涨星 +1274，是候选集中最成熟的“多 Agent 交易框架”之一。
- **技术栈/架构亮点**：Python + Apache-2.0，多 Agent 协作，覆盖 finance/trading 场景。
- **是否适合借鉴**：适合。其多 Agent 角色分工（如分析师、交易员、风控）可作为企业级 Agent 框架的蓝本。
- **可能风险**：策略过拟合；回测与实盘差异；LLM 幻觉导致错误交易信号；维护活跃度需持续观察。

### 3.3 iFixAi（ifixai-ai/iFixAi）
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”，可在 120 秒内给出结论。
- **为什么值得关注**：topics 覆盖 `ai-governance`、`ai-safety`、`eu-ai-act`、`iso-42001`、`nist-ai-rmf`、`owasp-llm`、`prompt-injection`，是金融场景中 Agent 治理与合规的稀缺样本。
- **技术栈/架构亮点**：Python + Apache-2.0，支持人类或 Agent 自身运行审计，覆盖幻觉检测、LLM 安全、风险评估。
- **是否适合借鉴**：非常适合。金融企业部署 AI Agent 前，可借鉴其审计框架构建内部 Agent 合规检查层。
- **可能风险**：审计标准仍在演进；对金融交易场景的适配度需验证；误报/漏报可能影响决策。

### 3.4 colibri（JustVugg/colibri）
- **解决什么问题**：为前沿 MoE 模型提供分层推理引擎，热专家放 GPU（CUDA/Vulkan）、温专家放 RAM、冷专家从 NVMe 流式加载。
- **为什么值得关注**：C 语言实现，Apache-2.0，7d 涨星 +2110，展示了在消费级硬件上运行大模型的工程路径。
- **技术栈/架构亮点**：GPU/RAM/NVMe 三级缓存分层，C 语言高性能实现。
- **是否适合借鉴**：适合。金融场景中本地化部署 LLM 时，可借鉴其分层推理思路降低硬件成本。
- **可能风险**：与金融业务无直接关联；C 代码维护门槛高；硬件兼容性风险。

### 3.5 headroom（headroomlabs-ai/headroom）
- **解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前进行压缩，降低 token 消耗。
- **为什么值得关注**：宣称对 coding agent 减少 20% token，对 JSON 减少 60-95% token，且答案不变；提供 library、proxy、MCP server 三种形态。
- **技术栈/架构亮点**：Python + Apache-2.0，支持 FastAPI、LangChain、MCP，可作为 LLM 数据管道的中间层。
- **是否适合借鉴**：非常适合。金融行情、订单簿、新闻流等数据量大，喂给 LLM 前压缩可显著降本。
- **可能风险**：压缩可能损失关键金融信息；需验证在数值型金融数据上的保真度。

### 3.6 tick-stock-panel（shy3130/tick-stock-panel）
- **解决什么问题**：A 股“自建策略 + 监控 + 回测”量化工作台，支持 LLM 驱动策略定制、个股分析与复盘。
- **为什么值得关注**：topics 覆盖 `duckdb`、`polars`、`fastapi`、`react`、`ai-agent`，是 A 股场景下现代数据栈 + LLM 的典型组合。
- **技术栈/架构亮点**：DuckDB + Polars 做本地分析，FastAPI + React 做服务与前端，LLM 做策略定制。
- **是否适合借鉴**：适合。其“本地数据引擎 + 现代 Web 框架 + LLM 策略层”的组合可复用到其他市场。
- **可能风险**：A 股数据合规；策略过拟合；回测幸存者偏差；个人开源项目维护持续性。

### 3.7 ai-hedge-fund（virattt/ai-hedge-fund）
- **解决什么问题**：模拟 AI 对冲基金团队，多角色 Agent 协作完成投资决策。
- **为什么值得关注**：stars 64603，是“AI 对冲基金”概念的开源代表，常被用于教学与原型验证。
- **技术栈/架构亮点**：Python + MIT，多角色 Agent 模拟。
- **是否适合借鉴**：适合作为多角色投研 Agent 的教学原型，但不建议直接用于实盘。
- **可能风险**：策略过拟合；回测与实盘差异；LLM 幻觉；金融合规风险。

### 3.8 OpenBB（openbq-org/OpenBB）
- **解决什么问题**：为分析师、量化与 AI Agent 提供开放数据平台。
- **为什么值得关注**：stars 75290，topics 覆盖 `equity`、`options`、`fixed-income`、`crypto`、`derivatives`、`quantitative-finance`，是金融数据平台的重要开源项目。
- **技术栈/架构亮点**：Python，多资产类别数据接入，面向 AI Agent 的数据接口。
- **是否适合借鉴**：适合。可作为金融数据层与 AI Agent 之间的标准化接口参考。
- **可能风险**：数据源授权与稳定性；与 AI Agent 集成的成熟度需验证。

### 3.9 Vibe-Trading（HKUDS/Vibe-Trading）
- **解决什么问题**：定位为“个人交易 Agent”，结合 LLM、MCP、多 Agent 与回测。
- **为什么值得关注**：来自 HKUDS，topics 覆盖 `ai-agent`、`algorithmic-trading`、`backtesting`、`mcp`、`multi-agent`，是学术机构在“Vibe Trading”方向的探索。
- **技术栈/架构亮点**：Python + MIT，MCP 集成，多 Agent 架构。
- **是否适合借鉴**：适合作为“LLM + MCP + 交易”的学术原型参考。
- **可能风险**：策略过拟合；学术原型与生产系统差距大；金融合规风险。

### 3.10 Kronos（shiyu-coder/Kronos）
- **解决什么问题**：定位为“金融市场语言的基础模型”。
- **为什么值得关注**：stars 47460，是金融时序基础模型方向的代表项目。
- **技术栈/架构亮点**：Python + MIT，基础模型路线。
- **是否适合借鉴**：适合作为金融基础模型研究方向的跟踪对象。
- **可能风险**：模型泛化能力存疑；金融数据分布漂移；回测过拟合。

## 4. 趋势归纳

### 技术趋势
- **Agent Skills 生态崛起**：大量项目围绕 Claude/Codex/Cursor 的“Skill”能力展开，技能包正在成为可复用、可分发、可审计的 Agent 能力单元。
- **本地优先与自托管**：`locally-uncensored`、`Orkas`、`awesome-selfhosted` 等项目显示 AI 工具向本地化、隐私保护方向演进。
- **MCP 成为数据接入标准**：`awesome-mcp-servers`、`awesome-remote-mcp-servers`、`headroom` 等项目表明 MCP 正在成为 AI Agent 连接外部工具与数据的通用协议。
- **token 压缩与上下文工程**：`headroom` 等项目聚焦降低 LLM 推理成本，对金融大数据场景尤为重要。

### 产品趋势
- **AI 投研工作台一体化**：`daily_stock_analysis`、`tick-stock-panel` 将行情、新闻、LLM 分析、看板、推送整合为单一产品。
- **AI Agent 治理产品化**：`iFixAi` 将 Agent 审计、合规、安全评估产品化，金融场景需求明确。
- **设计智能与金融产品结合**：`ui-ux-pro-max-skill`、`open-design`、`awesome-design-md` 显示金融产品 UI/看板可通过 AI 设计技能快速生成。

### 量化/交易策略趋势
- **LLM 多 Agent 投研**：`TradingAgents`、`ai-hedge-fund`、`Vibe-Trading` 均采用多 Agent 协作模式。
- **金融基础模型**：`Kronos` 代表“金融市场语言基础模型”方向，值得长期跟踪。
- **A 股量化工作台**：`tick-stock-panel`、`daily_stock_analysis` 显示 A 股场景的 LLM 量化工具在升温。

### AI Agent 与自动化交易结合趋势
- **交易决策技能化**：`day-trader-skill`、`trader-skill` 将交易决策流程封装为 Claude 技能，强调“不自动下单、需人工确认”。
- **Agent 审计前置**：`iFixAi` 的审计理念与交易 Agent 结合，可能成为金融 Agent 部署的标配。
- **数据接入 MCP 化**：金融数据源通过 MCP server 接入 Agent，降低集成成本。

### 值得后续做原型验证的方向
- 金融数据 → token 压缩 → LLM 分析的降本流水线。
- 多角色投研 Agent 的沙箱化回测与审计。
- 基于 Agent Skills 的金融产品 UI 快速生成。
- 本地优先的 A 股量化工作台。

## 5. 今日灵感清单

1. **MVP：金融数据 token 压缩代理**：参考 `headroom`，构建一个面向行情/订单簿/新闻的压缩代理，验证在金融数据上喂给 LLM 的降本效果与信息保真度。
2. **MVP：多角色投研 Agent 沙箱**：参考 `TradingAgents` 与 `ai-hedge-fund`，搭建一个只做回测、不接实盘的多角色投研 Agent 沙箱，内置审计日志。
3. **调研：Agent Skills 的金融场景适配**：调研 `agentic-awesome-skills`、`day-trader-skill`、`trader-skill`，评估将交易决策流程技能化的可行性。
4. **调研：MCP 金融数据源生态**：调研 `awesome-mcp-servers` 与 `awesome-remote-mcp-servers` 中金融相关 MCP server，梳理可复用的数据接入层。
5. **Demo：AI 生成金融看板**：参考 `ui-ux-pro-max-skill` 与 `open-design`，让 Codex/Agent 自动生成一个交易监控看板原型。
6. **原型：Agent 审计层**：参考 `iFixAi`，为内部 AI Agent 构建一个轻量审计层，覆盖 prompt injection、幻觉检测、合规检查。
7. **调研：本地化 LLM 推理架构**：调研 `colibri` 的分层推理思路，评估在本地部署金融 LLM 的硬件成本优化空间。
8. **Watchlist：金融基础模型**：将 `Kronos` 加入 watchlist，跟踪金融时序基础模型的进展。
9. **原型：A 股量化工作台**：参考 `tick-stock-panel` 的 DuckDB + Polars + FastAPI + React 架构，搭建一个本地 A 股策略回测原型。
10. **调研：自托管金融工具栈**：从 `awesome-selfhosted` 中筛选金融相关自托管工具，评估构建私有化投研环境的可行性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| daily_stock_analysis | 单日涨星最高，LLM 投研工作台代表，架构可直接借鉴 |
| TradingAgents | 多 Agent 交易框架成熟样本，适合长期跟踪架构演进 |
| iFixAi | AI Agent 审计与合规稀缺项目，金融 Agent 治理刚需 |
| headroom | token 压缩对金融大数据场景降本价值明确 |
| tick-stock-panel | A 股量化工作台，DuckDB+Polars+LLM 架构值得复刻 |
| Kronos | 金融基础模型方向，长期研究价值高 |
| OpenBB | 金融数据平台与 AI Agent 接口标准化的重要项目 |
| colibri | 本地化大模型推理架构，硬件成本优化参考 |
| Vibe-Trading | 学术机构在 LLM+MCP+交易方向的探索，值得跟踪 |
| ai-hedge-fund | AI 对冲基金概念原型，适合教学与沙箱验证 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日/7 日基线**：本次报告提供了 `baseline_1d`（2026-11-08）与 `baseline_7d`（2026-11-03），但部分项目（如 `awesome-telegram`、`Turnitout-Humanizer`）的 `star_delta_7d` 为 null，说明 7 日基线数据缺失或项目创建时间晚于基线日期。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 null，无法评估中期涨星趋势。
- **采集失败**：未发现明确采集失败标记，但部分项目 7d 涨星缺失可能由基线文件缺失或项目新建导致。
- **样本偏差**：候选集由关键词搜索（如 "trading bot"、"quant"、"backtesting"、"fintech" 等）生成，导致大量 `awesome-*` 列表类项目因 README 关键词命中被纳入，并被误分类为 trading_bot/quant_research。这些项目与金融/量化交易无直接关系，解读时需剔除噪声。此外，`Turnitout-Humanizer` 等明显无关项目也被纳入，进一步说明分类准确性有限。
