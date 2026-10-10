# ACES

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

ACES（株式会社ACES / ACES, Inc.）是一家东京公司，于 2017-11-20 由六名创始人创立，其中三人出自东京大学松尾研究室。总部位于文京区汤岛。公司经营两项业务。**DX Partner** 业务为大企业和政府机构设计、开发并运营定制 AI 系统，采用项目合同加 AI 许可合同的形式。**AI 软件**业务销售 **ACES Meet**，这是一款 AI 会议纪要与销售赋能 SaaS，运行在自研语音识别系统之上。公司目前把自己的技术基础称为“AI OS”：由可复用的数据、知识和 agent 模块组成，用于构建针对单个企业的“专家 AI”（expert AI）。ACES 未上市。其招聘材料称公司正在准备 IPO。

- 已披露的融资：来自 Deep30 和 IGPI 的种子轮，金额为数千万円（[2019-05-22](https://acesinc.co.jp/news/post-930)）；来自 IGPI 和 Deep30 的约 3.2 亿日元（約3.2億円）（[2020-12-03](https://acesinc.co.jp/news/post-782)）；以及与 SOMPO Light Vortex 的资本业务合作，金额未披露（[2022-05-26](https://acesinc.co.jp/news/post-536)）。资本金为 1 亿日元（[公司概要](https://acesinc.co.jp/company-profile)；无日期，访问于 2026-10-11）。未发现之后的融资轮次。
- 人数：正式员工 72 人（[招聘网站](https://recruit.acesinc.co.jp/workstyle)；无日期，访问于 2026-10-11）；“正社員70名 / 全体110名規模”（正式员工 70 人，含外包和实习生约 110 人）（[HR 候选人资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)）。2026-03-19 的一篇工程博客按相同口径给出约 150 人；见“备注”。
- 公司称 DX Partner 业务“前年比190%”（为上一年的 190%）（[HR 资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)）。近期具名项目包括与三井住友银行共同开发的法人营业 AI 应用（[2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html)），以及与 YKK AP 合作的不安全行为检测（[2025-04-23](https://prtimes.jp/main/html/rd/p/000000099.000044470.html)）。
- 工程：公司称主要开发语言为 Python 和 JavaScript/TypeScript（[技术博客，2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123)）。ACES Meet 在 AWS 上运行 Python/Django 和 Next.js，认证用 Auth0，授权用 Cerbos（[技术博客](https://tech.acesinc.co.jp/)）。DX Partner 职位列出 AWS 或 Azure。所查阅的职位全部为日文，其中一个要求商务级日语（[Algorithm Engineer/Manager 职位](https://open.talentio.com/r/1/c/aces/pages/94487)；无日期，访问于 2026-10-11）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | 株式会社ＡＣＥＳ（假名读音 エーシーズ）/ ACES, Inc. | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856)、[公司概要](https://acesinc.co.jp/company-profile) |
| 法人编号 | 4010001187856，指定于 2017-11-22 | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856) |
| 成立 | 2017-11-20 | [公司概要](https://acesinc.co.jp/company-profile) |
| 总部 | 〒113-0034 東京都文京区湯島二丁目31番14号 ルーシッドスクエア湯島3階。登记地址为 東京都文京区湯島２丁目３１番１４号（最后更新于 2024-01-12） | [公司概要](https://acesinc.co.jp/company-profile)、[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856) |
| 代表人 | 代表取締役 田村 浩一郎（Koichiro Tamura） | [公司概要](https://acesinc.co.jp/company-profile) |
| 资本金 | 1 亿日元（1億円） | [公司概要](https://acesinc.co.jp/company-profile)；[PR TIMES 公司信息栏](https://prtimes.jp/main/html/rd/p/000000073.000044470.html)；无日期，访问于 2026-10-11 |
| 财年结束日 | 9 月 30 日（据 2020 和 2021 财年的官报公告） | [catr.jp 汇总的官報公告](https://catr.jp/companies/cd880/160167) |
| 上市状态 | 未上市（“未上場”）。职位和招聘网站称“IPO準備中”（正在准备 IPO）。ACES 未出现在 2026-10-06 更新的 JPX 新上市页面上 | [PR TIMES 公司信息栏](https://prtimes.jp/main/html/rd/p/000000073.000044470.html)、[招聘网站](https://recruit.acesinc.co.jp/workstyle)、[JPX](https://www.jpx.co.jp/listing/stocks/new/index.html) |
| 业务线 | DXパートナーサービス（DX Partner）、AIソフトウェアサービス（AI 软件） | [公司概要](https://acesinc.co.jp/company-profile) |
| 人数 | 正式员工 72 人，分布为 DX Partner 54.2%、AI 软件 20.8%、R&D 13.8%、管理部门 11.1%（无日期，访问于 2026-10-11）。正式员工 70 人 / 总计约 110 人（2026-07-30） | [招聘网站](https://recruit.acesinc.co.jp/workstyle)、[HR 资料](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| 工作语言 | 日语。所有职位均为日文；见“工作条件” | [Talentio 招聘页](https://open.talentio.com/r/1/c/aces/homes/2662) |
| 投资方（已披露） | Deep30投資事業有限責任組合、株式会社経営共創基盤（IGPI）、SOMPO Light Vortex株式会社 | [2019-05-22](https://acesinc.co.jp/news/post-930)、[2020-12-03](https://acesinc.co.jp/news/post-782)、[2022-05-26](https://acesinc.co.jp/news/post-536) |
| 累计融资 | 未公布累计金额；见“融资” | — |
| 安全认证 | ISO/IEC 27001，2022-04-21 公布（基础 ISMS 证书 IS 764116）。ACES Meet 的 ISO/IEC 27017（JIP-ISMS517-1.0），证书 CLOUD 847927，2026-07-28 登记，有效期至 2028-03-29，认证机构 BSI Group Japan | [2022-04-21](https://acesinc.co.jp/news/post-564)、[2026-08-03](https://prtimes.jp/main/html/rd/p/000000120.000044470.html) |

**登记地址变更历史**（[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856)）：指定时为文京区小石川；2018-06-11 起为文京区本郷2丁目；2019-07-31 起为文京区本郷4丁目（本郷トーセイビル）；2021-02-09 起为文京区湯島2-31-14（湯島ファーストジェネシスビル3階）；2024-01-04 登记地址中删去了楼名。公司于 [2019-09-04](https://acesinc.co.jp/news/post-908) 和 [2021-02-17](https://acesinc.co.jp/news/post-768) 公布过办公室搬迁。

**项目与奖项。** 参加的项目：AWS Activate（[2018-07-01](https://acesinc.co.jp/news/post-952)）、Microsoft for Startups（[2019-08-13](https://acesinc.co.jp/news/post-915)）、NVIDIA Inception（[2020-02-05](https://acesinc.co.jp/news/post-875)），以及软银的 ONE SHIP 合作伙伴计划（[2020-12-03](https://acesinc.co.jp/news/post-868)）。[公司概要](https://acesinc.co.jp/company-profile)列出的奖项有：HONGO AI 2019（HONGO AI AWARD 和フジタ賞）；Plug and Play Japan Fall Summit 2020 IoT 部门 Japan Session Award；国土交通省关东地方整备局的令和3年度 新技術推進技術者表彰；週刊東洋経済「すごいベンチャー100」（2020）；与 JFEE（公司原文写法）共同开发的钢筋检查 AI 在国土交通省创新技术试点中获最高评价（令和元年度）；ILS TOP100 Startups（2022）；以及 CEO 入选 Forbes 30 Under 30 Asia 2022。ACES Meet 获得 AIsmiley AI PRODUCTS AWARD 会议纪要 AI 部门大奖（[2024-04-16](https://prtimes.jp/main/html/rd/p/000000083.000044470.html)）。

### 公司陈述的市场背景

- 在招聘资料中，公司把机会归因于日本人口减少，并称这要求社会从劳动密集型转向资本和知识密集型。资料引用了麦肯锡对 AI 软件与服务市场的预测。资料还称，企业内部约 90% 的重要数据是“非公開・非構造”（非公开、非结构化）的，通用 LLM 无法学习或引用（[HR 资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)）。
- 职位描述称日本 AI 项目的成功率为 3%（“日本のAI導入PJが成功率3%”），而 ACES 有 87% 的项目在 PoC 之后继续推进（[Software Engineer 职位](https://open.talentio.com/r/1/c/aces/pages/81333)；无日期，访问于 2026-10-11）。公司介绍资料将其与“一般的なAI/DX PJ”（一般 AI/DX 项目）的 43% 对比，但未注明来源（[公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao)；2026-07-02 修改版）。

---

## 产品

### 业务线

[公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao)（2026-07-02 修改版）描述了建立在同一套自研 AI 模块之上的两项业务：

| 业务 | 销售内容 | 合同形式 | 来源 |
|---|---|---|---|
| DX Partner（DXパートナー） | 面向特定客户，从咨询到定制开发和运营：AI 战略与 AI CoE 支持；构建“AI OS”（AgentOps、Expertise/MLOps、DataOps）；围绕 AI 重新设计业务流程。典型阶段为 3–6 个月咨询、3–6 个月 PoC 与定制 AI 开发、6 个月以上运营或业务合作，合计约 1.5 年以上 | プロジェクト実行契約＋AIライセンス契約（项目合同加 AI 许可） | [DX Partner 页面](https://acesinc.co.jp/dxpartner)、[公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) |
| AI 软件（AIソフトウェア） | 跨行业 SaaS；目前为 ACES Meet | AIライセンス契約（AI 许可） | [公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao)、[ACES Meet](https://meet.acesinc.co.jp/) |

DX Partner 页面列出的打包方案有：自社専用生成AI導入（企业专属生成式 AI 导入）、RAG精度改善（RAG 精度改进；[2025-09-02](https://prtimes.jp/main/html/rd/p/000000104.000044470.html)）、VoC活用（客户声音分析，以“ACES Meeting Intelligence”名称销售；[2026-02-13](https://prtimes.jp/main/html/rd/p/000000112.000044470.html)）和安全管理DX（安全管理 DX；[2025-10-07](https://prtimes.jp/main/html/rd/p/000000108.000044470.html)）。该页面称其项目经验主要集中在金融和制造业（[DX Partner 页面](https://acesinc.co.jp/dxpartner)；无日期，访问于 2026-10-11）。

### AI OS 模块分层

据 [HR 资料（2026-07-30）](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)和[技术页面](https://acesinc.co.jp/technologies)中的图示：

| 层 | 公司所述作用 | 列出的模块 |
|---|---|---|
| Data Layer | 把原始视频、音频和业务数据转换为 AI 可读的数据 | 文档整形 AI、副语言分析 AI、多摄像头行为追踪、戴口罩人脸识别、表情与视线分析、多说话人语音识别、作业工序分析、损伤检测 |
| Knowledge Layer | 赋予结构化数据含义，并将其转化为知识或调优后的模型 | 隐私遮蔽、话语分类、损伤价值评估、学习型语音识别、QA 抽取、行为分析、RAG 推理平台、学习型说话人识别 |
| Agent Layer | 把业务流程拆分为 AI 可执行的单元 | AI 认证/授权平台；会议纪要、合规审计、眼镜推荐、销售提案、对话导航、安全支持、销售预测/采购优化等 agent |

### ACES Meet

ACES Meet 记录线上和线下会议，进行转写、摘要和分析，并把结果推送到 CRM 等系统（[产品网站](https://meet.acesinc.co.jp/)；无日期，访问于 2026-10-11）。产品网站称，与“LLM技術を応用した音声認識モデル”（基于 LLM 技术的语音识别模型）相比，转写需要修改的地方约减少 40%，但未说明比较对象。一位 AI 工程经理写道，ACES Meet 自 2022 年 3 月前后一直使用自研语音识别系统（[技术博客，2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000)）。

| 日期 | 变化 | 来源 |
|---|---|---|
| 2021-11-24 | 作为面向线上商谈的销售支持 AI 工具推出 β 版 | [公告](https://acesinc.co.jp/news/post-728) |
| 2022-03-17 | 正式提供，具备说话人分离、表情分析和 Salesforce 集成 | [公告](https://acesinc.co.jp/news/post-701) |
| 2022-10-11 | 集成 Google Meet 和 Microsoft Teams | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000039.000044470.html) |
| 2023-03-22 | 使用 ChatGPT 的“AIまとめ”自动摘要 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000051.000044470.html) |
| 2023-04-06 | 逐次分析与实时转写 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000054.000044470.html) |
| 2023-08-30 | 线下面对面会议的分说话人音频分析和纪要 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000069.000044470.html) |
| 2025-03-14 | 与人才中介行业核心系统 CAREERPLUS（Brain Lab）集成 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000098.000044470.html) |
| 2025-07-04 | 词典功能（β 版）：客户登记术语，模型按企业追加训练 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000101.000044470.html) |
| 2025-08-20 | ACES Meet API：会议搜索、会议信息、转写、AI 摘要与分析。此前已有 Salesforce、HubSpot 和 Slack 的标准集成 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000103.000044470.html) |
| 2025-10-22 | 用于线下录音的 iOS 应用（Android 版计划中）；单次最长 3 小时；音频 30 天后从设备删除，且无法导出 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000107.000044470.html) |
| 2026-07-28 | 取得 ISO/IEC 27017 登记，覆盖 ACES Meet 及其对 AWS 和 Auth0 的使用 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000120.000044470.html) |

产品网站及其案例页面提到的客户包括 Sales Marker、IDOM、Stech&Co.、インゲージ、RAKUS 和日本レコードマネジメント（[产品网站](https://meet.acesinc.co.jp/)；无日期，访问于 2026-10-11）。

### 其他产品及现状

| 产品 | 发布 | 内容 | 当前状态 |
|---|---|---|---|
| SHARON | [2019-05-22](https://acesinc.co.jp/news/post-930) | 以人体感知为重点的嵌入式图像识别算法包 | 当前公司网站未提及 |
| Deep Nine | [2020-06-01](https://acesinc.co.jp/news/post-854) | 与电通、GAORA 和共同通信数码合作开发的棒球姿态估计应用 | 当前公司网站未提及 |
| ACES ChatHub | [2023-06-02](https://prtimes.jp/main/html/rd/p/000000061.000044470.html) | 企业版 ChatGPT 聊天机器人平台，后迁移到 Azure OpenAI Service（[2023-07-19](https://prtimes.jp/main/html/rd/p/000000065.000044470.html)），并增加了内部数据引用功能（[2023-10-17](https://prtimes.jp/main/html/rd/p/000000074.000044470.html)） | 未列入当前 AI 软件产品；未发现停止服务的公告 |
| AUX Checker | [2024-08-09](https://prtimes.jp/main/html/rd/p/000000089.000044470.html) | 与 SOMPOオークス 共同开发的车辆损伤检测应用；自 2024 年 9 月起与 Ichinen 进行为期一年的商业化 PoC | — |
| AUX Pricing | [2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html) | 与オークスモビリティ共同开发、面向经销商的事故车定价应用 | 公布价格：每年 12 万日元 |

### 商业化

- ACES Meet 没有公开价目表。其[服务条款](https://meet.acesinc.co.jp/terms/)（制定 2021-10-20）规定，费用按网站公布或另行规定的价目表执行，每个用户账户设定一份许可。产品网站引导访客填写咨询表单。
- DX Partner 业务以项目合同加 AI 许可合同的形式销售。公司称，开发出的算法和数据在内部积累并模块化，再以许可形式提供给客户（[Algorithm Engineer/Manager 职位](https://open.talentio.com/r/1/c/aces/pages/94487)；无日期，访问于 2026-10-11）。
- AUX Pricing 是唯一找到公开价格的产品（每年 12 万日元；[2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html)）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2020-12-03 | 自成立以来在体育、零售、建筑和汽车领域开展联合 DX 项目 | [公告](https://acesinc.co.jp/news/post-782) |
| “〜2024”（至 2024 年） | 10–40 人；描述为“コンサル中心の個人商店”（以咨询为中心的个体作坊式经营） | [HR 资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| 无日期 | DX Partner“前年度150%”（为上一年度的 150%） | [Software Architect 职位](https://open.talentio.com/r/1/c/aces/pages/104805)；访问于 2026-10-11 |
| 无日期 | DX Partner“前年比160%以上”（为上一年的 160% 以上），需求以大型金融机构为主 | [FDE 职位](https://open.talentio.com/r/1/c/aces/pages/123475)；访问于 2026-10-11 |
| 2026-07-30 | DX Partner“前年比190%”；正式员工 70 人，总计约 110 人 | [HR 资料](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| 无日期 | SMBC-GAI：为三井住友银行内部生成式 AI 做文档结构化和 RAG 改进，已推广至全体员工；约节省 5 万工时 | [AI Engineer 职位](https://open.talentio.com/r/1/c/aces/pages/22022)、[公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) |

上述增长数字均未说明基准指标（收入、订单或项目数）。

### 已公布客户与合作伙伴

| 日期 | 对象 | 公布内容 |
|---|---|---|
| [2018-06-19](https://acesinc.co.jp/news/post-954) | エムスリー | 深度学习算法开发 |
| [2020-08-27](https://acesinc.co.jp/news/post-816) | Zoff | 零售 DX 业务合作；之后为 Zoff Virtual Counter 提供推荐引擎（[2021-11-25](https://acesinc.co.jp/news/post-720)） |
| [2020-09-09](https://acesinc.co.jp/news/post-806) | JFEE / 国土交通省 | 钢筋检查 AI 在国土交通省试点中获最高评价；无人机版本于 [2023-02-15](https://prtimes.jp/main/html/rd/p/000000047.000044470.html) 完成开发与验证 |
| [2020-09-29](https://acesinc.co.jp/news/post-803) | 陸上自衛隊（JGSDF） | 达成由 ACES 就 AI 运用提供建议的协议 |
| [2022-01-26](https://acesinc.co.jp/news/post-711) | バンダイナムコ研究所 | AI 角色动作生成的联合研发；之后出售动作数据集 |
| [2022-05-26](https://acesinc.co.jp/news/post-536) | SOMPO Light Vortex（SOMPO HD） | 资本业务合作；把 AI 用于事故车和二手车 B2B 拍卖。ACES 称自 2019 年起已与 SOMPO 控股合作 |
| [2022-09-14](https://prtimes.jp/main/html/rd/p/000000038.000044470.html) | 大同生命 | 使用 ACES Meet 的销售分析项目 |
| [2022-12-22](https://prtimes.jp/main/html/rd/p/000000043.000044470.html) | 電源開発（J-POWER） | 图像 AI 安全管理系统：统计高处或开口部附近的作业人数、检测梯子作业、检测接近开口部 |
| [2023-10-13](https://prtimes.jp/main/html/rd/p/000000073.000044470.html) | 経済産業省（METI） | 关于行政领域 LLM 运用的项目；在 Azure 上试行提供 ACES ChatHub |
| [2025-04-23](https://prtimes.jp/main/html/rd/p/000000099.000044470.html) | YKK AP | 不安全行为与未佩戴防护装备检测的试点导入完成；自 2025 财年起全公司推广 |
| [2026-02-20](https://prtimes.jp/main/html/rd/p/000000113.000044470.html) | 三井住友銀行（SMBC） | ACES 以三井住友银行 AI 开发伙伴身份在 SMBC Group RisingX 2026 上发表 |
| [2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html) | 三井住友銀行（SMBC） | 共同开发的法人营业人员 AI 应用已投入使用：根据面谈内容及该行特有的产品与营业知识，提示可能的课题和产品 |

DX Partner 页面还提到公司参加了与时任首相石破茂的 AI 运用“車座”（座谈会）（[DX Partner 页面](https://acesinc.co.jp/dxpartner)；无日期，访问于 2026-10-11）。

### 公开计划

- 招聘网站的战略页面称，公司目标是从日本领先的“AIとの協働を実現させるAIソリューション企業”（实现与 AI 协作的 AI 解决方案企业）转变为“次世代のビジネスプロセスを生み出す、AI事業投資会社”（创造下一代业务流程的 AI 事业投资公司）（[战略页面](https://recruit.acesinc.co.jp/strategy)；无日期，访问于 2026-10-11）。
- IR/经营企划职位列出的后续工作包括 IPO 准备、M&A 与 PMI、扩充 AI 模块以及事業複線化（增加业务线）（[IR 职位](https://open.talentio.com/r/1/c/aces/pages/124609)；无日期，访问于 2026-10-11）。
- 公司介绍资料称，ACES 的目标是成为用可组合模块构建专家 AI 及其 AI OS 的“和製Palantir”（日本版 Palantir）（[公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao)；2026-07-02 修改版）。
- HR 资料称，在本财年及下一财年上半年，管理层将把组织建设置于销售增长之前（“売上成長 < 組織力強化”）（[HR 资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)）。

---

## 创始人

**田村 浩一郎（Koichiro Tamura）**：联合创始人、代表取締役 CEO（[公司概要](https://acesinc.co.jp/company-profile)）。

- 1993 年出生（[Green 公司访谈](https://www.green-japan.com/company/9285/interview)；无日期，访问于 2026-10-11）。
- 在东京大学大学院工学系研究科（松尾研究室）研究深度学习在金融工程中的应用。他在经营公司的同时用三年时间取得工学博士学位（[公司概要](https://acesinc.co.jp/company-profile)）。
- 在 2023 年的一次访谈中，他说 ACES 于 2017 年成立，起因是 Transformer 论文发表后他与一位朋友讨论出的想法：与出版社合作，用 AI 翻译日本漫画。该项目搁浅后，团队转向 DX 业务（[kigyolog 访谈，2023-02-07](https://kigyolog.com/interview.php?id=207)）。
- 入选 Forbes 30 Under 30 Asia 2022 Enterprise Technology 类别（[2022-05-26](https://acesinc.co.jp/news/post-522)）。

**联合创始人。** 职位描述称六名创始人中有五人是工程师（[Software Engineer 职位](https://open.talentio.com/r/1/c/aces/pages/81333)）。Wantedly 称六人中有三人出自松尾研究室（[Wantedly](https://www.wantedly.com/companies/acesinc)；无日期，访问于 2026-10-11）。下表中除三田村出自一篇博客外，其余人员在 [HR 资料（2026-07-30）](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)中均标为 Co-Founder。

| 姓名 | 原文职务 | 公开背景 |
|---|---|---|
| 與島 仙太郎 | 取締役 COO、Co-Founder | 东京大学系统创成学专业硕士（2019）；读研期间共同创立 ACES；以项目经理身份负责多项联合研究（[公司概要](https://acesinc.co.jp/company-profile)） |
| 中川 大海 | 執行役員、Co-Founder | 东京大学工学博士；WI 2019 Best Student Paper Award；负责业务开发 |
| 久保 静真 | 執行役員、Co-Founder | 东京大学（松尾研究室）硕士；负责包括深度学习在内的算法开发和基础设施设计的管理。2021 年以开发部负责人身份署名了技术博客的第一篇文章（[2021-09-24](https://tech.acesinc.co.jp/entry/2021/09/24/104953)） |
| 西條 真史 | 執行役員、Co-Founder | 庆应义塾大学 SFC；乐天（二手交易应用ラクマ的业务开发与市场营销）；负责 AI 软件业务 |
| 三田村 | 联合创始人 / 软件工程师 | 见于一篇 [2026-03-19 博客](https://tech.acesinc.co.jp/entry/2026/03/19/083000)中的自我介绍；文中未写名字 |

**其他管理层与治理**（[公司概要](https://acesinc.co.jp/company-profile)、[HR 资料](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)）：

- **小松原 龍介**：取締役 CFO。曾任职于 KPMG AZSA（审计）和 IGPI（战略、本金投资、M&A 咨询、企业重组）。
- **川上 登福**：外部董事。IGPI 合伙人、董事总经理，日本深度学习协会理事。他在 2019 年种子轮时成为顾问，在 2020 年那轮融资时成为董事（[2020-12-03](https://acesinc.co.jp/news/post-782)）。
- **新原 浩朗**：自 [2025-05-14](https://prtimes.jp/main/html/rd/p/000000100.000044470.html) 起任外部董事。曾任经济产业省经济产业政策局长和内阁官房内阁审议官；2024-09-30 从政府退休。
- **技术顾问**：松尾 豊（东京大学；自 [2019 年种子轮](https://acesinc.co.jp/news/post-930)起任顾问）和染谷 隆夫（东京大学；[2023-04-27](https://prtimes.jp/main/html/rd/p/000000058.000044470.html)）。沢田 渉（IGPI 高级执行研究员，曾任职于三井住友银行）于 [2023-10-04](https://prtimes.jp/main/html/rd/p/000000072.000044470.html) 成为顾问。
- **监事**：一名于 2021-08 就任的常勤监事，其履历称他曾参与 Ricksoft 2019 年在东证 Mothers 上市的准备工作；另有分别于 2022-06 和 2024-06 就任的外部监事。
- HR 资料中的其他执行董事：山本 豊（交付负责人）和佐久間 桂吾（associate partner；曾任职于 NTT Data 和 AWS）。

HR 资料中的管理部门组织图显示，HR 团队有四人，另有经营企划/IR、会计与财务、总务与劳务、法务，以及 IT/企业工程等职能。

---

## 融资

| 日期 | 轮次（公司原文） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2019-05-22 | シードラウンド（第三者割当増資） | 数千万円（数千万日元） | Deep30投資事業有限責任組合；株式会社経営共創基盤（IGPI） | — | [ACES](https://acesinc.co.jp/news/post-930)、[BRIDGE](https://thebridge.jp/2019/05/sharon) |
| 2020-12-03 | 資金調達（无轮次名称；由 IGPI 和 Deep30 认购） | 約3.2億円（约 3.2 亿日元） | IGPI；Deep30 | 未说明 | [ACES](https://acesinc.co.jp/news/post-782) |
| 2022-05-26 | 資本業務提携（资本业务合作） | 未披露 | SOMPO Light Vortex株式会社（SOMPO 控股全资子公司） | 未说明 | [ACES](https://acesinc.co.jp/news/post-536) |

- 2019 年那轮用于 SHARON 的研发和招聘。2020 年那轮的资金用途被描述为扩大算法许可和软件业务（[2019-05-22](https://acesinc.co.jp/news/post-930)、[2020-12-03](https://acesinc.co.jp/news/post-782)）。
- IGPI 认购了 2019 年和 2020 年两轮。IGPI 合伙人川上 登福担任外部董事，CFO 小松原 龍介曾在 IGPI 任职。未公布持股比例。
- 在公司新闻索引和 [PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/44470) 上均未发现 2022-05-26 之后的融资公告。

**财务数据。** 公司不公布收入。一个汇总官报（官報）決算公告的数据库显示了两个年度的数据（[catr.jp](https://catr.jp/companies/cd880/160167)）；未查阅官报原件：

| 财年结束日 | 净利润 | 留存收益 | 总资产 |
|---|---|---|---|
| 2020-09-30 | 762.9 万日元 | 2,148.6 万日元 | 1.51214 亿日元 |
| 2021-09-30 | 3,654.2 万日元 | 3,786.0 万日元 | 4.61989 亿日元 |

---

## 工程

### 技术栈与平台

**由公司技术文章确认**（[技术博客](https://tech.acesinc.co.jp/)）：

- **语言：** Python 和 JavaScript/TypeScript，公司称为主要开发语言（[2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123)）。
- **ACES Meet 后端：** Python/Django（[2025-02-28](https://tech.acesinc.co.jp/entry/2025/02/28/080000)）。
- **ACES Meet 前端：** Next.js、React 和 TypeScript。Next.js 于 2025 年 1 月升级到 v15 并迁移到 App Router（[2025-01-31](https://tech.acesinc.co.jp/entry/2025/01/31/083000)）。
- **AWS：** 2022 年 ACES Meet 的监控对象包括 ALB、Fargate/ECS、SQS、SageMaker、AWS Batch 和 RDS（[2022-04-12](https://tech.acesinc.co.jp/entry/2022/04/12/122321)）。GPU 推理运行在通过 AWS Batch 启动的 GPU 实例上，模型权重打包在从 ECR 拉取的 Docker 镜像中（[2025-02-07](https://tech.acesinc.co.jp/entry/2025/02/07/083000)）。会议列表搜索使用 Elasticsearch（[2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130)）。Aurora Blue/Green 部署被列为部署安全工作的一部分（[2025-01-10](https://tech.acesinc.co.jp/entry/2025/01/10/083000)）。ACES 为每个客户或产品使用单独的 AWS 账户，用 AWS Organizations 管理，并通过 Transit Gateway 连接到共享服务账户（[2021-10-18](https://tech.acesinc.co.jp/entry/2021/10/18/144813)、[2022-04-12](https://tech.acesinc.co.jp/entry/2022/04/12/122321)）。
- **可观测性：** 跨 AWS 账户的 Grafana 加 CloudWatch（2022 年）；Sentry，包括基于 trace 的 N+1 查询检测（[2026-03-18](https://tech.acesinc.co.jp/entry/2026/03/18/083000)）。
- **身份：** 认证使用 Auth0，其配置用 Terraform 管理（[2025-06-13](https://tech.acesinc.co.jp/entry/2025/06/13/083000)）。2026 年 8 月中旬上线的新授权平台用 Cerbos 取代了应用内的权限检查；选型对比表称其只需在现有 ECS 中添加一个 sidecar（[2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130)）。
- **CI 与供应链：** GitHub Actions（matrix 并行测试）、Dependabot 和 Renovate，Actions 固定到 commit SHA（[2024-12-13](https://tech.acesinc.co.jp/entry/2024/12/13/083000)、[2025-01-31](https://tech.acesinc.co.jp/entry/2025/01/31/083000)、[2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123)）。
- **Azure：** ACES ChatHub 和经济产业省项目的 LLM 环境构建在 Microsoft Azure 上，使用 Azure OpenAI Service（[2023-07-19](https://prtimes.jp/main/html/rd/p/000000065.000044470.html)、[2023-10-13](https://prtimes.jp/main/html/rd/p/000000073.000044470.html)）。
- **机器学习：** 内部包 `aces-vision` 以统一接口实现了数十个图像和视频深度学习模型，训练写法“像 PyTorch Lightning 一样”。产品之下有一个名为“ACES Platform”的内部 API 平台（[2021-09-24](https://tech.acesinc.co.jp/entry/2021/09/24/104953)）。ACES Meet 的摘要功能使用 ChatGPT API（[2023-04-28](https://tech.acesinc.co.jp/entry/2023/04/28/130729)）。
- **内部 AI 工具：** ChatGPT Enterprise、Claude Enterprise 和 Cursor Enterprise 已向约 150 人开放，包括业务人员、实习生和外包人员（[2026-03-19](https://tech.acesinc.co.jp/entry/2026/03/19/083000)）。2026 年的两份资料列出了 Cursor、Claude/Claude Code 和 Codex，招聘网站列出了 GitHub Copilot 和 Dify。

**职位中列出（DX Partner），公司注明为主要工具，并按项目选型**（[Software Engineer](https://open.talentio.com/r/1/c/aces/pages/81333)、[Software Architect](https://open.talentio.com/r/1/c/aces/pages/104805)；无日期，访问于 2026-10-11）：Python/TypeScript；Django、Flask、FastAPI、React；Linux；AWS/Azure；Docker、Terraform；GitHub；Notion；Slack、Zoom。AI 工程师职位列出 Python 和 PyTorch（[AI Engineer](https://open.talentio.com/r/1/c/aces/pages/22022)）。软件工程实习职位另外列出 Next.js，并把 PostgreSQL/MySQL/NoSQL 和 AWS/GCP 列为优先经验（[实习职位](https://open.talentio.com/r/1/c/aces/pages/120817)）。

**公开代码仓库。** GitHub 组织 [`aces-inc`](https://github.com/aces-inc)（名称“ACES”，blog 字段为 acesinc.co.jp，创建于 2018-10-16）有 14 个公开仓库。其中 13 个是 fork，包括 ESPnet、Dify、Redash、RT-DETR、Style-Bert-VITS2 和 ndkale（一个 SQS 任务 worker）。唯一的原创仓库 `mysql-utf8mb4` 最后一次推送在 2021-09-07（GitHub API；访问于 2026-10-11）。

### 系统

| 系统 | 功能 | 来源 |
|---|---|---|
| ACES Meet 分析流水线 | 把录制的会议音视频分析成转写、摘要和统计数据；语音识别为自研，推理运行在通过 AWS Batch 启动的 GPU 实例上 | [2025-02-07](https://tech.acesinc.co.jp/entry/2025/02/07/083000)、[2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000) |
| ACES Meet 集成 | Salesforce 字段自动填写、HubSpot、Slack、CAREERPLUS；会议数据 API | [2025-08-20](https://prtimes.jp/main/html/rd/p/000000103.000044470.html)、[产品网站](https://meet.acesinc.co.jp/) |
| ACES Meet 安全控制 | IP 白名单、MFA、数据库加密、禁止服务器环境的外部连接、外部机构漏洞检测；视频数据只能由程序访问 | [安全页面](https://meet.acesinc.co.jp/security/)；无日期，访问于 2026-10-11 |
| 多租户授权 | Cerbos 策略引擎；把 Cerbos PlanResources API 返回的授权条件转换为会议列表的 Elasticsearch 查询；迁移采用双写，并在切换前与旧检查并行运行比对 | [2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130) |
| 安全管理 AI | 利用现有监控摄像头实时检测摔倒、绊倒、未佩戴防护装备、探身和接近危险区域，配有告警、数据库和仪表盘 | [2025-10-07](https://prtimes.jp/main/html/rd/p/000000108.000044470.html)、[YKK AP](https://prtimes.jp/main/html/rd/p/000000099.000044470.html) |
| 车辆损伤与定价 | 从八个方向拍摄的照片中检测损伤，结果输入用オークスモビリティ销售数据（每年约 5 万辆事故车）训练的价格模型 | [2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html) |
| 企业 RAG 与知识结构化 | 把含有复杂图表和版式的文档转换为 AI 可读数据；SMBC-GAI 的 RAG 改进；三井住友银行法人营业应用 | [DX Partner 页面](https://acesinc.co.jp/dxpartner)、[2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html) |
| 抽象化遮蔽 | 已获专利的基于 LLM 的技术，把机密实体替换为抽象描述（例如“大手金融機関”，大型金融机构），而不是直接涂黑 | [项目页面](https://acesinc.co.jp/projects/6EUJ3NeF)；无日期，访问于 2026-10-11 |

公司公布的已授权专利：基于视频的非语言信息分析（[2021-11-24](https://acesinc.co.jp/news/post-733)）；多说话人线上商谈的自动摘要（[2023-03-09](https://prtimes.jp/main/html/rd/p/000000050.000044470.html)）；使用大规模模型的行为识别（[2024-02-13](https://prtimes.jp/main/html/rd/p/000000081.000044470.html)）；说话人分类（[2024-07-23](https://prtimes.jp/main/html/rd/p/000000088.000044470.html)）；对话视频中的多模态重要场景提取（[2024-12-13](https://prtimes.jp/main/html/rd/p/000000093.000044470.html)）。

### 招聘所需技术背景

来自 [Talentio 招聘页](https://open.talentio.com/r/1/c/aces/homes/2662)（21 个开放页面；无日期，访问于 2026-10-11）：

- **Software Engineer / Software Architect / FDE（必须）：** 从设计、实现到测试的完整 Web 应用开发经验；在 AWS 或 Azure 上构建和运维系统；代码审查和 CI/CD；能独立把业务需求转化为解决方案。职位明确说明不要求 AI/ML 知识和 Python 经验。**优先：** 开发过使用 AI/ML 的系统；设计或运维过业务系统或大型 Web 应用；用 Terraform 或 Docker 做基础设施自动化；技术负责人或架构经验；性能调优与日志设计。FDE 岗位还包括售前阶段的客户工作，以及把系统推进到投产和落地（[FDE](https://open.talentio.com/r/1/c/aces/pages/123475)）。
- **AI Engineer（必须）：** 机器学习、深度学习或数理统计的深厚知识；有过查阅文献、把没有明确定义的问题从假设推进到实现的经历；理工科硕士或博士学位，或同等的研究能力。**优先：** 从零实现论文并打包成 Python 库；论文发表；Kaggle 或竞技编程成绩；边缘计算或模型加速（[AI Engineer](https://open.talentio.com/r/1/c/aces/pages/22022)）。
- **Algorithm Engineer/Manager（必须）：** ML/DL 开发或研究；面向客户、从需求到运维的 AI 系统工作；管理 AI 工程团队；商务级日语。**优先：** 论文或专利、Kaggle、MLOps、项目管理（[职位](https://open.talentio.com/r/1/c/aces/pages/94487)）。
- **外包软件工程师（必须）：** 3 年以上 TypeScript 和 React 经验，2 年以上在 AWS、Azure 或客户本地环境开发的经验（[职位](https://open.talentio.com/r/1/c/aces/pages/115624)）。

### 行业领域

具名项目涉及银行（三井住友银行）、保险（SOMPO、大同生命）、制造和能源现场安全（YKK AP、J-POWER）、汽车后市场拍卖（オークスモビリティ）、人才中介（Brain Lab 的 CAREERPLUS）以及政府（经济产业省、陆上自卫队）。DX Partner 页面称其经验主要集中在金融和制造业。所查阅的工程职位均不要求事先具备行业知识。软件类职位说明不要求 AI 经验，IT Consultant 职位说明不要求 AI 知识（[IT Consultant](https://open.talentio.com/r/1/c/aces/pages/78619)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 所有职位和招聘网站均为日文。Algorithm Engineer/Manager 职位要求商务级日语，非母语者需相当于 JLPT N1。Green 给 Algorithm Engineer 职位打了“多国籍な職場”（多国籍职场）标签。未发现英文职位 | [职位](https://open.talentio.com/r/1/c/aces/pages/94487)、[Green](https://www.green-japan.com/company/9285/job/188942) |
| 地点 | 东京文京区汤岛总部 | [Software Engineer 职位](https://open.talentio.com/r/1/c/aces/pages/81333) |
| 远程 | 招聘网站：混合办公，每周两天远程；到岗时间和日期自由。职位：“リモート相談可能”（远程可协商）。外包岗位：按项目远程或到场 | [招聘网站](https://recruit.acesinc.co.jp/)、[外包职位](https://open.talentio.com/r/1/c/aces/pages/115624) |
| 工作时间 | 弹性工作制，核心时间 11:00–15:00 | [招聘网站](https://recruit.acesinc.co.jp/) |
| 雇用形式 | 正式员工（每周 40 小时以上；每年两次按产出发放奖金）；面向在职博士生的短时正式员工（每周 30 小时以上，每月 120 小时，奖金、股票期权和福利与全职相同）；长期实习生（每周 15 小时以上） | [工作方式页面](https://recruit.acesinc.co.jp/workstyle)、[博士 AI Engineer 职位](https://open.talentio.com/r/1/c/aces/pages/117320) |
| 薪资 | Software Engineer 600 万–1,000 万日元（Talentio）。Green 上：FDE/Software Engineer 850 万–1,400 万日元，Algorithm Engineer 600 万–900 万日元，HR 500 万–800 万日元。其他多数职位写“応相談”（面议）。薪酬按职种参照各自的招聘市场设定 | [Talentio](https://open.talentio.com/r/1/c/aces/pages/81333)、[Green FDE](https://www.green-japan.com/company/9285/job/310473)、[工作方式页面](https://recruit.acesinc.co.jp/workstyle) |
| 职级 | 分为执行者（P1–P4；P2 对应实习生和应届生）、专家（S1–S4）和管理者（M1–M4）三条职级线 | [工作方式页面](https://recruit.acesinc.co.jp/workstyle) |
| 休假与福利 | 周末及节假日休息；入职当天发放 13 天带薪假；允许副业；购书补贴；提供笔记本电脑和双显示器；全额交通补贴；健康检查 | [招聘网站](https://recruit.acesinc.co.jp/)、[Software Architect 职位](https://open.talentio.com/r/1/c/aces/pages/104805) |
| 员工数据 | 平均年龄 33 岁；平均加班每月 23.5 小时；57.5% 已成家；10 人休过育儿假或产假 | [工作方式页面](https://recruit.acesinc.co.jp/workstyle)；无日期，访问于 2026-10-11 |
| 招聘流程 | 书面筛选；一面（技能匹配，需事先做在线性格测试，可能有工作样本测试）；二面（价值观与文化）；背景调查后与 CEO 终面；全程约 3–4 周 | [招聘网站](https://recruit.acesinc.co.jp/)、[HR 资料](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731) |
| 学生与初级人员 | 软件和 ML 工程师的长期实习；实习之后可转入博士短时正式员工制度 | [ML 实习职位](https://open.talentio.com/r/1/c/aces/pages/55105)、[SWE 实习职位](https://open.talentio.com/r/1/c/aces/pages/120817) |
| 签证担保 | 所查阅的职位均未说明 | — |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-10-11）：公司网站（sitemap、公司概要、新闻索引、项目、DX Partner 和技术页面）、招聘网站、Talentio 上全部 21 个开放页面、ACES Meet 网站（sitemap、安全页面、条款）、技术博客（sitemap 中的 50 篇文章）、note 杂志索引、Speaker Deck（四份资料）、PR TIMES 公司页面、国税厅法人编号登记、JPX 新上市页面、GitHub 组织 `aces-inc`、Green、Wantedly、TokyoDev 和 Japan Dev（两者均无 ACES 页面）、INITIAL（仅作为线索）以及 catr.jp。检索词包括 ACES、株式会社ACES、エーシーズ、ACES Meet、ACES ChatHub 和 SHARON，覆盖日文和英文。

- **收入。** 未公布。增长只以 DX Partner 业务的同比比率出现，且未说明基准指标。找到的财务数字只有 catr.jp 汇总的 2020 和 2021 财年官报公告。
- **各轮金额与累计融资。** 2019 年种子轮金额只写作数千万円，SOMPO Light Vortex 的投资金额未披露，也未公布累计金额或持股比例。
- **IPO 时间和市场。** 公司称正在准备 IPO，但未给出目标时间或市场。
- **ACES Meet 价格。** 无公开价目表。
- **工程团队人数。** 未公布。唯一的拆分是 72 名正式员工按业务的占比（R&D 13.8%）。
- **签证担保、英文岗位、离职率。** 均未找到。
- **开源。** GitHub 组织中是 fork 和一个小型原创仓库；见“技术栈与平台”。

### 不同来源之间的不一致

- **人数：** “70”（[Talentio 职位](https://open.talentio.com/r/1/c/aces/pages/81333)、[Green](https://www.green-japan.com/company/9285)；无日期）；正式员工 72 人（[招聘网站](https://recruit.acesinc.co.jp/workstyle)；无日期）；正式员工 70 人 / 含外包和实习生约 110 人（[HR 资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)；[公司介绍资料](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao)也写 110 人）；含实习生和外包约 150 人（[技术博客，2026-03-19](https://tech.acesinc.co.jp/entry/2026/03/19/083000)）。110 和 150 两个数字的口径说明相同，但相差约 40 人。
- **DX Partner 增长：** 150%（[Software Architect 职位](https://open.talentio.com/r/1/c/aces/pages/104805)）、160% 以上（[FDE 职位](https://open.talentio.com/r/1/c/aces/pages/123475)）和 190%（[HR 资料，2026-07-30](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)），均为与“上一年”的比较。职位没有日期，无法判断它们是否对应不同财年。
- **总部地址：** [2026-02-13 公告](https://prtimes.jp/main/html/rd/p/000000112.000044470.html)写总部在東京都港区。其他所有公告、[公司概要](https://acesinc.co.jp/company-profile)和[国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856)均为文京区湯島。[Green](https://www.green-japan.com/company/9285) 仍写楼名“湯島ファーストジェネシスビル3階”，而登记已于 2024-01-04 删去该楼名；公司现在使用“ルーシッドスクエア湯島3階”。
- **ACES Meet 正式提供日期：** 2022-03-17（[公告](https://acesinc.co.jp/news/post-701)）；“2022年4月”（[ITコンサルタント 职位](https://open.talentio.com/r/1/c/aces/pages/78619)）；“2022年3月ごろから”（2022 年 3 月前后起）（[技术博客，2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000)）。
- **轮次标签：** 公司称 2019 年那轮为种子轮，之后的融资未命名。[INITIAL](https://initial.inc/companies/A-31174)（数据库）将公司标为截至 2022-05-30 的“シリーズB”，并显示了一个投后估值，但没有一手来源证实。
- **发布日期：** 同一篇公告在公司新闻索引和 PR TIMES 上的日期有时不同。例如，染谷 隆夫的任命在[新闻索引](https://acesinc.co.jp/news)上为 2023-06-03，在 [PR TIMES](https://prtimes.jp/main/html/rd/p/000000058.000044470.html) 上为 2023-04-27。本页对 PR TIMES 链接采用 PR TIMES 的日期。
- **平均年龄：** 33 岁（[招聘网站](https://recruit.acesinc.co.jp/workstyle)）与 34 岁（[Green](https://www.green-japan.com/company/9285)），均无日期。

### 其他

- 业务重心随时间变化。在 2019–2022 年的公告中，公司把自己描述为图像和视频识别、“Human Sensing”公司（[2019-05-22](https://acesinc.co.jp/news/post-930)、[2022-05-26](https://acesinc.co.jp/news/post-536)）。2025 年起的公告使用“专家 AI”和“AI OS”的说法（[2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html)、[2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html)）。
- 公司新闻索引止于 2026-03-03，之后的若干 PR TIMES 公告未收录其中，包括 2026-03-17、2026-04-24 和 2026-08-03 的公告。本页同时检查了该索引和 [PR TIMES 公司页面](https://prtimes.jp/main/html/searchrlp/company_id/44470)。
- 新闻索引中有一条 2021-06-16 的条目，标题为“一部報道について”（关于部分报道）。它链接到公司某个子域名上的 PDF，该子域名已无法解析，因此未能查阅其内容。
- 与产品相关的研究成果包括 WI 2019 Best Student Paper Award（联合创始人中川）、一篇关于 AI 辅助人才评估的 CHI 2023 案例研究（获 Honorable Case Study 奖），以及与万代南梦宫研究所合作的动作数据集论文（[新闻索引](https://acesinc.co.jp/news)）。

---

## 资料来源

**官方**

- [公司官网（日文）](https://acesinc.co.jp/) · [公司概要与成员](https://acesinc.co.jp/company-profile) · [愿景与业务](https://acesinc.co.jp/whoweare) · [技术／AI OS](https://acesinc.co.jp/technologies) · [DX Partner](https://acesinc.co.jp/dxpartner) · [项目](https://acesinc.co.jp/projects) · [遮蔽专利](https://acesinc.co.jp/projects/6EUJ3NeF)
- [新闻索引（日文）](https://acesinc.co.jp/news)
- [招聘网站（日文）](https://recruit.acesinc.co.jp/) · [工作方式](https://recruit.acesinc.co.jp/workstyle) · [战略](https://recruit.acesinc.co.jp/strategy)
- [Talentio 招聘页（日文）](https://open.talentio.com/r/1/c/aces/homes/2662)：[Software Engineer](https://open.talentio.com/r/1/c/aces/pages/81333)、[Software Architect](https://open.talentio.com/r/1/c/aces/pages/104805)、[FDE](https://open.talentio.com/r/1/c/aces/pages/123475)、[AI Engineer](https://open.talentio.com/r/1/c/aces/pages/22022)、[Algorithm Engineer/Manager](https://open.talentio.com/r/1/c/aces/pages/94487)、[IT Consultant](https://open.talentio.com/r/1/c/aces/pages/78619)、[博士 AI Engineer](https://open.talentio.com/r/1/c/aces/pages/117320)、[ML 实习](https://open.talentio.com/r/1/c/aces/pages/55105)、[SWE 实习](https://open.talentio.com/r/1/c/aces/pages/120817)、[外包 SWE](https://open.talentio.com/r/1/c/aces/pages/115624)、[IR／经营企划](https://open.talentio.com/r/1/c/aces/pages/124609)
- [ACES Meet（日文）](https://meet.acesinc.co.jp/) · [安全](https://meet.acesinc.co.jp/security/) · [条款](https://meet.acesinc.co.jp/terms/)
- [ACES Developer's Blog（日文）](https://tech.acesinc.co.jp/)：[开发概要，2021-09-24](https://tech.acesinc.co.jp/entry/2021/09/24/104953) · [Transit Gateway，2021-10-18](https://tech.acesinc.co.jp/entry/2021/10/18/144813) · [Grafana + CloudWatch，2022-04-12](https://tech.acesinc.co.jp/entry/2022/04/12/122321) · [ChatGPT API 摘要，2023-04-28](https://tech.acesinc.co.jp/entry/2023/04/28/130729) · [ACES Meet 开发理念，2024-12-13](https://tech.acesinc.co.jp/entry/2024/12/13/083000) · [技术负责人的使命，2025-01-10](https://tech.acesinc.co.jp/entry/2025/01/10/083000) · [依赖库更新／Next.js，2025-01-31](https://tech.acesinc.co.jp/entry/2025/01/31/083000) · [GPU 成本，2025-02-07](https://tech.acesinc.co.jp/entry/2025/02/07/083000) · [Python/Django，2025-02-28](https://tech.acesinc.co.jp/entry/2025/02/28/080000) · [Auth0，2025-06-13](https://tech.acesinc.co.jp/entry/2025/06/13/083000) · [发布安全，2026-03-18](https://tech.acesinc.co.jp/entry/2026/03/18/083000) · [企业版 AI 工具，2026-03-19](https://tech.acesinc.co.jp/entry/2026/03/19/083000) · [供应链安全方针，2026-03-31](https://tech.acesinc.co.jp/entry/2026/03/31/181123) · [语音识别，2026-07-27](https://tech.acesinc.co.jp/entry/2026/07/27/070000) · [Cerbos 迁移，2026-09-09](https://tech.acesinc.co.jp/entry/2026/09/09/125130)
- [ACES note 杂志（日文）](https://note.acesinc.co.jp/m/m31330dc74c51)
- [Speaker Deck（日文）](https://speakerdeck.com/aces)：[公司介绍资料（发布于 2023-12-18，修改于 2026-07-02）](https://speakerdeck.com/aces/aceshui-she-shuo-ming-zi-liao) · [HR 候选人资料（2026-07-30）](https://speakerdeck.com/aces/hou-bu-zhe-xiang-ke-hr-mian-tan-zi-liao-v1-dot-1-20260731)
- [GitHub 组织](https://github.com/aces-inc)

**新闻稿（公司网站，日文，较新在前）**

- [Forbes 30 Under 30 Asia 2022——2022-05-26](https://acesinc.co.jp/news/post-522)
- [与 SOMPO Light Vortex 资本业务合作——2022-05-26](https://acesinc.co.jp/news/post-536)
- [ISMS（ISO/IEC 27001）——2022-04-21](https://acesinc.co.jp/news/post-564)
- [ACES Meet 正式提供——2022-03-17](https://acesinc.co.jp/news/post-701)
- [与万代南梦宫研究所联合研发——2022-01-26](https://acesinc.co.jp/news/post-711)
- [Zoff 推荐引擎——2021-11-25](https://acesinc.co.jp/news/post-720)
- [ACES Meet β 版——2021-11-24](https://acesinc.co.jp/news/post-728) · [非语言分析专利——2021-11-24](https://acesinc.co.jp/news/post-733)
- [办公室扩大搬迁——2021-02-17](https://acesinc.co.jp/news/post-768)
- [从 IGPI 和 Deep30 融资 3.2 亿日元——2020-12-03](https://acesinc.co.jp/news/post-782) · [ONE SHIP——2020-12-03](https://acesinc.co.jp/news/post-868)
- [陆上自卫队顾问协议——2020-09-29](https://acesinc.co.jp/news/post-803)
- [JFEE 钢筋检查 AI——2020-09-09](https://acesinc.co.jp/news/post-806)
- [Zoff 业务合作——2020-08-27](https://acesinc.co.jp/news/post-816)
- [Deep Nine——2020-06-01](https://acesinc.co.jp/news/post-854)
- [NVIDIA Inception——2020-02-05](https://acesinc.co.jp/news/post-875)
- [企业识别更新与办公室搬迁——2019-09-04](https://acesinc.co.jp/news/post-908)
- [Microsoft for Startups——2019-08-13](https://acesinc.co.jp/news/post-915)
- [种子轮与 SHARON——2019-05-22](https://acesinc.co.jp/news/post-930)
- [AWS Activate——2018-07-01](https://acesinc.co.jp/news/post-952)
- [与エムスリー的算法开发——2018-06-19](https://acesinc.co.jp/news/post-954)

**PR TIMES（日文，较新在前）**——[公司页面](https://prtimes.jp/main/html/searchrlp/company_id/44470)

- [ACES Meet 取得 ISO/IEC 27017——2026-08-03](https://prtimes.jp/main/html/rd/p/000000120.000044470.html)
- [三井住友银行法人营业 AI 应用——2026-04-24](https://prtimes.jp/main/html/rd/p/000000118.000044470.html)
- [SMBC Group RisingX 2026——2026-02-20](https://prtimes.jp/main/html/rd/p/000000113.000044470.html)
- [VoC 分析方案——2026-02-13](https://prtimes.jp/main/html/rd/p/000000112.000044470.html)
- [ACES Meet iOS 应用——2025-10-22](https://prtimes.jp/main/html/rd/p/000000107.000044470.html)
- [安全管理 DX 方案——2025-10-07](https://prtimes.jp/main/html/rd/p/000000108.000044470.html)
- [RAG 精度改进——2025-09-02](https://prtimes.jp/main/html/rd/p/000000104.000044470.html)
- [ACES Meet API——2025-08-20](https://prtimes.jp/main/html/rd/p/000000103.000044470.html)
- [ACES Meet 词典功能——2025-07-04](https://prtimes.jp/main/html/rd/p/000000101.000044470.html)
- [新原 浩朗出任外部董事——2025-05-14](https://prtimes.jp/main/html/rd/p/000000100.000044470.html)
- [YKK AP 安全项目——2025-04-23](https://prtimes.jp/main/html/rd/p/000000099.000044470.html)
- [CAREERPLUS 集成——2025-03-14](https://prtimes.jp/main/html/rd/p/000000098.000044470.html)
- [AUX Pricing——2025-02-03](https://prtimes.jp/main/html/rd/p/000000097.000044470.html)
- [重要场景提取专利——2024-12-13](https://prtimes.jp/main/html/rd/p/000000093.000044470.html)
- [AUX Checker 商业化验证——2024-08-09](https://prtimes.jp/main/html/rd/p/000000089.000044470.html)
- [说话人分类专利——2024-07-23](https://prtimes.jp/main/html/rd/p/000000088.000044470.html)
- [AIsmiley AI PRODUCTS AWARD——2024-04-16](https://prtimes.jp/main/html/rd/p/000000083.000044470.html)
- [行为识别专利——2024-02-13](https://prtimes.jp/main/html/rd/p/000000081.000044470.html)
- [ACES ChatHub 内部数据引用——2023-10-17](https://prtimes.jp/main/html/rd/p/000000074.000044470.html)
- [经济产业省 LLM 项目——2023-10-13](https://prtimes.jp/main/html/rd/p/000000073.000044470.html)
- [沢田 渉出任顾问——2023-10-04](https://prtimes.jp/main/html/rd/p/000000072.000044470.html)
- [线下会议分析——2023-08-30](https://prtimes.jp/main/html/rd/p/000000069.000044470.html)
- [ACES ChatHub 采用 Azure OpenAI——2023-07-19](https://prtimes.jp/main/html/rd/p/000000065.000044470.html)
- [ACES ChatHub 推出——2023-06-02](https://prtimes.jp/main/html/rd/p/000000061.000044470.html)
- [染谷 隆夫出任技术顾问——2023-04-27](https://prtimes.jp/main/html/rd/p/000000058.000044470.html)
- [实时转写——2023-04-06](https://prtimes.jp/main/html/rd/p/000000054.000044470.html)
- [ChatGPT 摘要——2023-03-22](https://prtimes.jp/main/html/rd/p/000000051.000044470.html)
- [多说话人摘要专利——2023-03-09](https://prtimes.jp/main/html/rd/p/000000050.000044470.html)
- [无人机钢筋检查——2023-02-15](https://prtimes.jp/main/html/rd/p/000000047.000044470.html)
- [J-POWER 安全项目——2022-12-22](https://prtimes.jp/main/html/rd/p/000000043.000044470.html)
- [Google Meet／Teams 集成——2022-10-11](https://prtimes.jp/main/html/rd/p/000000039.000044470.html)
- [大同生命项目——2022-09-14](https://prtimes.jp/main/html/rd/p/000000038.000044470.html)

**第三方报道、登记与档案**

- [国税厅法人编号公表网站——4010001187856（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=4010001187856)
- [JPX 新上市页面（日文）](https://www.jpx.co.jp/listing/stocks/new/index.html)
- [catr.jp——官报财务公告（日文）](https://catr.jp/companies/cd880/160167)
- [BRIDGE——种子轮，2019-05-29（日文）](https://thebridge.jp/2019/05/sharon)
- [kigyolog——CEO 访谈，2023-02-07（日文）](https://kigyolog.com/interview.php?id=207)
- [Green——公司页面（日文）](https://www.green-japan.com/company/9285) · [访谈（日文）](https://www.green-japan.com/company/9285/interview) · [FDE 职位（日文）](https://www.green-japan.com/company/9285/job/310473) · [Algorithm Engineer 职位（日文）](https://www.green-japan.com/company/9285/job/188942)
- [Wantedly——公司页面（日文）](https://www.wantedly.com/companies/acesinc)
- [INITIAL（日文；数据库，仅作线索）](https://initial.inc/companies/A-31174)
