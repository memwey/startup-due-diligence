# OJO

[English](README.md) | **简体中文**

> 依据公开资料整理。最后更新：2026-08-26。
> 本文与英文版同步至：2026-08-26。英文版为原始版本。
> 每项数据均标注来源与日期。使用前请自行核验原始资料。

## TL;DR

OJO 是 `ojo.art` 上的一款邀请制 AI 设计产品，在同一张画布上生成产品策略、UI 设计、落地页和可运行的交互原型。其服务条款将运营主体列为 "Touchine AI (HK) Limited, a company incorporated in Hong Kong SAR"（[服务条款](https://ojo.art/terms)；更新与生效日期均为 2026-03-16）。

- 产品于 2026-08-18 在 X 上公开发布："Today, we're introducing OJO: The first Design Agent Team Workspace."（[@OJOaidesign，2026-08-18](https://x.com/OJOaidesign/status/2089731834095489430)）。首页目前仍写着 "OJO is in private beta. Join the waitlist and we will enable access for you as soon as we can."（[ojo.art](https://ojo.art/)；访问于 2026-08-26）。
- 公司自身的各类物料中出现了四个名字 —— **OJO**（品牌）、**Touchine**（法律主体与 npm scope）、**iRise**（静态资源路径与 GitHub 组织）、**Nexight**（VS Code 插件市场发布者），详见 `名称与主体`。
- 价格已公开且处于生效状态：Free（$0）、Plus（$27/月 或 $300/年）、Pro（$62/月 或 $684/年），另有四档积分包，通过 Stripe 与 Antom 收款（[/api/commerce/v1/billing/plans](https://ojo.art/subscribe)；读取于 2026-08-26），详见 `商业化`。
- 在下文所述检索范围内，未发现公开的创始人、团队成员、人数、融资或用户规模信息，详见 `备注`。

---

## Basic

| 项目 | 内容 | 来源 |
|---|---|---|
| 公开品牌 | OJO（页面标题 "OJO \| AI Design Agent for UI, Landing Pages, and Product Prototypes"） | [ojo.art](https://ojo.art/)；访问于 2026-08-26 |
| 自我描述 | "OJO is an AI Design Agent Team Workspace that turns ideas into research-backed UI designs, landing pages, and product prototypes. Join the private beta." | `og:description` meta 标签，[ojo.art](https://ojo.art/)；访问于 2026-08-26 |
| 运营主体 | "Touchine AI (HK) Limited, a company incorporated in Hong Kong SAR（'Touchine,' 'we,' 'us,' or 'our'）" | [服务条款](https://ojo.art/terms) 前言；更新／生效于 2026-03-16 |
| 公司注册信息 | 商业登记号 "80290592"；成立日期 "2026年04月28日"；类型 "私人股份有限公司"；状态 "仍註冊" | [tempb.com 公司名录](https://www.tempb.com/companies/touchine-ai-hk-limited/)，第三方聚合站；页面日期 2026-07-18 |
| 注册地址 | "Suite 6503, 65/F, Central Plaza, 18 Harbour Road, Wan Chai, Hong Kong" | [服务条款](https://ojo.art/terms) §14.4、[隐私政策](https://ojo.art/privacy-policy) §10 |
| 适用法律 | "the laws of the Hong Kong Special Administrative Region"；"exclusive jurisdiction of the courts of Hong Kong" | [服务条款](https://ojo.art/terms) §13 |
| 文档日期 | 服务条款与隐私政策均为 "Updated: Mar. 16, 2026 / Effective: Mar. 16, 2026"；帮助中心为 "Last updated: Mar 28, 2026" | [服务条款](https://ojo.art/terms)、[隐私政策](https://ojo.art/privacy-policy)、[帮助中心](https://ojo.art/help-center) |
| 年龄政策 | "Confirm you are at least 18 years of age"；"The Services are not intended for individuals under 18 years of age" | [服务条款](https://ojo.art/terms) §1、[隐私政策](https://ojo.art/privacy-policy) §8 |
| 公开联系方式 | `official@ojo.art`（法务、隐私权利、数据保护联系人、训练退出）；`support@ojo.art`（支持、DMCA 代理人） | [服务条款](https://ojo.art/terms) §14.4、[隐私政策](https://ojo.art/privacy-policy) §10 |
| 准入方式 | 邀请制："OJO is currently in an invite-only beta phase. Please visit ojo.art to submit an invitation code and request access." | [帮助中心](https://ojo.art/help-center) §2.1；访问于 2026-08-26 |
| 域名 | `ojo.art` 注册于 2026-03-03（注册商 Spaceship, Inc.；注册人由 "Privacy service provided by WITHHELD FOR PRIVACY LLC" 隐匿，州为美国 Delaware）。`touchine.ai` 注册于 2026-04-13（Cloudflare 注册商，注册人国别 CN），跳转至 `ojo.art`。`touchine.com` 注册于 2026-03-25（阿里云／万网，注册人所在地 "bei jing"，CN）。`ws.ojo.dev` 通过 CNAME 解析到 AWS `us-east-1` 负载均衡器。 | WHOIS 与 DNS 查询于 2026-08-26 |
| 站点语言 | 六种：`en`、`zh-CN`、`zh-HK`、`ja`、`es`、`ko`，以 `hreflang` 声明 | [ojo.art](https://ojo.art/) 页面头部；访问于 2026-08-26 |
| 公开路由 | `/`、五个语言根路径、`/help-center`、`/terms`、`/privacy-policy`，以及各语言的博客 sitemap；`/subscribe` 与 `/dashboard` 属应用路由，未列入 sitemap | [sitemap.xml](https://ojo.art/sitemap.xml)、[pages-sitemap.xml](https://ojo.art/pages-sitemap.xml)；读取于 2026-08-26 |
| 社交与社区 | X `@OJOaidesign` —— "Joined June 2026"，2,076 关注者，171 关注中。Discord 服务器 "OJO" —— 303 名成员，37 人在线。网站上的邀请链接（`Fw55pk7z3N`）与 X 简介中的（`GDtZg4Fs27`）指向同一服务器 id `1503702135249047562`。 | [X 主页](https://x.com/OJOaidesign)、[Discord 邀请 API](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true)；观察于 2026-08-26 |
| 移动应用 | 美区 App Store 未检索到该品牌的应用 | [iTunes 搜索 API](https://itunes.apple.com/search?term=ojo%20design%20agent&entity=software&country=us&limit=5)；查询于 2026-08-26 |
| 互联网档案馆 | 未索引到 `ojo.art` 的任何快照 | [Wayback 可用性 API](http://archive.org/wayback/available?url=ojo.art) 与 CDX 索引；查询于 2026-08-26 |
| 团队、人数、融资 | 网站、法律文件及下文检索范围内的任何来源均未公布 | 见 `备注` |

### 名称与主体

| 名称 | 出现位置 | 说明 | 来源 |
|---|---|---|---|
| OJO | 公开品牌、域名、产品 | `ojo.art`；也是 CLI 可执行文件名 `ojo` | [ojo.art](https://ojo.art/) |
| Touchine AI (HK) Limited | 服务条款与隐私政策中的法律主体 | 香港特别行政区公司；商业登记号 80290592 | [服务条款](https://ojo.art/terms)、[tempb.com](https://www.tempb.com/companies/touchine-ai-hk-limited/) |
| OJO ART LIMITED | 仅出现在服务条款 §11 | 责任限制条款写作 "OJO ART LIMITED AND ITS DIRECTORS, EMPLOYEES, AND AGENTS SHALL NOT BE LIABLE…"，与前言中定义的主体不是同一个名字 | [服务条款](https://ojo.art/terms) §11 |
| Touchine（npm scope） | 软件包注册表 | `@touchine/ojo` —— "OJO CLI — login, project management, AI chat, run status queries, workspace sync, and session history"；该 scope 下还有 `@touchine/contract-design-project`（发布于 2026-04-21） | [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |
| touchine.ai | 域名 | 跳转至 `ojo.art` | 观察于 2026-08-26 |
| touchine.com | 域名 | 提供一个看上去无关的页面，标题为 "Touchine Project Engineering - Boson Core"，在中国大陆备案为 "京ICP备2026017083号-1" 与 "京公网安备11010502060187号"。没有任何来源将该备案与 Touchine AI (HK) Limited 关联起来，见 `备注`。 | [touchine.com](https://touchine.com/)；读取于 2026-08-26 |
| iRise / irise-studio | 静态资源与代码托管 | 市场站点由 `/_static/irise-official/` 提供；npm 包的 `repository` 字段指向 `git+https://github.com/irise-studio/irise-extension.git`，目录 `apps/cli` | [ojo.art](https://ojo.art/) 资源路径、[npm registry](https://registry.npmjs.org/@touchine%2Fojo) |
| Nexight | VS Code 插件市场发布者 | 发布者 `nexight`（显示名 "Nexight"），发布者域名 `https://ojo.art`（未通过域名验证），发布插件 `ojo` | [VS Code Marketplace API](https://marketplace.visualstudio.com/items?itemName=nexight.ojo)；读取于 2026-08-26 |
| `zk` | 前端存储键名 | 浏览器存储使用 `zk`／`ZK` 前缀（`zk-web-subscribe-billing-plans-cache-v1`、`__ZK_AUTH_STATE_SYNC__`、`zk_mixpanel_analytics_consent_v1`），应用的 i18n 键名以 `canvas.components.*` 命名 | 于 `ojo.art` 读取 localStorage，2026-08-26 |

GitHub 组织 `irise-studio` 存在，创建于 2026-04-08，有 6 个关注者、0 个公开仓库、无公开成员；未登录请求 `irise-studio/irise-extension` 返回 "Not Found"（[GitHub API](https://api.github.com/orgs/irise-studio)；读取于 2026-08-26）。

---

## Product

帮助中心将产品描述为 "an AI-powered design and development platform for the next generation of product creators"，用户 "describe what you want, and AI will build it for you immediately"，产出 "real, runnable product prototypes that can be previewed and interacted with directly in the browser, with one-click sync to a fully developable code project"（[帮助中心](https://ojo.art/help-center)；最后更新 2026-03-28）。

服务条款的描述则不同："ojo.art is an AI-powered visual design platform utilizing advanced models including but not limited to Google Gemini and Anthropic Claude to transform user prompts and inputs into professional design assets"，并列出 "Text-to-image and image-to-image generation; Design editing, iteration, and composition tools; Brand kit generation and asset management; Collaboration workspaces and template libraries"（[服务条款](https://ojo.art/terms) §3）。

### 界面与功能范围

| 界面 | 内容 | 来源 |
|---|---|---|
| 网页画布 | 主产品。每次生成的原型保存为一个项目，拥有唯一链接 `https://ojo.art/p/<projectId>`，并配有网页编辑器用于 "real-time preview, fine-tuning, and continued modification with AI assistance" | [帮助中心](https://ojo.art/help-center) §3.2–3.3 |
| Agent 团队与 Skills | 首页要求用户 "先组建你的 Agent 团队和 Skills，再让它们为你设计"，并宣称 "自由添加 200 多种不同类型的 Skills" | [ojo.art/zh-CN](https://ojo.art/zh-CN/)；访问于 2026-08-26 |
| 站点展示的具名 Skills | 产品页面架构、设计优化专家、产品需求分析、线框稿生成、站点结构分析、UI/UX 最佳实践、视觉基因生成、图片搜索 | [ojo.art/zh-CN](https://ojo.art/zh-CN/)；访问于 2026-08-26 |
| Agent 团队预设 | 落地页代码中包含四张团队卡片："Requirements Team"、"Redesign Team"、"Prototype Design Team"、"Game Workshop" | [ojo.art](https://ojo.art/) 的 `AgentTeamBridgeSection` 打包文件；读取于 2026-08-26 |
| CLI | `npm install -g @touchine/ojo`。命令包括 `ojo auth login`（模式 `web`、`device`、`pat`）、`ojo project list`、`ojo project open`、`ojo chat --message`、`ojo query --project-id`、`ojo workspace sync <id> [--path]`。同步下来的代码位于 `<project-name>/ojo-prototype`，自动安装依赖并启动开发环境。 | [ojo.art](https://ojo.art/)、[帮助中心](https://ojo.art/help-center) §3.4–3.5 |
| 编辑器插件 | "Ojo platform integration for VS Code and Cursor: sign in, open projects, chat with sessions, sync local workspaces, and (in Cursor) register a session-scoped Ojo MCP server for agent tools." | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=nexight.ojo) |
| 导出 | 首页写着 "支持CLI、插件嵌入AI开发流，资产互通 / 设计即交付"。套餐功能区分 "仅支持代码导出" 与 "全格式导出"。 | [ojo.art/zh-CN](https://ojo.art/zh-CN/)、[计费套餐 API](https://ojo.art/subscribe) |
| 博客 | 16 篇文章，分为 "OJO PlayBook"、"OJO Field Notes"、"OJO 最佳实践" 三个系列，六种语言全部发布 | [博客索引](https://ojo.art/blog/posts/)；读取于 2026-08-26 |

### 商业化

以下数据于 2026-08-26 从 [ojo.art/subscribe](https://ojo.art/subscribe) 渲染时调用的 `GET /api/commerce/v1/billing/plans` 读取。返回中 `commercializationMode` 为 `"live"`；套餐记录的 `updatedAt` 分别为 2026-06-17（Free）和 2026-07-13（全部付费套餐）。

| 套餐 | 月付 | 年付 | 积分 | 所列部分权益 |
|---|---|---|---|---|
| Free | $0 | $0 | 每日登录可领 200 积分，UTC 零点刷新 | 基础模型；分享链接仅可查看；不支持导出；256K 上下文窗口 |
| Plus | $27/月（2,200 积分） | $300/年，页面标注 "$25/月"（26,400 积分/年） | 同左 | "Flash + 有限高级模型"；仅支持代码导出；单项目保存 30 天；256K 上下文窗口；可购买积分包 |
| Pro | $62/月（5,000 积分） | $684/年，页面标注 "$57/月"（60,000 积分/年） | 同左 | "SOTA / Master / 生图模型"；全格式导出；长期历史记录；语音能力；分享并共同编辑；专属客服；1M 上下文窗口；CLI |
| Ultra | "即将开放" | — | "更高积分额度即将公布" | 团队成员与权限管理；更高并发通道；共享工作空间；企业级支持 |

积分包：500 积分 $8、1,000 积分 $15、3,000 积分 $40、8,000 积分 $99。所有付费项目的 `paymentMethods` 均为 `["card","alipay"]`，`checkoutProviders` 均为 `["stripe","antom"]`（计费套餐 API；读取于 2026-08-26）。服务条款补充：促销赠送积分 "within 30 days" 过期，订阅积分月付最多结转一个月、年付最多十二个月，购买的积分 "valid for 12 months"，且 "All purchases are final"（[服务条款](https://ojo.art/terms) §5）。

### 已披露的规模数据

未公布任何用户、订阅、收入或生成量总数。截至 2026-08-26 可获得的公开信号：

| 信号 | 数值 | 来源 |
|---|---|---|
| X 关注者 | 2,076（关注中 171）；账号 "Joined June 2026" | [@OJOaidesign](https://x.com/OJOaidesign) |
| 发布帖互动 | 53.3 万次浏览、235 条回复、114 次转发、823 次点赞 | [@OJOaidesign，2026-08-18](https://x.com/OJOaidesign/status/2089731834095489430) |
| Discord | 303 名成员、37 人在线；服务器 id `1503702135249047562`，按 Discord snowflake 换算对应 2026-05-12 | [Discord 邀请 API](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true) |
| VS Code 插件 | 版本 0.0.1，发布于 2026-03-20；17 次安装、222 次下载 | [VS Code Marketplace API](https://marketplace.visualstudio.com/items?itemName=nexight.ojo) |
| npm CLI | 5 个版本（1.0.4–1.0.8）；首次发布 2026-05-18，最新 1.0.8 发布于 2026-08-06 | [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |

### 已公布的内容规则

用户不得生成违反 "laws or regulations of Hong Kong, your jurisdiction, or international law"、侵犯知识产权、"Constitutes non-consensual intimate imagery, deepfakes for deceptive purposes, or harmful misinformation"、"Promotes hate speech, violence, discrimination, or illegal activities"、"Exploits or harms minors" 的内容，也不得通过脚本刷量或逆向工程冲击基础设施（[服务条款](https://ojo.art/terms) §7）。

AI 产出的所有权 "Upon generation and full payment of applicable Credits" 转移给用户，但用户不得 "Use AI Output to train, develop, or improve competing AI models or services"，也不得 "Resell raw AI Output as stock imagery, design templates, or NFT collections without substantial transformative modification"（[服务条款](https://ojo.art/terms) §6）。

---

## 团队

`ojo.art`、服务条款、隐私政策、帮助中心、X 账号，以及 `备注` 所述检索范围内的任何来源，均未提及创始人、高管、员工或人数。在公司物料中找到的仅有两个个人标识：`@touchine/ojo` 与 `@touchine/contract-design-project` 的 npm 维护者账号 `rogerhorsley`（`rogerhorsleymorris@gmail.com`）（[npm registry](https://registry.npmjs.org/@touchine%2Fojo)；读取于 2026-08-26），以及 Discord 邀请创建者 `waterplants888`／"Waterplants"（[Discord 邀请 API](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true)；读取于 2026-08-26）。两者均未在任何地方被标注为公司职务。

---

## 融资

公司未宣布、也没有任何检索到的来源报道过任何融资轮次、投资方、估值或金额。未找到 Touchine AI (HK) Limited 或 `ojo.art` 上 OJO 的 Crunchbase、PitchBook 或 Tracxn 档案；以 "OJO" 加融资关键词检索返回的是 **OJO Labs** —— 一家位于美国德州奥斯汀、与本公司无关的房地产公司，2019 年完成 4,500 万美元 C 轮（[PR Newswire，2019](https://www.prnewswire.com/news-releases/ojo-labs-raises-45-million-in-series-c-funding-to-accelerate-product-development-and-fuel-expansion-300814706.html)），见 `备注`。

---

## Engineering

### 技术栈与平台

| 层次 | 可观察到的内容 | 来源 |
|---|---|---|
| 市场站点 | React，采用 React Router 风格的入口（`entry.client`、`root`），使用 Rolldown 构建（`rolldown-runtime` chunk），由 `/_static/irise-official/` 提供；使用 Tailwind 风格的工具类 | [ojo.art](https://ojo.art/) 打包文件；读取于 2026-08-26 |
| 产品应用 | 独立的 webpack 构建，由 `/_static/canvas/` 提供，i18n 键名以 `canvas.*` 命名 | [ojo.art/subscribe](https://ojo.art/subscribe) 的网络请求；读取于 2026-08-26 |
| 构建期运行时配置 | `{"apiPrefix":"/api","authRedirectOrigin":"https://ojo.art","firebaseAuthOrigin":"https://ojo-art-platform.firebaseapp.com","officialHomeOrigin":"https://ojo.art","websocketEndpoint":"wss://ws.ojo.dev/ws","officialHomePath":"/"}` | `ojo.art` 的应用打包文件 `main.*.js`；读取于 2026-08-26 |
| 认证 | Firebase Auth（项目 `ojo-art-platform`），提供 "Continue with Google"、"Continue with GitHub"、邮件登录链接（`emailForSignIn`）以及六位验证码流程 | [ojo.art](https://ojo.art/) 的应用与 `official-copy` 打包文件；读取于 2026-08-26 |
| 支付 | Stripe 与 Antom；银行卡与支付宝 | [计费套餐 API](https://ojo.art/subscribe)；[服务条款](https://ojo.art/terms) §5.5 中点名 Stripe |
| 分析 | Mixpanel，受存储的同意标记（`zk_mixpanel_analytics_consent_v1`）控制；Cloudflare RUM（`/cdn-cgi/rum`） | `ojo.art` 的 localStorage 与网络请求；读取于 2026-08-26 |
| 边缘／CDN | Cloudflare（`server: cloudflare`、`cf-ray` 响应头） | 响应头；读取于 2026-08-26 |
| CLI | Node 包，`bin: {"ojo": "dist/index.js"}`；依赖包括 `ink` 与 `react`（终端 UI）、`commander`、`inquirer`、`axios`、`zod`、`ora`、`chalk`、`open`、`cli-table3`、`terminal-link`、`semver`、`sql.js`（本地 SQLite） | [npm registry](https://registry.npmjs.org/@touchine%2Fojo) |

### 系统

- **浏览器侧可观察到的 API：** `POST /api/account/api/user/v1/user_info`、`GET /api/commerce/v1/billing/plans`、`GET /client-context?device_timezone=…&browser_language=…&app_locale=…`（`ojo.art` 的网络请求；读取于 2026-08-26）。`/api/account/api/` 这种重复路径提示存在一层网关，为各服务加前缀。
- **实时通道：** WebSocket 端点 `wss://ws.ojo.dev/ws`，其 DNS 通过 CNAME 解析到 `…us-east-1.elb.amazonaws.com`（构建配置与 `dig`；读取于 2026-08-26）。
- **自带模型：** 应用打包文件中校验的服务商白名单为 `openai`、`openai-compatible`、`anthropic`、`gemini`、`deepseek`、`moonshot`、`kimi-global`、`kimi-code-plan`、`minimax`、`minimax-global`、`bailian-us`、`openrouter`，在界面上呈现为 "自定义模型 API 配置"，Plus 套餐标为限时体验、Pro 套餐为开放（应用打包文件与[计费套餐 API](https://ojo.art/subscribe)；读取于 2026-08-26）。
- **爬虫策略：** `robots.txt` 由 Cloudflare 托管，设置 `Content-Signal: search=yes,ai-train=no,use=reference`，并对 Amazonbot、Applebot-Extended、Bytespider、CCBot、ClaudeBot、CloudflareBrowserRenderingCrawler、Google-Extended、GPTBot 与 meta-externalagent 设置 `Disallow: /`（[robots.txt](https://ojo.art/robots.txt)；读取于 2026-08-26）。不带浏览器 User-Agent 的请求会收到 HTTP 403。

### 文档中的数据处理方式

- **数据区域。** "China Mainland Users: Personal data is processed and stored on servers located within the People's Republic of China, operated by qualified local service providers; International Users (US, EU, others): Data is stored in AWS US East jurisdictions"（[隐私政策](https://ojo.art/privacy-policy) §3.1）。该政策声明遵循香港 PDPO、GDPR、CCPA 与中国 PIPL（前言）。
- **使用用户内容训练。** "We may use Inputs and AI Output to train, develop, and improve our models and the Services. Personal identifiers are removed or anonymized before use in training datasets"，可通过 "Account Settings > Privacy" 或邮件退出（[服务条款](https://ojo.art/terms) §8、[隐私政策](https://ojo.art/privacy-policy) §4）。
- **第三方处理。** "Your Inputs are processed by third-party AI providers (Google, Anthropic)"；隐私政策补充 "No third-party AI provider uses your data to train their general models (prohibited by our contracts with Google and Anthropic)"（[服务条款](https://ojo.art/terms) §8.3、[隐私政策](https://ojo.art/privacy-policy) §4.1）。
- **留存期。** 内容删除 "within 30 days"，备份最长 90 天，已删除账号的数据 "permanently deleted within 90 days"，财务记录 "Retained for 7 years per Hong Kong tax law"（[服务条款](https://ojo.art/terms) §9.1、[隐私政策](https://ojo.art/privacy-policy) §6.1）。
- **声明的安全措施。** "TLS 1.3 encryption for data in transit; AES-256 encryption for data at rest; Access controls and audit logging; Regular security assessments"（[隐私政策](https://ojo.art/privacy-policy) §6.2）。
- **Cookie。** "We use essential cookies for authentication and service operation. We do not currently use tracking cookies for advertising purposes (No Google Analytics, No Facebook Pixel)"（[隐私政策](https://ojo.art/privacy-policy) §7）。

### 公司自述的目标用户

候补名单问卷要求申请者从 "Product prototyping"、"UI design and developer handoff"、"Design variants and exploration"、"Personal projects and portfolio" 中选择用途；从 "Product designer"、"Frontend developer"、"Product manager"、"Solo developer"、"Founder"、"Student" 中选择身份；从 "Solo"、"2–5"、"6–20"、"20+" 中选择团队规模。联系方式一步提供的社交平台选项中包含微信公众号（[ojo.art](https://ojo.art/) 的 `official-copy` 打包文件；读取于 2026-08-26）。

### 招聘要求与工作条件

未找到任何招聘信息、招聘页面或用人表述。`ojo.art` 上的 `/careers`、`/jobs` 与 `/about` 返回 HTTP 404（查询于 2026-08-26）。检索 "OJO" 时出现的职位 —— 例如 Built In Austin 上的 "Senior Product Designer, Agent Team" —— 属于奥斯汀那家无关的房地产公司 OJO Labs。

### 行业领域

面向产品团队的 AI 设计与原型工具：把自然语言需求转成 UI、落地页和可运行原型，并导出到代码与设计工具。

---

## 备注

### 未公开的信息

以下结论的检索范围（2026-08-26）：`ojo.art` 首页及六个语言根路径、`/terms`、`/privacy-policy`、`/help-center`、`/subscribe`、`/blog/posts/` 与 `/blog/zh-cn/posts/`、`robots.txt`、`sitemap.xml` 与 `pages-sitemap.xml`；对 `/about`、`/careers`、`/pricing`、`/privacy`、`/legal/*`、`/docs`、`/login`、`/app`、`/changelog`、`/refund-policy`、`/workspace`、`/canvas`、`/explore`、`/invite`、`/waitlist` 的探测；页面的网络请求、JavaScript 打包文件、构建期运行时配置与浏览器存储；计费套餐 API；`ojo.art`、`touchine.ai`、`touchine.com`、`ojo.dev` 与 `irise.art` 的 WHOIS 与 DNS；互联网档案馆 CDX 与可用性 API；npm registry 中的 `@touchine` scope；GitHub API 中的 `irise-studio`；VS Code Marketplace API；Discord 邀请 API；X 账号及其发布话题；美区 App Store；tempb.com 香港公司名录；以及围绕 OJO、ojo.art、Touchine、Touchine AI (HK) Limited、iRise Studio 和该 ICP 备案号的中英文检索。

- **创始人、高管与任何具名员工。** 公司控制的任何来源均未提及。
- **人数、办公地点与团队实际所在地。** 香港地址是列为法律联系地址的中环广场某室；未说明其他地点。站点图片资源中的中文文件名（`花`、`前景`、`人`、`代码`、`元素`、`背景`、`海报`、`荧幕`、`人物`、`墨水`、`素材`）以及 `touchine.ai` 与 `touchine.com` 的 CN 注册人国别，是仅有的与地点相关的信号。
- **任何融资轮次、投资方或估值。**
- **香港公司注册处的详细登记事项。** 未取得董事、股东与登记地址；上文的成立日期与商业登记号来自第三方聚合站，而非注册处本身，后者的查询需要付费或登录。
- **任何用户、订阅、收入、项目或生成量总数。**
- **各档位背后具体是什么模型。** 套餐提到 "基础模型"、"Flash + 有限高级模型" 与 "SOTA / Master / 生图模型"，未点名任何一个模型或版本。服务条款以 "including but not limited to" 提到 Google Gemini 与 Anthropic Claude。
- **每次操作消耗多少积分。** 只公布了各套餐的总额度，没有任何单次生成的积分价格。
- **Touchine AI (HK) Limited 与 `touchine.com` 背后北京主体之间的关系。** 备案号 "京ICP备2026017083号-1" 未能解析出登记名称；本环境下无法访问工信部备案查询服务。
- **"Nexight" 是谁。** 该 VS Code 发布者声称域名为 `https://ojo.art`，但插件市场未验证该域名，这一名称也未出现在公司的其他任何来源中。
- **GitHub 仓库。** 已发布 npm 包所引用的 `irise-studio/irise-extension` 为私有仓库。
- **LinkedIn 公司主页、Product Hunt 发布或主流媒体报道。** 均未找到；找到的唯一第三方文章是 [aiposthub.com](https://www.aiposthub.com/ojo-ai-design-agent-team-workspace/)（2026-08-19），属聚合站。
- **`ojo.art` 在互联网档案馆没有任何历史快照，** 这限制了对更早期定位的核查。
- **2026-08-26 无法读取的来源：** `ojo.art/dashboard` 与产品本身（邀请制）、`github.com/irise-studio/irise-extension`（私有）、香港公司注册处（需付费或登录），以及不带浏览器 User-Agent 通过普通 HTTP 客户端访问的 `ojo.art`（HTTP 403）。

### 来源之间的矛盾

- **服务条款里出现了两家公司。** 前言约束用户与 "Touchine AI (HK) Limited" 之间的关系，而责任限制条款限制的却是 "OJO ART LIMITED" 的责任（[服务条款](https://ojo.art/terms) 前言、§11）。站点上没有任何地方说明后一个名字对应哪家主体。
- **条款的日期早于公司成立。** 两份法律文件均标注 "Updated: Mar. 16, 2026 / Effective: Mar. 16, 2026"，而公司名录记录 Touchine AI (HK) Limited 成立于 2026-04-28（[服务条款](https://ojo.art/terms)、[tempb.com](https://www.tempb.com/companies/touchine-ai-hk-limited/)）。
- **Skills 数量说法不一。** 首页宣称 "200 多种" Skills；X 账号称 "OJO currently offers more than 300 skills"（[ojo.art/zh-CN](https://ojo.art/zh-CN/)、[@OJOaidesign](https://x.com/OJOaidesign)；均读取于 2026-08-26）。
- **计费接口的数值与自身文案不一致。** Free 套餐的功能文案写 "每日登录 100 积分"，而该套餐的 `credits` 字段与渲染出的页面都写 200。Plus 年付的功能文案写 "每年 30,000 积分"，而年付 `credits` 字段与渲染出的页面都写 26,400（[计费套餐 API](https://ojo.art/subscribe)；读取于 2026-08-26）。
- **对产品是什么有三套说法。** 服务条款（2026-03-16）描述的是 "an AI-powered visual design platform"，做 "Text-to-image and image-to-image generation … Brand kit generation and asset management"；帮助中心（2026-03-28）描述的是 "an AI-powered design and development platform"，产出可运行原型并同步到代码；首页与发布帖（2026 年 8 月）描述的则是面向产品策略、PRD 与原型的 "Design Agent Team Workspace"。服务条款列出的功能与当前产品文档中的界面并不对应。
- **同时流通两个 Discord 邀请链接。** 网站链接 `discord.gg/Fw55pk7z3N`，X 简介链接 `discord.gg/GDtZg4Fs27`；两者指向同一服务器（邀请 API；读取于 2026-08-26）。

### 其他

- **品牌比产品年轻。** VS Code 插件于 2026-03-20 发布时已称 "Ojo platform integration"，域名 `ojo.art` 注册于 2026-03-03，法律文件日期为 2026-03-16 —— 均早于 2026-08-18 的公开发布约五个月（[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=nexight.ojo)、WHOIS、[服务条款](https://ojo.art/terms)、[@OJOaidesign](https://x.com/OJOaidesign/status/2089731834095489430)）。
- **准入资格以邀请码形式在 X 上分发。** 公司在自己的发布帖下回复 "Go ojo.art and use OJO-T4FMC29RJE everyone."，随后又发 "use this: OJO-JT2G452FKN"；X 简介写着 "Comment OJO to get early access"（[@OJOaidesign](https://x.com/OJOaidesign/status/2089731834095489430)；读取于 2026-08-26）。第三方也在转发邀请码，例如 `OJO-MDTAM37V8T`（[versun.me，2026-08-20](https://versun.me/blog/tweet-2090310807007752333)）。
- **收款体系同时面向海外与中国用户。** 所有付费项目都同时列出 Stripe 与 Antom 作为收银渠道、银行卡与支付宝作为支付方式，价格以美元计，隐私政策则为中国大陆用户单独安排了数据基础设施（[计费套餐 API](https://ojo.art/subscribe)、[隐私政策](https://ojo.art/privacy-policy) §3.1）。
- **一个仍在内测的产品配了相当大的博客 SEO 面。** 三个系列共 16 篇文章在六种语言下全量发布 —— 96 个本地化 URL —— 标题针对 "What Is an AI Design Agent?"、"Prompt to UI: How to Generate Product Interfaces with AI"、"AI Website Design Generator" 一类检索词（[博客索引](https://ojo.art/blog/posts/)；读取于 2026-08-26）。
- **发布期的声量主要来自创作者账号。** 公司自己的帖子引用并转推了 `@jshguo`、`@PrajwalTomar_`、`@Shruti_0810`、`@yabhishekhd` 等第三方账号的内容（[@OJOaidesign](https://x.com/OJOaidesign)；读取于 2026-08-26）。
- **同名公司会干扰检索。** "OJO" 同时是 OJO Labs 的名字 —— 一家奥斯汀的房地产 AI 公司，2018 年融资 2,050 万美元、2019 年融资 4,500 万美元；以 "OJO" 加融资、招聘或高管关键词检索，返回的多是那家公司而非本文对象（[PR Newswire，2018](https://www.prnewswire.com/news-releases/ojo-labs-raises-20-5-million-in-series-b-financing-to-propel-its-conversational-ai-ojo-to-millions-of-consumers-300650811.html)、[PR Newswire，2019](https://www.prnewswire.com/news-releases/ojo-labs-raises-45-million-in-series-c-funding-to-accelerate-product-development-and-fuel-expansion-300814706.html)）。

---

## 资料来源

**官方**

- [ojo.art](https://ojo.art/) · [zh-CN](https://ojo.art/zh-CN/) · [zh-HK](https://ojo.art/zh-HK/) · [ja](https://ojo.art/ja/) · [es](https://ojo.art/es/) · [ko](https://ojo.art/ko/)
- [服务条款](https://ojo.art/terms)（更新／生效 2026-03-16）· [隐私政策](https://ojo.art/privacy-policy)（更新／生效 2026-03-16）· [帮助中心](https://ojo.art/help-center)（最后更新 2026-03-28）
- [定价](https://ojo.art/subscribe) · [博客（英文）](https://ojo.art/blog/posts/) · [博客（简体中文）](https://ojo.art/blog/zh-cn/posts/)
- [robots.txt](https://ojo.art/robots.txt) · [sitemap 索引](https://ojo.art/sitemap.xml) · [页面 sitemap](https://ojo.art/pages-sitemap.xml)
- 社交 —— [X @OJOaidesign](https://x.com/OJOaidesign) · [发布帖，2026-08-18](https://x.com/OJOaidesign/status/2089731834095489430) · [Discord](https://discord.gg/Fw55pk7z3N) · [Discord 邀请 API 记录](https://discord.com/api/v10/invites/Fw55pk7z3N?with_counts=true)
- 开发物料 —— [npm `@touchine/ojo`](https://www.npmjs.com/package/@touchine/ojo) · [npm registry 记录](https://registry.npmjs.org/@touchine%2Fojo) · [VS Code 插件 `nexight.ojo`](https://marketplace.visualstudio.com/items?itemName=nexight.ojo) · [GitHub 组织 `irise-studio`](https://github.com/irise-studio)
- 相关域名 —— [touchine.ai](https://touchine.ai/)（跳转至 `ojo.art`）· [touchine.com](https://touchine.com/)（独立站点，北京 ICP 备案）

**第三方**

- [tempb.com —— Touchine AI (HK) Limited](https://www.tempb.com/companies/touchine-ai-hk-limited/)（香港公司名录聚合站）
- [aiposthub.com —— OJO 是什麼？AI Design Agent Team 功能與限制](https://www.aiposthub.com/ojo-ai-design-agent-team-workspace/)（2026-08-19）
- [versun.me —— 转发邀请码](https://versun.me/blog/tweet-2090310807007752333)（2026-08-20）
- [iTunes 搜索 API —— 美区商店无第一方应用](https://itunes.apple.com/search?term=ojo%20design%20agent&entity=software&country=us&limit=5)

**同名但无关的公司（用于消歧）**

- [OJO Labs B 轮，2018](https://www.prnewswire.com/news-releases/ojo-labs-raises-20-5-million-in-series-b-financing-to-propel-its-conversational-ai-ojo-to-millions-of-consumers-300650811.html) · [OJO Labs C 轮，2019](https://www.prnewswire.com/news-releases/ojo-labs-raises-45-million-in-series-c-funding-to-accelerate-product-development-and-fuel-expansion-300814706.html)
