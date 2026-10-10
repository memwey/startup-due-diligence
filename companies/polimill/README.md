# Polimill

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Polimill (Polimill株式会社, read ポリミル; corporate number 5010401158530) is a Tokyo company incorporated on 2021-02-25. It runs two products: **QommonsAI** (コモンズAI), a generative-AI platform for Japanese local governments and other public bodies that cross-searches published administrative documents and lets staff switch between models from OpenAI, Anthropic, Google and Preferred Networks; and **Surfvote** (サーフボート), a social-network-style service, launched in 2021, where users vote and comment on social and policy "issues". QommonsAI is free up to 1,000 accounts per organisation ([product site](https://info.qommons.ai/); accessed 2026-10-11).

- About 1,100 municipalities and 600,000 staff use QommonsAI ("全国約1,100自治体・60万人の職員が利用しています", as of 2026-08-31, [product site](https://info.qommons.ai/)). The company projects about 1,200 municipalities and 650,000 users for December 2026 ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)). All counts are company-stated.
- Latest round: シリーズA of about ¥635M (約6億3,500万円) — ¥520M from venture capital, about ¥15M from management and angels, and ¥100M of debt from a megabank — at a stated post-money valuation of about ¥5B ([2026-01-19](https://polimill.jp/20260119-1/)). No investor is named. The previous プレシリーズA brought cumulative funding to "5億円超え" ([2024-10-03](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)).
- Before October 2025 the company had 4 full-time employees; it hired 6 more in October–November 2025 ([2025-11-05](https://polimill.jp/20251105-1/)). In October 2026 recruiting interviews, the development department is "15名ほど" (about 15) and the organisation "数十人規模" (a few dozen people) ([talk03](https://polimill.jp/interview/talk03/), [talk02](https://polimill.jp/interview/talk02/); 2026-10-02).
- Engineering: data is stored on AWS in Tokyo with failover to Osaka ([FAQ](https://info.qommons.ai/faq); accessed 2026-10-11). GPT models run on Azure OpenAI in the Japan region ([2026-05-08](https://polimill.jp/20260508-4/)). The web app returns `x-powered-by: Next.js` from behind Amazon CloudFront (observed 2026-10-11). The development team is multinational and remote, and its common language is Japanese ("共通言語は日本語ですが多国籍", [talk03](https://polimill.jp/interview/talk03/)). The backend posting requires JLPT N1 from non-native speakers ([Green](https://www.green-japan.com/company/10658/job/285168); posted 2025-05-30).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | Polimill株式会社 (registry: Ｐｏｌｉｍｉｌｌ株式会社, フリガナ ポリミル); site footer "Polimill Co.,Ltd." | [NTA registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530), [company page](https://polimill.jp/company/) |
| Corporate number | 5010401158530; assigned 2021-03-04 (令和3年3月4日) | [NTA registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530) |
| Founded | 2021-02-25 (設立) | [2021-11-30](https://polimill.jp/pr20211130/), [2026-02-25](https://polimill.jp/20260225-1/) |
| HQ | 東京都港区虎ノ門3丁目8番27号 巴町アネックス2号館3階 (registered 2026-03-24) | [NTA registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530), [company page](https://polimill.jp/company/) |
| Registered address history | 浜松町2-2-15 浜松町ダイヤビル2F (at registration) → 赤坂8-4-14 青山タワープレイス8F (from 2021-03-31) → 六本木7-14-23 ラウンドクロス六本木 (from 2024-04-12) → 虎ノ門 (from 2026-03-24) | [NTA registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530) |
| Representatives | 代表取締役CEO 伊藤あやめ and 代表取締役COO 谷口野乃花, both appointed March 2025 | [company page](https://polimill.jp/company/), [talk01](https://polimill.jp/interview/talk01/), [talk02](https://polimill.jp/interview/talk02/) |
| Representative at founding | 代表取締役 横田えり, named in releases from 2021 to March 2025 | [2021-11-30](https://polimill.jp/pr20211130/), [2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html) |
| Stated business | 「この国の社会の全体最適化」 ("overall optimisation of this country's society") | [company page](https://polimill.jp/company/) |
| Mission | 「のこしたいみらいをともにつくる」, adopted at an internal 第一回京都会議 | [2025-12-05](https://polimill.jp/20251205-1/), [about](https://polimill.jp/about/) |
| Capital | ¥600M (資本金6億円); see `Notes` for a conflicting figure | [PR TIMES company box](https://prtimes.jp/main/html/rd/p/000000435.000088829.html); Undated; accessed 2026-10-11 |
| Headcount | 4 full-time employees plus 6 hires in Oct–Nov 2025; "数十人規模" in Oct 2026 | [2025-11-05](https://polimill.jp/20251105-1/), [talk02](https://polimill.jp/interview/talk02/) |
| Engineering working language | Development department: Japanese as the common language, multinational members, remote | [talk03](https://polimill.jp/interview/talk03/) (2026-10-02) |
| Customers | About 1,100 municipalities and 600,000 staff on QommonsAI as of 2026-08-31 | [product site](https://info.qommons.ai/) |
| Total raised | "5億円超え" after the プレシリーズA (2024-10-03); シリーズA of about ¥635M (2026-01-19). No cumulative total after the シリーズA is stated | [2024-10-03](https://prtimes.jp/main/html/rd/p/000000435.000088829.html), [2026-01-19](https://polimill.jp/20260119-1/) |
| Investors | Not named in any company release reviewed | see `Funding` |
| ISMS | ISO/IEC 27001:2022 / JIS Q 27001:2023, IS 823638, BSIグループジャパン, registered 2025-10-07; scope covers public-sector AI and the citizen SNS | [2025-10-09](https://polimill.jp/20251009-1/) |
| QMS | ISO 9001:2015, FS 826724, BSIグループジャパン, registered 2025-08-15 | [2025-10-09](https://polimill.jp/20251009-2/) |
| Privacy Mark | 第10825416(01)号, JIPDEC, valid 2025-10-01 to 2027-09-30 | [2025-10-10](https://polimill.jp/20251010-1/) |
| Other security status | ISO/IEC 27017:2015 listed as held; ISMAP "現在取得手続き中" (in process) | [FAQ](https://info.qommons.ai/faq), [security policy](https://info.qommons.ai/info/security) (revised 2026-10-01) |

**Government programmes and recognition.** The company says it was listed in METI's 「行政と連携実績のあるスタートアップ100選」 ([2023-04-25](https://polimill.jp/pr20230425/)). Other recognition: its legal-text AI 「コモンズLawScopeAI」 won a 優秀賞 at a Digital Agency hackathon ([2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html)); it was contracted by the Digital Agency, after a 公募型プロポーザル, for 「法制事務における生成AIの活用等に関する技術検証」, with the contract signed 2025-05-20 ([2025-06-02](https://prtimes.jp/main/html/rd/p/000000520.000088829.html)); and it was one of 4 projects selected from 16 applicants for MIC's 「公共分野における信頼できるAIを用いた開発実証事業」, as the representative organisation for a PLaMo evaluation in five Hyogo municipalities ([MIC, 2026-06-08](https://www.soumu.go.jp/menu_news/s-news/01tsushin03_02000462.html)). COO 谷口野乃花 was named to Forbes 30 Under 30 Asia 2026 in the AI category ([2026-06-04](https://polimill.jp/20260604-1/)).

### Context as stated by the company

- The 5th-anniversary release cites 744 municipalities classed as "消滅可能性自治体" (at risk of disappearing) out of 1,729, record-low public-sector recruitment, and the loss of tacit knowledge as veteran staff retire. It presents the free core product as a long-horizon choice, framed as "social discounting" rather than exponential discounting ([2026-02-25](https://polimill.jp/20260225-1/)).
- The シリーズA release states the aim "予算の制約でAIが使えない自治体をゼロにする" (no municipality left unable to use AI for budget reasons) and says the business model does not rely on usage fees ([2026-01-19](https://polimill.jp/20260119-1/)).

---

## Product

### QommonsAI

The product site describes it as "全国の行政文書を、根拠ごと引き出せる。1,000アカウントまで無料の、自治体のための生成AI。" (nationwide administrative documents with their evidence; generative AI for municipalities, free up to 1,000 accounts) ([product site](https://info.qommons.ai/); accessed 2026-10-11).

**Origins.** In March 2024 the company began a free beta of a ministry/municipality support AI called 【DIGITAL COMMONS】. It used ChatGPT as the beta interface and AWS for data processing ([2024-03-13](https://polimill.jp/2024031301-2/)). A QommonsAI preview went to 17 基礎自治体 and 4 広域自治体, and the company said about 50 municipalities and ministries were contracted at release ([2024-08-02](https://prtimes.jp/main/html/rd/p/000000418.000088829.html)). The product version followed, with 100 free accounts ([2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html)). The company's new-year release says development began in March 2024 and the product was released in July 2024 ([2025-01-06](https://prtimes.jp/main/html/rd/p/000000484.000088829.html)). No release explicitly states that DIGITAL COMMONS was renamed QommonsAI.

Feature areas, as organised on the [function page](https://info.qommons.ai/function) and [FAQ](https://info.qommons.ai/faq) (accessed 2026-10-11):

| Area | What the product pages state |
|---|---|
| Model selection | Models from OpenAI, Anthropic, Google and Preferred Networks, switchable mid-conversation. The FAQ lists GPT-5.4, GPT-5.4 mini, Claude Opus 4.6, Claude Sonnet 4.6, Claude Haiku 4.5, Gemini 3.1 Pro, Gemini 3 Flash and others, plus PLaMo 2.2 Prime; some are marked as domestic-region models |
| Nationwide administrative knowledge | Published documents from central ministries, all 47 prefectures and municipalities (assembly minutes, plans, ordinance materials), plus academic papers and white papers. Answers cite municipality, assembly, date and source link. Polimill collects and updates the data. Legal search uses an in-house "LawChunker", stated at 98% accuracy (2.1x the previous method) |
| Seven specialist AIs | 議会対応AI (assembly Q&A), 行政文書AI (e-Gov法令, via the e-Gov database and official API), 公共サービスサポートAI, 社会福祉AI, 「住民の声」返信サポートAI (resident-reply drafts of up to 300 characters), プライベートナレッジAI, QommonsAI Talk (general chat). Each has its own data source and system prompt |
| Private knowledge (RAG) | Four drive types, up to five folder levels, three roles (super-admin / admin / member). Accepts PDF, Word, Excel, PowerPoint, CSV, text and images, with OCR of scanned PDFs and slide images. 100GB free for 基礎自治体, 300GB for 広域自治体 |
| Deep Research | Iterative search across in-house documents, the national administrative knowledge base and the web, producing a cited report |
| Image generation | Multiple models with 4K output; unavailable on LGWAN |
| Admin and safety | PII detection by pattern and by AI, in warn or block mode; 100+ admin-defined banned words; CIDR IP allow-lists; per-municipality tenant separation; usage dashboards, automatic monthly reports and CSV export of input/output logs |
| LGWAN | LGWAN-ASP access since April 2026 via 株式会社シナジー's data centre. Only text and screen information crosses the boundary. Image generation, file upload and download, and outbound links are unavailable on LGWAN |
| Training | Three tiers (初級/中級/上級); free slots for the first two are allocated by lottery |

**Commercialization.**

- *Free tier.* Up to 1,000 accounts per organisation with no time limit and, below that threshold, no token or conversation cap ([price page](https://info.qommons.ai/price), [FAQ](https://info.qommons.ai/faq); accessed 2026-10-11). The free tier was 100 accounts at product launch and rose to 1,000 in ver.2.1 ([2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html), [2025-10-02](https://polimill.jp/20251002-1/)).
- *Above 1,000 accounts.* A release published a stepped monthly price for each additional 1,000 accounts and stated no usage cap ([2026-01-09](https://polimill.jp/20260109-1/)). The current price page instead says a plan is proposed according to user numbers, and the FAQ says monthly usage is capped above 1,000 accounts (accessed 2026-10-11).
- *LGWAN.* No extra charge ([2025-12-08](https://polimill.jp/20251208-1/), [2026-01-09](https://polimill.jp/20260109-1/)).
- *Training and support.* Paid training per session and a monthly "AI導入伴走支援 Light" support plan have a published price list ([price page](https://info.qommons.ai/price)). Earlier releases described free on-site training anywhere in Japan ([2025-07-23](https://polimill.jp/20250723-1/)).
- *Payment and sales channel.* Government customers pay by invoice. A separate enterprise/individual edition is priced per account per month, from 10 accounts, with card payment available ([commerce-law page](https://info.qommons.ai/info/commerce-law), [enterprise price page](https://info.qommons.ai/business_personal/price)). The product is sold directly to every municipality, without resellers ("代理店を介さない直販体制") ([function page](https://info.qommons.ai/function)).
- *Stated revenue model.* "QommonsAIの収益モデルは、利用料ではありません" (QommonsAI's revenue model is not usage fees): the company points to an ecosystem built around the Qommons ONE app store and future tiers ([2026-01-09](https://polimill.jp/20260109-1/)).
- *Planned agent version.* Billing would be per completed production run (SBE), at a unit price fixed for the contract year ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)).

### Surfvote

A social-network-style service where users vote among options on "issues" (イシュー) and comment. Issues are written by staff, academics, experts and municipalities, and the company says results are submitted to ministries and politicians as appropriate ([2023-04-25](https://polimill.jp/pr20230425/)). It launched in September 2021 with Twitter login ([2022-12-13](https://polimill.jp/pr2022121302/), [2021-10-26](https://polimill.jp/pr20211026/)). Later additions include email registration and a PC version ([2021-11-30](https://polimill.jp/pr20211130/)), a SaaS edition used in national-university classes ([2022-05-31](https://polimill.jp/pr20220531/)), and 「Surfvoteローカル」 for municipalities, first used by 奈良県田原本町 from 2022-11-24 ([2022-12-13](https://polimill.jp/pr2022121302/)). Yokohama states that its ward-level opinion collection on Surfvote is provided by Polimill and 株式会社トラストアーキテクチャ under a contract with the city ([Yokohama, updated 2026-06-01](https://www.city.yokohama.lg.jp/city-info/koho-kocho/kocho/dp/dpkekka/R07dpkekka.html)). No public Surfvote price list was found.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2021-11-30 | Surfvote: 74 issues | [release](https://polimill.jp/pr20211130/) |
| 2024-08-02 | QommonsAI preview: about 50 municipalities and ministries contracted | [release](https://prtimes.jp/main/html/rd/p/000000418.000088829.html) |
| 2024-11-30 | QommonsAI: 100 municipalities and ministries within three months of release | [release](https://prtimes.jp/main/html/rd/p/000000470.000088829.html) |
| 2025-01-06 | Surfvote: 700+ issues published in total | [release](https://prtimes.jp/main/html/rd/p/000000484.000088829.html) |
| 2025-07-23 | QommonsAI: about 300 municipalities; about 60 new each month | [release](https://polimill.jp/20250723-1/) |
| 2025-08-06 | Surfvote: 500,000 monthly page views | [release](https://polimill.jp/20250806-2/) |
| 2025-12-31 | QommonsAI: about 600 municipalities, about 200,000 users; Surfvote: 600,000 monthly PV | [annual summary](https://polimill.jp/20251231-1/) |
| 2026-02-25 | QommonsAI: about 700 municipalities, about 250,000 staff; Surfvote: 800,000 monthly PV | [5th anniversary](https://polimill.jp/20260225-1/) |
| 2026-04 | QommonsAI: about 800 municipalities, about 300,000 staff | [2026-05-08](https://polimill.jp/20260508-4/) |
| 2026-07 | QommonsAI: 1,050 "自治体・パブリックセクター", about 550,000 staff | [Wantedly](https://www.wantedly.com/projects/2420681); accessed 2026-10-11 |
| 2026-08-31 | QommonsAI: about 1,100 municipalities, 600,000 staff | [product site](https://info.qommons.ai/) |

The company describes QommonsAI as "導入シェアNo.1" (No.1 adoption share), qualified as "当社2026年1月調べ、他サービスとバンドルされていない単体プロダクトにおいて" (company survey of January 2026, among standalone products not bundled with other services) ([2026-01-19](https://polimill.jp/20260119-1/)).

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2024-07-09](https://polimill.jp/2024071901-2/) | 奈良県田原本町 | Partnership agreement and QommonsAI trial; the release calls it the first in Nara |
| [2025-03-17](https://prtimes.jp/main/html/rd/p/000000506.000088829.html) | 大阪府阪南市 | Business partnership agreement following a QommonsAI trial |
| [2025-05-14](https://polimill.jp/qommonsai_0514_2025/) | Preferred Networks | PLaMo Prime added as a standard model, offered to about 150 municipalities |
| [2025-06-02](https://prtimes.jp/main/html/rd/p/000000520.000088829.html) | Digital Agency | Technical verification of generative AI for legislative drafting work (法制事務) |
| [2026-02-27](https://polimill.jp/20260227-1/) | 株式会社シナジー (Okinawa) | Joint LGWAN connection service from April 2026; planned integration with its document-management system 「ActiveCity」 |
| [2026-04-20](https://kyodonewsprwire.jp/release/202604207739) | 兵庫県尼崎市 | City release: partnership agreement signed 2026-04-24, described as the first by a 中核市 (core city) |
| [2026-05-08](https://polimill.jp/20260508-4/) | 日本マイクロソフト | Azure OpenAI Japan region adopted for GPT-5.4; described as the first joint initiative |
| [2026-06-30](https://polimill.jp/20260630-1/) | MIC; 兵庫県 with 姫路市, 尼崎市, 加西市, 加東市 and 多可町 | Evaluation of PLaMo 3.0 Prime on QommonsAI in live municipal work, June 2026 – March 2027 (planned) |
| [2026-09-25](https://polimill.jp/20260925/) | 香川県 中讃広域圏 (2 cities, 3 towns) and its administrative association | Simultaneous generative-AI agreements |

Further municipal agreements announced in 2025–2026 include 和光市, 日進市, 大崎市, 野辺地町, 苫小牧市, 多可町, 小牧市 and 河内長野市 (see the [press index](https://polimill.jp/news/)). Of the 152 items dated 2026 in the company's [PR TIMES feed](https://prtimes.jp/main/html/searchrlp/company_id/88829), 89 have 研修 (training) in the title, mostly reports of QommonsAI training at individual municipalities (title count, 2026-10-11).

### Stated plans

- **Use of シリーズA funds** ([2026-01-19](https://polimill.jp/20260119-1/)): (1) Qommons ONE development and partners; (2) nationwide sales and support toward 1,200 municipalities and 800,000 users in 2026; (3) R&D on "QommonsAI Pro", "Qommons Connect" and "QommonsAI Advance"; (4) a data platform combining GraphRAG with an administrative ontology (行政オントロジー); (5) trials of humanoid robots in public services.
- **Qommons ONE** — an app store inside QommonsAI. Partner apps connect via MCP, either as data provided to Polimill or as partner-run MCP servers. Partners go through a four-axis review and sandbox testing ([2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)). The October 2026 release says it opens at the end of October 2026 and targets about 100 apps during 2027 ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)). Earlier dates are listed in `Notes`.
- **QommonsAI 3.0 エージェント版** (agent version), planned for January 2027. Staff define a task in natural language, and the workflow is driven by code plus a "判断モデル" (decision model) for branching, with an LLM generating text only at the end. Per-step settings choose AI processing or human confirmation, with approval routes. It adds event triggers and sandbox runs, and connects to external services via MCP ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)).
- **全国行政AXレポジトリ** — a shared repository of standardised municipal task templates, planned for April 2027 with free participation ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)).

---

## Founder

The company page lists five officers under 役員紹介 ([company page](https://polimill.jp/company/); accessed 2026-10-11). Appointment dates come from the company's recruiting interviews ([talk01](https://polimill.jp/interview/talk01/), 2026-09-18; [talk02](https://polimill.jp/interview/talk02/), [talk03](https://polimill.jp/interview/talk03/), 2026-10-02).

| Name | Role as written | Background as stated by the company |
|---|---|---|
| 伊藤あやめ | 代表取締役CEO, from March 2025 | Sophia University; handled Japanese agency business for UK and US metal processors at an Itochu-group non-ferrous metals trader. Joined Polimill in January 2023, initially working on PR |
| 谷口野乃花 | 代表取締役COO, from March 2025 | Started a business while at a University of Tokyo-affiliated high school; mentor to an 850-person sales organisation in customer success at a SaaS company. Joined around the QommonsAI launch. Described in June 2026 as 23 years old and studying economics at Keio University while overseeing QommonsAI ([2026-06-04](https://polimill.jp/20260604-1/)) |
| Julian Brody | ビジョナリー・エバンジェリスト; called "創業者" (founder) in talk01 | Designed superconducting magnets and generators at Hitachi; worked on many projects at Yahoo Japan; holds patents including a recommendation algorithm with a risk-aversion parameter |
| 若林正浩 | CAIO, from March 2025; 開発部担当取締役 (director in charge of development) | Data scientist, marketer and university researcher in neuroaesthetics |
| 前川知英 | 社外取締役 (outside director) and CAO, from March 2025 | AI and data research at the University of Tokyo; financial and quantitative work at a financial institution; founded a company in 2018 supporting data use by local governments and regional banks |

**Founding and the earlier representative.** Releases from 2021 to early 2025 name **横田えり** as 代表取締役 ([2021-11-30](https://polimill.jp/pr20211130/), [2023-07-31](https://polimill.jp/pr20230731/), which carries a comment from 横田 on the company's purpose). The October 2021 release describes the founding team as eight people: a director with web experience since the early internet, freelance app engineers, a designer, SNS-analysis and information-processing specialists, and university students ([2021-10-26](https://polimill.jp/pr20211026/)). In talk01, Julian Brody says he had been building a predecessor of Surfvote with a small team before incorporating in 2021. The company page does not list 横田えり, and no source reviewed states the relationship between 横田えり and Julian Brody. Julian Brody attended the Amagasaki signing as "ビジョナリー・エバンジェリスト" ([Amagasaki, 2026-04-20](https://kyodonewsprwire.jp/release/202604207739)).

**Other functions.** talk03 describes the development department (QommonsAI and Surfvote development and operations, government R&D tenders, and security certification), a "ソーシャルストラテジスト" role handling certification work, and a full-stack engineer who worked on contract from about 2021 before joining as an employee in 2025. talk02 mentions sales, an FDE-style sales role, and a training team.

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2021-10-26 | シードラウンド | ¥9.25M (925万円) | not named | 約3,000万円 including an angel round | [Polimill](https://polimill.jp/pr20211026/) |
| 2021-11-30 | not named | not stated | not named | 約3,500万円超 | [Polimill](https://polimill.jp/pr20211130/) |
| 2022-05-31 | not named | not stated | not named | 7,500万円超 | [Polimill](https://polimill.jp/pr20220531/) |
| 2022-12-13 | 第三者割当増資 (individuals as subscribers) | ¥43.3M (4,330万円) | individuals | 約1億3,000万円 | [Polimill](https://polimill.jp/pr2022121302/) |
| 2023-04-25 | not named (Mar–Apr 2023) | 4,000万円以上 | individual investors | 1億7,000万円超 | [Polimill](https://polimill.jp/pr20230425/) |
| 2023-07-31 | 増資 (July 2023) | not stated | not named | 2億円超 | [Polimill](https://polimill.jp/pr20230731/) |
| 2024-10-03 | プレシリーズA | not stated | not named | 5億円超 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000435.000088829.html) |
| 2026-01-19 | シリーズA | 約6億3,500万円: VC ¥520M + management and angels ~¥15M (equity ~¥535M) + megabank debt ¥100M | not named | not stated | [Polimill](https://polimill.jp/20260119-1/), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000625.000088829.html) |

- The [2022-12-13 release](https://polimill.jp/pr2022121302/) says all funding to that date, about 1億3,000万円, came from founding members and individuals.
- The 2023-07-31 release stated a plan to raise about ¥100M as a プレシリーズA in autumn 2023 ([2023-07-31](https://polimill.jp/pr20230731/)). The round the company later labelled プレシリーズA was announced on 2024-10-03.
- The シリーズA release gives a post-money valuation of about 50億円 and the headline "無料なのに50億円" ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000625.000088829.html)). Kepple describes the same round as a third-party allotment to venture capital and angel investors plus a loan from financial institutions ([Kepple](https://kepple.co.jp/articles/7sefmz9zt6)).
- The 5th-anniversary release thanks investors for backing a model of "基本無料でのインフラ提供" (infrastructure provided free at the base level) ([2026-02-25](https://polimill.jp/20260225-1/)).
- One Wantedly listing is titled "IPOを目指すスタートアップの人事" (HR at a startup aiming for an IPO) ([Wantedly](https://www.wantedly.com/companies/company_9612155/projects); accessed 2026-10-11). The polimill.jp accounting role mentions "将来の上場準備" (future listing preparation) ([recruit](https://polimill.jp/recruit/); accessed 2026-10-11).

---

## Engineering

### Technology stack and platforms

**Confirmed by documentation or observable public assets**

- **AWS.** Uploaded data is stored in AWS Tokyo, encrypted with AES-256, with keys in AWS KMS. Failover to AWS Osaka with cross-region replication is stated, along with 99%+ annual availability (99.5% target) ([FAQ](https://info.qommons.ai/faq)). The security policy lists AWS CloudTrail audit logs, TLS 1.2+, NTP via AWS, daily backups of user data (28–31 generations) and hourly backups of RAG data (366 generations) ([security policy](https://info.qommons.ai/info/security)). Two releases state processing on AWS domestic regions "JP CRIS等で国内処理を具体保証" ([2026-01-09](https://polimill.jp/20260109-1/), [2026-01-19](https://polimill.jp/20260119-1/)).
- **LLM hosting by provider** ([FAQ](https://info.qommons.ai/faq), LGWAN section):

  | Model family | Where requests are processed |
  |---|---|
  | ChatGPT | OpenAI's servers |
  | Claude | Polimill's own AWS environment, within Japan |
  | Gemini | Google's servers |
  | PLaMo | Preferred Networks' servers, within Japan |

  Separately, GPT-5.4 is served through Azure OpenAI in Foundry Models in the Japan region ([2026-05-08](https://polimill.jp/20260508-4/)).
- **Web app delivery.** `qommons.ai/login` responds with `x-powered-by: Next.js` and is served through Amazon CloudFront (HTTP headers observed 2026-10-11).
- **Surfvote front end.** The page loads Firebase JS SDK 10.8.0 (app and auth) (surfvote.com page source, observed 2026-10-11), and its sitemap is hosted on an S3 bucket in ap-northeast-1 ([robots.txt](https://surfvote.com/robots.txt)).
- **Retrieval and integration.** A "大規模分散型HybridRAG基盤" for searching several hundred million public documents ([2025-07-23](https://polimill.jp/20250723-1/)); "LawChunker" for statute structure ([2026-01-19](https://polimill.jp/20260119-1/)); e-Gov law database and official API ([FAQ](https://info.qommons.ai/faq)); MCP for Qommons ONE apps and the planned agent version ([2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)). GraphRAG with an administrative ontology is described as under construction ([2026-01-19](https://polimill.jp/20260119-1/)).

**Hiring requirements only (do not by themselves establish current use)**

- Backend Engineer, posted 2025-05-30 ([Green](https://www.green-japan.com/company/10658/job/285168)). Tags: Python, Go, Node.js, AWS, Docker. *Required*: backend development (Python, Go, Node.js etc., "言語は不問" — any language); Docker/AWS (ECS, Aurora, S3). *Preferred*: Python with FastAPI or LangChain; QuickSight. The job description refers to OpenAI and Claude orchestration, RBAC/ABAC, and QuickSight dashboards.
- AI/NLP Engineer and Tech Lead (knowledge graph and semantic systems), both posted 2025-08-11 ([Green](https://www.green-japan.com/company/10658/job/293843), [Green](https://www.green-japan.com/company/10658/job/293842)). They describe ontology and knowledge-graph work, LLM/rule/dictionary hybrid information extraction (NER/RE/event), NL→graph-query conversion, and MLOps/GraphOps. No programming language is named.

### Systems

| System | What it does | Source |
|---|---|---|
| Multi-model chat platform | Per-tenant web app; models from four vendors switchable within a conversation; per-organisation, department and user controls over which AIs, models and functions are available | [FAQ](https://info.qommons.ai/faq) |
| National administrative knowledge base | Collected and maintained by Polimill. The company says it corrected filename and date errors in municipal documents during metadata tagging, confirming with municipalities | [2025-07-23](https://polimill.jp/20250723-1/), [function page](https://info.qommons.ai/function) |
| Tenant RAG storage | Folder hierarchy with role-based access; file ingestion with OCR; up to 100MB per file (Excel 10MB / 300 records) | [FAQ](https://info.qommons.ai/faq) |
| PII and policy filtering | Pattern and AI-based PII detection, warn or block; two-tier banned-word lists; all detections logged for admins | [FAQ](https://info.qommons.ai/faq) |
| LGWAN gateway | Load balancers, proxies and firewalls at 株式会社シナジー's data centre (public segment) between LGWAN and the internet; file transfer disabled; one tenant and one account for both networks | [2026-02-27](https://polimill.jp/20260227-1/), [FAQ](https://info.qommons.ai/faq) |
| Usage analytics | Dashboards, automatically generated monthly impact reports, CSV log export | [function page](https://info.qommons.ai/function) |
| Qommons ONE | App distribution inside QommonsAI; partners supply data or operate MCP servers; review and sandbox before listing | [2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html) |
| Surfvote | Issue publishing, voting, comments and ratings; municipal "local" edition; university SaaS edition | [2022-12-13](https://polimill.jp/pr2022121302/), [2023-04-25](https://polimill.jp/pr20230425/) |

**Operations.** On 2026-06-23, QommonsAI was unreachable for about 8 hours 20 minutes (07:38–15:58) because a domain renewal had not completed and the domain expired. The company stated that servers, databases and data were unaffected, and listed renewal checks, alerting and a domain register as countermeasures ([2026-06-23](https://polimill.jp/apology/)). The FAQ states that planned maintenance is announced at least 5 business days in advance and that a written incident report follows within one week ([FAQ](https://info.qommons.ai/faq)).

**Development process as described.** The development department lists three areas: product development and operations, R&D delivered under government tenders, and security certification. LGWAN connectivity was built by an infrastructure-focused engineer together with the partner company ([talk03](https://polimill.jp/interview/talk03/)). The product site says requests from municipalities are reflected through "アジャイル開発体制" (agile development) "最短数日で" (in as little as a few days) ([function page](https://info.qommons.ai/function)).

### Technical background sought

- **Backend Engineer** ([Green](https://www.green-japan.com/company/10658/job/285168), posted 2025-05-30). *Required*: web-application backend development; REST APIs, asynchronous and batch processing; team development with Git; development and operations on Docker/AWS; JLPT N1 for non-native Japanese speakers. *Preferred*: LLM, vector search (RAG) or NLP implementation; systems with strict security requirements (RBAC, encryption); data-analysis platforms and log aggregation/visualisation.
- **AI/NLP Engineer** ([Green](https://www.green-japan.com/company/10658/job/293843), posted 2025-08-11). *Required*: 7+ years in NLP and data-platform construction, and leading a team technically across model development, accuracy improvement and architecture.
- **AI/NLP Tech Lead** ([Green](https://www.green-japan.com/company/10658/job/293842), posted 2025-08-11). *Required*: a top-tier domestic track record in knowledge graphs, LLM application or ontology design; publications at international conferences or in peer-reviewed journals; production implementation and operations experience.
- **Engineer (polimill.jp)**. Frontend and backend, API design, data integration, authentication, permissions and audit logs, LLM evaluation, prompt design and monitoring. The posting describes balancing research and implementation ([recruit](https://polimill.jp/recruit/); accessed 2026-10-11). No required or preferred split is given.
- The CAIO states: "エンジニアとしての経験はそこまで重視していません" (experience as an engineer is not weighted heavily) ([talk03](https://polimill.jp/interview/talk03/)).

### Industry domain

The work sits in Japanese public administration:

- assembly Q&A drafting (議会答弁) and municipal regulations (例規);
- statutes via e-Gov, and legislative drafting for the Digital Agency project;
- LGWAN and municipal information-security classification (the FAQ refers customers handling "機密性3" information to their own guidelines);
- welfare, child-support and multicultural-desk work in the MIC project;
- municipal budgeting and procurement.

The backend posting lists "公共・行政領域への関心、または社会課題への問題意識" (interest in the public sector or social issues) as *preferred*, not required. No posting reviewed requires prior public-sector experience.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | Development department: "共通言語は日本語ですが多国籍" (common language Japanese, multinational: China, Singapore, Philippines, Korea). Backend posting requires JLPT N1 for non-native speakers | [talk03](https://polimill.jp/interview/talk03/), [Green](https://www.green-japan.com/company/10658/job/285168) |
| Remote | "開発チームはリモート中心ですが、営業チームは出社" (development mainly remote; sales in office). Backend posting: full remote. AI/NLP postings: remote by consultation | [talk02](https://polimill.jp/interview/talk02/), [Green](https://www.green-japan.com/company/10658/job/285168), [Green](https://www.green-japan.com/company/10658/job/293843) |
| Location | Toranomon, Tokyo | [company page](https://polimill.jp/company/) |
| Hours | 10:00–19:00 (backend); 10:00–18:00 (AI/NLP) | [Green](https://www.green-japan.com/company/10658/job/285168), [Green](https://www.green-japan.com/company/10658/job/293843) |
| Salary | Backend ¥4M–¥12M; AI/NLP Engineer ¥10M–¥15M; AI/NLP Tech Lead ¥15M–¥22M | Green postings above |
| Equity | "株式／RSU／SO制度あり" (shares, RSUs and stock options) in the AI/NLP postings | [Green](https://www.green-japan.com/company/10658/job/293843) |
| Leave and benefits | Two days off per week (土日祝), 120 days off per year, 10–20 days paid leave; social insurance; PC and dev environment of choice; book and seminar subsidies | [Green](https://www.green-japan.com/company/10658/job/285168) |
| Visa sponsorship | Not stated in any posting reviewed | — |
| Junior candidates | Green's sales listing is tagged "未経験歓迎" (no experience required); Wantedly describes its listings as 新卒・中途・インターン (new-graduate, mid-career and intern). No engineering posting reviewed targets new graduates | [Green company page](https://www.green-japan.com/company/10658), [Wantedly](https://www.wantedly.com/companies/company_9612155/projects) |
| Team composition | Average age in the 20s; two female representatives | [Green](https://www.green-japan.com/company/10658/job/285168) |

---

## Notes

### Not publicly disclosed

Search scope (2026-10-11):

- **Company sites.** polimill.jp (sitemap, WordPress post index of 603 posts, company, about, services, recruit and interview pages); info.qommons.ai (function, price, FAQ, security and commerce-law pages); the qommons.ai login page; surfvote.com.
- **Press, registers and databases.** PR TIMES company feed (company_id 88829) and selected releases; the NTA corporate register; INITIAL and Kepple, used as leads.
- **Job boards.** Wantedly (17 listings) and Green (6 listings).
- **Developer platforms.** GitHub organisations polimill, Polimill-Inc, polimill-inc, qommons, qommonsai, surfvote and polimill-jp; name lookups on Zenn, note, Qiita and Speaker Deck.
- **Web searches.** Polimill, ポリミル, QommonsAI, コモンズAI, Surfvote, 横田えり and Julian Brody, in Japanese and English.

Findings:

- **Investors.** No VC, angel or lender is named in company releases. A Forbes profile quoted in the company's [2026-06-04 release](https://polimill.jp/20260604-1/) refers to "undisclosed venture capitalists".
- **Revenue and financial results.** Not published.
- **Cumulative funding after the シリーズA.** Not stated.
- **Engineering blog or technical writing.** None found; Zenn, note, Qiita and Speaker Deck lookups under "polimill" returned no account.
- **Open source.** GitHub organisations [`polimill`](https://github.com/polimill) (created 2026-02-10) and [`Surfvote`](https://github.com/Surfvote) (created 2021-02-21) exist, each with 0 public repositories and no profile fields linking them to the company, so ownership is unconfirmed. `qommons` and `qommonsai` do not exist.
- **Founder relationship.** No source states how 横田えり and Julian Brody relate, or when 横田えり left the board. No release announcing the March 2025 change of representatives was found.
- **LGWAN-ASP registration.** The J-LIS LGWAN-ASP service list returned HTTP 403 to automated access, so QommonsAI's or Synergy's registration status there was not checked.
- **Other.** No visa-sponsorship statement, turnover figure or SLA service-credit terms were found.

### Inconsistencies across sources

- **Capital.** 6億円 ([PR TIMES company box](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)) versus 2億4572万1558円 ([Green company page](https://www.green-japan.com/company/10658)). Both are undated (accessed 2026-10-11), and neither says whether capital reserve is included. The company page lists no capital.
- **Headcount.** "20人" on [Green](https://www.green-japan.com/company/10658) (undated); 4 full-time employees plus 6 hires ([2025-11-05](https://polimill.jp/20251105-1/)); "数十人規模" ([talk02](https://polimill.jp/interview/talk02/), 2026-10-02).
- **Address.** [INITIAL](https://initial.inc/companies/A-40660) (profile updated 2026-02-18) and the [Green company page](https://www.green-japan.com/company/10658) give Roppongi addresses. Green has "クロスオフィス六本木4F", while the registry's former address is "ラウンドクロス六本木". The registry shows Toranomon from 2026-03-24, and Green's job postings already give Toranomon.
- **QommonsAI release date.** Development started March 2024 and release was July 2024 ([2025-01-06](https://prtimes.jp/main/html/rd/p/000000484.000088829.html)); "2024年10月には…リリース" ([about](https://polimill.jp/about/)); preview [2024-08-02](https://prtimes.jp/main/html/rd/p/000000418.000088829.html); product version [2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html).
- **Founder.** Releases from 2021 name 横田えり as 代表取締役 ([2021-11-30](https://polimill.jp/pr20211130/)). The 2026 recruiting interview calls Julian Brody "創業者" ([talk01](https://polimill.jp/interview/talk01/)).
- **Representative in release boilerplate.** Releases switch from 横田えり to the new representatives between [2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html) and [2025-03-17](https://prtimes.jp/main/html/rd/p/000000506.000088829.html). A Surfvote release dated [2025-05-19](https://prtimes.jp/main/html/rd/p/000000519.000088829.html) still names 横田えり. Wantedly listings describe a "Co-CEO体制", while the company page uses CEO/COO titles.
- **Lender.** The company says the シリーズA debt came from a "メガバンク" (megabank) ([2026-01-19](https://polimill.jp/20260119-1/)). The Forbes text quoted in the [2026-06-04 release](https://polimill.jp/20260604-1/) says "local banks".
- **Valuation.** About 50億円 post-money (company) versus 3,951百万円 on [INITIAL](https://initial.inc/companies/A-40660), labelled 推測 (estimate) and including potential shares, as of 2026-01-18.
- **2026 user target.** 1,200 municipalities and 800,000 users ([2026-01-19](https://polimill.jp/20260119-1/)) versus about 1,200 municipalities and 650,000 users for December 2026 ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)).
- **Qommons ONE timeline.** Release in April 2026 with 100+ apps within 2026 ([2026-01-19](https://polimill.jp/20260119-1/)); beta in April and official release in June 2026 ([2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)); opening at the end of October 2026 with about 100 apps targeted in 2027 ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)).
- **Pricing above 1,000 accounts.** Stepped monthly price with "利用上限なし" (no usage cap) ([2026-01-09](https://polimill.jp/20260109-1/)) versus "ご利用人数に応じた料金プランをご提案" (plan proposed by user count) and a monthly usage cap ([price page](https://info.qommons.ai/price), [FAQ](https://info.qommons.ai/faq); accessed 2026-10-11).
- **Within the FAQ** ([FAQ](https://info.qommons.ai/faq), accessed 2026-10-11):
  - Log retention is given as 3 months in one answer, and in another as archive after 14 inactive days with deletion 90 days later.
  - Support hours are given as 10:00–18:00 in one answer and 10:00–17:00 in another.
  - "トークン数や対話数に制限はございません" (no limit on tokens or conversations) appears alongside a usage cap above 1,000 accounts.
- **Counting basis.** Wantedly counts "1,050の自治体・パブリックセクター" (municipalities and public sector) as of 2026-07; other sources count "自治体". An OpenAI customer page about Polimill (openai.com/index/polimill/) returned HTTP 403 to automated access on 2026-10-11 and was not used.

### Other

- **Revenue model.** The company states that the core product is free up to 1,000 accounts and that revenue is to come from the surrounding ecosystem rather than usage fees ([2026-01-09](https://polimill.jp/20260109-1/), [FAQ](https://info.qommons.ai/faq)).
- **Products announced but not yet launched**, as of 2026-10-11:
  - QommonsAI Pro, Qommons Connect and QommonsAI Advance ([2026-01-19](https://polimill.jp/20260119-1/));
  - "Runbook Qommons（仮称）", a no-code agent builder ([2026-02-25](https://polimill.jp/20260225-1/));
  - Qommons Qraft and Qommons Link ([function page](https://info.qommons.ai/function));
  - the agent version and the AX repository ([2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)).
- **Press output.** Of the 603 posts on polimill.jp, 599 are filed as プレスリリース (WordPress category counts, 2026-10-11). Of the 266 posts dated 2023, 226 have Surfvote, 投票, イシュー or 意見 in the title (title count, 2026-10-11). In talk01, 伊藤 says she issued one press release per day in her first months. The polimill.jp feed has no posts between 2024-07-17 and 2025-05-14, while PR TIMES carries releases for that period; both were checked for this page.

---

## Resources

**Official**

- [Corporate site (JA)](https://polimill.jp/) — [company](https://polimill.jp/company/) · [about](https://polimill.jp/about/) · [services](https://polimill.jp/services/) · [news index](https://polimill.jp/news/) · [recruit](https://polimill.jp/recruit/)
- Recruiting interviews (JA): [talk01 — founder and CEO, 2026-09-18](https://polimill.jp/interview/talk01/) · [talk02 — CAO and COO, 2026-10-02](https://polimill.jp/interview/talk02/) · [talk03 — development department, 2026-10-02](https://polimill.jp/interview/talk03/)
- [QommonsAI product site (JA)](https://info.qommons.ai/) — [function](https://info.qommons.ai/function) · [price](https://info.qommons.ai/price) · [FAQ](https://info.qommons.ai/faq) · [information security policy](https://info.qommons.ai/info/security) · [commerce-law disclosure](https://info.qommons.ai/info/commerce-law) · [enterprise edition price](https://info.qommons.ai/business_personal/price)
- [QommonsAI app login](https://qommons.ai/login)
- [Surfvote](https://surfvote.com/) · [robots.txt](https://surfvote.com/robots.txt)
- [PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/88829)
- GitHub organisations, ownership unconfirmed: [polimill](https://github.com/polimill) · [Surfvote](https://github.com/Surfvote)

**Press releases (JA — newest first)**

- [J-LIS fair: agent version, Qommons ONE, AX repository — 2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)
- [Kagawa Chusan area agreements — 2026-09-25](https://polimill.jp/20260925/)
- [MIC trusted-AI project selection (PLaMo) — 2026-06-30](https://polimill.jp/20260630-1/)
- [QommonsAI outage report (domain expiry) — 2026-06-23](https://polimill.jp/apology/)
- [COO in Forbes 30 Under 30 Asia — 2026-06-04](https://polimill.jp/20260604-1/)
- [Azure OpenAI Japan region adopted — 2026-05-08](https://polimill.jp/20260508-4/)
- [Qommons ONE teaser and partner recruitment — 2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)
- [LGWAN connection service with Synergy — 2026-02-27](https://polimill.jp/20260227-1/)
- [5th anniversary — 2026-02-25](https://polimill.jp/20260225-1/)
- [シリーズA, about ¥635M — 2026-01-19](https://polimill.jp/20260119-1/) · [PR TIMES](https://prtimes.jp/main/html/rd/p/000000625.000088829.html)
- [New pricing — 2026-01-09](https://polimill.jp/20260109-1/)
- [2025 annual summary — 2025-12-31](https://polimill.jp/20251231-1/)
- [LGWAN connection fee waived — 2025-12-08](https://polimill.jp/20251208-1/)
- [New mission — 2025-12-05](https://polimill.jp/20251205-1/)
- [Full-time staff doubled — 2025-11-05](https://polimill.jp/20251105-1/)
- [Privacy Mark — 2025-10-10](https://polimill.jp/20251010-1/)
- [ISO/IEC 27001 — 2025-10-09](https://polimill.jp/20251009-1/) · [ISO 9001 — 2025-10-09](https://polimill.jp/20251009-2/)
- [Free tier raised to 1,000 (ver.2.1) — 2025-10-02](https://polimill.jp/20251002-1/)
- [Surfvote 500,000 monthly PV — 2025-08-06](https://polimill.jp/20250806-2/)
- [300 municipalities; nationwide document search — 2025-07-23](https://polimill.jp/20250723-1/)
- [Digital Agency legislative-drafting verification — 2025-06-02](https://prtimes.jp/main/html/rd/p/000000520.000088829.html)
- [Surfvote issue release naming 横田えり — 2025-05-19](https://prtimes.jp/main/html/rd/p/000000519.000088829.html)
- [PLaMo Prime added — 2025-05-14](https://polimill.jp/qommonsai_0514_2025/)
- [Hannan City partnership — 2025-03-17](https://prtimes.jp/main/html/rd/p/000000506.000088829.html)
- [Digital Agency hackathon award — 2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html)
- [New year 2025 — 2025-01-06](https://prtimes.jp/main/html/rd/p/000000484.000088829.html)
- [100 municipalities in three months — 2024-11-30](https://prtimes.jp/main/html/rd/p/000000470.000088829.html)
- [QommonsAI product version — 2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html)
- [プレシリーズA, cumulative over ¥500M — 2024-10-03](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)
- [QommonsAI preview — 2024-08-02](https://prtimes.jp/main/html/rd/p/000000418.000088829.html)
- [Tawaramoto partnership — 2024-07-09](https://polimill.jp/2024071901-2/)
- [DIGITAL COMMONS beta — 2024-03-13](https://polimill.jp/2024031301-2/)
- [Cumulative over ¥200M — 2023-07-31](https://polimill.jp/pr20230731/)
- [Over ¥40M raised — 2023-04-25](https://polimill.jp/pr20230425/)
- [¥43.3M third-party allotment — 2022-12-13](https://polimill.jp/pr2022121302/)
- [Cumulative over ¥75M; university SaaS — 2022-05-31](https://polimill.jp/pr20220531/)
- [Email login and PC version — 2021-11-30](https://polimill.jp/pr20211130/)
- [Seed round, Surfvote release — 2021-10-26](https://polimill.jp/pr20211026/)

**Third-party coverage and profiles**

- [NTA corporate number register — 5010401158530 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530)
- [MIC — trusted-AI project selection, 2026-06-08 (JA)](https://www.soumu.go.jp/menu_news/s-news/01tsushin03_02000462.html)
- [Amagasaki City — partnership release, 2026-04-20 (JA)](https://kyodonewsprwire.jp/release/202604207739)
- [Yokohama City — Surfvote opinion collection results, FY2025 (JA)](https://www.city.yokohama.lg.jp/city-info/koho-kocho/kocho/dp/dpkekka/R07dpkekka.html)
- [Green — company page (JA)](https://www.green-japan.com/company/10658) · [Backend Engineer](https://www.green-japan.com/company/10658/job/285168) · [AI/NLP Engineer](https://www.green-japan.com/company/10658/job/293843) · [AI/NLP Tech Lead](https://www.green-japan.com/company/10658/job/293842)
- [Wantedly — listings (JA)](https://www.wantedly.com/companies/company_9612155/projects) · [sales listing with July 2026 figures](https://www.wantedly.com/projects/2420681)
- [Kepple — シリーズA coverage (JA)](https://kepple.co.jp/articles/7sefmz9zt6)
- [INITIAL / Speeda (JA)](https://initial.inc/companies/A-40660)
