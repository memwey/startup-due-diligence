# Naive.ai

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-18。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-18。英文版为原始版本。

## 摘要

截至 2026-08-18，`naive.ai` 只是一个静态单页：一句 "100 × intelligence for the pioneers"、一个指向 `hr@naive.ai` 的 "Join us" 链接，此外别无内容。它由 GitHub 组织 `naiveai-team` 通过 GitHub Pages 提供，该组织创建于 2026-02-24；其唯一仓库 `landing-page` 创建并最后推送于 2026-03-17（[naive.ai](https://naive.ai/)；[GitHub API](https://api.github.com/orgs/naiveai-team)；访问于 2026-08-18）。站点上没有产品、定价、团队、招聘、博客或文档页面，也没有任何法律主体名称。

- 该公司在公开层面与清华大学电子工程系长聘副教授**代季峰（Jifeng Dai）**相关联，但这一关联只来自第三方报道：他的[个人主页](https://jifengdai.org/)与[清华教师页](https://web.ee.tsinghua.edu.cn/daijifeng/zh_CN/index.htm)都完全没有提到 Naive.ai（两者均访问于 2026-08-18）。
- 一篇被大量转载的中文报道称 Naive.ai 完成"约 3 亿美元"融资、估值"约 8 亿美元"，投资方为"一线基金和科技巨头"且"具体机构暂未披露"。其来源链条很薄：所查阅版本发布于 2026-04-26，对该说法只标注"据多家媒体报道"却未点名任何一家，且本身是对一个微信公众号文章的转载（[AITNT](https://www.aitntnews.com/newDetail.html?newId=24460)）。未找到任何通讯社、有采编能力的中文科技媒体或公司声明承载这一轮次 —— 见 `融资`。
- 代季峰自己的主页确实记录了紧邻的上一段经历："2025.5 - 2026.1 | Leader of MiroMind, an AGI lab founded by Shanda. Unfortunately, MiroMind stopped operation in China due to geo-political issues in Jan 2026."（[jifengdai.org](https://jifengdai.org/)；访问于 2026-08-18）。这段离开的具体情形在代季峰与盛大之间存在公开争议 —— 见 `备注`。
- 另有一家完全无关的公司叫 **Naïve**（YC 2025 春季批次，旧金山，`usenaive.ai`，"Autonomous Company Infrastructure"，创始人 Sean Dorje 与 Dennis Zax），搜索引擎与数据库经常把它作为同名结果返回（[Y Combinator](https://www.ycombinator.com/companies/naive)；访问于 2026-08-18）—— 见 `品牌与法律实体`。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 站点 | `naive.ai`，单页，标题 "naive.ai"；正文只有 "100 × intelligence for the pioneers" 与 "Join us" | [naive.ai](https://naive.ai/)；访问于 2026-08-18 |
| 唯一公开联系方式 | `hr@naive.ai`（"Join us" 的 mailto 链接） | [naive.ai](https://naive.ai/) |
| 托管 | GitHub Pages —— `naive.ai` 解析到 `naiveai-team.github.io`，响应带 `server: GitHub.com`；页面 `last-modified` 头为 2026-03-17 | DNS 与响应头观察于 2026-08-18 |
| GitHub 组织 | `naiveai-team`，显示名 "NaiveAI"，网站字段为 `naive.ai`，创建于 2026-02-24，1 个公开仓库，无公开成员 | [GitHub API](https://api.github.com/orgs/naiveai-team)；访问于 2026-08-18 |
| 仓库 | `naiveai-team/landing-page`，创建并最后推送于 2026-03-17，语言 CSS，7 次提交，全部由名为 "Yuntao Chen"（`RogerChern`）的 GitHub 账号提交 | [GitHub API](https://api.github.com/repos/naiveai-team/landing-page)；访问于 2026-08-18 |
| 域名 | `naive.ai` 注册于 2017-12-16，注册商 NameCheap，注册人由 "Privacy service provided by Withheld for Privacy ehf" 隐去，使用 Cloudflare 名称服务器 | WHOIS 读取于 2026-08-18 |
| 域名此前的用途 | 2019 与 2021 年的互联网档案抓取显示的是标题为 "This domain (naive.ai) is for sale." 的停放页 —— 当前用途与更早的注册无关 | [Wayback 存档，2019-06-11](https://web.archive.org/web/20190611204800/http://naive.ai/)、[Wayback 存档，2021-03-02](https://web.archive.org/web/20210302172049/http://naive.ai/) |
| 法律主体 | 站点上未署名；未取得任何以此名称经营的公司登记文件 | 见 `备注` |
| 产品、定价、文档 | 均未公布；`/about`、`/team`、`/careers`、`/jobs`、`/blog`、`/research` 全部返回 HTTP 404，`app.`、`api.`、`docs.naive.ai` 无法解析 | 路径探测于 2026-08-18 |
| 公开关联的创始人 | 代季峰（Jifeng Dai），清华大学电子工程系长聘副教授 —— 该关联仅来自第三方报道 | [AITNT](https://www.aitntnews.com/newDetail.html?newId=24460)、[jifengdai.org](https://jifengdai.org/) |

### 品牌与法律实体

| 名称 | 类型 | 关系 | 来源 |
|---|---|---|---|
| naive.ai | 域名与单页站点 | 本页的调研对象；页面上不出现任何主体名称 | [naive.ai](https://naive.ai/) |
| `naiveai-team` | GitHub 组织 | 发布该站点；其网站字段指向 `naive.ai` | [GitHub API](https://api.github.com/orgs/naiveai-team) |
| Naïve（`usenaive.ai`） | 另一家公司，YC 2025 春季批次，旧金山，8 人，"Autonomous Company Infrastructure"，创始人 Sean Dorje 与 Dennis Zax | 无关的同名冲突；搜索 "Naive AI" 时经常被返回 | [Y Combinator](https://www.ycombinator.com/companies/naive) |
| `naive-ai`（GitHub） | 另一个无关的 GitHub 组织，创建于 2024-01-28 | 仅名称相同；未建立任何关联 | [GitHub API](https://api.github.com/orgs/naive-ai) |
| `naive.ai` 的前持有者 | 域名停放／出售页面，2019–2021 | 同一域名，在当前用途之前是另一种无关用途 | [Wayback，2021-03-02](https://web.archive.org/web/20210302172049/http://naive.ai/) |

在所查阅的任何来源中，都未确立当前 `naive.ai` 的公司登记、司法辖区、高管或法律名称 —— 见 `备注`。

---

## 产品

没有任何公开内容。整个页面只有站点名、"100 × intelligence for the pioneers" 一句话，以及一个 "Join us" 的 mailto 链接；没有产品说明、截图、等候名单、文档、定价或演示（[naive.ai](https://naive.ai/)；访问于 2026-08-18）。

唯一能找到的产品方向表述来自 `融资` 一节所述的第三方报道，其称公司做的是"开源模型的后训练和 AI Agent 方向"，核心团队来自原 MiroMind 成员（[AITNT](https://www.aitntnews.com/newDetail.html?newId=24460)；发布于 2026-04-26）。这个方向与代季峰自述的研究重点 "agentic AI and continual learning" 一致，但并不能由后者证实（[jifengdai.org](https://jifengdai.org/)；访问于 2026-08-18）。没有任何一手来源说明 Naive.ai 在做什么。

### 公开披露的规模变化

| 日期 | 可观察事件 | 来源 |
|---|---|---|
| 2017-12-16 | `naive.ai` 域名首次注册（与当前无关的持有者；至少到 2021 年一直停放待售） | WHOIS 读取于 2026-08-18；[Wayback，2021-03-02](https://web.archive.org/web/20210302172049/http://naive.ai/) |
| 2026-01 | 据代季峰自己的主页，MiroMind "stopped operation in China" | [jifengdai.org](https://jifengdai.org/) |
| 2026-02-24 | GitHub 组织 `naiveai-team` 创建 | [GitHub API](https://api.github.com/orgs/naiveai-team) |
| 2026-03-17 | `landing-page` 仓库创建，推送 7 次提交，设置 `CNAME`；线上页面的 `last-modified` 头至今仍是这个日期 | [GitHub API](https://api.github.com/repos/naiveai-team/landing-page)；响应头观察于 2026-08-18 |
| 2026-04-26 | 第三方报道称完成"约 3 亿美元"融资、估值"约 8 亿美元"，未注明出处 | [AITNT](https://www.aitntnews.com/newDetail.html?newId=24460) |
| 访问于 2026-08-18 | 站点自 2026-03-17 起未变；GitHub 组织仍只有一个仓库、无公开成员 | 2026-08-18 的观察 |

任何一手来源中都不存在用户、客户、营收、人数或产品使用量的数字。

---

## 创始人

**代季峰（Jifeng Dai）**是第三方报道中与 Naive.ai 公开关联的人。以下履历取自他本人的主页与清华教师页，均访问于 2026-08-18。两处都没有提到 Naive.ai。

| 时间 | 职位 | 来源 |
|---|---|---|
| 2005.9 – 2009.7 | 清华大学自动化系本科；"GPA ranking 2/160+" | [jifengdai.org](https://jifengdai.org/) |
| 2009.9 – 2014.7 | 清华大学自动化系博士生，导师周杰教授 | [jifengdai.org](https://jifengdai.org/) |
| 2012.9 – 2013.9 | UCLA VCLA 实验室访问学生，与 Song-Chun Zhu、Ying-Nian Wu 教授合作 | [jifengdai.org](https://jifengdai.org/) |
| 2014.7 – 2019.9 | 微软亚洲研究院视觉计算组研究员，晋升至 Principal Research Manager，负责人为孙剑与郭百宁 | [jifengdai.org](https://jifengdai.org/) |
| 2019.10 – 2022.7 | 商汤研究院执行研究总监，负责人为王晓刚教授 | [jifengdai.org](https://jifengdai.org/) |
| 2022.7 – 至今 | 清华大学电子工程系副教授；"got tenured at 2024"；当前方向为 "agentic AI and continual learning" | [jifengdai.org](https://jifengdai.org/)、[清华教师页](https://web.ee.tsinghua.edu.cn/daijifeng/zh_CN/index.htm) |
| 2022.9 – 2025.2 | 上海人工智能实验室领军研究员，带领上海 AI Lab 与商汤研究院的联合团队做多模态基础模型 | [jifengdai.org](https://jifengdai.org/) |
| 2025.5 – 2026.1 | "Leader of MiroMind, an AGI lab founded by Shanda. Unfortunately, MiroMind stopped operation in China due to geo-political issues in Jan 2026." | [jifengdai.org](https://jifengdai.org/) |

**学术记录。** 他主页所链接的 Google Scholar 档案显示引用 86,431 次、h 指数 83、i10 指数 131（访问于 2026-08-18）。其主页重点列出 InternVL、InternImage、UniAD（CVPR 2023 最佳论文奖）、BEVFormer、Deformable DETR、VL-BERT、Deformable ConvNets 与 R-FCN，其中多项被标注为所在会议最具影响力论文之列（[jifengdai.org](https://jifengdai.org/)、[Google Scholar](https://scholar.google.com/citations?user=SH_-B_AAAAAJ)）。列出的学术服务包括：TPAMI 副编辑、IJCV 编委，以及 NeurIPS、ICLR、CVPR、ICCV、ECCV 的领域主席。

**目前在招的是高校实验室，不是公司。** 他的主页写着："My lab at Tsinghua University is now hiring. If you are interested in internship, Ph.D. program, postdoctoral positions related to agentic AI or continual learning, please send me an email."（[jifengdai.org](https://jifengdai.org/)；访问于 2026-08-18）。

**其他名字。** 联合创始人**朱锡洲（Xizhou Zhu）**只出现在第三方报道中（[AITNT](https://www.aitntnews.com/newDetail.html?newId=24460)）；没有一手来源确认其在 Naive.ai 的角色，不过他确实是代季峰论文的高频合作者（[jifengdai.org](https://jifengdai.org/)）。在一手技术证据中与 Naive.ai 挂钩的唯一名字是 **Yuntao Chen** —— 落地页全部 7 次提交的作者账号（`RogerChern`）；没有来源说明其角色，这些提交本身只能证明该账号发布了这个站点（[GitHub API](https://api.github.com/repos/naiveai-team/landing-page)；访问于 2026-08-18）。

---

## 融资

截至 2026-08-18，在所查阅的公开来源中未找到 Naive.ai 发布的任何融资公告：没有新闻稿、投资人页面或公司声明，站点本身除那一行落地页文案外什么都没有。

| 日期 | 说法 | 金额 | 具名投资方 | 来源链条 |
|---|---|---|---|---|
| 发布于 2026-04-26 | 由清华副教授代季峰创立的 Naive.ai "已完成约3亿美元融资，估值约8亿美元"；方向为开源模型后训练与 AI Agent；核心团队来自原 MiroMind，联合创始人朱锡洲 | 约 3 亿美元融资，估值约 8 亿美元 | "一线基金和科技巨头，具体机构暂未披露" | [AITNT](https://www.aitntnews.com/newDetail.html?newId=24460) —— 只写"据多家媒体报道"却未点名任何一家，且本身转载自微信公众号"水木TsinghuaCent" |
| 无日期的镜像站 | 相同数字，标题冠以"传" | 同上 | 同上 | [jhth.cn](https://www.jhth.cn/live/56926.html) |

该说法无法回溯到一手来源。未在任何通讯社、36 氪或任何标注自采的媒体上找到对应版本；作为源头的微信公众号原文未能取得；也没有任何备案、投资方公告或公司声明予以佐证。Crunchbase 有一个 `naive-ai` 档案，2026-08-18 对自动访问返回 HTTP 403。因此金额、估值、日期、领投方乃至这轮融资是否存在，均未确立 —— 见 `备注`。

---

## 工程

### 技术栈与平台

几乎没有可观察的工程面。以下均确认于 2026-08-18。

- **站点是 GitHub Pages 上的静态页面。** `naive.ai` 解析到 `naiveai-team.github.io` 及 GitHub Pages 的地址段；响应带 `server: GitHub.com`，`last-modified` 为 2026-03-17。注册商处配置了 Cloudflare 名称服务器，但源站是 GitHub Pages。
- **仓库里只有一个落地页，别无他物** —— `naiveai-team/landing-page`，语言 CSS，创建于 2026-03-17，当天 7 次提交（`init landing page`、三组 `Create CNAME`／`Delete CNAME`、`fix gpt typo`），没有 release，没有 star。
- **页面不加载任何分析、错误追踪或第三方脚本**；唯一的外部请求是向 Google Fonts（`fonts.googleapis.com`、`fonts.gstatic.com`）取 Cormorant Garamond、Instrument Serif 与 Space Grotesk 三种字体。
- **不存在任何应用面。** `/about`、`/team`、`/careers`、`/jobs`、`/blog`、`/research` 返回 HTTP 404，`app.naive.ai`、`api.naive.ai`、`docs.naive.ai` 无法解析。
- **没有其他公开代码。** 该组织只有一个仓库、无公开成员；也未找到同名的 npm 或 PyPI 包。

### 招聘所需技术背景

公司未公布任何内容。`naive.ai` 上唯一的招聘信号是 "Join us" 背后的 `hr@naive.ai` mailto 链接，没有岗位、地点、要求或薪酬。代季峰个人主页上的招人启事面向的是清华大学的职位 —— agentic AI 与 continual learning 方向的实习、博士与博士后 —— 而不是公司（[jifengdai.org](https://jifengdai.org/)；访问于 2026-08-18）。

### 行业领域

公开证据只能支撑代季峰本人研究记录所描述的范围：多模态基础模型、视觉感知、自动驾驶感知，以及当前的 "agentic AI and continual learning"（[jifengdai.org](https://jifengdai.org/)、[清华教师页](https://web.ee.tsinghua.edu.cn/daijifeng/zh_CN/index.htm)）。报道中的公司方向 —— 开源模型后训练与 Agent —— 依赖的是 `融资` 一节中那条未经证实的报道。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| 招聘页 | 没有；`/careers` 与 `/jobs` 返回 HTTP 404 | 路径探测于 2026-08-18 |
| 投递渠道 | 仅 `hr@naive.ai` | [naive.ai](https://naive.ai/) |
| 地点、人数、薪资、远程政策、福利 | 未公布 | 见 `备注` |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-08-18）：`naive.ai` 以及对 `/about`、`/team`、`/careers`、`/jobs`、`/blog`、`/research` 与 `app.`、`api.`、`docs.` 子域名的探测；页面的 HTML、样式表与网络请求；`naive.ai` 的 WHOIS；2019 至 2021 年 `naive.ai` 的互联网档案 CDX 索引与抓取；GitHub 组织 `naiveai-team` 及其仓库、提交历史与成员，以及无关的 `naive-ai` 组织；`jifengdai.org` 与清华大学电子工程系教师页；Google Scholar；无关公司 Naïve 的 Y Combinator 档案；Crunchbase；MiroMind 官网；以及针对 "naive.ai"、"代季峰"、"Jifeng Dai"、"朱锡洲" 与所报融资数字的中英文检索。

- **任何法律主体、司法辖区、登记信息或高管。** 站点上不出现主体名称，也未取得任何以 Naive.ai 名义经营的公司登记记录。
- **公司在做什么。** 除落地页外，没有产品说明、路线图、等候名单、演示、文档或仓库。
- **代季峰是否确为创始人、以何种身份。** 这一关联只出现在第三方报道中；他的个人主页与学校页面都不提及该公司，公司页面也没有提到他。
- **团队、人数与地点。** 没有团队页、没有公开的 GitHub 成员、没有对外岗位。以一手证据与公司挂钩的只有落地页的提交者一个名字，且没有来源说明其角色。
- **融资。** 没有公告、备案或具名投资方。流传的数字无法回溯到一手来源。
- **技术、模型或基础设施。** 无从观察；站点是一个没有应用、API 或分析的静态页面。
- **与 MiroMind、盛大或其资产的任何关系。** 仅见于第三方转述；在所查阅的来源中，双方都没有任何一手声明提到 Naive.ai。
- **2026-08-18 无法读取的来源：** Crunchbase（HTTP 403）、Crain Currency 与 The Edge 上彭博社供稿的 MiroMind 报道（HTTP 403），以及作为融资说法源头的微信公众号原文。

### 不同来源之间的不一致

- **公司被安在一个自己页面上完全不提它的人身上。** 第三方报道称代季峰为 Naive.ai 创始人，而[jifengdai.org](https://jifengdai.org/) —— 一个维护得相当细致、履历一直列到 "2025.5 - 2026.1" 的主页 —— 与他的[清华教师页](https://web.ee.tsinghua.edu.cn/daijifeng/zh_CN/index.htm)都没有任何相关表述（两者均访问于 2026-08-18）。
- **融资：被当作事实陈述，却无法回溯。** "约 3 亿美元／约 8 亿美元" 由 [AITNT](https://www.aitntnews.com/newDetail.html?newId=24460) 作为事实陈述，由[镜像站](https://www.jhth.cn/live/56926.html)以"传"字冠名；前者只写"多家媒体报道"却未点名。未找到任何可佐证的一手来源。
- **MiroMind 任职时间。** 代季峰自己的主页写 "2025.5 - 2026.1"（[jifengdai.org](https://jifengdai.org/)）；中文自媒体账号则写 2025 年 3 月加入、2026 年 1 月 18 日卸任"技术顾问"（[新浪财经头条转载](https://t.cj.sina.com.cn/articles/view/2118746300/7e4980bc02001m9jg)）。两种关于职务与时间的描述对不上。
- **与另一家公司的同名冲突。** 数据库与搜索引擎对相同查询会返回 YC 2025 春季批次的 Naïve（`usenaive.ai`，旧金山）；那是一家创始人完全不同的另一家公司（[Y Combinator](https://www.ycombinator.com/companies/naive)）。

### 其他

- **公开足迹只有三个月，而且是静态的。** GitHub 组织创建于 2026-02-24，页面推送于 2026-03-17，此后线上页面再无变化 —— 2026-08-18 抓取时其 `last-modified` 头仍是 2026-03-17。
- **代季峰离开 MiroMind 的具体情形存在公开争议，本页只并列记录双方立场、不做裁断。** 他自己的主页把 MiroMind 在中国停止运营归因于 2026 年 1 月的 "geo-political issues"（[jifengdai.org](https://jifengdai.org/)）。2026 年 4 月由彭博社供稿及其他媒体转载的、标注来自《华盛顿邮报》的报道称，代季峰向该报表示他离开是因为公司要求 AI 研究人员迁往境外，并称 MiroMind 在北京方面提醒不要向境外转移核心人才与成果之后把员工撤出了中国（[首尔经济日报对《华盛顿邮报》报道的转述，2026-04-22](https://en.sedaily.com/finance/2026/04/22/ai-startup-miromind-flees-china-amid-beijings-tightening)；[Crain Currency，彭博社供稿](https://www.craincurrency.com/global/chinese-billionaire-chen-tianqiao-overhauls-ai-startup-after-warning-manus)）。中文自媒体账号则描述了盛大随后发出的、对上述说法提出异议的内部通报（[新浪财经头条转载](https://t.cj.sina.com.cn/articles/view/2118746300/7e4980bc02001m9jg)）。《华盛顿邮报》原文与盛大通报均未直接读到；相关供稿页面 2026-08-18 对自动访问返回 HTTP 403。本页只记录这些说法的存在与出处。
- **MiroMind 自身仍在运营公开站点**，标题为 "MiroMind | General Purpose Solver"（[miromind.ai](https://www.miromind.ai/)；访问于 2026-08-18）。
- **落地页文案是这家公司迄今唯一的对外表述：** "100 × intelligence for the pioneers"（[naive.ai](https://naive.ai/)）。

---

## 资料来源

**官方**

- [naive.ai](https://naive.ai/) —— 全部已公开的站点内容
- [GitHub 组织 `naiveai-team`](https://github.com/naiveai-team) —— [API 记录](https://api.github.com/orgs/naiveai-team) · [`landing-page` 仓库](https://github.com/naiveai-team/landing-page) · [仓库 API 记录](https://api.github.com/repos/naiveai-team/landing-page)
- 该域名此前无关用途的存档 —— [2019-06-11](https://web.archive.org/web/20190611204800/http://naive.ai/) · [2021-03-02](https://web.archive.org/web/20210302172049/http://naive.ai/)

**创始人与学术记录**

- [jifengdai.org —— 代季峰（Jifeng Dai）个人主页](https://jifengdai.org/)
- [清华大学电子工程系 —— 教师主页（中文）](https://web.ee.tsinghua.edu.cn/daijifeng/zh_CN/index.htm)
- [Google Scholar —— Jifeng Dai](https://scholar.google.com/citations?user=SH_-B_AAAAAJ)

**第三方报道与档案**

- [AITNT —— "清华副教授代季峰创立Naive.ai，获约3亿美元融资"，2026-04-26（中文）](https://www.aitntnews.com/newDetail.html?newId=24460) —— 转载自微信公众号"水木TsinghuaCent"；未点名任何来源
- [jhth.cn —— 同一说法的镜像，标题冠以"传…"（中文）](https://www.jhth.cn/live/56926.html)
- [新浪财经头条 —— 自媒体账号关于代季峰履历与 MiroMind 争议的转载文章（中文）](https://t.cj.sina.com.cn/articles/view/2118746300/7e4980bc02001m9jg)
- [首尔经济日报 —— 对《华盛顿邮报》MiroMind 报道的转述，2026-04-22](https://en.sedaily.com/finance/2026/04/22/ai-startup-miromind-flees-china-amid-beijings-tightening)
- [Crain Currency —— 关于陈天桥与 MiroMind 的彭博社供稿（2026-08-18 对自动访问返回 HTTP 403）](https://www.craincurrency.com/global/chinese-billionaire-chen-tianqiao-overhauls-ai-startup-after-warning-manus)
- [MiroMind](https://www.miromind.ai/)
- [Y Combinator —— Naïve（`usenaive.ai`），一家无关的另一家公司](https://www.ycombinator.com/companies/naive)
- [Crunchbase —— Naive.ai 档案（2026-08-18 对自动访问返回 HTTP 403）](https://www.crunchbase.com/organization/naive-ai)
