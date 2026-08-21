# KusArt

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-21.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

KusArt is a consumer AI anime-art generator — text-to-image original-character ("OC") creation, style presets, inpainting, upscaling, LoRA training and video generation — operated by `KAZAMA INC.`, a Delaware company at 2810 North Church Street, PMB 747006, Wilmington, DE 19802 ([Terms of Service](https://kusart.com/terms); Last updated April 2026). The product launched under a different brand: it ran as **KusaPics** on `kusa.pics` from at least May 2025, and `kusa.pics` now redirects to `kusart.com` ([Wayback capture, 2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/); redirect observed 2026-08-21) — see `Identity and legal entities`.

- The company's own archived corporate site states a pre-seed round: "Kamaza.Inc Raises $400K in Pre-Seed Funding Round … with iSeed Ventures as our lead investor", announced 2025-05-12 ([archived kazama.inc, captured 2026-02-17](https://web.archive.org/web/20260217050446/https://kazama.inc/)). That site is now a dead Vercel deployment (HTTP 404 on 2026-08-21).
- The same archived page is the only source naming the team: "Neko (Caiwei Lu) - Founder & CEO", "LAX (Zhuozhi Li) - Technical Lead", "Roxy (Yuan Zhang) - Growth Lead", plus an R&D and market team with US and Japan backgrounds — see `Founder`.
- Publicly observable scale is mixed: the style picker on the live site shows per-style usage counters, the largest reading "111.3M uses" for one style ([kusart.com](https://kusart.com/); read 2026-08-21), while Similarweb reported only 81.1K visits to `kusart.com` for July 2026 and a 61% month-on-month drop for `kusa.pics` ([Similarweb](https://www.similarweb.com/website/kusart.com/), [Similarweb](https://www.similarweb.com/website/kusa.pics/)) — the brand migration sits between those two pictures, see `Notes`.
- Money flows through a Hong Kong intermediary: "Sygnal E-commerce Limited is an authorised distributor of our products", at RM 1903, 19/F Lee Garden One, 33 Hysan Avenue, Causeway Bay ([Privacy Policy](https://kusart.com/privacy); Effective January 2025).
- Engineering is visible from the served application: a Next.js front end on Cloudflare calling a separate backend at `api.kusa.pics` under `/api/go/` paths, Firebase for auth, a documented B2B API with `X-API-Key`, credit-freeze accounting and webhooks, and PostHog plus Google Analytics, Reddit and X pixels (page resources inspected 2026-08-21).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | KusArt (page title "KusArt – Free Anime & OC AI Art Generator \| Create Original Characters Online") | [kusart.com](https://kusart.com/); accessed 2026-08-21 |
| Former brand | KusaPics, at `kusa.pics` | [Wayback capture, 2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/) |
| Operating entity | "KAZAMA INC. (hereinafter referred to as 'KusArt', 'we', 'us', or 'our')" | [Terms of Service](https://kusart.com/terms); Last updated April 2026 |
| Registered address | "KAZAMA INC.: 2810 North Church Street, PMB 747006, Wilmington, DE 19802 US" | [Terms of Service](https://kusart.com/terms) |
| Distributor | "Sygnal E-commerce Limited is an authorised distributor of our products", RM 1903, 19/F Lee Garden One, 33 Hysan Avenue, Causeway Bay, HK | [Privacy Policy](https://kusart.com/privacy); Effective January 2025 |
| Governing law | "the laws of the United States"; "To the extent a more specific jurisdiction is required … the laws of the State of Delaware" | [Terms of Service](https://kusart.com/terms) |
| Document dates | Terms of Service "Last updated: April 2026", "Effective Date: April 2026"; Privacy Policy "Effective Date: January 2025" | [Terms](https://kusart.com/terms), [Privacy Policy](https://kusart.com/privacy) |
| Age policy | "you affirm that you are at least 18 years old … The Services are not intended for children or users under the age of 18" | [Terms of Service](https://kusart.com/terms) |
| Public contacts | `support@kusart.com` (site); `admin@kazama.inc` and +1 (917) 419-6843 (archived corporate site) | [Terms](https://kusart.com/terms), [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Domains | `kusart.com` created 2010-11-12 (GoDaddy, registrant shielded by Domains By Proxy) and listed for sale on PerfectDomain as recently as 2025-07-12; `kusa.pics` created 2025-03-01 (NameSilo) and now redirects to `kusart.com` | WHOIS read 2026-08-21; [Wayback capture, 2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/) |
| Site languages | English plus `ja`, `fr`, `es`, `pt`, `de`, `ko`, `zh-CN` (eight locales, declared as `hreflang` alternates) | response headers observed 2026-08-21 |
| Social and community | Discord server "Kusart" (637 members, 49 online), Instagram `@kusart_official` (64K followers, 1,527 posts), X `@kusart_official`, YouTube `@KusArt_neko` | [Discord invite API](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true), [Instagram](https://www.instagram.com/kusart_official/); observed 2026-08-21 |
| Mobile apps | None found in the US App Store under the brand name | [iTunes search API](https://itunes.apple.com/search?term=kusart&entity=software&country=us&limit=5); checked 2026-08-21 |
| Team, headcount | Not published on the live site; named only on the archived corporate site — see `Founder` | see `Notes` |

### Identity and legal entities

| Name | Type | Period / status | Relationship as stated | Source |
|---|---|---|---|---|
| KusArt | Current public brand | Live on `kusart.com` | The product; the Terms define "KusArt" as KAZAMA INC. | [kusart.com](https://kusart.com/), [Terms](https://kusart.com/terms) |
| KusaPics | Former public brand | Live on `kusa.pics` from at least 2025-05-13 to at least 2026-02-02; the domain now redirects to `kusart.com` | Same product, described on the corporate site as "Our flagship product KusaPics" | [Wayback, 2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/), [Wayback, 2026-02-01](https://web.archive.org/web/20260201015926/https://kusa.pics/) |
| KAZAMA INC. | Legal entity named in the Terms and Privacy Policy | Current | Operator of the Services; Delaware address given | [Terms](https://kusart.com/terms) |
| Kamaza.Inc | Spelling used throughout the company's own corporate site, including its copyright line "© 2025 Kamaza.Inc" | Site archived 2025-12 to 2026-02; `kazama.inc` returned HTTP 404 ("DEPLOYMENT_NOT_FOUND") on 2026-08-21 | Presented as the company behind KusaPics, at the same Wilmington address as KAZAMA INC. | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Sygnal E-commerce Limited | Third-party entity named in the Privacy Policy | Current | "an authorised distributor of our products"; Hong Kong address | [Privacy Policy](https://kusart.com/privacy) |
| Prior `kusart.com` owner | Unrelated use of the domain | Internet Archive captures from 2007 onward; still listed for sale in July 2025 | Same domain, unrelated to the current product | [Wayback, 2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/) |

The company writes its own name two ways — "KAZAMA INC." in the legal documents and the domain `kazama.inc`, but "Kamaza.Inc" in the corporate site's headings, body text and copyright line. No corporate registry filing for either spelling was retrieved — see `Notes`.

---

## Product

KusArt describes itself as "an AI anime image generator. Powered by exclusive, ultra-aesthetic anime models" ([kusart.com](https://kusart.com/); accessed 2026-08-21). The archived corporate site adds that the product is "Built on diffusion models (DMs) and enhanced with proprietary modules" ([archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/)).

### Surfaces and feature areas

| Area | What it is | Source |
|---|---|---|
| Image generation | Text-to-image with tag controls and an auto-complete/tag-suggestion system; per-model routes for `kusa-anima`, `kusa-easy`, `kusa-mix` (image-to-image, reference-guided) and `kusa-niji` | [sitemap](https://kusart.com/en/sitemap.xml), [Anima model page](https://kusart.com/image-generator/kusa-anima) |
| OC creation | "OC Maker", OC editing, character sheet generator, character consistency across poses and scenes | [kusart.com](https://kusart.com/), [sitemap](https://kusart.com/en/sitemap.xml) |
| Editing tools | AI inpainting, image upscaler, prompt extraction from uploaded images ("image to prompt"), prompt optimisation; outpainting, style transfer and sketch colourising listed as "coming soon" | [kusart.com](https://kusart.com/) |
| Model training | "Train LoRA Models with Anima" — custom anime LoRA from user images, with dataset review and controlled settings | [train-lora](https://kusart.com/train-lora) |
| Video | Image-to-video and a video generator marked "New" in the app navigation | [sitemap](https://kusart.com/en/sitemap.xml), app navigation observed 2026-08-21 |
| Third-party models exposed | Pages for "Nano Banana" (anime meme templates), `gpt-image-2`, and a "Seedance 2.0" video contest | [nano-banana](https://kusart.com/nano-banana), [sitemap](https://kusart.com/en/sitemap.xml), [Seedance 2.0 contest](https://kusart.com/events/seedance-2) |
| Style library | A one-click style picker with per-style usage counters and categories (Cel Shading, Furry, General Anime, Kawaii, Thick Coating, MEME, Specialized Anime, Male Only, 3D Models) | [kusart.com](https://kusart.com/); read 2026-08-21 |
| "Play" mini-tools | Roughly 30 SEO-oriented generators — chibi sticker maker, face swap, outfit/pose/hairstyle changer, poster and album-cover makers, manga generator, meme remaker, wallpaper generator and others | [sitemap](https://kusart.com/en/sitemap.xml) |
| Community | Meme and style libraries, showcase galleries, a Kusa-Agent chat assistant in the app shell, and a Discord server | [kusart.com](https://kusart.com/), [Discord](https://discord.gg/XwxZaKSUzz) |
| B2B API | "B2B API console" documenting `X-API-Key` auth, task-create endpoints, credit freezing, polling and webhook callbacks | [api-for-business](https://kusart.com/api-for-business) |

### Commercialization

Pricing pages are not public: the header "Pricing" link points at `#pricing`, an anchor that does not exist on the page, `/pricing` returns HTTP 404, and `/credits` redirects away for logged-out visitors (checked 2026-08-21). The structure below is what the Terms describe.

| Item | Detail | Source |
|---|---|---|
| Free tier | "a limited number of daily credits for personal, non-commercial use. Images generated under this tier may include a watermark" | [Terms of Service](https://kusart.com/terms) |
| Subscriptions | Recurring monthly or annual plans providing a monthly credit allowance plus "watermark-free image generation, enhanced privacy controls, increased usage limits, and eligibility for commercial use rights where available" | [Terms of Service](https://kusart.com/terms) |
| "Unlimited Generation" scope | Applies "only to Kusa-XL and Kusa-Easy image generation"; other models, video, editing tools and multi-image generation still consume credits | [Terms of Service](https://kusart.com/terms) |
| Credit packs | One-time purchase; "Credits purchased via Credit Packs do not expire unless otherwise stated"; credits "have no cash value, are not legal tender, and may not be transferred, resold, exchanged, or redeemed for money" | [Terms of Service](https://kusart.com/terms) |
| Refunds | "generally non-refundable, except where required by applicable law"; cancellation takes effect at the end of the billing period; refund requests reviewed case by case | [Terms of Service](https://kusart.com/terms) |
| Payment restrictions | Paid features may not be used for "Adult content, pornographic services, escort services, or sexually explicit paid content", illegal or regulated goods, gambling, or transactions involving sanctioned regions | [Terms of Service](https://kusart.com/terms) |
| Commercial-use licence | Commercial rights apply "only to outputs generated in compliance with these Terms"; an "Officially authorized OC" programme states that "Individual users earning less than US$1 million annually do not need to sign a separate license agreement" | [Terms of Service](https://kusart.com/terms), [kusart.com](https://kusart.com/) homepage payload read 2026-08-21 |
| Privacy Mode | Subscriber-only prompt and image privacy; non-subscribers' content "may be eligible for display in community galleries, public feeds, promotional areas, or product examples, and prompts may be visible to other users" | [Terms of Service](https://kusart.com/terms) |
| Referral and invite | `/referral` and `/invite` routes exist in the sitemap | [sitemap](https://kusart.com/en/sitemap.xml) |

### Reported scale over time

| Date | Figure or event | Source |
|---|---|---|
| 2025-03-01 | `kusa.pics` domain registered | WHOIS read 2026-08-21 |
| 2025-05-11 (approx.) | Discord guild "Kusart" created, per its snowflake id | [Discord invite API](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true) |
| 2025-05-12 | Pre-seed round of US$400,000 announced, lead investor iSeed Ventures | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| 2025-05-13 | Earliest archived capture of the product, as "KusaPics – Free Anime & OC AI Art Generator" | [Wayback](https://web.archive.org/web/20250513203441/https://kusa.pics/) |
| 2025-07-12 | `kusart.com` still listed for sale on PerfectDomain | [Wayback](https://web.archive.org/web/20250712131124/https://kusart.com/) |
| 2026-02-02 | Last archived capture of `kusa.pics` still branded KusaPics | [Wayback](https://web.archive.org/web/20260201015926/https://kusa.pics/) |
| 2026-05-07 to 2026-06-20 | "KusArt × Seedance 2.0 Video Contest" submissions window | [events/seedance-2](https://kusart.com/events/seedance-2) |
| Undated (live) | "Anima AI Creative Contest — 3M credits + $10,000 prize pool" | [kusart.com](https://kusart.com/) homepage payload read 2026-08-21 |
| July 2026 reference period | Similarweb: `kusart.com` 81.1K visits, global rank #394,874, bounce rate 34.36%, 3.34 pages per visit, 2m26s average duration; top countries United States 21.23%, Japan 18.53%, Egypt 7.89%, South Korea 5.96%; direct traffic 65.02% | [Similarweb](https://www.similarweb.com/website/kusart.com/) |
| July 2026 reference period | Similarweb: `kusa.pics` visits down 61.07% month on month, 77.26% of desktop visits from referrals, split United States 50.99% / Japan 49.01% | [Similarweb](https://www.similarweb.com/website/kusa.pics/) |
| Read 2026-08-21 | Style usage counters on the live style picker: 111.3M, 4.6M, 3.1M, 3.1M, 2.9M, 1.6M, 1.4M, 1.2M uses for the largest styles | [kusart.com](https://kusart.com/) |
| Observed 2026-08-21 | Discord 637 members / 49 online; Instagram 64K followers, 1,527 posts | [Discord invite API](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true), [Instagram](https://www.instagram.com/kusart_official/) |

No user count, revenue, subscriber count or generation total is published by the company for either brand.

### Content rules as published

The Terms prohibit, among other categories: "Sexual content involving minors, age-ambiguous characters, school uniforms used in a sexual context, or characters presented as underage"; "Non-consensual intimate imagery, sexual exploitation, sexual harassment, or abusive sexual content"; and "Unauthorized use of real persons' likenesses, private images, personal data, or confidential information" ([Terms of Service](https://kusart.com/terms); Last updated April 2026). The company states it operates "internal controls, automated filtering mechanisms, keyword filters, image moderation tools, account risk signals" and conducts "continuous internal monitoring and periodic audits of our AI models and services".

On ownership, the Terms state: "You, whether a legal or physical entity, retain all rights and ownership of your Content. We do not claim ownership of your Content unless you and KusArt specifically agree otherwise in writing", while noting that "KusArt does not guarantee that any generated output is unique, non-infringing, accurate, lawful, commercially usable, or suitable for a particular purpose" and "does not verify ownership of all user-submitted content".

---

## Founder

No team page exists on `kusart.com`. The only source naming individuals is the company's own corporate site at `kazama.inc`, archived 2026-02-17 and returning HTTP 404 on 2026-08-21 ([archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/)). It states: "Kamaza is built by an international team with expertise in product thinking, AI capabilities, and cultural understanding".

| Person | Role and stated background | Source |
|---|---|---|
| Neko (Caiwei Lu) | "Founder & CEO"; "Brings 2 years of full-time entrepreneurial experience in anime community building and AI overseas expansion"; "60,000-follower illustrator on Bilibili"; "Well-connected in the global venture community" | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| LAX (Zhuozhi Li) | "Technical Lead"; "Wuhan University graduate"; "Currently developing advanced art style recommendation systems, unlimited art style models, character consistency features, and planning future Omni architecture models" | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Roxy (Yuan Zhang) | "Growth Lead"; "Shandong University graduate"; "Expert in global market promotion and localization" | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| R&D and market team | "members with backgrounds from the US and Japan, with graduates from top universities including UCI, USC, and University of Pennsylvania" | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |

None of these names appears on the live product site, no headcount is given, and no third-party source reviewed corroborates the roles — see `Notes`.

---

## Funding

One round is claimed, by the company itself on its now-offline corporate site.

| Date | Round | Amount | Investors | Source |
|---|---|---|---|---|
| Announced 2025-05-12 | "Pre-Seed Round" | US$400,000 ("$400K Total Funding Amount", "1 Funding Round") | "iSeed Ventures as our lead investor" | [archived kazama.inc, captured 2026-02-17](https://web.archive.org/web/20260217050446/https://kazama.inc/) |

The page states the purpose as: "This Pre-Seed investment will accelerate our AI technology development, expand our product offerings, and strengthen our position in the anime and creative AI community." A search-result summary additionally names Llama Ventures as a participant; that name does not appear in the archived company page and was not confirmed. No investor announcement, filing or press release corroborating the round was found, and no later round is claimed anywhere — see `Notes`.

---

## Engineering

### Technology stack and platforms

No stack page is published. Items below were confirmed from the served application and its network requests on 2026-08-21.

- **Front end:** Next.js (`x-powered-by: Next.js`, `_next/static` assets, App Router locale segments and `x-middleware-rewrite: /en`), served through Cloudflare (`server: cloudflare`, `cf-ray`, Cloudflare Insights); eight locales are declared via `hreflang` alternates.
- **Backend on a separate domain:** the app calls `api.kusa.pics` — observed endpoints include `/api/go/categories/list` and `/api/go/styles/list_for_user`; static assets also load from `cdn.kusa.pics` and a CloudFront distribution (`dz2b1yn8y4hm.cloudfront.net`). The retained `kusa.pics` domain therefore still serves the API and CDN after the brand moved to `kusart.com`.
- **Authentication:** Firebase — the page fetches `firebase.googleapis.com/v1alpha/projects/-/apps/1:751503584748:web:…/webConfig` — together with Google Identity Services (`accounts.google.com`). The B2B API documentation refers to "Firebase web tokens" for ordinary web routes.
- **Analytics and marketing:** PostHog (`us.i.posthog.com`, `us-assets.i.posthog.com`), Google Analytics (`G-HC6FZE38L4`) and Google Tag Manager, plus Reddit (`alb.reddit.com`, `pixel-config.reddit.com`) and X/Twitter (`static.ads-twitter.com`, `analytics.twitter.com`) advertising pixels.
- **Payments:** processed through third parties, with Sygnal E-commerce Limited named as authorised distributor; the Terms reference "payment processors, card networks, financial partners" but name none ([Privacy Policy](https://kusart.com/privacy), [Terms](https://kusart.com/terms)).
- **Models:** the product exposes its own named models — Kusa-XL, Kusa-Easy, Kusa-Anima, Kusa-Mix, Kusa-Niji — alongside pages for third-party models (Nano Banana, `gpt-image-2`, Seedance 2.0). The underlying architecture is described only as "diffusion models (DMs) and enhanced with proprietary modules" ([archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/)).
- **No public code:** no GitHub organisation or package registry presence under the brand was found (checked 2026-08-21).

### Systems

| System | What it does | Source |
|---|---|---|
| Generation task pipeline | B2B tasks follow create → authenticate → freeze credits → execute → poll `/tasks/get` or `/tasks/get_result` → webhook callback; "The selected worker calls internal or external generation capability and stores task output" | [B2B API console](https://kusart.com/api-for-business) |
| API authentication and billing | "All B2B routes use the X-API-Key header"; "Legacy keys with billing_account_id use that dedicated credit account. New user-scoped keys freeze from the user credit pool"; insufficient balance returns code `42002` | [B2B API console](https://kusart.com/api-for-business) |
| Credit ledger | Free daily credits, subscription allowances, non-expiring credit packs, capacity top-ups, and credit freezing before execution | [Terms](https://kusart.com/terms), [B2B API console](https://kusart.com/api-for-business) |
| Style catalogue and recommendation | Numbered style presets with usage counters and categories, served from `api.kusa.pics`; the archived team page describes "advanced art style recommendation systems, unlimited art style models, character consistency features" as in development | [kusart.com](https://kusart.com/), [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| LoRA training | User-supplied dataset upload, dataset review and controlled training settings against the Anima model | [train-lora](https://kusart.com/train-lora) |
| Moderation | "automated filtering mechanisms, keyword filters, image moderation tools, account risk signals", applied to prompts, uploads, reference images and outputs | [Terms](https://kusart.com/terms) |
| Community and sharing | Public galleries and feeds for non-subscriber content, meme and style libraries, and a Privacy Mode gate for subscribers | [Terms](https://kusart.com/terms), [kusart.com](https://kusart.com/) |

### Data handling as documented

The Privacy Policy is short. It says the company collects account information, generated content ("We store content generated by users, such as images created through our AI models"), usage data including IP address, and cookie data; that it does "not sell your personal data"; and that it shares data with service providers and payment processors, to whom it passes "payment amount, currency, and transaction ID" ([Privacy Policy](https://kusart.com/privacy); Effective January 2025).

The Terms add that non-subscriber content and prompts may be surfaced publicly by default, that users grant "a non-exclusive, worldwide, royalty-free license to display, host, reproduce, and distribute your shared content within the community areas of our platform and related promotional surfaces" when using sharing features, and that the Services may rely on "AI infrastructure providers" without naming any ([Terms of Service](https://kusart.com/terms)). No retention period, subprocessor list, GDPR/CCPA rights section, or statement about whether user content trains the company's models was found in either document — see `Notes`.

### Technical background sought

No careers page, job posting or hiring channel exists on `kusart.com` (paths probed 2026-08-21). The only role descriptions found are the three team entries on the archived corporate site, which describe work on style recommendation, "unlimited art style models", character consistency and planned "Omni architecture models" ([archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/)).

### Industry domain

The work spans diffusion-model image generation and fine-tuning (LoRA training, style presets, character consistency), anime fandom conventions such as Booru tagging, consumer subscription and credit billing through an offshore distributor, multi-locale SEO across eight languages and roughly 160 indexed pages, and content moderation for user-generated character art — including the age-representation rules and likeness restrictions written into the Terms ([sitemap](https://kusart.com/en/sitemap.xml), [Terms](https://kusart.com/terms), [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Careers page | None found on `kusart.com` | paths probed 2026-08-21 |
| Stated team composition | "an international team", with R&D and market members "with backgrounds from the US and Japan" | [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Offices | Only a Wilmington, Delaware mailing address (PMB) is published; no operating office is named | [Terms](https://kusart.com/terms), [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/) |
| Headcount, salary, remote policy, benefits, hiring process | Not published | see `Notes` |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-08-21): `kusart.com` homepage, `/terms`, `/privacy`, `/contact`, `/faq`, `/blog`, `/credits`, `/api-for-business`, `/train-lora`, `/nano-banana`, `/image-generator/*`, `/events/*`, `robots.txt`, `sitemap.xml` and the English locale sitemap (159 URLs); probes of `/pricing`, `/about`, `/company`, `/legal` and `/companyprofile`; the page's network requests, script hosts and Firebase configuration; WHOIS for `kusart.com` and `kusa.pics`; Internet Archive CDX indexes and dated captures for `kusart.com`, `kusa.pics` and `kazama.inc`; `api.kusa.pics`; the Discord invite API, Instagram, X and YouTube accounts; the Apple App Store; Similarweb for both domains; Crunchbase; and English and Chinese searches on KusArt, KusaPics, KAZAMA INC., Kamaza Inc. and the named team members.

- **Pricing.** No public price list exists: the header "Pricing" link targets a `#pricing` anchor that is absent from the page, `/pricing` returns HTTP 404, and `/credits` redirects logged-out visitors away. Only the credit/subscription *structure* is documented, in the Terms.
- **Any user, subscriber, revenue or generation total.** The company publishes none for either brand; the only quantities on the site are per-style usage counters.
- **Corporate registration.** No filing was retrieved for "KAZAMA INC." or "Kamaza Inc."; the Delaware address given is a PMB mailbox, not an operating office.
- **Which entity collects payment, and through what processor.** Sygnal E-commerce Limited is named as "authorised distributor" without explanation of the arrangement, and no payment processor is named in either policy.
- **Whether user content is used to train models.** Neither the Terms nor the Privacy Policy states a position, and no opt-out is described.
- **Data retention, subprocessors and statutory rights.** The Privacy Policy states no retention period, names no subprocessor, and contains no GDPR or CCPA rights section.
- **The models behind the product.** Only marketing names (Kusa-XL, Kusa-Easy, Kusa-Anima, Kusa-Mix, Kusa-Niji) and a generic "diffusion models … enhanced with proprietary modules" description; no base model, provider, hosting region or compute partner is named, including for the third-party models the site exposes.
- **Team size and current staffing.** The three named roles come from a corporate site that is now offline; the live product site names nobody.
- **Funding beyond the claimed pre-seed.** No later round is claimed and no investor announcement was found; iSeed Ventures' participation was not confirmed from the investor's side.
- **Sources that could not be read on 2026-08-21:** `kazama.inc` (HTTP 404, read via the Internet Archive instead), `kusart.com/credits` and `/manage-subscription` (login-gated), and Crunchbase (subscription-gated).

### Inconsistencies across sources

- **The company spells its own name two ways.** The Terms and Privacy Policy say "KAZAMA INC." and the domain is `kazama.inc`, while the corporate site's headings, body copy and copyright line all read "Kamaza.Inc" ([Terms](https://kusart.com/terms), [archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/)).
- **Brand versus documents.** The live site is KusArt, but the archived corporate site describes "Our flagship product KusaPics", and the API and CDN still run on `kusa.pics` — three names in simultaneous use as of 2026-08-21.
- **Policy dates predate the brand.** The Privacy Policy is "Effective January 2025", before the `kusa.pics` domain was registered on 2025-03-01 and before the earliest archived capture of the product.
- **Scale signals disagree by orders of magnitude.** One style's counter reads "111.3M uses" on the live site, while Similarweb reported 81.1K visits to `kusart.com` for July 2026 ([kusart.com](https://kusart.com/), [Similarweb](https://www.similarweb.com/website/kusart.com/)). The counters are cumulative and brand-migration traffic still sits partly on `kusa.pics`, but no source reconciles the two.
- **Investors.** The company's own page names only iSeed Ventures as lead; a search-result summary adds Llama Ventures, which appears nowhere in the archived page and was not confirmed.
- **NSFW positioning.** The Terms bar paid features from being used for "Adult content, pornographic services … or sexually explicit paid content" and prohibit sexualised depictions of age-ambiguous characters, while the product's public style categories and marketing lean on "waifu/husbando" character generation; no page states where the moderation line sits in practice.

### Other

- **A brand migration onto a bought domain.** `kusart.com` was still advertised for sale on PerfectDomain in July 2025, roughly two months after the product launched as KusaPics on `kusa.pics`; by August 2026 it serves the product and `kusa.pics` redirects to it, while continuing to host the API and CDN ([Wayback, 2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/); observations 2026-08-21).
- **The public surface is SEO-heavy.** The English sitemap alone lists 159 URLs, of which roughly 30 are single-purpose "Play" generators and a large block are meme-library and style pages, replicated across eight locales ([sitemap](https://kusart.com/en/sitemap.xml)).
- **The corporate site went offline while the product kept shipping.** `kazama.inc` was live as recently as its 2026-02-17 capture and now returns a Vercel "DEPLOYMENT_NOT_FOUND" error, taking with it the only public statements of funding and team ([archived kazama.inc](https://web.archive.org/web/20260217050446/https://kazama.inc/); checked 2026-08-21).
- **A documented B2B API sits behind a product with no public pricing.** The `/api-for-business` console publishes auth headers, response envelopes, error codes, credit-freeze behaviour and webhook flow, while the consumer plans themselves are not listed anywhere public ([B2B API console](https://kusart.com/api-for-business)).
- **Contests are a visible acquisition channel:** a Seedance 2.0 video contest ran 2026-05-07 to 2026-06-20, and an "Anima AI Creative Contest" advertises "3M credits + $10,000 prize pool" ([events/seedance-2](https://kusart.com/events/seedance-2), [kusart.com](https://kusart.com/)).
- **Audience is concentrated off-site.** Instagram carries 64K followers against a Discord of 637 members and modest measured web traffic, suggesting the brand's reach sits mainly on social platforms rather than on the site itself (figures observed 2026-08-21).

---

## Resources

**Official**

- [kusart.com](https://kusart.com/) · [FAQ](https://kusart.com/faq) · [Blog](https://kusart.com/blog) · [Contact](https://kusart.com/contact)
- [Terms of Service](https://kusart.com/terms) (Last updated April 2026) · [Privacy Policy](https://kusart.com/privacy) (Effective January 2025)
- [B2B API console](https://kusart.com/api-for-business) · [LoRA training](https://kusart.com/train-lora) · [Anima model page](https://kusart.com/image-generator/kusa-anima) · [Nano Banana](https://kusart.com/nano-banana) · [Seedance 2.0 contest](https://kusart.com/events/seedance-2)
- [robots.txt](https://kusart.com/robots.txt) · [sitemap index](https://kusart.com/sitemap.xml) · [English sitemap](https://kusart.com/en/sitemap.xml)
- Social — [Instagram @kusart_official](https://www.instagram.com/kusart_official/) · [X @kusart_official](https://x.com/kusart_official) · [YouTube @KusArt_neko](https://www.youtube.com/@KusArt_neko) · [Discord](https://discord.gg/XwxZaKSUzz) · [Discord invite API record](https://discord.com/api/v10/invites/XwxZaKSUzz?with_counts=true)
- Archived corporate site — [kazama.inc, captured 2026-02-17](https://web.archive.org/web/20260217050446/https://kazama.inc/) (live URL returns HTTP 404 as of 2026-08-21)
- Archived former brand — [kusa.pics as KusaPics, 2025-05-13](https://web.archive.org/web/20250513203441/https://kusa.pics/) · [kusa.pics, 2026-02-01](https://web.archive.org/web/20260201015926/https://kusa.pics/) · [kusart.com listed for sale, 2025-07-12](https://web.archive.org/web/20250712131124/https://kusart.com/)

**Third-party profiles**

- [Similarweb — kusart.com](https://www.similarweb.com/website/kusart.com/) · [Similarweb — kusa.pics](https://www.similarweb.com/website/kusa.pics/)
- [Crunchbase — Kazama (subscription-gated)](https://www.crunchbase.com/organization/kazama)
- [Apple iTunes search API — no first-party app in the US storefront](https://itunes.apple.com/search?term=kusart&entity=software&country=us&limit=5)
