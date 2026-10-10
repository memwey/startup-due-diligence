# Knowledge Work

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Knowledge Work（株式会社ナレッジワーク，网站页脚写作“Knowledge Work Inc.”）是一家东京公司，2020 年 3 月登记设立，并将 2020-04-01 定为创业日。公司于 2022 年 4 月推出同样名为 **ナレッジワーク** 的销售赋能云服务，现在面向日本大企业销售其所称的“セールスAIエージェント”（销售 AI 智能体），分为三条产品线：**Sales AX Consulting**（销售 AX 咨询）、**Sales AI Products**（AI 商谈记录、AI 销售角色扮演、代理商销售支持以及最初的知识共享模块）和 2026-08-04 推出的 **Sales AI Agent OS**（[服务网站](https://knowledgework.cloud/)；无日期，访问于 2026-10-11）。法人番号 4010401151825（[法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825)；信息截至 2026-10-11）。

- 融资：[2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) 公布 **シリーズC 1stクローズ 35 亿日元**（第三者配股增资），由 Globis Capital Partners 领投，新增十家企业／CVC 投资者，包括理光日本、三井住友银行和 NTT Docomo Ventures。公司最后一次公布的累计融资额是 Series B 后的 **61.2 亿日元**（[2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)）；Series C 之后未公布新的累计数字。
- 人数：截至 2026-02 共 **205** 名员工，其中“约半数”参与产品开发（[工程招聘页](https://knowledgework.com/recruit/engineering)；访问于 2026-10-11）；截至 2026-07 正式员工 **233** 名（[HERP 职位](https://herp.careers/v1/kwork/ZxZYCOkWex9k)；访问于 2026-10-11）。
- 于 [2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) 取得 Poetics（商谈分析 AI“JamRoll”）全部股份，并于 2025-06-30 将其吸收合并（[2025-07-01](https://prtimes.jp/main/html/rd/p/000000088.000063428.html)；[登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825)）。
- 工程（据公司自己的技术文章）：**Go** 后端，位于 100 多个模块的 monorepo 中；后端与 **TypeScript / React / Next.js** 前端共享 **protobuf / Connect RPC**；**Google Cloud**（Cloud Run、Cloud SQL for PostgreSQL、BigQuery）；LLM 调用 Gemini、GPT 和 Claude（[Zenn，2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c)；[Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)）。查阅到的工程职位均为日文，应届工程师职位要求 JLPT N1 或同等水平（[HERP](https://herp.careers/v1/kwork/ZxZYCOkWex9k)；访问于 2026-10-11）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 当前公开品牌 | ナレッジワーク / Knowledge Work；服务网站标语「セールスAIエージェント」 | [knowledgework.com](https://knowledgework.com/)、[knowledgework.cloud](https://knowledgework.cloud/)；访问于 2026-10-11 |
| 法定名称 | 株式会社ナレッジワーク；未在国税厅登记英文名称；网站页脚使用“Knowledge Work Inc.” | [法人番号公表サイト（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825)、[英文记录](https://www.houjin-bangou.nta.go.jp/en/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| 法人番号 | 4010401151825；指定于 2020-03-23 | [法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| 设立／创业 | 設立日 2020-03-18；創業日 2020-04-01（两者均见于公司公告） | [2026-08-04 公告](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)、[公司页面](https://knowledgework.com/company) |
| 总部 | 〒106-0041 東京都港区麻布台1丁目3-1 麻布台ヒルズ森JPタワー51F；登记地址于 2026-03-03 变更为麻布台1丁目3番1号 | [公司页面](https://knowledgework.com/company)；[登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| 代表人 | 代表取締役 CEO/CPO 麻野 耕司（Koji Asano） | [公司页面](https://knowledgework.com/company) |
| 资本金 | 97.4 亿日元，含资本准备金（資本準備金等含む） | [公司页面](https://knowledgework.com/company)；无日期，访问于 2026-10-11 |
| 员工人数 | 205 名（截至 2026-02）；正式员工 233 名（截至 2026-07） | [招聘页](https://knowledgework.com/recruit/engineering)、[HERP 职位](https://herp.careers/v1/kwork/ZxZYCOkWex9k) |
| 工程团队工作语言 | 无明文政策；工程职位以日文撰写，应届工程师和实习职位要求 JLPT N1 或同等的商务沟通能力（见“工作条件”） | [HERP 应届职位](https://herp.careers/v1/kwork/ZxZYCOkWex9k)；访问于 2026-10-11 |
| 客户 | 未公布总数；公告称“主に大手企業に数千名規模”（主要为大企业，数千人规模的部署），点名 NTT Docomo Business、瑞穗银行和日清食品 | [2026-08-04 公告](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) |
| 累计融资 | Series B 后累计 61.2 亿日元；此后又公布 35 亿日元的 Series C 1st close，未更新累计总额 | [2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)、[2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) |
| 最新公告列出的投资者 | 原有：グロービス・キャピタル・パートナーズ（领投）、DNX Ventures、WiL、Salesforce Ventures、フォースタートアップスキャピタル。Series B 之后的新投资者见“融资” | [2026-08-04 公告](https://prtimes.jp/main/html/rd/p/000000148.000063428.html) |
| 安全认证 | ISO/IEC 27001（IS 750583，初次登记 2021-09-15）；ISO/IEC 27017（CLOUD 791569，2023-12-13）；ISO/IEC 27701（PM 807882，2024-09-01）；针对“ナレッジワーク”产品系列的 SOC 2 Type 1 报告，基准日 2026-02-28，取得于 2026-03-26 | [ISMS 登记 27001](https://isms.jp/lst/ind/CR_IS_x0020_750583.html)、[ISMS 登记 27017](https://isms.jp/isms-cls/lst/ind/CR_CLOUD_x0020_791569.html)、[2024-09-26](https://prtimes.jp/main/html/rd/p/000000048.000063428.html)、[2026-04-02](https://prtimes.jp/main/html/rd/p/000000123.000063428.html) |
| 使命 | 「LIFE WITH ENABLEMENT できる喜びが巡る日々を届ける」（2025-07-11 制定；更早的公告使用「できる喜びが巡る日々を届ける」） | [首页](https://knowledgework.com/)、[2025-07-11](https://prtimes.jp/main/html/rd/p/000000089.000063428.html) |
| 公开账号 | X `@kworkcom`；GitHub `knowledge-work`；Speaker Deck `kworkdev`；Zenn publication `knowledgework`；note `knowledgework` | [首页](https://knowledgework.com/)、[Speaker Deck 主页](https://speakerdeck.com/kworkdev) |

**公司公布的奖项与认可：** 2022 年度优良设计奖（[2022-10-07](https://prtimes.jp/main/html/rd/p/000000012.000063428.html)）；BOXIL SaaS AWARD 2023 营销与销售部门第一名（[2023-05-15](https://prtimes.jp/main/html/rd/p/000000017.000063428.html)）；Salesforce Japan Partner Award 2025（[2025-04-10](https://prtimes.jp/main/html/rd/p/000000069.000063428.html)）；CTO 川中真耶获 Japan CxO Award 技术部门最优秀奖（[2025-12-17](https://prtimes.jp/main/html/rd/p/000000101.000063428.html)）。公布的专利：Knowledge AI Recommend（[2023-04-27](https://prtimes.jp/main/html/rd/p/000000021.000063428.html)）、“悬停放大与预览” UI（[2024-03-05](https://prtimes.jp/main/html/rd/p/000000039.000063428.html)）和查看器显示加速（[2024-03-06](https://prtimes.jp/main/html/rd/p/000000038.000063428.html)）。R&D 页面称，Poetics 曾入选 AWS 生成式 AI 加速器、Google 全球加速器项目和 AWS LLM 开发支援项目，合并后由 Knowledge Work 承继（[R&D](https://knowledgework.com/rd)；访问于 2026-10-11）。

### 品牌与法律实体

| 名称 | 类型 | 法域／期间 | 来源所述关系 | 来源 |
|---|---|---|---|---|
| 株式会社ナレッジワーク | 法律实体 | 日本；法人番号指定于 2020-03-23；存续 | knowledgework.com 和 knowledgework.cloud 网站的运营方 | [登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) |
| 株式会社Poetics | 原子公司，已合并 | 日本（涩谷）；法人番号 9010001187389；2025-05-01 取得 100% 股份，2025-06-30 被吸收合并 | “JamRoll”和“Poetics Speech API”的开发方；Knowledge Work 为存续公司 | [登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825)、[2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html)、[2025-07-01](https://prtimes.jp/main/html/rd/p/000000088.000063428.html) |
| kwork.studio | 原公司网站域名 | 至 2023-11 的公告中使用；现跳转至 knowledgework.com | HERP 职位页仍将其列为公司网站 | [2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)、[HERP 职位](https://herp.careers/careers/companies/kwork/jobs/w4Ks8k8FyIrE) |

登记的本店所在地变更历史（据登记）：港区海岸（2020-03）→ 江东区某地址（自 2020-07-14）→ 港区港南2丁目（自 2020-08-14）→ 港区西新橋1丁目（自 2022-08-15）→ 港区虎ノ門4丁目（神谷町トラストタワー，自 2024-02-02）→ 港区麻布台1丁目（自 2026-03-03）。公司于 [2026-02-16](https://prtimes.jp/main/html/rd/p/000000116.000063428.html) 宣布迁入麻布台之丘，并设置面向客户的“パークエリア”；于 [2026-09-04](https://prtimes.jp/main/html/rd/p/000000156.000063428.html) 宣布「デジタルイネーブルメントパーク」正式开放。

### 公司陈述的市场背景

根据 [Series C 公告（2026-08-04）](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)和[服务网站](https://knowledgework.cloud/)：

- 公司引用 MIT Project NANDA 的“The GenAI Divide: State of AI in Business 2025”，称企业生成式 AI 导入有 95% 未能带来 ROI。
- 公司将原因归于“水平型ユースケース”（全公司通用的 Copilot 和聊天机器人），主张转向“垂直型ユースケース”（按职能特化的智能体），并引用 McKinsey。
- 公司称日本的销售生产率很低，并将其归纳为两个问题：「営業効率」（时间被准备工作和内部事务占用）和「営業成果」（销售人员之间的业绩差异）。

---

## 产品

### 产品阵容

服务网站将产品分为三个系列（访问于 2026-10-11）：

| 系列 | 官方描述 | 列出的组成部分 | 页面 |
|---|---|---|---|
| セールスAXコンサルティングシリーズ（Sales AX Consulting） | 构建并运营按客户销售业务定制的 AI 智能体，由顾问和工程师交付 | セールスAXプランニング；データマネジメント・オペレーション；セールスイネーブルメント・コンサルティング；カスタマイズセールスAIエージェント構築；セールスイネーブルメント・トレーニング | [consulting](https://knowledgework.cloud/consulting) |
| セールスAIプロダクトシリーズ（Sales AI Products） | 面向标准销售业务的成品 AI 产品 | ナレッジワークAI商談記録（商谈记录）；ナレッジワークAI営業ロープレ（AI 角色扮演）；ナレッジワーク for パートナーセールス（代理商／合作伙伴销售） | [products](https://knowledgework.cloud/products) |
| セールスAIエージェントOSシリーズ（Sales AI Agent OS） | 利用企业自身数据和战略来构建、运行销售智能体的基础层 | セールスAIエージェントOS；セールスナレッジデータベース；セールスノウハウデータベース | [agentos](https://knowledgework.cloud/agentos) |

Sales AI Agent OS 被描述为四层：在销售语境中关联各公司销售数据的本体层、向智能体输入公司销售战略的战略层、实现／管理／分析智能体的智能体层，以及界面层（[2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)；[CTO／CAIO 访谈](https://knowledgework.com/why-enablement/4)）。公司称咨询和产品两个系列都运行在其之上。

产品沿革（据公司公告）：

- **2022-04-20**——「セールスイネーブルメントクラウド」“ナレッジワーク”正式发布，涵盖「ナレッジ領域」「ラーニング領域」「ワーク領域」（[公告](https://prtimes.jp/main/html/rd/p/000000003.000063428.html)）；Salesforce AppExchange 应用“Knowledge Work for Salesforce”于 [2022-10-24](https://prtimes.jp/main/html/rd/p/000000011.000063428.html) 发布。
- **2023-04**——设立“AI Integration Lab”，发布使用 ChatGPT 的“Knowledge AI Chat”（[2023-04-25](https://prtimes.jp/main/html/rd/p/000000020.000063428.html)、[2023-04-26](https://prtimes.jp/main/html/rd/p/000000022.000063428.html)）。
- **2024-12-05**——学习类产品「ラーニングイネーブルメント」（[公告](https://prtimes.jp/main/html/rd/p/000000056.000063428.html)）。
- **2025-02-18**——概念更名为「セールスイネーブルメントAI」；在主力模块「ナレッジ社内共有」之外新增三个模块：「ナレッジ資料作成」（PowerPoint 插件）、「ワーク商談推進」（基于 Salesforce 商机数据推荐知识）和「ワーク社外共有」（[公告](https://prtimes.jp/main/html/rd/p/000000063.000063428.html)）。
- **2025-05-15**——「ナレッジワークAI商談記録」，基于 Poetics 的 JamRoll 技术（[公告](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)）；之后扩展到 PC 浏览器和 Android 录音（[2025-10-22](https://prtimes.jp/main/html/rd/p/000000097.000063428.html)）、Salesforce 自定义对象（[2026-01-14](https://prtimes.jp/main/html/rd/p/000000108.000063428.html)）、将 NTT Docomo／au／SoftBank 运营商通话写入 Salesforce（[2026-04-27](https://prtimes.jp/main/html/rd/p/000000125.000063428.html)）以及 Windows 桌面应用（[2026-06-05](https://prtimes.jp/main/html/rd/p/000000131.000063428.html)）。
- **2025-11-28**——「ナレッジワークAI営業ロープレ」，使用 AI 虚拟形象进行角色扮演训练（[公告](https://prtimes.jp/main/html/rd/p/000000098.000063428.html)）。
- **2026-01-16**——概念更名为「セールスAXソリューション」，成立咨询部门「ナレッジワーク X」（[公告](https://prtimes.jp/main/html/rd/p/000000110.000063428.html)）；随后推出「ナレッジワーク for パートナーセールス」（[2026-02-04](https://prtimes.jp/main/html/rd/p/000000113.000063428.html)）、「ナレッジワークカスタマイズAIエージェント」（[2026-02-06](https://prtimes.jp/main/html/rd/p/000000114.000063428.html)）和「ナレッジワーク資料作成エージェント」（[2026-03-13](https://prtimes.jp/main/html/rd/p/000000119.000063428.html)）。
- **2026-05-20**——面向社内共有和 AI商談記録的「ナレッジワークMCPサーバー」，计划扩展到全部产品（[公告](https://prtimes.jp/main/html/rd/p/000000127.000063428.html)）；[2026-05-27](https://prtimes.jp/main/html/rd/p/000000128.000063428.html) 推出与 Agentforce 联动的金融业销售套件。
- **2026-08-04**——Sales AI Agent OS；**2026-08-06**——宣布开始研发以开放权重模型为基础的行业专用销售 LLM（[公告](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)）。

### 商业化

主要面向大企业，以按用户计费的云产品加咨询服务的形式销售。服务网站上未找到公开价目表，只提供资料下载、演示和咨询表单。找到的唯一公开价格是 AI商談記録：标价每用户每月 5,000 日元，2026 年 3 月底前申请可按 2,500 日元提供，仅限员工 1,000 人以上的企业（[2025-05-15](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)）。已公布的转售与共同交付渠道包括理光日本（“ナレッジワークAI商談記録 for RICOH”，[2026-08-04](https://prtimes.jp/main/html/rd/p/000000149.000063428.html)）、NTT Docomo Business（[2026-08-17](https://prtimes.jp/main/html/rd/p/000000152.000063428.html)）和三井住友金融集团的プラリタウン（[2026-08-20](https://prtimes.jp/main/html/rd/p/000000154.000063428.html)）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2022-04-20 | 经过封闭测试后，已在“複数の大手企業・中堅企業”的销售部门部署 | [公告](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) |
| 2023-10-02 | 理光日本向约 12,000 人部署，其中销售人员约 7,600 人 | [公告](https://prtimes.jp/main/html/rd/p/000000032.000063428.html) |
| 2025-02-18 | 以“開発人員100人規模”（约 100 名开发人员）推进销售 AI 智能体 | [公告](https://prtimes.jp/main/html/rd/p/000000063.000063428.html) |
| 2026-02 | 员工 205 名；约半数参与产品开发；平均年龄 36.32 岁；95.2% 为社招 | [招聘页](https://knowledgework.com/recruit/engineering)；访问于 2026-10-11 |
| 2026-07 | 正式员工 233 名 | [HERP 职位](https://herp.careers/v1/kwork/ZxZYCOkWex9k)；访问于 2026-10-11 |
| 2026-10-01 | YouTube 频道“NEW SALES チャンネル”开设 1 年 8 个月后订阅数超过 20 万 | [公告](https://prtimes.jp/main/html/rd/p/000000158.000063428.html) |

### 已公布客户与合作伙伴

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2022-06-17](https://prtimes.jp/main/html/rd/p/000000006.000063428.html) | Salesforce Ventures、ユーザベース、Sansan、One Capital | Series A 2nd close 投资者；与销售科技企业开展业务合作 |
| [2023-06-21](https://prtimes.jp/main/html/rd/p/000000023.000063428.html) | NTT Communications | 为 5,000 人规模使用而导入 |
| [2023-10-02](https://prtimes.jp/main/html/rd/p/000000032.000063428.html) | リコージャパン | 约 12,000 名用户 |
| [2024-04-22](https://prtimes.jp/main/html/rd/p/000000041.000063428.html) | みずほ銀行 | 约 5,000 名用户 |
| [2025-01-07](https://prtimes.jp/main/html/rd/p/000000059.000063428.html) | JTB | 法人销售部门 5,500 名用户 |
| [2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) | Poetics | 取得全部股份 |
| [2025-09-26](https://prtimes.jp/main/html/rd/p/000000094.000063428.html) | キリンビール | 社内共有，约 2,500 名用户 |
| [2025-10-31](https://prtimes.jp/main/html/rd/p/000000096.000063428.html) | パートナープロップ | 战略合作；进入合作伙伴赋能领域 |
| [2026-03-30](https://prtimes.jp/main/html/rd/p/000000122.000063428.html) | リコージャパン | 向约 6,000 人提供 AI商談記録 |
| [2026-07-28](https://prtimes.jp/main/html/rd/p/000000140.000063428.html) | 日本電気（NEC） | 1,000 人规模导入 AI商談記録 |
| [2026-08-04](https://prtimes.jp/main/html/rd/p/000000149.000063428.html) | リコージャパン | 资本业务合作；联合提案、系统集成及探讨共同开发 |
| [2026-08-17](https://prtimes.jp/main/html/rd/p/000000152.000063428.html) | NTTドコモビジネス | 面向销售 AX 的战略合作 |

2025 年以来点名的其他部署还包括 KDDI、三菱 HC Capital、三得利、日立系统、北陆银行、北海道银行、三井住友海上和 NN 生命（见 [PR TIMES 公司页](https://prtimes.jp/main/html/searchrlp/company_id/63428)）；每条均为单一企业的导入公告。

### 公开计划

- Series B（2023-11-29）：三年内发布十款新产品，首先是 2024 年 4 月的工作领域产品和 2024 年 7 月的学习领域产品（[公告](https://prtimes.jp/main/html/rd/p/000000035.000063428.html)）。
- ナレッジワーク X（2026-01-16）：三年内招聘约 200 名咨询专业人员（[公告](https://prtimes.jp/main/html/rd/p/000000110.000063428.html)）。
- SOC 2（2026-04-02）：目标取得 Type 2 报告（[公告](https://prtimes.jp/main/html/rd/p/000000123.000063428.html)）。
- Series C（2026-08-04）：与各行业龙头企业开展资本业务合作和 CVC 战略合作，并加速 Agent OS 开发（[公告](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)）。
- 行业 LLM（2026-08-06）：按行业（通信、IT、银行、保险、证券、制造、基础设施、零售、服务）特化的销售 LLM，在公司或客户可控的环境中训练和运行（[公告](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)）。

---

## 创始人

**麻野 耕司（Koji Asano）**——创始人、代表取締役 CEO/CPO（[公司页面](https://knowledgework.com/company)、[管理层页面](https://knowledgework.com/member)）。

- 2003 年：庆应义塾大学法学部毕业；加入 Link and Motivation。
- 2016 年：推出「モチベーションクラウド」，被称为日本首个组织改善云服务；2018 年：出任 Link and Motivation 董事。
- 2020 年 4 月：创立 Knowledge Work。著有『NEW SALES』（钻石社，[2022-06-08](https://prtimes.jp/main/html/rd/p/000000004.000063428.html)）、『THE TEAM』和『すべての組織は変えられる』（[管理层页面](https://knowledgework.com/member)）。

**川中 真耶（`@mayah`）**——共同创始人、CTO（[管理层页面](https://knowledgework.com/member)）。

- 2006 年：东京大学大学院信息理工学系研究科计算机科学专业硕士毕业；以研究员身份加入日本 IBM 东京基础研究所，从事 Web 安全和 Web 无障碍研究（[HERP 职位](https://herp.careers/v1/kwork/UM-xWCFZCVDN)）。
- 2011 年：以软件工程师身份加入 Google，参与 Chrome 开发。
- 2020 年：共同创立 Knowledge Work。曾参加 ACM ICPC 世界总决赛；担任漫画「王様達のヴァイキング」技术监修（[管理层页面](https://knowledgework.com/member)）。
- 作为第一名成员组建了公司的 FDE（Forward Deployed Engineer）小组，目前统管负责 FDE 工作和 Agent OS 开发的单元（[note，2026-08-28](https://note.com/knowledgework/n/n5c7dd150abd1)）。

**吉田 真麻（`@yoshiko`）**——管理层页面的简介写作「2020年、株式会社ナレッジワーク共同創業」；此前任职于 Goodpatch（2015）和 FOLIO（2017）；自创业起担任第一位前端工程师（[Zenn，2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)）；2023 年起任専門役員 Principal／软件工程师；Google Developer Expert（[管理层页面](https://knowledgework.com/member)、[HERP 职位](https://herp.careers/v1/kwork/UM-xWCFZCVDN)）。

### 主要管理层

| 姓名 | 所列职位 | 公开背景 | 来源 |
|---|---|---|---|
| 山崎 はずむ | CAIO | 原 Poetics CEO；通过 2025 年并购加入；东京大学博士课程（满期退学，未取得学位）；纽约大学特别研究员 | [管理层页面](https://knowledgework.com/member)、[2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) |
| 古森 茂幹 | 取締役 CSO | 日本惠普（2009 年董事，2014 年代表董事兼副社长执行董事）；Salesforce Japan（2015 年起任副社长，2024 年任董事副会长） | [管理层页面](https://knowledgework.com/member)、[2025-02-20](https://prtimes.jp/main/html/rd/p/000000065.000063428.html) |
| 田口 槙吾 | CRO（自 2026-08） | Sansan；Uzabase（FORCAS 事业 CEO）；2024 年加入 | [管理层页面](https://knowledgework.com/member)、[2026-08-10](https://prtimes.jp/main/html/rd/p/000000153.000063428.html) |
| 木村 秀夫（`@hidek`） | 上級執行役員 SVP，软件工程师；VPoE | GMO Internet；DeNA（2013 年起任执行董事）；Merpay VP of Engineering（2018）；2023 年加入 | [管理层页面](https://knowledgework.com/member)、[2023-09-01](https://prtimes.jp/main/html/rd/p/000000028.000063428.html) |
| 渡邊 尚吾（`@shogo`） | 執行役員 VP，软件工程师 | Google Cloud Japan 售前工程师（2020）；2023 年加入；Google Cloud Champion Innovator | [管理层页面](https://knowledgework.com/member)、[HERP 职位](https://herp.careers/v1/kwork/UM-xWCFZCVDN) |
| 日野 隆史 | 執行役員 VP，安全管理（自 2026-07） | 三井住友银行；雅虎日本（ISMS、事件管理）；Z Holdings；LINE Yahoo | [管理层页面](https://knowledgework.com/member)、[2026-07-01](https://prtimes.jp/main/html/rd/p/000000138.000063428.html) |
| 竹内 健太 | 執行役員 VP，财务（自 2026-09） | 摩根士丹利（并购顾问）；BizReach；Wharton MBA | [管理层页面](https://knowledgework.com/member)、[2026-09-01](https://prtimes.jp/main/html/rd/p/000000155.000063428.html) |
| 油井 誠（`@myui`） | 主导 Agent OS、行业 LLM 和 AI 研发的 AI 工程师（2026-07-01 加入） | 工学博士（奈良先端科学技术大学院大学）；产业技术综合研究所主任研究员；2015 年起任 Treasure Data 高级首席工程师；机器学习库 Hivemall 的开发者 | [2026-08-07](https://prtimes.jp/main/html/rd/p/000000151.000063428.html) |

公告中公布的董事会成员与顾问：自 [2022-04-20](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) 起，外部董事今野穣（Globis Capital Partners）和倉林陽（DNX Ventures），以及非常勤监事掛川紗矢香（原 Mercari）；自 [2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html) 起，外部董事難波俊充（WiL）和福山太郎（Fond 创始人）；自 [2026-04-20](https://prtimes.jp/main/html/rd/p/000000124.000063428.html) 起，原日本微软董事长樋口泰行任执行顾问。Go 专家上田拓也（`@tenntenn`）加入以启动“工程师赋能”业务（[2022-12-16](https://prtimes.jp/main/html/rd/p/000000016.000063428.html)）。[管理层页面](https://knowledgework.com/member)还列出了解决方案增长、金融行业客户、AX 咨询、客户成功、内容制作、HR、客户经理、业务架构、销售赋能、产品设计、公司职能和人才管理等方向的 VP 与 Principal。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2022-04 之前（当时未公开） | シードラウンド、プレシリーズAラウンド | 未单独披露 | グロービス・キャピタル・パートナーズ和 DNX Ventures（迄今各轮领投方）、ANRI、XTech Ventures | — | [2022-04-20](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) |
| 2022-04-20 | シリーズAラウンド 1stクローズ（第三者割当増資） | 10 亿日元 | 领投：グロービス・キャピタル・パートナーズ、DNX Ventures；另有 ANRI、XTech Ventures | 14.2 亿日元（含此前未公开的轮次） | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000063428.html) |
| 2022-06-17 | シリーズAラウンド 2ndクローズ（第三者割当増資） | 2 亿日元（Series A 合计 12 亿日元） | Salesforce Ventures、ユーザベース、Sansan、One Capital | 16.2 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000006.000063428.html) |
| 2023-11-29 | シリーズBラウンド（第三者割当増資） | 45 亿日元 | 领投：WiL、グロービス・キャピタル・パートナーズ；原有投资者及フォースタートアップスキャピタル等 | 61.2 亿日元 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000035.000063428.html) |
| 2026-08-04 | シリーズCラウンド 1stクローズ（第三者割当増資） | 35 亿日元 | 领投：グロービス・キャピタル・パートナーズ。新增：リコージャパン、Canon Marketing Japan MIRAI Fund、NTTドコモ・ベンチャーズ、三井住友銀行、ゆうちょアセットマネジメント（通过 JPSグロース・インベストメント投資事業有限責任組合）、三菱UFJイノベーション・パートナーズ、三井住友信託銀行、フコクCVCファンド－THE MUTUAL for Next 100－、電通ベンチャーズSGPファンド、博報堂DYベンチャーズ。原有：DNX Ventures、WiL、Salesforce Ventures、フォースタートアップスキャピタル | 未说明 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)、[公司新闻](https://knowledgework.com/news/article/jQM8vm0U) |

Globis Capital Partners 的合伙人在 Series C 公告中称，该机构“从创业轮起”持续以领投方身份参与；他在 Series B 公告中称该轮是创业出资后的第三次追加出资。フォースタートアップス称其集团自 2020 年起为 Knowledge Work 提供招聘支持，并于 2023 年 11 月首次出资（[2026-08-04](https://prtimes.jp/main/html/rd/p/000000469.000032589.html)）。佳能营销日本和 Global Brain（Canon MJ MIRAI Fund 及フコク基金的无限责任合伙人）都把 Canon MJ 基金 2026 年 8 月的出资称为「追加出資」（追加投资）（[Canon MJ](https://prtimes.jp/main/html/rd/p/000001442.000013943.html)、[Global Brain](https://prtimes.jp/main/html/rd/p/000000609.000047342.html)）；见“备注”。Series C 与 Agent OS 发布及理光日本资本业务合作同时公布；Series A 1st close 与产品正式发布同时公布。

---

## 工程

### 技术栈与平台

除另有标注外，以下均由公司自己的技术文章（Zenn publication、Speaker Deck、认证范围）证实。

- **后端：** Go，位于包含 100 多个 Go 模块的 monorepo 中，模块间本地依赖通过 `replace` 指令解决（[Zenn，2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c)）。以 **Protocol Buffers** 先定义 schema；公司称前后端共享的知识（包括认证与授权条件）都写在 protobuf 中（[Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)）。RPC 使用 **Connect RPC（gRPC）**（[Zenn，2026-03-06](https://zenn.dev/knowledgework/articles/6962837cd41940)）；2021 年时，前端调用 Extensible Service Proxy 上的 REST 端点，由其转发到 gRPC 服务器（[Zenn，2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)）。
- **前端：** TypeScript、React、Next.js、CSS Modules、Storybook；设计使用 Figma（[Zenn，2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)）；Connect ES 从 v1 迁移到 v2（[Zenn，2026-03-31](https://zenn.dev/knowledgework/articles/0d01d7aee48082)）；Vitest 取代 Jest（[Zenn，2023-12-26](https://zenn.dev/knowledgework/articles/jest-to-vitest)）；E2E 使用 Playwright。
- **云：** Google Cloud。ISO 27017 认证范围写明 Knowledge Work 是 Google Cloud 的云服务客户（[ISMS 登记](https://isms.jp/isms-cls/lst/ind/CR_CLOUD_x0020_791569.html)）。技术文章提到的服务：Cloud Run 和 Cloud Deploy（[Zenn，2024-02-26](https://zenn.dev/knowledgework/articles/cloud-deploy-for-cloud-run)）、Cloud Tasks 和 Cloud Scheduler（[Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)）、带只读副本的 Cloud SQL for PostgreSQL（[Zenn，2026-03-12](https://zenn.dev/knowledgework/articles/9956b686e28324)）、由 Datastream 导入数据的 BigQuery，以及以 Cloud Run Jobs 运行的 dbt，环境分为 dev／qa／stg／prd 项目（[Zenn，2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905)）。搜索使用 Elasticsearch（[Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)）。
- **AWS（承继）：** 原 Poetics／JamRoll 系统运行在 AWS 上（Amplify、ECS、RDS for MySQL），通过使用 Workload Identity Federation 和 AssumeRole 的私有连接与 Google Cloud 相连；公开计划是迁移到 Cloud Run 和 Cloud SQL，并从 MySQL 转为 PostgreSQL（[Speaker Deck，2026-01-31](https://speakerdeck.com/kworkdev/ma-post-merger-integration)；[Zenn，2025-10-07](https://zenn.dev/knowledgework/articles/303f715965d79d)）。
- **AI：** 每个智能体可选择 Gemini、GPT 或 Claude，默认在日本区域运行，客户允许时也可使用全球区域；从 Go 直接调用 SDK，工作流使用 `adk-go`（[Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)）；对外工具访问采用 Model Context Protocol（[2026-05-20](https://prtimes.jp/main/html/rd/p/000000127.000063428.html)）；内部 SRE 智能体使用 Google ADK（[Zenn，2026-09-28](https://zenn.dev/knowledgework/articles/ba94d985d1e341)）。公司称行业 LLM 以开放权重模型为起点（[2026-08-06](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)）。
- **工具：** Terraform（[Zenn，2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905)）、GitHub Actions（[Zenn，2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c)）、Datadog（[Zenn，2025-10-16](https://zenn.dev/knowledgework/articles/8ecf01f0ee0aea)）、Sentry（[Zenn，2025-03-28](https://zenn.dev/knowledgework/articles/39cf7c7e6f80f2)）；自研 ESLint 插件和一个 Terraform provider 公开在 GitHub 上（见下文）。
- **仅见于招聘：** SRE 职位将 GCP、AWS 或 Azure 上的基础设施运维经验列为优先条件（[HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)）；Azure 的使用未在其他来源中得到证实。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 多产品平台 | 网关层和认证层；由各产品后端（内容、CRM/SFA、技能、门户、流程、学习、录音、辅导、对外共享、资料生成、诀窍）共用的公共平台（目录、中间件）；内容处理；搜索；活动事件与审计；通知；来自 Azure AD 等的 SCIM 配置 | [Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework) |
| AI Backend | 智能体执行作为子系统隔离运行；智能体以 protobuf 定义为单体（LLM＋工具）、代理（Agentforce、Dify 等外部智能体）或工作流三类；工具通过 protobuf 注解定义，从各产品服务器动态获取列表，并以 OAuth2 scope 控制的 MCP 工具对外提供。资料称 AI商談記録和 AI営業ロープレ在该后端之外运行 | [Speaker Deck，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework) |
| Sales AI Agent OS | 本体层、战略层、智能体层和界面层（见“产品”）；CTO 称其从对销售活动及其状态变化的建模出发，而不是从表格数据出发 | [2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)、[CTO／CAIO 访谈](https://knowledgework.com/why-enablement/4) |
| AI 商谈记录 | 记录 Web 会议、IP 电话，并通过移动应用、PC 浏览器以及可自动检测 Teams 和 Zoom 会议的 Windows 桌面应用记录面谈；带说话人分离的转写、摘要与待办，自动录入 CRM/SFA（含 Salesforce 自定义对象）；运营商通话集成 | [2025-05-15](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)、[2026-06-05](https://prtimes.jp/main/html/rd/p/000000131.000063428.html)、[2026-04-27](https://prtimes.jp/main/html/rd/p/000000125.000063428.html) |
| AI 角色扮演 | 使用 AI 虚拟形象的角色扮演训练；AI Backend 资料称其涉及实时语音处理，运行在独立基础设施上 | [2025-11-28](https://prtimes.jp/main/html/rd/p/000000098.000063428.html)、[Speaker Deck](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework) |
| 知识共享（社内共有） | 最初的模块：销售资料与诀窍共享，带基于 RAG 的 AI 聊天、搜索输入辅助、分类自动推荐和自动摘要 | [2025-02-18](https://prtimes.jp/main/html/rd/p/000000063.000063428.html) |
| MCP server | 向外部 AI 智能体和 AI 聊天开放社内共有与 AI商談記録的数据 | [2026-05-20](https://prtimes.jp/main/html/rd/p/000000127.000063428.html) |
| 数据平台 | 将 Cloud SQL（PostgreSQL）、Google Analytics 和 Cloud Logging 的数据导入 BigQuery；dbt 分层；为客户输出分析报告 | [Zenn，2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905) |
| 语音研发 | 已发表的工作涉及日语说话人分离微调、重叠语音检测和语音识别数据增强（含 Poetics 时期的成果） | [R&D 页面](https://knowledgework.com/rd) |

**公开技术产出（访问于 2026-10-11）。** Zenn publication 共 197 篇文章，日期从 2021-09-27 到 2026-10-09（[zenn.dev/p/knowledgework](https://zenn.dev/p/knowledgework)）；note 上的“Knowledge Work Developers Blog”共 62 篇，包括「KNOWLEDGE WORK Dev Talk」访谈系列（[note](https://note.com/knowledgework)）；[Speaker Deck](https://speakerdeck.com/kworkdev) 上 41 份资料；一个 [Qiita organization](https://qiita.com/organizations/knowledgework)；以及 [connpass](https://knowledgework.connpass.com/) 上的「Encraft」学习会系列。GitHub 组织 [`knowledge-work`](https://github.com/knowledge-work)（创建于 2020-04-01）有 15 个公开仓库，其中 3 个为 fork；星标最多的是 `eslint-plugin-strict-dependencies`（242 星），近期的原创仓库包括 `go-vow`（Go linter，创建于 2026-09-17）、`command-action` 和一个 Slack Terraform provider（[GitHub API](https://api.github.com/orgs/knowledge-work/repos)）。公司赞助了 Go Conference 2025（[Zenn](https://zenn.dev/knowledgework/articles/968b90fca94b0b)）和日本音响学会 2026 年秋季研究发表会（[Zenn](https://zenn.dev/knowledgework/articles/c9e60d8a4a9cfe)）。

### 招聘所需技术背景

2026-10-11 开放的社招工程职位为 SRE（专家）、公司安全（专家）和一个工程类休闲面谈登记表；HERP 职位板上没有单独的 FDE 职位（[HERP 职位板](https://herp.careers/v1/kwork)）。

- **SRE（专家）**——必需：Web 应用开发经验；Web 安全知识与经验；日志分析与监控自动化经验；能自主提出并讨论规格、自行实现并编写测试；能与其他职种讨论产品。优先：在 GCP、AWS 或 Azure 上运维基础设施；定义 SLI/SLO 并基于数据改善性能；CI/CD 等开发效率提升；包含设计评审和代码评审的多人协作开发；能阅读技术文档的英语能力（[HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)；更新于 2026-09-28）。
- **公司安全（专家）**——必需：主导 ISMS 认证取得或运营；以 SaaS 为中心的 IT 基础设施安全（网络、服务器、IAM、加密、MDM、EDR）；Google Cloud／AWS 基础知识。优先：遵循 FISC 或 NIST SP 800 的经验；应用 OWASP 或 CIS 框架；CISSP／CISM／CEH；SAST、DAST、SIEM、CASB（[HERP](https://herp.careers/v1/kwork/QVNkg0p34ILT)）。
- **应届工程师（2027、2028 届）**——必需：编程经验（语言不限）和 JLPT N1 或同等水平；优先：计算机科学知识（[HERP](https://herp.careers/v1/kwork/ZxZYCOkWex9k)）。

### 行业领域

企业 B2B 销售：销售赋能、销售资料与诀窍、商谈记录、CRM/SFA（点名集成 Salesforce Sales Cloud 和 Agentforce），以及代理商／合作伙伴销售。公告中点名的客户集中在金融（银行、信托银行、保险）、电信和大型制造企业，行业 LLM 计划列出通信、IT、银行、保险、证券、制造、基础设施、零售和服务（[2026-08-06](https://prtimes.jp/main/html/rd/p/000000150.000063428.html)）。FDE 小组让工程师与负责设计各客户智能体工作的“エージェントストラテジスト”搭档（[note，2026-08-28](https://note.com/knowledgework/n/n5c7dd150abd1)）。查阅到的工程职位均未把销售或行业知识列为必需或优先条件；公司安全职位将 FISC（日本金融业安全指南）列为优先。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 无明文政策。工程职位以日文撰写；应届工程师和实习职位要求 JLPT N1 或同等的商务沟通能力；SRE 职位将能阅读技术文档的英语列为优先。未找到英文工程职位 | [应届](https://herp.careers/v1/kwork/ZxZYCOkWex9k)、[实习](https://herp.careers/v1/kwork/UM-xWCFZCVDN)、[SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE) |
| 地点 | 东京都港区麻布台之丘森 JP 塔 51 层 | [HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE) |
| 到岗政策 | 社招职位：混合办公，业务和公司职能岗每周到岗约 3 天，产品开发岗每周约 1 天；视情况或居住地，部分情况下允许完全远程。应届职位：以远程为基础，每周一天全公司到岗 | [SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)、[应届](https://herp.careers/v1/kwork/ZxZYCOkWex9k) |
| 异地员工 | 205 名员工中有 20 名（9.8%）为“遠方地勤務者”（截至 2026-02） | [招聘页](https://knowledgework.com/recruit/engineering) |
| 工时 | 弹性工时，标准每天 8 小时，核心时间 11:00–15:00；全员会议都在核心时间内举行 | [HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)、[招聘页](https://knowledgework.com/recruit/engineering) |
| 薪资 | SRE（专家）：理论年薪 910 万–2,310 万日元，基本月薪 65 万–165 万日元，含 45 小时固定加班费。公司安全（专家）：910 万–1,610 万日元。休闲面谈登记表：月薪 30 万–165 万日元，注明所有职位统一表述。每年两次奖金（2 月、8 月） | [SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)、[安全](https://herp.careers/v1/kwork/QVNkg0p34ILT)、[开放职位](https://herp.careers/v1/kwork/_lVOwBGi9TCb) |
| 休假和试用 | 周末和法定节假日休息；每年 4 月 1 日发放带薪假（第二年起 11–20 天）；产假、育儿假和护理假不论入职年限均可申请；男性员工育儿假取得率 100%（截至 2026-02）；试用期 3 个月 | [开放职位](https://herp.careers/v1/kwork/_lVOwBGi9TCb)、[招聘页](https://knowledgework.com/recruit/engineering) |
| 福利 | 通勤补贴每月最多 40,000 日元；“ABC Benefits”包括工作时间选择（时长和频率）、人生事件支持、学习支持（书籍、学习会）、资格考试费用、志愿活动假，以及 40 岁以上的高级体检 | [HERP](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)、[招聘页](https://knowledgework.com/recruit/engineering)、[2022-10-19](https://prtimes.jp/main/html/rd/p/000000013.000063428.html) |
| 评估 | 员工每季度申报希望的等级并与上级对齐；每季度回顾工作时间 | [招聘页](https://knowledgework.com/recruit/engineering) |
| 应届生和实习 | 招收 2027、2028 届应届工程师；选拔流程为在线编程测试、技术面试、“风格”面试、演讲和线下 CTO 面试。一个月带薪实习（时薪 2,000 日元，线上，约 5 人，后端或前端） | [应届](https://herp.careers/v1/kwork/ZxZYCOkWex9k)、[实习](https://herp.careers/v1/kwork/UM-xWCFZCVDN) |
| 签证 | 查阅到的职位均未说明 | [HERP 职位板](https://herp.careers/v1/kwork) |

---

## 备注

### 未公开披露

搜索范围（2026-10-11）：knowledgework.com 和 knowledgework.cloud 的 sitemap、公司页、管理层、R&D、安全、招聘和新闻页面；PR TIMES 公司 feed（121 条公告，2020-08-19 至 2026-10-01）；HERP `kwork` 职位板（careers 和 v1）；TokyoDev 和 Japan Dev 公司目录；Findy、Green 和 Wantedly 的公司页 URL；GitHub 组织 API（`knowledge-work`、`kwork`、`knowledgework`）；Zenn、note、Qiita、Speaker Deck 和 connpass；国税庁法人番号公表サイト；ISMS 登记；INITIAL；以ナレッジワーク、株式会社ナレッジワーク、Knowledge Work、kwork 和 Poetics 进行的日英文网络检索。

- **营收与利润。** 公司未公布。一篇二手文章称截至 2025 年 6 月的财年净亏损 2,217,038 千日元、总资产 4,123,317 千日元，但未注明所依据的決算公告（[coki.jp，2026-03-30](https://coki.jp/article/column/73539/)）；在查阅的来源中未找到原始公告。
- **客户数与 ARR。** 未找到总数。服务网站的 sitemap 在 `/users/` 下列出 19 个案例页面（[案例](https://knowledgework.cloud/users)；访问于 2026-10-11）。
- **价目表。** 仅 AI商談記録的标价见于公告；未找到其他产品价格。
- **Series C 后的累计融资与估值。** 公司未说明。把 35 亿日元的 Series C 1st close 加到公司公布的 Series B 后累计 61.2 亿日元上，得到 96.2 亿日元（研究者自行计算，并非公司数字）。
- **工程人数。** 除“開発人員100人規模”（2025-02-18）和“約半数がプロダクト開発に関与”（2026-02）外，未公布具体数字。
- **英文招聘与签证支持。** TokyoDev 和 Japan Dev 公司目录中未找到 Knowledge Work；HERP 上未找到英文职位或签证说明。Findy 和 Green 的 URL 返回未找到，Wantedly 的 URL 跳转到网站首页。
- **状态页、SLA 和公开 API 参考。** 均未找到；`status.knowledgework.cloud` 和 `help.knowledgework.cloud` 无法解析。
- **完整董事会构成。** 公司页面只列出代表董事；董事会成员只能从任命公告得知。
- **离职率。** 未公开。
- **J-Startup。** 未找到 Knowledge Work 入选的信息；公司称 Poetics 获得了 J-Startup 认定（[2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html)）。

### 不同来源之间的不一致

- **成立日期：** 公告写設立日 2020-03-18、創業日 2020-04-01（[2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)）；[理光日本联合公告](https://prtimes.jp/main/html/rd/p/000000149.000063428.html)和[佳能营销日本](https://prtimes.jp/main/html/rd/p/000001442.000013943.html)把 2020-04-01 标为設立；登记显示法人番号指定于 2020-03-23。
- **Poetics 收购日期：** [收购公告](https://prtimes.jp/main/html/rd/p/000000073.000063428.html)写“2025年5月1日に…全株式を取得”，而[合并公告](https://prtimes.jp/main/html/rd/p/000000088.000063428.html)中 CEO 的评论写“2025年4月30日に株式取得”。
- **Canon MJ MIRAI Fund：** Knowledge Work 将其列在「シリーズB以降の新規投資家」之下（[2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)），而[佳能营销日本](https://prtimes.jp/main/html/rd/p/000001442.000013943.html)和 [Global Brain](https://prtimes.jp/main/html/rd/p/000000609.000047342.html) 称 2026 年 8 月的出资为「追加出資」。未找到宣布更早一次 Canon MJ 出资的公告。
- **累计融资与估值（第三方）：** HERP 显示累計調達額 57 亿日元、評価額 146.9 亿日元（[HERP](https://herp.careers/careers/companies/kwork/jobs)；无日期，访问于 2026-10-11），低于公司自己公布的截至 2023-11 的 61.2 亿日元。INITIAL 显示截至 2026-07-29 含潜在股份的投后估值为 22,403 百万日元（[INITIAL](https://initial.inc/companies/A-38065)）。两个估值均非公司公布。
- **员工人数：** 205（2026-02，招聘页）、233 名正式员工（2026-07，HERP 职位）、235（HERP 公司页眉；无日期）。各数字的日期和口径不同。
- **远程政策：** 社招职位称产品开发岗约每周到岗一次（[SRE](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)）；应届职位称以远程为基础、每周一天全公司到岗（[应届](https://herp.careers/v1/kwork/ZxZYCOkWex9k)）；实习则可选择周二到岗（[实习](https://herp.careers/v1/kwork/UM-xWCFZCVDN)）。
- **职位中的 CTO 简介：** 2028 届应届工程师职位的“CTOプロフィール”栏重复了 CEO 的履历文字（[HERP](https://herp.careers/v1/kwork/ZxZYCOkWex9k)；访问于 2026-10-11）；其他职位和管理层页面给出的是 CTO 本人的履历。
- **公司网站：** HERP 职位页列出 `kwork.studio`，该域名现已跳转到 knowledgework.com（[HERP](https://herp.careers/careers/companies/kwork/jobs/w4Ks8k8FyIrE)）。

### 其他

- 公司对其产品的总体描述已变更四次：「セールスイネーブルメントクラウド」（2022-04）、「セールスイネーブルメントAI」（2025-02-18）、「セールスAXソリューション」（2026-01-16），以及分为三个系列的「セールスAIエージェント」（2026-08-04）。模块名称也有变化，例如「ナレッジ社内共有」（2025）改为「ナレッジワーク社内共有」（2026）。CEO 称 Series C 认可了公司「SaaS企業からAIエージェント企業への進化」（[2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)）。
- 一场演讲介绍了 Poetics 的并购后整合：用 Git Subtree 把仓库并入 monorepo、统一 GitHub 组织、共享 trunk-based 开发和 CUJ/SLO 实践，并将 JamRoll 的 GraphQL API 迁移到 Connect RPC（[Speaker Deck，2026-01-31](https://speakerdeck.com/kworkdev/ma-post-merger-integration)）。
- 公司在产品之外还经营销售类媒体活动：YouTube 频道「NEW SALES チャンネル」（[2025-01-29](https://prtimes.jp/main/html/rd/p/000000061.000063428.html)）、邀请制会议「NEW SALES PREMIERE」（2022 年起）以及与 Forbes JAPAN 合办的「Forbes JAPAN NEW SALES OF THE YEAR」（2023 年起每年举办）。相关公告每年都会出现在新闻 feed 中。
- 近期许多公告是 AI商談記録和 AI営業ロープレ的单一客户导入公告，尤其是地方银行和保险公司（2026-03 至 2026-07）。

---

## 资料来源

**官方**

- [公司官网（日文）](https://knowledgework.com/) · [公司信息](https://knowledgework.com/company) · [管理层](https://knowledgework.com/member) · [R&D](https://knowledgework.com/rd) · [信息安全方针](https://knowledgework.com/security) · [新闻索引](https://knowledgework.com/news/pr)
- [关于 Agent OS 的 CTO／CAIO 访谈（日文）](https://knowledgework.com/why-enablement/4)
- [服务网站——セールスAIエージェント（日文）](https://knowledgework.cloud/) · [Sales AX Consulting](https://knowledgework.cloud/consulting) · [Sales AI Products](https://knowledgework.cloud/products) · [Sales AI Agent OS](https://knowledgework.cloud/agentos) · [案例](https://knowledgework.cloud/users)
- [工程招聘页（日文）](https://knowledgework.com/recruit/engineering)
- [HERP 职位板](https://herp.careers/v1/kwork)——[SRE（专家）](https://herp.careers/v1/kwork/w4Ks8k8FyIrE)、[公司安全（专家）](https://herp.careers/v1/kwork/QVNkg0p34ILT)、[工程开放职位](https://herp.careers/v1/kwork/_lVOwBGi9TCb)、[2028 届应届工程师](https://herp.careers/v1/kwork/ZxZYCOkWex9k)、[2028 届工程实习](https://herp.careers/v1/kwork/UM-xWCFZCVDN) · [HERP Career 公司职位列表](https://herp.careers/careers/companies/kwork/jobs) · [HERP Career SRE 页面](https://herp.careers/careers/companies/kwork/jobs/w4Ks8k8FyIrE)
- [Zenn publication（日文）](https://zenn.dev/p/knowledgework)——[前端架构回顾，2021-09-27](https://zenn.dev/knowledgework/articles/32371c83e68cbe)、[Jest 迁移到 Vitest，2023-12-26](https://zenn.dev/knowledgework/articles/jest-to-vitest)、[Cloud Run 的 Cloud Deploy，2024-02-26](https://zenn.dev/knowledgework/articles/cloud-deploy-for-cloud-run)、[Go monorepo CI，2025-02-21](https://zenn.dev/knowledgework/articles/5d19395eb9e07c)、[Sentry 自定义 span，2025-03-28](https://zenn.dev/knowledgework/articles/39cf7c7e6f80f2)、[数据平台，2025-09-14](https://zenn.dev/knowledgework/articles/knowledgework-data-platform-20250905)、[AWS×GCP 私有 DNS，2025-10-07](https://zenn.dev/knowledgework/articles/303f715965d79d)、[Go Conference 2025 赞助，2025-10-08](https://zenn.dev/knowledgework/articles/968b90fca94b0b)、[异步处理监控，2025-10-16](https://zenn.dev/knowledgework/articles/8ecf01f0ee0aea)、[Go＋Connect interceptor，2026-03-06](https://zenn.dev/knowledgework/articles/6962837cd41940)、[Cloud SQL 复制延迟，2026-03-12](https://zenn.dev/knowledgework/articles/9956b686e28324)、[Connect ES v2 迁移，2026-03-31](https://zenn.dev/knowledgework/articles/0d01d7aee48082)、[用 Google ADK 开发 SRE 智能体，2026-09-28](https://zenn.dev/knowledgework/articles/ba94d985d1e341)、[日本音响学会赞助，2026-09-29](https://zenn.dev/knowledgework/articles/c9e60d8a4a9cfe)
- [note 上的 Knowledge Work Developers Blog（日文）](https://note.com/knowledgework)——[FDE Dev Talk，2026-08-28](https://note.com/knowledgework/n/n5c7dd150abd1)
- [Speaker Deck——kworkdev](https://speakerdeck.com/kworkdev)——[Knowledge Work の AI Backend，2025-12-22](https://speakerdeck.com/kworkdev/ai-backend-of-knowledgework)、[并购后整合，2026-01-31](https://speakerdeck.com/kworkdev/ma-post-merger-integration)
- [Qiita organization](https://qiita.com/organizations/knowledgework) · [connpass——Encraft](https://knowledgework.connpass.com/)
- [GitHub 组织](https://github.com/knowledge-work) · [通过 API 查看仓库](https://api.github.com/orgs/knowledge-work/repos)

**新闻稿（PR TIMES，日文，较新在前）**

- [PR TIMES 公司页](https://prtimes.jp/main/html/searchrlp/company_id/63428)
- [NEW SALES 频道订阅超过 20 万 — 2026-10-01](https://prtimes.jp/main/html/rd/p/000000158.000063428.html) · [デジタルイネーブルメントパーク正式开放 — 2026-09-04](https://prtimes.jp/main/html/rd/p/000000156.000063428.html) · [VP 财务任命 — 2026-09-01](https://prtimes.jp/main/html/rd/p/000000155.000063428.html)
- [三井住友金融集团プラリタウン销售合作 — 2026-08-20](https://prtimes.jp/main/html/rd/p/000000154.000063428.html) · [NTT Docomo Business 战略合作 — 2026-08-17](https://prtimes.jp/main/html/rd/p/000000152.000063428.html) · [CRO 任命 — 2026-08-10](https://prtimes.jp/main/html/rd/p/000000153.000063428.html)
- [油井誠加入 — 2026-08-07](https://prtimes.jp/main/html/rd/p/000000151.000063428.html) · [行业专用销售 LLM 研发 — 2026-08-06](https://prtimes.jp/main/html/rd/p/000000150.000063428.html) · [Sales AI Agent OS 与 Series C 1st close 35 亿日元 — 2026-08-04](https://prtimes.jp/main/html/rd/p/000000148.000063428.html)
- [理光日本资本业务合作 — 2026-08-04](https://prtimes.jp/main/html/rd/p/000000149.000063428.html) · [NEC 导入 AI商談記録 — 2026-07-28](https://prtimes.jp/main/html/rd/p/000000140.000063428.html) · [VP 安全管理任命 — 2026-07-01](https://prtimes.jp/main/html/rd/p/000000138.000063428.html)
- [AI商談記録桌面应用 — 2026-06-05](https://prtimes.jp/main/html/rd/p/000000131.000063428.html) · [金融业 Agentforce 套件 — 2026-05-27](https://prtimes.jp/main/html/rd/p/000000128.000063428.html) · [MCP server 与数据运营 — 2026-05-20](https://prtimes.jp/main/html/rd/p/000000127.000063428.html)
- [AI商談記録运营商通话 — 2026-04-27](https://prtimes.jp/main/html/rd/p/000000125.000063428.html) · [执行顾问樋口泰行 — 2026-04-20](https://prtimes.jp/main/html/rd/p/000000124.000063428.html) · [SOC 2 Type 1 报告 — 2026-04-02](https://prtimes.jp/main/html/rd/p/000000123.000063428.html)
- [理光日本 AI商談記録约 6,000 人 — 2026-03-30](https://prtimes.jp/main/html/rd/p/000000122.000063428.html) · [資料作成エージェント — 2026-03-13](https://prtimes.jp/main/html/rd/p/000000119.000063428.html) · [迁入麻布台之丘 — 2026-02-16](https://prtimes.jp/main/html/rd/p/000000116.000063428.html)
- [定制 AI 智能体 — 2026-02-06](https://prtimes.jp/main/html/rd/p/000000114.000063428.html) · [ナレッジワーク for パートナーセールス — 2026-02-04](https://prtimes.jp/main/html/rd/p/000000113.000063428.html) · [ナレッジワーク X 与销售 AX 解决方案 — 2026-01-16](https://prtimes.jp/main/html/rd/p/000000110.000063428.html)
- [支持 Salesforce 自定义对象 — 2026-01-14](https://prtimes.jp/main/html/rd/p/000000108.000063428.html) · [CTO 获 Japan CxO Award — 2025-12-17](https://prtimes.jp/main/html/rd/p/000000101.000063428.html) · [AI営業ロープレ发布 — 2025-11-28](https://prtimes.jp/main/html/rd/p/000000098.000063428.html)
- [PartnerProp 合作 — 2025-10-31](https://prtimes.jp/main/html/rd/p/000000096.000063428.html) · [AI商談記録 PC 浏览器与 Android 录音 — 2025-10-22](https://prtimes.jp/main/html/rd/p/000000097.000063428.html) · [麒麟啤酒导入社内共有 — 2025-09-26](https://prtimes.jp/main/html/rd/p/000000094.000063428.html)
- [新使命“LIFE WITH ENABLEMENT” — 2025-07-11](https://prtimes.jp/main/html/rd/p/000000089.000063428.html) · [合并 Poetics — 2025-07-01](https://prtimes.jp/main/html/rd/p/000000088.000063428.html) · [AI商談記録发布 — 2025-05-15](https://prtimes.jp/main/html/rd/p/000000076.000063428.html)
- [收购 Poetics — 2025-05-01](https://prtimes.jp/main/html/rd/p/000000073.000063428.html) · [Salesforce Japan Partner Award 2025 — 2025-04-10](https://prtimes.jp/main/html/rd/p/000000069.000063428.html) · [古森茂幹出任董事兼 CSO — 2025-02-20](https://prtimes.jp/main/html/rd/p/000000065.000063428.html)
- [セールスイネーブルメントAI — 2025-02-18](https://prtimes.jp/main/html/rd/p/000000063.000063428.html) · [NEW SALES YouTube 频道 — 2025-01-29](https://prtimes.jp/main/html/rd/p/000000061.000063428.html) · [JTB 5,500 名用户 — 2025-01-07](https://prtimes.jp/main/html/rd/p/000000059.000063428.html)
- [学习赋能产品 — 2024-12-05](https://prtimes.jp/main/html/rd/p/000000056.000063428.html) · [ISO 27701 — 2024-09-26](https://prtimes.jp/main/html/rd/p/000000048.000063428.html) · [瑞穗银行约 5,000 名用户 — 2024-04-22](https://prtimes.jp/main/html/rd/p/000000041.000063428.html)
- [专利：查看器加速 — 2024-03-06](https://prtimes.jp/main/html/rd/p/000000038.000063428.html) · [专利：悬停预览 — 2024-03-05](https://prtimes.jp/main/html/rd/p/000000039.000063428.html) · [ISO 27017 — 2024-02-20](https://prtimes.jp/main/html/rd/p/000000037.000063428.html)
- [Series B 45 亿日元 — 2023-11-29](https://prtimes.jp/main/html/rd/p/000000035.000063428.html) · [理光日本约 12,000 名用户 — 2023-10-02](https://prtimes.jp/main/html/rd/p/000000032.000063428.html) · [VPoE 任命 — 2023-09-01](https://prtimes.jp/main/html/rd/p/000000028.000063428.html)
- [NTT Communications 5,000 人规模 — 2023-06-21](https://prtimes.jp/main/html/rd/p/000000023.000063428.html) · [BOXIL SaaS AWARD 2023 — 2023-05-15](https://prtimes.jp/main/html/rd/p/000000017.000063428.html) · [专利：Knowledge AI Recommend — 2023-04-27](https://prtimes.jp/main/html/rd/p/000000021.000063428.html)
- [Knowledge AI Chat — 2023-04-26](https://prtimes.jp/main/html/rd/p/000000022.000063428.html) · [AI Integration Lab — 2023-04-25](https://prtimes.jp/main/html/rd/p/000000020.000063428.html) · [工程师赋能业务、tenntenn 加入 — 2022-12-16](https://prtimes.jp/main/html/rd/p/000000016.000063428.html)
- [Knowledge Work for Salesforce — 2022-10-24](https://prtimes.jp/main/html/rd/p/000000011.000063428.html) · [Life Event Support — 2022-10-19](https://prtimes.jp/main/html/rd/p/000000013.000063428.html) · [2022 年度优良设计奖 — 2022-10-07](https://prtimes.jp/main/html/rd/p/000000012.000063428.html)
- [Series A 2nd close — 2022-06-17](https://prtimes.jp/main/html/rd/p/000000006.000063428.html) · [『NEW SALES』出版 — 2022-06-08](https://prtimes.jp/main/html/rd/p/000000004.000063428.html) · [正式发布与 Series A 1st close — 2022-04-20](https://prtimes.jp/main/html/rd/p/000000003.000063428.html)
- [公司网站上的 Series C 公告](https://knowledgework.com/news/article/jQM8vm0U)

**第三方报道与档案**

- [佳能营销日本——追加出资，2026-08-04（日文）](https://prtimes.jp/main/html/rd/p/000001442.000013943.html) · [Global Brain，2026-08-04（日文）](https://prtimes.jp/main/html/rd/p/000000609.000047342.html) · [フォースタートアップス，2026-08-04（日文）](https://prtimes.jp/main/html/rd/p/000000469.000032589.html)
- [BRIDGE——Series C，2026-08-06（日文）](https://thebridge.jp/2026/08/knowledgework-raises-3-5-billion-yen-series-c-for-sales-ai-agent-os)
- [国税庁法人番号公表サイト——4010401151825（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010401151825) · [英文记录](https://www.houjin-bangou.nta.go.jp/en/henkorireki-johoto.html?selHouzinNo=4010401151825)
- [ISMS 登记——IS 750583（日文）](https://isms.jp/lst/ind/CR_IS_x0020_750583.html) · [CLOUD 791569（日文）](https://isms.jp/isms-cls/lst/ind/CR_CLOUD_x0020_791569.html)
- [INITIAL／Speeda（日文）](https://initial.inc/companies/A-38065)
- [coki.jp——2025 年 6 月期数字，2026-03-30（日文）](https://coki.jp/article/column/73539/)
