# Evoto

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-12。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-12。英文版为原始版本。

## 摘要

Evoto 是面向专业摄影师的桌面、平板、手机与网页软件——RAW 处理、AI 选片、人像修饰、调色、联机拍摄与活动图库——按"每导出一张照片消耗额度（credit）"计费。站点把运营方呈现为 `Truesight Technology Inc.`，一家地址为 "OFFICE NO. 1215 1000 N. WEST STREET, SUITE 1200, WILMINGTON, DELAWARE 19801, USA" 的特拉华州公司，同时并列 `TRUESIGHT PTE.LTD.`（新加坡）、`株式会社Truesight Japan` 和 `Truesight Korea Limited`（[关于页](https://www.evoto.ai/about)；无日期，访问于 2026-08-12）。但服务条款至今仍是为 `TRUESIGHT PTE. LTD.` 撰写并适用新加坡法律（[服务条款](https://res.evoto.ai/ui/www/policy/terms.html)；更新于 2024-03-22）——见 `品牌与法律实体`。

- 规模数字来自公司自述："200+ Countries & Regions"、"1M+ Professional Photographers"、"50k+ Photography Studios"、"800M+ Photos Processed"，同一页面注明其口径为 "based on internal account and usage data reviewed as of 2026"（[关于页](https://www.evoto.ai/about)；访问于 2026-08-12）。可独立观察到的分发量要小得多：Google Play 显示 "100K+" 下载、4.7 分／1.46K 条评价（[Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto)；访问于 2026-08-12），iOS 应用有 2,301 条评分、均分 4.91（[iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us)；访问于 2026-08-12）。
- 截至 2026-08-12，在所查阅的公开来源中，公司未公布过任何融资轮次。[Tracxn](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) 称 "Evoto has not raised any funding rounds yet"；[Latka](https://getlatka.com/companies/evoto.ai) 称累计融资 0 美元、"bootstrapped"（自筹），并给出 2025 年营收估算 410 万美元、2026 年约 37 名员工——见 `融资`。
- 定价按额度计量：编辑免费，导出消耗额度，大致每张照片 1 个额度；年度套餐从 800 额度 80 美元/年（每额度 0.10 美元）到 24,000 额度 1,205 美元/年（每额度 0.05 美元），单独购买的额度两年后过期（[付费页](https://www.evoto.ai/payment)；访问于 2026-08-12）。
- 2026 年 1 月，公司上线了一个 "Online AI Headshot Generator"（在线 AI 证件照生成器）页面，宣传语包括 "Save money vs. studio sessions"（[存档于 2026-01-10](https://web.archive.org/web/20260110205938/https://www.evoto.ai/features/ai-headshot-generator)），在客户与品牌大使的批评后将其下线，并表示 "We missed the mark, and we are sorry"（[Digital Camera World，2026-01-21](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash)）。该 URL 现在跳转至 `/404`（检查于 2026-08-12）。
- 工程方面的证据来自公开资产而非技术栈说明页：营销站点是置于 CloudFront 之后、以 S3 为源的 Nuxt 应用；桌面安装包是约 2.0 GB 的 NSIS 安装程序，经 GlobalSign EV 代码签名给 "Truesight Technology Inc."（特拉华州）；博客是置于 Cloudflare 之后的 WordPress；支持中心跑在 GitBook 上；隐私政策把 AWS 列为处理用户上传数据的云服务商，并称 "primary location for processing your personal information" 为美国（响应头与安装包检查于 2026-08-12；[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)；最后更新 2025-06-20）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | Evoto（产品线：Evoto Desktop、Evoto iPad、Evoto Mobile、Evoto Instant、Evoto Video、Evoto Online） | [官网](https://www.evoto.ai/)、[下载页](https://www.evoto.ai/download)、[付费页](https://www.evoto.ai/payment)；访问于 2026-08-12 |
| 站点页脚署名的主体 | "©️2026 Truesight Technology Inc. \| OFFICE NO. 1215 1000 N. West Street, Suite 1200, Wilmington, Delaware 19801, USA" | [下载页页脚](https://www.evoto.ai/download)；访问于 2026-08-12 |
| 服务条款署名的主体 | "TRUESIGHT PTE. LTD. (“TRUESIGHT”)"；适用 "the laws of Singapore"，并约定 "exclusive jurisdiction of the courts of Singapore" | [服务条款](https://res.evoto.ai/ui/www/policy/terms.html)；更新于 2024-03-22 |
| 退款政策署名的主体 | "Truesight PTE. LTD." | [退款政策](https://res.evoto.ai/ui/www/policy/refund.html)；无日期，访问于 2026-08-12 |
| 自述成立时间 | "Founded in 2020"；"In 2020, after sitting down with hundreds of working photographers" | [关于页](https://www.evoto.ai/about)、[公司页](https://www.evoto.ai/company)；无日期，访问于 2026-08-12 |
| 新加坡登记信息 | TRUESIGHT PTE. LTD.，UEN 202224238M，成立于 2022-07-13，私人股份有限公司，3 Fraser Street #04-23A DUO Tower 189352 | [companies.sg](https://www.companies.sg/business/202224238M/TRUESIGHT-PTE-LTD-)（ACRA 数据镜像）；访问于 2026-08-12 —— 见 `备注` |
| 日本登记信息 | 株式会社Truesight Japan，法人番号 5020001152305，東京都渋谷区渋谷2-24-12 渋谷スクランブルスクエア37階 | [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305)（记录更新于 2025-12-05） |
| 日本主体其他信息 | 設立 2023年6月、資本金 1000万円、代表取締役 Mitta Zhang（PR TIMES 会社概要 代表者名：張偉）、電話 050-1780-9810、未上場 | [PR TIMES 新闻稿及公司概要](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)；发布于 2025-12-05 |
| 韩国主体 | Truesight Korea Limited，Room 6080, Seongil Building, Nonhyeon-dong 584, Gangnam-daero, Gangnam-gu, Seoul | [关于页](https://www.evoto.ai/about)；无日期，访问于 2026-08-12 |
| Windows 安装包的代码签名证书 | 主体 "Truesight Technology Inc."，州 "Delaware"，市 "Newark"；由 "GlobalSign GCC R45 EV CodeSigning CA 2020" 签发，时间戳由 Sectigo 提供 | 从 [`Evoto_Setup_7.3.0-512.exe`](https://res.evoto.ai/package/7.3.0-512/Evoto_Setup_7.3.0-512.exe) 中读取的证书字符串，2026-08-12 |
| 具名管理层 | "Mitta — CEO & Founder"；"Mitta Zhang, CEO at Evoto" | [关于页](https://www.evoto.ai/about)、[PR Newswire，2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html) |
| 员工人数 | 公司未公布；第三方数字从 4 人到 500 人不等 —— 见 `备注` | 见 `备注` |
| 自述团队分布 | "Our team spans 6 countries"；"photographers, engineers, designers, and product people" | [关于页](https://www.evoto.ai/about)；无日期，访问于 2026-08-12 |
| 公开联系方式 | `support@evoto.ai`（美国／新加坡／韩国）、`support-jp@evoto.ai`（日本）、`contactus@evoto.ai`（隐私与退款）、`developer@evoto.ai` 与 +65 8743 2041（Google Play 开发者信息） | [关于页](https://www.evoto.ai/about)、[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)、[Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto) |
| 社交与社区 | Facebook `evotoai`、Instagram `evotoai`、X `Evotoofficial`、TikTok `evotoaitk`、YouTube `EvotoChannel`、LinkedIn `evoto-ai`、Reddit `r/EvotoAI`，论坛在 `forum.evoto.ai` | [官网页脚](https://www.evoto.ai/)；访问于 2026-08-12 |
| 站点语言 | 英文之外还有 `vi`、`ko`、`ja`、`de`、`fr`、`es`、`it`、`pt`、`es_Es`、`zh-Hant`、`pl`、`ar`、`tr`、`th`；没有简体中文版本 | [sitemap 索引](https://www.evoto.ai/sitemap_index.xml)、[robots.txt](https://www.evoto.ai/robots.txt)；访问于 2026-08-12 |
| 展示的认证 | ISO/IEC 27001 与 SOC 2 Type 2 徽标（未给出证书编号、范围或审计机构） | [关于页](https://www.evoto.ai/about)、[下载页](https://www.evoto.ai/download)；访问于 2026-08-12 |
| 日本隐私认证 | プライバシーマーク 第17004988(01)号，有效期 2025-01-07 至 2027-01-06，审查机构为一般社団法人日本情報システム・ユーザー協会，取得日 2025-01-07 | [PR TIMES，2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html) |
| iOS 应用 | `com.truesight.evoto`，"Evoto-AI Photo Editor&Retouch"，发行方 TRUESIGHT PTE. LTD.，首发 2024-11-01，版本 3.1.3（2026-08-11），801,347,584 字节，最低 iOS 15.0，13 种语言，2,301 条评分均分 4.91 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us)；访问于 2026-08-12 |
| Android 应用 | `com.truesight.evoto`，开发者 TRUESIGHT PTE. LTD.，"100K+" 下载，4.7 分／1.46K 条评价，更新于 2026-07-30，含应用内购买；开发者信息给出 3 Fraser Street, Singapore 189352 | [Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto)；访问于 2026-08-12 |
| Evoto Instant iOS 应用 | `ai.evoto.instant.capture`，首发 2025-09-10，版本 1.8.1（2026-08-07），12 条评分均分 4.33 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749685404&country=us)；访问于 2026-08-12 |
| 桌面安装包 | 稳定版 7.3.0-512，页面标注 "Update Time: 2026-08-06"；Windows 安装包 2,032,789,104 字节（`last-modified` 2026-08-07），macOS arm64 镜像 1,903,599,556 字节（`last-modified` 2026-08-07）；macOS 分 Intel 与 arm64 两个构建；另有 7.3.5-76 一组构建 | [下载页](https://www.evoto.ai/download) 及 2026-08-12 观察到的响应头 |
| 支持的桌面系统 | macOS "10.13 and above"；"Win7/Win10/Win11" | [下载页](https://www.evoto.ai/download)；访问于 2026-08-12 |

**活动、奖项与合作**：公司在摄影行业展会上参展：日本 CP+ 2024 与 CP+ 2025（[PR TIMES，2024-02-19](https://prtimes.jp/main/html/rd/p/000000001.000132859.html)、[PR TIMES，2025-02-20](https://prtimes.jp/main/html/rd/p/000000014.000132859.html)）、2024 年的ブライダル産業フェア与 PHOTONEXT（[PR TIMES，2024-04-30](https://prtimes.jp/main/html/rd/p/000000003.000132859.html)、[PR TIMES，2024-05-31](https://prtimes.jp/main/html/rd/p/000000004.000132859.html)）、2025 年 9 月在纽约举办的 "Evoto One" 品牌活动（[PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)），以及 2026 年纳什维尔 Imaging USA 的 #547 展位（[PR Newswire，2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)）；官网还列出 NAB、MPN FOTOVAKB 和 TexasSchool（[官网](https://www.evoto.ai/)；访问于 2026-08-12）。在日本，`株式会社Truesight Japan` 与 `株式会社ラボネットワーク` 签署代理店契约，于 2024-12-27 公布（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000132859.html)、[ラボネットワーク](https://www.labonetwork.co.jp/news/24122701/)）。公司宣布入选 "Capterra's 2026 Best Ease of Use rankings for both the Artificial Intelligence and Photo Editing categories"，并说明这属于 "category-level visibility in buyer-facing ranking views" 而非 "independent lab benchmarking"（[博客，2026-03-27](https://blog.evoto.ai/evoto-capterra-2026-press-release/)）。

### 品牌与法律实体

| 名称 | 类型 | 标示的司法辖区 | 来源中表述的关系 | 来源 |
|---|---|---|---|---|
| Evoto | 公开品牌 | — | 用于站点、应用、商店列表、博客、支持中心与论坛的名称 | [官网](https://www.evoto.ai/) |
| Truesight Technology Inc. | 站点页脚、`about` 页 "United States" 区块以及 Windows 代码签名证书中出现的法律主体 | 美国特拉华州 | 被呈现为 Evoto 背后的公司；`llms.txt` 称 Evoto 为 "software developed by TRUESIGHT TECHNOLOGY INC., a computer software company headquartered in the United States" | [关于页](https://www.evoto.ai/about)、[llms.txt](https://www.evoto.ai/llms.txt) |
| TRUESIGHT PTE.LTD. | 服务条款、退款政策、两个应用商店的发行方记录以及 `about` 页 "Singapore Branch" 区块中出现的法律主体 | 新加坡（据 ACRA 镜像 UEN 202224238M） | 条款中的缔约方；应用商店的销售方 | [服务条款](https://res.evoto.ai/ui/www/policy/terms.html)、[iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us) |
| 株式会社Truesight Japan | 法律主体，法人番号 5020001152305 | 日本（东京） | 其自身新闻稿先称自己是"シンガポールのIT企業 TRUESIGHT PTE.LTD."的日本法人（2025-01），后改称"米国のIT企業 Truesight Technology Inc."的日本法人（2025-12） | [PR TIMES，2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html)、[PR TIMES，2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) |
| Truesight Korea Limited | `about` 页 "Korea Branch" 区块中出现的法律主体 | 韩国（首尔） | 作为联系办公室列出；未取得登记记录 | [关于页](https://www.evoto.ai/about) |

`about` 页把新加坡、日本、韩国都标注为 "Branch"（分支），但新加坡的 ACRA 记录显示的是一家独立注册的私人有限公司，日本的则是独立登记的株式会社。所查阅的来源中没有一处说明这四个主体之间的持股关系，也未找到合并性质的公司文件 —— 见 `备注`。

公司自行维护的 LinkedIn 页面是围绕新加坡主体撰写的："TRUESIGHT PTE.LTD., established in 2020 in Singapore by a team of experienced AI researchers and graphic engineers, is a leading provider of AI-powered SaaS software solutions. Over the past three years, we have excelled in developing and hosting innovative softwares that empower professional creators and designers."。同一页面给出 Headquarters "Wilmington, Delaware"、Founded "2020"、Industry "Technology, Information and Internet"、Company size "501-1,000 employees"，并列出 47 个员工档案（[LinkedIn](https://www.linkedin.com/company/evoto-ai)；无日期，访问于 2026-08-12）。

---

## 产品

官网主标题是 "Tether. Cull. Retouch. Deliver. The Ultimate End-To-End Photography Workflow"（[官网](https://www.evoto.ai/)；访问于 2026-08-12）。公司把产品描述为 "an image organization and artificial intelligence (AI) SaaS image processing software … offer[ing] photo editing solutions including portrait retouching, AI color grading, background removal, AI skin retouching, blemish removal, body sculpting, clothing wrinkle removal, and tethered shooting for photographers, creators, and commercial business owners"（[llms.txt](https://www.evoto.ai/llms.txt)；访问于 2026-08-12）。

### 产品形态

| 形态 | 平台 | 是什么 | 来源 |
|---|---|---|---|
| Evoto Desktop | macOS 10.13+、Windows 7/10/11 | 主应用：RAW 处理、AI 选片、人像修饰、调色、背景处理、批量编辑、联机拍摄 | [下载页](https://www.evoto.ai/download)、[版本说明](https://www.evoto.ai/release-notes) |
| Evoto iPad | iPadOS | 平板版；公司发言人称其具备 "80–90% parity with desktop features" | [PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/) |
| Evoto Mobile | iOS、Android | 手机应用，含修饰、调色、RAW 与联机拍摄；支持 "Canon, Sony, Nikon, Fujifilm, Leica, Panasonic, and more" | [App Store 描述](https://apps.apple.com/us/app/evoto-ai-photo-editor-retouch/id6596737043)、[PR TIMES，2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) |
| Evoto Instant | `instant.evoto.ai`、iOS 应用 `ai.evoto.instant.capture`，另有 `EIPrinter` Windows 配套程序 | 实时活动图库："Shoot, Cull, Edit, Proof, Share in an Instant"，含图库与照片品牌化、客户选片、备注与幻灯片；新用户可领 "12 GB" 存储 | [instant.evoto.ai](https://instant.evoto.ai/)；访问于 2026-08-12 |
| Evoto Video | macOS、Windows | "Professional-grade AI color grading and retouching for video creators"，含 AI Color Match 与 "Ultra-precise 4K" 视频修饰 | [video.evoto.ai](https://video.evoto.ai/)；访问于 2026-08-12 |
| Evoto Online | 浏览器 | 网页试用入口，从功能落地页提供单项功能（"Online Trial"） | [付费页](https://www.evoto.ai/payment)套餐表与功能页；访问于 2026-08-12 |
| Academy、Webinar、博客、支持中心、论坛 | 网页 | `academy.evoto.ai`（Next.js）、`evoto.ai/webinar`（由具名摄影师主讲的录播）、`blog.evoto.ai`（WordPress，711 篇）、`support.evoto.ai`（GitBook）、`forum.evoto.ai` | 2026-08-12 观察到的响应头与 [WordPress REST API](https://blog.evoto.ai/wp-json/wp/v2/posts?per_page=1) |

### 版本发布历史

公开的版本说明列出 28 个桌面版本，从 2023-05-17 的 V1.5.0 到 2026-07-10 的 V7.3.0（[版本说明](https://www.evoto.ai/release-notes)；访问于 2026-08-12）。节选：

| 版本 | 日期 | 页面列出的主要功能 |
|---|---|---|
| V1.5.0 | 2023-05-17 | "Lens Corrections"、"Color Grading"、"New Makeup Presets & Contacts" |
| V4.1.0 | 2024-12-26 | AI 色彩匹配（日文公告中的 "AIカラーマッチ"） |
| V5.0.0 | 2025-06-23 | "Library"、"Dehaze"、"Unify Lighting"、"Double Eyelids" |
| V6.0.0 | 2025-09-16 | "AI Culling"、"Spill Removal"、"AI Exposure and White Balance Adjustment"、"Tethered Shooting" |
| V6.1.0 | 2025-11-05 | "Cloud Collaboration Now Available"、"AI-Powered Multi-Image Color Consistency"、"AI Denoise" |
| V6.2.0 | 2026-01-30 | "New Pet Retouching Module"、"Pet Masks"、"Photo Cluster"、"Stretch Marks Removal" |
| V7.0.5 | 2026-03-31 | "Your AI Looks"、"AI Lab"、"Smarter Mask Tools"、"Perfect Shot" |
| V7.1.5 | 2026-04-29 | "Our AI Commitment"、"AI Background Fusion"、"Floor Reflection"、"AI Body Complexion" |
| V7.3.0 | 2026-07-10 | "Batch AI Set Design"、"Matte Refinement"、"Strong Glare Removal"、"Glow Effect" |

### 商业化

下载与注册免费；导出编辑后的照片消耗额度，"From 1 credit per photo"（[付费页](https://www.evoto.ai/payment)；访问于 2026-08-12）。下列价格是 2026-08-12 付费页返回的美元数字；该页面按地区本地化，从东京出口访问时返回的是日元。

| 项目 | 内容 | 来源 |
|---|---|---|
| 年度套餐 | Starter 800 额度 80 美元/年（原价 89 美元，"Estimated monthly US$6.99"，2 台设备）；Basic 1,600 额度 134 美元（149 美元，3 台）；Basic Plus 3,600 额度 242 美元（269 美元，4 台）；Standard 9,000 额度 521 美元（579 美元，5 台）；Standard Plus 24,000 额度 1,205 美元（1,339 美元，6 台） | [付费页](https://www.evoto.ai/payment)；访问于 2026-08-12 |
| 折算单价 | 按档位分别为每额度 0.10、0.08、0.07、0.06、0.05 美元 | [付费页](https://www.evoto.ai/payment) |
| 按需购买 | 按需购买额度包；"The credit you have purchased will expire after 2 years"；2026 年 2 月的一篇评测给出入门价 "$49 for 200 credits"、约每张 0.25 美元 | [付费页 FAQ](https://www.evoto.ai/payment)、[Digital Camera World，2026-02-13](https://www.digitalcameraworld.com/tech/software/evoto-ai-review) |
| 加购包 | 200 至 24,000 额度的加购包，价格随订阅档位下降（例如 200 额度从 22 美元降至 11 美元） | [付费页](https://www.evoto.ai/payment) |
| 云存储包 | 500 GB 119 美元、1 TB 189 美元、2 TB 269 美元，各档位价格相同 | [付费页](https://www.evoto.ai/payment) |
| 免费试用与初始额度 | "one 7-day free trial per account"、"Try full features with 50 free credits"；下载页提供下载即得 "15 Credits" | [付费页](https://www.evoto.ai/payment)、[下载页](https://www.evoto.ai/download) |
| 额度结转 | 续订时未用额度可结转，"up to a maximum of 5 times the credit of your new subscription package"；有 30 天宽限期 | [付费页 FAQ](https://www.evoto.ai/payment) |
| 免额度功能 | 从桌面 v6.1 起，基础色彩调整、裁剪旋转、联机拍摄与手动工具的导出不消耗额度；iPad 版、Instant 与 v6.0 及更早的桌面版不适用 | [付费页](https://www.evoto.ai/payment)、[PR TIMES，2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html) |
| 支付方式 | "Credit cards and Paypal are currently the forms of acceptable payment for your Subscription" | [服务条款](https://res.evoto.ai/ui/www/policy/terms.html)；更新于 2024-03-22 |
| 退款 | 仅当 "your subscription order is within the 14-day cancellation period and you have not utilized the services under this specific order" 时可退；否则 "All fees paid are non-refundable"；处理最长 10 个工作日 | [退款政策](https://res.evoto.ai/ui/www/policy/refund.html) |
| 积分与推荐 | "Evoto Smart Points" 通过购买、推荐与互动获得，可兑换额度与云存储，"A single points system throughout your workflow — Photo Editor, Cloud, Instant, mobile, and desktop"；另有独立的推荐计划页面 | [积分计划](https://www.evoto.ai/loyalty)、[推荐计划](https://www.evoto.ai/referral)；访问于 2026-08-12 |
| 企业版 | 付费页有 "Enterprise" 分页，页脚有 "Contact Sales" 链接；未找到企业版价目表 | [付费页](https://www.evoto.ai/payment)；访问于 2026-08-12 |
| 日本渠道 | 日本市场的销售与支持通过 `株式会社Truesight Japan` 进行，并与 `株式会社ラボネットワーク` 达成代理店契约，于 2024-12-27 公布 | [PR TIMES，2024-12-27](https://prtimes.jp/main/html/rd/p/000000011.000132859.html) |

### 公开披露的规模变化

| 日期 | 披露的数字 | 来源 |
|---|---|---|
| 2022-11-23 | 营销站点已上线，名为 "EVOTO, AI-powered Image Editor"，宣称 "thousands of photos processed with 10x speed" | [Wayback 存档](https://web.archive.org/web/20221123171058/https://evoto.ai/) |
| 2023-05-17 | 公开版本说明中最早的桌面版本（V1.5.0） | [版本说明](https://www.evoto.ai/release-notes) |
| 2024-11-01 | iOS 应用首次发布 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us) |
| 2025-09-23 | "a team of 500 employees serving millions of users across 158 countries"；总部写作加州门洛帕克；成立年份写作 2022 | [PetaPixel](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/) |
| 2026-01-11 | Imaging USA 上的产品口径：工作流割裂导致的时间可挽回 "65%"、AI 选片 "5,000 photos in under 10 minutes"、AI 物体移除 "15x faster"、影楼加购率 "30% increase in studio upsell rates" | [PR Newswire](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html) |
| 2026-03-27 | 入选 "Capterra's 2026 Best Ease of Use rankings" 的人工智能与照片编辑两个类别 | [博客](https://blog.evoto.ai/evoto-capterra-2026-press-release/) |
| 2025（估算） | 营收 410 万美元，"latest figure estimated"；累计融资 0 美元；2026 年约 37 名员工 | [Latka](https://getlatka.com/companies/evoto.ai)；访问于 2026-08-12 |
| 访问于 2026-08-12 | 公司自述 "1M+ Professional Photographers"、"200+ Countries & Regions"、"50k+ Photography Studios"、"800M+ Photos Processed" | [关于页](https://www.evoto.ai/about) |
| 访问于 2026-08-12 | Google Play "100K+" 下载、4.7 分／1.46K 条评价；App Store 2,301 条评分均分 4.91；Evoto Instant 12 条评分 | [Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto)、[iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us) |

公司未公布任何客户数、营收、付费席位、额度消耗或留存数字 —— 见 `备注`。

### AI 证件照生成器页面及其下线（2026 年 1 月）

| 日期 | 事件 | 来源 |
|---|---|---|
| 2026-01-10 | Internet Archive 抓取到 `www.evoto.ai/features/ai-headshot-generator` 页面。页面提供 "Turn selfies into professional headshots fast for free"，承诺 "2K or 4K, watermark-free headshots with 5 free styles"，并以 "Skip the hassle of bookings and edits"、"saving time vs. traditional photoshoots"、"Save money vs. studio sessions. Fit budgets for individuals, teams, and industries" 作为卖点 | [存档页面](https://web.archive.org/web/20260110205938/https://www.evoto.ai/features/ai-headshot-generator) |
| 2026-01-12 | 公司首次回应：该工具 "moved into a phase of visibility beyond our intended roadmap" | [PetaPixel，2026-01-15](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/) |
| 2026-01-14 | 行业媒体继续报道该回应 | [The Phoblographer](https://www.thephoblographer.com/2026/01/14/evoto-ai-headshot-generator-anti-photographer/) |
| 2026-01-15 | PetaPixel 报道反弹；摄影师、Evoto 品牌大使 Sal Cincotta 被引述称 "Evoto is trying to hurt the very people that I'm trying to help" | [PetaPixel](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/) |
| 2026-01-16 | 后续声明称该页面 "intended as a secondary page focused on SEO" | [PetaPixel](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/) |
| 2026-01-21 | 报道引述公司声明："We missed the mark, and we are sorry"；"We realize that by testing a tool that generates images from scratch, we crossed a line. Evoto was built to handle the heavy lifting of retouching – not a tool that replaces the person behind the lens"；以及 "We do not use your images or your clients' images to train our AI models (…) We source our data exclusively through commercially licensed and purchased imagery"。该生成器被描述为已永久移除 | [Digital Camera World](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash) |
| 2026-02-13 | 一篇产品评测把 "Questions raised by 'headshotgate' controversy" 列入缺点 | [Digital Camera World 评测](https://www.digitalcameraworld.com/tech/software/evoto-ai-review) |
| 2026-04-29 | 桌面版 V7.1.5 发布名为 "Our AI Commitment" 的版本说明条目："Evoto does not use your images or data to train generative AI models without your explicit permission." | [版本说明](https://www.evoto.ai/release-notes) |
| 检查于 2026-08-12 | `www.evoto.ai/features/ai-headshot-generator` 返回 HTTP 302 跳转至 `/404` | 2026-08-12 观察到的请求 |

### 公开表述的计划

公司公开表述的方向是覆盖端到端工作流："Our customers would love to use Evoto for their entire workflow, from capture to delivery. That's the direction we're heading"（[美国发言人 Jay Peterson，PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)）。2026 年 1 月的新闻稿把 Evoto Mobile、Desktop 6.2 与 Instant 1.4 的组合称为 "the industry's first true All-in-One workflow"，并引述 CEO："We aren't just building tools; we are building a time machine for the modern photographer"（[PR Newswire，2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)）。

---

## 创始人

**Mitta** —— "CEO & Founder"。`about` 页引述其话："At Evoto, we believe AI should handle the pixels, so photographers can focus on the soul. Our mission is to bridge the gap between technical complexity and creative intent—giving you back the time to do what only a human can: capture emotion and tell a story."。Evoto 的任何页面都没有出现其姓氏、职业经历、教育背景或此前所在公司（[关于页](https://www.evoto.ai/about)；无日期，访问于 2026-08-12）。

更完整的名字出现在公司对外发布的稿件而非站点上。Imaging USA 新闻稿把一段话归于 "Mitta Zhang, CEO at Evoto"（[PR Newswire，2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)）。日文新闻稿把 `株式会社Truesight Japan` 的负责人写作 "代表取締役：Mitta Zhang"，而同一页面的 PR TIMES 公司概要区块把 代表者名 写作 張偉（[PR TIMES，2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)）。

一个日本创业公司数据库则把日本主体的负责人列为 代表取締役社長 ウィリアム・ワン，并称其拥有九州大学 MBA、曾任富士通半导体亚洲市场负责人，此前在中国的创业公司工作过（[スタクラ](https://startupclass.co.jp/online/companies/1846/)；无日期，访问于 2026-08-12）。关于日本主体由谁代表，所查阅的来源没有一处能把这两种说法对上 —— 见 `备注`。

**Jay Peterson** 在 2025 年 9 月的采访中被标注为 Evoto 的 "U.S. Spokesperson"，公司大部分公开的产品与规模表述出自该篇采访（[PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)）。

`evoto.ai` 上没有团队页、管理层页或投资人页；`about` 页只提到 "Mitta"，博客文章也没有工程或管理层署名（[关于页](https://www.evoto.ai/about)、[博客](https://blog.evoto.ai/)；访问于 2026-08-12）。

---

## 融资

截至 2026-08-12，在所查阅的公开来源中，未找到 Evoto 品牌或任一 Truesight 主体的融资公告：`evoto.ai` 上没有新闻页、投资人页或融资表述，日本 PR TIMES 订阅源列出的 20 篇新闻稿中也没有融资公告。下表记录第三方来源的说法。

| 日期 | 轮次（按来源写法） | 金额 | 投资方 | 来源 |
|---|---|---|---|---|
| 访问于 2026-08-12（页面标注 "Last updated August 3, 2026"） | 无 —— "Evoto has not raised any funding rounds yet"；被描述为 "unfunded company"，成立于 2024 年，总部在新加坡 | 无 | 未列出 | [Tracxn](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) |
| 访问于 2026-08-12 | 无 —— 累计融资 0 美元，"bootstrapped"、"no venture capital or outside funding"；2025 年营收"估算"为 410 万美元；2026 年约 37 名员工；成立于 2020 年 | 无 | 未列出 | [Latka](https://getlatka.com/companies/evoto.ai) |
| 访问于 2026-08-12 | 未确立 | — | — | PitchBook 有 [Truesight (China)](https://pitchbook.com/profiles/company/503403-85)（据搜索结果描述为 "developer of AI-powered image processing software intended for commercial photography and consumer electronics"）与 [TrueSight Technology](https://pitchbook.com/profiles/company/437673-34) 两个档案；两页在无订阅时均无法读取，也均未被确认就是本公司 —— 见 `备注` |

两个数据库的数字都未与一手来源核对过，且与公司自述的成立年份和总部所在地互相矛盾。股权结构、估值、股东名册以及四个 Truesight 主体之间的关系，在所查阅的任何来源中都未被确立。

---

## 工程

### 技术栈与平台

公司未发布技术栈说明页。除另有标注外，以下条目均由可观察的公开资产或一手文档确认（均观察于 2026-08-12）。

- **营销站点：** Nuxt（`x-powered-by: Nuxt`），经 Amazon CloudFront（`dpqccnyr1royh.cloudfront.net`）分发，静态资源与安装包放在 `res.evoto.ai` 的 Amazon S3 上（`server: AmazonS3`、`x-amz-server-side-encryption: AES256`）。`api.evoto.ai` 解析到同一个分发，根路径返回 HTTP 404。
- **面向机器的站点表面：** 站点的 `robots.txt` 带有 `Content-Signal: ai-train=yes, search=yes, ai-input=yes` 响应头，并发布 `llms.txt` 和索引 140 个页面的 `llms-full.txt`，每个页面都有 Markdown 孪生版本（`/about.md`、`/payment.md` 等），其中 126 个是功能落地页（[robots.txt](https://www.evoto.ai/robots.txt)、[llms.txt](https://www.evoto.ai/llms.txt)）。
- **其他 Web 资产：** `academy.evoto.ai` 是 CloudFront 后的 Next.js；`blog.evoto.ai` 是 Cloudflare 后的 WordPress，已发布 711 篇文章（`x-wp-total: 711`）；`support.evoto.ai` 在 Cloudflare 之后，`help.evoto.ai` 跳转到 GitBook（`app.gitbook.com`）；`forum.evoto.ai` 提供标题为 "Evoto" 的站点；`community.evoto.ai` 从 Google 前端返回 HTTP 503。
- **桌面应用：** Windows 安装包由 NSIS 构建（二进制中含 `Nullsoft`／`NSIS` 标记），7.3.0-512 为 2,032,789,104 字节，采用 EV 代码签名，主体为 "Truesight Technology Inc."（特拉华州 Newark），签发方为 "GlobalSign GCC R45 EV CodeSigning CA 2020"，时间戳由 Sectigo 提供；macOS 版分 Intel 与 arm64 两个约 1.9 GB 的磁盘镜像。同一 S3 存储桶还发布了独立的 `EvotoInstaller` 下载器（beta 与 stable 两种）以及配合 Evoto Instant 的 `EIPrinter` Windows 程序（19,235,781 字节，`last-modified` 2026-04-24）。
- **移动端：** iOS 版要求 iOS 15.0 及以上，体积 801,347,584 字节，附带 13 个语言代码；Android 版通过 Google Play 分发并含应用内购买（[iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us)、[Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto)）。
- **云端处理（一手表述）：** "Data Sharing Recipient: AWS (third-party cloud service provider), for the purpose of: To enable cloud-based analysis, processing, transmission, and storage of user-uploaded data"；"Our primary location for processing your personal information is United States"（[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)；最后更新 2025-06-20）。
- **分析、归因与第三方服务（一手表述加上观察到的页面资源）：** Mixpanel 与 Google 用于产品分析；Facebook、TikTok 与 ShareASale 用于广告归因；Infobip 用于手机号身份验证（[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)）。官网还加载 Google Tag Manager、Facebook Connect、Twitter 广告、Naver 与 Yahoo! JAPAN 的标签以及 `dwin1.com`（Awin），并写入表明使用 Statsig 的 `user_id_statsig` cookie（[官网](https://www.evoto.ai/)页面资源与响应头；观察于 2026-08-12）。
- **相机对接：** 有线与无线联机拍摄，支持 "Canon, Sony, Nikon, Fujifilm, Leica, Panasonic, and more"（[App Store 描述](https://apps.apple.com/us/app/evoto-ai-photo-editor-retouch/id6596737043)）。
- **没有公开代码：** `evoto`、`evotoai`、`truesight`、`truesight-technology` 名下均无 GitHub 组织；npm 上没有 `evoto` 包或 scope；PyPI 上没有名为 `evoto` 的包（API 检查于 2026-08-12）。

### 系统

| 系统 | 做什么 | 来源 |
|---|---|---|
| 额度计量与导出授权 | 编辑免费，导出消耗额度；桌面 v6.1 起部分功能免额度；结转上限为新套餐额度的 5 倍，另有 30 天宽限期 | [付费页](https://www.evoto.ai/payment)、[PR TIMES，2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html) |
| 跨产品账号与权益打通 | 桌面、iPad 与手机共用一个账号；已购买的"チケット"（额度）跨平台通用，但官网与 iPhone 应用内销售的额度包种类与价格不同 | [PR TIMES，2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) |
| 云存储与协作 | 桌面 V6.1.0（2025-11-05）上线 "Cloud Collaboration"；云存储按 500 GB／1 TB／2 TB 包售卖；Instant 提供 12 GB 赠送 | [版本说明](https://www.evoto.ai/release-notes)、[付费页](https://www.evoto.ai/payment)、[instant.evoto.ai](https://instant.evoto.ai/) |
| 活动图库流水线 | Instant 覆盖现场拍摄、选片、编辑、校对与分享，含图库品牌化、客户选片与收藏、客户备注与自动播放幻灯片，另有 Windows 打印配套程序 | [instant.evoto.ai](https://instant.evoto.ai/)、`res.evoto.ai` 上的 `EIPrinter` 安装包 |
| 联机拍摄 | 跨多个相机厂商的有线与无线联机，桌面版在 V6.0.0（2025-09-16）加入，iPad 与手机端同样支持 | [版本说明](https://www.evoto.ai/release-notes)、[PR TIMES，2024-12-16](https://prtimes.jp/main/html/rd/p/000000009.000132859.html) |
| AI 选片 | 对大批量拍摄自动挑选；公司称 "5,000 photos in under 10 minutes"，并有 "Face Focus Mode" 与 "Capture Time Grouping" | [PR Newswire，2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html) |
| 色彩迁移 | "AI Color Match" 在照片与视频上按参考图迁移色彩，无需 LUT 或蒙版；多图色彩一致性在 V6.1.0 加入 | [video.evoto.ai](https://video.evoto.ai/)、[版本说明](https://www.evoto.ai/release-notes) |
| 云内容审核 | "Cloud content may be automatically scanned to ensure we do not host illegal or abusive content, such as child sexual abuse material"；公开与分享的云内容 "is subject to review for intellectual property issues and safety concerns" | [隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html) |
| 积分账本 | "Evoto Smart Points" 余额在 Photo Editor、Cloud、Instant、手机与桌面之间共享，可兑换额度与存储 | [积分计划](https://www.evoto.ai/loyalty) |

### 数据处理（依文档记载）

隐私政策写明 "When the internal functions of the Software are insufficient to provide you services in full, we may upload your content to our web server for further processing"，这些内容 "will be stored on our web server to make it more convenient for your future editing"，并且 "Based on the need to improve our products and services, we may collect the content you upload in certain scenarios, and you agree to give us full authorization to engage in this behavior. If you do not agree with us collecting your content, you can turn it off in the software settings"（[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)；最后更新 2025-06-20）。同一政策还记载了 "as permitted by law" 的跨境传输、面向欧盟收件人的 GDPR 邮件 opt-in、通过邮件 `contactus@evoto.ai` 提出的删除请求 "within 72 hours" 处理、iPad 上采集 IDFA 并提供应用内追踪关闭选项，以及公司 "not knowingly collect any information from any minors under the age of 16" 的表述。

`about` 页给出的默认设定不同："Evoto never uses your photos to train AI models without your explicit permission"，并在 "Our Commitments, Plainly Stated" 中写道："Transparency — We don't use your photos to train our models unless you explicitly opt in. No buried terms. No surprises."（[关于页](https://www.evoto.ai/about)；访问于 2026-08-12）。2026-04-29 的版本说明再次表述为 "Evoto does not use your images or data to train generative AI models without your explicit permission"（[版本说明](https://www.evoto.ai/release-notes)），2026 年 1 月的声明还补充 "We source our data exclusively through commercially licensed and purchased imagery"（[Digital Camera World，2026-01-21](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash)）。政策里"默认开启、可在设置中关闭"的措辞与营销页面"未经明确许可绝不使用"的措辞，在此按原样并列记录 —— 见 `备注`。

条款还要求美国用户确保其内容 "does not contain sensitive data as defined by regulations such as the Protecting Americans' Data from Foreign Surveillance Act (PADFA)"，对用户内容免责，并把责任上限设为 "the last licensing fee you paid"（[服务条款](https://res.evoto.ai/ui/www/policy/terms.html)；更新于 2024-03-22）。

### 招聘所需技术背景

`evoto.ai` 上没有招聘页（2026-08-12 检查时 `/careers`、`/jobs` 与 `/company/careers` 均返回 HTTP 404），也未找到一手的职位发布。日本创业公司数据库中该日本主体的档案写着 現在公開中の求人情報がありません（"目前没有公开的招聘信息"），规模写作 10人以下（[スタクラ](https://startupclass.co.jp/online/companies/1846/)；访问于 2026-08-12）。LinkedIn 的职位页面未被查阅；一条搜索结果摘要提到大客户经理与市场类岗位，未经证实。公司未公布任何技术栈要求、职级门槛或面试流程 —— 见 `备注`。

### 行业领域

工作范围横跨专业摄影生产——RAW 处理与相机色彩配置、跨六家以上相机厂商的联机拍摄、大批量选片与批量交付、可用于印刷的导出，以及活动图库的交付与校对（[版本说明](https://www.evoto.ai/release-notes)、[instant.evoto.ai](https://instant.evoto.ai/)）——同时涉及对可识别自然人的面部与身体编辑，这把产品置于个人数据法规之下：站点提到 GDPR 与 CCPA，日本主体持有基于 JIS Q 15001 的隐私标志，条款援引 PADFA，隐私政策处理跨境传输、16 岁以下未成年人以及云内容的自动扫描（[关于页](https://www.evoto.ai/about)、[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)、[PR TIMES，2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html)）。商业上则涉及消费级应用商店分发与应用内购买、额度账本与结转核算、按居住国征收增值税，以及日本的渠道代理关系（[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)、[PR TIMES，2024-12-27](https://prtimes.jp/main/html/rd/p/000000011.000132859.html)）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | `evoto.ai` 上未找到 | 2026-08-12 检查的路径 |
| 已公布的办公地点 | 威尔明顿（特拉华州）、新加坡、东京、首尔 | [关于页](https://www.evoto.ai/about)；访问于 2026-08-12 |
| 自述的团队分布 | "Our team spans 6 countries"；"A global product built by a globally distributed team" | [关于页](https://www.evoto.ai/about) |
| 日本主体规模 | 创业公司数据库写作 10人以下；政府企业信息平台显示涩谷一个事业所、4 名职员 | [スタクラ](https://startupclass.co.jp/online/companies/1846/)、[gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305)（记录更新于 2025-12-05） |
| 自述的工作方式 | "Every major product decision is tested against photographer feedback, not internal assumptions"；"We hire people who believe tools should be in service of the people using them" | [关于页](https://www.evoto.ai/about) |
| 工作语言 | 未作为政策公布。产品提供 13 种应用语言，站点提供 15 个语言版本；日本市场的销售与支持通过日本主体进行 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us)、[sitemap 索引](https://www.evoto.ai/sitemap_index.xml) |
| 薪资、福利、远程政策、签证支持、面试流程、流动率 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-08-12）：`www.evoto.ai` 首页、`/about`、`/company`、`/payment`、`/download`、`/download/guide`、`/release-notes`、`/loyalty`、`/webinar`、`/referral`、`/evoto-mobile`、`/ipad`，以及 `robots.txt`、`sitemap_index.xml`、`llms.txt`、`llms-full.txt`，并探测了 `/careers`、`/jobs`、`/press`、`/news`、`/security`、`/enterprise`、`/contact-sales`、`/ambassador`、`/terms`、`/privacy` 与 `/legal`；`res.evoto.ai/ui/www/policy/` 下的政策文件（条款、隐私、退款、Cookie）；`instant.evoto.ai`、`video.evoto.ai`、`academy.evoto.ai`、`support.evoto.ai`、`help.evoto.ai`、`forum.evoto.ai`、`community.evoto.ai`、`api.evoto.ai`、`blog.evoto.ai` 及其 WordPress REST API；已发布的桌面安装包及其代码签名证书；App Store、iTunes lookup API 与 Google Play 列表（含开发者信息区块）；`株式会社Truesight Japan` 的 PR TIMES 订阅源（20 篇新闻稿，2024-02-19 至 2026-06-15）及若干单篇稿件；PR Newswire；gBizINFO 与日本法人番号目录；新加坡 ACRA 数据镜像目录；GitHub、npm 与 PyPI；`evoto.ai` 的 Wayback Machine CDX 索引；Crunchbase、Tracxn、Latka 与 PitchBook 档案；LinkedIn；以及针对品牌名与各 Truesight 主体名的英文、日文、中文检索。

- **任何融资轮次、投资方、估值或股权结构。** `evoto.ai` 上没有新闻索引或投资人页面，也没有任何新闻稿提及融资。第三方数据库称"未融资"或"自筹"，但没有一手来源。
- **四个 Truesight 主体之间的公司关系。** `about` 页把新加坡、日本、韩国称作 "Branch"，但新加坡与日本的主体是各自独立注册的公司。未找到任何确立母子公司或持股关系的文件、披露或公司表述。特拉华州与韩国的登记记录均未取得。
- **员工人数。** 公司未公布。第三方数字相差两个数量级 —— 见下文。
- **工程团队所在地，以及技术博客或开源。** 博客（711 篇）的内容是摄影教程、SEO 对比页与产品公告；未找到技术文章、架构说明或模型描述。品牌名与主体名下均无 GitHub、npm 或 PyPI 存在。
- **功能背后的 AI 模型与供应商。** 站点与政策中没有任何地方点名模型、供应商、托管区域或第三方推理厂商；AWS 只作为承载上传数据的云服务商被提及。
- **哪些处理在本地、哪些在云端。** 桌面安装包约 2 GB，隐私政策称在"软件内部功能不足以完整提供服务时"会上传内容，但没有页面说明哪些功能需要上传。
- **ISO/IEC 27001 与 SOC 2 Type 2 的证据。** 两个徽标出现在站点上，但没有证书编号、认证范围、认证机构、审计期间或信任门户。只有日本的隐私标志带有可核验的登记编号与有效期。
- **薪资区间、远程政策、签证支持、福利与面试流程。** 没有招聘页；唯一找到的招聘信息载体是日本创业公司数据库，其上没有在招岗位。
- **客户数、营收、付费订阅数、额度消耗与留存数字。** 公司只公布取整的累计营销数字（"1M+"、"800M+"），口径为 "internal account and usage data reviewed as of 2026"。
- **创始人的全名、职业经历与此前所在公司。** 站点上只出现 "Mitta"；对外发稿中出现 "Mitta Zhang"；公司未公布任何履历、教育背景或此前雇主。
- **2026-08-12 对自动访问设限的来源：** Crunchbase、PitchBook、`sgpbusiness.com` 与 `diyphotography.net`（HTTP 403）；`houjin.jp`（无响应）。LinkedIn 对普通请求返回 HTTP 999，但以浏览器 User-Agent 可读到页面，因此上文引用的数字为直接读取。凡是无法读取的来源，措辞均来自搜索结果摘要或替代镜像并已相应标注。

### 不同来源之间的不一致

- **成立年份：** 公司称 2020 年（[关于页](https://www.evoto.ai/about)），其 LinkedIn 页面称 "TRUESIGHT PTE.LTD., established in 2020 in Singapore"（[LinkedIn](https://www.linkedin.com/company/evoto-ai)）；[PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/) 称 "founded in 2022 by AI and graphics specialists at Truesight Technology Inc."；[Tracxn](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) 称 2024 年。新加坡公司成立于 2022-07-13，日本公司成立于 2023 年 6 月（[companies.sg](https://www.companies.sg/business/202224238M/TRUESIGHT-PTE-LTD-)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)）；最早的营销站点存档为 2022-11-23（[Wayback](https://web.archive.org/web/20221123171058/https://evoto.ai/)）。
- **总部：** 站点写威尔明顿（特拉华州）（[关于页](https://www.evoto.ai/about)）；PetaPixel 写加州门洛帕克（[2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)）；Tracxn 写新加坡；当前 Windows 构建的 EV 代码签名证书写特拉华州 Newark（读取于 2026-08-12）。
- **由哪个主体运营服务：** 服务条款与退款政策署名 `TRUESIGHT PTE. LTD.`，并把争议交由新加坡法律与法院管辖（[服务条款](https://res.evoto.ai/ui/www/policy/terms.html)；更新于 2024-03-22），而站点页脚、`about` 页与 `llms.txt` 把位于美国的 `Truesight Technology Inc.` 呈现为公司主体。日文新闻稿在 2025 年 1 月称母公司为新加坡企业，到 2025 年 12 月改称美国企业（[PR TIMES，2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html)、[PR TIMES，2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html)）。
- **员工人数：** "a team of 500 employees"（[PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)）；公司自有 [LinkedIn](https://www.linkedin.com/company/evoto-ai) 页面自报规模 "501-1,000 employees"，同时列出 47 个员工档案（访问于 2026-08-12）；2026 年 "approximately 37 people"（[Latka](https://getlatka.com/companies/evoto.ai)）；日本主体 10人以下（[スタクラ](https://startupclass.co.jp/online/companies/1846/)），其涩谷事业所 4 名职员（[gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305)）。
- **谁代表日本主体：** PR TIMES 新闻稿及其公司概要写 代表取締役 Mitta Zhang／代表者名 張偉（[PR TIMES，2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)）；スタクラ 档案写 代表取締役社長 ウィリアム・ワン，并附富士通半导体背景（[スタクラ](https://startupclass.co.jp/online/companies/1846/)）。
- **训练数据的同意默认值：** 隐私政策称上传内容可被收集用于产品改进，使用即视为给予 "full authorization"，并可"在软件设置中"关闭（[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)；最后更新 2025-06-20）；而 `about` 页与 V7.1.5 版本说明称"未经你的明确许可"绝不会用照片训练模型（[关于页](https://www.evoto.ai/about)、[版本说明](https://www.evoto.ai/release-notes)）。
- **覆盖范围：** 站点写 "200+ countries and regions"，2025 年 9 月的采访写 "158 countries"（[关于页](https://www.evoto.ai/about)、[PetaPixel](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)）。
- **价格展示：** 付费页按地区返回不同币种与数字 —— 2026-08-12 默认返回美元，从东京出口访问时返回日元 —— 因此单独引用的价格只对特定地区成立（[付费页](https://www.evoto.ai/payment)）。

### 其他

- **法律文件比公司形象的更新更滞后。** 服务条款的更新日期是 2024-03-22，且完全为新加坡主体撰写，隐私政策最后更新于 2025-06-20，而站点现在呈现的是一家美国公司和四个办公地点；这些政策文件以静态 HTML 形式由 S3 资源域名提供，而不在站点自身的路由下（[服务条款](https://res.evoto.ai/ui/www/policy/terms.html)、[隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)）。
- **公开表面高度面向 SEO。** `llms-full.txt` 索引 140 个页面，其中 126 个是功能落地页（"AI Double Chin Remover"、"AI Pet Leash Remover" 等），6 个是与 Lightroom、Photoshop、Capture One、Luminar Neo 和 Imagen AI 的正面对比页，每个页面都有 Markdown 孪生版本；2026 年 1 月的声明把被下线的 AI 证件照生成器描述为 "intended as a secondary page focused on SEO"（[llms.txt](https://www.evoto.ai/llms.txt)、[PetaPixel，2026-01-15](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/)）。
- **站点明确允许用其内容训练 AI。** `robots.txt` 带有 `Content-Signal: ai-train=yes, search=yes, ai-input=yes` 响应头（[robots.txt](https://www.evoto.ai/robots.txt)；观察于 2026-08-12）。
- **产品线在约三年内从一个应用扩展到六个形态：** 2023 年只有桌面版，2024 年 12 月推出 iPad 版，2025 年 9 月在 Evoto One 活动上公布 Instant 与 Video，手机版 2024 年 11 月在 iOS 上线并于 2025 年 12 月在日本发布公告（[版本说明](https://www.evoto.ai/release-notes)、[PR TIMES，2024-12-16](https://prtimes.jp/main/html/rd/p/000000009.000132859.html)、[PetaPixel，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)、[PR TIMES，2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html)）。
- **日本是唯一拥有独立公开传播渠道的市场。** 其 PR TIMES 订阅源列出 20 篇新闻稿，日期从 2024-02-19 到 2026-06-15；该主体持有隐私标志、通过具名代理商销售，并发布自己的日文产品手册；最近两篇日文稿是关于影楼与修图态度的消费者调查，而非产品新闻（[PR TIMES 公司订阅源](https://prtimes.jp/main/html/searchrlp/company_id/132859)；访问于 2026-08-12）。
- **站点提供繁体中文版本但没有简体中文版本**，而桌面应用与 iOS 应用列出的是通用的 `ZH` 语言代码（[robots.txt](https://www.evoto.ai/robots.txt)、[iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us)）。
- **免费边界在 2025 年发生过变化。** 在桌面 v6.1 及之后的版本上，色彩调整、裁剪旋转与手动工具对付费用户导出不再消耗额度，iPad 版、Instant 与更早的桌面版不在其列（[PR TIMES，2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)）。

---

## 资料来源

**官方**

- [官网](https://www.evoto.ai/) · [关于页](https://www.evoto.ai/about) · [公司页](https://www.evoto.ai/company)
- [付费页](https://www.evoto.ai/payment) · [下载页](https://www.evoto.ai/download) · [版本说明](https://www.evoto.ai/release-notes)
- [积分计划](https://www.evoto.ai/loyalty) · [推荐计划](https://www.evoto.ai/referral) · [Webinar](https://www.evoto.ai/webinar)
- [robots.txt](https://www.evoto.ai/robots.txt) · [sitemap 索引](https://www.evoto.ai/sitemap_index.xml) · [llms.txt](https://www.evoto.ai/llms.txt) · [llms-full.txt](https://www.evoto.ai/llms-full.txt)
- [服务条款](https://res.evoto.ai/ui/www/policy/terms.html)（更新于 2024-03-22） · [隐私政策](https://res.evoto.ai/ui/www/policy/privacy.html)（最后更新 2025-06-20） · [退款政策](https://res.evoto.ai/ui/www/policy/refund.html) · [Cookie 政策](https://res.evoto.ai/ui/www/policy/cookies.html)
- [Evoto Instant](https://instant.evoto.ai/) · [Evoto Video](https://video.evoto.ai/) · [Academy](https://academy.evoto.ai) · [支持中心](https://support.evoto.ai/) · [社区论坛](https://forum.evoto.ai)
- [博客](https://blog.evoto.ai/) —— [WordPress REST API 文章索引](https://blog.evoto.ai/wp-json/wp/v2/posts?per_page=1) · [Capterra 2026 公告，2026-03-27](https://blog.evoto.ai/evoto-capterra-2026-press-release/)
- 资源域名上的桌面安装包 —— [Windows 7.3.0-512](https://res.evoto.ai/package/7.3.0-512/Evoto_Setup_7.3.0-512.exe) · [macOS arm64 7.3.0-512](https://res.evoto.ai/package/7.3.0-512/Evoto-7.3.0-512_arm64.dmg) · [日文产品手册（PDF）](https://res.evoto.ai/ja/evoto-manural.pdf)
- ["Online AI Headshot Generator" 页面存档，抓取于 2026-01-10](https://web.archive.org/web/20260110205938/https://www.evoto.ai/features/ai-headshot-generator) · [官网存档，抓取于 2022-11-23](https://web.archive.org/web/20221123171058/https://evoto.ai/)

**新闻稿**

- [PR Newswire —— "Evoto Ends Photographer Burnout at Imaging USA 2026 with Revolutionary All-in-One Workflow"，2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)
- [PR TIMES —— 株式会社Truesight Japan 新闻稿订阅源（日文）](https://prtimes.jp/main/html/searchrlp/company_id/132859)
- [PR TIMES —— 一部機能を無料化，2025-12-05（日文）](https://prtimes.jp/main/html/rd/p/000000016.000132859.html) · [iPhone版リリース，2025-12-25（日文）](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) · [プライバシーマーク取得，2025-01-31（日文）](https://prtimes.jp/main/html/rd/p/000000013.000132859.html) · [ラボネットワークと代理店契約，2024-12-27（日文）](https://prtimes.jp/main/html/rd/p/000000011.000132859.html) · [Evoto iPad リリース，2024-12-16（日文）](https://prtimes.jp/main/html/rd/p/000000009.000132859.html) · [CP+2025 出展，2025-02-20（日文）](https://prtimes.jp/main/html/rd/p/000000014.000132859.html) · [PHOTONEXT 出展，2024-05-31（日文）](https://prtimes.jp/main/html/rd/p/000000004.000132859.html) · [ブライダル産業フェア 出展，2024-04-30（日文）](https://prtimes.jp/main/html/rd/p/000000003.000132859.html) · [CP+2024 出展，2024-02-19（日文）](https://prtimes.jp/main/html/rd/p/000000001.000132859.html)
- [ラボネットワーク —— 代理店契約締結のお知らせ，2024-12-27（日文）](https://www.labonetwork.co.jp/news/24122701/)

**应用商店列表**

- [App Store —— Evoto-AI Photo Editor&Retouch](https://apps.apple.com/us/app/evoto-ai-photo-editor-retouch/id6596737043) · [iTunes lookup API 记录](https://itunes.apple.com/lookup?id=6596737043&country=us)
- [iTunes lookup API —— Evoto Instant](https://itunes.apple.com/lookup?id=6749685404&country=us) · [Apple 开发者页面 —— TRUESIGHT PTE. LTD.](https://apps.apple.com/us/developer/truesight-pte-ltd/id1760458737)
- [Google Play —— com.truesight.evoto](https://play.google.com/store/apps/details?id=com.truesight.evoto)

**第三方报道与档案**

- [PetaPixel —— "Evoto Believes it Can Beat Adobe at Its Own Game"，2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)
- [PetaPixel —— "Evoto Alienated Photographers By Releasing a Tool Designed to Replace Them"，2026-01-15](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/)
- [Digital Camera World —— "We missed the mark, and we are sorry"，2026-01-21](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash)
- [Digital Camera World —— Evoto AI 评测，2026-02-13](https://www.digitalcameraworld.com/tech/software/evoto-ai-review)
- [The Phoblographer —— "Evoto AI Headshot Generator Apology is BS"，2026-01-14](https://www.thephoblographer.com/2026/01/14/evoto-ai-headshot-generator-anti-photographer/)
- [DIY Photography —— "Evoto Angers Photographers by a Surprise AI Headshot Launch"（2026-08-12 对自动访问返回 HTTP 403）](https://www.diyphotography.net/evoto-angers-photographers-by-a-surprise-ai-headshot-launch-but-is-evoto-the-villain-here/)
- [スタクラ —— 株式会社Truesight Japan 企业档案（日文）](https://startupclass.co.jp/online/companies/1846/)
- [gBizINFO —— 株式会社Truesight Japan，法人番号 5020001152305（日文）](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305)
- [companies.sg —— TRUESIGHT PTE. LTD.（202224238M）](https://www.companies.sg/business/202224238M/TRUESIGHT-PTE-LTD-) · [sgpbusiness —— TRUESIGHT PTE. LTD.（2026-08-12 对自动访问返回 HTTP 403）](https://www.sgpbusiness.com/company/Truesight-Pte-Ltd)
- [Tracxn —— Evoto 公司档案](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) · [Latka —— Evoto AI 营收档案](https://getlatka.com/companies/evoto.ai) · [Crunchbase —— Evoto（2026-08-12 对自动访问返回 HTTP 403）](https://www.crunchbase.com/organization/evoto)
- [PitchBook —— Truesight (China) 档案](https://pitchbook.com/profiles/company/503403-85) · [PitchBook —— TrueSight Technology 档案](https://pitchbook.com/profiles/company/437673-34) —— 两者 2026-08-12 对自动访问均返回 HTTP 403；均未被确认就是本公司
- [LinkedIn —— Evoto AI 公司页面](https://www.linkedin.com/company/evoto-ai)
