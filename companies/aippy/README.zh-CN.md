# Aippy

[English](README.md) | **简体中文**

> 基于公开信息整理的研究笔记。最后更新：2026-07-29。同步至：2026-07-29。
> 每个数字都链接到出处并标注日期。在依赖这些信息前请对照一手来源核实。

## 摘要

Aippy 是一个以移动端为主的 AI 创作社区：用户用自然语言描述想法，平台生成可玩的小游戏或可交互网页作品，成品被发布进一条竖屏信息流，其他用户在其中滑动、试玩、评论并"Remix"二次创作（[aippy.ai](https://aippy.ai/)；访问于 2026-07-29）。Web 平台的首个版本 v0.1.0 发布于 [2025-04-18](https://docs.aippy.ai/changelog)，iOS 应用首次上架于 [2025-07-28](https://itunes.apple.com/lookup?id=6749073777)。应用的发布主体是新加坡实体 **NADA AI PTE. LTD.**；业务由港股上市公司 **赤子城科技（Newborn Town Inc.，09911）** 孵化，并于 2026 年年中从上市体系中分离。

- **融资：** 首轮机构融资"数千万美元"，投资方为歌未资本（Glowill Capital），投后估值 **2.5 亿美元**，由 36 氪于 2026-06-02 首发（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)）。赤子城已将 NADA AI 移出并表范围，但"仍持有相当比例"股权（[新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)）。
- **公司口径的规模：** 全球下载量 300 万以上、月活跃用户接近 200 万、UGC 作品 200 万件以上、DAU 互动率约 50%、美区 App Store 评分 4.8（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)）。2026-07-29 可独立观测到的数据：iOS 美区 20,849 条评分、均分 4.86（[iTunes API](https://itunes.apple.com/lookup?id=6749073777)），Google Play 显示"100 万以上下载"区间（[Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy)）。
- **团队约 30 人**，核心成员来自清华大学、美国西北大学、慕尼黑工业大学，覆盖算法、产品、运营（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)）；[LinkedIn 页面](https://www.linkedin.com/company/aippy/)显示 11–50 人区间、4 份档案，总部写作圣何塞。
- **唯一可核验的技术栈证据在 npm 上。** `@aippy/runtime` 的 peer 依赖为 React 19、Vercel AI SDK（`ai` ^6.0.0、`@ai-sdk/react` ^3.0.0），依赖 `@ai-sdk/openai-compatible`；`@aippy/vite-plugins` 基于 Babel 为 Vite 做组件标记（[npm](https://registry.npmjs.org/-/v1/search?text=aippy)）。同一个 runtime 此前以 **`@new-born-town/aippy-runtime`** 发布——这是 Aippy 与其原母公司之间唯一可机器核验的关联。
- **关于工程组织，几乎没有任何公开信息。** 没有招聘页、没有职位、没有工程博客、没有具名工程师、没有安全页面。文档站最后一次内容提交是 [2025-06-27](https://github.com/AIPPY/Aippy-Docs)，官方公布的两个 Discord 邀请链接均已失效。一个[自称官方的 GitHub 账号](https://github.com/AippyAI/Aippy)在仓库描述里带有 pump.fun 风格的代币地址——见`备注`。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | Aippy；站点页脚署名 "NADA AI" | 浏览器渲染 [aippy.ai](https://aippy.ai/)，访问于 2026-07-29 |
| 应用发布主体 | NADA AI PTE. LTD.（`PTE. LTD.` 为新加坡私人有限公司形式） | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)、[Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |
| 原母公司 | 赤子城科技（Newborn Town Inc.），港交所 09911；孵化 Aippy，并于 2026 年将 NADA AI 移出并表 | [新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |
| 成立时间 | 2025 年 | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)、[LinkedIn](https://www.linkedin.com/company/aippy/) |
| Web 平台上线 | v0.1.0 于 2025-04-18；中文报道把产品上线时间记为 2025 年 4 月 | [更新日志](https://docs.aippy.ai/changelog)、[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| iOS 上线 | 2025-07-28；当前版本 1.17.0 发布于 2026-07-24 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| 总部 | LinkedIn 写美国圣何塞；Aippy 任何自有页面都未公布地址 | [LinkedIn](https://www.linkedin.com/company/aippy/) |
| 创始人兼 CEO | Evan（叶椿建），赤子城联合创始人、长期担任 CTO | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| 员工人数 | 约 30 人（2026 年 6 月公司口径）；LinkedIn 区间 11–50，平台上有 4 份档案 | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)、[LinkedIn](https://www.linkedin.com/company/aippy/) |
| 用户数 | 300 万以上下载、月活接近 200 万、作品 200 万件以上（2026 年 6 月公司口径） | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| 累计融资 | 一轮，"数千万美元"；各来源给出的是区间表述而非具体数字 | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| 估值 | 投后 2.5 亿美元，报道折合约 20 亿港元 | [新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |
| 投资方 | 歌未资本（Glowill Capital） | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| 工程团队工作语言 | 任何来源都未说明。产品、文档与应用商店页面全部仅有英文（`languageCodesISO2A` = `["EN"]`）；而公司的报道与原母公司均为中文语境 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)、[文档](https://docs.aippy.ai/welcome) |
| 联系方式 | `aippy.ai` 域下的 hi@、support@、legal@、bd@、developer@、feedback@；隐私政策中另有 careers@aippy.ai | [服务条款](https://aippy.ai/terms.html)、[隐私政策](https://aippy.ai/privacy.html) |
| 社交账号 | X [@aippyai](https://x.com/aippyai)、[LinkedIn](https://www.linkedin.com/company/aippy/)；站点和文档公布的 Discord 邀请链接均已失效 | [文档](https://docs.aippy.ai/welcome)、Discord 邀请 API，访问于 2026-07-29 |

### 品牌与法律实体

| 名称 | 类型 | 关系 | 来源 |
|---|---|---|---|
| Aippy | 公开品牌与产品 | 面向消费者的名称；据其自有条款，持有 `aippy.ai` 域名与商号 | [服务条款](https://aippy.ai/terms.html) |
| NADA AI PTE. LTD. | 运营主体（新加坡） | iOS 与 Android 应用的发布方；名称出现在网站页脚以及 `com.nadaai.aippy` 包名中 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)、[Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |
| 赤子城科技（Newborn Town Inc.） | 原母公司，港交所 09911 | 孵化 Aippy；2026 年重组后 NADA AI 不再并表，但赤子城仍持有"相当比例"股权，并继续提供本地化运营、全球流量协同与技术支持 | [新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |
| `@new-born-town` npm 命名空间 | 曾用发布身份 | Aippy 的 runtime SDK 最早以 `@new-born-town/aippy-runtime` 发布（2025-10-09 至 2025-10-13），之后迁至 `@aippy/runtime`，维护者为同样两人 | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| GitHub 上的 `AippyAI` | 未经核实的第三方账号 | 自称 "AippyAi official"，但 Aippy 任何自有页面都未链接到它；其仓库描述结尾是一串以 pump.fun 后缀 `pump` 结尾的 base58 字符串——见`备注` | [GitHub](https://github.com/AippyAI/Aippy) |

未取得 NADA AI PTE. LTD. 的任何工商登记记录，见`备注`。

---

## 产品

### 创作与信息流闭环

渲染后的站点是一条按分类组织的社区作品流，每件作品带播放、点赞和评论计数，顶部是一个提示词输入框，文案为"Type your idea and start building..."（[aippy.ai](https://aippy.ai/)；于 2026-07-29 渲染读取）。分类由一个公开接口下发，共七个：**Hot、Latest、Mindless、Brain Hack、Unhinged、Dopamine、Send This**（[分类接口](https://api.aippy.ai/api/template/category_v2)）。中文报道把这种形态描述为"互动 Feed 流"，用户像刷短视频一样浏览，并可用自然语言对已有作品 Remix（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)）。

App Store 页面把产出分成四类——"GAMES & SIMULATORS"、"TOOLS & GENERATORS"、"INTERACTIVE ART"、"AI EXPERIMENTS"——并称 Remix"始终会标注原作者"（[App Store 描述](https://itunes.apple.com/lookup?id=6749073777)、[FAQ](https://docs.aippy.ai/faq)）。

### 各端应用

| 端 | 名称 | 详情 | 来源 |
|---|---|---|---|
| Web | Aippy | React + Vite 单页应用，带 PWA manifest 与 Service Worker；源站为阿里云 OSS，前置 Cloudflare | [页面源码](https://aippy.ai/)、响应头，访问于 2026-07-29 |
| iOS | Aippy: Game Maker | 包名 `com.nadaai.aippy`，分类 Entertainment / Graphics & Design，12+ 分级，仅英文，最低 iOS 15.0，52.4 MB | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| Android | Aippy: AI Game Maker | 同一包名，100 万以上下载区间，更新于 2026-07-29 | [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |

### 文档记载的能力

[文档](https://docs.aippy.ai/welcome)描述了从文本提示生成 UI、带检查点版本历史的实时预览、画布内可视化编辑（[Instant Edit](https://docs.aippy.ai/features/instand-edit)，随 v0.5.0 于 2025-06-10 上线）以及一键发布，并声称支持全栈生成、数据库与 API 连接、自定义域名、支付和身份认证。而同一站点的[路线图](https://docs.aippy.ai/roadmap)把上述这些——后端与数据库、可视化编辑器、自定义域名、支付处理、第三方集成——统统列为"Coming Soon"。两页自相矛盾，见`备注`。

### 商业模式

五档订阅，各来源给出的价格一致，但配额随页面不同而不同。当前口径以线上[定价页](https://aippy.ai/pricing)（2026-07-29 渲染）为准：

| 套餐 | 价格 | 每月积分 | 生成请求数 | 素材存储 |
|---|---|---|---|---|
| Starter | $0 | 500（每日登录得 100，每月上限 500） | — | 500 MB |
| Explorer | $19 | 2,000 | 80 | 2 GB |
| Builder | $49 | 5,000 | 200 | 10 GB |
| Master | $99 | 10,000 | 400 | 20 GB |
| Team | $199 | 20,000 | 800 | 50 GB |

[更新日志](https://docs.aippy.ai/changelog)给出了换算关系："25 积分 = 一次提示 = 一次成功的生成请求"，随积分体系在 v0.5.1（2025-06-25）引入，同时上线的还有每成功注册一人赠 50 积分的邀请机制。支付由第三方处理——条款中点名 Stripe 与 PayPal，隐私政策中点名 Stripe（[条款](https://aippy.ai/terms.html)、[隐私政策](https://aippy.ai/privacy.html)）。条款还写明未用完的额度不结转，且除重复扣费、系统计费错误或连续超过 72 小时的服务中断外不予退款。

### 各时期披露的规模

| 日期 | 披露数字 | 来源 |
|---|---|---|
| 2025-04-18 | Web 平台 v0.1.0，首次发布 | [更新日志](https://docs.aippy.ai/changelog) |
| 2025-06-25 | v0.5.1，最后一条带日期的发布记录 | [更新日志](https://docs.aippy.ai/changelog) |
| 2025-07-28 | iOS 应用首次上架 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| 2026-01 | 赤子城称 Aippy 在苹果与安卓商店评分均达 4.9 | [新浪财经，2026-01-21](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml) |
| 2026-06-02 | 300 万以上下载、月活接近 200 万、作品 200 万件以上、DAU 互动率约 50%、美区 App Store 4.8 分、日新增创作较年初增长 10 倍、日均使用时长提升 25%、自然流量占比超 30% | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| 访问于 2026-07-29 | iOS：美区 20,849 条评分、均分 4.86；版本 1.17.0 发布于 2026-07-24 | [iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| 访问于 2026-07-29 | Google Play：100 万以上下载区间；更新于 2026-07-29 | [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) |
| 访问于 2026-07-29 | 信息流首位作品 "Guess The Logo!" 显示 45.4 万播放、4 千点赞、5.6 千评论 | [aippy.ai](https://aippy.ai/)，浏览器渲染 |

### 已公布的客户与合作方

截至 2026-07-29，在所查阅的来源中，Aippy 与赤子城均未公布任何客户、合作方、分发协议、模型供应商或基础设施供应商。唯一具名的商业关系是法律页面中的支付处理商和唯一披露的投资方。

### 公司自述的规划

本轮资金用途被表述为"顶尖人才引进和欧美核心市场用户规模化增长"（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)）。[路线图](https://docs.aippy.ai/roadmap)把全栈生成、可视化编辑器、自定义域名、支付与第三方集成列为后续方向，均未附日期。赤子城被表述的持续角色是本地化运营、全球流量协同与技术支持（[新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)）。

---

## 创始人

| 姓名 | 职位 | 来源陈述的履历事实 | 来源 |
|---|---|---|---|
| Evan（叶椿建） | Aippy 创始人兼 CEO | 赤子城科技联合创始人，长期担任其 CTO；被描述为在海外社交与游戏领域深耕十余年 | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |

所查阅的来源中没有第二位具名人士。网站、应用、文档、LinkedIn 页面与任何报道都未点名联合创始人、高管或工程负责人，Aippy 任何页面上也没有团队或"关于我们"页。npm 包由两个账号 `sin_bufan` 和 `kkunique` 发布，其真实身份未被说明（[npm](https://registry.npmjs.org/-/v1/search?text=aippy)）。

### 主要管理层

| 姓名 | 职位 | 来源 |
|---|---|---|
| — | 除创始人外，没有任何管理层被公开识别 | 检索于 2026-07-29，见`备注` |

---

## 融资

| 日期 | 轮次 | 金额 | 投资方 | 累计 | 来源 |
|---|---|---|---|---|---|
| 2026-06-02 报道 | 首轮（轮次未命名） | "数千万美元"，各来源给出的是区间表述而非具体数字 | 歌未资本（Glowill Capital） | 同上；未披露此前任何轮次 | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)、[新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) |

没有任何来源给这一轮标注字母轮次名。投后估值被表述为 2.5 亿美元、折合约 20 亿港元，并被描述为赤子城 AI 业务首次独立获得市场估值（[新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)、[新浪财经，2026-01-21](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml)）。

这一轮还伴随两项结构性事实。NADA AI 已被移出上市公司并表范围，赤子城保留 NADA AI"相当比例"的股权——所有来源都未给出具体比例。Aippy 与赤子城均未自行发布公告；报道源头是 36 氪的一篇首发，随后被新浪、投资界、东方财富、证券时报等转载。多家媒体刊出同一组数字属于同一个来源，不构成相互印证。

---

## 工程

### 技术栈与平台

由公开资产确认——`aippy.ai` 的页面源码与响应头、已发布的 JavaScript 包、npm 仓库以及文档仓库（均访问于 2026-07-29）：

| 项目 | 内容 | 证据 |
|---|---|---|
| Web 客户端 | React + Vite 单页应用，代码拆分为 `index`、`react-vendor`、`ui-vendor` 三块；通过 `vite-plugin-pwa` 提供 PWA 并注册 Service Worker | [页面源码](https://aippy.ai/) |
| UI 库 | 包中同时存在 Ant Design 与 MUI；使用 `i18next` 与 `react-i18next` 做多语言，目前仅提供英文 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 图形 | `three.js`，配合 `@react-three/fiber`，Draco 解码器从 `gstatic.com` 加载 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 生成产物的运行时 | `@aippy/runtime`——peer 依赖 React 19.1.1+、TypeScript 5+、`ai` ^6.0.0 与 `@ai-sdk/react` ^3.0.0（Vercel AI SDK）；依赖 `@ai-sdk/openai-compatible`。共 48 个版本，创建于 2025-10-14，最新 0.4.1 发布于 2026-06-23 | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| 生成产物的构建 | `@aippy/vite-plugins`——"素材管理与组件标记"，基于 `@babel/parser`、`@babel/traverse`、`esbuild`、`estree-walker`、`magic-string`。创建于 2025-10-29，最新 0.2.8 发布于 2026-04-21 | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| 曾用包命名空间 | `@new-born-town/aippy-runtime`，描述相同、维护者相同，发布于 2025-10-09 至 2025-10-13，之后由 `@aippy` 命名空间接替 | [npm](https://registry.npmjs.org/-/v1/search?text=aippy) |
| 托管与边缘 | 源站为阿里云 OSS，前置 Cloudflare；不带浏览器 User-Agent 的请求会拿到 OSS 的 `AccessDenied` XML | [aippy.ai](https://aippy.ai/) 响应头 |
| 后端 API | `api.aippy.ai`，JSON 接口，采用 `{code, msg, data}` 信封；多数端点需要鉴权，未登录返回 `code: 4011` | [分类接口](https://api.aippy.ai/api/template/category_v2) |
| 产品分析 | ThinkingData（数数科技）SDK，在 Web 包中初始化，上报地址为 `https://report.lolipopmobi.com`，开启 page-show / page-hide 自动埋点 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 归因与分析 | AppsFlyer OneLink（`aippy.onelink.me`）、Adjust、Amplitude、Google Analytics（`G-LD0Z19ZH4P`）、Cloudflare Web Analytics beacon | [页面源码](https://aippy.ai/)、[JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 支付 | JS 包中点名 Stripe；条款中点名 Stripe 与 PayPal | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js)、[条款](https://aippy.ai/terms.html) |
| 登录 | 支持 Google、Apple、GitHub 第三方登录 | [条款](https://aippy.ai/terms.html)、[隐私政策](https://aippy.ai/privacy.html) |
| 文档 | Mintlify；源码在公开仓库 [AIPPY/Aippy-Docs](https://github.com/AIPPY/Aippy-Docs) 中，其 `llms.txt` 仍保留模板标题 "Mint Starter Kit" | [llms.txt](https://docs.aippy.ai/llms.txt)、[仓库](https://github.com/AIPPY/Aippy-Docs) |

以下说法无法与任何公司自有页面相互印证，因此只作为线索记录，不作为技术栈事实：

| 说法 | 出处 | 状态 |
|---|---|---|
| Aippy 底层搭载赤子城自研"Boomix"多模态大模型和轻量化渲染引擎 | 一个中文内容聚合站，相同措辞在多个同类站点重复出现 | 未确认。赤子城自己首次披露该模型是在其 2024 年度业绩报道中，拼写为 **Boomiix**，描述其支撑 SoloAware 引擎在 SUGO 等产品中的社交匹配与内容推荐，并未提及 Aippy（[智通财经 经新浪财经，2025-03-04](https://finance.sina.com.cn/stock/hkstock/ggscyd/2025-03-04/doc-inenpfhz9590632.shtml)） |
| "Aippy 是由 Claude 大模型驱动的 AI Vibe Coding 平台……基于 React 框架，灵活集成 three.js 或 pixi.js" | [github.com/AippyAI/Aippy](https://github.com/AippyAI/Aippy) | 不可用。该账号未经核实，Aippy 任何自有页面都未链接到它，且其仓库描述结尾带有 pump.fun 风格的代币地址——见`备注` |

Aippy 自有的任何页面都未点名模型供应商、推理服务商、云区域、数据库，也未说明执行用户生成代码所用的沙箱机制。

### 系统

| 系统 | 作用 | 来源 |
|---|---|---|
| 提示词到项目的生成 | 把自然语言描述变成可运行的交互项目；定价页把这一步计为一次"生成请求"，每次 25 积分 | [aippy.ai](https://aippy.ai/)、[更新日志](https://docs.aippy.ai/changelog) |
| 提示词增强 | 生成链路前有一个独立的 `/api/llmodel/prompt/enhance` 端点 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 实时预览与检查点 | 项目随修改实时渲染，自动生成检查点并支持回滚 | [welcome](https://docs.aippy.ai/welcome)、[路线图](https://docs.aippy.ai/roadmap) |
| Instant Edit | 无需提示词，直接通过 Tailwind 控件修改选中 DOM 元素的文字、尺寸与样式 | [Instant Edit](https://docs.aippy.ai/features/instand-edit) |
| 发布与分享 | 项目发布、分享、Remix 端点；分享链接位于 `share.aippy.ai/p/` 与 `/u/` 下 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 社交关系与信息流 | 关注/取关、粉丝与关注列表、带回复的评论、点赞、收藏、举报、推荐、创作者榜单，以及带未读计数的消息箱 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js) |
| 内容审核 | 条款保留不经通知下架违规内容的权利，并专门设有内容审核与用户安全一节；但未描述任何机制、模型或处理时效 | [条款](https://aippy.ai/terms.html) |
| 素材流水线 | 媒体上传、列表、批量删除与用户维度存储统计，按套餐限额（500 MB 至 50 GB）；素材由 `cdn.aippy.ai` 提供，带阿里云 OSS 图片处理（`oss-process`）参数 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js)、[定价页](https://aippy.ai/pricing) |
| 计费 | 订阅套餐、订单创建、积分流水、每日签到（`attendance`）积分与邀请返利体系 | [JS 包](https://aippy.ai/assets/js/index-BJ8REtwf.js)、[更新日志](https://docs.aippy.ai/changelog) |
| AI Cloud 代码存储 | 条款中点名；账号删除后代码仍保留 90 天 | [条款](https://aippy.ai/terms.html) |

### 招聘所需技术背景

没有任何公开信息。`aippy.ai` 上没有招聘页——所有路径都返回同一个单页外壳——所检索的招聘平台上也没有任何职位，任何地方都没有关于岗位、职级、面试流程或期望背景的描述。找到的唯一招聘渠道是[隐私政策](https://aippy.ai/privacy.html)中的 `careers@aippy.ai`。与招聘有关的唯一表述是本轮资金用于"顶尖人才引进"（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)），与现有团队有关的唯一表述是这约 30 人来自清华大学、美国西北大学、慕尼黑工业大学，覆盖算法、产品与运营。

### 行业领域

- **消费级 UGC 平台与创作者社区。** 产品机制——信息流、关注关系、点赞、评论、Remix 署名、创作者榜单、每日签到奖励——都是社交产品机制，而创始人被陈述的背景正是十年的海外社交与游戏产品（[36氪首发，2026-06-02](https://36kr.com/p/3834400181741440)）。
- **出海增长运营。** 赤子城的持续贡献被表述为本地化运营与全球流量协同；本轮资金指向欧美用户增长（[新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)）。
- **执行不可信的用户生成代码。** 平台把模型根据匿名提示词写出的代码，运行在其他用户的浏览器里。任何公开材料都未描述沙箱、隔离或审查机制。
- **消费者数据与未成年人。** 隐私政策覆盖设备标识符（IDFA、IDFV、GAID）、跨境传输以及 GDPR/CCPA 权利，并声明服务不面向 18 岁以下人群——而 App Store 的分级是 12+（[隐私政策](https://aippy.ai/privacy.html)、[iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)）。

### 工作条件

几乎没有任何披露。下表记录的是实际存在的信息，而不是在没有公开政策的地方替它写一个。

| 项目 | 内容 | 来源 |
|---|---|---|
| 在招岗位 | 未公开。`aippy.ai/careers`、`/jobs`、`/about` 均返回通用单页外壳，所检索的招聘平台上也未找到任何职位 | 探测于 2026-07-29 |
| 投递渠道 | `careers@aippy.ai`，仅出现在隐私政策中 | [隐私政策](https://aippy.ai/privacy.html) |
| 地点 | LinkedIn 写圣何塞；运营主体是新加坡公司；原母公司与相关报道以北京和香港为中心。没有任何来源说明工程师实际在哪里办公 | [LinkedIn](https://www.linkedin.com/company/aippy/)、[iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) |
| 团队规模与构成 | 约 30 人，覆盖算法、产品、运营 | [36氪首发，2026-06-02](https://36kr.com/p/3834400181741440) |
| 远程政策、签证、福利、薪资、股权、流失率、面试流程 | 所查阅的来源中均未公开 | 检索于 2026-07-29 |

---

## 备注

### 未公开披露

以下结论的检索范围（2026-07-29）：分别以浏览器和非浏览器 User-Agent 抓取 `aippy.ai`，用浏览器渲染，并探测 `/pricing`、`/careers`、`/jobs`、`/about`、`/blog`、`/changelog`、`/community`、`/explore`、`/discover`；`robots.txt`；`status`、`blog`、`careers`、`jobs`、`api`、`docs`、`share`、`cdn`、`app`、`dev` 子域名；完整的已发布 JavaScript 包；`api.aippy.ai` 的公开端点；`docs.aippy.ai` 及其 `llms.txt`、welcome、FAQ、roadmap、changelog 和 pricing 页；`AIPPY/Aippy-Docs` 仓库及其提交历史；`aippy` 与 `nadaai` 的 GitHub 组织命名空间以及 GitHub 仓库搜索；npm 上的 `aippy` 检索；App Store 与 Google Play 页面及 iTunes lookup API；服务条款与隐私政策；两个公开 Discord 邀请码的 Discord 接口；LinkedIn 公司页；赤子城官网；以及围绕 Aippy、NADA AI、赤子城 + Aippy、Boomix/Boomiix 与 Aippy 招聘的中英文检索。

- **没有任何工程博客、技术文章、演讲或架构材料**，中英文皆无。
- **任何公司自有页面都未点名模型供应商、云服务商、数据库或沙箱机制。** 对于一个全部价值都建立在"模型生成可执行代码"之上的产品，其推理链路完全未披露。
- **没有招聘页，也没有任何职位。** 唯一的招聘信号是隐私政策里的一个邮箱地址。
- **除创始人外没有任何具名员工。** 任何地方都没有出现联合创始人、高管或工程负责人；npm 维护者用的是化名账号。
- **没有安全页面、信任中心、子处理方清单或认证。** 隐私政策只列出接收方的类别（"支付处理商"、"云服务提供商（如 AWS、Google Cloud）"）而非实际子处理方，而可观测到的源站是阿里云 OSS，并不在其列。
- **未取得任何工商登记记录。** NADA AI PTE. LTD. 未经 ACRA 核实；新加坡属地是根据 `PTE. LTD.` 后缀以及 App Store 与 Google Play 的发布方字段推断的。
- **赤子城保留的股权比例未公开**，轮次字母名、交割日期、分期结构与董事会构成也均未说明。
- **Aippy 与赤子城都没有就本轮融资发布自己的公告。** 所有内容都可追溯到 2026-06-02 的那一篇 36 氪首发。
- **未找到任何英文报道。** 检索到的报道全部是中文。
- **服务条款的管辖法条款是一个未填写的模板占位符。** [条款](https://aippy.ai/terms.html)（最后更新 2026-06-16）第 16 节写着"governed by the laws of [Jurisdiction, e.g., the State of California, USA]"，争议解决地写着"[Jurisdiction, e.g., San Francisco County, California]"。实际管辖地并未指明。
- **两个公开的 Discord 邀请链接都是失效的。** 文档中的邀请码 `G94ZAx6gVq` 返回"Invite is expired"，JS 包中的 `discord.com/invite/aippy` 返回"Unknown Invite"（Discord 邀请 API，2026-07-29）——尽管公司对外称有 1.5 万人的 Discord 核心社区。
- **文档已经陈旧。** [AIPPY/Aippy-Docs](https://github.com/AIPPY/Aippy-Docs) 的最后一次内容提交是 2025-06-27，更新日志最后一条是 2025-06-25 的 v0.5.1——距本页日期约十三个月，且早于 iOS 上线。

### 不同来源之间的不一致

- **免费额度有三个版本：** 线上[定价页](https://aippy.ai/pricing)写每月 500 积分（每日登录得 100）；文档[定价页](https://docs.aippy.ai/user-guides/pricing)写每月 30 次请求；[条款](https://aippy.ai/terms.html) 7.1 写每天 4 条、每月 20 条消息。付费档同样分叉——文档给出 100/260/550/1,200 次请求，线上页给出 80/200/400/800。
- **能力与路线图在同一个文档站内互相矛盾：** [welcome](https://docs.aippy.ai/welcome) 把后端逻辑、数据库集成、自定义域名、支付和第三方集成列为现有能力，[FAQ](https://docs.aippy.ai/faq) 称"Aippy 生成全栈应用"，而[路线图](https://docs.aippy.ai/roadmap)把这些统统列为"Coming Soon"。
- **产品到底是什么：** 文档描述的是一个通用的 Web 应用与工具生成器；中文报道和两个应用商店页描述的是 AI 游戏创作社区。首页的 meta 描述横跨两者。
- **商店评分：** 赤子城 2026 年 1 月的说法是两大商店均为 4.9（[新浪财经，2026-01-21](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml)）；2026 年 6 月的报道写美区 App Store 4.8；[iTunes API](https://itunes.apple.com/lookup?id=6749073777) 在 2026-07-29 返回的是美区 20,849 条评分、均分 4.86。
- **下载量：** 公司口径是全球 300 万以上（2026 年 6 月）；[Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy) 在 2026-07-29 显示安卓端处于 100 万以上区间。两者衡量的不是同一件事——跨平台累计对安卓单端区间——且都无法审计。
- **上线时间：** [更新日志](https://docs.aippy.ai/changelog)把 Web 平台首个版本记在 2025-04-18，[iTunes API](https://itunes.apple.com/lookup?id=6749073777) 把 iOS 上架记在 2025-07-28，而报道只写"2025 年 4 月上线"。公司成立时间也只写"2025 年"，未精确到月。
- **模型名称：** 与 Aippy 相关的内容页写"Boomix"；原母公司首次披露时写"Boomiix"（[智通财经 经新浪财经，2025-03-04](https://finance.sina.com.cn/stock/hkstock/ggscyd/2025-03-04/doc-inenpfhz9590632.shtml)）。两家公司都没有发布过模型页面。
- **年龄政策：** [隐私政策](https://aippy.ai/privacy.html)声明服务不面向 18 岁以下人群；App Store 的分级是 12+（[iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777)）。
- **公司到底在哪：** [LinkedIn](https://www.linkedin.com/company/aippy/) 写圣何塞；应用发布方是新加坡实体；孵化方、创始人与全部报道都在中文语境。没有任何来源把三者统一起来。

### 其他

- **一个自称 Aippy 的 GitHub 账号带有代币地址。** [github.com/AippyAI](https://github.com/AippyAI) 名称为 "AippyAi official"，填写了 `aippy.ai` 与 `@aippyai`，创建于 2025-12-12，仅 1 名关注者。其唯一仓库的描述写着"Aippy is an AI Vibe Coding platform powered by the Claude large model……flexibly integrates with three.js or pixi.js"，其后紧跟 `98dNFeSKWwRLfAmchCP1ASwQaa1UhTJ3zynyEhvHpump`——一串以 pump.fun 为新铸代币追加的 `pump` 为后缀的 base58 字符串。其简介另写着"Previously called MDCG"。Aippy 任何页面都未链接到该账号，而真正作为 `docs.aippy.ai` 源码的另一个账号 [AIPPY](https://github.com/AIPPY/Aippy-Docs)（创建于 2025-04-02）与之无关。"由 Claude 驱动"的说法源自此处，不应被当作公司的陈述。
- **npm 命名空间的迁移是这次剥离最干净的证据。** 同一个 runtime SDK、同样的描述、同样两位维护者，从 `@new-born-town/aippy-runtime`（2025 年 10 月）迁到 `@aippy/runtime`——这是公司分拆在技术侧留下的痕迹。
- **Web 埋点上报到一个第三方域名。** ThinkingData SDK 上报至 `report.lolipopmobi.com`；而 `lolipopmobi.com` 本身提供的是一个与之无关的老旧 "Face App" 站点，页脚写着 "Copyright © 2017-2020 Lbsbanana.ltd"（[lolipopmobi.com](https://lolipopmobi.com/)，访问于 2026-07-29）。该运营方与 Aippy 的关系在任何地方都没有说明。
- **站点对非浏览器客户端不可读。** 不带浏览器 User-Agent 的请求收到的是阿里云 OSS 的 `AccessDenied` XML 而不是页面，因此产品页面对朴素爬虫、以及引用这些内容的搜索结果是不可见的。
- **公司自有条款为自己保留了对已发布内容的宽泛许可**，免费、无需署名，同时声明用户保留所有权；条款还保留用提示词和代码训练模型的权利，仅对 Enterprise Plan 订阅者豁免——而这一套餐只出现在条款里，任何定价页上都没有（[条款](https://aippy.ai/terms.html)）。
- **内容分类对目标调性的表达异常直白**——"Mindless"、"Brain Hack"、"Unhinged"、"Dopamine"、"Send This"（[分类接口](https://api.aippy.ai/api/template/category_v2)）——与报道中"信息流优先、短时长"的定位一致，而非文档中的开发者工具定位。
- **这一估值对原母公司是有量级意义的。** 2.5 亿美元被描述为约 20 亿港元，有报道称接近赤子城当时市值的六分之一（[新浪科技 / 投资界，2026-06-02](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml)）。

---

## 资料来源

**官方**

- [Aippy —— aippy.ai](https://aippy.ai/) · [定价](https://aippy.ai/pricing)
- [服务条款 —— 最后更新 2026-06-16](https://aippy.ai/terms.html) · [隐私政策 —— 最后更新 2026-01-10](https://aippy.ai/privacy.html)
- [Web 应用 JS 包 —— 已发布的前端代码](https://aippy.ai/assets/js/index-BJ8REtwf.js)
- [公开分类接口](https://api.aippy.ai/api/template/category_v2)
- 文档：[welcome](https://docs.aippy.ai/welcome) · [FAQ](https://docs.aippy.ai/faq) · [路线图](https://docs.aippy.ai/roadmap) · [更新日志](https://docs.aippy.ai/changelog) · [定价](https://docs.aippy.ai/user-guides/pricing) · [Instant Edit](https://docs.aippy.ai/features/instand-edit) · [页面索引](https://docs.aippy.ai/llms.txt)
- [文档源码 —— AIPPY/Aippy-Docs](https://github.com/AIPPY/Aippy-Docs)
- [aippy 与 new-born-town 命名空间下发布的 npm 包](https://registry.npmjs.org/-/v1/search?text=aippy)
- [App Store 元数据 —— iTunes lookup API](https://itunes.apple.com/lookup?id=6749073777) · [Google Play](https://play.google.com/store/apps/details?id=com.nadaai.aippy)
- [LinkedIn](https://www.linkedin.com/company/aippy/) · [X —— @aippyai](https://x.com/aippyai)
- [赤子城科技 —— 原母公司](https://www.newborntown.com/)

**新闻稿**

- Aippy 与赤子城均未就 2026 年这轮融资发布新闻稿；下列均为媒体报道。

**第三方报道与资料页**

- [36氪首发 —— 首轮融资数千万美元、估值2.5亿美元，「Aippy」正在打造下一代AI游戏社区，2026-06-02（中文）](https://36kr.com/p/3834400181741440)
- [新浪科技 / 投资界 —— 独家丨Aippy从赤子城剥离，估值2.5亿美元，2026-06-02（中文）](https://finance.sina.com.cn/tech/roll/2026-06-02/doc-inhzysxu3300565.shtml) · [投资界版本](https://news.pedaily.cn/202606/564739.shtml)
- [新浪财经 —— 赤子城科技2025年营收67.6–70.0亿元，创新业务爆发式增长，2026-01-21（中文）](https://finance.sina.com.cn/stock/hkstock/ggscyd/2026-01-21/doc-inhiaktw3520185.shtml)
- [智通财经 经新浪财经 —— 赤子城科技首次披露Boomiix模型，2025-03-04（中文）](https://finance.sina.com.cn/stock/hkstock/ggscyd/2025-03-04/doc-inenpfhz9590632.shtml)
- [维基百科 —— NewBornTown](https://en.wikipedia.org/wiki/NewBornTown)

**列出以避免误认**

- [github.com/AippyAI/Aippy —— 未经核实的账号，其仓库描述带有 pump.fun 风格的代币地址](https://github.com/AippyAI/Aippy)
- [lolipopmobi.com —— Aippy 埋点上报域名背后是一个无关的老旧应用站点](https://lolipopmobi.com/)
