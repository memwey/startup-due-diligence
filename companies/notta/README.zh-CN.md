# Notta

[English](README.md) | **简体中文**

> 基于公开信息整理的研究笔记。最后更新：2026-07-29。同步至：2026-07-29。
> 每个数字都链接到出处并标注日期。在依赖这些信息前请对照一手来源核实。

## 摘要

Notta 是一款 AI 转写与会议记录产品——覆盖 Web 应用、iOS 与 Android 应用、Chrome 扩展、桌面端以及一款硬件录音笔——主要面向日本市场销售，并正在向美国拓展（[会社概要](https://www.notta.ai/company)；访问于 2026-07-29）。日本运营主体 **Ｎｏｔｔａ株式会社** 设立于 2022-05-25，法人番号 5010001226919（[国税庁法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919)），但公司自述的创业时间是 2020 年，而 iOS 应用早在 2019-12-19 就已上架（[公司沿革](https://www.notta.ai/hardware/memo)、[iTunes API](https://itunes.apple.com/lookup?id=1480649572)）。CEO 是 Ryan Zhang。

- **融资：** 2022 年累计融资 14 亿日元（[公司沿革](https://www.notta.ai/hardware/memo)）；[2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) 公司自称的 **シリーズA+（Series A+）** 轮 9.9 亿日元；[2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) 由 Granite-Integral Capital 领投的 **Series B** 23 亿日元（1,500 万美元）。
- **公司口径的规模：** 截至 [2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) 为 5,000 家企业、1,500 万用户；截至 [2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)，日经 225 成分股中 72% 在使用，企业用户同比增长 300%。员工人数为 100 名（含全球据点），截至 2026 年 1 月底（[会社概要](https://www.notta.ai/company)）。
- **安全披露程度在同规模公司里相当罕见：** ISO 27001，SOC 2 Type 1 于 2022-09-29 取得、Type 2 于 2023-02-12 取得，另声明符合 HIPAA/GDPR/APPI/CCPA，并设有 CPO 与 CISO 岗位（[安全页面](https://www.notta.ai/security)）。
- **技术栈主要可从 `mindcruiser` GitHub 组织还原：** Flutter/Dart 移动端（Firebase、`dio`、`drift`/`floor`、`just_audio`、`flutter_quill`、用于硬件录音笔的 `flutter_blue_classic`，以及自研的 `mc_flutter_recorder` 插件），AWS 且客户数据存放在日本区域，另有一个官方的 [Claude Desktop MCP 服务器](https://github.com/mindcruiser/notta-mcp)。摘要功能跑在 OpenAI GPT-5 上，但[在商务版与企业版上并不启用](https://www.notta.ai/blog/notta-gpt5-integration)。
- **四个法律主体共用同一个品牌。** 日文条款写明主体为 Ｎｏｔｔａ株式会社，适用日本法、东京地方法院管辖；[英文条款](https://www.notta.ai/en/terms) 写的是 "Notta Inc."，适用**香港**法、香港法院专属管辖。iOS 应用由 **Mind Cruiser Limited**（香港）发布，Android 应用由 **NOTTA PTE. LTD.**（新加坡）发布，而两个应用的包名都落在 `com.langogo.*` 命名空间下。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | Notta | [会社概要](https://www.notta.ai/company) |
| 法定名称（日本） | Ｎｏｔｔａ株式会社；英文材料中写作 "Notta Inc." | [会社概要](https://www.notta.ai/company)、[英文条款](https://www.notta.ai/en/terms) |
| 法人番号 | 5010001226919；合规发票登记号 T5010001226919 | [国税庁法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919)、[会社概要](https://www.notta.ai/company) |
| 设立时间 | 2022-05-25（法人番号指定日 2022-05-27）；而公司自己的沿革写创业于 2020 年、当年 5 月上线移动端 | [会社概要](https://www.notta.ai/company)、[国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919)、[公司沿革](https://www.notta.ai/hardware/memo) |
| 代表人 | Ryan Zhang，代表取締役 | [会社概要](https://www.notta.ai/company) |
| 注册资本 | 900 万日元 | [会社概要](https://www.notta.ai/company) |
| 地址 | 〒100-0004 東京都千代田区大手町1-9-2 大手町フィナンシャルシティグランキューブ3階，将于 2026-08-03 迁至 〒101-0051 東京都千代田区神田神保町1-13 J.NODE神保町4階 | [会社概要](https://www.notta.ai/company)、[迁址公告，2026-07-27](https://www.notta.ai/news/info/20260803-office-relocation) |
| 注册地址变更史 | 2023-07-14 由 中央区日本橋1-2-10 東洋ビル5階 变更；2025-04-21 由 渋谷区道玄坂1-12-1 渋谷マークシティW22階 变更 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919) |
| 电话 | 03-6820-6068 | [会社概要](https://www.notta.ai/company) |
| 员工人数 | 100 名"含全球据点"，截至 2026 年 1 月底 | [会社概要](https://www.notta.ai/company) |
| 客户 | 5,000 家企业、1,500 万用户 | [Series B 新闻稿，2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |
| 认证 | ISO 27001；SOC 2 Type 1（2022-09-29）与 Type 2（2023-02-12） | [安全页面](https://www.notta.ai/security) |
| 累计融资 | 14 亿日元（2022）+ 9.9 亿日元（2025-05）+ 23 亿日元（2025-12） | [公司沿革](https://www.notta.ai/hardware/memo)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |
| 工程团队工作语言 | 未说明。招聘页、公司页与新闻均以日文为主；产品与文案覆盖 20 种语言 | [採用情報](https://www.notta.ai/recruit)、[会社概要](https://www.notta.ai/company) |
| 联系方式 | contact@notta.ai（媒体）、support@notta.ai | [会社概要](https://www.notta.ai/company)、[故障报告](https://www.notta.ai/news/info/20260310-incident-report) |
| 公关代理 | サニーサイドアップ（Sunny Side Up）负责媒体对接 | [PR TIMES，2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) |

公司还声明其取得了全国社会保险劳务士会联合会的『職場環境改善宣言企業』认证（[会社概要](https://www.notta.ai/company)），并列出 2024 年与 ダイワボウ情報システム、SBC&S 签署的分销协议，以及 2024 Fall 与 2025 Winter 两期 ITreview Grid Award 三个类别的 "Leader" 入选（[公司沿革](https://www.notta.ai/hardware/memo)）。

### 品牌与法律实体

四个主体外加一个遗留命名空间共用 Notta 这个品牌。用户实际与哪一个签约，取决于他打开的是哪种语言的页面。

| 名称 | 类型 | 角色 | 来源 |
|---|---|---|---|
| Ｎｏｔｔａ株式会社 | 日本株式会社 | 日文条款中写明的服务提供方，约定适用日本法、以东京地方法院为第一审专属合意管辖法院 | [日文利用规约第 22 条](https://www.notta.ai/terms) |
| "Notta Inc." | 英文材料中使用的名称 | 英文条款中写明的服务提供方，约定适用**香港**法、香港法院专属管辖 | [英文条款](https://www.notta.ai/en/terms) |
| Mind Cruiser Limited | 香港公司 | iOS 应用的发布方；同时也是 [`mindcruiser` GitHub 组织](https://github.com/mindcruiser)的所有者，该组织地点写日本、链接指向 notta.ai | [iTunes API](https://itunes.apple.com/lookup?id=1480649572)、[GitHub 组织](https://api.github.com/orgs/mindcruiser) |
| NOTTA PTE. LTD. | 新加坡公司 | Android 应用的发布方；开发者地址写作 c/o Tricor Singapore, 9 Raffles Place #26-01 Republic Plaza | [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |
| `com.langogo.*` | 应用命名空间 | iOS 包名为 `com.langogo.lggtranscribe`，Android 包名为 `com.langogo.transcribe`，指向一段以 Langogo 为品牌的更早期渊源，而当前任何 Notta 页面都未加以说明 | [iTunes API](https://itunes.apple.com/lookup?id=1480649572)、[Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |

日本主体可在国家登记系统中核验，包括其地址变更史。截至 2026-07-29，没有任何备案、新闻稿或公司页面说明 Ｎｏｔｔａ株式会社、Mind Cruiser Limited 与 NOTTA PTE. LTD. 三者之间的持股关系，也没有解释 Langogo 命名空间的由来，见`备注`。

---

## 产品

### 各端形态

| 端 | 详情 | 来源 |
|---|---|---|
| Web 应用 | `app.notta.ai`；市场站点是 Gatsby 静态构建，托管在 Amazon S3 上、前置 CloudFront | [响应头](https://www.notta.ai/en)，访问于 2026-07-29 |
| iOS | "Notta-自動文字起こし" / "Notta Transcribe Voice to Text"，包名 `com.langogo.lggtranscribe`，首次发布 2019-12-19，版本 6.76.16 发布于 2026-07-20，最低 iOS 13.0，21 种本地化 | [iTunes API](https://itunes.apple.com/lookup?id=1480649572) |
| Android | "Notta-Transcribe Audio to Text"，包名 `com.langogo.transcribe`，100 万以上下载区间，更新于 2026-07-18 | [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |
| Chrome 扩展 | 对网页中播放的音频做转写 | [会社概要](https://www.notta.ai/company) |
| 桌面端 | Nottaデスクトップ，支持 Windows 与 macOS（Intel 与 Apple Silicon），2026-07-08 发布 | [发布稿，2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| 硬件 | Notta Memo AI 录音笔，2025-06-16 开售，含税 23,500 日元，通过 Amazon 销售；Zenchord 1 AI 麦克风在 Makuake 先行公开 | [Notta Memo 页面](https://www.notta.ai/hardware/memo)、[公司沿革](https://www.notta.ai/hardware/memo) |

### 核心能力

转写精度对外称 **98.86%、支持 58 种语言**，具备自动说话人识别、翻译至 42 种语言、屏幕录制、多端同步、播放时 AI 降噪、团队工作区与 AI 摘要（[App Store 描述](https://itunes.apple.com/lookup?id=1480649572)、[Notta Memo 页面](https://www.notta.ai/hardware/memo)）。而招聘页写的是覆盖 **104 种语言**，并"按语言使用最合适的 AI 语音识别引擎"（[採用情報](https://www.notta.ai/recruit)）——这是关于识别侧并非单一自研模型的最明确的公开表述。

**Notta Brain** 是其 AI 平台层，2026-01-30 正式发布，并在 2026-03-30 吸收了原有的"AI 聊天"功能。它基于已保存的录音、转写文本与上传资料，做摘要、跨多场会议的横向分析、生成幻灯片与图片、按评分标准给面试或商谈打分，并支持实时提问。[2026-06-17](https://www.notta.ai/news/release/notta-brain-new-features) 新增了定时执行的"定例任务"、Slack 机器人与 LINE 机器人，另有面向部分个人用户 beta 的目的导向 AI 工具。

**Nottaデスクトップ**（[2026-07-08](https://www.notta.ai/news/release/notta-desktop)）提供了云端产品做不到的两件事：**隐私模式**，全部 AI 处理在用户本机完成，音频与转写文本一律不上传；以及**无机器人录音**，直接采集 PC 系统音频，而不是往 Zoom、Teams 或 Google Meet 里派驻会议记录机器人。该产品面向高级版、商务版与企业版提供，其中隐私模式对发票结算客户需经销售单独开通。

### 集成

已公开 23 项集成：Zoom、Microsoft Teams、Google Meet、Webex；Google 日历与 Outlook 日历；Google Docs、Google Drive、Microsoft OneDrive、OneNote、SharePoint、Box、Dropbox、Notion；Salesforce、HubSpot、Pipedrive、Zoho CRM、Zendesk Sell、Salesflare、Freshsales；kintone、ClickUp、Slack、Zapier（[站点地图](https://www.notta.ai/sitemap-0.xml)）。2025 年 AWS 故障公告中另点名了 Autodesk 的授权集成（[2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact)）。

### 商业模式

订阅制 SaaS，按转写分钟数计量，另有增值包与硬件线。2026-07-29 页面展示的年付价格如下（[定价页](https://www.notta.ai/en/pricing)）：

| 套餐 | 价格（年付） | 转写额度 | 单次时长上限 | 主要差异 |
|---|---|---|---|---|
| 免费版 | 0 日元 | 每月 120 分钟、50 次文件上传、10 次 AI 摘要 | 3 分钟 | 1 个席位，无需信用卡 |
| Pro | 1,185 日元/月（14,220 日元/年） | 每月 1,800 分钟、100 次上传、100 次摘要 | 5 小时 | 导出、翻译、自定义词汇 |
| 商务版 | 2,508 日元/月/席（30,096 日元/年） | 不限量、200 次上传、200 次摘要 | 5 小时 | 会议视频录制、使用报告、CRM 与 Zapier |
| 企业版 | 定制，51 席起 | 定制，上传与摘要不限量 | 5 小时 | SAML SSO、审计日志、完整数据访问控制、教育 5 折 |
| ビジネスPlus（日本，2026-07-27 起） | 9,000 日元/月/席，64,800 日元/年/席（不含税） | 商务版功能加 Notta Brain 全部功能 | — | "无 AI 学习"设置、每月 8,000 积分、图片与幻灯片生成、实时摘要、定例任务 |

面向 Pro、商务版与企业版用户单独售卖的增值包：单语翻译年付 858 日元/月（月付 1,430 日元）、双语转写与翻译年付 1,320 日元/月（月付 2,200 日元）、Notta Brain 14,300 日元/年含每月 8,000 AI 积分（[定价页](https://www.notta.ai/en/pricing)）。公司曾公告一次自 2025-06-16 起的[价格调整](https://www.notta.ai/news/info/2025-06-16-price-changed)。

### 各时期披露的规模

| 日期 | 披露数字 | 来源 |
|---|---|---|
| 2019-12-19 | iOS 应用首次发布 | [iTunes API](https://itunes.apple.com/lookup?id=1480649572) |
| 2020 | 公司把创业时间定在此年；5 月移动端服务上线 | [公司沿革](https://www.notta.ai/hardware/memo) |
| 2022 | 累计融资 14 亿日元；取得 SOC 2 Type II | [公司沿革](https://www.notta.ai/hardware/memo) |
| 2022-09-29 / 2023-02-12 | 先取得 SOC 2 Type 1 报告，后取得 Type 2 报告 | [安全页面](https://www.notta.ai/security) |
| 2025-05-29 | 1,000 万用户；企业用户同比增长 300%；日经 225 中 72% 在使用 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) |
| 2025-06-16 | Notta Memo 硬件开售，23,500 日元 | [Notta Memo 页面](https://www.notta.ai/hardware/memo) |
| 2025-07-23 | 800 万以上用户、10 万以上客户、处理 3 亿以上小时；硬件在美国定价 149 美元 | [Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/) |
| 2025-12-09 | 5,000 家企业、1,500 万用户 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |
| 访问于 2026-07-29 | 英文站：1,000 万以上用户、6,000 家以上企业、3,000 万以上小时转写 | [About 页面](https://www.notta.ai/en/about) |
| 访问于 2026-07-29 | Notta Memo 页面：累计 1,500 万用户、5,000 家以上企业、1,000 万小时转写 | [Notta Memo 页面](https://www.notta.ai/hardware/memo) |
| 访问于 2026-07-29 | 招聘页："超过 150 万用户"；日文站页脚："200 万下载突破" | [採用情報](https://www.notta.ai/recruit)、[会社概要](https://www.notta.ai/company) |
| 访问于 2026-07-29 | iOS 日区：25,968 条评分、均分 4.35；iOS 美区：1,374 条、均分 4.05；Google Play 100 万以上下载 | [iTunes API](https://itunes.apple.com/lookup?id=1480649572)、[Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe) |

### 已公布的客户与合作方

| 日期 | 对象 | 内容 |
|---|---|---|
| 2024 | ダイワボウ情報システム、SBC&S | 面向日本渠道的分销协议（[公司沿革](https://www.notta.ai/hardware/memo)） |
| [2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) | Granite-Integral Capital | Series B 领投方；投资人称 Notta 体现了其 "Japan Nexus" 主张 |
| [2026-06-25](https://www.notta.ai/news/info/kochi-bank) | 高知銀行 | 地方银行导入 |
| [2025-11-27](https://www.notta.ai/news) | オープンハウス・アーキテクト | 就 AI 议事录市场共同举办圆桌 |

### 公司自述的规划

Series A+ 新闻稿列出三项资金用途：加速硬件生态建设、集中投入语音识别与自然语言处理、大幅扩充日本法人客户的销售与支持体系（[2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)）。Series B 新闻稿则收敛为面向企业业务扩张的人才招聘，以及软硬件双线的语音 AI 开发（[2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)）。CEO 把美国描述为下一个市场，理由是它是全球最大的 SaaS 与 AI 生产力工具市场（[Slator，2025-07-23](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)）。产品侧，2026-06-10 的公告称公司正在为"AI 智能体时代"强化 AI 产品开发、Web 应用基础设施与用户体验设计（[2026-06-10](https://www.notta.ai/news/info/ai-agent-era-development-enhancement)）。

---

## 创始人

| 姓名 | 职位 | 来源陈述的履历事实 | 来源 |
|---|---|---|---|
| Ryan Zhang | 代表取締役 / 创始人兼 CEO | 来自中国的连续创业者，做过多款应用，选择在中国以外发展；其语音转文字应用在日本取得成功，且未在中国提供 | [日经亚洲，2023-03-29](https://asia.nikkei.com/business/china-tech/chinese-tech-entrepreneur-bets-big-on-japan-but-not-china)、[会社概要](https://www.notta.ai/company) |

Ryan Zhang 在两轮融资新闻稿以及公司页面所引的法人登记信息中都被列为代表取締役。他著有《VOICE TO PROFIT》一书，[2025-11-04](https://www.notta.ai/news) 在 Amazon 开启预售。截至 2026-07-29 所查阅的来源中，没有任何联合创始人被点名。

### 主要管理层

| 姓名 | 职位 | 来源 |
|---|---|---|
| Ranee Zhang | 增长副总裁 | [notta.ai 上的作者页](https://www.notta.ai/en/author/ranee-zhang) |
| CPO 与 CISO | 安全页面称公司设有由高管构成的安全小组，含首席隐私官与首席信息安全官；均未具名 | [安全页面](https://www.notta.ai/security) |

Notta 任何页面都未点名 CTO、工程副总裁或工程经理。唯一被具名的技术员工是一位软件工程师——见`工程`。

---

## 融资

| 日期 | 轮次 | 金额 | 披露的投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2022 | 未命名 | 累计 14 亿日元 | 未披露 | 14 亿日元 | [公司沿革](https://www.notta.ai/hardware/memo) |
| 2025-05-29 | **シリーズA+（Series A+）** | 9.9 亿日元 | Mizuho Leaguer Investment 与 GSR Ventures 新进入股，既有投资方追加 | 约 23.9 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) |
| 2025-12-09 | **Series B** | 23 亿日元（1,500 万美元） | 由 Granite-Integral Capital Pte. Ltd.（新加坡；共同负责人 CK Chuon、Joe Yan）领投 | 约 46.9 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) |

任何一轮都未披露估值。2022 年那笔融资只以一行文字出现在公司自己的沿革里，没有轮次名、日期或投资方。

2025 年 5 月这一轮的轮次命名在各来源之间不一致：公司称之为 **Series A+**（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)），[BRIDGE](https://thebridge.jp/2025/05/notta-a-provider-of-ai-meeting-minutes-services-raises-990-million-yen-in-series-a-funding) 报道为 Series A，[Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/) 则写作一笔 630 万美元、于 2025-06-30 交割的融资，并点名 GL Ventures 为联合领投——领投方与交割日期都是公司自己的新闻稿中没有的，同时给出累计融资"超过 1,600 万美元"，这与 14 亿日元加 9.9 亿日元吻合，但与公司公布的任何数字都不对应。

Series B 新闻稿把 Granite-Integral Capital 描述为 **Granite Asia** 与 **Integral Globaltech Partners**（成立于 2025 年，インテグラル株式会社的子公司）的合资事业，运作一支 1 亿美元规模的成长基金；Granite Asia 被称在亚太管理 50 亿美元（[PR TIMES，2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)）。

---

## 工程

### 技术栈与平台

由公开资产确认——`mindcruiser` GitHub 组织、npm、HTTP 响应头，以及公司自己的故障与发布公告（均访问于 2026-07-29）：

| 项目 | 内容 | 证据 |
|---|---|---|
| 云 | AWS。客户音频与转写数据被声明全部存放在日本区域；部分服务依赖 `us-east-1`，并在 2025-10-20 的故障中受影响 | [故障公告，2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact) |
| 市场站点 | Gatsby 静态构建（`/page-data/` 路由），托管于 Amazon S3 并启用 `INTELLIGENT_TIERING`，前置 CloudFront | [响应头](https://www.notta.ai/en)、[robots.txt](https://www.notta.ai/robots.txt) |
| 移动端 | Flutter / Dart。该组织 fork 了 `just_audio`、`flutter_file_picker`、`uni_links`、`app_links`、`share_handler`、`flutter_quill`、`dio`、`drift`、`floor`、`flutter_keychain`、`plus_plugins`、`flutterfire` 与 `aad_oauth` | [GitHub 组织仓库](https://api.github.com/orgs/mindcruiser/repos) |
| 自研移动插件 | `mc_flutter_recorder`，一个用于录音的 Swift Flutter 插件，创建于 2023-01-05 | [GitHub](https://github.com/mindcruiser/mc_flutter_recorder) |
| 硬件连接 | 2024-10-16 fork 的 `flutter_blue_classic`（经典蓝牙插件）；Notta Memo 通过蓝牙或 Wi-Fi 把录音传给 App | [GitHub 组织仓库](https://api.github.com/orgs/mindcruiser/repos)、[Notta Memo 页面](https://www.notta.ai/hardware/memo) |
| 身份认证 | 通过 `aad_oauth` 支持 Azure AD OAuth；企业版提供 SAML SSO；支持 Apple、Google、Microsoft 第三方登录 | [GitHub 组织仓库](https://api.github.com/orgs/mindcruiser/repos)、[定价页](https://www.notta.ai/en/pricing)、[隐私政策](https://www.notta.ai/en/privacy) |
| 会话录制 | 2024-07-05 fork 的 `rrweb`（"record and replay the web"） | [GitHub 组织仓库](https://api.github.com/orgs/mindcruiser/repos) |
| Web 静态资源 | `notta-web-icon`（2026-07-24 有推送）与 `notta-web-static-files-storage`，后者自述为 Notta Web 项目的 CDN 静态文件仓库 | [GitHub 组织仓库](https://api.github.com/orgs/mindcruiser/repos) |
| 摘要模型 | OpenAI **GPT-5**，已集成进 AI 摘要功能；但在商务版与企业版上**不启用** | [博客，更新于 2026-05-15](https://www.notta.ai/blog/notta-gpt5-integration) |
| 语音识别 | 未点名。招聘页称 Notta"按语言使用最合适的 AI 语音识别引擎"——即按语言选路而非单一模型 | [採用情報](https://www.notta.ai/recruit) |
| 端侧推理 | Nottaデスクトップ的隐私模式把全部 AI 处理放在用户本机的 Windows 或 macOS 上完成，零外发 | [发布稿，2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| 智能体接口 | npm 上的 `@notta-labs/notta-mcp` 与 `@notta-labs/notta-cli`（创建于 2026-04-14，最新 2026-06-18），以及 [notta-mcp](https://github.com/mindcruiser/notta-mcp) 仓库：一个本地 stdio MCP 服务器，打包为 `.mcpb` 的 Claude Desktop 扩展，基于 `@modelcontextprotocol/sdk`、`@aws-sdk/client-s3` 与 `zod` | [npm](https://registry.npmjs.org/-/v1/search?text=notta)、[GitHub](https://github.com/mindcruiser/notta-mcp) |
| MCP 服务器的凭据处理 | OAuth 流程把凭据写入 `~/.config/notta_cli/credentials.json`，目录权限 `0700`、文件权限 `0600`；临时 S3 上传凭据只保存在内存中；`transcribe` 工具拒绝白名单目录之外的路径、超过 2 GB 的文件与超过 4 小时的录音 | [notta-mcp README](https://github.com/mindcruiser/notta-mcp) |
| 口令存储 | 安全页面称口令使用 SHA-256 哈希，明文口令既不传输也不存储；存储的音频、图片与文本数据默认加密 | [安全页面](https://www.notta.ai/security) |
| 备份与灾备 | 定期备份存放在日本国内数据中心，制定了灾难恢复计划，可切换到备用系统或备用数据中心 | [安全页面](https://www.notta.ai/security) |
| 内部办公工具 | Google Workspace、Slack、Airtable、Notion、HubSpot | [採用情報](https://www.notta.ai/recruit) |

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 转写流水线 | 实时录音与文件转写，按语言选择引擎，说话人识别，自定义词汇，播放时 AI 降噪 | [App Store 描述](https://itunes.apple.com/lookup?id=1480649572)、[採用情報](https://www.notta.ai/recruit) |
| 会议机器人派遣 | 加入 Zoom、Teams、Google Meet 与 Webex 会议进行录音转写的机器人；配有热备环境，在 2025 年 AWS 故障中 28 分钟内完成切换 | [故障公告，2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact)、[定价页](https://www.notta.ai/en/pricing) |
| 无机器人桌面采集 | 直接采集 PC 系统音频，参会者名单中不会出现额外成员 | [发布稿，2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| 本地推理运行时 | Nottaデスクトップ隐私模式下完全在端侧完成转写与 AI 处理 | [发布稿，2026-07-08](https://www.notta.ai/news/release/notta-desktop) |
| Notta Brain | 在已保存录音、转写文本与上传资料之上做检索与分析；跨会议横向分析、生成幻灯片与图片、按评分标准打分、实时摘要、定例任务、Slack 与 LINE 机器人 | [发布稿，2026-06-17](https://www.notta.ai/news/release/notta-brain-new-features) |
| 日历与自动化 | 从日历条目安排会议；由 Google Drive 触发的自动化 | [故障公告，2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact)、[定价页](https://www.notta.ai/en/pricing) |
| 硬件同步 | Notta Memo 用 32 GB 内置存储保存录音，通过蓝牙（小文件）或 Wi-Fi（大文件）传给 App，随后自动生成笔记 | [Notta Memo 页面](https://www.notta.ai/hardware/memo) |
| MCP 服务器 | 让 Claude Desktop 上传本地音视频做转写，并列出、搜索、轮询与读取 Notta 记录 | [notta-mcp](https://github.com/mindcruiser/notta-mcp) |
| 监控 | 安全页面描述了对数据处理性能的实时跟踪，覆盖流量、处理时长与错误率指标并设有告警；`status.notta.ai` 提供公开状态页 | [安全页面](https://www.notta.ai/security)、[status.notta.ai](https://status.notta.ai/) |

公司公开了两份故障通告，且都相当具体。[2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact) 逐项列出了 AWS `us-east-1` 故障影响了哪些功能、各自何时恢复——SSO 登录（16:42 发现，18:22 恢复）、会议机器人派遣（15:52 发现，16:20 完成热备切换）、Autodesk／Slack／Zoom 授权与 Google Drive 自动化（16:32 发现，18:55 恢复）——并说明日历同步、非机器人转写、Zapier、商店与支付、AI 相关功能未受影响。[2026-03-10](https://www.notta.ai/news/info/20260310-incident-report) 一次持续 4 小时 20 分钟、对本地缓存过期用户与新登录用户返回 HTTP 500 的登录故障，被定位为 Web 应用中某个第三方软件组件由外部提供方推送更新所致，通过停用该组件恢复。

### 招聘所需技术背景

没有任何工程岗位在招。截至 2026-07-29，[招聘页](https://www.notta.ai/recruit)只列出一个职位——**パートナーセールス（ハードウェア）**，要求 3 年以上法人销售经验、硬件或 IT 产品销售经验、渠道/代理销售经验，以及被描述为"使用 Mac、会用各类 AI 工具"的基础 IT 素养。加分项：SaaS 销售、AI/语音识别领域销售、渠道伙伴管理、新业务从零起步经验，以及英语或中文的商务沟通能力。

关于工程门槛，唯一的公开表述是一则入职公告而非岗位描述。[2026-06-10](https://www.notta.ai/news/info/ai-agent-era-development-enhancement) 公司宣布软件工程师 **Yan Siyuan（Matt）** 加入开发团队，负责 Notta Brain 的智能体体验与产品开发基础设施。其被陈述的背景——Rust/WebAssembly 前端框架 **Yew** 的维护者之一，主导了近期主要版本，并且是 **gloo** 的协作者与包所有者——可与一手记录相互印证：GitHub 账号 [Madoshakalaka](https://github.com/Madoshakalaka) 的姓名写作 Siyuan Yan、公司 Notta、地点东京，简介为 "Call me Matt too. Maintainer at @yewstack"；该账号于 2025-12-08 发布了 `yew-v0.22.0`；[Yew 博客](https://yew.rs/blog)上 0.22 的发布文章署名 Mattuwu，"Maintainer of Yew"。2026-07-29 查询时 [Yew](https://github.com/yewstack/yew) 有 32,760 颗星，与公司"超过 3 万 2,000"的说法相符。他还预定于 2026-06-11 在 Anthropic 的 [Code w/ Claude 2026 Tokyo](https://claude.com/code-with-claude/tokyo) 上演讲。

### 行业领域

- **日本企业与公共部门采购。** 公司把自己定位给上市公司与政府自治体，倚重 ISO 27001 与 SOC 2 Type 2，提供符合经产省规定的安全检查表，并可通过 ITreview 发起安全审查请求（[安全页面](https://www.notta.ai/security)）。
- **录音相关法律。** 英文条款把遵守录音告知与同意义务的责任放在用户身上，并提示在部分司法辖区未经事先书面同意录制他人可能构成违法（[英文条款](https://www.notta.ai/en/terms)）。
- **数据驻留与 AI 训练控制。** 日本境内数据驻留是其对外强调的卖点，而 ビジネスPlus 套餐正是围绕"AI学習なし"（不用于 AI 训练）这一设置定义的（[故障公告](https://www.notta.ai/news/info/20251020-aws-outage-impact)、[2026-07-27](https://www.notta.ai/news/info/notta-business-plus)）。
- **语音识别与自然语言处理**在两轮融资新闻稿中都被列为核心技术方向；任何地方都没有把某种具体研究背景列为硬性要求。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 在招岗位 | 截至 2026-07-29 共一个：パートナーセールス（ハードウェア）。没有任何工程、产品或设计岗位 | [採用情報](https://www.notta.ai/recruit) |
| 地点 | 東京都千代田区大手町1-9-2，2026-08-03 迁至神田神保町。未说明远程或混合办公政策 | [採用情報](https://www.notta.ai/recruit)、[迁址公告](https://www.notta.ai/news/info/20260803-office-relocation) |
| 工作时间 | 09:30–18:30，标准劳动时间每日 7 小时 30 分，休息 90 分钟 | [採用情報](https://www.notta.ai/recruit) |
| 休息日 | 完全双休（周六、周日及法定节假日） | [採用情報](https://www.notta.ai/recruit) |
| 带薪假 | 入职当日授予 10 天 | [採用情報](https://www.notta.ai/recruit) |
| 社会保险 | 厚生年金、健康保险、雇用保险、劳灾保险齐备 | [採用情報](https://www.notta.ai/recruit) |
| 试用期 | 6 个月，期间雇佣形态为**契约社员（契約社員）**；其余雇佣条件称不变 | [採用情報](https://www.notta.ai/recruit) |
| 投递渠道 | 招聘页上链接的一份问卷表单；未公布招聘专用邮箱 | [採用情報](https://www.notta.ai/recruit) |
| 员工人数 | 100 名含全球据点，截至 2026 年 1 月底；未按职能或地点拆分 | [会社概要](https://www.notta.ai/company) |
| 薪资、股权、签证支持、流失率、面试流程 | 未公开 | [採用情報](https://www.notta.ai/recruit) |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-29）：`www.notta.ai`，含 `robots.txt`、`sitemap-0.xml`，以及日文与英文两版的公司、安全、招聘、about、contact、定价、硬件、集成、条款与隐私页面；新闻索引及站点地图中全部 `/news/info/` 与 `/news/release/` 条目；`app`、`api`、`status`、`developers`、`docs`、`engineering`、`blog`、`tech` 子域名；`mindcruiser`、`notta`、`notta-ai`、`nottaai`、`langogo` 等 GitHub 命名空间与 `mindcruiser` 的全部 26 个仓库；npm 上的 `notta` 与 `@notta-labs`；App Store 与 Google Play 页面及 iTunes lookup API；国税庁法人番号公表サイト含变更履历；PR TIMES 公司 id 106830 下的第 35 与第 59 号新闻稿；以及围绕 Notta 融资、Mind Cruiser Limited、NOTTA PTE. LTD.、Langogo 与 Notta 工程招聘的中日英文检索。

- **没有工程博客、技术文章或架构材料。** 不存在 `engineering`、`tech`、`blog` 或 `developers` 子域名，`/blog` 路径是一套数百篇规模的日英市场／SEO 内容，而不是技术写作。
- **从未点名语音识别供应商或模型。** 最强的公开表述是 Notta"按语言使用最合适的 AI 语音识别引擎"（[採用情報](https://www.notta.ai/recruit)）；全站唯一被点名的模型是用于摘要的 OpenAI GPT-5。
- **没有公开 API 文档。** `developers.notta.ai` 与 `docs.notta.ai` 无法解析，而英文条款却提到了 API 访问与速率限制。
- **没有任何工程岗位在招。** 在招的是一个销售岗。任何岗位都未公布薪资区间、股权、签证支持说明、面试流程或流失率。
- **任何公司页面都未点名 CTO 或工程负责人**，安全页面所描述的 CPO 与 CISO 同样没有具名。
- **三轮融资均未披露估值**，2022 年那笔 14 亿日元也没有日期、轮次名或投资方。
- **ISO 27001 的证书编号、认证机构与适用范围未公开**，SOC 2 报告与子处理方清单均需提交表单才能取得；安全检查表被放在留资表单之后。
- **四个主体之间的关系任何地方都没有说明。** 没有任何公司页面、新闻稿或备案解释 Ｎｏｔｔａ株式会社、Mind Cruiser Limited 与 NOTTA PTE. LTD. 的关系，也没有解释应用包名为何落在 `com.langogo.*` 命名空间。日本登记系统只能确认日本主体。
- **未公开工程人数、地点分布或团队结构。** 唯一的数字是"含全球据点 100 名"。
- **不存在英文版公司信息页。** `/company` 只有日文；`/en/about` 是市场页，没有公司数据、地址或管理层。

### 不同来源之间的不一致

- **用户数有五个版本：** 150 万（[採用情報](https://www.notta.ai/recruit)）、200 万下载（日文站页脚）、800 万（[Slator，2025-07-23](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)）、1,000 万（[PR TIMES，2025-05-29](https://prtimes.jp/main/html/rd/p/000000035.000106830.html) 与[英文 About 页](https://www.notta.ai/en/about)）、1,500 万（[PR TIMES，2025-12-09](https://prtimes.jp/main/html/rd/p/000000059.000106830.html) 与 [Notta Memo 页面](https://www.notta.ai/hardware/memo)）。其中数个同时挂在公司自己的站点上。
- **企业客户数：** 5,000 家以上（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)、[Notta Memo 页面](https://www.notta.ai/hardware/memo)）对 6,000 家以上（[英文 About 页](https://www.notta.ai/en/about)）对 10 万以上客户（[Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)）。
- **累计转写时长：** 3,000 万小时以上（[英文 About 页](https://www.notta.ai/en/about)）、1,000 万小时（[Notta Memo 页面](https://www.notta.ai/hardware/memo)）、3 亿小时以上（[Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)）。
- **语言覆盖：** 转写 58 种、翻译 42 种（[App Store 描述](https://itunes.apple.com/lookup?id=1480649572)、[Notta Memo 页面](https://www.notta.ai/hardware/memo)）对 104 种（[採用情報](https://www.notta.ai/recruit)）。
- **成立年份：** 法人登记与两份融资新闻稿都写设立于 2022-05-25；公司自己的沿革写创业于 2020 年、当年 5 月上线服务；App Store 显示 iOS 应用首发于 2019-12-19。三者可以各自成立，但没有任何页面把它们对上。
- **管辖法取决于页面语言：** [日文条款](https://www.notta.ai/terms)写明 Ｎｏｔｔａ株式会社、日本法、东京地方法院；[英文条款](https://www.notta.ai/en/terms)写的是 "Notta Inc."、香港法、香港法院专属管辖。
- **轮次命名：** 公司把 2025 年 5 月这轮称为 **Series A+**（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)）；[BRIDGE](https://thebridge.jp/2025/05/notta-a-provider-of-ai-meeting-minutes-services-raises-990-million-yen-in-series-a-funding) 称之为 Series A；[Slator](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/) 报道为一笔 2025-06-30 交割的 630 万美元融资，并点名 GL Ventures 为联合领投，而公司新闻稿完全没有提到这一方。
- **地址：** [会社概要](https://www.notta.ai/company)仍显示大手町，而 PR TIMES 的公司档案与[迁址公告](https://www.notta.ai/news/info/20260803-office-relocation)给出的是 2026-08-03 起的神田神保町。登记系统的最后更新日是 2025-04-23。
- **"日本 AI 独角兽"**这一说法出现在覆盖 2025 年那轮融资的转发稿标题里；公司与任何投资方都没有披露过能支撑该描述的估值。

### 其他

- **安全披露是整份公开记录里最详实的部分。** 除认证外，[安全页面](https://www.notta.ai/security)还记载了带灾备切换计划的日本境内备份数据中心、静态加密、SHA-256 口令哈希、带审计日志的身份与访问控制、CPO/CISO 安全小组、发布前的单元／集成／系统测试，以及周期性内部安全培训。
- **公司会公开真正的故障复盘**，逐个受影响子系统给出发现与恢复时间戳——这在同规模公司中不多见，也是外界了解其架构最清晰的一扇窗（[2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact)、[2026-03-10](https://www.notta.ai/news/info/20260310-incident-report)）。
- **GPT-5 摘要在商务版与企业版上被排除**（[博客，更新于 2026-05-15](https://www.notta.ai/blog/notta-gpt5-integration)），也就是说企业档位跑的是与消费档位不同的摘要链路。
- **产品线如今横跨软件与两款硬件**——Notta Memo（23,500 日元，2025-06-16 开售，28 克，4 个 MEMS 麦克风加 1 个骨传导麦克风，32 GB，约 30 小时录音）以及在 Makuake 先行公开的 Zenchord 1 AI 麦克风（[Notta Memo 页面](https://www.notta.ai/hardware/memo)）。硬件在 2025 年两轮融资中都被列为资金用途。
- **`mindcruiser` GitHub 组织几乎全部是上游 Flutter 与 Dart 包的 fork**，外加少量 Notta 自有的资源仓库和那个 MCP 扩展。没有任何原创开源库，组织只有 8 个关注者。
- **公司曾于 [2025-11-11](https://www.notta.ai/news) 公开提醒**存在冒充 Notta 官网的假冒站点。
- **一个名为 `Notta-Ai` 的 GitHub 组织是优惠码垃圾账号**，创建于 2025-05-17，只有一个 `.github` 仓库，名称写着 "Notta AI Promo Code - 90% Off"，与该公司无关（[GitHub API](https://api.github.com/orgs/notta-ai)）。
- **站点是一片规模很大的多语言 SEO 资产** —— 站点地图中包含约 20 种语言、数百个博客与工具页，`/tools/` 与 `/translate-audio/` 部分的体量远超产品页。[robots.txt](https://www.notta.ai/robots.txt) 里屏蔽了 `/showcase/`、`/changelog/` 与 `/landing-page/`，而英文条款还透露出第二个产品 "Notta Showcase"，它没有任何市场页面。

---

## 资料来源

**官方**

- [Notta —— www.notta.ai](https://www.notta.ai/en) · [日文站](https://www.notta.ai/company)
- [会社概要](https://www.notta.ai/company) · [About（英文）](https://www.notta.ai/en/about) · [安全页面](https://www.notta.ai/security)
- [採用情報](https://www.notta.ai/recruit) · [定价](https://www.notta.ai/en/pricing)
- [Notta Memo 硬件页，含公司沿革](https://www.notta.ai/hardware/memo)
- [利用規約 —— 日文条款](https://www.notta.ai/terms) · [Terms of Service —— 英文](https://www.notta.ai/en/terms) · [Privacy Policy —— 英文](https://www.notta.ai/en/privacy)
- [新着情報（新闻索引）](https://www.notta.ai/news) · [站点地图](https://www.notta.ai/sitemap-0.xml) · [robots.txt](https://www.notta.ai/robots.txt)
- [Nottaデスクトップ发布稿，2026-07-08](https://www.notta.ai/news/release/notta-desktop)
- [Notta Brain 新功能，2026-06-17](https://www.notta.ai/news/release/notta-brain-new-features)
- [强化开发体制公告，2026-06-10](https://www.notta.ai/news/info/ai-agent-era-development-enhancement)
- [ビジネスPlus 套餐，2026-07-27](https://www.notta.ai/news/info/notta-business-plus) · [迁址公告，2026-07-27](https://www.notta.ai/news/info/20260803-office-relocation) · [高知銀行，2026-06-25](https://www.notta.ai/news/info/kochi-bank) · [价格调整，2025-06-16](https://www.notta.ai/news/info/2025-06-16-price-changed)
- [AWS 故障影响公告，2025-10-21](https://www.notta.ai/news/info/20251020-aws-outage-impact) · [登录故障报告，2026-03-10](https://www.notta.ai/news/info/20260310-incident-report)
- [GPT-5 集成文章，更新于 2026-05-15](https://www.notta.ai/blog/notta-gpt5-integration)
- [状态页](https://status.notta.ai/)
- [GitHub —— mindcruiser 组织](https://api.github.com/orgs/mindcruiser) · [仓库列表](https://api.github.com/orgs/mindcruiser/repos) · [notta-mcp](https://github.com/mindcruiser/notta-mcp) · [mc_flutter_recorder](https://github.com/mindcruiser/mc_flutter_recorder)
- [npm —— notta 相关包](https://registry.npmjs.org/-/v1/search?text=notta)
- [App Store 元数据 —— iTunes lookup API](https://itunes.apple.com/lookup?id=1480649572) · [Google Play](https://play.google.com/store/apps/details?id=com.langogo.transcribe)
- [Ranee Zhang —— 增长副总裁作者页](https://www.notta.ai/en/author/ranee-zhang)

**新闻稿**

- [Notta、Granite-Integral Capitalから23億円のシリーズB資金調達を実施 —— 2025-12-09（日文）](https://prtimes.jp/main/html/rd/p/000000059.000106830.html)
- [AI議事録サービス提供のＮｏｔｔａ株式会社 シリーズA+総額9億9000万円の資金調達を実施 —— 2025-05-29（日文）](https://prtimes.jp/main/html/rd/p/000000035.000106830.html)

**第三方报道与资料页**

- [国税庁法人番号公表サイト —— Ｎｏｔｔａ株式会社，法人番号 5010001226919，含地址变更履历（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010001226919)
- [BRIDGE —— Notta 完成 23 亿日元 Series B，2025-12（英文）](https://thebridge.jp/en/2025/12/notta-provider-of-ai-transcription-tools-raises-%C2%A52-3-billion-in-series-b-from-granite-integral-capital)
- [BRIDGE —— シリーズAラウンド9億9,000万円を調達，2025-05（日文）](https://thebridge.jp/2025/05/notta-a-provider-of-ai-meeting-minutes-services-raises-990-million-yen-in-series-a-funding)
- [Slator —— 转写创业公司 Notta 融资 630 万美元，把独立录音设备带入美国，2025-07-23](https://slator.com/transcription-startup-notta-raises-usd-6m-to-bring-standalone-recorder-to-us/)
- [The SaaS News —— Notta 完成 23 亿日元 Series B](https://www.thesaasnews.com/news/notta-raises-2-3-billion-in-series-b)
- [日经亚洲 —— 中国科技创业者押注日本而非中国，2023-03-29](https://asia.nikkei.com/business/china-tech/chinese-tech-entrepreneur-bets-big-on-japan-but-not-china)
- [Yew —— 该公司具名工程师所维护的框架仓库](https://github.com/yewstack/yew) · [Yew 博客](https://yew.rs/blog) · [GitHub 上的 Madoshakalaka / Siyuan Yan](https://github.com/Madoshakalaka)
- [Anthropic —— Code w/ Claude 2026 Tokyo](https://claude.com/code-with-claude/tokyo)

**列出以避免误认**

- [GitHub 组织 `Notta-Ai` —— 与公司无关的优惠码账号](https://api.github.com/orgs/notta-ai)
