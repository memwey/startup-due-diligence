# Anyflow

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Anyflow（Anyflow株式会社，法人番号 1011001109588）是一家东京公司，主力产品 **Anyflow Embed** 是一款嵌入式 iPaaS（組み込み型iPaaS）：SaaS 厂商利用其无代码编辑器、连接器和 JavaScript SDK，在自家产品内向用户提供与其他 SaaS 的集成。公司还销售 **Anyflow Automation**，产品页将其描述为把 SaaS 厂商产品与企业核心系统连接起来的“Headless iPaaS”（[官网首页](https://anyflow.jp/)；无日期，访问于 2026-10-11）。公司称成立于 2016-02-12；该法人最初名为 Revode株式会社，2017 年更名为株式会社ピケ，2019 年更名为 Anyflow株式会社（[国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)；截至 2026-10-11 的记录）。自 2024-12-10 起，公司成为 CO2 排放核算 SaaS 企业アスエネ株式会社（Asuene）的全资子公司（[Asuene 公告](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)、[Anyflow 公告](https://anyflow.jp/news/asuene-groupin)；均为 2024-12-10）。

- 被收购前的融资：2019-09-24 获 Coral Capital 2,000万日元种子轮；2020-01-08 完成由 Global Brain 和 Globis Capital Partners 领投的约 2.2 亿日元 pre-Series A；2022-12-08 与スマレジ（Smaregi）资本业务合作（金额未披露）。Asuene 的收购公告称 Anyflow 此前“累計約3.4億円”；收购价格未披露（[Asuene，2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)）。
- 公司披露的规模：Embed 上线第一年客户发布 247 个集成，累计执行超过 2,400 万次（[2024-07-16](https://anyflow.jp/news/anyflow-embed-1st-anniv)）；可连接“200種以上”云服务（[2026-05-28](https://anyflow.jp/news/iGZsEBie)）。2025-06-11 的公告援引デロイト トーマツ ミック経済研究所的报告，称 Embed 在“IT・Web向けSaaS開発連携型ツール”中份额第一（[2025-06-11](https://anyflow.jp/news/2025-share-no1)）。
- 员工人数：“30名(業務委託含む)”（[HERP 职位](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)，发布于 2025-12-22；访问于 2026-10-11）。公司发布的其他数字从约 20 人到“30名強”不等（见“备注”）。
- 工程（据招聘信息）：Embed 使用 **Python（FastAPI、Django ORM、Celery）**，前端为 **TypeScript/React**，数据层为 **MySQL（Cloud SQL）** 和 **Redis**，运行在 **GCP/GKE** 上，使用 Terraform 和 ArgoCD；Automation 团队在 Cloud Run 上用 **TypeScript（Deno、Node.js）** 编写客户工作流。安全政策称所有生产系统运行在日本区域的 Google Cloud 上（[安全政策](https://docs-embed.anyflow.jp/policy/security-policy)；无日期，访问于 2026-10-11）。职位均以日文发布，未找到关于英语工作语言的说明；以远程为主，弹性工时核心时间为 10:30–17:30（[招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)；无日期，访问于 2026-10-11）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前公开品牌 | Anyflow；产品为 Anyflow Embed 和 Anyflow Automation | [官网首页](https://anyflow.jp/)；访问于 2026-10-11 |
| 法定名称 | Anyflow株式会社 / Anyflow Inc.（フリガナ：エニーフロー） | [公司页面](https://anyflow.jp/about)、[国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588) |
| 法人番号 | 1011001109588，指定于 2016-02-17；适格请求书登记号 T1011001109588 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)、[公司页面](https://anyflow.jp/about) |
| 曾用法定名称 | Revode株式会社（至 2017-05-31）；株式会社ピケ（2017-05-31 至 2019-01-30） | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588) |
| 成立 | 2016-02-12（公司陈述） | [公司页面](https://anyflow.jp/about) |
| 登记总部 | 東京都港区新橋2丁目20番15号 新橋駅前ビル1号館6階，自 2025-04-16 起登记 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)；截至 2026-10-11 的信息 |
| 公司页面地址 | 〒105-0001 東京都港区虎ノ門1-3-1 東京虎ノ門グローバルスクエア6階——与 Asuene 于 2026-05-25 迁入的总部地址相同 | [公司页面](https://anyflow.jp/about)、[Asuene，2026-05-07](https://prtimes.jp/main/html/rd/p/000000681.000058538.html) |
| 管理层 | 代表取締役CEO 坂本 蓮；取締役CTO 大久保 陽平；執行役員COO 阿部 遼介 | [公司页面](https://anyflow.jp/about)；访问于 2026-10-11 |
| 股东 | アスエネ株式会社，自 2024-12-10 起持股 100% | [公司页面](https://anyflow.jp/about)、[Asuene，2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html) |
| 资本金 | 1,000万日元 | [HERP 职位](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)；访问于 2026-10-11 |
| 员工人数 | “30名(業務委託含む)”；其他数字见“备注” | [HERP 职位](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)，发布于 2025-12-22 |
| 工作语言 | 查阅到的职位均以日文撰写；工作流构建工程师职位要求商务级日语；没有职位或 FAQ 说明以英语为工作语言 | [招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)、[工作流构建工程师职位](https://herp.careers/v1/anyflow/Jht3MH0DI3if)；访问于 2026-10-11 |
| 累计融资 | 被收购前“累計約3.4億円”（Asuene 的说法）；公司自身最后公布的数字为 pre-Series A 后约 2.6 亿日元 | [Asuene，2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)、[Anyflow，2020-01-08](https://anyflow.jp/news/pre-seriesA-fundraise) |
| 已公开投资方 | Coral Capital、Global Brain、Globis Capital Partners、スマレジ；天使投资人古川健介、堀井翔太、赤坂优（据 BRIDGE） | [种子轮](https://anyflow.jp/news/seed-finance)、[pre-Series A](https://anyflow.jp/news/pre-seriesA-fundraise)、[スマレジ](https://prtimes.jp/main/html/rd/p/000000017.000034258.html)、[BRIDGE，2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding) |
| 安全认证 | ISMS IS 751085，JIS Q 27001:2025（ISO/IEC 27001:2022+Amd 1:2024），认证机构 BSI Group Japan；首次登记 2021-10-12，有效期至 2027-10-11；范围“iPaaSの企画・開発及び運営” | [ISMS 登记](https://isms.jp/lst/ind/CR_IS_x0020_751085.html)；访问于 2026-10-11 |
| 专利 | JP7645548B2「システム、方法、およびプログラム」，申请号 JP2022-103544，申请日 2022-06-28，发明人坂本 蓮、大久保 陽平、川村 将史；Google Patents 显示授权日期 2025-03-14 | [Google Patents](https://patents.google.com/patent/JP7645548B2/ja)、[JP2024004078A](https://patents.google.com/patent/JP2024004078A/ja) |
| 托管 | “すべてのプロダクションシステムとデータベースは、日本にホストされているGoogle Cloud Platformで稼働” | [安全政策](https://docs-embed.anyflow.jp/policy/security-policy)；访问于 2026-10-11 |

### 品牌与法律实体

| 名称 | 类型 | 期间 | 来源中所述关系 | 来源 |
|---|---|---|---|---|
| Revode株式会社 | 曾用法定名称 | 2016-02 至 2017-05-31 | 同一法人番号 1011001109588 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588) |
| 株式会社ピケ | 曾用法定名称 | 2017-05-31 至 2019-01-30 | 同一法人番号；2018 年发布云端 RPA“Anybot” | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)、[PR TIMES，2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html) |
| Anybot | 曾用产品品牌 | 自 2018-10-24 开放预注册 | 株式会社ピケ的云端 RPA；`anybot.ai` 现跳转至 `anyflow.co.jp`，后者再跳转至 `anyflow.jp`（2026-10-11 检查） | [PR TIMES，2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html) |
| Anyflow（最初的 iPaaS） | 同一法人的早期产品 | 自 2019-10 起 β | 面向一般企业的无代码 SaaS 间自动化；CTO 称 Embed 是从零构建，而非在其基础上扩展 | [pre-Series A 公告](https://anyflow.jp/news/pre-seriesA-fundraise)、[Green CTO 介绍](https://www.green-japan.com/company/10894/pr) |
| アスエネ株式会社 | 母公司 | 自 2024-12-10 起 | 取得 100% 股份；在集团公司列表中称其为“AIデータ連携プラットフォーム「Anyflow」” | [Asuene，2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)、[Asuene，2026-06-26](https://prtimes.jp/main/html/rd/p/000000711.000058538.html) |

公司自己的通知称更名为 Anyflow株式会社的日期为 2019-01-17（[2019-01-17](https://anyflow.jp/news/rename-company-name)）；登记记录为 2019-01-30（见“备注”）。

**项目与奖项**（除另有说明外均为公司公布）：IVS 2019 Summer Launchpad 决赛入围、Incubate Camp 12th 综合第一、B Dash Camp 2019 Fall Pitch Arena 优胜（[pre-Series A 公告](https://anyflow.jp/news/pre-seriesA-fundraise)、[PR TIMES，2019-11-05](https://prtimes.jp/main/html/rd/p/000000004.000034258.html)）；第 8 期 FUJITSU ACCELERATOR 路演大赛優秀賞（[2020-02-10](https://anyflow.jp/news/fujitsu-accelerator)）；EY Innovative Startup 2020（[PR TIMES，2020-02-28](https://prtimes.jp/main/html/rd/p/000000007.000034258.html)）；最初的 Anyflow 产品被列为经济产业省 IT導入補助金2020 的 IT 工具（[PR TIMES，2020-08-06](https://prtimes.jp/main/html/rd/p/000000014.000034258.html)）；CEO 入选 Forbes 30 Under 30 Asia 2022 Enterprise Technology（[2022-05-26](https://anyflow.jp/news/forbes-30-under-30-asia-2022)）。招聘页链接了在 Startup Aquarium 2023 和 2024 上的电梯演讲（[招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)）。

### 公司陈述的市场背景

- Embed 页面援引 SaaStr Annual 2021，称考虑购买 SaaS 的用户中有 30% 需要与其他 SaaS 集成，并称自行开发一个集成通常需要 3–6 个月（[Embed 页面](https://anyflow.jp/products/embed)；无日期，访问于 2026-10-11）。
- 公司对 111 名 B2B SaaS 采购负责人的调查（通过 IDEATECH 的リサピー进行网络调查，2026-05-18 至 05-19）称，75.7% 曾在比较功能或价格之前就因 API 集成不足而排除某款 SaaS，63.1% 曾因缺少集成而选择其他服务（[2026-07-14](https://anyflow.jp/news/3RLk2a_Q)）。该公告标题使用了不同的数字（见“备注”）。
- Asuene 的收购公告以 SSBJ 标准下的 Scope 1–3 披露以及从 ERP 和 SaaS 系统收集活动量数据的工作量来说明此次交易（[Asuene，2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)）。

---

## 产品

### 产品定位与功能领域

**Anyflow Embed**——“SaaS事業者向けの組み込み型iPaaS”，让厂商“最短1週間”向用户提供与其他系统的集成（[官网首页](https://anyflow.jp/)）。自 2023-07-13 起正式发布（[2023-07-13](https://anyflow.jp/news/anyflow-embed)）；BRIDGE 报道称其此前已开发约两年，并以隐身模式提供服务（[BRIDGE，2023-07-13](https://thebridge.jp/2023/07/anyflow-embed-official-launch)）。[docs-embed.anyflow.jp](https://docs-embed.anyflow.jp/) 上的文档（[sitemap](https://docs-embed.anyflow.jp/sitemap-pages.xml) 中共 149 页，访问于 2026-10-11）结构如下：

| 领域 | 文档内容 |
|---|---|
| 解决方案编辑器 | 触发器（轮询、实时、定时；由厂商发起的 Webhook、Request 和“My Event”触发器）、动作（内置、HTTP 和自定义 API 调用；键值存储、日志和邮件；CSV、日期时间、列表、变量，以及需申请开启、禁用 `import` 的受限 [Python 动作](https://docs-embed.anyflow.jp/solution-editor/actions/data-transform/python)）、逻辑（if、循环、分页、错误监控、停止）、变量 |
| 向导编辑器 | 嵌入厂商产品中的终端用户设置界面，含映射、条件、CSV、table-assist 等组件 |
| 发布 | 部署与[部署环境](https://docs-embed.anyflow.jp/release/deploy-environment)（开发／预发布／生产）、通过 SDK 嵌入并使用厂商生成的 [RS256 JWT](https://docs-embed.anyflow.jp/release/embed/generate-jwt)、在 Anyflow 域名上的[向导托管](https://docs-embed.anyflow.jp/release/wizard-hosting) |
| Anyflow SDK | npm 上的 `@anyflowinc/embed-sdk`；[变更记录](https://docs-embed.anyflow.jp/anyflow-sdk/docs/changelog)至 v0.16.0（2026-03-18） |
| Anyflow API | End-user API、[Vender Server API](https://docs-embed.anyflow.jp/anyflow-api/vender-server-api)（以 API Secret 换取 Bearer token，地址 `embed-vender-api.anyflow.jp`）、Webhook |
| 运维 | 面向厂商和终端用户的执行历史、错误处理与重试、事件通知、[执行上限](https://docs-embed.anyflow.jp/ops/step-execution-limit) |
| 连接器 | 连接器列表、自定义 OAuth 客户端、各连接器注意事项 |
| 政策 | [安全政策](https://docs-embed.anyflow.jp/policy/security-policy)、[服务水平](https://docs-embed.anyflow.jp/policy/service-level)、[故障响应](https://docs-embed.anyflow.jp/policy/incident-response)、责任划分 |
| 代码解决方案（β） | 通过“Embed CLI”以 Deno 上的 TypeScript 编写集成逻辑，按 Claude Code、Codex 等编码代理的使用方式设计；自 2026-07 起仅向部分客户提供（[文档](https://docs-embed.anyflow.jp/release-notes/code-solution)、[2026-07-28](https://anyflow.jp/news/o3pigXgy)） |

有日期的功能发布包括：面向没有公开 API 的厂商的“My Event”（[2024-01-16](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)）；无需公开 API 即可双向交换数据的“リクエスト&レスポンス”（[2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html)）；在无代码流程中以指定语言和版本运行代码的“コードアクション”（[2025-04-17](https://anyflow.jp/news/code-action)）；以及“AI エージェント / RAG向けデータ自動連携サービス”，将客户在 Google Drive、Box、SharePoint、Gmail、Slack 等处的数据同步至向量数据库（[2026-05-28](https://anyflow.jp/news/iGZsEBie)）。[发布说明](https://docs-embed.anyflow.jp/release-notes/recent)列出了截至 2026-03-18 的较小改动。

**Anyflow Automation**——产品页将其描述为“SaaS事業者向けのHeadless iPaaS”，把企业客户的现有系统与厂商的 SaaS 集成：有 API 时用 API，否则用 CSV 或数据库连接，提供“100以上”连接器和全托管基础设施（[Automation 页面](https://anyflow.jp/products/automation)；无日期，访问于 2026-10-11）。招聘信息将交付描述为客户项目：工作流构建团队用 TypeScript 编写每个集成，一般采用瀑布式，企业项目规模在 10 人月以下（[工作流构建工程师职位](https://herp.careers/v1/anyflow/Jht3MH0DI3if)、[PM 负责人职位](https://herp.careers/v1/anyflow/T7Zo5Ic0m7_7)）。

**其他产品。** 2026-03-31 的通知宣布四款与スマレジ相关的集成应用于 2026-04-30 停止提供，并将“Anyflow Connect”列为后继服务，价格部分变更（[2026-03-31](https://anyflow.jp/news/smaregi-integration-end)）；未找到 Anyflow Connect 的产品页。技术客户成功职位提到为特定客户部署的“Anyflow Embedカスタムメイド版”（[职位](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)）。

### 商业化

Embed 和 Automation 均无公开价目表；两个产品页都引导至演示或咨询表单。[使用条款](https://anyflow.jp/terms)（2019-11-29 制定，最近一次修订 2022-07-20）将费用分为初始导入费、月度固定费、月度按量费、选项费和其他费用，金额均在申请书中约定，开具发票并以银行转账支付；除按量费外，整个合同期的费用须在服务开始月份的次月月底前一次性支付。Embed 页面称集成的构建、设计、测试和部署可由客户自行完成，也可委托 Anyflow（[Embed 页面](https://anyflow.jp/products/embed)）。早期产品曾公布价格：Anybot 测试期间“月額7万円から”（[2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html)），最初的 Anyflow“月額3万円から”（[2020-08-06](https://prtimes.jp/main/html/rd/p/000000014.000034258.html)）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2019-09-24 | 支持约 10 款 SaaS，以日本国内产品为主（最初的 Anyflow） | [BRIDGE](https://thebridge.jp/2019/09/anyflow-seed-round-funding) |
| 2020-01-08 | 上线以来企业咨询“数百件以上”；付费用户“出始めた” | [BRIDGE](https://thebridge.jp/2020/01/anyflow-pre-series-a-round-funding) |
| 2023-07-13 | 正式发布时公开可知的 Embed 用户为 16 家 SaaS 公司 | [BRIDGE](https://thebridge.jp/2023/07/anyflow-embed-official-launch) |
| 2024-07-16 | 2023-07-13 至 2024-07-12 期间在 Embed 上发布到生产环境的集成 247 个；累计执行超过 2,400 万次 | [Anyflow](https://anyflow.jp/news/anyflow-embed-1st-anniv) |
| 2025-02-19 | “140種類以上の連携コネクタ” | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000032.000034258.html) |
| 2025-06-11 | 在デロイト トーマツ ミック経済研究所“SaaS管理・運用・開発市場(SaaS for SaaS)の実態と展望 2024年度版”中，“IT・Web向けSaaS開発連携型ツール”份额第一 | [Anyflow](https://anyflow.jp/news/2025-share-no1) |
| 发布于 2025-12-12 | “日々数十万件タスクを処理” | [SRE 职位](https://herp.careers/v1/anyflow/5sHcw3MfypEy) |
| 2026-05-28 | 可连接“200種以上のクラウドサービス” | [Anyflow](https://anyflow.jp/news/iGZsEBie) |
| 访问于 2026-10-11 | 网站连接器 sitemap 中有 165 个连接器页面 | [sitemap](https://anyflow.jp/sitemap.xml) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2022-12-08](https://prtimes.jp/main/html/rd/p/000000017.000034258.html) | スマレジ | 资本业务合作；Embed 用于スマレジ POS 与电商网站及 Google Sheets 的集成 |
| [2023-07-19](https://prtimes.jp/main/html/rd/p/000000019.000034258.html) | 弥生 | 业务合作；Embed 被采用为弥生会計等产品的 API 集成基础 |
| [2023-08-29](https://anyflow.jp/news/smarthr-plus) | SmartHR／freee | 为 SmartHR Plus 应用商店开发“freee人事労務 年末調整連携 by Anyflow Embed” |
| [2023-11-29](https://anyflow.jp/news/anyflow-embed-netprotections) | ネットプロテクションズ | NP掛け払い采用 Embed |
| [2024-03-12](https://anyflow.jp/news/moneyforward-cloud) | マネーフォワード | Embed 推出五款マネーフォワード クラウド产品的连接器 |
| [2024-07-16](https://anyflow.jp/news/anyflow-embed-1st-anniv) | DIGGLE、インフォボックス、KAEN、日本パープル、Sales Marker、SmartHR、Srush 及另外四家 | 一周年之际公开客户评价 |
| [2025-02-19](https://prtimes.jp/main/html/rd/p/000000032.000034258.html) | アスエネ（母公司） | ASUENE 采用 Embed；Asuene 宣布与勘定奉行クラウド、freee会計和 ESGTech 集成（[Asuene](https://prtimes.jp/main/html/rd/p/000000461.000058538.html)） |
| [2025-05-23](https://anyflow.jp/news/case-smarthr) | SmartHR | 案例：一年内交付 15 个集成 |

### 公开计划

- 代码解决方案：在正式发布前实现部署功能、在管理界面显示执行日志，并扩充支持的应用（[2026-07-28](https://anyflow.jp/news/o3pigXgy)）。
- 集团整合：借助 Asuene 的销售基础扩大 Embed 的销售网络，并将 Anyflow 的集成技术用于 CO2 数据收集（[2024-12-10](https://anyflow.jp/news/asuene-groupin)）。
- 企业市场：企业 BizDev 职位称 SMB 业务在增长，招聘人员向企业客户推广解决方案，并以地方银行（地銀）为客户示例（[职位](https://herp.careers/v1/anyflow/oMisMJmQvdea)，发布于 2026-07-23）。

---

## 创始人

**坂本 蓮（Ren Sakamoto）**——代表取締役CEO（[公司页面](https://anyflow.jp/about)）。

- 初中开始编程（[Wantedly 职位，2024-05-11，已关闭](https://www.wantedly.com/projects/1698588)）。
- 大学四年级时入选 KDDI 的加速器 KDDI ∞ Labo；因项目要求成立公司，于毕业前的 2 月创立公司（[Founder 访谈，2019-06-17](https://found-er.com/interview/1442/)）。BRIDGE 报道称，他此前开发过面向程序员的修 bug 支援平台 AppMotor，入选 ∞ Labo 第 9 期（[BRIDGE，2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding)）。
- 毕业后加入 CyberAgent，负责维护 Ameba 的基础设施（[Founder 访谈](https://found-er.com/interview/1442/)）；后来的一则职位将该岗位描述为服务端工程师（[Wantedly](https://www.wantedly.com/projects/1698588)）。
- 本人称做过约 20 款产品，包括午餐应用“Dish”，并称 Anyflow 起初是 RPA 产品，后来转向 iPaaS（[Founder 访谈](https://found-er.com/interview/1442/)）。2018-10-24 以株式会社ピケ CEO 身份发布云端 RPA Anybot（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000001.000034258.html)）。
- 入选 Forbes 30 Under 30 Asia 2022 Enterprise Technology（[2022-05-26](https://anyflow.jp/news/forbes-30-under-30-asia-2022)）；JP7645548B2 的发明人之一（[Google Patents](https://patents.google.com/patent/JP7645548B2/ja)）。

**联合创始人。** BRIDGE 在 2019 年将中西 奎太列为联合创始人（[BRIDGE，2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding)）；他未出现在当前的[公司页面](https://anyflow.jp/about)上。CEO 访谈称共有三位创始人，均为工程师（[Founder 访谈](https://found-er.com/interview/1442/)）；查阅的资料中均未提及第三位创始人的姓名。

### 主要管理层

**大久保 陽平（Yohei Okubo）**——取締役CTO。2021 年 1 月加入，最初以业务委托身份参与基于 Celery 的工作流引擎、SaaS 连接器、CI 自动化、日志监控和 Kubernetes 运维；约一年后，CEO 和前任 CTO 请他接任 CTO，前任 CTO 继续以工程师身份参与 Embed 开发。此前：应届加入一家大型网络广告代理商开发广告运营工具，之后以自由职业者身份担任技术负责人，并从事 SRE 和数据工程工作（[Green，访问于 2026-10-11](https://www.green-japan.com/company/10894/pr)）。JP7645548B2 的发明人之一。

**阿部 遼介**——執行役員COO（[公司页面](https://anyflow.jp/about)）。企业 BizDev 岗位直接向 COO 汇报（[职位](https://herp.careers/v1/anyflow/oMisMJmQvdea)）。未找到其履历。

**須永 智成**——Anyflow Embed 事業責任者・プロダクトオーナー；曾在一家金融集团（智能手机应用 PM）和互动视频初创公司 MIL 任职，2023 年加入（[2026-06-29](https://anyflow.jp/news/_8Tdn3Ok)）。

一则已关闭的 2024 年 Wantedly 职位还列出松田 光希（CFO，曾任上市公司 IPO 负责人）和藤本 遼平（市场营销，曾就职于 DeNA 和 Wantedly）（[Wantedly，2024-05-11](https://www.wantedly.com/projects/1698588)）；两人均未出现在当前公司页面上。招聘 FAQ 给出的组织构成为：工程师和设计师 55%，CS/CRE 和销售 40%，后台职能 5%（[招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)）。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2019-09 之前（未说明日期） | 天使轮（BRIDGE 的说法） | 未单独说明 | 古川健介、堀井翔太、赤坂优 | — | [BRIDGE](https://thebridge.jp/2019/09/anyflow-seed-round-funding) |
| 2019-09-24 | シードラウンド（J-KISS型新株予約権方式） | 2,000万日元 | Coral Capital | 含天使轮 5,000万日元（BRIDGE） | [Anyflow](https://anyflow.jp/news/seed-finance)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000034258.html) |
| 2020-01-08 | プレシリーズA | 约 2.2 亿日元 | グローバル・ブレイン（领投）、グロービス・キャピタル・パートナーズ（领投）、Coral Capital | 约 2.6 亿日元（公司） | [Anyflow](https://anyflow.jp/news/pre-seriesA-fundraise)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000005.000034258.html) |
| 2022-12-08 | 資本業務提携 | 未披露 | スマレジ | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000017.000034258.html) |
| 2024-12-10 | 完全子会社化（收购） | 未披露 | アスエネ取得 100% 股份 | 被收购前“累計約3.4億円”（Asuene） | [Asuene](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)、[Anyflow](https://anyflow.jp/news/asuene-groupin) |

Coral Capital 参与了种子轮，并在 pre-Series A 中跟投。pre-Series A 公告称资金将用于加强和加快产品开发，并计划将来成为整合和管理国内外 SaaS 的平台（[2020-01-08](https://anyflow.jp/news/pre-seriesA-fundraise)）。スマレジ资本业务合作与スマレジ将 Embed 用于 POS 与电商集成同时公布，弥生业务合作在七个月后公布；Embed 于两者之间的 2023-07-13 正式发布。查阅的资料均未拆分约 2.6 亿日元（2020 年）与约 3.4 亿日元（2024 年）之间的差额，也未披露スマレジ的出资金额。

---

## 工程

### 技术栈与平台

**由文档或公开资产确认**

- **托管：** 所有生产系统和数据库运行在日本区域的 Google Cloud 上（[安全政策](https://docs-embed.anyflow.jp/policy/security-policy)）。公开的[状态页](https://anyflow-embed.statuspage.io/)将 GKE、Cloud SQL、Stackdriver 以及 Netlify（源服务器和边缘网络）列为监控组件（访问于 2026-10-11）。
- **SDK：** `@anyflowinc/embed-sdk`，[npm](https://www.npmjs.com/package/@anyflowinc/embed-sdk) 上的 JavaScript/TypeScript SDK——首次发布于 2023-05-19，v0.16.0 发布于 2026-03-18；其开发依赖包括 TypeScript、Rollup、Jest 和 ESLint（npm registry 元数据，访问于 2026-10-11）。向导在 iframe 中渲染，并以厂商后端签名的 RS256 JWT 认证（[SDK 文档](https://docs-embed.anyflow.jp/anyflow-sdk/docs)、[JWT 文档](https://docs-embed.anyflow.jp/release/embed/generate-jwt)）。
- **代码解决方案：** 基于 **Deno 2.x** 的 TypeScript；`embed` CLI 二进制（无 Windows 版本，Windows 上使用 WSL）通过 **Auth0**（OAuth 2.0 Authorization Code Flow）登录；SaaS 客户端为 `@anyflowinc/<name>` 包，通过 `deno add` 添加；沙箱限制为内存 1 GiB、最长运行 60 分钟、不可写文件系统（[文档](https://docs-embed.anyflow.jp/release-notes/code-solution)）。JSR 上存在 `@anyflowinc` scope（创建于 2024-03-05），但未列出公开包（[JSR](https://jsr.io/@anyflowinc)；访问于 2026-10-11）。
- **Python：** 需申请开启的 Python 动作运行受限子集，禁用 `import`（[文档](https://docs-embed.anyflow.jp/solution-editor/actions/data-transform/python)）。
- **安全政策中提到的安全措施：** 管理界面登录仅限以 Google Workspace 等为 IdP 的 SSO；共享凭据使用 1Password；认证数据以 256 位加密存储（[安全政策](https://docs-embed.anyflow.jp/policy/security-policy)）。

**由当前招聘信息推断**（访问于 2026-10-11）

- **Embed 后端：** Python、FastAPI、Django ORM、Celery；设计方式为 DDD 和六边形架构（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)、[SRE](https://herp.careers/v1/anyflow/5sHcw3MfypEy)）。CTO 的介绍确认工作流引擎基于 Celery（[Green](https://www.green-japan.com/company/10894/pr)）。
- **Embed 前端：** TypeScript、React、Linaria、ESLint、Prettier、Jest（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)）。
- **数据：** Cloud SQL 上的 MySQL、Redis（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)）。
- **基础设施：** GCP（GKE、GCS、Cloud SQL、Cloud IAP、Cloud NAT、Cloud Build、BigQuery、Cloud KMS、Cloud Pub/Sub）、Kubernetes；CI/CD 与 IaC 使用 GitHub Actions、Cloud Build、ArgoCD、Terraform；监控与安全使用 Datadog、Stackdriver、Trivy（[SRE](https://herp.careers/v1/anyflow/5sHcw3MfypEy)）。
- **Automation 团队：** TypeScript（Deno、Node.js），运行于 GCP（Cloud Run、Cloud SQL、BigQuery、Cloud Logging、Cloud KMS、Cloud Scheduler、Cloud Storage、Cloud Armor、Identity Platform、Firestore），以及 Resend；GitHub Actions、Cloud Build、Terraform（[工作流构建工程师职位](https://herp.careers/v1/anyflow/Jht3MH0DI3if)）。
- **工具：** Linear、Notion、Slack、GitHub；可用的 AI 工具列为 Claude Code、GitHub Copilot、CodeRabbit、ChatGPT、Devin、Gemini（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)）。

**仅见于招聘要求：** React（Next.js）、Airflow 和 Digdag 只作为加分项出现（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)）。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 工作流引擎 | 执行集成“解决方案”的自研引擎；软件工程师岗位负责新功能、改进和提速 | [软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)、[Green](https://www.green-japan.com/company/10894/pr) |
| 连接器 | 各 SaaS 的连接器，含认证（包括自定义 OAuth 客户端），并在第三方 API 变更时维护；CRE 人员用“コネクタSDK”以 Python 开发模块 | [Embed 页面](https://anyflow.jp/products/embed)、[CRE 职位](https://herp.careers/v1/anyflow/IZa74EMW4xS1) |
| 向导与 SDK | 终端用户设置界面通过 iframe 嵌入，或托管在 Anyflow 域名上；以 JWT 标识厂商的用户 | [SDK 文档](https://docs-embed.anyflow.jp/anyflow-sdk/docs)、[向导托管](https://docs-embed.anyflow.jp/release/wizard-hosting) |
| 厂商侧触发器 | Webhook、Request（含响应步骤）和 My Event 触发器让厂商无需公开 API 即可推送数据；每个来源 IP 每 10 秒 100 次请求的限额，请求大小软上限 20 MB | [上限](https://docs-embed.anyflow.jp/ops/step-execution-limit)、[2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html) |
| 代码解决方案运行环境 | 在沙箱中以 Deno 执行由代理编写的 `main.ts`，通过 `embed pull`／`embed push` 同步 | [文档](https://docs-embed.anyflow.jp/release-notes/code-solution) |
| AI 代理／RAG 数据同步 | 按计划从 200 多项服务收集客户的文档和消息并写入向量数据库 | [2026-05-28](https://anyflow.jp/news/iGZsEBie) |
| 执行历史与监控 | 厂商和终端用户的执行历史、步骤级日志屏蔽、向六款外部工具发送事件通知（[2024-12-26](https://prtimes.jp/main/html/rd/p/000000031.000034258.html)）、间隔不超过 2 分钟的指标／日志／外形监控、自动扩缩容 | [发布说明](https://docs-embed.anyflow.jp/release-notes/recent)、[故障响应](https://docs-embed.anyflow.jp/policy/incident-response) |

文档列出的运行上限：每个动作步骤 10 MB 软上限（轮询触发器下为 1 MB），每步存储日志 100 MB 硬上限，解决方案超时 12 小时（[上限](https://docs-embed.anyflow.jp/ops/step-execution-limit)）。原始执行数据在执行结束 30 天后删除；每日加密备份最多保留 7 天（[安全政策](https://docs-embed.anyflow.jp/policy/security-policy)）。可用率目标为 99.8%，按季度计算；页面称目前未制定 SLA（[服务水平](https://docs-embed.anyflow.jp/policy/service-level)）。

### 招聘所需技术背景

- **软件工程师（Embed）：** 必需——Web API 的设计、开发和运维；数据库 schema 设计与运维；使用 Git 的团队开发；借助 Claude Code 等 AI 编码代理开发。加分——WYSIWYG 编辑器等复杂 Web 应用；GCP/Kubernetes 运维；异步处理；基于 CI 的自动化测试；性能改进和持续重构；DDD；外部 API 集成；主导 B2B 开发（[职位](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)）。
- **SRE：** 必需——Kubernetes 和云基础设施运维、数据库 schema 设计。加分——运维月访问量超过一亿的服务器、涵盖应用与基础设施的架构设计、外部 API 集成（[职位](https://herp.careers/v1/anyflow/5sHcw3MfypEy)）。
- **工作流构建工程师（Automation）：** 必需——受托开发或 SI 等客户项目经验（协调需求和变更、兼顾工期与质量）、单元测试。加分——项目管理、API 集成，以及涉及 CSV、数据库、批处理和作业设计的数据集成（[职位](https://herp.careers/v1/anyflow/Jht3MH0DI3if)）。
- **产品经理（Embed）：** 必需——Scrum 或敏捷开发、根据客户反馈持续改进、对 API/SaaS 集成（REST、OAuth、Webhook）的实务理解。加分——B2B SaaS 的 PdM 或技术型客户支持、DevOps 或开发效率改进（[职位](https://herp.careers/v1/anyflow/qs53UJS4TYOX)）。
- **CRE 与技术客户成功：** 必需——Web 服务技术支持或 CRE／导入工程师经验，企业岗位还需客户项目经验；加分——Python、外部 API 集成、开发项目管理（[CRE](https://herp.careers/v1/anyflow/IZa74EMW4xS1)、[TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)）。

### 行业领域

SaaS 之间及 SaaS 与核心系统之间的集成：第三方 API 认证（OAuth、API key）、API 版本变更、分页与速率限制、数据映射、对无 API 系统的 CSV 和数据库交换，以及会计（freee、マネーフォワード、弥生、勘定奉行）、人事（SmartHR）和 POS（スマレジ）等日本商务 SaaS。产品经理职位要求具备 API/SaaS 集成的实务知识；工程类岗位只把外部 API 集成经验列为加分项而非必需。技术客户成功岗位优先考虑金融行业经验，企业 BizDev 岗位优先考虑与地方银行的关系（[TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)、[BizDev](https://herp.careers/v1/anyflow/oMisMJmQvdea)）。通过母公司，部分工作涉及为 Scope 1–3 CO2 核算收集活动量数据（[Asuene，2025-02-19](https://prtimes.jp/main/html/rd/p/000000461.000058538.html)）。查阅的职位均未说明领域知识能否在入职后学习。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 职位和招聘页均为日文；工作流构建工程师要求商务级日语；未找到英文职位 | [招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)、[工作流构建工程师](https://herp.careers/v1/anyflow/Jht3MH0DI3if) |
| 远程 | 原则上以远程为主；线下活动（全员会、offsite）约每季度或每半年一次（计划）；目前不要求每周或隔周到岗；只要能参加线下活动，首都圈以外也可远程；也可在虎ノ門的 WeWork 办公。职位补充称部分岗位可能被要求到岗；TCS 岗位可能需常驻合作方 | [招聘 FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)、[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)、[TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO) |
| 工时 | 工程师实行弹性工时，核心时间 10:30–17:30（弹性时段 8:30–10:30、17:30–21:30）；业务岗位 9:30–18:30；加班“月10時間程度” | [招聘 FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)、[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX) |
| 薪资（年薪） | 软件工程师 600万–900万日元；SRE 800万–1,200万日元；产品经理 600万–1,000万日元；PM 负责人（Automation）700万–1,000万日元；工作流构建工程师 500万–650万日元；CRE 500万–700万日元；TCS 500万–800万日元；企业 BizDev 750万–1,150万日元。软件工程师和 SRE 职位的月薪包含 45 小时的固定加班费 | [HERP 职位列表](https://herp.careers/v1/anyflow)；访问于 2026-10-11 |
| 休假与试用 | 完全双休，年休 120 天，带薪年假可按半天休，产假、育儿假（有男性取得先例）；试用期 3 个月 | [软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX) |
| 福利 | 社会保险、健康检查、公司配发电脑、购书和外部培训支持、通勤补贴（每月上限 2 万日元）、提供 AI 工具账号 | [软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX) |
| 招聘流程 | 可选的休闲面谈、简历筛选、1–3 轮线上面试、可能布置技术课题、一面后通过 back check 做背景调查、可选的试用入职（合计约一天，加入 Slack） | [招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671) |
| 副业与业务委托 | 欢迎先以副业或业务委托形式加入 | [招聘 FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671) |
| 初级与应届 | 工程类职位要求至少三年 Web 开发经验；所列实习仅为网络研讨会支持和销售 | [HERP 职位列表](https://herp.careers/v1/anyflow) |
| 签证支持 | 查阅的职位均未说明 | — |
| 团队做法 | Embed 采用 Scrum（细化、计划、回顾）；Automation 项目一般采用瀑布式；Embed 工程师全员远程，每天约 30 分钟例会 | [软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)、[工作流构建工程师](https://herp.careers/v1/anyflow/Jht3MH0DI3if) |
| 年龄与离职 | 招聘 FAQ 称平均年龄约 36 岁（20 多岁约 10%，30 多岁约 60%，40 多岁约 30%）；2024 年 Wantedly 职位称约 34 岁，且此前两年没有全职成员离职 | [招聘 FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)、[Wantedly，2024-05-11](https://www.wantedly.com/projects/1698588) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：anyflow.jp 及其 sitemap、robots.txt、公司、产品、案例、新闻和法律页面；docs-embed.anyflow.jp 及其 sitemap；状态页；Notion 招聘页和全部 HERP 职位；PR TIMES 上 Anyflow 和 Asuene 的页面；国税庁 法人番号公表サイト、ISMS 登记和 Google Patents；GitHub 组织名 `anyflowinc`、`anyflow`、`anyflow-inc`、`anyflowjp`、`anyflow-jp` 查询，npm 和 JSR；note、Speaker Deck、Zenn、Qiita、connpass、Wantedly、Green、TokyoDev 和 Japan Dev；以 Anyflow、Anyflow株式会社、Anyflow Embed、株式会社ピケ和 Anybot 进行的日英文网络搜索；INITIAL 和 HERP 企业档案（仅作线索）。

- **营收、ARR 和客户数。** 未找到绝对数字。唯一的增长数字是 2024 年 Wantedly 职位中的“前ARR600%以上の成長”，未说明基数和期间（[Wantedly](https://www.wantedly.com/projects/1698588)）。
- **收购价格与スマレジ出资。** 金额和持股比例均未披露（[Asuene](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)、[スマレジ合作](https://prtimes.jp/main/html/rd/p/000000017.000034258.html)）。
- **价目表。** Embed、Automation 和 Anyflow Connect 均未公开。
- **技术博客。** 未找到。[note 账号](https://note.com/anyflow)仅有一篇文章（2020-05-11）；[Speaker Deck 账号](https://speakerdeck.com/anyflow)只有一份日期为 2024-02-13、仅含图片的公司介绍资料；未找到 Zenn publication、Qiita organization 或 connpass 群组。
- **开源。** GitHub 组织 [`anyflowinc`](https://github.com/anyflowinc)（“Anyflow Inc.”，创建于 2017-05-01，X 账号 `anyflowinc`，邮箱在 `anyflow.co.jp` 域名下）没有公开仓库（[GitHub API](https://api.github.com/orgs/anyflowinc)）。GitHub 用户 `anyflow` 属于无关的个人。npm 包 `@anyflowinc/embed-sdk` 未声明仓库或许可证。
- **SLA。** “現在 SLA を定めておりません”（[服务水平](https://docs-embed.anyflow.jp/policy/service-level)）。
- **第三位联合创始人的姓名、COO 的履历、签证支持和英语岗位。** 均未找到。

### 不同来源之间的不一致

- **成立日期：** 2016-02-12（公司页面和公告）；法人番号于 2016-02-17 以 Revode株式会社名义指定（[国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)）；BRIDGE 写公司于 2017 年创立（[2019-09-24](https://thebridge.jp/2019/09/anyflow-seed-round-funding)）。
- **更名日期：** 公司通知称“2019年1月17日より”更名（[通知](https://anyflow.jp/news/rename-company-name)）；登记记录的变更日期为 2019-01-30（[国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)）。
- **地址：** 登记自 2025-04-16 起为新橋2丁目20番15号；公司页面、2026 年公告和 ISMS 登记为虎ノ門1-3-1 東京虎ノ門グローバルスクエア6階；当前 HERP 职位和招聘页为虎ノ門1-10-5 KDX虎ノ門一丁目ビル WeWork 3階 アスエネ株式会社内；2025 年公告为同一栋楼的 WeWork 4階（[2025-06-11](https://anyflow.jp/news/2025-share-no1)）。
- **累计融资：** pre-Series A 后约 2.6 亿日元（公司及 [Forbes JAPAN](https://forbesjapan.com/articles/detail/31650)，均为 2020-01-08），而 [BRIDGE（2020-01-08）](https://thebridge.jp/2020/01/anyflow-pre-series-a-round-funding)写 2亿7,000万日元；被收购前约 3.4 亿日元（[Asuene，2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html)）；HERP 企业档案显示 2.8 亿日元，系根据登记资料估算（[HERP 档案](https://herp.careers/careers/companies/anyflow)；访问于 2026-10-11）。
- **员工人数：** 含业务委托“30名強”（[招聘 FAQ](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)）；“30名(業務委託含む)”（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)，发布于 2025-12-22）；Dev 约 20 人＋Biz 约 10 人（[TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)，发布于 2026-07-22）；Dev 13 人＋Biz 12 人，约 25 人（[产品经理](https://herp.careers/v1/anyflow/qs53UJS4TYOX)，发布于 2025-12-12）；Dev 11 人＋Biz 10 人，约 20 人（[CRE](https://herp.careers/v1/anyflow/IZa74EMW4xS1)，发布于 2025-12-12）。HERP 档案根据 2024-08 至 2026-08 的厚生年金参保数据显示为 18 人（[HERP 档案](https://herp.careers/careers/companies/anyflow)）。2024 年 5 月，Wantedly 列出 15 名成员、含业务委托 20 名（[Wantedly](https://www.wantedly.com/projects/1698588)）。
- **连接器数量：** “100以上”（[Automation 页面](https://anyflow.jp/products/automation)）、“140種類以上”（[2025-02-19](https://prtimes.jp/main/html/rd/p/000000032.000034258.html)）、“200種以上”（[2026-05-28](https://anyflow.jp/news/iGZsEBie)），网站 sitemap 中有 165 个连接器页面（访问于 2026-10-11）。各来源均未定义计数口径。
- **Anyflow Automation 的定位：** 用于企业核心系统集成的“SaaS事業者向けのHeadless iPaaS”（[Automation 页面](https://anyflow.jp/products/automation)）及客户数据集成项目（[工作流构建工程师](https://herp.careers/v1/anyflow/Jht3MH0DI3if)），与“自社の業務を自動化、効率化するためのプラットフォーム”（[招聘页](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671)）和“社内業務の自動化を支援する”（[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)）的描述不同。
- **调查数字：** 2026-07-14 公告的标题和导语称 91.9% 曾因 API 集成不足排除某款 SaaS；其摘要和详细结果对同一问题给出的是 75.7%（[2026-07-14](https://anyflow.jp/news/3RLk2a_Q)）。
- **ISMS 标准：** 文档中的安全政策引用 JIS Q 27001:2014（ISO/IEC 27001:2013）（[政策](https://docs-embed.anyflow.jp/policy/security-policy)）；登记显示为 JIS Q 27001:2025（ISO/IEC 27001:2022+Amd 1:2024）（[登记](https://isms.jp/lst/ind/CR_IS_x0020_751085.html)）。
- **My Event 发布日期：** 2024-01-16 作为新功能公布（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)）；后来的公告称其于 2023 年 12 月发布（[2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html)）。

### 其他

- 产品顺序：云端 RPA Anybot（2018-10 开放预注册，当时公司名为株式会社ピケ）→ 面向一般企业的最初 Anyflow iPaaS（2019-10 β）→ 面向 SaaS 厂商的 Anyflow Embed（2023-07-13 正式发布）→ Anyflow Automation、AI/RAG 数据同步（2026-05）和代码解决方案（2026-07 β）。CTO 称 Embed 是从零构建的，从立项到上线约四个月（[Green](https://www.green-japan.com/company/10894/pr)）。
- 专利表述从“特許出願中”（[2022-12-08](https://prtimes.jp/main/html/rd/p/000000017.000034258.html)、[2024-01-16](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)）变为 [Embed 页面](https://anyflow.jp/products/embed)上的“特許取得済”，与 Google Patents 所列的 JP7645548B2 授权一致。
- Asuene 在 2026-06-26 公告的集团公司列表中称 Anyflow 为“AIデータ連携プラットフォーム”（[Asuene](https://prtimes.jp/main/html/rd/p/000000711.000058538.html)）。
- 状态页的故障记录列出 2024-01-18 至 2026-08-25 的 20 起故障，其中 7 起与定时触发器未触发有关（[状态页](https://anyflow-embed.statuspage.io/)；访问于 2026-10-11）。
- Embed 的完整文档在 GitBook 上公开，包括 `llms-full.txt` 导出；产品页面链接至文档（“ドキュメントへ”）。
- 截至 2026-10-11，PR TIMES 列出 Anyflow 的 38 篇公告；2025-06-11 至 2026-05-28 之间没有新公告（[PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/34258)）。
- 2026-10-11 无法访问：一篇 CodeZine 文章（机器人验证）、TokyoDev 档案 URL（HTTP 403）、TechCrunch Japan 2019 年的文章（证书错误），以及 Forbes Asia 个人档案正文。

---

## 资料来源

**官方**

- [官网首页](https://anyflow.jp/) · [公司页面](https://anyflow.jp/about) · [sitemap](https://anyflow.jp/sitemap.xml)
- [Anyflow Embed](https://anyflow.jp/products/embed) · [Anyflow Automation](https://anyflow.jp/products/automation) · [连接器](https://anyflow.jp/connectors) · [案例](https://anyflow.jp/case)
- [使用条款](https://anyflow.jp/terms) · [隐私政策](https://anyflow.jp/privacy)
- [Embed 文档](https://docs-embed.anyflow.jp/) · [文档 sitemap](https://docs-embed.anyflow.jp/sitemap-pages.xml) · [发布说明](https://docs-embed.anyflow.jp/release-notes/recent) · [代码解决方案](https://docs-embed.anyflow.jp/release-notes/code-solution) · [SDK](https://docs-embed.anyflow.jp/anyflow-sdk/docs) · [SDK 变更记录](https://docs-embed.anyflow.jp/anyflow-sdk/docs/changelog) · [JWT](https://docs-embed.anyflow.jp/release/embed/generate-jwt) · [Vender Server API](https://docs-embed.anyflow.jp/anyflow-api/vender-server-api) · [部署环境](https://docs-embed.anyflow.jp/release/deploy-environment) · [向导托管](https://docs-embed.anyflow.jp/release/wizard-hosting) · [Python 动作](https://docs-embed.anyflow.jp/solution-editor/actions/data-transform/python) · [上限](https://docs-embed.anyflow.jp/ops/step-execution-limit)
- [安全政策](https://docs-embed.anyflow.jp/policy/security-policy) · [服务水平](https://docs-embed.anyflow.jp/policy/service-level) · [故障响应](https://docs-embed.anyflow.jp/policy/incident-response) · [状态页](https://anyflow-embed.statuspage.io/)
- [招聘页（Notion）](https://anyflow.notion.site/Anyflow-9b321b9a62724099be47115c093ed671) · [HERP 职位列表](https://herp.careers/v1/anyflow)——[软件工程师](https://herp.careers/v1/anyflow/NC0_ouH2OBRX)、[SRE](https://herp.careers/v1/anyflow/5sHcw3MfypEy)、[产品经理](https://herp.careers/v1/anyflow/qs53UJS4TYOX)、[工作流构建工程师](https://herp.careers/v1/anyflow/Jht3MH0DI3if)、[PM 负责人](https://herp.careers/v1/anyflow/T7Zo5Ic0m7_7)、[CRE](https://herp.careers/v1/anyflow/IZa74EMW4xS1)、[TCS](https://herp.careers/v1/anyflow/qYCdm6lIYZXO)、[企业 BizDev](https://herp.careers/v1/anyflow/oMisMJmQvdea)
- [GitHub 组织](https://github.com/anyflowinc) · [GitHub API](https://api.github.com/orgs/anyflowinc) · [npm](https://www.npmjs.com/package/@anyflowinc/embed-sdk) · [JSR scope](https://jsr.io/@anyflowinc) · [note（日文）](https://note.com/anyflow) · [Speaker Deck](https://speakerdeck.com/anyflow) · [公司介绍资料，2024-02-13](https://speakerdeck.com/anyflow/we-are-hiring)

**新闻稿（anyflow.jp，日文，较新在前）**

- [代码解决方案 β — 2026-07-28](https://anyflow.jp/news/o3pigXgy)
- [SaaS 采购者调查 — 2026-07-14](https://anyflow.jp/news/3RLk2a_Q)
- [与クラウドサーカス合办网络研讨会 — 2026-06-29](https://anyflow.jp/news/_8Tdn3Ok)
- [AI 代理／RAG 数据同步 — 2026-05-28](https://anyflow.jp/news/iGZsEBie)
- [停止スマレジ集成应用 — 2026-03-31](https://anyflow.jp/news/smaregi-integration-end)
- [份额第一 — 2025-06-11](https://anyflow.jp/news/2025-share-no1)
- [SmartHR 案例 — 2025-05-23](https://anyflow.jp/news/case-smarthr)
- [コードアクション — 2025-04-17](https://anyflow.jp/news/code-action)
- [被 Asuene 收购 — 2024-12-10](https://anyflow.jp/news/asuene-groupin)
- [Embed 一周年 — 2024-07-16](https://anyflow.jp/news/anyflow-embed-1st-anniv)
- [マネーフォワード クラウド — 2024-03-12](https://anyflow.jp/news/moneyforward-cloud)
- [NP掛け払い — 2023-11-29](https://anyflow.jp/news/anyflow-embed-netprotections)
- [SmartHR Plus 应用 — 2023-08-29](https://anyflow.jp/news/smarthr-plus)
- [Embed 正式发布 — 2023-07-13](https://anyflow.jp/news/anyflow-embed)
- [Forbes 30 Under 30 Asia — 2022-05-26](https://anyflow.jp/news/forbes-30-under-30-asia-2022)
- [FUJITSU ACCELERATOR 获奖 — 2020-02-10](https://anyflow.jp/news/fujitsu-accelerator)
- [pre-Series A — 2020-01-08](https://anyflow.jp/news/pre-seriesA-fundraise)
- [种子轮 — 2019-09-24](https://anyflow.jp/news/seed-finance)
- [更名为 Anyflow — 2019-01-17](https://anyflow.jp/news/rename-company-name)

**PR TIMES（日文）**

- [公司公告列表](https://prtimes.jp/main/html/searchrlp/company_id/34258)
- [ASUENE 采用 Embed — 2025-02-19](https://prtimes.jp/main/html/rd/p/000000032.000034258.html) · [错误通知扩展至六款工具 — 2024-12-26](https://prtimes.jp/main/html/rd/p/000000031.000034258.html) · [Request & Response — 2024-08-20](https://prtimes.jp/main/html/rd/p/000000026.000034258.html) · [My Event — 2024-01-16](https://prtimes.jp/main/html/rd/p/000000023.000034258.html)
- [弥生业务合作 — 2023-07-19](https://prtimes.jp/main/html/rd/p/000000019.000034258.html) · [スマレジ资本业务合作 — 2022-12-08](https://prtimes.jp/main/html/rd/p/000000017.000034258.html) · [IT導入補助金 — 2020-08-06](https://prtimes.jp/main/html/rd/p/000000014.000034258.html)
- [EY Innovative Startup 2020 — 2020-02-28](https://prtimes.jp/main/html/rd/p/000000007.000034258.html) · [pre-Series A — 2020-01-08](https://prtimes.jp/main/html/rd/p/000000005.000034258.html) · [B Dash Camp — 2019-11-05](https://prtimes.jp/main/html/rd/p/000000004.000034258.html) · [种子轮 — 2019-09-24](https://prtimes.jp/main/html/rd/p/000000003.000034258.html) · [Anybot（株式会社ピケ时期）— 2018-10-24](https://prtimes.jp/main/html/rd/p/000000001.000034258.html)
- Asuene：[100% 收购 — 2024-12-10](https://prtimes.jp/main/html/rd/p/000000438.000058538.html) · [通过 Anyflow 实现集成 — 2025-02-19](https://prtimes.jp/main/html/rd/p/000000461.000058538.html) · [总部搬迁 — 2026-05-07](https://prtimes.jp/main/html/rd/p/000000681.000058538.html) · [集团公司列表 — 2026-06-26](https://prtimes.jp/main/html/rd/p/000000711.000058538.html)

**登记信息**

- [国税庁 法人番号公表サイト — 1011001109588（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011001109588)
- [ISMS 登记 — IS 751085（日文）](https://isms.jp/lst/ind/CR_IS_x0020_751085.html)
- [Google Patents — JP7645548B2](https://patents.google.com/patent/JP7645548B2/ja) · [JP2024004078A](https://patents.google.com/patent/JP2024004078A/ja)

**第三方报道与档案**

- [BRIDGE — 种子轮，2019-09-24（日文）](https://thebridge.jp/2019/09/anyflow-seed-round-funding) · [pre-Series A，2020-01-08（日文）](https://thebridge.jp/2020/01/anyflow-pre-series-a-round-funding) · [Embed 正式发布，2023-07-13（日文）](https://thebridge.jp/2023/07/anyflow-embed-official-launch) · [收购，2024-12-12（日文）](https://thebridge.jp/2024/12/anyflow-was-acqired-by-asuene-strengthening-data-collaboration-towards-achieving-carbon-neutrality)
- [Forbes JAPAN — pre-Series A，2020-01-08（日文）](https://forbesjapan.com/articles/detail/31650)
- [Founder — CEO 访谈，2019-06-17（日文）](https://found-er.com/interview/1442/)
- [Green — 成员介绍（含 CTO）（日文）](https://www.green-japan.com/company/10894/pr) · [Embed 事业负责人访谈（日文）](https://www.green-japan.com/company/10894/interview)
- [Wantedly — Tech Lead 职位，2024-05-11，已关闭（日文）](https://www.wantedly.com/projects/1698588)
- [HERP — 企业档案（日文）](https://herp.careers/careers/companies/anyflow) · [INITIAL（日文）](https://initial.inc/companies/A-17184)
