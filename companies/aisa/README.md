# AIsa

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

AIsa is a San Francisco company founded in 2025 ([2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)). It operates a gateway that lets AI agents and developers reach LLMs, data APIs, SaaS tools and packaged "Skills" through one API key and one billing account, with usage-based charging and settlement in fiat or stablecoins. Two different legal names appear in its own legal pages: `AIPay Inc.` in the terms and `AIPAY GLOBAL PTE. LTD` in the privacy policy, both marked "dba AIsa".

- More than 50,000 registered agents onboarded without paid marketing; from February to June 2026 registered agent users grew 150x and API calls and transactions grew 200x ([2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)). The homepage separately says "Join 5,000+ Agents Already Running" ([homepage](https://aisa.one/); Undated; accessed 2026-07-29) — see `Notes`.
- US$6.5M in total funding to date, including a seed round co-led by Alibaba and Tribe Capital, announced [2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network). Two earlier pre-seed announcements of undisclosed size were published on [2025-08-31](https://www.chaincatcher.com/article/2202064) and [2025-10-28](https://www.chaincatcher.com/article/2215658), with overlapping but not identical investor lists — see `Notes`.
- Team size is given as 10 people ([Forbes, 2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)); the LinkedIn company page shows a 2–10 employee band ([LinkedIn](https://www.linkedin.com/company/aipayhq); Undated; accessed 2026-07-29).
- Engineering evidence is drawn from the observable product surface rather than a published stack: a Next.js site behind Cloudflare, Mintlify docs on Vercel, an OpenAI-compatible inference endpoint at `api.aisa.one/v1`, a bearer data-API surface at `/apis/v1`, an x402 pay-per-call mirror at `/apis/v2`, and open-source agent Skills in Python and Node published under [github.com/AISA-skills](https://github.com/AISA-skills). The site has no careers page; the only public hiring channel found is a series of four Chinese-language recruitment posts on V2EX between [2026-05-21](https://www.v2ex.com/t/1214335) and [2026-07-28](https://www.v2ex.com/t/1230516), which are also the only public source for the roles, required stack and working conditions.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | AIsa | [homepage](https://aisa.one/); Undated; accessed 2026-07-29 |
| Legal name (terms) | AIPay Inc. (dba. "AIsa") | [Terms of Service](https://aisa.one/TOS); Last update 2026-03-10 |
| Legal name (privacy policy) | AIPAY GLOBAL PTE. LTD (dba "AIsa") | [Privacy Policy](https://aisa.one/privacy); Last update 2026-03-10 |
| Founded | 2025 | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| HQ | San Francisco | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| Additional location listed | Singapore | [LinkedIn](https://www.linkedin.com/company/aipayhq); Undated; accessed 2026-07-29 |
| Representative | Jordan Liu, Founder and CEO | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| Headcount | "a 10-person team" | [Forbes, 2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/) |
| Headcount band | 2–10 employees | [LinkedIn](https://www.linkedin.com/company/aipayhq); Undated; accessed 2026-07-29 |
| Registered agents | 50,000+ onboarded without paid marketing | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| Named customer | Impossible Finance | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| Total raised | US$6.5M in total funding to date | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| Investors named by the company | Alibaba, Tribe Capital, Draper Associates, Sumitomo Corporation, Saison Capital and other investors | [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| GitHub organisation | `AISA-skills`, created 2026-05-22, location "United States of America", 7 public repositories | [GitHub](https://github.com/AISA-skills); accessed 2026-07-29 |
| Public contacts | developer@aisa.one (developer), press@aisa.one (media), partner@aisa.one (partnerships), support@aisa.one (plugin manifest) | [homepage](https://aisa.one/), [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network), [ai-plugin.json](https://aisa.one/.well-known/ai-plugin.json) |
| Community channel | Discord | [homepage](https://aisa.one/); Undated; accessed 2026-07-29 |
| Site languages | 13 locales: English, zh-CN, zh-TW, ja-JP, ko, pt-BR, fr, de, it, es, tr, ru, ar | [sitemap.xml](https://aisa.one/sitemap.xml); accessed 2026-07-29 |

**Programs, hackathons and awards**: AIsa says it was the official technology partner of the Circle- and Arc-associated "Agentic Economy on Arc" hackathon held 2026-04-20 to 2026-04-26 ([blog, 2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc)), and reports taking second place at that event ([blog, 2026-02-26](https://aisa.one/blog/aisa-awarded-second-place-agentic-commerce-arc-hackathon)). It sponsored "Claws Out" at ETHDenver 2026 ([blog, 2026-02-27](https://aisa.one/blog/aisa-sponsors-claws-out-ethdenver-2026)) and, earlier, the Solana x402 Virtual Hackathon, where it funded a "Best AgentPay Demo" track worth $5,000 in AI resources ([ChainCatcher, 2025-11-07](https://www.chaincatcher.com/en/article/2218188)).

**Market context as stated by the company**: the [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) frames the problem as digital resources being "designed for human users, requiring account creation, API key management, subscription plans, contracts and manual payment workflows that autonomous agents cannot efficiently navigate", and attributes its own growth to the rise of agent frameworks it names as OpenClaw and Hermes.

### Identity and legal entities

| Name | Type | Jurisdiction indicated | Relationship | Source |
|---|---|---|---|---|
| AIsa | Public brand / trading name | — | Name used across the site, docs, press and GitHub | [homepage](https://aisa.one/) |
| AIPay Inc. | Legal entity named as contracting party | Not stated; "Inc." and the arbitration/class-action clause indicate a US entity | Stated as doing business as "AIsa" | [Terms of Service](https://aisa.one/TOS) |
| AIPAY GLOBAL PTE. LTD | Legal entity named as data controller | "PTE. LTD" is a Singapore private-company suffix; the page does not state a jurisdiction | Stated as doing business as "AIsa" | [Privacy Policy](https://aisa.one/privacy) |
| AIPay, Inc. | Legal name used by an investor | United States (page lists San Francisco) | Draper Associates' portfolio page writes the company as "AIsa (AIPay, Inc.)" | [Draper Associates](https://www.draper.vc/portfolio/alsa) |

The relationship between `AIPay Inc.` and `AIPAY GLOBAL PTE. LTD` is not stated on any reviewed page. The LinkedIn company URL slug is `aipayhq` and lists both San Francisco and Singapore ([LinkedIn](https://www.linkedin.com/company/aipayhq); Undated; accessed 2026-07-29). No corporate-registry record for either name was located in the reviewed public sources as of 2026-07-29; the Singapore registry aggregators checked returned bot-protection interstitials rather than results.

---

## Product

AIsa describes itself as "the unified resource and transaction network for AI agents" and, in its machine-readable product index, as "a capability and transaction layer across resources that can still have different endpoints, schemas, authorization requirements, and billing units" ([llms.txt](https://aisa.one/llms.txt); accessed 2026-07-29).

### Surfaces

| Surface | Status shown | What it is | Source |
|---|---|---|---|
| Model Gateway | Live | OpenAI-compatible inference across model families including GPT, Claude, Gemini, Grok, DeepSeek, Qwen, Kimi, MiniMax, GLM, Seed, Seedream and Wan | [models catalog](https://aisa.one/models), [docs index](https://aisa.one/docs/llms.txt) |
| APIs | Live | Per-call data and action endpoints grouped by provider | [API index](https://aisa.one/api) |
| Skills | Live | Task-oriented instruction bundles installable into agent runtimes | [skills index](https://aisa.one/skills) |
| Machine-to-Machine | Private Beta | Circle Nanopayments and the Machine Payments Protocol (MPP) over HTTP 402-style flows | [homepage](https://aisa.one/); Undated; accessed 2026-07-29 |
| Foundry | Coming Soon | Cloud-hosted pre-configured agent instances with monitoring, guardrails and nanopayment billing | [homepage](https://aisa.one/); Undated; accessed 2026-07-29 |
| Agent Discovery | Live | Published A2A agent card, AI-plugin manifest, MCP manifest, OpenAPI spec and llms.txt files | [agent-discovery](https://aisa.one/agent-discovery) |

### Catalog size

The homepage headline is "1000+ APIs, Skills, and LLMs" ([homepage](https://aisa.one/); Undated; accessed 2026-07-29). Counting the published sitemap on 2026-07-29 gives 102 model pages, 90 API pages and 48 skill pages ([sitemap.xml](https://aisa.one/sitemap.xml)); the larger figure appears to count individual endpoints, since the homepage lists per-provider endpoint counts such as DataForSEO 445, Apollo 54, Agent Mail 51, Twitter 32, Financial 22 and CoinGecko 21. The Agent Discovery page states that 43 capabilities are advertised through the A2A agent card — "42 installable skills plus the core AI Model Inference capability" ([agent-discovery](https://aisa.one/agent-discovery); Undated; accessed 2026-07-29).

Upstream providers named on the homepage API listing (Undated; accessed 2026-07-29): Apollo, DataForSEO, Tavily, Perplexity, CoinGecko, Polymarket, Kalshi, Twitter/X, Reddit, Instagram, Pinterest, YouTube, Scholar, Agent Mail, WaveInflu, and a "Financial" group.

### Commercialization

Billing is usage-based with no fixed monthly platform fee ([pricing docs](https://aisa.one/docs/guides/pricing); accessed 2026-07-29). Two models apply: token-based billing for LLM inference (priced per 1M input and output tokens, billed separately) and a fixed per-request charge for non-LLM APIs. Accounts are funded through a wallet.

| Item | Detail | Source |
|---|---|---|
| Top-up methods | Card via Stripe, or stablecoin through AIsa's own crypto payment flow | [wallet docs](https://aisa.one/docs/guides/pricing/wallet) |
| Volume discounts | $50 → 5%, $100 → 5%, $200 → 10%, $500 → 15%, $1000 → 20% | [wallet docs](https://aisa.one/docs/guides/pricing/wallet) |
| Signup credit | $2 on new accounts (Free tier) | [rate-limit docs](https://aisa.one/docs/api-reference/rate-limits) |
| Rate-limit tiers | Free 60 RPM / 60,000 TPM / 5 concurrent; Starter 600 / 600,000 / 20; Growth 3,000 / 3,000,000 / 50; Enterprise custom | [rate-limit docs](https://aisa.one/docs/api-reference/rate-limits) |
| Tier progression | Free → Starter is automatic on first wallet top-up; Growth requires $500+ topped up or an approved application | [rate-limit docs](https://aisa.one/docs/api-reference/rate-limits) |
| Pay-per-call without an account | `/apis/v2` mirrors the data APIs for x402 settlement — "No registration — call any endpoint, receive an HTTP 402 challenge, settle with a stablecoin micropayment" | [mcp.json](https://aisa.one/.well-known/mcp.json) |

A per-request price band of "$0.00044 to $0.12 per request, settled in USDC via Circle Nanopayments" is given for the Arc hackathon integration ([blog, 2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc)). No comprehensive public price list per endpoint was found outside the console and the marketplace pages.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2025-10-28 | AI Marketplace-402 described as aggregating "600+ LLMs, 1,000,000+ data APIs and GPU" resources, positioned as "the NASDAQ of AI resources" | [ChainCatcher (ZH)](https://www.chaincatcher.com/article/2215658) |
| 2026-04-23 | "processed over one million API calls" | [blog](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc) |
| 2026-07-03 | Registered agent users 150x and API calls/transactions 200x from February to June 2026; 50,000+ registered agents onboarded without paid marketing | [release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| 2026-07-03 | "more than 20,000 registered agents" onboarded without paid marketing | [Forbes](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/) |
| Undated; accessed 2026-07-29 | "Join 5,000+ Agents Already Running" | [homepage](https://aisa.one/) |

### Announced customers, partners and ecosystem claims

| Date | Party | What was announced |
|---|---|---|
| [2025-08-31](https://www.chaincatcher.com/article/2202064) | Circle, Visa, Stripe, PayPal, Privy, JPMorgan Kinexys | The company listed itself as an early member of Circle's Global Payment Network, an early contributor to the Visa Intelligence Commerce ecosystem, a core developer on Stripe AgentKit and Global Financial Accounts, a joint promoter of PYUSD with PayPal, an account-layer collaborator with Privy, and as exploring $JPMD treasury-agent use with JPMorgan Kinexys |
| [2025-10-28](https://www.chaincatcher.com/article/2215658) | Coinbase x402, Google AP2/A2A | AgentPayWall-402 described as deeply integrated with Coinbase x402, with native HTTP 402 / x402 / L402 support extending across Base, Lightning, Solana, BNB, Polygon and X-Layer, plus participation in Google AP2/A2A |
| [2025-11-07](https://www.chaincatcher.com/en/article/2218188) | Solana x402 Virtual Hackathon | AIsa sponsored a "Best AgentPay Demo" track worth $5,000 in AI resources |
| [2026-02-26](https://aisa.one/blog/aisa-awarded-second-place-agentic-commerce-arc-hackathon) | Circle- and Google-backed Agentic Commerce on Arc hackathon | AIsa reports being awarded second place |
| [2026-02-27](https://aisa.one/blog/aisa-sponsors-claws-out-ethdenver-2026) | ETHDenver 2026 | AIsa sponsored the "Claws Out" event |
| [2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc) | Circle / Arc | AIsa served as data-layer technology partner for the "Agentic Economy on Arc" hackathon (2026-04-20 to 2026-04-26), exposing 100+ endpoints over x402 with Circle Nanopayments |
| [2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) | Impossible Finance | Named as a customer using AIsa to access models, data and APIs through one interface |
| [2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) | x402 ecosystem | The company states that, per x402's public leaderboard, it "has ranked as the top seller and top server", and that it integrates with agent-payment initiatives from Circle, Visa and Stripe |

Agent frameworks named as supported integration targets, each with its own tutorial page: OpenClaw, Hermes Agent, Claude Code, Codex, Cursor, Manus and custom agents ([homepage](https://aisa.one/); Undated; accessed 2026-07-29).

### Stated plans

From the [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network), the new funding goes to expanding the engineering team, scaling payment infrastructure, onboarding additional model/data/API providers, and accelerating stablecoin settlement. It also states plans to "expand its resource marketplace, deepen enterprise controls including budgets, approval workflows and audit trails, and scale the infrastructure required for autonomous agents to transact securely at internet scale". Foundry is listed as "Coming Soon" and Machine-to-Machine as "Private Beta" ([homepage](https://aisa.one/); Undated; accessed 2026-07-29).

---

## Founder

**Jordan Liu** — Founder and CEO ([2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)). Forbes writes "Liu previously founded a PayPal-like digital wallet aimed at unbanked customers in Southeast Asia and a blockchain wallet" ([Forbes, 2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)).

A profile written by Qin En Looi, published [2026-05-11](https://www.linkedin.com/pulse/unfiltered-jordan-liu-founder-ceo-alsa-qin-en-looi--rytrc), adds that the Southeast Asian wallet was acquired by a public company and that the blockchain wallet he co-founded grew "from zero to eight million monthly active users across multiple chains", backed by Binance Labs and UTXO. Neither company is named in the reviewed sources; see `Notes`. The piece is published by an investor in the seed round, and states no dates, education, or AIsa founding date.

The pre-seed announcement of [2025-08-31](https://www.chaincatcher.com/article/2202064) describes the founding team by prior role without naming anyone: a serial fintech founder, a former head of Bloomberg's financial-data business, a Meta AI scientist, a Visa token-payments product lead, and a Bitcoin L2 core contributor. That release also states the team has worked in AI, payments, decentralised systems and large-scale commercialisation of recommendation systems.

Liu is titled "Founder and CEO" in the [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network), but "联合创始人兼 CEO" (co-founder and CEO) in the [2025-10-28 pre-seed announcement](https://www.chaincatcher.com/article/2215658), and Forbes also calls him a co-founder. No other co-founder is named in any reviewed source.

The [2026-05-21 recruitment post](https://www.v2ex.com/t/1214335) states that the AI Engineer role reports to the "CEO / CTO team" — the only reference to a CTO found in any source. No CTO is named anywhere.

Liu is the only named individual across AIsa's own site, press releases, blog, docs and GitHub organisation as of 2026-07-29. No team, about, or leadership page exists on the site. Forbes describes the company as having a 10-person team but does not name any other member ([Forbes, 2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)).

Longer-form appearance: [The Breakdown podcast — "The Three Layers of AI Agent Commerce with Jordan Liu"](https://open.spotify.com/episode/4lk37Fn2yiVrni6NIRvZri).

---

## Funding

| Date | Round (as named in the source) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2025-08-31 | Pre-Seed | Amount and valuation "not yet disclosed" | Institutional: Draper Associates (Tim Draper), 分布式资本 / Fenbushi Capital (Shen Bo), Sats Ventures, BoostVC (Adam Draper), WaterDrip Capital, IMPA Ventures, 10K Ventures, SosoValue, CatherVC. Angels described as including Domo (BRC-20 founder), Paul Taylor (former BlackRock digital-asset investment head), Jackie (Side Door Ventures partner), David (Inception Capital founder), Lucia (a fund founding partner with Tether as major LP), Harry (Pioneer Fund founder), Karen (former Temasek venture partner), and former Visa Crypto executives | — | [ChainCatcher (ZH)](https://www.chaincatcher.com/article/2202064) · [EN](https://www.chaincatcher.com/en/article/2202064) |
| 2025-10-28 | Pre-Seed (dateline San Francisco, 2025-10-27) | Not disclosed | Institutional: Draper Associates (Tim Draper), Fenbushi Capital US (Shen Bo), BoostVC (Adam Draper), Sats Ventures, Trampoline Ventures, IMPA Ventures, SNZ Capital, WaterDrip Capital, 10K Ventures. Angels described as including Paul Taylor, Domo, Jackie (Side Door Ventures), David (Inception Capital), Lucia (Arcanum Capital founding partner, Tether major LP), Harry (Awakening Ventures founding partner), Kari (former Temasek venture partner), James/Joey (former top-CEX executives and fund partners), former Visa Crypto executives, Jennifer (HK family office), Hunter (CatherVC co-founder) | — | [ChainCatcher (ZH)](https://www.chaincatcher.com/article/2215658) · [EN](https://www.chaincatcher.com/en/article/2215658) |
| 2026-07-03 | "a new seed round" | Round size not disclosed; US$6.5M stated as total funding to date | Co-leads Alibaba and Tribe Capital, with Draper Associates, Sumitomo Corporation, Saison Capital and other investors | US$6.5M | [AIsa](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network), [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html) |

The company's own wording is "US$6.5 million in total funding to date, including a new seed round"; it does not separate the seed amount from the pre-seed. Media coverage generally describes the whole $6.5M as the seed round — see `Notes`. Neither pre-seed announcement discloses an amount, and the two are published under the same round name eight weeks apart — see `Notes`.

The [2025-10-28 announcement](https://www.chaincatcher.com/article/2215658) carries quotes from Jordan Liu and from Maxime Bucaille, described as an investment director at Draper Associates. Draper Associates participated in both rounds and lists AIsa as a current portfolio company ([Draper Associates](https://www.draper.vc/portfolio/alsa); Undated; accessed 2026-07-29). BoostVC appears in the pre-seed investor list and on the LinkedIn page's backing line, but not in the seed release. The seed release carries quotes from Jordan Liu and from Francis Zhan, investor at Tribe Capital; the GlobeNewswire version dated [2026-07-07](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html) additionally carries a quote from Qin Jin, Investment Director of Alibaba Group, which the version on aisa.one does not.

The August pre-seed announcement names beta products **Agentic Accounts**, **AgentPayGuard** and **AgentPayWall-402**, and planned products **AIsaNet**, **AIsa Treasury** and **AIsa Marketplace** ([ChainCatcher, 2025-08-31](https://www.chaincatcher.com/article/2202064)). The October announcement instead presents four components said to be in public beta: **AI Marketplace-402**, **AgentPayWall-402**, **AIsaNet** and **AIsa Treasury** ([ChainCatcher, 2025-10-28](https://www.chaincatcher.com/article/2215658)). None of these names appears on the current site — see `Notes`.

---

## Engineering

### Technology stack and platforms

No stack page is published. The items below are confirmed by observable public assets unless labelled otherwise.

- **Web and docs hosting:** `aisa.one` responds with `x-nextjs-cache` / `x-nextjs-prerender` headers behind `server: cloudflare`, indicating Next.js served through Cloudflare; `aisa.one/docs` responds with `x-mintlify-client-version` and `x-vercel-*` headers, indicating Mintlify documentation on Vercel; `console.aisa.one` sits behind a Cloudflare challenge (response headers observed 2026-07-29).
- **API surfaces:** `https://api.aisa.one/v1` for OpenAI-compatible inference (bearer only), `https://api.aisa.one/apis/v1` for bearer-authenticated data APIs, and `https://api.aisa.one/apis/v2` mirroring the same data surface for x402 pay-per-call ([mcp.json](https://aisa.one/.well-known/mcp.json), [architecture docs](https://aisa.one/docs/evaluate/architecture)).
- **Payments:** Stripe for card top-ups, and a stablecoin flow requiring wallet connection and a spending limit ([wallet docs](https://aisa.one/docs/guides/pricing/wallet)). An unauthenticated request to `api.aisa.one/v1/models` on 2026-07-29 returned `HTTP 402` with `content-type: application/problem+json` and a `WWW-Authenticate: Payment` challenge carrying `method="tempo"`, `realm="api.aisa.one"`, `intent="charge"` and a base64 request payload whose `methodDetails` names `chainId 4217`.
- **Custom protocol headers observed** on that same response: `X-AISA-Max-Price-USD`, `X-AISA-Price-USD`, `X-AISA-Pricing-Strategy`, `X-AISA-Pricing-Version`, `X-AISA-Credit-Model`, `X-AISA-Estimated-Credits`, `X-AISA-Accounted-Credits`, `X-AISA-Request-Multiplier`, `X-AISA-Result-SHA256`, `Payment-Receipt`, `Idempotency-Key` and `X-MPP-Discovery`.
- **Skills implementation:** the public repositories are Python and Node — for example `search-research-skills` ships `SKILL.md` plus `scripts/*.mjs` for the Tavily skill and a `scripts/lib/` Python package for the `last30days` skill, with modules for Reddit, TikTok, Instagram, Pinterest, YouTube, Hacker News, Polymarket, Xiaohongshu, clustering, dedupe, reranking and rendering ([repo tree](https://github.com/AISA-skills/search-research-skills); accessed 2026-07-29). Six of the seven repositories are MIT-licensed; `saas-automation-skills` is Apache-2.0.
- **Skill packaging:** each skill is a directory with a `SKILL.md` carrying YAML front matter (`name`, `description`, `compatibility`, and an `metadata.aisa` block declaring required binaries and environment variables such as `AISA_API_KEY`). The stated compatibility target is "Agent Skills compatible clients such as OpenClaw, Claude Code, Hermes, and GitHub-backed skill catalogs" ([SKILL.md example](https://raw.githubusercontent.com/AISA-skills/search-research-skills/main/aisa-tavily/SKILL.md); accessed 2026-07-29).
- **Rate limiting:** enforced per API key across RPM, TPM (input + output combined) and concurrency, with `X-RateLimit-*` and `Retry-After` headers documented ([rate-limit docs](https://aisa.one/docs/api-reference/rate-limits)).
- **Hiring-only mentions**, from the V2EX recruitment posts and not otherwise confirmed in production: Python as the required language; Go and TypeScript as preferred; LangChain, CrewAI, AutoGen and MetaGPT named as multi-agent frameworks of which at least one is expected; RAG, vector retrieval and structured document parsing; SFT, RL and DPO post-training as a bonus; crawlers, automation scripts and the OpenAI, Anthropic and Gemini APIs for the growth role; n8n and Dify as bonus low-code workflow platforms; Claude Code, Codex and Cursor listed as AI coding tools the team uses ([2026-05-21](https://www.v2ex.com/t/1214335), [2026-05-25](https://www.v2ex.com/t/1215230), [2026-07-28](https://www.v2ex.com/t/1230516)). A requirement in a posting does not establish current production use.

### Systems

| System | What it does | Source |
|---|---|---|
| Model gateway | Routes OpenAI-compatible inference requests to upstream model providers, plus Claude-native messages, Gemini `generateContent` and image generation routes | [ai-plugin.json](https://aisa.one/.well-known/ai-plugin.json), [models catalog](https://aisa.one/models) |
| Data and action API relay | Normalizes and proxies third-party APIs (search, social, financial, prediction markets, sales intelligence, email) behind one credential | [API index](https://aisa.one/api) |
| Usage metering and billing | Records tokens, request counts and per-request cost; deducts from a wallet balance; exposes usage logs | [pricing docs](https://aisa.one/docs/guides/pricing), [wallet docs](https://aisa.one/docs/guides/pricing/wallet) |
| Machine payment layer | HTTP 402-style challenge/settle/retry flow via x402, Circle Nanopayments and the Machine Payments Protocol | [homepage](https://aisa.one/), [mcp.json](https://aisa.one/.well-known/mcp.json) |
| Machine discovery surface | `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, `/docs/llms.txt`, `/.well-known/agent-card.json` (A2A), `/.well-known/ai-plugin.json`, `/.well-known/mcp.json`, `openapi.yaml` | [agent-discovery](https://aisa.one/agent-discovery) |
| Agent Skills catalog | Instruction bundles distributed both as site pages and as GitHub repositories, installable into agent runtimes | [skills index](https://aisa.one/skills), [GitHub](https://github.com/AISA-skills) |
| Foundry | Cloud-hosted agent deployment with monitoring, guardrails and nanopayment billing — listed as Coming Soon, not observable | [homepage](https://aisa.one/); Undated; accessed 2026-07-29 |
| AIsa CIO | A hosted example agent for multi-market portfolio valuation and SEC filing analysis, built on the platform's financial, prediction-market, search and model APIs; the page states the shown transcript is a scripted replay with illustrative figures | [agent page](https://aisa.one/agents/aisa-cio); Undated; accessed 2026-07-29 |

**Discovery design.** The engineering post [The Agent-Readable Web (2026-04-23)](https://aisa.one/blog/the-agent-readable-web), attributed to "AIsa Team", describes rebuilding the discovery surface around a "five-hop test" — an agent should be able to gather everything needed to transact within five HTTP requests, chaining `robots.txt` → `llms.txt` (stated at roughly 650 lines) → `agent-card.json` → `sitemap.xml` → per-skill OpenAPI specs (stated at 24 published at the time). It argues for server-rendered documentation over client-side SPAs, semantic HTML and JSON-LD, and summarizes the position as "Agent-friendliness and human-friendliness mostly agree".

**Internal agent system as described in hiring.** The [2026-05-25 recruitment post](https://www.v2ex.com/t/1215230) states that the company is "an AI-native company internally as well — all key business processes run on a self-built multi-agent system", and that the role therefore builds both customer-facing agent infrastructure and the company's own operations. The [2026-05-21 post](https://www.v2ex.com/t/1214335) splits the work into an external product side (autonomous agents over the resource layer, cross-provider dynamic routing, external API composition, agent-native payment and authorization) and an internal system side (a multi-agent operating system covering growth, customer service, risk control and finance). The AI-engineer descriptions add a natural-language operations console with traceable execution chains and safe degradation, a skills library that consolidates execution traces into reusable skills, and an agent evaluation and regression pipeline. These are the company's own statements in a recruitment context; none of them is observable in the public product surface.

**MCP status.** The MCP manifest lists one server entry per skill at `https://mcp.aisa.one/<slug>/sse` over `http+sse`, but the manifest itself notes these are a convention rather than a standard well-known file and that entries with `status: "planned"` are "rolling out — filter on status when dialing" ([mcp.json](https://aisa.one/.well-known/mcp.json); accessed 2026-07-29). `mcp.aisa.one` did not resolve when checked on 2026-07-29.

### Data handling as documented

The [security and data privacy guide](https://aisa.one/docs/guides/security) states a no-storage policy for request content: prompts and API responses are "not stored", payloads are "processed transiently and discarded after the request completes", and data is not used for training or analytics. Limited operational metadata — timestamps, API key identifiers, rate-limit counters, error and status information — may be retained. The page also states that protocol versions and cryptographic configuration "are managed at the infrastructure level and are not exposed publicly". The [privacy policy](https://aisa.one/privacy) separately says the company collects billing information, uses third-party payment processors, does not store full card numbers, and processes data for AML and KYC compliance.

### Technical background sought

All of the following comes from the four V2EX recruitment posts, published by user `wateryfield`, which identify the company as AIsa and link `aisa.one`. Roles advertised across the series: AI Engineer, Backend / full-stack Engineer, Growth Engineer, and Developer Advocate.

**AI Engineer** ([2026-05-21](https://www.v2ex.com/t/1214335), [2026-05-25](https://www.v2ex.com/t/1215230), [2026-07-28](https://www.v2ex.com/t/1230516))

- *Required:* having built multi-agent systems in production; familiarity with at least one of LangChain, CrewAI, AutoGen or MetaGPT; understanding of RAG, tool calling, long-task orchestration, and agent failure modes and fallbacks; engineering trade-offs across cost, latency, reliability and interpretability; building training and evaluation sets from logs, human labelling and user feedback. The 2026-07-28 version adds 2+ years of AI development experience with a lead or major role in a shipped AI product, and either big-tech or startup experience, where startup experience must come with users, revenue or funding.
- *Preferred:* cluster architecture experience or having built an agent framework; having built cross-provider dynamic routing; self-hosting LLMs or post-training (SFT, RL, DPO); multimodal retrieval; payment systems, autonomous trading flows, or high-availability systems; LLM-as-judge or automated agent regression testing; participation in protocol specification discussions or open-source implementations; ongoing contribution to AI or agent open-source communities.
- *Explicitly unsuitable* ([2026-05-21](https://www.v2ex.com/t/1214335)): candidates who only do prompt engineering without going into framework internals; who want to work only on the customer product and not internal agent systems; or who need a fully specified PRD before starting.

**Backend / full-stack Engineer** ([2026-05-25](https://www.v2ex.com/t/1215230), [2026-07-28](https://www.v2ex.com/t/1230516))

- *Required:* solid backend or full-stack fundamentals; familiarity with APIs, databases, cloud infrastructure and day-to-day operations; Chinese and English communication. Experience requirement moved from "1–5 years" in May to "3–5 years" plus a 211/985 bachelor's degree or above and large-internet-company experience in July.
- *Preferred:* LLM, model API, AI gateway or inference platform experience; DevOps, deployment and cloud operations; having used Claude Code, Codex or Cursor.
- The role explicitly includes platform operations work — putting models live and updating prices — alongside API, agent-skill and plugin development.

**Growth Engineer** ([2026-05-25](https://www.v2ex.com/t/1215230))

- *Required:* having independently owned a tool, workflow or small product end to end; crawlers, API calls, automation scripts, data cleaning and analysis; familiarity with mainstream LLM APIs (OpenAI, Anthropic, Gemini) and workflow orchestration over them; ability to write Skills; demonstrated SEO results covering keywords, search intent, content structure, indexing, ranking and conversion; English as a working language, read and write.
- *Preferred:* growth-hacking projects such as bulk SEO page generation, bulk KOL outreach or bulk content distribution; n8n or Dify; consumer-facing overseas product engineering; independent-developer, overseas-tool, content-site or SEO-site experience.

**Developer Advocate** ([2026-06-24](https://www.v2ex.com/t/1222499), repeated [2026-07-28](https://www.v2ex.com/t/1230516))

- *Required:* able to write code independently and complete API integration and agent development; Python; understanding of LLM, agent and RAG concepts; strong Chinese technical writing.
- *Preferred:* TypeScript or Go; backend, SDK or developer-tool experience; LangChain or similar; open-source maintainership; a personal technical brand; Meetup or conference speaking; prior DevRel or DX experience at a DevTool/API platform; early-stage startup experience.
- The post states this is the company's first developer-relations hire and that the remit is the Chinese developer community specifically, naming GitHub, 掘金, 知乎, V2EX, WeChat technical groups and offline meetups as the target channels.

### Industry domain

The work spans agent runtimes and tool protocols (MCP, A2A, OpenAI plugin manifests, llms.txt, OpenAPI 3.1), API gateway and metering design, and machine payments: HTTP 402 / x402 challenge-and-settle flows, USDC and stablecoin settlement, Circle Nanopayments, the Machine Payments Protocol, and card processing via Stripe. The documentation also treats spend authorization as a first-class concern, distinguishing read, write and payment operations and requiring per-request, per-task and time-based limits plus audit records before enabling autonomous purchasing ([machine payments concepts](https://aisa.one/docs/concepts/machine-payments-for-agents)). The privacy policy adds AML/KYC obligations to that surface ([privacy policy](https://aisa.one/privacy)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Careers page | None on the site. `/careers`, `/jobs`, `/about`, `/team` and `/contact` all return HTTP 404; the footer's "Contact" link does not lead to a hiring page | aisa.one paths checked 2026-07-29 |
| Public hiring channel | Four Chinese-language recruitment posts on V2EX by user `wateryfield`, 2026-05-21, 2026-05-25, 2026-06-24 and 2026-07-28, in the 酷工作 and 远程工作 nodes. Applications go to an email address masked by V2EX | [2026-05-21](https://www.v2ex.com/t/1214335), [2026-05-25](https://www.v2ex.com/t/1215230), [2026-06-24](https://www.v2ex.com/t/1222499), [2026-07-28](https://www.v2ex.com/t/1230516) |
| Remote policy | "远程居家办公" — full-time remote work from home, part-time not accepted. The 2026-05-21 title listed 北京/上海/广州/深圳/杭州 and Singapore, which the poster corrected in the thread: "I wrote it wrong, it is actually remote; the team occasionally works together offline every few months, and previously rented a co-working space near Zhongguancun in Beijing" | [2026-05-25](https://www.v2ex.com/t/1215230), [2026-05-21 reply #4](https://www.v2ex.com/t/1214335) |
| Location | San Francisco headquarters; Singapore listed as an additional location on LinkedIn; a previous Beijing co-working space mentioned in the V2EX thread | [release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network), [LinkedIn](https://www.linkedin.com/company/aipayhq), [2026-05-21](https://www.v2ex.com/t/1214335) |
| Team size | 10 people (Forbes); 2–10 band (LinkedIn); described in hiring as "a small and focused company" whose members have 211/985, overseas-study and big-tech backgrounds | [Forbes](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/), [LinkedIn](https://www.linkedin.com/company/aipayhq), [2026-07-28](https://www.v2ex.com/t/1230516) |
| Stated hiring intent | Funding to be used to "expand AIsa's engineering team" | [release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) |
| Working language | Not stated as a company-wide policy. The AI Engineer and Growth Engineer postings require English for reading and writing as a working language; the backend posting requires Chinese and English, which the poster explained in-thread as "because sometimes you need to communicate in English with suppliers and customers"; the Developer Advocate role requires strong Chinese technical writing. One 2026-07-28 reply asking whether fluent English is mandatory was unanswered as of 2026-07-29 | [2026-05-25 and reply #2](https://www.v2ex.com/t/1215230), [2026-07-28](https://www.v2ex.com/t/1230516), [2026-06-24](https://www.v2ex.com/t/1222499) |
| Salary | Not published. Asked directly in three threads; the poster answered "open, negotiable" once and did not answer the other two | [2026-05-21 replies](https://www.v2ex.com/t/1214335), [2026-05-25 replies](https://www.v2ex.com/t/1215230), [2026-07-28](https://www.v2ex.com/t/1230516) |
| Equity | The 2026-05-21 AI Engineer post offers "competitive salary + founding-team-level options"; later posts state salary only | [2026-05-21](https://www.v2ex.com/t/1214335) |
| Career track and reporting | AI Engineer described as a senior individual-contributor track with no people management, reporting to the "CEO / CTO team" | [2026-05-21](https://www.v2ex.com/t/1214335) |
| Interview process | Video interview | [2026-07-28](https://www.v2ex.com/t/1230516) |
| Overtime, visa sponsorship, benefits, turnover | Not published. A question about overtime in the 2026-05-25 thread was unanswered as of 2026-07-29 | [2026-05-25 replies](https://www.v2ex.com/t/1215230) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): `aisa.one` homepage, `robots.txt`, full `sitemap.xml`, news index, blog index and all ten listed posts' metadata, product `llms.txt` and `/docs/llms.txt`, pricing/wallet/rate-limit/architecture/security/machine-payment documentation pages, Terms of Service and Privacy Policy, the `.well-known` discovery files, `api.aisa.one` response headers, and the `AISA-skills` GitHub organisation and its seven repositories; brand, legal-name and founder searches in English and Chinese; the Draper Associates portfolio page, LinkedIn company page, Dealroom profile; English-language press coverage; Chinese-language searches across 36Kr, 钛媒体, ChainCatcher, Odaily, PANews, BlockBeats, TechFlow, Foresight News and 金色财经; and the V2EX 酷工作 and 远程工作 boards including the posting user's full topic history.

- **Careers surface on the company's own properties.** The site has no careers page and no AIsa or AIPay listing was found on the English-language job boards and databases reviewed. Hiring happens on V2EX in Chinese instead — see `Engineering`. Nothing on aisa.one links to those posts.
- **Named employees other than the founder.** None. No team page, no engineering bylines — the one technical post is attributed to "AIsa Team". The V2EX posts are made by a user account, `wateryfield`, that does not state a name or role.
- **Salary bands.** Not published in any of the four V2EX postings; answered as "open, negotiable" when asked directly.
- **Revenue and transaction volume in currency terms.** Not disclosed. Growth is reported only as multiples (150x, 200x) and as an API-call count ("over one million", 2026-04-23).
- **Seed round size on its own.** The company reports only a US$6.5M cumulative total; the pre-seed amount was never disclosed.
- **Security certification.** No SOC 2, ISO/IEC 27001 or equivalent is claimed on any reviewed page. The security guide explicitly declines to publish protocol versions and cryptographic configuration.
- **Status page or published SLA.** None found; `status.aisa.one` does not resolve.
- **Corporate registry records.** No filing or register entry was located for `AIPay Inc.` or `AIPAY GLOBAL PTE. LTD` in the reviewed public sources; the Singapore registry aggregators checked returned bot-protection pages.
- **The founder's prior companies by name.** Forbes and the investor profile describe two prior ventures but name neither. A search-result snippet attributes the multi-chain wallet to UXUY; no source page supporting that attribution was retrieved, so it is recorded here as unconfirmed.
- **Dealroom profile.** Returned HTTP 403 to automated access on 2026-07-29 and was not used as a source.

### Inconsistencies across sources

- **Registered agents:** 50,000+ ([company release, 2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)) versus "more than 20,000" ([Forbes, same date](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)), both using the phrasing "without paid marketing". The homepage separately says "Join 5,000+ Agents Already Running" ([homepage](https://aisa.one/); Undated; accessed 2026-07-29), which describes running rather than registered agents; the three figures are not reconciled anywhere reviewed.
- **Legal name:** `AIPay Inc.` in the [Terms of Service](https://aisa.one/TOS) versus `AIPAY GLOBAL PTE. LTD` in the [Privacy Policy](https://aisa.one/privacy), both dated 2026-03-10 and both marked "dba AIsa".
- **Round framing:** the company says US$6.5M is "total funding to date, including a new seed round" ([release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)); Forbes, FinSMEs and CryptoRank describe a "$6.5 million seed round", which would exclude the 2025 pre-seed from the total.
- **Two pre-seed announcements under the same round name.** The [2025-08-31](https://www.chaincatcher.com/article/2202064) and [2025-10-28](https://www.chaincatcher.com/article/2215658) pieces both announce the completion of a "Pre-Seed" round with no amount. Neither references the other, and the investor lists differ: SosoValue and CatherVC appear as institutions in August but not October, where CatherVC's co-founder appears as an angel instead; Trampoline Ventures and SNZ Capital appear only in October. Whether this is one round announced twice, an extension, or two separate closings is not stated anywhere reviewed.
- **Investor names rendered differently across the two announcements:** 分布式资本 (Shen Bo) in August versus "Fenbushi Capital US (Shen Bo)" in October — the same firm; "Karen" versus "Kari" for the former Temasek venture partner; Harry described as founder of Pioneer Fund in August and founding partner of Awakening Ventures in October; Lucia's fund unnamed in August and given as Arcanum Capital in October.
- **Founder title:** "Founder and CEO" in the [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) versus "联合创始人兼 CEO" (co-founder and CEO) in the [2025-10-28 announcement](https://www.chaincatcher.com/article/2215658) and "co-founder" in [Forbes](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/). No second co-founder is ever named.
- **Funding as described in hiring versus in the release.** The [2026-05-21 V2EX post](https://www.v2ex.com/t/1214335) states "the company has completed two rounds, on the scale of tens of millions (数千万), and is about to start its Series A", with investors "covering payments and cloud computing". The [2026-07-03 release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) states US$6.5M as total funding to date and names the round a seed round, not a Series A. The V2EX figure gives no currency, and a recruitment post is a weaker source than a company release; the two are recorded here rather than reconciled.
- **Resource-catalog claims across time:** "600+ LLMs, 1,000,000+ data APIs and GPU" for AI Marketplace-402 in [October 2025](https://www.chaincatcher.com/article/2215658) versus "1000+ APIs, Skills, and LLMs" on the current [homepage](https://aisa.one/) and 102 model pages in the [sitemap](https://aisa.one/sitemap.xml). The 2025 figures describe a product name that no longer exists on the site.
- **Catalog size:** "1000+ APIs, Skills, and LLMs" on the [homepage](https://aisa.one/) versus 43 capabilities advertised in the A2A card ([agent-discovery](https://aisa.one/agent-discovery)) and 240 catalog pages in the [sitemap](https://aisa.one/sitemap.xml) (102 models, 90 APIs, 48 skills). The counts measure different units — endpoints, advertised capabilities, and catalog pages — and no page defines which.
- **Model-gateway breadth:** "50+ LLMs" in the [agent card](https://aisa.one/.well-known/agent-card.json) versus "100+ AI models" in the [ai-plugin manifest](https://aisa.one/.well-known/ai-plugin.json) and the [2026-02-19 blog post](https://aisa.one/blog/introducing-aisa-unified-gateway) title, against 102 model pages in the sitemap.
- **Investor list on LinkedIn:** the [LinkedIn page](https://www.linkedin.com/company/aipayhq) names Tribe Capital, Draper Associates and BoostVC; the [seed release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) names Alibaba, Tribe Capital, Draper Associates, Sumitomo Corporation and Saison Capital, and does not mention BoostVC, which appears only in the [pre-seed list](https://www.chaincatcher.com/en/article/2202064).
- **Alibaba quote:** present in the [GlobeNewswire release of 2026-07-07](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html), absent from the [aisa.one version dated 2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network). The two texts are otherwise substantially the same.

### Other

- **Product naming has turned over completely since the pre-seed.** The August 2025 announcement named Agentic Accounts, AgentPayGuard, AgentPayWall-402, AIsaNet, AIsa Treasury and AIsa Marketplace ([ChainCatcher, 2025-08-31](https://www.chaincatcher.com/en/article/2202064)); the October 2025 announcement named AI Marketplace-402, AgentPayWall-402, AIsaNet and AIsa Treasury ([ChainCatcher, 2025-10-28](https://www.chaincatcher.com/article/2215658)); a November 2025 sponsorship write-up still described the product as "AIsaNet (micropayment network) and AIsa Treasury (cross-currency liquidity engine)" ([ChainCatcher, 2025-11-07](https://www.chaincatcher.com/en/article/2218188)). None of those names appears on the site as of 2026-07-29, where the surfaces are Model Gateway, APIs, Skills, Machine-to-Machine and Foundry.
- **Coverage splits by language and by period.** The 2025 pre-seed announcements and hackathon sponsorship were carried in Chinese-language crypto trade media (ChainCatcher), with no English general-tech coverage found; the 2026 seed round was carried in English business and startup media (Forbes, Business Insider, Yahoo Finance, FinSMEs, CryptoRank, The AI Insider) with no Chinese-language coverage found in the reviewed sources as of 2026-07-29. Searches of 36Kr, 钛媒体, Odaily, PANews, BlockBeats, TechFlow, Foresight News and 金色财经 for the seed round returned no matching article.
- **The 2025 announcements make ecosystem claims that the current site does not repeat in the same form.** August 2025 listed Circle, Visa, Stripe, PayPal, Privy and JPMorgan Kinexys relationships ([ChainCatcher](https://www.chaincatcher.com/article/2202064)); the current [funding release](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network) narrows this to integrating "with emerging agent-payment initiatives from Circle, Visa and Stripe". PayPal, Privy and JPMorgan Kinexys are not mentioned on the site as of 2026-07-29.
- **Positioning language differs by audience.** The company's own release calls it a "resource and transaction network"; Forbes and Business Insider headline it as a payments company; the LinkedIn page name is "The Resource Marketplace for AI Apps"; the Draper Associates portfolio entry describes "a payment network for AI agents comparable to Visa" using blockchain technology ([Draper Associates](https://www.draper.vc/portfolio/alsa)).
- **The V2EX postings form a dated series and can be compared against each other.** The backend role's experience requirement moved from "1–5 years" ([2026-05-25](https://www.v2ex.com/t/1215230)) to "3–5 years" with a 211/985 degree and large-internet-company experience ([2026-07-28](https://www.v2ex.com/t/1230516)). The poster announced on 2026-05-27 that the backend headcount had been filled and closed, then reposted the role on 2026-07-28. Investors are unnamed in the May and June posts ("international top-tier VCs and strategic investors covering payments and cloud computing") and named in the July post, after the funding announcement. View counts were 3,645, 3,327, 2,036 and 982 respectively when accessed on 2026-07-29.
- **The recruitment posts state that the site needs a VPN to open from mainland China** ("需 vpn 打开网址", [2026-07-28](https://www.v2ex.com/t/1230516)), while the same posts recruit a developer advocate whose remit is the Chinese developer community and the site publishes simplified- and traditional-Chinese locales.
- **The company publishes an unusual amount of machine-readable surface for its size** — six discovery files, an OpenAPI 3.1 specification, per-locale site trees in 13 languages, and 240 catalog pages — while publishing no team page, careers page, or named engineering staff.
- **Most product depth sits behind the console.** Pricing per endpoint, usage logs, budgets and API-key management are described in documentation but require an account; `console.aisa.one` is behind a Cloudflare challenge.
- **The Machine-to-Machine surface is labelled Private Beta and Foundry Coming Soon** on the homepage, while the funding release, blog posts and the live `HTTP 402` challenge on `api.aisa.one` all describe machine payments as operating. The scope difference between the beta label and the live x402 mirror at `/apis/v2` is not explained on any reviewed page.

---

## Resources

**Official**

- [Homepage](https://aisa.one/)
- [News index](https://aisa.one/news) — [funding release, 2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)
- [Blog](https://aisa.one/blog) — [The Agent-Readable Web, 2026-04-23](https://aisa.one/blog/the-agent-readable-web) · [Data layer for Agentic Economy on Arc, 2026-04-23](https://aisa.one/blog/aisa-data-layer-agentic-economy-arc) · [Second place, Agentic Commerce on Arc, 2026-02-26](https://aisa.one/blog/aisa-awarded-second-place-agentic-commerce-arc-hackathon) · [Claws Out at ETHDenver 2026, 2026-02-27](https://aisa.one/blog/aisa-sponsors-claws-out-ethdenver-2026) · [Unified Gateway, 2026-02-19](https://aisa.one/blog/introducing-aisa-unified-gateway)
- [Documentation](https://aisa.one/docs) — [pricing](https://aisa.one/docs/guides/pricing) · [wallet and payments](https://aisa.one/docs/guides/pricing/wallet) · [rate limits](https://aisa.one/docs/api-reference/rate-limits) · [architecture](https://aisa.one/docs/evaluate/architecture) · [security evaluation](https://aisa.one/docs/evaluate/security) · [security and data privacy](https://aisa.one/docs/guides/security) · [machine payments for agents](https://aisa.one/docs/concepts/machine-payments-for-agents) · [docs index for agents](https://aisa.one/docs/llms.txt)
- [Catalogs](https://aisa.one/models) — [APIs](https://aisa.one/api) · [Skills](https://aisa.one/skills) · [AIsa CIO agent](https://aisa.one/agents/aisa-cio)
- [Agent Discovery](https://aisa.one/agent-discovery) — [agent-card.json](https://aisa.one/.well-known/agent-card.json) · [ai-plugin.json](https://aisa.one/.well-known/ai-plugin.json) · [mcp.json](https://aisa.one/.well-known/mcp.json) · [product llms.txt](https://aisa.one/llms.txt) · [sitemap.xml](https://aisa.one/sitemap.xml)
- [Terms of Service](https://aisa.one/TOS) · [Privacy Policy](https://aisa.one/privacy)
- [GitHub organisation `AISA-skills`](https://github.com/AISA-skills) — [search-research-skills](https://github.com/AISA-skills/search-research-skills) · [example SKILL.md](https://raw.githubusercontent.com/AISA-skills/search-research-skills/main/aisa-tavily/SKILL.md)

**Press releases**

- [AIsa Raises $6.5M to Build the AI Agent Resource Network — 2026-07-03](https://aisa.one/news/aisa-raises-6-5m-ai-agent-resource-network)
- [GlobeNewswire distribution of the same release — 2026-07-07](https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html)

**Third-party coverage and profiles**

- [Forbes — Startup Raises $6.5 Million…, 2026-07-03](https://www.forbes.com/sites/elainepofeldt/2026/07/03/startup-raises-65-million-by-making-it-easier-for-ai-employees-to-make-payments-online/)
- [Business Insider Markets — funding coverage, 2026-07](https://markets.businessinsider.com/news/stocks/aisa-raises-6-5m-co-led-by-alibaba-and-tribe-capital-to-build-the-transaction-network-for-ai-agents-1036305081)
- [Yahoo Finance — funding coverage, 2026-07](https://finance.yahoo.com/technology/ai/articles/aisa-raises-6-5m-co-204900040.html)
- [FinSMEs — AIsa Closes Seed Funding, 2026-07](https://www.finsmes.com/2026/07/aisa-closes-seed-funding.html)
- [CryptoRank — seed round summary, 2026-07-03](https://cryptorank.io/news/feed/alsa-seed-2026-07-03)
- [The AI Insider — seed round coverage, 2026-07-17](https://theaiinsider.tech/2026/07/17/aisa-secures-6-5m-co-led-by-alibaba-and-tribe-capital-to-build-the-transaction-network-for-ai-agents/)
- [ChainCatcher — pre-seed announcement, 2025-08-31 (ZH)](https://www.chaincatcher.com/article/2202064) · [EN](https://www.chaincatcher.com/en/article/2202064)
- [ChainCatcher — second pre-seed announcement, 2025-10-28 (ZH)](https://www.chaincatcher.com/article/2215658) · [EN](https://www.chaincatcher.com/en/article/2215658)
- [ChainCatcher — Solana x402 hackathon sponsorship, 2025-11-07 (ZH)](https://www.chaincatcher.com/article/2218188) · [EN](https://www.chaincatcher.com/en/article/2218188)
- V2EX recruitment posts by user `wateryfield` — [AI Engineer, 2026-05-21 (ZH)](https://www.v2ex.com/t/1214335) · [AI / backend / growth engineers, 2026-05-25 (ZH)](https://www.v2ex.com/t/1215230) · [Developer Advocate, 2026-06-24 (ZH)](https://www.v2ex.com/t/1222499) · [AI / backend / DevRel engineers, 2026-07-28 (ZH)](https://www.v2ex.com/t/1230516)
- [Draper Associates — portfolio entry](https://www.draper.vc/portfolio/alsa)
- [LinkedIn — company page](https://www.linkedin.com/company/aipayhq)
- [LinkedIn — "Unfiltered with Jordan Liu", Qin En Looi, 2026-05-11](https://www.linkedin.com/pulse/unfiltered-jordan-liu-founder-ceo-alsa-qin-en-looi--rytrc)
- [The Breakdown podcast — The Three Layers of AI Agent Commerce with Jordan Liu](https://open.spotify.com/episode/4lk37Fn2yiVrni6NIRvZri)
- [Dealroom — company profile (403 to automated access on 2026-07-29)](https://app.dealroom.co/companies/aisa_one_interface_for_compute_data_and_monetization)
