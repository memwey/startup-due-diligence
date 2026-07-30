# Eazo

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-30。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-30。英文版为原始版本。

## 摘要

Eazo 是一个面向消费者的 AI 应用与 agent 平台，运营主体为 `ASI X Inc.`，一家在特拉华州登记的公司，其网站页脚写着 "Made with ♥︎ in San Francisco"（[官网](https://eazo.ai/)；无日期，访问于 2026-07-30）。它公开了三条产品线：一个用于发现、使用和二次改造（remix）创作者所做 AI 应用的移动 App（[App Store](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137)，首次发布于 2026-03-28）；`Eazo Creator`，一个用于生成并部署这些应用的零代码全栈构建器（[creator.eazo.ai](https://creator.eazo.ai/)；访问于 2026-07-30）；以及 `Eazo Anima`，一个面向开发者的 agent 身份、记忆与网页行动基础设施产品（[anima.eazo.ai](https://anima.eazo.ai/)；访问于 2026-07-30）。同一法律主体 `ASI X Inc.` 也出现在 Fellou 行动型浏览器的法律页面中（[Fellou 服务条款](https://fellou.ai/terms/)、[Fellou 隐私政策](https://fellou.ai/policy/)；生效日 2026-02-01）——见 `品牌与法律实体`。

- 截至 2026-07-30，在所查阅的公开来源中，公司未就 Eazo 或 Fellou 任一品牌公布过任何融资轮次。第三方数据库互相矛盾：据报道 PitchBook 档案称累计融资 4040 万美元、投资方为 LongRiver Investments，而 [Tracxn](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw) 称该公司"Unfunded"（未获融资）——见 `备注`。
- 分发量仍处早期：Google Play 对 `ai.eazo.portal` 显示 "50+ Downloads" 和应用内购买（[Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)；访问于 2026-07-30），App Store 列表显示 15 条评分、均分 4.5（[iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)；访问于 2026-07-30）。
- 公开记录中规模最大的活动是 2026-05-23/24 的 EAZO 全球黑客松，覆盖旧金山（山景城）、纽约、上海以及线上，声明奖池 30 万美元、253 个获奖名额，计分权重为平台用户投票 50%、专家评审 40%、选手互评 10%（[黑客松页面存档，抓取于 2026-05-19](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)）。
- 团队规模未公布。招聘页写着"We're a team across the San Francisco Bay Area and Singapore"，并列出三个岗位——Agent Engineer、Growth、Design Engineer——以及一个人才社区（[招聘页](https://eazo.ai/careers)；无日期，访问于 2026-07-30）。"Yang, Founder & CEO of Eazo" 是站点上唯一具名的人（[关于页](https://eazo.ai/about)）。
- 工程方面的证据来自公开资产而非技术栈说明页：营销站点由 Express 提供服务并置于 Cloudflare 之后，`Eazo Creator` 是置于 nginx 之后的 Vite SPA，`Eazo Anima` 为 Next.js 并配 VitePress 文档，Android APK 通过 CloudFront 从 Amazon S3 分发，`eak.eazo.ai` 位于 AWS 负载均衡器之后（响应头观察于 2026-07-30）。公开的 [eazo-creator-nextjs-template](https://github.com/EazoAI/eazo-creator-nextjs-template) 把应用运行时记录为 Next.js 16 / React 19 / Bun / Drizzle ORM + PostgreSQL，平台 AI "rout[ed] through AWS Bedrock via the Eazo AI gateway"，默认模型为 `deepseek.v3.1`（[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)；访问于 2026-07-30）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | Eazo（页面标题中写作 EAZO） | [官网](https://eazo.ai/)；无日期，访问于 2026-07-30 |
| 法律名称 | ASI X Inc. | [平台服务条款](https://eazo.ai/terms-of-service)；生效日 2026-02-01 |
| 登记地址 | 251 Little Falls Drive, Wilmington, New Castle, DE 19808 | [隐私政策，EEA+ 附录](https://eazo.ai/privacy-policy)；生效日 2026-02-01 |
| 自述出处 | "Made with ♥︎ in San Francisco by ASI X Inc." | [官网页脚](https://eazo.ai/)；无日期，访问于 2026-07-30 |
| 团队所在地 | "a team across the San Francisco Bay Area and Singapore" | [招聘页](https://eazo.ai/careers)；无日期，访问于 2026-07-30 |
| Google Play 上的开发者联系信息 | ASI X Inc，`media@fellou.ai`，251 Little Falls Dr, Wilmington, DE 19808-1674，+1 702-245-1490 | [Google Play "About the developer"](https://play.google.com/store/apps/details?id=ai.eazo.portal)；访问于 2026-07-30 |
| 站点上具名的负责人 | "Yang"，Founder & CEO of Eazo | [关于页](https://eazo.ai/about)；无日期，访问于 2026-07-30 |
| 员工人数 | 未公布 | 见 `备注` |
| 隐私政策覆盖的域名 | `eazo.ai`；`eazo.online` | [隐私政策](https://eazo.ai/privacy-policy)；生效日 2026-02-01 |
| 公开联系方式 | `team@eazo.ai`（联系）、`hi@eazo.ai`（仲裁退出与争议通知）、`privacy@eazo.ai`（数据权利）、`media@eazo.ai`（应用支持） | [官网页脚](https://eazo.ai/)、[服务条款 10.4](https://eazo.ai/terms-of-service)、[隐私政策](https://eazo.ai/privacy-policy)、[Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal) |
| 社区渠道 | Discord、X（`@EazoAI`）、TikTok（`@eazoai`） | [官网页脚](https://eazo.ai/)；无日期，访问于 2026-07-30 |
| iOS 应用 | `ai.eazo.portal`，"Eazo: Discover AI Apps, Agents"，首次发布 2026-03-28，2026-07-29 更新至 0.2.23 版，生活类，12+，仅英文，最低 iOS 16.0，15 条评分均分 4.47 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)；访问于 2026-07-30 |
| Android 应用 | `ai.eazo.portal`，2026-07-28 更新，通讯类，"50+ Downloads"，含应用内购买，Teen 分级 | [Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)；访问于 2026-07-30 |
| APK 直接下载 | `cdn.eazo.ai/mobile/eazo.apk`，211,453,650 字节，`last-modified` 为 2026-06-25 | 响应头观察于 2026-07-30 |
| GitHub 组织 | `EazoAI`，创建于 2026-02-11，5 个公开仓库，无公开成员 | [GitHub API](https://api.github.com/orgs/EazoAI)；访问于 2026-07-30 |
| npm 组织 | `@eazo`，4 个包：`sdk`、`eak`、`auth`、`node-sdk`，均为 MIT | [npm registry 搜索](https://registry.npmjs.org/-/v1/search?text=eazo)；访问于 2026-07-30 |
| 数据传输地区 | "third parties in locations including the United States, Japan and Singapore" | [隐私政策，EEA+ 附录](https://eazo.ai/privacy-policy)；生效日 2026-02-01 |

**活动与合作方**：Eazo 于 2026-05-23/24 举办了 EAZO 全球黑客松。存档的活动页写明上海线下场地为上海创新创意设计研究院（DIIS），虹口区东长治路505号（[存档于 2026-05-19](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)）。旧金山的 Luma 页面把联合主办方列为 "Eazo.ai · Corgi · Streaml · Gen · Photon · AI Valley"，并称活动 "is in partnership with the Gen AI Foundry"，把 Gen Digital 描述为拥有 "trusted consumer brands including Norton, Avast, LifeLock, MoneyLion" 的公司（[Luma，硅谷场](https://luma.com/frw43jmv)；访问于 2026-07-30）。

**公司自述的市场背景**：文章 [You Were Born to Be Powerful（2026-01-26）](https://eazo.ai/blog/you-were-born-to-be-powerful) 把公司定位表述为 "All tech elites are building Agents for elites. We're building Agents for everyone"，把 "deep research reports, data analysis, industry surveys, market insights" 与日常任务对比，并把 Eazo 描述为 "InternetOS, your operating system for the internet"。[关于页](https://eazo.ai/about) 把使命表述为做用户的 "Smart Life Gateway"，愿景为 "Make Agent a way of life"，并列出五条价值观。

### 品牌与法律实体

| 名称 | 类型 | 指向的司法辖区 | 关系 | 来源 |
|---|---|---|---|---|
| Eazo / EAZO | 公开品牌 | — | 站点、应用、文档、npm scope 和 GitHub 组织统一使用的名称 | [官网](https://eazo.ai/) |
| ASI X Inc. | 被列为合同主体与数据控制者的法律实体 | 美国特拉华州（给出了登记地址） | 声明为 Eazo 各项服务的运营方 | [服务条款](https://eazo.ai/terms-of-service)、[隐私政策](https://eazo.ai/privacy-policy) |
| Fellou | 另一个公开品牌（行动型浏览器）以及 `Eko` 框架 | — | Fellou 自己的服务条款和隐私政策把 `ASI X Inc.` 列为同一合同主体与数据控制者，登记地址相同 | [Fellou 服务条款](https://fellou.ai/terms/)、[Fellou 隐私政策](https://fellou.ai/policy/) |
| Eazo Anima / EAK | 产品品牌 | — | 文档写作 "Eazo Anima (EAK)"；`eak.eazo.ai` 跳转至 `anima.eazo.ai` | [Quickstart](https://anima.eazo.ai/docs/guides/quickstart)，跳转观察于 2026-07-30 |
| Eazo Technology Co., Ltd. | LinkedIn 上一家名称相近的公司 | 未确立 | 在所查阅来源中未发现与 ASI X Inc. 的任何关联；此处记录以避免被误认为同一家公司 | [LinkedIn](https://www.linkedin.com/company/eazo-technology) |

Eazo 与 Fellou 的关系有来自双方的一手证据。Fellou 的法律页面写明 `ASI X Inc.` 以及与 Eazo 相同的威尔明顿地址（[Fellou 隐私政策](https://fellou.ai/policy/)）。Google Play 为 Eazo 应用核验过的 "About the developer" 栏把开发者邮箱写为 `media@fellou.ai`（[Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)；访问于 2026-07-30）。四个 `@eazo` npm 包全部由三个注册邮箱为 `zhuowei@fellou.ai`、`liaochangjiang@fellou.ai` 和 `suntianxiang@fellou.ai` 的账号维护（[npm registry](https://registry.npmjs.org/@eazo%2Fsdk)；访问于 2026-07-30）。`@FellouAI` 的 X 账号有一条帖子推广 Eazo 黑客松并 @ 了 `@EazoAI`（[X，2026-05](https://x.com/FellouAI/status/2054356197491273795)）；`x.com` 在 2026-07-30 阻止自动访问，因此该帖文字取自搜索结果标题，未经确认。两个品牌的营销页面互不提及；只有法律页面、应用商店信息和包注册表这些表层把它们连了起来。

`Authing` 与 `GenAuth` 是另一层尚未澄清的关系。Eazo 的身份层命名为 `GenAuth`（[GenAuth 文档](https://anima.eazo.ai/docs/genauth/)），`@eazo/auth` 包自述处理 "Web (GenAuth OIDC/JWT)" 并依赖 `authing-js-sdk`，关键词同时包含 `genauth` 和 `authing`（[npm](https://registry.npmjs.org/@eazo%2Fauth)；访问于 2026-07-30），SDK 变更日志提到 "the Authing OAuth popup"（[CHANGELOG 0.21.0](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)），而另有一个独立的身份平台运营在 [genauth.ai](https://www.genauth.ai/)。所查阅的任何 Eazo 页面都未说明 `GenAuth` 是 Eazo 自研组件、第三方产品，还是共用品牌。见 `备注`。

---

## 产品

首页主标题为 "Discover what agents can do for your life."，副标题为 "Discover agents built by creators. Make them your own — or build the next one."。导航有三项：Home、Creator（`creator.eazo.ai`）和 Developer（`eak.eazo.ai`）（[官网](https://eazo.ai/)；无日期，访问于 2026-07-30）。页脚标语为 "DISCOVER. SHARE. USE. REMIX."。

### 产品线

| 产品线 | 展示的状态 | 是什么 | 来源 |
|---|---|---|---|
| Eazo Mobile | iOS 与 Android 已上线 | 面向消费者的 App，用于 "Discover"、"Use instantly"、"Remix" 和 "Build & share" 由创作者制作的 AI 应用、agent、聊天机器人和助手 | [App Store 描述](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137) |
| Eazo Creator | 已上线，需登录 | 零代码全栈构建器；`creator.eazo.ai` 上需登录的 SPA 跳转至 `eazo.ai/creator/` | [creator.eazo.ai](https://creator.eazo.ai/)；访问于 2026-07-30 |
| Eazo Anima（EAK） | "currently in private build"；提供等候名单和早期访问表单 | 托管式 agent 基础设施：`GenAuth`（身份）、`GUMem`（记忆）、`Web Agent`（行动），以及邮件和审计记录 | [anima.eazo.ai](https://anima.eazo.ai/)、[早期访问](https://anima.eazo.ai/early-access)；访问于 2026-07-30 |
| Eazo Anima 文档 | 已发布 | 双语（英文／简体中文）VitePress 文档，含快速开始、15 个用例指南、API 表层和安全页 | [文档](https://anima.eazo.ai/docs/)；访问于 2026-07-30 |
| Eazo Anima 定价 | "Pricing · Coming soon" | 页面称 "GenAuth, GUMem, and Web Agent are running in production — the numbers behind them aren't final yet"；最后修订标为 "2026 · Q2" | [定价](https://anima.eazo.ai/pricing)；访问于 2026-07-30 |

### 一手资料中描述的 Eazo Creator

[黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)（中文，抓取于 2026-05-19）围绕三步描述 Creator——BUILD（"生产级的 UI"）、DEPLOY（"全栈自动化部署，一行代码不用写"）、PUBLISH（"一键直达 Eazo 社区"）——并把承诺表述为"所思即所得，生产即上线"。一篇日期为 [2026-05-18](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/)、标注为 "Third-Party Advertising" 的第三方广告投放还描述了六个并行生成的 AI 设计方向、自动化 QA 测试与缺陷修复、"Database, authentication, AI capabilities, API endpoints — all platform-managed"，以及一个可在社区共享的 skills 生态。

公开模板仓库把生成应用的能力面记录为 `@eazo/sdk` 的 `auth`、`device`、`ai`、`storage`、`memory` 和 `notifications` 模块，加上服务端 `requireAuth` 守卫和 `notifications.publish`（[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)；访问于 2026-07-30）。其中值得注意的记录行为：

- `ai` 仅在服务端可用；在默认的 `EAZO_AI_PROVIDER_MODE=eazo` 模式下调用 Creator 的 `/api/app-ai/chat` 代理，"so official Eazo model usage is charged to the app creator's credits"；`byok` 模式则改为调用创作者自备的 OpenAI 兼容供应方（[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)）。
- `memory.reportAction()` 把用户行为事件写入 "the Gum memory service — a persistent, semantically searchable log of what users did in your app"（[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)）。自 `@eazo/sdk` 0.21.0（2026-06-11）起，该调用受应用作者的 `sendAnonymousData` 同意开关约束，开关从 `GET /api/apps-open/:appId` 读取，并在服务端 `POST /api/open/gum/action` 处再次校验（[CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)）。
- `share.compose()` 把文本和最多四张图片附件交给宿主，宿主 "AI-drafts a post from the inputs"；在普通浏览器中则显示 "Continue in the Eazo app" 的引导（[SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md)）。
- 在网页端打开的应用会获得一个顶部交接横幅，带有应用标识、点赞／评论栏，以及 "Remix" 和 "Open in Eazo" 两个 CTA；当 App 未能打开时，Remix 回落到 `creator.eazo.ai`（[CHANGELOG 0.21.0](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)）。

### 商业化

服务条款描述的是一套面向创作者的变现体系，而不是订阅价目表；未找到 Eazo Mobile、Eazo Creator 或 Eazo Anima 的任何公开价目表（[服务条款 § 3.5](https://eazo.ai/terms-of-service)；生效日 2026-02-01）。

| 项目 | 内容 | 来源 |
|---|---|---|
| 收什么费 | "In-App Charges"——针对创作者应用或 agent 终端用户收取的付费功能、付费访问、订阅、一次性购买或按量计费 | [服务条款 § 3.5.1](https://eazo.ai/terms-of-service) |
| 收款模式 | 创作者必须指定其中一种、并由 Eazo 确认：(A) Platform Collects、(B) Creator Collects、(C) Credits/Hybrid Settlement | [服务条款 § 3.5.1](https://eazo.ai/terms-of-service) |
| 平台费 | Eazo 及／或其支付服务商 "may deduct … a platform fee and/or commission at the rate(s) displayed in the relevant Service interface"；费率未公开 | [服务条款 § 3.5.2](https://eazo.ai/terms-of-service) |
| 创作者提现 | "Creator Earnings" 记录在 "Earnings Balance" 台账中；提现需完成 KYC、提供税务信息，并通过反洗钱／反恐融资和制裁筛查，另有最低金额和持有期 | [服务条款 § 3.5.3](https://eazo.ai/terms-of-service) |
| 支付服务商 | "We use Stripe and/or other service providers"；在模式 B 下创作者通过自有账户（"e.g. a Stripe Connect connected account"）成为登记商户 | [服务条款 § 3.5.4、§ 3.5.9](https://eazo.ai/terms-of-service) |
| 点数（credits） | 在模式 C 下终端用户向 Eazo 购买点数；点数 "have no cash value outside the Services … may expire, and … are non-refundable"，Eazo 可在通知后调整点数换算与模型成本费率 | [服务条款 § 3.5.10](https://eazo.ai/terms-of-service) |
| 自动退款 | "in the event of a generation failure or if your User App or Agent does not pass our review process, any In-App Charges or credits consumed during that process will be automatically refunded" | [服务条款 § 3.5.7](https://eazo.ai/terms-of-service) |
| 对创作者的责任上限 | 上限为 "the Platform Fees actually received by Eazo from your In-App Charges during the twelve (12) months preceding the event" | [服务条款 § 3.5.13](https://eazo.ai/terms-of-service) |
| 创作者侧的 AI 成本 | 默认模式下，官方 Eazo 模型用量计入应用创作者的点数 | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| Anima 的计费迹象 | API 错误码包含 `insufficient_credits` 和 `budget_exceeded`；限制包含 "per-project monthly credit budget — soft warning at 80%, hard stop at 100%" | [WebAgent API 概览](https://anima.eazo.ai/docs/webagent/reference/) |
| Anima 早期访问 | "Early-access teams pay nothing during calibration" | [定价](https://anima.eazo.ai/pricing) |

### 各时期公布的规模数据

| 日期 | 公布的数字 | 来源 |
|---|---|---|
| 2026-03-28 | iOS 应用首次发布 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us) |
| 2026-05-18 | 黑客松 "over 1,000 builders have already signed up" | [Stanford Daily，第三方广告](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/) |
| 2026-05 | "1000+ creators have already signed up for EAZO Global Hackathon" —— 取自搜索结果标题；未经确认，`x.com` 阻止自动访问 | [X，@FellouAI](https://x.com/FellouAI/status/2054356197491273795) |
| 2026-05-23/24 | Luma 记录出席人数为 "303 Went"（硅谷场）和 "176 Went"（纽约场） | [Luma 硅谷](https://luma.com/frw43jmv)、[Luma 纽约](https://luma.com/ay4dy8o5) |
| 访问于 2026-07-30 | Google Play "50+ Downloads"；App Store 15 条评分、均分 4.47 | [Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)、[iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us) |

公司未就 Eazo Mobile 或 Eazo Creator 公布任何用户数、创作者数、应用目录规模、收入或交易数据——见 `备注`。

### EAZO 2026 全球黑客松

| 项目 | 内容 | 来源 |
|---|---|---|
| 日期与形式 | 2026-05-23/24，48 小时，线下加线上；宣传语为"全球首场『零代码』全栈黑客松" | [黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| 地点 | 旧金山（山景城）、纽约、上海（DIIS，虹口区东长治路505号），全球线上参赛并入上海或旧金山赛区 | [黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)、[Luma 硅谷](https://luma.com/frw43jmv) |
| 奖池 | 合计 30 万美元、253 个获奖名额：全球奖 9 万美元（总冠军 5 万、People's Choice 2.5 万、Builder's Choice 1.5 万）；三个赛区各取前 20 名的区域奖；特别奖 9 万美元；颁奖后七天的 "D+7" 拉新传播奖 3.5 万美元 | [黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| 区域奖池（纽约） | "NYC regional prize pool: $17,000 total" | [Luma 纽约](https://luma.com/ay4dy8o5) |
| 计分 | Eazo 平台用户投票 50%、六人专家评审团打分 40%（2 位投资人、2 位 AI 创始人、1 位 coding agent 专家、1 位 design agent 专家）、选手互评 10%；五项评分维度各占 20% | [黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| 提交要求 | 提交物必须是真实上线、任何人可用的产品，而非原型或 Demo；硬截止为各地时间 2026-05-24 07:00，前 30 队进入 Demo Day | [黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| 赛道 | 超级家长、AI 陪伴（明确包含面向 ADHD/ASD 群体的应用）、人生操作系统、身体智能、自由创意 | [黑客松页面存档](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| 报名与规则 | 通过 Tally 表单和 Luma 报名；规则与条款托管在 Google Drive；另有一个投票站点 `hackathon2026.eazo.dev`（部署在 Vercel，客户端渲染） | [Luma 纽约](https://luma.com/ay4dy8o5)、[hackathon2026.eazo.dev](https://hackathon2026.eazo.dev/) |
| 活动后状态 | 公司自己的 `eazo.ai/hackathon` 页面现返回 HTTP 404，Devpost 列表返回 HTTP 410 Gone；未找到获奖名单公告 | 路径检查于 2026-07-30；[Devpost](https://eazo-ai-hackathon.devpost.com/) |

黑客松总结文章 [We Ran a Different Kind of Hackathon（2026-05-02）](https://eazo.ai/blog/we-ran-a-different-kind-of-hackathon) 把前提表述为 "No code. 48 hours. Three cities. One moment."，并称提交作品 "live on the platform, discovered and used by real people"。

### 公司自述的计划

[招聘页](https://eazo.ai/careers) 写道 "We're creating InternetOS, a system of agents that live in daily life, work alongside you, and quietly expand what you're capable of"，以及 "We're just getting started, and there's still room to shape what this company becomes"。[Eazo Anima](https://anima.eazo.ai/) 称自己在 "building toward a web where we make Agents first-class citizens of the Web, with their own identity, inspectable memory, delegated authority, and replayable actions"，并称身份、记忆、网页执行、邮件和审计记录 "currently in private build"。[定价页](https://anima.eazo.ai/pricing) 把下一个里程碑写为 "Public pricing → talk to sales for an ETA"。

---

## 创始人

**Yang** —— "Founder & CEO of Eazo"，关于页引用其原话："We believe AI is a mirror to the human mind—designed to Learn more, Know more, and Be more. By bringing Capability Equality to everyone, we empower you to navigate a complex world. We never stop."（[关于页](https://eazo.ai/about)；无日期，访问于 2026-07-30）。任何 Eazo 页面都没有出现姓氏、履历、教育背景或公司成立日期。

三处外部来源指向同一人。Eazo 自办硅谷黑客松的 Luma 页面显示 "Hosted by Yang Xie"，链接到 Luma 用户 `dominic0` 和 X 账号 `@dominicy0`，主办组织列有 `eazo.ai`（[Luma](https://luma.com/frw43jmv)；访问于 2026-07-30）。一个 LinkedIn 档案 `linkedin.com/in/ivydom/` 被索引为 "Yang Xie - ASI X"；该页面 2026-07-30 对自动访问返回 HTTP 999，未被直接读取。Fellou——其法律页面写明同一主体 `ASI X Inc.`——在媒体报道中被归于创始人 Yang Xie／谢扬：[GlobeNewswire（2025-08-12）](https://www.globenewswire.com/news-release/2025/08/12/3131385/0/en/Fellou-Announces-Next-Generation-Agentic-AI-Browser-Transforming-the-Future-of-Work.html) 称 Fellou "co-founded by 2021 Forbes U30 Asia honoree Yang Xie"。

Eazo 的 "Yang" 即 Yang Xie，是基于黑客松主办人姓名、LinkedIn 索引和共用法律主体做出的研究者推断；没有任何 Eazo 页面直接写明这一点。

第三方报道中关于 Yang Xie 的履历事实，均非来自 Eazo 或 ASI X 的来源：身份平台 Authing 的创始人，2019 年创立，2024 年被描述为服务超过 700 家客户（[新浪科技／创事记，2025-04-21](https://finance.sina.com.cn/tech/csj/2025-04-21/doc-inetwzpw8763926.shtml)）；此前在字节跳动任职（[APT401 Substack](https://apt401.substack.com/p/the-browser-that-acts-how-fellou)）；2021 年入选福布斯亚洲 30 Under 30（[GlobeNewswire，2025-08-12](https://www.globenewswire.com/news-release/2025/08/12/3131385/0/en/Fellou-Announces-Next-Generation-Agentic-AI-Browser-Transforming-the-Future-of-Work.html)）。有一期长访谈以播客形式存在：[《与Fellou创始人谢扬的3小时访谈》（中文）](https://podcasts.apple.com/cn/podcast/34-%E4%B8%8Efellou%E5%88%9B%E5%A7%8B%E4%BA%BA%E8%B0%A2%E6%89%AC%E7%9A%843%E5%B0%8F%E6%97%B6%E8%AE%BF%E8%B0%88-%E5%AD%A4%E7%8B%AC-95%E5%90%8E-%E7%89%8C%E6%A1%8C%E4%B8%8E%E7%94%9F%E4%BA%A7%E5%8A%9B%E7%9A%84%E5%AE%8C%E7%BE%8E%E5%88%9B%E4%B8%9A/id1754955836?i=1000704842263)。

出现在 Eazo 公开材料中的其他人是黑客松的联合主办人和评委，而非声明的员工。硅谷 Luma 页面列出包括 Yang Xie、Lyn Zhang、NingNing、Laura Dang、Vivian Cai、Krypton M.、Ryan Foo、Yuna Chu 和 bojun sheng 在内的十一位主办人，以及 AI Valley 账号（[Luma](https://luma.com/frw43jmv)）。纽约页面列出的评委包括 Donnie D'Amato 和 Nuoran（[Luma 纽约](https://luma.com/ay4dy8o5)）。`eazo.ai` 上没有团队页、管理层页或人员介绍页，两篇博客均署名 "Eazo Team"。

`@eazo` 各包背后的三个 npm 维护者账号，其注册邮箱为 `zhuowei@fellou.ai`、`liaochangjiang@fellou.ai` 和 `suntianxiang@fellou.ai`，账号名为 `luozhuowei`、`liaochangjiang_fellou` 和 `lucsun-fellou`（[npm](https://registry.npmjs.org/@eazo%2Fsdk)；访问于 2026-07-30）。没有任何 Eazo 页面把这些账号与具名职务对应起来。

---

## 融资

截至 2026-07-30，在所查阅的公开来源中，未找到公司就 Eazo 品牌、Fellou 品牌或 `ASI X Inc.` 发布的任何融资公告。下表记录的是第三方来源的说法。

| 日期 | 轮次（按来源写法） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 无日期；访问于 2026-07-30 | 未命名 | 报道为 4040 万美元 | LongRiver Investments | 报道为 4040 万美元 | [PitchBook 的 Fellou 档案](https://pitchbook.com/profiles/company/894665-44)——该页对自动访问返回 HTTP 403；数字取自搜索结果摘要，因此未经确认 |
| 无日期；访问于 2026-07-30 | "Unfunded"——"Fellou has not raised any funding rounds yet" | 无 | 未列出 | 无 | [Tracxn 的 Fellou 档案](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw) |
| 2026-07-07 | 不是轮次，而是一则状态说法 | — | — | — | [36 氪（中文）](https://36kr.com/p/3884772932792581)："Fellou后续遇到融资困难，难以为继。"该文未给出这一说法的出处 |

两个数据库的数字描述的都是 Fellou 品牌，而非 Eazo 品牌。两者都未与一手来源核对，且互相矛盾——见 `备注`。投资方参与情况、轮次名称、估值，以及是否存在专门属于 Eazo 的融资，在所查阅的任何来源中都未得到确认。

日期晚于 36 氪那一说法的第三方材料显示 ASI X Inc. 仍在以 Eazo 品牌持续发布：`@eazo/sdk` 0.22.3 于 2026-07-28 发布（[npm](https://registry.npmjs.org/@eazo%2Fsdk)）、Android 应用于 2026-07-28 更新（[Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)）、iOS 应用于 2026-07-29 更新（[iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)）、`eazo-creator-nextjs-template` 于 2026-07-29 有推送（[GitHub](https://github.com/EazoAI/eazo-creator-nextjs-template)）。招聘页挂着三个在招岗位，提供 "Top-of-market salary + equity"（[招聘页](https://eazo.ai/careers)；无日期，访问于 2026-07-30）。这些是带日期的观察，而不是关于融资状况的结论。

---

## 工程

### 技术栈与平台

未发布技术栈说明页。除标注外，以下条目均由可观察的公开资产或一手公开仓库确认。

- **托管与边缘（由 2026-07-30 观察到的响应头确认）：** `eazo.ai` 返回 `x-powered-by: Express` 并输出服务端渲染的 HTML；`eazo.ai/creator/` 由 `nginx/1.27.5` 提供服务，是 Vite 构建的 SPA，其静态资源从 `assets.eazo.ai` 加载；`anima.eazo.ai` 返回 `x-powered-by: Next.js` 以及 `x-nextjs-cache` / `x-nextjs-prerender`；`eak.eazo.ai` 返回 `server: awselb/2.0` 并 302 跳转至 `anima.eazo.ai`；`cdn.eazo.ai` 通过 `CloudFront` 从 `AmazonS3` 分发 APK，带 `x-amz-server-side-encryption: AES256`；`api.eazo.ai`、`docs.eazo.ai` 和 `status.eazo.ai` 经 Cloudflare 解析但返回 HTTP 404；`hackathon2026.eazo.dev` 返回 `server: Vercel`。
- **文档：** VitePress，英文／简体中文双语，位于 `anima.eazo.ai/docs/`（[文档](https://anima.eazo.ai/docs/)；访问于 2026-07-30）。
- **生成应用的运行时（由公开模板确认）：** Next.js 16.2.4 App Router、React 19.2.4、TypeScript、Tailwind CSS v4、Bun 1.3.9、shadcn/ui、`@base-ui/react`、lucide-react、framer-motion、Drizzle ORM 0.45 配 `postgres.js` 连接 PostgreSQL、`i18next` / `react-i18next` 支持 `en-US` 与 `zh-CN`、`zod`，以及 `@modelcontextprotocol/sdk`（[package.json](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/package.json)、[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)）。模板的 i18n 栈被描述为 "same stack as Eazo Creator frontend"。
- **模型访问（由公开模板确认）：** 平台 AI "routes through AWS Bedrock via the Eazo AI gateway"；文档中的默认模型 key 为 `deepseek.v3.1`，公布的支持列表涵盖 DeepSeek v3.1/v3.2、OpenAI `gpt-oss` 与 `gpt-oss-safeguard`（20b/120b）、Qwen3（含 `qwen3-vl-235b-a22b-instruct` 及 coder 变体）、Mistral 的 Ministral／Magistral／Devstral／Voxtral 与 `mistral-large-3-675b-instruct`、Google Gemma 3、NVIDIA Nemotron、MiniMax M2 系列、Moonshot Kimi K2、Z.ai GLM 4.6/4.7/5，以及 Writer Palmyra Vision（[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)；访问于 2026-07-30）。该封装 "uses OpenAI-compatible request/response shapes"。
- **认证与会话加密（由已发布的包确认）：** `@eazo/node-sdk` 自述为 "Decrypt encrypted data using ECC secp256k1 + AES-256-GCM"，依赖 `elliptic`；`@eazo/auth` 处理 "Eazo Mobile (encrypted session) and Web (GenAuth OIDC/JWT)"，依赖 `jose`、`elliptic` 和 `authing-js-sdk`；`@eazo/sdk` 依赖 `authing-js-sdk`、`elliptic`、`openai`、`qrcode-generator` 和 `@radix-ui/react-dialog`；服务端推送发布 "Authenticates by signing an ES256K JWT with `EAZO_PRIVATE_KEY`"（[npm](https://registry.npmjs.org/@eazo%2Fsdk)、[SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md)）。
- **在已部署页面中观察到的分析与工具：** Google Analytics 的 `gtag.js`（`eazo.ai` 上为 `G-EXPH819QL6`，`eazo.ai/creator/` 上为 `G-V1CNGB211P`）；Creator 的运行时配置声明了 `VITE_AUTHING_*`、`VITE_POSTHOG_KEY`、`VITE_POSTHOG_HOST` 和 `VITE_ANALYTICS_API_BASE` 等键，表明存在 Authing 和 PostHog 的集成点（公开文件中的值为空）（[creator-runtime-config.js](https://eazo.ai/creator/creator-runtime-config.js)；访问于 2026-07-30）。申请表单使用 Tally；活动使用 Luma；黑客松规则通过 Google Drive 分发。
- **Anima 的 API 表层（由已发布的 OpenAPI 文档确认）：** `anima.eazo.ai/docs/openapi/v1.json` 上的规范声明 OpenAPI 3.1.0、标题 "WebAgent Backend"、版本 0.2.4，共 125 条路径，其中 47 条在 `/api/admin` 之下（访问于 2026-07-30）。文档中的 base URL 为 `https://api.eak.eazo.ai`，Bearer key 以 `wa_` 开头，游标分页每页上限 100，并支持可选的 `Idempotency-Key` 头（[API 概览](https://anima.eazo.ai/docs/webagent/reference/)）。
- **SDK 分发：** TypeScript 包 `@eazo/eak`（15 个版本，2026-06-02 至 2026-06-18）与 `@eazo/sdk`（27 个版本，2026-04-22 至 2026-07-28），均为 MIT（[npm](https://registry.npmjs.org/@eazo%2Feak)、[npm](https://registry.npmjs.org/@eazo%2Fsdk)；访问于 2026-07-30）。文档还提到一个 Python 包 `eazo-eak`（[Quickstart](https://anima.eazo.ai/docs/guides/quickstart)）；2026-07-30 时 `pypi.org/pypi/eazo-eak/json` 返回 HTTP 404——见 `备注`。
- **仅在招聘中提到、未在生产中另获确认的项：** 知识图谱、向量检索、记忆压缩、LangGraph、"Agent SDKs"，以及 "Deep understanding of React or V8 JavaScript Engine"（[招聘页](https://eazo.ai/careers)；无日期，访问于 2026-07-30）。招聘要求不构成当前实际使用的证据。

### 系统

| 系统 | 做什么 | 来源 |
|---|---|---|
| Eazo Mobile 宿主桥 | 嵌入式网页应用与原生外壳之间的 `postMessage` 桥：原生登录 UI、分享／撰写交接、按应用的推送订阅、设备上下文与语言 | [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| 加密会话交接 | 宿主签发加密的用户 token；应用服务端用 ECC 私钥解密并返回用户档案 | [模板 README](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/README.md) |
| 应用脚手架与部署 | 由平台注入的环境变量（应用 id、标题／描述、AI 供应模式）和全栈应用的一键部署；平台提供自有 SDK 包地址而非公共 npm 源 | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)、[SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| AI 网关与创作者计费 | 位于 `/api/app-ai/chat` 的代理，把官方模型用量计入创作者点数，并提供 BYOK 旁路 | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| 市场支付 | 由 SDK 掌握的结账、状态轮询、权益刷新和一套支付台账；Stripe 返回时带 `payment_id`，SDK 据此轮询 "the Eazo ledger"；生成的应用被要求不得自行加入 Stripe SDK、webhook 或密钥 | [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| 推送通知分发 | 按（用户，应用）写入的订阅位由宿主完成；服务端 `notifications.publish` 向订阅者分发，文档记录订阅者超过 5,000 时返回 413 | [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| Gum / GUMem 记忆服务 | 以 `ActionLogs / Messages → Facts → Summaries → Topics` 分层结构存储会话、行为和画像记忆，采用向量与图混合存储，支持按任务范围召回、webhook 和生命周期删除 | [GUMem 概览](https://anima.eazo.ai/docs/gumem/getting-start/overview/)、[anima.eazo.ai](https://anima.eazo.ai/) |
| GenAuth 委托授权 | 签发短时效 `grantToken`，携带 `userId`、`agentKey`、允许与拒绝的 scope、过期时间和 `auditId`；提供身份网关、MCP Hub Profiles、审计记录和 `genauth-cli` | [GenAuth 概览](https://anima.eazo.ai/docs/genauth/)、[安全指南](https://anima.eazo.ai/docs/guides/security) |
| Web Agent 执行面 | 基于受控浏览器沙箱的 session／run 模型，提供 `DoAnything` API、成型的 `DeepResearch`／`WebSearch`／`Track` API、SSE 事件流、ReAct 轨迹、浏览器视频帧、截图、录制、暂停／恢复／介入、已保存的站点登录与 profile，以及带重试的监控投递 | [WebAgent 概览](https://anima.eazo.ai/docs/webagent/)、[OpenAPI 3.1 规范](https://anima.eazo.ai/docs/openapi/v1.json) |
| 生成应用中的 MCP 服务器 | 通过 `@modelcontextprotocol/sdk` 提供 Streamable HTTP MCP 服务器，无状态运行，每次请求创建全新实例 | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| 生成应用中的定时任务 | Vercel Cron 调用 `/api/notifications/cron/daily-digest`，以共享的 `CRON_SECRET` 认证 | [.env.example](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/.env.example) |
| 已公开但非公众产品的内部管理面 | OpenAPI 文档还声明了打着 `admin:benchmark`、`admin:inspect`、`admin:deploy`、`admin:dynamic-config`、`admin:env`、`admin:tenants`、`admin:workers`、`admin:audit` 和 `admin:panic` 标签的管理端点，包括浏览器与会话检查、部署／回滚，以及按租户发放点数 | [OpenAPI 3.1 规范](https://anima.eazo.ai/docs/openapi/v1.json)；访问于 2026-07-30 |

**公布的基准测试说法。** GUMem 文档称在 LoCoMo 长会话记忆基准上达到 92.9% 准确率，描述为 "currently SOTA-level performance"，并给出一张包含 16 个对比系统的表格，其中包括 Mem0（91.60，标注 "New April 2026"）、HyperGraphRAG、MIRIX、HippoRAG 2、LightRAG、MemOS、Membase、GraphRAG、Zep、LangMem、MemU、OpenAI 和 A-Mem。该页说明评测使用官方 `locomo10.json` 的 10 组会话子集——272 个 session、5,882 轮对话、1,986 条 QA 标注——并链接了 [LoCoMo 论文](https://arxiv.org/abs/2402.17753) 和 [数据集](https://github.com/snap-research/locomo/blob/main/data/locomo10.json)（[性能页](https://anima.eazo.ai/docs/gumem/concepts/performance)；访问于 2026-07-30）。该数字为自行报告；页面未给出评测日期、评判模型或任何独立复现。

**文档状态标注。** Anima 的 "API Surface" 页标注 "Draft interface — The examples below express integration intent. They are not final SDK or HTTP contracts"（[API 表层](https://anima.eazo.ai/docs/api/)；访问于 2026-07-30），而 WebAgent 参考文档则发布了一份具体的 OpenAPI 3.1 文档。

### 文档中说明的数据处理

服务条款称，通过 Eazo 创建的应用和 agent "may also include memory-related capabilities"，并且 "Unless you adjust the relevant settings where controls are made available, Eazo may enable by default the setting under which user data generated from the use of your app or agent within Eazo Mobile is automatically reported, synchronized, or otherwise transmitted to Eazo"（[服务条款 § 3.1](https://eazo.ai/terms-of-service)；生效日 2026-02-01）。已发布的应用和 agent 在创作者未更改可见性或 Remix 设置时 "may be public by default" 且 "may be remixable by default"（[服务条款 § 5.8、§ 5.9](https://eazo.ai/terms-of-service)）。

隐私政策称，服务 "powered by one or more third-party generative AI models"，输入 "may be transmitted to these third-party AI providers"，公司会 "take steps to contractually restrict those providers from using your data for their independent model training"，而其自身用于改进模型的使用只发生在信息 "securely encrypted and de-identified" 之后，并附有反对权（[隐私政策 § 1.2.11](https://eazo.ai/privacy-policy)）。未点名任何第三方 AI 供应方。该政策还称公司按 CCPA 定义向第三方广告网络 "'sell[s]' and 'share[s]'" 个人信息，可通过邮件 `privacy@eazo.ai` 退出，并说明会为基于位置的查询收集精确 GPS 位置，以及收集真实姓名、出生日期和政府证件号码 "to verify your age and your identity as required by applicable laws"（[隐私政策](https://eazo.ai/privacy-policy)）。

Anima 安全指南记录了双层模型——GenAuth 授权加受控浏览器沙箱——并称 "EAK does not persist user passwords"，密码 "should not be written to task results, ReAct traces, GUMem, audit body text, callback events, or application logs"，`callbackUrl` 必须使用 HTTPS，返回的视频帧和截图必须绑定到具体的 `taskId`、项目和用户会话，且 "EAK does not publish browser video as a public resource"（[安全指南](https://anima.eazo.ai/docs/guides/security)；访问于 2026-07-30）。

### 招聘所需技术背景

以下全部来自 [eazo.ai/careers](https://eazo.ai/careers) 上的三个岗位页（无日期，访问于 2026-07-30）。投递通过 Tally 表单而非招聘系统完成。

**Agent Engineer** —— 旧金山或新加坡，"remote possible for exceptional cases"，全职。

- *必需：* "Deeply self-driven"；在 JavaScript、TypeScript 和 Python 上有实力，"with solid engineering fundamentals"；工作范围覆盖 agent 记忆、agent 主动性和多 agent 编排，包括设计核心 agent 系统（记忆、主动推理、任务编排）和优化多 agent 工作流。
- *优先：* 有原创的 agent/LLM 项目、实验或产品，可通过 GitHub、博客或 demo 展示；在黑客松、NOI、Kaggle 或类似竞赛中获奖；agent 框架、知识图谱、向量检索或记忆压缩经验；对 Agent SDK、LangGraph 或类似生态有贡献；对 React 或 V8 JavaScript 引擎有深入理解；做过从零到一"with real users or revenue"的东西。
- 岗位描述写着 "No hierarchy here" 和 "If you need someone to tell you what to do, this isn't the role."。

**Design Engineer** —— 旧金山，"remote possible for exceptional candidates"，全职。

- *必需：* 设计并构建生成式 UI（"GenUI"）系统，"from concept to production code"；交付 "real features in React, not just hand off mockups"；面向动态界面的信息架构；交互与动效设计；建立设计系统。
- *优先：* 设计过 AI 原生或基于 agent 的产品；扎实的 React 与现代前端能力；能同时展示设计思考和已上线代码的作品集；动效设计与微交互；建过或参与过规模化设计系统；生成式 UI、自适应界面或非常规交互模式；信息架构或复杂数据驱动产品经验。

**Growth** —— 旧金山，"remote possible for exceptional candidates"，全职。

- *必需：* 端到端负责从获取到激活到留存的完整漏斗；跑增长实验；"across multiple markets (North America, Europe, Japan)" 推动获客；漏斗与行为分析；把增长机制内建到产品里；SEO/SEM、社交、内容与社区。
- *优先：* 把某个 AI 原生产品 "from zero to significant scale" 做起来过；多市场发布经验；增长循环或推荐机制；为技术产品做过内容创作或品牌建设；创业公司经验。

**Talent Community** —— 全球，一个开放表单，覆盖工程、设计、增长、产品、研究、运营 "or something else"。

### 行业领域

工作范围覆盖 agent 运行时与工具协议（MCP、OIDC/OAuth 委托、OpenAPI 3.1、SSE 事件流）、iOS 与 Android 的消费级应用商店分发，以及创作者市场的商务：平台代收与创作者自收、登记商户归属、点数、退款与拒付、提现环节的 KYC 与代扣税，以及反洗钱／反恐融资和制裁筛查（[服务条款 § 3.5](https://eazo.ai/terms-of-service)）。Anima 文档还加上了委托授权设计和浏览器自动化的安全议题：scope 与拒绝 scope 建模、审计记录、密码路径隔离，以及明确要求在 "The target site's terms do not allow automated access and you do not have the required authorization" 时不要使用 WebAgent（[WebAgent 概览](https://anima.eazo.ai/docs/webagent/)）。隐私文档再加上 GDPR/EEA+、英国、瑞士以及十三个具名美国州的隐私法规、CCPA 的出售／共享披露，以及未满 18 岁用户的处理（[隐私政策](https://eazo.ai/privacy-policy)）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | `eazo.ai/careers`，四条列表加一个 FAQ；通过 Tally 表单投递 | [招聘页](https://eazo.ai/careers)；无日期，访问于 2026-07-30 |
| 地点 | Agent Engineer："San Francisco or Singapore"；Growth 与 Design Engineer："San Francisco"；Talent Community："Global" | [招聘页](https://eazo.ai/careers) |
| 远程政策 | "remote possible for exceptional cases"（Agent Engineer）和 "remote possible for exceptional candidates"（Growth、Design Engineer）；未给出通行的远程政策 | [招聘页](https://eazo.ai/careers) |
| 薪酬 | 三个岗位均写 "Top-of-market salary + equity (open to negotiate)"；未公布区间 | [招聘页](https://eazo.ai/careers) |
| 签证支持 | "We prefer candidates who already have work authorization. For truly exceptional candidates who need sponsorship, we're open to exploring options." | [招聘 FAQ](https://eazo.ai/careers) |
| 年限要求 | "No. We care about what you can do, not how long you've been doing it." | [招聘 FAQ](https://eazo.ai/careers) |
| 实习生与在校生 | "Yes, for every role. Strong interns have a clear path to full-time offers." | [招聘 FAQ](https://eazo.ai/careers) |
| 面试流程 | "Typically 2-3 rounds"，可能含带回家作业或结对编程；"expect a decision within 1-3 weeks from your first conversation" | [招聘 FAQ](https://eazo.ai/careers) |
| 自述的协作方式 | "Small team, flat structure, high ownership. We ship fast, debate ideas openly, and care about craft. No hand-holding" | [招聘 FAQ](https://eazo.ai/careers) |
| 工作语言 | 未作为政策写明。招聘站点、产品站点、App Store 列表和英文文档为英文；Anima 文档、Creator 前端的 i18n 栈和黑客松页面同时提供简体中文 | [招聘页](https://eazo.ai/careers)、[文档](https://anima.eazo.ai/docs/)、[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| 团队规模、福利、流动率、坐班政策 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-30）：`eazo.ai` 首页、`/about`、`/careers`、`/blog` 及两篇文章、`/terms-of-service`、`/privacy-policy`，以及对 `/robots.txt`、`/sitemap.xml`、`/llms.txt`、`/.well-known/security.txt`、`/hackathon`、`/apps`、`/explore`、`/discover` 和 `/gallery` 的探测；`creator.eazo.ai` 及其运行时配置；`eak.eazo.ai`、`anima.eazo.ai` 及其文档、定价、早期访问、OpenAPI 文档和 dashboard 跳转；`cdn.eazo.ai`、`api.eazo.ai`、`docs.eazo.ai`、`status.eazo.ai`、`mcp.eazo.ai`、`assets.eazo.ai` 和 `hackathon2026.eazo.dev`；`EazoAI` GitHub 组织及全部五个公开仓库，包括 `README.md`、`AGENTS.md`、`package.json`、`.env.example` 和 `CHANGELOG.md`；`@eazo` npm scope 及全部四个包；PyPI；App Store 和 Google Play 列表包括开发者信息栏；`fellou.ai` 及其服务条款和隐私政策；`FellouAI` GitHub 组织；`eazo.ai`、`eak.eazo.ai`、`anima.eazo.ai` 和 `eazo.dev` 的 Wayback Machine CDX 索引；对品牌名、法律名称和创始人的英文与中文检索；在 36 氪、品玩 PingWest、新浪科技、腾讯新闻、中国日报和知乎上的检索；Crunchbase、PitchBook、Tracxn 和 ZoomInfo 档案；LinkedIn；以及 Luma、Devpost 和 Stanford Daily 的黑客松材料。

- **公司发布的任何融资轮次、投资方或估值。** `eazo.ai` 和 `fellou.ai` 上都没有新闻索引、融资页或公告。找到的唯一数字来自互相矛盾的第三方数据库条目——见下文。
- **除 "Yang" 之外的团队规模和具名员工。** 没有团队页或管理层页；两篇博客均署名 "Eazo Team"；GitHub 组织无公开成员；npm 维护者账号未写明职务。
- **薪资区间。** 未公布；三个岗位均写 "Top-of-market salary + equity (open to negotiate)"。
- **用户数、创作者数、应用目录规模、收入或交易数据。** 均未公布。不存在公开的网页作品集、发现页或目录 API：`/apps`、`/explore`、`/discover` 和 `/gallery` 全部返回 HTTP 404，应用目录只能在移动 App 内或 Creator 登录后访问。
- **平台费费率和 Anima 定价。** 服务条款把平台费费率推给"相关服务界面"；Anima 定价页为 "Coming soon"。
- **具名的第三方 AI 供应方。** 隐私政策只提到 "one or more third-party generative AI models"。模板把 AWS Bedrock 记录为网关并列出模型 key，但未说明任何供应合同、区域或降级方案。
- **安全认证、状态页或公开 SLA。** 所查阅的任何页面都未声明 SOC 2、ISO/IEC 27001 或同类认证。`status.eazo.ai` 和 `docs.eazo.ai` 经 Cloudflare 解析但返回 HTTP 404，模板 README 中指向 `docs.eazo.ai` 的链接因此是失效链接。
- **工程博客。** 博客只有两篇文章（2026-01-26 和 2026-05-02），都是产品与公司定位而非技术写作。技术材料改为发布在 Anima 文档和模板仓库中。
- **`ASI X Inc.` 的工商登记记录。** 未取得。特拉华州 `icis.corp.delaware.gov` 的企业名称检索有 CAPTCHA 门槛，OpenCorporates 于 2026-07-30 返回 CAPTCHA 验证页；未读到任何登记备案。两家公司隐私政策中给出的威尔明顿地址是注册代理地址，不必然是实际办公地。
- **Python SDK。** Quickstart 记录了名为 `eazo-eak` 的包的 `pip` 式用法，但 2026-07-30 时 `pypi.org/pypi/eazo-eak/json` 返回 HTTP 404。未在 PyPI 上找到该名称的包。
- **黑客松结果。** 未找到获奖公告、结果页或奖金发放确认。`eazo.ai/hackathon` 返回 HTTP 404，Devpost 列表返回 HTTP 410 Gone；`hackathon2026.eazo.dev` 上的投票站点为客户端渲染，未暴露任何列表路由。
- **2026-07-30 对自动访问设限的站点：** LinkedIn（HTTP 999）、PitchBook（403）、Crunchbase（403）、`x.com`（402）、OpenCorporates（CAPTCHA）。因此 Eazo 和 Fellou 的 X 账号、被索引为 "Yang Xie - ASI X" 的 LinkedIn 档案，以及 PitchBook 的数字都未被直接读取；上文引用它们的地方，文字取自搜索结果标题或摘要，并已标注为未经确认。

### 不同来源之间的不一致

- **累计融资：** 据报道 [PitchBook 档案](https://pitchbook.com/profiles/company/894665-44) 称 4040 万美元、投资方为 LongRiver Investments，而 [Tracxn](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw) 称同一家公司 "Unfunded"。两者描述的都是 Fellou 品牌，都没有日期，也都未与一手来源核对。PitchBook 的数字取自搜索结果摘要，因为该页返回 HTTP 403。
- **经营状态：** [36 氪（2026-07-07）](https://36kr.com/p/3884772932792581) 无出处地称"Fellou后续遇到融资困难，难以为继"。与之相对，`fellou.ai` 仍在提供首页、服务条款和隐私政策，而 `fellou.ai/blog` 和 `fellou.ai/eko/docs/` 于 2026-07-30 返回 HTTP 503，`FellouAI` GitHub 组织对 `eko` 的最近一次推送日期为 2026-03-03、其他仓库最后推送在 2025 年，同时同一法律主体在 2026-07-28 和 2026-07-29 发布了 Eazo 的更新。两种说法在此并列记录，不作调和。
- **应用名称：** App Store 列表在同一 id `6758009137` 下同时被索引为 "Eazo" 和 "Eazo: Discover AI Apps, Agents"；lookup API 返回较长的名称（[iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)）。
- **应用商店分类：** Apple 把该应用归入生活类，Google Play 归入通讯类（[iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)、[Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)）。
- **产品自我描述随受众变化：** "a community of AI apps and agents"（[App Store](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137)）、"InternetOS, your operating system for the internet"（[博客，2026-01-26](https://eazo.ai/blog/you-were-born-to-be-powerful)）、"your Smart Life Gateway"（[关于页](https://eazo.ai/about)），以及 "The world's first zero-code full-stack AI builder"（[Luma 合作方介绍](https://luma.com/frw43jmv)）。
- **黑客松城市：** 博客文章和 Stanford Daily 投放都把旧金山、纽约和上海列为线下城市（[博客，2026-05-02](https://eazo.ai/blog/we-ran-a-different-kind-of-hackathon)、[Stanford Daily，2026-05-18](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/)）；Luma 页面只把旧金山（山景城）和纽约描述为线下赛区，亚洲线上并入上海赛区（[Luma 硅谷](https://luma.com/frw43jmv)）。
- **Anima API 路径前缀：** API 概览把资源路径写为 `/v1/projects/{project_id}/...`，而已发布的 OpenAPI 文档声明为 `/api/v1/projects/{pid}/...`（[API 概览](https://anima.eazo.ai/docs/webagent/reference/)、[OpenAPI 规范](https://anima.eazo.ai/docs/openapi/v1.json)）。
- **Anima 的成熟度信号：** 首页称身份、记忆和网页执行 "currently in private build"，而定价页称 "GenAuth, GUMem, and Web Agent are running in production"（[anima.eazo.ai](https://anima.eazo.ai/)、[定价](https://anima.eazo.ai/pricing)）。
- **`GenAuth` 是 Eazo 自有层还是第三方平台：** 文档把 `GenAuth` 呈现为 Anima 三层之一（[GenAuth 概览](https://anima.eazo.ai/docs/genauth/)），而 `@eazo/auth` 依赖 `authing-js-sdk`、同时以 `genauth` 和 `authing` 作为关键词，SDK 变更日志也提到 "the Authing OAuth popup"（[npm](https://registry.npmjs.org/@eazo%2Fauth)、[CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)）；另有一个独立身份平台以 [GenAuth](https://www.genauth.ai/) 名义经营。所查阅的任何页面都未说明其关系。

### 其他

- **两个品牌、一个法律主体，营销上互不提及。** `ASI X Inc.` 在 Eazo 和 Fellou 的法律页面中都被列为合同主体，登记地址相同，且 Eazo 应用在 Google Play 的开发者邮箱为 `media@fellou.ai`。两个品牌的营销站点互不链接、互不提及。工程时间线是相邻而非重叠的：`EazoAI` GitHub 组织创建于 2026-02-11，两家公司现行的服务条款和隐私政策都在 2026-02-01 生效，iOS 应用在 2026-03-28 上线，而 `FellouAI` 的仓库最后推送分布在 2025 年至 2026-03-03 之间。
- **公司在开发者产品上公开的深度远超消费产品。** Eazo Anima 提供双语文档、15 个用例指南、一套安全模型、一张基准对比表和一份 125 条路径的 OpenAPI 3.1 文档，而 `eazo.ai` 本身只是一屏落地页加两篇博客，没有 sitemap、没有 `llms.txt`，也没有公开的应用目录。
- **已发布的 OpenAPI 文档包含内部管理面。** 125 条声明路径中有 47 条是 `/api/admin/*`，涵盖带数据集与证据产物的基准测试运行器、带时间线的实时浏览器与会话检查、部署／回滚／部署流式输出、动态配置与环境变量修改、按租户发放点数、worker 管理，以及一个 `POST /api/admin/panic` 端点（[OpenAPI 规范](https://anima.eazo.ai/docs/openapi/v1.json)；访问于 2026-07-30）。
- **平台官方模型列表中没有任何闭源前沿模型。** 文档中每一个 Eazo 模型 key 都是开放权重或托管开源模型——DeepSeek、OpenAI `gpt-oss`、Qwen、Mistral、Gemma、Nemotron、MiniMax、Kimi、GLM、Palmyra——默认值为 `deepseek.v3.1`（[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)；访问于 2026-07-30）。
- **默认公开和默认可 remix 被写进了服务条款**，同时还有一条默认设置：除创作者更改，Eazo Mobile 内的应用使用数据会上报给 Eazo（[服务条款 § 3.1、§ 5.8、§ 5.9](https://eazo.ai/terms-of-service)）。SDK 变更日志记录该上报的同意开关是在 2026-06-11 的 0.21.0 版本中加入的，比服务条款生效晚了四个多月（[CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)）。
- **SDK 发布序列带日期且可逐版本比对。** `@eazo/sdk` 在 2026-04-22 至 2026-07-28 之间发布了 27 个版本，市场支付要求 0.22.3 或更高；`@eazo/eak` 在 2026-06-02 至 2026-06-18 之间发布了 15 个版本，之后未再发布（[npm](https://registry.npmjs.org/@eazo%2Fsdk)、[npm](https://registry.npmjs.org/@eazo%2Feak)；访问于 2026-07-30）。
- **消费端分发数字与黑客松投入在量级上相差很远。** 公布的奖池为 30 万美元、253 个名额，而 2026-07-30 检查时 Google Play 显示 "50+ Downloads"、App Store 显示 15 条评分。
- **公司把异常多的运营环节放在第三方 SaaS 上。** 投递和黑客松报名用 Tally、活动用 Luma、黑客松规则放 Google Drive、黑客松提交用 Devpost、投票应用部署在 Vercel、分析用 Google Analytics 和 PostHog、认证用 Authing、支付用 Stripe、模型访问经 AWS Bedrock——没有自建的招聘系统、状态页或新闻索引。

---

## 资料来源

**官方**

- [官网](https://eazo.ai/)
- [关于我们](https://eazo.ai/about) · [招聘](https://eazo.ai/careers)
- [博客](https://eazo.ai/blog) —— [You Were Born to Be Powerful，2026-01-26](https://eazo.ai/blog/you-were-born-to-be-powerful) · [We Ran a Different Kind of Hackathon，2026-05-02](https://eazo.ai/blog/we-ran-a-different-kind-of-hackathon)
- [平台服务条款](https://eazo.ai/terms-of-service) · [隐私政策](https://eazo.ai/privacy-policy) —— 均于 2026-02-01 生效
- [Eazo Creator](https://creator.eazo.ai/) —— [运行时配置](https://eazo.ai/creator/creator-runtime-config.js)
- [Eazo Anima](https://anima.eazo.ai/) —— [定价](https://anima.eazo.ai/pricing) · [早期访问](https://anima.eazo.ai/early-access)
- [Eazo Anima 文档](https://anima.eazo.ai/docs/) —— [Quickstart](https://anima.eazo.ai/docs/guides/quickstart) · [GUMem 概览](https://anima.eazo.ai/docs/gumem/getting-start/overview/) · [GUMem 基准测试](https://anima.eazo.ai/docs/gumem/concepts/performance) · [WebAgent 概览](https://anima.eazo.ai/docs/webagent/) · [WebAgent API 概览](https://anima.eazo.ai/docs/webagent/reference/) · [GenAuth 概览](https://anima.eazo.ai/docs/genauth/) · [API 表层（草案）](https://anima.eazo.ai/docs/api/) · [安全指南](https://anima.eazo.ai/docs/guides/security) · [OpenAPI 3.1 规范](https://anima.eazo.ai/docs/openapi/v1.json)
- [GitHub 组织 `EazoAI`](https://github.com/EazoAI) —— [eazo-sdk](https://github.com/EazoAI/eazo-sdk)（[SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md)、[CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)）· [eazo-creator-nextjs-template](https://github.com/EazoAI/eazo-creator-nextjs-template)（[README](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/README.md)、[AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)、[package.json](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/package.json)、[.env.example](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/.env.example)）· [GitHub API 组织记录](https://api.github.com/orgs/EazoAI)
- npm scope `@eazo` —— [@eazo/sdk](https://registry.npmjs.org/@eazo%2Fsdk) · [@eazo/eak](https://registry.npmjs.org/@eazo%2Feak) · [@eazo/auth](https://registry.npmjs.org/@eazo%2Fauth) · [@eazo/node-sdk](https://registry.npmjs.org/@eazo%2Fnode-sdk) · [scope 搜索](https://registry.npmjs.org/-/v1/search?text=eazo)
- [EAZO 2026 全球黑客松页面存档（中／英），抓取于 2026-05-19](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)
- [Fellou](https://fellou.ai/) —— [服务条款](https://fellou.ai/terms/) · [隐私政策](https://fellou.ai/policy/)，均写明 `ASI X Inc.`

**应用商店列表**

- [App Store —— Eazo: Discover AI Apps, Agents](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137) · [iTunes lookup API 记录](https://itunes.apple.com/lookup?id=6758009137&country=us)
- [Google Play —— ai.eazo.portal](https://play.google.com/store/apps/details?id=ai.eazo.portal)

**第三方报道与档案**

- [Stanford Daily —— "Join The Eazo Hackathon"，2026-05-18（标注为第三方广告）](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/)
- [Luma —— Eazo AI 2026 Global Hackathon：硅谷场](https://luma.com/frw43jmv) · [Luma —— Eazo.ai 纽约黑客松](https://luma.com/ay4dy8o5)
- [Devpost —— Eazo.ai 黑客松列表（2026-07-30 返回 HTTP 410 Gone）](https://eazo-ai-hackathon.devpost.com/)
- [hackathon2026.eazo.dev —— 投票站点](https://hackathon2026.eazo.dev/)
- [X —— @FellouAI 推广 EAZO 黑客松的帖子，2026-05](https://x.com/FellouAI/status/2054356197491273795)
- [36 氪 —— 《AI浏览器这百亿大蛋糕，谁也没吃到？》，2026-07-07（中文）](https://36kr.com/p/3884772932792581)
- [36 氪 —— 《这个AI新赛道火了，给Agent做浏览器》，2025-04-21（中文）](https://36kr.com/p/3271114913128836)
- [新浪科技／创事记 —— 《95后打造世界首个行动型浏览器——Fellou》，2025-04-21（中文）](https://finance.sina.com.cn/tech/csj/2025-04-21/doc-inetwzpw8763926.shtml)
- [GlobeNewswire —— "Fellou Announces Next-Generation Agentic AI Browser"，2025-08-12](https://www.globenewswire.com/news-release/2025/08/12/3131385/0/en/Fellou-Announces-Next-Generation-Agentic-AI-Browser-Transforming-the-Future-of-Work.html)
- [APT401 —— "The Browser That Acts: How Fellou Captured China's Tech Imagination"](https://apt401.substack.com/p/the-browser-that-acts-how-fellou)
- [Apple Podcasts —— 《与Fellou创始人谢扬的3小时访谈》（中文）](https://podcasts.apple.com/cn/podcast/34-%E4%B8%8Efellou%E5%88%9B%E5%A7%8B%E4%BA%BA%E8%B0%A2%E6%89%AC%E7%9A%843%E5%B0%8F%E6%97%B6%E8%AE%BF%E8%B0%88-%E5%AD%A4%E7%8B%AC-95%E5%90%8E-%E7%89%8C%E6%A1%8C%E4%B8%8E%E7%94%9F%E4%BA%A7%E5%8A%9B%E7%9A%84%E5%AE%8C%E7%BE%8E%E5%88%9B%E4%B8%9A/id1754955836?i=1000704842263)
- [Tracxn —— Fellou 公司档案](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw)
- [PitchBook —— Fellou 公司档案（2026-07-30 对自动访问返回 HTTP 403）](https://pitchbook.com/profiles/company/894665-44)
- [LinkedIn —— "Eazo Technology Co., Ltd."（名称相近；未确立任何关联）](https://www.linkedin.com/company/eazo-technology)
- [GenAuth —— 身份平台](https://www.genauth.ai/)
- [LoCoMo 基准论文](https://arxiv.org/abs/2402.17753) · [locomo10.json 数据集](https://github.com/snap-research/locomo/blob/main/data/locomo10.json)
