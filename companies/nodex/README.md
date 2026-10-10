# NodeX

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

NodeX (NodeX株式会社, English name NodeX, Inc.; the brand is also written NODE X and read ノードクロス) is a Tokyo company founded on 2019-05-07 as CollaboGate Japan株式会社 and renamed on 2025-03-04 (corporate number 6011001127965, [国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)). Its product, also called NodeX, gives IoT and edge devices a W3C decentralized identifier (DID): a Rust agent installed on the device handles device authentication, key management and end-to-end encrypted messaging (DIDComm) and sends telemetry to a cloud dashboard, NodeX Studio ([docs](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43), [product page](https://nodex.inc/product); Undated; accessed 2026-10-11). In 2026 the company describes the business as a zero-trust security platform for critical infrastructure and names defense and national security as its first target market ([2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html), [Agent engineer posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B); posting metadata dated 2026-09-29).

- Cumulative funding is ¥830M: a seed round of "累計2.3億円" via J-KISS stock acquisition rights (J-KISS型新株予約権) from 伊藤忠テクノロジーベンチャーズ, DNX Ventures and 株式会社ラック ([2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)), then a ¥600M プレシリーズA from DNX Ventures and ITOCHU Technology Ventures ([2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)).
- The company does not name customers on its own site. Its releases name joint projects with 東芝テック, PFU, NR-Power Lab (NGK and Ricoh joint venture) and MEEQ; in January 2025 it said the Japan Air Self-Defense Force had begun discussing collaboration with it, citing Reuters ([2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html)). BRIDGE reported Toshiba and Mitsubishi Heavy Industries as adopters ([2025-03-21](https://thebridge.jp/2025/03/node-x-a-platform-for-secure-transmission-of-real-world-data-raises-600-million-yen-in-pre-series-a-funding-from-dnx-and-itochu-affiliated-investors)).
- The team is about 20 people by the company's count ("20人ほど", [job postings](https://herp.careers/v1/nodex/K8HNCsT2LA_B), 2026-09-29), which says it is growing from about 20 toward about 50. Other sources give 16, 13 and 11 (see `Notes`).
- Engineering: the agent is written in Rust ([docs](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43)) and the service runs on Google Cloud ([ISMS cloud certification scope](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)). Current postings list TypeScript/React, Rust/Axum/SQLx, GraphQL, PostgreSQL/Bigtable/Redis and GCP/Vercel. The current Agent engineer posting requires native-level Japanese and allows full remote work within Japan, with a monthly in-office All Hands ([posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B); accessed 2026-10-11).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | NodeX; also written NODE X; reading ノードクロス ("NODE X（ノード・クロス）") | [nodex.inc](https://nodex.inc/), [2025-03-19 release](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| Legal name | ＮｏｄｅＸ株式会社 (furigana ノードクロス); English name "NodeX, Inc." given by the company | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965), [company page](https://nodex.inc/company) |
| Corporate number | 6011001127965; designated 2019-05-14 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| Former legal name | ＣｏｌｌａｂｏＧａｔｅ Ｊａｐａｎ株式会社 (コラボゲートジャパン); name change effective 2025-03-04 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| Founded | 2019-05-07 | [company page](https://nodex.inc/company) |
| Registered head office | 東京都渋谷区円山町５番５号Ｎａｖｉ渋谷Ｖ３階 (register record last updated 2025-03-19) | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| Office address given by the company | 〒105-5515 東京都港区虎ノ門1-17-1 虎ノ門ヒルズビジネスタワー 15F; job postings name the office as CIC Tokyo | [company page](https://nodex.inc/company), [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B); accessed 2026-10-11 |
| Representative | 代表取締役CEO 三井 正義 (Masayoshi Mitsui) | [company page](https://nodex.inc/company) |
| Directors listed | 取締役CRO 林 泰成; 取締役CBO 内田 光紀; 社外取締役 小川 剛 (General Partner, 伊藤忠テクノロジーベンチャーズ) | [company page](https://nodex.inc/company); accessed 2026-10-11 |
| Capital | ¥100M "（2026年1月現在）" | [HERP postings](https://herp.careers/v1/nodex/K8HNCsT2LA_B); accessed 2026-10-11 |
| Headcount | "20人ほど"; the company-information block on the same job pages gives 16 | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B), dated 2026-09-29 |
| Working language | No company-wide statement found; the Agent engineer posting requires "ネイティブレベルの日本語コミュニケーション" | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| Total raised | ¥830M cumulative ("累計8.3億円") | [2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| Investors listed by the company | 伊藤忠テクノロジーベンチャーズ, DNXベンチャーズ, LAC | [company page](https://nodex.inc/company) |
| Security certification | ISO/IEC 27001 (JIS Q 27001:2025), registration JP027239; ISMS cloud security (JIP-ISMS517-1.0, ISO/IEC 27017 based), registration 28118935; both first registered 2026-03-30, valid to 2029-03-29, certified by ビューローベリタスジャパン | [ISMS-AC 27001 record](https://isms.jp/lst/ind/CR_JP027239.html), [ISMS-AC cloud record](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html) |
| Other government record | 事業継続力強化計画認定 (中小企業庁), 2025-07-22 | [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965) |

The ISO/IEC 27001 scope reads "IoTシステム向けセキュリティソフトウェアの研究、開発、企画、教育、販売、保守、運用及びアドバイザリー業務". The cloud security scope covers providing NodeX as a cloud service provider "及びGoogleクラウドサービスカスタマとしての利用" ([ISMS-AC](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)).

**Programs, memberships and recognition.** The company joined the Decentralized Identity Foundation (DIF), stating it was the first Japanese startup to do so ([2021-03-10](https://prtimes.jp/main/html/rd/p/000000001.000070282.html)), and the CEO has been DIF Japan Chair since 2022 ([2026-05-12 speaker bio](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)). Other items: Garage+ (Taipei) Startup Global Program Batch 12, 2021-11-01 to 11-05 ([2021-11-16](https://prtimes.jp/main/html/rd/p/000000003.000070282.html)); Renesas Ready Partner for the RA and RX microcontroller families ([2022-06-08](https://prtimes.jp/main/html/rd/p/000000005.000070282.html)); a project with 東芝テック selected for the Digital Agency's "Trusted Web の実現に向けたユースケース実証事業" ([2022-09-13](https://prtimes.jp/main/html/rd/p/000000006.000070282.html)); and BRIDGE's "HOT100 with Accenture Ventures" ([2025-04-30](https://thebridge.jp/2025/04/can-generative-ai-reduce-office-energy-consumption-nodexs-vision-for-a-data-driven-society-with-decentralized-id-hot100-accenture-ventures-vol-6)).

### Identity and legal entities

| Name | Type | Period or status | Relationship | Source |
|---|---|---|---|---|
| CollaboGate Japan株式会社 | Former legal name | 2019-05-07 to 2025-03-04 | Same corporate number as NodeX株式会社 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| NodeX株式会社 / NodeX, Inc. | Current legal name | From 2025-03-04 | — | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965), [company page](https://nodex.inc/company) |
| NODE X / NodeX | Brand | Unified in March 2025: "社名変更を実施、ブランドを「NODE X（ノード・クロス）」に統一" | Product and company name | [2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| UNiD | Former product brand | Used in releases from 2021-03 to 2022-06 | Earlier DID platform and device agent ("UNiD EDGE") from the same company | [2021-03-10](https://prtimes.jp/main/html/rd/p/000000001.000070282.html), [2022-06-08](https://prtimes.jp/main/html/rd/p/000000005.000070282.html), [GitHub `getunid`](https://github.com/getunid) |
| collabogate.com, nodecross.io | Former web domains | Both redirect to `nodex.inc`; `nodecross.io` and `getunid.io` WHOIS name the registrant organization "CollaboGate Japan, Inc." | Business continuity | WHOIS and HTTP checks, 2026-10-11 |
| nodecross.app | Service domain | Hosts the GraphQL API (`api.nodecross.app`) and API references | In current use | [docs](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44) |
| GitHub `nodecross` | Code organization | Display name "NodeX", blog `https://nodex.inc`, location "Japan"; created 2023-01-25 | Company's public code host | [GitHub API](https://api.github.com/orgs/nodecross); read 2026-10-11 |

The legal continuity between CollaboGate Japan and NodeX is established by the register (same corporate number). The CollaboGate name still appears in company infrastructure: the security policy and hiring policy are hosted on `collabogate.notion.site`, HERP job links on the careers page use the path `/v1/collabogate/`, and the 2026-05-12 release lists `contact@collabogate.com` as the press contact ([careers](https://nodex.inc/careers), [2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)).

### Market context as stated by the company

- Edge devices outnumbered mobile devices from 2018 and are forecast to reach 275 billion, 94.5% of all devices, by 2035; building a zero-trust data platform in-house would take "2〜3年の期間と数十億円の初期投資" ([2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)).
- Japan's defense budget has grown to about 2% of GDP ("2026年度 約9兆円"), and the company states that Ministry of Defense procurement notices already include zero-trust device authentication as a requirement ([posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B), 2026-09-29).
- The company frames device, robot and AI-agent identity as "Non-Human Identity（NHI）" ([2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)).

---

## Product

The documentation describes NodeX as "IoTシステムのオブザーバビリティ（可観測性）を確保するためのプラットフォーム": developers integrate NodeX Agent into a device so that its telemetry is collected securely into NodeX Studio in the cloud ([docs](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43); Undated; accessed 2026-10-11). The website presents three components ([product page](https://nodex.inc/product)).

### Components and feature areas

| Component | What it is, per the company | Source |
|---|---|---|
| NodeX Agent | Device middleware for device identification and authentication, provisioning automation, key and certificate lifecycle management, telemetry instrumentation and device-to-device E2EE. The documentation calls it "Rust製ソフトウェア" and lists Ubuntu 20.04/22.04/24.04, Debian 10–12, Yocto Mickledore 4.2, macOS (latest version) and Windows 10. | [product page](https://nodex.inc/product), [docs](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43) |
| NodeX Cloud | Cloud data platform described as handling "数十万台規模のデバイス接続", with a "分散型IDベースのWeb PKI" | [product page](https://nodex.inc/product) |
| NodeX Studio | Device management and monitoring dashboard: real-time metrics, events and logs, alerts, cross-organization device management, three user roles (管理ユーザー, 開発者, オペレーター) and two-factor authentication | [product page](https://nodex.inc/product), [security white paper](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5) |
| Agent local API | Endpoints to look up and resolve DIDs, create and verify DIDComm messages, send events, custom metrics, logs and attributes, run device operations and read device config | [Agent API reference](https://agent-api-ref.nodecross.app/) (v6.2.0) |
| Studio GraphQL API | Data shown in Studio is available over GraphQL at `api.nodecross.app/v1/public/graphql`, authenticated with a JWT signed by an "APIクライアント" secret | [docs](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44), [API reference](https://studio-graphql-api-ref.nodecross.app/) |
| Archive export | Every 5 minutes, collected data is written as gzip-compressed JSONL to the customer's Amazon S3, Azure Storage or Google Cloud Storage; one file per 800 devices | [docs](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4) |

Agent data defaults: metrics are collected every 15 s (configurable 5–300 s) and sent every 60 s (60–3600 s); events are strings up to 255 bytes; logs are strings up to 1 MB that are not viewable in Studio and are only forwarded through the archive function; default retention is 14 days for all four types ([docs](https://docs.nodex.inc/NodeX-Agent-11fd301e9c6580768821fed1c00063b4)).

### How the company has described the product over time

| Date | Company wording | Source |
|---|---|---|
| 2021-03-10 | UNiD, "国内初エンタープライズ対応の分散型IDプラットフォーム", offered to businesses digitizing customer experience; mission "Reimagine Digital Trust" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000001.000070282.html) |
| 2021-11-29 | "EDGE-TO-CLOUD SECURITY PLATFORM「UNiD」"; PFU proof of concept with "UNiD EDGE SDK" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000004.000070282.html) |
| 2022-06-08 | "Zero Trust IoT Security Platform「UNiD」"; device management agent "UNiD EDGE" developed as open source | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000005.000070282.html) |
| 2023-02-15 | "IoTデータセキュリティソリューション「NodeX」" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) |
| 2023-08-09 | "データトラスト基盤「NodeX」" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000008.000070282.html) |
| 2024-03 | The CEO says an observability service for managing IoT devices started in March 2024 | [CEO interview](https://nodex.inc/interview/interview01), 2025-03-11 |
| 2025-03-19 | "エッジ向けゼロトラストデータ基盤" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| 2026-05-12 | "重要インフラ向けゼロトラストセキュリティ基盤「NodeX」事業" | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000014.000070282.html) |
| 2026-09-29 | Defense and national security chosen as "最初の主戦場" among critical-infrastructure sectors | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |

### Commercialization

No public price list was found. The company describes NodeX as delivered "SaaS提供" and says customers can start "ライセンス契約後、わずか1週間" ([nodex.inc](https://nodex.inc/)); use-case pages say agent integration takes about 1–2 weeks after a user licence contract, followed by an expert team helping define service requirements over three to six months ([use case](https://nodex.inc/usecase/usecase01), 2025-03-18). The agent binaries on GitHub may be used only under a separate written agreement, which the licence defines to include license, subscription, evaluation, proof-of-concept and distribution agreements ([LICENSE](https://github.com/nodecross/nodex/blob/main/LICENSE), added 2026-09-18). The security white paper refers to "すべての契約プラン" without listing plans ([white paper](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5)).

### Reported scale over time

| Date | Reported figure or statement | Source |
|---|---|---|
| 2023-02-15 | More than 10 major manufacturers had begun technical evaluation of NodeX | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) |
| 2024-12 | CEO: tie-ups with top-tier Japanese industrial companies; "ようやく初期PMFに至れた" | [CEO interview](https://nodex.inc/interview/interview01), published 2025-03-11 |
| 2025-03-19 | Adopted by "国内トップティアのメーカー" (unnamed) | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| 2025-03-19 | DNX: "複数のエンプラ顧客を獲得" during a seed period of about two and a half years | [DNX Ventures note](https://note.com/dnx_vc/n/n09886e4c33d1) |
| 2026-09-29 | "ミッションクリティカル領域ですでにPMFを確認" | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |

No customer count, device count or revenue figure is published.

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2021-07-06](https://prtimes.jp/main/html/rd/p/000000002.000070282.html) | テセラ・テクノロジー, Renesas | Business alliance with テセラ to build a "分散型IoTプラットフォーム" on Renesas security MCUs |
| [2021-11-29](https://prtimes.jp/main/html/rd/p/000000004.000070282.html) | PFU | Proof of concept embedding UNiD EDGE SDK in PFU document scanners for end-to-end authenticated, encrypted transfer to cloud storage |
| [2022-09-13](https://prtimes.jp/main/html/rd/p/000000006.000070282.html) | 東芝テック | Joint Trusted Web demonstration: tamper-verifiable documents scanned on digital multifunction printers |
| [2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) | 東芝テック, PFU, Intel, Renesas | Joint projects toward product adoption with 東芝テック and PFU; partnerships with Intel and Renesas |
| [2023-08-09](https://prtimes.jp/main/html/rd/p/000000008.000070282.html) | NR-Power Lab (日本ガイシ and リコー joint venture) | Virtual power plant (VPP) system built on NodeX: technical validation in FY2023, field validation planned for FY2024 |
| [2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html) | Japan Air Self-Defense Force | The company states a [Reuters article (2025-01-22)](https://www.reuters.com/business/retail-consumer/japan-hunts-dual-use-goods-makers-aid-military-expansion-2025-01-22/) mentioned the ASDF was communicating with it toward a partnership |
| [2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) | 東芝, リコー, Intel | Funding-release comments from Toshiba's chief digital officer, Ricoh's CTO and an Intel Japan executive officer |
| [2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html) | ミーク (MEEQ) | Solution partnership and proof of concept combining MEEQ SIM and its closed network with NodeX for mobile IoT devices |

Third-party reports of customers: BRIDGE wrote that the platform "すでに東芝や三菱重工など国内大手に採用され" ([2025-03-21](https://thebridge.jp/2025/03/node-x-a-platform-for-secure-transmission-of-real-world-data-raises-600-million-yen-in-pre-series-a-funding-from-dnx-and-itochu-affiliated-investors)); KDDI MUGENLABO Magazine refers to "東芝や三菱重工といった日本を代表する製造業との提携" ([2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)); a BRIDGE event report described the CEO's business as protecting communications of critical infrastructure "防衛省や NTT、電力会社など" ([2025-07](https://thebridge.jp/2025/07/ai-era-collaboration-partners-intention-time-key-ivs2025)). The company's own releases do not name these customers.

### Stated plans

- 2023-02-15: use the seed funding to hire engineers and business development staff globally ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)).
- 2025-03-18: remote control of utility equipment using LLM-optimized settings is "現在、顧客のフィードバックを得ながら開発中" ([use case](https://nodex.inc/usecase/usecase03)).
- 2025-03-19: strengthen the product and delivery teams and prioritize early-customer success; hiring engineers, product managers and business development ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)).
- 2025-05-12: according to the CEO, 2025–26 focuses on "ディープサクセス" for existing customers, followed by global expansion and growth in customer numbers once that is confirmed ([KDDI MUGENLABO](https://mugenlabo-magazine.kddi.com/list/nodex/)).
- 2026-09-29: grow the organization "20名規模から50名規模へ" ([posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B)).

---

## Founder

**三井 正義 (Masayoshi Mitsui)** — founder, 代表取締役CEO ([company page](https://nodex.inc/company), [careers](https://nodex.inc/careers)).

- Born 1989 in Kyoto Prefecture ([週刊BCN, 2025-11-27](https://www.weeklybcn.com/journal/era/detail/20251127_212929.html)).
- Graduated from Keio University's Faculty of Science and Technology and completed graduate school at Keio SFC, researching digital machine tools and autonomous distributed systems ([2026-05-12 speaker bio](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)).
- At the end of his first university year, around 2011, spent six months in New York, then ran an SNS consulting business as a sole proprietor while studying ([CEO interview](https://nodex.inc/interview/interview01), 2025-03-11).
- 2015: founded Bitom, which developed a cloud service for 3D printers; he describes the first company as having failed ([週刊BCN](https://www.weeklybcn.com/journal/era/detail/20251127_212929.html), [CEO interview](https://nodex.inc/interview/interview01)).
- From 2017: ran a research community on distributed ledger technology ([speaker bio](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)).
- Around 2018: began attending DIF and took part in W3C specification work ([CEO interview](https://nodex.inc/interview/interview01), [KDDI MUGENLABO, 2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)).
- 2019-05: founded CollaboGate Japan (now NodeX) ([company page](https://nodex.inc/company)).
- 2022: became DIF Japan Chair ([speaker bio](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)). KDDI MUGENLABO also reports that he took part in a Cabinet Office project on use cases for decentralized identity in Japan (undated in the article; [2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)).
- 2026-04: presented the session "DID-Backed X.509: Linking Decentralized Identity to PKI Certificates" at Internet Identity Workshop #42 with the company's engineering team ([2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)).

### Selected leadership

| Name | Role as written | Stated background | Source |
|---|---|---|---|
| 内田 光紀 | 取締役CBO | Nikon and Wind River, 18 years and more than 6,000 licence and partnership negotiations with device makers; Temple University LL.M. (2006) and MBA (2013); a SCORE committee member (written "JET SCORE" on the interview page, "JST SCORE" in the culture deck); joined as CBO in 2021 | [interview](https://nodex.inc/interview/interview06), 2025-03-04; [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 林 泰成 | 取締役CRO | Account executive at Salesforce Japan; led sales operations at a foreign fintech startup; joined as CRO in 2023 | [interview](https://nodex.inc/interview/interview03), 2025-03-10 |
| 橋本 寛 | シニアデリバリーマネージャー | Kyoto University engineering; 日本総研, PTC, UiPath; joined 2023 | [interview](https://nodex.inc/interview/interview02), 2025-03-10 |
| 川上 和良 | 基盤テックリード | Projection-mapping control systems, FX and arbitrage trading systems, audio AI engines; Rust, C++, Go; joined 2025 | [interview](https://nodex.inc/interview/interview05), 2025-03-10 |
| 松尾 一成 | エージェント・テックリード | Nagoya University mathematics master's; ML pipeline backend, autonomous mobile robot and AGV software; formal verification; Rust at NodeX | [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck), Ver.2025.03.10 |
| 小川 剛 | 社外取締役 | General Partner, 伊藤忠テクノロジーベンチャーズ | [company page](https://nodex.inc/company) |

Advisors listed on the company page: 元橋 一之 (University of Tokyo RCAST; appointed [2023-08-21](https://prtimes.jp/main/html/rd/p/000000009.000070282.html)) and 高橋 大造 (Intel Japan, 執行役員 パートナー事業本部 本部長). The culture deck (Ver.2025.03.10) organizes the company into Growth & Delivery (sales, delivery, marketing), Product & Technology (agent, cloud platform, product) and Corporate & Finance, and its team page lists, beyond the two tech leads, a full-stack engineer and PdM, an SRE engineer, a security engineer and two full-stack engineers.

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| Announced 2023-02-15 | シード (J-KISS型新株予約権) | "累計2.3億円" | 伊藤忠テクノロジーベンチャーズ, DNX Ventures, 株式会社ラック | ¥230M | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) |
| Dated 2025-02-21 in the body; announced 2025-03-19 | プレシリーズA | ¥600M | DNX Ventures, ITOCHU Technology Ventures | ¥830M | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |

ITV's partner states in the 2025 release that ITV "2022年にNODE Xにリードで投資"; DNX states it led the プレシリーズA and that its first investment was made in December 2022 in the seed round ([DNX Ventures note, 2025-03-19](https://note.com/dnx_vc/n/n09886e4c33d1)). ITV and DNX took part in both rounds; 株式会社ラック appears only in the seed release, and LAC is listed among investors on the company page. The プレシリーズA was announced together with the company name change, brand unification and a corporate site renewal ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)). The release states the funds go to product evolution and strengthening the product and delivery teams.

---

## Engineering

### Technology stack and platforms

| Item | Evidence level | Source |
|---|---|---|
| Rust for NodeX Agent | Confirmed by documentation ("Rust製ソフトウェア"); repository topics and release notes also reference Rust tooling | [docs](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43), [releases](https://github.com/nodecross/nodex/releases) |
| Rust for the Studio backend; Axum, SQLx | Company deck bios describe "RustでのStudio開発"; Axum and SQLx are hiring-listed | [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck), [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| DIDs (`did:webvh`), DIDComm, ECDH-1PU+A256KW key agreement with A256GCM, P-384 and Ed25519 keys | Confirmed by the Agent API reference (v6.2.0) and v6.3.1 release notes ("compliance with didwebvh v1.0") | [Agent API reference](https://agent-api-ref.nodecross.app/), [releases](https://github.com/nodecross/nodex/releases) |
| FIPS and non-FIPS agent builds | Confirmed by release assets from v5.0.0 (2025-11-25); the API reference describes the DIDComm encryption as "FIPS 140-3 compliant" | [releases](https://github.com/nodecross/nodex/releases) |
| Agent targets: Linux x86_64 and aarch64 (`.deb` and zip), Windows (MSI), macOS aarch64; a Yocto layer `meta-nodex` (BitBake) | Confirmed by release assets and public repository | [releases](https://github.com/nodecross/nodex/releases), [GitHub `nodecross`](https://github.com/nodecross) |
| Google Cloud | Confirmed: ISMS cloud scope names Google Cloud use; archive docs name a service account in project `nodex-production`; the culture deck lists Cloud Run, GKE, Cloud Bigtable, BigQuery and Cloud Monitoring | [ISMS-AC](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html), [docs](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4), [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| GraphQL (Studio API), JWT | Confirmed by documentation | [docs](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44) |
| Auth0 | Confirmed by the security white paper (password management); also hiring-listed | [white paper](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5) |
| GitHub Actions, Renovate | Deck lists GitHub Actions; release notes mention CI workflows and Renovate | [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck), [releases](https://github.com/nodecross/nodex/releases) |
| TypeScript, React (Next.js in 2025 postings) | Hiring-listed | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B), [archived listing, 2025-02-19](https://web.archive.org/web/20250219084303/https://herp.careers/v1/collabogate) |
| PostgreSQL, Redis, Bigtable | Hiring-listed (Bigtable also in the deck) | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| SendGrid, PagerDuty, Vercel; Figma, GitHub, Notion, Slack, Linear; Claude (Anthropic) | Hiring-listed tools | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| Terraform, Cloud Run | Hiring-listed in a 2025 cloud infrastructure posting | [archived listing, 2025-02-19](https://web.archive.org/web/20250219084303/https://herp.careers/v1/collabogate) |

### Systems

| System | What it does | Source |
|---|---|---|
| Device identity and E2EE messaging | The agent manages each device's DID and keys with a root of trust, automates provisioning, performs mutual authentication and sends DIDComm-encrypted messages; destination DIDs must be authorized, with authorization cached up to 60 s | [README](https://github.com/nodecross/nodex), [Agent API reference](https://agent-api-ref.nodecross.app/) |
| Local agent interface | HTTP on `localhost:3000` on Windows; a Unix domain socket at `~/.nodex/run/nodex.sock` on Unix | [Agent API reference](https://agent-api-ref.nodecross.app/) |
| Telemetry pipeline | Collection and forwarding of metrics, custom metrics, events and logs into Studio, with 14-day default retention | [docs](https://docs.nodex.inc/NodeX-Agent-11fd301e9c6580768821fed1c00063b4) |
| Studio monitoring and alerting | Dashboards, alert conditions, role-based permissions and audit-log archive settings | [docs](https://docs.nodex.inc/10bd301e9c6580b99677d8323218a3fa) |
| Archive export | Scheduled export to customer S3, Azure Storage or GCS buckets | [docs](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4) |
| Mobile IoT over closed networks | PoC with MEEQ: device-level authentication, device-to-server E2E encryption and integrity, and continuous monitoring over MEEQ's closed network | [2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html) |
| DID-backed X.509 | An approach linking DIDs to existing X.509 certificates, presented as a proposal at IIW #42 | [2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html) |

The security white paper for NodeX Studio states: data stored in Japan; AES256 encryption at rest and TLS in transit; daily backups kept for five generations; disaster recovery targets RPO 48 hours and RTO 24 hours; a 99.9% availability target; logical tenant separation; user access logs kept one year; third-party web application and infrastructure vulnerability assessments; and a target of notifying users within three hours of a serious incident ([white paper](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5); Undated; accessed 2026-10-11).

**Code and release history.** The public repository `nodecross/nodex` was created on 2025-04-30 and distributes agent binaries and, until their removal on [2026-01-19](https://github.com/nodecross/nodex/commit/8684127d478fb52d055d204f18c726cede336a19), Python and Node.js examples. It published 44 releases from v1.1.16 (2025-04-30) to v6.3.1 (2026-06-26). Its licence changed from Apache-2.0 to proprietary on [2026-03-19](https://github.com/nodecross/nodex/commit/a0fea2fa7bf0fa21c56c94d1ea2a8b1dfc175544), and the README states "the source code is not published here" ([README](https://github.com/nodecross/nodex); read 2026-10-11). The Agent engineer posting states "NodeXはこれまで外部パートナーと共に開発を進めてきました" and that the role is to lead architecture and technology selection as the product enters full operation ([posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B)).

### Technical background sought

Five postings were open on HERP on 2026-10-11: NodeX Agent engineer, Delivery Engineer, Delivery Manager, an account executive for enterprise, government and defense, and an open business position ([job list](https://herp.careers/v1/nodex)).

- **NodeX Agent engineer** — required: development on Linux; Rust (non-commercial experience accepted); requirements definition, basic design and unit/integration testing; code review; working autonomously while specifications are unsettled. Preferred: choosing and combining cryptographic primitives against a threat model; algorithm selection that accounts for CRYPTREC or FIPS; TLS handshake and record protocol; threat modeling; commercial Rust; Windows development; secure coding; DID and Verifiable Credentials; building from RFCs; post-quantum cryptography or zero-knowledge proofs at a conceptual level; X.509 and PKI; GCP ([posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B)).
- **Delivery Engineer** — required: technical lead roles in customer support, technical support or implementation; reading code and isolating problems; structuring customer requirements at architecture and component level; writing technical documents. Preferred: networking and security basics (TLS, PKI, certificates, DNS); delivery or support for multifunction printers, IoT or security; presales, SE or field engineering; leading PoCs; digital identity, authentication, authorization and encryption ([posting](https://herp.careers/v1/nodex/YOSy7rnYAP1r)).
- **Delivery Manager** — required: leading a multi-organization IT project of six months or more to completion; enough technical literacy to discuss networks, TLS, PKI and certificates with customer engineers. Preferred: projects with prime system integrators; government, defense or quasi-public procurement; regulated industries such as medical, finance, manufacturing OT or energy ([posting](https://herp.careers/v1/nodex/lYSIMVfDShYE)).

### Industry domain

Device identity and zero-trust security for critical infrastructure: defense and national security, medical devices and networks, energy (including VPP), manufacturing equipment such as multifunction printers and scanners, and mobility and transport ([postings](https://herp.careers/v1/nodex), [2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html)). Relevant standards and regimes named in company materials include W3C DIDs and Verifiable Credentials, DIF work, CRYPTREC and FIPS, the Digital Agency's zero-trust architecture policy and Trusted Web, IEC 62443 and NIST SP800 ([2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html), [2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html)). The Delivery Engineer posting states that prior knowledge of DID, DIDComm or zero trust is not required ("事前にこれらを知っている必要はありません"); the Delivery Manager posting likewise does not require prior knowledge of DIDs.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | Agent engineer posting requires native-level Japanese. A 2023 listing included an English-language "Chief of Staff (English ver)" posting. The culture deck lists English learning support. | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B), [archived listing, 2023-03-07](https://web.archive.org/web/20230307164600/https://herp.careers/v1/collabogate), [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| Location and remote | Tokyo office (CIC Tokyo, Toranomon Hills Business Tower 15F) or remote. Agent posting: "国内でのフルリモートOK・全国勤務可", with attendance at the monthly All Hands; all postings require attendance on company-designated days. The account executive role is hybrid. | [Agent posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B), [AE posting](https://herp.careers/v1/nodex/_PTcDQIhGvBX) |
| Working hours | 裁量労働制 for the Agent, Delivery Engineer and Delivery Manager roles; flextime with core hours 10:00–15:00 for the account executive role. The culture deck (Ver.2025.03.10) describes full flextime with no core time and 45 hours of fixed overtime pay included. | [postings](https://herp.careers/v1/nodex), [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| Salary | ¥8,000,000–¥15,000,000 for the Agent, Delivery Engineer, Delivery Manager and AE roles; open business role from ¥8,000,000. The deck shows seven grades (G1–G7) on a chart spanning ¥3M to ¥22M. | [postings](https://herp.careers/v1/nodex), [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| Equity | "長期インセンティブ（ストックオプション）制度" | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| Employment type and probation | Full-time or contract; three-month probation; five days' paid leave granted on joining | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| Benefits | Social insurance (協会けんぽ), childbirth, childcare and nursing-care support, remote work support; the deck adds commuting allowance up to ¥30,000 a month and household-service support | [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B), [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| Evaluation | Grade reviews in January and July; performance against goals plus behaviour against the four values, with peer reference | [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| Hiring process | Document screening, casual interview, usually two interviews, final interview over a meal, offer and HR meeting | [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| Visa sponsorship, new graduates | Not stated in any posting reviewed | [postings](https://herp.careers/v1/nodex) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11): `nodex.inc` pages from its sitemap (home, product, company, careers, use cases, interviews, news, terms, privacy) and `robots.txt`; the Notion-hosted documentation at `docs.nodex.inc`, API references on `nodecross.app`, and the security policy, white paper and hiring policy on `collabogate.notion.site`; PR TIMES releases 1–16 for company ID 70282; the HERP job list and HERP Career profile, plus archived HERP listings from 2023-03 and 2025-02; the 国税庁 法人番号公表サイト, gBizINFO and ISMS-AC registers; GitHub organizations `nodecross`, `getunid`, `collabogate`, `nodexinc` and the names `nodex` and `nodex-inc`; Speaker Deck; probes of Wantedly, TokyoDev, Japan Dev, Zenn, Qiita, note and LinkedIn; WHOIS for related domains; and Japanese and English searches on NodeX, NODE X, ノードクロス, CollaboGate, UNiD and 三井正義.

- **Revenue, customer count and device count.** None published.
- **Pricing.** No price list; contract plans are referenced but not described.
- **Named customers on the company's own site.** The site and releases describe "国内トップティアのメーカー" without names; the names Toshiba and Mitsubishi Heavy Industries come from BRIDGE, not from the company.
- **Valuation.** Not disclosed by the company. HERP Career shows "評価額 18.5 億円", which it labels as estimated from registry filings ([HERP Career](https://herp.careers/careers/companies/nodex); accessed 2026-10-11).
- **Engineering headcount.** Not stated; the culture deck names seven engineering members as of Ver.2025.03.10.
- **Agent source code.** Not public. The `nodecross/nodex` repository holds binaries only; the older Rust repository `nodex-didcomm` is archived and the 2022-era `getunid/unid` repository returns 404.
- **Engineering blog.** No company tech blog was found on Zenn, Qiita, note or the company site. Speaker Deck hosts the CEO's decks, including DIF Japan monthly call talks.
- **Visa sponsorship and English-language roles.** Not stated in current postings.
- **Status page or contractual SLA.** None found; the white paper gives a 99.9% availability target.
- **Patents.** gBizINFO shows 0 patents, designs and trademarks for the corporate number, and no patent is mentioned in company materials ([gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965); accessed 2026-10-11).
- **LAC's own announcement.** No LAC announcement of its seed investment was found.
- **Content of the 2026-08-10 Nikkei item.** The company's news index lists "日本経済新聞 朝刊1面に当社の技術が紹介されました" with a [reprint link](https://webreprint.nikkei.co.jp/r/806F2E1B44594CD380BB054593813E61/), but the reprint is an encrypted PDF that could not be read on 2026-10-11.

### Inconsistencies across sources

- **Head office.** The register lists 東京都渋谷区円山町 (Navi渋谷V 3F) as the head office (record last updated 2025-03-19), and the [2026-03-02 MEEQ release](https://prtimes.jp/main/html/rd/p/000000013.000070282.html) gives 本社 as 東京都渋谷区. The company page, PR TIMES profile, job postings and ISMS records give Toranomon Hills Business Tower 15F ([国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965), [company page](https://nodex.inc/company), [ISMS-AC](https://isms.jp/lst/ind/CR_JP027239.html)).
- **Office postal code.** The company page gives 〒105-5515, which Japan Post assigns to [虎ノ門ヒルズステーションタワー 15F](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1055515); the 2023-08-09 release and the culture deck's company overview give 〒105-6415, Japan Post's code for [虎ノ門ヒルズビジネスタワー 15F](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1056415); job postings and the deck's work-location slide give 〒105-6490. All three accompany the street address 虎ノ門1-17-1 虎ノ門ヒルズビジネスタワー 15階.
- **Headcount.** 20 (culture deck, Ver.2025.03.10); "まだ20名未満の組織" ([interview](https://nodex.inc/interview/interview02), 2025-03-10); 16 (company block on HERP job pages; accessed 2026-10-11); "20人ほど" (posting text, 2026-09-29); 13 insured persons at the Shibuya establishment ([gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965), pension-insurance data, undated); 11 ([HERP Career](https://herp.careers/careers/companies/nodex), pension-insured basis, period to 2026-08). The sources use different measures and dates.
- **Open source.** The website calls NodeX Agent "オープンソースの軽量ミドルウェア" and says binaries and sample code are distributed on GitHub ([product page](https://nodex.inc/product), [nodex.inc](https://nodex.inc/); accessed 2026-10-11). The repository README says the source is not published, the LICENSE states "It is NOT an open source license", and the examples were removed on 2026-01-19 ([README](https://github.com/nodecross/nodex), [LICENSE](https://github.com/nodecross/nodex/blob/main/LICENSE)).
- **Round name.** The company calls the 2025 round プレシリーズA; in the same release ITV's partner refers to "今回のシリーズAラウンド", and a BRIDGE article describes "総額6億円のシリーズAラウンド" ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html), [BRIDGE, 2025-04-30](https://thebridge.jp/2025/04/can-generative-ai-reduce-office-energy-consumption-nodexs-vision-for-a-data-driven-society-with-decentralized-id-hot100-accenture-ventures-vol-6)).
- **Seed round timing.** The seed was announced on 2023-02-15. ITV says it invested in 2022 and DNX says its first investment was in December 2022; the DNX interviewer on the company's site refers to "2022年には2.3億円のシード資金調達", while the senior delivery manager's interview says "2023年に累計2.3億円" ([DNX note](https://note.com/dnx_vc/n/n09886e4c33d1), [interview01](https://nodex.inc/interview/interview01), [interview02](https://nodex.inc/interview/interview02)).
- **Start of standards work.** The 2023 seed release says the company joined W3C and DIF "2019年から"; the CEO says he began attending DIF around 2018 and joined in 2019; KDDI MUGENLABO says he took part in W3C specification work from 2018; the 2026 postings say founding members have been in W3C and DIF "2017年から" ([2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html), [interview01](https://nodex.inc/interview/interview01), [MUGENLABO](https://mugenlabo-magazine.kddi.com/list/nodex/), [posting](https://herp.careers/v1/nodex/K8HNCsT2LA_B)).
- **Supported platforms.** The README lists "Linux kernel x86(32bit) & x86-64(64bit), FreeRTOS ARM Cortex-M33(32bit)"; the documentation lists Ubuntu, Debian, Yocto, macOS and Windows 10; release assets contain x86_64 and aarch64 Linux, Windows and macOS aarch64 builds and no FreeRTOS build ([README](https://github.com/nodecross/nodex), [docs](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43), [releases](https://github.com/nodecross/nodex/releases)).
- **Cost of in-house development.** The homepage says an in-house secure data platform costs "数億円"; the 2025-03-19 release says "数十億円の初期投資" ([nodex.inc](https://nodex.inc/), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)).
- **Tech lead's name.** 川上 和良 on the company page and interview, 川上 和義 in the culture deck ([company page](https://nodex.inc/company), [culture deck](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)).
- **Product release date.** The CEO dates the NodeX release to "2023年8月"; the 2023-02-15 release already presents NodeX as the company's solution ([2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html), [2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)).

### Other

- **Name collisions.** The GitHub organization `nodexinc` exists (created 2022-02-13, no repositories, no profile metadata), with no link to this company found ([GitHub API](https://api.github.com/orgs/nodexinc)); `github.com/Nodex` is an unrelated user account from 2011. The domain `nodex.io`, used as the contact link in the [2026-03-02 release](https://prtimes.jp/main/html/rd/p/000000013.000070282.html), is privacy-registered through a US registrar and did not resolve on 2026-10-11; the company's own domains are `nodex.inc` and `nodecross.app`. Other unrelated projects named NodeX appear in package and freelance directories. Facts on this page are tied to `nodex.inc`, the CollaboGate name or ノードクロス.
- **Positioning shift.** The company's descriptions moved from a DID platform for customer experience (2021) to IoT data security for manufacturers (2023), an edge zero-trust data platform (2025) and critical-infrastructure security with defense first (2026); see `How the company has described the product over time`.
- **Media items on the company's news index** include a front-page Nikkei morning edition item on 2026-08-10 and a contributed article in the radiology journal RadFan (July 2026) on "既存医療ネットワークにおけるサイバーセキュリティと医療機器保護" ([news](https://nodex.inc/news), [RadFan](https://note.com/medical_radfan/n/ne1191dd62d19)).
- **The CEO describes a change in sales approach in 2024.** He says that from around January 2024 the company switched to presenting NodeX as a direct solution to each customer's pain, after a first year in which the product "なぜか刺さらない" ([interview01](https://nodex.inc/interview/interview01), 2025-03-11).
- **PR TIMES release 12 for this company returns 404**, and the company's news index carries the MEEQ release under 2026-03-03 while PR TIMES dates it 2026-03-02 09:00.

---

## Resources

**Official**

- [Corporate site](https://nodex.inc/) · [Product](https://nodex.inc/product) · [Company](https://nodex.inc/company) · [Careers](https://nodex.inc/careers) · [Use cases](https://nodex.inc/usecase) · [News](https://nodex.inc/news) · [Terms](https://nodex.inc/legal/terms)
- Use cases — [Product as a service (2025-03-18)](https://nodex.inc/usecase/usecase01) · [Utility equipment energy saving (2025-03-18)](https://nodex.inc/usecase/usecase03)
- Interviews — [CEO, 2025-03-11](https://nodex.inc/interview/interview01) · [Senior delivery manager, 2025-03-10](https://nodex.inc/interview/interview02) · [CRO, 2025-03-10](https://nodex.inc/interview/interview03) · [Tech lead, 2025-03-10](https://nodex.inc/interview/interview05) · [CBO, 2025-03-04](https://nodex.inc/interview/interview06)
- Documentation — [NodeX ご利用ガイド](https://docs.nodex.inc/manual) · [はじめに](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43) · [詳細仕様](https://docs.nodex.inc/10bd301e9c6580b99677d8323218a3fa) · [Agent collection intervals](https://docs.nodex.inc/NodeX-Agent-11fd301e9c6580768821fed1c00063b4) · [GraphQL API](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44) · [Archive settings](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4)
- API references — [Agent API](https://agent-api-ref.nodecross.app/) · [Studio GraphQL API](https://studio-graphql-api-ref.nodecross.app/)
- Security — [Security policy](https://collabogate.notion.site/NodeX-2edd301e9c658012afbff5f98688ba33) · [Security white paper](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5)
- GitHub — [`nodecross`](https://github.com/nodecross) · [`nodecross/nodex`](https://github.com/nodecross/nodex) · [Releases](https://github.com/nodecross/nodex/releases) · [LICENSE](https://github.com/nodecross/nodex/blob/main/LICENSE) · [licence change commit](https://github.com/nodecross/nodex/commit/a0fea2fa7bf0fa21c56c94d1ea2a8b1dfc175544) · [examples removal commit](https://github.com/nodecross/nodex/commit/8684127d478fb52d055d204f18c726cede336a19) · [org API record](https://api.github.com/orgs/nodecross) · [`getunid`](https://github.com/getunid)
- Jobs — [HERP job list](https://herp.careers/v1/nodex) · [NodeX Agent engineer](https://herp.careers/v1/nodex/K8HNCsT2LA_B) · [Delivery Engineer](https://herp.careers/v1/nodex/YOSy7rnYAP1r) · [Delivery Manager](https://herp.careers/v1/nodex/lYSIMVfDShYE) · [Account executive](https://herp.careers/v1/nodex/_PTcDQIhGvBX)
- [Culture deck, Ver.2025.03.10 (Speaker Deck)](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)

**Press releases (PR TIMES, JA — newest first)**

- [IIW #42 report event — 2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)
- [MEEQ solution partnership — 2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html)
- [プレシリーズA, cumulative ¥830M, rename — 2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)
- [Reuters mention of ASDF partnership preparation — 2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html)
- [Advisor 元橋一之 — 2023-08-21](https://prtimes.jp/main/html/rd/p/000000009.000070282.html)
- [NR-Power Lab VPP — 2023-08-09](https://prtimes.jp/main/html/rd/p/000000008.000070282.html)
- [Seed, ¥230M via J-KISS — 2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)
- [Digital Agency Trusted Web selection — 2022-09-13](https://prtimes.jp/main/html/rd/p/000000006.000070282.html)
- [Renesas Ready Partner — 2022-06-08](https://prtimes.jp/main/html/rd/p/000000005.000070282.html)
- [PFU proof of concept — 2021-11-29](https://prtimes.jp/main/html/rd/p/000000004.000070282.html)
- [Garage+ Batch 12 — 2021-11-16](https://prtimes.jp/main/html/rd/p/000000003.000070282.html)
- [Distributed IoT platform demonstration — 2021-07-06](https://prtimes.jp/main/html/rd/p/000000002.000070282.html)
- [UNiD partner programme — 2021-03-10](https://prtimes.jp/main/html/rd/p/000000001.000070282.html)

**Registers**

- [国税庁 法人番号公表サイト — 6011001127965](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)
- [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965)
- [ISMS-AC — ISO/IEC 27001 JP027239](https://isms.jp/lst/ind/CR_JP027239.html) · [ISMS-AC — cloud security 28118935](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)
- Japan Post postal codes — [105-5515](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1055515) · [105-6415](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1056415)

**Third-party coverage and profiles**

- [DNX Ventures — 追加投資 (JA), 2025-03-19](https://note.com/dnx_vc/n/n09886e4c33d1)
- [BRIDGE — プレシリーズA (JA), 2025-03-21](https://thebridge.jp/2025/03/node-x-a-platform-for-secure-transmission-of-real-world-data-raises-600-million-yen-in-pre-series-a-funding-from-dnx-and-itochu-affiliated-investors) · [HOT100 with Accenture Ventures (JA), 2025-04-30](https://thebridge.jp/2025/04/can-generative-ai-reduce-office-energy-consumption-nodexs-vision-for-a-data-driven-society-with-decentralized-id-hot100-accenture-ventures-vol-6) · [IVS2025 session (JA), 2025-07](https://thebridge.jp/2025/07/ai-era-collaboration-partners-intention-time-key-ivs2025)
- [KDDI MUGENLABO Magazine — CEO interview (JA), 2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)
- [週刊BCN — CEO profile (JA), 2025-11-27](https://www.weeklybcn.com/journal/era/detail/20251127_212929.html)
- [Reuters — Japan hunts dual-use goods makers to aid military expansion, 2025-01-22](https://www.reuters.com/business/retail-consumer/japan-hunts-dual-use-goods-makers-aid-military-expansion-2025-01-22/)
- [Nikkei reprint, 2026-08-10 (JA, encrypted PDF)](https://webreprint.nikkei.co.jp/r/806F2E1B44594CD380BB054593813E61/) · [RadFan contribution (JA)](https://note.com/medical_radfan/n/ne1191dd62d19)
- [HERP Career — company profile (JA)](https://herp.careers/careers/companies/nodex)
- Archived HERP listings — [2023-03-07](https://web.archive.org/web/20230307164600/https://herp.careers/v1/collabogate) · [2025-02-19](https://web.archive.org/web/20250219084303/https://herp.careers/v1/collabogate)
- [GitHub API — `nodexinc` (name match; no link to the company found)](https://api.github.com/orgs/nodexinc)
