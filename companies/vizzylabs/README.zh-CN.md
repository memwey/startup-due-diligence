# Vizzy Labs

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-14。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-14。英文版为原始版本。

## 摘要

Vizzy Labs 把创作者拍摄的短视频卖给消费级品牌。面向品牌的站点自称 "The _Automatic_ UGC Video Platform for Real Growth —— High-Quality UGC Videos, instantly. Paid by Performance"，由四个具名 agent 分别负责趋势分析、创作者筛选、效果复盘与结算（[官网](https://www.vizzylabs.ai/)；访问于 2026-08-14）。第二个入口 `app.vizzylabs.ai` 是订阅制产品 "Vizzy AI | AI Video Search Engine for Creators"，第三个入口 `vizzycircle.com` 则用来招募创作者本身。所有政策文件中出现的法律主体都是 `Vispie Inc`，该主体此前的品牌 `Vispie AI` 至少到 2025 年初还运营在 `vispie.com` 上（[服务条款](https://www.vizzylabs.ai/terms)；最后更新 2025-02-13）—— 见 `品牌与法律实体`。

- 规模数字全部为自述，且口径互不衔接：品牌站显示已生成 "2,159" 条视频、"674.3M" 总播放、"187.8M" 总互动，并称 "We analyze 5M+ new videos every day"（[官网](https://www.vizzylabs.ai/)）；创作者站显示 "10,000+ Creators"、"$2M+ Deals Closed"、"50+ Brand Partners"（[vizzycircle.com](https://www.vizzycircle.com/)）。唯一可独立计数的是 Vizzy Circle 的 Discord 服务器：17,679 名成员、367 人在线（[Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true)；观察于 2026-08-14）。
- 未找到任何融资公告。官网页脚带有 "🚀 Venture Backed" 标识；一个招聘页写着 "backed by Sequoia Capital"（[Creative Strategist 岗位页](https://www.vizzylabs.ai/careers/creative-strategist)）；[CB Insights](https://www.cbinsights.com/company/vizzy-labs) 则写作 "Seed VC"，投资方列为 GV、Bain Capital Ventures 与 Forerunner Ventures，未给金额与日期 —— 见 `融资`。
- 创作者侧的分成规则是公开的："$30 flat fee + performance bonus ($10–$1,500) starting at 1K views"，并设有 "Prime Creator program for higher flat fees"；加入免费，申请走 Google 表单，社区在 Discord（[vizzycircle.com](https://www.vizzycircle.com/)；访问于 2026-08-14）。
- 公司在自己的招聘页里描述了两种不同的业务：三个岗位写的是 UGC 与品牌视频，另两个写的是 "the future of interactive drama: short-form stories where viewers decide what happens next"（[招聘页](https://www.vizzylabs.ai/careers)；访问于 2026-08-14）—— 见 `备注`。
- 工程方面的证据来自公开资产：两个站点都是部署在 Vercel 上的 SvelteKit；应用的打包文件里引用了 PostHog、Umami、Sentry、Google Tag Manager、Google Identity Services、Facebook Connect 与 Rewardful，并暴露出视频格式检索、创作者统计、Meta 广告账户代理和 Instagram 内容发现等 API 路径（打包文件检查于 2026-08-14）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | Vizzy Labs / Vizzy（面向品牌）、Vizzy AI（`app.vizzylabs.ai`）、Vizzy Circle（面向创作者） | [官网](https://www.vizzylabs.ai/)、[app.vizzylabs.ai](https://app.vizzylabs.ai/product)、[vizzycircle.com](https://www.vizzycircle.com/)；访问于 2026-08-14 |
| 法律主体 | "Vispie Inc" —— 服务条款与隐私政策中都以其为运营方 | [服务条款](https://www.vizzylabs.ai/terms)、[隐私政策](https://www.vizzylabs.ai/privacy)；最后更新 2025-02-13 |
| 对创作者的主体表述 | "Vizzy Circle is operated by VizzyLabs (Vispie Inc.), a venture-backed AI video analytics company based in Stanford, CA … We are a registered U.S. company — not a scam, not a middleman" | [vizzycircle.com FAQ](https://www.vizzycircle.com/)；访问于 2026-08-14 |
| 注册地址 | 所查阅的页面均未公布 | 见 `备注` |
| 自述所在地 | 创作者站写 "Stanford, CA"；第三方档案写 "San Francisco, California, United States"；招聘页写 "SF / Hybrid / Remote" | [vizzycircle.com](https://www.vizzycircle.com/)、[CB Insights](https://www.cbinsights.com/company/vizzy-labs)、[招聘页](https://www.vizzylabs.ai/careers) |
| 成立年份 | 公司未表述；第三方档案写 2025 年 | [CB Insights](https://www.cbinsights.com/company/vizzy-labs)；访问于 2026-08-14 |
| 域名注册 | `vispie.com` 注册于 2024-03-10（GoDaddy，注册人 "Domains By Proxy, LLC"）；`vizzylabs.ai` 注册于 2024-12-08（GoDaddy）；`vizzycircle.com` 注册于 2026-01-06（Cloudflare） | WHOIS 记录读取于 2026-08-14 |
| 版权声明 | 品牌站写 "© 2025 Vizzy. All rights reserved."；创作者站写 "© 2026 Vizzy Circle. All rights reserved." | [官网](https://www.vizzylabs.ai/)、[vizzycircle.com](https://www.vizzycircle.com/) |
| 公开联系方式 | `support@vispie.com`（隐私事务联系邮箱）；应用打包文件中出现 Calendly 链接 `calendly.com/yohanlee/30-minute-meeting`；品牌站通过页面内 "Tell us about your product" 表单收集线索 | [隐私政策](https://www.vizzylabs.ai/privacy)，应用 JavaScript 打包文件检查于 2026-08-14 |
| 具名人员 | Yohan Lee（Founder / CEO）、Adham Zaki（Founding Engineer） | [The Org](https://theorg.com/org/vizzy-labs)、[Luma 活动页](https://luma.com/jfwqqbcv) |
| 员工人数 | 公司未公布。LinkedIn 自报 "11-50 employees" 并列出 13 个员工档案；The Org 只列了 2 人 | [LinkedIn](https://www.linkedin.com/company/vizzylabs)、[The Org](https://theorg.com/org/vizzy-labs)；访问于 2026-08-14 |
| 社交账号 | Instagram `@vizzy_labs`（168 粉丝、8 条帖子）、X `@vizzylabs_ai`（5 粉丝，2025 年 5 月注册）、TikTok `@vizzy_labs`、Facebook 页面 `vizzylabs` 与 `vizzycircle`、LinkedIn `vizzylabs`（947 关注） | 各账号访问于 2026-08-14 |
| 创作者社区 | Discord 服务器 "Vizzy Circle"（guild id `1413650512359985254`）：约 17,679 名成员、367 人在线；邀请链接由 "Amy - Vizzy Account Manager" 发出 | [Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true)；观察于 2026-08-14 |
| 法律文件 | 服务条款与隐私政策，均标注 "Last updated: Feb 13th, 2025"；没有 Cookie 政策、DPA、安全页面或子处理者清单 | [服务条款](https://www.vizzylabs.ai/terms)、[隐私政策](https://www.vizzylabs.ai/privacy) |
| 托管 | `www.vizzylabs.ai` 与 `www.vizzycircle.com` 都返回 `server: Vercel`；`www.vizzylabs.ai` 还返回 `x-sveltekit-page: true` | 响应头观察于 2026-08-14 |

**公司自称的品牌与客户**：品牌站的 "Success stories" 版块列出 "MrBeast Chocolate —— 2.3M views"、"Manus AI —— +67% conversions"、"Study X —— 1M+ installs"，其上方的 logo 条为 "alpha, buoy, chance, chime, dose, remini, rocket"（[官网](https://www.vizzylabs.ai/)；访问于 2026-08-14）。创作者站称自己 "trusted by brands like Madnesz & Cluely"，并有一条更长的 logo 条："alpha, buoy, chance, chime, dose, honeylove, remini, rocket, scoopz, tarte"（[vizzycircle.com](https://www.vizzycircle.com/)；访问于 2026-08-14）。在所查阅的来源中，这些合作关系都没有从被点名品牌自身的材料中得到确认。

**活动**：公司出现在 StartX 的一场 "Founder Spotlight" 线上活动中，标题为 "Explore the growth tactics behind viral apps like Cluely, Turbolearn, and PingoAI with Vizzy Labs"，主办方是斯坦福背景的加速器社区 StartX；该活动在页面上显示为已结束且未标注日期（[Luma](https://luma.com/jfwqqbcv)；访问于 2026-08-14）。

### 品牌与法律实体

| 名称 | 类型 | 期间／状态 | 来源中表述的关系 | 来源 |
|---|---|---|---|---|
| Vizzy Labs / Vizzy | 面向品牌的公开品牌 | 当前 | 用于站点、招聘页、社交账号与对外介绍的名称 | [官网](https://www.vizzylabs.ai/) |
| Vispie Inc | 法律主体 | 当前 | 服务条款与隐私政策中作为服务运营方；对创作者表述为创作者协议的适用主体 | [服务条款](https://www.vizzylabs.ai/terms)、[vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| Vispie AI | `vispie.com` 上的旧品牌 | 2025-01-30 的存档抓取时仍在线；2026-08-14 时 `www.vispie.com` TLS 握手失败 | 定位为 "Your Data + Our Trend Engine = Viral Videos in Minutes"、"Trusted by 20+ enterprises"，页脚写 "© VisPie.AI. 2024" | [Wayback 存档，2025-01-30](https://web.archive.org/web/20250130073405/http://www.vispie.com/) |
| Vizzy Circle | `vizzycircle.com` 上的创作者网络品牌 | 域名注册于 2026-01-06 | "operated by VizzyLabs (Vispie Inc.)" | [vizzycircle.com](https://www.vizzycircle.com/) |
| 其他叫 "Vizzy" 的公司 | 同名冲突 | — | 伦敦一家招聘领域创业公司同样以 Vizzy 为名，2025 年 4 月由 Adjuvo 领投融资 365 万英镑；检索 "Vizzy" 的融资数据库结果常常返回它而不是本公司 | [UNLEASH，2025](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/) |

服务条款对业务的描述与其说匹配当前官网，不如说匹配旧产品："Vispie Inc provides an AI search and analysis service for advertising videos. Vispie Inc is available via www.vizzylabs.ai"（[服务条款](https://www.vizzylabs.ai/terms)；最后更新 2025-02-13）。未取得 `Vispie Inc` 的任何公司登记文件，因此其注册州、注册地址与高管在此均未确立 —— 见 `备注`。

---

## 产品

### 产品形态

| 形态 | 面向对象 | 是什么 | 来源 |
|---|---|---|---|
| `www.vizzylabs.ai` | 品牌方 | "The Automatic UGC Video Platform for Real Growth. High-Quality UGC Videos, instantly. Paid by Performance." —— "Vizzy's AI recruits, evaluates, and manages real and AI creators, so you get high-performing UGC on autopilot" | [官网](https://www.vizzylabs.ai/)；访问于 2026-08-14 |
| `app.vizzylabs.ai` | 创作者与营销人员 | "Vizzy AI \| AI Video Search Engine for Creators" —— 创意研究、视频分镜分析、爆款视频检索、趋势创意追踪、视频脚本提取，以及一个接入 Meta 的创意效果看板 | [app.vizzylabs.ai](https://app.vizzylabs.ai/product)；访问于 2026-08-14 |
| `www.vizzycircle.com` | 创作者 | "Vizzy Circle —— Premium UGC Creator Network"：申请、被匹配到品牌campaign、接受一对一辅导、交付 UGC、拿钱 | [vizzycircle.com](https://www.vizzycircle.com/)；访问于 2026-08-14 |
| Discord + Google 表单 | 创作者 | 入口与社区：一份 "Vizzy Circle Creator Network Application" Google 表单和一个 Discord 服务器 | [申请表单](https://docs.google.com/forms/d/e/1FAIpQLSd_ooDJ4m5hFQecHzZ2BEyo3DO0GbQ3_6-q0VvmDdoy9PI8Lw/viewform)、[Discord 邀请](https://discord.gg/MZhbHg7Q5Z) |

### 页面描述的四个 agent 流程

品牌站把产品组织成四步的 "Vizzy's Agentic Workflow"（[官网](https://www.vizzylabs.ai/)；访问于 2026-08-14）：

| 步骤 | Agent | 页面称其做什么 |
|---|---|---|
| 1 | Trend & Competitor Agent | "We analyze 5M+ new videos every day to detect viral formats, trending audio and winning hooks — before they peak"；追踪 "competitor creatives, formats, and performance signals" |
| 2 | Creator Sourcing Agent | "Creators are sourced based on historical performance, audience match, and format compatibility — selecting creators with the highest probability of success for your app" |
| 3 | Performance Review Agent | "After filming, AI agents perform automated analysis, with human experts validating critical decisions" |
| 4 | Data Optimization & Payout Agent | "Once videos go live, performance data is processed through our agent to automate payouts and improve creator selection and creative decisions over time" |

### 商业化

| 项目 | 内容 | 来源 |
|---|---|---|
| 品牌侧模式 | "Paid by Performance"；未公布价目表、报价卡或起投门槛；页面上唯一的行动入口是 "Tell us about your product" 表单 | [官网](https://www.vizzylabs.ai/)；访问于 2026-08-14 |
| 应用订阅档位 | Basic 免费（"3 searches per day"，功能受限）；Creator 每月 29 美元，按年付为每月 25 美元；Pro 每月 99 美元，按年付为每月 79 美元；Enterprise "Custom —— Contact Sales"；年付标注 "(20% off)" | [app.vizzylabs.ai](https://app.vizzylabs.ai/product)；访问于 2026-08-14 |
| 各档位限额 | Creator：50 次视频分镜分析、每月 100 次创意研究、无限访问 "50M viral videos"、无限趋势创意追踪与脚本提取。Pro：1,000 次分镜分析、无限创意研究。Enterprise 另加 "Personalized onboarding and CSM"、"Personalized creative reports"、"Customized competitor tracker" | [app.vizzylabs.ai](https://app.vizzylabs.ai/product) |
| 创作者报酬 | "$30 flat fee + performance bonus ($10–$1,500) starting at 1K views"；"Top performers can join our Prime Creator program for higher flat fees"；"Rates may vary by campaign" | [vizzycircle.com FAQ](https://www.vizzycircle.com/)；访问于 2026-08-14 |
| 创作者成本 | "Vizzy Circle is 100% free to join — no paid onboarding, no hidden fees, no product purchases required, and no upfront costs of any kind. We pay you; you never pay us. If a campaign involves a product, it will be provided to you at no cost." | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| 创作者合同 | "Yes, there is a written creator agreement that outlines compensation, deliverables, payment terms, and content usage rights before you start any campaign … All terms and conditions are governed by VizzyLabs (Vispie Inc.)"；协议本身未公开 | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| 创作者门槛 | "No experience and zero followers required"；"many creators go from complete beginners to earning $1,000+/month"；"Most active creators run 3-4 campaigns simultaneously … Top performers managing multiple campaigns scale to $3K-$10K monthly" | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| 推荐／联盟追踪 | 应用打包文件加载 `r.wdfl.co/rw.js`（Rewardful），表明接入了联盟推广追踪 | 应用 JavaScript 打包文件检查于 2026-08-14 |

### 定位的历次变化

公开定位在约十八个月内变了三次，每一版都有存档可查。

| 日期 | 站点与标题 | 当时的定位原文 |
|---|---|---|
| 2025-01-30 | `vispie.com` —— "Vispie AI" | "Your Data + Our Trend Engine = Viral Videos in Minutes"；"Trusted by 20+ enterprises"；功能列为爆款视频发现、竞品检索、视频分析与 "Automatic Batch Video Editing Powered by Trend AI"（[Wayback](https://web.archive.org/web/20250130073405/http://www.vispie.com/)） |
| 2025-06-18 | `vizzylabs.ai` —— "Vizzy Labs \| AI-Powered TikTok Ad Creative Strategist" | "AI Creative Strategist to Ship Winning Ads. Find winning video formats instantly from our ads library with 500,000,000+ TikTok & Instagram ads and organic content"；页面由 Framer 构建（[Wayback](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/)） |
| 2025-12-08 | `vizzylabs.ai` —— "Vizzy AI \| AI Video Search Engine for Creators" | 订阅制产品，Creator／Pro／Enterprise／Basic 四档至今仍在 `app.vizzylabs.ai` 上；"Unlimited access to 50M viral videos"（[Wayback](https://web.archive.org/web/20251208202228/https://www.vizzylabs.ai/)） |
| 2026-05-17 至 2026-08-14 | `vizzylabs.ai` —— "Vizzy: Automatic UGC Video Platform" | 当前的四 agent、按效果付费的 UGC 定位（[Wayback](https://web.archive.org/web/20260517154252/https://www.vizzylabs.ai/)、[官网](https://www.vizzylabs.ai/)） |

### 公开披露的规模变化

| 日期 | 披露的数字 | 来源 |
|---|---|---|
| 2024-03-10 | `vispie.com` 域名注册 | WHOIS 读取于 2026-08-14 |
| 2024-12-08 | `vizzylabs.ai` 域名注册 | WHOIS 读取于 2026-08-14 |
| 2025-01-30 | Vispie AI："Trusted by 20+ enterprises" | [Wayback](https://web.archive.org/web/20250130073405/http://www.vispie.com/) |
| 2025-05 | X 账号 `@vizzylabs_ai` 注册 | [X 主页](https://x.com/vizzylabs_ai)；访问于 2026-08-14 |
| 2025-06-18 | 广告素材库表述为 "500,000,000+ TikTok & Instagram ads and organic content" | [Wayback](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/) |
| 2025-12-08 | 应用套餐文案写 "Unlimited access to 50M viral videos" | [Wayback](https://web.archive.org/web/20251208202228/https://www.vizzylabs.ai/) |
| 2026-01-06 | `vizzycircle.com` 域名注册 | WHOIS 读取于 2026-08-14 |
| 无日期（已结束活动） | "engineered over 650M views on social media"；服务对象是 "apps backed by a16z, GV, and Forerunner Ventures"；创始人 "led the TikTok Creative Center product, growing it from an internal tool to a platform used by 6M advertisers" | [Luma / StartX Founder Spotlight](https://luma.com/jfwqqbcv) |
| 访问于 2026-08-14 | 品牌站："2,159" 条已生成视频、"674.3M" 总播放（"Avg 312.3K views per video"）、"187.8M" 总互动（"Avg 87K interactions per video"）、每日分析 "5M+" 条新视频 | [官网](https://www.vizzylabs.ai/) |
| 访问于 2026-08-14 | 创作者站："10,000+ Creators"、"$2M+ Deals Closed"、"50+ Brand Partners" | [vizzycircle.com](https://www.vizzycircle.com/) |
| 观察于 2026-08-14 | Discord 服务器：约 17,679 名成员、367 人在线 | [Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true) |
| 访问于 2026-08-14 | LinkedIn 947 关注、"11-50 employees"、13 个员工档案；Instagram 168 粉丝、8 条帖子；X 5 粉丝 | [LinkedIn](https://www.linkedin.com/company/vizzylabs)、[Instagram](https://www.instagram.com/vizzy_labs/)、[X](https://x.com/vizzylabs_ai) |

除 "$2M+ Deals Closed" 这条横幅数字外，未公布任何营收、付费客户数、campaign 数量或结算总额 —— 见 `备注`。

### 公开表述的计划

公司没有路线图页面。找到的前瞻性表述都在招聘文案里："Building the future of brand video — where AI meets creativity to transform how brands create and scale video content"（[招聘页](https://www.vizzylabs.ai/careers)）；另有两个岗位写着 "building the future of interactive drama: short-form stories where viewers decide what happens next"，并把 "drama apps (ReelShort, DramaBox, Mango, or similar) or game platforms (Roblox, Epic, or similar)" 的经验列为 "a major plus"（[Scriptwriters & Producers 岗位页](https://www.vizzylabs.ai/careers/ai-agent-engineer)、[Marketing Roles 岗位页](https://www.vizzylabs.ai/careers/marketing-roles)；访问于 2026-08-14）。在应用内，"TikTok" 与 "Youtube" 作为广告平台连接器标注为 "Coming soon"，Meta 是唯一已上线的连接器（[app.vizzylabs.ai](https://app.vizzylabs.ai/product)）。

---

## 创始人

**Yohan Lee** —— The Org 上列为 "Founder"，LinkedIn 被索引为 "Founder @ Vizzy Labs | Stanford"；该 LinkedIn 个人页 2026-08-14 对自动访问返回 HTTP 999，未被直接读取（[The Org](https://theorg.com/org/vizzy-labs/org-chart/yohan-lee)、[LinkedIn](https://www.linkedin.com/in/yohanlee12/)）。StartX 活动页把他描述为 "the founder and CEO of Vizzy Labs, and former TikTok Creative AI PM, where he led the TikTok Creative Center product, growing it from an internal tool to a platform used by 6M advertisers"（[Luma](https://luma.com/jfwqqbcv)；访问于 2026-08-14）。这个名字在产品内部得到印证：应用的 JavaScript 打包文件中包含预约链接 `https://calendly.com/yohanlee/30-minute-meeting`（打包文件检查于 2026-08-14）。所查阅的来源中未公布其教育或任职的起止时间，也没有 TikTok 之外的其他任职经历。

**Adham Zaki** —— 列为 "Founding Engineer"（[The Org](https://theorg.com/org/vizzy-labs)；访问于 2026-08-14）。没有其他公开信息。

公司只以概括方式描述创始团队，且各招聘页写法不一：两个岗位写 "founded by Stanford and Google alumni"，另一个写 "Founded by operators from TikTok, Google, and Stanford"（[Scriptwriters & Producers 岗位页](https://www.vizzylabs.ai/careers/ai-agent-engineer)、[Marketing Roles 岗位页](https://www.vizzylabs.ai/careers/marketing-roles)、[Creative Strategist 岗位页](https://www.vizzylabs.ai/careers/creative-strategist)）。

创作者社区的公开 Discord 邀请由一个署名 "Amy - Vizzy Account Manager" 的账号发出（[Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true)；观察于 2026-08-14）。`vizzylabs.ai` 上没有团队页、管理层页或关于页 —— `/about`、`/team` 与 `/company` 都跳转到 `app.vizzylabs.ai` 且没有对应内容（路径检查于 2026-08-14）。

---

## 融资

截至 2026-08-14，在所查阅的公开来源中未找到公司发布的任何融资公告。三个站点都没有新闻页、投资人页或融资表述。下表记录公司自身的说法与第三方档案的说法。

| 日期 | 说法 | 金额 | 具名投资方 | 来源 |
|---|---|---|---|---|
| 访问于 2026-08-14 | 官网页脚区域的 "🚀 Venture Backed" 标识 | 未说明 | 无 | [官网](https://www.vizzylabs.ai/) |
| 访问于 2026-08-14 | "Founded by operators from TikTok, Google, and Stanford and backed by Sequoia Capital, Vizzy Labs is already powering campaigns across fast-growing consumer brands, generating millions of views each month" | 未说明 | Sequoia Capital | [Creative Strategist 岗位页](https://www.vizzylabs.ai/careers/creative-strategist) |
| 访问于 2026-08-14 | "a Silicon Valley top VC-backed startup"；"backed by some of the top VCs in the space" | 未说明 | 无 | [Scriptwriters & Producers 岗位页](https://www.vizzylabs.ai/careers/ai-agent-engineer)、[AI Video Creators 岗位页](https://www.vizzylabs.ai/careers/ai-video-creators) |
| 访问于 2026-08-14 | "a venture-backed AI video analytics company based in Stanford, CA" | 未说明 | 无 | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| 访问于 2026-08-14 | "latest funding round is Seed VC"；成立于 2025 年；总部在旧金山 | 未说明 | GV、Bain Capital Ventures、Forerunner Ventures | [CB Insights](https://www.cbinsights.com/company/vizzy-labs) |

对第三方数字有两点需要注意。其一，a16z、GV、Forerunner Ventures 这三个名字，在公司自己的活动介绍里是用来形容其*客户*的投资方，而不是 Vizzy Labs 的投资方（"Working with apps backed by a16z, GV, and Forerunner Ventures"，[Luma](https://luma.com/jfwqqbcv)）；所查阅的来源中没有一处把这两种用法对上。其二，在通用搜索和融资数据库里检索 "Vizzy" 会返回另一家伦敦的招聘领域创业公司，其 2025 年 4 月由 Adjuvo 领投融资 365 万英镑（[UNLEASH](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/)、[Crunchbase 融资轮次页](https://www.crunchbase.com/funding_round/vizzy-6454-seed--2028b984)），那一轮不是本公司的。金额、日期、领投方与估值在所查阅的任何来源中都未确立。红杉自身的投资组合列表未就这一说法进行核对 —— 见 `备注`。

---

## 工程

### 技术栈与平台

公司未发布技术栈说明页。除另有标注外，以下条目均由可观察的公开资产确认（均观察于 2026-08-14）。

- **品牌站：** 部署在 Vercel 上的 SvelteKit —— `www.vizzylabs.ai` 返回 `server: Vercel` 与 `x-sveltekit-page: true`，资源路径为 `_app/immutable/`；DNS 经 `vercel-dns-016.com` 解析。`robots.txt` 允许全部抓取，未提供 sitemap。
- **应用：** `app.vizzylabs.ai` 同样是 Vercel 上的 SvelteKit，提供 `robots.txt` 与 `sitemap.xml`，根路径 302 跳转到 `/product`。
- **创作者站：** `www.vizzycircle.com` 同样由 Vercel 提供服务、同样是 `_app/immutable/` 资源；申请走 Google 表单、社区在 Discord，而非自建设施。
- **上一代站点：** 2025-06-18 的存档首页带有 `framer-*` 类名，说明在改写为 SvelteKit 之前，营销站是用 Framer 搭的（[Wayback](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/)）。
- **分析、错误追踪与营销标签（来自应用 JavaScript 打包文件）：** PostHog（`us.i.posthog.com`、`app.posthog.com`）、Umami（`cloud.umami.is/script.js`）、Sentry、Google Tag Manager、Facebook Connect，以及 Rewardful（`r.wdfl.co/rw.js`）。图标使用 Iconify（`api.iconify.design`、`api.simplesvg.com`、`api.unisvg.com`）。
- **登录方式：** Google Identity Services（`accounts.google.com/gsi/client`）以及邮箱登录；登录弹窗在社交登录之外提供 "Continue with Email"。
- **广告平台对接：** Meta 是唯一已上线的连接器（"Track Facebook & Instagram campaigns"），TikTok 与 YouTube 标注为 "Coming soon"；应用中还有 "Reconnect your Facebook account" 流程与 campaign "Naming Conventions" 工具。
- **没有公开代码：** `vizzylabs`、`vizzy-labs`、`VizzyLabs` 名下均无 GitHub 组织，npm 上检索 "vizzylabs" 无结果。存在一个名为 `VisPie` 的 GitHub 组织（创建于 2024-06-03），但公开仓库为 0、无成员、无任何资料，因此无法确认属于本公司（API 检查于 2026-08-14）。
- **旧域名：** `www.vispie.com` 可解析但 2026-08-14 时 TLS 握手失败（`tlsv1 alert internal error`），旧品牌站点目前无法通过 HTTPS 访问；而隐私联系邮箱 `support@vispie.com` 仍指向该域名。

### 系统

应用自身的 JavaScript 打包文件暴露了后端路由名，这是关于公司实际运行了什么的最具体的公开描述。

| 系统 | 证据 | 来源 |
|---|---|---|
| 视频格式检索与趋势排序 | `/api/v1/video-formats/v2/search`、`/api/v1/video-formats/v2/trending` | 应用 JavaScript 打包文件检查于 2026-08-14 |
| 视频语料库与创作者统计 | `/api/v1/video/videos`、`/api/v1/video/videos/batch`、`/api/v1/video/videos/creators`、`/api/v1/video/videos/stats`、`/api/v1/content/batch/media-urls` | 应用 JavaScript 打包文件检查于 2026-08-14 |
| Meta 广告数据接入与报表 | `/api/v1/meta-ads/batch`，以及位于 `/api/proxy/facebook/auth/init/`、`/ad-accounts/`、`/accounts/status/`、`/reports/`、`/tags/`、`/categories/`、`/available-actions/all/` 的代理层 | 应用 JavaScript 打包文件检查于 2026-08-14 |
| Instagram 内容发现 | `/api/discovery/instagram/posts/` 与 `/api/proxy/discovery/instagram/posts/` | 应用 JavaScript 打包文件检查于 2026-08-14 |
| 探索与行业浏览 | `/api/explore/search`、`/api/explore/industry` | 应用 JavaScript 打包文件检查于 2026-08-14 |
| 自动化条件生成（"autopilot"） | `/api/v1/autopilot/generate-criteria` | 应用 JavaScript 打包文件检查于 2026-08-14 |
| 看板与问卷 | `/api/v1/dashboards`、`/api/proxy/survey/surveys/` | 应用 JavaScript 打包文件检查于 2026-08-14 |
| 创作者招募与结算运营 | 只在站点上被描述、未暴露为接口：创作者筛选、一对一辅导、campaign brief 与脚本模板、按效果触发的奖金结算 | [官网](https://www.vizzylabs.ai/)、[vizzycircle.com](https://www.vizzycircle.com/) |

### 数据处理（依文档记载）

隐私政策是一份简短的通用文本：列出账号数据、使用数据、IP 地址、浏览器与操作系统，写明 "We do not sell your personal information"，未点名任何子处理者，未规定留存期限，没有 GDPR 或 CCPA 权利条款，儿童年龄门槛设为 13 岁（[隐私政策](https://www.vizzylabs.ai/privacy)；最后更新 2025-02-13）。

服务条款中有两条值得按原文引用。关于用户内容："While Vispie Inc holds the copyright, you are granted the right to use the content"，随后是一段宽泛授权，用户须授予 "a worldwide license to use, host, store, reproduce, modify, create derivative works … communicate, publish, publicly perform, publicly display and distribute such content"。关于数据采集："You agree not to conduct any systematic or automated data collection activities (including scraping, data mining, data extraction or data harvesting) on or in relation to the Service. Prohibited data collection includes, but is not limited to, using the Service as input into other services, websites, or databases."（[服务条款](https://www.vizzylabs.ai/terms)；最后更新 2025-02-13）。而产品在营销侧被描述为每天分析来自 TikTok、Instagram 与 YouTube 的 "5M+ new videos"（[官网](https://www.vizzylabs.ai/)、[Algorithm Engineer 岗位页](https://www.vizzylabs.ai/careers/algorithm-engineer)）；没有任何页面说明这些数据如何取得、依据何种授权。

### 招聘所需技术背景

以下全部来自 [vizzylabs.ai/careers](https://www.vizzylabs.ai/careers) 上的岗位页（访问于 2026-08-14）。其中只有一个是工程岗。

**Algorithm Engineer** —— SF / Hybrid / Remote，全职，未公布薪资区间。

- *职责：* "Develop and optimize video analysis models (scene detection, hook analysis, engagement prediction)"；"Build NLP pipelines for content tagging, sentiment analysis, and trend extraction"；"Design recommendation algorithms for content strategy suggestions"；"Work with large-scale social media datasets (TikTok, Instagram, YouTube)"；"Deploy models to production and monitor performance"。
- *必需：* "MS/PhD in Computer Science, Machine Learning, or related field (or equivalent experience)"；"Strong background in deep learning (PyTorch/TensorFlow)"；"Experience with computer vision or NLP in production"；"Proficiency in Python and familiarity with ML infrastructure (AWS SageMaker, Docker)"。
- *加分：* 发表过论文或有研究经历；"video understanding or multimodal models"；"Knowledge of LLMs and prompt engineering"；推荐系统；"social media data at scale"。
- *岗位提供：* "Access to large-scale social media datasets"；"Competitive compensation + equity"；"Publish research and attend conferences"。

**非工程岗位** —— Creative Strategist（"2–4+ years in creative strategy, creator marketing, performance social"，加分项包括 "English / Chinese bilingual" 与 "Familiarity with AI tools"）；AI Video Creators（"Deep experience with AI video generation tools"，点名 "Higgsfield, Creatify, Kling, Veo, or similar"）；Scriptwriters & Producers；以及四个市场方向（Meta 与 TikTok 投放、短视频内容、社交账号运营、增长与社区）。

### 行业领域

工作范围涵盖创作者营销运营 —— 创作者寻源与筛选、campaign brief、内容审核、按效果结算 —— 以及 Meta 上的付费社交效果衡量，TikTok 与 YouTube 则被表述为后续工作（[官网](https://www.vizzylabs.ai/)、[app.vizzylabs.ai](https://app.vizzylabs.ai/product)）。同时涉及对第三方社交视频的大规模采集与分析（[Algorithm Engineer 岗位页](https://www.vizzylabs.ai/careers/algorithm-engineer)）、付费创作者内容的披露规则、覆盖 "compensation, deliverables, payment terms, and content usage rights" 的书面创作者协议（[vizzycircle.com FAQ](https://www.vizzycircle.com/)），以及编剧与市场岗位中点名的竖屏短剧与游戏平台两个生态（ReelShort、DramaBox、Mango；Roblox、Epic）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | `vizzylabs.ai/careers`，五个岗位，通过页面内 "Apply for This Position" 表单投递 | [招聘页](https://www.vizzylabs.ai/careers)；访问于 2026-08-14 |
| 地点 | 四个岗位写 "SF / Hybrid / Remote"；AI Video Creators 写 "Remote" | [招聘页](https://www.vizzylabs.ai/careers) |
| 用工形式 | 全职、兼职、自由职业均有，视岗位而定 | [招聘页](https://www.vizzylabs.ai/careers) |
| 公布的薪资区间 | Creative Strategist 6 万–10 万美元 "+ Meaningful Equity"；Scriptwriters & Producers 6 万–12 万美元（全职）；AI Video Creators 6 万–15 万美元；市场岗 6 万–12 万美元；Algorithm Engineer 未公布区间，只写 "Competitive compensation + equity" | [招聘页](https://www.vizzylabs.ai/careers) |
| 投递截止日期 | "Application deadline: July 14, 2026"（Scriptwriters & Producers）与 "Application Deadline: July 7, 2026"（市场岗）；2026-08-14 读取页面时两个日期都已过，岗位仍在线 | [Scriptwriters & Producers 岗位页](https://www.vizzylabs.ai/careers/ai-agent-engineer)、[Marketing Roles 岗位页](https://www.vizzylabs.ai/careers/marketing-roles) |
| 汇报关系 | Creative Strategist 岗位 "reporting directly to founders" | [Creative Strategist 岗位页](https://www.vizzylabs.ai/careers/creative-strategist) |
| 工作语言 | 未作为政策公布；一个岗位把 "English / Chinese bilingual" 列为加分项 | [Creative Strategist 岗位页](https://www.vizzylabs.ai/careers/creative-strategist) |
| 福利、签证支持、面试流程、办公地址、流动率 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-08-14）：`www.vizzylabs.ai` 首页、`/careers` 及全部五个岗位页、`/privacy`、`/terms`、`robots.txt`，并探测了 `/about`、`/company`、`/team`、`/blog`、`/pricing`、`/contact`、`/press`、`/docs`、`/jobs` 与 `/sitemap.xml`；`app.vizzylabs.ai` 的 `/product`、`/pricing`、`/legal/terms-of-service`、`/legal/privacy-policy`、`robots.txt`、`sitemap.xml` 及其 JavaScript 打包文件；`www.vizzycircle.com` 及其 FAQ、Discord 邀请与 Google 申请表单；`api.vizzylabs.ai` 及若干其他子域名；`vispie.com` 的 HTTP 与 HTTPS 访问；三个域名的 WHOIS；`vizzylabs.ai` 与 `vispie.com` 的 Wayback Machine CDX 索引；Instagram、X、TikTok、Facebook 与 LinkedIn 账号；Discord invite API；GitHub 与 npm；CB Insights、Crunchbase、Tracxn 与 The Org；StartX 的 Luma 活动页与 StartX 社区目录；以及针对品牌名、主体名与创始人姓名的英文检索。

- **任何融资金额、日期、领投方或估值。** 公司自有渠道上不存在公告；找到的说法只有一个标识、一处招聘页提到红杉，以及一条列了另外三家投资方的数据库条目 —— 见 `不同来源之间的不一致`。
- **`Vispie Inc` 的公司登记记录。** 未取得任何文件，因此注册州、注册地址、高管与存续状态均未确立。公司页面上没有任何注册地址，唯一给出的地理信息是创作者站上的 "Stanford, CA"。
- **员工人数与具体成员。** 没有团队页；所查阅的来源中总共只有两个人被具名，且都出自第三方组织架构网站。
- **视频语料库如何采集、依据何种授权。** 公司宣传每天分析数百万条 TikTok、Instagram 与 YouTube 视频，早期版本还宣称拥有 "500,000,000+" 条广告素材库，而其自身条款禁止对服务进行自动化数据采集；没有任何页面说明该语料库的来源、授权或平台 API 依据。
- **模型、供应商与基础设施细节。** 站点与两份政策中都没有点名任何模型、推理供应商、云区域或数据处理地；AWS SageMaker 与 Docker 只作为招聘要求出现，这并不能确立生产环境使用。
- **品牌侧定价。** "Paid by Performance" 是面向品牌唯一给出的商业模式；没有价目表、起投门槛、CPM／CPV 口径或合同期限。
- **创作者协议。** 创作者 FAQ 称有书面协议约定报酬、交付物、付款条件与内容使用权，但协议本身未公开；也没有付款周期、争议处理流程、税表要求或适用地域。
- **任何客户方的确认。** 被点名的品牌（MrBeast Chocolate、Manus AI、Study X、Madnesz、Cluely）与 logo 条只出现在公司自己的页面上；未找到任何被点名品牌的案例、新闻稿或表态。
- **安全、合规与数据保护姿态。** 没有安全页面、认证、子处理者清单、DPA、状态页或漏洞披露联系方式；隐私政策未点名任何子处理者，也未规定留存期限。
- **技术博客、文档或开源。** 均未找到。`/docs` 与 `/blog` 跳转进应用且无内容；两个品牌名下都没有公开仓库或包。
- **2026-08-14 对自动访问设限的来源：** Crunchbase（HTTP 403）、创始人的 LinkedIn 个人页（HTTP 999）、TikTok 主页（对普通请求返回 HTTP 403）。凡上文引用到这些来源，措辞来自搜索结果摘要或替代来源并已相应标注。

### 不同来源之间的不一致

- **公司到底做什么业务。** 三个岗位页和两个公开站点描述的是 UGC 与品牌视频；另两个岗位页描述的是 "the future of interactive drama: short-form stories where viewers decide what happens next"，并把短剧 App 与游戏平台经验列为加分（[招聘页](https://www.vizzylabs.ai/careers)、[Scriptwriters & Producers 岗位页](https://www.vizzylabs.ai/careers/ai-agent-engineer)、[Marketing Roles 岗位页](https://www.vizzylabs.ai/careers/marketing-roles)）。服务条款描述的是第三种："an AI search and analysis service for advertising videos"（[服务条款](https://www.vizzylabs.ai/terms)）。
- **投资方。** 一个岗位页写 "backed by Sequoia Capital"（[Creative Strategist 岗位页](https://www.vizzylabs.ai/careers/creative-strategist)）；[CB Insights](https://www.cbinsights.com/company/vizzy-labs) 列的是 GV、Bain Capital Ventures 与 Forerunner Ventures；官网与创作者站只写 "venture backed"；而公司自己的活动介绍用 a16z、GV、Forerunner Ventures 来形容其客户的投资方（[Luma](https://luma.com/jfwqqbcv)）。这几种说法两两不一致。
- **所在地。** "Stanford, CA"（[vizzycircle.com](https://www.vizzycircle.com/)）对 "San Francisco, California"（[CB Insights](https://www.cbinsights.com/company/vizzy-labs)）对招聘页里的 "SF / Hybrid / Remote"。
- **语料库规模。** "500,000,000+ TikTok & Instagram ads and organic content"（2025-06 站点）、"50M viral videos"（应用套餐文案，2025-12 至今）、每日分析 "5M+ new videos"（当前官网）描述的是不同量级，且未说明彼此关系。
- **创作者社区规模。** 创作者站写 "10,000+ Creators"，而它指向的 Discord 服务器显示 17,679 名成员（[vizzycircle.com](https://www.vizzycircle.com/)、[Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true)；均为 2026-08-14）。
- **一个与内容对不上的岗位 URL。** `vizzylabs.ai/careers/ai-agent-engineer` 渲染出的是 "Vizzy Labs | Scriptwriters & Producers" 岗位，招聘列表里也不存在 AI agent engineer 岗位（检查于 2026-08-14）。
- **各站点的版权年份。** 品牌站写 "© 2025 Vizzy"，创作者站写 "© 2026 Vizzy Circle"（均访问于 2026-08-14）。
- **数据库中的同名冲突。** 融资数据库与搜索引擎会返回伦敦的招聘创业公司 Vizzy（2025 年 4 月由 Adjuvo 领投的 365 万英镑种子轮），以及一个硬苏打饮料品牌；都不是本公司（[UNLEASH](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/)、[Crunchbase 融资轮次页](https://www.crunchbase.com/funding_round/vizzy-6454-seed--2028b984)）。

### 其他

- **三个品牌、三个域名、三类受众，同一个主体。** `vizzylabs.ai` 面向品牌，`app.vizzylabs.ai` 面向营销人员与创作者卖订阅，`vizzycircle.com` 招募创作者；三者都由 `Vispie Inc` 署名或受其约束，而只有中间那个公布了价目表。
- **法律文件早于当前产品。** 两份文件都标注 2025-02-13 —— 早于应用的订阅档位、早于 UGC 平台定位，比创作者网络的域名注册早约十一个月 —— 并把业务描述为广告视频检索服务。
- **隐私联系邮箱指向一个已不再提供站点的域名。** 声明的联系方式是 `support@vispie.com`，而 `www.vispie.com` 在 2026-08-14 时 TLS 握手失败。
- **面向创作者的 FAQ 以"是否正规"开篇。** 第一条问题是 "Is Vizzy Circle a legitimate company? How can I verify?"，答案给出主体名称、官网、社交账号与 Discord 规模（[vizzycircle.com](https://www.vizzycircle.com/)）；创作者一侧的疑虑也表现为 TikTok 上反复出现的检索话题。
- **受众分布极不均衡。** Discord 社区显示 17,679 名成员，而 X 账号只有 5 个粉丝、Instagram 168 个粉丝和 8 条帖子（均为 2026-08-14）—— 公司的触达集中在一个封闭社区里，而不是公开账号上。
- **创作者证言无法回溯到具体的人。** 三条证言都只有名字加姓氏首字母（"Jess R."、"Marcus K."、"Aisha T."），署的是品类而非账号（[vizzycircle.com](https://www.vizzycircle.com/)）。
- **首页的计数器渲染为 "0+"。** 三张头部数据卡（"Top creators"、"Videos analyzed"、"Converted Views"）是客户端动画计数器，在服务端返回的 HTML 中显示为 "0+"；具体数字出现在页面更靠下的位置（观察于 2026-08-14）。
- **相对于公开足迹的体量，营销技术栈偏重：** 应用打包文件中同时装载了 PostHog、Umami、Sentry、Google Tag Manager、Facebook Connect 与 Rewardful 联盟追踪（检查于 2026-08-14）。

---

## 资料来源

**官方**

- [官网](https://www.vizzylabs.ai/) · [招聘页](https://www.vizzylabs.ai/careers) · [robots.txt](https://www.vizzylabs.ai/robots.txt)
- 岗位页 —— [Creative Strategist](https://www.vizzylabs.ai/careers/creative-strategist) · [Scriptwriters & Producers](https://www.vizzylabs.ai/careers/ai-agent-engineer) · [AI Video Creators](https://www.vizzylabs.ai/careers/ai-video-creators) · [Marketing Roles](https://www.vizzylabs.ai/careers/marketing-roles) · [Algorithm Engineer](https://www.vizzylabs.ai/careers/algorithm-engineer)
- [服务条款](https://www.vizzylabs.ai/terms) · [隐私政策](https://www.vizzylabs.ai/privacy) —— 均为最后更新 2025-02-13
- [Vizzy AI 应用](https://app.vizzylabs.ai/product) · [应用服务条款](https://app.vizzylabs.ai/legal/terms-of-service) · [应用隐私政策](https://app.vizzylabs.ai/legal/privacy-policy)
- [Vizzy Circle](https://www.vizzycircle.com/) · [Vizzy Circle Discord 邀请](https://discord.gg/MZhbHg7Q5Z) · [Vizzy Circle 创作者网络申请表](https://docs.google.com/forms/d/e/1FAIpQLSd_ooDJ4m5hFQecHzZ2BEyo3DO0GbQ3_6-q0VvmDdoy9PI8Lw/viewform)
- 社交 —— [Instagram @vizzy_labs](https://www.instagram.com/vizzy_labs/) · [TikTok @vizzy_labs](https://www.tiktok.com/@vizzy_labs) · [X @vizzylabs_ai](https://x.com/vizzylabs_ai) · [LinkedIn](https://www.linkedin.com/company/vizzylabs)
- 存档 —— [vizzylabs.ai，2025-06-18](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/) · [vizzylabs.ai，2025-12-08](https://web.archive.org/web/20251208202228/https://www.vizzylabs.ai/) · [vizzylabs.ai，2026-05-17](https://web.archive.org/web/20260517154252/https://www.vizzylabs.ai/) · [vispie.com，2025-01-30](https://web.archive.org/web/20250130073405/http://www.vispie.com/)
- [Vizzy Circle 服务器的 Discord invite API 记录](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true)

**第三方报道与档案**

- [Luma —— StartX Founder Spotlight 中的 Vizzy Labs 专场](https://luma.com/jfwqqbcv)
- [The Org —— Vizzy Labs](https://theorg.com/org/vizzy-labs) · [The Org —— Yohan Lee](https://theorg.com/org/vizzy-labs/org-chart/yohan-lee) · [LinkedIn —— Yohan Lee（2026-08-14 对自动访问返回 HTTP 999）](https://www.linkedin.com/in/yohanlee12/)
- [CB Insights —— Vizzy Labs](https://www.cbinsights.com/company/vizzy-labs) · [Crunchbase —— Vizzy Labs（2026-08-14 对自动访问返回 HTTP 403）](https://www.crunchbase.com/organization/vizzylabs-ai)
- [StartX 社区目录](https://web.startx.com/community?6a151520_page=3) —— 在所查阅的页面中未找到 Vizzy Labs
- 同名冲突参考，非本公司 —— [UNLEASH —— 英国招聘创业公司 Vizzy 融资 365 万英镑，2025](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/) · [Crunchbase —— Vizzy 种子轮，2025-04-17（2026-08-14 对自动访问返回 HTTP 403）](https://www.crunchbase.com/funding_round/vizzy-6454-seed--2028b984)
