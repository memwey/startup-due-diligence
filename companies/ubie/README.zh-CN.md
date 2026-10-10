# Ubie

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Ubie（Ubie株式会社 / Ubie, Inc.；法人番号 7010701034132）是一家总部位于东京、成立于 2017 年 5 月的公司，由医师阿部吉倫（Yoshinori Abe）和工程师久保恒太（Kota Kubo）创立。公司以同一个 AI 问诊引擎支撑三项业务：一是面向消费者的免费服务「ユビー」（2020 年起为症状检索服务，2025-09-16 又以同一名称增加了对话式“医療AIパートナー”）；二是以“ユビーメディカルナビ”名义销售的医院和诊所产品（ユビーAI問診、ユビー生成AI、ユビーDPCサポーター、ユビーリンク）；三是面向制药企业的疾病认知与营销解决方案。纽约子公司 Ubie Inc. 运营英文服务 `ubiehealth.com` 和面向医疗机构的产品 Ubie Smart Support（[About](https://ubie.life/about_ubie)、[Service](https://ubie.life/service)；无日期，访问于 2026-10-11）。

- **规模：** 「ユビー」月活用户约 1,300 万；ユビー生成AI 已在 160 多家大型医院使用，其中包括 20 多家大学医院（[2026-09-28 公告](https://prtimes.jp/main/html/rd/p/000000227.000048083.html)）。美国公司称美国月活用户约 600 万，全球超过 2,000 万（[PR Newswire，2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html)）。
- **融资：** 公司于 2025-05-12 宣布，自创立以来累计融资约 180 亿日元。此前 Google、日本郵政キャピタル、NTTドコモ 和 セブン-イレブン・ジャパン 进行了金额未披露的股权投资，商工中金和日本政策金融公库又各提供 10 亿日元长期贷款（[2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html)）。最近一次有名称的轮次是 シリーズC，于 2022-10-06 以 62.6 亿日元完成（[公告](https://prtimes.jp/main/html/rd/p/000000044.000048083.html)）。公司官网 About 页面仍显示 109.8 亿日元，见“备注”。
- **员工人数：** 截至 2026 年 4 月为 220 人（[招聘网站](https://recruit.ubie.life/)；访问于 2026-10-11）。公司官网 About 页面显示截至 2025 年 4 月为 240 人（[About](https://ubie.life/about_ubie)）。
- **工程：** 产品服务使用 TypeScript/Node.js（GraphQL BFF 背后的 NestJS 模块化单体），平台服务使用 Go；Web 端为 React/Next.js，移动端为 React Native；数据库为 AlloyDB 上的 PostgreSQL；运行在 Google Cloud 上的 Kubernetes（[Ubie 技术博客](https://zenn.dev/p/ubie_dev)；[职位](https://herp.careers/v1/ubiehr)）。查阅到的工程职位全部以日语撰写，唯一写明语言要求的职位要求母语级日语，未找到英文工程职位。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | Ubie株式会社（英文社名：Ubie, Inc.）；登记名称为 Ｕｂｉｅ株式会社，读音为“ユビー” | [About](https://ubie.life/about_ubie)；[国税厅法人番号公表网站](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132) |
| 法人番号 | 7010701034132；指定日 2017-05-12；登记记录最后更新于 2024-12-26 | [国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132)；访问于 2026-10-11 |
| 成立 | 2017 年 5 月 | [About](https://ubie.life/about_ubie) |
| 总部（登记地址） | 〒103-0023 東京都中央区日本橋本町三丁目8番4号 日本橋ライフサイエンスビルディング4 5F；自 2024-12-09 起为登记地址 | [About](https://ubie.life/about_ubie)、[国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132) |
| 代表人 | 共同代表取締役 医师 阿部吉倫；共同代表取締役 久保恒太 | [About](https://ubie.life/about_ubie) |
| 列出的其他高管 | 社外取締役 重富隆介；社外監査役 律师 湯浅紀佳 | [公司介绍资料](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)（Speaker Deck 元数据：发布于 2026-05-05，修改于 2026-09-27） |
| 员工人数 | 220 人（截至 2026-04）；240 人（截至 2025-04） | [招聘网站](https://recruit.ubie.life/)、[About](https://ubie.life/about_ubie) |
| 办公地点 | 日本和美国（纽约） | [About](https://ubie.life/about_ubie)、[business.ubiehealth.com](https://business.ubiehealth.com/) |
| 资本金 | 資本金 9,000 万日元 | [HERP 职位中的公司信息栏](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)；无日期，访问于 2026-10-11 |
| 累计融资 | 自创立以来约 180 亿日元 | [2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html) |
| 消费者用户 | 「ユビー」月活用户约 1,300 万 | [2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html) |
| 医疗机构 | ユビーメディカルナビ 导入 1,800 家机构；平台连接 15,000 多家医疗机构 | [About](https://ubie.life/about_ubie)、[Service](https://ubie.life/service)；无日期，访问于 2026-10-11 |
| 制药企业覆盖 | 约九成“全球巨型药企”（定义为年营收超过 100 亿美元）与 Ubie 有业务往来 | [About](https://ubie.life/about_ubie)；无日期，访问于 2026-10-11 |
| 安全与数据处理 | 2020 年 10 月取得 ISMS；公司称系统符合 3省2ガイドライン；服务运行在 Google Cloud Platform 上；公开了漏洞披露政策（VCDP） | [安全管理体制](https://ubie.life/safety/security_management)、[数据保护](https://ubie.life/safety/data_protection)、[VCDP](https://ubie.life/safety/vcdp)；无日期，访问于 2026-10-11 |
| 招聘系统 | HERP（`ubiehr`）；招聘网站列出 47 个职位（产品 5、工程 15、业务 20、公司职能 7） | [招聘网站](https://recruit.ubie.life/)；访问于 2026-10-11 |

**项目与奖项。** Ubie 出自インディージャパン运营的生命科学加速器 ZENTECH DOJO NIHONBASHI 第 4 期（[BRIDGE，2018-05](https://thebridge.jp/2018/05/ubie-jpy300m-funding)）。2020 年入选 JETRO 的“日ASEANにおけるアジアDX促進事業”（[2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html)）；2025 年通过 JETRO 的 HealthTech Gateway “AI Medical in the US”参加了 Mayo Clinic Platform_Accelerate（[2025-09-04](https://prtimes.jp/main/html/rd/p/000000175.000048083.html)）。公司列于 [J-Startup](https://www.j-startup.go.jp/startups/212-ubie.html)，但该页面未注明入选年份。公司公布的奖项：

- AI問診ユビー 获第 3 届日本服务大奖“厚生劳动大臣奖”和“评审特别奖”（[2020-10-27](https://prtimes.jp/main/html/rd/p/000000009.000048083.html)）
- Google Play ベスト オブ 2023“優れた AI 部門”大奖（[2023-11-30](https://prtimes.jp/main/html/rd/p/000000064.000048083.html)）
- 生成AI大賞2024 特別賞和優秀賞（[2024-12-19](https://prtimes.jp/main/html/rd/p/000000117.000048083.html)）
- 日本スタートアップ大賞2026 厚生劳动大臣奖（医療・福祉スタートアップ賞），于 2026-09-25 颁发（[2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html)）

### 公司陈述的背景

- 公司称其 2025 年 8 月自行开展的调查显示，72% 的受访者属于“医療迷子”，即在从察觉症状到接受治疗的某个阶段遇到困难（[2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)）。
- 公司以 2024 年医生工时上限（医師の働き方改革）和 2026 年度診療報酬改定为背景介绍医院产品（[2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)、[2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html)）。
- 在获奖公告中，公司称日本医疗在迈向 2040 年时将面临需求上升与人手减少（[2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html)）。

### 品牌与法律实体

| 名称 | 类型 | 法域／期间 | 来源中所述关系 | 来源 |
|---|---|---|---|---|
| Ubie株式会社（Ubie, Inc.） | 法律实体 | 日本；法人番号指定于 2017-05-12 | 母公司。登记地址从品川区北品川（2017）依次迁至日本橋本町3-11-5（2018-08-17）、日本橋室町1-5-3（2019-03-04）、日本橋堀留町2-4-3（2023-04-24）和日本橋本町3-8-4（2024-12-09） | [国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132) |
| Ubie, Inc. / Ubie Inc.（美国） | 关联实体（子公司） | 纽约州；成立于 2022-10-04 | 被称为美国“現地法人”。成立时代表人为 Naoto Shimazu，2026 年为 Kota Kubo。美国使用条款称其为“Ubie, a company incorporated under the laws of the State of New York” | [2022-12-08](https://prtimes.jp/main/html/rd/p/000000047.000048083.html)、[2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)、[美国条款](https://ubiehealth.com/terms)（最后更新 2023-10-30） |
| 新加坡实体（名称未披露） | 关联实体 | 新加坡；不晚于 2020-10-15 成立 | 公告称其为 Ubie 首家海外公司。现公司官网只列出日本和美国办公地点，未说明该实体现状 | [2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html)、[About](https://ubie.life/about_ubie) |
| Dr. Ubie | 曾用产品 | 印度；2018 年测试上线 | 面向消费者的 Web 问诊服务，测试营销约半年后中止 | [2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html) |

日本母公司的英文名与美国子公司名称都是“Ubie, Inc.”，各来源中有时带逗号，有时不带。通过 PR Newswire 发布的美国公告署名为“SOURCE Ubie, Inc.”，未说明由哪个实体发布。

---

## 产品

### 产品阵容

| 产品 | 面向对象 | 内容 | 来源 |
|---|---|---|---|
| 「ユビー」（症状检索引擎，2020 年 4 月以“AI受診相談ユビー”上线；2025-09-16 增加“医療AIパートナー”） | 日本消费者 | 免费 App 和 Web 服务。症状检索会提出约 20 个经医师监修的问题，并给出相关疾病、自我处理信息和附近医疗机构。自 2025-09-16 起，还提供对话式指引：会记住用户情况，并可使用マイナポータル 中的处方和就诊记录 | [2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)、[2024-10-01](https://prtimes.jp/main/html/rd/p/000000105.000048083.html)、[ubie.app 条款](https://ubie.app/terms) |
| ユビーAI問診 | 医院和诊所 | 用于就诊前和院内的 AI 问诊。问题会根据患者回答分支，以“医師語”生成病历草稿，并可与电子病历联动。自 2018 年起提供 | [产品页](https://intro.dr-ubie.com/products/aimon)、[2022-07-27](https://prtimes.jp/main/html/rd/p/000000039.000048083.html) |
| ユビー生成AI（2024-05-02 以“ユビーメディカルナビ 生成AI”名义推出 β 版） | 医院 | 面向医院职员的多模型生成式 AI：文本生成与摘要、语音识别、图像识别和 RAG。在各医院独立环境中运行，并关闭对客户数据的训练；可与电子病历联动，也可在移动设备上使用 | [2024-05-02](https://prtimes.jp/main/html/rd/p/000000076.000048083.html)、[2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html)、[产品页](https://intro.dr-ubie.com/products/generativeai_lp) |
| ユビーDPCサポーター | 医院 | 根据病历和医嘱数据建议 DPC 编码 | [产品页](https://intro.dr-ubie.com/products/dpc-supporter)、[2025-12-04](https://prtimes.jp/main/html/rd/p/000000191.000048083.html) |
| ユビーリンク／ホームページAI相談窓口 | 诊所和医院 | 在「ユビー」中免费刊登医疗机构，并为机构自有网站提供症状检查横幅（ユビーリンク 于 2021-07-27 推出） | [产品一览](https://intro.dr-ubie.com/products)、[2021-07-27](https://prtimes.jp/main/html/rd/p/000000022.000048083.html) |
| ユビー for Pharma／ユビーAds | 制药企业 | 通过平台向消费者和医疗机构传递疾病与治疗认知信息，另有一款面向医疗健康的定向广告产品 | [ph-ubie.com](https://ph-ubie.com/)、[ユビーAds](https://ph-ubie.com/ubie_ads)、[Service](https://ubie.life/service) |
| Ubie Symptom Checker（美国） | 美国消费者 | 英文症状检查服务，于 2022-04-26 推出：从约 3,500 类问题中提出约 20 个问题，覆盖 1,100 多种疾病 | [美国公告，2022-04-26](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us) |
| Ubie Smart Support（美国） | 美国诊所和医疗系统 | AI 电话与聊天代理，接听未接来电和非工作时间来电、预约挂号，并把电话转交给工作人员 | [产品页](https://business.ubiehealth.com/provider/smart-support)、[2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html) |
| Ubie Self-Serve（美国） | 美国广告主 | 自助广告，可在 Ubie 的患者体验中按症状、疾病预测和专科兴趣进行定向 | [PR Newswire，2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html) |

公司称其核心资产是一个问诊引擎，基于国内外 5 万篇医学论文、在 50 多名医师监修下构建（[Service](https://ubie.life/service)；无日期，访问于 2026-10-11）。

### 商业化

- **消费者服务**免费。AI 伙伴的发布公告写明“利用料金：無料”（[2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)）。
- **ユビーAI問診**的价格由年度许可费、平板（iPad）费用和电子病历联动所需的网络费用构成，具体金额只能通过下载表单获取（[价格页](https://intro.dr-ubie.com/products/pricing)；访问于 2026-10-11）。ユビー生成AI 推出时采用“個別見積り”（单独报价）（[2024-05-02](https://prtimes.jp/main/html/rd/p/000000076.000048083.html)）。公司在 [2024-07-08](https://prtimes.jp/main/html/rd/p/000000091.000048083.html)、[2025-03-21](https://prtimes.jp/main/html/rd/p/000000136.000048083.html) 和 [2025-11-28](https://prtimes.jp/main/html/rd/p/000000190.000048083.html) 公布了配合厚生劳动省和东京都补贴项目的套餐。
- **制药业务**收入来自疾病认知项目和营销解决方案，未找到公开价目表。在美国，Self-Serve 广告公布了每日最低金额（[2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html)），面向诊所的 Smart Support 公布了固定月费（[产品页](https://business.ubiehealth.com/provider/smart-support)；访问于 2026-10-11）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2021-05-21 | AI問診ユビー 已在 47 个都道府县的 400 多家机构导入 | [公告](https://prtimes.jp/main/html/rd/p/000000020.000048083.html) |
| 2021-06-08 | AI受診相談ユビー 上线一年后月活用户超过 100 万 | [公告](https://prtimes.jp/main/html/rd/p/000000021.000048083.html) |
| 2022-07-25 | ユビーAI問診 导入机构超过 1,000 家 | [公告](https://prtimes.jp/main/html/rd/p/000000038.000048083.html) |
| 2022-09-07 | ユビーリンク 导入机构超过 15,000 家 | [公告](https://prtimes.jp/main/html/rd/p/000000043.000048083.html) |
| 2024-04-12 | 「ユビー」与“ユビー病気のQ&A”合计月活约 1,000 万；ユビーメディカルナビ 导入 1,700 多家机构；与超过三分之二的全球巨型药企有业务往来 | [公告](https://prtimes.jp/main/html/rd/p/000000073.000048083.html) |
| 2025-03-06 | 月活约 1,200 万；1,800 多家机构 | [公告](https://prtimes.jp/main/html/rd/p/000000128.000048083.html) |
| 2025-06-26 | 美国症状检查服务累计用户超过 400 万；全球月活超过 1,300 万；营销解决方案被前 30 大生命科学公司中的 21 家使用 | [PR Newswire](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html) |
| 2026-01 | ユビー生成AI 已在 100 家医院导入，其中包括 10 多家大学医院；每月超过 10 万次会话；已登记 8,000 多个用例模板 | [2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html) |
| 2026-06-03 | 美国月活约 600 万；全球月活超过 2,000 万 | [PR Newswire](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html) |
| 2026-09-28 | 月活约 1,300 万；ユビー生成AI 在 160 多家大型医院使用，其中包括 20 多家大学医院 | [公告](https://prtimes.jp/main/html/rd/p/000000227.000048083.html) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2020-06-04](https://prtimes.jp/main/html/rd/p/000000005.000048083.html) | スズケン | 投资 20 亿日元，并通过其 240 家分店共同销售 |
| [2021-04-21](https://prtimes.jp/main/html/rd/p/000000019.000048083.html) | 武田薬品 | 合作推动罕见病早期发现，并于 [2023-04-10 签署综合合作协议](https://prtimes.jp/main/html/rd/p/000000052.000048083.html)予以扩展。公司公布的其他制药合作包括辉瑞（[2021-10-15](https://prtimes.jp/main/html/rd/p/000000024.000048083.html)）、拜耳（[2021-11-24](https://prtimes.jp/main/html/rd/p/000000026.000048083.html)）和勃林格殷格翰（[2022-02-02](https://prtimes.jp/main/html/rd/p/000000031.000048083.html)） |
| [2023-03-13](https://prtimes.jp/main/html/rd/p/000000050.000048083.html) | ファイザー | 合作开展 OAB 疾病认知，公司称促成约 17,000 人前往医疗机构就诊 |
| [2024-09-30](https://prtimes.jp/main/html/rd/p/000000104.000048083.html) | シミックホールディングス | 业务合作，覆盖 CRO、SMO 和 CSO 业务 |
| [2024-10-08](https://prtimes.jp/main/html/rd/p/000000107.000048083.html) | Google | 投资，并约定合作推进日本医疗系统 DX，包括生成式 AI |
| [2025-03-27](https://prtimes.jp/main/html/rd/p/000000138.000048083.html) | NTTドコモ | 资本业务合作：d 账户登录与数据联动，并共同开展制药营销 |
| [2025-03-31](https://prtimes.jp/main/html/rd/p/000000139.000048083.html) | セブン-イレブン・ジャパン | 资本业务合作；首个试点是在症状检索结果中链接 7NOW 配送 |
| [2025-12-08](https://prtimes.jp/main/html/rd/p/000000192.000048083.html) | Medable（美国） | 就日本分散式临床试验建立战略合作 |
| [2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html) | Mayo Clinic（美国） | Ubie Inc. 开始共同开发 Ubie Smart Support；Mayo Clinic 对该技术拥有经济利益 |
| [2026-08-21](https://prtimes.jp/main/html/rd/p/000000224.000048083.html) | NeoX | 通过 Reserve with Google 提供药局预约，首批覆盖东京、神奈川、千叶约 300 家药局 |
| [2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html) | 金沢医科大学病院 | 自 2026 年 10 月起在电子病历环境中全面使用 ユビー生成AI |

2025–2026 年的新闻稿中有很大一部分是单家医院的案例。例如九州大学病院预计借助 ユビーDPCサポーター 每年改善收益 6,500 万日元以上（[2025-12-04](https://prtimes.jp/main/html/rd/p/000000191.000048083.html)），北里大学病院决定导入 ユビー生成AI（[2026-09-16](https://prtimes.jp/main/html/rd/p/000000226.000048083.html)）。

### 公开计划

- **ユビー生成AI：** 计划推出ベッドコントロール（床位管理）功能（[2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)）。
- **Ubie Smart Support：** Ubie 与 Mayo Clinic 计划开发慢性病管理附加模块（[2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)）。
- **2024 年资金用途：** 制药业务的开发与增长、消费者功能、新业务，以及「ユビー」的营销（[2024-04-12](https://prtimes.jp/main/html/rd/p/000000073.000048083.html)）。
- **2025 年合作方向：** 公司称将把 Google、日本郵政グループ、NTTドコモ 和 セブン-イレブン 的技术与全国网络同自身能力结合（[2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html)）。

---

## 创始人

**阿部吉倫（Yoshinori Abe）**，医师，联合创始人、共同代表取締役（[About](https://ubie.life/about_ubie)）。

- 2015 年毕业于东京大学医学部，随后在东京大学医学部附属医院和东京都健康长寿医疗中心完成初期研修。
- 因遇到一名忽视便血、48 岁去世的患者而转向数据科学。
- 2017 年 5 月联合创立 Ubie。
- 自 2019 年 12 月起任日本急救医学会急救 AI 研究活性化特别委员会委员。
- 2020 年入选 Forbes 30 Under 30 Asia（Healthcare & Science）。
- 自 2023 年起任日本医疗创投协会（JMVA）理事。

**久保恒太（Kota Kubo）**，工程师，联合创始人、共同代表取締役（[About](https://ubie.life/about_ubie)）。

- 毕业于东京大学研究生院工学系研究科。
- 2013 年在校期间开始研究和开发模拟医生“症状—疾病”关联的软件与算法。
- 曾在エムスリー工作约三年，从事医生问答服务等 B2C 医疗软件开发及网络营销。
- 2017 年联合创立 Ubie。
- 被称为“共同代表取締役 兼 Ubie US CEO”，也是 Ubie Inc. 的代表人（[2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)）。

### 主要管理层

| 姓名 | 所列职位 | 来源 |
|---|---|---|
| Yuku Kotani | “Ubie, Inc. CTO”（其 Zenn 个人简介中的自述）。2025-06-16 的公司技术博客文章称其为 VP of Technology | [Zenn 个人页](https://zenn.dev/yuku)（访问于 2026-10-11）、[技术博客文章](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) |
| 西田（名未披露） | CFO | [新闻索引](https://ubie.life/news)，2026-06-26 条目 |
| 風間正弘 | Chief AI Officer（CAIO） | [新闻索引](https://ubie.life/news)，2026-01-16 和 2026-03-05 条目 |
| 井上真夢 | アクセラレーター本部代表・政策渉外参事 | [新闻索引](https://ubie.life/news)，2026-01-16 条目 |
| 西村里穂 | 医療機関事業本部長（招聘网站显示 2018 年入职） | [2026-08-07](https://prtimes.jp/main/html/rd/p/000000223.000048083.html)、[招聘网站](https://recruit.ubie.life/) |
| 重富隆介 | 自 2022-10 起任社外取締役；就任时为ブラックストーン・グループ・ジャパン代表取締役会長 | [2022-10-06](https://prtimes.jp/main/html/rd/p/000000044.000048083.html)、[公司介绍资料](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211) |
| 吉川和美 | 自 2022-10 起任常勤監査役（注册会计师）；2026 年公司介绍资料未列出 | [2022-10-06](https://prtimes.jp/main/html/rd/p/000000044.000048083.html) |

工程职位写明由 CTO 负责工程愿景和技术战略，并招聘与 CTO 合作的 VP of Engineering、Head of Platform Engineering 和工程经理（[EM 职位](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)、[VPoE 职位](https://herp.careers/v1/ubiehr/x3F1XHsBBT_L)）。

招聘网站列出以下组织（[事业部介绍](https://recruit.ubie.life/division-Introduction)；访问于 2026-10-11）：

- ファーマイノベーション事業本部（制药）
- 病院事業本部（医院）
- クリニック/薬局事業本部（诊所和药局）
- Global事業本部，以纽约为据点
- プロダクトプラットフォーム本部，负责所有事业部的产品开发
- テクノロジープラットフォーム本部（技术平台）
- アクセラレーター本部，涵盖合作、政策、财务、风险、HR 和公司职能
- 生成AI推進室，直属经营层

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2017-09 | 种子轮（BRIDGE 报道；无公司公告） | 6,000 万日元 | D4V | — | [BRIDGE，2018-05](https://thebridge.jp/2018/05/ubie-jpy300m-funding) |
| 2018-05-07 | 未注明（J-KISS） | 未披露；BRIDGE 推测为 3 亿日元，并称之为 A 轮 | 関電ベンチャーマネジメント | — | [BRIDGE，2018-05](https://thebridge.jp/2018/05/ubie-jpy300m-funding) |
| 2020-06-04 | 資金調達（未命名轮次） | 约 20 亿日元 | スズケン | — | [公告](https://prtimes.jp/main/html/rd/p/000000005.000048083.html) |
| 2021-04 | 累计金额更新（非轮次） | — | — | 44.8 亿日元 | [Ubie note](https://note.com/ubie/n/n08baa940b694) |
| 2022-07-27 | シリーズC ファーストクローズ | 35 亿日元 | 新增：農林中金キャピタル、NVenture Capital、第一生命保険、エッグフォワード 等；原有：スズケン | 79.8 亿日元 | [公告](https://prtimes.jp/main/html/rd/p/000000039.000048083.html) |
| 2022-10-06 | シリーズC（完成） | 追加 27.6 亿日元；本轮合计 62.6 亿日元 | 股权：総合メディカル、AAIC Investment Pte. Ltd.、日本インパクト投資2号投資事業有限責任組合、楽天キャピタル；贷款：商工組合中央金庫、日本政策金融公庫、みずほ銀行 | 107.2 亿日元（累計資本調達額） | [公告](https://prtimes.jp/main/html/rd/p/000000044.000048083.html) |
| 2024-04-12 | インパクトファイナンス（股权加贷款） | 约 35 亿日元 | 股权：三井住友信託銀行（作为影响力投资）、JA三井リース 等；贷款额度：三井住友信託銀行、三菱UFJ銀行、みずほ銀行 | 未说明 | [公告](https://prtimes.jp/main/html/rd/p/000000073.000048083.html) |
| 2024-10-08 | 最新の資金調達ラウンド（未命名） | 未披露 | Google | 未说明 | [公告](https://prtimes.jp/main/html/rd/p/000000107.000048083.html) |
| 2025-03-06 | 第三者割当増資 | 未披露 | 日本郵政キャピタル | 未说明 | [公告](https://prtimes.jp/main/html/rd/p/000000128.000048083.html) |
| 2025-03-27 | 資本業務提携 | 未披露 | NTTドコモ | 未说明 | [公告](https://prtimes.jp/main/html/rd/p/000000138.000048083.html) |
| 2025-03-31 | 資本業務提携（第三者割当増資） | 未披露 | セブン-イレブン・ジャパン | 未说明 | [公告](https://prtimes.jp/main/html/rd/p/000000139.000048083.html) |
| 2025-05-07 | 長期融資 | 10 亿日元 | 商工組合中央金庫 | 未说明 | [公告](https://prtimes.jp/main/html/rd/p/000000148.000048083.html) |
| 2025-05-08 | 長期融資（スタートアップ支援資金） | 10 亿日元 | 日本政策金融公庫 | 约 180 亿日元（2025-05-12 公布） | [公告](https://prtimes.jp/main/html/rd/p/000000149.000048083.html)、[2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html) |

关于上表：

- Ubie 自己的公告只命名了一个轮次，即 シリーズC。2020 年スズケン公告未命名轮次；Ubie 自己的 [note](https://note.com/ubie/n/n08baa940b694) 中列出的 MobiHealthNews 标题称之为 1,870 万美元的“Series B”。
- BRIDGE 援引スズケン的披露称，这笔投资使スズケン持有约 10% 的已发行股份（[BRIDGE，2020-06](https://thebridge.jp/2020/06/ubie-jpy2b-funding)）。
- 2022-07-27，即 シリーズC 首次交割同日，中部電力 作为业务合作的一部分也认购了第三方配售股份，金额未说明（[公告](https://prtimes.jp/main/html/rd/p/000000040.000048083.html)）。
- シリーズC 完成（2022-10）和 2024 年融资都混合了股权与银行贷款，公告标题金额将两者合计。
- 累计金额从 107.2 亿日元（2022-10）增至约 180 亿日元（2025-05），但期间公告只披露了 2024-04 融资（约 35 亿日元）和 2025 年两笔贷款（各 10 亿日元）的金额。
- 在面向美国的公告中，Ubie 称累计融资“over $125M”（[2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)）。

---

## 工程

### 技术栈与平台

除另有说明外，以下内容由公司技术博客和公开仓库证实。

- **后端。** Yuku Kotani 于 2022 年 12 月发文宣布全公司决定：新开发统一为两种语言，产品服务用 Node.js，共享平台服务用 Go。同一决定为面向前端的服务选用 GraphQL，服务间通信选用 gRPC（[Zenn，2022-12-14](https://zenn.dev/yuku/articles/4437cde02a672b)）。当时 Kotlin、Go、Node.js、Ruby 和 Python 服务都在运行，现有的 Server-Side Kotlin 服务不会仅因技术栈调整而重写。之后的文章描述了：
  - BFF 是用 NestJS 模块化单体加 Prisma 构建的 GraphQL 服务器（[Zenn，2025-03-13](https://zenn.dev/nissy_dev/articles/nestjs-prisma-db-access-management)）；
  - 一个 Kotlin 个性化功能正被 Go 服务替换（[Zenn，2025-06-16](https://zenn.dev/glassmonkey/articles/7f393a44ffb029)）。
  
  2026 年的一个职位称，面向用户的服务以 Node.js 模块化单体为中心，认证授权和 PHR 平台使用 Go（[职位](https://herp.careers/v1/ubiehr/sqYyDunoCtcf)）。
- **Web 与移动端。** Web 端使用 React 与 Next.js，前端使用 Apollo Client（[Zenn，2022-12-14](https://zenn.dev/yuku/articles/4437cde02a672b)）。移动 App 于 2024 年初从 Ionic（Capacitor）迁移到 React Native（Expo）（[Zenn，2024-11-18](https://zenn.dev/yuku/articles/46cf443d5dd25b)）。
- **数据存储。** PostgreSQL，已从 Cloud SQL 迁移到 AlloyDB（[Zenn，2025-02-05](https://zenn.dev/electricalsheep/articles/cf1d74b65ec64b)）。公开仓库中还有 Cloud Spanner 和 Elasticsearch 相关工具（`spanner-kase`、`esqa`）（[GitHub](https://github.com/ubie-oss)）。
- **基础设施。** Google Cloud Platform（[数据保护](https://ubie.life/safety/data_protection)），多集群 Kubernetes、Terraform，以及取代 Argo Workflows 的 Cloud Workflows（[Zenn，2025-02-05](https://zenn.dev/electricalsheep/articles/cf1d74b65ec64b)）。SRE 职位还提到边缘层的 CDN/WAF、带 Istio（Envoy）服务网格的 Kubernetes 和托管数据库，全部由一个小型平台团队负责（[职位](https://herp.careers/v1/ubiehr/QzoglruZi_M1)）。
- **数据与分析。** BigQuery 和 dbt；BI 工具为 Lightdash，公司为其公开了 Terraform provider 和 pre-commit hooks（[GitHub](https://github.com/ubie-oss)；[分析职位](https://herp.careers/v1/ubiehr/Bilnrfg8U7vj)）。
- **内部生成式 AI。** 自研工具可调用 Gemini、GPT 和 Claude 模型，截至 2026 年 6 月有 85% 的员工每周使用。公司签约的工具包括 Notion AI、NotebookLM、GitHub Copilot、Devin、Cursor、Azure OpenAI、Dify、Perplexity、v0 和 Claude Code（[生成式 AI 页面](https://recruit.ubie.life/generative-ai)）。内部 AI 服务使用 Next.js/TypeScript、AlloyDB for PostgreSQL、LangChain/LangGraph、Go 和 Python 构建（[Corporate AI Engineer 职位](https://herp.careers/v1/ubiehr/_oeH0lYReImI)）。
- **仅见于招聘要求：**
  - C#/.NET、MSI 安装包和 Windows 系统编程，用于院内客户端（[职位](https://herp.careers/v1/ubiehr/QC24-tv1B1S8)）；
  - 使用 LLM API 的 Python、TypeScript 或 Go，以及 Elasticsearch 和向量检索（[AI/ML 职位](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv)）；
  - OAuth2/OIDC、SAML 和 Auth0/Okta/Keycloak（[认证职位](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58)）；
  - Honeycomb、Datadog 和 OpenTelemetry，属于优先项（[SRE 职位](https://herp.careers/v1/ubiehr/QzoglruZi_M1)）。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 问诊引擎 | AI 根据患者主诉和回答选择后续问题，支撑消费者症状检索、ユビーAI問診 和美国症状检查服务 | [产品页](https://intro.dr-ubie.com/products/aimon)、[美国公告](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us) |
| AI 伙伴 | 带每位用户记忆和マイナポータル数据联动的对话式指引。参考信息限于公共机构和专业网站，由包括医师在内的团队监控 | [2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html) |
| 医院生成式 AI 平台 | 在隔离的各医院环境中提供文本、语音、图像和 RAG 功能，支持电子病历联动和移动端访问。医院自行建立模板和工作流：8,000 多个模板（2026-01），每家医院平均运行 100 多个工作流（2026-08） | [2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)、[2026-08-07](https://prtimes.jp/main/html/rd/p/000000223.000048083.html) |
| 医院数据联动客户端 | 部署在医院网络内的 Windows 客户端，监控目录并把数据发送到 Ubie 云端；须适应本地部署、代理、VPN 和封闭网络连接 | [职位](https://herp.careers/v1/ubiehr/QC24-tv1B1S8) |
| 身份平台 | 消费者、患者和医护人员的 ID 管理：MFA、多租户、SSO/SAML、消费者与 B2B 产品间的 ID 联动，以及向 AI 代理委派权限 | [职位](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58) |
| 个性化中枢 | 一个 Go 服务，根据用户在各产品中的状态建议下一步行动；它取代了一个与制药项目管理系统绑定的 Kotlin 功能 | [Zenn，2025-06-16](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) |
| LLM 平台运维 | 围绕模型单价、每分钟 token 限额和延迟做容量规划；FinOps（承诺使用折扣、spot 实例、成本分摊）；按日本和美国监管要求分别构建基础设施；内部“Infra Agent”承担部分调查和成本分析工作 | [SRE 职位](https://herp.careers/v1/ubiehr/QzoglruZi_M1) |
| 安全分析代理 | 用于安全告警分析的 AI 代理，已运行约一年 | [Zenn，2026-03-31](https://zenn.dev/mizutani/articles/ai-sec-alert-ops) |

公司在 Zenn 上以 publication“Ubie テックブログ”运营技术博客，2020-12-18 至 2026-07-31 共有 186 篇文章（[Zenn](https://zenn.dev/p/ubie_dev)；统计于 2026-10-11）。招聘网站在 connpass 上列出其活动（[生成式 AI 页面](https://recruit.ubie.life/generative-ai)）。GitHub 组织 `ubie-oss`（名称“Ubie, Inc.”，创建于 2021-11-19）有 51 个公开仓库，其中 34 个不是 fork，包括：

- `slack-mcp-server`，星标最多，有 110 颗；
- `kotlin-graphql-sample`；
- `n8n-cli`；
- 设计系统包（`ubie-ui`、`design-tokens`、`ubie-icons`）和 Ubie Vitals 网站；
- `nslog`，一个面向 NestJS 的结构化日志库；
- `dbt-data-privacy`（[GitHub](https://github.com/ubie-oss)；访问于 2026-10-11）。

### 招聘所需技术背景

当前工程职位的必需项（[HERP](https://herp.careers/v1/ubiehr)；访问于 2026-10-11）：

- **产品工程师：** 以某项核心专长为支点，从发现问题到交付和改进端到端创造价值，并能快速深入专业领域（[职位](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)）。
- **产品平台工程师：** React/TypeScript 前端，或 Node.js/TypeScript、Go 后端开发经验，以及主导技术选型或设计的经验（[职位](https://herp.careers/v1/ubiehr/sqYyDunoCtcf)）。
- **AI/ML 工程师：** 生产级 Web 应用、生产级 AI/ML 功能，以及用 Python、TypeScript 或 Go 构建 LLM API 系统的经验；另须具备 RAG 或 agentic search、或 AI/ML 系统评估经验之一（[职位](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv)）。
- **高级 SRE：** 生产环境 Kubernetes 的设计与改进（仅做一线监控不算）、Terraform 等 IaC、Google Cloud 或 AWS 生产运维，以及 Linux 和网络故障排查（[职位](https://herp.careers/v1/ubiehr/QzoglruZi_M1)）。
- **Windows 应用工程师：** C#/.NET 桌面应用、文件系统监控、网络编程、安装包，以及 API 或文件集成（[职位](https://herp.careers/v1/ubiehr/QC24-tv1B1S8)）。
- **工程经理：** 能把组织变革推进到底；明确不要求初创公司经验（[职位](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)）。

优先项包括：

- 借助生成式 AI 的开发；
- Next.js 和 GraphQL API 设计；
- PostgreSQL；
- 服务网格（Envoy/Istio）；
- 云成本优化；
- SLO、错误预算和事后复盘实践；
- LLM 产品运维；
- 带持久记忆的 AI 代理；
- 语音识别；
- 受监管行业的基础设施。

### 行业领域

相关工作涉及日本医疗和美国诊所运营的多个领域：

- **医院 IT：** 电子病历和部門システム、医院封闭网络、HL7/FHIR、SS-MIX2、DICOM 和レセコン（[Windows 职位](https://herp.careers/v1/ubiehr/QC24-tv1B1S8)）。
- **安全指引：** 3省2ガイドライン（[认证职位](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58)；[数据保护](https://ubie.life/safety/data_protection)）。
- **医院支付与运营：** DPC/PDPS 编码和診療報酬改定（[DPC 页面](https://intro.dr-ubie.com/products/dpc-supporter)）。
- **消费者健康数据：** PHR，以及消费者 App 使用的マイナポータル联动（[2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html)）。
- **制药与临床试验：** 制药企业疾病认知工作和临床试验（CRO、SMO、DCT）（[2024-09-30](https://prtimes.jp/main/html/rd/p/000000104.000048083.html)、[2025-12-08](https://prtimes.jp/main/html/rd/p/000000192.000048083.html)）。
- **各国监管：** SRE 职位指出日本和美国的医疗监管不同（[职位](https://herp.careers/v1/ubiehr/QzoglruZi_M1)）。

职位中的领域背景一般属于优先而非必需：

- 医疗信息系统经验和医療情報技師资格（AI/ML）。
- 医院系统知识（Windows）。
- 医疗、健康科技或制药经验（产品岗位）。

产品工程师职位要求有深入医学和生命科学的意愿。部分 Scrum 团队有医师作为领域专家参与（[公司介绍资料](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 查阅到的 HERP 工程职位全部以日语撰写；只有 Product Security Engineer 职位写明语言要求：“日本語（ネイティブレベル）”。美国公司页面称全职岗位已满 | [安全职位](https://herp.careers/v1/ubiehr/cQ6vihXLiMLg)、[business.ubiehealth.com](https://business.ubiehealth.com/)；访问于 2026-10-11 |
| 远程与到岗 | FAQ：除部分销售岗外，员工自行决定工作地点；只要能约每月到岗一次即可完全远程。各职位不同：每周两天必须到岗（SRE、安全），建议每周到岗两天（AI/ML、平台、分析、Windows），或仅在需要时到岗，例如月度业务汇报和季度团建（产品工程师、VPoE） | [FAQ](https://recruit.ubie.life/faq)、[SRE](https://herp.careers/v1/ubiehr/QzoglruZi_M1)、[AI/ML](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv)、[产品工程师](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) |
| 工时制度 | 弹性工时或裁量劳动制，无核心时间（合同工除外）。多数工程职位采用専門業務型裁量労働制，视为每天工作 9.5 小时。产品工程师职位采用完全弹性工时，基本时间 10:00–19:00，平均每月加班 20–30 小时 | [工作环境](https://recruit.ubie.life/work-environment)、[职位](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) |
| 薪资（公开区间） | 800 万–1,500 万日元：平台、认证、SRE、分析、公司内部 AI。1,000 万–1,500 万日元：AI/ML。1,000 万日元起：产品工程师。1,000 万–1,800 万日元：EM。1,000 万–2,000 万日元：Head of Platform。1,200 万–2,500 万日元：VPoE。600 万–1,200 万日元：Windows、网络。最高约 2,000 万日元：安全岗位。实习 2,000 日元／小时。薪资包含 45 小时固定加班费 | [HERP](https://herp.careers/v1/ubiehr)；访问于 2026-10-11 |
| 雇佣类型 | General Employee（総合職）和 Expert（職務限定／岗位型） | [职位](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv) |
| 股权 | 自 2023 年 4 月起为全体正式员工提供税制适格股票期权“U-win”，离职后仍可保留并行权；法定产假（14 周）计入归属期 | [2023-04-07](https://prtimes.jp/main/html/rd/p/000000051.000048083.html)、[工作环境](https://recruit.ubie.life/work-environment) |
| 休假与试用 | 每年休息日 125 天（工作环境页面）或 120 天（职位）；入职即授予带薪年假；试用期 6 个月 | [工作环境](https://recruit.ubie.life/work-environment)、[职位](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) |
| 福利 | 保姆补贴、公司内医师咨询、自选设备、学习和购书费用、流感疫苗、允许副业、関東ITソフトウェア健康保険組合 | [工作环境](https://recruit.ubie.life/work-environment) |
| 应届生与初级人员 | 不区分应届和社招；在读大学生以相同条件作为正式员工工作；招聘网站列有软件工程实习 | [FAQ](https://recruit.ubie.life/faq)、[实习职位](https://herp.careers/v1/ubiehr/9QxaWhCu--oj) |
| 组织 | 采用 Holacracy，以角色取代管理职；产品团队普遍使用 Scrum；员工平均年龄 36.5 岁；约一半成员在养育子女 | [公司介绍资料](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)、[business.ubiehealth.com](https://business.ubiehealth.com/)、[FAQ](https://recruit.ubie.life/faq) |
| 签证支持 | 查阅到的职位未说明 | [HERP](https://herp.careers/v1/ubiehr) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）。检索名称：Ubie、Ubie株式会社、ユビー、Ubie Inc.、ubiehealth，以及产品名（ユビーAI問診、ユビーメディカルナビ、ユビー生成AI、AI受診相談ユビー），使用日文和英文。官方来源：ubie.life（sitemap、About、Service、News、安全相关页面）、recruit.ubie.life（sitemap 中的页面和 FAQ）、HERP 职位板、intro.dr-ubie.com、ph-ubie.com、ubie.app 条款，以及 ubiehealth.com／business.ubiehealth.com。新闻：PR TIMES 公司页（198 篇公告，2019-09-24 至 2026-10-09）、PR Newswire 和 BRIDGE。开源：Zenn publication、Speaker Deck，以及 GitHub 组织 `ubie-oss`、`ubie-inc` 和 `ubieinc`（`ubie` 和 `ubiehealth` 返回 404）。登记与名录：国税厅法人番号公表网站、J-Startup 和 Japan Dev；TokyoDev 返回 HTTP 403。

- **营收与利润。** 查阅的公告、公司页面和招聘资料中均未找到相关数字；未查阅官報上的決算公告。
- **2024–2025 年股权投资的金额**（Google、日本郵政キャピタル、NTTドコモ 和 セブン-イレブン・ジャパン），以及这些投资所属轮次的名称。
- **CTO 任命。** 没有任何公告或公司页面写出 CTO 姓名；唯一找到的是 Yuku Kotani 在 Zenn 上的自述。
- **医疗器械状态。** 查阅到的 Ubie 资料均未称任何产品已根据薬機法／PMDA 取得“医療機器プログラム”的批准或认证。消费者条款称该服务提供一般参考信息，不提供诊断或治疗（[ubie.app 条款](https://ubie.app/terms)，最后修订于 2026-03-31）。
- **ISMS 细节。** 公司页面未写明证书编号、认证机构和认证范围。ISMS-AC 登记库的检索需要提交表单，因此未检索。
- **工程人员人数**，以及日本和美国之间的人员分布。
- **新加坡实体**的法定名称和现状。
- **价目表。** 医院和制药产品均未公开价目表；医院产品价格只能通过下载表单获取。

### 不同来源之间的不一致

- **累计融资：** 109.8 亿日元（[About](https://ubie.life/about_ubie)；无日期，访问于 2026-10-11）；约 180 亿日元（[2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html)；[HERP 公司信息栏](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)同样如此）；“over $125M”（[PR Newswire，2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)）。About 页面的数字接近 2022-10 シリーズC 完成时所称的 107.2 亿日元。
- **员工人数：** 截至 2025-04 为 240 人（[About](https://ubie.life/about_ubie)）；截至 2026-04 为 220 人（[招聘网站](https://recruit.ubie.life/)、[资料](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)、[HERP](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)）；“an organization of 200 members”（[business.ubiehealth.com](https://business.ubiehealth.com/)；无日期）。2026 年资料在计算育儿比例时仍以 240 人为基数。
- **医疗机构数量：** ユビーメディカルナビ 导入 1,800 家机构（[About](https://ubie.life/about_ubie)）；“1700以上の医療機関”的反馈和与“15,000件以上の医療機関”连接（[Service](https://ubie.life/service)）；病院事業本部服务“5000を超える医療機関”（[事业部介绍](https://recruit.ubie.life/division-Introduction)）。各页面均未定义统计口径。
- **制药企业覆盖：** 约九成全球巨型药企（[About](https://ubie.life/about_ubie)）；超过三分之二（[事业部介绍](https://recruit.ubie.life/division-Introduction)；截至 [2025-05](https://prtimes.jp/main/html/rd/p/000000149.000048083.html) 的公告同样如此）；超过八成大型制药企业（2026 年[职位](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)）；前 30 大生命科学公司中的 21 家（[2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)）；“50%+ Mega-Pharma Partnerships”（[business.ubiehealth.com](https://business.ubiehealth.com/)）。
- **美国地址：** 1460 Broadway, New York, NY 10036（[2022-12-08](https://prtimes.jp/main/html/rd/p/000000047.000048083.html)、[2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html)）；379 W Broadway, 2nd Floor, New York, NY 10012（[business.ubiehealth.com](https://business.ubiehealth.com/)、[资料](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)）；379 W Broadway, New York, NY 10036（[HERP](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)）。
- **美国业务开始时间：** 一份日期为 2022-04-26 的美国公告宣布美国症状检查服务上线（[公告](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us)）；同一新闻室 2023-12-04 的公告则称美国业务始于 2022 年 10 月（[公告](https://business.ubiehealth.com/newsroom/ubie-used-by-2-million-americans-in-first-year)），与美国实体 2022-10-04 的成立日期一致。
- **远程政策：** [FAQ](https://recruit.ubie.life/faq) 和[工作环境页面](https://recruit.ubie.life/work-environment)称可以完全远程；但多个 2026 年职位要求每周两天必须到岗（[SRE](https://herp.careers/v1/ubiehr/QzoglruZi_M1)），或将每周两天到岗描述为常态（[EM](https://herp.careers/v1/ubiehr/9QuHU73KCC2P)）。
- **年休息日：** 125 天（[工作环境](https://recruit.ubie.life/work-environment)）与 120 天（[职位](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd)）。
- **评估所用 Mayo Clinic 数据：** “3 million Mayo Clinic patients”的去标识化数据（[2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)）与“1千万人以上”（[2025-09-04](https://prtimes.jp/main/html/rd/p/000000175.000048083.html)）。
- **Japan Dev 上的工程语言和办公地点：** [Japan Dev 公司页](https://japan-dev.com/companies/ubie)（无日期；标注未经核实；无开放职位）称工程师不需要日语，标有签证支持，并列出东京和新加坡办公室。而当前职位只有日文，其中一个要求母语级日语，公司官网列出的是日本和美国办公地点。
- **英文高管头衔：** 2022-04-26 的美国公告称阿部为“Co-founder and CEO”，同时也称久保为 CEO；之后的美国公告称久保为“Co-Founder and CEO”（2025-06-26）和“co-founder and co-CEO”（2026-06-03）；日文公告则对两人都使用“共同代表取締役”。Kotani 在 [2025-06-16 的文章](https://zenn.dev/glassmonkey/articles/7f393a44ffb029)中被称为 VP of Technology，而其 [Zenn 个人页](https://zenn.dev/yuku)写的是 CTO。

### 其他

- **使命表述。** 2026-07-01 及之前的公告使用使命“テクノロジーで人々を適切な医療に案内する”；2026-07-02 起的公告使用“テクノロジーで、医療の願いを解き放つ”，公司官网和招聘网站现在也显示后者（[2026-07-02](https://prtimes.jp/main/html/rd/p/000000217.000048083.html)、[About](https://ubie.life/about_ubie)）。2026-10-08 的 Ubie Pharma Summit 2027 公告仍使用旧表述（[公告](https://prtimes.jp/main/html/rd/p/000000230.000048083.html)）。未找到宣布变更的公告。
- **产品名称多次变更：** AI受診相談ユビー → ユビーAI受診相談 → 症状検索エンジン「ユビー」，并于 2025-09-16 增加医療AIパートナー「ユビー」；AI問診Ubie → ユビーAI問診；ユビーメディカルナビ 生成AI → ユビー生成AI。较早的公告使用旧名称。
- **研究、政策与活动。** Ubie 于 2023-07-31 成立研究组织 Ubie Lab（[公告](https://prtimes.jp/main/html/rd/p/000000060.000048083.html)）。在日本数字健康联盟（JaDHA）内，公司主导了与 AI Safety Institute 合作的医疗 AI 安全评估指南，于 2026 年 4 月发布（[2026-04-03](https://prtimes.jp/main/html/rd/p/000000211.000048083.html)）。公司自 2023-02-28 起每年举办制药行业会议 Ubie Pharma Summit，2027 年会议定于 2027-05-19 和 20 日举行（[2023-02-01](https://prtimes.jp/main/html/rd/p/000000048.000048083.html)、[2026-10-08](https://prtimes.jp/main/html/rd/p/000000230.000048083.html)）。
- **健康影响估算。** 公司估算自创立以来带来的健康寿命延长超过 2.7 万年（QALY 增量），经济价值超过 1,500 亿日元（[2024-10-08](https://prtimes.jp/main/html/rd/p/000000107.000048083.html)）。这些是公司的估算。
- **新闻稿构成。** 在 198 篇 PR TIMES 公告中，有很多是会议公告（Ubie Pharma Summit、日本医療生成AIフォーラム）和单家医院导入案例，另有若干篇标注为仅限媒体用户查看。

---

## 资料来源

**官方**

- [公司官网（日文）](https://ubie.life/)：[About](https://ubie.life/about_ubie) · [Service](https://ubie.life/service) · [新闻索引](https://ubie.life/news)
- 安全相关页面：[数据保护](https://ubie.life/safety/data_protection) · [安全管理体制](https://ubie.life/safety/security_management) · [VCDP](https://ubie.life/safety/vcdp)
- [医院产品（intro.dr-ubie.com）](https://intro.dr-ubie.com/products)：[ユビーAI問診](https://intro.dr-ubie.com/products/aimon) · [价格](https://intro.dr-ubie.com/products/pricing) · [ユビー生成AI](https://intro.dr-ubie.com/products/generativeai_lp) · [ユビーDPCサポーター](https://intro.dr-ubie.com/products/dpc-supporter)
- [制药企业服务（ph-ubie.com）](https://ph-ubie.com/) · [ユビーAds](https://ph-ubie.com/ubie_ads)
- 消费者服务：[ユビー 条款（日文）](https://ubie.app/terms) · [美国条款](https://ubiehealth.com/terms)
- 美国公司网站：[business.ubiehealth.com](https://business.ubiehealth.com/) · [Origin](https://business.ubiehealth.com/origin) · [Ubie Smart Support](https://business.ubiehealth.com/provider/smart-support)
- 美国新闻室：[美国上线，2022-04-26](https://business.ubiehealth.com/newsroom/ubie-launches-ai-powered-symptom-checker-in-the-us) · [美国使用 200 万次，2023-12-04](https://business.ubiehealth.com/newsroom/ubie-used-by-2-million-americans-in-first-year)
- [招聘网站](https://recruit.ubie.life/)：[FAQ](https://recruit.ubie.life/faq) · [工作环境](https://recruit.ubie.life/work-environment) · [生成式 AI](https://recruit.ubie.life/generative-ai) · [事业部](https://recruit.ubie.life/division-Introduction)
- [HERP 职位板](https://herp.careers/v1/ubiehr)：
  - 产品与平台：[Product Engineer](https://herp.careers/v1/ubiehr/Tirj5oCs5hdd) · [Product Platform Engineer](https://herp.careers/v1/ubiehr/sqYyDunoCtcf) · [Auth Platform Engineer](https://herp.careers/v1/ubiehr/YCfO7_Vx1l58)
  - AI 与数据：[AI/ML Engineer](https://herp.careers/v1/ubiehr/f5-1jXvnBMVv) · [Corporate AI Engineer](https://herp.careers/v1/ubiehr/_oeH0lYReImI) · [Analytics Engineer](https://herp.careers/v1/ubiehr/Bilnrfg8U7vj)
  - 基础设施、客户端与安全：[Senior SRE](https://herp.careers/v1/ubiehr/QzoglruZi_M1) · [Windows Application Engineer](https://herp.careers/v1/ubiehr/QC24-tv1B1S8) · [Product Security Engineer](https://herp.careers/v1/ubiehr/cQ6vihXLiMLg)
  - 工程管理：[Engineering Manager](https://herp.careers/v1/ubiehr/9QuHU73KCC2P) · [VP of Engineering](https://herp.careers/v1/ubiehr/x3F1XHsBBT_L)
  - 实习：[Software Engineer Intern](https://herp.careers/v1/ubiehr/9QxaWhCu--oj)
- [Ubie テックブログ（Zenn）](https://zenn.dev/p/ubie_dev)：
  - 技术栈：[Go 与 Node.js，2022-12-14](https://zenn.dev/yuku/articles/4437cde02a672b) · [React Native，2024-11-18](https://zenn.dev/yuku/articles/46cf443d5dd25b)
  - 数据与基础设施：[迁移到 AlloyDB，2025-02-05](https://zenn.dev/electricalsheep/articles/cf1d74b65ec64b) · [NestJS/Prisma 模块化单体，2025-03-13](https://zenn.dev/nissy_dev/articles/nestjs-prisma-db-access-management) · [Go 个性化平台，2025-06-16](https://zenn.dev/glassmonkey/articles/7f393a44ffb029) · [安全分析 AI 代理，2026-03-31](https://zenn.dev/mizutani/articles/ai-sec-alert-ops)
  - 人员：[Yuku Kotani 个人页](https://zenn.dev/yuku)
- [Ubie note：累计 44.8 亿日元（日文）](https://note.com/ubie/n/n08baa940b694)
- [Speaker Deck 上的公司介绍资料（日文）](https://speakerdeck.com/ubie/ubie-hui-she-an-nei-202211)
- [GitHub 组织 ubie-oss](https://github.com/ubie-oss)

**新闻稿（PR TIMES，日文，较新在前；[公司页](https://prtimes.jp/main/html/searchrlp/company_id/48083)）**

- **2026：** [金沢医科大学病院 ユビー生成AI — 2026-10-09](https://prtimes.jp/main/html/rd/p/000000229.000048083.html) · [Ubie Pharma Summit 2027 — 2026-10-08](https://prtimes.jp/main/html/rd/p/000000230.000048083.html) · [日本スタートアップ大賞2026 — 2026-09-28](https://prtimes.jp/main/html/rd/p/000000227.000048083.html) · [北里大学病院 — 2026-09-16](https://prtimes.jp/main/html/rd/p/000000226.000048083.html) · [Reserve with Google 药局预约 — 2026-08-21](https://prtimes.jp/main/html/rd/p/000000224.000048083.html) · [Google Cloud Next Tokyo 演讲 — 2026-08-07](https://prtimes.jp/main/html/rd/p/000000223.000048083.html) · [九州がんセンター（首篇使用新使命的公告）— 2026-07-02](https://prtimes.jp/main/html/rd/p/000000217.000048083.html) · [AISI 医疗 AI 安全指南 — 2026-04-03](https://prtimes.jp/main/html/rd/p/000000211.000048083.html) · [Ubie Inc. 与 Mayo Clinic — 2026-02-16](https://prtimes.jp/main/html/rd/p/000000201.000048083.html) · [ユビー生成AI 100 家医院 — 2026-02-05](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)
- **2025：** [Medable 合作 — 2025-12-08](https://prtimes.jp/main/html/rd/p/000000192.000048083.html) · [九州大学病院 DPC — 2025-12-04](https://prtimes.jp/main/html/rd/p/000000191.000048083.html) · [补贴套餐 — 2025-11-28](https://prtimes.jp/main/html/rd/p/000000190.000048083.html) · [医療AIパートナー「ユビー」发布 — 2025-09-16](https://prtimes.jp/main/html/rd/p/000000178.000048083.html) · [Mayo Clinic Platform_Accelerate — 2025-09-04](https://prtimes.jp/main/html/rd/p/000000175.000048083.html) · [累计 180 亿日元 — 2025-05-12](https://prtimes.jp/main/html/rd/p/000000151.000048083.html) · [日本政策金融公庫 贷款 — 2025-05-08](https://prtimes.jp/main/html/rd/p/000000149.000048083.html) · [商工中金 贷款 — 2025-05-07](https://prtimes.jp/main/html/rd/p/000000148.000048083.html) · [セブン-イレブン・ジャパン 合作 — 2025-03-31](https://prtimes.jp/main/html/rd/p/000000139.000048083.html) · [NTTドコモ 合作 — 2025-03-27](https://prtimes.jp/main/html/rd/p/000000138.000048083.html) · [厚生劳动省补贴套餐 — 2025-03-21](https://prtimes.jp/main/html/rd/p/000000136.000048083.html) · [日本郵政キャピタル — 2025-03-06](https://prtimes.jp/main/html/rd/p/000000128.000048083.html)
- **2024：** [生成AI大賞2024 — 2024-12-19](https://prtimes.jp/main/html/rd/p/000000117.000048083.html) · [Google 投资 — 2024-10-08](https://prtimes.jp/main/html/rd/p/000000107.000048083.html) · [大阪ガス 合作 — 2024-10-01](https://prtimes.jp/main/html/rd/p/000000105.000048083.html) · [シミック 合作 — 2024-09-30](https://prtimes.jp/main/html/rd/p/000000104.000048083.html) · [东京都补贴套餐 — 2024-07-08](https://prtimes.jp/main/html/rd/p/000000091.000048083.html) · [ユビーメディカルナビ 生成AI β — 2024-05-02](https://prtimes.jp/main/html/rd/p/000000076.000048083.html) · [影响力融资约 35 亿日元 — 2024-04-12](https://prtimes.jp/main/html/rd/p/000000073.000048083.html)
- **2023：** [Google Play Best of 2023 — 2023-11-30](https://prtimes.jp/main/html/rd/p/000000064.000048083.html) · [Ubie Lab — 2023-07-31](https://prtimes.jp/main/html/rd/p/000000060.000048083.html) · [武田薬品 综合协议 — 2023-04-10](https://prtimes.jp/main/html/rd/p/000000052.000048083.html) · [股票期权 U-win — 2023-04-07](https://prtimes.jp/main/html/rd/p/000000051.000048083.html) · [辉瑞 OAB 成果 — 2023-03-13](https://prtimes.jp/main/html/rd/p/000000050.000048083.html) · [首届 Ubie Pharma Summit — 2023-02-01](https://prtimes.jp/main/html/rd/p/000000048.000048083.html)
- **2022：** [美国子公司 — 2022-12-08](https://prtimes.jp/main/html/rd/p/000000047.000048083.html) · [シリーズC 完成 62.6 亿日元 — 2022-10-06](https://prtimes.jp/main/html/rd/p/000000044.000048083.html) · [ユビーリンク 15,000 — 2022-09-07](https://prtimes.jp/main/html/rd/p/000000043.000048083.html) · [中部電力 合作 — 2022-07-27](https://prtimes.jp/main/html/rd/p/000000040.000048083.html) · [シリーズC 首次交割 35 亿日元 — 2022-07-27](https://prtimes.jp/main/html/rd/p/000000039.000048083.html) · [ユビーAI問診 1,000 家机构 — 2022-07-25](https://prtimes.jp/main/html/rd/p/000000038.000048083.html) · [勃林格殷格翰合作 — 2022-02-02](https://prtimes.jp/main/html/rd/p/000000031.000048083.html)
- **2021：** [拜耳合作 — 2021-11-24](https://prtimes.jp/main/html/rd/p/000000026.000048083.html) · [辉瑞合作 — 2021-10-15](https://prtimes.jp/main/html/rd/p/000000024.000048083.html) · [ユビーリンク 发布 — 2021-07-27](https://prtimes.jp/main/html/rd/p/000000022.000048083.html) · [月活 100 万 — 2021-06-08](https://prtimes.jp/main/html/rd/p/000000021.000048083.html) · [AI問診ユビー 400 家机构 — 2021-05-21](https://prtimes.jp/main/html/rd/p/000000020.000048083.html) · [武田薬品 合作 — 2021-04-21](https://prtimes.jp/main/html/rd/p/000000019.000048083.html)
- **2020：** [日本服务大奖 — 2020-10-27](https://prtimes.jp/main/html/rd/p/000000009.000048083.html) · [新加坡实体、JETRO — 2020-10-15](https://prtimes.jp/main/html/rd/p/000000008.000048083.html) · [スズケン 20 亿日元 — 2020-06-04](https://prtimes.jp/main/html/rd/p/000000005.000048083.html)

**PR Newswire（英文，Ubie, Inc.）**

- [自助广告平台 — 2026-06-03](https://www.prnewswire.com/news-releases/ubie-launches-self-serve-platform-for-targeted-healthcare-advertising-within-ai-patient-experiences-302790171.html)
- [累计融资超过 1.25 亿美元 — 2025-06-26](https://www.prnewswire.com/news-releases/ubie-announces-cumulative-total-funding-of-over-125m-as-us-efforts-target-expansion-into-generative-ai-and-provider-solutions-302491436.html)

**第三方报道与档案**

- [国税厅法人番号公表网站 — 7010701034132（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701034132)
- [BRIDGE — KVM 融资与种子轮历史，2018-05（日文）](https://thebridge.jp/2018/05/ubie-jpy300m-funding) · [スズケン 20 亿日元，2020-06（日文）](https://thebridge.jp/2020/06/ubie-jpy2b-funding)
- [J-Startup — Ubie（日文）](https://www.j-startup.go.jp/startups/212-ubie.html)
- [Japan Dev — 公司页（未经核实）](https://japan-dev.com/companies/ubie)
