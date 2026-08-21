# KusArt

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-21。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-21。英文版为原始版本。

## 摘要

KusArt 是一个面向消费者的 AI 二次元绘画生成器 —— 文生图的原创角色（OC）创作、风格预设、局部重绘、放大、LoRA 训练与视频生成 —— 运营方为 `KAZAMA INC.`，一家地址在 2810 North Church Street, PMB 747006, Wilmington, DE 19802 的特拉华州公司（[服务条款](https://kusart.com/terms)；最后更新 2026 年 4 月）。产品最初用的是另一个品牌：从至少 2025 年 5 月起以 **KusaPics** 运营在 `kusa.pics` 上，而 `kusa.pics` 现在跳转至 `kusart.com`（[Wayback 存档，2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/)；跳转观察于 2026-08-21）—— 见 `品牌与法律实体`。

- 公司自己那个已存档的官网写明了一轮种子前融资："Kamaza.Inc Raises $400K in Pre-Seed Funding Round … with iSeed Ventures as our lead investor"，公布日期 2025-05-12（[kazama.inc 存档，抓取于 2026-02-17](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。该站点现已是一个失效的 Vercel 部署（2026-08-21 返回 HTTP 404）。
- 同一存档页面是唯一列出团队的来源："Neko (Caiwei Lu) - Founder & CEO"、"LAX (Zhuozhi Li) - Technical Lead"、"Roxy (Yuan Zhang) - Growth Lead"，另有一支具备美国与日本背景的研发与市场团队 —— 见 `创始人`。
- 可公开观察的规模信号并不一致：线上站点的风格选择器给出各风格的使用计数，最高一项显示 "111.3M uses"（[kusart.com](https://kusart.com/)；读取于 2026-08-21），而 Similarweb 在 2026 年 7 月口径下对 `kusart.com` 只给出 8.11 万次访问，对 `kusa.pics` 则是环比下跌 61%（[Similarweb](https://www.similarweb.com/website/kusart.com/)、[Similarweb](https://www.similarweb.com/website/kusa.pics/)）—— 品牌迁移正好夹在这两幅图之间，见 `备注`。
- 资金通过一个香港中间方流转："Sygnal E-commerce Limited is an authorised distributor of our products"，地址为 RM 1903, 19/F Lee Garden One, 33 Hysan Avenue, Causeway Bay（[隐私政策](https://kusart.com/privacy)；生效于 2025 年 1 月）。
- 工程可从实际加载的应用看出：置于 Cloudflare 之后的 Next.js 前端，调用位于 `api.kusa.pics`、路径前缀为 `/api/go/` 的独立后端；用 Firebase 做认证；有一份文档化的 B2B API，含 `X-API-Key`、额度冻结记账与 webhook；分析侧是 PostHog 加 Google Analytics，以及 Reddit 与 X 的广告像素（页面资源检查于 2026-08-21）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | KusArt（页面标题 "KusArt – Free Anime & OC AI Art Generator \| Create Original Characters Online"） | [kusart.com](https://kusart.com/)；访问于 2026-08-21 |
| 旧品牌 | KusaPics，域名 `kusa.pics` | [Wayback 存档，2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/) |
| 运营主体 | "KAZAMA INC. (hereinafter referred to as 'KusArt', 'we', 'us', or 'our')" | [服务条款](https://kusart.com/terms)；最后更新 2026 年 4 月 |
| 登记地址 | "KAZAMA INC.: 2810 North Church Street, PMB 747006, Wilmington, DE 19802 US" | [服务条款](https://kusart.com/terms) |
| 分销方 | "Sygnal E-commerce Limited is an authorised distributor of our products"，RM 1903, 19/F Lee Garden One, 33 Hysan Avenue, Causeway Bay, HK | [隐私政策](https://kusart.com/privacy)；生效于 2025 年 1 月 |
| 适用法律 | "the laws of the United States"；"To the extent a more specific jurisdiction is required … the laws of the State of Delaware" | [服务条款](https://kusart.com/terms) |
| 文件日期 | 服务条款 "Last updated: April 2026"、"Effective Date: April 2026"；隐私政策 "Effective Date: January 2025" | [服务条款](https://kusart.com/terms)、[隐私政策](https://kusart.com/privacy) |
| 年龄政策 | "you affirm that you are at least 18 years old … The Services are not intended for children or users under the age of 18" | [服务条款](https://kusart.com/terms) |
| 公开联系方式 | `support@kusart.com`（站点）；`admin@kazama.inc` 与 +1 (917) 419-6843（已存档的官网） | [服务条款](https://kusart.com/terms)、[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| 域名 | `kusart.com` 注册于 2010-11-12（GoDaddy，注册人由 Domains By Proxy 隐去），迟至 2025-07-12 仍在 PerfectDomain 上挂售；`kusa.pics` 注册于 2025-03-01（NameSilo），现跳转至 `kusart.com` | WHOIS 读取于 2026-08-21；[Wayback 存档，2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/) |
| 站点语言 | 英文之外还有 `ja`、`fr`、`es`、`pt`、`de`、`ko`、`zh-CN`（共八个语言版本，以 `hreflang` 备用链接声明） | 响应头观察于 2026-08-21 |
| 社交与社区 | Discord 服务器 "Kusart"（637 名成员、49 人在线）、Instagram `@kusart_official`（6.4 万粉丝、1,527 条帖子）、X `@kusart_official`、YouTube `@KusArt_neko` | [Discord invite API](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true)、[Instagram](https://www.instagram.com/kusart_official/)；观察于 2026-08-21 |
| 移动应用 | 美国区 App Store 中未找到该品牌的应用 | [iTunes 搜索 API](https://itunes.apple.com/search?term=kusart&entity=software&country=us&limit=5)；检查于 2026-08-21 |
| 团队、人数 | 线上站点未公布；仅在已存档的官网上具名 —— 见 `创始人` | 见 `备注` |

### 品牌与法律实体

| 名称 | 类型 | 期间／状态 | 来源中表述的关系 | 来源 |
|---|---|---|---|---|
| KusArt | 当前公开品牌 | 运行于 `kusart.com` | 产品本身；条款把 "KusArt" 定义为 KAZAMA INC. | [kusart.com](https://kusart.com/)、[服务条款](https://kusart.com/terms) |
| KusaPics | 旧公开品牌 | 从至少 2025-05-13 到至少 2026-02-02 运行于 `kusa.pics`；该域名现跳转至 `kusart.com` | 同一产品，官网称其为 "Our flagship product KusaPics" | [Wayback，2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/)、[Wayback，2026-02-01](https://web.archive.org/web/20260201015926/https://kusa.pics/) |
| KAZAMA INC. | 条款与隐私政策中署名的法律主体 | 当前 | 服务的运营方；给出特拉华州地址 | [服务条款](https://kusart.com/terms) |
| Kamaza.Inc | 公司自有官网通篇使用的写法，包括版权行 "© 2025 Kamaza.Inc" | 站点存档于 2025-12 至 2026-02；`kazama.inc` 2026-08-21 返回 HTTP 404（"DEPLOYMENT_NOT_FOUND"） | 被呈现为 KusaPics 背后的公司，地址与 KAZAMA INC. 相同 | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Sygnal E-commerce Limited | 隐私政策中点名的第三方主体 | 当前 | "an authorised distributor of our products"；香港地址 | [隐私政策](https://kusart.com/privacy) |
| `kusart.com` 的前持有者 | 该域名的无关用途 | 互联网档案自 2007 年起有抓取；到 2025 年 7 月仍在挂售 | 同一域名，与当前产品无关 | [Wayback，2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/) |

公司把自己的名字写成两种：法律文件里是 "KAZAMA INC."、域名是 `kazama.inc`，而官网的标题、正文与版权行都写 "Kamaza.Inc"。两种写法都未取得公司登记文件 —— 见 `备注`。

---

## 产品

KusArt 自述为 "an AI anime image generator. Powered by exclusive, ultra-aesthetic anime models"（[kusart.com](https://kusart.com/)；访问于 2026-08-21）。已存档的官网补充说，产品 "Built on diffusion models (DMs) and enhanced with proprietary modules"（[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。

### 产品形态与功能面

| 方面 | 是什么 | 来源 |
|---|---|---|
| 图像生成 | 带标签控制与自动补全／标签建议的文生图；按模型分设 `kusa-anima`、`kusa-easy`、`kusa-mix`（图生图、参考图引导）与 `kusa-niji` 路由 | [sitemap](https://kusart.com/en/sitemap.xml)、[Anima 模型页](https://kusart.com/image-generator/kusa-anima) |
| OC 创作 | "OC Maker"、OC 编辑、角色设定表生成，以及跨姿势与场景的角色一致性 | [kusart.com](https://kusart.com/)、[sitemap](https://kusart.com/en/sitemap.xml) |
| 编辑工具 | 局部重绘、图像放大、从上传图片反推提示词（image to prompt）、提示词优化；扩图、风格迁移与线稿上色标为"即将推出" | [kusart.com](https://kusart.com/) |
| 模型训练 | "Train LoRA Models with Anima" —— 用用户自有图片训练二次元 LoRA，含数据集审阅与受控参数 | [train-lora](https://kusart.com/train-lora) |
| 视频 | 图生视频，以及应用导航中标注 "New" 的视频生成器 | [sitemap](https://kusart.com/en/sitemap.xml)、2026-08-21 观察到的应用导航 |
| 对外暴露的第三方模型 | "Nano Banana"（二次元梗图模板）、`gpt-image-2`，以及一场 "Seedance 2.0" 视频比赛 | [nano-banana](https://kusart.com/nano-banana)、[sitemap](https://kusart.com/en/sitemap.xml)、[Seedance 2.0 比赛](https://kusart.com/events/seedance-2) |
| 风格库 | 一键使用的风格选择器，带各风格使用计数与分类（赛璐璐、兽人、一般动漫、可爱、厚涂、MEME、特殊动漫、男性向、3D 模型） | [kusart.com](https://kusart.com/)；读取于 2026-08-21 |
| "Play" 小工具 | 约 30 个面向 SEO 的生成器 —— Q 版贴纸、换脸、换装／换姿势／换发型、海报与专辑封面制作、漫画生成器、梗图重做、壁纸生成器等 | [sitemap](https://kusart.com/en/sitemap.xml) |
| 社区 | 梗图与风格库、作品展示画廊、应用外壳中的 Kusa-Agent 聊天助手，以及一个 Discord 服务器 | [kusart.com](https://kusart.com/)、[Discord](https://discord.gg/XwxZaKSUzz) |
| B2B API | "B2B API console"，文档化了 `X-API-Key` 认证、任务创建接口、额度冻结、轮询与 webhook 回调 | [api-for-business](https://kusart.com/api-for-business) |

### 商业化

定价页面并不公开：页头的 "Pricing" 链接指向 `#pricing`，而页面上并不存在这个锚点；`/pricing` 返回 HTTP 404；未登录访问 `/credits` 会被跳走（检查于 2026-08-21）。下面是条款所描述的结构。

| 项目 | 内容 | 来源 |
|---|---|---|
| 免费档 | "a limited number of daily credits for personal, non-commercial use. Images generated under this tier may include a watermark" | [服务条款](https://kusart.com/terms) |
| 订阅 | 按月或按年的循环套餐，提供每月额度以及 "watermark-free image generation, enhanced privacy controls, increased usage limits, and eligibility for commercial use rights where available" | [服务条款](https://kusart.com/terms) |
| "无限生成"的范围 | "only to Kusa-XL and Kusa-Easy image generation"；其他模型、视频、编辑工具与多图生成仍消耗额度 | [服务条款](https://kusart.com/terms) |
| 额度包 | 一次性购买；"Credits purchased via Credit Packs do not expire unless otherwise stated"；额度 "have no cash value, are not legal tender, and may not be transferred, resold, exchanged, or redeemed for money" | [服务条款](https://kusart.com/terms) |
| 退款 | "generally non-refundable, except where required by applicable law"；取消在当期结束时生效；退款请求逐案审核 | [服务条款](https://kusart.com/terms) |
| 支付限制 | 付费功能不得用于 "Adult content, pornographic services, escort services, or sexually explicit paid content"、违法或受管制商品、赌博，或涉及受制裁地区的交易 | [服务条款](https://kusart.com/terms) |
| 商用授权 | 商用权利 "only to outputs generated in compliance with these Terms"；"Officially authorized OC" 计划写明 "Individual users earning less than US$1 million annually do not need to sign a separate license agreement" | [服务条款](https://kusart.com/terms)、2026-08-21 读取的 [kusart.com](https://kusart.com/) 首页载荷 |
| 隐私模式 | 仅订阅用户可用的提示词与图片隐私；非订阅用户的内容 "may be eligible for display in community galleries, public feeds, promotional areas, or product examples, and prompts may be visible to other users" | [服务条款](https://kusart.com/terms) |
| 推荐与邀请 | sitemap 中存在 `/referral` 与 `/invite` 路由 | [sitemap](https://kusart.com/en/sitemap.xml) |

### 公开披露的规模变化

| 日期 | 数字或事件 | 来源 |
|---|---|---|
| 2025-03-01 | `kusa.pics` 域名注册 | WHOIS 读取于 2026-08-21 |
| 约 2025-05-11 | 依 snowflake id 推算，Discord 服务器 "Kusart" 创建 | [Discord invite API](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true) |
| 2025-05-12 | 公布 40 万美元种子前融资，领投方 iSeed Ventures | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| 2025-05-13 | 产品最早的存档抓取，品牌为 "KusaPics – Free Anime & OC AI Art Generator" | [Wayback](https://web.archive.org/web/20250513203441/https://kusa.pics/) |
| 2025-07-12 | `kusart.com` 仍在 PerfectDomain 上挂售 | [Wayback](https://web.archive.org/web/20250712131124/https://kusart.com/) |
| 2026-02-02 | `kusa.pics` 最后一次仍以 KusaPics 品牌被存档 | [Wayback](https://web.archive.org/web/20260201015926/https://kusa.pics/) |
| 2026-05-07 至 2026-06-20 | "KusArt × Seedance 2.0 Video Contest" 投稿期 | [events/seedance-2](https://kusart.com/events/seedance-2) |
| 无日期（线上） | "Anima AI Creative Contest —— 3M credits + $10,000 prize pool" | 2026-08-21 读取的 [kusart.com](https://kusart.com/) 首页载荷 |
| 2026 年 7 月口径 | Similarweb：`kusart.com` 8.11 万次访问，全球排名 #394,874，跳出率 34.36%，每次访问 3.34 页，平均停留 2 分 26 秒；国家分布美国 21.23%、日本 18.53%、埃及 7.89%、韩国 5.96%；直接流量 65.02% | [Similarweb](https://www.similarweb.com/website/kusart.com/) |
| 2026 年 7 月口径 | Similarweb：`kusa.pics` 访问量环比下跌 61.07%，桌面访问中 77.26% 来自引荐流量，构成为美国 50.99%／日本 49.01% | [Similarweb](https://www.similarweb.com/website/kusa.pics/) |
| 读取于 2026-08-21 | 线上风格选择器上的使用计数：最高的几项为 111.3M、4.6M、3.1M、3.1M、2.9M、1.6M、1.4M、1.2M 次使用 | [kusart.com](https://kusart.com/) |
| 观察于 2026-08-21 | Discord 637 名成员／49 人在线；Instagram 6.4 万粉丝、1,527 条帖子 | [Discord invite API](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true)、[Instagram](https://www.instagram.com/kusart_official/) |

两个品牌下，公司都没有公布用户数、营收、订阅数或生成总量。

### 已公布的内容规则

条款禁止的类别包括："Sexual content involving minors, age-ambiguous characters, school uniforms used in a sexual context, or characters presented as underage"；"Non-consensual intimate imagery, sexual exploitation, sexual harassment, or abusive sexual content"；以及 "Unauthorized use of real persons' likenesses, private images, personal data, or confidential information"（[服务条款](https://kusart.com/terms)；最后更新 2026 年 4 月）。公司称其运行着 "internal controls, automated filtering mechanisms, keyword filters, image moderation tools, account risk signals"，并进行 "continuous internal monitoring and periodic audits of our AI models and services"。

关于权属，条款写道："You, whether a legal or physical entity, retain all rights and ownership of your Content. We do not claim ownership of your Content unless you and KusArt specifically agree otherwise in writing"，同时说明 "KusArt does not guarantee that any generated output is unique, non-infringing, accurate, lawful, commercially usable, or suitable for a particular purpose"，且 "does not verify ownership of all user-submitted content"。

---

## 创始人

`kusart.com` 上没有团队页。唯一具名的来源是公司自有官网 `kazama.inc`，存档于 2026-02-17，该地址 2026-08-21 返回 HTTP 404（[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。页面写道："Kamaza is built by an international team with expertise in product thinking, AI capabilities, and cultural understanding"。

| 人物 | 职位与自述背景 | 来源 |
|---|---|---|
| Neko（Caiwei Lu） | "Founder & CEO"；"Brings 2 years of full-time entrepreneurial experience in anime community building and AI overseas expansion"；"60,000-follower illustrator on Bilibili"；"Well-connected in the global venture community" | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| LAX（Zhuozhi Li） | "Technical Lead"；"Wuhan University graduate"；"Currently developing advanced art style recommendation systems, unlimited art style models, character consistency features, and planning future Omni architecture models" | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Roxy（Yuan Zhang） | "Growth Lead"；"Shandong University graduate"；"Expert in global market promotion and localization" | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| 研发与市场团队 | "members with backgrounds from the US and Japan, with graduates from top universities including UCI, USC, and University of Pennsylvania" | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |

这些名字都没有出现在线上产品站点上，没有给出人数，所查阅的第三方来源也没有一处能佐证这些职位 —— 见 `备注`。

---

## 融资

只有一轮融资的说法，且出自公司自己那个现已下线的官网。

| 日期 | 轮次 | 金额 | 投资方 | 来源 |
|---|---|---|---|---|
| 公布于 2025-05-12 | "Pre-Seed Round" | 40 万美元（"$400K Total Funding Amount"、"1 Funding Round"） | "iSeed Ventures as our lead investor" | [kazama.inc 存档，抓取于 2026-02-17](https://web.archive.org/web/20260217050446/https://kazama.inc/) |

该页面说明用途为："This Pre-Seed investment will accelerate our AI technology development, expand our product offerings, and strengthen our position in the anime and creative AI community."。一条搜索结果摘要另外点名 Llama Ventures 参投；该名字并未出现在存档的公司页面上，也未获证实。未找到任何投资方公告、备案或新闻稿佐证这一轮，也没有任何地方声称有更晚的轮次 —— 见 `备注`。

---

## 工程

### 技术栈与平台

公司未发布技术栈说明页。以下条目均于 2026-08-21 从实际加载的应用及其网络请求中确认。

- **前端：** Next.js（`x-powered-by: Next.js`、`_next/static` 资源、App Router 的语言分段与 `x-middleware-rewrite: /en`），经 Cloudflare 提供服务（`server: cloudflare`、`cf-ray`、Cloudflare Insights）；以 `hreflang` 备用链接声明了八个语言版本。
- **后端在另一个域名上：** 应用调用 `api.kusa.pics` —— 观察到的接口包括 `/api/go/categories/list` 与 `/api/go/styles/list_for_user`；静态资源还来自 `cdn.kusa.pics` 与一个 CloudFront 分发（`dz2b1yn8y4hm.cloudfront.net`）。也就是说品牌迁到 `kusart.com` 之后，保留下来的 `kusa.pics` 仍在承载 API 与 CDN。
- **认证：** Firebase —— 页面会请求 `firebase.googleapis.com/v1alpha/projects/-/apps/1:751503584748:web:…/webConfig` —— 并配合 Google Identity Services（`accounts.google.com`）。B2B API 文档提到普通 Web 路由使用 "Firebase web tokens"。
- **分析与营销：** PostHog（`us.i.posthog.com`、`us-assets.i.posthog.com`）、Google Analytics（`G-HC6FZE38L4`）与 Google Tag Manager，另有 Reddit（`alb.reddit.com`、`pixel-config.reddit.com`）与 X／Twitter（`static.ads-twitter.com`、`analytics.twitter.com`）的广告像素。
- **支付：** 由第三方处理，隐私政策点名 Sygnal E-commerce Limited 为授权分销方；条款提到 "payment processors, card networks, financial partners" 但一个都没点名（[隐私政策](https://kusart.com/privacy)、[服务条款](https://kusart.com/terms)）。
- **模型：** 产品对外暴露自有命名的模型 —— Kusa-XL、Kusa-Easy、Kusa-Anima、Kusa-Mix、Kusa-Niji —— 以及第三方模型页面（Nano Banana、`gpt-image-2`、Seedance 2.0）。底层架构只被描述为 "diffusion models (DMs) and enhanced with proprietary modules"（[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。
- **没有公开代码：** 未找到该品牌名下的 GitHub 组织或包仓库存在（检查于 2026-08-21）。

### 系统

| 系统 | 做什么 | 来源 |
|---|---|---|
| 生成任务流水线 | B2B 任务依次为 创建 → 鉴权 → 冻结额度 → 执行 → 轮询 `/tasks/get` 或 `/tasks/get_result` → webhook 回调；"The selected worker calls internal or external generation capability and stores task output" | [B2B API 控制台](https://kusart.com/api-for-business) |
| API 鉴权与计费 | "All B2B routes use the X-API-Key header"；"Legacy keys with billing_account_id use that dedicated credit account. New user-scoped keys freeze from the user credit pool"；余额不足返回代码 `42002` | [B2B API 控制台](https://kusart.com/api-for-business) |
| 额度账本 | 每日免费额度、订阅额度、不过期的额度包、容量加购，以及执行前的额度冻结 | [服务条款](https://kusart.com/terms)、[B2B API 控制台](https://kusart.com/api-for-business) |
| 风格目录与推荐 | 带使用计数与分类的编号风格预设，由 `api.kusa.pics` 提供；存档的团队页把 "advanced art style recommendation systems, unlimited art style models, character consistency features" 描述为在研 | [kusart.com](https://kusart.com/)、[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| LoRA 训练 | 用户上传数据集、数据集审阅，以及针对 Anima 模型的受控训练参数 | [train-lora](https://kusart.com/train-lora) |
| 审核 | "automated filtering mechanisms, keyword filters, image moderation tools, account risk signals"，适用于提示词、上传内容、参考图与产出 | [服务条款](https://kusart.com/terms) |
| 社区与分享 | 面向非订阅用户内容的公开画廊与信息流、梗图与风格库，以及面向订阅用户的隐私模式开关 | [服务条款](https://kusart.com/terms)、[kusart.com](https://kusart.com/) |

### 数据处理（依文档记载）

隐私政策很短。它说公司收集账号信息、生成内容（"We store content generated by users, such as images created through our AI models"）、包含 IP 地址在内的使用数据，以及 cookie 数据；称不会 "sell your personal data"；并说明会与服务商及支付处理方共享数据，向后者传递 "payment amount, currency, and transaction ID"（[隐私政策](https://kusart.com/privacy)；生效于 2025 年 1 月）。

条款补充说明：非订阅用户的内容与提示词默认可能被公开展示；使用分享功能时，用户授予 "a non-exclusive, worldwide, royalty-free license to display, host, reproduce, and distribute your shared content within the community areas of our platform and related promotional surfaces"；服务可能依赖 "AI infrastructure providers"，但一个都没点名（[服务条款](https://kusart.com/terms)）。两份文件中都没有找到留存期限、子处理者清单、GDPR／CCPA 权利条款，也没有关于用户内容是否用于训练自有模型的表述 —— 见 `备注`。

### 招聘所需技术背景

`kusart.com` 上不存在招聘页、职位发布或招聘渠道（路径探测于 2026-08-21）。唯一能找到的岗位描述是存档官网上的三条团队条目，其中提到的工作内容包括风格推荐、"unlimited art style models"、角色一致性，以及规划中的 "Omni architecture models"（[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。

### 行业领域

工作范围涵盖扩散模型的图像生成与微调（LoRA 训练、风格预设、角色一致性）、Booru 标签等二次元社群惯例、通过离岸分销方进行的消费级订阅与额度计费、覆盖八种语言约 160 个索引页面的多语种 SEO，以及面向用户生成角色作品的内容审核 —— 包括条款中写入的年龄表现规则与肖像限制（[sitemap](https://kusart.com/en/sitemap.xml)、[服务条款](https://kusart.com/terms)、[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | `kusart.com` 上未找到 | 路径探测于 2026-08-21 |
| 自述的团队构成 | "an international team"，其研发与市场成员 "with backgrounds from the US and Japan" | [kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| 办公地点 | 只公布了威尔明顿（特拉华州）的一个邮箱地址（PMB）；没有点名任何实际办公地点 | [服务条款](https://kusart.com/terms)、[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| 人数、薪资、远程政策、福利、招聘流程 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-08-21）：`kusart.com` 首页、`/terms`、`/privacy`、`/contact`、`/faq`、`/blog`、`/credits`、`/api-for-business`、`/train-lora`、`/nano-banana`、`/image-generator/*`、`/events/*`、`robots.txt`、`sitemap.xml` 与英文语言版 sitemap（159 个 URL）；对 `/pricing`、`/about`、`/company`、`/legal`、`/companyprofile` 的探测；页面的网络请求、脚本来源与 Firebase 配置；`kusart.com` 与 `kusa.pics` 的 WHOIS；`kusart.com`、`kusa.pics` 与 `kazama.inc` 的互联网档案 CDX 索引与带日期抓取；`api.kusa.pics`；Discord invite API、Instagram、X 与 YouTube 账号；苹果 App Store；两个域名的 Similarweb；Crunchbase；以及针对 KusArt、KusaPics、KAZAMA INC.、Kamaza Inc. 与具名团队成员的中英文检索。

- **定价。** 不存在公开价目表：页头 "Pricing" 链接指向页面上并不存在的 `#pricing` 锚点，`/pricing` 返回 HTTP 404，未登录访问 `/credits` 会被跳走。公开的只有条款里的额度／订阅*结构*。
- **任何用户、订阅、营收或生成总量数字。** 两个品牌下公司都未公布；站点上唯一的数量是各风格的使用计数。
- **公司登记。** 未取得 "KAZAMA INC." 或 "Kamaza Inc." 的任何备案；给出的特拉华州地址是一个 PMB 邮箱，而非实际办公地点。
- **由哪个主体收款、经由哪家处理方。** Sygnal E-commerce Limited 被点名为"授权分销方"却未解释这一安排，两份政策中也都没有点名任何支付处理方。
- **用户内容是否被用于训练模型。** 条款与隐私政策都未表态，也没有描述任何退出方式。
- **数据留存、子处理者与法定权利。** 隐私政策没有规定留存期限、没有点名任何子处理者，也没有 GDPR 或 CCPA 权利条款。
- **产品背后的模型。** 只有营销名称（Kusa-XL、Kusa-Easy、Kusa-Anima、Kusa-Mix、Kusa-Niji）与一句笼统的 "diffusion models … enhanced with proprietary modules"；没有点名任何基础模型、供应商、托管区域或算力合作方，对站点上暴露的第三方模型也是如此。
- **团队规模与当前人员。** 三个具名岗位来自一个现已下线的官网；线上产品站点一个人都没具名。
- **除所称种子前轮之外的融资。** 没有更晚轮次的说法，也未找到投资方公告；iSeed Ventures 的参与未从投资方一侧得到确认。
- **2026-08-21 无法读取的来源：** `kazama.inc`（HTTP 404，改由互联网档案读取）、`kusart.com/credits` 与 `/manage-subscription`（需登录），以及 Crunchbase（需订阅）。

### 不同来源之间的不一致

- **公司把自己的名字写成两种。** 条款与隐私政策写 "KAZAMA INC."、域名是 `kazama.inc`，而官网的标题、正文与版权行都写 "Kamaza.Inc"（[服务条款](https://kusart.com/terms)、[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)）。
- **品牌与文件对不上。** 线上站点叫 KusArt，存档的官网却写 "Our flagship product KusaPics"，而 API 与 CDN 仍跑在 `kusa.pics` 上 —— 截至 2026-08-21，三个名字同时在用。
- **政策日期早于品牌本身。** 隐私政策标注 "Effective January 2025"，早于 `kusa.pics` 于 2025-03-01 的域名注册，也早于产品最早的存档抓取。
- **规模信号相差若干个数量级。** 线上某个风格的计数显示 "111.3M uses"，而 Similarweb 给出 `kusart.com` 2026 年 7 月只有 8.11 万次访问（[kusart.com](https://kusart.com/)、[Similarweb](https://www.similarweb.com/website/kusart.com/)）。计数是累计值，且品牌迁移期间部分流量仍留在 `kusa.pics`，但没有任何来源把两者对上。
- **投资方。** 公司自己的页面只点名 iSeed Ventures 领投；一条搜索结果摘要另加 Llama Ventures，该名字在存档页面中并不存在，也未获证实。
- **NSFW 定位。** 条款禁止付费功能被用于 "Adult content, pornographic services … or sexually explicit paid content"，并禁止对年龄模糊角色的性化描绘，而产品的公开风格分类与营销又主打 "waifu／husbando" 角色生成；没有任何页面说明审核界线在实践中划在哪里。

### 其他

- **一次迁移到买来域名上的品牌更替。** 2025 年 7 月 `kusart.com` 仍在 PerfectDomain 上挂售，那时产品已以 KusaPics 之名在 `kusa.pics` 上线约两个月；到 2026 年 8 月，该域名承载产品，`kusa.pics` 跳转过去，同时继续承载 API 与 CDN（[Wayback，2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/)；2026-08-21 的观察）。
- **公开表面偏重 SEO。** 仅英文 sitemap 就列出 159 个 URL，其中约 30 个是单一用途的 "Play" 生成器，还有一大块是梗图库与风格页，并在八种语言下复制（[sitemap](https://kusart.com/en/sitemap.xml)）。
- **产品还在迭代，官网却下线了。** `kazama.inc` 迟至 2026-02-17 的抓取时仍在线，如今返回 Vercel 的 "DEPLOYMENT_NOT_FOUND"，把关于融资与团队的唯一公开表述一并带走（[kazama.inc 存档](https://web.archive.org/web/20260217050446/https://kazama.inc/)；检查于 2026-08-21）。
- **一个没有公开定价的产品，却有文档化的 B2B API。** `/api-for-business` 控制台公布了鉴权头、响应信封、错误码、额度冻结行为与 webhook 流程，而面向消费者的套餐本身在任何公开位置都查不到（[B2B API 控制台](https://kusart.com/api-for-business)）。
- **比赛是可见的获客渠道：** Seedance 2.0 视频比赛于 2026-05-07 至 2026-06-20 举行，"Anima AI Creative Contest" 则宣传 "3M credits + $10,000 prize pool"（[events/seedance-2](https://kusart.com/events/seedance-2)、[kusart.com](https://kusart.com/)）。
- **受众集中在站外。** Instagram 有 6.4 万粉丝，而 Discord 只有 637 名成员、实测网站流量也不大，说明品牌的触达主要在社交平台而非站点本身（数字观察于 2026-08-21）。

---

## 资料来源

**官方**

- [kusart.com](https://kusart.com/) · [FAQ](https://kusart.com/faq) · [博客](https://kusart.com/blog) · [联系页](https://kusart.com/contact)
- [服务条款](https://kusart.com/terms)（最后更新 2026 年 4 月） · [隐私政策](https://kusart.com/privacy)（生效于 2025 年 1 月）
- [B2B API 控制台](https://kusart.com/api-for-business) · [LoRA 训练](https://kusart.com/train-lora) · [Anima 模型页](https://kusart.com/image-generator/kusa-anima) · [Nano Banana](https://kusart.com/nano-banana) · [Seedance 2.0 比赛](https://kusart.com/events/seedance-2)
- [robots.txt](https://kusart.com/robots.txt) · [sitemap 索引](https://kusart.com/sitemap.xml) · [英文 sitemap](https://kusart.com/en/sitemap.xml)
- 社交 —— [Instagram @kusart_official](https://www.instagram.com/kusart_official/) · [X @kusart_official](https://x.com/kusart_official) · [YouTube @KusArt_neko](https://www.youtube.com/@KusArt_neko) · [Discord](https://discord.gg/XwxZaKSUzz) · [Discord invite API 记录](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true)
- 存档的官网 —— [kazama.inc，抓取于 2026-02-17](https://web.archive.org/web/20260217050446/https://kazama.inc/)（线上地址 2026-08-21 返回 HTTP 404）
- 存档的旧品牌 —— [kusa.pics 时期的 KusaPics，2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/) · [kusa.pics，2026-02-01](https://web.archive.org/web/20260201015926/https://kusa.pics/) · [挂售中的 kusart.com，2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/)

**第三方档案**

- [Similarweb —— kusart.com](https://www.similarweb.com/website/kusart.com/) · [Similarweb —— kusa.pics](https://www.similarweb.com/website/kusa.pics/)
- [Crunchbase —— Kazama（需订阅）](https://www.crunchbase.com/organization/kazama)
- [Apple iTunes 搜索 API —— 美国区无第一方应用](https://itunes.apple.com/search?term=kusart&entity=software&country=us&limit=5)
