# ACES

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

ACES (株式会社ACES / ACES, Inc.) is a Tokyo company founded on 2017-11-20 by six founders, three of whom came from the University of Tokyo's Matsuo Lab. It is headquartered in Yushima, Bunkyo-ku. It runs two businesses. The **DX Partner** business designs, builds and operates custom AI systems for large companies and government bodies, under project contracts combined with AI licence contracts. The **AI software** business sells **ACES Meet**, an AI meeting-minutes and sales-enablement SaaS that runs on an in-house speech recognition system. The company now describes its technology base as an "AI OS": reusable data, knowledge and agent modules used to build company-specific "expert AI". ACES is not listed. Its recruiting materials state that it is preparing for an IPO.

- Disclosed funding: a seed round of 数千万円 (tens of millions of yen) from Deep30 and IGPI ([2019-05-22](https://acesinc.co.jp/news/post-930)); about ¥320M (約3.2億円) from IGPI and Deep30 ([2020-12-03](https://acesinc.co.jp/news/post-782)); and a capital and business alliance with SOMPO Light Vortex, amount not disclosed ([2022-05-26](https://acesinc.co.jp/news/post-536)). Capital is ¥100M ([company profile](https://acesinc.co.jp/company-profile); Undated; accessed 2026-10-11). No later round was found.
- Headcount: 72 full-time employees ([recruiting site](https://recruit.acesinc.co.jp/workstyle); Undated; accessed 2026-10-11); "正社員70名 / 全体110名規模" (70 full-time, about 110 including contractors and interns) ([HR candidate deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)). An engineering blog post from 2026-03-19 gives about 150 members on the same basis; see Notes.
- The DX Partner business is stated to have grown "前年比190%" (190% of the previous year) ([HR deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)). Recent named projects include a corporate-sales AI application co-developed with Sumitomo Mitsui Banking Corporation ([2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html)) and unsafe-behavior detection with YKK AP ([2025-04-23](https://prtimes.jp/main/html/rd/p/000000099.000044470.html)).
- Engineering: Python and JavaScript/TypeScript are the stated main languages ([tech blog, 2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123)). ACES Meet runs Python/Django and Next.js on AWS, with Auth0 for authentication and Cerbos for authorization ([tech blog](https://tech.acesinc.co.jp/)). DX Partner postings list AWS or Azure. Every posting reviewed is in Japanese, and one requires business-level Japanese ([Algorithm Engineer/Manager posting](https://open.talentio.com/r/1/c/aces/pages/94487); Undated; accessed 2026-10-11).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | 株式会社ＡＣＥＳ (furigana エーシーズ) / ACES, Inc. | [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856), [company profile](https://acesinc.co.jp/company-profile) |
| Corporate number | 4010001187856, designated 2017-11-22 | [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856) |
| Founded | 2017-11-20 | [company profile](https://acesinc.co.jp/company-profile) |
| HQ | 〒113-0034 東京都文京区湯島二丁目31番14号 ルーシッドスクエア湯島3階. The register lists 東京都文京区湯島２丁目３１番１４号 (last updated 2024-01-12) | [company profile](https://acesinc.co.jp/company-profile), [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856) |
| Representative | 代表取締役 田村 浩一郎 (Koichiro Tamura) | [company profile](https://acesinc.co.jp/company-profile) |
| Capital | ¥100M (1億円) | [company profile](https://acesinc.co.jp/company-profile); [PR TIMES company box](https://prtimes.jp/main/html/rd/p/000000073.000044470.html); Undated; accessed 2026-10-11 |
| Fiscal year end | 30 September (gazette notices for FY2020 and FY2021) | [catr.jp compilation of 官報 notices](https://catr.jp/companies/cd880/160167) |
| Listing status | Unlisted ("未上場"). Postings and the recruiting site state "IPO準備中" (preparing for an IPO). ACES does not appear on the JPX new-listings page updated 2026-10-06 | [PR TIMES company box](https://prtimes.jp/main/html/rd/p/000000073.000044470.html), [recruiting site](https://recruit.acesinc.co.jp/workstyle), [JPX](https://www.jpx.co.jp/listing/stocks/new/index.html) |
| Business lines | DXパートナーサービス (DX Partner), AIソフトウェアサービス (AI software) | [company profile](https://acesinc.co.jp/company-profile) |
| Headcount | 72 full-time employees, split DX Partner 54.2%, AI software 20.8%, R&D 13.8%, corporate 11.1% (Undated; accessed 2026-10-11). 70 full-time / about 110 in total (2026-07-30) | [recruiting site](https://recruit.acesinc.co.jp/workstyle), [HR deck](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| Working language | Japanese. All postings are in Japanese; see Working conditions | [Talentio careers page](https://open.talentio.com/r/1/c/aces/homes/2662) |
| Investors (disclosed) | Deep30投資事業有限責任組合, 株式会社経営共創基盤 (IGPI), SOMPO Light Vortex株式会社 | [2019-05-22](https://acesinc.co.jp/news/post-930), [2020-12-03](https://acesinc.co.jp/news/post-782), [2022-05-26](https://acesinc.co.jp/news/post-536) |
| Total raised | No cumulative figure has been published; see Funding | — |
| Security certifications | ISO/IEC 27001, announced 2022-04-21 (base ISMS certificate IS 764116). ISO/IEC 27017 (JIP-ISMS517-1.0) for ACES Meet, certificate CLOUD 847927, registered 2026-07-28, valid to 2028-03-29, registrar BSI Group Japan | [2022-04-21](https://acesinc.co.jp/news/post-564), [2026-08-03](https://prtimes.jp/main/html/rd/p/000000120.000044470.html) |

**Registered address history** ([NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856)): 文京区小石川 at designation; 文京区本郷2丁目 from 2018-06-11; 文京区本郷4丁目 (本郷トーセイビル) from 2019-07-31; 文京区湯島2-31-14 (湯島ファーストジェネシスビル3階) from 2021-02-09; the building name was dropped from the registered address on 2024-01-04. The company announced office moves on [2019-09-04](https://acesinc.co.jp/news/post-908) and [2021-02-17](https://acesinc.co.jp/news/post-768).

**Programs and awards.** Programs: AWS Activate ([2018-07-01](https://acesinc.co.jp/news/post-952)), Microsoft for Startups ([2019-08-13](https://acesinc.co.jp/news/post-915)), NVIDIA Inception ([2020-02-05](https://acesinc.co.jp/news/post-875)) and SoftBank's ONE SHIP partner program ([2020-12-03](https://acesinc.co.jp/news/post-868)). The [company profile](https://acesinc.co.jp/company-profile) lists these awards: HONGO AI 2019 (HONGO AI AWARD and フジタ賞); Plug and Play Japan Fall Summit 2020 IoT Japan Session Award; the MLIT Kanto Regional Development Bureau's 令和3年度 新技術推進技術者表彰; 週刊東洋経済「すごいベンチャー100」(2020); top rating, with JFEE (as the company writes it), in an MLIT pilot for innovative construction technology for rebar-inspection AI (令和元年度); ILS TOP100 Startups (2022); and Forbes 30 Under 30 Asia 2022 for the CEO. ACES Meet won the minutes-AI category grand prix of the AIsmiley AI PRODUCTS AWARD ([2024-04-16](https://prtimes.jp/main/html/rd/p/000000083.000044470.html)).

### Market context as stated by the company

- In its recruiting deck, the company attributes the opportunity to Japan's shrinking population, which it says requires a shift from labor-intensive to capital- and knowledge-intensive work. It cites a McKinsey projection for the AI software and services market. It also states that about 90% of the important data inside companies is "非公開・非構造" (private and unstructured), which general-purpose LLMs cannot learn from or reference ([HR deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)).
- Job postings say AI projects in Japan have a 3% success rate ("日本のAI導入PJが成功率3%"), and that ACES keeps 87% of its projects going after the PoC stage ([Software Engineer posting](https://open.talentio.com/r/1/c/aces/pages/81333); Undated; accessed 2026-10-11). The company deck compares this with 43% for "一般的なAI/DX PJ" (typical AI/DX projects), without naming a source ([company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao); version modified 2026-07-02).

---

## Product

### Business lines

The [company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) (version modified 2026-07-02) describes two businesses built on one set of in-house AI modules:

| Business | What is sold | Contract form | Source |
|---|---|---|---|
| DX Partner (DXパートナー) | Consulting through custom development and operation for a specific client: AI strategy and AI CoE support; building an "AI OS" (AgentOps, Expertise/MLOps, DataOps); redesigning business processes around AI. Typical phases are 3–6 months of consulting, 3–6 months of PoC and custom AI development, and 6 months or more of operation or business alliance, about 1.5 years or more in total | プロジェクト実行契約＋AIライセンス契約 (project contract plus AI licence) | [DX Partner page](https://acesinc.co.jp/dxpartner), [company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) |
| AI software (AIソフトウェア) | Cross-industry SaaS; currently ACES Meet | AIライセンス契約 (AI licence) | [company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao), [ACES Meet](https://meet.acesinc.co.jp/) |

The DX Partner page lists packaged solutions: 自社専用生成AI導入 (in-house generative AI deployment), RAG精度改善 (RAG accuracy improvement; [2025-09-02](https://prtimes.jp/main/html/rd/p/000000104.000044470.html)), VoC活用 (customer-voice analysis, sold as "ACES Meeting Intelligence"; [2026-02-13](https://prtimes.jp/main/html/rd/p/000000112.000044470.html)) and 安全管理DX (safety-management DX; [2025-10-07](https://prtimes.jp/main/html/rd/p/000000108.000044470.html)). The page says most of its project experience is in finance and manufacturing ([DX Partner page](https://acesinc.co.jp/dxpartner); Undated; accessed 2026-10-11).

### AI OS module layers

As drawn in the [HR deck (2026-07-30)](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) and on the [technology page](https://acesinc.co.jp/technologies):

| Layer | Stated role | Modules named |
|---|---|---|
| Data Layer | Turns raw video, audio and business data into data an AI can read | Document formatting AI, paralinguistic analysis AI, multi-camera behavior tracking, mask-compatible face recognition, facial expression and gaze analysis, multi-speaker speech recognition, work-process analysis, damage detection |
| Knowledge Layer | Gives structured data meaning and turns it into knowledge or tuned models | Privacy masking, utterance classification, damage valuation, learning speech recognition, QA extraction, behavior analysis, RAG inference platform, learning speaker identification |
| Agent Layer | Breaks business procedures into units that AI can execute | AI authentication/authorization platform; agents for minutes, compliance audit, eyewear recommendation, sales proposals, dialogue navigation, safety support, and sales forecasting / purchasing optimization |

### ACES Meet

ACES Meet records online and in-person meetings, then transcribes, summarizes and analyzes them, and pushes the results to CRM and other systems ([product site](https://meet.acesinc.co.jp/); Undated; accessed 2026-10-11). The product site claims about 40% fewer transcript corrections than "LLM技術を応用した音声認識モデル" (speech recognition models built on LLM technology), without naming the comparison. An AI engineering manager writes that ACES Meet has used an in-house speech recognition system since around March 2022 ([tech blog, 2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000)).

| Date | Change | Source |
|---|---|---|
| 2021-11-24 | Beta launch as a sales-support AI tool for online sales meetings | [release](https://acesinc.co.jp/news/post-728) |
| 2022-03-17 | General availability, with speaker separation, facial-expression analysis and Salesforce integration | [release](https://acesinc.co.jp/news/post-701) |
| 2022-10-11 | Google Meet and Microsoft Teams integration | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000039.000044470.html) |
| 2023-03-22 | "AIまとめ" automatic summaries using ChatGPT | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000051.000044470.html) |
| 2023-04-06 | Sequential analysis and live transcription | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000054.000044470.html) |
| 2023-08-30 | Per-speaker audio analysis and minutes for in-person meetings | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000069.000044470.html) |
| 2025-03-14 | Integration with CAREERPLUS, a core system for staffing agencies (Brain Lab) | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000098.000044470.html) |
| 2025-07-04 | Dictionary function (beta): customers register terms, and the model is additionally trained for each company | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000101.000044470.html) |
| 2025-08-20 | ACES Meet API: meeting search, meeting info, transcripts, AI summaries and analysis. Standard integrations already existed for Salesforce, HubSpot and Slack | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000103.000044470.html) |
| 2025-10-22 | iOS app for in-person recording (Android planned); up to 3 hours per recording; audio is deleted from the device after 30 days and cannot be exported | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000107.000044470.html) |
| 2026-07-28 | ISO/IEC 27017 registration covering ACES Meet and its use of AWS and Auth0 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000120.000044470.html) |

The product site and its case-study pages name customers including Sales Marker, IDOM, Stech&Co., インゲージ, RAKUS and 日本レコードマネジメント ([product site](https://meet.acesinc.co.jp/); Undated; accessed 2026-10-11).

### Other products and their status

| Product | Announced | What it is | Current status |
|---|---|---|---|
| SHARON | [2019-05-22](https://acesinc.co.jp/news/post-930) | Embeddable image-recognition algorithm package focused on human sensing | Not mentioned on the current corporate site |
| Deep Nine | [2020-06-01](https://acesinc.co.jp/news/post-854) | Pose-estimation app for baseball, built with Dentsu, GAORA and Kyodo News Digital | Not mentioned on the current corporate site |
| ACES ChatHub | [2023-06-02](https://prtimes.jp/main/html/rd/p/000000061.000044470.html) | Enterprise ChatGPT chatbot platform, moved onto Azure OpenAI Service ([2023-07-19](https://prtimes.jp/main/html/rd/p/000000065.000044470.html)), with in-house data reference added ([2023-10-17](https://prtimes.jp/main/html/rd/p/000000074.000044470.html)) | Not listed among current AI software products; no discontinuation notice found |
| AUX Checker | [2024-08-09](https://prtimes.jp/main/html/rd/p/000000089.000044470.html) | Vehicle damage-detection app built with SOMPOオークス; one-year business PoC with Ichinen from September 2024 | — |
| AUX Pricing | [2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html) | Accident-car pricing app built with オークスモビリティ for dealers | Price published: ¥120,000 per year |

### Commercialization

- No public price list exists for ACES Meet. Its [terms of service](https://meet.acesinc.co.jp/terms/) (制定 2021-10-20) say fees follow a price list posted on the site or defined separately, with a licence set on each user account. The product site directs visitors to a contact form.
- DX Partner work is sold as a project contract combined with an AI licence contract. The company says the algorithms and data developed are accumulated and modularized in-house, then supplied to customers as licences ([Algorithm Engineer/Manager posting](https://open.talentio.com/r/1/c/aces/pages/94487); Undated; accessed 2026-10-11).
- AUX Pricing is the only product found with a published price (¥120,000 per year; [2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html)).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2020-12-03 | Joint DX projects since founding in sports, retail, construction and automotive | [release](https://acesinc.co.jp/news/post-782) |
| "〜2024" (up to 2024) | 10–40 people; described as "コンサル中心の個人商店" (a consulting-centered one-shop operation) | [HR deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| Undated | DX Partner "前年度150%" (150% of the previous year) | [Software Architect posting](https://open.talentio.com/r/1/c/aces/pages/104805); accessed 2026-10-11 |
| Undated | DX Partner "前年比160%以上" (160%+ of the previous year), with demand led by large financial institutions | [FDE posting](https://open.talentio.com/r/1/c/aces/pages/123475); accessed 2026-10-11 |
| 2026-07-30 | DX Partner "前年比190%"; 70 full-time and about 110 in total | [HR deck](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| Undated | SMBC-GAI: document structuring and RAG improvement for SMBC's in-house generative AI, deployed to all employees; about 50,000 work-hours saved | [AI Engineer posting](https://open.talentio.com/r/1/c/aces/pages/22022), [company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) |

None of the growth figures states a base metric (revenue, orders or projects).

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2018-06-19](https://acesinc.co.jp/news/post-954) | エムスリー | Deep-learning algorithm development |
| [2020-08-27](https://acesinc.co.jp/news/post-816) | Zoff | Retail-DX business alliance; recommendation engine for Zoff Virtual Counter later supplied ([2021-11-25](https://acesinc.co.jp/news/post-720)) |
| [2020-09-09](https://acesinc.co.jp/news/post-806) | JFEE / MLIT | Rebar-inspection AI rated highest in an MLIT pilot; drone-based version completed [2023-02-15](https://prtimes.jp/main/html/rd/p/000000047.000044470.html) |
| [2020-09-29](https://acesinc.co.jp/news/post-803) | 陸上自衛隊 (JGSDF) | Agreement for ACES to advise on AI use |
| [2022-01-26](https://acesinc.co.jp/news/post-711) | バンダイナムコ研究所 | Joint R&D on AI character motion generation; motion dataset later sold |
| [2022-05-26](https://acesinc.co.jp/news/post-536) | SOMPO Light Vortex (SOMPO HD) | Capital and business alliance; AI for accident and used-car B2B auctions. ACES says it had worked with SOMPO Holdings since 2019 |
| [2022-09-14](https://prtimes.jp/main/html/rd/p/000000038.000044470.html) | 大同生命 | Sales analysis project using ACES Meet |
| [2022-12-22](https://prtimes.jp/main/html/rd/p/000000043.000044470.html) | 電源開発 (J-POWER) | Image-AI safety management system: counting workers at heights or openings, detecting ladder work, detecting approach to openings |
| [2023-10-13](https://prtimes.jp/main/html/rd/p/000000073.000044470.html) | 経済産業省 (METI) | Project on LLM use in public administration; ACES ChatHub trial on Azure |
| [2025-04-23](https://prtimes.jp/main/html/rd/p/000000099.000044470.html) | YKK AP | Trial of unsafe-behavior and PPE-non-use detection completed; company-wide rollout from FY2025 |
| [2026-02-20](https://prtimes.jp/main/html/rd/p/000000113.000044470.html) | 三井住友銀行 (SMBC) | ACES presented as SMBC's AI development partner at SMBC Group RisingX 2026 |
| [2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html) | 三井住友銀行 (SMBC) | Co-developed AI application for corporate-sales staff, now in use: suggests likely issues and products from meeting content and bank-specific product and sales knowledge |

The DX Partner page also cites participation in an AI "車座" (roundtable discussion) with then Prime Minister Ishiba ([DX Partner page](https://acesinc.co.jp/dxpartner); Undated; accessed 2026-10-11).

### Stated plans

- The recruiting site's strategy page says the company aims to move from being Japan's leading "AIとの協働を実現させるAIソリューション企業" (AI solutions company that makes collaboration with AI happen) to "次世代のビジネスプロセスを生み出す、AI事業投資会社" (an AI business-investment company that creates next-generation business processes) ([strategy page](https://recruit.acesinc.co.jp/strategy); Undated; accessed 2026-10-11).
- The IR/corporate-planning posting lists IPO preparation, M&A and PMI, expanding the AI module set, and 事業複線化 (adding business lines) as upcoming work ([IR posting](https://open.talentio.com/r/1/c/aces/pages/124609); Undated; accessed 2026-10-11).
- The company deck says ACES aims to be a "和製Palantir" (Japanese Palantir) that builds expert AI and its AI OS from combinable modules ([company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao); version modified 2026-07-02).
- The HR deck says that for the current fiscal year and the first half of the next, management will put organization-building ahead of sales growth ("売上成長 < 組織力強化") ([HR deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)).

---

## Founder

**田村 浩一郎 (Koichiro Tamura)**: co-founder and 代表取締役 CEO ([company profile](https://acesinc.co.jp/company-profile)).

- Born 1993 ([Green company interview](https://www.green-japan.com/company/9285/interview); Undated; accessed 2026-10-11).
- At the University of Tokyo Graduate School of Engineering (Matsuo Lab) he researched applications of deep learning to financial engineering. He earned a doctorate in engineering in three years while running the company ([company profile](https://acesinc.co.jp/company-profile)).
- In a 2023 interview he said ACES was incorporated in 2017 to pursue an idea, raised with a friend after the Transformer paper, for AI translation of Japanese manga with a publisher. When that project stalled, the team turned to DX work ([kigyolog interview, 2023-02-07](https://kigyolog.com/interview.php?id=207)).
- Selected for Forbes 30 Under 30 Asia 2022, Enterprise Technology ([2022-05-26](https://acesinc.co.jp/news/post-522)).

**Co-founders.** Postings say five of the six founders are engineers ([Software Engineer posting](https://open.talentio.com/r/1/c/aces/pages/81333)). Wantedly says three of the six came from the Matsuo Lab ([Wantedly](https://www.wantedly.com/companies/acesinc); Undated; accessed 2026-10-11). The names below are labelled Co-Founder in the [HR deck (2026-07-30)](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731), apart from 三田村, who is named in a blog post.

| Name | Role as written | Stated background |
|---|---|---|
| 與島 仙太郎 | 取締役 COO, Co-Founder | University of Tokyo, Systems Innovation master's (2019); co-founded ACES during graduate school; project manager across joint research ([company profile](https://acesinc.co.jp/company-profile)) |
| 中川 大海 | 執行役員, Co-Founder | University of Tokyo, doctorate in engineering; WI 2019 Best Student Paper Award; leads business development |
| 久保 静真 | 執行役員, Co-Founder | University of Tokyo (Matsuo Lab) master's; manages algorithm development (including deep learning) and infrastructure design. Signed the first tech-blog post in 2021 as head of the development department ([2021-09-24](https://tech.acesinc.co.jp/entry/2021/09/24/104953)) |
| 西條 真史 | 執行役員, Co-Founder | Keio SFC; Rakuten (business development and marketing for the フリマアプリ ラクマ); heads the AI software business |
| 三田村 | Co-founder / software engineer | Self-description in a [2026-03-19 blog post](https://tech.acesinc.co.jp/entry/2026/03/19/083000); given name not stated there |

**Other leadership and governance** ([company profile](https://acesinc.co.jp/company-profile), [HR deck](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)):

- **小松原 龍介**: 取締役 CFO. Previously KPMG AZSA (audit) and IGPI (strategy, principal investment, M&A advisory, turnarounds).
- **川上 登福**: outside director. Partner and managing director at IGPI and a director of the Japan Deep Learning Association. He became an adviser at the 2019 seed round and a director at the 2020 round ([2020-12-03](https://acesinc.co.jp/news/post-782)).
- **新原 浩朗**: outside director from [2025-05-14](https://prtimes.jp/main/html/rd/p/000000100.000044470.html). Former METI Director-General of the Economic and Industrial Policy Bureau and Cabinet Secretariat Councillor; retired from government on 2024-09-30.
- **Technical advisors**: 松尾 豊 (University of Tokyo; adviser from the [2019 seed round](https://acesinc.co.jp/news/post-930)) and 染谷 隆夫 (University of Tokyo; [2023-04-27](https://prtimes.jp/main/html/rd/p/000000058.000044470.html)). 沢田 渉 (IGPI senior executive fellow, formerly SMBC) became an adviser on [2023-10-04](https://prtimes.jp/main/html/rd/p/000000072.000044470.html).
- **Auditors**: a full-time auditor appointed 2021-08, whose biography states he helped prepare Ricksoft's 2019 TSE Mothers listing, plus outside auditors appointed 2022-06 and 2024-06.
- Other executive officers in the HR deck: 山本 豊 (head of delivery) and 佐久間 桂吾 (associate partner; previously NTT Data and AWS).

The HR deck's corporate org chart shows a four-person HR team and functions for corporate planning/IR, accounting and finance, general affairs and labor, legal, and IT/corporate engineering.

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2019-05-22 | シードラウンド (第三者割当増資) | 数千万円 (tens of millions of yen) | Deep30投資事業有限責任組合; 株式会社経営共創基盤 (IGPI) | — | [ACES](https://acesinc.co.jp/news/post-930), [BRIDGE](https://thebridge.jp/2019/05/sharon) |
| 2020-12-03 | 資金調達 (no round name; IGPI and Deep30 as subscribers) | 約3.2億円 (about ¥320M) | IGPI; Deep30 | not stated | [ACES](https://acesinc.co.jp/news/post-782) |
| 2022-05-26 | 資本業務提携 (capital and business alliance) | not disclosed | SOMPO Light Vortex株式会社 (wholly owned by SOMPO Holdings) | not stated | [ACES](https://acesinc.co.jp/news/post-536) |

- The 2019 round funded R&D for SHARON and hiring. The 2020 round was described as funding expansion of algorithm licensing and software ([2019-05-22](https://acesinc.co.jp/news/post-930), [2020-12-03](https://acesinc.co.jp/news/post-782)).
- IGPI subscribed in both the 2019 and 2020 rounds. IGPI partner 川上 登福 is an outside director, and CFO 小松原 龍介 previously worked at IGPI. No shareholding percentages have been published.
- No financing announcement after 2022-05-26 was found on the company news index or on [PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/44470).

**Financial statements.** The company does not publish revenue. A database compilation of 官報 (official gazette) 決算公告 shows two years ([catr.jp](https://catr.jp/companies/cd880/160167)); the gazette issues themselves were not reviewed:

| Fiscal year ended | Net income | Retained earnings | Total assets |
|---|---|---|---|
| 2020-09-30 | ¥7.629M | ¥21.486M | ¥151.214M |
| 2021-09-30 | ¥36.542M | ¥37.860M | ¥461.989M |

---

## Engineering

### Technology stack and platforms

**Confirmed by the company's technical writing** ([tech blog](https://tech.acesinc.co.jp/)):

- **Languages:** Python and JavaScript/TypeScript, stated as the main development languages ([2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123)).
- **ACES Meet backend:** Python/Django ([2025-02-28](https://tech.acesinc.co.jp/entry/2025/02/28/080000)).
- **ACES Meet frontend:** Next.js, React and TypeScript. Next.js was upgraded to v15 and moved to the App Router in January 2025 ([2025-01-31](https://tech.acesinc.co.jp/entry/2025/01/31/083000)).
- **AWS:** ALB, Fargate/ECS, SQS, SageMaker, AWS Batch and RDS appear as monitored services for ACES Meet in 2022 ([2022-04-12](https://tech.acesinc.co.jp/entry/2022/04/12/122321)). GPU inference runs on GPU instances launched through AWS Batch, with model weights packaged in Docker images pulled from ECR ([2025-02-07](https://tech.acesinc.co.jp/entry/2025/02/07/083000)). Meeting-list search uses Elasticsearch ([2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130)). Aurora Blue/Green deployment is listed as part of the deployment-safety work ([2025-01-10](https://tech.acesinc.co.jp/entry/2025/01/10/083000)). ACES uses a separate AWS account per customer or product, managed with AWS Organizations and connected through Transit Gateway to a shared-services account ([2021-10-18](https://tech.acesinc.co.jp/entry/2021/10/18/144813), [2022-04-12](https://tech.acesinc.co.jp/entry/2022/04/12/122321)).
- **Observability:** Grafana with CloudWatch across AWS accounts (2022); Sentry, including trace-based N+1 query detection ([2026-03-18](https://tech.acesinc.co.jp/entry/2026/03/18/083000)).
- **Identity:** Auth0 for authentication, with its configuration managed in Terraform ([2025-06-13](https://tech.acesinc.co.jp/entry/2025/06/13/083000)). Cerbos replaced in-application permission checks in a new authorization platform released in mid-August 2026; the selection table describes it as needing only a sidecar added to the existing ECS setup ([2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130)).
- **CI and supply chain:** GitHub Actions (matrix-parallel tests), Dependabot and Renovate, with Actions pinned to commit SHAs ([2024-12-13](https://tech.acesinc.co.jp/entry/2024/12/13/083000), [2025-01-31](https://tech.acesinc.co.jp/entry/2025/01/31/083000), [2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123)).
- **Azure:** ACES ChatHub and the METI LLM environment were built on Microsoft Azure with Azure OpenAI Service ([2023-07-19](https://prtimes.jp/main/html/rd/p/000000065.000044470.html), [2023-10-13](https://prtimes.jp/main/html/rd/p/000000073.000044470.html)).
- **ML:** an internal package, `aces-vision`, implements dozens of image and video deep-learning models behind one interface, with training "like PyTorch Lightning". An internal API platform called "ACES Platform" sits beneath the products ([2021-09-24](https://tech.acesinc.co.jp/entry/2021/09/24/104953)). The ChatGPT API powers ACES Meet's summary function ([2023-04-28](https://tech.acesinc.co.jp/entry/2023/04/28/130729)).
- **Internal AI tools:** ChatGPT Enterprise, Claude Enterprise and Cursor Enterprise were made available to about 150 members, including business staff, interns and contractors ([2026-03-19](https://tech.acesinc.co.jp/entry/2026/03/19/083000)). The 2026 decks list Cursor, Claude/Claude Code and Codex, and the recruiting site lists GitHub Copilot and Dify.

**Listed in job postings (DX Partner), labelled by the company as the main tools, with selection made per project** ([Software Engineer](https://open.talentio.com/r/1/c/aces/pages/81333), [Software Architect](https://open.talentio.com/r/1/c/aces/pages/104805); Undated; accessed 2026-10-11): Python/TypeScript; Django, Flask, FastAPI, React; Linux; AWS/Azure; Docker, Terraform; GitHub; Notion; Slack, Zoom. AI engineer postings list Python and PyTorch ([AI Engineer](https://open.talentio.com/r/1/c/aces/pages/22022)). The software-engineering intern posting adds Next.js and lists PostgreSQL/MySQL/NoSQL and AWS/GCP as preferred experience ([intern posting](https://open.talentio.com/r/1/c/aces/pages/120817)).

**Public repositories.** The GitHub organization [`aces-inc`](https://github.com/aces-inc) (name "ACES", blog field acesinc.co.jp, created 2018-10-16) has 14 public repositories. Thirteen are forks, including ESPnet, Dify, Redash, RT-DETR, Style-Bert-VITS2 and ndkale (an SQS task worker). The only original repository, `mysql-utf8mb4`, was last pushed 2021-09-07 (GitHub API; accessed 2026-10-11).

### Systems

| System | What it does | Source |
|---|---|---|
| ACES Meet analysis pipeline | Recorded meeting audio and video is analyzed into transcripts, summaries and statistics; speech recognition is developed in-house, and inference runs on GPU instances launched through AWS Batch | [2025-02-07](https://tech.acesinc.co.jp/entry/2025/02/07/083000), [2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000) |
| ACES Meet integrations | Salesforce field auto-fill, HubSpot, Slack, CAREERPLUS; an API for meeting data | [2025-08-20](https://prtimes.jp/main/html/rd/p/000000103.000044470.html), [product site](https://meet.acesinc.co.jp/) |
| ACES Meet security controls | IP allow-lists, MFA, database encryption, no external connections to the server environment, external vulnerability testing; video data accessible only from programs | [security page](https://meet.acesinc.co.jp/security/); Undated; accessed 2026-10-11 |
| Multi-tenant authorization | Cerbos policy engine; authorization conditions from Cerbos's PlanResources API are turned into Elasticsearch queries for the meeting list; migration used dual writes and a parallel run against the old checks before cutover | [2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130) |
| Safety-management AI | Real-time detection of falls, trips, missing PPE, leaning out and approaching hazards from existing surveillance cameras, with alerts, a database and dashboards | [2025-10-07](https://prtimes.jp/main/html/rd/p/000000108.000044470.html), [YKK AP](https://prtimes.jp/main/html/rd/p/000000099.000044470.html) |
| Vehicle damage and pricing | Damage detection from photos taken from eight directions, feeding a price model trained on オークスモビリティ's sales data (about 50,000 accident cars a year) | [2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html) |
| Enterprise RAG and knowledge structuring | Converts documents with complex figures and layouts into AI-readable data; SMBC-GAI RAG improvement; SMBC corporate-sales application | [DX Partner page](https://acesinc.co.jp/dxpartner), [2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html) |
| Abstraction-based masking | Patented LLM-based technique that replaces confidential entities with abstracted descriptions (e.g. "大手金融機関", major financial institution) rather than blanking them | [project page](https://acesinc.co.jp/projects/6EUJ3NeF); Undated; accessed 2026-10-11 |

Granted patents announced by the company: non-verbal message analysis from video ([2021-11-24](https://acesinc.co.jp/news/post-733)); automatic summarization of online meetings with several speakers ([2023-03-09](https://prtimes.jp/main/html/rd/p/000000050.000044470.html)); action recognition using large models ([2024-02-13](https://prtimes.jp/main/html/rd/p/000000081.000044470.html)); speaker classification ([2024-07-23](https://prtimes.jp/main/html/rd/p/000000088.000044470.html)); multimodal key-scene extraction from dialogue video ([2024-12-13](https://prtimes.jp/main/html/rd/p/000000093.000044470.html)).

### Technical background sought

From the [Talentio careers page](https://open.talentio.com/r/1/c/aces/homes/2662) (21 open pages; Undated; accessed 2026-10-11):

- **Software Engineer / Software Architect / FDE (required):** end-to-end web application work from design through implementation and testing; building and running systems on AWS or Azure; code review and CI/CD; turning business requirements into solutions independently. AI/ML knowledge and Python experience are explicitly not required. **Preferred:** building systems that use AI/ML; designing or running business systems or large web applications; infrastructure automation with Terraform or Docker; tech lead or architecture experience; performance tuning and log design. The FDE role also covers pre-sales customer work and taking systems through to production and adoption ([FDE](https://open.talentio.com/r/1/c/aces/pages/123475)).
- **AI Engineer (required):** deep knowledge of machine learning, deep learning or mathematical statistics; having searched the literature and carried an undefined problem from hypothesis to implementation; a science or engineering master's or doctorate, or equivalent research ability. **Preferred:** implementing papers from scratch and packaging them as Python libraries; publications; Kaggle or competitive-programming results; edge computing or model speed-up ([AI Engineer](https://open.talentio.com/r/1/c/aces/pages/22022)).
- **Algorithm Engineer/Manager (required):** ML/DL development or research; customer-facing requirements-to-operation work on AI systems; managing an AI engineering team; business-level Japanese. **Preferred:** papers or patents, Kaggle, MLOps, project management ([posting](https://open.talentio.com/r/1/c/aces/pages/94487)).
- **Contract software engineer (required):** 3+ years of TypeScript and React, and 2+ years developing on AWS, Azure or customer on-premise environments ([posting](https://open.talentio.com/r/1/c/aces/pages/115624)).

### Industry domain

Named projects span banking (SMBC), insurance (SOMPO, Daido Life), manufacturing and energy site safety (YKK AP, J-POWER), automotive aftermarket auctions (オークスモビリティ), staffing (Brain Lab's CAREERPLUS) and government (METI, JGSDF). The DX Partner page says most of its experience is in finance and manufacturing. No engineering posting reviewed requires prior industry knowledge. The software postings state that AI experience is not required, and the IT Consultant posting says AI knowledge is not required ([IT Consultant](https://open.talentio.com/r/1/c/aces/pages/78619)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | All postings and the recruiting site are in Japanese. The Algorithm Engineer/Manager posting requires business-level Japanese, equivalent to JLPT N1 for non-native speakers. Green tags the Algorithm Engineer listing "多国籍な職場" (multinational workplace). No English-language posting was found | [posting](https://open.talentio.com/r/1/c/aces/pages/94487), [Green](https://www.green-japan.com/company/9285/job/188942) |
| Location | Head office, Yushima, Bunkyo-ku, Tokyo | [Software Engineer posting](https://open.talentio.com/r/1/c/aces/pages/81333) |
| Remote | Recruiting site: hybrid with two remote days a week; office hours and days are free. Postings: "リモート相談可能" (remote negotiable). Contract roles: remote or on-site depending on the project | [recruiting site](https://recruit.acesinc.co.jp/), [contract posting](https://open.talentio.com/r/1/c/aces/pages/115624) |
| Hours | Flextime with core hours 11:00–15:00 | [recruiting site](https://recruit.acesinc.co.jp/) |
| Employment types | Full-time (40h+/week; bonus twice a year based on output); short-hours full-time for working PhD students (30h+/week, 120h/month, same bonus, stock options and benefits as full-time); long-term interns (15h+/week) | [work-style page](https://recruit.acesinc.co.jp/workstyle), [PhD AI Engineer posting](https://open.talentio.com/r/1/c/aces/pages/117320) |
| Salary | Software Engineer ¥6.0M–¥10.0M (Talentio). On Green: FDE/Software Engineer ¥8.5M–¥14.0M, Algorithm Engineer ¥6.0M–¥9.0M, HR ¥5.0M–¥8.0M. Most other postings say "応相談" (negotiable). Pay is set per job type by reference to each hiring market | [Talentio](https://open.talentio.com/r/1/c/aces/pages/81333), [Green FDE](https://www.green-japan.com/company/9285/job/310473), [work-style page](https://recruit.acesinc.co.jp/workstyle) |
| Grades | Separate ladders for players (P1–P4; P2 assumed for interns and new graduates), specialists (S1–S4) and managers (M1–M4) | [work-style page](https://recruit.acesinc.co.jp/workstyle) |
| Leave and benefits | Weekends and holidays off; 13 days of paid leave granted on the joining date; side jobs allowed; book allowance; laptop and dual monitors; full commuting allowance; health checks | [recruiting site](https://recruit.acesinc.co.jp/), [Software Architect posting](https://open.talentio.com/r/1/c/aces/pages/104805) |
| Workforce figures | Average age 33; average overtime 23.5 h/month; 57.5% have households of their own; 10 people have taken childcare or maternity leave | [work-style page](https://recruit.acesinc.co.jp/workstyle); Undated; accessed 2026-10-11 |
| Hiring process | Document screening; first interview (skill fit, with an online personality test and possibly a work-sample test); second interview (values and culture); final interview with the CEO after a reference check; about 3–4 weeks in total | [recruiting site](https://recruit.acesinc.co.jp/), [HR deck](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| Students and juniors | Long-term internships for software and ML engineers; the PhD short-hours track can follow an internship | [ML intern posting](https://open.talentio.com/r/1/c/aces/pages/55105), [SWE intern posting](https://open.talentio.com/r/1/c/aces/pages/120817) |
| Visa sponsorship | Not stated in any posting reviewed | — |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11): the corporate site (sitemap, company profile, news index, projects, DX Partner and technology pages), the recruiting site, all 21 open pages on Talentio, the ACES Meet site (sitemap, security, terms), the tech blog (50 entries from its sitemap), the note magazine index, Speaker Deck (four decks), the PR TIMES company page, the NTA corporate-number register, the JPX new-listings page, the GitHub organization `aces-inc`, Green, Wantedly, TokyoDev and Japan Dev (no ACES profile on either), INITIAL (used as a lead only) and catr.jp. Searches covered ACES, 株式会社ACES, エーシーズ, ACES Meet, ACES ChatHub and SHARON, in Japanese and English.

- **Revenue.** Not published. Growth appears only as year-on-year ratios for the DX Partner business, without a base metric. The only financial figures found are FY2020 and FY2021 gazette notices compiled by catr.jp.
- **Round sizes and cumulative funding.** The 2019 seed amount is given only as 数千万円, the SOMPO Light Vortex investment amount is not disclosed, and no cumulative total or shareholding percentages have been published.
- **IPO timing and market.** The company says it is preparing for an IPO but gives no target date or market.
- **ACES Meet pricing.** No public price list.
- **Engineering headcount.** Not published. The only breakdown is by business share of 72 full-time staff (R&D 13.8%).
- **Visa sponsorship, English-language roles, turnover.** None found.
- **Open source.** The GitHub organization contains forks and one small original repository; see Technology stack.

### Inconsistencies across sources

- **Headcount:** "70" ([Talentio postings](https://open.talentio.com/r/1/c/aces/pages/81333), [Green](https://www.green-japan.com/company/9285); Undated); 72 full-time ([recruiting site](https://recruit.acesinc.co.jp/workstyle); Undated); 70 full-time / about 110 including contractors and interns ([HR deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731); the [company deck](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) also gives 110); about 150 members including interns and contractors ([tech blog, 2026-03-19](https://tech.acesinc.co.jp/entry/2026/03/19/083000)). The 110 and 150 figures use the same stated scope but differ by about 40.
- **DX Partner growth:** 150% ([Software Architect posting](https://open.talentio.com/r/1/c/aces/pages/104805)), 160%+ ([FDE posting](https://open.talentio.com/r/1/c/aces/pages/123475)) and 190% ([HR deck, 2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)), all "previous year" comparisons. The postings are undated, so it is not clear whether they describe different fiscal years.
- **Head-office location:** the [2026-02-13 release](https://prtimes.jp/main/html/rd/p/000000112.000044470.html) gives the head office as 東京都港区. Every other release, the [company profile](https://acesinc.co.jp/company-profile) and the [NTA register](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856) give 文京区湯島. [Green](https://www.green-japan.com/company/9285) still lists the building as "湯島ファーストジェネシスビル3階", which the register dropped on 2024-01-04; the company now uses "ルーシッドスクエア湯島3階".
- **ACES Meet general-availability date:** 2022-03-17 ([release](https://acesinc.co.jp/news/post-701)); "2022年4月" ([ITコンサルタント posting](https://open.talentio.com/r/1/c/aces/pages/78619)); "2022年3月ごろから" (from around March 2022) ([tech blog, 2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000)).
- **Round labels:** the company called its 2019 round a seed round and gave no name to the later financings. [INITIAL](https://initial.inc/companies/A-31174) (database) labels the company "シリーズB" as of 2022-05-30 and shows a post-money valuation that no primary source confirms.
- **Release dates:** the company news index sometimes shows a different date from PR TIMES for the same release. For example, the 染谷 隆夫 appointment appears as 2023-06-03 on the [news index](https://acesinc.co.jp/news) but as 2023-04-27 on [PR TIMES](https://prtimes.jp/main/html/rd/p/000000058.000044470.html). This page uses the PR TIMES date for PR TIMES links.
- **Average age:** 33 ([recruiting site](https://recruit.acesinc.co.jp/workstyle)) versus 34 ([Green](https://www.green-japan.com/company/9285)), both undated.

### Other

- The business mix has shifted over time. The company described itself as an image and video recognition and "Human Sensing" company in 2019–2022 releases ([2019-05-22](https://acesinc.co.jp/news/post-930), [2022-05-26](https://acesinc.co.jp/news/post-536)). Since 2025 its releases use the terms "expert AI" and "AI OS" ([2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html), [2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html)).
- The company's news index stops at 2026-03-03, and several later PR TIMES releases do not appear in it, including those of 2026-03-17, 2026-04-24 and 2026-08-03. Both the index and the [PR TIMES company page](https://prtimes.jp/main/html/searchrlp/company_id/44470) were checked.
- The news index contains a 2021-06-16 item titled "一部報道について" (regarding certain media reports). It links to a PDF on a company subdomain that no longer resolves, so its content was not reviewed.
- Research output connected to products includes a WI 2019 Best Student Paper Award (co-founder 中川), a CHI 2023 case study on AI-assisted personnel assessment, which received an Honorable Case Study award, and a motion dataset paper with Bandai Namco Research ([news index](https://acesinc.co.jp/news)).

---

## Resources

**Official**

- [Corporate site (JA)](https://acesinc.co.jp/) · [company profile and members](https://acesinc.co.jp/company-profile) · [vision and business](https://acesinc.co.jp/whoweare) · [technology / AI OS](https://acesinc.co.jp/technologies) · [DX Partner](https://acesinc.co.jp/dxpartner) · [projects](https://acesinc.co.jp/projects) · [masking patent](https://acesinc.co.jp/projects/6EUJ3NeF)
- [News index (JA)](https://acesinc.co.jp/news)
- [Recruiting site (JA)](https://recruit.acesinc.co.jp/) · [work style](https://recruit.acesinc.co.jp/workstyle) · [strategy](https://recruit.acesinc.co.jp/strategy)
- [Talentio careers page (JA)](https://open.talentio.com/r/1/c/aces/homes/2662): [Software Engineer](https://open.talentio.com/r/1/c/aces/pages/81333), [Software Architect](https://open.talentio.com/r/1/c/aces/pages/104805), [FDE](https://open.talentio.com/r/1/c/aces/pages/123475), [AI Engineer](https://open.talentio.com/r/1/c/aces/pages/22022), [Algorithm Engineer/Manager](https://open.talentio.com/r/1/c/aces/pages/94487), [IT Consultant](https://open.talentio.com/r/1/c/aces/pages/78619), [PhD AI Engineer](https://open.talentio.com/r/1/c/aces/pages/117320), [ML intern](https://open.talentio.com/r/1/c/aces/pages/55105), [SWE intern](https://open.talentio.com/r/1/c/aces/pages/120817), [contract SWE](https://open.talentio.com/r/1/c/aces/pages/115624), [IR / corporate planning](https://open.talentio.com/r/1/c/aces/pages/124609)
- [ACES Meet (JA)](https://meet.acesinc.co.jp/) · [security](https://meet.acesinc.co.jp/security/) · [terms](https://meet.acesinc.co.jp/terms/)
- [ACES Developer's Blog (JA)](https://tech.acesinc.co.jp/): [dev overview, 2021-09-24](https://tech.acesinc.co.jp/entry/2021/09/24/104953) · [Transit Gateway, 2021-10-18](https://tech.acesinc.co.jp/entry/2021/10/18/144813) · [Grafana + CloudWatch, 2022-04-12](https://tech.acesinc.co.jp/entry/2022/04/12/122321) · [ChatGPT API summaries, 2023-04-28](https://tech.acesinc.co.jp/entry/2023/04/28/130729) · [ACES Meet dev philosophy, 2024-12-13](https://tech.acesinc.co.jp/entry/2024/12/13/083000) · [tech lead mission, 2025-01-10](https://tech.acesinc.co.jp/entry/2025/01/10/083000) · [library updates / Next.js, 2025-01-31](https://tech.acesinc.co.jp/entry/2025/01/31/083000) · [GPU cost, 2025-02-07](https://tech.acesinc.co.jp/entry/2025/02/07/083000) · [Python/Django, 2025-02-28](https://tech.acesinc.co.jp/entry/2025/02/28/080000) · [Auth0, 2025-06-13](https://tech.acesinc.co.jp/entry/2025/06/13/083000) · [release safety, 2026-03-18](https://tech.acesinc.co.jp/entry/2026/03/18/083000) · [enterprise AI tools, 2026-03-19](https://tech.acesinc.co.jp/entry/2026/03/19/083000) · [supply-chain policy, 2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123) · [speech recognition, 2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000) · [Cerbos migration, 2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130)
- [ACES magazine on note (JA)](https://note.acesinc.co.jp/m/m31330dc74c51)
- [Speaker Deck (JA)](https://speakerdeck.com/aces): [company deck (published 2023-12-18, modified 2026-07-02)](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) · [HR candidate deck (2026-07-30)](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)
- [GitHub organization](https://github.com/aces-inc)

**Press releases (company site, JA; newest first)**

- [Forbes 30 Under 30 Asia 2022 — 2022-05-26](https://acesinc.co.jp/news/post-522)
- [SOMPO Light Vortex capital and business alliance — 2022-05-26](https://acesinc.co.jp/news/post-536)
- [ISMS (ISO/IEC 27001) — 2022-04-21](https://acesinc.co.jp/news/post-564)
- [ACES Meet general availability — 2022-03-17](https://acesinc.co.jp/news/post-701)
- [Bandai Namco Research joint R&D — 2022-01-26](https://acesinc.co.jp/news/post-711)
- [Zoff recommendation engine — 2021-11-25](https://acesinc.co.jp/news/post-720)
- [ACES Meet beta — 2021-11-24](https://acesinc.co.jp/news/post-728) · [non-verbal analysis patent — 2021-11-24](https://acesinc.co.jp/news/post-733)
- [Office expansion — 2021-02-17](https://acesinc.co.jp/news/post-768)
- [¥320M from IGPI and Deep30 — 2020-12-03](https://acesinc.co.jp/news/post-782) · [ONE SHIP — 2020-12-03](https://acesinc.co.jp/news/post-868)
- [JGSDF advisory agreement — 2020-09-29](https://acesinc.co.jp/news/post-803)
- [JFEE rebar-inspection AI — 2020-09-09](https://acesinc.co.jp/news/post-806)
- [Zoff alliance — 2020-08-27](https://acesinc.co.jp/news/post-816)
- [Deep Nine — 2020-06-01](https://acesinc.co.jp/news/post-854)
- [NVIDIA Inception — 2020-02-05](https://acesinc.co.jp/news/post-875)
- [Corporate identity refresh and office move — 2019-09-04](https://acesinc.co.jp/news/post-908)
- [Microsoft for Startups — 2019-08-13](https://acesinc.co.jp/news/post-915)
- [Seed round and SHARON — 2019-05-22](https://acesinc.co.jp/news/post-930)
- [AWS Activate — 2018-07-01](https://acesinc.co.jp/news/post-952)
- [M3 algorithm development — 2018-06-19](https://acesinc.co.jp/news/post-954)

**PR TIMES (JA; newest first)** — [company page](https://prtimes.jp/main/html/searchrlp/company_id/44470)

- [ISO/IEC 27017 for ACES Meet — 2026-08-03](https://prtimes.jp/main/html/rd/p/000000120.000044470.html)
- [SMBC corporate-sales AI application — 2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html)
- [SMBC Group RisingX 2026 — 2026-02-20](https://prtimes.jp/main/html/rd/p/000000113.000044470.html)
- [VoC analysis solution — 2026-02-13](https://prtimes.jp/main/html/rd/p/000000112.000044470.html)
- [ACES Meet iOS app — 2025-10-22](https://prtimes.jp/main/html/rd/p/000000107.000044470.html)
- [Safety-management DX solution — 2025-10-07](https://prtimes.jp/main/html/rd/p/000000108.000044470.html)
- [RAG accuracy improvement — 2025-09-02](https://prtimes.jp/main/html/rd/p/000000104.000044470.html)
- [ACES Meet API — 2025-08-20](https://prtimes.jp/main/html/rd/p/000000103.000044470.html)
- [ACES Meet dictionary function — 2025-07-04](https://prtimes.jp/main/html/rd/p/000000101.000044470.html)
- [新原 浩朗 joins as outside director — 2025-05-14](https://prtimes.jp/main/html/rd/p/000000100.000044470.html)
- [YKK AP safety project — 2025-04-23](https://prtimes.jp/main/html/rd/p/000000099.000044470.html)
- [CAREERPLUS integration — 2025-03-14](https://prtimes.jp/main/html/rd/p/000000098.000044470.html)
- [AUX Pricing — 2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html)
- [Key-scene extraction patent — 2024-12-13](https://prtimes.jp/main/html/rd/p/000000093.000044470.html)
- [AUX Checker PoB — 2024-08-09](https://prtimes.jp/main/html/rd/p/000000089.000044470.html)
- [Speaker classification patent — 2024-07-23](https://prtimes.jp/main/html/rd/p/000000088.000044470.html)
- [AIsmiley AI PRODUCTS AWARD — 2024-04-16](https://prtimes.jp/main/html/rd/p/000000083.000044470.html)
- [Action recognition patent — 2024-02-13](https://prtimes.jp/main/html/rd/p/000000081.000044470.html)
- [ACES ChatHub data reference — 2023-10-17](https://prtimes.jp/main/html/rd/p/000000074.000044470.html)
- [METI LLM project — 2023-10-13](https://prtimes.jp/main/html/rd/p/000000073.000044470.html)
- [沢田 渉 as adviser — 2023-10-04](https://prtimes.jp/main/html/rd/p/000000072.000044470.html)
- [In-person meeting analysis — 2023-08-30](https://prtimes.jp/main/html/rd/p/000000069.000044470.html)
- [ACES ChatHub on Azure OpenAI — 2023-07-19](https://prtimes.jp/main/html/rd/p/000000065.000044470.html)
- [ACES ChatHub launch — 2023-06-02](https://prtimes.jp/main/html/rd/p/000000061.000044470.html)
- [染谷 隆夫 as technical adviser — 2023-04-27](https://prtimes.jp/main/html/rd/p/000000058.000044470.html)
- [Live transcription — 2023-04-06](https://prtimes.jp/main/html/rd/p/000000054.000044470.html)
- [ChatGPT summaries — 2023-03-22](https://prtimes.jp/main/html/rd/p/000000051.000044470.html)
- [Multi-speaker summary patent — 2023-03-09](https://prtimes.jp/main/html/rd/p/000000050.000044470.html)
- [Drone rebar inspection — 2023-02-15](https://prtimes.jp/main/html/rd/p/000000047.000044470.html)
- [J-POWER safety project — 2022-12-22](https://prtimes.jp/main/html/rd/p/000000043.000044470.html)
- [Google Meet / Teams integration — 2022-10-11](https://prtimes.jp/main/html/rd/p/000000039.000044470.html)
- [Daido Life project — 2022-09-14](https://prtimes.jp/main/html/rd/p/000000038.000044470.html)

**Third-party coverage, registers and profiles**

- [国税庁 法人番号公表サイト — 4010001187856 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856)
- [JPX new listings page (JA)](https://www.jpx.co.jp/listing/stocks/new/index.html)
- [catr.jp — gazette financial notices (JA)](https://catr.jp/companies/cd880/160167)
- [BRIDGE — seed round, 2019-05-29 (JA)](https://thebridge.jp/2019/05/sharon)
- [kigyolog — CEO interview, 2023-02-07 (JA)](https://kigyolog.com/interview.php?id=207)
- [Green — company profile (JA)](https://www.green-japan.com/company/9285) · [interview (JA)](https://www.green-japan.com/company/9285/interview) · [FDE posting (JA)](https://www.green-japan.com/company/9285/job/310473) · [Algorithm Engineer posting (JA)](https://www.green-japan.com/company/9285/job/188942)
- [Wantedly — company page (JA)](https://www.wantedly.com/companies/acesinc)
- [INITIAL (JA; database, lead only)](https://initial.inc/companies/A-31174)
