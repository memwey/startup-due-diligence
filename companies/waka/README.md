# Waka

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Waka ([hellowaka.com](https://www.hellowaka.com/)) describes itself as "stablecoin trade settlement infrastructure for operators moving value across emerging markets, starting with the Africa–Asia corridor." It offers local collections in African markets, a treasury layer holding fiat and USDT balances, and payouts through African, Asian and global rails including Alipay, WeChat Pay, FPS, FAST, SWIFT and USDT. A [Frontier Fintech partner piece dated 2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade), co-written with the CEO, is subtitled "A Partner Piece with Waka formerly Pyxis" — the name under which the same team operated from 2023.

- Reported traction: "over US$ 100m in annual flow across eight African markets" and "over 100 liquidity providers ... connected across 20 currencies" ([Frontier Fintech, 2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade) — a partner piece co-written with the CEO, not independent coverage).
- Team size: "about twenty people," members "in Africa, China, Singapore and Australia," per job postings dated [2026-07-28](https://www.v2ex.com/t/1230518); 12 people across four countries as of [2025-09-19](https://share.transistor.fm/s/27884a18), under the Pyxis name. [LinkedIn](https://www.linkedin.com/company/hellowaka/) lists the company at 11–50 employees (Undated; accessed 2026-07-29).
- No funding round has been announced under the Waka name. Pyxis was in the [Orbit Startups 2023 cohort](https://orbitventures.com/company/pyxis/) at seed stage.
- Hiring material lists Java / Spring Boot, Go, Node.js, Vue and React, but does not establish which backend stack is in production. Both roles are global-remote on a UTC+3 / UTC+8 collaboration window, with no published salary. The two postings were published on V2EX on [2026-07-28](https://www.v2ex.com/t/1230518) under the name **Pyxis**, giving hellowaka.com as the website. Separately, the publicly served customer-portal bundle confirms Vue 3 on the frontend and sends API calls to `https://api.pyxis.money` (Accessed 2026-07-29; see [Engineering](#engineering)).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Brand and site | Waka — [hellowaka.com](https://www.hellowaka.com/) | site |
| Domain created | 2025-12-11 (registrar Cloudflare) | WHOIS; Accessed 2026-07-29 |
| Entity named in legal docs | "Waka", registered office 3A Lionel Street, Doncaster East, VIC 3109, Australia | [General Terms V1.2, 2026-03-12](https://portal.hellowaka.com/static/GeneralTerms.html) |
| Governing law | New South Wales, Australia | [General Terms V1.2](https://portal.hellowaka.com/static/GeneralTerms.html) |
| Stated regulatory posture | "Waka provides services through entities registered with FINTRAC in Canada and AUSTRAC in Australia." | [site footer](https://www.hellowaka.com/); Undated; accessed 2026-07-29 |
| Contact | customerservice@hellowaka.com | [Terms](https://portal.hellowaka.com/static/GeneralTerms.html), [Privacy Policy](https://portal.hellowaka.com/static/PrivacyPolicy.html) |
| Headcount | "about twenty people" (2026-07-28); 12 across four countries (stated 2025-09-19, as Pyxis); LinkedIn band 11–50 (Undated; accessed 2026-07-29) | [V2EX posting](https://www.v2ex.com/t/1230518), [podcast](https://share.transistor.fm/s/27884a18), [LinkedIn](https://www.linkedin.com/company/hellowaka/) |
| Team locations | Members "in Africa, China, Singapore and Australia" (2026-07-28); "operators from Nairobi, Hong Kong, Singapore, and other trade hubs" (2026-02) | [V2EX posting](https://www.v2ex.com/t/1230518), [hellowaka.com, archived 2026-02-26](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) |
| HQ as stated in hiring material | "a fintech company headquartered in Singapore" | [V2EX posting, 2026-07-28](https://www.v2ex.com/t/1230518) |
| Engineering-team language (inferred) | No formal policy found. Engineering hiring is in Chinese; the Full-Stack role requires reading English material and basic English with overseas teams, while the Tech Lead role requires English with overseas teams and partners. The day-to-day primary language is not confirmed | [Tech Lead](https://www.v2ex.com/t/1230518), [Full-Stack Engineer](https://www.v2ex.com/t/1230527) |

### Identity and legal entities

| Type | Name | Status or jurisdiction | Evidence and limitation |
|---|---|---|---|
| Current public brand | Waka / hellowaka.com | In use | Website, portal and legal documents use Waka |
| Former or predecessor brand | Pyxis / Pyxis Pay | Described as "Waka formerly Pyxis" | [Frontier Fintech, 2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade) establishes brand continuity, not legal-entity identity |
| Entity named in current Terms | "Waka" | Australia; office stated in Victoria, governing law stated as New South Wales | [General Terms V1.2](https://portal.hellowaka.com/static/GeneralTerms.html); no registration number is published |
| Related entity | Pyxis Pay (Pte. Ltd.) | Singapore; UEN 202306267Z, established 2023 | [Singapore FinTech Association listing](https://membership.singaporefintech.org/company/202306267Z) |
| Related entity | Pyxis Pay Limited | Canada; incorporated 2023-10-16, FINTRAC registration now shown as expired | [FINTRAC MSB registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx); Accessed 2026-07-29 |

The observable continuity is: Pyxis says it was founded in 2022; Singapore and Canadian Pyxis entities appeared in 2023; hellowaka.com was registered in December 2025 and was publicly live by early 2026; and July 2026 hiring still used the Pyxis name while pointing to hellowaka.com. The Waka portal also calls `api.pyxis.money`. These facts support continuity of brand, team and product infrastructure. They do **not** establish that the Australian "Waka", the Singapore company and the Canadian company are the same legal entity, subsidiaries of one parent, or parties to a documented rename or asset transfer.

### Registry checks

Because the site's own footer names two regulators, both public registers were searched on 2026-07-29:

| Register | Query | Result |
|---|---|---|
| [FINTRAC Money Services Business Registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) | "waka" | No matching entity |
| [FINTRAC Money Services Business Registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) | "pyxis" | **PYXIS PAY LIMITED**, MSB registration M24908802, services "Foreign Exchange, Money Transferring", initial approval 2024-01-22, expiry date 2026-01-23, **status "Expired"** |
| [AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/) | "waka" | No matching entity |
| [AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/) | "pyxis" | "No match found" |
| [ABN Lookup](https://abr.business.gov.au/) | "waka", postcode 3109 (the address in the Terms) | No matching entity |
| [CBK Directory of Authorized Payment Service Providers, 2025-11-06](https://www.centralbank.go.ke/wp-content/uploads/2025/11/Directory-of-Authorized-Payment-Service-Providers-6-November-2025.pdf) | "Pyxis", "Waka" | Neither name appears |

AUSTRAC's Virtual Asset Service Provider Register returned no results for any query attempted, including a known Australian exchange used as a control, so no conclusion is drawn from it.

### Market context as stated by the company

From the [Frontier Fintech partner piece (2026-04-20)](https://frontierfintech.substack.com/p/117-payments-follow-trade), co-written with CEO April Long:

- Stablecoin transfer volume reached US$27.6 trillion in 2024, with B2B transfers the largest single use case.
- On-ramp and off-ramp costs are said to have compressed from 3–4% to below 0.5%; two years earlier, on-ramping in Nairobi and off-ramping in Singapore carried combined costs of 3–4%.
- The stated position is that stablecoins should be "backend rails while keeping the customer experience fiat-facing."

From the founder's own newsletter, [2026-05-05](https://aprilnewsletter.substack.com/p/arent-remittance-companies-already): Africa remittances of US$95bn (2024), China–Africa trade of US$295.56bn (2024), Africa's total merchandise trade of ~US$1.53tn (2024), and China exports to Africa up 25.8% year-on-year in 2025. At the [2024 China-Africa Digital Financial Inclusion Summit](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html), China–Africa trade was given as US$282bn for the prior year.

---

## Product

The public site organizes the product as three layers plus a portal and API. There is no product documentation site; the descriptions below come from [hellowaka.com](https://www.hellowaka.com/) (Undated; accessed 2026-07-29).

### Feature areas

- **Collections** — "Virtual accounts and named collection flows across supported local markets," via mobile money and bank rails.
- **Treasury** — "Balances, beneficiaries, approvals, FX and stablecoin movement live in one treasury view," with KYB, approvals and exports.
- **Payouts** — "Named payouts to approved beneficiaries through supported African, Asian, and global rails": Alipay, WeChat Pay, FPS, FAST, SWIFT, USDT.
- **Stablecoin treasury and ramps** — movement between fiat and stablecoin rails (USDT on-ramp and off-ramp) "with business controls and corridor-level approvals."
- **Dashboard** — FX quotes, exports, beneficiaries, payout status, counterparties, exportable records.
- **API** — "Programmatic access to virtual accounts, payout instructions, FX rates, counterparties, and webhooks." No public developer documentation was found.

The stated onboarding flow is: KYB and corridor approval → collect, hold and convert → pay out and reconcile.

### Coverage

| Side | Markets and rails | Source |
|---|---|---|
| Africa (collect and pay out) | Kenya, Tanzania, Uganda, Ghana, Gabon, Cameroon, Chad, Congo, Nigeria, Senegal, South Africa, Equatorial Guinea, Central African Republic — "More Markets to Come" | [hellowaka.com](https://www.hellowaka.com/) |
| China | SWIFT, Local Bank, Alipay, WeChat | [hellowaka.com](https://www.hellowaka.com/) |
| Hong Kong | SWIFT, RTGS, FPS | [hellowaka.com](https://www.hellowaka.com/) |
| Singapore | SWIFT, FAST | [hellowaka.com](https://www.hellowaka.com/) |
| Global | SWIFT | [hellowaka.com](https://www.hellowaka.com/) |

The 13-market African list is the same set that [pyxis.money](https://www.pyxis.money/) lists (Kenya under C2C, the remaining twelve under B2B; Undated; accessed 2026-07-29).

### Commercialization

No public price list was found. The [General Terms V1.2 (2026-03-12)](https://portal.hellowaka.com/static/GeneralTerms.html) state that "The Service Fees are charged separately depending on the Service used by the Customer or as otherwise agreed in writing with us," and refer to a fee schedule on the website; no such schedule was published on the site when accessed on 2026-07-29. The Terms describe the services as "collection services, payout services, foreign exchange services, online payment acceptance services, and technology services."

The [Frontier Fintech piece (2026-04-20)](https://frontierfintech.substack.com/p/117-payments-follow-trade) describes the offering as "a fully integrated service that runs from local relationship managers and client onboarding, through FX liquidity management and market making, across a stablecoin settlement rail, and all the way to compliant CNY settlement into the Chinese mainland, with the documentation package that makes each payment legible to the SAFE and PBOC frameworks." It also states the customer portfolio is structured across three tiers: "high-volume stability anchors, a core profit layer, and high-spread alpha positions."

### Reported scale and claims over time

| Date | Reported figure or claim | Source |
|---|---|---|
| 2024-08-22 | Kenyan traders will be able to pay up to US$70,000 via WeChat; integration with Alipay described as in progress | [Business Daily](https://www.businessdailyafrica.com/bd/corporate/technology/kenyan-traders-to-pay-for-chinese-goods-via-alipay-4735424) |
| 2024-08-27 | Deal being finalized for transactions up to US$70,000 via WeChat Pay | [China Daily](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html) |
| 2024-08-29 | Described as "currently in pilot phase" | [NTU-SBF Centre for African Studies](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform) |
| 2025-09-19 | 12-person team across four countries; described as having revenue; 90% of effort had gone to small traders before a pivot to bulk traders | [African Tech Roundup podcast](https://share.transistor.fm/s/27884a18) |
| 2026-02-26 (site as archived) | "24 hrs Typical Settlement", "70% FX Cost Reduction", "2-4 wks Integration Time"; "Up to 70% cheaper than traditional routes"; "The first stablecoin trade settlement network with direct RMB delivery" | [Wayback capture](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) |
| 2026-04-20 | "over US$ 100m in annual flow across eight African markets, generating a respectable ARR on modest working capital"; "Over 100 liquidity providers are connected across 20 currencies" | [Frontier Fintech](https://frontierfintech.substack.com/p/117-payments-follow-trade) |
| 2026-07-28 | "About twenty people," members in Africa, China, Singapore and Australia; company described as "in a phase of rapidly building product and core systems, not a pure maintenance role on mature systems," and "building payment products, merchant systems, API services and internal operations tooling from 0 to 1" | [V2EX postings](https://www.v2ex.com/t/1230518) |
| Accessed 2026-07-29 | 13 African markets listed; no headline metrics, no "first" claim, no settlement-time or cost-reduction figures | [hellowaka.com](https://www.hellowaka.com/) |

### Announced customers and partners

| Date | Party | Detail | Source |
|---|---|---|---|
| 2024-08-22 | Alipay, WeChat Pay | Announced as integration partners for Kenya–China payments, under the Pyxis name | [Business Daily](https://www.businessdailyafrica.com/bd/corporate/technology/kenyan-traders-to-pay-for-chinese-goods-via-alipay-4735424) |
| n.d. (site) | WeChat Pay, UnionPay, M-PESA, Tencent, Alipay | Listed as partnerships on the Pyxis site and investor page; the Pyxis newsroom section reproduces media headlines about the WeChat Pay and Alipay launches | [pyxis.money](https://www.pyxis.money/), [Orbit Ventures](https://orbitventures.com/company/pyxis/) |
| 2026-04-20 | — | "the company has begun serving large Chinese enterprises with continent-wide B2B distribution networks" | [Frontier Fintech](https://frontierfintech.substack.com/p/117-payments-follow-trade) |

No named Waka customer has been published. The [Frontier Fintech piece](https://frontierfintech.substack.com/p/117-payments-follow-trade) states that Waka's liquidity providers include "partners backed by Visa Ventures, Coinbase Ventures, and Tether" — this describes the backers of Waka's partners, not investors in Waka.

### Stated plans

From the [Frontier Fintech piece (2026-04-20)](https://frontierfintech.substack.com/p/117-payments-follow-trade), the commercial roadmap runs in two directions: (1) "deepening the enterprise relationship on both sides of the corridor," working with large corporations in Africa and China; and (2) "expanding into the payment company channel: African fintechs and cross-border platforms that are already processing trade-related flows and need a compliant, liquid path into China."

---

## Founder

**April Long** — CEO and co-founder of Waka ([Frontier Fintech, 2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)); previously co-founder and CEO of Pyxis ([Orbit Ventures](https://orbitventures.com/company/pyxis/), [NTU-SBF CAS, 2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)).

- Was present to receive President Xi Jinping in Tanzania at age 23; the [2025-09-19 podcast](https://share.transistor.fm/s/27884a18) gives the age at the time of recording as 35.
- 2015: at Standard Chartered, working with Chinese trading company clients on lending ([podcast, 2025-09-19](https://share.transistor.fm/s/27884a18)).
- China desk manager at Standard Chartered Bank Kenya; described as fluent in Chinese and familiar with both the Kenyan and Chinese financial systems ([NTU-SBF CAS, 2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)).
- Also worked at Gulf African Bank; described as having "10+ years in Africa-Asia corridor financial services" and as having founded Waka "after a decade of managing the China-Africa corridor from inside Standard Chartered Kenya and Gulf African Bank" ([Frontier Fintech, 2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)).
- Co-founded Pyxis; the [Pyxis about page](https://www.pyxis.money/about) dates the founding to 2022, while corporate records date the Singapore and Canadian entities to 2023 (see [Notes](#notes)).
- Resident in Nairobi as of [2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform); [LinkedIn](https://www.linkedin.com/in/longapril/) lists Singapore as location (as reported in search results, 2026-07-29; the profile itself returns HTTP 999 to automated fetches).
- Spoke at the 2024 China-Africa Digital Financial Inclusion Summit ([China Daily, 2024-08-27](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html)).
- Writes [April's Newsletter](https://aprilnewsletter.substack.com/) on Substack, first post [2025-09-05](https://aprilnewsletter.substack.com/p/welcome-to-aprils-newsletter). The [about page](https://aprilnewsletter.substack.com/about) states: "I build cross-border payment infrastructure for emerging markets." The newsletter does not name Waka in the posts reviewed.
- Long-form interview: [African Tech Roundup, 2025-09-19](https://share.transistor.fm/s/27884a18) — covers a pivot from serving SMEs to serving bulk traders and aggregators.

**George Chan** — Singaporean; co-founder of Pyxis, listed as COO by [Orbit Ventures](https://orbitventures.com/company/pyxis/). Previously at CrimsonLogic, then general manager for Africa at GUUD, a trade technology company; described as fluent in Chinese and resident in Nairobi ([NTU-SBF CAS, 2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)). No Waka role has been published.

**Other people identified**

| Name | Role | Stated background | Source |
|---|---|---|---|
| Michael Ogongo | Head of Partnerships, Waka | Previously at Antler East Africa; Cornell University; based in New York | [LinkedIn](https://www.linkedin.com/in/michael-ogongo-2a666612a/) |

No company team page, leadership page, or "about" page exists on hellowaka.com. The archived [February 2026 site](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) described the team only in aggregate: "operators from Nairobi, Hong Kong, Singapore, and other trade hubs who have spent years inside emerging market payments, FX, and compliance."

---

## Funding (Pyxis predecessor)

| Date | Round | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2023 (cohort) | Seed | Not disclosed | Orbit Startups 2023 cohort (Pyxis) | — | [Orbit Ventures](https://orbitventures.com/company/pyxis/) |

All funding evidence found belongs to the Pyxis predecessor; none establishes which present Waka-related legal entity, if any, received the investment. No round has been announced under the Waka name as of 2026-07-29.

**Unconfirmed database lead:** a search-result summary attributed a 2023-09-18 seed round to SOSV. The [Crunchbase Pyxis profile](https://www.crunchbase.com/organization/pyxis-8b86) returned HTTP 403 when accessed on 2026-07-29, and no primary announcement confirming that date or investor was found. Orbit Startups is affiliated with SOSV, which is consistent with, but does not confirm, the attribution.

The [Orbit Ventures portfolio page](https://orbitventures.com/company/pyxis/) tags the company as Digitization, Women Founders, Kenya, Seed, Fintech and "Orbit Startups 2023"; lists April Long as CEO and George Chan as COO; and states that Pyxis "has secured partnerships with big fintech players including WeChat Pay, UnionPay, and M-PESA and has processed millions in transactions," addressing "a thriving $500Bn market and growing 10% annually." It states no round date or amount.

In the [2025-09-19 podcast](https://share.transistor.fm/s/27884a18), the CEO described the company as effectively un-funded relative to competitors — "Without millions to burn on market education" and "I'm grateful I didn't have money to burn" — and the [2026-04-20 partner piece](https://frontierfintech.substack.com/p/117-payments-follow-trade) refers to revenue generated "on modest working capital."

---

## Engineering

### Technology stack and platforms

The Pyxis/Waka naming evidence is summarized under [Identity and legal entities](#identity-and-legal-entities). The two technical sources below agree where they overlap.

**Mentioned in job postings, not confirmed as the production stack.** Two postings were placed on V2EX on 2026-07-28 by user `Charles678` under the company name **Pyxis**, giving `hellowaka.com` as the website and `ncrew@pyxis.money` as the application address: a [Tech Lead role](https://www.v2ex.com/t/1230518) and a [Full-Stack Engineer role](https://www.v2ex.com/t/1230527).

| Posting | Concrete technologies named | Evidence status |
|---|---|---|
| Full-Stack Engineer | Java / Spring Boot preferred; Go and Node.js also welcome; Vue, React or another mainstream frontend framework; REST API and databases required; Docker, cloud services, CI/CD and Python preferred | Hiring requirement only |
| Tech Lead | At least one of Java / Spring Boot, Go or Node.js; databases, caching, message queues and APIs required; cloud services and CI/CD preferred | Hiring requirement only; the posting says specific choices are still evolving |

Experience with high availability, production stability, observability, security, payment and settlement systems, external integrations, Web3, and 0-to-1 platform building is recorded under [Technical background sought](#technical-background-sought), rather than treated as evidence of the current stack.

**Inferred from publicly served front-end assets** and HTTP headers; Accessed 2026-07-29:

| Layer | Observation |
|---|---|
| Marketing site | Built and hosted on [Framer](https://www.framer.com); `robots.txt` and `sitemap.xml` on hellowaka.com point at `blissful-shortbread-214183.framer.app` |
| Customer portal | `portal.hellowaka.com` — Vite-built single-page app (`/assets/index-<hash>.js`, ES module entry), Vue 3 with `vue-router` and Pinia, Ant Design Vue component library (`AButton`, `AForm`, `ATable`, … in the bundle), axios HTTP client, Inter via Google Fonts |
| Web server | `server: openresty` on portal.hellowaka.com |
| API backend | The portal's axios interceptor sets `baseURL:"https://api.pyxis.money"` with `withCredentials:true` and a 120-second timeout. Endpoint paths visible in the bundle include `/api/client/v1/user/login/email`, `/api/client/v1/user/register/kyc/email`, `/api/client/v1/user/password/reset/by-code`, and `/api/form-config/get-form-config` |
| Anti-bot | GeeTest CAPTCHA v4, named in the [Privacy Policy](https://portal.hellowaka.com/static/PrivacyPolicy.html) as collecting "data for its AI-powered risk engine" |
| Analytics | "Google stats or similar provider via cookies" ([Privacy Policy](https://portal.hellowaka.com/static/PrivacyPolicy.html)) |
| Other | The portal's HTML loads `https://mcp.figma.com/mcp/html-to-design/capture.js`, and its HTML comments are written in Simplified Chinese |

### Systems

The [Tech Lead posting](https://www.v2ex.com/t/1230518) names the core modules directly: "merchants, orders, payments, settlement, reconciliation and Partner API." The [engineering posting](https://www.v2ex.com/t/1230527) splits the work the same way:

| Area | What the posting says it covers |
|---|---|
| Backend and API | Order, payment, settlement, reconciliation and merchant management modules; business interfaces, data models, permission control, core business logic; transaction consistency, exception retries, log tracing, performance optimization; integration with third-party Partners, payment channels and external systems; API onboarding, signature authentication, exception handling |
| Frontend and internal tools | Merchant Portal and internal operations back-office; turning "complex payment, settlement, reconciliation and risk-control flows into clear, usable interfaces"; working with operations, compliance and sales to turn repetitive work into tooling; "AI Bot and business automation tools" |
| Engineering quality | Production troubleshooting, log analysis, stability work; code quality, engineering standards, testability; using AI tools for coding, debugging, testing, refactoring and documentation |

The Tech Lead role additionally owns "the payment platform's technical architecture, system boundaries and evolution roadmap," establishing "testing, release, monitoring, logging and security standards," and managing technical debt "between delivery speed, system quality and long-term cost."

The portal's client-side router exposes the same surface from the operator's side. One route per screen, as read from the production bundle on 2026-07-29:

| Route | What it appears to cover |
|---|---|
| `/register`, `/login`, `/security` | Email-based registration and login, password reset by emailed code, account security |
| `/kyb/verification`, `/verification/business` | Know-your-business onboarding and document submission |
| `/virtual-accounts` | Virtual account issuance for collections |
| `/pay-ins`, `/pay-outs`, `/orders` | Collection and disbursement instructions, and order history |
| `/balances/`, `/balances/deposit`, `/balances/exchange`, `/balances/withdraw` | Multi-currency balances, deposits, FX conversion, withdrawals |
| `/batch-uploads`, `/batch-uploads/:batchNo`, `/batch-uploads/new` | Bulk payout file upload and per-batch detail |
| `/dev-management` | Developer/API credential management |
| `/permissions` | User roles within a customer account |
| `/dashboard/`, `/homepage` | Landing and overview screens |

No public API reference, OpenAPI/AsyncAPI specification, SDK, sandbox, changelog, or status page was found. `docs.hellowaka.com`, `api.hellowaka.com`, `developer.hellowaka.com`, `app.hellowaka.com` and `status.hellowaka.com` do not resolve; `portal.hellowaka.com` is the only subdomain that responds.

### Technical background sought

The postings seek prior work on payment and settlement systems, third-party payment-channel and partner-API integration, merchant portals and internal operations tooling, transaction consistency, idempotency, retries and compensation, and observability, monitoring and release standards. Payment, clearing and settlement, accounting, trading or banking experience is preferred rather than required. On-chain settlement, digital-asset payments or Web3 appears only as a preferred item on the Tech Lead role; it is not evidence that the current production system uses an EVM chain or any particular blockchain stack. No crawling or ERP-integration background is requested.

### Industry domain

Africa–Asia trade settlement. From the company's own published material:

- **Chinese inbound settlement rules.** The [partner piece](https://frontierfintech.substack.com/p/117-payments-follow-trade) states that each payment ships with "the documentation package that makes each payment legible to the SAFE and PBOC frameworks" — China's State Administration of Foreign Exchange and central bank.
- **Multi-jurisdiction AML/KYB.** Collections across 13 African markets and payouts into China, Hong Kong and Singapore, each with its own registration and reporting regime; the site's own footer scopes availability to "KYB, compliance review, supported corridors, and applicable regulatory requirements."
- **FX and market making.** The service description includes "FX liquidity management and market making" across a stated 20 currencies and 100+ liquidity providers.
- **Local rails.** Mobile money (M-PESA is named on the Pyxis side), bank transfer, Alipay, WeChat Pay, FPS, FAST, RTGS, SWIFT, and USDT on-/off-ramps.
- **RMB internationalization.** The founder's newsletter covers [PBOC clearing-bank structure](https://aprilnewsletter.substack.com/p/standard-banks-rmb-clearing-news) (2026-06-29), [direct RMB payment for African merchants](https://aprilnewsletter.substack.com/p/deep-dive-why-do-we-need-rmb-payment) (2025-12-17), and [policy effects on the USDT/CNY peg](https://aprilnewsletter.substack.com/p/how-policy-is-reshaping-the-usdtcny) (2025-12-11).

The [engineering posting (2026-07-28)](https://www.v2ex.com/t/1230527) states the expectation directly: "We do not require you to be familiar with African payments or cross-border finance to begin with, but we hope you are willing to understand merchants, operations, compliance, payment channels and settlement flows, and then turn these business problems into reliable products and systems." Domain knowledge is therefore framed as something to be learned on the job rather than hired for — payment/fintech background appears only under "plus points" on both roles.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Employment form | Tech Lead: "full-time, remote." Full-Stack Engineer: "full-time fixed-term contract, remote work" — the two roles are offered on different contract terms | [Tech Lead](https://www.v2ex.com/t/1230518), [Full-Stack](https://www.v2ex.com/t/1230527) |
| Location | "Global remote" for both roles. No office address is published for Waka; the Terms give an Australian registered office; the postings describe the company as headquartered in Singapore | [postings](https://www.v2ex.com/t/1230518), [Terms](https://portal.hellowaka.com/static/GeneralTerms.html) |
| Time zone | "Main collaboration time zones: UTC+3 / UTC+8" (both roles) | [postings](https://www.v2ex.com/t/1230518) |
| Equity | "Company options: early standout contributors have the opportunity to receive them" (both roles) | [postings](https://www.v2ex.com/t/1230518) |
| Engineering-team language (inferred) | No formal policy found. Both postings are in Chinese. The Full-Stack role requires reading English material and basic English communication with overseas teams; the Tech Lead role requires English communication with overseas teams and partners. This establishes a need for English in cross-border work, but not the team's primary day-to-day language | [Tech Lead](https://www.v2ex.com/t/1230518), [Full-Stack Engineer](https://www.v2ex.com/t/1230527) |
| Salary | Not stated in either posting; two questions about the range on the [engineering thread](https://www.v2ex.com/t/1230527) were unanswered as of 2026-07-29 | [posting thread](https://www.v2ex.com/t/1230527) |
| AI tooling | Stated as an expectation rather than a perk: the engineering role requires that a candidate "proactively uses AI engineering tools, rather than developing only in the traditional way," and both roles list "deep use of Codex, Claude Code or similar AI engineering tools" as a plus | [postings](https://www.v2ex.com/t/1230518) |
| Stated working environment | Both postings describe underspecified requirements — "many requirements have no complete spec" — and a 0-to-1 build phase rather than maintenance of mature systems | [postings](https://www.v2ex.com/t/1230527) |
| Visa, benefits, turnover | Not published | — |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): hellowaka.com and pyxis.money navigation, `robots.txt`, sitemaps, portal and legal pages; current and archived brand sites; searches for Waka, Pyxis and Pyxis Pay in English and Chinese; common documentation, API, status and careers subdomains; GitHub searches by company, domain and product name; the two identified V2EX job threads; company and founder social profiles; FINTRAC, AUSTRAC, ABN and Singapore records; investor portfolios and funding databases.

- No careers page on either hellowaka.com or pyxis.money. The only hiring material found is two V2EX threads posted on 2026-07-28, neither linked from any company property.
- No salary bands, visa policy, or benefits in either posting; direct questions about the range went unanswered in the thread.
- No engineering blog, conference talks, open-source repositories, or public technical writing under the Waka or Pyxis name.
- No public API documentation, SDK, sandbox, or status page, despite the site marketing an API as "the scale layer."
- No published price list or fee schedule, although the Terms refer to one on the website.
- No team or leadership page. Only two people are publicly identifiable as being at Waka (the CEO and the Head of Partnerships).
- No named security certification (ISO 27001, SOC 2, PCI DSS) is claimed anywhere on the site or in the legal documents.
- No corporate registration number, ABN/ACN, or licence number is published for the "Waka" entity named in the Terms.
- No funding round, amount, valuation, or investor list under the Waka name.
- Whether George Chan, the Pyxis co-founder, has a role at Waka.

### Inconsistencies across sources

- **Regulatory registrations.** The [site footer](https://www.hellowaka.com/) states services are provided "through entities registered with FINTRAC in Canada and AUSTRAC in Australia." As of 2026-07-29, the only related entity in the [FINTRAC MSB registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) is PYXIS PAY LIMITED, whose registration M24908802 is listed with status "Expired" and an expiry date of 2026-01-23; no entity named Waka appears. The [AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/) returns no match for either name. This may mean the registered entities trade under names not identified here.
- **Jurisdiction in the Terms.** The [General Terms V1.2](https://portal.hellowaka.com/static/GeneralTerms.html) give a registered office in Doncaster East, Victoria, but state the Terms "will be governed by and constructed in accordance with the laws of the New South Wales, Australia."
- **Founding year of the predecessor.** The [Pyxis about page](https://www.pyxis.money/about) says "Since its founding in 2022"; the [Singapore FinTech Association listing](https://membership.singaporefintech.org/company/202306267Z) gives Pyxis Pay Pte. Ltd. as established 2023 (UEN 202306267Z); [FINTRAC](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) records Pyxis Pay Limited as incorporated 2023-10-16.
- **Headcount over time and by source type.** The predecessor reported 12 people across four countries on [2025-09-19](https://share.transistor.fm/s/27884a18); the Waka/Pyxis hiring post stated "about twenty people" on [2026-07-28](https://www.v2ex.com/t/1230518). [LinkedIn](https://www.linkedin.com/company/hellowaka/) gives only a broad 11–50 band (Undated; accessed 2026-07-29), so it is not treated as a competing point estimate.
- **Where the team is.** The postings place members "in Africa, China, Singapore and Australia"; the [February 2026 site](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) said "Nairobi, Hong Kong, Singapore, and other trade hubs." Neither list mentions the other's Hong Kong or China respectively.
- **Product claims between site versions.** The [2026-02-26 capture](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) claimed "24 hrs Typical Settlement," "70% FX Cost Reduction," "Up to 70% cheaper than traditional routes," and "The first stablecoin trade settlement network with direct RMB delivery." None of these figures or the "first" claim appear on the [site as of 2026-07-29](https://www.hellowaka.com/).
- **Independence of the traction figures.** The US$100m annual flow, eight markets, 100+ liquidity providers and 20 currencies all come from a single source, the [Frontier Fintech piece](https://frontierfintech.substack.com/p/117-payments-follow-trade), which its own subtitle and byline identify as "A Partner Piece" "Co-Written with April Long, CEO and Cofounder at Waka." No independent confirmation of these figures was found.

### Other

- **Reported strategy change.** In the [2025-09-19 podcast](https://share.transistor.fm/s/27884a18) the CEO described spending two years targeting African SMEs with, by their account, "zero demand after six months embedded in Nairobi's wholesale markets," before pivoting to bulk traders and Chinese trading companies — stating "90% of African trade is still happening in a more traditional way." The current site is addressed to "importers, fintechs, treasury teams, marketplaces, stablecoin businesses, and OTC desks," not to small merchants.
- **Published product surface.** Waka publishes no developer documentation, API reference, price list, or status page. The Terms and Privacy Policy, both V1.2 dated 2026-03-12, are the only public documents with any specificity.

---

## Resources

**Official**

- [Waka — hellowaka.com](https://www.hellowaka.com/)
- [Waka Partner Portal](https://portal.hellowaka.com/)
- [General Terms V1.2, 2026-03-12](https://portal.hellowaka.com/static/GeneralTerms.html)
- [Privacy Policy V1.2, 2026-03-12](https://portal.hellowaka.com/static/PrivacyPolicy.html)
- [LinkedIn — Waka](https://www.linkedin.com/company/hellowaka/)
- [April's Newsletter (founder's Substack, linked as the company blog)](https://aprilnewsletter.substack.com/)
  - [Welcome to April's Newsletter — 2025-09-05](https://aprilnewsletter.substack.com/p/welcome-to-aprils-newsletter)
  - [How policy is reshaping the USDT/CNY peg — 2025-12-11](https://aprilnewsletter.substack.com/p/how-policy-is-reshaping-the-usdtcny)
  - [Africa's Trade Urgently Needs RMB Payments At Source — 2025-12-15](https://aprilnewsletter.substack.com/p/beyond-payment-why-rmb-is-the-api)
  - [Why African Merchants Can't Pay Suppliers and How Direct RMB Payment Fixes it — 2025-12-17](https://aprilnewsletter.substack.com/p/deep-dive-why-do-we-need-rmb-payment)
  - [Aren't Remittance Companies Already Doing Trade Payments? — 2026-05-05](https://aprilnewsletter.substack.com/p/arent-remittance-companies-already)
  - [Standard Bank's RMB Clearing News Is Bigger Than Another Payment Rail — 2026-06-29](https://aprilnewsletter.substack.com/p/standard-banks-rmb-clearing-news)

**Predecessor brand (Pyxis)**

- [pyxis.money](https://www.pyxis.money/) · [About](https://www.pyxis.money/about)
- [Singapore FinTech Association — Pyxis Pay (Pte. Ltd.), UEN 202306267Z](https://membership.singaporefintech.org/company/202306267Z)
- [Orbit Ventures — Pyxis portfolio page](https://orbitventures.com/company/pyxis/)
- [Crunchbase — Pyxis](https://www.crunchbase.com/organization/pyxis-8b86) (returns HTTP 403 to automated fetches)

**Job postings** (posted under the name Pyxis; applications to `ncrew@pyxis.money`; language tag: ZH)

- [V2EX 酷工作 — Tech Lead, Java/Go/Node, cross-border payment infrastructure — 2026-07-28 20:21 +08:00 (ZH)](https://www.v2ex.com/t/1230518)
- [V2EX 远程工作 — Full-Stack Engineer — 2026-07-28 20:56 +08:00 (ZH)](https://www.v2ex.com/t/1230527)

**Registries and primary records**

- [FINTRAC Money Services Business Registry (XLSX)](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) · [registry search](https://fintrac-canafe.canada.ca/msb-esm/reg-eng)
- [AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/) · [Virtual Asset Service Provider Register](https://online.apps.austrac.gov.au/vaspr/)
- [ABN Lookup (Australia)](https://abr.business.gov.au/)
- [CBK Directory of Authorized Payment Service Providers, 2025-11-06 (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2025/11/Directory-of-Authorized-Payment-Service-Providers-6-November-2025.pdf)
- [Internet Archive — hellowaka.com](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/)

**Third-party coverage and profiles**

- [Frontier Fintech — "#117 Payments Follow Trade", 2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade) — partner piece co-written with the CEO; the source of all current traction figures
- [African Tech Roundup — "April Long of Pyxis: Why serving bulk traders beats saving SMEs in Africa-China trade", 2025-09-19](https://share.transistor.fm/s/27884a18) · [SoundCloud](https://soundcloud.com/african-tech-round-up/april-long-of-pyxis-why)
- [NTU-SBF Centre for African Studies — "Singaporean targets Kenya-China trade with new payment platform", 2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)
- [Business Daily (Kenya) — "New platform allows Kenyan traders to pay for Chinese goods via Alipay", 2024-08-22](https://www.businessdailyafrica.com/bd/corporate/technology/kenyan-traders-to-pay-for-chinese-goods-via-alipay-4735424)
- [China Daily — "Technology to boost e-commerce role in China-Africa trade", 2024-08-27](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html)
- [LinkedIn — April Long](https://www.linkedin.com/in/longapril/) (Undated; accessed 2026-07-29 via search results; profile returns HTTP 999 to automated fetches)
- [LinkedIn — Michael Ogongo, Head of Partnerships](https://www.linkedin.com/in/michael-ogongo-2a666612a/)
