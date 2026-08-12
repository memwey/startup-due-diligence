# Evoto

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-12.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Evoto is desktop, tablet, mobile and web software for professional photographers — RAW editing, AI culling, portrait retouching, colour grading, tethered shooting and event galleries — sold on a credit-per-exported-photo model. The site presents the operator as `Truesight Technology Inc.`, a Delaware company at "OFFICE NO. 1215 1000 N. WEST STREET, SUITE 1200, WILMINGTON, DELAWARE 19801, USA", alongside `TRUESIGHT PTE.LTD.` (Singapore), `株式会社Truesight Japan` and `Truesight Korea Limited` ([about](https://www.evoto.ai/about); Undated; accessed 2026-08-12). The Terms of Use, however, are still written for `TRUESIGHT PTE. LTD.` under Singapore law ([Terms of Use](https://res.evoto.ai/ui/www/policy/terms.html); Updated 2024-03-22) — see `Identity and legal entities`.

- Scale is company-stated: "200+ Countries & Regions", "1M+ Professional Photographers", "50k+ Photography Studios", "800M+ Photos Processed", qualified on the same page as "based on internal account and usage data reviewed as of 2026" ([about](https://www.evoto.ai/about); accessed 2026-08-12). Independently observable distribution is smaller: Google Play shows "100K+" downloads and 4.7 from 1.46K reviews ([Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto); accessed 2026-08-12), and the iOS app has 2,301 ratings averaging 4.91 ([iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us); accessed 2026-08-12).
- No funding round has been announced by the company in the reviewed public sources as of 2026-08-12. [Tracxn](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) states "Evoto has not raised any funding rounds yet"; [Latka](https://getlatka.com/companies/evoto.ai) states US$0 raised, "bootstrapped", with an estimated US$4.1M 2025 revenue and about 37 employees in 2026 — see `Funding`.
- Pricing is credit-metered: editing is free and exporting consumes credits at roughly one credit per photo, with annual plans from US$80/year for 800 credits (US$0.10/credit) to US$1,205/year for 24,000 credits (US$0.05/credit), and pay-as-you-go credits expiring after two years ([payment](https://www.evoto.ai/payment); accessed 2026-08-12).
- In January 2026 the company published an "Online AI Headshot Generator" page marketed as "Save money vs. studio sessions" ([archived 2026-01-10](https://web.archive.org/web/20260110205938/https://www.evoto.ai/features/ai-headshot-generator)), withdrew it after customer and ambassador criticism, and stated "We missed the mark, and we are sorry" ([Digital Camera World, 2026-01-21](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash)). The URL now redirects to `/404` (checked 2026-08-12).
- Engineering evidence comes from public assets, not a stack page: the marketing site is Nuxt behind CloudFront with S3 origins, the desktop build is a ~2.0 GB NSIS installer EV-code-signed to "Truesight Technology Inc." (Delaware) via GlobalSign, the blog is WordPress behind Cloudflare, support runs on GitBook, and the privacy policy names AWS as the cloud provider for user-uploaded data with the "primary location for processing your personal information" being the United States (response headers and installer inspected 2026-08-12; [Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html); Last Updated 2025-06-20).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | Evoto (product family: Evoto Desktop, Evoto iPad, Evoto Mobile, Evoto Instant, Evoto Video, Evoto Online) | [homepage](https://www.evoto.ai/), [download](https://www.evoto.ai/download), [payment](https://www.evoto.ai/payment); accessed 2026-08-12 |
| Entity named in the site footer | "©️2026 Truesight Technology Inc. \| OFFICE NO. 1215 1000 N. West Street, Suite 1200, Wilmington, Delaware 19801, USA" | [download page footer](https://www.evoto.ai/download); accessed 2026-08-12 |
| Entity named in the Terms of Use | "TRUESIGHT PTE. LTD. (“TRUESIGHT”)"; governed by "the laws of Singapore" with "exclusive jurisdiction of the courts of Singapore" | [Terms of Use](https://res.evoto.ai/ui/www/policy/terms.html); Updated 2024-03-22 |
| Entity named in the Refund Policy | "Truesight PTE. LTD." | [Refund Policy](https://res.evoto.ai/ui/www/policy/refund.html); Undated; accessed 2026-08-12 |
| Stated founding | "Founded in 2020"; "In 2020, after sitting down with hundreds of working photographers" | [about](https://www.evoto.ai/about), [company](https://www.evoto.ai/company); Undated; accessed 2026-08-12 |
| Singapore registration | TRUESIGHT PTE. LTD., UEN 202224238M, incorporated 2022-07-13, private company limited by shares, 3 Fraser Street #04-23A DUO Tower 189352 | [companies.sg](https://www.companies.sg/business/202224238M/TRUESIGHT-PTE-LTD-) (ACRA data mirror); accessed 2026-08-12 — see `Notes` |
| Japan registration | 株式会社Truesight Japan, corporate number 5020001152305, 東京都渋谷区渋谷2-24-12 渋谷スクランブルスクエア37階 | [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305) (record updated 2025-12-05) |
| Japan entity details | 設立 2023年6月、資本金 1000万円、代表取締役 Mitta Zhang（PR TIMES 会社概要 代表者名：張偉）、電話 050-1780-9810、未上場 | [PR TIMES release and company profile](https://prtimes.jp/main/html/rd/p/000000016.000132859.html); Published 2025-12-05 |
| Korea entity | Truesight Korea Limited, Room 6080, Seongil Building, Nonhyeon-dong 584, Gangnam-daero, Gangnam-gu, Seoul | [about](https://www.evoto.ai/about); Undated; accessed 2026-08-12 |
| Code-signing certificate on the Windows build | Subject "Truesight Technology Inc.", state "Delaware", locality "Newark"; issued under "GlobalSign GCC R45 EV CodeSigning CA 2020" with Sectigo timestamping | certificate strings read from [`Evoto_Setup_7.3.0-512.exe`](https://res.evoto.ai/package/7.3.0-512/Evoto_Setup_7.3.0-512.exe) on 2026-08-12 |
| Named leadership | "Mitta — CEO & Founder"; "Mitta Zhang, CEO at Evoto" | [about](https://www.evoto.ai/about), [PR Newswire, 2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html) |
| Headcount | Not published by the company; third-party figures range from 4 to 500 — see `Notes` | see `Notes` |
| Stated team footprint | "Our team spans 6 countries"; "photographers, engineers, designers, and product people" | [about](https://www.evoto.ai/about); Undated; accessed 2026-08-12 |
| Public contacts | `support@evoto.ai` (US/Singapore/Korea), `support-jp@evoto.ai` (Japan), `contactus@evoto.ai` (privacy and refunds), `developer@evoto.ai` and +65 8743 2041 (Google Play developer block) | [about](https://www.evoto.ai/about), [Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html), [Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto) |
| Social and community | Facebook `evotoai`, Instagram `evotoai`, X `Evotoofficial`, TikTok `evotoaitk`, YouTube `EvotoChannel`, LinkedIn `evoto-ai`, Reddit `r/EvotoAI`, forum at `forum.evoto.ai` | [homepage footer](https://www.evoto.ai/); accessed 2026-08-12 |
| Website locales | English plus `vi`, `ko`, `ja`, `de`, `fr`, `es`, `it`, `pt`, `es_Es`, `zh-Hant`, `pl`, `ar`, `tr`, `th`; no Simplified Chinese locale | [sitemap index](https://www.evoto.ai/sitemap_index.xml), [robots.txt](https://www.evoto.ai/robots.txt); accessed 2026-08-12 |
| Certifications displayed | ISO/IEC 27001 and SOC 2 Type 2 badges (no certificate number, scope or auditor given) | [about](https://www.evoto.ai/about), [download](https://www.evoto.ai/download); accessed 2026-08-12 |
| Japan privacy certification | プライバシーマーク 第17004988(01)号, valid 2025-01-07 to 2027-01-06, awarded by 一般社団法人日本情報システム・ユーザー協会, granted 2025-01-07 | [PR TIMES, 2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html) |
| iOS app | `com.truesight.evoto`, "Evoto-AI Photo Editor&Retouch", seller TRUESIGHT PTE. LTD., first released 2024-11-01, version 3.1.3 on 2026-08-11, 801,347,584 bytes, min iOS 15.0, 13 languages, 2,301 ratings averaging 4.91 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us); accessed 2026-08-12 |
| Android app | `com.truesight.evoto`, developer TRUESIGHT PTE. LTD., "100K+" downloads, 4.7 from 1.46K reviews, updated 2026-07-30, in-app purchases; developer block gives 3 Fraser Street, Singapore 189352 | [Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto); accessed 2026-08-12 |
| Evoto Instant iOS app | `ai.evoto.instant.capture`, first released 2025-09-10, version 1.8.1 on 2026-08-07, 12 ratings averaging 4.33 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749685404&country=us); accessed 2026-08-12 |
| Desktop builds | Stable 7.3.0-512 with "Update Time: 2026-08-06"; Windows installer 2,032,789,104 bytes (`last-modified` 2026-08-07), macOS arm64 disk image 1,903,599,556 bytes (`last-modified` 2026-08-07); separate Intel and arm64 macOS builds; a 7.3.5-76 build set is also published | [download](https://www.evoto.ai/download) and response headers observed 2026-08-12 |
| Supported desktop OS | macOS "10.13 and above"; "Win7/Win10/Win11" | [download](https://www.evoto.ai/download); accessed 2026-08-12 |

**Events, awards and partners.** The company exhibits at photography trade shows: CP+ 2024 and CP+ 2025 in Japan ([PR TIMES, 2024-02-19](https://prtimes.jp/main/html/rd/p/000000001.000132859.html), [PR TIMES, 2025-02-20](https://prtimes.jp/main/html/rd/p/000000014.000132859.html)), ブライダル産業フェア and PHOTONEXT in 2024 ([PR TIMES, 2024-04-30](https://prtimes.jp/main/html/rd/p/000000003.000132859.html), [PR TIMES, 2024-05-31](https://prtimes.jp/main/html/rd/p/000000004.000132859.html)), the "Evoto One" brand event in New York in September 2025 ([PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)), and Imaging USA 2026 in Nashville at booth #547 ([PR Newswire, 2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)); the homepage also lists NAB, MPN FOTOVAKB and TexasSchool ([homepage](https://www.evoto.ai/); accessed 2026-08-12). In Japan, `株式会社Truesight Japan` signed a distribution agreement with `株式会社ラボネットワーク` announced 2024-12-27 ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000132859.html), [Labo Network](https://www.labonetwork.co.jp/news/24122701/)). The company announced inclusion in "Capterra's 2026 Best Ease of Use rankings for both the Artificial Intelligence and Photo Editing categories", describing it as "category-level visibility in buyer-facing ranking views" rather than "independent lab benchmarking" ([blog, 2026-03-27](https://blog.evoto.ai/evoto-capterra-2026-press-release/)).

### Identity and legal entities

| Name | Type | Jurisdiction indicated | Relationship as stated | Source |
|---|---|---|---|---|
| Evoto | Public brand | — | Name used on the site, apps, store listings, blog, support and forum | [homepage](https://www.evoto.ai/) |
| Truesight Technology Inc. | Legal entity named in the site footer, the `about` page "United States" block and the Windows code-signing certificate | Delaware, United States | Presented as the company behind Evoto; `llms.txt` calls Evoto "software developed by TRUESIGHT TECHNOLOGY INC., a computer software company headquartered in the United States" | [about](https://www.evoto.ai/about), [llms.txt](https://www.evoto.ai/llms.txt) |
| TRUESIGHT PTE.LTD. | Legal entity named in the Terms of Use, Refund Policy, both app-store seller records, and the `about` page "Singapore Branch" block | Singapore (UEN 202224238M per ACRA mirrors) | Contracting party in the Terms; app-store seller of record | [Terms of Use](https://res.evoto.ai/ui/www/policy/terms.html), [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us) |
| 株式会社Truesight Japan | Legal entity, corporate number 5020001152305 | Japan (Tokyo) | Described in its own releases as the 日本法人 of, first, "シンガポールのIT企業 TRUESIGHT PTE.LTD." (2025-01) and later "米国のIT企業 Truesight Technology Inc." (2025-12) | [PR TIMES, 2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html), [PR TIMES, 2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) |
| Truesight Korea Limited | Legal entity named in the `about` page "Korea Branch" block | Korea (Seoul) | Listed as a contact office; no registry record retrieved | [about](https://www.evoto.ai/about) |

The `about` page labels Singapore, Japan and Korea as "Branch", while Singapore's ACRA-derived record shows a separately incorporated private company and Japan's is a separately registered 株式会社. No reviewed source states the ownership relationship between the four entities, and no consolidated corporate filing was found — see `Notes`.

The company-maintained LinkedIn page is written around the Singapore entity: "TRUESIGHT PTE.LTD., established in 2020 in Singapore by a team of experienced AI researchers and graphic engineers, is a leading provider of AI-powered SaaS software solutions. Over the past three years, we have excelled in developing and hosting innovative softwares that empower professional creators and designers." The same page gives Headquarters "Wilmington, Delaware", Founded "2020", Industry "Technology, Information and Internet" and Company size "501-1,000 employees", and lists 47 employee profiles ([LinkedIn](https://www.linkedin.com/company/evoto-ai); Undated; accessed 2026-08-12).

---

## Product

The homepage headline is "Tether. Cull. Retouch. Deliver. The Ultimate End-To-End Photography Workflow" ([homepage](https://www.evoto.ai/); accessed 2026-08-12). The company describes the product as "an image organization and artificial intelligence (AI) SaaS image processing software … offer[ing] photo editing solutions including portrait retouching, AI color grading, background removal, AI skin retouching, blemish removal, body sculpting, clothing wrinkle removal, and tethered shooting for photographers, creators, and commercial business owners" ([llms.txt](https://www.evoto.ai/llms.txt); accessed 2026-08-12).

### Surfaces

| Surface | Platforms | What it is | Source |
|---|---|---|---|
| Evoto Desktop | macOS 10.13+, Windows 7/10/11 | The main application: RAW processing, AI culling, portrait retouching, colour grading, background editing, batch editing, tethered shooting | [download](https://www.evoto.ai/download), [release notes](https://www.evoto.ai/release-notes) |
| Evoto iPad | iPadOS | Tablet version; a company spokesperson described it as offering "80–90% parity with desktop features" | [PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/) |
| Evoto Mobile | iOS, Android | Phone app with retouching, colour, RAW and tethered shooting; supports "Canon, Sony, Nikon, Fujifilm, Leica, Panasonic, and more" | [App Store description](https://apps.apple.com/us/app/evoto-ai-photo-editor-retouch/id6596737043), [PR TIMES, 2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) |
| Evoto Instant | `instant.evoto.ai`, iOS app `ai.evoto.instant.capture`, plus an `EIPrinter` Windows companion | Real-time event photo gallery: "Shoot, Cull, Edit, Proof, Share in an Instant", with gallery and photo branding, client picks, notes and slideshow; new users offered "12 GB" storage | [instant.evoto.ai](https://instant.evoto.ai/); accessed 2026-08-12 |
| Evoto Video | macOS, Windows | "Professional-grade AI color grading and retouching for video creators", with AI Color Match and "Ultra-precise 4K" video retouch | [video.evoto.ai](https://video.evoto.ai/); accessed 2026-08-12 |
| Evoto Online | Browser | Web trial surface exposing individual features ("Online Trial") from the feature landing pages | [payment](https://www.evoto.ai/payment) plan table, feature pages; accessed 2026-08-12 |
| Academy, Webinars, Blog, Support, Forum | Web | `academy.evoto.ai` (Next.js), `evoto.ai/webinar` (recorded sessions hosted by named photographers), `blog.evoto.ai` (WordPress, 711 posts), `support.evoto.ai` (GitBook), `forum.evoto.ai` | response headers and [WordPress REST API](https://blog.evoto.ai/wp-json/wp/v2/posts?per_page=1) observed 2026-08-12 |

### Release history

The published release notes list 28 desktop versions from V1.5.0 on 2023-05-17 to V7.3.0 on 2026-07-10 ([release notes](https://www.evoto.ai/release-notes); accessed 2026-08-12). Selected entries:

| Version | Date | Headline features as listed |
|---|---|---|
| V1.5.0 | 2023-05-17 | "Lens Corrections", "Color Grading", "New Makeup Presets & Contacts" |
| V4.1.0 | 2024-12-26 | AI colour matching ("AIカラーマッチ" in the Japanese announcement) |
| V5.0.0 | 2025-06-23 | "Library", "Dehaze", "Unify Lighting", "Double Eyelids" |
| V6.0.0 | 2025-09-16 | "AI Culling", "Spill Removal", "AI Exposure and White Balance Adjustment", "Tethered Shooting" |
| V6.1.0 | 2025-11-05 | "Cloud Collaboration Now Available", "AI-Powered Multi-Image Color Consistency", "AI Denoise" |
| V6.2.0 | 2026-01-30 | "New Pet Retouching Module", "Pet Masks", "Photo Cluster", "Stretch Marks Removal" |
| V7.0.5 | 2026-03-31 | "Your AI Looks", "AI Lab", "Smarter Mask Tools", "Perfect Shot" |
| V7.1.5 | 2026-04-29 | "Our AI Commitment", "AI Background Fusion", "Floor Reflection", "AI Body Complexion" |
| V7.3.0 | 2026-07-10 | "Batch AI Set Design", "Matte Refinement", "Strong Glare Removal", "Glow Effect" |

### Commercialization

Download and account creation are free; exporting an edited photo consumes credits, "From 1 credit per photo" ([payment](https://www.evoto.ai/payment); accessed 2026-08-12). Prices below are the US dollar figures returned for the payment page on 2026-08-12; the page localizes by region and returned Japanese yen when fetched from a Tokyo egress.

| Item | Detail | Source |
|---|---|---|
| Annual plans | Starter 800 credits US$80/year (list US$89, "Estimated monthly US$6.99", 2 devices); Basic 1,600 US$134 (US$149, 3 devices); Basic Plus 3,600 US$242 (US$269, 4 devices); Standard 9,000 US$521 (US$579, 5 devices); Standard Plus 24,000 US$1,205 (US$1,339, 6 devices) | [payment](https://www.evoto.ai/payment); accessed 2026-08-12 |
| Effective credit price | US$0.10, US$0.08, US$0.07, US$0.06 and US$0.05 per credit by tier | [payment](https://www.evoto.ai/payment) |
| Pay-as-you-go | Credit packages purchased as needed; "The credit you have purchased will expire after 2 years"; a February 2026 review put entry pricing at "$49 for 200 credits" and about US$0.25 per image | [payment FAQ](https://www.evoto.ai/payment), [Digital Camera World, 2026-02-13](https://www.digitalcameraworld.com/tech/software/evoto-ai-review) |
| Add-on packages | 200 to 24,000 extra credits, priced by subscription tier (for example 200 credits at US$22 down to US$11) | [payment](https://www.evoto.ai/payment) |
| Cloud storage packs | 500 GB US$119, 1 TB US$189, 2 TB US$269, same price at every tier | [payment](https://www.evoto.ai/payment) |
| Free trial and starter credits | "one 7-day free trial per account", "Try full features with 50 free credits"; the download page offers "15 Credits" on download | [payment](https://www.evoto.ai/payment), [download](https://www.evoto.ai/download) |
| Rollover | Unused credits roll over on renewal "up to a maximum of 5 times the credit of your new subscription package"; 30-day grace period | [payment FAQ](https://www.evoto.ai/payment) |
| Credit-free features | Basic colour adjustments, crop and rotate, tethered shooting and manual tools export without consuming credits from desktop v6.1 onward; iPad, Instant and v6.0-or-earlier desktop excluded | [payment](https://www.evoto.ai/payment), [PR TIMES, 2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html) |
| Payment methods | "Credit cards and Paypal are currently the forms of acceptable payment for your Subscription" | [Terms of Use](https://res.evoto.ai/ui/www/policy/terms.html); Updated 2024-03-22 |
| Refunds | Refundable "only if your subscription order is within the 14-day cancellation period and you have not utilized the services under this specific order"; otherwise "All fees paid are non-refundable"; processing up to 10 business days | [Refund Policy](https://res.evoto.ai/ui/www/policy/refund.html) |
| Loyalty and referral | "Evoto Smart Points" earned on purchases, referrals and engagement, redeemable for credits and cloud storage, with "A single points system throughout your workflow — Photo Editor, Cloud, Instant, mobile, and desktop"; a separate referral programme page exists | [loyalty](https://www.evoto.ai/loyalty), [referral](https://www.evoto.ai/referral); accessed 2026-08-12 |
| Enterprise | The payment page has an "Enterprise" tab and the footer a "Contact Sales" link; no enterprise price list was found | [payment](https://www.evoto.ai/payment); accessed 2026-08-12 |
| Japan distribution | Sales and support in Japan run through `株式会社Truesight Japan`, with a distribution agreement with `株式会社ラボネットワーク` announced 2024-12-27 | [PR TIMES, 2024-12-27](https://prtimes.jp/main/html/rd/p/000000011.000132859.html) |

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2022-11-23 | Marketing site already live as "EVOTO, AI-powered Image Editor", promising "thousands of photos processed with 10x speed" | [Wayback capture](https://web.archive.org/web/20221123171058/https://evoto.ai/) |
| 2023-05-17 | Earliest desktop version listed in the public release notes (V1.5.0) | [release notes](https://www.evoto.ai/release-notes) |
| 2024-11-01 | iOS app first released | [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us) |
| 2025-09-23 | "a team of 500 employees serving millions of users across 158 countries"; headquarters given as Menlo Park, California; founding given as 2022 | [PetaPixel](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/) |
| 2026-01-11 | Product claims at Imaging USA: "65%" of time reclaimed from fragmented workflows, AI Culling processing "5,000 photos in under 10 minutes", "15x faster" AI Object Removal, "30% increase in studio upsell rates" | [PR Newswire](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html) |
| 2026-03-27 | Included in "Capterra's 2026 Best Ease of Use rankings" for Artificial Intelligence and Photo Editing | [blog](https://blog.evoto.ai/evoto-capterra-2026-press-release/) |
| 2025 (estimate) | US$4.1M revenue, "latest figure estimated"; US$0 raised; about 37 employees in 2026 | [Latka](https://getlatka.com/companies/evoto.ai); accessed 2026-08-12 |
| Accessed 2026-08-12 | Company-stated "1M+ Professional Photographers", "200+ Countries & Regions", "50k+ Photography Studios", "800M+ Photos Processed" | [about](https://www.evoto.ai/about) |
| Accessed 2026-08-12 | Google Play "100K+" downloads, 4.7 from 1.46K reviews; App Store 2,301 ratings averaging 4.91; Evoto Instant 12 ratings | [Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto), [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us) |

No customer count, revenue, paid-seat, credit-consumption or retention figure is published by the company — see `Notes`.

### The AI Headshot Generator page and its withdrawal (January 2026)

| Date | Event | Source |
|---|---|---|
| 2026-01-10 | A page at `www.evoto.ai/features/ai-headshot-generator` is captured by the Internet Archive. It offers to "Turn selfies into professional headshots fast for free", promises "2K or 4K, watermark-free headshots with 5 free styles", and markets it as "Skip the hassle of bookings and edits", "saving time vs. traditional photoshoots" and "Save money vs. studio sessions. Fit budgets for individuals, teams, and industries" | [archived page](https://web.archive.org/web/20260110205938/https://www.evoto.ai/features/ai-headshot-generator) |
| 2026-01-12 | First company response: the tool "moved into a phase of visibility beyond our intended roadmap" | [PetaPixel, 2026-01-15](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/) |
| 2026-01-14 | Trade coverage of the response continues | [The Phoblographer](https://www.thephoblographer.com/2026/01/14/evoto-ai-headshot-generator-anti-photographer/) |
| 2026-01-15 | PetaPixel reports the backlash; photographer and Evoto ambassador Sal Cincotta is quoted saying "Evoto is trying to hurt the very people that I'm trying to help" | [PetaPixel](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/) |
| 2026-01-16 | Follow-up statement describing the page as "intended as a secondary page focused on SEO" | [PetaPixel](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/) |
| 2026-01-21 | Company statement reported: "We missed the mark, and we are sorry"; "We realize that by testing a tool that generates images from scratch, we crossed a line. Evoto was built to handle the heavy lifting of retouching – not a tool that replaces the person behind the lens"; and "We do not use your images or your clients' images to train our AI models (…) We source our data exclusively through commercially licensed and purchased imagery". The generator is described as permanently removed | [Digital Camera World](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash) |
| 2026-02-13 | A product review lists "Questions raised by 'headshotgate' controversy" among its cons | [Digital Camera World review](https://www.digitalcameraworld.com/tech/software/evoto-ai-review) |
| 2026-04-29 | Desktop V7.1.5 ships a release-note item titled "Our AI Commitment": "Evoto does not use your images or data to train generative AI models without your explicit permission." | [release notes](https://www.evoto.ai/release-notes) |
| Checked 2026-08-12 | `www.evoto.ai/features/ai-headshot-generator` returns HTTP 302 to `/404` | request observed 2026-08-12 |

### Stated plans

The company's stated direction is workflow coverage end to end: "Our customers would love to use Evoto for their entire workflow, from capture to delivery. That's the direction we're heading" ([Jay Peterson, U.S. spokesperson, PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)). The January 2026 release frames the combination of Evoto Mobile, Desktop 6.2 and Instant 1.4 as "the industry's first true All-in-One workflow" and quotes the CEO: "We aren't just building tools; we are building a time machine for the modern photographer" ([PR Newswire, 2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)).

---

## Founder

**Mitta** — "CEO & Founder". The `about` page quotes: "At Evoto, we believe AI should handle the pixels, so photographers can focus on the soul. Our mission is to bridge the gap between technical complexity and creative intent—giving you back the time to do what only a human can: capture emotion and tell a story." No surname, career history, education or prior company appears on any Evoto page ([about](https://www.evoto.ai/about); Undated; accessed 2026-08-12).

The fuller name appears in company distributions rather than on the site. The Imaging USA release attributes a quote to "Mitta Zhang, CEO at Evoto" ([PR Newswire, 2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)). Japanese releases name "代表取締役：Mitta Zhang" for `株式会社Truesight Japan`, while the PR TIMES company profile block on the same pages gives 代表者名 as 張偉 ([PR TIMES, 2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)).

A Japanese startup database instead lists the Japan entity's representative as 代表取締役社長 ウィリアム・ワン, with an MBA from Kyushu University, a prior role as Asia marketing head at Fujitsu Semiconductor and earlier work at Chinese startups ([スタクラ](https://startupclass.co.jp/online/companies/1846/); Undated; accessed 2026-08-12). The two accounts of who represents the Japanese entity are not reconciled by any reviewed source — see `Notes`.

**Jay Peterson** is identified as Evoto's "U.S. Spokesperson" in the September 2025 interview that carries most of the company's public product and scale statements ([PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)).

No team, leadership or investors page exists on `evoto.ai`; the `about` page names only "Mitta", and the blog posts carry no engineering or executive bylines ([about](https://www.evoto.ai/about), [blog](https://blog.evoto.ai/); accessed 2026-08-12).

---

## Funding

No financing announcement by the company was found for the Evoto brand or any Truesight entity in the reviewed public sources as of 2026-08-12: there is no press page, investor page or funding statement on `evoto.ai`, and no financing announcement appears among the 20 releases listed in its Japanese PR TIMES feed. The table records what third-party sources state.

| Date | Round (as named in the source) | Amount | Investors | Source |
|---|---|---|---|---|
| Accessed 2026-08-12 (page dated "Last updated August 3, 2026") | None — "Evoto has not raised any funding rounds yet"; described as an "unfunded company", founded 2024, headquartered in Singapore | None | None listed | [Tracxn](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) |
| Accessed 2026-08-12 | None — US$0 raised, "bootstrapped", "no venture capital or outside funding"; 2025 revenue "estimated" at US$4.1M; about 37 employees in 2026; founded 2020 | None | None listed | [Latka](https://getlatka.com/companies/evoto.ai) |
| Accessed 2026-08-12 | Not established | — | — | PitchBook publishes profiles for [Truesight (China)](https://pitchbook.com/profiles/company/503403-85) ("developer of AI-powered image processing software intended for commercial photography and consumer electronics", per the search-result description) and [TrueSight Technology](https://pitchbook.com/profiles/company/437673-34); neither page was readable without a subscription and neither was confirmed to describe this company — see `Notes` |

Neither database figure was confirmed against a primary source, and the two disagree with the company's own founding year and headquarters statements. Ownership, valuation, cap table and the relationship between the four Truesight entities are not established by any source reviewed.

---

## Engineering

### Technology stack and platforms

No stack page is published. Items below are confirmed by observable public assets or first-party documents unless labelled otherwise (all observed 2026-08-12).

- **Marketing site:** Nuxt (`x-powered-by: Nuxt`) served through Amazon CloudFront (`dpqccnyr1royh.cloudfront.net`), with static assets and application packages on Amazon S3 at `res.evoto.ai` (`server: AmazonS3`, `x-amz-server-side-encryption: AES256`). `api.evoto.ai` resolves to the same distribution and returns HTTP 404 at the root.
- **Machine-readable site surface:** the site publishes `robots.txt` with the header `Content-Signal: ai-train=yes, search=yes, ai-input=yes`, an `llms.txt`, an `llms-full.txt` indexing 140 pages, and a Markdown twin for every page (`/about.md`, `/payment.md`, …), of which 126 are feature landing pages ([robots.txt](https://www.evoto.ai/robots.txt), [llms.txt](https://www.evoto.ai/llms.txt)).
- **Other web properties:** `academy.evoto.ai` runs Next.js behind CloudFront; `blog.evoto.ai` is WordPress behind Cloudflare with 711 published posts (`x-wp-total: 711`); `support.evoto.ai` is behind Cloudflare and `help.evoto.ai` redirects to GitBook (`app.gitbook.com`); `forum.evoto.ai` serves a site titled "Evoto"; `community.evoto.ai` returned HTTP 503 from a Google frontend.
- **Desktop application:** NSIS-built Windows installer (`Nullsoft`/`NSIS` markers in the binary), 2,032,789,104 bytes for 7.3.0-512, EV code-signed with subject "Truesight Technology Inc." (Delaware, Newark) under "GlobalSign GCC R45 EV CodeSigning CA 2020" and timestamped by Sectigo; macOS shipped as separate Intel and arm64 disk images of about 1.9 GB. A separate `EvotoInstaller` downloader (beta and stable variants) and an `EIPrinter` Windows companion for Evoto Instant (19,235,781 bytes, `last-modified` 2026-04-24) are published from the same S3 bucket.
- **Mobile:** iOS build requires iOS 15.0 or later, is 801,347,584 bytes, and ships 13 language codes; the Android app is distributed through Google Play with in-app purchases ([iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us), [Google Play](https://play.google.com/store/apps/details?id=com.truesight.evoto)).
- **Cloud processing (first-party statement):** "Data Sharing Recipient: AWS (third-party cloud service provider), for the purpose of: To enable cloud-based analysis, processing, transmission, and storage of user-uploaded data"; "Our primary location for processing your personal information is United States" ([Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html); Last Updated 2025-06-20).
- **Analytics, attribution and third-party services (first-party statement plus observed page assets):** Mixpanel and Google for product analytics; Facebook, TikTok and ShareASale for advertising attribution; Infobip for phone-number identity verification ([Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html)). The homepage additionally loads Google Tag Manager, Facebook Connect, Twitter ads, Naver and Yahoo! JAPAN tags and `dwin1.com` (Awin), and sets a `user_id_statsig` cookie indicating Statsig ([homepage](https://www.evoto.ai/) assets and response headers; observed 2026-08-12).
- **Camera integration:** wired and wireless tethered shooting with "Canon, Sony, Nikon, Fujifilm, Leica, Panasonic, and more" ([App Store description](https://apps.apple.com/us/app/evoto-ai-photo-editor-retouch/id6596737043)).
- **No public code:** no GitHub organisation under `evoto`, `evotoai`, `truesight` or `truesight-technology`; no `evoto` npm package or scope; no PyPI package named `evoto` (API checks 2026-08-12).

### Systems

| System | What it does | Source |
|---|---|---|
| Credit metering and export licensing | Editing is free; export consumes credits, with per-feature credit-free exceptions from desktop v6.1, rollover to 5× the plan's credits and a 30-day grace period | [payment](https://www.evoto.ai/payment), [PR TIMES, 2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html) |
| Cross-product account and entitlement sharing | One account across desktop, iPad and phone; "purchased tickets" (credits) are usable across platforms, though the credit packages sold on the website and in the iPhone app differ | [PR TIMES, 2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) |
| Cloud storage and collaboration | "Cloud Collaboration" shipped in desktop V6.1.0 (2025-11-05); cloud storage sold as 500 GB / 1 TB / 2 TB packs; Instant offers a 12 GB bundle | [release notes](https://www.evoto.ai/release-notes), [payment](https://www.evoto.ai/payment), [instant.evoto.ai](https://instant.evoto.ai/) |
| Event gallery pipeline | Instant covers live capture, culling, editing, proofing and sharing, with gallery branding, client picks and favourites, client notes and auto-play slideshows, plus a Windows printing companion | [instant.evoto.ai](https://instant.evoto.ai/), `EIPrinter` package on `res.evoto.ai` |
| Tethered capture | Wired and wireless tethering across multiple camera vendors, added to desktop in V6.0.0 (2025-09-16) and available on iPad and phone | [release notes](https://www.evoto.ai/release-notes), [PR TIMES, 2024-12-16](https://prtimes.jp/main/html/rd/p/000000009.000132859.html) |
| AI culling | Automatic selection over large shoots; the company states "5,000 photos in under 10 minutes", with "Face Focus Mode" and "Capture Time Grouping" | [PR Newswire, 2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html) |
| Colour transfer | "AI Color Match" transfers colour from a reference image across stills and video without LUTs or masks; multi-image colour consistency added in V6.1.0 | [video.evoto.ai](https://video.evoto.ai/), [release notes](https://www.evoto.ai/release-notes) |
| Cloud content moderation | "Cloud content may be automatically scanned to ensure we do not host illegal or abusive content, such as child sexual abuse material"; public and shared cloud content "is subject to review for intellectual property issues and safety concerns" | [Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html) |
| Loyalty points ledger | "Evoto Smart Points" balance shared across Photo Editor, Cloud, Instant, mobile and desktop, redeemable for credits and storage | [loyalty](https://www.evoto.ai/loyalty) |

### Data handling as documented

The Privacy Policy states that "When the internal functions of the Software are insufficient to provide you services in full, we may upload your content to our web server for further processing", that such content "will be stored on our web server to make it more convenient for your future editing", and that "Based on the need to improve our products and services, we may collect the content you upload in certain scenarios, and you agree to give us full authorization to engage in this behavior. If you do not agree with us collecting your content, you can turn it off in the software settings" ([Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html); Last Updated 2025-06-20). The same policy records cross-border transfers "as permitted by law", GDPR-based opt-in for EU email recipients, deletion requests handled "within 72 hours" by email to `contactus@evoto.ai`, IDFA collection on iPad with an in-app tracking opt-out, and a statement that the company does "not knowingly collect any information from any minors under the age of 16".

The `about` page states a different default: "Evoto never uses your photos to train AI models without your explicit permission", and under "Our Commitments, Plainly Stated": "Transparency — We don't use your photos to train our models unless you explicitly opt in. No buried terms. No surprises." ([about](https://www.evoto.ai/about); accessed 2026-08-12). The 2026-04-29 release note repeats it as "Evoto does not use your images or data to train generative AI models without your explicit permission" ([release notes](https://www.evoto.ai/release-notes)), and the January 2026 statement adds "We source our data exclusively through commercially licensed and purchased imagery" ([Digital Camera World, 2026-01-21](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash)). The default-on-with-opt-out wording in the policy and the never-without-permission wording on the marketing pages are recorded here as they stand — see `Notes`.

The Terms also require United States users to ensure their content "does not contain sensitive data as defined by regulations such as the Protecting Americans' Data from Foreign Surveillance Act (PADFA)", disclaim responsibility for user content, and cap total liability at "the last licensing fee you paid" ([Terms of Use](https://res.evoto.ai/ui/www/policy/terms.html); Updated 2024-03-22).

### Technical background sought

No careers page exists on `evoto.ai` (`/careers`, `/jobs` and `/company/careers` all return HTTP 404 on 2026-08-12), and no first-party job posting was found. The Japanese startup-database profile for the Japan entity states 現在公開中の求人情報がありません ("no job openings currently published") and gives its size as 10人以下 ([スタクラ](https://startupclass.co.jp/online/companies/1846/); accessed 2026-08-12). LinkedIn's job pages were not inspected; a search-result summary referred to key-account and marketing roles, which is unconfirmed. No stack requirement, seniority bar or interview process is published — see `Notes`.

### Industry domain

The work spans professional photography production — RAW processing and camera colour profiles, tethered capture across six or more camera vendors, high-volume culling and batch delivery, print-quality export, and event gallery delivery and proofing ([release notes](https://www.evoto.ai/release-notes), [instant.evoto.ai](https://instant.evoto.ai/)) — together with facial and body editing of identifiable people, which places the product inside personal-data regimes: GDPR and CCPA are named on the site, the Japanese entity holds a JIS Q 15001-based Privacy Mark, the Terms reference PADFA, and the privacy policy addresses cross-border transfer, minors under 16 and automated scanning of cloud content ([about](https://www.evoto.ai/about), [Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html), [PR TIMES, 2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html)). Commercially it involves consumer app-store distribution and in-app purchase, credit ledgers and rollover accounting, VAT collection by country of residence, and a channel-distribution relationship in Japan ([Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html), [PR TIMES, 2024-12-27](https://prtimes.jp/main/html/rd/p/000000011.000132859.html)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Careers page | None found on `evoto.ai` | paths checked 2026-08-12 |
| Offices as published | Wilmington (Delaware), Singapore, Tokyo, Seoul | [about](https://www.evoto.ai/about); accessed 2026-08-12 |
| Stated distribution of the team | "Our team spans 6 countries"; "A global product built by a globally distributed team" | [about](https://www.evoto.ai/about) |
| Japan entity size | 10人以下 per the startup database; the government business registry lists one Shibuya office with 4 employees | [スタクラ](https://startupclass.co.jp/online/companies/1846/), [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305) (record updated 2025-12-05) |
| Stated working practice | "Every major product decision is tested against photographer feedback, not internal assumptions"; "We hire people who believe tools should be in service of the people using them" | [about](https://www.evoto.ai/about) |
| Working language | Not stated as a policy. The product ships in 13 app languages and the site in 15 locales; Japanese sales and support run through the Japanese entity | [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us), [sitemap index](https://www.evoto.ai/sitemap_index.xml) |
| Salary, benefits, remote policy, visa sponsorship, interview process, turnover | Not published | see `Notes` |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-08-12): `www.evoto.ai` homepage, `/about`, `/company`, `/payment`, `/download`, `/download/guide`, `/release-notes`, `/loyalty`, `/webinar`, `/referral`, `/evoto-mobile`, `/ipad`, plus `robots.txt`, `sitemap_index.xml`, `llms.txt`, `llms-full.txt` and probes of `/careers`, `/jobs`, `/press`, `/news`, `/security`, `/enterprise`, `/contact-sales`, `/ambassador`, `/terms`, `/privacy` and `/legal`; the policy documents on `res.evoto.ai/ui/www/policy/` (terms, privacy, refund, cookies); `instant.evoto.ai`, `video.evoto.ai`, `academy.evoto.ai`, `support.evoto.ai`, `help.evoto.ai`, `forum.evoto.ai`, `community.evoto.ai`, `api.evoto.ai`, `blog.evoto.ai` and its WordPress REST API; the published desktop installers and their code-signing certificates; the App Store, iTunes lookup API and Google Play listings including the developer block; the PR TIMES company feed for `株式会社Truesight Japan` (20 releases, 2024-02-19 to 2026-06-15) and individual releases; PR Newswire; gBizINFO and Japanese corporate-number directories; Singapore ACRA-derived company directories; GitHub, npm and PyPI; Wayback Machine CDX indexes for `evoto.ai`; Crunchbase, Tracxn, Latka and PitchBook profiles; LinkedIn; and English, Japanese and Chinese searches on the brand and the Truesight entity names.

- **Any funding round, investor, valuation or ownership structure.** No press index or investor page exists on `evoto.ai`, and no release mentions financing. Third-party databases state "unfunded" or "bootstrapped" without a primary source.
- **The corporate relationship between the four Truesight entities.** The `about` page calls Singapore, Japan and Korea "Branch", but the Singapore and Japan entities are separately registered companies. No filing, disclosure or company statement establishing parent, subsidiary or ownership was found. No Delaware or Korean registry record was retrieved.
- **Headcount.** Not published by the company. Third-party figures disagree by two orders of magnitude — see below.
- **Where engineering is located, and any engineering blog or open source.** The blog (711 posts) is photography tutorials, SEO comparison pages and product announcements; no technical writing, architecture post or model description was found. No GitHub, npm or PyPI presence exists under the brand or entity names.
- **The AI models and providers behind the features.** No model, provider, hosting region or third-party inference vendor is named anywhere on the site or in the policies; AWS is named only as the cloud provider for uploaded data.
- **What runs locally versus in the cloud.** The desktop installer is about 2 GB, and the privacy policy says content is uploaded "when the internal functions of the Software are insufficient", but no page states which features require upload.
- **ISO/IEC 27001 and SOC 2 Type 2 evidence.** Both badges appear on the site with no certificate number, scope, certification body, audit period or trust portal. Only the Japanese Privacy Mark carries a verifiable registration number and validity period.
- **Salary bands, remote policy, visa sponsorship, benefits and interview process.** No careers page exists; the only recruitment surface found was the Japanese startup database, which lists no open roles.
- **Customer, revenue, paid-subscriber, credit-consumption and retention figures.** The company publishes only rounded cumulative marketing figures ("1M+", "800M+"), attributed to "internal account and usage data reviewed as of 2026".
- **The founder's full name, career history and prior companies.** Only "Mitta" appears on the site; "Mitta Zhang" appears in distributed releases; no biography, education or prior employer is published by the company.
- **Sources that blocked automated access on 2026-08-12:** Crunchbase, PitchBook, `sgpbusiness.com` and `diyphotography.net` (HTTP 403); `houjin.jp` (no response). LinkedIn returned HTTP 999 to a plain request and served the page to a browser user agent, so its figures above were read directly. Where a source could not be read, wording comes from search-result snippets or alternative mirrors and is labelled accordingly.

### Inconsistencies across sources

- **Founding year:** the company says 2020 ([about](https://www.evoto.ai/about)) and its LinkedIn page says "TRUESIGHT PTE.LTD., established in 2020 in Singapore" ([LinkedIn](https://www.linkedin.com/company/evoto-ai)); [PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/) says "founded in 2022 by AI and graphics specialists at Truesight Technology Inc."; [Tracxn](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) says 2024. The Singapore company was incorporated 2022-07-13 and the Japanese one in June 2023 ([companies.sg](https://www.companies.sg/business/202224238M/TRUESIGHT-PTE-LTD-), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)); the earliest archived marketing site is 2022-11-23 ([Wayback](https://web.archive.org/web/20221123171058/https://evoto.ai/)).
- **Headquarters:** the site gives Wilmington, Delaware ([about](https://www.evoto.ai/about)); PetaPixel gives Menlo Park, California ([2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)); Tracxn gives Singapore; the EV code-signing certificate on the current Windows build gives Newark, Delaware (read 2026-08-12).
- **Which entity operates the service:** the Terms of Use and Refund Policy name `TRUESIGHT PTE. LTD.` and place disputes under Singapore law and courts ([Terms](https://res.evoto.ai/ui/www/policy/terms.html); Updated 2024-03-22), while the site footer, the `about` page and `llms.txt` present `Truesight Technology Inc.` in the United States as the company. Japanese releases describe the parent as Singaporean in January 2025 and as American by December 2025 ([PR TIMES, 2025-01-31](https://prtimes.jp/main/html/rd/p/000000013.000132859.html), [PR TIMES, 2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html)).
- **Headcount:** "a team of 500 employees" ([PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)); a self-declared company size of "501-1,000 employees" alongside 47 listed employee profiles on the company's own [LinkedIn](https://www.linkedin.com/company/evoto-ai) page (accessed 2026-08-12); "approximately 37 people" in 2026 ([Latka](https://getlatka.com/companies/evoto.ai)); 10人以下 for the Japanese entity ([スタクラ](https://startupclass.co.jp/online/companies/1846/)) and 4 employees at its Shibuya office ([gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305)).
- **Who represents the Japanese entity:** PR TIMES releases and its company profile give 代表取締役 Mitta Zhang / 代表者名 張偉 ([PR TIMES, 2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)); the スタクラ profile gives 代表取締役社長 ウィリアム・ワン with a Fujitsu Semiconductor background ([スタクラ](https://startupclass.co.jp/online/companies/1846/)).
- **Training-data consent default:** the Privacy Policy says uploaded content may be collected for product improvement with "full authorization" implied by use and an opt-out "in the software settings" ([Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html); Last Updated 2025-06-20), while the `about` page and the V7.1.5 release note say photos are never used to train models "without your explicit permission" ([about](https://www.evoto.ai/about), [release notes](https://www.evoto.ai/release-notes)).
- **Reach:** "200+ countries and regions" on the site versus "158 countries" in the September 2025 interview ([about](https://www.evoto.ai/about), [PetaPixel](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)).
- **Pricing display:** the payment page returns different currencies and figures by region — US dollars by default and Japanese yen when fetched from a Tokyo egress on 2026-08-12 — so a single quoted price is region-specific ([payment](https://www.evoto.ai/payment)).

### Other

- **The legal stack is older than the corporate presentation.** The Terms of Use carry an update date of 2024-03-22 and are written entirely for the Singapore entity, and the Privacy Policy was last updated 2025-06-20, while the site now presents a US company and four offices; the policy documents are served as static HTML from the S3 asset host rather than from the site's own routes ([Terms](https://res.evoto.ai/ui/www/policy/terms.html), [Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html)).
- **The public surface is heavily SEO-oriented.** `llms-full.txt` indexes 140 pages, of which 126 are feature landing pages ("AI Double Chin Remover", "AI Pet Leash Remover", …) and six are head-to-head comparison pages against Lightroom, Photoshop, Capture One, Luminar Neo and Imagen AI, each with a Markdown twin; the January 2026 statement described the withdrawn AI Headshot Generator as "intended as a secondary page focused on SEO" ([llms.txt](https://www.evoto.ai/llms.txt), [PetaPixel, 2026-01-15](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/)).
- **The site explicitly permits AI training on its own content.** `robots.txt` is served with `Content-Signal: ai-train=yes, search=yes, ai-input=yes` ([robots.txt](https://www.evoto.ai/robots.txt); observed 2026-08-12).
- **The product line went from one application to six surfaces in about three years:** desktop only in 2023, iPad in December 2024, Instant and Video announced at the Evoto One event in September 2025, and the phone app in November 2024 on iOS with a Japanese launch announcement in December 2025 ([release notes](https://www.evoto.ai/release-notes), [PR TIMES, 2024-12-16](https://prtimes.jp/main/html/rd/p/000000009.000132859.html), [PetaPixel, 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/), [PR TIMES, 2025-12-25](https://prtimes.jp/main/html/rd/p/000000018.000132859.html)).
- **Japan is the only market with a separate public communications channel.** Its PR TIMES feed lists 20 releases dated 2024-02-19 to 2026-06-15, and the entity holds a Privacy Mark, works through a named distributor, and publishes its own Japanese product manual; the two most recent Japanese releases are consumer surveys about photo studios and retouching attitudes rather than product news ([PR TIMES company feed](https://prtimes.jp/main/html/searchrlp/company_id/132859); accessed 2026-08-12).
- **The site ships a Traditional Chinese locale but no Simplified Chinese one**, while the desktop application and iOS app list a generic `ZH` language code ([robots.txt](https://www.evoto.ai/robots.txt), [iTunes lookup API](https://itunes.apple.com/lookup?id=6596737043&country=us)).
- **Free-tier boundaries moved during 2025.** Colour correction, crop/rotate and manual tools became export-credit-free for paid users on desktop v6.1 and later, excluding iPad, Instant and older desktop builds ([PR TIMES, 2025-12-05](https://prtimes.jp/main/html/rd/p/000000016.000132859.html)).

---

## Resources

**Official**

- [Homepage](https://www.evoto.ai/) · [About](https://www.evoto.ai/about) · [About Us / company](https://www.evoto.ai/company)
- [Payment options](https://www.evoto.ai/payment) · [Download](https://www.evoto.ai/download) · [Release notes](https://www.evoto.ai/release-notes)
- [Loyalty programme](https://www.evoto.ai/loyalty) · [Referral programme](https://www.evoto.ai/referral) · [Webinars](https://www.evoto.ai/webinar)
- [robots.txt](https://www.evoto.ai/robots.txt) · [sitemap index](https://www.evoto.ai/sitemap_index.xml) · [llms.txt](https://www.evoto.ai/llms.txt) · [llms-full.txt](https://www.evoto.ai/llms-full.txt)
- [Terms of Use](https://res.evoto.ai/ui/www/policy/terms.html) (Updated 2024-03-22) · [Privacy Policy](https://res.evoto.ai/ui/www/policy/privacy.html) (Last Updated 2025-06-20) · [Refund Policy](https://res.evoto.ai/ui/www/policy/refund.html) · [Cookie Policy](https://res.evoto.ai/ui/www/policy/cookies.html)
- [Evoto Instant](https://instant.evoto.ai/) · [Evoto Video](https://video.evoto.ai/) · [Academy](https://academy.evoto.ai) · [Support centre](https://support.evoto.ai/) · [Community forum](https://forum.evoto.ai)
- [Blog](https://blog.evoto.ai/) — [WordPress REST API post index](https://blog.evoto.ai/wp-json/wp/v2/posts?per_page=1) · [Capterra 2026 announcement, 2026-03-27](https://blog.evoto.ai/evoto-capterra-2026-press-release/)
- Desktop packages on the asset host — [Windows 7.3.0-512](https://res.evoto.ai/package/7.3.0-512/Evoto_Setup_7.3.0-512.exe) · [macOS arm64 7.3.0-512](https://res.evoto.ai/package/7.3.0-512/Evoto-7.3.0-512_arm64.dmg) · [Japanese manual (PDF)](https://res.evoto.ai/ja/evoto-manural.pdf)
- [Archived "Online AI Headshot Generator" page, captured 2026-01-10](https://web.archive.org/web/20260110205938/https://www.evoto.ai/features/ai-headshot-generator) · [Archived homepage, captured 2022-11-23](https://web.archive.org/web/20221123171058/https://evoto.ai/)

**Press releases**

- [PR Newswire — "Evoto Ends Photographer Burnout at Imaging USA 2026 with Revolutionary All-in-One Workflow", 2026-01-11](https://www.prnewswire.com/news-releases/evoto-ends-photographer-burnout-at-imaging-usa-2026-with-revolutionary-all-in-one-workflow-302658081.html)
- [PR TIMES — 株式会社Truesight Japan release feed (JA)](https://prtimes.jp/main/html/searchrlp/company_id/132859)
- [PR TIMES — 一部機能を無料化, 2025-12-05 (JA)](https://prtimes.jp/main/html/rd/p/000000016.000132859.html) · [iPhone版リリース, 2025-12-25 (JA)](https://prtimes.jp/main/html/rd/p/000000018.000132859.html) · [プライバシーマーク取得, 2025-01-31 (JA)](https://prtimes.jp/main/html/rd/p/000000013.000132859.html) · [ラボネットワークと代理店契約, 2024-12-27 (JA)](https://prtimes.jp/main/html/rd/p/000000011.000132859.html) · [Evoto iPad リリース, 2024-12-16 (JA)](https://prtimes.jp/main/html/rd/p/000000009.000132859.html) · [CP+2025 出展, 2025-02-20 (JA)](https://prtimes.jp/main/html/rd/p/000000014.000132859.html) · [PHOTONEXT 出展, 2024-05-31 (JA)](https://prtimes.jp/main/html/rd/p/000000004.000132859.html) · [ブライダル産業フェア 出展, 2024-04-30 (JA)](https://prtimes.jp/main/html/rd/p/000000003.000132859.html) · [CP+2024 出展, 2024-02-19 (JA)](https://prtimes.jp/main/html/rd/p/000000001.000132859.html)
- [Labo Network — 代理店契約締結のお知らせ, 2024-12-27 (JA)](https://www.labonetwork.co.jp/news/24122701/)

**Store listings**

- [App Store — Evoto-AI Photo Editor&Retouch](https://apps.apple.com/us/app/evoto-ai-photo-editor-retouch/id6596737043) · [iTunes lookup API record](https://itunes.apple.com/lookup?id=6596737043&country=us)
- [iTunes lookup API — Evoto Instant](https://itunes.apple.com/lookup?id=6749685404&country=us) · [Apple developer page — TRUESIGHT PTE. LTD.](https://apps.apple.com/us/developer/truesight-pte-ltd/id1760458737)
- [Google Play — com.truesight.evoto](https://play.google.com/store/apps/details?id=com.truesight.evoto)

**Third-party coverage and profiles**

- [PetaPixel — "Evoto Believes it Can Beat Adobe at Its Own Game", 2025-09-23](https://petapixel.com/2025/09/23/evoto-believes-it-can-beat-adobe-at-its-own-game/)
- [PetaPixel — "Evoto Alienated Photographers By Releasing a Tool Designed to Replace Them", 2026-01-15](https://petapixel.com/2026/01/15/evoto-alienated-photographers-by-releasing-a-tool-designed-to-replace-them/)
- [Digital Camera World — "We missed the mark, and we are sorry", 2026-01-21](https://www.digitalcameraworld.com/photography/photo-editing/we-missed-the-mark-and-we-are-sorry-evoto-responds-to-ai-headshot-generator-backlash)
- [Digital Camera World — Evoto AI review, 2026-02-13](https://www.digitalcameraworld.com/tech/software/evoto-ai-review)
- [The Phoblographer — "Evoto AI Headshot Generator Apology is BS", 2026-01-14](https://www.thephoblographer.com/2026/01/14/evoto-ai-headshot-generator-anti-photographer/)
- [DIY Photography — "Evoto Angers Photographers by a Surprise AI Headshot Launch" (HTTP 403 to automated access on 2026-08-12)](https://www.diyphotography.net/evoto-angers-photographers-by-a-surprise-ai-headshot-launch-but-is-evoto-the-villain-here/)
- [スタクラ — 株式会社Truesight Japan 企業プロフィール (JA)](https://startupclass.co.jp/online/companies/1846/)
- [gBizINFO — 株式会社Truesight Japan, corporate number 5020001152305 (JA)](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=5020001152305)
- [companies.sg — TRUESIGHT PTE. LTD. (202224238M)](https://www.companies.sg/business/202224238M/TRUESIGHT-PTE-LTD-) · [sgpbusiness — TRUESIGHT PTE. LTD. (HTTP 403 to automated access on 2026-08-12)](https://www.sgpbusiness.com/company/Truesight-Pte-Ltd)
- [Tracxn — Evoto company profile](https://tracxn.com/d/companies/evoto/__hpvy--AEZ7rSgMKGa4Li-FlvfSVYRRj8iC3YKjhJReI) · [Latka — Evoto AI revenue profile](https://getlatka.com/companies/evoto.ai) · [Crunchbase — Evoto (HTTP 403 to automated access on 2026-08-12)](https://www.crunchbase.com/organization/evoto)
- [PitchBook — Truesight (China) profile](https://pitchbook.com/profiles/company/503403-85) · [PitchBook — TrueSight Technology profile](https://pitchbook.com/profiles/company/437673-34) — both HTTP 403 to automated access on 2026-08-12; neither confirmed to describe this company
- [LinkedIn — Evoto AI company page](https://www.linkedin.com/company/evoto-ai)
