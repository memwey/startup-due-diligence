# CrushOn AI

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-14。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-14。英文版为原始版本。

## 摘要

CrushOn AI 是 `crushon.ai` 上一个仅限成年人的角色聊天服务，页面标题为 "CrushOn AI - No Filter NSFW Character AI Chat - Spicy AI GF"，用户创建 AI 角色并与之聊天，按月消耗消息额度的订阅制收费（[官网](https://crushon.ai/)；访问于 2026-08-14）。该服务在不到三年里，在自己的文件中先后写过四种运营主体：2025 年初之前完全不署主体，之后是华盛顿州贝尔维尤的 `Crushon AI Corp.`，再之后是不列颠哥伦比亚省温哥华的 `CRUSHON AI INC.`，2025 年年中起变为塞浦路斯公司 `TECHIEPIE LTD`（注册于 2025-03-19）（[存档页脚](https://web.archive.org/web/20250306123450/https://crushon.ai/terms-of-service)、[服务条款](https://crushon.ai/terms-of-service)；最后修订 2025-07-22）—— 见 `品牌与法律实体`。

- 条款写明 "The Service is provided by TECHIEPIE LTD, a company registered in Cyprus"，而适用法律条款写的是 "the Service shall be deemed solely based in Hong Kong"，并 "governed by and construed in accordance with the laws of the HK"；页脚还额外挂了一个特拉华州地址（[服务条款](https://crushon.ai/terms-of-service)；最后修订 2025-07-22）。
- 定价是七档消息额度订阅：免费档每月 100 额度，付费档每月 5.99 至 199.99 美元（按年为 58.88 至 1,799.99 美元），对应每月 2,000 至 125,000 额度，另有 "Pro Models" 聊天包加购（[定价页](https://crushon.ai/pricing)；2026-08-14 在浏览器中读取）。
- 公司在站点任何位置都没有公布用户数、营收或角色数量。可独立观察的数字只有官方 Discord —— 71,491 名成员、6,755 人在线（[Discord invite API](https://discord.com/api/v10/invites/crushonai?with_counts=true)；观察于 2026-08-14）—— 以及 Similarweb 的公开档案，其 2026 年 7 月口径显示 2,240 万次访问、全球排名第 1,512（[Similarweb](https://www.similarweb.com/website/crushon.ai/)）。
- 不存在任何融资公告。[Tracxn](https://tracxn.com/d/companies/crushon-ai/__Q35HFbL4EOKKbeaPG1IMIImXSmSm5PMMERN6lpfOev8) 称 "Crushon AI has not raised any funding yet"，而 [StartupHub.ai](https://www.startuphub.ai/investment_rounds/crushonai-funding-round-2026) 断言 2026-04-29 有一笔 1,500 万美元融资，却没有给出任何来源 —— 见 `融资`。
- 工程方面的证据完全来自实际加载的应用：Next.js App Router 置于 Cloudflare 机器人防护之后，自建 Sentry、自建 GrowthBook 特性开关、自建 SensorsData 埋点端点；隐私政策写明 "We may use User Content to train AI models"，且未点名任何模型供应商（页面资源检查于 2026-08-14）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | CrushOn AI / CrushOn.AI；页面标题 "CrushOn AI - No Filter NSFW Character AI Chat - Spicy AI GF" | [官网](https://crushon.ai/)；访问于 2026-08-14 |
| 自我描述 | meta description："Dive into NSFW Character AI chats without filters. Experience genuine, unrestricted NSFW AI interactions with Juicy AI characters - Your Spicy AI Girlfriend" | [官网](https://crushon.ai/)；访问于 2026-08-14 |
| 当前运营主体 | "The Service is provided by TECHIEPIE LTD, a company registered in Cyprus"；页脚写 "© 2025 TECHIEPIE LTD. All Rights Reserved" | [服务条款](https://crushon.ai/terms-of-service)；最后修订 2025-07-22 |
| 塞浦路斯登记信息 | TECHIEPIE LTD，注册号 HE 472689，注册于 2025-03-19，状态 Active，私人有限公司；董事与秘书均列为 Christiana Magniti | [i-Cyprus 登记镜像](https://i-cyprus.com/company/654032)；访问于 2026-08-14 |
| 页脚给出的地址 | "Strovolou 77, STROVOLOS CENTER, Flat/Office 301, Strovolos, 2018, Nicosia, Cyprus" 与 "8 THE GREEN STE A DOVER, DE 19901" | [服务条款](https://crushon.ai/terms-of-service)；访问于 2026-08-14 |
| 适用法律 | "you agree that the Service shall be deemed solely based in Hong Kong … These Terms of Service and any separate agreements whereby we provide you shall be governed by and construed in accordance with the laws of the HK" | [服务条款](https://crushon.ai/terms-of-service) |
| 域名注册 | `crushon.ai` 注册于 2023-05-26（GoDaddy）；WHOIS 的 "Registrant Organization" 至今仍写 "CRUSHON AI CORP." | WHOIS 读取于 2026-08-14 —— 见 `备注` |
| 文件日期 | 服务条款 "Last modified July 22, 2025"；隐私政策 "Last modified March 6, 2025"；2257 声明 "Last Updated: Feb 8, 2025" | [服务条款](https://crushon.ai/terms-of-service)、[隐私政策](https://crushon.ai/privacy-policy)、[2257 声明](https://crushon.ai/2257) |
| 年龄政策 | "Crushon is available only to users 18 and older"；"You affirm that You are more than 18 years of age"。2026-08-14 在浏览器中打开站点时没有出现任何年龄验证步骤 —— 准入完全依赖用户自我声明 | [社区准则](https://crushon.ai/community-guidelines)、[服务条款](https://crushon.ai/terms-of-service) |
| 已发布的政策 | 服务条款、隐私政策、社区准则、内容移除政策、投诉政策、18 U.S.C. 2257 合规声明、联盟计划 | [站点页脚](https://crushon.ai/terms-of-service)；访问于 2026-08-14 |
| 支付令牌化 | "Crushon uses Basis Theory, a third-party service provider for payment tokenization" | [服务条款](https://crushon.ai/terms-of-service) |
| 社区 | Discord 服务器 "CrushOn AI"（guild id `1113353675927212074`）：约 71,491 名成员、6,755 人在线；站点上唯一的 "Contact Us" 链接指向它 | [Discord invite API](https://discord.com/api/v10/invites/crushonai?with_counts=true)；观察于 2026-08-14 |
| 联盟计划 | 通过 Google 表单运行，而非第一方页面 | [联盟申请表](https://docs.google.com/forms/d/e/1FAIpQLScro_QKiXXbUf3qA_pv5QkLLiJdwxqKAJt1NCb3ZzUMkstgkA/viewform)；访问于 2026-08-14 |
| 移动应用 | 条款提到 "the Crushon mobile application … provided through Apple's App Store or the Google Play Marketplace"，但 2026-08-14 在两家美国商店中都未找到第一方 CrushOn 应用 | [iTunes 搜索 API](https://itunes.apple.com/search?term=crushon&entity=software&country=us&limit=5)、[Google Play 搜索](https://play.google.com/store/search?q=crushon&c=apps&hl=en&gl=US) |
| 团队、人数、办公地点 | 站点上任何位置都未公布 | 见 `备注` |
| 开源 | `crushon`、`crushonai` 名下均无 GitHub 组织；npm 上没有 "crushon" 相关包 | API 检查于 2026-08-14 |

**服务上线时间**：域名注册于 2023-05-26，官方 Discord 服务器的 guild id 对应 2023-05-31，站点最早的互联网档案抓取是 [2023-06-03](https://web.archive.org/web/20230603004309/https://crushon.ai/)，站点又在 2026 年 6 月办过 "3rd anniversary" 页面 —— 四个互相独立的标记都指向 2023 年 6 月前后上线（WHOIS 与 Discord 读取于 2026-08-14）。

### 品牌与法律实体

站点自有文件中署名的运营主体，在 2025 年 2 月到 8 月之间换了三次。下表每一行都取自站点自身页脚或条款的带日期存档。

| 观察日期 | 站点上署名的主体 | 给出的地址 | 来源 |
|---|---|---|---|
| 2024-11-04 与 2025-01-24 | 无 —— 条款只写 "provided by Crushon"，标注 "Last modified September 25, 2023" | 页脚无地址 | [条款存档，2024-11-04](https://web.archive.org/web/20241104142659/https://crushon.ai/terms-of-service) |
| 2025-03-06 | "© 2025 Crushon AI Corp." | 3120 139th Ave SE, Bellevue, WA 98005 | [条款存档，2025-03-06](https://web.archive.org/web/20250306123450/https://crushon.ai/terms-of-service) |
| 2025-03-28 | "© 2025 CRUSHON AI INC." | 329 HOWE ST UNIT 626, VANCOUVER BC V6C 3N2, CANADA | [2257 声明存档，2025-03-28](https://web.archive.org/web/20250328101207/https://crushon.ai/2257) |
| 2025-08-02 至 2026-08-14 | "© 2025 TECHIEPIE LTD" | Strovolou 77, Strovolos Center, Flat/Office 301, Strovolos 2018, Nicosia, Cyprus；以及 8 The Green Ste A, Dover, DE 19901 | [条款存档，2025-08-02](https://web.archive.org/web/20250802153204/https://crushon.ai/terms-of-service)、[现行条款](https://crushon.ai/terms-of-service) |

另有一个站点 `crushonai.com` 把 "Crushon AI Corp." 呈现为 "a software consulting and go-to-market studio based in Washington, US"，其总部写作 "3120 139th Ave SE Suite 500, Bellevue, WA 98005" —— 与 2025 年 3 月 CrushOn 页脚中出现的是同一个街道地址 —— 并称自己 "supported fast-growing startups and indie founders building tools in the AI, chatbot, and healthcare tech spaces — including platforms with over 1M+ monthly users"（[crushonai.com](https://crushonai.com/)；无日期，页脚写 "© Crushon AI Corp. 2025"；访问于 2026-08-14）。

未取得任何能确立 `Crushon AI Corp.`（华盛顿州）、`CRUSHON AI INC.`（不列颠哥伦比亚省）与 `TECHIEPIE LTD`（塞浦路斯）三者关系的文件，上述任一站点也没有任何公司页或公告解释这些更替 —— 见 `备注`。

---

## 产品

### 是什么

CrushOn AI 是一个角色聊天平台：用户创建角色，与自己或他人创建的角色聊天，并为消息容量付费。导航包含 Home、Recent Chats、Create、Rankings、Profile、Pricing、Store、Bonus 与 Notifications（[官网](https://crushon.ai/)；访问于 2026-08-14）。条款把它描述为 "a generative artificial intelligence (AI) chat functionality"，并写明 "The basic Service is free to use for customers and message credits can be purchased for full use"（[服务条款](https://crushon.ai/terms-of-service)）。

### 定价页所描述的功能面

| 方面 | 各档位的差异 | 来源 |
|---|---|---|
| 模型接入 | 三档模型 —— "Free Models"（所有档位无限使用）、"Pro Models" 与 "Ultra Models"（消耗额度；免费档无法使用 Ultra）。没有点名任何模型或供应商 | [定价页](https://crushon.ai/pricing)；读取于 2026-08-14 |
| 消息长度 | "Maximum AI Message Length" 按档位从 225 到 550 字符；从 Luxe 档起才可调节 | [定价页](https://crushon.ai/pricing) |
| 记忆 | 免费档 "8K Memory"，Standard 起 "16K Memory Models"，Elite 为 "24K Memory Models"；每个角色 200 至 1,000 条历史消息；每个会话可置顶 4,000–6,000 字符；低／中／高频 "Auto Summary" 以及 "Resummarize" 功能 | [定价页](https://crushon.ai/pricing) |
| 聊天留存 | 免费档："Chat History will be deleted after 7 days of inactivity"。付费档："Chat History is kept during the Membership Period" | [定价页](https://crushon.ai/pricing) |
| 并发与容量 | 每个角色并发会话数 1 到 15；免费档使用 "Shared Chat Capacity (Responses may be slower during Peak Time)"，付费档为 "Dedicated Chat Capacity with Basic Priority" | [定价页](https://crushon.ai/pricing) |
| 其他功能 | 群聊（"Unique Model with 8K Memory"，免费档不可用）、语音消息与自定义语音位（1 到 10 个以上）、每日 "Inspiration Replies"（20 到 250）、资料卡、额外聊天气泡 | [定价页](https://crushon.ai/pricing) |
| 创作者变现 | 上传角色的用户 "can become Creators and receive rewards from other users"；打赏完全自愿，公司保留暂停结算与撤销打赏的权利 | [服务条款](https://crushon.ai/terms-of-service) |

### 商业化

下列价格于 2026-08-14 在浏览器中从实时定价页读取。页面提供月付与年付切换，页面顶部对年付标注 "47% Off"。

| 套餐 | 月付 | 年付（折合每月／每年，划线价） | 每月消息额度 |
|---|---|---|---|
| Free | 0 美元 | —— | 100 |
| Standard | 5.99 美元 | 4.90 美元／58.88 美元（划线价 79.88 美元） | 2,000 |
| Premium | 14.99 美元（划线价 19.99 美元） | 7.90 美元／94.88 美元（划线价 178.88 美元） | 6,000 |
| Luxe（"Most Popular"） | 39.99 美元 | 25.00 美元／299.99 美元（划线价 479.88 美元） | 20,000 |
| Deluxe | 标注 "Retired" | 标注 "Retired" | —— |
| Elite | 89.99 美元 | 66.70 美元／799.99 美元（划线价 1,079.88 美元） | 55,000 |
| Imperial | 199.99 美元 | 150.00 美元／1,799.99 美元（划线价 2,399.88 美元） | 125,000 |

| 项目 | 内容 | 来源 |
|---|---|---|
| 加购：Pro Models 聊天包 | "Unlimited access to Pro Models"，30 天 39.99 美元或一年 299.99 美元（显示为每月 24.99 美元，划线价每年 479.88 美元）；"works alongside any membership and doesn't consume your Monthly or Bonus credits" | [定价页](https://crushon.ai/pricing)；读取于 2026-08-14 |
| 套装 | "Ultimate Bundle"：Premium 一年 + 聊天包 365 天 394.88 美元（划线价 658.76 美元）；Luxe 一年 + 聊天包 599.98 美元（划线价 959.76 美元） | [定价页](https://crushon.ai/pricing) |
| 其他可购项 | "CrushOn Coins"、"CrushOn Diamonds"、"message quota"、"Message Credit Capacity Expansion" 以及 "Store" 版块；按档位提供 5%–20% 的额度购买折扣 | [隐私政策](https://crushon.ai/privacy-policy)、[定价页](https://crushon.ai/pricing) |
| 计费 | "Subscription fees are automatically charged to your selected payment method on a recurring monthly basis"；取消路径为 Profile → My Subscription → Manage → Cancel Subscription，在当期结束时生效 | [服务条款](https://crushon.ai/terms-of-service) |
| 退款 | "We will not issue refunds of usage fees"；"We do not offer partial refunds or credits for unused time, mid-cycle cancellations, or downgrades"；用户同意除欺诈外不发起拒付 | [服务条款](https://crushon.ai/terms-of-service) |
| 计费支持渠道 | "please click here to submit a ticket on Discord" | [服务条款](https://crushon.ai/terms-of-service) |
| 支付处理 | 由 Basis Theory 做令牌化；"We do not store your Financial Data" | [服务条款](https://crushon.ai/terms-of-service)、[隐私政策](https://crushon.ai/privacy-policy) |

### 公开披露的规模变化

公司自身不公布任何规模数字。下列内容要么是可观察的计数，要么是第三方估算，并已相应标注。

| 日期 | 数字 | 来源 |
|---|---|---|
| 2023-05-26 | `crushon.ai` 域名注册 | WHOIS 读取于 2026-08-14 |
| 2023-06-03 | 站点最早的互联网档案抓取 | [Wayback 存档](https://web.archive.org/web/20230603004309/https://crushon.ai/) |
| 2026-06 | 站点上线 "3rd anniversary" 页面与抽奖 | [Wayback 存档，2026-06-15](https://web.archive.org/web/20260615214222/https://crushon.ai/3rd-anniversary) |
| 2026 年 7 月口径 | Similarweb 公开档案：2,240 万次访问，全球排名 #1,512，美国排名 #1,648，跳出率 30.92%，每次访问 12.71 页，平均停留 13 分 25 秒；国家分布美国 26.5%、德国 5.48%、加拿大 5.2%、法国 4.78%、俄罗斯 3.81%；直接流量 66.95% | [Similarweb](https://www.similarweb.com/website/crushon.ai/)；访问于 2026-08-14 |
| 观察于 2026-08-14 | Discord 服务器：约 71,491 名成员、6,755 人在线 | [Discord invite API](https://discord.com/api/v10/invites/crushonai?with_counts=true) |
| 访问于 2026-08-14 | 第三方数据库：成立于 2024 年，门洛帕克，"unfunded" | [Tracxn](https://tracxn.com/d/companies/crushon-ai/__Q35HFbL4EOKKbeaPG1IMIImXSmSm5PMMERN6lpfOev8)（页面最后更新 2026-06-26） |

有若干聚合站点发布过看起来很精确的 CrushOn AI 用户、营收与消息量数字。所查阅的这些页面都没有引用一手来源，且彼此矛盾 —— 见 `备注`。

### 已公布的内容规则

社区准则设定的规则，与页面标题上 "No Filter NSFW" 的定位并存（[社区准则](https://crushon.ai/community-guidelines)；经[存档，2026-07-16](https://web.archive.org/web/20260716045138/https://crushon.ai/community-guidelines)读取）：

- **年龄：** "Crushon is available only to users 18 and older."
- **内容中的未成年人：** "Do not create or depict characters who are minors or whose age is not clearly defined as over 18. This includes 'aged-up' characters, originally depicted as minors in source material. Realistic or human-like depictions of underage characters, even if fictional, are strictly prohibited."
- **真实人物：** "Do not post real images or overly realistic AI-generated images of any individuals … to protect individual privacy and prevent the misuse of someone's likeness without consent"；未经同意冒充真实个人被列为可移除内容。
- **性相关图像：** "Avoid depicting explicit sexual activity and stimulation. Implied sexual activity is permitted when contextually appropriate (medical, educational, fictional representation)."
- **违法活动：** "Do not use the Crushon Service to engage in or promote illegal activities, including commercial sexual activity, trafficking, or pornography."
- **其他禁止项：** 仇恨言论（含 "idolization of hate figures"）、可能引发迫在眉睫暴力的错误信息、人肉搜索、账号劫持、垃圾信息、列举的恋物内容、兽交、血腥暴力与威胁。

2257 声明主张该服务不适用美国记录保存要求，理由是 "our website does not depict actual human beings engaged in real sexually explicit conduct"、所有内容 "is exclusively generated by artificial intelligence"、用户不能上传真人图像，以及 "The content created from this website contains only text generated based on AI and does not contain images or videos"（[2257 声明](https://crushon.ai/2257)；最后更新 2025-02-08）。

---

## 创始人

`crushon.ai` 上任何位置都没有具名的创始人、高管或员工：没有关于页、团队页、管理层页或新闻页，唯一面向人的联系渠道是一个 Discord 服务器（站点导航与页脚查阅于 2026-08-14）。

在任何一手记录中找到的唯一具名个人来自塞浦路斯登记：TECHIEPIE LTD 的董事与秘书均列为 **Christiana Magniti**，股东信息在公开镜像上被隐去（[i-Cyprus](https://i-cyprus.com/company/654032)；访问于 2026-08-14）。所查阅的来源中没有一处把这个名字与产品研发联系起来，也未取得更早两个主体在不列颠哥伦比亚省或华盛顿州的登记文件 —— 见 `备注`。

---

## 融资

截至 2026-08-14，在所查阅的公开来源中未找到公司发布的任何融资公告。站点没有新闻页、投资人页或公司页，运营主体换了三次也没有任何配套说明。

| 日期 | 说法 | 金额 | 具名投资方 | 来源 |
|---|---|---|---|---|
| 访问于 2026-08-14（页面最后更新 2026-06-26） | "Crushon AI has not raised any funding yet"；"an unfunded company based in Menlo Park (United States), founded in 2024" | 无 | 无 | [Tracxn](https://tracxn.com/d/companies/crushon-ai/__Q35HFbL4EOKKbeaPG1IMIImXSmSm5PMMERN6lpfOev8) |
| 声称公布于 2026-04-29 | 一笔 "$15M" 融资，地点旧金山 | 1,500 万美元 | 页面未点名 | [StartupHub.ai](https://www.startuphub.ai/investment_rounds/crushonai-funding-round-2026) —— 该页未引用任何新闻稿、备案或其他来源 |
| 访问于 2026-08-14 | 存在档案，但需订阅才能查看 | —— | —— | [PitchBook](https://pitchbook.com/profiles/company/1458847-81)、[Crunchbase](https://www.crunchbase.com/organization/crushon-ai) |

两个数据库的立场直接互相否定，且都未与一手来源核对过。股权结构、估值、营收以及与任何投资方的关系，在所查阅的来源中均未确立。

---

## 工程

### 技术栈与平台

公司未发布技术栈说明页。以下条目均于 2026-08-14 在浏览器中从实际加载的应用及其网络请求中确认。

- **前端：** Next.js App Router —— chunk 路径形如 `_next/static/chunks/app/[locale]/(dashboard)/…`，表明是带语言分段的 App Router 构建；静态资源由 `static.crushon.ai` 与 `cdn.crushon.ai` 提供。
- **边缘与机器人防护：** 整站置于 Cloudflare 的交互式质询之后 —— 2026-08-14 对 `crushon.ai` 的所有自动化请求都返回 HTTP 403 并带 `cf-mitigated: challenge`，连 `robots.txt` 允许的路径也不例外；页面加载 `static.cloudflareinsights.com`。
- **错误追踪：** 自建 Sentry，位于 `sentry.crushon.ai`，接收来自 `sentry.javascript.nextjs/7.120.4` 的上报。
- **特性开关与实验：** 自建 GrowthBook，位于 `growthbook-api.crushon.ai`，页面加载时拉取两份 SDK 特性配置；埋点数据里带有 `banner_download_experiment`、`search_overlay_transition`、`abtest_world_card_home_transition` 等实验键。
- **产品分析：** 自建 SensorsData 端点 `sensor.crushon.ai`，加载 `sensors/sensorsdata.min.js`（SDK 版本 1.26.5）并向 `sensor.crushon.ai/sensors/ue` 上报事件；此外还有 Google Analytics 与 Google Tag Manager。
- **登录方式：** Google Identity Services（`accounts.google.com`）；隐私政策补充称会从 "Apple, Google, Discord and Line" 这些第三方平台登录中接收个人信息。
- **联盟追踪：** Rewardful（`r.wdfl.co`）。
- **支付：** 由 Basis Theory 做卡片令牌化；定价页在 "Pay with Credit / Debit Card" 之外还提供 "Other Payments"。
- **模型层：** 产品对外暴露 "Free"、"Pro"、"Ultra" 三档模型以及 8K／16K／24K 记忆档，但没有任何页面或政策点名模型、供应商或托管区域。
- **没有公开代码：** `crushon`、`crushonai` 名下均无 GitHub 组织，npm 上也没有匹配 "crushon" 的包（API 检查于 2026-08-14）。

### 系统

| 系统 | 做什么 | 来源 |
|---|---|---|
| 角色创建与目录 | 用户创建角色，他人发现并与之聊天；Rankings 页面对其排序 | [官网导航](https://crushon.ai/)、[服务条款](https://crushon.ai/terms-of-service) |
| 额度计量 | 按档位分配每月消息额度，由 Pro 与 Ultra 模型的消息消耗；另有容量扩充、充值包与按档位的购买折扣 | [定价页](https://crushon.ai/pricing) |
| 会话记忆与摘要 | 分档上下文窗口、每角色历史消息上限、置顶文本，以及自动摘要与手动 "Resummarize" | [定价页](https://crushon.ai/pricing) |
| 语音生成 | 语音消息、"unlimited AI voice replies" 与按档位的自定义语音位，另有 "Up to 70% off on PRO voice generation" | [定价页](https://crushon.ai/pricing) |
| 群聊 | 面向多角色会话的独立 "Unique Model with 8K Memory"，仅付费档可用 | [定价页](https://crushon.ai/pricing) |
| 创作者打赏 | 对角色创作者的打赏，由公司控制资格、结算频率，并可撤销打赏 | [服务条款](https://crushon.ai/terms-of-service) |
| 审核与下架 | 内容移除政策、投诉政策、产品内举报工具，以及声明的 "review and take action, including limiting or terminating a user's access" 能力 | [社区准则](https://crushon.ai/community-guidelines)、[站点页脚](https://crushon.ai/terms-of-service) |
| 实验 | 埋点数据中可见由 GrowthBook 驱动的 A/B 实验，包括应用下载横幅的分组 | 页面资源检查于 2026-08-14 |

### 数据处理（依文档记载）

隐私政策写明聊天内容会以聚合方式用于模型训练："For all contents generated from the chat, we will only use such contents in a general way for training our models and we will not link chat contents to specific users."。同一文件在别处的表述更宽："We may use User Content to train AI models, as well as for our Business Purposes"，针对聊天则写 "We may use User Content from character chats to train AI models"（[隐私政策](https://crushon.ai/privacy-policy)；最后修订 2025-03-06）。文中没有描述任何训练退出机制。

留存期限是开放式的："We retain Personal Information for so long as it is reasonably necessary to achieve the relevant purposes described in this Policy, or for so long as is required by law"，未给出具体期限（[隐私政策](https://crushon.ai/privacy-policy)）。在产品层面，免费档聊天记录 "after 7 days of inactivity" 删除，付费档则 "kept during the Membership Period"（[定价页](https://crushon.ai/pricing)）。

政策点名了 Google Analytics 与 Google Tag Manager，描述了来自 Apple、Google、Discord 与 Line 登录的数据，并把 GDPR 与英国数据保护法列入适用法律；但未点名任何云服务商、模型供应商或其他子处理者。年龄下限设为 18 岁，并称公司 "does not knowingly collect any Personal Information about or market to children, minors, or anyone under the age of 18"（[隐私政策](https://crushon.ai/privacy-policy)）。

条款为公司赋予了对用户提交内容的宽泛权利，并包含集体诉讼弃权、传票成本转嫁（"If Crushon has to provide information in response to a subpoena related to Your account, then we may charge You for our costs"）以及出口管制合规义务（[服务条款](https://crushon.ai/terms-of-service)）。

### 招聘所需技术背景

`crushon.ai` 上未找到招聘页、职位发布或招聘渠道（2026-08-14 探测路径；所有请求都返回 Cloudflare 质询，在浏览器渲染出的站点导航与页脚中也没有招聘链接）。关于工程团队及其规模、所在地或工作语言，没有任何公开信息 —— 见 `备注`。

### 行业领域

工作处在消费级 LLM 产品与成人内容的交叉点：大规模的会话记忆与摘要、语音合成、额度计量与订阅计费、创作者变现，以及面向用户生成角色目录的内容审核。从公司自有文件可见的监管面包括 18 U.S.C. §2257 记录保存、GDPR 与英国数据保护、18 岁年龄下限、DMCA 式的知识产权通知，以及成人服务常见的支付网络约束 —— 最后一点体现在使用令牌化服务商和明确的反拒付条款上（[2257 声明](https://crushon.ai/2257)、[隐私政策](https://crushon.ai/privacy-policy)、[服务条款](https://crushon.ai/terms-of-service)）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | 未找到 | 2026-08-14 探测路径并查阅站点导航 |
| 办公地点 | 未公布任何实际办公地点；给出的地址是塞浦路斯注册办公地址与一个特拉华州地址 | [服务条款](https://crushon.ai/terms-of-service) |
| 人数、薪资、远程政策、福利、招聘流程 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-08-14）：`crushon.ai` 首页、`/pricing`、`/terms-of-service`、`/privacy-policy`、`/community-guidelines`、`/content-removal-policy`、`/complaints-policy`、`/2257` 与 `robots.txt`（既经互联网档案读取，也在浏览器中直接读取）；对 `/about`、`/blog`、`/contact`、`/careers`、`/jobs` 等路径的探测；页面的网络请求与脚本来源；`crushonai.com`；`crushon.ai` 的 WHOIS；2023-06 至 2026-07 的互联网档案 CDX 索引与带日期的抓取；Discord invite API；苹果与谷歌应用商店；GitHub 与 npm；塞浦路斯公司登记镜像；Tracxn、Crunchbase、PitchBook、StartupHub.ai 与 Similarweb；以及针对品牌名与各主体名的英文检索。

- **谁在经营这家公司。** 任何公司自有渠道上都没有具名的创始人、高管或员工。一手记录中唯一具名的人是塞浦路斯登记中 TECHIEPIE LTD 的董事兼秘书。
- **2025 年运营主体为何换了三次，以及这些主体之间的关系。** 从不署名到华盛顿州公司、再到不列颠哥伦比亚省公司、再到塞浦路斯公司，没有任何公告、备案或公司表述加以解释。未取得不列颠哥伦比亚省或华盛顿州的登记文件；塞浦路斯记录不公开披露股东。
- **公司口径的任何融资、营收、用户或消息数字。** 站点任何位置都没有公布 —— 没有新闻页、投资人页、使用量计数器，也没有角色数量口径。
- **产品背后的模型与基础设施。** "Free Models"、"Pro Models"、"Ultra Models" 这三档从未对应到具名模型、厂商或托管区域，条款与隐私政策也都未点名云服务商或推理供应商。
- **用户能否退出模型训练。** 隐私政策写明聊天内容用于训练模型，但没有描述任何退出方式。
- **具体的数据留存期限。** 政策只写 "for so long as it is reasonably necessary"。
- **除自我声明外的任何年龄核验机制。** 2026-08-14 在浏览器中打开时，站点直接进入内容目录，没有年龄验证步骤；条款依赖用户自行确认已满 18 岁。
- **第一方移动应用。** 条款描述了 App Store 与 Google Play 应用；2026-08-14 在两家美国商店中都未找到。
- **任何招聘页、技术博客、文档或开源存在。** 均未找到。
- **安全姿态。** 未找到安全页面、认证、子处理者清单、DPA、状态页或漏洞披露联系方式；隐私政策只承诺 "commercially reasonable security measures"。
- **2026-08-14 无法读取的来源：** `crushon.ai` 本身的自动化 HTTP 访问（Cloudflare 质询，HTTP 403 —— 本文中所有实时站点事实均在浏览器中或从互联网档案抓取中读取）；Crunchbase 与 PitchBook（订阅页）；Bizapedia 与 OpenGovUS（受限）。

### 不同来源之间的不一致

- **运营主体与域名注册人不一致。** 站点条款与页脚署名 TECHIEPIE LTD（塞浦路斯），而 `crushon.ai` 的 WHOIS 记录至今仍写 "Registrant Organization: CRUSHON AI CORP."（WHOIS 读取于 2026-08-14；[服务条款](https://crushon.ai/terms-of-service)）。
- **主体、适用法律与地址同时指向四个法域。** 一家塞浦路斯注册公司、页脚里的特拉华州地址、香港的法律选择与管辖约定，以及历史上的华盛顿州与不列颠哥伦比亚省主体（[服务条款](https://crushon.ai/terms-of-service)、各存档页脚）。
- **2257 声明与产品实际不一致。** 声明写 "The content created from this website contains only text generated based on AI and does not contain images or videos"，而社区准则为图片发布设了规则并禁止 "overly realistic AI-generated images of any individuals"，角色本身也带有头像图片（[2257 声明](https://crushon.ai/2257)、[社区准则](https://crushon.ai/community-guidelines)）。
- **"No Filter" 定位与已公布规则不一致。** 页面标题与 meta description 宣传 "No Filter NSFW" 与 "unrestricted NSFW AI interactions"，而社区准则禁止宣传 "pornography" 并要求用户 "Avoid depicting explicit sexual activity and stimulation"（[官网](https://crushon.ai/)、[社区准则](https://crushon.ai/community-guidelines)）。
- **成立年份与总部。** [Tracxn](https://tracxn.com/d/companies/crushon-ai/__Q35HFbL4EOKKbeaPG1IMIImXSmSm5PMMERN6lpfOev8) 写 2024 年与门洛帕克；而域名、Discord 服务器与最早的存档抓取都指向 2023 年 5–6 月，所查阅的来源中也没有一处把任何运营放在门洛帕克。
- **融资。** [Tracxn](https://tracxn.com/d/companies/crushon-ai/__Q35HFbL4EOKKbeaPG1IMIImXSmSm5PMMERN6lpfOev8) 称公司没有融过资；[StartupHub.ai](https://www.startuphub.ai/investment_rounds/crushonai-funding-round-2026) 称 2026-04-29 公布了 1,500 万美元且未引用任何来源。别处流传的聚合类"统计"页面给出的 ARR、月聊天量与市场份额等数字，无法追溯到任何一手来源且彼此矛盾，本文不予转述。
- **流量估算因厂商与口径差异很大。** Similarweb 公开档案在 2026 年 7 月口径下给出 2,240 万次访问（[Similarweb](https://www.similarweb.com/website/crushon.ai/)）；其他页面流传着更早期、更大的数字，且未说明口径。

### 其他

- **这个服务从外部异常难以观察。** Cloudflare 的交互式质询对所有自动化请求返回 HTTP 403，连 `robots.txt` 允许的路径也不例外，定价页又是客户端渲染 —— 因此存档抓取里的定价页只显示 "Loading"。本文所有实时数字都来自 2026-08-14 的真实浏览器会话。
- **几乎整套分析与可靠性组件都自建在公司自己的域名下** —— Sentry、GrowthBook 与 SensorsData 端点全部位于 `*.crushon.ai` 并置于 Cloudflare 之后，另外还有第三方的 Google Analytics 与 Google Tag Manager（页面资源检查于 2026-08-14）。
- **唯一的公开支持与联系渠道是 Discord。** 站点的 "Contact Us" 链接、计费支持指引与社区都指向 `discord.gg/crushonai`；联盟计划跑在 Google 表单上。
- **法律文件相对当前公司身份，一份偏新、两份偏旧。** 条款最后修订于 2025-07-22 并署名塞浦路斯主体，而隐私政策最后修订于 2025-03-06、2257 声明于 2025-02-08 —— 后者早于该塞浦路斯公司自身 2025-03-19 的注册日期，前者也与之相近。
- **更早一版条款曾原封不动挂了约一年半。** 2024-11 与 2025-01 的抓取都显示 "Last modified September 25, 2023" 且不署主体，随后才是 2025 年密集的主体更替（[条款存档，2024-11-04](https://web.archive.org/web/20241104142659/https://crushon.ai/terms-of-service)）。
- **页脚带有指向其他成人 AI 站点的交叉链接**，标签为 "AI Porn Chat"、"AI Sex Chat" 与 "Juicy Chat AI"；它们的跳转目标由客户端渲染，在所查阅的抓取中未能解析出目标 URL（[条款存档，2026-07-28](https://web.archive.org/web/20260728204653/https://crushon.ai/terms-of-service)）。

---

## 资料来源

**官方** —— 下列 `crushon.ai` 链接置于 Cloudflare 交互式质询之后，对自动化抓取返回 HTTP 403；在浏览器中可正常打开，其存档副本列在下方。

- [官网](https://crushon.ai/) · [定价页](https://crushon.ai/pricing) · [robots.txt](https://crushon.ai/robots.txt)
- [服务条款](https://crushon.ai/terms-of-service)（最后修订 2025-07-22） · [隐私政策](https://crushon.ai/privacy-policy)（最后修订 2025-03-06） · [社区准则](https://crushon.ai/community-guidelines) · [内容移除政策](https://crushon.ai/content-removal-policy) · [投诉政策](https://crushon.ai/complaints-policy) · [18 U.S.C. 2257 合规声明](https://crushon.ai/2257)（最后更新 2025-02-08）
- [Discord 服务器](https://discord.gg/crushonai) · [Discord invite API 记录](https://discord.com/api/v10/invites/crushonai?with_counts=true) · [联盟计划申请表](https://docs.google.com/forms/d/e/1FAIpQLScro_QKiXXbUf3qA_pv5QkLLiJdwxqKAJt1NCb3ZzUMkstgkA/viewform)
- [crushonai.com —— "Crushon AI Corp." 咨询工作室站点](https://crushonai.com/)
- 存档抓取 —— [条款，2024-11-04](https://web.archive.org/web/20241104142659/https://crushon.ai/terms-of-service) · [条款，2025-03-06（Crushon AI Corp.，贝尔维尤 WA）](https://web.archive.org/web/20250306123450/https://crushon.ai/terms-of-service) · [2257 声明，2025-03-28（CRUSHON AI INC.，温哥华 BC）](https://web.archive.org/web/20250328101207/https://crushon.ai/2257) · [条款，2025-08-02（TECHIEPIE LTD）](https://web.archive.org/web/20250802153204/https://crushon.ai/terms-of-service) · [条款，2026-07-28](https://web.archive.org/web/20260728204653/https://crushon.ai/terms-of-service) · [隐私政策，2026-07-28](https://web.archive.org/web/20260728182017/https://crushon.ai/privacy-policy) · [社区准则，2026-07-16](https://web.archive.org/web/20260716045138/https://crushon.ai/community-guidelines)
- 最早与周年抓取 —— [首页，2023-06-03](https://web.archive.org/web/20230603004309/https://crushon.ai/) · [3 周年页面，2026-06-15](https://web.archive.org/web/20260615214222/https://crushon.ai/3rd-anniversary)

**登记与第三方档案**

- [i-Cyprus —— TECHIEPIE LTD（HE 472689）](https://i-cyprus.com/company/654032)
- [Similarweb —— crushon.ai 流量档案](https://www.similarweb.com/website/crushon.ai/)
- [Tracxn —— Crushon AI](https://tracxn.com/d/companies/crushon-ai/__Q35HFbL4EOKKbeaPG1IMIImXSmSm5PMMERN6lpfOev8) · [Crunchbase —— Crushon AI（需订阅）](https://www.crunchbase.com/organization/crushon-ai) · [PitchBook —— Crushon AI（需订阅）](https://pitchbook.com/profiles/company/1458847-81)
- [StartupHub.ai —— 声称的 1,500 万美元融资，未引用来源](https://www.startuphub.ai/investment_rounds/crushonai-funding-round-2026)
- [Apple iTunes 搜索 API —— 美国区无第一方 CrushOn 应用](https://itunes.apple.com/search?term=crushon&entity=software&country=us&limit=5) · [Google Play 搜索 —— 无第一方 CrushOn 应用](https://play.google.com/store/search?q=crushon&c=apps&hl=en&gl=US)
