# Research guide

**English** | [简体中文](GUIDE.zh-CN.md)

How company pages in `companies/` are researched and written.

> Last updated: 2026-07-29.

## Repository layout

Each company has its own directory, named with a stable lowercase slug:

```text
companies/
  README.md
  README.zh-CN.md
  company-name/
    README.md
    README.zh-CN.md
```

The two files directly under `companies/` are the English and Simplified
Chinese company indexes. Within each company directory, `README.md` is the
canonical English research page and is displayed by default when browsing the
directory on GitHub. `README.zh-CN.md` is its Simplified Chinese translation.
Additional company-specific assets or data may be kept in the same directory.

Translated pages must preserve the English page's section structure, figures,
dates, distinctions between fact and inference, and source links. Research
findings should be added to the English page first and then translated. Each
translation records the date through which it is synchronized; if it falls
behind, retain the older synchronization date rather than implying parity.

## Principles

1. **Facts, not analysis.** Report what sources say. No "why an engineer might care", no competitive positioning, no editorial reads on strategy, founders, or fundraising pace. Anyone can generate analysis; sourced facts are the value here.
2. **Every figure carries a source and a date.** Numbers go stale fast — "800+ sites" is meaningless without "as of 2026-04". Link the specific page, not the site.
3. **Prefer primary sources.** Company press releases, product documentation, job postings, and legal/pricing pages beat media coverage and startup databases. Databases are often months behind.
4. **Record material conflicts, don't flatten them.** Apply the claim-specific source precedence for the current statement, then retain both sides with links when they describe the same scope and period or the difference would materially mislead the reader.
5. **Absence is a scoped finding.** No tech blog, no published salary bands, no security certification — say what public sources were checked and when, in the `Notes` section.
6. **Apply materiality, not exhaustiveness.** Public availability is not by itself a reason to include a fact. Keep information that materially changes the reader's understanding of the product, engineering work, working conditions, business durability, control, regulation, or an important source conflict.

## Research protocol

### Minimum search scope for absence claims

Before writing that information was not publicly found, complete a reproducible minimum search:

1. Map the official surface: homepage navigation, `robots.txt` or sitemap where available, company/about, product and documentation, press index, careers, legal pages, blog, and relevant subdomains.
2. Search the current brand, legal name, former names, and product names together with the target topic, in English and the company's relevant local language.
3. Check the authoritative external source for the claim type: corporate or regulatory registers for identity and licences; investor portfolios and funding databases for financing; current and archived job boards for hiring; GitHub organisation, company-name, domain, and product-name searches for open source.
4. Record the search date, names and languages used, and source classes checked. Scope the conclusion as "not found in the reviewed public sources as of YYYY-MM-DD", not "does not exist".

An existing blog or press index does not need every article read before making an unrelated absence claim. Search its index, sitemap, categories, and relevant keywords. A claim that the blog never covers a particular topic requires a correspondingly broader review. Do not search founders' unrelated personal repositories or private accounts merely to support a company-level absence claim.

### Source precedence by claim type

Source authority is specific to the claim; there is no single hierarchy for every fact.

| Claim type | Preferred order |
|---|---|
| Legal identity, registration, licence | Regulator or corporate register; statutory filing; current legal document; official company page; third party |
| Funding, ownership, current operating figure | Dated statutory filing or company release; investor announcement; current official overview; reputable media; database |
| Current product capability | Current product or API documentation and observable public product surface; dated product release; official marketing; interview or social post |
| Technology stack | Public technical assets, documentation, or technical writing; current job posting as inference or hiring-only evidence; third-party profile |
| Working conditions | Current official role, careers FAQ, or policy; first-party recruiting platform; reputable job board; general company profile |

Use the most authoritative, specific, and appropriately dated source for the current statement. Keep an older figure as history when it describes a different date. Put a disagreement in `Notes` when sources purport to describe the same scope and period, or when the difference would materially mislead the reader. A stale database entry does not need equal placement beside a newer primary release unless the conflict itself matters.

### Date labels

Use the date that describes the claim, not merely the date on which the page was opened.

| Label | Use |
|---|---|
| `Published` | When an article, release, filing, or posting was issued |
| `Effective` | When terms, a policy, registration, or licence took effect |
| `As of` | The measurement date or period to which a figure applies |
| `Accessed` | When an undated or continuously changing page was inspected |

If a source has no publication date, write `Undated; accessed YYYY-MM-DD`. An access date does not make an undated figure current. When the source supplies both publication and measurement dates, retain both.

## Page structure

Skeleton to copy for a new company:

```markdown
# Company Name

> Notes compiled from publicly available sources. Last updated: YYYY-MM-DD.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR
## Basic
## Product
## Founder
## Funding
## Engineering
## Notes
## Resources
```

When a translation exists, add reciprocal language links below the title:

```markdown
**English** | [简体中文](README.zh-CN.md)
```

```markdown
[English](README.md) | **简体中文**
```

### Bilingual terminology

Use these section names consistently. Company-specific subheadings may be added, but should not introduce a new translation for an established term.

| English | Simplified Chinese |
|---|---|
| TL;DR | 摘要 |
| Basic | 基本情况 |
| Product | 产品 |
| Founder | 创始人 |
| Selected leadership | 主要管理层 |
| Funding | 融资 |
| Capital and financials | 资本与财务 |
| Engineering | 工程 |
| Technology stack and platforms | 技术栈与平台 |
| Systems | 系统 |
| Technical background sought | 招聘所需技术背景 |
| Industry domain | 行业领域 |
| Working conditions | 工作条件 |
| Notes | 备注 |
| Not publicly disclosed | 未公开披露 |
| Inconsistencies across sources | 不同来源之间的不一致 |
| Other | 其他 |
| Resources | 资料来源 |
| Identity and legal entities | 品牌与法律实体 |

What belongs in each section:

### TL;DR

One paragraph — what the company is, where, when founded, what the product does — followed by 3–5 bullets carrying the numbers a reader would otherwise have to hunt for: current scale, total funding and latest round, team size, and the one-line engineering summary (main language, cloud, whether the engineering team works in English). Every bullet links its source.

### Basic

A table of company facts, each with a source column: current public brand, legal name (local and English), founding date, HQ address, representatives, headcount, engineering-team working language, customer count, assets or scale under management, total raised, and investor list. Describe a company-wide language policy only when the source actually applies company-wide. Add former legal names and former brands when applicable.

Below the table: accelerators, government programs, and awards, each linked and dated. If the company states market or regulatory context in its own releases (policy changes, industry conditions), summarize it here and attribute it as the company's framing rather than as established fact.

Do not collapse different identity concepts into a generic "former name":

- **Former legal name** — the same legal entity changed its registered name.
- **Former brand** — the business changed its public brand; legal continuity may or may not be established.
- **Trading name / DBA** — a commercial name used by a legal entity.
- **Predecessor** — an earlier company or operation; do not assume it is the same legal entity.
- **Related entity** — a group, regional, licensed, employing, or settlement entity; it is not an alias.

For a straightforward rename, rows in `Basic` are enough. When several brands, legal entities, or jurisdictions are involved, add an `Identity and legal entities` subsection with name, type, jurisdiction, relevant period or status, relationship, and source. Separate confirmed legal continuity, evidence of business or brand continuity, researcher inference, and unresolved relationships.

### Product

- **What it is and its feature areas** — organized the way the docs organize them, linking each area to its documentation page.
- **Commercialization** — how it is sold: subscription, capacity-based, volume-based, services. Note whether a public price list exists and whether multiple dated versions show the model changing. Keep the structure, skip the individual numbers; the price list is one click away.
- **Reported scale over time** — a table of representative milestones with dates: the earliest useful baseline, major changes, and the latest figure. Do not reproduce every quarterly or repeated disclosure.
- **Announced customers and partners** — include material examples that establish a new product, rail, customer segment, geography, concentration, or strategic change. Routine campaigns, exhibitions, repeated deployments, and non-specific MOUs do not need one row each.
- **Stated plans** — where the company says it is heading, quoted from its own releases (use of funds, targets with deadlines).

### Founder

Founders first: role and responsibility split, then a dated career timeline built from interviews and speaker bios. Add other leaders when their remit materially affects product, engineering, operations, finance, hiring, or company control; do not reproduce a full listed-company board or auditor roster by default. Then note what other functions the team page lists (frontend, backend, data science, etc.).

Verifiable career facts only. Don't characterize people, and don't assess whether a founding team is well matched.

### Funding

One table: date, round name, amount, investors, cumulative, source. Use the round names the company itself used. Follow with plain facts that don't fit the table — which investor led, repeat participation, investors listed on the company page without a stated round, and any product launch announced alongside a round.

For a listed company, this section may be renamed `Capital and financials`. Keep pre-IPO rounds and the IPO, a three-to-five-year operating trend, material ownership or control, customer concentration, and meaningful option dilution. Summarize rather than reproduce complete share-issuance ledgers, custody-account shareholder tables, or routine quarterly guidance.

### Engineering

- **Technology stack and platforms** — concrete implementation choices: languages, frameworks, databases, infrastructure, protocols, execution environments, and external platforms, such as Java, InfluxDB, AWS, MQTT, EVM, or Solidity. Label each item as confirmed by documentation or public assets, inferred from hiring, or mentioned only as a hiring requirement. A requirement does not establish current use.
- **Systems** — what the company actually builds or operates: payment and settlement, real-time dispatch, IoT telemetry, monitoring platforms, data acquisition, forecasting and optimization, on-chain settlement, ERP integration, and similar systems. Give each system a short description and a source. Do not infer a system solely from a preferred qualification.
- **Technical background sought** — the kinds of work candidates are expected to have done before: observability or monitoring systems, DevOps and platform engineering, financial core systems, high-volume transaction processing, smart-contract security, node infrastructure, or third-party integrations. Keep required and preferred items separate. This is about prior problem experience, not years of employment or a list of technologies.
- **Industry domain** — the business, regulatory, physical, and economic knowledge behind the work: finance, cross-border payments, energy markets, freight and customs, stablecoin regulation, market mechanisms, contract and subsidy schemes, settlement flows, regulators and filing regimes, or the physics the product models. State whether this background is required, preferred, or explicitly learnable after joining.
- **Working conditions** — a sourced table: engineering-team working language and the scope of that evidence, location and office policy, remote constraints, visa sponsorship, benefits, salary if published, turnover, whether new graduates or junior engineers are explicitly considered, and any stated expectation about how the team works.

A term can belong to different sections only with a different meaning. For example, on-chain settlement is a system, EVM is a platform, Solidity is a concrete technology, smart-contract auditing is a sought technical background, and stablecoin regulation is industry knowledge. Keep those claims separate and source each one at the appropriate level.

### Notes

Grouped into three:

- **Not publicly disclosed** — engineering blog, open-source presence, salary bands, security certifications, which investor joined which round. Each conclusion states the search date and reviewed public-source scope.
- **Inconsistencies across sources** — headcount, round naming, cumulative funding, policy statements, targets. Both sides linked.
- **Other** — anything factual worth flagging that has no home above: business model shifts the company has announced, clusters of related announcements, how much of the product surface is published openly.

### Resources

Every source used, grouped as **Official** (site, company page, press index, careers, documentation with sub-links), **Press releases** (each with date, newest first), and **Third-party coverage and profiles** (VC announcements, media, job boards, databases). Mark non-English sources with a language tag.

## Special company situations

### Listed or disclosure-heavy companies

Regulatory filings make far more information available than an early-stage company page can use. Apply the same engineer-oriented scope rather than treating the filing as a checklist to reproduce. Prefer:

- the latest value plus a three-to-five-year trend for revenue, profitability, headcount, and the operating metric that best explains scale;
- business mix, material customer concentration, control, dilution, development footprint, and disclosed investment in software or infrastructure;
- product, partner, and leadership events only when they change the reader's understanding of the business or engineering work.

Availability is not materiality. Full securities issuance histories, every major shareholder, all outside directors and auditors, routine quarterly figures, and every press release normally remain in the linked filing or press index.

### Renames, predecessor brands, and multiple entities

Establish identity before attributing operating facts. Use the current primary brand as the page title and stable directory slug, then record aliases and predecessor names inside the page. For complex cases, put `Identity and legal entities` near the beginning and include a short dated continuity timeline.

Do not automatically carry a predecessor's funding, customers, licences, headcount, traction, or claims into the current brand. State which brand or entity each historical fact applies to. Evidence such as shared founders, domains, email addresses, backends, hiring, or an explicit "formerly" statement may establish business or brand continuity without proving that the legal entity is the same. Record that distinction once in the identity section and cross-reference it rather than repeating the same caveat throughout the page.

## Where to look

### 1. Official site

Map it before reading anything: the homepage's own links point to the subdomains that carry the substance — documentation, the careers site, the press index, the company/team page. Marketing copy on the landing page is the least useful thing there.

### 2. Product documentation

If a company publishes docs, this beats every interview and news article. Look for:

| Docs area | What you learn |
|---|---|
| `technology/`, methodology pages | Real algorithms, models, data sources, training and inference cadence, accuracy figures |
| `api/` | Protocols, auth model, integration architecture, assumptions about customer systems and hardware |
| `reference/` | The actual feature surface — better than marketing copy |
| `legal/pricing` | The business model; often several dated versions showing how it changed |
| `legal/information-security` | Security posture, and whether any third-party certification is named |

Docs sites usually expose a sitemap that lists every page, which is faster than clicking through the navigation.

### 3. Press releases

Work from the company's own press index rather than search results, and read the release body rather than a summary of it — summaries routinely mangle numbers. Note that a company's own index often lags its newest releases by days or weeks, so also check its page on the distribution service.

Common distribution services:

| Region | Services |
|---|---|
| Japan | [PR TIMES](https://prtimes.jp), [@Press](https://www.atpress.ne.jp), [Kyodo News PR Wire](https://kyodonewsprwire.jp), [Dream News](https://www.dreamnews.jp), [ValuePress](https://www.value-press.com) |
| Global | Business Wire, PR Newswire, GlobeNewswire, EIN Presswire |

### 4. Job postings

There is rarely a published stack page. Reconstruct it from postings, and mark it as inferred:

- **Required vs. preferred** is the signal. A required language can support a stack inference; "Kubernetes nice to have" is a hiring-only platform mention, not evidence of production use. Years of experience are not part of the stack.
- **Closed postings still count** — say so and date them. An older posting accepting "Go or Rust" versus a current one requiring only Go is itself information.
- Postings also carry remote and relocation policy, visa sponsorship, language requirements, equity, benefits, and whether new graduates or junior engineers are considered.

Where to look:

| Region | Boards |
|---|---|
| Japan | The company's own careers site (often Notion, Herp, or Ashby), [TokyoDev](https://www.tokyodev.com) (English-speaking roles), [Wantedly](https://www.wantedly.com), [Green](https://www.green-japan.com), [Findy](https://findy-code.io), [LAPRAS](https://lapras.com) |
| Global | LinkedIn, the company's own site, Y Combinator's job board for YC companies |

Prefer the company's own page — aggregators paraphrase, and some republish stale listings.

### 5. Founders and team

- Company `about`/`company` page for current roles and stated backgrounds.
- Long-form interviews, often only in the local language, for career history with dates.
- VC investment announcements — they state the thesis and sometimes the round structure.
- Conference and event speaker bios are surprisingly detailed.
- LinkedIn for role confirmation only.

Keep to verifiable career facts. Don't characterize people.

### 6. Funding

Build the table from the company's own release for each round, and use the round name the company itself used. Media and databases relabel rounds — pre-Series A reported as Series A is common. Use databases as leads. An outdated cumulative total belongs in `Notes` only when it purports to cover the same date or would otherwise materially mislead the reader.

### 7. Other public sources

| Category | Sites |
|---|---|
| Startup databases (Japan) | [INITIAL / Speeda Startup Info](https://initial.inc), [STARTUP DB](https://startup-db.com), [Kepple](https://kepple.co.jp) |
| Startup databases (global) | Crunchbase, PitchBook, Tracxn, CB Insights, Preqin |
| Startup media | [BRIDGE](https://thebridge.jp), Forbes JAPAN, TechCrunch, Nikkei xTECH |
| Government / program pages | [J-Startup](https://www.j-startup.go.jp), JETRO, METI program announcements, local accelerator sites |
| Corporate registry | [国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp) for legal name, corporate number, registered address and its history |
| Filings | EDINET (Japan), SEC EDGAR (US) — relevant when a partner or acquirer is listed |
| Industry media | Trade publications for the company's sector; they cover product launches national outlets skip |

Databases are useful for finding leads — a round you hadn't seen, an investor name — but confirm every figure against a primary source before it goes on the page.

### 8. Founder and company social media

Use only public professional accounts and only material relevant to the company. Place the fact according to its subject, not its source type: product announcements in `Product`, hiring statements in `Engineering`, career history in `Founder`, financing claims in `Funding`, and unresolved conflicts in `Notes`.

Label the attribution, account, post date, and URL. A founder post proves that the founder made the statement; it does not independently confirm the claim. Preserve tense and status: "plans", "targets", "exploring", and "in development" must not become current product facts. Do not use private or access-controlled content, unrelated personal activity, character inference, or personal repositories that are not clearly connected to the company.

Social posts and mutable job pages are fragile sources. Link an existing web archive when available and lawful, but do not require an archive for every source or imply that an unavailable automated fetch means the page is invalid. If a page is human-accessible but blocks automated access, record the access date and limitation. Search-result snippets alone are weak evidence and must be labelled unconfirmed.

## Publication and update workflow

Each company page is a dated research snapshot, not a continuously monitored record. The `Last updated` date is the boundary through which the page's research content was verified, not the filesystem edit date.

| Update type | Required verification | Date handling |
|---|---|---|
| Editorial-only | Check affected local links, formatting, bilingual structure, and meaning; no external-source refresh | Do not change the company page's `Last updated` |
| Targeted content update | Verify every added or changed claim, its source link, and directly dependent surrounding statements | Advance `Last updated`; synchronize or explicitly leave the translation's older sync date |
| Material refresh or first publication | Repeat the minimum search scope, verify every retained claim has support, and check every source link | Advance `Last updated` and translation sync date after both pass |

A new financing round, rename, major product or regulatory change, or broad engineering refresh normally makes the update material. Companies, source pages, and URLs may change afterward; unrelated repository edits do not require a full recheck.

When a retained source stops working: look for the official replacement URL, then an existing archive, then a source of equivalent authority. Keep an important historical claim with a clear dead-link or archive note when support remains understandable. Remove a claim when it is immaterial and no longer supportable; do not silently replace a primary source with a weaker database entry.

## Checklist before publishing

- [ ] Every number has a date and a link to the page it came from
- [ ] Round names match the company's own wording
- [ ] Technology stack items distinguish confirmed use, inference, and hiring-only mentions
- [ ] Hiring requirements are not presented as proof that a system or technology is in production
- [ ] Required and preferred technical or industry backgrounds remain separate
- [ ] Conflicts between sources are listed in `Notes`, not silently resolved
- [ ] Absence findings state the search date and reviewed public-source scope
- [ ] Source precedence matches the claim type
- [ ] Undated and mutable sources carry an `Accessed` date without implying currency
- [ ] Founder or company social posts preserve attribution and aspiration/current status
- [ ] The page applies materiality rather than reproducing every available disclosure
- [ ] Former brands, predecessors, and related legal entities are distinguished when applicable
- [ ] No evaluative language: nothing about whether the company is a good bet
- [ ] At publication, every source link opens and supports the cited statement
- [ ] `Last updated` date set
- [ ] Translations preserve the same figures, dates, and source links
- [ ] Language links work in both directions
- [ ] Each translation states its synchronization date
