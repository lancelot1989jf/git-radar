# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-09-20

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 交易框架**：TradingAgents、QuantDinger、Vibe-Trading 等 LLM 多 Agent 交易框架持续高热，AI 决策与交易执行链路正在产品化。
  2. **AI 设计/前端生成与金融产品结合**：open-design、ui-ux-pro-max-skill 等“设计智能体”项目涨星极快，可显著降低金融数据看板、交易终端、风控仪表盘的 UI 构建成本。
  3. **本地化/边缘侧模型推理**：colibri、needle、ds4 等项目聚焦在已有硬件上运行前沿 MoE/小模型，为自托管量化研究、私有数据推理提供新选项。

- **是否出现新趋势**：出现。Jev/System One 决策模型相关项目（jev-trader、awesome-jev-projects、awesome-jev-typesafe）在极短时间内集中出现并快速涨星，显示“类型化决策模型 + AI 交易”可能成为新的叙事热点，但项目极新、生态未验证，需谨慎观察。

- **是否出现值得复刻/参考的工程架构**：是。QuantDinger 的“多租户交易 SaaS + 内置用户管理/计费/结算”架构、OpenStock 的实时行情 + 个性化告警 + 公司洞察产品形态、TradingAgents 的多 Agent 投研决策流水线，均具备较高参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本次候选集中未发现明确骗局，但多个项目存在“过度营销”措辞（如“vibe trading”“AI Trading OS”“master of graph engineering”），且 jev-trader、awesome-jev-* 等项目创建时间极短、star 基数低，需警惕叙事驱动型项目。所有 crypto/trading bot 类项目均需按高风险对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 481922 | +245 | 信息不足 | Python | API 资源清单 | 免费 API 聚合列表 | 数据源发现 | 中 |
| 2 | vinta/awesome-python | 321996 | +207 | 信息不足 | Python | Python 资源清单 | Python 工具选型清单 | 技术选型参考 | 低 |
| 3 | nexu-io/open-design | 97339 | +207 | 信息不足 | TypeScript | AI 设计/Agent | 本地优先的 AI 设计引擎 | 金融 UI 快速生成 | 低 |
| 4 | awesome-selfhosted/awesome-selfhosted | 320650 | +215 | 信息不足 | 无 | 自托管清单 | 可自托管服务清单 | 交易系统自托管选型 | 中 |
| 5 | nextlevelbuilder/ui-ux-pro-max-skill | 129389 | +270 | 信息不足 | Python | AI 设计技能 | 多平台 UI/UX 设计智能技能 | 前端 Agent 技能 | 低 |
| 6 | avelino/awesome-go | 184950 | +127 | 信息不足 | Go | Go 资源清单 | Go 框架/库精选清单 | 低延迟交易基建选型 | 中 |
| 7 | ripienaar/free-for-dev | 137906 | +101 | 信息不足 | HTML | 免费资源清单 | SaaS/PaaS/IaaS 免费层清单 | 低成本原型验证 | 低 |
| 8 | JustVugg/colibri | 36629 | +183 | 信息不足 | C | 本地模型推理 | 纯 C 零依赖运行前沿 MoE 模型 | 本地量化推理引擎 | 低 |
| 9 | career-ops-hq/career-ops | 72280 | +94 | 信息不足 | JavaScript | AI Agent 工具 | 开源 AI 求职代理 | Agent 工作流参考 | 低 |
| 10 | TauricResearch/TradingAgents | 107834 | +185 | 信息不足 | Python | AI 交易/多 Agent | 多 Agent LLM 金融交易框架 | 投研 Agent 架构 | 低 |
| 11 | headroomlabs-ai/headroom | 73289 | +158 | 信息不足 | Python | LLM 上下文压缩 | 工具输出/日志/JSON 压缩 | 降低 Agent token 成本 | 低 |
| 12 | awesome-dsh-plugin/awesome-dsh-plugin | 16437 | +126 | 信息不足 | Python | 插件清单 | DeepSeek Harness 插件列表 | Agent 插件生态观察 | 低 |
| 13 | codecrafters-io/build-your-own-x | 548496 | +206 | 信息不足 | Markdown | 教程清单 | 从零复刻技术项目教程 | 复刻交易系统 demo | 中 |
| 14 | VoltAgent/awesome-design-md | 116911 | +193 | 信息不足 | 无 | 设计系统清单 | DESIGN.md 设计系统集合 | Agent 生成 UI 规范 | 中 |
| 15 | OpenByteInc/QuantDinger | 11858 | +100 | 信息不足 | Python | AI 交易/量化 | 开源 AI Trading OS/多租户交易 SaaS | 交易 SaaS 架构 | 中 |
| 16 | cactus-compute/needle | 11936 | +261 | 信息不足 | Python | 边缘 AI | 微型设备自动化基础模型 | 边缘侧决策模型 | 中 |
| 17 | Open-Dev-Society/OpenStock | 16990 | +772 | 信息不足 | TypeScript | 行情产品 | 开源实时行情与告警平台 | 行情产品 MVP | 低 |
| 18 | ruvnet/ruflo | 72954 | +79 | 信息不足 | TypeScript | Agent 框架 | 多智能体 swarm 编排框架 | 多 Agent 编排 | 低 |
| 19 | jarrodwatts/jev-trader | 1598 | +254 | 信息不足 | TypeScript | AI 交易 | 每区块一次 AI 交易决策 | 高频决策实验 | 低 |
| 20 | virattt/ai-hedge-fund | 63637 | +73 | 信息不足 | Python | AI 交易/回测 | AI 对冲基金团队模拟 | 多角色投研 Agent | 低 |
| 21 | AlphaGBM/skills | 3130 | +151 | 信息不足 | Python | 行情数据技能 | 29 个开源市场数据 Skills | 行情数据接入 Agent | 低 |
| 22 | ZhuLinsen/daily_stock_analysis | 65387 | +51 | 信息不足 | Python | LLM 股票分析 | LLM 多市场股票智能分析 | 决策看板/推送 | 低 |
| 23 | punkpeye/awesome-mcp-servers | 95356 | +56 | 信息不足 | 无 | MCP 清单 | MCP server 集合 | 工具接入参考 | 低 |
| 24 | unslothai/unsloth | 76514 | +59 | 信息不足 | Python | LLM 训练/推理 | 本地训练/运行 LLM | 私有模型微调 | 低 |
| 25 | freqtrade/freqtrade | 54616 | +59 | 信息不足 | Python | 加密交易 bot | 开源加密交易机器人 | 交易 bot 工程参考 | 中 |
| 26 | logicrw/awesome-jev-projects | 244 | +115 | 信息不足 | JavaScript | Jev 生态清单 | Jev 项目雷达 | 新生态观察 | 低 |
| 27 | OpenBB-finance/OpenBB | 73321 | +49 | 信息不足 | Python | 开放数据平台 | 分析师/量化/AI Agent 数据平台 | 数据平台架构 | 中 |
| 28 | HKUDS/Vibe-Trading | 33746 | +45 | 信息不足 | Python | AI 交易 | 个人交易 Agent | 交易 Agent 产品化 | 中 |
| 29 | antirez/ds4 | 22574 | +41 | 信息不足 | C | 本地推理引擎 | DeepSeek 4 本地推理引擎 | 本地推理性能 | 低 |
| 30 | CopilotKit/OpenBot | 5235 | +49 | 信息不足 | TypeScript | AI Agent 治理 | 开源 AI 同事/浏览器自动化 | Agent 治理与审计 | 中 |
| 31 | code-yeongyu/oh-my-openagent | 69236 | +31 | 信息不足 | TypeScript | Agent 编排 | 图工程 Agent 编排 | Agent 工作流 | 低 |
| 32 | garrytan/gbrain | 30182 | +28 | 信息不足 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent Brain | Agent 架构参考 | 低 |
| 33 | anbeime/skill | 7024 | +49 | 信息不足 | Python | Skills 商店 | AI Agent 技能商店 | 技能包分发 | 低 |
| 34 | nidhinjs/prompt-master | 13439 | +48 | 信息不足 | 无 | Prompt 工程 | 精准 Prompt 生成技能 | Prompt 成本优化 | 低 |
| 35 | valentynkit/awesome-jev-typesafe | 112 | +81 | 信息不足 | JavaScript | Jev 生态清单 | TypeSafe Jev 决策模型清单 | 新生态观察 | 低 |
| 36 | awesomedata/awesome-public-datasets | 79067 | +21 | 信息不足 | 无 | 数据集清单 | 高质量公开数据集清单 | 数据源发现 | 中 |
| 37 | myhhub/stock | 14488 | +78 | 信息不足 | Python | 股票量化 | 股票数据/指标/选股/回测 | A 股量化参考 | 低 |
| 38 | OthmanAdi/planning-with-files | 27031 | +28 | 信息不足 | Shell | Agent 规划 | 基于文件的持久化 Agent 规划 | 长任务 Agent 可靠性 | 低 |
| 39 | ifixai-ai/iFixAi | 15643 | +28 | 信息不足 | Python | AI 审计/风控 | AI Agent 独立审计 | Agent 合规审计 | 低 |
| 40 | fffaraz/awesome-cpp | 73382 | +19 | 信息不足 | 无 | C++ 资源清单 | C++ 框架/库精选 | 低延迟系统选型 | 低 |
| 41 | TNT-Likely/PanWatch | 1089 | +60 | 信息不足 | Python | AI 盯盘 | 自托管 AI 盯盘助手 | 盯盘产品参考 | 中 |
| 42 | kvmem/kvmem-llama.cpp | 389 | +76 | 信息不足 | C++ | 本地推理 | llama.cpp KV 内存优化 | 推理性能优化 | 低 |
| 43 | josephmisiti/awesome-machine-learning | 74381 | +4 | 信息不足 | Python | ML 资源清单 | ML 框架/库精选 | ML 选型参考 | 低 |
| 44 | Developer-Y/cs-video-courses | 83540 | -3 | 信息不足 | 无 | 课程清单 | CS 视频课程清单 | 学习资源 | 中 |
| 45 | vuejs/awesome-vue | 73546 | -1 | 信息不足 | 无 | Vue 资源清单 | Vue 生态精选 | 前端选型 | 低 |
| 46 | ByteByteGoHq/system-design-101 | 89546 | +111 | 信息不足 | 无 | 系统设计 | 系统设计图解 | 交易系统架构参考 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将 LLM 多 Agent 协作引入金融交易决策，模拟分析师、研究员、交易员等多角色团队完成投研与交易信号生成。
- **为什么值得关注**：24h 涨星 +185，总 star 超 10 万，是当前 AI 交易 Agent 方向的代表性项目；Apache-2.0 许可，适合学习与二次开发。
- **技术栈/架构亮点**：Python + 多 Agent 编排；将交易决策拆分为多个专业角色，形成可解释的决策流水线。
- **是否适合借鉴**：适合。其多角色投研 Agent 架构可直接迁移到企业级投研助手、研报自动生成、交易信号解释等场景。
- **可能风险**：项目定位为研究工具，策略表现未经实盘验证；LLM 决策存在幻觉与过拟合风险；不可直接用于真实资金交易。

### 3.2 OpenByteInc/QuantDinger
- **解决什么问题**：提供“AI Trading OS”，覆盖研究、Python 策略构建、回测、模拟/实盘交易，并支持多租户交易 SaaS 部署。
- **为什么值得关注**：24h 涨星 +100，定位完整交易平台，且明确包含用户管理、计费、支付、结算等 SaaS 能力，产品化程度高。
- **技术栈/架构亮点**：Python + Apache-2.0；集成 Alpaca、Binance 等交易所；支持 MCP server；多资产覆盖（加密、股票、外汇）。
- **是否适合借鉴**：适合。其“交易 SaaS 多租户架构”和“研究-回测-交易一体化”设计值得企业级交易平台参考。
- **可能风险**：涉及真实交易所接入，API key 安全风险高；crypto 交易存在合规与资金风险；项目较新，稳定性未验证。

### 3.3 Open-Dev-Society/OpenStock
- **解决什么问题**：开源替代昂贵市场平台，提供实时价格、个性化告警、公司洞察。
- **为什么值得关注**：24h 涨星 +772，为本次候选集中单日涨星最高项目；TypeScript + Next.js 技术栈，产品形态清晰。
- **技术栈/架构亮点**：Next.js + shadcn-ui + TailwindCSS + Inngest；AGPL-3.0 许可；实时行情与告警的产品化实现。
- **是否适合借鉴**：适合。可作为“轻量级行情终端 + 告警系统”的 MVP 参考，尤其适合快速搭建内部投研看板。
- **可能风险**：AGPL 许可对商业闭源使用有限制；行情数据源合规性需自行核实。

### 3.4 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，通过多个 Agent 角色完成投资决策。
- **为什么值得关注**：总 star 超 6 万，是 AI 交易 Agent 领域的经典参考项目；24h 涨星 +73，持续活跃。
- **技术栈/架构亮点**：Python + MIT 许可；多角色 Agent 模拟（如价值投资、成长投资、量化分析等角色）。
- **是否适合借鉴**：适合。其“多策略角色并行决策 + 汇总”模式可用于投研信号融合、策略组合管理。
- **可能风险**：研究/教育属性强，不可直接用于实盘；回测结果可能存在幸存者偏差。

### 3.5 HKUDS/Vibe-Trading
- **解决什么问题**：提供“个人交易 Agent”，将 LLM 能力与交易决策结合。
- **为什么值得关注**：来自 HKUDS，总 star 超 3 万；24h 涨星 +45；覆盖回测、MCP、多 Agent 等热点能力。
- **技术栈/架构亮点**：Python + MIT；集成 MCP、多 Agent、回测；定位“vibe trading”个人交易代理。
- **是否适合借鉴**：部分适合。其 MCP 集成与 Agent 交易流程可参考，但“vibe trading”定位偏营销化，需剥离叙事看工程实现。
- **可能风险**：crypto 相关，存在资金与合规风险；策略有效性未验证；不可直接用于实盘。

### 3.6 freqtrade/freqtrade
- **解决什么问题**：开源加密交易机器人，支持策略开发、回测、模拟与实盘交易。
- **为什么值得关注**：总 star 超 5 万，是加密交易 bot 领域最成熟的开源项目之一；24h 涨星 +59，维护活跃。
- **技术栈/架构亮点**：Python + GPL-3.0；支持 Telegram 控制、多交易所、回测与参数优化。
- **是否适合借鉴**：适合作为交易 bot 工程参考，尤其是策略生命周期管理、交易所适配层设计。
- **可能风险**：GPL 许可限制商业闭源；crypto 交易资金风险高；不可输入真实 API key 运行未知策略。

### 3.7 OpenBB-finance/OpenBB
- **解决什么问题**：面向分析师、量化与 AI Agent 的开放数据平台，统一多源金融数据访问。
- **为什么值得关注**：总 star 超 7 万，是金融数据基础设施的重要开源项目；24h 涨星 +49。
- **技术栈/架构亮点**：Python；覆盖股票、期权、加密、固定收益、宏观等数据；支持 AI Agent 数据消费。
- **是否适合借鉴**：非常适合。其“统一数据访问层”设计可借鉴到企业级数据工程与 Agent 数据接入。
- **可能风险**：许可为 Other，商业使用需仔细阅读条款；数据源合规与稳定性需自行评估。

### 3.8 ifixai-ai/iFixAi
- **解决什么问题**：对 AI Agent 进行独立审计，回答“Agent 是否在做它该做的事”。
- **为什么值得关注**：24h 涨星 +28，总 star 超 1.5 万；定位 AI Agent 治理与风控，与金融合规需求高度相关。
- **技术栈/架构亮点**：Python + Apache-2.0；覆盖幻觉检测、prompt injection、ISO-42001、NIST AI RMF、OWASP LLM 等合规框架。
- **是否适合借鉴**：非常适合。金融场景中 AI Agent 的审计、对齐、风控是刚需，该项目可作为 Agent 治理模块参考。
- **可能风险**：审计能力依赖具体 Agent 实现，泛化能力有限；需结合金融业务合规要求二次开发。

### 3.9 headroomlabs-ai/headroom
- **解决什么问题**：在工具输出、日志、文件、RAG 分块进入 LLM 前进行压缩，降低 token 消耗。
- **为什么值得关注**：24h 涨星 +158，总 star 超 7 万；对高频调用 LLM 的金融 Agent 系统有直接成本价值。
- **技术栈/架构亮点**：Python + Apache-2.0；提供库、代理、MCP server 三种形态；对 JSON 可减少 60-95% token。
- **是否适合借鉴**：非常适合。金融数据（行情、订单簿、日志）通常体积大、重复性高，压缩后可显著降低 Agent 推理成本。
- **可能风险**：压缩可能损失关键信息，需在金融场景中验证保真度。

### 3.10 JustVugg/colibri
- **解决什么问题**：在已有硬件上运行前沿 MoE 模型，纯 C 实现、零依赖、专家从磁盘流式加载。
- **为什么值得关注**：24h 涨星 +183，总 star 超 3.6 万；为本地化、私有化部署大模型提供轻量方案。
- **技术栈/架构亮点**：C + Apache-2.0；零依赖、流式专家加载，适合资源受限环境。
- **是否适合借鉴**：适合。量化研究常需在私有数据上运行模型，本地推理引擎可降低数据外泄风险与推理成本。
- **可能风险**：项目较新，模型兼容性与稳定性需验证；性能与生态成熟度不如主流推理框架。

## 4. 趋势归纳

- **技术趋势**：
  - LLM 上下文工程持续升温：headroom（token 压缩）、planning-with-files（持久化规划）、prompt-master（精准 prompt）等项目涨星显著，反映 Agent 成本与可靠性成为核心痛点。
  - 本地/边缘推理加速：colibri、needle、ds4、kvmem-llama.cpp 等项目聚焦在消费级硬件或微型设备上运行模型，私有化推理需求上升。
  - MCP 生态持续扩张：awesome-mcp-servers、AlphaGBM/skills、anbeime/skill 等项目显示 MCP 与 Skills 正在成为 Agent 工具接入的事实标准。

- **产品趋势**：
  - “AI 设计引擎”与金融产品结合：open-design、ui-ux-pro-max-skill、awesome-design-md 等项目涨星极快，金融看板、交易终端、风控仪表盘的 UI 生成成本有望大幅下降。
  - 交易 SaaS 产品化：QuantDinger 明确提供多租户、计费、结算能力，显示开源交易平台正在从“工具”走向“可运营产品”。
  - 开源行情终端复兴：OpenStock 单日涨星 +772，说明“免费、开源、实时行情 + 告警”仍有强需求。

- **量化/交易策略趋势**：
  - LLM 多 Agent 投研成为主流范式：TradingAgents、ai-hedge-fund、Vibe-Trading、daily_stock_analysis 等项目均采用多角色 Agent 协作。
  - “AI 交易决策 + 传统回测”融合：多个项目同时具备 LLM 决策与回测能力，显示行业正在尝试用回测约束 LLM 策略。
  - Jev/System One 类型化决策模型作为新叙事出现，但生态极新，需观察。

- **AI Agent 与自动化交易结合趋势**：
  - Agent 治理与审计需求上升：iFixAi、OpenBot 等项目显示，随着 Agent 进入交易与业务流程，“可审计、可治理”成为新焦点。
  - 交易 Agent 从“单 Agent”走向“多 Agent + MCP + Skills”组合，工具链标准化程度提高。

- **值得后续做原型验证的方向**：
  - 基于 MCP 的金融数据接入层 + LLM 投研 Agent。
  - 带审计日志与风控闸门的 AI 交易决策沙箱。
  - 本地推理引擎支撑的私有量化研究环境。
  - 用 AI 设计引擎快速生成交易监控看板。

## 5. 今日灵感清单

1. **MVP：AI 投研决策看板**：参考 OpenStock + daily_stock_analysis，用 Next.js 搭建实时行情 + LLM 多角色分析 + 告警推送的轻量看板，先做模拟盘。
2. **MVP：金融数据 MCP Server**：参考 AlphaGBM/skills 与 OpenBB，封装一个面向 Claude Code/Codex 的金融数据 MCP server，提供行情、财务、新闻三类工具。
3. **调研：Agent 上下文压缩在金融数据上的保真度**：用 headroom 对订单簿、K 线、日志等金融数据进行压缩测试，评估 token 节省与信息损失。
4. **调研：Jev/System One 类型化决策模型**：观察 jev-trader、awesome-jev-* 项目的技术实质，判断是否为可复用的决策建模范式，还是纯叙事。
5. **Codex 自动复现 demo：多角色投研 Agent**：基于 TradingAgents 或 ai-hedge-fund 的架构，让 Codex 复现一个最小化多角色投研流水线，输出结构化决策报告。
6. **MVP：AI Agent 审计模块**：参考 iFixAi，为内部交易/投研 Agent 增加决策日志、幻觉检测、prompt injection 防护与合规检查。
7. **调研：本地推理引擎在量化研究中的可行性**：测试 colibri/ds4 在本地运行小模型进行金融文本分析、信号解释的性能与成本。
8. **MVP：AI 生成的交易监控 UI**：用 open-design 或 ui-ux-pro-max-skill 快速生成一个交易风控仪表盘原型，验证设计 Agent 在金融场景的可用性。
9. **调研：多租户交易 SaaS 架构**：拆解 QuantDinger 的用户管理、计费、结算设计，评估是否可复用到企业内部策略平台。
10. **Watchlist：OpenStock、QuantDinger、TradingAgents、iFixAi、headroom**，持续观察其架构演进与社区活跃度。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| Open-Dev-Society/OpenStock | 单日涨星最高，产品形态清晰，适合观察开源行情终端演进 |
| OpenByteInc/QuantDinger | 交易 SaaS 多租户架构独特，产品化程度高 |
| TauricResearch/TradingAgents | AI 多 Agent 交易框架代表，架构可借鉴 |
| ifixai-ai/iFixAi | AI Agent 审计/风控方向，与金融合规需求高度契合 |
| headroomlabs-ai/headroom | LLM 上下文压缩，对金融 Agent 成本优化有直接价值 |
| jarrodwatts/jev-trader | 新叙事代表，需观察其技术实质与可持续性 |
| AlphaGBM/skills | 金融数据 Skills 生态，适合跟踪 MCP 工具链演进 |
| JustVugg/colibri | 本地推理引擎，适合观察私有化模型部署趋势 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-09-19.json`，24h 涨星数据可用。
- **7 日基线**：缺失，`baseline_7d` 为 `null`，因此所有项目的 7d 涨星均标记为“信息不足”。
- **30 日涨星**：所有项目 `star_delta_30d` 均为 `null`，无法提供月度趋势。
- **采集失败**：本次数据中未发现明确的采集失败标记，但部分项目（如 kvmem-llama.cpp）缺少 description，信息完整度有限。
- **样本偏差**：候选集由多个关键词查询合并而成，包含大量 awesome-list 类项目（如 public-apis、awesome-python、awesome-go 等），这些项目并非直接金融/量化项目，而是因关键词命中进入候选，可能稀释了真正交易/量化项目的信号。此外，多个项目因“fintech”“quant”等宽泛关键词被匹配，分类准确性有限。
