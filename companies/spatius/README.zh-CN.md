# Spatius

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-26。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-26。英文版为原始版本。

## 摘要

Spatius 卖的是实时 AI 数字人基础设施：云端 **Motion Server** 把语音音频转成面部驱动数据，**AvatarKit** 客户端 SDK（Web、iOS、Android、Flutter）在终端设备本地渲染一个 3D 高斯泼溅（3DGS）形象，因此不需要传输渲染好的视频流（[文档 — How It Works](https://docs.spatius.ai/concepts/how-it-works.md)；访问于 2026-08-26）。站点运营方是新加坡公司 **SPATIALWALK PTE. LTD.**（[spatius.ai](https://www.spatius.ai/)、[服务条款](https://www.spatius.ai/terms-of-service/)，生效于 2026-04-26）。同一业务在中国以 **空间漫步 / SpatialWalk** 品牌、由 **空间漫步科技（深圳）有限公司** 运营（[spatialwalk.cn](https://www.spatialwalk.cn/)，备案号 粤ICP备2025499042号）；另有第三个名字 **SpatialReal, Inc.**（美国加州圣何塞）出现在一个同时在线的平行站点上（[spatialreal.ai](https://www.spatialreal.ai/)；访问于 2026-08-26）—— 见 `品牌与法律实体`。

- 公开的性能与成本口径：入门级 SoC（G88、RK3576、S565、8189）上 1080p 25fps、无需独立 GPU，驱动数据 "~10–15 KB/s"，渲染环节额外延迟低于 300 ms，Scale 套餐 **$0.007/min（$0.42/小时）**，对比云端推流 "~$0.15 / min"（[spatius.ai](https://www.spatius.ai/)、[文档](https://docs.spatius.ai/concepts/how-it-works.md)、[spatialwalk.cn](https://www.spatialwalk.cn/)；访问于 2026-08-26）。
- **融资是投资方发布的，不是公司发布的。** Impa Ventures（新加坡）于 2025-10-31 发布 "IMPA Family | Our Investment in Spatial Walk"，未写轮次名称、金额与跟投方（[Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)）。公司自己关于融资的表述只出现在招聘文案里 —— 见 `融资`。
- **招聘记录是关于工程最丰富的公开来源。** 2025-05-12 至 2026-02-04 之间，`hr@spatialwalk.net` 在 V2EX 发了 13 篇招聘帖，写明了技术栈（Go 后端、Swift/Metal、Kotlin、Vue/WebGPU/wasm、3DGS）、base 城市从北京改为深圳，以及公司自述的 "中美双总部"（[sov2ex 索引](https://www.sov2ex.com/api/search?q=spatialwalk&size=20)；[V2EX 1131126](https://www.v2ex.com/t/1131126)、[V2EX 1189876](https://www.v2ex.com/t/1189876)）。
- 具名用户全部来自公司自己的博客：**Midoo AI**（"15K+ daily avatar sessions"，2026-07-01）、**ChickyTutor**（2026-07-08）与 **SayMei**（2026-08-11，附产品指标）；中文站另列 **Talk AI** 与 **听力熊**（[Spatius 博客](https://www.spatius.ai/blog/)、[spatialwalk.top](https://spatialwalk.top/)；访问于 2026-08-26）。
- 团队规模公司没有公布；LinkedIn 公司页写 "11-50 employees" 与 2025 年成立，而 GitHub 组织 `spatialwalk` 创建于 2024-05-23、`spatialwalk.net` 注册于 2024-08-08（[LinkedIn](https://www.linkedin.com/company/spatius-ai)、[GitHub API](https://api.github.com/orgs/spatialwalk)，WHOIS 读取于 2026-08-26）—— 见 `不同来源之间的不一致`。

---

## 基本情况

| 项目 | 内容 | 来源 |
|---|---|---|
| 当前公开品牌 | Spatius —— "Real-Time AI Avatar Infrastructure"、"Next-Gen Digital Human" | [spatius.ai](https://www.spatius.ai/)；访问于 2026-08-26 |
| 运营主体 | "SPATIALWALK PTE. LTD."，文中写明以 Spatius 名义经营 | [服务条款](https://www.spatius.ai/terms-of-service/)；生效于 2026-04-26 |
| 登记地址 | "70 Shenton Way, #16-13, EON Shenton, Singapore 079118" | [服务条款](https://www.spatius.ai/terms-of-service/)、[隐私政策](https://www.spatius.ai/privacy-policy/) |
| 新加坡注册信息 | UEN 202531523H，注册于 2025-07-21，状态 "Live Company"，主营行业 SSIC 63909 "Other information service activities n.e.c."，登记 1 名董事/股东 | [RecordOwl（ACRA 数据镜像）](https://recordowl.com/company/spatialwalk-pte-ltd)；读取于 2026-08-26 |
| 中国品牌与主体 | 空间漫步 / SpatialWalk；页脚 "© 2026 空间漫步科技（深圳）有限公司 版权所有" | [spatialwalk.cn](https://www.spatialwalk.cn/)；访问于 2026-08-26 |
| 中国备案号 | 粤ICP备2025499042号（广东，2025 年序列） | [spatialwalk.cn](https://www.spatialwalk.cn/)、[spatialwalk.top](https://spatialwalk.top/) |
| 美国主体 | "SpatialReal, Inc. · 160 E Tasman Dr, San Jose, CA 95134, USA" | [spatialreal.ai](https://www.spatialreal.ai/)；访问于 2026-08-26 |
| 适用法律 | "These Terms are governed by the laws of Singapore"；新加坡法院专属管辖，欧盟／英国消费者除外 | [服务条款](https://www.spatius.ai/terms-of-service/) |
| 责任上限 | 索赔前三个月已付费用与 "SGD 100" 两者中的较高者 | [服务条款](https://www.spatius.ai/terms-of-service/) |
| 文件日期 | 服务条款生效于 2026-04-26；隐私政策 "Last Updated: April 22, 2026"；中文合规接入指引更新于 2026-01-06 | [服务条款](https://www.spatius.ai/terms-of-service/)、[隐私政策](https://www.spatius.ai/privacy-policy/)、[合规接入指引](https://www.spatialwalk.cn/compliance-guide) |
| 公开联系方式 | `hello@spatius.ai`（演示、合作）、`support@spatius.ai`（隐私）；中国：`hello@spatialwalk.net`、`support@spatialwalk.net`；招聘：`hr@spatialwalk.net` | [联系页](https://www.spatius.ai/contact/)、[隐私政策](https://www.spatius.ai/privacy-policy/)、[spatialwalk.top](https://spatialwalk.top/)、[V2EX 1173996](https://www.v2ex.com/t/1173996) |
| 人数 | LinkedIn 公司页写 "11-50 employees"；公司自己未公布数字 | [LinkedIn](https://www.linkedin.com/company/spatius-ai)；访问于 2026-08-26 |
| 社区 | Discord "Spatius" —— 51 名成员、4 人在线；更早的 "SpatialReal Inc." 服务器 —— 39 名成员、6 人在线 | [Discord invite API（Spatius）](https://discord.com/api/v9/invites/9HGhZfHZh9?with_counts=true)、[Discord invite API（SpatialReal）](https://discord.com/api/v9/invites/dRSUTdPCjm?with_counts=true)；读取于 2026-08-26 |
| 域名 | `spatialwalk.net` 注册于 2024-08-08（Cloudflare）；`spatialreal.ai` 注册于 2025-11-03；`spatius.ai` 注册于 2026-04-10；`spatialwalk.ai` 以 301 跳转至 `www.spatialwalk.cn`；`spatialwalk.top` 提供中文 SpatialWalk 站点并承载 `cn-beijing` 控制台 | WHOIS 读取于 2026-08-26；跳转观察于 2026-08-26；[文档 — Regions](https://docs.spatius.ai/api-reference/regions.md) |
| GitHub 组织 | `spatialwalk` —— 创建于 2024-05-23，10 个公开仓库，website 字段为 `spatius.ai`；`spatius-ai` —— 创建于 2026-04-19，11 个公开仓库 | [GitHub API](https://api.github.com/orgs/spatialwalk)、[GitHub API](https://api.github.com/orgs/spatius-ai)；读取于 2026-08-26 |
| 移动应用 | 美国区 App Store 中未搜到 "spatius" 或 "spatialwalk" 的第一方应用 | [iTunes 搜索 API](https://itunes.apple.com/search?term=spatius&entity=software&country=us&limit=5)；检查于 2026-08-26 |
| 站点规模 | 主 sitemap 共 210 个 URL（其中 188 个是博客文章），另有 comparisons、integrations、glossary 三份各 51 个 URL 的 sitemap；含英文与 `/zh/` 两个语言版本 | [sitemap 索引](https://www.spatius.ai/sitemap-index.xml)；读取于 2026-08-26 |

### 品牌与法律实体

| 名称 | 类型 | 司法辖区／期间 | 来源中表述的关系 | 来源 |
|---|---|---|---|---|
| Spatius | 当前国际品牌 | `spatius.ai`，域名注册于 2026-04-10 | "SPATIALWALK PTE. LTD. operating as Spatius" | [服务条款](https://www.spatius.ai/terms-of-service/) |
| SPATIALWALK PTE. LTD. | 法律实体 | 新加坡，UEN 202531523H，注册于 2025-07-21 | `spatius.ai` 的运营方；出现在站点页脚与法律文件中 | [RecordOwl](https://recordowl.com/company/spatialwalk-pte-ltd)、[spatius.ai](https://www.spatius.ai/) |
| 空间漫步科技（深圳）有限公司 | 法律实体 | 中国深圳；备案号 粤ICP备2025499042号 | `spatialwalk.cn` 的版权方，该站点以 Spatius 名义售卖同一产品 | [spatialwalk.cn](https://www.spatialwalk.cn/) |
| SpatialWalk / 空间漫步 | 面向中国市场的品牌 | `spatialwalk.net`（注册于 2024-08-08）、`spatialwalk.cn`、`spatialwalk.top` | 同一条产品线；中文站页脚为 "SpatialWalk 空间漫步科技（深圳）有限公司" | [spatialwalk.top](https://spatialwalk.top/) |
| SpatialReal, Inc. | 法律实体 | 160 E Tasman Dr, San Jose, CA 95134, USA | `spatialreal.ai` 页脚；该站点在线售卖同一套 SDK，`docs.spatialreal.ai` 正是 `spatialwalk` GitHub 组织的示例仓库所链接的文档站 | [spatialreal.ai](https://www.spatialreal.ai/)、[avatarkit-voice-agent-demo](https://github.com/spatialwalk/avatarkit-voice-agent-demo) |
| SpatialReal | 此前／并行的国际品牌 | `spatialreal.ai`，域名注册于 2025-11-03 | npm 包 `@spatialwalk/avatarkit` 的描述为 "for SpatialReal avatars"；2026 年被 `@spatius/avatarkit` 取代 | [GitHub API](https://api.github.com/orgs/spatialwalk)、[npm registry](https://registry.npmjs.org/@spatialwalk/avatarkit) |
| 空间漫步传媒科技（深圳）有限责任公司 | 无关的名称撞车 | 成立于 2019-08-20，法定代表人 耿珑 | 另一家中文名相近的深圳公司；未建立任何关联 | [百度百科](https://baike.baidu.com/item/%E7%A9%BA%E9%97%B4%E6%BC%AB%E6%AD%A5%E4%BC%A0%E5%AA%92%E7%A7%91%E6%8A%80%EF%BC%88%E6%B7%B1%E5%9C%B3%EF%BC%89%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/24226245) |

所查资料中没有任何一份说明新加坡、中国与美国三个主体之间的关系 —— 持股结构、各地区的签约主体、以及深圳工程团队的雇主是谁，均未公开。

---

## 产品

平台公开的组成部分有三个（[文档 — Welcome](https://docs.spatius.ai/getting-started.md)；访问于 2026-08-26）：

- **AvatarKit** —— Web、iOS、Android、Flutter 的客户端 SDK，"download avatar assets, render the avatar locally, and play synchronized audio"。形象资产是 "about 5-10 MB" 的 3D 高斯泼溅包，必须下载完成后才开始渲染（[文档 — Avatar](https://docs.spatius.ai/concepts/avatar.md)）。
- **Motion Server** —— 云端服务，"receives avatar speech audio, returns motion data"，码率 "~10–15 KB/s, much lower than a video stream"（[文档 — How It Works](https://docs.spatius.ai/concepts/how-it-works.md)）。
- **Spatius Studio** —— `app.spatius.ai` 上的 Web 控制台，用于管理应用与形象（页面标题 "Spatius Studio"，读取于 2026-08-26）。

文档中的接入方式：**Direct Mode**（客户端持有音频）、**Backend Mode**（Python 与 Go 服务端 SDK）、**LiveKit Agents**、**Agora Convo AI**，以及一个 **TEN Framework** 扩展（[文档 — Integrations](https://docs.spatius.ai/integrations/overview.md)、[SDK 能力矩阵](https://docs.spatius.ai/reference/sdk-capabilities.md)）。音频输入为 "mono 16-bit PCM (`s16le`)"，部分 SDK 接受 Opus；平台只负责驱动形象 —— "developers manage microphone, ASR, LLM, and speech generation"（[文档 — FAQ](https://docs.spatius.ai/resources/faq.md)）。

公开的区域有三个：`us-west`、`ap-northeast`、`cn-beijing`；中国控制台运行在 `console.cn-beijing.spatialwalk.top`，其余端点在 `spatius.ai` 下（[文档 — Regions](https://docs.spatius.ai/api-reference/regions.md)）。

形象通过一套有文档的 REST API 生成：`POST /avatars` 接收一个公网可访问的 JPEG 或 PNG 链接，最大 5 MiB，短边不小于 340 px，"Exactly one clearly visible face"，返回一个需要轮询的异步任务；每次成功生成消耗一个 "Avatar Creations" 额度，并受频率、24 小时滚动配额与并发限制（[文档 — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)）。

营销站点上公开的性能与成本口径（访问于 2026-08-26）：

| 口径 | 数值 | 来源 |
|---|---|---|
| 分辨率与帧率 | 入门级 SoC 上 1080p 25fps，"（G88, RK3576等低功耗芯片验证通过)"，无需独立 GPU | [spatialwalk.cn](https://www.spatialwalk.cn/)、[spatius.ai](https://www.spatius.ai/) |
| 渲染附加延迟 | "<300ms"；配合高性能音频方案可实现 "<1s 端到端延迟" | [spatialwalk.cn](https://www.spatialwalk.cn/) |
| 带宽 | "100 kbps"（英文站）；"10–20KB/s 参数包"（中文站）；"~10–15 KB/s"（文档） | [spatius.ai](https://www.spatius.ai/)、[spatialwalk.top](https://spatialwalk.top/)、[文档](https://docs.spatius.ai/concepts/how-it-works.md) |
| 抗丢包 | "三倍冗余抗丢包，网络抖动下播放不中断" | [spatialwalk.cn](https://www.spatialwalk.cn/) |
| 渲染分工 | "90% 渲染在端侧完成" | [spatialwalk.top](https://spatialwalk.top/) |
| 技术路线 | "3DGS路线 + 自研轻量化多模态模型 + 端侧实时推理"，外加自研音素同步算法 | [spatialwalk.top](https://spatialwalk.top/) |
| 接入工作量 | "一个熟练的客户端工程师仅需2-3个工作日即可完成核心功能的集成" | [spatialwalk.top](https://spatialwalk.top/) |
| 累计用量 | "10M+ interactions processed to date" | [spatialreal.ai](https://www.spatialreal.ai/) |

### 商业化

Spatius 公开的是基于积分的价目表，五档自助套餐加企业版：Free（$0，1,000 积分 ≈ 100 分钟，2 路并发）、Starter（$19）、Builder（$49）、Growth（$149）、Scale（$299，400,000 积分 ≈ 40,000 分钟，40 路并发，单次会话时长不限）；年付标称 8 折。超量计费在 Starter 至 Growth 为 "$0.009/minute"，Scale 为 "$0.007/minute"。形象生成单独售卖，从单个 $25 到 500 个装每个 $16。企业版宣传不限会话数、定制形象 API、SLA 与 "SOC II/GDPR compliance"（[定价页](https://www.spatius.ai/pricing/)；读取于 2026-08-26）。

中文站用同样的单价配了一个预算计算器：$5,000 预算下，"Spatius 进阶版套餐（端云结合）" 按 "$0.007 / min" 可得 "11,349 小时"，而行业均价 "~$0.15 / min" 只有 "556 小时"（[spatialwalk.cn](https://www.spatialwalk.cn/)）。中文 FAQ 对硬件场景写的是另一种商业形态："针对C端硬件产品，我们主要采用按激活设备量的年度授权或终身授权"，软件则按用量或按月计费（[spatialwalk.top](https://spatialwalk.top/)）。

并行的 `spatialreal.ai` 价目表在免费档上不一致 —— "Free: 500 credits/month" 对 Spatius 的 1,000，"Starter: 22,000 credits/month ($19)" 对 Spatius 的 20,000（[spatialreal.ai](https://www.spatialreal.ai/)；读取于 2026-08-26）。

### 公开规模变化

| 日期 | 事件或数字 | 来源 |
|---|---|---|
| 2024-05-23 | GitHub 组织 `spatialwalk` 创建 | [GitHub API](https://api.github.com/orgs/spatialwalk) |
| 2024-08-08 | `spatialwalk.net` 域名注册 | WHOIS 读取于 2026-08-26 |
| 2025-11-06 | 首个公开 SDK 版本：npm `@spatialwalk/avatarkit` 1.0.0-beta.1，描述 "AvatarKit SDK - 3D Gaussian Splatting Avatar Rendering SDK"，MIT 许可 | [npm registry](https://registry.npmjs.org/@spatialwalk/avatarkit) |
| 2025-12-07 | Flutter 插件 `avatar_kit` 1.0.0-beta.1 发布 | [pub.dev](https://pub.dev/packages/avatar_kit) |
| 2026-04-10 | `spatius.ai` 域名注册；GitHub 组织 `spatius-ai` 创建于 2026-04-19 | WHOIS 读取于 2026-08-26；[GitHub API](https://api.github.com/orgs/spatius-ai) |
| 2026-07-01 | 博客："How Midoo AI Scaled to 15K+ Daily Avatar Sessions with Spatius" | [Spatius 博客](https://www.spatius.ai/blog/) |
| 2026-07-26 | 客户故事中引用的 SayMei 数字："2,300+ registered learners"、"10,000+ completed live lesson sessions"、"312,000+ … conversation turns"、"190+ hours of live lesson time since April 25" | [SayMei 客户故事](https://www.spatius.ai/blog/saymei-ai-mandarin-tutor-spatius/)；发布于 2026-08-11 |
| 2026-08-17 | `@spatius/avatarkit` 1.3.7 与 iOS v1.3.3 发布 | [npm registry](https://registry.npmjs.org/-/v1/search?text=spatius&size=20)、[GitHub releases](https://github.com/spatius-ai/avatarkit-ios-release/releases) |
| 2026-08-24 | 近一个月 npm 下载量：`@spatius/avatarkit` 7,417 次，`@spatialwalk/avatarkit` 973 次 | [npm API](https://api.npmjs.org/downloads/point/last-month/@spatius/avatarkit) |

### 已公布的客户

| 客户 | 声称内容 | 日期 | 来源 |
|---|---|---|---|
| Midoo AI | "Scaled to 15K+ Daily Avatar Sessions with Spatius" | 2026-07-01 | [Spatius 博客](https://www.spatius.ai/blog/) |
| ChickyTutor | 在语音家教产品上加了一层实时形象 | 2026-07-08 | [Spatius 博客](https://www.spatius.ai/blog/) |
| SayMei | 以 Spatius 形象作为 LiveKit 中文家教的可见层；"12 average conversation turns with Spatius Pink (vs. 7 with previous avatar)"；引语署名 "Leland Char, Founder of SayMei" | 2026-08-11 | [SayMei 客户故事](https://www.spatius.ai/blog/saymei-ai-mandarin-tutor-spatius/) |
| Talk AI | AI 口语外教："接入 SDK，实时对话、精准口型、自然表情" | 未标日期 | [spatialwalk.top](https://spatialwalk.top/) |
| 听力熊 | 儿童 AI 伙伴产品："按设备授权的低成本SDK" | 未标日期 | [spatialwalk.top](https://spatialwalk.top/) |

### 公司自述的计划

- 定制训练的 3DGS 形象模型被描述为 "currently in beta access"，中文站把基于图片的形象定制标为 "用户内测开放中"（[Spatius 博客 — 产品更新](https://www.spatius.ai/blog/spatius-product-update-avatar-apis-faster-audio-production-ready-sdks/)，发布于 2026-08-22；[spatialwalk.cn](https://www.spatialwalk.cn/)）。
- 中文 FAQ 写 "我们目前全面支持 iOS，Web及Android SDK将在11月上线" —— Web 与 Android SDK 定在 11 月上线，页面上没有写年份（[spatialwalk.top](https://spatialwalk.top/)；读取于 2026-08-26）。
- 招聘文案把目标写为 "打造端侧 AI 形象引擎，重构全球下一代人机交互标准"（[V2EX 1189876](https://www.v2ex.com/t/1189876)；2026-02-01）。

---

## 创始人

中文站公开了一个四人团队区块（2026-08-26 读取自 [spatialwalk.top](https://spatialwalk.top/)，该站与 `spatialwalk.net` 是同一页面）：

| 姓名 | 页面上的头衔 | 页面上的描述 |
|---|---|---|
| Hang Li | CEO | "前腾讯产品经理，曾为中国Top 1的音乐社交产品赋能过亿用户增长" |
| Yuhang Li | CTO | "前字节跳动资深全栈工程师，丰富的软件开发及渲染引擎经验" |
| Yudong Guo | 首席科学家 | "3D数字人领域奠基性论文AD-NeRF作者，中国科学技术大学助理教授" |
| Xiaodong Cun | 首席技术顾问 | "SadTalker (13k+ GitHub Stars) 作者 … 前腾讯AI Lab高级研究员，大湾区大学助理教授" |

两位学者可核实的履历，来自他们自己的页面：

- **Yudong Guo** 是中国科学技术大学助理教授；2021 年在该校获得博士学位，导师为 Juyong Zhang 教授，2015 年获统计学学士学位，2016 年秋至 2017 年春在南洋理工大学 MultiMedia Lab 任研究助理。AD-NeRF（"AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis"）发表于 ICCV 2021（[yudongguo.github.io](https://yudongguo.github.io/)；访问于 2026-08-26）。其页面未提及 Spatius、SpatialWalk 或任何公司职务。
- **Xiaodong Cun** 是大湾区大学计算与信息科学学院助理教授，主持该校 GVC Lab；SadTalker 发表于 CVPR 2023，作者署名中包含腾讯 AI Lab（[SadTalker 项目页](https://sadtalker.github.io/)、[GitHub — OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker)；访问于 2026-08-26）。

投资方的公告补充了创始人的经历，文中只以 "Hang" 相称："Hang has spent over seven years as a product manager at leading Internet companies like Tencent"；他 "built a matchmaking app in college and eventually quit his stable career to start Spatial Walk — right when Apple unveiled the Vision Pro"，并飞到纽约排队体验该设备（[Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)；2025-10-31）。

招聘文案把更大范围的团队描述为 "核心团队来自清华、中科大、南洋理工、字节跳动、腾讯，曾在 CVPR 、ICCV 、NeurIPS 等顶级学术会议发表多篇论文，并与清华、浙大等高校实验室长期合作"（[V2EX 1153830](https://www.v2ex.com/t/1153830)；2025-08-20）。任何公司页面都没有具名列出工程师，`spatius.ai` 与 `spatialreal.ai` 也都没有团队页。

---

## 融资

| 日期 | 轮次 | 金额 | 投资方 | 来源 |
|---|---|---|---|---|
| 2025-10-31 | 未写明 | 未披露 | Impa Ventures（新加坡） | [Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk) |
| 2025-05-12 | 招聘帖中称的 "种子融资" | "数百万"（未写币种）；"下一轮美元融资进行中" | 未具名 | [V2EX 1131126](https://www.v2ex.com/t/1131126) |
| 2025-08-20 起 | 招聘帖中称的 "多轮融资" | "估值过亿" | 未具名 | [V2EX 1153830](https://www.v2ex.com/t/1153830)、[V2EX 1161367](https://www.v2ex.com/t/1161367) |

表格之外的事实：

- 唯一找到的投资方公告是 Impa Ventures 的那篇。文中没有轮次、金额与跟投方，并把该基金描述为投资 "AI and frontier technologies … from 0 to 1"（[Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)；[Impa Ventures](https://impa.ventures/)）。
- 该文的对比表把 Spatial Walk 的价格写为 "$0.003 / min"，对比 Tavus（$0.3/min）、Synthesia（$3/min）与 HeyGen（"Real-time $0.15 / min"）—— 大约是公司十个月后公布价格 $0.007/min 的一半。
- 任何公司站点、任何新闻稿、任何中英文媒体上都没有找到融资公告；Crunchbase 返回 HTTP 403，PitchBook 需订阅（检查于 2026-08-26）—— 见 `备注`。
- 招聘帖是雇主自己写的招聘文案，不是备案文件或投资方声明。这里收录它们，是因为这是公司方关于融资仅有的公开表述。

---

## 工程

### 技术栈与平台

由公开产物（软件包、仓库、文档）确认：

- **客户端 SDK** —— Web（`@spatius/avatarkit`，MIT，1.3.7 发布于 2026-08-17；前身 `@spatialwalk/avatarkit` 共 104 个版本，2025-11-06 至 2026-04-22）、iOS（Swift；发布仓库 `spatius-ai/avatarkit-ios-release`，v1.3.3 发布于 2026-08-17）、Android（Kotlin；Maven Central 制品 `ai.spatialwalk:avatarkit`）、Flutter（pub.dev 上的 `avatar_kit`，44 个版本，首发于 2025-12-07）（[npm](https://registry.npmjs.org/@spatialwalk/avatarkit)、[pub.dev](https://pub.dev/packages/avatar_kit)、[Maven Central](https://mvnrepository.com/artifact/ai.spatialwalk/avatarkit)、[GitHub releases](https://github.com/spatius-ai/avatarkit-ios-release/releases)）。
- **服务端 SDK** —— Python 与 Go，早期组织中另有一个 TypeScript 服务端 SDK；还有一个 Go 写的 `open-platform-cli`（[GitHub API](https://api.github.com/orgs/spatius-ai)、[GitHub API](https://api.github.com/orgs/spatialwalk)）。
- **实时传输** —— LiveKit（自有插件 `livekit-plugins-spatius`，Web 端内置 provider）与声网 Agora（iOS/Android 原生 provider、Convo AI 接入、TEN Framework 扩展）；也支持 WebSocket（[文档 — Integrations](https://docs.spatius.ai/integrations/overview.md)、[SDK 能力矩阵](https://docs.spatius.ai/reference/sdk-capabilities.md)）。
- **渲染** —— 3D 高斯泼溅资产在客户端渲染；npm 包描述为 "3D Gaussian Splatting Avatar Rendering SDK"（[npm](https://registry.npmjs.org/@spatialwalk/avatarkit)）。
- **音频** —— 单声道 16-bit PCM（`s16le`），客户端 SDK 默认启用 Opus 上行（[文档 — FAQ](https://docs.spatius.ai/resources/faq.md)、[SDK 能力矩阵](https://docs.spatius.ai/reference/sdk-capabilities.md)）。
- **隐私政策中具名的基础设施与供应商** —— AWS 与 Google Cloud（基础设施）、LiveKit Cloud（通信）、PostHog（分析）、Stripe（支付）、Google 与 GitHub（登录），以及未具名的 ASR 供应商（[隐私政策](https://www.spatius.ai/privacy-policy/)）。
- **边缘** —— `spatius.ai` 前置 Cloudflare（响应头 `server: cloudflare`，观察于 2026-08-26）。
- **文档** —— MDX，由公开仓库 `spatius-ai/docs` 发布，并提供 `llms.txt` 索引（[GitHub API](https://api.github.com/orgs/spatius-ai)、[llms.txt](https://docs.spatius.ai/llms.txt)）。

只作为招聘要求或加分项出现、未确认在用的：Kubernetes、gRPC、Redis、Kafka、Docker、Vue.js、React、Node.js、WebGL/WebGPU/WebXR、WebAssembly、Metal、Vulkan、OpenGL ES、MediaCodec、AVFoundation、Unity3D/Unreal 的 Shader 开发（[V2EX 1173996](https://www.v2ex.com/t/1173996)、[V2EX 1136977](https://www.v2ex.com/t/1136977)、[V2EX 1175749](https://www.v2ex.com/t/1175749)、[V2EX 1132398](https://www.v2ex.com/t/1132398)）。

### 系统

- **驱动推理服务** —— 接收语音音频、输出面部驱动参数，码率约 10–15 KB/s，按区域部署，通过 WebSocket 在 `wss://api.<region>.spatius.ai/v2/driveningress` 接入（[文档 — How It Works](https://docs.spatius.ai/concepts/how-it-works.md)、[文档 — Regions](https://docs.spatius.ai/api-reference/regions.md)）。
- **控制台与会话令牌 API** —— 各区域的 `console.<region>` 端点签发单次会话令牌，管理 API 用 `X-App-ID`/`X-API-Key` 鉴权（[文档 — Regions](https://docs.spatius.ai/api-reference/regions.md)、[文档 — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)）。
- **形象生成流水线** —— 异步任务，把提交的照片转成可下载的 3DGS 形象包，并带有额度预占与释放语义（[文档 — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)）。
- **客户端渲染与播放引擎** —— 资产下载、本地渲染、音频与驱动数据同步、生命周期与状态事件、帧饥饿处理、渲染质量控制（[文档 — Client Lifecycle](https://docs.spatius.ai/concepts/lifecycle.md)、[SDK 能力矩阵](https://docs.spatius.ai/reference/sdk-capabilities.md)）。
- **全球后端** —— 招聘文案描述为用 Go 构建的 "全球多点部署、低延迟、自动扩缩容"，并建设 "监控、Tracing 、告警体系"（[V2EX 1173996](https://www.v2ex.com/t/1173996)；2025-11-20）。

### 招聘所需技术背景

取自 2025-05 至 2026-02 的招聘帖（[sov2ex 索引](https://www.sov2ex.com/api/search?q=spatialwalk&size=20)）：

- **要求** —— Go、Python 或 Node.js 后端开发与 API 设计；iOS 侧 Swift、UIKit/SwiftUI、GCD 与 Concurrency；Android 侧 Kotlin/Java、Android Framework、线程与内存模型；前端实习岗要求 Vue.js；后端岗要求 Docker、Linux 与云原生运维；能设计 "对外 SDK" 并讲究接口设计。
- **加分项** —— 分布式与高并发系统；Kubernetes、gRPC、Redis、Kafka；移动端图形（Metal、OpenGL ES、Vulkan）与 Shader 开发；音视频与 WebRTC；数字人、VR/AR 项目经验；对 3DGS 或 NeRF 的研究了解；开源项目或技术博客；资深移动端岗位要求字节跳动、腾讯、阿里、美团或 Google/Meta 等大厂经验。
- 多篇帖子反复出现的表述："能快速使用 AI 工具实现自己的想法" 与 "Everybody codes 也是我们企业价值观的一部分"；企业版 Cursor 与 Claude Code 被列为提供的工具（[V2EX 1161367](https://www.v2ex.com/t/1161367)；2025-09-23）。

### 行业领域

工作内容落在实时形象渲染与端侧推理上，面向公司自己列出的场景：教学培训、招聘面试、直播互动、智能终端、车载与自助终端、AI 硬件（[spatialwalk.cn](https://www.spatialwalk.cn/)、[spatius.ai](https://www.spatius.ai/)）。其中两块领域知识带有明确义务，而非仅是加分项：

- **中国个人信息合规** —— 面向客户的合规接入指引援引《个人信息保护法》《数据安全法》《网络安全法》，并列出义务：SDK 初始化前须取得同意、不满 14 周岁需监护人授权、未成年人语音数据保存不超过 7 天、新版本发布后 30 天内完成 SDK 升级、"接受" 与 "拒绝" 按钮同等显著（[合规接入指引](https://www.spatialwalk.cn/compliance-guide)；更新于 2026-01-06）。
- **面向新加坡主体产品的数据处理** —— 音频 "permanently deleted immediately upon completion of transcription"，交互文本经 LiveKit 保存 30 天，账号数据保存至账号存续期结束后 3 年，开发者上传的照片保存至删除后 30 天，支付记录 7 年，欧洲经济区／英国的跨境传输使用标准合同条款（[隐私政策](https://www.spatius.ai/privacy-policy/)；更新于 2026-04-22）。

### 工作条件

| 项目 | 内容 | 来源 |
|---|---|---|
| base 城市 | 2025-08 之后的帖子写 "深圳，远程"；2025-05 与 2025-06 的帖子写 "base 北京（支持远程办公）" | [V2EX 1153930](https://www.v2ex.com/t/1153930)、[V2EX 1131126](https://www.v2ex.com/t/1131126) |
| 公司自述 | "中美双总部创业公司" | [V2EX 1160643](https://www.v2ex.com/t/1160643)；2025-09-19 |
| 远程政策 | 允许远程，多篇帖子附有条件："熟悉后可远程"、"能力优秀者接受远程" | [V2EX 1153830](https://www.v2ex.com/t/1153830)、[V2EX 1160643](https://www.v2ex.com/t/1160643) |
| 薪酬 | "薪资标准直接对标字节跳动 (ByteDance) 等大厂同职级级别"；"不逊大厂的薪资和远超大厂的期权"；未公开薪资区间 | [V2EX 1189876](https://www.v2ex.com/t/1189876)、[V2EX 1175749](https://www.v2ex.com/t/1175749) |
| 期权 | 面向优秀者与资深岗位写明有期权 | [V2EX 1153830](https://www.v2ex.com/t/1153830)、[V2EX 1189876](https://www.v2ex.com/t/1189876) |
| 提供的工具 | "企业版 cursor ，claude code 等 AI 工具" | [V2EX 1161367](https://www.v2ex.com/t/1161367) |
| 应届与实习 | 2025-06-06 发布过一个全职前端实习岗并写明有转正机会；多个岗位接受 "本科及以上在读" | [V2EX 1136977](https://www.v2ex.com/t/1136977)、[V2EX 1153830](https://www.v2ex.com/t/1153830) |
| 工作语言 | 没有作为制度写明；2026-02 的移动端岗位要求 "良好的英文阅读能力"，所有招聘帖都是中文，而产品、文档与支持界面是英文 | [V2EX 1189876](https://www.v2ex.com/t/1189876)、[文档](https://docs.spatius.ai/getting-started.md) |
| 投递方式 | `hr@spatialwalk.net`，邮件标题 "姓名+应聘岗位"；任何公司站点上都没有招聘页 | [V2EX 1160643](https://www.v2ex.com/t/1160643)；路径探测于 2026-08-26 |

---

## 备注

### 未公开披露

检索日期 2026-08-26，范围覆盖公司各站点（`spatius.ai`、`spatialwalk.cn`、`spatialwalk.top`、`spatialreal.ai`）、文档站、两个 GitHub 组织、各软件包仓库、V2EX、互联网档案馆，以及中英文网络搜索：

- **融资金额、轮次名称、估值与投资方名单。** 只有 Impa Ventures 一家具名，且出自其自己的文章，无任何数字。
- **空间漫步科技（深圳）有限公司的工商登记信息** —— 成立日期、法定代表人、注册资本与股东均未取得；天眼查返回 HTTP 419，企查查搜索被 Cloudflare 拦截。
- **SPATIALWALK PTE. LTD.、空间漫步科技（深圳）有限公司与 SpatialReal, Inc. 之间的持股关系。**
- **公司自己给出的人数。** 只有 LinkedIn 的 "11-50 employees" 区间，且同一页面在平台上只列出 5 名员工。
- **招聘页。** `spatius.ai` 的 `/careers`、`/jobs`、`/about`、`/company`、`/team` 全部返回首页而非独立页面（探测于 2026-08-26）；招聘走 V2EX 帖子与 `hr@spatialwalk.net`。
- **安全认证。** "SOC II/GDPR compliance" 只作为定价页企业版的一条卖点出现；没有找到证书、审计报告或信任中心页面。
- **工程博客。** 188 篇博客是产品、对比与选型导购类内容；没有任何一篇工程文章说明延迟与带宽口径背后的模型、训练数据或测试方法。
- **2026-08-26 无法读取的来源：** Crunchbase（HTTP 403）、PitchBook（需订阅）、LinkedIn 个人主页（HTTP 999）、`spatialwalk.net`（对非浏览器客户端返回 HTTP 418 —— 同一站点改从 `spatialwalk.top` 读取）、`remote-info.cn`（域名无法解析），以及 `web.archive.org` 上没有 `spatius.ai`、`spatialwalk.cn` 或 `spatialwalk.ai` 的任何快照。

### 不同来源之间的不一致

- **成立年份。** LinkedIn 公司页写 "Founded: 2025"；GitHub 组织 `spatialwalk` 创建于 2024-05-23，`spatialwalk.net` 注册于 2024-08-08，投资方文章把创业时点放在 Apple 发布 Vision Pro 之际（[LinkedIn](https://www.linkedin.com/company/spatius-ai)、[GitHub API](https://api.github.com/orgs/spatialwalk)、[Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)）。新加坡主体本身注册更晚，是 2025-07-21（[RecordOwl](https://recordowl.com/company/spatialwalk-pte-ltd)）。
- **总部。** 法律文件与 LinkedIn 写新加坡；2025-08 之后的所有招聘帖与中国主体信息写深圳；`spatialreal.ai` 页脚写美国加州圣何塞；2025-05 与 2025-06 的招聘帖写北京；招聘文案写 "中美双总部"（[服务条款](https://www.spatius.ai/terms-of-service/)、[V2EX 1153930](https://www.v2ex.com/t/1153930)、[spatialreal.ai](https://www.spatialreal.ai/)、[V2EX 1131126](https://www.v2ex.com/t/1131126)）。
- **两个同时在线的品牌，价目表不同。** `spatius.ai` 与 `spatialreal.ai` 卖同一套 SDK、同样的 $19/$299 档位，但赠送积分不同（Free 1,000 对 500；Starter 20,000 对 22,000），且两站互不提及（[定价页](https://www.spatius.ai/pricing/)、[spatialreal.ai](https://www.spatialreal.ai/)）。
- **每分钟单价的变化。** 投资方文章在 2025-10-31 写的是 "$0.003 / min"；2026-08-26 公开的 Scale 单价是 "$0.007 / min"（[Impa Ventures](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)、[定价页](https://www.spatius.ai/pricing/)）。
- **带宽数字。** 英文站 "100 kbps"，中文站 "10–20KB/s"，文档 "~10–15 KB/s"（[spatius.ai](https://www.spatius.ai/)、[spatialwalk.top](https://spatialwalk.top/)、[文档](https://docs.spatius.ai/concepts/how-it-works.md)）。
- **形象生成的输入。** 当前 API 接收单张静态照片；中文营销页仍写 "仅需 1 分钟真人视频素材，即可生成可驱动的超写实 3D 数字形象"（[文档 — Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md)、[spatialwalk.top](https://spatialwalk.top/)）。
- **平台支持进度。** 中文 FAQ 仍写 "我们目前全面支持 iOS，Web及Android SDK将在11月上线"，而 Web、Android 与 Flutter SDK 均已发布，文档中 iOS、Android、Web、Flutter 都标为支持（[spatialwalk.top](https://spatialwalk.top/)、[SDK 能力矩阵](https://docs.spatius.ai/reference/sdk-capabilities.md)）。
- **首席科学家的列名。** 中文团队页把 Yudong Guo 列为首席科学家；其本人的学术主页没有列出任何公司任职（[spatialwalk.top](https://spatialwalk.top/)、[yudongguo.github.io](https://yudongguo.github.io/)）。

### 其他

- **三个市场、三个品牌，时间线清晰。** `spatialwalk.net`（2024-08）承载中文 SpatialWalk 站点；`spatialreal.ai`（2025-11）承载美国主体下的英文 SpatialReal 站点；`spatius.ai`（2026-04）承载新加坡主体下的当前英文 Spatius 站点。npm 包顺序一致：`@spatialwalk/avatarkit`（2025-11 至 2026-04）而后 `@spatius/avatarkit`（2026-04 起），且旧 GitHub 组织的示例仓库至今仍链向 `docs.spatialreal.ai`（[npm](https://registry.npmjs.org/@spatialwalk/avatarkit)、[avatarkit-voice-agent-demo](https://github.com/spatialwalk/avatarkit-voice-agent-demo)）。
- **一次自述的方向转变。** 2025-05 与 2025-06 的招聘帖描述的是 "一家专注于 AI 和空间计算 的科技公司"，base 北京；2025-08 起同一账号描述的是 "实时互动 AI 数字形象技术"，base 深圳（[V2EX 1131126](https://www.v2ex.com/t/1131126)、[V2EX 1153930](https://www.v2ex.com/t/1153930)）。
- **公开页面明显是按 SEO 组织的。** 主 sitemap 的 210 个 URL 中有 188 个是博客文章，另有三份 sitemap 各 51 个 URL，分别是对比页、集成页与术语表；博客中包含点名竞品的对比页（[sitemap 索引](https://www.spatius.ai/sitemap-index.xml)、[Spatius 博客](https://www.spatius.ai/blog/)）。
- **两个站点对 AI 爬虫都是放行的。** `spatius.ai` 与 `spatialwalk.cn` 明确允许 GPTBot、ClaudeBot、PerplexityBot、Google-Extended、Applebot-Extended、Bytespider、CCBot 等（[robots.txt](https://www.spatius.ai/robots.txt)；读取于 2026-08-26）。
- **可观测到的采用量不大，但不是零。** 当前 Web SDK 近一个月 7,417 次 npm 下载、Discord 51 人、SDK 仓库 1–3 个 star，与 `spatialreal.ai` 上 "10M+ interactions" 的口径并列（[npm API](https://api.npmjs.org/downloads/point/last-month/@spatius/avatarkit)、[Discord invite API（Spatius）](https://discord.com/api/v9/invites/9HGhZfHZh9?with_counts=true)、[GitHub API](https://api.github.com/orgs/spatius-ai)）。
- **中国区域用的是另一个域名。** `cn-beijing` 控制台运行在 `console.cn-beijing.spatialwalk.top`，而 `us-west` 与 `ap-northeast` 的控制台在 `spatius.ai` 的子域下（[文档 — Regions](https://docs.spatius.ai/api-reference/regions.md)）。

---

## 资料来源

**官方**

- [spatius.ai](https://www.spatius.ai/) · [定价页](https://www.spatius.ai/pricing/) · [联系页](https://www.spatius.ai/contact/) · [博客](https://www.spatius.ai/blog/) · [robots.txt](https://www.spatius.ai/robots.txt) · [sitemap 索引](https://www.spatius.ai/sitemap-index.xml)
- [服务条款](https://www.spatius.ai/terms-of-service/)（生效于 2026-04-26）· [隐私政策](https://www.spatius.ai/privacy-policy/)（更新于 2026-04-22）
- 文档 —— [Welcome](https://docs.spatius.ai/getting-started.md) · [How It Works](https://docs.spatius.ai/concepts/how-it-works.md) · [Avatar](https://docs.spatius.ai/concepts/avatar.md) · [Client Lifecycle](https://docs.spatius.ai/concepts/lifecycle.md) · [Integrations](https://docs.spatius.ai/integrations/overview.md) · [SDK 能力矩阵](https://docs.spatius.ai/reference/sdk-capabilities.md) · [Regions](https://docs.spatius.ai/api-reference/regions.md) · [Create an Avatar](https://docs.spatius.ai/api-reference/avatars/create-an-avatar.md) · [FAQ](https://docs.spatius.ai/resources/faq.md) · [llms.txt](https://docs.spatius.ai/llms.txt)
- 中文站点（语言：中文）—— [spatialwalk.cn](https://www.spatialwalk.cn/) · [spatialwalk.top](https://spatialwalk.top/) · [合规接入指引](https://www.spatialwalk.cn/compliance-guide)（更新于 2026-01-06）
- 并行英文站点 —— [spatialreal.ai](https://www.spatialreal.ai/)
- 客户故事 —— [SayMei](https://www.spatius.ai/blog/saymei-ai-mandarin-tutor-spatius/)（2026-08-11）· [产品更新](https://www.spatius.ai/blog/spatius-product-update-avatar-apis-faster-audio-production-ready-sdks/)（2026-08-22）
- 代码与软件包 —— [GitHub `spatius-ai`](https://api.github.com/orgs/spatius-ai) · [GitHub `spatialwalk`](https://api.github.com/orgs/spatialwalk) · [avatarkit-voice-agent-demo](https://github.com/spatialwalk/avatarkit-voice-agent-demo) · [iOS SDK releases](https://github.com/spatius-ai/avatarkit-ios-release/releases) · [npm `@spatialwalk/avatarkit`](https://registry.npmjs.org/@spatialwalk/avatarkit) · [npm 搜索 "spatius"](https://registry.npmjs.org/-/v1/search?text=spatius&size=20) · [npm 下载量](https://api.npmjs.org/downloads/point/last-month/@spatius/avatarkit) · [pub.dev `avatar_kit`](https://pub.dev/packages/avatar_kit) · [Maven Central `ai.spatialwalk:avatarkit`](https://mvnrepository.com/artifact/ai.spatialwalk/avatarkit)
- 社区 —— [Discord invite API（Spatius）](https://discord.com/api/v9/invites/9HGhZfHZh9?with_counts=true) · [Discord invite API（SpatialReal）](https://discord.com/api/v9/invites/dRSUTdPCjm?with_counts=true) · [LinkedIn 公司页](https://www.linkedin.com/company/spatius-ai)

**投资方与登记信息**

- [Impa Ventures —— "IMPA Family | Our Investment in Spatial Walk"](https://impa.ventures/writing/impa-family-our-investment-in-spatial-walk)（2025-10-31）· [Impa Ventures](https://impa.ventures/)
- [RecordOwl —— SPATIALWALK PTE. LTD.（ACRA 数据镜像）](https://recordowl.com/company/spatialwalk-pte-ltd)

**招聘帖**（语言：中文，均来自 `hr@spatialwalk.net`）

- [13 篇帖子的索引](https://www.sov2ex.com/api/search?q=spatialwalk&size=20) · [1131126（2025-05-12）](https://www.v2ex.com/t/1131126) · [1132398（2025-05-17）](https://www.v2ex.com/t/1132398) · [1136977（2025-06-06）](https://www.v2ex.com/t/1136977) · [1153830（2025-08-20）](https://www.v2ex.com/t/1153830) · [1153930（2025-08-21）](https://www.v2ex.com/t/1153930) · [1160643（2025-09-19）](https://www.v2ex.com/t/1160643) · [1161367（2025-09-23）](https://www.v2ex.com/t/1161367) · [1173996（2025-11-20）](https://www.v2ex.com/t/1173996) · [1175749（2025-11-28）](https://www.v2ex.com/t/1175749) · [1189876（2026-02-01）](https://www.v2ex.com/t/1189876)

**第三方资料与学术来源**

- [yudongguo.github.io](https://yudongguo.github.io/) · [SadTalker 项目页](https://sadtalker.github.io/) · [GitHub — OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker)
- [iTunes 搜索 API —— 美国区未见第一方应用](https://itunes.apple.com/search?term=spatius&entity=software&country=us&limit=5)
- [百度百科 —— 空间漫步传媒科技（深圳）有限责任公司（无关的名称撞车，语言：中文）](https://baike.baidu.com/item/%E7%A9%BA%E9%97%B4%E6%BC%AB%E6%AD%A5%E4%BC%A0%E5%AA%92%E7%A7%91%E6%8A%80%EF%BC%88%E6%B7%B1%E5%9C%B3%EF%BC%89%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/24226245)
