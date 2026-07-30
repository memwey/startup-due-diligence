# Eazo

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-30.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Eazo is a consumer platform for AI apps and agents operated by `ASI X Inc.`, a Delaware-registered company whose website footer reads "Made with ♥︎ in San Francisco" ([homepage](https://eazo.ai/); Undated; accessed 2026-07-30). It has three published surfaces: a mobile app for discovering, using and remixing creator-made AI apps ([App Store](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137), first released 2026-03-28); `Eazo Creator`, a no-code full-stack builder that scaffolds and deploys those apps ([creator.eazo.ai](https://creator.eazo.ai/); accessed 2026-07-30); and `Eazo Anima`, a developer infrastructure product for agent identity, memory and web action ([anima.eazo.ai](https://anima.eazo.ai/); accessed 2026-07-30). The same legal entity `ASI X Inc.` is named in the legal pages of the Fellou agentic browser ([Fellou Terms](https://fellou.ai/terms/), [Fellou Privacy Policy](https://fellou.ai/policy/); Effective 2026-02-01) — see `Identity and legal entities`.

- No funding round has been announced by the company for either the Eazo or Fellou brand in the reviewed public sources as of 2026-07-30. Third-party databases conflict: a PitchBook profile is reported to state US$40.4M raised with LongRiver Investments as an investor, while [Tracxn](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw) states the company is "Unfunded" — see `Notes`.
- Distribution is early: Google Play shows "50+ Downloads" and In-app purchases for `ai.eazo.portal` ([Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal); accessed 2026-07-30), and the App Store listing shows 15 ratings averaging 4.5 ([iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us); accessed 2026-07-30).
- The largest publicly documented activity is the EAZO Global Hackathon on 2026-05-23/24 across San Francisco (Mountain View), New York and Shanghai plus online, with a stated US$300,000 prize pool, 253 prize slots and a scoring split of 50% platform user votes, 40% expert panel, 10% peer review ([archived hackathon page, captured 2026-05-19](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)).
- Team size is not published. The careers page states "We're a team across the San Francisco Bay Area and Singapore" and lists three roles — Agent Engineer, Growth, Design Engineer — plus a talent community ([careers](https://eazo.ai/careers); Undated; accessed 2026-07-30). "Yang, Founder & CEO of Eazo" is the only person named on the site ([about](https://eazo.ai/about)).
- Engineering evidence comes from public assets rather than a stack page: the marketing site is served by Express behind Cloudflare, `Eazo Creator` is a Vite SPA behind nginx, `Eazo Anima` is Next.js with VitePress docs, the Android APK is served from Amazon S3 through CloudFront, and `eak.eazo.ai` sits behind an AWS load balancer (response headers observed 2026-07-30). The public [eazo-creator-nextjs-template](https://github.com/EazoAI/eazo-creator-nextjs-template) documents the app runtime as Next.js 16 / React 19 / Bun / Drizzle ORM on PostgreSQL, with platform AI "rout[ed] through AWS Bedrock via the Eazo AI gateway" and `deepseek.v3.1` as the default model ([AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md); accessed 2026-07-30).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | Eazo (styled EAZO in page titles) | [homepage](https://eazo.ai/); Undated; accessed 2026-07-30 |
| Legal name | ASI X Inc. | [Platform Service Terms](https://eazo.ai/terms-of-service); Effective 2026-02-01 |
| Registered address | 251 Little Falls Drive, Wilmington, New Castle, DE 19808 | [Privacy Policy, EEA+ Addendum](https://eazo.ai/privacy-policy); Effective 2026-02-01 |
| Stated origin | "Made with ♥︎ in San Francisco by ASI X Inc." | [homepage footer](https://eazo.ai/); Undated; accessed 2026-07-30 |
| Team locations | "a team across the San Francisco Bay Area and Singapore" | [careers](https://eazo.ai/careers); Undated; accessed 2026-07-30 |
| Developer contact on Google Play | ASI X Inc, `media@fellou.ai`, 251 Little Falls Dr, Wilmington, DE 19808-1674, +1 702-245-1490 | [Google Play "About the developer"](https://play.google.com/store/apps/details?id=ai.eazo.portal); accessed 2026-07-30 |
| Representative named on the site | "Yang", Founder & CEO of Eazo | [about](https://eazo.ai/about); Undated; accessed 2026-07-30 |
| Headcount | Not published | see `Notes` |
| Domains covered by the privacy policy | `eazo.ai`; `eazo.online` | [Privacy Policy](https://eazo.ai/privacy-policy); Effective 2026-02-01 |
| Public contacts | `team@eazo.ai` (contact), `hi@eazo.ai` (arbitration opt-out and dispute notice), `privacy@eazo.ai` (data rights), `media@eazo.ai` (app support) | [homepage footer](https://eazo.ai/), [Terms clause 10.4](https://eazo.ai/terms-of-service), [Privacy Policy](https://eazo.ai/privacy-policy), [Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal) |
| Community channels | Discord, X (`@EazoAI`), TikTok (`@eazoai`) | [homepage footer](https://eazo.ai/); Undated; accessed 2026-07-30 |
| iOS app | `ai.eazo.portal`, "Eazo: Discover AI Apps, Agents", first released 2026-03-28, version 0.2.23 on 2026-07-29, Lifestyle, 12+, English only, min iOS 16.0, 15 ratings averaging 4.47 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us); accessed 2026-07-30 |
| Android app | `ai.eazo.portal`, updated 2026-07-28, Communication category, "50+ Downloads", In-app purchases, Teen rating | [Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal); accessed 2026-07-30 |
| Direct APK | `cdn.eazo.ai/mobile/eazo.apk`, 211,453,650 bytes, `last-modified` 2026-06-25 | response headers observed 2026-07-30 |
| GitHub organisation | `EazoAI`, created 2026-02-11, 5 public repositories, no public members | [GitHub API](https://api.github.com/orgs/EazoAI); accessed 2026-07-30 |
| npm organisation | `@eazo`, 4 packages: `sdk`, `eak`, `auth`, `node-sdk`, all MIT | [npm registry search](https://registry.npmjs.org/-/v1/search?text=eazo); accessed 2026-07-30 |
| Data transfer locations | "third parties in locations including the United States, Japan and Singapore" | [Privacy Policy, EEA+ Addendum](https://eazo.ai/privacy-policy); Effective 2026-02-01 |

**Events and partners**: Eazo ran the EAZO Global Hackathon on 2026-05-23/24. The archived event page names Shanghai's in-person venue as 上海创新创意设计研究院 (DIIS), 虹口区东长治路505号 ([archived 2026-05-19](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)). The San Francisco Luma page lists the co-hosting organisations as "Eazo.ai · Corgi · Streaml · Gen · Photon · AI Valley", and states the event "is in partnership with the Gen AI Foundry", describing Gen Digital as a company with "trusted consumer brands including Norton, Avast, LifeLock, MoneyLion" ([Luma, Silicon Valley](https://luma.com/frw43jmv); accessed 2026-07-30).

**Market context as stated by the company**: the post [You Were Born to Be Powerful (2026-01-26)](https://eazo.ai/blog/you-were-born-to-be-powerful) frames the company's position as "All tech elites are building Agents for elites. We're building Agents for everyone", contrasts "deep research reports, data analysis, industry surveys, market insights" against everyday tasks, and describes Eazo as "InternetOS, your operating system for the internet". The [about page](https://eazo.ai/about) states the mission as being a "Smart Life Gateway", the vision as "Make Agent a way of life", and lists five values.

### Identity and legal entities

| Name | Type | Jurisdiction indicated | Relationship | Source |
|---|---|---|---|---|
| Eazo / EAZO | Public brand | — | Name used across the site, apps, docs, npm scope and GitHub organisation | [homepage](https://eazo.ai/) |
| ASI X Inc. | Legal entity named as contracting party and data controller | Delaware, United States (registered address given) | Stated operator of the Eazo services | [Terms](https://eazo.ai/terms-of-service), [Privacy Policy](https://eazo.ai/privacy-policy) |
| Fellou | Separate public brand (agentic browser) and the `Eko` framework | — | Fellou's own Terms and Privacy Policy name `ASI X Inc.` as the same contracting party and data controller, at the same registered address | [Fellou Terms](https://fellou.ai/terms/), [Fellou Privacy Policy](https://fellou.ai/policy/) |
| Eazo Anima / EAK | Product brand | — | "Eazo Anima (EAK)" per the docs; `eak.eazo.ai` redirects to `anima.eazo.ai` | [Quickstart](https://anima.eazo.ai/docs/guides/quickstart), redirect observed 2026-07-30 |
| Eazo Technology Co., Ltd. | Company with a similar name on LinkedIn | Not established | No connection to ASI X Inc. found in the reviewed sources; recorded here so the name is not mistaken for the same company | [LinkedIn](https://www.linkedin.com/company/eazo-technology) |

The Eazo–Fellou relationship rests on first-party evidence from both sides. Fellou's legal pages name `ASI X Inc.` and the same Wilmington address as Eazo's ([Fellou Privacy Policy](https://fellou.ai/policy/)). Google Play's verified "About the developer" block for the Eazo app gives the developer email as `media@fellou.ai` ([Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal); accessed 2026-07-30). All four `@eazo` npm packages are maintained by three accounts whose registry emails are `zhuowei@fellou.ai`, `liaochangjiang@fellou.ai` and `suntianxiang@fellou.ai` ([npm registry](https://registry.npmjs.org/@eazo%2Fsdk); accessed 2026-07-30). A post from the `@FellouAI` X account promotes the Eazo hackathon and tags `@EazoAI` ([X, 2026-05](https://x.com/FellouAI/status/2054356197491273795)); `x.com` blocked automated access on 2026-07-30, so the post text is taken from a search-result title and is unconfirmed. Neither brand's marketing pages mention the other; only the legal, store-listing and package-registry surfaces connect them.

`Authing` and `GenAuth` are a separate, unresolved relationship. Eazo's identity layer is named `GenAuth` ([GenAuth docs](https://anima.eazo.ai/docs/genauth/)), the `@eazo/auth` package is described as handling "Web (GenAuth OIDC/JWT)" and depends on `authing-js-sdk` with keywords including both `genauth` and `authing` ([npm](https://registry.npmjs.org/@eazo%2Fauth); accessed 2026-07-30), the SDK changelog refers to "the Authing OAuth popup" ([CHANGELOG 0.21.0](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)), and a separate identity platform operates at [genauth.ai](https://www.genauth.ai/). No reviewed Eazo page states whether `GenAuth` is Eazo's own component, a third-party product, or a shared brand. See `Notes`.

---

## Product

The homepage headline is "Discover what agents can do for your life." with the subhead "Discover agents built by creators. Make them your own — or build the next one." Its navigation has three entries: Home, Creator (`creator.eazo.ai`) and Developer (`eak.eazo.ai`) ([homepage](https://eazo.ai/); Undated; accessed 2026-07-30). The footer tagline is "DISCOVER. SHARE. USE. REMIX."

### Surfaces

| Surface | Status shown | What it is | Source |
|---|---|---|---|
| Eazo Mobile | Live on iOS and Android | Consumer app to "Discover", "Use instantly", "Remix" and "Build & share" AI apps, agents, chatbots and assistants made by creators | [App Store description](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137) |
| Eazo Creator | Live behind login | No-code full-stack builder; the login-gated SPA at `creator.eazo.ai` redirects to `eazo.ai/creator/` | [creator.eazo.ai](https://creator.eazo.ai/); accessed 2026-07-30 |
| Eazo Anima (EAK) | "currently in private build"; waitlist and early-access form | Managed agent infrastructure: `GenAuth` (identity), `GUMem` (memory), `Web Agent` (action), plus email and audit trails | [anima.eazo.ai](https://anima.eazo.ai/), [early access](https://anima.eazo.ai/early-access); accessed 2026-07-30 |
| Eazo Anima Docs | Published | Bilingual (EN / 简体中文) VitePress documentation with quickstart, 15 use-case guides, API surface and security pages | [docs](https://anima.eazo.ai/docs/); accessed 2026-07-30 |
| Eazo Anima pricing | "Pricing · Coming soon" | States "GenAuth, GUMem, and Web Agent are running in production — the numbers behind them aren't final yet"; last revision given as "2026 · Q2" | [pricing](https://anima.eazo.ai/pricing); accessed 2026-07-30 |

### Eazo Creator, as described in first-party material

The [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) (Chinese, captured 2026-05-19) describes Creator around three steps — BUILD ("生产级的 UI"), DEPLOY ("全栈自动化部署，一行代码不用写"), PUBLISH ("一键直达 Eazo 社区") — and states the promise as "所思即所得，生产即上线". A third-party advertising placement dated [2026-05-18](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/) and labelled "Third-Party Advertising" additionally describes six parallel AI-generated design directions, automated QA testing and bug fixing, "Database, authentication, AI capabilities, API endpoints — all platform-managed", and a community-shareable skills ecosystem.

The public template repository documents the generated app's capability surface as the `@eazo/sdk` modules `auth`, `device`, `ai`, `storage`, `memory` and `notifications`, plus a server-side `requireAuth` guard and `notifications.publish` ([AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md); accessed 2026-07-30). Notable documented behaviours:

- `ai` is server-side only and, in the default `EAZO_AI_PROVIDER_MODE=eazo` mode, calls Creator's `/api/app-ai/chat` proxy "so official Eazo model usage is charged to the app creator's credits"; a `byok` mode calls a creator-supplied OpenAI-compatible provider instead ([AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)).
- `memory.reportAction()` writes user action events to "the Gum memory service — a persistent, semantically searchable log of what users did in your app" ([AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)). Since `@eazo/sdk` 0.21.0 (2026-06-11) the call is gated on an app author's `sendAnonymousData` consent flag read from `GET /api/apps-open/:appId`, enforced again server-side at `POST /api/open/gum/action` ([CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)).
- `share.compose()` hands text and up to four image attachments to the host, which "AI-drafts a post from the inputs"; in a plain browser it shows a "Continue in the Eazo app" CTA ([SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md)).
- Apps opened on the web get a top handoff banner carrying app identity, a likes/comments rail, and "Remix" plus "Open in Eazo" CTAs; Remix falls back to `creator.eazo.ai` when the app does not open ([CHANGELOG 0.21.0](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)).

### Commercialization

The Terms describe a creator-monetization system rather than a subscription price list; no public price list for Eazo Mobile, Eazo Creator or Eazo Anima was found ([Terms § 3.5](https://eazo.ai/terms-of-service); Effective 2026-02-01).

| Item | Detail | Source |
|---|---|---|
| What is charged | "In-App Charges" — paid features, paid access, subscriptions, one-time purchases or usage-based charges levied on end users of a creator's app or agent | [Terms § 3.5.1](https://eazo.ai/terms-of-service) |
| Collection models | Creators must designate one, confirmed by Eazo: (A) Platform Collects, (B) Creator Collects, (C) Credits/Hybrid Settlement | [Terms § 3.5.1](https://eazo.ai/terms-of-service) |
| Platform fee | Eazo and/or its payment providers "may deduct … a platform fee and/or commission at the rate(s) displayed in the relevant Service interface"; the rate is not published | [Terms § 3.5.2](https://eazo.ai/terms-of-service) |
| Creator payouts | "Creator Earnings" tracked in an "Earnings Balance" ledger; Withdrawals require KYC, tax information, AML/CTF and sanctions screening, a minimum amount and a holding period | [Terms § 3.5.3](https://eazo.ai/terms-of-service) |
| Payment providers | "We use Stripe and/or other service providers"; under Model B the creator is merchant of record via their own account, "e.g. a Stripe Connect connected account" | [Terms § 3.5.4, § 3.5.9](https://eazo.ai/terms-of-service) |
| Credits | Under Model C end users buy credits from Eazo; credits "have no cash value outside the Services … may expire, and … are non-refundable", and Eazo may adjust credit-to-earnings and model-cost rates with notice | [Terms § 3.5.10](https://eazo.ai/terms-of-service) |
| Automatic refunds | "in the event of a generation failure or if your User App or Agent does not pass our review process, any In-App Charges or credits consumed during that process will be automatically refunded" | [Terms § 3.5.7](https://eazo.ai/terms-of-service) |
| Liability cap toward creators | Capped at "the Platform Fees actually received by Eazo from your In-App Charges during the twelve (12) months preceding the event" | [Terms § 3.5.13](https://eazo.ai/terms-of-service) |
| Creator-side AI cost | Default mode charges official Eazo model usage to the app creator's credits | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| Anima billing signals | API errors include `insufficient_credits` and `budget_exceeded`; limits include "per-project monthly credit budget — soft warning at 80%, hard stop at 100%" | [WebAgent API overview](https://anima.eazo.ai/docs/webagent/reference/) |
| Anima early access | "Early-access teams pay nothing during calibration" | [pricing](https://anima.eazo.ai/pricing) |

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2026-03-28 | iOS app first released | [iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us) |
| 2026-05-18 | "over 1,000 builders have already signed up" for the hackathon | [Stanford Daily, Third-Party Advertising](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/) |
| 2026-05 | "1000+ creators have already signed up for EAZO Global Hackathon" — from a search-result title; unconfirmed, `x.com` blocked automated access | [X, @FellouAI](https://x.com/FellouAI/status/2054356197491273795) |
| 2026-05-23/24 | Luma attendance recorded as "303 Went" (Silicon Valley) and "176 Went" (New York) | [Luma SV](https://luma.com/frw43jmv), [Luma NY](https://luma.com/ay4dy8o5) |
| Accessed 2026-07-30 | Google Play "50+ Downloads"; App Store 15 ratings, 4.47 average | [Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal), [iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us) |

No user, creator, app-catalog, revenue or transaction figure is published by the company for Eazo Mobile or Eazo Creator — see `Notes`.

### EAZO Global Hackathon 2026

| Item | Detail | Source |
|---|---|---|
| Dates and format | 2026-05-23/24, 48 hours, in-person plus online; billed as "全球首场『零代码』全栈黑客松" | [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| Locations | San Francisco (Mountain View), New York, Shanghai (DIIS, 虹口区东长治路505号), plus global online folded into the Shanghai or San Francisco region | [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon), [Luma SV](https://luma.com/frw43jmv) |
| Prize pool | US$300,000 total, 253 prize slots: global US$90,000 (Grand US$50,000, People's Choice US$25,000, Builder's Choice US$15,000); regional 20 teams per region across three regions; special awards US$90,000; a "D+7" growth award of US$35,000 seven days after the ceremony | [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| Regional prize pool (New York) | "NYC regional prize pool: $17,000 total" | [Luma NY](https://luma.com/ay4dy8o5) |
| Scoring | 50% Eazo platform user votes, 40% a six-member expert panel (2 investors, 2 AI founders, 1 coding-agent expert, 1 design-agent expert), 10% peer review; five equally weighted criteria at 20% each | [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| Submission requirement | Submissions must be live, publicly usable products, not prototypes or demos; hard deadline 2026-05-24 07:00 local, top 30 teams advance to Demo Day | [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| Tracks | 超级家长 (family), AI 陪伴 (companionship, explicitly including ADHD/ASD-oriented apps), 人生操作系统 (personal productivity), 身体智能 (health and body), 自由创意 (open) | [archived hackathon page](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon) |
| Registration and rules | Registration via Tally forms and Luma; rules and terms hosted on Google Drive; a separate voting site at `hackathon2026.eazo.dev` (Vercel-hosted, client-rendered) | [Luma NY](https://luma.com/ay4dy8o5), [hackathon2026.eazo.dev](https://hackathon2026.eazo.dev/) |
| Post-event status | The company's own `eazo.ai/hackathon` page now returns HTTP 404 and the Devpost listing returns HTTP 410 Gone; no winners announcement was found | paths checked 2026-07-30; [Devpost](https://eazo-ai-hackathon.devpost.com/) |

The hackathon write-up [We Ran a Different Kind of Hackathon (2026-05-02)](https://eazo.ai/blog/we-ran-a-different-kind-of-hackathon) states the premise as "No code. 48 hours. Three cities. One moment." and that submissions "live on the platform, discovered and used by real people".

### Stated plans

The [careers page](https://eazo.ai/careers) states "We're creating InternetOS, a system of agents that live in daily life, work alongside you, and quietly expand what you're capable of", and "We're just getting started, and there's still room to shape what this company becomes". [Eazo Anima](https://anima.eazo.ai/) states it is "building toward a web where we make Agents first-class citizens of the Web, with their own identity, inspectable memory, delegated authority, and replayable actions", and that identity, memory, web execution, email and audit trails are "currently in private build". The [pricing page](https://anima.eazo.ai/pricing) gives the next milestone as "Public pricing → talk to sales for an ETA".

---

## Founder

**Yang** — "Founder & CEO of Eazo", quoted on the about page: "We believe AI is a mirror to the human mind—designed to Learn more, Know more, and Be more. By bringing Capability Equality to everyone, we empower you to navigate a complex world. We never stop." ([about](https://eazo.ai/about); Undated; accessed 2026-07-30). No surname, career history, education or founding date appears on any Eazo page.

Three external sources point to the same person. The Luma page for Eazo's own Silicon Valley hackathon is "Hosted by Yang Xie", linking to Luma user `dominic0` and X handle `@dominicy0`, with `eazo.ai` listed as a hosting organisation ([Luma](https://luma.com/frw43jmv); accessed 2026-07-30). A LinkedIn profile at `linkedin.com/in/ivydom/` is indexed as "Yang Xie - ASI X"; the page returned HTTP 999 to automated access on 2026-07-30 and was not read directly. Fellou — whose legal pages name the same entity `ASI X Inc.` — is attributed in media to founder Yang Xie / 谢扬: [GlobeNewswire (2025-08-12)](https://www.globenewswire.com/news-release/2025/08/12/3131385/0/en/Fellou-Announces-Next-Generation-Agentic-AI-Browser-Transforming-the-Future-of-Work.html) describes Fellou as "co-founded by 2021 Forbes U30 Asia honoree Yang Xie".

That Eazo's "Yang" is Yang Xie is researcher inference from the hackathon host name, the LinkedIn indexing and the shared legal entity; no Eazo page states it.

Career facts reported for Yang Xie in third-party coverage, none of them from an Eazo or ASI X source: founder of the identity platform Authing, founded 2019, described in 2024 as serving more than 700 customers ([Sina Tech / 创事记, 2025-04-21](https://finance.sina.com.cn/tech/csj/2025-04-21/doc-inetwzpw8763926.shtml)); prior work at ByteDance ([APT401 Substack](https://apt401.substack.com/p/the-browser-that-acts-how-fellou)); selected for Forbes 30 Under 30 Asia in 2021 ([GlobeNewswire, 2025-08-12](https://www.globenewswire.com/news-release/2025/08/12/3131385/0/en/Fellou-Announces-Next-Generation-Agentic-AI-Browser-Transforming-the-Future-of-Work.html)). A long-form interview exists as a podcast episode, ["与Fellou创始人谢扬的3小时访谈" (ZH)](https://podcasts.apple.com/cn/podcast/34-%E4%B8%8Efellou%E5%88%9B%E5%A7%8B%E4%BA%BA%E8%B0%A2%E6%89%AC%E7%9A%843%E5%B0%8F%E6%97%B6%E8%AE%BF%E8%B0%88-%E5%AD%A4%E7%8B%AC-95%E5%90%8E-%E7%89%8C%E6%A1%8C%E4%B8%8E%E7%94%9F%E4%BA%A7%E5%8A%9B%E7%9A%84%E5%AE%8C%E7%BE%8E%E5%88%9B%E4%B8%9A/id1754955836?i=1000704842263).

Other people appearing in Eazo's public material are co-hosts and judges of the hackathon rather than stated employees. The Silicon Valley Luma page lists eleven hosts including Yang Xie, Lyn Zhang, NingNing, Laura Dang, Vivian Cai, Krypton M., Ryan Foo, Yuna Chu and bojun sheng, alongside the AI Valley account ([Luma](https://luma.com/frw43jmv)). The New York page names judges including Donnie D'Amato and Nuoran ([Luma NY](https://luma.com/ay4dy8o5)). No team, leadership or about-the-people page exists on `eazo.ai`, and the two blog posts are attributed to "Eazo Team".

The three npm maintainer accounts behind the `@eazo` packages publish under the registry emails `zhuowei@fellou.ai`, `liaochangjiang@fellou.ai` and `suntianxiang@fellou.ai`, with account names `luozhuowei`, `liaochangjiang_fellou` and `lucsun-fellou` ([npm](https://registry.npmjs.org/@eazo%2Fsdk); accessed 2026-07-30). No Eazo page connects those accounts to named roles.

---

## Funding

No financing announcement by the company was found for the Eazo brand, the Fellou brand or `ASI X Inc.` in the reviewed public sources as of 2026-07-30. The table records what third-party sources state.

| Date | Round (as named in the source) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Undated; accessed 2026-07-30 | Not named | Reported as US$40.4M | LongRiver Investments | Reported as US$40.4M | [PitchBook profile for Fellou](https://pitchbook.com/profiles/company/894665-44) — page returned HTTP 403 to automated access; figures taken from search-result snippets and therefore unconfirmed |
| Undated; accessed 2026-07-30 | "Unfunded" — "Fellou has not raised any funding rounds yet" | None | None listed | None | [Tracxn profile for Fellou](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw) |
| 2026-07-07 | Not a round; a status claim | — | — | — | [36Kr (ZH)](https://36kr.com/p/3884772932792581): "Fellou后续遇到融资困难，难以为继。" ("Fellou subsequently encountered financing difficulties and was unable to continue.") The article gives no source for the statement |

Both database figures describe the Fellou brand, not the Eazo brand. Neither was confirmed against a primary source, and the two contradict each other — see `Notes`. Investor participation, round names, valuation and any Eazo-specific raise are not established by any source reviewed.

Third-party material dated after the 36Kr statement describes ASI X Inc. continuing to ship under the Eazo brand: `@eazo/sdk` 0.22.3 published 2026-07-28 ([npm](https://registry.npmjs.org/@eazo%2Fsdk)), the Android app updated 2026-07-28 ([Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)), the iOS app updated 2026-07-29 ([iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)), and a push to `eazo-creator-nextjs-template` on 2026-07-29 ([GitHub](https://github.com/EazoAI/eazo-creator-nextjs-template)). The careers page carries three open roles offering "Top-of-market salary + equity" ([careers](https://eazo.ai/careers); Undated; accessed 2026-07-30). These are dated observations, not a funding position.

---

## Engineering

### Technology stack and platforms

No stack page is published. Items are confirmed by observable public assets or first-party public repositories unless labelled otherwise.

- **Hosting and edge (confirmed by response headers observed 2026-07-30):** `eazo.ai` returns `x-powered-by: Express` with server-rendered HTML; `eazo.ai/creator/` is served by `nginx/1.27.5` as a Vite-built SPA whose assets load from `assets.eazo.ai`; `anima.eazo.ai` returns `x-powered-by: Next.js` with `x-nextjs-cache` / `x-nextjs-prerender`; `eak.eazo.ai` responds with `server: awselb/2.0` and 302-redirects to `anima.eazo.ai`; `cdn.eazo.ai` serves the APK from `AmazonS3` through `CloudFront` with `x-amz-server-side-encryption: AES256`; `api.eazo.ai`, `docs.eazo.ai` and `status.eazo.ai` resolve through Cloudflare but return HTTP 404; `hackathon2026.eazo.dev` returns `server: Vercel`.
- **Documentation:** VitePress, bilingual EN / 简体中文, at `anima.eazo.ai/docs/` ([docs](https://anima.eazo.ai/docs/); accessed 2026-07-30).
- **Generated app runtime (confirmed by the public template):** Next.js 16.2.4 App Router, React 19.2.4, TypeScript, Tailwind CSS v4, Bun 1.3.9, shadcn/ui, `@base-ui/react`, lucide-react, framer-motion, Drizzle ORM 0.45 with `postgres.js` against PostgreSQL, `i18next` / `react-i18next` for `en-US` and `zh-CN`, `zod`, and `@modelcontextprotocol/sdk` ([package.json](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/package.json), [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md)). The template's i18n stack is described as "same stack as Eazo Creator frontend".
- **Model access (confirmed by the public template):** platform AI "routes through AWS Bedrock via the Eazo AI gateway"; the documented default model key is `deepseek.v3.1`, and the published list of supported keys covers DeepSeek v3.1/v3.2, OpenAI `gpt-oss` and `gpt-oss-safeguard` (20b/120b), Qwen3 (including `qwen3-vl-235b-a22b-instruct` and coder variants), Mistral Ministral/Magistral/Devstral/Voxtral and `mistral-large-3-675b-instruct`, Google Gemma 3, NVIDIA Nemotron, MiniMax M2 family, Moonshot Kimi K2, Z.ai GLM 4.6/4.7/5, and Writer Palmyra Vision ([AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md); accessed 2026-07-30). The wrapper "uses OpenAI-compatible request/response shapes".
- **Authentication and session crypto (confirmed by published packages):** `@eazo/node-sdk` is described as "Decrypt encrypted data using ECC secp256k1 + AES-256-GCM" and depends on `elliptic`; `@eazo/auth` handles "Eazo Mobile (encrypted session) and Web (GenAuth OIDC/JWT)" and depends on `jose`, `elliptic` and `authing-js-sdk`; `@eazo/sdk` depends on `authing-js-sdk`, `elliptic`, `openai`, `qrcode-generator` and `@radix-ui/react-dialog`; server-side notification publishing "Authenticates by signing an ES256K JWT with `EAZO_PRIVATE_KEY`" ([npm](https://registry.npmjs.org/@eazo%2Fsdk), [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md)).
- **Analytics and tooling observed in deployed pages:** Google Analytics `gtag.js` (`G-EXPH819QL6` on `eazo.ai`, `G-V1CNGB211P` on `eazo.ai/creator/`); the Creator runtime config declares `VITE_AUTHING_*`, `VITE_POSTHOG_KEY`, `VITE_POSTHOG_HOST` and `VITE_ANALYTICS_API_BASE` keys, indicating Authing and PostHog integration points (values empty in the public file) ([creator-runtime-config.js](https://eazo.ai/creator/creator-runtime-config.js); accessed 2026-07-30). Application forms use Tally; events use Luma; the hackathon rules were distributed via Google Drive.
- **Anima API surface (confirmed by the published OpenAPI document):** the spec at `anima.eazo.ai/docs/openapi/v1.json` declares OpenAPI 3.1.0, title "WebAgent Backend", version 0.2.4, and 125 paths, of which 47 are under `/api/admin` (accessed 2026-07-30). Documented base URL is `https://api.eak.eazo.ai` with Bearer keys prefixed `wa_`, cursor pagination capped at 100 per page, and an optional `Idempotency-Key` header ([API overview](https://anima.eazo.ai/docs/webagent/reference/)).
- **SDK distribution:** TypeScript package `@eazo/eak` (15 versions, 2026-06-02 to 2026-06-18) and `@eazo/sdk` (27 versions, 2026-04-22 to 2026-07-28), both MIT ([npm](https://registry.npmjs.org/@eazo%2Feak), [npm](https://registry.npmjs.org/@eazo%2Fsdk); accessed 2026-07-30). The docs also reference a Python package `eazo-eak` ([Quickstart](https://anima.eazo.ai/docs/guides/quickstart)); `pypi.org/pypi/eazo-eak/json` returned HTTP 404 on 2026-07-30 — see `Notes`.
- **Hiring-only mentions**, from the careers page and not otherwise confirmed in production: knowledge graphs, vector retrieval, memory compression, LangGraph, "Agent SDKs", and "Deep understanding of React or V8 JavaScript Engine" ([careers](https://eazo.ai/careers); Undated; accessed 2026-07-30). A requirement in a posting does not establish current use.

### Systems

| System | What it does | Source |
|---|---|---|
| Eazo Mobile host bridge | A `postMessage` bridge between embedded web apps and the native shell: native login UI, share/compose handoff, per-app push subscription, device context and locale | [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| Encrypted session handoff | The host issues an encrypted user token; the app's server decrypts it with an ECC private key and returns the user profile | [template README](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/README.md) |
| App scaffolding and deployment | Platform-stamped environment (app id, title/description, AI provider mode) and one-click deployment of full-stack apps; the platform supplies its own SDK package spec instead of the public npm source | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md), [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| AI gateway and creator billing | Proxy at `/api/app-ai/chat` that meters official model usage against the creator's credits, with a BYOK bypass | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| Marketplace payments | SDK-owned checkout, status polling, entitlement refresh and a payment ledger; Stripe returns with a `payment_id` that the SDK polls against "the Eazo ledger"; generated apps are told not to add Stripe SDKs, webhooks or secret keys | [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| Push notification fan-out | Per-(user, app) subscription bit written through the host; server-side `notifications.publish` fans out to subscribers, with a documented 413 error above 5,000 subscribers | [SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md) |
| Gum / GUMem memory service | Stores conversation, behaviour and profile memory in a layered `ActionLogs / Messages → Facts → Summaries → Topics` hierarchy with hybrid vector + graph storage, task-scoped recall, webhooks and lifecycle deletion | [GUMem overview](https://anima.eazo.ai/docs/gumem/getting-start/overview/), [anima.eazo.ai](https://anima.eazo.ai/) |
| GenAuth delegated authorization | Issues short-lived `grantToken`s carrying `userId`, `agentKey`, allowed and denied scopes, expiry and an `auditId`; provides an identity gateway, MCP Hub Profiles, audit trail and a `genauth-cli` | [GenAuth overview](https://anima.eazo.ai/docs/genauth/), [security guide](https://anima.eazo.ai/docs/guides/security) |
| Web Agent execution plane | Session/run model over a controlled browser sandbox with a `DoAnything` API, shaped `DeepResearch`, `WebSearch` and `Track` APIs, SSE event streams, ReAct traces, browser video frames, screenshots, recordings, pause/resume/intervene, saved site logins and profiles, and monitor deliveries with retry | [WebAgent overview](https://anima.eazo.ai/docs/webagent/), [OpenAPI 3.1 spec](https://anima.eazo.ai/docs/openapi/v1.json) |
| MCP server in generated apps | Streamable HTTP MCP server via `@modelcontextprotocol/sdk`, running stateless so a fresh server instance is created per request | [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| Scheduled jobs in generated apps | Vercel Cron invoking `/api/notifications/cron/daily-digest`, authenticated by a shared `CRON_SECRET` | [.env.example](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/.env.example) |
| Internal admin surface (published, not public product) | The OpenAPI document also declares admin endpoints tagged `admin:benchmark`, `admin:inspect`, `admin:deploy`, `admin:dynamic-config`, `admin:env`, `admin:tenants`, `admin:workers`, `admin:audit` and `admin:panic`, including browser and session inspection, deploy/rollback and per-tenant credit grants | [OpenAPI 3.1 spec](https://anima.eazo.ai/docs/openapi/v1.json); accessed 2026-07-30 |

**Published benchmark claim.** The GUMem documentation states 92.9% accuracy on the LoCoMo long-conversation memory benchmark, described as "currently SOTA-level performance", against a table of 16 comparison systems including Mem0 (91.60, marked "New April 2026"), HyperGraphRAG, MIRIX, HippoRAG 2, LightRAG, MemOS, Membase, GraphRAG, Zep, LangMem, MemU, OpenAI and A-Mem. The page states the evaluation uses the official `locomo10.json` 10-conversation subset — 272 sessions, 5,882 dialogue turns, 1,986 QA annotations — and links the [LoCoMo paper](https://arxiv.org/abs/2402.17753) and [dataset](https://github.com/snap-research/locomo/blob/main/data/locomo10.json) ([performance page](https://anima.eazo.ai/docs/gumem/concepts/performance); accessed 2026-07-30). The figure is self-reported; no evaluation date, judge model or independent reproduction is stated on the page.

**Documentation status labels.** The Anima "API Surface" page is marked "Draft interface — The examples below express integration intent. They are not final SDK or HTTP contracts" ([API surface](https://anima.eazo.ai/docs/api/); accessed 2026-07-30), while the WebAgent reference publishes a concrete OpenAPI 3.1 document.

### Data handling as documented

The Terms state that apps and agents created through Eazo "may also include memory-related capabilities" and that "Unless you adjust the relevant settings where controls are made available, Eazo may enable by default the setting under which user data generated from the use of your app or agent within Eazo Mobile is automatically reported, synchronized, or otherwise transmitted to Eazo" ([Terms § 3.1](https://eazo.ai/terms-of-service); Effective 2026-02-01). Published apps and agents "may be public by default" and "may be remixable by default" unless the creator changes visibility or Remix settings ([Terms § 5.8, § 5.9](https://eazo.ai/terms-of-service)).

The Privacy Policy states that services are "powered by one or more third-party generative AI models", that inputs "may be transmitted to these third-party AI providers", that the company takes "steps to contractually restrict those providers from using your data for their independent model training", and that its own model-improvement use happens "only after the information has been securely encrypted and de-identified", with a right to object ([Privacy Policy § 1.2.11](https://eazo.ai/privacy-policy)). No third-party AI provider is named. The policy also states the company "'sell[s]' and 'share[s]'" personal information with third-party advertising networks under CCPA definitions, with opt-out by email to `privacy@eazo.ai`, and describes collection of precise GPS location for location-based queries, real name, date of birth and government ID number "to verify your age and your identity as required by applicable laws" ([Privacy Policy](https://eazo.ai/privacy-policy)).

The Anima security guide documents a two-layer model — GenAuth authorization plus a controlled browser sandbox — and states that "EAK does not persist user passwords", that passwords "should not be written to task results, ReAct traces, GUMem, audit body text, callback events, or application logs", that `callbackUrl` must use HTTPS, that returned video frames and screenshots must be bound to a `taskId`, project and user session, and that "EAK does not publish browser video as a public resource" ([security guide](https://anima.eazo.ai/docs/guides/security); accessed 2026-07-30).

### Technical background sought

All of the following comes from the three role pages on [eazo.ai/careers](https://eazo.ai/careers) (Undated; accessed 2026-07-30). Applications go through Tally forms rather than an applicant-tracking system.

**Agent Engineer** — San Francisco or Singapore, "remote possible for exceptional cases", full time.

- *Required:* being "Deeply self-driven"; strength in JavaScript, TypeScript and Python "with solid engineering fundamentals"; work spans agent memory, agent proactivity and multi-agent orchestration, and includes designing core agent systems (memory, proactive reasoning, task orchestration) and optimizing multi-agent workflows.
- *Preferred:* original agent/LLM projects, experiments or products, shown via GitHub, blog or demo; awards from hackathons, NOI, Kaggle or similar competitions; agent frameworks, knowledge graphs, vector retrieval or memory compression; contributions to Agent SDKs, LangGraph or similar ecosystems; deep understanding of React or the V8 JavaScript engine; having built something zero to one "with real users or revenue".
- The posting states "No hierarchy here" and "If you need someone to tell you what to do, this isn't the role."

**Design Engineer** — San Francisco, "remote possible for exceptional candidates", full time.

- *Required:* designing and building generative UI ("GenUI") systems "from concept to production code"; shipping "real features in React, not just hand off mockups"; information architecture for dynamic interfaces; interaction and motion design; establishing design systems.
- *Preferred:* designing AI-native or agent-based products; strong React and modern frontend proficiency; a portfolio showing both design thinking and shipped code; motion design and micro-interactions; having built or contributed to design systems at scale; generative UI, adaptive interfaces or unconventional interaction patterns; information architecture or complex data-driven products.

**Growth** — San Francisco, "remote possible for exceptional candidates", full time.

- *Required:* owning the full funnel from acquisition to activation to retention; running experiments; driving acquisition "across multiple markets (North America, Europe, Japan)"; funnel and behaviour analysis; building growth mechanisms into the product; SEO/SEM, social, content and community.
- *Preferred:* having grown an AI-native product "from zero to significant scale"; multi-market launch experience; growth loops or referral mechanisms; content creation or brand building for technical products; startup experience.

**Talent Community** — Global, an open form for engineering, design, growth, product, research, operations "or something else".

### Industry domain

The work spans agent runtimes and tool protocols (MCP, OIDC/OAuth delegation, OpenAPI 3.1, SSE event streams), consumer app-store distribution on iOS and Android, and creator-marketplace commerce: platform-collected versus creator-collected payments, merchant-of-record allocation, credits, refunds and chargebacks, KYC and tax withholding on payouts, and AML/CTF and sanctions screening on withdrawals ([Terms § 3.5](https://eazo.ai/terms-of-service)). The Anima documentation adds delegated-authority design and browser-automation safety: scope and denied-scope modelling, audit trails, password-path isolation, and the explicit instruction not to use WebAgent where "The target site's terms do not allow automated access and you do not have the required authorization" ([WebAgent overview](https://anima.eazo.ai/docs/webagent/)). The privacy documentation adds GDPR/EEA+, UK, Swiss and thirteen named US state privacy regimes, CCPA sale/share disclosure, and under-18 handling ([Privacy Policy](https://eazo.ai/privacy-policy)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Careers page | `eazo.ai/careers`, with four listings and an FAQ; applications submitted through Tally forms | [careers](https://eazo.ai/careers); Undated; accessed 2026-07-30 |
| Locations | Agent Engineer: "San Francisco or Singapore"; Growth and Design Engineer: "San Francisco"; Talent Community: "Global" | [careers](https://eazo.ai/careers) |
| Remote policy | "remote possible for exceptional cases" (Agent Engineer) and "remote possible for exceptional candidates" (Growth, Design Engineer); no general remote policy stated | [careers](https://eazo.ai/careers) |
| Compensation | "Top-of-market salary + equity (open to negotiate)" on all three roles; no band published | [careers](https://eazo.ai/careers) |
| Visa sponsorship | "We prefer candidates who already have work authorization. For truly exceptional candidates who need sponsorship, we're open to exploring options." | [careers FAQ](https://eazo.ai/careers) |
| Years of experience | "No. We care about what you can do, not how long you've been doing it." | [careers FAQ](https://eazo.ai/careers) |
| Interns and students | "Yes, for every role. Strong interns have a clear path to full-time offers." | [careers FAQ](https://eazo.ai/careers) |
| Interview process | "Typically 2-3 rounds", possibly with a take-home assignment or pair programming; "expect a decision within 1-3 weeks from your first conversation" | [careers FAQ](https://eazo.ai/careers) |
| Stated way of working | "Small team, flat structure, high ownership. We ship fast, debate ideas openly, and care about craft. No hand-holding" | [careers FAQ](https://eazo.ai/careers) |
| Working language | Not stated as a policy. The careers site, product site, App Store listing and English documentation are in English; the Anima docs, the Creator frontend i18n stack and the hackathon page also ship 简体中文 | [careers](https://eazo.ai/careers), [docs](https://anima.eazo.ai/docs/), [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md) |
| Team size, benefits, turnover, office policy | Not published | see `Notes` |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-30): `eazo.ai` homepage, `/about`, `/careers`, `/blog` and both posts, `/terms-of-service`, `/privacy-policy`, and probes of `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/.well-known/security.txt`, `/hackathon`, `/apps`, `/explore`, `/discover` and `/gallery`; `creator.eazo.ai` and its runtime config; `eak.eazo.ai`, `anima.eazo.ai` and its docs, pricing, early-access, OpenAPI document and dashboard redirect; `cdn.eazo.ai`, `api.eazo.ai`, `docs.eazo.ai`, `status.eazo.ai`, `mcp.eazo.ai`, `assets.eazo.ai` and `hackathon2026.eazo.dev`; the `EazoAI` GitHub organisation and all five public repositories including `README.md`, `AGENTS.md`, `package.json`, `.env.example` and `CHANGELOG.md`; the `@eazo` npm scope and all four packages; PyPI; the App Store and Google Play listings including the developer block; `fellou.ai` and its terms and privacy policy; the `FellouAI` GitHub organisation; Wayback Machine CDX indexes for `eazo.ai`, `eak.eazo.ai`, `anima.eazo.ai` and `eazo.dev`; English and Chinese searches on the brand, legal name and founder; searches across 36Kr, 品玩 PingWest, Sina Tech, Tencent News, ChinaDaily and Zhihu; Crunchbase, PitchBook, Tracxn and ZoomInfo profiles; LinkedIn; and the Luma, Devpost and Stanford Daily hackathon material.

- **Any funding round, investor or valuation from the company.** No press index, funding page or announcement exists on `eazo.ai` or `fellou.ai`. The only figures found are third-party database entries that contradict each other — see below.
- **Team size and named employees other than "Yang".** No team or leadership page; both blog posts are attributed to "Eazo Team"; the GitHub organisation has no public members; the npm maintainer accounts state no roles.
- **Salary bands.** Not published; all three roles state "Top-of-market salary + equity (open to negotiate)".
- **User, creator, app-catalog, revenue or transaction figures.** None published. There is no public web gallery, discovery page or catalog API: `/apps`, `/explore`, `/discover` and `/gallery` all return HTTP 404, and the app catalog is reachable only inside the mobile app or behind the Creator login.
- **Platform fee rate and Anima pricing.** The Terms defer the platform-fee rate to "the relevant Service interface"; the Anima pricing page is "Coming soon".
- **The named third-party AI providers.** The Privacy Policy refers only to "one or more third-party generative AI models". The template documents AWS Bedrock as the gateway and lists model keys, but no provider contract, region or fallback is stated.
- **Security certification, status page or published SLA.** No SOC 2, ISO/IEC 27001 or equivalent is claimed on any reviewed page. `status.eazo.ai` and `docs.eazo.ai` resolve through Cloudflare but return HTTP 404, and the template README's link to `docs.eazo.ai` is therefore dead.
- **An engineering blog.** The blog holds two posts (2026-01-26 and 2026-05-02), both product and company positioning rather than technical writing. Technical material is published in the Anima docs and the template repositories instead.
- **Corporate registry record for `ASI X Inc.`** Not retrieved. The Delaware entity name search at `icis.corp.delaware.gov` is gated by a CAPTCHA and OpenCorporates returned a CAPTCHA challenge on 2026-07-30; no registry filing was read. The Wilmington address given in both companies' privacy policies is a registered-agent address, not necessarily an operating office.
- **The Python SDK.** The Quickstart documents `pip`-style use of a package named `eazo-eak`, but `pypi.org/pypi/eazo-eak/json` returned HTTP 404 on 2026-07-30. No PyPI package under that name was found.
- **Hackathon outcome.** No winners announcement, results page or prize-payment confirmation was found. `eazo.ai/hackathon` returns HTTP 404 and the Devpost listing returns HTTP 410 Gone; the voting site at `hackathon2026.eazo.dev` renders client-side and exposes no listing route.
- **Sources that blocked automated access on 2026-07-30:** LinkedIn (HTTP 999), PitchBook (403), Crunchbase (403), `x.com` (402), OpenCorporates (CAPTCHA). The Eazo and Fellou X accounts, the LinkedIn profile indexed as "Yang Xie - ASI X", and the PitchBook figures were therefore not read directly; where they appear above, the wording comes from search-result titles or snippets and is labelled unconfirmed.

### Inconsistencies across sources

- **Total raised:** a [PitchBook profile](https://pitchbook.com/profiles/company/894665-44) is reported to state US$40.4M with LongRiver Investments as investor, while [Tracxn](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw) states the same company is "Unfunded". Both describe the Fellou brand, both are undated, and neither was confirmed against a primary source. The PitchBook figure comes from search-result snippets because the page returned HTTP 403.
- **Operating status:** [36Kr (2026-07-07)](https://36kr.com/p/3884772932792581) states "Fellou后续遇到融资困难，难以为继" without attribution. Against that, `fellou.ai` still serves its homepage, terms and privacy policy, while `fellou.ai/blog` and `fellou.ai/eko/docs/` returned HTTP 503 on 2026-07-30, the `FellouAI` GitHub organisation's most recent push to `eko` is dated 2026-03-03 and its other repositories were last pushed in 2025, and the same legal entity shipped Eazo releases on 2026-07-28 and 2026-07-29. The two accounts are recorded here rather than reconciled.
- **App name:** the App Store listing is indexed both as "Eazo" and "Eazo: Discover AI Apps, Agents" under the same id `6758009137`; the lookup API returns the longer name ([iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us)).
- **App store category:** Apple lists the app under Lifestyle, Google Play under Communication ([iTunes lookup API](https://itunes.apple.com/lookup?id=6758009137&country=us), [Google Play](https://play.google.com/store/apps/details?id=ai.eazo.portal)).
- **Product self-description varies by audience:** "a community of AI apps and agents" ([App Store](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137)), "InternetOS, your operating system for the internet" ([blog, 2026-01-26](https://eazo.ai/blog/you-were-born-to-be-powerful)), "your Smart Life Gateway" ([about](https://eazo.ai/about)), and "The world's first zero-code full-stack AI builder" ([Luma partner blurb](https://luma.com/frw43jmv)).
- **Hackathon cities:** the blog post and the Stanford Daily placement both name San Francisco, New York and Shanghai as in-person cities ([blog, 2026-05-02](https://eazo.ai/blog/we-ran-a-different-kind-of-hackathon), [Stanford Daily, 2026-05-18](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/)); the Luma pages describe only San Francisco (Mountain View) and New York as in-person regions, with Asia online folded into the Shanghai region ([Luma SV](https://luma.com/frw43jmv)).
- **Anima API path prefix:** the API overview gives resource paths as `/v1/projects/{project_id}/...` while the published OpenAPI document declares them as `/api/v1/projects/{pid}/...` ([API overview](https://anima.eazo.ai/docs/webagent/reference/), [OpenAPI spec](https://anima.eazo.ai/docs/openapi/v1.json)).
- **Anima maturity signals:** the homepage says identity, memory and web execution are "currently in private build" while the pricing page says "GenAuth, GUMem, and Web Agent are running in production" ([anima.eazo.ai](https://anima.eazo.ai/), [pricing](https://anima.eazo.ai/pricing)).
- **`GenAuth` as Eazo's own layer versus a third-party platform:** the docs present `GenAuth` as one of Anima's three layers ([GenAuth overview](https://anima.eazo.ai/docs/genauth/)), while `@eazo/auth` depends on `authing-js-sdk`, tags itself with both `genauth` and `authing`, and the SDK changelog refers to "the Authing OAuth popup" ([npm](https://registry.npmjs.org/@eazo%2Fauth), [CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)); a separate identity platform trades as [GenAuth](https://www.genauth.ai/). No reviewed page states the relationship.

### Other

- **Two brands, one legal entity, no cross-reference in marketing.** `ASI X Inc.` is named as the contracting party in both Eazo's and Fellou's legal pages at the same registered address, and the Eazo app's Google Play developer email is `media@fellou.ai`. Neither brand's marketing site links to or mentions the other. The engineering timelines are adjacent rather than overlapping: the `EazoAI` GitHub organisation was created 2026-02-11, both companies' current terms and privacy policies took effect 2026-02-01, the iOS app shipped 2026-03-28, and `FellouAI`'s repositories were last pushed between 2025 and 2026-03-03.
- **The company publishes far more depth on the developer product than on the consumer one.** Eazo Anima ships bilingual documentation, 15 use-case guides, a security model, a benchmark comparison table and a 125-path OpenAPI 3.1 document, while `eazo.ai` itself is a single-screen landing page with two blog posts, no sitemap, no `llms.txt` and no public app catalog.
- **The published OpenAPI document includes the internal admin surface.** Forty-seven of the 125 declared paths are `/api/admin/*`, covering a benchmark runner with datasets and evidence artifacts, live browser and session inspection with timelines, deploy/rollback/deployment streaming, dynamic config and environment patching, per-tenant credit grants, worker management and a `POST /api/admin/panic` endpoint ([OpenAPI spec](https://anima.eazo.ai/docs/openapi/v1.json); accessed 2026-07-30).
- **The platform's official model list contains no proprietary frontier models.** Every documented Eazo model key is an open-weight or hosted-open model — DeepSeek, OpenAI `gpt-oss`, Qwen, Mistral, Gemma, Nemotron, MiniMax, Kimi, GLM, Palmyra — with `deepseek.v3.1` as the documented default ([AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md); accessed 2026-07-30).
- **Default-public and default-remixable are written into the Terms**, alongside a default under which app usage data inside Eazo Mobile is reported to Eazo unless the creator changes the setting ([Terms § 3.1, § 5.8, § 5.9](https://eazo.ai/terms-of-service)). The SDK changelog records the consent gate for that reporting being added in 0.21.0 on 2026-06-11, more than four months after the Terms took effect ([CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)).
- **The SDK release series is dated and diffable.** `@eazo/sdk` shipped 27 versions between 2026-04-22 and 2026-07-28, with marketplace payments requiring 0.22.3 or later; `@eazo/eak` shipped 15 versions between 2026-06-02 and 2026-06-18 and has not been republished since ([npm](https://registry.npmjs.org/@eazo%2Fsdk), [npm](https://registry.npmjs.org/@eazo%2Feak); accessed 2026-07-30).
- **The consumer distribution numbers and the hackathon spend are far apart in scale.** The published prize pool is US$300,000 across 253 slots, while Google Play showed "50+ Downloads" and the App Store 15 ratings when checked on 2026-07-30.
- **The company runs an unusually large amount of its operations on third-party SaaS.** Applications and hackathon registration on Tally, events on Luma, hackathon rules on Google Drive, hackathon submissions on Devpost, the voting app on Vercel, analytics on Google Analytics and PostHog, auth on Authing, payments on Stripe, and model access through AWS Bedrock — with no self-hosted applicant tracking, status page or press index.

---

## Resources

**Official**

- [Homepage](https://eazo.ai/)
- [About Us](https://eazo.ai/about) · [Careers](https://eazo.ai/careers)
- [Blog](https://eazo.ai/blog) — [You Were Born to Be Powerful, 2026-01-26](https://eazo.ai/blog/you-were-born-to-be-powerful) · [We Ran a Different Kind of Hackathon, 2026-05-02](https://eazo.ai/blog/we-ran-a-different-kind-of-hackathon)
- [Platform Service Terms](https://eazo.ai/terms-of-service) · [Privacy Policy](https://eazo.ai/privacy-policy) — both Effective 2026-02-01
- [Eazo Creator](https://creator.eazo.ai/) — [runtime config](https://eazo.ai/creator/creator-runtime-config.js)
- [Eazo Anima](https://anima.eazo.ai/) — [pricing](https://anima.eazo.ai/pricing) · [early access](https://anima.eazo.ai/early-access)
- [Eazo Anima Docs](https://anima.eazo.ai/docs/) — [Quickstart](https://anima.eazo.ai/docs/guides/quickstart) · [GUMem overview](https://anima.eazo.ai/docs/gumem/getting-start/overview/) · [GUMem benchmark](https://anima.eazo.ai/docs/gumem/concepts/performance) · [WebAgent overview](https://anima.eazo.ai/docs/webagent/) · [WebAgent API overview](https://anima.eazo.ai/docs/webagent/reference/) · [GenAuth overview](https://anima.eazo.ai/docs/genauth/) · [API surface (draft)](https://anima.eazo.ai/docs/api/) · [security guide](https://anima.eazo.ai/docs/guides/security) · [OpenAPI 3.1 spec](https://anima.eazo.ai/docs/openapi/v1.json)
- [GitHub organisation `EazoAI`](https://github.com/EazoAI) — [eazo-sdk](https://github.com/EazoAI/eazo-sdk) ([SDK README](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/sdk/README.md), [CHANGELOG](https://raw.githubusercontent.com/EazoAI/eazo-sdk/main/CHANGELOG.md)) · [eazo-creator-nextjs-template](https://github.com/EazoAI/eazo-creator-nextjs-template) ([README](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/README.md), [AGENTS.md](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/AGENTS.md), [package.json](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/package.json), [.env.example](https://raw.githubusercontent.com/EazoAI/eazo-creator-nextjs-template/main/.env.example)) · [GitHub API org record](https://api.github.com/orgs/EazoAI)
- npm scope `@eazo` — [@eazo/sdk](https://registry.npmjs.org/@eazo%2Fsdk) · [@eazo/eak](https://registry.npmjs.org/@eazo%2Feak) · [@eazo/auth](https://registry.npmjs.org/@eazo%2Fauth) · [@eazo/node-sdk](https://registry.npmjs.org/@eazo%2Fnode-sdk) · [scope search](https://registry.npmjs.org/-/v1/search?text=eazo)
- [Archived EAZO Global Hackathon 2026 page (ZH/EN), captured 2026-05-19](https://web.archive.org/web/20260519123846/https://eazo.ai/hackathon)
- [Fellou](https://fellou.ai/) — [Terms](https://fellou.ai/terms/) · [Privacy Policy](https://fellou.ai/policy/), both naming `ASI X Inc.`

**Store listings**

- [App Store — Eazo: Discover AI Apps, Agents](https://apps.apple.com/us/app/eazo-discover-ai-apps-agents/id6758009137) · [iTunes lookup API record](https://itunes.apple.com/lookup?id=6758009137&country=us)
- [Google Play — ai.eazo.portal](https://play.google.com/store/apps/details?id=ai.eazo.portal)

**Third-party coverage and profiles**

- [Stanford Daily — "Join The Eazo Hackathon", 2026-05-18 (labelled Third-Party Advertising)](https://stanforddaily.com/2026/05/18/join-the-eazo-hackathon/)
- [Luma — Eazo AI 2026 Global Hackathon: Silicon Valley](https://luma.com/frw43jmv) · [Luma — Eazo.ai NYC Hackathon](https://luma.com/ay4dy8o5)
- [Devpost — Eazo.ai Hackathon listing (HTTP 410 Gone on 2026-07-30)](https://eazo-ai-hackathon.devpost.com/)
- [hackathon2026.eazo.dev — voting site](https://hackathon2026.eazo.dev/)
- [X — @FellouAI post promoting the EAZO hackathon, 2026-05](https://x.com/FellouAI/status/2054356197491273795)
- [36Kr — "AI浏览器这百亿大蛋糕，谁也没吃到？", 2026-07-07 (ZH)](https://36kr.com/p/3884772932792581)
- [36Kr — "这个AI新赛道火了，给Agent做浏览器", 2025-04-21 (ZH)](https://36kr.com/p/3271114913128836)
- [Sina Tech / 创事记 — "95后打造世界首个行动型浏览器——Fellou", 2025-04-21 (ZH)](https://finance.sina.com.cn/tech/csj/2025-04-21/doc-inetwzpw8763926.shtml)
- [GlobeNewswire — "Fellou Announces Next-Generation Agentic AI Browser", 2025-08-12](https://www.globenewswire.com/news-release/2025/08/12/3131385/0/en/Fellou-Announces-Next-Generation-Agentic-AI-Browser-Transforming-the-Future-of-Work.html)
- [APT401 — "The Browser That Acts: How Fellou Captured China's Tech Imagination"](https://apt401.substack.com/p/the-browser-that-acts-how-fellou)
- [Apple Podcasts — "与Fellou创始人谢扬的3小时访谈" (ZH)](https://podcasts.apple.com/cn/podcast/34-%E4%B8%8Efellou%E5%88%9B%E5%A7%8B%E4%BA%BA%E8%B0%A2%E6%89%AC%E7%9A%843%E5%B0%8F%E6%97%B6%E8%AE%BF%E8%B0%88-%E5%AD%A4%E7%8B%AC-95%E5%90%8E-%E7%89%8C%E6%A1%8C%E4%B8%8E%E7%94%9F%E4%BA%A7%E5%8A%9B%E7%9A%84%E5%AE%8C%E7%BE%8E%E5%88%9B%E4%B8%9A/id1754955836?i=1000704842263)
- [Tracxn — Fellou company profile](https://tracxn.com/d/companies/fellou/__rAPhhscomUnL6oyjVLWcasY1OujUe0hnb0dOg30Z5Hw)
- [PitchBook — Fellou company profile (HTTP 403 to automated access on 2026-07-30)](https://pitchbook.com/profiles/company/894665-44)
- [LinkedIn — "Eazo Technology Co., Ltd." (similar name; no established connection)](https://www.linkedin.com/company/eazo-technology)
- [GenAuth — identity platform](https://www.genauth.ai/)
- [LoCoMo benchmark paper](https://arxiv.org/abs/2402.17753) · [locomo10.json dataset](https://github.com/snap-research/locomo/blob/main/data/locomo10.json)
