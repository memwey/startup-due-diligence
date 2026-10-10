# Nature

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-10-11.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Nature (Nature株式会社 / Nature Inc., corporate number 4130001055679) is a Yokohama-based hardware and energy-management company. Its official company page gives 2014-12-10 as the founding date; the CEO says the company was first registered in the United States in December 2014 while he was at Harvard Business School, and the Japanese legal entity was called Nature Japan株式会社 until 2019-08-07. It sells the **Nature Remo** smart infrared remote, the **Nature Remo E** home energy management system (HEMS, called スマホHEMS by the company), the **Nature EV Switch** EV-charging controller and the **Nature Lock** smart lock, all used through the "Nature Home" app. It also sells a demand-response (DR) support service to electricity retailers and a cloud API.

- Scale: "累計販売台数80万台を超える" (over 800,000 cumulative units) for the Nature Remo series ([2026-10-01 release](https://nature.global/press/release/28318/)); a backend posting states that over 450,000 IoT devices are connected to the Nature Remo cloud ([Backend Engineer posting](https://herp.careers/v1/nature/F06a8ZG7ncFG), datePosted 2025-05-16; accessed 2026-10-11).
- Funding: latest announced round is a **シリーズD** totalling approx. 12.2億円 (10.2億円 closed in February 2024 plus an undisclosed additional amount from 脱炭素化支援機構, announced [2024-06-27](https://nature.global/press/release/20904/)). BRIDGE put publicly disclosed funding since founding at over 25億円 ([BRIDGE, 2024-06-28](https://thebridge.jp/2024/06/nature-series-d2-round-funding)). The statutory financial notice for the year ended 2026-03-31 reports a net loss of 1億9561万円 ([官報決算データベース](https://catr.jp/companies/9dfc0/74413)).
- Team: 56 people including contractors and interns ([company page](https://nature.global/about/); Undated; accessed 2026-10-11); the company deck gives 45 employees, with software engineers at 38% of full-time roles ([company deck](https://speakerdeck.com/naturepr/company-information), modified 2026-05-31).
- Engineering: Go backend on AWS (ECS, Aurora MySQL, ElastiCache Redis, DynamoDB), React Native/TypeScript app, C/C++ firmware on ESP32/ESP-IDF with Rust named in postings; devices talk Wi-Fi, BLE, Wi-SUN, LTE-M, Matter and ECHONET Lite ([engineering blog, 2021-04-29](https://engineering.nature.global/entry/start-blog), [Firmware Engineer posting](https://herp.careers/v1/nature/km0uZc0P_FSl), datePosted 2026-09-18). Postings are in Japanese and the Backend Engineer posting requires native-level Japanese; engineering roles allow full remote work with about one company-wide office day per month ([posting](https://herp.careers/v1/nature/F06a8ZG7ncFG); accessed 2026-10-11).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Current public brand | Nature (product brands Nature Remo, Nature Remo E, Nature EV Switch, Nature Lock / Nature Key, Nature Green; app "Nature Home") | [nature.global](https://nature.global/); accessed 2026-10-11 |
| Legal name | Nature株式会社 (Nature Inc.); フリガナ ネイチャー; corporate number 4130001055679 | [company page](https://nature.global/about/), [NTA 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) (information as of 2026-10-11) |
| Former legal name | Nature Japan株式会社 (ネイチャージャパン), changed to Nature株式会社 on 2019-08-07 | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) |
| Founded | "設立：2014年12月10日" | [company page](https://nature.global/about/); Undated; accessed 2026-10-11 |
| HQ | 〒221-0052 神奈川県横浜市神奈川区栄町1-1 KDX横浜ビル 11F (registered address 栄町1番地1 since 2021-12-20) | [company page](https://nature.global/about/), [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) |
| Lab / retreat | 〒259-0304 神奈川県足柄下郡湯河原町宮下698-15 "Smart Energy Lab" | [company page](https://nature.global/about/) |
| Representative | 代表取締役 塩出 晴海 (Haruumi Shiode) | [company page](https://nature.global/about/) |
| Business as registered on the company page | "IoT機器の開発・製造・販売、及びエネルギーマネジメント事業" | [company page](https://nature.global/about/) |
| Headcount | "56名（業務委託、インターン含む）" | [company page](https://nature.global/about/); Undated; accessed 2026-10-11 |
| Capital | "25.8億円（資本剰余金含む）" | [HERP company box](https://herp.careers/v1/nature/F06a8ZG7ncFG), [company deck](https://speakerdeck.com/naturepr/company-information) (modified 2026-05-31) |
| Units | Nature Remo series: over 800,000 cumulative units sold | [2026-10-01 release](https://nature.global/press/release/28318/) |
| Total raised | Over 25億円 publicly disclosed since founding (media figure); see `Funding` | [BRIDGE, 2024-06-28](https://thebridge.jp/2024/06/nature-series-d2-round-funding) |
| Shareholders named by the company | 環境エネルギー投資, 脱炭素化支援機構 (JICN), KDDI Green Partners Fund, 東京ガス, ENEOS, Daikin, Delight Ventures (DeNA), MUFJ Capital, 博報堂DYV "他" | [company deck](https://speakerdeck.com/naturepr/company-information) (modified 2026-05-31) |
| Security certification | ISO/IEC 27001:2022, certificate no. 16297, Intertek Certification, registered 2026-02-20; scope HQ and Smart Energy Lab | [2026-03-09 release](https://nature.global/press/release/26121/) |
| Product security labels | JC-STAR ★1 for Nature Remo E / E lite / E2 / E2 lite (announced 2025-10-10) and for Nature EV Switch | [2025-10-10 release](https://nature.global/press/release/25287/), [2025-10-31 release](https://nature.global/press/release/25360/) |
| Energy registrations | Registered as a 東京都家庭用アグリゲーター (Tokyo household aggregator) on 2026-08-06 | [2026-08-24 release](https://nature.global/press/release/27984/) |

### Identity and legal entities

| Name | Type | Jurisdiction / period | Relationship as stated in sources | Source |
|---|---|---|---|---|
| Nature株式会社 (Nature Inc.) | Current legal entity | Japan; corporate number 4130001055679 | Operating company named in all current releases, terms and the API documentation | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679), [terms](https://terms.nature.global/ja/) |
| Nature Japan株式会社 | Former legal name of the same entity | Japan; until 2019-08-07 | Same corporate number; registered addresses moved 京都市左京区 → 東京都渋谷区桜丘町 (2017-12-15) → 渋谷区広尾 (2018-08-23) → 渋谷区宇田川町 (2020-03-27) → 横浜市神奈川区 (2021-12-20) | [NTA](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) |
| US company ("Nature, Inc.") | Predecessor or related entity; legal relationship not stated | United States; registered December 2014 per the CEO | CEO: "2014年12月、アメリカで会社を登記し、Natureは誕生しました". The 2019 funding release states that head-office functions were moved entirely to Japan and the business would restart "Nature 株式会社として" | [CEO interview, 2025-12-04 (JA)](https://note.com/nature_global/n/n3a9457ec0239), [2019-08-01 release](https://nature.global/press/release/566/) |

No source reviewed states whether the US company was merged, dissolved, or remains a parent or subsidiary of the Japanese entity, or the date on which Nature Japan株式会社 was incorporated.

**Programs, registrations and awards**: selected for 500 KOBE ACCELERATOR ([2017-08-14](https://nature.global/press/news/1312/)) and Google for Startups Accelerator Class 3 ([2021-01-07](https://nature.global/press/release/3816/)); participated with Kansai Electric in the 平成29年度 virtual power plant demonstration ([2017-07-25](https://nature.global/press/news/513/)). iF Design Award 2020 for Nature Remo E ([2020-02-05](https://nature.global/press/news/1426/)) and 2021 for Remo 3, Remo mini 2 and Remo E lite ([2021-04-15](https://nature.global/press/release/5025/)); グッドデザイン賞 2024 for Nature Remo Lapis ([2024-10-16](https://nature.global/press/release/22036/)); named in Forbes JAPAN's "次世代GX企業50選" energy-management category ([2025-08-14](https://nature.global/press/news/24875/)). Retail electricity: the Electricity and Gas Market Surveillance Commission (電力・ガス取引監視等委員会) answered on 2020-11-04 that it had no objection to registering Nature株式会社 as a 小売電気事業を営もうとする者 ([reply](https://www.egc.meti.go.jp/info/public/pdf/20201104001b.pdf), [applicant list](https://www.egc.meti.go.jp/info/public/pdf/20201104001c.pdf)); see `Notes`.

### Market context as stated by the company

- The Series D release cites the government target of a renewable share above 50% of the power mix for 2050 carbon neutrality, and frames the need as raising self-consumption for users and flexible demand for grid operators ([2024-02-07](https://nature.global/press/release/18339/), [2024-06-27](https://nature.global/press/release/20904/)).
- Current postings cite GX policy and the development of the 需給調整市場 (balancing market) as "制度の追い風" (institutional tailwinds) ([Backend Engineer posting](https://herp.careers/v1/nature/F06a8ZG7ncFG)).
- The company attributes the 2022 exit from electricity retail to JEPX procurement price spikes (LNG shortage, the war in Ukraine, an earthquake) ([2022-04-11](https://nature.global/press/release/8397/)).
- ERAB Cybersecurity Guidelines Ver3.0 (revised 2025-05-22) made JC-STAR ★1 or higher mandatory for IoT devices used as ERAB control targets, which the company cites for its labels ([2025-10-10](https://nature.global/press/release/25287/)).

---

## Product

The site navigation groups products into ホームオートメーション (home automation) and エネルギーマネジメント (energy management), with a separate 法人のお客様 (business) section ([nature.global](https://nature.global/); accessed 2026-10-11).

### Product line-up

| Product | Area | What it is | Launch / key dates |
|---|---|---|---|
| Nature Remo series (Lapis, Remo 3, Remo mini 2, Remo nano) | Home automation | Wi-Fi smart infrared remote; Remo 3 has temperature, humidity, illuminance and motion sensors; Remo nano supports Matter; Lapis adds automatic air-conditioner power saving ("オートエコ") | First Remo on sale [2017-10-16](https://nature.global/press/release/522/); Remo 3 [2020-08-05](https://nature.global/press/release/606/); nano [2023-07-04](https://nature.global/press/release/15936/); Lapis [2024-07-05](https://nature.global/press/release/21289/) |
| Nature Lock / Nature Key | Home automation | Smart lock with a key fob supporting hands-free unlock and Apple "Find My"; hardware and base firmware provided by Sony Network Communications' Qrio Lock design, developed and manufactured in Japan | Announced [2026-04-21](https://nature.global/press/release/26546/); general sale [2026-04-30](https://nature.global/press/release/26672/) |
| Nature Remo E2 / E2 lite (and earlier Remo E / E lite) | Energy management | Plug-in HEMS reading the smart meter over Wi-SUN B-route and controlling ECHONET Lite equipment (solar, batteries, V2H, EcoCute, Ene-Farm, air conditioners); "lite" models monitor only | Remo E preorders [2019-12-10](https://nature.global/press/release/578/); E lite [2020-04-28](https://nature.global/press/release/589/); E2 [2025-04-08](https://nature.global/press/release/24003/) |
| Nature EV Switch | Energy management | LTE-M connected controller for 200V EV-charging outlets: monitoring, remote start/stop, timers, weather-linked and surplus-solar charging | Panasonic service from 2025 ([2025-02-25](https://nature.global/press/release/23308/)); corporate sales [2025-10-31](https://nature.global/press/release/25360/); individual sales and installation service [2026-03-10](https://nature.global/press/release/26117/) |
| Nature Green | Energy management (software) | App automations: JEPX price-linked air-conditioner and battery control, EcoCute heating by weather forecast, V2H timer, "スマートEV充電 for Tesla" | First paid option [2023-08-08](https://nature.global/press/release/16586/); Tesla option [2026-09-24](https://nature.global/press/release/28217/) |
| デマンドレスポンス支援サービス | Business (electricity retailers) | DR operations for retailers: behaviour-change DR and device-control DR (air conditioners, EcoCute, batteries), admin console, JEPX-linked triggering, result reports | First used by Kansai Electric in summer 2022 ([2022-06-28](https://nature.global/press/release/9771/)); renewed [2025-07-01](https://nature.global/press/release/24645/) |
| Nature API | Business / developers | Cloud API, Local API, Remo E ECHONET Lite API, OAuth2/OpenID Connect provider | Remo API published [2018-02-01](https://nature.global/press/news/1361/); paid corporate Remo E API [2021-01-05](https://nature.global/press/release/3811/) |

Discontinued: **Natureスマート電気**, a retail electricity service with prices that varied with supply and demand, launched in the TEPCO and Kansai areas on [2021-03-01](https://nature.global/press/release/4320/), expanded nationally (except Okinawa and remote islands) by [2021-07-06](https://nature.global/press/release/5591/), and stopped supplying power on 2022-06-30 ([2022-04-11](https://nature.global/press/release/8397/)).

### Commercialization

- **Hardware** is sold through the company's Shopify store, Amazon.co.jp, Rakuten and electronics retailers, with published list prices and volume pricing on request for businesses ([business page](https://nature.global/business/); accessed 2026-10-11). Since 2026-10-01, Remo purchases on the official store, Rakuten and Amazon carry a refund guarantee if basic air-conditioner operation cannot be made to work ([2026-10-01](https://nature.global/press/release/28318/)).
- **Nature Green** options are a mix of free and monthly paid options listed with prices on the [Nature Green page](https://shop.nature.global/pages/nature-green) (accessed 2026-10-11).
- **B2B**: the DR support service and commercial use of the Nature API are sold on enquiry; no price is published ([API page](https://nature.global/business/api-remo/)). The developer portal permits corporations to use the API "商用利用前の検証段階に限り" (only at the pre-commercial validation stage), with commercial use handled by enquiry ([developer portal](https://developer.nature.global/)). The EV Switch is also supplied as a module (EVSW-6B1-P) for Panasonic's "おうちEV充電サービス" ([2026-03-10](https://nature.global/press/release/26117/)).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2016-06-03 | Kickstarter: US$50,000 raised in 10 days | [release](https://nature.global/press/release/456/) |
| 2018-02-19 | Kickstarter, Makuake and Indiegogo together raised "総額2000万円以上" | [release](https://nature.global/press/release/524/) |
| 2019-08-01 | Nature Remo series: 100,000 cumulative units | [release](https://nature.global/press/release/566/) |
| 2020-09-16 | Remo and Remo E series combined: 200,000 cumulative units; NPS 30 in a user survey | [release](https://nature.global/press/release/615/) |
| 2021-04-15 | Remo and Remo E series combined: 300,000 units | [release](https://nature.global/press/release/5025/) |
| 2022-04-11 | Nature Remo: over 400,000 units | [release](https://nature.global/press/release/8397/) |
| 2023-07-04 | Nature Remo: 600,000 units | [release](https://nature.global/press/release/15936/) |
| 2024-06-27 | Nature Remo: over 650,000 units | [release](https://nature.global/press/release/20904/) |
| 2026-05-31 (deck modified) | Remo and Remo E series combined: "800,000台突破"; Nature Home app used by "数十万人" | [company deck](https://speakerdeck.com/naturepr/company-information) |
| 2026-10-01 | Nature Remo: over 800,000 units | [release](https://nature.global/press/release/28318/) |

### Announced customers and partners

| Date | Party | What was announced |
|---|---|---|
| [2022-06-28](https://nature.global/press/release/9771/) | 関西電力 | First DR support service customer (summer 2022); adopted again in later seasons and year-round from [2024-06-25](https://nature.global/press/news/20713/) |
| [2022-12-23](https://nature.global/press/release/12753/) | NTTドコモ | DR collaboration; Nature's automatic power-saving used in "ドコモでんき自動エコモード" ([2024-03-04](https://nature.global/press/release/18635/)) |
| [2023-02-13](https://nature.global/press/release/13793/) | オクトパスエナジー | DR support service |
| [2024-04-18](https://nature.global/press/release/19564/) | 東京ガス | Business alliance on DR using household DER; DR support service provided from [2025-04-01](https://nature.global/press/release/23974/) |
| [2024-06-26](https://nature.global/press/release/20279/) | auエネルギー＆ライフ | "スマート節電 with Nature Green" |
| [2024-10-30](https://nature.global/press/release/22262/) | Shizen Connect | Cloud-to-cloud VPP control of Nature Remo E households |
| [2025-02-25](https://nature.global/press/release/23308/) | パナソニック エレクトリックワークス社 | Nature EV Switch module in "おうちEV充電サービス" |
| [2025-09-04](https://nature.global/press/release/25064/) | 東京ガス, 三菱自動車 | Remote EV-charging demonstration under a Tokyo Metropolitan Government program |
| [2025-12-25](https://nature.global/press/release/25801/) | 世田谷区 | Results of a July–August 2025 energy-saving demonstration (2.52% consumption reduction) |
| [2026-04-21](https://nature.global/press/release/26546/) | ソニーネットワークコミュニケーションズ | Qrio Lock design and technology provided for Nature Lock |

### Stated plans

- Series D use of funds: build the "Nature DER Platform" to control distributed energy resources, grow through partner companies (including investors), and hire ([2024-02-07](https://nature.global/press/release/18339/), [2024-06-27](https://nature.global/press/release/20904/)).
- Medium-term vision stated with the Nature Lock launch: "統合的なスマートホームの体験を提供し、快適でサステナブルな暮らしを実現する" ([2026-04-21](https://nature.global/press/release/26546/)).
- The company deck's roadmap shows a "Nature V2H" and "Nature蓄電池" toward 2030, marked "想定のものであり、今後変更の可能性があります" (assumed, subject to change) ([company deck](https://speakerdeck.com/naturepr/company-information)).
- The Backend Engineer posting expects connected devices to pass 1,000,000 "数年で" (within a few years) ([posting](https://herp.careers/v1/nature/F06a8ZG7ncFG)); the labour/general-affairs posting states the company is building internal systems "数年後のIPOを見据えて" (with an IPO in a few years in view) ([posting](https://herp.careers/v1/nature/A6An3g_K1bIS), datePosted 2025-11-26).

---

## Founder

**塩出 晴海 (Haruumi Shiode)** — founder, 代表取締役 CEO ([company page](https://nature.global/about/), [team page](https://nature.global/careers/team/)).

- Studied at Hokkaido University's engineering faculty, with an exchange at the University of Wisconsin–Madison; completed a Computer Science master's at KTH Royal Institute of Technology in 2008 ([CEO interview (JA)](https://note.com/nature_global/n/n3a9457ec0239), [team page](https://nature.global/careers/team/)).
- Mitsui & Co.: power-business investment and development in developing countries, including an Indonesian coal-fired power project ([team page](https://nature.global/careers/team/), [CEO interview (JA)](https://note.com/nature_global/n/n3a9457ec0239)).
- Harvard Business School MBA, completed 2016; founded Nature while at Harvard, registering a company in the US in December 2014 ([team page](https://nature.global/careers/team/), [CEO interview (JA)](https://note.com/nature_global/n/n3a9457ec0239)).
- Longer interviews: [立志編 (JA), 2025-12-04](https://note.com/nature_global/n/n3a9457ec0239), [組織・カルチャー編 (JA), 2025-12-04](https://note.com/nature_global/n/nb47e66f7c43d).

**大塚 雅和 (Masakazu Ohtsuka)** — co-founder; listed as "Co-founder and CTO" in the [company deck](https://speakerdeck.com/naturepr/company-information) (modified 2026-05-31).

- Panasonic from 2000 (car-navigation firmware), Kayac from 2007, independent from 2013; built and sold the IRKit learning remote, then developed the first Nature Remo ([interview, 2022-08-18 (JA)](https://note.com/nature_global/n/n6c8b703cdc85), [team page](https://nature.global/careers/team/)).
- Left Nature to work in Estonia after the Remo launch and returned in 2022 after about four years ([interview, 2022-08-18 (JA)](https://note.com/nature_global/n/n6c8b703cdc85)); wrote "7月からCTOに復帰しました" on [2023-07-19](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown). The team page states he lives in Estonia.

### Selected leadership

| Name | Role as written | Background as stated | Source |
|---|---|---|---|
| Tomomi Nagao (長尾) | Designer; creative direction | Kyocera (phones, IoT products); joined 2018 and involved in product design "創業時より"; the CEO names 長尾 as the early industrial designer | [team page](https://nature.global/careers/team/), [CEO interview (JA)](https://note.com/nature_global/n/n3a9457ec0239) |
| Ryo Takei | Corporate Lead | CPA; audit at Deloitte Tohmatsu; finance head and IPO-preparation lead at a SaaS company; joined 2025-02 | [team page](https://nature.global/careers/team/) |
| Shikhar Ghosh | Advisor | Not stated | [team page](https://nature.global/careers/team/) |

Names in this table are given as the romaji team page writes them. Technical advisors appointed [2019-11-17](https://nature.global/press/release/575/): 川崎 修平 (former DeNA director and CTO) and [阿部 力也](https://nature.global/press/release/572/) (Digital Grid Consortium); 宇野 雄 (Cookpad) became design advisor with the [2021-07-14](https://nature.global/press/release/5754/) round. The engineering blog's first post (2021-04-29) was written by "Songmu", described as VPoE ([post](https://engineering.nature.global/entry/start-blog)); Songmu is not listed on the current team page.

The team page lists software engineers working on firmware, mobile, server and SRE, plus hardware engineering, design, customer support, business development, HR, marketing/data analysis, product marketing and corporate roles ([team page](https://nature.global/careers/team/); accessed 2026-10-11). In December 2025 the company moved from four years of holacracy to a "Hybrid型組織", placing managers in functional circles while project circles stay holacratic ([HR note, 2025-12-19 (JA)](https://note.com/nature_global/n/n26cb9d5921ec)).

---

## Funding

| Date | Round (company's wording) | Amount | Investors | Cumulative | Source |
|---|---|---|---|---|---|
| 2018-02-19 | 第三者割当増資 | 1億円 | 大和企業投資 | — | [release](https://nature.global/press/release/524/) |
| 2019-08-01 (closed 2019-07-31) | 第三者割当増資 | 5億円 | 環境エネルギー投資, ディー・エヌ・エー (to be transferred to Delight Ventures) | — | [release](https://nature.global/press/release/566/) |
| 2021-07-14 | 第三者割当増資 | 7.5億円 | 環境エネルギー投資, 大和企業投資 | — | [release](https://nature.global/press/release/5754/) |
| 2024-02-07 | 第三者割当増資; later described as シリーズDラウンド | 約10.2億円 | 東京ガス, EEI4号イノベーション&インパクト投資事業有限責任組合 (環境エネルギー投資), KDDI Green Partners Fund (SBIインベストメント), ダイキン工業, ENEOSイノベーションパートナーズ, HAKUHODO DY FUTURE DESIGN FUND 2号 (博報堂DYベンチャーズ), 三菱UFJキャピタル9号, Yokohama Next 投資事業有限責任組合 (横浜キャピタル) | — | [release](https://nature.global/press/release/18339/) |
| 2024-06-27 | シリーズDラウンド (additional close) | Not disclosed; Series D total 約12.2億円 | 脱炭素化支援機構 (JICN) | "25億円を超えた" (BRIDGE, disclosed amounts only) | [release](https://nature.global/press/release/20904/), [BRIDGE](https://thebridge.jp/2024/06/nature-series-d2-round-funding) |

- The company first used a series label in the June 2024 release ("2024年2月より実施しているシリーズDラウンド"); its 2018, 2019 and 2021 releases use only 第三者割当増資, and no company source labelling any round as Series A, B or C was found.
- 環境エネルギー投資 invested in 2019, 2021 and 2024; 大和企業投資 in 2018 and 2021. The 2019 release states DeNA's holding was to move to Delight Ventures, which the deck now lists as "Delight Ventures（DeNA）".
- Crowdfunding (Kickstarter 2016, Makuake 2016, Indiegogo) is reported by the company as over 2000万円 in total and is not included in the table ([2018-02-19](https://nature.global/press/release/524/)).
- The 2024-02 round was announced with the "Nature DER Platform" plan; the 2021 round with entry into electricity retail and a design advisor appointment.

### Statutory financial notices (決算公告)

Figures as transcribed from 官報 決算公告 by the [官報決算データベース](https://catr.jp/companies/9dfc0/74413) (accessed 2026-10-11). Revenue is not included in the published notices.

| Fiscal year end | Net income | Retained earnings | Total assets |
|---|---|---|---|
| 2026-03-31 (第11期, published 2026-07-30) | ▲1億9561万円 | ▲15億8649万6000円 | 11億7459万8000円 |
| 2025-03-31 (第10期, published 2025-07-30) | ▲3億927万7000円 | ▲13億9088万6000円 | 12億9620万4000円 |
| 2024-03-31 | ▲5億1040万円 | ▲10億8160万9000円 | 14億6000万2000円 |
| 2023-03-31 | ▲3億2341万5000円 | ▲5億6559万5000円 | 9億4373万9000円 |
| 2022-03-31 | ▲2億8676万4000円 | ▲2億2620万8000円 | 12億9255万5000円 |
| 2021-03-31 | 346万5000円 | 6502万9000円 | 6億6136万円 |

---

## Engineering

### Technology stack and platforms

**Confirmed by the company's technical writing and public assets:**

- **Backend:** "ほぼすべてGo"; Node.js on Lambda and Cloud Functions ([blog, 2021-04-29](https://engineering.nature.global/entry/start-blog)). The backend is a Go monorepo per the CTO ([blog, 2026-07-31](https://engineering.nature.global/entry/2026/07/prove-pure-refactoring-with-ai-and-auto-merge)). Public Go repositories under [`natureglobal`](https://github.com/natureglobal) include `firequeue` (Kinesis Data Firehose queue) and `realip`.
- **Cloud:** AWS — ECS (Fargate), ALB, Aurora MySQL, ElastiCache Redis (cache and Pub/Sub), DynamoDB for time-series data, Kinesis Data Firehose, Glue/Parquet, Lambda, Amplify; Terraform; Datadog. Google Cloud Functions and Firebase for some integrations ([blog, 2021-04-29](https://engineering.nature.global/entry/start-blog), [blog, 2024-04-02](https://engineering.nature.global/entry/2024/04/02/101743)). An outage report names the AWS US-EAST-1 region and ECS Fargate ([2024-07-31](https://nature.global/press/news/21522/)).
- **Mobile:** React Native and TypeScript for iOS and Android ([blog, 2021-04-29](https://engineering.nature.global/entry/start-blog)), with native widgets ([blog, 2022-12-06](https://engineering.nature.global/entry/add-native-widget-to-react-native-app)).
- **Firmware:** C on microcontrollers ([blog, 2021-04-29](https://engineering.nature.global/entry/start-blog)); ESP-IDF, with unit tests run under Catch2 on a FreeRTOS POSIX port ([blog, 2022-12-02](https://engineering.nature.global/entry/freertos-catch-part1)); forks of `esp-idf`, `esp-nimble` and `FreeRTOS-Kernel` on GitHub. Two firmware engineers co-wrote 『基礎から学ぶ 組込みRust』 ([blog, 2021-05-07](https://engineering.nature.global/entry/embedded-rust-from-basics)).
- **Device protocols:** Wi-Fi, BLE, Wi-SUN (920MHz) for the smart-meter B-route, LTE-M (EV Switch), Matter (Remo nano), ECHONET Lite ([Remo E2 release](https://nature.global/press/release/24003/), [EV Switch release](https://nature.global/press/release/26117/), [Remo nano release](https://nature.global/press/release/15936/)).
- **Public API surface:** HTTPS/JSON Cloud API at `api.nature.global` (OpenAPI 3.0.3), OAuth2 bearer tokens and an OpenID Connect provider; a Local API on the device discovered via Bonjour `_remo._tcp` ([developer portal](https://developer.nature.global/), [Cloud API spec](https://swagger.nature.global/), [Local API spec](https://local-swagger.nature.global/)).
- **Operations tooling:** status page on Atlassian Statuspage ([status.nature.global](https://status.nature.global/), response headers checked 2026-10-11); CI with GitHub Actions running Claude (Claude Code and the Claude API) to verify refactoring-only pull requests ([blog, 2026-07-31](https://engineering.nature.global/entry/2026/07/prove-pure-refactoring-with-ai-and-auto-merge)).

**Listed in current job postings** (hiring evidence; accessed 2026-10-11):

- Backend: Go, AWS, Docker, ECS, MySQL (RDS), Redis (ElastiCache), CircleCI, GitHub, Zenhub, Slack ([Backend Engineer](https://herp.careers/v1/nature/F06a8ZG7ncFG)).
- Firmware: C, C++ (C++17–C++23), Rust; Wi-Fi, BLE, LTE, Wi-SUN; HTTP, WebSocket, Matter, ECHONET-Lite; ESP32 series and ESP-IDF; Ubuntu hosts; GitHub Actions; LLM tools GitHub Copilot, Claude Code, Devin, Gemini, NotebookLM ([Firmware Engineer](https://herp.careers/v1/nature/km0uZc0P_FSl)).
- Mobile: React Native, TypeScript, Swift, Kotlin, Java; CircleCI ([Smartphone App Engineer](https://herp.careers/v1/nature/dhj2CBULhCSH)).
- The company deck lists AWS and GCP as clouds and ChatGPT, Claude Code, Claude Cowork, Gemini, Devin and Cursor among AI tools ([company deck](https://speakerdeck.com/naturepr/company-information)).

### Systems

| System | What it does | Source |
|---|---|---|
| Device connectivity | Remo devices keep long-lived WebSocket connections ("ウン十万接続") to eight Go "stream" servers on ECS behind an ALB; with ALB blue-green deployment the devices move to a new ALB over about 24–36 hours, and the post describes draining stream-server connections gradually during deploys | [blog, 2023-07-19](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown) |
| Infrared signal database | Air-conditioner signals captured with an in-house analysis tool, "Nature Learn", from remotes bought by staff; supplemented by official data from some manufacturers; air-conditioner detection is exposed as `/1/detectappliance` | [2026-06-18](https://nature.global/press/release/27356/), [Cloud API spec](https://swagger.nature.global/) |
| Local control | Air-conditioner operation over the home Wi-Fi when the cloud is unavailable, released after two outages in July 2024 | [2024-07-11](https://nature.global/press/news/21359/), [2025-02-12](https://nature.global/press/release/22669/) |
| HEMS / DER control | Remo E reads smart meters and ECHONET Lite equipment and controls batteries, V2H, EcoCute and Ene-Farm; Remo E2 supports the distribution-board metering class without a B-route application | [2026-08-24](https://nature.global/press/release/27984/), [Remo E API doc](https://developer.nature.global/docs/nature-remo-e-api-specification/) |
| Market-linked automation | JEPX area-price-linked air-conditioner and battery control; weather- and generation-based EcoCute heating; surplus-solar Tesla charging | [Nature Green page](https://shop.nature.global/pages/nature-green), [2026-09-24](https://nature.global/press/release/28217/) |
| DR support platform | Retailer admin console for registering DR events, JEPX-linked automatic triggering, participant emails, and result reports from preliminary and confirmed values; "上げDR" and "下げDR" | [2025-07-01](https://nature.global/press/release/24645/) |
| Aggregator integration | Cloud-to-cloud link in which Shizen Connect plans VPP control and Nature executes it on households' DER | [2024-10-30](https://nature.global/press/release/22262/) |
| EV charging control | LTE-M relay controller; API relay operations limited to 10 per day per device; meets 特定計量制度 requirements (display not yet implemented) | [Cloud API spec](https://swagger.nature.global/), [2026-03-10](https://nature.global/press/release/26117/) |
| Data pipeline | Kinesis Data Firehose ingestion via `firequeue` (asynchronous batching cut average API latency from 42.8 ms to 23.4 ms); Glue/Parquet for analysis | [blog, 2024-04-02](https://engineering.nature.global/entry/2024/04/02/101743), [blog, 2021-04-29](https://engineering.nature.global/entry/start-blog) |
| Firmware release tooling | CLI for staged firmware rollouts | [blog, 2022-12-09](https://engineering.nature.global/entry/staged-firmware-release-cli) |

### Technical background sought

From current HERP postings (accessed 2026-10-11):

- **Backend, required:** server-side development in Go, Ruby, Perl, Python, Java or similar; development and operation of a web application at "中規模以上（目安ユーザー規模1万人）"; review and test culture; building applications including systems from zero; native-level Japanese; interest in IoT. **Preferred:** multiple AWS services, microservice-style distributed systems, OSS contribution, IoT product development, agile/scrum ([posting](https://herp.careers/v1/nature/F06a8ZG7ncFG)).
- **Firmware, required:** embedded development in C and C++11 or later; TCP/IP and HTTP fundamentals; review and test culture. **Preferred:** IoT products, circuit design, web or mobile development, OSS, agile, Rust ([posting](https://herp.careers/v1/nature/km0uZc0P_FSl)).
- **Mobile, required:** iOS and Android apps integrated with a backend, at a similar scale. **Preferred:** backend development, React Native or Flutter, BLE device integration, OSS, agile ([posting](https://herp.careers/v1/nature/dhj2CBULhCSH)).
- Postings state that engineers currently share infrastructure, backend, mobile and embedded work and are expected to take tasks outside their main area when needed ([Backend posting](https://herp.careers/v1/nature/F06a8ZG7ncFG)).

### Industry domain

Japanese household energy: smart meters and the Wi-SUN B-route, ECHONET Lite device classes, JEPX spot prices, DR (behaviour-change and device-control, up and down), VPP and aggregation, the 需給調整市場, ERAB cybersecurity guidelines and JC-STAR, 特定計量制度, and national and Tokyo subsidy programs (GX志向型住宅, household battery and EV-charger subsidies) ([2025-04-08](https://nature.global/press/release/24003/), [2025-10-10](https://nature.global/press/release/25287/), [2026-08-24](https://nature.global/press/release/27984/)). Energy-industry experience is required for the business-development role "012" and five or more years of energy-product sales for the sales role ([BD posting](https://herp.careers/v1/nature/OZuuB4z-0YYb), [Sales posting](https://herp.careers/v1/nature/rxhJK_Wv9hzU)); the engineering postings do not list energy-domain knowledge as required, and the engineering-intern posting lists interest in IoT products or power systems under 求める人物像 ([posting](https://herp.careers/v1/nature/YqFSO9OIdsxs)). The company deck states 6% of full-time staff came from the energy industry ([company deck](https://speakerdeck.com/naturepr/company-information)).

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Working language | All postings are in Japanese. Backend: "ネイティブレベルの日本語力" required. Engineering intern: must read English technical documents. Recruiter/CEO assistant: English text communication required. No company language policy published | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG), [intern](https://herp.careers/v1/nature/YqFSO9OIdsxs), [recruiter](https://herp.careers/v1/nature/rdeGy2njtW2B) |
| Composition | Foreign nationals 10% of employees; 30s 57%, 40s 31%; male:female 3:1 | [company deck](https://speakerdeck.com/naturepr/company-information) (modified 2026-05-31) |
| Remote | Engineering postings: full remote allowed, on the premise of coming in when in-person discussion is needed; about one company-wide office day per month. Deck: development roles fully remote by default; business and admin roles about two office days per week recommended. Interns: at least one office day per week | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG), [company deck](https://speakerdeck.com/naturepr/company-information), [intern](https://herp.careers/v1/nature/UPK-qaE-dwBP) |
| Hours | Flextime with no core time; working window 5:00–22:00 | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| Location | Yokohama HQ, 5 minutes' walk from Yokohama Station | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| Salary | Annual salary system including 45 hours of fixed overtime pay: Backend ¥6.2M–¥12M; Smartphone App ¥6.2M–¥12M; Firmware ¥6.2M–¥9M; Product Manager ¥7.2M–¥12M; interns from ¥1,300/hour, engineering interns from ¥1,500/hour | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG), [App](https://herp.careers/v1/nature/dhj2CBULhCSH), [Firmware](https://herp.careers/v1/nature/km0uZc0P_FSl), [PdM](https://herp.careers/v1/nature/gh8SQSJj0ppB), [intern](https://herp.careers/v1/nature/UPK-qaE-dwBP), [eng. intern](https://herp.careers/v1/nature/YqFSO9OIdsxs) |
| Leave | Weekends and holidays, year-end holidays, annual paid leave and paid sick leave from joining, wedding and bereavement leave; probation with unchanged conditions | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| Benefits | Commuting allowance up to ¥80,000/month; books; study support; latest development devices; outdoor-activity support; EV, solar and battery purchase support; gadget support; language-study support; side jobs with permission | [Backend](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| Visa | No engineering posting mentions visa sponsorship; the labour/general-affairs posting lists "ビザの取得サポート" among its duties | [posting](https://herp.careers/v1/nature/A6An3g_K1bIS) |
| Juniors | Internship postings (engineering interns: minimum six months, at least two days a week of about four hours, remote allowed with some limits); no new-graduate posting found | [eng. intern](https://herp.careers/v1/nature/YqFSO9OIdsxs), [job list](https://herp.careers/v1/nature) |
| Organization | Holacracy-based for four years; Hybrid model with functional managers since December 2025 | [HR note (JA)](https://note.com/nature_global/n/n26cb9d5921ec) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-10-11): nature.global (sitemap index, WordPress REST API listing of 145 press releases and 180 notices), shop, terms, developer, swagger, status and engineering subdomains; HERP job board (15 postings); note and Speaker Deck accounts; GitHub organisations `natureglobal`, `nature-global`, `natureinc`, `nature-inc`, `nature-remo` and `natureremo`; NTA 法人番号公表サイト, gBizINFO, 電力・ガス取引監視等委員会 documents and 官報決算データベース; PR TIMES; BRIDGE, TechCrunch, Japan Dev; Japanese and English web searches for Nature株式会社, Nature Japan株式会社, Nature Inc. and product names.

- **Revenue.** Neither releases nor the 決算公告 transcriptions state revenue.
- **Valuation, the amount from each investor, and any lead investor** for any round, including the undisclosed 2024-06 JICN amount.
- **Retail electricity registration details.** The 2020-11-04 commission documents confirm the application; the METI registration number, registration date and any later withdrawal were not found in the reviewed sources (the METI register page returned HTTP 403 to automated access).
- **The US company's legal relationship** to Nature株式会社, and the incorporation date of Nature Japan株式会社.
- **Engineering headcount.** Only percentages are published (software engineers 38%, hardware engineers 6% of full-time roles in the deck).
- **Equity for employees.** Not mentioned in current HERP postings; Japan Dev's unverified profile lists an "Employee stock option plan".
- **Published SLA.** A public status page exists; no SLA or uptime commitment was found.
- **Open source.** The `natureglobal` organisation (name "Nature Inc.", email info@nature.global, created 2018-04-19) has 19 public repositories, of which 8 are original and 11 are forks; the most recent push to an original repository is `firequeue` (2024-07-31). A fork of `teslamotors/fleet-telemetry` was created 2026-04-28. `nature-remo` is a separate "Nature Remo Community" organisation with no stated company link.

### Inconsistencies across sources

- **Founding date:** "2014年12月10日" ([company page](https://nature.global/about/); also in releases from at least [2022-04-11](https://nature.global/press/release/8397/)); "2015年にハーバード大学発ベンチャーとして設立" ([2019-08-01 release](https://nature.global/press/release/566/)); US registration in December 2014 ([CEO interview](https://note.com/nature_global/n/n3a9457ec0239)). The fiscal year ended 2026-03-31 is labelled 第11期 in the 決算公告 ([官報決算データベース](https://catr.jp/companies/9dfc0/74413)); researcher inference: this numbering is consistent with a first fiscal period ending in March 2016, not December 2014.
- **Headcount:** 56 including contractors and interns ([company page](https://nature.global/about/); Undated); 50 including interns and contractors ([HERP company box](https://herp.careers/v1/nature/F06a8ZG7ncFG); Undated); 45 employees ([deck](https://speakerdeck.com/naturepr/company-information), modified 2026-05-31); 32 insured persons at the HQ office in the social-insurance data shown by [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=4130001055679) (date of the figure not shown). The scopes differ.
- **Capital:** "25.8億円（資本剰余金含む）" ([HERP](https://herp.careers/v1/nature/F06a8ZG7ncFG), [deck](https://speakerdeck.com/naturepr/company-information)) versus 資本金 "5000万円" in the [PR TIMES company box](https://prtimes.jp/main/html/rd/p/000000182.000019285.html) (accessed 2026-10-11). The first includes capital surplus; the second does not say.
- **Unit counts:** over 800,000 for the Nature Remo series alone ([2026-06-18](https://nature.global/press/release/27356/), [2026-10-01](https://nature.global/press/release/28318/)) versus 800,000 for Remo and Remo E combined ([deck](https://speakerdeck.com/naturepr/company-information), modified 2026-05-31) versus "累計70万台" for consumer sales in the [Business Development posting](https://herp.careers/v1/nature/oDyWEgu8BBMF) (datePosted 2022-03-18; accessed 2026-10-11).
- **CTO role:** the [team page](https://nature.global/careers/team/) heads 大塚's entry "CTO" but says "現在はソフトウェアエンジニア。エストニア在住"; the [deck](https://speakerdeck.com/naturepr/company-information) says "Co-founder and CTO … 現在はソフトウェア全般を統括する"; his [2023-07-19 post](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown) says he returned to the CTO role in July 2023.
- **Working language and hours:** Japan Dev's unverified, undated profile says "We don't require Japanese skill for developers", lists core hours 11:00–17:00, a ¥30,000 commuting cap and a Tokyo location ([Japan Dev](https://japan-dev.com/companies/nature); accessed 2026-10-11); the current [Backend posting](https://herp.careers/v1/nature/F06a8ZG7ncFG) requires native-level Japanese, has no core time, a ¥80,000 cap, and a Yokohama office.

### Other

- **Electricity retail entered and exited.** Natureスマート電気 ran from 2021-03-01 to 2022-06-30; the company then said it would focus on DR, ZEH and EV energy management ([2022-04-11](https://nature.global/press/release/8397/)). The DR support service began with Kansai Electric in summer 2022.
- **Outages.** On 2024-07-08 a write surge on the time-series database took down the API servers, followed by mass reconnections; on 2024-07-31 an AWS ECS Fargate incident in US-EAST-1 broke WebSocket connections ([2024-07-11](https://nature.global/press/news/21359/), [2024-07-31](https://nature.global/press/news/21522/)). The company named server-independent control as its priority; local control shipped for Remo Lapis on [2025-02-12](https://nature.global/press/release/22669/) and for Remo 3 and Remo mini 2 on [2025-03-18](https://nature.global/press/news/23693/).
- **Overseas sales.** The company planned Remo sales in the US, Australia and Singapore from late September 2020 ([2020-09-16](https://nature.global/press/release/615/)); TechCrunch reported a US and Canada launch of Remo 3 and that the team had made monthly trips to factories in Shenzhen before the pandemic ([TechCrunch, 2020-09-23](https://techcrunch.com/2020/09/23/japanese-startup-nature-launches-remo-3-its-home-appliance-smart-remote-in-the-u-s-and-canada)). `en.nature.global` redirected to the Japanese site on 2026-10-11; no current statement on overseas sales was found.
- **Discontinued integrations:** IFTTT ([2023-12-13](https://nature.global/press/news/18009/)) and the Nature user community ([2024-04-01](https://nature.global/press/news/19351/)).
- **Publishing surfaces.** The company runs an [engineering blog](https://engineering.nature.global/) on Hatena (latest post 2026-07-31; earliest 2021-04-29), a [note account](https://note.com/nature_global) with staff interviews, and a [connpass group](https://nature.connpass.com/) whose most recent event was 2023-07-19. The API reference and OpenAPI files are public.

---

## Resources

**Official**

- [Corporate site (JA)](https://nature.global/) · [company page](https://nature.global/about/) · [mission](https://nature.global/mission/) · [business page](https://nature.global/business/) · [Nature API business page](https://nature.global/business/api-remo/)
- [Press release index](https://nature.global/press/release/)
- [Careers](https://nature.global/careers/) · [team](https://nature.global/careers/team/) · [job list](https://nature.global/careers/job/) · [interviews](https://nature.global/careers/interview/)
- [HERP job board](https://herp.careers/v1/nature) — [Backend Engineer](https://herp.careers/v1/nature/F06a8ZG7ncFG), [Firmware Engineer](https://herp.careers/v1/nature/km0uZc0P_FSl), [Smartphone App Engineer](https://herp.careers/v1/nature/dhj2CBULhCSH), [Product Manager](https://herp.careers/v1/nature/gh8SQSJj0ppB), [Business Development](https://herp.careers/v1/nature/oDyWEgu8BBMF), [Business Development (energy)](https://herp.careers/v1/nature/OZuuB4z-0YYb), [Sales (energy management)](https://herp.careers/v1/nature/rxhJK_Wv9hzU), [Labour/general affairs](https://herp.careers/v1/nature/A6An3g_K1bIS), [Recruiter/CEO assistant](https://herp.careers/v1/nature/rdeGy2njtW2B), [Intern](https://herp.careers/v1/nature/UPK-qaE-dwBP), [Engineering intern](https://herp.careers/v1/nature/YqFSO9OIdsxs)
- [Developer portal](https://developer.nature.global/) · [Remo E API](https://developer.nature.global/docs/nature-remo-e-api-specification/) · [Cloud API spec](https://swagger.nature.global/) · [Local API spec](https://local-swagger.nature.global/)
- [Nature Green](https://shop.nature.global/pages/nature-green) · [Terms and policies](https://terms.nature.global/ja/) · [Status page](https://status.nature.global/)
- [Engineering blog (JA)](https://engineering.nature.global/) · [note (JA)](https://note.com/nature_global) · [company deck on Speaker Deck (JA)](https://speakerdeck.com/naturepr/company-information) · [connpass](https://nature.connpass.com/) · [GitHub organization](https://github.com/natureglobal)

**Press releases and notices (nature.global, JA — newest first)**

- [Air-conditioner operation guarantee — 2026-10-01](https://nature.global/press/release/28318/)
- [Smart EV charging for Tesla — 2026-09-24](https://nature.global/press/release/28217/)
- [Tokyo household aggregator registration — 2026-08-24](https://nature.global/press/release/27984/)
- [Air-conditioner guarantee campaign, Nature Learn — 2026-06-18](https://nature.global/press/release/27356/)
- [Nature Lock general sale — 2026-04-30](https://nature.global/press/release/26672/)
- [Nature Lock and Nature Key announced — 2026-04-21](https://nature.global/press/release/26546/)
- [EV Switch individual sales — 2026-03-10](https://nature.global/press/release/26117/)
- [ISO/IEC 27001 — 2026-03-09](https://nature.global/press/release/26121/)
- [Setagaya demonstration results — 2025-12-25](https://nature.global/press/release/25801/)
- [EV Switch launch — 2025-10-31](https://nature.global/press/release/25360/)
- [JC-STAR ★1 — 2025-10-10](https://nature.global/press/release/25287/)
- [EV remote charging demonstration — 2025-09-04](https://nature.global/press/release/25064/)
- [Forbes JAPAN GX 50 — 2025-08-14](https://nature.global/press/news/24875/)
- [DR support service renewal — 2025-07-01](https://nature.global/press/release/24645/)
- [Nature Remo E2 — 2025-04-08](https://nature.global/press/release/24003/)
- [Tokyo Gas DR support service — 2025-04-02](https://nature.global/press/release/23974/)
- [Local control for Remo 3 and mini 2 — 2025-03-18](https://nature.global/press/news/23693/)
- [EV Switch and Panasonic — 2025-02-25](https://nature.global/press/release/23308/)
- [Local control for Remo Lapis — 2025-02-12](https://nature.global/press/release/22669/)
- [Shizen Connect partnership — 2024-10-30](https://nature.global/press/release/22262/)
- [Good Design Award — 2024-10-16](https://nature.global/press/release/22036/)
- [Outage report — 2024-07-31](https://nature.global/press/news/21522/)
- [Outage cause report — 2024-07-11](https://nature.global/press/news/21359/)
- [Nature Remo Lapis — 2024-07-05](https://nature.global/press/release/21289/)
- [Series D total 12.2億円 — 2024-06-27](https://nature.global/press/release/20904/)
- [auエネルギー＆ライフ — 2024-06-26](https://nature.global/press/release/20279/)
- [Kansai Electric year-round DR — 2024-06-25](https://nature.global/press/news/20713/)
- [Tokyo Gas alliance — 2024-04-18](https://nature.global/press/release/19564/)
- [User community closure — 2024-04-01](https://nature.global/press/news/19351/)
- [ドコモでんき自動エコモード — 2024-03-04](https://nature.global/press/release/18635/)
- [10.2億円 funding — 2024-02-07](https://nature.global/press/release/18339/)
- [IFTTT integration ended — 2023-12-13](https://nature.global/press/news/18009/)
- [Nature Green paid option — 2023-08-08](https://nature.global/press/release/16586/)
- [Nature Remo nano — 2023-07-04](https://nature.global/press/release/15936/)
- [Octopus Energy DR — 2023-02-13](https://nature.global/press/release/13793/)
- [NTT Docomo DR — 2022-12-23](https://nature.global/press/release/12753/)
- [Kansai Electric DR — 2022-06-28](https://nature.global/press/release/9771/)
- [Natureスマート電気 closure — 2022-04-11](https://nature.global/press/release/8397/)
- [7.5億円 funding — 2021-07-14](https://nature.global/press/release/5754/)
- [Natureスマート電気 nationwide — 2021-07-06](https://nature.global/press/release/5591/)
- [300,000 units, iF Design Award 2021 — 2021-04-15](https://nature.global/press/release/5025/)
- [Natureスマート電気 launch — 2021-03-01](https://nature.global/press/release/4320/)
- [Google for Startups Accelerator — 2021-01-07](https://nature.global/press/release/3816/)
- [Paid corporate Remo E API — 2021-01-05](https://nature.global/press/release/3811/)
- [200,000 units, overseas plans — 2020-09-16](https://nature.global/press/release/615/)
- [Nature Remo 3 — 2020-08-05](https://nature.global/press/release/606/)
- [Nature Remo E lite — 2020-04-28](https://nature.global/press/release/589/)
- [iF Design Award 2020 — 2020-02-05](https://nature.global/press/news/1426/)
- [Nature Remo E preorders — 2019-12-10](https://nature.global/press/release/578/)
- [Technical advisor 川崎修平 — 2019-11-17](https://nature.global/press/release/575/) · [technical advisor 阿部力也 — 2019-11-17](https://nature.global/press/release/572/)
- [5億円 funding — 2019-08-01](https://nature.global/press/release/566/)
- [1億円 funding — 2018-02-19](https://nature.global/press/release/524/)
- [API published — 2018-02-01](https://nature.global/press/news/1361/)
- [Nature Remo on sale — 2017-10-16](https://nature.global/press/release/522/)
- [500 KOBE ACCELERATOR — 2017-08-14](https://nature.global/press/news/1312/)
- [VPP demonstration — 2017-07-25](https://nature.global/press/news/513/)
- [Kickstarter US$50,000 — 2016-06-03](https://nature.global/press/release/456/)

**Engineering blog and interviews (JA)**

- [Technologies behind Nature Remo — 2021-04-29](https://engineering.nature.global/entry/start-blog)
- [Embedded Rust book — 2021-05-07](https://engineering.nature.global/entry/embedded-rust-from-basics)
- [FreeRTOS + Catch2 — 2022-12-02](https://engineering.nature.global/entry/freertos-catch-part1)
- [Native widgets in React Native — 2022-12-06](https://engineering.nature.global/entry/add-native-widget-to-react-native-app)
- [Staged firmware release CLI — 2022-12-09](https://engineering.nature.global/entry/staged-firmware-release-cli)
- [WebSocket ECS graceful shutdown — 2023-07-19](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown)
- [firequeue — 2024-04-02](https://engineering.nature.global/entry/2024/04/02/101743)
- [AI-verified refactoring auto-merge — 2026-07-31](https://engineering.nature.global/entry/2026/07/prove-pure-refactoring-with-ai-and-auto-merge)
- [CEO interview, 立志編 — 2025-12-04](https://note.com/nature_global/n/n3a9457ec0239) · [組織・カルチャー編 — 2025-12-04](https://note.com/nature_global/n/nb47e66f7c43d)
- [Hybrid organization — 2025-12-19](https://note.com/nature_global/n/n26cb9d5921ec)
- [大塚 interview — 2022-08-18](https://note.com/nature_global/n/n6c8b703cdc85)

**Registers, filings and third-party coverage**

- [NTA 法人番号公表サイト — 4130001055679 (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679)
- [gBizINFO (JA)](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=4130001055679)
- [電力・ガス取引監視等委員会 — reply, 2020-11-04 (JA)](https://www.egc.meti.go.jp/info/public/pdf/20201104001b.pdf) · [applicant list (JA)](https://www.egc.meti.go.jp/info/public/pdf/20201104001c.pdf)
- [官報決算データベース — 決算公告 transcriptions (JA)](https://catr.jp/companies/9dfc0/74413)
- [PR TIMES — release with company box, 2026-10-01 (JA)](https://prtimes.jp/main/html/rd/p/000000182.000019285.html)
- [BRIDGE — Series D total 12.2億円, 2024-06-28 (JA)](https://thebridge.jp/2024/06/nature-series-d2-round-funding)
- [TechCrunch — Remo 3 in the US and Canada, 2020-09-23](https://techcrunch.com/2020/09/23/japanese-startup-nature-launches-remo-3-its-home-appliance-smart-remote-in-the-u-s-and-canada)
- [Japan Dev — company profile (unverified)](https://japan-dev.com/companies/nature)
