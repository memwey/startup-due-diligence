# Even Realities

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-09-01.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Even Realities sells display-first smart glasses with no camera and no speaker: **Even G1** (2024), **Even G2** (2025) and the **Even R1** smart ring that controls them. A green Micro LED projector feeds a waveguide; the paired phone does the computing. The website is "owned and operated by **Hong Kong Even Realities Limited**", with separate contracting entities for the EEA (**Even Realities GmbH**, Berlin) and the United States (**Even Realities US Inc**, Delaware) ([Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service); last updated 2026-07-28). The company's own recruiting page describes it as "总部位于中国深圳与德国柏林" — dual-headquartered in Shenzhen and Berlin ([Liepin employer page](https://m.liepin.com/company/13683985/); read 2026-09-01).

- **US$150M pre-Series B at a US$1B valuation**, announced 2026-07-06, led by **Meituan** with **Tencent** participating; earlier backers named in coverage include HSG (formerly Sequoia China) and Hillhouse ([TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)) — see `Funding`.
- The **UK PSTI statement of compliance** gives exact release dates and a security-support floor: G1 released 2024-06-25 (updates to no earlier than 2029-06-25), G2 and R1 released 2025-11-12 (no earlier than 2030-11-12) ([UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance)).
- There is a **real developer platform with observable usage**: the MIT-licensed `@evenrealities/even_hub_sdk` was downloaded **238,666 times** in the month to 2026-08-29, and the Even Realities Discord had **16,182 members** ([npm downloads](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk), [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true); read 2026-09-01).
- A **Terminal Mode** ships as an npm CLI that spawns **Claude Code or Codex** on the developer's laptop and renders the session onto "the G2's 576×288 canvas", driven by R1 ring gestures ([`@evenrealities/even-terminal`](https://www.npmjs.com/package/@evenrealities/even-terminal); readme read 2026-09-01) — see `Systems`.
- Hiring is **hardware-shaped**: all 20 job postings visible on the company's Liepin page on 2026-09-01 were structural, mould, acoustics, display-driver, quality, packaging, supply-chain or design roles in Shenzhen-Nanshan, against a stated total of 64 open positions ([Liepin employer page](https://m.liepin.com/company/13683985/)).
- TechCrunch reports the company is **not yet sold in China**, with the US its fastest-growing market ([TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/); 2026-07-06).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Even Realities | [evenrealities.com](https://www.evenrealities.com/); accessed 2026-09-01 |
| Website operator | "This Website is owned and operated by Hong Kong Even Realities Limited, together with its affiliates and subsidiaries (including, for example, Even Realities GmbH)" | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service); last updated 2026-07-28 |
| Hong Kong entity address | "Room 29D, 8/F, On Cheong Factory Building, No. 19 Tai Yip Street, Kwun Tong, Hong Kong" | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| EEA entity | "Even Realities GmbH, a company registered in Berlin, with its registered address located at Friedrichstraße 79, 10117 Berlin, Germany" — also the named controller in the device/app privacy policy | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service), [Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP) |
| US entity | "Even Realities US Inc, a company registered in State of Delaware, with its registered address located at 8 The Green Ste A, Dover, Kent, DE 19901" | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| Shenzhen entity | "Even Realities Ltd, Building West 2603, LEPU TOWER, Nanshan District, Shenzhen, China" | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers); updated 2026-08-18 |
| Japan entity | "Even Realities Co., Ltd., 2F, Ginza Otake Residence, 1-22-11 Ginza, Chuo-ku, Tokyo, Japan" | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) |
| Chinese legal name | 深圳市逸文科技有限公司, established 2023-06-02, Nanshan District, Shenzhen; legal representative 王骁逸 | [Baidu Baike (language: zh)](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335), [Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866) |
| Mobile-app publisher | "Even Realities Ltd." — apps `Even Realities` (`com.even.sg`, first released 2025-11-21) and `Even G1` (`com.even.g1`, first released 2024-07-31) | [iTunes search API](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10); read 2026-09-01 |
| Founded | 2023; the Chinese entity was established 2023-06-02 | [Liepin employer page](https://m.liepin.com/company/13683985/), [Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866) |
| Stated headquarters | "总部位于中国深圳与德国柏林" (Shenzhen and Berlin); Shenzhen address 深圳市南山区乐普大厦, Berlin address Friedrichstraße 79 | [Liepin employer page](https://m.liepin.com/company/13683985/) |
| Headcount | "100-499人" on the company's Liepin page; TechCrunch reported 300–400 employees, up from 30–40 in 2024; a Shenzhen municipal profile said about 100 in July 2025 | [Liepin employer page](https://m.liepin.com/company/13683985/), [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/), [Shenzhen DRC (language: zh)](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html) |
| Open roles | "职位 · 64" stated; 20 postings visible on the page, all in 深圳-南山区 | [Liepin employer page](https://m.liepin.com/company/13683985/); read 2026-09-01 |
| Investors named by the company | "鼎晖投资、青山资本、红杉资本、砺思资本、爱尔眼科" (CDH Investments, Qingshan Capital, Sequoia, Monolith, Aier Eye Hospital) | [Liepin employer page](https://m.liepin.com/company/13683985/) |
| Valuation | US$1B post-money, stated 2026-07-06 | [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) |
| Retail footprint | "产品已入驻全球300+高端眼镜店" (300+ premium eyewear stores worldwide); the G1 page says "over 300 opticians who can fine-tune your Even G1" | [Liepin employer page](https://m.liepin.com/company/13683985/), [Even G1](https://www.evenrealities.com/g1) |
| Named retail channels | Japan: Yodobashi, BIC CAMERA. Taiwan: Taiwan Mobile, E-life Mall, Fayaque, eslite spectrum. Korea: Naver Store operated by Mune. US showroom: Alexander Daas Opticians, San Francisco | [Retail](https://www.evenrealities.com/retail); accessed 2026-09-01 |
| Storefront | Shopify (store id 60045131891); site served over Shopify CDN | [robots.txt](https://www.evenrealities.com/robots.txt), product pages; read 2026-09-01 |
| Support platform | Zendesk help centre at `support.evenrealities.com` — 207 articles | [Zendesk help-centre API](https://support.evenrealities.com/api/v2/help_center/en-us/articles.json); read 2026-09-01 |
| Site locales | `de-DE`, `es-ES`, `fr-FR`, `it-IT`, `ja-JP`, `ko-KR`, `zh-Hans-HK`, `zh-Hant-HK` alongside the default English store | [evenrealities.com](https://www.evenrealities.com/) footer; read 2026-09-01 |
| Community | Discord "Even Realities" — 16,182 members, 2,444 online; server created 2024-10-30 | [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true); read 2026-09-01 |
| Public social accounts | X `@EvenRealities`, LinkedIn `even-realities`, Instagram, TikTok, YouTube, Facebook — all listed in the site's `Organization` structured data | product-page JSON-LD; read 2026-09-01 |
| GitHub organisation | `even-realities` — created 2024-10-22, 5 public repositories, 833 followers, website field `evenrealities.com` | [GitHub API](https://api.github.com/orgs/even-realities); read 2026-09-01 |
| Security contact | `software@evenrealities.com` for vulnerability reports; `support@evenrealities.com` for UK PSTI security issues, acknowledged within 24 hours and updated every 7 days | [Vulnerability Disclosure Policy](https://support.evenrealities.com/hc/en-us/articles/15840567983887-Vulnerability-Disclosure-Policy) (effective 2026-04-17), [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) |

### Identity and legal entities

| Name | Type | Jurisdiction | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Even Realities | Public brand | Global | Brand on all product surfaces and packaging | [evenrealities.com](https://www.evenrealities.com/) |
| Hong Kong Even Realities Limited | Legal entity | Hong Kong | "owned and operated by"; the default contracting party outside the EEA and US | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| Even Realities GmbH | Legal entity | Berlin, Germany | Contracting party for EEA users; controller named in the device/app privacy policy | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service), [Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP) |
| Even Realities US Inc | Legal entity | Delaware, USA | Contracting party for US users | [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) |
| Even Realities Ltd | Related entity | Shenzhen, China | Listed among "affiliated companies" that may receive personal data under the group's data policy | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) |
| Even Realities Co., Ltd. | Related entity | Tokyo, Japan | Listed among the same affiliated companies | [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) |
| 深圳市逸文科技有限公司 | Legal entity | Shenzhen, China | Chinese registered company behind the brand; legal representative 王骁逸 | [Baidu Baike (language: zh)](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335) |
| `evenrealities.cn` | Parallel domain | — | Serves the same English store as `evenrealities.com`; the company's Liepin page lists it as "公司官网"; no ICP filing string was found on the page | [evenrealities.cn](https://www.evenrealities.cn/), [Liepin employer page](https://m.liepin.com/company/13683985/); read 2026-09-01 |

No source reviewed states the ownership relationships between the Hong Kong, German, US, Japanese, Shenzhen and Chinese-registered entities. The English name "Even Realities Ltd" is used both by the Apple App Store publisher record and, with a Shenzhen address, in the group's data-transfer disclosure.

---

## Product

### What it is and its feature areas

Three shipping products, all of them "camera-free" by design ([Even G2 FAQ](https://www.evenrealities.com/smart-glasses): "To prioritize your privacy and deliver a seamless display experience, Even G2 relies on its integrated microphone for information input rather than a camera").

| Product | Released | Published specifications |
|---|---|---|
| Even G1 | 2024-06-25 | Waveguide, binocular, green Micro LED, resolution 640×200, FoV 25°, refresh 20 Hz, brightness 1000 nits, 98% passthrough, two microphones, BLE 5.2, wireless charging, "up to 1.5 days" battery, splash/light-rain resistant, prescription lenses in Mitsui Chemicals MR™ material |
| Even G2 | 2025-11-12 | Waveguide, binocular, green Micro LED, resolution 640×350, FoV 27.5°, refresh 60 Hz, brightness 1200 nits, 98% passthrough, four microphones, BLE 5.4, "up to 2 days" battery with a case holding "up to 7 full charges", IP65, magnesium and titanium frame, screwless hinge |
| Even R1 | 2025-11-12 | "Zirconia ceramic with medical-grade stainless steel lining", IP68, "Up to 7 days" battery, 90-minute charge, Bluetooth BLE, heart rate via LED beam, accelerometer step/calorie/distance tracking, controls the G2 |

Sources: [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) for the release dates; [Even G1](https://www.evenrealities.com/g1), [Even G2](https://www.evenrealities.com/smart-glasses) specification tables and [Even R1 product JSON-LD](https://www.evenrealities.com/products/r1) for the specifications; all accessed 2026-09-01.

Feature names published on the site: **Conversate**, **Teleprompt**, **Translate**, **Even AI**, **HUD / Dashboard**, **Transcribe**, **Navigate** ("Works wherever Google Maps does"), **QuickNote** / **QuickList**, **Health**, and **Terminal** ([evenrealities.com](https://www.evenrealities.com/) footer; accessed 2026-09-01). The G2 FAQ states the assistant runs on a proprietary model: "Even G2 runs on Even AI, powered by our proprietary EvenLLM" ([Even G2](https://www.evenrealities.com/smart-glasses)).

Optical claims on the technology page: **Even HAO™** ("Holistic Adaptive Optics") described as "our proprietary technology turning the glasses projectors, waveguides and lenses into a perfect orchestra"; a projector "40% smaller. But brighter and sharper imagery"; lens centres "30% slimmer"; "over 100 layer coatings"; a graded grating that "spreads the light more evenly"; **TriSync** three-way connectivity between temples, phone and ring; and durability testing — "Screwless hinges opened and closed 40,000 times", "Drop-tested from 2 metres", "Certified IP65". Fit was designed against "100,000 3-D head shapes" analysed in the company's behavioural labs ([Technology](https://www.evenrealities.com/tech); accessed 2026-09-01).

The company page attributes the ophthalmic work to a named external collaborator: "Dr. Qu Jia, Honorary Doctor at New England College of Optometry and former President of Wenzhou Medical University, is leading an ophthalmology team specializing in visual brain processing, myopia control, and contact lenses" ([Company](https://www.evenrealities.com/company); accessed 2026-09-01).

### Commercialization

Direct-to-consumer hardware sales through a Shopify storefront, plus optical and electronics retail partners and an enterprise-purchase channel. Published US prices, read 2026-09-01 from the product pages' structured data:

| Product | Published price points (USD) |
|---|---|
| Even G2 A / Even G2 B | 599, 758, 828, 948 |
| Even G1 A | 499, 658 |
| Even R1 | 249 |

Sources: [Even G2 A](https://www.evenrealities.com/products/g2-a), [Even G2 B](https://www.evenrealities.com/products/g2-b), [Even G1 A](https://www.evenrealities.com/products/g1-a), [Even R1](https://www.evenrealities.com/products/r1). The higher price points correspond to prescription and lens-index options rather than separate models. TechCrunch reported the economics as "$599" frames with "prescription lenses or ring add $200-$300, averaging ~$1,000 per order" ([TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)).

Other commercial surfaces: an **enterprise purchase** page, a **partner-with-us** form segmented into "Optical Store / Distributor / Other Retailer", a **creators** collaboration form, and a **10% education discount** promoted site-wide ([evenrealities.com](https://www.evenrealities.com/); accessed 2026-09-01). Warranty is "2-year warranty for Europe and a 1-year warranty for all other regions"; non-prescription returns run 14 days, prescription orders can only be cancelled "within 24 hours of purchase" ([Even G2 FAQ](https://www.evenrealities.com/smart-glasses)).

The developer platform carries no published revenue share. The Even Hub Developer Platform terms describe plug-in submission, "Publication Review" ("development information verification, security testing, UI testing, and dynamic testing") and rejection, and grant Even Realities a "non-exclusive, transferable, sublicensable, royalty-free, worldwide license" over Developer Content; no fee, commission or payout schedule appears in the agreement ([Even Hub Developer Platform Terms of Service](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service); last updated 2026-03-24).

### Reported scale over time

| Date | Figure as stated | Source |
|---|---|---|
| 2023-06-02 | 深圳市逸文科技有限公司 established | [Baidu Baike (language: zh)](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335) |
| 2024-06-25 | Even G1 released | [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) |
| 2024-07-31 | `Even G1` iOS app first released | [iTunes search API](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10) |
| 2024-10-22 / 2024-10-28 | GitHub organisation created; `EvenDemoApp` (BLE protocol reference implementation) first published | [GitHub API](https://api.github.com/orgs/even-realities) |
| 2024-10-30 | Discord server created | [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true) |
| 2025 (reported) | "小半年的时间卖出一万多副" — 10,000+ G1 units in roughly half a year; "40多个国家和地区" and "300多家欧洲眼镜店" | [Leiphone (language: zh)](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html) |
| 2025-07-13 | Shenzhen municipal profile: about 100 employees; G1 at US$599 | [Shenzhen DRC (language: zh)](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html) |
| 2025-11-12 | Even G2 and Even R1 released | [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) |
| 2025-11-21 | `Even Realities` iOS app (`com.even.sg`) first released | [iTunes search API](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10) |
| 2026-01-27 | `@evenrealities/even_hub_sdk` first published to npm | [npm registry](https://registry.npmjs.org/@evenrealities/even_hub_sdk) |
| 2026-04-25 | `@evenrealities/even-terminal` first published to npm | [npm registry](https://registry.npmjs.org/@evenrealities%2Feven-terminal) |
| 2026-07-06 | US$150M round at a US$1B valuation; 300–400 employees, up from 30–40 in 2024; "surpassed its 10,000-unit sales target" for G1 | [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) |
| 2026-08-29 | npm downloads in the trailing month: 238,666 for the Even Hub SDK, 207,762 for the CLI, 2,886 for `even-terminal` | [npm API](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk) |
| 2026-09-01 | Discord 16,182 members; GitHub org 833 followers; 64 stated open positions | [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true), [GitHub API](https://api.github.com/orgs/even-realities), [Liepin employer page](https://m.liepin.com/company/13683985/) |

### Announced customers, partners and named users

| Name | What is claimed | Source |
|---|---|---|
| Palmer Luckey | Founder of Oculus and Anduril; "At TED 2025, he delivered a flawless talk with no notes or teleprompter, later admitting he'd read it all off his G1" | [evenrealities.com](https://www.evenrealities.com/); accessed 2026-09-01 |
| Amy Tan | Author; uses Conversate for on-stage interviews and Translate for foreign-language drama | [evenrealities.com](https://www.evenrealities.com/) |
| Jason Rajasinghe, Andres Vidoza, Duncan Clark | Named creators/users on the homepage carousel | [evenrealities.com](https://www.evenrealities.com/) |
| InnoHome (Taiwan) | "Even Realities Taiwan strategic partnership with InnoHome brings Even G2 to Taiwan" | [News blog](https://www.evenrealities.com/blogs/news/even-realities-taiwan-strategic-partnership-with-innohome-brings-even-g2-to-taiwan) |
| Jun Ginza (Japan) | "Even Day Japan 2026 supported by Jun Ginza"; a second post on the retail partnership | [News blog](https://www.evenrealities.com/blogs/news/event-recap-even-day-japan-2026-supported-by-jun-ginza) |
| Tokyo 2025 Deaflympics | "Beyond the Water: Empowering Lives at the Tokyo 2025 Deaflympics" | [Stories blog](https://www.evenrealities.com/blogs/stories/beyond-the-water-empowering-lives-at-the-tokyo-2025-deaflympics) |
| Ottica La Fege, Line of Sight, Hungry Eyes | Named eyewear retailers in company news posts | [News blog](https://www.evenrealities.com/blogs/news/heritage-meets-future-ottica-la-fege-on-even-g2) |

Press recognitions the company republishes, all posted 2026-04-17: USA Today naming the G2 "one of best innovations at CES 2026", The Guardian listing it among "the best gadgets at CES 2026", plus reviews from WIRED, CNET, ZDNET, TechRadar, Mashable, Tom's Guide, BBC and Business Insider Japan ([Press blog](https://www.evenrealities.com/blogs/press/usa-today-names-even-g2-one-of-best-innovations-at-ces-2026)). USA Today's piece as republished gives the G2 weight as 36 grams.

### Stated plans

- Even Hub is described as a platform under active construction, inviting developers to "create spatial experiences and collaborate with early developers shaping the platform" ([hub.evenrealities.com](https://hub.evenrealities.com); accessed 2026-09-01).
- A page titled `even-g2-x-007-first-light` exists in the site's page sitemap ([pages sitemap](https://www.evenrealities.com/sitemap/pages/1.xml); read 2026-09-01).
- The G1 FAQ states R1 compatibility is not shipped: "Even R1 currently supports interaction only with Even G2 and is not yet compatible with Even G1. Our product team is actively expanding device compatibility" ([Even G1](https://www.evenrealities.com/g1)).

---

## Founder

The company's own Liepin employer page publishes four co-founders with dated career detail (in Chinese; read 2026-09-01, [Liepin employer page](https://m.liepin.com/company/13683985/)):

| Name | Title | Career facts as published |
|---|---|---|
| 王骁逸 (Will Wang) | 创始人 / CEO | 上海交通大学 机械工程学士; 加州大学伯克利分校 运筹学硕士. Product lead at "P&G、Western Digital、Apple、OPPO、坚果投影". "负责Apple制造设计，深度参与iPhone、Apple Watch等数款产品的研发与量产". As CPO of 坚果投影 (JMGO), led the O-series ultra-short-throw, N-series gimbal projectors and "目氪三色激光". |
| 胡丹 (Dan Hu) | 联合创始人 / CDO | 国立华侨大学 工业设计学士; 香港理工大学 设计策略硕士. Design lead at "Philips、Samsung、韶音、清华设计管理研究所、坚果投影". "Philips Design Committee唯一大陆背景成员"; led Samsung home-appliance line design and the Shokz (韶音) bone-conduction headphone line. "30余次获得国际大奖，包括IDEA金银铜奖、iF、红点、G-mark和Edison金奖". |
| 欧阳剑 (Tom Ouyang) | 联合创始人 / CTO | 普渡大学 机械工程学士; 加州大学洛杉矶分校 机械工程硕士. R&D lead at "Western Digital、Apple、坚果投影". "负责Western Digital机械硬盘MEMS微机电传动模组研发"; "Apple iPhone后置主摄模组设计负责人，前后完成8款主摄模组量产项目落地"; at JMGO, optics and structures lead. |
| 王力 (Christy Wang) | 联合创始人 / COO | 上海交通大学 金融英语学士. "百度战略办专家、执一资本、弈秋资本、势乘资本等机构董事及管理合伙人"; "累计融资额近40亿" across angel to pre-IPO projects. |

TechCrunch describes the CEO as having "spent two years at Apple before leaving in 2018, contributing to both the Apple Watch and iPhone", and says the founding team "drew from enterprise technology and the luxury eyewear world" ([TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/); 2026-07-06).

Two eyewear-industry hires are named in Chinese coverage rather than by the company: **Nicolai Schnur**, described as a former LINDBERG CMO, and **Philipp Haffmans**, described as a co-founder of MYKITA and ic! berlin ([Leiphone (language: zh)](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)). The company's own recruiting copy states the team draws on "MYKITA、Ic!berlin、LINDBERG等高端眼镜行业资深专家" and "Apple、华为、OPPO、vivo等消费电子巨头背景", and the company page lists "Apple, Samsung, Philips, Mykita and Lindberg" as prior employers ([Liepin employer page](https://m.liepin.com/company/13683985/), [Company](https://www.evenrealities.com/company)).

The Liepin page also lists recruiter accounts by role, including "Co-founder & CTO — 4个职位", "AI Leader — 2个职位", "COO — 1个职位" and "设计负责人 — 1个职位", indicating those functions exist and hire directly ([Liepin employer page](https://m.liepin.com/company/13683985/)).

---

## Funding

| Date | Round | Amount | Investors | Source |
|---|---|---|---|---|
| 2024-01 | 天使轮 (angel) | Not disclosed | Not named | [Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866) |
| 2024-08 | Pre-A | Not disclosed | 博原资本 (Boyuan), 华创资本 (Huachuang), 投中资产 | [Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866) |
| 2024-09 | Registered-capital change inferred as a further round | Not disclosed; registered capital updated to RMB 8,635,617 | New shareholder 中山市联汇股权投资合伙企业; natural-person shareholder 李莉莉 exited | [Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866), [Tencent News (language: zh)](https://news.qq.com/rain/a/20240812A06XK100) |
| 2024-12-10 | A 轮 | Not disclosed | Monolith 砺思资本, 鼎晖投资 (CDH) | [Baidu Baike (language: zh)](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335) |
| 2026-07-06 | Pre-Series B | US$150M at a US$1B post-money valuation | Meituan (lead), Tencent; earlier backers named in coverage include HSG (formerly Sequoia China) and Hillhouse | [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) |

Plain facts that do not fit the table:

- The company's own investor list, on its recruiting page, is "鼎晖投资、青山资本、红杉资本、砺思资本、爱尔眼科" — CDH, Qingshan Capital, Sequoia, Monolith and the listed eye-hospital chain Aier ([Liepin employer page](https://m.liepin.com/company/13683985/)). **Aier Eye Hospital is a strategic investor from the ophthalmology industry**, consistent with the prescription-lens positioning.
- Chinese coverage in late 2024 described the company as on course to complete three rounds within a year of the G1 launch ([Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866); 2024-09).
- No amount is published for any round before the 2026 pre-Series B in the sources reviewed. Round valuations before 2026 appear only as ranges in secondary Chinese coverage ("数亿美金", "估值超10亿" RMB) ([Leiphone (language: zh)](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)).
- The company has published no funding announcement of its own; the `/press` page returns an interstitial to automated clients and the news blog carries no financing post (checked 2026-09-01).

---

## Engineering

### Technology stack and platforms

**Confirmed by published artifacts** (packages, repositories, documentation, headers; read 2026-09-01):

- **Even Hub SDK** — `@evenrealities/even_hub_sdk`, MIT, "TypeScript SDK for Even Hub developers to communicate with Even App", 12 versions from 2026-01-27 to 0.0.14 on 2026-08-20 ([npm](https://registry.npmjs.org/@evenrealities/even_hub_sdk)).
- **Tooling** — `@evenrealities/evenhub-cli` (0.1.14), `@evenrealities/evenhub-simulator` with per-platform binaries for `darwin-arm64`, `darwin-x64`, `linux-x64`, `linux-arm64`, `win32-x64`, `win32-arm64` (0.9.4, 2026-08-31), and `@evenrealities/pretext`, "Pixel-accurate font measurement library for Even Realities G2 glasses" ([npm search](https://registry.npmjs.org/-/v1/search?text=evenhub&size=20)).
- **App model** — plug-ins are web apps: "HTML, CSS, and JavaScript or TypeScript", "Bring any stack - Vite, React, plain JS", packaged with `evenhub pack` into an `.ehpk` and uploaded to the developer portal or side-loaded by QR code. Node.js 18+ is required ([Even Hub docs](https://hub.evenrealities.com/docs), [evenhub-templates README](https://github.com/even-realities/evenhub-templates)).
- **Runtime split** — "Code executes on the phone; the glasses render and capture input" ([Even Hub docs](https://hub.evenrealities.com/docs)).
- **Display and input contract for developers** — "576 x 288 px per eye", monochrome green with "16 levels"; gestures "Press, double press, swipe up, swipe down, tap then long press and release" on the temple touchpads and optionally the R1; audio "4-mic array, single stream, 16 kHz PCM"; "No camera, no speaker" ([Even Hub docs](https://hub.evenrealities.com/docs)).
- **Wire format** — protobuf; the templates README documents a concrete footgun: "`OsEventTypeList.CLICK_EVENT` is `0`, and protobuf omits zero-value fields on the wire. A single tap therefore arrives as an envelope with **no `eventType` field at all**" ([evenhub-templates README](https://github.com/even-realities/evenhub-templates)).
- **Device BLE protocol** — the `EvenDemoApp` reference implementation (C, BSD-2-Clause, 473 stars) documents dual-BLE to the left and right temples, LC3 audio streaming from the right microphone with a 30-second cap, 1-bit 576×136 BMP image transfer in 194-byte packets with a CRC command, and text pagination at a 488-pixel line width ([EvenDemoApp README](https://github.com/even-realities/EvenDemoApp)).
- **Embedded UI** — the organisation publishes `lvgl-sys-v9`, Rust bindings for LVGL v9 ([GitHub API](https://api.github.com/orgs/even-realities/repos)).
- **Web and commerce** — Shopify storefront; Sanity CMS (`cdn.sanity.io` asset host on product pages); Zendesk help centre; Klarna, Shop Pay, Apple Pay, Google Pay, PayPal and UnionPay at checkout ([evenrealities.com](https://www.evenrealities.com/)).
- **Data hosting** — "Data generated in connection with your use of Even Realities Products is stored on servers located in the Netherlands" ([Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers)).

**Named in the company's own recruiting copy** rather than in artifacts: "从光学设计到AI算法：掌握从底层光学技术到上层AI应用的全栈核心技术" — full-stack capability from optical design to AI algorithms ([Liepin employer page](https://m.liepin.com/company/13683985/)).

### Systems

- **Optical stack** — projector, waveguide with a graded grating, and prescription lens as one system, marketed as Even HAO™; lenses are "digitally surfaced with a diamond-tipped lathe", shaped by "Free-form technology and ray-tracing software", with "over 100 layer coatings" ([Technology](https://www.evenrealities.com/tech)).
- **TriSync connectivity** — "Even G2, your phone and Even R1 work together as one intuitive system. Temple tips sync wirelessly with your phone and Ring" ([Technology](https://www.evenrealities.com/tech)). At the protocol level the glasses expose two independent BLE endpoints, one per temple ([EvenDemoApp README](https://github.com/even-realities/EvenDemoApp)).
- **Even Hub plug-in platform** — developer registration, plug-in upload, "Publication Review" with security, UI and dynamic testing, rejection and takedown mechanics, a user-complaint channel, an audit right surviving two years past termination, and a Data Processing Agreement for developer access to user data ([Even Hub Developer Platform Terms of Service](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service), [Data Processing Agreement](https://support.evenrealities.com/hc/en-us/articles/15606721200911-Even-Hub-Developer-Platform-Data-Processing-Agreement)).
- **Terminal Mode** — `even-terminal` "runs a local HTTP server on `:3456`…, spawns your AI agent (Claude Code or Codex) as a child process, captures its streaming output, renders it onto the G2's 576×288 canvas, and translates R1 ring gestures back into keyboard events for the agent". Transports are LAN by default, with `--tailscale` or `--expose pinggy|bore|ngrok` tunnels; the package depends on `@anthropic-ai/claude-agent-sdk`, `express` and `ws` ([`@evenrealities/even-terminal` README and manifest](https://registry.npmjs.org/@evenrealities%2Feven-terminal); read 2026-09-01). The site describes the interaction as "Approve simple actions with a ring tap; tap and hold to record a quick voice instruction" ([Terminal](https://www.evenrealities.com/terminal)).
- **Even AI / EvenLLM** — the FAQ claims a proprietary model that "understands context in real time" and "intelligently retrieves and refines relevant information" ([Even G2](https://www.evenrealities.com/smart-glasses)); no model card, benchmark or architecture description was found.
- **Firmware update and security response** — OTA firmware updates for glasses and ring (a large share of the 207 support articles concern update failures), plus a published vulnerability-disclosure process covering "Official device firmware and embedded software" and "Device communication, update, authentication, and authorization mechanisms" ([Zendesk help centre](https://support.evenrealities.com/hc/en-us), [Vulnerability Disclosure Policy](https://support.evenrealities.com/hc/en-us/articles/15840567983887-Vulnerability-Disclosure-Policy)).

### Technical background sought

The 20 job postings visible on the company's Liepin page on 2026-09-01 are reproduced below with the salary and requirement text as written. All are located in 深圳-南山区; `·14薪` and `·16薪` denote 14- and 16-month salary structures ([Liepin employer page](https://m.liepin.com/company/13683985/)).

| Posting (as written) | Salary | Experience | Education | Posted |
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

None of the 20 visible postings is a software, firmware, algorithm or AI role, although the page states 64 open positions and lists an "AI Leader" and a "Co-founder & CTO" among the recruiters posting jobs. The visible set is dominated by mechanical structure, mould and materials, acoustics, display-driver hardware, quality (SQE/DQE), packaging, logistics, after-sales and industrial/brand design — the profile of a consumer-hardware manufacturer.

### Industry domain

- **Ophthalmic optics and prescription eyewear.** The product is sold as a prescription device: single-vision support "from -12.00 to +12.00", lens indices 1.60 / 1.67 / 1.74 explained by prescription strength, progressive lenses only through authorised retail partners, and an "UltraFit" service in which "your optician fine-tunes tilt, vertex distance and wrap angle" ([Even G2](https://www.evenrealities.com/smart-glasses), [Technology](https://www.evenrealities.com/tech)).
- **Waveguide and Micro LED display engineering.** Published parameters are FoV, nits, refresh rate, passthrough percentage and grating design rather than software metrics ([Even G2](https://www.evenrealities.com/smart-glasses)).
- **Connected-product regulation.** The company publishes a **UK PSTI Act 2022 statement of compliance** with per-product PDFs and a stated minimum security-update period: "We will maintain security updates for some device models for at least 5 years from the date of release" ([UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance)).
- **EU/UK data protection.** The EEA controller is the Berlin GmbH; data sits on Netherlands servers; cross-border sharing with the Hong Kong, Shenzhen, Tokyo and Delaware affiliates relies on Standard Contractual Clauses and transfer impact assessments ([Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP), [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers)).
- **Consumer health data.** The R1 collects heart rate, blood oxygen, sleep and activity, and the company publishes a separate **Consumer Health Data Privacy Policy** and a **Privacy Notice for Health Data** ([Privacy & Legal category](https://support.evenrealities.com/hc/en-us/categories/13501923846159-Privacy-Legal)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Locations | Shenzhen (南山区乐普大厦) and Berlin (Friedrichstraße 79) stated as dual headquarters; all 20 visible job postings are in 深圳-南山区 | [Liepin employer page](https://m.liepin.com/company/13683985/) |
| Benefits listed | 弹性工作 (flexible hours), 领导好, 扁平管理 (flat management), 年底双薪, 绩效奖金, 股票期权 (stock options), 五险一金, 定期体检, 节日礼物, 年度旅游, 团队聚餐, 带薪年假; plus "公积金全额缴纳" (full housing-fund contribution) | [Liepin employer page](https://m.liepin.com/company/13683985/) |
| Published salary bands | RMB 15k–80k per month across the 20 visible postings, most on a 14-month structure and the two "专家/lead" hardware roles on 16 months | [Liepin employer page](https://m.liepin.com/company/13683985/) |
| Entry level | The visible postings ask for 3+ to 10+ years; two say "经验不限" and one simulation role accepts "1年以上" with a master's degree | [Liepin employer page](https://m.liepin.com/company/13683985/) |
| Working language | Job postings and the employer profile are in Chinese; product, documentation, developer platform and support surfaces are in English; one posting title is written in English ("Industrial Designer _Senior"). No language policy is published | [Liepin employer page](https://m.liepin.com/company/13683985/), [Even Hub docs](https://hub.evenrealities.com/docs) |
| Careers channel | No careers page exists on `evenrealities.com` — the page sitemap contains no `/careers` or `/jobs` entry; hiring runs through Liepin and other Chinese job boards | [pages sitemap](https://www.evenrealities.com/sitemap/pages/1.xml); read 2026-09-01 |

---

## Notes

### Not publicly disclosed

Searched on 2026-09-01 across `evenrealities.com` (robots.txt, all four sitemaps, product/tech/company/retail/terminal pages and product structured data), `evenrealities.cn`, `hub.evenrealities.com`, the Zendesk help centre and its API, the GitHub organisation and repositories, the npm registry, the Apple App Store search API, the Discord invite API, plus English and Chinese web search:

- **Revenue, ARR, margin or units sold since 2024.** The only unit figure anywhere is the G1's "10,000+ in roughly half a year" from 2024, repeated by TechCrunch as a target surpassed.
- **Amounts for every round before the 2026 pre-Series B.** Angel, Pre-A and A-round sizes are not published by the company or by any source reviewed.
- **The ownership relationships between the six named entities** (Hong Kong, Berlin, Delaware, Tokyo, Shenzhen "Even Realities Ltd", and 深圳市逸文科技有限公司). The legal documents list them as affiliates without stating structure.
- **Any company-published funding announcement.** `/press` returns a JavaScript interstitial to automated clients, and the news blog carries no financing post.
- **A careers page, or any salary band outside China.** Berlin is stated as a headquarters but no Berlin role was found in the sources reviewed.
- **An engineering blog or technical writing.** The blog is product, buyer-guide and press-repost content; the `even-insider` category is editorial rather than technical.
- **Any specification for EvenLLM** — model size, provider, whether inference is on-device, on the phone or in the cloud, or any benchmark.
- **A published SLA, security certification (SOC 2, ISO 27001) or penetration-test summary.** The company publishes a vulnerability disclosure policy and a PSTI statement, not certifications.
- **ICP filing for `evenrealities.cn`.** No filing string appears on the page; the site serves the English store, consistent with TechCrunch's report that the products are not sold in China.
- **Sources that could not be read on 2026-09-01:** CNBC (HTTP 403), Quartz (HTTP 403), `evenrealities.com/press` (bot interstitial), and the Shopify `products.json` and per-product `.js` endpoints (HTTP 404 — blocked; prices were taken from on-page structured data instead).

### Inconsistencies across sources

- **Even G2 display resolution, three numbers.** The specification table on the product page says **640×350**; the same page's `Product` structured data says **"640×400 (100% increase from Even G1)"**; the developer documentation and the `even-terminal` readme both describe the render target as **576×288** ([Even G2](https://www.evenrealities.com/smart-glasses), [Even G2 A JSON-LD](https://www.evenrealities.com/products/g2-a), [Even Hub docs](https://hub.evenrealities.com/docs), [`even-terminal`](https://registry.npmjs.org/@evenrealities%2Feven-terminal)). The site's own G1 figure is 640×200, which no more than doubles to 640×400 rather than 640×350.
- **CTO's Chinese name.** The company's Liepin page writes **欧阳剑**; Leiphone writes **欧阳健** ([Liepin employer page](https://m.liepin.com/company/13683985/), [Leiphone (language: zh)](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)).
- **Headcount.** "100-499人" (Liepin, 2026-09-01), "300 to 400 employees" (TechCrunch, 2026-07-06), "约100人" (Shenzhen municipal profile, 2025-07-13).
- **Funding stage on the company's own recruiting page** still reads "A轮" on 2026-09-01, two months after the pre-Series B was reported ([Liepin employer page](https://m.liepin.com/company/13683985/), [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)).
- **Even G1 price.** Launch coverage and the Shenzhen municipal profile give US$599; the product page's structured data on 2026-09-01 gives US$499 as the entry price ([Shenzhen DRC (language: zh)](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html), [Even G1 A](https://www.evenrealities.com/products/g1-a)).
- **Official website.** The company's Liepin page lists "公司官网：https://www.evenrealities.cn"; the storefront, legal documents and developer platform all use `evenrealities.com` ([Liepin employer page](https://m.liepin.com/company/13683985/)).
- **Passthrough figure.** Both the G1 and G2 specification tables state 98%; the technology page's lens claim describes "a high rate of light transmission" without a figure, while Chinese coverage of the G1 reported 99% ([Even G1](https://www.evenrealities.com/g1), [Sohu (language: zh)](https://www.sohu.com/a/812622589_120998866)).
- **Optics brand name.** The G1 page calls it "HAOS™ — Holistic Adaptive Optical System"; the current technology page calls it "Even HAO™ — Holistic Adaptive Optics" ([Even G1](https://www.evenrealities.com/g1), [Technology](https://www.evenrealities.com/tech)).
- **Round naming.** TechCrunch calls the July 2026 round a "pre-Series B"; the company's own materials reviewed do not name it at all.

### Other

- **The developer platform has measurable pull relative to the company's size.** 238,666 monthly npm downloads of the SDK and 207,762 of the CLI, 16,182 Discord members, 833 GitHub-org followers and 473 stars on the BLE demo app — against a hardware company of roughly 300–400 people whose flagship shipped in November 2025 ([npm API](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk), [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true), [GitHub API](https://api.github.com/orgs/even-realities)).
- **A third-party developer ecosystem exists on npm.** Packages published by people outside the company include `@even-toolkit/create-even-app`, `even-sim-recorder`, `even-demo-kit`, `@penta2himajin/even-deskless` and `even-terminal-pi` (a provider adapter for a different coding agent) ([npm search](https://registry.npmjs.org/-/v1/search?text=evenhub&size=20); read 2026-09-01).
- **Terminal Mode is a coding-agent product shipped by a glasses company.** It depends on Anthropic's `@anthropic-ai/claude-agent-sdk` and names Claude Code and Codex as providers; the site's testimonial wall is dated April–June 2026 and drawn from the Discord ([`even-terminal`](https://registry.npmjs.org/@evenrealities%2Feven-terminal), [Terminal](https://www.evenrealities.com/terminal)).
- **The camera-free choice is a stated product constraint, not an omission.** It appears in the FAQ, the developer documentation ("No camera, no speaker") and the CEO's framing in coverage ([Even G2](https://www.evenrealities.com/smart-glasses), [Even Hub docs](https://hub.evenrealities.com/docs), [TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/)).
- **Distribution is optical-retail-shaped rather than electronics-shaped**, with an optician-fitting service, a partner application form segmented by store type, and named eyewear retailers alongside Yodobashi and BIC CAMERA ([Retail](https://www.evenrealities.com/retail), [Partner with Us](https://www.evenrealities.com/partner-with-us)).
- **A Chinese company selling only abroad.** TechCrunch reports the products are "Not yet sold in China", with the US the fastest-growing market and Japan, South Korea, the Middle East and Europe also named; the site's locales cover German, Spanish, French, Italian, Japanese, Korean and Hong Kong Chinese, but not mainland China ([TechCrunch](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/), [evenrealities.com](https://www.evenrealities.com/)).
- **The founding team is a JMGO (坚果投影) alumni cluster.** The CEO, CDO and CTO are all described on the company's own recruiting page as having led product, design or R&D at 坚果投影 before founding Even Realities ([Liepin employer page](https://m.liepin.com/company/13683985/)).

---

## Resources

**Official**

- [evenrealities.com](https://www.evenrealities.com/) · [robots.txt](https://www.evenrealities.com/robots.txt) · [sitemap index](https://www.evenrealities.com/sitemap.xml) · [pages sitemap](https://www.evenrealities.com/sitemap/pages/1.xml) · [evenrealities.cn](https://www.evenrealities.cn/)
- Product — [Even G1](https://www.evenrealities.com/g1) · [Even G2](https://www.evenrealities.com/smart-glasses) · [Even R1](https://www.evenrealities.com/smart-ring) · [Technology](https://www.evenrealities.com/tech) · [Terminal](https://www.evenrealities.com/terminal) · [Store](https://www.evenrealities.com/store) · [Retail](https://www.evenrealities.com/retail) · [Enterprise purchase](https://www.evenrealities.com/enterprise-purchase) · [Partner with Us](https://www.evenrealities.com/partner-with-us)
- Product structured data — [Even G2 A](https://www.evenrealities.com/products/g2-a) · [Even G2 B](https://www.evenrealities.com/products/g2-b) · [Even G1 A](https://www.evenrealities.com/products/g1-a) · [Even R1](https://www.evenrealities.com/products/r1)
- Company — [Company](https://www.evenrealities.com/company) · [Blog](https://www.evenrealities.com/blog) · [News](https://www.evenrealities.com/blogs/news) · [Press reposts](https://www.evenrealities.com/blogs/press)
- Developer — [Even Hub](https://hub.evenrealities.com) · [Even Hub docs](https://hub.evenrealities.com/docs) · [GitHub `even-realities`](https://api.github.com/orgs/even-realities) · [EvenDemoApp](https://github.com/even-realities/EvenDemoApp) · [evenhub-templates](https://github.com/even-realities/evenhub-templates) · [npm `@evenrealities/even_hub_sdk`](https://registry.npmjs.org/@evenrealities/even_hub_sdk) · [npm `@evenrealities/even-terminal`](https://registry.npmjs.org/@evenrealities%2Feven-terminal) · [npm downloads](https://api.npmjs.org/downloads/point/last-month/@evenrealities/even_hub_sdk) · [npm search "evenhub"](https://registry.npmjs.org/-/v1/search?text=evenhub&size=20) · [Discord invite API](https://discord.com/api/v9/invites/GsuDkKDXDe?with_counts=true)
- Legal and compliance (Zendesk) — [Terms of Service](https://support.evenrealities.com/hc/en-us/articles/14290554040335-Terms-of-Service) (last updated 2026-07-28) · [Privacy Policy (Device & APP)](https://support.evenrealities.com/hc/en-us/articles/14270525749519-Privacy-Policy-Device-APP) (effective 2026-07-25) · [Data Storage and Cross-Border Transfers](https://support.evenrealities.com/hc/en-us/articles/15685480925583-Data-Storage-and-Cross-Border-Transfers) · [Vulnerability Disclosure Policy](https://support.evenrealities.com/hc/en-us/articles/15840567983887-Vulnerability-Disclosure-Policy) (effective 2026-04-17) · [UK PSTI Statement of Compliance](https://support.evenrealities.com/hc/en-us/articles/14519551777295-UK-PSTI-Statement-of-Compliance) · [Even Hub Developer Platform Terms of Service](https://support.evenrealities.com/hc/en-us/articles/15606676690703-Even-Hub-Developer-Platform-Terms-of-Service) (last updated 2026-03-24) · [Even Hub Developer Platform Data Processing Agreement](https://support.evenrealities.com/hc/en-us/articles/15606721200911-Even-Hub-Developer-Platform-Data-Processing-Agreement) · [Privacy & Legal category index](https://support.evenrealities.com/hc/en-us/categories/13501923846159-Privacy-Legal) · [Help-centre article API](https://support.evenrealities.com/api/v2/help_center/en-us/articles.json)
- Hiring (language: zh) — [Liepin employer page](https://m.liepin.com/company/13683985/)

**Registry and platform records**

- [Baidu Baike — 深圳市逸文科技有限公司 (language: zh)](https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%80%B8%E6%96%87%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/65221335)
- [iTunes search API — publisher "Even Realities Ltd."](https://itunes.apple.com/search?term=even%20realities&entity=software&country=us&limit=10)

**Third-party coverage**

- [TechCrunch — Smart glasses maker Even Realities hits $1B valuation with $150M funding led by Meituan, Tencent](https://techcrunch.com/2026/07/06/smart-glasses-maker-even-realities-hits-1b-valuation-with-150m-funding-led-by-meituan-tencent/) — 2026-07-06
- [Shenzhen Development and Reform Commission — 逸文科技创始人王骁逸：怎么把 599 美元的智能眼镜卖给 CEO 们 (language: zh)](https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/mqfc/myqyjdxsj/content/post_12331103.html) — 2025-07-13
- [Leiphone — 逸文科技，为何受资本争抢？ (language: zh)](https://m.leiphone.com/category/weiwu/pHewD8yVOSugr5Sc.html)
- [Sohu — 比肩"AR四小龙"？深圳这家AR企业有望一年完成三轮融资 (language: zh)](https://www.sohu.com/a/812622589_120998866) — 2024-09
- [Tencent News — 深圳AR眼镜公司Even Realities发生工商变更，新增股东 (language: zh)](https://news.qq.com/rain/a/20240812A06XK100) — 2024-08-12
