# Jerry

[English](README.md) | **简体中文**

> 基于公开信息整理的研究笔记。最后更新：2026-07-29。同步至：2026-07-29。
> 每个数字都链接到出处并标注日期。在依赖这些信息前请对照一手来源核实。

## 摘要

Jerry（`jerry.ai`，前身域名 `getjerry.com`）是一家总部位于加州帕洛阿尔托的公司，成立于 2017 年，并在 Y Combinator 2017 年夏季批次孵化（[YC 页面](https://www.ycombinator.com/companies/jerry-inc)；无日期，访问于 2026-07-29）。公司持有保险经纪牌照，并运营一款面向消费者的手机应用：在 100 多家承保方之间比较车险、房屋险、租客险和摩托车险，代客完成投保与换保，并在此之上叠加免费的车辆养护功能和基于手机的车联网评分（[产品流程](https://jerry.ai/how-jerry-works/)、[车辆养护](https://jerry.ai/car-care/)、[驾驶安全](https://jerry.ai/driver-safety/)；无日期，访问于 2026-07-29）。收入来自承保方佣金（[FAQ](https://jerry.ai/faq/)）。此外，公司把为自身客服搭建的生成式 AI 智能体平台作为独立产品 Propelix 对外销售。

- **规模与融资：** 500 万以上客户，累计融资 2.42 亿美元（截至 2023 年 Series C2），最近一次公开估值为 2021 年 Series C 时的 4.5 亿美元（[Series C 新闻稿，2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/)、[Carrier Management，2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm)）。
- **公司自称已盈利。** 招聘描述称"自 2024 年起盈利"、"收入增长 70 倍"；LinkedIn 页面称 2025 年收入同比增长 68%（[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)，访问于 2026-07-29；[LinkedIn](https://www.linkedin.com/company/jerryinc)，访问于 2026-07-29）。
- **技术栈** —— 由公开资产确认的部分：Kong 3.9.3 网关、nginx、AWS（CloudFront、S3、Lambda@Edge）、NestJS、React/Next.js、Contentful、自建 Sentry、Datadog RUM、GrowthBook，市场站点用 WordPress。来自已关闭招聘岗位的部分：Node.js + TypeScript、Go、Python、React Native、Postgres、Redis、DynamoDB、ClickHouse。
- **目前没有任何工程岗位在招。** 截至 2026-07-29，招聘板列出 47 个岗位：保险 15、数据 13、市场 10、产品 7、商务拓展 2，工程为零（[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)）。同一招聘板此前发布过工程岗位——多伦多应届生岗位于 [2025-11-24](https://builtintoronto.com/job/software-engineer-entry/7776678) 下架——如今这些岗位在接口中返回空。
- **AI 平台完全自研，并正在产品化。** 招聘描述称该系统自动处理"超过 70% 的销售与服务入站请求（每月 5 万余次会话）"，早于市面成品方案自建，提示词"分散在六个不同位置"；同一平台以 [Propelix](https://propelix.ai) 对外销售，其条款写明该产品"是 Jerry Services, Inc. 的产品"（[Propelix 使用条款](https://propelix.ai/terms)；最后更新 2025-10-22）。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | Jerry；宣传语为"美国第一款也是唯一一款 AllCar™ 应用" | [about](https://jerry.ai/about/)、[LinkedIn](https://www.linkedin.com/company/jerryinc) |
| 母公司实体 | Jerry Services, Inc. | [保险牌照页](https://jerry.ai/insurance-licenses/)、[使用条款](https://jerry.ai/terms-of-use/) |
| 持牌经纪实体 | Jerry Insurance Agency, LLC——"Jerry Services, Inc. 的全资子公司" | [保险牌照页](https://jerry.ai/insurance-licenses/) |
| 其他被点名实体 | Jerry Offers Inc. | [隐私政策](https://jerry.ai/privacy-policy/)；更新于 2026-07-20 |
| 牌照编号 | 全国销售人员编号（NPN）18788611；加州本州牌照 0M34848；在全部 50 个州及华盛顿特区持牌 | [保险牌照页](https://jerry.ai/insurance-licenses/) |
| 地址 | 430 Sherman Ave, Suite 305, Palo Alto, CA 94306 | [使用条款](https://jerry.ai/terms-of-use/)；更新于 2024-01-17 |
| 成立时间 | 2017 年；Y Combinator 2017 夏季批次 | [about](https://jerry.ai/about/)、[YC 页面](https://www.ycombinator.com/companies/jerry-inc) |
| 应用上线 | 公司称 2019 年 1 月；iOS 商店记录的首次发布日期为 2017-11-11 | [about](https://jerry.ai/about/)、[iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950) |
| 创始人 | Art Agrawal（CEO）、Musawir Shah（CTO）、Lina Zhang（运营副总裁） | [团队页](https://jerry.ai/team/) |
| 客户数 | 500 万以上（2024 年达到 500 万） | [about](https://jerry.ai/about/) |
| 比价承保方数量 | 100 多家 | [产品流程](https://jerry.ai/how-jerry-works/) |
| 累计融资 | 截至 2023 年 Series C2 为 2.42 亿美元；2026 年公司材料写"2.4 亿美元以上" | [Carrier Management，2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm)、[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 员工人数 | 公司未公布。YC 页面 225；Built In 296；LinkedIn 区间 201–500，平台上有 402 份档案 | [YC 页面](https://www.ycombinator.com/companies/jerry-inc)、[Built In](https://builtin.com/company/jerry)、[LinkedIn](https://www.linkedin.com/company/jerryinc) |
| 办公地点 | 2026 年招聘描述写"完全远程，在帕洛阿尔托、纽约、芝加哥和多伦多设有办公室" | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 工程团队工作语言 | 英语；历史上的工程据点是多伦多和旧金山湾区 | [Built In Toronto 岗位](https://builtintoronto.com/job/software-engineer-entry/7776678)；2025-11-24 下架 |
| GitHub 组织 | [getjerry](https://github.com/getjerry)，已认证，创建于 2017-05-16，地点帕洛阿尔托，32 个公开仓库 | [GitHub API](https://api.github.com/orgs/getjerry) |
| 联系方式 | hi@jerry.ai、press@jerry.ai、recruiting@jerry.ai；833-445-3779 | [about](https://jerry.ai/about/)、[新闻页](https://jerry.ai/news/)、[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

公司在自有页面上列出的奖项：Forbes 与 Statista 的美国最佳创业雇主（2021、2022、2024，新闻页另链接了 2026 年榜单）、Y Combinator Top Companies、Comparably 最佳企业文化、Top 50 Inspiring Workplaces、LinkedIn 2021 年最佳初创公司，以及 Financial Technology Report 的 Top 50 InsurTech CEO 入选（[about](https://jerry.ai/about/)、[新闻页](https://jerry.ai/news/)）。Jerry 在 [2026 年 Forbes 榜单](https://www.forbes.com/lists/americas-best-startup-employers/)中的具体名次在 2026-07-29 未能取得。

### 品牌与法律实体

| 名称 | 类型 | 角色 | 来源 |
|---|---|---|---|
| Jerry Services, Inc. | 母公司 | 被列为经纪实体的母公司、App Store 与 Google Play 的开发者主体，以及 Propelix 的所有者 | [保险牌照页](https://jerry.ai/insurance-licenses/)、[iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950)、[Propelix 使用条款](https://propelix.ai/terms) |
| Jerry Insurance Agency, LLC | 子公司 | 持牌保险销售主体，本州为加州 | [保险牌照页](https://jerry.ai/insurance-licenses/) |
| Jerry Offers Inc. | 关联实体 | 在隐私政策中与经纪实体并列出现，未说明职能 | [隐私政策](https://jerry.ai/privacy-policy/) |
| ISU Insurance Agency Network | 第三方 | 出现在使用条款中，页面未解释关系 | [使用条款](https://jerry.ai/terms-of-use/) |
| `getjerry.com` | 旧域名 | 仍作为内部域名在用——Sentry、GrowthBook 以及 CTO 的开发者邮箱都在该域下 | [jerry.ai 的 CSP 响应头](https://jerry.ai/)、[Google Play 页面](https://play.google.com/store/apps/details?id=com.jerrym) |

未取得任何工商登记记录，见`备注`。

---

## 产品

### 保险——PriceProtect™

[流程](https://jerry.ai/how-jerry-works/)分四步：收集驾驶人、车辆与现有保单信息，字段"由公开记录预填"；返回"最多 20 条初始报价"；在应用内完成购买，由 Jerry 处理文书并取消原保单；随后持续监测市场费率并在合适时提示重新比价。覆盖险种为[车险](https://jerry.ai/car-insurance/)、[房屋险](https://jerry.ai/home-insurance/)、[租客险](https://jerry.ai/renters-insurance/)和[摩托车险](https://jerry.ai/motorcycle-insurance/)。持牌坐席全天候在线聊天，电话时段为周一至周五东部时间 08:00–24:00、周末 08:00–18:30（[FAQ](https://jerry.ai/faq/)）。

### 车辆养护——GarageGuard™

[免费，且无需持有 Jerry 保单](https://jerry.ai/car-care/)：基于年份/品牌/车型/里程生成保养记录与提醒、基于 VIN 的召回查询、自然语言故障排查、24–48 小时内汇总周边修理厂的维修报价、车辆估值以及证件资料存储。2023 年推出（[about](https://jerry.ai/about/)）。

### 驾驶安全——DriveShield™

[基于手机的车联网](https://jerry.ai/driver-safety/)，无需硬件：对行程评分，积分与每周挑战计入州内排行榜，用户可"在参与的承保方处获得保费折扣"。页面写明驾驶数据只在有利于费率时、且经用户授权后才共享给承保方。2023 年推出（[about](https://jerry.ai/about/)）。

### Propelix

一款独立的 B2B 产品：面向受监管行业的提示词管理与虚拟坐席平台，提供提示词版本控制、对照生产日志的测试与调试、发布监控、用于个性化回复的实时数据接入，以及知识库管理（[propelix.ai](https://propelix.ai)；无日期，访问于 2026-07-29）。其条款写明该产品"是 Jerry Services, Inc. 的产品"（[Propelix 使用条款](https://propelix.ai/terms)；最后更新 2025-10-22）。在 [2024 年 4 月的 CIO 访谈](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)中，Jerry 首席运营官 John Spottiswood——在该访谈中的身份是 Propelix 总裁——称它"本质上是 AI 虚拟坐席领域的 GitHub"，说它支持团队在 OpenAI、Anthropic、Google 和 Mistral 模型之上构建，覆盖聊天、语音、短信和邮件渠道，并表示它是"为了解决我们在 Jerry 自己遇到的需求"而做的。

### ChatGPT 集成

2026 年 3 月，Jerry 宣布在 ChatGPT 应用内先后上线维修费用估算和车险报价，数据来自其修理厂与承保方数据（[Carrier Management，2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm)）。该报道指出承保不在 ChatGPT 内完成，交易需回到 Jerry 自有渠道。

### 商业模式

Jerry 从通过它购买的保单中赚取承保方佣金，与传统经纪相同，并称这不会抬高客户价格（[FAQ](https://jerry.ai/faq/)）。"在部分州的部分承保方处，客户可能需要支付一次性的经纪费或手续费"，并在购买前披露（[FAQ](https://jerry.ai/faq/)、[产品流程](https://jerry.ai/how-jerry-works/)）。车辆养护与驾驶安全免费，且不要求持有 Jerry 保单。没有公开价目表，因为消费者产品本身不收费。Propelix 未公布任何定价。

### 各时期披露的规模

| 日期 | 披露数字 | 来源 |
|---|---|---|
| 2019-01 | 手机应用上线 | [about](https://jerry.ai/about/) |
| 2020 | 当年收入增长 10 倍 | [Jerry debuts，2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-05-17 | 接近 100 万客户；45 秒内比较 45 家以上承保方 | [Jerry debuts，2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-08-10 | 100 万以上客户；估值 4.5 亿美元 | [Series C 新闻稿，2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/) |
| 2023-08-03 | 400 万美国客户 | [Insurance Journal，2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm) |
| 2024 年初 | "于 2024 年初实现盈利" | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 2024 | 客户数达到 500 万 | [about](https://jerry.ai/about/) |
| 2025 | "2025 年收入同比增长 68%，同时保持盈利" | [LinkedIn](https://www.linkedin.com/company/jerryinc) |
| 访问于 2026-07-29 | "已帮助 1,192,562 名驾驶人在 100 多家承保方之间比价" | [数据方法论页](https://jerry.ai/car-insurance-data-methodology/) |
| 访问于 2026-07-29 | iOS：美区 29,828 条评分，均分 4.68，版本 3.133.1 发布于 2026-07-21 | [iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950) |
| 访问于 2026-07-29 | Google Play：100 万以上下载，更新于 2026-07-17 | [Google Play](https://play.google.com/store/apps/details?id=com.jerrym) |
| 访问于 2026-07-29 | "超过 70% 的销售与服务入站请求（每月 5 万余次会话）"已自动化 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

### 已公布的客户与合作方

| 日期 | 对象 | 内容 |
|---|---|---|
| [2021-12-01](https://jerry.ai/newsroom/jerry-partners-with-lyft-to-save-drivers-time-and-money-on-car-expenses/) | Lyft | 向 Lyft 司机提供保险比价，首批在伊利诺伊州和宾夕法尼亚州上线 |
| [2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm) | OpenAI | 在 ChatGPT 应用内提供维修费用估算与保险报价 |
| [访问于 2026-07-29](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html) | 未具名的保险与信贷合作方 | Propelix 自述的首批客户，未公开任何名称 |

### 公司自述的规划

对方向最清晰的表述出现在招聘描述而非公告中（[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)；访问于 2026-07-29）：

- 目标写作"在未来 4 年内从 500 万客户做到 5000 万客户，成为一家 100 亿美元的公司"。
- 扩张方向是"进入相邻垂直领域（如房屋、摩托车、房车等），成为你所有实体资产的一站式入口"；YC 页面把公司定位为"打造管理你全部实体资产的 AI 智能体"。
- AI 路线图上点名的下一批赌注是"语音机器人、computer use、消费级 AI 应用"，均未被描述为已上线；此外还有把分散在六处的提示词整合到统一平台。

---

## 创始人

三位创始人共同创办过 [YourMechanic](https://jerry.ai/author/musawir-shah/)，2017 年离开该公司到 Y Combinator 孵化 Jerry（[团队页](https://jerry.ai/team/)）。

| 姓名 | 职位 | 此前经历 | 来源 |
|---|---|---|---|
| Art Agrawal | 联合创始人兼 CEO | 创办 YourMechanic（2012 年 TechCrunch Disrupt 冠军），做到覆盖 50 个州、2000 多名技师；德雷塞尔大学 | [团队页](https://jerry.ai/team/) |
| Musawir Shah | 联合创始人兼 CTO | YourMechanic 工程副总裁；NVIDIA 高级软件工程师；中佛罗里达大学计算机科学博士 | [团队页](https://jerry.ai/team/)、[作者简介](https://jerry.ai/author/musawir-shah/) |
| Lina Zhang | 联合创始人兼运营副总裁 | 一年内将 YourMechanic 从 5 个市场扩到 50 多个；Morrison & Foerster 知识产权律师；斯坦福生物化学研究员；加州律师协会会员 | [团队页](https://jerry.ai/team/) |

Musawir Shah 的[作者简介](https://jerry.ai/author/musawir-shah/)称他"领导 Jerry 的软件工程团队"，并写明他在 YourMechanic 负责面向消费者的研发、软件架构、技术栈评估与集成，以及一支工程师与 UI/UX 设计师团队。他的 [GitHub 账号](https://github.com/musawirali)标注为 Jerry, Inc. 的 CTO，地点帕洛阿尔托；他是 [getjerry 组织](https://api.github.com/orgs/getjerry/public_members)仅有的两名公开成员之一。

### 主要管理层

来自[团队页](https://jerry.ai/team/)（无日期，访问于 2026-07-29），其中职责涉及产品、工程、数据或招聘的管理者：

| 姓名 | 职位 | 此前经历 |
|---|---|---|
| John Spottiswood | 首席运营官；同时担任 Propelix 总裁 | Match、LendingClub、QuinStreet、Inflection；哈佛 MBA |
| Ed Chung | 首席财务官 | View Ridge Capital Management、Farallon Capital、Warburg Pincus；CFA |
| Josh Damico | 保险运营副总裁 | Geico（销售、服务、核保）；管理 55 家以上承保方合作关系 |
| MengHan Li | 增长副总裁 | 麦肯锡；北京大学；MIT |
| Armando La Rocca | 业务运营与分析副总裁 | Better.com、Life House；博科尼大学、达顿 MBA |
| Haley Park | 人力运营副总裁 | Windfall、Subsplash |
| Neima Shahidy | 合作伙伴副总裁 | Amazon Alexa 市场进入策略；微软 Surface |
| Journee Isip | 新业务副总裁 | LinkedIn、Meta、BCG、富国银行；哥伦比亚大学物理学、芝加哥布斯 MBA |
| Gillian Li | 财务副总裁 | 德勤、Enuma；复旦大学；CFA |

2026-07-29 在招的两个 Agentic AI 产品岗位均直接向首席运营官汇报（[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)）。除 CTO 外，公司任何自有页面都未点名其他工程负责人。

---

## 融资

| 日期 | 轮次 | 金额 | 披露的投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2018 | Series A | 公司新闻稿未披露金额 | 由 Bow Capital 领投 | — | [Jerry debuts，2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-05-17 | Series B | 2800 万美元 | 由 Goodwater Capital 领投；天使投资人包括 Jay Vijayan（Tekion）、Jon McNeill（DVx Ventures）、Brandon Krieg（Stash） | 5700 万美元 | [Jerry debuts，2021-05-17](https://jerry.ai/newsroom/jerry-debuts/) |
| 2021-08-10 | Series C | 7500 万美元，估值 4.5 亿美元 | 由 Goodwater Capital 领投；Bow Capital、Kamerra 继续参与；Highland Capital Partners 和 Park West Asset Management 为新进 | 1.32 亿美元 | [Series C 新闻稿，2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/) |
| 2023-08-03 | Series C2 | 1.1 亿美元，股权加债权 | 股权部分由 Park West Asset Management 领投，Goodwater Capital、Highland Capital Partners、Plug and Play Ventures 追加；TriplePoint Capital 领投债权额度并同时参与股权 | 2.42 亿美元 | [Carrier Management，2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm)、[Insurance Journal，2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm) |

2023 年的这轮被公司命名为 Series C2，并称其承接自"C1"轮，等于把 2021 年 8 月的 Series C 追溯改名。自 2023-08-03 起未再宣布任何轮次，自 2021 年 4.5 亿美元后也未再披露估值。

[Series C 新闻稿](https://jerry.ai/newsroom/jerry-series-c-funding/)称资金用于"更多汽车比价与购买市场"——车贷、维修、延保、停车、保养。C2 轮与 GarageGuard、DriveShield 的发布同时公布（[Insurance Journal，2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm)）。

公司的[投资人页](https://jerry.ai/investors/)列出 11 家机构，但未把任何一家对应到具体轮次：Bow Capital、FundersClub、Goodwater Capital、Kamerra、Liquid2 Ventures、Oriza Ventures、Plug and Play、SV Angel、TriplePoint Capital、Y Combinator、Zillionize。页面还列出 27 位个人投资者，其中包括 Joe Montana（Liquid2 Ventures）、Jon McNeill（DVx Ventures）、Joshua Buckley（Product Hunt）、Immad Akhund（Mercury）和 Michael Vaughn（前 Venmo）。Oriza Ventures 和 SV Angel 只出现在该页面，从未出现在任何轮次公告中。

---

## 工程

### 技术栈与平台

由公开资产确认——`jerry.ai` 的 HTTP 响应头与内容安全策略、GitHub 组织，以及发布到 npm 的包（均访问于 2026-07-29）：

| 项目 | 内容 | 证据 |
|---|---|---|
| API 网关 | Kong 3.9.3，位于 nginx 之后；每个响应都带 `x-kong-request-id` 和 `x-kong-upstream-latency` | [响应头](https://jerry.ai/) |
| 正在进行的网关工作 | 2026-06-08 创建的 `kong` 与 `kubernetes-ingress-controller` 分支 | [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| 云 | AWS——CloudFront 位于最前，S3（`us-west-2`）承载 web 应用，媒体文件放在 `jerry-uploads-prod` 桶 | [响应头](https://jerry.ai/)、[jerry.ai 的 CSP](https://jerry.ai/) |
| Serverless Next.js | `@getjerry/lambda-at-edge`、`@getjerry/next-aws-lambda`、`@getjerry/s3-static-assets`、`@getjerry/cloudfront`，以及 `terraform-next`——通过 Terraform 把 Next.js 部署到 Lambda@Edge 和 S3 | [npm registry](https://registry.npmjs.org/-/v1/search?text=getjerry)、[GitHub API](https://api.github.com/orgs/getjerry/repos) |
| 后端框架 | NestJS——`nest-casl` 是 getjerry 自研的包（301 星），为 NestJS 提供 CASL 权限控制，peer 依赖为 `@nestjs/graphql` | [nest-casl](https://github.com/getjerry/nest-casl) |
| 前端与工具链 | React；`@getjerry/eslint-config`（ESLint 9、`@typescript-eslint`、airbnb、`eslint-plugin-react`）、`@getjerry/tsconfig`、`@getjerry/prettier-config`、`@getjerry/oxfmt-config`（oxfmt ≥ 0.42），均于 2026-07-09 发布 | [npm registry](https://registry.npmjs.org/-/v1/search?text=getjerry) |
| 流式数据 | Confluent Platform Helm charts 的分支（Kubernetes 上的 Kafka） | [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| 错误追踪 | 自建 Sentry，位于 `sentry.ing.getjerry.com` | [jerry.ai 首页](https://jerry.ai/) |
| 可观测性 | Datadog 浏览器 RUM（`datadoghq-browser-agent`、`browser-intake-datadoghq.com`） | [jerry.ai 的 CSP](https://jerry.ai/) |
| 特性开关与实验 | GrowthBook，自建于 `growthbook-api.getjerry.app` | [jerry.ai 的 CSP](https://jerry.ai/) |
| 内容管理 | 产品页面内容用 Contentful（`images.ctfassets.net`）；市场站点用 WordPress 7.0.2 配 W3 Total Cache | [jerry.ai 的 CSP](https://jerry.ai/)、[jerry.ai 首页](https://jerry.ai/) |
| 第三方 API | Google Maps 与 Places API；Stripe（2022 年 fork 了其 React Native 绑定） | [jerry.ai 的 CSP](https://jerry.ai/)、[GitHub API](https://api.github.com/orgs/getjerry/repos) |
| 分析与产品工具 | Hotjar、Google Analytics / Tag Manager、Google Site Kit、Podscribe、TikTok 与 Google 广告像素 | [jerry.ai 的 CSP](https://jerry.ai/) |
| 交付流程 | GitHub Actions——getjerry 自研了 S3 缓存、Slack 构建通知、Asana 集成和发布打标的 action，因此 Asana 与 Slack 在用 | [GitHub API](https://api.github.com/orgs/getjerry/repos) |
| 状态页 | 基于 GitHub Actions 的 Upptime，域名 `status.jerry.ai`，只监控两个端点：首页和标注为 "Insurance System" 的 `jerry.ai/health` | [.upptimerc.yml](https://github.com/getjerry/upptime) |
| 数据团队工具 | "SQL (Clickhouse)、Metabase、Python、Jupyter Hub、GitHub"——在每个在招数据岗位中原文列出 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

以下来自**已关闭**的工程岗位，属于对应时期的招聘证据，不能确认当前仍在生产使用：

| 项目 | 内容 | 出处 |
|---|---|---|
| 前端 | React、React Native | 多伦多应届生岗位，[2025-11-24](https://builtintoronto.com/job/software-engineer-entry/7776678) 下架 |
| 后端 | Node.js + TypeScript、Go、Python | 同上 |
| 基础设施 | AWS、Docker、CI/CD | 同上 |
| 数据存储 | Redis、Postgres、DynamoDB、ClickHouse | 同上 |
| AI/ML | "Python 流水线、LLM 集成、内部模型" | 同上 |
| Propelix 工程 | JavaScript、React、Node.js；"不要求事先掌握" | 高级全栈工程师（多伦多），[2025-08-04](https://builtin.com/job/senior-full-stack-engineer/4456345) 下架 |

AI 平台本身在两个在招产品岗位中被点名（[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)；访问于 2026-07-29）。岗位要求候选人先搞清"我们各套技术栈（如 Propelix、Botly、CRM、GitHub、Replit）之间如何交互"。**Botly** 只出现在这些招聘描述中，未找到任何公开文档。OpenAI 在五个在招岗位中被列为合作方，[LinkedIn 简介](https://www.linkedin.com/company/jerryinc)称公司"通过 OpenAI 的 API 处理数十亿 token"。Propelix 自己的材料称支持 OpenAI、Anthropic、Google 和 Mistral 的模型（[CIO，2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)）。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 报价与比价引擎 | 用公开记录预填投保信息，在 100 多家承保方间返回最多 20 条报价，随保额与免赔额调整实时重算，最后由承保方核保确认 | [产品流程](https://jerry.ai/how-jerry-works/) |
| 保单切换与退保 | 完成购买、提交文书、取消原保单 | [产品流程](https://jerry.ai/how-jerry-works/) |
| 费率监测与重新比价触发 | 持续跟踪市场费率，在合适时机提醒客户重新比价 | [产品流程](https://jerry.ai/how-jerry-works/) |
| 基于手机的车联网 | 用手机传感器采集行程、评分、积分、每周挑战、州内排行榜，并在授权后向承保方共享 | [驾驶安全](https://jerry.ai/driver-safety/) |
| 维修报价市场 | 汇总周边修理厂的竞争性报价，通常在 24–48 小时内返回；并发布合理价格区间 | [车辆养护](https://jerry.ai/car-care/) |
| VIN 服务 | 召回查询与基于里程的保养计划 | [车辆养护](https://jerry.ai/car-care/) |
| 报价数据仓库与内容流水线 | 自有报价数据库，按 12–18 个月滚动窗口做费率分析，与 NAIC 和 BLS 交叉校验，脱敏后发布到最快每日刷新一次的内容页 | [数据方法论页](https://jerry.ai/car-insurance-data-methodology/) |
| 虚拟坐席平台（Propelix） | 多模型提示词管理、版本控制、对照生产日志测试、知识库，以及跨聊天、语音、短信、邮件的坐席部署 | [propelix.ai](https://propelix.ai)、[CIO，2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html) |
| 销售与服务自动化 | 自动处理"超过 70% 的销售与服务入站请求（每月 5 万余次会话）"；同时驱动车辆照片校验与后台自动化 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| ChatGPT 应用 | 在 ChatGPT 内呈现维修费用估算与保险报价；承保在站外完成 | [Carrier Management，2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm) |

招聘描述对 AI 平台现状的说明相当坦率：它是在"市面成品平台出现之前"自建的，"底层技术完全自研"，而提示词"如今分散在六个不同位置。没有单一事实来源，没有统一平台，也没有明确归属"（[招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)）。

### 招聘所需技术背景

截至 2026-07-29 没有在招的工程岗位，以下要求来自已关闭的工程岗位以及在招的技术类产品与数据岗位。

- **软件工程，入门级（多伦多，2025-11-24 关闭）：** 计算机或工程学士学位；实习、co-op 或个人项目经历优先但非必需；新工程师被分入覆盖核心应用、留存或自动化的"engineering pods"。
- **软件工程，高级（Propelix，多伦多，2025-08-04 关闭）：** 5 年以上经验；掌握多门语言；能胜任面向客户的沟通，因为该岗位包含把保险客户接入平台；有快速交付的记录；有高增长创业公司经历优先。
- **技术产品经理，AI（在招）：** 4 年以上"在快节奏创业公司担任前置部署工程、技术产品经理或类似技术角色"的经验；有在延迟、成本与准确率之间权衡的提示词策略、评测框架与护栏设计经验；能参与 API 设计与系统架构讨论；会 SQL。
- **数据科学与业务分析（在招）：** 6 年以上"咨询公司、投资银行或高增长科技公司"经验。招聘描述称这支 14 人的团队由"前麦肯锡、BCG 和贝恩顾问"组成，工作被描述为嵌入式分析——定义指标、做实验、推动决策——而非建模或数据工程。

### 行业领域

- **财产与意外险分销。** 公司在全部 50 个州持有经纪牌照；佣金、经纪费/手续费、承保方偏好与核保确认共同塑造了产品形态（[保险牌照页](https://jerry.ai/insurance-licenses/)、[FAQ](https://jerry.ai/faq/)）。
- **消费者数据监管。** [隐私政策](https://jerry.ai/privacy-policy/)涵盖社会安全号、驾照、信用分、理赔历史、VIN 以及"实时驾驶与地理位置信息"，并针对部分州居民说明了"用于产生法律或类似重大影响之决策的画像行为"。
- **受监管行业中的 AI。** Propelix 明确面向"受监管企业"，而 Jerry 自己的智能体运行在保险销售与服务场景中（[propelix.ai](https://propelix.ai)）。
- 保险行业知识是保险运营岗位的**硬性要求**，在工程、数据和 AI 产品岗位中**均未**被列为要求。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 在招岗位 | 截至 2026-07-29 共 47 个：保险 15、数据 13、市场 10、产品 7、商务拓展 2。没有工程部门 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 招聘系统 | Ashby，地址为 `jobs.ashbyhq.com/Jerry.ai`；`jerry.ai/job-openings` 由其渲染 | [岗位列表页](https://jerry.ai/job-openings/) |
| 地点与办公政策 | 招聘描述写"完全远程，在帕洛阿尔托、纽约、芝加哥和多伦多设有办公室"；每个非远程岗位还列出芝加哥、波士顿和旧金山湾区作为可选地点。多伦多的工程岗位曾标注为坐班 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)、[Built In Toronto](https://builtintoronto.com/job/software-engineer-entry/7776678) |
| 雇佣地域限制 | 受薪员工仅限 AZ、CA、CO、FL、GA、IL、MA、NC、NJ、NV、NY、OR、TN、TX、UT、VA 及加拿大安大略省；时薪员工仅限 AZ、FL、GA、NV、NY、NC、TN、TX、UT、VA | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 公开薪资——数据 | Associate 8.5 万–13 万美元；Data Scientist 13 万–15 万；Senior 15 万–17 万；Staff 与 Senior Manager 17 万–21 万；Manager 15 万–17 万；增长产品经理 11 万–15 万 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 公开薪资——产品（AI） | 技术产品经理 13 万–17 万美元；高级技术产品经理、高级产品经理、Product Owner 与 Senior Manager 16 万–21 万 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 公开薪资——其他 | 市场 7.5 万–19 万美元；商务拓展总监 18 万–22 万；保险销售与服务时薪 19–21 美元 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 股权 | 每个岗位都把股权列为薪酬组成部分；levels.fyi 显示为 4 年、每年 25% 的标准归属节奏 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)、[levels.fyi](https://www.levels.fyi/companies/jerry/salaries) |
| 第三方报告的工程薪酬 | levels.fyi 报告软件工程师总包中位数 15 万美元，全岗位中位数 130,773 美元；更新于 2026-07-28 | [levels.fyi](https://www.levels.fyi/companies/jerry/salaries) |
| 福利 | 医疗、牙科、视力保险；带薪休假；带薪育儿假；401(k) 含公司匹配；健康福利。兼职、合同工和自由职业岗位可能不适用 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 应届生 | 工程岗位在招时明确接受应届生——多伦多岗位不要求任何既往经验。当前没有面向应届生的在招岗位 | [Built In Toronto](https://builtintoronto.com/job/software-engineer-entry/7776678) |
| 公司自述价值观 | "Truth Seeking"、"Sense of Urgency"、"Pursuit of Excellence"；"对自己所做的事拥有完全的主导权" | [招聘页](https://jerry.ai/careers/) |
| 公司自述工作方式 | "不做 PPT"、"没有企业套话"、"没有冗余、没有无意义会议、不用等审批"；"扁平的组织架构"；职级描述为可浮动——"同一岗位你可能看到不同职级的招聘广告" | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 投递处理 | "由于收到的申请量很大，我们只会联系进入考虑范围的申请人"；无障碍支持联系 recruiting@jerry.ai | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |
| 签证支持、流失率、面试流程 | 未公开 | [招聘 API](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai) |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-29）：`jerry.ai` 及其[站点地图索引](https://jerry.ai/sitemap_index.xml)中的全部页面——51 个页面加上新闻、页面和文章三个子站点地图；`robots.txt`；直接探测 `/security`、`/trust`、`/soc2`、`/engineering`、`/blog`、`/tech`、`/data-security`、`/compliance` 路径，以及 `eng`、`engineering`、`blog`、`tech`、`api`、`docs`、`developers` 子域名；Ashby 招聘 API 与全部 47 条岗位记录；通过 REST API 访问的 `getjerry` GitHub 组织、全部 32 个仓库、公开成员列表和 upptime 配置；`@getjerry` 命名空间下发布的 npm 包；App Store 与 Google Play 页面；`propelix.ai` 及其条款页；YC、Built In、LinkedIn、levels.fyi 和维基百科的资料页；公司新闻室及其在 PR Newswire 上的分发；以及围绕 Jerry 融资、诉讼、工程招聘、Propelix 和 Botly 的英文检索。

- **没有任何工程博客、技术写作或架构材料。** 唯一带技术内容的作者页是 CTO 的个人简介；所有 `/blog`、`/engineering`、`/tech` 路径与子域名都没有内容。
- **没有安全页面、信任中心、子处理方清单或具名认证。** 站点任何位置都未声明 SOC 2、ISO 27001 或同类认证。面向消费者的说法只有"银行级加密"和 DataLock™ 保证，而后者是关于营销联系的承诺，不是安全控制（[产品流程](https://jerry.ai/how-jerry-works/)、[FAQ](https://jerry.ai/faq/)）。
- **没有公开 API 或开发者文档。** `api.jerry.ai`、`docs.jerry.ai`、`developers.jerry.ai` 均无法解析。
- **没有任何工程岗位在招**，此前被搜索引擎收录的 Ashby 工程岗位如今在岗位接口中返回空。这是招聘暂停、冻结还是时间差，从公开来源无法判断。
- **公司不公布员工人数。** 三个第三方数字互不一致，见下。
- **未取得任何工商登记记录。** 加州州务卿企业检索和 OpenCorporates 在 2026-07-29 均阻断了自动访问，因此 "Jerry Services, Inc." 与 "Jerry Insurance Agency, LLC" 未经登记机关核实；实体名称及其母子关系均来自公司自有的法律页面。
- **自 2021 年 8 月起没有新的估值**，自 2023 年 8 月起没有新的融资轮次。盈利、70 倍收入以及 2025 年 68% 增长这三项均为公司在招聘文案和 LinkedIn 上的自述，未找到任何备案、审计或投资方确认。
- **种子轮与 Series A 未说明具体投资方对应哪一轮**；[投资人页](https://jerry.ai/investors/)只是一份无归属的名单，其中 Oriza Ventures 和 SV Angel 未在任何其他地方出现。
- **Propelix 未公布定价、具名客户、文档或技术细节**，只有一个落地页和一个条款页；它没有 about 页、robots.txt 或站点地图。
- **未发现涉及 Jerry 的诉讼。** 在检索保险经纪相关诉讼时出现的 2026 年 TCPA 集体诉讼，被告是 [InsureMe, Inc.](https://natlawreview.com/article/painful-premium-insurance-brokerage-firm-hit-class-action-lawsuit-alleging)，不是 Jerry。
- **未找到 CTO 的任何访谈或会议演讲。** 公司在技术上的公开发声者是首席运营官，他在 2023 年 Generative AI World 上介绍了客服 AI 的成果（[GAI Insights](https://gaiinsights.com/blog/jerry-case-study-for-customer-service-saving-over-4m-a-year)）。

### 不同来源之间的不一致

- **员工人数：** 225（[YC 页面](https://www.ycombinator.com/companies/jerry-inc)）、296（[Built In](https://builtin.com/company/jerry)）、201–500 区间且有 402 份档案（[LinkedIn](https://www.linkedin.com/company/jerryinc)）、2021 年为 186（[维基百科](https://en.wikipedia.org/wiki/Jerry_%28company%29)）。全部要么无日期，要么为自报。
- **办公地点：** 招聘描述写帕洛阿尔托、纽约、芝加哥、多伦多；[LinkedIn](https://www.linkedin.com/company/jerryinc) 写硅谷加多伦多和布法罗，另有分布在四个国家的远程员工；[Built In](https://builtin.com/company/jerry) 写帕洛阿尔托、布法罗、多伦多和伊利诺伊州 Lockport；[维基百科](https://en.wikipedia.org/wiki/Jerry_%28company%29) 写纽约州 Lockport。没有任何两个来源一致。
- **远程政策：** 2026 年的招聘描述写"完全远程"；2025 年的多伦多工程岗位标注为坐班（[Built In Toronto](https://builtintoronto.com/job/software-engineer-entry/7776678)）。
- **承保方数量：** [官网](https://jerry.ai/how-jerry-works/)写"100 多家"；[App Store 描述](https://itunes.apple.com/lookup?id=1258315950)写"最多 50 家"；[Built In](https://builtin.com/company/jerry) 写"55 家以上"；[2021 年新闻稿](https://jerry.ai/newsroom/jerry-debuts/)写"45 家以上"。
- **收入增长：** 2026 年 7 月的招聘描述写"收入增长 70 倍"；2025 年 11 月的多伦多岗位写"5 年内收入增长 60 倍"；[LinkedIn](https://www.linkedin.com/company/jerryinc) 写"2025 年收入同比增长 68%"。三者的基准和期间都不相同。
- **客户节省金额：** [2021 年新闻稿](https://jerry.ai/newsroom/jerry-series-c-funding/)写"每年 800 美元"；2025 年多伦多岗位写"每年超过 1000 美元"；现行[产品流程页](https://jerry.ai/how-jerry-works/)写"平均每年 3,979 美元"，并限定为过去 12 个月内找到节省空间且记录良好的客户。
- **自动化率：** "93% 至 94% 的入站对话由虚拟坐席回复"且无需转人工（[CIO，2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)）；2026 年招聘描述写"超过 70% 的销售与服务入站请求（每月 5 万余次会话）"。两者口径不同——对话与请求，每月 5 万次会话与 [2023 年](https://gaiinsights.com/blog/jerry-case-study-for-customer-service-saving-over-4m-a-year)引用的每月 20 万条以上消息——因此无法直接比较，也不能简单认定其中之一取代另一个。
- **App Store 评分：** [评价页](https://jerry.ai/reviews/)写 4.7 分、"1.64 万条以上评价"；[iTunes API](https://itunes.apple.com/lookup?id=1258315950) 返回美区 29,828 条评分、均分 4.68；[首页](https://jerry.ai/)写"400 万次以上下载"。评分、评价和下载是三种不同口径，页面并未加以区分。
- **轮次命名：** 2021 年 8 月那一轮公布时叫 [Series C](https://jerry.ai/newsroom/jerry-series-c-funding/)，在 [2023 年 C2 的报道](https://www.carriermanagement.com/features/2023/08/03/251512.htm)中被称为 "C1"。

### 其他

- **内部 AI 平台变成了产品。** Propelix 作为 Jerry Services, Inc. 的产品对外销售，由 Jerry 的首席运营官担任总裁，而 Jerry 自身的消费者业务仍是保险经纪。加入 AI 方向的工程师可能落在其中任何一侧。
- **Series C2 从未发布在 Jerry 自己的新闻室。** [新闻室站点地图](https://jerry.ai/newsroom-sitemap.xml)中没有任何 2023 年的融资稿件；该轮次只能通过行业媒体获得记录。
- **招聘重心完全偏离工程。** 47 个在招岗位中，15 个是时薪 19–21 美元的保险销售与服务岗，13 个是要求咨询或投行背景的分析岗，10 个是 SEO/AEO 内容与社区营销岗。公开薪资区间把分析与 AI 产品岗（16 万–21 万美元）放在了 levels.fyi 软件工程师中位数（15 万美元）之上。
- **AI 产品岗位对技术债的描述异常坦率**——六处提示词、没有单一事实来源、没有统一平台、没有明确归属——这比公司在其他任何地方公开的架构细节都多。
- **公开的 web 表面主要是 SEO 机器。** 站点地图索引下分设车险、维修、评价和本地等多个子地图，并配有一份公开的[内容方法论](https://jerry.ai/car-insurance-data-methodology/)，从报价数据库出发最快每日刷新页面；在招市场岗位中有 10 个是 SEO、AEO、社区和自然增长方向。
- **状态页只监控两个 URL。** `status.jerry.ai` 只检查首页和一个标注为 "Insurance System" 的 `/health` 端点（[.upptimerc.yml](https://github.com/getjerry/upptime)）——它不是服务级别的状态页。
- **GitHub 组织中大部分是 fork。** 32 个公开仓库里约三分之二是上游项目的分支；实质性的原创工作是 `nest-casl` 和一组内部 GitHub Actions。2026-07-09 重新发布的 npm 配置包，是前端工具链最新的公开信号。
- **公司同时运行两个品牌域名。** `getjerry.com` 仍留在 CSP 中并承载内部服务（Sentry、GrowthBook），CTO 在 Google Play 上的开发者联系邮箱也是 `getjerry.com` 地址（[Google Play](https://play.google.com/store/apps/details?id=com.jerrym)）。

---

## 资料来源

**官方**

- [Jerry —— jerry.ai](https://jerry.ai/)
- [关于](https://jerry.ai/about/) · [团队](https://jerry.ai/team/) · [投资人](https://jerry.ai/investors/) · [FAQ](https://jerry.ai/faq/)
- [产品流程](https://jerry.ai/how-jerry-works/) · [车辆养护](https://jerry.ai/car-care/) · [驾驶安全](https://jerry.ai/driver-safety/) · [用户评价](https://jerry.ai/reviews/)
- 险种：[车险](https://jerry.ai/car-insurance/) · [房屋险](https://jerry.ai/home-insurance/) · [租客险](https://jerry.ai/renters-insurance/) · [摩托车险](https://jerry.ai/motorcycle-insurance/)
- [车险数据方法论](https://jerry.ai/car-insurance-data-methodology/)
- [招聘](https://jerry.ai/careers/) · [岗位列表](https://jerry.ai/job-openings/) · [Ashby 招聘 API——页面渲染所用的 47 条岗位记录](https://api.ashbyhq.com/posting-api/job-board/Jerry.ai)
- [保险牌照](https://jerry.ai/insurance-licenses/) · [使用条款](https://jerry.ai/terms-of-use/) · [隐私政策](https://jerry.ai/privacy-policy/)
- [新闻室](https://jerry.ai/news/) · [新闻室站点地图](https://jerry.ai/newsroom-sitemap.xml) · [站点地图索引](https://jerry.ai/sitemap_index.xml)
- [Musawir Shah——作者简介](https://jerry.ai/author/musawir-shah/)
- [Propelix](https://propelix.ai) · [Propelix 使用条款](https://propelix.ai/terms)
- [状态页配置——getjerry/upptime](https://github.com/getjerry/upptime)
- [GitHub 组织——getjerry](https://github.com/getjerry) · [组织 API](https://api.github.com/orgs/getjerry) · [仓库 API](https://api.github.com/orgs/getjerry/repos) · [公开成员 API](https://api.github.com/orgs/getjerry/public_members)
- [nest-casl](https://github.com/getjerry/nest-casl) · [getjerry 发布的 npm 包](https://registry.npmjs.org/-/v1/search?text=getjerry)
- [Musawir Shah —— GitHub](https://github.com/musawirali)
- [LinkedIn](https://www.linkedin.com/company/jerryinc)
- [App Store 元数据——iTunes lookup API](https://itunes.apple.com/lookup?id=1258315950) · [Google Play](https://play.google.com/store/apps/details?id=com.jerrym)

**新闻稿**

- [Jerry 2026 年美国驾驶人现状报告 —— 2026-07-01](https://jerry.ai/studies/2026-state-of-the-american-driver-report/)
- [Jerry 与 Lyft 达成合作 —— 2021-12-01](https://jerry.ai/newsroom/jerry-partners-with-lyft-to-save-drivers-time-and-money-on-car-expenses/)
- [基于 AI 的汽车持有超级应用 Jerry 完成 7500 万美元 Series C，估值 4.5 亿美元 —— 2021-08-10](https://jerry.ai/newsroom/jerry-series-c-funding/)
- [Jerry 亮相，累计融资 5700 万美元 —— 2021-05-17](https://jerry.ai/newsroom/jerry-debuts/)

**第三方报道与资料页**

- [Carrier Management —— Jerry 把 AI 驱动的保险带进 ChatGPT，2026-03-12](https://www.carriermanagement.com/news/2026/03/12/285603.htm)
- [CIO —— Propelix 让企业轻松搭建自己的生成式 AI 聊天机器人，2024-04-16](https://www.cio.com/video/2091544/propelix-lets-companies-easily-build-their-own-generative-ai-chatbots.html)
- [Carrier Management —— 车险省钱应用 Jerry 宣布 1.1 亿美元 C2 轮，2023-08-03](https://www.carriermanagement.com/features/2023/08/03/251512.htm)
- [Insurance Journal —— 加州汽车应用 Jerry 获 1.1 亿美元融资并扩展服务，2023-08-03](https://www.insurancejournal.com/news/west/2023/08/03/733720.htm)
- [GAI Insights —— 客服案例研究，Generative AI World 2023](https://gaiinsights.com/blog/jerry-case-study-for-customer-service-saving-over-4m-a-year)
- [TechCrunch —— Jerry 以 4.5 亿美元估值融资 7500 万美元，2021-08-10](https://techcrunch.com/2021/08/10/jerry-raises-75m-at-a-450m-valuation/)
- [Y Combinator 公司资料页](https://www.ycombinator.com/companies/jerry-inc)
- [Built In —— 公司资料页](https://builtin.com/company/jerry) · [Built In Toronto —— Software Engineer (entry)，2025-11-24 下架](https://builtintoronto.com/job/software-engineer-entry/7776678) · [Built In —— Senior Full Stack Engineer（Propelix），2025-08-04 下架](https://builtin.com/job/senior-full-stack-engineer/4456345)
- [levels.fyi —— Jerry 薪酬](https://www.levels.fyi/companies/jerry/salaries)
- [维基百科 —— Jerry (company)](https://en.wikipedia.org/wiki/Jerry_%28company%29)
- [Forbes —— 美国最佳创业雇主榜](https://www.forbes.com/lists/americas-best-startup-employers/)
- [National Law Review —— 被告为 InsureMe, Inc. 的 TCPA 集体诉讼，列出以避免误认](https://natlawreview.com/article/painful-premium-insurance-brokerage-firm-hit-class-action-lawsuit-alleging)
