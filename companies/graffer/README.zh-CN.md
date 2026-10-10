# Graffer

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-10-11。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-10-11。英文版为原始版本。

## 摘要

Graffer（株式会社グラファー / Graffer, Inc.）是一家东京公司，由石井大地（Daichi Ishii）于 2017-07-18 创立。公司经营两条业务线。一条是 **Graffer Platform**，面向地方政府和中央省厅销售的一组云服务，包括在线申请（Graffer スマート申請）、手续指引、窗口预约、用于电话咨询的 IVR 和 AI 语音代理，以及护理认定（要介護認定）进度查询服务。另一条是 **Graffer AI Solution**，面向企业销售企业级生成式 AI 工作平台（Graffer AI Studio）、业务专用 AI 代理、食品行业规格书（食品規格書）AI 数据转换产品（Graffer Databridge）、AI 辅助的受托开发和培训（[公司页面](https://graffer.jp/company)、[公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。自 2026 年 1 月起，公司使命为“We Remove Steps.”（[关于我们](https://graffer.jp/about)）。

- 政府业务规模：截至 2026-03，“270団体超”（超过 270 个团体），其中包括 70% 的政令指定都市，覆盖约 7,000 万居民（[公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。政府产品页面显示“7215 万人の市民が対象”和“254 の政府機関での案件実績”（无日期，访问于 2026-10-11；[政府页面](https://graffer.jp/governments)）。各来源数字不一致，见“备注”。
- 融资：截至 [2021-04-01](https://graffer.jp/news/2679) 约 12 亿日元的 Series B，累计约 22.2 亿日元（約22.2億円）。随后于 [2023-04-14](https://graffer.jp/news/4516) 与チェンジホールディングス进行资本业务合作，金额未披露。公司于 [2026-04-27](https://graffer.jp/news/7317) 收购行政システム研究所 100% 股份，于 [2026-06-30](https://graffer.jp/news/7505) 收购 5Minutes 100% 股份。
- 员工人数：“社員 81名”（81 名员工，仅正式员工，截至 2026-06）（[公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。
- 工程：招聘信息列出后端 Go 和 Python（Gin、Flask），前端 TypeScript、React 和 Next.js，以及 AWS、Docker、Kubernetes、Terraform、PostgreSQL、MySQL 和 MongoDB。公开的认证范围确认使用 AWS 和 MongoDB Atlas。工程师采用“全周期”（full-cycle）方式工作，从需求到运维由一人负责（[全周期工程师职位](https://herp.careers/v1/graffer/QE1EVzBa9GqT)、[公司页面](https://graffer.jp/company)；访问于 2026-10-11）。所有招聘信息和招聘资料均为日文。公司提供完全远程办公和无核心时间的弹性工时（[公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 法定名称 | 株式会社グラファー / Graffer, Inc. | [国税厅法人番号记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779)、[公司页面](https://graffer.jp/company) |
| 法人番号 | 9010401132779；指定日 2017-07-28（平成29年7月28日） | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779)；信息截至 2026-10-11 |
| 成立 | 2017-07-18 | [公司页面](https://graffer.jp/company) |
| 登记总部 | 東京都渋谷区千駄ヶ谷１丁目５番８号（自 2022-01-05）。此前登记地址：港区赤坂1-12-32 → 渋谷区神宮前2-3-10（2018-03-22）→ 渋谷区千駄ヶ谷1-2-3（2019-11-01） | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779) |
| 办公室 | 千駄ヶ谷オフィス，ジュニアー千駄ヶ谷ビル2F。2019 年 12 月曾开设神户办公室；当前公司页面只列出千驮谷办公室 | [公司页面](https://graffer.jp/company)、[2019-12-20](https://graffer.jp/news/1524) |
| 代表人 | 代表取締役 / 創業者 石井 大地 | [公司页面](https://graffer.jp/company) |
| 董事会 | 石井 大地（代表取締役）、小寺 広晃（取締役 兼 COO）、村田 祐介（取締役）、澤山 陽平、中谷 昇、瀧 俊雄（社外取締役）、千葉 尚洋（常勤監査役・社外） | [公司页面](https://graffer.jp/company)；访问于 2026-10-11 |
| 资本金 | 1,544,977,927 日元，含资本准备金（資本準備金を含む） | [公司页面](https://graffer.jp/company)；访问于 2026-10-11 |
| 主要股东（按所列） | 経営陣及び従業員、Incubate Fund、Coral Capital（旧500 Startups Japan）、株式会社チェンジホールディングス、TOPPANホールディングス株式会社、個人投資家 | [公司页面](https://graffer.jp/company) |
| 主要往来银行 | みずほ銀行、三井住友銀行、商工組合中央金庫 | [公司页面](https://graffer.jp/company) |
| 员工人数 | 81 名员工（社員のみ），截至 2026-06 | [公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 工作语言 | 未说明。招聘网站、全部十个 HERP 职位和两份招聘资料都只有日文版 | [招聘网站](https://career.graffer.inc/)、[HERP](https://herp.careers/v1/graffer)；访问于 2026-10-11 |
| 累计融资 | Series B 公告所述累计约 22.2 亿日元；之后的金额未披露 | [2021-04-01](https://graffer.jp/news/2679) |
| ISMS | ISO/IEC 27001:2022，IS 689557。初次登记 2018-06-23；有效期至 2027-06-22。范围：Webサービスの開発及び運用、ビジネスアウトソーシング事業、人材派遣業 | [公司页面](https://graffer.jp/company)、[ISMS 登记](https://isms.jp/lst/ind/CR_IS_x0020_689557.html) |
| 云安全 | ISO/IEC 27017：Graffer Platform 为 CLOUD 806590（初次登记 2024-06-23），Graffer AI Studio 为 CLOUD 828729（2025-05-07） | [公司页面](https://graffer.jp/company)、[2025-06-06](https://graffer.jp/news/6618) |
| 隐私 | プライバシーマーク 第17004041号（[2021-03-12](https://graffer.jp/news/2581) 公布） | [公司页面](https://graffer.jp/company) |
| ISMAP | Graffer Platform 于 2021-12-20 登记入 ISMAP 云服务清单。公司以维持登记所需的审计费用为由，于 2022-01-24 申请撤回，随后被删除 | [2022-04-01](https://graffer.jp/news/3504) |

**项目与荣誉。** 入选 J-Startup 2021（[2021-10-20](https://graffer.jp/news/3080)）。2023 和 2024 年获得 Findy Team+ Award（[2024-11-01](https://graffer.jp/news/6095)）。Graffer スマート申請入选总务省“情報アクセシビリティ好事例2024”（[2025-03-19](https://graffer.jp/news/6490)）。公司于 [2019-08-23](https://graffer.jp/news/1402) 推出媒体网站“Govtech Trends”。

**公司陈述的市场背景。** 公司介绍资料引用政府数据：行政手续超过 62,000 种，每年约 25 亿次，手续耗时 12億3,238時間，手续成本 3兆1,070億日元。资料还称，把中央与地方政府的云／IT 支出和相邻的 BPO 支出合计，TAM 接近 10 万亿日元（[公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。在食品行业，公司引用经济产业省调查称，商品信息交换每年耗费 30 万人月，公司将其换算为约 1,000 亿日元的成本（[2025-11-19](https://graffer.jp/news/6911)）。

### 品牌与法律实体

| 名称 | 类型 | 管辖地／时期 | 所述关系 | 来源 |
|---|---|---|---|---|
| 株式会社グラファー（Graffer, Inc.） | 法律实体 | 日本；法人番号 9010401132779 | 运营公司 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779) |
| 株式会社行政システム研究所 | 子公司 | 札幌；成立于 2014-06；2026-04-27 收购 100% | 面向地方政府的公会计系统 | [2026-04-28](https://graffer.jp/news/7317) |
| 株式会社5Minutes | 子公司 | 神户；成立于 2021-02；2026-06-30 收购 100% | Google Workspace／Google Cloud 正规代理商 | [2026-06-30](https://graffer.jp/news/7505) |
| 株式会社KURASERU | 业务转让的对方 | 大阪 | Graffer 于 2024-10-24 受让其护理认定查询系统业务 | [2024-10-24](https://graffer.jp/news/6054) |
| ｇｒａｐｈｅｒ株式会社 | 读音相同（グラファー）的无关实体 | 东京都中野区 | 所查来源均未提及任何关联 | [国税厅记录](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011201021353) |

KURASERU 公告和 5Minutes 公告中，两家对方公司的代表董事为同一人：平山流石（[2024-10-24](https://graffer.jp/news/6054)、[2026-06-30](https://graffer.jp/news/7505)）。收购价格和收购后的架构均未披露。

---

## 产品

当前产品阵容依据[公司介绍资料（2026-07 版）](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)中的服务地图、[政府产品页面](https://graffer.jp/governments)和 [AI Solution 网站](https://graffer.jp/ai-solution)整理（访问于 2026-10-11）。

### Graffer Platform（地方政府与省厅）

| 服务 | 内容 | 发布／首次公开日期 | 页面 |
|---|---|---|---|
| Graffer スマート申請 | 在智能手机上完成的在线申请，具备表单生成器、模板、My Number 卡身份验证、无现金支付、电子签名、LGWAN 支持和文件在线交付 | [2020-04-07](https://graffer.jp/news/1616) | [页面](https://graffer.jp/governments/solution-smart-apply) |
| Graffer 手続きガイド | 通过回答问题告诉居民需要办理哪些手续的指引 | 首个自治体部署（镰仓）[2018-11-01](https://graffer.jp/news/405) | [页面](https://graffer.jp/governments/solution-guides) |
| Graffer 窓口予約 | 政府窗口的在线预约 | [2021-09-01](https://graffer.jp/news/2928) | [页面](https://graffer.jp/governments/solution-booth-reserve) |
| Graffer Call | 使用按键拨号和 AI 分流的 IVR、短信链接和自动外呼；通话录音功能宣布于 2025 年 8 月下旬提供（[2025-07-29](https://graffer.jp/news/6699)） | “提供を開始” [2024-08-16](https://graffer.jp/news/5898)；见“备注” | [页面](https://graffer.jp/governments/solution-call) |
| Graffer AI オペレーター | 对话式 AI 电话代理，根据登记的知识库回答，并可转接职员 | 首次公开提及 [2025-10-03](https://graffer.jp/news/6822) | [页面](https://graffer.jp/governments/solution-ai-operator) |
| お悩みハンドブック | 根据用户勾选的困扰查找支援制度和咨询窗口；有全国版和自治体版 | 全国版 [2022-01-27](https://graffer.jp/news/3297)；自治体定制 [2022-12-15](https://graffer.jp/news/4081) | [页面](https://graffer.jp/governments/solution-compass) |
| Graffer 要介護認定照会 | 在线查询护理认定进度并在线申请信息提供；自治体通过 LGWAN-ASP 连接 | 业务受让 [2024-10-24](https://graffer.jp/news/6054) | [页面](https://graffer.jp/governments/solution-nintei-shoukai) |
| Graffer 認定調査票作成 | 以 AI 辅助编制护理认定调查表（试点） | 都城市试点 [2026-08-28](https://graffer.jp/news/7697) | [咨询页面](https://graffer.jp/governments/solution-nintei-chosahyo) |
| Graffer AI BPO | 基于 AI 的业务流程外包 | 列于资料的服务地图中；无日期 | [资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |

面向省厅及外围团体，[省厅页面](https://graffer.jp/ministries)（访问于 2026-10-11）提供咨询与 DX 规划、BPR、采购支援、业务专用 AI 代理、“SI by AI駆動開発”（遗留系统迁移与现代化）和培训，并邀请其他公司将公共部门项目分包给 Graffer。

### Graffer AI Solution（企业）

| 产品／服务 | 内容 | 发布 | 页面 |
|---|---|---|---|
| Graffer AI Studio | 企业生成式 AI 工作平台，提供 GPT、Gemini 和 Claude 模型及模型自动选择、基于内部文档的 RAG、转写、数据分析、批量处理、无需提示词的任务库、图像生成和“AI Labs”。企业管控包括 SAML SSO、SCIM、用户管理 API 和审计日志 | 封闭测试 [2023-03-24](https://graffer.jp/news/4389)；正式发布 [2023-04-26](https://graffer.jp/news/4561) | [页面](https://graffer.jp/ai-solution/products/graffer-ai-studio) |
| 業務特化AIエージェント | 在 AI Studio 平台上为客户构建并托管的专用 AI 应用 | [2025-10-07](https://prtimes.jp/main/html/rd/p/000000103.000038525.html) | [页面](https://graffer.jp/ai-solution/ai-consulting-development) |
| Graffer Databridge | 读取 PDF 和 Excel 格式食品规格书（食品規格書）并转换为各零售商格式的 AI 代理；专利申请 特願2024-209582 | 封闭测试 [2025-11-19](https://graffer.jp/news/6911)；国分西日本 [2026-06-02](https://graffer.jp/news/7409) | [页面](https://graffer.jp/ai-solution/ai-databridge/food-kikaku) |
| Graffer AI駆動開発プログラム | 以团队为单位导入 AI 优先开发流程的培训（“生産性2,000%アップ”） | [2025-10-06](https://graffer.jp/news/6834) | [页面](https://graffer.jp/ai-solution/generative-ai-learning/ai-dev-training) |
| AI駆動受託開発 / AI駆動基幹システム刷新 | AI 辅助的受托开发和遗留核心系统替换，包括从源代码逆向生成规格书 | 列于资料的服务地图中 | [资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 顾问与培训 | 导入陪跑支援（伴走支援）和生成式 AI 培训 | [产品开发资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)将 Graffer AI Solution 标为 2023-10 | [网站](https://graffer.jp/ai-solution) |

**已停止的服务。** Graffer 法人証明書請求（在线申请法人登记证明；截至 [2020-02-26](https://graffer.jp/news/1561) 有 10,000 家法人用户）和 Graffer 電子証明書取得サポート于 2025-03-31 停止受理新申请。Graffer 法人証明書請求于 2025-06-30 全面终止（[2025-02-27](https://graffer.jp/news/6473)）。

### 商业化

政府产品以 SaaS 形式销售，公司另提供咨询、BPO 和受托开发。未找到 Graffer Platform 的公开价目表；窓口予約页面称采用定额制，但未给出数字。Graffer AI Studio 提供完全支援方案和仅工具方案，未公开价格（[页面](https://graffer.jp/ai-solution/products/graffer-ai-studio)）。唯一公开价格结构的是业务专用 AI 代理服务：开发费 50 万日元起，月费 2 万日元起，AI 模型使用费另计，标准交付期 1 个月，最短 2 周（[2025-10-07](https://prtimes.jp/main/html/rd/p/000000103.000038525.html)、[页面](https://graffer.jp/ai-solution/ai-consulting-development)）。Graffer Platform 的服务已登记在数字厅的数字市场（Digital Marketplace）上；公司称 Graffer 要介護認定照会是首个通过该市场被采用的服务（[2025-11-17](https://graffer.jp/news/6904)）。

### 历年公开规模

| 日期 | 公开数字 | 来源 |
|---|---|---|
| 2019-01-21 | 团队约 10 人 | [BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising) |
| 2019-03 → 2023-03 | 政府团体数：2（2019-03）、6（2020-03）、50（2021-03）、102（2022-03）、160（2023-03） | [公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 2022-02-16 | お悩みハンドブック全国版累计用户超过 10 万 | [公告](https://graffer.jp/news/3381) |
| 2023-03-14 | “全国140以上の自治体”；政令指定都市 70% | [2023-04-14](https://graffer.jp/news/4516) |
| 2024-10-24 | “全国200以上の自治体” | [公告](https://graffer.jp/news/6054) |
| 2025-04 → 2025-06 | 发布频率每天 6.18 次 | [资料，2025-07-31](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge) |
| 发布于 2025-07-31 | 273 个团体；覆盖居民超过 4,100 万 | [资料，2025-07-31](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge) |
| 2026-03 | “270団体超”；约 7,000 万居民 | [公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 资料 2026-07 版 | Graffer AI Solution 已支援“2.8万人超”（超过 28,000 名）商务人士使用生成式 AI | [公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 2025-04 → 2026-03 | Graffer スマート申請用户满意度 4.3/5，约 80 万名受访者 | [スマート申請页面](https://graffer.jp/governments/solution-smart-apply) |
| 2026-07 | Graffer スマート申請上约 7 万个共享表单；约 3,000 个表单由 AI 根据纸质样式生成 | [スマート申請页面](https://graffer.jp/governments/solution-smart-apply) |
| 无日期，访问于 2026-10-11 | “7215 万人の市民が対象”、“254 の政府機関での案件実績”；お悩みハンドブック使用者超过 60 万人 | [政府页面](https://graffer.jp/governments)、[个人与事业者服务页面](https://graffer.jp/services) |

### 已公布客户与合作伙伴

仅列代表性案例；[新闻索引](https://graffer.jp/news)共有 510 条，大部分是单个自治体的采用公告。

| 日期 | 相关方 | 公告内容 |
|---|---|---|
| [2019-08-19](https://graffer.jp/news/1396) | Yahoo! JAPAN | 生活信息领域的业务合作 |
| [2021-03-30](https://graffer.jp/news/2648) | 福岡市 | 基于 Graffer スマート申請的全厅电子申请系统 |
| [2021-09-03](https://graffer.jp/news/2935) | 滋賀県 | 共同采购スマート申請、手続きガイド和窓口予約 |
| [2023-04-26](https://graffer.jp/news/4561) | ニチイ学館 | Graffer AI Studio 的概念验证 |
| [2023-10-12](https://graffer.jp/news/4924) | TOPPAN 集团 | 提供 Graffer AI Studio |
| [2025-02-26](https://graffer.jp/news/6439) | ミスターマックス | 总部全部门采用 Graffer AI Solution |
| [2025-04-22](https://graffer.jp/news/6589) | 東京消防庁 | スマート申請与其电子申请系统对接 |
| [2025-05-30](https://graffer.jp/news/6613) | 京都市 | 所有区役所和支所的总机采用 Graffer Call |
| [2025-08-21](https://graffer.jp/news/6737) → [2026-05-29](https://graffer.jp/news/7399) | 国土交通省 | 建設業法举报热线 DX；结果称电话量减少约 35% |
| [2025-12-02](https://graffer.jp/news/6970) | ROUTE06 | 业务合作，将其需求定义工具“Acsim”与 AI駆動開発プログラム 结合 |
| [2026-01-06](https://graffer.jp/news/7035) | 港区 | AI 代理接听电话试点（Graffer AI オペレーター） |
| [2026-03-10](https://graffer.jp/news/7211) | リコー | AI駆動開発プログラム；公告称原需两个月的工序在三周内完成，Pull Request 数量翻倍 |
| [2026-05-28](https://graffer.jp/news/7405) | デジタル庁 | 完成审阅系统开发文档的 AI 代理概念验证 |
| [2026-06-18](https://graffer.jp/news/7446) | 大阪府 | 加入大阪府行政AIエージェントコンソーシアム |
| [2026-08-31](https://graffer.jp/news/7705) | 福岡市 | AI 辅助补助金审查试点 |

### 公开计划

- Govtech：公司称将从面向居民的系统扩展到职员使用的后台业务系统，实现“エンドツーエンドの業務処理フロー”（[公司介绍资料，2026-07 版](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。收购行政システム研究所后，计划交叉销售 Graffer Platform，并为自治体职员增加新服务（[2026-04-28](https://graffer.jp/news/7317)）。
- Food & Beverage：利用 AI 代理将食品行业的数据转换成本降至五分之一以下（[公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。Databridge 计划扩展到电商平台、HR（人才派遣）、制造和服装领域（[2025-11-19](https://graffer.jp/news/6911)）。
- AI 驱动开发：“Prompt to App: システム開発不要な世界の実現”（[公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。

---

## 创始人

**石井 大地（Daichi Ishii）**——代表取締役 / 創業者（[公司页面](https://graffer.jp/company)）。

- 考入东京大学医学部，后转入文学部并毕业。2011 年获第 48 届文藝賞（河出書房新社），以小说家身份出道（[公司页面](https://graffer.jp/company)）。
- 曾创立和经营多家公司，并在初创企业中开展新业务。在 Recruit Holdings 的 Media & Solutions SBU 负责业务战略制定和对日本国内外科技公司的业务开发投资。2017 年创立 Graffer（[公司页面](https://graffer.jp/company)）。[BRIDGE（2019-01-21）](https://thebridge.jp/2019/01/graffer-fundraising)另称，他在加入投资公司之前曾任 Medley 执行董事（執行役員）；公司自己的履历未提及 Medley。
- 他在创始人寄语中称，创始团队中没有人在政府领域工作过，选择这一领域是受创业时一位投资人的启发（[关于我们](https://graffer.jp/about)）。BRIDGE 称提出 GovTech 方向的是 Incubate Fund GP 村田祐介，他现为 Graffer 董事（[BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising)）。
- 自 [2024-02-06](https://graffer.jp/news/5276) 起任スタートアップ協会理事。[2026-07-28](https://graffer.jp/news/7552) 宣布出任内阁人事局“AI时代国家公务员应有形态”研讨会成员。
- 著作：《こうすればうまくいく 行政のデジタル化》（2020-12-25）和《AI駆動開発チームの作り方・育て方 生産性20倍アップのソフトウェア開発》（日经 BP，2026）（[2026-07-28](https://graffer.jp/news/7552)、[2026-02-16](https://graffer.jp/news/7137)）。

### 主要管理层

摘自[公司页面](https://graffer.jp/company)（访问于 2026-10-11）：

| 姓名 | 所列职位 | 公开背景 |
|---|---|---|
| 小寺 広晃 | 取締役 兼 COO（自 2026-05 担任现职） | 2014 年加入 Recruit Lifestyle（QR 支付）；2019 年加入；2023-03 起任 CBO，2026-01 起任 COO，负责生成式 AI 产品 |
| 澤田 淳 | 輪番社長 兼 Senior Vice President of Business；執行役員（GovTech本部） | 3M Japan FP&A；GCA（Houlihan Lokey）M&A；2021-10 加入；自 2026-10 任輪番社長 |
| 羽生 和馬 | Senior Vice President of Corporate | GYAO 人事部长；Yahoo Japan 人事；2021-05 加入 |
| 河治 寿都 | Senior Vice President of Engineering；執行役員（エンジニアリング本部） | GREE 应届工程师；在跨境电商、IoT 和医疗健康领域任 Tech Lead／VPoE／EM；2025-04 加入，负责 Graffer AI Studio；自 2026-01 担任现职 |
| 黑﨑 脩 | Vice President of AI Solution Development | Simplex（外汇交易系统）；参与创业；2021-02 以 PM 身份加入；2023-03 起任 VP of Product 兼 VP of Engineering；自 2026-01 担任现职 |
| 市川 翔子 | Vice President of AI Solution Development | 三菱商事；新加坡战略咨询公司；2020 年加入；2025-07 起任 VP of Business（Enterprise） |

外部董事包括澤山陽平（Coral Capital 创始合伙人）、中谷昇（前 INTERPOL IGCI 首任总局长；NEC CSO；[2023-11-01](https://graffer.jp/news/5053) 就任）和瀧俊雄（Money Forward 联合创始人）。村田祐介（Incubate Fund 代表合伙人）任董事。紫垣拓也于 [2021-04-01](https://graffer.jp/news/2679) 被宣布出任 CFO，但未出现在当前公司页面。公司介绍了“社長輪番制”（社长轮值制），澤田自 2026-10 被列为輪番社長（[公司页面](https://graffer.jp/company)、[公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。资料所列员工背景包括 IT（Recruit、AWS、Uzabase、Works Applications、Yahoo）、政府（総務省、経産省）、商社和专业服务机构。

---

## 融资

| 日期 | 轮次（公司用语） | 金额 | 投资者 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2019-01-21 | 資金調達（无轮次名称；BRIDGE：J-KISS 可转换工具，由 500 Startups Japan 领投） | 1.8 亿日元 | 500 Startups Japan、インキュベイトファンド、个人投资者 | — | [Graffer](https://graffer.jp/news/735)、[BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising) |
| 2019-12-20 | シリーズA（第三者割当増資） | 约 4.5 亿日元 | Coral Capital、インキュベイトファンド（均为原有投资者） | 约 7.2 亿日元 | [Graffer](https://graffer.jp/news/1524) |
| 2020-07-16 | 第三者割当増資；与凸版印刷资本业务合作 | 约 2.5 亿日元 | 原有股东、凸版印刷 | 本轮后含准备金资本金 975,000,313 日元 | [Graffer](https://graffer.jp/news/1754) |
| 2021-04-01 | シリーズB | 约 12 亿日元 | 原有投资者 | 约 22.2 亿日元 | [Graffer](https://graffer.jp/news/2679) |
| 2023-04-14 | 資本業務提携 | 未披露 | チェンジホールディングス | — | [Graffer](https://graffer.jp/news/4516) |

轮次名称遵循公司公告。Incubate Fund 参与了 2019-01 轮和 Series A；Series B 公告只写“原有投资者”。TOPPAN Holdings（原凸版印刷）和 Change Holdings 被[公司页面](https://graffer.jp/company)列为主要股东。2019-01 轮与 Graffer 法人証明書請求的发布同时公布，Series A 与新设神户办公室同时公布，Series B 与 CFO 任命同时公布。在[新闻索引](https://graffer.jp/news)和 [PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/38525) 上均未找到 2023-04 之后的融资公告（检查于 2026-10-11）。

---

## 工程

### 技术栈与平台

**由公开资产或公司文件确认：**

- **AWS**——出现在 Graffer Platform 和 Graffer AI Studio 两份 ISO/IEC 27017 认证范围中。两份白皮书均称服务使用 Amazon Time Sync Service（[公司页面](https://graffer.jp/company)、[Platform 白皮书](https://graffer.jp/legal/whitepaper)、[AI Studio 白皮书](https://console.graffer.jp/aistudio/docs/whitepaper)）。公司 note 文章写道“グラファーはAWS環境でずっと開発してきました”（[note，2026-07-10](https://note.graffer.inc/n/nd0a48a1d33e0)）。
- **MongoDB Atlas**——出现在两份 ISO/IEC 27017 认证范围中（[公司页面](https://graffer.jp/company)）。
- **Twilio**——Graffer Call 使用；发送给 Twilio 的通话数据（电话号码、通话记录）存储在美国，其他客户数据存储在日本（[Platform 白皮书](https://graffer.jp/legal/whitepaper)，第四版 2024-03-01）。
- **SB Payment Service**——处理 Graffer 服务的卡支付（[Platform 白皮书](https://graffer.jp/legal/whitepaper)）。
- **LLM 提供方**——AI Studio 知识库使用 Azure OpenAI Service（[2023-08-24](https://graffer.jp/news/4830)）；AI Studio 提供 GPT、Gemini 和 Claude 模型（[页面](https://graffer.jp/ai-solution/products/graffer-ai-studio)）。
- **主权 AI 验证环境**——在さくらのクラウド上运行数字厅开源的“ガバメントAI 源内”代码，并搭配国产 LLM：LLM-jp 和 PLaMo（[2026-06-22](https://graffer.jp/news/7451)）。
- **Next.js、LLM、向量检索**——列为近期采用的新技术（“新技術採用（LLM、ベクトル検索、Next.jsへの移行）”），另有跨产品共用的设计系统（[产品开发资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)）。
- **Atlassian Statuspage**——[grafferstatus.jp](https://www.grafferstatus.jp/) 状态页列出 AI Studio 和 Graffer Databridge（访问于 2026-10-11）。

**来自招聘信息（当前 HERP 职位，访问于 2026-10-11；各职位“開発環境”部分内容相同）：**

| 层 | 所列内容 |
|---|---|
| 前端 | TypeScript；React、Next.js；AWS、Docker、Terraform；Storybook、Chromatic |
| 后端 | Go、Python；Gin、Flask；AWS、Docker、Kubernetes；PostgreSQL、MySQL、MongoDB；GraphQL、REST、gRPC |
| 通用 | GitHub Actions、Argo（CI/CD）；Sentry、Datadog；Figma；GitHub、Renovate；GitHub Copilot、Devin、Cursor、v0；Jira、GitHub Issues；Slack、Google Workspace、esa |

来源：[全周期工程师](https://herp.careers/v1/graffer/QE1EVzBa9GqT)、[SRE](https://herp.careers/v1/graffer/8JGn2ARp6KPL)、[安全工程师](https://herp.careers/v1/graffer/7FDCJHZzT21G)。SRE 和安全工程师职位的要求中还将 Google Cloud 与 AWS 并列，这仅是招聘要求。2026-07 版公司介绍资料列出正在使用的工具有 GitHub Copilot、Cursor 和 Claude Code。2025-10 的公告称，公司自 2023 年初起原则上要求所有开发成员使用生成式 AI 编码工具（[2025-10-06](https://graffer.jp/news/6834)）。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| Graffer スマート申請 | 带模板的表单生成器，可在自治体之间共享表单；根据上传的纸质样式由 AI 生成表单；My Number 卡身份验证（隐私政策列出公司的 Graffer電子署名アプリ 和数字厅的マイナアプリ）；事前和事后支付；CSV 导出和 kintone 集成 | [页面](https://graffer.jp/governments/solution-smart-apply)、[隐私政策](https://graffer.jp/legal/privacy-policy) |
| Graffer Call | 按键 IVR，由 AI 分流到对应部门；短信发送 URL；批量自动外呼并追踪结果；职员可编辑话术场景 | [2024-08-16](https://graffer.jp/news/5898) |
| Graffer AI オペレーター | 语音识别，根据登记的知识库回答，带上下文转接职员，生成通话摘要和转写 | [2025-10-03](https://graffer.jp/news/6822) |
| Graffer AI Studio | 多模型对话、RAG、Assistants API 代码执行（[2024-04-12](https://graffer.jp/news/5476)）、任务库（[2024-06-27](https://graffer.jp/news/5693)）、图像生成（[2025-09-30](https://graffer.jp/news/6811)）、模型自动选择（[2025-10-30](https://graffer.jp/news/6880)）、AI Labs（[2025-06-25](https://graffer.jp/news/6650)）；每日备份，存储在日本境内 7 天 | [页面](https://graffer.jp/ai-solution/products/graffer-ai-studio)、[白皮书](https://console.graffer.jp/aistudio/docs/whitepaper) |
| Graffer Databridge | 制造商上传规格书，AI 代理提取字段、换算单位并标出缺漏；批发商一键导出零售商指定的 PDF 或 CSV；系统内聊天用于修改请求 | [2025-11-19](https://graffer.jp/news/6911) |
| 本地 LLM 文档处理 | 在 PC 或本地部署环境运行，不向云端 LLM 发送数据；无需模板即可提取字段，支持标记识别（OMR），并将结果分为自动处理／需人工确认／难以判断 | [2026-06-03](https://graffer.jp/news/7414) |
| 文档审阅 AI 代理（MVP） | 读取基本设计书和测试计划书，按检查清单核对并提出修改建议；估计审阅时间最多缩短 50% | [2026-05-28](https://graffer.jp/news/7405) |
| AI 驱动的遗留系统迁移 | 为大型企业核心系统上云项目，从源代码逆向生成规格书 | [note，2026-07-22](https://note.graffer.inc/n/naa4850501c58) |
| 平台内部 | SRE 职责包括设计、构建和运营微服务平台（多租户架构经验为优先条件）；另有一个基础设施仓库按环境保存部署配置 | [SRE 职位](https://herp.careers/v1/graffer/8JGn2ARp6KPL)、[2022-12-08 访谈](https://career.graffer.inc/inside-graffer/engineer-real-3) |

**开发组织。** 公司称，自创立以来，Product Manager 和 Product Developer 各自负责功能从发现问题、需求、设计、实现、测试、发布到运营的全过程，不按工序分工（“プロダクト志向×多能工”）（[产品开发资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)）。自 2026-01 起，工程由河治（SVP of Engineering）领导，黑﨑负责 AI Solution 开发（[Findy，2026-06-17](https://findy-code.io/pick-up/interviews/graffer-engineer)）。“AI Driven Development”（AIDD）团队负责受托开发（[note，2026-07-22](https://note.graffer.inc/n/naa4850501c58)）。Platform 团队负责安全、SRE 和共用后端基础设施（[SRE 职位](https://herp.careers/v1/graffer/8JGn2ARp6KPL)）。

### 招聘所需技术背景

- **全周期工程师**——必需：使用过 AWS、GCP 或 Azure 云基础设施（个人使用也算）；从前端到后端的全栈开发（个人项目也算）；在一项服务上持续开发和运营（含用户咨询）至少六个月；团队开发经验，包括代码审查。优先：撰写需求文档、基本设计书、ADR、PRD 或设计文档；微服务或 DDD；测试；用生成式 AI 构建 Web 服务；自行策划 Web 服务；复杂业务系统领域；带领或管理工程团队（[职位](https://herp.careers/v1/graffer/QE1EVzBa9GqT)）。
- **SRE**——必需：Web 应用开发；构建和运营容器环境与集群（Docker、Kubernetes）；Web 与网络安全知识；在 AWS 和 Google Cloud 上的基础设施；基础设施即代码（Terraform、CloudFormation）；使用 Datadog 等工具监控。优先：微服务和多租户架构、Go、DevSecOps（[职位](https://herp.careers/v1/graffer/8JGn2ARp6KPL)）。
- **安全工程师**——必需：Web 应用开发、云安全监控与运营、深入的 Web 安全知识、事件响应。优先：微服务及 AWS／Google Cloud 上的安全事件审计、用 Go 进行安全编程、SOC 2 或 ISO 认证工作、通过软件实现企业安全自动化（[职位](https://herp.careers/v1/graffer/7FDCJHZzT21G)）。
- **产品经理／高级全周期工程师**——必需：规划、构建、测试和运营 Web 产品；担任过产品负责人并负责路线图；主导跨 UI 设计、工程和市场的决策（[职位](https://herp.careers/v1/graffer/6tLzIUrHM_e-)）。
- **Solution Director（AI Solution）**——必需：系统开发项目管理；从需求到详细设计的系统设计；数据库、API 和类／模块设计。优先：架构与非功能设计（可扩展性、可用性、安全）、SIer IT 咨询、在开发流程中使用生成式 AI（[职位](https://herp.careers/v1/graffer/hF0M8OCAIdqq)）。

### 行业领域

日本地方政府行政——居民手续、LGWAN 网络、My Number 卡身份认证、自治体采购、护理保险认定、公会计；省厅业务方面则涉及建設業法举报热线、数字厅文档审阅等国家系统。企业业务涉及食品流通商品数据（食品規格書）和企业系统迁移。招聘 FAQ 称不需要事先了解政府业务；现有员工大多入职前没有这方面知识，可通过入职培训和学习会掌握（[招聘网站](https://career.graffer.inc/)）。2022 年的工程师访谈称，制定功能规格时需要考虑个人信息和行政文书的处理规则（[访谈](https://career.graffer.inc/inside-graffer/engineer-real-3)）。

### 工作条件

| 项目 | 详情 | 来源 |
|---|---|---|
| 远程与地点 | 可完全远程；部分团队设有到岗日。成员分布在北至青森、南至冲绳的各地，公司称自创立起即以“フルリモート・フルフレックス”运营。职位所列工作地点为千驮谷办公室 | [公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)、[招聘 FAQ](https://career.graffer.inc/)、[2025-11-27](https://career.graffer.inc/inside-graffer/beyond-remote-work) |
| 工时 | 无核心时间的弹性工时；双休；国定假日和年末年初假期 | [职位](https://herp.careers/v1/graffer/QE1EVzBa9GqT) |
| 薪资（年薪，含每月 45 小时固定加班费） | 全周期工程师 540 万–1,200 万日元；SRE 600 万–1,200 万日元；安全工程师 720 万–1,200 万日元；PdM／高级工程师 780 万–1,500 万日元；Solution Director 780 万–1,080 万日元 | [HERP 职位](https://herp.careers/v1/graffer)；访问于 2026-10-11 |
| 股权 | “ストックインセンティブ制度”：每月从工资中扣除固定金额购买公司股票 | [公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 调薪与人事制度 | 每月调薪；角色等级制；每月实时评估，不设评分等级 | [公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)、[招聘 FAQ](https://career.graffer.inc/) |
| 福利 | 入职首月 5 万日元远程环境补贴；每月 3 万日元生产力提升津贴；公司租赁住房；购书补贴；团队午餐补贴；関東ITソフトウェア健康保険組合；育儿假（有取得实例） | [公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)、[职位](https://herp.careers/v1/graffer/QE1EVzBa9GqT) |
| 入职培训 | 为每人定制的工程师训练营；三个月的伙伴（buddy）制度 | [公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) |
| 副业 | 经批准并遵守所列规则可从事副业 | [招聘 FAQ](https://career.graffer.inc/) |
| 试用期 | 三个月，期间条件不变 | [职位](https://herp.careers/v1/graffer/QE1EVzBa9GqT) |
| 选拔流程 | 书面筛选、1–3 次面试、录用面谈；最终面试和录用面谈原则上在办公室进行；约 3–4 周 | [招聘 FAQ](https://career.graffer.inc/) |
| 初级人员与实习生 | 产品开发资料称，Product Developer 入职时不要求全栈经验，有多名成员以 2–4 年经验入职；设有 Intern 职位类别 | [产品开发资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)、[招聘网站](https://career.graffer.inc/) |
| 工作语言与签证 | 未说明；未找到英文职位 | 见“备注” |

---

## 备注

### 未公开披露

以下结论的搜索范围（2026-10-11）：graffer.jp（两个站点地图、公司页面、关于我们、政府及各产品页面、省厅页面、个人与事业者服务页面、AI Solution 各页面、新闻索引全部 51 页、法律页面和 Platform 白皮书）；console.graffer.jp 上的 AI Studio 白皮书；career.graffer.inc 及其 Inside Graffer 文章；全部十个 HERP 职位；note.graffer.inc（13 篇）；Speaker Deck（5 份资料）；PR TIMES 公司页面；GitHub API；Qiita；Zenn；TokyoDev；Japan Dev；Wantedly；国税厅法人番号公表网站；ISMS 登记；作为线索的 INITIAL 和 HERP 公司资料；BRIDGE；Findy。检索名称：グラファー、株式会社グラファー、Graffer、Graffer, Inc. 及各产品名，日文和英文。

- **营收与利润。** 公告、资料和公司网站中均未找到数字。未在官报（官報）中检索決算公告。
- **估值。** 公司未公布。INITIAL 显示截至 2023-04-26 的投后估值估算为 108.1 亿日元（10,810 百万日元）（[INITIAL](https://initial.inc/companies/A-30003)），HERP 显示“評価額 101.9 億円”（[HERP 公司资料](https://herp.careers/careers/companies/graffer)）。两者都是数据库估算值。
- **2021 年后的金额。** Change Holdings 投资及任何后续轮次的金额；行政システム研究所、5Minutes 和 KURASERU 业务的收购价格。
- **工程人员数量。** 资料只给出员工总数 81 人，未找到工程人员细分。
- **价格。** Graffer Platform 各服务和 Graffer AI Studio 均无价目表；只有业务专用 AI 代理服务公开了价格结构。
- **工程博客。** 没有专门的工程博客。技术内容散见于 Speaker Deck 演讲、招聘网站和 note 文章。[Qiita 组织](https://qiita.com/organizations/graffer)有 27 篇文章，最新一篇日期为 2019-10-01。未找到 Zenn 发布页。
- **开源。** GitHub 组织 [`graffer-inc`](https://github.com/graffer-inc)（“A Tokyo-based Government Tech Startup”，创建于 2017-12-01）有 13 个公开仓库，其中 12 个是 fork；唯一的原创仓库 `react-native-compressed-jsbundle-expo-module` 最后推送于 2024-12-24。
- **工作语言、签证担保、英文职位。** 未说明。在 TokyoDev 和 Japan Dev 上均未找到 Graffer 的职位（Japan Dev 公司 URL 返回 404）。
- **LGWAN-ASP 登记。** 公司页面称支持 LGWAN，但 J-LIS 服务清单返回 HTTP 403，未能核实。
- **离职率。** 未公开。

### 不同来源之间的不一致

- **政府业务覆盖面。** 公司介绍资料称截至 2026-03 为“270団体超”、约 7,000 万居民，而同一资料第 14 页写“4,000万人超の人口カバー / 導入団体270+”（[资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。其他数字：“250超の自治体導入 / 7,000万人以上”（同一资料的服务地图和[关于我们页面](https://graffer.jp/about)）；“全国250以上の自治体”（[2026-04-28](https://graffer.jp/news/7317)、[2026-06-30](https://graffer.jp/news/7505)）；273 个团体、超过 4,100 万居民（[2025-07-31 资料](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge)）；“7215 万人”和“254 の政府機関”（[政府页面](https://graffer.jp/governments)；访问于 2026-10-11）。各来源使用的单位不同——自治体、团体、有项目的政府机构——且都未定义计数口径。
- **含准备金的资本金。** 975,000,313 日元（[2020-07-16](https://graffer.jp/news/1754)）；2,205,721,759 日元（[2021-04-01](https://graffer.jp/news/2679)）；1,798,276,785 日元（[2023-04-14](https://graffer.jp/news/4516)）；1,544,977,927 日元（[2024-10-24](https://graffer.jp/news/6054) 起及[公司页面](https://graffer.jp/company)）。该数字在 2021 年后下降；未找到解释下降原因的公告。PR TIMES 显示“15億4497万円”，未注明是否含准备金（[PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/38525)）。
- **累计融资。** 已披露的 2019 年两轮合计 6.3 亿日元，而 Series A 公告称累计约 7.2 亿日元。7.2＋2.5＋12 亿日元合计 21.7 亿日元，而 Series B 公告为约 22.2 亿日元（[2019-12-20](https://graffer.jp/news/1524)、[2021-04-01](https://graffer.jp/news/2679)）。HERP 显示“累計調達額 29.1 億円”，系根据登记资料估算（[HERP 公司资料](https://herp.careers/careers/companies/graffer)）。
- **2019-01 的融资工具。** 公司公告称为来自三类投资者的資金調達（[公告](https://graffer.jp/news/735)）；BRIDGE 更正其报道，称这是由 500 Startups Japan 领投的 J-KISS（新股预约权）轮（[BRIDGE](https://thebridge.jp/2019/01/graffer-fundraising)）。
- **Graffer Call 发布时间。** 产品开发资料的时间线将 Graffer Call 发布标为 2023-06（[产品开发资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian)）。宣布“提供を開始”的公告日期为 [2024-08-16](https://graffer.jp/news/5898)，而大東市的采用公告在其之前，于 [2024-07-22](https://graffer.jp/news/5791) 发布。
- **总部搬迁。** 2019-12-20 公告称总部于 2019 年 6 月从神宫前迁至千驮谷（[公告](https://graffer.jp/news/1524)）。国税厅记录的登记地址变更日期为 2019-11-01（[国税厅](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779)）。
- **书籍发行日期。** 2026-02-15（[2026-02-16](https://graffer.jp/news/7137)、[AI Solution 网站](https://graffer.jp/ai-solution)）与“2026/2/12発刊”（[2026-07-28](https://graffer.jp/news/7552)）不同。

### 其他

- **业务构成的变化。** 公司起步于面向个人和企业的行政手续服务（くらしのてつづき、Grafferフォーム、法人証明書請求），2018 年起转向自治体 SaaS，2023 年起增加企业生成式 AI，并随 2026-01 的使命变更将 Food & Beverage 和 AI 驱动开发列为独立领域（[2019-01-21](https://graffer.jp/news/735)、[2025-02-27](https://graffer.jp/news/6473)、[公司介绍资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao)）。招聘网站称公司涉足“行政・食品流通・AI駆動開発”（[招聘网站](https://career.graffer.inc/)）。
- **收购。** 自 2024 年以来，公司收购了一项业务和两家公司：KURASERU 的护理认定查询系统（2024-10）、行政システム研究所（2026-04）和 5Minutes（2026-06）。2024-10 的公告称将继续推进并购和业务合作（[2024-10-24](https://graffer.jp/news/6054)）。
- **已披露的安全事件。** 公司于 [2020-10-27](https://graffer.jp/news/1987) 报告，由于文件设置错误，丰岛区保育课使用的 Graffer 手続きガイド页面自 2020-10-01 起可在网上看到用户输入的信息（3 件，16 人）。公司于 [2020-04-29](https://graffer.jp/news/1661) 报告 Graffer 法人証明書請求的证明书申请曾暂时停止。AI Studio 页面称“サービス開始からセキュリティインシデントや大規模障害発生なし”（[页面](https://graffer.jp/ai-solution/products/graffer-ai-studio)；访问于 2026-10-11）。
- **公开文档。** 两条产品线的安全白皮书均公开（[Platform](https://graffer.jp/legal/whitepaper)、[AI Studio](https://console.graffer.jp/aistudio/docs/whitepaper)）；未找到公开的 API 参考文档。
- **新闻渠道。** 同时检查了[新闻索引](https://graffer.jp/news)和 [PR TIMES](https://prtimes.jp/main/html/searchrlp/company_id/38525)。部分 PR TIMES 条目（如 2025-10-07 公布 AI 代理价格的公告）未出现在网站新闻索引中。

---

## 资料来源

**官方**

- [公司官网（日文）](https://graffer.jp/) · [公司页面——董事会、管理层、资本、认证](https://graffer.jp/company) · [关于我们／创始人寄语](https://graffer.jp/about)
- [新闻索引](https://graffer.jp/news)
- [Graffer Platform——政府产品](https://graffer.jp/governments)：[スマート申請](https://graffer.jp/governments/solution-smart-apply) · [手続きガイド](https://graffer.jp/governments/solution-guides) · [窓口予約](https://graffer.jp/governments/solution-booth-reserve) · [Call](https://graffer.jp/governments/solution-call) · [AI オペレーター](https://graffer.jp/governments/solution-ai-operator) · [要介護認定照会](https://graffer.jp/governments/solution-nintei-shoukai) · [認定調査票作成](https://graffer.jp/governments/solution-nintei-chosahyo) · [お悩みハンドブック](https://graffer.jp/governments/solution-compass)
- [省厅页面](https://graffer.jp/ministries) · [个人与事业者服务](https://graffer.jp/services)
- [Graffer AI Solution](https://graffer.jp/ai-solution)：[AI Studio](https://graffer.jp/ai-solution/products/graffer-ai-studio) · [业务专用 AI 代理](https://graffer.jp/ai-solution/ai-consulting-development) · [AI駆動開発プログラム](https://graffer.jp/ai-solution/generative-ai-learning/ai-dev-training) · [Databridge for 食品規格書](https://graffer.jp/ai-solution/ai-databridge/food-kikaku)
- [Graffer Platform 安全白皮书](https://graffer.jp/legal/whitepaper) · [Graffer AI Studio 安全白皮书](https://console.graffer.jp/aistudio/docs/whitepaper) · [隐私政策](https://graffer.jp/legal/privacy-policy) · [状态页](https://www.grafferstatus.jp/)
- [招聘网站](https://career.graffer.inc/) · Inside Graffer：[远程办公，2025-11-27](https://career.graffer.inc/inside-graffer/beyond-remote-work) · [工程师访谈，2022-12-08](https://career.graffer.inc/inside-graffer/engineer-real-3) · [会议报告，2025-10-09](https://career.graffer.inc/inside-graffer/developer_conference_2025)
- [HERP 职位页](https://herp.careers/v1/graffer)：[全周期工程师](https://herp.careers/v1/graffer/QE1EVzBa9GqT) · [SRE](https://herp.careers/v1/graffer/8JGn2ARp6KPL) · [安全工程师](https://herp.careers/v1/graffer/7FDCJHZzT21G) · [PdM／高级工程师](https://herp.careers/v1/graffer/6tLzIUrHM_e-) · [Solution Director](https://herp.careers/v1/graffer/hF0M8OCAIdqq)
- Speaker Deck：[公司介绍资料（2026-07 版）](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao) · [产品开发资料](https://speakerdeck.com/graffer/zhu-shi-hui-she-gurahuahui-she-shao-jie-zi-liao-purodakutokai-fa-bian) · [AI 优先开发，2025-07-31](https://speakerdeck.com/graffer/aiwoqian-ti-tositakai-fa-purosesutomanezimentonobian-ge) · [全周期开发演讲，2026-06-17](https://speakerdeck.com/graffer/sono-yue-jing-wu-li-sitemasen-fdenoxian-niaruhurusaikurukai-fa)
- note：[主权 AI 环境搭建，2026-07-10](https://note.graffer.inc/n/nd0a48a1d33e0) · [AIDD 工程师，2026-07-22](https://note.graffer.inc/n/naa4850501c58)
- [GitHub 组织](https://github.com/graffer-inc) · [Qiita 组织](https://qiita.com/organizations/graffer)

**新闻稿（graffer.jp，日文，较新在前）**

- [福冈市 AI 补助金审查 — 2026-08-31](https://graffer.jp/news/7705) · [都城市認定調査票作成试点 — 2026-08-28](https://graffer.jp/news/7697) · [石井出任内阁人事局研讨会成员 — 2026-07-28](https://graffer.jp/news/7552)
- [收购 5Minutes — 2026-06-30](https://graffer.jp/news/7505) · [主权 AI 环境 — 2026-06-22](https://graffer.jp/news/7451) · [大阪府 AI 代理联盟 — 2026-06-18](https://graffer.jp/news/7446) · [本地 LLM 技术 — 2026-06-03](https://graffer.jp/news/7414) · [国分西日本 Databridge — 2026-06-02](https://graffer.jp/news/7409)
- [国交省热线结果 — 2026-05-29](https://graffer.jp/news/7399) · [数字厅文档审阅 AI 代理 — 2026-05-28](https://graffer.jp/news/7405) · [收购行政システム研究所 — 2026-04-28](https://graffer.jp/news/7317) · [理光 — 2026-03-10](https://graffer.jp/news/7211) · [书籍发行 — 2026-02-16](https://graffer.jp/news/7137) · [港区试点 — 2026-01-06](https://graffer.jp/news/7035)
- [ROUTE06 合作 — 2025-12-02](https://graffer.jp/news/6970) · [发布 Databridge — 2025-11-19](https://graffer.jp/news/6911) · [数字市场 — 2025-11-17](https://graffer.jp/news/6904) · [AI Studio 模型自动选择 — 2025-10-30](https://graffer.jp/news/6880) · [AI駆動開発プログラム — 2025-10-06](https://graffer.jp/news/6834) · [港区采纳 AI オペレーター — 2025-10-03](https://graffer.jp/news/6822)
- [AI Studio 图像生成 — 2025-09-30](https://graffer.jp/news/6811) · [国交省热线项目 — 2025-08-21](https://graffer.jp/news/6737) · [Graffer Call 通话录音 — 2025-07-29](https://graffer.jp/news/6699) · [AI Labs — 2025-06-25](https://graffer.jp/news/6650) · [ISO 27017／27001 — 2025-06-06](https://graffer.jp/news/6618) · [京都市 Graffer Call — 2025-05-30](https://graffer.jp/news/6613) · [东京消防厅对接 — 2025-04-22](https://graffer.jp/news/6589)
- [信息无障碍好案例 2024 — 2025-03-19](https://graffer.jp/news/6490) · [法人証明書請求终止 — 2025-02-27](https://graffer.jp/news/6473) · [Mr Max — 2025-02-26](https://graffer.jp/news/6439) · [Findy Team+ Award 2024 — 2024-11-01](https://graffer.jp/news/6095) · [KURASERU 业务受让 — 2024-10-24](https://graffer.jp/news/6054) · [Graffer Call — 2024-08-16](https://graffer.jp/news/5898)
- [大东市 Graffer Call — 2024-07-22](https://graffer.jp/news/5791) · [AI 任务库 — 2024-06-27](https://graffer.jp/news/5693) · [AI Studio Assistants API — 2024-04-12](https://graffer.jp/news/5476) · [スタートアップ協会理事 — 2024-02-06](https://graffer.jp/news/5276) · [外部董事中谷 — 2023-11-01](https://graffer.jp/news/5053) · [TOPPAN 集团 — 2023-10-12](https://graffer.jp/news/4924)
- [Azure OpenAI 知识库 — 2023-08-24](https://graffer.jp/news/4830) · [AI Studio 正式发布 — 2023-04-26](https://graffer.jp/news/4561) · [Change Holdings 合作 — 2023-04-14](https://graffer.jp/news/4516) · [发布 AI Studio — 2023-03-24](https://graffer.jp/news/4389) · [お悩みハンドブック自治体版 — 2022-12-15](https://graffer.jp/news/4081)
- [ISMAP 撤回 — 2022-04-01](https://graffer.jp/news/3504) · [お悩みハンドブック 10 万用户 — 2022-02-16](https://graffer.jp/news/3381) · [お悩みハンドブック全国版 — 2022-01-27](https://graffer.jp/news/3297) · [J-Startup — 2021-10-20](https://graffer.jp/news/3080) · [滋贺县共同采购 — 2021-09-03](https://graffer.jp/news/2935) · [窓口予約 — 2021-09-01](https://graffer.jp/news/2928)
- [Series B 与 CFO — 2021-04-01](https://graffer.jp/news/2679) · [福冈市 — 2021-03-30](https://graffer.jp/news/2648) · [隐私标志 — 2021-03-12](https://graffer.jp/news/2581) · [丰岛区事件报告 — 2020-10-27](https://graffer.jp/news/1987) · [TOPPAN 合作 — 2020-07-16](https://graffer.jp/news/1754) · [法人証明書請求暂停 — 2020-04-29](https://graffer.jp/news/1661)
- [スマート申請发布 — 2020-04-07](https://graffer.jp/news/1616) · [法人証明書請求 10,000 家 — 2020-02-26](https://graffer.jp/news/1561) · [Series A 与神户办公室 — 2019-12-20](https://graffer.jp/news/1524) · [Govtech Trends — 2019-08-23](https://graffer.jp/news/1402) · [Yahoo! JAPAN 合作 — 2019-08-19](https://graffer.jp/news/1396) · [1.8 亿日元融资 — 2019-01-21](https://graffer.jp/news/735) · [镰仓市手続きガイド — 2018-11-01](https://graffer.jp/news/405)

**PR TIMES（日文）**

- [公司页面](https://prtimes.jp/main/html/searchrlp/company_id/38525) · [业务专用 AI 代理及价格 — 2025-10-07](https://prtimes.jp/main/html/rd/p/000000103.000038525.html)

**第三方报道、登记与档案**

- [国税厅法人番号记录 — 9010401132779（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=9010401132779) · [国税厅记录 — ｇｒａｐｈｅｒ株式会社（日文）](https://www.houjin-bangou.nta.go.jp/henkorireki-johoto.html?selHouzinNo=1011201021353)
- [ISMS 登记 — IS 689557（日文）](https://isms.jp/lst/ind/CR_IS_x0020_689557.html)
- [BRIDGE — 1.8 亿日元融资，2019-01-21（日文）](https://thebridge.jp/2019/01/graffer-fundraising)
- [Findy — 河治与黑﨑访谈，2026-06-17（日文）](https://findy-code.io/pick-up/interviews/graffer-engineer)
- [HERP 公司资料（日文）](https://herp.careers/careers/companies/graffer) · [INITIAL（日文）](https://initial.inc/companies/A-30003)
