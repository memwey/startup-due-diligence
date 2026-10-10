# Couger

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Couger（クーガー株式会社 / Couger Inc.）是一家成立于 2006 年 12 月、位于东京涩谷区神宫前的公司（[PR TIMES 公司资料](https://prtimes.jp/main/html/rd/p/000000050.000033615.html)，2026-10-09；[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 27 页，2026-10-07）。公司开发 **LUDENS**，自称为“人型AIプラットフォーム”（人型 AI 平台），以及运行在其上的“虚拟人代理”（VHA）**Rachel（レイチェル）**（[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 7–8 页；[PR TIMES，2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)）。全家（FamilyMart）在门店平板上运行 Rachel 和另一个角色 Akira（アキラ），用于支持加盟店店长（[FamilyMart，2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)）。在这次部署之前，公司的公开记录涵盖网络游戏开发、AI 与机器人受托开发，以及基于以太坊的项目（GeneFlow、zkCREAM）（[Green 访谈](https://www.green-japan.com/interview/5263)；[SBBIT，2018-06-11](https://www.sbbit.jp/article/cont1/34986)；[PR TIMES 公司页](https://prtimes.jp/main/html/searchrlp/company_id/33615)）。自 2025 年 7 月起，公司的大部分新闻稿都是在宣布 **Sphear** 的活动；Sphear 是公司运营的“宇宙 × AI”社区（[PR TIMES 公司页](https://prtimes.jp/main/html/searchrlp/company_id/33615)）。

- **部署规模：** 截至 2024 年 7 月底约 7,000 家全家门店（[FamilyMart，2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html)）。公司介绍资料写“7,000店舗以上”（[公司介绍资料，2026-10-07](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)）。一家行业媒体报道有 13,000 家门店在使用该助手（[激流オンライン，2026-01-30](https://gekiryu-online.jp/2026/01/227822)）。见`不同来源之间的不一致`。
- **融资：** 唯一公开的外部股权是与伊藤忠商事的资本业务合作，于 2020-01-20 达成基本合意，未公布金额（[伊藤忠商事](https://www.itochu.co.jp/ja/news/press/2020/200120.html)）。根据[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)（2026-10-07），资本金为“282百万円”（2.82 亿日元）。
- **团队：** 截至 2026-03-31 共 41 人（正式员工 39 人、兼职 2 人），另有约 10 名外包人员。工程师占岗位的 49%（[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)）。
- **工程：** 当前职位列出 Python、TypeScript/React/Next.js，以及 AWS、Google Cloud 和 Azure（[Senior Software Engineer 职位](https://open.talentio.com/r/1/c/couger/pages/119821)；datePosted 2026-02-05）。一则 2024 年的职位列出 Unity 客户端（[paiza](https://paiza.jp/career/job_offers/28362)；更新于 2024-12-20）。行为脚本以 JavaScript 运行（“InteractiveCode”）。当前职位要求商务级或母语级日语。2022 年面向 ML/AI 团队的英文职位要求英语（[Notion 招聘页](https://couger.notion.site/Careers-Couger-Inc-35ada7ab0ed34c1baff8dac5f86b5636)）。工作方式为混合办公，且“フルリモートは不可”（不允许完全远程）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前公开品牌 | Couger / クーガー。公司介绍资料封面写“Virtual Human Agent × XAI” | [公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 1 页（2026-10-07） |
| 法定名称 | クーガー株式会社（假名读音 クーガー）。公司介绍资料使用的英文名为“Couger Inc.”；GitHub 组织使用“Couger, Inc.” | [国税厅法人番号公表网站](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073)、[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 27 页、[GitHub API](https://api.github.com/orgs/couger-inc) |
| 法人番号 | 7010701025073。指定于 2015-10-05（平成27年10月5日）；最终更新 2018-04-13（平成30年4月13日）。变更履历仅显示最初的“新規”一条 | [国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073)；读取于 2026-10-11 |
| 登记地址 | 東京都渋谷区神宮前６丁目１９番１６号 | [国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073) |
| 办公室 | 〒150-0001 東京都渋谷区神宮前6-19-16 越一ビル201 | [公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 27 页、[PR TIMES 公司资料](https://prtimes.jp/main/html/rd/p/000000050.000033615.html) |
| 成立 | 2006 年 12 月；公司介绍资料写“2006年12月19日” | [PR TIMES 公司资料](https://prtimes.jp/main/html/rd/p/000000050.000033615.html)、[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 27 页 |
| 所列高管 | 代表取締役 CEO 石井 敦（Atsushi Ishii）；取締役 CTO 高橋 光 | [PR TIMES，2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)（CEO）；[Green 访谈](https://www.green-japan.com/interview/5263)照片说明“取締役 CTO 高橋 光氏”（无日期，访问于 2026-10-11） |
| 资本金 | “282百万円”。PR TIMES 公司资料栏显示为“-” | [公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 27 页（2026-10-07）、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000050.000033615.html) |
| 员工人数 | 41 人（正社員 39、アルバイト 2），另有“業務委託 10名程度”，截至 2026-03-31 | [公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 18、27 页 |
| 工作语言 | 未找到全公司层面的说明。见`工作条件` | — |
| 客户 | 全家（Rachel/Akira）。2024-08-01 起在 Autobacs Seven 集团开展试用。介绍资料列出 14 家“取引先企業・機関” | [FamilyMart](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)、[Ridgelinez](https://www.ridgelinez.com/news/news_20240801/)、[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 16 页 |
| 累计融资 | 未披露。2020-01-20 与伊藤忠商事资本业务合作 | [伊藤忠商事](https://www.itochu.co.jp/ja/news/press/2020/200120.html) |
| 曾用产品名 | 2018 至 2020 年的新闻稿用“コネクトーム / Connectome”指代现称 LUDENS 的技术和代理 | [PR TIMES 2018-04-26](https://prtimes.jp/main/html/rd/p/000000002.000033615.html)、[PR TIMES 2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)、[伊藤忠商事 2020-01-20](https://www.itochu.co.jp/ja/news/press/2020/200120.html) |
| GitHub | `couger-inc`（“Couger, Inc.”；已认证；创建于 2018-01-19；10 个公开仓库）。`zkcream`（已认证；创建于 2020-10-06；6 个仓库） | [GitHub API](https://api.github.com/orgs/couger-inc)、[GitHub — zkcream](https://github.com/zkcream)；读取于 2026-10-11 |

**公司运营的相关社区与网站。** [Virtual Human Lab](https://virtualhumanlab.io/) 自称公开了 Couger 关于虚拟人代理的部分研究活动（“クーガーによるバーチャルヒューマンエージェントの研究活動を一部公開”；访问于 2026-10-11），其起始时间在不同来源中不一致，见`不同来源之间的不一致`。[Sphear](https://sphear.to/) 是一个“宇宙 × AI”社区，首场活动于 2025-08-01 举办（[PR TIMES，2025-07-03](https://prtimes.jp/main/html/rd/p/000000036.000033615.html)）；第 13 场活动定于 2026-11-06（[PR TIMES，2026-10-09](https://prtimes.jp/main/html/rd/p/000000050.000033615.html)）。Enterprise Ethereum Alliance 于 2017-05-22 公布的 86 家新成员中列有 Couger（[EEA，2017-05-22](https://entethalliance.org/enterprise-ethereum-alliance-expands-dramatically-announcing-86-new-members/)）。

**公司公布的计算机视觉竞赛成绩（PR TIMES）：**
- Facebook Research OpenEDS 眼动追踪挑战赛第 3 名（[2019-10-16](https://prtimes.jp/main/html/rd/p/000000011.000033615.html)）。
- CVPR 2020 热成像超分辨率挑战赛第 2 名（[2020-06-29](https://prtimes.jp/main/html/rd/p/000000022.000033615.html)）。
- ICCV 2021 挑战赛第 3 名，SkeletonNetV2 获 Best Challenge Paper Award（[2021-11-29](https://prtimes.jp/main/html/rd/p/000000026.000033615.html)）。
- ECCV 2022 Instagram Filter Removal Challenge，114 名参赛者中排第 9（[2023-01-23](https://prtimes.jp/main/html/rd/p/000000030.000033615.html)）。
- CVPR 2024 MIPI 挑战赛第 7 名（[2024-07-23](https://prtimes.jp/main/html/rd/p/000000032.000033615.html)）。
- 一篇热成像超分辨率论文被 CVPR 2025 workshop 接收（[2025-06-17](https://prtimes.jp/main/html/rd/p/000000035.000033615.html)）。
- IEEE IJCB 2025 上的巩膜分割基准竞赛（SSBC 2025）合成数据组第 1 名（[2025-07-10](https://prtimes.jp/main/html/rd/p/000000037.000033615.html)）。

**会议赞助（主办方页面）：**
- Product History Conference 2024（2024-11-30），Silver；CEO 发表了关于 Rachel 导入 7,000 家便利店过程的演讲（[YOUTRUST 活动页](https://lp-prohis.youtrust.jp/2024/)；访问于 2026-10-11）。
- JSAI2026，Platinum（[JSAI2026 赞助商列表](https://www.ai-gakkai.or.jp/jsai2026/sponsor/)；访问于 2026-10-11）。

---

## 产品

公司的使命是“人に寄り添い、成長させるAI”（贴近人、帮助人成长的 AI）（[公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 2 页）。介绍资料封面写“Virtual Human Agent × XAI”。

### 产品阵容

| 产品 | 公司的描述 | 状态依据 | 来源 |
|---|---|---|---|
| LUDENS（ルーデンス） | 人型AIプラットフォーム。介绍资料列出 VHA 界面、LudensCore（整体控制）、“知覚エンジン”（感知引擎）和“理解・行動促進エンジン”（理解与行为促进引擎）。一篇 2025 年的演讲报道提到 VisualCortex（图像识别）、LanguageCortex（语言）以及基于 JavaScript 的脚本层 InteractiveCode。职位中另有“Insight”（意义理解与检索）和“Ludens Analytics”（数据分析平台） | 现行；出现在当前工程职位中 | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 7 页、[Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference)、[职位](https://open.talentio.com/r/1/c/couger/pages/119821) |
| Rachel（レイチェル）/ Akira（アキラ） | 运行在 LUDENS 上的虚拟人代理。在全家作为平板上的店长助手 | 现行；全家部署 | [PR TIMES，2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)、[FamilyMart](https://www.family.co.jp/company/news_releases/2022/20221128_02.html) |
| VisualCortex | LUDENS 中的图像识别 AI；其处理已从服务器迁到现场 PC | 出现在一则当前职位和 2025 年的演讲报道中 | [Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference)、[职位](https://open.talentio.com/r/1/c/couger/pages/119821) |
| GeneFlow | 将 AI 训练数据、算法、模型和执行履历记录在区块链上；2018 年 α 版，2020-04-14 有限 β 版 | 在 PR TIMES 系列新闻稿中未找到 2020 年之后的发布 | [PR TIMES，2018-06-29](https://prtimes.jp/main/html/rd/p/000000005.000033615.html)、[PR TIMES，2020-04-14](https://prtimes.jp/main/html/rd/p/000000020.000033615.html) |
| zkCREAM | 基于 zk-SNARK 的匿名投票协议，以开源方式开发 | 主仓库已归档；最后推送于 2022-02 | [PR TIMES，2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html)、[GitHub — cream](https://github.com/couger-inc/cream) |

新闻稿中提到的早期产品和项目包括：
- 一款专门模拟行人动作的 AI 学习模拟器，作为自动驾驶的学习环境提供给本田技术研究所（[2019-09-18 的 PR TIMES 新闻稿](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)提及，未注明时间）；介绍资料的时间线在“〜2019”下列出“本田技術研究所 ロボット共同研究開発”（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 11 页）；
- 用于构建虚拟人的 JavaScript“Connectome SDK”，发布于 2019-09-18（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)）；
- 与アクト共同开发的区块链选举系统“OMEGA”（[PR TIMES，2020-01-27](https://prtimes.jp/main/html/rd/p/000000018.000033615.html)）。

**Rachel 在全家的功能。** 全家的新闻稿列出（[2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)）：
- 根据门店状况和店长特点提供信息与沟通，促使店长采取行动；
- 基于销售额、客数等大规模数据的参考信息；
- 新商品、促销和每周信息，以及未完成事项的确认；
- 与督导（SV）门店指导联动。

自 2024-07 起加入生成式 AI，可语音检索操作手册（收银操作、店员培训、紧急应对）（[FamilyMart，2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html)）。公司介绍资料描述了摘要、任务优先级、说明为何要做某项任务、反馈、共情和提醒（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 12 页）。

### 商业化

未找到 LUDENS 或 Rachel 的公开价目表。职位将客户项目描述为五个阶段：①提案、②業務分析、③開発、④システム導入、⑤導入後の伴走。技术客户经理、项目经理和 AI 导入顾问各自负责不同阶段（[PjM 职位](https://open.talentio.com/r/1/c/couger/pages/84099)、[TAM 职位](https://open.talentio.com/r/1/c/couger/pages/84100)）。一位 TAM 描述其工作比例为“TAM：営業＝7:3”（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 15 页）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2021-03-12 | 38 家全家门店，此前“昨年から都内を中心に”（自上一年起以东京为中心）试验性导入；日销售额比条件相近的其他门店“平均３―４％”增长；计划在 2021 财年内扩大到数百家以上。日刊工业新闻将其作为伊藤忠商事的举措报道 | [Newswitch（日刊工业新闻），2021-03-14](https://newswitch.jp/p/26324) |
| 2022-11-28 | 计划在 2023 财年末前覆盖约 5,000 家门店 | [FamilyMart](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)、[PR TIMES，2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html) |
| 2023-01 | 店长业务支援开始推广 | [PR TIMES，2024-08-07](https://prtimes.jp/main/html/rd/p/000000033.000033615.html) |
| 2024-07（月底） | 约 7,000 家门店 | [FamilyMart，2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) |
| 2026-01-30 | “足元すでに1万3000店が活用しており、来期中には全店に行き渡る見通しだ”（已有 13,000 家门店在用，预计下一财年内覆盖全部门店），系该媒体的报道 | [激流オンライン](https://gekiryu-online.jp/2026/01/227822) |
| 2026-10-07 | “全国7,000店舗以上へ提供中”；先行导入门店销售额平均提升 2%，预期 SV 工作量减少约 30% | [公司介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 12 页 |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2018-04-26](https://prtimes.jp/main/html/rd/p/000000002.000033615.html) | KDDI | 为“バーチャルキャラクター × xR”项目提供技术支持 |
| [2019-06-26](https://prtimes.jp/main/html/rd/p/000000009.000033615.html) | 電通国際情報サービス、京王電鉄 | 在トリエ京王調布的数字标牌上开展 VHA 实证实验 |
| [2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html) | 本田技術研究所 | 提供行人动作 AI 学习模拟器，未注明时间 |
| [2020-01-20](https://www.itochu.co.jp/ja/news/press/2020/200120.html) | 伊藤忠商事 | 资本业务合作（基本合意） |
| [2020-01-27](https://prtimes.jp/main/html/rd/p/000000018.000033615.html) | アクト | 共同开发区块链选举系统 OMEGA |
| [2021-02-10](https://prtimes.jp/main/html/rd/p/000000023.000033615.html) | Ethereum Foundation | 2020-12 签署合作；ETHTerakoya 社区，在以太坊基金会赞助下启动（[2020-05-25](https://prtimes.jp/main/html/rd/p/000000021.000033615.html)） |
| [2022-01-31](https://prtimes.jp/main/html/rd/p/000000027.000033615.html) | 早稲田リーガルコモンズ法律事務所 | zkCREAM 验证 |
| [2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html) | ファミリーマート | Rachel/Akira，2023 财年末前约 5,000 家门店 |
| [2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html) | ファミリーマート | CEO 自 2023-10-01 起出任全家“生成AIプロジェクト”顾问 |
| [2024-08-01](https://www.ridgelinez.com/news/news_20240801/) | オートバックスデジタルイニシアチブ、Ridgelinez | 在 Autobacs Seven 集团数字实验室试用 Rachel 接待顾客 |
| [2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) | ファミリーマート | 加入生成式 AI（自 2024-07 起）；约 7,000 家门店 |

公司介绍资料的客户名单（第 16 页）还列出 NHN JAPAN、電通総研、ソニー・インタラクティブエンタテインメント、NEDO、スクウェア・エニックス、産業技術総合研究所、電気通信大学、シンガポール国立大学和早稲田大学。数据分析师职位称 Rachel 正在“アパレル・小売など複数の大手企業”（多家大型服装和零售企业）导入，但未给出名称（[职位](https://open.talentio.com/r/1/c/couger/pages/122132)；datePosted 2026-04-09）。

### 公开计划

- “将来的には、サードパーティ企業がLUDENSを使ってバーチャルヒューマンエージェントを提供できることを想定している”（第三方企业在 LUDENS 上提供 VHA）（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 8 页）。
- 近期重点是门店和现场的理解促进、行为改变与习惯养成，目标是“導入先を一気に拡大”（迅速扩大客户）（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 14 页）。
- 全家表示，计划将来把基于摄像头的“AI売場スコアリング”试点与 Rachel 及其 AI 订货系统联动（[FamilyMart，2026-01-13](https://www.family.co.jp/company/news_releases/2026/20260113_02.html)）。
- Sphear 的公开目标是“人類の宇宙移住にAIの力で貢献すること”（以 AI 助力人类宇宙移居）（[PR TIMES，2026-01-08](https://prtimes.jp/main/html/rd/p/000000043.000033615.html)）。

---

## 创始人

公司介绍资料在“大規模システムと最先端AIを極めた創業者”标题下列出 **石井 敦（Atsushi Ishii，CEO）** 和 **高橋 光（CTO）**（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 5 页）。WIRED 写道石井“共同創業し”（共同创立）该公司（[WIRED，2022-05-16](https://wired.jp/article/the-next-innovators-3-atsushi-ishii/)）。

**石井 敦——代表取締役 CEO**
- 学习机械工程。之后从事发电厂控制系统软件工作，加入日本 IBM（藤泽），再转到 Lycos Japan 开发大规模搜索引擎。乐天收购 Lycos Japan 后，他继续在乐天做搜索，随后在移动视频公司セーバー负责技术（[Green 访谈](https://www.green-japan.com/interview/5263)；无日期，访问于 2026-10-11）。
- 他称セーバー被出售后，自己差一点加入 SpaceX。他最终为一个与国内大企业合作的大规模搜索引擎项目注册了 Couger，但该项目在“クーガー設立の初日に”（公司成立当天）被取消。公司约从 2014 年起转向 AI 与机器人领域（[SBBIT，2018-06-11](https://www.sbbit.jp/article/cont1/34986)）。成立后，公司从事大规模系统和网络游戏的设计开发，并与大学开展共同研究（[Green 访谈](https://www.green-japan.com/interview/5263)）。
- 自 2009 年起任硅谷 LivingImage 的 CTO 两年；自 2010 年起任 dango 的 CTO 四年，参与游戏『マジモン』的开发（[Green 访谈](https://www.green-japan.com/interview/5263)）。
- 斯坦福大学 2018 年 AI 特别讲座讲师；电气通信大学前客座研究员（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 5 页；[PR TIMES，2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html)）。
- 2022-04-07 出任 Enterprise Ethereum Alliance 日本支部代表，被描述为全球 13 名核心成员之一，接替 Couger 的石黒 一明（[PR TIMES，2022-04-07](https://prtimes.jp/main/html/rd/p/000000028.000033615.html)）。
- 自 2023-10-01 起任全家生成式 AI 项目顾问（[PR TIMES，2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html)）。

**高橋 光——取締役 CTO。** 曾在一家大型独立系统集成商工作，2001 年加入 Lycos Japan，负责面向大规模用户的邮件和社区系统设计开发，之后在乐天和 Infoseek 继续这类工作。他擅长处理“デイリーで億単位のアクセス”（每天数亿次访问）的后端，以及网络游戏后端（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 5 页）。

**公司公布的其他人员：**
- チーフアーキテクト土田 悠貴于 2025-11-20 与 CEO 一同在アーキテクチャConference 2025 演讲（[Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference)）。
- [招聘网站成员页](https://careers.couger.co.jp/member)（无日期，访问于 2026-10-11）列出：
  - 中村 竜晴，事業統括ディレクター（欧洲 VR 初创公司、迪士尼日本、咨询）；
  - 五十嵐 智哉，チーフアーキテクト（PlayStation 赛车和格斗游戏）；
  - 平崎 葵，全栈 Web 团队工程经理；
  - 技术客户管理、产品管理、NLP 与检索、DevOps、高级 QA、技术咨询、公关和招聘等岗位。
- `TomoyaIgarashi`（公司栏为“Couger Inc.”）是 `couger-inc` GitHub 组织唯一的公开成员（[GitHub API](https://api.github.com/orgs/couger-inc/public_members)；读取于 2026-10-11）。

**顾问。** 山川 宏（全脑架构倡议组织）出任顾问，于 2019-09-18 公布（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)）。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2020-01-20 | 資本業務提携（资本业务合作；“基本合意”） | 未披露 | 伊藤忠商事 | 未披露 | [伊藤忠商事](https://www.itochu.co.jp/ja/news/press/2020/200120.html)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000017.000033615.html) |
| 2021-07-02 | “開発助成金採択”（开发资助；PR TIMES，2021-07-02）/“公式プログラムに選ばれる”（入选官方项目；PR TIMES，2022-04-07）：以太坊基金会对 zkCREAM 的资助；非股权 | 未披露 | Ethereum Foundation | — | [PR TIMES，2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html)、[PR TIMES，2022-04-07](https://prtimes.jp/main/html/rd/p/000000028.000033615.html) |

表格以外的事实：
- 伊藤忠的新闻稿称，除出资外，“伊藤忠グループのネットワークを活かし、同社の国内外への展開を支援いたします”（利用伊藤忠集团网络支持其国内外拓展），未给出持股比例或金额（[伊藤忠商事，2020-01-20](https://www.itochu.co.jp/ja/news/press/2020/200120.html)）。Couger 关于全家的新闻稿称伊藤忠为“資本業務提携先”（资本业务合作方），并称 Rachel 是与伊藤忠和全家合作开发的（[PR TIMES，2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html)）。
- 2021 年 zkCREAM 新闻稿称，已通过 Gitcoin 募得“100万円を超える支援金”（超过 100 万日元的捐助），主要来自海外（[PR TIMES，2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html)）。
- 在公司、投资方和新闻来源中均未找到其他股权轮次、投资者、估值或累计总额。2.82 亿日元资本金（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 27 页，2026-10-07）是公司公布的唯一资本数字。

---

## 工程

### 技术栈与平台

由文档或公开资产确认：
- **行为脚本：** InteractiveCode 是基于 JavaScript 的脚本层，承载具体业务流程和对话逻辑（[Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference)，关于 2025-11-20 的演讲；无日期，访问于 2026-10-11）。2019 年的 Connectome SDK 同样允许开发者用 JavaScript 编写虚拟人的行为，包括调用外部 API（[PR TIMES，2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html)）。
- **LLM：** 自 2024-07 起 Rachel/Akira 搭载生成式 AI（[FamilyMart](https://www.family.co.jp/company/news_releases/2024/20240802_01.html)）。介绍资料的架构图在感知引擎中列出“LLM”（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 7 页）。
- **区块链工作：**
  - GeneFlow 基于 Ethereum 和 Quorum，学习完成的模型和学习数据存放在“分散型ファイルシステム”（分布式文件系统）中（[PR TIMES，2018-06-29](https://prtimes.jp/main/html/rd/p/000000005.000033615.html)）。
  - zkCREAM 使用 TypeScript，包括 API 服务器、界面、Vue faucet 和基于 snarkjs 的可信设置 fork（[GitHub — zkcream](https://github.com/zkcream)、[GitHub — cream](https://github.com/couger-inc/cream)）。
- **Rust：** `couger-inc/rust-freetype` 和 `couger-inc/font-kit`，均创建于 2024-08-26，最新提交分别为 2023-07-19 和 2024-09-05。用途未说明（[GitHub — couger-inc](https://github.com/couger-inc)）。

根据当前招聘信息推断（招聘依据；不能证明已用于生产）：
- **语言：** Python 和 TypeScript/JavaScript 在各工程职位中反复出现。Go 出现在全栈职位的职责描述中（“GoやPythonによるAPIやバッチ処理”），也是加分项（[全栈职位](https://open.talentio.com/r/1/c/couger/pages/109446)；datePosted 2024-06-04）。
- **Web：** React、Next.js、Material UI、Tailwind CSS；GitHub、GitHub Actions；Jest、MSW、Cypress、Storybook；Confluence、Jira、Slack（[Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821)、[Product Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687)）。
- **云与平台：** Amazon Web Services、Google Cloud、Microsoft Azure、Firebase；Linux、Windows、Docker（[Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821)）。
- **机器学习：** PyTorch、Transformers、Rasa、Weights & Biases、Hugging Face、Kubernetes、Terraform（[Senior Software Engineer（Machine Learning），Green](https://www.green-japan.com/company/5263/job/301740)；无日期，访问于 2026-10-11）。
- **客户端应用：** Unity（C#），加分项为用 C++、Rust、Objective-C 或 Kotlin 开发原生插件；目标平台为 Windows、Mac、iOS 和 Android；使用 Xcode 和 Android Studio（[paiza](https://paiza.jp/career/job_offers/28362)；更新于 2024-12-20）。QA 职位将“Unity / Airtest”列为构建工具（[Senior QA](https://open.talentio.com/r/1/c/couger/pages/117722)）。
- **数据：** MySQL、Tableau、Power BI、Python、R（[Senior Data Analyst](https://open.talentio.com/r/1/c/couger/pages/122132)；datePosted 2026-04-09）。
- **早期：** 2022 年英文职位列出 Python、Linux、Docker、Jenkins、GitHub Actions 和 AWS（[Server Application Engineer](https://couger.notion.site/ad09a89b538849f585f410ce7ef4706f)；最后编辑于 2022-10-11）。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| LUDENS 客户端应用 | VHA 界面（语音、表情、动作、GUI、角色）、“インタラクションフレームワーク”，以及负责“インターフェースの全体制御”的 LudensCore | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 7 页 |
| LUDENS 云平台 | “理解・行動促進エンジン”（用户行为分析、用户特性分析、业务分析、规划、优先级、沟通）；“知覚エンジン”（自然语言、图像识别、LLM）；Web UI/API；连接外部数据的数据连接器 | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 7 页 |
| 引擎与脚本分离 | LudensCore 被描述为原生应用，提供 UI、通信、3D 渲染和脚本运行环境，不含具体用例逻辑。InteractiveCode 承载订货建议等流程。AI 生成的回复候选先经 InteractiveCode 按角色设定和场景处理后再输出 | [Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference) |
| 边缘与云端分工 | 由于传送视频导致响应“著しく遅く”（明显变慢），VisualCortex 的处理从服务器迁到现场 PC | [Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference) |
| 平台组件名称 | VisualCortex（图像识别）、LanguageCortex（自然语言）、Insight（意义理解与检索）、Ludens Analytics（数据分析） | [Senior Software Engineer 职位](https://open.talentio.com/r/1/c/couger/pages/119821) |
| 全家部署 | 每家门店的平板；销售额和客数数据；基于生成式 AI 的操作手册语音检索 | [FamilyMart 2022](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)、[FamilyMart 2024](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) |
| 运维 | 轮班 on-call，负责非工作时间和节假日的故障应对，并有 on-call 津贴 | [Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821)、[全栈](https://open.talentio.com/r/1/c/couger/pages/109446) |

**组织。** 介绍资料的组织图把 VHA、Fullstack-web（Frontend、Backend、DevOps）、Test Automation 和 Corporate IT 放在 CTO（技術統括）之下。产品管理、客户管理、设计和 QA 归属“プロダクト統括”。LudensCore、图像识别和自然语言/检索团队画在两者之间（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 19 页）。Senior Software Engineer 职位称，开发体制正从前后端分离的团队转为一体化的全栈 Web 团队（[职位](https://open.talentio.com/r/1/c/couger/pages/119821)）。

**研究成果。** `couger-inc/research` 仓库列出 2019 至 2023 年的论文，主题包括骨架提取、眼部区域分割、热成像超分辨率、Instagram 滤镜去除、深度引导重照明和基于意图的对话模型（[GitHub](https://github.com/couger-inc/research)；最后提交于 2024-07-01）。

### 招聘所需技术背景

依据 2026-10-11 [careers.couger.co.jp](https://careers.couger.co.jp/) 上列出的职位，以及 Green 和 paiza：
- **必需：**
  - 全栈 Web 的设计、开发和运维；
  - 系统架构、数据库和 Web API 设计；
  - AWS 等云基础设施的设计与构建；
  - 通过技术讨论和评审提升质量（[Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821)）；
  - 在云服务上构建 Web API 和批处理或流处理数据管道；
  - 基于 RDBMS、NoSQL 或 NewSQL 的后端（[全栈](https://open.talentio.com/r/1/c/couger/pages/109446)）；
  - 技术选型、架构以及跨团队技术决策（[Product Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687)）；
  - Unity 开发（[paiza](https://paiza.jp/career/job_offers/28362)）。
- **加分：**
  - 大规模、高可用系统；
  - 机器学习或 LLM 产品；
  - 事件驱动架构；
  - 搜索引擎或向量数据库；
  - 技术领导（[Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821)）；
  - Unity 原生插件、通过 API 与服务器通信、3D 模型与光照，以及个人发布过游戏（[paiza](https://paiza.jp/career/job_offers/28362)）。
- **ML 岗位职责：** 对话系统的机器学习模型；利用 LLM 和多模态模型的对话生成、意图理解与行动建议算法；训练管道、评估、监控和自动化测试。任职要求需登录后才能查看（[Green](https://www.green-japan.com/company/5263/job/301740)）。

### 行业领域

- **便利店运营。** 工作涉及店长业务、订货、卖场打造、督导（SV）门店指导，以及销售额和客数数据（[FamilyMart，2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html)）。零售知识列为加分项而非必需：AI 导入顾问为“小売業界に関する深い知識”（[职位](https://open.talentio.com/r/1/c/couger/pages/84428)），数据分析师为处理零售或流通现场数据的经验（[职位](https://open.talentio.com/r/1/c/couger/pages/122132)）。查阅到的工程职位均未将行业知识列为必需。
- **效果衡量。** 数据分析师岗位要求用回归分析、假设检验和因果推断量化 Rachel 对销售和运营的影响（[职位](https://open.talentio.com/r/1/c/couger/pages/122132)）。
- **游戏 AI。** 公司把游戏 AI 作为 Rachel 设计的基础，并称 Rachel 运行在“「現実世界」という究極のオープンワールド”（现实世界这一终极开放世界）中。一份 2025 年的资料讲解了 A*、NavMesh、GOAP、行为树和有限状态机（[Speaker Deck，2025-05-02](https://speakerdeck.com/couger/xian-shi-shi-jie-toiujiu-ji-noopunwarudogemuwoshi-xian-suruniha)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言（当前职位） | Product Tech Lead 和 Senior QA：商务级日语。全栈：“ビジネスレベル以上（日本語能力試験N1相当）”。Senior Data Analyst 和 InfoSec：母语级日语。Senior Software Engineer 职位没有语言要求一栏 | [Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687)、[全栈](https://open.talentio.com/r/1/c/couger/pages/109446)、[QA](https://open.talentio.com/r/1/c/couger/pages/117722)、[分析师](https://open.talentio.com/r/1/c/couger/pages/122132)、[InfoSec](https://open.talentio.com/r/1/c/couger/pages/112252) |
| 工作语言（2022 年英文职位） | Server Application Engineer：“Highly proficient in spoken and written English”。Engineering Manager（ML/AI）：商务级英语、基础日语，管理“diverse in experience and nationality”（经验和国籍多元）的团队 | [Server Application Engineer](https://couger.notion.site/ad09a89b538849f585f410ce7ef4706f)、[Engineering Manager](https://couger.notion.site/ec98d708d9e94523aa0161dc72b1cf6c)；最后编辑于 2022-10-11 |
| 地点 | 涩谷办公室，距涩谷站步行 5 分钟 | [招聘网站](https://careers.couger.co.jp/) |
| 远程 | 混合办公；“フルリモートは不可”（不允许完全远程）；入职首月原则上到岗，之后到岗频率由员工自行决定。员工须住在可通勤范围内。2025 财年：34% 的人每周到岗三天及以上，66% 每周两天及以下 | [职位](https://open.talentio.com/r/1/c/couger/pages/119821)、[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 18、24 页 |
| 工时 | 固定工时制，按岗位为 9:00–18:00 或 10:00–19:00 | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 24 页 |
| 薪资 | 官方职位：“非公開”（不公开）。Green：Product Tech Lead 1,000 万–1,500 万日元；Senior Software Engineer 和 Senior Software Engineer（ML）800 万–1,200 万日元；Senior Data Analyst 700 万–1,200 万日元。paiza 的 Unity 职位：500 万–1,200 万日元，含 45 小时固定加班费 | [Green](https://www.green-japan.com/company/5263)、[paiza](https://paiza.jp/career/job_offers/28362)；访问于 2026-10-11 |
| 加班与休假（2025 财年） | 平均加班每月 9.6 小时。平均带薪休假取得天数每年 14.6 天（含病假）。另有每年 3 天夏季休假和 5 天病假（入职时给 2 天） | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 18、24 页 |
| 福利 | 社会保险（関東ITソフトウェア健康保険組合）；通勤补贴上限 5 万日元；通信津贴；公司每月最多负担一次以交流为目的的午餐 | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 24–25 页 |
| 招聘流程 | 书面筛选，然后一面、二面和终面；工程师有技术课题；终面以外可选在线面试 | [招聘 FAQ](https://careers.couger.co.jp/) |
| 团队构成 | 工程师 49%；客户管理 16%；市场/公关 10%；人事、总务和会计 10%；产品管理 8%；业务企划和销售 4%。平均年龄：工程师 38 岁，产品与客户管理 35 岁。男女比例 7:3。20 名员工正在养育子女（其中女性 6 名） | [介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 18 页 |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：
- **公司网站：** careers.couger.co.jp 及其 10 个 Talentio 职位、英文 Notion 招聘页、virtualhumanlab.io 和 sphear.to。公司自己的网站 couger.co.jp 的 robots.txt 声明不允许作为 AI 输入（`ai-input=no`），因此本页不以其为来源。
- **公司渠道：** PR TIMES 公司页（company_id 33615；按编号检查了第 1–50 号新闻稿）和公司的 Speaker Deck 账户。
- **GitHub API：** 尝试过的组织名为 `couger`、`couger-inc`、`couger-jp`、`CougerInc`、`cougerinc`、`couger-ai`、`couger-lab`、`zkcream`、`ludens`、`ludens-ai`、`virtualhumanlab`、`sphear` 和 `geneflow`。
- **外部来源：** 国税厅法人番号公表网站、gBizINFO、伊藤忠商事、全家、Ridgelinez 和 Enterprise Ethereum Alliance 的新闻稿页面、Newswitch（日刊工业新闻）、北海道ハイテクノロジー専門学校、Product History Conference 2024 和 JSAI2026 的主办方页面、Green、paiza、Wantedly、LinkedIn、STARTUP DB 和 INITIAL。
- **网络检索：** 以クーガー株式会社、Couger、LUDENS、レイチェル和コネクトーム进行日英文检索。

结论：
- **融资细节。** 未找到金额、持股比例、估值、累计总额，也未找到伊藤忠以外的投资者。
- **营收与财务报表。** 未公开。gBizINFO 没有财务报表、补助金或政府采购记录；列有 4 件商标、0 件专利（[gBizINFO](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=7010701025073)；读取于 2026-10-11）。
- **价格。** LUDENS、Rachel 和 VisualCortex 均未公开价格。
- **全家和 Autobacs 试用以外的客户。** 职位提到未具名的服装和零售企业，一则 AI 导入顾问职位提到来自通信和金融领域的咨询（[职位](https://open.talentio.com/r/1/c/couger/pages/84428)）。
- **股权或股票期权。** 查阅到的职位均未提及。
- **签证支持。** 查阅到的职位均未说明。
- **安全认证。** 在查阅的来源中未找到。ISMS 只在 InfoSec 职位中作为加分经验出现（[职位](https://open.talentio.com/r/1/c/couger/pages/112252)）。未提交 ISMS、隐私标志（Privacy Mark）和 SECURITY ACTION 登记的检索表单。
- **工程博客。** Medium 出版物 `couger-blog` 最后一篇发布于 2024-05-22（RSS 读取于 2026-10-11）。Virtual Human Lab 博客以活动报道和随笔为主。在 `qiita.com/organizations/couger` 和 `zenn.dev/p/couger` 未找到组织（404）。
- **开源。** `couger-inc` 有 10 个公开仓库，其中 7 个已归档、3 个是 fork。`zkcream` 有 6 个，最后推送于 2022-02-25（[GitHub](https://github.com/couger-inc)、[GitHub](https://github.com/zkcream)）。
- **2026-10-11 无法读取的来源：**
  - CodeZine 的 Developers Summit 2025 报道，以及该活动在 event.shoeisha.jp 上的演讲页面（HTTP 403）；
  - TokyoDev（Cloudflare 验证，HTTP 403）；
  - medium.com 页面（HTTP 403；已读取 RSS）；
  - LinkedIn 个人资料页（HTTP 999）；
  - Buffett Code（HTTP 403）；
  - STARTUP DB 和 INITIAL 的融资数据（仅限会员）；
  - YOUTRUST 关于 Product History Conference 演讲的报道（客户端渲染，未取得正文）；
  - entethalliance-japan.org（无响应）；
  - 日经文章（付费墙；未引用）。

### 不同来源之间的不一致

- **门店数。** Couger 的招聘网站和介绍资料写约 7,000 家或“7,000店舗以上”（[招聘网站](https://careers.couger.co.jp/)；无日期，访问于 2026-10-11；[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)，2026-10-07）。激流オンライン报道“1万3000店が活用”（[2026-01-30](https://gekiryu-online.jp/2026/01/227822)）。
- **同一份介绍资料中的全家门店占比。** 第 8 页写“国内全店の半数近く”（近一半）；第 12 页写“国内全店舗の半数以上”（超过一半）（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)）。
- **公布的效果。**
  - 日销售额比条件相近的其他门店“平均３―４％”增长（[Newswitch（日刊工业新闻）](https://newswitch.jp/p/26324)，2021-03）。
  - “売上5%増”（[招聘网站](https://careers.couger.co.jp/)；无日期）。
  - 导入企业“売上の2〜3％向上”（[分析师职位](https://open.talentio.com/r/1/c/couger/pages/122132)，2026-04-09）。
  - 先行导入门店销售额平均 +2%，预期 SV 工作量减少约 30%（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 12 页）。
- **全家部署的开始时间。**
  - 日刊工业新闻 2021-03 报道称门店“昨年から”（自上一年即 2020 年起）试验性使用该代理（[Newswitch，2021-03-14](https://newswitch.jp/p/26324)）。
  - 介绍资料的时间线把“ファミリーマートへレイチェル提供開始”标在 2021 年（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 11 页）。
  - 2024 年的新闻稿称店长业务支援“2023年1月より”推进（[PR TIMES，2024-08-07](https://prtimes.jp/main/html/rd/p/000000033.000033615.html)）。
- **Virtual Human Lab 的起始时间。** 北海道ハイテクノロジー専門学校 2020-07-27 的通知把“バーチャルヒューマンラボ”描述为与 Couger 合作的产学教育项目（“株式会社COUGERが連携した産学連携の教育プログラム”）（[HHT，2020-07-27](https://www.hht.ac.jp/news/53284/)）。介绍资料的时间线则把“バーチャルヒューマンラボを開設”放在 2022 年，并描述为 AI 与脑科学研究活动（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 11 页）。两处来源都没有提及对方。
- **首席架构师。** [招聘网站成员页](https://careers.couger.co.jp/member)（无日期）将五十嵐 智哉列为チーフアーキテクト。[Virtual Human Lab 报道](https://virtualhumanlab.io/JP_blog_ArchitectureConference)（关于 2025-11-20 的演讲）则介绍土田 悠貴为チーフアーキテクト。两处来源都没有提及对方。
- **员工人数。**
  - 截至 2026-03-31 为 41 人（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)）。
  - 48 人（[Green](https://www.green-japan.com/company/5263)）和 46 名成员（[Wantedly](https://www.wantedly.com/companies/couger)）；均无日期，访问于 2026-10-11。
  - “11-50 employees”（[LinkedIn](https://www.linkedin.com/company/couger)）。
- **远程政策。**
  - 职位写“フルリモートは不可”（[职位](https://open.talentio.com/r/1/c/couger/pages/119821)）。
  - 招聘 FAQ 写“リモートで勤務可能です”，但有必须到岗的日子（[招聘网站](https://careers.couger.co.jp/)）。
  - 介绍资料中引用的成员问卷把公司描述为“フルリモート中心”（以完全远程为主）（[介绍资料](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki)第 21 页，2026-03 问卷）。

### 其他

- **公开重点的变化。**
  - Couger 在 PR TIMES 上 2018-04 至 2022-04 的新闻稿涉及与合作方的虚拟人项目（KDDI；ISID 与京王電鉄）、计算机视觉竞赛成绩、Blockchain EXE 社区，以及区块链项目（GeneFlow、OMEGA、ETHTerakoya、zkCREAM、EEA 日本支部职务）。
  - 2022-11 至 2025-06 的新闻稿以全家的 Rachel 和竞赛成绩为主。
  - 在从 PR TIMES 取得的 2025-07-03 至 2026-10-09 之间的 13 篇 Couger 新闻稿中，有 12 篇宣布 Sphear 活动；该区间内另有两个编号（42 和 47）返回 404（[PR TIMES 公司页](https://prtimes.jp/main/html/searchrlp/company_id/33615)）。Sphear 第 1 至第 6 场活动均定价 3,000 日元、各 30 个名额（[第 1 场，2025-07-03](https://prtimes.jp/main/html/rd/p/000000036.000033615.html)、[第 6 场，2026-01-08](https://prtimes.jp/main/html/rd/p/000000043.000033615.html)）。
- **名称撞车。** 一个名为 `LUDENS-AI` 的 GitHub 组织（创建于 2024-07-19；未认证；无网站、邮箱或公司字段）有一个以飞书登录为核心的中文仓库。未发现它与 Couger 有关联（[GitHub — LUDENS-AI](https://github.com/LUDENS-AI)）。
- **英文招聘页。** 英文 Notion 招聘页最后编辑于 2023-10-31，只列出两个 2022 年的职位。当前招聘网站和所有当前职位都是日文（[Notion](https://couger.notion.site/Careers-Couger-Inc-35ada7ab0ed34c1baff8dac5f86b5636)、[招聘网站](https://careers.couger.co.jp/)）。

---

## 资料来源

**官方**

- [PR TIMES 公司页](https://prtimes.jp/main/html/searchrlp/company_id/33615)
- [公司介绍资料，2026-10-07（Speaker Deck，日文）](https://speakerdeck.com/couger/kabushikigaisha-kanpani-dekki) · [游戏 AI 资料，2025-05-02（日文）](https://speakerdeck.com/couger/xian-shi-shi-jie-toiujiu-ji-noopunwarudogemuwoshi-xian-suruniha)
- [招聘网站（日文）](https://careers.couger.co.jp/) · [成员](https://careers.couger.co.jp/member)
- Talentio 职位（日文）——[Senior Software Engineer](https://open.talentio.com/r/1/c/couger/pages/119821) · [Full-stack Engineer](https://open.talentio.com/r/1/c/couger/pages/109446) · [Product Tech Lead](https://open.talentio.com/r/1/c/couger/pages/108687) · [Senior QA Engineer](https://open.talentio.com/r/1/c/couger/pages/117722) · [Senior Data Analyst](https://open.talentio.com/r/1/c/couger/pages/122132) · [InfoSec / Corporate IT](https://open.talentio.com/r/1/c/couger/pages/112252) · [Project Manager](https://open.talentio.com/r/1/c/couger/pages/84099) · [Technical Account Manager](https://open.talentio.com/r/1/c/couger/pages/84100) · [AI 导入顾问](https://open.talentio.com/r/1/c/couger/pages/84428)
- [英文招聘页（Notion）](https://couger.notion.site/Careers-Couger-Inc-35ada7ab0ed34c1baff8dac5f86b5636)——[Server Application Engineer](https://couger.notion.site/ad09a89b538849f585f410ce7ef4706f) · [Engineering Manager（ML/AI）](https://couger.notion.site/ec98d708d9e94523aa0161dc72b1cf6c)
- [Virtual Human Lab](https://virtualhumanlab.io/)——[アーキテクチャConference 2025 报道（日文）](https://virtualhumanlab.io/JP_blog_ArchitectureConference) · [Sphear](https://sphear.to/)
- GitHub——[couger-inc](https://github.com/couger-inc) · [组织 API](https://api.github.com/orgs/couger-inc) · [公开成员 API](https://api.github.com/orgs/couger-inc/public_members) · [cream](https://github.com/couger-inc/cream) · [research](https://github.com/couger-inc/research) · [zkcream](https://github.com/zkcream)

**新闻稿（PR TIMES，日文，较新在前）**

- [Sphear #13（含公司资料栏）— 2026-10-09](https://prtimes.jp/main/html/rd/p/000000050.000033615.html) · [Sphear #6 — 2026-01-08](https://prtimes.jp/main/html/rd/p/000000043.000033615.html) · [SSBC 2025 第 1 名 — 2025-07-10](https://prtimes.jp/main/html/rd/p/000000037.000033615.html)
- [Sphear 启动与第 1 场 — 2025-07-03](https://prtimes.jp/main/html/rd/p/000000036.000033615.html) · [CVPR 2025 workshop 论文 — 2025-06-17](https://prtimes.jp/main/html/rd/p/000000035.000033615.html) · [约 7,000 家全家门店、生成式 AI — 2024-08-07](https://prtimes.jp/main/html/rd/p/000000033.000033615.html)
- [CVPR 2024 MIPI — 2024-07-23](https://prtimes.jp/main/html/rd/p/000000032.000033615.html) · [CEO 出任全家生成式 AI 顾问 — 2023-12-05](https://prtimes.jp/main/html/rd/p/000000031.000033615.html) · [ECCV 2022 挑战赛 — 2023-01-23](https://prtimes.jp/main/html/rd/p/000000030.000033615.html)
- [向全家提供 Rachel、5,000 家门店 — 2022-11-29](https://prtimes.jp/main/html/rd/p/000000029.000033615.html) · [CEO 出任 EEA 日本支部代表 — 2022-04-07](https://prtimes.jp/main/html/rd/p/000000028.000033615.html) · [与律师事务所验证 zkCREAM — 2022-01-31](https://prtimes.jp/main/html/rd/p/000000027.000033615.html)
- [ICCV 2021 获奖 — 2021-11-29](https://prtimes.jp/main/html/rd/p/000000026.000033615.html) · [zkCREAM 资助 — 2021-07-02](https://prtimes.jp/main/html/rd/p/000000024.000033615.html) · [与以太坊基金会合作 — 2021-02-10](https://prtimes.jp/main/html/rd/p/000000023.000033615.html)
- [CVPR 2020 挑战赛 — 2020-06-29](https://prtimes.jp/main/html/rd/p/000000022.000033615.html) · [ETHTerakoya 启动 — 2020-05-25](https://prtimes.jp/main/html/rd/p/000000021.000033615.html) · [GeneFlow β 版 — 2020-04-14](https://prtimes.jp/main/html/rd/p/000000020.000033615.html)
- [与アクト合作 OMEGA — 2020-01-27](https://prtimes.jp/main/html/rd/p/000000018.000033615.html) · [伊藤忠合作 — 2020-01-20](https://prtimes.jp/main/html/rd/p/000000017.000033615.html) · [OpenEDS 挑战赛 — 2019-10-16](https://prtimes.jp/main/html/rd/p/000000011.000033615.html)
- [Connectome SDK 与顾问山川宏 — 2019-09-18](https://prtimes.jp/main/html/rd/p/000000010.000033615.html) · [トリエ京王調布 VHA 实证实验 — 2019-06-26](https://prtimes.jp/main/html/rd/p/000000009.000033615.html) · [GeneFlow（Connectome）— 2018-06-29](https://prtimes.jp/main/html/rd/p/000000005.000033615.html)
- [VHA 与 KDDI 项目 — 2018-04-26](https://prtimes.jp/main/html/rd/p/000000002.000033615.html)

**第三方报道与档案**

- [国税厅法人番号公表网站 — 7010701025073（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=7010701025073) · [gBizINFO（日文）](https://info.gbiz.go.jp/hojin/ichiran?hojinBango=7010701025073)
- [Enterprise Ethereum Alliance — 86 家新成员，2017-05-22](https://entethalliance.org/enterprise-ethereum-alliance-expands-dramatically-announcing-86-new-members/)
- [伊藤忠商事 — 对 Couger 的出资，2020-01-20（日文）](https://www.itochu.co.jp/ja/news/press/2020/200120.html)
- 全家（日文）——[2022-11-28](https://www.family.co.jp/company/news_releases/2022/20221128_02.html) · [2024-08-02](https://www.family.co.jp/company/news_releases/2024/20240802_01.html) · [2026-01-13](https://www.family.co.jp/company/news_releases/2026/20260113_02.html)
- [Ridgelinez — Autobacs 试用，2024-08-01（日文）](https://www.ridgelinez.com/news/news_20240801/)
- [Newswitch（日刊工业新闻）— 全家店长代理，2021-03-14（日文）](https://newswitch.jp/p/26324)
- [激流オンライン — 全家 AI 特辑，2026-01-30（日文）](https://gekiryu-online.jp/2026/01/227822)
- [北海道ハイテクノロジー専門学校 — Virtual Human Lab 项目，2020-07-27（日文）](https://www.hht.ac.jp/news/53284/)
- [WIRED — CEO 访谈，2022-05-16（日文）](https://wired.jp/article/the-next-innovators-3-atsushi-ishii/) · [SBBIT — CEO 访谈，2018-06-11（日文）](https://www.sbbit.jp/article/cont1/34986)
- [Green — CEO 访谈（日文）](https://www.green-japan.com/interview/5263) · [公司与职位（日文）](https://www.green-japan.com/company/5263) · [Senior Software Engineer（ML）（日文）](https://www.green-japan.com/company/5263/job/301740)
- [paiza — Unity 工程师职位，更新于 2024-12-20（日文）](https://paiza.jp/career/job_offers/28362)
- [Wantedly（日文）](https://www.wantedly.com/companies/couger) · [LinkedIn](https://www.linkedin.com/company/couger)
- [STARTUP DB（日文）](https://startup-db.com/companies/vNOKZXOUwDAp185L) · [INITIAL / Speeda（日文）](https://initial.inc/investors/V11957)
- 活动主办方（日文）——[Product History Conference 2024（YOUTRUST）](https://lp-prohis.youtrust.jp/2024/) · [JSAI2026 赞助商](https://www.ai-gakkai.or.jp/jsai2026/sponsor/)
- [GitHub — LUDENS-AI（名称撞车，未发现关联）](https://github.com/LUDENS-AI)
