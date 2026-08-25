# TapNow

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-26。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-26。英文版为原始版本。

## 摘要

TapNow 自称 "Your Creative OS" —— 一个以 agent 驱动、以无限画布为形态的创作工作空间，"orchestrate[s] text, image, audio, and video models"，以网页应用和 macOS 桌面端交付（[官网](https://www.tapnow.ai/)、[下载页](https://www.tapnow.ai/download)；访问于 2026-08-26）。缔约主体是 `Tamar AI Inc.`，"a Delaware corporation that operates the Services under the TapNow brand"（[服务条款](https://www.tapnow.ai/terms-of-service)；最后更新 2025-09-01），而公司自己的招聘页把在招岗位放在 "SHENZHEN · OPEN ROLES" 这个标题下（[招聘页](https://www.tapnow.ai/careers)；访问于 2026-08-26）。

- 该品牌更早的定位有据可查，但已从线上站点移除：一份存档的 `about` 页面把 **Tamar AI** 呈现为 "The World's Leading AI Company for Marketing"、"Leading the E-commerce Revolution through Artificial Intelligence"，并称其已 "empowered thousands of e-commerce sellers"、为 "major corporations, including industry giants like Google and Amazon" 提供技术服务（[Wayback 存档，2025-10-06](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)）。该页面现在渲染的是 404 视图 —— 见 `品牌与法律实体`。
- 未找到这家公司的任何融资公告。融资数据库检索 `TapNow` 返回的是**另一家完全无关的公司** —— 一家 2022 年成立于东京、融资 194 万美元的照片与视频分享应用（[Tracxn](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8)；页面最后更新 2026-08-17）；Mixpanel 的客户案例讲的也是这家 "a social networking app created by Sango Technologies"（[Mixpanel](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/)）。
- 规模数字都出自公司自述且很单薄：负责 TapNow 技术方向的人在招聘帖里写 "TapNow 目前已经拥有上百万用户，日活也保持在不错的水平"（[V2EX](https://www.v2ex.com/t/1230334)）。独立来看，Similarweb 在 2026 年 7 月口径下给 `tapnow.ai` 98.4 万次访问，流量构成为中国 55.31%、美国 17.53%、日本 8.53%（[Similarweb](https://www.similarweb.com/website/tapnow.ai/)）。
- 企业版的说法相当具体："SOC 2 Type 2 with annual penetration testing"、SAML SSO、SCIM 用户provisioning、GDPR 与 CCPA、"AES-256 at rest. TLS 1.2+ in transit"，以及一条训练数据承诺 "Without explicit authorization, non-public customer content is not used to train general-purpose models offered to unrelated third parties"（[企业版页面](https://www.tapnow.ai/enterprise)；访问于 2026-08-26）。
- 工程可从实际加载的应用与公司自己的招聘帖看出：置于 Google Frontend 之后的 Next.js，资源放在 `files.tapnow.art`，打包中含 Sentry 与 Mixpanel，文档站 `docs.tapnow.ai` 默认中文，招聘话术围绕把 agent 当作 "新的生产主体"、以及测试先行的 QA agent 展开（[V2EX](https://www.v2ex.com/t/1232468)）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | TapNow；产品命名为 "Creative OS"，另有配套的社区产品 "TapTV" | [官网](https://www.tapnow.ai/)、[文档](https://docs.tapnow.ai/)、[服务条款](https://www.tapnow.ai/terms-of-service) |
| 缔约主体 | "Tamar AI Inc., a Delaware corporation that operates the Services under the TapNow brand" | [服务条款](https://www.tapnow.ai/terms-of-service)；最后更新 2025-09-01 |
| 公司邮箱域名 | 招聘联系方式给出 `andy.hu@tamaredge.ai`；`tamaredge.ai` 注册于 2023-08-24（NameSilo，注册人隐去），且不提供网站 | [V2EX](https://www.v2ex.com/t/1230334)；WHOIS 读取于 2026-08-26 |
| 团队所在地 | 招聘页写 "SHENZHEN · OPEN ROLES"；一个岗位帖标题为 "Agent 工程师（QA 方向）/ Agentic Quality Engineer｜深圳" | [招聘页](https://www.tapnow.ai/careers)、[V2EX](https://www.v2ex.com/t/1232468) |
| 文件日期 | 服务条款 "Last updated [September 1, 2025]"；隐私政策 "Last Updated: [September 1, 2025]"；AI 生成内容使用与商用许可 "Version 1.1 \| Effective August 6, 2026 \| Last updated August 10, 2026" | [服务条款](https://www.tapnow.ai/terms-of-service)、[隐私政策](https://www.tapnow.ai/privacy-policy)、[内容许可](https://www.tapnow.ai/generated-content-license) |
| 年龄政策 | "You must be at least 18 years old and legally capable of entering into a binding contract. The Services are not directed to children." | [服务条款](https://www.tapnow.ai/terms-of-service) |
| 域名 | `tapnow.ai` 注册于 2025-01-23（GoDaddy，注册人由 Domains By Proxy 隐去，使用 AWS 名称服务器）；`files.tapnow.art` 承载上传资源；`tamaredge.ai` 注册于 2023-08-24 | WHOIS 与响应头读取于 2026-08-26 |
| 站点语言 | 英文（默认）之外还有 `fr`、`ja`、`ko`、`zh` —— sitemap 中共 45 个 URL，覆盖五种语言 | [sitemap](https://www.tapnow.ai/sitemap.xml)；访问于 2026-08-26 |
| 文档 | `docs.tapnow.ai` 跳转到 `/zh/docs`，标题为 "Creative OS 文档"，把 TapNow Creative OS 描述为 "全球首个AI原生创作系统" | [docs.tapnow.ai](https://docs.tapnow.ai/)；访问于 2026-08-26 |
| 桌面端 | "Download for Mac · v0.4.12 · 267 MB" | [下载页](https://www.tapnow.ai/download)；访问于 2026-08-26 |
| 网页端 | `app.tapnow.ai`，标题为 "TapNow \| Your Agentic Creative Canvas" | [app.tapnow.ai](https://app.tapnow.ai/)；访问于 2026-08-26 |
| 作为客户／伙伴展示的 logo | 首页在 "Trusted by the world's leading creative teams" 下预加载阿里巴巴、Google Ads、Google Cloud、TikTok 与 YouTube 的 "trust icons" | 2026-08-26 的[官网](https://www.tapnow.ai/)响应头与页面 |
| 团队、人数、创始人 | 站点上未公布 —— 见 `创始人` | 见 `备注` |

### 品牌与法律实体

| 名称 | 类型 | 状态 | 来源中表述的关系 | 来源 |
|---|---|---|---|---|
| TapNow | 当前公开品牌 | 在线 | 产品本身；条款把 TapNow 定义为 Tamar AI Inc. 运营的品牌 | [服务条款](https://www.tapnow.ai/terms-of-service) |
| Tamar AI Inc. | 法律主体 | 当前 | "a Delaware corporation that operates the Services under the TapNow brand" | [服务条款](https://www.tapnow.ai/terms-of-service) |
| Tamar AI（品牌） | 更早的公司级品牌 | `about` 页面 2026-08-26 返回 404 视图；最后一次抓到实际内容是 2025-10-06 | 被呈现为 "The World's Leading AI Company for Marketing"、"pioneering innovations like TapNow and TapTV" | [Wayback，2025-10-06](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)；2026-08-26 读取的站点文案包 |
| Tamar Edge | 出现在公司招聘邮箱域名（`tamaredge.ai`）中的名称 | 域名注册于 2023-08-24；不提供网站 | 没有任何公司页面解释它与 Tamar AI Inc. 的关系 | [V2EX](https://www.v2ex.com/t/1230334)；WHOIS 读取于 2026-08-26 |
| TapTV | 产品／社区品牌 | 在线，条款与招聘帖中均有提及 | "the TapTV community"；被描述为 "面向内容消费与创作者连接的新产品方向" | [服务条款](https://www.tapnow.ai/terms-of-service)、[V2EX](https://www.v2ex.com/t/1230334) |
| TapNow（Sango Technologies） | 产品同名的无关公司 | 另一家公司 | 一家 2022 年成立于东京的照片与视频分享社交应用；融资数据库与厂商案例检索 "TapNow" 时返回的是它 | [Tracxn](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8)、[Mixpanel](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/) |
| tamar.ai | 无关站点 | 在线 | 一个阿联酋企业税合规站点；未发现任何关联 | [tamar.ai](https://tamar.ai/)；访问于 2026-08-26 |

站点自身的多语言文案包里，仍然保留着那个被移除页面的元数据 —— "Tamar AI｜The World's Leading AI Company for Marketing"，以及招聘页标题 "Join the World's Leading AI Company for Marketing and Ecommerce" —— 尽管两个页面现在都渲染 404 视图（[页面源码存档，2026-04-27](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about)）。未取得 Tamar AI Inc. 的任何登记文件；尽管在深圳招人，也没有任何公司页面点名中国或香港的运营主体 —— 见 `备注`。

---

## 产品

官网写道："TapNow is the best way to create with AI Agents. Orchestrate text, image, audio, and video models. Zero friction."（[官网](https://www.tapnow.ai/)；访问于 2026-08-26）。条款把服务描述为 "online creative tools for managing materials, organizing and editing content, collaborating on projects, generating or transforming content using artificial intelligence"（[服务条款](https://www.tapnow.ai/terms-of-service)）。

### 产品形态

| 形态 | 是什么 | 来源 |
|---|---|---|
| 网页应用 | `app.tapnow.ai`，"Your Agentic Creative Canvas" | [app.tapnow.ai](https://app.tapnow.ai/) |
| 桌面应用 | "Your Creative OS now on desktop … Bring TapNow to your desktop, and connect it to your local creative files"；macOS，v0.4.12，267 MB；经授权后读取本地项目文件夹 | [下载页](https://www.tapnow.ai/download) |
| 文档 | `docs.tapnow.ai`，默认中文，"Creative OS 文档" | [docs.tapnow.ai](https://docs.tapnow.ai/) |
| TapTV | 条款中提及、招聘帖中被描述为面向内容消费与创作者连接的 "新产品方向" 的社区产品 | [服务条款](https://www.tapnow.ai/terms-of-service)、[V2EX](https://www.v2ex.com/t/1230334) |
| 企业版 | "Creative OS for Teams"，含工作区、成员、共享额度与用量管理；通过 "Contact sales" 销售 | [企业版页面](https://www.tapnow.ai/enterprise) |
| 宣言 | 一份关于产品概念模型的书面表述，标注 "WRITTEN IN AUTUMN 2025" | [宣言页](https://www.tapnow.ai/manifesto) |

### 页面所描述的画布模型

宣言定义了产品的词汇表："Node is the Vocabulary, the atom of your idea. Wire is the Logic, the flow of your thoughts. Group is the Phrase, crystallizing know-how into reusable Chapters. Canvas is the Universe—an infinite space"（[宣言页](https://www.tapnow.ai/manifesto)；写于 2025 年秋）。它把问题界定为想象与创作之间的 "Friction"，并主张一种角色消融的 "Skillset Collapse"："We serve Intent, not Identity."。

下载页与招聘帖补充了实际工作面：技能（"Skill Creator"、"Manage skill"）、插件、flow 文件夹、分镜规划；QA 岗位帖中则把 "画布、节点、3D 节点与 Playlist" 描述为人与 agent 共同创作的 Workspace（[下载页](https://www.tapnow.ai/download)、[V2EX](https://www.v2ex.com/t/1232468)）。产品示意图中可见的模型名称包括 "Banana Pro"、"Seedance Prompt Copilot" 与 "Sonnet 5"（[下载页](https://www.tapnow.ai/download)；读取于 2026-08-26）。

### 商业化

| 项目 | 内容 | 来源 |
|---|---|---|
| 套餐档位 | 定价页的载荷中出现 Free、Pro、Team 与 Enterprise 四档；金额由客户端渲染，服务端返回的 HTML 中没有 | [定价页](https://www.tapnow.ai/pricing)；检查于 2026-08-26 |
| 额度 | 企业管理涵盖 "Credits — Allocate shared credits where they are needed" 与 "Usage — See activity across the organization" | [企业版页面](https://www.tapnow.ai/enterprise) |
| 企业销售 | "Contact sales"；没有公开价目表、起订门槛或合同期限 | [企业版页面](https://www.tapnow.ai/enterprise) |
| 商用许可 | 单独的 "AI Generated Content Use and Commercial License" 授予用户在全球范围内非独占地 "copy, edit, adapt, publish, distribute, display, and commercially monetize the relevant generated content"，且 "no separate license fee … for the uses listed in the project license certificate" | [内容许可](https://www.tapnow.ai/generated-content-license)；v1.1，2026-08-06 生效 |
| 项目许可证书 | TapNow "may issue a project license certificate for eligible projects and specific exported files"，记录模型／API 版本、生成时间、导出文件、许可范围、标识状态与当前状态；并明确 "not a copyright registration certificate or a guarantee of third-party rights" | [内容许可](https://www.tapnow.ai/generated-content-license) |
| 许可边界 | 该许可 "does not authorize independent sublicensing, resale, stock-library distribution, model training or improvement, incorporation into a product or API, or continued use outside that project" | [内容许可](https://www.tapnow.ai/generated-content-license) |
| AI 标识 | "Where applicable law requires labeling, TapNow will add the required explicit and implicit labels"；用户不得删除或伪造；"TapNow will retain recipient information and related logs for at least six months" | [内容许可](https://www.tapnow.ai/generated-content-license) |

### 公开披露的规模变化

| 日期 | 数字或事件 | 来源 |
|---|---|---|
| 2023-08-24 | `tamaredge.ai` 域名注册 | WHOIS 读取于 2026-08-26 |
| 2025-01-23 | `tapnow.ai` 域名注册 | WHOIS 读取于 2026-08-26 |
| 2025-09-01 | 服务条款与隐私政策最后更新，署名 Tamar AI Inc. | [服务条款](https://www.tapnow.ai/terms-of-service)、[隐私政策](https://www.tapnow.ai/privacy-policy) |
| 2025-10-06 | 存档的 `about` 页面把 Tamar AI 呈现为一家电商营销 AI 公司，称已 "empowered thousands of e-commerce sellers" | [Wayback](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about) |
| 2025 年秋 | 撰写 TapNow 宣言 | [宣言页](https://www.tapnow.ai/manifesto) |
| 2026-04-27 | 存档抓取显示 `about` 页面已渲染 404 视图 | [Wayback](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about) |
| 2026-08-06／2026-08-10 | AI 生成内容使用与商用许可 v1.1 生效并更新 | [内容许可](https://www.tapnow.ai/generated-content-license) |
| 无日期的招聘帖 | "TapNow 目前已经拥有上百万用户，日活也保持在不错的水平"；并提到与影视飓风合作的 AI 入门课程 | [V2EX](https://www.v2ex.com/t/1230334) |
| 2026 年 7 月口径 | Similarweb：98.4 万次访问，全球排名 #55,436，中国区排名 #3,492，Social Media Networks 类目 #514，跳出率 36.33%，每次访问 3.35 页，平均停留 3 分 11 秒；中国 55.31%、美国 17.53%、日本 8.53%、香港 5.06%、新加坡 3.72%；直接流量 62.63% | [Similarweb](https://www.similarweb.com/website/tapnow.ai/) |
| 访问于 2026-08-26 | 桌面端版本 v0.4.12（267 MB） | [下载页](https://www.tapnow.ai/download) |

公司没有公布任何营收、订阅、付费席位或生成量数字。

### 公开项目与合作方

企业版页面列出三个具名的公开项目："TapNow × Kaadas —— AI Smart Lock Creative Challenge"、"Lenovo AI × TapNow —— World Cup AI Creation Competition"、"Happy Horse × Alibaba Cloud × TapNow —— AI Music Video Competition"（[企业版页面](https://www.tapnow.ai/enterprise)；访问于 2026-08-26）。首页在 "Trusted by the world's leading creative teams" 下展示阿里巴巴、Google Ads、Google Cloud、TikTok 与 YouTube 的 logo 图标；没有任何页面说明这些标识代表客户、集成还是投放渠道 —— 见 `备注`。

### 安全与管理方面的说法

企业版页面写道："Training data protection — Without explicit authorization, non-public customer content is not used to train general-purpose models offered to unrelated third parties"；"Identity management — Secure access with SAML SSO"；"SCIM user provisioning"；"Global compliance — Meet GDPR and CCPA requirements"；"Third-party certified — SOC 2 Type 2 with annual penetration testing"；以及 "Data protection — AES-256 at rest. TLS 1.2+ in transit"（[企业版页面](https://www.tapnow.ai/enterprise)；访问于 2026-08-26）。没有公布证书编号、审计机构、审计期间或信任门户。

---

## 创始人

`www.tapnow.ai` 上不存在创始人、高管或团队页面；招聘页只把公司描述为 "a small, focused team spanning product, design, engineering, and content"（[招聘页](https://www.tapnow.ai/careers)；访问于 2026-08-26）。

从一手来源能识别出的唯一个人是公司招聘帖的作者，他自我介绍为 "老胡，目前负责 TapNow 的技术方向"，并给出联系邮箱 `andy.hu@tamaredge.ai`（[V2EX](https://www.v2ex.com/t/1230334)；访问于 2026-08-26）。没有公布职位、履历或任职经历。

第三方 AI 生成的聚合页面还流传着关于 TapNow 的其他人名与一套中国公司架构。这些内容无法追溯到任何备案、公司页面或具名记者，因此本页不予转述 —— 见 `备注`。

招聘页倒是描述了四段式的招聘流程："Get to know each other"、"Work through a real problem"、"Meet the team"、"Decide together"，以及三条原则 —— "Stay at the frontier"、"Own the whole problem"、"Be direct, build fast"（[招聘页](https://www.tapnow.ai/careers)）。

---

## 融资

截至 2026-08-26，在所查阅的公开来源中未找到这家公司的任何融资公告。`tapnow.ai` 上没有新闻页、投资人页或融资表述，条款与已存档的公司定位中也都没有提到投资方。

| 来源 | 它描述的是什么 | 为什么不适用 |
|---|---|---|
| [Tracxn —— "TapNow"](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8)（页面最后更新 2026-08-17） | "TapNow has raised a total funding of $1.94M over 1 round. Its latest funding round was a Series A round on Oct 16, 2023"，成立于 2022 年，总部东京，投资方 SBI Investment 与 DIMENSION | 该档案描述的是一款 "photos and videos with friends" 分享应用、总部在东京 —— 与注册在特拉华、团队在深圳的 `tapnow.ai` 创作画布公司不是一家 |
| [Mixpanel 客户案例](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/) | "a social networking app created by Sango Technologies"，200 万用户，CEO Yuma Noma，留存提升 50% | 同一家东京公司；这些指标属于它，而不属于 `tapnow.ai` |

`tapnow.ai` 的融资金额、轮次、投资方与估值，在所查阅的任何来源中都未确立。

---

## 工程

### 技术栈与平台

公司未发布技术栈说明页。以下条目均由实际加载的应用、其资源以及公司自己的招聘帖确认（均观察于 2026-08-26）。

- **网页前端：** Next.js App Router（`x-powered-by: Next.js`、`_next/static` 资源、RSC 相关 vary 头），置于 `Google Frontend` 之后；DNS 托管在 AWS Route 53 名称服务器上，主域同时解析到一个 Vercel 地址（`76.76.21.21`）与一个 Google Cloud 地址。
- **资源域名：** 上传与生成的媒体由 `files.tapnow.art` 的 `/api/conversation/storage/uploads/…` 提供，与营销站点分属不同域名。
- **观测组件：** 页面打包中引用了 Sentry 与 Mixpanel（`api.mixpanel.com`、`api-js.mixpanel.com`）。
- **桌面客户端：** 267 MB 的 macOS 构建（v0.4.12），经授权读取本地文件夹，并提供插件、技能与附件；下载页展示其读取 `~/Creative/Projects/…` 并引用 `.psd`、`.fig`、`.mp4`、`.pdf` 等资源。
- **文档与多语言：** 文档默认中文（`docs.tapnow.ai/zh/docs`），而营销站点默认英文，并提供 `fr`、`ja`、`ko`、`zh` 版本。
- **模型编排：** 产品被描述为编排 "text, image, audio, and video models"；界面示意图中出现 "Banana Pro"、"Seedance Prompt Copilot" 与 "Sonnet 5"，但没有任何页面说明生产环境使用哪些供应商。
- **数据流向（一手表述）：** "Our Services may transmit prompts, files, or other necessary content to cloud providers, model providers, and other technical service providers that help us perform the requested operation"（[隐私政策](https://www.tapnow.ai/privacy-policy)）。
- **没有公开代码：** 未找到该品牌名下的 GitHub 组织或包仓库存在。

### 系统

| 系统 | 做什么 | 来源 |
|---|---|---|
| Agent 画布 | 以节点、连线、分组与无限画布作为人与 agent 的共享工作空间，并含 3D 节点与 Playlist | [宣言页](https://www.tapnow.ai/manifesto)、[V2EX](https://www.v2ex.com/t/1232468) |
| 多模型编排 | 把一个创作任务在文本、图像、音频与视频模型之间路由 | [官网](https://www.tapnow.ai/) |
| 技能与插件 | 用户自建"技能"，配有 Skill Creator 与管理界面，另有插件体系 | [下载页](https://www.tapnow.ai/download) |
| 本地文件桥接 | 桌面端经授权读取本地项目文件夹，并把它们作为上下文带入画布 | [下载页](https://www.tapnow.ai/download) |
| 工作区管理 | 工作区、组织级成员、共享额度分配与用量报表 | [企业版页面](https://www.tapnow.ai/enterprise) |
| 许可认证 | 为导出文件签发并验证项目许可证书，含标识状态与在线验证页面 | [内容许可](https://www.tapnow.ai/generated-content-license) |
| AI 内容标识 | 为产出添加法律要求的显式与隐式标识，并对接收方信息与日志 "retain … for at least six months" | [内容许可](https://www.tapnow.ai/generated-content-license) |
| 内部 agent 工具链 | 公司自述为 "一个完全 AI Native 的团队"，把 agent 视为生产主体，采用测试先行的 QA agent 生成与维护用例，并以 eval 持续检验 | [V2EX](https://www.v2ex.com/t/1232468) |

### 数据处理（依文档记载）

隐私政策写明 Tamar AI Inc. 会收集账号与联系信息，以及 "Customer Content, such as prompts, instructions, uploaded images, video, audio, text, project files, comments, reference materials"；内容可能被传输给 "cloud providers, model providers, and other technical service providers"；关于训练则写道："Unless you provide separate affirmative authorization, TapNow will not use non-public Customer Content to train or improve a general-purpose model offered to unrelated third parties. We may use aggregated or de-identified information and limited controlled evaluation data to improve the functionality, safety, and reliability of the Services"（[隐私政策](https://www.tapnow.ai/privacy-policy)；最后更新 2025-09-01）。

政策还写明 TapNow "does not sell personal information for money"，也不按 CCPA 定义为跨情境行为广告共享个人信息；留存为 "only for as long as reasonably necessary for the purposes described in this Policy"，未给出固定期限；处理可能发生在 "the United States and other countries where we or our providers operate"，跨境传输采用 "contractual, organizational, or other lawful measures"。未点名任何子处理者、云服务商或模型供应商。

### 招聘所需技术背景

公司的公开招聘通过自有招聘页与中文开发者论坛进行。负责 TapNow 技术方向的人发布的招聘帖列出七个在招岗位及人民币月薪区间（[V2EX](https://www.v2ex.com/t/1230334)；访问于 2026-08-26）：

| 岗位 | 区间（人民币／月） |
|---|---|
| 全栈工程师 | 35k–65k |
| 客户端工程师 | 15k–35k |
| 客户端工程师，3D 创作方向 | 20k–65k |
| 后端工程师，Agent 方向 | 20k–40k |
| 后端工程师，AI 产品方向 | 28k–40k |
| Agent 开发工程师，测试方向 | 12k–25k |
| 运维工程师 | 15k–25k |

同一帖把想要的画像归纳为 "原型探索者（Prototyper）"、"建造者（Builder）"、"清道夫（Sweeper）"、"增长者（Grower）"、"维护者（Maintainer）"。QA 岗位帖明确表示不要传统测试工程师："我们不想再招一个亲自做测试的人，而是想招一个让 Agent 学会做测试的人"，并称把 "会写 Playwright 、Pytest" 视为质量工程终点的人不适合这个岗位；工作内容是设计让 agent 生成、扩展、去重与维护测试用例的 harness，并用 eval 持续检验（[V2EX](https://www.v2ex.com/t/1232468)）。

### 行业领域

工作范围涵盖跨多模态生成模型的 agent 编排、无限画布与节点图的交互设计、带本地文件系统集成的桌面客户端、3D 创作，以及企业管理（SSO、SCIM、工作区与额度治理）。同时还有相当重的内容合规面：AI 产出的商用许可、项目许可证书、带六个月日志留存的 AI 内容标识义务，以及 GDPR／CCPA 处理（[内容许可](https://www.tapnow.ai/generated-content-license)、[企业版页面](https://www.tapnow.ai/enterprise)、[隐私政策](https://www.tapnow.ai/privacy-policy)）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | `tapnow.ai/careers`，标题为 "SHENZHEN · OPEN ROLES"；岗位列表本身由客户端渲染 | [招聘页](https://www.tapnow.ai/careers)；访问于 2026-08-26 |
| 地点 | 深圳；有一个岗位帖标题写 "深圳" | [招聘页](https://www.tapnow.ai/careers)、[V2EX](https://www.v2ex.com/t/1232468) |
| 公布的薪资区间 | 七个工程岗位，人民币每月 12k–65k，见公司的 V2EX 招聘帖 | [V2EX](https://www.v2ex.com/t/1230334) |
| 自述文化 | "High standards, High trust"；"We're a small, cross-disciplinary team. We speak plainly, trust one another, and take responsibility for the outcome"；中文帖写 "我们崇尚积极、直接、务实的团队文化" | [招聘页](https://www.tapnow.ai/careers)、[V2EX](https://www.v2ex.com/t/1230334) |
| 招聘流程 | 四个阶段：互相了解、共同解决一个真实问题、与团队见面、共同决定 | [招聘页](https://www.tapnow.ai/careers) |
| 投递渠道 | 招聘页的 "Explore open roles"；V2EX 帖中的微信 `zhidengfacai` 与 `andy.hu@tamaredge.ai` | [招聘页](https://www.tapnow.ai/careers)、[V2EX](https://www.v2ex.com/t/1230334) |
| 人数、福利、远程政策、股权 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-08-26）：`www.tapnow.ai` 首页、`/manifesto`、`/download`、`/enterprise`、`/pricing`、`/careers`、`/terms-of-service`、`/privacy-policy`、`/generated-content-license`、`/community-guidelines`、`robots.txt` 与 `sitemap.xml`（五个语言版本共 45 个 URL）；对 `/about`、`/en/about`、`/contact`、`/blog`、`/news`、`/company` 与 `/legal` 的探测；定价页的 JavaScript 分包与站点的网络请求域名；`app.tapnow.ai`、`docs.tapnow.ai`、`files.tapnow.art`、`api.tapnow.ai` 与 `tamaredge.ai`；`tapnow.ai` 与 `tamaredge.ai` 的 WHOIS；`tapnow.ai`、`/about`、`/en/about`、`/zh/about` 的互联网档案 CDX 索引与带日期抓取；Similarweb；Tracxn；Mixpanel 客户案例；公司的 V2EX 招聘帖；以及针对 TapNow、Tamar AI、Tamar Edge 与相关深圳主体名称的中英文检索。

- **创始人、高管与人数。** 线上站点没有团队页或关于页；只有一个人能通过招聘帖被识别，且未公布职位或履历。
- **公司登记与集团结构。** 未取得 Tamar AI Inc. 的任何备案；也没有任何公司页面解释特拉华主体、`tamaredge.ai` 邮箱域名与深圳团队三者之间的关系。
- **定价。** 套餐名称（Free、Pro、Team、Enterprise）出现在页面载荷里，但金额、额度与计费周期都不在服务端渲染，企业版只有 "Contact sales"。
- **公司口径的任何融资、营收、用户或使用量数字。** 唯一的规模表述是招聘帖里未量化的 "上百万用户"；站点本身什么都没公布。
- **模型与供应商。** 产品编排第三方模型却一个都没在生产环境点名；隐私政策只提到 "model providers"。
- **企业安全说法的证据。** SOC 2 Type 2、渗透测试、SSO、SCIM 与加密都是断言，没有证书编号、审计机构、报告索取路径或信任门户。
- **首页 logo 条的含义。** 阿里巴巴、Google Ads、Google Cloud、TikTok 与 YouTube 以 "trust icons" 出现，但没有任何关于关系的表述。
- **留存期限与子处理者。** 隐私政策未规定固定留存期限，也未点名任何子处理者、云服务商或区域。
- **2026-08-26 无法读取的来源：** 内置浏览器中的 `tapnow.ai`（浏览层拒绝导航，因此本页所有线上事实均来自 HTTP 抓取与存档）；`tamaredge.ai`（无响应）；面向这家公司的 Crunchbase 类数据库（收录的只有东京那家同名 TapNow）。

### 不同来源之间的不一致

- **两家无关公司共用产品名。** 融资数据库与厂商案例检索 "TapNow" 返回的是 Sango Technologies 的东京社交应用 —— 2022 年成立、融资 194 万美元、200 万用户、CEO Yuma Noma（[Tracxn](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8)、[Mixpanel](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/)）。这些数字都不属于 `tapnow.ai`。
- **公司定位变了，而证据被移除。** 2025 年 10 月，站点把 Tamar AI 呈现为服务 "thousands of e-commerce sellers"、并为 "major corporations, including industry giants like Google and Amazon" 提供技术服务的营销与电商 AI 公司（[Wayback](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)）；到 2026 年 4 月，`about` 页面已渲染 404 视图，而站点文案包里仍留着它的旧标题（[Wayback](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about)）。没有任何说明解释这一变化。
- **司法辖区与人员所在地不一致。** 条款把用户绑定到一家特拉华公司，并写明这些条款 "apply to individuals and organizations that access or use the Services in the United States"，而招聘页与招聘帖把团队放在深圳，文档也默认中文（[服务条款](https://www.tapnow.ai/terms-of-service)、[招聘页](https://www.tapnow.ai/careers)、[文档](https://docs.tapnow.ai/)）。
- **"全球首个／全球领先"类说法。** 文档称 Creative OS 是 "全球首个AI原生创作系统"，已存档的关于页称 Tamar AI 是 "The World's Leading AI Company for Marketing"；两处说法在任何页面上都没有出处或定义（[文档](https://docs.tapnow.ai/)、[Wayback](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)）。
- **流量地域与对外定位不一致。** 英文优先的营销站点与特拉华主体，与 Similarweb 给出的 55.31% 中国流量、以及默认中文的文档站并存（[Similarweb](https://www.similarweb.com/website/tapnow.ai/)、[文档](https://docs.tapnow.ai/)）。
- **未经证实的第三方公司档案。** AI 生成的聚合页面断言了 TapNow 具体的中国运营主体、一家香港公司与若干高管姓名。这些都无法追溯到登记、公司页面或具名记者，且同类页面还把两家 TapNow 混为一谈，因此本页不予转述。

### 其他

- **相对于其公开体量，法律文件这一层做得异常完整。** 除常规条款与隐私政策外，公司还发布了带版本号的 "AI Generated Content Use and Commercial License"（v1.1，2026-08-06 生效），引入按项目签发的许可证书、处理 AI 标识义务、承诺至少六个月的接收方日志留存，并写明日文、英文、中文版本冲突时 "the English version prevails"（[内容许可](https://www.tapnow.ai/generated-content-license)）。
- **该许可明确防范追溯性撤销。** 对于在证书有效期内合法生成并导出的内容，"TapNow generally will not retroactively cancel the license listed in the certificate solely because a subscription later expires, a model is later discontinued, or rules generally change"，另有列举的例外情形（[内容许可](https://www.tapnow.ai/generated-content-license)）。
- **公司是围绕 agent 而不是围绕人头在招人。** 其 QA 岗位帖主张 "当 Agent 可以快速完成开发，质量就会成为整个生产系统能否闭环的关键"，要找的是调教 QA agent 的人，而不是跑测试的人（[V2EX](https://www.v2ex.com/t/1232468)）。
- **市场动作以联名项目为主。** 三个具名公开项目分别把 TapNow 与凯迪仕、联想、阿里云绑在一起，招聘帖还提到与大型中文视频制作频道影视飓风的课程合作（[企业版页面](https://www.tapnow.ai/enterprise)、[V2EX](https://www.v2ex.com/t/1230334)）。
- **产品面被拆在三个域名上：** 营销在 `tapnow.ai`，应用在 `app.tapnow.ai`，用户资源在 `files.tapnow.art`（观察于 2026-08-26）。

---

## 资料来源

**官方**

- [官网](https://www.tapnow.ai/) · [宣言](https://www.tapnow.ai/manifesto) · [下载页](https://www.tapnow.ai/download) · [企业版](https://www.tapnow.ai/enterprise) · [定价页](https://www.tapnow.ai/pricing) · [招聘页](https://www.tapnow.ai/careers)
- [服务条款](https://www.tapnow.ai/terms-of-service)（最后更新 2025-09-01） · [隐私政策](https://www.tapnow.ai/privacy-policy)（最后更新 2025-09-01） · [AI 生成内容使用与商用许可](https://www.tapnow.ai/generated-content-license)（v1.1，2026-08-06 生效） · [社区准则](https://www.tapnow.ai/community-guidelines)
- [网页应用](https://app.tapnow.ai/) · [文档（默认中文）](https://docs.tapnow.ai/) · [robots.txt](https://www.tapnow.ai/robots.txt) · [sitemap](https://www.tapnow.ai/sitemap.xml)
- 公司招聘帖 —— [V2EX：TapNow 诚邀各位英雄好汉加入（岗位与薪资区间）](https://www.v2ex.com/t/1230334) · [V2EX：Agent 工程师（QA 方向）](https://www.v2ex.com/t/1232468)
- 已存档的旧定位 —— [Tamar AI 关于页，抓取于 2025-10-06](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about) · [渲染为 404 的关于页，抓取于 2026-04-27](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about)

**第三方档案与同名冲突**

- [Similarweb —— tapnow.ai](https://www.similarweb.com/website/tapnow.ai/)
- [AMZ123 —— Tamar AI 档案，描述 Llamrei 与 Lamta 两款电商产品（中文）](https://www.amz123.com/tamarai/introduction)
- 非本公司 —— [Tracxn —— TapNow（东京照片／视频分享应用）](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8) · [Mixpanel 客户案例 —— Sango Technologies 的 TapNow](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/) · [tamar.ai —— 无关的阿联酋税务合规站点](https://tamar.ai/)
