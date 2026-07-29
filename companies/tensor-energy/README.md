# Tensor Energy

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Tensor Energy (Tensor Energy株式会社) is a Fukuoka-based company founded in November 2021. It develops **Tensor Cloud**, a cloud platform for renewable energy operators covering generation forecasting, financial simulation, asset management, battery charge/discharge optimization, and electricity market trading.

- As of [2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html), the platform covers 194 MW across 1,000+ power plants and battery sites; as of [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html), 30+ operators and aggregators were customers.
- Total funding ¥1.7B, most recently a ¥950M Series A closed [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html), led by Global Brain.
- Team size ~18 across 9 countries ([2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)). Internal working language is English ([TokyoDev](https://www.tokyodev.com/companies/tensor-energy); Undated; accessed 2026-07-29).
- Backend is Go on AWS serverless; engineering roles have been advertised as not requiring Japanese ([job posting](https://tensor-career-en.notion.site/Senior-Backend-Engineer-198e97a69a1681db97bed51078da60cc), [TokyoDev listing](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer); Undated; accessed 2026-07-29).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | Tensor Energy株式会社 / Tensor Energy Inc. | [company page](https://www.tensorenergy.jp/en/company) |
| Founded | November 2021 | [company page](https://www.tensorenergy.jp/en/company) |
| HQ | ONE FUKUOKA BLDG. 7F, 1-11-1 Tenjin, Chuo-ku, Fukuoka 810-0001 | [company page](https://www.tensorenergy.jp/en/company) |
| Representatives | Nana Hori (堀 菜々), Vincent Filter (フィルター ヴィンセント) | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| Headcount | ~18, across 9 countries | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| Internal language | English | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy); Undated; accessed 2026-07-29 |
| Customers | 30+ power producers and aggregators | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| Assets on platform | 194 MW, 1,000+ sites | [2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) |
| Total raised | ¥1.7B | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| Investors | Genesia Ventures, Delight Ventures, Global Brain, Globis Capital Partners, Mizuho Capital, Fukuoka Financial Group, Plug and Play | [company page](https://www.tensorenergy.jp/en/company) |

The company page and TokyoDev profile are continuously updated pages without publication dates; both were accessed on 2026-07-29.

Programs and awards announced by the company: [J-Startup KYUSHU (2023-04-18)](https://prtimes.jp/main/html/rd/p/000000004.000096424.html), [Plug and Play Japan Winter/Spring 2023 Batch (2022-12-01)](https://prtimes.jp/main/html/rd/p/000000142.000028153.html), [JETRO Global Startup Acceleration Program (2024-09-03)](https://prtimes.jp/main/html/rd/p/000000009.000096424.html), [ASEAN market-entry support program (2024-08-09)](https://prtimes.jp/main/html/rd/p/000000008.000096424.html), [High Growth Program FY2026 (2026-06-05)](https://prtimes.jp/main/html/rd/p/000000034.000096424.html). The company was based at Fukuoka Growth Next, where two of its investors were introduced ([BRIDGE, 2024-04](https://thebridge.jp/2024/04/tensor-energy-fgn-special)).

### Market context as stated by the company

From the [Series A release, 2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html):

- Japan's energy self-sufficiency rate was approximately 13% (FY2022, Agency for Natural Resources and Energy).
- Output curtailment of solar and wind has spread to all 10 grid areas; the Tokyo area saw its first curtailment on 2026-03-01.
- From April 2026, small-scale batteries and generators became eligible to participate in the balancing market (需給調整市場). A bill amending the Electricity Business Act was approved by cabinet in March 2026.

---

## Product

**Tensor Cloud** is documented publicly at [docs.tensorenergy.jp](https://docs.tensorenergy.jp/en/). Feature areas, per the documentation:

### Development / simulation
[Simulations](https://docs.tensorenergy.jp/reference/simulations/introduction) with [CAPEX](https://docs.tensorenergy.jp/reference/library/capex) and [OPEX](https://docs.tensorenergy.jp/reference/library/opex) libraries, [scenarios](https://docs.tensorenergy.jp/reference/library/scenarios/introduction), [price forward curves](https://docs.tensorenergy.jp/technology/simulations/price-forward-curves), [solar](https://docs.tensorenergy.jp/technology/simulations/solar) and [battery](https://docs.tensorenergy.jp/technology/simulations/battery) models, [curtailment](https://docs.tensorenergy.jp/technology/simulations/curtailment), [FIP](https://docs.tensorenergy.jp/technology/simulations/fip), [financial](https://docs.tensorenergy.jp/technology/simulations/financial) and [weather](https://docs.tensorenergy.jp/technology/simulations/weather-model) models, and [SPV settings](https://docs.tensorenergy.jp/reference/spvs/introduction).

### Asset management
[Asset list](https://docs.tensorenergy.jp/reference/assets/asset-list), map, timeline, settings, [bulk upload](https://docs.tensorenergy.jp/reference/assets/bulk-upload), tags, files, [data coverage](https://docs.tensorenergy.jp/reference/assets/data-coverage); [accounts](https://docs.tensorenergy.jp/reference/asset-management/accounts); [contract management](https://docs.tensorenergy.jp/reference/contracts/introduction) for PPAs and bilateral agreements.

### Operations and trading
[Forecasts](https://docs.tensorenergy.jp/reference/forecasting/forecasts), [balancing groups](https://docs.tensorenergy.jp/reference/balancing/balancing-groups), [balancing plan submission](https://docs.tensorenergy.jp/reference/balancing-operations/submitting-plans), [generation data upload](https://docs.tensorenergy.jp/reference/data-uploads/generation-data), [JEPX trading](https://docs.tensorenergy.jp/reference/trading/jepx), and [battery optimization](https://docs.tensorenergy.jp/technology/operations/battery-optimization).

### Commercialization

The product is commercialized as a paid subscription with a fully published price list. The current version is dated [January 2026](https://docs.tensorenergy.jp/legal/pricing/pricing-2026-01); an earlier version dated [June 2023](https://docs.tensorenergy.jp/legal/pricing/pricing-2023-06) remains online, so the pricing model has been revised at least once.

The structure combines a monthly workspace subscription with unlimited users, capacity-based fees per registered kWp for forecasting and asset management, and volume-based fees for aggregation support. Aggregation is offered in two variants: a SaaS plan where the customer handles JEPX trading itself, and a BPO plan where Tensor Energy runs the operation.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2024-04 | 152 solar sites; target 400 by end of 2024 | [BRIDGE](https://thebridge.jp/2024/04/tensor-energy-fgn-special) |
| 2024-09 | 170+ solar sites | [Ambitions](https://ambitions-web.com/articles/tensorenergy) |
| 2026-04-02 | 800+ sites; 30+ operators and aggregators; 21 months of solar+battery operating history | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| 2026-07-27 | 194 MW, 1,000+ sites, including 1,051 low-voltage solar sites; 2+ years of operating history for high-voltage solar+battery | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) |

### Announced customers and partners

| Date | Party | Detail |
|---|---|---|
| [2024-06-03](https://prtimes.jp/main/html/rd/p/000000007.000096424.html) | Kyocera TCL Solar | Solar + battery facility in Kumamoto begins operation; described in the [2026-07-27 release](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) as Japan's first large FIP co-located battery |
| [2025-03-10](https://prtimes.jp/main/html/rd/p/000000012.000096424.html) | Tokyo Century | Demand-forecasting-enabled Tensor Cloud for onsite PPA and FIP surplus sales |
| [2026-02-03](https://prtimes.jp/main/html/rd/p/000000026.000096424.html) | — | Low-voltage solar bulk operation support business launched |
| [2026-02-18](https://prtimes.jp/main/html/rd/p/000000027.000096424.html) | — | Selected for a low-voltage solar "FIP conversion + battery" feasibility validation project |
| [2026-03-16](https://prtimes.jp/main/html/rd/p/000000028.000096424.html) | Univers | Low-voltage grid battery bulk operation aggregation business |
| [2026-03-30](https://prtimes.jp/main/html/rd/p/000000032.000096424.html) | KS Energy (Higo Bank group) | FIP co-located battery aggregation, DC-link method |
| [2026-04-07](https://prtimes.jp/main/html/rd/p/000000030.000096424.html) | — | Support for JEPX new system migration |
| [2026-06-29](https://prtimes.jp/main/html/rd/p/000000035.000096424.html) | — | Started recruiting EPC partners for FIT→FIP conversion of solar plants |
| [2026-07-21](https://prtimes.jp/main/html/rd/p/000000037.000096424.html) | LC-JAPAN | Low-voltage grid battery partnership |
| [2026-07-22](https://prtimes.jp/main/html/rd/p/000000036.000096424.html) | Green Road Energy | Low-voltage grid battery partner |
| [2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) | Rising Corporation (listed) | Low-voltage grid battery partner |

### Stated plans

From the [Series A release (2026-04-02)](https://prtimes.jp/main/html/rd/p/000000031.000096424.html), funds are to be used for: (1) hiring, including executives, and building out sales, service delivery, and corporate functions; (2) product development toward automated battery operation and fully automated asset management; (3) expansion into acquiring, operating, and managing power plants directly, and eventually structuring energy asset funds.

For the low-voltage battery business, the stated aggregation target is 500 units by 2028 and 1,000 by 2030 ([2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)).

---

## Founder

**Nana Hori (堀 菜々)** — co-founder, representative director; leads operations and customer relationships.

- 2011: entered the renewable energy industry as a strategy consultant, working on battery market research, solar market entry projects, battery product development, and distributed generation project finance, in Japan and abroad ([Ambitions](https://ambitions-web.com/articles/tensorenergy), [Venture Café Fukuoka](https://venturecafefukuoka.org/speakers/%E3%83%8A%E3%83%8A-%E5%A0%80/)).
- 2016: participated in establishing Shift Energy Japan, a renewable energy finance platform, leading the business development team on solar project structuring, development, and construction ([Venture Café Fukuoka](https://venturecafefukuoka.org/speakers/%E3%83%8A%E3%83%8A-%E5%A0%80/)).
- Relocated to Fukuoka approximately six years before the [2024-04 BRIDGE interview](https://thebridge.jp/2024/04/tensor-energy-fgn-special) while working on battery storage.
- November 2021: co-founded Tensor Energy. Described on the [company page](https://www.tensorenergy.jp/en/company) as having 13+ years in renewables.
- Longer interviews: [Ambitions (JA)](https://ambitions-web.com/articles/tensorenergy), [Globis Capital Partners podcast (JA)](https://www.globiscapital.co.jp/ja/podcast/eo-qz_cn7ldz), [Fukuoka Growth Next founding story (JA)](https://growth-next.com/blog/tensor-energy-founding-story).

**Vincent Filter** — co-founder, representative director; leads product and technology ([company page](https://www.tensorenergy.jp/en/company), [LinkedIn](https://www.linkedin.com/in/vincent-filter-72131860/)).

- Former strategy consultant covering the power sector.
- Prior experience in SaaS development and commercialization; UX design background.

**Other leadership listed on the [company page](https://www.tensorenergy.jp/en/company)**

| Name | Role | Stated background |
|---|---|---|
| Akira Shirota | COO | 30+ years in power and energy |
| Sebastian Watzke | Head of Product | ex-Google, ex-Rakuten |
| Riccardo Iacobucci | Principal Energy & Data Scientist | PhD, Kyoto University |
| Miguel Acevedo | Infrastructure & IoT | 20 years in cloud and software |
| Macky Tanaka | Head of Design | — |

The same page also lists frontend, backend, business development, and data science team members.

---

## Funding

| Date | Round | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2022-03-08 | Seed | ¥70M | Genesia Ventures | ¥70M | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000002.000096424.html) |
| 2024-03-27 | Pre-Series A | ¥450M | Genesia Ventures and others | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000006.000096424.html), [Genesia (EN)](https://www.genesiaventures.com/en/investment-tensorenergy-3/) |
| 2025-03-04 | Pre-Series A extension | ¥100M | Globis Capital Partners | ~¥700M | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000013.000096424.html) |
| 2026-04-02 | Series A | ¥950M | Global Brain (lead), Globis Capital Partners, Delight Ventures | ¥1.7B | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000031.000096424.html), [Kepple (JA)](https://kepple.co.jp/articles/h7tb46tvbss1) |

Round labels above follow the company's own releases. [Genesia Ventures](https://www.genesiaventures.com/en/investment-tensorenergy-3/) described its March 2024 participation as its third investment in the company. The [company page](https://www.tensorenergy.jp/en/company) additionally lists Mizuho Capital, Fukuoka Financial Group, and Plug and Play as investors.

The March 2024 round was announced together with the launch of the battery charge/discharge optimization service ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000006.000096424.html)). The solar generation forecasting service went GA in [June 2023](https://prtimes.jp/main/html/rd/p/000000005.000096424.html).

---

## Engineering

### Technology stack and platforms

Inferred from job postings and public documentation:

- **Backend:** Go ([posting](https://tensor-career-en.notion.site/Senior-Backend-Engineer-198e97a69a1681db97bed51078da60cc)); an earlier posting accepted Go or Rust ([TokyoDev, 2025-03-05](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer))
- **Cloud:** AWS, serverless and event-driven; AWS CDK; AWS IoT Core ([posting](https://tensor-career-en.notion.site/Senior-Backend-Engineer-198e97a69a1681db97bed51078da60cc), [integration guide](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide))
- **Frontend:** TypeScript ([company page](https://www.tensorenergy.jp/en/company))
- **Interfaces:** REST platform API; MQTT over TLS, defined via AsyncAPI, for battery control ([API overview](https://docs.tensorenergy.jp/api/overview))

### Systems

| System | What it does | Docs |
|---|---|---|
| Solar generation forecasting | Per-plant ML models trained on that plant's history, validated against a physics simulation of the same plant and rejected if they don't beat it. Four weather providers, 14-day horizon. | [docs](https://docs.tensorenergy.jp/technology/operations/solar-forecasts) |
| Price forecasting | Per-area JEPX day-ahead price models, plus a separate model per area for the probability of a zero-price event. 13 days ahead at 30-minute granularity; weekly retraining, daily inference. | [docs](https://docs.tensorenergy.jp/technology/operations/price-forecasts) · [balancing market](https://docs.tensorenergy.jp/technology/operations/balancing-market-forecasts) |
| Battery optimization | Mixed integer linear program deciding charge/discharge across JEPX day-ahead and EPRX primary adjustment (FCR), replanned at least every 30 minutes around the D-1 10:00 gate closure. | [docs](https://docs.tensorenergy.jp/technology/operations/battery-optimization) |
| Battery / EMS integration | MQTT over TLS on AWS IoT Core carrying telemetry up and dispatch commands down, with an X.509 certificate per site gateway, 1 Hz telemetry where FCR applies, and local buffering with backfill on reconnect. | [guide](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide) · [specs](https://docs.tensorenergy.jp/api/battery-optimization/battery-optimization-specs) |
| Simulation engine | Financial and generation modelling over an asset's life — CAPEX/OPEX, scenarios, price forward curves, curtailment, FIP. | [docs](https://docs.tensorenergy.jp/technology/simulations/introduction) |
| Platform API | REST access to assets, forecasts, and actuals. | [docs](https://docs.tensorenergy.jp/api/platform/introduction) |

Public documentation is built with Docusaurus. A [public status page](https://status.tensorenergy.jp/) tracks Tensor Cloud UI, Platform, User Authentication, Tensor API, and Documentation. Accessed 2026-07-29, its trailing three-month view showed 100% for UI, auth, and API and 99.988% for the platform, with a 15-minute platform outage on 2026-07-28.

### Technical background sought

The backend role requires production Go experience. Preferred rather than required backgrounds include GraphQL, Kubernetes, DevOps or platform engineering, information security, AWS CDK and agile development ([posting](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)). These are hiring signals; the documented product itself confirms AWS CDK and IoT infrastructure, but does not establish production use of GraphQL or Kubernetes.

### Industry domain

The Japanese electricity market. What an engineer would have to pick up:

- Market mechanics — JEPX day-ahead in half-hourly slots with a D-1 10:00 gate closure, EPRX primary adjustment (FCR), the balancing market, balancing groups, plan submission to the TSO, imbalance responsibility ([docs](https://docs.tensorenergy.jp/technology/operations/battery-optimization))
- Subsidy and contract schemes — FIT, the FIP premium, post-FIT operation, onsite and offsite PPAs ([docs](https://docs.tensorenergy.jp/reference/contracts/introduction))
- Grid operations — output curtailment and its signals, low- versus high-voltage connection, AC-linked / DC-linked / grid-only battery sites ([docs](https://docs.tensorenergy.jp/technology/simulations/curtailment))
- Physics and asset finance — irradiance and plant modelling, battery state of energy and cycle cost, 30-year project cash flow with SPVs ([docs](https://docs.tensorenergy.jp/technology/simulations/financial))
- Regulatory change on its own schedule — the April 2026 reform opened the balancing market to low-voltage resources, and an Electricity Business Act amendment passed cabinet in March 2026 ([2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html))

On acquiring it: postings list "basic understanding of the energy industry and willingness to learn" as preferred, not required. The company states that all team members, engineering included, are expected to understand industry structure, energy physics, energy economics and regulation, and are taken into the field ([TokyoDev](https://www.tokyodev.com/companies/tensor-energy)).

### Working conditions

The TokyoDev company profile, role page and company careers page are undated, continuously updated sources; all were accessed on 2026-07-29.

| Item | Detail | Source |
|---|---|---|
| Language | English is the internal common language; Spanish, Japanese, German, French also spoken. Engineering postings require business English, no Japanese | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy), [posting](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer) |
| Location | Hiring prioritizes Fukuoka city, relocation encouraged but not required; Fukuoka-based staff asked to come in at least 2 days/week | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| Remote | Must be in an Asia time zone, 4–5 hours daily overlap; company operates across CET and JST | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| Visa | Japanese visa sponsored after at least 3 months of remote work | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| Benefits | Fully remote work, Fukuoka office as collaborative space, flexible hours, informal dress code, visa support, equity compensation, health insurance and pension for employees in Japan | [careers page](https://tensor-career-en.notion.site/Customer-Growth-198e97a69a1681198652e60e522b4207) |
| Turnover | Two people left in the preceding two and a half years | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| Domain expectation | All team members, engineering included, are expected to understand industry structure, energy physics, energy economics, and regulation; team members are taken into the field | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): the English and Japanese corporate sites, Tensor Cloud documentation and sitemap, legal and security pages, status page, company press releases, current careers pages and TokyoDev listings; searches for Tensor Energy and Tensor Cloud in English and Japanese; GitHub organisation/name/domain searches; conference and technical-talk searches; investor portfolios and funding databases.

- No engineering blog, conference talks, or public open-source repositories were found.
- Salary ranges are not published in the job postings reviewed ([TokyoDev posting](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer) states "No salary range given").
- The published [information security policy (January 2024)](https://docs.tensorenergy.jp/legal/information-security/information-security-2024-01) does not name any third-party certification such as ISO 27001 or SOC 2.
- The rounds in which Mizuho Capital, Fukuoka Financial Group, and Plug and Play invested are not stated publicly.

### Inconsistencies across sources

- **Headcount:** 16 ([TokyoDev](https://www.tokyodev.com/companies/tensor-energy)), 21 across 10 countries as of September 2024 ([Ambitions](https://ambitions-web.com/articles/tensorenergy)), 18 across 9 countries ([2026-04-02 release](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)), 9+ across 7+ nationalities ([Wantedly](https://sg.wantedly.com/companies/TensorEnergy)).
- **Round naming:** the company calls the March 2024 round ["pre-Series A" (プレシリーズA)](https://prtimes.jp/main/html/rd/p/000000006.000096424.html); [BRIDGE (2024-04)](https://thebridge.jp/2024/04/tensor-energy-fgn-special) reported the same round as "Series A, ¥450M."
- **Remote policy:** the [careers page](https://tensor-career-en.notion.site/Customer-Growth-198e97a69a1681198652e60e522b4207) describes the working style as "fully remote"; the [TokyoDev profile](https://www.tokyodev.com/companies/tensor-energy) describes a Fukuoka-first policy with 2 days/week in office for local staff.
- **Aggregation targets:** two releases one week apart state 1,000 low-voltage battery units by 2028 ([2026-07-21, LC-JAPAN](https://prtimes.jp/main/html/rd/p/000000037.000096424.html)) versus 500 by 2028 and 1,000 by 2030 ([2026-07-27, Rising Corporation](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)).

### Other

- The company plans to acquire and operate power plants itself and to structure energy asset funds ([2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)), alongside selling Tensor Cloud to power producers.
- Three low-voltage battery partnerships were announced within one week in July 2026 ([LC-JAPAN](https://prtimes.jp/main/html/rd/p/000000037.000096424.html), [Green Road Energy](https://prtimes.jp/main/html/rd/p/000000036.000096424.html), [Rising Corporation](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)), following the April 2026 rule change that opened the balancing market to low-voltage resources.
- [Pricing](https://docs.tensorenergy.jp/legal/pricing/pricing-2026-01), [terms of use](https://docs.tensorenergy.jp/en/legal/terms-of-use/terms-of-use-2026-06), [product and technology documentation](https://docs.tensorenergy.jp/en/), the [battery integration spec](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide), and the [status page](https://status.tensorenergy.jp/) are all published openly, without a login.

---

## Resources

**Official**

- [Tensor Cloud — product site (EN)](https://www.tensorenergy.jp/en) · [JA](https://www.tensorenergy.jp)
- [Company page — team and investors](https://www.tensorenergy.jp/en/company)
- [Press releases](https://www.tensorenergy.jp/en/press)
- [Careers (Notion)](https://tensor-career-en.notion.site/)
- [Status page](https://status.tensorenergy.jp/)
- [Documentation home](https://docs.tensorenergy.jp/en/)
  - [Solar forecasting methodology](https://docs.tensorenergy.jp/technology/operations/solar-forecasts)
  - [Price forecasting methodology](https://docs.tensorenergy.jp/technology/operations/price-forecasts)
  - [Balancing market forecasts](https://docs.tensorenergy.jp/technology/operations/balancing-market-forecasts)
  - [Battery optimization](https://docs.tensorenergy.jp/technology/operations/battery-optimization)
  - [Battery optimization integration guide (MQTT)](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide) · [specs](https://docs.tensorenergy.jp/api/battery-optimization/battery-optimization-specs) · [changelog](https://docs.tensorenergy.jp/api/battery-optimization/changelog)
  - [API overview](https://docs.tensorenergy.jp/api/overview) · [platform REST API](https://docs.tensorenergy.jp/api/platform/introduction)
  - [Pricing, January 2026](https://docs.tensorenergy.jp/legal/pricing/pricing-2026-01) · [June 2023](https://docs.tensorenergy.jp/legal/pricing/pricing-2023-06)
  - [Information security policy, January 2024](https://docs.tensorenergy.jp/legal/information-security/information-security-2024-01)
  - [Terms of use, June 2026](https://docs.tensorenergy.jp/en/legal/terms-of-use/terms-of-use-2026-06)

**Press releases (PR TIMES, JA)**

- [Series A, ¥950M — 2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)
- [Rising Corporation partnership — 2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)
- [Green Road Energy partnership — 2026-07-22](https://prtimes.jp/main/html/rd/p/000000036.000096424.html)
- [LC-JAPAN partnership — 2026-07-21](https://prtimes.jp/main/html/rd/p/000000037.000096424.html)
- [EPC partner recruitment for FIT→FIP — 2026-06-29](https://prtimes.jp/main/html/rd/p/000000035.000096424.html)
- [High Growth Program FY2026 — 2026-06-05](https://prtimes.jp/main/html/rd/p/000000034.000096424.html)
- [JEPX system migration support — 2026-04-07](https://prtimes.jp/main/html/rd/p/000000030.000096424.html)
- [KS Energy (Higo Bank group) partnership — 2026-03-30](https://prtimes.jp/main/html/rd/p/000000032.000096424.html)
- [Univers partnership, low-voltage battery aggregation — 2026-03-16](https://prtimes.jp/main/html/rd/p/000000028.000096424.html)
- [Low-voltage solar FIP+battery validation project — 2026-02-18](https://prtimes.jp/main/html/rd/p/000000027.000096424.html)
- [Low-voltage solar bulk operation support — 2026-02-03](https://prtimes.jp/main/html/rd/p/000000026.000096424.html)
- [Globis follow-on, ¥100M — 2025-03-04](https://prtimes.jp/main/html/rd/p/000000013.000096424.html)
- [Tokyo Century onsite PPA / FIP surplus — 2025-03-10](https://prtimes.jp/main/html/rd/p/000000012.000096424.html)
- [Pre-Series A, ¥450M + battery optimization launch — 2024-03-27](https://prtimes.jp/main/html/rd/p/000000006.000096424.html)
- [Kyocera TCL Solar Kumamoto battery starts operation — 2024-06-03](https://prtimes.jp/main/html/rd/p/000000007.000096424.html)
- [Solar generation forecasting GA — 2023-06-29](https://prtimes.jp/main/html/rd/p/000000005.000096424.html)
- [Seed round, ¥70M from Genesia Ventures — 2022-03-08](https://prtimes.jp/main/html/rd/p/000000002.000096424.html)

**Third-party coverage and profiles**

- [Genesia Ventures — investment announcement (EN)](https://www.genesiaventures.com/en/investment-tensorenergy-3/)
- [Kepple — Series A coverage (JA)](https://kepple.co.jp/articles/h7tb46tvbss1)
- [BRIDGE — Fukuoka Growth Next feature, 2024-04 (JA)](https://thebridge.jp/2024/04/tensor-energy-fgn-special)
- [Fukuoka Growth Next — founding story (JA)](https://growth-next.com/blog/tensor-energy-founding-story)
- [Ambitions — interview with Nana Hori (JA)](https://ambitions-web.com/articles/tensorenergy)
- [Globis Capital Partners — founders podcast (JA)](https://www.globiscapital.co.jp/ja/podcast/eo-qz_cn7ldz)
- [Solar Journal — low-voltage battery bulk operation (JA)](https://solarjournal.jp/product/63870/)
- [TokyoDev — company profile and policies](https://www.tokyodev.com/companies/tensor-energy)
- [TokyoDev — Senior Go Software Engineer posting, 2025-03-05 (closed)](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)
- [Wantedly](https://sg.wantedly.com/companies/TensorEnergy)
- [LinkedIn](https://www.linkedin.com/company/tensorenergy)
- [Crunchbase](https://www.crunchbase.com/organization/tensor-energy)
- [INITIAL / Speeda startup profile (JA)](https://initial.inc/companies/A-41638)
