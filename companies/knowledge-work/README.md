# Knowledge Work

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Knowledge Work (株式会社ナレッジワーク, "Knowledge Work Inc." in the site footer) is a Tokyo company registered in March 2020 and counting 2020-04-01 as its founding day. It launched a sales-enablement cloud also called **ナレッジワーク** in April 2022 and now sells what it calls "セールスAIエージェント" (sales AI agents) to large Japanese enterprises through three lines: **Sales AX Consulting**, **Sales AI Products** (AI meeting recording, AI role-play, partner-sales support and the original knowledge-sharing module), and a **Sales AI Agent OS** launched 2026-08-04 ([service site](https://knowledgework.cloud/); Undated; accessed 2026-10-11). Corporate number 4010401151825 ([法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825); information as of 2026-10-11).

- Funding: **シリーズC 1stクローズ 35億円** (third-party allotment) announced [2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html), led by Globis Capital Partners, with ten new corporate/CVC investors including Ricoh Japan, SMBC and NTT Docomo Ventures. The last company-stated cumulative total is **61.2億円** after the Series B ([2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)); no post-Series C cumulative figure was published.
- Headcount: **205** employees as of 2026-02, "about half" involved in product development ([engineering recruiting page](https://knowledgework.com/recruit/engineering); accessed 2026-10-11); **233** full-time employees as of 2026-07 ([HERP posting](https://herp.careers/v1/kwork/ZxZYCOkWex9k); accessed 2026-10-11).
- Acquired 100% of Poetics (meeting-analysis AI "JamRoll") on [2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) and merged it on 2025-06-30 ([2025-07-01](https://prtimes.jp/main/html/rd/p/000000088.000063428.html); [registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825)).
- Engineering, from the company's own technical writing: **Go** backend in a 100+-module monorepo, **protobuf / Connect RPC** shared between backend and **TypeScript / React / Next.js** frontend, **Google Cloud** (Cloud Run, Cloud SQL for PostgreSQL, BigQuery), with LLM calls to Gemini, GPT and Claude ([Zenn, 2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c); [Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)). Engineering postings reviewed are Japanese-language and the new-graduate engineer posting requires JLPT N1 or equivalent ([HERP](https://herp.careers/v1/kwork/ZxZYCOkWex9k); accessed 2026-10-11).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | ナレッジワーク / Knowledge Work; service site tagline 「セールスAIエージェント」 | [knowledgework.com](https://knowledgework.com/), [knowledgework.cloud](https://knowledgework.cloud/); accessed 2026-10-11 |
| Legal name | 株式会社ナレッジワーク; no English name is registered with the National Tax Agency; the site footer uses "Knowledge Work Inc." | [法人番号公表サイト (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825), [EN record](https://www.houjin-bangou.nta.go.jp/en/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| Corporate number | 4010401151825; designated 2020-03-23 | [法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| Incorporation / founding | 設立日 2020-03-18; 創業日 2020-04-01 (both stated in company releases) | [2026-08-04 release](https://prtimes.jp/main/html/rd/p/000000148.000063428.html), [company page](https://knowledgework.com/company) |
| HQ | 〒106-0041 東京都港区麻布台1丁目3-1 麻布台ヒルズ森JPタワー51F; registered address changed to 麻布台1丁目3番1号 on 2026-03-03 | [company page](https://knowledgework.com/company); [registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| Representative | 代表取締役 CEO/CPO 麻野 耕司 (Koji Asano) | [company page](https://knowledgework.com/company) |
| Capital | 97.4億円 including capital reserve (資本準備金等含む) | [company page](https://knowledgework.com/company); Undated; accessed 2026-10-11 |
| Headcount | 205 (as of 2026-02); 233 full-time employees (as of 2026-07) | [recruiting page](https://knowledgework.com/recruit/engineering), [HERP posting](https://herp.careers/v1/kwork/ZxZYCOkWex9k) |
| Engineering working language | No stated policy; engineering postings are written in Japanese, and the new-graduate engineer and intern postings require JLPT N1 or equivalent business communication (see `Working conditions`) | [HERP new-grad posting](https://herp.careers/v1/kwork/ZxZYCOkWex9k); accessed 2026-10-11 |
| Customers | No aggregate count published; releases describe deployments "主に大手企業に数千名規模" (mainly large companies, at the scale of thousands of users), naming NTT Docomo Business, Mizuho Bank and Nissin Foods | [2026-08-04 release](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) |
| Total raised | 61.2億円 cumulative after the Series B; 35億円 Series C 1st close announced since, with no updated cumulative total | [2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html), [2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) |
| Investors named in the latest release | Existing: グロービス・キャピタル・パートナーズ (lead), DNX Ventures, WiL, Salesforce Ventures, フォースタートアップスキャピタル. New since Series B: see `Funding` | [2026-08-04 release](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) |
| Security certifications | ISO/IEC 27001 (IS 750583, first registered 2021-09-15); ISO/IEC 27017 (CLOUD 791569, 2023-12-13); ISO/IEC 27701 (PM 807882, 2024-09-01); SOC 2 Type 1 report for the "ナレッジワーク" product series, reference date 2026-02-28, obtained 2026-03-26 | [ISMS registry 27001](https://isms.jp/lst/ind/CR_IS_x0020_750583.html), [ISMS registry 27017](https://isms.jp/isms-cls/lst/ind/CR_CLOUD_x0020_791569.html), [2024-09-26](https://prtimes.jp/main/html/rd/p/000000048.000063428.html), [2026-04-02](https://prtimes.jp/main/html/rd/p/000000123.000063428.html) |
| Mission | 「LIFE WITH ENABLEMENT できる喜びが巡る日々を届ける」 (adopted 2025-07-11; earlier releases use 「できる喜びが巡る日々を届ける」) | [homepage](https://knowledgework.com/), [2025-07-11](https://prtimes.jp/main/html/rd/p/000000089.000063428.html) |
| Public accounts | X `@kworkcom`; GitHub `knowledge-work`; Speaker Deck `kworkdev`; Zenn publication `knowledgework`; note `knowledgework` | [homepage](https://knowledgework.com/), [Speaker Deck profile](https://speakerdeck.com/kworkdev) |

**Awards and recognitions announced by the company**: 2022 Good Design Award ([2022-10-07](https://prtimes.jp/main/html/rd/p/000000012.000063428.html)); BOXIL SaaS AWARD 2023, sales & marketing category first place ([2023-05-15](https://prtimes.jp/main/html/rd/p/000000017.000063428.html)); Salesforce Japan Partner Award 2025 ([2025-04-10](https://prtimes.jp/main/html/rd/p/000000069.000063428.html)); Japan CxO Award, technology category top prize, to CTO 川中 真耶 ([2025-12-17](https://prtimes.jp/main/html/rd/p/000000101.000063428.html)). Patents announced: Knowledge AI Recommend ([2023-04-27](https://prtimes.jp/main/html/rd/p/000000021.000063428.html)), the "hover enlarge & preview" UI ([2024-03-05](https://prtimes.jp/main/html/rd/p/000000039.000063428.html)) and viewer display speed-up ([2024-03-06](https://prtimes.jp/main/html/rd/p/000000038.000063428.html)). The R&D page states that Poetics was selected for the AWS Generative AI Accelerator, a Google global accelerator and an AWS LLM development support program, and that Knowledge Work succeeded to these after the merger ([R&D](https://knowledgework.com/rd); accessed 2026-10-11).

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| 株式会社ナレッジワーク | Legal entity | Japan; corporate number designated 2020-03-23; active | Operator of the knowledgework.com and knowledgework.cloud sites | [registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| 株式会社Poetics | Former subsidiary, merged | Japan (Shibuya); corporate number 9010001187389; 100% acquired 2025-05-01, absorbed 2025-06-30 | Developer of "JamRoll" and "Poetics Speech API"; Knowledge Work is the surviving company | [registry](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825), [2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html), [2025-07-01](https://prtimes.jp/main/html/rd/p/000000088.000063428.html) |
| kwork.studio | Former corporate-site domain | Used in releases through 2023-11; now redirects to knowledgework.com | HERP job pages still list it as the corporate site | [2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html), [HERP posting](https://herp.careers/careers/companies/kwork/jobs/w4Ks8k8FyIrE) |

Registered head-office history (registry): 港区海岸 (2020-03) → a Kōtō-ku address (from 2020-07-14) → 港区港南2丁目 (from 2020-08-14) → 港区西新橋1丁目 (from 2022-08-15) → 港区虎ノ門4丁目 (神谷町トラストタワー, from 2024-02-02) → 港区麻布台1丁目 (from 2026-03-03). The company announced the move to Azabudai Hills on [2026-02-16](https://prtimes.jp/main/html/rd/p/000000116.000063428.html), with a customer-facing "パークエリア", and the grand opening of the 「デジタルイネーブルメントパーク」 on [2026-09-04](https://prtimes.jp/main/html/rd/p/000000156.000063428.html).

### Market context as stated by the company

From the [Series C release (2026-08-04)](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) and the [service site](https://knowledgework.cloud/):

- It cites MIT Project NANDA's "The GenAI Divide: State of AI in Business 2025" for the claim that 95% of enterprise generative-AI deployments fail to deliver ROI.
- It attributes this to "水平型ユースケース" (company-wide copilots and chatbots) and argues for "垂直型ユースケース" (function-specific agents), citing McKinsey.
- It describes Japanese sales productivity as very low, framed as two problems: 「営業効率」 (time lost to preparation and internal work) and 「営業成果」 (variance between reps).

---

## Product

### Line-up

The service site organizes the offering into three series (accessed 2026-10-11):

| Series | What it is, as described | Named components | Page |
|---|---|---|---|
| セールスAXコンサルティングシリーズ (Sales AX Consulting) | Builds and operates AI agents customized to a customer's sales operations, delivered by consultants and engineers | セールスAXプランニング; データマネジメント・オペレーション; セールスイネーブルメント・コンサルティング; カスタマイズセールスAIエージェント構築; セールスイネーブルメント・トレーニング | [consulting](https://knowledgework.cloud/consulting) |
| セールスAIプロダクトシリーズ (Sales AI Products) | Packaged AI products for standard sales work | ナレッジワークAI商談記録 (meeting recording); ナレッジワークAI営業ロープレ (AI role-play); ナレッジワーク for パートナーセールス (agency/partner sales) | [products](https://knowledgework.cloud/products) |
| セールスAIエージェントOSシリーズ (Sales AI Agent OS) | Base layer for building and running sales agents with company-specific data and strategy | セールスAIエージェントOS; セールスナレッジデータベース; セールスノウハウデータベース | [agentos](https://knowledgework.cloud/agentos) |

The Sales AI Agent OS is described as four layers: an ontology layer linking each company's sales data in sales context, a strategy layer that feeds the company's sales strategy to agents, an agent layer that implements, manages and analyzes agents, and an interface layer ([2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html); [CTO/CAIO interview](https://knowledgework.com/why-enablement/4)). The consulting and product series are stated to run on top of it.

Product history, from company releases:

- **2022-04-20** — general availability of the 「セールスイネーブルメントクラウド」 "ナレッジワーク", covering 「ナレッジ領域」, 「ラーニング領域」 and 「ワーク領域」 ([release](https://prtimes.jp/main/html/rd/p/000000003.000063428.html)); Salesforce AppExchange app "Knowledge Work for Salesforce" on [2022-10-24](https://prtimes.jp/main/html/rd/p/000000011.000063428.html).
- **2023-04** — "AI Integration Lab" set up and "Knowledge AI Chat" using ChatGPT released ([2023-04-25](https://prtimes.jp/main/html/rd/p/000000020.000063428.html), [2023-04-26](https://prtimes.jp/main/html/rd/p/000000022.000063428.html)).
- **2024-12-05** — learning product 「ラーニングイネーブルメント」 ([release](https://prtimes.jp/main/html/rd/p/000000056.000063428.html)).
- **2025-02-18** — concept renamed 「セールスイネーブルメントAI」; three new modules, 「ナレッジ資料作成」 (PowerPoint add-in), 「ワーク商談推進」 (knowledge recommendations from Salesforce opportunity data) and 「ワーク社外共有」, added to the main 「ナレッジ社内共有」 module ([release](https://prtimes.jp/main/html/rd/p/000000063.000063428.html)).
- **2025-05-15** — 「ナレッジワークAI商談記録」, built on Poetics' JamRoll technology ([release](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)); later extended to PC-browser and Android recording ([2025-10-22](https://prtimes.jp/main/html/rd/p/000000097.000063428.html)), Salesforce custom objects ([2026-01-14](https://prtimes.jp/main/html/rd/p/000000108.000063428.html)), carrier calls on NTT Docomo/au/SoftBank written to Salesforce ([2026-04-27](https://prtimes.jp/main/html/rd/p/000000125.000063428.html)) and a Windows desktop app ([2026-06-05](https://prtimes.jp/main/html/rd/p/000000131.000063428.html)).
- **2025-11-28** — 「ナレッジワークAI営業ロープレ」, role-play training with AI avatars ([release](https://prtimes.jp/main/html/rd/p/000000098.000063428.html)).
- **2026-01-16** — concept renamed 「セールスAXソリューション」 and consulting unit 「ナレッジワーク X」 launched ([release](https://prtimes.jp/main/html/rd/p/000000110.000063428.html)); followed by 「ナレッジワーク for パートナーセールス」 ([2026-02-04](https://prtimes.jp/main/html/rd/p/000000113.000063428.html)), 「ナレッジワークカスタマイズAIエージェント」 ([2026-02-06](https://prtimes.jp/main/html/rd/p/000000114.000063428.html)) and 「ナレッジワーク資料作成エージェント」 ([2026-03-13](https://prtimes.jp/main/html/rd/p/000000119.000063428.html)).
- **2026-05-20** — 「ナレッジワークMCPサーバー」 for 社内共有 and AI商談記録, to be extended to all products ([release](https://prtimes.jp/main/html/rd/p/000000127.000063428.html)); an Agentforce-linked package for financial-sector sales on [2026-05-27](https://prtimes.jp/main/html/rd/p/000000128.000063428.html).
- **2026-08-04** — Sales AI Agent OS; **2026-08-06** — R&D on industry-specific sales LLMs based on open-weight models announced ([release](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)).

### Commercialization

Sold mainly to large enterprises as per-user cloud products plus consulting. No public price list was found on the service site; it offers document downloads, demos and a contact form. The only published price found is for AI商談記録: list price ¥5,000 per user per month, offered at ¥2,500 for applications through March 2026, limited to companies with 1,000+ employees ([2025-05-15](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)). Resale and co-delivery channels announced include Ricoh Japan ("ナレッジワークAI商談記録 for RICOH", [2026-08-04](https://prtimes.jp/main/html/rd/p/000000149.000063428.html)), NTT Docomo Business ([2026-08-17](https://prtimes.jp/main/html/rd/p/000000152.000063428.html)) and SMBC Group's プラリタウン ([2026-08-20](https://prtimes.jp/main/html/rd/p/000000154.000063428.html)).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2022-04-20 | Already deployed in sales departments at "複数の大手企業・中堅企業" after a closed beta | [release](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) |
| 2023-10-02 | Ricoh Japan deploying to about 12,000 people, of whom about 7,600 are sales staff | [release](https://prtimes.jp/main/html/rd/p/000000032.000063428.html) |
| 2025-02-18 | Building sales AI agents with "開発人員100人規模" (development staff of about 100) | [release](https://prtimes.jp/main/html/rd/p/000000063.000063428.html) |
| 2026-02 | 205 employees; about half involved in product development; average age 36.32; 95.2% mid-career hires | [recruiting page](https://knowledgework.com/recruit/engineering); accessed 2026-10-11 |
| 2026-07 | 233 full-time employees | [HERP posting](https://herp.careers/v1/kwork/ZxZYCOkWex9k); accessed 2026-10-11 |
| 2026-10-01 | YouTube channel "NEW SALES チャンネル" passed 200,000 subscribers 1 year 8 months after launch | [release](https://prtimes.jp/main/html/rd/p/000000158.000063428.html) |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2022-06-17](https://prtimes.jp/main/html/rd/p/000000006.000063428.html) | Salesforce Ventures, Uzabase, Sansan, One Capital | Series A 2nd-close investors; business tie-ups with SalesTech companies |
| [2023-06-21](https://prtimes.jp/main/html/rd/p/000000023.000063428.html) | NTT Communications | Deployment toward 5,000-person use |
| [2023-10-02](https://prtimes.jp/main/html/rd/p/000000032.000063428.html) | リコージャパン | About 12,000 users |
| [2024-04-22](https://prtimes.jp/main/html/rd/p/000000041.000063428.html) | みずほ銀行 | About 5,000 users |
| [2025-01-07](https://prtimes.jp/main/html/rd/p/000000059.000063428.html) | JTB | 5,500 users in corporate sales |
| [2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) | Poetics | Acquisition of all shares |
| [2025-09-26](https://prtimes.jp/main/html/rd/p/000000094.000063428.html) | キリンビール | 社内共有, about 2,500 users |
| [2025-10-31](https://prtimes.jp/main/html/rd/p/000000096.000063428.html) | パートナープロップ | Strategic partnership; entry into partner enablement |
| [2026-03-30](https://prtimes.jp/main/html/rd/p/000000122.000063428.html) | リコージャパン | AI商談記録 to about 6,000 people |
| [2026-07-28](https://prtimes.jp/main/html/rd/p/000000140.000063428.html) | 日本電気 (NEC) | AI商談記録 at 1,000-person scale |
| [2026-08-04](https://prtimes.jp/main/html/rd/p/000000149.000063428.html) | リコージャパン | Capital and business alliance; joint proposals, SI and possible joint development |
| [2026-08-17](https://prtimes.jp/main/html/rd/p/000000152.000063428.html) | NTTドコモビジネス | Strategic partnership for sales AX |

Other named deployments since 2025 include KDDI, Mitsubishi HC Capital, Suntory, Hitachi Systems, Hokuriku Bank, Hokkaido Bank, Mitsui Sumitomo Insurance and NN Life (see the [PR TIMES company feed](https://prtimes.jp/main/html/searchrlp/company_id/63428)); each is a single-company adoption release.

### Stated plans

- Series B (2023-11-29): release ten new products in three years, starting with a work-area product in April 2024 and a learning-area product in July 2024 ([release](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)).
- ナレッジワーク X (2026-01-16): hire about 200 consulting professionals over three years ([release](https://prtimes.jp/main/html/rd/p/000000110.000063428.html)).
- SOC 2 (2026-04-02): aims to obtain a Type 2 report ([release](https://prtimes.jp/main/html/rd/p/000000123.000063428.html)).
- Series C (2026-08-04): capital and business alliances and CVC partnerships with industry-leading companies, and accelerated development of the Agent OS ([release](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)).
- Industry LLM (2026-08-06): sales LLMs specialized by industry (telecom, IT, banking, insurance, securities, manufacturing, infrastructure, retail, services), trained and run in environments controlled by the company or customers ([release](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)).

---

## Founder

**麻野 耕司 (Koji Asano)** — founder, 代表取締役 CEO/CPO ([company page](https://knowledgework.com/company), [leaders page](https://knowledgework.com/member)).

- 2003: graduated from Keio University, Faculty of Law; joined Link and Motivation.
- 2016: launched 「モチベーションクラウド」, described as Japan's first organization-improvement cloud; 2018: director of Link and Motivation.
- April 2020: founded Knowledge Work. Author of 『NEW SALES』 (Diamond, [2022-06-08](https://prtimes.jp/main/html/rd/p/000000004.000063428.html)), 『THE TEAM』 and 『すべての組織は変えられる』 ([leaders page](https://knowledgework.com/member)).

**川中 真耶 (`@mayah`)** — co-founder, CTO ([leaders page](https://knowledgework.com/member)).

- 2006: master's degree, Computer Science, Graduate School of Information Science and Technology, University of Tokyo; joined IBM Japan Tokyo Research Laboratory as a researcher in web security and web accessibility ([HERP posting](https://herp.careers/v1/kwork/UM-xWCFZCVDN)).
- 2011: joined Google as a software engineer, working on Chrome.
- 2020: co-founded Knowledge Work. Competed in the ACM ICPC World Finals; technical supervisor of the manga 「王様達のヴァイキング」 ([leaders page](https://knowledgework.com/member)).
- Set up the company's FDE (Forward Deployed Engineer) group as its first member and now leads a unit covering FDE work and Agent OS development ([note, 2026-08-28](https://note.com/knowledgework/n/n5c7dd150abd1)).

**吉田 真麻 (`@yoshiko`)** — her leaders-page bio reads 「2020年、株式会社ナレッジワーク共同創業」; previously Goodpatch (2015) and FOLIO (2017); first frontend engineer from founding ([Zenn, 2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)); 専門役員 Principal / software engineer from 2023; Google Developer Expert ([leaders page](https://knowledgework.com/member), [HERP posting](https://herp.careers/v1/kwork/UM-xWCFZCVDN)).

### Selected leadership

| Name | Role as listed | Stated background | Source |
|---|---|---|---|
| 山崎 はずむ | CAIO | Former CEO of Poetics; joined via the 2025 acquisition; University of Tokyo doctoral program (completed without degree); NYU visiting researcher | [leaders page](https://knowledgework.com/member), [2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) |
| 古森 茂幹 | 取締役 CSO | Hewlett-Packard Japan (director 2009, representative director and executive vice president 2014); Salesforce Japan (vice president from 2015, director and vice chairman 2024) | [leaders page](https://knowledgework.com/member), [2025-02-20](https://prtimes.jp/main/html/rd/p/000000065.000063428.html) |
| 田口 槙吾 | CRO (from 2026-08) | Sansan; Uzabase (FORCAS business CEO); joined 2024 | [leaders page](https://knowledgework.com/member), [2026-08-10](https://prtimes.jp/main/html/rd/p/000000153.000063428.html) |
| 木村 秀夫 (`@hidek`) | 上級執行役員 SVP, software engineer; VPoE | GMO Internet; DeNA (executive officer from 2013); Merpay VP of Engineering (2018); joined 2023 | [leaders page](https://knowledgework.com/member), [2023-09-01](https://prtimes.jp/main/html/rd/p/000000028.000063428.html) |
| 渡邊 尚吾 (`@shogo`) | 執行役員 VP, software engineer | Google Cloud Japan pre-sales engineer (2020); joined 2023; Google Cloud Champion Innovator | [leaders page](https://knowledgework.com/member), [HERP posting](https://herp.careers/v1/kwork/UM-xWCFZCVDN) |
| 日野 隆史 | 執行役員 VP, security management (from 2026-07) | SMBC; Yahoo Japan (ISMS, incident management); Z Holdings; LINE Yahoo | [leaders page](https://knowledgework.com/member), [2026-07-01](https://prtimes.jp/main/html/rd/p/000000138.000063428.html) |
| 竹内 健太 | 執行役員 VP, finance (from 2026-09) | Morgan Stanley (M&A advisory); BizReach; Wharton MBA | [leaders page](https://knowledgework.com/member), [2026-09-01](https://prtimes.jp/main/html/rd/p/000000155.000063428.html) |
| 油井 誠 (`@myui`) | AI engineer leading Agent OS, industry-LLM and AI R&D (joined 2026-07-01) | PhD in engineering (NAIST); AIST senior researcher; Treasure Data senior principal engineer from 2015; developer of the Hivemall ML library | [2026-08-07](https://prtimes.jp/main/html/rd/p/000000151.000063428.html) |

Board and advisors announced in releases: outside directors 今野 穣 (Globis Capital Partners) and 倉林 陽 (DNX Ventures), and part-time auditor 掛川 紗矢香 (ex-Mercari), from [2022-04-20](https://prtimes.jp/main/html/rd/p/000000003.000063428.html); outside directors 難波 俊充 (WiL) and 福山 太郎 (Fond founder) from [2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html); 樋口 泰行, former chairman of Microsoft Japan, as executive advisor from [2026-04-20](https://prtimes.jp/main/html/rd/p/000000124.000063428.html). Go specialist 上田 拓也 (`@tenntenn`) joined to start an "engineer enablement" business ([2022-12-16](https://prtimes.jp/main/html/rd/p/000000016.000063428.html)). The [leaders page](https://knowledgework.com/member) also lists VPs and principals for solution growth, financial-sector accounts, AX consulting, customer success, production, HR, account management, business architecture, sales enablement, product design, corporate and talent management.

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Before 2022-04 (undisclosed at the time) | シードラウンド, プレシリーズAラウンド | not disclosed separately | グロービス・キャピタル・パートナーズ and DNX Ventures (leads of all rounds to date), ANRI, XTech Ventures | — | [2022-04-20](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) |
| 2022-04-20 | シリーズAラウンド 1stクローズ (第三者割当増資) | 10億円 | Leads: グロービス・キャピタル・パートナーズ, DNX Ventures; also ANRI, XTech Ventures | 14.2億円 (including the previously undisclosed rounds) | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) |
| 2022-06-17 | シリーズAラウンド 2ndクローズ (第三者割当増資) | 2億円 (Series A total 12億円) | Salesforce Ventures, ユーザベース, Sansan, One Capital | 16.2億円 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000006.000063428.html) |
| 2023-11-29 | シリーズBラウンド (第三者割当増資) | 45億円 | Leads: WiL, グロービス・キャピタル・パートナーズ; existing investors and フォースタートアップスキャピタル等 | 61.2億円 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000063428.html) |
| 2026-08-04 | シリーズCラウンド 1stクローズ (第三者割当増資) | 35億円 | Lead: グロービス・キャピタル・パートナーズ. New: リコージャパン, Canon Marketing Japan MIRAI Fund, NTTドコモ・ベンチャーズ, 三井住友銀行, ゆうちょアセットマネジメント (via JPSグロース・インベストメント投資事業有限責任組合), 三菱UFJイノベーション・パートナーズ, 三井住友信託銀行, フコクCVCファンド－THE MUTUAL for Next 100－, 電通ベンチャーズSGPファンド, 博報堂DYベンチャーズ. Existing: DNX Ventures, WiL, Salesforce Ventures, フォースタートアップスキャピタル | not stated | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000148.000063428.html), [company news](https://knowledgework.com/news/article/jQM8vm0U) |

Globis Capital Partners' partner states in the Series C release that the firm has participated as lead investor continuously "from the founding round"; in the Series B release he described that round as its third follow-on since the founding investment. フォースタートアップス says its group has supported Knowledge Work's recruiting since 2020 and first invested in November 2023 ([2026-08-04](https://prtimes.jp/main/html/rd/p/000000469.000032589.html)). Canon Marketing Japan and Global Brain (general partner of the Canon MJ MIRAI Fund and of the フコク fund) both describe the August 2026 investment by the Canon MJ fund as 「追加出資」 (additional investment) ([Canon MJ](https://prtimes.jp/main/html/rd/p/000001442.000013943.html), [Global Brain](https://prtimes.jp/main/html/rd/p/000000609.000047342.html)); see `Notes`. The Series C was announced alongside the Agent OS launch and the Ricoh Japan capital and business alliance; the Series A 1st close was announced with the product's general availability.

---

## Engineering

### Technology stack and platforms

Confirmed by the company's own technical writing (Zenn publication, Speaker Deck, certification scope) unless marked otherwise.

- **Backend:** Go, in a monorepo of 100+ Go modules with local dependencies resolved through `replace` directives ([Zenn, 2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c)). Schema-first APIs in **Protocol Buffers**; the company states that knowledge shared between frontend and backend, including authentication and authorization conditions, is written in protobuf ([Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)). RPC via **Connect RPC (gRPC)** ([Zenn, 2026-03-06](https://zenn.dev/knowledgework/articles/6962837cd41940)); in 2021 the frontend called REST endpoints on Extensible Service Proxy, which forwarded to gRPC servers ([Zenn, 2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)).
- **Frontend:** TypeScript, React, Next.js, CSS Modules, Storybook; Figma for design ([Zenn, 2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)); Connect ES migrated from v1 to v2 ([Zenn, 2026-03-31](https://zenn.dev/knowledgework/articles/0d01d7aee48082)); Vitest replaced Jest ([Zenn, 2023-12-26](https://zenn.dev/knowledgework/articles/jest-to-vitest)); Playwright for E2E.
- **Cloud:** Google Cloud. The ISO 27017 scope names Knowledge Work as a cloud service customer of Google Cloud ([ISMS registry](https://isms.jp/isms-cls/lst/ind/CR_CLOUD_x0020_791569.html)). Services named in technical posts: Cloud Run and Cloud Deploy ([Zenn, 2024-02-26](https://zenn.dev/knowledgework/articles/cloud-deploy-for-cloud-run)), Cloud Tasks and Cloud Scheduler ([Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)), Cloud SQL for PostgreSQL with read replicas ([Zenn, 2026-03-12](https://zenn.dev/knowledgework/articles/9956b686e28324)), BigQuery fed by Datastream, with dbt run as Cloud Run Jobs, across dev/qa/stg/prd projects ([Zenn, 2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905)). Search runs on Elasticsearch ([Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)).
- **AWS (inherited):** the former Poetics/JamRoll system ran on AWS (Amplify, ECS, RDS for MySQL) and is connected to Google Cloud over a private link using Workload Identity Federation and AssumeRole; the stated plan is to move it to Cloud Run and Cloud SQL and from MySQL to PostgreSQL ([Speaker Deck, 2026-01-31](https://speakerdeck.com/kworkdev/ma-post-merger-integration); [Zenn, 2025-10-07](https://zenn.dev/knowledgework/articles/303f715965d79d)).
- **AI:** Gemini, GPT and Claude selectable per agent, run in Japanese regions by default and in global regions if the customer permits; SDKs called directly from Go, with `adk-go` used for workflows ([Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)); Model Context Protocol for external tool access ([2026-05-20](https://prtimes.jp/main/html/rd/p/000000127.000063428.html)); Google ADK for an internal SRE agent ([Zenn, 2026-09-28](https://zenn.dev/knowledgework/articles/ba94d985d1e341)). The industry LLM effort is stated to start from open-weight models ([2026-08-06](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)).
- **Tooling:** Terraform ([Zenn, 2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905)), GitHub Actions ([Zenn, 2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c)), Datadog ([Zenn, 2025-10-16](https://zenn.dev/knowledgework/articles/8ecf01f0ee0aea)), Sentry ([Zenn, 2025-03-28](https://zenn.dev/knowledgework/articles/39cf7c7e6f80f2)); custom ESLint plugins and a Terraform provider are published on GitHub (below).
- **Hiring-only mention:** the SRE posting lists infrastructure operation on GCP, AWS or Azure as preferred ([HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)); Azure use is not otherwise confirmed.

### Systems

| System | What it does | Source |
|---|---|---|
| Multi-product platform | Gateway and authentication layers; a common platform (directory, middleware) shared by product backends (content, CRM/SFA, skills, portal, process, learning, recording, coaching, external share, creation, know-how); content processing; search; activity events and audit; notifications; SCIM provisioning from Azure AD and others | [Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework) |
| AI Backend | Agent execution isolated as a subsystem; agent definitions in protobuf as single (LLM + tools), proxy (external agents such as Agentforce or Dify) or workflow types; tools defined by protobuf annotations, listed dynamically from product servers, and exposed externally as MCP tools under OAuth2 scopes. The deck states AI商談記録 and AI営業ロープレ run outside this backend | [Speaker Deck, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework) |
| Sales AI Agent OS | Ontology, strategy, agent and interface layers (see `Product`); the CTO describes modelling sales activities and their state changes rather than starting from tabular data | [2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html), [CTO/CAIO interview](https://knowledgework.com/why-enablement/4) |
| AI meeting recording | Records web meetings, IP phone, in-person meetings via mobile apps, PC browser and a Windows desktop app that detects Teams and Zoom meetings; transcription with speaker separation, summaries and tasks, automatic CRM/SFA entry including Salesforce custom objects; carrier-call integration | [2025-05-15](https://prtimes.jp/main/html/rd/p/000000076.000063428.html), [2026-06-05](https://prtimes.jp/main/html/rd/p/000000131.000063428.html), [2026-04-27](https://prtimes.jp/main/html/rd/p/000000125.000063428.html) |
| AI role-play | Role-play training with AI avatars; the AI Backend deck states it involves real-time voice processing on separate infrastructure | [2025-11-28](https://prtimes.jp/main/html/rd/p/000000098.000063428.html), [Speaker Deck](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework) |
| Knowledge sharing (社内共有) | Original module: sales-collateral and know-how sharing with RAG-based AI chat, search suggestions, category recommendation and automatic summaries | [2025-02-18](https://prtimes.jp/main/html/rd/p/000000063.000063428.html) |
| MCP server | Exposes 社内共有 and AI商談記録 data to external AI agents and chats | [2026-05-20](https://prtimes.jp/main/html/rd/p/000000127.000063428.html) |
| Data platform | Cloud SQL (PostgreSQL), Google Analytics and Cloud Logging into BigQuery; dbt layers; analysis-report output for customers | [Zenn, 2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905) |
| Speech R&D | Published work on speaker diarization fine-tuning, overlapped-speech detection and ASR data augmentation for Japanese (including Poetics-era work) | [R&D page](https://knowledgework.com/rd) |

**Public technical output (accessed 2026-10-11).** A Zenn publication with 197 articles dated 2021-09-27 to 2026-10-09 ([zenn.dev/p/knowledgework](https://zenn.dev/p/knowledgework)); "Knowledge Work Developers Blog" on note with 62 posts including the 「KNOWLEDGE WORK Dev Talk」 interview series ([note](https://note.com/knowledgework)); 41 decks on [Speaker Deck](https://speakerdeck.com/kworkdev); a [Qiita organization](https://qiita.com/organizations/knowledgework); and the 「Encraft」 study-group series on [connpass](https://knowledgework.connpass.com/). The GitHub organization [`knowledge-work`](https://github.com/knowledge-work) (created 2020-04-01) has 15 public repositories, 3 of them forks; the most-starred is `eslint-plugin-strict-dependencies` (242 stars), and recent originals include `go-vow` (a Go linter, created 2026-09-17), `command-action` and a Slack Terraform provider ([GitHub API](https://api.github.com/orgs/knowledge-work/repos)). The company sponsored Go Conference 2025 ([Zenn](https://zenn.dev/knowledgework/articles/968b90fca94b0b)) and the Acoustical Society of Japan's autumn 2026 meeting ([Zenn](https://zenn.dev/knowledgework/articles/c9e60d8a4a9cfe)).

### Technical background sought

Mid-career engineering postings open on 2026-10-11 were SRE (expert), corporate security (expert) and an engineering casual-interview form; the HERP board did not list a separate FDE posting ([HERP board](https://herp.careers/v1/kwork)).

- **SRE (expert)** — required: web application development; web security knowledge and experience; automation of log analysis and monitoring; proposing and discussing specifications and implementing and testing them; discussing the product with other roles. Preferred: infrastructure operation on GCP, AWS or Azure; defining SLI/SLOs and improving performance from data; CI/CD and developer-efficiency work; team development with design and code review; English sufficient to read technical documents ([HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE); updated 2026-09-28).
- **Corporate security (expert)** — required: leading ISMS certification or operation; SaaS-centred infrastructure security (network, server, IAM, encryption, MDM, EDR); basic Google Cloud/AWS knowledge. Preferred: compliance with FISC or NIST SP 800; OWASP or CIS frameworks; CISSP/CISM/CEH; SAST, DAST, SIEM, CASB ([HERP](https://herp.careers/v1/kwork/QVNkg0p34ILT)).
- **New-graduate engineer (2027, 2028 intakes)** — required: programming experience in any language and JLPT N1 or equivalent; preferred: computer-science knowledge ([HERP](https://herp.careers/v1/kwork/ZxZYCOkWex9k)).

### Industry domain

Enterprise B2B sales: sales enablement, sales collateral and know-how, meeting records, CRM/SFA (Salesforce Sales Cloud and Agentforce are named integrations), and agency/partner sales. Customers named in releases are concentrated in finance (banks, trust banks, insurers), telecoms and large manufacturers, and the industry-LLM plan lists telecom, IT, banking, insurance, securities, manufacturing, infrastructure, retail and services ([2026-08-06](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)). The FDE group pairs engineers with "エージェントストラテジスト" who design per-customer agent work ([note, 2026-08-28](https://note.com/knowledgework/n/n5c7dd150abd1)). No engineering posting reviewed lists sales or industry knowledge as required or preferred; the corporate-security posting lists FISC (Japanese financial-industry security guidelines) as preferred.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | No stated policy. Engineering postings are in Japanese; the new-graduate engineer and intern postings require JLPT N1 or equivalent business communication; the SRE posting lists English for reading technical documents as preferred. No English-language engineering posting was found | [new-grad](https://herp.careers/v1/kwork/ZxZYCOkWex9k), [intern](https://herp.careers/v1/kwork/UM-xWCFZCVDN), [SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE) |
| Location | Azabudai Hills Mori JP Tower 51F, Minato-ku, Tokyo | [HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE) |
| Office policy | Mid-career postings: hybrid, with business and corporate roles in the office about 3 days a week and product-development roles about 1 day a week; full remote permitted in some cases depending on circumstances or residence. New-graduate posting: remote-based with one company-wide office day a week | [SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE), [new-grad](https://herp.careers/v1/kwork/ZxZYCOkWex9k) |
| Remote-resident staff | 20 of 205 employees (9.8%) listed as 遠方地勤務者 (as of 2026-02) | [recruiting page](https://knowledgework.com/recruit/engineering) |
| Hours | Flextime, standard 8 hours a day, core time 11:00–15:00; all-hands meetings are held within core time | [HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE), [recruiting page](https://knowledgework.com/recruit/engineering) |
| Salary | SRE (expert): theoretical annual ¥9.1M–¥23.1M, base ¥650,000–¥1,650,000 a month, including fixed overtime pay for 45 hours. Corporate security (expert): ¥9.1M–¥16.1M. Casual-interview forms: ¥300,000–¥1,650,000 a month, stated as uniform across postings. Bonuses twice a year (February, August) | [SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE), [security](https://herp.careers/v1/kwork/QVNkg0p34ILT), [open position](https://herp.careers/v1/kwork/_lVOwBGi9TCb) |
| Leave and probation | Weekends and public holidays off; paid leave granted each April 1 (11–20 days from the second year); maternity, childcare and nursing-care leave available regardless of tenure; 100% of male employees took childcare leave (as of 2026-02); 3-month probation | [open position](https://herp.careers/v1/kwork/_lVOwBGi9TCb), [recruiting page](https://knowledgework.com/recruit/engineering) |
| Benefits | Commuting allowance up to ¥40,000 a month; "ABC Benefits" including work-time choice (hours and frequency), life-event support, learning support (books, study sessions), certification-exam fees, volunteer leave and medical checkups for 40+ | [HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE), [recruiting page](https://knowledgework.com/recruit/engineering), [2022-10-19](https://prtimes.jp/main/html/rd/p/000000013.000063428.html) |
| Evaluation | Employees declare the grade they seek each quarter and agree it with their manager; work time reviewed quarterly | [recruiting page](https://knowledgework.com/recruit/engineering) |
| New graduates and interns | 2027 and 2028 new-graduate engineer intakes; selection by web coding test, technical interview, "style" interview, presentation and an in-person CTO interview. One-month paid internship (¥2,000/hour, online, about 5 people, backend or frontend) | [new-grad](https://herp.careers/v1/kwork/ZxZYCOkWex9k), [intern](https://herp.careers/v1/kwork/UM-xWCFZCVDN) |
| Visa | Not stated in any posting reviewed | [HERP board](https://herp.careers/v1/kwork) |

---

## Notes

### Not publicly disclosed

Search scope (2026-10-11): knowledgework.com and knowledgework.cloud sitemaps, company page, leaders, R&D, security, recruiting and news pages; the PR TIMES company feed (121 releases, 2020-08-19 to 2026-10-01); HERP boards `kwork` (careers and v1); TokyoDev and Japan Dev company directories; Findy, Green and Wantedly profile URLs; GitHub organization API (`knowledge-work`, `kwork`, `knowledgework`); Zenn, note, Qiita, Speaker Deck and connpass; 国税庁 法人番号公表サイト; ISMS registry; INITIAL; web searches for ナレッジワーク, 株式会社ナレッジワーク, Knowledge Work, kwork and Poetics in Japanese and English.

- **Revenue and profit.** Not published by the company. A secondary article reports a net loss of ¥2,217,038 thousand and total assets of ¥4,123,317 thousand for the fiscal year ended June 2025, without citing the underlying 決算公告 ([coki.jp, 2026-03-30](https://coki.jp/article/column/73539/)); the original notice was not located in the reviewed sources.
- **Customer count and ARR.** No aggregate number found. The service site's sitemap lists 19 case-study pages under `/users/` ([case studies](https://knowledgework.cloud/users); accessed 2026-10-11).
- **Price list.** Only AI商談記録's list price appears, in a release; no other product price was found.
- **Post-Series C cumulative funding and valuation.** Not stated by the company. Adding the 35億円 Series C 1st close to the company's post-Series B cumulative 61.2億円 gives 96.2億円 (researcher arithmetic, not a company figure).
- **Engineering headcount.** Not published as a number beyond "開発人員100人規模" (2025-02-18) and "約半数がプロダクト開発に関与" (2026-02).
- **English-language hiring and visa sponsorship.** No Knowledge Work profile was found in the TokyoDev or Japan Dev company directories; no English-language posting or visa statement was found on HERP. The Findy and Green URLs returned not-found and the Wantedly URL redirected to the site top page.
- **Status page, SLA and public API reference.** None found; `status.knowledgework.cloud` and `help.knowledgework.cloud` did not resolve.
- **Full board composition.** The company page lists only the representative director; board membership is known only from appointment releases.
- **Turnover.** Not published.
- **J-Startup.** No selection of Knowledge Work found; the company describes Poetics as J-Startup certified ([2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html)).

### Inconsistencies across sources

- **Founding date:** releases give 設立日 2020-03-18 and 創業日 2020-04-01 ([2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)); the [Ricoh Japan joint release](https://prtimes.jp/main/html/rd/p/000000149.000063428.html) and [Canon MJ](https://prtimes.jp/main/html/rd/p/000001442.000013943.html) label 2020-04-01 as 設立; the registry shows the corporate number designated 2020-03-23.
- **Poetics acquisition date:** "2025年5月1日に…全株式を取得" in the [acquisition release](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) versus "2025年4月30日に株式取得" in the CEO's comment in the [merger release](https://prtimes.jp/main/html/rd/p/000000088.000063428.html).
- **Canon MJ MIRAI Fund:** listed by Knowledge Work under 「シリーズB以降の新規投資家」 ([2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)), while [Canon MJ](https://prtimes.jp/main/html/rd/p/000001442.000013943.html) and [Global Brain](https://prtimes.jp/main/html/rd/p/000000609.000047342.html) call the August 2026 investment 「追加出資」. No release announcing an earlier Canon MJ investment was found.
- **Cumulative funding and valuation (third-party):** HERP shows 累計調達額57億円 and 評価額146.9億円 ([HERP](https://herp.careers/careers/companies/kwork/jobs); Undated; accessed 2026-10-11), below the company's own 61.2億円 as of 2023-11. INITIAL shows a post-money valuation including latent shares of 22,403百万円 as of 2026-07-29 ([INITIAL](https://initial.inc/companies/A-38065)). Neither valuation is stated by the company.
- **Headcount:** 205 (2026-02, recruiting page), 233 full-time (2026-07, HERP posting), 235 (HERP company header; Undated). The figures have different dates and scopes.
- **Remote policy:** mid-career postings state product-development roles come in about once a week ([SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)); the new-graduate posting describes remote work as the default with a weekly company-wide office day ([new-grad](https://herp.careers/v1/kwork/ZxZYCOkWex9k)); the internship offers optional Tuesday attendance ([intern](https://herp.careers/v1/kwork/UM-xWCFZCVDN)).
- **CTO profile in a posting:** in the 2028 new-graduate engineer posting, the "CTOプロフィール" field repeats the CEO's career text ([HERP](https://herp.careers/v1/kwork/ZxZYCOkWex9k); accessed 2026-10-11); other postings and the leaders page give the CTO's own history.
- **Corporate site:** HERP job pages list `kwork.studio`, which now redirects to knowledgework.com ([HERP](https://herp.careers/careers/companies/kwork/jobs/w4Ks8k8FyIrE)).

### Other

- The company's description of its offering has changed four times: 「セールスイネーブルメントクラウド」 (2022-04), 「セールスイネーブルメントAI」 (2025-02-18), 「セールスAXソリューション」 (2026-01-16) and 「セールスAIエージェント」 with three series (2026-08-04). Module names also changed, e.g. 「ナレッジ社内共有」 (2025) to 「ナレッジワーク社内共有」 (2026). The CEO describes the Series C as recognizing the company's shift 「SaaS企業からAIエージェント企業への進化」 ([2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)).
- Post-merger integration of Poetics is described in a talk: repositories merged into the monorepo with Git Subtree, GitHub organizations unified, trunk-based development and CUJ/SLO practices shared, and JamRoll's GraphQL API being moved to Connect RPC ([Speaker Deck, 2026-01-31](https://speakerdeck.com/kworkdev/ma-post-merger-integration)).
- The company runs sales-media activities alongside the product: the YouTube channel 「NEW SALES チャンネル」 ([2025-01-29](https://prtimes.jp/main/html/rd/p/000000061.000063428.html)), the invitation-only conference 「NEW SALES PREMIERE」 (since 2022) and 「Forbes JAPAN NEW SALES OF THE YEAR」 with Forbes JAPAN (annually since 2023). Announcements about them recur in the press feed each year.
- Many recent releases are single-customer adoption announcements for AI商談記録 and AI営業ロープレ, especially regional banks and insurers (2026-03 to 2026-07).

---

## Resources

**Official**

- [Corporate site (JA)](https://knowledgework.com/) · [Company information](https://knowledgework.com/company) · [Leaders](https://knowledgework.com/member) · [R&D](https://knowledgework.com/rd) · [Information security policy](https://knowledgework.com/security) · [News index](https://knowledgework.com/news/pr)
- [CTO/CAIO interview on the Agent OS (JA)](https://knowledgework.com/why-enablement/4)
- [Service site — セールスAIエージェント (JA)](https://knowledgework.cloud/) · [Sales AX Consulting](https://knowledgework.cloud/consulting) · [Sales AI Products](https://knowledgework.cloud/products) · [Sales AI Agent OS](https://knowledgework.cloud/agentos) · [Case studies](https://knowledgework.cloud/users)
- [Engineering recruiting page (JA)](https://knowledgework.com/recruit/engineering)
- [HERP job board](https://herp.careers/v1/kwork) — [SRE (expert)](https://herp.careers/v1/kwork/w4Ks8k8FyIrE), [corporate security (expert)](https://herp.careers/v1/kwork/QVNkg0p34ILT), [engineering open position](https://herp.careers/v1/kwork/_lVOwBGi9TCb), [2028 new-graduate engineer](https://herp.careers/v1/kwork/ZxZYCOkWex9k), [2028 engineer internship](https://herp.careers/v1/kwork/UM-xWCFZCVDN) · [HERP Career company listing](https://herp.careers/careers/companies/kwork/jobs) · [HERP Career SRE page](https://herp.careers/careers/companies/kwork/jobs/w4Ks8k8FyIrE)
- [Zenn publication (JA)](https://zenn.dev/p/knowledgework) — [frontend architecture retrospective, 2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe), [Jest to Vitest, 2023-12-26](https://zenn.dev/knowledgework/articles/jest-to-vitest), [Cloud Deploy for Cloud Run, 2024-02-26](https://zenn.dev/knowledgework/articles/cloud-deploy-for-cloud-run), [Go monorepo CI, 2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c), [Sentry custom spans, 2025-03-28](https://zenn.dev/knowledgework/articles/39cf7c7e6f80f2), [data platform, 2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905), [AWS×GCP private DNS, 2025-10-07](https://zenn.dev/knowledgework/articles/303f715965d79d), [Go Conference 2025 sponsorship, 2025-10-08](https://zenn.dev/knowledgework/articles/968b90fca94b0b), [async-processing monitoring, 2025-10-16](https://zenn.dev/knowledgework/articles/8ecf01f0ee0aea), [Go + Connect interceptors, 2026-03-06](https://zenn.dev/knowledgework/articles/6962837cd41940), [Cloud SQL replication lag, 2026-03-12](https://zenn.dev/knowledgework/articles/9956b686e28324), [Connect ES v2 migration, 2026-03-31](https://zenn.dev/knowledgework/articles/0d01d7aee48082), [SRE agent with Google ADK, 2026-09-28](https://zenn.dev/knowledgework/articles/ba94d985d1e341), [Acoustical Society of Japan sponsorship, 2026-09-29](https://zenn.dev/knowledgework/articles/c9e60d8a4a9cfe)
- [Knowledge Work Developers Blog on note (JA)](https://note.com/knowledgework) — [FDE Dev Talk, 2026-08-28](https://note.com/knowledgework/n/n5c7dd150abd1)
- [Speaker Deck — kworkdev](https://speakerdeck.com/kworkdev) — [Knowledge Work の AI Backend, 2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework), [M&A post-merger integration, 2026-01-31](https://speakerdeck.com/kworkdev/ma-post-merger-integration)
- [Qiita organization](https://qiita.com/organizations/knowledgework) · [connpass — Encraft](https://knowledgework.connpass.com/)
- [GitHub organization](https://github.com/knowledge-work) · [repositories via API](https://api.github.com/orgs/knowledge-work/repos)

**Press releases (PR TIMES, JA — newest first)**

- [PR TIMES company feed](https://prtimes.jp/main/html/searchrlp/company_id/63428)
- [NEW SALES channel passes 200,000 subscribers — 2026-10-01](https://prtimes.jp/main/html/rd/p/000000158.000063428.html)
- [Digital Enablement Park grand opening — 2026-09-04](https://prtimes.jp/main/html/rd/p/000000156.000063428.html)
- [VP Finance appointment — 2026-09-01](https://prtimes.jp/main/html/rd/p/000000155.000063428.html)
- [SMBC Group プラリタウン sales partnership — 2026-08-20](https://prtimes.jp/main/html/rd/p/000000154.000063428.html)
- [NTT Docomo Business strategic partnership — 2026-08-17](https://prtimes.jp/main/html/rd/p/000000152.000063428.html)
- [CRO appointment — 2026-08-10](https://prtimes.jp/main/html/rd/p/000000153.000063428.html)
- [油井 誠 joins — 2026-08-07](https://prtimes.jp/main/html/rd/p/000000151.000063428.html)
- [Industry-specific sales LLM R&D — 2026-08-06](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)
- [Sales AI Agent OS and Series C 1st close, 35億円 — 2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)
- [Ricoh Japan capital and business alliance — 2026-08-04](https://prtimes.jp/main/html/rd/p/000000149.000063428.html)
- [NEC adopts AI商談記録 — 2026-07-28](https://prtimes.jp/main/html/rd/p/000000140.000063428.html)
- [VP Security Management appointment — 2026-07-01](https://prtimes.jp/main/html/rd/p/000000138.000063428.html)
- [AI商談記録 desktop app — 2026-06-05](https://prtimes.jp/main/html/rd/p/000000131.000063428.html)
- [Agentforce package for financial-sector sales — 2026-05-27](https://prtimes.jp/main/html/rd/p/000000128.000063428.html)
- [MCP server and data operations — 2026-05-20](https://prtimes.jp/main/html/rd/p/000000127.000063428.html)
- [AI商談記録 with carrier calls — 2026-04-27](https://prtimes.jp/main/html/rd/p/000000125.000063428.html)
- [Executive advisor 樋口 泰行 — 2026-04-20](https://prtimes.jp/main/html/rd/p/000000124.000063428.html)
- [SOC 2 Type 1 report — 2026-04-02](https://prtimes.jp/main/html/rd/p/000000123.000063428.html)
- [Ricoh Japan AI商談記録, about 6,000 users — 2026-03-30](https://prtimes.jp/main/html/rd/p/000000122.000063428.html)
- [資料作成エージェント — 2026-03-13](https://prtimes.jp/main/html/rd/p/000000119.000063428.html)
- [Office move to Azabudai Hills — 2026-02-16](https://prtimes.jp/main/html/rd/p/000000116.000063428.html)
- [Customized AI agents — 2026-02-06](https://prtimes.jp/main/html/rd/p/000000114.000063428.html)
- [ナレッジワーク for パートナーセールス — 2026-02-04](https://prtimes.jp/main/html/rd/p/000000113.000063428.html)
- [ナレッジワーク X and Sales AX Solution — 2026-01-16](https://prtimes.jp/main/html/rd/p/000000110.000063428.html)
- [Salesforce custom-object support — 2026-01-14](https://prtimes.jp/main/html/rd/p/000000108.000063428.html)
- [Japan CxO Award to the CTO — 2025-12-17](https://prtimes.jp/main/html/rd/p/000000101.000063428.html)
- [AI営業ロープレ launch — 2025-11-28](https://prtimes.jp/main/html/rd/p/000000098.000063428.html)
- [PartnerProp partnership — 2025-10-31](https://prtimes.jp/main/html/rd/p/000000096.000063428.html)
- [AI商談記録 PC browser and Android recording — 2025-10-22](https://prtimes.jp/main/html/rd/p/000000097.000063428.html)
- [Kirin Beer adopts 社内共有 — 2025-09-26](https://prtimes.jp/main/html/rd/p/000000094.000063428.html)
- [New mission "LIFE WITH ENABLEMENT" — 2025-07-11](https://prtimes.jp/main/html/rd/p/000000089.000063428.html)
- [Merger of Poetics — 2025-07-01](https://prtimes.jp/main/html/rd/p/000000088.000063428.html)
- [AI商談記録 launch — 2025-05-15](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)
- [Acquisition of Poetics — 2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html)
- [Salesforce Japan Partner Award 2025 — 2025-04-10](https://prtimes.jp/main/html/rd/p/000000069.000063428.html)
- [古森 茂幹 as director and CSO — 2025-02-20](https://prtimes.jp/main/html/rd/p/000000065.000063428.html)
- [Sales Enablement AI — 2025-02-18](https://prtimes.jp/main/html/rd/p/000000063.000063428.html)
- [NEW SALES YouTube channel — 2025-01-29](https://prtimes.jp/main/html/rd/p/000000061.000063428.html)
- [JTB, 5,500 users — 2025-01-07](https://prtimes.jp/main/html/rd/p/000000059.000063428.html)
- [Learning enablement product — 2024-12-05](https://prtimes.jp/main/html/rd/p/000000056.000063428.html)
- [ISO 27701 — 2024-09-26](https://prtimes.jp/main/html/rd/p/000000048.000063428.html)
- [Mizuho Bank, about 5,000 users — 2024-04-22](https://prtimes.jp/main/html/rd/p/000000041.000063428.html)
- [Patent, viewer speed-up — 2024-03-06](https://prtimes.jp/main/html/rd/p/000000038.000063428.html)
- [Patent, hover preview — 2024-03-05](https://prtimes.jp/main/html/rd/p/000000039.000063428.html)
- [ISO 27017 — 2024-02-20](https://prtimes.jp/main/html/rd/p/000000037.000063428.html)
- [Series B, 45億円 — 2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)
- [Ricoh Japan, about 12,000 users — 2023-10-02](https://prtimes.jp/main/html/rd/p/000000032.000063428.html)
- [VPoE appointment — 2023-09-01](https://prtimes.jp/main/html/rd/p/000000028.000063428.html)
- [NTT Communications, 5,000-person scale — 2023-06-21](https://prtimes.jp/main/html/rd/p/000000023.000063428.html)
- [BOXIL SaaS AWARD 2023 — 2023-05-15](https://prtimes.jp/main/html/rd/p/000000017.000063428.html)
- [Patent, Knowledge AI Recommend — 2023-04-27](https://prtimes.jp/main/html/rd/p/000000021.000063428.html)
- [Knowledge AI Chat — 2023-04-26](https://prtimes.jp/main/html/rd/p/000000022.000063428.html)
- [AI Integration Lab — 2023-04-25](https://prtimes.jp/main/html/rd/p/000000020.000063428.html)
- [Engineer enablement business, tenntenn joins — 2022-12-16](https://prtimes.jp/main/html/rd/p/000000016.000063428.html)
- [Knowledge Work for Salesforce — 2022-10-24](https://prtimes.jp/main/html/rd/p/000000011.000063428.html)
- [Life Event Support — 2022-10-19](https://prtimes.jp/main/html/rd/p/000000013.000063428.html)
- [Good Design Award 2022 — 2022-10-07](https://prtimes.jp/main/html/rd/p/000000012.000063428.html)
- [Series A 2nd close — 2022-06-17](https://prtimes.jp/main/html/rd/p/000000006.000063428.html)
- [『NEW SALES』 book — 2022-06-08](https://prtimes.jp/main/html/rd/p/000000004.000063428.html)
- [General availability and Series A 1st close — 2022-04-20](https://prtimes.jp/main/html/rd/p/000000003.000063428.html)
- [Company-hosted copy of the Series C release](https://knowledgework.com/news/article/jQM8vm0U)

**Third-party coverage and profiles**

- [Canon MJ — additional investment, 2026-08-04 (JA)](https://prtimes.jp/main/html/rd/p/000001442.000013943.html) · [Global Brain, 2026-08-04 (JA)](https://prtimes.jp/main/html/rd/p/000000609.000047342.html) · [フォースタートアップス, 2026-08-04 (JA)](https://prtimes.jp/main/html/rd/p/000000469.000032589.html)
- [BRIDGE — Series C, 2026-08-06 (JA)](https://thebridge.jp/2026/08/knowledgework-raises-3-5-billion-yen-series-c-for-sales-ai-agent-os)
- [国税庁 法人番号公表サイト — 4010401151825 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) · [English record](https://www.houjin-bangou.nta.go.jp/en/henkorireki-johoto.html?selHouzinNo=4010401151825)
- [ISMS registry — IS 750583 (JA)](https://isms.jp/lst/ind/CR_IS_x0020_750583.html) · [CLOUD 791569 (JA)](https://isms.jp/isms-cls/lst/ind/CR_CLOUD_x0020_791569.html)
- [INITIAL / Speeda (JA)](https://initial.inc/companies/A-38065)
- [coki.jp — FY2025/6 figures, 2026-03-30 (JA)](https://coki.jp/article/column/73539/)
