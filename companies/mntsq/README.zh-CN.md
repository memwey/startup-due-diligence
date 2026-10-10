# MNTSQ

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

MNTSQ（MNTSQ株式会社，读作モンテスキュー；英文名 MNTSQ, Ltd.）是一家总部位于东京、设立于 2018-11-14 的公司。创始人兼 CEO 板谷 隆平（Ryuhei Itaya）是长岛·大野·常松律师事务所（長島・大野・常松法律事務所，“NO&T”）的律师；公司将 AI 工程师安野 贵博（安野 貴博，Takahiro Anno）和堅山 耀太郎（Yotaro Katayama）列为共同创始人。公司销售面向大型企业的合同生命周期管理系统 **MNTSQ CLM**，包括法务案件受理与合同审查（案件管理）、合同台账（契約管理）、条款级合同数据库，以及以 **MNTSQ AI契約アシスタント** 和 **MNTSQ AI Agent** 名义销售的基于 LLM 的功能。NO&T 于 2019 年出资 8 亿日元（8億円），并监修产品内置的合同范本和审查规则手册（playbook）。另外两家大型律师事务所——西村朝日（西村あさひ，2024 年）和森·滨田松本（森・濱田松本，2025 年）——此后也入股。

- 公司陈述的规模：日本营收前 100 强企业中有 41 家使用（[2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html)），截至 2026-06-12 为 42 家（[2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)）。公司还称，截至 2026-05，采用企业数（含集团子公司）已超过 2,000 家（[2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html)）。
- 融资：公司未公布累计融资额。已披露的轮次包括 NO&T 出资的 8 亿日元（[2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)）、ALL STAR SAAS FUND 出资的 10 亿日元シリーズB（[2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)），以及 2024 年来自三家企业风投、外加债券和贷款的约 10 亿日元（[2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)）。西村朝日与森·滨田松本的出资金额未披露。
- 团队：截至 2026-07-31 有员工 120 人。截至 2026-08，开发本部（開発本部）约 50 人，分为四个团队（[软件工程师（后端）职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11）。
- 工程：核心为 Ruby on Rails（自创立起即使用 Ruby），另有 Python 服务（FastAPI、Celery）和 Vue.js/TypeScript 前端。基础设施为 AWS（ECS/Fargate、Aurora MySQL、SQS、OpenSearch），并从 AWS 上的工作负载调用 Google Cloud（Vertex AI、Cloud Vision API）（[职位](https://hrmos.co/pages/mntsq/jobs/10055)、[技术博客，2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103)）。所查阅的职位均为日文，未写明英语要求。工程师采用混合办公，每月至少到岗 5 天。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前公开品牌 | MNTSQ（モンテスキュー）；主力产品“MNTSQ CLM” | [公司概要](https://mntsq.co.jp/about)；访问于 2026-10-11 |
| 法定名称 | MNTSQ株式会社 / MNTSQ, Ltd.；登记写法为ＭＮＴＳＱ株式会社，假名读音モンテスキュー | [国税厅法人番号公表网站](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433)（截至 2026-10-11 的信息） |
| 法人番号 | 7010001196433；法人番号指定日 2018-11-27 | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) |
| 成立 | 設立日 2018-11-14 | 公司新闻稿中的公司简介，例如 [2026-05-19](https://prtimes.jp/main/html/rd/p/000000094.000050130.html) |
| 总部 | 〒104-6004 東京都中央区晴海1-8-10 晴海アイランド トリトンスクエア オフィスタワーX棟 4階。登记地址自 2025-10-10 起变更为晴海１丁目８番１０号 | [公司概要](https://mntsq.co.jp/about)、[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) |
| 历史登记地址 | 千代田区神田司町2-21-3（至 2019-12-06）→ 千代田区岩本町3-5-2（至 2020-08-24）→ 中央区日本橋堀留町2-9-8（至 2022-08-12）→ 中央区日本橋堀留町1-9-8（至 2025-10-10） | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433) |
| 代表人 | 代表取締役 板谷 隆平（Founder / CEO） | [公司概要](https://mntsq.co.jp/about) |
| 资本金 | 1 亿日元（資本金 1億円） | [HRMOS 职位页的公司信息](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11 |
| 员工人数 | 120 人（従業員数 120名，截至 2026 年 7 月末） | [HRMOS 职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11 |
| 员工人数变化 | 2018 年创立时 4 人；截至 2022-07 为 50 人；“100名近く”（2025-10）；“社員数100名強”（2026-06） | [2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html)、[2025-10-09](https://prtimes.jp/main/html/rd/p/000000071.000050130.html)、[2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html) |
| 人员构成 | 产品 41%、业务 46%、职能 13%，含董事（截至 2026-09） | [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)（标注 2026-09-01 更新） |
| 工作语言 | 未找到全公司或工程团队的语言政策。所查阅的职位和招聘页面全部为日文，均未提及英语 | [HRMOS 职位列表](https://hrmos.co/pages/mntsq/jobs)、[招聘网站](https://careers.mntsq.co.jp/)；访问于 2026-10-11 |
| 客户 | 日本营收前 100 强中的 41 家（2026-05）；42 家（截至 2026-06-12）；采用企业 2,000 家以上，含集团子公司（截至 2026-05） | 见“规模变化” |
| 累计融资 | 公司未公布 | 见“融资” |
| 公司列出的投资方 | NO&T、PKSHA Technology、ALL STAR SAAS FUND、かんぽNEXTパートナーズ、三菱UFJイノベーション・パートナーズ、日揮みらい投資事業有限責任組合、西村あさひ法律事務所・外国法共同事業、森・濱田松本法律事務所外国法共同事業（债券：あおぞらHYBRID3号投資事業有限責任組合；贷款：商工組合中央金庫） | 见“融资”中的新闻稿 |
| 安全认证 | ISO/IEC 27001:2022 及 JIS Q 27001:2023，证书编号 IS 798405，由 BSI Japan 颁发。认证范围：契約業務に関する自社SaaSの研究・開発・運用・保守。首次登记 2024-01-22 | [公告，2024-03-22](https://mntsq.co.jp/news/information/202403-isms) |

**项目与奖项。** 公司入选日经“NEXTユニコーン調査2024”（[公告，2025-01-17](https://mntsq.co.jp/news/information/nextunicorn2024)）。公司入选“かんぽ生命 - アフラック - 日本郵便 Acceleration Program 2025”（[2025-08-15](https://prtimes.jp/main/html/rd/p/000000066.000050130.html)）。MNTSQ CLM 获得 ITreview Grid Award“Leader”评级，2026 Summer 为连续第四次（[2026-07-15](https://prtimes.jp/main/html/rd/p/000000106.000050130.html)）。公司获得 HR's SDGsアワード2026「はたらくを楽しく」部门的最優秀賞，并被评为準グランプリ（[2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)）。

### 公司所述的律师事务所关系

- **NO&T。** 公司称自己是“創業当初から長島・大野・常松法律事務所の全面的なサポートを受けて2018年11月に設立”（[2025-10-09](https://prtimes.jp/main/html/rd/p/000000071.000050130.html)）。公司自 2019-02 起在 NO&T 内部非公开试点其 NLP 软件，产品被用于 NO&T 的法务尽职调查工作。2019-10-21，公司宣布与 NO&T 及 PKSHA Technology 建立资本业务合作，其中包括 NO&T 出资 8 亿日元（[2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)）。两名 NO&T 合伙人以外部董事/监事身份加入董事会（[2019-11-13](https://prtimes.jp/main/html/rd/p/000000002.000050130.html)）。NO&T 监修合同范本（“MNTSQ雛型”）以及 MNTSQ AI契約アシスタント 标配的审查规则手册（審査基準集）（[2026-01-16](https://prtimes.jp/main/html/rd/p/000000081.000050130.html)、[AI契約アシスタント 页面](https://mntsq.co.jp/product/aicontract-assistant)）。双方合著出版了《LegalTech》一书（[2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)）。
- **西村朝日（西村あさひ）。** 双方开展包含对 MNTSQ 出资在内的战略合作；该所同时开始使用 MNTSQ CLM（[2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html)）。
- **森·滨田松本（森・濱田松本）。** 包含出资在内的资本业务合作。双方将研究在 MNTSQ 平台上提供森·滨田松本的法务内容并与 MNTSQ 的 AI 结合，也将研究森·滨田松本使用 MNTSQ 技术（[2025-05-07](https://prtimes.jp/main/html/rd/p/000000063.000050130.html)）。
- 公司将上述关系概括为日本四大律师事务所（四大法律事務所）中有三家参与其业务（[2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)）。

### 公司陈述的市场与监管背景

- 2020 年推出 MNTSQ for Enterprise 时，公司提到新冠疫情期间的远程办公。它还提到新的问题：如何在多个电子签约服务之间汇总已电子签署的合同，以及如何符合《电子账簿保存法》（電子帳簿保存法）（[2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)）。
- 在 Series B 新闻稿中，CEO 写道，LLM 的进展，加上“弁護士法に関する社会的検討に一定の目処がついた”，促使公司计划向更多客户直接提供 AI 合同审查（[2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)）。
- 当前的工程职位称合同领域数字化滞后，大企业各自运行自有的本地部署系统。职位还称司法考试考生人数约为十年前的一半（[职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11）。

---

## 产品

### 产品构成与功能领域

官网将产品分为五个模块（[产品索引](https://mntsq.co.jp/product)、[首页](https://mntsq.co.jp/)；访问于 2026-10-11）：

| 模块 | 公司的描述 | 列出的功能 | 页面 |
|---|---|---|---|
| MNTSQ 案件管理（案件管理） | 统一受理法务咨询与合同审查，审查状态可视化，知识自动积累 | 案件搜索与列表、负责人工作量视图、状态管理、申请表单、邮件通知、附件管理、权限控制、参考知识推荐；[2025-06-30](https://prtimes.jp/main/html/rd/p/000000064.000050130.html) 新增“案件フロー”流程控制 | [页面](https://mntsq.co.jp/product/casemanage) |
| MNTSQ 契約管理（合同管理） | AI 自动填写各部门合同台账的管理项目；通知提醒截止日期和续约 | 上传、台账与列表视图、自定义字段、自动填写字段、提醒、关联相关合同、搜索、导出、权限控制 | [页面](https://mntsq.co.jp/product/contractmanage) |
| データベース（数据库） | 自动收集合同相关数据，由专用于合同的 AI 分析和整理 | PDF OCR、条款拆解（条項分解）、元数据管理、范本管理、知识浏览、权限控制 | [页面](https://mntsq.co.jp/product/databasemanage) |
| MNTSQ AI契約アシスタント | 对案件进行风险评级；低风险案件由业务部门自行处理，高风险案件自动生成申请并转交法务 | 合同审查、法务咨询、审查规则手册、自动立案、AI 审查、AI 咨询。标配 NO&T 监修的审查规则手册 | [页面](https://mntsq.co.jp/product/aicontract-assistant) |
| MNTSQ AI Agent | 基于客户合同知识构建、贯穿其他模块的法务专用 AI 智能体 | 审查规则手册、过往案件搜索、对话咨询、展示 AI 的推理过程、初步法律分析。提示词由律师和企业法务从业者编写 | [页面](https://mntsq.co.jp/product/mntsq-ai-agent) |

首页列出的其他功能：

- **以 Word 插件形式提供的 AI 合同审查。** 将对方草稿与客户自有范本比对，并提示相似的过往合同。于 2024-04-01 发布（[2024-02-28](https://prtimes.jp/main/html/rd/p/000000049.000050130.html)）。2026-09-07，MNTSQ AI Agent 被加入 Word 中，可以：
  - 在审查开始前提出审查方针；
  - 以修订模式写入修改和批注；
  - 先参照客户自有的审查规则手册，再回退到律所监修的审查规则手册；
  - 指出条款编号不一致、残留占位符等形式问题（[2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html)）。
- **范本。** “MNTSQ雛型”是 NO&T 监修、附带解说的合同范本。[2026-01-16](https://prtimes.jp/main/html/rd/p/000000081.000050130.html) 范本数量扩充至约两倍，[2026-06-18](https://prtimes.jp/main/html/rd/p/000000101.000050130.html) 新增 13 种，包括 AI 服务使用条款。
- **语言与货币。**
  - 英文界面：[2023-10-02](https://prtimes.jp/main/html/rd/p/000000047.000050130.html)。
  - 合同管理支持 ISO 4217 全部货币：[2025-12-16](https://prtimes.jp/main/html/rd/p/000000078.000050130.html)。
  - 对日语和英语以外语言（如中文、泰语、德语）的合同进行 AI 解析（要素拆解）：[2026-01-21](https://prtimes.jp/main/html/rd/p/000000080.000050130.html)。
- **安全功能。** AWS 上的数据加密存储，SSO 和 IP 地址限制免费提供（[首页](https://mntsq.co.jp/)；访问于 2026-10-11）。

### 集成与 API

- **电子签约。** 自 2021 年起支持导入 DocuSign 和クラウドサイン（CloudSign）上已签署的合同（[CloudSign，2021-04-14](https://prtimes.jp/main/html/rd/p/000000009.000050130.html)）。2026-07-23 扩展为覆盖整个签约流程：从案件生成电子签约草稿、追踪发送记录，以及将签署完成的文件自动登记到台账（[2026-07-23](https://prtimes.jp/main/html/rd/p/000000107.000050130.html)）。
- **聊天工具。** Slack 集成支持评论通知、在消息串中回复并写回案件时间线，以及创建案件（[2026-08-06](https://prtimes.jp/main/html/rd/p/000000110.000050130.html)）。Microsoft Teams 支持通知和回复，包括通过手机应用操作（[2026-09-01](https://prtimes.jp/main/html/rd/p/000000117.000050130.html)）。
- **邮件与存储。**
  - 邮件往来自动导入数据库，附件可全文搜索。
  - 可从 SharePoint、Google Drive 和 Box 导入文件。
  - 通过导入设置文件即可变更用户和权限（[首页](https://mntsq.co.jp/)；访问于 2026-10-11）。
- **公开 API。** 「案件管理公開API」提供文件上传与下载、案件详情获取，以及案件的创建和更新（[2026-04-07](https://prtimes.jp/main/html/rd/p/000000089.000050130.html)）。日期时间字段于 [2026-06-16](https://prtimes.jp/main/html/rd/p/000000100.000050130.html) 统一为带时区的 ISO 8601 格式。未找到公开的 API 参考文档。
- **交易对象主数据。** 可依据国税厅法人主数据创建交易对象记录。名称变更会自动同步，旧名称保留为别名（[2026-05-19](https://prtimes.jp/main/html/rd/p/000000094.000050130.html)）。

### 商业化

收费由初始费用（初始设置及导入支持）和月费（服务使用及支持）组成，根据客户要解决的问题和使用规模报价。未找到公开价目表；导入方案资料需填写表单后下载（[首页](https://mntsq.co.jp/)；访问于 2026-10-11）。每位客户从导入阶段起配备专属顾问，包括协助迁移已有数据；公司还举办用户大会（“MNTSQ Meeting”）。工程职位将业务描述为“受託ゼロ、個社カスタマイズゼロ”（不承接外包开发，不做单一客户定制）（[职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11）。

### 产品沿革

| 日期 | 事件 | 来源 |
|---|---|---|
| 2019-02 | 在 NO&T 内部非公开试点用于法务尽职调查的 NLP 软件；公司称此前经过两年非公开准备 | [2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html) |
| 2020-06-10 | 与小松制作所、福冈银行等就面向企业的产品开展概念验证 | [2020-06-10](https://prtimes.jp/main/html/rd/p/000000003.000050130.html) |
| 2020-12-07 | “MNTSQ for Enterprise”合同数据库正式发布；面向律所的产品名为“MNTSQ for M&A” | [2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html) |
| 2022-01-26 | 宣布 2022 年秋推出案件管理；当时的产品阵容为数据库、合同管理和自动起草（自動ドラフティング） | [2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html) |
| 2022-07-19 | 产品称为“MNTSQ CLM”；新闻稿称自 2020-11 开始正式销售 | [2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html) |
| 2023-06-05 | 成立生成式 AI／LLM 新开发团队 | [2023-06-05](https://prtimes.jp/main/html/rd/p/000000035.000050130.html) |
| 2024-04-01 | 发布 MNTSQ AI契約レビュー | [2024-02-28](https://prtimes.jp/main/html/rd/p/000000049.000050130.html) |
| 2025-10-01 | 发布 MNTSQ AI契約アシスタント，这是首个搭载 MNTSQ AI Agent 的服务。此前与三菱电机进行了约一年的 PoC，并于 2025-04-01 开始接受订单 | [2025-03-19](https://prtimes.jp/main/html/rd/p/000000061.000050130.html)、[2026-03-05](https://prtimes.jp/main/html/rd/p/000000084.000050130.html) |
| 2026-03-05 | AI Agent 加入案件管理：比较相似案件、初步法律分析，以及起草向申请部门询问缺失信息的邮件 | [2026-03-05](https://prtimes.jp/main/html/rd/p/000000084.000050130.html) |
| 2026-09-07 | AI Agent 加入 Word 中的合同审查（第三阶段） | [2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html) |

### 规模变化

| 日期 | 公布的数字 | 来源 |
|---|---|---|
| 2020-12-07 | 小松制作所在新闻稿中的评论：为期五个月的 PoC 显示，约 40% 的合同审查工作可以提高效率 | [2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html) |
| 2022-07-19 | 成员：50 人（创立时 4 人） | [2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html) |
| 2023-09-19 | 被“売上高1兆円以上の国内企業の約5社に1社”使用（MNTSQ 自行调查） | [2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html) |
| 2025-10-08 | 伊藤忠商事采用后，日经 2024 年「法務力が高い企業」排名前 5 全部、前 10 中 7 家、前 20 中 14 家为用户 | [2025-10-08](https://prtimes.jp/main/html/rd/p/000000069.000050130.html) |
| 2025-12-24 | 日经 2025 年排名前 10 中 9 家为用户，上一年为 6 家 | [2025-12-24](https://prtimes.jp/main/html/rd/p/000000079.000050130.html) |
| 2026-05-12 | 日本营收前 100 强企业中的 41 家 | [2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html) |
| 2026-06-29 | 前 100 强中的 42 家（日经，截至 2026-06-12） | [2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html) |
| 2026-07-07 | 采用企业 2,000 家以上（含集团子公司），以及国内销售额最大的 10 家上市公司中的 8 家（均截至 2026-05） | [2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html) |

### 已公布的客户与合作方

| 日期 | 对象 | 公布内容 |
|---|---|---|
| [2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html) | 小松製作所、大阪ガス | MNTSQ for Enterprise 的首批客户 |
| [2021-06-30](https://prtimes.jp/main/html/rd/p/000000012.000050130.html) | 三菱商事 | 合同数据库与法务部现有的案件及文档管理系统对接 |
| [2021-09-30](https://prtimes.jp/main/html/rd/p/000000013.000050130.html) | Zuva（Kira Systems 的分拆公司） | 与 Zuva 的 DocAI 平台集成，用于日英合同解析 |
| [2021-11-01](https://prtimes.jp/main/html/rd/p/000000014.000050130.html) | 三井住友銀行 | 自动起草功能针对银团贷款合同进行配置；新闻稿称合作源于 MNTSQ 向 NO&T 提供的服务 |
| [2022-01-26](https://prtimes.jp/main/html/rd/p/000000018.000050130.html) | 三菱電機 | 采用全部服务阵容，包括自动起草 |
| [2023-08-09](https://prtimes.jp/main/html/rd/p/000000040.000050130.html) | 日立製作所 | 采用 MNTSQ CLM 进行合同知识管理 |
| [2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html) | 三菱UFJ銀行 | 在其集团企业风投的投资方评论中被称为 MNTSQ CLM 现有用户 |
| [2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html) | 西村あさひ | 该律所成为用户兼投资方 |
| [2025-10-08](https://prtimes.jp/main/html/rd/p/000000069.000050130.html) | 伊藤忠商事 | 采用 MNTSQ CLM |
| [2026-06-04](https://prtimes.jp/main/html/rd/p/000000098.000050130.html) | 東京エレクトロン | 替换了其运行约 20 年的自研合同管理系统 |

[客户页面](https://mntsq.co.jp/clients)和[案例索引](https://mntsq.co.jp/case)列出了更多用户（访问于 2026-10-11）。已公布的用户还包括律师事务所稲葉総合法律事務所（[2021-12-22](https://prtimes.jp/main/html/rd/p/000000015.000050130.html)）。

### 公开计划

- Series B 资金用途：加快包括 LLM 应用在内的产品开发投入，并提供 AI 合同审查（[2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)）。
- 2024 年融资：将在资本业务合作框架内研究与投资方企业共同开发解决方案（[2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)）。
- 公司对 MNTSQ AI Agent 的愿景：一个能自主行动、“契約交渉まで行ってくれる”（直至代为进行合同谈判）的智能体（[2025-09-19 官网新闻稿](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025)、[2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html)）。
- 任命 COO 时的表述：扩大在日本大企业领域的导入和份额，并将该领域描述为未来合同网络和平台的枢纽（[2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html)）。
- 一则现行人事职位将招聘背景写为“IPO準備に向けた体制強化”，并称公司正在推进面向 IPO 的体制建设（[制度企画・労務 职位](https://hrmos.co/pages/mntsq/jobs/30017)，页面元数据 datePosted 2026-09-07；访问于 2026-10-11）。

---

## 创始人

**板谷 隆平（Ryuhei Itaya）**——Founder / CEO，代表取締役。公司概要页面仍将他列为 NO&T 的律师（[公司概要](https://mntsq.co.jp/about)）。工程职位称他同时兼任 CPO（[职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11）。

- 2013 年：毕业于东京大学法学部，在学期间通过司法考试预备考试（司法試験予備試験）（[专栏，2025-03-03](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)）。
- 2014 年：登记为律师并加入 NO&T，从事并购（M&A）及 AI/IT 等技术相关法律咨询。在该所工作期间创立 MNTSQ（[公司概要](https://mntsq.co.jp/about)）。
- 一般社団法人AIリーガルテック協会理事（理事），见 [2025-07-09](https://prtimes.jp/main/html/rd/p/000000065.000050130.html) 新闻稿。
- 2025-12：在日经律师排名“人工知能（AI）ガバナンス”类别中位列第 10（[2025-12-24](https://prtimes.jp/main/html/rd/p/000000079.000050130.html)）。
- 2026-05：在英国《金融时报》“Asia-Pacific Innovative Lawyers Awards 2026”中获得“Legal Intrapreneur”奖（[2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)）。

**安野 贵博（安野 貴博，Takahiro Anno）**——公司专栏称板谷与安野共同创立了 MNTSQ。专栏将安野描述为自然语言处理专家，他用板谷编写的约 100 条不公平条款样本训练了最初的模型（[专栏，2025-03-03](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)）。2019 年堅山在 Wantedly 上发表的公司文章称安野也是 MNTSQ 的董事（取締役）（[Wantedly，2019-10-29](https://www.wantedly.com/companies/mntsq/post_articles/192635)）。当前[公司概要页面](https://mntsq.co.jp/about)的管理层部分未列出他。

**堅山 耀太郎（Yotaro Katayama）**——[公司概要页面](https://mntsq.co.jp/about)将他列为“Co-Founder / 取締役”及 Preferred Networks CFO。Preferred Networks 的个人简介给出以下经历（[PFN 管理层，日文](https://www.preferred.jp/ja/company/leadership)；访问于 2026-10-11）：

- 2016 年：东京大学大学院工学系研究科硕士毕业，之后任职于高盛证券日本。
- BEDORE（现 PKSHA Workplace）共同创始人兼董事。
- 2018 年：作为共同创始人加入 MNTSQ 董事会，负责工程和财务。
- 2023 年：在 MNTSQ 任职期间获得东京大学工学博士学位。
- 2024-05：任 Preferred Networks CFO。

### 主要管理层

| 姓名 | 职务（原文） | 公开背景 | 来源 |
|---|---|---|---|
| 深井 亮（Ryo Fukai） | COO，自 2026-06-01 起 | 共立；2019 年起任职于 Sansan，2020 年作为首位销售加入“Bill One”的创立，后负责销售及产品企划（PMM） | [2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html) |
| 高田 直満 | VP of Engineering | — | [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)（2026-09-01 更新） |
| 粟谷 翔 | 社外取締役（外部董事） | NO&T 合伙人 | [公司概要](https://mntsq.co.jp/about) |
| 藤原 総一郎 | 監査役（监事） | NO&T 执行合伙人（自 2024 年起）；2019–2024 年任 MNTSQ 外部董事，2024 年起任监事 | [公司概要](https://mntsq.co.jp/about)、[专栏](https://mntsq.co.jp/column/interview/noandt_and_mntsq/) |
| 内海 慶 | 算法工程师，自 2026-05 起 | 曾在雅虎日本、电装 IT 实验室（デンソーアイティーラボラトリ）和 SB Intuitions 从事 NLP 研究；获 NLP2025 优秀奖（優秀賞） | [2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html) |

公司组织图显示 CEO 之下设四个部门：事業本部、開発本部、人事本部和経営管理部。開発本部包括三部分（[Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)）：

- 開発部：CLM 应用、CLM 平台、法务智能体、面向业务部门及 enabling 等团队。
- プラットフォーム部：SRE 团队、QA 团队和安全推进室。
- リーガルエキスパートチーム：法务新业务企划和法务顾问。

---

## 融资

| 日期 | 轮次（公司原文） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2019-10-21 之前（日期未披露） | 資本技術提携（资本技术合作） | 未披露 | PKSHA Technology | — | [2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html) |
| 2019-10-21 | 資本業務提携（资本业务合作） | NO&T 出资 8 亿日元（8億円） | 長島・大野・常松法律事務所 | — | [2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html) |
| 2023-09-19 | シリーズB | 10 亿日元（10億円） | ALL STAR SAAS FUND（新投资方） | 未说明 | [2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html) |
| 2024-06-03 | 无轮次名称；第三方定向增资、发行债券和贷款 | 合计约 10 亿日元（総額約10億円） | 股权：かんぽNEXTパートナーズ、三菱UFJイノベーション・パートナーズ、日揮みらい投資事業有限責任組合。债券：あおぞらHYBRID3号投資事業有限責任組合（由あおぞら企業投資管理）。贷款：商工組合中央金庫 | 未说明 | [2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html) |
| 2024-06-04 | 出資を含む戦略的協業 | 未披露 | 西村あさひ法律事務所・外国法共同事業 | 未说明 | [2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html) |
| 2025-05-07 | 資本業務提携（含出资） | 未披露 | 森・濱田松本法律事務所外国法共同事業 | 未说明 | [2025-05-07](https://prtimes.jp/main/html/rd/p/000000063.000050130.html) |

- 2019 年新闻稿称，PKSHA 的出资在 NO&T 本轮之前已经完成，未说明金额（[2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)）。后续新闻稿将该次合作描述为募集“約8億円”（[2019-11-13](https://prtimes.jp/main/html/rd/p/000000002.000050130.html)）。
- 在 Series B 新闻稿中，CEO 表示，为了持续进行增长投资，公司决定在本轮接受新的 VC 出资（“新規のVCによる出資を受け入れることといたしました”）（[2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)）。未找到标注为シリーズA的新闻稿。
- 2024 年新闻稿称，本轮融资是因为当年 4 月推出的 MNTSQ AI契約レビュー 需求旺盛。三菱 UFJ 和日挥旗下投资机构的投资方评论称，三菱UFJ銀行和日挥集团已是 MNTSQ CLM 用户（[2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)）。BRIDGE 仅称该轮为“直近のラウンド”（[BRIDGE，2024-06-04](https://thebridge.jp/2024/06/mntsq-jpy1b-round-funding)）。
- Series B 新闻稿与 MNTSQ AI契約レビュー 正在开发的公告于同一天发布（[2023-09-19](https://prtimes.jp/main/html/rd/p/000000046.000050130.html)）。

---

## 工程

### 技术栈与平台

**经公司技术文章确认**（技术博客和新闻稿）：

- **Ruby / Ruby on Rails。** 公司称，自 2018 年创立以来，Ruby 一直是其 Web 服务的主要开发语言（[2023-03-06](https://prtimes.jp/main/html/rd/p/000000031.000050130.html)）。2026 年的一篇文章称服务的核心部分采用 Ruby on Rails（[技术博客，2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614)）。公司曾是 RubyKaigi 2023 的 Ruby Sponsor。
- **异步任务。** Rails 后台任务从基于 Redis 的 Resque 迁移至 Amazon SQS，按优先级分层并按功能拆分队列，每个队列单独自动扩缩容（[2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614)）。Python worker 在 SQS 上使用 Celery（[2026-06-29](https://tech.mntsq.co.jp/entry/2026/06/29/090000)）。
- **搜索。** 服务原先在 EC2 上自建运行 Elasticsearch 7.x，之后无停机迁移到 Amazon OpenSearch Service，迁移从 2025-10 持续到 2026-06。该项目将按租户组划分的多个集群合并为 VPC 内的单一域，启用细粒度访问控制，并用 Terraform 管理（[2026-08-26](https://tech.mntsq.co.jp/entry/2026/08/26/180213)）。
- **AWS 与 Google Cloud。** 应用运行在 Amazon ECS 上。三个后端服务调用 Google Cloud 的 Vertex AI 或 Cloud Vision API，现已改用 Workload Identity Federation 认证，不再使用服务账号密钥。部署通过 GitHub Actions 进行（[2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103)）。
- **LLM。** 2024 年的一次分享比较了 GPT-4o、Claude 3.5 Sonnet 和 Gemini 1.5 Pro 在合同解析上的表现，比较了准确度、上下文窗口、输出速度、价格以及能否在日本区域使用（演讲者的主观评价）（[LT 资料，2024-07-11](https://speakerdeck.com/mntsq/ltzi-liao-mntsqnoqi-yue-shu-jie-xi-wo-llmnizhi-kihuan-eruhua)）。
- **其他工具。** 其他技术博客文章涉及 Datadog、Redash、AWS Security Hub、Playwright 和 ECS Exec（[文章列表](https://tech.mntsq.co.jp/archive)；访问于 2026-10-11）。

**当前职位中列出**（招聘文件；[软件工程师（后端）](https://hrmos.co/pages/mntsq/jobs/10055)、[技术负责人](https://hrmos.co/pages/mntsq/jobs/10034)，[Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) 中列表相同）：

| 类别 | 内容 |
|---|---|
| 语言 | Ruby、Python、JavaScript、TypeScript |
| Web 框架 | Ruby on Rails、FastAPI、Vue.js |
| CSS / UI | Element Plus、Tailwind CSS、PostCSS、Storybook |
| 平台 | Amazon Web Services、Google Cloud |
| 数据库 | Aurora MySQL |
| 搜索 | Elasticsearch、OpenSearch |
| 监控 | CloudWatch、Datadog |
| 容器 | Docker、Docker Compose、ECS/Fargate |
| 配置管理 | Terraform、Itamae |
| AI 工程师职位 | Python、TypeScript、FastAPI、MCP、PyTorch、MySQL、OpenSearch、GitHub、Docker（[AI（NLP）工程师](https://hrmos.co/pages/mntsq/jobs/10064)） |

职位称开发以使用 Claude、Devin 等 AI 工具为前提。员工可获得 Claude Enterprise 账号，列为福利之一（[职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11）。

### 系统

| 系统 | 功能 | 来源 |
|---|---|---|
| 合同解析 | 合同专用 OCR、条款级拆解，并用机器学习提取交易对方、签署日、期限、金额等字段。后端“解析基盤”服务负责条款拆解和 OCR。2026 年新增多语言解析 | [2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html)、[技术博客 2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103)、[2026-01-21](https://prtimes.jp/main/html/rd/p/000000080.000050130.html) |
| AI 智能体后端 | 为 MNTSQ AI Agent 回答合同相关问题、判定风险和检索知识的两个服务 | [2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103) |
| 离线评估 | 使用 LLM-as-a-Judge 对 AI 输出质量做内部评估 | [2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103) |
| 知识图谱检索（原型） | 用于合同审查：将合同条文、案件评论和审查规则手册条目切分成块，抽取实体与关系，同时用关键词层面和情境层面的查询检索，生成有依据的回答 | [2026-09-09](https://tech.mntsq.co.jp/entry/2026/09/09/083234) |
| 多租户搜索 | 单一 OpenSearch 域存放所有租户的索引，包括文档索引和条款索引，超大租户使用更多分片 | [2026-08-26](https://tech.mntsq.co.jp/entry/2026/08/26/180213) |
| 任务队列 | 基于 SQS、按优先级和功能拆分的队列，带自动扩缩容和 Datadog 监控 | [2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614) |
| 集成 | 电子签约（DocuSign、CloudSign）、邮件导入、SharePoint、Google Drive 和 Box、Slack、Teams、案件管理公开 API、国税厅法人主数据 | 见“集成与 API” |

公司在 Hatena Blog 上运营日文技术博客。其站点地图列出 2020-11 至 2026-09 的 108 篇文章，其中 24 篇发布于 2026 年（[tech.mntsq.co.jp](https://tech.mntsq.co.jp/)；访问于 2026-10-11）。公司还在 [note](https://note.mntsq.co.jp/) 上发文，并在 [connpass](https://mntsq.connpass.com/) 上举办活动。

### 招聘所需技术背景

来自 HRMOS 上的当前职位（访问于 2026-10-11）：

- **软件工程师（后端）。**
  - 必须：3 年以上 Web 应用开发与运维经验；主动解决技术问题的经验；作为后端工程师进行 API 设计和数据库设计的经验。
  - 优先：Ruby on Rails、Vue.js 或 Python；主导 BtoB 系统从设计到实现；基于可用性、安全性和容错性进行云基础设施设计与配置管理（[职位](https://hrmos.co/pages/mntsq/jobs/10055)）。
- **技术负责人（テックリード）。**
  - 必须：5 年以上 Web 应用设计、开发与运维经验；技术选型和架构设计经验；作为技术负责人主导高难度项目；BtoB 系统设计经验。
  - 优先：使用机器学习、NLP 或搜索系统的产品开发经验；基于 Elasticsearch 或 Apache Solr 的搜索系统开发；面向高度专业化实务领域的系统建设（[职位](https://hrmos.co/pages/mntsq/jobs/10034)）。
- **AI（NLP）工程师。**
  - 必须：系统的 ML/NLP 知识；3 年以上将 ML/NLP 引入产品、设计评估指标并持续改进性能的经验；使用主要 LLM API（OpenAI、Claude、Gemini）的经验；Web 应用或 API 开发经验。
  - 优先：使用 MCP 或 A2A 开发 AI 智能体；基于 Elasticsearch 或 OpenSearch 的搜索系统；数据平台建设；LLM 微调或预训练；在 AI/NLP 学术会议上演讲或投稿（[职位](https://hrmos.co/pages/mntsq/jobs/10064)）。
- **主导工程师（前端）。**
  - 必须：5 年以上 Vue.js 或 React 经验。
  - 优先：设计系统的构建和运营经验（[职位](https://hrmos.co/pages/mntsq/jobs/10037)）。
- **设计工程师。**
  - 必须：设计系统的构建、运营和改进经验（[职位](https://hrmos.co/pages/mntsq/jobs/10038)）。
- **选拔。** 后端的技术考核是以使用 AI 为前提的数据库模式设计题。终面为线下面试，流程包括背景调查和推荐人核实（[职位](https://hrmos.co/pages/mntsq/jobs/10055)）。

### 行业领域

工作涉及日本企业法务实务：

- 业务部门与法务部门之间的合同起草、审查和谈判；
- 合同台账、续约及期限管理；
- 以范本和审查规则手册形式呈现的律所最佳实践；
- 电子签约与《电子账簿保存法》（電子帳簿保存法）；
- 修订后的分包相关法律（取適法），公司已为其增加范本（[2026-06-18](https://prtimes.jp/main/html/rd/p/000000101.000050130.html)）。

开发本部设有法务专家团队，由律师和曾任企业法务的人员组成，参与产品企划（[Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)）。CEO 的招聘寄语称“契約に詳しい必要はありません”（不需要熟悉合同）（[招聘网站](https://careers.mntsq.co.jp/)；访问于 2026-10-11）。工程职位要求的是对公司业务领域感兴趣并愿意学习，而非已有法务经验（[职位](https://hrmos.co/pages/mntsq/jobs/10055)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 未说明。职位、招聘网站和资料均为日文；未发现英语要求或英文职位 | [HRMOS 职位列表](https://hrmos.co/pages/mntsq/jobs)；访问于 2026-10-11 |
| 地点 | 东京晴海 Triton Square 办公楼 X 栋 4 层；工作地点的变更范围由公司决定 | [职位](https://hrmos.co/pages/mntsq/jobs/10055) |
| 到岗政策 | 混合办公；每月至少到岗 5 天，其余时间仅可在家远程；不可完全远程。每月第三个周二全员到岗召开月度分享会 | [职位](https://hrmos.co/pages/mntsq/jobs/10055)、[招聘 FAQ](https://careers.mntsq.co.jp/) |
| 工作时间 | 无核心时间的完全弹性工作制；标准工时 8 小时。工程师设置不安排会议的日子和时段 | [职位](https://hrmos.co/pages/mntsq/jobs/10055) |
| 薪资（年薪，按职位） | 技术负责人 1,100 万–1,500 万日元；主导工程师（后端/前端）900 万–1,300 万日元；AI（NLP）工程师 800 万–1,500 万日元；软件工程师（后端/前端）和设计工程师 650 万–1,200 万日元。年薪分 12 个月发放，含 45 小时视同加班费，超出部分另付；每年评估两次 | [技术负责人](https://hrmos.co/pages/mntsq/jobs/10034)、[主导后端](https://hrmos.co/pages/mntsq/jobs/10036)、[主导前端](https://hrmos.co/pages/mntsq/jobs/10037)、[AI](https://hrmos.co/pages/mntsq/jobs/10064)、[后端](https://hrmos.co/pages/mntsq/jobs/10055)、[前端](https://hrmos.co/pages/mntsq/jobs/10056)、[设计](https://hrmos.co/pages/mntsq/jobs/10038)；访问于 2026-10-11 |
| 薪资等级 | 资料显示七个等级的薪资区间，坐标轴标注 400–1,800，未注明单位。1 级起点约为 500，7 级无上限 | [Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) |
| 股权 | 薪资之外另有股票期权制度 | [职位](https://hrmos.co/pages/mntsq/jobs/10055) |
| 休假与试用期 | 每周双休加法定节假日；入职即有 13 天带薪年假，此后每年 14–23 天；试用期 3 个月 | [职位](https://hrmos.co/pages/mntsq/jobs/10055) |
| 福利 | 通勤补贴每月最高 5 万日元、办公室健身房免费使用、保姆服务折扣券、流感疫苗接种补贴、Claude Enterprise 账号、関東ITソフトウェア健康保険組合 | [职位](https://hrmos.co/pages/mntsq/jobs/10055) |
| 副业 | 经事先批准后允许 | [职位](https://hrmos.co/pages/mntsq/jobs/10055)、[招聘 FAQ](https://careers.mntsq.co.jp/) |
| 入职培训 | 为期三个月的项目，配备导师 | [职位](https://hrmos.co/pages/mntsq/jobs/10055) |
| 签证担保、应届生 | 所查阅的工程职位均未提及 | [HRMOS 职位列表](https://hrmos.co/pages/mntsq/jobs)；访问于 2026-10-11 |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-10-11）：

- 官网及其站点地图：公司概要、产品、客户、案例、新闻索引和信息安全方针；
- 招聘网站及 HRMOS 职位列表上的全部现行职位（23 个），以及 HERP Career 聚合页面；
- MNTSQ 的 PR TIMES 企业页面（列出 104 篇新闻稿）；
- 技术博客站点地图、note、Speaker Deck（10 份资料）和 connpass；
- GitHub 组织 API、国税厅法人番号公表网站、BRIDGE 以及 PFN 管理层页面；
- 以 MNTSQ、モンテスキュー、ＭＮＴＳＱ株式会社 与融资、ARR、決算公告、J-Startup 组合进行的日文和英文网络搜索。

TokyoDev 对自动访问返回 HTTP 403；Japan Dev 没有 MNTSQ 的公司页面（HTTP 404）。

- **营收、ARR、盈利情况和估值。** 未公布。网络搜索中未找到決算公告；未检索官报本身。
- **累计融资。** 公司未公布总额。PKSHA、西村朝日和森·滨田松本的出资金额未披露，且未找到标注为シリーズA的新闻稿。
- **工程团队工作语言与签证政策。** 所查阅的职位和招聘页面均未说明。
- **价目表。** 仅公开了收费结构；导入方案资料需填写表单获取。
- **公开 API 文档。** 新闻稿介绍了案件管理 API，但未找到公开的参考文档。
- **开源。** GitHub 组织 [`MNTSQ`](https://github.com/MNTSQ) 创建于 2018-11-21。其元数据中地点为“Japan”，没有网站、邮箱或 X 账号，所查阅的公司网站也均未链接到它。它有四个公开仓库：三个 Ruby/Rails 工具的 fork（`apivore`、`ruby-ntlm`、`annotate_models`），以及一个 Python 仓库 `simple-mcp-rag`，最后推送于 2025-10-21。
- **状态页或 SLA。** 未找到。
- **离职率。** 未公布。

### 不同来源之间的不一致

- **创立年份。** 公司新闻稿给出設立日 2018-11-14，国税厅登记显示法人番号指定日为 2018-11-27（[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433)）。公司自己与 NO&T 的专栏则称“2019年にMNTSQを創業しました”（[专栏，2025-03-03](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)）。
- **前 100 强客户数。** 后端职位写的是“2026年4月現在”前 100 强中 43 家（[职位](https://hrmos.co/pages/mntsq/jobs/10055)；访问于 2026-10-11）。此后发布的新闻稿写的是 41 家（[2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html)、[2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)、[2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html)），再之后为截至 2026-06-12 的 42 家（[2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)）。
- **堅山的董事职务。** MNTSQ 公司概要页面将他列为“Co-Founder / 取締役”（[公司概要](https://mntsq.co.jp/about)）。Preferred Networks 的个人简介则称他“MNTSQの社外取締役も務める”（同时担任 MNTSQ 外部董事）（[PFN 管理层](https://www.preferred.jp/ja/company/leadership)）。
- **开发团队结构。** 职位称截至 2026-08，開発本部约 50 人，分为四个团队（CLM、法務エージェント、事業部向け、イネーブリング）（[职位](https://hrmos.co/pages/mntsq/jobs/10034)）。2026-09 的资料将 CLM 拆分为应用和平台两个团队，并另设プラットフォーム部和法务专家团队（[Engineering Team Deck](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao)）。来源未说明这 50 人是否包括平台团队和法务专家团队。
- **新闻稿日期。** mntsq.co.jp 新闻页面上标注为“更新”的日期有时与 PR TIMES 相差一天，例如 2019-10-20 与 2019-10-21、2023-09-18 与 2023-09-19。本文采用 PR TIMES 的日期。

### 其他

- 公司的产品名称几经变化：
  - **2020 年：**“MNTSQ for M&A”（律所尽职调查）和“MNTSQ for Enterprise”（[2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)）。
  - **2022-01：**产品阵容统称“MNTSQ”（[2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html)）。
  - **2022-07 起：**“MNTSQ CLM”（[2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html)）。
  - **2026 年的新闻稿**分别称其为契約プラットフォーム和契約AIインフラ（[2026-08-06](https://prtimes.jp/main/html/rd/p/000000110.000050130.html)、[2026-09-01](https://prtimes.jp/main/html/rd/p/000000117.000050130.html)）。
- 公司首次大规模媒体宣传于 2026 年 6 月至 7 月进行：YouTube 广告、出租车内屏广告，以及东京站和大手町站的户外广告（[2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html)）。
- 在 2026-01-16 至 2026-09-18 期间的 32 篇 PR TIMES 新闻稿中，17 篇是产品功能或范本更新。其余为奖项（5 篇）、案例（4 篇）、活动（3 篇）、人事任命与加入（2 篇）和广告宣传（1 篇）（[PR TIMES 企业页面](https://prtimes.jp/main/html/searchrlp/company_id/50130)；访问于 2026-10-11）。

---

## 资料来源

**官方**

- [公司官网（日文）](https://mntsq.co.jp/) · [公司概要](https://mntsq.co.jp/about) · [客户](https://mntsq.co.jp/clients) · [案例](https://mntsq.co.jp/case) · [新闻索引](https://mntsq.co.jp/news)
- 产品页面：[索引](https://mntsq.co.jp/product) · [案件管理](https://mntsq.co.jp/product/casemanage) · [契約管理](https://mntsq.co.jp/product/contractmanage) · [データベース](https://mntsq.co.jp/product/databasemanage) · [AI契約アシスタント](https://mntsq.co.jp/product/aicontract-assistant) · [AI Agent](https://mntsq.co.jp/product/mntsq-ai-agent)
- [ISMS 认证公告，2024-03-22（日文）](https://mntsq.co.jp/news/information/202403-isms) · [NEXTユニコーン調査2024 公告，2025-01-17（日文）](https://mntsq.co.jp/news/information/nextunicorn2024)
- [专栏：NO&T 与 MNTSQ 的创业故事，2025-03-03（日文）](https://mntsq.co.jp/column/interview/noandt_and_mntsq/)
- [官网上的 MNTSQ AI Agent 新闻稿，2025-09-19（日文）](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025)
- [招聘网站（日文）](https://careers.mntsq.co.jp/) · [工程招聘页面（日文）](https://careers.mntsq.co.jp/mntsq-for-engineers)
- [HRMOS 职位列表（日文）](https://hrmos.co/pages/mntsq/jobs)：[技术负责人](https://hrmos.co/pages/mntsq/jobs/10034) · [主导工程师（后端）](https://hrmos.co/pages/mntsq/jobs/10036) · [主导工程师（前端）](https://hrmos.co/pages/mntsq/jobs/10037) · [设计工程师](https://hrmos.co/pages/mntsq/jobs/10038) · [软件工程师（后端）](https://hrmos.co/pages/mntsq/jobs/10055) · [软件工程师（前端）](https://hrmos.co/pages/mntsq/jobs/10056) · [AI（NLP）工程师](https://hrmos.co/pages/mntsq/jobs/10064) · [制度企画・労務](https://hrmos.co/pages/mntsq/jobs/30017)
- [技术博客（日文）](https://tech.mntsq.co.jp/) · [文章列表](https://tech.mntsq.co.jp/archive)——[GCP Workload Identity Federation，2026-09-29](https://tech.mntsq.co.jp/entry/2026/09/29/184103) · [法务工作所需的搜索，2026-09-09](https://tech.mntsq.co.jp/entry/2026/09/09/083234) · [Elasticsearch 迁移至 OpenSearch，2026-08-26](https://tech.mntsq.co.jp/entry/2026/08/26/180213) · [Celery + SQS，2026-06-29](https://tech.mntsq.co.jp/entry/2026/06/29/090000) · [Redis 迁移至 SQS，2026-05-11](https://tech.mntsq.co.jp/entry/2026/05/11/085614)
- [note（日文）](https://note.mntsq.co.jp/) · [connpass](https://mntsq.connpass.com/)
- [Speaker Deck](https://speakerdeck.com/mntsq)——[Engineering Team Deck，2026-09-01 更新（日文）](https://speakerdeck.com/mntsq/mntsq-enziniaxiang-kehui-she-shao-jie-zi-liao) · [LT：用 LLM 替换合同解析，2024-07-11（日文）](https://speakerdeck.com/mntsq/ltzi-liao-mntsqnoqi-yue-shu-jie-xi-wo-llmnizhi-kihuan-eruhua)
- [堅山在 Wantedly 上的文章，2019-10-29（日文）](https://www.wantedly.com/companies/mntsq/post_articles/192635)
- [GitHub 组织 MNTSQ](https://github.com/MNTSQ)

**新闻稿（PR TIMES，日文——按时间倒序）** · [企业页面](https://prtimes.jp/main/html/searchrlp/company_id/50130)

- [AI Agent 第三阶段：Word 中的合同审查——2026-09-07](https://prtimes.jp/main/html/rd/p/000000118.000050130.html)
- [Microsoft Teams 集成——2026-09-01](https://prtimes.jp/main/html/rd/p/000000117.000050130.html)
- [Slack 集成——2026-08-06](https://prtimes.jp/main/html/rd/p/000000110.000050130.html)
- [扩展电子签约集成——2026-07-23](https://prtimes.jp/main/html/rd/p/000000107.000050130.html)
- [ITreview Grid Award 2026 Summer——2026-07-15](https://prtimes.jp/main/html/rd/p/000000106.000050130.html)
- [采用企业 2,000 家；首次媒体宣传——2026-07-07](https://prtimes.jp/main/html/rd/p/000000105.000050130.html)
- [HR's SDGsアワード2026——2026-06-29](https://prtimes.jp/main/html/rd/p/000000104.000050130.html)
- [范本：新增 13 种，含 AI 服务条款——2026-06-18](https://prtimes.jp/main/html/rd/p/000000101.000050130.html)
- [公开 API：ISO 8601 日期格式——2026-06-16](https://prtimes.jp/main/html/rd/p/000000100.000050130.html)
- [东京电子案例——2026-06-04](https://prtimes.jp/main/html/rd/p/000000098.000050130.html)
- [任命 COO（深井 亮）——2026-06-01](https://prtimes.jp/main/html/rd/p/000000097.000050130.html)
- [CEO 获 FT Legal Intrapreneur 奖——2026-05-22](https://prtimes.jp/main/html/rd/p/000000096.000050130.html)
- [基于国税厅主数据的交易对象管理——2026-05-19](https://prtimes.jp/main/html/rd/p/000000094.000050130.html)
- [算法工程师内海 慶加入——2026-05-12](https://prtimes.jp/main/html/rd/p/000000093.000050130.html)
- [案件管理公开 API——2026-04-07](https://prtimes.jp/main/html/rd/p/000000089.000050130.html)
- [案件管理搭载 AI Agent——2026-03-05](https://prtimes.jp/main/html/rd/p/000000084.000050130.html)
- [多语言合同解析——2026-01-21](https://prtimes.jp/main/html/rd/p/000000080.000050130.html)
- [范本阵容扩充至两倍——2026-01-16](https://prtimes.jp/main/html/rd/p/000000081.000050130.html)
- [日经 2025 排名：前 10 中 9 家——2025-12-24](https://prtimes.jp/main/html/rd/p/000000079.000050130.html)
- [ISO 4217 货币——2025-12-16](https://prtimes.jp/main/html/rd/p/000000078.000050130.html)
- [迁至晴海 Triton Square——2025-10-09](https://prtimes.jp/main/html/rd/p/000000071.000050130.html)
- [伊藤忠商事采用 MNTSQ CLM——2025-10-08](https://prtimes.jp/main/html/rd/p/000000069.000050130.html)
- [简保生命–Aflac–日本邮政加速器——2025-08-15](https://prtimes.jp/main/html/rd/p/000000066.000050130.html)
- [AIリーガルテック協会研讨会——2025-07-09](https://prtimes.jp/main/html/rd/p/000000065.000050130.html)
- [案件フロー 功能——2025-06-30](https://prtimes.jp/main/html/rd/p/000000064.000050130.html)
- [森·滨田松本资本业务合作——2025-05-07](https://prtimes.jp/main/html/rd/p/000000063.000050130.html)
- [AI契約アシスタント 开始接受订单——2025-03-19](https://prtimes.jp/main/html/rd/p/000000061.000050130.html)
- [西村朝日战略合作——2024-06-04](https://prtimes.jp/main/html/rd/p/000000051.000050130.html)
- [通过三家企业风投、债券和贷款募集 10 亿日元——2024-06-03](https://prtimes.jp/main/html/rd/p/000000050.000050130.html)
- [AI契約レビュー 发布——2024-02-28](https://prtimes.jp/main/html/rd/p/000000049.000050130.html)
- [英文界面——2023-10-02](https://prtimes.jp/main/html/rd/p/000000047.000050130.html)
- [Series B，10 亿日元——2023-09-19](https://prtimes.jp/main/html/rd/p/000000045.000050130.html)
- [宣布开发 MNTSQ AI契約レビュー——2023-09-19](https://prtimes.jp/main/html/rd/p/000000046.000050130.html)
- [日立制作所采用 MNTSQ CLM——2023-08-09](https://prtimes.jp/main/html/rd/p/000000040.000050130.html)
- [生成式 AI／LLM 开发团队——2023-06-05](https://prtimes.jp/main/html/rd/p/000000035.000050130.html)
- [RubyKaigi 2023 Ruby Sponsor——2023-03-06](https://prtimes.jp/main/html/rd/p/000000031.000050130.html)
- [办公室迁移；成员 50 人——2022-07-19](https://prtimes.jp/main/html/rd/p/000000021.000050130.html)
- [三菱电机采用全部服务——2022-01-26](https://prtimes.jp/main/html/rd/p/000000018.000050130.html)
- [宣布案件管理——2022-01-26](https://prtimes.jp/main/html/rd/p/000000017.000050130.html)
- [稲葉総合法律事務所采用 MNTSQ——2021-12-22](https://prtimes.jp/main/html/rd/p/000000015.000050130.html)
- [三井住友银行银团贷款合同起草——2021-11-01](https://prtimes.jp/main/html/rd/p/000000014.000050130.html)
- [Zuva DocAI 集成——2021-09-30](https://prtimes.jp/main/html/rd/p/000000013.000050130.html)
- [三菱商事——2021-06-30](https://prtimes.jp/main/html/rd/p/000000012.000050130.html)
- [CloudSign 集成——2021-04-14](https://prtimes.jp/main/html/rd/p/000000009.000050130.html)
- [MNTSQ for Enterprise 发布——2020-12-07](https://prtimes.jp/main/html/rd/p/000000004.000050130.html)
- [与小松制作所、福冈银行开展 PoC——2020-06-10](https://prtimes.jp/main/html/rd/p/000000003.000050130.html)
- [NO&T 合伙人加入董事会——2019-11-13](https://prtimes.jp/main/html/rd/p/000000002.000050130.html)
- [与 NO&T 及 PKSHA 资本业务合作，8 亿日元——2019-10-21](https://prtimes.jp/main/html/rd/p/000000001.000050130.html)

**第三方报道与资料**

- [国税厅法人番号公表网站——7010001196433（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001196433)
- [Preferred Networks 管理层——堅山 耀太郎简介（日文）](https://www.preferred.jp/ja/company/leadership)
- [BRIDGE——2024 年融资，2024-06-04（日文）](https://thebridge.jp/2024/06/mntsq-jpy1b-round-funding)
