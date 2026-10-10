# Medmain

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Medmain（メドメイン株式会社 / Medmain Inc.）是一家总部位于福冈、于 2018-01-11 注册成立的公司，由飯塚 統（Osamu Iizuka）在九州大学医学部就读期间创立。公司开发 **PidPort**：一套基于浏览器的云系统，用于存储、浏览、标注和共享数字化病理切片（全切片图像，WSI），用于远程会诊、病例讨论会和教学，并配有自研的病理图像 AI 模型；公司还提供切片扫描服务。公司产品页面注明，在日本国内 AI 解析功能计划将来提供（※日本国内において、AI解析に関する機能については将来的な提供を計画しています）。自 2026-04-30 起，Medmain 通过 TechMatrix（テクマトリックス，东证 Prime 3762）及其子公司 PSP 成为 TechMatrix 的合并子公司。

- **控制权：** TechMatrix 与 PSP 约定以约 23 亿日元（約23億円）收购除 PSP 和 CEO 飯塚所持股份以外的全部股份；交易后 TechMatrix 持有 29.10%、PSP 持有 42.95% 的表决权（[TechMatrix TDnet，2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)）。Medmain 于 [2026-05-01](https://medmain.com/news/63907/) 宣布交易已于 2026-04-30 完成。
- **被收购前的融资：** 在 One Capital 领投的 4.7 亿日元融资之后，股权累计融资额为 25 亿日元（[2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)）；公司唯一命名过的轮次是 8.5 亿日元的シリーズA2（[2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)）。
- **规模：** 根据 [TechMatrix 2026-02-17 披露](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)中的标的公司概况，2024 财年（12 月结算）营收 2.4882 亿日元、营业亏损 2.7716 亿日元，员工 15 人。
- **监管：** ISO 13485:2016（首次注册 2025-01-27）和 ISO/IEC 27001:2022（2024-11-04）（[公司页面](https://medmain.com/aboutus/)；访问于 2026-10-11）。公司于 [2024-08-02](https://prtimes.jp/main/html/rd/p/000000041.000034505.html) 宣布取得第一種医療機器製造販売業许可，但公司页面列出的是编号不同的第二種许可——见“备注”。在查阅的资料中，未见 Medmain 产品取得 PMDA 批准或认证的公告。
- **工程：** 产品 FAQ 写明存储使用 AWS、认证使用 Auth0（[PidPort 页面](https://service.medmain.com/service/pidport)；访问于 2026-10-11）。当前的 [Fullstack Engineer 职位](https://open.talentio.com/r/1/c/medmain/pages/114519)列出 Kotlin（Spring Boot）、Python、React/TypeScript、MySQL、MongoDB、AWS 和 Terraform，要求能用日语沟通，允许在日本国内外完全远程，年薪 800 万–1,200 万日元（无日期，访问于 2026-10-11）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前公开品牌 | Medmain；产品 PidPort、PidPort Personal、PidPort Digital Slide Creation Service | [服务网站](https://service.medmain.com/service/pidport)；访问于 2026-10-11 |
| 法定名称 | メドメイン株式会社（Medmain Inc.） | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259)、[公司页面](https://medmain.com/aboutus/) |
| 法人番号 | 2290001080259；番号指定日 2018-01-18 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259)；截至 2026-10-11 的信息 |
| 成立 | 2018-01-11 | [成立公告，2018-01-11](https://medmain.com/pressrelease/829/)、[公司页面](https://medmain.com/aboutus/) |
| 登记总部 | 福岡県福岡市中央区赤坂２丁目４番５号；2019-05-21 由福岡市中央区荒戸１丁目３番９号インスパイヤー大濠３０１号迁入 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259) |
| 办公地点 | 福冈：赤坂2-4-5 シャトレサクシーズ104。东京：港区南青山2-10-11 A青山ビル2F。美国：212 Homer Ave, Palo Alto, CA（Medmain USA Inc.） | [公司页面](https://medmain.com/aboutus/)；访问于 2026-10-11 |
| 代表人 | 代表取締役 CEO 飯塚 統（Osamu Iizuka） | [公司页面](https://medmain.com/aboutus/) |
| 母公司 | TechMatrix 持有 29.10%、PSP 持有 42.95% 的表决权；自 2026-04-30 起为 TechMatrix 的合并子公司 | [TechMatrix TDnet，2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)、[2026-05-01](https://medmain.com/news/63907/) |
| 资本金 | 含资本准备金 11.9 亿日元（11億9000万円，公司页面）；資本金 1 亿日元（TechMatrix 披露及 Medmain 2026-02-17 公告）——见“备注” | [公司页面](https://medmain.com/aboutus/)、[TechMatrix TDnet](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |
| 已发行股份；财年 | 151,183 股；12 月结算 | [TechMatrix TDnet，2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |
| 员工人数 | 15 人（従業員数） | [TechMatrix TDnet，2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |
| 工作语言 | 未公布全公司政策；职位层面的证据见“工作条件” | — |
| 客户 | PidPort 已在日本拥有大学附属医院的大学中超过 60% 导入（大学病院を有する大学の6割超） | [2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html) |
| 累计融资 | 股权累计融资 25 亿日元 | [2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html) |
| 许可与备案（公司页面） | 第二種医療機器製造販売業 13B2X10662；高度管理医療機器等販売・貸与業 7港み生機器第59号；電気通信事業届出 H-04-01768 | [公司页面](https://medmain.com/aboutus/)；访问于 2026-10-11 |
| 许可（公告） | 第一種医療機器製造販売業，13B1X10433，东京都于 2024-07-02 颁发 | [2024-08-02](https://prtimes.jp/main/html/rd/p/000000041.000034505.html) |
| 认证 | ISO/IEC 27001:2022 及 JIS Q 27001:2023，JP24/00000322，SGSジャパン，首次注册 2024-11-04，范围为“医療ソフトウェア・クラウドサービスの企画・開発・運営および販売”。ISO 13485:2016，50301629 MP2016，ドイツ品質システム認証，首次注册 2025-01-27，范围为“The design of software for pathology diagnostic support” | [公司页面](https://medmain.com/aboutus/)、[ISMS 公告](https://prtimes.jp/main/html/rd/p/000000043.000034505.html)、[ISO 13485 公告](https://prtimes.jp/main/html/rd/p/000000045.000034505.html) |
| 专利 | 特許第7752741号“所見作成作業効率化システム”，登记于 2025-10-02 | [2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html) |
| 主要往来银行 | 三菱UFJ銀行、福岡銀行 | [TechMatrix TDnet，2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf) |

### 品牌与法律实体

| 名称 | 类型 | 法域／期间 | 资料中所述关系 | 来源 |
|---|---|---|---|---|
| Medmain | 品牌；早于公司成立 | 网站于 2015-12-28 开设；学生时期项目九医クラウド（2016）和病理软件“OMEGA”（2017）以该品牌发布 | 在注册成立前已运营；资料未说明其与 2018 年成立公司之间的法律延续性 | [2015-12-28](https://medmain.com/news/35/)、[2016-06-20](https://medmain.com/pressrelease/322/)、[2017-05-24](https://medmain.com/pressrelease/324/) |
| メドメイン株式会社 | 法律实体 | 日本，自 2018-01-11 起 | 运营公司；“九州大学発のスタートアップ” | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259)、[2018-01-11](https://medmain.com/pressrelease/748/) |
| Medmain USA Inc. | 关联实体 | 特拉华州，2018-05-22 公布 | “メドメインの米国法人”；公司页面列有 Palo Alto 地址 | [2018-05-22](https://medmain.com/pressrelease/1023/)、[公司页面](https://medmain.com/aboutus/) |
| メドテリア株式会社 | 关联实体 | 日本，2024-08-01 成立 | 承接面向医学生的云服务 Medteria 业务；飯塚任董事；持股关系未说明 | [2024-08-01](https://medmain.com/news/52692/) |
| テクマトリックス株式会社 | 母公司 | 东证 Prime 3762 | 自 2026-04-30 起持有 Medmain 29.10% 的表决权 | [TechMatrix TDnet，2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf) |
| PSP株式会社 | 母公司集团内公司 | 东京；TechMatrix 持有 50.02% | 自 2022 年起为股东；自 2026-04-30 起持有 Medmain 42.95% 的表决权 | [TechMatrix TDnet，2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf) |

**项目与奖项**（公司公告）：经济产业省“飛躍 Next Enterprise”硅谷派遣项目（[2018-12-21](https://medmain.com/pressrelease/1441/)）；NICT“起業家万博”総務大臣賞（[2019-04-06](https://medmain.com/pressrelease/1504/)）；J-Startup（[2019-06-26](https://medmain.com/pressrelease/1563/)）；与九州大学起業部共同获得第2回日本オープンイノベーション大賞 文部科学大臣賞（[2020-02-19](https://medmain.com/news/1692/)）；NEDO 研究開発型スタートアップ支援事業，补助上限 2 亿日元（[2022-06-27](https://prtimes.jp/main/html/rd/p/000000023.000034505.html)）；AMED 令和5年度 医工連携イノベーション推進事業，课题为胃·大肠活检 AI 系统（[2023-09-07](https://prtimes.jp/main/html/rd/p/000000034.000034505.html)）；U.S. Market Gateway Accelerator for BioSciences and MedTech（[2023-09-06](https://prtimes.jp/main/html/rd/p/000000035.000034505.html)）；经济产业省设于 Palo Alto 的 Japan Innovation Campus（[2023-11-22](https://prtimes.jp/main/html/rd/p/000000038.000034505.html)）；福冈市 High Growth Program（[2024-08-01](https://medmain.com/news/44031/)）、令和6年度 IPO等に向けた成長支援プログラム（[2024-08-08](https://medmain.com/news/44474/)）和令和7年度 IPO Growth Program（[2025-09-03](https://medmain.com/news/57313/)）；Forbes JAPAN“JAPAN's AI 50”（[2025-01-30](https://medmain.com/news/50262/)）；日経 NEXTユニコーン 2024（[2025-01-31](https://medmain.com/news/50364/)）和 2025（[2026-01-21](https://medmain.com/news/61450/)）；Mizuho Innovation Award 2025.1Q（[2025-06-11](https://medmain.com/news/54666/)）。公司于 [2023-04](https://medmain.com/news/25661/) 加入 AI医療機器協議会，飯塚于 [2025-06](https://medmain.com/news/54862/) 出任该协会理事。

### 公司陈述的市场背景

- 日本病理医人数：[招聘介绍页](https://medmain.notion.site/recruiting-note)写“日本全国に僅か2500名強（医師全体数の0.7〜0.8%ほど）”（无日期，访问于 2026-10-11）；[2024-10-31 公告](https://prtimes.jp/main/html/rd/p/000000042.000034505.html)写“約2,800名”。公司称许多医院只有一名病理医，或将诊断外包。
- [2026-02-17 公告](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)称 PSP 是日本云 PACS 份额第一的企业，拥有 2,600 家机构的客户基础；并将病理诊断支援 AI 进入临床应用阶段、确保医疗器械审批工作的连续性、以及将数字病理数据回馈医学研究列为加入 TechMatrix 集团的理由。

---

## 产品

产品页面位于 [service.medmain.com](https://service.medmain.com/service/pidport)；机构用户在 `pidport.com` 登录，个人用户在 `entry.personal.pidport.com` 注册。

### PidPort（机构版）

公司称其为“デジタル病理支援クラウドシステム”，无需扫描仪、服务器或安装软件（[PidPort 页面](https://service.medmain.com/service/pidport)；访问于 2026-10-11）。页面列出的功能：

- 自研高速浏览器查看器；最多四张切片分屏并同步操作；Z-stack 浏览；色调设置可分个人用和共享用保存；
- 用户间共享的评论和标注绘图；截图；附加相关文档（pdf、doc(x)、xls(x)、csv、ppt(x)、zip）；
- 批量上传 WSI，支持 tiff、jpeg、png、svs、ndpi、zip（vsi）、isyntax 和 i2syntax；
- 使用场景包括医院间远程会诊、在线病例讨论会、教学和共同研究（[使用场景页面](https://service.medmain.com/scene)）。

FAQ 称与电子病历的衔接方式是把 PidPort 病例 URL 贴入病历，系统层面的对接“正在考虑”；推荐浏览器为 Chrome（[FAQ](https://service.medmain.com/faq)；访问于 2026-10-11）。

**AI 解析状态。** 查阅的所有现行产品页面都注明日本国内的 AI 解析功能计划将来提供（[产品](https://medmain.com/products/)、[PidPort](https://service.medmain.com/service/pidport)、[选择理由](https://service.medmain.com/reason)；访问于 2026-10-11）。[2020-03-10 公告](https://prtimes.jp/main/html/rd/p/000000009.000034505.html)称，在日本以外可使用 AI 解析、远程诊断和云存储（部分地区部分功能不可用），在日本国内只提供远程诊断、云存储和切片数字化。PidPort 页面列出的 AI 覆盖范围为胃、大肠、肺、乳腺、胰腺（EUS-FNB 腺癌）、前列腺和淋巴结转移的组织判定，以及宫颈和尿液的细胞判定。

### 其他产品与服务

| 产品 | 内容 | 来源 |
|---|---|---|
| PidPort Personal | 面向个人的自助方案：Starter（免费；上传、浏览、标注、Z-stack）和 Personal（每月 3,980 日元，50 GB；图像下载，AI 解析“今后追加”），另有 100 GB 和 250 GB 档；此前 PidPort 只以法人合同方式提供 | [方案页面](https://service.medmain.com/service/personal)（访问于 2026-10-11）、[2026-07-01](https://medmain.com/news/65758/)、[2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html) |
| PidPort Digital Slide Creation Service（Imaging Center） | 玻璃切片代扫描；2019-06 开始；使用 Leica Aperio AT2 和浜松ホトニクス NanoZoomer S360；仅明场 ×20 或 ×40；每张 WSI 平均约 1 GB；交付方式为 PidPort 文件夹、下载系统或硬盘 | [2019-06-17](https://medmain.com/pressrelease/1552/)、[FAQ](https://service.medmain.com/faq) |
| 病理版 NOBORI | 结合 Medmain 与 PSP 技术的病理云 PACS，自 2024-11-01 提供：云存储、图像解析 AI、会诊和远程病理诊断，并可与 CT、MRI、内窥镜图像统一管理 | [2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html) |
| Medteria | 2018 年推出的医学生云服务；2024-08-01 分拆至メドテリア株式会社 | [2018-06-11](https://prtimes.jp/main/html/rd/p/000000001.000034505.html)、[2024-08-01](https://medmain.com/news/52692/) |

### 商业化

PidPort 的机构价格为个别报价（“個別にご案内”），扫描服务按张计价、数量越多单价越低，需询价（[FAQ](https://service.medmain.com/faq)；访问于 2026-10-11）。只有个人方案公开价格（[方案页面](https://service.medmain.com/service/personal)）。产品网站页脚链接了特定商取引法说明。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2018-10-15 | PidPort α 版计划在合作医疗机构内封闭运行，与实际诊断分离 | [公告](https://prtimes.jp/main/html/rd/p/000000004.000034505.html) |
| 2020-08-24 | PidPort 于 2020-02 正式发布；与日本国内外 50 多家医疗机构开展共同研究 | [公告](https://prtimes.jp/main/html/rd/p/000000010.000034505.html) |
| 2022-07-26 | 已开发覆盖 7 个器官、12 个模型的 AI | [公告](https://prtimes.jp/main/html/rd/p/000000024.000034505.html) |
| 2024-10-31 | 与日本国内外 100 多家医疗机构有共同研究或使用实绩 | [公告](https://prtimes.jp/main/html/rd/p/000000042.000034505.html) |
| 2024-12-23 | PidPort 已在日本 82 所设有医学部的大学中超过半数导入 | [公告](https://prtimes.jp/main/html/rd/p/000000044.000034505.html) |
| 2026-02-17 | 已在拥有大学附属医院的大学中超过 60% 导入；海外医疗机构也在使用 | [公告](https://prtimes.jp/main/html/rd/p/000000054.000034505.html) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2022-07-26](https://prtimes.jp/main/html/rd/p/000000024.000034505.html) | PSP | 资本业务合作；PSP 代销 Medmain 产品并将其整合进自身基础设施 |
| [2023-11-02](https://medmain.com/news/32208/) | 久留米大学医学部病理学講座 | 将 PidPort 用于教学与研究 |
| [2023-12-18](https://medmain.com/news/34196/) | JP-AID（日本病理学会）／东京大学 | JP-AID 开发的胃活检诊断支援 AI 将由 Medmain 在 AMED 项目下以程序医疗器械获批为目标推进开发 |
| [2025-05-21](https://medmain.com/news/53996/) | 鳥取大学医学部 | 在解剖学和病理学组织学实习中使用 PidPort |
| [2025-07-25](https://prtimes.jp/main/html/rd/p/000000049.000034505.html) | Bạch Mai 医院、E 医院、Thái Nguyên A 医院（越南） | 签署数字病理与医疗 AI 合作备忘录 |
| [2025-08-01](https://prtimes.jp/main/html/rd/p/000000050.000034505.html) | SMC（メディカルツーリズム・ジャパン事業部） | 在越南推进病理 AI 研究利用的合作协议 |
| [2025-09-12](https://medmain.com/news/57578/) | 胡志明市 Thống Nhất 医院 | 病理诊断科导入 PidPort |
| [2025-10-20](https://prtimes.jp/main/html/rd/p/000000052.000034505.html) | 河内 Ha Dong General Hospital | PidPort 的研究利用和实证试验 |

产品网站的导入案例列出了国際医療福祉大学、一般社団法人 PathPortどこでも病理ラボ、東葛病院和東京医科大学病院（[案例列表](https://service.medmain.com/case)；访问于 2026-10-11）。

### 公开计划

- 2025 年资金用途：进一步开发病理 AI 和 PidPort、数字化领域投资、销售、病理 AI 的药事审批申请（病理AIの薬事承認申請）以及海外扩张的基础建设（[2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)）。2024 年 Series A2 公告列出的用途为软件开发、数字化设备、销售和医疗器械审批申请（[2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)）。
- 加入 TechMatrix 集团后：加强为病理诊断支援 AI 取得医疗器械批准以及持续开展药事与质量工作的体制；深化与 PSP 云 PACS 和远程影像诊断平台的衔接；借助 PSP 的客户基础和销售、支持体系在全国推广（[2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)）。
- 将所见文书专利实装到 PidPort（[2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html)）；在个人方案中追加 AI 解析（[2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html)）。

---

## 创始人

**飯塚 統（Osamu Iizuka）**——创始人、代表取締役 CEO（[公司页面](https://medmain.com/aboutus/)）。

- 在九州大学医学部医学科就读期间（九州大学医学部医学科在学中）开发 AI 与 Web 软件，并曾在一家创业公司担任软件工程师（[公司页面](https://medmain.com/aboutus/)）。他在招聘网站的寄语中称，在大学研究室用机器学习做的细胞追踪系统是把这项工作应用到病理诊断的起点（[CEO 寄语](https://recruit.medmain.com/message)；无日期，访问于 2026-10-11）。
- 2017-11-17：病理软件“Omega”在硅谷 Live Sharks Tank 路演活动中获胜（[2017-11-24](https://medmain.com/news/672/)）。
- 2018-01-11：注册成立 Medmain 并出任代表取締役（[2018-01-11](https://medmain.com/pressrelease/748/)）。一篇访谈称公司由四名九州大学学生创立（[社長名鑑](https://shachomeikan.jp/industry_article/3551)；信息截至 2025-01）。
- 2018-05：PidPort 在爱沙尼亚 Latitude59 路演比赛中获胜（[2018-05-30](https://medmain.com/news/1037/)）。
- 2020-04-02：入选 Forbes 30 Under 30 Asia，Healthcare & Science 类别（[2020-04-02](https://medmain.com/news/1743/)）。
- 2024-08-01：出任分拆出的メドテリア株式会社董事（[2024-08-01](https://medmain.com/news/52692/)）。
- 2025-06：出任 AI医療機器協議会理事（[2025-06-17](https://medmain.com/news/54862/)）。
- 持股：截至 2026-01-31，持有普通股 43,581 股，占表决权 28.83%（[TechMatrix TDnet，2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)）。

### 主要管理层

[公司页面](https://medmain.com/aboutus/)列出的董事会（无日期，访问于 2026-10-11；页面只给出英文姓名）：

| 姓名 | 职务 | 公开背景 |
|---|---|---|
| Osamu Iizuka（飯塚 統） | CEO、董事 | 见上文 |
| Masayuki Tsuneki（常木 雅之） | 董事 | 病理学研究者、大学教员；曾在国立大学、耶鲁大学和国立癌症研究中心从事致癌分子病理学研究 |
| Yoshihisa Yoda（依田 佳久） | 董事 | ニチメン（现双日）；曾任 TechMatrix 董事并创设其医疗事业部门；2018 年创立 NOBORI；2022 年起任 PSP 社长。同时为 TechMatrix 取締役 専務執行役員（[2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)） |
| Tomohiro Tanaka | 董事 | 在 TechMatrix 从事医疗影像管理系统销售近 20 年；2022 年 PSP 与 NOBORI 合并后任 PACS 业务销售负责人；目前负责启动病理影像云业务 |
| Masayuki Takahashi | 监事 | 从综合商社海外销售起步；曾负责 TechMatrix 上市事务；统管 PSP 及其集团的管理工作 |

常木是公司 AI 论文的通讯作者，所属单位为“Medmain Research, Medmain Inc.”（[Ki-67 论文，2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12984776/fullTextXML)）；公司宣布他入选斯坦福大学／Elsevier“World's Top 2% Scientists”临床医学领域名单（[2025-12-25](https://medmain.com/news/60752/)）。2026-02-17 公告列出浅子 信太郎为经营顾问、深田 啓介（エンジェルナビ CEO；自 [2024-04](https://prtimes.jp/main/html/rd/p/000000040.000034505.html) 起任顾问）为财务顾问（[2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)）。公司页面未列出 CTO。Fullstack Engineer 职位称开发团队以一位曾在医疗创业公司担任 CTO/PdM 的 PdM 和病理 AI 开发负责人（病理医）为核心，另有来自日本国内外的工程师（[职位](https://open.talentio.com/r/1/c/medmain/pages/114519)）。

招聘网站上的职位类别为 Engineering、Sales & Marketing、BizDev（R&D 业务开发）、AI Product Manager，以及业务委托的 Doctor／病理医リエゾン（[Talentio](https://open.talentio.com/r/1/c/medmain/homes/3686)；访问于 2026-10-11）。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2018-08-17 | 第三者割当増資 | 1 亿日元 | DEEPCORE TOKYO1号投資事業有限責任組合；九州アントレプレナークラブ2号（ドーガン・ベータ） | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000034505.html) |
| 2020-08-24 | 第三者割当増資 | 约 11 亿日元 | 新增：国際医療福祉大学・高邦会グループ、福岡和白病院グループ、QTnet、Hike Ventures、みらい創造機構、Hike Ventures 组建的 SPV、个人投资者。原有：ディープコア、ドーガン・ベータ | 约 12 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000010.000034505.html) |
| 2022-07-26 | 第三者割当増資（資本業務提携） | 3 亿日元 | PSP | 未说明 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000024.000034505.html) |
| 2024-04-18 | シリーズA2 | 8.5 亿日元 | PSP、ミガロホールディングス、ニコン、エンジェルナビ・グループ、福山太郎、个人投资者 | 20.5 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000040.000034505.html) |
| 2025-05-08 | 第三者割当増資 | 4.7 亿日元 | One Capital（领投）、Niremia Collective、Plug and Play | 25 亿日元（股权） | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000046.000034505.html) |

公司只为 2024 年一轮命名（シリーズA2）。[BRIDGE（2020-08）](https://thebridge.jp/2020/08/medmain-series-a-round-funding)称 2020 年一轮大致相当于 Series A；[BRIDGE（2024-04）](https://thebridge.jp/2024/04/medmain-series-a2-round-funding)称 2024 年一轮是 Series A 的第二次交割，并将第一次交割对应到 2022 年 PSP 的投资。PSP 于 2022 年投资，并在 Series A2 中再次投资。Medmain 还在 2022 年获得上限 2 亿日元的 NEDO 补助（见“基本情况”）。

### 被 TechMatrix 集团收购

TechMatrix 与 PSP 于 2026-02-17 签署基本协议，收购 Medmain 股份，使其连同 PSP 原有持股合计过半；2026-04-24 就股份转让达成协议，转让于 2026-04-30 生效，各出售股东的转让日期不同（[TechMatrix TDnet，2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)、[2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)、[Medmain，2026-05-01](https://medmain.com/news/63907/)）。

| 持有人 | 交易前（截至 2026-01-31 或 2026-02-17） | 交易后（2026-04-30） |
|---|---|---|
| TechMatrix | 0 | 普通股 8,427 股、S 种优先股 14,077 股、A 种优先股 22,867 股；45,371 个表决权，29.10% |
| PSP | 普通股 5,593 股、A 种优先股 17,080 股；22,673 个表决权，15.00% | 普通股 12,738 股、S 种优先股 19,864 股、A 种优先股 34,375 股；66,977 个表决权，42.95% |
| 飯塚 統 | 普通股 43,581 股，28.83% | 不在收购范围内；交易后比例未说明 |
| DEEPCORE TOKYO 1号投資事業有限責任組合 | 8.81% | 属于收购范围 |
| One Capital DX2号投資事業有限責任組合 | 7.54% | 属于收购范围 |
| One Capital2号投資事業有限責任組合 | 4.93% | 属于收购范围 |

对价合计约 23 亿日元——TechMatrix 约 11.6 亿日元、PSP 约 11.4 亿日元——支付给出售股东，而非支付给 Medmain（[2026-04-24](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)）。交易前 PSP 向 Medmain 董事会派驻 1 名董事（[2026-02-17](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)）。

### TechMatrix 披露的财务数据

[2026-02-17 披露](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)中 Medmain 最近三个财年的数据（标注为“連結”，单位：千日元）：

| 财年（12 月） | 2022 | 2023 | 2024 |
|---|---|---|---|
| 营收 | 60,742 | 171,148 | 248,820 |
| 营业亏损 | △390,341 | △324,929 | △277,162 |
| 经常亏损 | △376,411 | △220,942 | △242,070 |
| 净亏损 | △377,074 | △221,561 | △242,644 |
| 净资产 | 296,397 | 389,460 | 155,949 |
| 总资产 | 375,885 | 470,552 | 216,807 |

---

## 工程

### 技术栈与平台

- **产品文档确认：** 存储使用 AWS，认证使用 Auth0（[PidPort FAQ](https://service.medmain.com/service/pidport)；访问于 2026-10-11）。
- **公司论文确认（机器学习研究）：** TensorFlow；以 TensorFlow 为后端的 Keras；scikit-learn；从零训练的 Inception-v3，以 max-pooling 和 RNN 汇总切块结果（[Sci Rep 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6992793/fullTextXML)）；采用部分微调和弱监督学习的 EfficientNetB1（[PLOS ONE 2022](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9683606/fullTextXML)）；StarDist 细胞核检测（[Diagnostics 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12984776/fullTextXML)）。数据集使用 Leica Aperio AT2 扫描，以 JPEG2000 压缩的 SVS 格式保存。
- **当前 Fullstack Engineer 职位列出（技術環境）：** 后端 Kotlin（Spring、Spring Boot）和 Python；前端 React.js 和 TypeScript；MySQL 和 MongoDB；AWS；Terraform；Jira；Zoom、Slack、Notion、Google Workspace。职位补充说明技术栈会按开发阶段选择（[职位](https://open.talentio.com/r/1/c/medmain/pages/114519)；无日期，访问于 2026-10-11）。
- **公开 GitHub 资产：** 组织 [`medmain`](https://github.com/medmain)（“Medmain Inc.”，创建于 2018-04-25）在 2026-10-11 有 15 个公开仓库。原创仓库包括 `react-openseadragon`（OpenSeadragon 图像查看器的 React 封装；最后推送 2021-01-18）、`react-ui-kit`（“React shared components used by Medmain applications”；2022-07-18）和 `ml-lung-subtype`（2021-02-22）。fork 包括 `openslide`、`libvips`、`cantaloupe`（IIIF 图像服务器）、`geotiff.js`（最后推送 2026-02-14）、`auth0-java`（2025-11-21）、`tensorflow` 和 `terraform-aws-vpc`。fork 不能证明在生产中使用。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| PidPort 云与查看器 | 面向机构和个人的 WSI 上传、存储、检索、浏览器分块浏览、标注、评论和多切片同步 | [PidPort 页面](https://service.medmain.com/service/pidport)、[方案页面](https://service.medmain.com/service/personal) |
| WSI 分类模型 | 切块级 CNN 结果汇总为切片级预测；训练数据由病理医用自研标注工具标注；公司称拥有加速模型开发的迁移学习基础技术（“partial transfusion”，MIDL 2021） | [产品](https://medmain.com/products/)、[2021-07-09](https://medmain.com/news/2164/)、[Sci Rep 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6992793/fullTextXML) |
| 训练回路（2018 年设计） | 上传图像在 Web 服务器上由 AI 解析；部分已解析图像送往超级计算机用于追加训练 | [2018-10-15](https://prtimes.jp/main/html/rd/p/000000004.000034505.html) |
| 细胞级免疫组化定量 | 细胞核检测加分类，在病理医指定的 ROI 内计算 Ki-67 标记指数；阳性细胞分类 ROC-AUC 0.981 | [2026-04-03](https://prtimes.jp/main/html/rd/p/000000055.000034505.html) |
| 所见文书核对（专利） | 将病理医撰写的所见文与 AI 依据图像生成的所见文比较，计算相似度以提示错字、遗漏和不一致 | [2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html) |
| 切片数字化 | 代扫描业务及交付流程 | [FAQ](https://service.medmain.com/faq) |
| 病理云 PACS | 与 PSP 共同打造的病理版 NOBORI 服务 | [2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html) |
| 自助计费 | 个人注册、选择方案、在线支付并可使用优惠码 | [2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html) |

截至 2026-10-11，Europe PMC 收录的 Medmain 署名论文共 26 篇，多为 2020–2023 年，涉及胃、大肠、肺、乳腺、胰腺、前列腺、宫颈和尿液细胞学、黑色素瘤及淋巴结转移（[Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AFF%3A%22Medmain%22&format=json&pageSize=100&resultType=lite)）。所列数据来源包括広島大学病院、国際医療福祉大学三田病院和カマチグループ医院。公司还发布了一项多中心胃活检 AI 研究的 opt-out 通知，公司为该研究的分担机构（[情報公開](https://medmain.com/disclosure/)）。

### 招聘所需技术背景

- **Fullstack Engineer——必需：** Java 开发（5 年以上）；数据库设计（3 年以上）；以“最近 3 年内”引出的经验：Kotlin 或 Scala、AWS 等云环境开发、Docker 等容器化开发、REST API 开发、GitHub 或 GitLab；以及能用日语沟通。**优先：** Python、React/TypeScript、Auth0 等认证服务、Terraform 等基础设施即代码（[职位](https://open.talentio.com/r/1/c/medmain/pages/114519)）。
- **AI Product Manager——必需：** AI/ML 产品的 PdM/PM、AI 创业公司的产品战略、医疗／健康 AI 业务开发、SaMD 开发或企划、AI 咨询或 AI 业务负责人经验。**优先：** PMDA/FDA 法规应对、AI 验证设计、QMS、病理领域。职责包括判断是否申请 SaMD 批准，以及在不申请批准时设计业务战略（[职位](https://open.talentio.com/r/1/c/medmain/pages/127108)；无日期，访问于 2026-10-11）。

### 行业领域

组织病理学与细胞病理学：玻璃切片与 WSI、扫描仪文件格式、HE 染色与免疫组化、活检与手术切除标本，以及病理医报告。法规方面包括药机法（薬機法）、程序医疗器械（SaMD）、製造販売業许可和 ISO 13485 质量管理，以及 opt-out 通知等研究伦理程序。AI Product Manager 职位将 SaMD 和病理知识列为优先条件，R&D Business Development 职位将病理学理解和生命科学知识列为优先条件（[R&D BD 职位](https://open.talentio.com/r/1/c/medmain/pages/127106)）。查阅的职位均未说明行业知识可在入职后学习。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | Fullstack Engineer：要求能用日语沟通。AI Product Manager：职责包括与海外成员用英语沟通。招聘介绍页：公司内外使用英语的机会很多；外籍员工较多，以工程师为主。未找到全公司语言政策 | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519)、[AI PM](https://open.talentio.com/r/1/c/medmain/pages/127108)、[招聘介绍页](https://medmain.notion.site/recruiting-note) |
| 地点与远程 | 福冈总部和东京办公室。Fullstack 职位：工作地点不限，可在日本国内外完全远程。招聘网站：远程取决于职种。招聘介绍页：有员工在伦敦、中国等地远程工作 | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519)、[招聘网站](https://recruit.medmain.com/)、[招聘介绍页](https://medmain.notion.site/recruiting-note) |
| 工时制度 | 工程师采用裁量劳动制（裁量労働制），业务岗采用弹性工时；标准工作日 8 小时；有加班 | [招聘介绍页](https://medmain.notion.site/recruiting-note)、[Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519) |
| 薪资 | Fullstack Engineer（正式员工）：年薪 8,000,000–12,000,000 日元。Fullstack Engineer（业务委托）：每周 25–30 小时以上，月报酬 840,000–1,000,000 日元。AI Product Manager 和 R&D Business Development：年薪 10,000,000–12,000,000 日元 | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519)、[业务委托](https://open.talentio.com/r/1/c/medmain/pages/86431)、[AI PM](https://open.talentio.com/r/1/c/medmain/pages/127108)、[R&D BD](https://open.talentio.com/r/1/c/medmain/pages/127106) |
| 股权 | 满足规定在职期间的成员可获授股票期权 | [招聘介绍页](https://medmain.notion.site/recruiting-note) |
| 休假与试用 | 周末和节假日休息，年休 120 天以上；试用期 3 个月 | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519) |
| 福利 | 语言学习补贴、搬家费补助、交通费、定期体检 | [Fullstack](https://open.talentio.com/r/1/c/medmain/pages/114519) |
| 副业 | 不限制副业 | [招聘介绍页](https://medmain.notion.site/recruiting-note) |
| 团队概况 | 平均年龄 30 多岁后段 | [招聘介绍页](https://medmain.notion.site/recruiting-note) |
| 签证、应届生 | 查阅的职位均未说明 | — |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：medmain.com 的 sitemap 和 WordPress 文章索引（275 篇，2015-12 至 2026-10）、公司页面、产品页和情報公開页；service.medmain.com 的 sitemap、产品、FAQ 和案例页；recruit.medmain.com、Notion 招聘介绍页和 Talentio 应聘网站；PR TIMES 公司 feed（公司 ID 34505）；blog.medmain.com；TechMatrix 的 IR 公告列表及两份 TDnet 披露；国税厅法人番号公表网站；Europe PMC；以 `medmain`、`medmain-inc`、`medmaininc`、`pidport` 和 `medmain-ai` 进行的 GitHub 组织检索；Wantedly、Japan Dev，以及以メドメイン、Medmain 和 PidPort 进行的日英文网络检索。

- **PMDA 批准或认证。** 新闻索引和 PR TIMES feed 中均未见 Medmain 产品取得批准或认证的公告，现行产品页面将日本国内的 AI 解析描述为计划中。未以交互方式查询 PMDA 自身的器械数据库。
- **工程人数。** 未公布；唯一的总数是 2026-02-17 TechMatrix 披露中的 15 名员工。
- **2024 财年之后的营收及被收购后的业绩。** 未找到。
- **PidPort 机构版和扫描服务的价格。** 个别报价。
- **工程博客。** 未找到。官方博客 [Medmain Speaks](https://blog.medmain.com/) 最后更新于 2025-05-08（日文）和 2025-05-09（英文），分类为 news、people & culture 和 pathology；其人物文章均为 2020 年。
- **状态页、SLA、数据存放地声明。** 未找到。
- **签证支持和应届生招聘。** 未说明。

### 不同来源之间的不一致

- **医疗器械许可：** [2024-08-02 公告](https://prtimes.jp/main/html/rd/p/000000041.000034505.html)宣布取得第一種医療機器製造販売業许可，编号 13B1X10433，2024-07-02 颁发；[公司页面](https://medmain.com/aboutus/)（访问于 2026-10-11）列出的是第二種医療機器製造販売業，编号 13B2X10662。两处来源均未提及对方的编号。
- **资本金：** [公司页面](https://medmain.com/aboutus/)、[Talentio 职位](https://open.talentio.com/r/1/c/medmain/pages/114519)和 [PR TIMES 公司资料](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)为含资本准备金 11.9 亿日元；Medmain [2026-02-17 公告](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)正文和 [TechMatrix 披露](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)为資本金 1 亿日元。
- **累计融资：** 已公布各轮合计约 28.2 亿日元（1＋约 11＋3＋8.5＋4.7），而公司称股权累计为 25 亿日元（[2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)）。Series A2 公告称 8.5 亿日元一轮后累计 20.5 亿日元，意味着此前为 12 亿日元——与 [2020 年公告](https://prtimes.jp/main/html/rd/p/000000010.000034505.html)在 2022 年 PSP 投资 3 亿日元之前给出的数字相同。[BRIDGE](https://thebridge.jp/2020/08/medmain-series-a-round-funding) 称 2022 年后累计约 15 亿日元。
- **支持的文件格式：** PidPort 功能列表包括 vsi、isyntax 和 i2syntax；[FAQ](https://service.medmain.com/faq)列出 PNG、JPEG、TIFF、SVS 和 NDPI；[PidPort 页面](https://service.medmain.com/service/pidport)中的 FAQ 部分列出 JPEG、TIFF、SVS 和 NDPI，并称即将支持 Leica SCN。
- **PidPort Personal 发布日期：** medmain.com 于 [2026-07-01](https://medmain.com/news/65758/) 发布，PR TIMES 于 [2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html) 发布。

### 其他

- 业务除软件外还包括服务：切片扫描、与母公司集团共同开发的云 PACS，以及 2026 年推出的个人订阅。
- [2020-08-24 公告](https://prtimes.jp/main/html/rd/p/000000010.000034505.html)称日本国内 AI 解析的药事申请正在推进（薬事申請を進めています）；[2023-12-18 文章](https://medmain.com/news/34196/)以及 2024、2025 年公告将取得批准描述为目标；在查阅的资料中此后未见批准公告。
- Medmain 公告中引用的 PSP 客户数随时间不同：约 2,200 家机构（[2022-07-26](https://prtimes.jp/main/html/rd/p/000000024.000034505.html)）、2,300 多家（[2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)）、2,400 多家（[2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html)）和 2,600 家（[2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)）。
- 截至 2026-10-11，medmain.com 新闻索引最近 20 条中有 8 条是学术会议展位出展公告。

---

## 资料来源

**官方**

- [公司官网](https://medmain.com/)——[About us 与公司概况](https://medmain.com/aboutus/)、[产品](https://medmain.com/products/)、[情報公開（opt-out 通知）](https://medmain.com/disclosure/)
- [产品网站](https://service.medmain.com/service/pidport)——[PidPort Personal](https://service.medmain.com/service/personal)、[FAQ](https://service.medmain.com/faq)、[选择理由](https://service.medmain.com/reason)、[使用场景](https://service.medmain.com/scene)、[导入案例](https://service.medmain.com/case)
- [招聘网站](https://recruit.medmain.com/)——[CEO 寄语](https://recruit.medmain.com/message)、[招聘介绍页（Notion）](https://medmain.notion.site/recruiting-note)
- [应聘网站（Talentio）](https://open.talentio.com/r/1/c/medmain/homes/3686)——[Fullstack Engineer](https://open.talentio.com/r/1/c/medmain/pages/114519)、[Fullstack Engineer（业务委托）](https://open.talentio.com/r/1/c/medmain/pages/86431)、[AI Product Manager](https://open.talentio.com/r/1/c/medmain/pages/127108)、[R&D Business Development](https://open.talentio.com/r/1/c/medmain/pages/127106)
- [官方博客 Medmain Speaks](https://blog.medmain.com/)
- [GitHub 组织](https://github.com/medmain)

**新闻稿与公告（日文，较新在前）**

- [PidPort Personal（PR TIMES）— 2026-09-02](https://prtimes.jp/main/html/rd/p/000000056.000034505.html)
- [PidPort Personal（medmain.com）— 2026-07-01](https://medmain.com/news/65758/)
- [成为 TechMatrix 合并子公司 — 2026-05-01](https://medmain.com/news/63907/)
- [Ki-67 AI，Diagnostics 论文 — 2026-04-03](https://prtimes.jp/main/html/rd/p/000000055.000034505.html)
- [加入 TechMatrix 集团 — 2026-02-17](https://prtimes.jp/main/html/rd/p/000000054.000034505.html)
- [日経 NEXTユニコーン2025 — 2026-01-21](https://medmain.com/news/61450/)
- [常木入选 Top 2% Scientists — 2025-12-25](https://medmain.com/news/60752/)
- [所见文书专利 — 2025-12-24](https://prtimes.jp/main/html/rd/p/000000053.000034505.html)
- [Ha Dong General Hospital — 2025-10-20](https://prtimes.jp/main/html/rd/p/000000052.000034505.html)
- [Thống Nhất 医院 — 2025-09-12](https://medmain.com/news/57578/)
- [令和7年度 IPO Growth Program — 2025-09-03](https://medmain.com/news/57313/)
- [与 SMC 合作（越南）— 2025-08-01](https://prtimes.jp/main/html/rd/p/000000050.000034505.html)
- [越南医院合作备忘录 — 2025-07-25](https://prtimes.jp/main/html/rd/p/000000049.000034505.html)
- [出任 AI医療機器協議会理事 — 2025-06-17](https://medmain.com/news/54862/)
- [Mizuho Innovation Award — 2025-06-11](https://medmain.com/news/54666/)
- [鳥取大学 — 2025-05-21](https://medmain.com/news/53996/)
- [4.7 亿日元融资 — 2025-05-08](https://prtimes.jp/main/html/rd/p/000000046.000034505.html)
- [ISO 13485 — 2025-02-19](https://prtimes.jp/main/html/rd/p/000000045.000034505.html)
- [日経 NEXTユニコーン2024 — 2025-01-31](https://medmain.com/news/50364/)
- [Forbes JAPAN AI 50 — 2025-01-30](https://medmain.com/news/50262/)
- [超过半数医学部大学导入 — 2024-12-23](https://prtimes.jp/main/html/rd/p/000000044.000034505.html)
- [ISMS — 2024-11-29](https://prtimes.jp/main/html/rd/p/000000043.000034505.html)
- [病理版 NOBORI — 2024-10-31](https://prtimes.jp/main/html/rd/p/000000042.000034505.html)
- [IPO等に向けた成長支援プログラム — 2024-08-08](https://medmain.com/news/44474/)
- [第一種医療機器製造販売業許可 — 2024-08-02](https://prtimes.jp/main/html/rd/p/000000041.000034505.html)
- [Medteria 分拆 — 2024-08-01](https://medmain.com/news/52692/)
- [High Growth Program — 2024-08-01](https://medmain.com/news/44031/)
- [Series A2，8.5 亿日元 — 2024-04-18](https://prtimes.jp/main/html/rd/p/000000040.000034505.html)
- [JP-AID 胃活检 AI — 2023-12-18](https://medmain.com/news/34196/)
- [Japan Innovation Campus — 2023-11-22](https://prtimes.jp/main/html/rd/p/000000038.000034505.html)
- [久留米大学 — 2023-11-02](https://medmain.com/news/32208/)
- [AMED 项目 — 2023-09-07](https://prtimes.jp/main/html/rd/p/000000034.000034505.html)
- [U.S. Market Gateway Accelerator — 2023-09-06](https://prtimes.jp/main/html/rd/p/000000035.000034505.html)
- [加入 AI医療機器協議会 — 2023-04-17](https://medmain.com/news/25661/)
- [与 PSP 合作，3 亿日元 — 2022-07-26](https://prtimes.jp/main/html/rd/p/000000024.000034505.html)
- [NEDO 补助 — 2022-06-27](https://prtimes.jp/main/html/rd/p/000000023.000034505.html)
- [迁移学习基础技术 — 2021-07-09](https://medmain.com/news/2164/)
- [约 11 亿日元融资 — 2020-08-24](https://prtimes.jp/main/html/rd/p/000000010.000034505.html)
- [Forbes 30 Under 30 Asia — 2020-04-02](https://medmain.com/news/1743/)
- [PidPort 海外正式提供 — 2020-03-10](https://prtimes.jp/main/html/rd/p/000000009.000034505.html)
- [日本オープンイノベーション大賞 — 2020-02-19](https://medmain.com/news/1692/)
- [J-Startup — 2019-06-26](https://medmain.com/pressrelease/1563/)
- [Imaging Center 开业 — 2019-06-17](https://medmain.com/pressrelease/1552/)
- [起業家万博 総務大臣賞 — 2019-04-06](https://medmain.com/pressrelease/1504/)
- [飛躍 Next Enterprise — 2018-12-21](https://medmain.com/pressrelease/1441/)
- [PidPort α 版 — 2018-10-15](https://prtimes.jp/main/html/rd/p/000000004.000034505.html)
- [1 亿日元融资 — 2018-08-17](https://prtimes.jp/main/html/rd/p/000000003.000034505.html)
- [Medteria 推出 — 2018-06-11](https://prtimes.jp/main/html/rd/p/000000001.000034505.html)
- [Latitude59 — 2018-05-30](https://medmain.com/news/1037/)
- [Medmain USA Inc. — 2018-05-22](https://medmain.com/pressrelease/1023/)
- [公司成立 — 2018-01-11](https://medmain.com/pressrelease/829/) · [Medmain Inc. 设立 — 2018-01-11](https://medmain.com/pressrelease/748/)
- [Live Sharks Tank — 2017-11-24](https://medmain.com/news/672/)
- [OMEGA 入选九州大学支援项目 — 2017-05-24](https://medmain.com/pressrelease/324/)
- [九医クラウド — 2016-06-20](https://medmain.com/pressrelease/322/)
- [网站开设 — 2015-12-28](https://medmain.com/news/35/)

**监管机构与母公司披露**

- [国税庁 法人番号公表サイト — 2290001080259（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=2290001080259)
- [TechMatrix TDnet — 基本协议，2026-02-17（日文）](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260217563835_P01_.pdf)
- [TechMatrix TDnet — 股份转让协议，2026-04-24（日文）](https://www.techmatrix.co.jp/ir/upload_file/tdnrelease/3762_20260424510337_P01_.pdf)

**研究论文（经 Europe PMC）**

- [Medmain 署名论文检索](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AFF%3A%22Medmain%22&format=json&pageSize=100&resultType=lite)
- [胃与结肠上皮性肿瘤，Scientific Reports 2020](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6992793/fullTextXML)
- [多器官腺癌，PLOS ONE 2022](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9683606/fullTextXML)
- [Ki-67 标记指数，Diagnostics 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12984776/fullTextXML)

**第三方报道与档案**

- [BRIDGE — 2020 年融资（日文）](https://thebridge.jp/2020/08/medmain-series-a-round-funding) · [Series A2，2024-04-18（日文）](https://thebridge.jp/2024/04/medmain-series-a2-round-funding)
- [社長名鑑 — CEO 访谈（日文）](https://shachomeikan.jp/industry_article/3551)
