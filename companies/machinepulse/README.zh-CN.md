# MachinePulse

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

MachinePulse Pte. Ltd. 是一家在新加坡注册的公司，做它自己所称的「Proactive AI Agents」（主动式 AI 智能体）（[招聘页面](https://join.machinepulse.ai/)；无日期，访问于 2026-07-29）。公司官网只有一页占位内容，实质内容分散在三个独立产品上：**Karpo**，一个活在 iMessage 里、在六个城市推荐场所和活动的免费消费级 AI；**World2Agent（W2A）**，一个把现实世界信号喂给 AI 智能体的 Apache-2.0 协议；以及 **Shotwright**，一个在 Windows 容器里驱动 Adobe After Effects 的 MIT 许可智能体。

- Karpo 于 2026-03-09 公开发布，截至 [2026-07-28](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) 自报已交付 52 万多条推荐、400 多万次对话，以及「接近 40% 的即时正面响应率」。
- 唯一找到的融资表述出自公司自己，在[招聘页面](https://join.machinepulse.ai/)和某个岗位正文中重复出现：「backed by top-tier USD funds, with a valuation approaching $100 million」（获顶级美元基金支持，估值接近 1 亿美元）。任何地方都没有公布过轮次、投资方或日期。
- 招聘站列出 20 个在招岗位（[jobs API](https://join.machinepulse.ai/api/jobs)；访问于 2026-07-29）。其中 18 个定位在**上海**，1 个在纽约；所有岗位的可选地点都是新加坡、上海、纽约、加州湾区。工程岗位描述了 Go 与 Python 后端、跑在 AWS/GCP/Azure 上的 Kubernetes、一个 iOS 客户端，以及一个自研的 LLM 后训练团队。
- [GitHub 组织](https://github.com/machinepulse-ai)创建于 2025-11-11，标注地点为新加坡，有 6 个公开仓库；[world2agent](https://github.com/machinepulse-ai/world2agent) 在 2026-07-29 访问时有 1,245 个 star、40 个 fork。
- 管理层只能从 LinkedIn 识别，且必须有登录态：**Leah Wang**，2026 年 1 月起任 CEO（此前在字节跳动任 Strategic Product Manager 至 2025 年 11 月）；**Nanqun Chen**，2025 年 12 月起任联合创始人兼 COO（前字节跳动，目前同时挂着阶跃星辰 Lead Product Manager）；**Lucas Wu**，2025 年 12 月起任创始成员（前腾讯、前智谱 Z Fund）。公司自己掌控的任何页面上都没有出现过这些名字。
- Karpo 在 iMessage 上的运行依托 **Linq** 的消息基础设施，这一点由 MachinePulse 一位创始成员陈述，并在 [Linq 的社区页面](https://linqapp.com/community)得到印证。
- **重名问题：**另有一家完全无关的工业物联网公司也叫 MachinePulse（孟买，`machinepulse.com`），它占据了搜索结果和创业数据库。Crunchbase、Tracxn、GetLatka 上「MachinePulse」的条目描述的是那一家，不是这一家。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | MachinePulse Pte. Ltd. | [官网页脚](https://www.machinepulse.ai/)、[Karpo 关于页面](https://app.karpo.ai/about-us) |
| 注册地 | 新加坡（Pte. Ltd. 是新加坡私人有限公司的形式） | 由实体名称推断；未与 ACRA 核对 |
| 实际办公地点 | 20 个在招岗位中 18 个定位在上海，1 个在纽约；所有岗位的可选地点为新加坡、上海、纽约、加州湾区 | [jobs API](https://join.machinepulse.ai/api/jobs)；访问于 2026-07-29 |
| 公开品牌 | MachinePulse；产品品牌为 Karpo、World2Agent、Shotwright | [官网](https://www.machinepulse.ai/) |
| 口号 | 「The Very Pulse of the Machine」；「building something PROACTIVE」 | [官网](https://www.machinepulse.ai/) |
| 自述方向 | 「Proactive AI Agents」与人机交互的演进 | [招聘页面](https://join.machinepulse.ai/) |
| GitHub 组织创建时间 | 2025-11-11；地点新加坡；6 个公开仓库 | [GitHub API](https://github.com/machinepulse-ai) |
| 联系方式 | support@（Karpo）、contact@（GitHub 组织）、partnership@、ahr@（社招）、intern@（实习），均为 `@machinepulse.ai` | [官网](https://www.machinepulse.ai/)、[Karpo 关于页面](https://app.karpo.ai/about-us)、[招聘页面](https://join.machinepulse.ai/) |
| 员工人数 | LinkedIn 区间为 51–200 人，有 17 人把 MachinePulse 列为当前雇主；411 个关注者 | [LinkedIn](https://www.linkedin.com/company/machinepulseai/about/)；2026-07-29 登录状态下访问 |
| 管理层 | Leah Wang（CEO）、Nanqun Chen（联合创始人、COO）、Lucas Wu（创始成员）、Titus Zhai（增长负责人） | LinkedIn 主页；见`创始人`一节 |
| 社交账号 | [LinkedIn](https://www.linkedin.com/company/machinepulseai/about/)、X [@MachinePulse_AI](https://x.com/MachinePulse_AI) 与 [@Karpo_AI](https://x.com/Karpo_AI)、[Instagram](https://www.instagram.com/karpo.ai)、[Discord](https://discord.gg/hDjaD8pX) | [官网](https://www.machinepulse.ai/)、[World2Agent](https://world2agent.ai/) |
| 官网版权年份 | 2026 | [官网](https://www.machinepulse.ai/) |

官网、招聘页面、Karpo 各页面和 LinkedIn 主页均为持续更新且没有发布日期的页面；访问于 2026-07-29。官网没有关于页面、团队页面、新闻索引、地址或注册号。

### 品牌与法律实体

有两家互不相关的公司使用 MachinePulse 这个名字。判断一条资料说的是哪一家，是本页其余全部事实的前提。

| 名称 | 域名 | 是什么 | 关系 |
|---|---|---|---|
| MachinePulse Pte. Ltd. | [machinepulse.ai](https://www.machinepulse.ai/) | 新加坡实体；Karpo、World2Agent、Shotwright | 本页调研对象 |
| MachinePulse（印度） | machinepulse.com | 总部孟买的工业物联网 / 机器数据分析平台，约 10 人，自筹资金 | 未发现任何关联 |

[Crunchbase](https://www.crunchbase.com/organization/machinepulse)、[Tracxn](https://tracxn.com/d/companies/machine-pulse/__T2EbVVSjXHxNVi2tptAU2PdQE2I7bYoG-0V2Qt1iFD8) 和 [GetLatka](https://getlatka.com/companies/machinepulse) 描述的都是印度那家；这些资料里的创始人、收入和人数数字不适用于新加坡实体。未找到新加坡实体的任何数据库条目（检索于 2026-07-29）。

uspto.report 的检索结果显示，以「Machinepulse Pte. Ltd.」为所有人提交了四件美国商标申请：[KARPO（99653628）](https://uspto.report/TM/99653628)、[KARPO（99653232）](https://uspto.report/TM/99653232)、[K（99653634）](https://uspto.report/TM/99653634)和 [MACHINEPULSE（99653745）](https://uspto.report/TM/99653745)。这些记录页在 2026-07-29 访问时返回 HTTP 403，因此申请日期、状态和所有人地址均未核实。所述商品与服务范围覆盖人工智能、机器学习和生成式模型的 SaaS，以及配置与管理自主 AI 智能体和工作流的软件。

---

## 产品

### Karpo

一个免费的消费级城市发现 AI 助手，通过 iMessage 向一个美国号码（+1 415 886 0326）发短信使用，也被描述为有独立 App（[Karpo 首页](https://app.karpo.ai/)、[工作方式](https://app.karpo.ai/how-it-works)、[FAQ](https://app.karpo.ai/faqs)；均访问于 2026-07-29）。

- **做什么** —— 推荐餐厅、酒吧、画廊、现场音乐和活动；从对话中学习偏好；可以加进 iMessage 群聊帮一群人收敛出方案（[FAQ](https://app.karpo.ai/faqs)）。
- **覆盖城市** —— 「最了解纽约、旧金山和伦敦」；也覆盖迈阿密、洛杉矶和新加坡（[关于页面](https://app.karpo.ai/about-us)）。
- **预订** —— 通过 Ticketmaster、Viator、Expedia 和 Klook 完成集成预订（[2026-07-28 新闻稿](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html)）。
- **内容栏目** —— 一个每周更新的栏目「Karpo's Finds」，公司自己的对比页面描述为 1,000–1,500 字、带引用出处、锚定到具体街区的稿件，覆盖 12 个生活方式标签（[对比页面](https://app.karpo.ai/scenarios/karpo-vs-gemini-best-ai-city-assistant-nyc-2026)）。这就是站点 `/explore/` 和 `/city-guides/` 板块背后的内容。
- **价格** —— 免费；FAQ 对是否完全免费的回答是「Yes」，公司对比页面写「Karpo is $0/year」，且「完整产品 —— 无限量 iMessage 对话、Karpo's Finds 栏目访问、主动推荐 —— 都是免费的」。没有任何付费档位、订阅或应用内购买的说明。
- **形态** —— 同一页面写道「Karpo does not have its own app icon. It is an iMessage extension.」（Karpo 没有自己的应用图标，它是一个 iMessage 扩展。）

### World2Agent（W2A）

一个开放协议，展示页在 [world2agent.ai](https://world2agent.ai/)，代码在 [github.com/machinepulse-ai/world2agent](https://github.com/machinepulse-ai/world2agent)，Apache 2.0 许可。它规范 AI 智能体如何感知外部数据，采用 `World → Sensor → Agent` 模型：sensor 是独立的 npm 包，监视某个数据源并以统一 schema 发出信号，智能体消费这些信号。

- **[架构文档](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md)中陈述的设计约束：**协议「自然语言优先」；sensor 保持中立 —— 不做价值判断，不假设自己运行在哪里，也不定义路由、优先级或动作。
- **传输方式：**stdout 管道、HTTP POST、WebSocket / Server-Sent Events，以及由消费方自定义的传输。
- **有原生插件的智能体运行时：**Claude Code、Hermes、OpenClaw（[README](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/README.md)）。
- **发布方式：**用 `build-w2a-sensor` skill 构建 sensor，发布到 npm，并在 [SensorHub](https://world2agent.ai/hub) 注册。
- **路线图：**一个 graph 层，在信号交付给智能体之前把多个 sensor 的信号组合和加工。

公司把该协议描述为与 MCP 互补而非替代（[中文报道，2026-04-29](https://www.80aj.com/2026/04/29/ai-agent-realtime-perception/)）。

### Shotwright

[github.com/machinepulse-ai/shotwright](https://github.com/machinepulse-ai/shotwright)，MIT 许可，Python，创建于 2026-05-18。一个对话驱动的产品：Copilot 或 Codex 智能体在 Windows 容器里操作真实的 Adobe After Effects 安装 —— 规划素材、准备资源、编写 JSX 自动化脚本、交给 nexrender 做无头渲染，再把成片 mp4 流回浏览器。README 中的技术栈标识包括 Windows Containers LTSC 2025、After Effects 2026、FastAPI 0.110+、React 18 和 Node 20+。README 声明目标「不是通用 AI 视频自动化」，而是一个可复现的 AE 运行时加上一层智能体。该仓库同时提供简体中文 README。

### 商业化

三个产品都没有任何已公开的收入机制。Karpo 免费且没有描述付费档位，World2Agent 和 Shotwright 都是宽松许可的开源项目，2026-07-29 查阅的所有站点上都没有企业版、价目页面或销售联系方式。

### 公开数据的变化

| 日期 | 公布的数字 | 来源 |
|---|---|---|
| 2025-11-11 | GitHub 组织创建 | [GitHub API](https://github.com/machinepulse-ai) |
| 2026-03-09 | Karpo 公开发布 | [2026-07-28 新闻稿](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) |
| 2026-04-23 | world2agent 仓库创建 | [GitHub API](https://github.com/machinepulse-ai/world2agent) |
| 2026-07-28 | Karpo：52 万多条推荐、400 多万次对话、约 40% 即时正面响应率，发布后 80 天 | [新闻稿](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) |
| 访问于 2026-07-29 | world2agent：1,245 star、40 fork；shotwright：13 star；其余四个仓库：0–5 star | [GitHub API](https://github.com/machinepulse-ai) |
| 访问于 2026-07-29 | SensorHub：11 个 sensor；下载最多的是 Hacker News sensor，526 次 | [SensorHub](https://world2agent.ai/hub) |
| 访问于 2026-07-29 | app.karpo.ai sitemap：5,847 个 URL，其中 5,520 个是 `/scenarios/` 页面 | [sitemap](https://app.karpo.ai/sitemap.xml) |

同一时间段内，400 多万次对话对应 52 万多条推荐；新闻稿没有定义这两个口径，也没有给出用户数。

### 已公布的合作方

| 日期 | 对象 | 详情 |
|---|---|---|
| [2026-07-28](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) | Ticketmaster、Viator、Expedia、Klook | 被列为集成预订合作方 |
| [2026-07-28](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) | Molly Tea（新加坡） | 线下互动活动，用户答对本地餐饮知识问答即可获得免费饮品 |

新闻稿没有说明这些预订集成属于商业协议、联盟分成还是公开 API 调用。

### 公司陈述的计划

关于商业方向最清楚的陈述出自岗位描述，而不是任何公告。[Senior Manager, Commercial Operations 岗位](https://join.machinepulse.ai/api/jobs)（创建于 2026-05-10）把职责定为搭建「一个北美本地生活平台」：建立供给侧运营体系，并独立推动外部合作。岗位列出了希望候选人具备哪类平台的经验 —— Yelp、OpenTable、Resy、Booking.com、Google Places、Eventbrite、SeatGeek —— 并要求 3 年以上北美本地生活、旅游或酒店行业经验。

其他岗位把目标市场定义为北美城市（主要是纽约和洛杉矶），并把日韩市场列为次要的文化重点；获客渠道为 Instagram、TikTok、Reddit、Discord、YouTube、X、Google 与 Meta 投放，以及 SEO 和 ASO。

[AI Product Manager](https://join.machinepulse.ai/api/jobs) 等多个岗位把产品描述为处于「0 到 1」阶段。

---

## 创始人

官网、招聘页面、Karpo 全部页面、所有仓库以及所有新闻稿中，都没有点出创始人或任何高管。[GitHub 组织](https://github.com/orgs/machinepulse-ai/people)没有公开成员。管理层只能从 LinkedIn 主页识别，而这需要登录态才能查看；以下四人均于 2026-07-29 读取。

| 姓名 | 角色 | 起始 | 所在地 | 来源 |
|---|---|---|---|---|
| Leah Wang | 首席执行官 | 2026 年 1 月 | 北美 | [LinkedIn](https://www.linkedin.com/in/leah-wang-8676903a8/) |
| Nanqun Chen | 联合创始人、COO | 2025 年 12 月 | 新加坡 | [LinkedIn](https://www.linkedin.com/in/nanqunchen/) |
| Lucas Wu | 创始成员 | 2025 年 12 月 | 新加坡 | [LinkedIn](https://www.linkedin.com/in/fan-lucas-wu/) |
| Titus Zhai | 增长负责人 | — | — | [2026-07-28 新闻稿](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) |

**Leah Wang** —— 首席执行官，主页标题栏自述为「Founder」。该主页只列了两段经历，20 个联系人。

- 2023 年 8 月 – 2025 年 11 月：字节跳动，Strategic Product Manager（所列地区：亚洲）。
- 2026 年 1 月至今：MachinePulse 首席执行官，列为「Self-employed」，地区为北美。

**Nanqun Chen** —— 联合创始人兼 COO。

- 2013 年 7 月 – 2014 年 3 月：IBM 软件工程师（DevOps SaaS），宁波。
- 2014 年 3 月 – 2015 年 12 月：宁波智慧物流科技产品经理，主页描述为 IBM Smarter Logistics Lab；负责化工与冷链物流的 SaaS 平台。
- 2016 年 1 月 – 2017 年 8 月：上海诺德供应链管理（NodeSCM）高级产品经理，负责 TMS/WMS 平台。
- 2017 年 8 月 – 2020 年 12 月：小贝文化科技（上海）联合创始人兼产品经理，做 Heychat 社交应用。
- 2020 年 12 月 – 2022 年 8 月：Silot.ai 高级产品经理，上海；负责印尼市场的 C2C 电商应用 Kaya。
- 2022 年 10 月 – 2024 年 2 月：字节跳动高级产品经理，上海。
- 2024 年 4 月至今：阶跃星辰（StepFun）Lead Product Manager，上海。主页上这一段与 MachinePulse 的职位并列显示为「至今」—— 见`备注`。
- 2025 年 12 月至今：MachinePulse 联合创始人，新加坡。

**Lucas Wu** —— 创始成员；主页标题栏为「Building proactive AI @MachinePulse, ex-Tencent, Duke Fuqua」。所列教育经历：杜克大学 Fuqua 商学院。

- 2019–2021 年：在 BCG、腾讯（智慧零售战略）、AWS（项目管理）和天善资本实习；2021 年 2 月 – 5 月在 TikTok 任 Monetization Product Intern（北京），负责自助广告平台的风控。
- 2021 年 10 月 – 2023 年 2 月：腾讯轮岗产品经理（腾讯产培项目），深圳。
- 2023 年 3 月 – 2025 年 9 月：天善资本投资经理，北京；早期 AI 软硬件与智能制造方向。
- 2025 年 9 月 – 2025 年 12 月：智谱 AI（Z.ai）Z Fund 高级投资经理，北京。
- 2025 年 12 月至今：MachinePulse 创始成员，新加坡。
- 2020 年 6 月至今：非营利组织 SEA 社会创新俱乐部发起人。

### 公司陈述的团队来源

关于团队背景存在四种表述，都没有点名任何人，且对创始人来自哪家公司说法不一致：

| 说法 | 来源 |
|---|---|
| 「我们的团队来自领先的 AI 应用团队和全球互联网公司，包括 TikTok、Amazon、PayPal 和 Keeta」 | [LinkedIn 公司简介](https://www.linkedin.com/company/machinepulseai/about/) |
| 「一家隐身状态的 AI 创业公司（由前 TikTok 产品负责人创办）」 | [Lucas Wu 的 LinkedIn 动态](https://www.linkedin.com/in/fan-lucas-wu/)，发布于 2025 年 12 月前后 |
| 「由来自顶级 AI 实验室的前高管创办，在大语言模型、上下文工程和多智能体系统方面有深厚积累」 | [Lucas Wu 的 MachinePulse 职位描述](https://www.linkedin.com/in/fan-lucas-wu/details/experience/) |
| 「与有字节跳动背景的资深从业者并肩工作」并获得指导；「可直接接触创始团队」 | [jobs API](https://join.machinepulse.ai/api/jobs) |

两位列出过往雇主的管理层主页都指向字节跳动：Leah Wang 任 Strategic Product Manager 至 2025 年 11 月，Nanqun Chen 任高级产品经理至 2024 年 2 月。

---

## 融资

公司、任何投资方以及查到的任何媒体报道都没有公布过融资轮次（检索于 2026-07-29）。

这条融资表述出现了两次，都在公司自己的招聘文案里。[招聘页面](https://join.machinepulse.ai/)（无日期，访问于 2026-07-29）称 MachinePulse 是一家「global AI startup」，「backed by top-tier USD funds, valued at nearly $100 million」。[Senior Manager, Commercial Operations 岗位描述](https://join.machinepulse.ai/api/jobs)（创建于 2026-05-10）重复为「a global AI startup backed by top-tier USD funds, with a valuation approaching $100 million」，并在待遇部分写「Backed by premier USD funds with a valuation approaching $100M and meaningful equity upside」。

第三处表述性质不同，在 [LinkedIn 公司简介页](https://www.linkedin.com/company/machinepulseai/about/)上（访问于 2026-07-29）：「We have secured continued backing from top-tier investors, with tens of millions of dollars in funding.」（已获得顶级投资方的持续支持，融资规模达数千万美元。）招聘文案说的是估值，这一处说的是融资额。两者并不矛盾，但没有任何一处同时给出这两个数字，也都没有对应到具体轮次或日期。

任何地方都没有点名投资方。三处表述都没有旁证：新加坡实体在 Crunchbase 和 Tracxn 上都没有条目，也找不到任何提及 MachinePulse 融资的新闻稿、投资方组合页面或报道。商业运营岗位要求候选人具备「创业公司经验或在早期公司（A 轮及更早）工作过」，这描述的是候选人背景，而非公司自身所处阶段。

---

## 工程

### 技术栈与平台

| 项目 | 详情 | 证据类型 |
|---|---|---|
| W2A 协议与 SDK | TypeScript；sensor 以 npm 包分发 | 已确认 —— [仓库](https://github.com/machinepulse-ai) |
| W2A 传输 | stdout、HTTP POST、WebSocket / SSE、自定义 | 已确认 —— [架构文档](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md) |
| W2A 智能体运行时 | Claude Code、Hermes、OpenClaw 插件 | 已确认 —— [README](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/README.md) |
| Shotwright 后端 | Python、FastAPI 0.110+ | 已确认 —— [README](https://github.com/machinepulse-ai/shotwright) |
| Shotwright 前端 | React 18、Node 20+ | 已确认 —— [README](https://github.com/machinepulse-ai/shotwright) |
| Shotwright 运行时 | Windows Containers LTSC 2025、Adobe After Effects 2026、nexrender、GitHub Container Registry | 已确认 —— [README](https://github.com/machinepulse-ai/shotwright) |
| Karpo 交付渠道 | 通过一个美国号码（+1 415 886 0326）走 Apple iMessage | 已确认 —— [工作方式](https://app.karpo.ai/how-it-works) |
| Karpo 消息基础设施 | [Linq](https://linqapp.com/)，一家提供 iMessage、RCS、短信和语音通信 API 的服务商 —— 「Karpo is now live on iMessage through Linq's messaging infrastructure」 | 已确认 —— [Lucas Wu 的 LinkedIn](https://www.linkedin.com/in/fan-lucas-wu/)；并在 [Linq 社区页面](https://linqapp.com/community)得到印证 |
| Karpo Web 站点 | `/scenarios/`、`/city-guides/`、`/explore/` 下的服务端渲染页面 | 已确认 —— [sitemap](https://app.karpo.ai/sitemap.xml) |

以下内容来自[岗位描述](https://join.machinepulse.ai/api/jobs)（访问于 2026-07-29），属于招聘证据，不等于生产环境已在使用。硬性要求的语言可以支撑推断；只出现在加分项里的则不能。

| 项目 | 详情 | 出现位置 |
|---|---|---|
| 后端语言 | Go 和 Python，作为两个描述几乎完全相同的资深岗位并列招聘；另有一个专门面向 Agent 系统的 Golang 岗位 | 硬性要求 |
| 数据存储 | PostgreSQL、Redis、消息队列、对象存储 | 硬性要求 |
| 编排与云 | Kubernetes 集群部署与调度；AWS、GCP、Azure 至少其一及其托管服务（ECS、EKS、GKE） | 硬性要求 |
| 基础设施工具 | Terraform、Ansible、Prometheus/Grafana、CI/CD 流水线、灰度发布与回滚 | 硬性要求 |
| 服务网格 | Istio，在流量与网络治理工作中作为示例点名 | 硬性要求（作为示例） |
| 可观测性 | 日志、指标、分布式追踪；容量规划与故障演练 | 硬性要求 |
| ML 训练栈 | PyTorch；HuggingFace、DeepSpeed、Megatron 至少其一；SFT、DPO、GRPO、PPO、奖励建模、知识蒸馏 | 硬性要求 |
| iOS 客户端 | Swift 配合 UIKit 和/或 SwiftUI；MVC/MVVM；Swift Package Manager、Tuist 或 CocoaPods；App Store 与 TestFlight 分发 | 硬性要求 / 加分项 |
| Web 前端 | JavaScript/TypeScript、HTML5、CSS3、React 或 Vue | 硬性要求（实习岗） |
| Agent 管道 | MCP 协议管道开发、prompt 工程、工具调用、上下文管理 | 硬性要求（实习岗） |
| 检索 | 向量数据库与检索框架；召回优化、排序、评估 | 仅加分项 |
| 多云 | 混合云、多地域多集群 Kubernetes 网络治理 | 仅加分项 |

由此可以得出两条其他资料没有确立的事实。公司有**自研的 LLM 后训练工作** —— ML Algorithm Engineer 岗位涵盖对齐与蒸馏，把大模型的推理与偏好能力迁移到小模型上，用于「意图识别、个性化回复生成和数字人格」—— 所以 MachinePulse 并非纯粹调用第三方模型 API。以及公司在做**原生 iOS 客户端**，这一点产品页面上没有提过。

在面向产品的资料中，没有任何一处点名 Karpo 使用的模型供应商或云厂商。Karpo 和 MachinePulse 都没有发布安全页面、子处理方清单或数据留存政策；`app.karpo.ai/terms` 和 `app.karpo.ai/privacy` 在 2026-07-29 抓取时都返回 HTTP 404，尽管 Karpo 落地页上有指向服务条款和隐私声明的链接。

### 系统

| 系统 | 功能 | 来源 |
|---|---|---|
| Karpo 对话式推荐 | 把模糊意图收敛成少量选项，在对话中学习偏好，按需生成行程；支持一对一和群聊 | [工作方式](https://app.karpo.ai/how-it-works)、[FAQ](https://app.karpo.ai/faqs) |
| Karpo 内容生成流水线 | 六个城市下 5,520 个 `/scenarios/` 页面，加上城市指南和按场所的 `/explore/experience/` 页面，多数时间戳为 2026-07-18 | [sitemap](https://app.karpo.ai/sitemap.xml) |
| W2A sensor 运行时 | 以 npm 包形式轮询外部数据源，通过可插拔传输发出符合 schema 的信号 | [架构文档](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md) |
| SensorHub 注册表 | 已发布 sensor 的目录，带下载量，由 postpublish CLI 自动注册 | [SensorHub](https://world2agent.ai/hub)、[notify-hub 仓库](https://github.com/machinepulse-ai/world2agent-notify-hub) |
| Shotwright AE 运行时 | 容器化的 After Effects，由智能体编写的 JSX 驱动，nexrender 无头渲染，成片以 mp4 流回 | [README](https://github.com/machinepulse-ai/shotwright) |

### 招聘所需技术背景

据[岗位描述](https://join.machinepulse.ai/api/jobs)（访问于 2026-07-29），候选人被期待具备的既往问题经验：

- **后端（Go / Python，资深）：**生产环境的并发与性能调优；一致性保证、缓存策略、限流与降级；灰度发布、回滚、服务指标解读与容量规划。加分：生产级 AI 应用、检索与排序评估。
- **后端（Go，Agent 方向）：**设计复杂业务系统并在可靠性、性能、成本与交付速度之间做权衡；工具接入、权限控制、任务状态管理、异常处理与分阶段发布。加分：工作流引擎、任务平台、故障管理。
- **基础设施（SRE）：**3–5 年基础设施或运维经验；Kubernetes 部署、管理与调度；流量调度与网络治理；推动 IaC 落地。加分：云架构师认证、服务网格落地、开源贡献。
- **ML（后训练）：**硕士及以上；Transformer 与 GPT 类架构；后训练与对齐的实操经验；把大模型能力迁移到小模型并上线。加分：对 LLaMA、Qwen、InternLM、Mistral、vLLM 或对齐工具链的贡献；论文发表；算法竞赛背景（AMC、ICPC、NOI、IOI）。
- **产品与内容岗位：**反复要求有真实的 LLM 项目实操 —— Agent Content 岗位明确排除经验仅停留在「把 ChatGPT 当日常工具用」的候选人 —— 以及对西方（主要是纽约/洛杉矶）或日韩生活方式的跨文化理解。

### 工作条件

招聘站的岗位列表由客户端从 `https://join.machinepulse.ai/api/jobs` 加载；服务端返回的 HTML 里只有申请表单，因此不执行 JavaScript 的工具看不到这些岗位。截至 2026-07-29，该接口返回 20 个岗位，全部标记为在招：12 个全职、8 个实习，分布在研发（8）、产品与增长（10）、行政（1），另有 1 个未设部门。创建时间集中在 2026-01-29（15 个），此后陆续新增于 2026-01-30、2026-02-04、2026-03-01、2026-05-10 和 2026-07-25。

| 项目 | 详情 | 来源 |
|---|---|---|
| 在招岗位 | 20 个：12 个全职、8 个实习 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 工作地点 | 18 个标注上海，1 个纽约（Senior Backend Engineer, Go），2 个未设；所有岗位可选新加坡 / 上海 / 纽约 / 加州湾区 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 工作语言 | 没有公司层面的明确政策。岗位以英文撰写；多个产品岗位要求「英语为工作语言」；申请材料鼓励附小红书、抖音、B 站链接，申请表单有微信号字段 | [jobs API](https://join.machinepulse.ai/api/jobs)、[申请表单](https://join.machinepulse.ai/) |
| 远程政策 | UI/UX Designer 岗位提供「弹性工作安排和阶段性远程」；实习要求每周至少 4 天到岗 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 股权 | 「有竞争力的薪资、绩效奖金和股权激励」（设计、产品岗）；「创始团队席位」和「可观的股权上行空间」（商业运营岗） | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 薪资 | 所有岗位均未公布 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 实习 | 20 个岗位中占 8 个；3–6 个月，表现优异可转正；其中一个后端实习限定 2026/2027 届 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 自述文化 | 「扁平」「无层级」「决策链极短」「可直接接触创始团队」；鼓励使用 AI 编程工具并提供「充足的 token 支持」 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 投递方式 | `ahr@machinepulse.ai`（全职）或 `intern@machinepulse.ai`（实习），主题写明岗位；或站内表单。部分岗位邀请提交 1–3 分钟视频自荐和社交主页链接 | [申请表单](https://join.machinepulse.ai/)、[jobs API](https://join.machinepulse.ai/api/jobs) |
| 面试流程 | 除商业运营岗提到节奏快、不确定性高外没有描述；未公布面试轮次 | [jobs API](https://join.machinepulse.ai/api/jobs) |
| 签证、福利、流动率 | 未公布 | [jobs API](https://join.machinepulse.ai/api/jobs) |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-29）：machinepulse.ai 及其上全部链接；用浏览器渲染 join.machinepulse.ai，并读取其 `/api/jobs` 接口和全部 20 条岗位记录；world2agent.ai 含 SensorHub；app.karpo.ai 含完整 sitemap、FAQ、关于、工作方式和 buzz 页面；通过 REST API 查询 GitHub 组织、其六个仓库及成员页面；world2agent 的 README 和架构文档；Shotwright 的 README；以中英文检索「MachinePulse」「MachinePulse Pte」「Karpo」「Karpo AI」「World2Agent」；在已登录的浏览器会话中读取 LinkedIn 公司页及其简介、招聘标签页，以及三位管理层的主页和完整履历页；Crunchbase、Tracxn 和 GetLatka；uspto.report 商标检索结果；以及检索 Karpo 的 App Store 条目。

- 在公司自己掌控的任何界面上 —— 官网、招聘页、产品页、仓库、新闻稿 —— 都没有点出创始人或高管。`创始人`一节中的姓名全部来自个人 LinkedIn 主页，而这些主页在未登录状态下无法读取。所有站点都没有团队页面。
- 没有找到任何融资轮次、投资方、估值日期，也没有任何数据库条目能佐证公司三处自述的融资表述。
- 没有取得办公地址、注册号或 ACRA 记录。新加坡注册地是由「Pte. Ltd.」后缀推断的，未与登记机关核对；未执行 BizFile 实体查询。
- 任何产品都没有已公开的收入模式。
- `app.karpo.ai/terms` 和 `app.karpo.ai/privacy` 虽被落地页链接，但都返回 HTTP 404。Karpo 和 MachinePulse 都没有发布安全页面、子处理方清单、数据留存说明或任何认证。
- 没有点名任何模型供应商。云厂商只被 SRE 岗位收窄到「AWS、GCP 或 Azure」，并未说明实际使用哪一家。
- 20 个岗位都没有公布薪资区间，也没有找到签证、福利或人员流动率信息。
- 没有任何一个具名个人被对应到某个招聘岗位、部门或汇报关系上；岗位描述提到「创始团队」但从不点名。
- 没有找到主流科技媒体的报道 —— 唯一找到的新闻是 2026-07-28 的一篇稿件，经 openPR 分发并被一批聚合站点转载，此外只有一篇关于 World2Agent 的中文博客。
- GitHub 组织没有公开成员，因此无法据此识别具体贡献者。
- Leah Wang 和 Nanqun Chen 的主页都没有填写教育经历，也没有任何一份主页写明公司的成立时间。
- **没有找到任何关于具名创始人的独立报道。**2026-07-29 以中英文检索「Leah Wang」+ MachinePulse、「Nanqun Chen」/ 陈南群 + 阶跃星辰 及 + MachinePulse、「Nanqun Chen」+ Silot/Kaya、Heychat + 小贝文化科技，以及 MachinePulse/Karpo + 创始人 / founder / interview / podcast，都没有返回关于他们任何一人的专访、人物报道或新闻。2026 年关于字节系创业做 AI 的中文盘点文章里也没有提到 MachinePulse。所有新闻材料中唯一被引用的员工是增长负责人，出自 2026-07-28 那一篇稿件。

### 不同来源之间的不一致

- **是哪一个 MachinePulse：**[Crunchbase](https://www.crunchbase.com/organization/machinepulse)、[Tracxn](https://tracxn.com/d/companies/machine-pulse/__T2EbVVSjXHxNVi2tptAU2PdQE2I7bYoG-0V2Qt1iFD8) 和 [GetLatka](https://getlatka.com/companies/machinepulse) 对「MachinePulse」返回的是孟买那家无关的工业物联网公司。它们的创始人、收入、人数和融资状态字段都不描述新加坡实体。
- **创始人来自哪里：**[LinkedIn 公司页](https://www.linkedin.com/company/machinepulseai/about/)写 TikTok、Amazon、PayPal、Keeta；一位[创始成员的动态](https://www.linkedin.com/in/fan-lucas-wu/)写「前 TikTok 产品负责人」；他的[职位描述](https://www.linkedin.com/in/fan-lucas-wu/details/experience/)写「来自顶级 AI 实验室的前高管」；[岗位描述](https://join.machinepulse.ai/api/jobs)写字节跳动。TikTok 和字节跳动是同一集团，但「顶级 AI 实验室」是另一种说法，而且没有任何一处点名到人。
- **Nanqun Chen 的当前任职：**他的[主页](https://www.linkedin.com/in/nanqunchen/details/experience/)把阶跃星辰 Lead Product Manager 列为 2024 年 4 月至今，与 2025 年 12 月至今的 MachinePulse 联合创始人并列（访问于 2026-07-29）。是否只是某一条没有结束标注，从主页上无法判断。
- **成立时间：**三位管理层主页把各自的 MachinePulse 职位起点标在 2025 年 12 月和 2026 年 1 月，GitHub 组织创建于 2025-11-11；没有任何一处说明公司本身何时成立或注册。
- **国别与实际运营重心：**一条[第三方社交帖](https://www.threads.com/@buzz.indica/post/DV8UQrGERU1/us-based-startup-machine-pulses-ai-agent-karpo-has-started-offering-to-pay)把 MachinePulse 说成「US-based」；法律实体是新加坡 Pte. Ltd.，[GitHub 组织](https://github.com/machinepulse-ai)标注新加坡；而 20 个在招岗位中有 18 个定位在上海（[jobs API](https://join.machinepulse.ai/api/jobs)）。三个来源指向三个国家 —— 单独看都不算错，但只有招聘数据能说明活儿实际在哪里干。
- **Karpo 的形态：**[2026-07-28 新闻稿](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html)称 Karpo「available on App and iMessage」，但公司自己的[对比页面](https://app.karpo.ai/scenarios/karpo-vs-gemini-best-ai-city-assistant-nyc-2026)写的正相反 ——「Karpo does not have its own app icon. It is an iMessage extension」—— [FAQ](https://app.karpo.ai/faqs) 和[工作方式](https://app.karpo.ai/how-it-works)页面也只描述了 iMessage 路径，且找不到 App Store 条目。一个涵盖 Swift、App Store 提审和 TestFlight 分发的 [iOS 开发实习岗位](https://join.machinepulse.ai/api/jobs)表明原生客户端正在开发中。以公司自身产品页面的分量看，目前并没有 App，新闻稿的说法夸大了。
- **Karpo 的能力：**[工作方式页面](https://app.karpo.ai/how-it-works)用的是设想式措辞来描述订票、订行程和「life admin」，而[新闻稿](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html)则把四家具名合作方的集成预订说成已经上线。

### 其他

- 三个产品几乎没有共同点：一个消费级生活助手、一个智能体基础设施协议、一个视频制作智能体。公司自己陈述的唯一共同线索是「主动式」智能体（[官网](https://www.machinepulse.ai/)、[招聘页面](https://join.machinepulse.ai/)）。
- Karpo 的公开 Web 站点绝大部分是程序化生成的：5,847 个 sitemap URL 中有 5,520 个是 `/scenarios/` 页面，很多挂靠在新闻事件和名人姓名上，时间戳集中在 2026-07-18（[sitemap](https://app.karpo.ai/sitemap.xml)）。
- 2026-07-28 那篇稿件经 [openPR](https://www.openpr.com/news/4589478/karpo-crosses-half-a-million-personalized-recommendations) 分发，并被大量近乎相同的地方新闻聚合域名原样转载。这是一篇稿件，不是多家独立报道。
- 一条[第三方社交帖](https://www.threads.com/@buzz.indica/post/DV8UQrGERU1/us-based-startup-machine-pulses-ai-agent-karpo-has-started-offering-to-pay)称 Karpo 会在觉得用户的计划有意思时，赞助其外出消费、每人最高 300 美元。没有找到公司自己发布的这个活动的出处。
- World2Agent 全部代码为 Apache 2.0，Shotwright 为 MIT；协议、SDK、插件、示例 sensor 和注册表 CLI 都公开发布。
- 招聘信息是这家公司信息密度最高的公开来源，且远超其他 —— 它确立了实际办公地点、技术栈、自研后训练团队和未发布 iOS 客户端的存在，以及商业方向，而这些在任何产品页面或新闻稿上都看不到。同时它在不执行 JavaScript 的情况下不可见，因为页面是从 `/api/jobs` 客户端渲染的。
- 招聘明显偏向市场侧：20 个岗位中 10 个属于产品与增长，且多数是海外社媒、达人营销、投放和增长，研发只有 8 个（[jobs API](https://join.machinepulse.ai/api/jobs)）。
- LinkedIn 上还有一条招聘线，不在招聘站的接口里：一位创始成员发布了纽约现场办公的 Partnership Development Manager、Social Media & Community Operations 和 Community & Events Operations 岗位（[Lucas Wu 的 LinkedIn](https://www.linkedin.com/in/fan-lucas-wu/)；访问于 2026-07-29）。而 `/api/jobs` 里只有一个纽约岗位。
- 一位创始成员称 Karpo 是「iMessage 上增长最快的应用之一」（[LinkedIn](https://www.linkedin.com/in/fan-lucas-wu/)）；这是公司方说法，没有给出支撑数字。
- 公司跑在自己无法掌控的第三方消息基础设施上：Karpo 的整条交付链路依赖 [Linq](https://linqapp.com/)，再往下依赖 Apple 的 iMessage。

---

## 资料来源

**官方**

- [MachinePulse —— 公司官网](https://www.machinepulse.ai/)
- [招聘](https://join.machinepulse.ai/) · [jobs API —— 页面渲染所用的 20 条岗位记录](https://join.machinepulse.ai/api/jobs)
- [LinkedIn](https://www.linkedin.com/company/machinepulseai/about/)
- [X —— @MachinePulse_AI](https://x.com/MachinePulse_AI)
- Karpo
  - [Karpo 首页](https://app.karpo.ai/)
  - [关于我们](https://app.karpo.ai/about-us)
  - [工作方式](https://app.karpo.ai/how-it-works)
  - [FAQ](https://app.karpo.ai/faqs)
  - [Buzz](https://app.karpo.ai/buzz)
  - [Sitemap](https://app.karpo.ai/sitemap.xml)
  - [X —— @Karpo_AI](https://x.com/Karpo_AI) · [Instagram](https://www.instagram.com/karpo.ai)
- World2Agent
  - [world2agent.ai](https://world2agent.ai/) · [SensorHub](https://world2agent.ai/hub)
  - [GitHub —— world2agent](https://github.com/machinepulse-ai/world2agent) · [README](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/README.md) · [架构文档](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md)
  - [GitHub —— notify-hub](https://github.com/machinepulse-ai/world2agent-notify-hub)
  - [Discord](https://discord.gg/hDjaD8pX)
- [GitHub 组织](https://github.com/machinepulse-ai) · [成员页面](https://github.com/orgs/machinepulse-ai/people)
- [GitHub —— Shotwright](https://github.com/machinepulse-ai/shotwright)

**新闻稿**

- [Karpo 发布 80 天内推荐量突破 50 万 —— 2026-07-28](https://www.openpr.com/news/4589478/karpo-crosses-half-a-million-personalized-recommendations) · [含全文的转载版](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html)

**第三方报道与资料**

- [80aj.com —— World2Agent 报道，2026-04-29（中文）](https://www.80aj.com/2026/04/29/ai-agent-realtime-perception/)
- [Threads —— 关于 Karpo 赞助活动的第三方帖子](https://www.threads.com/@buzz.indica/post/DV8UQrGERU1/us-based-startup-machine-pulses-ai-agent-karpo-has-started-offering-to-pay)
- LinkedIn 个人主页（需登录态）：[Leah Wang](https://www.linkedin.com/in/leah-wang-8676903a8/)、[Nanqun Chen](https://www.linkedin.com/in/nanqunchen/)、[Lucas Wu](https://www.linkedin.com/in/fan-lucas-wu/) · 履历页：[Nanqun Chen](https://www.linkedin.com/in/nanqunchen/details/experience/)、[Lucas Wu](https://www.linkedin.com/in/fan-lucas-wu/details/experience/)
- [Linq —— Karpo 在 iMessage 上所依托的消息基础设施](https://linqapp.com/) · [引用 MachinePulse 的社区页面](https://linqapp.com/community)
- 以 Machinepulse Pte. Ltd. 为所有人的 USPTO 商标条目：[KARPO 99653628](https://uspto.report/TM/99653628)、[KARPO 99653232](https://uspto.report/TM/99653232)、[K 99653634](https://uspto.report/TM/99653634)、[MACHINEPULSE 99653745](https://uspto.report/TM/99653745)

**无关的 MachinePulse（印度）资料 —— 列出以防混淆**

- [Crunchbase](https://www.crunchbase.com/organization/machinepulse)
- [Tracxn](https://tracxn.com/d/companies/machine-pulse/__T2EbVVSjXHxNVi2tptAU2PdQE2I7bYoG-0V2Qt1iFD8)
- [GetLatka](https://getlatka.com/companies/machinepulse)
