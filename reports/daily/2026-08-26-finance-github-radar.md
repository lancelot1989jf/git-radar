# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-08-26

## 1. 今日摘要

- **今日最值得关注的 3 个方向**：
  1. **AI Agent 交易与研究框架**：TradingAgents、Vibe-Trading、OpenAlice、ai-hedge-fund 等项目持续高热度，多智能体 LLM 金融交易框架成为最活跃的工程方向。
  2. **A 股数据与量化工作台**：daily_stock_analysis、a-stock-data、tick-stock-panel、HiThink-Tech/Financial-API 等中文项目集中爆发，围绕 A 股数据获取、LLM 选股、回测与监控形成完整工具链。
  3. **AI 设计/Agent 技能生态**：open-design、ui-ux-pro-max-skill、awesome-design-md 等“设计智能”项目涨星极快，反映 coding agent 从代码生成向 UI/原型/落地页生成延伸的趋势。

- **是否出现新趋势**：出现。AI Agent 技能包（skills）与设计系统（DESIGN.md）正在成为新的分发形态，多个项目以“skill 商店”“插件精选列表”形式快速涨星；同时 A 股本地化量化数据工具链明显升温。

- **是否出现值得复刻/参考的工程架构**：是。TradingAgents 的多智能体对抗式研究架构、nautilus_trader 的 Rust 事件驱动交易引擎、tick-stock-panel 的 DuckDB+Polars 本地量化工作台、headroom 的 LLM token 压缩代理，均具备较高工程参考价值。

- **是否有明显骗局、过度营销或高风险项目**：本批候选中未发现明显骗局，但存在大量“awesome-list”类项目因关键词误匹配进入榜单，实际与金融/量化无关；部分 crypto trading 项目带有杠杆/网格相关风险标记，需谨慎对待。

## 2. 今日 Top 项目表

| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | public-apis/public-apis | 471331 | +842 | +5209 | Python | API 资源列表 | 免费 API 合集 | 低 | 中 |
| 2 | nexu-io/open-design | 91923 | +431 | +2573 | 未知 | AI 设计 | 开源 Claude Design 替代品 | 高 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 121599 | +654 | +3325 | Python | AI 技能 | UI/UX 设计智能技能 | 高 | 低 |
| 4 | ripienaar/free-for-dev | 135463 | +193 | +3231 | HTML | 资源列表 | SaaS/PaaS 免费层合集 | 低 | 低 |
| 5 | awesome-dsh-plugin/awesome-dsh-plugin | 13106 | +435 | +3015 | Python | 插件列表 | DeepSeek Harness 插件精选 | 中 | 低 |
| 6 | codecrafters-io/build-your-own-x | 543308 | +343 | +1977 | Markdown | 教程 | 从零复刻技术项目 | 中 | 中 |
| 7 | TauricResearch/TradingAgents | 100822 | +522 | +1853 | Python | AI 交易 | 多智能体 LLM 金融交易框架 | 高 | 低 |
| 8 | awesome-selfhosted/awesome-selfhosted | 315495 | +405 | +1706 | 未知 | 自托管列表 | 自托管服务合集 | 低 | 中 |
| 9 | VoltAgent/awesome-design-md | 110779 | +359 | +1464 | 未知 | 设计系统 | DESIGN.md 设计系统合集 | 高 | 中 |
| 10 | vinta/awesome-python | 316360 | +286 | +1378 | Python | 资源列表 | Python 工具精选 | 低 | 低 |
| 11 | cactus-compute/needle | 9373 | +193 | +1536 | Python | 端侧模型 | 14MB 端侧基础模型 | 中 | 中 |
| 12 | ruvnet/ruflo | 69513 | +104 | +1141 | TypeScript | Agent 框架 | 多智能体元编排框架 | 高 | 低 |
| 13 | nautechsystems/nautilus_trader | 27916 | +112 | +1455 | Rust | 交易引擎 | Rust 事件驱动交易引擎 | 高 | 中 |
| 14 | unslothai/unsloth | 74934 | +193 | +1054 | Python | LLM 微调 | 本地 LLM 训练/推理 UI | 中 | 低 |
| 15 | headroomlabs-ai/headroom | 67757 | +164 | +848 | Python | Token 压缩 | LLM 输出压缩代理 | 高 | 低 |
| 16 | avelino/awesome-go | 182398 | +145 | +799 | Go | 资源列表 | Go 框架精选 | 低 | 中 |
| 17 | ZhuLinsen/daily_stock_analysis | 64086 | +234 | +694 | Python | A 股分析 | LLM 多市场股票分析系统 | 高 | 低 |
| 18 | JustVugg/colibri | 26270 | +93 | +752 | C | 模型推理 | 纯 C 零依赖 MoE 推理引擎 | 中 | 低 |
| 19 | goldmansachs/gs-quant | 12742 | +270 | +685 | Python | 量化金融 | 高盛量化金融工具包 | 高 | 低 |
| 20 | HKUDS/Vibe-Trading | 31842 | +131 | +548 | Python | AI 交易 | 个人交易 Agent | 高 | 中 |
| 21 | RyanCodrai/turbovec | 16452 | +48 | +798 | Rust | 向量索引 | Rust 向量索引库 | 中 | 低 |
| 22 | langfuse/langfuse | 33796 | +98 | +388 | TypeScript | LLM 可观测 | LLM 评估与监控平台 | 高 | 低 |
| 23 | garrytan/gbrain | 29165 | +77 | +400 | TypeScript | Agent 框架 | OpenClaw/Hermes Agent 大脑 | 中 | 低 |
| 24 | hesreallyhim/awesome-claude-code | 53063 | +77 | +404 | Python | 资源列表 | Claude Code 资源精选 | 低 | 低 |
| 25 | perixtar/Tech-OA-Interview-Questions | 4586 | +280 | +438 | Python | 面试题库 | 科技公司 OA 面试题 | 低 | 低 |
| 26 | lukasz-madon/awesome-remote-job | 48114 | +66 | +455 | 未知 | 资源列表 | 远程工作资源 | 低 | 低 |
| 27 | antirez/ds4 | 21833 | +77 | +255 | C | 模型推理 | DeepSeek 4 本地推理引擎 | 中 | 低 |
| 28 | code-yeongyu/oh-my-openagent | 68427 | +59 | +308 | TypeScript | Agent 框架 | 复杂代码库 Agent 编排 | 中 | 低 |
| 29 | OpenBB-finance/OpenBB | 72358 | +75 | +301 | Python | 金融数据 | 开放金融数据平台 | 高 | 中 |
| 30 | nidhinjs/prompt-master | 11830 | +54 | +368 | 未知 | Prompt 工程 | 精准 Prompt 生成技能 | 中 | 低 |
| 31 | punkpeye/awesome-mcp-servers | 92869 | +49 | +291 | 未知 | MCP 资源 | MCP 服务器合集 | 中 | 低 |
| 32 | simonlin1212/a-stock-data | 9264 | +44 | +349 | 未知 | A 股数据 | A 股全栈数据工具包 | 高 | 低 |
| 33 | xbtlin/ai-berkshire | 15925 | +50 | +218 | Python | 价值投资 | 多 Agent 价值投资研究框架 | 高 | 低 |
| 34 | CopilotKit/OpenBot | 3102 | +188 | 信息不足 | TypeScript | AI 自动化 | 开源 AI 数字员工 | 中 | 中 |
| 35 | coding-kitties/investing-algorithm-framework | 1827 | +113 | +118 | Python | 量化框架 | 量化交易开发框架 | 中 | 中 |
| 36 | OpenByteInc/QuantDinger | 11123 | +32 | +272 | Python | AI 量化 | 多资产 AI 量化平台 | 高 | 中 |
| 37 | HiThink-Tech/Financial-API | 1919 | +128 | 信息不足 | TypeScript | A 股数据 | 同花顺官方 A 股数据服务 | 高 | 低 |
| 38 | codeman008/Financial_freedom | 3562 | +24 | +437 | 未知 | 投资指南 | 赚钱投资指南 | 低 | 中 |
| 39 | anbeime/skill | 5847 | +78 | 信息不足 | Python | 技能商店 | 416 个技能包商店 | 中 | 低 |
| 40 | TraderAlice/OpenAlice | 6751 | +40 | +165 | TypeScript | AI 交易 | 全资产 AI 交易 Agent | 高 | 中 |
| 41 | shy3130/tick-stock-panel | 3844 | +71 | 信息不足 | Python | A 股量化 | A 股选股+监控+回测工作台 | 高 | 低 |
| 42 | Orchestra-Research/AI-Research-SKILLs | 12090 | +49 | +252 | TeX | AI 研究技能 | AI 研究工程技能库 | 中 | 低 |
| 43 | ByteByteGoHq/system-design-101 | 87659 | +121 | +324 | 未知 | 系统设计 | 系统设计图解 | 中 | 低 |
| 44 | lsdefine/GenericAgent | 14047 | +11 | +244 | Python | Agent 框架 | 自进化 Agent 技能树 | 中 | 低 |
| 45 | ifixai-ai/iFixAi | 11191 | +13 | +216 | Python | AI 审计 | AI Agent 独立审计 | 高 | 低 |
| 46 | josephmisiti/awesome-machine-learning | 74176 | +21 | +99 | Python | 资源列表 | ML 框架精选 | 低 | 低 |
| 47 | fffaraz/awesome-cpp | 72956 | +19 | +117 | 未知 | 资源列表 | C++ 资源精选 | 低 | 低 |
| 48 | virattt/ai-hedge-fund | 63065 | +20 | +100 | Python | AI 对冲基金 | AI 对冲基金团队模拟 | 高 | 低 |
| 49 | Developer-Y/cs-video-courses | 83187 | +12 | +58 | 未知 | 课程列表 | CS 视频课程合集 | 低 | 中 |
| 50 | rust-unofficial/awesome-rust | 58988 | +13 | +89 | Rust | 资源列表 | Rust 资源精选 | 低 | 低 |
| 51 | awesomedata/awesome-public-datasets | 78668 | 信息不足 | 信息不足 | 未知 | 数据集 | 公开数据集合集 | 低 | 中 |
| 52 | vuejs/awesome-vue | 73542 | +8 | +3 | 未知 | 资源列表 | Vue 资源精选 | 低 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents
- **解决什么问题**：将 LLM 多智能体协作引入金融交易决策，模拟研究团队的分工与对抗式讨论，输出交易信号。
- **为什么值得关注**：24h 涨星 +522，7d +1853，总 star 超 10 万，是当前 AI 交易领域最活跃的开源项目之一。
- **技术栈/架构亮点**：Python + Apache-2.0，多 Agent 架构，topic 包含 agent、finance、llm、multiagent、trading。强调研究工具属性。
- **是否适合借鉴**：适合。其多智能体分工、对抗式分析、决策留痕的思路可直接迁移到企业级投研 Agent 框架。
- **可能风险**：策略过拟合、回测偏差；LLM 输出不稳定；不可直接用于实盘。

### 3.2 nautechsystems/nautilus_trader
- **解决什么问题**：提供生产级 Rust 原生交易引擎，覆盖回测与实盘，支持多资产类别。
- **为什么值得关注**：7d 涨星 +1455，是少数以 Rust 为核心的高性能交易基础设施项目，工程成熟度较高。
- **技术栈/架构亮点**：Rust + Python 绑定，确定性事件驱动架构，topic 覆盖 crypto、forex、futures、options、sports-betting。
- **是否适合借鉴**：非常适合。事件驱动、确定性回测、多资产抽象是构建企业级交易系统的核心参考。
- **可能风险**：LGPL-3.0 许可证对闭源商用有约束；杠杆/网格相关标记提示需注意策略风险；复杂度高，学习曲线陡峭。

### 3.3 ZhuLinsen/daily_stock_analysis
- **解决什么问题**：LLM 驱动的多市场股票智能分析，整合多源行情、实时新闻、决策看板与自动推送。
- **为什么值得关注**：24h 涨星 +234，总 star 超 6.4 万，是 A 股 AI 分析方向的现象级项目。
- **技术栈/架构亮点**：Python + MIT，topic 包含 a-stock、ai-agent、llm、quant、quantitative-finance。强调零成本定时运行。
- **是否适合借鉴**：适合。其“多源数据 + LLM 分析 + 定时推送”的轻量架构适合快速搭建投研信息流 MVP。
- **可能风险**：数据源稳定性与合规性；LLM 分析结论不可作为投资依据；需注意新闻数据版权。

### 3.4 goldmansachs/gs-quant
- **解决什么问题**：高盛开源的量化金融 Python 工具包，覆盖衍生品定价、风险管理和交易策略。
- **为什么值得关注**：24h 涨星 +270，机构级背景使其在风险管理和衍生品建模方面具有独特参考价值。
- **技术栈/架构亮点**：Python + Apache-2.0，topic 包含 derivatives、risk-management、trading-strategies。
- **是否适合借鉴**：适合。风险模型、衍生品定价、策略接口设计值得企业级风控系统参考。
- **可能风险**：部分功能可能依赖高盛生态；衍生品模型复杂，误用风险高。

### 3.5 HKUDS/Vibe-Trading
- **解决什么问题**：定位为“个人交易 Agent”，将 LLM 与交易决策结合，支持回测与多智能体协作。
- **为什么值得关注**：港大背景，7d 涨星 +548，topic 覆盖 ai-agent、algorithmic-trading、backtesting、mcp、multi-agent。
- **技术栈/架构亮点**：Python + MIT，集成 MCP，强调多 Agent 与回测能力。
- **是否适合借鉴**：适合。其 MCP 集成思路可用于构建可插拔的 AI 交易工具链。
- **可能风险**：crypto_related 标记；策略有效性未经长期验证；不可直接实盘。

### 3.6 OpenBB-finance/OpenBB
- **解决什么问题**：面向分析师、量化研究员和 AI Agent 的开放金融数据平台。
- **为什么值得关注**：总 star 超 7.2 万，是金融数据基础设施的标杆项目，持续活跃。
- **技术栈/架构亮点**：Python，topic 覆盖 equity、crypto、derivatives、fixed-income、options、machine-learning。
- **是否适合借鉴**：非常适合。其数据标准化、多资产覆盖、AI Agent 接口设计值得数据工程团队参考。
- **可能风险**：数据源合规与许可；crypto_related 标记；部分数据可能需要付费订阅。

### 3.7 shy3130/tick-stock-panel
- **解决什么问题**：自托管、零运维的 A 股“选股 + 监控 + 回测”量化工作台，基于 TickFlow 数据源，支持 LLM 策略定制。
- **为什么值得关注**：24h 涨星 +71，新项目快速起量，技术栈现代。
- **技术栈/架构亮点**：Python + MIT，DuckDB + Polars + FastAPI + React，topic 包含 backtesting、screener、self-hosted、ai-agent。
- **是否适合借鉴**：非常适合。DuckDB+Polars 的本地量化数据处理架构轻量高效，适合中小规模量化工作台原型。
- **可能风险**：项目较新，维护活跃度待观察；数据源依赖 TickFlow；回测结果需谨慎解读。

### 3.8 virattt/ai-hedge-fund
- **解决什么问题**：模拟 AI 对冲基金团队，通过多个 AI Agent 协作完成投资研究与决策。
- **为什么值得关注**：总 star 超 6.3 万，是 AI 交易 Agent 方向的开创性项目之一。
- **技术栈/架构亮点**：Python + MIT，多 Agent 角色分工，强调研究工具属性。
- **是否适合借鉴**：适合。其 Agent 角色设计与决策流程可作为企业投研 Agent 的起点。
- **可能风险**：策略过拟合；回测幸存者偏差；不可直接实盘。

### 3.9 headroomlabs-ai/headroom
- **解决什么问题**：在 LLM 处理前压缩工具输出、日志、文件和 RAG 块，降低 token 消耗。
- **为什么值得关注**：7d 涨星 +848，总 star 超 6.7 万，解决 Agent 成本与上下文窗口的核心痛点。
- **技术栈/架构亮点**：Python + Apache-2.0，支持库、代理、MCP server 三种形态，topic 包含 context-engineering、token-optimization、rag。
- **是否适合借鉴**：非常适合。在金融数据密集的 Agent 场景中，token 压缩可显著降低成本并提升上下文利用率。
- **可能风险**：压缩可能损失关键信息，金融场景需验证压缩后决策质量。

### 3.10 langfuse/langfuse
- **解决什么问题**：开源 LLM 工程平台，提供评估、可观测性、指标、Prompt 管理和数据集。
- **为什么值得关注**：YC W23 背景，持续活跃，是 LLMOps 领域的重要基础设施。
- **技术栈/架构亮点**：TypeScript，集成 OpenTelemetry、LangChain、OpenAI SDK、LiteLLM。
- **是否适合借鉴**：非常适合。AI 交易 Agent 的决策留痕、评估与监控可基于此类平台构建。
- **可能风险**：自托管运维成本；与金融合规审计的集成需额外开发。

## 4. 趋势归纳

- **技术趋势**：
  - Rust 在交易基础设施中的渗透加深（nautilus_trader、turbovec）。
  - DuckDB + Polars 成为轻量量化数据栈的新组合（tick-stock-panel、Financial-API）。
  - MCP（Model Context Protocol）成为 AI 交易工具链的标准集成方式（Vibe-Trading、QuantDinger、a-stock-data、headroom）。
  - LLM token 压缩与上下文工程成为 Agent 成本优化的关键方向（headroom）。

- **产品趋势**：
  - “AI 技能包（skills）”和“插件精选列表”成为新的分发形态（ui-ux-pro-max-skill、awesome-dsh-plugin、anbeime/skill）。
  - 设计智能与 coding agent 深度融合，DESIGN.md 成为设计系统新载体（open-design、awesome-design-md）。
  - A 股本地化数据工具链集中爆发，强调零鉴权、零成本、自托管（a-stock-data、daily_stock_analysis、tick-stock-panel）。

- **量化/交易策略趋势**：
  - 多智能体 LLM 交易框架成为主流研究方向（TradingAgents、Vibe-Trading、ai-hedge-fund、OpenAlice）。
  - 机构级工具开源化加速（gs-quant、OpenBB）。
  - 回测与实盘一体化框架持续演进（nautilus_trader、QuantDinger、investing-algorithm-framework）。

- **AI Agent 与自动化交易结合趋势**：
  - 从“单 Agent 决策”向“多 Agent 对抗式研究 + 决策留痕 + 审计”演进。
  - AI Agent 审计与治理开始出现独立工具（iFixAi）。
  - 浏览器自动化与 Agent 治理结合（OpenBot、GenericAgent）。

- **值得后续做原型验证的方向**：
  - 基于 DuckDB + Polars 的本地 A 股量化研究工作台。
  - 多智能体对抗式投研框架 + Langfuse 决策留痕。
  - LLM token 压缩在金融数据密集场景的效果验证。
  - MCP 标准化的金融数据服务层。

## 5. 今日灵感清单

1. **MVP：本地 A 股量化研究工作台**：参考 tick-stock-panel 的 DuckDB + Polars + FastAPI 架构，搭建一个自托管的选股、回测、监控一体化原型，集成 LLM 生成策略说明。
2. **MVP：多智能体投研决策留痕系统**：参考 TradingAgents + Langfuse，构建一个带完整决策日志、可回溯、可评估的投研 Agent 框架。
3. **调研：MCP 金融数据服务标准化**：研究 a-stock-data、QuantDinger、OpenBB 的 MCP 集成方式，设计统一的金融数据 MCP 接口规范。
4. **调研：LLM token 压缩在金融场景的适用性**：基于 headroom 的思路，验证压缩行情数据、财报文本、新闻流后对 Agent 决策质量的影响。
5. **Codex/Agent 自动复现 demo**：让 Codex 复现 nautilus_trader 的事件驱动回测最小示例，理解确定性回测的核心设计。
6. **MVP：AI Agent 审计面板**：参考 iFixAi，为内部 AI 交易/投研 Agent 构建一个轻量审计与合规检查面板。
7. **调研：DESIGN.md 设计系统在金融 Dashboard 中的应用**：参考 awesome-design-md，为量化看板建立可复用的设计 token 与组件规范。
8. **加入 watchlist：gs-quant**：持续跟踪高盛量化工具包的衍生品定价与风险管理模块演进。
9. **加入 watchlist：OpenBB**：关注其 AI Agent 接口与多资产数据标准化进展。
10. **原型验证：端侧模型在金融舆情分析中的应用**：参考 needle、colibri 的端侧推理方案，评估在低资源环境下运行金融文本分类模型的可行性。

## 6. Watchlist 建议

| 项目 | 加入原因 |
|---|---|
| TauricResearch/TradingAgents | AI 多智能体交易框架标杆，持续高增长，架构值得长期跟踪 |
| nautechsystems/nautilus_trader | Rust 交易引擎工程参考价值高，适合研究事件驱动与确定性回测 |
| goldmansachs/gs-quant | 机构级量化工具，风险管理与衍生品模块值得关注 |
| OpenBB-finance/OpenBB | 金融数据基础设施标杆，AI Agent 接口演进值得跟踪 |
| HKUDS/Vibe-Trading | 港大背景，MCP 集成与多 Agent 交易思路有研究价值 |
| shy3130/tick-stock-panel | 新项目，DuckDB+Polars 架构轻量高效，适合观察 A 股量化工具链演进 |
| virattt/ai-hedge-fund | AI 对冲基金模拟的开创性项目，Agent 角色设计值得参考 |
| headroomlabs-ai/headroom | Token 压缩是 Agent 成本优化的关键方向，值得持续关注 |
| langfuse/langfuse | LLMOps 基础设施，适合作为 AI 交易 Agent 的可观测与评估底座 |
| ifixai-ai/iFixAi | AI Agent 审计与治理新兴方向，与金融合规需求高度相关 |

## 7. 风险提醒

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明

- **1 日基线**：存在，`baseline_1d` 为 `2026-08-25.json`，与当前快照 `2026-08-26.json` 相差 1 天，1 日涨星数据基本可靠。
- **7 日基线**：存在，`baseline_7d` 为 `2026-08-19.json`，与当前快照相差 7 天，7 日涨星数据基本可靠。
- **缺失数据**：部分项目（如 CopilotKit/OpenBot、HiThink-Tech/Financial-API、anbeime/skill、tick-stock-panel、awesomedata/awesome-public-datasets）的 `star_delta_7d` 或 `star_delta_1d` 为 null，原因是这些项目在对应基线快照中不存在或未被采集，已在表格中标注“信息不足”。
- **样本偏差**：候选列表包含大量“awesome-list”类项目（如 public-apis、free-for-dev、awesome-python、awesome-go 等），它们因关键词误匹配进入榜单，实际与金融/量化/交易无直接关系。这导致 Top 榜中资源列表类项目占比偏高，真实金融/量化项目的信号被稀释。
- **分类噪声**：`category_guess` 和 `risk_flags` 为自动推断结果，存在误分类可能。例如 needle、colibri、ds4 等模型推理项目被归入 quant_research，实际与量化金融无直接关联。
- **30 日涨星缺失**：所有项目的 `star_delta_30d` 均为 null，无法提供 30 日趋势判断。
