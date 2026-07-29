# AIsa

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

AIsa 是一家总部位于旧金山、成立于 2025 年的公司（[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)）。它运营一个网关，让 AI agent 和开发者通过单一 API key 和单一账单账户访问 LLM、数据 API、SaaS 工具以及打包好的 "Skills"，按用量计费，可用法币或稳定币结算。公司自己的法律页面上出现了两个不同的法律主体名称：服务条款中为 `AIPay Inc.`，隐私政策中为 `AIPAY GLOBAL PTE. LTD`，两者都标注为 "dba AIsa"。

- 在没有付费营销的情况下已接入超过 50,000 个注册 agent；2026 年 2 月至 6 月间注册 agent 用户增长 150 倍，API 调用与交易量增长 200 倍（[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)）。官网另称 "Join 5,000+ Agents Already Running"（[官网](https://aisa.one/)；无日期，访问于 2026-07-29）——见 `备注`。
- 累计融资 650 万美元，其中包括由阿里巴巴与 Tribe Capital 联合领投的种子轮，公布于 [2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)。更早还有两次金额未披露的 Pre-Seed 公告，分别发布于 [2025-08-31](https://www.chaincatcher.com/article/2202064) 和 [2025-10-28](https://www.chaincatcher.com/article/2215658)，投资方名单重叠但并不一致——见 `备注`。
- 团队规模被表述为 10 人（[Forbes，2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)）；LinkedIn 公司页显示为 2–10 人区间（[LinkedIn](https://www.linkedin.com/company/aipayhq)；无日期，访问于 2026-07-29）。
- 工程方面的证据来自可观察的产品表层而非公开的技术栈说明：站点为 Next.js 并置于 Cloudflare 之后，文档为部署在 Vercel 上的 Mintlify，`api.aisa.one/v1` 提供 OpenAI 兼容推理接口，`/apis/v1` 为 bearer 认证的数据 API，`/apis/v2` 为 x402 按调用付费的镜像，开源 agent Skills 以 Python 和 Node 发布于 [github.com/AISA-skills](https://github.com/AISA-skills)。站点没有招聘页；找到的唯一公开招聘渠道是 [2026-05-21](https://www.v2ex.com/t/1214335) 至 [2026-07-28](https://www.v2ex.com/t/1230516) 期间在 V2EX 上发布的四篇中文招聘帖，它们也是关于岗位、所需技术栈和工作条件的唯一公开来源。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 对外品牌 | AIsa | [官网](https://aisa.one/)；无日期，访问于 2026-07-29 |
| 法律名称（服务条款） | AIPay Inc.（dba. "AIsa"） | [服务条款](https://aisa.one/TOS)；最后更新 2026-03-10 |
| 法律名称（隐私政策） | AIPAY GLOBAL PTE. LTD（dba "AIsa"） | [隐私政策](https://aisa.one/privacy)；最后更新 2026-03-10 |
| 成立时间 | 2025 年 | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 总部 | 旧金山 | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 另一处列出的地点 | 新加坡 | [LinkedIn](https://www.linkedin.com/company/aipayhq)；无日期，访问于 2026-07-29 |
| 负责人 | Jordan Liu，Founder and CEO | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 员工人数 | "a 10-person team" | [Forbes，2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/) |
| 员工人数区间 | 2–10 人 | [LinkedIn](https://www.linkedin.com/company/aipayhq)；无日期，访问于 2026-07-29 |
| 注册 agent 数 | 超过 50,000 个，且未使用付费营销 | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 公布的客户 | Impossible Finance | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 累计融资 | 截至目前累计 650 万美元 | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 公司列出的投资方 | 阿里巴巴、Tribe Capital、Draper Associates、住友商事、Saison Capital 及其他投资方 | [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| GitHub 组织 | `AISA-skills`，创建于 2026-05-22，地点写为 "United States of America"，7 个公开仓库 | [GitHub](https://github.com/AISA-skills)；访问于 2026-07-29 |
| 公开联系方式 | developer@aisa.one（开发者）、press@aisa.one（媒体）、partner@aisa.one（合作）、support@aisa.one（插件清单中） | [官网](https://aisa.one/)、[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)、[ai-plugin.json](https://aisa.one/.well-known/ai-plugin.json) |
| 社区渠道 | Discord | [官网](https://aisa.one/)；无日期，访问于 2026-07-29 |
| 站点语言 | 13 个语言版本：英语、zh-CN、zh-TW、ja-JP、ko、pt-BR、fr、de、it、es、tr、ru、ar | [sitemap.xml](https://aisa.one/sitemap.xml)；访问于 2026-07-29 |

**项目、黑客松与奖项**：AIsa 称自己是 Circle 与 Arc 相关的 "Agentic Economy on Arc" 黑客松（2026-04-20 至 2026-04-26）的官方技术合作方（[博客，2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc)），并称在该活动中获得第二名（[博客，2026-02-26](https://aisa.one/blog/aisa-awarded-second-place-agentic-commerce-arc-hackathon)）。公司赞助了 ETHDenver 2026 的 "Claws Out" 活动（[博客，2026-02-27](https://aisa.one/blog/aisa-sponsors-claws-out-ethdenver-2026)），更早还赞助了 Solana x402 虚拟黑客松，设立了价值 5,000 美元 AI 资源的 "Best AgentPay Demo" 奖项（[ChainCatcher，2025-11-07](https://www.chaincatcher.com/en/article/2218188)）。

**公司自述的市场背景**：[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)将问题描述为，数字资源"为人类用户设计，需要注册账户、管理 API key、订阅计划、合同和人工付款流程，而自主 agent 无法高效地走完这些流程"，并把自身增长归因于它点名的 OpenClaw 和 Hermes 等 agent 框架的兴起。

### 品牌与法律实体

| 名称 | 类型 | 指向的司法管辖区 | 关系 | 来源 |
|---|---|---|---|---|
| AIsa | 对外品牌／商号 | — | 网站、文档、新闻稿和 GitHub 上统一使用的名称 | [官网](https://aisa.one/) |
| AIPay Inc. | 服务条款中的缔约主体 | 未写明；"Inc." 及仲裁／集体诉讼弃权条款指向美国主体 | 页面写明以 "AIsa" 名义经营 | [服务条款](https://aisa.one/TOS) |
| AIPAY GLOBAL PTE. LTD | 隐私政策中的数据控制者 | "PTE. LTD" 是新加坡私人有限公司后缀；页面未写明管辖区 | 页面写明以 "AIsa" 名义经营 | [隐私政策](https://aisa.one/privacy) |
| AIPay, Inc. | 投资方使用的法律名称 | 美国（页面标注旧金山） | Draper Associates 投资组合页写作 "AIsa (AIPay, Inc.)" | [Draper Associates](https://www.draper.vc/portfolio/alsa) |

所查阅的任何页面都未说明 `AIPay Inc.` 与 `AIPAY GLOBAL PTE. LTD` 之间的关系。LinkedIn 公司页的 URL 标识为 `aipayhq`，同时列出旧金山和新加坡（[LinkedIn](https://www.linkedin.com/company/aipayhq)；无日期，访问于 2026-07-29）。截至 2026-07-29，在所查阅的公开来源中未找到任一名称的工商登记记录；所查的新加坡登记信息聚合站点返回的是机器人验证页面而非查询结果。

---

## 产品

AIsa 自述为"面向 AI agent 的统一资源与交易网络"，并在其机器可读的产品索引中称自己是"一个跨资源的能力与交易层，而这些资源仍可以有各自不同的端点、schema、授权要求和计费单位"（[llms.txt](https://aisa.one/llms.txt)；访问于 2026-07-29）。

### 产品面

| 产品面 | 标注状态 | 内容 | 来源 |
|---|---|---|---|
| Model Gateway | 已上线 | OpenAI 兼容的推理接口，覆盖 GPT、Claude、Gemini、Grok、DeepSeek、Qwen、Kimi、MiniMax、GLM、Seed、Seedream、Wan 等模型系列 | [模型目录](https://aisa.one/models)、[文档索引](https://aisa.one/docs/llms.txt) |
| APIs | 已上线 | 按提供方分组的按调用计费的数据与动作端点 | [API 索引](https://aisa.one/api) |
| Skills | 已上线 | 可安装到 agent 运行时的任务导向指令包 | [Skills 索引](https://aisa.one/skills) |
| Machine-to-Machine | Private Beta | 基于 HTTP 402 式流程的 Circle Nanopayments 与 Machine Payments Protocol（MPP） | [官网](https://aisa.one/)；无日期，访问于 2026-07-29 |
| Foundry | Coming Soon | 云托管的预配置 agent 实例，带监控、护栏和 nanopayment 计费 | [官网](https://aisa.one/)；无日期，访问于 2026-07-29 |
| Agent Discovery | 已上线 | 公开发布的 A2A agent card、AI 插件清单、MCP 清单、OpenAPI 规范和 llms.txt 系列文件 | [agent-discovery](https://aisa.one/agent-discovery) |

### 目录规模

官网标题写的是 "1000+ APIs, Skills, and LLMs"（[官网](https://aisa.one/)；无日期，访问于 2026-07-29）。按 2026-07-29 公开的 sitemap 统计，为 102 个模型页、90 个 API 页和 48 个 skill 页（[sitemap.xml](https://aisa.one/sitemap.xml)）；更大的数字似乎是在统计单个端点，因为官网按提供方列出的端点数为 DataForSEO 445、Apollo 54、Agent Mail 51、Twitter 32、Financial 22、CoinGecko 21 等。Agent Discovery 页写明 A2A agent card 中广播了 43 项能力——"42 项可安装 skill 加上核心的 AI Model Inference 能力"（[agent-discovery](https://aisa.one/agent-discovery)；无日期，访问于 2026-07-29）。

官网 API 列表中点名的上游提供方（无日期，访问于 2026-07-29）：Apollo、DataForSEO、Tavily、Perplexity、CoinGecko、Polymarket、Kalshi、Twitter/X、Reddit、Instagram、Pinterest、YouTube、Scholar、Agent Mail、WaveInflu，以及一个 "Financial" 分组。

### 商业化

按用量计费，无固定月度平台费（[定价文档](https://aisa.one/docs/guides/pricing)；访问于 2026-07-29）。适用两种模型：LLM 推理按 token 计费（按每 100 万输入和输出 token 分别定价），非 LLM API 按请求固定收费。账户通过钱包充值。

| 项目 | 内容 | 来源 |
|---|---|---|
| 充值方式 | 经 Stripe 的银行卡支付，或经 AIsa 自有加密支付流程的稳定币支付 | [钱包文档](https://aisa.one/docs/guides/pricing/wallet) |
| 阶梯折扣 | 50 美元 → 5%、100 美元 → 5%、200 美元 → 10%、500 美元 → 15%、1000 美元 → 20% | [钱包文档](https://aisa.one/docs/guides/pricing/wallet) |
| 注册赠额 | 新账户 2 美元（Free 档） | [限流文档](https://aisa.one/docs/api-reference/rate-limits) |
| 限流分档 | Free 60 RPM／60,000 TPM／5 并发；Starter 600／600,000／20；Growth 3,000／3,000,000／50；Enterprise 定制 | [限流文档](https://aisa.one/docs/api-reference/rate-limits) |
| 升档方式 | 首次钱包充值后自动由 Free 升至 Starter；Growth 需累计充值 500 美元以上或申请获批 | [限流文档](https://aisa.one/docs/api-reference/rate-limits) |
| 无账户按调用付费 | `/apis/v2` 为数据 API 的 x402 结算镜像——"无需注册——调用任意端点，收到 HTTP 402 挑战，用稳定币微支付完成结算" | [mcp.json](https://aisa.one/.well-known/mcp.json) |

Arc 黑客松集成给出的单次请求价格区间为"每请求 0.00044 至 0.12 美元，经 Circle Nanopayments 以 USDC 结算"（[博客，2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc)）。除控制台和市场页面外，未找到逐端点的完整公开价目表。

### 公开披露的规模变化

| 日期 | 公布的数字 | 来源 |
|---|---|---|
| 2025-10-28 | AI Marketplace-402 被描述为聚合"600+ LLMs、100 万+ 数据 API 与 GPU"等资源，定位"AI 资源的 NASDAQ" | [ChainCatcher（中文）](https://www.chaincatcher.com/article/2215658) |
| 2026-04-23 | "处理了超过一百万次 API 调用" | [博客](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc) |
| 2026-07-03 | 2026 年 2 月至 6 月，注册 agent 用户增长 150 倍，API 调用与交易量增长 200 倍；在未使用付费营销的情况下接入超过 50,000 个注册 agent | [新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 2026-07-03 | 在未使用付费营销的情况下接入"超过 20,000 个注册 agent" | [Forbes](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/) |
| 无日期，访问于 2026-07-29 | "Join 5,000+ Agents Already Running" | [官网](https://aisa.one/) |

### 公布的客户、合作方与生态位声明

| 日期 | 对象 | 公布内容 |
|---|---|---|
| [2025-08-31](https://www.chaincatcher.com/article/2202064) | Circle、Visa、Stripe、PayPal、Privy、JPMorgan Kinexys | 公司自述为 Circle Global Payment Network 早期成员、Visa Intelligence Commerce 生态早期贡献方、Stripe AgentKit 与 Global Financial Accounts 的核心开发者、与 PayPal 共同推动 PYUSD、与 Privy 共建账户体系，并在与 JPMorgan Kinexys 探索 $JPMD 在 treasury agents 上的应用 |
| [2025-10-28](https://www.chaincatcher.com/article/2215658) | Coinbase x402、Google AP2/A2A | AgentPayWall-402 被描述为与 Coinbase x402 深度集成；原生支持 HTTP 402／x402／L402，并向 Base、Lightning、Solana、BNB、Polygon、X-Layer 等多链扩展，同时参与 Google AP2/A2A 生态建设 |
| [2025-11-07](https://www.chaincatcher.com/en/article/2218188) | Solana x402 虚拟黑客松 | AIsa 赞助设立价值 5,000 美元 AI 资源的 "Best AgentPay Demo" 奖项 |
| [2026-02-26](https://aisa.one/blog/aisa-awarded-second-place-agentic-commerce-arc-hackathon) | Circle 与 Google 支持的 Agentic Commerce on Arc 黑客松 | AIsa 称获得第二名 |
| [2026-02-27](https://aisa.one/blog/aisa-sponsors-claws-out-ethdenver-2026) | ETHDenver 2026 | AIsa 赞助 "Claws Out" 活动 |
| [2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc) | Circle／Arc | AIsa 作为 "Agentic Economy on Arc" 黑客松（2026-04-20 至 2026-04-26）的数据层技术合作方，通过 x402 与 Circle Nanopayments 开放 100 多个端点 |
| [2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) | Impossible Finance | 被点名为通过单一接口访问模型、数据和 API 的客户 |
| [2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) | x402 生态 | 公司称，按 x402 公开排行榜，它"曾位列 top seller 和 top server"，并称已与 Circle、Visa 和 Stripe 的 agent 支付相关计划集成 |

被列为支持的 agent 框架，每个都有独立教程页：OpenClaw、Hermes Agent、Claude Code、Codex、Cursor、Manus 以及自定义 agent（[官网](https://aisa.one/)；无日期，访问于 2026-07-29）。

### 公司自述的计划

据 [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)，新融资用于扩充工程团队、扩展支付基础设施、接入更多模型／数据／API 提供方，以及加快稳定币结算能力。新闻稿还称计划"扩展资源市场，深化包括预算、审批流和审计轨迹在内的企业级控制，并把自主 agent 在互联网规模上安全交易所需的基础设施做大"。官网上 Foundry 标注为 "Coming Soon"，Machine-to-Machine 标注为 "Private Beta"（[官网](https://aisa.one/)；无日期，访问于 2026-07-29）。

---

## 创始人

**Jordan Liu** —— Founder and CEO（[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)）。Forbes 写道，"Liu 此前创办过一个面向东南亚无银行账户人群的类 PayPal 数字钱包，以及一个区块链钱包"（[Forbes，2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)）。

由 Qin En Looi 撰写、发表于 [2026-05-11](https://www.linkedin.com/pulse/unfiltered-jordan-liu-founder-ceo-alsa-qin-en-looi--rytrc) 的一篇人物稿补充称，那个东南亚钱包被一家上市公司收购，而他联合创办的区块链钱包"从零做到跨多条链八百万月活"，投资方包括 Binance Labs 和 UTXO。所查阅的来源均未点名这两家公司；见 `备注`。该文作者所在机构是本次种子轮的投资方，文中未给出任何日期、教育背景或 AIsa 的成立时间。

[2025-08-31 的 Pre-Seed 公告](https://www.chaincatcher.com/article/2202064)以过往履历描述了创始团队，但没有点名任何人：一位 FinTech 连续创业者、一位前 Bloomberg 金融数据业务负责人、一位 Meta AI 科学家、一位 Visa 令牌支付产品负责人，以及一位 BTC L2 核心贡献者。该稿还称团队在 AI、支付、去中心化系统和推荐系统的大规模商业化领域深耕多年。

[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)中 Liu 的头衔是 "Founder and CEO"，而 [2025-10-28 的 Pre-Seed 公告](https://www.chaincatcher.com/article/2215658)写的是"联合创始人兼 CEO"，Forbes 也称他为 co-founder。所查阅的任何来源都没有点名第二位联合创始人。

[2026-05-21 的招聘帖](https://www.v2ex.com/t/1214335)写明 AI 工程师岗位的汇报对象是 "CEO / CTO 团队"——这是所有来源中唯一一处提到 CTO 的地方。没有任何来源点名过 CTO。

截至 2026-07-29，Liu 是 AIsa 官网、新闻稿、博客、文档和 GitHub 组织中唯一被点名的个人。站点没有团队页、公司介绍页或管理层页面。Forbes 称公司有 10 人团队，但未点名其他成员（[Forbes，2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)）。

较长的公开露面：[The Breakdown 播客——"The Three Layers of AI Agent Commerce with Jordan Liu"](https://open.spotify.com/episode/4lk37Fn2yiVrni6NIRvZri)。

---

## 融资

| 日期 | 轮次（按来源的说法） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2025-08-31 | Pre-Seed | 原文称"融资金额与估值暂未披露" | 机构：Draper Associates（Tim Draper）、分布式资本（沈波）、Sats Ventures、BoostVC（Adam Draper）、WaterDrip Capital、IMPA Ventures、10K Ventures、SosoValue、CatherVC。天使投资人被描述为包括 Domo（BRC-20 创始人）、Paul Taylor（前贝莱德数字资产投资负责人）、Jackie（Side Door Ventures 合伙人）、David（Inception Capital 创始人）、Lucia（某以 Tether 为主要 LP 的基金创始合伙人）、Harry（Pioneer Fund 创始人）、Karen（前淡马锡创投合伙人），以及若干前 Visa Crypto 高管 | — | [ChainCatcher（中文）](https://www.chaincatcher.com/article/2202064) · [英文](https://www.chaincatcher.com/en/article/2202064) |
| 2025-10-28 | Pre-Seed（正文落款为旧金山，2025-10-27） | 未披露 | 机构：Draper Associates（Tim Draper）、Fenbushi Capital US（Shen Bo）、BoostVC（Adam Draper）、Sats Ventures、Trampoline Ventures、IMPA Ventures、SNZ Capital、WaterDrip Capital、10K Ventures。天使投资人被描述为包括 Paul Taylor、Domo、Jackie（Side Door Ventures）、David（Inception Capital）、Lucia（Arcanum Capital 创始合伙人，Tether 主要 LP）、Harry（Awakening Ventures 创始合伙人）、Kari（前淡马锡创投合伙人）、James/Joey（前头部 CEX 高管、基金合伙人）、前 Visa Crypto 高管、Jennifer（香港家族办公室）、Hunter（CatherVC 联合创始人） | — | [ChainCatcher（中文）](https://www.chaincatcher.com/article/2215658) · [英文](https://www.chaincatcher.com/en/article/2215658) |
| 2026-07-03 | "a new seed round" | 单轮金额未披露；650 万美元为截至目前的累计融资额 | 阿里巴巴与 Tribe Capital 联合领投，Draper Associates、住友商事、Saison Capital 及其他投资方参与 | 650 万美元 | [AIsa](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)、[GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html) |

公司自己的措辞是"截至目前累计融资 650 万美元，其中包括新的一轮种子轮"，并未把种子轮金额与 Pre-Seed 分开列出。媒体报道普遍把 650 万美元整体描述为种子轮——见 `备注`。两次 Pre-Seed 公告都没有披露金额，且相隔八周使用了同一个轮次名称——见 `备注`。

[2025-10-28 的公告](https://www.chaincatcher.com/article/2215658)引用了 Jordan Liu 和 Draper Associates 投资总监 Maxime Bucaille 的话。Draper Associates 参与了两轮，并把 AIsa 列为在投组合公司（[Draper Associates](https://www.draper.vc/portfolio/alsa)；无日期，访问于 2026-07-29）。BoostVC 出现在 Pre-Seed 投资方名单和 LinkedIn 页的投资方一行中，但不在种子轮新闻稿里。种子轮新闻稿引用了 Jordan Liu 和 Tribe Capital 投资人 Francis Zhan 的话；[2026-07-07](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html) 的 GlobeNewswire 版本还额外引用了阿里巴巴集团投资总监 Qin Jin 的话，而 aisa.one 上的版本没有。

8 月的 Pre-Seed 公告点名了内测产品 **Agentic Accounts**、**AgentPayGuard**、**AgentPayWall-402**，以及规划中的产品 **AIsaNet**、**AIsa Treasury** 和 **AIsa Marketplace**（[ChainCatcher，2025-08-31](https://www.chaincatcher.com/article/2202064)）。10 月的公告则给出四大组件并称已开放公测：**AI Marketplace-402**、**AgentPayWall-402**、**AIsaNet** 和 **AIsa Treasury**（[ChainCatcher，2025-10-28](https://www.chaincatcher.com/article/2215658)）。这些名称都未出现在当前站点上——见 `备注`。

---

## 工程

### 技术栈与平台

公司未发布技术栈页面。以下条目除另有标注外，均由可观察的公开资产确认。

- **网站与文档托管：** `aisa.one` 的响应头包含 `x-nextjs-cache`／`x-nextjs-prerender`，且 `server: cloudflare`，表明是经 Cloudflare 提供服务的 Next.js；`aisa.one/docs` 的响应头包含 `x-mintlify-client-version` 和 `x-vercel-*`，表明是部署在 Vercel 上的 Mintlify 文档；`console.aisa.one` 位于 Cloudflare 挑战页之后（响应头观察于 2026-07-29）。
- **API 表层：** `https://api.aisa.one/v1` 提供 OpenAI 兼容推理（仅 bearer），`https://api.aisa.one/apis/v1` 提供 bearer 认证的数据 API，`https://api.aisa.one/apis/v2` 是同一数据表层面向 x402 按调用付费的镜像（[mcp.json](https://aisa.one/.well-known/mcp.json)、[架构文档](https://aisa.one/docs/evaluate/architecture)）。
- **支付：** 银行卡充值走 Stripe，稳定币流程需要连接钱包并设置花费上限（[钱包文档](https://aisa.one/docs/guides/pricing/wallet)）。2026-07-29 对 `api.aisa.one/v1/models` 的未认证请求返回 `HTTP 402`，`content-type: application/problem+json`，并带有 `WWW-Authenticate: Payment` 挑战，其中包含 `method="tempo"`、`realm="api.aisa.one"`、`intent="charge"`，以及一段 base64 请求载荷，其 `methodDetails` 中写明 `chainId 4217`。
- **在同一响应中观察到的自定义协议头：** `X-AISA-Max-Price-USD`、`X-AISA-Price-USD`、`X-AISA-Pricing-Strategy`、`X-AISA-Pricing-Version`、`X-AISA-Credit-Model`、`X-AISA-Estimated-Credits`、`X-AISA-Accounted-Credits`、`X-AISA-Request-Multiplier`、`X-AISA-Result-SHA256`、`Payment-Receipt`、`Idempotency-Key` 和 `X-MPP-Discovery`。
- **Skills 的实现：** 公开仓库使用 Python 和 Node——例如 `search-research-skills` 中，Tavily skill 提供 `SKILL.md` 加 `scripts/*.mjs`，`last30days` skill 提供一个 `scripts/lib/` Python 包，内含 Reddit、TikTok、Instagram、Pinterest、YouTube、Hacker News、Polymarket、小红书、聚类、去重、重排序和渲染等模块（[仓库文件树](https://github.com/AISA-skills/search-research-skills)；访问于 2026-07-29）。七个仓库中六个采用 MIT 许可，`saas-automation-skills` 为 Apache-2.0。
- **Skill 打包方式：** 每个 skill 是一个目录，内含带 YAML front matter 的 `SKILL.md`（字段包括 `name`、`description`、`compatibility`，以及声明所需二进制文件和 `AISA_API_KEY` 等环境变量的 `metadata.aisa` 块）。声明的兼容目标是"OpenClaw、Claude Code、Hermes 等兼容 Agent Skills 的客户端，以及基于 GitHub 的 skill 目录"（[SKILL.md 示例](https://raw.githubusercontent.com/AISA-skills/search-research-skills/main/aisa-tavily/SKILL.md)；访问于 2026-07-29）。
- **限流：** 按 API key 在 RPM、TPM（输入＋输出合计）和并发三个维度上执行，文档给出了 `X-RateLimit-*` 和 `Retry-After` 响应头（[限流文档](https://aisa.one/docs/api-reference/rate-limits)）。
- **仅出现在招聘要求中的技术**，来自 V2EX 招聘帖，未在其他渠道确认已投入生产：Python 为必需语言；Go 和 TypeScript 为优先项；LangChain、CrewAI、AutoGen、MetaGPT 被列为多智能体框架，要求至少熟悉其一；RAG、向量检索与文档结构化解析；SFT、RL、DPO 后训练为加分；增长岗要求爬虫、自动化脚本以及 OpenAI、Anthropic、Gemini 的 API；n8n 和 Dify 为加分的低代码工作流平台；Claude Code、Codex、Cursor 被列为团队使用的 AI 编程工具（[2026-05-21](https://www.v2ex.com/t/1214335)、[2026-05-25](https://www.v2ex.com/t/1215230)、[2026-07-28](https://www.v2ex.com/t/1230516)）。招聘要求不能证明当前已在生产中使用。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 模型网关 | 把 OpenAI 兼容的推理请求路由到上游模型提供方，另有 Claude 原生 messages、Gemini `generateContent` 和图像生成路由 | [ai-plugin.json](https://aisa.one/.well-known/ai-plugin.json)、[模型目录](https://aisa.one/models) |
| 数据与动作 API 中继 | 在单一凭证之后归一化并代理第三方 API（搜索、社交、金融、预测市场、销售情报、邮件） | [API 索引](https://aisa.one/api) |
| 用量计量与计费 | 记录 token、请求次数和单次请求成本；从钱包余额中扣减；提供用量日志 | [定价文档](https://aisa.one/docs/guides/pricing)、[钱包文档](https://aisa.one/docs/guides/pricing/wallet) |
| 机器支付层 | 经 x402、Circle Nanopayments 和 Machine Payments Protocol 的 HTTP 402 式"挑战—结算—重试"流程 | [官网](https://aisa.one/)、[mcp.json](https://aisa.one/.well-known/mcp.json) |
| 机器发现表层 | `robots.txt`、`sitemap.xml`、`llms.txt`、`llms-full.txt`、`/docs/llms.txt`、`/.well-known/agent-card.json`（A2A）、`/.well-known/ai-plugin.json`、`/.well-known/mcp.json`、`openapi.yaml` | [agent-discovery](https://aisa.one/agent-discovery) |
| Agent Skills 目录 | 指令包同时以站点页面和 GitHub 仓库两种形式分发，可安装到 agent 运行时 | [Skills 索引](https://aisa.one/skills)、[GitHub](https://github.com/AISA-skills) |
| Foundry | 带监控、护栏和 nanopayment 计费的云托管 agent 部署——标注为 Coming Soon，无法观察 | [官网](https://aisa.one/)；无日期，访问于 2026-07-29 |
| AIsa CIO | 一个托管的示例 agent，用于多市场组合估值和 SEC 文件分析，构建在平台的金融、预测市场、搜索和模型 API 之上；页面声明所展示的对话是脚本化回放，数字仅为示意 | [agent 页面](https://aisa.one/agents/aisa-cio)；无日期，访问于 2026-07-29 |

**发现层的设计。** 署名 "AIsa Team" 的工程博客 [The Agent-Readable Web（2026-04-23）](https://aisa.one/blog/the-agent-readable-web)描述了围绕 "five-hop test" 重建发现表层的做法——agent 应能在五次 HTTP 请求内取得完成交易所需的全部信息，链路为 `robots.txt` → `llms.txt`（文中称约 650 行）→ `agent-card.json` → `sitemap.xml` → 各 skill 的 OpenAPI 规范（文中称当时已发布 24 份）。文章主张服务端渲染的文档优于客户端 SPA，主张语义化 HTML 和 JSON-LD，并把立场概括为"对 agent 友好和对人友好大体上是一致的"。

**招聘帖中描述的内部智能体系统。** [2026-05-25 的招聘帖](https://www.v2ex.com/t/1215230)称公司"对内同样是一家 AI 原生公司——所有关键业务流程都运行在自研的多智能体系统之上"，因此该岗位既为客户构建智能体基础设施，也用同一套技术支撑公司自身运转。[2026-05-21 的帖子](https://www.v2ex.com/t/1214335)把工作分为对外产品侧（在资源层之上构建自主 Agent、跨模型服务商动态路由、外部 API 组合调用、Agent 原生支付与授权）和对内系统侧（覆盖增长、客服、风控、财务的内部多 Agent 操作系统）。AI 工程师岗位描述还提到带可追溯执行链路与安全降级的自然语言运营控制台、把执行轨迹沉淀为可复用技能的技能库，以及智能体评估与回归流水线。这些都是公司在招聘语境下的自述，在公开产品表层上均无法观察到。

**MCP 状态。** MCP 清单为每个 skill 列出一个服务器条目，地址形如 `https://mcp.aisa.one/<slug>/sse`，传输方式为 `http+sse`；但清单本身注明这只是一种约定而非标准的 well-known 文件，且 `status: "planned"` 的条目"仍在逐步上线——拨号时请按 status 过滤"（[mcp.json](https://aisa.one/.well-known/mcp.json)；访问于 2026-07-29）。2026-07-29 检查时 `mcp.aisa.one` 无法解析。

### 文档中的数据处理说明

[安全与数据隐私文档](https://aisa.one/docs/guides/security)声明对请求内容采取不存储策略：prompt 和 API 响应"不被存储"，请求载荷"以瞬态方式处理，请求完成后即丢弃"，且数据不用于训练或分析。可能保留有限的运营元数据——时间戳、API key 标识、限流计数器、错误和状态信息。该页还称协议版本和加密配置"在基础设施层面管理，不对外公开"。[隐私政策](https://aisa.one/privacy)另称公司会收集账单信息、使用第三方支付处理方、不存储完整卡号，并为反洗钱（AML）和了解你的客户（KYC）合规而处理数据。

### 招聘所需技术背景

以下全部来自四篇 V2EX 招聘帖，发帖账号为 `wateryfield`，帖中点名公司为 AIsa 并给出 `aisa.one` 链接。系列中出现过的岗位：AI 工程师、后端／全栈工程师、增长工程师、开发者关系工程师。

**AI 工程师**（[2026-05-21](https://www.v2ex.com/t/1214335)、[2026-05-25](https://www.v2ex.com/t/1215230)、[2026-07-28](https://www.v2ex.com/t/1230516)）

- *必需：* 在生产环境构建过多智能体系统；熟悉 LangChain、CrewAI、AutoGen、MetaGPT 中至少一种；理解 RAG、工具调用、长任务编排以及智能体失败模式与兜底机制；能在成本、延迟、可靠性、可解释性之间做工程取舍；有从日志、人工标注、用户反馈构建训练集与评估集的实战经验。2026-07-28 版本追加了 2 年以上 AI 开发经验且主导或参与过成熟 AI 产品，以及大厂或创业公司背景，其中创业公司背景需附带用户数、营收或融资。
- *优先／加分：* 集群架构实战经验或自研过智能体框架；构建过跨服务商动态路由系统；自主部署过大模型或有 SFT、RL、DPO 后训练经验；多模态检索；支付系统、自主交易流程或高可用系统经验；大模型裁判或自动化智能体回归测试；参与过协议规范讨论或开源实现；在 AI 或智能体开源社区持续贡献。
- *明确不适合的人*（[2026-05-21](https://www.v2ex.com/t/1214335)）：只做提示词工程、不愿深入框架内部的；只想做客户产品、不愿做内部智能体系统的；需要非常明确的 PRD 才能开始推进工作的。

**后端／全栈工程师**（[2026-05-25](https://www.v2ex.com/t/1215230)、[2026-07-28](https://www.v2ex.com/t/1230516)）

- *必需：* 扎实的后端或全栈基础；熟悉 API、数据库、云基础设施和日常工程运维；具备中英文沟通能力。经验要求从 5 月的"1–5 年"变为 7 月的"3–5 年"，并追加 211/985 本科及以上学历和大型互联网公司经验。
- *加分：* LLM、模型 API、AI gateway 或 inference platform 经验；DevOps、部署、云运维；用过 Claude Code、Codex 或 Cursor。
- 该岗位明确包含平台运营工作——模型上线、价格更新——与 API、agent skills 和 plugins 开发并列。

**增长工程师**（[2026-05-25](https://www.v2ex.com/t/1215230)）

- *必需：* 独立 Owner 过完整的工具、工作流或小产品；熟悉爬虫、API 调用、自动化脚本、数据清洗与分析；熟悉主流 LLM API（OpenAI、Anthropic、Gemini）并能做工作流编排；会写 Skill；有成功的 SEO 经验，覆盖关键词、搜索意图、内容结构、收录、排名和转化；英语读写可作为工作语言。
- *加分：* 增长黑客项目经验，如批量 SEO 页面生成、批量 KOL 建联、批量内容分发；n8n 或 Dify；C 端海外产品工程化；独立开发者、出海工具、内容站或 SEO 站点经验。

**开发者关系工程师**（[2026-06-24](https://www.v2ex.com/t/1222499)，[2026-07-28](https://www.v2ex.com/t/1230516) 重发）

- *必需：* 能独立写代码、跑通 API 集成与 Agent 开发；熟悉 Python；理解 LLM、Agent、RAG 等基本概念；优秀的中文技术写作能力。
- *加分：* TypeScript 或 Go；后端、SDK 或开发者工具开发经验；LangChain 等框架；开源项目维护者；技术圈个人品牌；Meetup 或技术大会分享经验；DevTool／API 平台的 DevRel 或 DX 经验；早期创业团队经历。
- 帖中写明这是公司的首位开发者关系工程师，且职责明确面向中国开发者社区，点名 GitHub、掘金、知乎、V2EX、技术微信群和线下技术大会作为目标渠道。

### 行业领域

工作范围横跨 agent 运行时与工具协议（MCP、A2A、OpenAI 插件清单、llms.txt、OpenAPI 3.1）、API 网关与计量设计，以及机器支付：HTTP 402／x402 的挑战—结算流程、USDC 与稳定币结算、Circle Nanopayments、Machine Payments Protocol，以及经 Stripe 的银行卡处理。文档还把花费授权当作一等问题处理，区分读、写和支付三类操作，并要求在启用自主采购前先定义单次请求、单个任务和按时间的限额以及审计记录（[机器支付概念文档](https://aisa.one/docs/concepts/machine-payments-for-agents)）。隐私政策为这一范围又增加了 AML／KYC 义务（[隐私政策](https://aisa.one/privacy)）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | 站点上没有。`/careers`、`/jobs`、`/about`、`/team` 和 `/contact` 均返回 HTTP 404；页脚的 "Contact" 链接也不指向招聘页 | 2026-07-29 检查的 aisa.one 路径 |
| 公开招聘渠道 | V2EX 上账号 `wateryfield` 发布的四篇中文招聘帖，分别为 2026-05-21、2026-05-25、2026-06-24 和 2026-07-28，位于酷工作和远程工作节点。投递邮箱被 V2EX 遮蔽 | [2026-05-21](https://www.v2ex.com/t/1214335)、[2026-05-25](https://www.v2ex.com/t/1215230)、[2026-06-24](https://www.v2ex.com/t/1222499)、[2026-07-28](https://www.v2ex.com/t/1230516) |
| 远程政策 | "远程居家办公"，全职性质，不接受兼职。2026-05-21 的标题写了北上广深杭和新加坡，发帖人在帖内更正："我写错了，其实是远程的，团队偶尔几个月会线下一起办公，之前在北京是在中关村附近租了个共享办公室" | [2026-05-25](https://www.v2ex.com/t/1215230)、[2026-05-21 第 4 楼](https://www.v2ex.com/t/1214335) |
| 地点 | 总部旧金山；LinkedIn 另列出新加坡；V2EX 帖中提到此前在北京有共享办公室 | [新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)、[LinkedIn](https://www.linkedin.com/company/aipayhq)、[2026-05-21](https://www.v2ex.com/t/1214335) |
| 团队规模 | 10 人（Forbes）；2–10 人区间（LinkedIn）；招聘帖中自述为"小而精的公司"，成员具有 211/985、海外留学及大厂背景 | [Forbes](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)、[LinkedIn](https://www.linkedin.com/company/aipayhq)、[2026-07-28](https://www.v2ex.com/t/1230516) |
| 公开的招聘意向 | 融资将用于"扩充 AIsa 的工程团队" | [新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 工作语言 | 没有公司层面的统一政策。AI 工程师和增长工程师岗位要求英文读写作为工作语言；后端岗位要求中英文沟通，发帖人在帖内解释为"因为有时候需要和供应商还有客户英语交流"；开发者关系岗位要求优秀的中文技术写作能力。2026-07-28 帖下一条询问"一定要英语流利吗"的回复，截至 2026-07-29 未获答复 | [2026-05-25 及第 2 楼](https://www.v2ex.com/t/1215230)、[2026-07-28](https://www.v2ex.com/t/1230516)、[2026-06-24](https://www.v2ex.com/t/1222499) |
| 薪资 | 未公开。三个帖子里都有人直接问过，发帖人只回过一次"open 可聊"，另两次未答 | [2026-05-21 回复](https://www.v2ex.com/t/1214335)、[2026-05-25 回复](https://www.v2ex.com/t/1215230)、[2026-07-28](https://www.v2ex.com/t/1230516) |
| 期权 | 2026-05-21 的 AI 工程师帖写"有竞争力薪资 + 创始团队级期权"；之后的帖子只写薪资 | [2026-05-21](https://www.v2ex.com/t/1214335) |
| 职级路线与汇报关系 | AI 工程师被描述为资深 IC 路线、不管理人，汇报对象为 "CEO / CTO 团队" | [2026-05-21](https://www.v2ex.com/t/1214335) |
| 面试方式 | 视频面试 | [2026-07-28](https://www.v2ex.com/t/1230516) |
| 加班、签证支持、福利、流失率 | 未公开。2026-05-25 帖下一条询问加班情况的回复，截至 2026-07-29 未获答复 | [2026-05-25 回复](https://www.v2ex.com/t/1215230) |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-29）：`aisa.one` 首页、`robots.txt`、完整 `sitemap.xml`、新闻索引、博客索引及所列十篇文章的元信息、产品 `llms.txt` 与 `/docs/llms.txt`、定价／钱包／限流／架构／安全／机器支付等文档页、服务条款与隐私政策、`.well-known` 发现文件、`api.aisa.one` 响应头，以及 `AISA-skills` GitHub 组织及其七个仓库；对品牌名、法律名称和创始人的英文与中文检索；Draper Associates 投资组合页、LinkedIn 公司页、Dealroom 档案；英文媒体报道；在 36 氪、钛媒体、ChainCatcher、Odaily、PANews、BlockBeats、深潮 TechFlow、Foresight News 和金色财经上的中文检索；以及 V2EX 酷工作和远程工作节点，包括发帖账号的完整主题列表。

- **公司自有渠道上的招聘入口。** 站点没有招聘页，在所查阅的英文招聘网站和数据库中也未找到 AIsa 或 AIPay 的职位。招聘实际发生在 V2EX 上、以中文进行——见 `工程`。aisa.one 上没有任何链接指向这些帖子。
- **除创始人外的具名员工。** 没有。没有团队页，也没有工程署名——唯一一篇技术文章署名为 "AIsa Team"。V2EX 帖子由账号 `wateryfield` 发布，该账号未写明姓名或职务。
- **薪资区间。** 四篇 V2EX 招聘帖均未公布；被直接问及时答复为"open 可聊"。
- **以货币计的收入和交易额。** 未披露。增长只以倍数（150 倍、200 倍）和一个 API 调用次数（2026-04-23 的"超过一百万次"）形式给出。
- **种子轮的单独金额。** 公司只公布 650 万美元的累计数；Pre-Seed 金额始终未披露。
- **安全认证。** 所查阅的任何页面都未声明 SOC 2、ISO/IEC 27001 或同类认证。安全文档明确表示不公开协议版本和加密配置。
- **状态页或公开 SLA。** 未找到；`status.aisa.one` 无法解析。
- **工商登记记录。** 在所查阅的公开来源中未找到 `AIPay Inc.` 或 `AIPAY GLOBAL PTE. LTD` 的任何登记或备案记录；所查的新加坡登记信息聚合站点返回的是机器人验证页面。
- **创始人此前公司的具体名称。** Forbes 和投资人撰写的人物稿描述了两段创业经历，但都未点名。一条搜索结果摘要把那个多链钱包指认为 UXUY；未能取到支持该指认的来源页面，故此处记为未经确认。
- **Dealroom 档案。** 2026-07-29 对自动访问返回 HTTP 403，未用作来源。

### 不同来源之间的不一致

- **注册 agent 数：** 超过 50,000（[公司新闻稿，2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)）对"超过 20,000"（[Forbes，同日](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)），两者都用了"未使用付费营销"的表述。官网另称 "Join 5,000+ Agents Already Running"（[官网](https://aisa.one/)；无日期，访问于 2026-07-29），描述的是运行中而非注册的 agent；所查阅的资料中没有任何一处调和这三个数字。
- **法律名称：** [服务条款](https://aisa.one/TOS)中为 `AIPay Inc.`，[隐私政策](https://aisa.one/privacy)中为 `AIPAY GLOBAL PTE. LTD`，两页都标注 2026-03-10 更新，也都写着 "dba AIsa"。
- **轮次口径：** 公司称 650 万美元是"截至目前的累计融资额，其中包括新的一轮种子轮"（[新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)）；Forbes、FinSMEs 和 CryptoRank 则描述为"650 万美元种子轮"，这一口径会把 2025 年的 Pre-Seed 排除在总额之外。
- **同一轮次名称下的两次 Pre-Seed 公告。** [2025-08-31](https://www.chaincatcher.com/article/2202064) 和 [2025-10-28](https://www.chaincatcher.com/article/2215658) 两篇都宣布完成 "Pre-Seed" 且都未披露金额。两篇互不提及，投资方名单也有差异：SosoValue 和 CatherVC 在 8 月以机构身份出现、10 月则不再出现，取而代之的是 CatherVC 联合创始人以天使身份出现；Trampoline Ventures 和 SNZ Capital 只出现在 10 月。这究竟是同一轮公告两次、一次追加，还是两次独立交割，所查阅的资料均未说明。
- **两次公告中投资方名称的写法不同：** 8 月写"分布式资本（沈波）"，10 月写 "Fenbushi Capital US（Shen Bo）"——是同一家机构；那位前淡马锡创投合伙人 8 月写作 "Karen"、10 月写作 "Kari"；Harry 在 8 月是 Pioneer Fund 创始人、在 10 月是 Awakening Ventures 创始合伙人；Lucia 的基金 8 月未具名、10 月写作 Arcanum Capital。
- **创始人头衔：** [2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)写 "Founder and CEO"，[2025-10-28 公告](https://www.chaincatcher.com/article/2215658)写"联合创始人兼 CEO"，[Forbes](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)写 co-founder。第二位联合创始人始终未被点名。
- **招聘帖与新闻稿对融资的描述不同。** [2026-05-21 的 V2EX 帖](https://www.v2ex.com/t/1214335)称"公司已完成两轮融资，融资规模数千万，即将启动 A 轮"，投资方"覆盖支付、云计算等领域"。[2026-07-03 新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)称截至目前累计 650 万美元，并把该轮称为种子轮而非 A 轮。V2EX 的说法没有写明币种，且招聘帖的来源强度弱于公司新闻稿；此处并列记录，不作调和。
- **资源目录规模在不同时点的口径：** [2025 年 10 月](https://www.chaincatcher.com/article/2215658)称 AI Marketplace-402 聚合"600+ LLMs、100 万+ 数据 API 与 GPU"，而当前[官网](https://aisa.one/)写 "1000+ APIs, Skills, and LLMs"，[sitemap](https://aisa.one/sitemap.xml) 中为 102 个模型页。2025 年的数字描述的是一个如今已不在站点上的产品名。
- **目录规模：** [官网](https://aisa.one/)的 "1000+ APIs, Skills, and LLMs" 对 A2A card 中广播的 43 项能力（[agent-discovery](https://aisa.one/agent-discovery)）以及 [sitemap](https://aisa.one/sitemap.xml) 中的 240 个目录页（102 模型、90 API、48 skill）。这些数字统计的单位不同——端点、广播的能力和目录页——且没有任何页面说明用的是哪一种。
- **模型网关覆盖面：** [agent card](https://aisa.one/.well-known/agent-card.json) 写 "50+ LLMs"，[ai-plugin 清单](https://aisa.one/.well-known/ai-plugin.json)和 [2026-02-19 博客](https://aisa.one/blog/introducing-aisa-unified-gateway)标题写 "100+ AI models"，而 sitemap 中是 102 个模型页。
- **LinkedIn 上的投资方名单：** [LinkedIn 页面](https://www.linkedin.com/company/aipayhq)列出 Tribe Capital、Draper Associates 和 BoostVC；[种子轮新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)列出阿里巴巴、Tribe Capital、Draper Associates、住友商事和 Saison Capital，未提及 BoostVC，后者只出现在 [Pre-Seed 名单](https://www.chaincatcher.com/en/article/2202064)中。
- **阿里巴巴的引语：** 出现在 [2026-07-07 的 GlobeNewswire 版本](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html)中，而 [aisa.one 上标注 2026-07-03 的版本](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)没有。两份文本的其余内容基本相同。

### 其他

- **自 Pre-Seed 以来产品命名已整体更换。** 2025 年 8 月的公告点名了 Agentic Accounts、AgentPayGuard、AgentPayWall-402、AIsaNet、AIsa Treasury 和 AIsa Marketplace（[ChainCatcher，2025-08-31](https://www.chaincatcher.com/en/article/2202064)）；2025 年 10 月的公告点名了 AI Marketplace-402、AgentPayWall-402、AIsaNet 和 AIsa Treasury（[ChainCatcher，2025-10-28](https://www.chaincatcher.com/article/2215658)）；2025 年 11 月的一篇赞助报道仍把产品描述为 "AIsaNet（微支付网络）与 AIsa Treasury（跨币种流动性引擎）"（[ChainCatcher，2025-11-07](https://www.chaincatcher.com/en/article/2218188)）。截至 2026-07-29，这些名称都未出现在站点上，站点上的产品面是 Model Gateway、APIs、Skills、Machine-to-Machine 和 Foundry。
- **报道在语言和时段上是分裂的。** 2025 年的两次 Pre-Seed 公告和黑客松赞助由中文加密行业媒体（ChainCatcher）刊发，未找到英文主流科技媒体报道；2026 年的种子轮由英文商业与创投媒体（Forbes、Business Insider、Yahoo Finance、FinSMEs、CryptoRank、The AI Insider）刊发，截至 2026-07-29 在所查阅的来源中未找到中文报道。就种子轮检索 36 氪、钛媒体、Odaily、PANews、BlockBeats、深潮 TechFlow、Foresight News 和金色财经，均无对应文章。
- **2025 年公告中的生态合作表述，当前站点没有以同样的方式重复。** 2025 年 8 月列出了与 Circle、Visa、Stripe、PayPal、Privy 和 JPMorgan Kinexys 的关系（[ChainCatcher](https://www.chaincatcher.com/article/2202064)）；当前的[融资新闻稿](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)只收窄为"已与 Circle、Visa 和 Stripe 的 agent 支付相关计划集成"。截至 2026-07-29，站点上没有提及 PayPal、Privy 和 JPMorgan Kinexys。
- **面向不同受众的定位表述并不一致。** 公司自己的新闻稿称其为"资源与交易网络"；Forbes 和 Business Insider 的标题把它写成一家支付公司；LinkedIn 页面名称是 "The Resource Marketplace for AI Apps"；Draper Associates 的投资组合条目则描述为"一个可类比 Visa 的 AI agent 支付网络"，并使用区块链技术（[Draper Associates](https://www.draper.vc/portfolio/alsa)）。
- **V2EX 上的招聘帖构成一个带日期的序列，可以互相比对。** 后端岗位的经验要求从"1–5 年"（[2026-05-25](https://www.v2ex.com/t/1215230)）变成"3–5 年"并追加 211/985 学历和大型互联网公司经验（[2026-07-28](https://www.v2ex.com/t/1230516)）。发帖人在 2026-05-27 宣布后端 HC 已招到并暂时关闭，之后又在 2026-07-28 重新发布该岗位。5 月和 6 月的帖子没有点名投资方（只写"国际顶级风投及知名战略投资方，覆盖支付、云计算等领域"），7 月的帖子在融资公布之后点了名。2026-07-29 访问时四帖的浏览量分别为 3,645、3,327、2,036 和 982。
- **招聘帖写明站点在中国大陆需要 VPN 才能打开**（"需 vpn 打开网址"，[2026-07-28](https://www.v2ex.com/t/1230516)），而同一批帖子正在招聘一位职责面向中国开发者社区的开发者关系工程师，站点也发布了简体和繁体中文版本。
- **相对于其规模，公司发布了异常多的机器可读表层**——六份发现文件、一份 OpenAPI 3.1 规范、13 种语言的分语言站点树和 240 个目录页——同时却没有团队页、招聘页或任何具名的工程人员。
- **产品的大部分细节都在控制台之后。** 逐端点定价、用量日志、预算和 API key 管理在文档中有描述，但都需要账户；`console.aisa.one` 位于 Cloudflare 挑战页之后。
- **官网把 Machine-to-Machine 标注为 Private Beta、Foundry 标注为 Coming Soon**，而融资新闻稿、博客文章以及 `api.aisa.one` 上实际返回的 `HTTP 402` 挑战都在描述机器支付已在运行。测试版标注与 `/apis/v2` 上已上线的 x402 镜像之间的范围差异，所查阅的页面都没有解释。

---

## 资料来源

**官方**

- [官网](https://aisa.one/)
- [新闻索引](https://aisa.one/news) —— [融资新闻稿，2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)
- [博客](https://aisa.one/blog) —— [The Agent-Readable Web，2026-04-23](https://aisa.one/blog/the-agent-readable-web) · [Agentic Economy on Arc 的数据层，2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc) · [Agentic Commerce on Arc 第二名，2026-02-26](https://aisa.one/blog/aisa-awarded-second-place-agentic-commerce-arc-hackathon) · [ETHDenver 2026 的 Claws Out，2026-02-27](https://aisa.one/blog/aisa-sponsors-claws-out-ethdenver-2026) · [统一网关，2026-02-19](https://aisa.one/blog/introducing-aisa-unified-gateway)
- [文档](https://aisa.one/docs) —— [定价](https://aisa.one/docs/guides/pricing) · [钱包与支付](https://aisa.one/docs/guides/pricing/wallet) · [限流](https://aisa.one/docs/api-reference/rate-limits) · [架构](https://aisa.one/docs/evaluate/architecture) · [安全评估](https://aisa.one/docs/evaluate/security) · [安全与数据隐私](https://aisa.one/docs/guides/security) · [面向 agent 的机器支付](https://aisa.one/docs/concepts/machine-payments-for-agents) · [面向 agent 的文档索引](https://aisa.one/docs/llms.txt)
- [目录](https://aisa.one/models) —— [APIs](https://aisa.one/api) · [Skills](https://aisa.one/skills) · [AIsa CIO agent](https://aisa.one/agents/aisa-cio)
- [Agent Discovery](https://aisa.one/agent-discovery) —— [agent-card.json](https://aisa.one/.well-known/agent-card.json) · [ai-plugin.json](https://aisa.one/.well-known/ai-plugin.json) · [mcp.json](https://aisa.one/.well-known/mcp.json) · [产品 llms.txt](https://aisa.one/llms.txt) · [sitemap.xml](https://aisa.one/sitemap.xml)
- [服务条款](https://aisa.one/TOS) · [隐私政策](https://aisa.one/privacy)
- [GitHub 组织 `AISA-skills`](https://github.com/AISA-skills) —— [search-research-skills](https://github.com/AISA-skills/search-research-skills) · [SKILL.md 示例](https://raw.githubusercontent.com/AISA-skills/search-research-skills/main/aisa-tavily/SKILL.md)

**新闻稿**

- [AIsa Raises $6.5M to Build the AI Agent Resource Network —— 2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)
- [同一新闻稿的 GlobeNewswire 分发版本 —— 2026-07-07](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html)

**第三方报道与档案**

- [Forbes —— Startup Raises $6.5 Million…，2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)
- [Business Insider Markets —— 融资报道，2026-07](https://markets.businessinsider.com/news/stocks/aisa-raises-6-5m-co-led-by-alibaba-and-tribe-capital-to-build-the-transaction-network-for-ai-agents-1036305081)
- [Yahoo Finance —— 融资报道，2026-07](https://finance.yahoo.com/technology/ai/articles/aisa-raises-6-5m-co-204900040.html)
- [FinSMEs —— AIsa Closes Seed Funding，2026-07](https://www.finsmes.com/2026/07/aisa-closes-seed-funding.html)
- [CryptoRank —— 种子轮摘要，2026-07-03](https://cryptorank.io/news/feed/alsa-seed-2026-07-03)
- [The AI Insider —— 种子轮报道，2026-07-17](https://theaiinsider.tech/2026/07/17/aisa-secures-6-5m-co-led-by-alibaba-and-tribe-capital-to-build-the-transaction-network-for-ai-agents/)
- [ChainCatcher —— Pre-Seed 公告，2025-08-31（中文）](https://www.chaincatcher.com/article/2202064) · [英文](https://www.chaincatcher.com/en/article/2202064)
- [ChainCatcher —— 第二次 Pre-Seed 公告，2025-10-28（中文）](https://www.chaincatcher.com/article/2215658) · [英文](https://www.chaincatcher.com/en/article/2215658)
- [ChainCatcher —— Solana x402 黑客松赞助，2025-11-07（中文）](https://www.chaincatcher.com/article/2218188) · [英文](https://www.chaincatcher.com/en/article/2218188)
- V2EX 招聘帖，发帖账号 `wateryfield` —— [AI Engineer，2026-05-21（中文）](https://www.v2ex.com/t/1214335) · [AI／后端／增长工程师，2026-05-25（中文）](https://www.v2ex.com/t/1215230) · [开发者关系工程师，2026-06-24（中文）](https://www.v2ex.com/t/1222499) · [AI／后端／开发者关系工程师，2026-07-28（中文）](https://www.v2ex.com/t/1230516)
- [Draper Associates —— 投资组合条目](https://www.draper.vc/portfolio/alsa)
- [LinkedIn —— 公司页](https://www.linkedin.com/company/aipayhq)
- [LinkedIn —— "Unfiltered with Jordan Liu"，Qin En Looi，2026-05-11](https://www.linkedin.com/pulse/unfiltered-jordan-liu-founder-ceo-alsa-qin-en-looi--rytrc)
- [The Breakdown 播客 —— The Three Layers of AI Agent Commerce with Jordan Liu](https://open.spotify.com/episode/4lk37Fn2yiVrni6NIRvZri)
- [Dealroom —— 公司档案（2026-07-29 对自动访问返回 403）](https://app.dealroom.co/companies/aisa_one_interface_for_compute_data_and_monetization)
