# Tensor Energy

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

Tensor Energy（Tensor Energy株式会社）是一家总部位于福冈、成立于 2021 年 11 月的公司。其产品 **Tensor Cloud** 是面向可再生能源运营商的云平台，覆盖发电预测、财务模拟、资产管理、电池充放电优化和电力市场交易。

- 截至 [2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)，平台覆盖 194 MW、1,000 多个发电站和电池站点；截至 [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)，客户包括 30 多家运营商和聚合商。
- 累计融资 17 亿日元，最近一轮是 [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)完成的 9.5 亿日元 Series A，由 Global Brain 领投。
- 团队约 18 人，来自 9 个国家（[2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)）；内部工作语言为英语（[TokyoDev](https://www.tokyodev.com/companies/tensor-energy)；无日期，访问于 2026-07-29）。
- 后端使用 Go 和 AWS Serverless；公开招聘的工程岗位不要求日语（[职位](https://tensor-career-en.notion.site/Senior-Backend-Engineer-198e97a69a1681db97bed51078da60cc)、[TokyoDev 职位](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)；无日期，访问于 2026-07-29）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | Tensor Energy株式会社 / Tensor Energy Inc. | [公司页面](https://www.tensorenergy.jp/en/company) |
| 成立 | 2021 年 11 月 | [公司页面](https://www.tensorenergy.jp/en/company) |
| 总部 | ONE FUKUOKA BLDG. 7F, 1-11-1 Tenjin, Chuo-ku, Fukuoka 810-0001 | [公司页面](https://www.tensorenergy.jp/en/company) |
| 代表人 | Nana Hori（堀 菜々）、Vincent Filter（フィルター ヴィンセント） | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| 员工人数 | 约 18 人，来自 9 个国家 | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| 内部语言 | 英语 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy)；无日期，访问于 2026-07-29 |
| 客户 | 30 多家发电企业和聚合商 | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| 平台资产 | 194 MW、1,000 多个站点 | [2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) |
| 累计融资 | 17 亿日元 | [2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| 投资者 | Genesia Ventures、Delight Ventures、Global Brain、Globis Capital Partners、Mizuho Capital、Fukuoka Financial Group、Plug and Play | [公司页面](https://www.tensorenergy.jp/en/company) |

公司页面和 TokyoDev 公司资料均为持续更新且没有发布日期的页面；访问于 2026-07-29。

公司公布的项目和奖项包括：[J-Startup KYUSHU（2023-04-18）](https://prtimes.jp/main/html/rd/p/000000004.000096424.html)、[Plug and Play Japan Winter/Spring 2023 Batch（2022-12-01）](https://prtimes.jp/main/html/rd/p/000000142.000028153.html)、[JETRO Global Startup Acceleration Program（2024-09-03）](https://prtimes.jp/main/html/rd/p/000000009.000096424.html)、[东盟市场进入支持项目（2024-08-09）](https://prtimes.jp/main/html/rd/p/000000008.000096424.html)、[High Growth Program FY2026（2026-06-05）](https://prtimes.jp/main/html/rd/p/000000034.000096424.html)。公司曾入驻 Fukuoka Growth Next，并在那里结识了两家投资机构（[BRIDGE，2024-04](https://thebridge.jp/2024/04/tensor-energy-fgn-special)）。

### 公司陈述的市场背景

根据 [Series A 公告，2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)：

- 日本能源自给率约 13%（FY2022，资源能源厅）。
- 光伏和风电限电已扩展至全部 10 个电网区域；东京区域于 2026-03-01 首次限电。
- 自 2026 年 4 月起，小型电池和发电机可以参与需給調整市場。修改《电气事业法》的法案于 2026 年 3 月获内阁通过。

---

## 产品

**Tensor Cloud** 的公开文档位于 [docs.tensorenergy.jp](https://docs.tensorenergy.jp/en/)。功能领域如下。

### 开发／模拟

[模拟](https://docs.tensorenergy.jp/reference/simulations/introduction)，包括 [CAPEX](https://docs.tensorenergy.jp/reference/library/capex) 和 [OPEX](https://docs.tensorenergy.jp/reference/library/opex)库、[场景](https://docs.tensorenergy.jp/reference/library/scenarios/introduction)、[远期价格曲线](https://docs.tensorenergy.jp/technology/simulations/price-forward-curves)、[光伏](https://docs.tensorenergy.jp/technology/simulations/solar)和[电池](https://docs.tensorenergy.jp/technology/simulations/battery)模型、[限电](https://docs.tensorenergy.jp/technology/simulations/curtailment)、[FIP](https://docs.tensorenergy.jp/technology/simulations/fip)、[财务](https://docs.tensorenergy.jp/technology/simulations/financial)和[天气](https://docs.tensorenergy.jp/technology/simulations/weather-model)模型，以及 [SPV 设置](https://docs.tensorenergy.jp/reference/spvs/introduction)。

### 资产管理

[资产列表](https://docs.tensorenergy.jp/reference/assets/asset-list)、地图、时间线、设置、[批量上传](https://docs.tensorenergy.jp/reference/assets/bulk-upload)、标签、文件和[数据覆盖情况](https://docs.tensorenergy.jp/reference/assets/data-coverage)；[账号](https://docs.tensorenergy.jp/reference/asset-management/accounts)；针对 PPA 和双边协议的[合同管理](https://docs.tensorenergy.jp/reference/contracts/introduction)。

### 运营与交易

[预测](https://docs.tensorenergy.jp/reference/forecasting/forecasts)、[平衡组](https://docs.tensorenergy.jp/reference/balancing/balancing-groups)、[平衡计划提交](https://docs.tensorenergy.jp/reference/balancing-operations/submitting-plans)、[发电数据上传](https://docs.tensorenergy.jp/reference/data-uploads/generation-data)、[JEPX 交易](https://docs.tensorenergy.jp/reference/trading/jepx)和[电池优化](https://docs.tensorenergy.jp/technology/operations/battery-optimization)。

### 商业化

产品采用付费订阅，并完整公开价目表。当前版本日期为 [2026 年 1 月](https://docs.tensorenergy.jp/legal/pricing/pricing-2026-01)；[2023 年 6 月](https://docs.tensorenergy.jp/legal/pricing/pricing-2023-06)的旧版本仍在线，说明定价模式至少修改过一次。

定价由不限用户数的每月 workspace 订阅费、按每个登记 kWp 收取的预测和资产管理容量费，以及按量收取的聚合支持费组成。聚合有两种：客户自行处理 JEPX 交易的 SaaS 方案，以及由 Tensor Energy 运营的 BPO 方案。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2024-04 | 152 个光伏站点；目标在 2024 年底达到 400 个 | [BRIDGE](https://thebridge.jp/2024/04/tensor-energy-fgn-special) |
| 2024-09 | 170 多个光伏站点 | [Ambitions](https://ambitions-web.com/articles/tensorenergy) |
| 2026-04-02 | 800 多个站点；30 多家运营商和聚合商；21 个月光伏＋电池运营历史 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) |
| 2026-07-27 | 194 MW、1,000 多个站点，其中低压光伏 1,051 个；高压光伏＋电池运营历史超过 2 年 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 详情 |
|---|---|---|
| [2024-06-03](https://prtimes.jp/main/html/rd/p/000000007.000096424.html) | Kyocera TCL Solar | 熊本光伏＋电池设施投运；[2026-07-27 公告](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)称其为日本首个大型 FIP 共址电池 |
| [2025-03-10](https://prtimes.jp/main/html/rd/p/000000012.000096424.html) | Tokyo Century | 面向 onsite PPA 和 FIP 余电销售、具备需求预测的 Tensor Cloud |
| [2026-02-03](https://prtimes.jp/main/html/rd/p/000000026.000096424.html) | — | 启动低压光伏批量运营支持业务 |
| [2026-02-18](https://prtimes.jp/main/html/rd/p/000000027.000096424.html) | — | 入选低压光伏“FIP 转换＋电池”可行性验证项目 |
| [2026-03-16](https://prtimes.jp/main/html/rd/p/000000028.000096424.html) | Univers | 低压电网电池批量运营聚合业务 |
| [2026-03-30](https://prtimes.jp/main/html/rd/p/000000032.000096424.html) | KS Energy（Higo Bank 集团） | FIP 共址电池聚合，直流连接方式 |
| [2026-04-07](https://prtimes.jp/main/html/rd/p/000000030.000096424.html) | — | 支持 JEPX 新系统迁移 |
| [2026-06-29](https://prtimes.jp/main/html/rd/p/000000035.000096424.html) | — | 为光伏电站 FIT→FIP 转换招募 EPC 合作伙伴 |
| [2026-07-21](https://prtimes.jp/main/html/rd/p/000000037.000096424.html) | LC-JAPAN | 低压电网电池合作 |
| [2026-07-22](https://prtimes.jp/main/html/rd/p/000000036.000096424.html) | Green Road Energy | 低压电网电池合作伙伴 |
| [2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) | Rising Corporation（上市公司） | 低压电网电池合作伙伴 |

### 公开计划

根据 [Series A 公告（2026-04-02）](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)，资金用于：（1）招聘，包括管理人员，并完善销售、服务交付和公司职能；（2）产品开发，推进电池自动运营和资产管理全自动化；（3）扩展至直接收购、运营和管理发电站，最终组建能源资产基金。

低压电池业务的聚合目标为 2028 年 500 台、2030 年 1,000 台（[2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)）。

---

## 创始人

**Nana Hori（堀 菜々）**——共同创始人、代表董事，负责运营和客户关系。

- 2011 年进入可再生能源行业，担任战略顾问，在日本和海外从事电池市场研究、光伏市场进入、电池产品开发和分布式发电项目融资（[Ambitions](https://ambitions-web.com/articles/tensorenergy)、[Venture Café Fukuoka](https://venturecafefukuoka.org/speakers/%E3%83%8A%E3%83%8A-%E5%A0%80/)）。
- 2016 年参与创立可再生能源融资平台 Shift Energy Japan，带领业务开发团队进行光伏项目架构、开发和建设（[Venture Café Fukuoka](https://venturecafefukuoka.org/speakers/%E3%83%8A%E3%83%8A-%E5%A0%80/)）。
- 在从事储能工作期间，于 [2024-04 BRIDGE 访谈](https://thebridge.jp/2024/04/tensor-energy-fgn-special)约六年前搬到福冈。
- 2021 年 11 月共同创立 Tensor Energy。[公司页面](https://www.tensorenergy.jp/en/company)称其拥有 13 年以上可再生能源经验。
- 长篇访谈：[Ambitions（日文）](https://ambitions-web.com/articles/tensorenergy)、[Globis Capital Partners 播客（日文）](https://www.globiscapital.co.jp/ja/podcast/eo-qz_cn7ldz)、[Fukuoka Growth Next 创业故事（日文）](https://growth-next.com/blog/tensor-energy-founding-story)。

**Vincent Filter**——共同创始人、代表董事，负责产品和技术（[公司页面](https://www.tensorenergy.jp/en/company)、[LinkedIn](https://www.linkedin.com/in/vincent-filter-72131860/)）。

- 曾任覆盖电力行业的战略顾问。
- 有 SaaS 开发和商业化经验，以及 UX 设计背景。

**[公司页面](https://www.tensorenergy.jp/en/company)列出的其他管理层**

| 姓名 | 职位 | 公开背景 |
|---|---|---|
| Akira Shirota | COO | 电力和能源行业 30 年以上 |
| Sebastian Watzke | Head of Product | 前 Google、前 Rakuten |
| Riccardo Iacobucci | Principal Energy & Data Scientist | 博士、京都大学 |
| Miguel Acevedo | Infrastructure & IoT | 云和软件 20 年 |
| Macky Tanaka | Head of Design | — |

同一页面还列出了前端、后端、业务开发和数据科学团队成员。

---

## 融资

| 日期 | 轮次 | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2022-03-08 | Seed | 7,000 万日元 | Genesia Ventures | 7,000 万日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000002.000096424.html) |
| 2024-03-27 | Pre-Series A | 4.5 亿日元 | Genesia Ventures 等 | — | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000006.000096424.html)、[Genesia（英文）](https://www.genesiaventures.com/en/investment-tensorenergy-3/) |
| 2025-03-04 | Pre-Series A extension | 1 亿日元 | Globis Capital Partners | 约 7 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000013.000096424.html) |
| 2026-04-02 | Series A | 9.5 亿日元 | Global Brain（领投）、Globis Capital Partners、Delight Ventures | 17 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)、[Kepple（日文）](https://kepple.co.jp/articles/h7tb46tvbss1) |

轮次名称遵循公司公告。[Genesia Ventures](https://www.genesiaventures.com/en/investment-tensorenergy-3/)称 2024 年 3 月是其第三次投资。公司页面另列 Mizuho Capital、Fukuoka Financial Group 和 Plug and Play 为投资者。

2024 年 3 月融资与电池充放电优化服务同时发布（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000006.000096424.html)）。光伏发电预测服务于 [2023 年 6 月](https://prtimes.jp/main/html/rd/p/000000005.000096424.html)正式发布。

---

## 工程

### 技术栈与平台

根据招聘信息和公开文档推断：

- **后端：** Go（[职位](https://tensor-career-en.notion.site/Senior-Backend-Engineer-198e97a69a1681db97bed51078da60cc)）；较早职位接受 Go 或 Rust（[TokyoDev，2025-03-05](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)）。
- **云：** AWS、Serverless 和事件驱动；AWS CDK；AWS IoT Core（[职位](https://tensor-career-en.notion.site/Senior-Backend-Engineer-198e97a69a1681db97bed51078da60cc)、[集成指南](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide)）。
- **前端：** TypeScript（[公司页面](https://www.tensorenergy.jp/en/company)）。
- **接口：** 平台 REST API；电池控制使用基于 TLS 的 MQTT，并以 AsyncAPI 定义（[API 概览](https://docs.tensorenergy.jp/api/overview)）。

### 系统

| 系统 | 作用 | 文档 |
|---|---|---|
| 光伏发电预测 | 针对每座电站用历史数据训练 ML 模型，并与同一电站的物理模拟对比，表现不优于物理模型时拒绝使用。采用四家天气数据，预测 14 天。 | [文档](https://docs.tensorenergy.jp/technology/operations/solar-forecasts) |
| 电价预测 | 每个区域建立 JEPX 日前价格模型，并另建零价格事件概率模型。以 30 分钟粒度预测未来 13 天；每周重训、每日推理。 | [文档](https://docs.tensorenergy.jp/technology/operations/price-forecasts) · [需給調整市場](https://docs.tensorenergy.jp/technology/operations/balancing-market-forecasts) |
| 电池优化 | 混合整数线性规划决定 JEPX 日前市场和 EPRX 一次调整力（FCR）的充放电；围绕 D-1 10:00 gate closure 至少每 30 分钟重算。 | [文档](https://docs.tensorenergy.jp/technology/operations/battery-optimization) |
| 电池／EMS 集成 | AWS IoT Core 上基于 TLS 的 MQTT：遥测上行、调度命令下行；每个站点网关使用一张 X.509 证书；涉及 FCR 时 1 Hz 遥测；断线时本地缓存，重连后补传。 | [指南](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide) · [规格](https://docs.tensorenergy.jp/api/battery-optimization/battery-optimization-specs) |
| 模拟引擎 | 覆盖资产全生命周期的财务和发电建模：CAPEX／OPEX、场景、远期价格曲线、限电、FIP。 | [文档](https://docs.tensorenergy.jp/technology/simulations/introduction) |
| 平台 API | 通过 REST 访问资产、预测和实际数据。 | [文档](https://docs.tensorenergy.jp/api/platform/introduction) |

公开文档使用 Docusaurus 构建。[公开状态页](https://status.tensorenergy.jp/)追踪 Tensor Cloud UI、Platform、User Authentication、Tensor API 和 Documentation。访问于 2026-07-29；当时的过去三个月视图显示 UI、认证和 API 为 100%，平台为 99.988%，并记录 2026-07-28 曾中断 15 分钟。

### 招聘所需技术背景

后端职位要求 Go 生产经验；GraphQL、Kubernetes、DevOps／平台工程、信息安全、AWS CDK 和敏捷开发背景属于优先而非必需（[职位](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)）。这些是招聘信号；产品文档能够确认 AWS CDK 和 IoT 基础设施，但不能证明 GraphQL 或 Kubernetes 已用于生产。

### 行业领域

日本电力市场。工程师需要补的东西：

- 市场机制——JEPX 前日市场按半小时时段交易、前日 10:00 截标，EPRX 一次调整力（FCR），需给调整市场，平衡集团，向 TSO 提交计划值，不平衡责任（[文档](https://docs.tensorenergy.jp/technology/operations/battery-optimization)）
- 补贴与合约制度——FIT、FIP 溢价、FIT 期满后运营、onsite 与 offsite PPA（[文档](https://docs.tensorenergy.jp/reference/contracts/introduction)）
- 电网运营——出力控制及其信号、低压与高压并网的区别、AC 连接／DC 连接／纯并网三种站点形态（[文档](https://docs.tensorenergy.jp/technology/simulations/curtailment)）
- 物理与资产金融——辐照与电站建模、蓄电池荷电状态与循环成本、含 SPV 的 30 年项目现金流（[文档](https://docs.tensorenergy.jp/technology/simulations/financial)）
- 按自身节奏变动的制度——2026 年 4 月改革向低压电源开放需给调整市场，《电气事业法》修正案 2026 年 3 月经内阁会议通过（[2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)）

关于如何获取：招聘把"对能源行业的基本理解与学习意愿"列为优先条件而非必需。公司表示包括工程在内的全体成员都被要求理解行业结构、能源物理、能源经济与法规，并会带成员去现场（[TokyoDev](https://www.tokyodev.com/companies/tensor-energy)）。

### 工作条件

TokyoDev 公司页、职位页和公司招聘页均为持续更新且没有发布日期的页面；访问于 2026-07-29。

| 项目 | 详情 | 来源 |
|---|---|---|
| 语言 | 英语是内部通用语言，也使用西班牙语、日语、德语、法语。工程职位要求商务英语，不要求日语 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy)、[职位](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer) |
| 地点 | 招聘优先福冈市，鼓励但不强制搬迁；福冈员工每周至少到岗 2 天 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| 远程 | 必须位于亚洲时区，每天重叠 4–5 小时；公司跨 CET 和 JST 运作 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| 签证 | 远程工作至少 3 个月后可提供日本签证支持 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| 福利 | 完全远程、福冈办公室作为协作空间、弹性工时、休闲着装、签证支持、股权报酬，以及日本员工的健康保险和年金 | [招聘页面](https://tensor-career-en.notion.site/Customer-Growth-198e97a69a1681198652e60e522b4207) |
| 离职 | 之前两年半有 2 人离职 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |
| 领域要求 | 包括工程师在内的所有成员应理解行业结构、能源物理、能源经济和监管；团队成员会前往现场 | [TokyoDev](https://www.tokyodev.com/companies/tensor-energy) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-07-29）：日英文公司网站、Tensor Cloud 文档及 sitemap、法律与信息安全页面、状态页、公司公告、当前招聘页和 TokyoDev 职位；以 Tensor Energy 和 Tensor Cloud 进行的日英文检索；按组织名、公司名和域名进行的 GitHub 检索；技术会议与演讲检索；投资机构 portfolio 与融资数据库。

- 未找到工程博客、会议演讲或公开的原创开源仓库。
- 所查招聘信息未公开薪资范围（[TokyoDev 职位](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)写“No salary range given”）。
- 已发布的[信息安全政策（2024 年 1 月）](https://docs.tensorenergy.jp/legal/information-security/information-security-2024-01)未列出 ISO 27001 或 SOC 2 等第三方认证。
- Mizuho Capital、Fukuoka Financial Group 和 Plug and Play 的投资轮次未公开。

### 不同来源之间的不一致

- **员工人数：** 16（[TokyoDev](https://www.tokyodev.com/companies/tensor-energy)）；截至 2024 年 9 月为 21 人、10 个国家（[Ambitions](https://ambitions-web.com/articles/tensorenergy)）；18 人、9 个国家（[2026-04-02 公告](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)）；9 人以上、7 个以上国籍（[Wantedly](https://sg.wantedly.com/companies/TensorEnergy)）。
- **轮次名称：** 公司称 2024 年 3 月为 [Pre-Series A](https://prtimes.jp/main/html/rd/p/000000006.000096424.html)；[BRIDGE（2024-04）](https://thebridge.jp/2024/04/tensor-energy-fgn-special)将同一轮报道为“Series A，4.5 亿日元”。
- **远程政策：** [招聘页](https://tensor-career-en.notion.site/Customer-Growth-198e97a69a1681198652e60e522b4207)称“fully remote”；[TokyoDev](https://www.tokyodev.com/companies/tensor-energy)称优先福冈，本地员工每周到岗 2 天。
- **聚合目标：** 相隔一周的两份公告分别称 2028 年达到 1,000 台低压电池（[2026-07-21，LC-JAPAN](https://prtimes.jp/main/html/rd/p/000000037.000096424.html)），以及 2028 年 500 台、2030 年 1,000 台（[2026-07-27，Rising Corporation](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)）。

### 其他

- 公司计划在销售 Tensor Cloud 之外，自行收购运营发电站并组建能源资产基金（[2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html)）。
- 2026 年 7 月一周内公布三项低压电池合作（[LC-JAPAN](https://prtimes.jp/main/html/rd/p/000000037.000096424.html)、[Green Road Energy](https://prtimes.jp/main/html/rd/p/000000036.000096424.html)、[Rising Corporation](https://prtimes.jp/main/html/rd/p/000000038.000096424.html)），此前 2026 年 4 月规则变化刚允许低压资源进入需給調整市場。
- [定价](https://docs.tensorenergy.jp/legal/pricing/pricing-2026-01)、[使用条款](https://docs.tensorenergy.jp/en/legal/terms-of-use/terms-of-use-2026-06)、[产品和技术文档](https://docs.tensorenergy.jp/en/)、[电池集成规格](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide)以及[状态页](https://status.tensorenergy.jp/)均无需登录即可公开访问。

---

## 资料来源

**官方**

- [Tensor Cloud 产品网站（英文）](https://www.tensorenergy.jp/en) · [日文](https://www.tensorenergy.jp)
- [公司页面——团队和投资者](https://www.tensorenergy.jp/en/company) · [新闻稿](https://www.tensorenergy.jp/en/press) · [招聘](https://tensor-career-en.notion.site/) · [状态页](https://status.tensorenergy.jp/)
- [文档首页](https://docs.tensorenergy.jp/en/)：[光伏预测](https://docs.tensorenergy.jp/technology/operations/solar-forecasts) · [电价预测](https://docs.tensorenergy.jp/technology/operations/price-forecasts) · [需給調整市場预测](https://docs.tensorenergy.jp/technology/operations/balancing-market-forecasts) · [电池优化](https://docs.tensorenergy.jp/technology/operations/battery-optimization)
- [电池集成指南](https://docs.tensorenergy.jp/api/battery-optimization/integration-guide) · [规格](https://docs.tensorenergy.jp/api/battery-optimization/battery-optimization-specs) · [变更日志](https://docs.tensorenergy.jp/api/battery-optimization/changelog)
- [API 概览](https://docs.tensorenergy.jp/api/overview) · [平台 REST API](https://docs.tensorenergy.jp/api/platform/introduction)
- [定价 2026-01](https://docs.tensorenergy.jp/legal/pricing/pricing-2026-01) · [定价 2023-06](https://docs.tensorenergy.jp/legal/pricing/pricing-2023-06) · [信息安全政策 2024-01](https://docs.tensorenergy.jp/legal/information-security/information-security-2024-01) · [使用条款 2026-06](https://docs.tensorenergy.jp/en/legal/terms-of-use/terms-of-use-2026-06)

**新闻稿（PR TIMES，日文）**

- [Series A，9.5 亿日元 — 2026-04-02](https://prtimes.jp/main/html/rd/p/000000031.000096424.html) · [Rising — 2026-07-27](https://prtimes.jp/main/html/rd/p/000000038.000096424.html) · [Green Road — 2026-07-22](https://prtimes.jp/main/html/rd/p/000000036.000096424.html) · [LC-JAPAN — 2026-07-21](https://prtimes.jp/main/html/rd/p/000000037.000096424.html)
- [FIT→FIP EPC 招募 — 2026-06-29](https://prtimes.jp/main/html/rd/p/000000035.000096424.html) · [High Growth Program — 2026-06-05](https://prtimes.jp/main/html/rd/p/000000034.000096424.html) · [JEPX 迁移 — 2026-04-07](https://prtimes.jp/main/html/rd/p/000000030.000096424.html)
- [KS Energy — 2026-03-30](https://prtimes.jp/main/html/rd/p/000000032.000096424.html) · [Univers — 2026-03-16](https://prtimes.jp/main/html/rd/p/000000028.000096424.html) · [低压光伏验证 — 2026-02-18](https://prtimes.jp/main/html/rd/p/000000027.000096424.html) · [批量运营支持 — 2026-02-03](https://prtimes.jp/main/html/rd/p/000000026.000096424.html)
- [Globis 追加 1 亿 — 2025-03-04](https://prtimes.jp/main/html/rd/p/000000013.000096424.html) · [Tokyo Century — 2025-03-10](https://prtimes.jp/main/html/rd/p/000000012.000096424.html)
- [Pre-Series A＋电池优化 — 2024-03-27](https://prtimes.jp/main/html/rd/p/000000006.000096424.html) · [Kyocera TCL — 2024-06-03](https://prtimes.jp/main/html/rd/p/000000007.000096424.html)
- [光伏预测 GA — 2023-06-29](https://prtimes.jp/main/html/rd/p/000000005.000096424.html) · [Seed 7,000 万 — 2022-03-08](https://prtimes.jp/main/html/rd/p/000000002.000096424.html)

**第三方报道与档案**

- [Genesia Ventures（英文）](https://www.genesiaventures.com/en/investment-tensorenergy-3/) · [Kepple（日文）](https://kepple.co.jp/articles/h7tb46tvbss1)
- [BRIDGE（日文）](https://thebridge.jp/2024/04/tensor-energy-fgn-special) · [Fukuoka Growth Next（日文）](https://growth-next.com/blog/tensor-energy-founding-story)
- [Ambitions（日文）](https://ambitions-web.com/articles/tensorenergy) · [Globis 播客（日文）](https://www.globiscapital.co.jp/ja/podcast/eo-qz_cn7ldz) · [Solar Journal（日文）](https://solarjournal.jp/product/63870/)
- [TokyoDev 公司页](https://www.tokyodev.com/companies/tensor-energy) · [Senior Go 职位](https://www.tokyodev.com/companies/tensor-energy/jobs/senior-go-software-engineer)
- [Wantedly](https://sg.wantedly.com/companies/TensorEnergy) · [LinkedIn](https://www.linkedin.com/company/tensorenergy) · [Crunchbase](https://www.crunchbase.com/organization/tensor-energy) · [INITIAL／Speeda（日文）](https://initial.inc/companies/A-41638)
