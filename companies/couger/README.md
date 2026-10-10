# Couger

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Couger (クーガー株式会社 / Couger Inc.) is a Tokyo company founded in December 2006 and based in Jingumae, Shibuya ([PR TIMES company profile](https://prtimes.jp/main/html/rd/p/000000050.000033615.html), 2026-10-09; [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.27, 2026-10-07). It develops **LUDENS**, which it calls a 人型AIプラットフォーム (human-type AI platform), and **Rachel (レイチェル)**, a "virtual human agent" (VHA) that runs on it ([company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) pp.7–8; [PR TIMES, 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)). FamilyMart runs Rachel and a second character, Akira (アキラ), on in-store tablets to support franchise store managers ([FamilyMart, 2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)). Before that rollout the company's public record covered online-game development, contract AI and robotics work, and Ethereum-based projects (GeneFlow, zkCREAM) ([Green interview](https://www.green-japan.com/interview/5263); [SBBIT, 2018-06-11](https://www.sbbit.jp/article/cont1/34986); [PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/33615)). Since July 2025, most of its press releases have announced events of **Sphear**, a "space × AI" community that the company runs ([PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/33615)).

- **Deployment:** about 7,000 FamilyMart stores as of the end of July 2024 ([FamilyMart, 2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html)). The company deck says "7,000店舗以上" ([company deck, 2026-10-07](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)). A trade outlet reports 13,000 stores using the assistant ([激流オンライン, 2026-01-30](https://gekiryu-online.jp/2026/01/227822)). See `Inconsistencies across sources`.
- **Funding:** the only disclosed external equity is a capital and business alliance with ITOCHU, agreed in principle on 2020-01-20, with no amount published ([ITOCHU](https://www.itochu.co.jp/ja/news/press/2020/200120.html)). Capital is "282百万円" (¥282M) according to the [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) (2026-10-07).
- **Team:** 41 people (39 full-time, 2 part-time) plus about 10 contractors as of 2026-03-31. Engineers make up 49% of roles ([company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)).
- **Engineering:** current postings list Python, TypeScript/React/Next.js and AWS, Google Cloud and Azure ([Senior Software Engineer posting](https://open.talentio.com/r/1/c/couger/pages/119821); datePosted 2026-02-05). A 2024 posting lists a Unity client ([paiza](https://paiza.jp/career/job_offers/28362); updated 2024-12-20). Behaviour scripting runs in JavaScript ("InteractiveCode"). Current postings require business-level or native Japanese. The 2022 English-language postings for the ML/AI team required English ([Notion careers page](https://couger.notion.site/Careers-Couger-Inc-35ada7ab0ed34c1baff8dac5f86b5636)). Work is hybrid, and "フルリモートは不可" (full remote not permitted).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Couger / クーガー. The company deck's cover reads "Virtual Human Agent × XAI" | [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.1 (2026-10-07) |
| Legal name | クーガー株式会社 (furigana クーガー). The company deck uses the English name "Couger Inc."; the GitHub organisation uses "Couger, Inc." | [NTA corporate number site](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073), [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.27, [GitHub API](https://api.github.com/orgs/couger-inc) |
| Corporate number | 7010701025073. Designated 2015-10-05 (平成27年10月5日); last updated 2018-04-13 (平成30年4月13日). The change history shows only the initial 新規 entry | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073); read 2026-10-11 |
| Registered address | 東京都渋谷区神宮前６丁目１９番１６号 | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073) |
| Office | 〒150-0001 東京都渋谷区神宮前6-19-16 越一ビル201 | [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.27, [PR TIMES company profile](https://prtimes.jp/main/html/rd/p/000000050.000033615.html) |
| Founded | December 2006; the company deck gives "2006年12月19日" | [PR TIMES company profile](https://prtimes.jp/main/html/rd/p/000000050.000033615.html), [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.27 |
| Officers listed | 代表取締役 CEO 石井 敦 (Atsushi Ishii); 取締役 CTO 高橋 光 | [PR TIMES, 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html) (CEO); [Green interview](https://www.green-japan.com/interview/5263) photo caption "取締役 CTO 高橋 光氏" (Undated; accessed 2026-10-11) |
| Capital | "282百万円". The PR TIMES profile box shows "-" | [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.27 (2026-10-07), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000050.000033615.html) |
| Headcount | 41 (正社員 39, アルバイト 2) plus "業務委託 10名程度", as of 2026-03-31 | [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) pp.18, 27 |
| Working language | No company-wide statement was found. See `Working conditions` | — |
| Customers | FamilyMart (Rachel/Akira). An Autobacs Seven group trial began 2024-08-01. The deck lists 14 "取引先企業・機関" | [FamilyMart](https://www.family.co.jp/company/news_releases/2022/20221128_02.html), [Ridgelinez](https://www.ridgelinez.com/news/news_20240801/), [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.16 |
| Total raised | Not disclosed. ITOCHU capital and business alliance, 2020-01-20 | [ITOCHU](https://www.itochu.co.jp/ja/news/press/2020/200120.html) |
| Former product name | "コネクトーム / Connectome" was used in releases from 2018 to 2020 for the technology and agent now called LUDENS | [PR TIMES 2018-04-26](https://prtimes.jp/main/html/rd/p/000000002.000033615.html), [PR TIMES 2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html), [ITOCHU 2020-01-20](https://www.itochu.co.jp/ja/news/press/2020/200120.html) |
| GitHub | `couger-inc` ("Couger, Inc."; verified; created 2018-01-19; 10 public repositories). `zkcream` (verified; created 2020-10-06; 6 repositories) | [GitHub API](https://api.github.com/orgs/couger-inc), [GitHub — zkcream](https://github.com/zkcream); read 2026-10-11 |

**Related communities and sites run by the company.** [Virtual Human Lab](https://virtualhumanlab.io/) describes itself as publishing part of Couger's research on virtual human agents ("クーガーによるバーチャルヒューマンエージェントの研究活動を一部公開"; accessed 2026-10-11). Its start date differs between sources; see `Inconsistencies across sources`. [Sphear](https://sphear.to/) is a "宇宙 × AI" community launched with a first event on 2025-08-01 ([PR TIMES, 2025-07-03](https://prtimes.jp/main/html/rd/p/000000036.000033615.html)); its #13 event is scheduled for 2026-11-06 ([PR TIMES, 2026-10-09](https://prtimes.jp/main/html/rd/p/000000050.000033615.html)). Couger is listed among the 86 new members announced by the Enterprise Ethereum Alliance on 2017-05-22 ([EEA, 2017-05-22](https://entethalliance.org/enterprise-ethereum-alliance-expands-dramatically-announcing-86-new-members/)).

**Computer-vision competition results announced by the company (PR TIMES):**
- Facebook Research OpenEDS eye-tracking challenge, 3rd ([2019-10-16](https://prtimes.jp/main/html/rd/p/000000011.000033615.html)).
- Thermal Image Super-Resolution Challenge at CVPR 2020, 2nd ([2020-06-29](https://prtimes.jp/main/html/rd/p/000000022.000033615.html)).
- ICCV 2021 challenge, 3rd, with a Best Challenge Paper Award for SkeletonNetV2 ([2021-11-29](https://prtimes.jp/main/html/rd/p/000000026.000033615.html)).
- ECCV 2022 Instagram Filter Removal Challenge, 9th of 114 participants ([2023-01-23](https://prtimes.jp/main/html/rd/p/000000030.000033615.html)).
- CVPR 2024 MIPI challenge, 7th ([2024-07-23](https://prtimes.jp/main/html/rd/p/000000032.000033615.html)).
- A thermal super-resolution paper accepted at a CVPR 2025 workshop ([2025-06-17](https://prtimes.jp/main/html/rd/p/000000035.000033615.html)).
- Sclera Segmentation Benchmarking Competition (SSBC) 2025 at IEEE IJCB 2025, 1st in the synthetic-data track ([2025-07-10](https://prtimes.jp/main/html/rd/p/000000037.000033615.html)).

**Conference sponsorships (organisers' pages):**
- Product History Conference 2024 (2024-11-30), Silver; the CEO gave a talk on Rachel's rollout to 7,000 convenience stores ([YOUTRUST event page](https://lp-prohis.youtrust.jp/2024/); accessed 2026-10-11).
- JSAI2026, Platinum ([JSAI2026 sponsor list](https://www.ai-gakkai.or.jp/jsai2026/sponsor/); accessed 2026-10-11).

---

## Product

The company's mission statement is "人に寄り添い、成長させるAI" (AI that stays close to people and helps them grow) ([company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.2). The deck's cover reads "Virtual Human Agent × XAI".

### Product line-up

| Product | What the company says it is | Status evidence | Source |
|---|---|---|---|
| LUDENS (ルーデンス) | 人型AIプラットフォーム. The deck names the VHA interface, LudensCore (overall control), a 知覚エンジン (perception engine) and a 理解・行動促進エンジン (understanding and behaviour-promotion engine). A 2025 talk report names VisualCortex (image recognition), LanguageCortex (language) and InteractiveCode, a JavaScript-based script layer. Postings add "Insight" (meaning interpretation and search) and "Ludens Analytics" (data analysis platform) | Current; named in current engineering postings | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.7, [Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference), [posting](https://open.talentio.com/r/1/c/couger/pages/119821) |
| Rachel (レイチェル) / Akira (アキラ) | Virtual human agents running on LUDENS. At FamilyMart they act as a store-manager assistant on tablets | Current; FamilyMart deployment | [PR TIMES, 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html), [FamilyMart](https://www.family.co.jp/company/news_releases/2022/20221128_02.html) |
| VisualCortex | Image-recognition AI within LUDENS; its processing was moved from servers to the on-site PC | Named in a current posting and in the 2025 talk report | [Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference), [posting](https://open.talentio.com/r/1/c/couger/pages/119821) |
| GeneFlow | Records AI training data, algorithms, models and execution history on a blockchain; α version 2018, limited β 2020-04-14 | No release after 2020 found in the PR TIMES series | [PR TIMES, 2018-06-29](https://prtimes.jp/main/html/rd/p/000000005.000033615.html), [PR TIMES, 2020-04-14](https://prtimes.jp/main/html/rd/p/000000020.000033615.html) |
| zkCREAM | zk-SNARK-based anonymous voting protocol, developed as open source | Main repository archived; last pushes 2022-02 | [PR TIMES, 2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html), [GitHub — cream](https://github.com/couger-inc/cream) |

Earlier products and projects named in releases include:
- an AI learning simulator of pedestrian movement, supplied to 本田技術研究所 as a training environment for autonomous driving (mentioned without a date in the [PR TIMES release of 2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)); the deck's timeline lists "本田技術研究所 ロボット共同研究開発" under "〜2019" ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.11);
- the JavaScript "Connectome SDK" for building virtual humans, released 2019-09-18 ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000010.000033615.html));
- the blockchain election system "OMEGA", developed with アクト ([PR TIMES, 2020-01-27](https://prtimes.jp/main/html/rd/p/000000018.000033615.html)).

**Rachel's functions at FamilyMart.** FamilyMart's release lists ([2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)):
- prompting action through information and communication fitted to the store's situation and the manager's traits;
- reference information from large-scale data on sales and customer counts;
- new-product, campaign and weekly information, plus checks of tasks not yet done;
- links to supervisor (SV) store guidance.

From 2024-07, generative AI was added for voice search of operating manuals (register operation, staff training, emergency response) ([FamilyMart, 2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html)). The company deck describes summaries, task priorities, explanations of why a task matters, feedback, empathy and reminders ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.12).

### Commercialization

No public price list was found for LUDENS or Rachel. Postings describe customer projects in five phases: ①提案 (proposal), ②業務分析 (business analysis), ③開発 (development), ④システム導入 (implementation) and ⑤導入後の伴走 (post-launch support). Technical account managers, project managers and AI implementation consultants each cover different phases ([PjM posting](https://open.talentio.com/r/1/c/couger/pages/84099), [TAM posting](https://open.talentio.com/r/1/c/couger/pages/84100)). One TAM describes a split of "TAM：営業＝7:3" ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.15).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2021-03-12 | 38 FamilyMart stores, after experimental introduction "昨年から都内を中心に" (from the previous year, mainly in Tokyo); daily sales up "平均３―４％" (3–4% on average) against comparable stores; plan to reach several hundred stores or more during FY2021. Reported by 日刊工業新聞 as an ITOCHU initiative | [Newswitch (日刊工業新聞), 2021-03-14](https://newswitch.jp/p/26324) |
| 2022-11-28 | Plan to reach about 5,000 stores by the end of FY2023 | [FamilyMart](https://www.family.co.jp/company/news_releases/2022/20221128_02.html), [PR TIMES, 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html) |
| 2023-01 | Store-manager rollout began | [PR TIMES, 2024-08-07](https://prtimes.jp/main/html/rd/p/000000033.000033615.html) |
| 2024-07 (end) | About 7,000 stores | [FamilyMart, 2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) |
| 2026-01-30 | "足元すでに1万3000店が活用しており、来期中には全店に行き渡る見通しだ" (13,000 stores using it; all stores expected during the next fiscal year), as reported by the outlet | [激流オンライン](https://gekiryu-online.jp/2026/01/227822) |
| 2026-10-07 | "全国7,000店舗以上へ提供中"; in pilot stores, sales up 2% on average and an expected reduction of about 30% in SV work | [company deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.12 |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2018-04-26](https://prtimes.jp/main/html/rd/p/000000002.000033615.html) | KDDI | Technical support for the "バーチャルキャラクター × xR" project |
| [2019-06-26](https://prtimes.jp/main/html/rd/p/000000009.000033615.html) | 電通国際情報サービス, 京王電鉄 | VHA field trial on digital signage at トリエ京王調布 |
| [2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html) | 本田技術研究所 | Supply of a pedestrian-movement AI learning simulator, mentioned without a date |
| [2020-01-20](https://www.itochu.co.jp/ja/news/press/2020/200120.html) | 伊藤忠商事 | Capital and business alliance (basic agreement) |
| [2020-01-27](https://prtimes.jp/main/html/rd/p/000000018.000033615.html) | アクト | Joint development of the blockchain election system OMEGA |
| [2021-02-10](https://prtimes.jp/main/html/rd/p/000000023.000033615.html) | Ethereum Foundation | Partnership signed 2020-12; ETHTerakoya community, started under Ethereum Foundation sponsorship ([2020-05-25](https://prtimes.jp/main/html/rd/p/000000021.000033615.html)) |
| [2022-01-31](https://prtimes.jp/main/html/rd/p/000000027.000033615.html) | 早稲田リーガルコモンズ法律事務所 | zkCREAM verification |
| [2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html) | ファミリーマート | Rachel/Akira, ~5,000 stores by end of FY2023 |
| [2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html) | ファミリーマート | CEO appointed adviser to FamilyMart's 生成AIプロジェクト from 2023-10-01 |
| [2024-08-01](https://www.ridgelinez.com/news/news_20240801/) | オートバックスデジタルイニシアチブ, Ridgelinez | Rachel customer-service trial at the Autobacs Seven group digital lab |
| [2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) | ファミリーマート | Generative AI added (from 2024-07); ~7,000 stores |

The company deck's customer list (p.16) also names NHN JAPAN, 電通総研, ソニー・インタラクティブエンタテインメント, NEDO, スクウェア・エニックス, 産業技術総合研究所, 電気通信大学, シンガポール国立大学 and 早稲田大学. The data-analyst posting states that Rachel is being introduced at "アパレル・小売など複数の大手企業" (several large apparel and retail companies) without naming them ([posting](https://open.talentio.com/r/1/c/couger/pages/122132); datePosted 2026-04-09).

### Stated plans

- "将来的には、サードパーティ企業がLUDENSを使ってバーチャルヒューマンエージェントを提供できることを想定している" (third-party companies providing VHAs on LUDENS) ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.8).
- The near-term focus is stated as understanding, behaviour change and habit formation in stores and on site, with the aim to "導入先を一気に拡大" (expand customers rapidly) ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.14).
- FamilyMart states that in future it plans to link its camera-based "AI売場スコアリング" trial with Rachel and its AI ordering system ([FamilyMart, 2026-01-13](https://www.family.co.jp/company/news_releases/2026/20260113_02.html)).
- Sphear's stated aim is "人類の宇宙移住にAIの力で貢献すること" (contributing to human space settlement with AI) ([PR TIMES, 2026-01-08](https://prtimes.jp/main/html/rd/p/000000043.000033615.html)).

---

## Founder

The company deck lists **石井 敦 (Atsushi Ishii, CEO)** and **高橋 光 (CTO)** under the heading "大規模システムと最先端AIを極めた創業者" ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.5). WIRED writes that Ishii "共同創業し" (co-founded) the company ([WIRED, 2022-05-16](https://wired.jp/article/the-next-innovators-3-atsushi-ishii/)).

**石井 敦 — 代表取締役 CEO**
- Studied mechanical engineering. He then worked on control-system software for power plants, joined IBM Japan (Fujisawa), and moved to Lycos Japan to develop its large-scale search engine. After Rakuten acquired Lycos Japan, he continued on search at Rakuten, then led technology at the mobile-video company セーバー ([Green interview](https://www.green-japan.com/interview/5263); Undated; accessed 2026-10-11).
- After セーバー was sold, he says he was close to joining SpaceX. He instead incorporated Couger for a large-scale search-engine project with a major domestic company, which was cancelled "クーガー設立の初日に" (on the day the company was founded). The company turned towards AI and robotics from around 2014 ([SBBIT, 2018-06-11](https://www.sbbit.jp/article/cont1/34986)). After founding, it designed and developed large-scale systems and online games and did joint research with universities ([Green interview](https://www.green-japan.com/interview/5263)).
- CTO of LivingImage (Silicon Valley) for two years from 2009, and CTO of dango for four years from 2010, where he worked on the game 『マジモン』 ([Green interview](https://www.green-japan.com/interview/5263)).
- Lecturer for Stanford University's 2018 special AI lecture; former visiting researcher at the University of Electro-Communications ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.5; [PR TIMES, 2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html)).
- Became Japan representative of the Enterprise Ethereum Alliance on 2022-04-07, described as one of 13 core members worldwide. He succeeded Couger's 石黒 一明 ([PR TIMES, 2022-04-07](https://prtimes.jp/main/html/rd/p/000000028.000033615.html)).
- Adviser to FamilyMart's generative AI project from 2023-10-01 ([PR TIMES, 2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html)).

**高橋 光 — 取締役 CTO.** He worked at a large independent systems integrator and joined Lycos Japan in 2001, where he designed mail and community systems for large user bases. He continued that work at Rakuten and Infoseek. He specialises in back ends that handle "デイリーで億単位のアクセス" (hundreds of millions of daily accesses) and in online-game back ends ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.5).

**Other people named by the company:**
- チーフアーキテクト 土田 悠貴 spoke with the CEO at アーキテクチャConference 2025 on 2025-11-20 ([Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference)).
- The [careers member page](https://careers.couger.co.jp/member) (Undated; accessed 2026-10-11) lists:
  - 中村 竜晴, 事業統括ディレクター (European VR startup, Disney Japan, consulting);
  - 五十嵐 智哉, チーフアーキテクト (PlayStation racing and fighting games);
  - 平崎 葵, engineering manager for the full-stack web team;
  - roles in technical account management, product management, NLP and search, DevOps, senior QA, technical consulting, PR and recruiting.
- `TomoyaIgarashi` (company "Couger Inc.") is the only public member of the `couger-inc` GitHub organisation ([GitHub API](https://api.github.com/orgs/couger-inc/public_members); read 2026-10-11).

**Adviser.** 山川 宏 (Whole Brain Architecture Initiative) was appointed adviser, as announced on 2019-09-18 ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)).

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2020-01-20 | 資本業務提携 (capital and business alliance; "基本合意", agreement in principle) | Not disclosed | 伊藤忠商事 | Not disclosed | [ITOCHU](https://www.itochu.co.jp/ja/news/press/2020/200120.html), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000017.000033615.html) |
| 2021-07-02 | "開発助成金採択" (development grant; PR TIMES, 2021-07-02) / "公式プログラムに選ばれる" (selected for an official program; PR TIMES, 2022-04-07): Ethereum Foundation grant for zkCREAM; non-equity | Not disclosed | Ethereum Foundation | — | [PR TIMES, 2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html), [PR TIMES, 2022-04-07](https://prtimes.jp/main/html/rd/p/000000028.000033615.html) |

Facts that do not fit the table:
- ITOCHU's release says that besides investing, "伊藤忠グループのネットワークを活かし、同社の国内外への展開を支援いたします" (it will support domestic and overseas expansion through the ITOCHU group network). It gives no stake or amount ([ITOCHU, 2020-01-20](https://www.itochu.co.jp/ja/news/press/2020/200120.html)). Couger's FamilyMart release calls ITOCHU its "資本業務提携先" (capital and business alliance partner) and says Rachel was developed in cooperation with ITOCHU and FamilyMart ([PR TIMES, 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)).
- The 2021 zkCREAM release says that donations of "100万円を超える支援金" (over ¥1M) had been collected through Gitcoin, mostly from overseas ([PR TIMES, 2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html)).
- No other equity round, investor, valuation or cumulative total was found in company, investor or press sources. The capital of ¥282M ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.27, 2026-10-07) is the only capital figure the company publishes.

---

## Engineering

### Technology stack and platforms

Confirmed by documentation or public assets:
- **Behaviour scripting:** InteractiveCode, a JavaScript-based script layer that holds business flows and dialogue logic ([Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference), on a talk of 2025-11-20; Undated; accessed 2026-10-11). The 2019 Connectome SDK likewise let developers program virtual-human behaviour in JavaScript, including calls to external APIs ([PR TIMES, 2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)).
- **LLM:** generative AI in Rachel/Akira from 2024-07 ([FamilyMart](https://www.family.co.jp/company/news_releases/2024/20240802_01.html)). The deck's architecture diagram lists "LLM" in the perception engine ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.7).
- **Blockchain work:**
  - GeneFlow on Ethereum and Quorum, with trained models and training data stored in a "分散型ファイルシステム" (distributed file system) ([PR TIMES, 2018-06-29](https://prtimes.jp/main/html/rd/p/000000005.000033615.html)).
  - zkCREAM in TypeScript, including an API server, an interface, a Vue faucet and a snarkjs-based trusted-setup fork ([GitHub — zkcream](https://github.com/zkcream), [GitHub — cream](https://github.com/couger-inc/cream)).
- **Rust:** `couger-inc/rust-freetype` and `couger-inc/font-kit`, both created 2024-08-26, with latest commits on 2023-07-19 and 2024-09-05 respectively. Their purpose is not stated ([GitHub — couger-inc](https://github.com/couger-inc)).

Inferred from current job postings (hiring evidence; not proof of production use):
- **Languages:** Python and TypeScript/JavaScript recur across the engineering postings. Go appears in the full-stack posting's description ("GoやPythonによるAPIやバッチ処理") and as a preferred skill ([full-stack posting](https://open.talentio.com/r/1/c/couger/pages/109446); datePosted 2024-06-04).
- **Web:** React, Next.js, Material UI, Tailwind CSS; GitHub, GitHub Actions; Jest, MSW, Cypress, Storybook; Confluence, Jira, Slack ([Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821), [Product Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687)).
- **Cloud and platforms:** Amazon Web Services, Google Cloud, Microsoft Azure, Firebase; Linux, Windows, Docker ([Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821)).
- **ML:** PyTorch, Transformers, Rasa, Weights & Biases, Hugging Face, Kubernetes, Terraform ([Senior Software Engineer (Machine Learning), Green](https://www.green-japan.com/company/5263/job/301740); Undated; accessed 2026-10-11).
- **Client app:** Unity (C#), with native plugins in C++, Rust, Objective-C or Kotlin as a preferred skill; targets Windows, Mac, iOS and Android; Xcode and Android Studio ([paiza](https://paiza.jp/career/job_offers/28362); updated 2024-12-20). The QA posting lists "Unity / Airtest" as build tools ([Senior QA](https://open.talentio.com/r/1/c/couger/pages/117722)).
- **Data:** MySQL, Tableau, Power BI, Python, R ([Senior Data Analyst](https://open.talentio.com/r/1/c/couger/pages/122132); datePosted 2026-04-09).
- **Earlier:** the 2022 English postings listed Python, Linux, Docker, Jenkins, GitHub Actions and AWS ([Server Application Engineer](https://couger.notion.site/ad09a89b538849f585f410ce7ef4706f); last edited 2022-10-11).

### Systems

| System | What it does | Source |
|---|---|---|
| LUDENS client application | VHA interface (voice, facial expression, motion, GUI, character), an "インタラクションフレームワーク" and LudensCore, which handles "インターフェースの全体制御" | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.7 |
| LUDENS cloud platform | "理解・行動促進エンジン" (user behaviour analysis, user trait analysis, business analysis, planning, priority, communication); "知覚エンジン" (natural language, image recognition, LLM); Web UI/API; a data connector to external data | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.7 |
| Engine/script separation | LudensCore, described as a native app, provides UI, communication, 3D rendering and a script runtime, and contains no use-case logic. InteractiveCode holds flows such as ordering advice. AI-generated reply candidates pass through InteractiveCode, which applies character and context before output | [Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference) |
| Edge/cloud split | VisualCortex processing moved from servers to the on-site PC because sending video made responses "著しく遅く" (markedly slow) | [Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference) |
| Named platform components | VisualCortex (image recognition), LanguageCortex (natural language), Insight (meaning and search), Ludens Analytics (data analysis) | [Senior Software Engineer posting](https://open.talentio.com/r/1/c/couger/pages/119821) |
| FamilyMart deployment | Tablets in each store; data on sales and customer counts; generative-AI voice search over operating manuals | [FamilyMart 2022](https://www.family.co.jp/company/news_releases/2022/20221128_02.html), [FamilyMart 2024](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) |
| Operations | On-call rotation covering incidents outside hours and on holidays, with an on-call allowance | [Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821), [full-stack](https://open.talentio.com/r/1/c/couger/pages/109446) |

**Organisation.** The deck's org chart places VHA, Fullstack-web (Frontend, Backend, DevOps), Test Automation and Corporate IT under the CTO (技術統括). Product management, customer management, design and QA sit under プロダクト統括. LudensCore, image recognition and natural-language/search teams are drawn between the two ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.19). The Senior Software Engineer posting says development is moving from separate front-end and back-end teams to a single full-stack web team ([posting](https://open.talentio.com/r/1/c/couger/pages/119821)).

**Research output.** The `couger-inc/research` repository lists papers from 2019 to 2023 on skeleton extraction, eye-region segmentation, thermal super-resolution, Instagram filter removal, depth-guided relighting and an intention-based conversation model ([GitHub](https://github.com/couger-inc/research); last commit 2024-07-01).

### Technical background sought

From the postings listed on [careers.couger.co.jp](https://careers.couger.co.jp/) on 2026-10-11, plus Green and paiza:
- **Required:**
  - full-stack web design, development and operation;
  - system architecture, database and Web API design;
  - designing and building cloud infrastructure such as AWS;
  - improving quality through technical discussion and review ([Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821));
  - Web APIs and batch or stream data pipelines on cloud services;
  - back ends on RDBMS, NoSQL or NewSQL ([full-stack](https://open.talentio.com/r/1/c/couger/pages/109446));
  - technology selection, architecture and cross-team technical decisions ([Product Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687));
  - Unity development ([paiza](https://paiza.jp/career/job_offers/28362)).
- **Preferred:**
  - large-scale, high-availability systems;
  - ML or LLM products;
  - event-driven architecture;
  - search engines or vector databases;
  - technical leadership ([Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821));
  - Unity native plugins, server communication over APIs, 3D models and lighting, and releasing a personal game ([paiza](https://paiza.jp/career/job_offers/28362)).
- **ML role responsibilities:** ML models for the dialogue system; dialogue generation, intent understanding and action-suggestion algorithms using LLMs and multimodal models; training pipelines, evaluation, monitoring and automated tests. Requirements are visible only to logged-in users ([Green](https://www.green-japan.com/company/5263/job/301740)).

### Industry domain

- **Convenience-store operations.** The work involves store-manager duties, ordering, merchandising, supervisor (SV) store guidance, and sales and customer-count data ([FamilyMart, 2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)). Retail knowledge is listed as preferred, not required: "小売業界に関する深い知識" for AI implementation consultants ([posting](https://open.talentio.com/r/1/c/couger/pages/84428)) and retail or distribution field data for the data analyst ([posting](https://open.talentio.com/r/1/c/couger/pages/122132)). No engineering posting reviewed lists industry knowledge as required.
- **Measuring impact.** The data-analyst role requires regression, hypothesis testing and causal inference to quantify Rachel's effect on sales and operations ([posting](https://open.talentio.com/r/1/c/couger/pages/122132)).
- **Game AI.** The company presents game AI as the basis of Rachel's design and describes Rachel as operating in "「現実世界」という究極のオープンワールド" (the real world as the ultimate open world). A 2025 deck covers A*, NavMesh, GOAP, behaviour trees and finite-state machines ([Speaker Deck, 2025-05-02](https://speakerdeck.com/couger/xian-shi-shi-jie-toiujiu-ji-noopunwarudogemuwoshi-xian-suruniha)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language (current postings) | Product Tech Lead and Senior QA: Japanese at business level. Full-stack: "ビジネスレベル以上（日本語能力試験N1相当）". Senior Data Analyst and InfoSec: native Japanese. The Senior Software Engineer posting has no language line | [Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687), [full-stack](https://open.talentio.com/r/1/c/couger/pages/109446), [QA](https://open.talentio.com/r/1/c/couger/pages/117722), [analyst](https://open.talentio.com/r/1/c/couger/pages/122132), [InfoSec](https://open.talentio.com/r/1/c/couger/pages/112252) |
| Working language (2022 English postings) | Server Application Engineer: "Highly proficient in spoken and written English". Engineering Manager (ML/AI): English at business level, Japanese at basic level, managing a team "diverse in experience and nationality" | [Server Application Engineer](https://couger.notion.site/ad09a89b538849f585f410ce7ef4706f), [Engineering Manager](https://couger.notion.site/ec98d708d9e94523aa0161dc72b1cf6c); last edited 2022-10-11 |
| Location | Shibuya office, 5 minutes from Shibuya Station | [careers](https://careers.couger.co.jp/) |
| Remote | Hybrid; "フルリモートは不可" (full remote not permitted); in the office for the first month, then frequency at the employee's discretion. Employees must live within commuting distance. FY2025: 34% came in three or more days a week and 66% two days or fewer | [posting](https://open.talentio.com/r/1/c/couger/pages/119821), [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) pp.18, 24 |
| Hours | Fixed hours, 9:00–18:00 or 10:00–19:00 depending on the position | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.24 |
| Salary | Official postings: "非公開" (not disclosed). Green: Product Tech Lead ¥10M–15M; Senior Software Engineer and Senior Software Engineer (ML) ¥8M–12M; Senior Data Analyst ¥7M–12M. paiza Unity posting: ¥5M–12M, including fixed overtime pay for 45 hours | [Green](https://www.green-japan.com/company/5263), [paiza](https://paiza.jp/career/job_offers/28362); accessed 2026-10-11 |
| Overtime and leave (FY2025) | Average overtime 9.6 hours/month. Average paid leave taken 14.6 days/year including sick leave. Plus 3 summer days and 5 sick days per year (2 on joining) | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) pp.18, 24 |
| Benefits | Social insurance (関東ITソフトウェア健康保険組合); commuting allowance up to ¥50,000; communication allowance; the company pays for a social lunch up to once a month | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) pp.24–25 |
| Selection | Document screening, then first, second and final interviews; a technical assignment for engineers; interviews other than the final one can be online | [careers FAQ](https://careers.couger.co.jp/) |
| Team composition | Engineers 49%; customer management 16%; marketing/PR 10%; HR, general affairs and accounting 10%; product management 8%; business planning and sales 4%. Average age 38 for engineers and 35 for product and customer management. Gender ratio 7:3. 20 employees raising children (6 of them women) | [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.18 |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11):
- **Company sites:** careers.couger.co.jp with its 10 Talentio postings, the English Notion careers page, virtualhumanlab.io and sphear.to. The company's own site couger.co.jp is not used as a source on this page because its robots.txt opts out of AI input (`ai-input=no`).
- **Company channels:** the PR TIMES company page (company_id 33615; releases 1–50 checked by number) and the company's Speaker Deck account.
- **GitHub API:** organisation names tried were `couger`, `couger-inc`, `couger-jp`, `CougerInc`, `cougerinc`, `couger-ai`, `couger-lab`, `zkcream`, `ludens`, `ludens-ai`, `virtualhumanlab`, `sphear` and `geneflow`.
- **External sources:** the NTA corporate-number site, gBizINFO, the ITOCHU, FamilyMart, Ridgelinez and Enterprise Ethereum Alliance release pages, Newswitch (日刊工業新聞), 北海道ハイテクノロジー専門学校, the Product History Conference 2024 and JSAI2026 organiser pages, Green, paiza, Wantedly, LinkedIn, STARTUP DB and INITIAL.
- **Web searches:** クーガー株式会社, Couger, LUDENS, レイチェル and コネクトーム, in Japanese and English.

Findings:
- **Funding details.** No amount, stake, valuation, cumulative total or investor other than ITOCHU was found.
- **Revenue and financial statements.** None published. gBizINFO shows no financial-statement, subsidy or procurement records; it lists 4 trademarks and 0 patents ([gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=7010701025073); read 2026-10-11).
- **Pricing** for LUDENS, Rachel or VisualCortex.
- **Customers beyond FamilyMart and the Autobacs trial.** Postings refer to unnamed apparel and retail companies, and an AI-consultant posting mentions enquiries from telecom and finance ([posting](https://open.talentio.com/r/1/c/couger/pages/84428)).
- **Equity or stock options.** No posting reviewed mentions them.
- **Visa sponsorship.** Not stated in any posting reviewed.
- **Security certifications.** None found in the reviewed sources. ISMS appears in the InfoSec posting only as preferred experience ([posting](https://open.talentio.com/r/1/c/couger/pages/112252)). The ISMS, Privacy Mark and SECURITY ACTION registry search forms were not submitted.
- **Engineering blog.** The Medium publication `couger-blog` last posted on 2024-05-22 (RSS feed read 2026-10-11). The Virtual Human Lab blog carries mostly event reports and essays. No organisation was found at `qiita.com/organizations/couger` or `zenn.dev/p/couger` (404).
- **Open source.** `couger-inc` has 10 public repositories: 7 archived and 3 forks. `zkcream` has 6, last pushed 2022-02-25 ([GitHub](https://github.com/couger-inc), [GitHub](https://github.com/zkcream)).
- **Sources that could not be read on 2026-10-11:**
  - CodeZine's Developers Summit 2025 report and the event's session page on event.shoeisha.jp (HTTP 403);
  - TokyoDev (Cloudflare challenge, HTTP 403);
  - medium.com pages (HTTP 403; the RSS feed was read);
  - LinkedIn profile pages (HTTP 999);
  - Buffett Code (HTTP 403);
  - funding data on STARTUP DB and INITIAL (members only);
  - the YOUTRUST report of the Product History Conference talk (client-rendered, no text retrieved);
  - entethalliance-japan.org (no response);
  - Nikkei articles (paywalled; not cited).

### Inconsistencies across sources

- **Store count.** Couger's careers site and deck say about 7,000 or "7,000店舗以上" ([careers](https://careers.couger.co.jp/); Undated; accessed 2026-10-11; [deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki), 2026-10-07). 激流オンライン reports "1万3000店が活用" ([2026-01-30](https://gekiryu-online.jp/2026/01/227822)).
- **Share of FamilyMart stores within the same deck.** Page 8 says "国内全店の半数近く" (nearly half); page 12 says "国内全店舗の半数以上" (more than half) ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)).
- **Reported effect.**
  - Daily sales "平均３―４％" higher than comparable stores ([Newswitch (日刊工業新聞)](https://newswitch.jp/p/26324), 2021-03).
  - "売上5%増" ([careers](https://careers.couger.co.jp/); Undated).
  - "売上の2〜3％向上" across client companies ([analyst posting](https://open.talentio.com/r/1/c/couger/pages/122132), 2026-04-09).
  - Sales +2% on average and an expected ~30% reduction in SV work in pilot stores ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.12).
- **Start of the FamilyMart deployment.**
  - 日刊工業新聞 reported in 2021-03 that stores had used the agent experimentally "昨年から" (since the previous year, i.e. 2020) ([Newswitch, 2021-03-14](https://newswitch.jp/p/26324)).
  - The deck timeline marks "ファミリーマートへレイチェル提供開始" in 2021 ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.11).
  - The 2024 release says the store-manager rollout ran "2023年1月より" ([PR TIMES, 2024-08-07](https://prtimes.jp/main/html/rd/p/000000033.000033615.html)).
- **Virtual Human Lab start date.** A 北海道ハイテクノロジー専門学校 notice of 2020-07-27 describes "バーチャルヒューマンラボ" as an industry-academia education program run with Couger ("株式会社COUGERが連携した産学連携の教育プログラム") ([HHT, 2020-07-27](https://www.hht.ac.jp/news/53284/)). The deck timeline places "バーチャルヒューマンラボを開設" in 2022, described as research on AI and brain science ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.11). Neither source mentions the other.
- **Chief architect.** 五十嵐 智哉 is listed as チーフアーキテクト on the [careers member page](https://careers.couger.co.jp/member) (Undated). 土田 悠貴 is introduced as チーフアーキテクト in the [Virtual Human Lab report](https://virtualhumanlab.io/JP_blog_ArchitectureConference) of the 2025-11-20 talk. Neither source mentions the other.
- **Headcount.**
  - 41 as of 2026-03-31 ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)).
  - 48 ([Green](https://www.green-japan.com/company/5263)) and 46 members ([Wantedly](https://www.wantedly.com/companies/couger)); both undated, accessed 2026-10-11.
  - "11-50 employees" ([LinkedIn](https://www.linkedin.com/company/couger)).
- **Remote policy.**
  - Postings state "フルリモートは不可" ([posting](https://open.talentio.com/r/1/c/couger/pages/119821)).
  - The careers FAQ says "リモートで勤務可能です", with required office days ([careers](https://careers.couger.co.jp/)).
  - A member-survey quote in the deck describes the company as "フルリモート中心" (centred on full remote) ([deck](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) p.21, survey of 2026-03).

### Other

- **Shift in public focus.**
  - Couger's PR TIMES releases from 2018-04 to 2022-04 cover virtual-human work with partners (KDDI; ISID with 京王電鉄), computer-vision competition results, the Blockchain EXE community, and blockchain projects (GeneFlow, OMEGA, ETHTerakoya, zkCREAM, the EEA Japan role).
  - From 2022-11 to 2025-06, the releases cover Rachel at FamilyMart and competition results.
  - Of the 13 Couger releases retrieved from PR TIMES dated 2025-07-03 to 2026-10-09, 12 announce Sphear events; two further release numbers in that range (42 and 47) returned 404 ([PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/33615)). Sphear #1 to #6 were each priced at ¥3,000 with 30 seats ([#1, 2025-07-03](https://prtimes.jp/main/html/rd/p/000000036.000033615.html), [#6, 2026-01-08](https://prtimes.jp/main/html/rd/p/000000043.000033615.html)).
- **Name collision.** A GitHub organisation named `LUDENS-AI` (created 2024-07-19; unverified; no website, email or company field) has a Chinese-language repository built around Feishu login. No connection to Couger was established ([GitHub — LUDENS-AI](https://github.com/LUDENS-AI)).
- **English careers page.** The English Notion careers page was last edited 2023-10-31 and lists only the two 2022 postings. The current careers site and all current postings are in Japanese ([Notion](https://couger.notion.site/Careers-Couger-Inc-35ada7ab0ed34c1baff8dac5f86b5636), [careers](https://careers.couger.co.jp/)).

---

## Resources

**Official**

- [PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/33615)
- [Company deck, 2026-10-07 (Speaker Deck, JA)](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) · [Game AI deck, 2025-05-02 (JA)](https://speakerdeck.com/couger/xian-shi-shi-jie-toiujiu-ji-noopunwarudogemuwoshi-xian-suruniha)
- [Careers site (JA)](https://careers.couger.co.jp/) · [Members](https://careers.couger.co.jp/member)
- Talentio postings (JA) — [Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821) · [Full-stack Engineer](https://open.talentio.com/r/1/c/couger/pages/109446) · [Product Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687) · [Senior QA Engineer](https://open.talentio.com/r/1/c/couger/pages/117722) · [Senior Data Analyst](https://open.talentio.com/r/1/c/couger/pages/122132) · [InfoSec / Corporate IT](https://open.talentio.com/r/1/c/couger/pages/112252) · [Project Manager](https://open.talentio.com/r/1/c/couger/pages/84099) · [Technical Account Manager](https://open.talentio.com/r/1/c/couger/pages/84100) · [AI Implementation Consultant](https://open.talentio.com/r/1/c/couger/pages/84428)
- [English careers page (Notion)](https://couger.notion.site/Careers-Couger-Inc-35ada7ab0ed34c1baff8dac5f86b5636) — [Server Application Engineer](https://couger.notion.site/ad09a89b538849f585f410ce7ef4706f) · [Engineering Manager (ML/AI)](https://couger.notion.site/ec98d708d9e94523aa0161dc72b1cf6c)
- [Virtual Human Lab](https://virtualhumanlab.io/) — [Architecture Conference 2025 report (JA)](https://virtualhumanlab.io/JP_blog_ArchitectureConference) · [Sphear](https://sphear.to/)
- GitHub — [couger-inc](https://github.com/couger-inc) · [org API](https://api.github.com/orgs/couger-inc) · [public members API](https://api.github.com/orgs/couger-inc/public_members) · [cream](https://github.com/couger-inc/cream) · [research](https://github.com/couger-inc/research) · [zkcream](https://github.com/zkcream)

**Press releases (PR TIMES, JA — newest first)**

- [Sphear #13 (company profile box) — 2026-10-09](https://prtimes.jp/main/html/rd/p/000000050.000033615.html)
- [Sphear #6 — 2026-01-08](https://prtimes.jp/main/html/rd/p/000000043.000033615.html)
- [SSBC 2025 first place — 2025-07-10](https://prtimes.jp/main/html/rd/p/000000037.000033615.html)
- [Sphear launch and #1 — 2025-07-03](https://prtimes.jp/main/html/rd/p/000000036.000033615.html)
- [CVPR 2025 workshop paper — 2025-06-17](https://prtimes.jp/main/html/rd/p/000000035.000033615.html)
- [~7,000 FamilyMart stores, generative AI — 2024-08-07](https://prtimes.jp/main/html/rd/p/000000033.000033615.html)
- [CVPR 2024 MIPI — 2024-07-23](https://prtimes.jp/main/html/rd/p/000000032.000033615.html)
- [CEO as FamilyMart generative AI adviser — 2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html)
- [ECCV 2022 challenge — 2023-01-23](https://prtimes.jp/main/html/rd/p/000000030.000033615.html)
- [Rachel for FamilyMart, 5,000 stores — 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)
- [CEO as EEA Japan representative — 2022-04-07](https://prtimes.jp/main/html/rd/p/000000028.000033615.html)
- [zkCREAM verification with law firm — 2022-01-31](https://prtimes.jp/main/html/rd/p/000000027.000033615.html)
- [ICCV 2021 award — 2021-11-29](https://prtimes.jp/main/html/rd/p/000000026.000033615.html)
- [zkCREAM grant — 2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html)
- [Ethereum Foundation partnership — 2021-02-10](https://prtimes.jp/main/html/rd/p/000000023.000033615.html)
- [CVPR 2020 challenge — 2020-06-29](https://prtimes.jp/main/html/rd/p/000000022.000033615.html)
- [ETHTerakoya launch — 2020-05-25](https://prtimes.jp/main/html/rd/p/000000021.000033615.html)
- [GeneFlow beta — 2020-04-14](https://prtimes.jp/main/html/rd/p/000000020.000033615.html)
- [OMEGA with アクト — 2020-01-27](https://prtimes.jp/main/html/rd/p/000000018.000033615.html)
- [ITOCHU alliance — 2020-01-20](https://prtimes.jp/main/html/rd/p/000000017.000033615.html)
- [OpenEDS challenge — 2019-10-16](https://prtimes.jp/main/html/rd/p/000000011.000033615.html)
- [Connectome SDK and adviser 山川 宏 — 2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)
- [VHA field trial at トリエ京王調布 — 2019-06-26](https://prtimes.jp/main/html/rd/p/000000009.000033615.html)
- [GeneFlow (Connectome) — 2018-06-29](https://prtimes.jp/main/html/rd/p/000000005.000033615.html)
- [VHA and KDDI project — 2018-04-26](https://prtimes.jp/main/html/rd/p/000000002.000033615.html)

**Third-party coverage and profiles**

- [NTA corporate number site — 7010701025073 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073) · [gBizINFO (JA)](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=7010701025073)
- [Enterprise Ethereum Alliance — 86 new members, 2017-05-22](https://entethalliance.org/enterprise-ethereum-alliance-expands-dramatically-announcing-86-new-members/)
- [ITOCHU — investment in Couger, 2020-01-20 (JA)](https://www.itochu.co.jp/ja/news/press/2020/200120.html)
- FamilyMart (JA) — [2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html) · [2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) · [2026-01-13](https://www.family.co.jp/company/news_releases/2026/20260113_02.html)
- [Ridgelinez — Autobacs trial, 2024-08-01 (JA)](https://www.ridgelinez.com/news/news_20240801/)
- [Newswitch (日刊工業新聞) — FamilyMart store-manager agent, 2021-03-14 (JA)](https://newswitch.jp/p/26324)
- [激流オンライン — FamilyMart AI feature, 2026-01-30 (JA)](https://gekiryu-online.jp/2026/01/227822)
- [北海道ハイテクノロジー専門学校 — Virtual Human Lab program, 2020-07-27 (JA)](https://www.hht.ac.jp/news/53284/)
- [WIRED — CEO interview, 2022-05-16 (JA)](https://wired.jp/article/the-next-innovators-3-atsushi-ishii/)
- [SBBIT — CEO interview, 2018-06-11 (JA)](https://www.sbbit.jp/article/cont1/34986)
- [Green — CEO interview (JA)](https://www.green-japan.com/interview/5263) · [company and postings (JA)](https://www.green-japan.com/company/5263) · [Senior Software Engineer (ML) (JA)](https://www.green-japan.com/company/5263/job/301740)
- [paiza — Unity engineer posting, updated 2024-12-20 (JA)](https://paiza.jp/career/job_offers/28362)
- [Wantedly (JA)](https://www.wantedly.com/companies/couger) · [LinkedIn](https://www.linkedin.com/company/couger)
- [STARTUP DB (JA)](https://startup-db.com/companies/vNOKZXOUwDAp185L) · [INITIAL / Speeda (JA)](https://initial.inc/investors/V11957)
- Event organisers (JA) — [Product History Conference 2024 (YOUTRUST)](https://lp-prohis.youtrust.jp/2024/) · [JSAI2026 sponsors](https://www.ai-gakkai.or.jp/jsai2026/sponsor/)
- [GitHub — LUDENS-AI (unrelated name collision; no link established)](https://github.com/LUDENS-AI)
