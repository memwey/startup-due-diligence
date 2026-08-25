# Spatius

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-26.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Spatius sells real-time AI avatar ("digital human") infrastructure: a cloud **Motion Server** turns speech audio into facial-motion data, and **AvatarKit** SDKs for Web, iOS, Android and Flutter render a 3D Gaussian Splatting avatar locally on the end user's device, so no rendered video is streamed ([docs — How It Works](https://docs.spatius.ai/concepts/how-it-works.md); accessed 2026-08-26). The site is operated by **SPATIALWALK PTE. LTD.**, Singapore ([spatius.ai](https://www.spatius.ai/), [Terms of Service](https://www.spatius.ai/terms-of-service/), effective 2026-04-26). The same business runs in China as **空间漫步 / SpatialWalk** through **空间漫步科技（深圳）有限公司** ([spatialwalk.cn](https://www.spatialwalk.cn/), ICP filing 粤ICP备2025499042号), and a third name, **SpatialReal, Inc.** of San Jose, California, is on a parallel live site ([spatialreal.ai](https://www.spatialreal.ai/); accessed 2026-08-26) — see `Identity and legal entities`.

- Published performance and cost claims: 1080p at 25fps on entry-level SoCs (G88, RK3576, S565, 8189) with no discrete GPU, motion data at "~10–15 KB/s", under 300 ms of added rendering latency, and a Scale-plan rate of **$0.007/min ($0.42/hour)** compared with "~$0.15 / min" for cloud streaming ([spatius.ai](https://www.spatius.ai/), [docs](https://docs.spatius.ai/concepts/how-it-works.md), [spatialwalk.cn](https://www.spatialwalk.cn/); accessed 2026-08-26).
- **Funding is announced by an investor, not by the company.** Impa Ventures (Singapore) published "IMPA Family | Our Investment in Spatial Walk" on 2025-10-31 with no round name, amount or co-investors ([Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)). The company's own funding statements appear only in recruiting copy — see `Funding`.
- **The hiring record is the richest public source on engineering.** Thirteen V2EX job posts from `hr@spatialwalk.net` between 2025-05-12 and 2026-02-04 name the stack (Go backend, Swift/Metal, Kotlin, Vue/WebGPU/wasm, 3DGS), the base city moving from Beijing to Shenzhen, and the self-description "中美双总部" (China–US dual headquarters) ([sov2ex index](https://www.sov2ex.com/api/search?q=spatialwalk&size=20); [V2EX 1131126](https://www.v2ex.com/t/1131126), [V2EX 1189876](https://www.v2ex.com/t/1189876)).
- Named users, all from the company's own blog: **Midoo AI** ("15K+ daily avatar sessions", 2026-07-01), **ChickyTutor** (2026-07-08) and **SayMei** (2026-08-11, with per-product metrics); the Chinese site names **Talk AI** and **听力熊** ([Spatius blog](https://www.spatius.ai/blog/), [spatialwalk.top](https://spatialwalk.top/); accessed 2026-08-26).
- Team size is not stated by the company; the LinkedIn company page lists "11-50 employees" and a 2025 founding year, while the `spatialwalk` GitHub organisation was created 2024-05-23 and `spatialwalk.net` registered 2024-08-08 ([LinkedIn](https://www.linkedin.com/company/spatius-ai), [GitHub API](https://api.github.com/orgs/spatialwalk), WHOIS read 2026-08-26) — see `Inconsistencies across sources`.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Spatius — "Real-Time AI Avatar Infrastructure", "Next-Gen Digital Human" | [spatius.ai](https://www.spatius.ai/); accessed 2026-08-26 |
| Operating entity | "SPATIALWALK PTE. LTD.", stated as operating as Spatius | [Terms of Service](https://www.spatius.ai/terms-of-service/); effective 2026-04-26 |
| Registered address | "70 Shenton Way, #16-13, EON Shenton, Singapore 079118" | [Terms of Service](https://www.spatius.ai/terms-of-service/), [Privacy Policy](https://www.spatius.ai/privacy-policy/) |
| Singapore registration | UEN 202531523H, incorporated 2025-07-21, status "Live Company", principal activity SSIC 63909 "Other information service activities n.e.c.", 1 officer/owner listed | [RecordOwl mirror of ACRA data](https://recordowl.com/company/spatialwalk-pte-ltd); read 2026-08-26 |
| Chinese brand and entity | 空间漫步 / SpatialWalk; footer "© 2026 空间漫步科技（深圳）有限公司 版权所有" | [spatialwalk.cn](https://www.spatialwalk.cn/); accessed 2026-08-26 |
| Chinese ICP filing | 粤ICP备2025499042号 (Guangdong series, 2025) | [spatialwalk.cn](https://www.spatialwalk.cn/), [spatialwalk.top](https://spatialwalk.top/) |
| US-facing entity | "SpatialReal, Inc. · 160 E Tasman Dr, San Jose, CA 95134, USA" | [spatialreal.ai](https://www.spatialreal.ai/); accessed 2026-08-26 |
| Governing law | "These Terms are governed by the laws of Singapore"; exclusive jurisdiction of the Singapore courts, with a carve-out for EU/UK consumers | [Terms of Service](https://www.spatius.ai/terms-of-service/) |
| Liability cap | Greater of fees paid in the preceding three months or "SGD 100" | [Terms of Service](https://www.spatius.ai/terms-of-service/) |
| Document dates | Terms of Service effective 2026-04-26; Privacy Policy "Last Updated: April 22, 2026"; Chinese compliance guide last updated 2026-01-06 | [Terms](https://www.spatius.ai/terms-of-service/), [Privacy](https://www.spatius.ai/privacy-policy/), [合规接入指引](https://www.spatialwalk.cn/compliance-guide) |
| Public contacts | `hello@spatius.ai` (demos, partnerships), `support@spatius.ai` (privacy); China: `hello@spatialwalk.net`, `support@spatialwalk.net`; hiring: `hr@spatialwalk.net` | [Contact](https://www.spatius.ai/contact/), [Privacy Policy](https://www.spatius.ai/privacy-policy/), [spatialwalk.top](https://spatialwalk.top/), [V2EX 1173996](https://www.v2ex.com/t/1173996) |
| Headcount | "11-50 employees" on the LinkedIn company page; no figure published by the company | [LinkedIn](https://www.linkedin.com/company/spatius-ai); accessed 2026-08-26 |
| Community | Discord "Spatius" — 51 members, 4 online; the older "SpatialReal Inc." server — 39 members, 6 online | [Discord invite API (Spatius)](https://discord.com/api/v9/invites/9HGhZfHZh9?with_counts=true), [Discord invite API (SpatialReal)](https://discord.com/api/v9/invites/dRSUTdPCjm?with_counts=true); read 2026-08-26 |
| Domains | `spatialwalk.net` created 2024-08-08 (Cloudflare); `spatialreal.ai` created 2025-11-03; `spatius.ai` created 2026-04-10; `spatialwalk.ai` 301-redirects to `www.spatialwalk.cn`; `spatialwalk.top` serves the Chinese SpatialWalk site and hosts the `cn-beijing` console | WHOIS read 2026-08-26; redirects observed 2026-08-26; [docs — Regions](https://docs.spatius.ai/api-reference/regions.md) |
| GitHub organisations | `spatialwalk` — created 2024-05-23, 10 public repositories, website field `spatius.ai`; `spatius-ai` — created 2026-04-19, 11 public repositories | [GitHub API](https://api.github.com/orgs/spatialwalk), [GitHub API](https://api.github.com/orgs/spatius-ai); read 2026-08-26 |
| Mobile apps | No first-party app found in the US App Store for "spatius" or "spatialwalk" | [iTunes search API](https://itunes.apple.com/search?term=spatius&entity=software&country=us&limit=5); checked 2026-08-26 |
| Site surface | 210 URLs in the main sitemap (188 of them blog posts), plus 51-URL sitemaps each for comparisons, integrations and glossary; English and `/zh/` locales | [sitemap index](https://www.spatius.ai/sitemap-index.xml); read 2026-08-26 |

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Spatius | Current international brand | `spatius.ai`, domain created 2026-04-10 | "SPATIALWALK PTE. LTD. operating as Spatius" | [Terms of Service](https://www.spatius.ai/terms-of-service/) |
| SPATIALWALK PTE. LTD. | Legal entity | Singapore, UEN 202531523H, incorporated 2025-07-21 | Operator of `spatius.ai`; named in the site footer and legal documents | [RecordOwl](https://recordowl.com/company/spatialwalk-pte-ltd), [spatius.ai](https://www.spatius.ai/) |
| 空间漫步科技（深圳）有限公司 | Legal entity | Shenzhen, China; ICP filing 粤ICP备2025499042号 | Copyright holder of `spatialwalk.cn`, which sells the same product under the name Spatius | [spatialwalk.cn](https://www.spatialwalk.cn/) |
| SpatialWalk / 空间漫步 | China-facing brand | `spatialwalk.net` (created 2024-08-08), `spatialwalk.cn`, `spatialwalk.top` | Same product line; the Chinese site's footer reads "SpatialWalk 空间漫步科技（深圳）有限公司" | [spatialwalk.top](https://spatialwalk.top/) |
| SpatialReal, Inc. | Legal entity | 160 E Tasman Dr, San Jose, CA 95134, USA | Footer of `spatialreal.ai`, a live site selling the same SDK; `docs.spatialreal.ai` is the documentation linked from the `spatialwalk` GitHub organisation's demo repository | [spatialreal.ai](https://www.spatialreal.ai/), [avatarkit-voice-agent-demo](https://github.com/spatialwalk/avatarkit-voice-agent-demo) |
| SpatialReal | Prior/parallel international brand | `spatialreal.ai`, domain created 2025-11-03 | The npm package `@spatialwalk/avatarkit` was described as an SDK "for SpatialReal avatars"; `@spatius/avatarkit` superseded it in 2026 | [GitHub API](https://api.github.com/orgs/spatialwalk), [npm registry](https://registry.npmjs.org/@spatialwalk/avatarkit) |
| 空间漫步传媒科技（深圳）有限责任公司 | Unrelated name collision | Founded 2019-08-20, legal representative 耿珑 | A different Shenzhen company with a similar Chinese name; no connection established | [Baidu Baike](https://baike.baidu.com/item/%E7%A9%BA%E9%97%B4%E6%BC%AB%E6%AD%A5%E4%BC%A0%E5%AA%92%E7%A7%91%E6%8A%80%EF%BC%88%E6%B7%B1%E5%9C%B3%EF%BC%89%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/24226245) |

No source reviewed states how the Singapore, Chinese and US entities relate to one another — ownership, contracting party per region, and which entity employs the Shenzhen engineering team are not published.

---

## Product

The platform has three published parts ([docs — Welcome](https://docs.spatius.ai/getting-started.md); accessed 2026-08-26):

- **AvatarKit** — client SDKs for Web, iOS, Android and Flutter that "download avatar assets, render the avatar locally, and play synchronized audio". Avatar assets are 3D Gaussian Splatting packages of "about 5-10 MB" that must finish downloading before rendering starts ([docs — Avatar](https://docs.spatius.ai/concepts/avatar.md)).
- **Motion Server** — a cloud service that "receives avatar speech audio, returns motion data" at "~10–15 KB/s, much lower than a video stream" ([docs — How It Works](https://docs.spatius.ai/concepts/how-it-works.md)).
- **Spatius Studio** — the web console at `app.spatius.ai` for managing apps and avatars (page title "Spatius Studio", read 2026-08-26).

Integration paths documented: **Direct Mode** (client owns the audio), **Backend Mode** (server SDKs in Python and Go), **LiveKit Agents**, **Agora Convo AI**, and a **TEN Framework** extension ([docs — Integrations](https://docs.spatius.ai/integrations/overview.md), [SDK capability matrix](https://docs.spatius.ai/reference/sdk-capabilities.md)). Audio input is "mono 16-bit PCM (`s16le`)" with Opus accepted by some SDKs; the platform animates only — "developers manage microphone, ASR, LLM, and speech generation" ([docs — FAQ](https://docs.spatius.ai/resources/faq.md)).

Three regions are published: `us-west`, `ap-northeast` and `cn-beijing`; the China console runs on `console.cn-beijing.spatialwalk.top` while the other endpoints sit on `spatius.ai` ([docs — Regions](https://docs.spatius.ai/api-reference/regions.md)).

Avatars are created through a documented REST API: `POST /avatars` takes a public JPEG or PNG URL, maximum 5 MiB, shorter side at least 340 px, "Exactly one clearly visible face", and returns an asynchronous job to poll; each successful creation consumes an "Avatar Creations" unit and is subject to rate, 24-hour rolling quota and concurrency limits ([docs — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)).

Stated performance and cost claims, as published on the marketing sites (accessed 2026-08-26):

| Claim | Value | Source |
|---|---|---|
| Resolution and frame rate | 1080p at 25fps on entry-level SoCs "(G88, RK3576等低功耗芯片验证通过)", no discrete GPU required | [spatialwalk.cn](https://www.spatialwalk.cn/), [spatius.ai](https://www.spatius.ai/) |
| Added rendering latency | "<300ms"; "<1s 端到端延迟" achievable with a high-performance audio pipeline | [spatialwalk.cn](https://www.spatialwalk.cn/) |
| Bandwidth | "100 kbps" (English site); "10–20KB/s 参数包" (Chinese site); "~10–15 KB/s" (documentation) | [spatius.ai](https://www.spatius.ai/), [spatialwalk.top](https://spatialwalk.top/), [docs](https://docs.spatius.ai/concepts/how-it-works.md) |
| Network resilience | "三倍冗余抗丢包，网络抖动下播放不中断" (triple redundancy against packet loss) | [spatialwalk.cn](https://www.spatialwalk.cn/) |
| Rendering split | "90% 渲染在端侧完成" | [spatialwalk.top](https://spatialwalk.top/) |
| Technical approach | "3DGS路线 + 自研轻量化多模态模型 + 端侧实时推理", plus a proprietary phoneme-sync algorithm | [spatialwalk.top](https://spatialwalk.top/) |
| Integration effort | "一个熟练的客户端工程师仅需2-3个工作日即可完成核心功能的集成" | [spatialwalk.top](https://spatialwalk.top/) |
| Cumulative usage | "10M+ interactions processed to date" | [spatialreal.ai](https://www.spatialreal.ai/) |

### Commercialization

Spatius publishes a credit-based price list with five self-serve tiers plus Enterprise: Free ($0, 1,000 credits ≈ 100 min, 2 concurrent sessions), Starter ($19), Builder ($49), Growth ($149) and Scale ($299, 400,000 credits ≈ 40,000 min, 40 concurrent sessions, unlimited session length); annual billing is advertised at a 20% discount. Overage is "$0.009/minute" on Starter through Growth and "$0.007/minute" on Scale. Avatar creations are sold separately, from $25 for one down to $16 each in a 500-pack. The Enterprise tier advertises unlimited sessions, a custom avatar API, an SLA and "SOC II/GDPR compliance" ([Pricing](https://www.spatius.ai/pricing/); read 2026-08-26).

The Chinese site sells the same rate with a budget calculator: at $5,000, "Spatius 进阶版套餐（端云结合）" at "$0.007 / min" yields "11,349 小时" against "556 小时" at an industry average of "~$0.15 / min" ([spatialwalk.cn](https://www.spatialwalk.cn/)). The Chinese FAQ describes a different commercial shape for hardware: "针对C端硬件产品，我们主要采用按激活设备量的年度授权或终身授权" (per-activated-device annual or perpetual licensing), with per-minute or monthly billing for software ([spatialwalk.top](https://spatialwalk.top/)).

The parallel `spatialreal.ai` price card differs on the free tier — "Free: 500 credits/month" against Spatius's 1,000, and "Starter: 22,000 credits/month ($19)" against Spatius's 20,000 ([spatialreal.ai](https://www.spatialreal.ai/); read 2026-08-26).

### Reported scale over time

| Date | Event or figure | Source |
|---|---|---|
| 2024-05-23 | GitHub organisation `spatialwalk` created | [GitHub API](https://api.github.com/orgs/spatialwalk) |
| 2024-08-08 | `spatialwalk.net` domain registered | WHOIS read 2026-08-26 |
| 2025-11-06 | First public SDK release: npm `@spatialwalk/avatarkit` 1.0.0-beta.1, "AvatarKit SDK - 3D Gaussian Splatting Avatar Rendering SDK", MIT | [npm registry](https://registry.npmjs.org/@spatialwalk/avatarkit) |
| 2025-12-07 | Flutter plugin `avatar_kit` 1.0.0-beta.1 published | [pub.dev](https://pub.dev/packages/avatar_kit) |
| 2026-04-10 | `spatius.ai` domain registered; GitHub organisation `spatius-ai` created 2026-04-19 | WHOIS read 2026-08-26; [GitHub API](https://api.github.com/orgs/spatius-ai) |
| 2026-07-01 | Blog: "How Midoo AI Scaled to 15K+ Daily Avatar Sessions with Spatius" | [Spatius blog](https://www.spatius.ai/blog/) |
| 2026-07-26 | SayMei figures quoted in the customer story: "2,300+ registered learners", "10,000+ completed live lesson sessions", "312,000+ … conversation turns", "190+ hours of live lesson time since April 25" | [SayMei customer story](https://www.spatius.ai/blog/saymei-ai-mandarin-tutor-spatius/); published 2026-08-11 |
| 2026-08-17 | `@spatius/avatarkit` 1.3.7 and iOS release v1.3.3 published | [npm registry](https://registry.npmjs.org/-/v1/search?text=spatius&size=20), [GitHub releases](https://github.com/spatius-ai/avatarkit-ios-release/releases) |
| 2026-08-24 | npm downloads for the trailing month: 7,417 for `@spatius/avatarkit`, 973 for `@spatialwalk/avatarkit` | [npm API](https://api.npmjs.org/downloads/point/last-month/@spatius/avatarkit) |

### Announced customers

| Customer | What is claimed | Date | Source |
|---|---|---|---|
| Midoo AI | "Scaled to 15K+ Daily Avatar Sessions with Spatius" | 2026-07-01 | [Spatius blog](https://www.spatius.ai/blog/) |
| ChickyTutor | Real-time avatar layer added to a voice tutor | 2026-07-08 | [Spatius blog](https://www.spatius.ai/blog/) |
| SayMei | Spatius avatar as the visible layer of a LiveKit-based Mandarin tutor; "12 average conversation turns with Spatius Pink (vs. 7 with previous avatar)"; quote attributed to "Leland Char, Founder of SayMei" | 2026-08-11 | [SayMei customer story](https://www.spatius.ai/blog/saymei-ai-mandarin-tutor-spatius/) |
| Talk AI | "接入 SDK，实时对话、精准口型、自然表情" for an AI spoken-English tutor | undated | [spatialwalk.top](https://spatialwalk.top/) |
| 听力熊 | "按设备授权的低成本SDK" for a children's AI companion product | undated | [spatialwalk.top](https://spatialwalk.top/) |

### Stated plans

- Custom-trained 3DGS avatar models are described as "currently in beta access", and the Chinese site marks image-based avatar customization as "用户内测开放中" ([Spatius blog — product update](https://www.spatius.ai/blog/spatius-product-update-avatar-apis-faster-audio-production-ready-sdks/), published 2026-08-22; [spatialwalk.cn](https://www.spatialwalk.cn/)).
- The Chinese FAQ states "我们目前全面支持 iOS，Web及Android SDK将在11月上线" — a November launch for the Web and Android SDKs, with no year given on the page ([spatialwalk.top](https://spatialwalk.top/); read 2026-08-26).
- The recruiting copy states the goal as "打造端侧 AI 形象引擎，重构全球下一代人机交互标准" (build an on-device AI avatar engine and redefine the next generation of human-computer interaction) ([V2EX 1189876](https://www.v2ex.com/t/1189876); 2026-02-01).

---

## Founder

The Chinese site publishes a four-person team section (read 2026-08-26 on [spatialwalk.top](https://spatialwalk.top/), which serves the same page as `spatialwalk.net`):

| Name | Title on the page | Description on the page |
|---|---|---|
| Hang Li | CEO | "前腾讯产品经理，曾为中国Top 1的音乐社交产品赋能过亿用户增长" |
| Yuhang Li | CTO | "前字节跳动资深全栈工程师，丰富的软件开发及渲染引擎经验" |
| Yudong Guo | 首席科学家 (Chief Scientist) | "3D数字人领域奠基性论文AD-NeRF作者，中国科学技术大学助理教授" |
| Xiaodong Cun | 首席技术顾问 (Chief Technical Advisor) | "SadTalker (13k+ GitHub Stars) 作者 … 前腾讯AI Lab高级研究员，大湾区大学助理教授" |

Verifiable career facts about the two academics, from their own pages:

- **Yudong Guo** is an assistant professor at USTC; he received his PhD there in 2021 under Prof. Juyong Zhang and a BSc in Statistics in 2015, and was a research assistant at Nanyang Technological University's MultiMedia Lab from Fall 2016 to Spring 2017. AD-NeRF ("AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis") was published at ICCV 2021 ([yudongguo.github.io](https://yudongguo.github.io/); accessed 2026-08-26). His page does not mention Spatius, SpatialWalk or any company role.
- **Xiaodong Cun** is an assistant professor at Great Bay University's School of Computing and Information Science and leads its GVC Lab; SadTalker was published at CVPR 2023 with a Tencent AI Lab affiliation among the authors ([SadTalker project page](https://sadtalker.github.io/), [GitHub — OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker); accessed 2026-08-26).

The investor announcement adds biography for the founder, named there only as "Hang": "Hang has spent over seven years as a product manager at leading Internet companies like Tencent"; he "built a matchmaking app in college and eventually quit his stable career to start Spatial Walk — right when Apple unveiled the Vision Pro", and flew to New York to queue for the device ([Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk); 2025-10-31).

Recruiting copy describes the wider team as "核心团队来自清华、中科大、南洋理工、字节跳动、腾讯，曾在 CVPR 、ICCV 、NeurIPS 等顶级学术会议发表多篇论文，并与清华、浙大等高校实验室长期合作" ([V2EX 1153830](https://www.v2ex.com/t/1153830); 2025-08-20). No individual engineer is named on any company page, and neither `spatius.ai` nor `spatialreal.ai` publishes a team section.

---

## Funding

| Date | Round | Amount | Investors | Source |
|---|---|---|---|---|
| 2025-10-31 | Not named | Not disclosed | Impa Ventures (Singapore) | [Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk) |
| 2025-05-12 | "种子融资" (seed), as described in a job post | "数百万" (millions, currency unstated); "下一轮美元融资进行中" (next USD round in progress) | Not named | [V2EX 1131126](https://www.v2ex.com/t/1131126) |
| 2025-08-20 onward | "多轮融资" (multiple rounds), as described in job posts | "估值过亿" (valuation over ¥100M) | Not named | [V2EX 1153830](https://www.v2ex.com/t/1153830), [V2EX 1161367](https://www.v2ex.com/t/1161367) |

Facts that do not fit the table:

- The only investor-side announcement found is Impa Ventures' post. It names no round, no amount and no co-investors, and describes the fund as investing in "AI and frontier technologies … from 0 to 1" ([Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk); [Impa Ventures](https://impa.ventures/)).
- That post quotes a price of "$0.003 / min" for Spatial Walk in a comparison table against Tavus ($0.3/min), Synthesia ($3/min) and HeyGen ("Real-time $0.15 / min") — roughly half the $0.007/min the company published ten months later.
- No funding announcement was found on any company site, in any press release, or from any Chinese or English outlet; Crunchbase returns HTTP 403 and PitchBook is subscription-gated (checked 2026-08-26) — see `Notes`.
- The job posts are recruiting copy written by the employer, not filings or investor statements. They are recorded here because they are the only company-side statements about funding that exist publicly.

---

## Engineering

### Technology stack and platforms

Confirmed by published artifacts (packages, repositories, documentation):

- **Client SDKs** — Web (`@spatius/avatarkit`, MIT, 1.3.7 on 2026-08-17; predecessor `@spatialwalk/avatarkit`, 104 versions, 2025-11-06 to 2026-04-22), iOS (Swift; release repo `spatius-ai/avatarkit-ios-release`, v1.3.3 on 2026-08-17), Android (Kotlin; Maven Central artifact `ai.spatialwalk:avatarkit`), Flutter (`avatar_kit` on pub.dev, 44 versions, first 2025-12-07) ([npm](https://registry.npmjs.org/@spatialwalk/avatarkit), [pub.dev](https://pub.dev/packages/avatar_kit), [Maven Central](https://mvnrepository.com/artifact/ai.spatialwalk/avatarkit), [GitHub releases](https://github.com/spatius-ai/avatarkit-ios-release/releases)).
- **Server SDKs** — Python and Go, plus a TypeScript server SDK in the older organisation; an `open-platform-cli` written in Go ([GitHub API](https://api.github.com/orgs/spatius-ai), [GitHub API](https://api.github.com/orgs/spatialwalk)).
- **Real-time transport** — LiveKit (own plugin `livekit-plugins-spatius`, bundled Web provider) and Agora (native provider on iOS/Android, Convo AI integration, TEN Framework extension); WebSockets as an alternative ([docs — Integrations](https://docs.spatius.ai/integrations/overview.md), [SDK capability matrix](https://docs.spatius.ai/reference/sdk-capabilities.md)).
- **Rendering** — 3D Gaussian Splatting assets rendered client-side; the npm package description reads "3D Gaussian Splatting Avatar Rendering SDK" ([npm](https://registry.npmjs.org/@spatialwalk/avatarkit)).
- **Audio** — mono 16-bit PCM (`s16le`), Opus uplink enabled by default on the client SDKs ([docs — FAQ](https://docs.spatius.ai/resources/faq.md), [SDK capability matrix](https://docs.spatius.ai/reference/sdk-capabilities.md)).
- **Infrastructure and vendors named in the Privacy Policy** — AWS and Google Cloud (infrastructure), LiveKit Cloud (communications), PostHog (analytics), Stripe (payments), Google and GitHub (authentication), unnamed ASR providers ([Privacy Policy](https://www.spatius.ai/privacy-policy/)).
- **Edge** — Cloudflare fronts `spatius.ai` (response headers `server: cloudflare`, observed 2026-08-26).
- **Documentation** — MDX, published from the public repository `spatius-ai/docs` with an `llms.txt` index ([GitHub API](https://api.github.com/orgs/spatius-ai), [llms.txt](https://docs.spatius.ai/llms.txt)).

Mentioned only as hiring requirements or preferences, not established as in use: Kubernetes, gRPC, Redis, Kafka, Docker, Vue.js, React, Node.js, WebGL/WebGPU/WebXR, WebAssembly, Metal, Vulkan, OpenGL ES, MediaCodec, AVFoundation, Unity3D/Unreal shader work ([V2EX 1173996](https://www.v2ex.com/t/1173996), [V2EX 1136977](https://www.v2ex.com/t/1136977), [V2EX 1175749](https://www.v2ex.com/t/1175749), [V2EX 1132398](https://www.v2ex.com/t/1132398)).

### Systems

- **Motion inference service** — takes speech audio and emits facial-motion parameters at ~10–15 KB/s, deployed per region and reached over WebSocket at `wss://api.<region>.spatius.ai/v2/driveningress` ([docs — How It Works](https://docs.spatius.ai/concepts/how-it-works.md), [docs — Regions](https://docs.spatius.ai/api-reference/regions.md)).
- **Console and session-token API** — per-region `console.<region>` endpoints issuing per-session tokens, with `X-App-ID`/`X-API-Key` authentication for the management API ([docs — Regions](https://docs.spatius.ai/api-reference/regions.md), [docs — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)).
- **Avatar build pipeline** — asynchronous jobs that turn a submitted photograph into a downloadable 3DGS avatar package, with quota reservation and release semantics ([docs — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)).
- **Client rendering and playback engine** — asset download, local rendering, audio/motion synchronisation, lifecycle and state events, frame-starvation handling, render-quality controls ([docs — Client Lifecycle](https://docs.spatius.ai/concepts/lifecycle.md), [SDK capability matrix](https://docs.spatius.ai/reference/sdk-capabilities.md)).
- **Global backend** — described in hiring copy as "全球多点部署、低延迟、自动扩缩容" with "监控、Tracing 、告警体系" built in Go ([V2EX 1173996](https://www.v2ex.com/t/1173996); 2025-11-20).

### Technical background sought

From the 2025-05 to 2026-02 job posts ([sov2ex index](https://www.sov2ex.com/api/search?q=spatialwalk&size=20)):

- **Required** — Go, Python or Node.js backend work with API design; Swift with UIKit/SwiftUI, GCD and Concurrency for iOS; Kotlin/Java with the Android framework, threading and memory models; Vue.js for the frontend internship; Docker, Linux and cloud-native operations for the backend roles; designing "对外 SDK" (public-facing SDKs) with attention to interface design.
- **Preferred** — distributed and high-concurrency systems; Kubernetes, gRPC, Redis, Kafka; mobile graphics (Metal, OpenGL ES, Vulkan) and shader work; audio/video and WebRTC; prior digital-human, VR/AR projects; research familiarity with 3DGS or NeRF; open-source projects or a technical blog; experience at ByteDance, Tencent, Alibaba, Meituan, Google or Meta for the senior mobile role.
- Stated repeatedly across posts: "能快速使用 AI 工具实现自己的想法" and "Everybody codes 也是我们企业价值观的一部分"; enterprise Cursor and Claude Code are listed as provided tools ([V2EX 1161367](https://www.v2ex.com/t/1161367); 2025-09-23).

### Industry domain

The work sits on real-time avatar rendering and on-device inference for consumer-facing scenarios that the company names as education and tutoring, recruitment and interviewing, live streaming, smart terminals, in-vehicle systems, kiosks and AI hardware ([spatialwalk.cn](https://www.spatialwalk.cn/), [spatius.ai](https://www.spatius.ai/)). Two domain areas carry stated obligations rather than preferences:

- **Chinese personal-information compliance** — the customer-facing compliance guide cites the Personal Information Protection Law, Data Security Law and Cybersecurity Law, and sets out obligations including consent before SDK initialisation, guardian authorisation for users under 14, a 7-day cap on retaining minors' voice data, SDK upgrades within 30 days of release, and equal prominence for "Accept" and "Reject" ([合规接入指引](https://www.spatialwalk.cn/compliance-guide); last updated 2026-01-06).
- **Data handling in the Singapore-facing product** — audio "permanently deleted immediately upon completion of transcription", interaction transcripts kept 30 days via LiveKit, account data kept for the account's life plus 3 years, developer-uploaded photographs plus 30 days after deletion, payment records 7 years, and Standard Contractual Clauses for EEA/UK transfers ([Privacy Policy](https://www.spatius.ai/privacy-policy/); last updated 2026-04-22).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Base city | "深圳，远程" (Shenzhen, remote) in posts from 2025-08 onward; earlier posts in 2025-05 and 2025-06 said "base 北京（支持远程办公）" (Beijing, remote supported) | [V2EX 1153930](https://www.v2ex.com/t/1153930), [V2EX 1131126](https://www.v2ex.com/t/1131126) |
| Company self-description | "中美双总部创业公司" (China–US dual-headquartered startup) | [V2EX 1160643](https://www.v2ex.com/t/1160643); 2025-09-19 |
| Remote policy | Remote allowed, in several posts conditioned on performance or on ramp-up: "熟悉后可远程", "能力优秀者接受远程" | [V2EX 1153830](https://www.v2ex.com/t/1153830), [V2EX 1160643](https://www.v2ex.com/t/1160643) |
| Compensation | "薪资标准直接对标字节跳动 (ByteDance) 等大厂同职级级别"; "不逊大厂的薪资和远超大厂的期权"; no salary band published | [V2EX 1189876](https://www.v2ex.com/t/1189876), [V2EX 1175749](https://www.v2ex.com/t/1175749) |
| Equity | Options stated for strong performers and for senior roles | [V2EX 1153830](https://www.v2ex.com/t/1153830), [V2EX 1189876](https://www.v2ex.com/t/1189876) |
| Tools provided | "企业版 cursor ，claude code 等 AI 工具" | [V2EX 1161367](https://www.v2ex.com/t/1161367) |
| Juniors and interns | A full-time frontend internship was advertised on 2025-06-06 with a conversion path; several roles accept "本科及以上在读" (currently enrolled undergraduates or above) | [V2EX 1136977](https://www.v2ex.com/t/1136977), [V2EX 1153830](https://www.v2ex.com/t/1153830) |
| Working language | Not stated as a policy; the 2026-02 mobile post asks for "良好的英文阅读能力" (good English reading ability) and all job posts are written in Chinese, while product, documentation and support surfaces are in English | [V2EX 1189876](https://www.v2ex.com/t/1189876), [docs](https://docs.spatius.ai/getting-started.md) |
| Application channel | `hr@spatialwalk.net`, subject line "姓名+应聘岗位"; no careers page exists on any company site | [V2EX 1160643](https://www.v2ex.com/t/1160643); paths probed 2026-08-26 |

---

## Notes

### Not publicly disclosed

Searched on 2026-08-26 across the company's sites (`spatius.ai`, `spatialwalk.cn`, `spatialwalk.top`, `spatialreal.ai`), its documentation, its GitHub organisations, package registries, V2EX, the Internet Archive, and English and Chinese web search:

- **Funding amounts, round names, valuation and the investor list.** Only Impa Ventures is named, in its own post, without figures.
- **Chinese corporate registry details** for 空间漫步科技（深圳）有限公司 — incorporation date, legal representative, registered capital and shareholders were not retrieved; Tianyancha returned HTTP 419 and Qichacha's search is behind a Cloudflare challenge.
- **The ownership relationship** between SPATIALWALK PTE. LTD., 空间漫步科技（深圳）有限公司 and SpatialReal, Inc.
- **Headcount from the company itself.** LinkedIn's "11-50 employees" band is the only figure, and the same page lists only 5 employees on the platform.
- **A careers page.** `/careers`, `/jobs`, `/about`, `/company` and `/team` on `spatius.ai` all return the homepage rather than a distinct page (probed 2026-08-26); hiring runs through V2EX posts and `hr@spatialwalk.net`.
- **Security certifications.** "SOC II/GDPR compliance" appears as an Enterprise plan bullet on the pricing page; no certificate, audit report or trust page was found.
- **An engineering blog.** The 188 blog posts are product, comparison and buyer-guide content; no engineering post describes the model, training data or benchmark methodology behind the latency and bandwidth claims.
- **Sources that could not be read on 2026-08-26:** Crunchbase (HTTP 403), PitchBook (subscription-gated), LinkedIn member profiles (HTTP 999), `spatialwalk.net` (HTTP 418 to non-browser clients — the identical site was read at `spatialwalk.top`), `remote-info.cn` (domain does not resolve), and `web.archive.org` has no capture of `spatius.ai`, `spatialwalk.cn` or `spatialwalk.ai`.

### Inconsistencies across sources

- **Founding year.** The LinkedIn company page says "Founded: 2025"; the `spatialwalk` GitHub organisation was created 2024-05-23, `spatialwalk.net` was registered 2024-08-08, and the investor post places the founding at the Apple Vision Pro unveiling ([LinkedIn](https://www.linkedin.com/company/spatius-ai), [GitHub API](https://api.github.com/orgs/spatialwalk), [Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)). The Singapore entity itself was incorporated later, on 2025-07-21 ([RecordOwl](https://recordowl.com/company/spatialwalk-pte-ltd)).
- **Headquarters.** Singapore in the legal documents and on LinkedIn; Shenzhen in every job post since 2025-08 and in the Chinese entity's filings; San Jose, California in the `spatialreal.ai` footer; Beijing in the 2025-05 and 2025-06 job posts; "中美双总部" in the recruiting copy ([Terms](https://www.spatius.ai/terms-of-service/), [V2EX 1153930](https://www.v2ex.com/t/1153930), [spatialreal.ai](https://www.spatialreal.ai/), [V2EX 1131126](https://www.v2ex.com/t/1131126)).
- **Two live brands with different price cards.** `spatius.ai` and `spatialreal.ai` sell the same SDK at the same $19/$299 tiers but differ on included credits (Free 1,000 vs 500; Starter 20,000 vs 22,000), and neither site mentions the other ([Pricing](https://www.spatius.ai/pricing/), [spatialreal.ai](https://www.spatialreal.ai/)).
- **Per-minute price over time.** The investor post published "$0.003 / min" on 2025-10-31; the published Scale rate on 2026-08-26 is "$0.007 / min" ([Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk), [Pricing](https://www.spatius.ai/pricing/)).
- **Bandwidth figures.** "100 kbps" on the English site, "10–20KB/s" on the Chinese site, "~10–15 KB/s" in the documentation ([spatius.ai](https://www.spatius.ai/), [spatialwalk.top](https://spatialwalk.top/), [docs](https://docs.spatius.ai/concepts/how-it-works.md)).
- **Avatar creation input.** The current API takes a single still photograph; the Chinese marketing page still says "仅需 1 分钟真人视频素材，即可生成可驱动的超写实 3D 数字形象" (one minute of video) ([docs — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md), [spatialwalk.top](https://spatialwalk.top/)).
- **Platform availability.** The Chinese FAQ still reads "我们目前全面支持 iOS，Web及Android SDK将在11月上线", while Web, Android and Flutter SDKs have shipped and iOS, Android, Web and Flutter are documented as supported ([spatialwalk.top](https://spatialwalk.top/), [SDK capability matrix](https://docs.spatius.ai/reference/sdk-capabilities.md)).
- **The Chief Scientist listing.** The Chinese team page names Yudong Guo as 首席科学家; his own academic homepage lists no company affiliation ([spatialwalk.top](https://spatialwalk.top/), [yudongguo.github.io](https://yudongguo.github.io/)).

### Other

- **Three brands in three markets, in dated sequence.** `spatialwalk.net` (2024-08) carries the Chinese SpatialWalk site; `spatialreal.ai` (2025-11) carries an English SpatialReal site under a US entity; `spatius.ai` (2026-04) carries the current English Spatius site under the Singapore entity. The npm packages track the same sequence: `@spatialwalk/avatarkit` (2025-11 to 2026-04) then `@spatius/avatarkit` (2026-04 onward), and the older GitHub organisation's demo repository still links to `docs.spatialreal.ai` ([npm](https://registry.npmjs.org/@spatialwalk/avatarkit), [avatarkit-voice-agent-demo](https://github.com/spatialwalk/avatarkit-voice-agent-demo)).
- **A stated pivot.** Job posts from 2025-05 and 2025-06 describe "一家专注于 AI 和空间计算 的科技公司" (AI and spatial computing) based in Beijing; from 2025-08 the same account describes "实时互动 AI 数字形象技术" (real-time interactive AI avatars) based in Shenzhen ([V2EX 1131126](https://www.v2ex.com/t/1131126), [V2EX 1153930](https://www.v2ex.com/t/1153930)).
- **The public surface is heavily SEO-shaped.** 188 of the 210 URLs in the main sitemap are blog posts, and three further sitemaps carry 51 URLs each for comparisons, integrations and glossary pages; the blog includes head-to-head comparison pages against named competitors ([sitemap index](https://www.spatius.ai/sitemap-index.xml), [Spatius blog](https://www.spatius.ai/blog/)).
- **Both AI-crawler robots policies are permissive.** `spatius.ai` and `spatialwalk.cn` explicitly allow GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bytespider, CCBot and others ([robots.txt](https://www.spatius.ai/robots.txt); read 2026-08-26).
- **Observable adoption is small but non-zero.** 7,417 npm downloads in the trailing month for the current Web SDK, a 51-member Discord, and 1–3 GitHub stars on the SDK repositories, against the "10M+ interactions" claim on `spatialreal.ai` ([npm API](https://api.npmjs.org/downloads/point/last-month/@spatius/avatarkit), [Discord invite API (Spatius)](https://discord.com/api/v9/invites/9HGhZfHZh9?with_counts=true), [GitHub API](https://api.github.com/orgs/spatius-ai)).
- **The China region is served from a separate domain.** The `cn-beijing` console runs on `console.cn-beijing.spatialwalk.top` while `us-west` and `ap-northeast` consoles run on `spatius.ai` subdomains ([docs — Regions](https://docs.spatius.ai/api-reference/regions.md)).

---

## Resources

**Official**

- [spatius.ai](https://www.spatius.ai/) · [Pricing](https://www.spatius.ai/pricing/) · [Contact](https://www.spatius.ai/contact/) · [Blog](https://www.spatius.ai/blog/) · [robots.txt](https://www.spatius.ai/robots.txt) · [sitemap index](https://www.spatius.ai/sitemap-index.xml)
- [Terms of Service](https://www.spatius.ai/terms-of-service/) (effective 2026-04-26) · [Privacy Policy](https://www.spatius.ai/privacy-policy/) (last updated 2026-04-22)
- Documentation — [Welcome](https://docs.spatius.ai/getting-started.md) · [How It Works](https://docs.spatius.ai/concepts/how-it-works.md) · [Avatar](https://docs.spatius.ai/concepts/avatar.md) · [Client Lifecycle](https://docs.spatius.ai/concepts/lifecycle.md) · [Integrations](https://docs.spatius.ai/integrations/overview.md) · [SDK capability matrix](https://docs.spatius.ai/reference/sdk-capabilities.md) · [Regions](https://docs.spatius.ai/api-reference/regions.md) · [Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md) · [FAQ](https://docs.spatius.ai/resources/faq.md) · [llms.txt](https://docs.spatius.ai/llms.txt)
- Chinese sites (language: zh) — [spatialwalk.cn](https://www.spatialwalk.cn/) · [spatialwalk.top](https://spatialwalk.top/) · [合规接入指引](https://www.spatialwalk.cn/compliance-guide) (last updated 2026-01-06)
- Parallel English site — [spatialreal.ai](https://www.spatialreal.ai/)
- Customer story — [SayMei](https://www.spatius.ai/blog/saymei-ai-mandarin-tutor-spatius/) (2026-08-11) · [Product update](https://www.spatius.ai/blog/spatius-product-update-avatar-apis-faster-audio-production-ready-sdks/) (2026-08-22)
- Code and packages — [GitHub `spatius-ai`](https://api.github.com/orgs/spatius-ai) · [GitHub `spatialwalk`](https://api.github.com/orgs/spatialwalk) · [avatarkit-voice-agent-demo](https://github.com/spatialwalk/avatarkit-voice-agent-demo) · [iOS SDK releases](https://github.com/spatius-ai/avatarkit-ios-release/releases) · [npm `@spatialwalk/avatarkit`](https://registry.npmjs.org/@spatialwalk/avatarkit) · [npm search "spatius"](https://registry.npmjs.org/-/v1/search?text=spatius&size=20) · [npm downloads](https://api.npmjs.org/downloads/point/last-month/@spatius/avatarkit) · [pub.dev `avatar_kit`](https://pub.dev/packages/avatar_kit) · [Maven Central `ai.spatialwalk:avatarkit`](https://mvnrepository.com/artifact/ai.spatialwalk/avatarkit)
- Community — [Discord invite API (Spatius)](https://discord.com/api/v9/invites/9HGhZfHZh9?with_counts=true) · [Discord invite API (SpatialReal)](https://discord.com/api/v9/invites/dRSUTdPCjm?with_counts=true) · [LinkedIn company page](https://www.linkedin.com/company/spatius-ai)

**Investor and registry**

- [Impa Ventures — "IMPA Family | Our Investment in Spatial Walk"](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk) (2025-10-31) · [Impa Ventures](https://impa.ventures/)
- [RecordOwl — SPATIALWALK PTE. LTD. (ACRA data mirror)](https://recordowl.com/company/spatialwalk-pte-ltd)

**Job postings** (language: zh, all from `hr@spatialwalk.net`)

- [Index of 13 posts](https://www.sov2ex.com/api/search?q=spatialwalk&size=20) · [1131126 (2025-05-12)](https://www.v2ex.com/t/1131126) · [1132398 (2025-05-17)](https://www.v2ex.com/t/1132398) · [1136977 (2025-06-06)](https://www.v2ex.com/t/1136977) · [1153830 (2025-08-20)](https://www.v2ex.com/t/1153830) · [1153930 (2025-08-21)](https://www.v2ex.com/t/1153930) · [1160643 (2025-09-19)](https://www.v2ex.com/t/1160643) · [1161367 (2025-09-23)](https://www.v2ex.com/t/1161367) · [1173996 (2025-11-20)](https://www.v2ex.com/t/1173996) · [1175749 (2025-11-28)](https://www.v2ex.com/t/1175749) · [1189876 (2026-02-01)](https://www.v2ex.com/t/1189876)

**Third-party profiles and academic sources**

- [yudongguo.github.io](https://yudongguo.github.io/) · [SadTalker project page](https://sadtalker.github.io/) · [GitHub — OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker)
- [iTunes search API — no first-party app in the US storefront](https://itunes.apple.com/search?term=spatius&entity=software&country=us&limit=5)
- [Baidu Baike — 空间漫步传媒科技（深圳）有限责任公司 (unrelated name collision, language: zh)](https://baike.baidu.com/item/%E7%A9%BA%E9%97%B4%E6%BC%AB%E6%AD%A5%E4%BC%A0%E5%AA%92%E7%A7%91%E6%8A%80%EF%BC%88%E6%B7%B1%E5%9C%B3%EF%BC%89%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/24226245)
