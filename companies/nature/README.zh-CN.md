# Nature

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Nature（Nature株式会社 / Nature Inc.，法人番号 4130001055679）是一家总部位于横滨的硬件与能源管理公司。官方公司页面给出的成立日期为 2014-12-10；CEO 称公司于 2014 年 12 月他就读哈佛商学院期间首先在美国登记，日本法人在 2019-08-07 之前名为 Nature Japan株式会社。公司销售智能红外遥控器 **Nature Remo**、家庭能源管理系统 **Nature Remo E**（HEMS，公司称之为“スマホHEMS”）、EV 充电控制器 **Nature EV Switch** 和智能门锁 **Nature Lock**，均通过“Nature Home”应用使用；另外向电力零售商提供需求响应（DR）支援服务，并提供云 API。

- 规模：Nature Remo 系列“累計販売台数80万台を超える”（累计销量超过 80 万台）（[2026-10-01 公告](https://nature.global/press/release/28318/)）；一则后端职位称已有超过 45 万台 IoT 设备连接到 Nature Remo 云（[后端工程师职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)，datePosted 2025-05-16；访问于 2026-10-11）。
- 融资：最近公布的一轮为 **シリーズD**，合计约 12.2億円（2024 年 2 月完成的 10.2億円，加上脱炭素化支援機構未披露金额的追加出资，于 [2024-06-27](https://nature.global/press/release/20904/) 公布）。BRIDGE 称成立以来已公开的融资额超过 25億円（[BRIDGE，2024-06-28](https://thebridge.jp/2024/06/nature-series-d2-round-funding)）。截至 2026-03-31 财年的法定决算公告显示净亏损 1億9561万円（[官報決算データベース](https://catr.jp/companies/9dfc0/74413)）。
- 团队：含业务委托和实习生共 56 人（[公司页面](https://nature.global/about/)；无日期，访问于 2026-10-11）；公司介绍资料称员工 45 人，软件工程师占全职岗位的 38%（[公司介绍资料](https://speakerdeck.com/naturepr/company-information)，修改于 2026-05-31）。
- 工程：后端为运行在 AWS（ECS、Aurora MySQL、ElastiCache Redis、DynamoDB）上的 Go，应用为 React Native/TypeScript，固件为 ESP32/ESP-IDF 上的 C/C++，职位中也列出 Rust；设备使用 Wi-Fi、BLE、Wi-SUN、LTE-M、Matter 和 ECHONET Lite 通信（[工程博客，2021-04-29](https://engineering.nature.global/entry/start-blog)、[固件工程师职位](https://herp.careers/v1/nature/km0uZc0P_FSl)，datePosted 2026-09-18）。职位均以日语撰写，后端工程师职位要求母语级日语；工程岗位可完全远程，每月约有一天全员到岗日（[职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)；访问于 2026-10-11）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前公开品牌 | Nature（产品品牌 Nature Remo、Nature Remo E、Nature EV Switch、Nature Lock / Nature Key、Nature Green；应用“Nature Home”） | [nature.global](https://nature.global/)；访问于 2026-10-11 |
| 法定名称 | Nature株式会社（Nature Inc.）；フリガナ ネイチャー；法人番号 4130001055679 | [公司页面](https://nature.global/about/)、[国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679)（2026-10-11 时点信息） |
| 曾用法定名称 | Nature Japan株式会社（ネイチャージャパン），于 2019-08-07 更名为 Nature株式会社 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) |
| 成立 | “設立：2014年12月10日” | [公司页面](https://nature.global/about/)；无日期，访问于 2026-10-11 |
| 总部 | 〒221-0052 神奈川県横浜市神奈川区栄町1-1 KDX横浜ビル 11F（自 2021-12-20 起登记地址为栄町1番地1） | [公司页面](https://nature.global/about/)、[国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) |
| 实验室／保养所 | 〒259-0304 神奈川県足柄下郡湯河原町宮下698-15 “Smart Energy Lab” | [公司页面](https://nature.global/about/) |
| 代表人 | 代表取締役 塩出 晴海（Haruumi Shiode） | [公司页面](https://nature.global/about/) |
| 公司页面所列业务 | “IoT機器の開発・製造・販売、及びエネルギーマネジメント事業” | [公司页面](https://nature.global/about/) |
| 员工人数 | “56名（業務委託、インターン含む）” | [公司页面](https://nature.global/about/)；无日期，访问于 2026-10-11 |
| 资本 | “25.8億円（資本剰余金含む）” | [HERP 公司信息栏](https://herp.careers/v1/nature/F06a8ZG7ncFG)、[公司介绍资料](https://speakerdeck.com/naturepr/company-information)（修改于 2026-05-31） |
| 销量 | Nature Remo 系列：累计销量超过 80 万台 | [2026-10-01 公告](https://nature.global/press/release/28318/) |
| 累计融资 | 成立以来公开披露的金额超过 25億円（媒体数字）；见“融资” | [BRIDGE，2024-06-28](https://thebridge.jp/2024/06/nature-series-d2-round-funding) |
| 公司列出的股东 | 環境エネルギー投資、脱炭素化支援機構（JICN）、KDDI Green Partners Fund、東京ガス、ENEOS、Daikin、Delight Ventures（DeNA）、MUFJ Capital、博報堂DYV“他” | [公司介绍资料](https://speakerdeck.com/naturepr/company-information)（修改于 2026-05-31） |
| 安全认证 | ISO/IEC 27001:2022，登录证编号 16297，认证机构 Intertek Certification，登录日 2026-02-20；范围为总部和 Smart Energy Lab | [2026-03-09 公告](https://nature.global/press/release/26121/) |
| 产品安全标签 | Nature Remo E / E lite / E2 / E2 lite 取得 JC-STAR ★1（2025-10-10 公布），Nature EV Switch 亦已取得 | [2025-10-10 公告](https://nature.global/press/release/25287/)、[2025-10-31 公告](https://nature.global/press/release/25360/) |
| 能源相关登记 | 2026-08-06 登记为“東京都家庭用アグリゲーター”（东京都家庭用聚合商） | [2026-08-24 公告](https://nature.global/press/release/27984/) |

### 品牌与法律实体

| 名称 | 类型 | 法域／期间 | 来源所述关系 | 来源 |
|---|---|---|---|---|
| Nature株式会社（Nature Inc.） | 当前法律实体 | 日本；法人番号 4130001055679 | 当前所有公告、条款和 API 文档中署名的运营公司 | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679)、[条款](https://terms.nature.global/ja/) |
| Nature Japan株式会社 | 同一实体的曾用法定名称 | 日本；至 2019-08-07 | 法人番号相同；登记地址依次为 京都市左京区 → 東京都渋谷区桜丘町（2017-12-15）→ 渋谷区広尾（2018-08-23）→ 渋谷区宇田川町（2020-03-27）→ 横浜市神奈川区（2021-12-20） | [国税庁](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679) |
| 美国公司（“Nature, Inc.”） | 前身或关联实体；法律关系未说明 | 美国；据 CEO 所述于 2014 年 12 月登记 | CEO：“2014年12月、アメリカで会社を登記し、Natureは誕生しました”。2019 年融资公告称总部职能已全部迁至日本，并以“Nature 株式会社として”重新出发 | [CEO 访谈，2025-12-04（日文）](https://note.com/nature_global/n/n3a9457ec0239)、[2019-08-01 公告](https://nature.global/press/release/566/) |

查阅的来源均未说明该美国公司是否已被合并、注销，或仍是日本实体的母公司或子公司，也未说明 Nature Japan株式会社的设立日期。

**项目、登记与奖项：** 入选 500 KOBE ACCELERATOR（[2017-08-14](https://nature.global/press/news/1312/)）和 Google for Startups Accelerator Class 3（[2021-01-07](https://nature.global/press/release/3816/)）；与关西电力一起参加平成29年度虚拟电厂实证事业（[2017-07-25](https://nature.global/press/news/513/)）。Nature Remo E 获 iF Design Award 2020（[2020-02-05](https://nature.global/press/news/1426/)），Remo 3、Remo mini 2 和 Remo E lite 获 2021 年该奖（[2021-04-15](https://nature.global/press/release/5025/)）；Nature Remo Lapis 获グッドデザイン賞 2024（[2024-10-16](https://nature.global/press/release/22036/)）；入选 Forbes JAPAN“次世代GX企業50選”能源管理部门（[2025-08-14](https://nature.global/press/news/24875/)）。电力零售：电力・燃气交易监视等委员会（電力・ガス取引監視等委員会）于 2020-11-04 答复，对将 Nature株式会社登记为“小売電気事業を営もうとする者”无异议（[答复](https://www.egc.meti.go.jp/info/public/pdf/20201104001b.pdf)、[申请者一览](https://www.egc.meti.go.jp/info/public/pdf/20201104001c.pdf)）；见“备注”。

### 公司陈述的市场背景

- Series D 公告引用政府为 2050 年碳中和设定的“可再生能源占电源结构 50% 以上”目标，并将需求表述为：提高用户侧的自家消费率，以及为电网运营方提供灵活的需求调节能力（[2024-02-07](https://nature.global/press/release/18339/)、[2024-06-27](https://nature.global/press/release/20904/)）。
- 当前职位将 GX 政策和需給調整市場（平衡市场）的建设称为“制度の追い風”（制度顺风）（[后端工程师职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)）。
- 公司将 2022 年退出电力零售归因于 JEPX 采购价格飙升（LNG 短缺、乌克兰战争、地震）（[2022-04-11](https://nature.global/press/release/8397/)）。
- 《ERAB 网络安全指南 Ver3.0》（2025-05-22 修订）规定，作为 ERAB 控制对象的 IoT 设备必须达到 JC-STAR ★1 以上，公司据此说明其标签取得（[2025-10-10](https://nature.global/press/release/25287/)）。

---

## 产品

网站导航将产品分为ホームオートメーション（家庭自动化）和エネルギーマネジメント（能源管理），另设“法人のお客様”（企业客户）栏目（[nature.global](https://nature.global/)；访问于 2026-10-11）。

### 产品阵容

| 产品 | 领域 | 内容 | 发布／关键日期 |
|---|---|---|---|
| Nature Remo 系列（Lapis、Remo 3、Remo mini 2、Remo nano） | 家庭自动化 | Wi-Fi 智能红外遥控器；Remo 3 带温度、湿度、照度和人感传感器；Remo nano 支持 Matter；Lapis 增加自动空调节电（“オートエコ”） | 首代 Remo 于 [2017-10-16](https://nature.global/press/release/522/) 开售；Remo 3 [2020-08-05](https://nature.global/press/release/606/)；nano [2023-07-04](https://nature.global/press/release/15936/)；Lapis [2024-07-05](https://nature.global/press/release/21289/) |
| Nature Lock / Nature Key | 家庭自动化 | 智能门锁，附带支持免手动开锁和 Apple“查找”的钥匙扣；硬件和基础固件由索尼网络通信的 Qrio Lock 设计提供，在日本国内开发和制造 | [2026-04-21](https://nature.global/press/release/26546/) 发布；[2026-04-30](https://nature.global/press/release/26672/) 一般销售 |
| Nature Remo E2 / E2 lite（及早期的 Remo E / E lite） | 能源管理 | 插电式 HEMS，经 Wi-SUN B 路线读取智能电表，并控制 ECHONET Lite 设备（光伏、蓄电池、V2H、EcoCute、Ene-Farm、空调）；“lite”型号仅监测 | Remo E [2019-12-10](https://nature.global/press/release/578/) 预售；E lite [2020-04-28](https://nature.global/press/release/589/)；E2 [2025-04-08](https://nature.global/press/release/24003/) |
| Nature EV Switch | 能源管理 | 经 LTE-M 联网的 200V EV 充电插座控制器：监测、远程启停、定时、天气联动及光伏余电充电 | 自 2025 年用于松下服务（[2025-02-25](https://nature.global/press/release/23308/)）；[2025-10-31](https://nature.global/press/release/25360/) 面向企业销售；[2026-03-10](https://nature.global/press/release/26117/) 面向个人销售并提供安装服务 |
| Nature Green | 能源管理（软件） | 应用内自动化：与 JEPX 价格联动的空调和蓄电池控制、按天气预报的 EcoCute 烧水、V2H 定时、“スマートEV充電 for Tesla” | 首个付费选项 [2023-08-08](https://nature.global/press/release/16586/)；Tesla 选项 [2026-09-24](https://nature.global/press/release/28217/) |
| デマンドレスポンス支援サービス | 企业（电力零售商） | 面向零售商的 DR 运营：行为改变型 DR 与设备控制型 DR（空调、EcoCute、蓄电池），管理后台，JEPX 联动触发，结果报告 | 2022 年夏由关西电力首次采用（[2022-06-28](https://nature.global/press/release/9771/)）；[2025-07-01](https://nature.global/press/release/24645/) 改版 |
| Nature API | 企业／开发者 | Cloud API、Local API、Remo E ECHONET Lite API、OAuth2/OpenID Connect 提供方 | Remo API 于 [2018-02-01](https://nature.global/press/news/1361/) 公开；面向企业的付费 Remo E API [2021-01-05](https://nature.global/press/release/3811/) |

已停止的服务：**Natureスマート電気**，一项价格随供需变动的电力零售服务，于 [2021-03-01](https://nature.global/press/release/4320/) 在东京电力和关西电力区域推出，至 [2021-07-06](https://nature.global/press/release/5591/) 扩展至全国（冲绳及离岛除外），于 2022-06-30 停止供电（[2022-04-11](https://nature.global/press/release/8397/)）。

### 商业化

- **硬件**通过公司 Shopify 商店、Amazon.co.jp、乐天和家电量贩店销售，公开标价，企业客户可按数量咨询特别价格（[企业页面](https://nature.global/business/)；访问于 2026-10-11）。自 2026-10-01 起，在官方商店、乐天和亚马逊购买的 Remo 若无法实现空调基本操作，可获退款保证（[2026-10-01](https://nature.global/press/release/28318/)）。
- **Nature Green** 由免费选项和按月付费选项组成，价格列于 [Nature Green 页面](https://shop.nature.global/pages/nature-green)（访问于 2026-10-11）。
- **B2B**：DR 支援服务和 Nature API 的商业使用均需咨询，未公开价格（[API 页面](https://nature.global/business/api-remo/)）。开发者门户规定企业仅可“商用利用前の検証段階に限り”（在商用前验证阶段）使用 API，商用需另行咨询（[开发者门户](https://developer.nature.global/)）。EV Switch 也以模块（EVSW-6B1-P）形式供应给松下的“おうちEV充電サービス”（[2026-03-10](https://nature.global/press/release/26117/)）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2016-06-03 | Kickstarter：10 天筹得 5 万美元 | [公告](https://nature.global/press/release/456/) |
| 2018-02-19 | Kickstarter、Makuake 和 Indiegogo 合计筹得“総額2000万円以上” | [公告](https://nature.global/press/release/524/) |
| 2019-08-01 | Nature Remo 系列：累计 10 万台 | [公告](https://nature.global/press/release/566/) |
| 2020-09-16 | Remo 与 Remo E 系列合计：累计 20 万台；用户调查 NPS 为 30 | [公告](https://nature.global/press/release/615/) |
| 2021-04-15 | Remo 与 Remo E 系列合计：30 万台 | [公告](https://nature.global/press/release/5025/) |
| 2022-04-11 | Nature Remo：超过 40 万台 | [公告](https://nature.global/press/release/8397/) |
| 2023-07-04 | Nature Remo：60 万台 | [公告](https://nature.global/press/release/15936/) |
| 2024-06-27 | Nature Remo：超过 65 万台 | [公告](https://nature.global/press/release/20904/) |
| 2026-05-31（资料修改日） | Remo 与 Remo E 系列合计：“800,000台突破”；Nature Home 应用有“数十万人”使用 | [公司介绍资料](https://speakerdeck.com/naturepr/company-information) |
| 2026-10-01 | Nature Remo：超过 80 万台 | [公告](https://nature.global/press/release/28318/) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2022-06-28](https://nature.global/press/release/9771/) | 関西電力 | DR 支援服务的首个客户（2022 年夏）；此后各季继续采用，自 [2024-06-25](https://nature.global/press/news/20713/) 起全年采用 |
| [2022-12-23](https://nature.global/press/release/12753/) | NTTドコモ | DR 合作；Nature 的自动节电技术用于“ドコモでんき自動エコモード”（[2024-03-04](https://nature.global/press/release/18635/)） |
| [2023-02-13](https://nature.global/press/release/13793/) | オクトパスエナジー | DR 支援服务 |
| [2024-04-18](https://nature.global/press/release/19564/) | 東京ガス | 利用家庭 DER 开展 DR 的业务合作；自 [2025-04-01](https://nature.global/press/release/23974/) 起提供 DR 支援服务 |
| [2024-06-26](https://nature.global/press/release/20279/) | auエネルギー＆ライフ | “スマート節電 with Nature Green” |
| [2024-10-30](https://nature.global/press/release/22262/) | Shizen Connect | 云对云方式对 Nature Remo E 家庭进行 VPP 控制 |
| [2025-02-25](https://nature.global/press/release/23308/) | パナソニック エレクトリックワークス社 | Nature EV Switch 模块用于“おうちEV充電サービス” |
| [2025-09-04](https://nature.global/press/release/25064/) | 東京ガス、三菱自動車 | 东京都项目下的 EV 远程充电控制实证 |
| [2025-12-25](https://nature.global/press/release/25801/) | 世田谷区 | 2025 年 7–8 月节能实证结果（用电量减少 2.52%） |
| [2026-04-21](https://nature.global/press/release/26546/) | ソニーネットワークコミュニケーションズ | 为 Nature Lock 提供 Qrio Lock 的设计与技术 |

### 公开计划

- Series D 资金用途：构建控制分布式能源资源的“Nature DER Platform”，通过合作企业（包括投资方）扩大普及，以及招聘（[2024-02-07](https://nature.global/press/release/18339/)、[2024-06-27](https://nature.global/press/release/20904/)）。
- 随 Nature Lock 发布公布的中期愿景：“統合的なスマートホームの体験を提供し、快適でサステナブルな暮らしを実現する”（[2026-04-21](https://nature.global/press/release/26546/)）。
- 公司介绍资料的路线图显示面向 2030 年的“Nature V2H”和“Nature蓄電池”，并注明“想定のものであり、今後変更の可能性があります”（为设想，今后可能变更）（[公司介绍资料](https://speakerdeck.com/naturepr/company-information)）。
- 后端工程师职位预计联网设备将“数年で”（在数年内）突破 100 万台（[职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)）；劳务总务职位称公司正“数年後のIPOを見据えて”（着眼于数年后 IPO）完善内部体制（[职位](https://herp.careers/v1/nature/A6An3g_K1bIS)，datePosted 2025-11-26）。

---

## 创始人

**塩出 晴海（Haruumi Shiode）**——创始人、代表取締役 CEO（[公司页面](https://nature.global/about/)、[团队页面](https://nature.global/careers/team/)）。

- 就读北海道大学工学部，期间赴威斯康星大学麦迪逊分校交换；2008 年在瑞典皇家理工学院（KTH）完成计算机科学硕士（[CEO 访谈（日文）](https://note.com/nature_global/n/n3a9457ec0239)、[团队页面](https://nature.global/careers/team/)）。
- 三井物产：从事发展中国家电力项目投资与开发，包括印度尼西亚燃煤电站项目（[团队页面](https://nature.global/careers/team/)、[CEO 访谈（日文）](https://note.com/nature_global/n/n3a9457ec0239)）。
- 2016 年完成哈佛商学院 MBA；在哈佛就读期间创立 Nature，于 2014 年 12 月在美国登记公司（[团队页面](https://nature.global/careers/team/)、[CEO 访谈（日文）](https://note.com/nature_global/n/n3a9457ec0239)）。
- 长篇访谈：[立志編（日文），2025-12-04](https://note.com/nature_global/n/n3a9457ec0239)、[組織・カルチャー編（日文），2025-12-04](https://note.com/nature_global/n/nb47e66f7c43d)。

**大塚 雅和（Masakazu Ohtsuka）**——共同创始人；在[公司介绍资料](https://speakerdeck.com/naturepr/company-information)（修改于 2026-05-31）中列为“Co-founder and CTO”。

- 2000 年起任职松下（车载导航固件），2007 年起任职 Kayac，2013 年起独立；个人开发并销售学习型遥控器 IRKit，之后开发了首代 Nature Remo（[访谈，2022-08-18（日文）](https://note.com/nature_global/n/n6c8b703cdc85)、[团队页面](https://nature.global/careers/team/)）。
- Remo 发售后离开 Nature 赴爱沙尼亚工作，约四年后于 2022 年回归（[访谈，2022-08-18（日文）](https://note.com/nature_global/n/n6c8b703cdc85)）；于 [2023-07-19](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown) 写道“7月からCTOに復帰しました”。团队页面称其居住在爱沙尼亚。

### 主要管理层

| 姓名 | 所列职位 | 公开背景 | 来源 |
|---|---|---|---|
| Tomomi Nagao（長尾） | 设计师；创意总监 | 京瓷（手机、IoT 产品）；2018 年加入，“創業時より”参与产品设计；CEO 称長尾为早期工业设计负责人 | [团队页面](https://nature.global/careers/team/)、[CEO 访谈（日文）](https://note.com/nature_global/n/n3a9457ec0239) |
| Ryo Takei | Corporate Lead | 注册会计师；德勤 Tohmatsu 审计；曾任一家 SaaS 公司财务经理部长及 IPO 准备负责人；2025-02 加入 | [团队页面](https://nature.global/careers/team/) |
| Shikhar Ghosh | Advisor | 未说明 | [团队页面](https://nature.global/careers/team/) |

本表姓名按团队页面的罗马字写法列出。[2019-11-17](https://nature.global/press/release/575/) 任命的技术顾问：川崎 修平（前 DeNA 董事兼 CTO）和 [阿部 力也](https://nature.global/press/release/572/)（Digital Grid Consortium）；宇野 雄（Cookpad）随 [2021-07-14](https://nature.global/press/release/5754/) 一轮融资出任设计顾问。工程博客首篇文章（2021-04-29）由被称为 VPoE 的“Songmu”撰写（[文章](https://engineering.nature.global/entry/start-blog)）；当前团队页面未列出 Songmu。

团队页面列出的岗位包括负责固件、移动端、服务器和 SRE 的软件工程师，以及硬件工程、设计、客户支持、业务开发、HR、市场/数据分析、产品市场和公司职能（[团队页面](https://nature.global/careers/team/)；访问于 2026-10-11）。2025 年 12 月，公司结束四年的合弄制（holacracy）运营，转为“Hybrid型組織”：在职能型圈子中设置经理，项目型圈子仍按合弄制运营（[HR note，2025-12-19（日文）](https://note.com/nature_global/n/n26cb9d5921ec)）。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2018-02-19 | 第三者割当増資 | 1億円 | 大和企業投資 | — | [公告](https://nature.global/press/release/524/) |
| 2019-08-01（2019-07-31 完成） | 第三者割当増資 | 5億円 | 環境エネルギー投資、ディー・エヌ・エー（拟转至 Delight Ventures） | — | [公告](https://nature.global/press/release/566/) |
| 2021-07-14 | 第三者割当増資 | 7.5億円 | 環境エネルギー投資、大和企業投資 | — | [公告](https://nature.global/press/release/5754/) |
| 2024-02-07 | 第三者割当増資；后被称为シリーズDラウンド | 約10.2億円 | 東京ガス、EEI4号イノベーション&インパクト投資事業有限責任組合（環境エネルギー投資）、KDDI Green Partners Fund（SBIインベストメント）、ダイキン工業、ENEOSイノベーションパートナーズ、HAKUHODO DY FUTURE DESIGN FUND 2号（博報堂DYベンチャーズ）、三菱UFJキャピタル9号、Yokohama Next 投資事業有限責任組合（横浜キャピタル） | — | [公告](https://nature.global/press/release/18339/) |
| 2024-06-27 | シリーズDラウンド（追加交割） | 未披露；Series D 合计約12.2億円 | 脱炭素化支援機構（JICN） | “25億円を超えた”（BRIDGE，仅计已公开金额） | [公告](https://nature.global/press/release/20904/)、[BRIDGE](https://thebridge.jp/2024/06/nature-series-d2-round-funding) |

- 公司首次使用轮次标签是在 2024 年 6 月的公告中（“2024年2月より実施しているシリーズDラウンド”）；2018、2019 和 2021 年的公告只使用“第三者割当増資”，未找到公司将任何一轮称为 Series A、B 或 C 的来源。
- 環境エネルギー投資参与了 2019、2021 和 2024 年融资；大和企業投資参与了 2018 和 2021 年融资。2019 年公告称 DeNA 的持股将转至 Delight Ventures，公司介绍资料现将其列为“Delight Ventures（DeNA）”。
- 众筹（2016 年 Kickstarter、2016 年 Makuake、Indiegogo）据公司称合计超过 2000万円，未计入上表（[2018-02-19](https://nature.global/press/release/524/)）。
- 2024-02 一轮与“Nature DER Platform”计划同时公布；2021 年一轮与进入电力零售及任命设计顾问同时公布。

### 法定决算公告（決算公告）

以下数字为[官報決算データベース](https://catr.jp/companies/9dfc0/74413)转录的官报決算公告（访问于 2026-10-11）。公开的公告中不包含营收。

| 财年截止日 | 净利润 | 利润剩余 | 总资产 |
|---|---|---|---|
| 2026-03-31（第11期，2026-07-30 刊登） | ▲1億9561万円 | ▲15億8649万6000円 | 11億7459万8000円 |
| 2025-03-31（第10期，2025-07-30 刊登） | ▲3億927万7000円 | ▲13億9088万6000円 | 12億9620万4000円 |
| 2024-03-31 | ▲5億1040万円 | ▲10億8160万9000円 | 14億6000万2000円 |
| 2023-03-31 | ▲3億2341万5000円 | ▲5億6559万5000円 | 9億4373万9000円 |
| 2022-03-31 | ▲2億8676万4000円 | ▲2億2620万8000円 | 12億9255万5000円 |
| 2021-03-31 | 346万5000円 | 6502万9000円 | 6億6136万円 |

---

## 工程

### 技术栈与平台

**由公司技术文章和公开资产确认：**

- **后端：**“ほぼすべてGo”（几乎全部为 Go）；Lambda 和 Cloud Functions 上使用 Node.js（[博客，2021-04-29](https://engineering.nature.global/entry/start-blog)）。据 CTO 所述，后端是一个 Go monorepo（[博客，2026-07-31](https://engineering.nature.global/entry/2026/07/prove-pure-refactoring-with-ai-and-auto-merge)）。[`natureglobal`](https://github.com/natureglobal) 下的公开 Go 仓库包括 `firequeue`（Kinesis Data Firehose 队列）和 `realip`。
- **云：** AWS——ECS（Fargate）、ALB、Aurora MySQL、ElastiCache Redis（缓存与 Pub/Sub）、用于时序数据的 DynamoDB、Kinesis Data Firehose、Glue/Parquet、Lambda、Amplify；Terraform；Datadog。部分集成使用 Google Cloud Functions 和 Firebase（[博客，2021-04-29](https://engineering.nature.global/entry/start-blog)、[博客，2024-04-02](https://engineering.nature.global/entry/2024/04/02/101743)）。一份故障报告提到 AWS US-EAST-1 区域和 ECS Fargate（[2024-07-31](https://nature.global/press/news/21522/)）。
- **移动端：** iOS 和 Android 使用 React Native 与 TypeScript（[博客，2021-04-29](https://engineering.nature.global/entry/start-blog)），并有原生小组件（[博客，2022-12-06](https://engineering.nature.global/entry/add-native-widget-to-react-native-app)）。
- **固件：** 微控制器上使用 C（[博客，2021-04-29](https://engineering.nature.global/entry/start-blog)）；ESP-IDF，单元测试在 FreeRTOS POSIX 移植环境下用 Catch2 运行（[博客，2022-12-02](https://engineering.nature.global/entry/freertos-catch-part1)）；GitHub 上有 `esp-idf`、`esp-nimble` 和 `FreeRTOS-Kernel` 的 fork。两名固件工程师合著了《基礎から学ぶ 組込みRust》（[博客，2021-05-07](https://engineering.nature.global/entry/embedded-rust-from-basics)）。
- **设备协议：** Wi-Fi、BLE、用于智能电表 B 路线的 Wi-SUN（920MHz）、LTE-M（EV Switch）、Matter（Remo nano）、ECHONET Lite（[Remo E2 公告](https://nature.global/press/release/24003/)、[EV Switch 公告](https://nature.global/press/release/26117/)、[Remo nano 公告](https://nature.global/press/release/15936/)）。
- **公开 API：** `api.nature.global` 上的 HTTPS/JSON Cloud API（OpenAPI 3.0.3），OAuth2 Bearer 令牌和 OpenID Connect 提供方；设备上的 Local API 通过 Bonjour `_remo._tcp` 发现（[开发者门户](https://developer.nature.global/)、[Cloud API 规范](https://swagger.nature.global/)、[Local API 规范](https://local-swagger.nature.global/)）。
- **运维工具：** 状态页基于 Atlassian Statuspage（[status.nature.global](https://status.nature.global/)，2026-10-11 检查响应头）；CI 使用 GitHub Actions 调用 Claude（Claude Code 和 Claude API）验证仅含重构的 PR（[博客，2026-07-31](https://engineering.nature.global/entry/2026/07/prove-pure-refactoring-with-ai-and-auto-merge)）。

**当前职位所列**（招聘证据；访问于 2026-10-11）：

- 后端：Go、AWS、Docker、ECS、MySQL（RDS）、Redis（ElastiCache）、CircleCI、GitHub、Zenhub、Slack（[后端工程师](https://herp.careers/v1/nature/F06a8ZG7ncFG)）。
- 固件：C、C++（C++17–C++23）、Rust；Wi-Fi、BLE、LTE、Wi-SUN；HTTP、WebSocket、Matter、ECHONET-Lite；ESP32 系列与 ESP-IDF；Ubuntu 主机；GitHub Actions；LLM 工具 GitHub Copilot、Claude Code、Devin、Gemini、NotebookLM（[固件工程师](https://herp.careers/v1/nature/km0uZc0P_FSl)）。
- 移动端：React Native、TypeScript、Swift、Kotlin、Java；CircleCI（[智能手机应用工程师](https://herp.careers/v1/nature/dhj2CBULhCSH)）。
- 公司介绍资料将 AWS 和 GCP 列为云平台，并将 ChatGPT、Claude Code、Claude Cowork、Gemini、Devin 和 Cursor 列为 AI 工具（[公司介绍资料](https://speakerdeck.com/naturepr/company-information)）。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 设备连接 | Remo 设备与 ALB 后方 ECS 上的 8 台 Go“stream”服务器保持长连接 WebSocket（“ウン十万接続”）；使用 ALB 蓝绿部署时，设备约在 24–36 小时内迁移到新 ALB，文章介绍了部署时逐步断开 stream 服务器连接的做法 | [博客，2023-07-19](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown) |
| 红外信号数据库 | 由员工购买遥控器实物，用自研分析工具“Nature Learn”采集空调信号；部分厂商提供官方数据补充；空调识别以 `/1/detectappliance` 接口公开 | [2026-06-18](https://nature.global/press/release/27356/)、[Cloud API 规范](https://swagger.nature.global/) |
| 本地控制 | 云端不可用时通过家庭 Wi-Fi 操作空调，在 2024 年 7 月两次故障后推出 | [2024-07-11](https://nature.global/press/news/21359/)、[2025-02-12](https://nature.global/press/release/22669/) |
| HEMS／DER 控制 | Remo E 读取智能电表和 ECHONET Lite 设备数据，控制蓄电池、V2H、EcoCute 和 Ene-Farm；Remo E2 支持分电盘计量类，无需申请 B 路线 | [2026-08-24](https://nature.global/press/release/27984/)、[Remo E API 文档](https://developer.nature.global/docs/nature-remo-e-api-specification/) |
| 市场联动自动化 | 与 JEPX 区域价格联动的空调和蓄电池控制；按天气和发电量的 EcoCute 烧水；光伏余电 Tesla 充电 | [Nature Green 页面](https://shop.nature.global/pages/nature-green)、[2026-09-24](https://nature.global/press/release/28217/) |
| DR 支援平台 | 零售商管理后台：登记 DR 事件、JEPX 联动自动触发、参与者邮件、基于速报值和确报值的结果报告；支持“上げDR”和“下げDR” | [2025-07-01](https://nature.global/press/release/24645/) |
| 聚合商集成 | 云对云连接：Shizen Connect 制定 VPP 控制计划，Nature 在家庭 DER 上执行 | [2024-10-30](https://nature.global/press/release/22262/) |
| EV 充电控制 | LTE-M 继电器控制器；API 继电器操作每台设备每天限 10 次；符合特定計量制度要求（显示功能尚未实现） | [Cloud API 规范](https://swagger.nature.global/)、[2026-03-10](https://nature.global/press/release/26117/) |
| 数据管道 | 通过 `firequeue` 向 Kinesis Data Firehose 写入（异步批处理使平均 API 延迟从 42.8 ms 降至 23.4 ms）；用 Glue/Parquet 做分析 | [博客，2024-04-02](https://engineering.nature.global/entry/2024/04/02/101743)、[博客，2021-04-29](https://engineering.nature.global/entry/start-blog) |
| 固件发布工具 | 分阶段固件发布的 CLI | [博客，2022-12-09](https://engineering.nature.global/entry/staged-firmware-release-cli) |

### 招聘所需技术背景

来自当前 HERP 职位（访问于 2026-10-11）：

- **后端，必需：** 使用 Go、Ruby、Perl、Python、Java 等进行服务端开发；开发并运营“中規模以上（目安ユーザー規模1万人）”的 Web 应用；理解评审和测试文化；能从零构建包括系统在内的应用；母语级日语；对 IoT 有兴趣。**优先：** 多种 AWS 服务、微服务式分布式系统、OSS 贡献、IoT 产品开发、敏捷/Scrum（[职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)）。
- **固件，必需：** 使用 C 和 C++11 及以上进行嵌入式开发；TCP/IP 和 HTTP 基础；评审和测试文化。**优先：** IoT 产品、电路设计、Web 或移动开发、OSS、敏捷、Rust（[职位](https://herp.careers/v1/nature/km0uZc0P_FSl)）。
- **移动端，必需：** 与后端联动的 iOS 和 Android 应用开发，规模相当。**优先：** 后端开发、React Native 或 Flutter、BLE 设备联动、OSS、敏捷（[职位](https://herp.careers/v1/nature/dhj2CBULhCSH)）。
- 职位称目前工程师兼任基础设施、后端、移动端和嵌入式工作，并期望在需要时承担主要领域以外的任务（[后端职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)）。

### 行业领域

日本家庭能源：智能电表与 Wi-SUN B 路线、ECHONET Lite 设备类、JEPX 现货价格、DR（行为改变型与设备控制型，上调与下调）、VPP 与聚合、需給調整市場、ERAB 网络安全指南与 JC-STAR、特定計量制度，以及国家和东京都的补贴项目（GX志向型住宅、家庭蓄电池和 EV 充电设备补贴）（[2025-04-08](https://nature.global/press/release/24003/)、[2025-10-10](https://nature.global/press/release/25287/)、[2026-08-24](https://nature.global/press/release/27984/)）。业务开发岗“012”要求能源行业经验，销售岗要求五年以上能源产品销售经验（[业务开发职位](https://herp.careers/v1/nature/OZuuB4z-0YYb)、[销售职位](https://herp.careers/v1/nature/rxhJK_Wv9hzU)）；工程职位未将能源领域知识列为必需，工程实习职位在“求める人物像”中列出对 IoT 产品或电力系统的兴趣（[职位](https://herp.careers/v1/nature/YqFSO9OIdsxs)）。公司介绍资料称 6% 的全职员工来自能源行业（[公司介绍资料](https://speakerdeck.com/naturepr/company-information)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 所有职位均以日语撰写。后端：要求“ネイティブレベルの日本語力”。工程实习：须能阅读英文技术文档。招聘兼 CEO 秘书：要求英文文字沟通。未公开公司语言政策 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG)、[实习](https://herp.careers/v1/nature/YqFSO9OIdsxs)、[招聘](https://herp.careers/v1/nature/rdeGy2njtW2B) |
| 构成 | 外籍员工占 10%；30 多岁 57%，40 多岁 31%；男女比例 3:1 | [公司介绍资料](https://speakerdeck.com/naturepr/company-information)（修改于 2026-05-31） |
| 远程 | 工程职位：可完全远程，前提是需要面对面讨论时能到岗；每月约一天全员到岗日。资料：开发岗位默认完全远程；业务和管理岗位建议每周到岗约两天。实习：每周至少到岗一天 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG)、[公司介绍资料](https://speakerdeck.com/naturepr/company-information)、[实习](https://herp.careers/v1/nature/UPK-qaE-dwBP) |
| 工时 | 弹性工时，无核心时间；可工作时段 5:00–22:00 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| 地点 | 横滨总部，距横滨站步行 5 分钟 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| 薪资 | 年薪制，含 45 小时固定加班费：后端 620 万–1,200 万日元；智能手机应用 620 万–1,200 万日元；固件 620 万–900 万日元；产品经理 720 万–1,200 万日元；实习时薪 1,300 日元起，工程实习时薪 1,500 日元起 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG)、[应用](https://herp.careers/v1/nature/dhj2CBULhCSH)、[固件](https://herp.careers/v1/nature/km0uZc0P_FSl)、[PdM](https://herp.careers/v1/nature/gh8SQSJj0ppB)、[实习](https://herp.careers/v1/nature/UPK-qaE-dwBP)、[工程实习](https://herp.careers/v1/nature/YqFSO9OIdsxs) |
| 休假 | 周末及节假日、年末年初假期，入职即享年假和带薪病假，婚丧假；试用期条件不变 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| 福利 | 通勤补贴每月上限 80,000 日元；购书；学习支持；最新开发设备；自然体验活动支持；EV、光伏和蓄电池购买支持；数码产品购买支持；语言学习支持；经许可可从事副业 | [后端](https://herp.careers/v1/nature/F06a8ZG7ncFG) |
| 签证 | 工程职位均未提及签证支持；劳务总务职位将“ビザの取得サポート”列为职责之一 | [职位](https://herp.careers/v1/nature/A6An3g_K1bIS) |
| 初级人才 | 有实习职位（工程实习：最少六个月，每周至少两天、每天约四小时，可远程但有部分限制）；未找到应届生职位 | [工程实习](https://herp.careers/v1/nature/YqFSO9OIdsxs)、[职位列表](https://herp.careers/v1/nature) |
| 组织 | 四年以合弄制为基础；2025 年 12 月起为设置职能经理的 Hybrid 模式 | [HR note（日文）](https://note.com/nature_global/n/n26cb9d5921ec) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：nature.global（sitemap 索引、通过 WordPress REST API 列出的 145 条新闻稿和 180 条通知），shop、terms、developer、swagger、status 和 engineering 子域名；HERP 职位板（15 个职位）；note 和 Speaker Deck 账号；GitHub 组织 `natureglobal`、`nature-global`、`natureinc`、`nature-inc`、`nature-remo` 和 `natureremo`；国税庁法人番号公表サイト、gBizINFO、電力・ガス取引監視等委員会文件和官報決算データベース；PR TIMES；BRIDGE、TechCrunch、Japan Dev；以 Nature株式会社、Nature Japan株式会社、Nature Inc. 和产品名进行的日英文网络检索。

- **营收。** 公告和決算公告转录均未披露营收。
- **估值、各投资方出资额及领投方**（任何一轮），包括 2024-06 JICN 未披露的金额。
- **电力零售登记细节。** 2020-11-04 的委员会文件可确认申请；在查阅的来源中未找到经济产业省登记编号、登记日期及之后是否撤销（经济产业省登记簿页面对自动访问返回 HTTP 403）。
- **美国公司与 Nature株式会社的法律关系**，以及 Nature Japan株式会社的设立日期。
- **工程人数。** 仅公开比例（资料中软件工程师占全职岗位 38%，硬件工程师 6%）。
- **员工股权。** 当前 HERP 职位未提及；Japan Dev 未经验证的页面列有“Employee stock option plan”。
- **公开 SLA。** 有公开状态页，但未找到 SLA 或可用性承诺。
- **开源。** `natureglobal` 组织（名称“Nature Inc.”，邮箱 info@nature.global，创建于 2018-04-19）有 19 个公开仓库，其中 8 个原创、11 个为 fork；原创仓库中最近一次推送为 `firequeue`（2024-07-31）。2026-04-28 创建了 `teslamotors/fleet-telemetry` 的 fork。`nature-remo` 是另一个名为“Nature Remo Community”的组织，未说明与公司有关。

### 不同来源之间的不一致

- **成立日期：**“2014年12月10日”（[公司页面](https://nature.global/about/)；至少自 [2022-04-11](https://nature.global/press/release/8397/) 起的公告也如此）；“2015年にハーバード大学発ベンチャーとして設立”（[2019-08-01 公告](https://nature.global/press/release/566/)）；2014 年 12 月在美国登记（[CEO 访谈](https://note.com/nature_global/n/n3a9457ec0239)）。決算公告将截至 2026-03-31 的财年标为第11期（[官報決算データベース](https://catr.jp/companies/9dfc0/74413)）；研究者推断：这一期数与首个会计期间于 2016 年 3 月结束相符，而非 2014 年 12 月。
- **员工人数：** 含业务委托和实习生 56 人（[公司页面](https://nature.global/about/)；无日期）；含实习生和业务委托 50 人（[HERP 公司信息栏](https://herp.careers/v1/nature/F06a8ZG7ncFG)；无日期）；员工 45 人（[资料](https://speakerdeck.com/naturepr/company-information)，修改于 2026-05-31）；[gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=4130001055679) 所示社保数据中总部事业所被保险人 32 人（未显示数据日期）。各口径不同。
- **资本：**“25.8億円（資本剰余金含む）”（[HERP](https://herp.careers/v1/nature/F06a8ZG7ncFG)、[资料](https://speakerdeck.com/naturepr/company-information)）与 [PR TIMES 公司信息栏](https://prtimes.jp/main/html/rd/p/000000182.000019285.html)中的資本金“5000万円”（访问于 2026-10-11）。前者包含资本剩余金，后者未说明。
- **销量：** 仅 Nature Remo 系列即超过 80 万台（[2026-06-18](https://nature.global/press/release/27356/)、[2026-10-01](https://nature.global/press/release/28318/)）；Remo 与 Remo E 合计 80 万台（[资料](https://speakerdeck.com/naturepr/company-information)，修改于 2026-05-31）；[业务开发职位](https://herp.careers/v1/nature/oDyWEgu8BBMF)称面向消费者“累計70万台”（datePosted 2022-03-18；访问于 2026-10-11）。
- **CTO 职位：**[团队页面](https://nature.global/careers/team/)将大塚的条目标为“CTO”，但写有“現在はソフトウェアエンジニア。エストニア在住”；[资料](https://speakerdeck.com/naturepr/company-information)写“Co-founder and CTO … 現在はソフトウェア全般を統括する”；其 [2023-07-19 文章](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown)称于 2023 年 7 月回任 CTO。
- **工作语言与工时：** Japan Dev 未经验证、无日期的页面称“We don't require Japanese skill for developers”，列出核心时间 11:00–17:00、通勤补贴上限 30,000 日元和东京地点（[Japan Dev](https://japan-dev.com/companies/nature)；访问于 2026-10-11）；当前[后端职位](https://herp.careers/v1/nature/F06a8ZG7ncFG)要求母语级日语，无核心时间，上限 80,000 日元，办公室位于横滨。

### 其他

- **进入并退出电力零售。** Natureスマート電気运营期间为 2021-03-01 至 2022-06-30；公司随后称将专注于 DR、ZEH 和 EV 能源管理（[2022-04-11](https://nature.global/press/release/8397/)）。DR 支援服务于 2022 年夏从关西电力开始。
- **故障。** 2024-07-08，时序数据库写入激增导致 API 服务器宕机，随后出现大量重连；2024-07-31，AWS US-EAST-1 区域的 ECS Fargate 故障导致 WebSocket 连接中断（[2024-07-11](https://nature.global/press/news/21359/)、[2024-07-31](https://nature.global/press/news/21522/)）。公司将不经服务器的控制列为优先事项；本地控制于 [2025-02-12](https://nature.global/press/release/22669/) 用于 Remo Lapis，于 [2025-03-18](https://nature.global/press/news/23693/) 用于 Remo 3 和 Remo mini 2。
- **海外销售。** 公司曾计划自 2020 年 9 月下旬在美国、澳大利亚和新加坡销售 Remo（[2020-09-16](https://nature.global/press/release/615/)）；TechCrunch 报道 Remo 3 在美国和加拿大上市，并称团队在疫情前每月前往深圳工厂（[TechCrunch，2020-09-23](https://techcrunch.com/2020/09/23/japanese-startup-nature-launches-remo-3-its-home-appliance-smart-remote-in-the-u-s-and-canada)）。2026-10-11 时 `en.nature.global` 重定向至日文网站；未找到关于海外销售的当前说明。
- **已终止的集成：** IFTTT（[2023-12-13](https://nature.global/press/news/18009/)）和 Nature 用户社区（[2024-04-01](https://nature.global/press/news/19351/)）。
- **发布渠道。** 公司在 Hatena 运营[工程博客](https://engineering.nature.global/)（最新文章 2026-07-31，最早 2021-04-29），在 [note](https://note.com/nature_global) 发布员工访谈，并有一个 [connpass 小组](https://nature.connpass.com/)，最近一次活动为 2023-07-19。API 参考和 OpenAPI 文件公开。

---

## 资料来源

**官方**

- [公司官网（日文）](https://nature.global/) · [公司页面](https://nature.global/about/) · [使命](https://nature.global/mission/) · [企业页面](https://nature.global/business/) · [Nature API 企业页面](https://nature.global/business/api-remo/)
- [新闻稿索引](https://nature.global/press/release/)
- [招聘](https://nature.global/careers/) · [团队](https://nature.global/careers/team/) · [职位列表](https://nature.global/careers/job/) · [访谈](https://nature.global/careers/interview/)
- [HERP 职位板](https://herp.careers/v1/nature)——[后端工程师](https://herp.careers/v1/nature/F06a8ZG7ncFG)、[固件工程师](https://herp.careers/v1/nature/km0uZc0P_FSl)、[智能手机应用工程师](https://herp.careers/v1/nature/dhj2CBULhCSH)、[产品经理](https://herp.careers/v1/nature/gh8SQSJj0ppB)、[业务开发](https://herp.careers/v1/nature/oDyWEgu8BBMF)、[业务开发（能源）](https://herp.careers/v1/nature/OZuuB4z-0YYb)、[销售（能源管理）](https://herp.careers/v1/nature/rxhJK_Wv9hzU)、[劳务总务](https://herp.careers/v1/nature/A6An3g_K1bIS)、[招聘兼 CEO 秘书](https://herp.careers/v1/nature/rdeGy2njtW2B)、[实习](https://herp.careers/v1/nature/UPK-qaE-dwBP)、[工程实习](https://herp.careers/v1/nature/YqFSO9OIdsxs)
- [开发者门户](https://developer.nature.global/) · [Remo E API](https://developer.nature.global/docs/nature-remo-e-api-specification/) · [Cloud API 规范](https://swagger.nature.global/) · [Local API 规范](https://local-swagger.nature.global/)
- [Nature Green](https://shop.nature.global/pages/nature-green) · [条款与政策](https://terms.nature.global/ja/) · [状态页](https://status.nature.global/)
- [工程博客（日文）](https://engineering.nature.global/) · [note（日文）](https://note.com/nature_global) · [Speaker Deck 公司介绍资料（日文）](https://speakerdeck.com/naturepr/company-information) · [connpass](https://nature.connpass.com/) · [GitHub 组织](https://github.com/natureglobal)

**新闻稿与通知（nature.global，日文，较新在前）**

- [空调操作保证 — 2026-10-01](https://nature.global/press/release/28318/)
- [Tesla 智能 EV 充电 — 2026-09-24](https://nature.global/press/release/28217/)
- [东京都家庭用聚合商登记 — 2026-08-24](https://nature.global/press/release/27984/)
- [空调保证活动、Nature Learn — 2026-06-18](https://nature.global/press/release/27356/)
- [Nature Lock 一般销售 — 2026-04-30](https://nature.global/press/release/26672/)
- [Nature Lock 与 Nature Key 发布 — 2026-04-21](https://nature.global/press/release/26546/)
- [EV Switch 面向个人销售 — 2026-03-10](https://nature.global/press/release/26117/)
- [ISO/IEC 27001 — 2026-03-09](https://nature.global/press/release/26121/)
- [世田谷区实证结果 — 2025-12-25](https://nature.global/press/release/25801/)
- [EV Switch 发售 — 2025-10-31](https://nature.global/press/release/25360/)
- [JC-STAR ★1 — 2025-10-10](https://nature.global/press/release/25287/)
- [EV 远程充电实证 — 2025-09-04](https://nature.global/press/release/25064/)
- [Forbes JAPAN GX 50 — 2025-08-14](https://nature.global/press/news/24875/)
- [DR 支援服务改版 — 2025-07-01](https://nature.global/press/release/24645/)
- [Nature Remo E2 — 2025-04-08](https://nature.global/press/release/24003/)
- [东京燃气 DR 支援服务 — 2025-04-02](https://nature.global/press/release/23974/)
- [Remo 3 与 mini 2 本地控制 — 2025-03-18](https://nature.global/press/news/23693/)
- [EV Switch 与松下 — 2025-02-25](https://nature.global/press/release/23308/)
- [Remo Lapis 本地控制 — 2025-02-12](https://nature.global/press/release/22669/)
- [Shizen Connect 合作 — 2024-10-30](https://nature.global/press/release/22262/)
- [グッドデザイン賞 — 2024-10-16](https://nature.global/press/release/22036/)
- [故障报告 — 2024-07-31](https://nature.global/press/news/21522/)
- [故障原因报告 — 2024-07-11](https://nature.global/press/news/21359/)
- [Nature Remo Lapis — 2024-07-05](https://nature.global/press/release/21289/)
- [Series D 合计 12.2億円 — 2024-06-27](https://nature.global/press/release/20904/)
- [auエネルギー＆ライフ — 2024-06-26](https://nature.global/press/release/20279/)
- [关西电力全年 DR — 2024-06-25](https://nature.global/press/news/20713/)
- [东京燃气业务合作 — 2024-04-18](https://nature.global/press/release/19564/)
- [用户社区关闭 — 2024-04-01](https://nature.global/press/news/19351/)
- [ドコモでんき自動エコモード — 2024-03-04](https://nature.global/press/release/18635/)
- [10.2億円融资 — 2024-02-07](https://nature.global/press/release/18339/)
- [IFTTT 集成终止 — 2023-12-13](https://nature.global/press/news/18009/)
- [Nature Green 付费选项 — 2023-08-08](https://nature.global/press/release/16586/)
- [Nature Remo nano — 2023-07-04](https://nature.global/press/release/15936/)
- [オクトパスエナジー DR — 2023-02-13](https://nature.global/press/release/13793/)
- [NTT 都科摩 DR — 2022-12-23](https://nature.global/press/release/12753/)
- [关西电力 DR — 2022-06-28](https://nature.global/press/release/9771/)
- [Natureスマート電気终止 — 2022-04-11](https://nature.global/press/release/8397/)
- [7.5億円融资 — 2021-07-14](https://nature.global/press/release/5754/)
- [Natureスマート電気扩展至全国 — 2021-07-06](https://nature.global/press/release/5591/)
- [30 万台、iF Design Award 2021 — 2021-04-15](https://nature.global/press/release/5025/)
- [Natureスマート電気上线 — 2021-03-01](https://nature.global/press/release/4320/)
- [Google for Startups Accelerator — 2021-01-07](https://nature.global/press/release/3816/)
- [面向企业的付费 Remo E API — 2021-01-05](https://nature.global/press/release/3811/)
- [20 万台、海外计划 — 2020-09-16](https://nature.global/press/release/615/)
- [Nature Remo 3 — 2020-08-05](https://nature.global/press/release/606/)
- [Nature Remo E lite — 2020-04-28](https://nature.global/press/release/589/)
- [iF Design Award 2020 — 2020-02-05](https://nature.global/press/news/1426/)
- [Nature Remo E 预售 — 2019-12-10](https://nature.global/press/release/578/)
- [技术顾问川崎修平 — 2019-11-17](https://nature.global/press/release/575/) · [技术顾问阿部力也 — 2019-11-17](https://nature.global/press/release/572/)
- [5億円融资 — 2019-08-01](https://nature.global/press/release/566/)
- [1億円融资 — 2018-02-19](https://nature.global/press/release/524/)
- [API 公开 — 2018-02-01](https://nature.global/press/news/1361/)
- [Nature Remo 开售 — 2017-10-16](https://nature.global/press/release/522/)
- [500 KOBE ACCELERATOR — 2017-08-14](https://nature.global/press/news/1312/)
- [VPP 实证 — 2017-07-25](https://nature.global/press/news/513/)
- [Kickstarter 5 万美元 — 2016-06-03](https://nature.global/press/release/456/)

**工程博客与访谈（日文）**

- [Nature Remo 背后的技术 — 2021-04-29](https://engineering.nature.global/entry/start-blog)
- [嵌入式 Rust 书籍 — 2021-05-07](https://engineering.nature.global/entry/embedded-rust-from-basics)
- [FreeRTOS + Catch2 — 2022-12-02](https://engineering.nature.global/entry/freertos-catch-part1)
- [React Native 原生小组件 — 2022-12-06](https://engineering.nature.global/entry/add-native-widget-to-react-native-app)
- [分阶段固件发布 CLI — 2022-12-09](https://engineering.nature.global/entry/staged-firmware-release-cli)
- [WebSocket ECS 平滑停机 — 2023-07-19](https://engineering.nature.global/entry/websocket-ecs-graceful-shutdown)
- [firequeue — 2024-04-02](https://engineering.nature.global/entry/2024/04/02/101743)
- [AI 验证重构自动合并 — 2026-07-31](https://engineering.nature.global/entry/2026/07/prove-pure-refactoring-with-ai-and-auto-merge)
- [CEO 访谈，立志編 — 2025-12-04](https://note.com/nature_global/n/n3a9457ec0239) · [組織・カルチャー編 — 2025-12-04](https://note.com/nature_global/n/nb47e66f7c43d)
- [Hybrid 组织 — 2025-12-19](https://note.com/nature_global/n/n26cb9d5921ec)
- [大塚访谈 — 2022-08-18](https://note.com/nature_global/n/n6c8b703cdc85)

**登记、公告与第三方报道**

- [国税庁法人番号公表サイト — 4130001055679（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4130001055679)
- [gBizINFO（日文）](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=4130001055679)
- [電力・ガス取引監視等委員会——答复，2020-11-04（日文）](https://www.egc.meti.go.jp/info/public/pdf/20201104001b.pdf) · [申请者一览（日文）](https://www.egc.meti.go.jp/info/public/pdf/20201104001c.pdf)
- [官報決算データベース——決算公告转录（日文）](https://catr.jp/companies/9dfc0/74413)
- [PR TIMES——含公司信息栏的公告，2026-10-01（日文）](https://prtimes.jp/main/html/rd/p/000000182.000019285.html)
- [BRIDGE——Series D 合计 12.2億円，2024-06-28（日文）](https://thebridge.jp/2024/06/nature-series-d2-round-funding)
- [TechCrunch——Remo 3 在美国和加拿大上市，2020-09-23](https://techcrunch.com/2020/09/23/japanese-startup-nature-launches-remo-3-its-home-appliance-smart-remote-in-the-u-s-and-canada)
- [Japan Dev——公司页面（未经验证）](https://japan-dev.com/companies/nature)
