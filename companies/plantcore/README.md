# Plantcore AI

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-12.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Plantcore AI (Chinese brand 工核; also written Plantcore.AI and PlantCore) is an early-stage industrial-AI startup that describes itself as a "中美双中心（杭州、波士顿）" company with its office in Hangzhou's Linping district or in Boston ([V2EX hiring post, 2026-01-02](https://www.v2ex.com/t/1182662)). Its LinkedIn page gives the founding year as 2025 ([LinkedIn](https://www.linkedin.com/company/plantcore-ai); accessed 2026-10-12). The current site says: "Plantcore builds AI systems for industry. We deploy customer requirements on Praxis AIP for large enterprises and build Plantcore Workbench for smaller factories. Iteron, industrial RL environments and research into model control advance our goal: AI that progressively takes over production." ([plantcore.ai](https://plantcore.ai/), English text; accessed 2026-10-12).

- **Scale:** No customer count is published. A January 2026 hiring post says "现有稳定 ToB 客户" (has stable B2B customers) ([V2EX, 2026-01-02](https://www.v2ex.com/t/1182662)). An undated Sinthome page lists "2 AI Agents in Production" ([Sinthome](https://sinthome-website.vercel.app/what-we-do/plantcore-ai)).
- **Funding:** No round has been announced. The only figure found is "$28K Seed Funding" under "Stage 1 Development Funded" on the same undated Sinthome page — see `Funding`.
- **Team:** LinkedIn shows a company-size band of "11-50 employees" but lists "4 employees" ([LinkedIn](https://www.linkedin.com/company/plantcore-ai); accessed 2026-10-12). The named co-founder is Yitian Lyu. A separate Hangzhou company, 工核智能, is reported as a one-person company led by 蔡治郅; whether it is Plantcore's operating entity is not confirmed — see `Identity and legal entities`.
- **Engineering:** The public open-source work is Iteron, a pre-alpha Rust agent runtime under Apache-2.0 (latest release v0.0.26, 2026-09-29) ([GitHub](https://github.com/Plantcore-AI/Iteron/releases)). The January 2026 CTO/founding-engineer post required Python (Node.js), React, AWS/GCP and Docker/K8s, and listed English as a working language as a plus ([V2EX, 2026-01-02](https://www.v2ex.com/t/1182662)).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | "工核 Plantcore AI \| 让 AI 接管工厂的工作" (Chinese page title); "Plantcore AI \| AI for autonomous factories" (English title) | [plantcore.ai](https://plantcore.ai/) and its `script.js`; accessed 2026-10-12 |
| Self-description | "Industrial delivery, Plantcore Workbench, Iteron and foundational research toward autonomous factories." | English meta description in [plantcore.ai](https://plantcore.ai/) `script.js`; accessed 2026-10-12 |
| Legal entity | Not named on the site, which has no terms, privacy policy or imprint | [plantcore.ai](https://plantcore.ai/); accessed 2026-10-12 |
| Founded | "2025" | [LinkedIn](https://www.linkedin.com/company/plantcore-ai); accessed 2026-10-12 |
| Locations | "中美双中心（杭州、波士顿）"; office "杭州市临平区（或波士顿线下办公）". In a reply on 2026-01-03 the poster added "目前业务主要在国内" (the business is currently mainly in China). | [V2EX, 2026-01-02](https://www.v2ex.com/t/1182662) |
| Headcount | Size band "11-50 employees"; "Discover all 4 employees" | [LinkedIn](https://www.linkedin.com/company/plantcore-ai); accessed 2026-10-12 |
| Named people | Co-founder Yitian Lyu; Xinkai Sun (posted the hiring thread from an `@plantcore.ai` address); Jamal Cao (creator and Owner of Iteron) — see `Founder` | see `Founder` |
| Customers, total raised, investors | None published — see `Product` and `Funding` | — |
| Domain | `plantcore.ai`, created 2025-10-10, registrar Cloudflare, registrant country US; DNS on Cloudflare; mail on Google Workspace | WHOIS and DNS; read 2026-10-12 |
| GitHub | Organization `Plantcore-AI`, display name "Plantcore.AI", created 2025-09-29, 8 public repositories; no blog, email, location or X account set | [GitHub API](https://api.github.com/orgs/Plantcore-AI); read 2026-10-12 |
| Contact | The current site's contact buttons point to the GitHub organization ("Connect with Plantcore on GitHub"); no email address is given. An earlier version of the site listed `sky.lyu@plantcore.ai`. | [plantcore.ai](https://plantcore.ai/); [Wayback, 2026-03-15](https://web.archive.org/web/20260315225845/https://www.plantcore.ai/) |
| Social | LinkedIn company page, 24 followers; YouTube channel `@plantcore-ai` with two videos: "Workforce Planning Workflow Demo" (2025-11-11) and "Plantcore.AI Founder Video" (2025-11-18) | [LinkedIn](https://www.linkedin.com/company/plantcore-ai), [YouTube](https://www.youtube.com/@plantcore-ai); accessed 2026-10-12 |

**Government programs.** Hangzhou media report that 工核智能 started in the 才立方 OPC ("one-person company") community in Linping, which offered "低门槛注册、免费办公空间、全程代办服务、大学生创业补贴" (low-threshold registration, free office space, full agency services, student-entrepreneur subsidies). The person running it is quoted as saying "在临平，各类补贴政策让我们这样的初创团队几乎没有经济压力" (in Linping, the various subsidy policies leave a startup team like ours with almost no financial pressure) ([杭州网, 2026-02-12](https://ori.hangzhou.com.cn/ornews/content/2026-02/12/content_9177556.htm)). These reports concern 工核智能. Its link to Plantcore is unconfirmed, as the table below explains.

### Identity and legal entities

| Name | Type | Period / status | Relationship and detail | Source |
|---|---|---|---|---|
| Plantcore AI / Plantcore.AI / 工核 | Current brand | Brand in use on `plantcore.ai`, LinkedIn, YouTube and GitHub in 2025–2026 | The Chinese name 工核 appears only on the current site | [plantcore.ai](https://plantcore.ai/), [LinkedIn](https://www.linkedin.com/company/plantcore-ai) |
| PlantCore | Spelling variant | Used in Iteron's contract files ("PlantCore resident bridge") and a December 2025 demo ("PlantCore APS") | Same brand, different capitalization | [Iteron `contracts/plantcore`](https://github.com/Plantcore-AI/Iteron/blob/main/contracts/plantcore/README.md), [plantcore-aps-frontend](https://github.com/Plantcore-AI/plantcore-aps-frontend) |
| 工核智能 | Chinese company reported by local media | Founded "2025年10月", in Hangzhou's Linping district | Reported as run by 蔡治郅 as a one-person company, using a "双中心" (two-centre) model: Cai handles industrial demand in China and "海外合伙人联动前沿技术" (an overseas partner links in frontier technology). The partner is described as "一位常驻美国的留学生朋友" (a friend studying in, and based in, the US). Neither article mentions Plantcore or `plantcore.ai`. The registered full name was not retrieved. | [杭州网, 2026-02-12](https://ori.hangzhou.com.cn/ornews/content/2026-02/12/content_9177556.htm); [临平区融媒体中心 via 凤凰网浙江, 2026-02-05](https://zj.ifeng.com/c/8qTmGc2Exts) |
| Sinthome | Related organization | Self-reported founding date 2023-02-02 | Describes itself as "a public-interest community" that "has evolved into an incubator-style public benefit platform". It lists "Industrial Vertical LLMs Research — Developing AI technologies for public good and specialized applications through PlantCore AI" among its current practices and hosts a Plantcore AI project page. Plantcore's LinkedIn "Website" field points to that Sinthome page. No ownership or legal relationship is stated. | [Sinthome — Who We Are](https://sinthome-website.vercel.app/who-we-are), [Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai), [LinkedIn](https://www.linkedin.com/company/plantcore-ai) |
| FluxSync | Name used in two demo repositories | December 2025 | "FluxSync APS" and "FluxSync AI Console" front-end demos in the `Plantcore-AI` organization; the name appears in no other source | [fluxsync-aps-frontend](https://github.com/Plantcore-AI/fluxsync-aps-frontend), [fluxsync-ai-console](https://github.com/Plantcore-AI/fluxsync-ai-console) |

Researcher inference, not a confirmed relationship: 工核智能 and Plantcore share the Chinese name 工核, a Linping office, a Hangzhou-plus-US two-centre setup, and an October 2025 start (the domain was registered on 2025-10-10). No source found on 2026-10-12 states that they are the same business. The corporate-registry mirrors 爱企查, 企查查 and 天眼查 returned access-restriction pages to automated requests that day.

---

## Product

The current site is a single bilingual page with three numbered sections plus a long-term vision ([plantcore.ai](https://plantcore.ai/); accessed 2026-10-12). It has no product documentation, pricing, sign-up or login.

### Feature areas

| Area | What the site says | Public artifact |
|---|---|---|
| 01.A — Large enterprises: FDE deployments on Praxis AIP | "Our FDE team uses Praxis AIP's capabilities to implement customer requirements as deployable industrial AI applications. Working with business, engineering and IT teams, we adapt workflows, integrate systems and deploy within each customer's operational constraints." Image caption: "Praxis AIP · The factory as an integrated system". Elsewhere: "As Praxis connects factories, supply and demand can be coordinated beyond static plans." | None. The "Discuss a Praxis AIP deployment" button links to the page's own contact anchor. The site does not say who develops Praxis AIP. |
| 01.B — Small and medium factories: Plantcore Workbench | "Plantcore Workbench provides a shared AI workspace for smaller factories. Around everyday work such as orders, inventory, scheduling and quality, users can describe tasks, explore business information, follow progress and review decisions that need their input." "Connections to existing business systems link information, task execution and feedback." | A product image (`/brand-assets/workbench.png`). The "Explore Plantcore Workbench" button links to the contact anchor. |
| 02 — Iteron (industrial agent harness) | "Iteron is our open-source runtime substrate. It organizes context, tools, execution policies and verification into modular contracts so developers can build, evaluate and govern agents for specific domains." "The current open-source release remains in early development and evaluation." Labelled "OPEN SOURCE / PRE-ALPHA". | [Plantcore-AI/Iteron](https://github.com/Plantcore-AI/Iteron) — see `Engineering` |
| 03 — Research: Cartograph | "Cartograph explores reasoning through these structures: moving from a model's probability space into industrial space, identifying relevant relationships and paths, then producing natural-language output." Framed as research into "model control". | Linked to `github.com/Plantcore-AI/cartograph`, which returned 404 (not public) on 2026-10-12 |
| 03 — Research: industrial RL environments | "We build reinforcement learning environments around these tasks, studying how to represent states, actions and feedback so agents can practice sequential decisions and undergo systematic evaluation." | No public code found |
| Long-term vision | "Our long-term vision is to use AI to bring human production toward an optimal solution and realize a cybernetic economy." This extends to cross-factory coordination of "capacity allocation, material flows and delivery schedules". The page labels this "a long-term research and development direction". | — |

### Positioning over time

| Date | Source | How the company described itself |
|---|---|---|
| Undated (footer "© 2025") | [Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai) | "Building the first Industrial Vertical Large Language Model". A three-layer plan: "AI Agents" (2025-2026), "CDO Data Platform" capturing "Contextualized Decision Outcomes" (2026-2028), and "Industrial Vertical LLM" (2028-2030). Business model as stated: "Factories pay us to deploy agents • Agents capture decision data as byproduct → Paid to build our moat". |
| Accessed 2026-10-12 (undated) | [LinkedIn About](https://www.linkedin.com/company/plantcore-ai) | "Plantcore.AI is pioneering the first industrial vertical LLM, trained on real-world Context–Decision–Outcome (CDO) data collected by autonomous AI agents on real factory floors." Specialties: "Data Engineering, AI Infrastructure, Decision Intelligence, Applied AI Research, and Factory Automation". |
| 2025-11-11 | [YouTube](https://www.youtube.com/watch?v=hGRDCEBRocw) | Demo video titled "Workforce Planning Workflow Demo" |
| Captured 2026-03-15 and 2026-04-17 | [Wayback](https://web.archive.org/web/20260315225845/https://www.plantcore.ai/) (Webflow site, footer "© 2025, Plantcore.AI") | "We build AI agents that improve factory decision-making", with a waitlist. "We built Context-Decision-Outcome data structure to allow agents to coordinate and exchange state without a pre-designed architecture". |
| Captured 2026-05-15 | [Wayback](https://web.archive.org/web/20260515010358/https://plantcore.ai/) | A GoDaddy website-builder placeholder reading "Launching Soon" with a contact form |
| Accessed 2026-10-12 | [plantcore.ai](https://plantcore.ai/) | "Let AI take over factories." FDE deployments on Praxis AIP, Plantcore Workbench, Iteron, research, and a "cybernetic economy" vision |

### Commercialization

No price list or packaging is published ([plantcore.ai](https://plantcore.ai/); accessed 2026-10-12). Statements about how the company sells:

- Enterprise work is delivered by an FDE (forward-deployed engineering) team, "from requirements through operational feedback" ([plantcore.ai](https://plantcore.ai/)).
- "AI agents deliver immediate 10%+ ROI • Factories pay us to deploy agents" ([Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai); undated).
- "开发工业生产 AI Agent 服务国际市场，现有稳定 ToB 客户" (develops industrial-production AI agents for the international market; has stable B2B customers) ([V2EX, 2026-01-02](https://www.v2ex.com/t/1182662)). In a reply the next day, the same poster wrote "目前业务主要在国内" (the business is currently mainly in China).

### Reported traction

| Date | Claim | Source |
|---|---|---|
| Undated (© 2025) | "2 AI Agents in Production — Inventory Management Assistant and Export Trade Assistant deployed and operating in real factory environments" | [Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai) |
| Undated (© 2025) | "Collaborating with garment manufacturing and alloy production facilities" | same |
| Undated (© 2025) | A procurement agent from "field research at an auto parts manufacturing facility": "$40K Order Value", "$120K Cost Savings", "300% ROI", "Single procurement decision, field-validated savings" | same |
| 2026-01-02 | "现有稳定 ToB 客户" (has stable B2B customers) | [V2EX](https://www.v2ex.com/t/1182662) |
| 2026-02-12 | About 工核智能 (link to Plantcore unconfirmed): "已敲开某头部饮料加工厂及多家汽车内饰厂的大门" (has got in the door at a leading beverage processor and several automotive-interior factories); "与某头部饮料加工厂的合作已进入细节对接阶段" (the beverage-processor cooperation is at the detailed-alignment stage); overseas, "成功与一家珠宝品牌达成合作" (reached a cooperation agreement with a jewellery brand). The report says its system offers "排产优化、能耗监控、质量预警" (scheduling optimization, energy monitoring, quality alerts). | [杭州网](https://ori.hangzhou.com.cn/ornews/content/2026-02/12/content_9177556.htm) |

No customer is named in any source.

### Stated plans

From the undated Sinthome page ([Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai)), headed "Near-Term Roadmap — Next 12-18 months of execution":

- "Q1-Q2 2025 — Scale Agent Deployment: Expand to 10-15 factories • Deploy 50+ agents • Validate 10%+ ROI consistently"
- "Q3-Q4 2025 — Launch CDO Platform: Standardize decision capture • Begin cross-factory learning • Accumulate 10K+ decisions"
- "H1 2026 — Seed Round & Scale: Raise seed funding • Expand to 50+ factories • Begin LLM prototyping"
- Under "Path to 2030": "10,000 factories connected • 150,000+ agents deployed"

No later source reports progress against these targets. The current site gives no dated targets.

---

## Founder

### Yitian Lyu — co-founder

- Self-identification: "Now I am cofounding Plantcore AI, using AI AGENT to push the boundary of factory production." This is from a post by Yitian Lyu shown on the company's LinkedIn page and dated 2025-12-24 ([LinkedIn post](https://www.linkedin.com/posts/plantcore-ai_industrialai-factory-lamiation-activity-7409644843817291776-lvbN)). A search-engine result for Lyu's LinkedIn profile is titled "Yitian Lyu - Co-Founder @ Plantcore.AI" ([profile](https://www.linkedin.com/in/skylyuyitian/)). The profile itself returned HTTP 999 to automated access on 2026-10-12.
- Career facts as Lyu posted them on 2025-12-17 ([LinkedIn post](https://www.linkedin.com/posts/plantcore-ai_aistartup-verticalai-factorylife-activity-7407151209343758336-XukI)):
  - "Graduating from BC 2024, I quit IB and Phil PhD to work as rag piling worker in an auto accessory factory."
  - "I worked in six different workshops—from plastic molding, pressing, cutting, sewing, packaging, to the warehouse. I also rotated through two departments: sales and procurement."
  - Lyu designed "a new cutting SOP that reduced material waste" and wrote "a ChatGPT plugin that helped the procurement team choose orders (it saved USD 125,000 in its first week of use!)".
  - "All of these experiences became the starting point for Plantcore AI."
- The 2025-12-24 post is a "Factory Diary" from work in a lamination workshop producing sunshades on July 7 and 8 of the previous summer.
- The handle in the profile URL is `skylyuyitian`. The earlier `plantcore.ai` site listed `sky.lyu@plantcore.ai` as its contact address ([Wayback, 2026-03-15](https://web.archive.org/web/20260315225845/https://www.plantcore.ai/)).

### Other named people

| Person | What the sources say | Source |
|---|---|---|
| Xinkai Sun | Posted the CTO/founding-engineer hiring thread on 2026-01-02 as V2EX user `xinkaisun`, opening "这里是 Plantcore.AI", with contact address `xinkai.sun@plantcore.ai`. No title is stated. A search-engine result for a LinkedIn profile is titled "Xinkai Sun - Plantcore AI" (not opened; HTTP 999). | [V2EX, 2026-01-02](https://www.v2ex.com/t/1182662); [LinkedIn](https://www.linkedin.com/in/xinkai-sun-34705826b/) |
| Jamal Cao (Zheng Cao, 曹政) | "Iteron was created and is led by Jamal Cao (`@fr0m-scratch`), the project's human Owner and Project Lead". The Owner "holds final authority over every project decision". Jamal Cao is the sole code owner of every path in the repository and has 282 commits, the most of any contributor. Jamal Cao's personal site gives "PhD student in Computer Engineering at the University of Florida" and "B.S. in Computer Science with a minor in Mathematics from New York University", and calls Jamal Cao "the creator and lead developer of Iteron". The personal site does not mention Plantcore, and no source states a role at the company. | [GOVERNANCE.md](https://github.com/Plantcore-AI/Iteron/blob/main/GOVERNANCE.md), [CODEOWNERS](https://github.com/Plantcore-AI/Iteron/blob/main/.github/CODEOWNERS), [contributors API](https://api.github.com/repos/Plantcore-AI/Iteron/contributors); [jamalcao.me](https://jamalcao.me/); read 2026-10-12 |
| 蔡治郅 | "工核智能负责人" (head of 工核智能). After graduating from university, Cai "未能进入本专业领域，误打误撞进入电商行业" (did not get into their own field of study and ended up in e-commerce). As a one-person company, Cai "身兼研发、运营、销售、客户对接数职" (handles R&D, operations, sales and customer liaison). Link to Plantcore unconfirmed. | [杭州网, 2026-02-12](https://ori.hangzhou.com.cn/ornews/content/2026-02/12/content_9177556.htm) |

The site has no team page. Iteron's contributor list has four other human accounts besides the Owner, with 1 to 7 commits each. The four December 2025 demo repositories each contain a single commit from one account ([GitHub API](https://api.github.com/orgs/Plantcore-AI/repos); read 2026-10-12).

---

## Funding

| Date | Round | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Undated (page footer © 2025) | "Stage 1 Development Funded" / "Seed Funding" | "$28K" | Not named | Not stated | [Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai) |

The same page says: "Secured initial funding to develop and deploy core AI agent infrastructure." Its roadmap lists "H1 2026 — Seed Round & Scale: Raise seed funding". No announcement of a seed or later round was found as of 2026-10-12. No investor is named in any source. Separately, Hangzhou media report Linping subsidies for 工核智能 (see `Basic`).

---

## Engineering

### Technology stack and platforms

| Item | Status | Detail | Source |
|---|---|---|---|
| Rust | Confirmed (public code) | Iteron is a Rust 2024-edition workspace, MSRV 1.90, with 23 workspace members. Dependencies include tokio, reqwest (rustls), serde, ratatui/crossterm for the TUI, and ring/ed25519-dalek. The manifest says "No agent framework." | [Cargo.toml](https://github.com/Plantcore-AI/Iteron/blob/main/Cargo.toml) |
| LLM provider APIs | Confirmed (public code) | Anthropic Messages, OpenAI Responses and OpenAI-compatible Chat adapters; built-in profiles for Anthropic, OpenAI, DeepSeek, GLM, MiniMax and Fireworks | [Iteron README](https://github.com/Plantcore-AI/Iteron) |
| Sandboxing | Confirmed (public code) | macOS Seatbelt and Linux bubblewrap backends behind `--confine`; no Windows code-execution sandbox | [Iteron README](https://github.com/Plantcore-AI/Iteron), [SECURITY.md](https://github.com/Plantcore-AI/Iteron/blob/main/SECURITY.md) |
| MCP, LSP | Confirmed (public code) | MCP client and LSP crates in the workspace | [Cargo.toml](https://github.com/Plantcore-AI/Iteron/blob/main/Cargo.toml) |
| Protocol Buffers | Confirmed as a referenced file in a private repository | `contracts/proto/plantcore/control/worker/v1/worker_control.proto` in `Plantcore-AI/plantcore-platform` | [contracts/plantcore/README.md](https://github.com/Plantcore-AI/Iteron/blob/main/contracts/plantcore/README.md) |
| Qwen | Named only | "Qwen smoke" is listed among release evidence that external workflows must produce | [contracts/plantcore/README.md](https://github.com/Plantcore-AI/Iteron/blob/main/contracts/plantcore/README.md) |
| GitHub Actions; Alibaba Cloud ECS | Confirmed (public runbook) | A "loaned Aliyun ECS Windows Server box" (Windows Server 2022) serves as a self-hosted Windows CI runner for both `Plantcore-AI/Iteron` and `Plantcore-AI/plantcore-desktop`. It is provisioned with MSVC, Rust 1.90.0, Node 22, CPython 3.12, WebView2, NSIS and WiX. | [ops/windows-runner/README.md](https://github.com/Plantcore-AI/Iteron/blob/main/ops/windows-runner/README.md) |
| MkDocs, GitHub Pages | Confirmed (public code) | Iteron documentation site | [mkdocs.yml](https://github.com/Plantcore-AI/Iteron/blob/main/mkdocs.yml), [docs](https://plantcore-ai.github.io/Iteron/) |
| TypeScript, React, Next.js, Vite, Tailwind, Zustand | Confirmed in demo repositories only | December 2025 front-end demos: Next.js 16 App Router (`dynamic-scheduling-simulator`, `fluxsync-aps-frontend`); React + Vite (`fluxsync-ai-console`, `plantcore-aps-frontend`). `fluxsync-ai-console` uses TanStack Query, shadcn/ui and MSW mock APIs. The READMEs describe all four as demos; `fluxsync-ai-console` states "后端依赖：无（全部通过 MSW Mock 提供 /api/* 接口）" (backend dependency: none; all `/api/*` endpoints come from MSW mocks). | [org repositories](https://github.com/Plantcore-AI) |
| OpenAI / Claude / Gemini models | Company statement | "集成 OpenAI/Claude/Gemini 等大模型，配齐全套 AI 工具" (integrates OpenAI, Claude, Gemini and other large models; full set of AI tools) | [V2EX, 2026-01-02](https://www.v2ex.com/t/1182662) |
| Python (Node.js), RESTful API, React, JavaScript, AWS/GCP, Docker/K8s | Hiring requirement only | Listed as hard requirements for the CTO/founding-engineer role | [V2EX, 2026-01-02](https://www.v2ex.com/t/1182662) |
| PyTorch / TensorFlow / JAX | Hiring preference only | "熟练使用 PyTorch、Tensorflow 或 Jax（任意即可）" (proficient in any one of PyTorch, TensorFlow or JAX) | [V2EX, 2026-01-02](https://www.v2ex.com/t/1182662) |
| Website hosting | Observed | Current site is static HTML/CSS/JS behind Cloudflare. Earlier versions were built on Webflow (captured March–April 2026) and the GoDaddy website builder (captured May 2026). | [plantcore.ai](https://plantcore.ai/); [Wayback](https://web.archive.org/web/20260315225845/https://www.plantcore.ai/) |

### Systems

| System | Description | Source |
|---|---|---|
| Iteron | "An open-source terminal coding agent built on a bounded, observable Rust runtime." Also described as "an open-source substrate for building, evaluating, and governing harness checkpoints for domain-specific AI agents". Features: interactive TUI, one-shot text/JSON/stream-JSON output, hash-chained local sessions with resume and fork, permission modes, and bounded runs. Its status: "Iteron remains pre-alpha. It does not claim production readiness". | [README](https://github.com/Plantcore-AI/Iteron), [status](https://github.com/Plantcore-AI/Iteron/blob/main/docs/project/status.md) |
| PlantCore platform (private) | Iteron runs as a "PlantCore resident bridge" via `iteron serve --plantcore`. The contracts reference a Cloud Worker that schedules each Run in a Pod. It speaks a worker-control protocol (`worker_control.proto`, v1) and an "iteron-app-server-bridge-v2" contract with output schema v7. The Worker owns "control reconnect, the fixed 30-second window, durable outbox/ACK reconciliation, and the timeout-triggered `drain` request". "The G1 runtime capability set is supported on Linux." | [contracts/plantcore/README.md](https://github.com/Plantcore-AI/Iteron/blob/main/contracts/plantcore/README.md) |
| plantcore-desktop (private) | A repository with its own Windows CI runner (label `desktop-win`). Its purpose is not described publicly. | [ops/windows-runner/README.md](https://github.com/Plantcore-AI/Iteron/blob/main/ops/windows-runner/README.md) |
| APS and supply-chain demos | "PlantCore APS" is an advanced planning and scheduling demo "专为现代化服装制造工厂打造" (built for modern garment factories), with Gantt scheduling and AI-suggested rush-order insertion. "FluxSync APS" is a "人机协作（Human-in-the-loop）的排产决策支持系统" (human-in-the-loop scheduling decision-support system) built around baseline-vs-simulation diffs and what-if analysis. "FluxSync AI Console" is an "AI 驱动的供应链协同平台" (AI-driven supply-chain collaboration platform) with a control tower, order lifecycle, role portals, MDM and system connectors. `dynamic-scheduling-simulator` is a scheduling and rush-order simulator with a Python scheduler A/B script. | [plantcore-aps-frontend](https://github.com/Plantcore-AI/plantcore-aps-frontend), [fluxsync-aps-frontend](https://github.com/Plantcore-AI/fluxsync-aps-frontend), [fluxsync-ai-console](https://github.com/Plantcore-AI/fluxsync-ai-console), [dynamic-scheduling-simulator](https://github.com/Plantcore-AI/dynamic-scheduling-simulator) |
| Earlier agents | "Inventory Management Assistant and Export Trade Assistant", and a procurement agent that "automates price comparison, supplier inquiry, and material selection optimization" | [Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai); undated |

Public repositories in the `Plantcore-AI` organization on 2026-10-12 ([GitHub API](https://api.github.com/orgs/Plantcore-AI/repos)):

| Repository | Language | Created | Notes |
|---|---|---|---|
| `Iteron` | Rust | 2026-07-15 | Apache-2.0; 9 stars, 1 fork; 233 pull requests and 129 issues; releases v0.0.1 (2026-08-06) to v0.0.26 (2026-09-29) |
| `plantcoreai_website` | — | 2025-10-28 | MIT; README titled "Sinthome Non-Profit Website"; homepage field `sinthome-website.vercel.app`; last push 2025-10-15 |
| `dynamic-scheduling-simulator` | TypeScript | 2025-12-12 | Demo |
| `fluxsync-aps-frontend` | TypeScript | 2025-12-12 | Demo |
| `fluxsync-ai-console` | TypeScript | 2025-12-20 | Demo |
| `plantcore-aps-frontend` | TypeScript | 2025-12-21 | Demo |
| `DnD` | Python | 2026-01-03 | "A framework for running D&D-style games where both players and the Dungeon Master (DM) are powered by Large Language Models" |
| `txc_search` | — | 2026-01-12 | Empty |

### Technical background sought

From the CTO/founding-engineer post of 2026-01-02 ([V2EX](https://www.v2ex.com/t/1182662)):

- **Responsibilities:** End-to-end development of industrial AI agents, "包括：搭建前后端技术架构、产品设计、部署和落地、搭建本地 LLM" (building the front-end and back-end architecture, product design, deployment and rollout, and setting up local LLMs). Also "开发多维度评测工具，评估产品 benchmark" (building multi-dimensional evaluation tools to benchmark the product).
- **Required:** "有 0-1 端到端 AI 产品开发和落地经验（agent 开发经验最佳），可以展示产品和 demo" (end-to-end 0-to-1 AI product development and launch experience, agent development preferred, with products and demos to show). Back-end work covering RESTful API design, permission systems and data modeling. Own understanding of different LLMs "从算法到应用" (from algorithms to applications).
- **Preferred:** A computer-science or software-engineering degree. Experience with ERP, MES, SAP or similar industrial software, or with complex B2B software. Full-time development experience.

### Industry domain

- **Manufacturing operations.** The site names orders, inventory, scheduling and quality as Workbench's scope, and "time, resources and processes" as the constraints of industrial tasks ([plantcore.ai](https://plantcore.ai/)). The public demos cover production scheduling, rush-order insertion and capacity in garment factories, plus supply-chain order management ([org repositories](https://github.com/Plantcore-AI)).
- **Procurement, inventory and export trade** are the domains of the earlier agents ([Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai)).
- **Hiring.** "有工厂工作经验" (factory work experience) and ERP/MES/SAP experience are listed as preferred, not required ([V2EX, 2026-01-02](https://www.v2ex.com/t/1182662)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Location | "杭州市临平区（或波士顿线下办公）" (Linping district, Hangzhou, or on-site in Boston) | [V2EX, 2026-01-02](https://www.v2ex.com/t/1182662) |
| Working language | "英文可以作为工作语言" (English usable as a working language) is listed as a plus, not a requirement. Iteron's README is bilingual. Its issues and specs mix English and Chinese, e.g. issue #421 "Iteron：11 worktree 归档、PRD v1.1…". | [V2EX](https://www.v2ex.com/t/1182662); [Iteron issues](https://github.com/Plantcore-AI/Iteron/issues?q=is%3Aissue) |
| Salary | CTO: "30 - 40 k/月" in a 2026-01-02 reply; later the same day, "合适的话 薪资可以给到 5w-6w（税后）" (if the fit is right, 50k–60k after tax). Currency and period of the second figure are not stated. Founding engineer: "可以再沟通" (negotiable). | [V2EX](https://www.v2ex.com/t/1182662) |
| Internships | In replies to questions about internships, the poster wrote "有的" (yes) | [V2EX](https://www.v2ex.com/t/1182662) |
| Remote work, visa sponsorship, benefits, equity | Not stated | — |
| How the open-source project is run | "Each maintainer may bind one persistent coding agent to their currently declared boundaries." Agents may implement and test but "do not dispatch work to one another, negotiate interfaces, approve pull requests, merge, change release gates, or accept risk." "This is deliberately not an agent-swarm development model." | [GOVERNANCE.md](https://github.com/Plantcore-AI/Iteron/blob/main/GOVERNANCE.md) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-12):

- **Company surfaces:** `plantcore.ai` (Chinese and English text, `script.js`, `robots.txt`) and probes of `/sitemap.xml`, `/about`, `/careers`, `/jobs`, `/en` and `/llms.txt`, all 404. Internet Archive captures of `plantcore.ai` and `www.plantcore.ai`. WHOIS and DNS. The GitHub organization `Plantcore-AI`: metadata, all public repositories and contributors, and a shallow clone of Iteron. The LinkedIn company page. The YouTube channel feed.
- **Related sites:** Sinthome's site (`/`, `/who-we-are`, `/what-we-do`, `/what-we-do/plantcore-ai`) and `jamalcao.me`.
- **Hiring and registries:** V2EX. OpenCorporates. Attempted 爱企查, 企查查 and 天眼查 searches for 工核智能.
- **Media:** Sogou WeChat search for 工核智能, Plantcore and 工核 AI 工厂.
- **Web searches** in English and Chinese on Plantcore AI, 工核, 工核智能, 蔡治郅, Praxis AIP, Iteron, Yitian Lyu, Xinkai Sun and Jamal Cao.

Findings:

- **Legal entity and jurisdiction.** No entity is named on the site, and no terms or privacy policy exist. WHOIS gives only "Registrant Country: US". OpenCorporates returned only unrelated UK companies.
- **Whether 工核智能 is Plantcore's operating entity.** It has not been confirmed (see `Identity and legal entities`), and its registered full name and registration number were not retrieved.
- **What Praxis AIP is.** The site uses the name for the enterprise deployment route but does not say who develops it. No documentation, product page or other public reference was found.
- **Plantcore Workbench availability.** No sign-up, pricing, documentation or release date. The site's Workbench button links to an on-page anchor.
- **Customers.** None is named. Customer and partner descriptions are anonymous ("garment manufacturing and alloy production facilities", "某头部饮料加工厂", "一家珠宝品牌").
- **Funding beyond the undated "$28K" figure, investors, and valuation.**
- **Cartograph source code.** The site links to it, but the repository is not public.
- **Whether Jamal Cao holds a role at Plantcore.** The company calls Iteron "our open-source runtime", and Iteron's governance names Jamal Cao as Owner. Neither source nor the personal site names a company role.
- **Whether Yitian Lyu has a role at Sinthome.** Search-engine snippets for a second LinkedIn profile under the same name mention a founder and director role at Sinthome. The profiles returned HTTP 999 and could not be read, and Sinthome's site names no people.
- **Content of the "Plantcore.AI Founder Video"** (YouTube, 2025-11-18). It was not reviewed; only the title and date were read from the channel feed.
- **Engineering blog, security certifications, published salary bands beyond the V2EX replies.**

### Inconsistencies across sources

- **Procurement savings.** The Sinthome page reports "$120K Cost Savings" on a "$40K Order Value" ("300% ROI") from "field research at an auto parts manufacturing facility". Yitian Lyu's 2025-12-17 post says a ChatGPT plugin written for an auto-accessory factory's procurement team "saved USD 125,000 in its first week of use". Neither source says whether the two describe the same event ([Sinthome](https://sinthome-website.vercel.app/what-we-do/plantcore-ai); [LinkedIn post](https://www.linkedin.com/posts/plantcore-ai_aistartup-verticalai-factorylife-activity-7407151209343758336-XukI)).
- **Team size.** LinkedIn shows the "11-50 employees" band but lists 4 employees ([LinkedIn](https://www.linkedin.com/company/plantcore-ai); accessed 2026-10-12). The 2026-01-02 post describes "团队成员背景多元" (a team with diverse backgrounds) ([V2EX](https://www.v2ex.com/t/1182662)). Hangzhou media describe 工核智能 as a "一人公司" (one-person company) ([杭州网, 2026-02-12](https://ori.hangzhou.com.cn/ornews/content/2026-02/12/content_9177556.htm)).
- **Positioning.** LinkedIn and the Sinthome page still describe "the first industrial vertical LLM" built from CDO data. The current site describes FDE deployments on Praxis AIP, Plantcore Workbench, an open-source agent harness and "model control" research, and does not mention a vertical LLM or CDO data.
- **Iteron version in its own docs.** `docs/project/status.md` says "The current source workspace declares v0.0.22" and names v0.0.20 as the latest published release; the README also says v0.0.20. `Cargo.toml` declares 0.0.26, and GitHub Releases lists v0.0.26 on 2026-09-29 ([status](https://github.com/Plantcore-AI/Iteron/blob/main/docs/project/status.md), [Cargo.toml](https://github.com/Plantcore-AI/Iteron/blob/main/Cargo.toml), [releases](https://github.com/Plantcore-AI/Iteron/releases); read 2026-10-12).

### Other

- **Iteron was first published as "Core Code".** Releases v0.0.1 (2026-08-06, "Core Code v0.0.1 (macOS arm64, built outside CI)") and v0.0.2 (2026-08-07) carry that name. The v0.0.3 changelog (2026-08-10) records "Renamed Core Code, its command, packages, archives, and user-facing prose to Iteron." ([releases](https://github.com/Plantcore-AI/Iteron/releases), [CHANGELOG](https://github.com/Plantcore-AI/Iteron/blob/main/CHANGELOG.md)).
- **Iteron's security posture is stated in its README.** "Pre-alpha; new ordinary sessions default to dangerous broad host authority." "The built-in file-write boundary has an unresolved symlink race." ([README](https://github.com/Plantcore-AI/Iteron)). `SECURITY.md` describes a newer default with "the permission bypass **off** and the macOS/Linux execution sandbox **on**" ([SECURITY.md](https://github.com/Plantcore-AI/Iteron/blob/main/SECURITY.md)).
- **The organization's website repository started as another organization's site.** `plantcoreai_website` is an Astro/React project whose README describes "a modern, responsive website for Sinthome", with a clone URL under a personal account ([plantcoreai_website](https://github.com/Plantcore-AI/plantcoreai_website)).
- **Name collisions.** "Plantcore" also names a music aesthetic ([Coog Radio, 2022](https://coogradio.com/2022/02/an-introduction-to-plantcore/)) and two unrelated UK companies, PLANTCORE ENGINEERING LIMITED and PLANTCORE LTD (dissolved) ([OpenCorporates](https://opencorporates.com/companies?q=plantcore)). Chinese searches for 工核 return mostly unrelated companies with similar names, such as 智核 and 群核.

---

## Resources

**Official**

- [plantcore.ai](https://plantcore.ai/) (accessed 2026-10-12) · earlier versions: [Wayback 2026-03-15](https://web.archive.org/web/20260315225845/https://www.plantcore.ai/) · [Wayback 2026-04-17](https://web.archive.org/web/20260417113921/https://www.plantcore.ai/) · [Wayback 2026-05-15](https://web.archive.org/web/20260515010358/https://plantcore.ai/)
- [LinkedIn company page](https://www.linkedin.com/company/plantcore-ai) · posts by Yitian Lyu shown on it: [2025-12-17](https://www.linkedin.com/posts/plantcore-ai_aistartup-verticalai-factorylife-activity-7407151209343758336-XukI) · [2025-12-24](https://www.linkedin.com/posts/plantcore-ai_industrialai-factory-lamiation-activity-7409644843817291776-lvbN)
- [YouTube @plantcore-ai](https://www.youtube.com/@plantcore-ai) · [Workforce Planning Workflow Demo (2025-11-11)](https://www.youtube.com/watch?v=hGRDCEBRocw) · [Plantcore.AI Founder Video (2025-11-18)](https://www.youtube.com/watch?v=PzbCMpF0Zjw)
- GitHub — [organization `Plantcore-AI`](https://github.com/Plantcore-AI) · [org API record](https://api.github.com/orgs/Plantcore-AI)
- Iteron — [repository](https://github.com/Plantcore-AI/Iteron) · [documentation](https://plantcore-ai.github.io/Iteron/) · [releases](https://github.com/Plantcore-AI/Iteron/releases) · [CHANGELOG](https://github.com/Plantcore-AI/Iteron/blob/main/CHANGELOG.md) · [GOVERNANCE.md](https://github.com/Plantcore-AI/Iteron/blob/main/GOVERNANCE.md) · [CODEOWNERS](https://github.com/Plantcore-AI/Iteron/blob/main/.github/CODEOWNERS) · [SECURITY.md](https://github.com/Plantcore-AI/Iteron/blob/main/SECURITY.md) · [Cargo.toml](https://github.com/Plantcore-AI/Iteron/blob/main/Cargo.toml) · [project status](https://github.com/Plantcore-AI/Iteron/blob/main/docs/project/status.md) · [PlantCore contract inputs](https://github.com/Plantcore-AI/Iteron/blob/main/contracts/plantcore/README.md) · [Windows runner runbook](https://github.com/Plantcore-AI/Iteron/blob/main/ops/windows-runner/README.md)
- Demo repositories — [plantcore-aps-frontend](https://github.com/Plantcore-AI/plantcore-aps-frontend) · [fluxsync-aps-frontend](https://github.com/Plantcore-AI/fluxsync-aps-frontend) · [fluxsync-ai-console](https://github.com/Plantcore-AI/fluxsync-ai-console) · [dynamic-scheduling-simulator](https://github.com/Plantcore-AI/dynamic-scheduling-simulator) · [plantcoreai_website](https://github.com/Plantcore-AI/plantcoreai_website)

**Hiring**

- [V2EX 酷工作 — [杭州/波士顿] 初创工业 AI 公司 招募 CTO/Founding Engineer](https://www.v2ex.com/t/1182662) (posted 2026-01-02 by `xinkaisun`) `[zh]`

**Third-party coverage and profiles**

- [Sinthome — Plantcore AI](https://sinthome-website.vercel.app/what-we-do/plantcore-ai) (undated; footer © 2025) · [Sinthome — Who We Are](https://sinthome-website.vercel.app/who-we-are) · [Sinthome — What We Do](https://sinthome-website.vercel.app/what-we-do)
- [杭州网 — 【新春走基层】一个工位，一台电脑，杭州这家"一人公司"靠AI"闯"市场](https://ori.hangzhou.com.cn/ornews/content/2026-02/12/content_9177556.htm) (2026-02-12; reporter 颉月娇) `[zh]`
- [凤凰网浙江 — AI时代，临平为何布局"OPC"？](https://zj.ifeng.com/c/8qTmGc2Exts) (2026-02-05; source line "来源丨临平区融媒体中心") `[zh]`
- [jamalcao.me](https://jamalcao.me/) — personal site of Iteron's creator (accessed 2026-10-12)
- LinkedIn profiles (search-result titles only; not readable to automated access): [Yitian Lyu](https://www.linkedin.com/in/skylyuyitian/) · [Xinkai Sun](https://www.linkedin.com/in/xinkai-sun-34705826b/)
- [OpenCorporates search: plantcore](https://opencorporates.com/companies?q=plantcore) (no matching entity)
