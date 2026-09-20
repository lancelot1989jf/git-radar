# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-19

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 与交易/金融工作流融合**：TradingAgents、Vibe-Trading、QuantDinger、PanWatch 等项目显示，多 Agent LLM 框架正在从“研究 demo”走向“可自托管的盯盘/决策/推送系统”。
  2. **AI Coding Agent 的 Skills/插件生态爆发**：open-design、ui-ux-pro-max-skill、awesome-dsh-plugin、AlphaGBM/skills 等项目表明，围绕 Claude Code / Codex / DeepSeek Harness 的“技能包”正在成为新的分发单元，金融数据与研究工作流开始以 Skills 形式封装。
  3. **本地优先、低资源 AI 推理**：colibri、needle、magnitude、Soup 等项目聚焦消费级硬件上的模型推理与微调，为量化研究中的本地 LLM 部署提供了新的工程选项。

- **是否出现新趋势**：出现。金融/量化项目与 AI Coding Agent 生态的耦合明显加深，尤其是“MCP + Skills + 自托管盯盘”的组合模式。另一个值得注意的趋势是“AI 交易决策每区块/每周期触发”的轻量 Agent 实验（如 jev-trader）。

- **是否出现值得复刻/参考的工程架构**：是。PanWatch 的“自托管 AI 盯盘助手 + TradingAgents 多 Agent 决策 + 全渠道推送”架构，以及 QuantDinger 的“研究/回测/模拟/实盘 + 多租户 SaaS”分层设计，都具有较高的参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明显骗局，但存在大量“awesome-list”类项目因关键词误匹配进入榜单，实际与金融/量化直接相关性较低。部分项目（如 Financial_freedom）标题带有“赚钱投资指南”色彩，应视为内容营销而非工程参考。所有涉及 crypto、trading bot 的项目均需按高风险对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 481677 | +208 | 信息不足 | Python | API 资源列表 | 免费 API 集合列表 | 低 | 中 |
| 2 | vinta/awesome-python | 321789 | +194 | 信息不足 | Python | Python 资源列表 | Python 工具精选列表 | 低 | 低 |
| 3 | nexu-io/open-design | 97132 | +161 | 信息不足 | TypeScript | AI 设计工具 | 本地优先的 AI 设计引擎 | 中 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 320435 | +221 | 信息不足 | 信息不足 | 自托管资源列表 | 自托管服务列表 | 低 | 中 |
| 5 | career-ops-hq/career-ops | 72186 | +101 | 信息不足 | JavaScript | AI 求职工具 | 开源 AI 求职扫描与评估 | 中 | 低 |
| 6 | nextlevelbuilder/ui-ux-pro-max-skill | 129119 | +246 | 信息不足 | Python | AI 设计 Skill | 多平台 UI/UX 设计智能 Skill | 中 | 低 |
| 7 | avelino/awesome-go | 184823 | +119 | 信息不足 | Go | Go 资源列表 | Go 框架与库精选列表 | 低 | 中 |
| 8 | JustVugg/colibri | 36446 | +245 | 信息不足 | C | 本地模型推理 | 纯 C 零依赖 MoE 推理引擎 | 高 | 低 |
| 9 | TauricResearch/TradingAgents | 107649 | +139 | 信息不足 | Python | AI 交易框架 | 多 Agent LLM 金融交易框架 | 高 | 低 |
| 10 | headroomlabs-ai/headroom | 73131 | +154 | 信息不足 | Python | LLM 上下文压缩 | 压缩工具输出与日志以节省 token | 高 | 低 |
| 11 | awesome-dsh-plugin/awesome-dsh-plugin | 16311 | +101 | 信息不足 | Python | DeepSeek Harness 插件列表 | DSH 插件精选列表 | 中 | 低 |
| 12 | codecrafters-io/build-your-own-x | 548290 | +175 | 信息不足 | Markdown | 编程教程列表 | 从零复刻技术的教程集合 | 中 | 中 |
| 13 | VoltAgent/awesome-design-md | 116718 | +137 | 信息不足 | 信息不足 | 设计系统列表 | DESIGN.md 设计系统分析集合 | 中 | 中 |
| 14 | cactus-compute/needle | 11675 | +313 | 信息不足 | Python | 端侧 AI 模型 | 微型设备自动化基础模型 | 高 | 中 |
| 15 | ZhuLinsen/daily_stock_analysis | 65336 | +71 | 信息不足 | Python | AI 股票分析 | LLM 多市场股票智能分析系统 | 高 | 低 |
| 16 | Open-Dev-Society/OpenStock | 16218 | +605 | 信息不足 | TypeScript | 行情平台 | 开源实时行情与提醒平台 | 高 | 低 |
| 17 | jarrodwatts/jev-trader | 1344 | +417 | 信息不足 | TypeScript | AI 交易实验 | 每区块一次 AI 交易决策 | 中 | 低 |
| 18 | AlphaGBM/skills | 2979 | +122 | 信息不足 | Python | 金融数据 Skills | 29 个开源市场数据与研究 Skills | 高 | 低 |
| 19 | ruvnet/ruflo | 72875 | +65 | 信息不足 | TypeScript | Agent 编排框架 | 多智能体 swarm 编排框架 | 中 | 低 |
| 20 | virattt/ai-hedge-fund | 63564 | +64 | 信息不足 | Python | AI 对冲基金模拟 | AI 对冲基金团队模拟 | 高 | 低 |
| 21 | ripienaar/free-for-dev | 137805 | +54 | 信息不足 | HTML | 免费资源列表 | SaaS/PaaS/IaaS 免费层列表 | 低 | 低 |
| 22 | punkpeye/awesome-mcp-servers | 95300 | +57 | 信息不足 | 信息不足 | MCP 服务器列表 | MCP 服务器集合 | 中 | 低 |
| 23 | TNT-Likely/PanWatch | 1029 | +104 | 信息不足 | Python | AI 盯盘助手 | 自托管 AI 盯盘与多 Agent 决策 | 高 | 中 |
| 24 | unslothai/unsloth | 76455 | +53 | 信息不足 | Python | LLM 微调 | 本地 LLM 训练与推理 UI | 中 | 低 |
| 25 | OpenBB-finance/OpenBB | 73272 | +52 | 信息不足 | Python | 金融数据平台 | 面向分析师与 AI Agent 的开放数据平台 | 高 | 中 |
| 26 | MakazhanAlpamys/Soup | 6888 | +67 | 信息不足 | Python | LLM 微调 | 单 YAML 微调 LLM | 中 | 低 |
| 27 | magnitudedev/magnitude | 4709 | +61 | 信息不足 | TypeScript | 本地推理引擎 | 消费级硬件推理引擎 | 中 | 低 |
| 28 | HKUDS/Vibe-Trading | 33701 | +36 | 信息不足 | Python | AI 交易 Agent | 个人交易 Agent | 高 | 中 |
| 29 | garrytan/gbrain | 30154 | +35 | 信息不足 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | 中 | 低 |
| 30 | CopilotKit/OpenBot | 5186 | +45 | 信息不足 | TypeScript | AI 自动化 | 开源 AI 数字员工 | 中 | 中 |
| 31 | ifixai-ai/iFixAi | 15615 | +39 | 信息不足 | Python | AI Agent 审计 | AI Agent 独立审计 | 高 | 低 |
| 32 | kvmem/kvmem-llama.cpp | 313 | +96 | 信息不足 | C++ | LLM 推理 | llama.cpp 相关 KV 内存项目 | 中 | 低 |
| 33 | tradesdontlie/tradingview-mcp | 6571 | +66 | 信息不足 | JavaScript | TradingView MCP | 连接 Claude Code 与 TradingView | 中 | 中 |
| 34 | logicrw/awesome-jev-projects | 129 | +83 | 信息不足 | JavaScript | Jev 生态雷达 | Jev 开源生态雷达 | 低 | 低 |
| 35 | OpenByteInc/QuantDinger | 11758 | +38 | 信息不足 | Python | AI 交易 OS | 开源 AI 交易 OS 与多租户 SaaS | 高 | 中 |
| 36 | HiThink-Tech/Financial-API | 3646 | +46 | 信息不足 | TypeScript | A 股金融数据 API | 同花顺官方 A 股数据服务 | 高 | 低 |
| 37 | codeman008/Financial_freedom | 3924 | +73 | 信息不足 | 信息不足 | 投资指南 | 赚钱投资指南 | 低 | 中 |
| 38 | anbeime/skill | 6975 | +40 | 信息不足 | Python | Skills 商店 | AI Agent 技能包商店 | 中 | 低 |
| 39 | awesomedata/awesome-public-datasets | 79046 | +16 | 信息不足 | 信息不足 | 数据集列表 | 高质量开放数据集列表 | 中 | 中 |
| 40 | fffaraz/awesome-cpp | 73363 | +14 | 信息不足 | 信息不足 | C++ 资源列表 | C/C++ 框架与库精选 | 低 | 低 |
| 41 | josephmisiti/awesome-machine-learning | 74377 | +8 | 信息不足 | Python | ML 资源列表 | 机器学习框架与库精选 | 低 | 低 |
| 42 | Developer-Y/cs-video-courses | 83543 | +7 | 信息不足 | 信息不足 | 课程列表 | 计算机科学视频课程列表 | 低 | 中 |
| 43 | code-yeongyu/oh-my-openagent | 69205 | +7 | 信息不足 | TypeScript | Agent 编排 | 图工程 Agent 编排工具 | 中 | 低 |
| 44 | vuejs/awesome-vue | 73547 | -1 | 信息不足 | 信息不足 | Vue 资源列表 | Vue.js 精选资源 | 低 | 低 |
| 45 | ByteByteGoHq/system-design-101 | 89435 | +55 | 信息不足 | 信息不足 | 系统设计 | 系统设计图解 | 中 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents

- **项目解决什么问题**：提供多 Agent LLM 金融交易框架，将交易决策拆分为多个协作 Agent，用于研究与模拟交易决策流程。
- **为什么最近值得关注**：24h 涨星 +139，总 star 超 10 万，且近 30 天有 push。作为“AI 交易 Agent”方向的代表性项目，持续吸引关注。
- **技术栈/架构亮点**：Python + Apache-2.0；多 Agent 架构，topics 包含 agent、finance、llm、multiagent、trading。其“多 Agent 协作决策”模式是当前 AI 交易研究的主流范式。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其多 Agent 角色分工思路可迁移到企业级投研 Agent、风控 Agent 的架构设计中。
- **可能的风险**：作为研究工具，策略表现未经真实市场验证；多 Agent LLM 决策存在幻觉与一致性问题；不应直接用于实盘。

### 3.2 ZhuLinsen/daily_stock_analysis

- **项目解决什么问题**：LLM 驱动的多市场股票智能分析系统，整合多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。
- **为什么最近值得关注**：总 star 6.5 万+，24h 涨星 +71，近 30 天有 push。中文项目，聚焦 A 股场景，对国内开发者参考价值高。
- **技术栈/架构亮点**：Python + MIT；topics 包含 a-stock、ai-agent、llm、quant、quantitative-finance、quantitative-trading。架构上强调“多源数据 + LLM 分析 + 看板 + 推送”的闭环。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其“定时运行 + 自动推送”的轻量 Agent 模式，可作为企业级投研日报自动化的原型参考。
- **可能的风险**：LLM 生成的“分析结论”可能包含幻觉；A 股数据源合规性需关注；不应将分析结果直接作为交易信号。

### 3.3 Open-Dev-Society/OpenStock

- **项目解决什么问题**：开源市场平台，提供实时价格跟踪、个性化提醒和公司洞察，定位为昂贵市场平台的免费替代品。
- **为什么最近值得关注**：24h 涨星 +605，是本次候选集中单日涨星最高的项目之一，总 star 1.6 万+，近 30 天有 push。
- **技术栈/架构亮点**：TypeScript + AGPL-3.0；topics 包含 nextjs、shadcn-ui、tailwindcss、inngest、coderabbit。采用现代 Web 技术栈，强调实时性与用户体验。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合作为行情展示与提醒系统的产品参考，尤其是实时数据推送与个性化提醒的产品设计。
- **可能的风险**：AGPL-3.0 许可证对商业闭源使用有限制；行情数据源稳定性与合规性需自行评估。

### 3.4 TNT-Likely/PanWatch

- **项目解决什么问题**：自托管 AI 盯盘助手，集成 TradingAgents 多 Agent 投资决策，支持 A 股/港股/美股实时监控、持仓管理、智能分析与全渠道推送。
- **为什么最近值得关注**：虽然总 star 仅 1029，但 24h 涨星 +104，增速显著；近 30 天有 push。它是“TradingAgents + 自托管盯盘”组合的典型落地案例。
- **技术栈/架构亮点**：Python + MIT；topics 包含 a-share、ai-agent、akshare、deepseek、fastapi、langgraph、llm、mcp、pwa、quant、self-hosted、trading-agents、trading-bot。架构上整合了数据源（akshare）、Agent 框架（langgraph）、服务层（fastapi）与前端（PWA）。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其“自托管 + 多 Agent 决策 + 全渠道推送”的架构，可作为企业级智能投研助手 MVP 的直接参考。
- **可能的风险**：标记为 trading_bot，风险等级中；涉及真实持仓管理，需注意数据安全与决策责任边界；不应直接接入实盘交易。

### 3.5 OpenByteInc/QuantDinger

- **项目解决什么问题**：开源 AI 交易 OS，支持 Agent 交易、vibe trading、Jev System One 集成，覆盖研究、Python 策略编写、回测、模拟/实盘交易，并可启动多租户交易 SaaS。
- **为什么最近值得关注**：总 star 1.1 万+，24h 涨星 +38，近 30 天有 push。其“交易 OS + 多租户 SaaS”的定位在开源项目中较为少见。
- **技术栈/架构亮点**：Python + Apache-2.0；topics 包含 agent、alpaca、backtesting、binance、crypto、forex、mcp-server、quant、saas、stocks、strategy、trade、typesafe-ai。架构上覆盖从研究到实盘再到 SaaS 商业化的完整链路。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合。其“研究-回测-模拟-实盘”分层设计，以及“多租户 SaaS + 计费/支付/结算”的商业化架构，值得企业级交易平台参考。
- **可能的风险**：涉及 crypto、实盘交易与多租户 SaaS，风险等级中；直接运行或接入真实 API key 存在资金与安全风险；多租户架构下的合规与风控复杂度高。

### 3.6 virattt/ai-hedge-fund

- **项目解决什么问题**：模拟 AI 对冲基金团队，通过多个 AI Agent 协作完成投资研究与决策。
- **为什么最近值得关注**：总 star 6.3 万+，24h 涨星 +64，近 30 天有 push。是“AI 对冲基金”概念的代表性开源项目。
- **技术栈/架构亮点**：Python + MIT；topics 为空，但描述明确指向 AI 对冲基金团队模拟。其价值在于概念验证与教学，而非生产级交易系统。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：适合作为多 Agent 投研流程的教学与原型参考，但不建议直接用于实盘。
- **可能的风险**：研究工具属性明显；模拟结果不代表真实收益；存在策略过拟合与回测幸存者偏差风险。

### 3.7 AlphaGBM/skills

- **项目解决什么问题**：将实时市场数据和研究工作流引入 Claude Code、Cursor 等 AI Coding CLI，提供 29 个面向股票、期权和大宗商品的开源 Skills。
- **为什么最近值得关注**：总 star 2979，24h 涨星 +122，增速较快；近 30 天有 push。代表了“金融数据能力以 Skills 形式封装给 AI Coding Agent”的新趋势。
- **技术栈/架构亮点**：Python + MIT；topics 为空。核心价值在于将金融数据获取与研究流程标准化为可被 AI Agent 调用的 Skills。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。这种“金融数据 Skills”模式可直接复用到企业级投研 Agent 的工具层设计中。
- **可能的风险**：研究工具属性；数据源质量与延迟需验证；Skills 的维护活跃度需持续观察。

### 3.8 HiThink-Tech/Financial-API

- **项目解决什么问题**：同花顺官方 A 股金融数据服务，提供实时/历史行情、财务报表、指数、板块、涨停等数据，支持 API、MCP、CLI 和 Python。
- **为什么最近值得关注**：总 star 3646，24h 涨星 +46，近 30 天有 push。官方背景使其在 A 股数据合规性与稳定性上具有独特价值。
- **技术栈/架构亮点**：TypeScript + MIT；topics 包含 a-share、ai-agent、duckdb、financial-data、mcp、npm-package、quantitative-finance、rest-api。支持 MCP 与 CLI，便于 AI Agent 集成。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。官方数据源 + MCP 接口的组合，是企业级 A 股投研 Agent 的理想数据底座。
- **可能的风险**：数据服务条款与使用限制需关注；作为数据依赖方，需评估服务稳定性与长期维护承诺。

### 3.9 ifixai-ai/iFixAi

- **项目解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它应该做的事”，可在 120 秒内给出审计结果。
- **为什么最近值得关注**：总 star 1.5 万+，24h 涨星 +39，近 30 天有 push。随着 AI Agent 进入交易与金融场景，Agent 审计与治理成为关键需求。
- **技术栈/架构亮点**：Python + Apache-2.0；topics 包含 agent-evaluation、ai-governance、ai-safety、eu-ai-act、iso-42001、nist-ai-rmf、owasp-llm、prompt-injection、risk-management。覆盖 AI 治理、安全与合规标准。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。在交易 Agent 上线前引入独立审计层，是风控架构的重要补充。
- **可能的风险**：审计能力本身依赖 LLM，存在误判可能；不应将其作为唯一风控手段。

### 3.10 JustVugg/colibri

- **项目解决什么问题**：在现有硬件上运行前沿 MoE 模型，纯 C 实现、零依赖，专家从磁盘流式加载。
- **为什么最近值得关注**：24h 涨星 +245，总 star 3.6 万+，近 30 天有 push。其“纯 C、零依赖、磁盘流式加载专家”的工程思路对资源受限环境下的 LLM 部署有启发。
- **技术栈/架构亮点**：C + Apache-2.0；topics 为空。强调极简依赖与流式加载，适合嵌入式或低资源场景。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：可作为本地 LLM 推理引擎的备选方案，尤其适合对延迟和资源敏感的边缘部署场景。
- **可能的风险**：项目较新，生态与文档可能不完善；与金融场景的直接结合需自行验证。

## 4. 趋势归纳

- **技术趋势**：
  - **MCP 与 Skills 成为 AI Agent 能力分发的标准单元**：AlphaGBM/skills、HiThink-Tech/Financial-API、awesome-mcp-servers、anbeime/skill 等项目显示，金融数据与研究能力正被封装为 MCP server 或 Skills，供 Claude Code、Codex、Cursor 等 CLI 调用。
  - **本地优先与低资源推理**：colibri、needle、magnitude、Soup、unsloth 等项目聚焦消费级硬件上的模型推理与微调，降低 AI 能力的部署门槛。
  - **多 Agent 编排框架成熟**：ruflo、oh-my-openagent、gbrain 等项目提供多 Agent 编排、swarm 协作与自适应记忆能力。

- **产品趋势**：
  - **自托管 AI 盯盘/投研助手**：PanWatch、daily_stock_analysis 等项目将 AI 分析、实时监控与推送结合，形成“个人/团队级投研助手”产品形态。
  - **开源交易 OS 与 SaaS 化**：QuantDinger 尝试将交易系统与多租户 SaaS 商业化结合，显示开源交易项目向平台化演进的趋势。
  - **AI 设计/UI 生成与金融产品结合**：open-design、ui-ux-pro-max-skill、awesome-design-md 等项目虽非金融专属，但其“AI 生成 dashboard/landing page”能力可加速金融产品原型开发。

- **量化/交易策略趋势**：
  - **LLM 多 Agent 决策**：TradingAgents、Vibe-Trading、ai-hedge-fund 等项目持续探索 LLM 在交易决策中的角色，但多数仍处于研究/模拟阶段。
  - **高频/区块级 AI 决策实验**：jev-trader 提出“每个区块一次 AI 交易决策”，显示 AI 交易正在向更高频、更自动化的方向试探。
  - **Jev System One / typesafe-ai 概念出现**：QuantDinger、awesome-jev-projects 等项目提及 Jev 模型与 typesafe AI，可能是新兴的决策模型范式，值得后续观察。

- **AI Agent 与自动化交易结合趋势**：
  - **从“AI 辅助分析”向“AI 驱动决策”演进**：但多数项目仍停留在模拟与研究阶段，真正可靠的自动化交易闭环尚未形成。
  - **Agent 审计与治理需求上升**：iFixAi 等项目的出现，说明 AI Agent 进入金融场景后，审计、合规与风控成为必须配套的能力。

- **值得后续做原型验证的方向**：
  1. 基于 MCP + Skills 的企业级投研数据层。
  2. 自托管多 Agent 盯盘助手（参考 PanWatch 架构）。
  3. 本地低资源 LLM 推理引擎在量化研究中的应用。
  4. AI Agent 独立审计层在交易系统风控中的集成。

## 5. 今日灵感清单

1. **MVP：企业级投研日报 Agent**：参考 daily_stock_analysis 与 PanWatch，构建一个自托管的多源行情 + LLM 分析 + 定时推送的投研日报系统，使用 HiThink-Tech/Financial-API 作为 A 股数据源，通过 MCP 集成到 Claude Code 或 Codex。
2. **MVP：金融数据 Skills 包**：参考 AlphaGBM/skills，将常用金融数据获取（行情、财报、板块、涨停）封装为 5-10 个标准化 Skills，供 AI Coding CLI 调用，形成可复用的团队工具层。
3. **调研：MCP 在金融数据服务中的标准化程度**：对比 HiThink-Tech/Financial-API、OpenBB、awesome-mcp-servers 中金融相关 MCP server 的接口设计，总结可复用的数据服务抽象模式。
4. **调研：本地低资源 LLM 推理引擎的量化研究适用性**：评估 colibri、needle、magnitude 在金融文本分析、新闻情绪提取等任务上的性能与资源消耗，探索本地化部署的可行性。
5. **Demo：AI Agent 审计层原型**：参考 iFixAi，为 TradingAgents 或 Vibe-Trading 的多 Agent 决策流程增加一个独立审计 Agent，输出决策合规性与一致性报告。
6. **Demo：AI 生成金融 Dashboard**：使用 open-design 或 ui-ux-pro-max-skill，让 Codex/Claude Code 自动生成一个行情监控 Dashboard 原型，验证 AI 设计工具在金融产品原型开发中的效率。
7. **原型：多 Agent 交易决策沙箱**：参考 ai-hedge-fund 与 TradingAgents，搭建一个完全离线的多 Agent 交易决策沙箱，使用模拟数据验证 Agent 协作流程，不接入任何真实交易接口。
8. **Watchlist：OpenStock**：关注其产品化路径与实时数据架构，作为开源行情平台的产品参考。
9. **Watchlist：QuantDinger**：关注其“交易 OS + 多租户 SaaS”架构演进，尤其是计费、支付与结算模块的设计。
10. **调研：Jev System One / typesafe-ai 概念**：通过 awesome-jev-projects 与 QuantDinger 的 topics，初步了解 Jev 决策模型与 typesafe AI 的技术主张，判断是否值得深入跟进。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | AI 多 Agent 交易框架的代表项目，持续活跃，适合跟踪多 Agent 决策范式演进。 |
| TNT-Likely/PanWatch | “自托管盯盘 + TradingAgents 集成”的落地案例，架构参考价值高，增速显著。 |
| OpenByteInc/QuantDinger | 开源交易 OS 与多租户 SaaS 的少见组合，商业化架构值得观察。 |
| Open-Dev-Society/OpenStock | 单日涨星最高之一，开源行情平台产品化路径清晰。 |
| AlphaGBM/skills | 金融数据 Skills 化的先行项目，代表 AI Coding Agent 与金融工作流融合趋势。 |
| HiThink-Tech/Financial-API | 官方 A 股数据服务，支持 MCP，是企业级 A 股投研 Agent 的潜在数据底座。 |
| ifixai-ai/iFixAi | AI Agent 审计与治理方向，金融场景风控的关键配套能力。 |
| HKUDS/Vibe-Trading | 学术背景的 AI 交易 Agent 项目，适合跟踪研究与工程结合的最新进展。 |
| virattt/ai-hedge-fund | AI 对冲基金模拟的经典项目，适合作为多 Agent 投研教学与原型参考。 |
| JustVugg/colibri | 纯 C 零依赖 MoE 推理引擎，低资源 LLM 部署的潜力方案。 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-09-18.json`，当前快照为 `2026-09-19.json`，1 日涨星数据可用。
- **7 日基线**：缺失，`baseline_7d` 为 `null`，因此所有项目的 7d 涨星均标记为“信息不足”。
- **30 日涨星**：所有项目的 `star_delta_30d` 均为 `null`，无法提供 30 日趋势分析。
- **采集失败**：本次数据中未发现明确的采集失败标记，但部分项目（如 kvmem-llama.cpp）描述为 `null`，信息完整性受限。
- **样本偏差**：候选集中包含大量“awesome-list”类项目（如 public-apis、awesome-python、awesome-go、awesome-selfhosted 等），它们因关键词误匹配进入榜单，与金融/量化/自动化交易的直接相关性较低，可能稀释了真正金融项目的信号。分析时应重点关注 category_guess 与 topics 中明确包含 trading、quant、finance、fintech 的项目。
