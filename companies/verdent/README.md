# Verdent

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Verdent AI, Inc. builds **Verdent**, an agentic coding product sold as a desktop application, a VS Code extension, and a JetBrains plugin. The product runs multiple coding agents in parallel over a plan → code → verify loop, each in an isolated Git worktree. It launched on [2025-09-23](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code) as "Verdent" (IDE plugin) plus "Verdent Deck" (desktop), and was repositioned on [2026-04-20](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html) around a "Manager" that plans, dispatches workers, and queues finished work for review.

- Founded by Zhijie Chen (co-founder and CEO, former Head of Algorithms at ByteDance/TikTok) and Xiaochun Liu (former Head of Tech & Product at Baidu) ([2025-09-23 release](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)); [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) also lists Yuyu Zhang as a co-founder.
- Series A led by Tencent at "tens of millions of USD", with Sequoia China having led the prior round; reported valuation ~US$200M ([Sina, 2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml); [NetEase, 2025-11](https://www.163.com/dy/article/KFADJCN1055692AH.html)). Neither the company nor the investors have published a release confirming this.
- Headcount is reported as 20 as of [2026-05-31](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg), 11–50 on [LinkedIn](https://www.linkedin.com/company/verdent-ai) (Undated; accessed 2026-07-29), and "30–40 people" in a [November 2025 interview](https://www.163.com/dy/article/KFADJCN1055692AH.html).
- Verdent reported 76.1% pass@1 and 81.2% pass@3 on SWE-bench Verified with Claude Sonnet 4.5 ([technical report, 2025-11-01](https://www.verdent.ai/blog/swe-bench-verified-technical-report)). Its SEAlign paper received a Distinguished Paper Award at [ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent).
- The product is model-agnostic and routes to third-party frontier models; all infrastructure and data sit on AWS in the United States ([security page](https://www.verdent.ai/security); Undated; accessed 2026-07-29).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | Verdent | [site](https://www.verdent.ai/) |
| Legal name | Verdent AI, Inc. | [site footer](https://www.verdent.ai/); Undated; accessed 2026-07-29 |
| Founded | "Founded in 2025" per company boilerplate | [2025-09-23 release](https://www.financialcontent.com/article/bizwire-2025-9-23-verdent-ai-introduces-verdent-and-verdent-deck-new-ai-tools-that-let-human-developers-thrive-to-deliver-complex-enterprise-grade-code) |
| Governing law | California; disputes in California state or federal courts | [terms](https://www.verdent.ai/terms); Effective 2026-05-25 |
| HQ | Not published on the site. Press datelines: Singapore, then San Francisco | [2025-12-19](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/), [2026-04-20](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html), [2026-05-21](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical) |
| Registered location | Singapore | [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg); accessed 2026-07-29 |
| Founders | Zhijie Chen (co-founder, CEO), Xiaochun Liu (co-founder), Yuyu Zhang (co-founder) | [2025-09-23 release](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code), [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) |
| Headcount | 20 (as of 2026-05-31); 11–50 on LinkedIn | [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg), [LinkedIn](https://www.linkedin.com/company/verdent-ai) |
| Investors | Tencent, Sequoia China | [Sina, 2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) |
| Contact | hi@verdent.ai (general), support@verdent.ai (support) | [site](https://www.verdent.ai/), [regions page](https://www.verdent.ai/regions) |
| Infrastructure | AWS, all servers in the United States | [security page](https://www.verdent.ai/security); Undated; accessed 2026-07-29 |

The site footer, about page, security page, and LinkedIn profile are continuously updated pages without publication dates; all were accessed on 2026-07-29. The [about page](https://www.verdent.ai/about-us) states the company's purpose and tagline ("By developers, for developers") but names no founders, offices, or headcount.

### Identity and related names

- **Verdent Deck** — the original name of the desktop application, used in the [2025-09-23 launch](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code) and on [Product Hunt](https://www.producthunt.com/products/verdent-deck). Current site navigation calls the desktop app simply "Verdent".
- **codeck.ai** — a domain whose page reads that "something big is brewing at Verdent.ai" ([codeck.ai](http://www.codeck.ai/); Undated; accessed 2026-07-29). The media contact on the [2025-12-19 release](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/) was an `@codeck.ai` address. The relationship between the two domains is not stated publicly.

---

## Product

### Feature areas

Documented at [verdent.ai/docs](https://www.verdent.ai/docs/), which covers three surfaces: **Verdent Desktop**, **Verdent Cloud** (browser-based web app development), and **Verdent for VS Code**. A JetBrains plugin is listed on the [download page](https://www.verdent.ai/download).

- **Manager** — the orchestration layer. Per the [Manager docs](https://www.verdent.ai/docs/verdent-manager/core-features/manager), it "identifies the goal, defines the stages (e.g. setup → core logic → UI → validation), splits each stage into executable subtasks, and decides which can run in parallel", then "dispatches a dedicated worker per subtask and runs as many as possible at once". Finished work lands in a **To Review** queue with the files touched, a summary of decisions, and a link to the diffs.
- **Plan Mode** — converts a prompt into a structured plan before code is written; upgraded with requirement clarification and Mermaid diagrams ([changelog](https://www.verdent.ai/changelog), 2026-01-17 and 2025-12-31).
- **Workspaces** — isolated per-task environments, each with its own Git branch and change history ([blog, 2026-01-27](https://www.verdent.ai/blog/verdent-your-ai-native-partner)).
- **Memory** — the Manager retains "preferences — frameworks, naming, architecture decisions, ways of working" across tasks; daily automatic memory summarization was added in v2.6.3 ([changelog](https://www.verdent.ai/changelog), 2026-07-02).
- **Messaging channels** — tasks can be assigned from Slack, Telegram, Discord, and Feishu ([docs](https://www.verdent.ai/docs/)).
- **Tool integrations** — GitHub, Stripe, Supabase, Notion, Linear ([docs](https://www.verdent.ai/docs/)); MCP tool support in the VS Code extension ([Marketplace listing](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent)).
- **Automations** — recurring scheduled tasks configured without cron syntax ([docs](https://www.verdent.ai/docs/)).

### Commercialization

Paid subscription with a public [price list](https://www.verdent.ai/pricing) (accessed 2026-07-29). Individual tiers run Free (7-day trial), Lite, Starter, Pro, and Max, from $5 to $179 per month; Teams is per-seat with unified billing; Enterprise is custom-priced. Each paid tier grants a monthly credit allowance, currently including a "limited-time bonus" on top of the base allowance, and credits can be topped up at a rate the page describes as "no markup added".

Two cost-control options were added on [2026-04-02](https://www.verdent.ai/blog/introducing-eco-mode-byok-and-updated-pricing): **Eco Mode**, described in the changelog as zero-credit workflows, and **BYOK** for Anthropic, OpenAI, and OpenRouter keys. The free tier is a change from launch, when [Hacker News](https://news.ycombinator.com/item?id=45359339) commenters were told there was "no free tier" and plans started at $19/month.

### Release history

Selected entries from the [changelog](https://www.verdent.ai/changelog) (accessed 2026-07-29):

| Date | Version | Entry |
|---|---|---|
| 2025-09-23 | v1.0.0 | Parallel agents with task isolation, Plan First, DiffLens Insight |
| 2025-10-25 | v1.2.1 | Windows and Intel Mac support |
| 2025-12-03 | v1.5.0 | Isolated parallel workspaces |
| 2026-01-22 | v1.11.1 | Codebase indexing, Skills marketplace, Plan Rules |
| 2026-01-29 | v1.12.0 | Code Intelligence with LSP, Message Queue |
| 2026-03-05 | v1.16.0 | Verdent Team — centralized billing, seats, access management |
| 2026-04-02 | v1.19.2 | Eco Mode; BYOK for Anthropic, OpenAI, OpenRouter |
| 2026-05-14 | v2.2.1 | Workspace redesign with side-by-side Manager/Task panels, integrated browser |
| 2026-06-07 | v2.3.9 | Redesigned agent engine |
| 2026-07-10 | v2.7.0 | Multi-Manager configuration — separate managers with distinct skills and memories |
| 2026-07-28 | v2.8.0 | Collapsed activity feed; input box for designs, images, and automations |

Most other entries add support for a newly released third-party model.

### Reported traction over time

| Date | Reported figure | Source |
|---|---|---|
| 2025-10-01 | Verdent Deck: #3 Product of the Day, 301 upvotes | [Product Hunt](https://www.producthunt.com/products/verdent-deck) |
| 2025-11-01 | SWE-bench Verified 76.1% pass@1, 81.2% pass@3 (Claude Sonnet 4.5) | [technical report](https://www.verdent.ai/blog/swe-bench-verified-technical-report) |
| 2025-12-19 | "10x faster project cycles" claimed for parallel agent execution | [press release](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/) |
| 2026-01-26 | Verdent: #2 Product of the Day, 288 upvotes | [Product Hunt](https://www.producthunt.com/products/verdent-deck) |
| 2026-04-19 | Verdent 2.0: #3 Product of the Day, 256 upvotes | [Product Hunt](https://www.producthunt.com/products/verdent-deck) |
| 2026-05-21 | Verdent Manager reached #3 Product of the Day; "paid user growth accelerated" | [press release](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical) |
| Accessed 2026-07-29 | VS Code extension: 36,328 installs, 4.5/5 from 45 ratings, v1.6.13 (updated 2026-07-23) | [Marketplace](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent) |
| Accessed 2026-07-29 | LinkedIn 4,121 followers; Product Hunt 1.4K followers, 6 reviews at 5.0 | [LinkedIn](https://www.linkedin.com/company/verdent-ai), [Product Hunt](https://www.producthunt.com/products/verdent-deck) |

No user counts, revenue, or ARR figures have been published.

### Stated plans

From the [2026-04-20 release](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html): the platform is to operate "more like an AI engineering team", extending beyond code generation into planning, execution, validation, and delivery, built around chat-first collaboration, parallel work, and trusted review across desktop, VS Code, and JetBrains.

In the [DeepTech interview (2025-11-24)](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml), Chen said the company targets overseas markets on a SaaS subscription model aimed at professional engineers, planned a formal marketing push in December 2025, and named Cursor and Devin as startup competitors and GitHub Copilot and Google Antigravity as large-company products in the same space. He said the company intends to extend into code review, test verification, and SRE operations. Asked about the reported US$200M valuation, he described it as "only a fraction of comparable Silicon Valley startups".

---

## Founder

**Zhijie Chen (陈志杰)** — co-founder and CEO.

- Chief technical architect at Baidu; [The New Stack](https://thenewstack.io/tiktoks-ex-algorithm-chief-launches-verdent-ai-coding-tool/) gives the period as 2010–2019. Described as having over ten years of programming experience ([DeepTech, 2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)).
- Head of Algorithms at ByteDance/TikTok ([2025-09-23 release](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)); also described as head of ByteDance's data science organization ([Sina, 2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)). Chinese coverage states he led the build-out of large-scale recommendation systems and the foundational algorithm platform, managing hundreds of engineers and scientists ([Sohu, 2025-11](https://www.sohu.com/a/955425497_122074763)).
- Co-founded Verdent AI; titled "Founder and CEO" in the [2026-05-21 release](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical).
- Longer interviews: [DeepTech, 2025-11-24 (ZH)](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml), [Tech Talks Daily podcast (EN)](https://techtalksnetwork.com/podcast/tech-talks-daily/episode/3517-how-verdent-ai-is-building-the-next-generation-ai-coding-agents).

**Xiaochun Liu (刘晓春)** — co-founder.

- Head of Tech & Product at Baidu ([2025-09-23 release](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)), covering search, recommendation advertising, and e-commerce ([Sina, 2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)); reported to have managed a cross-functional team of 300+ ([Sohu, 2025-11](https://www.sohu.com/a/955425497_122074763)).

**Yuyu Zhang** — co-founder, listed by [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) and on [LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/) (accessed 2026-07-29).

- PhD at Georgia Institute of Technology, 2015–2021; earlier study at Wuhan University ([LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/)).
- AI researcher at ByteDance working on recommendation systems for TikTok and Douyin; led the Seed-Coder project ([LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/)). Seed-Coder is published as [arXiv:2506.03524](https://arxiv.org/abs/2506.03524), listed on Verdent's [research page](https://www.verdent.ai/research).
- Listed location: San Francisco Bay Area.

**Huangzhao Zhang** — quoted in the [2026-04-20 release](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html) and credited with the affiliation "Verdent AI" on the [SEAlign paper](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent) at ICSE 2026; the other authors are from Peking University and Wuhan University.

The company does not publish a team page. No titles beyond CEO are stated in the reviewed sources.

---

## Funding

| Date | Round | Amount | Investors | Source |
|---|---|---|---|---|
| Before 2025-11 | Prior round | Not disclosed | Sequoia China (lead) | [Sina](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) |
| Reported 2025-11-17 | Series A | "Tens of millions of USD" | Tencent (lead), existing investors including Sequoia China | [Sina](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml), [Sohu](https://www.sohu.com/a/955425497_122074763) |

All funding information comes from media reporting, not from a company or investor announcement. [Sina](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) reported that no new fund joined the Series A — existing investors increased their positions. Valuation was reported as "possibly exceeding US$200M" ([Sohu](https://www.sohu.com/a/955425497_122074763)) and as US$200M ([NetEase](https://www.163.com/dy/article/KFADJCN1055692AH.html)). [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) still recorded the company as unfunded when accessed on 2026-07-29.

No round has been announced on the company site, on Business Wire, or on PR Newswire, and neither Tencent nor Sequoia China (HongShan) has published an announcement found in the searches described in `Notes`.

---

## Engineering

### Technology stack and platforms

| Item | Detail | Evidence class |
|---|---|---|
| Cloud | AWS; "all of our infrastructure and your data are located exclusively within the United States" | Confirmed — [security page](https://www.verdent.ai/security) |
| Model providers | Azure AI Foundry, Google Cloud Vertex API, AWS Bedrock | Confirmed — [security page](https://www.verdent.ai/security) |
| Other subprocessors | Parallel.ai (web search), Jina (web content retrieval), Stripe (billing only) | Confirmed — [security page](https://www.verdent.ai/security) |
| Client platforms | macOS (Apple Silicon and Intel), Windows; VS Code and JetBrains extensions | Confirmed — [download page](https://www.verdent.ai/download), [changelog](https://www.verdent.ai/changelog) |
| Isolation primitive | Git worktrees / branch-per-agent codespaces | Confirmed — [changelog](https://www.verdent.ai/changelog) v1.1.0, [SiliconANGLE](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/) |
| Code intelligence | LSP-based; codebase indexing | Confirmed — [changelog](https://www.verdent.ai/changelog) v1.12.0, v1.11.1 |
| Remote execution | SSH remote server support | Confirmed — [changelog](https://www.verdent.ai/changelog) v1.18.2, [docs](https://www.verdent.ai/docs/) |
| Extensibility | MCP tools, subagents, configuration rules, Skills marketplace | Confirmed — [Marketplace listing](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent), [changelog](https://www.verdent.ai/changelog) |

The models offered are third-party: as listed on the [pricing page](https://www.verdent.ai/pricing) (accessed 2026-07-29), Claude Fable 5 / Opus 5 / Sonnet 5, GPT-5.6, Gemini 3.1 Pro, GLM-5.2, Kimi K3, MiniMax M3, and DeepSeek-V4-Pro. No source reviewed indicates that Verdent trains or serves its own production model.

In the [DeepTech interview (2025-11-24)](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml), Chen said the codebase had reached "300,000–400,000 lines".

A third-party hands-on published on [2025-11-23](https://zhuanlan.zhihu.com/p/1975338816031176069) recorded the model choices then offered — Claude Sonnet 4.5, Claude Haiku 4.5, GPT-5-Codex, GPT-5, Kimi-K2-Turbo — three VS Code model presets (Performance / Balance / Efficiency), custom subagents invoked with `@`, custom commands, MCP server configuration, and Git commit and rollback from inside the tool.

### Systems

| System | What it does | Source |
|---|---|---|
| Manager / worker orchestration | Decomposes a goal into stages and subtasks, dispatches one worker per subtask, runs them in parallel, and collects results into a review queue | [docs](https://www.verdent.ai/docs/verdent-manager/core-features/manager) |
| Plan → code → verify loop | Structured planning ahead of edits, a todo system with explicit checkpoints, automatic test loops, and a code-review subagent | [blog, 2026-04-01](https://www.verdent.ai/blog/why-strong-coding-models-fail-at-real-software-engineering-and-how-to-fix-it) |
| Workspace isolation | One Git-enabled codespace and virtual environment per agent, with commit, PR, and rollback | [SiliconANGLE, 2025-09-23](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/) |
| DiffLens | Change summaries and version difference reports surfaced for human review | [changelog](https://www.verdent.ai/changelog) v1.0.0, v1.7.2 |
| Multi-model review | Concurrent review and planning across several models, with edit-conflict detection | [changelog](https://www.verdent.ai/changelog) v1.13.0, v1.15.0 |
| Memory | Cross-task retention of preferences and conventions, with daily automatic summarization | [docs](https://www.verdent.ai/docs/verdent-manager/core-features/manager), [changelog](https://www.verdent.ai/changelog) v2.6.3 |

### Published research

The [research page](https://www.verdent.ai/research) lists papers associated with the team, including several published while the authors were at ByteDance: [Seed-Coder](https://arxiv.org/abs/2506.03524), [Seed1.5-Thinking](https://arxiv.org/abs/2504.13914), [FullStack Bench](https://arxiv.org/abs/2412.00535), and [Multi-SWE-bench](https://arxiv.org/abs/2504.02605).

**SEAlign** ([arXiv:2503.18455](https://arxiv.org/abs/2503.18455)) received a Distinguished Paper Award in the [ICSE 2026 Research Track](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent) (Rio de Janeiro, 2026-04-12 to 2026-04-18). It trains agents on collected trajectories, identifies critical decision points with Monte Carlo Tree Search, and aligns on them with DPO. The company's [2026-04-01 blog post](https://www.verdent.ai/blog/why-strong-coding-models-fail-at-real-software-engineering-and-how-to-fix-it) reports Qwen2.5-Coder-Instruct-14B moving from 3.7% to 17.7% on SWE-Bench-Lite and 2.8% to 21.8% on SWE-bench Verified after this training, and argues that agent failures come from behavioural misalignment rather than coding weakness.

The [SWE-bench Verified technical report (2025-11-01)](https://www.verdent.ai/blog/swe-bench-verified-technical-report) states 76.1% pass@1 and 81.2% pass@3 using Claude Sonnet 4.5, described as the production system "with no leaderboard tuning or test-time scaling", and compares against Claude Code on the same model and Codex on GPT-5. The comparison is Verdent's own; it has not been independently reproduced in any source reviewed here.

### Security posture

From the [security page](https://www.verdent.ai/security) (Undated; accessed 2026-07-29):

- "Actively pursuing SOC 2 and ISO/IEC 42001 certifications" — neither is stated as obtained.
- Zero data retention agreements with Google Cloud Vertex API and AWS Bedrock. Azure AI Foundry is listed as a subprocessor that sees code data, without a stated retention agreement.
- Account data is removed immediately on deletion; cloud backups may retain data until normal retention periods expire.
- Least-privilege infrastructure access; MFA required for AWS access; model blocklists respected.
- "Services currently do not offer indexing or analysis of your code repositories."

### Working conditions

No careers page exists in the site [sitemap](https://www.verdent.ai/sitemap.xml) (accessed 2026-07-29), and no job postings were found in the searches described in `Notes`. Nothing is published about working language, office policy, remote arrangements, visa sponsorship, salary, or benefits.

The one data point on team composition is Chen's statement that the team is "30–40 people" whose "past performance and backgrounds are excellent" ([DeepTech, 2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml); [NetEase reprint](https://www.163.com/dy/article/KFADJCN1055692AH.html)).

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): the verdent.ai sitemap and every non-`/docs`, non-`/blog`, non-`/guides` page it lists; the documentation site; the changelog, blog, research, pricing, security, terms, and about pages; Business Wire, PR Newswire, and Fortune/FinancialContent press-release mirrors; searches for "Verdent", "Verdent AI", "Verdent Deck", and "陈志杰 Verdent" in English and Chinese; domain-scoped searches of 36kr.com, tmtpost.com, huxiu.com, geekpark.net, pingwest.com, leiphone.com, and infoq.cn; GitHub user and organisation searches for `verdent`; a GitHub code search of the `ruanyf/weekly` 谁在招人 board; LinkedIn company and founder profiles; Tracxn, IT桔子, and Product Hunt.

- No careers page, no job postings, and no published salary bands were found.
- No public GitHub organisation was found. The GitHub accounts matching `verdent` are unrelated individual users.
- No open-source repositories, engineering blog beyond the marketing blog, or conference talks by the company were found. The research page links to academic papers, most of which predate the company.
- No office address, legal registration number, or incorporation jurisdiction is published. The terms name California law; Tracxn lists Singapore; press datelines have used both Singapore and San Francisco.
- No user count, revenue, or ARR figure has been published.
- No security certification has been obtained per the company's own [security page](https://www.verdent.ai/security).
- No company or investor announcement of any funding round was found; all funding facts here rest on Chinese media reporting from November 2025.
- No article about the company was found on 36氪, 钛媒体, 虎嗅, 极客公园, 品玩, 雷峰网, or InfoQ 中文站 in the domain-scoped searches above, and no IT桔子 company entry was found. Chinese coverage of the company is concentrated on 新浪 and its syndication network.

### Inconsistencies across sources

- **Founding date:** company boilerplate says "Founded in 2025" ([2025-09-23 release](https://www.financialcontent.com/article/bizwire-2025-9-23-verdent-ai-introduces-verdent-and-verdent-deck-new-ai-tools-that-let-human-developers-thrive-to-deliver-complex-enterprise-grade-code)); the DeepTech interview says the company was founded at the end of 2024 ([2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)).
- **Co-founder's name:** rendered 刘晓春 in [Sina](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) and [Sohu](https://www.sohu.com/a/955425497_122074763), and 刘小春 in the [AI 工具集 directory entry](https://ai-bot.cn/verdent-ai/). English releases use "Xiaochun Liu", which does not disambiguate.
- **Headcount:** 20 as of 2026-05-31 ([Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg)), 11–50 ([LinkedIn](https://www.linkedin.com/company/verdent-ai)), "30–40" as of November 2025 ([DeepTech](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)).
- **Funding status:** [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) records the company as having raised nothing; Chinese media report a Tencent-led Series A ([Sina](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)).
- **Founder count:** the launch release names two founders ([2025-09-23](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)); [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) and [LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/) list three.
- **Code repository indexing:** the [security page](https://www.verdent.ai/security) states the services "do not offer indexing or analysis of your code repositories", while the [changelog](https://www.verdent.ai/changelog) announced codebase indexing in v1.11.1 (2026-01-22) and the [launch release](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code) said the product "indexes codebases".
- **Credit allowances:** the [pricing page](https://www.verdent.ai/pricing) and the company's own [comparison guide](https://www.verdent.ai/guides/claude-code-vs-verdent) state different monthly credit figures for the same tiers and prices, both accessed 2026-07-29; a third figure appears in [September 2025 coverage](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/).
- **Product Hunt ranking:** the [2026-05-21 release](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical) attributes a #3 Product of the Day placement to "Verdent Manager"; the [Product Hunt page](https://www.producthunt.com/products/verdent-deck) records three launches, the most recent being "Verdent 2.0" at #3 on 2026-04-19.

### Other

- The product is a wrapper over third-party frontier models rather than a model provider: every model listed on the [pricing page](https://www.verdent.ai/pricing) is external, and the [security page](https://www.verdent.ai/security) routes inference through Azure AI Foundry, Google Vertex, and AWS Bedrock.
- Model availability is restricted by upstream provider geography; the [regions page](https://www.verdent.ai/regions) offers refunds within 24 hours to customers who lose access to a model for that reason.
- Positioning has moved twice in ten months: "agentic coding suite" at [launch (2025-09-23)](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code), "AI-native partner" in [January 2026](https://www.verdent.ai/blog/verdent-your-ai-native-partner), and "AI engineering team for builders" / "AI technical cofounder" from [April 2026](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html). The current [zh-CN homepage](https://www.verdent.ai/zh-CN) leads with non-developer use cases — a game built in 12 hours, a desktop companion app, a self-service analytics pipeline.
- Pricing, terms, security policy, documentation, and the full changelog are published openly without a login.
- The company publishes competitor comparison pages under [/guides](https://www.verdent.ai/guides), including [one against Claude Code](https://www.verdent.ai/guides/claude-code-vs-verdent) and an [AI coding tools comparison](https://www.verdent.ai/guides/ai-coding-tools-comparison-2026); figures on those pages are the company's own.
- All Chinese-language coverage found traces to two original pieces, both from November 2025: the funding scoop by 投资实习所 ([Sina, 2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)) and the founder interview by DeepTech 深科技 ([Sina, 2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)). The [Sohu](https://www.sohu.com/a/955425497_122074763), [NetEase](https://www.163.com/dy/article/KFADJCN1055692AH.html), and [Zhihu](https://zhuanlan.zhihu.com/p/1976372371272267577) versions are syndicated reprints of these two, not independent reporting.

---

## Resources

**Official**

- [Verdent — product site](https://www.verdent.ai/) · [简体中文](https://www.verdent.ai/zh-CN)
- [About us](https://www.verdent.ai/about-us)
- [Download](https://www.verdent.ai/download)
- [Pricing](https://www.verdent.ai/pricing)
- [Security](https://www.verdent.ai/security)
- [Terms of Use, effective 2026-05-25](https://www.verdent.ai/terms)
- [Regions and model availability](https://www.verdent.ai/regions)
- [Changelog](https://www.verdent.ai/changelog)
- [Sitemap](https://www.verdent.ai/sitemap.xml)
- [Documentation home](https://www.verdent.ai/docs/)
  - [Manager — core feature docs](https://www.verdent.ai/docs/verdent-manager/core-features/manager)
- [Research index](https://www.verdent.ai/research)
- [Guides index](https://www.verdent.ai/guides)
  - [Claude Code vs Verdent](https://www.verdent.ai/guides/claude-code-vs-verdent)
  - [AI coding tools comparison 2026](https://www.verdent.ai/guides/ai-coding-tools-comparison-2026)
- [Blog](https://www.verdent.ai/blog)
  - [SWE-bench Verified technical report — 2025-11-01](https://www.verdent.ai/blog/swe-bench-verified-technical-report)
  - [Verdent: Your AI-native Partner — 2026-01-27](https://www.verdent.ai/blog/verdent-your-ai-native-partner)
  - [Why strong coding models fail at real software engineering — 2026-04-01](https://www.verdent.ai/blog/why-strong-coding-models-fail-at-real-software-engineering-and-how-to-fix-it)
  - [Eco Mode, BYOK, and updated pricing — 2026-04-02](https://www.verdent.ai/blog/introducing-eco-mode-byok-and-updated-pricing)
- [codeck.ai](http://www.codeck.ai/)

**Press releases**

- [Verdent builds on early momentum — 2026-05-21](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical)
- [Verdent: the world's first AI engineering team for builders — 2026-04-20](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html)
- [Major updates to the standalone AI coding tool — 2025-12-19](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/)
- [Verdent AI introduces Verdent and Verdent Deck — 2025-09-23](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code) · [mirror with full text](https://www.financialcontent.com/article/bizwire-2025-9-23-verdent-ai-introduces-verdent-and-verdent-deck-new-ai-tools-that-let-human-developers-thrive-to-deliver-complex-enterprise-grade-code)

**Third-party coverage and profiles**

- [SiliconANGLE — launch coverage, 2025-09-23](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/)
- [The New Stack — interview with Zhijie Chen](https://thenewstack.io/tiktoks-ex-algorithm-chief-launches-verdent-ai-coding-tool/)
- [Tech Talks Daily — podcast episode on Verdent](https://techtalksnetwork.com/podcast/tech-talks-daily/episode/3517-how-verdent-ai-is-building-the-next-generation-ai-coding-agents)
- [Show HN discussion, 2025-09](https://news.ycombinator.com/item?id=45359339)
- [Visual Studio Marketplace listing](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent)
- [Product Hunt](https://www.producthunt.com/products/verdent-deck)
- [LinkedIn — company](https://www.linkedin.com/company/verdent-ai)
- [LinkedIn — Yuyu Zhang](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/)
- [Tracxn profile](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg)
- [ICSE 2026 — SEAlign paper record](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent) · [arXiv](https://arxiv.org/abs/2503.18455)
- Team papers on the research page: [Seed-Coder](https://arxiv.org/abs/2506.03524), [Seed1.5-Thinking](https://arxiv.org/abs/2504.13914), [FullStack Bench](https://arxiv.org/abs/2412.00535), [Multi-SWE-bench](https://arxiv.org/abs/2504.02605)

**Chinese-language coverage (ZH)**

Two original pieces, both November 2025, plus their reprints and third-party hands-ons:

- [Sina Finance — exclusive on the Tencent-led round, by 投资实习所, 2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) — the funding scoop
- [Sina Tech — founder interview, by DeepTech 深科技, 2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml) — the founder interview
- [Sohu (ZFinance) — reprint of the funding scoop, 2025-11-17](https://www.sohu.com/a/955425497_122074763)
- [NetEase — reprint of the interview, 2025-11](https://www.163.com/dy/article/KFADJCN1055692AH.html)
- [Zhihu — reprint of the interview](https://zhuanlan.zhihu.com/p/1976372371272267577)
- [Zhihu — 初识 Verdent AI, third-party hands-on, 2025-11-23](https://zhuanlan.zhihu.com/p/1975338816031176069) · [CSDN mirror](https://adg.csdn.net/695238375b9f5f31781b3548.html)
- [CSDN — 试用 Verdent 的一些感受, third-party hands-on](https://blog.csdn.net/weixin_38754564/article/details/152013640)
- [AI 工具集 — directory entry](https://ai-bot.cn/verdent-ai/)
