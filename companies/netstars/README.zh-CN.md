# NETSTARS（ネットスターズ）

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

NETSTARS（株式会社ネットスターズ）是一家总部位于东京的支付网关公司，成立于 2009-02-12，自 2023-09-26 起在东京证券交易所 Growth 市场上市（证券代码 5590）。主力产品 **StarPay** 让商户通过一次签约、一套结算和一个管理后台，就能受理 40 多个二维码支付品牌，外加信用卡和电子货币；第二条产品线 **StarPay-DX** 则向同一批商户销售自助收银、移动点单、预约和小程序产品。

- FY2025（截至 2025-12 的财年）支付流水（GPV）为 **2 兆 1,228 亿日元**，同比增长 33.2%；营收 **47.88 亿日元**（+22.7%），营业利润 **2.93 亿日元** —— 上市以来首次实现全年营业盈利（[FY2025 決算短信](https://ssl4.eir-parts.net/doc/5590/tdnet/2757309/00.pdf)、[FY2025 有価証券報告書 p.21](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。
- 截至 2025-12-31，日本国内约 **70 万个账户**（门店、自动售货机、售票机等），来自约 15,000 家直签企业（[有価証券報告書 p.6](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)、[数字信息图](https://www.netstars.co.jp/infographics/)——无日期，访问于 2026-07-29）。
- 2025-12-31 合并员工 **221 人**，其中东京母公司 146 人、大连开发子公司 70 人。母公司平均年龄 38.2 岁、平均工龄 3.8 年、平均年薪 **693 万日元**（[有価証券報告書 pp.10, 23](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。
- 公司自述的技术形态是 AWS（据其自家材料还包括 Google）之上的云原生 + 容器；披露 2025 全年支付成功率 **99.999%**、单笔 40 毫秒，同时在法定文件中把"研究开发活动"填为"无"（[FY2026 Q1 決算説明資料](https://ssl4.eir-parts.net/doc/5590/tdnet/2811540/00.pdf)、[有価証券報告書 p.22](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。

---

## 基本情况

| 项目 | 内容 | 出处 |
|---|---|---|
| 法定名称 | 株式会社ネットスターズ / NETSTARS Co.,Ltd. | [有価証券報告書 p.1](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 成立 | 2009-02-12（注册地为千叶市美浜区） | [公司页面](https://www.netstars.co.jp/about)、[有価証券報告書 p.5](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 上市 | 东证 Growth，代码 5590，2023-09-26 上市 | [有価証券報告書 p.4](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 总部 | 东京都中央区八丁堀 3-3-5 住友不动产八丁堀大厦 3F/4F，邮编 104-0032 | [公司页面](https://www.netstars.co.jp/about) |
| 法定代表人 | 李 剛（り つよし），代表取締役社長 CEO | [有価証券報告書 p.1](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 资本金 | 45.0477 亿日元（2026-03-31）；44.8927 亿日元（2025-12-31） | [公司页面](https://www.netstars.co.jp/about)、[有価証券報告書 p.3](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 员工数 | 合并 221 人、母公司 146 人（2025-12-31）；合并 224 人（2026-03-31） | [有価証券報告書 p.10](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)、[公司页面](https://www.netstars.co.jp/about) |
| 报告分部 | 单一分部："金融科技事业" | [有価証券報告書 p.6](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| GPV（FY2025） | 2 兆 1,228 亿日元 | [有価証券報告書 p.21](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 已部署账户数 | 国内约 70 万（2025-12-31） | [有価証券報告書 p.6](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 直签企业数 | 约 15,000 家 | [数字信息图](https://www.netstars.co.jp/infographics/)；无日期，访问于 2026-07-29 |
| 审计机构 | 太陽有限責任監査法人（Grant Thornton Taiyo） | [有価証券報告書 p.2](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |

### 集团公司

| 公司 | 所在地 | 资本金 | 文件所述职能 | 持股 | 员工数（2025-12-31） |
|---|---|---|---|---|---|
| NETSTARS ASIA HOLDINGS PTE. LTD. | 新加坡 | 238.8 万美元 | 面向海外支付服务公司的销售 | 100% | 2 |
| NETSTARS VIETNAM CO., LTD. | 越南河内 | 209.91485 亿越南盾 | 系统开发 | 100%（间接） | 3 |
| 納思達科技（大連）有限公司 | 中国大连 | 100 万人民币 | 系统开发、推广 | 100% | 70（+4） |
| Net Stars Hong Kong Limited | 中国香港 | 25 万美元 | 国际汇款 | 40%（权益法） | — |
| 株式会社StarPay-Entertainment | 东京 | 4,500 万日元 | 娱乐类线上支付、游戏平台运营与发行 | 100% | — |

出处：[有価証券報告書 pp.9, 23](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)；StarPay-Entertainment 见 [2025-12-19 公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2733249/00.pdf)（2026-01-26 设立，自 FY2026 Q1 起并表，代表取締役为長福久弘）。Net Stars Hong Kong 是与 Finext Limited 设立的合资公司，[2024-08-14 公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2492220/00.pdf)。大连子公司的**北京分公司（13 人，2022-07 设立）已于 2025 年 10 月关闭**，职能集中到大连（[2025-08-25 公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2679923/00.pdf)）；FY2025 计入了含办公场所关闭费用在内的特别损失 4,095 万日元（[有価証券報告書 p.20](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。公司页面另列有横滨营业所（[公司页面](https://www.netstars.co.jp/about)）。

### 资质、认证与行业协会

来自[公司页面](https://www.netstars.co.jp/about)：

- **PCI DSS Ver 4.0.1 完全合规**，登记号 SYPQ233UG1TP
- **Privacy Mark**（隐私标志）认证号 第17003614(04)号
- **资金移动业者**（資金移動業者），关东财务局长第 00098 号 —— [有価証券報告書 p.5](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) 记为 2025 年 5 月完成第二种登记，公司页面记为 2025 年 3 月
- 信用卡号码等处理合同缔结事业者；电信事业者备案号 A-23-12267；有偿职业介绍事业许可号 13-ユ-318648
- 加入的团体：Fintech 协会、日本信用卡协会、无现金推进协议会（キャッシュレス推進協議会）、JNTO（日本政府观光局）、日本全渠道协会、日本资金结算业协会

### 公司自述的市场环境

来自 [FY2025 決算短信](https://ssl4.eir-parts.net/doc/5590/tdnet/2757309/00.pdf) 与 [有価証券報告書 p.11](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)：

- 经济产业省"2025 年前无现金支付比率达 40% 左右"的目标已提前达成，按旧口径 2024 年为 42.8%。
- 按经产省 2025-12-26 公布的新计算口径，2024 年该比率为 51.7%，目标为 2030 年 65%、长期 80%。
- 公司引用矢野经济研究所《2025年版 コード決済市場の実態と展望》，称码支付正扩展到线上、订阅型和高客单价的面对面场景。
- [2026 年 3 月成长可能性披露文件](https://ssl4.eir-parts.net/doc/5590/tdnet/2783892/00.pdf) 列出 2018–2024 年二维码支付金额 CAGR +120%、信用卡 +10%、NFC +2%，出处为无现金推进协议会、日本信用卡协会和日本银行。
- 日本《智能手机软件竞争促进法》（スマホソフトウェア競争促進法）于 2025 年 12 月施行，放开了应用内购买以外的支付手段；公司称这是设立 StarPay-Entertainment 的原因（[2025-12-19 公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2733249/00.pdf)）。

---

## 产品

### StarPay —— 多元无现金支付网关

商户与 NETSTARS 签约一次，即可受理二维码支付、信用卡、通用积分、电子货币，以及（2026 年起）稳定币；开通、审核、结算和对账统一在 **StarPay-Works** 管理后台完成（[StarPay 站点](https://starpay.netstars.co.jp/)）。接入形态包括 NETSTARS 自有终端、iOS/Android 应用，或通过 API 接入既有 POS、自动售货机、售票机、储物柜和线上收银台（[StarPay FAQ](https://starpay.netstars.co.jp/faq/)）。营销页面标注 **99.9% 稼动保证**、7×24 小时支持中心、PCI DSS 认证，以及最短一周上线。

品牌覆盖数（截至 [2026 年 3 月成长可能性披露文件](https://ssl4.eir-parts.net/doc/5590/tdnet/2783892/00.pdf)）：**40+ 二维码品牌、6 个信用卡品牌、7 个电子货币品牌**，并计划在 FY2026 新增"10 个以上"支付品牌。[数字信息图页面](https://www.netstars.co.jp/infographics/) 补充：通过 StarPay 可在日本使用的境外二维码服务来自 **13 个国家/地区**（数据截至 2025-12）。

### StarPay-DX 及周边产品

| 产品 | 说明 | 链接 |
|---|---|---|
| StarPay-DX | 门店 DX 的统称：预约、餐桌点单、会员、优惠券、外带、电商 | [页面](https://www.netstars.co.jp/starpay-dx/) |
| Regi-less 平台 | 自助收银 / 无人门店平台 | [regi-less.jp](https://regi-less.jp/) |
| StarPay-Order | 自助点单机与移动点单（已部署于 2024-06 开业的星野集团 1955 东京湾） | [2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) |
| StarPay-mini | 在超级应用（LINE 等）内的小程序开发 | [starpay-mini](https://starpay-mini.netstars.co.jp/) |
| StarPay 数字商品券 | 面向地方政府和商圈的电子代金券 | [house-coin](https://starpay.netstars.co.jp/house-coin/) |
| 区域积分服务 | 地方政府积分兑换 | [页面](https://www.netstars.co.jp/areapoint_service/) |
| StarPay-Robot | 小型自动清洁设备，带远程管理 | [starpay-robot.com](https://starpay-robot.com/) |
| StarPay-X | 公司提出的连接 Web2 与 Web3 的网关构想（多链、多钱包、多币种） | [页面](https://www.netstars.co.jp/starpayX/) |
| KubeStar | 基于 Kubernetes 的容器即服务平台，含多云管理、镜像漏洞扫描与攻击检测 | [页面](https://www.netstars.co.jp/kubestar/) |
| JPQR Global | 跨境二维码互通；NETSTARS 建设并运营"JPQR 转接系统"，担任 switcher | [2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) |
| Stablecoin Pay | 在 StarPay 内受理稳定币 | [2026-07-13 新闻稿](https://www.netstars.co.jp/news/9450/) |

### 变现方式

见 [有価証券報告書 p.7](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)：

- **支付**：NETSTARS 按支付金额向商户收取手续费，扣除支付事业者手续费后的净额计为自身收入。对直签商户，公司先从各支付品牌收到结算款，扣除自身手续费后于次月汇给商户 —— 这正是代收商户款项（預り金，2025-12-31 为 301.31 亿日元）主导资产负债表的原因。对 OEM 合作方，按支付总额收取手续费。若商户由取次店（转介代理）带来，公司需按流水向该代理支付费用，计入成本。
- **DX 产品**：导入时的初期开发/上线费用，按功能不同的月度使用与运维费，以及经由 DX 产品产生的支付流水手续费。
- **终端**：有需要的商户可购买；终端销售毛利率低于支付手续费，拉低了 FY2025 Q4 的整体毛利率（[FY2025 決算説明会 主要Q&A — 2026-02-20](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/199265/00.pdf)）。
- **Stablecoin Pay** 公开标价 **0.98%** 交易手续费（[2026-07-13 新闻稿](https://www.netstars.co.jp/news/9450/)）。

未找到 StarPay 的公开价目表；官网只提供申请表单或咨询表单。

### 历年披露的规模数字

| 日期 | 披露数字 | 出处 |
|---|---|---|
| 2018-12 | 超过 10 万个点位 | [公司沿革](https://www.netstars.co.jp/about) |
| 2021-04-14 | 超过 28 万个点位；37 个支付品牌 | [融资新闻稿](https://www.netstars.co.jp/news/3486/) |
| 2023 | 超过 40 万账户（上市当年） | [2026 年 3 月说明资料，沿革页](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) |
| 2024-10 | 超过 50 万个点位 | [公司沿革](https://www.netstars.co.jp/about) |
| 2025-12-31 | 约 70 万账户；FY2025 GPV 2 兆 1,228 亿日元 | [有価証券報告書 p.6](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)、[数字信息图](https://www.netstars.co.jp/infographics/) |

分年度 GPV 增速（来自 [2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) 上的标注）：FY2019 +292%、FY2020 +56%、FY2021 +118%、FY2022 +94%、FY2023 +46%、FY2024 +21%、FY2025 +33%。2018-12 → 2025-12 的七年 CAGR 公司标为 **+162%**。绝对值：FY2024 1 兆 5,942 亿日元 → FY2025 2 兆 1,228 亿日元（[有価証券報告書 p.21](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。FY2026 Q1 GPV 为 5,497 亿日元，同比 +17.6%（[FY2026 Q1 決算短信](https://ssl4.eir-parts.net/doc/5590/tdnet/2811008/00.pdf)）。

### 收入构成

| 科目 | FY2023 | FY2024 | FY2025 | FY2026 预测 |
|---|---|---|---|---|
| 支付相关（不含终端） | 25.02 亿（72.6%） | 32.15 亿（82.4%） | 39.18 亿（81.8%） | — |
| 终端销售 | 7.45 亿（21.6%） | 0.99 亿（2.6%） | 3.92 亿（8.2%） | — |
| 支付相关合计 | — | 33.15 亿 | 43.10 亿 | 51.50 亿 |
| DX / 小程序 | 1.34 亿（3.9%） | 3.60 亿（9.2%） | 3.17 亿（6.6%） | 4.10 亿 |
| 其他 | 0.65 亿（1.9%） | 2.25 亿（5.8%） | 1.60 亿（3.4%） | 2.00 亿 |
| **合计** | 34.47 亿\* | 39.02 亿 | 47.88 亿 | 57.60 亿 |

单位为日元。出处：[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf)。\*FY2023 在该资料中被追溯调整，剔除了 2023 年 4 月终止的国际通信业务；法定口径的 FY2023 营收为 37.20 亿日元（[有価証券報告書 p.2](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。

**客户集中度** —— 占营收 10% 以上、需披露的两家交易对手（[有価証券報告書 p.19](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）：

| 交易对手 | FY2024 | FY2025 |
|---|---|---|
| PayPay株式会社 | 10.49 亿日元（26.9%） | 12.20 亿日元（25.5%） |
| 株式会社NTTドコモ | 7.10 亿日元（18.2%） | 8.57 亿日元（17.9%） |

### 已公告的客户、合作方与上线事件

| 日期 | 对方 | 内容 |
|---|---|---|
| 2015-04-27 | 腾讯 | 签订 WeChat Pay 代理合同；StarPay 于 2015 年 7 月上线 |
| 2018-10 | PayPay、乐天 Pay | 接入 StarPay |
| [2024-03-25](https://ssl4.eir-parts.net/doc/5590/tdnet/2412982/00.pdf) | 三井住友卡 | 被 stera terminal unit / mobile 采用为二维码支付网关 |
| [2024-10-18](https://ssl4.eir-parts.net/doc/5590/tdnet/2511643/00.pdf) | 横滨市 | StarPay 用于完全无现金巴士实证运行 |
| [2025-04-23](https://ssl4.eir-parts.net/doc/5590/tdnet/2596644/00.pdf) · [2025-09-04](https://ssl4.eir-parts.net/doc/5590/tdnet/2684247/00.pdf) | Stripe | 码支付协作；StarPay 接入 Stripe Terminal |
| [2025-07-04](https://ssl4.eir-parts.net/doc/5590/tdnet/2651324/00.pdf) · [2025-08-18](https://ssl4.eir-parts.net/doc/5590/tdnet/2678096/00.pdf) | 2025 大阪·关西世博会 | 担任 JPQR Global 转接系统运营方；首批为柬埔寨，随后为印尼 QRIS |
| [2025-12-23](https://ssl4.eir-parts.net/doc/5590/tdnet/2734089/00.pdf) | 羽田机场第 3 航站楼 | 自 2026 年 1 月起的 USDC 门店支付实证，公司称为日本首例 |
| [2026-04-13](https://www.netstars.co.jp/news/9148/) | Circle | 基于 Circle 跨链基础设施 "Gateway" 的 USDC 多链开发 |
| [2026-06-15](https://www.netstars.co.jp/news/9318/) | Startale Group | Web3 支付基本协议（JPYSC、USDSC） |
| [2026-07-21](https://www.netstars.co.jp/news/9492/) | 横滨中华街 | 溢价商品券项目 |

公司列举的商户业态示例：超市与家居中心、药妆店、商业设施/百货/体育用品店、机场、酒店与娱乐设施、加油站、餐饮与食品服务、保险（[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf)）。销售网络方面，公司称拥有约 **300 家销售合作方**，包括 OEM 合作方、取次店、地方银行与信用金库，以及主要 POS 厂商（[同一资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf)）。

### 公司自述的计划

公司在 [2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) 和[成长可能性披露文件](https://ssl4.eir-parts.net/doc/5590/tdnet/2783892/00.pdf) 中提出了"2030 年应有之姿"：

- 到 FY2030，仅靠现有业务的内生增长实现 GPV **超过 6 兆日元**、支付相关营收 **超过 100 亿日元**、全公司营收 **超过 120 亿日元**。文件将其标注为 2023–2030 年目标 GPV CAGR **+25.0%**，对应 2023–2026 年的"进度 CAGR" +24.6%。
- 毛利率维持在 **70% 以上**；营业利润率与经常利润率达到 **25% 以上**（FY2025 实际营业利润率为 6.1%）。
- 海外：在现有的**卡塔尔、柬埔寨、蒙古**之外增加地区和商品。
- 进一步利用云计算、Web3.0 和 AI 压低服务器与开发成本，并开发面向细分业态的支付/汇款/DX 产品；明确将 M&A 列为进入新领域的手段之一。
- FY2026 业绩预测：营收 57.60 亿日元（+20.3%）、营业利润 5.00 亿日元（+70.8%）、经常利润 7.07 亿日元（+59.7%）、归母净利润 4.93 亿日元（+1.7%）、GPV 2 兆 5,474 亿日元（+20.0%）（[FY2025 決算短信](https://ssl4.eir-parts.net/doc/5590/tdnet/2757309/00.pdf)）。
- 创业以来从未分红，FY2026 也计划不分红（[有価証券報告書 p.17](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。

---

## 创始人

**李 剛（Ri Tsuyoshi）** —— 创始人、代表取締役社長 CEO。生于 1974-04-08。持股 3,317,000 股，占扣除库存股后已发行股份的 19.71%，为第一大单一股东（[有価証券報告書 pp.56, 66](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。

- 毕业于吉林大学物理学系（[公司页面](https://www.netstars.co.jp/about)）。
- 1999-04：入职株式会社 CSK（现 SCSK）（[有価証券報告書 p.66](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。
- 2005-04：入职新日铁解决方案。公司页面称其在 CSK 与新日铁解决方案期间负责 Cisco 网络的设计与建设（[公司页面](https://www.netstars.co.jp/about)）。
- 2009-02：创办 NETSTARS，出任代表取締役社長 CEO。
- 2014-08：任ウィ・ジャパン株式会社代表取締役。2018-10：任 NETSTARS ASIA HOLDINGS 董事。2019-10：任一般社团法人日中旅游商务协会理事。
- 长篇访谈：[日经"ベンチャー魂のひと"](https://www.nikkei.com/article/DGXZQOUB176YA0X10C25A2000000/)、[周刊经济学人 主编访谈](https://www.weekly-economist.com/interview/ri_tsuyoshi/)。

[有価証券報告書 p.16](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) 把"对特定人物的依赖"列为具名的经营风险（可能性：低；影响度：中），并说明正在引入执行役员和部长级人才以降低该风险。

### 主要管理层

| 姓名 | 职务 | 文件所述背景 |
|---|---|---|
| 陳 斌 / Chuck Chen | 取締役 CTO（2020-01 起） | 吉林大学信息工程系工学硕士。历任新加坡航空、Kaiser Foundation Health Plan、日立软件（美国）、Abacus International、Nokia of America，2009 年起入职 eBay（公司页面表述为 eBay/PayPal 高级架构师，负责移动技术架构），2014 年起任中国易宝支付 CTO |
| 長福 久弘 | 取締役 COO（2022-02 起） | 立正大学。历任 Advantage、Magic Ice Japan、Turbolinux、livedoor（2009）、LINE Business Partners、AUBE、出前館社外役员，2017-12 任 LINE Pay 取締役 COO，2020-03 任 LINE Pay 代表取締役 CEO；2021-09 加入 NETSTARS |
| 安達 源 | 取締役 CFO（2021-09 起） | 庆应义塾大学法学部。2013 年入职花旗集团证券，2015 年入职高盛证券 |
| 王 鯤 | 取締役（2011-10 起） | 南京理工大学信息工程学部。历经中国企业，2010 年入职三通；公司页面称其统管 StarPay 开发 |
| 吉田 興佳 | 取締役（2011-02 起） | 大连理工大学计算机信息与科学专业。历任松下 ITS、富士通 Frontech；公司页面称其统管 StarPay-mini 与新产品开发 |
| 李 大偉 | 执行役员（2026 年起） | 吉林大学毕业，北京大学研究生院。曾任中国易宝支付高级架构师；文件所述职责为支付基础设施建设与工程效率化 |

以上人员因直接负责技术、产品、运营、财务或工程效率而收录。出处：[有価証券報告書 pp.66–71](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)与[公司页面](https://www.netstars.co.jp/about)。完整法定董事和监事名单保留在监管文件中。

---

## 资本与财务

### 已公告的融资与资本合作

| 日期 | 事件 | 金额 | 参与方 | 出处 |
|---|---|---|---|---|
| 2016-07 | 资本业务合作 | — | 新生银行 | [公司沿革](https://www.netstars.co.jp/about) |
| 约 2018-02 | 资本合作 | — | NTT 越南（NTT 东日本集团）、伊藤忠 Techno-Solutions | [公告](https://www.netstars.co.jp/news/737/) |
| 2019-11-21 | 资本合作 | — | 伊藤忠商事 | [公告](https://www.netstars.co.jp/notification/2169/)、[伊藤忠新闻稿](https://www.itochu.co.jp/ja/news/press/2019/191121.html) |
| 2019-11-21 | 资本合作 | — | SCSK、T-Gaia | [公告](https://www.netstars.co.jp/notification/2171/)、[SCSK 新闻稿](https://www.scsk.jp/news/2019/press/product/20191121_2.html) |
| 2020-05 | 融资 | — | LUN Partners Group Limited | [公司沿革](https://www.netstars.co.jp/about) |
| 2020-09-30 | 追加融资 | 2020 年 5–9 月合计约 30 亿日元 | LUN Partners Group Limited 等 | [公告](https://www.netstars.co.jp/notification/3000/) |
| 2021-04-14 | 融资 | **合计 66 亿日元**，其中 40 亿来自 KKR 管理的基金 | KKR、SIG、LUN Partners 等 | [新闻稿](https://www.netstars.co.jp/news/3486/) |
| 2022-03 | 资本业务合作 | — | リージョナルマーケティング（Satudora Holdings 子公司） | [有価証券報告書 p.5](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 2023-09-26 | IPO，东证 Growth | 发行价 1,450 日元；承销价 1,334 日元；新股 700,000 股；缴款总额 9.338 亿日元 | 主承销商大和证券 | [有価証券報告書 p.55](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)、[ipokiso](https://www.ipokiso.com/company/2023/netstars.html) |

上表的轮次名称沿用公司自身表述；在查阅到的资料中，NETSTARS 从未使用 Series A/B/C 之类的标签。

### 所有权与稀释

截至 2025-12-31，创始人兼 CEO 李剛持有 3,317,000 股（**19.71%**），为第一大股东；KJP2 L.P. 持有 2,051,200 股（**12.19%**）。其他具名持股主要是托管和券商账户，文件未确认控股股东。FY2025 期末尚未行使的股票期权对应潜在稀释为已发行股份的 **11.28%**（[有価証券報告書 pp.16, 56](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。完整股东表和股份发行历史保留在监管文件中。

### 历年财务

| 财年（截至 12 月） | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| 营收（百万日元） | 1,964 | 2,987 | 3,721 | 3,902 | 4,788 |
| 经常损益（百万日元） | −1,014 | −566 | −329 | −22 | 443 |
| 归母净损益（百万日元） | −1,018 | −573 | −348 | −38 | 485 |
| 总资产（百万日元） | 18,512 | 21,579 | 28,356 | 35,740 | 38,354 |
| 自有资本比率（%） | 37.9 | 30.0 | 24.9 | 19.9 | 19.9 |
| 现金及现金等价物（百万日元） | 16,885 | 19,746 | 26,522 | 33,875 | 36,210 |
| 员工数（合并） | 184 | 217 | 223 | 223 | 221 |

出处：[有価証券報告書 p.2](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)。文件将 FY2021–FY2024 的亏损归因于在招聘、开发和促销上的前置投入。负债端以代收商户结算款为主：FY2025 期末預り金 301.31 亿日元，占负债总额 307.21 亿日元的绝大部分，文件也把当年负债增加的 20.88 亿日元归因于该科目随 GPV 增长。FY2025 期末仍有税务上的可结转亏损，被列为风险 —— 一旦用尽，实际税率将上升（[p.16](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。2026-04-30 签订了透支额度合同（[公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2797657/00.pdf)）。

---

## 工程

### 技术栈与平台

公司没有公开的技术栈页面。以下由招聘信息、法定文件和博客反推得出，明确标注为**推断**：

- **编程语言**：来自第三方招聘网站上"PG/開発メンバー"岗位的标签，列有 Java、Go、.NET/C#，并提到 Spring、Redis 和 Linux（[Green 180135](https://www.green-japan.com/company/6214/job/180135)）。同一网站的 PdM 岗位标签列有 JavaScript、Perl、Ruby、Java、Python、Go、MySQL 和 Kotlin（[Green 180138](https://www.green-japan.com/company/6214/job/180138)）。这些是招聘网站生成的标签列表，而非岗位正文中的"必须技能"，证据强度弱于岗位正文。
- **云与运行时**：法定文件中把 AWS 列为金融科技事业的基础，并称通过使用多个地理区域实现冗余，定期做漏洞诊断和非法访问对策（[有価証券報告書 p.15](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。投资者材料描述为"云原生基础设施 + 容器技术"，并称**同时使用多个云（AWS、Google）**以获得稳定性与安全性（[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf)）。
- **数据**：AWS Aurora 并做读写分离，ClickHouse 用于 OLAP，Tableau 用于分析，另有公司自称 **NoWorryDB** 的自研防错系统，保留 8 小时原始数据以便快速恢复；灾备设计为向异地数据库实时复制并自动故障切换（[技术博客，2024-06-04](https://www.netstars.co.jp/blog/7115/)）。
- **Kubernetes**：公司对外销售 **KubeStar**，一个基于 Kubernetes 的容器即服务产品，含一键部署/回滚、多云应用管理、容器镜像漏洞扫描和攻击检测（[产品页](https://www.netstars.co.jp/kubestar/)）。
- **现有招聘中提到的工具**：Postman、OpenSearch、Jira、Confluence、Backlog、自研测试工具，以及生成式 AI（Copilot）（[CE 岗位](https://recruit.jobcan.jp/netstars/job_offers/2180755)、[支付产品企划运营岗位](https://recruit.jobcan.jp/netstars/job_offers/2266198)）。
- **对外接口**：面向 POS 厂商、电商厂商、自动售货机、售票机、储物柜和应用内充值的 REST/Web API；二维码的 MPM 与 CPM 两种模式（[StarPay 站点](https://starpay.netstars.co.jp/)、[MPM 与 CPM 的区别，2026-07-15](https://www.netstars.co.jp/blog/9463/)）。未找到公开的开发者文档站点 —— API 规格似乎是在合同框架下提供给合作方的。

### 系统

| 系统 | 做什么 | 出处 |
|---|---|---|
| StarPay 支付网关 | 把商户的一笔交易路由到 40+ 二维码品牌之一，以及卡和电子货币通道；负责品牌签约、审核、结算轧差和按月付款给商户。披露 2025 年 1–12 月支付成功率 99.999%（不含第三方原因导致的错误）、单笔 40 毫秒、单笔成本 0.04 日元，截至 2025-12 面对面 800 TPS、线上 1,200 TPS | [FY2026 Q1 決算説明資料](https://ssl4.eir-parts.net/doc/5590/tdnet/2811540/00.pdf) |
| 审核 / 运营系统 | 商户审核与运营；单列的资本投入 1.683 亿日元，期间 2022-12 → 2027-12 | [有価証券報告書 p.24](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 数据平台 | 每日处理量被描述为数亿条支付数据；AWS Aurora + ClickHouse + Tableau，灾备复制与自动切换；团队被描述为拥有 10 年以上经验的数据科学家和工程师 | [博客，2024-06-04](https://www.netstars.co.jp/blog/7115/) |
| StarPay-DX / 小程序系统 | 自助收银、自助点单机与移动点单、预约、会员、优惠券；以原生应用、自助终端或超级应用内小程序形态交付。资本投入 1.366 亿日元，期间 2022-12 → 2027-12 | [有価証券報告書 p.24](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| JPQR 转接系统 | 日本 JPQR 标准与他国统一二维码标准（柬埔寨、印尼 QRIS）之间的 switcher；2023 年 8 月获选为经产省补贴的海外对接开发合作方 | [2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) |
| StarPay-X / Stablecoin Pay | 稳定币受理：Solana 与 Polygon 上的 USDC、USDT、JPYC，Aptos 计划 2026 年夏；已支持 MetaMask，计划支持 Bitget Wallet 与 imToken；目前为 CPM，MPM 计划中；商户以日元结算 | [2026-07-13 新闻稿](https://www.netstars.co.jp/news/9450/) |
| 扫码 | AI 辅助的二维码识别：一次扫描多个码、容忍角度倾斜、弱光、以及破损或污损的码 | [博客，2024-05-01](https://www.netstars.co.jp/blog/7067/) |
| KubeStar | 对外销售的 Kubernetes CaaS | [产品页](https://www.netstars.co.jp/kubestar/) |

**AI 在工程组织中的使用。** 公司称 AI 已用于核心系统效率化、运维应用监控、资源使用情况的智能分析、客服支持，以及 API 对接开发支持；FY2026 Q1 把包括销售部门在内的内部支持系统迁移到了 AI。公司披露 2025 年 GPV 同比增长 33% 的同时，以美元计价的服务器费用基本持平；FY2026 Q1 的 Q&A 中称 AI 降低了单笔支付成本、大幅削减了开发与对接工时、提升了客服效率，使其无需大幅增员即可管理和运营平台（[FY2026 Q1 決算説明資料](https://ssl4.eir-parts.net/doc/5590/tdnet/2811540/00.pdf)、[FY2026 Q1 主要Q&A](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/204228/00.pdf)）。

**研发。** FY2025 有価証券報告書的"研究開発活動"一栏填写的是"該当事項はありません"（无相应事项）（[p.22](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。FY2025 资本性支出合计 1.571 亿日元，其中 1.263 亿为计入软件仮勘定的部分（[p.23](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。公司称就自研的二维码支付系统持有专利，但未标明专利号（[p.16](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。

### 工程在哪里

按 2025-12-31 的设备状况表（[有価証券報告書 p.23](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）：东京总部 146 人（+22 临时）、大连 70 人（+4）、越南 3 人、新加坡 2 人。法定文件把大连和越南子公司描述为"主に当社の開発等の受託先"（主要是本公司的开发等受托方），大连实体被指定为特定子会社（[p.6](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。大连子公司的北京分公司（13 人）已于 2025 年 10 月关闭，开发职能集中到大连（[公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2679923/00.pdf)）。一篇博客的署名把扫码相关工作归属于"技術本部 Innovation Dept."（[2024-05-01](https://www.netstars.co.jp/blog/7067/)）。

截至 2026-07-29，公司自有招聘页面共列出 20 个岗位，其中没有一个是软件工程师岗；与技术相关的是 BtoB 客户工程师、门店 DX 产品经理和支付产品企划三个岗位，年薪区间 500–1,000 万日元（[岗位列表](https://recruit.jobcan.jp/netstars/list)）。

### 招聘所需技术背景

截至 2026-07-29，公司招聘网站没有软件工程师职位，因此查阅到的资料不能说明当前软件工程招聘要求或优先哪些技术背景。产品披露能够确认公司运行支付、多方结算、POS／设备集成、稳定币及 PCI DSS 范围内的系统，但这些系统本身不能证明相应经验是招聘条件。

### 行业领域

日本零售支付监管与多方结算机制。法定文件中的具体内容：

- **监管面**：《分期付款销售法》（割賦販売法）及行业指引对商户管理和安全提出要求；NETSTARS 持有资金移动业登记并运营跨境的 JPQR Global，公司把法规变更列为风险（可能性中，影响度小）（[有価証券報告書 p.15](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。维持 PCI DSS 4.0.1 完全合规（[公司页面](https://www.netstars.co.jp/about)）。
- **结算机制**：消费者、商户、二维码支付事业者和 NETSTARS 之间支付信息与资金的四步流转，以及由此产生的預り金负债，见 [有価証券報告書 p.7](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)；FY2025 期末余额为 301.31 亿日元。
- **交易对手合同**：已披露的框架协议包括腾讯（WeChat Pay，2015-04-27 起，1 年自动续约）、Alipay Singapore（2021-07-30 至 2024-07-29，3 年自动续约）、NTT docomo d払い（2018-05-22 起，任一方通知即可终止）、PayPay（2018-10-01 起，1 年自动续约）和 KDDI（2019-03-28 起，1 年自动续约）（[p.22](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。
- **地缘风险**：法定文件把"因国际纠纷等原因导致中国系二维码品牌（支付宝、微信支付）停止或终止受理"列为经营风险（[p.14](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。海外二维码（入境游）占 FY2025 GPV 的 7.3%；公司估算中国入境客减少的影响，按年化计约为 GPV −1.2%、营收 −2%（[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf)、[FY2025 主要Q&A](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/199265/00.pdf)）。
- **区块链**：2026 年的产品方向要求跨链（Solana、Polygon、Aptos、Canton）、跨钱包（MetaMask、Bitget Wallet、imToken）和跨币种（USDC、USDT、JPYC，以及 Startale 的 JPYSC/USDSC）工作，还涉及 Circle 的 Gateway 跨链基础设施（[2026-07-13 新闻稿](https://www.netstars.co.jp/news/9450/)、[2026-04-13 新闻稿](https://www.netstars.co.jp/news/9148/)）。

查阅到的资料中，没有任何一处说明工程师是否被要求掌握上述领域知识，或以何种方式掌握。

### 工作条件

| 项目 | 内容 | 出处 |
|---|---|---|
| 地点 | 东京总部（中央区八丁堀）；横滨营业所 | [公司页面](https://www.netstars.co.jp/about) |
| 远程 | 因岗位而异：客户工程师岗为"原则上到岗"；支付产品企划岗写明"原則出社"。第三方网站上较早的开发岗和技术支持岗写的是"每周至少一天远程，可协商" | [CE 岗位](https://recruit.jobcan.jp/netstars/job_offers/2180755)、[企划岗位](https://recruit.jobcan.jp/netstars/job_offers/2266198)、[Green 180135](https://www.green-japan.com/company/6214/job/180135) |
| 工时 | 弹性工作制，核心时段 11:00–14:00，标准工时 8 小时；标准班次写为 10:00–19:00（含 1 小时休息） | [企划岗位](https://recruit.jobcan.jp/netstars/job_offers/2266198) |
| 假期 | 年间休假 123 天，完全双休，年末年初与黄金周，带薪假，产假/陪产假与育儿假 | [CE 岗位](https://recruit.jobcan.jp/netstars/job_offers/2180755) |
| 语言 | PdM 岗位要求母语级日语；客户工程师岗位把英语或中文列为加分项而非必须。查阅到的岗位均未提到英语是公司内部通用语 | [PdM 岗位](https://recruit.jobcan.jp/netstars/job_offers/2154970)、[CE 岗位](https://recruit.jobcan.jp/netstars/job_offers/2180755) |
| 薪酬（母公司平均） | 年薪 693 万日元，含奖金和法定外工资；平均年龄 38.2 岁；平均工龄 3.8 年 | [有価証券報告書 p.10](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 股权 | 向董事和员工授予股票期权；FY2025 期末潜在稀释 11.28%。员工持股会奖励金上调，2026-02-24 公告 | [有価証券報告書 p.16](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)、[公告](https://ssl4.eir-parts.net/doc/5590/tdnet/2766521/00.pdf) |
| 工会 | 无；文件称劳资关系良好 | [有価証券報告書 p.10](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 多样性指标（母公司，FY2025） | 管理层女性比例 5.9%（FY2026 目标 ≥10.0%）；男性育儿假取得率 33.3%；男女薪酬差异 —— 全体劳动者 63.3%、正式员工 65.3%、兼职与有期合同 117.7% | [有価証券報告書 pp.10, 13](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 文件所述制度 | 可持续发展章节把弹性工时、在家办公和缩短工时制度列为兼顾工作与家庭的措施 | [有価証券報告書 p.13](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |
| 招聘方针 | 文件称通过"多国籍な採用"（多国籍招聘）来降低人才获取风险 | [有価証券報告書 p.16](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-07-29）：日文和英文公司网站、服务页与产品子域名；新闻、博客和 IR 索引；当前 Jobcan 招聘和具名第三方招聘网站；以 NETSTARS、ネットスターズ、StarPay 和主要产品名进行的日英文检索；常见文档、API 和状态页位置；按组织名、公司名和域名进行的 GitHub 检索；有价证券报告与认证披露。

- **没有独立的技术博客。** [公司博客](https://www.netstars.co.jp/blog/)以产品、合作方和市场内容为主；有两篇描述了架构（[高可用性，2024-06-04](https://www.netstars.co.jp/blog/7115/)；[AI 扫码，2024-05-01](https://www.netstars.co.jp/blog/7067/)），此后到 2026-07 为止的目录中没有再出现架构类文章。未找到公开的开源仓库或工程技术大会演讲。
- **未找到 StarPay 的公开开发者文档或 API 参考**；对接规格似乎是在合同框架下提供给 POS 和电商厂商的。
- **StarPay 与 StarPay-DX 均无公开价目表**。仅 Stablecoin Pay 的费率（0.98%）是公开的。
- **公司自有招聘页面除上述年薪区间外没有薪资带**；母公司平均年薪 693 万日元是唯一的全公司口径薪酬数字，且未按职能拆分。
- **没有状态页（status page）或公开的 SLA 文件**；99.9% 稼动率只出现在 [StarPay 站点](https://starpay.netstars.co.jp/)的营销文案中。
- **离职率 / 人员流动未公开**，法定文件中也没有留存率数字。
- **未在任何查阅到的资料中出现 ISO 27001 或 SOC 2**；列出的认证是 PCI DSS 4.0.1 和 Privacy Mark。
- **截至 2026-07-29，公司自有招聘页面上没有软件工程师岗位**；现存开发岗信息都在第三方网站上（无日期，访问于 2026-07-29）。
- 公司声称持有的二维码支付系统专利未标明专利号。

### 不同来源之间的不一致

- **FY2025 的 GPV 增速。** [FY2025 決算短信（2026-02-12）](https://ssl4.eir-parts.net/doc/5590/tdnet/2757309/00.pdf) 写的是 GPV 2 兆 1,228 亿日元"前年同期比+136.2%"；[有価証券報告書（2026-03-25）p.18](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) 和[決算説明資料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/198214/00.pdf) 对同一个 2 兆 1,228 亿日元写的是"+33.2%"。同一份法定文件给出的上年数字为 1 兆 5,942 亿日元。
- **2025-12-31 的员工数。** [有価証券報告書 p.10](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) 为合并 221 人；[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) 和[数字信息图页面](https://www.netstars.co.jp/infographics/) 为合并 **226 人**，且标注的基准日相同。[公司页面](https://www.netstars.co.jp/about) 给出的是 2026-03-31 的 224 人。
- **70 万账户是何时达成的。** [有価証券報告書 p.6](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) 写 2025-12-31 时约 70 万账户；[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) 的沿革页把"超过 60 万"放在 2025 年、"超过 70 万"放在 2026 年。
- **资金移动业登记日期。** [公司沿革页](https://www.netstars.co.jp/about) 写 2025 年 3 月（資金移動業者2種登録）；[有価証券報告書 p.5](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) 写 2025 年 5 月（第二種資金移動業登録完了）。
- **可靠性数字口径不同。** 99.9% 是营销页上的稼动保证（[StarPay 站点](https://starpay.netstars.co.jp/)）；99.999% 是 2025 年 1–12 月、剔除第三方原因错误后的支付成功率（[FY2026 Q1 決算説明資料](https://ssl4.eir-parts.net/doc/5590/tdnet/2811540/00.pdf)）；99.99% 是 2023 全年的可用率（[博客，2024-06-04](https://www.netstars.co.jp/blog/7115/)）。三者并非同一指标，且没有公开统一的定义。
- **同业对比数字在两版材料间发生变化。** PSP 对比中"海外 B 公司"的毛利率，在 [2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) 中为 37.1%，在 [FY2026 Q1 決算説明資料](https://ssl4.eir-parts.net/doc/5590/tdnet/2811540/00.pdf) 中为 43.1%，后者的脚注称原因是分部口径变更。两份材料都未披露对比公司的名称。

### 其他

- **收入集中于两家交易对手。** PayPay 与 NTT docomo 合计占 FY2025 营收的 43.4%、FY2024 营收的 45.1%（[有価証券報告書 p.19](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）；法定文件另将"对二维码支付事业者的依赖"单列为风险（可能性低，影响度大）（[p.15](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。
- **公司自己把所处市场描述为正在成熟。** FY2025 法定文件中的竞争风险写道，二维码支付市场"正在向成熟阶段转移"，靠服务内容或费率做差异化比以往更难（[p.14](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）—— 同样的表述也出现在 [2026 年 3 月成长可能性披露文件](https://ssl4.eir-parts.net/doc/5590/tdnet/2783892/00.pdf)中。
- **2026 年出现了一批集中的 Web3 公告。** 2026 年 4 月至 7 月间，公司先后发布了 StarPay-X 构想、Circle Gateway 开发，以及与 Aptos、Bitget Wallet、AllScale、Startale Group、Canton Foundation 的基本协议，随后于 2026-07-13 推出 Stablecoin Pay。FY2026 Q1 的 Q&A 称当时合作方为 7 家，预计增至 10 家左右（[Q&A](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/204228/00.pdf)）。
- **DX 业务在收缩，支付业务在增长。** DX/小程序营收从 FY2024 的 3.60 亿日元降至 FY2025 的 3.17 亿日元，低于计划 40.2%；同期支付相关营收增长 30.0% 并超出计划；FY2026 指引又把 DX 放回 4.10 亿日元（[2026 年 3 月说明资料](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf)）。
- **公司此前有终止业务线的记录。** 2010 年开始的国际通信与国际短信业务已于 2023 年 4 月终止；2011 年与腾讯、KDDI 共同发布的 Mobile QQ 日本版在沿革中标注为已终止（[有価証券報告書 p.5](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf)）。
- **公开发布的材料范围**：每季度的决算说明资料、自 FY2023 Q3 起每季度一份的主要 Q&A 文档、东证 Growth 上市公司必须提交的年度成长可能性披露文件、每年约两次的个人投资者说明资料，以及委托撰写的分析师报告。成长可能性披露文件的下次更新，公司标注为 FY2027 决算发表后的 3 月（[成长可能性披露文件](https://ssl4.eir-parts.net/doc/5590/tdnet/2783892/00.pdf)）。这些材料均无英文版。
- **英文内容有限。** [英文站点](https://www.netstars.co.jp/en/) 有 About、News、Services、IR、Careers 和 Contact；StarPay、StarPay-mini、StarPay-Order 和 KubeStar 的产品页仅有日文，查阅到的全部 IR 文件也都只有日文。

---

## 资料来源

**官方**

- [官网](https://www.netstars.co.jp/) · [英文站](https://www.netstars.co.jp/en/)
- [企业信息 —— 代表者致辞、役员、沿革、公司概要](https://www.netstars.co.jp/about)
- [数字看 NETSTARS（信息图）](https://www.netstars.co.jp/infographics/)
- [业务介绍索引](https://www.netstars.co.jp/servicelist/)
  - [StarPay](https://starpay.netstars.co.jp/) · [FAQ](https://starpay.netstars.co.jp/faq/) · [数字商品券](https://starpay.netstars.co.jp/house-coin/)
  - [StarPay-DX](https://www.netstars.co.jp/starpay-dx/) · [Regi-less](https://regi-less.jp/) · [StarPay-mini](https://starpay-mini.netstars.co.jp/) · [StarPay-Robot](https://starpay-robot.com/)
  - [StarPay-X](https://www.netstars.co.jp/starpayX/) · [KubeStar](https://www.netstars.co.jp/kubestar/) · [区域积分服务](https://www.netstars.co.jp/areapoint_service/)
- [新闻与通知索引](https://www.netstars.co.jp/topics/) · [博客](https://www.netstars.co.jp/blog/)
- [IR](https://www.netstars.co.jp/ir/) · [IR 新闻](https://www.netstars.co.jp/ir/news/) · [決算短信](https://www.netstars.co.jp/ir/library/result/) · [有価証券報告書](https://www.netstars.co.jp/ir/library/securities/) · [決算説明資料](https://www.netstars.co.jp/ir/library/presentation/) · [其他 IR 资料](https://www.netstars.co.jp/ir/library/material/)
- [招聘（Jobcan）](https://recruit.jobcan.jp/netstars/list)

**法定文件与 IR 资料（日文）**

- [FY2025 有価証券報告書 — 2026-03-25](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100XTGZ/00.pdf) · [FY2024 — 2025-03-28](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100VHQQ/00.pdf) · [FY2023 — 2024-03-29](https://ssl4.eir-parts.net/doc/5590/yuho_pdf/S100T640/00.pdf)
- [FY2025 決算短信 — 2026-02-12](https://ssl4.eir-parts.net/doc/5590/tdnet/2757309/00.pdf) · [FY2025 決算説明資料 — 2026-02-12](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/198214/00.pdf) · [FY2025 主要Q&A — 2026-02-20](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/199265/00.pdf)
- [FY2026 Q1 決算短信 — 2026-05-14](https://ssl4.eir-parts.net/doc/5590/tdnet/2811008/00.pdf) · [FY2026 Q1 決算説明資料 — 2026-05-14](https://ssl4.eir-parts.net/doc/5590/tdnet/2811540/00.pdf) · [FY2026 Q1 主要Q&A — 2026-05-19](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym/204228/00.pdf)
- [事業計画及び成長可能性に関する事項 — 2026-03-31](https://ssl4.eir-parts.net/doc/5590/tdnet/2783892/00.pdf) · [2025 年版 — 2025-02-28](https://ssl4.eir-parts.net/doc/5590/tdnet/2575006/00.pdf) · [2024 年版 — 2024-02-29](https://ssl4.eir-parts.net/doc/5590/tdnet/2404644/00.pdf) · [2023 年版（上市时）— 2023-09-26](https://ssl4.eir-parts.net/doc/5590/tdnet/2339490/00.pdf)
- [个人投资者说明资料 — 2026-03-26](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/200899/00.pdf) · [2025-09-29](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/187829/00.pdf) · [2025-06-16](https://ssl4.eir-parts.net/doc/5590/ir_material_for_fiscal_ym1/181444/00.pdf)
- [设立子公司 StarPay-Entertainment — 2025-12-19](https://ssl4.eir-parts.net/doc/5590/tdnet/2733249/00.pdf)
- [北京分公司关闭 — 2025-08-25](https://ssl4.eir-parts.net/doc/5590/tdnet/2679923/00.pdf)
- [与 Finext Limited 设立合资公司 — 2024-08-14](https://ssl4.eir-parts.net/doc/5590/tdnet/2492220/00.pdf)
- [员工持股会奖励金上调 — 2026-02-24](https://ssl4.eir-parts.net/doc/5590/tdnet/2766521/00.pdf)
- [透支额度合同 — 2026-04-30](https://ssl4.eir-parts.net/doc/5590/tdnet/2797657/00.pdf)

**新闻稿（日文）**

- [Stablecoin Pay 正式启动 — 2026-07-13](https://www.netstars.co.jp/news/9450/)
- [与 Canton Foundation 基本协议 — 2026-07-07](https://www.netstars.co.jp/news/9397/)
- [与 Startale Group 基本协议 — 2026-06-15](https://www.netstars.co.jp/news/9318/)
- [与 AllScale 基本协议 — 2026-06-08](https://www.netstars.co.jp/news/9290/)
- [与 Bitget Wallet 基本协议 — 2026-06-04](https://www.netstars.co.jp/news/9260/)
- [与 Aptos 基本协议 — 2026-05-08](https://www.netstars.co.jp/news/9209/)
- [永旺 Delight Connect 的 AI 呼叫解决方案 — 2026-04-15](https://www.netstars.co.jp/news/9172/)
- [Circle Gateway 多链开发 — 2026-04-13](https://www.netstars.co.jp/news/9148/)
- [StarPay-X 构想发布 — 2026-04-08](https://www.netstars.co.jp/news/9129/)
- [第二轮 USDC 门店实证 — 2026-04-02](https://www.netstars.co.jp/news/9122/)
- [KKR、SIG、LUN Partners 共 66 亿日元融资 — 2021-04-14](https://www.netstars.co.jp/news/3486/) · [PR TIMES](https://prtimes.jp/main/html/rd/p/000000023.000019526.html)
- [追加融资，2020 年 5–9 月约 30 亿日元 — 2020-09-30](https://www.netstars.co.jp/notification/3000/)
- [伊藤忠商事资本合作 — 2019-11-21](https://www.netstars.co.jp/notification/2169/) · [SCSK / T-Gaia 资本合作 — 2019-11-21](https://www.netstars.co.jp/notification/2171/)
- [NTT 东日本集团 / 伊藤忠 Techno-Solutions 资本合作 — 无日期；访问于 2026-07-29；约 2018 年初](https://www.netstars.co.jp/news/737/)

**含技术内容的博客（日文）**

- [支撑高可用性的机制 — 2024-06-04](https://www.netstars.co.jp/blog/7115/)
- [用 AI 增强 StarPay 应用的扫码功能 — 2024-05-01](https://www.netstars.co.jp/blog/7067/)
- [二维码支付的 MPM 与 CPM 有何不同 — 2026-07-15](https://www.netstars.co.jp/blog/9463/)
- [StarPay 介绍 — 2023-03-30](https://www.netstars.co.jp/blog/5092/)

**第三方报道与资料库**

- [伊藤忠商事 —— 资本合作新闻稿，2019-11-21（日文）](https://www.itochu.co.jp/ja/news/press/2019/191121.html)
- [SCSK —— 资本合作新闻稿，2019-11-21（日文）](https://www.scsk.jp/news/2019/press/product/20191121_2.html)
- [日经 —— "ベンチャー魂のひと" CEO 专访（日文）](https://www.nikkei.com/article/DGXZQOUB176YA0X10C25A2000000/)
- [周刊经济学人 —— 主编对话 CEO（日文）](https://www.weekly-economist.com/interview/ri_tsuyoshi/)
- [Payment Navi —— 报道索引（日文）](https://paymentnavi.com/paymentnews/171059.html)
- [IPO Kiso —— IPO 详情（日文）](https://www.ipokiso.com/company/2023/netstars.html)
- [IR Bank —— 披露索引（日文）](https://irbank.net/5590/ir)
- [Green —— 招聘信息（日文）](https://www.green-japan.com/company/6214)
- [en-gage —— 招聘页面（日文）](https://en-gage.net/netstars_saiyo/)
- [INITIAL / Speeda 创业公司档案（日文）](https://initial.inc/companies/A-30239)
- [STARTUP DB 档案（日文）](https://startup-db.com/companies/E0zvGDyUOR0pNnMa)
- [雅虎财经 —— 企业信息（日文）](https://finance.yahoo.co.jp/quote/5590.T/profile)
