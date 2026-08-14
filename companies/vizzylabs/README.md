# Vizzy Labs

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-14.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Vizzy Labs sells creator-made short-form video to consumer brands. Its brand-facing site describes "The _Automatic_ UGC Video Platform for Real Growth — High-Quality UGC Videos, instantly. Paid by Performance", run by four named agents for trend analysis, creator sourcing, performance review and payout ([homepage](https://www.vizzylabs.ai/); accessed 2026-08-14). A second surface at `app.vizzylabs.ai` is a subscription product, "Vizzy AI | AI Video Search Engine for Creators", and a third at `vizzycircle.com` recruits the creators themselves. The legal entity named in every policy document is `Vispie Inc`, whose own former brand `Vispie AI` operated at `vispie.com` until at least early 2025 ([Terms of Service](https://www.vizzylabs.ai/terms); Last updated 2025-02-13) — see `Identity and legal entities`.

- Scale figures are all self-reported and inconsistent in scope: the brand site shows "2,159" videos generated, "674.3M" total views and "187.8M" total engagement, and says "We analyze 5M+ new videos every day" ([homepage](https://www.vizzylabs.ai/)); the creator site shows "10,000+ Creators", "$2M+ Deals Closed" and "50+ Brand Partners" ([vizzycircle.com](https://www.vizzycircle.com/)). The one independently countable number is the Vizzy Circle Discord server: 17,679 members, 367 online ([Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true); observed 2026-08-14).
- No funding announcement was found. The homepage badge reads "🚀 Venture Backed"; one job page says "backed by Sequoia Capital" ([Creative Strategist posting](https://www.vizzylabs.ai/careers/creative-strategist)); [CB Insights](https://www.cbinsights.com/company/vizzy-labs) instead lists "Seed VC" with GV, Bain Capital Ventures and Forerunner Ventures, with no amount or date — see `Funding`.
- The creator economics are published: "$30 flat fee + performance bonus ($10–$1,500) starting at 1K views", with a "Prime Creator program for higher flat fees", free to join, applications through a Google Form and a Discord community ([vizzycircle.com](https://www.vizzycircle.com/); accessed 2026-08-14).
- The company describes two different businesses in its own job posts: UGC and brand video on three of them, and "the future of interactive drama: short-form stories where viewers decide what happens next" on the other two ([careers](https://www.vizzylabs.ai/careers); accessed 2026-08-14) — see `Notes`.
- Engineering evidence comes from public assets: both sites are SvelteKit on Vercel; the app bundle references PostHog, Umami, Sentry, Google Tag Manager, Google Identity Services, Facebook Connect and Rewardful, and exposes API paths for video-format search, creator statistics, Meta ad-account proxying and Instagram post discovery (bundles inspected 2026-08-14).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brands | Vizzy Labs / Vizzy (brand-facing), Vizzy AI (`app.vizzylabs.ai`), Vizzy Circle (creator-facing) | [homepage](https://www.vizzylabs.ai/), [app.vizzylabs.ai](https://app.vizzylabs.ai/product), [vizzycircle.com](https://www.vizzycircle.com/); accessed 2026-08-14 |
| Legal entity | "Vispie Inc" — named as operator in both the Terms of Service and the Privacy Policy | [Terms of Service](https://www.vizzylabs.ai/terms), [Privacy Policy](https://www.vizzylabs.ai/privacy); Last updated 2025-02-13 |
| Entity as described to creators | "Vizzy Circle is operated by VizzyLabs (Vispie Inc.), a venture-backed AI video analytics company based in Stanford, CA … We are a registered U.S. company — not a scam, not a middleman" | [vizzycircle.com FAQ](https://www.vizzycircle.com/); accessed 2026-08-14 |
| Registered address | Not published on any reviewed page | see `Notes` |
| Stated location | "Stanford, CA" on the creator site; "San Francisco, California, United States" on a third-party profile; job posts say "SF / Hybrid / Remote" | [vizzycircle.com](https://www.vizzycircle.com/), [CB Insights](https://www.cbinsights.com/company/vizzy-labs), [careers](https://www.vizzylabs.ai/careers) |
| Founding year | Not stated by the company; a third-party profile gives 2025 | [CB Insights](https://www.cbinsights.com/company/vizzy-labs); accessed 2026-08-14 |
| Domain registrations | `vispie.com` created 2024-03-10 (GoDaddy, registrant "Domains By Proxy, LLC"); `vizzylabs.ai` created 2024-12-08 (GoDaddy); `vizzycircle.com` created 2026-01-06 (Cloudflare) | WHOIS records read 2026-08-14 |
| Copyright lines | "© 2025 Vizzy. All rights reserved." on the brand site; "© 2026 Vizzy Circle. All rights reserved." on the creator site | [homepage](https://www.vizzylabs.ai/), [vizzycircle.com](https://www.vizzycircle.com/) |
| Public contact | `support@vispie.com` (privacy contact); a Calendly link `calendly.com/yohanlee/30-minute-meeting` appears in the app bundle; the brand site collects leads through an on-page "Tell us about your product" form | [Privacy Policy](https://www.vizzylabs.ai/privacy), app JavaScript bundle inspected 2026-08-14 |
| Named people | Yohan Lee (Founder / CEO), Adham Zaki (Founding Engineer) | [The Org](https://theorg.com/org/vizzy-labs), [Luma event listing](https://luma.com/jfwqqbcv) |
| Headcount | Not published by the company. LinkedIn self-declares "11-50 employees" and lists 13 employee profiles; The Org lists 2 people | [LinkedIn](https://www.linkedin.com/company/vizzylabs), [The Org](https://theorg.com/org/vizzy-labs); accessed 2026-08-14 |
| Social accounts | Instagram `@vizzy_labs` (168 followers, 8 posts), X `@vizzylabs_ai` (5 followers, joined May 2025), TikTok `@vizzy_labs`, Facebook pages `vizzylabs` and `vizzycircle`, LinkedIn `vizzylabs` (947 followers) | profiles accessed 2026-08-14 |
| Creator community | Discord server "Vizzy Circle" (guild id `1413650512359985254`): 17,679 approximate members, 367 online; invite issued by "Amy - Vizzy Account Manager" | [Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true); observed 2026-08-14 |
| Legal documents | Terms of Service and Privacy Policy, both "Last updated: Feb 13th, 2025"; no cookie policy, DPA, security page or subprocessor list | [Terms](https://www.vizzylabs.ai/terms), [Privacy Policy](https://www.vizzylabs.ai/privacy) |
| Hosting | Both `www.vizzylabs.ai` and `www.vizzycircle.com` return `server: Vercel`; `www.vizzylabs.ai` also returns `x-sveltekit-page: true` | response headers observed 2026-08-14 |

**Named brands and customers as claimed by the company.** The brand site's "Success stories" section names "MrBeast Chocolate — 2.3M views", "Manus AI — +67% conversions" and "Study X — 1M+ installs", above a logo strip reading "alpha, buoy, chance, chime, dose, remini, rocket" ([homepage](https://www.vizzylabs.ai/); accessed 2026-08-14). The creator site says it is "trusted by brands like Madnesz & Cluely" and carries a longer logo strip: "alpha, buoy, chance, chime, dose, honeylove, remini, rocket, scoopz, tarte" ([vizzycircle.com](https://www.vizzycircle.com/); accessed 2026-08-14). None of these relationships was confirmed from the named brands' own materials in the reviewed sources.

**Events.** The company appeared in a StartX "Founder Spotlight" virtual session titled "Explore the growth tactics behind viral apps like Cluely, Turbolearn, and PingoAI with Vizzy Labs", hosted by StartX, the Stanford-affiliated accelerator community; the event is shown as past and undated on the listing ([Luma](https://luma.com/jfwqqbcv); accessed 2026-08-14).

### Identity and legal entities

| Name | Type | Period / status | Relationship as stated | Source |
|---|---|---|---|---|
| Vizzy Labs / Vizzy | Public brand, brand-facing | Current | Name used on the site, careers pages, social accounts and in press-style descriptions | [homepage](https://www.vizzylabs.ai/) |
| Vispie Inc | Legal entity | Current | Named as the operator of the Service in the Terms and Privacy Policy; named to creators as the entity governing creator agreements | [Terms](https://www.vizzylabs.ai/terms), [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| Vispie AI | Former brand at `vispie.com` | Live as of the 2025-01-30 archive capture; `www.vispie.com` failed the TLS handshake on 2026-08-14 | Positioned as "Your Data + Our Trend Engine = Viral Videos in Minutes", "Trusted by 20+ enterprises", footer "© VisPie.AI. 2024" | [Wayback capture, 2025-01-30](https://web.archive.org/web/20250130073405/http://www.vispie.com/) |
| Vizzy Circle | Creator-network brand at `vizzycircle.com` | Domain created 2026-01-06 | "operated by VizzyLabs (Vispie Inc.)" | [vizzycircle.com](https://www.vizzycircle.com/) |
| Unrelated companies named "Vizzy" | Name collision | — | A London recruitment startup also trades as Vizzy and raised £3.65M led by Adjuvo in April 2025; funding-database results for "Vizzy" frequently return it instead of this company | [UNLEASH, 2025](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/) |

The Terms describe the business in terms that match the older product rather than the current homepage: "Vispie Inc provides an AI search and analysis service for advertising videos. Vispie Inc is available via www.vizzylabs.ai" ([Terms](https://www.vizzylabs.ai/terms); Last updated 2025-02-13). No corporate registry filing for `Vispie Inc` was retrieved, so its state of incorporation, registered address and officers are not established here — see `Notes`.

---

## Product

### Surfaces

| Surface | Audience | What it is | Source |
|---|---|---|---|
| `www.vizzylabs.ai` | Brands | "The Automatic UGC Video Platform for Real Growth. High-Quality UGC Videos, instantly. Paid by Performance." — "Vizzy's AI recruits, evaluates, and manages real and AI creators, so you get high-performing UGC on autopilot" | [homepage](https://www.vizzylabs.ai/); accessed 2026-08-14 |
| `app.vizzylabs.ai` | Creators and marketers | "Vizzy AI | AI Video Search Engine for Creators" — creative research, video storyboard analysis, viral-video search, trending creative tracker, video script extraction, plus a Meta-connected creative performance dashboard | [app.vizzylabs.ai](https://app.vizzylabs.ai/product); accessed 2026-08-14 |
| `www.vizzycircle.com` | Creators | "Vizzy Circle — Premium UGC Creator Network": apply, get matched to brand campaigns, receive 1-on-1 coaching, deliver UGC, get paid | [vizzycircle.com](https://www.vizzycircle.com/); accessed 2026-08-14 |
| Discord + Google Form | Creators | Intake and community: a "Vizzy Circle Creator Network Application" Google Form and a Discord server | [application form](https://docs.google.com/forms/d/e/1FAIpQLSd_ooDJ4m5hFQecHzZ2BEyo3DO0GbQ3_6-q0VvmDdoy9PI8Lw/viewform), [Discord invite](https://discord.gg/MZhbHg7Q5Z) |

### The four-agent workflow as described

The brand site organises the product as "Vizzy's Agentic Workflow" in four steps ([homepage](https://www.vizzylabs.ai/); accessed 2026-08-14):

| Step | Agent | What the page says it does |
|---|---|---|
| 1 | Trend & Competitor Agent | "We analyze 5M+ new videos every day to detect viral formats, trending audio and winning hooks — before they peak"; tracks "competitor creatives, formats, and performance signals" |
| 2 | Creator Sourcing Agent | "Creators are sourced based on historical performance, audience match, and format compatibility — selecting creators with the highest probability of success for your app" |
| 3 | Performance Review Agent | "After filming, AI agents perform automated analysis, with human experts validating critical decisions" |
| 4 | Data Optimization & Payout Agent | "Once videos go live, performance data is processed through our agent to automate payouts and improve creator selection and creative decisions over time" |

### Commercialization

| Item | Detail | Source |
|---|---|---|
| Brand-side model | "Paid by Performance"; no price list, rate card or minimum is published; the only call to action is a "Tell us about your product" form | [homepage](https://www.vizzylabs.ai/); accessed 2026-08-14 |
| App subscription tiers | Basic free ("3 searches per day", limited access); Creator US$29/month or US$25/month billed yearly; Pro US$99/month or US$79/month billed yearly; Enterprise "Custom — Contact Sales"; yearly billing marked "(20% off)" | [app.vizzylabs.ai](https://app.vizzylabs.ai/product); accessed 2026-08-14 |
| App tier limits | Creator: 50 video storyboard analyses, 100 creative research per month, unlimited access to "50M viral videos", unlimited trending creative tracker and script extractions. Pro: 1,000 storyboard analyses, unlimited creative research. Enterprise adds "Personalized onboarding and CSM", "Personalized creative reports", "Customized competitor tracker" | [app.vizzylabs.ai](https://app.vizzylabs.ai/product) |
| Creator compensation | "$30 flat fee + performance bonus ($10–$1,500) starting at 1K views"; "Top performers can join our Prime Creator program for higher flat fees"; "Rates may vary by campaign" | [vizzycircle.com FAQ](https://www.vizzycircle.com/); accessed 2026-08-14 |
| Creator costs | "Vizzy Circle is 100% free to join — no paid onboarding, no hidden fees, no product purchases required, and no upfront costs of any kind. We pay you; you never pay us. If a campaign involves a product, it will be provided to you at no cost." | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| Creator contracts | "Yes, there is a written creator agreement that outlines compensation, deliverables, payment terms, and content usage rights before you start any campaign … All terms and conditions are governed by VizzyLabs (Vispie Inc.)"; the agreement itself is not published | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| Creator entry requirements | "No experience and zero followers required"; "many creators go from complete beginners to earning $1,000+/month"; "Most active creators run 3-4 campaigns simultaneously … Top performers managing multiple campaigns scale to $3K-$10K monthly" | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| Referral / affiliate tracking | The app bundle loads `r.wdfl.co/rw.js` (Rewardful), indicating an affiliate-tracking integration | app JavaScript bundle inspected 2026-08-14 |

### Positioning over time

The public positioning has changed three times in about eighteen months, each version documented by an archived capture.

| Date | Site and title | Positioning as written |
|---|---|---|
| 2025-01-30 | `vispie.com` — "Vispie AI" | "Your Data + Our Trend Engine = Viral Videos in Minutes"; "Trusted by 20+ enterprises"; features listed as viral-video discovery, competitor search, video analysis and "Automatic Batch Video Editing Powered by Trend AI" ([Wayback](https://web.archive.org/web/20250130073405/http://www.vispie.com/)) |
| 2025-06-18 | `vizzylabs.ai` — "Vizzy Labs \| AI-Powered TikTok Ad Creative Strategist" | "AI Creative Strategist to Ship Winning Ads. Find winning video formats instantly from our ads library with 500,000,000+ TikTok & Instagram ads and organic content"; page built with Framer ([Wayback](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/)) |
| 2025-12-08 | `vizzylabs.ai` — "Vizzy AI \| AI Video Search Engine for Creators" | Subscription product with the Creator/Pro/Enterprise/Basic tiers still live today at `app.vizzylabs.ai`; "Unlimited access to 50M viral videos" ([Wayback](https://web.archive.org/web/20251208202228/https://www.vizzylabs.ai/)) |
| 2026-05-17 to 2026-08-14 | `vizzylabs.ai` — "Vizzy: Automatic UGC Video Platform" | The current four-agent, performance-paid UGC positioning ([Wayback](https://web.archive.org/web/20260517154252/https://www.vizzylabs.ai/), [homepage](https://www.vizzylabs.ai/)) |

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2024-03-10 | `vispie.com` domain registered | WHOIS read 2026-08-14 |
| 2024-12-08 | `vizzylabs.ai` domain registered | WHOIS read 2026-08-14 |
| 2025-01-30 | Vispie AI: "Trusted by 20+ enterprises" | [Wayback](https://web.archive.org/web/20250130073405/http://www.vispie.com/) |
| 2025-05 | X account `@vizzylabs_ai` created | [X profile](https://x.com/vizzylabs_ai); accessed 2026-08-14 |
| 2025-06-18 | Ads library described as "500,000,000+ TikTok & Instagram ads and organic content" | [Wayback](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/) |
| 2025-12-08 | App plans describe "Unlimited access to 50M viral videos" | [Wayback](https://web.archive.org/web/20251208202228/https://www.vizzylabs.ai/) |
| 2026-01-06 | `vizzycircle.com` domain registered | WHOIS read 2026-08-14 |
| Undated (past event) | "engineered over 650M views on social media"; works with "apps backed by a16z, GV, and Forerunner Ventures"; founder "led the TikTok Creative Center product, growing it from an internal tool to a platform used by 6M advertisers" | [Luma / StartX Founder Spotlight](https://luma.com/jfwqqbcv) |
| Accessed 2026-08-14 | Brand site: "2,159" videos generated, "674.3M" total views ("Avg 312.3K views per video"), "187.8M" total engagement ("Avg 87K interactions per video"), "5M+" new videos analyzed daily | [homepage](https://www.vizzylabs.ai/) |
| Accessed 2026-08-14 | Creator site: "10,000+ Creators", "$2M+ Deals Closed", "50+ Brand Partners" | [vizzycircle.com](https://www.vizzycircle.com/) |
| Observed 2026-08-14 | Discord server: 17,679 approximate members, 367 online | [Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true) |
| Accessed 2026-08-14 | LinkedIn 947 followers, "11-50 employees", 13 employee profiles; Instagram 168 followers and 8 posts; X 5 followers | [LinkedIn](https://www.linkedin.com/company/vizzylabs), [Instagram](https://www.instagram.com/vizzy_labs/), [X](https://x.com/vizzylabs_ai) |

No revenue, paying-customer, campaign-count or payout-total figure other than the "$2M+ Deals Closed" banner is published — see `Notes`.

### Stated plans

The company does not publish a roadmap page. The forward-looking statements found are in job postings: "Building the future of brand video — where AI meets creativity to transform how brands create and scale video content" ([careers](https://www.vizzylabs.ai/careers)), and, on two postings, "building the future of interactive drama: short-form stories where viewers decide what happens next", with experience at "drama apps (ReelShort, DramaBox, Mango, or similar) or game platforms (Roblox, Epic, or similar)" listed as "a major plus" ([Scriptwriters & Producers posting](https://www.vizzylabs.ai/careers/ai-agent-engineer), [Marketing Roles posting](https://www.vizzylabs.ai/careers/marketing-roles); accessed 2026-08-14). Within the app, "TikTok" and "Youtube" appear as ad-platform connectors marked "Coming soon", with Meta the only live connector ([app.vizzylabs.ai](https://app.vizzylabs.ai/product)).

---

## Founder

**Yohan Lee** — listed as "Founder" on The Org and indexed on LinkedIn as "Founder @ Vizzy Labs | Stanford"; the LinkedIn profile returned HTTP 999 to automated access on 2026-08-14 and was not read ([The Org](https://theorg.com/org/vizzy-labs/org-chart/yohan-lee), [LinkedIn](https://www.linkedin.com/in/yohanlee12/)). The StartX event listing describes him as "the founder and CEO of Vizzy Labs, and former TikTok Creative AI PM, where he led the TikTok Creative Center product, growing it from an internal tool to a platform used by 6M advertisers" ([Luma](https://luma.com/jfwqqbcv); accessed 2026-08-14). The name is corroborated inside the product: the app JavaScript bundle contains the scheduling link `https://calendly.com/yohanlee/30-minute-meeting` (bundle inspected 2026-08-14). No education dates, employment dates or prior companies beyond TikTok are published in the reviewed sources.

**Adham Zaki** — listed as "Founding Engineer" ([The Org](https://theorg.com/org/vizzy-labs); accessed 2026-08-14). No other detail is published.

The company describes its founding team only in aggregate, and the descriptions differ by posting: "founded by Stanford and Google alumni" on two postings, and "Founded by operators from TikTok, Google, and Stanford" on another ([Scriptwriters & Producers posting](https://www.vizzylabs.ai/careers/ai-agent-engineer), [Marketing Roles posting](https://www.vizzylabs.ai/careers/marketing-roles), [Creative Strategist posting](https://www.vizzylabs.ai/careers/creative-strategist)).

A person operating as "Amy - Vizzy Account Manager" issued the public Discord invite for the creator community ([Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true); observed 2026-08-14). No team page, leadership page or about page exists on `vizzylabs.ai` — `/about`, `/team` and `/company` redirect to `app.vizzylabs.ai` and do not resolve to content (paths checked 2026-08-14).

---

## Funding

No financing announcement by the company was found in the reviewed public sources as of 2026-08-14. There is no press page, investor page or funding statement on any of the three sites. The table records what the company asserts and what third-party profiles state.

| Date | Claim | Amount | Investors named | Source |
|---|---|---|---|---|
| Accessed 2026-08-14 | "🚀 Venture Backed" badge in the homepage footer area | Not stated | None | [homepage](https://www.vizzylabs.ai/) |
| Accessed 2026-08-14 | "Founded by operators from TikTok, Google, and Stanford and backed by Sequoia Capital, Vizzy Labs is already powering campaigns across fast-growing consumer brands, generating millions of views each month" | Not stated | Sequoia Capital | [Creative Strategist posting](https://www.vizzylabs.ai/careers/creative-strategist) |
| Accessed 2026-08-14 | "a Silicon Valley top VC-backed startup"; "backed by some of the top VCs in the space" | Not stated | None | [Scriptwriters & Producers posting](https://www.vizzylabs.ai/careers/ai-agent-engineer), [AI Video Creators posting](https://www.vizzylabs.ai/careers/ai-video-creators) |
| Accessed 2026-08-14 | "a venture-backed AI video analytics company based in Stanford, CA" | Not stated | None | [vizzycircle.com FAQ](https://www.vizzycircle.com/) |
| Accessed 2026-08-14 | "latest funding round is Seed VC"; founded 2025; headquartered in San Francisco | Not stated | GV, Bain Capital Ventures, Forerunner Ventures | [CB Insights](https://www.cbinsights.com/company/vizzy-labs) |

Two cautions apply to the third-party figures. First, the same three investor names — a16z, GV and Forerunner Ventures — appear in the company's own event blurb as investors in its *customers*, not in Vizzy Labs ("Working with apps backed by a16z, GV, and Forerunner Ventures", [Luma](https://luma.com/jfwqqbcv)); no source reviewed reconciles the two uses. Second, general web and database searches for "Vizzy" return a separate London recruitment startup that raised £3.65M led by Adjuvo in April 2025 ([UNLEASH](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/), [Crunchbase funding round](https://www.crunchbase.com/funding_round/vizzy-6454-seed--2028b984)); that round is not this company's. Amount, date, lead investor and valuation are not established by any source reviewed. Sequoia Capital's own portfolio listing was not checked against this claim — see `Notes`.

---

## Engineering

### Technology stack and platforms

No stack page is published. Items below are confirmed by observable public assets unless labelled otherwise (all observed 2026-08-14).

- **Brand site:** SvelteKit on Vercel — `www.vizzylabs.ai` returns `server: Vercel` and `x-sveltekit-page: true`, with `_app/immutable/` asset paths; DNS resolves through `vercel-dns-016.com`. `robots.txt` allows all crawling and no sitemap is served.
- **Application:** `app.vizzylabs.ai` is also SvelteKit on Vercel, serves `robots.txt` and `sitemap.xml`, and 302-redirects its root to `/product`.
- **Creator site:** `www.vizzycircle.com` is likewise served by Vercel with `_app/immutable/` assets; intake runs on Google Forms and community on Discord rather than on first-party infrastructure.
- **Previous site generation:** the 2025-06-18 archived homepage carries `framer-*` class names, indicating the marketing site was built in Framer before the SvelteKit rewrite ([Wayback](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/)).
- **Analytics, error tracking and marketing tags (from the app JavaScript bundles):** PostHog (`us.i.posthog.com`, `app.posthog.com`), Umami (`cloud.umami.is/script.js`), Sentry, Google Tag Manager, Facebook Connect, and Rewardful (`r.wdfl.co/rw.js`). Iconify (`api.iconify.design`, `api.simplesvg.com`, `api.unisvg.com`) is used for icons.
- **Authentication:** Google Identity Services (`accounts.google.com/gsi/client`) plus an email login path; the login modal offers "Continue with Email" alongside social login.
- **Ad-platform integration:** Meta is the only live connector ("Track Facebook & Instagram campaigns"), with TikTok and YouTube shown as "Coming soon"; the app also surfaces a "Reconnect your Facebook account" flow and campaign "Naming Conventions" tooling.
- **No public code:** no GitHub organisation exists under `vizzylabs`, `vizzy-labs` or `VizzyLabs`, and npm returns no packages for "vizzylabs". A GitHub organisation named `VisPie` exists (created 2024-06-03) but has zero public repositories, no members and no profile metadata, so it cannot be confirmed as this company's (API checks 2026-08-14).
- **Legacy domain:** `www.vispie.com` resolves but failed the TLS handshake on 2026-08-14 (`tlsv1 alert internal error`), so the former brand's site is not currently reachable over HTTPS; the privacy contact address `support@vispie.com` still points at that domain.

### Systems

The app's own JavaScript bundle exposes its backend route names, which is the most concrete public description of what the company operates.

| System | Evidence | Source |
|---|---|---|
| Video-format search and trend ranking | `/api/v1/video-formats/v2/search`, `/api/v1/video-formats/v2/trending` | app JavaScript bundles inspected 2026-08-14 |
| Video corpus and creator statistics | `/api/v1/video/videos`, `/api/v1/video/videos/batch`, `/api/v1/video/videos/creators`, `/api/v1/video/videos/stats`, `/api/v1/content/batch/media-urls` | app JavaScript bundles inspected 2026-08-14 |
| Meta ads ingestion and reporting | `/api/v1/meta-ads/batch` and a proxy layer at `/api/proxy/facebook/auth/init/`, `/ad-accounts/`, `/accounts/status/`, `/reports/`, `/tags/`, `/categories/`, `/available-actions/all/` | app JavaScript bundles inspected 2026-08-14 |
| Instagram content discovery | `/api/discovery/instagram/posts/` and `/api/proxy/discovery/instagram/posts/` | app JavaScript bundles inspected 2026-08-14 |
| Exploration and industry browsing | `/api/explore/search`, `/api/explore/industry` | app JavaScript bundles inspected 2026-08-14 |
| Automated criteria generation ("autopilot") | `/api/v1/autopilot/generate-criteria` | app JavaScript bundles inspected 2026-08-14 |
| Dashboards and surveys | `/api/v1/dashboards`, `/api/proxy/survey/surveys/` | app JavaScript bundles inspected 2026-08-14 |
| Creator recruiting and payout operations | Described on the sites rather than exposed as endpoints: creator sourcing, 1-on-1 coaching, campaign briefs and script templates, performance-triggered bonus payouts | [homepage](https://www.vizzylabs.ai/), [vizzycircle.com](https://www.vizzycircle.com/) |

### Data handling as documented

The Privacy Policy is a short general-purpose document: it lists account data, usage data, IP address, browser and OS, says "We do not sell your personal information", names no subprocessor, states no retention period, offers no GDPR or CCPA rights section, and sets the children's threshold at 13 ([Privacy Policy](https://www.vizzylabs.ai/privacy); Last updated 2025-02-13).

Two clauses in the Terms are worth quoting as written. On user content: "While Vispie Inc holds the copyright, you are granted the right to use the content", followed by a broad licence in which the user grants "a worldwide license to use, host, store, reproduce, modify, create derivative works … communicate, publish, publicly perform, publicly display and distribute such content". On data collection: "You agree not to conduct any systematic or automated data collection activities (including scraping, data mining, data extraction or data harvesting) on or in relation to the Service. Prohibited data collection includes, but is not limited to, using the Service as input into other services, websites, or databases." ([Terms](https://www.vizzylabs.ai/terms); Last updated 2025-02-13). The product itself is described on the marketing side as analysing "5M+ new videos every day" from TikTok, Instagram and YouTube ([homepage](https://www.vizzylabs.ai/), [Algorithm Engineer posting](https://www.vizzylabs.ai/careers/algorithm-engineer)); no page states how that data is obtained or under what licence.

### Technical background sought

All of the following comes from the postings on [vizzylabs.ai/careers](https://www.vizzylabs.ai/careers) (accessed 2026-08-14). Only one is an engineering role.

**Algorithm Engineer** — SF / Hybrid / Remote, full-time, no salary published.

- *Responsibilities:* "Develop and optimize video analysis models (scene detection, hook analysis, engagement prediction)"; "Build NLP pipelines for content tagging, sentiment analysis, and trend extraction"; "Design recommendation algorithms for content strategy suggestions"; "Work with large-scale social media datasets (TikTok, Instagram, YouTube)"; "Deploy models to production and monitor performance".
- *Required:* "MS/PhD in Computer Science, Machine Learning, or related field (or equivalent experience)"; "Strong background in deep learning (PyTorch/TensorFlow)"; "Experience with computer vision or NLP in production"; "Proficiency in Python and familiarity with ML infrastructure (AWS SageMaker, Docker)".
- *Preferred:* published papers or research experience; "video understanding or multimodal models"; "Knowledge of LLMs and prompt engineering"; recommendation systems; "social media data at scale".
- *Stated offer:* "Access to large-scale social media datasets"; "Competitive compensation + equity"; "Publish research and attend conferences".

**Non-engineering postings** — a Creative Strategist role ("2–4+ years in creative strategy, creator marketing, performance social", with "English / Chinese bilingual" and "Familiarity with AI tools" as nice-to-haves); AI Video Creators ("Deep experience with AI video generation tools" naming "Higgsfield, Creatify, Kling, Veo, or similar"); Scriptwriters & Producers; and four marketing tracks (media buying on Meta and TikTok, social content, page management, growth and community).

### Industry domain

The work spans creator-marketing operations — sourcing and vetting creators, campaign briefing, content review, and performance-linked payout — alongside paid social measurement on Meta and, as stated future work, TikTok and YouTube ([homepage](https://www.vizzylabs.ai/), [app.vizzylabs.ai](https://app.vizzylabs.ai/product)). It also involves large-scale collection and analysis of third-party social video ([Algorithm Engineer posting](https://www.vizzylabs.ai/careers/algorithm-engineer)), disclosure rules for paid creator content, written creator agreements covering "compensation, deliverables, payment terms, and content usage rights" ([vizzycircle.com FAQ](https://www.vizzycircle.com/)), and the two vertical-drama and game-platform ecosystems named in the scriptwriting and marketing postings (ReelShort, DramaBox, Mango; Roblox, Epic).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Careers page | `vizzylabs.ai/careers`, five postings, application through an on-page "Apply for This Position" form | [careers](https://www.vizzylabs.ai/careers); accessed 2026-08-14 |
| Locations | "SF / Hybrid / Remote" on four postings; "Remote" on AI Video Creators | [careers](https://www.vizzylabs.ai/careers) |
| Employment types | Full-time, part-time and freelance are all offered depending on the role | [careers](https://www.vizzylabs.ai/careers) |
| Published salary bands | Creative Strategist US$60,000–100,000 "+ Meaningful Equity"; Scriptwriters & Producers US$60,000–120,000 (full-time); AI Video Creators US$60,000–150,000; Marketing US$60,000–120,000; Algorithm Engineer — no band published, "Competitive compensation + equity" | [careers](https://www.vizzylabs.ai/careers) |
| Application deadlines | "Application deadline: July 14, 2026" (Scriptwriters & Producers) and "Application Deadline: July 7, 2026" (Marketing); both had passed when the pages were read on 2026-08-14, and the postings were still live | [Scriptwriters & Producers posting](https://www.vizzylabs.ai/careers/ai-agent-engineer), [Marketing Roles posting](https://www.vizzylabs.ai/careers/marketing-roles) |
| Reporting line | The Creative Strategist role is "reporting directly to founders" | [Creative Strategist posting](https://www.vizzylabs.ai/careers/creative-strategist) |
| Working language | Not stated as a policy; "English / Chinese bilingual" appears as a nice-to-have on one posting | [Creative Strategist posting](https://www.vizzylabs.ai/careers/creative-strategist) |
| Benefits, visa sponsorship, interview process, office address, turnover | Not published | see `Notes` |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-08-14): `www.vizzylabs.ai` homepage, `/careers` and all five posting pages, `/privacy`, `/terms`, `robots.txt`, and probes of `/about`, `/company`, `/team`, `/blog`, `/pricing`, `/contact`, `/press`, `/docs`, `/jobs` and `/sitemap.xml`; `app.vizzylabs.ai` `/product`, `/pricing`, `/legal/terms-of-service`, `/legal/privacy-policy`, `robots.txt`, `sitemap.xml` and its JavaScript bundles; `www.vizzycircle.com` and its FAQ, its Discord invite and its Google application form; `api.vizzylabs.ai` and several other subdomains; `vispie.com` over HTTP and HTTPS; WHOIS for all three domains; Wayback Machine CDX indexes for `vizzylabs.ai` and `vispie.com`; the Instagram, X, TikTok, Facebook and LinkedIn accounts; the Discord invite API; GitHub and npm; CB Insights, Crunchbase, Tracxn and The Org; the StartX Luma listing and the StartX community directory; and English-language searches on the brand names, the entity name and the founder's name.

- **Any funding amount, date, lead investor or valuation.** No announcement exists on any company surface; the claims found are a badge, a single job-page mention of Sequoia Capital, and a database entry naming three different investors — see `Inconsistencies`.
- **A corporate registry record for `Vispie Inc`.** No filing was retrieved, so state of incorporation, registered address, officers and standing are not established. No registered address appears on any company page; the only geography given is "Stanford, CA" on the creator site.
- **Headcount and who works there.** No team page exists; only two people are named anywhere in the reviewed sources, both on a third-party org-chart site.
- **Anything about how the video corpus is collected or licensed.** The company advertises analysis of millions of TikTok, Instagram and YouTube videos daily and, in an earlier version, a library of "500,000,000+" ads, while its own Terms prohibit automated data collection "on or in relation to the Service"; no page states the source, licence or platform-API basis of the corpus.
- **Model, provider and infrastructure detail.** No model, inference provider, cloud region or data-processing location is named on any page or in either policy; AWS SageMaker and Docker appear only as hiring requirements, which does not establish production use.
- **Brand-side pricing.** "Paid by Performance" is the only stated commercial model for brands; no rate card, minimum spend, CPM/CPV basis or contract term is published.
- **The creator agreement.** The creator FAQ says a written agreement governs compensation, deliverables, payment terms and content usage rights, but the agreement is not published; nor is a payout schedule, dispute process, tax-form requirement or eligibility jurisdiction.
- **Any customer confirmation.** The named brands (MrBeast Chocolate, Manus AI, Study X, Madnesz, Cluely) and the logo strips appear only on the company's own pages; no case study, press release or statement from any named brand was found.
- **Security, compliance and data-protection posture.** No security page, certification, subprocessor list, DPA, status page or vulnerability-disclosure contact exists; the Privacy Policy names no subprocessor and states no retention period.
- **An engineering blog, documentation or open source.** None found. `/docs` and `/blog` redirect into the app and do not resolve; there is no public repository or package under either brand name.
- **Sources that blocked automated access on 2026-08-14:** Crunchbase (HTTP 403), the founder's LinkedIn profile (HTTP 999), TikTok profile pages (HTTP 403 to a plain fetch). Where those appear above, wording comes from search-result summaries or alternative sources and is labelled accordingly.

### Inconsistencies across sources

- **Which business the company is in.** Three postings and both public sites describe UGC and brand video; two postings describe "the future of interactive drama: short-form stories where viewers decide what happens next", with drama-app and game-platform experience as a plus ([careers](https://www.vizzylabs.ai/careers), [Scriptwriters & Producers posting](https://www.vizzylabs.ai/careers/ai-agent-engineer), [Marketing Roles posting](https://www.vizzylabs.ai/careers/marketing-roles)). The Terms describe a third thing: "an AI search and analysis service for advertising videos" ([Terms](https://www.vizzylabs.ai/terms)).
- **Investors.** One job page states "backed by Sequoia Capital" ([Creative Strategist posting](https://www.vizzylabs.ai/careers/creative-strategist)); [CB Insights](https://www.cbinsights.com/company/vizzy-labs) lists GV, Bain Capital Ventures and Forerunner Ventures; the homepage and creator site say only "venture backed"; and the company's own event blurb uses a16z, GV and Forerunner Ventures to describe its customers' investors ([Luma](https://luma.com/jfwqqbcv)). No two of these agree.
- **Location.** "Stanford, CA" ([vizzycircle.com](https://www.vizzycircle.com/)) versus "San Francisco, California" ([CB Insights](https://www.cbinsights.com/company/vizzy-labs)) versus "SF / Hybrid / Remote" in postings.
- **Corpus size.** "500,000,000+ TikTok & Instagram ads and organic content" (2025-06 site), "50M viral videos" (app plan copy, 2025-12 to present), and "5M+ new videos every day" analysed (current homepage) describe different quantities without a stated relationship between them.
- **Creator community size.** The creator site says "10,000+ Creators" while the Discord server it points to reports 17,679 members ([vizzycircle.com](https://www.vizzycircle.com/), [Discord invite API](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true); both 2026-08-14).
- **A job URL that does not match its content.** `vizzylabs.ai/careers/ai-agent-engineer` renders the "Vizzy Labs | Scriptwriters & Producers" posting, and no AI-agent-engineer posting exists on the careers index (checked 2026-08-14).
- **Copyright years across surfaces.** "© 2025 Vizzy" on the brand site versus "© 2026 Vizzy Circle" on the creator site (both accessed 2026-08-14).
- **Name collision in databases.** Funding databases and search engines return a London recruitment startup called Vizzy (£3.65M seed led by Adjuvo, April 2025) and, separately, a hard-seltzer brand; neither is this company ([UNLEASH](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/), [Crunchbase funding round](https://www.crunchbase.com/funding_round/vizzy-6454-seed--2028b984)).

### Other

- **Three brands, three domains, three audiences, one entity.** `vizzylabs.ai` sells to brands, `app.vizzylabs.ai` sells subscriptions to marketers and creators, and `vizzycircle.com` recruits creators; all three name or are governed by `Vispie Inc`, and only the middle one has a published price list.
- **The legal documents predate the current product.** Both are dated 2025-02-13 — before the app subscription tiers, before the UGC platform positioning, and about eleven months before the creator network's domain was registered — and they describe the business as an ad-video search service.
- **The privacy contact points at a domain that no longer serves a site.** `support@vispie.com` is the stated contact, while `www.vispie.com` failed the TLS handshake on 2026-08-14.
- **The creator-facing FAQ leads with a legitimacy question.** Its first entry is "Is Vizzy Circle a legitimate company? How can I verify?", answered with the entity name, the website, the social accounts and the Discord size ([vizzycircle.com](https://www.vizzycircle.com/)); creator-side scepticism is also visible as a recurring TikTok search topic.
- **Audience distribution is lopsided.** The Discord community reports 17,679 members while the X account has 5 followers and Instagram 168 followers with 8 posts (all 2026-08-14) — the company's reach sits in a closed community rather than on its public accounts.
- **The creator testimonials are unattributable.** All three are first name plus initial ("Jess R.", "Marcus K.", "Aisha T.") with a category rather than a handle ([vizzycircle.com](https://www.vizzycircle.com/)).
- **The homepage counters render as "0+".** The three headline stat cards ("Top creators", "Videos analyzed", "Converted Views") are client-side animated counters that show "0+" in the served HTML; the concrete figures appear further down the page (observed 2026-08-14).
- **The marketing stack is unusually heavy for the size of the public footprint:** PostHog, Umami, Sentry, Google Tag Manager, Facebook Connect and Rewardful affiliate tracking all ship in the app bundle (inspected 2026-08-14).

---

## Resources

**Official**

- [Homepage](https://www.vizzylabs.ai/) · [Careers](https://www.vizzylabs.ai/careers) · [robots.txt](https://www.vizzylabs.ai/robots.txt)
- Job postings — [Creative Strategist](https://www.vizzylabs.ai/careers/creative-strategist) · [Scriptwriters & Producers](https://www.vizzylabs.ai/careers/ai-agent-engineer) · [AI Video Creators](https://www.vizzylabs.ai/careers/ai-video-creators) · [Marketing Roles](https://www.vizzylabs.ai/careers/marketing-roles) · [Algorithm Engineer](https://www.vizzylabs.ai/careers/algorithm-engineer)
- [Terms of Service](https://www.vizzylabs.ai/terms) · [Privacy Policy](https://www.vizzylabs.ai/privacy) — both Last updated 2025-02-13
- [Vizzy AI application](https://app.vizzylabs.ai/product) · [app Terms of Service](https://app.vizzylabs.ai/legal/terms-of-service) · [app Privacy Policy](https://app.vizzylabs.ai/legal/privacy-policy)
- [Vizzy Circle](https://www.vizzycircle.com/) · [Vizzy Circle Discord invite](https://discord.gg/MZhbHg7Q5Z) · [Vizzy Circle Creator Network Application form](https://docs.google.com/forms/d/e/1FAIpQLSd_ooDJ4m5hFQecHzZ2BEyo3DO0GbQ3_6-q0VvmDdoy9PI8Lw/viewform)
- Social — [Instagram @vizzy_labs](https://www.instagram.com/vizzy_labs/) · [TikTok @vizzy_labs](https://www.tiktok.com/@vizzy_labs) · [X @vizzylabs_ai](https://x.com/vizzylabs_ai) · [LinkedIn](https://www.linkedin.com/company/vizzylabs)
- Archived captures — [vizzylabs.ai, 2025-06-18](https://web.archive.org/web/20250618152802/https://www.vizzylabs.ai/) · [vizzylabs.ai, 2025-12-08](https://web.archive.org/web/20251208202228/https://www.vizzylabs.ai/) · [vizzylabs.ai, 2026-05-17](https://web.archive.org/web/20260517154252/https://www.vizzylabs.ai/) · [vispie.com, 2025-01-30](https://web.archive.org/web/20250130073405/http://www.vispie.com/)
- [Discord invite API record for the Vizzy Circle server](https://discord.com/api/v10/invites/MZhbHg7Q5Z?with_counts=true)

**Third-party coverage and profiles**

- [Luma — StartX Founder Spotlight session featuring Vizzy Labs](https://luma.com/jfwqqbcv)
- [The Org — Vizzy Labs](https://theorg.com/org/vizzy-labs) · [The Org — Yohan Lee](https://theorg.com/org/vizzy-labs/org-chart/yohan-lee) · [LinkedIn — Yohan Lee (HTTP 999 to automated access on 2026-08-14)](https://www.linkedin.com/in/yohanlee12/)
- [CB Insights — Vizzy Labs](https://www.cbinsights.com/company/vizzy-labs) · [Crunchbase — Vizzy Labs (HTTP 403 to automated access on 2026-08-14)](https://www.crunchbase.com/organization/vizzylabs-ai)
- [StartX community directory](https://web.startx.com/community?6a151520_page=3) — Vizzy Labs was not found in the pages reviewed
- Name-collision references, not this company — [UNLEASH — UK recruitment startup Vizzy raises £3.65M, 2025](https://www.unleash.ai/talent-acquisition/cv-disrupter-startup-vizzy-raises-3-65-million-seed-funding/) · [Crunchbase — Vizzy seed round, 2025-04-17 (HTTP 403 to automated access on 2026-08-14)](https://www.crunchbase.com/funding_round/vizzy-6454-seed--2028b984)
