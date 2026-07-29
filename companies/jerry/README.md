# Jerry

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Jerry (`jerry.ai`, formerly `getjerry.com`) is a Palo Alto company founded in 2017 and incubated in Y Combinator's Summer 2017 batch ([YC profile](https://www.ycombinator.com/companies/jerry-inc); Undated; accessed 2026-07-29). It operates a licensed insurance brokerage and a consumer mobile app that compares car, home, renters and motorcycle insurance across 100+ carriers, switches the policy, then adds free car-care and phone-telematics features on top ([how Jerry works](https://jerry.ai/how-jerry-works/), [car care](https://jerry.ai/car-care/), [driver safety](https://jerry.ai/driver-safety/); Undated; accessed 2026-07-29). Revenue comes from carrier commissions ([FAQ](https://jerry.ai/faq/)). It also sells the generative-AI agent platform it built for its own support desk as a separate product, Propelix.

- **Scale and financing:** 5M+ customers, $242M raised through a 2023 Series C2, last disclosed valuation $450M at the 2021 Series C ([Series C release, 2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/), [Carrier Management, 2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm)).
- **The company says it is profitable.** Job descriptions state "profitable since 2024" and "scaled revenue 70X"; the LinkedIn page claims 68% year-over-year revenue growth in 2025 ([jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai); accessed 2026-07-29, [LinkedIn](https://www.linkedin.com/company/jerryinc); accessed 2026-07-29).
- **Stack** — confirmed from public assets: Kong 3.9.3 gateway, nginx, AWS (CloudFront, S3, Lambda@Edge), NestJS, React/Next.js, Contentful, self-hosted Sentry, Datadog RUM, GrowthBook, WordPress for the marketing site. From closed job postings: Node.js + TypeScript, Go, Python, React Native, Postgres, Redis, DynamoDB, ClickHouse.
- **No engineering role is open.** As of 2026-07-29 the careers board lists 47 roles in Insurance (15), Data (13), Marketing (10), Product (7) and Business Development (2), and none in Engineering ([jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)). Engineering postings existed on the same board earlier — the Toronto new-grad listing was removed on [2025-11-24](https://builtintoronto.com/job/software-engineer-entry/7776678) — and now return null.
- **The AI platform is homegrown and is being productized.** Postings describe a system automating ">70% of inbound sales and service requests (over 50k chats per month)", built before off-the-shelf tooling existed, with prompts spread "across six separate locations"; the same platform is sold as [Propelix](https://propelix.ai), whose terms identify it as "a product of Jerry Services, Inc." ([Propelix Terms of Use](https://propelix.ai/terms); Last Updated 2025-10-22).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | Jerry; marketed as "America's first and only AllCar™ app" | [about](https://jerry.ai/about/), [LinkedIn](https://www.linkedin.com/company/jerryinc) |
| Parent entity | Jerry Services, Inc. | [insurance licenses](https://jerry.ai/insurance-licenses/), [terms of use](https://jerry.ai/terms-of-use/) |
| Licensed brokerage entity | Jerry Insurance Agency, LLC — "a wholly owned subsidiary of Jerry Services, Inc." | [insurance licenses](https://jerry.ai/insurance-licenses/) |
| Other named entity | Jerry Offers Inc. | [privacy policy](https://jerry.ai/privacy-policy/); Updated 2026-07-20 |
| Producer numbers | National Producer Number 18788611; California resident licence 0M34848; licensed in all 50 states and Washington, D.C. | [insurance licenses](https://jerry.ai/insurance-licenses/) |
| Address | 430 Sherman Ave, Suite 305, Palo Alto, CA 94306 | [terms of use](https://jerry.ai/terms-of-use/); Updated 2024-01-17 |
| Founded | 2017; Y Combinator Summer 2017 batch | [about](https://jerry.ai/about/), [YC profile](https://www.ycombinator.com/companies/jerry-inc) |
| App launch | Company says January 2019; the iOS listing's first release date is 2017-11-11 | [about](https://jerry.ai/about/), [iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950) |
| Founders | Art Agrawal (CEO), Musawir Shah (CTO), Lina Zhang (VP Operations) | [team](https://jerry.ai/team/) |
| Customers | 5M+ (reached 5 million in 2024) | [about](https://jerry.ai/about/) |
| Carriers compared | 100+ insurers | [how Jerry works](https://jerry.ai/how-jerry-works/) |
| Total raised | $242M through the 2023 Series C2; company materials in 2026 say "$240M+" | [Carrier Management, 2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm), [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Headcount | Not published by the company. YC profile 225; Built In 296; LinkedIn band 201–500 with 402 profiles | [YC profile](https://www.ycombinator.com/companies/jerry-inc), [Built In](https://builtin.com/company/jerry), [LinkedIn](https://www.linkedin.com/company/jerryinc) |
| Offices | 2026 postings say fully remote with offices in Palo Alto, New York, Chicago and Toronto | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Engineering working language | English; the historical engineering hubs are Toronto and the San Francisco Bay Area | [Built In Toronto posting](https://builtintoronto.com/job/software-engineer-entry/7776678); removed 2025-11-24 |
| GitHub organisation | [getjerry](https://github.com/getjerry), verified, created 2017-05-16, location Palo Alto, 32 public repositories | [GitHub API](https://api.github.com/orgs/getjerry) |
| Contact | hi@jerry.ai, press@jerry.ai, recruiting@jerry.ai; 833-445-3779 | [about](https://jerry.ai/about/), [news](https://jerry.ai/news/), [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

Awards the company lists on its own pages: Forbes and Statista America's Best Startup Employers (2021, 2022, 2024 and a 2026 listing linked from the newsroom), Y Combinator Top Companies, Comparably Best Company Culture, Top 50 Inspiring Workplaces, LinkedIn Top Startups 2021, and a Financial Technology Report Top 50 InsurTech CEOs placement ([about](https://jerry.ai/about/), [news](https://jerry.ai/news/)). Jerry's rank on the [2026 Forbes list](https://www.forbes.com/lists/americas-best-startup-employers/) was not retrieved on 2026-07-29.

### Identity and legal entities

| Name | Type | Role | Source |
|---|---|---|---|
| Jerry Services, Inc. | Parent corporation | Named as parent of the brokerage, as the App Store and Google Play developer, and as the owner of Propelix | [insurance licenses](https://jerry.ai/insurance-licenses/), [iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950), [Propelix Terms of Use](https://propelix.ai/terms) |
| Jerry Insurance Agency, LLC | Subsidiary | The licensed insurance producer; California is its resident state | [insurance licenses](https://jerry.ai/insurance-licenses/) |
| Jerry Offers Inc. | Affiliate | Named alongside the agency in the privacy policy; its function is not described | [privacy policy](https://jerry.ai/privacy-policy/) |
| ISU Insurance Agency Network | Third party | Named in the terms of use; the relationship is not explained on the page | [terms of use](https://jerry.ai/terms-of-use/) |
| `getjerry.com` | Legacy domain | Still active as an internal domain — Sentry, GrowthBook and the CTO's developer email all sit on it | [CSP header on jerry.ai](https://jerry.ai/), [Google Play listing](https://play.google.com/store/apps/details?id=com.jerrym) |

No corporate-registry record was retrieved; see `Notes`.

---

## Product

### Insurance — PriceProtect™

The [flow](https://jerry.ai/how-jerry-works/) is four steps: collect driver, vehicle and current-policy details with fields "pre-filled from public records"; return "up to 20 initial quotes"; buy in-app, with Jerry handling the paperwork and cancelling the prior policy; then monitor market rates and prompt a re-shop. Lines covered are [car](https://jerry.ai/car-insurance/), [homeowners](https://jerry.ai/home-insurance/), [renters](https://jerry.ai/renters-insurance/) and [motorcycle](https://jerry.ai/motorcycle-insurance/). Licensed agents are reachable 24/7 by chat, and by phone Monday–Friday 08:00–24:00 ET and weekends 08:00–18:30 ET ([FAQ](https://jerry.ai/faq/)).

### Car Care — GarageGuard™

[Free, and usable without a Jerry policy](https://jerry.ai/car-care/): service history and maintenance reminders built from year/make/model/mileage, VIN-based recall checks, plain-language diagnostics, repair quotes gathered from nearby shops within 24–48 hours, vehicle valuation, and document storage. Launched 2023 ([about](https://jerry.ai/about/)).

### Driver Safety — DriveShield™

[Phone-based telematics](https://jerry.ai/driver-safety/) with no hardware: trips are scored, points and weekly challenges feed state leaderboards, and users "qualify for insurance discounts with participating insurers". The page states driving data is shared with insurers only when it helps the rate and only with permission. Launched 2023 ([about](https://jerry.ai/about/)).

### Propelix

A separate B2B product: a prompt-management and virtual-agent platform for regulated businesses, offering prompt version control, testing and debugging against production logs, release monitoring, real-time data integration for personalized responses, and knowledge-base management ([propelix.ai](https://propelix.ai); Undated; accessed 2026-07-29). Its terms state it is "a product of Jerry Services, Inc." ([Propelix Terms of Use](https://propelix.ai/terms); Last Updated 2025-10-22). In an [April 2024 CIO interview](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html), Jerry COO John Spottiswood — described there as Propelix's President — calls it "essentially GitHub for AI-based virtual agents", says it lets teams build against OpenAI, Anthropic, Google and Mistral models across chat, voice, SMS and email, and states it was built "to solve a need that we had at Jerry".

### ChatGPT integration

In March 2026 Jerry announced repair-cost estimation and then car-insurance quoting inside the ChatGPT app, drawing on its repair-shop and carrier data ([Carrier Management, 2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm)). The article notes coverage is not bound inside ChatGPT; the transaction completes on Jerry's own surfaces.

### Commercialization

Jerry earns carrier commissions on policies purchased through it, the same model as a traditional broker, and states this does not raise the customer's price ([FAQ](https://jerry.ai/faq/)). "With select carriers in certain states, customers may incur an initial broker or origination fee", disclosed before purchase ([FAQ](https://jerry.ai/faq/), [how Jerry works](https://jerry.ai/how-jerry-works/)). Car Care and Driver Safety are free and do not require a Jerry policy. No public price list exists, because the consumer product has no price. Propelix publishes no pricing.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2019-01 | Mobile app launched | [about](https://jerry.ai/about/) |
| 2020 | 10x revenue growth during the year | [Jerry debuts, 2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-05-17 | Nearly 1 million customers; 45+ carriers compared in 45 seconds | [Jerry debuts, 2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-08-10 | 1M+ customers; $450M valuation | [Series C release, 2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/) |
| 2023-08-03 | 4 million U.S. customers | [Insurance Journal, 2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm) |
| Early 2024 | "became profitable in early 2024" | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 2024 | 5 million customers reached | [about](https://jerry.ai/about/) |
| 2025 | "68% year-over-year revenue growth in 2025 while maintaining profitability" | [LinkedIn](https://www.linkedin.com/company/jerryinc) |
| Accessed 2026-07-29 | "helped 1,192,562 drivers compare car insurance quotes from 100+ insurers" | [data methodology](https://jerry.ai/car-insurance-data-methodology/) |
| Accessed 2026-07-29 | iOS: 4.68 average from 29,828 US ratings, version 3.133.1 released 2026-07-21 | [iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950) |
| Accessed 2026-07-29 | Google Play: 1M+ downloads, updated 2026-07-17 | [Google Play](https://play.google.com/store/apps/details?id=com.jerrym) |
| Accessed 2026-07-29 | ">70% of inbound sales and service requests (over 50k chats per month)" automated | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

### Announced customers and partners

| Date | Party | Detail |
|---|---|---|
| [2021-12-01](https://jerry.ai/newsroom/jerry-partners-with-lyft-to-save-drivers-time-and-money-on-car-expenses/) | Lyft | Insurance comparison offered to Lyft drivers, rolled out first in Illinois and Pennsylvania |
| [2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm) | OpenAI | Repair-cost estimates and insurance quoting inside the ChatGPT app |
| [Accessed 2026-07-29](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html) | Unnamed insurance and lender partners | Propelix's stated initial customers; none named publicly |

### Stated plans

The clearest statements of direction sit in job descriptions rather than announcements ([jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai); accessed 2026-07-29):

- The stated goal is to "go from 5M to 50M customers and become a $10B business in the next 4 years".
- Expansion is "into adjacent verticals (e.g. home, motorcycle, RV, etc) to become the one-stop-shop for all your physical assets"; the YC profile frames the company as "building the AI agent to manage all your physical assets".
- Named next bets on the AI roadmap are "voicebot, computer use, consumer AI applications", none of which is described as shipped, plus consolidating prompts from six locations onto one platform.

---

## Founder

The three founders built [YourMechanic](https://jerry.ai/author/musawir-shah/) together and left it to incubate Jerry at Y Combinator in 2017 ([team](https://jerry.ai/team/)).

| Name | Role | Prior | Source |
|---|---|---|---|
| Art Agrawal | Co-Founder and CEO | Founded YourMechanic (2012 TechCrunch Disrupt winner), grew it to 2,000+ mechanics across 50 states; Drexel University | [team](https://jerry.ai/team/) |
| Musawir Shah | Co-Founder and CTO | VP Engineering at YourMechanic; senior software engineer at NVIDIA; doctorate in computer science, University of Central Florida | [team](https://jerry.ai/team/), [author bio](https://jerry.ai/author/musawir-shah/) |
| Lina Zhang | Co-Founder and VP Operations | Scaled YourMechanic from 5 to 50+ markets in a year; IP attorney at Morrison & Foerster; biochemistry researcher at Stanford; California State Bar | [team](https://jerry.ai/team/) |

Musawir Shah's [author bio](https://jerry.ai/author/musawir-shah/) states he "leads the Jerry software engineering team" and that at YourMechanic he was responsible for consumer-facing R&D, software architecture, stack evaluation and integration, and a team of engineers and UI/UX designers. His [GitHub account](https://github.com/musawirali) lists CTO at Jerry, Inc., Palo Alto; he is one of two public members of the [getjerry organisation](https://api.github.com/orgs/getjerry/public_members).

### Selected leadership

From the [team page](https://jerry.ai/team/) (Undated; accessed 2026-07-29), the leaders whose remit touches product, engineering, data or hiring:

| Name | Role | Prior |
|---|---|---|
| John Spottiswood | Chief Operating Officer; also President of Propelix | Match, LendingClub, QuinStreet, Inflection; Harvard MBA |
| Ed Chung | Chief Financial Officer | View Ridge Capital Management, Farallon Capital, Warburg Pincus; CFA |
| Josh Damico | VP Insurance Operations | Geico (sales, servicing, underwriting); manages 55+ carrier partnerships |
| MengHan Li | VP of Growth | McKinsey; Peking University; MIT |
| Armando La Rocca | VP Business Ops and Analytics | Better.com, Life House; Bocconi, Darden MBA |
| Haley Park | VP of People Operations | Windfall, Subsplash |
| Neima Shahidy | VP of Partnerships | Amazon Alexa go-to-market; Microsoft Surface |
| Journee Isip | VP of New Business | LinkedIn, Meta, BCG, Wells Fargo; Columbia physics, Chicago Booth MBA |
| Gillian Li | VP of Finance | Deloitte, Enuma; Fudan University; CFA |

The two Agentic AI product roles open on 2026-07-29 both report directly to the COO ([jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)). No engineering leader other than the CTO is named on any company surface.

---

## Funding

| Date | Round | Amount | Investors named | Cumulative | Source |
|---|---|---|---|---|---|
| 2018 | Series A | Not stated in the company release | Led by Bow Capital | — | [Jerry debuts, 2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-05-17 | Series B | $28M | Led by Goodwater Capital; angels including Jay Vijayan (Tekion), Jon McNeill (DVx Ventures), Brandon Krieg (Stash) | $57M | [Jerry debuts, 2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-08-10 | Series C | $75M at a $450M valuation | Led by Goodwater Capital; Bow Capital and Kamerra returning; Highland Capital Partners and Park West Asset Management new | $132M | [Series C release, 2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/) |
| 2023-08-03 | Series C2 | $110M in equity and debt | Equity led by Park West Asset Management, with Goodwater Capital, Highland Capital Partners and Plug and Play Ventures reinvesting; TriplePoint Capital led the debt facility and also invested in the equity | $242M | [Carrier Management, 2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm), [Insurance Journal, 2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm) |

The 2023 round is named Series C2 by the company and referred to as following its "C1" round, which retroactively renames the August 2021 Series C. No round has been announced since 2023-08-03, and no valuation has been disclosed since the $450M mark in 2021.

The [Series C release](https://jerry.ai/newsroom/jerry-series-c-funding/) states the money was for "additional automotive compare-and-buy marketplaces" — vehicle financing, repair, warranties, parking, maintenance. The C2 round was announced alongside the launch of GarageGuard and DriveShield ([Insurance Journal, 2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm)).

The company's [investors page](https://jerry.ai/investors/) lists 11 firms without attaching any of them to a round: Bow Capital, FundersClub, Goodwater Capital, Kamerra, Liquid2 Ventures, Oriza Ventures, Plug and Play, SV Angel, TriplePoint Capital, Y Combinator, Zillionize. It also names 27 individual investors, among them Joe Montana (Liquid2 Ventures), Jon McNeill (DVx Ventures), Joshua Buckley (Product Hunt), Immad Akhund (Mercury) and Michael Vaughn (formerly Venmo). Oriza Ventures and SV Angel appear only on that page, never in a round announcement.

---

## Engineering

### Technology stack and platforms

Confirmed from public assets — HTTP response headers and the Content-Security-Policy on `jerry.ai`, the GitHub organisation, and packages published to npm (all accessed 2026-07-29):

| Item | Detail | Evidence |
|---|---|---|
| API gateway | Kong 3.9.3, behind nginx; `x-kong-request-id` and `x-kong-upstream-latency` on every response | [response headers](https://jerry.ai/) |
| Gateway work in progress | Forks of `kong` and `kubernetes-ingress-controller` created 2026-06-08 | [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| Cloud | AWS — CloudFront in front of everything, S3 (`us-west-2`) serving the web app, `jerry-uploads-prod` S3 bucket for media | [response headers](https://jerry.ai/), [CSP on jerry.ai](https://jerry.ai/) |
| Serverless Next.js | `@getjerry/lambda-at-edge`, `@getjerry/next-aws-lambda`, `@getjerry/s3-static-assets`, `@getjerry/cloudfront`, plus `terraform-next` — Next.js deployed to Lambda@Edge and S3 via Terraform | [npm registry](https://registry.npmjs.org/-/v1/search?text=getjerry), [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| Backend framework | NestJS — `nest-casl`, an original getjerry package (301 stars) providing CASL authorization for NestJS with `@nestjs/graphql` as a peer dependency | [nest-casl](https://github.com/getjerry/nest-casl) |
| Frontend and tooling | React; `@getjerry/eslint-config` (ESLint 9, `@typescript-eslint`, airbnb, `eslint-plugin-react`), `@getjerry/tsconfig`, `@getjerry/prettier-config`, and `@getjerry/oxfmt-config` (oxfmt ≥ 0.42), all published 2026-07-09 | [npm registry](https://registry.npmjs.org/-/v1/search?text=getjerry) |
| Streaming | Fork of Confluent Platform Helm charts (Kafka on Kubernetes) | [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| Error tracking | Self-hosted Sentry at `sentry.ing.getjerry.com` | [jerry.ai homepage](https://jerry.ai/) |
| Observability | Datadog browser RUM (`datadoghq-browser-agent`, `browser-intake-datadoghq.com`) | [CSP on jerry.ai](https://jerry.ai/) |
| Feature flags / experiments | GrowthBook, self-hosted at `growthbook-api.getjerry.app` | [CSP on jerry.ai](https://jerry.ai/) |
| CMS | Contentful (`images.ctfassets.net`) for product-surface content; WordPress 7.0.2 with W3 Total Cache for the marketing site | [CSP on jerry.ai](https://jerry.ai/), [jerry.ai homepage](https://jerry.ai/) |
| Third-party APIs | Google Maps and Places APIs; Stripe (React Native bindings forked in 2022) | [CSP on jerry.ai](https://jerry.ai/), [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| Analytics and product tooling | Hotjar, Google Analytics / Tag Manager, Google Site Kit, Podscribe, TikTok and Google ads pixels | [CSP on jerry.ai](https://jerry.ai/) |
| Delivery workflow | GitHub Actions — original getjerry actions for S3 caching, Slack build notifications, Asana integration and release tagging; Asana and Slack are therefore in use | [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| Status page | Upptime on GitHub Actions at `status.jerry.ai`, monitoring exactly two endpoints: the homepage and `jerry.ai/health`, labelled "Insurance System" | [.upptimerc.yml](https://github.com/getjerry/upptime) |
| Data team tools | "SQL (Clickhouse), Metabase, Python, Jupyter Hub, GitHub" — stated verbatim in every open Data role | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

The following come from **closed** engineering postings and are hiring evidence for the period stated, not confirmation of current production use:

| Item | Detail | Where it appears |
|---|---|---|
| Frontend | React, React Native | Toronto new-grad posting, removed [2025-11-24](https://builtintoronto.com/job/software-engineer-entry/7776678) |
| Backend | Node.js + TypeScript, Go, Python | same |
| Infrastructure | AWS, Docker, CI/CD | same |
| Data stores | Redis, Postgres, DynamoDB, ClickHouse | same |
| AI/ML | "Python pipelines, LLM integrations, internal models" | same |
| Propelix engineering | JavaScript, React, Node.js; "prior knowledge not required" | Senior Full Stack Engineer (Toronto), removed [2025-08-04](https://builtin.com/job/senior-full-stack-engineer/4456345) |

The AI platform itself is named in two currently open Product roles ([jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai); accessed 2026-07-29). The posting asks candidates to learn "how our various tech stacks (e.g. Propelix, Botly, CRM, GitHub, and Replit) interact". **Botly** appears only in these postings; no public documentation of it was found. OpenAI is named as a partner in five open roles, and the [LinkedIn About](https://www.linkedin.com/company/jerryinc) claims the company is "processing billions of tokens through OpenAI's API". Propelix's own materials describe supporting OpenAI, Anthropic, Google and Mistral models ([CIO, 2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)).

### Systems

| System | What it does | Source |
|---|---|---|
| Quote and comparison engine | Pre-fills applicant data from public records, returns up to 20 quotes across 100+ carriers, recalculates as coverage and deductibles are adjusted, then confirms against carrier underwriting | [how Jerry works](https://jerry.ai/how-jerry-works/) |
| Policy switching and cancellation | Completes purchase, files paperwork, cancels the prior policy | [how Jerry works](https://jerry.ai/how-jerry-works/) |
| Rate-monitoring / re-shop trigger | Watches market rates over time and alerts the customer when to re-shop | [how Jerry works](https://jerry.ai/how-jerry-works/) |
| Phone-based telematics | Trip capture from smartphone sensors, drive scoring, points, weekly challenges, state leaderboards, permissioned sharing with carriers | [driver safety](https://jerry.ai/driver-safety/) |
| Repair marketplace | Collects competing repair estimates from nearby shops, typically within 24–48 hours; publishes fair-price estimates | [car care](https://jerry.ai/car-care/) |
| VIN services | Recall lookups and mileage-based maintenance schedules | [car care](https://jerry.ai/car-care/) |
| Quote data warehouse and content pipeline | A proprietary quote database used for rate analysis with 12–18-month rolling windows, cross-validated against NAIC and BLS, anonymized, then published to content pages refreshed up to once a day | [data methodology](https://jerry.ai/car-insurance-data-methodology/) |
| Virtual agent platform (Propelix) | Multi-model prompt management, versioning, testing against production logs, knowledge bases, and agent deployment across chat, voice, SMS and email | [propelix.ai](https://propelix.ai), [CIO, 2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html) |
| Sales and service automation | Automates ">70% of inbound sales and service requests (over 50k chats per month)"; also drives vehicle photo validation and back-office automation | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| ChatGPT app | Repair-cost estimation and insurance quoting surfaced inside ChatGPT; binding happens off-platform | [Carrier Management, 2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm) |

The postings describe the AI platform's condition candidly: it was built "before off-the-shelf platforms existed", "the underlying technology is entirely homegrown", and prompts "now live across six separate locations. There is no single source of truth, no unified platform, and no clear owner" ([jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)).

### Technical background sought

No engineering role is open as of 2026-07-29, so the requirements below come from the closed engineering postings and the open technical Product and Data roles.

- **Software engineering, entry (Toronto, closed 2025-11-24):** a CS or engineering bachelor's degree; internship, co-op or side-project experience preferred but not required; new engineers are placed in "engineering pods" covering core app, retention or automation.
- **Software engineering, senior (Propelix, Toronto, closed 2025-08-04):** 5+ years; proficiency across several languages; comfort in client-facing conversations, since the role included onboarding insurance customers onto the platform; a record of shipping fast; high-growth startup experience preferred.
- **Technical Product Management, AI (open):** 4+ years "in a technical role like forward deployed engineering, technical product management, or similar at a fast-paced startup"; prior work designing prompt strategies, evaluation frameworks and guardrails while trading off latency, cost and accuracy; comfort with API design and system architecture; SQL.
- **Data Science and BizOps (open):** 6+ years "at a consulting firm, investment bank, or high-growth technology company". The postings state the team of 14 is drawn from "former McKinsey, BCG and Bain consultants", and the work is described as embedded analytics — defining metrics, running experiments and driving decisions — rather than modelling or data engineering.

### Industry domain

- **Property and casualty insurance distribution.** The business is a licensed brokerage in all 50 states; commissions, broker/origination fees, carrier appetite and underwriting confirmation shape the product ([insurance licenses](https://jerry.ai/insurance-licenses/), [FAQ](https://jerry.ai/faq/)).
- **Consumer data regulation.** The [privacy policy](https://jerry.ai/privacy-policy/) covers SSNs, driver's licences, credit scores, claims history, VINs and "realtime driving and geolocation information", and addresses "profiling in furtherance of decisions that produce legal or similarly significant effects" for certain state residents.
- **Regulated-industry AI.** Propelix is positioned explicitly for "regulated businesses", and Jerry's own agents operate in insurance sales and service ([propelix.ai](https://propelix.ai)).
- Insurance domain knowledge is **required** for the insurance-operations roles, and is **not** stated as a requirement in the engineering, data or AI-product postings.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Open roles | 47 as of 2026-07-29: Insurance 15, Data 13, Marketing 10, Product 7, Business Development 2. No Engineering department | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Job board | Ashby, at `jobs.ashbyhq.com/Jerry.ai`; `jerry.ai/job-openings` renders from it | [job openings](https://jerry.ai/job-openings/) |
| Location and office policy | Postings say "fully remote with offices in Palo Alto, New York, Chicago, and Toronto"; every non-remote role also lists Chicago, Boston and the SF Bay Area as options. The Toronto engineering listing was marked in-office | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai), [Built In Toronto](https://builtintoronto.com/job/software-engineer-entry/7776678) |
| Hiring geography limits | Salaried employees only in AZ, CA, CO, FL, GA, IL, MA, NC, NJ, NV, NY, OR, TN, TX, UT, VA and Ontario, Canada; hourly only in AZ, FL, GA, NV, NY, NC, TN, TX, UT, VA | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Published salary — Data | Associate $85k–$130k; Data Scientist $130k–$150k; Senior $150k–$170k; Staff and Senior Manager $170k–$210k; Manager $150k–$170k; PM Growth $110k–$150k | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Published salary — Product (AI) | Technical PM $130k–$170k; Senior Technical PM, Senior PM, Product Owner and Senior Manager $160k–$210k | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Published salary — other | Marketing $75k–$190k; Business Development directors $180k–$220k; insurance sales and service $19–$21 per hour | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Equity | Listed as a compensation component on every posting; levels.fyi reports a standard 4-year schedule vesting 25% per year | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai), [levels.fyi](https://www.levels.fyi/companies/jerry/salaries) |
| Reported engineering compensation | levels.fyi median total compensation $150k for Software Engineer, $130,773 across all roles; updated 2026-07-28 | [levels.fyi](https://www.levels.fyi/companies/jerry/salaries) |
| Benefits | Health, dental and vision; PTO; paid parental leave; 401(k) with employer matching; wellness benefits. Part-time, contract and freelance roles may not qualify | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| New graduates | Explicitly considered for engineering when those roles were open — the Toronto listing required no prior experience. No open role today is scoped to new graduates | [Built In Toronto](https://builtintoronto.com/job/software-engineer-entry/7776678) |
| Stated values | "Truth Seeking", "Sense of Urgency", "Pursuit of Excellence"; "full ownership over what you do" | [careers](https://jerry.ai/careers/) |
| Stated working style | "No slides", "No corporate fluff", "no bloat, unnecessary meetings, or waiting for approvals"; "a flat org chart"; leveling described as flexible — "You may see job ads for this role at different job levels" | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Application handling | "due to the volume of applications we receive, only applicants under consideration will be contacted"; accommodations via recruiting@jerry.ai | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| Visa sponsorship, turnover, interview process | Not published | [jobs API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): `jerry.ai` and every page in its [sitemap index](https://jerry.ai/sitemap_index.xml) — 51 pages plus the newsroom, page and post sitemaps; `robots.txt`; direct probes of `/security`, `/trust`, `/soc2`, `/engineering`, `/blog`, `/tech`, `/data-security` and `/compliance`, and of the `eng`, `engineering`, `blog`, `tech`, `api`, `docs` and `developers` subdomains; the Ashby job board API and all 47 role records; the `getjerry` GitHub organisation via the REST API, all 32 repositories, the public-members list and the upptime configuration; npm packages published under `@getjerry`; the App Store and Google Play listings; `propelix.ai` and its terms page; the YC, Built In, LinkedIn, levels.fyi and Wikipedia profiles; the company newsroom and its distribution on PR Newswire; and searches in English for Jerry funding, litigation, engineering hiring, Propelix and Botly.

- **No engineering blog, technical writing, or architecture material of any kind.** The only author page with technical content is the CTO's bio; every `/blog`, `/engineering` and `/tech` path and subdomain returns nothing.
- **No security page, trust centre, subprocessor list, or named certification.** No SOC 2, ISO 27001 or equivalent is claimed anywhere on the site. The consumer-facing claims are "bank-level encryption" and the DataLock™ Guarantee, which is a marketing-contact promise rather than a security control ([how Jerry works](https://jerry.ai/how-jerry-works/), [FAQ](https://jerry.ai/faq/)).
- **No public API or developer documentation.** `api.jerry.ai`, `docs.jerry.ai` and `developers.jerry.ai` do not resolve.
- **No engineering role is open**, and the previously indexed Ashby engineering postings now return null from the job-posting API. Whether this reflects a hiring pause, a freeze, or timing is not determinable from public sources.
- **The company does not publish a headcount.** Three third-party figures disagree; see below.
- **No corporate-registry record was retrieved.** The California Secretary of State business search and OpenCorporates both blocked automated access on 2026-07-29, so "Jerry Services, Inc." and "Jerry Insurance Agency, LLC" were not verified against a register; the entity names and their parent/subsidiary relationship come from the company's own legal pages.
- **No valuation since August 2021**, and no funding round since August 2023. Profitability, the 70X revenue figure and the 68% 2025 growth figure are company statements in recruitment copy and on LinkedIn, with no filing, audit or investor confirmation found.
- **Which investor joined which round is not stated** for the seed or Series A; the [investors page](https://jerry.ai/investors/) is an unattributed list, and Oriza Ventures and SV Angel appear nowhere else.
- **Propelix publishes no pricing, no named customer, no documentation and no technical detail** beyond a landing page and a terms page; it has no about page, robots.txt or sitemap.
- **No litigation involving Jerry was found.** A 2026 TCPA class action that surfaces in searches for insurance-brokerage suits names [InsureMe, Inc.](https://natlawreview.com/article/painful-premium-insurance-brokerage-firm-hit-class-action-lawsuit-alleging), not Jerry.
- **No interview or conference talk by the CTO was found.** The public technical voice of the company is the COO, who presented the customer-service AI results at Generative AI World 2023 ([GAI Insights](https://gaiinsights.com/blog/jerry-case-study-for-customer-service-saving-over-4m-a-year)).

### Inconsistencies across sources

- **Headcount:** 225 ([YC profile](https://www.ycombinator.com/companies/jerry-inc)), 296 ([Built In](https://builtin.com/company/jerry)), 201–500 with 402 profiles ([LinkedIn](https://www.linkedin.com/company/jerryinc)), 186 as of 2021 ([Wikipedia](https://en.wikipedia.org/wiki/Jerry_%28company%29)). All are undated or self-reported.
- **Offices:** job postings say Palo Alto, New York, Chicago, Toronto; [LinkedIn](https://www.linkedin.com/company/jerryinc) says Silicon Valley plus Toronto and Buffalo with remote staff in four countries; [Built In](https://builtin.com/company/jerry) says Palo Alto, Buffalo, Toronto and Lockport, Illinois; [Wikipedia](https://en.wikipedia.org/wiki/Jerry_%28company%29) says Lockport, New York. No two agree.
- **Remote policy:** 2026 postings say "fully remote"; the 2025 Toronto engineering listing was marked in-office ([Built In Toronto](https://builtintoronto.com/job/software-engineer-entry/7776678)).
- **Carrier count:** "100+ insurers" on the [site](https://jerry.ai/how-jerry-works/); "up to 50 insurers" in the [App Store description](https://itunes.apple.com/lookup?id=1258315950); "55+ carriers" on [Built In](https://builtin.com/company/jerry); "over 45 carriers" in the [2021 release](https://jerry.ai/newsroom/jerry-debuts/).
- **Revenue growth:** "scaled revenue 70X" in July 2026 postings; "60x revenue growth over 5 years" in the November 2025 Toronto posting; "68% year-over-year revenue growth in 2025" on [LinkedIn](https://www.linkedin.com/company/jerryinc). The three are not stated over the same baseline or period.
- **Customer savings:** "$800 per year" in the [2021 releases](https://jerry.ai/newsroom/jerry-series-c-funding/); "over $1,000/year" in the 2025 Toronto posting; "an average of $3,979 per year" on the current [how-it-works page](https://jerry.ai/how-jerry-works/), which qualifies it to customers with clean records who found savings in the past 12 months.
- **Automation rate:** "93 to 94% of all inbound conversations being responded to by virtual agents" without escalation ([CIO, 2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)); ">70% of inbound sales and service requests (over 50k chats per month)" in the 2026 postings. The units differ — conversations against requests, and 50k chats a month against the 200,000+ messages a month cited in [2023](https://gaiinsights.com/blog/jerry-case-study-for-customer-service-saving-over-4m-a-year) — so the two are not directly comparable and neither supersedes the other cleanly.
- **App Store rating:** the [reviews page](https://jerry.ai/reviews/) says 4.7 from "16.4k+ reviews"; the [iTunes API](https://itunes.apple.com/lookup?id=1258315950) returns 4.68 from 29,828 US ratings; the [homepage](https://jerry.ai/) cites "4M+ downloads". Ratings, reviews and downloads are different measures and the pages do not distinguish them.
- **Round naming:** the August 2021 round was announced as [Series C](https://jerry.ai/newsroom/jerry-series-c-funding/) and is called "C1" in the [2023 C2 coverage](https://www.carriermanagement.com/features/2023/08/03/251512.htm).

### Other

- **The internal AI platform became a product.** Propelix is sold to third parties as a product of Jerry Services, Inc., with Jerry's COO as its President, while Jerry's own consumer business remains an insurance brokerage. An engineer joining the AI track may be working on either.
- **The Series C2 was never published on Jerry's own newsroom.** The [newsroom sitemap](https://jerry.ai/newsroom-sitemap.xml) contains no 2023 funding release; the round is documented only through trade press.
- **Hiring is weighted entirely away from engineering.** 15 of 47 open roles are hourly insurance sales and service positions at $19–$21/hour, 13 are analytics roles requiring consulting or banking backgrounds, and 10 are SEO/AEO content and community marketing. The published ranges put the analytics and AI-product bands ($160k–$210k) above the levels.fyi software-engineer median ($150k).
- **The AI product roles are unusually candid about technical debt** — six prompt locations, no source of truth, no unified platform, no clear owner — which is more architectural detail than the company publishes anywhere else.
- **The published web surface is largely SEO machinery.** The sitemap index carries separate car-insurance, car-repair, reviews and local sitemaps alongside a documented [content methodology](https://jerry.ai/car-insurance-data-methodology/) that refreshes pages up to daily from the quote database; ten of the open marketing roles are SEO, AEO, community and organic growth.
- **The status page monitors two URLs.** `status.jerry.ai` checks the homepage and a single `/health` endpoint labelled "Insurance System" ([.upptimerc.yml](https://github.com/getjerry/upptime)) — it is not a service-level status page.
- **Most of the GitHub organisation is forks.** Of 32 public repositories, roughly two-thirds are forks of upstream projects; the substantive original work is `nest-casl` and a set of internal GitHub Actions. The npm config packages, republished on 2026-07-09, are the most current public signal of the front-end toolchain.
- **The company operates two brand domains.** `getjerry.com` remains in the CSP and hosts internal services (Sentry, GrowthBook), and the CTO's Google Play developer contact is a `getjerry.com` address ([Google Play](https://play.google.com/store/apps/details?id=com.jerrym)).

---

## Resources

**Official**

- [Jerry — jerry.ai](https://jerry.ai/)
- [About](https://jerry.ai/about/) · [Team](https://jerry.ai/team/) · [Investors](https://jerry.ai/investors/) · [FAQ](https://jerry.ai/faq/)
- [How Jerry works](https://jerry.ai/how-jerry-works/) · [Car care](https://jerry.ai/car-care/) · [Driver safety](https://jerry.ai/driver-safety/) · [Reviews](https://jerry.ai/reviews/)
- Insurance lines: [car](https://jerry.ai/car-insurance/) · [home](https://jerry.ai/home-insurance/) · [renters](https://jerry.ai/renters-insurance/) · [motorcycle](https://jerry.ai/motorcycle-insurance/)
- [Car insurance data methodology](https://jerry.ai/car-insurance-data-methodology/)
- [Careers](https://jerry.ai/careers/) · [Job openings](https://jerry.ai/job-openings/) · [Ashby jobs API — the 47 role records the page renders from](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)
- [Insurance licenses](https://jerry.ai/insurance-licenses/) · [Terms of use](https://jerry.ai/terms-of-use/) · [Privacy policy](https://jerry.ai/privacy-policy/)
- [Newsroom](https://jerry.ai/news/) · [Newsroom sitemap](https://jerry.ai/newsroom-sitemap.xml) · [Sitemap index](https://jerry.ai/sitemap_index.xml)
- [Musawir Shah — author bio](https://jerry.ai/author/musawir-shah/)
- [Propelix](https://propelix.ai) · [Propelix Terms of Use](https://propelix.ai/terms)
- [Status page configuration — getjerry/upptime](https://github.com/getjerry/upptime)
- [GitHub organisation — getjerry](https://github.com/getjerry) · [org API](https://api.github.com/orgs/getjerry) · [repositories API](https://api.github.com/orgs/getjerry/repos) · [public members API](https://api.github.com/orgs/getjerry/public_members)
- [nest-casl](https://github.com/getjerry/nest-casl) · [npm packages published by getjerry](https://registry.npmjs.org/-/v1/search?text=getjerry)
- [Musawir Shah — GitHub](https://github.com/musawirali)
- [LinkedIn](https://www.linkedin.com/company/jerryinc)
- [App Store listing metadata — iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950) · [Google Play](https://play.google.com/store/apps/details?id=com.jerrym)

**Press releases**

- [Jerry 2026 State of the American Driver Report — 2026-07-01](https://jerry.ai/studies/2026-state-of-the-american-driver-report/)
- [Jerry partners with Lyft — 2021-12-01](https://jerry.ai/newsroom/jerry-partners-with-lyft-to-save-drivers-time-and-money-on-car-expenses/)
- [AI-based car ownership super app Jerry secures $75 million Series C financing at $450 million valuation — 2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/)
- [Jerry debuts with $57 million in total funding — 2021-05-17](https://jerry.ai/newsroom/jerry-debuts/)

**Third-party coverage and profiles**

- [Carrier Management — Jerry brings AI-powered insurance to ChatGPT, 2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm)
- [CIO — Propelix lets companies easily build their own generative AI chatbots, 2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)
- [Carrier Management — Car insurance savings app Jerry announces $110M C2 funding round, 2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm)
- [Insurance Journal — Car app Jerry in California gets $110M in funding, adds services, 2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm)
- [GAI Insights — customer service case study, Generative AI World 2023](https://gaiinsights.com/blog/jerry-case-study-for-customer-service-saving-over-4m-a-year)
- [TechCrunch — Jerry raises $75M at a $450M valuation, 2021-08-10](https://techcrunch.com/2021/08/10/jerry-raises-75m-at-a-450m-valuation/)
- [Y Combinator company profile](https://www.ycombinator.com/companies/jerry-inc)
- [Built In — company profile](https://builtin.com/company/jerry) · [Built In Toronto — Software Engineer (entry), removed 2025-11-24](https://builtintoronto.com/job/software-engineer-entry/7776678) · [Built In — Senior Full Stack Engineer (Propelix), removed 2025-08-04](https://builtin.com/job/senior-full-stack-engineer/4456345)
- [levels.fyi — Jerry salaries](https://www.levels.fyi/companies/jerry/salaries)
- [Wikipedia — Jerry (company)](https://en.wikipedia.org/wiki/Jerry_%28company%29)
- [Forbes — America's Best Startup Employers](https://www.forbes.com/lists/americas-best-startup-employers/)
- [National Law Review — TCPA class action naming InsureMe, Inc., listed to prevent misattribution](https://natlawreview.com/article/painful-premium-insurance-brokerage-firm-hit-class-action-lawsuit-alleging)
