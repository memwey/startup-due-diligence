# Flexport

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

Flexport, Inc. 是 2013 年成立于旧金山的公司。它是持牌货代与报关行，同时运营自己的软件平台：客户通过 [flexport.com](https://www.flexport.com/) 和公开 REST API 订舱海运、空运与卡车运输，完成清关并跟踪货物。2023 年起，它还经营从 Shopify 收购来的电商履约业务。

- 当前招聘信息称，客户每年经由 Flexport 运送"超过 190 亿美元的商品，覆盖 112 个国家"（[职位，更新于 2026-07-09](https://job-boards.greenhouse.io/flexport/jobs/7819181)）。
- 累计融资约 25 亿美元、共十轮；最近一次定价轮为 [2022 年 2 月](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/)的 9.35 亿美元 Series E，估值 80 亿美元（[Crunchbase](https://www.crunchbase.com/funding_round/flexport-series-e--3590ef78)）。
- Shopify 持有约 17%（全面摊薄）。截至 2025-12-31，其权益法账面价值为 6.02 亿美元；其分担的 Flexport 亏损由 FY2024 的 1.38 亿美元收窄至 FY2025 的 4,000 万美元（[Shopify 10-K，2026-02-11 提交](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)）。
- 一则在招职位把技术栈描述为"正从 React/Flow + Ruby on Rails 单体，迁往 React/TypeScript 与 Kubernetes 上的 Kotlin 微服务"（[Senior Software Engineer, Customs，更新于 2026-07-10](https://job-boards.greenhouse.io/flexport/jobs/8000000)）。美国职位公开基本薪资区间。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | Flexport, Inc. | [Shopify 10-K，2026-02-11 提交](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| 成立 | 2013 年 | [Wikipedia](https://en.wikipedia.org/wiki/Flexport)；无发布日期；访问于 2026-07-29 |
| 总部 | 加州旧金山 Phelan Building | [Wikipedia](https://en.wikipedia.org/wiki/Flexport)；无发布日期；访问于 2026-07-29 |
| CEO 兼联合创始人 | Ryan Petersen | [Convoy 出售说明，2025-07-28](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/) |
| 工程人数 | "400 名以上软件工程师" | [关于页面](https://www.flexport.com/company/about-us/)；无发布日期；访问于 2026-07-29 |
| 总人数 | 约 2,100 人（2025 年）——第三方数字，非公司公布 | [Wikipedia](https://en.wikipedia.org/wiki/Flexport)；访问于 2026-07-29 |
| 覆盖范围 | 112 个国家 | [关于页面](https://www.flexport.com/company/about-us/)、[职位，2026-07-09](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| 在招职位 | 共 151 个，其中 18 个与工程相关 | [Greenhouse 招聘板 API](https://boards-api.greenhouse.io/v1/boards/flexport/jobs)；截至 2026-07-29 |
| 工程地点 | 旧金山、阿姆斯特丹、亚特兰大、上海、北京、深圳 | [Greenhouse 招聘板](https://job-boards.greenhouse.io/flexport)；截至 2026-07-29 |
| 投资方 | Y Combinator、First Round Capital、Founders Fund、Google Ventures、DST Global、软银愿景基金、Andreessen Horowitz、MSD Partners、Shopify | [Series E 公告，2022-02-07](https://www.businesswire.com/news/home/20220207005279/en/Flexport-Announces-935-Million-in-Funding-to-Advance-Resiliency-and-Visibility-in-Global-Supply-Chain)、[Wikipedia](https://en.wikipedia.org/wiki/Flexport) |

### 持牌主体

Flexport 不只是软件公司；这些牌照才是它能够作为承运合同当事人介入运输的前提。以下为其自己的[条款页面](https://www.flexport.com/terms-and-conditions/)所述（访问于 2026-07-29）：

| 主体 | 角色 | 所述牌照 |
|---|---|---|
| Flexport International LLC | 国际海运货代 | 持牌 Ocean Transportation Intermediary，FMC# 025219NF |
| Flexport Customs LLC | 美国报关业务 | 持有全国许可的持牌报关行 |

以上均为公司自述。本次调研未将其与 [FMC 公开 OTI 登记](https://www.fmc.gov/about/bureaus-offices/bureau-of-enforcement-investigations-and-compliance-beic/office-of-compliance/ocean-transportation-intermediaries/)或 CBP 记录交叉核对；2026-07-29 尝试访问 FMC 检索端点时返回错误。

### 公司陈述的市场背景

- 全球贸易被描述为"10 万亿美元的行业"，较早的职位文本中则写作"占全球 GDP 12% 的行业"（[职位，2026-07](https://job-boards.greenhouse.io/flexport/jobs/7978127)）。
- CEO 把行业中的人工环节——"人们传来传去 PDF，在企业系统之间搬运数据"——描述为 AI agent 的目标（[Dealroom 记录](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot)；访问于 2026-07-29）。

---

## 产品

### 服务线

海运、空运、卡车运输、报关、B2B 与电商履约、退货、货物保险、贸易融资（"Capital"）、退税（duty drawback）、商品归类、贸易咨询与碳排放报告——各自在 [flexport.com/products](https://www.flexport.com/products/flexport-platform/) 下有独立页面。

### 平台与开发者接口

- [Flexport Platform](https://www.flexport.com/products/flexport-platform/)、[Control Tower](https://www.flexport.com/technology/control-tower/)、[Customs Suite](https://www.flexport.com/technology/customs-suite/) 和 [Flexport Intelligence](https://www.flexport.com/technology/flexport-intelligence/)，分别对应订舱、可视化、报关与分析。
- [Atlas](https://atlas.flexport.com/)——面向公众的全球海运交互视图，包含船舶、港口与航线数据。
- 公开的 [REST API](https://apidocs.flexport.com/)，含 v1/v2/v3 版本管理、里程碑事件 webhook、分页与变更记录，覆盖运单、集装箱、采购订单、订舱、报关单、发票、商品与网络资源。EDI 文档一并发布在 [developers.flexport.com](https://developers.flexport.com/faq/general/)。

产品发布按季节节奏进行：[Winter 2025](https://www.prnewswire.com/news-releases/flexport-unveils-20-tech-and-ai-powered-products-to-modernize-global-supply-chains-302383593.html)（2025-02-24）发布 20 多项产品，含 Flexport Intelligence 与 Control Tower；[Winter 2026](https://www.flexport.com/technology/product-release/winter-2026/) 新增 Atlas、报关行审计工具、关税退款计算器、提升箱量利用率的 AI 拼箱引擎、数字化路由规则、AI 搜索与翻译，以及 NetSuite 与 TikTok Shop 集成。

### 商业化

收入是交易型而非订阅型：客户为实际运输和服务付费，因此有意义的口径是净收入（总收入减去采购运力的成本），而不是总收入。没有公开价目表；平台通过 [flexport.com/rates](https://www.flexport.com/rates/) 按票报价。履约、报关、保险与贸易融资是分别计价的服务。

### 历年公开规模

| 期间 | 公开数字 | 来源 |
|---|---|---|
| 2021 | 收入 33 亿美元；首次盈利，净利润 3,700 万美元 | [Sacra](https://sacra.com/c/flexport/)；访问于 2026-07-29 |
| 2022 | 收入约 41 亿美元（疫情后高点） | [Sacra](https://sacra.com/c/flexport/) |
| 2023 | 收入 16 亿美元 | [Sacra](https://sacra.com/c/flexport/) |
| 2024 | 收入 21 亿美元 | [Sacra](https://sacra.com/c/flexport/) |
| FY2024 | Shopify 分担的 Flexport 亏损：1.38 亿美元 | [Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| FY2025 | Shopify 分担的 Flexport 亏损：4,000 万美元；Shopify 权益法账面价值 6.02 亿美元（2024 年：6.42 亿），可转债公允价值 3.26 亿美元（2024 年：2.91 亿） | [Shopify 10-K，2026-02-11 提交](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| 2025 | 净收入约 4.5 亿美元，上年约 3.5 亿；2025 年之所以盈利，仅因出售 Convoy Platform | [Dealroom 记录](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot)、[Sacra](https://sacra.com/c/flexport/) |
| 2026 目标 | 净收入约 6 亿美元，并实现主营业务盈利 | [Dealroom 记录](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot) |

### 收购与出售

| 日期 | 事件 | 详情 |
|---|---|---|
| 2023-05 | 收购 Shopify Logistics，含 Deliverr | 对价为 Flexport 13% 的全面摊薄股权（含认股权与期权）（[Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)） |
| 2023-11 | 收购已停业数字货运经纪公司 Convoy 的资产 | 报道价格约 1,600 万美元（[FreightWaves](https://www.freightwaves.com/news/less-than-2-years-after-flexport-bought-convoys-tech-stack-its-being-sold-to-dat)） |
| 2025-07-28 | 将 Convoy Platform 出售给 DAT Freight & Analytics | 报道价格约 2.5 亿美元（[GeekWire](https://www.geekwire.com/2025/flexport-is-selling-convoys-technology-to-freight-giant-dat/)）；Flexport 保留了建在其上的数字经纪业务，并称该平台"需要成为中立的基础设施层"（[公司文章，2025-07-28](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)） |

### 公开计划

CEO 称约有 100 项高成本核心流程被列为 AI agent 的目标，其中 5 项已上线并产生节省，2026 年需要交付其余约 80% 才能支撑这笔投入，同时定位向成本领先转变（[Dealroom 记录](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot)；访问于 2026-07-29）。招聘信息描述了旧金山新设的 "Autonomous Freight Systems" 团队，负责建设 AI 驱动的报价与自助订舱，使客户"仅凭技术即可锁定运力，无需客户经理、无需运营介入"（[职位，2026-07-09](https://job-boards.greenhouse.io/flexport/jobs/7819181)）。

---

## 创始人

**Ryan Petersen**——联合创始人兼 CEO。Flexport 曾参加 Y Combinator，早期轮次的投资方包括 Founders Fund、First Round Capital 和 Google Ventures（[Wikipedia](https://en.wikipedia.org/wiki/Flexport)；访问于 2026-07-29）。2022 年他把 CEO 一职交给前亚马逊消费业务负责人 Dave Clark，2023 年 9 月 Clark 辞职后他重新出任 CEO（[Wikipedia](https://en.wikipedia.org/wiki/Flexport)）。公司的战略性文章由他撰写，包括 [Convoy Platform 出售说明（2025-07-28）](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)。

**David Petersen**——[Wikipedia](https://en.wikipedia.org/wiki/Flexport) 将其与 Ryan 并列为联合创始人；公司自身材料只提到 Ryan Petersen。所查阅的资料中未见其在 Flexport 的现任职务。

截至 2026-07-29，flexport.com 上未找到列出现任高管的团队页面。

---

## 融资

| 日期 | 轮次 | 金额 | 投资方 | 来源 |
|---|---|---|---|---|
| 2013–2017 | 种子轮至 Series C | 累计 3.04 亿美元，含 1.1 亿美元 Series C | Founders Fund、First Round Capital、Google Ventures | [Wikipedia](https://en.wikipedia.org/wiki/Flexport) |
| 2019-02 | Series D | 10 亿美元 | 软银愿景基金（领投） | [公司博客](https://www.flexport.com/blog/flexport-secures-usd1-billion-in-funding-led-by-softbank-vision-fund/) |
| 2022-02-07 | Series E | 9.35 亿美元，估值 80 亿美元 | Andreessen Horowitz 与 MSD Partners（共同领投），Shopify、DST Global、Founders Fund、软银愿景基金参与 | [公司博客](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/)、[Business Wire](https://www.businesswire.com/news/home/20220207005279/en/Flexport-Announces-935-Million-in-Funding-to-Advance-Resiliency-and-Visibility-in-Global-Supply-Chain) |
| 2023-05 | 为收购 Shopify Logistics 而发行的股权 | 13% 全面摊薄股权 | Shopify | [Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |
| 2023-12 | 可转债 | 2.6 亿美元 | Shopify | [Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) |

累计融资约 25 亿美元、共十轮（[Tracxn](https://tracxn.com/d/companies/flexport/__MY-G7JqqdTHK8-1y1arkCLJEJeVwbwMgeQLTcMS4Izk/funding-and-investors)；访问于 2026-07-29）。Shopify 的持股在全面摊薄（含认股权与期权）口径下约为 17%，此外还与 Flexport 有商业协议和联合营销协议：FY2025 Shopify 就此确认 900 万美元费用，FY2024 为 400 万美元，FY2025 未确认收入分成（[Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)）。

---

## 工程

### 技术栈与平台

以下来自公司自有招聘板上 2026 年 7 月的在招职位：

| 层次 | 内容 | 证据类型 |
|---|---|---|
| 应用架构 | "正从 React/Flow + Ruby on Rails 单体，迁往 React/TypeScript 与 Kubernetes 上的 Kotlin 微服务" | 由[职位，2026-07-10](https://job-boards.greenhouse.io/flexport/jobs/8000000) 确认 |
| 后端 | Java、Spring Boot、Ruby on Rails；"我们的平台用 Ruby 构建" | 职位中作为团队技术栈陈述，[职位](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| 前端 | React、TypeScript、Next.js | [职位](https://job-boards.greenhouse.io/flexport/jobs/7311835) |
| 云 | AWS | [职位](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| 构建与 CI | Buildkit、GitHub Actions、Gradle、Bazel、npm/pnpm/bun、Go 与 Cargo 工具链、Artifactory/ECR | 平台团队职责范围，[职位 2026-07-13](https://job-boards.greenhouse.io/flexport/jobs/7921068) |
| 基础设施即代码 | Terraform、CloudFormation、CDKTF | 仅为招聘要求，[职位](https://job-boards.greenhouse.io/flexport/jobs/7994947) |
| 数据仓库 | 以"诸如"形式列出 Snowflake、BigQuery、Redshift 或 Databricks | 仅为招聘要求，[职位](https://job-boards.greenhouse.io/flexport/jobs/7449436) |
| AI | LLM agent、RAG、prompt engineering、评估 | AI 职位的必需条件，[职位](https://job-boards.greenhouse.io/flexport/jobs/7311835) |

开源方面：[flexport GitHub 组织](https://github.com/flexport)有 69 个公开仓库（访问于 2026-07-29），多为 Ruby 工具——[rubocop-flexport](https://github.com/flexport/rubocop-flexport)、处理不稳定测试的 [quarantine](https://github.com/flexport/quarantine)，以及 `activejob-limiter`——另有 `vllm-production-stack` 与 `llm-d-deployer` 的 fork，两者都是 LLM 推理服务基础设施。招聘站链接了工程博客 [flexport.engineering](https://flexport.engineering/)；2026-07-29 该站对自动请求无响应。

### 系统

| 系统 | 做什么 | 来源 |
|---|---|---|
| 报价平台与自助订舱 | 面向客户的海运、空运、卡车运价与订舱，由旧金山新设的 AI 优先团队 "Autonomous Freight Systems" 建设 | [职位](https://job-boards.greenhouse.io/flexport/jobs/7819181) |
| 异常处理 AI agent | 发现问题、改航、保持货物流转的 agent，关键环节保留人类专家 | [职位](https://job-boards.greenhouse.io/flexport/jobs/7311835) |
| 报关系统 | 报关单、商品归类与合规，由阿姆斯特丹的专门团队负责 | [职位](https://job-boards.greenhouse.io/flexport/jobs/8000000) |
| 数据基础设施 | 每日处理数百万条供应链事件的管道与架构，支撑货物可视化 | [职位](https://job-boards.greenhouse.io/flexport/jobs/7449436) |
| 开发者平台 | 面向工程组织的构建工具、CI/CD、Kubernetes 与制品基础设施 | [职位](https://job-boards.greenhouse.io/flexport/jobs/7921068) |
| 公开 API 与 EDI | 带版本的 REST API 与 webhook，以及面向企业客户的 EDI 对接 | [API 文档](https://apidocs.flexport.com/) |

### 招聘所需技术背景

区分职位中的必需与优先：

- **AI 职位的必需条件：** 动手做过 agent 模式、RAG、prompt engineering、工具调用与评估，明确要求"超出'了解 AI'的程度"（[职位](https://job-boards.greenhouse.io/flexport/jobs/7975365)）。
- **基础设施职位的必需条件：** 在云上端到端负责生产系统、基础设施即代码、容器与面向服务架构、数据仓库与管道工作（[职位](https://job-boards.greenhouse.io/flexport/jobs/7449436)）。
- **安全职位的必需条件：** 面向多语言代码库的应用安全——Ruby、Java/Kotlin、TypeScript/JavaScript、Python（[职位](https://job-boards.greenhouse.io/flexport/jobs/7921061)）。
- **优先而非必需：** 反而是现有技术栈本身——"有我们技术栈相关经验者优先：Java、Spring Boot、Ruby on Rails、React、AWS"出现在旧金山职位的"加分项"里（[职位](https://job-boards.greenhouse.io/flexport/jobs/7819181)）。

报关职位写明团队"对候选人的技术背景不设限"，招聘站也称欢迎没有货代经验的工程师（[招聘页](https://www.flexport.com/careers/teams/engineering/)；访问于 2026-07-29）。

### 行业领域

工作依托国际货代与报关，与 [Shippio](../shippio/) 属同一领域，但监管范围在美国与欧盟：

- **海关与贸易合规**——报关单、HS 归类、退税、关税退款与报关差错率；Winter 2026 发布中包含审计其他报关行申报的工具和关税退款计算器（[发布页](https://www.flexport.com/technology/product-release/winter-2026/)）。
- **持牌中介**——以 FMC 之下的持牌 OTI 和 CBP 之下的报关行身份运营，决定了软件被允许代客户做哪些事（[条款](https://www.flexport.com/terms-and-conditions/)）。
- **运价经济学**——承运合约与舱位分配、运价表、箱量利用率与拼箱；公司称拼箱算法带来 10% 的运费下降（[关于页面](https://www.flexport.com/company/about-us/)）。
- **单证与数据交换**——采购订单、商业发票、提单，以及企业系统之间的 EDI 报文流转（[API 文档](https://apidocs.flexport.com/)）。

行业知识明确不是招聘前提，公司预期入职后再学。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工程地点 | 旧金山、阿姆斯特丹、亚特兰大、上海、北京、深圳；职位按城市发布 | [招聘板](https://job-boards.greenhouse.io/flexport)；截至 2026-07-29 |
| 公开薪资区间（美国） | Staff Software Engineer（旧金山）基本工资 196,875–246,094 美元；Senior Software Engineer（旧金山）183,000–229,000 美元；Automation Engineer I（亚特兰大）78,400–98,000 美元。区间不含奖金、股权与福利 | [Staff](https://job-boards.greenhouse.io/flexport/jobs/7819181)、[Senior](https://job-boards.greenhouse.io/flexport/jobs/7975365)、[Automation](https://job-boards.greenhouse.io/flexport/jobs/8015840) 职位 |
| 非美国区间 | 所查阅的阿姆斯特丹与中国职位均未公布薪资区间 | [职位](https://job-boards.greenhouse.io/flexport/jobs/7311835) |
| 远程政策 | 所查阅的职位中均未写明远程或混合办公政策 | [招聘板](https://job-boards.greenhouse.io/flexport)；截至 2026-07-29 |
| 第三方薪酬数据 | Levels.fyi 显示 Software Engineer I 为 18.7 万美元，Senior Staff 为 44 万美元以上，总包中位数 26.6 万美元 | [Levels.fyi](https://www.levels.fyi/companies/flexport/salaries/software-engineer)；访问于 2026-07-29 |

---

## 备注

### 未公开披露

2026-07-29 检索范围包括 flexport.com、其招聘与开发者站点、Greenhouse 招聘板、GitHub 以及 Shopify 的 SEC 文件：

- 公司未公布人数、收入或估值。本页所有财务数字要么来自 Shopify 的备案文件，要么来自第三方分析。
- 没有公开价目表或费率表；价格按票报出。
- 所查阅的网站页面未声明任何安全认证（ISO 27001、SOC 2）。
- 没有高管或管理团队页面。
- 招聘站链接的工程博客对自动请求无响应，其内容未被查阅。

### 不同来源之间的不一致

- **估值。** 80 亿美元是 [2022 年 2 月](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/)那一轮的价格，也是多数数据库至今沿用的数字。[Sacra](https://sacra.com/c/flexport/) 依据 Shopify 的持股倒推，估算 2024 年为 38 亿美元。Shopify 自己的 [10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm) 给出的是权益法账面价值，属会计口径，并非估值。三者不可直接比较。
- **收入。** 2024 年的 21 亿美元是总收入；2025 年的约 4.5 亿美元是净收入。两者在流传时常常不带口径说明。
- **人数。** 约 2,100 人（2025 年）出自 [Wikipedia](https://en.wikipedia.org/wiki/Flexport)；公司[关于页面](https://www.flexport.com/company/about-us/)只给出"400 名以上软件工程师"，且无日期。
- **创始人。** [Wikipedia](https://en.wikipedia.org/wiki/Flexport) 将 Ryan 与 David Petersen 并列为联合创始人；公司材料只提到 Ryan Petersen。

### 其他

- Convoy Platform 于 2023 年 11 月买入、2025 年 7 月卖出，前后约 20 个月，报道买价约 1,600 万美元、卖价约 2.5 亿美元；建在其上的经纪业务由 Flexport 保留（[公司文章](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)）。
- 2022 年 12 月至 2024 年 10 月期间报道了四轮裁员，其中 [2023 年 10 月](https://www.cnbc.com/2023/10/12/flexport-is-laying-off-20percent-of-its-workforce.html)约 20%、[2024 年 10 月](https://www.supplychaindive.com/news/flexport-layoffs-fulfillment-forwarding-shopify/728950/)约 2%。
- Shopify 同时是股东、可转债持有人、商业合作方与联合营销对手方（[Shopify 10-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)）。目前它的备案文件是了解 Flexport 财务最可靠的公开窗口。
- 工程分布在美国、荷兰和中国三座城市，最新的 AI 团队职位发布在旧金山与阿姆斯特丹（[招聘板](https://job-boards.greenhouse.io/flexport)；截至 2026-07-29）。

---

## 资料来源

**官方资料**

- [Flexport](https://www.flexport.com/) · [关于](https://www.flexport.com/company/about-us/) · [新闻室](https://www.flexport.com/company/newsroom/) · [博客](https://www.flexport.com/blog/)
- [招聘——工程](https://www.flexport.com/careers/teams/engineering/) · [Greenhouse 招聘板](https://job-boards.greenhouse.io/flexport) · [招聘板 API](https://boards-api.greenhouse.io/v1/boards/flexport/jobs)
- [API 文档](https://apidocs.flexport.com/) · [开发者 FAQ 与 EDI 文档](https://developers.flexport.com/faq/general/)
- [Atlas——公开海运地图](https://atlas.flexport.com/)
- [条款与条件，含牌照声明](https://www.flexport.com/terms-and-conditions/)
- [Flexport Platform](https://www.flexport.com/products/flexport-platform/) · [Control Tower](https://www.flexport.com/technology/control-tower/) · [Customs Suite](https://www.flexport.com/technology/customs-suite/) · [Flexport Intelligence](https://www.flexport.com/technology/flexport-intelligence/) · [运价](https://www.flexport.com/rates/)
- [Winter 2026 产品发布](https://www.flexport.com/technology/product-release/winter-2026/)
- [Why We Bought, Built, and Sold the Convoy Platform，2025-07-28](https://www.flexport.com/blog/why-we-bought-built-and-sold-the-convoy-platform/)
- [Series E 公告，2022-02-07](https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/) · [Series D 公告，2019](https://www.flexport.com/blog/flexport-secures-usd1-billion-in-funding-led-by-softbank-vision-fund/)
- [GitHub 组织](https://github.com/flexport) · [rubocop-flexport](https://github.com/flexport/rubocop-flexport) · [quarantine](https://github.com/flexport/quarantine) · [工程博客](https://flexport.engineering/)

**备案与财务**

- [Shopify FY2025 10-K，2026-02-11 提交](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm)——权益法投资、可转债、关联方协议
- [Shopify 10-Q，2026-05-05 提交](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000019/shop-20260331.htm)
- [Sacra——收入与估值分析](https://sacra.com/c/flexport/)
- [Tracxn——融资历史](https://tracxn.com/d/companies/flexport/__MY-G7JqqdTHK8-1y1arkCLJEJeVwbwMgeQLTcMS4Izk/funding-and-investors) · [Crunchbase Series E](https://www.crunchbase.com/funding_round/flexport-series-e--3590ef78)

**第三方报道**

- [Business Wire——Series E，2022-02-07](https://www.businesswire.com/news/home/20220207005279/en/Flexport-Announces-935-Million-in-Funding-to-Advance-Resiliency-and-Visibility-in-Global-Supply-Chain)
- [PR Newswire——Winter 2025 发布，2025-02-24](https://www.prnewswire.com/news-releases/flexport-unveils-20-tech-and-ai-powered-products-to-modernize-global-supply-chains-302383593.html)
- [GeekWire——Convoy Platform 出售给 DAT，2025](https://www.geekwire.com/2025/flexport-is-selling-convoys-technology-to-freight-giant-dat/) · [FreightWaves](https://www.freightwaves.com/news/less-than-2-years-after-flexport-bought-convoys-tech-stack-its-being-sold-to-dat)
- [CNBC——2023 年 10 月裁员](https://www.cnbc.com/2023/10/12/flexport-is-laying-off-20percent-of-its-workforce.html) · [Supply Chain Dive——2024 年 10 月裁员](https://www.supplychaindive.com/news/flexport-layoffs-fulfillment-forwarding-shopify/728950/)
- [Dealroom——CEO 谈净收入与 AI agent](https://app.dealroom.co/news/note/freight-email-forwarding-reborn-ryan-petersen-on-flexport-s-push-to-600m-the-saas-apocalypse-and-the-cost-leader-pivot)
- [Levels.fyi——薪酬数据](https://www.levels.fyi/companies/flexport/salaries/software-engineer)
- [Wikipedia](https://en.wikipedia.org/wiki/Flexport)
