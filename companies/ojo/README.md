# OJO

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-08-26.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

OJO is an invite-only AI design product at `ojo.art` that generates product strategy, UI designs, landing pages and runnable interactive prototypes on a single canvas. Its Terms of Service name the operator as "Touchine AI (HK) Limited, a company incorporated in Hong Kong SAR" ([Terms of Service](https://ojo.art/terms); Updated and Effective Mar. 16, 2026).

- The product was publicly introduced on X on 2026-08-18: "Today, we're introducing OJO: The first Design Agent Team Workspace." ([@OJOaidesign, 2026-08-18](https://x.com/OJOaidesign/status/2089731834095489430)). The homepage still reads "OJO is in private beta. Join the waitlist and we will enable access for you as soon as we can." ([ojo.art](https://ojo.art/); accessed 2026-08-26).
- Four names appear across the company's own artifacts — **OJO** (brand), **Touchine** (legal entity and npm scope), **iRise** (static-asset path and GitHub org), and **Nexight** (VS Code Marketplace publisher) — see `Identity and names`.
- Prices are published and live: Free ($0), Plus ($27/month or $300/year), Pro ($62/month or $684/year), plus four credit packs, charged through Stripe and Antom ([/api/commerce/v1/billing/plans](https://ojo.art/subscribe); read 2026-08-26) — see `Commercialization`.
- The founder is **Kiki ZHANG** (X `@kiki_ZHANG_OJO`, bio "ex Bytedancer, now Founder of @ojoaidesign"), whom OJO's own GitHub organization names as the company's X account. Chinese outlet 硅星人Pro reported on 2026-08-12 that this is **张琪智 (KiKi)**, the former product lead of ByteDance's 剪映 — see `Team`.
- No funding round, headcount or user total is published anywhere the search below reached — see `Notes`.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | OJO (page title "OJO \| AI Design Agent for UI, Landing Pages, and Product Prototypes") | [ojo.art](https://ojo.art/); accessed 2026-08-26 |
| Self-description | "OJO is an AI Design Agent Team Workspace that turns ideas into research-backed UI designs, landing pages, and product prototypes. Join the private beta." | `og:description` meta tag, [ojo.art](https://ojo.art/); accessed 2026-08-26 |
| Operating entity | "Touchine AI (HK) Limited, a company incorporated in Hong Kong SAR ('Touchine,' 'we,' 'us,' or 'our')" | [Terms of Service](https://ojo.art/terms) §preamble; Updated/Effective Mar. 16, 2026 |
| Company registration | BR number "80290592"; incorporated "2026年04月28日" (2026-04-28); type "私人股份有限公司" (private company limited by shares); status "仍註冊" (still registered) | [tempb.com company directory](https://www.tempb.com/companies/touchine-ai-hk-limited/), a third-party aggregator; page dated 2026-07-18 |
| Registered address | "Suite 6503, 65/F, Central Plaza, 18 Harbour Road, Wan Chai, Hong Kong" | [Terms of Service](https://ojo.art/terms) §14.4, [Privacy Policy](https://ojo.art/privacy-policy) §10 |
| Governing law | "the laws of the Hong Kong Special Administrative Region"; "exclusive jurisdiction of the courts of Hong Kong" | [Terms of Service](https://ojo.art/terms) §13 |
| Document dates | Terms of Service and Privacy Policy both "Updated: Mar. 16, 2026 / Effective: Mar. 16, 2026"; Help Center "Last updated: Mar 28, 2026" | [Terms](https://ojo.art/terms), [Privacy Policy](https://ojo.art/privacy-policy), [Help Center](https://ojo.art/help-center) |
| Age policy | "Confirm you are at least 18 years of age"; "The Services are not intended for individuals under 18 years of age" | [Terms](https://ojo.art/terms) §1, [Privacy Policy](https://ojo.art/privacy-policy) §8 |
| Public contacts | `official@ojo.art` (legal, privacy rights, DPO, training opt-out); `support@ojo.art` (support, DMCA agent) | [Terms](https://ojo.art/terms) §14.4, [Privacy Policy](https://ojo.art/privacy-policy) §10 |
| Access model | Invite-only: "OJO is currently in an invite-only beta phase. Please visit ojo.art to submit an invitation code and request access." | [Help Center](https://ojo.art/help-center) §2.1; accessed 2026-08-26 |
| Domains | `ojo.art` created 2026-03-03 (registrar Spaceship, Inc.; registrant shielded by "Privacy service provided by WITHHELD FOR PRIVACY LLC", state Delaware, US). `touchine.ai` created 2026-04-13 (Cloudflare registrar, registrant country CN) and redirects to `ojo.art`. `touchine.com` created 2026-03-25 (Alibaba Cloud/HiChina, registrant state "bei jing", CN). `ws.ojo.dev` resolves via CNAME to an AWS `us-east-1` load balancer. | WHOIS and DNS read 2026-08-26 |
| Site locales | Six: `en`, `zh-CN`, `zh-HK`, `ja`, `es`, `ko`, declared as `hreflang` alternates | [ojo.art](https://ojo.art/) page head; accessed 2026-08-26 |
| Public routes | `/`, five locale roots, `/help-center`, `/terms`, `/privacy-policy`, plus per-locale blog sitemaps; `/subscribe` and `/dashboard` are app routes not listed in the sitemap | [sitemap.xml](https://ojo.art/sitemap.xml), [pages-sitemap.xml](https://ojo.art/pages-sitemap.xml); read 2026-08-26 |
| Social and community | X `@OJOaidesign` — "Joined June 2026", 2,076 followers, 171 following. Discord server "OJO" — 303 members, 37 online. The invite on the website (`Fw55pk7z3N`) and the one in the X bio (`GDtZg4Fs27`) resolve to the same guild id `1503702135249047562`. | [X profile](https://x.com/OJOaidesign), [Discord invite API](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true); observed 2026-08-26 |
| Mobile apps | None found in the US App Store under the brand name | [iTunes search API](https://itunes.apple.com/search?term=ojo%20design%20agent&entity=software&country=us&limit=5); checked 2026-08-26 |
| Internet Archive | No captures of `ojo.art` are indexed | [Wayback availability API](http://archive.org/wayback/available?url=ojo.art) and CDX index; checked 2026-08-26 |
| Founder | "Kiki ZHANG" (X `@kiki_ZHANG_OJO`), self-described "ex Bytedancer, now Founder of @ojoaidesign"; reported by 硅星人Pro as 张琪智 (KiKi), former product lead of ByteDance's 剪映 | [GitHub org `touchine-ojo`](https://github.com/touchine-ojo), [@kiki_ZHANG_OJO](https://x.com/kiki_ZHANG_OJO), [硅星人Pro via 虎嗅, 2026-08-12](https://www.huxiu.com/article/4882486.html) |
| Headcount, funding | Not published on the site, in the legal documents, or in any source the search below reached | see `Notes` |

### Identity and names

| Name | Where it appears | Detail | Source |
|---|---|---|---|
| OJO | Public brand, domain, product | `ojo.art`; also the CLI binary name `ojo` | [ojo.art](https://ojo.art/) |
| Touchine AI (HK) Limited | Legal entity in Terms and Privacy Policy | Hong Kong SAR company; BR 80290592 | [Terms](https://ojo.art/terms), [tempb.com](https://www.tempb.com/companies/touchine-ai-hk-limited/) |
| OJO ART LIMITED | Terms of Service §11 only | The limitation-of-liability clause reads "OJO ART LIMITED AND ITS DIRECTORS, EMPLOYEES, AND AGENTS SHALL NOT BE LIABLE…", a different name from the entity defined in the preamble | [Terms](https://ojo.art/terms) §11 |
| Touchine (npm scope) | Package registry | `@touchine/ojo` — "OJO CLI — login, project management, AI chat, run status queries, workspace sync, and session history"; scope also holds `@touchine/contract-design-project` (published 2026-04-21) | [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |
| touchine.ai | Domain | Redirects to `ojo.art` | observed 2026-08-26 |
| touchine.com | Domain | Serves an unrelated-looking page titled "Touchine Project Engineering - Boson Core", filed in China under "京ICP备2026017083号-1" and "京公网安备11010502060187号". No source connects this ICP filing to Touchine AI (HK) Limited — see `Notes`. | [touchine.com](https://touchine.com/); read 2026-08-26 |
| iRise / irise-studio | Static assets and code hosting | The marketing site is served from `/_static/irise-official/`; the npm package's `repository` field points to `git+https://github.com/irise-studio/irise-extension.git`, directory `apps/cli` | [ojo.art](https://ojo.art/) asset paths, [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |
| touchine-ojo | GitHub organization | Display name "OJO TEAM", location "Hong Kong", blog `https://ojo.art`, email `support@touchine.ai`, X account `kiki_ZHANG_OJO`; created 2026-07-07; one public repository | [GitHub API](https://api.github.com/orgs/touchine-ojo); read 2026-08-26 |
| Nexight | VS Code Marketplace publisher | Publisher `nexight` (display name "Nexight"), publisher domain `https://ojo.art` (not domain-verified), publishing the extension `ojo` | [VS Code Marketplace API](https://marketplace.visualstudio.com/items?itemName=nexight.ojo); read 2026-08-26 |
| `zk` | Front-end storage keys | Browser storage uses a `zk`/`ZK` prefix (`zk-web-subscribe-billing-plans-cache-v1`, `__ZK_AUTH_STATE_SYNC__`, `zk_mixpanel_analytics_consent_v1`) and app i18n keys are namespaced `canvas.components.*` | localStorage read on `ojo.art` 2026-08-26 |

The GitHub organization `irise-studio` exists, was created 2026-04-08, has 6 followers, 0 public repositories and no public members; `irise-studio/irise-extension` returns "Not Found" to unauthenticated requests ([GitHub API](https://api.github.com/orgs/irise-studio); read 2026-08-26).

---

## Product

The Help Center describes the product as "an AI-powered design and development platform for the next generation of product creators", where users "describe what you want, and AI will build it for you immediately", producing "real, runnable product prototypes that can be previewed and interacted with directly in the browser, with one-click sync to a fully developable code project" ([Help Center](https://ojo.art/help-center); Last updated Mar 28, 2026).

The Terms of Service describe it differently: "ojo.art is an AI-powered visual design platform utilizing advanced models including but not limited to Google Gemini and Anthropic Claude to transform user prompts and inputs into professional design assets", listing "Text-to-image and image-to-image generation; Design editing, iteration, and composition tools; Brand kit generation and asset management; Collaboration workspaces and template libraries" ([Terms](https://ojo.art/terms) §3).

### Surfaces and feature areas

| Surface | What it is | Source |
|---|---|---|
| Web canvas | The main product. Each generated prototype is saved as a project with a unique link at `https://ojo.art/p/<projectId>`, with a web editor for "real-time preview, fine-tuning, and continued modification with AI assistance" | [Help Center](https://ojo.art/help-center) §3.2–3.3 |
| Agent teams and Skills | The homepage instructs users to "先组建你的 Agent 团队和 Skills，再让它们为你设计" (first assemble your Agent team and Skills, then let them design for you) and advertises "自由添加 200 多种不同类型的 Skills" (freely add 200+ different types of Skills) | [ojo.art/zh-CN](https://ojo.art/zh-CN/); accessed 2026-08-26 |
| Named Skills shown on the site | 产品页面架构 (page architecture), 设计优化专家 (design optimization expert), 产品需求分析 (requirement analysis), 线框稿生成 (wireframe generation), 站点结构分析 (site structure analysis), UI/UX 最佳实践, 视觉基因生成 (visual DNA generation), 图片搜索 (image search) | [ojo.art/zh-CN](https://ojo.art/zh-CN/); accessed 2026-08-26 |
| Agent team presets | The landing-page markup carries four team cards: "Requirements Team", "Redesign Team", "Prototype Design Team", "Game Workshop" | `AgentTeamBridgeSection` bundle on [ojo.art](https://ojo.art/); read 2026-08-26 |
| CLI | `npm install -g @touchine/ojo`. Commands: `ojo auth login` (modes `web`, `device`, `pat`), `ojo project list`, `ojo project open`, `ojo chat --message`, `ojo query --project-id`, `ojo workspace sync <id> [--path]`. Synced code lands in `<project-name>/ojo-prototype` with dependencies installed and the dev server started automatically. | [ojo.art](https://ojo.art/), [Help Center](https://ojo.art/help-center) §3.4–3.5 |
| Editor extension | "Ojo platform integration for VS Code and Cursor: sign in, open projects, chat with sessions, sync local workspaces, and (in Cursor) register a session-scoped Ojo MCP server for agent tools." | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=nexight.ojo) |
| Export | The homepage states "支持CLI、插件嵌入AI开发流，资产互通 / 设计即交付" (CLI and plugins embed into AI development flows; assets interoperate; design is delivery). Plan features distinguish "仅支持代码导出" (code export only) from "全格式导出" (all-format export). | [ojo.art/zh-CN](https://ojo.art/zh-CN/), [billing plans API](https://ojo.art/subscribe) |
| Open-source skills | `touchine-ojo/OJO-Design-Skills` (MIT) — "Reusable UI/UX design skills for AI coding agents — Codex, Claude Code, ZCode, and more", installed by one script targeting Codex, Claude Code, ZCode, DeepCode, WorkBuddy, OpenCode or a generic agent directory | [GitHub](https://github.com/touchine-ojo/OJO-Design-Skills); read 2026-08-26 |
| Blog | 16 posts in three series — "OJO PlayBook", "OJO Field Notes", "OJO Best Practices" — published across all six locales | [blog index](https://ojo.art/blog/posts/); read 2026-08-26 |

### Commercialization

Read from `GET /api/commerce/v1/billing/plans` as rendered on [ojo.art/subscribe](https://ojo.art/subscribe) on 2026-08-26. The payload reports `commercializationMode: "live"`; plan records carry `updatedAt` values of 2026-06-17 (Free) and 2026-07-13 (all paid plans).

| Plan | Monthly | Annual | Credits | Selected features as listed |
|---|---|---|---|---|
| Free | $0 | $0 | 200 credits, claimable on daily login, reset at 00:00 UTC | Basic models; view-only share links; export not supported; 256K context window |
| Plus | $27/month (2,200 credits) | $300/year, stated as "$25/month" (26,400 credits/year) | as shown | "Flash + limited advanced models"; code export only; 30-day per-project retention; 256K context window; credit packs purchasable |
| Pro | $62/month (5,000 credits) | $684/year, stated as "$57/month" (60,000 credits/year) | as shown | "SOTA / Master / image-generation models"; all-format export; long-term history; voice; share-and-co-edit; dedicated support; 1M context window; CLI |
| Ultra | "即将开放" (coming soon) | — | "更高积分额度即将公布" (higher allowance to be announced) | Team member and permission management; higher concurrency; shared workspaces; enterprise support |

Credit packs: 500 for $8, 1,000 for $15, 3,000 for $40, 8,000 for $99. All paid items list `paymentMethods: ["card","alipay"]` and `checkoutProviders: ["stripe","antom"]` (billing plans API; read 2026-08-26). The Terms add that free promotional credits expire "within 30 days", subscription credits roll over "up to a maximum of one (1) month … or twelve (12) months for annual plans", paid credits are "valid for 12 months", and "All purchases are final" ([Terms](https://ojo.art/terms) §5).

### Reported scale

No user, subscriber, revenue or generation total is published. The public signals available on 2026-08-26:

| Signal | Value | Source |
|---|---|---|
| X followers | 2,076 (171 following); account "Joined June 2026" | [@OJOaidesign](https://x.com/OJOaidesign) |
| Launch post engagement | 533,000 views, 235 replies, 114 reposts, 823 likes | [@OJOaidesign, 2026-08-18](https://x.com/OJOaidesign/status/2089731834095489430) |
| Discord | 303 members, 37 online; guild id `1503702135249047562`, which by Discord snowflake arithmetic corresponds to 2026-05-12 | [Discord invite API](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true) |
| VS Code extension | version 0.0.1, published 2026-03-20; 17 installs, 222 downloads | [VS Code Marketplace API](https://marketplace.visualstudio.com/items?itemName=nexight.ojo) |
| npm CLI | 5 versions (1.0.4–1.0.8); first published 2026-05-18, latest 1.0.8 on 2026-08-06 | [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |
| Founder's X account | `@kiki_ZHANG_OJO`, 221 followers, 172 following; "Joined June 2026" | [@kiki_ZHANG_OJO](https://x.com/kiki_ZHANG_OJO) |
| Open-source repo | `OJO-Design-Skills`: 8 stars, 0 forks, 5 commits; first commit 2026-07-25, last push 2026-07-29 | [GitHub API](https://api.github.com/repos/touchine-ojo/OJO-Design-Skills) |

### Content rules as published

Users may not generate content that violates "laws or regulations of Hong Kong, your jurisdiction, or international law", infringes IP, "Constitutes non-consensual intimate imagery, deepfakes for deceptive purposes, or harmful misinformation", "Promotes hate speech, violence, discrimination, or illegal activities", "Exploits or harms minors", or overloads infrastructure through botting or reverse engineering ([Terms](https://ojo.art/terms) §7).

Ownership of AI Output transfers to the user "Upon generation and full payment of applicable Credits", but users may not "Use AI Output to train, develop, or improve competing AI models or services" or "Resell raw AI Output as stock imagery, design templates, or NFT collections without substantial transformative modification" ([Terms](https://ojo.art/terms) §6).

---

## Team

Nobody is named on `ojo.art` itself, in the Terms, Privacy Policy or Help Center. The founder is identified through the company's GitHub organization and X.

| Fact | Detail | Source |
|---|---|---|
| Founder, as stated by the company | The GitHub organization `touchine-ojo`, display name "OJO TEAM", blog `https://ojo.art`, email `support@touchine.ai`, lists `kiki_ZHANG_OJO` as its X account | [GitHub API](https://api.github.com/orgs/touchine-ojo); read 2026-08-26 |
| Founder, as stated by the person | X `@kiki_ZHANG_OJO`, display name "Kiki ZHANG", bio "ex Bytedancer, now Founder of @ojoaidesign", "Joined June 2026" | [@kiki_ZHANG_OJO](https://x.com/kiki_ZHANG_OJO); read 2026-08-26 |
| Founder's launch post | "OJO is officially here.❤️ After leaving ByteDance and starting OJO, I kept asking myself: When AI makes building easier for everyone, what still makes a product worth shipping? My answer: taste." | [@kiki_ZHANG_OJO, 2026-08-19](https://x.com/kiki_ZHANG_OJO/status/2089746515246133495) |
| Press identification | "4月，剪映产品负责人张琪智离职，开始AI Design方向创业。她的新产品OJO定位为设计场景里的Agent团队工作台，目前已经开始内测。" ("In April, 剪映 product lead 张琪智 left and started a venture in AI Design. Her new product OJO is positioned as an Agent team workspace for design scenarios and has entered closed beta.") The article's appendix lists "OJO（ojo.art）". | [硅星人Pro via 虎嗅, 2026-08-12](https://www.huxiu.com/article/4882486.html) |
| Reported English name | Headline: "字节跳动剪映产品负责人张琪智（KiKi）离职创业，4月中旬已在深圳成立新公司" | [鲁中晨报 via 网易, 2026-05-13](https://www.163.com/dy/article/KSRD3PT40530JPVV.html) |
| Repository code owners | `.github/CODEOWNERS` on `OJO-Design-Skills` reads `* @rogerhorsley @kikizhang0710-png`; the GitHub account `kikizhang0710-png` was created 2026-03-27 | [CODEOWNERS](https://github.com/touchine-ojo/OJO-Design-Skills/blob/main/.github/CODEOWNERS), [GitHub API](https://api.github.com/users/kikizhang0710-png); read 2026-08-26 |
| Other identifiers in company artifacts | npm maintainer `rogerhorsley` (`rogerhorsleymorris@gmail.com`) on `@touchine/ojo` and `@touchine/contract-design-project`, whose commits are authored as "Sisma"; Discord invite creator `waterplants888` / "Waterplants". Neither is presented anywhere as a company role. | [npm registry](https://registry.npmjs.org/@touchine%2Fojo), [commit list](https://api.github.com/repos/touchine-ojo/OJO-Design-Skills/commits), [Discord invite API](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true) |

**Career as reported for 张琪智** (Chinese press, May 2026, not confirmed by the company): born 1994; undergraduate at 西南大学新闻传媒学院, master's at 香港中文大学; joined 郭列's 脸萌 as a product manager after graduating in 2015; moved to ByteDance when it acquired 脸萌 for $300M in March 2018; appeared as 剪映工具产品负责人 at the December 2022 剪映创作大会; promoted to 剪映产品负责人 at the end of 2024; stepped down as manager, director and legal representative of 脸萌技术（深圳）有限公司 on 2026-03-26 and registered 深圳想象着陆科技有限公司 on 2026-04-17 as sole shareholder and legal representative, with RMB 1,000,000 registered capital ([澎湃新闻](https://m.thepaper.cn/newsDetail_forward_33177991), [每日经济新闻, 2026-05-13](https://www.nbd.com.cn/articles/2026-05-13/4391026.html), [DoNews](https://www.donews.com/news/detail/4/6547954.html)).

No company-controlled source names 张琪智, connects OJO to 深圳想象着陆科技有限公司, or names any employee other than the founder.

---

## Funding

No funding round, investor, valuation or amount is announced by the company or reported by any source the search reached. The 硅星人Pro survey of 剪映 alumni startups that identifies OJO gives funding figures for several other companies in the same piece but none for OJO ([硅星人Pro via 虎嗅, 2026-08-12](https://www.huxiu.com/article/4882486.html)). The reported Shenzhen company registered by 张琪智, 深圳想象着陆科技有限公司, is described as wholly owned by that person with RMB 1,000,000 registered capital, which is a registration figure and not an investment ([每日经济新闻, 2026-05-13](https://www.nbd.com.cn/articles/2026-05-13/4391026.html)).

No Crunchbase, PitchBook or Tracxn profile for Touchine AI (HK) Limited or for OJO at `ojo.art` was found; searches for "OJO" plus funding terms return results for **OJO Labs**, an unrelated Austin, Texas real-estate company that raised a $45M Series C in 2019 ([PR Newswire, 2019](https://www.prnewswire.com/news-releases/ojo-labs-raises-45-million-in-series-c-funding-to-accelerate-product-development-and-fuel-expansion-300814706.html)) — see `Notes`.

---

## Engineering

### Technology stack and platforms

| Layer | What is observable | Source |
|---|---|---|
| Marketing site | React with React Router-style entry points (`entry.client`, `root`), built with Rolldown (`rolldown-runtime` chunk), served from `/_static/irise-official/`; Tailwind-style utility classes | [ojo.art](https://ojo.art/) bundles; read 2026-08-26 |
| Product app | A separate webpack build served from `/_static/canvas/`, with i18n keys namespaced `canvas.*` | network requests on [ojo.art/subscribe](https://ojo.art/subscribe); read 2026-08-26 |
| Build-time runtime config | `{"apiPrefix":"/api","authRedirectOrigin":"https://ojo.art","firebaseAuthOrigin":"https://ojo-art-platform.firebaseapp.com","officialHomeOrigin":"https://ojo.art","websocketEndpoint":"wss://ws.ojo.dev/ws","officialHomePath":"/"}` | app bundle `main.*.js` on `ojo.art`; read 2026-08-26 |
| Auth | Firebase Auth (project `ojo-art-platform`), with "Continue with Google", "Continue with GitHub" and an email sign-in link (`emailForSignIn`) plus a six-digit verification code flow | app bundle and `official-copy` bundle on [ojo.art](https://ojo.art/); read 2026-08-26 |
| Payments | Stripe and Antom; card and Alipay | [billing plans API](https://ojo.art/subscribe); [Terms](https://ojo.art/terms) §5.5 names Stripe |
| Analytics | Mixpanel, gated behind a stored consent flag (`zk_mixpanel_analytics_consent_v1`); Cloudflare RUM (`/cdn-cgi/rum`) | localStorage and network requests on `ojo.art`; read 2026-08-26 |
| Edge / CDN | Cloudflare (`server: cloudflare`, `cf-ray` headers) | response headers; read 2026-08-26 |
| CLI | Node package with `bin: {"ojo": "dist/index.js"}`; dependencies include `ink` and `react` (terminal UI), `commander`, `inquirer`, `axios`, `zod`, `ora`, `chalk`, `open`, `cli-table3`, `terminal-link`, `semver`, `sql.js` (local SQLite) | [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |

### Systems

- **API surface observed from the browser:** `POST /api/account/api/user/v1/user_info`, `GET /api/commerce/v1/billing/plans`, `GET /client-context?device_timezone=…&browser_language=…&app_locale=…` (network requests on `ojo.art`; read 2026-08-26). The doubled `/api/account/api/` path suggests a gateway prefixing per-service routes.
- **Realtime:** a WebSocket endpoint at `wss://ws.ojo.dev/ws`, whose DNS resolves through a CNAME to `…us-east-1.elb.amazonaws.com` (build config and `dig`; read 2026-08-26).
- **Bring-your-own-model:** the app bundle validates a provider allow-list of `openai`, `openai-compatible`, `anthropic`, `gemini`, `deepseek`, `moonshot`, `kimi-global`, `kimi-code-plan`, `minimax`, `minimax-global`, `bailian-us`, `openrouter`, exposed in the UI as "自定义模型 API 配置" (custom model API configuration), listed as a limited-time feature on Plus and open on Pro (app bundle and [billing plans API](https://ojo.art/subscribe); read 2026-08-26).
- **Crawler policy:** `robots.txt` is Cloudflare-managed and sets `Content-Signal: search=yes,ai-train=no,use=reference`, with `Disallow: /` for Amazonbot, Applebot-Extended, Bytespider, CCBot, ClaudeBot, CloudflareBrowserRenderingCrawler, Google-Extended, GPTBot and meta-externalagent ([robots.txt](https://ojo.art/robots.txt); read 2026-08-26). Requests without a browser user agent receive HTTP 403.

### Data handling as documented

- **Data regions.** "China Mainland Users: Personal data is processed and stored on servers located within the People's Republic of China, operated by qualified local service providers; International Users (US, EU, others): Data is stored in AWS US East jurisdictions" ([Privacy Policy](https://ojo.art/privacy-policy) §3.1). The policy states compliance with the Hong Kong PDPO, GDPR, CCPA and China's PIPL (§preamble).
- **Training on user content.** "We may use Inputs and AI Output to train, develop, and improve our models and the Services. Personal identifiers are removed or anonymized before use in training datasets", with an opt-out via "Account Settings > Privacy" or email ([Terms](https://ojo.art/terms) §8, [Privacy Policy](https://ojo.art/privacy-policy) §4).
- **Third-party processing.** "Your Inputs are processed by third-party AI providers (Google, Anthropic)"; the Privacy Policy adds "No third-party AI provider uses your data to train their general models (prohibited by our contracts with Google and Anthropic)" ([Terms](https://ojo.art/terms) §8.3, [Privacy Policy](https://ojo.art/privacy-policy) §4.1).
- **Retention.** Content deletion "within 30 days", backups up to 90 days, deleted-account data "permanently deleted within 90 days", financial records "Retained for 7 years per Hong Kong tax law" ([Terms](https://ojo.art/terms) §9.1, [Privacy Policy](https://ojo.art/privacy-policy) §6.1).
- **Stated security measures.** "TLS 1.3 encryption for data in transit; AES-256 encryption for data at rest; Access controls and audit logging; Regular security assessments" ([Privacy Policy](https://ojo.art/privacy-policy) §6.2).
- **Cookies.** "We use essential cookies for authentication and service operation. We do not currently use tracking cookies for advertising purposes (No Google Analytics, No Facebook Pixel)" ([Privacy Policy](https://ojo.art/privacy-policy) §7).

### Audience the company says it targets

The waitlist questionnaire asks applicants to pick use cases from "Product prototyping", "UI design and developer handoff", "Design variants and exploration", "Personal projects and portfolio"; roles from "Product designer", "Frontend developer", "Product manager", "Solo developer", "Founder", "Student"; and team size from "Solo", "2–5", "6–20", "20+". The contact step offers a set of social platforms that includes a WeChat official account option ([ojo.art](https://ojo.art/) `official-copy` bundle; read 2026-08-26).

### Technical background sought, working conditions

No job posting, careers page or hiring statement was found. `/careers`, `/jobs` and `/about` return HTTP 404 on `ojo.art` (checked 2026-08-26). Job listings that appear in searches for "OJO" — for example a "Senior Product Designer, Agent Team" role on Built In Austin — belong to OJO Labs, the unrelated Austin real-estate company.

### Industry domain

AI design and prototyping tools for product teams: turning natural-language briefs into UI, landing pages and runnable prototypes, with export into code and design tools.

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-08-26): `ojo.art` homepage and all six locale roots, `/terms`, `/privacy-policy`, `/help-center`, `/subscribe`, `/blog/posts/` and `/blog/zh-cn/posts/`, `robots.txt`, `sitemap.xml` and `pages-sitemap.xml`; probes of `/about`, `/careers`, `/pricing`, `/privacy`, `/legal/*`, `/docs`, `/login`, `/app`, `/changelog`, `/refund-policy`, `/workspace`, `/canvas`, `/explore`, `/invite`, `/waitlist`; the page's network requests, JavaScript bundles, build-time runtime config and browser storage; the billing plans API; WHOIS and DNS for `ojo.art`, `touchine.ai`, `touchine.com`, `ojo.dev` and `irise.art`; the Internet Archive CDX and availability APIs; the npm registry for the `@touchine` scope; the GitHub API for `irise-studio`; the VS Code Marketplace API; the Discord invite API; the X accounts `@OJOaidesign` and `@kiki_ZHANG_OJO` and their launch threads; the US App Store; the tempb.com Hong Kong company directory; and English and Chinese searches on OJO, ojo.art, Touchine, Touchine AI (HK) Limited, iRise Studio, Nexight, the ICP filing number, 张琪智 and 深圳想象着陆科技有限公司.

- **Any employee other than the founder, and any executive team.** No company-controlled source names a second person in a role.
- **A first-party statement of the founder's legal name or prior title.** The X bio says only "ex Bytedancer"; the identification as 张琪智, former 剪映 product lead, comes from Chinese press, not from the company.
- **Headcount, office location and where the team actually works.** The Hong Kong address is a suite in Central Plaza given as a legal contact address; no other location is stated. Chinese-language filenames in the site's image assets (`花`, `前景`, `人`, `代码`, `元素`, `背景`, `海报`, `荧幕`, `人物`, `墨水`, `素材`) and the CN registrant countries on `touchine.ai` and `touchine.com` are the only location-adjacent signals found.
- **Any funding round, investor or valuation.**
- **Hong Kong registry particulars.** Directors, shareholders and the registered address on file were not retrieved; the incorporation date and BR number above come from a third-party aggregator, not from the Companies Registry itself, whose search is access-gated.
- **Any user, subscriber, revenue, project or generation total.**
- **Which models sit behind the tiers.** Plans reference "基础模型" (basic), "Flash + 有限高级模型" (Flash + limited advanced) and "SOTA / Master / 生图模型" (SOTA / Master / image-generation) without naming a single model or version. The Terms name Google Gemini and Anthropic Claude "including but not limited to".
- **What credits cost per operation.** Only totals per plan are published; no per-generation credit price is listed.
- **The relationship between OJO's disclosed operator and the founder's reported Chinese company.** Press reports 深圳想象着陆科技有限公司 (Shenzhen, registered 2026-04-17); the product's Terms name Touchine AI (HK) Limited (Hong Kong, reported incorporation 2026-04-28); `touchine.com` carries a Beijing ICP filing. No source connects the three.
- **The relationship between Touchine AI (HK) Limited and the Beijing entity behind `touchine.com`.** The ICP filing "京ICP备2026017083号-1" was not resolved to a registrant name; MIIT lookup services were unreachable from this environment.
- **Who "Nexight" is.** The VS Code publisher claims `https://ojo.art` as its domain but the domain is not verified by the Marketplace, and the name appears in no other company source.
- **The GitHub repository.** `irise-studio/irise-extension`, referenced by the published npm package, is private.
- **A LinkedIn company page, Product Hunt launch, or press coverage from an established outlet.** None found; the only third-party write-up located is [aiposthub.com](https://www.aiposthub.com/ojo-ai-design-agent-team-workspace/) (2026-08-19), an aggregator.
- **Any Internet Archive history for `ojo.art`,** which limits what can be checked about earlier positioning.
- **Sources that could not be read on 2026-08-26:** `ojo.art/dashboard` and the product itself (invite-gated), `github.com/irise-studio/irise-extension` (private), the Hong Kong Companies Registry (access-gated), and `ojo.art` via plain HTTP clients without a browser user agent (HTTP 403).

### Inconsistencies across sources

- **The Terms name two different companies.** The preamble binds the user to "Touchine AI (HK) Limited", while the limitation-of-liability clause caps the liability of "OJO ART LIMITED" ([Terms](https://ojo.art/terms) §preamble, §11). No entity by the second name is identified anywhere on the site.
- **The Terms predate the company.** Both legal documents are dated "Updated: Mar. 16, 2026 / Effective: Mar. 16, 2026", while the company directory records Touchine AI (HK) Limited as incorporated on 2026-04-28 ([Terms](https://ojo.art/terms), [tempb.com](https://www.tempb.com/companies/touchine-ai-hk-limited/)).
- **Skill counts differ.** The homepage advertises "200 多种" (200+) Skills; the X account states "OJO currently offers more than 300 skills" ([ojo.art/zh-CN](https://ojo.art/zh-CN/), [@OJOaidesign](https://x.com/OJOaidesign); both read 2026-08-26).
- **The pricing payload disagrees with its own display copy.** The Free plan's feature line reads "每日登录 100 积分" while the plan's `credits` field and the rendered page both say 200. The Plus annual feature line reads "每年 30,000 积分" while the annual `credits` field and the rendered page both say 26,400 ([billing plans API](https://ojo.art/subscribe); read 2026-08-26).
- **Three descriptions of what the product is.** The Terms (Mar. 16, 2026) describe "an AI-powered visual design platform" doing "Text-to-image and image-to-image generation … Brand kit generation and asset management"; the Help Center (Mar 28, 2026) describes "an AI-powered design and development platform" that produces runnable prototypes and syncs to code; the homepage and launch post (Aug 2026) describe a "Design Agent Team Workspace" for product strategy, PRDs and prototypes. The Terms' feature list does not match the surfaces the current product documents.
- **The company's own artifacts and the press describe different corporate homes.** The company is registered in Hong Kong with a Wan Chai address and a `Hong Kong` location on its GitHub organization, while the founder is reported to have registered a wholly owned company in Shenzhen and `touchine.com` is filed in Beijing ([Terms](https://ojo.art/terms), [GitHub API](https://api.github.com/orgs/touchine-ojo), [每日经济新闻, 2026-05-13](https://www.nbd.com.cn/articles/2026-05-13/4391026.html), [touchine.com](https://touchine.com/)).
- **Two Discord invites in circulation.** The website links `discord.gg/Fw55pk7z3N` and the X bio links `discord.gg/GDtZg4Fs27`; both resolve to the same server (invite API; read 2026-08-26).

### Other

- **The brand is younger than the product.** The VS Code extension was published on 2026-03-20 and already described "Ojo platform integration", the domain `ojo.art` was registered on 2026-03-03, and the legal documents are dated 2026-03-16 — roughly five months before the 2026-08-18 public introduction ([VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=nexight.ojo), WHOIS, [Terms](https://ojo.art/terms), [@OJOaidesign](https://x.com/OJOaidesign/status/2089731834095489430)).
- **Access is distributed as codes on X.** The company replied to its own launch post with "Go ojo.art and use OJO-T4FMC29RJE everyone." and later "use this: OJO-JT2G452FKN"; the X bio reads "Comment OJO to get early access" ([@OJOaidesign](https://x.com/OJOaidesign/status/2089731834095489430); read 2026-08-26). Third parties have republished codes, e.g. `OJO-MDTAM37V8T` ([versun.me, 2026-08-20](https://versun.me/blog/tweet-2090310807007752333)).
- **Billing is built for both a Western and a Chinese customer.** Every paid item lists Stripe and Antom as checkout providers and card plus Alipay as payment methods, prices are in USD, and the privacy policy provisions separate China-mainland data infrastructure ([billing plans API](https://ojo.art/subscribe), [Privacy Policy](https://ojo.art/privacy-policy) §3.1).
- **The blog is a large SEO surface for a private-beta product.** 16 posts across three series are published in all six locales — 96 localized URLs — with titles targeting queries such as "What Is an AI Design Agent?", "Prompt to UI: How to Generate Product Interfaces with AI" and "AI Website Design Generator" ([blog index](https://ojo.art/blog/posts/); read 2026-08-26).
- **Launch amplification came through creator accounts.** The company's own posts quote and boost third-party threads from accounts such as `@jshguo`, `@PrajwalTomar_`, `@Shruti_0810` and `@yabhishekhd` ([@OJOaidesign](https://x.com/OJOaidesign); read 2026-08-26).
- **A competitor's account publicly vouched for OJO before launch.** 硅星人Pro reports that after startup rumours about OJO circulated on Chinese social media, the account of Cutto (`cutto.ai`) commented under multiple posts on OJO's behalf, saying the two companies' founders are friends and that a founder leaving 剪映 would carry non-compete obligations and therefore could not build an AI video product ([硅星人Pro via 虎嗅, 2026-08-12](https://www.huxiu.com/article/4882486.html)).
- **OJO sits inside a documented wave of 剪映 alumni startups.** The same survey names LibTV, Lovart, LibLib, Noisee, YouWare, Bloome, VidMuse, OiiOii, Pexo, Cutto, Renoise and Flova alongside OJO, and reports at least ten AI application companies founded by 剪映 alumni over two years ([硅星人Pro via 虎嗅, 2026-08-12](https://www.huxiu.com/article/4882486.html)).
- **A name collision matters for research.** "OJO" also names OJO Labs, an Austin real-estate AI company that raised $20.5M in 2018 and $45M in 2019; most search results for "OJO" plus funding, careers or leadership terms return that company, not this one ([PR Newswire, 2018](https://www.prnewswire.com/news-releases/ojo-labs-raises-20-5-million-in-series-b-financing-to-propel-its-conversational-ai-ojo-to-millions-of-consumers-300650811.html), [PR Newswire, 2019](https://www.prnewswire.com/news-releases/ojo-labs-raises-45-million-in-series-c-funding-to-accelerate-product-development-and-fuel-expansion-300814706.html)).

---

## Resources

**Official**

- [ojo.art](https://ojo.art/) · [zh-CN](https://ojo.art/zh-CN/) · [zh-HK](https://ojo.art/zh-HK/) · [ja](https://ojo.art/ja/) · [es](https://ojo.art/es/) · [ko](https://ojo.art/ko/)
- [Terms of Service](https://ojo.art/terms) (Updated/Effective Mar. 16, 2026) · [Privacy Policy](https://ojo.art/privacy-policy) (Updated/Effective Mar. 16, 2026) · [Help Center](https://ojo.art/help-center) (Last updated Mar 28, 2026)
- [Pricing](https://ojo.art/subscribe) · [Blog (English)](https://ojo.art/blog/posts/) · [Blog (简体中文)](https://ojo.art/blog/zh-cn/posts/)
- [robots.txt](https://ojo.art/robots.txt) · [sitemap index](https://ojo.art/sitemap.xml) · [pages sitemap](https://ojo.art/pages-sitemap.xml)
- Social — [X @OJOaidesign](https://x.com/OJOaidesign) · [Launch post, 2026-08-18](https://x.com/OJOaidesign/status/2089731834095489430) · [Discord](https://discord.gg/Fw55pk7z3N) · [Discord invite API record](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true)
- Founder — [X @kiki_ZHANG_OJO](https://x.com/kiki_ZHANG_OJO) · [founder's launch post, 2026-08-19](https://x.com/kiki_ZHANG_OJO/status/2089746515246133495)
- Developer artifacts — [npm `@touchine/ojo`](https://www.npmjs.com/package/@touchine/ojo) · [npm registry record](https://registry.npmjs.org/@touchine%2Fojo) · [VS Code extension `nexight.ojo`](https://marketplace.visualstudio.com/items?itemName=nexight.ojo) · [GitHub org `irise-studio`](https://github.com/irise-studio) · [GitHub org `touchine-ojo`](https://github.com/touchine-ojo) · [OJO-Design-Skills](https://github.com/touchine-ojo/OJO-Design-Skills) · [CODEOWNERS](https://github.com/touchine-ojo/OJO-Design-Skills/blob/main/.github/CODEOWNERS)
- Related domains — [touchine.ai](https://touchine.ai/) (redirects to `ojo.art`) · [touchine.com](https://touchine.com/) (separate site, Beijing ICP filing)

**Third-party**

- [tempb.com — Touchine AI (HK) Limited](https://www.tempb.com/companies/touchine-ai-hk-limited/) (Hong Kong company directory aggregator)
- [aiposthub.com — OJO 是什麼？AI Design Agent Team 功能與限制](https://www.aiposthub.com/ojo-ai-design-agent-team-workspace/) (2026-08-19)
- [versun.me — invite code repost](https://versun.me/blog/tweet-2090310807007752333) (2026-08-20)
- [硅星人Pro via 虎嗅 — 剪映员工离职创业已出现「人传人」现象](https://www.huxiu.com/article/4882486.html) (2026-08-12) — the article that identifies OJO's founder
- [鲁中晨报 via 网易 — 字节跳动剪映产品负责人张琪智（KiKi）离职创业](https://www.163.com/dy/article/KSRD3PT40530JPVV.html) (2026-05-13)
- [澎湃新闻 — 剪映产品负责人张琪智被曝离职](https://m.thepaper.cn/newsDetail_forward_33177991) · [每日经济新闻](https://www.nbd.com.cn/articles/2026-05-13/4391026.html) (2026-05-13) · [DoNews](https://www.donews.com/news/detail/4/6547954.html)
- [iTunes search API — no first-party app in the US storefront](https://itunes.apple.com/search?term=ojo%20design%20agent&entity=software&country=us&limit=5)

**Unrelated company with the same name (for disambiguation)**

- [OJO Labs Series B, 2018](https://www.prnewswire.com/news-releases/ojo-labs-raises-20-5-million-in-series-b-financing-to-propel-its-conversational-ai-ojo-to-millions-of-consumers-300650811.html) · [OJO Labs Series C, 2019](https://www.prnewswire.com/news-releases/ojo-labs-raises-45-million-in-series-c-funding-to-accelerate-product-development-and-fuel-expansion-300814706.html)
