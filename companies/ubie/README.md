# Ubie

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Ubie (Ubie株式会社 / Ubie, Inc.; corporate number 7010701034132) is a Tokyo company founded in May 2017 by physician 阿部 吉倫 (Yoshinori Abe) and engineer 久保 恒太 (Kota Kubo). It runs three businesses on one AI questionnaire engine: the free consumer service 「ユビー」 (a symptom checker since 2020, joined on 2025-09-16 by a conversational 医療AIパートナー under the same name), hospital and clinic products sold as ユビーメディカルナビ (ユビーAI問診, ユビー生成AI, ユビーDPCサポーター, ユビーリンク), and disease-awareness and marketing solutions for pharmaceutical companies. A New York subsidiary, Ubie Inc., operates the English-language service at `ubiehealth.com` and a provider product, Ubie Smart Support ([About](https://ubie.life/about_ubie), [Service](https://ubie.life/service); Undated; accessed 2026-10-11).

- **Scale:** 「ユビー」 has about 13 million monthly users, and ユビー生成AI is used in 160+ large hospitals, including 20+ university hospitals ([2026-09-28 release](https://prtimes.jp/main/html/rd/p/000000227.000048083.html)). The US company reports about 6 million monthly US users and 20M+ globally ([PR Newswire, 2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html)).
- **Funding:** cumulative funding since founding reached about 180億円, announced 2025-05-12. That total followed equity investments of undisclosed size from Google, 日本郵政キャピタル, NTTドコモ and セブン-イレブン・ジャパン, plus 10億円 long-term loans each from 商工中金 and 日本政策金融公庫 ([2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html)). The last named round is シリーズC, which closed at 62.6億円 on 2022-10-06 ([release](https://prtimes.jp/main/html/rd/p/000000044.000048083.html)). The corporate About page still shows 109.8億円; see `Notes`.
- **Headcount:** 220 as of April 2026 ([recruiting site](https://recruit.ubie.life/); accessed 2026-10-11). The corporate About page shows 240 as of April 2025 ([About](https://ubie.life/about_ubie)).
- **Engineering:** TypeScript/Node.js (a NestJS modular monolith behind a GraphQL BFF) for product services, Go for platform services, React/Next.js on the web, React Native for mobile, PostgreSQL on AlloyDB, and Kubernetes on Google Cloud ([Ubie tech blog](https://zenn.dev/p/ubie_dev); [postings](https://herp.careers/v1/ubiehr)). Every engineering posting reviewed is written in Japanese. The one posting that states a language requirement asks for native-level Japanese. No English-language engineering posting was found.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Legal name | Ubie株式会社 (英文社名: Ubie, Inc.); registered as Ｕｂｉｅ株式会社, reading ユビー | [About](https://ubie.life/about_ubie); [NTA 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132) |
| Corporate number | 7010701034132; assigned 2017-05-12; registry record last updated 2024-12-26 | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132); accessed 2026-10-11 |
| Founded | May 2017 | [About](https://ubie.life/about_ubie) |
| HQ (registered address) | 〒103-0023 東京都中央区日本橋本町三丁目8番4号 日本橋ライフサイエンスビルディング4 5F; registered address since 2024-12-09 | [About](https://ubie.life/about_ubie), [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132) |
| Representatives | 共同代表取締役 医師 阿部 吉倫; 共同代表取締役 久保 恒太 | [About](https://ubie.life/about_ubie) |
| Other officers listed | 社外取締役 重富 隆介; 社外監査役 弁護士 湯浅 紀佳 | [Company deck](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211) (Speaker Deck metadata: published 2026-05-05, modified 2026-09-27) |
| Headcount | 220 (as of 2026-04); 240 (as of 2025-04) | [Recruiting site](https://recruit.ubie.life/), [About](https://ubie.life/about_ubie) |
| Offices | Japan and the United States (New York) | [About](https://ubie.life/about_ubie), [business.ubiehealth.com](https://business.ubiehealth.com/) |
| Capital | 資本金 9,000万円 | [HERP posting company block](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd); Undated; accessed 2026-10-11 |
| Total raised | 約180億円 since founding | [2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html) |
| Consumer users | about 13 million monthly users of 「ユビー」 | [2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html) |
| Medical institutions | ユビーメディカルナビ in 1,800 institutions; 15,000+ institutions connected to the platform | [About](https://ubie.life/about_ubie), [Service](https://ubie.life/service); Undated; accessed 2026-10-11 |
| Pharma reach | about 90% of "global mega-pharma" (defined as annual revenue above US$10B) transact with Ubie | [About](https://ubie.life/about_ubie); Undated; accessed 2026-10-11 |
| Security and data handling | ISMS obtained October 2020; systems stated to comply with the 3省2ガイドライン; services run on Google Cloud Platform; a vulnerability disclosure policy (VCDP) is published | [Security management](https://ubie.life/safety/security_management), [Data protection](https://ubie.life/safety/data_protection), [VCDP](https://ubie.life/safety/vcdp); Undated; accessed 2026-10-11 |
| Hiring system | HERP (`ubiehr`); the recruiting site listed 47 postings (product 5, engineering 15, business 20, corporate 7) | [Recruiting site](https://recruit.ubie.life/); accessed 2026-10-11 |

**Programs and awards.** Ubie came out of the 4th batch of ZENTECH DOJO NIHONBASHI, a life-science accelerator run by インディージャパン ([BRIDGE, 2018-05](https://thebridge.jp/2018/05/ubie-jpy300m-funding)). In 2020 it was selected for JETRO's 日ASEANにおけるアジアDX促進事業 ([2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html)), and in 2025 it took part in Mayo Clinic Platform_Accelerate through JETRO's HealthTech Gateway "AI Medical in the US" ([2025-09-04](https://prtimes.jp/main/html/rd/p/000000175.000048083.html)). It is listed on [J-Startup](https://www.j-startup.go.jp/startups/212-ubie.html); the page does not state a selection year. Awards announced by the company:

- 第3回 日本サービス大賞 厚生労働大臣賞 and 審査員特別賞 for AI問診ユビー ([2020-10-27](https://prtimes.jp/main/html/rd/p/000000009.000048083.html))
- Google Play ベスト オブ 2023, 優れた AI 部門 大賞 ([2023-11-30](https://prtimes.jp/main/html/rd/p/000000064.000048083.html))
- 生成AI大賞2024 特別賞 and 優秀賞 ([2024-12-19](https://prtimes.jp/main/html/rd/p/000000117.000048083.html))
- 日本スタートアップ大賞2026 厚生労働大臣賞 (医療・福祉スタートアップ賞), presented on 2026-09-25 ([2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html))

### Context as stated by the company

- The company says its own August 2025 survey found that 72% of respondents were "医療迷子", having trouble at some stage between noticing symptoms and getting treatment ([2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)).
- It presents hospital products against the 2024 working-hours cap for doctors (医師の働き方改革) and the FY2026 診療報酬改定 ([2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html), [2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html)).
- In the award release, it describes Japanese healthcare as facing rising demand and a shrinking workforce towards 2040 ([2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html)).

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Ubie株式会社 (Ubie, Inc.) | Legal entity | Japan; corporate number assigned 2017-05-12 | Parent company. Registered address moved from 品川区北品川 (2017) to 日本橋本町3-11-5 (2018-08-17), 日本橋室町1-5-3 (2019-03-04), 日本橋堀留町2-4-3 (2023-04-24) and 日本橋本町3-8-4 (2024-12-09) | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132) |
| Ubie, Inc. / Ubie Inc. (US) | Related entity (subsidiary) | New York; established 2022-10-04 | Called the US 現地法人. The representative was Naoto Shimazu at establishment and Kota Kubo in 2026. The US terms of use name "Ubie, a company incorporated under the laws of the State of New York" | [2022-12-08](https://prtimes.jp/main/html/rd/p/000000047.000048083.html), [2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html), [US terms](https://ubiehealth.com/terms) (last updated 2023-10-30) |
| Singapore entity (name not stated) | Related entity | Singapore; established by 2020-10-15 | Announced as Ubie's first overseas company. The current corporate site lists only Japan and US offices; its current status is not stated | [2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html), [About](https://ubie.life/about_ubie) |
| Dr. Ubie | Former product | India; 2018 test launch | Consumer web questionnaire. Test marketing was suspended after about six months | [2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html) |

The Japanese parent's English name and the US subsidiary's name are both "Ubie, Inc." Sources show it both with and without the comma. US-facing releases from PR Newswire carry "SOURCE Ubie, Inc." and do not say which entity issued them.

---

## Product

### Line-up

| Product | For | What it is | Source |
|---|---|---|---|
| 「ユビー」 (症状検索エンジン, launched as AI受診相談ユビー in April 2020; 医療AIパートナー added 2025-09-16) | Consumers, Japan | Free app and web service. The symptom search asks about 20 doctor-supervised questions and returns related diseases, self-care information and nearby institutions. Since 2025-09-16 it also offers conversational guidance that remembers the user's situation and can use マイナポータル prescription and visit history | [2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html), [2024-10-01](https://prtimes.jp/main/html/rd/p/000000105.000048083.html), [ubie.app terms](https://ubie.app/terms) |
| ユビーAI問診 | Hospitals and clinics | AI pre-visit and in-clinic questionnaire. Questions branch on the patient's answers, a draft medical record is generated in "医師語", and it can link with electronic medical records. Offered since 2018 | [Product page](https://intro.dr-ubie.com/products/aimon), [2022-07-27](https://prtimes.jp/main/html/rd/p/000000039.000048083.html) |
| ユビー生成AI (β launched 2024-05-02 as ユビーメディカルナビ 生成AI) | Hospitals | Multi-model generative AI for hospital staff: text generation and summarisation, speech recognition, image recognition and RAG. It runs in per-hospital environments with training on customer data turned off, and can link with EMRs and run on mobile devices | [2024-05-02](https://prtimes.jp/main/html/rd/p/000000076.000048083.html), [2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html), [Product page](https://intro.dr-ubie.com/products/generativeai_lp) |
| ユビーDPCサポーター | Hospitals | Suggests DPC codes from medical records and order data | [Product page](https://intro.dr-ubie.com/products/dpc-supporter), [2025-12-04](https://prtimes.jp/main/html/rd/p/000000191.000048083.html) |
| ユビーリンク / ホームページAI相談窓口 | Clinics and hospitals | Free listing of institutions in 「ユビー」 and a symptom-check banner for the institution's own website (ユビーリンク launched 2021-07-27) | [Products](https://intro.dr-ubie.com/products), [2021-07-27](https://prtimes.jp/main/html/rd/p/000000022.000048083.html) |
| ユビー for Pharma / ユビーAds | Pharmaceutical companies | Disease and treatment awareness delivered to consumers and institutions through the platform, plus a healthcare-targeted ad product | [ph-ubie.com](https://ph-ubie.com/), [ユビーAds](https://ph-ubie.com/ubie_ads), [Service](https://ubie.life/service) |
| Ubie Symptom Checker (US) | Consumers, US | English symptom checker launched 2022-04-26: about 20 questions drawn from about 3,500 question types, covering 1,100+ diseases | [US release, 2022-04-26](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us) |
| Ubie Smart Support (US) | US practices and health systems | AI phone and chat agent that answers missed or after-hours calls, books appointments and hands calls off to staff | [Product page](https://business.ubiehealth.com/provider/smart-support), [2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html) |
| Ubie Self-Serve (US) | US advertisers | Self-serve ads targeted by symptom, disease prediction and specialty interest inside Ubie's patient experiences | [PR Newswire, 2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html) |

The company describes the core asset as a questionnaire engine built from 50,000 domestic and overseas medical papers under the supervision of 50+ physicians ([Service](https://ubie.life/service); Undated; accessed 2026-10-11).

### Commercialization

- **Consumer services** are free. The AI partner's launch release states 利用料金：無料 ([2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)).
- **ユビーAI問診** is priced from an annual licence fee, the tablets (iPads), and a network fee for EMR integration. Figures are available only through a download form ([Pricing](https://intro.dr-ubie.com/products/pricing); accessed 2026-10-11). ユビー生成AI was offered at 個別見積り (quoted individually) at launch ([2024-05-02](https://prtimes.jp/main/html/rd/p/000000076.000048083.html)). Packages tied to subsidy programmes from 厚生労働省 and the Tokyo metropolitan government were announced on [2024-07-08](https://prtimes.jp/main/html/rd/p/000000091.000048083.html), [2025-03-21](https://prtimes.jp/main/html/rd/p/000000136.000048083.html) and [2025-11-28](https://prtimes.jp/main/html/rd/p/000000190.000048083.html).
- **Pharma** revenue comes from disease-awareness projects and marketing solutions. No public price list was found. In the US, Self-Serve advertising has a published daily minimum ([2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html)), and Smart Support for practices has a published flat monthly fee ([product page](https://business.ubiehealth.com/provider/smart-support); accessed 2026-10-11).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2021-05-21 | AI問診ユビー in 400+ institutions across 47 prefectures | [Release](https://prtimes.jp/main/html/rd/p/000000020.000048083.html) |
| 2021-06-08 | AI受診相談ユビー passes 1 million monthly users, one year after launch | [Release](https://prtimes.jp/main/html/rd/p/000000021.000048083.html) |
| 2022-07-25 | ユビーAI問診 passes 1,000 institutions | [Release](https://prtimes.jp/main/html/rd/p/000000038.000048083.html) |
| 2022-09-07 | ユビーリンク passes 15,000 institutions | [Release](https://prtimes.jp/main/html/rd/p/000000043.000048083.html) |
| 2024-04-12 | 「ユビー」 and ユビー病気のQ&A together at about 10 million monthly users; ユビーメディカルナビ at 1,700+ institutions; deals with more than two-thirds of global mega-pharma | [Release](https://prtimes.jp/main/html/rd/p/000000073.000048083.html) |
| 2025-03-06 | About 12 million monthly users; 1,800+ institutions | [Release](https://prtimes.jp/main/html/rd/p/000000128.000048083.html) |
| 2025-06-26 | US symptom checker passes 4 million total users; 13M+ monthly users worldwide; marketing solutions used by 21 of the top 30 life-science companies | [PR Newswire](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html) |
| 2026-01 | ユビー生成AI in 100 hospitals, including 10+ university hospitals; 100,000+ sessions per month; 8,000+ registered use-case templates | [2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html) |
| 2026-06-03 | About 6 million monthly US users; 20M+ monthly users globally | [PR Newswire](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html) |
| 2026-09-28 | About 13 million monthly users; ユビー生成AI in 160+ large hospitals, including 20+ university hospitals | [Release](https://prtimes.jp/main/html/rd/p/000000227.000048083.html) |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2020-06-04](https://prtimes.jp/main/html/rd/p/000000005.000048083.html) | スズケン | 20億円 investment, with joint sales through its 240 branches |
| [2021-04-21](https://prtimes.jp/main/html/rd/p/000000019.000048083.html) | 武田薬品 | Collaboration on early detection of rare diseases, extended by a [comprehensive agreement on 2023-04-10](https://prtimes.jp/main/html/rd/p/000000052.000048083.html). Other pharma collaborations announced include Pfizer ([2021-10-15](https://prtimes.jp/main/html/rd/p/000000024.000048083.html)), Bayer ([2021-11-24](https://prtimes.jp/main/html/rd/p/000000026.000048083.html)) and Boehringer Ingelheim ([2022-02-02](https://prtimes.jp/main/html/rd/p/000000031.000048083.html)) |
| [2023-03-13](https://prtimes.jp/main/html/rd/p/000000050.000048083.html) | ファイザー | Joint OAB awareness work, which the company says led about 17,000 people to visit a medical institution |
| [2024-09-30](https://prtimes.jp/main/html/rd/p/000000104.000048083.html) | シミックホールディングス | Business alliance covering CRO, SMO and CSO work |
| [2024-10-08](https://prtimes.jp/main/html/rd/p/000000107.000048083.html) | Google | Investment, and an agreement to work on DX of Japan's healthcare system, including generative AI |
| [2025-03-27](https://prtimes.jp/main/html/rd/p/000000138.000048083.html) | NTTドコモ | Capital and business alliance: d-account login and data linkage, and joint pharma marketing |
| [2025-03-31](https://prtimes.jp/main/html/rd/p/000000139.000048083.html) | セブン-イレブン・ジャパン | Capital and business alliance; a 7NOW delivery link from symptom results as the first pilot |
| [2025-12-08](https://prtimes.jp/main/html/rd/p/000000192.000048083.html) | Medable (US) | Strategic partnership on decentralised clinical trials in Japan |
| [2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html) | Mayo Clinic (US) | Ubie Inc. starts co-development of Ubie Smart Support. Mayo Clinic has a financial interest in the technology |
| [2026-08-21](https://prtimes.jp/main/html/rd/p/000000224.000048083.html) | NeoX | Pharmacy booking via Reserve with Google, starting with about 300 pharmacies in Tokyo, Kanagawa and Chiba |
| [2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html) | 金沢医科大学病院 | Full use of ユビー生成AI in the EMR environment from October 2026 |

Hospital case releases make up much of the 2025–2026 press feed. Examples include 九州大学病院, where ユビーDPCサポーター is expected to improve revenue by more than 6,500万円 a year ([2025-12-04](https://prtimes.jp/main/html/rd/p/000000191.000048083.html)), and 北里大学病院, which decided to adopt ユビー生成AI ([2026-09-16](https://prtimes.jp/main/html/rd/p/000000226.000048083.html)).

### Stated plans

- **ユビー生成AI:** a ベッドコントロール (bed management) function is planned ([2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)).
- **Ubie Smart Support:** Ubie and Mayo Clinic plan a chronic-disease management add-on module ([2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)).
- **Use of funds, 2024:** development and growth of the pharma business, consumer features, new businesses, and marketing for 「ユビー」 ([2024-04-12](https://prtimes.jp/main/html/rd/p/000000073.000048083.html)).
- **Partnerships, 2025:** the company says it will combine the technology and nationwide networks of Google, 日本郵政グループ, NTTドコモ and セブン-イレブン with its own ([2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html)).

---

## Founder

**阿部 吉倫 (Yoshinori Abe)**, physician, co-founder and 共同代表取締役 ([About](https://ubie.life/about_ubie)).

- Graduated from the University of Tokyo Faculty of Medicine in 2015, then did initial residency at 東京大学医学部付属病院 and 東京都健康長寿医療センター.
- Moved into data science after meeting a patient who had ignored rectal bleeding and died at 48.
- Co-founded Ubie in May 2017.
- Member of the 日本救急医学会 救急AI研究活性化特別委員会 from December 2019.
- Named to Forbes 30 Under 30 Asia (Healthcare & Science) in 2020.
- Director of the 日本医療ベンチャー協会 (JMVA) since 2023.

**久保 恒太 (Kota Kubo)**, engineer, co-founder and 共同代表取締役 ([About](https://ubie.life/about_ubie)).

- Graduated from the University of Tokyo Graduate School of Engineering.
- In 2013, while still at the university, began researching and building software and algorithms that simulate doctors' symptom-to-disease associations.
- Worked for about three years at エムスリー on B2C healthcare software, including a doctor Q&A service, and on web marketing.
- Co-founded Ubie in 2017.
- Described as 共同代表取締役 兼 Ubie US CEO and as the representative of Ubie Inc. ([2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)).

### Selected leadership

| Name | Role as written | Source |
|---|---|---|
| Yuku Kotani | "Ubie, Inc. CTO" (self-description on his Zenn profile). A 2025-06-16 post on the company tech blog calls him VP of Technology | [Zenn profile](https://zenn.dev/yuku) (accessed 2026-10-11), [tech blog post](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) |
| 西田 (given name not stated) | CFO | [News index](https://ubie.life/news), item dated 2026-06-26 |
| 風間 正弘 | Chief AI Officer (CAIO) | [News index](https://ubie.life/news), items dated 2026-01-16 and 2026-03-05 |
| 井上 真夢 | アクセラレーター本部代表・政策渉外参事 | [News index](https://ubie.life/news), item dated 2026-01-16 |
| 西村 里穂 | 医療機関事業本部長 (joined 2018 according to the recruiting site) | [2026-08-07](https://prtimes.jp/main/html/rd/p/000000223.000048083.html), [Recruiting site](https://recruit.ubie.life/) |
| 重富 隆介 | 社外取締役 from 2022-10. He was 代表取締役会長 of ブラックストーン・グループ・ジャパン at appointment | [2022-10-06](https://prtimes.jp/main/html/rd/p/000000044.000048083.html), [Company deck](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211) |
| 吉川 和美 | 常勤監査役 from 2022-10 (a CPA). She is not listed in the 2026 company deck | [2022-10-06](https://prtimes.jp/main/html/rd/p/000000044.000048083.html) |

Engineering postings name a CTO as the owner of engineering vision and technical strategy. They also recruit a VP of Engineering, a Head of Platform Engineering and an engineering manager who would work with the CTO ([EM posting](https://herp.careers/v1/ubiehr/9QuHU73KCC2P), [VPoE posting](https://herp.careers/v1/ubiehr/x3F1XHsBBT_L)).

The recruiting site lists these organisations ([Division page](https://recruit.ubie.life/division-Introduction); accessed 2026-10-11):

- ファーマイノベーション事業本部 (pharma)
- 病院事業本部 (hospitals)
- クリニック/薬局事業本部 (clinics and pharmacies)
- Global事業本部, based in New York
- プロダクトプラットフォーム本部, which develops products for all business units
- テクノロジープラットフォーム本部 (technology platform)
- アクセラレーター本部, which covers alliances, policy, finance, risk, HR and corporate functions
- 生成AI推進室, reporting directly to management

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2017-09 | Seed (reported by BRIDGE; no company release) | 6,000万円 | D4V | — | [BRIDGE, 2018-05](https://thebridge.jp/2018/05/ubie-jpy300m-funding) |
| 2018-05-07 | Not stated (J-KISS) | Not disclosed; BRIDGE estimated 3億円 and called it Series A | 関電ベンチャーマネジメント | — | [BRIDGE, 2018-05](https://thebridge.jp/2018/05/ubie-jpy300m-funding) |
| 2020-06-04 | 資金調達 (round not named) | 約20億円 | スズケン | — | [Release](https://prtimes.jp/main/html/rd/p/000000005.000048083.html) |
| 2021-04 | Cumulative update (no round) | — | — | 44.8億円 | [Ubie note](https://note.com/ubie/n/n08baa940b694) |
| 2022-07-27 | シリーズC ファーストクローズ | 35億円 | New: 農林中金キャピタル, NVenture Capital, 第一生命保険, エッグフォワード, others. Existing: スズケン | 79.8億円 | [Release](https://prtimes.jp/main/html/rd/p/000000039.000048083.html) |
| 2022-10-06 | シリーズC (close) | +27.6億円; 62.6億円 for the round | Equity: 総合メディカル, AAIC Investment Pte. Ltd., 日本インパクト投資2号投資事業有限責任組合, 楽天キャピタル. Loans: 商工組合中央金庫, 日本政策金融公庫, みずほ銀行 | 107.2億円 (累計資本調達額) | [Release](https://prtimes.jp/main/html/rd/p/000000044.000048083.html) |
| 2024-04-12 | インパクトファイナンス (equity plus loans) | 約35億円 | Equity: 三井住友信託銀行 (as impact investment), JA三井リース, others. Loan facilities: 三井住友信託銀行, 三菱UFJ銀行, みずほ銀行 | Not stated | [Release](https://prtimes.jp/main/html/rd/p/000000073.000048083.html) |
| 2024-10-08 | 最新の資金調達ラウンド (not named) | Not disclosed | Google | Not stated | [Release](https://prtimes.jp/main/html/rd/p/000000107.000048083.html) |
| 2025-03-06 | 第三者割当増資 | Not disclosed | 日本郵政キャピタル | Not stated | [Release](https://prtimes.jp/main/html/rd/p/000000128.000048083.html) |
| 2025-03-27 | 資本業務提携 | Not disclosed | NTTドコモ | Not stated | [Release](https://prtimes.jp/main/html/rd/p/000000138.000048083.html) |
| 2025-03-31 | 資本業務提携 (第三者割当増資) | Not disclosed | セブン-イレブン・ジャパン | Not stated | [Release](https://prtimes.jp/main/html/rd/p/000000139.000048083.html) |
| 2025-05-07 | 長期融資 | 10億円 | 商工組合中央金庫 | Not stated | [Release](https://prtimes.jp/main/html/rd/p/000000148.000048083.html) |
| 2025-05-08 | 長期融資 (スタートアップ支援資金) | 10億円 | 日本政策金融公庫 | 約180億円 (announced 2025-05-12) | [Release](https://prtimes.jp/main/html/rd/p/000000149.000048083.html), [2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html) |

Notes on the table:

- Ubie's own releases name only one round, シリーズC. The 2020 スズケン release does not name a round. A MobiHealthNews headline listed in Ubie's own [note](https://note.com/ubie/n/n08baa940b694) calls it a "Series B" of US$18.7M.
- BRIDGE reported, citing スズケン's disclosure, that the investment gave スズケン roughly 10% of issued shares ([BRIDGE, 2020-06](https://thebridge.jp/2020/06/ubie-jpy2b-funding)).
- On 2022-07-27, the same day as the シリーズC first close, 中部電力 also took a third-party allotment as part of a business alliance; the amount was not stated ([release](https://prtimes.jp/main/html/rd/p/000000040.000048083.html)).
- The シリーズC close (2022-10) and the 2024 financing both mixed equity with bank loans, and the releases count both in the headline amount.
- The cumulative total rose from 107.2億円 (2022-10) to 約180億円 (2025-05), but the releases in between give amounts only for the 2024-04 financing (約35億円) and the two 2025 loans (10億円 each).
- In US-facing releases, Ubie states cumulative funding of "over $125M" ([2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)).

---

## Engineering

### Technology stack and platforms

Confirmed by the company's technical blog and public repositories unless marked otherwise.

- **Backend.** A December 2022 post by Yuku Kotani announced a company-wide decision to standardise new development on two languages: Node.js for product services and Go for shared platform services. The same decision chose GraphQL for frontend-facing services and gRPC between services ([Zenn, 2022-12-14](https://zenn.dev/yuku/articles/4437cde02a672b)). At that point Kotlin, Go, Node.js, Ruby and Python services were all running, and existing Server-Side Kotlin services were not to be rewritten just for the stack change. Later posts describe:
  - the BFF as a GraphQL server built as a NestJS modular monolith with Prisma ([Zenn, 2025-03-13](https://zenn.dev/nissy_dev/articles/nestjs-prisma-db-access-management));
  - a Kotlin personalisation feature being replaced by a Go service ([Zenn, 2025-06-16](https://zenn.dev/glassmonkey/articles/7f393a44ffb029)).
  
  A 2026 posting says user-facing services centre on a Node.js modular monolith, while authentication and authorisation and the PHR platform use Go ([posting](https://herp.careers/v1/ubiehr/sqYyDunoCtcf)).
- **Web and mobile.** React with Next.js on the web and Apollo Client on the frontend ([Zenn, 2022-12-14](https://zenn.dev/yuku/articles/4437cde02a672b)). The mobile app moved from Ionic (Capacitor) to React Native with Expo in early 2024 ([Zenn, 2024-11-18](https://zenn.dev/yuku/articles/46cf443d5dd25b)).
- **Data stores.** PostgreSQL, migrated from Cloud SQL to AlloyDB ([Zenn, 2025-02-05](https://zenn.dev/electricalsheep/articles/cf1d74b65ec64b)). Public repositories also include Cloud Spanner and Elasticsearch tooling (`spanner-kase`, `esqa`) ([GitHub](https://github.com/ubie-oss)).
- **Infrastructure.** Google Cloud Platform ([Data protection](https://ubie.life/safety/data_protection)), Kubernetes with multiple clusters, Terraform, and Cloud Workflows, which replaced Argo Workflows ([Zenn, 2025-02-05](https://zenn.dev/electricalsheep/articles/cf1d74b65ec64b)). The SRE posting adds CDN/WAF at the edge, Kubernetes with an Istio (Envoy) service mesh, and managed databases, all run by one small platform team ([posting](https://herp.careers/v1/ubiehr/QzoglruZi_M1)).
- **Data and analytics.** BigQuery and dbt; Lightdash as the BI tool, for which the company publishes a Terraform provider and pre-commit hooks ([GitHub](https://github.com/ubie-oss); [analytics posting](https://herp.careers/v1/ubiehr/Bilnrfg8U7vj)).
- **Internal generative AI.** An in-house tool that gives access to Gemini, GPT and Claude models, used weekly by 85% of employees as of June 2026. Contracted tools include Notion AI, NotebookLM, GitHub Copilot, Devin, Cursor, Azure OpenAI, Dify, Perplexity, v0 and Claude Code ([Generative AI page](https://recruit.ubie.life/generative-ai)). Internal AI services are built with Next.js/TypeScript, AlloyDB for PostgreSQL, LangChain/LangGraph, Go and Python ([Corporate AI Engineer posting](https://herp.careers/v1/ubiehr/_oeH0lYReImI)).
- **Hiring-only mentions:**
  - C#/.NET, MSI installers and Windows system programming, for an in-hospital client ([posting](https://herp.careers/v1/ubiehr/QC24-tv1B1S8));
  - Python, TypeScript or Go with LLM APIs; Elasticsearch and vector search ([AI/ML posting](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv));
  - OAuth2/OIDC, SAML and Auth0/Okta/Keycloak ([auth posting](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58));
  - Honeycomb, Datadog and OpenTelemetry, as preferred items ([SRE posting](https://herp.careers/v1/ubiehr/QzoglruZi_M1)).

### Systems

| System | What it does | Source |
|---|---|---|
| Questionnaire engine | AI picks follow-up questions from the patient's complaint and answers. It underlies the consumer symptom search, ユビーAI問診 and the US symptom checker | [Product page](https://intro.dr-ubie.com/products/aimon), [US release](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us) |
| AI partner | Conversational guidance with per-user memory and マイナポータル data linkage. References are limited to public bodies and specialist sites, with monitoring by a team that includes physicians | [2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html) |
| Hospital generative AI platform | Text, speech, image and RAG functions on isolated per-hospital environments, with EMR integration and mobile access. Hospitals build their own templates and workflows: 8,000+ templates (2026-01) and an average of 100+ workflows per hospital (2026-08) | [2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html), [2026-08-07](https://prtimes.jp/main/html/rd/p/000000223.000048083.html) |
| Hospital data-integration client | A Windows client inside hospital networks that watches directories and sends data to Ubie's cloud. It must work over on-premises, proxy, VPN and closed-network connections | [posting](https://herp.careers/v1/ubiehr/QC24-tv1B1S8) |
| Identity platform | Consumer, patient and clinician ID management: MFA, multi-tenancy, SSO/SAML, ID linkage between consumer and B2B products, and delegation of permissions to AI agents | [posting](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58) |
| Personalisation hub | A Go service that proposes next steps based on the user's state across products. It replaced a Kotlin feature tied to a pharma project-management system | [Zenn, 2025-06-16](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) |
| LLM platform operations | Capacity planning around model price, token-per-minute limits and latency; FinOps (committed-use discounts, spot instances, cost allocation); regulation-specific infrastructure for Japan and the US; an internal "Infra Agent" that handles part of investigations and cost analysis | [SRE posting](https://herp.careers/v1/ubiehr/QzoglruZi_M1) |
| Security analysis agent | An AI agent for security alert analysis, in operation for about a year | [Zenn, 2026-03-31](https://zenn.dev/mizutani/articles/ai-sec-alert-ops) |

The company runs a technical blog as a Zenn publication, "Ubie テックブログ", with 186 posts between 2020-12-18 and 2026-07-31 ([Zenn](https://zenn.dev/p/ubie_dev); counted 2026-10-11). The recruiting site lists its events on connpass ([Generative AI page](https://recruit.ubie.life/generative-ai)). The GitHub organisation `ubie-oss` (name "Ubie, Inc.", created 2021-11-19) has 51 public repositories, 34 of them not forks. They include:

- `slack-mcp-server`, the most-starred, with 110 stars;
- `kotlin-graphql-sample`;
- `n8n-cli`;
- design-system packages (`ubie-ui`, `design-tokens`, `ubie-icons`) and the Ubie Vitals website;
- `nslog`, a structured logger for NestJS;
- `dbt-data-privacy` ([GitHub](https://github.com/ubie-oss); accessed 2026-10-11).

### Technical background sought

Required items in current engineering postings ([HERP](https://herp.careers/v1/ubiehr); accessed 2026-10-11):

- **Product engineer:** end-to-end value creation from a core specialism, from problem discovery to delivery and improvement, plus fast, deep dives into specialised domains ([posting](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)).
- **Product platform engineer:** React/TypeScript frontend, or Node.js/TypeScript or Go backend experience, and having led technology selection or design ([posting](https://herp.careers/v1/ubiehr/sqYyDunoCtcf)).
- **AI/ML engineer:** production web applications, production AI/ML features, and LLM-API systems in Python, TypeScript or Go, plus either RAG or agentic search, or evaluation of AI/ML systems ([posting](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv)).
- **Senior SRE:** production Kubernetes design and improvement (first-line monitoring alone does not count), IaC such as Terraform, production on Google Cloud or AWS, and Linux and network troubleshooting ([posting](https://herp.careers/v1/ubiehr/QzoglruZi_M1)).
- **Windows application engineer:** C#/.NET desktop apps, file-system monitoring, network programming, installers, and API or file integrations ([posting](https://herp.careers/v1/ubiehr/QC24-tv1B1S8)).
- **Engineering manager:** carrying organisational change through to completion. Startup experience is explicitly not required ([posting](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)).

Preferred items include:

- generative-AI-assisted development;
- Next.js and GraphQL API design;
- PostgreSQL;
- a Service Mesh (Envoy/Istio);
- cloud cost optimisation;
- SLO, error budget and postmortem practice;
- operating LLM products;
- persistent-memory AI agents;
- speech recognition;
- regulated-industry infrastructure.

### Industry domain

The work touches several areas of Japanese healthcare and US practice operations:

- **Hospital IT:** EMRs and 部門システム, closed hospital networks, HL7/FHIR, SS-MIX2, DICOM and レセコン ([Windows posting](https://herp.careers/v1/ubiehr/QC24-tv1B1S8)).
- **Security guidance:** the 3省2ガイドライン ([auth posting](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58); [Data protection](https://ubie.life/safety/data_protection)).
- **Hospital reimbursement and operations:** DPC/PDPS coding and 診療報酬改定 ([DPC page](https://intro.dr-ubie.com/products/dpc-supporter)).
- **Consumer health data:** PHR, and the マイナポータル linkage used in the consumer app ([2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)).
- **Pharma and trials:** pharma disease-awareness work and clinical trials (CRO, SMO, DCT) ([2024-09-30](https://prtimes.jp/main/html/rd/p/000000104.000048083.html), [2025-12-08](https://prtimes.jp/main/html/rd/p/000000192.000048083.html)).
- **Regulation by country:** the SRE posting notes that Japan and the US have different healthcare regulations ([posting](https://herp.careers/v1/ubiehr/QzoglruZi_M1)).

In postings, domain background is generally preferred rather than required:

- Medical information-system experience and the 医療情報技師 qualification (AI/ML).
- Hospital-system knowledge (Windows).
- Healthcare, health-tech or pharma experience (product roles).

The Product Engineer posting requires an inclination to dive deep into medicine and life sciences. Some Scrum teams include physicians as domain experts ([Company deck](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | All HERP engineering postings reviewed are in Japanese. Only the Product Security Engineer posting states a language requirement: 日本語（ネイティブレベル）. The US company page says all full-time roles are filled | [Security posting](https://herp.careers/v1/ubiehr/cQ6vihXLiMLg), [business.ubiehealth.com](https://business.ubiehealth.com/); accessed 2026-10-11 |
| Remote and office | FAQ: except some sales roles, employees choose where to work. Fully remote is possible if the person can come to the office about once a month. Postings vary: two office days a week mandatory (SRE, security), two days recommended (AI/ML, platform, analytics, Windows), or office only when needed, e.g. monthly business reviews and quarterly offsites (product engineer, VPoE) | [FAQ](https://recruit.ubie.life/faq), [SRE](https://herp.careers/v1/ubiehr/QzoglruZi_M1), [AI/ML](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv), [Product engineer](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) |
| Working-time system | Flextime or discretionary work, with no core time (contract staff excepted). Most engineering postings use 専門業務型裁量労働制, deemed at 9.5 hours a day. The product engineer posting uses full flextime with base hours of 10:00–19:00 and average overtime of 20–30 hours a month | [Work environment](https://recruit.ubie.life/work-environment), [postings](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) |
| Salary (published ranges) | ¥8M–15M: platform, auth, SRE, analytics, corporate AI. ¥10M–15M: AI/ML. From ¥10M: product engineer. ¥10M–18M: EM. ¥10M–20M: Head of Platform. ¥12M–25M: VPoE. ¥6M–12M: Windows, network. Up to about ¥20M: security roles. Interns ¥2,000/hour. Pay includes fixed overtime for 45 hours | [HERP](https://herp.careers/v1/ubiehr); accessed 2026-10-11 |
| Employment types | General Employee (総合職) and Expert (職務限定 / job-based) | [postings](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv) |
| Equity | Tax-qualified stock options ("U-win") for all full-time employees since April 2023, which can be kept and exercised after leaving. Statutory maternity leave (14 weeks) counts towards vesting | [2023-04-07](https://prtimes.jp/main/html/rd/p/000000051.000048083.html), [Work environment](https://recruit.ubie.life/work-environment) |
| Leave and probation | 125 days off a year (work-environment page) or 120 (postings); paid leave granted on joining; 6-month probation | [Work environment](https://recruit.ubie.life/work-environment), [posting](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) |
| Benefits | Babysitter subsidy, in-house physician consultations, equipment of choice, study and book costs, flu vaccination, side jobs allowed, 関東ITソフトウェア健康保険組合 | [Work environment](https://recruit.ubie.life/work-environment) |
| New graduates and juniors | No new-graduate/mid-career distinction. Current university students work as full-time employees on the same terms. A software engineering internship is listed | [FAQ](https://recruit.ubie.life/faq), [Intern posting](https://herp.careers/v1/ubiehr/9QxaWhCu--oj) |
| Organisation | Holacracy, with roles in place of managers. Scrum across product teams. Average employee age 36.5. About half of members are raising children | [Company deck](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211), [business.ubiehealth.com](https://business.ubiehealth.com/), [FAQ](https://recruit.ubie.life/faq) |
| Visa sponsorship | Not stated in the postings reviewed | [HERP](https://herp.careers/v1/ubiehr) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11). Names searched: Ubie, Ubie株式会社, ユビー, Ubie Inc., ubiehealth, and the product names (ユビーAI問診, ユビーメディカルナビ, ユビー生成AI, AI受診相談ユビー), in Japanese and English. Official sources: ubie.life (sitemap, About, Service, News, safety pages), recruit.ubie.life (sitemap pages and FAQ), the HERP board, intro.dr-ubie.com, ph-ubie.com, ubie.app terms, and ubiehealth.com / business.ubiehealth.com. Press: the PR TIMES company feed (198 releases, 2019-09-24 to 2026-10-09), PR Newswire and BRIDGE. Open source: the Zenn publication, Speaker Deck, and the GitHub organisations `ubie-oss`, `ubie-inc` and `ubieinc` (`ubie` and `ubiehealth` return 404). Registers and directories: the NTA 法人番号公表サイト, J-Startup and Japan Dev; TokyoDev returned HTTP 403.

- **Revenue and profit.** No figure was found in the releases, corporate pages or recruiting materials reviewed. 官報 決算公告 were not checked.
- **Amounts of the 2024–2025 equity investments** by Google, 日本郵政キャピタル, NTTドコモ and セブン-イレブン・ジャパン, and the name of the round they belong to.
- **CTO appointment.** No release or corporate page names the CTO. The only identification found is Yuku Kotani's self-description on Zenn.
- **Medical-device status.** No Ubie source reviewed says any product is approved or certified as a 医療機器プログラム under the 薬機法 / PMDA. The consumer terms say the service gives general reference information and does not provide diagnosis or treatment ([ubie.app terms](https://ubie.app/terms), last revised 2026-03-31).
- **ISMS details.** The certificate number, certification body and scope are not stated on the company's pages. The ISMS-AC registry was not searched because its search is a form submission.
- **Engineering headcount** and the split of headcount between Japan and the US.
- **The Singapore entity's** legal name and current status.
- **Price lists** for hospital and pharma products. Hospital pricing is only available through a download form.

### Inconsistencies across sources

- **Cumulative funding:** 109.8億円 ([About](https://ubie.life/about_ubie); Undated; accessed 2026-10-11) versus 約180億円 ([2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html); also the [HERP company block](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)) versus "over $125M" ([PR Newswire, 2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)). The About figure is close to the 107.2億円 stated at the シリーズC close in 2022-10.
- **Headcount:** 240 as of 2025-04 ([About](https://ubie.life/about_ubie)); 220 as of 2026-04 ([Recruiting site](https://recruit.ubie.life/), [deck](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211), [HERP](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)); "an organization of 200 members" ([business.ubiehealth.com](https://business.ubiehealth.com/); Undated). The 2026 deck still uses 240 as the base for its child-rearing ratio.
- **Medical-institution counts:** ユビーメディカルナビ in 1,800 institutions ([About](https://ubie.life/about_ubie)); feedback from "1700以上の医療機関" and links with "15,000件以上の医療機関" ([Service](https://ubie.life/service)); 病院事業本部 serves "5000を超える医療機関" ([Division page](https://recruit.ubie.life/division-Introduction)). None of these pages defines what is counted.
- **Pharma reach:** about 90% of global mega-pharma ([About](https://ubie.life/about_ubie)); more than two-thirds ([Division page](https://recruit.ubie.life/division-Introduction); also releases through [2025-05](https://prtimes.jp/main/html/rd/p/000000149.000048083.html)); more than 80% of major pharma companies (2026 [postings](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)); 21 of the top 30 life-science companies ([2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)); "50%+ Mega-Pharma Partnerships" ([business.ubiehealth.com](https://business.ubiehealth.com/)).
- **US address:** 1460 Broadway, New York, NY 10036 ([2022-12-08](https://prtimes.jp/main/html/rd/p/000000047.000048083.html), [2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)); 379 W Broadway, 2nd Floor, New York, NY 10012 ([business.ubiehealth.com](https://business.ubiehealth.com/), [deck](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)); 379 W Broadway, New York, NY 10036 ([HERP](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)).
- **Start of US operations:** a US release dated 2022-04-26 announces the US symptom checker launch ([release](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us)). A 2023-12-04 release from the same newsroom says US operations began in October 2022 ([release](https://business.ubiehealth.com/newsroom/ubie-used-by-2-million-americans-in-first-year)), which matches the US entity's founding on 2022-10-04.
- **Remote policy:** the [FAQ](https://recruit.ubie.life/faq) and [work-environment page](https://recruit.ubie.life/work-environment) say fully remote is possible. Several 2026 postings make two office days a week mandatory ([SRE](https://herp.careers/v1/ubiehr/QzoglruZi_M1)) or describe them as the norm ([EM](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)).
- **Annual days off:** 125 ([Work environment](https://recruit.ubie.life/work-environment)) versus 120 ([posting](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)).
- **Mayo Clinic data used in evaluation:** de-identified data from "3 million Mayo Clinic patients" ([2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)) versus 1千万人以上 ([2025-09-04](https://prtimes.jp/main/html/rd/p/000000175.000048083.html)).
- **Engineering language and offices on Japan Dev:** the [Japan Dev profile](https://japan-dev.com/companies/ubie) (Undated; marked unverified; no open jobs) says engineers do not need Japanese, tags visa sponsorship, and lists Tokyo and Singapore offices. Current postings are Japanese-only, one requires native Japanese, and the corporate site lists Japan and US offices.
- **Executive titles in English:** a 2022-04-26 US release calls Abe "Co-founder and CEO" and also names Kubo as CEO. Later US releases call Kubo "Co-Founder and CEO" (2025-06-26) and "co-founder and co-CEO" (2026-06-03). Japanese releases use 共同代表取締役 for both. Kotani is called VP of Technology in a [2025-06-16 post](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) and CTO on his [Zenn profile](https://zenn.dev/yuku).

### Other

- **Mission wording.** Releases up to 2026-07-01 use the mission 「テクノロジーで人々を適切な医療に案内する」. Releases from 2026-07-02 use 「テクノロジーで、医療の願いを解き放つ」, which the corporate and recruiting sites now show ([2026-07-02](https://prtimes.jp/main/html/rd/p/000000217.000048083.html), [About](https://ubie.life/about_ubie)). The 2026-10-08 Ubie Pharma Summit 2027 release still uses the earlier wording ([release](https://prtimes.jp/main/html/rd/p/000000230.000048083.html)). No release announcing the change was found.
- **Product names have changed several times:** AI受診相談ユビー → ユビーAI受診相談 → 症状検索エンジン「ユビー」, with 医療AIパートナー「ユビー」 added on 2025-09-16; AI問診Ubie → ユビーAI問診; ユビーメディカルナビ 生成AI → ユビー生成AI. Older releases use the earlier names.
- **Research, policy and events.** Ubie set up the research organisation Ubie Lab on 2023-07-31 ([release](https://prtimes.jp/main/html/rd/p/000000060.000048083.html)). Inside the 日本デジタルヘルス・アライアンス (JaDHA), it led a healthcare AI-safety evaluation guide with the AI Safety Institute, published in April 2026 ([2026-04-03](https://prtimes.jp/main/html/rd/p/000000211.000048083.html)). It has run an annual pharma-industry conference, Ubie Pharma Summit, since 2023-02-28; the 2027 edition is set for 2027-05-19 and 20 ([2023-02-01](https://prtimes.jp/main/html/rd/p/000000048.000048083.html), [2026-10-08](https://prtimes.jp/main/html/rd/p/000000230.000048083.html)).
- **Health-impact estimate.** The company estimates its health-span impact since founding at more than 2.7万年 (QALY increment) and its economic value at more than 1,500億円 ([2024-10-08](https://prtimes.jp/main/html/rd/p/000000107.000048083.html)). These are company estimates.
- **Press feed composition.** Many of the 198 PR TIMES releases are conference announcements (Ubie Pharma Summit, 日本医療生成AIフォーラム) and single-hospital adoption cases. Several are marked as visible to media users only.

---

## Resources

**Official**

- [Corporate site (JA)](https://ubie.life/): [About](https://ubie.life/about_ubie) · [Service](https://ubie.life/service) · [News index](https://ubie.life/news)
- Safety pages: [Data protection](https://ubie.life/safety/data_protection) · [Security management](https://ubie.life/safety/security_management) · [VCDP](https://ubie.life/safety/vcdp)
- [Hospital products (intro.dr-ubie.com)](https://intro.dr-ubie.com/products): [ユビーAI問診](https://intro.dr-ubie.com/products/aimon) · [Pricing](https://intro.dr-ubie.com/products/pricing) · [ユビー生成AI](https://intro.dr-ubie.com/products/generativeai_lp) · [ユビーDPCサポーター](https://intro.dr-ubie.com/products/dpc-supporter)
- [Pharma services (ph-ubie.com)](https://ph-ubie.com/) · [ユビーAds](https://ph-ubie.com/ubie_ads)
- Consumer service: [ユビー terms (JA)](https://ubie.app/terms) · [US terms](https://ubiehealth.com/terms)
- US company site: [business.ubiehealth.com](https://business.ubiehealth.com/) · [Origin](https://business.ubiehealth.com/origin) · [Ubie Smart Support](https://business.ubiehealth.com/provider/smart-support)
- US newsroom: [US launch, 2022-04-26](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us) · [2 million US uses, 2023-12-04](https://business.ubiehealth.com/newsroom/ubie-used-by-2-million-americans-in-first-year)
- [Recruiting site](https://recruit.ubie.life/): [FAQ](https://recruit.ubie.life/faq) · [Work environment](https://recruit.ubie.life/work-environment) · [Generative AI](https://recruit.ubie.life/generative-ai) · [Divisions](https://recruit.ubie.life/division-Introduction)
- [Job board on HERP](https://herp.careers/v1/ubiehr):
  - Product and platform: [Product Engineer](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) · [Product Platform Engineer](https://herp.careers/v1/ubiehr/sqYyDunoCtcf) · [Auth Platform Engineer](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58)
  - AI and data: [AI/ML Engineer](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv) · [Corporate AI Engineer](https://herp.careers/v1/ubiehr/_oeH0lYReImI) · [Analytics Engineer](https://herp.careers/v1/ubiehr/Bilnrfg8U7vj)
  - Infrastructure, clients and security: [Senior SRE](https://herp.careers/v1/ubiehr/QzoglruZi_M1) · [Windows Application Engineer](https://herp.careers/v1/ubiehr/QC24-tv1B1S8) · [Product Security Engineer](https://herp.careers/v1/ubiehr/cQ6vihXLiMLg)
  - Engineering leadership: [Engineering Manager](https://herp.careers/v1/ubiehr/9QuHU73KCC2P) · [VP of Engineering](https://herp.careers/v1/ubiehr/x3F1XHsBBT_L)
  - Internship: [Software Engineer Intern](https://herp.careers/v1/ubiehr/9QxaWhCu--oj)
- [Ubie テックブログ (Zenn)](https://zenn.dev/p/ubie_dev):
  - Stack: [Go and Node.js, 2022-12-14](https://zenn.dev/yuku/articles/4437cde02a672b) · [React Native, 2024-11-18](https://zenn.dev/yuku/articles/46cf443d5dd25b)
  - Data and infrastructure: [AlloyDB migration, 2025-02-05](https://zenn.dev/electricalsheep/articles/cf1d74b65ec64b) · [NestJS/Prisma modular monolith, 2025-03-13](https://zenn.dev/nissy_dev/articles/nestjs-prisma-db-access-management) · [Go personalisation platform, 2025-06-16](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) · [Security analysis AI agent, 2026-03-31](https://zenn.dev/mizutani/articles/ai-sec-alert-ops)
  - People: [Yuku Kotani profile](https://zenn.dev/yuku)
- [Ubie note: cumulative 44.8億円 (JA)](https://note.com/ubie/n/n08baa940b694)
- [Company deck on Speaker Deck (JA)](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)
- [GitHub organisation ubie-oss](https://github.com/ubie-oss)

**Press releases (PR TIMES, JA, newest first; [company feed](https://prtimes.jp/main/html/searchrlp/company_id/48083))**

- **2026:** [金沢医科大学病院 ユビー生成AI — 2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html) · [Ubie Pharma Summit 2027 — 2026-10-08](https://prtimes.jp/main/html/rd/p/000000230.000048083.html) · [日本スタートアップ大賞2026 — 2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html) · [北里大学病院 — 2026-09-16](https://prtimes.jp/main/html/rd/p/000000226.000048083.html) · [Reserve with Google pharmacy booking — 2026-08-21](https://prtimes.jp/main/html/rd/p/000000224.000048083.html) · [Google Cloud Next Tokyo talk — 2026-08-07](https://prtimes.jp/main/html/rd/p/000000223.000048083.html) · [九州がんセンター (first release with new mission) — 2026-07-02](https://prtimes.jp/main/html/rd/p/000000217.000048083.html) · [AISI healthcare AI-safety guide — 2026-04-03](https://prtimes.jp/main/html/rd/p/000000211.000048083.html) · [Ubie Inc. and Mayo Clinic — 2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html) · [ユビー生成AI 100 hospitals — 2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)
- **2025:** [Medable partnership — 2025-12-08](https://prtimes.jp/main/html/rd/p/000000192.000048083.html) · [九州大学病院 DPC — 2025-12-04](https://prtimes.jp/main/html/rd/p/000000191.000048083.html) · [Subsidy package — 2025-11-28](https://prtimes.jp/main/html/rd/p/000000190.000048083.html) · [医療AIパートナー「ユビー」 launch — 2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html) · [Mayo Clinic Platform_Accelerate — 2025-09-04](https://prtimes.jp/main/html/rd/p/000000175.000048083.html) · [Cumulative 180億円 — 2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html) · [日本政策金融公庫 loan — 2025-05-08](https://prtimes.jp/main/html/rd/p/000000149.000048083.html) · [商工中金 loan — 2025-05-07](https://prtimes.jp/main/html/rd/p/000000148.000048083.html) · [Seven-Eleven Japan alliance — 2025-03-31](https://prtimes.jp/main/html/rd/p/000000139.000048083.html) · [NTT DOCOMO alliance — 2025-03-27](https://prtimes.jp/main/html/rd/p/000000138.000048083.html) · [MHLW subsidy package — 2025-03-21](https://prtimes.jp/main/html/rd/p/000000136.000048083.html) · [Japan Post Capital — 2025-03-06](https://prtimes.jp/main/html/rd/p/000000128.000048083.html)
- **2024:** [生成AI大賞2024 — 2024-12-19](https://prtimes.jp/main/html/rd/p/000000117.000048083.html) · [Google investment — 2024-10-08](https://prtimes.jp/main/html/rd/p/000000107.000048083.html) · [Osaka Gas alliance — 2024-10-01](https://prtimes.jp/main/html/rd/p/000000105.000048083.html) · [CMIC alliance — 2024-09-30](https://prtimes.jp/main/html/rd/p/000000104.000048083.html) · [Tokyo subsidy package — 2024-07-08](https://prtimes.jp/main/html/rd/p/000000091.000048083.html) · [ユビーメディカルナビ 生成AI β — 2024-05-02](https://prtimes.jp/main/html/rd/p/000000076.000048083.html) · [Impact finance 約35億円 — 2024-04-12](https://prtimes.jp/main/html/rd/p/000000073.000048083.html)
- **2023:** [Google Play Best of 2023 — 2023-11-30](https://prtimes.jp/main/html/rd/p/000000064.000048083.html) · [Ubie Lab — 2023-07-31](https://prtimes.jp/main/html/rd/p/000000060.000048083.html) · [Takeda comprehensive agreement — 2023-04-10](https://prtimes.jp/main/html/rd/p/000000052.000048083.html) · [Stock option plan U-win — 2023-04-07](https://prtimes.jp/main/html/rd/p/000000051.000048083.html) · [Pfizer OAB results — 2023-03-13](https://prtimes.jp/main/html/rd/p/000000050.000048083.html) · [First Ubie Pharma Summit — 2023-02-01](https://prtimes.jp/main/html/rd/p/000000048.000048083.html)
- **2022:** [US subsidiary — 2022-12-08](https://prtimes.jp/main/html/rd/p/000000047.000048083.html) · [シリーズC close 62.6億円 — 2022-10-06](https://prtimes.jp/main/html/rd/p/000000044.000048083.html) · [ユビーリンク 15,000 — 2022-09-07](https://prtimes.jp/main/html/rd/p/000000043.000048083.html) · [Chubu Electric alliance — 2022-07-27](https://prtimes.jp/main/html/rd/p/000000040.000048083.html) · [シリーズC first close 35億円 — 2022-07-27](https://prtimes.jp/main/html/rd/p/000000039.000048083.html) · [ユビーAI問診 1,000 institutions — 2022-07-25](https://prtimes.jp/main/html/rd/p/000000038.000048083.html) · [Boehringer Ingelheim collaboration — 2022-02-02](https://prtimes.jp/main/html/rd/p/000000031.000048083.html)
- **2021:** [Bayer collaboration — 2021-11-24](https://prtimes.jp/main/html/rd/p/000000026.000048083.html) · [Pfizer collaboration — 2021-10-15](https://prtimes.jp/main/html/rd/p/000000024.000048083.html) · [ユビーリンク launch — 2021-07-27](https://prtimes.jp/main/html/rd/p/000000022.000048083.html) · [1 million monthly users — 2021-06-08](https://prtimes.jp/main/html/rd/p/000000021.000048083.html) · [AI問診ユビー 400 institutions — 2021-05-21](https://prtimes.jp/main/html/rd/p/000000020.000048083.html) · [Takeda collaboration — 2021-04-21](https://prtimes.jp/main/html/rd/p/000000019.000048083.html)
- **2020:** [日本サービス大賞 — 2020-10-27](https://prtimes.jp/main/html/rd/p/000000009.000048083.html) · [Singapore entity, JETRO — 2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html) · [20億円 from スズケン — 2020-06-04](https://prtimes.jp/main/html/rd/p/000000005.000048083.html)

**PR Newswire (EN, Ubie, Inc.)**

- [Self-serve advertising platform — 2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html)
- [Cumulative funding over $125M — 2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)

**Third-party coverage and profiles**

- [国税庁 法人番号公表サイト — 7010701034132 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132)
- [BRIDGE — KVM funding and seed history, 2018-05 (JA)](https://thebridge.jp/2018/05/ubie-jpy300m-funding) · [スズケン 20億円, 2020-06 (JA)](https://thebridge.jp/2020/06/ubie-jpy2b-funding)
- [J-Startup — Ubie (JA)](https://www.j-startup.go.jp/startups/212-ubie.html)
- [Japan Dev — company profile (unverified)](https://japan-dev.com/companies/ubie)
