# NodeX

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

NodeX（NodeX株式会社，英文名 NodeX, Inc.；品牌也写作 NODE X，读作ノードクロス）是一家东京公司，2019-05-07 以 CollaboGate Japan株式会社 名义成立，2025-03-04 更为现名（法人番号 6011001127965，[国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)）。其产品同样名为 NodeX，为物联网和边缘设备分配 W3C 分布式标识符（DID）：安装在设备上的 Rust 代理负责设备认证、密钥管理和端到端加密消息（DIDComm），并把遥测数据发送到云端看板 NodeX Studio（[文档](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43)、[产品页](https://nodex.inc/product)；无日期，访问于 2026-10-11）。2026 年，公司将业务描述为面向关键基础设施的零信任安全平台，并把国防与国家安全列为首个目标市场（[2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)、[Agent 工程师职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)；职位元数据日期 2026-09-29）。

- 累计融资 8.3 亿日元：先以 J-KISS 型新株予约权完成“累計2.3億円”的种子轮，投资方为伊藤忠テクノロジーベンチャーズ、DNX Ventures 和株式会社ラック（[2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)），随后由 DNX Ventures 与 ITOCHU Technology Ventures 投资 6 亿日元的プレシリーズA（[2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)）。
- 公司官网不列出客户名称。其新闻稿提到与東芝テック、PFU、NR-Power Lab（日本碍子与理光的合资公司）和 MEEQ 的合作项目；2025 年 1 月，公司援引路透社称日本航空自卫队已开始与其商讨合作（[2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html)）。BRIDGE 报道东芝和三菱重工已采用该平台（[2025-03-21](https://thebridge.jp/2025/03/node-x-a-platform-for-secure-transmission-of-real-world-data-raises-600-million-yen-in-pre-series-a-funding-from-dnx-and-itochu-affiliated-investors)）。
- 按公司说法团队约 20 人（“20人ほど”，[招聘职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)，2026-09-29），并称正从约 20 人向约 50 人扩张。其他来源给出 16、13 和 11 人（见`备注`）。
- 工程：代理用 Rust 编写（[文档](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43)），服务运行在 Google Cloud 上（[ISMS 云安全认证范围](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)）。当前职位列出 TypeScript/React、Rust/Axum/SQLx、GraphQL、PostgreSQL/Bigtable/Redis 以及 GCP/Vercel。当前 Agent 工程师职位要求母语级日语，允许在日本国内全远程工作，每月需到岗参加 All Hands（[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)；访问于 2026-10-11）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 公开品牌 | NodeX；也写作 NODE X；读作ノードクロス（“NODE X（ノード・クロス）”） | [nodex.inc](https://nodex.inc/)、[2025-03-19 公告](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| 法定名称 | ＮｏｄｅＸ株式会社（フリガナ ノードクロス）；公司给出的英文名为“NodeX, Inc.” | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)、[公司页面](https://nodex.inc/company) |
| 法人番号 | 6011001127965；指定日 2019-05-14 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| 曾用法定名称 | ＣｏｌｌａｂｏＧａｔｅ Ｊａｐａｎ株式会社（コラボゲートジャパン）；更名于 2025-03-04 生效 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| 成立 | 2019-05-07 | [公司页面](https://nodex.inc/company) |
| 登记总部 | 東京都渋谷区円山町５番５号Ｎａｖｉ渋谷Ｖ３階（登记记录最后更新于 2025-03-19） | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| 公司公布的办公地址 | 〒105-5515 東京都港区虎ノ門1-17-1 虎ノ門ヒルズビジネスタワー 15F；招聘职位称该办公室为 CIC Tokyo | [公司页面](https://nodex.inc/company)、[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)；访问于 2026-10-11 |
| 代表人 | 代表取締役CEO 三井 正義（Masayoshi Mitsui） | [公司页面](https://nodex.inc/company) |
| 列出的董事 | 取締役CRO 林 泰成；取締役CBO 内田 光紀；社外取締役 小川 剛（伊藤忠テクノロジーベンチャーズ General Partner） | [公司页面](https://nodex.inc/company)；访问于 2026-10-11 |
| 资本金 | 1 亿日元“（2026年1月現在）” | [HERP 职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)；访问于 2026-10-11 |
| 员工人数 | “20人ほど”；同一职位页的公司信息栏写 16 人 | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)，日期 2026-09-29 |
| 工作语言 | 未找到全公司层面的说明；Agent 工程师职位要求“ネイティブレベルの日本語コミュニケーション” | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| 累计融资 | 累计 8.3 亿日元（“累計8.3億円”） | [2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| 公司列出的投资方 | 伊藤忠テクノロジーベンチャーズ、DNXベンチャーズ、LAC | [公司页面](https://nodex.inc/company) |
| 安全认证 | ISO/IEC 27001（JIS Q 27001:2025），登记号 JP027239；ISMS 云安全（JIP-ISMS517-1.0，基于 ISO/IEC 27017），登记号 28118935；两者均于 2026-03-30 首次登记，有效期至 2029-03-29，认证机构为ビューローベリタスジャパン | [ISMS-AC 27001 记录](https://isms.jp/lst/ind/CR_JP027239.html)、[ISMS-AC 云安全记录](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html) |
| 其他政府记录 | 事業継続力強化計画認定（中小企業庁），2025-07-22 | [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965) |

ISO/IEC 27001 的认证范围为“IoTシステム向けセキュリティソフトウェアの研究、開発、企画、教育、販売、保守、運用及びアドバイザリー業務”。云安全认证范围涵盖以云服务提供方身份提供 NodeX，“及びGoogleクラウドサービスカスタマとしての利用”（[ISMS-AC](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)）。

**项目、会员与认可。** 公司加入了 Decentralized Identity Foundation（DIF），并称自己是首家加入的日本初创公司（[2021-03-10](https://prtimes.jp/main/html/rd/p/000000001.000070282.html)）；CEO 自 2022 年起担任 DIF Japan Chair（[2026-05-12 演讲者简介](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。其他事项：Garage+（台北）Startup Global Program 第 12 期，2021-11-01 至 11-05（[2021-11-16](https://prtimes.jp/main/html/rd/p/000000003.000070282.html)）；面向 RA 和 RX 微控制器系列的 Renesas Ready Partner（[2022-06-08](https://prtimes.jp/main/html/rd/p/000000005.000070282.html)）；与東芝テック 的项目入选数字厅“Trusted Web の実現に向けたユースケース実証事業”（[2022-09-13](https://prtimes.jp/main/html/rd/p/000000006.000070282.html)）；以及 BRIDGE 的“HOT100 with Accenture Ventures”（[2025-04-30](https://thebridge.jp/2025/04/can-generative-ai-reduce-office-energy-consumption-nodexs-vision-for-a-data-driven-society-with-decentralized-id-hot100-accenture-ventures-vol-6)）。

### 品牌与法律实体

| 名称 | 类型 | 期间或状态 | 关系 | 来源 |
|---|---|---|---|---|
| CollaboGate Japan株式会社 | 曾用法定名称 | 2019-05-07 至 2025-03-04 | 与 NodeX株式会社 法人番号相同 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965) |
| NodeX株式会社 / NodeX, Inc. | 现行法定名称 | 自 2025-03-04 起 | — | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)、[公司页面](https://nodex.inc/company) |
| NODE X / NodeX | 品牌 | 2025 年 3 月统一：“社名変更を実施、ブランドを「NODE X（ノード・クロス）」に統一” | 产品名与公司名 | [2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| UNiD | 曾用产品品牌 | 用于 2021-03 至 2022-06 的新闻稿 | 同一公司早期的 DID 平台与设备代理（“UNiD EDGE”） | [2021-03-10](https://prtimes.jp/main/html/rd/p/000000001.000070282.html)、[2022-06-08](https://prtimes.jp/main/html/rd/p/000000005.000070282.html)、[GitHub `getunid`](https://github.com/getunid) |
| collabogate.com、nodecross.io | 曾用网站域名 | 两者都跳转到 `nodex.inc`；`nodecross.io` 和 `getunid.io` 的 WHOIS 注册组织为“CollaboGate Japan, Inc.” | 业务延续 | WHOIS 与 HTTP 检查，2026-10-11 |
| nodecross.app | 服务域名 | 托管 GraphQL API（`api.nodecross.app`）和 API 参考文档 | 目前仍在使用 | [文档](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44) |
| GitHub `nodecross` | 代码组织 | 显示名“NodeX”，blog `https://nodex.inc`，location“Japan”；创建于 2023-01-25 | 公司的公开代码托管 | [GitHub API](https://api.github.com/orgs/nodecross)；读取于 2026-10-11 |

CollaboGate Japan 与 NodeX 之间的法律延续由登记确认（法人番号相同）。CollaboGate 这一名称仍出现在公司基础设施中：安全方针和招聘方针托管在 `collabogate.notion.site`，招聘页上的 HERP 职位链接使用 `/v1/collabogate/` 路径，2026-05-12 新闻稿的媒体联系邮箱为 `contact@collabogate.com`（[招聘页](https://nodex.inc/careers)、[2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。

### 公司陈述的市场背景

- 边缘设备数量自 2018 年起超过移动设备，预计到 2035 年达到 2,750 亿台，占全部设备的 94.5%；自行构建零信任数据基础设施需要“2〜3年の期間と数十億円の初期投資”（[2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)）。
- 日本防卫预算已增至约 GDP 的 2%（“2026年度 約9兆円”），公司称防卫省的采购公告已把零信任设备认证列为要求（[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)，2026-09-29）。
- 公司把设备、机器人和 AI agent 的身份称为“Non-Human Identity（NHI）”（[2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。

---

## 产品

文档将 NodeX 描述为“IoTシステムのオブザーバビリティ（可観測性）を確保するためのプラットフォーム”：开发者把 NodeX Agent 集成进设备，使其遥测数据被安全地收集到云端的 NodeX Studio（[文档](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43)；无日期，访问于 2026-10-11）。官网把产品分为三个组件（[产品页](https://nodex.inc/product)）。

### 组件与功能领域

| 组件 | 公司描述 | 来源 |
|---|---|---|
| NodeX Agent | 设备端中间件，负责设备识别与认证、配置自动化、密钥与证书生命周期管理、遥测埋点以及设备间 E2EE。文档称其为“Rust製ソフトウェア”，并列出 Ubuntu 20.04/22.04/24.04、Debian 10–12、Yocto Mickledore 4.2、macOS（最新一个版本）和 Windows 10。 | [产品页](https://nodex.inc/product)、[文档](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43) |
| NodeX Cloud | 云端数据基础设施，称可处理“数十万台規模のデバイス接続”，并提供“分散型IDベースのWeb PKI” | [产品页](https://nodex.inc/product) |
| NodeX Studio | 设备管理与监控看板：实时指标、事件与日志，告警，跨组织设备管理，三种用户角色（管理ユーザー、開発者、オペレーター）以及双因素认证 | [产品页](https://nodex.inc/product)、[安全白皮书](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5) |
| Agent 本地 API | 用于查找和解析 DID、创建与验证 DIDComm 消息、发送事件、自定义指标、日志和属性、执行设备操作以及读取设备配置的接口 | [Agent API 参考](https://agent-api-ref.nodecross.app/)（v6.2.0） |
| Studio GraphQL API | Studio 中显示的数据可通过 `api.nodecross.app/v1/public/graphql` 的 GraphQL 获取，使用以“APIクライアント”密钥签名的 JWT 认证 | [文档](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44)、[API 参考](https://studio-graphql-api-ref.nodecross.app/) |
| 归档导出 | 每 5 分钟把收集到的数据以 gzip 压缩的 JSONL 写入客户的 Amazon S3、Azure Storage 或 Google Cloud Storage；每 800 台设备一个文件 | [文档](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4) |

Agent 数据默认值：指标每 15 秒采集一次（可设 5–300 秒），每 60 秒发送一次（60–3600 秒）；事件为最多 255 字节的字符串；日志为最多 1 MB 的字符串，无法在 Studio 中查看，只能通过归档功能转发；四类数据默认保留 14 天（[文档](https://docs.nodex.inc/NodeX-Agent-11fd301e9c6580768821fed1c00063b4)）。

### 公司对产品的描述变化

| 日期 | 公司措辞 | 来源 |
|---|---|---|
| 2021-03-10 | UNiD，“国内初エンタープライズ対応の分散型IDプラットフォーム”，面向推动客户体验数字化的企业；使命“Reimagine Digital Trust” | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000001.000070282.html) |
| 2021-11-29 | “EDGE-TO-CLOUD SECURITY PLATFORM「UNiD」”；与 PFU 使用“UNiD EDGE SDK”的概念验证 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000004.000070282.html) |
| 2022-06-08 | “Zero Trust IoT Security Platform「UNiD」”；设备管理代理“UNiD EDGE”以开源方式开发 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000005.000070282.html) |
| 2023-02-15 | “IoTデータセキュリティソリューション「NodeX」” | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) |
| 2023-08-09 | “データトラスト基盤「NodeX」” | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000008.000070282.html) |
| 2024-03 | CEO 称用于管理物联网设备的可观测性服务于 2024 年 3 月开始运行 | [CEO 访谈](https://nodex.inc/interview/interview01)，2025-03-11 |
| 2025-03-19 | “エッジ向けゼロトラストデータ基盤” | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| 2026-05-12 | “重要インフラ向けゼロトラストセキュリティ基盤「NodeX」事業” | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000014.000070282.html) |
| 2026-09-29 | 在关键基础设施各领域中，把国防与国家安全选为“最初の主戦場” | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |

### 商业化

未找到公开价目表。公司称 NodeX 以“SaaS提供”方式交付，客户可在“ライセンス契約後、わずか1週間”内开始使用（[nodex.inc](https://nodex.inc/)）；用例页称签订用户许可合同后约 1–2 周完成代理集成，随后由专家团队在三到六个月内协助确定服务需求（[用例](https://nodex.inc/usecase/usecase01)，2025-03-18）。GitHub 上的代理二进制文件只能在另行签订的书面协议下使用，许可证将该协议定义为包括许可、订阅、评估、概念验证和分销协议（[LICENSE](https://github.com/nodecross/nodex/blob/main/LICENSE)，2026-09-18 添加）。安全白皮书提到“すべての契約プラン”，但未列出具体方案（[白皮书](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5)）。

### 历年公开规模

| 日期 | 公开数字或说法 | 来源 |
|---|---|---|
| 2023-02-15 | 超过 10 家大型制造商已开始对 NodeX 进行技术评估 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) |
| 2024-12 | CEO：已与日本产业界顶级企业合作；“ようやく初期PMFに至れた” | [CEO 访谈](https://nodex.inc/interview/interview01)，2025-03-11 发布 |
| 2025-03-19 | 已被“国内トップティアのメーカー”采用（未具名） | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |
| 2025-03-19 | DNX：在约两年半的种子期内“複数のエンプラ顧客を獲得” | [DNX Ventures note](https://note.com/dnx_vc/n/n09886e4c33d1) |
| 2026-09-29 | “ミッションクリティカル領域ですでにPMFを確認” | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |

未公开客户数、设备数或营收数字。

### 已公布客户与合作伙伴

| 日期 | 合作方 | 公布内容 |
|---|---|---|
| [2021-07-06](https://prtimes.jp/main/html/rd/p/000000002.000070282.html) | テセラ・テクノロジー、瑞萨 | 与テセラ业务合作，基于瑞萨安全 MCU 构建“分散型IoTプラットフォーム” |
| [2021-11-29](https://prtimes.jp/main/html/rd/p/000000004.000070282.html) | PFU | 在 PFU 文档扫描仪中嵌入 UNiD EDGE SDK 的概念验证，实现到云存储的端到端认证加密传输 |
| [2022-09-13](https://prtimes.jp/main/html/rd/p/000000006.000070282.html) | 東芝テック | 联合 Trusted Web 实证：在数码复合机上扫描、可验证是否被篡改的文档 |
| [2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) | 東芝テック、PFU、英特尔、瑞萨 | 与東芝テック 和 PFU 开展面向产品采用的联合项目；与英特尔和瑞萨建立合作关系 |
| [2023-08-09](https://prtimes.jp/main/html/rd/p/000000008.000070282.html) | NR-Power Lab（日本ガイシ与リコー的合资公司） | 基于 NodeX 构建虚拟电厂（VPP）系统：2023 财年技术验证，计划 2024 财年实地验证 |
| [2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html) | 日本航空自卫队 | 公司称[路透社文章（2025-01-22）](https://www.reuters.com/business/retail-consumer/japan-hunts-dual-use-goods-makers-aid-military-expansion-2025-01-22/)提到航空自卫队正与其沟通合作 |
| [2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) | 東芝、リコー、英特尔 | 融资公告中刊登了东芝首席数字官、理光 CTO 和英特尔日本一位执行役员的评论 |
| [2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html) | ミーク（MEEQ） | 解决方案合作及概念验证：将 MEEQ SIM 及其闭域网与 NodeX 结合，用于移动物联网设备 |

第三方关于客户的报道：BRIDGE 写道该平台“すでに東芝や三菱重工など国内大手に採用され”（[2025-03-21](https://thebridge.jp/2025/03/node-x-a-platform-for-secure-transmission-of-real-world-data-raises-600-million-yen-in-pre-series-a-funding-from-dnx-and-itochu-affiliated-investors)）；KDDI MUGENLABO Magazine 提到“東芝や三菱重工といった日本を代表する製造業との提携”（[2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)）；BRIDGE 的一篇活动报道称 CEO 的业务是保护“防衛省や NTT、電力会社など”关键基础设施的通信（[2025-07](https://thebridge.jp/2025/07/ai-era-collaboration-partners-intention-time-key-ivs2025)）。公司自己的新闻稿未点名这些客户。

### 公开计划

- 2023-02-15：将种子轮资金用于在全球招聘工程师和业务开发人员（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)）。
- 2025-03-18：利用 LLM 优化设置远程控制公用设施设备的功能“現在、顧客のフィードバックを得ながら開発中”（[用例](https://nodex.inc/usecase/usecase03)）。
- 2025-03-19：加强产品与交付团队，优先保障早期客户成功；招聘工程师、产品经理和业务开发人员（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)）。
- 2025-05-12：据 CEO 说，2025–26 年专注于现有客户的“ディープサクセス”，确认后再推进全球扩张和客户数量增长（[KDDI MUGENLABO](https://mugenlabo-magazine.kddi.com/list/nodex/)）。
- 2026-09-29：组织规模“20名規模から50名規模へ”（[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)）。

---

## 创始人

**三井 正义（Masayoshi Mitsui）**——创始人，代表取締役CEO（[公司页面](https://nodex.inc/company)、[招聘页](https://nodex.inc/careers)）。

- 1989 年生于京都府（[週刊BCN，2025-11-27](https://www.weeklybcn.com/journal/era/detail/20251127_212929.html)）。
- 毕业于庆应义塾大学理工学部，在庆应 SFC 完成研究生学业，研究数字化工作母机与自律分散系统（[2026-05-12 演讲者简介](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。
- 大学一年级末（约 2011 年）在纽约待了半年，之后在读期间以个人事业主身份经营 SNS 咨询业务（[CEO 访谈](https://nodex.inc/interview/interview01)，2025-03-11）。
- 2015 年：创立 Bitom，开发面向 3D 打印机的云服务；他本人称第一家公司以失败告终（[週刊BCN](https://www.weeklybcn.com/journal/era/detail/20251127_212929.html)、[CEO 访谈](https://nodex.inc/interview/interview01)）。
- 2017 年起：运营分布式账本技术研究社区（[演讲者简介](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。
- 约 2018 年：开始参加 DIF 活动，并参与 W3C 规范制定（[CEO 访谈](https://nodex.inc/interview/interview01)、[KDDI MUGENLABO，2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)）。
- 2019-05：创立 CollaboGate Japan（现 NodeX）（[公司页面](https://nodex.inc/company)）。
- 2022 年：出任 DIF Japan Chair（[演讲者简介](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。KDDI MUGENLABO 还报道他参与过内阁府关于日本分布式身份应用场景的项目（文章未注明时间；[2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)）。
- 2026-04：与公司工程团队一起在 Internet Identity Workshop #42 发表议题“DID-Backed X.509: Linking Decentralized Identity to PKI Certificates”（[2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)）。

### 主要管理层

| 姓名 | 职务原文 | 公开背景 | 来源 |
|---|---|---|---|
| 内田 光紀 | 取締役CBO | 尼康和 Wind River，18 年间与设备厂商谈判 6,000 多件许可与合作；天普大学 LL.M.（2006）和 MBA（2013）；SCORE 委员（访谈页写作“JET SCORE”，文化手册写作“JST SCORE”）；2021 年以 CBO 身份加入 | [访谈](https://nodex.inc/interview/interview06)，2025-03-04；[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 林 泰成 | 取締役CRO | Salesforce 日本客户经理；在一家外资金融科技初创公司主导销售运营；2023 年以 CRO 身份加入 | [访谈](https://nodex.inc/interview/interview03)，2025-03-10 |
| 橋本 寛 | シニアデリバリーマネージャー | 京都大学工学部；日本総研、PTC、UiPath；2023 年加入 | [访谈](https://nodex.inc/interview/interview02)，2025-03-10 |
| 川上 和良 | 基盤テックリード | 投影映射控制系统、外汇与套利交易系统、音频 AI 引擎；Rust、C++、Go；2025 年加入 | [访谈](https://nodex.inc/interview/interview05)，2025-03-10 |
| 松尾 一成 | エージェント・テックリード | 名古屋大学数学硕士；机器学习流水线后端、自主移动机器人与 AGV 软件；形式化验证；在 NodeX 使用 Rust | [文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)，Ver.2025.03.10 |
| 小川 剛 | 社外取締役 | 伊藤忠テクノロジーベンチャーズ General Partner | [公司页面](https://nodex.inc/company) |

公司页面列出的顾问：元橋 一之（东京大学先端科学技术研究中心；[2023-08-21](https://prtimes.jp/main/html/rd/p/000000009.000070282.html) 就任）和高橋 大造（英特尔日本，執行役員 パートナー事業本部 本部長）。文化手册（Ver.2025.03.10）把公司分为 Growth & Delivery（销售、交付、市场）、Product & Technology（代理、云平台、产品）和 Corporate & Finance 三部分，其团队页除两位技术负责人外，还列出一名全栈工程师兼 PdM、一名 SRE 工程师、一名安全工程师和两名全栈工程师。

---

## 融资

| 日期 | 轮次（公司措辞） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2023-02-15 公布 | シード（J-KISS型新株予約権） | “累計2.3億円” | 伊藤忠テクノロジーベンチャーズ、DNX Ventures、株式会社ラック | 2.3 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000007.000070282.html) |
| 正文日期 2025-02-21；2025-03-19 公布 | プレシリーズA | 6 亿日元 | DNX Ventures、ITOCHU Technology Ventures | 8.3 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html) |

ITV 合伙人在 2025 年公告中称 ITV“2022年にNODE Xにリードで投資”；DNX 称其领投了プレシリーズA，首次投资是在 2022 年 12 月的种子轮（[DNX Ventures note，2025-03-19](https://note.com/dnx_vc/n/n09886e4c33d1)）。ITV 和 DNX 参与了两轮；株式会社ラック只出现在种子轮公告中，公司页面将 LAC 列为投资方。プレシリーズA 与公司更名、品牌统一和官网改版一同公布（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)）。公告称资金用于产品演进以及加强产品与交付团队。

---

## 工程

### 技术栈与平台

| 项目 | 证据级别 | 来源 |
|---|---|---|
| NodeX Agent 使用 Rust | 文档确认（“Rust製ソフトウェア”）；仓库 topics 与发布说明也提到 Rust 工具链 | [文档](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43)、[发布](https://github.com/nodecross/nodex/releases) |
| Studio 后端使用 Rust；Axum、SQLx | 公司手册中的成员简介写有“RustでのStudio開発”；Axum 和 SQLx 来自招聘列表 | [文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)、[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| DID（`did:webvh`）、DIDComm、ECDH-1PU+A256KW 密钥协商配合 A256GCM、P-384 与 Ed25519 密钥 | 由 Agent API 参考（v6.2.0）和 v6.3.1 发布说明（“compliance with didwebvh v1.0”）确认 | [Agent API 参考](https://agent-api-ref.nodecross.app/)、[发布](https://github.com/nodecross/nodex/releases) |
| FIPS 与非 FIPS 代理构建 | 由 v5.0.0（2025-11-25）起的发布文件确认；API 参考称 DIDComm 加密“FIPS 140-3 compliant” | [发布](https://github.com/nodecross/nodex/releases) |
| 代理目标平台：Linux x86_64 与 aarch64（`.deb` 和 zip）、Windows（MSI）、macOS aarch64；Yocto 层 `meta-nodex`（BitBake） | 由发布文件和公开仓库确认 | [发布](https://github.com/nodecross/nodex/releases)、[GitHub `nodecross`](https://github.com/nodecross) |
| Google Cloud | 已确认：ISMS 云安全范围写明使用 Google 云；归档文档给出项目 `nodex-production` 中的服务账号；文化手册列出 Cloud Run、GKE、Cloud Bigtable、BigQuery 和 Cloud Monitoring | [ISMS-AC](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)、[文档](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4)、[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| GraphQL（Studio API）、JWT | 文档确认 | [文档](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44) |
| Auth0 | 安全白皮书确认（用于密码管理）；招聘列表中也有 | [白皮书](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5) |
| GitHub Actions、Renovate | 手册列出 GitHub Actions；发布说明提到 CI 工作流和 Renovate | [文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)、[发布](https://github.com/nodecross/nodex/releases) |
| TypeScript、React（2025 年职位中还有 Next.js） | 招聘列表 | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)、[归档职位列表，2025-02-19](https://web.archive.org/web/20250219084303/https://herp.careers/v1/collabogate) |
| PostgreSQL、Redis、Bigtable | 招聘列表（Bigtable 也见于手册） | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| SendGrid、PagerDuty、Vercel；Figma、GitHub、Notion、Slack、Linear；Claude（Anthropic） | 招聘列表中的工具 | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| Terraform、Cloud Run | 2025 年一则云基础设施职位中的招聘列表 | [归档职位列表，2025-02-19](https://web.archive.org/web/20250219084303/https://herp.careers/v1/collabogate) |

### 系统

| 系统 | 功能 | 来源 |
|---|---|---|
| 设备身份与 E2EE 消息 | 代理以信任根管理每台设备的 DID 和密钥，自动完成配置，执行双向认证并发送 DIDComm 加密消息；目标 DID 须经授权，授权结果最多缓存 60 秒 | [README](https://github.com/nodecross/nodex)、[Agent API 参考](https://agent-api-ref.nodecross.app/) |
| 本地代理接口 | Windows 上为 `localhost:3000` 的 HTTP；Unix 上为 `~/.nodex/run/nodex.sock` 的 Unix 域套接字 | [Agent API 参考](https://agent-api-ref.nodecross.app/) |
| 遥测管线 | 采集指标、自定义指标、事件和日志并转发到 Studio，默认保留 14 天 | [文档](https://docs.nodex.inc/NodeX-Agent-11fd301e9c6580768821fed1c00063b4) |
| Studio 监控与告警 | 看板、告警条件、基于角色的权限和审计日志归档设置 | [文档](https://docs.nodex.inc/10bd301e9c6580b99677d8323218a3fa) |
| 归档导出 | 定时导出到客户的 S3、Azure Storage 或 GCS 存储桶 | [文档](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4) |
| 闭域网上的移动物联网 | 与 MEEQ 的概念验证：设备级认证、设备到服务器的 E2E 加密与完整性保护，以及经 MEEQ 闭域网的持续监控 | [2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html) |
| DID 支撑的 X.509 | 将 DID 与现有 X.509 证书关联的方案，作为提案在 IIW #42 上发表 | [2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html) |

NodeX Studio 安全白皮书写明：数据保存在日本国内；静态数据以 AES256 加密，传输使用 TLS；每日备份并保留五代；灾难恢复目标 RPO 48 小时、RTO 24 小时；可用性目标 99.9%；租户逻辑隔离；用户访问日志保存一年；由第三方进行 Web 应用和基础设施漏洞评估；发生重大事件时目标在三小时内通知用户（[白皮书](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5)；无日期，访问于 2026-10-11）。

**代码与发布历史。** 公开仓库 `nodecross/nodex` 创建于 2025-04-30，用于分发代理二进制文件，并在 [2026-01-19](https://github.com/nodecross/nodex/commit/8684127d478fb52d055d204f18c726cede336a19) 删除前附带 Python 和 Node.js 示例。仓库共发布 44 个版本，从 v1.1.16（2025-04-30）到 v6.3.1（2026-06-26）。其许可证于 [2026-03-19](https://github.com/nodecross/nodex/commit/a0fea2fa7bf0fa21c56c94d1ea2a8b1dfc175544) 从 Apache-2.0 改为专有许可，README 写明“the source code is not published here”（[README](https://github.com/nodecross/nodex)；读取于 2026-10-11）。Agent 工程师职位称“NodeXはこれまで外部パートナーと共に開発を進めてきました”，该职位将在产品进入正式运营阶段时主导架构与技术选型（[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)）。

### 招聘所需技术背景

2026-10-11 时 HERP 上开放五个职位：NodeX Agent 工程师、Delivery Engineer、Delivery Manager、面向企业、政府与国防的客户经理，以及业务类开放职位（[职位列表](https://herp.careers/v1/nodex)）。

- **NodeX Agent 工程师**——必需：Linux 开发；Rust（非商业经验亦可）；需求定义、基本设计和单元／集成测试；代码评审；在规格未定时自主推进开发。优先：针对威胁模型选择与组合密码原语；兼顾 CRYPTREC 或 FIPS 的算法选择；TLS 握手与记录协议；威胁建模；Rust 商业开发；Windows 开发；安全编码；DID 与 Verifiable Credentials；依据 RFC 开发产品；概念层面了解后量子密码或零知识证明；X.509 与 PKI；GCP（[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)）。
- **Delivery Engineer**——必需：在客户支持、技术支持或导入工作中担任技术主导；读代码并定位问题；在架构与组件层面整理客户需求；编写技术文档。优先：网络与安全基础（TLS、PKI、证书、DNS）；复合机、物联网或安全领域的交付或支持；售前、SE 或现场工程；主导概念验证；数字身份、认证、授权与加密（[职位](https://herp.careers/v1/nodex/YOSy7rnYAP1r)）。
- **Delivery Manager**——必需：以负责人身份完成历时六个月以上、涉及多个组织的 IT 项目；具备与客户工程师讨论网络、TLS、PKI 和证书的技术素养。优先：与总包系统集成商合作的项目；政府、国防或准公共机构采购；医疗、金融、制造 OT 或能源等受监管行业（[职位](https://herp.careers/v1/nodex/lYSIMVfDShYE)）。

### 行业领域

关键基础设施的设备身份与零信任安全：国防与国家安全、医疗设备与网络、能源（含 VPP）、复合机和扫描仪等制造设备，以及移动出行与交通（[职位](https://herp.careers/v1/nodex)、[2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html)）。公司资料提到的相关标准与制度包括 W3C DID 与 Verifiable Credentials、DIF 的工作、CRYPTREC 与 FIPS、数字厅的零信任架构方针与 Trusted Web、IEC 62443 和 NIST SP800（[2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)、[2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html)）。Delivery Engineer 职位称不要求事先了解 DID、DIDComm 或零信任（“事前にこれらを知っている必要はありません”）；Delivery Manager 职位同样不要求事先了解 DID。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | Agent 工程师职位要求母语级日语。2023 年的职位列表中有一则英文“Chief of Staff (English ver)”职位。文化手册列有英语学习支持。 | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)、[归档职位列表，2023-03-07](https://web.archive.org/web/20230307164600/https://herp.careers/v1/collabogate)、[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 地点与远程 | 东京办公室（CIC Tokyo，虎ノ門ヒルズビジネスタワー 15F）或远程。Agent 职位：“国内でのフルリモートOK・全国勤務可”，需参加每月的 All Hands；所有职位都要求在公司指定日期到岗。客户经理职位为混合办公。 | [Agent 职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)、[客户经理职位](https://herp.careers/v1/nodex/_PTcDQIhGvBX) |
| 工时 | Agent、Delivery Engineer 和 Delivery Manager 职位为裁量労働制；客户经理职位为弹性工时，核心时间 10:00–15:00。文化手册（Ver.2025.03.10）写的是无核心时间的完全弹性工时，并含 45 小时固定加班费。 | [职位](https://herp.careers/v1/nodex)、[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 薪资 | Agent、Delivery Engineer、Delivery Manager 和客户经理职位为 800 万–1,500 万日元；业务类开放职位 800 万日元起。手册显示七个等级（G1–G7），图表范围为 300 万至 2,200 万日元。 | [职位](https://herp.careers/v1/nodex)、[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 股权 | “長期インセンティブ（ストックオプション）制度” | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| 雇佣形式与试用 | 正式员工或合同员工；试用期三个月；入职时给予五天带薪假 | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B) |
| 福利 | 社会保险（協会けんぽ）、生育、育儿与护理支持、远程办公支持；手册另列每月最高 3 万日元的通勤补贴和家政服务支持 | [职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)、[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 评估 | 每年 1 月和 7 月评定等级；按目标达成度评估业绩，并按四项价值观评估行为，参考同事意见 | [文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 招聘流程 | 简历筛选、休闲面谈、通常两轮面试、以聚餐形式进行的终面、录用与 HR 面谈 | [文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck) |
| 签证担保、应届生 | 所查看的职位均未说明 | [职位](https://herp.careers/v1/nodex) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：`nodex.inc` 站点地图中的页面（首页、产品、公司、招聘、用例、访谈、新闻、条款、隐私）和 `robots.txt`；托管在 Notion 上的 `docs.nodex.inc` 文档、`nodecross.app` 上的 API 参考，以及 `collabogate.notion.site` 上的安全方针、白皮书和招聘方针；PR TIMES 公司 ID 70282 的第 1–16 号新闻稿；HERP 职位列表和 HERP Career 公司页，以及 2023-03 和 2025-02 的 HERP 职位列表存档；国税庁 法人番号公表サイト、gBizINFO 和 ISMS-AC 登记；GitHub 组织 `nodecross`、`getunid`、`collabogate`、`nodexinc` 以及名称 `nodex` 和 `nodex-inc`；Speaker Deck；对 Wantedly、TokyoDev、Japan Dev、Zenn、Qiita、note 和 LinkedIn 的探查；相关域名的 WHOIS；以及以 NodeX、NODE X、ノードクロス、CollaboGate、UNiD 和三井正義进行的日英文检索。

- **营收、客户数与设备数。** 均未公开。
- **价格。** 没有价目表；提到了合同方案，但未作说明。
- **公司官网上的具名客户。** 官网和新闻稿只写“国内トップティアのメーカー”而不点名；东芝和三菱重工的名字来自 BRIDGE，而非公司本身。
- **估值。** 公司未披露。HERP Career 显示“評価額 18.5 億円”，并注明是根据登记资料估算（[HERP Career](https://herp.careers/careers/companies/nodex)；访问于 2026-10-11）。
- **工程团队人数。** 未说明；文化手册截至 Ver.2025.03.10 列出七名工程成员。
- **代理源代码。** 未公开。`nodecross/nodex` 仓库只有二进制文件；较早的 Rust 仓库 `nodex-didcomm` 已归档，2022 年前后的 `getunid/unid` 仓库返回 404。
- **工程博客。** 在 Zenn、Qiita、note 或公司官网上均未找到公司技术博客。Speaker Deck 上有 CEO 的演讲资料，包括 DIF Japan 月度会议的分享。
- **签证担保与英文职位。** 当前职位均未说明。
- **状态页或合同 SLA。** 未找到；白皮书给出 99.9% 的可用性目标。
- **专利。** gBizINFO 显示该法人番号名下专利、外观设计和商标均为 0，公司资料中也未提及任何专利（[gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965)；访问于 2026-10-11）。
- **LAC 自身的公告。** 未找到 LAC 关于其种子轮投资的公告。
- **2026-08-10 日经报道的内容。** 公司新闻索引列有“日本経済新聞 朝刊1面に当社の技術が紹介されました”及[转载链接](https://webreprint.nikkei.co.jp/r/806F2E1B44594CD380BB054593813E61/)，但该转载为加密 PDF，2026-10-11 无法读取。

### 不同来源之间的不一致

- **总部。** 登记的总部为東京都渋谷区円山町（Navi渋谷V 3F）（登记记录最后更新于 2025-03-19），[2026-03-02 MEEQ 公告](https://prtimes.jp/main/html/rd/p/000000013.000070282.html)中的本社也写作東京都渋谷区。公司页面、PR TIMES 公司资料、招聘职位和 ISMS 记录则写虎ノ門ヒルズビジネスタワー 15F（[国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)、[公司页面](https://nodex.inc/company)、[ISMS-AC](https://isms.jp/lst/ind/CR_JP027239.html)）。
- **办公室邮政编码。** 公司页面写 〒105-5515，日本邮政将其分配给[虎ノ門ヒルズステーションタワー 15F](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1055515)；2023-08-09 公告和文化手册的公司概况写 〒105-6415，即日本邮政为[虎ノ門ヒルズビジネスタワー 15F](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1056415)分配的编码；招聘职位和手册的工作地点页写 〒105-6490。三者对应的街道地址都是虎ノ門1-17-1 虎ノ門ヒルズビジネスタワー 15階。
- **员工人数。** 20 人（文化手册，Ver.2025.03.10）；“まだ20名未満の組織”（[访谈](https://nodex.inc/interview/interview02)，2025-03-10）；16 人（HERP 职位页公司信息栏；访问于 2026-10-11）；“20人ほど”（职位正文，2026-09-29）；涩谷事业所参保人数 13 人（[gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965)，养老保险数据，无日期）；11 人（[HERP Career](https://herp.careers/careers/companies/nodex)，按厚生年金参保人计，统计期截至 2026-08）。各来源的口径和日期不同。
- **开源。** 官网称 NodeX Agent 为“オープンソースの軽量ミドルウェア”，并称在 GitHub 分发二进制文件和示例代码（[产品页](https://nodex.inc/product)、[nodex.inc](https://nodex.inc/)；访问于 2026-10-11）。仓库 README 称未公开源代码，LICENSE 写明“It is NOT an open source license”，示例已于 2026-01-19 删除（[README](https://github.com/nodecross/nodex)、[LICENSE](https://github.com/nodecross/nodex/blob/main/LICENSE)）。
- **轮次名称。** 公司称 2025 年一轮为プレシリーズA；同一公告中 ITV 合伙人称“今回のシリーズAラウンド”，BRIDGE 一篇文章写作“総額6億円のシリーズAラウンド”（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)、[BRIDGE，2025-04-30](https://thebridge.jp/2025/04/can-generative-ai-reduce-office-energy-consumption-nodexs-vision-for-a-data-driven-society-with-decentralized-id-hot100-accenture-ventures-vol-6)）。
- **种子轮时间。** 种子轮于 2023-02-15 公布。ITV 称其于 2022 年投资，DNX 称首次投资在 2022 年 12 月；公司官网上的 DNX 访谈者提到“2022年には2.3億円のシード資金調達”，而高级交付经理的访谈称“2023年に累計2.3億円”（[DNX note](https://note.com/dnx_vc/n/n09886e4c33d1)、[interview01](https://nodex.inc/interview/interview01)、[interview02](https://nodex.inc/interview/interview02)）。
- **标准化工作的起点。** 2023 年种子轮公告称公司“2019年から”加入 W3C 和 DIF；CEO 称约 2018 年开始参加 DIF，2019 年加入；KDDI MUGENLABO 称他自 2018 年参与 W3C 规范制定；2026 年职位称创始成员“2017年から”身处 W3C 和 DIF（[2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)、[interview01](https://nodex.inc/interview/interview01)、[MUGENLABO](https://mugenlabo-magazine.kddi.com/list/nodex/)、[职位](https://herp.careers/v1/nodex/K8HNCsT2LA_B)）。
- **支持的平台。** README 列出“Linux kernel x86(32bit) & x86-64(64bit), FreeRTOS ARM Cortex-M33(32bit)”；文档列出 Ubuntu、Debian、Yocto、macOS 和 Windows 10；发布文件包含 x86_64 与 aarch64 Linux、Windows 和 macOS aarch64 构建，没有 FreeRTOS 构建（[README](https://github.com/nodecross/nodex)、[文档](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43)、[发布](https://github.com/nodecross/nodex/releases)）。
- **自建成本。** 首页称自建安全数据基础设施需要“数億円”；2025-03-19 公告称“数十億円の初期投資”（[nodex.inc](https://nodex.inc/)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)）。
- **技术负责人姓名。** 公司页面和访谈写川上 和良，文化手册写川上 和義（[公司页面](https://nodex.inc/company)、[文化手册](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)）。
- **产品发布时间。** CEO 将 NodeX 的发布时间定为“2023年8月”；而 2023-02-15 公告已把 NodeX 作为公司的解决方案介绍（[2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)、[2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)）。

### 其他

- **重名情况。** GitHub 组织 `nodexinc` 存在（创建于 2022-02-13，无仓库，无资料信息），未发现与本公司的关联（[GitHub API](https://api.github.com/orgs/nodexinc)）；`github.com/Nodex` 是 2011 年注册的无关用户账号。在 [2026-03-02 公告](https://prtimes.jp/main/html/rd/p/000000013.000070282.html)中用作联系链接的域名 `nodex.io` 通过美国注册商以隐私保护方式注册，2026-10-11 无法解析；公司自己的域名是 `nodex.inc` 和 `nodecross.app`。软件包和自由职业平台上还有其他与本公司无关、同样名为 NodeX 的项目。本页事实均对应 `nodex.inc`、CollaboGate 名称或ノードクロス。
- **定位变化。** 公司的描述从面向客户体验的 DID 平台（2021）转为面向制造商的物联网数据安全（2023）、边缘零信任数据基础设施（2025），再到以国防为先的关键基础设施安全（2026）；见`公司对产品的描述变化`。
- **公司新闻索引中的媒体条目**包括 2026-08-10 日本经济新闻早报头版的一则报道，以及在放射诊疗期刊 RadFan（2026 年 7 月号）投稿的“既存医療ネットワークにおけるサイバーセキュリティと医療機器保護”（[新闻](https://nodex.inc/news)、[RadFan](https://note.com/medical_radfan/n/ne1191dd62d19)）。
- **CEO 描述了 2024 年销售方式的变化。** 他说，在产品“なぜか刺さらない”的第一年之后，公司从 2024 年 1 月前后开始把 NodeX 作为直接解决各客户痛点的方案来介绍（[interview01](https://nodex.inc/interview/interview01)，2025-03-11）。
- **该公司在 PR TIMES 的第 12 号新闻稿返回 404**；公司新闻索引把 MEEQ 公告列在 2026-03-03，而 PR TIMES 的日期为 2026-03-02 09:00。

---

## 资料来源

**官方**

- [公司官网](https://nodex.inc/) · [产品](https://nodex.inc/product) · [公司](https://nodex.inc/company) · [招聘](https://nodex.inc/careers) · [用例](https://nodex.inc/usecase) · [新闻](https://nodex.inc/news) · [条款](https://nodex.inc/legal/terms)
- 用例——[产品服务化（2025-03-18）](https://nodex.inc/usecase/usecase01) · [公用设施设备节能（2025-03-18）](https://nodex.inc/usecase/usecase03)
- 访谈——[CEO，2025-03-11](https://nodex.inc/interview/interview01) · [高级交付经理，2025-03-10](https://nodex.inc/interview/interview02) · [CRO，2025-03-10](https://nodex.inc/interview/interview03) · [技术负责人，2025-03-10](https://nodex.inc/interview/interview05) · [CBO，2025-03-04](https://nodex.inc/interview/interview06)
- 文档——[NodeX ご利用ガイド](https://docs.nodex.inc/manual) · [はじめに](https://docs.nodex.inc/10bd301e9c6580beb40ecb3f72832d43) · [詳細仕様](https://docs.nodex.inc/10bd301e9c6580b99677d8323218a3fa) · [Agent 采集间隔](https://docs.nodex.inc/NodeX-Agent-11fd301e9c6580768821fed1c00063b4) · [GraphQL API](https://docs.nodex.inc/GraphQL-API-154d301e9c65803c9d44cea816bcdb44) · [归档设置](https://docs.nodex.inc/1e0d301e9c65802eb6b4cb049888a3b4)
- API 参考——[Agent API](https://agent-api-ref.nodecross.app/) · [Studio GraphQL API](https://studio-graphql-api-ref.nodecross.app/)
- 安全——[安全方针](https://collabogate.notion.site/NodeX-2edd301e9c658012afbff5f98688ba33) · [安全白皮书](https://collabogate.notion.site/2fbd301e9c6580aa8687d6c4f19d5ce5)
- GitHub——[`nodecross`](https://github.com/nodecross) · [`nodecross/nodex`](https://github.com/nodecross/nodex) · [发布](https://github.com/nodecross/nodex/releases) · [LICENSE](https://github.com/nodecross/nodex/blob/main/LICENSE) · [许可证变更提交](https://github.com/nodecross/nodex/commit/a0fea2fa7bf0fa21c56c94d1ea2a8b1dfc175544) · [删除示例提交](https://github.com/nodecross/nodex/commit/8684127d478fb52d055d204f18c726cede336a19) · [组织 API 记录](https://api.github.com/orgs/nodecross) · [`getunid`](https://github.com/getunid)
- 招聘——[HERP 职位列表](https://herp.careers/v1/nodex) · [NodeX Agent 工程师](https://herp.careers/v1/nodex/K8HNCsT2LA_B) · [Delivery Engineer](https://herp.careers/v1/nodex/YOSy7rnYAP1r) · [Delivery Manager](https://herp.careers/v1/nodex/lYSIMVfDShYE) · [客户经理](https://herp.careers/v1/nodex/_PTcDQIhGvBX)
- [文化手册，Ver.2025.03.10（Speaker Deck）](https://speakerdeck.com/ms256k1/collabogate-japan-zhu-shi-hui-she-culture-deck)

**新闻稿（PR TIMES，日文，较新在前）**

- [IIW #42 报告会——2026-05-12](https://prtimes.jp/main/html/rd/p/000000014.000070282.html)
- [MEEQ 解决方案合作——2026-03-02](https://prtimes.jp/main/html/rd/p/000000013.000070282.html)
- [プレシリーズA、累计 8.3 亿日元、更名——2025-03-19](https://prtimes.jp/main/html/rd/p/000000011.000070282.html)
- [路透社提及航空自卫队合作准备——2025-01-27](https://prtimes.jp/main/html/rd/p/000000010.000070282.html)
- [顾问元橋一之——2023-08-21](https://prtimes.jp/main/html/rd/p/000000009.000070282.html)
- [NR-Power Lab VPP——2023-08-09](https://prtimes.jp/main/html/rd/p/000000008.000070282.html)
- [种子轮，经 J-KISS 2.3 亿日元——2023-02-15](https://prtimes.jp/main/html/rd/p/000000007.000070282.html)
- [入选数字厅 Trusted Web——2022-09-13](https://prtimes.jp/main/html/rd/p/000000006.000070282.html)
- [Renesas Ready Partner——2022-06-08](https://prtimes.jp/main/html/rd/p/000000005.000070282.html)
- [PFU 概念验证——2021-11-29](https://prtimes.jp/main/html/rd/p/000000004.000070282.html)
- [Garage+ 第 12 期——2021-11-16](https://prtimes.jp/main/html/rd/p/000000003.000070282.html)
- [分布式物联网平台实证——2021-07-06](https://prtimes.jp/main/html/rd/p/000000002.000070282.html)
- [UNiD 合作伙伴招募——2021-03-10](https://prtimes.jp/main/html/rd/p/000000001.000070282.html)

**登记信息**

- [国税庁 法人番号公表サイト——6011001127965](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=6011001127965)
- [gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=6011001127965)
- [ISMS-AC——ISO/IEC 27001 JP027239](https://isms.jp/lst/ind/CR_JP027239.html) · [ISMS-AC——云安全 28118935](https://isms.jp/isms-cls/lst/ind/CR__x0032_8118935.html)
- 日本邮政邮编——[105-5515](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1055515) · [105-6415](https://www.post.japanpost.jp/cgi-zip/zipcode.php?zip=1056415)

**第三方报道与档案**

- [DNX Ventures——追加投資（日文），2025-03-19](https://note.com/dnx_vc/n/n09886e4c33d1)
- [BRIDGE——プレシリーズA（日文），2025-03-21](https://thebridge.jp/2025/03/node-x-a-platform-for-secure-transmission-of-real-world-data-raises-600-million-yen-in-pre-series-a-funding-from-dnx-and-itochu-affiliated-investors) · [HOT100 with Accenture Ventures（日文），2025-04-30](https://thebridge.jp/2025/04/can-generative-ai-reduce-office-energy-consumption-nodexs-vision-for-a-data-driven-society-with-decentralized-id-hot100-accenture-ventures-vol-6) · [IVS2025 分会场（日文），2025-07](https://thebridge.jp/2025/07/ai-era-collaboration-partners-intention-time-key-ivs2025)
- [KDDI MUGENLABO Magazine——CEO 访谈（日文），2025-05-12](https://mugenlabo-magazine.kddi.com/list/nodex/)
- [週刊BCN——CEO 人物介绍（日文），2025-11-27](https://www.weeklybcn.com/journal/era/detail/20251127_212929.html)
- [路透社——Japan hunts dual-use goods makers to aid military expansion，2025-01-22](https://www.reuters.com/business/retail-consumer/japan-hunts-dual-use-goods-makers-aid-military-expansion-2025-01-22/)
- [日经转载，2026-08-10（日文，加密 PDF）](https://webreprint.nikkei.co.jp/r/806F2E1B44594CD380BB054593813E61/) · [RadFan 投稿（日文）](https://note.com/medical_radfan/n/ne1191dd62d19)
- [HERP Career——公司资料（日文）](https://herp.careers/careers/companies/nodex)
- HERP 职位列表存档——[2023-03-07](https://web.archive.org/web/20230307164600/https://herp.careers/v1/collabogate) · [2025-02-19](https://web.archive.org/web/20250219084303/https://herp.careers/v1/collabogate)
- [GitHub API——`nodexinc`（同名；未发现与本公司的关联）](https://api.github.com/orgs/nodexinc)
