# New Aim

[English](README.md) | **简体中文**

> 基于公开信息整理的研究笔记。最后更新：2026-07-30。同步至：2026-07-30。
> 每个数字都标注了来源与日期。在依赖这些信息之前，请对照一手来源核实。

## 摘要

New Aim 是一家总部位于墨尔本的电商公司：进口消费品（主要是家具、床品、家电、户外与健身用品），以旗下 31 个自有品牌通过 30 多个澳大利亚零售渠道销售，并自营其他零售商可以接入的仓储、货运与软件系统（[关于我们](https://www.newaim.com.au/about-us)，访问于 2026-07-30）。公司称这一模式为"business-to-many"（B2M）。公司把自己的起点定在 2005 年；创始人 Fung Lam 则表示这门生意"起步于 2003 年的一家 eBay 店铺"（[Stockland 新闻稿，2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)）。公司有三条业务线：自营电商、**Dropshipzone** B2B2C 市场平台，以及 AI 分析产品 **AirOxy**（[Business News Australia，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。

- **营收以带日期的法定区间形式公开**，因为公司须按《现代奴隶制法》申报：FY20 为 2.5–3 亿澳元，FY21 为 3–3.5 亿，FY22、FY23、FY24 均为 3.5–4 亿，**FY25 回落到 3–3.5 亿**（[登记记录](https://modernslaveryregister.gov.au/statements/?q=new+aim)）。见诸媒体的最后一份经审计数据是 FY21：**营收 3.43 亿澳元、净利润 3,900 万澳元**，税前利润超过 6,200 万澳元（[The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)）。
- **21 年间没有披露过任何外部股权融资。** CEO Alex Ji：「我们的成长一直靠自有资金，从未为此接受任何外部股权。」（[2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）2022 年公司曾委任麦格理募集最多 1 亿澳元，但未见任何完成公告。公司正在「考虑潜在的 ASX 上市」。
- **员工约 400 人**，"从澳大利亚墨尔本到中国广州"（[招聘页](https://www.newaim.com.au/careers)），其中自有 IT 与数据团队**约 70 人**（[2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。
- **对一家私营公司而言，技术栈的公开程度罕见地高**，因为有两家云厂商发布了案例研究。New Aim 原本以自建机房为主，后将全部系统迁移到**阿里云**（ECS、ApsaraDB RDS for MySQL、CEN、CDN、OSS），再从 2024 年 3 月起迁往 **Google Cloud**——Compute Engine、Anthos、Cloud SQL、Firestore、BigQuery、Cloud VPN、Cloud Armor、Vertex AI（[阿里云案例](https://www.alibabacloud.com/en/customers/new-aim)、[Google Cloud 案例](https://cloud.google.com/customers/new-aim)）。内部平台名为 **AimCore**，运行在 BigQuery 之上。
- **两份联邦法院判决都围绕 New Aim 如何管理供应商数据。** 一审 [2025] FCA 747 中公司败诉，原因之一是它不给员工配发工作手机、也没有针对供应商信息的保密协议；随后在 **[2026] FCAFC 49**（2026-04-20）就 17 家具名供应商的较窄主张上二审胜诉（[13 Wentworth Chambers](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)、[IP Law Watch，2025-07-21](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 公开品牌 | New Aim | [首页](https://www.newaim.com.au/)，访问于 2026-07-30 |
| 法律名称（现行） | **NEW AIM LTD**，实体类型为"Australian Public Company"（澳大利亚公众公司） | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432)，记录提取于 2026-07-30 |
| 法律名称（近期） | "New Aim Pty Ltd"，在 2025-12-19 签署的 FY25 法定申报文件中被描述为"澳大利亚私人公司"，AirOxy 使用条款（最后更新 2025-10-29）亦用此名 | [FY25 现代奴隶制声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)、[AirOxy 使用条款](https://airoxy.ai/home/terms_of_use) |
| ABN / ACN | ABN 50 115 804 432；ACN 115 804 432 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432)、[条款与条件](https://www.newaim.com.au/terms-and-conditions) |
| ABN 状态 | 自 2005-09-02 起有效；自 2005-10-01 起注册 GST；ABN 最后更新 2026-07-01 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432) |
| 注册商号 | `dropshipzone`，自 2023-08-04 起注册 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432) |
| 成立时间 | 公司把自身起点定在 2005 年；IBISWorld 给出的注册日期为 2005-08-22；创始人把 eBay 生意的起点定在 2003 年 | [关于我们](https://www.newaim.com.au/about-us)、[IBISWorld](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/)、[Stockland，2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion) |
| 总部 | 16-18 Cato St, Hawthorn East VIC 3123；03 9376 0841；info@newaim.com.au。Hawthorn 总部于 2021 年 7 月启用 | [联系页](https://www.newaim.com.au/contact-us)、[新闻，2021 年 7 月](https://www.newaim.com.au/news) |
| 创始人 | Fung Lam（联合创始人兼执行董事）与 Cecilia Chiu（联合创始人兼首席运营官）；**Werner Liu** 被记载为创业时的共同出资人、AFR 年轻富豪榜的共同上榜人，并于 2021 年退出 | [关于我们](https://www.newaim.com.au/about-us)、[CEO Magazine，2019-12](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)、[The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) |
| 员工人数 | "超过 400 名员工，从澳大利亚墨尔本到中国广州"；IBISWorld 记载 2025 年含子公司共 386 人；LinkedIn 显示 201–500 区间 | [招聘页](https://www.newaim.com.au/careers)、[IBISWorld](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/)、[LinkedIn](https://au.linkedin.com/company/new-aim) |
| IT 与数据团队 | 约 70 人，截至 2025-09 | [Business News Australia，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 仓储面积 | 约 70,000 平方米（官网页面，访问于 2026-07-30）；2026-02 为"超过 110,000 平方米"；2026-05 为"超过 120,000 平方米" | [关于我们](https://www.newaim.com.au/about-us)、[Best Managed Companies 页](https://www.newaim.com.au/best-managed-companies)、[BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| 渠道数量 | 关于我们页称"超过 40 个渠道"；2026 年称"超过 30 个主要零售渠道" | [关于我们](https://www.newaim.com.au/about-us)、[BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| 商品范围 | 关于我们页称"450 多条产品线、超过 6,000 个活跃 SKU"；截至 2025-09 为"7,000 多个 SKU、400 多个子类目" | [关于我们](https://www.newaim.com.au/about-us)、[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 供应商 | "今天，在 2024 年，我们有 400 多家供应商"；The Australian 在 2022 年报道"中国 400 多家工厂" | [技术页](https://www.newaim.com.au/technology)、[The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| 累计融资 | 未公布任何外部股权轮次。见`融资` | [BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 工程团队工作语言 | 公司所有公开页面均未说明。中国子公司"支持 IT 与采购职能"；官网提供英文与简体中文 | [FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)、[中文关于我们](https://www.newaim.com.au/zh-cn/about-us) |
| 认证 | 未公布任何认证。见`备注` | — |

奖项与榜单，均以来源自身标注的日期为准：

| 日期 | 荣誉 | 来源 |
|---|---|---|
| [2018-10](https://www.afr.com/work-and-careers/careers/financial-review-fast-100-2018-the-full-list-20181030-h179hx) | AFR Fast 100 第 82 名；2017–18 年营收约 1.2 亿澳元，年均增长 44.3% | 公司[新闻](https://www.newaim.com.au/news)引用 AFR |
| [2019-09](https://www.afr.com/policy/economy/australia-s-top-500-private-companies-revealed-20190902-p52n8c) | 首次入选 AFR / IBISWorld 500 大私营企业，第 349 名 | 公司[新闻](https://www.newaim.com.au/news) |
| [2020-02](https://www.afr.com/work-and-careers/management/fast-100-and-fast-starters-winners-revealed-20200219-p54269) | AFR Fast 100 第 49 名；公司估值 2.8 亿澳元，四年复合增长率 44% | 公司[新闻](https://www.newaim.com.au/news) |
| 2020、2021、2022、2023 | FT / Statista 亚太高增长企业榜，连续四年入选；2023 年榜单按营收增长在澳大利亚排第二 | [FT 2023](https://www.ft.com/high-growth-asia-pacific-ranking-2023)、公司[新闻](https://www.newaim.com.au/news) |
| 2021-11 | AFR 年轻富豪榜：Fung Lam 第 6 名，估计净资产 10.2 亿澳元 | 公司[新闻](https://www.newaim.com.au/news)引用 [AFR](https://www.afr.com/young-rich) |
| 2022-09 / 2024-09 | The Australian / IBISWorld 500 大私营企业：2022 年第 193 名，2024 年第 282 名 | [2022 年 PDF](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a434bf99103902761316fdd_The-Australian-Top-500-Private-Companies_2022.pdf)、公司[新闻](https://www.newaim.com.au/news) |
| 2023-11 | Fung Lam 获 Ethnic Business Awards 之 Henry Ngai 中大型企业类奖项 | 公司[新闻](https://www.newaim.com.au/news) |
| [2026-02-27](https://www.deloitte.com/au/en/about/press-room/deloitte-best-managed-companies-awards-270226.html) | 德勤私人企业「澳大利亚 2025 年最佳管理公司」九家得主之一 | 德勤新闻稿 |
| 2026-04 | 亚太 Stevie 奖组织卓越奖（澳门） | 公司[新闻](https://www.newaim.com.au/news) |

公司把自身所处市场描述为结构性两极化：联合创始人 Cecilia Chiu 撰文称，澳大利亚「690 亿澳元（2024 年）」的电商市场正在分裂为掌控需求的平台与掌控履约基础设施的企业，中间层被挤压（[BNA，2025-12-19](https://www.businessnewsaustralia.com/blog/the-growing-divide-in-australia-s-e-commerce-market)）。这是公司自身的表述，并以赞助会员内容形式发布。

### 品牌与法律实体

| 名称 | 类型 | 关系与期间 | 来源 |
|---|---|---|---|
| NEW AIM LTD | 澳大利亚公众公司，ACN 115 804 432 | 现行注册实体名称，`newaim.com.au` 的运营主体 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432)、[条款](https://www.newaim.com.au/terms-and-conditions) |
| New Aim Pty Ltd | 曾用注册名称，ACN 相同 | 用于 2025-12-19 签署的 FY25 法定申报与 2025-10-29 更新的 AirOxy 条款；官网页脚在 [2025-12-14](http://web.archive.org/web/20251214072201/https://www.newaim.com.au/careers/) 仍为"New Aim Pty Ltd"，现为"New Aim Ltd" | [FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)、[AirOxy 条款](https://airoxy.ai/home/terms_of_use) |
| New Aim Hong Kong Co., Limited（"HKNA"） | 香港控股公司 | 于 2022-01-01 设立，为全资控股公司 | [FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| 广州 New Aim 电子商务有限公司（"GZNA"，Guangzhou New Aim E-commerce Co., Ltd） | 中国公司 | HKNA 的全资子公司；在中国雇员，支持 **IT 与采购** | [FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| 前身中国服务实体 | 独立法律实体，未具名 | FY22 之前通过服务协议为 New Aim 提供包括 IT 与采购在内的专属服务；在 FY21/22 期间清算，员工转入 GZNA | [FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| Dropshipzone | 市场平台品牌 | 自 2023-08-04 起是同一 ABN 下的注册商号。Google Cloud 新闻稿称其为 New Aim 的"子公司 B2B2C 市场平台"；Dropshipzone 隐私声明称由 New Aim Ltd"拥有并运营"，其 API 文档也标注同一 ABN | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432)、[Google Cloud，2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)、[DSZ 隐私声明](https://www.dropshipzone.com.au/privacy_statement) |
| OzPlaza / OzPlaza.living | eBay 店铺 | "由 New Aim 拥有并运营"；2018 年成为第二家评价数突破 100 万的澳大利亚 eBay 卖家 | [Internet Retailing，2018-09](https://internetretailing.com.au/aussie-seller-cracks-ebay-benchmark/) |
| AirOxy | 产品品牌 | 以 New Aim 自有 ACN 运营；条款中署名 New Aim Pty Ltd | [AirOxy 条款](https://airoxy.ai/home/terms_of_use) |

从 `Pty Ltd` 到 `Ltd` 是同一 ACN 上的公司类型变更，而非新设实体。截至 2026-07-30，未找到任何公司公告、申报文件或媒体报道宣布或解释这一变更；见`备注`。

---

## 产品

### 三条业务线

Alex Ji 把 New Aim 描述为三条业务线：覆盖整条供应链的原有自营电商、Dropshipzone 平台，以及 AirOxy（[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。法定申报文件把同一业务描述为四种模式（[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)）：

| 模式 | 内容 |
|---|---|
| Dropshipzone | New Aim 的 B2B 市场平台。New Aim 既是运营方也是平台上的供应商；第三方"DSZ 供应商"直接与零售商签约并自行履约 |
| 线上市场平台 | 通过 Amazon、eBay、Big W、Kogan、Bunnings、Myer、Barbeques Galore、Kmart 直接面向消费者销售（FY25 名单） |
| D2C 品牌网站 | 自有品牌的独立站 |
| 代发货合作 | New Aim 持有库存并代零售商履约，消费者与零售商签约 |

### 自有品牌

[品牌页](https://www.newaim.com.au/brands)列出 31 个品牌（访问于 2026-07-30）：5-Star Chef、Alba、Alfresco、Alpha、Aqua Buddy、Artiss、Cefito、Devanti、Emajin、Embellir、Everfit、Gardeon、Giantz、Giselle Bedding、Glacio、Green Fingers、Grillz、i.Pet、Instahut、Jingle Jollys、Keezi、Leier、Livemor、Lockmaster、Prime Turf、Rigo、Seamanship、Ul-tech、Wanderlite、Weisshorn、Zenses。FY24 法定申报列出其中 11 个及各自的 D2C 域名——`artiss.com.au`、`cefito.com.au`、`devanti.com.au`、`everfit.com.au`、`gardeon.com.au`、`gisellebedding.com.au`、`jinglejollys.com.au`、`ipet-au.com`、`keezi.com.au`、`rigokids.com.au`、`weisshorn.com.au`——FY22 另有 `artissin.com.au` 与 `cosyclub.com.au`（[FY24](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/)、[FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)）。

### Dropshipzone

2012 年在墨尔本上线，由 Cecilia Chiu 创立（[关于页](https://www.dropshipzone.com.au/about_us)、[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。**2022 年 10 月**从类批发平台转型为市场平台，此后 DSZ 供应商直接与零售商签约——公司自己形容这一变化削弱了它对这些供应商劳工实践的监督能力（[FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)）。

- **商业条款：** 免费注册，无前期费用、订阅费或会员费；无最低起订量；需要有效 ABN 或 ACN、公司名称和在线店铺链接，审核通常在 2 个工作日内完成（[FAQ](https://www.dropshipzone.com.au/faq)，访问于 2026-07-30）。
- **商品目录：** "超过 100,000 件可转售商品"（[首页](https://www.dropshipzone.com.au/)，访问于 2026-07-30），分 19 个类目。
- **已公布政策：** 供应商服务水平协议、强制伤害报告、产品安全召回、道德采购、禁售商品、比价、价格欺诈、商品类目资格（[政策页](https://www.dropshipzone.com.au/policy)）。
- **Shopify 应用：** **2020-05-15** 上线，免费安装，14 条评价评分 4.4，开发者地址为 16-18 Cato St（[Shopify 应用商店](https://apps.shopify.com/newaim_app)，访问于 2026-07-30）。
- **零售商 API：** `api.dropshipzone.com.au` 下 10 个公开端点——鉴权、类目列表、类目商品、按 SKU 查商品、商品搜索、库存、运费、区域映射、下单。访问令牌 15 分钟过期；文档限流为每分钟 60 次、每小时 600 次。文档由 apidoc 0.23.0 于 **2021-07-07** 生成，版本 1.0.1（[apidoc](https://www.dropshipzone.com.au/apidoc/index.html)、[api_data.json](https://www.dropshipzone.com.au/apidoc/api_data.json)）。
- 另有一套 **Supplier API** 在 [2022 年 8 月](https://www.retailbiz.com.au/online-retailing/dropshipzone-delivers-new-api-for-data-integration/)宣布为"澳大利亚供应商首创"；未找到任何公开文档。

### AirOxy

公司描述为 AI 驱动的分析与市场情报平台，基于 AimCore 的技术构建并运行在 Google Cloud 上（[Google Cloud，2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)）。**2024 年 7 月**在 Online Retailer 展会试点；Alex Ji 表示首个公开版本发布于"去年年底"，即 2024 年底（[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。2025 年 7 月在悉尼 Google Cloud Summit 上展示（[公司新闻](https://www.newaim.com.au/news)）。

已公布的功能领域（[airoxy.ai](https://airoxy.ai/)，访问于 2026-07-30）：采购价格趋势历史、商品评级、畅销榜、关键词推荐、澳大利亚主要渠道概览，以及 AI 聊天助手。应用自身的路由表另外暴露了 AI 文案写作、AI 图像生成、选品发现，以及带最低价导出的竞品追踪。

2026-07-30 显示的定价（[套餐页](https://airoxy.ai/home/plans)）：

| 套餐 | 价格 | 商品列表 | AI 对话 | AI 图像 | AI 文案 | 团队席位 |
|---|---|---|---|---|---|---|
| Starter | 29 澳元/月 | 最多 500 | 300/月 | 10 点数/月 | 20/月 | 1 |
| Business | 79 澳元/月 | 最多 2,000 | 3,000/月 | 20 点数/月 | 100/月 | 1 |
| Enterprise | 联系销售 | 团队合计最多 20,000 | 30,000/月 | 300 点数/月 | 500/月 | 10（软上限） |

所有套餐都标注盈利能力与毛利分析、覆盖澳大利亚各主要电商平台的数据来源，以及与 Dropshipzone 和 Shopify 的集成。支付仅通过 Stripe，AirOxy 声明不接收或存储卡片信息。模型训练的退出（opt-out）需通过邮件申请（[使用条款，最后更新 2025-10-29](https://airoxy.ai/home/terms_of_use)）。

### 历年公布的规模

| 日期 | 公布数字 | 来源 |
|---|---|---|
| 2013 | 一个 11,000 平方米的租赁仓库 | [The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| 2016 | Stockland Brooklyn 配送中心 5,000 平方米，后扩至 65,000 平方米 | [Stockland，2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion) |
| 2018-09 | OzPlaza.living 成为第二家评价数突破 100 万的澳大利亚 eBay 卖家，全球 83 家之一；99.4% 为好评 | [Internet Retailing](https://internetretailing.com.au/aussie-seller-cracks-ebay-benchmark/)、[CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/) |
| 截至 2020 | 250 多名员工，66,000 平方米仓库，年营业额超过 3 亿澳元 | [阿里云案例研究](https://www.alibabacloud.com/en/customers/new-aim) |
| FY21（至 2021-06-30） | 依据向 ASIC 报送的财务报告：营收 3.43 亿澳元、净利润 3,900 万澳元、税前利润超过 6,200 万澳元 | [The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) |
| 2021 | 约 400 万件包裹；中国员工超过 100 人 | [The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| FY21 | 出货"超过 400 万件产品" | [关于我们](https://www.newaim.com.au/about-us) |
| 2022-08 | 接入澳新 35 个线上市场与零售商渠道；代发货业务约占营收三分之一 | [The Australian](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)、[The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| 2023-09 | 新建 31,500 平方米配送中心，可容纳 32,000 个托盘，150 米雨棚，配备 AGV 与分拣机器人系统，目标 5 星 Green Star 评级 | [公司新闻](https://www.newaim.com.au/news)、[Stockland](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion) |
| 2024-09 | Dropshipzone 上 2,500 多家活跃零售商；覆盖超过二分之一的澳大利亚家庭 | [Google Cloud](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) |
| 2025-09 | 30 多个渠道、7,000 多个 SKU、400 多个子类目，约 400 名员工中约 70 人在 IT 与数据岗 | [BNA](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 2026-02 | "超过 110,000 平方米自管仓储"、"每年处理超过 500 万件"、"数千家零售与中小企业合作伙伴" | [Best Managed Companies 页](https://www.newaim.com.au/best-managed-companies) |
| 2026-05 | "超过 120,000 平方米自管仓储"、"2025 年处理超过 8,000 个标准集装箱"、"每年约 400 万件"，产品送达"超过 70% 的澳大利亚家庭" | [BNA](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| 访问于 2026-07-30 | "自 2005 年以来，我们的产品已进入超过 60% 的澳大利亚家庭"；"每 2 个澳大利亚人中就有 1 人拥有 New Aim 的产品"；"澳大利亚电商前十" | [关于我们](https://www.newaim.com.au/about-us)、[首页](https://www.newaim.com.au/) |

### 已公布的客户与合作方

| 日期 | 对象 | 详情 |
|---|---|---|
| FY22 | Harvey Norman、Coles、Costco、Mosaic Brands、Zanui、Big W、David Jones、Kitchen Warehouse | 定制代发货安排（[FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)） |
| FY24 | Harvey Norman、Coles、Costco、David Jones、Kitchen Warehouse、Everything Caravan & Camping、Lasoo、Ineda、Baby Bunting | 代发货合作方；Mosaic Brands、Zanui、Big W 不再列出（[FY24 声明](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/)） |
| FY25 | Amazon、eBay、Big W、Kogan、Bunnings、Myer、Barbeques Galore、**Kmart** | 市场平台名单；相较 FY24，Catch、Mydeal、WooliesX、Mysale 不再列出（[FY25](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)、[FY24](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/)） |
| [2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) | Google Cloud | 云整合与 AirOxy 共同开发；提及的客户包括 Bunnings、Woolworths、Big W、Baby Bunting |
| [2025-06](https://www.rmit.edu.au/news/ccsri/enhance-ai-driven-ecommerce-solutions) | RMIT 大学 | 与 RMIT 网络安全研究与创新中心、CSIRO Data61 合作研究供应链优化、动态定价与个性化，遵循"隐私设计先行"原则 |
| 2025-10 | Hugo Cross-Border（大健云仓） | 面向进入澳大利亚的跨境卖家的合作（[公司新闻](https://www.newaim.com.au/news)） |
| 2025-11 | 莫纳什大学 | 2025 年澳大利亚本科商业案例竞赛金牌赞助商，案例基于 Dropshipzone 模式（[Monash](https://www.monash.edu/business/news/2025/bright-ideas-shine-at-global-business-challenge)） |
| 2023-10 | Stockland | 承租 Truganina 的 90 Melbourne Drive（Melbourne Business Park）；合作关系始于 2016 年的 Brooklyn 配送中心（[Stockland](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)） |

### 公司表述的计划

2025 年 9 月的 20 周年庆典上，公司提出四大增长引擎：扩大 D2C 电商版图、推动 Dropshipzone 市场平台全球化、升级自有 AI 智能能力、构建"统一的一站式电商生态"（[公司新闻](https://www.newaim.com.au/news)）。2025 年 11 月在深圳的峰会上推出 **New Aim 360**，描述为整合供应链物流、Channel-as-a-Service、AirOxy AI 与售后支持的端到端赋能生态，并称现场有 100 多家企业主动接洽（[公司新闻](https://www.newaim.com.au/news)）。Alex Ji 把 AirOxy 类比为从亚马逊内部系统孵化出的 AWS，并表示公司在权衡多个方案的同时"正在考虑潜在的 ASX 上市"（[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。

---

## 创始人

| 姓名 | 职务 | 来源记载的履历事实 | 来源 |
|---|---|---|---|
| **Fung Lam** | 联合创始人兼执行董事；2025-06-01 之前任 CEO | IT 专业毕业。最初从两元店批量买货在 eBay 转售，"大概从 2003 年"开始使用 eBay；2005 年大学毕业后与 Werner Liu 一起创办 New Aim。2021 年在与共同持股人 Werner Liu 的法律纠纷后取得公司完全控制权。约 1982 年出生（2022 年报道称 40 岁） | [The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf)、[The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)、[CEO Magazine，2019-12](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/) |
| **Cecilia Chiu** | 联合创始人兼首席运营官；此前为首席战略官，2023–24 年奖项通告中职称为 CSO | 2012 年创立 Dropshipzone，被描述为澳大利亚代发货模式的早期引入者。2022 年提到自己"在电商行业 15 年"。她表示自己与丈夫共同创办 New Aim；Fung Lam 另外提到妻子对业务的参与 | [关于我们](https://www.newaim.com.au/about-us)、[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)、[Power Retail，2022-07](https://powerretail.com.au/20-questions-with-cecilia-chiu-co-founder-of-new-aim/)、[BNA，2025-12-19](https://www.businessnewsaustralia.com/blog/the-growing-divide-in-australia-s-e-commerce-market)、[CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/) |
| **Werner Liu** | 前共同持股人，据 AFR 为前执行董事 | 与 Fung Lam 在两人均为大学毕业生时共同出资创办 New Aim。2020 年 AFR 年轻富豪榜与 Fung Lam 并列第 19 名，净资产 2.73 亿澳元，二人均被描述为创始人与执行董事。2021 年与 Lam 分道扬镳；The Australian 报道他将获得约 1.01 亿澳元。他不出现在 New Aim 现有任何页面上 | [CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)、[The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)、[Being Asian Australian 对 2020 年 AFR 年轻富豪榜的整理](https://beingasianaustralian.net/2020/12/24/at-least-14-asian-australians-listed-on-the-afr-young-rich-list/) |

### 主要管理层

[关于我们页](https://www.newaim.com.au/about-us)列出的现任管理层（访问于 2026-07-30）：**Alex Ji**（CEO）、**Cecilia Chiu**（COO）、**Stephen Xiao**（CFO）、**Carrie Hu**（CIO）、**Christine Peng**（CPO——[中文页](https://www.newaim.com.au/zh-cn/about-us)译作首席人力官）。

**Alex（Yiming）Ji**，自 **2025-06-01** 起任 CEO（[公告](https://www.newaim.com.au/new-chapter-new-aim)）：

- 2021 年以首席信息官身份加入 New Aim，后转任首席运营官，2024 年 9 月在 COO 职务上兼任 CTO（[公司新闻](https://www.newaim.com.au/news)）。
- 加入 New Aim 之前，曾在 **NAB、Vocus Group 与 Sportsbet** 担任数据科学高级管理职务；曾任苏州大学客座教授。
- 西北工业大学计算机科学（荣誉）学士，方向为软件工程与人工智能；澳大利亚国立大学信息科学与工程博士。
- 2023 年入选澳大利亚 CIO50，2024 年排名第 7（[CIO50 2024](https://www.cio.com/article/3568346/australias-leading-it-executives-honoured-at-cio50-2024-awards.html)、[获奖者页](https://www.cio.com/awardee/3558026/alex-ji.html)）。

**Carrie Hu** 于 2024 年 9 月晋升 CPO 并加入执行领导团队，获 CIO50 2024「Next CIO Award」，并因包含 Dropshipzone 的工作获 2023 年 Women in Digital Awards 年度数字化转型领袖（[公司新闻](https://www.newaim.com.au/news)）。关于我们页列其为 **CIO**，但 2026 年 6 月一篇文章署名为 **CTO**（[BNA，2026-06-09](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human)）；见`备注`。

**David Huang** 在未标注日期的阿里云案例研究中被引述为"New Aim 首席运营官"，且不出现在公司现有任何页面上（[阿里云](https://www.alibabacloud.com/en/customers/new-aim)，访问于 2026-07-30）。

关于我们页列出公司的职能划分：采购；人力资源与行政；财务与法务；客户服务与质量管理；仓储；IT；渠道；类别。FY25 申报文件把澳大利亚职能列为品牌、渠道、财务、人力资源、数据与分析、数字产品交付、物流与质量管理（[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)）。

---

## 融资

从未公布过任何外部股权轮次。公司的立场由其 CEO 在 2025 年 9 月表述：「我们的成长一直靠自有资金，从未为此接受任何外部股权……我们每年把利润重新投入业务以持续增长。」（[BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）

| 日期 | 事件 | 金额 | 详情 | 来源 |
|---|---|---|---|---|
| 2021 | 创始人股权回购 | 向 Werner Liu 支付约 1.01 亿澳元 | Fung Lam 在与共同持股人 Werner Liu 的法律纠纷后取得完全控制权；The Australian 了解到为支付和解款而举债引发了对债务水平的担忧，顾问机构 **McGrathNicol** 被引入 | [The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) |
| 2022-08 | 融资委任 | 拟募集最多 1 亿澳元，"约 5,000 万至 1 亿澳元换取未披露比例的股份" | 委任麦格理；招商文件代号 **Project Hawkeye**，称 New Aim 为"零售业保守得最好的秘密"，并预测 FY23 营收约 4 亿澳元；目标投资人可能为私募股权 | [The Australian，2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)、[公司新闻](https://www.newaim.com.au/news) |
| 2025-09 | 潜在 ASX 上市 | — | "正在考虑潜在的 ASX 上市"；为支持 AirOxy 推广，正在权衡多个方案 | [BNA，2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 2026-07-30 | 公司类型 | — | ABN 登记现将该实体记录为名称为 NEW AIM LTD 的 **Australian Public Company**；2025-12-19 签署的 FY25 申报仍称其为私人公司 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432)、[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |

截至 2026-07-30，未在任何公开来源中找到 2022 年麦格理委任的完成、撤回或其他结果。

### 法定记录中的营收

每份《现代奴隶制法》声明都会申报其报告期的年度营收区间。这是目前可得的唯一连续、带日期的第一方营收序列：

| 期间 | 申报年度营收 | 声明编号 | 来源 |
|---|---|---|---|
| FY20（2019-07-01 – 2020-06-30） | 2.5–3 亿澳元 | #2022-2472 | [登记](https://modernslaveryregister.gov.au/statements/11261/) |
| FY21 | 3–3.5 亿澳元 | #2022-2473 | [登记](https://modernslaveryregister.gov.au/statements/11270/) |
| FY22 | 3.5–4 亿澳元 | #2022-2476 | [登记](https://modernslaveryregister.gov.au/statements/11271/) |
| FY23 | 3.5–4 亿澳元 | #2023-2889 | [登记](https://modernslaveryregister.gov.au/statements/16116/) |
| FY24 | 3.5–4 亿澳元 | #2024-3204 | [登记](https://modernslaveryregister.gov.au/statements/21077/) |
| FY25（2024-07-01 – 2025-06-30） | **3–3.5 亿澳元** | #2025-3497 | [登记](https://modernslaveryregister.gov.au/statements/26345/) |

IBISWorld 另行报告"2025 年"总营收 356,565,000 澳元、"2024 年"320,514,000 澳元，以及 2025 年含全部子公司 386 名员工（[IBISWorld](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/)）。这些数字与登记记录逐期区间的顺序对不上；见`备注`。

---

## 工程

### 技术栈与平台

New Aim 未公布技术栈页面。下列条目分别由云厂商案例研究、相关公司自己的新闻稿、已公布的 API 文档、HTTP 响应头，以及一个以公司邮箱发布的软件包所证实——每条均标注证据类型。

| 条目 | 详情 | 证据 |
|---|---|---|
| 云，现行 | **Google Cloud**，迁移始于 **2024 年 3 月**。到 2024 年底完成两个阶段，迁移了仓储与订单管理系统以及 Dropshipzone 业务 | 已确认——[Google Cloud 案例研究](https://cloud.google.com/customers/new-aim)、[Google Cloud 新闻稿，2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) |
| 具名的 Google Cloud 产品 | Compute Engine（配 Local SSD 与 Persistent Disk）、企业容器平台 **Anthos**、数据库 **Cloud SQL** 与 **Firestore**、数据仓库 **BigQuery**、Cloud VPN、Cloud Armor、Vertex AI | 已确认——[Google Cloud 案例研究](https://cloud.google.com/customers/new-aim) |
| 生成式 AI | 从 **Vertex AI 的 Model Garden** 中测试并选用模型，在 AirOxy 中用于价格洞察、市场趋势与商品图片优化 | 已确认——[Google Cloud 新闻稿](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) |
| 云，此前 | **阿里云**——Elastic Compute Service、**ApsaraDB RDS for MySQL**、云企业网、CDN、对象存储服务。New Aim 从以自建机房为主的架构"成功将其全部系统迁移到阿里云" | 已确认——[阿里云案例研究](https://www.alibabacloud.com/en/customers/new-aim)，未标注日期；访问于 2026-07-30 |
| 迁移原因 | Google Cloud 案例研究称 New Aim"此前的基础设施服务提供商退出了市场"。阿里云自 2023 年 12 月起通知受影响客户，并于 2024-09-30 停止澳大利亚数据中心运营 | 推断——所有已查阅来源均未指名退出的提供商（[阿里云通知](https://www.alibabacloud.com/en/notice/notice_on_the_ceasing_operation_of_alibaba_cloud_data_centers_in_australia_and_india_351)） |
| 可用性 | 服务可用率从 **97% 提升到 99%**；基础设施事件响应时间从数小时缩短到 15 分钟 | 已确认——[Google Cloud 案例研究](https://cloud.google.com/customers/new-aim) |
| 公司官网 | Webflow，从名为 `newaim-stagging-domain.webflow` 的项目发布，经 Cloudflare 分发 | 已确认——[响应头与页面源码](https://www.newaim.com.au/)，访问于 2026-07-30 |
| Dropshipzone 前端 | **Next.js**（`X-Powered-By: Next.js`、`/_next/static/` 资源路径）。其 `robots.txt` 仍禁止 Magento 时代的路径（`/downloader/`、`/catalogsearch/`、`/catalog/product_compare/`、`LICENSE_AFL.txt`），部分类目 URL 同时存在 `.html` 与简洁两种形式 | 已确认——[响应头](https://www.dropshipzone.com.au/)、[robots.txt](https://www.dropshipzone.com.au/robots.txt)，访问于 2026-07-30 |
| Dropshipzone API | `api.dropshipzone.com.au` 上基于 JSON 的 REST；令牌鉴权，15 分钟过期；文档记载的限流为每分钟 60 次、每小时 600 次，由"API Gateway"执行；文档由 apidoc 0.23.0 于 2021-07-07 生成 | 已确认——[api_project.json](https://www.dropshipzone.com.au/apidoc/api_project.json)、[api_data.json](https://www.dropshipzone.com.au/apidoc/api_data.json) |
| AirOxy 前端 | 运行在 **nginx** 上的 Vite 构建单页应用；React、React Router、Redux 与 MUI，CSV 解析用 PapaParse。**Amplitude** 分析，启用 autocapture 与会话回放，后者在离开公开落地页路由后才惰性加载 | 已确认——[airoxy.ai](https://airoxy.ai/) 页面源码与 JS 包，访问于 2026-07-30 |
| AirOxy 后端主机 | `api.airoxy.com.au` 与 `identity.airoxy.com.au`（独立身份服务）；**Stripe** 计费门户；**Firebase** 服务，包括 Remote Config、Installations 与 `vertexai-preview` SDK；一个名为 `airoxyproductlensdev` 的 **Azure Blob Storage** 账户 | 已确认——已公布的 [AirOxy JS 包](https://airoxy.ai/app-75bf66c1.js)中的字符串引用，访问于 2026-07-30 |
| 公开发布的前端工具 | npm 上的 `@airoxy/create-react`——"an react scaffold using react react-router and redux"，CLI 为 `airoxy-create-react`，2024-02-23 至 2024-02-29 间发布 11 个版本，维护者邮箱 `jack.pan@newaim.com.au` | 已确认——[npm](https://registry.npmjs.org/@airoxy/create-react) |
| 对外提供的集成 | Shopify 与 Magento，"信息双向流动" | 公司表述——[技术页](https://www.newaim.com.au/technology) |
| 内部 HR/ATS 平台 | Employment Hero 用于发布职位；据 FY25 申报，也作为交付培训的"员工管理平台" | 已确认——[招聘页](https://www.newaim.com.au/careers)的链接、[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| 仓储自动化硬件 | 2023 年配送中心的 AGV 与分拣机器人系统；订单履约使用 RF 扫描 | 公司表述——[公司新闻，2023-09](https://www.newaim.com.au/news)、[首页](https://www.newaim.com.au/) |
| 招聘要求 | 软件工程师岗位要求"Java、Python 或类似编程语言" | 仅招聘提及——[LinkedIn 职位（已过期）](https://au.linkedin.com/jobs/view/software-engineer-at-new-aim-4405094003)，2026-07-30 自搜索结果摘要 |

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| **AimCore** | 自研运营平台，被描述为嵌入整条价值链，把采购、进口货运、仓位分配、补货、拣货、发运与售后整合为"一个决策引擎"。运行在 BigQuery 数据仓库上，分析商品采购、物流与仓储数据 | [BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)、[Google Cloud 案例研究](https://cloud.google.com/customers/new-aim) |
| 仓储与订单管理 | 定制的仓库管理系统，加上由内部 IT 团队集成的订单管理系统；下单到仓库拣货之间全自动即时联动 | [技术页](https://www.newaim.com.au/technology) |
| 仓储优化 | 上架模拟以减少叉车行走并最大化立方利用率；补货算法优先服务水平要求最严格的渠道；波次规划优化拣货路径 | [BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| **Postage Optimiser** / 末端邮费优化器（LPO） | 按包裹尺寸、邮编与快递公司在合作网络中选择承运商与服务的调度算法；末端配送路由被描述为使用历史数据、AI 与机器学习。Cecilia Chiu 曾表述为在"五到六家快递公司中选最低费率" | [技术页](https://www.newaim.com.au/technology)、[公司新闻中的 CIO50 2023 引述](https://www.newaim.com.au/news)、[The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| 多渠道数据平台 | 整合 40 个销售渠道数据集的数据平台，见于 Alex Ji 2023 年 CIO50 获奖说明 | [公司新闻，2023-07](https://www.newaim.com.au/news) |
| 预测与需求计划 | 与实时现金流挂钩的销售与预算预测；以 CBM（而非仅件数）跨多站点思考的仓容与 S&OP 计划；一个模型调优工作台，让采购人员把定性信号注入定量预测，并在写入计划前有人工确认环节；一个自然语言数据代理，回答计划人员诸如某子类目库存天数为何下滑之类的问题 | [BNA，2026-06-09](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human) |
| **AirOxy** 决策引擎 | 声称"处理定价、搜索行为、类目排名与竞品动态方面超过 1 亿个数据点"，作为闭环引擎驱动定价、库存分配与渠道策略 | [BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| **Dropshipzone** 市场平台 | 为中小零售商提供商品目录管理、履约，以及与主要零售平台的集成；通过 Shopify 应用与零售商 API 实现商品/库存/订单同步与运费计算 | [BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)、[Shopify 应用](https://apps.shopify.com/newaim_app) |
| AI 客服 | 用自然语言处理对消息分类归类、驱动自动回复并加快响应；声称解决"最多 30% 的 New Aim 商品与客户咨询" | [技术页](https://www.newaim.com.au/technology) |
| AR 虚拟展厅 | 被描述为家居用品品类正在推进中 | [技术页](https://www.newaim.com.au/technology) |

### 招聘所需技术背景

2026-07-30 [招聘页](https://www.newaim.com.au/careers)仅列出三个职位：**Staff Software Engineer**（日期 05-02-2026）、**Quality Control Officer**（05-02-2026）、**Warehouse Picker & Packer – Derrimut/Truganina**（15-06-2025）。前两个职位的 LinkedIn 链接都跳转到 LinkedIn 的 `expired_jd_redirect`，因此无法读取职位内容；仓库岗链接指向 Employment Hero 的一条列表。

2026-07-30 唯一可恢复的工程岗位文本来自一条同样已过期的 **Software Engineer** 招聘：地点 Hawthorn East VIC 3123，坐班、长期、全职；设计、开发、测试、实施并维护支撑 New Aim 电商平台的软件应用、后端服务、平台集成与系统组件；至少 1 年相关经验；具备 Java、Python 或类似编程语言经验（[Employment Hero 列表](https://employmenthero.com/jobs/position/new-aim-software-engineer-lj7cb/)与 [LinkedIn 职位](https://au.linkedin.com/jobs/view/software-engineer-at-new-aim-4405094003)在 2026-07-30 分别返回 404 与过期跳转；文本来自搜索结果索引，因此**未经确认**）。

招聘页的历史快照显示工程岗位在该页上出现得极少：[2025 年 3 月](http://web.archive.org/web/20250315202431/https://www.newaim.com.au/careers/)为仓库、叉车与渠道增长岗，[2025 年 10 月](http://web.archive.org/web/20251006230929/https://www.newaim.com.au/careers/)仅有仓库岗，[2025 年 12 月](http://web.archive.org/web/20251214072201/https://www.newaim.com.au/careers/)为质检加仓库岗。2026 年 2 月的 Staff Software Engineer 是所查阅快照范围内该页首次出现的工程岗位。

### 行业领域

- **大件笨重商品电商。** 公司把大件笨重定义为超过 10 公斤的商品，并称该品类"无法轻易自动化"，需要更多仓储面积、更高接触度的操作、更严格的库存控制和更大的运费波动暴露（[BNA，2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)）。
- **澳大利亚市场平台与全渠道集成**——在 30 至 40 个不同的零售商与市场渠道之间协调商品目录、库存、定价与运费规则。
- **中国采购与跨境供应链。** 自有品牌商品大多在中国制造；集团设有香港控股公司与负责 IT 与采购的广州子公司（[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)）。
- **现代奴隶制、道德采购与产品安全合规。** New Aim 是 2018 年《现代奴隶制法》（联邦）下的报告实体，已提交六份声明；设有木材尽职调查政策、道德采购政策、供应商问卷，自 FY25 起设立管理层风险委员会，并在 FY25 完成统一 ESG 与供应商合规平台的设计，计划 FY26 上线（[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)）。
- **1988 年《隐私法》（联邦）下的澳大利亚隐私原则**，并向香港与中国的关联企业披露信息（[隐私政策](https://www.newaim.com.au/privacy-policy)）。
- **商业秘密与保密法。** 两起联邦法院诉讼都围绕 New Aim 的中国供应商身份是否构成保密信息，以及它如何管理员工对这些信息的访问；见`备注`。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 在招职位 | 2026-07-30 共三个：Staff Software Engineer、Quality Control Officer、Warehouse Picker & Packer。三者中有两个链接已失效 | [招聘页](https://www.newaim.com.au/careers) |
| 地点 | 总部 16-18 Cato St, Hawthorn East VIC 3123；仓库位于墨尔本西部的 Derrimut、Laverton North 与 Truganina；在中国广州设有办公室 | [联系页](https://www.newaim.com.au/contact-us)、[Employment Hero 列表](https://employmenthero.com/jobs/position/new-aim-warehouse-picker-packer-monday-to-wednesday-osc0j/)、[招聘页](https://www.newaim.com.au/careers) |
| 办公政策 | 可恢复的软件工程师招聘写明**坐班**、长期、全职。公司官网任何位置均未公布远程或混合办公政策 | 未经确认的招聘文本；[招聘页](https://www.newaim.com.au/careers) |
| 澳大利亚劳务派遣 | FY22 约 40% 的仓库工人通过四家劳务派遣机构聘用，其中一家为 Sidekicker。**FY25 公司声明在澳大利亚完全没有使用劳务派遣** | [FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)、[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| 签证持有者 | FY22 约 **47%** 的自有仓库员工持工作签证；公司在入职前完成 VEVO 核查，并承诺以员工母语提供文件 | [FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| 中国团队 | FY22 中国客服团队中经两家机构派遣的人员不足 2%，薪酬高于广州法定最低工资。FY25 未使用派遣人员，约 4% 的中国员工为临时员工 | [FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)、[FY25](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| 疫情期间安排 | FY22 办公人员按维州政府要求远程工作；仓库工人作为必要工种在现场工作 | [FY22 声明](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| 培训 | 通过员工管理平台每年向澳大利亚与中国员工提供现代奴隶制培训 | [FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| 薪资、股权、签证赞助、流失率、面试流程、福利 | 所有职位均未公布 | [招聘页](https://www.newaim.com.au/careers) |

有两项员工体验事实来自诉讼记录而非公司材料：在争议所涉期间，New Aim **未向员工配发工作手机**，未限制供应商联系方式在个人设备上的存储方式，未要求离职时删除，也没有专门针对供应商信息的强制保密协议（[IP Law Watch，2025-07-21](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)）。全席法庭后来认定，17 家特定供应商的身份仍属保密信息，并受白标做法与员工访问限制的保护（[13 Wentworth Chambers 关于 [2026] FCAFC 49 的案例说明](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)）。

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-30）：`www.newaim.com.au`，包括其 `robots.txt`（返回空的 200）以及导航与页脚链接的每个页面——首页、about-us、technology、brands（两页分页）、careers、news、partnerships、contact-us、terms-and-conditions、privacy-policy、new-chapter-new-aim、best-managed-companies——以及对应的 `zh-cn` 镜像；`sitemap.xml` 返回 404；`engineering`、`tech`、`blog`、`developers`、`docs`、`api`、`status`、`careers`、`jobs`、`shop` 子域均无法解析；`www.dropshipzone.com.au`，包括 `robots.txt`、`sitemap.xml`、`about_us`、`press`、`faq`、`policy`、`privacy_statement` 与 `apidoc` 文件；`airoxy.ai`，包括落地页、套餐页、使用条款与已公布的 JavaScript 包；澳大利亚商业登记（ABR）；澳大利亚现代奴隶制登记（全部六份声明）；德勤私人企业与 Google Cloud 新闻室；Google Cloud 与阿里云的客户案例研究；对 `newaim`、`new-aim`、`newaim-it`、`dropshipzone`、`airoxy`、`aimcore` 的 GitHub 组织与用户检索；对 `airoxy` 与 `dropshipzone` 的 npm 检索；Shopify 应用商店；LinkedIn 公司页与招聘页上的两个职位链接；以及针对 New Aim 融资、ASX 上市、广州 New Aim、New Aim Hong Kong、Werner Liu 与 New Aim 工程招聘的中英文检索。

- **完全没有工程博客、技术文章或架构材料。** 没有 engineering 或 tech 子域，公司官网没有博客，也没有任何技术演讲记录。已公开的技术细节全部来自两家云厂商的案例研究，以及公司在 Business News Australia 投放的三篇赞助文章。
- **没有开源存在。** 以任何 New Aim、Dropshipzone、AirOxy 或 AimCore 名义的 GitHub 组织均不存在；一个创建于 2025-06-02 的 `newaim-it` GitHub 用户账号有零个公开仓库。唯一的公开产物是一个 npm 包 `@airoxy/create-react`，最后发布于 2024-02-29。
- **任何位置都没有具名的安全认证**——没有 ISO 27001、SOC 2、PCI DSS、IRAP 或等价认证——三个产品域名上都没有安全页、信任中心、子处理者清单或状态页。Cloud Armor 是唯一具名的安全控制措施。
- **2022 年 8 月宣布的 Dropshipzone Supplier API 没有公开文档**，AirOxy 与 AimCore 则完全没有任何 API 文档。官网上的零售商 API 文档生成于 2021 年 7 月，页脚版权写作"©2012-2020"。
- **任何职位（包括当前在招的 Staff Software Engineer）都没有公布薪资区间、股权、签证赞助说明、面试流程、流失率或远程/混合办公政策。**
- **没有按职能或地点划分的工程人数。** 唯一找到的拆分是媒体采访中"约 400 人中约 70 人"在 IT 与数据岗，以及法定声明中把广州子公司描述为支持"IT 与采购"。
- **没有公开经审计的财务报表。** New Aim 向 ASIC 报送报告——FY21 的一份曾被引述——但未在任何公开来源中找到 FY21 之后的年报、资产负债表或利润数字。现代奴隶制登记的区间是唯一连续的第一方营收序列。
- **公司类型从 `Pty Ltd` 变为 `Ltd` 未见任何解释。** 未找到任何公告、申报或文章宣布此事、说明其日期，或将其与 CEO 所称正在考虑的 ASX 上市联系起来。
- **2022 年麦格理委任没有公开报道的结果。** 未找到任何来源说明募资是完成、撤回还是被替代。
- **公司未披露任何估值。** 2.8 亿澳元来自 AFR 2020 年 Fast 100 的评估；Fung Lam 2021 年年轻富豪榜的 10.2 亿澳元是基于其持股对个人净资产的估计，而非公司估值。
- **股权结构未披露。** 未找到任何公司页面或申报说明 2021 年 Werner Liu 退出后的现行持股情况。
- **CIO/CTO 职务的现行名称以及是否有 CTO 都无法明确确定**；见下文。

### 不同来源之间的不一致

- **仓储面积同时存在三个在线数字。** [关于我们](https://www.newaim.com.au/about-us)与[技术页](https://www.newaim.com.au/technology)在 2026-07-30 仍显示约 70,000 平方米，而公司自己的 [2026 年 2 月页面](https://www.newaim.com.au/best-managed-companies)称"超过 110,000 平方米"，[2026 年 5 月](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)称"超过 120,000 平方米"。Google Cloud 的说法是"多个仓库，总计超过 100,000 平方米"。
- **出货件数：** "每年超过 500 万件"（[2026-02](https://www.newaim.com.au/best-managed-companies)）对"每年约 400 万件"（[2026-05](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)）——较晚的数字反而更低。
- **家庭覆盖率：** "超过 60% 的澳大利亚家庭"（[关于我们](https://www.newaim.com.au/about-us)）、"每 2 个澳大利亚人中就有 1 人拥有 New Aim 产品"（[首页](https://www.newaim.com.au/)）、"超过二分之一的家庭"（[Google Cloud，2024](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)）、"超过 70% 的澳大利亚家庭"（[2026-05](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)）。
- **渠道数量：** "超过 40 个渠道"（[关于我们](https://www.newaim.com.au/about-us)）对"超过 30 个主要零售渠道"（[2026-05](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)）与"30 多个线上市场"（[Google Cloud，2024](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)）；[2022 年 8 月](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)为 35 个，[2023 年 10 月](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)为"超过 40 个"。
- **SKU：** 6,000 多个、450 多条产品线（[关于我们](https://www.newaim.com.au/about-us)）对 7,000 多个、400 多个子类目（[2025-09](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）；[2019 年](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)为 6,500 多个。Dropshipzone 另行宣传"超过 100,000 件商品"，其中包含第三方供应商的商品。
- **FY24 与 FY25 的营收在不同来源之间对不上。** 登记记录申报 FY24 为 3.5–4 亿澳元、FY25 为 3–3.5 亿澳元；IBISWorld 公布"2025 年"3.566 亿澳元、"2024 年"3.205 亿澳元——两个量级的年份顺序刚好相反。IBISWorld 可能按发布年而非财年标注报告；两个来源都未说明这一点。
- **自有资金的说法与 2022 年募资。** CEO 表示公司"从未接受任何外部股权"（[2025-09](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)）。如果麦格理的流程没有完成，两种说法可以并存，但没有来源确认这一点；而 The Australian 关于为 2021 年创始人和解举债、以及 McGrathNicol 被引入的报道，公司材料中完全未提及。
- **Carrie Hu 的职务。** [关于我们页](https://www.newaim.com.au/about-us)列为 **CIO**，[中文页](https://www.newaim.com.au/zh-cn/about-us)作首席信息官；[2026-06-09](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human) 署名为 **"CTO from New Aim"**；2024 年 9 月晋升为 **CPO**，2024 年 10 月的 CIO50 条目中称其为**首席产品官**（[公司新闻](https://www.newaim.com.au/news)）。另外，关于我们页上 Christine Peng 的职务也是"CPO"，中文译作首席人力官。
- **同一条 2024 年 10 月新闻中 Alex Ji 的职务**既写作"Our CIO & COO, Alex Ji"，相邻条目又写作在"COO 职务上兼任 CTO"（[公司新闻](https://www.newaim.com.au/news)）。
- **Cecilia Chiu 的职务**在现行关于我们页为 COO，在 Google Cloud 案例研究与 2022 年媒体中为首席战略官，在 2023–24 年奖项通告中为 CSO（[关于我们](https://www.newaim.com.au/about-us)、[Google Cloud 案例研究](https://cloud.google.com/customers/new-aim)、[公司新闻](https://www.newaim.com.au/news)）。
- **成立日期：** 公司称 2005 年、IBISWorld 称 2005-08-22、ABN 自 2005-09-02 起有效，而 Fung Lam 自己说"起步于 2003 年的一家 eBay 店铺"（[Stockland，2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)），以及"eBay 1999 年才开始，我大概从 2003 年就在用了"（[The Australian，2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf)）。
- **创始人有几位。** 现行关于我们页列出两位联合创始人 Fung Lam 与 Cecilia Chiu。CEO Magazine 描述 Fung Lam"与 Werner Liu"一起投资创办 New Aim，2020 年 AFR 年轻富豪榜条目把 Lam 与 Liu 并列为"创始人与执行董事"。Werner Liu 不出现在公司现有任何页面上。
- **Dropshipzone 的公司地位：** Google Cloud 新闻稿称其为"子公司 B2B2C 市场平台"，而 ABN 登记把 `dropshipzone` 记录为 New Aim 自身 ABN 下的商号，Dropshipzone 隐私声明也称由 New Aim Ltd 拥有并运营。未找到任何独立的 Dropshipzone 法律实体。
- **AirOxy 定价与其自身 FAQ 相矛盾。** [套餐页](https://airoxy.ai/home/plans)列出 29 与 79 澳元的月付档位，而同一站点落地页的 FAQ 写着"AirOxy 限时免费！"（均访问于 2026-07-30）。
- **德勤奖项的年份标注。** 公司[新闻页](https://www.newaim.com.au/news)把该奖归入 2026 年 2 月，标题为"澳大利亚 2025 年最佳管理公司"；德勤提及 New Aim 的新闻稿日期为 [2026-02-27](https://www.deloitte.com/au/en/about/press-room/deloitte-best-managed-companies-awards-270226.html)，也称其为 2025 年一批。

### 其他

- **诉讼记录是关于 New Aim 如何运作的最详细独立材料。** *New Aim Pty Ltd v Leung* 涉及一名前员工被指将 New Aim 中国商品供应商的身份与联系方式披露给竞争对手，诉由为违约、违反保密义务，以及违反 2001 年《公司法》（联邦）第 183 条。经过如下：
  - **[2022] FCA 722**——一审法官在就律师如何准备专家报告作出事实认定后，全盘排除了 New Aim 的专家证据（[KHQ Lawyers](https://www.khq.com.au/blog/2023/08/28/new-aim-full-court-clarity-expert-evidence/)）。
  - **[2023] FCAFC 67**——全席法庭一致撤销该判决并命令由另一名法官重审，认定执业律师参与专家证据的起草本身并不构成问题（[KHQ Lawyers](https://www.khq.com.au/blog/2023/08/28/new-aim-full-court-clarity-expert-evidence/)、[Mondaq](https://www.mondaq.com/australia/disclosure-electronic-discovery-privilege/1322382/expert-evidence-new-aim-pty-ltd-v-leung-2023-fcafc-67)）。
  - **[2025] FCA 747**（*No 4*）——重审中法院认定，截至 2021 年 1 月 New Aim 全部供应商的身份与联系方式不具备必要的保密性质，并指出公司未向员工配发工作手机、未限制供应商联系方式在个人设备上的存储、未要求离职时删除、也没有针对供应商信息的专门保密协议（[IP Law Watch，2025-07-21](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)）。
  - **[2026] FCAFC 49**（2026-04-20，Moshinsky、Thawley、Button 三位法官）——全席法庭就涉及 **17 家特定供应商**的较窄主张支持 New Aim 的上诉，认定其身份与联系方式属保密信息，这些供应商是适合澳大利亚市场的可靠现行供应商、识别它们"需要大量精力与时间"，New Aim 通过白标做法与员工访问限制保护了该信息，Leung 先生同时违反了合同保密义务与第 183 条。对两名竞争对手被告的主张被发回重审（[13 Wentworth Chambers](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)）。随后于 2026-06-01 作出费用判决 **[2026] FCAFC 79**。
- **公司的公开技术文字是以赞助内容形式投放的。** 本页引用的四篇 Business News Australia 文章中有三篇标注为 New Aim 或其高管的"Member news brought to you by"；2025 年 9 月关于上市的报道是 Nick Nichols 撰写的记者文章。这些赞助文章中的技术细节，是公司在任何地方公布过的最具体内容。
- **公司官网在 2024 年重建并更换了平台。** 品牌形象于 2024 年 10 月与 Christopher Doyle & Co 合作更新（[Mumbrella](https://mumbrella.com.au/new-aim-refreshes-brand-identity-855087)）；存档页面显示直到 2025 年 12 月官网仍是 WordPress，现网站为 Webflow。`/about_us/` 与 `/careers/` 等旧 URL 仍被 AirOxy 使用条款和第三方页面引用。
- **法定申报中的供应商结构在 FY22 到 FY25 之间发生了明显变化。** DSZ 供应商占供应商总数从约 17% 升至约 24%，澳大利亚运营支持类供应商从约 33% 降至约 25%，中国运营支持类从约 5% 升至约 7%，自有品牌商品供应商从约 45% 降至约 42%（[FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)、[FY25](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)）。
- **FY25 供应商问卷覆盖率大幅提升：** 向约 96% 的一级供应商发放问卷，约 46% 回复，公司称这是 FY24 的九倍。约三分之一的商品供应商供应木材类产品，全部按木材尽职调查政策接受评估（[FY25 声明](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)）。
- **21 年后 eBay 业务仍是具名渠道。** OzPlaza 在 2019 年被描述为约占营收四分之一（[CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)）；eBay 在 FY25 申报中仍被列为市场平台。
- **已公布的 AirOxy 前端包中出现了一个 `airoxyproductlensdev` 的 Azure Blob Storage 主机**，而 2024 年的新闻稿定位为纯 Google Cloud。该名称暗示某个"product lens"功能的开发环境；公司材料从未提及 Azure，也没有提及同名功能。

---

## 资料来源

以下每个链接均在 2026-07-30 检查过。四个来源对自动化请求返回 HTTP 403，但人工仍可访问，因此本页未独立核验其内容：四个 `ft.com` 亚太高增长榜单页面、莫纳什大学 AUBCC 条目，以及 Mumbrella 的品牌形象文章。`austlii.edu.au` 与 `judgments.fedcourt.gov.au` 均拒绝自动访问，因此四份判决通过律所与大律师事务所的案例说明引用，而非判决原文；AFR 与 The Australian 的文章需付费订阅，其中两篇 The Australian 文章引自 New Aim 自己 CDN 上托管的 PDF 副本。

**官方**

- [New Aim — www.newaim.com.au](https://www.newaim.com.au/) · [关于我们](https://www.newaim.com.au/about-us) · [技术](https://www.newaim.com.au/technology) · [品牌](https://www.newaim.com.au/brands) · [招聘](https://www.newaim.com.au/careers) · [新闻](https://www.newaim.com.au/news) · [合作关系](https://www.newaim.com.au/partnerships) · [联系](https://www.newaim.com.au/contact-us)
- [条款与条件](https://www.newaim.com.au/terms-and-conditions) · [隐私政策](https://www.newaim.com.au/privacy-policy)
- [CEO 交接公告 — Fung Lam 于 2025-06-01 交棒 Alex Ji](https://www.newaim.com.au/new-chapter-new-aim)
- [Best Managed Companies 页面，2026 年 2 月](https://www.newaim.com.au/best-managed-companies)
- [中文站](https://www.newaim.com.au/zh-cn/about-us)（ZH）
- [Dropshipzone](https://www.dropshipzone.com.au/) · [关于](https://www.dropshipzone.com.au/about_us) · [媒体](https://www.dropshipzone.com.au/press) · [FAQ](https://www.dropshipzone.com.au/faq) · [平台政策](https://www.dropshipzone.com.au/policy) · [隐私声明](https://www.dropshipzone.com.au/privacy_statement) · [robots.txt](https://www.dropshipzone.com.au/robots.txt)
- [Dropshipzone API 文档](https://www.dropshipzone.com.au/apidoc/index.html) · [api_data.json](https://www.dropshipzone.com.au/apidoc/api_data.json) · [api_project.json](https://www.dropshipzone.com.au/apidoc/api_project.json)
- [AirOxy](https://airoxy.ai/) · [套餐](https://airoxy.ai/home/plans) · [使用条款，最后更新 2025-10-29](https://airoxy.ai/home/terms_of_use)
- [Dropshipzone Shopify 应用，2020-05-15 上线](https://apps.shopify.com/newaim_app)
- [npm — @airoxy/create-react](https://registry.npmjs.org/@airoxy/create-react)
- [LinkedIn — New Aim](https://au.linkedin.com/company/new-aim)

**法定申报与登记**

- [ABN Lookup — NEW AIM LTD，ABN 50 115 804 432](https://abr.business.gov.au/ABN/View?abn=50115804432)
- [澳大利亚现代奴隶制登记 — New Aim 声明](https://modernslaveryregister.gov.au/statements/?q=new+aim)
- [FY25 声明 PDF](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) · [FY24](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/) · [FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)
- 登记条目：[FY20](https://modernslaveryregister.gov.au/statements/11261/) · [FY21](https://modernslaveryregister.gov.au/statements/11270/) · [FY22](https://modernslaveryregister.gov.au/statements/11271/) · [FY23](https://modernslaveryregister.gov.au/statements/16116/) · [FY24](https://modernslaveryregister.gov.au/statements/21077/) · [FY25](https://modernslaveryregister.gov.au/statements/26345/)

**厂商案例研究与新闻稿**

- [Google Cloud — New Aim 案例研究](https://cloud.google.com/customers/new-aim)
- [Google Cloud 新闻稿，2024-09-11 — New Aim Taps Google Cloud](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)
- [阿里云 — New Aim 案例研究](https://www.alibabacloud.com/en/customers/new-aim)（未标注日期；访问于 2026-07-30）
- [阿里云 — 关于停止澳大利亚与印度数据中心运营的通知](https://www.alibabacloud.com/en/notice/notice_on_the_ceasing_operation_of_alibaba_cloud_data_centers_in_australia_and_india_351)
- [Stockland 新闻稿，2023-10-24 — Melbourne Business Park 租约](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)
- [RMIT 大学，2025-06 — AI 驱动电商研究合作](https://www.rmit.edu.au/news/ccsri/enhance-ai-driven-ecommerce-solutions)
- [德勤澳大利亚，2026-02-27 — Best Managed Companies 奖项](https://www.deloitte.com/au/en/about/press-room/deloitte-best-managed-companies-awards-270226.html)
- [莫纳什大学，2025 — AUBCC 案例竞赛](https://www.monash.edu/business/news/2025/bright-ideas-shine-at-global-business-challenge)
- [iTWire，2024-09 — New Aim taps Google Cloud](https://itwire.com/business-it-news/data/new-aim-taps-google-cloud-to-democratise-access-to-generative-ai-and-big-data-for-australian-retailers) · [IT Brief](https://itbrief.com.au/story/new-aim-leverages-google-cloud-to-boost-ai-in-ecommerce)

**第三方报道与档案**

- [Business News Australia，2025-09-29 — New Aim 考虑上市以推进 AI 驱动零售生态计划（记者撰写）](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)
- [Business News Australia，2026-05-01 — New Aim 如何打造澳大利亚最大的大件笨重电商运营（赞助会员内容）](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)
- [Business News Australia，2026-06-09 — 下一个访问你网站的顾客不是人，作者 Carrie Ruan Hu（赞助会员内容）](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human)
- [Business News Australia，2025-12-19 — 澳大利亚电商市场日益扩大的分化，作者 Cecilia Chiu（赞助会员内容）](https://www.businessnewsaustralia.com/blog/the-growing-divide-in-australia-s-e-commerce-market)
- [The Australian，2022-08-15 — 麦格理为"零售业保守得最好的秘密"募集 1 亿澳元（New Aim 托管的 PDF）](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)
- [The Australian，2022-03-25 — Fung Lam 的 New Aim 正在改变澳大利亚零售（New Aim 托管的 PDF）](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf)
- [The Australian / IBISWorld 2022 年 500 大私营企业（New Aim 托管的 PDF）](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a434bf99103902761316fdd_The-Australian-Top-500-Private-Companies_2022.pdf)
- [CEO Magazine，2019 年 12 月 — Fung Lam 专访](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)
- [Power Retail，2022-07 — 20 questions with Cecilia Chiu](https://powerretail.com.au/20-questions-with-cecilia-chiu-co-founder-of-new-aim/) · [Power Retail，2022-10 — 'Become a Superman'](https://powerretail.com.au/become-a-superman-tips-for-success-from-one-of-australias-richest-men/)
- [Internet Retailing，2018-09 — 澳大利亚卖家突破 eBay 里程碑](https://internetretailing.com.au/aussie-seller-cracks-ebay-benchmark/)
- [Retailbiz，2022-08 — Dropshipzone 推出数据集成新 API](https://www.retailbiz.com.au/online-retailing/dropshipzone-delivers-new-api-for-data-integration/)
- [Mumbrella，2024-10 — New Aim 更新品牌形象](https://mumbrella.com.au/new-aim-refreshes-brand-identity-855087)
- [CIO Australia — CIO50 2024 奖项](https://www.cio.com/article/3568346/australias-leading-it-executives-honoured-at-cio50-2024-awards.html) · [Alex Ji 获奖者页](https://www.cio.com/awardee/3558026/alex-ji.html)
- [IBISWorld — New Aim Pty Ltd 公司档案](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/)
- [FT / Statista 亚太高增长企业 2023](https://www.ft.com/high-growth-asia-pacific-ranking-2023) · [2022](https://www.ft.com/high-growth-asia-pacific-ranking-2022) · [2021](https://www.ft.com/high-growth-asia-pacific-ranking-2021) · [2020](https://www.ft.com/high-growth-asia-pacific-ranking-2020)
- [AFR Fast 100 2020](https://www.afr.com/work-and-careers/management/fast-100-and-fast-starters-winners-revealed-20200219-p54269) · [Fast 100 2018](https://www.afr.com/work-and-careers/careers/financial-review-fast-100-2018-the-full-list-20181030-h179hx) · [2019 年 500 大私营企业](https://www.afr.com/policy/economy/australia-s-top-500-private-companies-revealed-20190902-p52n8c) · [年轻富豪榜](https://www.afr.com/young-rich)

**诉讼**

- [13 Wentworth Chambers — New Aim Pty Ltd v Leung [2026] FCAFC 49（2026-04-20，Moshinsky、Thawley、Button 法官）](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)
- [IP Law Watch，2025-07-21 — New Aim misses the mark：New Aim Pty Ltd v Leung (No 4) [2025] FCA 747](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)
- [KHQ Lawyers，2023-08-28 — New Aim：全席法庭澄清专家证据（[2023] FCAFC 67、[2022] FCA 722）](https://www.khq.com.au/blog/2023/08/28/new-aim-full-court-clarity-expert-evidence/)
- [Mondaq — 专家证据：New Aim Pty Ltd v Leung [2023] FCAFC 67](https://www.mondaq.com/australia/disclosure-electronic-discovery-privilege/1322382/expert-evidence-new-aim-pty-ltd-v-leung-2023-fcafc-67)
- [维州大律师公会商事分会案例摘要 — New Aim Pty Ltd v Leung](https://www.vicbar.com.au/Web/Web/Contents/Associations/Commercial/Digest/new-aim-pty-ltd-v-leung.aspx)

**网页存档**

- [招聘页存档，2025-12-14](http://web.archive.org/web/20251214072201/https://www.newaim.com.au/careers/) · [2025-10-06](http://web.archive.org/web/20251006230929/https://www.newaim.com.au/careers/) · [2025-03-15](http://web.archive.org/web/20250315202431/https://www.newaim.com.au/careers/)
