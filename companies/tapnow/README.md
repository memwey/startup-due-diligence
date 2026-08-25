# TapNow

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-26.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

TapNow calls itself "Your Creative OS" — an agentic, infinite-canvas workspace that "orchestrate[s] text, image, audio, and video models", delivered as a web app and a macOS desktop app ([homepage](https://www.tapnow.ai/), [download](https://www.tapnow.ai/download); accessed 2026-08-26). The contracting entity is `Tamar AI Inc.`, "a Delaware corporation that operates the Services under the TapNow brand" ([Terms of Service](https://www.tapnow.ai/terms-of-service); Last updated 2025-09-01), while the company's own careers page advertises its open roles under the heading "SHENZHEN · OPEN ROLES" ([careers](https://www.tapnow.ai/careers); accessed 2026-08-26).

- The brand's earlier positioning is documented but has been removed from the live site: an archived `about` page presented **Tamar AI** as "The World's Leading AI Company for Marketing", "Leading the E-commerce Revolution through Artificial Intelligence", claiming it had "empowered thousands of e-commerce sellers" and provided "technical services to major corporations, including industry giants like Google and Amazon" ([Wayback capture, 2025-10-06](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)). The page now returns a 404 view — see `Identity and legal entities`.
- No funding announcement was found for this company. The `TapNow` profiles that funding databases return describe a **different, unrelated company** — a Tokyo photo-and-video sharing app founded 2022 that raised US$1.94M ([Tracxn](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8); page last updated 2026-08-17) — as does a Mixpanel customer story about "a social networking app created by Sango Technologies" ([Mixpanel](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/)).
- Scale is company-stated and thin: a recruiting post by the person leading TapNow's technical direction says "TapNow 目前已经拥有上百万用户，日活也保持在不错的水平" ("TapNow already has millions of users, and DAU stays at a decent level") ([V2EX](https://www.v2ex.com/t/1230334)). Independently, Similarweb reported 984K visits for `tapnow.ai` in the July 2026 reference period, with China 55.31%, the United States 17.53% and Japan 8.53% of traffic ([Similarweb](https://www.similarweb.com/website/tapnow.ai/)).
- Enterprise claims are specific: "SOC 2 Type 2 with annual penetration testing", SAML SSO, SCIM provisioning, GDPR and CCPA, "AES-256 at rest. TLS 1.2+ in transit", and a training-data commitment that "Without explicit authorization, non-public customer content is not used to train general-purpose models offered to unrelated third parties" ([enterprise](https://www.tapnow.ai/enterprise); accessed 2026-08-26).
- Engineering is visible from the served application and from the company's own recruiting posts: Next.js behind Google Frontend, assets on `files.tapnow.art`, Sentry and Mixpanel in the bundle, Chinese-first documentation at `docs.tapnow.ai`, and a hiring pitch built around agents as "新的生产主体" ("the new production unit") with test-driven QA agents ([V2EX](https://www.v2ex.com/t/1232468)).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | TapNow; the product is branded "Creative OS", with a companion community product "TapTV" | [homepage](https://www.tapnow.ai/), [docs](https://docs.tapnow.ai/), [Terms of Service](https://www.tapnow.ai/terms-of-service) |
| Contracting entity | "Tamar AI Inc., a Delaware corporation that operates the Services under the TapNow brand" | [Terms of Service](https://www.tapnow.ai/terms-of-service); Last updated 2025-09-01 |
| Corporate email domain | Recruiting contact given as `andy.hu@tamaredge.ai`; `tamaredge.ai` was registered 2023-08-24 (NameSilo, registrant shielded) and serves no website | [V2EX](https://www.v2ex.com/t/1230334); WHOIS read 2026-08-26 |
| Team location | "SHENZHEN · OPEN ROLES" on the careers page; a role posting is headed "Agent 工程师（QA 方向）/ Agentic Quality Engineer｜深圳" | [careers](https://www.tapnow.ai/careers), [V2EX](https://www.v2ex.com/t/1232468) |
| Document dates | Terms of Service "Last updated [September 1, 2025]"; Privacy Policy "Last Updated: [September 1, 2025]"; AI Generated Content Use and Commercial License "Version 1.1 \| Effective August 6, 2026 \| Last updated August 10, 2026" | [Terms](https://www.tapnow.ai/terms-of-service), [Privacy Policy](https://www.tapnow.ai/privacy-policy), [content licence](https://www.tapnow.ai/generated-content-license) |
| Age policy | "You must be at least 18 years old and legally capable of entering into a binding contract. The Services are not directed to children." | [Terms of Service](https://www.tapnow.ai/terms-of-service) |
| Domains | `tapnow.ai` created 2025-01-23 (GoDaddy, registrant shielded by Domains By Proxy, AWS name servers); `files.tapnow.art` serves uploaded assets; `tamaredge.ai` created 2023-08-24 | WHOIS and response headers read 2026-08-26 |
| Site locales | English (default) plus `fr`, `ja`, `ko`, `zh` — 45 URLs in the sitemap across five languages | [sitemap](https://www.tapnow.ai/sitemap.xml); accessed 2026-08-26 |
| Documentation | `docs.tapnow.ai` redirects to `/zh/docs`, titled "Creative OS 文档", describing TapNow Creative OS as "全球首个AI原生创作系统" ("the world's first AI-native creation system") | [docs.tapnow.ai](https://docs.tapnow.ai/); accessed 2026-08-26 |
| Desktop app | "Download for Mac · v0.4.12 · 267 MB" | [download](https://www.tapnow.ai/download); accessed 2026-08-26 |
| Web app | `app.tapnow.ai`, titled "TapNow \| Your Agentic Creative Canvas" | [app.tapnow.ai](https://app.tapnow.ai/); accessed 2026-08-26 |
| Logos shown as customers/partners | Homepage preloads "trust icons" for Alibaba, Google Ads, Google Cloud, TikTok and YouTube under "Trusted by the world's leading creative teams" | [homepage](https://www.tapnow.ai/) response headers and page, 2026-08-26 |
| Team, headcount, founders | Not published on the site — see `Founder` | see `Notes` |

### Identity and legal entities

| Name | Type | Status | Relationship as stated | Source |
|---|---|---|---|---|
| TapNow | Current public brand | Live | The product; the Terms define TapNow as the brand Tamar AI Inc. operates | [Terms of Service](https://www.tapnow.ai/terms-of-service) |
| Tamar AI Inc. | Legal entity | Current | "a Delaware corporation that operates the Services under the TapNow brand" | [Terms of Service](https://www.tapnow.ai/terms-of-service) |
| Tamar AI (brand) | Former corporate-level brand | The `about` page returned a 404 view on 2026-08-26; last rendered content captured 2025-10-06 | Presented as "The World's Leading AI Company for Marketing", "pioneering innovations like TapNow and TapTV" | [Wayback, 2025-10-06](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about); site message bundle read 2026-08-26 |
| Tamar Edge | Name appearing in the company's recruiting email domain (`tamaredge.ai`) | Domain registered 2023-08-24; no website served | No company page explains the relationship to Tamar AI Inc. | [V2EX](https://www.v2ex.com/t/1230334); WHOIS read 2026-08-26 |
| TapTV | Product/community brand | Live, referenced in the Terms and in recruiting posts | "the TapTV community"; described as "面向内容消费与创作者连接的新产品方向" | [Terms of Service](https://www.tapnow.ai/terms-of-service), [V2EX](https://www.v2ex.com/t/1230334) |
| TapNow (Sango Technologies) | Unrelated company with the same product name | Separate company | A Tokyo-based photo-and-video sharing social app founded 2022; funding databases and vendor case studies return it for "TapNow" | [Tracxn](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8), [Mixpanel](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/) |
| tamar.ai | Unrelated website | Live | A UAE corporate-tax compliance site; no connection found | [tamar.ai](https://tamar.ai/); accessed 2026-08-26 |

The site's own internationalisation bundle still carries the removed page's metadata — "Tamar AI｜The World's Leading AI Company for Marketing" and a careers title "Join the World's Leading AI Company for Marketing and Ecommerce" — even though both pages now render the 404 view ([archived page source, 2026-04-27](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about)). No registry filing for Tamar AI Inc. was retrieved, and no company page names a Chinese or Hong Kong operating entity, despite the Shenzhen hiring — see `Notes`.

---

## Product

The homepage states: "TapNow is the best way to create with AI Agents. Orchestrate text, image, audio, and video models. Zero friction." ([homepage](https://www.tapnow.ai/); accessed 2026-08-26). The Terms describe the Services as "online creative tools for managing materials, organizing and editing content, collaborating on projects, generating or transforming content using artificial intelligence" ([Terms of Service](https://www.tapnow.ai/terms-of-service)).

### Surfaces

| Surface | What it is | Source |
|---|---|---|
| Web app | `app.tapnow.ai`, "Your Agentic Creative Canvas" | [app.tapnow.ai](https://app.tapnow.ai/) |
| Desktop app | "Your Creative OS now on desktop … Bring TapNow to your desktop, and connect it to your local creative files"; macOS, v0.4.12, 267 MB; reads local project folders with permission | [download](https://www.tapnow.ai/download) |
| Documentation | `docs.tapnow.ai`, Chinese by default, "Creative OS 文档" | [docs.tapnow.ai](https://docs.tapnow.ai/) |
| TapTV | Community product referenced in the Terms and described in recruiting as a "新产品方向" for content consumption and creator connection | [Terms](https://www.tapnow.ai/terms-of-service), [V2EX](https://www.v2ex.com/t/1230334) |
| Enterprise | "Creative OS for Teams" with workspaces, members, shared credits and usage oversight; sold through "Contact sales" | [enterprise](https://www.tapnow.ai/enterprise) |
| Manifesto | A written statement of the product's conceptual model, "WRITTEN IN AUTUMN 2025" | [manifesto](https://www.tapnow.ai/manifesto) |

### The canvas model as described

The manifesto defines the product's vocabulary: "Node is the Vocabulary, the atom of your idea. Wire is the Logic, the flow of your thoughts. Group is the Phrase, crystallizing know-how into reusable Chapters. Canvas is the Universe—an infinite space" ([manifesto](https://www.tapnow.ai/manifesto); written autumn 2025). It frames the problem as "Friction" between imagination and creation and argues for a "Skillset Collapse" in which roles dissolve: "We serve Intent, not Identity."

The desktop page and recruiting posts add the working surfaces: skills ("Skill Creator", "Manage skill"), plugins, flow folders, storyboard planning, and — in the QA role posting — "画布、节点、3D 节点与 Playlist" as the shared workspace for humans and agents ([download](https://www.tapnow.ai/download), [V2EX](https://www.v2ex.com/t/1232468)). Model names visible in the product mock-ups include "Banana Pro", a "Seedance Prompt Copilot" and "Sonnet 5" ([download](https://www.tapnow.ai/download); read 2026-08-26).

### Commercialization

| Item | Detail | Source |
|---|---|---|
| Plan tiers | The pricing page's payload names Free, Pro, Team and Enterprise tiers; the amounts are rendered client-side and are not present in the served HTML | [pricing](https://www.tapnow.ai/pricing); inspected 2026-08-26 |
| Credits | Enterprise administration covers "Credits — Allocate shared credits where they are needed" and "Usage — See activity across the organization" | [enterprise](https://www.tapnow.ai/enterprise) |
| Enterprise sales | "Contact sales"; no public price list, minimum or contract term | [enterprise](https://www.tapnow.ai/enterprise) |
| Commercial-use licence | A separate "AI Generated Content Use and Commercial License" grants users worldwide, non-exclusive rights to "copy, edit, adapt, publish, distribute, display, and commercially monetize the relevant generated content", with "no separate license fee … for the uses listed in the project license certificate" | [content licence](https://www.tapnow.ai/generated-content-license); Version 1.1, effective 2026-08-06 |
| Project license certificate | TapNow "may issue a project license certificate for eligible projects and specific exported files", recording model/API version, generation time, exported file, licence scope, labelling status and current status; explicitly "not a copyright registration certificate or a guarantee of third-party rights" | [content licence](https://www.tapnow.ai/generated-content-license) |
| Licence limits | The licence "does not authorize independent sublicensing, resale, stock-library distribution, model training or improvement, incorporation into a product or API, or continued use outside that project" | [content licence](https://www.tapnow.ai/generated-content-license) |
| AI labelling | "Where applicable law requires labeling, TapNow will add the required explicit and implicit labels"; users must not remove or forge them; "TapNow will retain recipient information and related logs for at least six months" | [content licence](https://www.tapnow.ai/generated-content-license) |

### Reported scale over time

| Date | Figure or event | Source |
|---|---|---|
| 2023-08-24 | `tamaredge.ai` domain registered | WHOIS read 2026-08-26 |
| 2025-01-23 | `tapnow.ai` domain registered | WHOIS read 2026-08-26 |
| 2025-09-01 | Terms of Service and Privacy Policy last updated, naming Tamar AI Inc. | [Terms](https://www.tapnow.ai/terms-of-service), [Privacy Policy](https://www.tapnow.ai/privacy-policy) |
| 2025-10-06 | Archived `about` page presents Tamar AI as an e-commerce marketing AI company that has "empowered thousands of e-commerce sellers" | [Wayback](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about) |
| Autumn 2025 | The TapNow Manifesto is written | [manifesto](https://www.tapnow.ai/manifesto) |
| 2026-04-27 | The `about` page already renders the 404 view in archived captures | [Wayback](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about) |
| 2026-08-06 / 2026-08-10 | AI Generated Content Use and Commercial License v1.1 takes effect and is updated | [content licence](https://www.tapnow.ai/generated-content-license) |
| Undated recruiting post | "TapNow 目前已经拥有上百万用户，日活也保持在不错的水平"; a collaboration with 影视飓风 on an introductory AI course is cited | [V2EX](https://www.v2ex.com/t/1230334) |
| July 2026 reference period | Similarweb: 984K visits, global rank #55,436, China rank #3,492, category rank #514 in Social Media Networks, bounce rate 36.33%, 3.35 pages per visit, 3m11s average duration; China 55.31%, United States 17.53%, Japan 8.53%, Hong Kong 5.06%, Singapore 3.72%; direct traffic 62.63% | [Similarweb](https://www.similarweb.com/website/tapnow.ai/) |
| Accessed 2026-08-26 | Desktop app at v0.4.12 (267 MB) | [download](https://www.tapnow.ai/download) |

No revenue, subscriber, paid-seat or generation figure is published by the company.

### Public programs and partners

The enterprise page lists three named public programs: "TapNow × Kaadas — AI Smart Lock Creative Challenge", "Lenovo AI × TapNow — World Cup AI Creation Competition", and "Happy Horse × Alibaba Cloud × TapNow — AI Music Video Competition" ([enterprise](https://www.tapnow.ai/enterprise); accessed 2026-08-26). The homepage displays logo icons for Alibaba, Google Ads, Google Cloud, TikTok and YouTube under "Trusted by the world's leading creative teams"; no page explains whether these denote customers, integrations or advertising channels — see `Notes`.

### Security and administration claims

The enterprise page states: "Training data protection — Without explicit authorization, non-public customer content is not used to train general-purpose models offered to unrelated third parties"; "Identity management — Secure access with SAML SSO"; "SCIM user provisioning"; "Global compliance — Meet GDPR and CCPA requirements"; "Third-party certified — SOC 2 Type 2 with annual penetration testing"; and "Data protection — AES-256 at rest. TLS 1.2+ in transit" ([enterprise](https://www.tapnow.ai/enterprise); accessed 2026-08-26). No certificate number, auditor, audit period or trust portal is published.

---

## Founder

No founder, executive or team page exists on `www.tapnow.ai`; the careers page describes the company only as "a small, focused team spanning product, design, engineering, and content" ([careers](https://www.tapnow.ai/careers); accessed 2026-08-26).

The only individual identifiable from a first-party source is the author of the company's recruiting posts, who introduces himself as "老胡, 目前负责 TapNow 的技术方向" ("Lao Hu, currently responsible for TapNow's technical direction") and gives the contact address `andy.hu@tamaredge.ai` ([V2EX](https://www.v2ex.com/t/1230334); accessed 2026-08-26). No title, biography or employment history is published.

Third-party AI-generated aggregator pages circulate additional names and a Chinese corporate structure for TapNow. None of it could be traced to a filing, a company page or a named journalist, and it is therefore not reproduced here — see `Notes`.

The careers page does describe the hiring process in four stages: "Get to know each other", "Work through a real problem", "Meet the team", and "Decide together", alongside three stated principles — "Stay at the frontier", "Own the whole problem", "Be direct, build fast" ([careers](https://www.tapnow.ai/careers)).

---

## Funding

No financing announcement by this company was found in the reviewed public sources as of 2026-08-26. There is no press page, investor page or funding statement on `tapnow.ai`, and neither the Terms nor the archived corporate positioning mentions investors.

| Source | What it describes | Why it does not apply |
|---|---|---|
| [Tracxn — "TapNow"](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8) (page last updated 2026-08-17) | "TapNow has raised a total funding of $1.94M over 1 round. Its latest funding round was a Series A round on Oct 16, 2023", founded 2022, headquartered in Tokyo, investors SBI Investment and DIMENSION | The profile describes an app for sharing "photos and videos with friends" based in Tokyo — a different company from the Delaware-incorporated, Shenzhen-staffed creative-canvas company at `tapnow.ai` |
| [Mixpanel customer story](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/) | "a social networking app created by Sango Technologies", 2 million users, CEO Yuma Noma, 50% retention increase | Same Tokyo company; the metrics belong to it, not to `tapnow.ai` |

Amount, round, investors and valuation for `tapnow.ai` are not established by any source reviewed.

---

## Engineering

### Technology stack and platforms

No stack page is published. Items below were confirmed from the served application, its assets and the company's own recruiting posts (all observed 2026-08-26).

- **Web front end:** Next.js App Router (`x-powered-by: Next.js`, `_next/static` assets, RSC vary headers), served behind `Google Frontend`; DNS is hosted on AWS Route 53 name servers, and the apex resolves to both a Vercel address (`76.76.21.21`) and a Google Cloud address.
- **Asset host:** uploaded and generated media are served from `files.tapnow.art` under `/api/conversation/storage/uploads/…`, a separate domain from the marketing site.
- **Instrumentation:** the page bundles reference Sentry and Mixpanel (`api.mixpanel.com`, `api-js.mixpanel.com`).
- **Desktop client:** a 267 MB macOS build (v0.4.12) that reads local folders with permission and exposes plugins, skills and attachments — the download page shows it reading `~/Creative/Projects/…` and referencing `.psd`, `.fig`, `.mp4` and `.pdf` assets.
- **Documentation and locales:** documentation defaults to Chinese (`docs.tapnow.ai/zh/docs`) while the marketing site defaults to English with `fr`, `ja`, `ko` and `zh` alternates.
- **Model orchestration:** the product is described as orchestrating "text, image, audio, and video models"; UI mock-ups name "Banana Pro", "Seedance Prompt Copilot" and "Sonnet 5", but no page states which providers are used in production.
- **Data flows (first-party statement):** "Our Services may transmit prompts, files, or other necessary content to cloud providers, model providers, and other technical service providers that help us perform the requested operation" ([Privacy Policy](https://www.tapnow.ai/privacy-policy)).
- **No public code:** no GitHub organisation or package presence under the brand was found.

### Systems

| System | What it does | Source |
|---|---|---|
| Agentic canvas | Nodes, wires, groups and an infinite canvas as the shared workspace for users and agents, with 3D nodes and playlists | [manifesto](https://www.tapnow.ai/manifesto), [V2EX](https://www.v2ex.com/t/1232468) |
| Multi-model orchestration | Routing a single creative task across text, image, audio and video models | [homepage](https://www.tapnow.ai/) |
| Skills and plugins | User-created "skills" with a Skill Creator and management surface, plus a plugin system | [download](https://www.tapnow.ai/download) |
| Local file bridge | Desktop client reads local project folders with permission and brings them into the canvas as context | [download](https://www.tapnow.ai/download) |
| Workspace administration | Workspaces, organization-level members, shared credit allocation and usage reporting | [enterprise](https://www.tapnow.ai/enterprise) |
| Licence certification | Issuing and verifying project license certificates for exported files, including labelling status and an online verification page | [content licence](https://www.tapnow.ai/generated-content-license) |
| AI content labelling | Adding legally required explicit and implicit labels to outputs, with recipient information and logs retained "for at least six months" | [content licence](https://www.tapnow.ai/generated-content-license) |
| Internal agent tooling | The company describes running as "一个完全 AI Native 的团队", treating agents as production units, with a TDD-first QA agent that generates and maintains test cases, evaluated through `eval` harnesses | [V2EX](https://www.v2ex.com/t/1232468) |

### Data handling as documented

The Privacy Policy states that Tamar AI Inc. collects account and contact information and "Customer Content, such as prompts, instructions, uploaded images, video, audio, text, project files, comments, reference materials"; that content may be transmitted to "cloud providers, model providers, and other technical service providers"; and, on training: "Unless you provide separate affirmative authorization, TapNow will not use non-public Customer Content to train or improve a general-purpose model offered to unrelated third parties. We may use aggregated or de-identified information and limited controlled evaluation data to improve the functionality, safety, and reliability of the Services" ([Privacy Policy](https://www.tapnow.ai/privacy-policy); Last Updated 2025-09-01).

It further states that TapNow "does not sell personal information for money" and does not share personal information for cross-context behavioural advertising as defined by the CCPA; that retention is "only for as long as reasonably necessary for the purposes described in this Policy" without fixed periods; and that processing may occur "in the United States and other countries where we or our providers operate", with "contractual, organizational, or other lawful measures for cross-border transfers". No subprocessor list, cloud provider or model provider is named.

### Technical background sought

The company's public hiring is done through its own careers page and Chinese developer forums. A recruiting post by the person leading TapNow's technical direction lists seven open roles with monthly salary bands in RMB ([V2EX](https://www.v2ex.com/t/1230334); accessed 2026-08-26):

| Role | Band (RMB/month) |
|---|---|
| 全栈工程师 (full-stack engineer) | 35k–65k |
| 客户端工程师 (client engineer) | 15k–35k |
| 客户端工程师，3D 创作方向 (client engineer, 3D) | 20k–65k |
| 后端工程师，Agent 方向 (backend, agent) | 20k–40k |
| 后端工程师，AI 产品方向 (backend, AI product) | 28k–40k |
| Agent 开发工程师，测试方向 (agent engineer, QA) | 12k–25k |
| 运维工程师 (SRE/ops) | 15k–25k |

The same post frames the profiles it wants as "原型探索者（Prototyper）", "建造者（Builder）", "清道夫（Sweeper）", "增长者（Grower）" and "维护者（Maintainer）". The QA posting is explicit that it is not looking for a conventional test engineer: "我们不想再招一个亲自做测试的人，而是想招一个让 Agent 学会做测试的人" ("we don't want to hire someone who does the testing themselves, but someone who teaches the Agent to test"), and states that treating "会写 Playwright 、Pytest" as the endpoint of quality engineering makes the role a poor fit; the work is designing harnesses that let agents generate, extend, deduplicate and maintain test cases, verified through evals ([V2EX](https://www.v2ex.com/t/1232468)).

### Industry domain

The work spans agentic orchestration across multi-modal generation models, infinite-canvas and node-graph interaction design, desktop client work with local filesystem integration, 3D creation, and enterprise administration (SSO, SCIM, workspace and credit governance). It also carries a substantial content-compliance surface: commercial-use licensing of AI outputs, project license certificates, AI content labelling obligations with six-month log retention, and GDPR/CCPA handling ([content licence](https://www.tapnow.ai/generated-content-license), [enterprise](https://www.tapnow.ai/enterprise), [Privacy Policy](https://www.tapnow.ai/privacy-policy)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Careers page | `tapnow.ai/careers`, headed "SHENZHEN · OPEN ROLES"; the role list itself renders client-side | [careers](https://www.tapnow.ai/careers); accessed 2026-08-26 |
| Location | Shenzhen; one posting is headed "深圳" | [careers](https://www.tapnow.ai/careers), [V2EX](https://www.v2ex.com/t/1232468) |
| Published salary bands | Seven engineering roles at 12k–65k RMB per month, via the company's V2EX recruiting post | [V2EX](https://www.v2ex.com/t/1230334) |
| Stated culture | "High standards, High trust"; "We're a small, cross-disciplinary team. We speak plainly, trust one another, and take responsibility for the outcome"; the Chinese post says "我们崇尚积极、直接、务实的团队文化" | [careers](https://www.tapnow.ai/careers), [V2EX](https://www.v2ex.com/t/1230334) |
| Hiring process | Four stages: get to know each other, work through a real problem, meet the team, decide together | [careers](https://www.tapnow.ai/careers) |
| Application channels | The careers page's "Explore open roles"; WeChat `zhidengfacai` and `andy.hu@tamaredge.ai` in the V2EX post | [careers](https://www.tapnow.ai/careers), [V2EX](https://www.v2ex.com/t/1230334) |
| Headcount, benefits, remote policy, equity | Not published | see `Notes` |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-08-26): `www.tapnow.ai` homepage, `/manifesto`, `/download`, `/enterprise`, `/pricing`, `/careers`, `/terms-of-service`, `/privacy-policy`, `/generated-content-license`, `/community-guidelines`, `robots.txt` and `sitemap.xml` (45 URLs across five locales); probes of `/about`, `/en/about`, `/contact`, `/blog`, `/news`, `/company` and `/legal`; the pricing page's JavaScript chunks and the site's network hosts; `app.tapnow.ai`, `docs.tapnow.ai`, `files.tapnow.art`, `api.tapnow.ai` and `tamaredge.ai`; WHOIS for `tapnow.ai` and `tamaredge.ai`; Internet Archive CDX indexes and dated captures of `tapnow.ai`, `/about`, `/en/about` and `/zh/about`; Similarweb; Tracxn; the Mixpanel customer story; the company's V2EX recruiting posts; and English and Chinese searches on TapNow, Tamar AI, Tamar Edge and the Shenzhen entity names.
 
- **Founders, executives and headcount.** No team or about page exists on the live site; only one person is identifiable, through a recruiting post, and no title or biography is published.
- **Corporate registration and group structure.** No filing for Tamar AI Inc. was retrieved, and no company page explains the relationship between the Delaware entity, the `tamaredge.ai` email domain and the Shenzhen-based team.
- **Pricing.** Plan names (Free, Pro, Team, Enterprise) appear in the page payload, but no amount, credit allowance or billing period is rendered server-side, and enterprise pricing is "Contact sales" only.
- **Any funding, revenue, user or usage figure from the company.** The only scale statement found is the unquantified "上百万用户" in a recruiting post; nothing is published on the site itself.
- **Models and providers.** The product orchestrates third-party models but names none in production; the Privacy Policy refers only to "model providers".
- **Evidence for the enterprise security claims.** SOC 2 Type 2, penetration testing, SSO, SCIM and encryption are asserted with no certificate number, auditor, report request path or trust portal.
- **What the homepage logo strip means.** Alibaba, Google Ads, Google Cloud, TikTok and YouTube appear as "trust icons" without any statement of the relationship.
- **Retention periods and subprocessors.** The Privacy Policy states no fixed retention period and names no subprocessor, cloud provider or region.
- **Sources that could not be read on 2026-08-26:** `tapnow.ai` in the in-app browser (navigation denied by the browsing surface, so all live-site facts here come from HTTP fetches and archived captures); `tamaredge.ai` (no response); Crunchbase-class databases for this company (only the unrelated Tokyo TapNow is profiled).

### Inconsistencies across sources

- **Two unrelated companies share the product name.** Funding databases and vendor case studies return a Tokyo social app by Sango Technologies — founded 2022, US$1.94M raised, 2 million users, CEO Yuma Noma — for the query "TapNow" ([Tracxn](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8), [Mixpanel](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/)). None of those figures belongs to `tapnow.ai`.
- **The corporate positioning changed and the evidence was removed.** In October 2025 the site presented Tamar AI as a marketing and e-commerce AI company serving "thousands of e-commerce sellers" and providing "technical services to major corporations, including industry giants like Google and Amazon" ([Wayback](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)); by April 2026 the `about` page rendered a 404 view, while the site's message bundle still carries its old title ([Wayback](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about)). No statement explains the change.
- **Jurisdiction versus staffing.** The Terms bind users to a Delaware corporation and state that they "apply to individuals and organizations that access or use the Services in the United States", while the careers page and recruiting posts place the team in Shenzhen and the documentation defaults to Chinese ([Terms](https://www.tapnow.ai/terms-of-service), [careers](https://www.tapnow.ai/careers), [docs](https://docs.tapnow.ai/)).
- **"World's first" claims.** The documentation calls Creative OS "全球首个AI原生创作系统" ("the world's first AI-native creation system") and the archived about page called Tamar AI "The World's Leading AI Company for Marketing"; neither claim is sourced or defined on any page ([docs](https://docs.tapnow.ai/), [Wayback](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about)).
- **Traffic geography versus stated market.** The English-first marketing site and Delaware entity sit alongside traffic that Similarweb places at 55.31% China, and a documentation site that defaults to Chinese ([Similarweb](https://www.similarweb.com/website/tapnow.ai/), [docs](https://docs.tapnow.ai/)).
- **Unverified third-party company profiles.** AI-generated aggregator pages assert a specific Chinese operating entity, a Hong Kong company and named executives for TapNow. None could be traced to a registry, a company page or a named journalist, and the same class of page also conflates the two TapNows, so those claims are not reproduced here.

### Other

- **The legal stack is unusually developed for the size of the public footprint.** Alongside standard terms and a privacy policy, the company publishes a versioned "AI Generated Content Use and Commercial License" (v1.1, effective 2026-08-06) that introduces per-project licence certificates, addresses AI-labelling duties, commits to at least six months of recipient logs, and states that in a conflict between the Japanese, English and Chinese versions "the English version prevails" ([content licence](https://www.tapnow.ai/generated-content-license)).
- **The licence explicitly protects against retroactive revocation.** For content exported while a certificate is valid, "TapNow generally will not retroactively cancel the license listed in the certificate solely because a subscription later expires, a model is later discontinued, or rules generally change", subject to listed exceptions ([content licence](https://www.tapnow.ai/generated-content-license)).
- **The company hires around agents rather than headcount.** Its QA posting argues that "当 Agent 可以快速完成开发，质量就会成为整个生产系统能否闭环的关键" ("once agents can complete development quickly, quality becomes the key to closing the loop of the whole production system") and asks for someone to tune a QA agent rather than run tests ([V2EX](https://www.v2ex.com/t/1232468)).
- **Marketing is programme-led.** The three named public programmes pair TapNow with Kaadas, Lenovo and Alibaba Cloud, and a recruiting post cites a course collaboration with 影视飓风, a large Chinese video-production channel ([enterprise](https://www.tapnow.ai/enterprise), [V2EX](https://www.v2ex.com/t/1230334)).
- **Product surfaces are split across three domains:** marketing on `tapnow.ai`, the application on `app.tapnow.ai`, and user assets on `files.tapnow.art` (observed 2026-08-26).

---

## Resources

**Official**

- [Homepage](https://www.tapnow.ai/) · [Manifesto](https://www.tapnow.ai/manifesto) · [Download](https://www.tapnow.ai/download) · [Enterprise](https://www.tapnow.ai/enterprise) · [Pricing](https://www.tapnow.ai/pricing) · [Careers](https://www.tapnow.ai/careers)
- [Terms of Service](https://www.tapnow.ai/terms-of-service) (Last updated 2025-09-01) · [Privacy Policy](https://www.tapnow.ai/privacy-policy) (Last Updated 2025-09-01) · [AI Generated Content Use and Commercial License](https://www.tapnow.ai/generated-content-license) (v1.1, effective 2026-08-06) · [Community Guidelines](https://www.tapnow.ai/community-guidelines)
- [Web app](https://app.tapnow.ai/) · [Documentation (Chinese by default)](https://docs.tapnow.ai/) · [robots.txt](https://www.tapnow.ai/robots.txt) · [sitemap](https://www.tapnow.ai/sitemap.xml)
- Company recruiting posts — [V2EX: TapNow 诚邀各位英雄好汉加入（roles and salary bands）](https://www.v2ex.com/t/1230334) · [V2EX: Agent 工程师（QA 方向）](https://www.v2ex.com/t/1232468)
- Archived former positioning — [Tamar AI about page, captured 2025-10-06](https://web.archive.org/web/20251006014746/https://www.tapnow.ai/en/about) · [about page rendering 404, captured 2026-04-27](https://web.archive.org/web/20260427120417/https://www.tapnow.ai/about)

**Third-party profiles and name collisions**

- [Similarweb — tapnow.ai](https://www.similarweb.com/website/tapnow.ai/)
- [AMZ123 — Tamar AI profile, describing the Llamrei and Lamta e-commerce products (ZH)](https://www.amz123.com/tamarai/introduction)
- Not this company — [Tracxn — TapNow (Tokyo photo/video sharing app)](https://tracxn.com/d/companies/tapnow/__HPqEiiWGwBONXgMMMHXzuXic-5-PzwEH7c5Ugd9iTQ8) · [Mixpanel customer story — TapNow by Sango Technologies](https://mixpanel.com/customers/how-tapnow-increased-rentention-with-mixpanel/) · [tamar.ai — unrelated UAE tax-compliance site](https://tamar.ai/)
