# Verdent

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-07-29。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-07-29。英文版为原始版本。

## 摘要

Verdent AI, Inc. 开发 **Verdent**，一款智能体编程产品，以桌面应用、VS Code 扩展和 JetBrains 插件三种形态售卖。产品以「计划 → 编码 → 验证」的循环并行运行多个编码智能体，每个智能体在独立的 Git worktree 中工作。产品于 [2025-09-23](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code) 以「Verdent」（IDE 插件）加「Verdent Deck」（桌面端）的组合发布，并在 [2026-04-20](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html) 重新定位为围绕「Manager」展开——由它做计划、派发 worker、把完成的工作放进待审队列。

- 由陈志杰（联合创始人兼 CEO，前字节跳动 / TikTok 算法负责人）和刘晓春（前百度技术与产品负责人）创办（[2025-09-23 新闻稿](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)）；[Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) 还把 Yuyu Zhang 列为联合创始人。
- A 轮由腾讯领投，金额为「数千万美元」，上一轮由红杉中国领投；报道的估值约 2 亿美元（[新浪，2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)；[网易，2025-11](https://www.163.com/dy/article/KFADJCN1055692AH.html)）。公司和投资方均未发布公告确认。
- 员工人数：截至 [2026-05-31](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) 为 20 人，[LinkedIn](https://www.linkedin.com/company/verdent-ai) 显示 11–50 人（无日期，访问于 2026-07-29），[2025 年 11 月的访谈](https://www.163.com/dy/article/KFADJCN1055692AH.html)中说「三四十人」。
- Verdent 自报在 SWE-bench Verified 上使用 Claude Sonnet 4.5 取得 pass@1 76.1%、pass@3 81.2%（[技术报告，2025-11-01](https://www.verdent.ai/blog/swe-bench-verified-technical-report)）。其 SEAlign 论文获 [ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent) 杰出论文奖。
- 产品不绑定单一模型，全部调用第三方前沿模型；所有基础设施和数据都位于美国的 AWS 上（[安全页面](https://www.verdent.ai/security)；无日期，访问于 2026-07-29）。

---

## 基本情况

| 项目 | 详情 | 来源 |
|---|---|---|
| 公开品牌 | Verdent | [官网](https://www.verdent.ai/) |
| 法定名称 | Verdent AI, Inc. | [官网页脚](https://www.verdent.ai/)；无日期，访问于 2026-07-29 |
| 成立 | 公司通稿写「Founded in 2025」 | [2025-09-23 新闻稿](https://www.financialcontent.com/article/bizwire-2025-9-23-verdent-ai-introduces-verdent-and-verdent-deck-new-ai-tools-that-let-human-developers-thrive-to-deliver-complex-enterprise-grade-code) |
| 适用法律 | 加利福尼亚州法律；争议由加州州法院或联邦法院管辖 | [服务条款](https://www.verdent.ai/terms)；生效于 2026-05-25 |
| 总部 | 官网未公布。新闻稿发稿地：先是新加坡，后是旧金山 | [2025-12-19](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/)、[2026-04-20](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html)、[2026-05-21](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical) |
| 注册地 | 新加坡 | [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg)；访问于 2026-07-29 |
| 创始人 | 陈志杰（联合创始人、CEO）、刘晓春（联合创始人）、Yuyu Zhang（联合创始人） | [2025-09-23 新闻稿](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)、[Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) |
| 员工人数 | 20 人（截至 2026-05-31）；LinkedIn 显示 11–50 人 | [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg)、[LinkedIn](https://www.linkedin.com/company/verdent-ai) |
| 投资者 | 腾讯、红杉中国 | [新浪，2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) |
| 联系方式 | hi@verdent.ai（通用）、support@verdent.ai（支持） | [官网](https://www.verdent.ai/)、[区域页面](https://www.verdent.ai/regions) |
| 基础设施 | AWS，所有服务器位于美国 | [安全页面](https://www.verdent.ai/security)；无日期，访问于 2026-07-29 |

官网页脚、关于页面、安全页面和 LinkedIn 主页均为持续更新且没有发布日期的页面；访问于 2026-07-29。[关于页面](https://www.verdent.ai/about-us)写明了公司宗旨和口号（「By developers, for developers」），但没有提到创始人、办公地点或人数。

### 品牌与法律实体

- **Verdent Deck** —— 桌面应用的原名，用于 [2025-09-23 发布](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)和 [Product Hunt](https://www.producthunt.com/products/verdent-deck) 页面。当前官网导航中桌面端就叫「Verdent」。
- **codeck.ai** —— 一个域名，页面上写着「something big is brewing at Verdent.ai」（[codeck.ai](http://www.codeck.ai/)；无日期，访问于 2026-07-29）。[2025-12-19 新闻稿](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/)的媒体联系邮箱使用的是 `@codeck.ai` 域名。两个域名的关系未见公开说明。

---

## 产品

### 功能模块

文档在 [verdent.ai/docs](https://www.verdent.ai/docs/)，覆盖三个形态：**Verdent Desktop**、**Verdent Cloud**（浏览器端 Web 应用开发）和 **Verdent for VS Code**。[下载页面](https://www.verdent.ai/download)另列出 JetBrains 插件。

- **Manager** —— 编排层。据 [Manager 文档](https://www.verdent.ai/docs/verdent-manager/core-features/manager)，它「确定目标，划分阶段（如 setup → core logic → UI → validation），把每个阶段拆成可执行子任务，并决定哪些可以并行」，然后「为每个子任务派发一个专属 worker，并尽可能同时运行」。完成的工作进入 **To Review** 队列，附带改动的文件、决策摘要和 diff 链接。
- **Plan Mode** —— 在写代码前把提示词转成结构化计划；后续增加了需求澄清和 Mermaid 图（[更新日志](https://www.verdent.ai/changelog)，2026-01-17 与 2025-12-31）。
- **Workspaces** —— 每个任务独立的环境，各自有 Git 分支和改动历史（[博客，2026-01-27](https://www.verdent.ai/blog/verdent-your-ai-native-partner)）。
- **Memory** —— Manager 跨任务保留「偏好 —— 框架、命名、架构决策、工作方式」；v2.6.3 增加了每日自动记忆归纳（[更新日志](https://www.verdent.ai/changelog)，2026-07-02）。
- **消息渠道** —— 可从 Slack、Telegram、Discord 和飞书派活（[文档](https://www.verdent.ai/docs/)）。
- **工具集成** —— GitHub、Stripe、Supabase、Notion、Linear（[文档](https://www.verdent.ai/docs/)）；VS Code 扩展支持 MCP 工具（[Marketplace 页面](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent)）。
- **Automations** —— 无需写 cron 表达式即可配置周期性任务（[文档](https://www.verdent.ai/docs/)）。

### 商业化

付费订阅制，[价目表](https://www.verdent.ai/pricing)公开（访问于 2026-07-29）。个人档位为 Free（7 天试用）、Lite、Starter、Pro、Max，价格从每月 5 美元到 179 美元；Teams 按席位计费并统一开票；Enterprise 为定制报价。每个付费档位给出每月额度（credits），目前在基础额度之上还叠加了「限时赠送」，额度用完可加购，页面称加购「不加价」。

[2026-04-02](https://www.verdent.ai/blog/introducing-eco-mode-byok-and-updated-pricing) 增加了两项成本控制手段：**Eco Mode**，更新日志描述为零额度消耗的工作流；以及支持 Anthropic、OpenAI、OpenRouter 密钥的 **BYOK**。免费档位相对发布时是变化：发布时 [Hacker News](https://news.ycombinator.com/item?id=45359339) 上团队回复称「没有免费档」，起步价为每月 19 美元。

### 版本历史

摘自[更新日志](https://www.verdent.ai/changelog)（访问于 2026-07-29）：

| 日期 | 版本 | 条目 |
|---|---|---|
| 2025-09-23 | v1.0.0 | 任务隔离的并行智能体、Plan First、DiffLens Insight |
| 2025-10-25 | v1.2.1 | 支持 Windows 和 Intel Mac |
| 2025-12-03 | v1.5.0 | 相互隔离的并行工作区 |
| 2026-01-22 | v1.11.1 | 代码库索引、Skills 市场、Plan Rules |
| 2026-01-29 | v1.12.0 | 基于 LSP 的 Code Intelligence、Message Queue |
| 2026-03-05 | v1.16.0 | Verdent Team —— 统一账单、席位与权限管理 |
| 2026-04-02 | v1.19.2 | Eco Mode；支持 Anthropic、OpenAI、OpenRouter 的 BYOK |
| 2026-05-14 | v2.2.1 | 工作区重构，Manager/Task 并排面板，内置浏览器 |
| 2026-06-07 | v2.3.9 | 重写的 agent 引擎 |
| 2026-07-10 | v2.7.0 | Multi-Manager 配置 —— 多个 manager 各带独立技能与记忆 |
| 2026-07-28 | v2.8.0 | 折叠式活动流；可输入设计稿、图片和自动化任务的输入框 |

其余条目大多是接入新发布的第三方模型。

### 公开数据的变化

| 日期 | 公布的数字 | 来源 |
|---|---|---|
| 2025-10-01 | Verdent Deck：Product of the Day 第 3 名，301 票 | [Product Hunt](https://www.producthunt.com/products/verdent-deck) |
| 2025-11-01 | SWE-bench Verified pass@1 76.1%、pass@3 81.2%（Claude Sonnet 4.5） | [技术报告](https://www.verdent.ai/blog/swe-bench-verified-technical-report) |
| 2025-12-19 | 宣称并行智能体带来「10 倍」的项目周期加速 | [新闻稿](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/) |
| 2026-01-26 | Verdent：Product of the Day 第 2 名，288 票 | [Product Hunt](https://www.producthunt.com/products/verdent-deck) |
| 2026-04-19 | Verdent 2.0：Product of the Day 第 3 名，256 票 | [Product Hunt](https://www.producthunt.com/products/verdent-deck) |
| 2026-05-21 | Verdent Manager 拿到 Product of the Day 第 3 名；「付费用户增长加速」 | [新闻稿](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical) |
| 访问于 2026-07-29 | VS Code 扩展：36,328 次安装，45 个评分下 4.5/5，v1.6.13（2026-07-23 更新） | [Marketplace](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent) |
| 访问于 2026-07-29 | LinkedIn 4,121 关注者；Product Hunt 1.4K 关注者、6 条评价 5.0 分 | [LinkedIn](https://www.linkedin.com/company/verdent-ai)、[Product Hunt](https://www.producthunt.com/products/verdent-deck) |

用户数、收入和 ARR 均未公开。

### 公司陈述的计划

根据 [2026-04-20 新闻稿](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html)：平台要「更像一支 AI 工程团队」，从代码生成扩展到计划、执行、验证和交付，围绕 chat 优先的协作、并行工作和可信审查展开，覆盖桌面端、VS Code 和 JetBrains。

在 [DeepTech 专访（2025-11-24）](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)中，陈志杰称公司主攻海外市场、采用 SaaS 订阅模式、面向专业工程师群体，并计划在 2025 年 12 月正式推广；他把 Cursor、Devin 列为创业公司层面的竞品，把 GitHub Copilot、Google Antigravity 列为大厂产品。他还表示公司打算向代码审查、测试验证、SRE 运维等场景扩展。谈及报道中的 2 亿美元估值，他形容那「只有美国硅谷竞品初创企业的零头」。

---

## 创始人

**陈志杰** —— 联合创始人兼 CEO。

- 百度首席技术架构师；[The New Stack](https://thenewstack.io/tiktoks-ex-algorithm-chief-launches-verdent-ai-coding-tool/) 给出的时间是 2010–2019 年。被描述为有十年以上编程经验（[DeepTech，2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)）。
- 字节跳动 / TikTok 算法负责人（[2025-09-23 新闻稿](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)）；也被描述为字节数据科学组织负责人（[新浪，2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)）。中文报道称他主导了大规模推荐系统与基础算法平台的搭建，管理过数百名工程师和科学家（[搜狐，2025-11](https://www.sohu.com/a/955425497_122074763)）。
- 联合创办 Verdent AI；[2026-05-21 新闻稿](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical)中头衔为「Founder and CEO」。
- 长访谈：[DeepTech，2025-11-24（中文）](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)、[Tech Talks Daily 播客（英文）](https://techtalksnetwork.com/podcast/tech-talks-daily/episode/3517-how-verdent-ai-is-building-the-next-generation-ai-coding-agents)。

**刘晓春** —— 联合创始人。

- 百度技术与产品负责人（[2025-09-23 新闻稿](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)），负责搜索、推荐广告和电子商务方向（[新浪，2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)）；据报道管理过 300 多人的跨职能团队（[搜狐，2025-11](https://www.sohu.com/a/955425497_122074763)）。

**Yuyu Zhang** —— 联合创始人，由 [Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) 和 [LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/) 列出（访问于 2026-07-29）。

- 佐治亚理工学院博士，2015–2021 年；更早就读于武汉大学（[LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/)）。
- 曾在字节跳动做 AI 研究，参与 TikTok 和抖音的推荐系统，并主导 Seed-Coder 项目（[LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/)）。Seed-Coder 发表为 [arXiv:2506.03524](https://arxiv.org/abs/2506.03524)，列在 Verdent 的[研究页面](https://www.verdent.ai/research)上。
- 所列所在地：旧金山湾区。

**Huangzhao Zhang** —— 在 [2026-04-20 新闻稿](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html)中被引用发言，并在 ICSE 2026 的 [SEAlign 论文](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent)中署名单位为「Verdent AI」；其余作者来自北京大学和武汉大学。

公司没有团队页面。在查阅的资料中，除 CEO 外没有公布其他头衔。

---

## 融资

| 日期 | 轮次 | 金额 | 投资方 | 来源 |
|---|---|---|---|---|
| 2025-11 之前 | 上一轮 | 未披露 | 红杉中国（领投） | [新浪](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) |
| 报道于 2025-11-17 | A 轮 | 「数千万美元」 | 腾讯（领投），红杉中国等老股东跟投 | [新浪](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)、[搜狐](https://www.sohu.com/a/955425497_122074763) |

全部融资信息来自媒体报道，而非公司或投资方公告。[新浪](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)报道称 A 轮没有新基金进入，是老股东加注。估值一处写作「或已突破 2 亿美元」（[搜狐](https://www.sohu.com/a/955425497_122074763)），一处写作 2 亿美元（[网易](https://www.163.com/dy/article/KFADJCN1055692AH.html)）。[Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) 在 2026-07-29 访问时仍记录该公司未融资。

公司官网、Business Wire 和 PR Newswire 上都没有任何轮次的公告，腾讯和红杉中国（HongShan）也没有在 `备注`所述的检索范围内发布过相关公告。

---

## 工程

### 技术栈与平台

| 项目 | 详情 | 证据类型 |
|---|---|---|
| 云 | AWS；「所有基础设施和你的数据都仅位于美国境内」 | 已确认 —— [安全页面](https://www.verdent.ai/security) |
| 模型供应商 | Azure AI Foundry、Google Cloud Vertex API、AWS Bedrock | 已确认 —— [安全页面](https://www.verdent.ai/security) |
| 其他子处理方 | Parallel.ai（网页搜索）、Jina（网页内容抓取）、Stripe（仅账单） | 已确认 —— [安全页面](https://www.verdent.ai/security) |
| 客户端平台 | macOS（Apple Silicon 与 Intel）、Windows；VS Code 与 JetBrains 扩展 | 已确认 —— [下载页面](https://www.verdent.ai/download)、[更新日志](https://www.verdent.ai/changelog) |
| 隔离机制 | Git worktree / 每个智能体一个分支的 codespace | 已确认 —— [更新日志](https://www.verdent.ai/changelog) v1.1.0、[SiliconANGLE](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/) |
| 代码智能 | 基于 LSP；代码库索引 | 已确认 —— [更新日志](https://www.verdent.ai/changelog) v1.12.0、v1.11.1 |
| 远程执行 | SSH 远程服务器支持 | 已确认 —— [更新日志](https://www.verdent.ai/changelog) v1.18.2、[文档](https://www.verdent.ai/docs/) |
| 可扩展性 | MCP 工具、子智能体、配置规则、Skills 市场 | 已确认 —— [Marketplace 页面](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent)、[更新日志](https://www.verdent.ai/changelog) |

提供的模型全部来自第三方：据[价目页面](https://www.verdent.ai/pricing)（访问于 2026-07-29）列出，包括 Claude Fable 5 / Opus 5 / Sonnet 5、GPT-5.6、Gemini 3.1 Pro、GLM-5.2、Kimi K3、MiniMax M3 和 DeepSeek-V4-Pro。查阅的资料中没有迹象显示 Verdent 训练或部署自研的生产模型。

在 [DeepTech 专访（2025-11-24）](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)中，陈志杰称代码量已达到「三四十万行」。

[2025-11-23 发布的一篇第三方试用](https://zhuanlan.zhihu.com/p/1975338816031176069)记录了当时提供的模型 —— Claude Sonnet 4.5、Claude Haiku 4.5、GPT-5-Codex、GPT-5、Kimi-K2-Turbo，VS Code 端的三种模型组合预设（Performance / Balance / Efficiency），用 `@` 调用的自定义 subagent、自定义命令、MCP 服务配置，以及工具内的 Git 提交与回滚。

### 系统

| 系统 | 功能 | 来源 |
|---|---|---|
| Manager / worker 编排 | 把目标拆成阶段和子任务，为每个子任务派一个 worker 并行执行，结果汇入待审队列 | [文档](https://www.verdent.ai/docs/verdent-manager/core-features/manager) |
| 计划 → 编码 → 验证循环 | 改动前先做结构化计划，带显式检查点的 todo 体系，自动测试循环，以及做代码审查的子智能体 | [博客，2026-04-01](https://www.verdent.ai/blog/why-strong-coding-models-fail-at-real-software-engineering-and-how-to-fix-it) |
| 工作区隔离 | 每个智能体一个启用 Git 的 codespace 和虚拟环境，支持提交、PR 和回滚 | [SiliconANGLE，2025-09-23](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/) |
| DiffLens | 把改动摘要和版本差异报告呈现给人工审查 | [更新日志](https://www.verdent.ai/changelog) v1.0.0、v1.7.2 |
| 多模型审查 | 多个模型并行做审查和计划，并检测编辑冲突 | [更新日志](https://www.verdent.ai/changelog) v1.13.0、v1.15.0 |
| Memory | 跨任务保留偏好与约定，每日自动归纳 | [文档](https://www.verdent.ai/docs/verdent-manager/core-features/manager)、[更新日志](https://www.verdent.ai/changelog) v2.6.3 |

### 已发表研究

[研究页面](https://www.verdent.ai/research)列出了与团队相关的论文，其中若干是作者还在字节跳动时发表的：[Seed-Coder](https://arxiv.org/abs/2506.03524)、[Seed1.5-Thinking](https://arxiv.org/abs/2504.13914)、[FullStack Bench](https://arxiv.org/abs/2412.00535) 和 [Multi-SWE-bench](https://arxiv.org/abs/2504.02605)。

**SEAlign**（[arXiv:2503.18455](https://arxiv.org/abs/2503.18455)）获 [ICSE 2026 Research Track](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent) 杰出论文奖（里约热内卢，2026-04-12 至 2026-04-18）。该方法在收集的轨迹上训练智能体，用蒙特卡洛树搜索定位关键决策点，再用 DPO 在这些点上做对齐。公司的 [2026-04-01 博客](https://www.verdent.ai/blog/why-strong-coding-models-fail-at-real-software-engineering-and-how-to-fix-it)称，经过这种训练后 Qwen2.5-Coder-Instruct-14B 在 SWE-Bench-Lite 上从 3.7% 提升到 17.7%，在 SWE-bench Verified 上从 2.8% 提升到 21.8%，并主张智能体失败源于行为不对齐而非编码能力不足。

[SWE-bench Verified 技术报告（2025-11-01）](https://www.verdent.ai/blog/swe-bench-verified-technical-report)称使用 Claude Sonnet 4.5 取得 pass@1 76.1%、pass@3 81.2%，并说明这是生产系统的成绩，「没有针对榜单调优，也没有测试时扩展」，同时对比了同模型下的 Claude Code 和 GPT-5 下的 Codex。该对比出自 Verdent 自己，本文查阅的资料中没有第三方复现。

### 安全状况

来自[安全页面](https://www.verdent.ai/security)（无日期，访问于 2026-07-29）：

- 「正在积极申请 SOC 2 和 ISO/IEC 42001 认证」—— 两者均未表述为已获得。
- 与 Google Cloud Vertex API 和 AWS Bedrock 签有零数据留存协议。Azure AI Foundry 被列为会接触代码数据的子处理方，未说明留存协议。
- 账户数据在删除时立即移除；云备份可能保留至正常留存周期到期。
- 基础设施按最小权限授予；访问 AWS 必须使用 MFA；遵守模型屏蔽名单。
- 「本服务目前不提供对你的代码仓库的索引或分析。」

### 工作条件

官网 [sitemap](https://www.verdent.ai/sitemap.xml)（访问于 2026-07-29）中没有招聘页面，`备注`所述的检索范围内也没有找到任何职位发布。工作语言、办公政策、远程安排、签证支持、薪资和福利均无公开信息。

关于团队构成唯一的数据点是陈志杰所说团队「三四十人」，且「无论是过往绩效还是背景都非常出色」（[DeepTech，2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)；[网易转载](https://www.163.com/dy/article/KFADJCN1055692AH.html)）。

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-29）：verdent.ai 的 sitemap 及其中除 `/docs`、`/blog`、`/guides` 外的全部页面；文档站；更新日志、博客、研究、价目、安全、条款和关于页面；Business Wire、PR Newswire 以及 Fortune/FinancialContent 的新闻稿镜像；以中英文检索「Verdent」「Verdent AI」「Verdent Deck」「陈志杰 Verdent」；对 36kr.com、tmtpost.com、huxiu.com、geekpark.net、pingwest.com、leiphone.com、infoq.cn 的站内定向检索；GitHub 上对 `verdent` 的用户与组织搜索；对 `ruanyf/weekly` 谁在招人板块的 GitHub 代码检索；LinkedIn 公司页与创始人主页；Tracxn、IT桔子和 Product Hunt。

- 未找到招聘页面、职位发布或公开的薪资区间。
- 未找到公开的 GitHub 组织。GitHub 上匹配 `verdent` 的账号均为无关的个人用户。
- 未找到开源仓库、营销博客之外的工程博客，或公司的会议演讲。研究页面链接的学术论文大多早于公司成立。
- 未公开办公地址、法人注册号或注册地。服务条款指向加州法律；Tracxn 记为新加坡；新闻稿发稿地既用过新加坡也用过旧金山。
- 未公布任何用户数、收入或 ARR 数字。
- 按公司自己的[安全页面](https://www.verdent.ai/security)，尚未取得任何安全认证。
- 未找到公司或投资方发布的任何轮次融资公告；本文的融资事实全部依赖 2025 年 11 月的中文媒体报道。
- 在上述站内定向检索中，36氪、钛媒体、虎嗅、极客公园、品玩、雷峰网和 InfoQ 中文站都没有关于该公司的文章，也没有找到 IT桔子 的公司条目。中文报道集中在新浪及其转载体系。

### 不同来源之间的不一致

- **成立时间：**公司通稿写「Founded in 2025」（[2025-09-23 新闻稿](https://www.financialcontent.com/article/bizwire-2025-9-23-verdent-ai-introduces-verdent-and-verdent-deck-new-ai-tools-that-let-human-developers-thrive-to-deliver-complex-enterprise-grade-code)）；DeepTech 专访称公司成立于 2024 年底（[2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)）。
- **联合创始人姓名：**[新浪](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)和[搜狐](https://www.sohu.com/a/955425497_122074763)写作刘晓春，[AI 工具集条目](https://ai-bot.cn/verdent-ai/)写作刘小春。英文新闻稿统一用「Xiaochun Liu」，无法区分。
- **员工人数：**截至 2026-05-31 为 20 人（[Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg)）、11–50 人（[LinkedIn](https://www.linkedin.com/company/verdent-ai)）、2025 年 11 月「三四十人」（[DeepTech](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)）。
- **融资状态：**[Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) 记录该公司未融资；中文媒体报道腾讯领投的 A 轮（[新浪](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)）。
- **创始人数量：**发布新闻稿列出两位创始人（[2025-09-23](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)）；[Tracxn](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg) 和 [LinkedIn](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/) 列出三位。
- **代码仓库索引：**[安全页面](https://www.verdent.ai/security)称服务「不提供对你的代码仓库的索引或分析」，而[更新日志](https://www.verdent.ai/changelog) v1.11.1（2026-01-22）宣布了代码库索引，[发布新闻稿](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)也称产品会「索引代码库」。
- **额度数字：**[价目页面](https://www.verdent.ai/pricing)与公司自己的[对比指南](https://www.verdent.ai/guides/claude-code-vs-verdent)对同样档位、同样价格给出了不同的月度额度，两者都访问于 2026-07-29；[2025 年 9 月的报道](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/)中还有第三个数字。
- **Product Hunt 名次：**[2026-05-21 新闻稿](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical)把 Product of the Day 第 3 名归于「Verdent Manager」；[Product Hunt 页面](https://www.producthunt.com/products/verdent-deck)记录了三次发布，最近一次是 2026-04-19 的「Verdent 2.0」，名次第 3。

### 其他

- 产品是第三方前沿模型之上的一层，而非模型供应方：[价目页面](https://www.verdent.ai/pricing)列出的模型全部来自外部，[安全页面](https://www.verdent.ai/security)显示推理经由 Azure AI Foundry、Google Vertex 和 AWS Bedrock。
- 模型可用性受上游供应商的地域限制影响；[区域页面](https://www.verdent.ai/regions)对因此失去某模型访问权的客户提供 24 小时内退款。
- 定位在十个月内改过两次：[发布时（2025-09-23）](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code)是「agentic coding suite」，[2026 年 1 月](https://www.verdent.ai/blog/verdent-your-ai-native-partner)是「AI-native partner」，[2026 年 4 月](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html)起是「AI engineering team for builders」／「AI 技术联合创始人」。当前[中文首页](https://www.verdent.ai/zh-CN)主打的是非开发者场景 —— 12 小时做出的游戏、桌面陪伴应用、自助分析管道。
- 价目、条款、安全政策、文档和完整更新日志都无需登录即可查看。
- 公司在 [/guides](https://www.verdent.ai/guides) 下发布竞品对比页面，包括[对比 Claude Code](https://www.verdent.ai/guides/claude-code-vs-verdent)和一篇 [AI 编程工具横评](https://www.verdent.ai/guides/ai-coding-tools-comparison-2026)；这些页面上的数字出自公司自己。
- 找到的全部中文报道都可追溯到 2025 年 11 月的两篇原始文章：投资实习所的融资独家（[新浪，2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml)）和 DeepTech 深科技的创始人专访（[新浪，2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml)）。[搜狐](https://www.sohu.com/a/955425497_122074763)、[网易](https://www.163.com/dy/article/KFADJCN1055692AH.html)、[知乎](https://zhuanlan.zhihu.com/p/1976372371272267577)上的版本都是这两篇的转载，并非独立报道。

---

## 资料来源

**官方**

- [Verdent —— 产品官网](https://www.verdent.ai/) · [简体中文](https://www.verdent.ai/zh-CN)
- [关于我们](https://www.verdent.ai/about-us)
- [下载](https://www.verdent.ai/download)
- [价格](https://www.verdent.ai/pricing)
- [安全](https://www.verdent.ai/security)
- [服务条款，生效于 2026-05-25](https://www.verdent.ai/terms)
- [区域与模型可用性](https://www.verdent.ai/regions)
- [更新日志](https://www.verdent.ai/changelog)
- [Sitemap](https://www.verdent.ai/sitemap.xml)
- [文档首页](https://www.verdent.ai/docs/)
  - [Manager —— 核心功能文档](https://www.verdent.ai/docs/verdent-manager/core-features/manager)
- [研究索引](https://www.verdent.ai/research)
- [指南索引](https://www.verdent.ai/guides)
  - [Claude Code vs Verdent](https://www.verdent.ai/guides/claude-code-vs-verdent)
  - [2026 年 AI 编程工具横评](https://www.verdent.ai/guides/ai-coding-tools-comparison-2026)
- [博客](https://www.verdent.ai/blog)
  - [SWE-bench Verified 技术报告 —— 2025-11-01](https://www.verdent.ai/blog/swe-bench-verified-technical-report)
  - [Verdent: Your AI-native Partner —— 2026-01-27](https://www.verdent.ai/blog/verdent-your-ai-native-partner)
  - [强编码模型为何在真实软件工程中失败 —— 2026-04-01](https://www.verdent.ai/blog/why-strong-coding-models-fail-at-real-software-engineering-and-how-to-fix-it)
  - [Eco Mode、BYOK 与价格调整 —— 2026-04-02](https://www.verdent.ai/blog/introducing-eco-mode-byok-and-updated-pricing)
- [codeck.ai](http://www.codeck.ai/)

**新闻稿**

- [Verdent 延续早期势头 —— 2026-05-21](https://natlawreview.com/press-releases/verdent-builds-early-momentum-ai-coding-tools-move-toward-technical)
- [Verdent：面向 builder 的全球首个 AI 工程团队 —— 2026-04-20](https://www.prnewswire.com/news-releases/verdent-the-worlds-first-ai-engineering-team-for-builders-302747211.html)
- [独立桌面版 AI 编程工具重大更新 —— 2025-12-19](https://fortune.com/press-releases/verdent-ai-updates-ai-coding-tool-parallel-tasks-2025-12-19/)
- [Verdent AI 推出 Verdent 与 Verdent Deck —— 2025-09-23](https://www.businesswire.com/news/home/20250923178280/en/Verdent-AI-Introduces-Verdent-and-Verdent-Deck-New-AI-Tools-That-Let-Human-Developers-Thrive-to-Deliver-Complex-Enterprise-Grade-Code) · [含全文的镜像](https://www.financialcontent.com/article/bizwire-2025-9-23-verdent-ai-introduces-verdent-and-verdent-deck-new-ai-tools-that-let-human-developers-thrive-to-deliver-complex-enterprise-grade-code)

**第三方报道与资料**

- [SiliconANGLE —— 发布报道，2025-09-23](https://siliconangle.com/2025/09/23/verdent-launches-agentic-ai-coding-suite-orchestrates-multiple-agents/)
- [The New Stack —— 陈志杰专访](https://thenewstack.io/tiktoks-ex-algorithm-chief-launches-verdent-ai-coding-tool/)
- [Tech Talks Daily —— Verdent 播客节目](https://techtalksnetwork.com/podcast/tech-talks-daily/episode/3517-how-verdent-ai-is-building-the-next-generation-ai-coding-agents)
- [Show HN 讨论，2025-09](https://news.ycombinator.com/item?id=45359339)
- [Visual Studio Marketplace 页面](https://marketplace.visualstudio.com/items?itemName=VerdentAI.verdent)
- [Product Hunt](https://www.producthunt.com/products/verdent-deck)
- [LinkedIn —— 公司](https://www.linkedin.com/company/verdent-ai)
- [LinkedIn —— Yuyu Zhang](https://www.linkedin.com/in/yuyu-zhang-a9833aa3/)
- [Tracxn 资料](https://tracxn.com/d/companies/verdent/__47DmRDHdslJwd9Z0wDAZxdniv0yKn8wRiZSAqY0TRNg)
- [ICSE 2026 —— SEAlign 论文条目](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/46/SEAlign-Alignment-Training-for-Software-Engineering-Agent) · [arXiv](https://arxiv.org/abs/2503.18455)
- 研究页面上的团队论文：[Seed-Coder](https://arxiv.org/abs/2506.03524)、[Seed1.5-Thinking](https://arxiv.org/abs/2504.13914)、[FullStack Bench](https://arxiv.org/abs/2412.00535)、[Multi-SWE-bench](https://arxiv.org/abs/2504.02605)

**中文媒体报道**

两篇原始文章，均发表于 2025 年 11 月，以及它们的转载和第三方试用：

- [新浪财经 —— 腾讯领投轮次独家报道，投资实习所，2025-11-17](https://finance.sina.com.cn/roll/2025-11-17/doc-infxstse6567772.shtml) —— 融资独家
- [新浪科技 —— 创始人专访，DeepTech 深科技，2025-11-24](https://finance.sina.com.cn/tech/roll/2025-11-24/doc-infypaav5690289.shtml) —— 创始人专访
- [搜狐（ZFinance）—— 融资独家转载，2025-11-17](https://www.sohu.com/a/955425497_122074763)
- [网易 —— 专访转载，2025-11](https://www.163.com/dy/article/KFADJCN1055692AH.html)
- [知乎 —— 专访转载](https://zhuanlan.zhihu.com/p/1976372371272267577)
- [知乎 —— 初识 Verdent AI，第三方试用，2025-11-23](https://zhuanlan.zhihu.com/p/1975338816031176069) · [CSDN 镜像](https://adg.csdn.net/695238375b9f5f31781b3548.html)
- [CSDN —— 试用 Verdent 的一些感受，第三方试用](https://blog.csdn.net/weixin_38754564/article/details/152013640)
- [AI 工具集 —— 工具目录条目](https://ai-bot.cn/verdent-ai/)
