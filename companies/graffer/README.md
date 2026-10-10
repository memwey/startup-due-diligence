# Graffer

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Graffer (株式会社グラファー / Graffer, Inc.) is a Tokyo company founded on 2017-07-18 by 石井 大地 (Daichi Ishii). It runs two lines of business: **Graffer Platform**, a suite of cloud services sold to local governments and central ministries — online applications (Graffer スマート申請), procedure guides, counter reservations, IVR and AI voice agents for phone enquiries, and a long-term-care certification status service — and **Graffer AI Solution**, which sells an enterprise generative-AI workspace (Graffer AI Studio), task-specific AI agents, an AI data-conversion product for food-industry specification sheets (Graffer Databridge), AI-assisted contract development, and training ([company page](https://graffer.jp/company), [company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). Since January 2026 its mission has been "We Remove Steps." ([about](https://graffer.jp/about)).

- Government scale: "270団体超" (over 270 organisations), including 70% of designated cities, covering about 70 million residents, as of 2026-03 ([company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). The government product page shows "7215 万人の市民が対象" and "254 の政府機関での案件実績" (Undated; accessed 2026-10-11; [governments page](https://graffer.jp/governments)). The figures differ between sources; see `Notes`.
- Funding: about ¥2.22B (約22.2億円) cumulative by the 約12億円 Series B on [2021-04-01](https://graffer.jp/news/2679). A capital and business alliance with Change Holdings followed on [2023-04-14](https://graffer.jp/news/4516); no amount was disclosed. The company bought 100% of 行政システム研究所 on [2026-04-27](https://graffer.jp/news/7317) and of 5Minutes on [2026-06-30](https://graffer.jp/news/7505).
- Headcount: "社員 81名" (81 employees, employees only, as of 2026-06) ([company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)).
- Engineering: the job postings list Go and Python (Gin, Flask) for the backend and TypeScript, React and Next.js for the frontend, plus AWS, Docker, Kubernetes, Terraform, PostgreSQL, MySQL and MongoDB. Public certification scopes confirm AWS and MongoDB Atlas. Engineers work "full-cycle", with one person covering everything from requirements to operation ([full-cycle engineer posting](https://herp.careers/v1/graffer/QE1EVzBa9GqT), [company page](https://graffer.jp/company); accessed 2026-10-11). All postings and recruiting material are in Japanese. Full remote work and flextime with no core hours are offered ([company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | 株式会社グラファー / Graffer, Inc. | [NTA corporate number record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779), [company page](https://graffer.jp/company) |
| Corporate number | 9010401132779; designated 2017-07-28 (平成29年7月28日) | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779); information as of 2026-10-11 |
| Founded | 2017-07-18 | [company page](https://graffer.jp/company) |
| Registered head office | 東京都渋谷区千駄ヶ谷１丁目５番８号 (since 2022-01-05). Earlier registered addresses: 港区赤坂1-12-32 → 渋谷区神宮前2-3-10 (2018-03-22) → 渋谷区千駄ヶ谷1-2-3 (2019-11-01) | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779) |
| Office | 千駄ヶ谷オフィス, ジュニアー千駄ヶ谷ビル2F. A Kobe office was opened in December 2019; the current company page lists only the Sendagaya office | [company page](https://graffer.jp/company), [2019-12-20](https://graffer.jp/news/1524) |
| Representative | 代表取締役 / 創業者 石井 大地 | [company page](https://graffer.jp/company) |
| Board | 石井 大地 (代表取締役), 小寺 広晃 (取締役 兼 COO), 村田 祐介 (取締役), 澤山 陽平, 中谷 昇, 瀧 俊雄 (社外取締役), 千葉 尚洋 (常勤監査役・社外) | [company page](https://graffer.jp/company); accessed 2026-10-11 |
| Capital | ¥1,544,977,927 including capital reserve (資本準備金を含む) | [company page](https://graffer.jp/company); accessed 2026-10-11 |
| Major shareholders (as listed) | 経営陣及び従業員, Incubate Fund, Coral Capital (旧500 Startups Japan), 株式会社チェンジホールディングス, TOPPANホールディングス株式会社, 個人投資家 | [company page](https://graffer.jp/company) |
| Main banks | みずほ銀行, 三井住友銀行, 商工組合中央金庫 | [company page](https://graffer.jp/company) |
| Headcount | 81 employees (社員のみ), as of 2026-06 | [company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| Working language | Not stated. The careers site, all ten HERP postings and both recruiting decks are in Japanese only | [careers site](https://career.graffer.inc/), [HERP](https://herp.careers/v1/graffer); accessed 2026-10-11 |
| Total raised | 約22.2億円 cumulative, stated in the Series B release; later amounts not disclosed | [2021-04-01](https://graffer.jp/news/2679) |
| ISMS | ISO/IEC 27001:2022, IS 689557. First registered 2018-06-23; valid to 2027-06-22. Scope: Webサービスの開発及び運用, ビジネスアウトソーシング事業, 人材派遣業 | [company page](https://graffer.jp/company), [ISMS registry](https://isms.jp/lst/ind/CR_IS_x0020_689557.html) |
| Cloud security | ISO/IEC 27017: CLOUD 806590 for Graffer Platform (first registered 2024-06-23) and CLOUD 828729 for Graffer AI Studio (2025-05-07) | [company page](https://graffer.jp/company), [2025-06-06](https://graffer.jp/news/6618) |
| Privacy | プライバシーマーク 第17004041号 (announced [2021-03-12](https://graffer.jp/news/2581)) | [company page](https://graffer.jp/company) |
| ISMAP | Graffer Platform was registered on the ISMAP cloud service list on 2021-12-20. The company filed for withdrawal on 2022-01-24, citing the audit cost of keeping the registration, and was removed | [2022-04-01](https://graffer.jp/news/3504) |

**Programs and recognition.** Selected for J-Startup 2021 ([2021-10-20](https://graffer.jp/news/3080)). Won the Findy Team+ Award in 2023 and 2024 ([2024-11-01](https://graffer.jp/news/6095)). Graffer スマート申請 was named in the 総務省「情報アクセシビリティ好事例2024」([2025-03-19](https://graffer.jp/news/6490)). The company launched the media site "Govtech Trends" on [2019-08-23](https://graffer.jp/news/1402).

**Market context as stated by the company.** The company deck cites government figures of more than 62,000 types of administrative procedure, about 2.5 billion procedures a year, 12億3,238時間 of procedure time and ¥3兆1,070億 in procedure costs. It also gives an estimated TAM approaching ¥10 trillion when cloud/IT and adjacent BPO spending by central and local government are combined ([company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). For the food industry, it cites a METI study putting product-information exchange at 300,000 person-months a year, which it equates to a cost of about ¥100 billion ([2025-11-19](https://graffer.jp/news/6911)).

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated | Source |
|---|---|---|---|---|
| 株式会社グラファー (Graffer, Inc.) | Legal entity | Japan; corporate number 9010401132779 | Operating company | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779) |
| 株式会社行政システム研究所 | Subsidiary | Sapporo; founded 2014-06; 100% acquired 2026-04-27 | Public-accounting (公会計) systems for local governments | [2026-04-28](https://graffer.jp/news/7317) |
| 株式会社5Minutes | Subsidiary | Kobe; founded 2021-02; 100% acquired 2026-06-30 | Google Workspace / Google Cloud authorised reseller | [2026-06-30](https://graffer.jp/news/7505) |
| 株式会社KURASERU | Counterparty to a business transfer | Osaka | Graffer took over its long-term-care certification enquiry system business on 2024-10-24 | [2024-10-24](https://graffer.jp/news/6054) |
| ｇｒａｐｈｅｒ株式会社 | Unrelated entity with the same reading (グラファー) | Tokyo, Nakano-ku | No connection is stated in any source reviewed | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011201021353) |

The KURASERU release and the 5Minutes release name the same representative director, 平山 流石, for the two counterparties ([2024-10-24](https://graffer.jp/news/6054), [2026-06-30](https://graffer.jp/news/7505)). Neither the purchase prices nor the post-acquisition structure were disclosed.

---

## Product

The current line-up follows the service map in the [company deck (version 2026-07)](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao), the [government product page](https://graffer.jp/governments) and the [AI Solution site](https://graffer.jp/ai-solution) (accessed 2026-10-11).

### Graffer Platform (local governments and ministries)

| Service | What it is | Launch / first public date | Page |
|---|---|---|---|
| Graffer スマート申請 | Online applications that complete on a smartphone, with a form builder, templates, My Number Card identity verification, cashless payment, e-signatures, LGWAN support and online issuance of documents | [2020-04-07](https://graffer.jp/news/1616) | [page](https://graffer.jp/governments/solution-smart-apply) |
| Graffer 手続きガイド | Question-driven guide that tells residents which procedures apply to them | First municipal deployment (Kamakura) [2018-11-01](https://graffer.jp/news/405) | [page](https://graffer.jp/governments/solution-guides) |
| Graffer 窓口予約 | Online booking for government counters | [2021-09-01](https://graffer.jp/news/2928) | [page](https://graffer.jp/governments/solution-booth-reserve) |
| Graffer Call | IVR using push-dial and AI routing, SMS links and automated outbound calls; call recording announced for late August 2025 ([2025-07-29](https://graffer.jp/news/6699)) | "提供を開始" [2024-08-16](https://graffer.jp/news/5898); see `Notes` | [page](https://graffer.jp/governments/solution-call) |
| Graffer AI オペレーター | Conversational AI phone agent that answers from a registered knowledge base and transfers calls to staff | First public mention [2025-10-03](https://graffer.jp/news/6822) | [page](https://graffer.jp/governments/solution-ai-operator) |
| お悩みハンドブック | Finds support programmes and contacts from the problems a user ticks; national version and municipal versions | National version [2022-01-27](https://graffer.jp/news/3297); municipal customisation [2022-12-15](https://graffer.jp/news/4081) | [page](https://graffer.jp/governments/solution-compass) |
| Graffer 要介護認定照会 | Online status checks and information-request applications for long-term-care certification; municipalities connect over LGWAN-ASP | Business acquired [2024-10-24](https://graffer.jp/news/6054) | [page](https://graffer.jp/governments/solution-nintei-shoukai) |
| Graffer 認定調査票作成 | AI support for preparing care-certification survey forms (pilot) | Pilot in Miyakonojo [2026-08-28](https://graffer.jp/news/7697) | [inquiry page](https://graffer.jp/governments/solution-nintei-chosahyo) |
| Graffer AI BPO | AI-based business-process outsourcing | Listed in the deck's service map; not dated | [deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |

For ministries and affiliated bodies, the [ministries page](https://graffer.jp/ministries) (accessed 2026-10-11) offers consulting and DX planning, BPR, procurement support, task-specific AI agents, "SI by AI駆動開発" (legacy migration and modernisation) and training. It also invites other firms to subcontract public-sector projects to Graffer.

### Graffer AI Solution (enterprises)

| Offering | What it is | Launch | Page |
|---|---|---|---|
| Graffer AI Studio | Enterprise generative-AI workspace offering GPT, Gemini and Claude models with automatic model selection, RAG over internal documents, transcription, data analysis, batch processing, a prompt-free task library, image generation and "AI Labs". Enterprise controls include SAML SSO, SCIM, a user-management API and audit logs | Closed beta [2023-03-24](https://graffer.jp/news/4389); GA [2023-04-26](https://graffer.jp/news/4561) | [page](https://graffer.jp/ai-solution/products/graffer-ai-studio) |
| 業務特化AIエージェント | Customer-specific AI apps built and hosted on the AI Studio platform | [2025-10-07](https://prtimes.jp/main/html/rd/p/000000103.000038525.html) | [page](https://graffer.jp/ai-solution/ai-consulting-development) |
| Graffer Databridge | AI agent that reads PDF and Excel food specification sheets (食品規格書) and converts them into each retailer's format; patent application 特願2024-209582 | Closed beta [2025-11-19](https://graffer.jp/news/6911); 国分西日本 [2026-06-02](https://graffer.jp/news/7409) | [page](https://graffer.jp/ai-solution/ai-databridge/food-kikaku) |
| Graffer AI駆動開発プログラム | Team-level training that installs an AI-first development process ("生産性2,000%アップ") | [2025-10-06](https://graffer.jp/news/6834) | [page](https://graffer.jp/ai-solution/generative-ai-learning/ai-dev-training) |
| AI駆動受託開発 / AI駆動基幹システム刷新 | AI-assisted contract development and replacement of legacy core systems, including reverse-engineering specifications from source code | Listed in the deck's service map | [deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| Advisory and training | Adoption support (伴走支援) and generative-AI training | Graffer AI Solution dated 2023-10 in the [product deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian) | [site](https://graffer.jp/ai-solution) |

**Discontinued.** Graffer 法人証明書請求 (online ordering of corporate registry certificates; 10,000 corporate users by [2020-02-26](https://graffer.jp/news/1561)) and Graffer 電子証明書取得サポート stopped taking new orders on 2025-03-31. Graffer 法人証明書請求 shut down completely on 2025-06-30 ([2025-02-27](https://graffer.jp/news/6473)).

### Commercialization

Government products are sold as SaaS, and the company also offers consulting, BPO and contract development. No public price list was found for Graffer Platform; the 窓口予約 page describes a fixed-fee plan (定額制) without numbers. Graffer AI Studio offers a full-support plan or a tool-only plan, with no published prices ([page](https://graffer.jp/ai-solution/products/graffer-ai-studio)). The task-specific AI agent service is the one offering with a published price structure: development from ¥500,000, monthly fee from ¥20,000, AI model usage billed separately, and delivery in a standard one month or as little as two weeks ([2025-10-07](https://prtimes.jp/main/html/rd/p/000000103.000038525.html), [page](https://graffer.jp/ai-solution/ai-consulting-development)). Graffer Platform services are registered on Digital Agency's Digital Marketplace; the company states that Graffer 要介護認定照会 was the first service adopted through it ([2025-11-17](https://graffer.jp/news/6904)).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2019-01-21 | Team of about 10 people | [BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising) |
| 2019-03 → 2023-03 | Government organisations: 2 (2019-03), 6 (2020-03), 50 (2021-03), 102 (2022-03), 160 (2023-03) | [company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 2022-02-16 | お悩みハンドブック national version passes 100,000 cumulative users | [release](https://graffer.jp/news/3381) |
| 2023-03-14 | "全国140以上の自治体"; 70% of designated cities | [2023-04-14](https://graffer.jp/news/4516) |
| 2024-10-24 | "全国200以上の自治体" | [release](https://graffer.jp/news/6054) |
| 2025-04 → 2025-06 | Release frequency 6.18 per day | [deck, 2025-07-31](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge) |
| Published 2025-07-31 | 273 organisations; over 41 million residents covered | [deck, 2025-07-31](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge) |
| 2026-03 | "270団体超"; about 70 million residents | [company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| Deck version 2026-07 | Graffer AI Solution has supported generative-AI use by "2.8万人超" (more than 28,000) business people | [company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 2025-04 → 2026-03 | Graffer スマート申請 user satisfaction 4.3/5 from about 800,000 respondents | [スマート申請 page](https://graffer.jp/governments/solution-smart-apply) |
| 2026-07 | About 70,000 shared forms on Graffer スマート申請; about 3,000 forms created by AI from paper templates | [スマート申請 page](https://graffer.jp/governments/solution-smart-apply) |
| Undated; accessed 2026-10-11 | "7215 万人の市民が対象", "254 の政府機関での案件実績"; お悩みハンドブック used by more than 600,000 people | [governments page](https://graffer.jp/governments), [services page](https://graffer.jp/services) |

### Announced customers and partners

Representative examples only; the [news index](https://graffer.jp/news) carries 510 items, most of them individual municipal adoptions.

| Date | Party | What was announced |
|---|---|---|
| [2019-08-19](https://graffer.jp/news/1396) | Yahoo! JAPAN | Business alliance in lifestyle information |
| [2021-03-30](https://graffer.jp/news/2648) | 福岡市 | City-wide electronic application system on Graffer スマート申請 |
| [2021-09-03](https://graffer.jp/news/2935) | 滋賀県 | Joint procurement of スマート申請, 手続きガイド and 窓口予約 |
| [2023-04-26](https://graffer.jp/news/4561) | ニチイ学館 | Proof of concept for Graffer AI Studio |
| [2023-10-12](https://graffer.jp/news/4924) | TOPPAN group | Graffer AI Studio provided |
| [2025-02-26](https://graffer.jp/news/6439) | ミスターマックス | Graffer AI Solution adopted across all head-office departments |
| [2025-04-22](https://graffer.jp/news/6589) | 東京消防庁 | Integration between スマート申請 and its e-application system |
| [2025-05-30](https://graffer.jp/news/6613) | 京都市 | Graffer Call on the main lines of all ward offices and branches |
| [2025-08-21](https://graffer.jp/news/6737) → [2026-05-29](https://graffer.jp/news/7399) | 国土交通省 | DX of the 建設業法 whistleblowing hotline; results reported as about 35% fewer calls |
| [2025-12-02](https://graffer.jp/news/6970) | ROUTE06 | Business alliance combining its "Acsim" requirements tool with the AI駆動開発プログラム |
| [2026-01-06](https://graffer.jp/news/7035) | 港区 | Pilot of AI agent phone answering (Graffer AI オペレーター) |
| [2026-03-10](https://graffer.jp/news/7211) | リコー | AI駆動開発プログラム; release states a two-month process was completed in three weeks and pull requests doubled |
| [2026-05-28](https://graffer.jp/news/7405) | デジタル庁 | Completed an AI-agent proof of concept for reviewing system-development documents |
| [2026-06-18](https://graffer.jp/news/7446) | 大阪府 | Joined the 大阪府行政AIエージェントコンソーシアム |
| [2026-08-31](https://graffer.jp/news/7705) | 福岡市 | Pilot of AI-assisted subsidy screening |

### Stated plans

- Govtech: the company says it will expand from resident-facing systems into the back-office systems that staff use, to deliver "エンドツーエンドの業務処理フロー" ([company deck, version 2026-07](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). After the 行政システム研究所 acquisition it plans to cross-sell Graffer Platform and add new services for municipal staff ([2026-04-28](https://graffer.jp/news/7317)).
- Food & Beverage: cut food-industry data-conversion costs to one fifth or less using AI agents ([company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). Databridge is to expand to e-commerce malls, HR (staffing), manufacturing and apparel ([2025-11-19](https://graffer.jp/news/6911)).
- AI-driven development: "Prompt to App: システム開発不要な世界の実現" ([company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)).

---

## Founder

**石井 大地 (Daichi Ishii)** — 代表取締役 / 創業者 ([company page](https://graffer.jp/company)).

- Entered the University of Tokyo Faculty of Medicine, then transferred to and graduated from the Faculty of Letters. Won the 48th 文藝賞 (Kawade Shobo Shinsha) in 2011 and debuted as a novelist ([company page](https://graffer.jp/company)).
- Founded and managed several companies and launched businesses at startups. At Recruit Holdings' Media & Solutions SBU he worked on business strategy and business-development investment in Japanese and overseas technology companies. He founded Graffer in 2017 ([company page](https://graffer.jp/company)). [BRIDGE (2019-01-21)](https://thebridge.jp/2019/01/graffer-fundraising) also states that he was an executive officer (執行役員) at Medley before joining an investment firm; the company's own biography does not name Medley.
- In the founder message he states that nobody on the founding team had worked in government, and that an investor at founding prompted the choice of field ([about](https://graffer.jp/about)). BRIDGE names Incubate Fund GP 村田 祐介, now a Graffer director, as the person who suggested GovTech ([BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising)).
- Director of the Japan Startup Association (スタートアップ協会) from [2024-02-06](https://graffer.jp/news/5276). Member of the Cabinet Bureau of Personnel Affairs' study group on civil servants in the AI era, announced [2026-07-28](https://graffer.jp/news/7552).
- Books: 『こうすればうまくいく 行政のデジタル化』 (2020-12-25) and 『AI駆動開発チームの作り方・育て方 生産性20倍アップのソフトウェア開発』 (Nikkei BP, 2026) ([2026-07-28](https://graffer.jp/news/7552), [2026-02-16](https://graffer.jp/news/7137)).

### Selected leadership

From the [company page](https://graffer.jp/company) (accessed 2026-10-11):

| Name | Role as written | Stated background |
|---|---|---|
| 小寺 広晃 | 取締役 兼 COO (current role since 2026-05) | Recruit Lifestyle 2014 (QR payments); joined 2019; CBO from 2023-03 and COO from 2026-01 for generative-AI products |
| 澤田 淳 | 輪番社長 兼 Senior Vice President of Business; 執行役員 (GovTech本部) | 3M Japan FP&A; GCA (Houlihan Lokey) M&A; joined 2021-10; 輪番社長 since 2026-10 |
| 羽生 和馬 | Senior Vice President of Corporate | GYAO HR head; Yahoo Japan HR; joined 2021-05 |
| 河治 寿都 | Senior Vice President of Engineering; 執行役員 (エンジニアリング本部) | GREE new-graduate engineer; Tech Lead / VPoE / EM in cross-border e-commerce, IoT and healthcare; joined 2025-04 on Graffer AI Studio; current role since 2026-01 |
| 黑﨑 脩 | Vice President of AI Solution Development | Simplex (FX trading systems); co-founded a startup; joined 2021-02 as PM; VP of Product 兼 VP of Engineering from 2023-03; current role since 2026-01 |
| 市川 翔子 | Vice President of AI Solution Development | Mitsubishi Corporation; strategy consulting in Singapore; joined 2020; VP of Business (Enterprise) from 2025-07 |

Outside directors include 澤山 陽平 (Coral Capital founding partner), 中谷 昇 (former INTERPOL IGCI executive director; NEC CSO; appointed [2023-11-01](https://graffer.jp/news/5053)) and 瀧 俊雄 (Money Forward co-founder). 村田 祐介 (Incubate Fund representative partner) is a director. 紫垣 拓也 was announced as CFO on [2021-04-01](https://graffer.jp/news/2679) but does not appear on the current company page. The company describes a rotating-president system (社長輪番制), with 澤田 listed as 輪番社長 from 2026-10 ([company page](https://graffer.jp/company), [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). Staff backgrounds listed in the deck include IT (Recruit, AWS, Uzabase, Works Applications, Yahoo), government (総務省, 経産省), trading companies and professional firms.

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2019-01-21 | 資金調達 (no round name; BRIDGE: J-KISS convertible, led by 500 Startups Japan) | 1.8億円 | 500 Startups Japan, インキュベイトファンド, individual investors | — | [Graffer](https://graffer.jp/news/735), [BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising) |
| 2019-12-20 | シリーズA (第三者割当増資) | 約4.5億円 | Coral Capital, インキュベイトファンド (both existing) | 約7.2億円 | [Graffer](https://graffer.jp/news/1524) |
| 2020-07-16 | 第三者割当増資; 資本業務提携 with 凸版印刷 | 約2.5億円 | Existing shareholders, 凸版印刷 | Capital incl. reserve ¥975,000,313 after the round | [Graffer](https://graffer.jp/news/1754) |
| 2021-04-01 | シリーズB | 約12億円 | Existing investors | 約22.2億円 | [Graffer](https://graffer.jp/news/2679) |
| 2023-04-14 | 資本業務提携 | Not disclosed | チェンジホールディングス | — | [Graffer](https://graffer.jp/news/4516) |

The round labels follow the company's releases. Incubate Fund participated in the 2019-01 round and the Series A; the Series B release names only "existing investors". TOPPAN Holdings (formerly 凸版印刷) and Change Holdings are listed as major shareholders on the [company page](https://graffer.jp/company). The 2019-01 round was announced alongside the launch of Graffer 法人証明書請求, the Series A alongside the new Kobe office, and the Series B alongside the CFO appointment. No financing release after 2023-04 was found in the [news index](https://graffer.jp/news) or on [PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/38525) (checked 2026-10-11).

---

## Engineering

### Technology stack and platforms

**Confirmed by public assets or company documentation:**

- **AWS** — named in the ISO/IEC 27017 scopes for both Graffer Platform and Graffer AI Studio. Both whitepapers say the services use Amazon Time Sync Service ([company page](https://graffer.jp/company), [Platform whitepaper](https://graffer.jp/legal/whitepaper), [AI Studio whitepaper](https://console.graffer.jp/aistudio/docs/whitepaper)). A company note post states "グラファーはAWS環境でずっと開発してきました" ([note, 2026-07-10](https://note.graffer.inc/n/nd0a48a1d33e0)).
- **MongoDB Atlas** — named in both ISO/IEC 27017 scopes ([company page](https://graffer.jp/company)).
- **Twilio** — used by Graffer Call; call data sent to Twilio (phone numbers, call history) is stored in the US, while other customer data is stored in Japan ([Platform whitepaper](https://graffer.jp/legal/whitepaper), 4th edition 2024-03-01).
- **SB Payment Service** — handles card payments for Graffer services ([Platform whitepaper](https://graffer.jp/legal/whitepaper)).
- **LLM providers** — Azure OpenAI Service for the AI Studio knowledge base ([2023-08-24](https://graffer.jp/news/4830)); GPT, Gemini and Claude models in AI Studio ([page](https://graffer.jp/ai-solution/products/graffer-ai-studio)).
- **Sovereign-AI verification setup** — Digital Agency's open-sourced "ガバメントAI 源内" code running on さくらのクラウド with the Japanese LLMs LLM-jp and PLaMo ([2026-06-22](https://graffer.jp/news/7451)).
- **Next.js, LLMs, vector search** — listed as recent technology adoptions ("新技術採用（LLM、ベクトル検索、Next.jsへの移行）"), alongside a design system shared across products ([product deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)).
- **Atlassian Statuspage** — a status page at [grafferstatus.jp](https://www.grafferstatus.jp/) lists AI Studio and Graffer Databridge (accessed 2026-10-11).

**From job postings (current HERP postings, accessed 2026-10-11; identical "開発環境" block in each):**

| Layer | Listed |
|---|---|
| Frontend | TypeScript; React, Next.js; AWS, Docker, Terraform; Storybook, Chromatic |
| Backend | Go, Python; Gin, Flask; AWS, Docker, Kubernetes; PostgreSQL, MySQL, MongoDB; GraphQL, REST, gRPC |
| Common | GitHub Actions, Argo (CI/CD); Sentry, Datadog; Figma; GitHub, Renovate; GitHub Copilot, Devin, Cursor, v0; Jira, GitHub Issues; Slack, Google Workspace, esa |

Source: [full-cycle engineer](https://herp.careers/v1/graffer/QE1EVzBa9GqT), [SRE](https://herp.careers/v1/graffer/8JGn2ARp6KPL), [Security Engineer](https://herp.careers/v1/graffer/7FDCJHZzT21G). The SRE and Security Engineer postings also name Google Cloud alongside AWS in their requirements; this is a hiring requirement only. The 2026-07 company deck lists GitHub Copilot, Cursor and Claude Code as tools in use. A 2025-10 release states that the company has required all development members to use generative-AI coding tools in principle since early 2023 ([2025-10-06](https://graffer.jp/news/6834)).

### Systems

| System | What it does | Source |
|---|---|---|
| Graffer スマート申請 | Form builder with templates and cross-municipality form sharing; AI generation of forms from uploaded paper templates; My Number Card identity verification (the privacy policy names the company's Graffer電子署名アプリ and Digital Agency's マイナアプリ); pre- and post-payment; CSV export and kintone integration | [page](https://graffer.jp/governments/solution-smart-apply), [privacy policy](https://graffer.jp/legal/privacy-policy) |
| Graffer Call | Push-dial IVR with AI routing to the right department, SMS URLs, bulk automated outbound calls with result tracking; a scenario editor for staff | [2024-08-16](https://graffer.jp/news/5898) |
| Graffer AI オペレーター | Speech recognition, answers from a registered knowledge base, transfer to staff with context, call summaries and transcripts | [2025-10-03](https://graffer.jp/news/6822) |
| Graffer AI Studio | Multi-model chat, RAG, Assistants API code execution ([2024-04-12](https://graffer.jp/news/5476)), task library ([2024-06-27](https://graffer.jp/news/5693)), image generation ([2025-09-30](https://graffer.jp/news/6811)), automatic model selection ([2025-10-30](https://graffer.jp/news/6880)), AI Labs ([2025-06-25](https://graffer.jp/news/6650)); daily backups stored in Japan for 7 days | [page](https://graffer.jp/ai-solution/products/graffer-ai-studio), [whitepaper](https://console.graffer.jp/aistudio/docs/whitepaper) |
| Graffer Databridge | Manufacturers upload specification sheets; an AI agent extracts the fields, converts units and flags gaps; wholesalers export to retailer-specific PDF or CSV with one click; in-system chat for correction requests | [2025-11-19](https://graffer.jp/news/6911) |
| Local-LLM document processing | Runs on a PC or on-premises without sending data to cloud LLMs; template-free extraction, mark reading (OMR), and sorting of results into auto / needs-review / undeterminable | [2026-06-03](https://graffer.jp/news/7414) |
| Document-review AI agent (MVP) | Reads basic designs and test plans, checks them against a checklist and proposes fixes; estimated up to 50% shorter reviews | [2026-05-28](https://graffer.jp/news/7405) |
| AI-driven legacy migration | Reverse-engineering source code into specification documents for a large enterprise's core-system cloud migration | [note, 2026-07-22](https://note.graffer.inc/n/naa4850501c58) |
| Platform internals | SRE duties include designing, building and running a microservice platform (multi-tenant architecture experience is a preferred skill); a separate infrastructure repository holds deployment configuration per environment | [SRE posting](https://herp.careers/v1/graffer/8JGn2ARp6KPL), [2022-12-08 interview](https://career.graffer.inc/inside-graffer/engineer-real-3) |

**Development organisation.** The company says that since founding, Product Managers and Product Developers have each taken features from problem discovery through requirements, design, implementation, testing, release and operation, without splitting the work by process ("プロダクト志向×多能工") ([product deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)). Since 2026-01 engineering has been led by 河治 (SVP of Engineering), with 黑﨑 leading AI Solution development ([Findy, 2026-06-17](https://findy-code.io/pick-up/interviews/graffer-engineer)). An "AI Driven Development" (AIDD) team handles contract development ([note, 2026-07-22](https://note.graffer.inc/n/naa4850501c58)). The Platform team covers security, SRE and shared backend infrastructure ([SRE posting](https://herp.careers/v1/graffer/8JGn2ARp6KPL)).

### Technical background sought

- **Full-cycle engineer** — required: cloud infrastructure use on AWS, GCP or Azure (personal use counts); full-stack development from frontend to backend (personal projects count); at least six months of continuous development and operation, including user enquiries, on one service; team development including code review. Preferred: writing requirements, basic-design documents, ADRs, PRDs or design docs; microservices or DDD; tests; building web services with generative AI; planning one's own web service; complex business-system domains; leading or managing engineering teams ([posting](https://herp.careers/v1/graffer/QE1EVzBa9GqT)).
- **SRE** — required: web application development; building and running container environments and clusters (Docker, Kubernetes); web and network security; infrastructure on AWS and Google Cloud; infrastructure as code (Terraform, CloudFormation); monitoring with tools such as Datadog. Preferred: microservice and multi-tenant architecture, Go, DevSecOps ([posting](https://herp.careers/v1/graffer/8JGn2ARp6KPL)).
- **Security Engineer** — required: web application development, cloud security monitoring and operations, deep web-security knowledge, incident response. Preferred: security-event auditing for microservices and on AWS / Google Cloud, secure programming in Go, SOC 2 or ISO certification work, automating corporate security through software ([posting](https://herp.careers/v1/graffer/7FDCJHZzT21G)).
- **Product Manager / senior full-cycle engineer** — required: planning, building, testing and running web products; having owned a product and its roadmap; leading decisions across UI design, engineering and marketing ([posting](https://herp.careers/v1/graffer/6tLzIUrHM_e-)).
- **Solution Director (AI Solution)** — required: system-development project management; system design from requirements to detailed design; DB, API and class/module design. Preferred: architecture and non-functional design (scalability, availability, security), SIer IT consulting, using generative AI in the development process ([posting](https://herp.careers/v1/graffer/hF0M8OCAIdqq)).

### Industry domain

Japanese local-government administration — resident procedures, the LGWAN network, My Number Card identity, municipal procurement, long-term-care insurance certification, public accounting — and, for the ministries business, national systems such as the 建設業法 hotline and Digital Agency's document review. The enterprise side covers food-distribution product data (食品規格書) and enterprise system migration. The careers FAQ states that prior knowledge of government is not required; most current staff had none before joining, and it is learned through onboarding and study sessions ([careers site](https://career.graffer.inc/)). A 2022 engineer interview describes features being specified with attention to personal-information and administrative-document handling rules ([interview](https://career.graffer.inc/inside-graffer/engineer-real-3)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Remote and location | Full remote possible; some teams set office days. Members work from Aomori to Okinawa and the company says it has run on "フルリモート・フルフレックス" since founding. Postings list the Sendagaya office as work location | [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao), [careers FAQ](https://career.graffer.inc/), [2025-11-27](https://career.graffer.inc/inside-graffer/beyond-remote-work) |
| Hours | Flextime with no core time; two-day weekends; national holidays and year-end holidays | [posting](https://herp.careers/v1/graffer/QE1EVzBa9GqT) |
| Salary (annual, including 45 hours/month of fixed overtime pay) | Full-cycle engineer ¥5.4M–¥12.0M; SRE ¥6.0M–¥12.0M; Security Engineer ¥7.2M–¥12.0M; PdM / senior engineer ¥7.8M–¥15.0M; Solution Director ¥7.8M–¥10.8M | [HERP postings](https://herp.careers/v1/graffer); accessed 2026-10-11 |
| Equity | "ストックインセンティブ制度": a fixed amount is deducted from monthly salary to buy company shares | [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| Pay reviews and HR system | Pay revised monthly; role-grade system; monthly real-time evaluation with no rating scale | [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao), [careers FAQ](https://career.graffer.inc/) |
| Benefits | ¥50,000 remote-setup allowance in the first month; ¥30,000 monthly productivity allowance; company-leased housing; book subsidy; team-lunch subsidy; 関東ITソフトウェア健康保険組合; parental leave (taken) | [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao), [posting](https://herp.careers/v1/graffer/QE1EVzBa9GqT) |
| Onboarding | Engineer bootcamp customised per person; three-month buddy system | [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| Side jobs | Allowed with approval, subject to listed rules | [careers FAQ](https://career.graffer.inc/) |
| Probation | Three months, with no change in conditions | [posting](https://herp.careers/v1/graffer/QE1EVzBa9GqT) |
| Selection | Document screening, 1–3 interviews, offer meeting; final interview and offer meeting at the office in principle; about 3–4 weeks | [careers FAQ](https://career.graffer.inc/) |
| Juniors and interns | The product deck states full-stack experience is not required for Product Developers at entry, and that several members joined with 2–4 years of experience; an Intern job group exists | [product deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian), [careers site](https://career.graffer.inc/) |
| Working language and visa | Not stated; no English-language posting found | See `Notes` |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11): graffer.jp (both sitemaps, company, about, governments and product pages, ministries, services, AI Solution pages, all 51 pages of the news index, legal pages and the Platform whitepaper); the AI Studio whitepaper on console.graffer.jp; career.graffer.inc and its Inside Graffer posts; all ten HERP postings; note.graffer.inc (13 posts); Speaker Deck (5 decks); the PR TIMES company page; the GitHub API; Qiita; Zenn; TokyoDev; Japan Dev; Wantedly; the NTA corporate number site; the ISMS registry; INITIAL and HERP company profiles as leads; BRIDGE; Findy. Names searched: グラファー, 株式会社グラファー, Graffer, Graffer, Inc., and product names, in Japanese and English.

- **Revenue and profit.** No figures were found in releases, decks or the company site. The official gazette (官報) was not searched for 決算公告.
- **Valuation.** Not published by the company. INITIAL shows an estimated post-money valuation of ¥10,810M as of 2023-04-26 ([INITIAL](https://initial.inc/companies/A-30003)), and HERP shows "評価額 101.9 億円" ([HERP profile](https://herp.careers/careers/companies/graffer)). Both are database estimates.
- **Amounts after 2021.** The Change Holdings investment and any later rounds; the prices paid for 行政システム研究所, 5Minutes and the KURASERU business.
- **Engineering headcount.** The deck gives 81 employees in total; no engineering breakdown was found.
- **Pricing.** No price list for Graffer Platform services or Graffer AI Studio; only the task-specific AI agent service publishes a price structure.
- **Engineering blog.** There is no dedicated engineering blog. Technical content appears in Speaker Deck talks, the careers site and note posts. The [Qiita organization](https://qiita.com/organizations/graffer) has 27 posts, the latest dated 2019-10-01. No Zenn publication was found.
- **Open source.** The GitHub organization [`graffer-inc`](https://github.com/graffer-inc) ("A Tokyo-based Government Tech Startup", created 2017-12-01) has 13 public repositories. Twelve are forks; the single original, `react-native-compressed-jsbundle-expo-module`, was last pushed 2024-12-24.
- **Working language, visa sponsorship, English roles.** Not stated. No Graffer listing was found on TokyoDev or Japan Dev (the Japan Dev company URL returned 404).
- **LGWAN-ASP registration.** Company pages describe LGWAN support, but the J-LIS service list returned HTTP 403 and was not verified.
- **Turnover.** Not published.

### Inconsistencies across sources

- **Government footprint.** "270団体超" with about 70 million residents (company deck, as of 2026-03), while slide 14 of the same deck says "4,000万人超の人口カバー / 導入団体270+" ([deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). Other figures: "250超の自治体導入 / 7,000万人以上" (the same deck's service map and the [about page](https://graffer.jp/about)); "全国250以上の自治体" ([2026-04-28](https://graffer.jp/news/7317), [2026-06-30](https://graffer.jp/news/7505)); 273 organisations and over 41 million residents ([2025-07-31 deck](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge)); "7215 万人" and "254 の政府機関" ([governments page](https://graffer.jp/governments); accessed 2026-10-11). The sources use different units — municipalities, organisations, government bodies with projects — and none defines its count.
- **Capital including reserve.** ¥975,000,313 ([2020-07-16](https://graffer.jp/news/1754)); ¥2,205,721,759 ([2021-04-01](https://graffer.jp/news/2679)); ¥1,798,276,785 ([2023-04-14](https://graffer.jp/news/4516)); ¥1,544,977,927 ([2024-10-24](https://graffer.jp/news/6054) onwards and the [company page](https://graffer.jp/company)). The figure falls after 2021; no release explaining the decreases was found. PR TIMES shows "15億4497万円" without the reserve qualifier ([PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/38525)).
- **Cumulative funding.** The disclosed 2019 rounds sum to 6.3億円, while the Series A release states 約7.2億円 cumulative. 7.2 + 2.5 + 12 億円 gives 21.7億円, against the Series B release's 約22.2億円 ([2019-12-20](https://graffer.jp/news/1524), [2021-04-01](https://graffer.jp/news/2679)). HERP shows "累計調達額 29.1 億円", estimated from registry filings ([HERP profile](https://herp.careers/careers/companies/graffer)).
- **2019-01 instrument.** The company release calls it 資金調達 from three investor groups ([release](https://graffer.jp/news/735)); BRIDGE corrected its article to say it was a J-KISS (stock acquisition rights) round led by 500 Startups Japan ([BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising)).
- **Graffer Call launch.** The product deck timeline dates the Graffer Call release to 2023-06 ([product deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)). The release announcing "提供を開始" is dated [2024-08-16](https://graffer.jp/news/5898), after an adoption by 大東市 announced on [2024-07-22](https://graffer.jp/news/5791).
- **Head-office move.** The 2019-12-20 release says the head office moved from Jingumae to Sendagaya in June 2019 ([release](https://graffer.jp/news/1524)). The NTA record dates the registered address change to 2019-11-01 ([NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779)).
- **Book release date.** 2026-02-15 ([2026-02-16](https://graffer.jp/news/7137), [AI Solution site](https://graffer.jp/ai-solution)) versus "2026/2/12発刊" ([2026-07-28](https://graffer.jp/news/7552)).

### Other

- **Shift in business mix.** The company started with consumer and business services for administrative paperwork (くらしのてつづき, Grafferフォーム, 法人証明書請求), moved to municipal SaaS from 2018, added enterprise generative AI from 2023, and announced Food & Beverage and AI-driven development as separate domains with the 2026-01 mission change ([2019-01-21](https://graffer.jp/news/735), [2025-02-27](https://graffer.jp/news/6473), [company deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)). The careers site states the company works across "行政・食品流通・AI駆動開発" ([careers site](https://career.graffer.inc/)).
- **Acquisitions.** Since 2024 the company has bought one business and two companies: KURASERU's care-certification enquiry system (2024-10), 行政システム研究所 (2026-04) and 5Minutes (2026-06). The 2024-10 release states it will continue to pursue M&A and alliances ([2024-10-24](https://graffer.jp/news/6054)).
- **Security incidents disclosed.** On [2020-10-27](https://graffer.jp/news/1987) the company reported that a file-setting error on a Graffer 手続きガイド page for Toshima Ward's childcare section made information entered by users viewable online from 2020-10-01 (3 cases, 16 people). On [2020-04-29](https://graffer.jp/news/1661) it reported a temporary stop of certificate requests on Graffer 法人証明書請求. The AI Studio page states "サービス開始からセキュリティインシデントや大規模障害発生なし" ([page](https://graffer.jp/ai-solution/products/graffer-ai-studio); accessed 2026-10-11).
- **Public documentation.** Security whitepapers for both product lines are public ([Platform](https://graffer.jp/legal/whitepaper), [AI Studio](https://console.graffer.jp/aistudio/docs/whitepaper)); no public API reference was found.
- **Press channels.** The [news index](https://graffer.jp/news) and [PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/38525) were both checked. Some PR TIMES items, such as the 2025-10-07 AI agent pricing release, were not found in the site's news index.

---

## Resources

**Official**

- [Corporate site (JA)](https://graffer.jp/) · [Company page — board, management, capital, certifications](https://graffer.jp/company) · [About / founder message](https://graffer.jp/about)
- [News index](https://graffer.jp/news)
- [Graffer Platform — government products](https://graffer.jp/governments): [スマート申請](https://graffer.jp/governments/solution-smart-apply) · [手続きガイド](https://graffer.jp/governments/solution-guides) · [窓口予約](https://graffer.jp/governments/solution-booth-reserve) · [Call](https://graffer.jp/governments/solution-call) · [AI オペレーター](https://graffer.jp/governments/solution-ai-operator) · [要介護認定照会](https://graffer.jp/governments/solution-nintei-shoukai) · [認定調査票作成](https://graffer.jp/governments/solution-nintei-chosahyo) · [お悩みハンドブック](https://graffer.jp/governments/solution-compass)
- [Ministries page](https://graffer.jp/ministries) · [Individual and business services](https://graffer.jp/services)
- [Graffer AI Solution](https://graffer.jp/ai-solution): [AI Studio](https://graffer.jp/ai-solution/products/graffer-ai-studio) · [Task-specific AI agents](https://graffer.jp/ai-solution/ai-consulting-development) · [AI駆動開発プログラム](https://graffer.jp/ai-solution/generative-ai-learning/ai-dev-training) · [Databridge for 食品規格書](https://graffer.jp/ai-solution/ai-databridge/food-kikaku)
- [Graffer Platform security whitepaper](https://graffer.jp/legal/whitepaper) · [Graffer AI Studio security whitepaper](https://console.graffer.jp/aistudio/docs/whitepaper) · [Privacy policy](https://graffer.jp/legal/privacy-policy) · [Status page](https://www.grafferstatus.jp/)
- [Careers site](https://career.graffer.inc/) · Inside Graffer: [remote work, 2025-11-27](https://career.graffer.inc/inside-graffer/beyond-remote-work) · [engineer interview, 2022-12-08](https://career.graffer.inc/inside-graffer/engineer-real-3) · [conference report, 2025-10-09](https://career.graffer.inc/inside-graffer/developer_conference_2025)
- [HERP job board](https://herp.careers/v1/graffer): [full-cycle engineer](https://herp.careers/v1/graffer/QE1EVzBa9GqT) · [SRE](https://herp.careers/v1/graffer/8JGn2ARp6KPL) · [Security Engineer](https://herp.careers/v1/graffer/7FDCJHZzT21G) · [PdM / senior engineer](https://herp.careers/v1/graffer/6tLzIUrHM_e-) · [Solution Director](https://herp.careers/v1/graffer/hF0M8OCAIdqq)
- Speaker Deck: [company deck (version 2026-07)](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) · [product development deck](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian) · [AI-first development, 2025-07-31](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge) · [full-cycle development talk, 2026-06-17](https://speakerdeck.com/graffer/sono-yue-jing-wu-li-sitemasen-fdenoxian-niaruhurusaikurukai-fa)
- note: [sovereign AI build, 2026-07-10](https://note.graffer.inc/n/nd0a48a1d33e0) · [AIDD engineer, 2026-07-22](https://note.graffer.inc/n/naa4850501c58)
- [GitHub organization](https://github.com/graffer-inc) · [Qiita organization](https://qiita.com/organizations/graffer)

**Press releases (graffer.jp, JA — newest first)**

- [Fukuoka AI subsidy screening — 2026-08-31](https://graffer.jp/news/7705) · [Miyakonojo 認定調査票作成 pilot — 2026-08-28](https://graffer.jp/news/7697) · [Ishii joins Cabinet personnel study group — 2026-07-28](https://graffer.jp/news/7552)
- [5Minutes acquisition — 2026-06-30](https://graffer.jp/news/7505) · [Sovereign AI environment — 2026-06-22](https://graffer.jp/news/7451) · [Osaka AI agent consortium — 2026-06-18](https://graffer.jp/news/7446) · [Local LLM technology — 2026-06-03](https://graffer.jp/news/7414) · [Databridge for 国分西日本 — 2026-06-02](https://graffer.jp/news/7409)
- [MLIT hotline results — 2026-05-29](https://graffer.jp/news/7399) · [Digital Agency document-review AI agent — 2026-05-28](https://graffer.jp/news/7405) · [行政システム研究所 acquisition — 2026-04-28](https://graffer.jp/news/7317) · [Ricoh — 2026-03-10](https://graffer.jp/news/7211) · [Book release — 2026-02-16](https://graffer.jp/news/7137) · [Minato Ward pilot — 2026-01-06](https://graffer.jp/news/7035)
- [ROUTE06 alliance — 2025-12-02](https://graffer.jp/news/6970) · [Databridge announced — 2025-11-19](https://graffer.jp/news/6911) · [Digital Marketplace — 2025-11-17](https://graffer.jp/news/6904) · [AI Studio model auto-selection — 2025-10-30](https://graffer.jp/news/6880) · [AI駆動開発プログラム — 2025-10-06](https://graffer.jp/news/6834) · [Minato Ward selects AI オペレーター — 2025-10-03](https://graffer.jp/news/6822)
- [AI Studio image generation — 2025-09-30](https://graffer.jp/news/6811) · [MLIT hotline project — 2025-08-21](https://graffer.jp/news/6737) · [Graffer Call call recording — 2025-07-29](https://graffer.jp/news/6699) · [AI Labs — 2025-06-25](https://graffer.jp/news/6650) · [ISO 27017 / 27001 — 2025-06-06](https://graffer.jp/news/6618) · [Kyoto Graffer Call — 2025-05-30](https://graffer.jp/news/6613) · [Tokyo Fire Department integration — 2025-04-22](https://graffer.jp/news/6589)
- [Accessibility good practice 2024 — 2025-03-19](https://graffer.jp/news/6490) · [法人証明書請求 shutdown — 2025-02-27](https://graffer.jp/news/6473) · [Mr Max — 2025-02-26](https://graffer.jp/news/6439) · [Findy Team+ Award 2024 — 2024-11-01](https://graffer.jp/news/6095) · [KURASERU business transfer — 2024-10-24](https://graffer.jp/news/6054) · [Graffer Call — 2024-08-16](https://graffer.jp/news/5898)
- [Daito Graffer Call — 2024-07-22](https://graffer.jp/news/5791) · [AI task library — 2024-06-27](https://graffer.jp/news/5693) · [AI Studio Assistants API — 2024-04-12](https://graffer.jp/news/5476) · [Startup association director — 2024-02-06](https://graffer.jp/news/5276) · [Outside director 中谷 — 2023-11-01](https://graffer.jp/news/5053) · [TOPPAN group — 2023-10-12](https://graffer.jp/news/4924)
- [Azure OpenAI knowledge base — 2023-08-24](https://graffer.jp/news/4830) · [AI Studio GA — 2023-04-26](https://graffer.jp/news/4561) · [Change Holdings alliance — 2023-04-14](https://graffer.jp/news/4516) · [AI Studio announced — 2023-03-24](https://graffer.jp/news/4389) · [お悩みハンドブック municipal version — 2022-12-15](https://graffer.jp/news/4081)
- [ISMAP withdrawal — 2022-04-01](https://graffer.jp/news/3504) · [お悩みハンドブック 100,000 users — 2022-02-16](https://graffer.jp/news/3381) · [お悩みハンドブック national — 2022-01-27](https://graffer.jp/news/3297) · [J-Startup — 2021-10-20](https://graffer.jp/news/3080) · [Shiga joint procurement — 2021-09-03](https://graffer.jp/news/2935) · [窓口予約 — 2021-09-01](https://graffer.jp/news/2928)
- [Series B and CFO — 2021-04-01](https://graffer.jp/news/2679) · [Fukuoka City — 2021-03-30](https://graffer.jp/news/2648) · [Privacy Mark — 2021-03-12](https://graffer.jp/news/2581) · [Toshima incident report — 2020-10-27](https://graffer.jp/news/1987) · [TOPPAN alliance — 2020-07-16](https://graffer.jp/news/1754) · [法人証明書請求 stop — 2020-04-29](https://graffer.jp/news/1661)
- [スマート申請 launch — 2020-04-07](https://graffer.jp/news/1616) · [法人証明書請求 10,000 companies — 2020-02-26](https://graffer.jp/news/1561) · [Series A and Kobe office — 2019-12-20](https://graffer.jp/news/1524) · [Govtech Trends — 2019-08-23](https://graffer.jp/news/1402) · [Yahoo! JAPAN alliance — 2019-08-19](https://graffer.jp/news/1396) · [1.8億円 round — 2019-01-21](https://graffer.jp/news/735) · [Kamakura 手続きガイド — 2018-11-01](https://graffer.jp/news/405)

**PR TIMES (JA)**

- [Company page](https://prtimes.jp/main/html/searchrlp/company_id/38525) · [Task-specific AI agents with pricing — 2025-10-07](https://prtimes.jp/main/html/rd/p/000000103.000038525.html)

**Third-party coverage, registers and profiles**

- [NTA corporate number record — 9010401132779 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779) · [NTA record — ｇｒａｐｈｅｒ株式会社 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011201021353)
- [ISMS registry — IS 689557 (JA)](https://isms.jp/lst/ind/CR_IS_x0020_689557.html)
- [BRIDGE — 1.8億円 round, 2019-01-21 (JA)](https://thebridge.jp/2019/01/graffer-fundraising)
- [Findy — interview with 河治 and 黑﨑, 2026-06-17 (JA)](https://findy-code.io/pick-up/interviews/graffer-engineer)
- [HERP company profile (JA)](https://herp.careers/careers/companies/graffer) · [INITIAL (JA)](https://initial.inc/companies/A-30003)
