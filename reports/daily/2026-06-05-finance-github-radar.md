# GitHub 金融/量化/自动化交易开源项目雷达 - 2026-06-05

## 1. 今日摘要
- **今日最值得关注的 3 个方向**：
    1.  **AI Agent 驱动的交易框架**：以 `TradingAgents` 和 `Vibe-Trading` 为代表，多智能体协作与 LLM 决策在量化交易中的应用持续升温，成为研究热点。
    2.  **AI 原生设计工具与 Agent 技能生态**：`open-design` 和 `ui-ux-pro-max-skill` 等项目展示了 AI Agent（如 Claude Code、Codex）如何通过“技能（Skills）”和“设计系统（Design Systems）”自动化生成专业级 UI/UX，这一模式正向金融终端和数据看板领域渗透。
    3.  **金融数据平台与终端现代化**：`FinceptTerminal` 和 `OpenBB` 等项目致力于构建开源、可扩展的金融数据分析平台，强调为 AI Agent 提供数据接口，反映了金融数据基础设施的“Agent-First”重构趋势。
- **新趋势**：出现了“Vibe-Trading”（氛围交易）概念，即通过自然语言与多智能体交互完成从研究到执行的全流程交易，降低了量化交易的使用门槛。同时，`DESIGN.md` 驱动的“Vibe-Design”模式正在兴起，允许开发者通过 Markdown 文件定义设计规范，再由 AI Agent 生成匹配的界面代码。
- **值得复刻/参考的工程架构**：
    - `TauricResearch/TradingAgents` 的多智能体金融交易框架架构。
    - `nexu-io/open-design` 的本地优先（Local-first）、沙箱化预览与多格式导出的 AI 设计工具架构。
    - `simonlin1212/a-stock-data` 的 A 股全栈数据工具包的分层架构设计。
- **明显骗局、过度营销或高风险项目**：多个 Polymarket 相关的交易机器人（如 `polymarket-copy-trading-bot`、`Polymarket-trading-bot`）存在严重的描述关键词堆砌、无 License、近期创建且缺乏 7 日基线数据等问题，营销痕迹明显，风险极高。

## 2. 今日 Top 项目表
| 排名 | 项目 | stars | 24h 涨星 | 7d 涨星 | 语言 | 主题/分类 | 一句话说明 | 灵感价值 | 风险等级 |
|:---:|---|:---:|:---:|:---:|---|---|---|---|:---:|
| 1 | nexu-io/open-design | 59.5k | +546 | +3975 | TypeScript | fintech_product | 本地优先的开源 AI 设计工具，支持 259+ 技能与 142+ 设计系统 | AI Agent 驱动的 UI 生成范式，可复刻到金融终端开发 | 低 |
| 2 | TauricResearch/TradingAgents | 83.2k | +210 | +2475 | Python | ai_trading, backtesting | 多智能体 LLM 金融交易框架 | 多 Agent 协作交易系统的架构参考 | 低 |
| 3 | nextlevelbuilder/ui-ux-pro-max-skill | 87.9k | +366 | +3029 | Python | fintech_product | 为构建专业 UI/UX 提供设计智能的 AI 技能 | AI Agent 技能化封装，可借鉴用于生成金融看板 | 低 |
| 4 | codecrafters-io/build-your-own-x | 512.3k | +304 | +4797 | Markdown | trading_bot | 通过从零复刻技术来掌握编程的教程集合 | 提供构建交易系统、数据库等核心组件的教学灵感 | 中 |
| 5 | VoltAgent/awesome-design-md | 87.8k | +280 | +2177 | null | crypto_trading, fintech_product | 流行品牌设计系统的 DESIGN.md 文件集合，供 AI Agent 生成 UI | 设计系统工程化，可应用于金融产品设计规范管理 | 中 |
| 6 | public-apis/public-apis | 439.7k | +226 | +1823 | Python | crypto_trading, quant_research | 免费 API 集合列表 | 为量化研究、数据工程提供免费数据源索引 | 中 |
| 7 | HKUDS/Vibe-Trading | 10.9k | +196 | +1888 | Python | ai_trading, backtesting | 个人 AI 交易 Agent，支持多智能体与 MCP 协议 | “氛围交易”新范式，探索自然语言驱动的交易流程 | 中 |
| 8 | ruvnet/ruflo | 58.1k | +173 | +1651 | TypeScript | ai_trading, backtesting | 领先的 Agent 元框架，用于部署多智能体集群 | 多智能体协作与工作流编排的工程参考 | 低 |
| 9 | ZhuLinsen/daily_stock_analysis | 41.0k | +153 | +1559 | Python | ai_trading, quant_research | LLM 驱动的 A/港/美股智能分析系统，零成本定时运行 | 零成本、全自动的 AI 股票分析流水线参考 | 低 |
| 10 | awesome-selfhosted/awesome-selfhosted | 297.4k | +190 | +1389 | null | trading_bot | 可自托管网络服务与 Web 应用列表 | 为构建自主可控的金融数据服务提供软件选型参考 | 中 |
| 11 | garrytan/gbrain | 21.2k | +155 | +1405 | TypeScript | fintech_product | 一个固执己见的 Agent 大脑 | Agent 核心逻辑与决策机制的实现参考 | 低 |
| 12 | vinta/awesome-python | 301.5k | +174 | +1240 | Python | backtesting, quant_research | Python 框架、库、工具与资源的精选列表 | 量化研究与回测框架的 Python 生态索引 | 低 |
| 13 | ggml-org/llama.cpp | 114.9k | +209 | +1144 | C++ | ai_trading, quant_research | C/C++ 实现的 LLM 推理引擎 | 为本地化、低延迟的 AI 交易推理提供技术基础 | 低 |
| 14 | shiyu-coder/Kronos | 28.7k | +191 | +1249 | Python | backtesting, quant_research | 金融市场语言的基础模型 | 金融领域的专用基础模型，探索时序预测新范式 | 低 |
| 15 | code-yeongyu/oh-my-openagent | 61.2k | +104 | +979 | TypeScript | quant_research | 面向复杂代码库的 Agent 框架 | 复杂软件工程中 Agent 编排与工具使用的参考 | 低 |
| 16 | Fincept-Corporation/FinceptTerminal | 25.5k | +128 | +928 | C++ | ai_trading, fintech_product | 现代金融应用，提供高级市场分析与投资研究工具 | 开源金融终端的架构与交互设计参考 | 低 |
| 17 | RyanCodrai/turbovec | 4.6k | +183 | +964 | Python | quant_research | 基于 TurboQuant 的向量索引，Rust 编写 Python 绑定 | 高性能向量搜索在量化因子分析中的应用潜力 | 低 |
| 18 | avelino/awesome-go | 174.7k | +108 | +700 | Go | backtesting, crypto_trading | Go 语言框架、库和软件的精选列表 | 为构建高性能交易系统提供 Go 生态索引 | 中 |
| 22 | simonlin1212/a-stock-data | 3.5k | +56 | +591 | null | trading_infra | A股全栈数据工具包，7层架构，零第三方依赖 | 为 AI Agent 设计的 A 股数据基础设施，架构值得借鉴 | 低 |
| 27 | brokermr810/QuantDinger | 7.3k | +57 | +384 | Python | ai_trading, backtesting | 面向加密/股票/外汇的 AI 量化交易平台 | 集回测、实盘、数据、多 Agent 研究于一体的平台架构 | 中 |
| 28 | OpenBB-finance/OpenBB | 68.7k | +34 | +413 | Python | crypto_trading, quant_research | 面向分析师、量化工程师和 AI Agent 的金融数据平台 | 为 AI Agent 提供标准化金融数据接口的参考实现 | 中 |
| 31 | TraderAlice/OpenAlice | 4.9k | +36 | +342 | TypeScript | ai_trading, backtesting | 覆盖研究、入场、管理、退出的全流程 AI 交易 Agent | 全流程自动化交易 Agent 的闭环架构参考 | 中 |
| 33 | freqtrade/freqtrade | 51.2k | +23 | +264 | Python | backtesting, crypto_trading | 免费开源的加密货币交易机器人 | 成熟的策略回测与实盘交易框架，策略开发参考 | 中 |
| 39 | Open-Dev-Society/OpenStock | 13.0k | +12 | +244 | TypeScript | - | 开源市场数据平台，替代昂贵的商业产品 | 开源金融信息平台的 UI/UX 与数据呈现参考 | 低 |

## 3. 重点项目深度分析

### 3.1 TauricResearch/TradingAgents (Python, 83.2k stars)
- **项目解决什么问题**：构建了一个基于多智能体（Multi-Agent）和大语言模型（LLM）的金融交易框架，旨在模拟不同角色的交易员协同工作，进行市场分析、策略制定和风险管理。
- **为什么最近值得关注**：7 日涨星 +2475，是当前多智能体与量化交易结合方向最火热的项目之一。其“多角色协作”的范式为构建复杂、稳健的 AI 交易系统提供了新思路。
- **技术栈/架构亮点**：采用 Python 编写，核心是多 Agent 协作架构。每个 Agent 可被赋予特定角色（如基本面分析师、技术分析师、风险管理员），通过 LLM 进行交互和决策。这种架构将交易决策过程模块化、角色化，便于调试和扩展。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其多 Agent 角色分工与协作的架构设计，可直接应用于企业级金融 Agent 框架的开发中，用于处理复杂的、需要多维度信息的投资决策任务。
- **可能的风险**：作为研究工具，策略可能存在严重的过拟合风险；多 Agent 交互的延迟可能不适用于高频交易；依赖 LLM 的稳定性与准确性，存在输出幻觉风险。

### 3.2 HKUDS/Vibe-Trading (Python, 10.9k stars)
- **项目解决什么问题**：提出了“Vibe-Trading”（氛围交易）的概念，旨在让用户通过自然语言与个人 AI 交易 Agent 交互，完成从市场感知到交易执行的全过程。
- **为什么最近值得关注**：7 日涨星 +1888，代表了 AI 交易领域“降低使用门槛”和“交互范式变革”的新趋势。其集成了 MCP 协议，展示了 AI Agent 与外部工具连接的标准方式。
- **技术栈/架构亮点**：Python 实现，集成了 MCP（Model Context Protocol）协议，支持多智能体。这表明其架构注重模块化和标准化，允许 Agent 安全、高效地调用外部数据源和交易接口。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：极具借鉴价值。“Vibe-Trading”的理念和 MCP 集成方式，为设计下一代以用户意图为中心的智能交易助手提供了直接参考。
- **可能的风险**：概念较新，可能过度简化了交易的复杂性；自然语言指令的模糊性可能导致非预期的交易行为；依赖 MCP 生态的成熟度。

### 3.3 nexu-io/open-design (TypeScript, 59.5k stars)
- **项目解决什么问题**：提供一个本地优先（Local-first）的开源 AI 设计工具，作为 Figma 的替代品。它通过集成 259+ 技能和 142+ 设计系统，让 AI Agent 能生成 Web、桌面、移动端原型、幻灯片、图片和视频。
- **为什么最近值得关注**：24 小时涨星 +546，7 日涨星 +3975，增长极为迅猛。它展示了 AI Agent 如何通过“技能”和“设计系统”的组合，实现高度自动化、专业化的 UI 生成，这种模式对金融科技产品的快速原型开发意义重大。
- **技术栈/架构亮点**：TypeScript 编写，原生桌面应用。核心亮点是“技能（Skills）”和“设计系统（Design Systems）”的插件化架构，以及沙箱化预览和多格式导出（HTML/PDF/PPTX/MP4）能力。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合。其“技能+设计系统”的架构模式，可以迁移到金融领域，用于构建能自动生成交易看板、风控仪表盘、数据分析报告的 AI Agent。
- **可能的风险**：项目较新（2026年4月创建），长期维护能力待观察；过度依赖特定的 AI 模型（如 Claude）的接口稳定性。

### 3.4 simonlin1212/a-stock-data (null, 3.5k stars)
- **项目解决什么问题**：为 AI 编程助手提供一个全栈的 A 股数据工具包，号称具有“7层架构 · 27端点 · 13数据源 · 零第三方依赖”。
- **为什么最近值得关注**：7 日涨星 +591，虽然 star 总量不高，但增长迅速。它精准地解决了 AI Agent 在金融领域应用的一个核心痛点：如何可靠、高效地获取结构化数据。
- **技术栈/架构亮点**：其宣称的“7层架构”和“零第三方依赖”是最大的架构亮点，暗示了从数据采集、清洗、存储到 API 服务的全链路自研设计，这对于金融数据服务的稳定性和合规性至关重要。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：非常适合作为数据基础设施层的参考实现。其分层架构和面向 AI 助手的设计理念，可直接应用于构建企业级量化投研平台的数据中台。
- **可能的风险**：项目信息有限，未显示主要编程语言；“零第三方依赖”的维护成本可能很高；数据源的合规性和稳定性是长期挑战。

### 3.5 Fincept-Corporation/FinceptTerminal (C++, 25.5k stars)
- **项目解决什么问题**：旨在提供一个类似 Bloomberg 终端的现代开源金融应用，集成了高级市场分析、投资研究和经济数据工具。
- **为什么最近值得关注**：7 日涨星 +928，持续受到关注。它代表了用现代技术栈（C++, Qt, Python）重构专业金融终端的趋势，强调交互式探索和数据驱动决策。
- **技术栈/架构亮点**：使用 C++ 和 Qt 构建，保证了高性能和跨平台的原生体验，同时结合 Python 用于机器学习和数据分析。这种混合架构兼顾了性能与灵活性。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其作为金融数据可视化与交互分析的终端产品，在 UI/UX 设计、数据流管理、插件化扩展方面提供了优秀参考。未来可考虑为其增加 AI Agent 接口，实现语音或自然语言交互。
- **可能的风险**：C++ 代码库的维护门槛较高；作为商业公司的开源产品，其开源策略和社区治理模式可能发生变化。

### 3.6 OpenBB-finance/OpenBB (Python, 68.7k stars)
- **项目解决什么问题**：一个面向分析师、量化工程师和 AI Agent 的金融数据平台，提供标准化的数据访问接口。
- **为什么最近值得关注**：作为成熟的金融数据平台，它明确将“AI Agent”列为其服务对象，代表了金融数据基础设施的“Agent-First”重构趋势。
- **技术栈/架构亮点**：Python 生态为核心，提供统一的数据模型和 API，屏蔽了不同数据源的差异。其架构强调可扩展性，允许社区贡献新的数据扩展。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：是构建 AI 交易 Agent 数据层的绝佳参考。其标准化数据接口的设计理念，是解决 Agent 数据获取碎片化问题的关键。
- **可能的风险**：开源版的 License 可能对商业使用有限制；数据源的稳定性和延迟可能无法满足所有实盘交易场景。

### 3.7 shiyu-coder/Kronos (Python, 28.7k stars)
- **项目解决什么问题**：构建一个“金融市场语言的基础模型”（Foundation Model），试图用统一的模型来理解和预测金融时序数据。
- **为什么最近值得关注**：7 日涨星 +1249，代表了量化研究从传统时序模型向大语言模型范式转变的前沿探索。
- **技术栈/架构亮点**：Python 实现，核心是将金融时间序列数据视为一种“语言”，并训练一个基础模型来学习其内在规律。这是一种范式创新。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其研究成果可以作为 AI 交易 Agent 的核心决策引擎或特征提取器，提供更强大的市场预测能力。
- **可能的风险**：作为研究项目，模型可能存在严重的过拟合，实盘效果未知；金融市场的非平稳性对基础模型的泛化能力构成巨大挑战。

### 3.8 TraderAlice/OpenAlice (TypeScript, 4.9k stars)
- **项目解决什么问题**：打造一个“个人华尔街”，提供一个覆盖股票、加密、商品、外汇和宏观经济的全流程 AI 交易 Agent，从研究到入场、持仓管理再到退出。
- **为什么最近值得关注**：7 日涨星 +342，其“全流程闭环”的设计理念是 AI 交易 Agent 从辅助工具走向自主决策的关键一步。
- **技术栈/架构亮点**：TypeScript 编写，采用 AGPL-3.0 协议。其架构亮点在于试图打通“研究-决策-执行-管理”的完整交易生命周期，形成一个闭环系统。
- **是否适合借鉴到 AI/自动化交易/企业级 Agent 框架中**：其全流程闭环的架构设计是构建高级交易 Agent 的重要参考，特别是状态管理和多阶段决策流程的设计。
- **可能的风险**：AGPL-3.0 协议具有强传染性，商业集成需谨慎；全流程自动化风险极高，任何一个环节的失误都可能导致资金损失。

## 4. 趋势归纳
- **技术趋势**：
    - **多智能体协作**：从 `TradingAgents` 到 `Vibe-Trading`，多 Agent 分工协作成为构建复杂金融 AI 系统的主流架构。
    - **MCP 协议集成**：`Vibe-Trading` 等项目开始集成 MCP 协议，标志着 AI Agent 与外部工具（数据源、交易所）的连接方式正在标准化。
    - **AI Agent 技能化**：`ui-ux-pro-max-skill`、`prompt-master` 等项目展示了将 AI 能力封装为可复用“技能（Skills）”的趋势，这降低了构建复杂 Agent 的门槛。
    - **金融基础模型**：`Kronos` 等项目探索将 LLM 范式应用于金融时序数据，试图构建金融领域的专用基础模型。
- **产品趋势**：
    - **“Vibe” 概念兴起**：从“Vibe-Trading”到“Vibe-Design”（`awesome-design-md`），强调通过自然语言或简单指令驱动 AI 完成复杂专业任务，用户体验范式正在变革。
    - **AI 原生设计工具**：`open-design` 的火爆表明，AI 驱动的、本地优先的、高度自动化的设计工具正在挑战传统 SaaS 模式。
    - **金融终端开源化与现代化**：`FinceptTerminal`、`OpenStock` 等项目试图用现代技术栈和开源模式替代昂贵的传统金融终端。
- **量化/交易策略趋势**：
    - **AI Agent 驱动的策略**：策略开发从人工编写规则，转向由 LLM 驱动的多 Agent 自主分析、决策和执行。
    - **全流程自动化**：`OpenAlice` 等项目尝试覆盖从研究到退出的交易全生命周期，追求更高程度的自动化。
- **AI Agent 与自动化交易结合趋势**：
    - **Agent-First 数据基础设施**：`OpenBB`、`a-stock-data` 等项目明确将服务 AI Agent 作为核心目标，提供结构化、标准化的数据接口。
    - **自然语言交互界面**：交易系统的交互方式正在从复杂的 GUI/CLI 向自然语言对话式界面演进。
- **值得后续做原型验证的方向**：
    - 基于 MCP 协议，构建一个可插拔的金融数据与交易执行 Agent 框架。
    - 复刻 `open-design` 的“技能+设计系统”模式，开发一个能自动生成金融风控仪表盘的 Agent。
    - 利用 `a-stock-data` 的数据架构，为 `TradingAgents` 或自研 Agent 构建一个 A 股市场的数据适配器。

## 5. 今日灵感清单
1.  **MVP 灵感：AI 驱动的金融看板生成器**：借鉴 `open-design` 和 `awesome-design-md` 的模式，创建一个 Agent 技能，用户只需提供数据源和需求描述，即可自动生成包含 K 线图、风控指标、新闻舆情等模块的实时金融看板。
2.  **调研方向：MCP 协议在量化交易中的标准化应用**：深入研究 `Vibe-Trading` 对 MCP 协议的实现，调研如何将行情数据、历史回测、订单执行等不同功能标准化为 MCP 服务，构建一个可插拔的量化交易 Agent 生态。
3.  **Demo 复现：多智能体交易决策模拟**：基于 `TradingAgents` 的架构思想，使用 Codex 或 Claude 快速复现一个简化版的多 Agent 股票分析 Demo，模拟“价值投资者”、“趋势交易者”和“风险管理者”三个 Agent 对同一只股票的辩论和决策过程。
4.  **架构研究：A 股数据中台设计**：分析 `a-stock-data` 宣称的“7层架构”，结合数据工程最佳实践，设计一个面向 AI Agent 的企业级金融数据中台蓝图，重点关注数据质量、低延迟和合规性。
5.  **产品灵感：开源金融终端插件市场**：参考 `FinceptTerminal` 和 `OpenBB` 的扩展机制，构思一个开源金融终端的插件市场，允许开发者以标准化的方式贡献数据源、分析工具、AI 策略和可视化组件。
6.  **技术验证：Rust 在量化基础设施中的性能优势**：关注 `turbovec` 项目，验证使用 Rust 编写核心计算模块（如因子计算、向量搜索），并通过 Python 绑定提供给上层策略应用，是否能显著提升回测和实时计算性能。
7.  **安全研究：AI Agent 在金融领域的提示注入防御**：鉴于 `hexstrike-ai` 等安全工具的火热，研究针对金融 AI Agent 的提示注入攻击场景，并设计相应的防御机制，确保交易指令的安全执行。
8.  **Watchlist 新增**：将 `TauricResearch/TradingAgents`、`HKUDS/Vibe-Trading`、`nexu-io/open-design`、`simonlin1212/a-stock-data`、`shiyu-coder/Kronos` 加入重点关注列表，跟踪其架构演进和社区发展。

## 6. Watchlist 建议
- **TauricResearch/TradingAgents**：多智能体交易框架的标杆项目，其架构设计和 Agent 协作模式是未来 AI 交易系统的重要参考。
- **HKUDS/Vibe-Trading**：代表了“氛围交易”这一新兴交互范式，并集成了 MCP 协议，是探索下一代 AI 交易助手的关键项目。
- **nexu-io/open-design**：AI 原生设计工具的爆款，其“技能+设计系统”的架构模式对金融科技产品的 UI 自动化生成有巨大借鉴意义。
- **simonlin1212/a-stock-data**：专注于解决 A 股数据获取痛点，其面向 AI 助手的分层架构设计值得深入研究，是构建本土化量化平台的数据基础。
- **shiyu-coder/Kronos**：金融基础模型的前沿探索，代表了量化研究的一个新方向，其模型能力和局限性值得长期跟踪。
- **TraderAlice/OpenAlice**：追求交易全流程闭环自动化的 Agent，其生命周期管理设计对构建高级交易 Agent 有启发。
- **Fincept-Corporation/FinceptTerminal**：开源金融终端的现代化尝试，其混合语言（C++/Python）架构和交互设计是构建专业金融工作站的参考。
- **OpenBB-finance/OpenBB**：金融数据平台的“Agent-First”演进代表，是构建 AI 交易 Agent 数据层的标准化参考。

## 7. 风险提醒
- **GitHub star 不是投资建议**：Star 数仅代表社区关注度，与项目盈利能力或策略收益率无关。
- **不运行未知 trading bot**：尤其是 `polymarket-copy-trading-bot`、`Polymarket-trading-bot` 等描述堆砌、缺乏许可证、近期创建的项目，存在恶意代码、窃取 API Key 或资金的高风险。
- **不泄露交易所 API key**：任何要求输入真实交易所 API Key 的开源项目都应极度谨慎，建议先在模拟环境或只读权限下测试。
- **注意策略风险**：马丁、网格、套利、杠杆类策略存在巨大爆仓风险。回测结果可能存在幸存者偏差和过拟合，实盘表现可能截然不同。
- **注意合规风险**：使用自动化交易工具需遵守当地法律法规和交易所规则。

> 风险提醒：本报告只用于开源项目观察和工程灵感收集，不构成投资建议。不要直接运行未知 trading bot，不要输入真实交易所 API Key，不要将 GitHub star 或短期涨星视为收益信号。自动交易、杠杆、马丁、网格和套利类项目可能存在重大资金风险、合规风险和安全风险。

## 8. 数据质量说明
- **基线数据**：本次报告使用了 `2026-06-04.json` 作为 1 日基线，`2026-05-29.json` 作为 7 日基线，数据完整。
- **数据缺失**：部分项目（如 `polymarket-copy-trading-bot`、`Polymarket-trading-bot`）因创建时间过短，缺少 7 日涨星数据。所有项目均缺少 30 日涨星数据。
- **样本偏差**：候选项目列表由特定查询条件（如关键词匹配、topic 过滤）生成，可能偏向于特定技术栈或概念（如 AI、量化、加密），无法完全代表 GitHub 上所有金融科技项目的全貌。部分项目（如 `build-your-own-x`、`public-apis`）因描述或 readme 中包含匹配关键词而被收录，其核心主题并非金融科技，分析时需注意区分。
