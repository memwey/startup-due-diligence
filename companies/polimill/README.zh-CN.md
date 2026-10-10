# Polimill

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Polimill（Polimill株式会社，读作ポリミル；法人番号 5010401158530）是一家东京公司，设立于 2021-02-25。公司运营两款产品：**QommonsAI**（コモンズAI），面向日本地方政府及其他公共机构的生成式 AI 平台，可横跨检索已公开的行政文书，职员可在 OpenAI、Anthropic、Google 和 Preferred Networks 的模型之间切换；**Surfvote**（サーフボート），2021 年上线的社交网络式服务，用户可就社会与政策“议题”投票和评论。QommonsAI 对每个机构 1,000 个账号以内免费（[产品网站](https://info.qommons.ai/)；访问于 2026-10-11）。

- 约 1,100 个自治体、60 万名职员使用 QommonsAI（“全国約1,100自治体・60万人の職員が利用しています”，截至 2026-08-31，[产品网站](https://info.qommons.ai/)）。公司预计 2026 年 12 月达到约 1,200 个自治体、65 万名用户（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。所有数字均为公司自述。
- 最近一轮：シリーズA 约 6.35 亿日元（約6億3,500万円）——风险投资 5.2 亿日元、管理层及天使投资人约 1,500 万日元、来自大型银行（メガバンク）的债务融资 1 亿日元——公司称投后估值约 50 亿日元（[2026-01-19](https://polimill.jp/20260119-1/)）。未披露任何投资方名称。此前的プレシリーズA 使累计融资达到“5億円超え”（[2024-10-03](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)）。
- 2025 年 10 月之前公司有 4 名正式员工；2025 年 10–11 月新招 6 人（[2025-11-05](https://polimill.jp/20251105-1/)）。在 2026 年 10 月的招聘访谈中，开发部为“15名ほど”（约 15 人），整个组织为“数十人規模”（几十人）（[talk03](https://polimill.jp/interview/talk03/)、[talk02](https://polimill.jp/interview/talk02/)；2026-10-02）。
- 工程：数据保存在 AWS 东京区域，并可故障切换至大阪（[FAQ](https://info.qommons.ai/faq)；访问于 2026-10-11）。GPT 模型运行在 Azure OpenAI 日本区域（[2026-05-08](https://polimill.jp/20260508-4/)）。Web 应用经 Amazon CloudFront 返回 `x-powered-by: Next.js`（观察于 2026-10-11）。开发团队为多国籍、远程办公，共同语言为日语（“共通言語は日本語ですが多国籍”，[talk03](https://polimill.jp/interview/talk03/)）。后端职位要求非日语母语者具备 JLPT N1（[Green](https://www.green-japan.com/company/10658/job/285168)；发布于 2025-05-30）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | Polimill株式会社（登记名：Ｐｏｌｉｍｉｌｌ株式会社，フリガナ ポリミル）；网站页脚为“Polimill Co.,Ltd.” | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530)、[公司页面](https://polimill.jp/company/) |
| 法人番号 | 5010401158530；指定于 2021-03-04（令和3年3月4日） | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530) |
| 设立 | 2021-02-25（設立） | [2021-11-30](https://polimill.jp/pr20211130/)、[2026-02-25](https://polimill.jp/20260225-1/) |
| 总部 | 東京都港区虎ノ門3丁目8番27号 巴町アネックス2号館3階（2026-03-24 登记） | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530)、[公司页面](https://polimill.jp/company/) |
| 登记地址变更 | 浜松町2-2-15 浜松町ダイヤビル2F（登记时）→ 赤坂8-4-14 青山タワープレイス8F（自 2021-03-31）→ 六本木7-14-23 ラウンドクロス六本木（自 2024-04-12）→ 虎ノ門（自 2026-03-24） | [国税厅登记](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530) |
| 代表人 | 代表取締役CEO 伊藤あやめ、代表取締役COO 谷口野乃花，均于 2025 年 3 月就任 | [公司页面](https://polimill.jp/company/)、[talk01](https://polimill.jp/interview/talk01/)、[talk02](https://polimill.jp/interview/talk02/) |
| 设立时代表人 | 代表取締役 横田えり，2021 年至 2025 年 3 月的新闻稿中署名 | [2021-11-30](https://polimill.jp/pr20211130/)、[2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html) |
| 自述业务 | 「この国の社会の全体最適化」（这个国家社会的整体最优化） | [公司页面](https://polimill.jp/company/) |
| 使命 | 「のこしたいみらいをともにつくる」，在公司内部的第一回京都会議上确定 | [2025-12-05](https://polimill.jp/20251205-1/)、[about](https://polimill.jp/about/) |
| 资本金 | 6 亿日元（資本金6億円）；另一不同数字见 `备注` | [PR TIMES 公司信息栏](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)；无日期，访问于 2026-10-11 |
| 员工人数 | 4 名正式员工，另于 2025 年 10–11 月新招 6 人；2026 年 10 月称“数十人規模” | [2025-11-05](https://polimill.jp/20251105-1/)、[talk02](https://polimill.jp/interview/talk02/) |
| 工程团队工作语言 | 开发部：以日语为共同语言，成员多国籍，远程办公 | [talk03](https://polimill.jp/interview/talk03/)（2026-10-02） |
| 客户 | 截至 2026-08-31，约 1,100 个自治体、60 万名职员使用 QommonsAI | [产品网站](https://info.qommons.ai/) |
| 累计融资 | プレシリーズA 后“5億円超え”（2024-10-03）；シリーズA 约 6.35 亿日元（2026-01-19）。シリーズA 之后未公布累计总额 | [2024-10-03](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)、[2026-01-19](https://polimill.jp/20260119-1/) |
| 投资方 | 所查阅的公司新闻稿均未披露 | 见 `融资` |
| ISMS | ISO/IEC 27001:2022 / JIS Q 27001:2023，IS 823638，BSIグループジャパン，2025-10-07 登录；范围涵盖公共部门 AI 与公民 SNS | [2025-10-09](https://polimill.jp/20251009-1/) |
| QMS | ISO 9001:2015，FS 826724，BSIグループジャパン，2025-08-15 登录 | [2025-10-09](https://polimill.jp/20251009-2/) |
| 隐私标志（Pマーク） | 第10825416(01)号，JIPDEC，有效期 2025-10-01 至 2027-09-30 | [2025-10-10](https://polimill.jp/20251010-1/) |
| 其他安全状态 | 列明已取得 ISO/IEC 27017:2015；ISMAP“現在取得手続き中”（正在办理） | [FAQ](https://info.qommons.ai/faq)、[安全方针](https://info.qommons.ai/info/security)（2026-10-01 修订） |

**政府项目与认可。** 公司称已入选经济产业省「行政と連携実績のあるスタートアップ100選」（[2023-04-25](https://polimill.jp/pr20230425/)）。其他认可：其法律文本 AI「コモンズLawScopeAI」在数字厅黑客松获得優秀賞（[2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html)）；经公募型プロポーザル，公司承接数字厅「法制事務における生成AIの活用等に関する技術検証」业务，合同于 2025-05-20 签订（[2025-06-02](https://prtimes.jp/main/html/rd/p/000000520.000088829.html)）；在总务省「公共分野における信頼できるAIを用いた開発実証事業」中，作为兵库县五个市町 PLaMo 评估项目的代表机构，是 16 个申请中入选的 4 个项目之一（[总务省，2026-06-08](https://www.soumu.go.jp/menu_news/s-news/01tsushin03_02000462.html)）。COO 谷口野乃花入选 Forbes 30 Under 30 Asia 2026 AI 类别（[2026-06-04](https://polimill.jp/20260604-1/)）。

### 公司陈述的背景

- 五周年新闻稿援引：1,729 个市区町村中有 744 个被列为“消滅可能性自治体”（有消失风险的自治体），公务员录用处于历史低位，资深职员退休导致隐性知识流失。该稿把免费核心产品描述为一种长期选择，以“社会贴现”（social discounting）而非指数贴现来解释（[2026-02-25](https://polimill.jp/20260225-1/)）。
- シリーズA 新闻稿提出目标“予算の制約でAIが使えない自治体をゼロにする”（不让任何自治体因预算限制而用不上 AI），并称其商业模式不依赖使用费（[2026-01-19](https://polimill.jp/20260119-1/)）。

---

## 产品

### QommonsAI

产品网站的描述是“全国の行政文書を、根拠ごと引き出せる。1,000アカウントまで無料の、自治体のための生成AI。”（连同依据一起调取全国行政文书；面向自治体、1,000 个账号以内免费的生成式 AI）（[产品网站](https://info.qommons.ai/)；访问于 2026-10-11）。

**起源。** 2024 年 3 月，公司开始免费提供名为【DIGITAL COMMONS】的省厅／自治体支援 AI 的 β 版。该版本以 ChatGPT 作为界面，以 AWS 处理数据（[2024-03-13](https://polimill.jp/2024031301-2/)）。QommonsAI 预览版提供给 17 个基础自治体和 4 个广域自治体，公司称发布时约 50 个自治体和省厅已签约（[2024-08-02](https://prtimes.jp/main/html/rd/p/000000418.000088829.html)）。随后推出产品版，免费提供 100 个账号（[2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html)）。公司的新年新闻稿称，开发始于 2024 年 3 月，2024 年 7 月发布（[2025-01-06](https://prtimes.jp/main/html/rd/p/000000484.000088829.html)）。没有新闻稿明确说明 DIGITAL COMMONS 已更名为 QommonsAI。

按[功能页面](https://info.qommons.ai/function)和 [FAQ](https://info.qommons.ai/faq) 的组织方式列出的功能领域（访问于 2026-10-11）：

| 领域 | 产品页面的陈述 |
|---|---|
| 模型选择 | 支持 OpenAI、Anthropic、Google 和 Preferred Networks 的模型，可在对话中途切换。FAQ 列出 GPT-5.4、GPT-5.4 mini、Claude Opus 4.6、Claude Sonnet 4.6、Claude Haiku 4.5、Gemini 3.1 Pro、Gemini 3 Flash 等，以及 PLaMo 2.2 Prime；部分标注为国内区域模型 |
| 全国行政知识库 | 中央省厅、全部 47 个都道府县及各市区町村公开的文书（议会会议记录、计划、条例资料），以及学术论文和白皮书。回答注明自治体名、议会名、日期和原文链接。数据由 Polimill 收集和更新。法令检索使用自研“LawChunker”，宣称准确率 98%（为原方法的 2.1 倍） |
| 七个专业 AI | 議会対応AI（议会答辩）、行政文書AI（e-Gov法令，调用 e-Gov 数据库和官方 API）、公共サービスサポートAI、社会福祉AI、「住民の声」返信サポートAI（起草 300 字以内的居民回复）、プライベートナレッジAI、QommonsAI Talk（通用对话）。各专业 AI 有独立的数据源和系统提示词 |
| 私有知识（RAG） | 四种云盘类型，最多五层文件夹，三级角色（超级管理员／管理员／成员）。支持 PDF、Word、Excel、PowerPoint、CSV、文本和图片，并对扫描版 PDF 和幻灯片中的图片文字做 OCR。基础自治体免费 100GB，广域自治体 300GB |
| Deep Research | 跨庁内文书、全国行政知识库和网络反复检索，生成带出处的报告 |
| 图像生成 | 多个模型，支持 4K 输出；LGWAN 环境不可用 |
| 管理与安全 | 基于规则和 AI 的个人信息检测，可选警告或拦截模式；管理员可设置 100 个以上禁用词；CIDR 格式 IP 白名单；按自治体隔离租户；使用情况仪表盘、自动月报，以及输入输出日志的 CSV 导出 |
| LGWAN | 自 2026 年 4 月起经由株式会社シナジー 的数据中心提供 LGWAN-ASP 访问。只有文本和画面信息跨越边界。LGWAN 环境下不能生成图像、上传或下载文件，也不能跳转外部链接 |
| 培训 | 分三级（初級／中級／上級）；前两级的免费名额以抽签方式分配 |

**商业化。**

- *免费额度。* 每个机构 1,000 个账号以内免费，无期限；在此范围内不限 token 数和对话数（[价格页面](https://info.qommons.ai/price)、[FAQ](https://info.qommons.ai/faq)；访问于 2026-10-11）。产品版上线时免费额度为 100 个账号，ver.2.1 将其提高到 1,000 个（[2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html)、[2025-10-02](https://polimill.jp/20251002-1/)）。
- *超过 1,000 个账号。* 一份新闻稿公布了按每增加 1,000 个账号计的阶梯式月费，并称不设使用上限（[2026-01-09](https://polimill.jp/20260109-1/)）。现行价格页面则改为按使用人数提出方案，FAQ 称超过 1,000 个账号时设有月度使用上限（访问于 2026-10-11）。
- *LGWAN。* 不额外收费（[2025-12-08](https://polimill.jp/20251208-1/)、[2026-01-09](https://polimill.jp/20260109-1/)）。
- *培训与支持。* 按次收费的培训以及按月收费的“AI導入伴走支援 Light”支持方案有公开价目表（[价格页面](https://info.qommons.ai/price)）。此前的新闻稿称可在全国各地免费上门培训（[2025-07-23](https://polimill.jp/20250723-1/)）。
- *付款与销售渠道。* 政府客户以发票付款。另有企业／个人版，按账号按月计费，10 个账号起，可用信用卡付款（[特定商取引法页面](https://info.qommons.ai/info/commerce-law)、[企业版价格页面](https://info.qommons.ai/business_personal/price)）。产品对所有自治体直接销售，不经代理商（“代理店を介さない直販体制”）（[功能页面](https://info.qommons.ai/function)）。
- *自述收入模式。* “QommonsAIの収益モデルは、利用料ではありません”（QommonsAI 的收入模式不是使用费）：公司指向以 Qommons ONE 应用商店和未来产品层级为中心的生态系统（[2026-01-09](https://polimill.jp/20260109-1/)）。
- *计划中的智能体版。* 按完成的正式运行次数（SBE）计费，单价在合同年度内固定（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。

### Surfvote

一款社交网络式服务，用户可就“议题”（イシュー）在选项中投票并发表评论。议题由运营人员、大学教师、专家和自治体撰写；公司称会视情况把结果提交给相关省厅和政治人物（[2023-04-25](https://polimill.jp/pr20230425/)）。服务于 2021 年 9 月上线，最初以 Twitter 账号登录（[2022-12-13](https://polimill.jp/pr2022121302/)、[2021-10-26](https://polimill.jp/pr20211026/)）。之后陆续增加：邮箱注册和 PC 版（[2021-11-30](https://polimill.jp/pr20211130/)）、用于国立大学课堂的 SaaS 版（[2022-05-31](https://polimill.jp/pr20220531/)），以及面向自治体的「Surfvoteローカル」，奈良县田原本町自 2022-11-24 起首先使用（[2022-12-13](https://polimill.jp/pr2022121302/)）。横滨市称，其利用 Surfvote 按区征集意见的服务，是由 Polimill 与株式会社トラストアーキテクチャ根据与该市的委托合同提供的（[横滨市，2026-06-01 更新](https://www.city.yokohama.lg.jp/city-info/koho-kocho/kocho/dp/dpkekka/R07dpkekka.html)）。未找到 Surfvote 的公开价目表。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2021-11-30 | Surfvote：74 个议题 | [新闻稿](https://polimill.jp/pr20211130/) |
| 2024-08-02 | QommonsAI 预览版：约 50 个自治体和省厅签约 | [新闻稿](https://prtimes.jp/main/html/rd/p/000000418.000088829.html) |
| 2024-11-30 | QommonsAI：发布三个月内 100 个自治体和省厅导入 | [新闻稿](https://prtimes.jp/main/html/rd/p/000000470.000088829.html) |
| 2025-01-06 | Surfvote：累计发布议题 700 个以上 | [新闻稿](https://prtimes.jp/main/html/rd/p/000000484.000088829.html) |
| 2025-07-23 | QommonsAI：约 300 个自治体；每月新增约 60 个 | [新闻稿](https://polimill.jp/20250723-1/) |
| 2025-08-06 | Surfvote：月页面浏览量 50 万 | [新闻稿](https://polimill.jp/20250806-2/) |
| 2025-12-31 | QommonsAI：约 600 个自治体、约 20 万名用户；Surfvote：月 PV 60 万 | [年度总结](https://polimill.jp/20251231-1/) |
| 2026-02-25 | QommonsAI：约 700 个自治体、约 25 万名职员；Surfvote：月 PV 80 万 | [五周年](https://polimill.jp/20260225-1/) |
| 2026-04 | QommonsAI：约 800 个自治体、约 30 万名职员 | [2026-05-08](https://polimill.jp/20260508-4/) |
| 2026-07 | QommonsAI：1,050 个“自治体・パブリックセクター”，约 55 万名职员 | [Wantedly](https://www.wantedly.com/projects/2420681)；访问于 2026-10-11 |
| 2026-08-31 | QommonsAI：约 1,100 个自治体、60 万名职员 | [产品网站](https://info.qommons.ai/) |

公司称 QommonsAI 为“導入シェアNo.1”（导入份额第一），并附限定说明“当社2026年1月調べ、他サービスとバンドルされていない単体プロダクトにおいて”（公司 2026 年 1 月调查，限于未与其他服务捆绑的单一产品）（[2026-01-19](https://polimill.jp/20260119-1/)）。

### 已公布客户与合作伙伴

| 日期 | 对象 | 公布内容 |
|---|---|---|
| [2024-07-09](https://polimill.jp/2024071901-2/) | 奈良县田原本町 | 合作协定及 QommonsAI 试点；新闻稿称为奈良县首例 |
| [2025-03-17](https://prtimes.jp/main/html/rd/p/000000506.000088829.html) | 大阪府阪南市 | QommonsAI 试点后签订业务合作协定 |
| [2025-05-14](https://polimill.jp/qommonsai_0514_2025/) | Preferred Networks | PLaMo Prime 作为标准模型加入，向约 150 个自治体提供 |
| [2025-06-02](https://prtimes.jp/main/html/rd/p/000000520.000088829.html) | 数字厅 | 法制事務领域生成式 AI 的技术验证 |
| [2026-02-27](https://polimill.jp/20260227-1/) | 株式会社シナジー（冲绳） | 自 2026 年 4 月起共同提供 LGWAN 接入服务；计划与其文书管理系统「ActiveCity」联动 |
| [2026-04-20](https://kyodonewsprwire.jp/release/202604207739) | 兵库县尼崎市 | 市政府新闻稿：2026-04-24 签订合作协定，称为中核市首例 |
| [2026-05-08](https://polimill.jp/20260508-4/) | 日本微软（日本マイクロソフト） | 为 GPT-5.4 采用 Azure OpenAI 日本区域；称为双方首个合作项目 |
| [2026-06-30](https://polimill.jp/20260630-1/) | 总务省；兵库县及姫路市、尼崎市、加西市、加東市、多可町 | 在实际自治体业务中基于 QommonsAI 评估 PLaMo 3.0 Prime，2026 年 6 月至 2027 年 3 月（计划） |
| [2026-09-25](https://polimill.jp/20260925/) | 香川县中讃广域圈（2 市 3 町）及其行政事务组合 | 同时签订生成式 AI 协定 |

2025–2026 年公布的其他自治体协定包括和光市、日進市、大崎市、野辺地町、苫小牧市、多可町、小牧市和河内長野市（见[新闻索引](https://polimill.jp/news/)）。公司 [PR TIMES 源](https://prtimes.jp/main/html/searchrlp/company_id/88829)中日期为 2026 年的 152 条内容里，有 89 条标题含“研修”（培训），多为在各自治体开展 QommonsAI 培训的报告（按标题统计，2026-10-11）。

### 公开计划

- **シリーズA 资金用途**（[2026-01-19](https://polimill.jp/20260119-1/)）：（1）Qommons ONE 开发与合作伙伴拓展；（2）全国销售与支持体系，目标 2026 年达到 1,200 个自治体、80 万名用户；（3）“QommonsAI Pro”“Qommons Connect”“QommonsAI Advance”的研发；（4）结合 GraphRAG 与行政本体（行政オントロジー）的数据基础；（5）人形机器人在公共服务中的试点。
- **Qommons ONE**——QommonsAI 内的应用商店。合作伙伴应用通过 MCP 接入，方式有两种：向 Polimill 提供数据，或由合作伙伴自行运营 MCP 服务器。合作伙伴需通过四维度审核和沙箱测试（[2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)）。2026 年 10 月的新闻稿称其于 2026 年 10 月底开放，目标是 2027 年内上架约 100 个应用（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。此前公布的时间见 `备注`。
- **QommonsAI 3.0 エージェント版**（智能体版），计划 2027 年 1 月提供。职员用自然语言定义业务，流程由代码主导，分支由“判断モデル”（判断模型）决定，最后才由 LLM 生成文本。每个步骤可设置为 AI 处理或职员确认，并附审批路径。新增事件触发和沙箱运行，通过 MCP 连接外部服务（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。
- **全国行政AXレポジトリ**——共享标准化自治体业务模板的资料库，计划 2027 年 4 月公开，自治体可免费参与（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。

---

## 创始人

公司页面在“役員紹介”下列出五名成员（[公司页面](https://polimill.jp/company/)；访问于 2026-10-11）。就任时间来自公司的招聘访谈（[talk01](https://polimill.jp/interview/talk01/)，2026-09-18；[talk02](https://polimill.jp/interview/talk02/)、[talk03](https://polimill.jp/interview/talk03/)，2026-10-02）。

| 姓名 | 职务（原文） | 公司所述背景 |
|---|---|---|
| 伊藤あやめ | 代表取締役CEO，2025 年 3 月起 | 上智大学毕业；曾在伊藤忠集团旗下有色金属贸易公司负责英美金属加工厂商的日本代理业务。2023 年 1 月加入 Polimill，最初从事公关 |
| 谷口野乃花 | 代表取締役COO，2025 年 3 月起 | 在东京大学附属高中就读期间有创业经历；曾在一家 SaaS 公司的客户成功部门担任 850 人销售组织的导师。约在 QommonsAI 上线时加入。2026 年 6 月被描述为 23 岁，在庆应义塾大学学习经济学的同时统管 QommonsAI（[2026-06-04](https://polimill.jp/20260604-1/)） |
| Julian Brody | ビジョナリー・エバンジェリスト；talk01 中称为“創業者”（创始人） | 曾在日立制作所设计开发超导电磁铁和发电机；曾在雅虎日本参与众多项目；持有多项专利，包括引入用户风险规避参数的推荐算法 |
| 若林正浩 | CAIO，2025 年 3 月起；開発部担当取締役（负责开发部的董事） | 曾任数据科学家、营销人员及大学神经美学研究人员 |
| 前川知英 | 社外取締役（外部董事）兼 CAO，2025 年 3 月起 | 曾在东京大学从事 AI 与数据利用研究；在金融机构从事金融和数理工作；2018 年创业，支持地方政府和地方金融机构的数据利用 |

**创立与早期代表人。** 2021 年至 2025 年初的新闻稿署名 **横田えり** 为代表取締役（[2021-11-30](https://polimill.jp/pr20211130/)；[2023-07-31](https://polimill.jp/pr20230731/) 中载有横田关于公司宗旨的评论）。2021 年 10 月的新闻稿称创始团队共 8 人：一名自互联网早期即从事 Web 服务的总监、自由职业应用开发工程师、设计师、SNS 分析与信息处理专家以及大学生（[2021-10-26](https://polimill.jp/pr20211026/)）。在 talk01 中，Julian Brody 称在 2021 年成立公司之前，他已与一个小团队开发 Surfvote 的前身产品。公司页面未列出横田えり，所查阅的资料均未说明横田えり与 Julian Brody 之间的关系。Julian Brody 曾以“ビジョナリー・エバンジェリスト”身份出席尼崎市签约（[尼崎市，2026-04-20](https://kyodonewsprwire.jp/release/202604207739)）。

**其他职能。** talk03 介绍了开发部（QommonsAI 与 Surfvote 的开发运营、政府研发招标项目、安全认证）、负责认证工作的“ソーシャルストラテジスト”岗位，以及一名约自 2021 年起以业务委托身份参与、2025 年转为正式员工的全栈工程师。talk02 提到销售、FDE 式销售岗位和培训团队。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2021-10-26 | シードラウンド | 925 万日元（925万円） | 未披露 | 含天使轮约 3,000 万日元（約3,000万円） | [Polimill](https://polimill.jp/pr20211026/) |
| 2021-11-30 | 未命名 | 未说明 | 未披露 | 約3,500万円超 | [Polimill](https://polimill.jp/pr20211130/) |
| 2022-05-31 | 未命名 | 未说明 | 未披露 | 7,500万円超 | [Polimill](https://polimill.jp/pr20220531/) |
| 2022-12-13 | 第三者割当増資（以个人为认购方） | 4,330 万日元（4,330万円） | 个人 | 約1億3,000万円 | [Polimill](https://polimill.jp/pr2022121302/) |
| 2023-04-25 | 未命名（2023 年 3–4 月） | 4,000万円以上 | 个人投资者 | 1億7,000万円超 | [Polimill](https://polimill.jp/pr20230425/) |
| 2023-07-31 | 増資（2023 年 7 月） | 未说明 | 未披露 | 2億円超 | [Polimill](https://polimill.jp/pr20230731/) |
| 2024-10-03 | プレシリーズA | 未说明 | 未披露 | 5億円超 | [PR TIMES](https://prtimes.jp/main/html/rd/p/000000435.000088829.html) |
| 2026-01-19 | シリーズA | 約6億3,500万円：VC 5.2 亿日元 + 管理层及天使约 1,500 万日元（股权约 5.35 亿日元）+ 大型银行债务 1 亿日元 | 未披露 | 未说明 | [Polimill](https://polimill.jp/20260119-1/)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000625.000088829.html) |

- [2022-12-13 新闻稿](https://polimill.jp/pr2022121302/)称，截至当时的全部资金约 1億3,000万円，均来自创始成员和个人。
- 2023-07-31 新闻稿曾计划于 2023 年秋以プレシリーズA 名义新筹约 1 亿日元（[2023-07-31](https://polimill.jp/pr20230731/)）。公司后来称为プレシリーズA 的一轮于 2024-10-03 公布。
- シリーズA 新闻稿给出约 50億円 的投后估值，标题为“無料なのに50億円”（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000625.000088829.html)）。Kepple 将同一轮描述为向风险投资机构和天使投资人进行的第三者割当增资，加上金融机构贷款（[Kepple](https://kepple.co.jp/articles/7sefmz9zt6)）。
- 五周年新闻稿感谢投资者支持“基本無料でのインフラ提供”（基础部分免费提供的基础设施）这一模式（[2026-02-25](https://polimill.jp/20260225-1/)）。
- Wantedly 上有一则职位标题为“IPOを目指すスタートアップの人事”（以 IPO 为目标的初创公司的人事岗位）（[Wantedly](https://www.wantedly.com/companies/company_9612155/projects)；访问于 2026-10-11）。polimill.jp 的会计岗位提到“将来の上場準備”（未来的上市准备）（[招聘页面](https://polimill.jp/recruit/)；访问于 2026-10-11）。

---

## 工程

### 技术栈与平台

**经文档或可观察的公开资产确认**

- **AWS。** 上传数据保存在 AWS 东京区域，以 AES-256 加密，密钥由 AWS KMS 管理。FAQ 写明可故障切换到 AWS 大阪区域并做跨区域复制，年可用率 99% 以上（目标 99.5%）（[FAQ](https://info.qommons.ai/faq)）。安全方针列出 AWS CloudTrail 审计日志、TLS 1.2 以上、经 AWS 的 NTP，以及用户数据每日备份（保留 28–31 代）和 RAG 数据每小时备份（保留 366 代）（[安全方针](https://info.qommons.ai/info/security)）。两份新闻稿称在 AWS 国内区域运行，“JP CRIS等で国内処理を具体保証”（[2026-01-09](https://polimill.jp/20260109-1/)、[2026-01-19](https://polimill.jp/20260119-1/)）。
- **各提供商的 LLM 处理位置**（[FAQ](https://info.qommons.ai/faq)，LGWAN 部分）：

  | 模型系列 | 请求处理位置 |
  |---|---|
  | ChatGPT | OpenAI 的服务器 |
  | Claude | Polimill 自有的 AWS 环境，在日本国内完成 |
  | Gemini | Google 的服务器 |
  | PLaMo | Preferred Networks 的服务器，在日本国内完成 |

  另外，GPT-5.4 通过日本区域的 Azure OpenAI in Foundry Models 提供（[2026-05-08](https://polimill.jp/20260508-4/)）。
- **Web 应用分发。** `qommons.ai/login` 返回 `x-powered-by: Next.js`，经 Amazon CloudFront 提供（HTTP 响应头，观察于 2026-10-11）。
- **Surfvote 前端。** 页面加载 Firebase JS SDK 10.8.0（app 与 auth）（surfvote.com 页面源码，观察于 2026-10-11），站点地图托管在 ap-northeast-1 的 S3 存储桶（[robots.txt](https://surfvote.com/robots.txt)）。
- **检索与集成。** 用于检索数亿份公开文书的“大規模分散型HybridRAG基盤”（[2025-07-23](https://polimill.jp/20250723-1/)）；用于解析法令结构的“LawChunker”（[2026-01-19](https://polimill.jp/20260119-1/)）；e-Gov 法令数据库和官方 API（[FAQ](https://info.qommons.ai/faq)）；Qommons ONE 应用和计划中的智能体版使用 MCP（[2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)）。GraphRAG 与行政本体的结合被描述为正在构建中（[2026-01-19](https://polimill.jp/20260119-1/)）。

**仅见于招聘要求（不能单独证明当前在用）**

- 后端工程师，发布于 2025-05-30（[Green](https://www.green-japan.com/company/10658/job/285168)）。标签：Python、Go、Node.js、AWS、Docker。*必需*：后端开发（Python、Go、Node.js 等，“言語は不問”——语言不限）；Docker/AWS（ECS、Aurora、S3）。*优先*：使用 FastAPI 或 LangChain 的 Python；QuickSight。职位描述提到 OpenAI 与 Claude 的编排、RBAC/ABAC 以及 QuickSight 仪表盘。
- AI/NLP 工程师与技术负责人（知识图谱与语义系统），均发布于 2025-08-11（[Green](https://www.green-japan.com/company/10658/job/293843)、[Green](https://www.green-japan.com/company/10658/job/293842)）。职位描述涉及本体与知识图谱、LLM／规则／词典混合的信息抽取（NER/RE/事件）、自然语言到图查询的转换，以及 MLOps/GraphOps。未指明任何编程语言。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 多模型对话平台 | 按租户隔离的 Web 应用；四家供应商的模型可在对话中切换；可按组织、部门、用户控制可用的 AI、模型和功能 | [FAQ](https://info.qommons.ai/faq) |
| 全国行政知识库 | 由 Polimill 收集和维护。公司称在添加元数据时修正了自治体文书中的文件名和日期错误，并向自治体核实 | [2025-07-23](https://polimill.jp/20250723-1/)、[功能页面](https://info.qommons.ai/function) |
| 租户 RAG 存储 | 文件夹层级与基于角色的访问控制；带 OCR 的文件导入；单文件最大 100MB（Excel 为 10MB／300 条记录） | [FAQ](https://info.qommons.ai/faq) |
| 个人信息与策略过滤 | 基于规则和 AI 的个人信息检测，警告或拦截；两层禁用词列表；所有检测记录供管理员查看 | [FAQ](https://info.qommons.ai/faq) |
| LGWAN 网关 | 在 LGWAN 与互联网边界的株式会社シナジー 数据中心（公开网段）部署负载均衡器、代理服务器和防火墙；禁用文件传输；两套网络共用同一租户和账号 | [2026-02-27](https://polimill.jp/20260227-1/)、[FAQ](https://info.qommons.ai/faq) |
| 使用分析 | 仪表盘、自动生成的月度效果报告、CSV 日志导出 | [功能页面](https://info.qommons.ai/function) |
| Qommons ONE | 在 QommonsAI 内分发应用；合作伙伴提供数据或运营 MCP 服务器；上架前经审核和沙箱验证 | [2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html) |
| Surfvote | 议题发布、投票、评论和评价；自治体“本地”版；大学 SaaS 版 | [2022-12-13](https://polimill.jp/pr2022121302/)、[2023-04-25](https://polimill.jp/pr20230425/) |

**运维。** 2026-06-23，因域名续费手续未正常完成而导致域名过期，QommonsAI 约 8 小时 20 分钟（07:38–15:58）无法访问。公司称服务器、数据库和数据未受影响，并列出续费确认、告警设置和域名台账等改进措施（[2026-06-23](https://polimill.jp/apology/)）。FAQ 称计划维护至少提前 5 个工作日通知，故障后一周内提交书面报告（[FAQ](https://info.qommons.ai/faq)）。

**公司描述的开发流程。** 开发部列出三项工作：产品开发与运营、以政府招标方式承接的研发、安全认证。LGWAN 接入由一名侧重基础设施的工程师与合作公司共同完成（[talk03](https://polimill.jp/interview/talk03/)）。产品网站称通过“アジャイル開発体制”（敏捷开发体制）将自治体需求“最短数日で”（最快几天内）反映到服务中（[功能页面](https://info.qommons.ai/function)）。

### 招聘所需技术背景

- **后端工程师**（[Green](https://www.green-japan.com/company/10658/job/285168)，发布于 2025-05-30）。*必需*：Web 应用后端开发；REST API、异步与批处理；使用 Git 的团队开发；在 Docker/AWS 上的开发与运维；非日语母语者需 JLPT N1。*优先*：LLM、向量检索（RAG）或 NLP 的实现；高安全要求系统（RBAC、加密）；数据分析平台与日志汇总／可视化。
- **AI/NLP 工程师**（[Green](https://www.green-japan.com/company/10658/job/293843)，发布于 2025-08-11）。*必需*：NLP 和数据平台建设 7 年以上经验，并能在模型开发、精度改进和架构设计上从技术层面带领团队。
- **AI/NLP 技术负责人**（[Green](https://www.green-japan.com/company/10658/job/293842)，发布于 2025-08-11）。*必需*：在知识图谱、LLM 应用或本体设计方面具有国内顶尖的成果；在国际会议或同行评审期刊发表过论文；具备生产级实现与运维经验。
- **工程师（polimill.jp）。** 前后端、API 设计、数据联动、认证、权限与审计日志、LLM 评估、提示词设计和运维监控。职位描述强调兼顾研究与实现（[招聘页面](https://polimill.jp/recruit/)；访问于 2026-10-11）。未区分必需与优先条件。
- CAIO 表示：“エンジニアとしての経験はそこまで重視していません”（不太看重作为工程师的经验）（[talk03](https://polimill.jp/interview/talk03/)）。

### 行业领域

工作内容属于日本公共行政领域：

- 议会答辩起草（議会答弁）与自治体例规（例規）；
- 经 e-Gov 获取法令，以及数字厅项目中的法令起草；
- LGWAN 与自治体信息安全分级（FAQ 请处理“機密性3”信息的客户参照各自的指南）；
- 总务省项目中的福利、育儿支援和多元文化窗口业务；
- 自治体预算与采购。

后端职位把“公共・行政領域への関心、または社会課題への問題意識”（对公共／行政领域的兴趣或对社会问题的关注）列为*优先*而非必需条件。所查阅的职位均未要求具备公共部门工作经验。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 工作语言 | 开发部：“共通言語は日本語ですが多国籍”（共同语言为日语，成员来自中国、新加坡、菲律宾、韩国等）。后端职位要求非母语者具备 JLPT N1 | [talk03](https://polimill.jp/interview/talk03/)、[Green](https://www.green-japan.com/company/10658/job/285168) |
| 远程 | “開発チームはリモート中心ですが、営業チームは出社”（开发以远程为主，销售到办公室）。后端职位：完全远程。AI/NLP 职位：可商议远程 | [talk02](https://polimill.jp/interview/talk02/)、[Green](https://www.green-japan.com/company/10658/job/285168)、[Green](https://www.green-japan.com/company/10658/job/293843) |
| 地点 | 东京虎之门 | [公司页面](https://polimill.jp/company/) |
| 工作时间 | 10:00–19:00（后端）；10:00–18:00（AI/NLP） | [Green](https://www.green-japan.com/company/10658/job/285168)、[Green](https://www.green-japan.com/company/10658/job/293843) |
| 薪资 | 后端 400 万–1,200 万日元；AI/NLP 工程师 1,000 万–1,500 万日元；AI/NLP 技术负责人 1,500 万–2,200 万日元 | 上述 Green 职位 |
| 股权 | AI/NLP 职位注明“株式／RSU／SO制度あり”（股票、RSU 和股票期权） | [Green](https://www.green-japan.com/company/10658/job/293843) |
| 假期与福利 | 每周双休（土日祝），年假日 120 天，带薪年假 10–20 天；社会保险；按需配备 PC 和开发环境；购书与研讨会补助 | [Green](https://www.green-japan.com/company/10658/job/285168) |
| 签证担保 | 所查阅职位均未说明 | — |
| 初级候选人 | Green 的销售职位标注“未経験歓迎”（欢迎无经验者）；Wantedly 称其招聘包括新卒・中途・インターン（应届、社招和实习）。所查阅的工程职位均不面向应届生 | [Green 公司页面](https://www.green-japan.com/company/10658)、[Wantedly](https://www.wantedly.com/companies/company_9612155/projects) |
| 团队构成 | 平均年龄 20 多岁；两名代表人均为女性 | [Green](https://www.green-japan.com/company/10658/job/285168) |

---

## 备注

### 未公开披露

检索范围（2026-10-11）：

- **公司网站。** polimill.jp（站点地图、共 603 篇文章的 WordPress 文章索引、公司、about、服务、招聘和访谈页面）；info.qommons.ai（功能、价格、FAQ、安全方针和特定商取引法页面）；qommons.ai 登录页面；surfvote.com。
- **新闻、登记与数据库。** PR TIMES 公司源（company_id 88829）及选定的新闻稿；国税厅法人番号登记；INITIAL 和 Kepple（仅作线索）。
- **招聘网站。** Wantedly（17 个职位）和 Green（6 个职位）。
- **开发者平台。** GitHub 组织名 polimill、Polimill-Inc、polimill-inc、qommons、qommonsai、surfvote、polimill-jp；在 Zenn、note、Qiita 和 Speaker Deck 上按名称查找。
- **网络检索。** 以日文和英文检索 Polimill、ポリミル、QommonsAI、コモンズAI、Surfvote、横田えり 和 Julian Brody。

结论：

- **投资方。** 公司新闻稿未披露任何 VC、天使投资人或贷款方。公司 [2026-06-04 新闻稿](https://polimill.jp/20260604-1/)引用的 Forbes 介绍称投资方为“undisclosed venture capitalists”。
- **收入与财务结果。** 未公开。
- **シリーズA 之后的累计融资。** 未说明。
- **工程博客或技术文章。** 未找到；在 Zenn、note、Qiita 和 Speaker Deck 上以“polimill”查找均无账号。
- **开源。** GitHub 组织 [`polimill`](https://github.com/polimill)（创建于 2026-02-10）和 [`Surfvote`](https://github.com/Surfvote)（创建于 2021-02-21）存在，但均为 0 个公开仓库，资料字段中也没有与公司关联的信息，因此归属未确认。`qommons` 和 `qommonsai` 不存在。
- **创始人关系。** 没有资料说明横田えり 与 Julian Brody 的关系，也没有说明横田えり 何时离开董事会。未找到公布 2025 年 3 月代表人变更的新闻稿。
- **LGWAN-ASP 登记。** J-LIS 的 LGWAN-ASP 服务列表对自动访问返回 HTTP 403，因此未核实 QommonsAI 或シナジー 在该列表中的登记状态。
- **其他。** 未找到签证担保说明、离职率数据或 SLA 服务赔偿条款。

### 不同来源之间的不一致

- **资本金。** 6億円（[PR TIMES 公司信息栏](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)）与 2億4572万1558円（[Green 公司页面](https://www.green-japan.com/company/10658)）。两者均无日期（访问于 2026-10-11），也都未说明是否包含资本准备金。公司页面未列出资本金。
- **员工人数。** [Green](https://www.green-japan.com/company/10658) 为“20人”（无日期）；4 名正式员工加 6 名新招（[2025-11-05](https://polimill.jp/20251105-1/)）；“数十人規模”（[talk02](https://polimill.jp/interview/talk02/)，2026-10-02）。
- **地址。** [INITIAL](https://initial.inc/companies/A-40660)（资料更新于 2026-02-18）和 [Green 公司页面](https://www.green-japan.com/company/10658)给出六本木地址。Green 写的是“クロスオフィス六本木4F”，而登记中的旧地址为“ラウンドクロス六本木”。登记显示自 2026-03-24 起为虎之门，Green 的职位页面也已写虎之门。
- **QommonsAI 发布日期。** 2024 年 3 月开始开发、7 月发布（[2025-01-06](https://prtimes.jp/main/html/rd/p/000000484.000088829.html)）；“2024年10月には…リリース”（[about](https://polimill.jp/about/)）；预览版 [2024-08-02](https://prtimes.jp/main/html/rd/p/000000418.000088829.html)；产品版 [2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html)。
- **创始人。** 2021 年起的新闻稿署名横田えり 为代表取締役（[2021-11-30](https://polimill.jp/pr20211130/)）。2026 年的招聘访谈称 Julian Brody 为“創業者”（[talk01](https://polimill.jp/interview/talk01/)）。
- **新闻稿模板中的代表人。** 新闻稿署名在 [2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html) 与 [2025-03-17](https://prtimes.jp/main/html/rd/p/000000506.000088829.html) 之间由横田えり 换为新任代表人。一份日期为 [2025-05-19](https://prtimes.jp/main/html/rd/p/000000519.000088829.html) 的 Surfvote 新闻稿仍署名横田えり。Wantedly 职位称“Co-CEO体制”，而公司页面使用 CEO／COO 头衔。
- **贷款方。** 公司称シリーズA 的债务融资来自“メガバンク”（大型银行）（[2026-01-19](https://polimill.jp/20260119-1/)）。[2026-06-04 新闻稿](https://polimill.jp/20260604-1/)引用的 Forbes 文字则写作“local banks”。
- **估值。** 公司称投后约 50億円，而 [INITIAL](https://initial.inc/companies/A-40660) 截至 2026-01-18 的数字为 3,951百万円，标注为推測（估算）且包含潜在股份。
- **2026 年用户目标。** 1,200 个自治体、80 万名用户（[2026-01-19](https://polimill.jp/20260119-1/)），与 2026 年 12 月约 1,200 个自治体、65 万名用户（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。
- **Qommons ONE 时间表。** 2026 年 4 月发布、2026 年内 100 个以上应用（[2026-01-19](https://polimill.jp/20260119-1/)）；4 月 β 版、2026 年 6 月正式版（[2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)）；2026 年 10 月底开放、2027 年目标约 100 个应用（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。
- **超过 1,000 个账号的定价。** 阶梯式月费且“利用上限なし”（无使用上限）（[2026-01-09](https://polimill.jp/20260109-1/)），与“ご利用人数に応じた料金プランをご提案”（按使用人数提出方案）及月度使用上限（[价格页面](https://info.qommons.ai/price)、[FAQ](https://info.qommons.ai/faq)；访问于 2026-10-11）。
- **FAQ 内部**（[FAQ](https://info.qommons.ai/faq)，访问于 2026-10-11）：
  - 日志保存期限一处写 3 个月，另一处写 14 天无操作后归档、归档 90 天后删除。
  - 支持时间一处写 10:00–18:00，另一处写 10:00–17:00。
  - “トークン数や対話数に制限はございません”（不限 token 数和对话数）与超过 1,000 个账号时的使用上限并存。
- **计数口径。** Wantedly 截至 2026-07 的口径为“1,050の自治体・パブリックセクター”（自治体及公共部门）；其他来源的口径为“自治体”。OpenAI 关于 Polimill 的客户案例页面（openai.com/index/polimill/）在 2026-10-11 对自动访问返回 HTTP 403，未被使用。

### 其他

- **收入模式。** 公司称核心产品在 1,000 个账号以内免费，收入将来自周边生态系统而非使用费（[2026-01-09](https://polimill.jp/20260109-1/)、[FAQ](https://info.qommons.ai/faq)）。
- **已公布但尚未上线的产品**（截至 2026-10-11）：
  - QommonsAI Pro、Qommons Connect 和 QommonsAI Advance（[2026-01-19](https://polimill.jp/20260119-1/)）；
  - 无代码智能体构建平台“Runbook Qommons（仮称）”（[2026-02-25](https://polimill.jp/20260225-1/)）；
  - Qommons Qraft 和 Qommons Link（[功能页面](https://info.qommons.ai/function)）；
  - 智能体版和 AX 资料库（[2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)）。
- **新闻发布量。** polimill.jp 的 603 篇文章中有 599 篇归类为プレスリリース（WordPress 分类计数，2026-10-11）。日期为 2023 年的 266 篇中，有 226 篇标题含 Surfvote、投票、イシュー或意見（按标题统计，2026-10-11）。伊藤在 talk01 中称，入职最初几个月每天发布一篇新闻稿。polimill.jp 在 2024-07-17 至 2025-05-14 之间没有文章，而 PR TIMES 有该时期的新闻稿；本文两处均已核查。

---

## 资料来源

**官方**

- [公司官网（日文）](https://polimill.jp/)——[公司](https://polimill.jp/company/) · [about](https://polimill.jp/about/) · [服务](https://polimill.jp/services/) · [新闻索引](https://polimill.jp/news/) · [招聘](https://polimill.jp/recruit/)
- 招聘访谈（日文）：[talk01——创始人与 CEO，2026-09-18](https://polimill.jp/interview/talk01/) · [talk02——CAO 与 COO，2026-10-02](https://polimill.jp/interview/talk02/) · [talk03——开发部，2026-10-02](https://polimill.jp/interview/talk03/)
- [QommonsAI 产品网站（日文）](https://info.qommons.ai/)——[功能](https://info.qommons.ai/function) · [价格](https://info.qommons.ai/price) · [FAQ](https://info.qommons.ai/faq) · [信息安全方针](https://info.qommons.ai/info/security) · [特定商取引法表示](https://info.qommons.ai/info/commerce-law) · [企业版价格](https://info.qommons.ai/business_personal/price)
- [QommonsAI 应用登录](https://qommons.ai/login)
- [Surfvote](https://surfvote.com/) · [robots.txt](https://surfvote.com/robots.txt)
- [PR TIMES 公司页面](https://prtimes.jp/main/html/searchrlp/company_id/88829)
- GitHub 组织（归属未确认）：[polimill](https://github.com/polimill) · [Surfvote](https://github.com/Surfvote)

**新闻稿（日文，较新在前）**

- [J-LIS 展会：智能体版、Qommons ONE、AX 资料库 — 2026-10-05](https://prtimes.jp/main/html/rd/p/000000779.000088829.html)
- [香川县中讃广域协定 — 2026-09-25](https://polimill.jp/20260925/)
- [总务省可信 AI 实证项目入选（PLaMo） — 2026-06-30](https://polimill.jp/20260630-1/)
- [QommonsAI 故障报告（域名过期） — 2026-06-23](https://polimill.jp/apology/)
- [COO 入选 Forbes 30 Under 30 Asia — 2026-06-04](https://polimill.jp/20260604-1/)
- [采用 Azure OpenAI 日本区域 — 2026-05-08](https://polimill.jp/20260508-4/)
- [Qommons ONE 预告网站与合作伙伴招募 — 2026-04-15](https://prtimes.jp/main/html/rd/p/000000672.000088829.html)
- [与シナジー 合作的 LGWAN 接入服务 — 2026-02-27](https://polimill.jp/20260227-1/)
- [五周年 — 2026-02-25](https://polimill.jp/20260225-1/)
- [シリーズA，约 6.35 亿日元 — 2026-01-19](https://polimill.jp/20260119-1/) · [PR TIMES](https://prtimes.jp/main/html/rd/p/000000625.000088829.html)
- [新价格方案 — 2026-01-09](https://polimill.jp/20260109-1/)
- [2025 年度总结 — 2025-12-31](https://polimill.jp/20251231-1/)
- [免除 LGWAN 接入费 — 2025-12-08](https://polimill.jp/20251208-1/)
- [新使命 — 2025-12-05](https://polimill.jp/20251205-1/)
- [正式员工倍增 — 2025-11-05](https://polimill.jp/20251105-1/)
- [隐私标志 — 2025-10-10](https://polimill.jp/20251010-1/)
- [ISO/IEC 27001 — 2025-10-09](https://polimill.jp/20251009-1/) · [ISO 9001 — 2025-10-09](https://polimill.jp/20251009-2/)
- [免费额度提高到 1,000（ver.2.1） — 2025-10-02](https://polimill.jp/20251002-1/)
- [Surfvote 月 PV 50 万 — 2025-08-06](https://polimill.jp/20250806-2/)
- [300 个自治体；全国文书检索 — 2025-07-23](https://polimill.jp/20250723-1/)
- [数字厅法制事務技术验证 — 2025-06-02](https://prtimes.jp/main/html/rd/p/000000520.000088829.html)
- [署名横田えり 的 Surfvote 议题新闻稿 — 2025-05-19](https://prtimes.jp/main/html/rd/p/000000519.000088829.html)
- [加入 PLaMo Prime — 2025-05-14](https://polimill.jp/qommonsai_0514_2025/)
- [阪南市合作 — 2025-03-17](https://prtimes.jp/main/html/rd/p/000000506.000088829.html)
- [数字厅黑客松获奖 — 2025-03-07](https://prtimes.jp/main/html/rd/p/000000508.000088829.html)
- [2025 年新年致辞 — 2025-01-06](https://prtimes.jp/main/html/rd/p/000000484.000088829.html)
- [三个月 100 个自治体 — 2024-11-30](https://prtimes.jp/main/html/rd/p/000000470.000088829.html)
- [QommonsAI 产品版 — 2024-10-29](https://prtimes.jp/main/html/rd/p/000000447.000088829.html)
- [プレシリーズA，累计超过 5 亿日元 — 2024-10-03](https://prtimes.jp/main/html/rd/p/000000435.000088829.html)
- [QommonsAI 预览版 — 2024-08-02](https://prtimes.jp/main/html/rd/p/000000418.000088829.html)
- [田原本町合作 — 2024-07-09](https://polimill.jp/2024071901-2/)
- [DIGITAL COMMONS β 版 — 2024-03-13](https://polimill.jp/2024031301-2/)
- [累计超过 2 亿日元 — 2023-07-31](https://polimill.jp/pr20230731/)
- [新筹 4,000 万日元以上 — 2023-04-25](https://polimill.jp/pr20230425/)
- [4,330 万日元第三者割当增资 — 2022-12-13](https://polimill.jp/pr2022121302/)
- [累计超过 7,500 万日元；大学 SaaS — 2022-05-31](https://polimill.jp/pr20220531/)
- [邮箱登录与 PC 版 — 2021-11-30](https://polimill.jp/pr20211130/)
- [种子轮与 Surfvote 发布 — 2021-10-26](https://polimill.jp/pr20211026/)

**第三方报道与资料**

- [国税厅法人番号公表网站 — 5010401158530（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=5010401158530)
- [总务省——可信 AI 实证项目入选结果，2026-06-08（日文）](https://www.soumu.go.jp/menu_news/s-news/01tsushin03_02000462.html)
- [尼崎市——合作新闻稿，2026-04-20（日文）](https://kyodonewsprwire.jp/release/202604207739)
- [横滨市——Surfvote 意见征集结果，令和 7 年度（日文）](https://www.city.yokohama.lg.jp/city-info/koho-kocho/kocho/dp/dpkekka/R07dpkekka.html)
- [Green——公司页面（日文）](https://www.green-japan.com/company/10658) · [后端工程师](https://www.green-japan.com/company/10658/job/285168) · [AI/NLP 工程师](https://www.green-japan.com/company/10658/job/293843) · [AI/NLP 技术负责人](https://www.green-japan.com/company/10658/job/293842)
- [Wantedly——职位列表（日文）](https://www.wantedly.com/companies/company_9612155/projects) · [含 2026 年 7 月数字的销售职位](https://www.wantedly.com/projects/2420681)
- [Kepple——シリーズA 报道（日文）](https://kepple.co.jp/articles/7sefmz9zt6)
- [INITIAL / Speeda（日文）](https://initial.inc/companies/A-40660)
