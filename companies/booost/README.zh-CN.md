# Booost

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Booost（Booost株式会社 / Booost, Inc.；法人番号 7010001167327）是一家总部位于东京、成立于 2015-04-15 的公司。公司销售 **booost Sustainability**，并称之为“サステナビリティERP”（可持续发展 ERP）：一个用于在企业集团和供应链范围内收集、审批、计算和披露 ESG 与温室气体数据的 SaaS 平台，主要面向为 SSBJ 披露做准备的日本大型上市公司。该法人最初登记为株式会社日本新電力総合研究所，于 2020-04-01 更名为 booost technologies株式会社，并于 2025-04-02 更名为 Booost株式会社（[国税厅法人番号登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)；访问于 2026-10-11）。公司业务起步于电力能源管理，目前仍列有零售电力登记（[公司概况](https://booost.inc/COMPANY_about)；访问于 2026-10-11）。

- 公司自述的导入规模：截至 2025 年 12 月，覆盖 95 个以上国家、约 6,500 家公司（累计）和 197,000 个以上据点（[2026-01-14](https://prtimes.jp/main/html/rd/p/000000237.000056793.html)）。2025 年 9 月同一指标为约 2,000 家公司（[2025-09-29](https://prtimes.jp/main/html/rd/p/000000211.000056793.html)）——见`备注`。
- 最近一轮：**シリーズC 1stクローズ，7 亿日元**，由 One Capital（领投）和プロネクサス出资，预定于 2026-03-31 完成；公司称 Series A 以来累计融资由此达到 **41.5 亿日元**（[2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)）。公司此前就同一累计金额给出的数字无法相互对上——见`备注`。
- 员工人数：公司自己的图表显示 2025 年为 100 人，2021 年为 55 人（[公司介绍资料](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)；访问于 2026-10-11）。截至 2025 年 11 月，员工（不含高管）中 47% 从事产品类工作，外籍员工占 10%（同一资料）。
- 工程：根据当前招聘职位，后端为 PHP/Laravel（部分 Python），前端为 React.js / Vue.js / TypeScript，数据库 MySQL，运行在 AWS 上（[HRMOS](https://hrmos.co/pages/booost/jobs/991960580122120278087)；访问于 2026-10-11）；公司的 Zenn 文章描述了一个 Laravel 单体应用以及一个新的 React SPA（[2025-09-18](https://zenn.dev/booost/articles/114ffed27ad29e)）。工程职位要求日语；混合办公，每周到东京或大阪办公室一天（周三）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前品牌 | Booost（公司）；产品 booost Sustainability。“booost / BOOOST は弊社商標です” | [公司概况](https://booost.inc/COMPANY_about)；访问于 2026-10-11 |
| 法定名称 | Booost株式会社 / Booost, Inc.（登记为Ｂｏｏｏｓｔ株式会社，读音ブースト，英文“Booost,Inc.”） | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)；记录最后更新于 2026-08-24 |
| 法人番号 | 7010001167327 | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327) |
| 曾用法定名称 | 株式会社日本新電力総合研究所（2020-04-01 变更）；booost technologies株式会社（2025-04-02 变更） | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327) |
| 成立 | 2015-04-15 | [公司概况](https://booost.inc/COMPANY_about) |
| 总部 | 〒141-0032 東京都品川区大崎1-6-4 新大崎勧業ビルディング10F（自 2022-12-14 起为登记地址） | [公司概况](https://booost.inc/COMPANY_about)、[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327) |
| 大阪事务所 | 〒533-0031 大阪市東淀川区西淡路1-1-36 新大阪ビル4F | [公司概况](https://booost.inc/COMPANY_about) |
| 代表人 | 代表取締役 青井 宏憲（Hirokazu Aoi） | [公司概况](https://booost.inc/COMPANY_about) |
| 资本金 | 25 亿日元，含资本剩余金（資本剰余金含む），截至 2026 年 3 月末 | [公司概况](https://booost.inc/COMPANY_about) |
| 员工人数 | 100 人（2025 年，公司图表）；截至 2025-01-01 为 90 人（招聘职位中的公司信息栏） | [资料](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)、[HRMOS](https://hrmos.co/pages/booost/jobs/991960580122120278087)；访问于 2026-10-11 |
| 员工构成 | 不含高管，截至 2025-11：产品 47%、业务 31%、咨询 11%、职能 11%；男性 63% / 女性 37%；外籍员工 10% | [资料](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 工作语言 | 日语；工程职位均要求日语，所查职位中没有只用英语的岗位 | [HRMOS 职位](https://hrmos.co/pages/booost)；访问于 2026-10-11 |
| 客户 | 95 个以上国家、约 6,500 家公司（累计）、197,000 个以上据点，截至 2025-12 | [2026-01-14](https://prtimes.jp/main/html/rd/p/000000237.000056793.html) |
| 累计融资 | Series A 以来 41.5 亿日元，含 Series C 1st close（2026-03-26 公布的预计数） | [2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html) |
| 股东（2026 年 3 月末） | グロービス・キャピタル・パートナーズ、東京大学エッジキャピタルパートナーズ、NTTドコモ・ベンチャーズ、三菱UFJキャピタル、One Capital、伊藤忠商事、BIPROGY、パーソルビジネスプロセスデザイン、プロネクサス、经营层（経営陣） | [公司概况](https://booost.inc/COMPANY_about) |
| 上市状态 | 未上市（未上場）；未出现在 2026-10-06 更新的 JPX 新上市日程中 | [PR TIMES 公司信息栏](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)、[JPX](https://www.jpx.co.jp/listing/stocks/new/index.html)；访问于 2026-10-11 |
| 能源相关登记 | 経済産業省 小売電気事業者 登録番号A0244；日本卸電力取引所（JEPX）取引会員 0148；電力広域的運営推進機関会员 | [公司概况](https://booost.inc/COMPANY_about) |
| 信息安全 | ISO/IEC 27001:2022（JIS Q 27001:2023），JP24/00000231，SGSジャパン，总部；首次登记 2024-08-14，有效至 2026-12-14 | [ISMS-AC 登记](https://isms.jp/lst/ind/CR_JP24_x002F_00000231.html) |
| 个人信息保护 | プライバシーマーク 17003780(04)，有效至 2028-01-06 | [JIPDEC 登记](https://entity-search.jipdec.or.jp/pmark/?bango=17003780)；访问于 2026-10-11 |
| SOC 2 | Type 1（基准日 2025-10-31）和 Type 2（期间 2025-11-01 至 2026-01-31），Security 准则，覆盖 booost GX、booost ESG 和 booost Supplier | [Type 1，2025-12-15](https://prtimes.jp/main/html/rd/p/000000232.000056793.html)、[Type 2，2026-03-03](https://prtimes.jp/main/html/rd/p/000000250.000056793.html) |
| 知识产权 | 持有专利 49 件、注册外观设计 9 件、注册商标 92 件；累计申请 241 件（截至 2026 年 6 月） | [知识资产战略页面](https://booost-ai.com/ipstrategy/) |

**公司列出的会员资格与认可**：一般社団法人 新経済連盟、スマートシティ官民連携プラットフォーム（观察员）、日本気候リーダーズ・パートナーシップ（JCLP）、Green x Digitalコンソーシアム、ロボット革命・産業IoTイニシアティブ協議会和 IFRS Sustainability Alliance（[公司概况](https://booost.inc/COMPANY_about)）；联合国全球契约签署方（[2023-09-28](https://prtimes.jp/main/html/rd/p/000000091.000056793.html)）；2035 年净零目标获得 SBT 认定（[2023-11-22](https://prtimes.jp/main/html/rd/p/000000100.000056793.html)）；第4回 IP BASE AWARD 奨励賞（[知识资产战略页面](https://booost-ai.com/ipstrategy/)）。截至 2026-10-11，公司不在 [J-Startup 企业名单](https://www.j-startup.go.jp/startups/)中。

### 品牌与法律实体

| 名称 | 类型 | 期间或状态 | 来源 |
|---|---|---|---|
| 株式会社日本新電力総合研究所 | 曾用法定名称，同一法人（7010001167327） | 至 2020-04-01 | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327) |
| booost technologies株式会社 / booost technologies, Inc. | 曾用法定名称，同一法人 | 登记显示为 2020-04-01 至 2025-04-02；公司公告称变更于 2025-04-15 生效 | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)、[2025-04-15](https://prtimes.jp/main/html/rd/p/000000171.000056793.html) |
| Booost株式会社 / Booost, Inc. | 现法定名称 | 登记显示自 2025-04-02 起 | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327) |
| ENERGY X、ENERGY X GREEN | 曾用产品品牌 | 见于 2022 年公告；公司称 ENERGY X 是 booost Energy 的前身（前身） | [2022-02-02](https://prtimes.jp/main/html/rd/p/000000015.000056793.html)、[2024-10-22](https://prtimes.jp/main/html/rd/p/000000138.000056793.html) |
| booost Sustainability Cloud | 曾用产品名 | 2025-04-15 更名为 booost Sustainability | [2025-04-15](https://prtimes.jp/main/html/rd/p/000000171.000056793.html) |
| booost-tech.com → booost-ai.com | 服务网站域名 | 2026-07-01 变更，旧域名重定向 | [2026-07-01](https://prtimes.jp/main/html/rd/p/000000273.000056793.html) |

登记的总部地址变更：千代田区丸の内1-3-1 → 丸の内1-6-2（2016-12-16）→ 永田町2-11-1 山王パークタワー（2018-01-16）→ 品川区大崎1-6-4（2022-12-14）（[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)）。

### 公司陈述的市场背景

- SSBJ 准则自 2027 年 3 月期起适用于市值 3 万亿日元以上的东证 Prime 上市公司（约 70 家），随后扩展至 1 万亿日元以上（约 200 家）、5,000 亿日元以上（约 300 家），最终预计适用于全部约 1,600 家 Prime 公司（[2026-04-15](https://prtimes.jp/main/html/rd/p/000000258.000056793.html)）。
- 公司提出“サステナビリティ2026問題”一词，指其所描述的企业在强制披露准备上起步晚、危机感不足的状况，并于 2024 年 11 月围绕这一概念发起「日本をSX先進国へ」项目（[2024-11-28](https://prtimes.jp/main/html/rd/p/000000146.000056793.html)）。
- 公司的一项调查显示，12.7% 的企业称其 SSBJ 工作由 CFO 条线主导，可持续发展部门主导占 30.9%，为最常见的回答（[2026-08-05](https://prtimes.jp/main/html/rd/p/000000280.000056793.html)）。

---

## 产品

**booost Sustainability** 被描述为一个“統合型SXプラットフォーム”，覆盖环境、社会和治理方面的“1,200以上のデータポイント”，支持跨集团公司和供应链的多层审批流程，并按第三方鉴证的需要设计（[2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)）。客户可组合使用各模块（[资料，第 37 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）。产品页面位于 [booost-ai.com](https://booost-ai.com/)。

### 产品构成与功能板块

| 板块 | 模块 | 公司描述的功能 | 来源 |
|---|---|---|---|
| 数据收集与管理 | booost ESG、booost GX、booost Supplier、booost Energy、booost PCF | E/S/G 数据；使用排放因子数据库（IDEA、IEA、ecoinvent）的 Scope 1–3 温室气体核算；供应商尽职调查与一手数据；包括 30 分钟智能电表数据在内的能源数据；与 BOM 关联的产品碳足迹 | [资料，第 37 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)、[GX](https://booost-ai.com/gx/)、[Energy](https://booost-ai.com/energy/)、[PCF](https://booost-ai.com/pcf/) |
| 披露与鉴证 | booost Disclosure、booost Audit、booost Regulation | SSBJ/ISSB/CSRD 数据点模板；XBRL 分类标准文件输出与多准则报告；供第三方鉴证机构使用的账号 | [Disclosure](https://booost-ai.com/disclosure/)、[2025-09-30](https://prtimes.jp/main/html/rd/p/000000209.000056793.html) |
| 决策支持 | booost Intelligence、booost Impact | 下钻分析；可持续发展因素在短、中、长期的财务影响 | [Impact](https://booost-ai.com/impact/)、[2025-10-06](https://prtimes.jp/main/html/rd/p/000000214.000056793.html) |
| 数据治理 | booost Data Governance | 审批流程（资料称可自动生成最多 15 层）、25 种语言、全球组织主数据、证据附件 | [资料，第 37 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 供应链数据交换与产品法规 | booost Data EX-PF、booost CBAM、booost DPP、Product Compliance Suite | 基于 PACT 模型的企业间数据交换；欧盟／英国 CBAM 报告；欧盟数字产品护照；自 2026 年 10 月提供的产品法规模块组 | [Data EX-PF](https://booost-ai.com/dataex-pf/)、[CBAM](https://booost-ai.com/cbam/)、[2026-08-26](https://prtimes.jp/main/html/rd/p/000000283.000056793.html)、[2026-08-28](https://prtimes.jp/main/html/rd/p/000000286.000056793.html) |
| AI 功能 | 供应商数据收集 AI、披露草稿生成 AI | 读取格式各异的供应商 Excel 文件并映射到字段；根据收集的数据生成符合 SSBJ/CSRD 的文本草稿 | [2026-04-30](https://prtimes.jp/main/html/rd/p/000000264.000056793.html)、[AI 页面](https://booost-ai.com/ai/) |
| 行业套件 | booost Manufacturing、booost Logistics、booost Automotive | 面向制造业（基于 BOM 的产品排放）、物流（运输排放及省エネ法能源使用量）和汽车行业的预组合模块 | [2025-07-31](https://prtimes.jp/main/html/rd/p/000000194.000056793.html)、[2025-11-05](https://prtimes.jp/main/html/rd/p/000000221.000056793.html)、[2025-11-27](https://prtimes.jp/main/html/rd/p/000000224.000056793.html) |
| 能源采购 | booost Energy Marketplace、booost Transition Driver | 由参与的零售电力公司通过竞价响应的可再生电力采购；集团范围的转型规划 | [Marketplace](https://booost-ai.com/marketplace/)、[条款](https://booost-ai.com/terms/electricity_consumer/)、[2025-09-01](https://prtimes.jp/main/html/rd/p/000000202.000056793.html) |

公司提出的与标准相关的声明：GRI Licensed Software & Tools Partner（[2025-04-23](https://prtimes.jp/main/html/rd/p/000000172.000056793.html)）；面向汽车／电池可追溯性的 ABtC 应用认证（[2025-04-14](https://prtimes.jp/main/html/rd/p/000000170.000056793.html)）；符合 PACT Technical Specifications V3（[2026-02-26](https://prtimes.jp/main/html/rd/p/000000246.000056793.html)），并自 2026-04-01 成为 PACT 解决方案提供商会员（[2026-04-30](https://prtimes.jp/main/html/rd/p/000000263.000056793.html)）；booost PCF 获 SGS Japan 依据 ISO 14067 进行妥当性确认（[2025-11-17](https://prtimes.jp/main/html/rd/p/000000222.000056793.html)）。

### 商业化

- 以 SaaS 形式销售，并提供咨询服务（“Sustainability コンサルティングサービス”）（[公司概况](https://booost.inc/COMPANY_about)）。
- [服务条款](https://booost-ai.com/terms/)（2025-08-20 生效的修订版）规定合同期限为自开通起一年，除非任一方在到期前三个月提出，否则自动续约；费用按另行提供的价目表执行。**未找到公开价目表。**
- **booost CBAM** 可应申请免费提供（[2026-04-01](https://prtimes.jp/main/html/rd/p/000000256.000056793.html)、[CBAM 页面](https://booost-ai.com/cbam/)）。
- 间接渠道：产品计划通过伊藤忠商事各事业部门和 CTC 销售，包括面向约 270 家伊藤忠合并集团公司（[2024-11-27](https://prtimes.jp/main/html/rd/p/000000145.000056793.html)）；BIPROGY 开始提供该产品（[2025-07-11](https://prtimes.jp/main/html/rd/p/000000188.000056793.html)）；プロネクサス与 Booost 计划联合开发并向双方客户群销售，プロネクサス称其客户包括约 2,200 家上市公司（[2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2022-02-02 | 员工 50 人；领投方称产品已服务拥有 20,000 个以上据点的大企业 | [Series A 公告](https://prtimes.jp/main/html/rd/p/000000015.000056793.html) |
| 2024-04-03 | 公司称其管理着日本温室气体总排放量的约 7.5%（日本の温室効果ガス総排出量の約7.5％） | [2024-04-03](https://prtimes.jp/main/html/rd/p/000000112.000056793.html) |
| 2024-10 末 | 80 个以上国家、约 2,000 家公司、186,000 个以上据点 | [Series B 公告](https://prtimes.jp/main/html/rd/p/000000146.000056793.html) |
| 2025-02 | 85 个以上国家、约 2,000 家公司、192,000 个以上据点 | [2025-04-15](https://prtimes.jp/main/html/rd/p/000000171.000056793.html) |
| 2025-09 | 92 个以上国家、约 2,000 家公司、192,000 个以上据点 | [2025-09-29](https://prtimes.jp/main/html/rd/p/000000211.000056793.html) |
| 2025-12 | 95 个以上国家（含香港特别行政区和英属维尔京群岛）、约 6,500 家公司（累计）、197,000 个以上据点（各公司历史最大据点数之和） | [2026-01-14](https://prtimes.jp/main/html/rd/p/000000237.000056793.html) |
| 2024 财年 / 2025 财年（预测） | 年销售额 5,000 亿日元以上企业中的 ITR 市场份额：22.0% / 25.4%，两年均居第一 | [2026-04-15](https://prtimes.jp/main/html/rd/p/000000258.000056793.html) |
| 2021–2025 | 各年员工人数：55、68、68、92、100 | [资料，第 6 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2022-03-15](https://prtimes.jp/main/html/rd/p/000000020.000056793.html) | シスコシステムズ | 合作 |
| [2023-10-17](https://prtimes.jp/main/html/rd/p/000000094.000056793.html) | TSIホールディングス | 提供 booost Sustainability Cloud |
| [2024-05-23](https://prtimes.jp/main/html/rd/p/000000114.000056793.html) | トラスコ中山 | 提供 booost Sustainability Cloud |
| [2024-09-24](https://prtimes.jp/main/html/rd/p/000000127.000056793.html) | 日本ハム | 提供 booost Sustainability Cloud |
| [2024-11-27](https://prtimes.jp/main/html/rd/p/000000145.000056793.html) | 伊藤忠商事 | 资本业务合作；分阶段导入用于集团可持续发展数据；向约 270 家合并集团公司推广销售 |
| [2024-12-20](https://prtimes.jp/main/html/rd/p/000000150.000056793.html) | デロイト トーマツ | 联盟协议 |
| [2025-01-30](https://prtimes.jp/main/html/rd/p/000000157.000056793.html) | アビームコンサルティング | 战略业务合作 |
| [2025-09-30](https://prtimes.jp/main/html/rd/p/000000210.000056793.html) | プロネクサス | 战略合作基本协议（财务与非财务一体化披露） |
| [2025-10-10](https://prtimes.jp/main/html/rd/p/000000216.000056793.html) | アシックス | 导入 booost Sustainability |
| [2025-12-16](https://prtimes.jp/main/html/rd/p/000000233.000056793.html) | ERMグループ | 面向 SSBJ 的联盟协议 |
| [2025-12-23](https://prtimes.jp/main/html/rd/p/000000235.000056793.html) | 阪急阪神ホールディングス | 开始在集团范围内提供 |
| [2026-07-22](https://prtimes.jp/main/html/rd/p/000000278.000056793.html) | SGホールディングス（与アビームコンサルティング） | 共同支持 SSBJ 合规 |
| [2026-07-23](https://prtimes.jp/main/html/rd/p/000000274.000056793.html) | 大日本印刷 | 导入 booost Sustainability |
| [2026-08-27](https://prtimes.jp/main/html/rd/p/000000284.000056793.html) | 伊藤忠ファッションシステム | 面向纺织／服装业欧盟环境法规的行业项目「ESPR-T」 |

[2026-01-14 公告](https://prtimes.jp/main/html/rd/p/000000237.000056793.html)还将ダイキン工業、ニトリホールディングス、ブリヂストン、イオン和荏原製作所列为市值 5,000 亿日元以上的客户。公司公布的政府委托工作包括经济产业省令和7年度电池可持续性平台实证（[2025-10-24](https://prtimes.jp/main/html/rd/p/000000219.000056793.html)）以及令和7年度经济产业省脱碳会议／调查项目（[2025-12-01](https://prtimes.jp/main/html/rd/p/000000228.000056793.html)）。

### 公开计划

- Series C 资金用途：围绕 booost Sustainability、booost Impact 和 booost Disclosure 的产品开发及 AI agent；与プロネクサス共同开发一体化披露平台；招聘“AIエンジニアやプロダクト人材”及披露／法规专业人才（[2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)）。
- 定位为“サステナビリティ×AIカンパニー”，将 AI 扩展到数据收集、质量控制、披露起草、法规更新、鉴证准备和财务影响分析（[2026-07-01](https://prtimes.jp/main/html/rd/p/000000273.000056793.html)）。
- 目标是在 Prime 市场各市值档位（3 万亿、1 万亿、5,000 亿日元）各取得 20% 份额（[note，2025-02-18](https://note.com/booost_tech/n/nd78f47765416)）。
- 招聘资料称公司以 IPO 为目标，并描述了将マーケットプレイス类业务分拆为集团公司的长期计划（[资料，第 7 和第 48 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）；工程职位提到“数年後のIPOを見据えた”增长（[HRMOS](https://hrmos.co/pages/booost/jobs/991960580122120278087)）。

---

## 创始人

**青井 宏憲（Hirokazu Aoi）**——创始人、代表取締役（[公司概况](https://booost.inc/COMPANY_about)）。

- 2010 年：加入一家咨询公司，担任其智慧能源业务团队负责人（[资料，第 4 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）。一篇由公司撰写的 PR TIMES STORY 将其描述为“東証一部コンサルティング会社”，称他在那里管理智慧能源业务团队，但未写出公司名称（[2024-11-28](https://prtimes.com/story/detail/DBngV3iVP2x)）。
- 2015-04：设立公司（[资料，第 4 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）；登记显示该法人在 2020 年前名为株式会社日本新電力総合研究所（[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)）。公司称其于零售电力全面自由化开始的 2015 年，以电力能源管理业务起步（[团队页面](https://booost.inc/COMPANY_team)）。
- 公司资料中未找到其教育背景。

### 主要管理层

| 姓名 | 职务（团队页面，访问于 2026-10-11） | 公开背景 | 来源 |
|---|---|---|---|
| 大我 猛 | 取締役 COO | 前 SAP Japan 常務執行役員 Chief Transformation Officer；曾任职日本 Oracle 和一家外资咨询公司；2023-01 加入 | [资料，第 55 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 高塚 智敬 | 取締役 CTO | NTT Data 高级项目经理（国家核心系统，预算约 20 亿日元）；B2B SaaS 产品管理；与东京大学、京都大学的 AI 联合研究；IPA 数据库专家、PMP。2024-04-03 时职务为執行役員 VPoE，2024-11 前已任 CTO | [资料](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)、[note 访谈，2024-11-27](https://note.com/booost_tech/n/n609965543449)、[2024-04-03](https://prtimes.jp/main/html/rd/p/000000112.000056793.html) |
| 中西 孝夫 | 取締役 CRO | 在 SAP 任 Global Account Director 10 年；在 Oracle 从事销售管理 13 年；2024-03 以 VP of Sales 身份加入；自 2025-03-01 任取締役兼執行役員CRO | [2025-03-04](https://prtimes.jp/main/html/rd/p/000000162.000056793.html) |
| 岡村 崇 | 上級執行役員 Chief of Staff and VP of Strategy | 日本NCR、SAP Japan；Veeva Japan 总经理（2011-03）及代表取締役（2011-05），2022-02 离任；自 2024-01 起任 Booost 顾问；2026-03 加入 | [资料，第 55 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)、[2024-01-29](https://prtimes.jp/main/html/rd/p/000000104.000056793.html)、[2026-06-03](https://prtimes.jp/main/html/rd/p/000000270.000056793.html) |

[团队页面](https://booost.inc/COMPANY_team)上的其他高管：柴田 学（執行役員 CSuO），青井 洸樹和中野 創（執行役員），鈴木 智博（監査役）。该页面列出的顾问：宮田 善孝、笹埜 健斗（庆应 SFC；[2024-06-04](https://prtimes.jp/main/html/rd/p/000000115.000056793.html)）和田中 謙司（东京大学教授）。另行公布的有：前金融厅长官栗田 照久自 2025-09-24 起任特別顧問（[2025-09-29](https://prtimes.jp/main/html/rd/p/000000211.000056793.html)），以及前 Mercari Group CTO 若狭 建任顾问（[2024-04-03](https://prtimes.jp/main/html/rd/p/000000112.000056793.html)）；两人均未出现在当前团队页面上。

团队页面上的成员职能包括プロダクト開発、プロダクトサイト開発、テクニカルサポート、プロフェッショナルサービス、ドメインエキスパート、知財戦略、アライアンス和マーケットプレイス。[资料中的组织图（第 59 页）](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)将プロダクト開発本部置于 CTO 之下，下设プロダクトマネジメント部（能源管理／减排、组织单位、产品单位和设计各组）、エンジニアリング部（第 1–6 组）及一个咨询组；图中还显示 CEO 之下设有トレーディング本部。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2022-02-02 | シリーズA | 12 亿日元 | グロービス・キャピタル・パートナーズ（领投）、東京大学エッジキャピタルパートナーズ（UTEC）、NTTドコモ・ベンチャーズ | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000015.000056793.html) |
| 2022-04-07 | シリーズAのエクステンションラウンド | 未披露 | 三菱UFJキャピタル | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000025.000056793.html) |
| 2024-11-28 | シリーズB | 未单独披露 | One Capital（领投）、伊藤忠商事、BIPROGY、パーソルビジネスプロセスデザイン | Series A 以来 33.5 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000146.000056793.html) |
| 2026-03-26 | シリーズC 1stクローズ | 7 亿日元（预定 2026-03-31 完成） | One Capital（领投）、プロネクサス | Series A 以来 41.5 亿日元（预计） | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)、[BRIDGE](https://thebridge.jp/2026/03/booost-raises-series-c-first-close-for-sustainability-erp) |

Series B 的三家企业投资方均另签有资本业务合作协议：BIPROGY 和パーソルビジネスプロセスデザイン于 [2024-10-29](https://prtimes.jp/main/html/rd/p/000000139.000056793.html)，伊藤忠商事于 [2024-11-27](https://prtimes.jp/main/html/rd/p/000000145.000056793.html)。One Capital 同时领投了 Series B 和 Series C；プロネクサス在出资前已于 2025 年 9 月签署战略合作基本协议（[2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)）。Series B 与「日本をSX先進国へ」项目及一项针对 Prime 上市公司 600 人的调查一同公布；Series C 公告将其称为“1stクローズ”，但截至 2026-10-11 未找到后续 close。公司只统计“シリーズA以降”的融资；未找到描述更早融资的公告。

---

## 工程

### 技术栈与平台

按证据类型标注。

- **后端——由技术文章和职位确认：** PHP 与 Laravel；职位写明“PHP（一部Python）”。公司一篇 Zenn 文章描述了承载多个服务的“Laravelをベースとしたモノリシックな構成”（[2025-09-18](https://zenn.dev/booost/articles/114ffed27ad29e)）；其他 Zenn 文章涉及 Laravel 升级和 Carbon 3（[Zenn publication](https://zenn.dev/p/booost)）。一篇关于 DDD 的技术博客文章以 PHP 实现的温室气体排放聚合作为教学示例（[2025-06-27](https://zenn.dev/booost/articles/2ec4340c1d5f21)）。
- **前端——由技术文章确认：** 现有产品是使用 Vue.js、TypeScript、Laravel Blade 和 Bootstrap 4 构建的 MPA；一个新产品使用 React SPA，搭配 TypeScript、Tailwind CSS、shadcn/ui、React Router、TanStack Query 和 react-hook-form，并在 GitHub Actions 中用 Storybook 和 Vitest 测试（[2025-09-18](https://zenn.dev/booost/articles/114ffed27ad29e)）。职位列出“React.js、Vue.js、TypeScript”。
- **数据库——来自职位：** MySQL（[Web 应用工程师](https://hrmos.co/pages/booost/jobs/991960580122120278087)）。
- **云与基础设施——来自职位和技术文章：** AWS（SRE 职位列出 EC2、RDS、ALB、GuardDuty、CloudWatch）；[SRE 职位](https://hrmos.co/pages/booost/jobs/000007601)列出的 IaC 为“OpenTofu（terraform)”和 Ansible，[EM 职位](https://hrmos.co/pages/booost/jobs/991960580122120278018)列出“AWS cdk”和 Docker。2024 年 12 月的一篇 Zenn 文章称基础设施以 AWS CDK 编码，并在考虑部分迁移到 Terraform（[2024-12-25](https://zenn.dev/booost/articles/b053f025660b6b)）。
- **CI/CD——来自职位：** GitHub Actions、AWS CodePipeline/CodeBuild。
- **可观测性与安全——来自职位和技术文章：** New Relic（[SRE 职位](https://hrmos.co/pages/booost/jobs/00000720251104)；一篇关于 New Relic Flex 的 [2026-05-19 Zenn 文章](https://zenn.dev/booost/articles/2c98cc299e108e)）、Wiz（[2025-06-13](https://zenn.dev/booost/articles/4cd39da88ffff3)）和 Vanta（SRE 职位）。
- **AI 开发工具——来自职位和招聘页面：** Claude / Claude Code、ChatGPT / Codex、Cursor、用于 AI 代码审查的 CodeRabbit、Notion AI；QA 职位列出的是 GitHub Copilot 而非 Claude Code（[产品开发招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)、[QA 职位](https://hrmos.co/pages/booost/jobs/00000720251105)）。
- **协作：** Slack、Asana、Gather（据 [2024-10-29](https://zenn.dev/booost/articles/gather-introduction)，已在开发组织内导入）、Notion；设计使用 Figma 和 Adobe XD。
- **标准与外部数据——由公司公告确认：** PACT 数据模型及 Technical Specifications V3；booost Data EX-PF 参照的 Open Data Spaces Protocols / ODS-RAM（[2026-06-11](https://prtimes.jp/main/html/rd/p/000000271.000056793.html)）；经济产业省的ウラノス・エコシステム（[2024-06-14](https://prtimes.jp/main/html/rd/p/000000116.000056793.html)）；通过 API 更新的 AIST-IDEA 排放因子（[2026-05-12](https://prtimes.jp/main/html/rd/p/000000260.000056793.html)）；XBRL。

所查来源未说明云区域、容器编排方式，以及 MySQL 以外的任何数据存储。

### 系统

| 系统 | 功能 | 来源 |
|---|---|---|
| 集团可持续发展数据收集 | 从集团公司和据点收集 1,200 个以上 ESG 数据点，支持多层审批流程、权限和证据附件 | [2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)、[资料，第 37 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 温室气体核算 | 使用 IDEA、IEA 和 ecoinvent 排放因子进行 Scope 1–3 计算及碳会计自动分录；通过 API 刷新 AIST-IDEA 因子 | [资料，第 37 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)、[2026-05-12](https://prtimes.jp/main/html/rd/p/000000260.000056793.html) |
| 智能电表 Scope 2 | 利用 30 分钟间隔的智能电表电力数据计算 Scope 2；依据修订后的电气事业法，自 2023-10 起非电力企业也可使用这些数据 | [2024-07-02](https://prtimes.jp/main/html/rd/p/000000118.000056793.html) |
| 产品碳足迹 | 与 BOM 关联、按零部件逐级汇总的产品级 CFP；获 SGS Japan 依据 ISO 14067 妥当性确认 | [2025-07-31](https://prtimes.jp/main/html/rd/p/000000194.000056793.html)、[2025-11-17](https://prtimes.jp/main/html/rd/p/000000222.000056793.html) |
| booost Data EX-PF | 遵循 WBCSD/PACT 数据模型并参照 ODS-RAM 的供应链数据交换平台，具备数据主权和商业秘密保护；booost CBAM 作为其附加功能运行 | [2026-02-26](https://prtimes.jp/main/html/rd/p/000000244.000056793.html)、[2026-06-11](https://prtimes.jp/main/html/rd/p/000000271.000056793.html)、[2026-04-01](https://prtimes.jp/main/html/rd/p/000000256.000056793.html) |
| 披露与 XBRL | 定量／定性披露项目、标签、XBRL 分类标准文件输出以及多准则报告（SSBJ 等） | [2025-09-30](https://prtimes.jp/main/html/rd/p/000000209.000056793.html)、[资料，第 37 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 财务影响 | 将非财务因素与分录和科目数据关联以计算财务影响，基于专利第 7588352 号 | [2025-10-06](https://prtimes.jp/main/html/rd/p/000000214.000056793.html)、[2026-04-15](https://prtimes.jp/main/html/rd/p/000000258.000056793.html) |
| AI 功能 | 解析供应商 Excel 并映射字段、检测错误；生成披露草稿；服务网站宣传 Supplier、Disclosure、Audit 和 Reduction 四类 agent | [2026-04-30](https://prtimes.jp/main/html/rd/p/000000264.000056793.html)、[booost-ai.com](https://booost-ai.com/) |
| DPP | 收集产品与供应链信息、生成并发布 DPP、访问权限管理和历史管理 | [2026-08-26](https://prtimes.jp/main/html/rd/p/000000283.000056793.html) |
| Energy Marketplace | 客户提交采购条件；参与的零售电力公司通过竞价响应，并使用在 booost Sustainability 中收集的数据 | [条款，2026-08-07 生效](https://booost-ai.com/terms/electricity_consumer/) |

CTO 称，服务器设计、应用设计和实现环境都是为拥有大量实体和据点、集团结构复杂的大型组织构建的（[note，2024-11-27](https://note.com/booost_tech/n/n609965543449)）。

### 招聘所需技术背景

来自当前 HRMOS 职位（无日期，访问于 2026-10-11）：

- **Web 应用工程师**——必需：使用 PHP、Python、Ruby、Java 等语言开发 Web 应用 2 年以上；从详细设计到实现和测试的经验；RDB 设计与操作；基于 Git/GitHub 的团队开发；在日本企业使用日语工作的经验；对 AI 辅助开发感兴趣。优先：PHP/Laravel、React.js/Vue.js/TypeScript、AWS 基础使用（[职位](https://hrmos.co/pages/booost/jobs/991960580122120278087)）。
- **高级工程师**——必需：后端开发 3 年以上、前端经验、需求定义和基本设计、通过代码审查提升质量、使用 AI 工具开发。优先：AWS 设计与构建、CI/CD、SaaS 或企业级产品、带领团队（[职位](https://hrmos.co/pages/booost/jobs/991960580122120278101)）。
- **后端技术负责人**——必需：B2B Web 开发 5 年以上、RDBMS 数据建模与运维、技术指导、中长期技术战略。优先：基于容器的系统、ISUCON 等性能调优、作为技术负责人承担决策、测试代码、OSS 贡献、气候／能源行业开发。职责包括规定架构“ドメイン駆動、クリーンアーキテクチャなど”（[职位](https://hrmos.co/pages/booost/jobs/991960580122120278086)）。
- **SRE（负责人／经理候选）**——必需：在 AWS 上设计、构建和运维 Web 三层架构，Linux 服务器，Infrastructure as Code；经理岗位另需管理 2–3 人及制定路线图。优先：大规模基础设施、主导 SRE 实践（SLI/SLO）、CI/CD、容器架构、Python 3 脚本（[负责人](https://hrmos.co/pages/booost/jobs/000007601)、[经理](https://hrmos.co/pages/booost/jobs/00000720251104)）。
- **QA 工程师**——必需：B2B Web 应用测试 3 年以上，测试计划／设计／执行，将复杂业务领域转化为测试设计。优先：左移参与、质量指标、单元／API／E2E 自动化、非功能测试（[职位](https://hrmos.co/pages/booost/jobs/00000720251105)）。
- **产品经理**——必需：B2B Web 产品管理或项目管理、与客户进行需求定义。优先：画面与数据库设计、企业级服务、中大型 SI 项目管理、SQL；明确欢迎来自 SIer 或 IT 咨询的候选人（[职位](https://hrmos.co/pages/booost/jobs/991960580122120278109)）。

### 行业领域

工作内容建立在企业可持续发展披露和碳核算之上：ISSB/IFRS S1–S2、SSBJ、CSRD/ESRS、GRI 和 TCFD；GHG Protocol Scope 1–3 及排放因子数据库；产品碳足迹（ISO 14067、PACT）；欧盟／英国 CBAM、欧盟 ESPR 与数字产品护照以及电池可追溯性；XBRL 和 EDINET 分类标准；第三方鉴证与内部控制；以及日本电力市场（零售供电、JEPX、智能电表数据、可再生能源采购）。

工程职位写明“入社時点でサステナビリティ領域の知識・経験は必要ございません”，并称相关知识可通过培训、工作和资格考取支持获得（[Web 应用工程师](https://hrmos.co/pages/booost/jobs/991960580122120278087)）。后端技术负责人、SRE 和 EM 职位将气候或能源行业开发经验列为优先条件；产品经理职位将可持续发展／能源经验列为优先条件。公司称鼓励全体员工考取サステナ経営検定 2 级，并列出 GX検定、炭素会計アドバイザー等其他支持的资格（[资料，第 63–64 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 日语。Web 应用工程师要求有在日本企业使用日语工作的经历；后端技术负责人、SRE 和 PdM 要求“Native-like fluency in Japanese”；QA 要求商务日语 | [HRMOS 职位](https://hrmos.co/pages/booost) |
| 地点 | 东京总部（大崎）或大阪事务所；工程职位称东京与大阪成员比例为 1:1 | [Web 应用工程师](https://hrmos.co/pages/booost/jobs/991960580122120278087) |
| 远程 | 混合办公，每周到岗一天，建议周三；产品开发部门被描述为“週4リモート勤務”，周三为到岗日；无法通勤到东京或大阪者可“応相談”全远程（Web 应用工程师职位） | [招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)、[职位](https://hrmos.co/pages/booost/jobs/991960580122120278087) |
| 工作时间 | 弹性工作制，标准工作日 7.5 小时；产品岗位核心时间 13:00–17:00，其他部门 11:00–15:00；部分工程岗位可能适用裁量労働制 | [职位](https://hrmos.co/pages/booost/jobs/991960580122120278086)、[资料，第 62 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 薪资（HRMOS，月薪） | Web 应用工程师 26.7 万–47.6 万日元；高级工程师 41.6 万–83.3 万日元；后端技术负责人 47.6 万–107.1 万日元；SRE 负责人 35.7 万–88.0 万日元；SRE 经理 47.6 万–100.0 万日元；产品经理 47.6 万–89.2 万日元；加班费另付；按业绩每年两次奖金 | [HRMOS 职位](https://hrmos.co/pages/booost) |
| 薪资（Green，年薪） | Web 应用工程师 450 万–800 万日元；SRE 负责人 600 万–1,200 万日元；EM 700 万–1,600 万日元；后端技术负责人 800 万–1,800 万日元；产品经理 800 万–1,500 万日元 | [Green](https://www.green-japan.com/company/8922)；无日期，访问于 2026-10-11 |
| 休假 | 年休约 125 天；入职时带薪年假 5 天，六个月后再给 5 天；夏季、年末年始、产假、育儿假和护理假 | [职位](https://hrmos.co/pages/booost/jobs/991960580122120278087) |
| 福利 | 社会保险、通勤补贴、体检、内部交流费用补助、育儿短时工作、“Booostアカデミア”培训、资格考取支持 | [招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)、[资料，第 63 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |
| 试用期 | 三个月；不纳入评估和奖金 | [职位](https://hrmos.co/pages/booost/jobs/991960580122120278087) |
| 招聘流程 | 休闲面谈、书面筛选、约三轮面试、终面前进行背景调查（reference check）；从申请到录用 2–4 周 | [招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829) |
| 团队结构 | プロダクト開発本部 = 产品管理组（客户沟通、需求、基本设计）和工程组（详细设计、实现、基础设施、安全）。2024 年 12 月 SRE 组共 4 人：2 名正式员工和 2 名来自 Topotal 的 SRE-as-a-Service 人员，分布在关东和关西，全远程 | [招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)、[Zenn，2024-12-25](https://zenn.dev/booost/articles/b053f025660b6b) |
| 其他人力数据 | 截至 2025-11（不含高管）：男性育儿假取得率 50%、有子女员工 42%、带薪假使用率 75% | [资料，第 57 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：booost.inc（sitemap、公司、团队、新闻、招聘页面），booost-ai.com（sitemap、产品、法律、知识产权和安全页面），PR TIMES 公司页面和 RSS（最近 200 条公告，另逐条打开了更早的公告），note、Zenn publication、Speaker Deck、HRMOS 职位、产品开发 Notion 页面、Green、Japan Dev 和 TokyoDev（TokyoDev 返回了反爬验证）；国税厅登记、ISMS-AC 和 JIPDEC 登记、JPX 新上市页面和 J-Startup 名单；对 booost、booost-tech、booost-technologies、booostinc、booost-inc、booost-ai、booosttech 和 booost-sustainability 的 GitHub 组织查询，以及用户／组织搜索；INITIAL 仅作线索。检索词包括 Booost、booost technologies、日本新電力総合研究所及各产品名，使用日文和英文。

- **营收、ARR 和盈利情况。** 未披露。One Capital 在 [Series C 公告](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)中的评论提到 ARR 增长，但没有数字。网络检索未找到已公布的决算公告；未直接检索官报。
- **Series B 金额与估值。** Series B 只通过累计总额披露，而这些总额无法相互对上（见下文）。公司未公布估值。
- **Series A 之前的融资。** 未找到。
- **当前工程人数。** 未公布。资料给出产品类岗位占非高管员工的 47%（2025-11），团队页面显示 24 个标为プロダクト開発或プロダクトサイト開発的成员条目，其中部分只有姓名首字母，四个没有姓名（访问于 2026-10-11）；两者都不是工程人数。
- **公开价目表与公开 API 参考文档。** 均未找到。CBAM 页面提到“PACT技術仕様に準拠したAPI”，但没有公开文档。
- **云区域、托管拓扑、状态页或 SLA。** 未找到。
- **开源。** GitHub 组织 [`jepco-system`](https://github.com/jepco-system) 名称为“Booost”，链接到 booost.inc；它有一个公开仓库 [`pact-catalog`](https://github.com/jepco-system/pact-catalog)，是 `wbcsd/pact-catalog` 的 TypeScript fork，描述为“booostGX for pact-catalog”，最后推送于 2023-07-13。另有一个名为 `Booost-ai` 的组织，没有公开仓库，也没有资料元数据，无法确认与公司的关系。该组织元数据未列出 X 账号或邮箱。
- **签证担保、英语工程岗位和应届工程师招聘。** 所查职位中均未找到。
- **离职率。** 未公布。

### 不同来源之间的不一致

- **Series A 以来累计融资：** Series B 后为 33.5 亿日元（[2024-11-28 公告](https://prtimes.jp/main/html/rd/p/000000146.000056793.html)；[资料，第 8 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）；Series B 后为 36.5 亿日元（[note，2025-02-18](https://note.com/booost_tech/n/nd78f47765416)）；加上 7 亿日元 Series C 1st close 后为 41.5 亿日元（[2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)）。33.5 + 7 = 40.5，36.5 + 7 = 43.5；公司未解释差异。
- **Series C 时间：** 资料的沿革页写有“2024年シリーズCで総額41.5億円の資金調達を実施”（[第 7 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)），而其下一页和公告均将 Series C 定在 2026 年 3 月。
- **Series A 时间：** 2022-02-02 公布（[公告](https://prtimes.jp/main/html/rd/p/000000015.000056793.html)）；extension 公告称 Series A 于“2022年1月”实施（[2022-04-07](https://prtimes.jp/main/html/rd/p/000000025.000056793.html)）；Series B 公告称 Series A 轮于 2022 年 4 月完成（[2024-11-28](https://prtimes.jp/main/html/rd/p/000000146.000056793.html)）。
- **更名日期：** 登记记录变更为 Booost株式会社的日期为 2025-04-02（[国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)）；公司公告称于 2025-04-15 生效（[公告](https://prtimes.jp/main/html/rd/p/000000171.000056793.html)）。
- **创立时名称：** 公司资料称 booost technologies 于 2015 年 4 月创业或设立（[资料，第 7 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)；[PR TIMES STORY](https://prtimes.com/story/detail/DBngV3iVP2x)）；登记显示该法人在 2020-04-01 之前为株式会社日本新電力総合研究所。
- **客户数：** 2025 年 9 月约 2,000 家（[2025-09-29](https://prtimes.jp/main/html/rd/p/000000211.000056793.html)、[SOC 2 Type 1 公告](https://prtimes.jp/main/html/rd/p/000000232.000056793.html)），而 2025 年 12 月累计约 6,500 家（[2026-01-14](https://prtimes.jp/main/html/rd/p/000000237.000056793.html)）；只有后一个数字标明为累计，两份公告均未定义“公司”的计数口径。2024 年 10 月末的据点数，在 [伊藤忠公告](https://prtimes.jp/main/html/rd/p/000000145.000056793.html)中为 180,000 个以上，在一天后的 [Series B 公告](https://prtimes.jp/main/html/rd/p/000000146.000056793.html)中为 186,000 个以上。
- **2024 财年 ITR 份额：** 22.4%（预测，ITR 2025 年版；[2025-07-01](https://prtimes.jp/main/html/rd/p/000000185.000056793.html)）对比 22.0%（ITR 2026 年版；[2026-04-15](https://prtimes.jp/main/html/rd/p/000000258.000056793.html)）。
- **基础设施即代码：** AWS CDK，并在考虑迁移到 Terraform（[Zenn，2024-12-25](https://zenn.dev/booost/articles/b053f025660b6b)）；[EM 职位](https://hrmos.co/pages/booost/jobs/991960580122120278018)写“AWS cdk”；[SRE 职位](https://hrmos.co/pages/booost/jobs/000007601)写“OpenTofu（terraform)”和 Ansible。
- **育儿短时工作：** [招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)和[资料第 62 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)写“小学4年生まで”，而 [HRMOS 职位](https://hrmos.co/pages/booost/jobs/991960580122120278087)写“3歳に満たない子を養育する従業員”。
- **招聘流程：** 约三轮面试、2–4 周（[招聘页面](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)），对比 2–4 轮面试、约一个月（[资料，第 67 页](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)）。

### 其他

- **电力业务渊源。** 公司概况仍列有零售电力登记（A0244）和 JEPX 交易会员资格，资料中的组织图包含トレーディング本部，booost Energy Marketplace 条款于 2026-08-07 修订（[公司概况](https://booost.inc/COMPANY_about)、[条款](https://booost-ai.com/terms/electricity_consumer/)）。2022 年 Series A 公告将产品描述为 ENERGY X（“CO2フリー電気の調達、供給が可能なクラウド型エネルギーマネジメントシステム”）和 ENERGY X GREEN（[2022-02-02](https://prtimes.jp/main/html/rd/p/000000015.000056793.html)）。
- **域名。** 公司网站自 2025-04-15 起为 booost.inc；服务网站于 2026-07-01 从 booost-tech.com 迁至 booost-ai.com；booost.inc 上仍有部分链接指向 booost-tech.com（访问于 2026-10-11）。
- **公告构成。** 截至 2026-10-11，最近 20 条 PR TIMES 公告中有 12 条是研讨会、社群活动、会议、圆桌会或演讲的通知（[PR TIMES 公司页面](https://prtimes.jp/main/html/searchrlp/company_id/56793)）。公司还运营 Sustainability Leadership Community（SLC），并称会员已超过 1,000 人（[2026-04-03](https://prtimes.jp/main/html/rd/p/000000257.000056793.html)）。
- **Speaker Deck 日期。** 公司介绍资料显示的发布日期为 2025-04-14，但内容包含截至 2025 年 11 月和 2026 年 3 月的数字；本文按访问日期 2026-10-11 引用。
- **技术演讲。** 公司工程师撰文介绍了在 PHPerKaigi 2025 和 2026，以及关西、福冈和北海道的 PHP 会议上的演讲（[Zenn publication](https://zenn.dev/p/booost)）。

---

## 资料来源

**官方**

- [公司网站（日文）](https://booost.inc/) · [英文](https://booost.inc/TOP_EN)
- [公司概况](https://booost.inc/COMPANY_about) · [团队](https://booost.inc/COMPANY_team) · [新闻](https://booost.inc/NEWS) · [招聘](https://booost.inc/RECRUIT)
- [服务网站——booost Sustainability](https://booost-ai.com/)
  - [booost GX](https://booost-ai.com/gx/) · [booost Energy](https://booost-ai.com/energy/) · [booost PCF](https://booost-ai.com/pcf/) · [booost Disclosure](https://booost-ai.com/disclosure/) · [booost Impact](https://booost-ai.com/impact/)
  - [booost Data EX-PF](https://booost-ai.com/dataex-pf/) · [booost CBAM](https://booost-ai.com/cbam/) · [AI](https://booost-ai.com/ai/) · [Energy Marketplace](https://booost-ai.com/marketplace/)
  - [服务条款](https://booost-ai.com/terms/) · [Energy Marketplace 条款](https://booost-ai.com/terms/electricity_consumer/) · [信息安全方针](https://booost-ai.com/security-policy/) · [知识资产战略](https://booost-ai.com/ipstrategy/)
- [产品开发招聘页面（Notion）](https://booost-tech.notion.site/booost-technologies-3a148cd671c845ecb2778a19bc592829)
- [HRMOS 职位列表](https://hrmos.co/pages/booost)——[Web 应用工程师](https://hrmos.co/pages/booost/jobs/991960580122120278087)、[高级工程师](https://hrmos.co/pages/booost/jobs/991960580122120278101)、[后端技术负责人](https://hrmos.co/pages/booost/jobs/991960580122120278086)、[EM](https://hrmos.co/pages/booost/jobs/991960580122120278018)、[SRE 负责人](https://hrmos.co/pages/booost/jobs/000007601)、[SRE 经理](https://hrmos.co/pages/booost/jobs/00000720251104)、[QA 工程师](https://hrmos.co/pages/booost/jobs/00000720251105)、[产品经理](https://hrmos.co/pages/booost/jobs/991960580122120278109)
- [Zenn publication（日文）](https://zenn.dev/p/booost)——[Laravel 单体中的前端技术选型](https://zenn.dev/booost/articles/114ffed27ad29e)、[SRE 团队](https://zenn.dev/booost/articles/b053f025660b6b)、[New Relic Flex](https://zenn.dev/booost/articles/2c98cc299e108e)、[Wiz](https://zenn.dev/booost/articles/4cd39da88ffff3)、[以温室气体排放为例的 DDD](https://zenn.dev/booost/articles/2ec4340c1d5f21)、[Gather](https://zenn.dev/booost/articles/gather-introduction)
- [note（日文）](https://note.com/booost_tech)——[CTO 访谈](https://note.com/booost_tech/n/n609965543449)、[Series B 投资方推荐语](https://note.com/booost_tech/n/nd78f47765416)
- [公司介绍资料（Speaker Deck，日文）](https://speakerdeck.com/booost/hui-she-shao-jie-zi-liao-booostzhu-shi-hui-she)
- [GitHub 组织 `jepco-system`](https://github.com/jepco-system) · [`pact-catalog` fork](https://github.com/jepco-system/pact-catalog)

**新闻稿（PR TIMES，日文，较新在前）**

- [公司页面与完整公告索引](https://prtimes.jp/main/html/searchrlp/company_id/56793)
- [Product Compliance Suite — 2026-08-28](https://prtimes.jp/main/html/rd/p/000000286.000056793.html)
- [伊藤忠ファッションシステム ESPR-T 项目 — 2026-08-27](https://prtimes.jp/main/html/rd/p/000000284.000056793.html)
- [booost DPP — 2026-08-26](https://prtimes.jp/main/html/rd/p/000000283.000056793.html)
- [SSBJ 调查 — 2026-08-05](https://prtimes.jp/main/html/rd/p/000000280.000056793.html)
- [大日本印刷导入 — 2026-07-23](https://prtimes.jp/main/html/rd/p/000000274.000056793.html)
- [SGホールディングス 与 ABeam — 2026-07-22](https://prtimes.jp/main/html/rd/p/000000278.000056793.html)
- [可持续发展 × AI 与域名变更 — 2026-07-01](https://prtimes.jp/main/html/rd/p/000000273.000056793.html)
- [booost Data EX-PF 更新（ODP）— 2026-06-11](https://prtimes.jp/main/html/rd/p/000000271.000056793.html)
- [岡村相关文章 — 2026-06-03](https://prtimes.jp/main/html/rd/p/000000270.000056793.html)
- [AIST-IDEA API 对接 — 2026-05-12](https://prtimes.jp/main/html/rd/p/000000260.000056793.html)
- [AI 功能 — 2026-04-30](https://prtimes.jp/main/html/rd/p/000000264.000056793.html)
- [PACT 解决方案提供商会员 — 2026-04-30](https://prtimes.jp/main/html/rd/p/000000263.000056793.html)
- [ITR 份额连续第二年 — 2026-04-15](https://prtimes.jp/main/html/rd/p/000000258.000056793.html)
- [SLC 会员超过 1,000 人 — 2026-04-03](https://prtimes.jp/main/html/rd/p/000000257.000056793.html)
- [booost CBAM 免费 — 2026-04-01](https://prtimes.jp/main/html/rd/p/000000256.000056793.html)
- [Series C 1st close，7 亿日元 — 2026-03-26](https://prtimes.jp/main/html/rd/p/000000254.000056793.html)
- [SOC 2 Type 2 — 2026-03-03](https://prtimes.jp/main/html/rd/p/000000250.000056793.html)
- [符合 PACT Technical Specifications V3 — 2026-02-26](https://prtimes.jp/main/html/rd/p/000000246.000056793.html)
- [booost Data EX-PF — 2026-02-26](https://prtimes.jp/main/html/rd/p/000000244.000056793.html)
- [约 6,500 家公司 — 2026-01-14](https://prtimes.jp/main/html/rd/p/000000237.000056793.html)
- [阪急阪神ホールディングス — 2025-12-23](https://prtimes.jp/main/html/rd/p/000000235.000056793.html)
- [ERM 联盟 — 2025-12-16](https://prtimes.jp/main/html/rd/p/000000233.000056793.html)
- [SOC 2 Type 1 — 2025-12-15](https://prtimes.jp/main/html/rd/p/000000232.000056793.html)
- [经济产业省脱碳会议项目 — 2025-12-01](https://prtimes.jp/main/html/rd/p/000000228.000056793.html)
- [booost Automotive — 2025-11-27](https://prtimes.jp/main/html/rd/p/000000224.000056793.html)
- [booost PCF ISO 14067 妥当性确认 — 2025-11-17](https://prtimes.jp/main/html/rd/p/000000222.000056793.html)
- [booost Logistics — 2025-11-05](https://prtimes.jp/main/html/rd/p/000000221.000056793.html)
- [经济产业省电池平台项目 — 2025-10-24](https://prtimes.jp/main/html/rd/p/000000219.000056793.html)
- [アシックス导入 — 2025-10-10](https://prtimes.jp/main/html/rd/p/000000216.000056793.html)
- [财务影响功能 — 2025-10-06](https://prtimes.jp/main/html/rd/p/000000214.000056793.html)
- [プロネクサス基本协议 — 2025-09-30](https://prtimes.jp/main/html/rd/p/000000210.000056793.html)
- [多准则报告与 XBRL — 2025-09-30](https://prtimes.jp/main/html/rd/p/000000209.000056793.html)
- [特別顧問栗田 照久 — 2025-09-29](https://prtimes.jp/main/html/rd/p/000000211.000056793.html)
- [booost Transition Driver — 2025-09-01](https://prtimes.jp/main/html/rd/p/000000202.000056793.html)
- [booost Manufacturing — 2025-07-31](https://prtimes.jp/main/html/rd/p/000000194.000056793.html)
- [BIPROGY 渠道提供 — 2025-07-11](https://prtimes.jp/main/html/rd/p/000000188.000056793.html)
- [ITR 份额 22.4% — 2025-07-01](https://prtimes.jp/main/html/rd/p/000000185.000056793.html)
- [GRI Licensed Software & Tools Partner — 2025-04-23](https://prtimes.jp/main/html/rd/p/000000172.000056793.html)
- [更名为 Booost — 2025-04-15](https://prtimes.jp/main/html/rd/p/000000171.000056793.html)
- [ABtC 认证 — 2025-04-14](https://prtimes.jp/main/html/rd/p/000000170.000056793.html)
- [CRO 任命 — 2025-03-04](https://prtimes.jp/main/html/rd/p/000000162.000056793.html)
- [アビームコンサルティング合作 — 2025-01-30](https://prtimes.jp/main/html/rd/p/000000157.000056793.html)
- [デロイト トーマツ联盟 — 2024-12-20](https://prtimes.jp/main/html/rd/p/000000150.000056793.html)
- [Series B 与「日本をSX先進国へ」项目 — 2024-11-28](https://prtimes.jp/main/html/rd/p/000000146.000056793.html)
- [伊藤忠商事资本业务合作 — 2024-11-27](https://prtimes.jp/main/html/rd/p/000000145.000056793.html)
- [BIPROGY 与パーソルビジネスプロセスデザイン合作 — 2024-10-29](https://prtimes.jp/main/html/rd/p/000000139.000056793.html)
- [业务扩展至 SX — 2024-10-22](https://prtimes.jp/main/html/rd/p/000000138.000056793.html)
- [日本ハム — 2024-09-24](https://prtimes.jp/main/html/rd/p/000000127.000056793.html)
- [智能电表 Scope 2 — 2024-07-02](https://prtimes.jp/main/html/rd/p/000000118.000056793.html)
- [ウラノス・エコシステム — 2024-06-14](https://prtimes.jp/main/html/rd/p/000000116.000056793.html)
- [顾问笹埜 健斗 — 2024-06-04](https://prtimes.jp/main/html/rd/p/000000115.000056793.html)
- [トラスコ中山 — 2024-05-23](https://prtimes.jp/main/html/rd/p/000000114.000056793.html)
- [顾问若狭 建 — 2024-04-03](https://prtimes.jp/main/html/rd/p/000000112.000056793.html)
- [顾问岡村 — 2024-01-29](https://prtimes.jp/main/html/rd/p/000000104.000056793.html)
- [SBT 认定 — 2023-11-22](https://prtimes.jp/main/html/rd/p/000000100.000056793.html)
- [TSIホールディングス — 2023-10-17](https://prtimes.jp/main/html/rd/p/000000094.000056793.html)
- [联合国全球契约 — 2023-09-28](https://prtimes.jp/main/html/rd/p/000000091.000056793.html)
- [シスコシステムズ合作 — 2022-03-15](https://prtimes.jp/main/html/rd/p/000000020.000056793.html)
- [Series A extension — 2022-04-07](https://prtimes.jp/main/html/rd/p/000000025.000056793.html)
- [Series A，12 亿日元 — 2022-02-02](https://prtimes.jp/main/html/rd/p/000000015.000056793.html)

**登记、报道与档案**

- [国税庁 法人番号公表サイト — 7010001167327（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010001167327)
- [ISMS-AC 登记 — JP24/00000231（日文）](https://isms.jp/lst/ind/CR_JP24_x002F_00000231.html)
- [JIPDEC 隐私标志登记 — 17003780（日文）](https://entity-search.jipdec.or.jp/pmark/?bango=17003780)
- [JPX 新上市（日文）](https://www.jpx.co.jp/listing/stocks/new/index.html) · [J-Startup 企业名单](https://www.j-startup.go.jp/startups/)
- [BRIDGE — Series C，2026-03（日文）](https://thebridge.jp/2026/03/booost-raises-series-c-first-close-for-sustainability-erp)
- [PR TIMES STORY — CEO 谈 2026 问题，2024-11-28（日文）](https://prtimes.com/story/detail/DBngV3iVP2x)
- [Green — 公司页面（日文）](https://www.green-japan.com/company/8922)
- [INITIAL / Speeda（日文）](https://initial.inc/companies/A-37922)
