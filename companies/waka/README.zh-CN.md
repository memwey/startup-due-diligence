# Waka

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

Waka（[hellowaka.com](https://www.hellowaka.com/)）将自己描述为“面向在新兴市场转移价值的运营商、从非洲—亚洲走廊起步的稳定币贸易结算基础设施”。产品提供非洲本地收款、持有法币和 USDT 余额的资金管理层，以及通过 Alipay、WeChat Pay、FPS、FAST、SWIFT 和 USDT 等非洲、亚洲及全球渠道付款。[2026-04-20 Frontier Fintech 合作文章](https://frontierfintech.substack.com/p/117-payments-follow-trade)由 CEO 共同撰写，副标题为“A Partner Piece with Waka formerly Pyxis”；同一团队自 2023 年起以 Pyxis 名义运营。

- 公开进展：“八个非洲市场年流量超过 1 亿美元”，“100 多家流动性提供商连接 20 种货币”（[Frontier Fintech，2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)；这是 CEO 共同撰写的合作文章，并非独立报道）。
- 团队：“约二十人”，成员位于“非洲、中国、新加坡和澳大利亚”，来自 [2026-07-28](https://www.v2ex.com/t/1230518)招聘帖；Pyxis 名义下截至 [2025-09-19](https://share.transistor.fm/s/27884a18)为四国 12 人。[LinkedIn](https://www.linkedin.com/company/hellowaka/)标为 11–50 人（无日期，访问于 2026-07-29）。
- Waka 名义下没有公布融资轮次。Pyxis 参加了 [Orbit Startups 2023](https://orbitventures.com/company/pyxis/) 种子期项目。
- 招聘信息列出 Java／Spring Boot、Go、Node.js、Vue 和 React，但不能证明生产后端实际采用哪一种。两个职位均为全球远程，协作时区 UTC+3／UTC+8，未公开薪资；招聘帖于 [2026-07-28](https://www.v2ex.com/t/1230518)以 **Pyxis** 名义发布，网站填写 hellowaka.com。另据公开提供的客户 Portal bundle，可确认前端使用 Vue 3，API 请求发往 `https://api.pyxis.money`（访问于 2026-07-29，见[工程](#工程)）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 品牌与网站 | Waka — [hellowaka.com](https://www.hellowaka.com/) | 网站 |
| 域名创建 | 2025-12-11（注册商 Cloudflare） | WHOIS；访问于 2026-07-29 |
| 法律文件中的实体 | “Waka”，注册地址 3A Lionel Street, Doncaster East, VIC 3109, Australia | [General Terms V1.2，2026-03-12](https://portal.hellowaka.com/static/GeneralTerms.html) |
| 适用法律 | 澳大利亚新南威尔士州 | [General Terms V1.2](https://portal.hellowaka.com/static/GeneralTerms.html) |
| 自述监管状态 | “Waka 通过在加拿大 FINTRAC 和澳大利亚 AUSTRAC 登记的实体提供服务。” | [网站页脚](https://www.hellowaka.com/)；无日期，访问于 2026-07-29 |
| 联系方式 | customerservice@hellowaka.com | [Terms](https://portal.hellowaka.com/static/GeneralTerms.html)、[Privacy Policy](https://portal.hellowaka.com/static/PrivacyPolicy.html) |
| 员工人数 | “约二十人”（2026-07-28）；四国 12 人（2025-09-19，以 Pyxis 名义）；LinkedIn 区间 11–50（无日期，访问于 2026-07-29） | [V2EX](https://www.v2ex.com/t/1230518)、[播客](https://share.transistor.fm/s/27884a18)、[LinkedIn](https://www.linkedin.com/company/hellowaka/) |
| 团队地点 | 成员位于“非洲、中国、新加坡和澳大利亚”（2026-07-28）；“来自内罗毕、香港、新加坡和其他贸易枢纽的运营者”（2026-02） | [V2EX](https://www.v2ex.com/t/1230518)、[hellowaka.com 归档 2026-02-26](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) |
| 招聘材料所称总部 | “总部位于新加坡的金融科技公司” | [V2EX，2026-07-28](https://www.v2ex.com/t/1230518) |
| 工程团队工作语言（推断） | 未找到正式政策。工程招聘使用中文；全栈职位要求阅读英文资料并与海外团队进行基础英文沟通，Tech Lead 则要求用英语与海外团队和合作伙伴沟通。日常主要语言仍无法确认 | [Tech Lead](https://www.v2ex.com/t/1230518)、[全栈工程师](https://www.v2ex.com/t/1230527) |

### 品牌与法律实体

| 类型 | 名称 | 状态或司法辖区 | 证据与限制 |
|---|---|---|---|
| 当前公开品牌 | Waka／hellowaka.com | 正在使用 | 网站、Portal 和法律文件均使用 Waka |
| 曾用或前身品牌 | Pyxis／Pyxis Pay | 被描述为“Waka formerly Pyxis” | [Frontier Fintech，2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)能证明品牌延续，不能证明法律主体相同 |
| 当前 Terms 所称实体 | “Waka” | 澳大利亚；注册地址称在 Victoria，适用法律称为 New South Wales | [General Terms V1.2](https://portal.hellowaka.com/static/GeneralTerms.html)；未公开注册号 |
| 关联实体 | Pyxis Pay (Pte. Ltd.) | 新加坡；UEN 202306267Z，成立于 2023 年 | [Singapore FinTech Association 记录](https://membership.singaporefintech.org/company/202306267Z) |
| 关联实体 | Pyxis Pay Limited | 加拿大；2023-10-16 成立，FINTRAC 登记现显示为已过期 | [FINTRAC MSB 登记](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx)；访问于 2026-07-29 |

可观察到的延续关系是：Pyxis 自称 2022 年创立；新加坡和加拿大的 Pyxis 实体出现于 2023 年；hellowaka.com 于 2025 年 12 月注册，并在 2026 年初公开上线；到 2026 年 7 月，招聘仍使用 Pyxis 名称但指向 hellowaka.com，Waka Portal 也调用 `api.pyxis.money`。这些事实支持品牌、团队和产品基础设施具有连续性，但**不能**证明澳大利亚“Waka”、新加坡公司和加拿大公司是同一法律主体、同属一家母公司，或已经发生有文件支持的更名或资产转移。

### 登记核查

由于网站页脚点名两个监管机构，本页于 2026-07-29 检索了两个公开登记：

| 登记 | 查询 | 结果 |
|---|---|---|
| [FINTRAC Money Services Business Registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) | “waka” | 没有匹配实体 |
| [FINTRAC Money Services Business Registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) | “pyxis” | **PYXIS PAY LIMITED**，MSB 登记 M24908802，服务“Foreign Exchange, Money Transferring”，首次批准 2024-01-22，到期 2026-01-23，**状态“Expired”** |
| [AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/) | “waka” | 没有匹配实体 |
| [AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/) | “pyxis” | “No match found” |
| [ABN Lookup](https://abr.business.gov.au/) | “waka”，邮编 3109（Terms 中的地址） | 没有匹配实体 |
| [CBK Authorized Payment Service Providers，2025-11-06](https://www.centralbank.go.ke/wp-content/uploads/2025/11/Directory-of-Authorized-Payment-Service-Providers-6-November-2025.pdf) | “Pyxis”“Waka” | 两个名称均未出现 |

AUSTRAC Virtual Asset Service Provider Register 对所有尝试的查询都没有返回结果，包括作为对照的一家已知澳大利亚交易所，因此不据此作结论。

### 公司陈述的市场背景

根据 CEO April Long 共同撰写的 [Frontier Fintech 合作文章（2026-04-20）](https://frontierfintech.substack.com/p/117-payments-follow-trade)：

- 2024 年稳定币转账量达 27.6 万亿美元，B2B 转账是最大单一用途。
- 出入金成本据称从 3–4% 降至 0.5% 以下；两年前在内罗毕入金、新加坡出金的合计成本为 3–4%。
- 其观点是稳定币应作为“后端轨道，同时保持面向客户的法币体验”。

创始人自己的 Newsletter 于 [2026-05-05](https://aprilnewsletter.substack.com/p/arent-remittance-companies-already)列出：非洲侨汇 950 亿美元（2024）、中非贸易 2,955.6 亿美元（2024）、非洲商品贸易总额约 1.53 万亿美元（2024），以及 2025 年中国对非出口同比增长 25.8%。[2024 中非数字金融普惠峰会](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html)给出的上一年中非贸易额为 2,820 亿美元。

---

## 产品

公开网站将产品分成三层，另有 Portal 和 API。没有产品文档网站；以下说明来自 [hellowaka.com](https://www.hellowaka.com/)（无日期，访问于 2026-07-29）。

### 功能领域

- **Collections**——通过移动货币和银行渠道，在支持的本地市场提供“虚拟账号和实名收款流程”。
- **Treasury**——“余额、收款人、审批、外汇和稳定币流动集中在一个资金管理视图”，含 KYB、审批和导出。
- **Payouts**——通过非洲、亚洲和全球渠道向已批准收款人实名付款：Alipay、WeChat Pay、FPS、FAST、SWIFT、USDT。
- **稳定币资金和出入金**——在法币与稳定币渠道间移动（USDT 入金／出金），并有“业务控制和走廊级审批”。
- **Dashboard**——外汇报价、导出、收款人、付款状态、交易对手和可导出记录。
- **API**——“以程序方式访问虚拟账号、付款指令、汇率、交易对手和 Webhook”。未找到公开开发者文档。

所述开户流程为：KYB 与走廊审批 → 收款、持有和兑换 → 付款和对账。

### 覆盖范围

| 方向 | 市场与渠道 | 来源 |
|---|---|---|
| 非洲（收款和付款） | Kenya、Tanzania、Uganda、Ghana、Gabon、Cameroon、Chad、Congo、Nigeria、Senegal、South Africa、Equatorial Guinea、Central African Republic——“More Markets to Come” | [hellowaka.com](https://www.hellowaka.com/) |
| 中国 | SWIFT、Local Bank、Alipay、WeChat | [hellowaka.com](https://www.hellowaka.com/) |
| 香港 | SWIFT、RTGS、FPS | [hellowaka.com](https://www.hellowaka.com/) |
| 新加坡 | SWIFT、FAST | [hellowaka.com](https://www.hellowaka.com/) |
| 全球 | SWIFT | [hellowaka.com](https://www.hellowaka.com/) |

这 13 个非洲市场与 [pyxis.money](https://www.pyxis.money/)的列表相同（Kenya 列在 C2C，其余 12 个列在 B2B；无日期，访问于 2026-07-29）。

### 商业化

未找到公开价目表。[General Terms V1.2（2026-03-12）](https://portal.hellowaka.com/static/GeneralTerms.html)称“服务费根据客户使用的服务分别收取，或按双方书面约定”，并提及网站上的 fee schedule；2026-07-29 访问网站时未见该表。Terms 将服务描述为收款、付款、外汇、在线支付受理和技术服务。

[Frontier Fintech（2026-04-20）](https://frontierfintech.substack.com/p/117-payments-follow-trade)将其描述为一体化服务：从本地客户经理和客户开户，经外汇流动性管理、做市和稳定币结算，到合规人民币结算进入中国大陆，并提供让每笔付款符合 SAFE 和 PBOC 框架的文件。文章还称客户组合分为“高交易量稳定锚、核心利润层和高利差 alpha 仓位”三层。

### 历年公开规模与主张

| 日期 | 公开数字或主张 | 来源 |
|---|---|---|
| 2024-08-22 | 肯尼亚贸易商将能通过 WeChat 支付最高 70,000 美元；称 Alipay 集成正在进行 | [Business Daily](https://www.businessdailyafrica.com/bd/corporate/technology/kenyan-traders-to-pay-for-chinese-goods-via-alipay-4735424) |
| 2024-08-27 | 正在敲定通过 WeChat Pay 进行最高 70,000 美元交易的协议 | [China Daily](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html) |
| 2024-08-29 | 被描述为“目前处于试点阶段” | [NTU-SBF Centre for African Studies](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform) |
| 2025-09-19 | 四国 12 人；称已有收入；转向大宗贸易商前，90% 精力曾用于小商户 | [African Tech Roundup 播客](https://share.transistor.fm/s/27884a18) |
| 2026-02-26（网站归档） | “典型结算 24 小时”“外汇成本降低 70%”“集成 2–4 周”“比传统路径最多便宜 70%”“首个可直接交付人民币的稳定币贸易结算网络” | [Wayback](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/) |
| 2026-04-20 | “八个非洲市场年流量超过 1 亿美元，以适度营运资金产生可观 ARR”；“100 多家流动性提供商连接 20 种货币” | [Frontier Fintech](https://frontierfintech.substack.com/p/117-payments-follow-trade) |
| 2026-07-28 | “约二十人”，位于非洲、中国、新加坡和澳大利亚；“处于快速建设产品和核心系统阶段，不是在成熟系统上纯维护”，“从 0 到 1 建支付产品、商户系统、API 服务和内部运营工具” | [V2EX](https://www.v2ex.com/t/1230518) |
| 访问于 2026-07-29 | 列出 13 个非洲市场；无头部指标、“第一”主张、结算时间或成本降低数字 | [hellowaka.com](https://www.hellowaka.com/) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 详情 | 来源 |
|---|---|---|---|
| 2024-08-22 | Alipay、WeChat Pay | 以 Pyxis 名义宣布为肯尼亚—中国支付集成伙伴 | [Business Daily](https://www.businessdailyafrica.com/bd/corporate/technology/kenyan-traders-to-pay-for-chinese-goods-via-alipay-4735424) |
| 无日期（网站） | WeChat Pay、UnionPay、M-PESA、Tencent、Alipay | Pyxis 网站和投资者页面列为合作；Pyxis 新闻区复述了 WeChat Pay 和 Alipay 发布的媒体标题 | [pyxis.money](https://www.pyxis.money/)、[Orbit Ventures](https://orbitventures.com/company/pyxis/) |
| 2026-04-20 | — | “公司已开始服务在全非洲拥有 B2B 分销网络的大型中国企业” | [Frontier Fintech](https://frontierfintech.substack.com/p/117-payments-follow-trade) |

没有公布具名的 Waka 客户。[Frontier Fintech](https://frontierfintech.substack.com/p/117-payments-follow-trade)称 Waka 的流动性提供商包括“由 Visa Ventures、Coinbase Ventures 和 Tether 支持的合作伙伴”——这是合作伙伴的投资方，不是 Waka 的投资者。

### 公开计划

根据 [Frontier Fintech（2026-04-20）](https://frontierfintech.substack.com/p/117-payments-follow-trade)，商业路线有两个方向：（1）“深化走廊两端的企业关系”，与非洲和中国大型企业合作；（2）“扩展支付公司渠道”：服务已经处理贸易相关资金流、需要合规且流动性充足的中国通道的非洲金融科技公司和跨境平台。

---

## 创始人

**April Long**——Waka CEO 和共同创始人（[Frontier Fintech，2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)）；此前为 Pyxis 共同创始人兼 CEO（[Orbit Ventures](https://orbitventures.com/company/pyxis/)、[NTU-SBF CAS，2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)）。

- 23 岁时在坦桑尼亚参与接待习近平主席；[2025-09-19 播客](https://share.transistor.fm/s/27884a18)称录制时年龄 35 岁。
- 2015 年在 Standard Chartered 工作，为中国贸易公司客户提供贷款服务（[播客，2025-09-19](https://share.transistor.fm/s/27884a18)）。
- 曾任 Standard Chartered Bank Kenya 中国业务经理；被描述为中文流利，并熟悉肯尼亚和中国金融系统（[NTU-SBF CAS，2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)）。
- 也曾任职 Gulf African Bank；被称拥有“10 年以上非洲—亚洲走廊金融服务经验”，并在 Standard Chartered Kenya 和 Gulf African Bank 内部管理中非走廊十年后创立 Waka（[Frontier Fintech，2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)）。
- 共同创立 Pyxis；[Pyxis About](https://www.pyxis.money/about)称成立于 2022 年，而新加坡和加拿大企业记录为 2023 年，见[备注](#备注)。
- 截至 [2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)居住于内罗毕；[LinkedIn](https://www.linkedin.com/in/longapril/)地点为新加坡（来自 2026-07-29 搜索结果；页面本身对自动访问返回 HTTP 999）。
- 在 2024 中非数字金融普惠峰会演讲（[China Daily，2024-08-27](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html)）。
- 在 Substack 撰写 [April's Newsletter](https://aprilnewsletter.substack.com/)，首篇为 [2025-09-05](https://aprilnewsletter.substack.com/p/welcome-to-aprils-newsletter)。[About](https://aprilnewsletter.substack.com/about)写道：“我为新兴市场构建跨境支付基础设施。”所查文章未点名 Waka。
- 长篇访谈：[African Tech Roundup，2025-09-19](https://share.transistor.fm/s/27884a18)，涉及从服务中小企业转向大宗贸易商和聚合商。

**George Chan**——新加坡人；Pyxis 共同创始人，[Orbit Ventures](https://orbitventures.com/company/pyxis/)列为 COO。曾任 CrimsonLogic，后任贸易科技公司 GUUD 非洲区总经理；被描述为中文流利、居住于内罗毕（[NTU-SBF CAS，2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)）。未公开其在 Waka 的职位。

**其他已确认人员**

| 姓名 | 职位 | 公开背景 | 来源 |
|---|---|---|---|
| Michael Ogongo | Waka Head of Partnerships | 曾任 Antler East Africa；Cornell University；位于纽约 | [LinkedIn](https://www.linkedin.com/in/michael-ogongo-2a666612a/) |

hellowaka.com 没有团队、管理层或 About 页面。[2026 年 2 月归档网站](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/)只笼统描述团队：“来自内罗毕、香港、新加坡和其他贸易枢纽、在新兴市场支付、外汇和合规领域工作多年的运营者。”

---

## 融资（Pyxis 前身）

| 日期 | 轮次 | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2023（项目批次） | Seed | 未披露 | Orbit Startups 2023（Pyxis） | — | [Orbit Ventures](https://orbitventures.com/company/pyxis/) |

已找到的融资证据均属于 Pyxis 前身，不能证明当前哪个 Waka 关联法律实体（如有）实际接受了投资。截至 2026-07-29，Waka 名义下没有公布融资轮次。

**未经确认的数据库线索：** 搜索结果摘要把 2023-09-18 的种子轮归于 SOSV。[Crunchbase Pyxis 页面](https://www.crunchbase.com/organization/pyxis-8b86)于 2026-07-29 访问时返回 HTTP 403，也未找到确认该日期或投资者的一手公告。Orbit Startups 与 SOSV 有关联，这与该说法相符，但不能构成确认。

[Orbit Ventures portfolio 页面](https://orbitventures.com/company/pyxis/)将公司标记为 Digitization、Women Founders、Kenya、Seed、Fintech 和“Orbit Startups 2023”；列 April Long 为 CEO、George Chan 为 COO；称 Pyxis 已与 WeChat Pay、UnionPay 和 M-PESA 等大型金融科技公司合作并处理数百万交易，面向“5000 亿美元且每年增长 10%”的市场，但未说明轮次日期或金额。

[2025-09-19 播客](https://share.transistor.fm/s/27884a18)中，CEO 将公司描述为相对于竞争者几乎没有外部资金——“没有数百万美元可烧在市场教育上”“我庆幸没有钱可烧”；[2026-04-20 合作文章](https://frontierfintech.substack.com/p/117-payments-follow-trade)称收入是在“适度营运资金”下产生。

---

## 工程

### 技术栈与平台

Pyxis／Waka 的名称证据已集中整理在[品牌与法律实体](#品牌与法律实体)。以下两个技术来源在重叠之处说法一致。

**招聘信息提及，不能确认是生产技术栈。** 用户 `Charles678` 于 2026-07-28 以 **Pyxis** 公司名在 V2EX 发布两个职位，网站为 `hellowaka.com`、申请邮箱为 `ncrew@pyxis.money`：[Tech Lead](https://www.v2ex.com/t/1230518)和[全栈工程师](https://www.v2ex.com/t/1230527)。

| 职位 | 点名的具体技术 | 证据状态 |
|---|---|---|
| 全栈工程师 | 优先 Java／Spring Boot，也欢迎 Go 和 Node.js；要求 Vue、React 或其他主流前端框架、REST API 和数据库；优先 Docker、云服务、CI/CD 和 Python | 仅为招聘要求 |
| Tech Lead | 要求 Java／Spring Boot、Go、Node.js 中至少一种，以及数据库、缓存、消息队列和 API；优先云服务和 CI/CD | 仅为招聘要求；帖子明确称具体技术选型仍在演进 |

高可用、生产稳定性、可观测性、安全、支付与结算系统、外部集成、Web3 和从 0 到 1 平台建设等经历归入[招聘所需技术背景](#招聘所需技术背景)，不作为当前技术栈的证据。

**根据公开前端资产和 HTTP header 推断**；访问于 2026-07-29：

| 层 | 观察 |
|---|---|
| 营销网站 | 由 [Framer](https://www.framer.com)构建和托管；hellowaka.com 的 `robots.txt`、`sitemap.xml` 指向 `blissful-shortbread-214183.framer.app` |
| 客户 Portal | `portal.hellowaka.com`：Vite 单页应用（`/assets/index-<hash>.js`，ES module 入口），Vue 3、`vue-router`、Pinia、Ant Design Vue（bundle 中有 `AButton`、`AForm`、`ATable` 等）、axios，Google Fonts 的 Inter |
| Web server | portal.hellowaka.com 返回 `server: openresty` |
| API 后端 | Portal axios interceptor 设置 `baseURL:"https://api.pyxis.money"`、`withCredentials:true`、120 秒 timeout。bundle 中可见 `/api/client/v1/user/login/email`、`/api/client/v1/user/register/kyc/email`、`/api/client/v1/user/password/reset/by-code`、`/api/form-config/get-form-config` |
| 反机器人 | GeeTest CAPTCHA v4；[Privacy Policy](https://portal.hellowaka.com/static/PrivacyPolicy.html)称其为 AI 风险引擎收集数据 |
| 分析 | “Google stats or similar provider via cookies”（[Privacy Policy](https://portal.hellowaka.com/static/PrivacyPolicy.html)） |
| 其他 | Portal HTML 加载 `https://mcp.figma.com/mcp/html-to-design/capture.js`，HTML 注释使用简体中文 |

### 系统

[Tech Lead 职位](https://www.v2ex.com/t/1230518)直接列出核心模块：“商户、订单、支付、结算、对账和 Partner API”。[工程职位](https://www.v2ex.com/t/1230527)采用相同拆分：

| 领域 | 招聘信息所述范围 |
|---|---|
| 后端与 API | 订单、支付、结算、对账、商户管理；业务接口、数据模型、权限控制、核心逻辑；事务一致性、异常重试、日志追踪、性能优化；对接第三方 Partner、支付渠道和外部系统；API 接入、签名认证、异常处理 |
| 前端与内部工具 | Merchant Portal 和内部运营后台；把复杂支付、结算、对账和风控流程变成清晰可用界面；与运营、合规和销售把重复工作工具化；“AI Bot 和业务自动化工具” |
| 工程质量 | 生产排障、日志分析、稳定性；代码质量、工程规范、可测试性；用 AI 工具编码、调试、测试、重构和写文档 |

Tech Lead 还负责“支付平台技术架构、系统边界和演进路线”，建立“测试、发布、监控、日志和安全标准”，并在“交付速度、系统质量和长期成本”之间管理技术债。

Portal 客户端路由反映了运营侧同一业务面，以下为 2026-07-29 从生产 bundle 读取的每屏路由：

| 路由 | 可能覆盖的内容 |
|---|---|
| `/register`、`/login`、`/security` | 邮箱注册登录、邮件验证码重置密码、账户安全 |
| `/kyb/verification`、`/verification/business` | KYB 开户和文件提交 |
| `/virtual-accounts` | 签发收款虚拟账号 |
| `/pay-ins`、`/pay-outs`、`/orders` | 收付款指令和订单历史 |
| `/balances/`、`/balances/deposit`、`/balances/exchange`、`/balances/withdraw` | 多币种余额、充值、外汇兑换、提现 |
| `/batch-uploads`、`/batch-uploads/:batchNo`、`/batch-uploads/new` | 批量付款文件上传和批次详情 |
| `/dev-management` | 开发者／API 凭证管理 |
| `/permissions` | 客户账号内用户角色 |
| `/dashboard/`、`/homepage` | 首页和概览 |

未找到公开 API reference、OpenAPI／AsyncAPI、SDK、sandbox、changelog 或状态页。`docs.hellowaka.com`、`api.hellowaka.com`、`developer.hellowaka.com`、`app.hellowaka.com`、`status.hellowaka.com`均无法解析；只有 `portal.hellowaka.com`响应。

### 招聘所需技术背景

招聘希望候选人做过支付与清结算系统、第三方支付渠道与 Partner API 集成、商户 Portal 与内部运营工具，以及事务一致性、幂等、重试与补偿、可观测性、监控和发布规范。支付、清结算、会计、交易或银行系统经验属于优先而非必需。链上结算、数字资产支付或 Web3 只作为 Tech Lead 的优先条件出现，不能据此认定当前生产系统使用 EVM 链或任何特定区块链技术栈。招聘未要求爬虫或 ERP 集成背景。

### 行业领域

非洲—亚洲贸易结算。公司公开材料涉及：

- **中国入境结算规则。** [合作文章](https://frontierfintech.substack.com/p/117-payments-follow-trade)称每笔付款都附有“使其符合 SAFE 和 PBOC 框架”的文件，即中国国家外汇管理局和央行框架。
- **多司法辖区 AML／KYB。** 13 个非洲市场收款，并向中国、香港、新加坡付款，各有登记和报告制度；网站页脚将可用性限定于“KYB、合规审查、支持的走廊和适用监管要求”。
- **外汇与做市。** 服务描述包括面向所称 20 种货币、100 多家流动性提供商的“外汇流动性管理和做市”。
- **本地渠道。** 移动货币（Pyxis 点名 M-PESA）、银行转账、Alipay、WeChat Pay、FPS、FAST、RTGS、SWIFT 和 USDT 出入金。
- **人民币国际化。** 创始人 Newsletter 涉及 [PBOC 清算行结构](https://aprilnewsletter.substack.com/p/standard-banks-rmb-clearing-news)（2026-06-29）、[非洲商户直接人民币支付](https://aprilnewsletter.substack.com/p/deep-dive-why-do-we-need-rmb-payment)（2025-12-17）和[政策对 USDT／CNY 锚定的影响](https://aprilnewsletter.substack.com/p/how-policy-is-reshaping-the-usdtcny)（2025-12-11）。

[工程职位（2026-07-28）](https://www.v2ex.com/t/1230527)直接写明：“不要求一开始就熟悉非洲支付或跨境金融，但希望愿意理解商户、运营、合规、支付渠道和结算流程，再把这些业务问题变成可靠产品和系统。”领域知识被定位为入职后学习；支付／金融科技背景在两个职位中都只是加分项。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 雇佣形式 | Tech Lead：“全职，远程”；全栈：“全职固定期限合同，远程工作”——两个职位合同条件不同 | [Tech Lead](https://www.v2ex.com/t/1230518)、[全栈](https://www.v2ex.com/t/1230527) |
| 地点 | 两者均为“全球远程”。Waka 未公开办公室地址；Terms 给出澳大利亚注册地址；招聘称总部在新加坡 | [招聘帖](https://www.v2ex.com/t/1230518)、[Terms](https://portal.hellowaka.com/static/GeneralTerms.html) |
| 时区 | “主要协作时区：UTC+3／UTC+8”（两个职位） | [招聘帖](https://www.v2ex.com/t/1230518) |
| 股权 | “公司期权：早期优秀贡献者有机会获得”（两个职位） | [招聘帖](https://www.v2ex.com/t/1230518) |
| 工程团队工作语言（推断） | 未找到正式政策，两则招聘帖均使用中文。全栈职位要求阅读英文资料并与海外团队进行基础英文沟通；Tech Lead 要求用英语与海外团队和合作伙伴沟通。这能证明跨境工作需要英语，但不能确认团队日常主要语言 | [Tech Lead](https://www.v2ex.com/t/1230518)、[全栈工程师](https://www.v2ex.com/t/1230527) |
| 薪资 | 两个职位均未说明；[工程帖](https://www.v2ex.com/t/1230527)中两次询问范围，截至 2026-07-29 未获答复 | [招聘帖](https://www.v2ex.com/t/1230527) |
| AI 工具 | 写成明确要求而非福利：工程职位要求“主动使用 AI 工程工具，而不是只按传统方式开发”，两个职位都把“深度使用 Codex、Claude Code 或类似 AI 工程工具”列为加分项 | [招聘帖](https://www.v2ex.com/t/1230518) |
| 公司自述的工作环境 | 两个职位都描述需求不完整——“很多需求没有完整 spec”——并处于 0 到 1 的建设阶段，而非成熟系统的维护 | [招聘帖](https://www.v2ex.com/t/1230527) |
| 签证、福利、离职 | 未公开 | — |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-07-29）：hellowaka.com 与 pyxis.money 的导航、`robots.txt`、sitemap、Portal 和法律页面；当前及归档品牌网站；以 Waka、Pyxis、Pyxis Pay 进行的中英文检索；常见文档、API、状态页和招聘子域名；按公司名、域名和产品名进行的 GitHub 检索；两则已确认的 V2EX 招聘帖；公司与创始人社交页面；FINTRAC、AUSTRAC、ABN 和新加坡登记；投资机构 portfolio 与融资数据库。

- hellowaka.com 和 pyxis.money 都没有招聘页；唯一招聘资料是 2026-07-28 的两个 V2EX 帖，均未由公司渠道链接。
- 两个职位均无薪资、签证政策或福利；帖子中直接询问范围的问题未获回答。
- Waka 或 Pyxis 名义下没有工程博客、会议演讲、开源仓库或公开技术文章。
- 虽然网站把 API 营销为“the scale layer”，但没有公开 API 文档、SDK、sandbox 或状态页。
- 没有公开价目表或 fee schedule，尽管 Terms 提到网站上存在。
- 没有团队或管理层页面；公开可确认在 Waka 的只有 CEO 和 Head of Partnerships 两人。
- 网站和法律文件均未声明 ISO 27001、SOC 2、PCI DSS 等安全认证。
- Terms 中的“Waka”实体没有公开公司注册号、ABN／ACN 或许可证编号。
- Waka 名义下没有融资轮次、金额、估值或投资者名单。
- Pyxis 共同创始人 George Chan 是否在 Waka 任职未公开。

### 不同来源之间的不一致

- **监管登记。** [网站页脚](https://www.hellowaka.com/)称服务通过加拿大 FINTRAC 和澳大利亚 AUSTRAC 登记实体提供。截至 2026-07-29，[FINTRAC MSB](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx)唯一关联实体 PYXIS PAY LIMITED 的 M24908802 状态为“Expired”、到期日 2026-01-23，没有 Waka；[AUSTRAC Remittance Sector Register](https://online.apps.austrac.gov.au/rsr/)对两个名称均无结果。这可能意味着登记实体使用了本页未识别的名称。
- **Terms 司法辖区。** [General Terms V1.2](https://portal.hellowaka.com/static/GeneralTerms.html)给出 Victoria 的 Doncaster East 注册地址，但称条款受澳大利亚 New South Wales 法律管辖并解释。
- **前身成立年份。** [Pyxis About](https://www.pyxis.money/about)称“成立于 2022”；[Singapore FinTech Association](https://membership.singaporefintech.org/company/202306267Z)称 Pyxis Pay Pte. Ltd. 成立于 2023（UEN 202306267Z）；[FINTRAC](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx)记录 Pyxis Pay Limited 成立于 2023-10-16。
- **不同时间与来源类型的员工人数。** 前身在 [2025-09-19](https://share.transistor.fm/s/27884a18)称四国 12 人；Waka／Pyxis 招聘帖于 [2026-07-28](https://www.v2ex.com/t/1230518)称“约二十人”。[LinkedIn](https://www.linkedin.com/company/hellowaka/)只提供 11–50 的宽泛区间（无日期，访问于 2026-07-29），不作为相互冲突的精确人数。
- **团队地点。** 招聘称成员在“非洲、中国、新加坡和澳大利亚”；[2026 年 2 月网站](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/)称“内罗毕、香港、新加坡和其他贸易枢纽”。两者分别未提香港和中国。
- **不同网站版本的产品主张。** [2026-02-26 归档](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/)有“典型结算 24 小时”“外汇成本降低 70%”“比传统路径最多便宜 70%”“首个直接交付人民币的稳定币贸易结算网络”；[2026-07-29 网站](https://www.hellowaka.com/)不再出现这些数字或“第一”主张。
- **业务数字独立性。** 年流量 1 亿美元、八个市场、100 多家流动性提供商、20 种货币都来自同一篇 [Frontier Fintech](https://frontierfintech.substack.com/p/117-payments-follow-trade)，其副标题和署名明确标为“A Partner Piece”“Co-Written with April Long, CEO and Cofounder at Waka”。未找到独立确认。

### 其他

- **公开的策略变化。** [2025-09-19 播客](https://share.transistor.fm/s/27884a18)中，CEO 称花两年服务非洲中小企业，“在内罗毕批发市场驻点六个月后需求为零”，随后转向大宗贸易商和中国贸易公司，并称“90% 的非洲贸易仍以更传统方式进行”。当前网站面向“进口商、金融科技公司、资金团队、市场平台、稳定币企业和 OTC 交易台”，而非小商户。
- **公开的产品表面。** Waka 未公开开发者文档、API reference、价目表或状态页。仅 Terms 和 Privacy Policy 两份 V1.2（2026-03-12）公开文件有一定具体内容。

---

## 资料来源

**官方**

- [Waka — hellowaka.com](https://www.hellowaka.com/) · [Partner Portal](https://portal.hellowaka.com/)
- [General Terms V1.2，2026-03-12](https://portal.hellowaka.com/static/GeneralTerms.html) · [Privacy Policy V1.2，2026-03-12](https://portal.hellowaka.com/static/PrivacyPolicy.html)
- [LinkedIn — Waka](https://www.linkedin.com/company/hellowaka/)
- [April's Newsletter（创始人 Substack，公司链接为博客）](https://aprilnewsletter.substack.com/)
  - [Welcome — 2025-09-05](https://aprilnewsletter.substack.com/p/welcome-to-aprils-newsletter)
  - [USDT／CNY — 2025-12-11](https://aprilnewsletter.substack.com/p/how-policy-is-reshaping-the-usdtcny)
  - [Africa's Trade Needs RMB — 2025-12-15](https://aprilnewsletter.substack.com/p/beyond-payment-why-rmb-is-the-api)
  - [Direct RMB Payment — 2025-12-17](https://aprilnewsletter.substack.com/p/deep-dive-why-do-we-need-rmb-payment)
  - [Trade Payments — 2026-05-05](https://aprilnewsletter.substack.com/p/arent-remittance-companies-already)
  - [Standard Bank RMB Clearing — 2026-06-29](https://aprilnewsletter.substack.com/p/standard-banks-rmb-clearing-news)

**前身品牌（Pyxis）**

- [pyxis.money](https://www.pyxis.money/) · [About](https://www.pyxis.money/about)
- [Singapore FinTech Association — Pyxis Pay](https://membership.singaporefintech.org/company/202306267Z) · [Orbit Ventures](https://orbitventures.com/company/pyxis/) · [Crunchbase](https://www.crunchbase.com/organization/pyxis-8b86)

**招聘信息**（以 Pyxis 名义发布，申请至 `ncrew@pyxis.money`，中文）

- [V2EX — Tech Lead — 2026-07-28 20:21 +08:00](https://www.v2ex.com/t/1230518)
- [V2EX — 全栈工程师 — 2026-07-28 20:56 +08:00](https://www.v2ex.com/t/1230527)

**登记与一手记录**

- [FINTRAC MSB Registry（XLSX）](https://fintrac-canafe.canada.ca/msb-esm/reg-eng.xlsx) · [查询页](https://fintrac-canafe.canada.ca/msb-esm/reg-eng)
- [AUSTRAC Remittance Register](https://online.apps.austrac.gov.au/rsr/) · [Virtual Asset Register](https://online.apps.austrac.gov.au/vaspr/)
- [ABN Lookup](https://abr.business.gov.au/) · [CBK 支付服务商目录，2025-11-06](https://www.centralbank.go.ke/wp-content/uploads/2025/11/Directory-of-Authorized-Payment-Service-Providers-6-November-2025.pdf)
- [Internet Archive — hellowaka.com](https://web.archive.org/web/20260226060002/https://www.hellowaka.com/)

**第三方报道与档案**

- [Frontier Fintech，2026-04-20](https://frontierfintech.substack.com/p/117-payments-follow-trade)——CEO 共同撰写的合作文章，当前业务数字的来源
- [African Tech Roundup，2025-09-19](https://share.transistor.fm/s/27884a18) · [SoundCloud](https://soundcloud.com/african-tech-round-up/april-long-of-pyxis-why)
- [NTU-SBF CAS，2024-08-29](https://www.ntu.edu.sg/cas/news-events/news/details/singaporean-targets-kenya-china-trade-with-new-payment-platform)
- [Business Daily，2024-08-22](https://www.businessdailyafrica.com/bd/corporate/technology/kenyan-traders-to-pay-for-chinese-goods-via-alipay-4735424)
- [China Daily，2024-08-27](https://www.chinadaily.com.cn/a/202408/27/WS66cd98daa31060630b9253a4.html)
- [LinkedIn — April Long](https://www.linkedin.com/in/longapril/)（无日期；2026-07-29 通过搜索结果访问，个人页面对自动访问返回 HTTP 999）· [Michael Ogongo](https://www.linkedin.com/in/michael-ogongo-2a666612a/)
