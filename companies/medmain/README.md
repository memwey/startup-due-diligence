# Medmain

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Medmain (メドメイン株式会社 / Medmain Inc.) is a Fukuoka-based company incorporated on 2018-01-11, founded by Osamu Iizuka (飯塚 統) while he was a medical student at Kyushu University. It develops **PidPort**, a browser-based cloud system for storing, viewing, annotating and sharing digitised pathology slides (whole-slide images, WSIs), used for remote consultation, conferences and teaching, together with in-house pathology-image AI models; it also runs a slide-scanning service. The company's product pages state that in Japan the AI analysis function is planned for future provision (※日本国内において、AI解析に関する機能については将来的な提供を計画しています). Since 2026-04-30 Medmain has been a consolidated subsidiary of TechMatrix (テクマトリックス, TSE Prime 3762) through TechMatrix and its subsidiary PSP.

- **Control:** TechMatrix and PSP agreed to buy all shares not held by PSP or CEO Iizuka for about ¥2.3B (約23億円); afterwards TechMatrix holds 29.10% and PSP 42.95% of voting rights ([TechMatrix TDnet, 2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)). Completion on 2026-04-30 was announced by Medmain on [2026-05-01](https://medmain.com/news/63907/).
- **Funding before the acquisition:** cumulative equity funding of 25億円 after a 4.7億円 round led by One Capital ([2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)); the company's only named round is シリーズA2, 8.5億円 ([2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)).
- **Size:** revenue ¥248.82M and operating loss ¥277.16M for FY2024 (December year-end), and 15 employees, per the target-company table in [TechMatrix's 2026-02-17 disclosure](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf).
- **Regulatory:** ISO 13485:2016 (first registered 2025-01-27) and ISO/IEC 27001:2022 (2024-11-04) ([company page](https://medmain.com/aboutus/); accessed 2026-10-11). A 第一種医療機器製造販売業 licence was announced on [2024-08-02](https://prtimes.jp/main/html/rd/p/000000041.000034505.html), but the company page lists a 第二種 licence with a different number — see `Notes`. No PMDA approval or certification of a Medmain product was announced in the sources reviewed.
- **Engineering:** the product FAQ names AWS for storage and Auth0 for authentication ([PidPort page](https://service.medmain.com/service/pidport); accessed 2026-10-11). The current [Fullstack Engineer posting](https://open.talentio.com/r/1/c/medmain/pages/114519) lists Kotlin (Spring Boot), Python, React/TypeScript, MySQL, MongoDB, AWS and Terraform, requires Japanese communication, allows full remote work in or outside Japan, and states ¥8M–¥12M a year (Undated; accessed 2026-10-11).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Medmain; products PidPort, PidPort Personal, PidPort Digital Slide Creation Service | [service site](https://service.medmain.com/service/pidport); accessed 2026-10-11 |
| Legal name | メドメイン株式会社 (Medmain Inc.) | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259), [company page](https://medmain.com/aboutus/) |
| Corporate number | 2290001080259; number designated 2018-01-18 | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259); information as of 2026-10-11 |
| Founded | 2018-01-11 | [founding release, 2018-01-11](https://medmain.com/pressrelease/829/), [company page](https://medmain.com/aboutus/) |
| Registered head office | 福岡県福岡市中央区赤坂２丁目４番５号; moved 2019-05-21 from 福岡市中央区荒戸１丁目３番９号インスパイヤー大濠３０１号 | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259) |
| Offices | Fukuoka: 赤坂2-4-5 シャトレサクシーズ104. Tokyo: 港区南青山2-10-11 A青山ビル2F. US: 212 Homer Ave, Palo Alto, CA (Medmain USA Inc.) | [company page](https://medmain.com/aboutus/); accessed 2026-10-11 |
| Representative | 代表取締役 CEO 飯塚 統 (Osamu Iizuka) | [company page](https://medmain.com/aboutus/) |
| Parent | TechMatrix 29.10% and PSP 42.95% of voting rights; consolidated subsidiary of TechMatrix from 2026-04-30 | [TechMatrix TDnet, 2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf), [2026-05-01](https://medmain.com/news/63907/) |
| Capital | 11億9000万円 including capital reserve (company page); 資本金 1億円 (TechMatrix disclosure and Medmain's 2026-02-17 release) — see `Notes` | [company page](https://medmain.com/aboutus/), [TechMatrix TDnet](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |
| Shares issued; fiscal year | 151,183 shares; December year-end | [TechMatrix TDnet, 2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |
| Headcount | 15 (従業員数) | [TechMatrix TDnet, 2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |
| Working language | No company-wide policy published; see `Working conditions` for posting-level evidence | — |
| Customers | PidPort adopted at more than 60% of Japanese universities that have a university hospital (大学病院を有する大学の6割超) | [2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html) |
| Total raised | 25億円 cumulative equity funding | [2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html) |
| Licences and filings (company page) | 第二種医療機器製造販売業 13B2X10662; 高度管理医療機器等販売・貸与業 7港み生機器第59号; 電気通信事業届出 H-04-01768 | [company page](https://medmain.com/aboutus/); accessed 2026-10-11 |
| Licence (release) | 第一種医療機器製造販売業, 13B1X10433, issued by Tokyo Metropolitan Government 2024-07-02 | [2024-08-02](https://prtimes.jp/main/html/rd/p/000000041.000034505.html) |
| Certifications | ISO/IEC 27001:2022 and JIS Q 27001:2023, JP24/00000322, SGSジャパン, first registered 2024-11-04, scope 医療ソフトウェア・クラウドサービスの企画・開発・運営および販売. ISO 13485:2016, 50301629 MP2016, ドイツ品質システム認証, first registered 2025-01-27, scope "The design of software for pathology diagnostic support" | [company page](https://medmain.com/aboutus/), [ISMS release](https://prtimes.jp/main/html/rd/p/000000043.000034505.html), [ISO 13485 release](https://prtimes.jp/main/html/rd/p/000000045.000034505.html) |
| Patent | 特許第7752741号 「所見作成作業効率化システム」, registered 2025-10-02 | [2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html) |
| Main banks | 三菱UFJ銀行, 福岡銀行 | [TechMatrix TDnet, 2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Medmain | Brand; predates the company | Site opened 2015-12-28; student-era projects 九医クラウド (2016) and the pathology software "OMEGA" (2017) were published under it | Operated before incorporation; legal continuity with the 2018 company is not stated | [2015-12-28](https://medmain.com/news/35/), [2016-06-20](https://medmain.com/pressrelease/322/), [2017-05-24](https://medmain.com/pressrelease/324/) |
| メドメイン株式会社 | Legal entity | Japan, from 2018-01-11 | Operating company; "九州大学発のスタートアップ" | [NTA record](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259), [2018-01-11](https://medmain.com/pressrelease/748/) |
| Medmain USA Inc. | Related entity | Delaware, announced 2018-05-22 | "メドメインの米国法人"; Palo Alto address on the company page | [2018-05-22](https://medmain.com/pressrelease/1023/), [company page](https://medmain.com/aboutus/) |
| メドテリア株式会社 | Related entity | Japan, established 2024-08-01 | Took over the Medteria medical-student cloud business; Iizuka is a director; ownership not stated | [2024-08-01](https://medmain.com/news/52692/) |
| テクマトリックス株式会社 | Parent | TSE Prime 3762 | 29.10% of Medmain voting rights from 2026-04-30 | [TechMatrix TDnet, 2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf) |
| PSP株式会社 | Parent-group company | Tokyo; TechMatrix holds 50.02% | Shareholder since 2022; 42.95% of Medmain voting rights from 2026-04-30 | [TechMatrix TDnet, 2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf) |

**Programs and awards** (company announcements): 経済産業省 飛躍 Next Enterprise, Silicon Valley course ([2018-12-21](https://medmain.com/pressrelease/1441/)); NICT 起業家万博 総務大臣賞 ([2019-04-06](https://medmain.com/pressrelease/1504/)); J-Startup ([2019-06-26](https://medmain.com/pressrelease/1563/)); 第2回日本オープンイノベーション大賞 文部科学大臣賞, jointly with 九州大学起業部 ([2020-02-19](https://medmain.com/news/1692/)); NEDO 研究開発型スタートアップ支援事業, grant of up to ¥200M ([2022-06-27](https://prtimes.jp/main/html/rd/p/000000023.000034505.html)); AMED 令和5年度 医工連携イノベーション推進事業 for a gastric and colorectal biopsy AI system ([2023-09-07](https://prtimes.jp/main/html/rd/p/000000034.000034505.html)); U.S. Market Gateway Accelerator for BioSciences and MedTech ([2023-09-06](https://prtimes.jp/main/html/rd/p/000000035.000034505.html)); METI's Japan Innovation Campus in Palo Alto ([2023-11-22](https://prtimes.jp/main/html/rd/p/000000038.000034505.html)); Fukuoka City's High Growth Program ([2024-08-01](https://medmain.com/news/44031/)), 令和6年度 IPO等に向けた成長支援プログラム ([2024-08-08](https://medmain.com/news/44474/)) and 令和7年度 IPO Growth Program ([2025-09-03](https://medmain.com/news/57313/)); Forbes JAPAN "JAPAN's AI 50" ([2025-01-30](https://medmain.com/news/50262/)); 日経 NEXTユニコーン 2024 ([2025-01-31](https://medmain.com/news/50364/)) and 2025 ([2026-01-21](https://medmain.com/news/61450/)); Mizuho Innovation Award 2025.1Q ([2025-06-11](https://medmain.com/news/54666/)). The company joined AI医療機器協議会 in [2023-04](https://medmain.com/news/25661/) and Iizuka became one of its directors (理事) in [2025-06](https://medmain.com/news/54862/).

### Market context as stated by the company

- Pathologists in Japan: "日本全国に僅か2500名強（医師全体数の0.7〜0.8%ほど）" in the [recruiting note](https://medmain.notion.site/recruiting-note) (Undated; accessed 2026-10-11); "約2,800名" in the [2024-10-31 release](https://prtimes.jp/main/html/rd/p/000000042.000034505.html). The company describes many hospitals as relying on a single pathologist or outsourcing diagnosis.
- The [2026-02-17 release](https://prtimes.jp/main/html/rd/p/000000054.000034505.html) describes PSP as the domestic share leader in cloud PACS with a customer base of 2,600 facilities, and gives the shift of pathology-support AI into clinical use, continuity in medical-device approval work, and returning digital-pathology data to research as the reasons for joining the TechMatrix group.

---

## Product

Product pages live on [service.medmain.com](https://service.medmain.com/service/pidport); organisation users log in at `pidport.com` and individual users sign up at `entry.personal.pidport.com`.

### PidPort (organisations)

Described as a "デジタル病理支援クラウドシステム" with no scanner, server or software installation required ([PidPort page](https://service.medmain.com/service/pidport); accessed 2026-10-11). Functions listed on the page:

- in-house high-speed browser viewer; split view of up to four slides with synchronised navigation; Z-stack viewing; colour-tone presets saved per user or shared;
- comments and annotation drawing shared between users; screenshots; attachment of related documents (pdf, doc(x), xls(x), csv, ppt(x), zip);
- bulk WSI upload in tiff, jpeg, png, svs, ndpi, zip (vsi), isyntax and i2syntax;
- use cases presented as remote consultation between hospitals, online conferences, and teaching and joint research ([scene pages](https://service.medmain.com/scene)).

The FAQ states that EHR linkage is by pasting PidPort case URLs into the record, with system-level integration "under consideration", and that Chrome is the recommended browser ([FAQ](https://service.medmain.com/faq); accessed 2026-10-11).

**AI analysis status.** Every current product page reviewed carries the note that AI analysis in Japan is planned for future provision ([products](https://medmain.com/products/), [PidPort](https://service.medmain.com/service/pidport), [reason](https://service.medmain.com/reason); accessed 2026-10-11). The [2020-03-10 release](https://prtimes.jp/main/html/rd/p/000000009.000034505.html) stated that AI analysis, remote diagnosis and cloud storage were available outside Japan (with some functions unavailable in some regions), while in Japan only remote diagnosis, cloud storage and slide digitisation were offered. The PidPort page lists AI coverage of stomach, colon, lung, breast, pancreas (EUS-FNB adenocarcinoma), prostate and lymph-node metastasis histology, and cervical and urine cytology.

### Other products and services

| Product | What it is | Source |
|---|---|---|
| PidPort Personal | Self-service plans for individuals: Starter (free; upload, viewing, annotation, Z-stack) and Personal (¥3,980/month, 50 GB; image download and AI analysis "to be added"), with 100 GB and 250 GB tiers; previously PidPort was sold only under corporate contracts | [plan page](https://service.medmain.com/service/personal) (accessed 2026-10-11), [2026-07-01](https://medmain.com/news/65758/), [2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html) |
| PidPort Digital Slide Creation Service (Imaging Center) | Contract scanning of glass slides; started 2019-06; Leica Aperio AT2 and Hamamatsu NanoZoomer S360; bright-field ×20 or ×40 only; average about 1 GB per WSI; delivery to a PidPort folder, a download system or HDD | [2019-06-17](https://medmain.com/pressrelease/1552/), [FAQ](https://service.medmain.com/faq) |
| NOBORI for pathology | Cloud pathology PACS combining Medmain and PSP technology, from 2024-11-01: cloud storage, image-analysis AI, consultation and remote pathology diagnosis, with CT, MRI and endoscopy images managed together | [2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html) |
| Medteria | Cloud service for medical students launched 2018; spun off to メドテリア株式会社 on 2024-08-01 | [2018-06-11](https://prtimes.jp/main/html/rd/p/000000001.000034505.html), [2024-08-01](https://medmain.com/news/52692/) |

### Commercialization

Organisation pricing for PidPort is quoted individually ("個別にご案内") and the scanning service uses volume-based per-slide pricing on request ([FAQ](https://service.medmain.com/faq); accessed 2026-10-11). Only the individual plans publish prices ([plan page](https://service.medmain.com/service/personal)). A 特定商取引法 notice is linked from the product site footer.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2018-10-15 | PidPort α version to be run closed at partner institutions, separated from actual diagnosis | [release](https://prtimes.jp/main/html/rd/p/000000004.000034505.html) |
| 2020-08-24 | PidPort formally released 2020-02; joint research with 50+ medical institutions in Japan and abroad | [release](https://prtimes.jp/main/html/rd/p/000000010.000034505.html) |
| 2022-07-26 | AI developed for 7 organs, 12 models | [release](https://prtimes.jp/main/html/rd/p/000000024.000034505.html) |
| 2024-10-31 | Joint research or usage with 100+ medical institutions in Japan and abroad | [release](https://prtimes.jp/main/html/rd/p/000000042.000034505.html) |
| 2024-12-23 | PidPort adopted at more than half of the 82 Japanese universities with a medical faculty | [release](https://prtimes.jp/main/html/rd/p/000000044.000034505.html) |
| 2026-02-17 | Adopted at more than 60% of universities that have a university hospital; also used at overseas medical institutions | [release](https://prtimes.jp/main/html/rd/p/000000054.000034505.html) |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2022-07-26](https://prtimes.jp/main/html/rd/p/000000024.000034505.html) | PSP | Capital and business alliance; PSP to resell Medmain products and integrate them into its infrastructure |
| [2023-11-02](https://medmain.com/news/32208/) | 久留米大学医学部病理学講座 | PidPort for education and research |
| [2023-12-18](https://medmain.com/news/34196/) | JP-AID (日本病理学会) / University of Tokyo | Gastric-biopsy diagnosis-support AI developed under JP-AID to be developed by Medmain toward approval as a program medical device under the AMED project |
| [2025-05-21](https://medmain.com/news/53996/) | 鳥取大学医学部 | PidPort in anatomy and pathology histology practicals |
| [2025-07-25](https://prtimes.jp/main/html/rd/p/000000049.000034505.html) | Bạch Mai Hospital, E Hospital, Thái Nguyên A Hospital (Vietnam) | MOUs on digital pathology and medical AI |
| [2025-08-01](https://prtimes.jp/main/html/rd/p/000000050.000034505.html) | SMC (メディカルツーリズム・ジャパン事業部) | Partnership for research use of pathology AI in Vietnam |
| [2025-09-12](https://medmain.com/news/57578/) | Thống Nhất Hospital, Ho Chi Minh City | PidPort introduced in the pathology department |
| [2025-10-20](https://prtimes.jp/main/html/rd/p/000000052.000034505.html) | Ha Dong General Hospital, Hanoi | Research use and demonstration of PidPort |

Case studies on the product site name 国際医療福祉大学, 一般社団法人 PathPortどこでも病理ラボ, 東葛病院 and 東京医科大学病院 ([case list](https://service.medmain.com/case); accessed 2026-10-11).

### Stated plans

- Use of the 2025 funds: further development of the pathology AI and PidPort, investment in digitisation, sales, regulatory filing for the pathology AI (病理AIの薬事承認申請) and groundwork for overseas expansion ([2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)). The 2024 Series A2 release listed software development, digitisation equipment, sales and medical-device approval filing ([2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)).
- After joining the TechMatrix group: strengthen the organisation for obtaining medical-device approval of pathology-support AI and for ongoing regulatory and quality work; deepen integration with PSP's cloud PACS and remote-diagnosis platform; expand nationally through PSP's customer base and sales and support organisation ([2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)).
- Implement the findings-text patent in PidPort ([2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html)); add AI analysis to the individual plans ([2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html)).

---

## Founder

**飯塚 統 (Osamu Iizuka)** — founder, 代表取締役 CEO ([company page](https://medmain.com/aboutus/)).

- Wrote AI and web software while enrolled in Kyushu University's School of Medicine (九州大学医学部医学科在学中) and worked as a software engineer at a venture company ([company page](https://medmain.com/aboutus/)). In his recruiting-site message he describes a cell-tracking system built with machine learning in a university lab as the starting point for applying the work to pathology ([CEO message](https://recruit.medmain.com/message); Undated; accessed 2026-10-11).
- 2017-11-17: the pathology software "Omega" won the Live Sharks Tank pitch event in Silicon Valley ([2017-11-24](https://medmain.com/news/672/)).
- 2018-01-11: incorporated Medmain and became representative director ([2018-01-11](https://medmain.com/pressrelease/748/)). An interview states the company was set up by four Kyushu University students ([社長名鑑](https://shachomeikan.jp/industry_article/3551); information as of 2025-01).
- 2018-05: PidPort won the Latitude59 pitch contest in Estonia ([2018-05-30](https://medmain.com/news/1037/)).
- 2020-04-02: Forbes 30 Under 30 Asia, Healthcare & Science ([2020-04-02](https://medmain.com/news/1743/)).
- 2024-08-01: director of the spun-off メドテリア株式会社 ([2024-08-01](https://medmain.com/news/52692/)).
- 2025-06: director (理事) of AI医療機器協議会 ([2025-06-17](https://medmain.com/news/54862/)).
- Holding: 43,581 common shares, 28.83% of voting rights, as of 2026-01-31 ([TechMatrix TDnet, 2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)).

### Selected leadership

Board as listed on the [company page](https://medmain.com/aboutus/) (Undated; accessed 2026-10-11; names are given in English only):

| Name | Role | Stated background |
|---|---|---|
| Osamu Iizuka (飯塚 統) | CEO, director | See above |
| Masayuki Tsuneki (常木 雅之) | Director | Pathology researcher and university faculty; molecular pathology of carcinogenesis at a national university, Yale University and the National Cancer Center |
| Yoshihisa Yoda (依田 佳久) | Director | Nichimen (now Sojitz); TechMatrix director who founded its medical business; founded NOBORI (2018); PSP president since 2022. Also TechMatrix 取締役 専務執行役員 ([2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)) |
| Tomohiro Tanaka | Director | Nearly 20 years selling medical-image management systems at TechMatrix; sales lead for PACS after the 2022 PSP–NOBORI merger; now launching a pathology image cloud business |
| Masayuki Takahashi | Auditor | Trading-company overseas sales; TechMatrix listing; oversees administration of PSP and its group |

Tsuneki is the corresponding author of the company's AI papers and is affiliated with "Medmain Research, Medmain Inc." ([Ki-67 paper, 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12984776/fullTextXML)); the company announced his inclusion in the Stanford/Elsevier "World's Top 2% Scientists" list in clinical medicine ([2025-12-25](https://medmain.com/news/60752/)). The 2026-02-17 release lists 浅子 信太郎 as management advisor and 深田 啓介 (エンジェルナビ CEO; advisor since [2024-04](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)) as financial advisor ([2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)). No CTO is listed on the company page. The Fullstack Engineer posting describes the development team as centred on a PdM who has been CTO/PdM at medical startups and the head of pathology-AI development, who is a pathologist, with engineers from Japan and abroad ([posting](https://open.talentio.com/r/1/c/medmain/pages/114519)).

Job categories on the applicant site are Engineering, Sales & Marketing, BizDev (R&D business development), AI Product Manager, and contract Doctor / pathologist liaison ([Talentio](https://open.talentio.com/r/1/c/medmain/homes/3686); accessed 2026-10-11).

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2018-08-17 | 第三者割当増資 | 1億円 | DEEPCORE TOKYO1号投資事業有限責任組合; 九州アントレプレナークラブ2号 (ドーガン・ベータ) | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000034505.html) |
| 2020-08-24 | 第三者割当増資 | 約11億円 | New: 国際医療福祉大学・高邦会グループ, 福岡和白病院グループ, QTnet, Hike Ventures, みらい創造機構, an SPV formed by Hike Ventures, individuals. Existing: ディープコア, ドーガン・ベータ | 約12億円 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000010.000034505.html) |
| 2022-07-26 | 第三者割当増資 (資本業務提携) | 3億円 | PSP | not stated | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000024.000034505.html) |
| 2024-04-18 | シリーズA2 | 8.5億円 | PSP, ミガロホールディングス, ニコン, エンジェルナビ・グループ, 福山太郎, individuals | 20.5億円 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000040.000034505.html) |
| 2025-05-08 | 第三者割当増資 | 4.7億円 | One Capital (lead), Niremia Collective, Plug and Play | 25億円 (equity) | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000046.000034505.html) |

The company names only the 2024 round (シリーズA2). [BRIDGE (2020-08)](https://thebridge.jp/2020/08/medmain-series-a-round-funding) described the 2020 round as roughly a Series A, and [BRIDGE (2024-04)](https://thebridge.jp/2024/04/medmain-series-a2-round-funding) called the 2024 round the second close of a Series A whose first close it placed at the 2022 PSP investment. PSP invested in 2022 and again in the Series A2. Medmain also received a NEDO grant of up to ¥200M in 2022 (see `Basic`).

### Acquisition by the TechMatrix group

TechMatrix and PSP signed a basic agreement on 2026-02-17 to acquire Medmain shares so that, with PSP's existing stake, they would hold a majority; the share-transfer agreement followed on 2026-04-24 and the transfer took effect on 2026-04-30, with the transfer date differing by selling shareholder ([TechMatrix TDnet, 2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf), [2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf), [Medmain, 2026-05-01](https://medmain.com/news/63907/)).

| Holder | Before (as of 2026-01-31 or 2026-02-17) | After (2026-04-30) |
|---|---|---|
| TechMatrix | 0 | 8,427 common, 14,077 Class S preferred, 22,867 Class A preferred; 45,371 votes, 29.10% |
| PSP | 5,593 common, 17,080 Class A preferred; 22,673 votes, 15.00% | 12,738 common, 19,864 Class S preferred, 34,375 Class A preferred; 66,977 votes, 42.95% |
| 飯塚 統 | 43,581 common, 28.83% | Excluded from the purchase; post-transaction ratio not stated |
| DEEPCORE TOKYO 1号投資事業有限責任組合 | 8.81% | Within the purchase scope |
| One Capital DX2号投資事業有限責任組合 | 7.54% | Within the purchase scope |
| One Capital2号投資事業有限責任組合 | 4.93% | Within the purchase scope |

The consideration was about ¥2.3B in total — about ¥1.16B from TechMatrix and ¥1.14B from PSP — paid to the selling shareholders, not to Medmain ([2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)). Before the deal PSP had one director on Medmain's board ([2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)).

### Financials disclosed by TechMatrix

Medmain's results for the last three fiscal years, as given in the [2026-02-17 disclosure](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) (labelled 連結, ¥ thousand):

| Fiscal year (December) | 2022 | 2023 | 2024 |
|---|---|---|---|
| Revenue | 60,742 | 171,148 | 248,820 |
| Operating loss | △390,341 | △324,929 | △277,162 |
| Ordinary loss | △376,411 | △220,942 | △242,070 |
| Net loss | △377,074 | △221,561 | △242,644 |
| Net assets | 296,397 | 389,460 | 155,949 |
| Total assets | 375,885 | 470,552 | 216,807 |

---

## Engineering

### Technology stack and platforms

- **Confirmed by product documentation:** AWS for storage and Auth0 for authentication ([PidPort FAQ](https://service.medmain.com/service/pidport); accessed 2026-10-11).
- **Confirmed by the company's papers (ML research):** TensorFlow; Keras with a TensorFlow backend; scikit-learn; Inception-v3 trained from scratch with max-pooling and RNN aggregation over tiles ([Sci Rep 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6992793/fullTextXML)); EfficientNetB1 with partial fine-tuning and weakly-supervised learning ([PLOS ONE 2022](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9683606/fullTextXML)); StarDist nucleus detection ([Diagnostics 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12984776/fullTextXML)). Datasets were scanned with Leica Aperio AT2 and stored as SVS with JPEG2000 compression.
- **Listed in the current Fullstack Engineer posting (技術環境):** Kotlin (Spring, Spring Boot) and Python backends; React.js and TypeScript frontend; MySQL and MongoDB; AWS; Terraform; Jira; Zoom, Slack, Notion, Google Workspace. The posting adds that the stack is chosen per development phase ([posting](https://open.talentio.com/r/1/c/medmain/pages/114519); Undated; accessed 2026-10-11).
- **Public GitHub assets:** the organisation [`medmain`](https://github.com/medmain) ("Medmain Inc.", created 2018-04-25) had 15 public repositories on 2026-10-11. Original repositories include `react-openseadragon` (React wrapper for the OpenSeadragon image viewer; last push 2021-01-18), `react-ui-kit` ("React shared components used by Medmain applications"; 2022-07-18) and `ml-lung-subtype` (2021-02-22). Forks include `openslide`, `libvips`, `cantaloupe` (IIIF image server), `geotiff.js` (last push 2026-02-14), `auth0-java` (2025-11-21), `tensorflow` and `terraform-aws-vpc`. Forks do not establish production use.

### Systems

| System | What it does | Source |
|---|---|---|
| PidPort cloud and viewer | WSI upload, storage, search, tiled browser viewing, annotation, comments and multi-slide sync for organisations and individuals | [PidPort page](https://service.medmain.com/service/pidport), [plan page](https://service.medmain.com/service/personal) |
| WSI classification models | Tile-level CNNs aggregated to slide-level predictions; trained on WSIs annotated by pathologists with an in-house annotation tool; the company says it has a transfer-learning base that speeds up model development ("partial transfusion", MIDL 2021) | [products](https://medmain.com/products/), [2021-07-09](https://medmain.com/news/2164/), [Sci Rep 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6992793/fullTextXML) |
| Training loop (2018 design) | Uploaded images analysed by AI on a web server; part of the analysed images sent to a supercomputer for additional training | [2018-10-15](https://prtimes.jp/main/html/rd/p/000000004.000034505.html) |
| Cell-level IHC quantification | Nucleus detection plus classification to compute the Ki-67 labelling index inside a pathologist-chosen ROI; ROC-AUC 0.981 for positive-cell classification | [2026-04-03](https://prtimes.jp/main/html/rd/p/000000055.000034505.html) |
| Findings-text check (patent) | Compares a pathologist's findings text with AI-generated findings from the image, scoring similarity to flag typos, omissions and inconsistencies | [2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html) |
| Slide digitisation | Contract scanning operation and delivery pipeline | [FAQ](https://service.medmain.com/faq) |
| Pathology cloud PACS | NOBORI pathology service built with PSP | [2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html) |
| Self-service billing | Individual sign-up, plan selection and online payment with promotion codes | [2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html) |

Papers with Medmain affiliation indexed in Europe PMC numbered 26 on 2026-10-11, mostly 2020–2023, on stomach, colon, lung, breast, pancreas, prostate, cervix and urine cytology, melanoma and lymph-node metastasis ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AFF%3A%22Medmain%22&format=json&pageSize=100&resultType=lite)). Data sources named include Hiroshima University Hospital, International University of Health and Welfare Mita Hospital and the Kamachi Group hospitals. The company also publishes an opt-out notice for a multi-centre gastric-biopsy AI study in which it is a participating site ([情報公開](https://medmain.com/disclosure/)).

### Technical background sought

- **Fullstack Engineer — required:** Java development (5+ years); database design (3+ years); experience introduced as "within the last three years" of Kotlin or Scala, cloud development such as AWS, container-based development such as Docker, REST API development, and GitHub or GitLab; and the ability to communicate in Japanese. **Preferred:** Python, React/TypeScript, authentication services such as Auth0, Terraform or other infrastructure as code ([posting](https://open.talentio.com/r/1/c/medmain/pages/114519)).
- **AI Product Manager — required:** PdM/PM of AI/ML products, product strategy at an AI startup, medical/health-AI business development, SaMD development or planning, AI consulting or AI business ownership. **Preferred:** PMDA/FDA regulatory work, AI validation design, QMS, pathology. Duties include deciding whether to pursue SaMD approval and designing the business strategy if approval is not pursued ([posting](https://open.talentio.com/r/1/c/medmain/pages/127108); Undated; accessed 2026-10-11).

### Industry domain

Histopathology and cytology: glass slides and WSIs, scanner file formats, H&E and immunohistochemistry, biopsy and resection specimens, and the pathologist's report. Regulation includes the PMD Act (薬機法), program medical devices (SaMD), 製造販売業 licences and ISO 13485 quality management, plus research-ethics procedures such as opt-out notices. The AI Product Manager posting treats SaMD and pathology knowledge as preferred, and the R&D Business Development posting lists pathology understanding and life-science knowledge as preferred ([R&D BD posting](https://open.talentio.com/r/1/c/medmain/pages/127106)). No posting reviewed states that the domain can be learned after joining.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | Fullstack Engineer: Japanese communication required. AI Product Manager: English communication with overseas members among duties. Recruiting note: many opportunities to use English inside and outside the company; many foreign-national employees, mainly engineers. No company-wide language policy found | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519), [AI PM](https://open.talentio.com/r/1/c/medmain/pages/127108), [recruiting note](https://medmain.notion.site/recruiting-note) |
| Location and remote | Fukuoka HQ and Tokyo office. Fullstack posting: no fixed work location, full remote possible in Japan or abroad. Recruiting site: remote depends on role. Recruiting note: employees work remotely from places including London and China | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519), [recruiting site](https://recruit.medmain.com/), [recruiting note](https://medmain.notion.site/recruiting-note) |
| Working time | Discretionary work (裁量労働制) for engineers, flextime for business roles; 8-hour standard day; overtime exists | [recruiting note](https://medmain.notion.site/recruiting-note), [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519) |
| Salary | Fullstack Engineer (full-time): ¥8,000,000–¥12,000,000 a year. Fullstack Engineer (contract): ¥840,000–¥1,000,000 a month for 25–30+ hours a week. AI Product Manager and R&D Business Development: ¥10,000,000–¥12,000,000 a year | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519), [contract](https://open.talentio.com/r/1/c/medmain/pages/86431), [AI PM](https://open.talentio.com/r/1/c/medmain/pages/127108), [R&D BD](https://open.talentio.com/r/1/c/medmain/pages/127106) |
| Equity | Stock options granted to members who meet a tenure requirement | [recruiting note](https://medmain.notion.site/recruiting-note) |
| Leave and probation | Weekends and holidays off, 120+ days a year; 3-month probation | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519) |
| Benefits | Language-learning allowance, relocation subsidy, transport allowance, health checks | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519) |
| Side jobs | No restriction on side jobs | [recruiting note](https://medmain.notion.site/recruiting-note) |
| Team profile | Average age in the late 30s | [recruiting note](https://medmain.notion.site/recruiting-note) |
| Visa, new graduates | Not stated in the postings reviewed | — |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11): medmain.com sitemap and WordPress post index (275 posts, 2015-12 to 2026-10), the company page, products and disclosure pages; service.medmain.com sitemap, product, FAQ and case pages; recruit.medmain.com, the Notion recruiting note and the Talentio applicant site; the PR TIMES company feed (company ID 34505); blog.medmain.com; TechMatrix's IR release list and both TDnet disclosures; the NTA corporate-number site; Europe PMC; GitHub organisation searches for `medmain`, `medmain-inc`, `medmaininc`, `pidport` and `medmain-ai`; Wantedly, Japan Dev and web searches in Japanese and English for メドメイン, Medmain and PidPort.

- **PMDA approval or certification.** No approval or certification of a Medmain product was announced in the press index or the PR TIMES feed, and current product pages describe AI analysis in Japan as planned. PMDA's own device database was not queried interactively.
- **Engineering headcount.** Not published; the only total is 15 employees in the 2026-02-17 TechMatrix disclosure.
- **Revenue after FY2024 and Medmain's post-acquisition results.** Not found.
- **Organisation pricing** for PidPort and the scanning service. Quoted individually.
- **Engineering blog.** None found. The official blog [Medmain Speaks](https://blog.medmain.com/) last posted on 2025-05-08 (Japanese) and 2025-05-09 (English), with categories news, people & culture and pathology; its people posts date from 2020.
- **Status page, SLA, data-residency statement.** None found.
- **Visa sponsorship and new-graduate hiring.** Not stated.

### Inconsistencies across sources

- **Medical-device licence:** the [2024-08-02 release](https://prtimes.jp/main/html/rd/p/000000041.000034505.html) announces a 第一種医療機器製造販売業 licence, number 13B1X10433, issued 2024-07-02; the [company page](https://medmain.com/aboutus/) (accessed 2026-10-11) lists 第二種医療機器製造販売業, number 13B2X10662. Neither source mentions the other number.
- **Capital:** 11億9000万円 including capital reserve on the [company page](https://medmain.com/aboutus/), the [Talentio postings](https://open.talentio.com/r/1/c/medmain/pages/114519) and the [PR TIMES company profile](https://prtimes.jp/main/html/rd/p/000000054.000034505.html); 資本金 1億円 in the body of Medmain's [2026-02-17 release](https://prtimes.jp/main/html/rd/p/000000054.000034505.html) and in the [TechMatrix disclosure](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf).
- **Cumulative funding:** the announced rounds add up to about 28.2億円 (1 + 約11 + 3 + 8.5 + 4.7), against a stated 25億円 cumulative equity total ([2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)). The Series A2 release gives 20.5億円 after an 8.5億円 round, which implies 12億円 before it — the same figure the [2020 release](https://prtimes.jp/main/html/rd/p/000000010.000034505.html) gave before the 3億円 PSP investment of 2022. [BRIDGE](https://thebridge.jp/2020/08/medmain-series-a-round-funding) put the total at about 15億円 after 2022.
- **Supported file formats:** the PidPort feature list includes vsi, isyntax and i2syntax; the [FAQ](https://service.medmain.com/faq) lists PNG, JPEG, TIFF, SVS and NDPI; the FAQ block on the [PidPort page](https://service.medmain.com/service/pidport) lists JPEG, TIFF, SVS and NDPI and says Leica SCN support is coming.
- **PidPort Personal launch date:** announced on medmain.com on [2026-07-01](https://medmain.com/news/65758/) and on PR TIMES on [2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html).

### Other

- The business includes services as well as software: slide scanning, a cloud PACS co-developed with the parent group, and individual subscriptions launched in 2026.
- The [2020-08-24 release](https://prtimes.jp/main/html/rd/p/000000010.000034505.html) said a regulatory filing for AI analysis in Japan was in progress (薬事申請を進めています); the [2023-12-18 post](https://medmain.com/news/34196/) and the 2024 and 2025 releases describe approval as a goal; no approval announcement followed in the sources reviewed.
- PSP's own customer count is given differently over time in Medmain's releases: about 2,200 facilities ([2022-07-26](https://prtimes.jp/main/html/rd/p/000000024.000034505.html)), 2,300+ ([2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)), 2,400+ ([2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html)) and 2,600 ([2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)).
- Of the 20 most recent posts in the medmain.com news index on 2026-10-11, 8 are booth-exhibition announcements for academic meetings.

---

## Resources

**Official**

- [Corporate site](https://medmain.com/) — [About us and company profile](https://medmain.com/aboutus/), [Products](https://medmain.com/products/), [情報公開 (opt-out notice)](https://medmain.com/disclosure/)
- [Product site](https://service.medmain.com/service/pidport) — [PidPort Personal](https://service.medmain.com/service/personal), [FAQ](https://service.medmain.com/faq), [Reasons](https://service.medmain.com/reason), [Use scenes](https://service.medmain.com/scene), [Case studies](https://service.medmain.com/case)
- [Recruiting site](https://recruit.medmain.com/) — [CEO message](https://recruit.medmain.com/message), [Recruiting note (Notion)](https://medmain.notion.site/recruiting-note)
- [Applicant site (Talentio)](https://open.talentio.com/r/1/c/medmain/homes/3686) — [Fullstack Engineer](https://open.talentio.com/r/1/c/medmain/pages/114519), [Fullstack Engineer (contract)](https://open.talentio.com/r/1/c/medmain/pages/86431), [AI Product Manager](https://open.talentio.com/r/1/c/medmain/pages/127108), [R&D Business Development](https://open.talentio.com/r/1/c/medmain/pages/127106)
- [Official blog, Medmain Speaks](https://blog.medmain.com/)
- [GitHub organisation](https://github.com/medmain)

**Press releases and announcements (JA — newest first)**

- [PidPort Personal (PR TIMES) — 2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html)
- [PidPort Personal (medmain.com) — 2026-07-01](https://medmain.com/news/65758/)
- [Consolidated subsidiary of TechMatrix — 2026-05-01](https://medmain.com/news/63907/)
- [Ki-67 AI, Diagnostics paper — 2026-04-03](https://prtimes.jp/main/html/rd/p/000000055.000034505.html)
- [Joining the TechMatrix group — 2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)
- [日経 NEXTユニコーン2025 — 2026-01-21](https://medmain.com/news/61450/)
- [Tsuneki in Top 2% Scientists — 2025-12-25](https://medmain.com/news/60752/)
- [Findings-text patent — 2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html)
- [Ha Dong General Hospital — 2025-10-20](https://prtimes.jp/main/html/rd/p/000000052.000034505.html)
- [Thống Nhất Hospital — 2025-09-12](https://medmain.com/news/57578/)
- [令和7年度 IPO Growth Program — 2025-09-03](https://medmain.com/news/57313/)
- [SMC partnership, Vietnam — 2025-08-01](https://prtimes.jp/main/html/rd/p/000000050.000034505.html)
- [Vietnam hospital MOUs — 2025-07-25](https://prtimes.jp/main/html/rd/p/000000049.000034505.html)
- [AI医療機器協議会 director — 2025-06-17](https://medmain.com/news/54862/)
- [Mizuho Innovation Award — 2025-06-11](https://medmain.com/news/54666/)
- [Tottori University — 2025-05-21](https://medmain.com/news/53996/)
- [4.7億円 round — 2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)
- [ISO 13485 — 2025-02-19](https://prtimes.jp/main/html/rd/p/000000045.000034505.html)
- [日経 NEXTユニコーン2024 — 2025-01-31](https://medmain.com/news/50364/)
- [Forbes JAPAN AI 50 — 2025-01-30](https://medmain.com/news/50262/)
- [Adopted at over half of medical universities — 2024-12-23](https://prtimes.jp/main/html/rd/p/000000044.000034505.html)
- [ISMS — 2024-11-29](https://prtimes.jp/main/html/rd/p/000000043.000034505.html)
- [NOBORI for pathology — 2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html)
- [IPO等に向けた成長支援プログラム — 2024-08-08](https://medmain.com/news/44474/)
- [第一種医療機器製造販売業許可 — 2024-08-02](https://prtimes.jp/main/html/rd/p/000000041.000034505.html)
- [Medteria spin-off — 2024-08-01](https://medmain.com/news/52692/)
- [High Growth Program — 2024-08-01](https://medmain.com/news/44031/)
- [Series A2, 8.5億円 — 2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)
- [JP-AID gastric-biopsy AI — 2023-12-18](https://medmain.com/news/34196/)
- [Japan Innovation Campus — 2023-11-22](https://prtimes.jp/main/html/rd/p/000000038.000034505.html)
- [Kurume University — 2023-11-02](https://medmain.com/news/32208/)
- [AMED project — 2023-09-07](https://prtimes.jp/main/html/rd/p/000000034.000034505.html)
- [U.S. Market Gateway Accelerator — 2023-09-06](https://prtimes.jp/main/html/rd/p/000000035.000034505.html)
- [AI医療機器協議会 membership — 2023-04-17](https://medmain.com/news/25661/)
- [PSP alliance, 3億円 — 2022-07-26](https://prtimes.jp/main/html/rd/p/000000024.000034505.html)
- [NEDO grant — 2022-06-27](https://prtimes.jp/main/html/rd/p/000000023.000034505.html)
- [Transfer-learning base technology — 2021-07-09](https://medmain.com/news/2164/)
- [約11億円 round — 2020-08-24](https://prtimes.jp/main/html/rd/p/000000010.000034505.html)
- [Forbes 30 Under 30 Asia — 2020-04-02](https://medmain.com/news/1743/)
- [Overseas launch of PidPort — 2020-03-10](https://prtimes.jp/main/html/rd/p/000000009.000034505.html)
- [日本オープンイノベーション大賞 — 2020-02-19](https://medmain.com/news/1692/)
- [J-Startup — 2019-06-26](https://medmain.com/pressrelease/1563/)
- [Imaging Center opens — 2019-06-17](https://medmain.com/pressrelease/1552/)
- [起業家万博 総務大臣賞 — 2019-04-06](https://medmain.com/pressrelease/1504/)
- [飛躍 Next Enterprise — 2018-12-21](https://medmain.com/pressrelease/1441/)
- [PidPort α version — 2018-10-15](https://prtimes.jp/main/html/rd/p/000000004.000034505.html)
- [1億円 round — 2018-08-17](https://prtimes.jp/main/html/rd/p/000000003.000034505.html)
- [Medteria launch — 2018-06-11](https://prtimes.jp/main/html/rd/p/000000001.000034505.html)
- [Latitude59 — 2018-05-30](https://medmain.com/news/1037/)
- [Medmain USA Inc. — 2018-05-22](https://medmain.com/pressrelease/1023/)
- [Founding — 2018-01-11](https://medmain.com/pressrelease/829/) · [Medmain Inc. established — 2018-01-11](https://medmain.com/pressrelease/748/)
- [Live Sharks Tank — 2017-11-24](https://medmain.com/news/672/)
- [OMEGA selected by Kyushu University — 2017-05-24](https://medmain.com/pressrelease/324/)
- [九医クラウド — 2016-06-20](https://medmain.com/pressrelease/322/)
- [Site launch — 2015-12-28](https://medmain.com/news/35/)

**Regulator and parent-company filings**

- [国税庁 法人番号公表サイト — 2290001080259 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259)
- [TechMatrix TDnet — basic agreement, 2026-02-17 (JA)](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)
- [TechMatrix TDnet — share-transfer agreement, 2026-04-24 (JA)](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)

**Research papers (via Europe PMC)**

- [Medmain-affiliated papers — search](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AFF%3A%22Medmain%22&format=json&pageSize=100&resultType=lite)
- [Gastric and colonic epithelial tumours, Scientific Reports 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6992793/fullTextXML)
- [Multi-organ adenocarcinoma, PLOS ONE 2022](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9683606/fullTextXML)
- [Ki-67 labelling index, Diagnostics 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12984776/fullTextXML)

**Third-party coverage and profiles**

- [BRIDGE — 2020 round (JA)](https://thebridge.jp/2020/08/medmain-series-a-round-funding) · [Series A2, 2024-04-18 (JA)](https://thebridge.jp/2024/04/medmain-series-a2-round-funding)
- [社長名鑑 — CEO interview (JA)](https://shachomeikan.jp/industry_article/3551)
