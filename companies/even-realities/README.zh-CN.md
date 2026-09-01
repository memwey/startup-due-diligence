# Even Realities

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-09-01。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-09-01。英文版为原始版本。

## 摘要

Even Realities 卖的是以显示为核心、不带摄像头也不带扬声器的智能眼镜：**Even G1**（2024）、**Even G2**（2025），以及用来操控它们的智能戒指 **Even R1**。绿色 Micro LED 投影机把画面送进光波导，算力放在配对的手机上。网站"owned and operated by **Hong Kong Even Realities Limited**"，欧洲经济区与美国另有签约主体（**Even Realities GmbH**，柏林；**Even Realities US Inc**，特拉华）（[Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service)；最后更新 2026-07-28）。公司自己的招聘页写"总部位于中国深圳与德国柏林"（[猎聘企业页](https://m.liepin.com/company/13683985/)；读取于 2026-09-01）。

- 最近一轮：**1.5 亿美元 pre-B 轮，估值 10 亿美元**，2026-07-06 公布，由**美团**领投、**腾讯**参投；报道中提到的早期投资方包括 HSG（原红杉中国）与高瓴（[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)）—— 见 `融资`。
- **英国 PSTI 合规声明**给出了精确的发布日期与安全支持下限：G1 发布于 2024-06-25（安全更新不早于 2029-06-25），G2 与 R1 发布于 2025-11-12（不早于 2030-11-12）（[UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance)）。
- **开发者平台有可观测的真实使用量**：MIT 协议的 `@evenrealities/even_hub_sdk` 在截至 2026-08-29 的一个月内被下载 **238,666 次**，Even Realities 的 Discord 有 **16,182 名成员**（[npm 下载量](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk)、[Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true)；读取于 2026-09-01）。
- **Terminal Mode** 以 npm CLI 的形式发布：在开发者的电脑上拉起 **Claude Code 或 Codex**，把会话渲染到 "the G2's 576×288 canvas"，再用 R1 戒指手势回控（[`@evenrealities/even-terminal`](https://www.npmjs.com/package/@evenrealities/even-terminal)；readme 读取于 2026-09-01）—— 见 `系统`。
- 招聘结构是**硬件公司的形状**：2026-09-01 在猎聘企业页上可见的 20 个岗位全部是结构、模具、声学、显示驱动、质量、包装、供应链或设计岗，base 深圳南山；页面同时写着共 64 个在招职位（[猎聘企业页](https://m.liepin.com/company/13683985/)）。
- TechCrunch 报道其产品**尚未在中国销售**，美国是增长最快的市场（[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)；2026-07-06）。

---

## 基本情况

| 项目 | 内容 | 出处 |
|---|---|---|
| 当前公开品牌 | Even Realities | [evenrealities.com](https://www.evenrealities.com/)；访问于 2026-09-01 |
| 网站运营方 | "This Website is owned and operated by Hong Kong Even Realities Limited, together with its affiliates and subsidiaries (including, for example, Even Realities GmbH)" | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service)；最后更新 2026-07-28 |
| 香港主体地址 | "Room 29D, 8/F, On Cheong Factory Building, No. 19 Tai Yip Street, Kwun Tong, Hong Kong" | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| 欧洲经济区主体 | "Even Realities GmbH, a company registered in Berlin, with its registered address located at Friedrichstraße 79, 10117 Berlin, Germany" —— 也是设备与 App 隐私政策中具名的数据控制者 | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service)、[Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP) |
| 美国主体 | "Even Realities US Inc, a company registered in State of Delaware, with its registered address located at 8 The Green Ste A, Dover, Kent, DE 19901" | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| 深圳主体 | "Even Realities Ltd, Building West 2603, LEPU TOWER, Nanshan District, Shenzhen, China" | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers)；更新于 2026-08-18 |
| 日本主体 | "Even Realities Co., Ltd., 2F, Ginza Otake Residence, 1-22-11 Ginza, Chuo-ku, Tokyo, Japan" | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) |
| 中国法律主体 | 深圳市逸文科技有限公司，成立于 2023-06-02，深圳市南山区，法定代表人 王骁逸 | [百度百科（语言：zh）](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335)、[搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866) |
| App 发布者 | "Even Realities Ltd." —— `Even Realities`（`com.even.sg`，首发 2025-11-21）与 `Even G1`（`com.even.g1`，首发 2024-07-31） | [iTunes search API](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10)；读取于 2026-09-01 |
| 成立时间 | 2023 年；中国主体成立于 2023-06-02 | [猎聘企业页](https://m.liepin.com/company/13683985/)、[搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866) |
| 自述总部 | "总部位于中国深圳与德国柏林"；深圳地址 深圳市南山区乐普大厦，柏林地址 Friedrichstraße 79 | [猎聘企业页](https://m.liepin.com/company/13683985/) |
| 人数 | 猎聘页写 "100-499人"；TechCrunch 报道 300–400 人（2024 年为 30–40 人）；深圳市发改委的一篇报道称约 100 人（2025 年 7 月） | [猎聘企业页](https://m.liepin.com/company/13683985/)、[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)、[深圳市发改委（语言：zh）](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html) |
| 在招岗位 | 页面写 "职位 · 64"；可见 20 条，全部在 深圳-南山区 | [猎聘企业页](https://m.liepin.com/company/13683985/)；读取于 2026-09-01 |
| 公司自己列出的投资方 | "鼎晖投资、青山资本、红杉资本、砺思资本、爱尔眼科" | [猎聘企业页](https://m.liepin.com/company/13683985/) |
| 估值 | 投后 10 亿美元，2026-07-06 口径 | [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) |
| 零售覆盖 | "产品已入驻全球300+高端眼镜店"；G1 页面写 "over 300 opticians who can fine-tune your Even G1" | [猎聘企业页](https://m.liepin.com/company/13683985/)、[Even G1](https://www.evenrealities.com/g1) |
| 具名零售渠道 | 日本：Yodobashi、BIC CAMERA。台湾：Taiwan Mobile、E-life Mall、Fayaque、eslite spectrum。韩国：Naver Store（由 Mune 运营）。美国体验店：Alexander Daas Opticians，旧金山 | [Retail](https://www.evenrealities.com/retail)；访问于 2026-09-01 |
| 商城 | Shopify（店铺 id 60045131891），站点走 Shopify CDN | [robots.txt](https://www.evenrealities.com/robots.txt) 与商品页；读取于 2026-09-01 |
| 支持平台 | Zendesk 帮助中心 `support.evenrealities.com` —— 207 篇文章 | [Zendesk 帮助中心 API](https://support.evenrealities.com/api/v2/help_center/en-us/articles.json)；读取于 2026-09-01 |
| 站点语言/地区 | 默认英文站之外还有 `de-DE`、`es-ES`、`fr-FR`、`it-IT`、`ja-JP`、`ko-KR`、`zh-Hans-HK`、`zh-Hant-HK` | [evenrealities.com](https://www.evenrealities.com/) 页脚；读取于 2026-09-01 |
| 社区 | Discord "Even Realities" —— 16,182 名成员、2,444 在线；服务器创建于 2024-10-30 | [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true)；读取于 2026-09-01 |
| 公开社交账号 | X `@EvenRealities`、LinkedIn `even-realities`、Instagram、TikTok、YouTube、Facebook —— 均列在站点的 `Organization` 结构化数据中 | 商品页 JSON-LD；读取于 2026-09-01 |
| GitHub 组织 | `even-realities` —— 创建于 2024-10-22，5 个公开仓库，833 followers，website 字段为 `evenrealities.com` | [GitHub API](https://api.github.com/orgs/even-realities)；读取于 2026-09-01 |
| 安全联系方式 | 漏洞报告 `software@evenrealities.com`；英国 PSTI 安全问题 `support@evenrealities.com`，24 小时内确认收到、每 7 天同步一次进展 | [Vulnerability Disclosure Policy](https://support.evenrealities.com/hc/en-us/articles/15840567983887-Vulnerability-Disclosure-Policy)（生效 2026-04-17）、[UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) |

### 品牌与法律实体

| 名称 | 类型 | 司法辖区 | 来源中写明的关系 | 出处 |
|---|---|---|---|---|
| Even Realities | 公开品牌 | 全球 | 所有产品界面与包装使用的品牌 | [evenrealities.com](https://www.evenrealities.com/) |
| Hong Kong Even Realities Limited | 法律主体 | 香港 | "owned and operated by"；欧洲经济区与美国之外的默认签约方 | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| Even Realities GmbH | 法律主体 | 德国柏林 | 欧洲经济区用户的签约方；设备与 App 隐私政策中的数据控制者 | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service)、[Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP) |
| Even Realities US Inc | 法律主体 | 美国特拉华州 | 美国用户的签约方 | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| Even Realities Ltd | 关联主体 | 中国深圳 | 被列为可能接收个人数据的 "affiliated companies" 之一 | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) |
| Even Realities Co., Ltd. | 关联主体 | 日本东京 | 同上，列在同一份关联公司清单中 | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) |
| 深圳市逸文科技有限公司 | 法律主体 | 中国深圳 | 品牌背后的中国注册公司，法定代表人 王骁逸 | [百度百科（语言：zh）](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335) |
| `evenrealities.cn` | 平行域名 | —— | 提供与 `evenrealities.com` 相同的英文商城；公司猎聘页把它写作"公司官网"；页面上未发现 ICP 备案号 | [evenrealities.cn](https://www.evenrealities.cn/)、[猎聘企业页](https://m.liepin.com/company/13683985/)；读取于 2026-09-01 |

所查资料中没有任何来源说明香港、德国、美国、日本、深圳以及中国注册主体之间的持股关系。"Even Realities Ltd" 这个英文名既出现在 Apple App Store 的发布者记录中，也以深圳地址出现在集团的跨境数据传输说明里。

---

## 产品

### 产品构成与功能板块

三款在售产品，设计上都不带摄像头、不带扬声器（[Even G2 FAQ](https://www.evenrealities.com/smart-glasses)："To prioritize your privacy and deliver a seamless display experience, Even G2 relies on its integrated microphone for information input rather than a camera"）。

| 产品 | 发布 | 公开的规格 |
|---|---|---|
| Even G1 | 2024-06-25 | 光波导，双目，绿色 Micro LED，分辨率 640×200，FoV 25°，刷新率 20 Hz，亮度 1000 nits，透光率 98%，两个麦克风，BLE 5.2，无线充电，"up to 1.5 days" 续航，防溅与小雨，屈光镜片采用三井化学 MR™ 材料 |
| Even G2 | 2025-11-12 | 光波导，双目，绿色 Micro LED，分辨率 640×350，FoV 27.5°，刷新率 60 Hz，亮度 1200 nits，透光率 98%，四个麦克风，BLE 5.4，"up to 2 days" 续航，充电盒 "up to 7 full charges"，IP65，镁与钛框架，无螺丝铰链 |
| Even R1 | 2025-11-12 | "Zirconia ceramic with medical-grade stainless steel lining"，IP68，"Up to 7 days" 续航，90 分钟充满，Bluetooth BLE，LED 光束测心率，加速度计记录步数/卡路里/距离，用于操控 G2 |

出处：发布日期见 [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance)；规格见 [Even G1](https://www.evenrealities.com/g1)、[Even G2](https://www.evenrealities.com/smart-glasses) 的规格表与 [Even R1 商品页 JSON-LD](https://www.evenrealities.com/products/r1)；均访问于 2026-09-01。

站点上公布的功能名称：**Conversate**、**Teleprompt**、**Translate**、**Even AI**、**HUD / Dashboard**、**Transcribe**、**Navigate**（"Works wherever Google Maps does"）、**QuickNote** / **QuickList**、**Health**、**Terminal**（[evenrealities.com](https://www.evenrealities.com/) 页脚；访问于 2026-09-01）。G2 的 FAQ 声称助手跑在自研模型上："Even G2 runs on Even AI, powered by our proprietary EvenLLM"（[Even G2](https://www.evenrealities.com/smart-glasses)）。

技术页上的光学口径：**Even HAO™**（"Holistic Adaptive Optics"），描述为 "our proprietary technology turning the glasses projectors, waveguides and lenses into a perfect orchestra"；投影机 "40% smaller. But brighter and sharper imagery"；镜片中心 "30% slimmer"；"over 100 layer coatings"；渐变光栅 "spreads the light more evenly"；**TriSync** 在镜腿、手机与戒指之间三方互联；可靠性测试 —— "Screwless hinges opened and closed 40,000 times"、"Drop-tested from 2 metres"、"Certified IP65"。适配性来自公司行为实验室分析的 "100,000 3-D head shapes"（[Technology](https://www.evenrealities.com/tech)；访问于 2026-09-01）。

公司页把眼科工作归到一位具名外部合作者："Dr. Qu Jia, Honorary Doctor at New England College of Optometry and former President of Wenzhou Medical University, is leading an ophthalmology team specializing in visual brain processing, myopia control, and contact lenses"（[Company](https://www.evenrealities.com/company)；访问于 2026-09-01）。

### 商业化

通过 Shopify 商城直销硬件，加上眼镜店与电子零售渠道，以及一个企业采购入口。2026-09-01 从商品页结构化数据读到的美国价格：

| 产品 | 公开价位（美元） |
|---|---|
| Even G2 A / Even G2 B | 599、758、828、948 |
| Even G1 A | 499、658 |
| Even R1 | 249 |

出处：[Even G2 A](https://www.evenrealities.com/products/g2-a)、[Even G2 B](https://www.evenrealities.com/products/g2-b)、[Even G1 A](https://www.evenrealities.com/products/g1-a)、[Even R1](https://www.evenrealities.com/products/r1)。较高价位对应屈光与镜片折射率选项，而非不同型号。TechCrunch 把经济模型描述为 "$599" 镜架加上 "prescription lenses or ring add $200-$300, averaging ~$1,000 per order"（[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)）。

其他商业界面：**企业采购**页、按 "Optical Store / Distributor / Other Retailer" 分类的**合作申请**表单、**创作者**合作表单，以及全站推广的 **10% 教育折扣**（[evenrealities.com](https://www.evenrealities.com/)；访问于 2026-09-01）。保修为 "2-year warranty for Europe and a 1-year warranty for all other regions"；非屈光镜片 14 天可退，屈光订单 "only possible within 24 hours of purchase"（[Even G2 FAQ](https://www.evenrealities.com/smart-glasses)）。

开发者平台没有公开的分成规则。Even Hub 开发者平台条款描述了插件提交、"Publication Review"（"development information verification, security testing, UI testing, and dynamic testing"）与下架机制，并授予 Even Realities 对 Developer Content 的 "non-exclusive, transferable, sublicensable, royalty-free, worldwide license"；协议中没有任何费用、佣金或结算条款（[Even Hub Developer Platform Terms of Service](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service)；最后更新 2026-03-24）。

### 公开规模变化

| 日期 | 原文口径 | 出处 |
|---|---|---|
| 2023-06-02 | 深圳市逸文科技有限公司成立 | [百度百科（语言：zh）](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335) |
| 2024-06-25 | Even G1 发布 | [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) |
| 2024-07-31 | `Even G1` iOS App 首发 | [iTunes search API](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10) |
| 2024-10-22 / 2024-10-28 | GitHub 组织创建；`EvenDemoApp`（BLE 协议参考实现）首次发布 | [GitHub API](https://api.github.com/orgs/even-realities) |
| 2024-10-30 | Discord 服务器创建 | [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true) |
| 2025（报道） | "小半年的时间卖出一万多副"；"40多个国家和地区"、"300多家欧洲眼镜店" | [雷峰网（语言：zh）](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html) |
| 2025-07-13 | 深圳市发改委报道：约 100 人；G1 售价 599 美元 | [深圳市发改委（语言：zh）](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html) |
| 2025-11-12 | Even G2 与 Even R1 发布 | [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) |
| 2025-11-21 | `Even Realities` iOS App（`com.even.sg`）首发 | [iTunes search API](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10) |
| 2026-01-27 | `@evenrealities/even_hub_sdk` 首次发布到 npm | [npm registry](https://registry.npmjs.org/@evenrealities/even_hub_sdk) |
| 2026-04-25 | `@evenrealities/even-terminal` 首次发布到 npm | [npm registry](https://registry.npmjs.org/@evenrealities%2Feven-terminal) |
| 2026-07-06 | 1.5 亿美元融资，估值 10 亿美元；300–400 人（2024 年为 30–40 人）；G1 "surpassed its 10,000-unit sales target" | [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) |
| 2026-08-29 | 近一个月 npm 下载量：Even Hub SDK 238,666、CLI 207,762、`even-terminal` 2,886 | [npm API](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk) |
| 2026-09-01 | Discord 16,182 名成员；GitHub 组织 833 followers；公开在招 64 个职位 | [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true)、[GitHub API](https://api.github.com/orgs/even-realities)、[猎聘企业页](https://m.liepin.com/company/13683985/) |

### 已公布的客户、合作方与具名用户

| 名称 | 公开口径 | 出处 |
|---|---|---|
| Palmer Luckey | Oculus 与 Anduril 创始人；"At TED 2025, he delivered a flawless talk with no notes or teleprompter, later admitting he'd read it all off his G1" | [evenrealities.com](https://www.evenrealities.com/)；访问于 2026-09-01 |
| Amy Tan | 作家；用 Conversate 做台上访谈，用 Translate 看外语剧集 | [evenrealities.com](https://www.evenrealities.com/) |
| Jason Rajasinghe、Andres Vidoza、Duncan Clark | 首页轮播中具名的创作者/用户 | [evenrealities.com](https://www.evenrealities.com/) |
| InnoHome（台湾） | "Even Realities Taiwan strategic partnership with InnoHome brings Even G2 to Taiwan" | [News 博客](https://www.evenrealities.com/blogs/news/even-realities-taiwan-strategic-partnership-with-innohome-brings-even-g2-to-taiwan) |
| Jun Ginza（日本） | "Even Day Japan 2026 supported by Jun Ginza"；另有一篇关于零售合作的文章 | [News 博客](https://www.evenrealities.com/blogs/news/event-recap-even-day-japan-2026-supported-by-jun-ginza) |
| 东京 2025 听障奥运会 | "Beyond the Water: Empowering Lives at the Tokyo 2025 Deaflympics" | [Stories 博客](https://www.evenrealities.com/blogs/stories/beyond-the-water-empowering-lives-at-the-tokyo-2025-deaflympics) |
| Ottica La Fege、Line of Sight、Hungry Eyes | 公司新闻中具名的眼镜零售商 | [News 博客](https://www.evenrealities.com/blogs/news/heritage-meets-future-ottica-la-fege-on-even-g2) |

公司转载的媒体认可，发布日期均为 2026-04-17：USA Today 把 G2 评为 "one of best innovations at CES 2026"，The Guardian 把它列入 "the best gadgets at CES 2026"，另有 WIRED、CNET、ZDNET、TechRadar、Mashable、Tom's Guide、BBC 与 Business Insider Japan 的评测（[Press 博客](https://www.evenrealities.com/blogs/press/usa-today-names-even-g2-one-of-best-innovations-at-ces-2026)）。转载的 USA Today 文章给出 G2 重量为 36 克。

### 公司自述的计划

- Even Hub 被描述为仍在建设中的平台，邀请开发者 "create spatial experiences and collaborate with early developers shaping the platform"（[hub.evenrealities.com](https://hub.evenrealities.com)；访问于 2026-09-01）。
- 站点的页面 sitemap 中存在一个名为 `even-g2-x-007-first-light` 的页面（[页面 sitemap](https://www.evenrealities.com/sitemap/pages/1.xml)；读取于 2026-09-01）。
- G1 的 FAQ 写明 R1 兼容性尚未交付："Even R1 currently supports interaction only with Even G2 and is not yet compatible with Even G1. Our product team is actively expanding device compatibility"（[Even G1](https://www.evenrealities.com/g1)）。

---

## 创始人

公司自己的猎聘企业页公布了四位联合创始人及其履历（中文原文；读取于 2026-09-01，[猎聘企业页](https://m.liepin.com/company/13683985/)）：

| 姓名 | 职务 | 页面上公布的履历 |
|---|---|---|
| 王骁逸 (Will Wang) | 创始人 / CEO | 上海交通大学 机械工程学士；加州大学伯克利分校 运筹学硕士。"P&G、Western Digital、Apple、OPPO、坚果投影等公司产品负责人"；"负责Apple制造设计，深度参与iPhone、Apple Watch等数款产品的研发与量产"；作为坚果投影 CPO，推出 O 系列超短焦投影、N 系列云台投影、"目氪三色激光"。 |
| 胡丹 (Dan Hu) | 联合创始人 / CDO | 国立华侨大学 工业设计学士；香港理工大学 设计策略硕士。"Philips、Samsung、韶音、清华设计管理研究所、坚果投影等公司设计负责人"；"Philips Design Committee唯一大陆背景成员"；主导 Samsung 家电产品线设计与韶音骨传导耳机产品线；"30余次获得国际大奖，包括IDEA金银铜奖、iF、红点、G-mark和Edison金奖"。 |
| 欧阳剑 (Tom Ouyang) | 联合创始人 / CTO | 普渡大学 机械工程学士；加州大学洛杉矶分校 机械工程硕士。"Western Digital、Apple、坚果投影等公司研发负责人"；"负责Western Digital机械硬盘MEMS微机电传动模组研发"；"Apple iPhone后置主摄模组设计负责人，前后完成8款主摄模组量产项目落地"；在坚果投影任光学与结构负责人。 |
| 王力 (Christy Wang) | 联合创始人 / COO | 上海交通大学 金融英语学士。"百度战略办专家、执一资本、弈秋资本、势乘资本等机构董事及管理合伙人"；"累计融资额近40亿"，项目覆盖天使至 Pre-IPO。 |

TechCrunch 描述这位 CEO "spent two years at Apple before leaving in 2018, contributing to both the Apple Watch and iPhone"，并称创始团队 "drew from enterprise technology and the luxury eyewear world"（[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)；2026-07-06）。

两位眼镜行业的招募是中文媒体报道的、而非公司具名公布的：**Nicolai Schnur**，被描述为前 LINDBERG CMO；**Philipp Haffmans**，被描述为 MYKITA 与 ic! berlin 的联合创始人（[雷峰网（语言：zh）](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)）。公司自己的招聘文案写团队来自 "MYKITA、Ic!berlin、LINDBERG等高端眼镜行业资深专家" 与 "Apple、华为、OPPO、vivo等消费电子巨头背景"；公司页则列出 "Apple, Samsung, Philips, Mykita and Lindberg"（[猎聘企业页](https://m.liepin.com/company/13683985/)、[Company](https://www.evenrealities.com/company)）。

猎聘页还按角色列出了发帖的招聘官，包括 "Co-founder & CTO —— 4个职位"、"AI Leader —— 2个职位"、"COO —— 1个职位"、"设计负责人 —— 1个职位"，说明这些职能存在且直接参与招聘（[猎聘企业页](https://m.liepin.com/company/13683985/)）。

---

## 融资

| 日期 | 轮次 | 金额 | 投资方 | 出处 |
|---|---|---|---|---|
| 2024-01 | 天使轮 | 未披露 | 未具名 | [搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866) |
| 2024-08 | Pre-A | 未披露 | 博原资本、华创资本、投中资产 | [搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866) |
| 2024-09 | 由注册资本变更推断的又一轮 | 未披露；注册资本变更为 863.5617 万元人民币 | 新增股东 中山市联汇股权投资合伙企业；自然人股东李莉莉退出 | [搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866)、[腾讯新闻（语言：zh）](https://news.qq.com/rain/a/20240812A06XK100) |
| 2024-12-10 | A 轮 | 未披露 | Monolith 砺思资本、鼎晖投资 | [百度百科（语言：zh）](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335) |
| 2026-07-06 | Pre-Series B | 1.5 亿美元，投后估值 10 亿美元 | 美团（领投）、腾讯；报道中提到的早期投资方包括 HSG（原红杉中国）与高瓴 | [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) |

表格之外的事实：

- 公司自己在招聘页上列出的投资方是 "鼎晖投资、青山资本、红杉资本、砺思资本、爱尔眼科"（[猎聘企业页](https://m.liepin.com/company/13683985/)）。**爱尔眼科是来自眼科行业的战略投资方**，与其屈光镜片定位一致。
- 2024 年底的中文报道称该公司有望在 G1 上市后一年内完成三轮融资（[搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866)；2024-09）。
- 所查资料中，2026 年这轮之前没有任何一轮公布过金额。2026 年之前的估值只在二手中文报道里以区间出现（"数亿美金"、"估值超10亿" 人民币）（[雷峰网（语言：zh）](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)）。
- 公司自己没有发布过任何融资公告；`/press` 页面对自动化客户端返回验证中间页，新闻博客中也没有融资文章（2026-09-01 核查）。

---

## 工程

### 技术栈与平台

**由公开资产确认**（包、仓库、文档、响应头；读取于 2026-09-01）：

- **Even Hub SDK** —— `@evenrealities/even_hub_sdk`，MIT，"TypeScript SDK for Even Hub developers to communicate with Even App"，自 2026-01-27 起 12 个版本，0.0.14 发布于 2026-08-20（[npm](https://registry.npmjs.org/@evenrealities/even_hub_sdk)）。
- **工具链** —— `@evenrealities/evenhub-cli`（0.1.14）、`@evenrealities/evenhub-simulator` 及其 `darwin-arm64`、`darwin-x64`、`linux-x64`、`linux-arm64`、`win32-x64`、`win32-arm64` 各平台二进制（0.9.4，2026-08-31），以及 `@evenrealities/pretext`（"Pixel-accurate font measurement library for Even Realities G2 glasses"）（[npm 搜索](https://registry.npmjs.org/-/v1/search?text=evenhub&size=20)）。
- **应用模型** —— 插件就是 Web 应用："HTML, CSS, and JavaScript or TypeScript"、"Bring any stack - Vite, React, plain JS"，用 `evenhub pack` 打包成 `.ehpk` 后上传到开发者门户，或用二维码旁加载。需要 Node.js 18+（[Even Hub 文档](https://hub.evenrealities.com/docs)、[evenhub-templates README](https://github.com/even-realities/evenhub-templates)）。
- **运行时切分** —— "Code executes on the phone; the glasses render and capture input"（[Even Hub 文档](https://hub.evenrealities.com/docs)）。
- **面向开发者的显示与输入约定** —— "576 x 288 px per eye"，单色绿、"16 levels"；镜腿触控板（以及可选的 R1）手势为 "Press, double press, swipe up, swipe down, tap then long press and release"；音频为 "4-mic array, single stream, 16 kHz PCM"；"No camera, no speaker"（[Even Hub 文档](https://hub.evenrealities.com/docs)）。
- **传输格式** —— protobuf；模板仓库的 README 写明了一个具体的坑："`OsEventTypeList.CLICK_EVENT` is `0`, and protobuf omits zero-value fields on the wire. A single tap therefore arrives as an envelope with **no `eventType` field at all**"（[evenhub-templates README](https://github.com/even-realities/evenhub-templates)）。
- **设备 BLE 协议** —— 参考实现 `EvenDemoApp`（C，BSD-2-Clause，473 stars）记录了左右镜腿的双 BLE 连接、右侧麦克风的 LC3 音频流（上限 30 秒）、1-bit 576×136 BMP 图像按 194 字节分包传输并以 CRC 命令校验，以及按 488 像素行宽分页的文本发送（[EvenDemoApp README](https://github.com/even-realities/EvenDemoApp)）。
- **嵌入式 UI** —— 组织公开了 `lvgl-sys-v9`，即 LVGL v9 的 Rust 绑定（[GitHub API](https://api.github.com/orgs/even-realities/repos)）。
- **Web 与电商** —— Shopify 商城；Sanity CMS（商品页资源域名 `cdn.sanity.io`）；Zendesk 帮助中心；结算支持 Klarna、Shop Pay、Apple Pay、Google Pay、PayPal 与 UnionPay（[evenrealities.com](https://www.evenrealities.com/)）。
- **数据托管** —— "Data generated in connection with your use of Even Realities Products is stored on servers located in the Netherlands"（[Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers)）。

**只在公司自己的招聘文案中出现**、没有对应公开资产："从光学设计到AI算法：掌握从底层光学技术到上层AI应用的全栈核心技术"（[猎聘企业页](https://m.liepin.com/company/13683985/)）。

### 系统

- **光学栈** —— 投影机、带渐变光栅的光波导与屈光镜片被当成一个系统来做，对外称 Even HAO™；镜片 "digitally surfaced with a diamond-tipped lathe"，由 "Free-form technology and ray-tracing software" 成形，带 "over 100 layer coatings"（[Technology](https://www.evenrealities.com/tech)）。
- **TriSync 连接** —— "Even G2, your phone and Even R1 work together as one intuitive system. Temple tips sync wirelessly with your phone and Ring"（[Technology](https://www.evenrealities.com/tech)）。在协议层，眼镜暴露两个独立的 BLE 端点，左右镜腿各一（[EvenDemoApp README](https://github.com/even-realities/EvenDemoApp)）。
- **Even Hub 插件平台** —— 开发者注册、插件上传、含安全/UI/动态测试的 "Publication Review"、驳回与下架机制、用户投诉通道、协议终止后仍存续两年的审计权，以及针对开发者访问用户数据的数据处理协议（[Even Hub Developer Platform Terms of Service](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service)、[Data Processing Agreement](https://support.evenrealities.com/hc/en-us/articles/15606721200911-Even-Hub-Developer-Platform-Data-Processing-Agreement)）。
- **Terminal Mode** —— `even-terminal` "runs a local HTTP server on `:3456`…, spawns your AI agent (Claude Code or Codex) as a child process, captures its streaming output, renders it onto the G2's 576×288 canvas, and translates R1 ring gestures back into keyboard events for the agent"。传输默认走局域网，也可用 `--tailscale` 或 `--expose pinggy|bore|ngrok` 隧道；包依赖 `@anthropic-ai/claude-agent-sdk`、`express` 与 `ws`（[`@evenrealities/even-terminal` README 与 manifest](https://registry.npmjs.org/@evenrealities%2Feven-terminal)；读取于 2026-09-01）。站点把交互描述为 "Approve simple actions with a ring tap; tap and hold to record a quick voice instruction"（[Terminal](https://www.evenrealities.com/terminal)）。
- **Even AI / EvenLLM** —— FAQ 声称自研模型 "understands context in real time"、"intelligently retrieves and refines relevant information"（[Even G2](https://www.evenrealities.com/smart-glasses)）；未找到任何 model card、基准或架构说明。
- **固件更新与安全响应** —— 眼镜与戒指的 OTA 固件更新（207 篇支持文章中相当一部分是升级失败的处理），以及一份覆盖 "Official device firmware and embedded software" 与 "Device communication, update, authentication, and authorization mechanisms" 的漏洞披露流程（[Zendesk 帮助中心](https://support.evenrealities.com/hc/en-us)、[Vulnerability Disclosure Policy](https://support.evenrealities.com/hc/en-us/articles/15840567983887-Vulnerability-Disclosure-Policy)）。

### 招聘所需技术背景

以下是 2026-09-01 在公司猎聘企业页上可见的 20 个岗位，薪资与要求按原文照录。全部 base 深圳-南山区；`·14薪`、`·16薪` 表示 14 薪与 16 薪结构（[猎聘企业页](https://m.liepin.com/company/13683985/)）。

| 岗位（原文） | 薪资 | 经验 | 学历 | 发布 |
|---|---|---|---|---|
| 结构专家 | 50-80k·14薪 | 10年以上 | 本科 | 2026-08-19 |
| 显示驱动硬件专家 | 50-80k·16薪 | 5-10年 | 本科 | 2026-08-15 |
| 声学专家/声学lead | 45-75k·16薪 | 5年以上 | 统招本科 | 2026-08-15 |
| 结构仿真工程师 | 40-70k·14薪 | 1年以上 | 硕士 | 2026-08-19 |
| 供应经理（GSM） | 35-55k | 5-10年 | 本科 | 2026-08-21 |
| 资深结构工程师 | 30-60k·14薪 | 5年以上 | 统招本科 | 2026-08-19 |
| 模具专家 | 30-60k·14薪 | 8年以上 | 统招本科 | 2026-08-19 |
| 高级声学工程师 | 30-60k·14薪 | 5年以上 | 统招本科 | 2026-08-19 |
| 材料工艺工程师（五金方向） | 30-45k·14薪 | 8年以上 | 本科 | 2026-08-19 |
| 模具工程师 | 30-40k·14薪 | 经验不限 | 本科 | 2026-08-19 |
| 独立站运营 | 25-55k·14薪 | 5-10年 | 本科 | 2026-08-24 |
| Industrial Designer _Senior | 25-55k | 5-10年 | 统招本科 | 2026-08-07 |
| 资深品牌设计（展陈方向） | 25-45k·14薪 | 经验不限 | 统招本科 | 2026-08-24 |
| 结构工程师 | 25-45k·14薪 | 3-5年 | 本科 | 2026-08-19 |
| 资深SQE物料质量工程师 | 20-40k·14薪 | 5-10年 | 本科 | 2026-08-19 |
| DQE研发质量工程师 | 20-30k | 5-10年 | 统招本科 | 2026-08-19 |
| 物流专员（中台效率与成本） | 18-25k·14薪 | 3年以上 | 统招本科 | 2026-08-19 |
| 售后备件管理 | 15-25k | 5年以上 | 本科 | 2026-08-31 |
| 售后维修工程师（盐田保税区） | 15-25k·14薪 | 5-10年 | 大专 | 2026-08-24 |
| 包装工程师 | 15-25k·14薪 | 3年以上 | 统招本科 | 2026-08-19 |

可见的 20 个岗位里没有一个是软件、固件、算法或 AI 岗位，尽管页面写着共 64 个在招职位，并在发帖招聘官里列出了 "AI Leader" 与 "Co-founder & CTO"。可见的这批以机械结构、模具与材料、声学、显示驱动硬件、质量（SQE/DQE）、包装、物流、售后与工业/品牌设计为主 —— 是消费硬件制造企业的画像。

### 行业领域

- **眼视光与屈光眼镜。** 产品按屈光器械卖：单光支持 "from -12.00 to +12.00"，按度数解释 1.60 / 1.67 / 1.74 三档折射率，渐进片只通过授权零售商配，另有 "UltraFit" 服务由 "your optician fine-tunes tilt, vertex distance and wrap angle"（[Even G2](https://www.evenrealities.com/smart-glasses)、[Technology](https://www.evenrealities.com/tech)）。
- **光波导与 Micro LED 显示工程。** 公开参数是 FoV、nits、刷新率、透光率与光栅设计，而不是软件指标（[Even G2](https://www.evenrealities.com/smart-glasses)）。
- **联网产品监管。** 公司公布了 **UK PSTI Act 2022 合规声明**，附各产品 PDF，并给出安全更新期限下限："We will maintain security updates for some device models for at least 5 years from the date of release"（[UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance)）。
- **欧盟/英国数据保护。** 欧洲经济区的控制者是柏林 GmbH；数据存放在荷兰服务器；与香港、深圳、东京、特拉华关联方之间的跨境共享依赖标准合同条款与数据传输影响评估（[Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP)、[Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers)）。
- **消费者健康数据。** R1 采集心率、血氧、睡眠与活动数据，公司为此单独发布了 **Consumer Health Data Privacy Policy** 与 **Privacy Notice for Health Data**（[Privacy & Legal 分类](https://support.evenrealities.com/hc/en-us/categories/13501923846159-Privacy-Legal)）。

### 工作条件

| 项目 | 内容 | 出处 |
|---|---|---|
| 地点 | 自述深圳（南山区乐普大厦）与柏林（Friedrichstraße 79）双总部；可见的 20 个岗位全部在 深圳-南山区 | [猎聘企业页](https://m.liepin.com/company/13683985/) |
| 列出的福利 | 弹性工作、领导好、扁平管理、年底双薪、绩效奖金、股票期权、五险一金、定期体检、节日礼物、年度旅游、团队聚餐、带薪年假；另有"公积金全额缴纳" | [猎聘企业页](https://m.liepin.com/company/13683985/) |
| 公开薪资区间 | 可见的 20 个岗位为月薪 15k–80k 人民币，多数为 14 薪，两个 "专家/lead" 硬件岗为 16 薪 | [猎聘企业页](https://m.liepin.com/company/13683985/) |
| 应届与初级 | 可见岗位要求 3 年以上至 10 年以上；两个写"经验不限"，一个仿真岗接受"1年以上"但要求硕士 | [猎聘企业页](https://m.liepin.com/company/13683985/) |
| 工作语言 | 招聘启事与企业介绍是中文；产品、文档、开发者平台与支持界面是英文；有一个岗位标题用英文写（"Industrial Designer _Senior"）。未公布语言政策 | [猎聘企业页](https://m.liepin.com/company/13683985/)、[Even Hub 文档](https://hub.evenrealities.com/docs) |
| 招聘渠道 | `evenrealities.com` 上没有招聘页 —— 页面 sitemap 中没有 `/careers` 或 `/jobs`；招聘走猎聘等中国招聘平台 | [页面 sitemap](https://www.evenrealities.com/sitemap/pages/1.xml)；读取于 2026-09-01 |

---

## 备注

### 未公开披露

2026-09-01 检索范围：`evenrealities.com`（robots.txt、四个 sitemap、产品/技术/公司/零售/terminal 页面与商品结构化数据）、`evenrealities.cn`、`hub.evenrealities.com`、Zendesk 帮助中心及其 API、GitHub 组织与仓库、npm registry、Apple App Store 搜索 API、Discord invite API，以及中英文网络检索：

- **收入、ARR、毛利，或 2024 年之后的销量。** 唯一的销量数字是 2024 年 G1 的"小半年一万多副"，TechCrunch 转述为已超额完成的目标。
- **2026 年 pre-B 之前每一轮的金额。** 天使轮、Pre-A 与 A 轮的规模，公司与所查来源均未公布。
- **六个具名主体之间的持股关系**（香港、柏林、特拉华、东京、深圳的 "Even Realities Ltd"，以及深圳市逸文科技有限公司）。法律文件只把它们列为关联方，没有说明结构。
- **公司自己发布的任何融资公告。** `/press` 对自动化客户端返回 JavaScript 中间页，新闻博客中也没有融资文章。
- **招聘页，或中国以外的任何薪资区间。** 柏林被写作总部之一，但所查来源中没有找到任何柏林岗位。
- **工程博客或技术写作。** 博客是产品、选购指南与媒体转载；`even-insider` 分类是编辑内容而非技术内容。
- **EvenLLM 的任何规格** —— 模型规模、供应商、推理是在设备端、手机端还是云端，以及任何基准。
- **公开的 SLA、安全认证（SOC 2、ISO 27001）或渗透测试摘要。** 公司公布的是漏洞披露政策与 PSTI 声明，不是认证。
- **`evenrealities.cn` 的 ICP 备案。** 页面上没有备案号字符串；该站点提供的是英文商城，与 TechCrunch 关于产品尚未在中国销售的报道一致。
- **2026-09-01 无法读取的来源：** CNBC（HTTP 403）、Quartz（HTTP 403）、`evenrealities.com/press`（反爬中间页），以及 Shopify 的 `products.json` 与单品 `.js` 接口（HTTP 404，已被封禁 —— 价格改从页内结构化数据读取）。

### 不同来源之间的不一致

- **Even G2 显示分辨率，三个数字。** 商品页的规格表写 **640×350**；同一页的 `Product` 结构化数据写 **"640×400 (100% increase from Even G1)"**；开发者文档与 `even-terminal` 的 readme 都把渲染目标描述为 **576×288**（[Even G2](https://www.evenrealities.com/smart-glasses)、[Even G2 A JSON-LD](https://www.evenrealities.com/products/g2-a)、[Even Hub 文档](https://hub.evenrealities.com/docs)、[`even-terminal`](https://registry.npmjs.org/@evenrealities%2Feven-terminal)）。站点自己给 G1 的数字是 640×200，翻倍应为 640×400 而非 640×350。
- **CTO 的中文名。** 公司猎聘页写 **欧阳剑**；雷峰网写 **欧阳健**（[猎聘企业页](https://m.liepin.com/company/13683985/)、[雷峰网（语言：zh）](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)）。
- **人数。** "100-499人"（猎聘，2026-09-01）、"300 to 400 employees"（TechCrunch，2026-07-06）、"约100人"（深圳市发改委，2025-07-13）。
- **公司自己招聘页上的融资阶段**在 2026-09-01 仍写着 "A轮"，距 pre-B 轮被报道已过两个月（[猎聘企业页](https://m.liepin.com/company/13683985/)、[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)）。
- **Even G1 价格。** 上市报道与深圳市发改委的文章写 599 美元；2026-09-01 商品页结构化数据中的起售价是 499 美元（[深圳市发改委（语言：zh）](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html)、[Even G1 A](https://www.evenrealities.com/products/g1-a)）。
- **官网。** 公司猎聘页写"公司官网：https://www.evenrealities.cn"；商城、法律文件与开发者平台用的都是 `evenrealities.com`（[猎聘企业页](https://m.liepin.com/company/13683985/)）。
- **透光率。** G1 与 G2 的规格表都写 98%；技术页只写 "a high rate of light transmission" 而没给数字；中文报道关于 G1 写的是 99%（[Even G1](https://www.evenrealities.com/g1)、[搜狐（语言：zh）](https://www.sohu.com/a/812622589_120998866)）。
- **光学技术命名。** G1 页面叫 "HAOS™ —— Holistic Adaptive Optical System"；当前技术页叫 "Even HAO™ —— Holistic Adaptive Optics"（[Even G1](https://www.evenrealities.com/g1)、[Technology](https://www.evenrealities.com/tech)）。
- **轮次命名。** TechCrunch 把 2026 年 7 月这轮称为 "pre-Series B"；所查的公司自有材料中完全没有给这轮命名。

### 其他

- **相对于公司体量，开发者平台的拉力是可测量的。** SDK 月下载 238,666 次、CLI 207,762 次，Discord 16,182 名成员，GitHub 组织 833 followers，BLE demo 仓库 473 stars —— 而这是一家约 300–400 人、旗舰产品 2025 年 11 月才发布的硬件公司（[npm API](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk)、[Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true)、[GitHub API](https://api.github.com/orgs/even-realities)）。
- **npm 上已经存在第三方开发者生态。** 由公司之外的人发布的包包括 `@even-toolkit/create-even-app`、`even-sim-recorder`、`even-demo-kit`、`@penta2himajin/even-deskless` 与 `even-terminal-pi`（为另一种编码 agent 写的 provider 适配层）（[npm 搜索](https://registry.npmjs.org/-/v1/search?text=evenhub&size=20)；读取于 2026-09-01）。
- **Terminal Mode 是一家眼镜公司发布的编码 agent 产品。** 它依赖 Anthropic 的 `@anthropic-ai/claude-agent-sdk`，把 Claude Code 与 Codex 列为 provider；站点上的用户评价墙日期为 2026 年 4 月至 6 月，取自 Discord（[`even-terminal`](https://registry.npmjs.org/@evenrealities%2Feven-terminal)、[Terminal](https://www.evenrealities.com/terminal)）。
- **不装摄像头是写明的产品约束，不是遗漏。** 它同时出现在 FAQ、开发者文档（"No camera, no speaker"）与 CEO 在报道中的表述里（[Even G2](https://www.evenrealities.com/smart-glasses)、[Even Hub 文档](https://hub.evenrealities.com/docs)、[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)）。
- **渠道形态更像眼镜零售而不是电子零售**：有验光师适配服务、按门店类型分类的合作申请表单，以及与 Yodobashi、BIC CAMERA 并列的具名眼镜零售商（[Retail](https://www.evenrealities.com/retail)、[Partner with Us](https://www.evenrealities.com/partner-with-us)）。
- **一家只在海外卖的中国公司。** TechCrunch 报道产品 "Not yet sold in China"，美国是增长最快的市场，另外还点了日本、韩国、中东与欧洲；站点的语言/地区覆盖德语、西语、法语、意语、日语、韩语与港版中文，但没有中国大陆（[TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)、[evenrealities.com](https://www.evenrealities.com/)）。
- **创始团队是一个坚果投影（JMGO）的同事群。** CEO、CDO 与 CTO 在公司自己的招聘页上都被描述为在创办 Even Realities 之前在坚果投影负责产品、设计或研发（[猎聘企业页](https://m.liepin.com/company/13683985/)）。

---

## 资料来源

**官方**

- [evenrealities.com](https://www.evenrealities.com/) · [robots.txt](https://www.evenrealities.com/robots.txt) · [sitemap index](https://www.evenrealities.com/sitemap.xml) · [页面 sitemap](https://www.evenrealities.com/sitemap/pages/1.xml) · [evenrealities.cn](https://www.evenrealities.cn/)
- 产品 —— [Even G1](https://www.evenrealities.com/g1) · [Even G2](https://www.evenrealities.com/smart-glasses) · [Even R1](https://www.evenrealities.com/smart-ring) · [Technology](https://www.evenrealities.com/tech) · [Terminal](https://www.evenrealities.com/terminal) · [Store](https://www.evenrealities.com/store) · [Retail](https://www.evenrealities.com/retail) · [企业采购](https://www.evenrealities.com/enterprise-purchase) · [Partner with Us](https://www.evenrealities.com/partner-with-us)
- 商品结构化数据 —— [Even G2 A](https://www.evenrealities.com/products/g2-a) · [Even G2 B](https://www.evenrealities.com/products/g2-b) · [Even G1 A](https://www.evenrealities.com/products/g1-a) · [Even R1](https://www.evenrealities.com/products/r1)
- 公司 —— [Company](https://www.evenrealities.com/company) · [Blog](https://www.evenrealities.com/blog) · [News](https://www.evenrealities.com/blogs/news) · [媒体转载](https://www.evenrealities.com/blogs/press)
- 开发者 —— [Even Hub](https://hub.evenrealities.com) · [Even Hub 文档](https://hub.evenrealities.com/docs) · [GitHub `even-realities`](https://api.github.com/orgs/even-realities) · [EvenDemoApp](https://github.com/even-realities/EvenDemoApp) · [evenhub-templates](https://github.com/even-realities/evenhub-templates) · [npm `@evenrealities/even_hub_sdk`](https://registry.npmjs.org/@evenrealities/even_hub_sdk) · [npm `@evenrealities/even-terminal`](https://registry.npmjs.org/@evenrealities%2Feven-terminal) · [npm 下载量](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk) · [npm 搜索 "evenhub"](https://registry.npmjs.org/-/v1/search?text=evenhub&size=20) · [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true)
- 法律与合规（Zendesk）—— [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service)（最后更新 2026-07-28）· [Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP)（生效 2026-07-25）· [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) · [Vulnerability Disclosure Policy](https://support.evenrealities.com/hc/en-us/articles/15840567983887-Vulnerability-Disclosure-Policy)（生效 2026-04-17）· [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) · [Even Hub Developer Platform Terms of Service](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service)（最后更新 2026-03-24）· [Even Hub Developer Platform Data Processing Agreement](https://support.evenrealities.com/hc/en-us/articles/15606721200911-Even-Hub-Developer-Platform-Data-Processing-Agreement) · [Privacy & Legal 分类索引](https://support.evenrealities.com/hc/en-us/categories/13501923846159-Privacy-Legal) · [帮助中心文章 API](https://support.evenrealities.com/api/v2/help_center/en-us/articles.json)
- 招聘（语言：zh）—— [猎聘企业页](https://m.liepin.com/company/13683985/)

**登记与平台记录**

- [百度百科 — 深圳市逸文科技有限公司（语言：zh）](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335)
- [iTunes search API — 发布者 "Even Realities Ltd."](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10)

**第三方报道**

- [TechCrunch — Smart glasses maker Even Realities hits $1B valuation with $150M funding led by Meituan, Tencent](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) —— 2026-07-06
- [深圳市发展和改革委员会 — 逸文科技创始人王骁逸：怎么把 599 美元的智能眼镜卖给 CEO 们（语言：zh）](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html) —— 2025-07-13
- [雷峰网 — 逸文科技，为何受资本争抢？（语言：zh）](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)
- [搜狐 — 比肩"AR四小龙"？深圳这家AR企业有望一年完成三轮融资（语言：zh）](https://www.sohu.com/a/812622589_120998866) —— 2024-09
- [腾讯新闻 — 深圳AR眼镜公司Even Realities发生工商变更，新增股东（语言：zh）](https://news.qq.com/rain/a/20240812A06XK100) —— 2024-08-12
