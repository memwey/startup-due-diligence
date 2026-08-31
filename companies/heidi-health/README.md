# Heidi

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-31.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Heidi (`heidihealth.com`) sells an ambient AI scribe for clinicians and is extending it into what the company calls an "AI Care Partner": **Scribe** (documentation), **Evidence** (cited clinical answers), **Dictate** (system-wide voice-to-text in a desktop app) and **Remote** (a 21-gram wearable microphone). The operator is **HEIDI HEALTH TRADING PTY LTD**, ABN 84 649 783 871, Melbourne ([ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871), record extracted 2026-08-31; [Heidi Scribe Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use)). The business was previously branded **Oscer** ([TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/); 2023-10-25).

- Latest round: **US$65M Series B**, announced 2025-10-05, led by **Point72 Private Investments**, at a **US$465M** post-money valuation, taking total raised to **US$96.6M** ([Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b); [TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/)). No later round was found in the sources reviewed on 2026-08-31 — see `Funding`.
- Company-stated scale as of 2026-08-31: **2.5M patient sessions per week**, **110 languages**, **190 countries**, **200+ specialties**, **US$96.6M raised**, **400+ employees** on the media page and **500+** on the careers page ([Media Room](https://www.heidihealth.com/en-au/about-us/media), [Careers](https://www.heidihealth.com/en-au/careers)) — the two headcounts conflict, see `Notes`.
- **85 open roles** were listed on the company's Ashby job board on 2026-08-31 — 24 in Engineering, 35 in GTM — concentrated in Melbourne (27), London (16), New York (9), San Francisco (7) and Sydney (6) ([Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)).
- Engineering, as described in those postings: **Python** services with **MongoDB and Redis**, **React/Next.js** frontends, a **Tauri + Rust** cross-platform desktop app, **Kubernetes + Terraform** across **AWS, GCP and Azure**, and an in-house deterministic **RPA engine** for EHRs without APIs — see `Engineering`.
- Named enterprise deployments include **Beth Israel Lahey Health** ("6,000+ providers across 14 hospitals and 175 primary care practices") and the NHS **Modality Partnership** ("360+ GPs … 53 sites") ([Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise); accessed 2026-08-31).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Heidi — "The AI Care Partner for clinicians" | [heidihealth.com/en-au](https://www.heidihealth.com/en-au); accessed 2026-08-31 |
| Australian legal entity | HEIDI HEALTH TRADING PTY LTD; ABN 84 649 783 871; ACN 649 783 871; Australian Private Company; ABN and GST active from 2021-04-28; main business location VIC 3000 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871); record extracted 2026-08-31 |
| Registered business name | "HEIDI HEALTH", registered from 2022-05-17 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871) |
| Contracting entity in the product terms | "Heidi Health Trading Pty Ltd." | [Heidi Scribe Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use); accessed 2026-08-31 |
| Address in the privacy policy | Level 30, 360 Elizabeth Street, Melbourne VIC 3000 | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Other group entities | Heidi Health Ltd (United Kingdom); Heidi Health Canada Inc (Ontario, Canada); Heidi Health Corp (Delaware, USA); Oscer Enterprises Pty Limited (Australia) | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Predecessor entity | OSCER ENTERPRISES PTY LTD; ABN 57 620 824 900; ACN 620 824 900; ABN active from 2017-08-01; business name "Oscer" from 2021-07-27; VIC 3000 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=57620824900); record extracted 2026-08-31 |
| Founders | Dr. Thomas Kelly (Co-Founder & CEO), Yu Liu (Co-Founder & CTO), Waleed Mussa (Co-Founder & CFO) | [Careers](https://www.heidihealth.com/en-au/careers), [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Founding year | Stated as 2021 by TechCrunch; as 2019 by other secondary sources; the predecessor entity's ABN dates from 2017 — see `Inconsistencies across sources` | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/), [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=57620824900) |
| Headcount | "400+ employees around the world" (Media Room); "500+ Heidis" (Careers) | [Media Room](https://www.heidihealth.com/en-au/about-us/media), [Careers](https://www.heidihealth.com/en-au/careers); both accessed 2026-08-31 |
| Offices | "8 Offices across AU, US, UK, Canada & Singapore" — Melbourne, Sydney, Brisbane, New York, San Francisco, London, Toronto, Singapore | [Careers](https://www.heidihealth.com/en-au/careers); accessed 2026-08-31 |
| Total raised | "USD 96.6m raised to date" | [Media Room](https://www.heidihealth.com/en-au/about-us/media); accessed 2026-08-31 |
| Investors named by the company | Point72 Private Investments, Blackbird, Headline, Latitude (Phoenix Court's growth fund), Possible Ventures, Archangel | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Weekly volume | "2.5 million patient sessions supported each week"; the AU homepage showed a live counter reading 2,740,338 patient visits this week | [Media Room](https://www.heidihealth.com/en-au/about-us/media), [heidihealth.com/en-au](https://www.heidihealth.com/en-au); read 2026-08-31 |
| Compliance claims | "NHS, HIPAA, GDPR, and Australian Privacy Principles … SOC2 and ISO27001" | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Trust centre | Hosted on Vanta at `trust.heidihealth.com` | [trust.heidihealth.com](https://trust.heidihealth.com/); read 2026-08-31 |
| Hiring system | Ashby, board slug `heidihealth.com.au`; 85 live postings on 2026-08-31 | [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| Site locales | 22 locale paths: `en-au`, `en-us`, `en-gb`, `en-ca`, `en-nz`, `en-ie`, `en-sg`, `en-hk`, `en-my`, `en-za`, `de-de`, `de-ch`, `de-be`, `de-lu`, `fr-fr`, `fr-ca`, `fr-ch`, `fr-be`, `fr-lu`, `es-es`, `es-mx`, `es-ar`, `it-it`, `ja-jp` | [heidihealth.com/en-au](https://www.heidihealth.com/en-au) footer; read 2026-08-31 |
| Public social accounts | X `@tryheidi` (the site's `twitter:site` meta tag reads `@heidi_health`), LinkedIn `heidihealth`, Instagram `tryheidi`, Facebook `tryheidi`, YouTube | [heidihealth.com/en-au](https://www.heidihealth.com/en-au); read 2026-08-31 |

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Heidi | Current public brand | Global; business name registered in Australia from 2022-05-17 | Brand used on all product surfaces | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871), [heidihealth.com/en-au](https://www.heidihealth.com/en-au) |
| HEIDI HEALTH TRADING PTY LTD | Legal entity | Australia (VIC), ABN active from 2021-04-28 | Named as the contracting party in the Scribe Terms of Use and as the data controller in the privacy policy | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871), [Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use) |
| OSCER ENTERPRISES PTY LTD | Legal entity | Australia (VIC), ABN active from 2017-08-01 | Listed among the Heidi group entities in the privacy policy; no ownership statement published | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=57620824900), [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Oscer | Former brand | Australia; business name registered 2021-07-27 | "Formerly called Oscer" — the same business, under Kelly, Mussa and Liu | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/), [Blackbird portfolio](https://www.blackbird.vc/portfolio/heidi-health) |
| Heidi Health Ltd | Related entity | United Kingdom | Listed as a group entity in the privacy policy | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Heidi Health Canada Inc | Related entity | Ontario, Canada | Listed as a group entity in the privacy policy | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Heidi Health Corp | Related entity | Delaware, USA | Listed as a group entity in the privacy policy | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| AutoMedica | Acquired company | United Kingdom; announced 2026-02-24 | "AutoMedica's evidence-led AI framework and regulatory relationships will underpin Heidi's Evidence capabilities"; terms not disclosed | [Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence) |

Blackbird's portfolio page records the firm investing at seed stage in **2021**, when the company was still Oscer and was "changing the way students learn clinical reasoning with innovative tools like AI virtual patients" ([Blackbird](https://www.blackbird.vc/portfolio/heidi-health); accessed 2026-08-31). Ownership relationships between the Australian, UK, Canadian and US entities are not published in any source reviewed.

---

## Product

### What it is and its feature areas

- **Scribe** — the ambient documentation product: "Heidi captures the encounter as it happens and writes notes that sound like you, not a generic template", with pre-consult preparation, transcription "in 110+ languages", generated referrals and handouts, one-click send to the EHR, and auto-applied codes and tasks ([Scribe](https://www.heidihealth.com/en-au/scribe); accessed 2026-08-31).
- **Evidence** — clinical answers with citations: "Open the citation behind any answer and read the source yourself", validated calculators that "show their working", per-user and per-team source prioritisation, and self-logging CPD ([Evidence](https://www.heidihealth.com/en-au/evidence); accessed 2026-08-31). Launched 2026-02-24 with named content partners **HealthPathways, EMGuidance, MIMS, Vidal, NICE and BMJ Group** ([Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence)).
- **Dictate** — press-and-hold dictation inside the desktop app that types into "your EHR, a referral letter, Outlook, any application on your computer", with "clinical vocabulary built in more than 90 languages" ([Dictate](https://www.heidihealth.com/en-au/product/dictate); accessed 2026-08-31). The desktop app was on version **2.9.0, released 2026-08-31**, for Windows (.EXE/.MSI) and macOS (Apple Silicon and Intel).
- **Remote** — hardware: "a 21-gram wearable mic, fully offline, with on-device encryption", clip-on, works online and offline, paired to a device over "an encrypted wireless connection", with audio "encrypted at rest on Heidi Remote and … automatically deleted once synchronised" ([Scribe](https://www.heidihealth.com/en-au/scribe), [Hardware](https://www.heidihealth.com/en-au/hardware); accessed 2026-08-31). Launched March 2026 ([Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/); 2026-03-24).
- **Comms** — "an AI partner for healthcare teams to coordinate patient communications across calls, bookings, reminders and follow-ups", announced alongside Evidence in February 2026 ([Heidi Progress Notes — "Evidence, Comms, and more customisations"](https://www.heidihealth.com/en-au/changelog); 2026-02-25). No dedicated Comms product page exists in the site navigation — `/en-us/comms` returns the catch-all page (checked 2026-08-31).
- **Templates** — a public template library and "Template Community" ([Templates](https://www.heidihealth.com/en-au/templates)).
- **Integrations** — a job posting describes the integration surface as "SMART on FHIR launches inside the chart, structured write-back into Epic, Cerner, Athena, MEDITECH Expanse, Veradigm, Best Practice. HL7 ADT feeds for patient demographics", plus an "Integration Marketplace … being rebuilt now" ([Technical Program Manager, Integrations](https://jobs.ashbyhq.com/heidihealth.com.au/3ec2c152-3983-4471-834a-60c8e1f6c993); published 2026-08-04).

Published minimum client requirements: Windows 10 or later / macOS 13.1 or later, latest Chromium-based browsers (Chrome, Edge), Android 8.0, iOS 17.0, 10 Mbps bandwidth minimum and 20 Mbps recommended ([System Requirements](https://www.heidihealth.com/en-au/system-requirements); accessed 2026-08-31).

### Commercialization

Four published tiers — **Free**, **Clinician**, **Practice** and an Enterprise "Talk to us" tier — billed "per user / month" with monthly and yearly options and a 14-day trial on the paid individual and team plans. Prices are rendered client-side per locale and were not present in the served HTML on 2026-08-31; the plan comparison is published in full ([Pricing](https://www.heidihealth.com/en-au/pricing); read 2026-08-31).

Feature gating as published: Free includes "Unlimited transcription", standard templates, task management, and limited Ask Heidi, advanced templates and patient/session linking. Clinician adds document and session sharing, coding, session status, free assistant users, preferred and premium evidence sources, a personal evidence library and evidence inside patient visits. Practice adds team template sharing, 1:1 template configuration, org-wide evidence library, centralised billing, priority support, team management, guided onboarding, dedicated customer success and SSO. "EHR integration add-on" is listed as a paid add-on on the Practice and Enterprise columns; "Service availability" and "Custom terms & hosting" are Enterprise-only ([Pricing](https://www.heidihealth.com/en-au/pricing)).

### Reported scale over time

| Date | Figure as stated | Source |
|---|---|---|
| 2023-10-25 | "more than 100 general practitioners in about 30 clinics" in Australia | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/) |
| 2024-02 | Scribe launch | [Heidi — Series A follow-on](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) |
| 2025-03-06 | "over 20 million patient interactions globally" since launch; "over 1 million consults every week" as of March 2025; five countries | [Heidi — Series A follow-on](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) |
| 2025-10-05 | "73 million patient visits" and "18 million hours" in 18 months; "over two million patient visits each week"; "110 languages"; "116 countries"; "200+ specialties" | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b) |
| 2026-02-24 | "over 100 million clinical interactions supported globally"; "2.4 million consults per week"; "110 languages from 190 countries" | [Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence) |
| 2026-03-24 | "118 million clinical sessions" cumulatively; "2.5 million patient interactions weekly"; UK: "1 in 2 GPs", "1.5 million monthly patient consultations" | [Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/) |
| 2026-03-10 | "more than 2.7 million visits a week" | [R1 RCM newsroom](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations) |
| 2026-08-31 | "2.5 million patient sessions supported each week", "190 countries", "400+ employees"; careers page: "47M hours saved since launch", "500+"; enterprise page: "62.9M hours saved by clinicians since launch", "61.7% Activation Rate (Enterprise)", "200+ Specialties Supported" | [Media Room](https://www.heidihealth.com/en-au/about-us/media), [Careers](https://www.heidihealth.com/en-au/careers), [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) |

### Announced customers and partners

| Customer / partner | What is claimed | Date | Source |
|---|---|---|---|
| Beth Israel Lahey Health (USA) | "89% note satisfaction, 74% less after-hours admin. 6,000+ providers across 14 hospitals and 175 primary care practices" | accessed 2026-08-31 | [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) |
| Modality Partnership (NHS, UK) | "360+ GPs, largest ambient AI rollout in UK primary care … 53 sites, benefiting almost half a million patients" | accessed 2026-08-31 | [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) |
| ForHealth (AU), Tamaki Health (NZ) | Named as "the largest multi-disciplinary healthcare network in Australia" and "the largest primary healthcare provider in New Zealand" | 2025-03-06 | [Heidi — Series A follow-on](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) |
| OneCare Vermont (USA) | Partnership "to reduce administrative burden for primary care practices across Vermont" | 2025-09-25 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Vim (USA) | "Partner to Accelerate Innovation at the Point of Care" | 2025-10-15 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| R1 RCM (USA) | Strategic partnership: Heidi users get "payer policy information, prior authorization rules and insurance eligibility information at the point of care"; notes "optimized to ensure accurate coding and billing" | 2026-03-10 | [R1 RCM newsroom](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations) |
| The Royal Children's Hospital (AU) | Deployment "so paediatricians can focus on patients, not paperwork" | 2026-06-03 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| QHR Technologies / Accuro EMR (Canada) | Integration of "AI documentation into Accuro EMR" | 2026-06-16 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Five Ontario pilots (Canada) | "333 active clinicians", "111,770 patient visits", three months each, "13 minutes saved per visit", "25,098+ clinical hours" valued at "$2.51 million"; Guelph Wellington OHT, Mississauga Health PCN, Kawartha Lakes OHT, Ottawa Institute of CBT, South Georgian Bay Provider Care Network | 2026-07-22 | [Newswire release](https://www.newswire.ca/news-releases/more-patients-less-paperwork-heidi-s-ai-scribe-returns-an-estimated-2-51m-in-clinical-time-893435988.html), [Canadian Healthcare Technology](https://www.canhealth.com/2026/07/22/heidi-ai-scribes-save-13-minutes-per-visit/) |
| Logos on the homepage | Bupa, University of Queensland, The Ohio State University, Beth Israel Lahey Health, Swiss Medical Network, Eucalyptus, Greencross Vets, QLD Children's Hospital, Sue Ryder, Tamaki Health | accessed 2026-08-31 | [heidihealth.com](https://www.heidihealth.com/) |

Two adoption claims appear in the enterprise FAQ: "60-80% adoption within the first month, far exceeding just 20-40% average seen with other AI scribes", and "My Emergency Doctor … achieving 77% adoption within just 3 weeks" ([Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise); accessed 2026-08-31). Both are the company's own framing.

### Stated plans

- Series B use of funds: "expand headcount, office locations, and local support in USA, UK, and Canada", and "build adoption in France, Spain, Germany, Ireland, South Africa, Singapore, and Hong Kong" ([Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b); 2025-10-05).
- Mission statements repeated across postings and releases: "halve the time it takes to deliver world-class care" (2026-06 postings) and "double the world's healthcare capacity and strengthen the human connection at its heart" (2026-08 postings) ([Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837), [Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)).
- A "New Bets" squad exists in London for zero-to-one products: "Scribe already powers millions of patient visits a week, and Evidence and Remote are scaling behind it. Your job … is to build what comes next" ([Backend Software Engineer - New Bets](https://jobs.ashbyhq.com/heidihealth.com.au/68074198-b723-4db9-af97-5f33392593f4); published 2026-08-21).

---

## Founder

Three co-founders are named on the company's own pages ([Careers](https://www.heidihealth.com/en-au/careers), [Media Room](https://www.heidihealth.com/en-au/about-us/media); accessed 2026-08-31):

| Name | Title | Career facts from sources |
|---|---|---|
| Dr. Thomas Kelly | Co-Founder & CEO | Described in the company's own release as "CEO and co-founder of Heidi, and former vascular surgical resident" ([Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care); 2025-03-06). TechCrunch describes him as a vascular surgeon who founded the company in 2021 ([TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)); Blackbird's portfolio page describes his motivation as a junior doctor seeing "incorrect, delayed or missed diagnoses" ([Blackbird](https://www.blackbird.vc/portfolio/heidi-health)). |
| Yu Liu | Co-Founder & CTO | Named as co-founder on the company's pages and in TechCrunch's 2023 report. |
| Waleed Mussa | Co-Founder & CFO | Named as co-founder on the company's pages and in TechCrunch's 2023 report. |

Kelly's stated reason for starting the company, in his own words: "That's why I founded Heidi – to free doctors from non-clinical work so they can focus on their patients and enjoy fulfilling careers in medicine" ([Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care); 2025-03-06).

### Selected leadership

The company's website publishes no leadership page beyond the three founders — `/about-us/people` serves the same content as `/careers` (checked 2026-08-31). Other executives are named in the company's own release and job postings:

| Name | Title | Prior role as stated | Source |
|---|---|---|---|
| Paul Williamson | Chief Revenue Officer | ex-Plaid Head of Revenue | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b); 2025-10-05 |
| Dr. Simon Kos | Chief Medical Officer | ex-Microsoft Chief Medical Officer | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b); 2025-10-05 |
| Jessie Young | President, North America | Not stated | [Head of Engineering, North America](https://jobs.ashbyhq.com/heidihealth.com.au/adfea4ea-f501-4513-9b59-45b12774ee1d); published 2026-06-16 |

Functions the job board shows the company staffing, by department: GTM (35 roles), Engineering (24), Product (11), Marketing (6), Legal/Regulatory & Compliance (2), People (1), Customer Experience (1), plus 5 "Expression of Interest" postings ([Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true); read 2026-08-31). Engineering sub-teams named on the postings: Engineering, Engineering R&D, Engineering Service Delivery, Clinical AI R&D, Data and IT.

---

## Funding

| Date | Round | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2021 (year only) | Seed | A$5M | Blackbird (led) | — | [Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/), [Blackbird](https://www.blackbird.vc/portfolio/heidi-health) |
| 2023-10-25 | Series A | A$10M (≈US$6.4M) | Blackbird (led), Hostplus, Vesta, Wormhole Capital, Archangel Ventures, Possible Ventures, Daniel Ventures | A$15M | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/) |
| 2025-03-06 | "Series A follow-on" / "top-up" | US$16.6M (reported as A$26.8M) | Headline (led), Local Globe, Anthology (Menlo Ventures and Anthropic), Blackbird, HESTA, Possible Ventures, Archangel Ventures | A$36.8M | [Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care), [Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/) |
| 2025-10-05 | Series B | US$65M (reported as A$98M) at a US$465M (A$704M) valuation | Point72 Private Investments (led), Blackbird, Headline, Latitude (Phoenix Court's growth fund) | US$96.6M | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b), [TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/), [SmartCompany](https://www.smartcompany.com.au/startupsmart/heidi-health-98-million-raise-valuation-704-million/) |

Plain facts that do not fit the table:

- The company itself calls the March 2025 round a "Series A follow-on investment"; Startup Daily calls it a "top-up" to the October 2023 Series A ([Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care), [Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/)).
- **Anthology**, described in Heidi's own release as a vehicle of "Menlo Ventures and Anthropic", participated in the March 2025 round; it does not appear in the investor list the company publishes on its Media Room today ([Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care), [Media Room](https://www.heidihealth.com/en-au/about-us/media)).
- **HESTA**, an Australian superannuation fund, and **Hostplus**, another, appear in the 2023 and 2025 rounds respectively but not in the current investor list ([TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/), [Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)).
- The Series B was announced alongside two executive hires (Williamson, Kos) rather than a product launch ([Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)).
- The **AutoMedica** acquisition (announced 2026-02-24) is the only acquisition found; terms were not disclosed ([Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence)).
- No round after the October 2025 Series B was found in the sources reviewed on 2026-08-31. Job postings published in August 2026 still say "Backed by nearly $100 million in funding" ([Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48)).

---

## Engineering

### Technology stack and platforms

**Confirmed by observable public assets** (headers and pages read 2026-08-31):

- **Next.js on Vercel** for the marketing site (`server: Vercel`, `x-powered-by: Next.js`), the status page (`status.heidihealth.com`) and the web application (`scribe.heidihealth.com`).
- **Sanity** as the CMS (`cdn.sanity.io` asset host on marketing pages).
- **Intercom** for support and help centre (`support.heidihealth.com`, Cloudflare-fronted); **Vanta** for the trust centre; **Ashby** for recruiting; **Google Tag Manager** on the site.
- **Cross-platform desktop app** for Windows (.EXE and .MSI) and macOS (Apple Silicon and Intel builds), version 2.9.0 released 2026-08-31, plus Android and iOS clients ([Dictate](https://www.heidihealth.com/en-au/product/dictate), [System Requirements](https://www.heidihealth.com/en-au/system-requirements)).

**Described in current job postings as what the team builds and runs** (hiring evidence, not independent confirmation):

- **Desktop**: "Heidi's cross-platform desktop applications using Tauri, Rust, and Next.js, shipping production-grade software on macOS and Windows (Linux a plus)", with "high-performance Rust components powering real-time audio capture, transcription pipelines, local state management" ([Senior Software Engineer - Desktop App](https://jobs.ashbyhq.com/heidihealth.com.au/738c99ed-0a85-467f-821c-1beae5565148); 2026-08-26).
- **Backend**: "high-performance backend systems using Python"; "Solid experience with MongoDB and Redis for data management"; "message queue systems for real-time data processing" ([Senior Backend Engineer - UK](https://jobs.ashbyhq.com/heidihealth.com.au/76723d60-69ac-4368-a97d-4ce125d3c822); 2026-06-05). A newer posting pairs "Python services" with "React/TypeScript front ends" ([Backend Software Engineer - New Bets](https://jobs.ashbyhq.com/heidihealth.com.au/68074198-b723-4db9-af97-5f33392593f4); 2026-08-21).
- **Frontend**: "Advanced proficiency with React and Next.js (SSR/SSG/ISR…)", monorepo tooling ("Turborepo, Nx, Bazel"), design systems and Storybook, micro-frontends and module federation, TDD/BDD with "Playwright, Cucumber" ([Staff Frontend Solution Architect](https://jobs.ashbyhq.com/heidihealth.com.au/c6b7c2b6-5b9b-47b4-8e65-ba866225c95f); 2026-08-05).
- **Cloud, three providers, by role**: GCP ("Compute Engine, managed instance groups, GKE… VPCs, peering, Private Service Connect, Cloud DNS"), Azure ("preferably Azure"), and AWS ("Strong experience operating cloud infrastructure at scale (AWS preferred)") ([Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48), [Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837), [Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)).
- **Platform**: Kubernetes and containers, Terraform and Helm, Docker, GitOps and monorepo build systems, canary/blue-green deployments, "MongoDB Atlas, Redis, or Postgres cloud deployments" as a nice-to-have ([Senior Software Engineer - Developer Experience](https://jobs.ashbyhq.com/heidihealth.com.au/99ef4d45-fcaf-4d53-b2db-9acd8a740be3); 2026-05-07).
- **Observability**: Datadog, Prometheus, Grafana, ELK; SLOs and error budgets ([Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)).
- **Models**: "our ASR, note generation, Evidence, and Dictate models" are owned by an in-house model team; the stated goal for enterprise work is "better economics than relying solely on closed-source models such as Claude, Gemini, and OpenAI", via fine-tuning "open-weight language models" and "cloud or on-prem deployment" ([Senior LLMOps Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/4f287875-c13f-483c-af50-d48f7d637d73), [Senior AI Models Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/f2a33fd0-e4bc-4e0b-84e3-c136a32af0ab)). TechCrunch reported a "model-agnostic approach, building on proprietary models and external systems like Google Gemini" ([TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/); 2025-10-05).
- **Localisation**: Crowdin or Smartling integrated into release pipelines; XLIFF/JSON/XML content formats; "AI-assisted translation pipelines … with human-in-the-loop review" ([Senior Localisation Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/ea5b66c6-c1d5-48e5-b985-129fc01d02cc); 2026-08-19).
- **AI-assisted development is an explicit expectation**: "Prototype with AI-assisted tools like Claude Code and Cursor to ship in days, then harden what works into production-grade code"; "You build with AI tools (Cursor, Claude Code, whatever ships faster) and can show what you've made with them" ([Senior Software Engineer - RPA](https://jobs.ashbyhq.com/heidihealth.com.au/797ab212-3cc6-4dd0-8646-908241fc8f34), [Backend Software Engineer - New Bets](https://jobs.ashbyhq.com/heidihealth.com.au/68074198-b723-4db9-af97-5f33392593f4)).

**Mentioned only as candidate requirements or preferences**, not established as in production: Ansible, GitHub Advanced Security, Snyk, Trivy, service mesh, Karpenter, Linkerd, dbt, Databricks, Looker, Tableau, Omni, Mixpanel, Amplitude, Statsig, C#, FlaUI, Selenium.

### Systems

- **Ambient transcription and note generation** — real-time audio capture, transcription and structured note generation across web, desktop and mobile ([Scribe](https://www.heidihealth.com/en-au/scribe)).
- **In-house RPA engine for EHRs without APIs** — "Most EHRs don't offer us an API… we build our own automation engine that works the EHR the way a person would: reading the interface, mapping the fields and pushing structured data into the record." The posting states the vendor-platform decision explicitly: "We looked hard at the vendor RPA platforms and decided against building on someone else's engine as they were either too slow, too fragile for patient data, and we weren't comfortable that they could guarantee determinism… AI helps us set automations up fast; deterministic code is what runs in production." Components named: "UI-automation flows (accessibility-tree mapping, templated field entry, structured write-back)", patient-matching and validation logic, work queues, retries and exception handling ([Senior Software Engineer - RPA](https://jobs.ashbyhq.com/heidihealth.com.au/797ab212-3cc6-4dd0-8646-908241fc8f34); 2026-08-19).
- **Integration platform** — a shared integration framework plus a customer-facing Integration Marketplace spanning Scribe, Comms and Evidence; SMART on FHIR, structured EHR write-back, HL7 ADT feeds, pre-charting from appointment data ([Technical Program Manager, Integrations](https://jobs.ashbyhq.com/heidihealth.com.au/3ec2c152-3983-4471-834a-60c8e1f6c993); 2026-08-04).
- **Model platform and LLMOps** — a deployment health dashboard, "complete session-to-model lineage", distributed tracing across multi-step LLM pipelines, a feedback flywheel from Intercom tickets and CSAT into training data, and "per-model P&L… revenue against inference cost for every model deployment" ([Senior LLMOps Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/4f287875-c13f-483c-af50-d48f7d637d73); 2026-08-10).
- **Platform/SRE** — a core team that "owns production": Kubernetes clusters, cloud infrastructure, on-call, incident response, SLOs and capacity planning ([Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8); 2026-08-04).
- **Developer platform** — company-wide build systems, common CI/CD pipelines, Docker images, IDE extensions and CLI tools, environment scaffolds, secrets management and automated provisioning ([Senior Software Engineer - Developer Experience](https://jobs.ashbyhq.com/heidihealth.com.au/99ef4d45-fcaf-4d53-b2db-9acd8a740be3); 2026-05-07).
- **Forward-deployed engineering** — a named motion: "EMR integrations, SSO, SCIM provisioning, data pipelines, and security configuration" for enterprise customers, with engineers embedded on site ([Forward Deployed Engineer - UK](https://jobs.ashbyhq.com/heidihealth.com.au/02ad14b7-a9bb-45e3-a90f-631179f86d8d); 2026-06-05).
- **Localisation platform** — pipelines and tooling to ship 110 languages across web and mobile ([Senior Localisation Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/ea5b66c6-c1d5-48e5-b985-129fc01d02cc)).
- **Design controls and quality system** — a role inside Engineering but reporting into Legal & Regulatory Affairs, to implement "IEC 62304 (software lifecycle), ISO 14971 (risk management), and ISO 13485 (quality management systems) within an agile, iterative environment" and to "Support external ISO 13485 and Notified Body audits" ([Design Quality Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/31e03395-c3a1-46c3-955c-ed9f50c2e8d7); 2026-08-12).

### Technical background sought

**Required**, by role family ([Ashby job board](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true); read 2026-08-31):

- SRE and platform: "7+ years in SRE, DevOps, platform, or operations-heavy engineering roles, including experience formally leading or managing a team"; on-call and live incident debugging; owning SLOs, error budgets and capacity planning "not just familiarity with the concepts". The GCP platform role asks for "3–7+ years in cloud or platform engineering" with hands-on production GCP.
- Backend: "5+ years of backend development experience", API design including security and versioning, third-party integrations, data modelling.
- Desktop: "5+ years", systems-level programming ("Rust preferred; C++ or Go acceptable"), desktop app packaging and updates.
- Frontend: "6+ years", scaling frontend architecture across multiple teams in high-growth SaaS.
- LLMOps: "the last 2–3 years hands-on in an LLMOps role, building the observability, tracing, evaluation, and feedback systems around production LLMs and owning them through real incidents", explicitly sourced from "an AI company operating at or ahead of Heidi's maturity, most likely in the US or China, where LLMOps practice runs deepest".
- RPA: production UI automation experience ("Playwright, accessibility-tree frameworks like FlaUI, or an RPA platform you've since outgrown"), Python primary, "deterministic-systems instincts: queues, retries, idempotency and exception handling".
- Forward deployed: "4+ years in a forward deploy, implementation engineering, or customer-facing technical role"; "REST APIs, SAML/OIDC, SCIM, and ideally FHIR/HL7".
- Zero-to-one: "3+ years shipping production software", full-stack Python + React/TypeScript, "prompting, retrieval, embeddings, evaluation".

**Preferred**: healthtech, startup or regulated-industry experience; multi-cloud (AWS + Azure); GKE/Kubernetes in production; "Knowledge of ISO 27001 / HIPAA / APRA-style compliance"; a broader backend, data-platform or ML-infrastructure foundation before LLMOps; C# or TypeScript alongside Python for the RPA role.

### Industry domain

- **Clinical documentation and coding.** A dedicated Clinical Coding Specialist role requires "HIMAA certification in Clinical Coding or equivalent", "Expert-level knowledge of ICD-10-AM/ACHI and Australian Coding Standards (ACS)", AR-DRG classification, and MBS/Medicare Australia billing requirements, working "directly with our engineering team to embed your expertise into automated systems" ([Clinical Coding Specialist (Australia)](https://jobs.ashbyhq.com/heidihealth.com.au/0ac1835a-8faa-446c-b0b2-a581ca21e50c); 2026-06-01).
- **EHR/EMR reality.** The integrations role expects candidates to "understand how a real EMR write-back actually works — encounter IDs, appointment IDs, patient context, addendum vs edit, side-by-side comparison, sectional mapping" across Epic, Cerner, Athena, MEDITECH Expanse, Veradigm and Best Practice ([Technical Program Manager, Integrations](https://jobs.ashbyhq.com/heidihealth.com.au/3ec2c152-3983-4471-834a-60c8e1f6c993)).
- **Medical-device software regulation.** IEC 62304, ISO 14971, ISO 13485 and "SaMD Experience: Prior experience working on Software as a Medical Device (SaMD)" are required for the Design Quality Engineer role ([Design Quality Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/31e03395-c3a1-46c3-955c-ed9f50c2e8d7)).
- **Regional health-data compliance.** The company publishes per-region compliance pages: UK (DCB0129, DTAC, DSPT, Cyber Essentials, ICO registration, Data Protection Act; "all our data is locally hosted within the UK"), HIPAA (BAAs offered to covered entities; "all our data is locally hosted within the United States"), plus Canada, GDPR and Australian Privacy Principles pages ([Compliance — UK](https://www.heidihealth.com/en-au/compliance/uk), [Compliance — HIPAA](https://www.heidihealth.com/en-au/compliance/hipaa); accessed 2026-08-31). The privacy policy states "Data localization solutions for customers located in Australia, Canada, US, UK and EU" ([Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy)).
- **Data handling claims.** The safety page states "As soon as Heidi transcribes, the audio disappears" and "Heidi doesn't use any of your data to train our AI"; the privacy policy states "No patient data is used to train, develop, or improve any of our AI models" for Scribe, while for Evidence "Queries may be reviewed and used in de-identified form to improve the platform, but PHI will not be used for model training" ([Safety](https://www.heidihealth.com/en-au/safety), [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Office policy | "Flexible hybrid working environment, with **3 days in the office**" in Melbourne/Sydney postings; the careers page says only "Work where you do your best thinking" | [Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48), [Careers](https://www.heidihealth.com/en-au/careers) |
| One role explicitly in-office | "This role is in-office in San Francisco. We believe in the energy and focus of being in the room together." | [Head of Engineering, North America](https://jobs.ashbyhq.com/heidihealth.com.au/adfea4ea-f501-4513-9b59-45b12774ee1d) |
| Remote roles | 2 of 85 postings are listed as "Remote" (both US-facing); the rest name a city | [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| Timezone expectation | "You'll be working across a significant timezone gap with our product and engineering teams in Australia" | [Head of Engineering, North America](https://jobs.ashbyhq.com/heidihealth.com.au/adfea4ea-f501-4513-9b59-45b12774ee1d) |
| Work from anywhere | "Work from anywhere for up to 1 month" | [Careers](https://www.heidihealth.com/en-au/careers) |
| Parental leave | "26 weeks for primary carers and 18 weeks for secondary carers, globally. Your equity continues to vest throughout." | [Careers](https://www.heidihealth.com/en-au/careers) |
| Clinical leave | "10 days per year to help our clinicians maintain accreditation… Available where ongoing accreditation is required." | [Careers](https://www.heidihealth.com/en-au/careers) |
| IVF / fertility | "A one-time direct payment to support employees through IVF, egg freezing or sperm freezing" | [Careers](https://www.heidihealth.com/en-au/careers) |
| Learning budget | "$1,000 per year" on the careers page; "$500 per annum" in the job postings — see `Notes` | [Careers](https://www.heidihealth.com/en-au/careers), [Senior Product Analyst](https://jobs.ashbyhq.com/heidihealth.com.au/5d352f63-74c2-458c-b40d-0666881f263f) |
| Home office | "A one-off $500" | [Careers](https://www.heidihealth.com/en-au/careers) |
| Gym | "Special corporate rates at Anytime Fitness in Melbourne, Sydney tbc"; an earlier posting says "Discounted corporate gym memberships" | [Senior Product Analyst](https://jobs.ashbyhq.com/heidihealth.com.au/5d352f63-74c2-458c-b40d-0666881f263f), [Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837) |
| Equity | "Become an owner, with shares (equity) in the company"; "Equity from day one" | [Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48), [Forward Deployed Engineer - UK](https://jobs.ashbyhq.com/heidihealth.com.au/02ad14b7-a9bb-45e3-a90f-631179f86d8d) |
| Published salary bands | 13 of 85 postings publish a band, all US or Sydney roles. Engineering: Pre-sales Solutions Engineer - US (Remote) $160K–$200K + equity. Product: Senior Product Designer (SF) $170K–$200K; Deployed PM, Health Systems (SF and Sydney) $170K–$220K; Head of Implementation (SF) $180K–$250K; Head of Product, North America (SF) $255K–$300K. No band is published for any Australian or UK engineering role. | [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true); read 2026-08-31 |
| Hiring process | Five stages: recruiter chat, behavioural interviews, "Live Challenge — a practical assignment on a real problem you could tackle in-role", final interviews with senior staff, offer | [Careers](https://www.heidihealth.com/en-au/careers) |
| Juniors and interns | One intern posting (Commercial Specialist, Melbourne) and an "Expression of Interest — Heidi Entry Program" (Melbourne); engineering postings ask for 3+ to 7+ years | [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| Working language | All 85 postings and all product surfaces reviewed are in English; no language policy is published | [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| Stated expectation about pace | "We achieve in 6 months what it takes our competitors 4 years to do" (2026-06 posting); "Ship, measure, go again. A button today, a workflow tomorrow. More iterations beat better planning." (2026-08 postings) | [Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837), [Senior AI Models Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/f2a33fd0-e4bc-4e0b-84e3-c136a32af0ab) |

---

## Notes

### Not publicly disclosed

Searched on 2026-08-31 across `heidihealth.com` (all locale paths reached from the AU footer, its `robots.txt` and sitemap index), the Ashby job board and its API, `trust.heidihealth.com`, `support.heidihealth.com`, `status.heidihealth.com`, ABN Lookup, the GitHub API, the npm registry, and English web search:

- **Revenue, ARR or any financial figure.** No source reviewed publishes revenue, gross margin, burn or customer contract values.
- **An engineering blog or any technical writing.** The blog is product, SEO and clinician-education content; no post describes model architecture, evaluation methodology or the accuracy claims' basis.
- **Open-source presence.** The GitHub organisation `Heidi-Health` exists (created 2024-07-26, updated 2024-10-14) with **0 public repositories**, no description, website, email or location; `heidihealth`, `heidiai`, `tryheidi`, `heidi-ai`, `oscer` and `oscerhealth` are not GitHub organisations; a GitHub user search for "heidihealth" returns 0 results; no first-party npm package was found ([GitHub API](https://api.github.com/orgs/heidi-health); read 2026-08-31).
- **Salary bands for Australian and UK roles.** All 13 published bands are for US roles plus two Sydney product roles.
- **The contents of the Vanta trust centre.** The page renders client-side and returned no certification list, subprocessor list or document index to a non-browser client; certification claims below come from the marketing pages instead ([trust.heidihealth.com](https://trust.heidihealth.com/); read 2026-08-31).
- **Cloud provider and data-residency detail per region.** The privacy policy says "Data localization solutions for customers located in Australia, Canada, US, UK and EU" and the compliance pages say data is "locally hosted" in the UK and US, but no source names which cloud provider hosts which region. Job postings name AWS, GCP and Azure in different roles.
- **Named subprocessors.** The privacy policy refers to "third party service providers", "evidence source partners and content licensors" and "third-party analytics tools" without naming them.
- **Data retention periods.** "We only keep your information for as long as you want it or are lawfully required to keep it" — no period is stated ([Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy)).
- **Regulatory clearance as a medical device.** No TGA (ARTG), FDA or MHRA clearance or registration is claimed on the safety or compliance pages; the company's own framing is compliance with privacy, security and NHS assessment frameworks. A TGA ARTG query did not complete on 2026-08-31, so no ARTG conclusion is drawn either way. The Design Quality Engineer posting indicates IEC 62304 / ISO 14971 / ISO 13485 work is in progress rather than complete.
- **Prices.** Plan prices are fetched client-side and were not in the served HTML for the `en-au`, `en-us` or `en-gb` pricing pages; the plan and feature structure is published in full.
- **A leadership or team page.** `/about-us/people` serves the careers page; only the three founders are named on the company's own site.
- **Sources that could not be read on 2026-08-31:** Fierce Healthcare (HTTP 403), Capital Brief (HTTP 403), Business News Australia (HTTP 403), Bloomberg (paywalled), Crunchbase and PitchBook (gated).

### Inconsistencies across sources

- **Headcount, same day.** "400+ employees around the world" on the Media Room versus "500+ Heidis" on the careers page ([Media Room](https://www.heidihealth.com/en-au/about-us/media), [Careers](https://www.heidihealth.com/en-au/careers); both accessed 2026-08-31).
- **Hours saved, same day, three figures.** "47M Hours saved since launch" (careers page), "62.9M … saved by clinicians since launch" (enterprise page), "18 million hours" in 18 months (Series B release, still repeated in June 2026 postings) ([Careers](https://www.heidihealth.com/en-au/careers), [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise), [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)).
- **Country count.** "116 countries" in the October 2025 release and in postings published as late as June 2026; "190 countries" on the Media Room and "190+ countries" in postings from August 2026 ([Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b), [Senior Product Analyst](https://jobs.ashbyhq.com/heidihealth.com.au/5d352f63-74c2-458c-b40d-0666881f263f), [Media Room](https://www.heidihealth.com/en-au/about-us/media), [Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)).
- **Weekly volume across three months of 2026.** "2.4 million consults per week" (2026-02-24), "more than 2.7 million visits a week" (2026-03-10), "2.5 million patient sessions" (Media Room, 2026-08-31), and a homepage live counter reading 2,740,338 on 2026-08-31 ([Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence), [R1 RCM](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations), [Media Room](https://www.heidihealth.com/en-au/about-us/media), [heidihealth.com/en-au](https://www.heidihealth.com/en-au)).
- **Founding year.** TechCrunch dates the founding to 2021 in both its 2023 and 2025 reports; several secondary profiles say 2019; the predecessor entity OSCER ENTERPRISES PTY LTD has held an ABN since 2017-08-01, and HEIDI HEALTH TRADING PTY LTD since 2021-04-28 ([TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/), [ABN Lookup — Oscer](https://abr.business.gov.au/ABN/View?abn=57620824900), [ABN Lookup — Heidi](https://abr.business.gov.au/ABN/View?abn=84649783871)).
- **Learning budget.** "$1,000 per year" on the careers page against "$500 per annum" in job postings published from May to June 2026 ([Careers](https://www.heidihealth.com/en-au/careers), [Senior Software Engineer - Developer Experience](https://jobs.ashbyhq.com/heidihealth.com.au/99ef4d45-fcaf-4d53-b2db-9acd8a740be3)).
- **Open-role count.** The site footer reads "Open Roles 10+" while the Ashby board carried 85 postings on the same day ([Careers](https://www.heidihealth.com/en-au/careers), [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)).
- **Blog dates.** Article pages display the modified date, not the publication date: the Series A follow-on release shows "June 26, 2026" on the page while its structured data carries `datePublished` 2025-03-03 and independent coverage dates it 2025-03-06; the "Relief, on repeat" post shows July 31, 2026 on the page against `datePublished` 2026-07-07 ([Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care), [Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/), [Heidi — Relief, on repeat](https://www.heidihealth.com/en-au/blog/introducing-relief-on-repeat)).
- **AUD conversions of the March 2025 round.** Reported as A$26.8M by Startup Daily and A$27M in its headline; Business News Australia's headline says A$25.7M (its body could not be read; HTTP 403) ([Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/)).
- **X handle.** The site footer links `twitter.com/tryheidi` while the pages' `twitter:site` meta tag reads `@heidi_health`.

### Other

- **Stale boilerplate persists in live job postings.** A posting published 2026-06-25 still opens with "our most recent $16.6MM round of funding" and "In just 12 months, 20 million patient consults were supported by Heidi, and we're now powering more than 1 million consults every week" — figures from the March 2025 release, superseded by the October 2025 Series B ([Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837)).
- **Three sets of company values are live at once.** "Live Forever / Practice Ownership / Move Fast, Fix Faster / Get Better" (careers page), "Build to Last / Own Your Practice / Move Fast, Stay Steady / Make Others Better" (May–June 2026 postings), and "Live Forever / Practice Ownership / Small Cuts Heal Faster / Make others better" (other June 2026 postings), plus a six-item "How we show up" list in August 2026 postings.
- **The business model is freemium and clinician-led, by the company's own description.** "We found product-market fit with a freemium medical scribe that clinicians love"; the pricing FAQ has an entry titled "Why is there a free version of Heidi forever?"; the CEO told Forbes "We will never, ever monetise our free users by selling their data" ([Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8), [Pricing](https://www.heidihealth.com/en-au/pricing), [Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/)).
- **Product surface expanded from one product to four in roughly six months of 2026**: Evidence and Comms announced 2026-02-24/25, Remote in March 2026, Dictate live from 2026-06-29, with a monthly "Progress Notes" changelog running since at least January 2026 ([Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence), [Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/), [Heidi — Relief, on repeat](https://www.heidihealth.com/en-au/blog/introducing-relief-on-repeat), [Changelog](https://www.heidihealth.com/en-au/changelog)).
- **Hiring is weighted to commercial roles.** GTM (35) plus Marketing (6) is 41 of 85 postings against 24 in Engineering; three of the six marketing roles are SEO roles based in Makati City, Philippines ([Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)).
- **AI crawlers are explicitly allowed.** `robots.txt` grants `Allow: /` to `ChatGPT-User`, `GPTBot` and `Google-Extended` in addition to `*` ([robots.txt](https://www.heidihealth.com/robots.txt); read 2026-08-31).
- **A public status page exists** at `status.heidihealth.com`, and the enterprise page advertises "Service availability" as an Enterprise-only commitment; no SLA number is published ([Pricing](https://www.heidihealth.com/en-au/pricing), [status.heidihealth.com](https://status.heidihealth.com/)).

---

## Resources

**Official**

- [heidihealth.com/en-au](https://www.heidihealth.com/en-au) · [robots.txt](https://www.heidihealth.com/robots.txt) · [sitemap index](https://www.heidihealth.com/sitemap-index.xml) · [status.heidihealth.com](https://status.heidihealth.com/) · [support.heidihealth.com](https://support.heidihealth.com/) · [trust.heidihealth.com](https://trust.heidihealth.com/)
- Product — [Scribe](https://www.heidihealth.com/en-au/scribe) · [Evidence](https://www.heidihealth.com/en-au/evidence) · [Dictate](https://www.heidihealth.com/en-au/product/dictate) · [Remote / Hardware](https://www.heidihealth.com/en-au/hardware) · [Templates](https://www.heidihealth.com/en-au/templates) · [Pricing](https://www.heidihealth.com/en-au/pricing) · [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) · [System Requirements](https://www.heidihealth.com/en-au/system-requirements) · [Changelog ("Progress Notes")](https://www.heidihealth.com/en-au/changelog)
- Company — [Media Room](https://www.heidihealth.com/en-au/about-us/media) · [Careers](https://www.heidihealth.com/en-au/careers) · [Customer Spotlight](https://www.heidihealth.com/en-au/customers) · [Blog](https://www.heidihealth.com/en-au/blog)
- Safety and compliance — [Safety](https://www.heidihealth.com/en-au/safety) · [HIPAA](https://www.heidihealth.com/en-au/compliance/hipaa) · [UK](https://www.heidihealth.com/en-au/compliance/uk) · [Canada](https://www.heidihealth.com/en-au/compliance/canada) · [GDPR](https://www.heidihealth.com/en-au/compliance/gdpr) · [APP (AU/NZ)](https://www.heidihealth.com/en-au/compliance/app)
- Legal — [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) · [Heidi Scribe Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use) · [Scribe Usage Policy](https://www.heidihealth.com/en-au/legal/scribe-usage-policy) · [UK GDPR Compliance Policy](https://www.heidihealth.com/en-au/legal/ukgdpr-compliance-policy) · [Accessibility Statement](https://www.heidihealth.com/en-au/legal/accessibility-statement)
- Hiring — [Ashby job board](https://jobs.ashbyhq.com/heidihealth.com.au) · [Ashby job board API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)

**Company announcements** (newest first)

- [Introducing: Relief, on repeat](https://www.heidihealth.com/en-au/blog/introducing-relief-on-repeat) — 2026-07-07
- [More Patients, Less Paperwork: Heidi's AI Scribe Returns an Estimated $2.51M in Clinical Time](https://www.newswire.ca/news-releases/more-patients-less-paperwork-heidi-s-ai-scribe-returns-an-estimated-2-51m-in-clinical-time-893435988.html) — 2026-07-22
- [Heidi and QHR Technologies integrate AI documentation into Accuro EMR](https://www.heidihealth.com/en-au/about-us/media) — 2026-06-16
- [The Royal Children's Hospital deploys Heidi](https://www.heidihealth.com/en-au/about-us/media) — 2026-06-03
- [Heidi Evidence launches, acquires AutoMedica](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence) — 2026-02-24
- [Building the AI Care Partner for Every Clinician](https://www.heidihealth.com/en-us/blog/ai-care-partner-for-every-clinician) — 2025-10-31
- [Heidi Secures $65 Million USD in Series B Funding](https://www.heidihealth.com/en-us/blog/heidi-series-b) — 2025-10-05
- [Heidi Health secures USD $16.6M in funding](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) — 2025-03-06 (page displays its modified date)

**Partner and registry sources**

- [ABN Lookup — HEIDI HEALTH TRADING PTY LTD](https://abr.business.gov.au/ABN/View?abn=84649783871) · [ABN Lookup — OSCER ENTERPRISES PTY LTD](https://abr.business.gov.au/ABN/View?abn=57620824900)
- [R1 RCM — R1 and Heidi Announce Strategic Partnership](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations) — 2026-03-10
- [Blackbird portfolio — Heidi Health](https://www.blackbird.vc/portfolio/heidi-health)
- [GitHub API — organisation `Heidi-Health`](https://api.github.com/orgs/heidi-health)

**Third-party coverage**

- [Forbes Australia — Australian AI startup Heidi Health launches its first hardware device](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/) — 2026-03-24
- [Canadian Healthcare Technology — Heidi AI scribes save 13 minutes per visit](https://www.canhealth.com/2026/07/22/heidi-ai-scribes-save-13-minutes-per-visit/) — 2026-07-22
- [TechCrunch — Heidi Health raises $65M Series B led by Steve Cohen's Point72](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/) — 2025-10-05
- [SmartCompany — Heidi Health's $98 million raise skyrockets its valuation to $704 million](https://www.smartcompany.com.au/startupsmart/heidi-health-98-million-raise-valuation-704-million/) — 2025-10-06
- [Startup Daily — GP administration startup Heidi Health tops up Series A with another $27 million](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/) — 2025-03-04
- [TechCrunch — Blackbird backs Heidi Health's AI platform for overworked doctors](https://techcrunch.com/2023/10/25/heidi-health/) — 2023-10-25
