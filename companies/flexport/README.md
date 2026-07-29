# Flexport

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Flexport, Inc. is a San Francisco company founded in 2013. It is a licensed freight forwarder and customs broker that operates its own software platform: clients book ocean, air and trucking freight, clear customs, and track shipments through [flexport.com](https://www.flexport.com/) and a public REST API. Since 2023 it also runs the ecommerce fulfilment business it acquired from Shopify.

- Current job postings state that companies move "more than $19B of merchandise across 112 countries a year" on Flexport ([posting, updated 2026-07-09](https://job-boards.greenhouse.io/flexport/jobs/7819181)).
- About $2.5B raised across ten rounds; the last priced round was a $935M Series E in [February 2022](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/) at an $8B valuation ([Crunchbase](https://www.crunchbase.com/funding_round/flexport-series-e--3590ef78)).
- Shopify holds roughly 17% fully diluted. Its equity-method carrying value was $602M at 2025-12-31, and its share of Flexport's loss narrowed to $40M in FY2025 from $138M in FY2024 ([Shopify 10-K, filed 2026-02-11](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)).
- A current posting describes the stack as "coming from a React/Flow + Ruby on Rails monolith, and moving to React/Typescript, Kotlin Microservices on Kubernetes" ([Senior Software Engineer, Customs, updated 2026-07-10](https://job-boards.greenhouse.io/flexport/jobs/8000000)). US postings publish base salary bands.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | Flexport, Inc. | [Shopify 10-K, filed 2026-02-11](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| Founded | 2013 | [Wikipedia](https://en.wikipedia.org/wiki/Flexport); Undated; accessed 2026-07-29 |
| HQ | Phelan Building, San Francisco, California | [Wikipedia](https://en.wikipedia.org/wiki/Flexport); Undated; accessed 2026-07-29 |
| CEO and co-founder | Ryan Petersen | [Convoy sale post, 2025-07-28](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/) |
| Engineering headcount | "More than 400 software engineers" | [about page](https://www.flexport.com/company/about-us/); Undated; accessed 2026-07-29 |
| Total headcount | ~2,100 (2025) — third-party figure, not company-published | [Wikipedia](https://en.wikipedia.org/wiki/Flexport); accessed 2026-07-29 |
| Reach | 112 countries | [about page](https://www.flexport.com/company/about-us/), [posting, 2026-07-09](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| Open roles | 151 total, 18 engineering-adjacent | [Greenhouse job board API](https://boards-api.greenhouse.io/v1/boards/flexport/jobs); as of 2026-07-29 |
| Engineering locations | San Francisco, Amsterdam, Atlanta, Shanghai, Beijing, Shenzhen | [Greenhouse job board](https://job-boards.greenhouse.io/flexport); as of 2026-07-29 |
| Investors | Y Combinator, First Round Capital, Founders Fund, Google Ventures, DST Global, SoftBank Vision Fund, Andreessen Horowitz, MSD Partners, Shopify | [Series E release, 2022-02-07](https://www.businesswire.com/news/home/20220207005279/en/Flexport-Announces-935-Million-in-Funding-to-Advance-Resiliency-and-Visibility-in-Global-Supply-Chain), [Wikipedia](https://en.wikipedia.org/wiki/Flexport) |

### Regulated entities

Flexport is not only a software company; the regulated licences are what let it act as principal in the shipment. Stated in its own [terms](https://www.flexport.com/terms-and-conditions/) (accessed 2026-07-29):

| Entity | Role | Licence as stated |
|---|---|---|
| Flexport International LLC | International ocean freight forwarding | Licensed Ocean Transportation Intermediary, FMC# 025219NF |
| Flexport Customs LLC | US customs brokerage | Licensed customs broker with a national permit |

These are the company's own statements. They were not cross-checked against the [FMC's public OTI register](https://www.fmc.gov/about/bureaus-offices/bureau-of-enforcement-investigations-and-compliance-beic/office-of-compliance/ocean-transportation-intermediaries/) or CBP records in this pass; an attempted lookup on the FMC search endpoint returned an error on 2026-07-29.

### Market context as stated by the company

- Global trade is described as "a $10T industry" and, in older posting text, as "an industry that comprises 12% of the global GDP" ([postings, 2026-07](https://job-boards.greenhouse.io/flexport/jobs/7978127)).
- The CEO describes the industry's manual work — "people passing PDFs and moving data between enterprise systems" — as the target for AI agents ([Dealroom note](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot); accessed 2026-07-29).

---

## Product

### Service lines

Ocean freight, air freight, trucking, customs brokerage, B2B and ecommerce fulfilment, returns, cargo insurance, trade finance ("Capital"), duty drawback, product classification, trade advisory, and emissions reporting — each has its own page under [flexport.com/products](https://www.flexport.com/products/flexport-platform/).

### Platform and developer surface

- [Flexport Platform](https://www.flexport.com/products/flexport-platform/), [Control Tower](https://www.flexport.com/technology/control-tower/), [Customs Suite](https://www.flexport.com/technology/customs-suite/), and [Flexport Intelligence](https://www.flexport.com/technology/flexport-intelligence/) for booking, visibility, customs and analytics.
- [Atlas](https://atlas.flexport.com/) — a public interactive view of global ocean freight with vessel, port and route data.
- A public [REST API](https://apidocs.flexport.com/) with v1/v2/v3 versioning, webhooks for milestone events, pagination and a changelog, covering shipments, containers, purchase orders, bookings, customs entries, invoices, products, and network resources. EDI documentation is published alongside it at [developers.flexport.com](https://developers.flexport.com/faq/general/).

Product releases are published on a seasonal cadence: the [Winter 2025 release](https://www.prnewswire.com/news-releases/flexport-unveils-20-tech-and-ai-powered-products-to-modernize-global-supply-chains-302383593.html) (2025-02-24) announced 20+ products including Flexport Intelligence and Control Tower; the [Winter 2026 release](https://www.flexport.com/technology/product-release/winter-2026/) adds Atlas, a customs-broker audit tool, a tariff refund calculator, an AI consolidation engine for container utilisation, digital routing guides, AI search and translation, and NetSuite and TikTok Shop integrations.

### Commercialization

Revenue is transactional rather than subscription: clients pay for freight moved and services performed, so the meaningful figure is net revenue (gross revenue minus the cost of the transportation bought), not gross revenue. No public price list exists; the platform quotes rates per shipment through [flexport.com/rates](https://www.flexport.com/rates/). Fulfilment, customs brokerage, insurance and trade finance are separately priced services.

### Reported scale over time

| Period | Reported figure | Source |
|---|---|---|
| 2021 | $3.3B revenue; first profitable year, $37M net income | [Sacra](https://sacra.com/c/flexport/); accessed 2026-07-29 |
| 2022 | ~$4.1B revenue (post-COVID peak) | [Sacra](https://sacra.com/c/flexport/) |
| 2023 | $1.6B revenue | [Sacra](https://sacra.com/c/flexport/) |
| 2024 | $2.1B revenue | [Sacra](https://sacra.com/c/flexport/) |
| FY2024 | Shopify's share of Flexport's loss: $138M | [Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| FY2025 | Shopify's share of Flexport's loss: $40M; Shopify's equity-method carrying value $602M (2024: $642M) and convertible notes fair value $326M (2024: $291M) | [Shopify 10-K, filed 2026-02-11](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| 2025 | ~$450M net revenue, up from ~$350M; profitable in 2025 only because of the Convoy Platform sale | [Dealroom note](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot), [Sacra](https://sacra.com/c/flexport/) |
| 2026 target | ~$600M net revenue and organic profitability | [Dealroom note](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot) |

### Acquisitions and divestitures

| Date | Event | Detail |
|---|---|---|
| 2023-05 | Acquired Shopify Logistics, including Deliverr | Consideration was a 13% equity interest in Flexport on a fully diluted basis, inclusive of warrants and options ([Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)) |
| 2023-11 | Acquired the assets of Convoy, a shut-down digital freight brokerage | Reported at ~$16M ([FreightWaves](https://www.freightwaves.com/news/less-than-2-years-after-flexport-bought-convoys-tech-stack-its-being-sold-to-dat)) |
| 2025-07-28 | Sold the Convoy Platform to DAT Freight & Analytics | Reported at ~$250M ([GeekWire](https://www.geekwire.com/2025/flexport-is-selling-convoys-technology-to-freight-giant-dat/)); Flexport kept the digital brokerage business built on it and said the platform "needed to be a neutral infrastructure layer" ([company post, 2025-07-28](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)) |

### Stated plans

The CEO describes roughly 100 costly core workflows targeted for AI agents, five of them already live and saving money, with about 80% of the remainder needed in 2026 to justify the spend, alongside a positioning shift toward cost leadership ([Dealroom note](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot); accessed 2026-07-29). Job postings describe a new San Francisco "Autonomous Freight Systems" team building AI-driven rates and self-serve booking so that clients "commit freight on technology alone, with no account executive and no operations touch" ([posting, 2026-07-09](https://job-boards.greenhouse.io/flexport/jobs/7819181)).

---

## Founder

**Ryan Petersen** — co-founder and CEO. Flexport went through Y Combinator and raised from Founders Fund, First Round Capital and Google Ventures in its early rounds ([Wikipedia](https://en.wikipedia.org/wiki/Flexport); accessed 2026-07-29). He handed the CEO role to Dave Clark, previously Amazon's consumer chief, in 2022, and resumed it in September 2023 after Clark resigned ([Wikipedia](https://en.wikipedia.org/wiki/Flexport)). He writes the company's strategic posts, including the [Convoy Platform sale rationale (2025-07-28)](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/).

**David Petersen** — named as a co-founder alongside Ryan on [Wikipedia](https://en.wikipedia.org/wiki/Flexport); most company material names only Ryan Petersen. No current role at Flexport was found in the sources reviewed.

No leadership or team page listing current executives was found on flexport.com as of 2026-07-29.

---

## Funding

| Date | Round | Amount | Investors | Source |
|---|---|---|---|---|
| 2013–2017 | Seed through Series C | $304M cumulative, including a $110M Series C | Founders Fund, First Round Capital, Google Ventures | [Wikipedia](https://en.wikipedia.org/wiki/Flexport) |
| 2019-02 | Series D | $1B | SoftBank Vision Fund (lead) | [company blog](https://www.flexport.com/blog/flexport-secures-usd1-billion-in-funding-led-by-softbank-vision-fund/) |
| 2022-02-07 | Series E | $935M at an $8B valuation | Andreessen Horowitz and MSD Partners (co-leads), with Shopify, DST Global, Founders Fund, SoftBank Vision Fund | [company blog](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/), [Business Wire](https://www.businesswire.com/news/home/20220207005279/en/Flexport-Announces-935-Million-in-Funding-to-Advance-Resiliency-and-Visibility-in-Global-Supply-Chain) |
| 2023-05 | Equity issued for the Shopify Logistics acquisition | 13% fully diluted equity interest | Shopify | [Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| 2023-12 | Convertible notes | $260M | Shopify | [Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |

Total raised is reported as about $2.5B across ten rounds ([Tracxn](https://tracxn.com/d/companies/flexport/__MY-G7JqqdTHK8-1y1arkCLJEJeVwbwMgeQLTcMS4Izk/funding-and-investors); accessed 2026-07-29). Shopify's stake is roughly 17% on a fully diluted basis including warrants and options, and it also holds a commercial agreement and a co-marketing agreement with Flexport, under which Shopify recognised $9M of expense in FY2025 and $4M in FY2024 and nil revenue share in FY2025 ([Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)).

---

## Engineering

### Technology stack and platforms

From current postings on the company's own board, dated 2026-07:

| Layer | Detail | Evidence class |
|---|---|---|
| Application | "Coming from a React/Flow + Ruby on Rails monolith, and moving to React/Typescript, Kotlin Microservices on Kubernetes" | Confirmed by [posting, 2026-07-10](https://job-boards.greenhouse.io/flexport/jobs/8000000) |
| Backend | Java, Spring Boot, Ruby on Rails; "our platform is built with Ruby" | Stated as the team's stack in [postings](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| Frontend | React, TypeScript, Next.js | [postings](https://job-boards.greenhouse.io/flexport/jobs/7311835) |
| Cloud | AWS | [postings](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| Build and CI | Buildkit, GitHub Actions, Gradle, Bazel, npm/pnpm/bun, Go and Cargo toolchains, Artifactory/ECR | Named as the platform team's surface, [posting 2026-07-13](https://job-boards.greenhouse.io/flexport/jobs/7921068) |
| Infrastructure as code | Terraform, CloudFormation, CDKTF | Hiring requirement only, [postings](https://job-boards.greenhouse.io/flexport/jobs/7994947) |
| Data warehouse | Snowflake, BigQuery, Redshift or Databricks named as "such as" | Hiring requirement only, [posting](https://job-boards.greenhouse.io/flexport/jobs/7449436) |
| AI | LLM agents, RAG, prompt engineering, evaluation | Required on AI roles, [posting](https://job-boards.greenhouse.io/flexport/jobs/7311835) |

Open source: the [flexport GitHub organisation](https://github.com/flexport) has 69 public repositories (accessed 2026-07-29), mostly Ruby tooling — [rubocop-flexport](https://github.com/flexport/rubocop-flexport), [quarantine](https://github.com/flexport/quarantine) for flaky-test handling, and `activejob-limiter` — plus forks of `vllm-production-stack` and `llm-d-deployer`, which are LLM-serving infrastructure. An engineering blog is linked from the careers site at [flexport.engineering](https://flexport.engineering/); it did not respond to automated requests on 2026-07-29.

### Systems

| System | What it does | Source |
|---|---|---|
| Rates platform and self-serve booking | Client-facing pricing and booking across ocean, air and trucking, built by a new AI-first "Autonomous Freight Systems" team in San Francisco | [posting](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| AI agents for exceptions | Agents that detect problems, reroute shipments and keep goods moving, with human experts in the loop | [posting](https://job-boards.greenhouse.io/flexport/jobs/7311835) |
| Customs systems | Customs entry, classification and compliance, built by a dedicated team in Amsterdam | [posting](https://job-boards.greenhouse.io/flexport/jobs/8000000) |
| Data infrastructure | Pipelines and architecture processing millions of supply chain events daily for shipment visibility | [posting](https://job-boards.greenhouse.io/flexport/jobs/7449436) |
| Developer platform | Build tooling, CI/CD, Kubernetes and artifact infrastructure for the engineering organisation | [posting](https://job-boards.greenhouse.io/flexport/jobs/7921068) |
| Public API and EDI | Versioned REST API with webhooks, plus EDI integration for enterprise clients | [API docs](https://apidocs.flexport.com/) |

### Technical background sought

Separating what the postings require from what they merely prefer:

- **Required on AI roles:** hands-on agent patterns, RAG, prompt engineering, tool use and evaluation — described as going "beyond 'AI familiarity'" ([posting](https://job-boards.greenhouse.io/flexport/jobs/7975365)).
- **Required on infrastructure roles:** production ownership on cloud infrastructure, infrastructure as code, containers and service-oriented architectures, data warehousing and pipeline work ([posting](https://job-boards.greenhouse.io/flexport/jobs/7449436)).
- **Required on security roles:** application security across a polyglot codebase — Ruby, Java/Kotlin, TypeScript/JavaScript, Python ([posting](https://job-boards.greenhouse.io/flexport/jobs/7921061)).
- **Preferred, not required:** experience with the existing stack itself — "Experience with elements of our tech stack: Java, Spring Boot, Ruby on Rails, React, AWS" appears under "it's a plus" on the San Francisco roles ([posting](https://job-boards.greenhouse.io/flexport/jobs/7819181)).

The Customs posting states the team is "tech-agnostic regarding candidate background," and the careers site says engineers without freight forwarding experience are welcome ([careers](https://www.flexport.com/careers/teams/engineering/); accessed 2026-07-29).

### Industry domain

The work sits on international freight forwarding and customs, which is the same domain as [Shippio](../shippio/) but at US and EU regulatory scope:

- **Customs and trade compliance** — customs entries, HS classification, duty drawback, tariff refunds, and broker error rates; the Winter 2026 release includes an audit tool for other brokers' filings and a tariff refund calculator ([release](https://www.flexport.com/technology/product-release/winter-2026/)).
- **Regulated intermediation** — operating as a licensed OTI under the FMC and as a customs broker under CBP shapes what the software is allowed to do on a client's behalf ([terms](https://www.flexport.com/terms-and-conditions/)).
- **Freight economics** — carrier contracts and allocations, rate sheets, container utilisation and consolidation; a stated 10% freight-cost reduction comes from a consolidation algorithm ([about page](https://www.flexport.com/company/about-us/)).
- **Documents and interchange** — purchase orders, commercial invoices, bills of lading and EDI message flows between enterprise systems ([API docs](https://apidocs.flexport.com/)).

Domain knowledge is explicitly not a hiring prerequisite; it is expected to be learned on the job.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Engineering locations | San Francisco, Amsterdam, Atlanta, Shanghai, Beijing, Shenzhen; roles are posted per city | [job board](https://job-boards.greenhouse.io/flexport); as of 2026-07-29 |
| Published salary bands (US) | Staff Software Engineer, San Francisco: $196,875–$246,094 base; Senior Software Engineer, San Francisco: $183,000–$229,000 base; Automation Engineer I, Atlanta: $78,400–$98,000 base. Bands exclude bonus, equity and benefits | [Staff](https://job-boards.greenhouse.io/flexport/jobs/7819181), [Senior](https://job-boards.greenhouse.io/flexport/jobs/7975365), [Automation](https://job-boards.greenhouse.io/flexport/jobs/8015840) postings |
| Non-US bands | Amsterdam and China postings reviewed do not publish a salary range | [postings](https://job-boards.greenhouse.io/flexport/jobs/7311835) |
| Remote policy | No remote or hybrid policy was stated in the postings reviewed | [job board](https://job-boards.greenhouse.io/flexport); as of 2026-07-29 |
| Third-party compensation data | Levels.fyi reports $187K for Software Engineer I to $440K+ for Senior Staff, median $266K total compensation | [Levels.fyi](https://www.levels.fyi/companies/flexport/salaries/software-engineer); accessed 2026-07-29 |

---

## Notes

### Not publicly disclosed

Searched on 2026-07-29 across flexport.com, its careers and developer sites, the Greenhouse board, GitHub, and Shopify's SEC filings:

- No company-published headcount, revenue, or valuation. Every financial figure on this page comes either from Shopify's filings or from third-party analysis.
- No public price list or rate card; pricing is quoted per shipment.
- No security certification (ISO 27001, SOC 2) is claimed on the site pages reviewed.
- No leadership or executive team page.
- The engineering blog linked from the careers site did not respond to automated requests; its contents were not reviewed.

### Inconsistencies across sources

- **Valuation.** $8B was the [February 2022](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/) round price and is still the figure most databases carry. [Sacra](https://sacra.com/c/flexport/) estimates $3.8B as of 2024 by imputing from Shopify's stake. Shopify's own [10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) reports an equity-method carrying value, which is an accounting balance and not a valuation. The three are not comparable.
- **Revenue.** $2.1B for 2024 is gross revenue; ~$450M for 2025 is net revenue. Both circulate without the qualifier.
- **Headcount.** ~2,100 (2025) appears on [Wikipedia](https://en.wikipedia.org/wiki/Flexport); the company's [about page](https://www.flexport.com/company/about-us/) gives only "more than 400 software engineers", undated.
- **Founders.** [Wikipedia](https://en.wikipedia.org/wiki/Flexport) names Ryan and David Petersen as co-founders; company material names only Ryan Petersen.

### Other

- The Convoy Platform was bought in November 2023 and sold in July 2025, about 20 months later, for a reported ~$250M against a reported ~$16M purchase price; Flexport kept the brokerage business running on it ([company post](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)).
- Four rounds of layoffs were reported between December 2022 and October 2024, including ~20% in [October 2023](https://www.cnbc.com/2023/10/12/flexport-is-laying-off-20percent-of-its-workforce.html) and ~2% in [October 2024](https://www.supplychaindive.com/news/flexport-layoffs-fulfillment-forwarding-shopify/728950/).
- Shopify is simultaneously a shareholder, a convertible-note holder, a commercial partner and a co-marketing counterparty ([Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)). Its filings are currently the most reliable public window into Flexport's finances.
- Engineering is split between the US, the Netherlands and three cities in China, with the newest AI teams posted in San Francisco and Amsterdam ([job board](https://job-boards.greenhouse.io/flexport); as of 2026-07-29).

---

## Resources

**Official**

- [Flexport](https://www.flexport.com/) · [about](https://www.flexport.com/company/about-us/) · [newsroom](https://www.flexport.com/company/newsroom/) · [blog](https://www.flexport.com/blog/)
- [Careers — engineering](https://www.flexport.com/careers/teams/engineering/) · [Greenhouse job board](https://job-boards.greenhouse.io/flexport) · [job board API](https://boards-api.greenhouse.io/v1/boards/flexport/jobs)
- [API documentation](https://apidocs.flexport.com/) · [developer FAQ and EDI docs](https://developers.flexport.com/faq/general/)
- [Atlas — public ocean freight map](https://atlas.flexport.com/)
- [Terms and conditions, including licence statements](https://www.flexport.com/terms-and-conditions/)
- [Flexport Platform](https://www.flexport.com/products/flexport-platform/) · [Control Tower](https://www.flexport.com/technology/control-tower/) · [Customs Suite](https://www.flexport.com/technology/customs-suite/) · [Flexport Intelligence](https://www.flexport.com/technology/flexport-intelligence/) · [rates](https://www.flexport.com/rates/)
- [Winter 2026 product release](https://www.flexport.com/technology/product-release/winter-2026/)
- [Why We Bought, Built, and Sold the Convoy Platform, 2025-07-28](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)
- [Series E announcement, 2022-02-07](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/) · [Series D announcement, 2019](https://www.flexport.com/blog/flexport-secures-usd1-billion-in-funding-led-by-softbank-vision-fund/)
- [GitHub organisation](https://github.com/flexport) · [rubocop-flexport](https://github.com/flexport/rubocop-flexport) · [quarantine](https://github.com/flexport/quarantine) · [engineering blog](https://flexport.engineering/)

**Filings and financial**

- [Shopify 10-K for FY2025, filed 2026-02-11](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) — equity-method investment, convertible notes, related-party agreements
- [Shopify 10-Q, filed 2026-05-05](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000019/shop-20260331.htm)
- [Sacra — revenue and valuation analysis](https://sacra.com/c/flexport/)
- [Tracxn — funding history](https://tracxn.com/d/companies/flexport/__MY-G7JqqdTHK8-1y1arkCLJEJeVwbwMgeQLTcMS4Izk/funding-and-investors) · [Crunchbase Series E](https://www.crunchbase.com/funding_round/flexport-series-e--3590ef78)

**Third-party coverage**

- [Business Wire — Series E, 2022-02-07](https://www.businesswire.com/news/home/20220207005279/en/Flexport-Announces-935-Million-in-Funding-to-Advance-Resiliency-and-Visibility-in-Global-Supply-Chain)
- [PR Newswire — Winter 2025 release, 2025-02-24](https://www.prnewswire.com/news-releases/flexport-unveils-20-tech-and-ai-powered-products-to-modernize-global-supply-chains-302383593.html)
- [GeekWire — Convoy Platform sale to DAT, 2025](https://www.geekwire.com/2025/flexport-is-selling-convoys-technology-to-freight-giant-dat/) · [FreightWaves](https://www.freightwaves.com/news/less-than-2-years-after-flexport-bought-convoys-tech-stack-its-being-sold-to-dat)
- [CNBC — October 2023 layoffs](https://www.cnbc.com/2023/10/12/flexport-is-laying-off-20percent-of-its-workforce.html) · [Supply Chain Dive — October 2024 layoffs](https://www.supplychaindive.com/news/flexport-layoffs-fulfillment-forwarding-shopify/728950/)
- [Dealroom — CEO interview on net revenue and AI agents](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot)
- [Levels.fyi — compensation data](https://www.levels.fyi/companies/flexport/salaries/software-engineer)
- [Wikipedia](https://en.wikipedia.org/wiki/Flexport)
