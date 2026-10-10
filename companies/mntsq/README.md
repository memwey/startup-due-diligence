# MNTSQ

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

MNTSQ (MNTSQ株式会社, read モンテスキュー; English name MNTSQ, Ltd.) is a Tokyo company established on 2018-11-14. Its founder and CEO, Ryuhei Itaya (板谷 隆平), is a lawyer at the law firm Nagashima Ohno & Tsunematsu (長島・大野・常松法律事務所, "NO&T"); the company names AI engineer Takahiro Anno (安野 貴博) and Yotaro Katayama (堅山 耀太郎) as co-founders. It sells **MNTSQ CLM**, a contract lifecycle management system for large enterprises: legal-matter intake and contract review (案件管理), a contract ledger (契約管理), a clause-level contract database, and LLM-based features sold as **MNTSQ AI契約アシスタント** and **MNTSQ AI Agent**. NO&T invested ¥800M (8億円) in 2019 and supervises the templates and playbooks shipped in the product. Two more large law firms, Nishimura & Asahi (2024) and Mori Hamada & Matsumoto (2025), later took stakes as well.

- Scale as stated by the company: used by 41 of Japan's top 100 companies by revenue ([2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html)), and by 42 as of 2026-06-12 ([2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)). The company also reports more than 2,000 adopting companies, counting group companies, as of 2026-05 ([2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html)).
- Funding: the company has not published a cumulative total. Disclosed rounds are ¥800M from NO&T ([2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)), a ¥1.0B シリーズB from ALL STAR SAAS FUND ([2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)), and about ¥1.0B in 2024 from three corporate VCs plus a bond and a loan ([2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)). Nishimura & Asahi and Mori Hamada & Matsumoto invested undisclosed amounts.
- Team: 120 employees as of 2026-07-31. The development division (開発本部) has about 50 people in four teams as of 2026-08 ([Software Engineer (Backend) posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11).
- Engineering: a Ruby on Rails core (Ruby since founding), Python services (FastAPI, Celery) and a Vue.js/TypeScript frontend. Infrastructure is AWS (ECS/Fargate, Aurora MySQL, SQS, OpenSearch), with Google Cloud (Vertex AI, Cloud Vision API) called from AWS workloads ([postings](https://hrmos.co/pages/mntsq/jobs/10055), [tech blog, 2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103)). All postings reviewed are in Japanese and do not state an English requirement. Engineers work hybrid, with at least 5 office days per month.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | MNTSQ (モンテスキュー); main product "MNTSQ CLM" | [about](https://mntsq.co.jp/about); accessed 2026-10-11 |
| Legal name | MNTSQ株式会社 / MNTSQ, Ltd.; registry spelling ＭＮＴＳＱ株式会社, furigana モンテスキュー | [NTA corporate number register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) (information as of 2026-10-11) |
| Corporate number | 7010001196433; number designated 2018-11-27 | [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) |
| Founded | 設立日 2018-11-14 | Company boilerplate, e.g. [2026-05-19](https://prtimes.jp/main/html/rd/p/000000094.000050130.html) |
| HQ | 〒104-6004 東京都中央区晴海1-8-10 晴海アイランド トリトンスクエア オフィスタワーX棟 4階. Registered address changed to 晴海１丁目８番１０号 effective 2025-10-10 | [about](https://mntsq.co.jp/about), [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) |
| Former registered addresses | 千代田区神田司町2-21-3 (until 2019-12-06) → 千代田区岩本町3-5-2 (until 2020-08-24) → 中央区日本橋堀留町2-9-8 (until 2022-08-12) → 中央区日本橋堀留町1-9-8 (until 2025-10-10) | [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) |
| Representative | 代表取締役 板谷 隆平 (Founder / CEO) | [about](https://mntsq.co.jp/about) |
| Capital | ¥100M (資本金 1億円) | [HRMOS posting, company info](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11 |
| Headcount | 120 (従業員数 120名, as of end of July 2026) | [HRMOS posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11 |
| Headcount history | 4 at founding in 2018; 50 as of 2022-07; "100名近く" (2025-10); "社員数100名強" (2026-06) | [2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html), [2025-10-09](https://prtimes.jp/main/html/rd/p/000000071.000050130.html), [2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html) |
| Staff mix | Product 41%, business 46%, corporate 13%, directors included (as of 2026-09) | [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) (marked 2026-09-01 更新) |
| Working language | No company-wide or engineering language policy found. Every posting and careers page reviewed is in Japanese; none mentions English | [HRMOS job board](https://hrmos.co/pages/mntsq/jobs), [careers site](https://careers.mntsq.co.jp/); accessed 2026-10-11 |
| Customers | 41 of Japan's top 100 companies by revenue (2026-05); 42 (as of 2026-06-12); 2,000+ adopting companies including group companies (as of 2026-05) | See `Reported scale over time` |
| Total raised | Not published by the company | See `Funding` |
| Investors named by the company | NO&T, PKSHA Technology, ALL STAR SAAS FUND, かんぽNEXTパートナーズ, 三菱UFJイノベーション・パートナーズ, 日揮みらい投資事業有限責任組合, 西村あさひ法律事務所・外国法共同事業, 森・濱田松本法律事務所外国法共同事業 (bond: あおぞらHYBRID3号投資事業有限責任組合; loan: 商工組合中央金庫) | Releases in `Funding` |
| Security certification | ISO/IEC 27001:2022 and JIS Q 27001:2023, certificate IS 798405, issued by BSI Japan. Scope: 契約業務に関する自社SaaSの研究・開発・運用・保守. Initial registration 2024-01-22 | [Notice, 2024-03-22](https://mntsq.co.jp/news/information/202403-isms) |

**Programs and awards.** The company was selected in Nikkei's "NEXTユニコーン調査2024" ([notice, 2025-01-17](https://mntsq.co.jp/news/information/nextunicorn2024)). It was adopted into the "かんぽ生命 - アフラック - 日本郵便 Acceleration Program 2025" ([2025-08-15](https://prtimes.jp/main/html/rd/p/000000066.000050130.html)). MNTSQ CLM received ITreview Grid Award "Leader" ratings, the fourth consecutive one for 2026 Summer ([2026-07-15](https://prtimes.jp/main/html/rd/p/000000106.000050130.html)). The company won the 最優秀賞 in the 「はたらくを楽しく」 category of HR's SDGsアワード2026 and was also named 準グランプリ ([2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)).

### Law-firm relationships as described by the company

- **NO&T.** The company says it was "創業当初から長島・大野・常松法律事務所の全面的なサポートを受けて2018年11月に設立" ([2025-10-09](https://prtimes.jp/main/html/rd/p/000000071.000050130.html)). It ran a private pilot of its NLP software inside NO&T from 2019-02, and the product was used in NO&T's legal due diligence work. On 2019-10-21 it announced a capital and business alliance with NO&T and PKSHA Technology, including ¥800M from NO&T ([2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)). Two NO&T partners joined the board as outside officers ([2019-11-13](https://prtimes.jp/main/html/rd/p/000000002.000050130.html)). NO&T supervises the contract templates ("MNTSQ雛型") and the playbook (審査基準集) supplied as standard with MNTSQ AI契約アシスタント ([2026-01-16](https://prtimes.jp/main/html/rd/p/000000081.000050130.html), [AI契約アシスタント page](https://mntsq.co.jp/product/aicontract-assistant)). The two co-published the book "LegalTech" ([2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)).
- **Nishimura & Asahi (西村あさひ).** A strategic collaboration that includes an investment in MNTSQ; the firm also began using MNTSQ CLM ([2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html)).
- **Mori Hamada & Matsumoto (森・濱田松本).** A capital and business alliance that includes an investment. The parties will consider offering Mori Hamada legal content on MNTSQ's platform, combined with MNTSQ's AI, and will consider Mori Hamada using MNTSQ technology ([2025-05-07](https://prtimes.jp/main/html/rd/p/000000063.000050130.html)).
- The company summarises this as three of Japan's four largest law firms (四大法律事務所) participating in its business ([2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)).

### Market and regulatory context as stated by the company

- When it launched MNTSQ for Enterprise in 2020, the company cited remote work during COVID-19. It also cited new questions about consolidating e-signed contracts across multiple services and complying with the 電子帳簿保存法 (Electronic Books Maintenance Act) ([2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)).
- In the Series B release, the CEO wrote that LLM progress, together with the fact that "弁護士法に関する社会的検討に一定の目処がついた", led the company to plan delivering AI contract review directly to more customers ([2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)).
- Current engineering postings describe the contract domain as late to digitalise, with large companies running their own on-premise systems. They also state that the number of bar-exam candidates is about half of what it was ten years ago ([posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11).

---

## Product

### Product line-up and feature areas

The site groups the product into five modules ([product index](https://mntsq.co.jp/product), [homepage](https://mntsq.co.jp/); accessed 2026-10-11):

| Module | Description as given by the company | Listed features | Page |
|---|---|---|---|
| MNTSQ 案件管理 (matter management) | Single intake for legal consultations and contract review, with review status made visible and knowledge accumulated automatically | Matter search and lists, assignee workload view, status management, request forms, email notifications, attachment management, permission control, suggested reference knowledge; "案件フロー" workflow control added [2025-06-30](https://prtimes.jp/main/html/rd/p/000000064.000050130.html) | [page](https://mntsq.co.jp/product/casemanage) |
| MNTSQ 契約管理 (contract management) | AI fills in management fields of departmental contract ledgers; notifications warn of deadlines and renewals | Upload, ledger and list views, custom fields, automatic field entry, alerts, linking related contracts, search, export, permission control | [page](https://mntsq.co.jp/product/contractmanage) |
| データベース (database) | Collects contract-related data automatically; contract-specialised AI analyses and organises it | PDF OCR, clause decomposition (条項分解), metadata management, template management, knowledge browsing, permission control | [page](https://mntsq.co.jp/product/databasemanage) |
| MNTSQ AI契約アシスタント | Rates the risk of a matter; business units handle low-risk matters, and high-risk ones are escalated to legal with the request drafted automatically | Contract review, legal consultation, playbook, automatic matter creation, AI review, AI consultation. NO&T-supervised playbook included as standard | [page](https://mntsq.co.jp/product/aicontract-assistant) |
| MNTSQ AI Agent | A legal-specialised AI agent built on the customer's contract knowledge, working across the other modules | Playbook, past-matter search, chat consultation, display of the AI's reasoning, preliminary legal analysis. Prompts written by lawyers and in-house legal practitioners | [page](https://mntsq.co.jp/product/mntsq-ai-agent) |

Other surfaces listed on the homepage:

- **AI contract review as a Word plug-in.** It compares a counterparty draft with the customer's template and surfaces similar past contracts. It was released 2024-04-01 ([2024-02-28](https://prtimes.jp/main/html/rd/p/000000049.000050130.html)). On 2026-09-07 MNTSQ AI Agent was added inside Word, where it:
  - proposes a review policy before review starts;
  - writes tracked-change redlines and comments;
  - checks the customer's own playbook first and falls back to the law-firm-supervised playbook;
  - flags formal defects such as inconsistent clause numbering and leftover placeholders ([2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html)).
- **Templates.** "MNTSQ雛型" are NO&T-supervised templates with commentary. The range was doubled on [2026-01-16](https://prtimes.jp/main/html/rd/p/000000081.000050130.html), and 13 templates, including AI-service terms of use, were added on [2026-06-18](https://prtimes.jp/main/html/rd/p/000000101.000050130.html).
- **Languages and currencies.**
  - English UI: [2023-10-02](https://prtimes.jp/main/html/rd/p/000000047.000050130.html).
  - All ISO 4217 currencies in contract management: [2025-12-16](https://prtimes.jp/main/html/rd/p/000000078.000050130.html).
  - AI analysis (element decomposition) of contracts in languages beyond Japanese and English, such as Chinese, Thai and German: [2026-01-21](https://prtimes.jp/main/html/rd/p/000000080.000050130.html).
- **Security features.** Data on AWS is stored encrypted, and SSO and IP-address restriction are included at no extra charge ([homepage](https://mntsq.co.jp/); accessed 2026-10-11).

### Integrations and API

- **E-signature.** DocuSign and CloudSign signed-contract import has been available since 2021 ([CloudSign, 2021-04-14](https://prtimes.jp/main/html/rd/p/000000009.000050130.html)). It was extended on 2026-07-23 to cover the whole signing flow: creating e-signature drafts from a matter, tracking sending history, and automatically registering signed documents to a ledger ([2026-07-23](https://prtimes.jp/main/html/rd/p/000000107.000050130.html)).
- **Chat.** Slack integration covers comment notifications, threaded replies written back to the matter timeline, and matter creation ([2026-08-06](https://prtimes.jp/main/html/rd/p/000000110.000050130.html)). Microsoft Teams covers notifications and replies, including from the mobile app ([2026-09-01](https://prtimes.jp/main/html/rd/p/000000117.000050130.html)).
- **Email and storage.**
  - Email correspondence is ingested into the database, with full-text search of attachments.
  - Files are imported from SharePoint, Google Drive and Box.
  - User and permission changes can be applied by importing a settings file ([homepage](https://mntsq.co.jp/); accessed 2026-10-11).
- **Public API.** The 「案件管理公開API」 provides file upload and download, retrieval of matter details, and creation and update of matters ([2026-04-07](https://prtimes.jp/main/html/rd/p/000000089.000050130.html)). Date and time fields were standardised to ISO 8601 with time zone on [2026-06-16](https://prtimes.jp/main/html/rd/p/000000100.000050130.html). No public API reference was found.
- **Counterparty master.** Counterparty records can be created from the National Tax Agency corporate master. Name changes are reflected automatically, and old names are kept as aliases ([2026-05-19](https://prtimes.jp/main/html/rd/p/000000094.000050130.html)).

### Commercialization

Pricing is an initial fee (initial setup and implementation support) plus a monthly fee (service use and support), quoted according to the customer's issues and scale. No public price list was found; a plan guide is offered as a download behind a form ([homepage](https://mntsq.co.jp/); accessed 2026-10-11). Each customer is assigned a consultant from implementation onward, including support for migrating existing data, and the company runs user conferences ("MNTSQ Meeting"). Engineering postings describe the business as "受託ゼロ、個社カスタマイズゼロ" (no contract development, no per-customer customisation) ([posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11).

### Product history

| Date | Event | Source |
|---|---|---|
| 2019-02 | Private pilot at NO&T of NLP software for legal due diligence, after what the company calls two years of non-public preparation | [2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html) |
| 2020-06-10 | Proof-of-concept trials for a corporate product with Komatsu, Fukuoka Bank and others | [2020-06-10](https://prtimes.jp/main/html/rd/p/000000003.000050130.html) |
| 2020-12-07 | "MNTSQ for Enterprise" contract database officially released; the law-firm product was named "MNTSQ for M&A" | [2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html) |
| 2022-01-26 | 案件管理 announced for autumn 2022; the line-up was database, contract management and automated drafting (自動ドラフティング) | [2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html) |
| 2022-07-19 | Product referred to as "MNTSQ CLM"; general sales stated to have begun in 2020-11 | [2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html) |
| 2023-06-05 | New development team for generative AI/LLM established | [2023-06-05](https://prtimes.jp/main/html/rd/p/000000035.000050130.html) |
| 2024-04-01 | MNTSQ AI契約レビュー released | [2024-02-28](https://prtimes.jp/main/html/rd/p/000000049.000050130.html) |
| 2025-10-01 | MNTSQ AI契約アシスタント released, the first service carrying MNTSQ AI Agent. Orders opened 2025-04-01 after a PoC of about a year with Mitsubishi Electric | [2025-03-19](https://prtimes.jp/main/html/rd/p/000000061.000050130.html), [2026-03-05](https://prtimes.jp/main/html/rd/p/000000084.000050130.html) |
| 2026-03-05 | AI Agent added to 案件管理: similar-matter comparison, preliminary legal analysis, and draft emails asking the requesting department for missing information | [2026-03-05](https://prtimes.jp/main/html/rd/p/000000084.000050130.html) |
| 2026-09-07 | AI Agent added to contract review in Word (third rollout phase) | [2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html) |

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2020-12-07 | Komatsu's comment in the release: a five-month PoC indicated about 40% of contract-review work could be made more efficient | [2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html) |
| 2022-07-19 | Members: 50 (from 4 at founding) | [2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html) |
| 2023-09-19 | Used by "売上高1兆円以上の国内企業の約5社に1社" (MNTSQ's own research) | [2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html) |
| 2025-10-08 | After Itochu's adoption: all of the top 5, 7 of the top 10 and 14 of the top 20 in Nikkei's 2024 「法務力が高い企業」 ranking are users | [2025-10-08](https://prtimes.jp/main/html/rd/p/000000069.000050130.html) |
| 2025-12-24 | 9 of the top 10 in Nikkei's 2025 ranking, up from 6 a year earlier | [2025-12-24](https://prtimes.jp/main/html/rd/p/000000079.000050130.html) |
| 2026-05-12 | 41 of Japan's top 100 companies by revenue | [2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html) |
| 2026-06-29 | 42 of the top 100 (Nikkei, as of 2026-06-12) | [2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html) |
| 2026-07-07 | 2,000+ adopting companies including group companies, and 8 of the 10 listed companies with the largest domestic sales (both as of 2026-05) | [2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html) |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html) | 小松製作所, 大阪ガス | Launch customers of MNTSQ for Enterprise |
| [2021-06-30](https://prtimes.jp/main/html/rd/p/000000012.000050130.html) | 三菱商事 | Contract database integrated with the legal department's existing matter and document management system |
| [2021-09-30](https://prtimes.jp/main/html/rd/p/000000013.000050130.html) | Zuva (Kira Systems spin-off) | Integration with Zuva's DocAI platform for Japanese–English contract analysis |
| [2021-11-01](https://prtimes.jp/main/html/rd/p/000000014.000050130.html) | 三井住友銀行 | Automated drafting configured for syndicated loan agreements; the release says the contact came through MNTSQ's service to NO&T |
| [2022-01-26](https://prtimes.jp/main/html/rd/p/000000018.000050130.html) | 三菱電機 | Adopted the full service line-up, including automated drafting |
| [2023-08-09](https://prtimes.jp/main/html/rd/p/000000040.000050130.html) | 日立製作所 | Adopted MNTSQ CLM for contract knowledge management |
| [2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html) | 三菱UFJ銀行 | Named as an existing MNTSQ CLM user in its group CVC's investor comment |
| [2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html) | 西村あさひ | Law firm became a user and an investor |
| [2025-10-08](https://prtimes.jp/main/html/rd/p/000000069.000050130.html) | 伊藤忠商事 | Adopted MNTSQ CLM |
| [2026-06-04](https://prtimes.jp/main/html/rd/p/000000098.000050130.html) | 東京エレクトロン | Replaced an in-house contract management system it had run for about 20 years |

The [clients page](https://mntsq.co.jp/clients) and the [case study index](https://mntsq.co.jp/case) list further users (accessed 2026-10-11). Announced users also include law firm 稲葉総合法律事務所 ([2021-12-22](https://prtimes.jp/main/html/rd/p/000000015.000050130.html)).

### Stated plans

- Series B use of funds: accelerated investment in product development, including LLM use, and delivery of AI contract review ([2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)).
- 2024 round: joint solution development with the investing companies would be considered within the capital and business alliances ([2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)).
- Stated aspiration for MNTSQ AI Agent: an agent that acts autonomously "契約交渉まで行ってくれる" (all the way to negotiating contracts) ([2025-09-19 release on site](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025), [2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html)).
- On the COO appointment: expand adoption and share in the Japanese enterprise segment, described as the hub of a future contract network and platform ([2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html)).
- A current HR posting gives its background as "IPO準備に向けた体制強化" and states that organisational preparation toward an IPO is under way ([制度企画・労務 posting](https://hrmos.co/pages/mntsq/jobs/30017), page metadata datePosted 2026-09-07; accessed 2026-10-11).

---

## Founder

**板谷 隆平 (Ryuhei Itaya)** — Founder / CEO and 代表取締役. The about page still lists him as a lawyer at NO&T ([about](https://mntsq.co.jp/about)). Engineering postings state that he also serves as CPO ([posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11).

- 2013: graduated from the University of Tokyo Faculty of Law, having passed the 司法試験予備試験 (preliminary bar examination) while a student ([column, 2025-03-03](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)).
- 2014: registered as a lawyer and joined NO&T, advising on M&A and on AI/IT technology matters. He founded MNTSQ while working at the firm ([about](https://mntsq.co.jp/about)).
- Director (理事) of 一般社団法人AIリーガルテック協会, as stated in a [2025-07-09](https://prtimes.jp/main/html/rd/p/000000065.000050130.html) release.
- 2025-12: ranked 10th in the "人工知能（AI）ガバナンス" category of Nikkei's lawyer ranking ([2025-12-24](https://prtimes.jp/main/html/rd/p/000000079.000050130.html)).
- 2026-05: received the "Legal Intrapreneur" award at the Financial Times "Asia-Pacific Innovative Lawyers Awards 2026" ([2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)).

**安野 貴博 (Takahiro Anno)** — a company column states that Itaya co-founded MNTSQ with Anno. It describes Anno as a natural-language-processing specialist who trained the first models on about 100 sample unfair clauses that Itaya wrote ([column, 2025-03-03](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)). A 2019 company post on Wantedly by Katayama describes Anno as also a director (取締役) of MNTSQ ([Wantedly, 2019-10-29](https://www.wantedly.com/companies/mntsq/post_articles/192635)). He is not listed in the management section of the current [about page](https://mntsq.co.jp/about).

**堅山 耀太郎 (Yotaro Katayama)** — listed as "Co-Founder / 取締役" and as CFO of Preferred Networks on the [about page](https://mntsq.co.jp/about). His Preferred Networks biography gives this career ([PFN leadership, JA](https://www.preferred.jp/ja/company/leadership); accessed 2026-10-11):

- 2016: master's degree from the University of Tokyo Graduate School of Engineering, then Goldman Sachs Japan.
- Co-founder and director of BEDORE (now PKSHA Workplace).
- 2018: joined MNTSQ's board as a co-founder, responsible for engineering and finance.
- 2023: doctorate in engineering from the University of Tokyo, earned while at MNTSQ.
- 2024-05: CFO of Preferred Networks.

### Selected leadership

| Name | Role as written | Stated background | Source |
|---|---|---|---|
| 深井 亮 (Ryo Fukai) | COO, from 2026-06-01 | 共立; Sansan from 2019, where he joined the "Bill One" launch in 2020 as its first salesperson and later headed sales and product planning (PMM) | [2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html) |
| 高田 直満 | VP of Engineering | — | [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) (2026-09-01 更新) |
| 粟谷 翔 | 社外取締役 (outside director) | NO&T partner | [about](https://mntsq.co.jp/about) |
| 藤原 総一郎 | 監査役 (corporate auditor) | NO&T managing partner (from 2024); MNTSQ outside director 2019–2024, auditor since 2024 | [about](https://mntsq.co.jp/about), [column](https://mntsq.co.jp/column/interview/noandt_and_mntsq/) |
| 内海 慶 | Algorithm engineer, from 2026-05 | NLP research at Yahoo Japan, Denso IT Laboratory and SB Intuitions; 優秀賞 at NLP2025 | [2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html) |

The company's organisation chart has four units under the CEO: 事業本部, 開発本部, 人事本部 and 経営管理部. 開発本部 contains three parts ([Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)):

- 開発部: CLM application, CLM platform, legal-agent, business-division and enabling teams.
- プラットフォーム部: SRE and QA teams and a security office.
- リーガルエキスパートチーム: legal new-business planning and legal consultants.

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Before 2019-10-21 (date not disclosed) | 資本技術提携 (capital and technology alliance) | not disclosed | PKSHA Technology | — | [2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html) |
| 2019-10-21 | 資本業務提携 (capital and business alliance) | ¥800M (8億円) from NO&T | 長島・大野・常松法律事務所 | — | [2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html) |
| 2023-09-19 | シリーズB | ¥1.0B (10億円) | ALL STAR SAAS FUND (new) | not stated | [2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html) |
| 2024-06-03 | No round name; third-party allotment, bond issue and loan | approx. ¥1.0B total (総額約10億円) | Equity: かんぽNEXTパートナーズ, 三菱UFJイノベーション・パートナーズ, 日揮みらい投資事業有限責任組合. Bond: あおぞらHYBRID3号投資事業有限責任組合 (managed by あおぞら企業投資). Loan: 商工組合中央金庫 | not stated | [2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html) |
| 2024-06-04 | 出資を含む戦略的協業 | not disclosed | 西村あさひ法律事務所・外国法共同事業 | not stated | [2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html) |
| 2025-05-07 | 資本業務提携 (including investment) | not disclosed | 森・濱田松本法律事務所外国法共同事業 | not stated | [2025-05-07](https://prtimes.jp/main/html/rd/p/000000063.000050130.html) |

- The 2019 release states PKSHA's investment had already been made before the NO&T round, without an amount ([2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)). A follow-up release describes the alliance as raising "約8億円" ([2019-11-13](https://prtimes.jp/main/html/rd/p/000000002.000050130.html)).
- In the Series B release, the CEO states that in this round the company decided to accept investment from a new VC in order to keep making growth investments ("新規のVCによる出資を受け入れることといたしました") ([2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)). No release labelled シリーズA was found.
- The 2024 release states the round followed demand for MNTSQ AI契約レビュー, launched that April. Investor comments from MUFG's and JGC's investment arms state that MUFG Bank and the JGC group were already MNTSQ CLM users ([2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)). BRIDGE described the round only as "直近のラウンド" ([BRIDGE, 2024-06-04](https://thebridge.jp/2024/06/mntsq-jpy1b-round-funding)).
- The Series B release was published the same day as the announcement that MNTSQ AI契約レビュー was in development ([2023-09-19](https://prtimes.jp/main/html/rd/p/000000046.000050130.html)).

---

## Engineering

### Technology stack and platforms

**Confirmed by the company's technical writing** (tech blog and releases):

- **Ruby / Ruby on Rails.** The company states that Ruby has been the main language of its web service since founding in 2018 ([2023-03-06](https://prtimes.jp/main/html/rd/p/000000031.000050130.html)). A 2026 post says the core of the service is Ruby on Rails ([tech blog, 2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614)). The company was a Ruby Sponsor of RubyKaigi 2023.
- **Asynchronous jobs.** Rails background jobs moved from Resque on Redis to Amazon SQS, with priority-tiered and feature-specific queues and per-queue autoscaling ([2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614)). Python workers use Celery on SQS ([2026-06-29](https://tech.mntsq.co.jp/entry/2026/06/29/090000)).
- **Search.** The service ran self-hosted Elasticsearch 7.x on EC2 until a no-downtime migration to Amazon OpenSearch Service, which ran from 2025-10 to 2026-06. The project consolidated per-tenant-group clusters into a single VPC domain with fine-grained access control, managed with Terraform ([2026-08-26](https://tech.mntsq.co.jp/entry/2026/08/26/180213)).
- **AWS and Google Cloud.** Applications run on Amazon ECS. Three backend services call Google Cloud's Vertex AI or Cloud Vision API, now authenticated through Workload Identity Federation instead of service-account keys. Deployment runs through GitHub Actions ([2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103)).
- **LLMs.** A 2024 talk compared GPT-4o, Claude 3.5 Sonnet and Gemini 1.5 Pro for contract analysis. It weighed accuracy, context window, output speed, price and availability in a Japan region (the presenter's own assessment) ([LT deck, 2024-07-11](https://speakerdeck.com/mntsq/ltzi-liao-mntsqnoqi-yue-shu-jie-xi-wo-llmnizhi-kihuan-eruhua)).
- **Other tools.** Other tech-blog posts cover Datadog, Redash, AWS Security Hub, Playwright and ECS Exec ([archive](https://tech.mntsq.co.jp/archive); accessed 2026-10-11).

**Listed in current job postings** (hiring documents; [Software Engineer (Backend)](https://hrmos.co/pages/mntsq/jobs/10055), [Tech Lead](https://hrmos.co/pages/mntsq/jobs/10034), and the same list in the [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)):

| Category | Items |
|---|---|
| Languages | Ruby, Python, JavaScript, TypeScript |
| Web frameworks | Ruby on Rails, FastAPI, Vue.js |
| CSS / UI | Element Plus, Tailwind CSS, PostCSS, Storybook |
| Platforms | Amazon Web Services, Google Cloud |
| Database | Aurora MySQL |
| Search | Elasticsearch, OpenSearch |
| Monitoring | CloudWatch, Datadog |
| Containers | Docker, Docker Compose, ECS/Fargate |
| Configuration management | Terraform, Itamae |
| AI engineer posting | Python, TypeScript, FastAPI, MCP, PyTorch, MySQL, OpenSearch, GitHub, Docker ([AI (NLP) Engineer](https://hrmos.co/pages/mntsq/jobs/10064)) |

The postings state that development assumes AI tools such as Claude and Devin. Employees receive a Claude Enterprise account as a listed benefit ([posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11).

### Systems

| System | What it does | Source |
|---|---|---|
| Contract analysis | Contract-specialised OCR, clause-level decomposition and machine-learning extraction of fields such as counterparty, signing date, term and amount. A backend "解析基盤" service performs clause decomposition and OCR. Multi-language analysis was added in 2026 | [2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html), [tech blog 2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103), [2026-01-21](https://prtimes.jp/main/html/rd/p/000000080.000050130.html) |
| AI agent backend | Two services that answer contract questions, judge risk and search knowledge for MNTSQ AI Agent | [2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103) |
| Offline evaluation | Internal evaluation of AI output quality using LLM-as-a-Judge | [2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103) |
| Knowledge-graph retrieval (prototype) | For contract review: chunks contracts, matter comments and playbook items; extracts entities and relations; searches with both keyword-level and situation-level queries to produce grounded answers | [2026-09-09](https://tech.mntsq.co.jp/entry/2026/09/09/083234) |
| Multi-tenant search | One OpenSearch domain holding all tenants' indices, with document and clause indices and larger shard counts for very large tenants | [2026-08-26](https://tech.mntsq.co.jp/entry/2026/08/26/180213) |
| Job queueing | SQS-based queues split by priority and by feature, with autoscaling and Datadog monitoring | [2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614) |
| Integrations | E-signature (DocuSign, CloudSign), email ingestion, SharePoint, Google Drive and Box, Slack, Teams, public matter-management API, NTA corporate master | See `Integrations and API` |

The company runs a Japanese-language tech blog on Hatena Blog. Its sitemap lists 108 posts from 2020-11 to 2026-09, 24 of them in 2026 ([tech.mntsq.co.jp](https://tech.mntsq.co.jp/); accessed 2026-10-11). The company also publishes on [note](https://note.mntsq.co.jp/) and hosts events on [connpass](https://mntsq.connpass.com/).

### Technical background sought

From the current postings on HRMOS (accessed 2026-10-11):

- **Software Engineer (Backend).**
  - Required: three or more years developing and operating web applications; independently solving technical problems; API and database design as a backend engineer.
  - Preferred: Ruby on Rails, Vue.js or Python; leading BtoB system design through implementation; cloud infrastructure design and configuration management based on availability, security and fault tolerance ([posting](https://hrmos.co/pages/mntsq/jobs/10055)).
- **Tech Lead.**
  - Required: five or more years of web-application design, development and operation; technology selection and architecture design; leading difficult projects as tech lead; BtoB system design.
  - Preferred: product development with machine learning, NLP or search systems; search systems on Elasticsearch or Apache Solr; systems for highly specialised professional domains ([posting](https://hrmos.co/pages/mntsq/jobs/10034)).
- **AI (NLP) Engineer.**
  - Required: systematic ML/NLP knowledge; three or more years building ML/NLP into products, designing evaluation metrics and improving performance; using major LLM APIs (OpenAI, Claude, Gemini); web-application or API development.
  - Preferred: building AI agents with MCP or A2A; search systems on Elasticsearch or OpenSearch; data-platform work; LLM fine-tuning or pre-training; talks or papers at AI/NLP venues ([posting](https://hrmos.co/pages/mntsq/jobs/10064)).
- **Lead Engineer (Frontend).**
  - Required: five or more years with Vue.js or React.
  - Preferred: building and running a design system ([posting](https://hrmos.co/pages/mntsq/jobs/10037)).
- **Design Engineer.**
  - Required: building, running and improving a design system ([posting](https://hrmos.co/pages/mntsq/jobs/10038)).
- **Selection.** The backend technical assignment is a schema-design exercise in which AI use is assumed. Final interviews are held in person, and the process includes reference and background checks ([posting](https://hrmos.co/pages/mntsq/jobs/10055)).

### Industry domain

The work concerns Japanese corporate legal practice:

- contract drafting, review and negotiation between business units and legal departments;
- contract ledgers, renewal and deadline management;
- law-firm best practice in the form of templates and playbooks;
- e-signature and the 電子帳簿保存法 (Electronic Books Maintenance Act);
- the revised subcontracting law (取適法), for which templates were added ([2026-06-18](https://prtimes.jp/main/html/rd/p/000000101.000050130.html)).

The development division includes a legal expert team of lawyers and former in-house legal staff who work on product planning ([Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)). The CEO's recruiting message states "契約に詳しい必要はありません" (no need to be familiar with contracts) ([careers site](https://careers.mntsq.co.jp/); accessed 2026-10-11). Engineering postings ask for interest in, and willingness to learn, the company's business domain rather than prior legal experience ([posting](https://hrmos.co/pages/mntsq/jobs/10055)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | Not stated. Postings, careers site and deck are in Japanese; no English requirement or English-language posting found | [HRMOS job board](https://hrmos.co/pages/mntsq/jobs); accessed 2026-10-11 |
| Location | Tokyo, Harumi Triton Square Office Tower X, 4F; workplace changes are at the company's discretion | [posting](https://hrmos.co/pages/mntsq/jobs/10055) |
| Office policy | Hybrid; at least 5 office days per month, otherwise remote from home only; full remote not allowed. All-staff monthly meeting in the office on the third Tuesday | [posting](https://hrmos.co/pages/mntsq/jobs/10055), [careers FAQ](https://careers.mntsq.co.jp/) |
| Hours | Full flextime with no core time; 8 standard hours. Engineers set meeting-free days and time slots | [posting](https://hrmos.co/pages/mntsq/jobs/10055) |
| Salary (annual, by posting) | Tech Lead ¥11.0M–15.0M; Lead Engineer (Backend / Frontend) ¥9.0M–13.0M; AI (NLP) Engineer ¥8.0M–15.0M; Software Engineer (Backend / Frontend) and Design Engineer ¥6.5M–12.0M. Annual salary paid in 12 instalments, including 45 hours of deemed overtime with any excess paid separately; reviews twice a year | [Tech Lead](https://hrmos.co/pages/mntsq/jobs/10034), [Lead BE](https://hrmos.co/pages/mntsq/jobs/10036), [Lead FE](https://hrmos.co/pages/mntsq/jobs/10037), [AI](https://hrmos.co/pages/mntsq/jobs/10064), [SE BE](https://hrmos.co/pages/mntsq/jobs/10055), [SE FE](https://hrmos.co/pages/mntsq/jobs/10056), [Design](https://hrmos.co/pages/mntsq/jobs/10038); accessed 2026-10-11 |
| Salary grades | The deck shows seven grades with ranges on an axis labelled 400–1,800, unit not stated. Grade 1 starts around 500 and grade 7 has no upper limit | [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) |
| Equity | Stock option scheme in addition to salary | [posting](https://hrmos.co/pages/mntsq/jobs/10055) |
| Leave and probation | Two days off per week plus public holidays; 13 days of paid leave on joining, then 14–23 days a year; 3-month probation | [posting](https://hrmos.co/pages/mntsq/jobs/10055) |
| Benefits | Commuting allowance up to ¥50,000/month, free office gym, babysitter discount vouchers, flu-vaccination subsidy, Claude Enterprise account, 関東ITソフトウェア健康保険組合 | [posting](https://hrmos.co/pages/mntsq/jobs/10055) |
| Side jobs | Allowed with prior approval | [posting](https://hrmos.co/pages/mntsq/jobs/10055), [careers FAQ](https://careers.mntsq.co.jp/) |
| Onboarding | Three-month programme with a mentor | [posting](https://hrmos.co/pages/mntsq/jobs/10055) |
| Visa sponsorship, new graduates | Not mentioned in the engineering postings reviewed | [HRMOS job board](https://hrmos.co/pages/mntsq/jobs); accessed 2026-10-11 |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11):

- the official site and its sitemap: about, product, clients, case studies, news index and security policy;
- the careers site and every current posting on the HRMOS job board (23 roles), plus the HERP Career aggregator listing;
- MNTSQ's PR TIMES company page (104 releases listed);
- the tech blog sitemap, note, Speaker Deck (10 decks) and connpass;
- the GitHub organisation API, the NTA corporate number register, BRIDGE, and the PFN leadership page;
- Japanese and English web searches for MNTSQ, モンテスキュー and ＭＮＴＳＱ株式会社 combined with funding, ARR, 決算公告 and J-Startup.

TokyoDev returned HTTP 403 to automated access; Japan Dev has no MNTSQ company page (HTTP 404).

- **Revenue, ARR, profitability and valuation.** Not published. No 決算公告 was found in web search; the 官報 itself was not searched.
- **Cumulative funding.** The company has not published a total. The PKSHA, Nishimura & Asahi and Mori Hamada amounts are undisclosed, and no release labelled シリーズA was found.
- **Engineering working language and visa policy.** Not stated in any posting or careers page reviewed.
- **Price list.** Only the fee structure is public; a plan guide is gated behind a form.
- **Public API documentation.** The matter-management API is described in releases, but no public reference was found.
- **Open source.** The GitHub organisation [`MNTSQ`](https://github.com/MNTSQ) was created 2018-11-21. Its metadata lists location "Japan" and no website, email or X account, and none of the company's sites reviewed link to it. It has four public repositories: three forks of Ruby/Rails tooling (`apivore`, `ruby-ntlm`, `annotate_models`) and one Python repository, `simple-mcp-rag`, last pushed 2025-10-21.
- **Status page or SLA.** None found.
- **Turnover.** Not published.

### Inconsistencies across sources

- **Founding year.** The company's releases give 設立日 2018-11-14, and the NTA register shows the corporate number designated 2018-11-27 ([NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433)). The company's own column with NO&T states "2019年にMNTSQを創業しました" ([column, 2025-03-03](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)).
- **Top-100 customer count.** The backend posting states 43 of the top 100 "2026年4月現在" ([posting](https://hrmos.co/pages/mntsq/jobs/10055); accessed 2026-10-11). Releases published after that date give 41 ([2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html), [2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html), [2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html)), and later 42 as of 2026-06-12 ([2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)).
- **Katayama's board role.** MNTSQ's about page lists him as "Co-Founder / 取締役" ([about](https://mntsq.co.jp/about)). Preferred Networks' biography says he "MNTSQの社外取締役も務める" (also serves as an outside director of MNTSQ) ([PFN leadership](https://www.preferred.jp/ja/company/leadership)).
- **Development team structure.** The postings describe 開発本部 as about 50 people in four teams (CLM, 法務エージェント, 事業部向け, イネーブリング), as of 2026-08 ([posting](https://hrmos.co/pages/mntsq/jobs/10034)). The 2026-09 deck splits CLM into application and platform teams and adds a separate プラットフォーム部 and a legal expert team ([Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)). The sources do not state whether the 50-person figure includes the platform and legal expert teams.
- **Release dates.** Dates shown as 更新 on mntsq.co.jp news pages sometimes differ by a day from PR TIMES, for example 2019-10-20 versus 2019-10-21 and 2023-09-18 versus 2023-09-19. This page uses the PR TIMES dates.

### Other

- The company's product names have changed over time:
  - **2020:** "MNTSQ for M&A" (law-firm due diligence) and "MNTSQ for Enterprise" ([2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)).
  - **2022-01:** the line-up is called "MNTSQ" ([2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html)).
  - **From 2022-07:** "MNTSQ CLM" ([2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html)).
  - **2026 releases** describe it variously as 契約プラットフォーム and 契約AIインフラ ([2026-08-06](https://prtimes.jp/main/html/rd/p/000000110.000050130.html), [2026-09-01](https://prtimes.jp/main/html/rd/p/000000117.000050130.html)).
- The company's first large media campaign ran from June to July 2026: YouTube ads, taxi signage, and outdoor advertising at Tokyo and Otemachi stations ([2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html)).
- Of the 32 PR TIMES releases dated 2026-01-16 to 2026-09-18, 17 are product feature or template updates. The rest are awards (5), case studies (4), events (3), appointments and hires (2) and an advertising campaign (1) ([PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/50130); accessed 2026-10-11).

---

## Resources

**Official**

- [Corporate site (JA)](https://mntsq.co.jp/) · [About / company profile](https://mntsq.co.jp/about) · [Clients](https://mntsq.co.jp/clients) · [Case studies](https://mntsq.co.jp/case) · [News index](https://mntsq.co.jp/news)
- Product pages: [index](https://mntsq.co.jp/product) · [案件管理](https://mntsq.co.jp/product/casemanage) · [契約管理](https://mntsq.co.jp/product/contractmanage) · [データベース](https://mntsq.co.jp/product/databasemanage) · [AI契約アシスタント](https://mntsq.co.jp/product/aicontract-assistant) · [AI Agent](https://mntsq.co.jp/product/mntsq-ai-agent)
- [ISMS certification notice, 2024-03-22 (JA)](https://mntsq.co.jp/news/information/202403-isms) · [NEXTユニコーン調査2024 notice, 2025-01-17 (JA)](https://mntsq.co.jp/news/information/nextunicorn2024)
- [Column: NO&T and MNTSQ founding story, 2025-03-03 (JA)](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)
- [MNTSQ AI Agent release on the company site, 2025-09-19 (JA)](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025)
- [Careers site (JA)](https://careers.mntsq.co.jp/) · [Engineering careers page (JA)](https://careers.mntsq.co.jp/mntsq-for-engineers)
- [HRMOS job board (JA)](https://hrmos.co/pages/mntsq/jobs): [Tech Lead](https://hrmos.co/pages/mntsq/jobs/10034) · [Lead Engineer (Backend)](https://hrmos.co/pages/mntsq/jobs/10036) · [Lead Engineer (Frontend)](https://hrmos.co/pages/mntsq/jobs/10037) · [Design Engineer](https://hrmos.co/pages/mntsq/jobs/10038) · [Software Engineer (Backend)](https://hrmos.co/pages/mntsq/jobs/10055) · [Software Engineer (Frontend)](https://hrmos.co/pages/mntsq/jobs/10056) · [AI (NLP) Engineer](https://hrmos.co/pages/mntsq/jobs/10064) · [制度企画・労務](https://hrmos.co/pages/mntsq/jobs/30017)
- [Tech Blog (JA)](https://tech.mntsq.co.jp/) · [archive](https://tech.mntsq.co.jp/archive) — [GCP Workload Identity Federation, 2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103) · [Search for legal work, 2026-09-09](https://tech.mntsq.co.jp/entry/2026/09/09/083234) · [Elasticsearch to OpenSearch, 2026-08-26](https://tech.mntsq.co.jp/entry/2026/08/26/180213) · [Celery + SQS, 2026-06-29](https://tech.mntsq.co.jp/entry/2026/06/29/090000) · [Redis to SQS, 2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614)
- [note (JA)](https://note.mntsq.co.jp/) · [connpass](https://mntsq.connpass.com/)
- [Speaker Deck](https://speakerdeck.com/mntsq) — [Engineering Team Deck, 2026-09-01 更新 (JA)](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) · [LT: replacing contract analysis with LLMs, 2024-07-11 (JA)](https://speakerdeck.com/mntsq/ltzi-liao-mntsqnoqi-yue-shu-jie-xi-wo-llmnizhi-kihuan-eruhua)
- [Wantedly post by 堅山, 2019-10-29 (JA)](https://www.wantedly.com/companies/mntsq/post_articles/192635)
- [GitHub organization MNTSQ](https://github.com/MNTSQ)

**Press releases (PR TIMES, JA — newest first)** · [company page](https://prtimes.jp/main/html/searchrlp/company_id/50130)

- [AI Agent phase 3: contract review in Word — 2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html)
- [Microsoft Teams integration — 2026-09-01](https://prtimes.jp/main/html/rd/p/000000117.000050130.html)
- [Slack integration — 2026-08-06](https://prtimes.jp/main/html/rd/p/000000110.000050130.html)
- [E-signature integration extended — 2026-07-23](https://prtimes.jp/main/html/rd/p/000000107.000050130.html)
- [ITreview Grid Award 2026 Summer — 2026-07-15](https://prtimes.jp/main/html/rd/p/000000106.000050130.html)
- [2,000 adopting companies; first media campaign — 2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html)
- [HR's SDGsアワード2026 — 2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)
- [Templates: 13 added incl. AI service terms — 2026-06-18](https://prtimes.jp/main/html/rd/p/000000101.000050130.html)
- [Public API: ISO 8601 date format — 2026-06-16](https://prtimes.jp/main/html/rd/p/000000100.000050130.html)
- [Tokyo Electron case study — 2026-06-04](https://prtimes.jp/main/html/rd/p/000000098.000050130.html)
- [COO appointment (深井 亮) — 2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html)
- [CEO receives FT Legal Intrapreneur award — 2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)
- [Counterparty management with NTA master — 2026-05-19](https://prtimes.jp/main/html/rd/p/000000094.000050130.html)
- [Algorithm engineer 内海 慶 joins — 2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html)
- [Public matter-management API — 2026-04-07](https://prtimes.jp/main/html/rd/p/000000089.000050130.html)
- [AI Agent in 案件管理 — 2026-03-05](https://prtimes.jp/main/html/rd/p/000000084.000050130.html)
- [Multi-language contract analysis — 2026-01-21](https://prtimes.jp/main/html/rd/p/000000080.000050130.html)
- [Template line-up doubled — 2026-01-16](https://prtimes.jp/main/html/rd/p/000000081.000050130.html)
- [Nikkei 2025 ranking: 9 of top 10 — 2025-12-24](https://prtimes.jp/main/html/rd/p/000000079.000050130.html)
- [ISO 4217 currencies — 2025-12-16](https://prtimes.jp/main/html/rd/p/000000078.000050130.html)
- [Office move to Harumi Triton Square — 2025-10-09](https://prtimes.jp/main/html/rd/p/000000071.000050130.html)
- [Itochu adopts MNTSQ CLM — 2025-10-08](https://prtimes.jp/main/html/rd/p/000000069.000050130.html)
- [Kanpo–Aflac–Japan Post accelerator — 2025-08-15](https://prtimes.jp/main/html/rd/p/000000066.000050130.html)
- [AIリーガルテック協会 symposium — 2025-07-09](https://prtimes.jp/main/html/rd/p/000000065.000050130.html)
- [案件フロー feature — 2025-06-30](https://prtimes.jp/main/html/rd/p/000000064.000050130.html)
- [Mori Hamada & Matsumoto capital and business alliance — 2025-05-07](https://prtimes.jp/main/html/rd/p/000000063.000050130.html)
- [AI契約アシスタント orders open — 2025-03-19](https://prtimes.jp/main/html/rd/p/000000061.000050130.html)
- [Nishimura & Asahi strategic collaboration — 2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html)
- [¥1.0B via three CVCs, bond and loan — 2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)
- [AI契約レビュー release — 2024-02-28](https://prtimes.jp/main/html/rd/p/000000049.000050130.html)
- [English UI — 2023-10-02](https://prtimes.jp/main/html/rd/p/000000047.000050130.html)
- [Series B, ¥1.0B — 2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)
- [MNTSQ AI契約レビュー development announced — 2023-09-19](https://prtimes.jp/main/html/rd/p/000000046.000050130.html)
- [Hitachi adopts MNTSQ CLM — 2023-08-09](https://prtimes.jp/main/html/rd/p/000000040.000050130.html)
- [Generative AI/LLM development team — 2023-06-05](https://prtimes.jp/main/html/rd/p/000000035.000050130.html)
- [RubyKaigi 2023 Ruby Sponsor — 2023-03-06](https://prtimes.jp/main/html/rd/p/000000031.000050130.html)
- [Office move; 50 members — 2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html)
- [Mitsubishi Electric adopts full line-up — 2022-01-26](https://prtimes.jp/main/html/rd/p/000000018.000050130.html)
- [案件管理 announced — 2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html)
- [稲葉総合法律事務所 adopts MNTSQ — 2021-12-22](https://prtimes.jp/main/html/rd/p/000000015.000050130.html)
- [SMBC syndicated-loan drafting — 2021-11-01](https://prtimes.jp/main/html/rd/p/000000014.000050130.html)
- [Zuva DocAI integration — 2021-09-30](https://prtimes.jp/main/html/rd/p/000000013.000050130.html)
- [Mitsubishi Corporation — 2021-06-30](https://prtimes.jp/main/html/rd/p/000000012.000050130.html)
- [CloudSign integration — 2021-04-14](https://prtimes.jp/main/html/rd/p/000000009.000050130.html)
- [MNTSQ for Enterprise release — 2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)
- [PoC with Komatsu and Fukuoka Bank — 2020-06-10](https://prtimes.jp/main/html/rd/p/000000003.000050130.html)
- [NO&T partners join board — 2019-11-13](https://prtimes.jp/main/html/rd/p/000000002.000050130.html)
- [NO&T and PKSHA capital and business alliance, ¥800M — 2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)

**Third-party coverage and profiles**

- [NTA corporate number register — 7010001196433 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433)
- [Preferred Networks leadership — 堅山 耀太郎 biography (JA)](https://www.preferred.jp/ja/company/leadership)
- [BRIDGE — 2024 round, 2024-06-04 (JA)](https://thebridge.jp/2024/06/mntsq-jpy1b-round-funding)
