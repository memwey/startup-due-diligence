# Notta

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-29.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

Notta is an AI transcription and meeting-notes product — web app, iOS and Android apps, a Chrome extension, a desktop app, and a hardware voice recorder — sold mainly into the Japanese market and increasingly into the US ([company page](https://www.notta.ai/company); accessed 2026-07-29). The Japanese operating entity, **Ｎｏｔｔａ株式会社**, was established on 2022-05-25 and is registered under corporate number 5010001226919 ([国税庁法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919)), but the company dates its own founding to 2020 and the iOS app has been on the store since 2019-12-19 ([timeline](https://www.notta.ai/hardware/memo), [iTunes API](https://itunes.apple.com/lookup?id=1480649572)). The CEO is Ryan Zhang.

- **Funding:** ¥1.4bn raised in 2022 ([company timeline](https://www.notta.ai/hardware/memo)), a ¥990M round the company calls **Series A+** on [2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html), and a ¥2.3bn (US$15M) **Series B** led by Granite-Integral Capital on [2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html).
- **Scale, as the company states it:** 5,000 companies and 15 million users as of [2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html); 72% of Nikkei 225 companies and enterprise users up 300% year on year as of [2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html). Headcount is 100 including overseas sites, as of end-January 2026 ([company page](https://www.notta.ai/company)).
- **Security posture is unusually well documented for a company this size:** ISO 27001, SOC 2 Type 1 obtained 2022-09-29 and Type 2 on 2023-02-12, plus stated HIPAA/GDPR/APPI/CCPA compliance and named CPO and CISO roles ([security page](https://www.notta.ai/security)).
- **The stack is mostly reconstructible from the `mindcruiser` GitHub org:** a Flutter/Dart mobile app (Firebase, `dio`, `drift`/`floor`, `just_audio`, `flutter_quill`, `flutter_blue_classic` for the hardware recorder, and an in-house `mc_flutter_recorder` plugin), AWS with customer data in a Japan region, and an official [MCP server for Claude Desktop](https://github.com/mindcruiser/notta-mcp). Summarization runs on OpenAI GPT-5, but [not on the Business and Enterprise plans](https://www.notta.ai/blog/notta-gpt5-integration).
- **Four legal entities carry the brand.** The Japanese terms name Ｎｏｔｔａ株式会社 under Japanese law and Tokyo District Court; the [English terms](https://www.notta.ai/en/terms) name "Notta Inc." under **Hong Kong** law and Hong Kong courts. The iOS app is published by **Mind Cruiser Limited** (Hong Kong), the Android app by **NOTTA PTE. LTD.** (Singapore), and both app bundle identifiers sit in a `com.langogo.*` namespace.

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | Notta | [company page](https://www.notta.ai/company) |
| Legal name (Japan) | Ｎｏｔｔａ株式会社; "Notta Inc." in English materials | [company page](https://www.notta.ai/company), [English terms](https://www.notta.ai/en/terms) |
| Corporate number | 5010001226919; invoice registration number T5010001226919 | [国税庁法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919), [company page](https://www.notta.ai/company) |
| Established | 2022-05-25 (corporate number assigned 2022-05-27); the company's own timeline says it was founded in 2020 and launched the mobile app that May | [company page](https://www.notta.ai/company), [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919), [timeline](https://www.notta.ai/hardware/memo) |
| Representative | Ryan Zhang, 代表取締役 | [company page](https://www.notta.ai/company) |
| Capital | ¥9,000,000 | [company page](https://www.notta.ai/company) |
| Address | 〒100-0004 東京都千代田区大手町1-9-2 大手町フィナンシャルシティグランキューブ3階, moving on 2026-08-03 to 〒101-0051 東京都千代田区神田神保町1-13 J.NODE神保町4階 | [company page](https://www.notta.ai/company), [relocation notice, 2026-07-27](https://www.notta.ai/news/info/20260803-office-relocation) |
| Registered-address history | 2023-07-14 from 中央区日本橋1-2-10 東洋ビル5階; 2025-04-21 from 渋谷区道玄坂1-12-1 渋谷マークシティW22階 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919) |
| Phone | 03-6820-6068 | [company page](https://www.notta.ai/company) |
| Headcount | 100, "including global sites", as of end-January 2026 | [company page](https://www.notta.ai/company) |
| Customers | 5,000 companies and 15 million users | [Series B release, 2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |
| Certifications | ISO 27001; SOC 2 Type 1 (2022-09-29) and Type 2 (2023-02-12) | [security page](https://www.notta.ai/security) |
| Total raised | ¥1.4bn (2022) + ¥990M (2025-05) + ¥2.3bn (2025-12) | [timeline](https://www.notta.ai/hardware/memo), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html), [PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |
| Engineering working language | Not stated. The careers page, corporate page and news are Japanese-first; product and docs ship in 20 languages | [recruit page](https://www.notta.ai/recruit), [company page](https://www.notta.ai/company) |
| Contact | contact@notta.ai (press), support@notta.ai | [company page](https://www.notta.ai/company), [incident report](https://www.notta.ai/news/info/20260310-incident-report) |
| PR agency | サニーサイドアップ (Sunny Side Up) handles press enquiries | [PR TIMES, 2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) |

The company also states it holds the 『職場環境改善宣言企業』 certification from the National Federation of Labour and Social Security Attorneys' Associations ([company page](https://www.notta.ai/company)), and lists distributor agreements with ダイワボウ情報システム and SBC&S signed in 2024, plus ITreview Grid Award "Leader" placements in three categories in 2024 Fall and 2025 Winter ([timeline](https://www.notta.ai/hardware/memo)).

### Identity and legal entities

Four entities and one legacy namespace carry the Notta brand. Which one a user contracts with depends on the language of the page they read.

| Name | Type | Role | Source |
|---|---|---|---|
| Ｎｏｔｔａ株式会社 | Japanese KK | Named as the service provider in the Japanese terms, which specify Japanese law and Tokyo District Court as the exclusive first-instance forum | [Japanese terms, art. 22](https://www.notta.ai/terms) |
| "Notta Inc." | Name used in English materials | Named as the provider in the English terms, which specify **Hong Kong** law and exclusive jurisdiction in Hong Kong courts | [English terms](https://www.notta.ai/en/terms) |
| Mind Cruiser Limited | Hong Kong company | Publisher of the iOS app; also the owner of the [`mindcruiser` GitHub organisation](https://github.com/mindcruiser), which lists Japan and links to notta.ai | [iTunes API](https://itunes.apple.com/lookup?id=1480649572), [GitHub org](https://api.github.com/orgs/mindcruiser) |
| NOTTA PTE. LTD. | Singapore company | Publisher of the Android app; developer address given as c/o Tricor Singapore, 9 Raffles Place #26-01 Republic Plaza | [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |
| `com.langogo.*` | Application namespace | The iOS bundle id is `com.langogo.lggtranscribe` and the Android package is `com.langogo.transcribe`, pointing to an earlier Langogo-branded lineage that no current Notta page explains | [iTunes API](https://itunes.apple.com/lookup?id=1480649572), [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |

The Japanese entity is verifiable in the national registry, including its address history. No filing, release, or company page found on 2026-07-29 states the ownership relationship between Ｎｏｔｔａ株式会社, Mind Cruiser Limited and NOTTA PTE. LTD., or explains the Langogo namespace; see `Notes`.

---

## Product

### Surfaces

| Surface | Detail | Source |
|---|---|---|
| Web app | `app.notta.ai`; marketing site is a Gatsby static build served from Amazon S3 behind CloudFront | [response headers](https://www.notta.ai/en), accessed 2026-07-29 |
| iOS | "Notta-自動文字起こし" / "Notta Transcribe Voice to Text", bundle `com.langogo.lggtranscribe`, first released 2019-12-19, version 6.76.16 on 2026-07-20, minimum iOS 13.0, 21 localizations | [iTunes API](https://itunes.apple.com/lookup?id=1480649572) |
| Android | "Notta-Transcribe Audio to Text", package `com.langogo.transcribe`, 1M+ downloads bucket, updated 2026-07-18 | [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |
| Chrome extension | Transcribes audio playing in web pages | [company page](https://www.notta.ai/company) |
| Desktop | Notta Desktop, Windows and macOS (Intel and Apple Silicon), released 2026-07-08 | [release, 2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| Hardware | Notta Memo AI voice recorder, on sale 2025-06-16 at ¥23,500 including tax, sold through Amazon; Zenchord 1 AI microphone previewed on Makuake | [Notta Memo page](https://www.notta.ai/hardware/memo), [timeline](https://www.notta.ai/hardware/memo) |

### Core capabilities

Transcription is claimed at **98.86% accuracy across 58 languages**, with automatic speaker identification, translation into 42 languages, screen recording, cross-device sync, AI noise removal on playback, team workspaces and AI summarization ([App Store description](https://itunes.apple.com/lookup?id=1480649572), [Notta Memo page](https://www.notta.ai/hardware/memo)). The careers page instead says the service covers **104 languages** and selects "the optimal AI speech-recognition engine for each language" ([recruit page](https://www.notta.ai/recruit)) — the clearest public statement that recognition is not a single in-house model.

**Notta Brain** is the AI platform layer, released 2026-01-30 and absorbing the former "AI chat" feature on 2026-03-30. It works over stored recordings, transcripts and uploaded documents to summarize, analyse across multiple meetings, generate slides and images, apply scoring rubrics to interviews or sales calls, and answer questions in real time. On [2026-06-17](https://www.notta.ai/news/release/notta-brain-new-features) it gained scheduled recurring tasks, a Slack bot and a LINE bot, with purpose-built AI tools in beta for some individual users.

**Notta Desktop** ([2026-07-08](https://www.notta.ai/news/release/notta-desktop)) adds two things the cloud product cannot do: a **privacy mode** in which all AI processing happens on the user's own PC with no audio or transcript uploaded anywhere, and **bot-free recording**, which captures the PC's system audio directly instead of sending a note-taking bot into Zoom, Teams or Google Meet. It is available on the Premium, Business and Enterprise plans, with privacy mode gated behind a sales conversation for invoice-billed customers.

### Integrations

23 integrations are published: Zoom, Microsoft Teams, Google Meet, Webex; Google Calendar and Outlook Calendar; Google Docs, Google Drive, Microsoft OneDrive, OneNote, SharePoint, Box, Dropbox, Notion; Salesforce, HubSpot, Pipedrive, Zoho CRM, Zendesk Sell, Salesflare, Freshsales; kintone, ClickUp, Slack and Zapier ([sitemap](https://www.notta.ai/sitemap-0.xml)). The 2025 AWS outage notice additionally names an Autodesk authorization integration ([2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact)).

### Commercialization

Subscription SaaS with metered transcription minutes, plus add-ons and a hardware line. Annual pricing as displayed on 2026-07-29 ([pricing page](https://www.notta.ai/en/pricing)):

| Plan | Price (annual billing) | Transcription | Per recording | Notable |
|---|---|---|---|---|
| Free | ¥0 | 120 min/month, 50 file uploads, 10 AI summaries | 3 minutes | 1 seat, no card required |
| Pro | ¥1,185/month (¥14,220/year) | 1,800 min/month, 100 uploads, 100 summaries | 5 hours | Export, translation, custom vocabulary |
| Business | ¥2,508/month/seat (¥30,096/year) | Unlimited, 200 uploads, 200 summaries | 5 hours | Meeting video recording, usage reports, CRM and Zapier |
| Enterprise | Custom, from 51 seats | Customized, unlimited uploads and summaries | 5 hours | SAML SSO, audit logs, full data access control, 50% education discount |
| ビジネスPlus (Japan, from 2026-07-27) | ¥9,000/month/seat, ¥64,800/year/seat ex-tax | Business features plus all Notta Brain features | — | "No AI training" setting, 8,000 credits/month, image and slide generation, real-time summary, recurring tasks |

Add-ons sold separately to Pro, Business and Enterprise users: monolingual translation at ¥858/month annually (¥1,430 monthly), bilingual transcription and translation at ¥1,320/month annually (¥2,200 monthly), and Notta Brain at ¥14,300/year for 8,000 AI credits per month ([pricing page](https://www.notta.ai/en/pricing)). A [price change](https://www.notta.ai/news/info/2025-06-16-price-changed) was announced for 2025-06-16.

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2019-12-19 | iOS app first release | [iTunes API](https://itunes.apple.com/lookup?id=1480649572) |
| 2020 | Company dates its founding here; mobile app service started in May | [timeline](https://www.notta.ai/hardware/memo) |
| 2022 | ¥1.4bn raised in total; SOC 2 Type II obtained | [timeline](https://www.notta.ai/hardware/memo) |
| 2022-09-29 / 2023-02-12 | SOC 2 Type 1 report, then Type 2 report | [security page](https://www.notta.ai/security) |
| 2025-05-29 | 10 million users; enterprise users +300% YoY; 72% of Nikkei 225 companies | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) |
| 2025-06-16 | Notta Memo hardware on sale at ¥23,500 | [Notta Memo page](https://www.notta.ai/hardware/memo) |
| 2025-07-23 | 8M+ users, 100,000+ clients, 300M+ hours processed; hardware priced at US$149 in the US | [Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/) |
| 2025-12-09 | 5,000 companies and 15 million users | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |
| Accessed 2026-07-29 | English site: 10M+ users, 6,000+ companies, 30M+ hours transcribed | [about page](https://www.notta.ai/en/about) |
| Accessed 2026-07-29 | Notta Memo page: 15M cumulative users, 5,000+ companies, 10M hours transcribed | [Notta Memo page](https://www.notta.ai/hardware/memo) |
| Accessed 2026-07-29 | Careers page: "over 1.5 million users"; Japanese site footer: "2 million downloads" | [recruit page](https://www.notta.ai/recruit), [company page](https://www.notta.ai/company) |
| Accessed 2026-07-29 | iOS Japan: 4.35 from 25,968 ratings; iOS US: 4.05 from 1,374 ratings; Google Play 1M+ downloads | [iTunes API](https://itunes.apple.com/lookup?id=1480649572), [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |

### Announced customers and partners

| Date | Party | Detail |
|---|---|---|
| 2024 | ダイワボウ情報システム, SBC&S | Distributor agreements for the Japanese channel ([timeline](https://www.notta.ai/hardware/memo)) |
| [2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) | Granite-Integral Capital | Series B lead; the investor frames Notta as embodying its "Japan Nexus" thesis |
| [2026-06-25](https://www.notta.ai/news/info/kochi-bank) | 高知銀行 (Kochi Bank) | Regional bank deployment |
| [2025-11-27](https://www.notta.ai/news) | オープンハウス・アーキテクト | Joint roundtable on the AI meeting-minutes market |

### Stated plans

The Series A+ release names three uses of funds: accelerating the hardware ecosystem, concentrated investment in speech recognition and NLP, and a large expansion of Japanese enterprise sales and support ([2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)). The Series B release narrows this to hiring for enterprise expansion and continued voice-AI development across both software and hardware ([2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)). The US is described by the CEO as the next market because it is the largest SaaS and AI-productivity market ([Slator, 2025-07-23](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)). On the product side, the 2026-06-10 announcement states the company is strengthening AI product development, web application infrastructure and user-experience design for an "AI agent era" ([2026-06-10](https://www.notta.ai/news/info/ai-agent-era-development-enhancement)).

---

## Founder

| Name | Role | Career facts stated | Source |
|---|---|---|---|
| Ryan Zhang | 代表取締役 / Founder and CEO | Chinese serial technology entrepreneur who has launched multiple applications and chose to build outside China; the voice-to-text app succeeded in Japan and was not made available in China | [Nikkei Asia, 2023-03-29](https://asia.nikkei.com/business/china-tech/chinese-tech-entrepreneur-bets-big-on-japan-but-not-china), [company page](https://www.notta.ai/company) |

Ryan Zhang is named as representative director in both funding releases and in the national corporate registry filings referenced from the company page. He authored a book, *VOICE TO PROFIT*, which opened for pre-order on Amazon on [2025-11-04](https://www.notta.ai/news). No co-founder is named in any source reviewed on 2026-07-29.

### Selected leadership

| Name | Role | Source |
|---|---|---|
| Ranee Zhang | VP of Growth | [author page on notta.ai](https://www.notta.ai/en/author/ranee-zhang) |
| CPO and CISO | The security page states the company has a security group of senior managers including a Chief Privacy Officer and a Chief Information Security Officer; neither is named | [security page](https://www.notta.ai/security) |

No CTO, VP of Engineering, or engineering manager is named on any Notta surface. The only individually named technical employee is a software engineer — see `Engineering`.

---

## Funding

| Date | Round | Amount | Investors named | Cumulative | Source |
|---|---|---|---|---|---|
| 2022 | Not named | ¥1.4bn in total | Not disclosed | ¥1.4bn | [company timeline](https://www.notta.ai/hardware/memo) |
| 2025-05-29 | **シリーズA+ (Series A+)** | ¥990M | Mizuho Leaguer Investment and GSR Ventures newly joined; existing investors added | ~¥2.39bn | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) |
| 2025-12-09 | **Series B** | ¥2.3bn (US$15M) | Led by Granite-Integral Capital Pte. Ltd. (Singapore; co-heads CK Chuon and Joe Yan) | ~¥4.69bn | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |

No valuation has been disclosed for any round. The 2022 raise appears only as a one-line entry on the company's own timeline, with no round name, date, or investor.

Round naming diverges across sources for the May 2025 raise: the company calls it **Series A+**, [BRIDGE](https://thebridge.jp/2025/05/notta-a-provider-of-ai-meeting-minutes-services-raises-990-million-yen-in-series-a-funding) reports it as Series A, and [Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/) describes a US$6.3M round that closed 2025-06-30 with GL Ventures and Mizuho Leaguer Investments leading and GSR participating — naming a lead and a closing date the company's own release does not, and putting cumulative funding "over US$16 million", which is consistent with ¥1.4bn plus ¥990M but not with any figure the company publishes.

Granite-Integral Capital is described in the Series B release as a joint venture between **Granite Asia** and **Integral Globaltech Partners** (founded 2025, subsidiary of インテグラル株式会社), running a US$100M growth fund; Granite Asia is stated to manage US$5bn across APAC ([PR TIMES, 2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)).

---

## Engineering

### Technology stack and platforms

Confirmed from public assets — the `mindcruiser` GitHub organisation, npm, HTTP response headers, and the company's own incident and release notices (all accessed 2026-07-29):

| Item | Detail | Evidence |
|---|---|---|
| Cloud | AWS. Customer audio and transcript data are stated to be stored entirely in a Japan region; some services depended on `us-east-1` and broke during the 2025-10-20 outage | [outage notice, 2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact) |
| Marketing site | Gatsby static build (`/page-data/` routes) on Amazon S3 with `INTELLIGENT_TIERING`, fronted by CloudFront | [response headers](https://www.notta.ai/en), [robots.txt](https://www.notta.ai/robots.txt) |
| Mobile app | Flutter / Dart. The org forks `just_audio`, `flutter_file_picker`, `uni_links`, `app_links`, `share_handler`, `flutter_quill`, `dio`, `drift`, `floor`, `flutter_keychain`, `plus_plugins`, `flutterfire` and `aad_oauth` | [GitHub org repos](https://api.github.com/orgs/mindcruiser/repos) |
| In-house mobile plugin | `mc_flutter_recorder`, a Swift Flutter plugin for audio recording, created 2023-01-05 | [GitHub](https://github.com/mindcruiser/mc_flutter_recorder) |
| Hardware connectivity | `flutter_blue_classic` (Bluetooth Classic plugin) forked 2024-10-16; Notta Memo transfers recordings to the app over Bluetooth or Wi-Fi | [GitHub org repos](https://api.github.com/orgs/mindcruiser/repos), [Notta Memo page](https://www.notta.ai/hardware/memo) |
| Identity | Azure Active Directory OAuth via `aad_oauth`; SAML SSO on the Enterprise plan; Apple, Google and Microsoft third-party sign-in | [GitHub org repos](https://api.github.com/orgs/mindcruiser/repos), [pricing page](https://www.notta.ai/en/pricing), [privacy policy](https://www.notta.ai/en/privacy) |
| Session capture | `rrweb` ("record and replay the web") forked 2024-07-05 | [GitHub org repos](https://api.github.com/orgs/mindcruiser/repos) |
| Web assets | `notta-web-icon` (pushed 2026-07-24) and `notta-web-static-files-storage`, described as a CDN store for the Notta Web project | [GitHub org repos](https://api.github.com/orgs/mindcruiser/repos) |
| Summarization model | OpenAI **GPT-5**, integrated into the AI summary feature; explicitly **not** applied on the Business and Enterprise plans | [blog, updated 2026-05-15](https://www.notta.ai/blog/notta-gpt5-integration) |
| Speech recognition | Not named. The careers page states Notta "uses the optimal AI speech-recognition engine for each language" — a per-language engine selection rather than one model | [recruit page](https://www.notta.ai/recruit) |
| On-device inference | Notta Desktop's privacy mode runs all AI processing locally on the user's Windows or macOS machine with zero external transmission | [release, 2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| Agent interface | `@notta-labs/notta-mcp` and `@notta-labs/notta-cli` on npm (created 2026-04-14, latest 2026-06-18), plus the [notta-mcp](https://github.com/mindcruiser/notta-mcp) repo: a local stdio MCP server packaged as a `.mcpb` Claude Desktop extension, built on `@modelcontextprotocol/sdk`, `@aws-sdk/client-s3` and `zod` | [npm](https://registry.npmjs.org/-/v1/search?text=notta), [GitHub](https://github.com/mindcruiser/notta-mcp) |
| Credential handling in the MCP server | OAuth flow writes to `~/.config/notta_cli/credentials.json` with `0700` on the directory and `0600` on the file; temporary S3 upload credentials are held in memory only; the `transcribe` tool rejects paths outside allow-listed folders, files over 2 GB, and recordings over 4 hours | [notta-mcp README](https://github.com/mindcruiser/notta-mcp) |
| Password storage | The security page states passwords are hashed with SHA-256 and that plaintext passwords are neither transmitted nor stored; stored audio, image and text data is encrypted at rest by default | [security page](https://www.notta.ai/security) |
| Backup and DR | Regular backups held in domestic (Japan) data centres, with a documented disaster-recovery plan and failover to a backup system or data centre | [security page](https://www.notta.ai/security) |
| Internal work tools | Google Workspace, Slack, Airtable, Notion, HubSpot | [recruit page](https://www.notta.ai/recruit) |

### Systems

| System | What it does | Source |
|---|---|---|
| Transcription pipeline | Live recording and file transcription with per-language engine selection, speaker identification, custom vocabulary, and AI noise removal at playback | [App Store description](https://itunes.apple.com/lookup?id=1480649572), [recruit page](https://www.notta.ai/recruit) |
| Meeting bot dispatch | A bot that joins Zoom, Teams, Google Meet and Webex calls to record and transcribe; runs with a hot-standby environment that was cut over within 28 minutes during the 2025 AWS outage | [outage notice, 2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact), [pricing page](https://www.notta.ai/en/pricing) |
| Bot-free desktop capture | Captures PC system audio directly so no participant appears in the meeting roster | [release, 2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| Local inference runtime | Fully on-device transcription and AI processing in Notta Desktop's privacy mode | [release, 2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| Notta Brain | Retrieval and analysis over stored recordings, transcripts and uploaded documents; cross-meeting analysis, slide and image generation, rubric-based scoring, real-time summary, scheduled recurring tasks, Slack and LINE bots | [release, 2026-06-17](https://www.notta.ai/news/release/notta-brain-new-features) |
| Calendar and automations | Meeting scheduling from calendar entries; Google Drive-triggered automations | [outage notice, 2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact), [pricing page](https://www.notta.ai/en/pricing) |
| Hardware sync | Notta Memo stores recordings on 32 GB of internal memory and transfers them to the app over Bluetooth (small files) or Wi-Fi (large files), after which a note is created automatically | [Notta Memo page](https://www.notta.ai/hardware/memo) |
| MCP server | Lets Claude Desktop upload local audio and video for transcription and then list, search, poll and read Notta records | [notta-mcp](https://github.com/mindcruiser/notta-mcp) |
| Monitoring | The security page describes real-time tracking of data-processing performance with traffic, latency and error-rate indicators and alerting; a public status page runs at `status.notta.ai` | [security page](https://www.notta.ai/security), [status.notta.ai](https://status.notta.ai/) |

Two incident notices are published, and both are specific. On [2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact) the company itemised which functions the AWS `us-east-1` outage broke and when each recovered — SSO login (16:42 detected, 18:22 restored), meeting bot dispatch (15:52 detected, hot-standby cutover complete 16:20), and Autodesk/Slack/Zoom authorization plus Google Drive automations (16:32 detected, 18:55 restored) — and stated that calendar sync, non-bot transcription, Zapier, store and payments, and AI features were unaffected. On [2026-03-10](https://www.notta.ai/news/info/20260310-incident-report) a four-hour-twenty-minute login failure returning HTTP 500 to users with expired local caches or new logins was traced to an update pushed by an external provider of a third-party software component in the web application, and resolved by disabling that component.

### Technical background sought

No engineering role is open. The [careers page](https://www.notta.ai/recruit) lists exactly one position as of 2026-07-29 — **Partner Sales (Hardware)** — requiring 3+ years of B2B sales, hardware or IT product sales experience, channel/reseller sales experience, and basic IT literacy described as "Mac use and use of various AI tools". Preferred: SaaS sales, AI/speech-recognition sales, channel-partner management, new-business launch experience, and business-level English or Chinese.

The one public statement about the engineering bar is a hiring announcement rather than a posting. On [2026-06-10](https://www.notta.ai/news/info/ai-agent-era-development-enhancement) the company announced that software engineer **Yan Siyuan (Matt)** had joined the development team to work on the Notta Brain agent experience and on product-development infrastructure. His stated background — one of the maintainers of the Rust/WebAssembly frontend framework **Yew**, leading recent major releases, and a collaborator and package owner on **gloo** — checks out against the primary record: the GitHub account [Madoshakalaka](https://github.com/Madoshakalaka) gives the name Siyuan Yan, company Notta, location Tokyo and the bio "Call me Matt too. Maintainer at @yewstack"; it published the `yew-v0.22.0` release on 2025-12-08; and the [Yew blog](https://yew.rs/blog) carries the 0.22 release post under the handle Mattuwu, "Maintainer of Yew". [Yew](https://github.com/yewstack/yew) itself had 32,760 stars when checked on 2026-07-29, matching the company's "over 32,000" claim. He was scheduled to speak at Anthropic's [Code w/ Claude 2026 Tokyo](https://claude.com/code-with-claude/tokyo) on 2026-06-11.

### Industry domain

- **Japanese enterprise and public-sector procurement.** The company positions itself for listed companies and government bodies, leaning on ISO 27001 and SOC 2 Type 2, publishes a security sheet conforming to METI guidance, and offers a secure-check request through ITreview ([security page](https://www.notta.ai/security)).
- **Recording law.** The English terms put the burden of complying with recording-consent law on the user and note that recording others without prior written consent may be an offence in some jurisdictions ([English terms](https://www.notta.ai/en/terms)).
- **Data residency and AI-training controls.** Japanese data residency is a stated selling point, and the ビジネスPlus plan is defined around an "AI学習なし" (no AI training) setting ([outage notice](https://www.notta.ai/news/info/20251020-aws-outage-impact), [2026-07-27](https://www.notta.ai/news/info/notta-business-plus)).
- **Speech recognition and NLP** are named as the core technical domains in both funding releases; no specific research background is stated as required anywhere.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Open roles | One, as of 2026-07-29: Partner Sales (Hardware). No engineering, product or design role is posted | [recruit page](https://www.notta.ai/recruit) |
| Location | 東京都千代田区大手町1-9-2, moving to 神田神保町 on 2026-08-03. No remote or hybrid policy is stated | [recruit page](https://www.notta.ai/recruit), [relocation notice](https://www.notta.ai/news/info/20260803-office-relocation) |
| Hours | 09:30–18:30, standard working time 7 hours 30 minutes per day with a 90-minute break | [recruit page](https://www.notta.ai/recruit) |
| Days off | Full two-day weekend (Saturday, Sunday and public holidays) | [recruit page](https://www.notta.ai/recruit) |
| Paid leave | 10 days granted on the joining date | [recruit page](https://www.notta.ai/recruit) |
| Insurance | Employees' pension, health, employment and workers' accident insurance | [recruit page](https://www.notta.ai/recruit) |
| Probation | 6 months, during which the employment type is **contract employee (契約社員)**; other conditions stated to be unchanged | [recruit page](https://www.notta.ai/recruit) |
| Application route | A survey form linked from the careers page; careers-specific email is not published | [recruit page](https://www.notta.ai/recruit) |
| Headcount | 100 including global sites, as of end-January 2026; no split by function or location | [company page](https://www.notta.ai/company) |
| Salary, equity, visa sponsorship, turnover, interview process | Not published | [recruit page](https://www.notta.ai/recruit) |

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-29): `www.notta.ai` including `robots.txt`, `sitemap-0.xml` and the company, security, recruit, about, contact, pricing, hardware, integrations, terms and privacy pages in both Japanese and English; the news index and every `/news/info/` and `/news/release/` item in the sitemap; the `app`, `api`, `status`, `developers`, `docs`, `engineering`, `blog` and `tech` subdomains; the `mindcruiser`, `notta`, `notta-ai`, `nottaai` and `langogo` GitHub namespaces and all 26 `mindcruiser` repositories; npm for `notta` and `@notta-labs`; the App Store and Google Play listings and the iTunes lookup API; the National Tax Agency corporate-number registry including change history; PR TIMES releases 35 and 59 under company id 106830; and searches in Japanese and English for Notta funding, Mind Cruiser Limited, NOTTA PTE. LTD., Langogo, and Notta engineering hiring.

- **No engineering blog, technical article, or architecture material.** There is no `engineering`, `tech`, `blog` or `developers` subdomain, and the `/blog` path is a Japanese and English marketing/SEO content operation of several hundred articles, not technical writing.
- **The speech-recognition vendor or model is never named.** The strongest public statement is that Notta selects "the optimal AI speech-recognition engine for each language" ([recruit page](https://www.notta.ai/recruit)); the only named model anywhere is OpenAI GPT-5 for summarization.
- **No public API documentation.** `developers.notta.ai` and `docs.notta.ai` do not resolve, and the English terms reference API access and rate limits without publishing either.
- **No engineering job posting.** One sales role is open. No salary band, equity, visa-sponsorship statement, interview process or turnover figure is published for any role.
- **No CTO or engineering leader is named** on any company surface, and the CPO and CISO the security page describes are not named either.
- **No valuation** has been disclosed for any of the three raises, and the 2022 ¥1.4bn round has no date, name, or investor attached anywhere.
- **The ISO 27001 certificate number, registrar and scope are not published**, and neither the SOC 2 report nor a subprocessor list is available without a form submission; the security sheet is gated behind a lead-capture form.
- **The relationship between the four entities is not stated anywhere.** No company page, release, or filing explains how Ｎｏｔｔａ株式会社, Mind Cruiser Limited and NOTTA PTE. LTD. relate, or why the app bundle identifiers sit in a `com.langogo.*` namespace. The Japanese registry confirms only the Japanese entity.
- **No engineering headcount, location split, or team structure is published.** The single figure is 100 employees "including global sites".
- **No English-language corporate page exists.** `/company` is Japanese-only; `/en/about` is a marketing page with no corporate data, no address, and no leadership.

### Inconsistencies across sources

- **User count, five different figures:** 1.5 million ([recruit page](https://www.notta.ai/recruit)), 2 million downloads (Japanese site footer), 8 million ([Slator, 2025-07-23](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)), 10 million ([PR TIMES, 2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) and the [English about page](https://www.notta.ai/en/about)), and 15 million ([PR TIMES, 2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) and the [Notta Memo page](https://www.notta.ai/hardware/memo)). Several of these are live simultaneously on the company's own site.
- **Company count:** 5,000+ ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html), [Notta Memo page](https://www.notta.ai/hardware/memo)) versus 6,000+ ([English about page](https://www.notta.ai/en/about)) versus 100,000+ clients ([Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)).
- **Hours transcribed:** 30 million+ ([English about page](https://www.notta.ai/en/about)), 10 million ([Notta Memo page](https://www.notta.ai/hardware/memo)), 300 million+ ([Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)).
- **Language coverage:** 58 transcription languages and 42 translation languages ([App Store description](https://itunes.apple.com/lookup?id=1480649572), [Notta Memo page](https://www.notta.ai/hardware/memo)) versus 104 languages ([recruit page](https://www.notta.ai/recruit)).
- **Founding year:** the corporate registry and both funding releases say the company was established 2022-05-25; the company's own timeline says it was founded in 2020 and started the service that May; the App Store shows the iOS app first released 2019-12-19. All three can be true of different things, but no page reconciles them.
- **Governing law depends on the language of the page:** the [Japanese terms](https://www.notta.ai/terms) name Ｎｏｔｔａ株式会社, Japanese law and Tokyo District Court; the [English terms](https://www.notta.ai/en/terms) name "Notta Inc.", Hong Kong law and exclusive jurisdiction in Hong Kong courts.
- **Round naming:** the company calls the May 2025 raise **Series A+** ([PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)); [BRIDGE](https://thebridge.jp/2025/05/notta-a-provider-of-ai-meeting-minutes-services-raises-990-million-yen-in-series-a-funding) calls it Series A; [Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/) reports a US$6.3M round closing 2025-06-30 and names GL Ventures as a co-lead, which the company's release does not mention at all.
- **Address:** the [company page](https://www.notta.ai/company) still shows Otemachi while the PR TIMES company profile and the [relocation notice](https://www.notta.ai/news/info/20260803-office-relocation) give Kanda-Jimbocho from 2026-08-03. The registry's last update is 2025-04-23.
- **"Japanese AI Unicorn"** appears in the headline of the syndicated release covering the 2025 round; no valuation supporting that description has been disclosed by the company or any investor.

### Other

- **The security disclosure is the most detailed part of the public record.** Beyond the certifications, the [security page](https://www.notta.ai/security) documents domestic backup data centres with a DR failover plan, at-rest encryption, SHA-256 password hashing, identity and access controls with audit logging, a CPO/CISO security group, pre-release unit/integration/system testing, and recurring internal security training.
- **The company publishes real incident post-mortems** with detection and recovery timestamps per affected subsystem — unusual for a company of this size, and the clearest available window into its architecture ([2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact), [2026-03-10](https://www.notta.ai/news/info/20260310-incident-report)).
- **GPT-5 summarization is excluded from the Business and Enterprise plans** ([blog, updated 2026-05-15](https://www.notta.ai/blog/notta-gpt5-integration)), so the enterprise tiers run a different summarization path from the consumer tiers.
- **The product line now spans software and two hardware devices** — Notta Memo (¥23,500, on sale 2025-06-16, 28g, four MEMS microphones plus a bone-conduction mic, 32 GB, ~30 hours recording) and the Zenchord 1 AI microphone previewed on Makuake ([Notta Memo page](https://www.notta.ai/hardware/memo)). Hardware is a stated use of funds in both 2025 rounds.
- **The `mindcruiser` GitHub organisation is almost entirely forks of upstream Flutter and Dart packages**, plus a handful of Notta-specific asset repositories and the MCP extension. There is no original open-source library, and the org has 8 followers.
- **The company warned publicly about counterfeit sites** impersonating the official Notta site on [2025-11-11](https://www.notta.ai/news).
- **A GitHub organisation named `Notta-Ai` is a promo-code spam account**, created 2025-05-17 with a single `.github` repository and a name reading "Notta AI Promo Code - 90% Off"; it is unrelated to the company ([GitHub API](https://api.github.com/orgs/notta-ai)).
- **The site is a very large multilingual SEO estate** — the sitemap carries hundreds of blog and tool pages across roughly 20 languages, and `/tools/` and `/translate-audio/` sections dwarf the product pages. `/showcase/`, `/changelog/` and `/landing-page/` are disallowed in [robots.txt](https://www.notta.ai/robots.txt), and the English terms reveal a second product, "Notta Showcase", that has no marketing page.

---

## Resources

**Official**

- [Notta — www.notta.ai](https://www.notta.ai/en) · [Japanese site](https://www.notta.ai/company)
- [会社概要 (corporate information)](https://www.notta.ai/company) · [About (EN)](https://www.notta.ai/en/about) · [Security](https://www.notta.ai/security)
- [採用情報 (careers)](https://www.notta.ai/recruit) · [Pricing](https://www.notta.ai/en/pricing)
- [Notta Memo hardware page, including the company timeline](https://www.notta.ai/hardware/memo)
- [利用規約 — Japanese terms](https://www.notta.ai/terms) · [Terms of Service — English](https://www.notta.ai/en/terms) · [Privacy Policy — English](https://www.notta.ai/en/privacy)
- [新着情報 (news index)](https://www.notta.ai/news) · [sitemap](https://www.notta.ai/sitemap-0.xml) · [robots.txt](https://www.notta.ai/robots.txt)
- [Notta Desktop release, 2026-07-08](https://www.notta.ai/news/release/notta-desktop)
- [Notta Brain new features, 2026-06-17](https://www.notta.ai/news/release/notta-brain-new-features)
- [Development team strengthening, 2026-06-10](https://www.notta.ai/news/info/ai-agent-era-development-enhancement)
- [ビジネスPlus plan, 2026-07-27](https://www.notta.ai/news/info/notta-business-plus) · [Office relocation, 2026-07-27](https://www.notta.ai/news/info/20260803-office-relocation) · [Kochi Bank, 2026-06-25](https://www.notta.ai/news/info/kochi-bank) · [Price change, 2025-06-16](https://www.notta.ai/news/info/2025-06-16-price-changed)
- [AWS outage impact notice, 2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact) · [Login incident report, 2026-03-10](https://www.notta.ai/news/info/20260310-incident-report)
- [GPT-5 integration article, updated 2026-05-15](https://www.notta.ai/blog/notta-gpt5-integration)
- [Status page](https://status.notta.ai/)
- [GitHub — mindcruiser organisation](https://api.github.com/orgs/mindcruiser) · [repositories](https://api.github.com/orgs/mindcruiser/repos) · [notta-mcp](https://github.com/mindcruiser/notta-mcp) · [mc_flutter_recorder](https://github.com/mindcruiser/mc_flutter_recorder)
- [npm — notta packages](https://registry.npmjs.org/-/v1/search?text=notta)
- [App Store metadata — iTunes lookup API](https://itunes.apple.com/lookup?id=1480649572) · [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe)
- [Ranee Zhang — VP of Growth author page](https://www.notta.ai/en/author/ranee-zhang)

**Press releases**

- [Notta、Granite-Integral Capitalから23億円のシリーズB資金調達を実施 — 2025-12-09 (JA)](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)
- [AI議事録サービス提供のＮｏｔｔａ株式会社 シリーズA+総額9億9000万円の資金調達を実施 — 2025-05-29 (JA)](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)

**Third-party coverage and profiles**

- [国税庁法人番号公表サイト — Ｎｏｔｔａ株式会社, corporate number 5010001226919, with address change history (JA)](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919)
- [BRIDGE — Notta raises ¥2.3bn Series B, 2025-12 (EN)](https://thebridge.jp/en/2025/12/notta-provider-of-ai-transcription-tools-raises-%C2%A52-3-billion-in-series-b-from-granite-integral-capital)
- [BRIDGE — シリーズAラウンド9億9,000万円を調達, 2025-05 (JA)](https://thebridge.jp/2025/05/notta-a-provider-of-ai-meeting-minutes-services-raises-990-million-yen-in-series-a-funding)
- [Slator — Transcription startup Notta raises USD 6.3M to bring standalone recorder to the US, 2025-07-23](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)
- [The SaaS News — Notta raises ¥2.3 billion in Series B](https://www.thesaasnews.com/news/notta-raises-2-3-billion-in-series-b)
- [Nikkei Asia — Chinese tech entrepreneur bets big on Japan, but not China, 2023-03-29](https://asia.nikkei.com/business/china-tech/chinese-tech-entrepreneur-bets-big-on-japan-but-not-china)
- [Yew — GitHub repository, the framework the company's named engineer maintains](https://github.com/yewstack/yew) · [Yew blog](https://yew.rs/blog) · [Madoshakalaka / Siyuan Yan on GitHub](https://github.com/Madoshakalaka)
- [Anthropic — Code w/ Claude 2026 Tokyo](https://claude.com/code-with-claude/tokyo)

**Listed to prevent misattribution**

- [GitHub organisation `Notta-Ai` — an unrelated promo-code account](https://api.github.com/orgs/notta-ai)
