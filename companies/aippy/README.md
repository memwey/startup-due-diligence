# Aippy

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Aippy is a mobile-first AI creation community: a user describes an idea in natural language, the platform generates a playable mini-game or interactive web piece, and the result is published into a vertical feed that other users scroll, play, comment on, and "Remix" ([aippy.ai](https://aippy.ai/); accessed 2026-07-29). The web platform first shipped as v0.1.0 on [2025-04-18](https://docs.aippy.ai/changelog) and the iOS app was first released on [2025-07-28](https://itunes.apple.com/lookup?id=6749073777). The app is published by **NADA AI PTE. LTD.**, a Singapore entity; the business was incubated inside HKEX-listed **Newborn Town Inc. (赤子城科技, 09911)** and separated from the listed group in mid-2026.

- **Funding:** a first institutional round of "tens of millions of USD" (数千万美元) from Glowill Capital (歌未资本) at a post-money valuation of **$250M**, reported 2026-06-02 as a 36Kr exclusive ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)). Newborn Town deconsolidated NADA AI but "retains a considerable proportion" of its equity ([新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)).
- **Scale, as the company states it:** 3M+ global downloads, ~2M monthly active users, 2M+ UGC works, ~50% DAU interaction rate, 4.8 US App Store rating ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)). Independently observable on 2026-07-29: iOS 4.86 from 20,849 US ratings ([iTunes API](https://itunes.apple.com/lookup?id=6749073777)) and a Google Play "1M+ downloads" bucket ([Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy)).
- **Team ~30**, drawn from Tsinghua, Northwestern and TU Munich across algorithms, product and operations ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)); the [LinkedIn page](https://www.linkedin.com/company/aippy/) shows an 11–50 band with 4 profiles and gives the headquarters as San Jose.
- **The only verifiable stack evidence is on npm.** `@aippy/runtime` peer-depends on React 19, the Vercel AI SDK (`ai` ^6.0.0, `@ai-sdk/react` ^3.0.0) and dependency `@ai-sdk/openai-compatible`; `@aippy/vite-plugins` does Babel-based component tagging for Vite ([npm](https://registry.npmjs.org/-/v1/search?text=aippy)). The same runtime was previously published as **`@new-born-town/aippy-runtime`** by the same two maintainers — the one machine-checkable link between Aippy and its former parent.
- **Almost nothing about the engineering organisation is public.** There is no careers page, no job posting, no engineering blog, no named engineer, and no security page. The documentation site's last content commit is [2025-06-27](https://github.com/AIPPY/Aippy-Docs) and both published Discord invites are dead. A [GitHub account claiming to be official](https://github.com/AippyAI/Aippy) carries a pump.fun-style token address in its repository description — see `Notes`.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | Aippy; the site footer reads "NADA AI" | [aippy.ai](https://aippy.ai/) rendered in a browser, accessed 2026-07-29 |
| App publisher | NADA AI PTE. LTD. (`PTE. LTD.` is the Singapore private-limited form) | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777), [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |
| Former parent | Newborn Town Inc. (赤子城科技), HKEX 09911; incubated Aippy and deconsolidated NADA AI in 2026 | [新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |
| Founded | 2025 | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440), [LinkedIn](https://www.linkedin.com/company/aippy/) |
| Web platform launch | v0.1.0 on 2025-04-18; Chinese coverage dates the product launch to April 2025 | [changelog](https://docs.aippy.ai/changelog), [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| iOS launch | 2025-07-28; current version 1.17.0 released 2026-07-24 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| Headquarters | LinkedIn gives San Jose, United States; no address is published on any Aippy surface | [LinkedIn](https://www.linkedin.com/company/aippy/) |
| Founder and CEO | Evan (叶椿建), co-founder and long-serving CTO of Newborn Town | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| Headcount | ~30 (company statement, June 2026); LinkedIn band 11–50 with 4 profiles | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440), [LinkedIn](https://www.linkedin.com/company/aippy/) |
| Customers / users | 3M+ downloads, ~2M MAU, 2M+ works (company statement, June 2026) | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| Total raised | One round, "tens of millions of USD"; the sources publish a band, not a number | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| Valuation | $250M post-money, described as ~HK$2bn | [新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |
| Investor | Glowill Capital (歌未资本) | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| Engineering working language | Not stated anywhere. All product, documentation and app-store surfaces are English-only (`languageCodesISO2A` = `["EN"]`); the company's coverage and its former parent are Chinese-language | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777), [docs](https://docs.aippy.ai/welcome) |
| Contact | hi@, support@, legal@, bd@, developer@ and feedback@ `aippy.ai`; careers@aippy.ai is named in the privacy policy | [terms of service](https://aippy.ai/terms.html), [privacy policy](https://aippy.ai/privacy.html) |
| Social | X [@aippyai](https://x.com/aippyai), [LinkedIn](https://www.linkedin.com/company/aippy/); the Discord invites published on the site and docs are expired | [docs](https://docs.aippy.ai/welcome), Discord invite API, accessed 2026-07-29 |

### Identity and legal entities

| Name | Type | Relationship | Source |
|---|---|---|---|
| Aippy | Public brand and product | The consumer-facing name; owns the `aippy.ai` domain and trade names per its own terms | [terms of service](https://aippy.ai/terms.html) |
| NADA AI PTE. LTD. | Operating entity (Singapore) | Publishes the iOS and Android apps; the name appears in the website footer and in the `com.nadaai.aippy` bundle identifier | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777), [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |
| Newborn Town Inc. (赤子城科技) | Former parent, HKEX 09911 | Incubated Aippy; after the 2026 restructuring NADA AI is no longer consolidated, but Newborn Town retains a "considerable proportion" of equity and continues to supply localization operations, global traffic coordination and technical support | [新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |
| `@new-born-town` npm scope | Former publishing identity | The Aippy runtime SDK was first published as `@new-born-town/aippy-runtime` (2025-10-09 to 2025-10-13) before moving to `@aippy/runtime` under the same two maintainers | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| `AippyAI` on GitHub | Unverified third-party account | Self-describes as "AippyAi official" but is not linked from any Aippy surface; its repository description ends in a base58 string with the pump.fun `pump` suffix — see `Notes` | [GitHub](https://github.com/AippyAI/Aippy) |

No corporate-registry record was retrieved for NADA AI PTE. LTD.; see `Notes`.

---

## Product

### The creation and feed loop

The rendered site is a category feed of community creations with view, like and comment counts, headed by a single prompt box reading "Type your idea and start building..." ([aippy.ai](https://aippy.ai/); rendered and read on 2026-07-29). The taxonomy is served by a public endpoint and is seven categories: **Hot, Latest, Mindless, Brain Hack, Unhinged, Dopamine, Send This** ([category API](https://api.aippy.ai/api/template/category_v2)). Chinese coverage describes the form factor as an "interactive feed" that users scroll like short video, with natural-language Remix of existing works ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)).

The App Store listing groups the output into four kinds — "GAMES & SIMULATORS", "TOOLS & GENERATORS", "INTERACTIVE ART" and "AI EXPERIMENTS" — and states remixing "always credit[s] the original" ([App Store description](https://itunes.apple.com/lookup?id=6749073777), [FAQ](https://docs.aippy.ai/faq)).

### Apps

| Surface | Name | Detail | Source |
|---|---|---|---|
| Web | Aippy | React + Vite single-page app with a PWA manifest and service worker; served from Alibaba Cloud OSS behind Cloudflare | [page source](https://aippy.ai/), response headers, accessed 2026-07-29 |
| iOS | Aippy: Game Maker | Bundle `com.nadaai.aippy`, Entertainment / Graphics & Design, 12+, English only, minimum iOS 15.0, 52.4 MB | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| Android | Aippy: AI Game Maker | Same bundle id, 1M+ downloads bucket, updated 2026-07-29 | [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |

### Documented capabilities

The [documentation](https://docs.aippy.ai/welcome) describes generative UI from a text prompt, live preview with checkpoint-based version history, in-canvas visual editing ([Instant Edit](https://docs.aippy.ai/features/instand-edit), shipped in v0.5.0 on 2025-06-10), and one-click publishing. It also claims full-stack generation with database and API connectivity, custom domains, payments and authentication. The [roadmap](https://docs.aippy.ai/roadmap) on the same site lists exactly those items — backend and database, visual editor, custom domains, payment processing and third-party integrations — as "Coming Soon". The two pages contradict each other; see `Notes`.

### Commercialization

Five subscription tiers, priced identically across every source but with different quotas depending on which page you read. The live [pricing page](https://aippy.ai/pricing) (rendered 2026-07-29) is the current statement:

| Plan | Price | Credits / month | Building requests | Asset storage |
|---|---|---|---|---|
| Starter | $0 | 500 (100 per daily login, capped at 500) | — | 500 MB |
| Explorer | $19 | 2,000 | 80 | 2 GB |
| Builder | $49 | 5,000 | 200 | 10 GB |
| Master | $99 | 10,000 | 400 | 20 GB |
| Team | $199 | 20,000 | 800 | 50 GB |

The [changelog](https://docs.aippy.ai/changelog) fixes the exchange rate: "25 credits = one prompt = one successful building request", introduced with the credit system in v0.5.1 on 2025-06-25, alongside a referral scheme granting 50 free credits per successful registration. Payments are handled by third-party processors — Stripe and PayPal are named in the terms, Stripe in the privacy policy ([terms](https://aippy.ai/terms.html), [privacy policy](https://aippy.ai/privacy.html)). The terms also state that unused messages do not roll over and that no refunds are given except for duplicate charges, billing errors, or outages exceeding 72 consecutive hours.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2025-04-18 | Web platform v0.1.0, first release | [changelog](https://docs.aippy.ai/changelog) |
| 2025-06-25 | v0.5.1, last dated release entry published | [changelog](https://docs.aippy.ai/changelog) |
| 2025-07-28 | iOS app first released | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| 2026-01 | Newborn Town reports Aippy scoring 4.9 on both the Apple and Android stores | [新浪财经, 2026-01-21](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml) |
| 2026-06-02 | 3M+ downloads, ~2M MAU, 2M+ UGC works, ~50% DAU interaction rate, 4.8 US App Store, daily new creations up 10x since the start of the year, daily usage time up 25%, 30%+ organic traffic | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| Accessed 2026-07-29 | iOS: 4.86 average from 20,849 US ratings; version 1.17.0 released 2026-07-24 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| Accessed 2026-07-29 | Google Play: 1M+ downloads bucket; updated 2026-07-29 | [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |
| Accessed 2026-07-29 | Top feed item "Guess The Logo!" showed 454K views, 4K likes and 5.6K comments | [aippy.ai](https://aippy.ai/), rendered in a browser |

### Announced customers and partners

No customer, partner, distribution deal, model vendor or infrastructure vendor has been announced by Aippy or by Newborn Town in any source reviewed on 2026-07-29. The only named commercial relationships are the payment processors in the legal pages and the single disclosed investor.

### Stated plans

The round's proceeds are stated as going to "top talent recruitment and user scale-up in core European and American markets" ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)). The [roadmap](https://docs.aippy.ai/roadmap) names full-stack generation, a visual editor, and custom domains, payments and third-party integrations as forthcoming, with no dates attached. Newborn Town's stated continuing role is localization operations, global traffic coordination and technical support ([新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)).

---

## Founder

| Name | Role | Career facts stated | Source |
|---|---|---|---|
| Evan (叶椿建) | Founder and CEO of Aippy | Co-founder of Newborn Town Inc. and its long-serving CTO; described as having more than ten years in overseas social and gaming products | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |

No other individual is named in any source reviewed. Neither the website, the apps, the documentation, the LinkedIn page nor any press item names a co-founder, an executive, or an engineering leader, and no team or about page exists on any Aippy surface. The npm packages are published by two accounts, `sin_bufan` and `kkunique`, whose real-world identities are not stated ([npm](https://registry.npmjs.org/-/v1/search?text=aippy)).

### Selected leadership

| Name | Role | Source |
|---|---|---|
| — | No leadership other than the founder is publicly identified | Searched 2026-07-29; see `Notes` |

---

## Funding

| Date | Round | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Reported 2026-06-02 | First round (轮次未命名) | "数千万美元" — tens of millions of USD, published as a band rather than a figure | Glowill Capital (歌未资本) | Same; no prior round disclosed | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440), [新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |

The round is not given a letter name by any source. Post-money valuation is stated as $250M, described as roughly HK$2bn and characterised as the first time Newborn Town's AI business received an independent market valuation ([新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml), [新浪财经, 2026-01-21](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml)).

Two structural facts accompany the round. NADA AI has been separated from the listed company's consolidation scope, and Newborn Town keeps a "considerable proportion" (相当比例) of NADA AI's equity — no percentage is published by any source. Neither Aippy nor Newborn Town issued its own release; the reporting is a 36Kr exclusive (首发) subsequently carried by Sina, 投资界, 东方财富, 证券时报 and others. Several outlets carrying the same numbers trace to that one article and are not independent corroboration.

---

## Engineering

### Technology stack and platforms

Confirmed from public assets — the page source and response headers of `aippy.ai`, the shipped JavaScript bundle, the npm registry, and the documentation repository (all accessed 2026-07-29):

| Item | Detail | Evidence |
|---|---|---|
| Web client | React + Vite single-page app, code-split into `index`, `react-vendor` and `ui-vendor` chunks; PWA via `vite-plugin-pwa` with a registered service worker | [page source](https://aippy.ai/) |
| UI libraries | Ant Design and MUI both present in the bundle; `i18next` with `react-i18next` for localization, currently shipping English only | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Graphics | `three.js`, with `@react-three/fiber` and a Draco decoder loaded from `gstatic.com` | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Generated-project runtime | `@aippy/runtime` — peer dependencies React 19.1.1+, TypeScript 5+, `ai` ^6.0.0 and `@ai-sdk/react` ^3.0.0 (the Vercel AI SDK); dependency `@ai-sdk/openai-compatible`. 48 versions, created 2025-10-14, latest 0.4.1 on 2026-06-23 | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| Generated-project build | `@aippy/vite-plugins` — "Asset management and component tagging", built on `@babel/parser`, `@babel/traverse`, `esbuild`, `estree-walker` and `magic-string`. Created 2025-10-29, latest 0.2.8 on 2026-04-21 | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| Former package scope | `@new-born-town/aippy-runtime`, same description and same two maintainers, published 2025-10-09 to 2025-10-13 before the `@aippy` scope took over | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| Hosting and edge | Alibaba Cloud OSS origin behind Cloudflare; a request without a browser user agent returns the OSS `AccessDenied` XML | response headers on [aippy.ai](https://aippy.ai/) |
| Backend API | `api.aippy.ai`, a JSON API with `{code, msg, data}` envelopes; most endpoints require authentication and return `code: 4011` | [category API](https://api.aippy.ai/api/template/category_v2) |
| Product analytics | ThinkingData (ThinkingAnalytics) SDK, initialised in the web bundle against `https://report.lolipopmobi.com` with page-show and page-hide auto-tracking | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Attribution and analytics | AppsFlyer OneLink (`aippy.onelink.me`), Adjust, Amplitude, Google Analytics (`G-LD0Z19ZH4P`), Cloudflare Web Analytics beacon | [page source](https://aippy.ai/), [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Payments | Stripe named in the bundle; Stripe and PayPal named in the terms | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js), [terms](https://aippy.ai/terms.html) |
| Auth | Third-party sign-in with Google, Apple and GitHub | [terms](https://aippy.ai/terms.html), [privacy policy](https://aippy.ai/privacy.html) |
| Documentation | Mintlify; source in the public [AIPPY/Aippy-Docs](https://github.com/AIPPY/Aippy-Docs) repository, whose `llms.txt` still carries the template title "Mint Starter Kit" | [llms.txt](https://docs.aippy.ai/llms.txt), [repo](https://github.com/AIPPY/Aippy-Docs) |

The following are claims from sources that could not be confirmed against any company-controlled surface, and are recorded as leads rather than stack facts:

| Claim | Where it comes from | Status |
|---|---|---|
| Aippy runs on Newborn Town's self-developed "Boomix" multimodal model plus a lightweight rendering engine | A Chinese content-aggregation page; the wording is repeated across similar sites | Unconfirmed. Newborn Town's own first disclosure of the model, in its 2024 annual results coverage, spells it **Boomiix** and describes it powering the SoloAware engine for social matching and recommendation in products such as SUGO — with no mention of Aippy ([智通财经 via 新浪财经, 2025-03-04](https://finance.sina.com.cn/stock/hkstock/ggscyd/2025-03-04/doc-inenpfhz9590632.shtml)) |
| "Aippy is an AI Vibe Coding platform powered by the Claude large model… built on the React framework and flexibly integrates with three.js or pixi.js" | [github.com/AippyAI/Aippy](https://github.com/AippyAI/Aippy) | Not usable. The account is unverified, is not linked from any Aippy surface, and its repository description ends with a pump.fun-style token address — see `Notes` |

No model provider, inference vendor, cloud region, database, or sandboxing mechanism for executing user-generated code is named on any surface Aippy controls.

### Systems

| System | What it does | Source |
|---|---|---|
| Prompt-to-project generation | Turns a natural-language description into a runnable interactive project; the pricing page counts this as a "building request" at 25 credits each | [aippy.ai](https://aippy.ai/), [changelog](https://docs.aippy.ai/changelog) |
| Prompt enhancement | A dedicated `/api/llmodel/prompt/enhance` endpoint sits in front of generation | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Live preview and checkpoints | Real-time rendering of the project as it changes, with automatic checkpoints and rollback | [welcome](https://docs.aippy.ai/welcome), [roadmap](https://docs.aippy.ai/roadmap) |
| Instant Edit | Direct manipulation of a selected DOM element's text, size and style through Tailwind controls, without a prompt | [Instant Edit](https://docs.aippy.ai/features/instand-edit) |
| Publishing and sharing | Project publish, share and remix endpoints; share links under `share.aippy.ai/p/` and `/u/` | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Social graph and feed | Follow/unfollow, followers and following, comments with replies, likes, favourites, reports, recommendations, top-creator listings and a message inbox with unread counts | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| Content moderation | The terms reserve the right to remove non-compliant content without notice and devote a section to content moderation and user safety; no mechanism, model or turnaround is described | [terms](https://aippy.ai/terms.html) |
| Asset pipeline | Media upload, listing, batch delete and per-user storage stats, quota-limited per plan (500 MB to 50 GB); assets served from `cdn.aippy.ai` with Alibaba OSS image processing (`oss-process`) parameters | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js), [pricing page](https://aippy.ai/pricing) |
| Billing | Subscription plans, order creation, credit transaction records, daily check-in (`attendance`) credits and an affiliate/referral system | [bundle](https://aippy.ai/assets/js/index-BJ8REtwf.js), [changelog](https://docs.aippy.ai/changelog) |
| AI Cloud code storage | Named in the terms; stored code is retained for 90 days after account deletion | [terms](https://aippy.ai/terms.html) |

### Technical background sought

Nothing is published. There is no careers page on `aippy.ai` — every path returns the same single-page shell — no job posting on any board searched, and no description anywhere of the roles, seniority, interview process or expected background. The only hiring channel found is the address `careers@aippy.ai` in the [privacy policy](https://aippy.ai/privacy.html). The one statement bearing on hiring is that the round's proceeds go to "top talent recruitment" ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)), and the one statement about the existing team is that its ~30 people come from Tsinghua, Northwestern and TU Munich across algorithms, product and operations.

### Industry domain

- **Consumer UGC platforms and creator communities.** The product's mechanics — feed, follow graph, likes, comments, remix attribution, top-creator surfacing, daily check-in rewards — are social-product mechanics, and the founder's stated background is a decade of overseas social and gaming products ([36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440)).
- **Overseas ("出海") growth operations.** Newborn Town's continuing contribution is stated as localization operations and global traffic coordination; the round targets European and American user growth ([新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)).
- **Executing untrusted user-generated code.** The platform runs code that a model wrote from an anonymous prompt, in other users' browsers. No sandboxing, isolation or review mechanism is described in any public material.
- **Consumer data and minors.** The privacy policy covers device identifiers (IDFA, IDFV, GAID), cross-border transfers, and GDPR/CCPA rights, and states the service is not intended for anyone under 18 — while the App Store rates the app 12+ ([privacy policy](https://aippy.ai/privacy.html), [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)).

### Working conditions

Almost nothing is disclosed. The table records what exists rather than implying a policy where none is published.

| Item | Detail | Source |
|---|---|---|
| Open roles | None published. `aippy.ai/careers`, `/jobs` and `/about` all return the generic single-page shell, and no posting was found on any board searched | probed 2026-07-29 |
| Application route | `careers@aippy.ai`, named only in the privacy policy | [privacy policy](https://aippy.ai/privacy.html) |
| Location | LinkedIn lists San Jose; the operating entity is Singaporean; the former parent and the reporting are Beijing- and Hong-Kong-centred. No source states where engineers actually sit | [LinkedIn](https://www.linkedin.com/company/aippy/), [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| Team size and composition | ~30 people across algorithms, product and operations | [36氪首发, 2026-06-02](https://36kr.com/p/3834400181741440) |
| Remote policy, visa, benefits, salary, equity, turnover, interview process | Not published in any source reviewed | searched 2026-07-29 |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): `aippy.ai` fetched with and without a browser user agent, rendered in a browser, and probed at `/pricing`, `/careers`, `/jobs`, `/about`, `/blog`, `/changelog`, `/community`, `/explore` and `/discover`; `robots.txt`; the `status`, `blog`, `careers`, `jobs`, `api`, `docs`, `share`, `cdn`, `app` and `dev` subdomains; the full shipped JavaScript bundle; `api.aippy.ai` public endpoints; `docs.aippy.ai` including `llms.txt` and the welcome, FAQ, roadmap, changelog and pricing pages; the `AIPPY/Aippy-Docs` repository and its commit history; the `aippy` and `nadaai` GitHub organisation namespaces and a GitHub repository search; the npm registry for `aippy`; the App Store and Google Play listings and the iTunes lookup API; the terms of service and privacy policy; the Discord invite API for both published invites; the LinkedIn company page; Newborn Town's own site; and searches in Chinese and English for Aippy, NADA AI, 赤子城 + Aippy, Boomix/Boomiix, and Aippy hiring.

- **No engineering blog, technical post, talk or architecture material of any kind**, in either language.
- **No model provider, cloud provider, database or sandboxing mechanism is named** on any surface the company controls. For a product whose entire value is model-generated executable code, the inference stack is undisclosed.
- **No careers page and no job posting.** The only hiring signal is an email address inside the privacy policy.
- **No named employee other than the founder.** No co-founder, executive, or engineering lead appears anywhere; the npm maintainer handles are pseudonymous.
- **No security page, trust centre, subprocessor list or certification.** The privacy policy names categories of recipients ("payment processors", "cloud service providers (e.g., AWS, Google Cloud)") rather than actual subprocessors, and the observable origin is Alibaba Cloud OSS, which is not among them.
- **No corporate-registry record was retrieved.** NADA AI PTE. LTD. was not verified against ACRA; the Singapore jurisdiction is inferred from the `PTE. LTD.` suffix and the App Store and Google Play publisher fields.
- **No equity percentage** is published for Newborn Town's retained stake, and no round letter, closing date, tranche structure or board composition is stated.
- **Neither Aippy nor Newborn Town published its own announcement of the round.** Everything traces to one 36Kr exclusive of 2026-06-02.
- **No English-language press coverage was found.** All reporting located is Chinese-language.
- **The governing law of the terms is an unfilled template placeholder.** Section 16 of the [terms](https://aippy.ai/terms.html) (Last Updated 2026-06-16) reads "governed by the laws of [Jurisdiction, e.g., the State of California, USA]" and points disputes to "[Jurisdiction, e.g., San Francisco County, California]". No jurisdiction is actually specified.
- **Both published Discord invites are dead.** The docs invite `G94ZAx6gVq` returns "Invite is expired" and the bundle's `discord.com/invite/aippy` returns "Unknown Invite" (Discord invite API, 2026-07-29) — despite the company citing a 15,000-strong Discord core community.
- **The documentation is stale.** The last content commit to [AIPPY/Aippy-Docs](https://github.com/AIPPY/Aippy-Docs) is 2025-06-27 and the last changelog entry is v0.5.1 of 2025-06-25 — roughly thirteen months before this page's date, and predating the iOS launch entirely.

### Inconsistencies across sources

- **Free-tier quota, three different figures:** the live [pricing page](https://aippy.ai/pricing) says 500 credits per month (100 per daily login); the docs [pricing page](https://docs.aippy.ai/user-guides/pricing) says 30 requests per month; the [terms](https://aippy.ai/terms.html) §7.1 say 4 messages per day and 20 per month. Paid-tier quotas diverge the same way — the docs give 100/260/550/1,200 requests where the live page gives 80/200/400/800.
- **Capabilities versus roadmap, inside the same documentation site:** [welcome](https://docs.aippy.ai/welcome) presents backend logic, database integration, custom domains, payments and third-party integrations as current capabilities and the [FAQ](https://docs.aippy.ai/faq) states "Aippy generates full-stack applications", while the [roadmap](https://docs.aippy.ai/roadmap) lists all of them as "Coming Soon".
- **What the product is:** the documentation describes a general web-app and tool builder; the Chinese coverage and both app-store listings describe an AI game-creation community. The homepage metadata spans both.
- **App-store rating:** Newborn Town's January 2026 statement says 4.9 on both stores ([新浪财经, 2026-01-21](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml)); the June 2026 coverage says 4.8 on the US App Store; the [iTunes API](https://itunes.apple.com/lookup?id=6749073777) returned 4.86 from 20,849 US ratings on 2026-07-29.
- **Downloads:** the company states 3M+ globally (June 2026); [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) shows a 1M+ bucket for Android on 2026-07-29. These measure different things — cross-platform cumulative versus an Android-only bucket — and neither is auditable.
- **Launch date:** the [changelog](https://docs.aippy.ai/changelog) dates the web platform's first release to 2025-04-18 and the [iTunes API](https://itunes.apple.com/lookup?id=6749073777) dates the iOS release to 2025-07-28, while the coverage says simply "launched April 2025". The company is also described as "founded in 2025" without a month.
- **Model name:** Aippy-related content pages write "Boomix"; the first disclosure by the former parent writes "Boomiix" ([智通财经 via 新浪财经, 2025-03-04](https://finance.sina.com.cn/stock/hkstock/ggscyd/2025-03-04/doc-inenpfhz9590632.shtml)). Neither company has published a model page.
- **Age policy:** the [privacy policy](https://aippy.ai/privacy.html) states the service is not intended for anyone under 18; the App Store rates the app 12+ ([iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)).
- **Where the company is:** [LinkedIn](https://www.linkedin.com/company/aippy/) says San Jose; the app publisher is a Singapore entity; the incubator, the founder and all reporting are Chinese. No source reconciles the three.

### Other

- **A GitHub account presenting itself as Aippy carries a token address.** [github.com/AippyAI](https://github.com/AippyAI) is named "AippyAi official", lists `aippy.ai` and `@aippyai`, and was created 2025-12-12 with one follower. Its single repository's description reads "Aippy is an AI Vibe Coding platform powered by the Claude large model… flexibly integrates with three.js or pixi.js" followed by `98dNFeSKWwRLfAmchCP1ASwQaa1UhTJ3zynyEhvHpump` — a base58 string with the suffix pump.fun appends to tokens minted there. Its bio adds "Previously called MDCG". No Aippy surface links to this account, and the separate [AIPPY](https://github.com/AIPPY/Aippy-Docs) account — created 2025-04-02 and the actual source of `docs.aippy.ai` — is unconnected to it. The "powered by Claude" claim originates here and should not be read as a statement by the company.
- **The npm scope migration is the cleanest evidence of the spin-out.** The same runtime SDK, same description, same two maintainers, moved from `@new-born-town/aippy-runtime` (October 2025) to `@aippy/runtime` — a technical trace of the corporate separation that the filings and press describe.
- **Web analytics report to a third-party domain.** The ThinkingData SDK posts to `report.lolipopmobi.com`; `lolipopmobi.com` itself serves an unrelated legacy "Face App" site whose footer reads "Copyright © 2017-2020 Lbsbanana.ltd" ([lolipopmobi.com](https://lolipopmobi.com/), accessed 2026-07-29). The relationship between that operator and Aippy is not stated anywhere.
- **The site is unreadable to non-browser clients.** Requests without a browser user agent receive Alibaba Cloud OSS's `AccessDenied` XML rather than the page, so the product surface is invisible to naive crawlers and to the search results that quote it.
- **The company's own terms grant it a broad licence over published content**, royalty-free and without attribution, while stating that the user retains ownership; it also reserves the right to train models on prompts and code except for Enterprise Plan subscribers — a plan that appears in the terms but on none of the pricing pages ([terms](https://aippy.ai/terms.html)).
- **The content taxonomy is unusually explicit about the intended register** — "Mindless", "Brain Hack", "Unhinged", "Dopamine", "Send This" ([category API](https://api.aippy.ai/api/template/category_v2)) — and matches the feed-first, short-session framing in the coverage rather than the developer-tool framing in the documentation.
- **The valuation is material to the former parent.** $250M is described as approximately HK$2bn, put by one report at close to a sixth of Newborn Town's market capitalisation at the time ([新浪科技 / 投资界, 2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)).

---

## Resources

**Official**

- [Aippy — aippy.ai](https://aippy.ai/) · [pricing](https://aippy.ai/pricing)
- [Terms of Service — Last Updated 2026-06-16](https://aippy.ai/terms.html) · [Privacy Policy — Last Updated 2026-01-10](https://aippy.ai/privacy.html)
- [Web app bundle — the shipped JavaScript](https://aippy.ai/assets/js/index-BJ8REtwf.js)
- [Public category API](https://api.aippy.ai/api/template/category_v2)
- Documentation: [welcome](https://docs.aippy.ai/welcome) · [FAQ](https://docs.aippy.ai/faq) · [roadmap](https://docs.aippy.ai/roadmap) · [changelog](https://docs.aippy.ai/changelog) · [pricing](https://docs.aippy.ai/user-guides/pricing) · [Instant Edit](https://docs.aippy.ai/features/instand-edit) · [page index](https://docs.aippy.ai/llms.txt)
- [Documentation source — AIPPY/Aippy-Docs](https://github.com/AIPPY/Aippy-Docs)
- [npm packages published under the aippy and new-born-town scopes](https://registry.npmjs.org/-/v1/search?text=aippy)
- [App Store metadata — iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) · [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy)
- [LinkedIn](https://www.linkedin.com/company/aippy/) · [X — @aippyai](https://x.com/aippyai)
- [Newborn Town — former parent](https://www.newborntown.com/)

**Press releases**

- No release was published by Aippy or by Newborn Town for the 2026 funding round; the sources below are media coverage.

**Third-party coverage and profiles**

- [36氪首发 — 首轮融资数千万美元、估值2.5亿美元，「Aippy」正在打造下一代AI游戏社区, 2026-06-02 (ZH)](https://36kr.com/p/3834400181741440)
- [新浪科技 / 投资界 — 独家丨Aippy从赤子城剥离，估值2.5亿美元, 2026-06-02 (ZH)](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) · [投资界版本](https://news.pedaily.cn/202606/564739.shtml)
- [新浪财经 — 赤子城科技2025年营收67.6–70.0亿元，创新业务爆发式增长, 2026-01-21 (ZH)](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml)
- [智通财经 via 新浪财经 — 赤子城科技首次披露Boomiix模型, 2025-03-04 (ZH)](https://finance.sina.com.cn/stock/hkstock/ggscyd/2025-03-04/doc-inenpfhz9590632.shtml)
- [Wikipedia — NewBornTown](https://en.wikipedia.org/wiki/NewBornTown)

**Listed to prevent misattribution**

- [github.com/AippyAI/Aippy — unverified account whose repository description carries a pump.fun-style token address](https://github.com/AippyAI/Aippy)
- [lolipopmobi.com — the domain behind Aippy's analytics endpoint serves an unrelated legacy app site](https://lolipopmobi.com/)
