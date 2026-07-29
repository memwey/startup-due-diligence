# MachinePulse

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

MachinePulse Pte. Ltd. is a Singapore-registered company building what it calls "Proactive AI Agents" ([careers page](https://join.machinepulse.ai/); Undated; accessed 2026-07-29). Its corporate site is a one-page holder; the substance sits in three separate properties: **Karpo**, a free consumer AI that lives in iMessage and recommends places and events in six cities; **World2Agent (W2A)**, an Apache-2.0 protocol for feeding real-world signals into AI agents; and **Shotwright**, an MIT-licensed agent that drives Adobe After Effects inside a Windows container.

- Karpo launched publicly on 2026-03-09 and reported 520,000+ recommendations delivered, 4M+ conversations, and a "near-40% immediate positive response rate" as of [2026-07-28](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html).
- The only funding statement found is the company's own, repeated on the [careers page](https://join.machinepulse.ai/) and inside a job description: "backed by top-tier USD funds, with a valuation approaching $100 million". No round, investor, or date has been announced anywhere found.
- The careers site lists 20 active roles ([jobs API](https://join.machinepulse.ai/api/jobs); accessed 2026-07-29). 18 are located in **Shanghai**, one in New York; every role offers Singapore, Shanghai, New York, and California Bay Area as location options. The engineering roles describe Go and Python backends, Kubernetes on AWS/GCP/Azure, an iOS client, and an in-house LLM post-training team.
- The [GitHub organisation](https://github.com/machinepulse-ai) was created 2025-11-11, lists Singapore, and holds 6 public repositories; [world2agent](https://github.com/machinepulse-ai/world2agent) had 1,245 stars and 40 forks when accessed 2026-07-29.
- No founder or CEO is named in any source reviewed. The only staff identified are a Head of Growth quoted in a press release and one engineer on LinkedIn; a design internship posting refers to "senior practitioners with ByteDance backgrounds".
- **Name collision:** an unrelated industrial-IoT company also called MachinePulse (Mumbai, `machinepulse.com`) dominates search results and startup databases. Crunchbase, Tracxn, and GetLatka entries for "MachinePulse" describe that company, not this one.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | MachinePulse Pte. Ltd. | [site footer](https://www.machinepulse.ai/), [Karpo about page](https://app.karpo.ai/about-us) |
| Jurisdiction | Singapore (Pte. Ltd. is the Singapore private-limited form) | inferred from the entity name; not verified against ACRA |
| Operating locations | 18 of 20 open roles are located in Shanghai, one in New York; all roles offer Singapore, Shanghai, New York, and California Bay Area as options | [jobs API](https://join.machinepulse.ai/api/jobs); accessed 2026-07-29 |
| Public brand | MachinePulse; products branded Karpo, World2Agent, Shotwright | [site](https://www.machinepulse.ai/) |
| Tagline | "The Very Pulse of the Machine"; "building something PROACTIVE" | [site](https://www.machinepulse.ai/) |
| Stated focus | "Proactive AI Agents" and the evolution of human-machine interaction | [careers page](https://join.machinepulse.ai/) |
| GitHub org created | 2025-11-11; location Singapore; 6 public repos | [GitHub API](https://github.com/machinepulse-ai) |
| Contact | support@ (Karpo), contact@ (GitHub org), partnership@, ahr@ (hiring), intern@ (internships), all `@machinepulse.ai` | [site](https://www.machinepulse.ai/), [Karpo about page](https://app.karpo.ai/about-us), [careers page](https://join.machinepulse.ai/) |
| Social | [LinkedIn](https://www.linkedin.com/company/machinepulseai/about/), X [@MachinePulse_AI](https://x.com/MachinePulse_AI) and [@Karpo_AI](https://x.com/Karpo_AI), [Instagram](https://www.instagram.com/karpo.ai), [Discord](https://discord.gg/hDjaD8pX) | [site](https://www.machinepulse.ai/), [World2Agent](https://world2agent.ai/) |
| Copyright year on site | 2026 | [site](https://www.machinepulse.ai/) |

The corporate site, careers page, Karpo pages, and LinkedIn profile are continuously updated pages without publication dates; all were accessed on 2026-07-29. The corporate site carries no about page, team page, press index, address, or registration number.

### Identity and legal entities

Two unrelated businesses use the name MachinePulse. Establishing which one a source describes is a prerequisite for every other fact on this page.

| Name | Domain | What it is | Relationship |
|---|---|---|---|
| MachinePulse Pte. Ltd. | [machinepulse.ai](https://www.machinepulse.ai/) | Singapore entity; Karpo, World2Agent, Shotwright | The subject of this page |
| MachinePulse (India) | machinepulse.com | Mumbai-based industrial IoT / machine-data analytics platform, ~10 staff, self-funded | No relationship found |

The India company is the one described by [Crunchbase](https://www.crunchbase.com/organization/machinepulse), [Tracxn](https://tracxn.com/d/companies/machine-pulse/__T2EbVVSjXHxNVi2tptAU2PdQE2I7bYoG-0V2Qt1iFD8), and [GetLatka](https://getlatka.com/companies/machinepulse); those profiles carry founder, revenue, and headcount figures that do not apply to the Singapore entity. No database entry for the Singapore entity was found (searched 2026-07-29).

Search listings on uspto.report show four US trademark applications filed under the owner name "Machinepulse Pte. Ltd.": [KARPO (99653628)](https://uspto.report/TM/99653628), [KARPO (99653232)](https://uspto.report/TM/99653232), [K (99653634)](https://uspto.report/TM/99653634), and [MACHINEPULSE (99653745)](https://uspto.report/TM/99653745). The individual record pages returned HTTP 403 when accessed on 2026-07-29, so filing dates, status, and the owner's address were not verified. The stated goods and services cover SaaS for artificial intelligence, machine learning and generative models, and software for configuring and managing autonomous AI agents and workflows.

---

## Product

### Karpo

A free consumer AI assistant for city discovery, reached by texting a US number (+1 415 886 0326) from iMessage, and also described as available as an app ([Karpo home](https://app.karpo.ai/), [how it works](https://app.karpo.ai/how-it-works), [FAQ](https://app.karpo.ai/faqs); all accessed 2026-07-29).

- **What it does** — recommends restaurants, bars, galleries, live music, and events; learns preferences from the conversation; can be added to an iMessage group chat to help a group converge on a plan ([FAQ](https://app.karpo.ai/faqs)).
- **Coverage** — "knows New York City, San Francisco, and London the best"; also serves Miami, Los Angeles, and Singapore ([about page](https://app.karpo.ai/about-us)).
- **Booking** — integrated booking through Ticketmaster, Viator, Expedia, and Klook ([2026-07-28 release](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html)).
- **Price** — free; the FAQ answers the cost question with "Yes" to being completely free. No paid tier, subscription, or in-product purchase is documented.

### World2Agent (W2A)

An open protocol, presented at [world2agent.ai](https://world2agent.ai/) and developed at [github.com/machinepulse-ai/world2agent](https://github.com/machinepulse-ai/world2agent) under Apache 2.0. It standardizes how AI agents perceive external data, on a `World → Sensor → Agent` model: sensors are independent npm packages that watch a data source and emit signals in a common schema, and agents consume those signals.

- **Design constraints stated in the [architecture doc](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md):** the protocol is "natural-language-first"; sensors stay neutral — they do not make value judgments, assume where they run, or define routing, prioritization, or actions.
- **Transports:** stdout piping, HTTP POST, WebSocket / Server-Sent Events, and consumer-defined custom transports.
- **Agent runtimes with native plugins:** Claude Code, Hermes, OpenClaw ([README](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/README.md)).
- **Publishing:** sensors are built with a `build-w2a-sensor` skill, published to npm, and registered on [SensorHub](https://world2agent.ai/hub).
- **Roadmap:** a graph layer to compose and enrich signals from several sensors before delivery.

The company describes the protocol as complementary to MCP rather than a replacement ([Chinese write-up, 2026-04-29](https://www.80aj.com/2026/04/29/ai-agent-realtime-perception/)).

### Shotwright

[github.com/machinepulse-ai/shotwright](https://github.com/machinepulse-ai/shotwright), MIT-licensed, Python, created 2026-05-18. A chat-driven product in which a Copilot or Codex agent operates a real Adobe After Effects install inside a Windows container: it plans footage, prepares assets, writes JSX automation scripts, hands them to nexrender for headless rendering, and streams the finished mp4 to the browser. Stack badges in the README name Windows Containers LTSC 2025, After Effects 2026, FastAPI 0.110+, React 18, and Node 20+. The README states the goal is "not generic AI video automation" but a reproducible AE runtime with an agent layer on top. The repository carries a Simplified Chinese README alongside the English one.

### Commercialization

No revenue mechanism is documented for any of the three products. Karpo is free with no paid tier described, World2Agent and Shotwright are permissively licensed open source, and no enterprise offering, pricing page, or sales contact exists on any of the properties reviewed on 2026-07-29.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2025-11-11 | GitHub organisation created | [GitHub API](https://github.com/machinepulse-ai) |
| 2026-03-09 | Karpo public launch | [2026-07-28 release](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) |
| 2026-04-23 | world2agent repository created | [GitHub API](https://github.com/machinepulse-ai/world2agent) |
| 2026-07-28 | Karpo: 520,000+ recommendations, 4M+ conversations, ~40% immediate positive response rate, 80 days post-launch | [release](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) |
| Accessed 2026-07-29 | world2agent: 1,245 stars, 40 forks; shotwright: 13 stars; other four repos: 0–5 stars | [GitHub API](https://github.com/machinepulse-ai) |
| Accessed 2026-07-29 | SensorHub: 11 sensors; most-downloaded is the Hacker News sensor at 526 downloads | [SensorHub](https://world2agent.ai/hub) |
| Accessed 2026-07-29 | app.karpo.ai sitemap: 5,847 URLs, of which 5,520 are `/scenarios/` pages | [sitemap](https://app.karpo.ai/sitemap.xml) |

The 4M+ conversations figure sits against 520,000+ recommendations over the same period; the release does not define either term or state a user count.

### Announced partners

| Date | Party | Detail |
|---|---|---|
| [2026-07-28](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) | Ticketmaster, Viator, Expedia, Klook | Named as integrated booking partners |
| [2026-07-28](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) | Molly Tea (Singapore) | On-site activation where users earned free drinks by answering local food-scene trivia |

The release does not state whether the booking integrations are commercial agreements, affiliate arrangements, or public API usage.

### Stated plans

The clearest statement of commercial direction is in a job description rather than any announcement. The [Senior Manager, Commercial Operations posting](https://join.machinepulse.ai/api/jobs) (created 2026-05-10) sets the remit as building "a North American Local Life Platform": constructing a supply-side operations system and independently driving external partnerships. It names the platform types the company wants that experience from — Yelp, OpenTable, Resy, Booking.com, Google Places, Eventbrite, SeatGeek — and asks for 3+ years in North American local life, travel, or hospitality.

Other postings define the target markets as North American cities, primarily New York and Los Angeles, with Japanese and Korean markets named as a secondary cultural focus, and the acquisition surfaces as Instagram, TikTok, Reddit, Discord, YouTube, X, Google and Meta paid media, plus SEO and ASO.

The [AI Product Manager](https://join.machinepulse.ai/api/jobs) and several other postings describe the product as being at the "0-to-1" stage.

---

## Founder

No founder, CEO, or other executive is named on the corporate site, the careers page, any Karpo page, any repository, or any press release reviewed. The [GitHub organisation](https://github.com/orgs/machinepulse-ai/people) has no public members.

The two people identifiable by name:

| Name | Role | Source |
|---|---|---|
| Titus Zhai | Head of Growth, MachinePulse | quoted in the [2026-07-28 release](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) |
| Lucas Wu | "Building proactive AI @MachinePulse"; located in Singapore | [LinkedIn](https://sg.linkedin.com/in/fan-lucas-wu); the profile returned HTTP 999 when fetched on 2026-07-29, so only the search-result headline was readable |

Two statements about the team appear in job descriptions and are the only characterisation of its composition found: the UI/UX Design Intern posting offers mentorship "directly alongside senior practitioners with ByteDance backgrounds", and the Commercial Operations posting offers "direct access to the founding team" ([jobs API](https://join.machinepulse.ai/api/jobs); accessed 2026-07-29). Neither names anyone.

---

## Funding

No funding round has been announced by the company, by any investor, or in any media report found (searched 2026-07-29).

The funding statement appears twice, both times in the company's own recruitment copy. The [careers page](https://join.machinepulse.ai/) (Undated; accessed 2026-07-29) describes MachinePulse as a "global AI startup" that is "backed by top-tier USD funds, valued at nearly $100 million". The [Senior Manager, Commercial Operations description](https://join.machinepulse.ai/api/jobs) (created 2026-05-10) repeats it as "a global AI startup backed by top-tier USD funds, with a valuation approaching $100 million" and, under what the company offers, "Backed by premier USD funds with a valuation approaching $100M and meaningful equity upside".

No investor is named, no round label or amount is given, and no date is attached in either place. Nothing corroborates it: no Crunchbase or Tracxn entry exists for the Singapore entity, and no press release, investor portfolio page, or news article mentioning a MachinePulse round was found. The same posting asks for candidates with "startup experience or time at an early-stage company (Series A or earlier)", which is a description of the candidate's background rather than a statement of the company's own stage.

---

## Engineering

### Technology stack and platforms

| Item | Detail | Evidence class |
|---|---|---|
| W2A protocol and SDK | TypeScript; sensors distributed as npm packages | Confirmed — [repos](https://github.com/machinepulse-ai) |
| W2A transports | stdout, HTTP POST, WebSocket / SSE, custom | Confirmed — [architecture doc](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md) |
| W2A agent runtimes | Claude Code, Hermes, OpenClaw plugins | Confirmed — [README](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/README.md) |
| Shotwright backend | Python, FastAPI 0.110+ | Confirmed — [README](https://github.com/machinepulse-ai/shotwright) |
| Shotwright frontend | React 18, Node 20+ | Confirmed — [README](https://github.com/machinepulse-ai/shotwright) |
| Shotwright runtime | Windows Containers LTSC 2025, Adobe After Effects 2026, nexrender, GitHub Container Registry | Confirmed — [README](https://github.com/machinepulse-ai/shotwright) |
| Karpo delivery channel | Apple iMessage via a US phone number (+1 415 886 0326) | Confirmed — [how it works](https://app.karpo.ai/how-it-works) |
| Karpo web surface | Server-rendered pages under `/scenarios/`, `/city-guides/`, `/explore/` | Confirmed — [sitemap](https://app.karpo.ai/sitemap.xml) |

The following come from the [job descriptions](https://join.machinepulse.ai/api/jobs) (accessed 2026-07-29) and are hiring evidence, not confirmed production use. A required language supports an inference; an item listed only as a bonus qualification does not.

| Item | Detail | Where it appears |
|---|---|---|
| Backend languages | Go and Python, advertised as two parallel senior roles with otherwise identical descriptions; a third role is Golang-specific for Agent systems | required |
| Datastores | PostgreSQL, Redis, message queues, object storage | required |
| Orchestration and cloud | Kubernetes cluster deployment and scheduling; at least one of AWS, GCP, or Azure and its managed services (ECS, EKS, GKE) | required |
| Infrastructure tooling | Terraform, Ansible, Prometheus/Grafana, CI/CD pipelines, canary releases and rollback | required |
| Service mesh | Istio, named as an example in traffic and network governance work | required (as example) |
| Observability | Logging, metrics, distributed tracing; capacity planning and fault drills | required |
| ML training stack | PyTorch; at least one of HuggingFace, DeepSpeed, or Megatron; SFT, DPO, GRPO, PPO, reward modeling, knowledge distillation | required |
| iOS client | Swift with UIKit and/or SwiftUI; MVC/MVVM; Swift Package Manager, Tuist or CocoaPods; App Store and TestFlight distribution | required / bonus |
| Web front end | JavaScript/TypeScript, HTML5, CSS3, React or Vue | required (intern role) |
| Agent plumbing | MCP protocol pipeline development, prompt engineering, tool calling, context management | required (intern role) |
| Retrieval | Vector databases and retrieval frameworks; recall optimization, ranking, evaluation | bonus only |
| Multi-cloud | Hybrid cloud and multi-region, multi-cluster Kubernetes network governance | bonus only |

Two facts follow from this that other sources did not establish. The company runs an **in-house LLM post-training effort** — the ML Algorithm Engineer role covers alignment and distillation to transfer reasoning and preference behaviour from large models into smaller ones for "intent recognition, personalized response generation, and digital persona" — so MachinePulse is not purely a consumer of third-party model APIs. And it is building a **native iOS client**, which the product pages do not mention.

No model provider or cloud provider is named for Karpo in any product-facing source. Neither Karpo nor MachinePulse publishes a security page, subprocessor list, or data-retention policy; `app.karpo.ai/terms` and `app.karpo.ai/privacy` both returned HTTP 404 when fetched on 2026-07-29, although the Karpo landing page links to Terms of Use and a Privacy Notice.

### Systems

| System | What it does | Source |
|---|---|---|
| Karpo conversational recommender | Turns loose intent into a short list of options, learns preferences across the conversation, and produces an agenda on request; works in one-to-one and group iMessage threads | [how it works](https://app.karpo.ai/how-it-works), [FAQ](https://app.karpo.ai/faqs) |
| Karpo content generation pipeline | 5,520 `/scenarios/` pages plus city-guide and per-venue `/explore/experience/` pages across six cities, most carrying 2026-07-18 timestamps | [sitemap](https://app.karpo.ai/sitemap.xml) |
| W2A sensor runtime | npm-packaged sensors polling external sources and emitting schema-conformant signals over pluggable transports | [architecture doc](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md) |
| SensorHub registry | Catalogue of published sensors with download counts, auto-registered by a postpublish CLI | [SensorHub](https://world2agent.ai/hub), [notify-hub repo](https://github.com/machinepulse-ai/world2agent-notify-hub) |
| Shotwright AE runtime | Containerized After Effects driven by agent-written JSX, rendered headlessly by nexrender, streamed back as mp4 | [README](https://github.com/machinepulse-ai/shotwright) |

### Technical background sought

From the [job descriptions](https://join.machinepulse.ai/api/jobs) (accessed 2026-07-29), the prior problem experience candidates are expected to bring:

- **Backend (Go / Python, senior):** production concurrency and performance tuning; consistency guarantees, caching strategy, rate limiting and graceful degradation; canary releases, rollback, service-metric interpretation and capacity planning. Bonus: production AI applications, retrieval and ranking evaluation.
- **Backend (Go, Agent):** designing complex business systems and trading off reliability, performance, cost and delivery speed; tool integration, access control, task-state management, exception handling and phased releases. Bonus: workflow engines, task platforms, incident management.
- **Infrastructure (SRE):** 3–5 years in infrastructure or operations; Kubernetes deployment, management and scheduling; traffic scheduling and network governance; IaC adoption. Bonus: cloud architect certification, service mesh rollout, open-source contributions.
- **ML (post-training):** master's or above; Transformer and GPT-style architectures; hands-on post-training and alignment; transferring large-model capability into small models and shipping them. Bonus: contributions to LLaMA, Qwen, InternLM, Mistral, vLLM or alignment toolchains; publications; algorithm-competition background (AMC, ICPC, NOI, IOI).
- **Product and content roles:** repeatedly require hands-on LLM project work — the Agent Content posting excludes candidates whose experience is "merely 'using ChatGPT' as a casual tool" — plus cross-cultural fluency in Western (primarily NYC/LA) or Japanese/Korean lifestyles.

### Working conditions

The careers site loads its listings client-side from `https://join.machinepulse.ai/api/jobs`; the server-rendered HTML contains only the application form, so the roles are invisible to tools that do not execute JavaScript. As of 2026-07-29 the API returned 20 roles, all marked active: 12 full-time and 8 internships, across Research & Development (8), Product & Growth (10), Administration (1), and one with no department set. Creation timestamps cluster on 2026-01-29 (15 roles), with later additions on 2026-01-30, 2026-02-04, 2026-03-01, 2026-05-10, and 2026-07-25.

| Item | Detail | Source |
|---|---|---|
| Open roles | 20 active: 12 full-time, 8 internships | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Locations | 18 roles listed as Shanghai, 1 New York (Senior Backend Engineer, Go), 2 unset; every role offers Singapore / Shanghai / New York / California Bay Area as options | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Working language | Not stated as a company-wide policy. Postings are written in English; several product roles require "English as a working language"; applicant materials invite Xiaohongshu, Douyin and Bilibili links, and the application form has a WeChat ID field | [jobs API](https://join.machinepulse.ai/api/jobs), [careers form](https://join.machinepulse.ai/) |
| Remote policy | The UI/UX Designer posting offers "flexible working arrangements and periodic remote options"; interns are required on-site at least 4 days per week | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Equity | "Competitive salary, performance bonuses, and equity incentives" (designer, PM); "a founding-team seat" and "meaningful equity upside" (Commercial Operations) | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Salary | Not published for any role | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Internships | 8 of 20 roles; 3–6 months, conversion to full-time offered for strong performers; one backend internship is scoped to the 2026/2027 graduating classes | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Stated culture | "Flat", "non-hierarchical", "extremely short decision-making chains", "direct access to the founding team"; AI coding tools encouraged with "ample token support" | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Application route | `ahr@machinepulse.ai` (full-time) or `intern@machinepulse.ai` (internships) with the position in the subject; or the on-site form. Some roles invite a 1–3 minute video pitch and social-profile links | [careers form](https://join.machinepulse.ai/), [jobs API](https://join.machinepulse.ai/api/jobs) |
| Interview process | Not described except for the Commercial Operations role's mention of ambiguity and pace; no stage count published | [jobs API](https://join.machinepulse.ai/api/jobs) |
| Visa, benefits, turnover | Not published | [jobs API](https://join.machinepulse.ai/api/jobs) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): machinepulse.ai and every link on it; join.machinepulse.ai rendered in a browser plus its `/api/jobs` endpoint and all 20 role records; world2agent.ai including the SensorHub; app.karpo.ai including its full sitemap, FAQ, about, how-it-works, and buzz pages; the GitHub organisation via the REST API, its six repositories, and its members page; the world2agent README and architecture doc; the Shotwright README; searches in English and Chinese for "MachinePulse", "MachinePulse Pte", "Karpo", "Karpo AI", and "World2Agent"; Crunchbase, Tracxn, and GetLatka; uspto.report trademark listings; and searches for a Karpo App Store listing.

- No founder or CEO is named anywhere. No team page exists on any property.
- No funding round, investor, valuation date, or database entry corroborating the careers-page claim was found.
- No office address, registration number, or ACRA record was retrieved. The Singapore jurisdiction is inferred from the "Pte. Ltd." suffix, not verified against the register; a BizFile entity search was not performed.
- No revenue model is documented for any product.
- `app.karpo.ai/terms` and `app.karpo.ai/privacy` returned HTTP 404 despite being linked from the landing page. No security page, subprocessor list, data-retention statement, or certification is published for either Karpo or MachinePulse.
- No model provider is named. The cloud is narrowed only to "AWS, GCP, or Azure" by the SRE posting, which does not say which one is in use.
- No salary band is published for any of the 20 roles, and no visa, benefits, or turnover information was found.
- No named individual is attached to any role, department, or reporting line; the postings refer to "the founding team" without naming it.
- No coverage in mainstream technology media was found — the only press located is a single 2026-07-28 release syndicated across openPR and a network of aggregator sites, plus one Chinese blog post on World2Agent.
- The GitHub organisation has no public members, so individual contributors cannot be identified from it.

### Inconsistencies across sources

- **Which MachinePulse:** [Crunchbase](https://www.crunchbase.com/organization/machinepulse), [Tracxn](https://tracxn.com/d/companies/machine-pulse/__T2EbVVSjXHxNVi2tptAU2PdQE2I7bYoG-0V2Qt1iFD8), and [GetLatka](https://getlatka.com/companies/machinepulse) return an unrelated Mumbai industrial-IoT company for the query "MachinePulse". Their founder, revenue, headcount, and funding-status fields do not describe the Singapore entity.
- **Country and centre of operations:** a [third-party social post](https://www.threads.com/@buzz.indica/post/DV8UQrGERU1/us-based-startup-machine-pulses-ai-agent-karpo-has-started-offering-to-pay) describes MachinePulse as "US-based"; the legal entity is a Singapore Pte. Ltd. and the [GitHub organisation](https://github.com/machinepulse-ai) lists Singapore; and 18 of 20 open roles are located in Shanghai ([jobs API](https://join.machinepulse.ai/api/jobs)). Three sources, three different countries — none of them wrong on its own terms, but the hiring data is the only one that indicates where the work is actually done.
- **Karpo platform:** the [2026-07-28 release](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) says Karpo is "available on App and iMessage"; the [FAQ](https://app.karpo.ai/faqs) and [how-it-works](https://app.karpo.ai/how-it-works) pages describe only the iMessage path, and no App Store listing was found. An [iOS Development Intern posting](https://join.machinepulse.ai/api/jobs) covering Swift, App Store submission and TestFlight distribution indicates a native client is under development, which is consistent with the app being unreleased rather than with either page being wrong.
- **Karpo capabilities:** the [how-it-works page](https://app.karpo.ai/how-it-works) presents ticket booking, travel booking, and "life admin" in aspirational phrasing, while the [press release](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html) presents integrated booking through four named partners as shipped.

### Other

- The three products share almost nothing: a consumer lifestyle assistant, an agent-infrastructure protocol, and a video-production agent. The only common thread stated by the company is "proactive" agents ([site](https://www.machinepulse.ai/), [careers page](https://join.machinepulse.ai/)).
- Karpo's public web surface is overwhelmingly programmatic: 5,520 of 5,847 sitemap URLs are `/scenarios/` pages, many pegged to news events and celebrity names, with timestamps clustered on 2026-07-18 ([sitemap](https://app.karpo.ai/sitemap.xml)).
- The 2026-07-28 release was distributed through [openPR](https://www.openpr.com/news/4589478/karpo-crosses-half-a-million-personalized-recommendations) and republished verbatim across a large set of near-identical local-news aggregator domains. It is one release, not multiple independent reports.
- A [third-party social post](https://www.threads.com/@buzz.indica/post/DV8UQrGERU1/us-based-startup-machine-pulses-ai-agent-karpo-has-started-offering-to-pay) describes Karpo offering to sponsor users' outings up to $300 per person if it finds their plan interesting. No company-published source for this campaign was found.
- All World2Agent code is Apache 2.0 and Shotwright is MIT; the protocol, SDK, plugins, example sensors, and registry CLI are all published openly.
- The careers listings are the densest public source on this company by a wide margin — they establish the operating location, the stack, the existence of an in-house post-training team and an unreleased iOS client, and the commercial direction, none of which appears on any product or press surface. They are also invisible without JavaScript, since the page renders them from `/api/jobs` client-side.
- Hiring is weighted toward go-to-market: 10 of 20 roles are in Product & Growth, most of them overseas social media, influencer marketing, paid media, and growth, against 8 in Research & Development ([jobs API](https://join.machinepulse.ai/api/jobs)).

---

## Resources

**Official**

- [MachinePulse — corporate site](https://www.machinepulse.ai/)
- [Careers](https://join.machinepulse.ai/) · [jobs API — the 20 role records the page renders from](https://join.machinepulse.ai/api/jobs)
- [LinkedIn](https://www.linkedin.com/company/machinepulseai/about/)
- [X — @MachinePulse_AI](https://x.com/MachinePulse_AI)
- Karpo
  - [Karpo home](https://app.karpo.ai/)
  - [About us](https://app.karpo.ai/about-us)
  - [How it works](https://app.karpo.ai/how-it-works)
  - [FAQ](https://app.karpo.ai/faqs)
  - [Buzz](https://app.karpo.ai/buzz)
  - [Sitemap](https://app.karpo.ai/sitemap.xml)
  - [X — @Karpo_AI](https://x.com/Karpo_AI) · [Instagram](https://www.instagram.com/karpo.ai)
- World2Agent
  - [world2agent.ai](https://world2agent.ai/) · [SensorHub](https://world2agent.ai/hub)
  - [GitHub — world2agent](https://github.com/machinepulse-ai/world2agent) · [README](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/README.md) · [architecture doc](https://raw.githubusercontent.com/machinepulse-ai/world2agent/main/docs/architecture.md)
  - [GitHub — notify-hub](https://github.com/machinepulse-ai/world2agent-notify-hub)
  - [Discord](https://discord.gg/hDjaD8pX)
- [GitHub organisation](https://github.com/machinepulse-ai) · [members page](https://github.com/orgs/machinepulse-ai/people)
- [GitHub — Shotwright](https://github.com/machinepulse-ai/shotwright)

**Press releases**

- [Karpo crosses half a million personalized recommendations in under 80 days — 2026-07-28](https://www.openpr.com/news/4589478/karpo-crosses-half-a-million-personalized-recommendations) · [syndicated copy with full text](https://news.eandtnews.com/story/560137/karpo-crosses-half-a-million-personalized-recommendations-in-under-80-days.html)

**Third-party coverage and profiles**

- [80aj.com — World2Agent write-up, 2026-04-29 (ZH)](https://www.80aj.com/2026/04/29/ai-agent-realtime-perception/)
- [Threads — third-party post on the Karpo sponsorship campaign](https://www.threads.com/@buzz.indica/post/DV8UQrGERU1/us-based-startup-machine-pulses-ai-agent-karpo-has-started-offering-to-pay)
- [LinkedIn — Lucas Wu](https://sg.linkedin.com/in/fan-lucas-wu)
- USPTO trademark listings under Machinepulse Pte. Ltd.: [KARPO 99653628](https://uspto.report/TM/99653628), [KARPO 99653232](https://uspto.report/TM/99653232), [K 99653634](https://uspto.report/TM/99653634), [MACHINEPULSE 99653745](https://uspto.report/TM/99653745)

**Profiles of the unrelated MachinePulse (India) — listed to prevent misattribution**

- [Crunchbase](https://www.crunchbase.com/organization/machinepulse)
- [Tracxn](https://tracxn.com/d/companies/machine-pulse/__T2EbVVSjXHxNVi2tptAU2PdQE2I7bYoG-0V2Qt1iFD8)
- [GetLatka](https://getlatka.com/companies/machinepulse)
