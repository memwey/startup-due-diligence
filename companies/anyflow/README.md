# Anyflow

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Anyflow (Anyflow株式会社, corporate number 1011001109588) is a Tokyo company whose main product, **Anyflow Embed**, is an embedded iPaaS (組み込み型iPaaS): SaaS vendors use its no-code editor, connectors and JavaScript SDK to ship integrations with other SaaS products inside their own product. It also sells **Anyflow Automation**, described on its product page as a "Headless iPaaS" for connecting a SaaS vendor's product with enterprise core systems ([homepage](https://anyflow.jp/); Undated; accessed 2026-10-11). The company dates its founding to 2016-02-12; the legal entity started as Revode株式会社, became 株式会社ピケ in 2017 and Anyflow株式会社 in 2019 ([国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588); record as of 2026-10-11). Since 2024-12-10 it has been a wholly owned subsidiary of アスエネ株式会社 (Asuene), a CO2-accounting SaaS company ([Asuene release](https://prtimes.jp/main/html/rd/p/000000438.000058538.html), [Anyflow release](https://anyflow.jp/news/asuene-groupin); both 2024-12-10).

- Funding before the acquisition: a 2,000万円 seed round from Coral Capital (2019-09-24), a 約2.2億円 pre-Series A led by Global Brain and Globis Capital Partners (2020-01-08), and a capital and business alliance with Smaregi (2022-12-08, amount not disclosed). Asuene's acquisition release puts Anyflow's cumulative funding at "累計約3.4億円"; the purchase price was not disclosed ([Asuene, 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)).
- Scale disclosed by the company: 247 integrations released by customers on Embed in its first year and more than 24 million cumulative executions ([2024-07-16](https://anyflow.jp/news/anyflow-embed-1st-anniv)); "200種以上" connectable cloud services ([2026-05-28](https://anyflow.jp/news/iGZsEBie)). A 2025-06-11 release cites a Deloitte Tohmatsu MIC report naming Embed No.1 by share among "IT・Web向けSaaS開発連携型ツール" ([2025-06-11](https://anyflow.jp/news/2025-share-no1)).
- Headcount: "30名(業務委託含む)" ([HERP posting](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), posted 2025-12-22; accessed 2026-10-11). Other company-published figures range from about 20 to "30名強" (see `Notes`).
- Engineering, per job postings: Embed is built in **Python (FastAPI, Django ORM, Celery)** with a **TypeScript/React** frontend, **MySQL (Cloud SQL)** and **Redis**, on **GCP/GKE** with Terraform and ArgoCD; the Automation team writes customer workflows in **TypeScript (Deno, Node.js)** on Cloud Run. The security policy states all production systems run on Google Cloud in Japan ([security policy](https://docs-embed.anyflow.jp/policy/security-policy); Undated; accessed 2026-10-11). Postings are in Japanese and no English working-language statement was found; work is remote-first with a 10:30–17:30 flex core time ([careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671); Undated; accessed 2026-10-11).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Anyflow; products Anyflow Embed and Anyflow Automation | [homepage](https://anyflow.jp/); accessed 2026-10-11 |
| Legal name | Anyflow株式会社 / Anyflow Inc. (フリガナ エニーフロー) | [company page](https://anyflow.jp/about), [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588) |
| Corporate number | 1011001109588, designated 2016-02-17; qualified-invoice registration T1011001109588 | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588), [company page](https://anyflow.jp/about) |
| Former legal names | Revode株式会社 (until 2017-05-31); 株式会社ピケ (2017-05-31 to 2019-01-30) | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588) |
| Founded | 2016-02-12 (company statement) | [company page](https://anyflow.jp/about) |
| Registered head office | 東京都港区新橋2丁目20番15号 新橋駅前ビル1号館6階, registered from 2025-04-16 | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588); information as of 2026-10-11 |
| Address on company page | 〒105-0001 東京都港区虎ノ門1-3-1 東京虎ノ門グローバルスクエア6階 — the same address Asuene moved its head office to on 2026-05-25 | [company page](https://anyflow.jp/about), [Asuene, 2026-05-07](https://prtimes.jp/main/html/rd/p/000000681.000058538.html) |
| Management | 代表取締役CEO 坂本 蓮; 取締役CTO 大久保 陽平; 執行役員COO 阿部 遼介 | [company page](https://anyflow.jp/about); accessed 2026-10-11 |
| Shareholder | アスエネ株式会社, 100% since 2024-12-10 | [company page](https://anyflow.jp/about), [Asuene, 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html) |
| Capital | 1,000万円 | [HERP posting](https://herp.careers/v1/anyflow/NC0_ouH2OBRX); accessed 2026-10-11 |
| Headcount | "30名(業務委託含む)"; see `Notes` for other figures | [HERP posting](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), posted 2025-12-22 |
| Working language | All reviewed job postings are in Japanese; the workflow-builder posting requires business-level Japanese; no posting or FAQ states an English working language | [careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671), [workflow-builder posting](https://herp.careers/v1/anyflow/Jht3MH0DI3if); accessed 2026-10-11 |
| Total raised | "累計約3.4億円" before the acquisition (Asuene's statement); the company's own last stated figure was 約2.6億円 after the pre-Series A | [Asuene, 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html), [Anyflow, 2020-01-08](https://anyflow.jp/news/pre-seriesA-fundraise) |
| Investors named | Coral Capital, Global Brain, Globis Capital Partners, Smaregi; angels 古川健介, 堀井翔太, 赤坂優 (per BRIDGE) | [seed](https://anyflow.jp/news/seed-finance), [pre-Series A](https://anyflow.jp/news/pre-seriesA-fundraise), [Smaregi](https://prtimes.jp/main/html/rd/p/000000017.000034258.html), [BRIDGE, 2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding) |
| Security certification | ISMS IS 751085, JIS Q 27001:2025 (ISO/IEC 27001:2022+Amd 1:2024), certified by BSI Group Japan; first registered 2021-10-12, valid to 2027-10-11; scope "iPaaSの企画・開発及び運営" | [ISMS registry](https://isms.jp/lst/ind/CR_IS_x0020_751085.html); accessed 2026-10-11 |
| Patent | JP7645548B2 「システム、方法、およびプログラム」, application JP2022-103544 filed 2022-06-28, inventors 坂本 蓮, 大久保 陽平, 川村 将史; Google Patents lists issue date 2025-03-14 | [Google Patents](https://patents.google.com/patent/JP7645548B2/ja), [JP2024004078A](https://patents.google.com/patent/JP2024004078A/ja) |
| Hosting | "すべてのプロダクションシステムとデータベースは、日本にホストされているGoogle Cloud Platformで稼働" | [security policy](https://docs-embed.anyflow.jp/policy/security-policy); accessed 2026-10-11 |

### Identity and legal entities

| Name | Type | Period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Revode株式会社 | Former legal name | 2016-02 to 2017-05-31 | Same corporate number 1011001109588 | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588) |
| 株式会社ピケ | Former legal name | 2017-05-31 to 2019-01-30 | Same corporate number; announced the cloud RPA "Anybot" in 2018 | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588), [PR TIMES, 2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html) |
| Anybot | Former product brand | Pre-registration from 2018-10-24 | Cloud RPA from 株式会社ピケ; `anybot.ai` now redirects to `anyflow.co.jp`, which redirects to `anyflow.jp` (checked 2026-10-11) | [PR TIMES, 2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html) |
| Anyflow (original iPaaS) | Earlier product of the same entity | β from 2019-10 | No-code SaaS-to-SaaS automation for businesses; the CTO states Embed was built from scratch rather than by extending it | [pre-Series A release](https://anyflow.jp/news/pre-seriesA-fundraise), [Green CTO profile](https://www.green-japan.com/company/10894/pr) |
| アスエネ株式会社 | Parent company | From 2024-12-10 | Acquired 100% of shares; lists Anyflow among its group companies as "AIデータ連携プラットフォーム「Anyflow」" | [Asuene, 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html), [Asuene, 2026-06-26](https://prtimes.jp/main/html/rd/p/000000711.000058538.html) |

The company's own notice dates the change to Anyflow株式会社 to 2019-01-17 ([2019-01-17](https://anyflow.jp/news/rename-company-name)); the register records 2019-01-30 (see `Notes`).

**Programs and awards** (company-announced unless noted): finalist at the IVS 2019 Summer Launchpad, first overall at Incubate Camp 12th, winner of the B Dash Camp 2019 Fall Pitch Arena ([pre-Series A release](https://anyflow.jp/news/pre-seriesA-fundraise), [PR TIMES, 2019-11-05](https://prtimes.jp/main/html/rd/p/000000004.000034258.html)); 優秀賞 at the 8th FUJITSU ACCELERATOR pitch contest ([2020-02-10](https://anyflow.jp/news/fujitsu-accelerator)); EY Innovative Startup 2020 ([PR TIMES, 2020-02-28](https://prtimes.jp/main/html/rd/p/000000007.000034258.html)); the original Anyflow product registered as an IT tool under the METI IT導入補助金2020 ([PR TIMES, 2020-08-06](https://prtimes.jp/main/html/rd/p/000000014.000034258.html)); CEO named to Forbes 30 Under 30 Asia 2022, Enterprise Technology ([2022-05-26](https://anyflow.jp/news/forbes-30-under-30-asia-2022)). The careers page links elevator pitches at Startup Aquarium 2023 and 2024 ([careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)).

### Market context as stated by the company

- The Embed page cites SaaStr Annual 2021 for the claim that 30% of users considering a SaaS purchase require integration with other SaaS, and states that an in-house integration typically takes 3–6 months ([Embed page](https://anyflow.jp/products/embed); Undated; accessed 2026-10-11).
- A company survey of 111 B2B SaaS buyers (internet survey via IDEATECH's リサピー, fielded 2026-05-18 to 05-19) reports that 75.7% had excluded a SaaS for insufficient API integration before comparing features or price, and 63.1% had chosen a different service because of missing integrations ([2026-07-14](https://anyflow.jp/news/3RLk2a_Q)). The release headline uses a different figure (see `Notes`).
- Asuene's acquisition release frames the deal around Scope 1–3 disclosure under SSBJ standards and the effort of collecting activity data from ERP and SaaS systems ([Asuene, 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)).

---

## Product

### What it is and its feature areas

**Anyflow Embed** — "SaaS事業者向けの組み込み型iPaaS" that lets a vendor deliver integrations with other systems "最短1週間" ([homepage](https://anyflow.jp/)). Generally available since 2023-07-13 ([2023-07-13](https://anyflow.jp/news/anyflow-embed)); BRIDGE reported it had been in development for about two years and offered in stealth before then ([BRIDGE, 2023-07-13](https://thebridge.jp/2023/07/anyflow-embed-official-launch)). The documentation at [docs-embed.anyflow.jp](https://docs-embed.anyflow.jp/) (149 pages in its [sitemap](https://docs-embed.anyflow.jp/sitemap-pages.xml), accessed 2026-10-11) is organized as:

| Area | What the docs cover |
|---|---|
| Solution editor | Triggers (polling, realtime, scheduler; vendor-initiated Webhook, Request and "My Event" triggers), actions (built-in, HTTP and custom API calls; key-value store, log and mail; CSV, date-time, list, variable and an opt-in restricted [Python action](https://docs-embed.anyflow.jp/solution-editor/actions/data-transform/python) without `import`), logic (if, loop, pagination, error monitoring, stop), variables |
| Wizard editor | The end-user setup screen embedded in the vendor's product, with widgets such as mapping, condition, CSV and table-assist |
| Release | Deploy and [deployment environments](https://docs-embed.anyflow.jp/release/deploy-environment) (dev/staging/production), embedding via the SDK with vendor-generated [RS256 JWTs](https://docs-embed.anyflow.jp/release/embed/generate-jwt), and [wizard hosting](https://docs-embed.anyflow.jp/release/wizard-hosting) on an Anyflow domain |
| Anyflow SDK | `@anyflowinc/embed-sdk` on npm; [changelog](https://docs-embed.anyflow.jp/anyflow-sdk/docs/changelog) to v0.16.0 (2026-03-18) |
| Anyflow API | End-user API, [Vender Server API](https://docs-embed.anyflow.jp/anyflow-api/vender-server-api) (API-secret → bearer token at `embed-vender-api.anyflow.jp`), webhooks |
| Operations | Execution history for vendors and end users, error handling and retries, event notifications, [execution limits](https://docs-embed.anyflow.jp/ops/step-execution-limit) |
| Connectors | Connector list, custom OAuth clients, per-connector notes |
| Policy | [Security policy](https://docs-embed.anyflow.jp/policy/security-policy), [service level](https://docs-embed.anyflow.jp/policy/service-level), [incident response](https://docs-embed.anyflow.jp/policy/incident-response), responsibility split |
| Code solutions (β) | Integration logic written in TypeScript on Deno through the "Embed CLI", designed for coding agents such as Claude Code or Codex; limited to some customers since 2026-07 ([docs](https://docs-embed.anyflow.jp/release-notes/code-solution), [2026-07-28](https://anyflow.jp/news/o3pigXgy)) |

Dated feature releases include "My Event" for vendors without a public API ([2024-01-16](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)), "リクエスト&レスポンス" for two-way exchange without a public API ([2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html)), "コードアクション" for running code in a chosen language and version inside no-code flows ([2025-04-17](https://anyflow.jp/news/code-action)), and an "AI エージェント / RAG向けデータ自動連携サービス" that syncs customer data from Google Drive, Box, SharePoint, Gmail, Slack and others into a vector database ([2026-05-28](https://anyflow.jp/news/iGZsEBie)). The [release notes](https://docs-embed.anyflow.jp/release-notes/recent) list smaller changes through 2026-03-18.

**Anyflow Automation** — the product page describes it as "SaaS事業者向けのHeadless iPaaS" that integrates enterprise customers' existing systems with the vendor's SaaS, using APIs where available and CSV or database connections otherwise, with "100以上" connectors and fully managed infrastructure ([Automation page](https://anyflow.jp/products/automation); Undated; accessed 2026-10-11). Job postings describe delivery as customer projects: a workflow-building team writes each integration in TypeScript, generally waterfall, with enterprise projects under 10 person-months ([workflow-builder posting](https://herp.careers/v1/anyflow/Jht3MH0DI3if), [PM lead posting](https://herp.careers/v1/anyflow/T7Zo5Ic0m7_7)).

**Other offerings.** A 2026-03-31 notice ended four Smaregi-related integration apps on 2026-04-30 and named "Anyflow Connect" as their successor, at partly changed prices ([2026-03-31](https://anyflow.jp/news/smaregi-integration-end)); no product page for Anyflow Connect was found. The technical customer success posting refers to "Anyflow Embedカスタムメイド版" deployed for specific customers ([posting](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)).

### Commercialization

No public price list exists for Embed or Automation; both product pages route to a demo or consultation form. The [terms of use](https://anyflow.jp/terms) (enacted 2019-11-29, last amended 2022-07-20) define the fee components as an onboarding fee, a fixed monthly fee, a usage-based monthly fee, option fees and other fees, each set in the order form, invoiced and paid by bank transfer; fees for the full contract term other than usage fees are paid in one lump sum by the end of the month after service starts. The Embed page says building, designing, testing and deploying an integration can be done by the customer or delegated to Anyflow ([Embed page](https://anyflow.jp/products/embed)). Earlier products published prices: Anybot "月額7万円から" during its beta ([2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html)) and the original Anyflow "月額3万円から" ([2020-08-06](https://prtimes.jp/main/html/rd/p/000000014.000034258.html)).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2019-09-24 | About 10 supported SaaS, mainly Japanese (original Anyflow) | [BRIDGE](https://thebridge.jp/2019/09/anyflow-seed-round-funding) |
| 2020-01-08 | "数百件以上" enterprise inquiries since launch; paid traction "出始めた" | [BRIDGE](https://thebridge.jp/2020/01/anyflow-pre-series-a-round-funding) |
| 2023-07-13 | 16 SaaS companies publicly known to use Embed at GA | [BRIDGE](https://thebridge.jp/2023/07/anyflow-embed-official-launch) |
| 2024-07-16 | 247 integrations released to production on Embed between 2023-07-13 and 2024-07-12; more than 24 million cumulative executions | [Anyflow](https://anyflow.jp/news/anyflow-embed-1st-anniv) |
| 2025-02-19 | "140種類以上の連携コネクタ" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000032.000034258.html) |
| 2025-06-11 | No.1 share among "IT・Web向けSaaS開発連携型ツール" in デロイト トーマツ ミック経済研究所's "SaaS管理・運用・開発市場(SaaS for SaaS)の実態と展望 2024年度版" | [Anyflow](https://anyflow.jp/news/2025-share-no1) |
| Posted 2025-12-12 | "日々数十万件タスクを処理" | [SRE posting](https://herp.careers/v1/anyflow/5sHcw3MfypEy) |
| 2026-05-28 | "200種以上のクラウドサービス" connectable | [Anyflow](https://anyflow.jp/news/iGZsEBie) |
| Accessed 2026-10-11 | 165 connector pages in the site's connector sitemap | [sitemap](https://anyflow.jp/sitemap.xml) |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2022-12-08](https://prtimes.jp/main/html/rd/p/000000017.000034258.html) | スマレジ | Capital and business alliance; Embed used for Smaregi POS integrations with EC sites and Google Sheets |
| [2023-07-19](https://prtimes.jp/main/html/rd/p/000000019.000034258.html) | 弥生 | Business alliance; Embed adopted as the API integration base for 弥生会計 and other products |
| [2023-08-29](https://anyflow.jp/news/smarthr-plus) | SmartHR / freee | "freee人事労務 年末調整連携 by Anyflow Embed" built for the SmartHR Plus app store |
| [2023-11-29](https://anyflow.jp/news/anyflow-embed-netprotections) | ネットプロテクションズ | Embed adopted for NP掛け払い |
| [2024-03-12](https://anyflow.jp/news/moneyforward-cloud) | マネーフォワード | Embed connectors for five マネーフォワード クラウド products |
| [2024-07-16](https://anyflow.jp/news/anyflow-embed-1st-anniv) | DIGGLE, インフォボックス, KAEN, 日本パープル, Sales Marker, SmartHR, Srush and four others | Customer comments published for the first anniversary |
| [2025-02-19](https://prtimes.jp/main/html/rd/p/000000032.000034258.html) | アスエネ (parent) | ASUENE adopts Embed; Asuene announced integrations with 勘定奉行クラウド, freee会計 and ESGTech ([Asuene](https://prtimes.jp/main/html/rd/p/000000461.000058538.html)) |
| [2025-05-23](https://anyflow.jp/news/case-smarthr) | SmartHR | Case study: 15 integrations delivered in one year |

### Stated plans

- Code solutions: deployment, execution logs in the admin console and more supported apps before a formal release ([2026-07-28](https://anyflow.jp/news/o3pigXgy)).
- Group integration: use Asuene's sales base to expand Embed's sales network and apply Anyflow's integration technology to CO2 data collection ([2024-12-10](https://anyflow.jp/news/asuene-groupin)).
- Enterprise: an Enterprise BizDev posting describes the SMB business as growing and seeks a hire to roll solutions out to enterprise customers, naming regional banks (地銀) as example customers ([posting](https://herp.careers/v1/anyflow/oMisMJmQvdea), posted 2026-07-23).

---

## Founder

**坂本 蓮 (Ren Sakamoto)** — 代表取締役CEO ([company page](https://anyflow.jp/about)).

- Started programming in junior high school ([Wantedly posting, 2024-05-11, closed](https://www.wantedly.com/projects/1698588)).
- In his fourth year at university, selected for KDDI's accelerator KDDI ∞ Labo; founded the company in February just before graduating because the program required one ([Founder interview, 2019-06-17](https://found-er.com/interview/1442/)). BRIDGE reports that he earlier built AppMotor, a bug-fixing support platform for programmers, selected for ∞ Labo's 9th batch ([BRIDGE, 2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding)).
- After graduating, joined CyberAgent, where he maintained Ameba infrastructure ([Founder interview](https://found-er.com/interview/1442/)); a later posting describes the role as server-side engineer ([Wantedly](https://www.wantedly.com/projects/1698588)).
- Says he built about 20 products, including the lunch app "Dish", and that Anyflow started as an RPA product before pivoting to iPaaS ([Founder interview](https://found-er.com/interview/1442/)). As CEO of 株式会社ピケ he announced the cloud RPA Anybot on 2018-10-24 ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000001.000034258.html)).
- Named to Forbes 30 Under 30 Asia 2022, Enterprise Technology ([2022-05-26](https://anyflow.jp/news/forbes-30-under-30-asia-2022)); listed inventor on JP7645548B2 ([Google Patents](https://patents.google.com/patent/JP7645548B2/ja)).

**Co-founders.** BRIDGE named 中西 奎太 as co-founder in 2019 ([BRIDGE, 2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding)); he is not listed on the current [company page](https://anyflow.jp/about). The CEO interview says there are three founders, all engineers ([Founder interview](https://found-er.com/interview/1442/)); the third founder is not named in any source reviewed.

### Selected leadership

**大久保 陽平 (Yohei Okubo)** — 取締役CTO. Joined in January 2021, first as a contractor, working on the Celery-based workflow engine, SaaS connectors, CI automation, log monitoring and Kubernetes operations; about a year later the CEO and the previous CTO asked him to take the CTO role, and the previous CTO continued as an engineer on Embed. Earlier: ad-operations tooling at a large web advertising agency as a new graduate, then freelance tech lead, SRE and data engineering work ([Green, accessed 2026-10-11](https://www.green-japan.com/company/10894/pr)). Listed inventor on JP7645548B2.

**阿部 遼介** — 執行役員COO ([company page](https://anyflow.jp/about)). The Enterprise BizDev role reports directly to the COO ([posting](https://herp.careers/v1/anyflow/oMisMJmQvdea)). No career background was found.

**須永 智成** — Anyflow Embed 事業責任者・プロダクトオーナー; joined in 2023 after a financial group (smartphone-app PM) and the interactive-video startup MIL ([2026-06-29](https://anyflow.jp/news/_8Tdn3Ok)).

A closed 2024 Wantedly posting also listed 松田 光希 (CFO, formerly IPO lead at a listed company) and 藤本 遼平 (marketing, ex-DeNA and Wantedly) ([Wantedly, 2024-05-11](https://www.wantedly.com/projects/1698588)); neither appears on the current company page. The careers FAQ gives the organization mix as engineers and designers 55%, CS/CRE and sales 40%, back office 5% ([careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)).

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Before 2019-09 (date not stated) | Angel round (BRIDGE's description) | not stated separately | 古川健介, 堀井翔太, 赤坂優 | — | [BRIDGE](https://thebridge.jp/2019/09/anyflow-seed-round-funding) |
| 2019-09-24 | シードラウンド (J-KISS型新株予約権方式) | 2,000万円 | Coral Capital | 5,000万円 incl. angel round (BRIDGE) | [Anyflow](https://anyflow.jp/news/seed-finance), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000034258.html) |
| 2020-01-08 | プレシリーズA | 約2.2億円 | グローバル・ブレイン (lead), グロービス・キャピタル・パートナーズ (lead), Coral Capital | 約2.6億円 (company) | [Anyflow](https://anyflow.jp/news/pre-seriesA-fundraise), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000005.000034258.html) |
| 2022-12-08 | 資本業務提携 | not disclosed | スマレジ | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000017.000034258.html) |
| 2024-12-10 | 完全子会社化 (acquisition) | not disclosed | アスエネ acquired 100% of shares | "累計約3.4億円" raised before the acquisition (Asuene) | [Asuene](https://prtimes.jp/main/html/rd/p/000000438.000058538.html), [Anyflow](https://anyflow.jp/news/asuene-groupin) |

Coral Capital invested in the seed round and again in the pre-Series A. The pre-Series A release stated the funds would go to product development and speed, and that the company planned to become a platform integrating and managing domestic and overseas SaaS ([2020-01-08](https://anyflow.jp/news/pre-seriesA-fundraise)). The Smaregi alliance was announced together with Smaregi's use of Embed for POS–EC integrations, and the Yayoi alliance seven months later; Embed reached GA between them, on 2023-07-13. Neither the gap between 約2.6億円 (2020) and 約3.4億円 (2024) nor the Smaregi amount is broken down in any reviewed source.

---

## Engineering

### Technology stack and platforms

**Confirmed by documentation or public assets**

- **Hosting:** Google Cloud in Japan for all production systems and databases ([security policy](https://docs-embed.anyflow.jp/policy/security-policy)). The public [status page](https://anyflow-embed.statuspage.io/) tracks GKE, Cloud SQL and Stackdriver as components, plus Netlify (origin servers and edge network) (accessed 2026-10-11).
- **SDK:** `@anyflowinc/embed-sdk`, a JavaScript/TypeScript SDK on [npm](https://www.npmjs.com/package/@anyflowinc/embed-sdk) — first published 2023-05-19, v0.16.0 on 2026-03-18; its dev dependencies include TypeScript, Rollup, Jest and ESLint (npm registry metadata, accessed 2026-10-11). The wizard is rendered in an iframe and authenticated with RS256 JWTs signed by the vendor's backend ([SDK docs](https://docs-embed.anyflow.jp/anyflow-sdk/docs), [JWT docs](https://docs-embed.anyflow.jp/release/embed/generate-jwt)).
- **Code solutions:** TypeScript on **Deno 2.x**; the `embed` CLI binary (no Windows build; WSL on Windows) logs in through **Auth0** (OAuth 2.0 Authorization Code Flow); SaaS clients are `@anyflowinc/<name>` packages added with `deno add`; sandbox limits 1 GiB memory, 60-minute run time, no filesystem writes ([docs](https://docs-embed.anyflow.jp/release-notes/code-solution)). The JSR scope `@anyflowinc` exists (created 2024-03-05) with no public packages listed ([JSR](https://jsr.io/@anyflowinc); accessed 2026-10-11).
- **Python:** an opt-in Python action runs a restricted subset with `import` disabled ([docs](https://docs-embed.anyflow.jp/solution-editor/actions/data-transform/python)).
- **Security tooling stated in the policy:** admin console login limited to SSO with an IdP such as Google Workspace; 1Password for shared credentials; credentials encrypted with 256-bit encryption ([security policy](https://docs-embed.anyflow.jp/policy/security-policy)).

**Inferred from current job postings** (accessed 2026-10-11)

- **Embed backend:** Python, FastAPI, Django ORM, Celery; design described as DDD with hexagonal architecture ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), [SRE](https://herp.careers/v1/anyflow/5sHcw3MfypEy)). The CTO's profile confirms a Celery-based workflow engine ([Green](https://www.green-japan.com/company/10894/pr)).
- **Embed frontend:** TypeScript, React, Linaria, ESLint, Prettier, Jest ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)).
- **Data:** MySQL on Cloud SQL, Redis ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)).
- **Infrastructure:** GCP (GKE, GCS, Cloud SQL, Cloud IAP, Cloud NAT, Cloud Build, BigQuery, Cloud KMS, Cloud Pub/Sub), Kubernetes; CI/CD and IaC with GitHub Actions, Cloud Build, ArgoCD, Terraform; monitoring and security with Datadog, Stackdriver, Trivy ([SRE](https://herp.careers/v1/anyflow/5sHcw3MfypEy)).
- **Automation team:** TypeScript (Deno, Node.js) on GCP (Cloud Run, Cloud SQL, BigQuery, Cloud Logging, Cloud KMS, Cloud Scheduler, Cloud Storage, Cloud Armor, Identity Platform, Firestore), Resend; GitHub Actions, Cloud Build, Terraform ([workflow-builder posting](https://herp.careers/v1/anyflow/Jht3MH0DI3if)).
- **Tools:** Linear, Notion, Slack, GitHub; AI tools listed as available: Claude Code, GitHub Copilot, CodeRabbit, ChatGPT, Devin, Gemini ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)).

**Hiring-only mentions:** React (Next.js), Airflow and Digdag appear only as preferred qualifications ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)).

### Systems

| System | What it does | Source |
|---|---|---|
| Workflow engine | In-house engine that executes integration "solutions"; the Software Engineer role covers new features, improvements and speed-ups | [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), [Green](https://www.green-japan.com/company/10894/pr) |
| Connectors | Per-SaaS connectors with authentication (including custom OAuth clients) and maintenance when third-party APIs change; CRE staff build modules in Python with a "コネクタSDK" | [Embed page](https://anyflow.jp/products/embed), [CRE posting](https://herp.careers/v1/anyflow/IZa74EMW4xS1) |
| Wizard and SDK | End-user setup UI embedded via iframe or hosted on an Anyflow domain; JWT-based identity of the vendor's users | [SDK docs](https://docs-embed.anyflow.jp/anyflow-sdk/docs), [wizard hosting](https://docs-embed.anyflow.jp/release/wizard-hosting) |
| Vendor-side triggers | Webhook, Request (with response step) and My Event triggers let a vendor push data without a public API; rate limit 100 requests per 10 s per source IP, 20 MB request soft limit | [limits](https://docs-embed.anyflow.jp/ops/step-execution-limit), [2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html) |
| Code-solution runtime | Sandboxed Deno execution of agent-written `main.ts`, synced with `embed pull` / `embed push` | [docs](https://docs-embed.anyflow.jp/release-notes/code-solution) |
| AI agent / RAG data sync | Scheduled collection of customers' documents and messages from 200+ services into a vector database | [2026-05-28](https://anyflow.jp/news/iGZsEBie) |
| Execution history and monitoring | Vendor and end-user run histories, step-level log masking, event notifications to six external tools ([2024-12-26](https://prtimes.jp/main/html/rd/p/000000031.000034258.html)), metrics/log/synthetic monitoring at ≤2-minute intervals, autoscaling | [release notes](https://docs-embed.anyflow.jp/release-notes/recent), [incident response](https://docs-embed.anyflow.jp/policy/incident-response) |

Documented operating limits: 10 MB soft limit per action step (1 MB with polling triggers), 100 MB hard limit on stored logs per step, 12-hour solution timeout ([limits](https://docs-embed.anyflow.jp/ops/step-execution-limit)). Raw execution data is deleted 30 days after a run; daily encrypted backups are kept for up to 7 days ([security policy](https://docs-embed.anyflow.jp/policy/security-policy)). The availability target is 99.8%, measured quarterly, and the page states no SLA is defined ([service level](https://docs-embed.anyflow.jp/policy/service-level)).

### Technical background sought

- **Software Engineer (Embed):** required — designing, building and operating Web APIs; database schema design and operation; team development with Git; development using AI coding agents such as Claude Code. Preferred — complex web apps such as WYSIWYG editors; GCP/Kubernetes operations; asynchronous processing; CI-based automated testing; performance work and continuous refactoring; DDD; external API integrations; leading B2B development ([posting](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)).
- **SRE:** required — Kubernetes and cloud infrastructure operations, database schema design. Preferred — operating servers with more than 100 million monthly accesses, architecture spanning application and infrastructure, external API integrations ([posting](https://herp.careers/v1/anyflow/5sHcw3MfypEy)).
- **Workflow-building engineer (Automation):** required — client work such as contract development or SI (negotiating requirements and changes, balancing deadlines and quality), unit testing. Preferred — project management, API integration, data integration with CSV, databases, batch and job design ([posting](https://herp.careers/v1/anyflow/Jht3MH0DI3if)).
- **Product Manager (Embed):** required — Scrum or agile delivery, continuous improvement from customer feedback, practical understanding of API/SaaS integration (REST, OAuth, Webhook). Preferred — B2B SaaS PdM or technical customer support, DevOps or developer-productivity work ([posting](https://herp.careers/v1/anyflow/qs53UJS4TYOX)).
- **CRE and technical customer success:** required — technical support for web services or CRE/implementation-engineer work, and client work for the enterprise role; preferred — Python, external API integrations, managing development projects ([CRE](https://herp.careers/v1/anyflow/IZa74EMW4xS1), [TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)).

### Industry domain

SaaS-to-SaaS and SaaS-to-core-system integration: third-party API authentication (OAuth, API keys), API version changes, pagination and rate limits, data mapping, CSV and database exchange for systems without APIs, and Japanese business SaaS such as accounting (freee, マネーフォワード, 弥生, 勘定奉行), HR (SmartHR) and POS (スマレジ) products. The Product Manager posting requires practical API/SaaS integration knowledge; for the engineering roles, external API integration experience is preferred, not required. Financial-sector experience is preferred for technical customer success, and regional-bank relationships for Enterprise BizDev ([TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO), [BizDev](https://herp.careers/v1/anyflow/oMisMJmQvdea)). Through the parent, part of the work concerns collecting activity data for Scope 1–3 CO2 accounting ([Asuene, 2025-02-19](https://prtimes.jp/main/html/rd/p/000000461.000058538.html)). None of the reviewed postings says whether domain knowledge can be learned after joining.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | Postings and careers page in Japanese; workflow-builder requires business-level Japanese; no English-language posting found | [careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671), [workflow builder](https://herp.careers/v1/anyflow/Jht3MH0DI3if) |
| Remote | Remote-first in principle; on-site events (all-hands, offsites) about once a quarter or half-year (planned); no weekly or biweekly office attendance currently required; remote from outside the Tokyo area allowed if events can be attended; office work possible at the Toranomon WeWork. Postings add that office attendance may be requested for some roles; the TCS role may involve on-site work at partners | [careers FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671), [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), [TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO) |
| Hours | Engineers on flextime with core time 10:30–17:30 (flexible 8:30–10:30 and 17:30–21:30); business roles 9:30–18:30; overtime "月10時間程度" | [careers FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671), [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX) |
| Salary (annual) | Software Engineer 600万–900万円; SRE 800万–1,200万円; Product Manager 600万–1,000万円; PM lead (Automation) 700万–1,000万円; workflow builder 500万–650万円; CRE 500万–700万円; TCS 500万–800万円; Enterprise BizDev 750万–1,150万円. The Software Engineer and SRE postings include a fixed overtime allowance for 45 hours in monthly pay | [HERP job list](https://herp.careers/v1/anyflow); accessed 2026-10-11 |
| Leave and probation | Two days off per week, 120 days off per year, paid leave in half-days, maternity leave, childcare leave (taken by men in the past); 3-month probation | [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX) |
| Benefits | Social insurance, health checks, company PC, books and external training, commuting allowance up to ¥20,000/month, AI tool accounts | [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX) |
| Hiring process | Optional casual interview, document screening, 1–3 online interviews, possible technical assignment, reference check via back check after the first interview, optional trial work (about one day, with Slack access) | [careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671) |
| Side jobs and contractors | Joining first as a side job or contractor is welcomed | [careers FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671) |
| Juniors and new graduates | Engineering postings require at least three years of web development; the only internships listed are webinar support and sales | [HERP job list](https://herp.careers/v1/anyflow) |
| Visa sponsorship | Not stated in any reviewed posting | — |
| Team practices | Embed uses Scrum (refinement, planning, retrospectives); Automation projects are generally waterfall; Embed engineers are all remote with a daily meeting of about 30 minutes | [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), [workflow builder](https://herp.careers/v1/anyflow/Jht3MH0DI3if) |
| Age and turnover | Average age about 36 (20s ~10%, 30s ~60%, 40s ~30%) per the careers FAQ; the 2024 Wantedly posting stated about 34 and no full-time departures in the previous two years | [careers FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671), [Wantedly, 2024-05-11](https://www.wantedly.com/projects/1698588) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11): anyflow.jp and its sitemap, robots.txt, company, product, case, news and legal pages; docs-embed.anyflow.jp and its sitemap; the status page; the Notion careers page and all HERP postings; PR TIMES pages for Anyflow and Asuene; the 国税庁 法人番号公表サイト, ISMS registry and Google Patents; GitHub organisation lookups for `anyflowinc`, `anyflow`, `anyflow-inc`, `anyflowjp` and `anyflow-jp`, npm and JSR; note, Speaker Deck, Zenn, Qiita, connpass, Wantedly, Green, TokyoDev and Japan Dev; web searches for Anyflow, Anyflow株式会社, Anyflow Embed, 株式会社ピケ and Anybot in Japanese and English; INITIAL and HERP company profiles as leads.

- **Revenue, ARR and customer count.** No absolute figure found. The only growth figure is "前ARR600%以上の成長" in the 2024 Wantedly posting, with no base or period ([Wantedly](https://www.wantedly.com/projects/1698588)).
- **Acquisition price and Smaregi investment.** Neither amount nor stake is disclosed ([Asuene](https://prtimes.jp/main/html/rd/p/000000438.000058538.html), [Smaregi alliance](https://prtimes.jp/main/html/rd/p/000000017.000034258.html)).
- **Price list** for Embed, Automation or Anyflow Connect.
- **Engineering blog.** None found. The [note account](https://note.com/anyflow) has one post (2020-05-11); the [Speaker Deck account](https://speakerdeck.com/anyflow) has one image-only company deck dated 2024-02-13; no Zenn publication, Qiita organisation or connpass group was found.
- **Open source.** The GitHub organisation [`anyflowinc`](https://github.com/anyflowinc) ("Anyflow Inc.", created 2017-05-01, X `anyflowinc`, email on `anyflow.co.jp`) has no public repositories ([GitHub API](https://api.github.com/orgs/anyflowinc)). The GitHub user `anyflow` belongs to an unrelated individual. The npm package `@anyflowinc/embed-sdk` declares no repository or license.
- **SLA.** "現在 SLA を定めておりません" ([service level](https://docs-embed.anyflow.jp/policy/service-level)).
- **Third co-founder's name, the COO's background, visa sponsorship and English-language roles.** Not found.

### Inconsistencies across sources

- **Founding date:** 2016-02-12 (company page and releases); the corporate number was designated 2016-02-17 under the name Revode株式会社 ([NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)); BRIDGE wrote that the company was founded in 2017 ([2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding)).
- **Rename date:** the company notice says the name changed "2019年1月17日より" ([notice](https://anyflow.jp/news/rename-company-name)); the register records the change on 2019-01-30 ([NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)).
- **Address:** the register shows 新橋2丁目20番15号 since 2025-04-16; the company page, 2026 releases and the ISMS registry show 虎ノ門1-3-1 東京虎ノ門グローバルスクエア6階; current HERP postings and the careers page show 虎ノ門1-10-5 KDX虎ノ門一丁目ビル WeWork 3階 アスエネ株式会社内; 2025 releases show the same building's WeWork 4階 ([2025-06-11](https://anyflow.jp/news/2025-share-no1)).
- **Cumulative funding:** 約2.6億円 after the pre-Series A (company and [Forbes JAPAN](https://forbesjapan.com/articles/detail/31650), both 2020-01-08) versus 2億7,000万円 ([BRIDGE, 2020-01-08](https://thebridge.jp/2020/01/anyflow-pre-series-a-round-funding)); 約3.4億円 before the acquisition ([Asuene, 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)); HERP's company profile shows 2.8億円, estimated from registry filings ([HERP profile](https://herp.careers/careers/companies/anyflow); accessed 2026-10-11).
- **Headcount:** "30名強" including contractors ([careers FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)); "30名(業務委託含む)" ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), posted 2025-12-22); Dev ~20 + Biz ~10 ([TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO), posted 2026-07-22); Dev 13 + Biz 12, ~25 ([Product Manager](https://herp.careers/v1/anyflow/qs53UJS4TYOX), posted 2025-12-12); Dev 11 + Biz 10, ~20 ([CRE](https://herp.careers/v1/anyflow/IZa74EMW4xS1), posted 2025-12-12). HERP's profile shows 18 employees based on pension-insurance enrolment for 2024-08 to 2026-08 ([HERP profile](https://herp.careers/careers/companies/anyflow)). In May 2024, Wantedly listed 15 members and 20 including contractors ([Wantedly](https://www.wantedly.com/projects/1698588)).
- **Connector count:** "100以上" ([Automation page](https://anyflow.jp/products/automation)), "140種類以上" ([2025-02-19](https://prtimes.jp/main/html/rd/p/000000032.000034258.html)), "200種以上" ([2026-05-28](https://anyflow.jp/news/iGZsEBie)), and 165 connector pages in the site sitemap (accessed 2026-10-11). The sources do not define what is counted.
- **What Anyflow Automation is:** "SaaS事業者向けのHeadless iPaaS" for enterprise core-system integration ([Automation page](https://anyflow.jp/products/automation)) and customer data-integration projects ([workflow builder](https://herp.careers/v1/anyflow/Jht3MH0DI3if)), versus "自社の業務を自動化、効率化するためのプラットフォーム" ([careers page](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)) and "社内業務の自動化を支援する" ([Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)).
- **Survey figure:** the 2026-07-14 release's headline and lead say 91.9% excluded a SaaS for insufficient API integration; its summary and detailed results give 75.7% for that question ([2026-07-14](https://anyflow.jp/news/3RLk2a_Q)).
- **ISMS standard:** the docs security policy cites JIS Q 27001:2014 (ISO/IEC 27001:2013) ([policy](https://docs-embed.anyflow.jp/policy/security-policy)); the registry shows JIS Q 27001:2025 (ISO/IEC 27001:2022+Amd 1:2024) ([registry](https://isms.jp/lst/ind/CR_IS_x0020_751085.html)).
- **My Event release date:** announced as a new feature on 2024-01-16 ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)); a later release says it shipped in December 2023 ([2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html)).

### Other

- Product sequence: cloud RPA Anybot (pre-registration 2018-10, as 株式会社ピケ) → the original Anyflow iPaaS for businesses (β 2019-10) → Anyflow Embed for SaaS vendors (GA 2023-07-13) → Anyflow Automation, AI/RAG data sync (2026-05) and code solutions (β 2026-07). The CTO states Embed was built from scratch and launched about four months after planning began ([Green](https://www.green-japan.com/company/10894/pr)).
- Patent wording changed from "特許出願中" ([2022-12-08](https://prtimes.jp/main/html/rd/p/000000017.000034258.html), [2024-01-16](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)) to "特許取得済" on the [Embed page](https://anyflow.jp/products/embed), consistent with the JP7645548B2 grant listed by Google Patents.
- Asuene's group-company list in its 2026-06-26 release calls Anyflow an "AIデータ連携プラットフォーム" ([Asuene](https://prtimes.jp/main/html/rd/p/000000711.000058538.html)).
- The status page's incident feed lists 20 incidents from 2024-01-18 to 2026-08-25, seven of them about scheduled triggers not firing ([status page](https://anyflow-embed.statuspage.io/); accessed 2026-10-11).
- The full Embed documentation is public on GitBook, including an `llms-full.txt` export; product pages link to it ("ドキュメントへ").
- PR TIMES lists 38 Anyflow releases as of 2026-10-11; there were none between 2025-06-11 and 2026-05-28 ([PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/34258)).
- Not accessible on 2026-10-11: a CodeZine article (bot check), the TokyoDev profile URL (HTTP 403), the TechCrunch Japan 2019 article (certificate error) and the Forbes Asia profile text.

---

## Resources

**Official**

- [Homepage](https://anyflow.jp/) · [company page](https://anyflow.jp/about) · [sitemap](https://anyflow.jp/sitemap.xml)
- [Anyflow Embed](https://anyflow.jp/products/embed) · [Anyflow Automation](https://anyflow.jp/products/automation) · [connectors](https://anyflow.jp/connectors) · [case studies](https://anyflow.jp/case)
- [Terms of use](https://anyflow.jp/terms) · [privacy policy](https://anyflow.jp/privacy)
- [Embed documentation](https://docs-embed.anyflow.jp/) · [docs sitemap](https://docs-embed.anyflow.jp/sitemap-pages.xml) · [release notes](https://docs-embed.anyflow.jp/release-notes/recent) · [code solutions](https://docs-embed.anyflow.jp/release-notes/code-solution) · [SDK](https://docs-embed.anyflow.jp/anyflow-sdk/docs) · [SDK changelog](https://docs-embed.anyflow.jp/anyflow-sdk/docs/changelog) · [JWT](https://docs-embed.anyflow.jp/release/embed/generate-jwt) · [Vender Server API](https://docs-embed.anyflow.jp/anyflow-api/vender-server-api) · [deployment environments](https://docs-embed.anyflow.jp/release/deploy-environment) · [wizard hosting](https://docs-embed.anyflow.jp/release/wizard-hosting) · [Python action](https://docs-embed.anyflow.jp/solution-editor/actions/data-transform/python) · [limits](https://docs-embed.anyflow.jp/ops/step-execution-limit)
- [Security policy](https://docs-embed.anyflow.jp/policy/security-policy) · [service level](https://docs-embed.anyflow.jp/policy/service-level) · [incident response](https://docs-embed.anyflow.jp/policy/incident-response) · [status page](https://anyflow-embed.statuspage.io/)
- [Careers page (Notion)](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671) · [HERP job list](https://herp.careers/v1/anyflow) — [Software Engineer](https://herp.careers/v1/anyflow/NC0_ouH2OBRX), [SRE](https://herp.careers/v1/anyflow/5sHcw3MfypEy), [Product Manager](https://herp.careers/v1/anyflow/qs53UJS4TYOX), [workflow builder](https://herp.careers/v1/anyflow/Jht3MH0DI3if), [PM lead](https://herp.careers/v1/anyflow/T7Zo5Ic0m7_7), [CRE](https://herp.careers/v1/anyflow/IZa74EMW4xS1), [TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO), [Enterprise BizDev](https://herp.careers/v1/anyflow/oMisMJmQvdea)
- [GitHub organisation](https://github.com/anyflowinc) · [GitHub API](https://api.github.com/orgs/anyflowinc) · [npm](https://www.npmjs.com/package/@anyflowinc/embed-sdk) · [JSR scope](https://jsr.io/@anyflowinc) · [note (JA)](https://note.com/anyflow) · [Speaker Deck](https://speakerdeck.com/anyflow) · [company deck, 2024-02-13](https://speakerdeck.com/anyflow/we-are-hiring)

**Press releases (anyflow.jp, JA — newest first)**

- [Code solutions β — 2026-07-28](https://anyflow.jp/news/o3pigXgy)
- [SaaS buyer survey — 2026-07-14](https://anyflow.jp/news/3RLk2a_Q)
- [Webinar with Cloud Circus — 2026-06-29](https://anyflow.jp/news/_8Tdn3Ok)
- [AI agent / RAG data sync — 2026-05-28](https://anyflow.jp/news/iGZsEBie)
- [End of Smaregi integration apps — 2026-03-31](https://anyflow.jp/news/smaregi-integration-end)
- [Share No.1 — 2025-06-11](https://anyflow.jp/news/2025-share-no1)
- [SmartHR case study — 2025-05-23](https://anyflow.jp/news/case-smarthr)
- [Code action — 2025-04-17](https://anyflow.jp/news/code-action)
- [Acquisition by Asuene — 2024-12-10](https://anyflow.jp/news/asuene-groupin)
- [Embed first anniversary — 2024-07-16](https://anyflow.jp/news/anyflow-embed-1st-anniv)
- [Money Forward Cloud — 2024-03-12](https://anyflow.jp/news/moneyforward-cloud)
- [NP掛け払い — 2023-11-29](https://anyflow.jp/news/anyflow-embed-netprotections)
- [SmartHR Plus app — 2023-08-29](https://anyflow.jp/news/smarthr-plus)
- [Embed GA — 2023-07-13](https://anyflow.jp/news/anyflow-embed)
- [Forbes 30 Under 30 Asia — 2022-05-26](https://anyflow.jp/news/forbes-30-under-30-asia-2022)
- [FUJITSU ACCELERATOR award — 2020-02-10](https://anyflow.jp/news/fujitsu-accelerator)
- [Pre-Series A — 2020-01-08](https://anyflow.jp/news/pre-seriesA-fundraise)
- [Seed round — 2019-09-24](https://anyflow.jp/news/seed-finance)
- [Rename to Anyflow — 2019-01-17](https://anyflow.jp/news/rename-company-name)

**PR TIMES (JA)**

- [Company release list](https://prtimes.jp/main/html/searchrlp/company_id/34258)
- [ASUENE adopts Embed — 2025-02-19](https://prtimes.jp/main/html/rd/p/000000032.000034258.html) · [Error notifications to six tools — 2024-12-26](https://prtimes.jp/main/html/rd/p/000000031.000034258.html) · [Request & Response — 2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html) · [My Event — 2024-01-16](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)
- [Yayoi alliance — 2023-07-19](https://prtimes.jp/main/html/rd/p/000000019.000034258.html) · [Smaregi capital alliance — 2022-12-08](https://prtimes.jp/main/html/rd/p/000000017.000034258.html) · [IT導入補助金 — 2020-08-06](https://prtimes.jp/main/html/rd/p/000000014.000034258.html)
- [EY Innovative Startup 2020 — 2020-02-28](https://prtimes.jp/main/html/rd/p/000000007.000034258.html) · [Pre-Series A — 2020-01-08](https://prtimes.jp/main/html/rd/p/000000005.000034258.html) · [B Dash Camp — 2019-11-05](https://prtimes.jp/main/html/rd/p/000000004.000034258.html) · [Seed — 2019-09-24](https://prtimes.jp/main/html/rd/p/000000003.000034258.html) · [Anybot, as 株式会社ピケ — 2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html)
- Asuene: [100% acquisition — 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html) · [integrations via Anyflow — 2025-02-19](https://prtimes.jp/main/html/rd/p/000000461.000058538.html) · [head office move — 2026-05-07](https://prtimes.jp/main/html/rd/p/000000681.000058538.html) · [group company list — 2026-06-26](https://prtimes.jp/main/html/rd/p/000000711.000058538.html)

**Registers**

- [国税庁 法人番号公表サイト — 1011001109588 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)
- [ISMS registry — IS 751085 (JA)](https://isms.jp/lst/ind/CR_IS_x0020_751085.html)
- [Google Patents — JP7645548B2](https://patents.google.com/patent/JP7645548B2/ja) · [JP2024004078A](https://patents.google.com/patent/JP2024004078A/ja)

**Third-party coverage and profiles**

- [BRIDGE — seed round, 2019-09-24 (JA)](https://thebridge.jp/2019/09/anyflow-seed-round-funding) · [pre-Series A, 2020-01-08 (JA)](https://thebridge.jp/2020/01/anyflow-pre-series-a-round-funding) · [Embed GA, 2023-07-13 (JA)](https://thebridge.jp/2023/07/anyflow-embed-official-launch) · [acquisition, 2024-12-12 (JA)](https://thebridge.jp/2024/12/anyflow-was-acqired-by-asuene-strengthening-data-collaboration-towards-achieving-carbon-neutrality)
- [Forbes JAPAN — pre-Series A, 2020-01-08 (JA)](https://forbesjapan.com/articles/detail/31650)
- [Founder — CEO interview, 2019-06-17 (JA)](https://found-er.com/interview/1442/)
- [Green — member profiles incl. CTO (JA)](https://www.green-japan.com/company/10894/pr) · [Embed business lead interview (JA)](https://www.green-japan.com/company/10894/interview)
- [Wantedly — Tech Lead posting, 2024-05-11, closed (JA)](https://www.wantedly.com/projects/1698588)
- [HERP — company profile (JA)](https://herp.careers/careers/companies/anyflow) · [INITIAL (JA)](https://initial.inc/companies/A-17184)
