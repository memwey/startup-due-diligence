# Shippio

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

Shippio（株式会社Shippio）是一家总部位于东京、成立于 2016 年 6 月的公司，最初名为サークルイン株式会社（Circle-in Corp.）。公司运营 **Shippio Platform**，为国际贸易和货运提供船舶追踪、贸易文件处理、询价订舱和成本分析等云服务；同时它自身也是持牌货运代理商，并通过子公司協和海運经营报关业务。

- 平台已有 1,500 多家公司使用（[服务网站](https://service.shippio.io/)；无日期，访问于 2026-07-29）。公司称，自 2022 年 Series B 以来，净营收约增长至 20 倍、处理集装箱量约 35 倍、平台用户约 8 倍（[2025-10-30](https://www.shippio.io/news/press-release/series-c/)）。
- 累计融资约 70 亿日元；最近一轮为 [2025-10-30](https://www.shippio.io/news/press-release/series-c/) 完成的 32.4 亿日元 Series C（股权 18.7 亿日元＋债务 13.7 亿日元），由 DNX Ventures 领投。
- CEO 称员工人数“超过 100 人”（[2026-01-05](https://www.shippio.io/news/press-release/shippio-2026/)）；公司目标是在三年内达到 300 人（[2025-10-30](https://www.shippio.io/news/press-release/series-c/)）。无日期的第三方资料不作为当前精确人数。
- 后端是在 AWS 上运行的 Ruby on Rails 和 Go，前端为 React/TypeScript，通过 GraphQL（Apollo Federation）通信（[TokyoDev 公司页](https://www.tokyodev.com/companies/shippio)、[后端工程师职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)；无日期，访问于 2026-07-29）。工程团队主要使用英语；后端职位要求英语，日语受欢迎但并非必须（[招聘 FAQ](https://recruit.shippio.io/faq)、[职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)；无日期，访问于 2026-07-29）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | 株式会社Shippio / Shippio, Inc.（创立时为サークルイン株式会社 / Circle-in Corp.） | [公司页面](https://www.shippio.io/corp/)、[2017-05-08](https://prtimes.jp/main/html/rd/p/000000001.000025761.html) |
| 成立 | 2016 年 6 月 | [公司页面](https://www.shippio.io/corp/) |
| 总部 | 〒105-0023 東京都港区芝浦一丁目1番1号 BLUE FRONT SHIBAURA TOWER S 9階（[2025-09-01](https://www.shippio.io/news/press-release/newoffice202509/) 迁入） | [公司页面](https://www.shippio.io/corp/) |
| 大阪分部 | 〒542-0076 大阪市中央区難波5-1-60 なんばスカイオ 27F WeWork内 | [公司页面](https://www.shippio.io/corp/) |
| 代表人 | 代表取締役 CEO 佐藤 孝徳（Takanori Sato） | [公司页面](https://www.shippio.io/corp/) |
| 资本金 | 含资本准备金 8.4 亿日元 | [公司页面](https://www.shippio.io/corp/)；无日期，访问于 2026-07-29 |
| 员工人数 | “超过 100 人”（CEO 新年致辞） | [2026-01-05](https://www.shippio.io/news/press-release/shippio-2026/) |
| 工作语言 | 工程团队主要使用英语，业务团队使用日语；全公司并不强制英语 | [招聘 FAQ](https://recruit.shippio.io/faq) |
| 客户 | 平台使用企业 1,500 多家 | [服务网站](https://service.shippio.io/)；无日期，访问于 2026-07-29 |
| 累计融资 | 约 70 亿日元 | [2025-10-30](https://www.shippio.io/news/press-release/series-c/) |
| 集团公司 | 協和海運株式会社（成立于 1960 年的报关公司，于 [2022-09-27](https://www.shippio.io/news/pressrelease202209-ma/) 完成 100% 收购） | [公司页面](https://www.shippio.io/corp/) |
| 许可 | 第一種貨物利用運送事業者（関自貨第1714号）；第二種貨物利用運送事業者（国総国物第107号、国自貨第386号）；IATA 公认代理店；国際複合一貫輸送約款（2013）；WAYBILL 約款（2013） | [公司页面](https://www.shippio.io/corp/) |
| 其他登记 | 完成保险代理店登记，并与东京海上日动签署代理店合同 | [2025-12-22](https://www.shippio.io/news/press-release/insurance2025/) |
| 安全认证 | ISO/IEC 27001:2022，JQA-IM2002，取得于 2023-05-26；登记显示有效至 2029-05-25 | [2023-05-31 公告](https://www.shippio.io/news/iso-iec270012022/)、[ISMS 登记](https://isms.jp/lst/ind/CR_JQA-IM2002.html) |

**会员与项目：** JIFFA 正会员、日本ロジスティクスシステム協会、[経団連（2024-10-01 加入）](https://www.shippio.io/news/keidanren/)、World Cargo Alliance、[J-Startup 入选（2021-10-21）](https://www.shippio.io/news/pressrelease20211021_jstart2021/)，以及 CEO 于 [2025-10-08](https://www.shippio.io/news/press-release/doyukai/) 加入的経済同友会。公司参加了 YJ Capital 和 East Ventures 运营的首期 Code Republic 加速器，并在 Demo Day 展示名为 PortHub 的服务（[BRIDGE，2017-05](https://thebridge.jp/2017/05/circle-in-seed-round-funding)、[2017-05-08 公告](https://prtimes.jp/main/html/rd/p/000000001.000025761.html)）。

公司在[公司页面](https://www.shippio.io/corp/)列出的**奖项**包括：生成AI大賞 2025 特別賞、ニッポン新事業創出大賞 2025 最優秀賞、日本DX大賞 2025 事業変革部門 大賞、Logistics Tech Startups APAC（2022）、LinkedIn Top Startups Japan（2022）、Ruby biz Grand prix 2022 大賞。此外还有 [DXイノベーション大賞2025 審査員特別賞（2026-03-17）](https://www.shippio.io/news/press-release/dxinnovation-award/)和 [Mizuho Innovation Award 2022 3Q（2022-11-25）](https://www.shippio.io/news/mizuho_innovation_award2022_3q_20221125/)。在 Financial Times / Statista “High-growth companies Asia-Pacific 2026”榜单中，公司综合排名第 84、物流与运输类别第 4，并称自己是该类别唯一的日本公司（[2026-03-24](https://www.shippio.io/news/ftranking2026/)）。

### 公司陈述的市场背景

根据 [Series C 公告（2025-10-30）](https://www.shippio.io/news/press-release/series-c/)：

- 2016 至 2024 年通关许可件数增长至八倍，公司将其归因于电商和进出口量增长。
- 公司称贸易业务仍然依赖模拟流程和个人经验（アナログかつ属人的）。
- 公司将美国关税和中东局势列为增加供应链不确定性的地缘政治风险。
- 公开目标：到 2030 年，让日本进出口货物的 30%——每年 540 万 TEU——通过 Shippio Platform 处理。

---

## 产品

**Shippio Platform** 是在 [2025-03-12 使命／愿景更新](https://www.shippio.io/news/press-release/newmv/)中启用的总品牌名，各项服务也同时更名。产品页面位于 [service.shippio.io](https://service.shippio.io/)。

### 服务阵容

| 服务 | 面向对象 | 内容 | 页面 |
|---|---|---|---|
| Shippio Forwarding | 货主 | Shippio 自营的数字货代服务，捆绑云平台 | [页面](https://service.shippio.io/forwarding) |
| Shippio Cargo | 货主 | 覆盖任意货代所处理货物的贸易管理云；2023-01-25 以“Any Cargo”发布 | [页面](https://service.shippio.io/cargo) · [2023-01-25](https://www.shippio.io/news/any-cargo20230125/) |
| Shippio Works | 国际物流运营商／货代 | 面向运营商一侧的贸易管理云，发布于 2024-09-04 | [页面](https://service.shippio.io/works) · [2024-09-04](https://www.shippio.io/news/shippioworks/) |
| Shippio Clear | 报关行和货代 | AI 通关云，发布于 2025-09-08，与協和海運共同开发 | [2025-09-08](https://www.shippio.io/news/press-release/shippio-clear/) |

产品页面列出的功能（无日期，访问于 2026-07-29）包括：带延误提醒的自动船舶追踪；按货件隔离的聊天和文件共享；读取 B/L、发票和装箱单的 AI-OCR，宣称识别准确率“不低于 97%”；AI 发票与采购订单匹配，宣称最多减少 80% 工作时间；交期分析；报价和成本模拟。Forwarding 页面称其拥有 120 多家日本国内合作伙伴和覆盖 35 个以上国家的海外网络。

### 商业化

产品以 SaaS 形式销售，并与公司自营的货代和报关业务结合，因此收入同时包含订阅费及运输／通关服务费。未找到完整的公开价目表。

- **Shippio Works** 在[产品页面](https://service.shippio.io/works)公开价格：每月 80,000 日元，最多 50 名用户，可无限邀请外部访客、无限连接 API。
- **Shippio Forwarding** [页面](https://service.shippio.io/forwarding)称，客户使用 Shippio 货代服务时，可免费使用云平台。
- **Shippio Cargo** 和 **Shippio Clear** 未公开价格。
- 自 [2025-07-23](https://www.shippio.io/news/press-release/apifree202507/)起，**Shippio API** 对平台客户免费。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2019-10-31 | 108 家使用企业；完成与 30 个国家的进出口业务 | [Series A 公告](https://www.shippio.io/news/finance-series-a/) |
| 2022-07 | 货件数同比 4.3 倍；与 42 个国家／地区有业务往来，约为 2020 年的 2.5 倍；贸易工作时间平均减少 44.9%，最多减少 67.9% | [六周年信息图](https://www.shippio.io/news/6th_anniversary_infographics/) |
| 2022-07-31 | 订单额约为上年同期 4 倍 | [Series B 公告](https://www.shippio.io/news/pressrelease202209-seriesb/) |
| 2025-01-20 | Shippio Works 账号超过 100 | [公告](https://www.shippio.io/news/shippio-works-accounts/) |
| 2025-03-12 | 活跃用户一年内增至 3.6 倍；处理货件量超过 10 倍 | [使命／愿景更新](https://www.shippio.io/news/press-release/newmv/) |
| 2025-10-23 | Shippio Works 被 80 多家公司采用，超过最初 50 家目标；下一目标为 200 家，称相当于 JIFFA 会员的 35–40% | [公告](https://www.shippio.io/news/press-release/works-1year/) |
| 2025-10-30 | 自 Series B（2022）以来：净营收（毛利润）约 20 倍、处理集装箱约 35 倍、平台用户约 8 倍 | [Series C 公告](https://www.shippio.io/news/press-release/series-c/) |
| 无日期，访问于 2026-07-29 | 平台使用企业 1,500 多家；Works 页面称 80 多家公司、“JIFFA 会员的 15% 以上” | [服务网站](https://service.shippio.io/)、[Works 页面](https://service.shippio.io/works) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2024-11-27](https://www.shippio.io/news/ohyama/) | オーヤマ | 采用 Any Cargo |
| [2025-01-09](https://www.shippio.io/news/naganuma/) | 長沼商事 | 采用 Any Cargo |
| [2025-02-12](https://www.shippio.io/news/works-fwdpro/) | Forwarder-PRO | 与 Shippio Works 系统集成 |
| [2025-03-05](https://www.shippio.io/news/daifuku-anycargo/) | ダイフク | 采用 Any Cargo |
| [2025-04-22](https://www.shippio.io/news/press-release/tokai-cargo/) | 東海 | 采用 Shippio Cargo |
| [2025-05-19](https://www.shippio.io/news/press-release/caas-tts/) | TTS | 采用 Shippio Cargo |
| [2025-06-18](https://www.shippio.io/news/press-release/case-callresponse/) | CALL＆RESPONSE | 采用 Shippio Forwarding |
| [2025-08-01](https://www.shippio.io/news/press-release/naka-kogyo/) | ナカ工業 | 采用平台 |
| [2025-08-05](https://www.shippio.io/news/press-release/works-mgl/) | 三井物産グローバルロジスティクス | 采用 Shippio Works |
| [2025-08-26](https://www.shippio.io/news/press-release/ykk-ap_cargo/) | YKK AP | 采用 Shippio Cargo |
| [2025-11-17](https://www.shippio.io/news/press-release/seino_secondment/) | セイノーホールディングス | 开始接收派驻人员 |
| [2025-11-20](https://www.shippio.io/news/aisin-dxl/) | アイシン | 使用 Shippio Cargo 船舶追踪数据实现物流可视化 |
| [2025-12-11](https://www.shippio.io/news/press-release/sumitomoriko-cargo/) | 住友理工 | 采用 Shippio Cargo |
| [2025-12-22](https://www.shippio.io/news/press-release/insurance2025/) | 東京海上日動 | 签署保险代理店合同 |
| [2026-02-17](https://www.shippio.io/news/press-release/cargo-logos/) | ロゴスコーポレーション | 采用 Shippio Cargo |
| [2026-02-26](https://www.shippio.io/news/press-release/cargo-gongcha/) | ゴンチャ ジャパン | 采用 Shippio Cargo |
| [2026-04-07](https://www.shippio.io/news/ananas/) | アナナスジャパン | 采用 Shippio Platform |
| [2026-04-21](https://www.shippio.io/news/press-release/naccs_202604/) | 国交省 Cyber Port／NACCS | 宣布系统集成（见“工程”） |
| [2026-05-19](https://www.shippio.io/news/synegic/) | シネジック | 采用平台 |
| [2026-06-02](https://www.shippio.io/news/ucc-forwardingcargo/) | UCC上島珈琲 | 采用 Forwarding＋Cargo |
| [2026-06-15](https://www.shippio.io/news/mitsubishi-motors-cargo/) | 三菱自動車 | 采用 Shippio Cargo |
| [2026-07-02](https://www.shippio.io/news/sanipak-cargo/) | 日本サニパック | 采用 Shippio Cargo |

公司还参加了经济产业省的[貿易プラットフォーム利活用推進検討会（2024-03-28）](https://www.shippio.io/news/digital_trade_platform/)和[国土交通省贸易 DX 意见交流会（2025-01-23）](https://www.shippio.io/news/press-release/mlit-tradedx/)，并于 [2026-05-14](https://www.shippio.io/news/press-release/pre-committee/)宣布成立推动贸易 DX 标准化行业组织的筹备委员会。

### 公开计划

根据 [Series C 公告（2025-10-30）](https://www.shippio.io/news/press-release/series-c/)，资金用于：（1）产品开发，由内部物流运营团队和集团报关公司向开发团队反馈；（2）AI，新设 **AI Advanced Lab**，先在公司自身物流业务中应用，再反映到产品；（3）进一步并购；（4）组织建设，三年内向 300 人发展，覆盖销售、CS、业务开发、PdM、产品设计、工程、HR 和公司职能。公告称当时约有 20 个职位开放。

长期目标是净营收持续每年翻倍，并在 2030 年前让日本进出口货物的 30%（每年 540 万 TEU）通过平台处理。

---

## 创始人

**佐藤 孝徳（Takanori Sato）**——共同创始人、代表取締役 CEO（[公司页面](https://www.shippio.io/corp/)）。

- 应届加入三井物产，先在石油部门从事原油交易，后在企业投资部门从事 PE 和初创投资，之后在北京的中国总代表处规划和推动三井的中国战略（[note 访谈](https://note.com/logizine/n/n4cd2f85fdf0a)、[公司介绍资料](https://speakerdeck.com/shippio/zhu-shi-hui-she-shippiohui-she-shao-jie-zi-liao-20221130)）。
- 2016 年 6 月，与当时同样派驻北京的土屋隆司共同创立サークルイン株式会社（后为株式会社Shippio）（[note 访谈](https://note.com/logizine/n/n4cd2f85fdf0a)、[2017-05-08 公告](https://prtimes.jp/main/html/rd/p/000000001.000025761.html)）。
- 2018 年取得第二类货物利用运输事业许可，公司称这是初创公司首次取得该许可，并发布 Shippio Forwarding（[BRIDGE，2018-12](https://thebridge.jp/2018/12/shippio-fundraising)）。
- 2025-10-08：加入経済同友会（[公告](https://www.shippio.io/news/press-release/doyukai/)）。
- 长篇访谈：[ロジ人（日文）](https://note.com/logizine/n/n4cd2f85fdf0a)、[STARTUPS JOURNAL（日文）](https://startup-db.com/magazine/category/interview/shippio-sato)、[Business Insider Japan（日文）](https://www.businessinsider.jp/article/2510shippio-raises-3-billion-yen-and-discusses-japans-startup-market/)、[十周年 note（日文）](https://www.shippio.io/news/10thanniversary/)。

**土屋 隆司**——共同创始人；创立时被称为代表取締役副社長，同样出身三井物产（[BRIDGE，2017-05](https://thebridge.jp/2017/05/circle-in-seed-round-funding)、[2017-05-08 公告图片说明](https://prtimes.jp/main/html/rd/p/000000001.000025761.html)）。当前[公司页面](https://www.shippio.io/corp/)仅将佐藤列为代表人，没有列出土屋。

**[公司介绍资料](https://speakerdeck.com/shippio/zhu-shi-hui-she-shippiohui-she-shao-jie-zi-liao-20221130)列出的管理层（版本日期 2025-10-30）**

| 姓名 | 所列职位 | 公开背景 |
|---|---|---|
| 佐藤 孝徳 | 代表取締役 CEO | 三井物产 |
| 阪 茉紘 | VP of Strategy | P&G Japan、McDonald's Japan、Plaid（2021 年执行董事） |
| 伊井 壮太郎 | Director of Product | LINE、Mercari、Pokémon |
| Felix Küppers | VP of Engineering | 全栈工程师；曾任海事云 ERP 公司 CTO／CEO；2022 年移居日本，2023 年加入 Shippio |
| 丹羽 剛 | VP of Finance | 野村证券、美国投资基金、航天初创 CFO；Wharton MBA |
| 伊達 雄介 | VP of HR | En Japan、Bengo4.com 执行董事 |
| 井上 裕史 | VP of Business | 三菱 UFJ 证券、Green、WealthNavi、Medley |

其他单独公布的任命包括：**Ryan O'Connor** 于 [2022-11-18](https://www.shippio.io/news/joined-shippio-as-cto-20221118/)出任 CTO（履历列有 DivX 2001、@WalmartLabs 2011、Rakuten 2012、Mercari 2019、Merlogi CTO 2021）；**伊達雄介**（VP of HR）和**丹羽剛**（VP of Finance）于 [2024-01-10](https://www.shippio.io/news/join2024_01/)就任；**阪茉紘**（VP of Strategy）于 [2026-01-20](https://www.shippio.io/news/press-release/vpos_202601/)公布任命，并称其于 2025 年 11 月加入。外部董事包括自 [Series A（2019-11-11）](https://www.shippio.io/news/finance-series-a/)起任职的 Globis Capital Partners 南良平，以及自 [2024-09-11](https://www.shippio.io/news/outsidedirector2024/)起任职的同公司湯浅エムレ秀和。Raksul CTO 泉雄介于 [2021-11-16](https://www.shippio.io/news/pressrelease20211116_tech_advisor/)成为技术顾问。

子公司協和海運社长两次从 Shippio 任命：井上于 [2024-09-02](https://www.shippio.io/news/kyowa-ceo/)上任；Shippio 集团持证报关士松本于 [2025-09-19](https://www.shippio.io/news/press-release/kyowa-ceo202509/)上任。资料还称员工平均年龄 35.3 岁，40% 的员工有子女。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2017-05-08 | 第三者割当増資（当时为サークルイン株式会社） | 未披露 | 500 Startups Japan、YJキャピタル、イーストベンチャーズ | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000001.000025761.html) |
| 2018-12-03 | 第三者割当増資 | 1.9 亿日元 | 500 Startups Japan、グロービス・キャピタル・パートナーズ、DBJキャピタル、YJキャピタル、East Ventures、2 名个人投资者 | — | [BRIDGE](https://thebridge.jp/2018/12/shippio-fundraising) |
| 2019-11-11 | シリーズA | 10.6 亿日元 | アンカー・シップ・パートナーズ、環境エネルギー投資、グロービス・キャピタル・パートナーズ、DBJキャピタル、Delight Ventures、East Ventures、Sony Innovation Fund、YJキャピタル、500 Startups Japan | 当时资本金 6.5122 亿日元 | [Shippio](https://www.shippio.io/news/finance-series-a/) |
| 2022-09-27 | シリーズB（第三者割当増資及び融資等） | 16.5 亿日元 | 新增：DNX Ventures、Spiral Innovation Partners、東京海上日動火災保険、みずほキャピタル、あおぞら企業投資；原有：デライト・ベンチャーズ、環境エネルギー投資、ソニーベンチャーズ、アンカー・シップ・パートナーズ | 约 30 亿日元 | [Shippio](https://www.shippio.io/news/pressrelease202209-seriesb/) |
| 2025-10-30 | シリーズC | 32.4 亿日元（股权 18.7 亿＋债务 13.7 亿） | 股权：DNX Ventures（领投）、環境エネルギー投資、鈴与（新增）、New Commerce Ventures（新增）、YMFGキャピタル（新增）、デライト・ベンチャーズ、あおぞら企業投資、Spiral Innovation Partners；债务：商工組合中央金庫、日本政策金融公庫、みずほ銀行、三菱UFJ銀行、りそな銀行等 | 约 70 亿日元 | [Shippio](https://www.shippio.io/news/press-release/series-c/)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000160.000025761.html) |

轮次名称遵循公司公告。公司 2017 和 2018 年公告只使用“第三者割当増資”；[BRIDGE（2017-05）](https://thebridge.jp/2017/05/circle-in-seed-round-funding)将 2017 年融资称为种子轮。DNX Ventures 同时领投 Series B 和 C；環境エネルギー投資、デライト・ベンチャーズ、あおぞら企業投資和 Spiral Innovation Partners 两轮均有出现。[Series C 公告](https://www.shippio.io/news/press-release/series-c/)中，New Commerce Ventures 合伙人称 Shippio 曾是他们原任职机构 Z Venture Capital 的被投公司。2017、2018 和 Series A 中的 YJキャピタル未出现在 Series B 或 C 公告中。

两轮融资与产品或公司事件同时公布：Series B 同时发布“Any Cargo”，并在同日[收购協和海運](https://www.shippio.io/news/pressrelease202209-ma/)；Series C 同时全面改版招聘网站。

---

## 工程

### 技术栈与平台

以下根据招聘信息、技术博客索引和 TokyoDev 公司页推断。

- **后端：** Ruby on Rails／Ruby 和 Go。[TokyoDev](https://www.tokyodev.com/companies/shippio)称后端为“Ruby on Rails and Go，部署于 AWS”。[后端职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)列出 Ruby on Rails、PostgreSQL、Redis、REST API、GraphQL。
- **前端：** TypeScript／JavaScript、React、Apollo Client（[前端职位，2025-09-29](https://japan-dev.com/jobs/shippio/shippio-front-end-engineer-dinv1r)、[技术博客索引](https://note.com/shippio/n/n36094bb0a387)）。
- **API 层：** 通过 Apollo Federation 使用 GraphQL；面向客户的 Shippio API 使用 REST（[SOA 资料](https://speakerdeck.com/shippio/voyage-for-the-future-soa-approach-powered-by-apollofederation)、[API 页面](https://service.shippio.io/shippio-api/)）。
- **云与基础设施：** AWS（ALB、S3、ECS、Aurora、RDS、Lambda、QuickSight、Route 53、CDK），以及 GCP、Firebase（[职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)、[Japan Dev](https://japan-dev.com/companies/shippio)）。
- **工具：** Docker、GitHub Actions、CircleCI、OpenTofu、ecspresso、Auth0、Datadog、LaunchDarkly、Playwright、Chromatic、Figma（[职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)、[QA 职位](https://herp.careers/v1/shippioinc/K_l6flVr-n80)、[技术博客索引](https://note.com/shippio/n/n36094bb0a387)）。

后端职位还将“Claude/AI”列为使用中的工具。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 船舶追踪 | 跨承运商自动更新船舶动态和 ETD／ETA；公司称其逻辑源于自营货代经验。Works 页面称确认船舶状态所需时间约减少 90%。 | [Works 页面](https://service.shippio.io/works) |
| 出港前预先追踪 | 在出港前发现国际运输延误风险。 | [2026-06-12](https://www.shippio.io/news/early-tracking2026/) |
| 空运货物追踪 | 自动追踪空运货物；公司于 [2024-11-21](https://www.shippio.io/news/air/)取得国际航空货运许可。 | [2026-03-02](https://www.shippio.io/news/press-release/air-tracking/) |
| AI-OCR | 读取 B/L、发票和装箱单，宣称准确率 97% 以上，并自动计算和检查错误；2026-04 增加规则自动学习，2026-05 扩展到费用相关文件。 | [2025-04-04](https://www.shippio.io/news/press-release/ai-ocr/)、[2025-08-12](https://www.shippio.io/news/press-release/ai-ocr_ivpl/)、[2026-04-01](https://www.shippio.io/news/press-release/ai-ocr_rules/)、[2026-05-08](https://www.shippio.io/news/ai-ocr_202605/) |
| AI 发票匹配 | 将采购订单内容与发票数据匹配；宣称最多减少 80% 工作时间。 | [2025-11-18](https://www.shippio.io/news/press-release/ai-invoice/) |
| AI 货件创建 | 解析邮件正文和附件 PDF，提取管理编号、港口、Incoterms 等字段并登记货件。 | [2026-05-21](https://www.shippio.io/news/ai-shipment/) |
| AI 账单项目标注 | 对不同服务商名称各异的账单明细分类，逐行输出 CSV，并换算为日元。 | [2026-07-28](https://www.shippio.io/news/ai-auto-tag/) |
| Shippio Clear | AI 通关：对非标准贸易文件 OCR、自动计算检查、转换为包含 HS 编码和原产地的 NACCS 申报格式并一键导出。公司称经協和海運验证可提升 70% 效率；先支持海运进口，计划扩展海运出口和空运。 | [2025-09-08](https://www.shippio.io/news/press-release/shippio-clear/) |
| 多层 AI Agent | “Commander”解释客户来信并路由至专业团队，称约 70% 可自动路由；“Specialist”执行标准任务，特定流程称最多自动化 90%。输出仍保留人工审批。 | [PC-Webzine（日文）](https://www.pc-webzine.com/article/3496) |
| Shippio API | REST。POST 登记货件；GET 获取船舶动态／ETD／ETA、在途货物与到达预测、合作方和主数据。凭证从产品设置页签发；自 2025-07 起对平台客户免费。 | [产品页](https://service.shippio.io/shippio-api/)、[Stoplight 文档](https://shippio.stoplight.io/docs/shippio-api/753cf96a69c40-shippio-api)、[2024-05-07](https://www.shippio.io/news/shippioapi/) |
| 文件集成 API | 与客户自有核心系统自动交换贸易文件数据。 | [2026-01-14](https://www.shippio.io/news/file-api/) |
| Cyber Port／NACCS 集成 | 使用 Cyber Port 的 NACCS 集成 API，在 Shippio Platform 与 NACCS 之间双向传输数据。公司指出国交省于 2026-04-16 更新 Cyber Port 条款以允许此用途。 | [2026-04-21](https://www.shippio.io/news/press-release/naccs_202604/) |

**架构历史。** [2022-12-01 Speaker Deck](https://speakerdeck.com/shippio/voyage-for-the-future-soa-approach-powered-by-apollofederation)描述了从 Rails 单体应用迁移到由 Apollo Federation 统一的 SOA：新服务使用 Go，AWS 改为多账号，并从 Terraform 迁移至 CDK。项目从 2021 年 9 月持续至 2022 年 8 月；资料称当时约有 8 名工程师，Series B 后目标约 20 人。公司 note 上有[同一迁移的日文总结](https://note.com/shippio/n/nc56f93ab661b)。

公司运营英文 [Medium 技术博客](https://techblog.shippio.io/)，分为 Frontend、Backend、Infrastructure、QA 和 Organization，并在 note 提供[历史文章索引](https://note.com/shippio/n/n36094bb0a387)。[招聘网站](https://recruit.shippio.io/)显示的最近四篇文章日期为 2025-08-05、2025-07-11、2025-03-25、2025-03-05。

### 招聘所需技术背景

后端职位优先考虑 AWS／GCP 云基础设施经验，以及把业务需求转化为架构设计的经验。QA 职位优先考虑 Web ERP 产品测试经验，职责涉及平台测试规划、自动化和质量改善。物流背景属于优先而非必需。查阅到的职位没有要求区块链、爬虫或实时交易经验。

### 行业领域

国际货代与通关业务——提单、商业发票、装箱单、Incoterms、HS 编码和原产地规则、FCL／LCL 海运和空运、承运商班期与船舶动态，以及日本政府系统 NACCS 和 Cyber Port。公司自身持有货代许可并拥有报关公司；[Series C 公告](https://www.shippio.io/news/press-release/series-c/)称内部物流运营团队、集团报关公司与开发团队的组合是其特点。

[招聘 FAQ](https://recruit.shippio.io/faq)称许多成员加入前没有贸易或国际物流经验，行业知识可以入职后学习，约 50% 员工直到进入招聘流程才开始对贸易行业感兴趣。QA 职位将物流背景列为优先而非必需。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 工程团队主要用英语；产品岗位与工程师用英语、团队内部用日语；业务团队用日语。公司称英语并非全员必需，并提供内部语言学习支持 | [招聘 FAQ](https://recruit.shippio.io/faq) |
| 各职位语言 | 后端：要求英语，日语受欢迎但非必须；前端：不要求日语，要求商务英语；QA：要求日语和基础英语 | [后端](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)、[前端](https://japan-dev.com/jobs/shippio/shippio-front-end-engineer-dinv1r)、[QA](https://herp.careers/v1/shippioinc/K_l6flVr-n80) |
| 工时制度 | 业务岗弹性工时；产品和开发岗采用専門業務型裁量労働制。后端职位写 9:00–18:00，可灵活调整，并设“meeting friendly hours” | [FAQ](https://recruit.shippio.io/faq)、[职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z) |
| 远程 | FAQ：远程结合各团队到岗；后端：每周最多远程 4 天；TokyoDev：原则上远程、每周到岗一次；Japan Dev：以远程为主、周二必须到岗，须住在东京办公室通勤范围 | [FAQ](https://recruit.shippio.io/faq)、[职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)、[TokyoDev](https://www.tokyodev.com/companies/shippio)、[Japan Dev](https://japan-dev.com/jobs/shippio/shippio-front-end-engineer-dinv1r) |
| 地点 | 东京总部（芝浦）和大阪分部（难波 SkyO 内 WeWork） | [公司页面](https://www.shippio.io/corp/) |
| 签证 | 前端职位称不提供签证支持，仅限日本居民 | [Japan Dev](https://japan-dev.com/jobs/shippio/shippio-front-end-engineer-dinv1r) |
| 薪资 | QA 职位为 500 万–720 万日元；后端与前端职位未披露区间 | [QA](https://herp.careers/v1/shippioinc/K_l6flVr-n80)、[后端](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z) |
| 股权 | 有股票期权制度，细节在招聘流程中说明 | [招聘 FAQ](https://recruit.shippio.io/faq) |
| 休假和试用 | 每年休息 120 天以上、周末休、病假、产假／陪产假／育儿假、婚丧假；试用期 3 个月 | [职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z) |
| 福利 | 搬迁支持和近距离住房补贴、语言学习支持；新设备、会议／研讨会、购书、育儿弹性工时、社保、通勤补贴 | [职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)、[Japan Dev](https://japan-dev.com/companies/shippio) |
| 开发流程 | 2021 工程师访谈称使用 Scrum、两周 sprint（偶尔一周）；后端职位提及 sprint planning 和 stand-up | [2021-11-15 访谈](https://www.shippio.io/news/recruitment-tech-20211115/)、[职位](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-07-29）：公司、服务和招聘网站及其新闻、产品、FAQ 和职位索引；以 Shippio、株式会社Shippio 和曾用名进行的日英文检索；当前及归档的 HERP、TokyoDev 和 Japan Dev 职位；Stoplight 文档；按组织名、公司名和域名进行的 GitHub 检索；安全认证登记和融资数据库。

- **薪资范围。** 只有 QA 职位公开 500万–720万日元；后端称面试时协商，Japan Dev 的前端职位无范围。
- **当前工程人数。** 公司未公布。找到的最具体数字是 [TokyoDev](https://www.tokyodev.com/companies/shippio)“约 60 人、其中 20 名工程师”（无日期，访问于 2026-07-29），以及 [2022-12 SOA 资料](https://speakerdeck.com/shippio/voyage-for-the-future-soa-approach-powered-by-apollofederation)所称当时约 8 名工程师、目标约 20 名；两者均不能证明当前人数。
- **营收。** 只公开倍数（自 2022 年净营收约 20 倍），未公开绝对值。
- **价格。** Shippio Cargo、作为独立产品的 Forwarding 和 Shippio Clear 未公开，只有 Works 有价格。
- **开源。** GitHub 组织 [`shippio`](https://github.com/shippio)有 5 个公开仓库，其中 4 个是 fork（`wkhtmltopdf_binary_gem`、`ghost-website`、`evil-seed`、`gqlgen`）；唯一原创仓库 `slack-tech-support-recorder` 最后推送于 2023-01-29。公司是 [RubyKaigi 2023](https://www.shippio.io/news/rubykaigi2023/) Platinum 赞助商，并获得 [Ruby biz Grand prix 2022](https://www.shippio.io/news/ruby_biz_grand_prix_2022_20221110/)。
- **状态页或公开 SLA。** 未找到。
- **离职率。** 未公开。

### 不同来源之间的不一致

- **资本金：** 含准备金 8.4 亿日元（[公司页](https://www.shippio.io/corp/)；无日期，访问于 2026-07-29）；21.9 亿（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000160.000025761.html)；无日期，访问于 2026-07-29）；含准备金 14.1 亿（[HERP](https://herp.careers/careers/companies/shippioinc)；无日期，访问于 2026-07-29）；13.4 亿（[六周年信息图，2022-07](https://www.shippio.io/news/6th_anniversary_infographics/)）；6.5122 亿（[Series A，2019-11](https://www.shippio.io/news/finance-series-a/)）。数字并非单调增加，各来源未一致说明是单指資本金还是含資本準備金。
- **注册地址：** [PR TIMES 公司资料](https://prtimes.jp/main/html/rd/p/000000160.000025761.html)仍写浜松町ビルディング15階，但公司于 [2025-09-01](https://www.shippio.io/news/press-release/newoffice202509/)宣布迁至 BLUE FRONT SHIBAURA TOWER S；两者都位于芝浦一丁目1番1号。
- **工作语言：** [FAQ](https://recruit.shippio.io/faq)称英语并非必须；[Japan Dev](https://japan-dev.com/companies/shippio)称“English-only workplace”且“不要求日语”；[QA 职位](https://herp.careers/v1/shippioinc/K_l6flVr-n80)要求日语，[应届产品职位](https://herp.careers/v1/shippioinc/ebBahXnjsTY_)要求母语级日语。
- **远程政策：** 后端称每周最多远程 4 天；TokyoDev 称每周到岗一次；Japan Dev 称周二必须到岗；FAQ 称按团队结合远程与到岗。
- **工程负责人头衔：** Ryan O'Connor 于 [2022-11-18](https://www.shippio.io/news/joined-shippio-as-cto-20221118/)被任命 CTO；[2025-10-30 版公司资料](https://speakerdeck.com/shippio/zhu-shi-hui-she-shippiohui-she-shao-jie-zi-liao-20221130)列 Felix Küppers 为 VP of Engineering、未列 CTO，但[前端职位](https://japan-dev.com/jobs/shippio/shippio-front-end-engineer-dinv1r)仍写最终环节为“CTO and CEO interview”。未找到 CTO 变更公告。
- **ISO 27001 有效期：** [2023-05-31 公告](https://www.shippio.io/news/iso-iec270012022/)写至 2026-05-25；[ISMS 登记](https://isms.jp/lst/ind/CR_JQA-IM2002.html)显示 JQA-IM2002 在 JIS Q 27001:2025（ISO/IEC 27001:2022+Amd 1:2024）下有效至 2029-05-25。登记范围为“国際物流プラットフォームの企画・開発・運営・販売”，2023 公告则为“デジタルフォワーディングサービスの企画・開発・運営・販売”。
- **国家覆盖：** 2022 年 7 月称往来 42 国（[信息图](https://www.shippio.io/news/6th_anniversary_infographics/)、[Series B](https://www.shippio.io/news/pressrelease202209-seriesb/)），而 [Forwarding 页面](https://service.shippio.io/forwarding)称海外网络 35 国以上（无日期，访问于 2026-07-29）。两者衡量对象不同，页面均未定义术语。
- **Works 采用情况：** [2025-10-23 公告](https://www.shippio.io/news/press-release/works-1year/)称 80 多家，“多数为 JIFFA 会员”，并将 200 家目标描述为 JIFFA 会员的 35–40%；[Works 页面](https://service.shippio.io/works)（无日期，访问于 2026-07-29）仍写 80 多家和“JIFFA 会员的 15% 以上”。

### 其他

- 业务并非纯 SaaS：公司持有第一、第二类货物利用运输许可和航空货运许可，自营货代，完全持有一家报关公司，并于 2025 年 12 月登记为保险代理店。[Series C 公告](https://www.shippio.io/news/press-release/series-c/)把进一步并购列为资金用途。
- 協和海運收购（2022-09-27，100% 股份；标的成立于 1960 年、位于横滨）有多篇公司和投资者复盘：[Coral Capital（日文）](https://coralcap.co/2024/04/shippio-kyowakaiun/)、[note（日文）](https://note.com/shippio/n/n733feb7e39c6)、[MAcloud journal（日文）](https://journal.macloud.jp/posts/article_0063)。
- [2025-03-12](https://www.shippio.io/news/press-release/newmv/)产品更名：“Any Cargo”改为“Shippio Cargo”，启用 Shippio Platform 总品牌，并公布新使命“産業の転換点をつくる”和愿景“国際物流を、アドバンストに”。2024 和 2025 年初公告仍使用旧名。
- 截至 2026-07-29，公司[新闻索引](https://www.shippio.io/news/press-release/)最近 20 条中有 10 条是展会出展公告。
- API reference 在 [Stoplight](https://shippio.stoplight.io/docs/shippio-api/753cf96a69c40-shippio-api)公开，但产品页面没有链接；[Shippio API 页面](https://service.shippio.io/shippio-api/)引导用户填写联系表。
- 公司新闻索引对最新内容通常比 PR TIMES 慢数小时至数日，本页同时检查了两者。

---

## 资料来源

**官方**

- [公司官网（日文）](https://www.shippio.io/) · [英文](https://www.shippio.io/en/)
- [公司信息——资料、许可、奖项、会员](https://www.shippio.io/corp/) · [英文](https://www.shippio.io/en/corp/)
- [About us](https://www.shippio.io/about/) · [新闻稿索引](https://www.shippio.io/news/press-release/)
- [产品网站——Shippio Platform](https://service.shippio.io/)：[Forwarding](https://service.shippio.io/forwarding) · [Cargo](https://service.shippio.io/cargo) · [Works](https://service.shippio.io/works) · [API 页面](https://service.shippio.io/shippio-api/) · [API reference](https://shippio.stoplight.io/docs/shippio-api/753cf96a69c40-shippio-api) · [案例](https://service.shippio.io/case/all)
- [招聘网站](https://recruit.shippio.io/) · [FAQ](https://recruit.shippio.io/faq) · [应届招聘](https://recruit.shippio.io/newgraduate)
- [HERP 职位](https://herp.careers/v1/shippioinc)：[后端](https://herp.careers/v1/shippioinc/tLtoq_zXXM0Z)、[QA](https://herp.careers/v1/shippioinc/K_l6flVr-n80)、[应届产品](https://herp.careers/v1/shippioinc/ebBahXnjsTY_)
- [技术博客（Medium，英文）](https://techblog.shippio.io/) · [note 文章索引（日文）](https://note.com/shippio/n/n36094bb0a387) · [note（日文）](https://note.com/shippio) · [SOA 迁移](https://note.com/shippio/n/nc56f93ab661b) · [并购一年复盘](https://note.com/shippio/n/n733feb7e39c6)
- [Speaker Deck](https://speakerdeck.com/shippio)：[公司介绍](https://speakerdeck.com/shippio/zhu-shi-hui-she-shippiohui-she-shao-jie-zi-liao-20221130)、[SOA／Apollo Federation](https://speakerdeck.com/shippio/voyage-for-the-future-soa-approach-powered-by-apollofederation)、[Platform vision](https://speakerdeck.com/shippio/shippio-platform-vision-2025-03-2)
- [GitHub 组织](https://github.com/shippio)

**新闻稿（shippio.io，日文，较新在前）**

- [AI 账单项目自动标注 — 2026-07-28](https://www.shippio.io/news/ai-auto-tag/) · [进出口调查 — 2026-07-14](https://www.shippio.io/news/survey-202607/) · [十周年 — 2026-06-24](https://www.shippio.io/news/10thanniversary/)
- [三菱汽车采用 Cargo — 2026-06-15](https://www.shippio.io/news/mitsubishi-motors-cargo/) · [出港前追踪 — 2026-06-12](https://www.shippio.io/news/early-tracking2026/) · [AI 创建货件 — 2026-05-21](https://www.shippio.io/news/ai-shipment/)
- [贸易 DX 行业组织筹委会 — 2026-05-14](https://www.shippio.io/news/press-release/pre-committee/) · [AI-OCR 扩展费用文件 — 2026-05-08](https://www.shippio.io/news/ai-ocr_202605/) · [Cyber Port／NACCS — 2026-04-21](https://www.shippio.io/news/press-release/naccs_202604/)
- [AI-OCR 规则学习 — 2026-04-01](https://www.shippio.io/news/press-release/ai-ocr_rules/) · [FT 高增长榜 — 2026-03-24](https://www.shippio.io/news/ftranking2026/) · [空运自动追踪 — 2026-03-02](https://www.shippio.io/news/press-release/air-tracking/)
- [VP Strategy — 2026-01-20](https://www.shippio.io/news/press-release/vpos_202601/) · [文件集成 API — 2026-01-14](https://www.shippio.io/news/file-api/) · [CEO 新年致辞 — 2026-01-05](https://www.shippio.io/news/press-release/shippio-2026/)
- [保险代理登记 — 2025-12-22](https://www.shippio.io/news/press-release/insurance2025/) · [AI 发票匹配 — 2025-11-18](https://www.shippio.io/news/press-release/ai-invoice/) · [Seino 派驻 — 2025-11-17](https://www.shippio.io/news/press-release/seino_secondment/)
- [Series C — 2025-10-30](https://www.shippio.io/news/press-release/series-c/) · [Works 一周年 — 2025-10-23](https://www.shippio.io/news/press-release/works-1year/) · [協和海運新社长 — 2025-09-19](https://www.shippio.io/news/press-release/kyowa-ceo202509/)
- [Shippio Clear — 2025-09-08](https://www.shippio.io/news/press-release/shippio-clear/) · [迁入 BLUE FRONT — 2025-09-01](https://www.shippio.io/news/press-release/newoffice202509/) · [发票／装箱单 OCR — 2025-08-12](https://www.shippio.io/news/press-release/ai-ocr_ivpl/)
- [API 免费 — 2025-07-23](https://www.shippio.io/news/press-release/apifree202507/) · [AI-OCR 发布 — 2025-04-04](https://www.shippio.io/news/press-release/ai-ocr/) · [使命／愿景与更名 — 2025-03-12](https://www.shippio.io/news/press-release/newmv/)
- [Works 超过 100 账号 — 2025-01-20](https://www.shippio.io/news/shippio-works-accounts/) · [航空货运许可 — 2024-11-21](https://www.shippio.io/news/air/) · [开始应届招聘 — 2024-11-05](https://www.shippio.io/news/newgraduate20241105/)
- [経団連 — 2024-10-01](https://www.shippio.io/news/keidanren/) · [外部董事 — 2024-09-11](https://www.shippio.io/news/outsidedirector2024/) · [Works 发布 — 2024-09-04](https://www.shippio.io/news/shippioworks/)
- [API 发布 — 2024-05-07](https://www.shippio.io/news/shippioapi/) · [METI 研究会 — 2024-03-28](https://www.shippio.io/news/digital_trade_platform/) · [VP HR／Finance — 2024-01-10](https://www.shippio.io/news/join2024_01/)
- [ISO 27001 — 2023-05-31](https://www.shippio.io/news/iso-iec270012022/) · [RubyKaigi — 2023-05-10](https://www.shippio.io/news/rubykaigi2023/) · [Any Cargo — 2023-01-25](https://www.shippio.io/news/any-cargo20230125/)
- [CTO 任命 — 2022-11-18](https://www.shippio.io/news/joined-shippio-as-cto-20221118/) · [Ruby biz — 2022-11-10](https://www.shippio.io/news/ruby_biz_grand_prix_2022_20221110/) · [收购協和海運 — 2022-09-27](https://www.shippio.io/news/pressrelease202209-ma/)
- [Series B — 2022-09-27](https://www.shippio.io/news/pressrelease202209-seriesb/) · [六周年 — 2022-07-20](https://www.shippio.io/news/6th_anniversary_infographics/) · [技术顾问 — 2021-11-16](https://www.shippio.io/news/pressrelease20211116_tech_advisor/)
- [工程师访谈 — 2021-11-15](https://www.shippio.io/news/recruitment-tech-20211115/) · [J-Startup — 2021-10-21](https://www.shippio.io/news/pressrelease20211021_jstart2021/) · [Series A — 2019-11-11](https://www.shippio.io/news/finance-series-a/)

**PR TIMES（日文）**

- [Series C — 2025-10-30](https://prtimes.jp/main/html/rd/p/000000160.000025761.html) · [Series B — 2022-09-27](https://prtimes.jp/main/html/rd/p/000000030.000025761.html) · [首次融资 — 2017-05-08](https://prtimes.jp/main/html/rd/p/000000001.000025761.html)

**第三方报道与档案**

- [BRIDGE — 1.9 亿日元，2018-12（日文）](https://thebridge.jp/2018/12/shippio-fundraising) · [种子轮，2017-05（日文）](https://thebridge.jp/2017/05/circle-in-seed-round-funding)
- [Kepple — Series C（日文）](https://kepple.co.jp/articles/wmpoc4d_59) · [Business Insider Japan — CEO 谈 Series C（日文）](https://www.businessinsider.jp/article/2510shippio-raises-3-billion-yen-and-discusses-japans-startup-market/)
- [PC-Webzine — 多层 AI Agent（日文）](https://www.pc-webzine.com/article/3496) · [Coral Capital — 協和海運收购（日文）](https://coralcap.co/2024/04/shippio-kyowakaiun/)
- [ロジ人 — CEO 访谈（日文）](https://note.com/logizine/n/n4cd2f85fdf0a) · [STARTUPS JOURNAL（日文）](https://startup-db.com/magazine/category/interview/shippio-sato)
- [TokyoDev](https://www.tokyodev.com/companies/shippio) · [Japan Dev](https://japan-dev.com/companies/shippio) · [前端职位](https://japan-dev.com/jobs/shippio/shippio-front-end-engineer-dinv1r)
- [HERP](https://herp.careers/careers/companies/shippioinc) · [STARTUP DB（日文）](https://startup-db.com/companies/OlBVGEVUkeOp5WqM) · [INITIAL／Speeda（日文）](https://initial.inc/companies/A-27893)
- [ISMS 登记 JQA-IM2002（日文）](https://isms.jp/lst/ind/CR_JQA-IM2002.html) · [Crunchbase](https://www.crunchbase.com/organization/shippio-3b46)
