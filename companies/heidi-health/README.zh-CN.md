# Heidi

[English](README.md) | **简体中文**

> 基于公开资料整理的调研笔记。最后更新：2026-08-31。
> 每一个数字都标注了出处链接和对应日期。据此做决定前请回查一手资料。
> 本文与英文版同步至：2026-08-31。英文版为原始版本。

## 摘要

Heidi（`heidihealth.com`）卖的是面向临床医生的环境式（ambient）AI 病历助手，并正在把它扩展成公司所称的 "AI Care Partner"：**Scribe**（病历文书）、**Evidence**（带引用的临床问答）、**Dictate**（桌面端全系统语音转文字）与 **Remote**（21 克可穿戴麦克风）。运营主体是 **HEIDI HEALTH TRADING PTY LTD**，ABN 84 649 783 871，位于墨尔本（[ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871)，记录提取于 2026-08-31；[Heidi Scribe Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use)）。该业务此前的品牌是 **Oscer**（[TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)；2023-10-25）。

- 最近一轮：**6,500 万美元 B 轮**，2025-10-05 公布，由 **Point72 Private Investments** 领投，投后估值 **4.65 亿美元**，累计融资 **9,660 万美元**（[Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)；[TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/)）。2026-08-31 检索的资料中未发现更晚的轮次 —— 见 `融资`。
- 公司自述规模（2026-08-31 口径）：每周 **250 万次问诊**、**110 种语言**、**190 个国家**、**200+ 专科**、累计融资 **9,660 万美元**；媒体页写 **400+ 员工**，招聘页写 **500+**（[Media Room](https://www.heidihealth.com/en-au/about-us/media)、[Careers](https://www.heidihealth.com/en-au/careers)）—— 两个人数互相矛盾，见 `备注`。
- 2026-08-31 当天，公司的 Ashby 招聘板上有 **85 个在招岗位** —— 工程 24 个、GTM 35 个 —— 集中在墨尔本（27）、伦敦（16）、纽约（9）、旧金山（7）与悉尼（6）（[Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)）。
- 招聘启事描述的工程侧：**Python** 服务配 **MongoDB 与 Redis**，**React/Next.js** 前端，**Tauri + Rust** 跨平台桌面应用，**Kubernetes + Terraform** 跑在 **AWS、GCP 与 Azure** 上，以及为没有 API 的 EHR 自研的确定性 **RPA 引擎** —— 见 `工程`。
- 已公布的企业级部署包括 **Beth Israel Lahey Health**（"6,000+ providers across 14 hospitals and 175 primary care practices"）与英国 NHS 的 **Modality Partnership**（"360+ GPs … 53 sites"）（[Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise)；访问于 2026-08-31）。

---

## 基本情况

| 项目 | 内容 | 出处 |
|---|---|---|
| 当前公开品牌 | Heidi —— "The AI Care Partner for clinicians" | [heidihealth.com/en-au](https://www.heidihealth.com/en-au)；访问于 2026-08-31 |
| 澳大利亚法律主体 | HEIDI HEALTH TRADING PTY LTD；ABN 84 649 783 871；ACN 649 783 871；澳大利亚私人公司；ABN 与 GST 自 2021-04-28 起有效；主要营业地 VIC 3000 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871)；记录提取于 2026-08-31 |
| 注册商号 | "HEIDI HEALTH"，自 2022-05-17 起注册 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871) |
| 产品条款中的签约主体 | "Heidi Health Trading Pty Ltd." | [Heidi Scribe Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use)；访问于 2026-08-31 |
| 隐私政策中的地址 | Level 30, 360 Elizabeth Street, Melbourne VIC 3000 | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| 其他集团主体 | Heidi Health Ltd（英国）；Heidi Health Canada Inc（加拿大安大略省）；Heidi Health Corp（美国特拉华州）；Oscer Enterprises Pty Limited（澳大利亚） | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| 前身主体 | OSCER ENTERPRISES PTY LTD；ABN 57 620 824 900；ACN 620 824 900；ABN 自 2017-08-01 起有效；商号 "Oscer" 自 2021-07-27 起注册；VIC 3000 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=57620824900)；记录提取于 2026-08-31 |
| 创始人 | Dr. Thomas Kelly（联合创始人兼 CEO）、Yu Liu（联合创始人兼 CTO）、Waleed Mussa（联合创始人兼 CFO） | [Careers](https://www.heidihealth.com/en-au/careers)、[Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| 成立年份 | TechCrunch 写 2021 年；另有二手来源写 2019 年；前身主体的 ABN 可追到 2017 年 —— 见 `不同来源之间的不一致` | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)、[ABN Lookup](https://abr.business.gov.au/ABN/View?abn=57620824900) |
| 人数 | "400+ employees around the world"（媒体页）；"500+ Heidis"（招聘页） | [Media Room](https://www.heidihealth.com/en-au/about-us/media)、[Careers](https://www.heidihealth.com/en-au/careers)；均访问于 2026-08-31 |
| 办公室 | "8 Offices across AU, US, UK, Canada & Singapore" —— 墨尔本、悉尼、布里斯班、纽约、旧金山、伦敦、多伦多、新加坡 | [Careers](https://www.heidihealth.com/en-au/careers)；访问于 2026-08-31 |
| 累计融资 | "USD 96.6m raised to date" | [Media Room](https://www.heidihealth.com/en-au/about-us/media)；访问于 2026-08-31 |
| 公司自己列出的投资方 | Point72 Private Investments、Blackbird、Headline、Latitude（Phoenix Court 旗下成长基金）、Possible Ventures、Archangel | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| 每周量 | "2.5 million patient sessions supported each week"；澳洲首页的实时计数器显示本周 2,740,338 次问诊 | [Media Room](https://www.heidihealth.com/en-au/about-us/media)、[heidihealth.com/en-au](https://www.heidihealth.com/en-au)；读取于 2026-08-31 |
| 合规声明 | "NHS, HIPAA, GDPR, and Australian Privacy Principles … SOC2 and ISO27001" | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Trust Center | 托管在 Vanta 上，域名 `trust.heidihealth.com` | [trust.heidihealth.com](https://trust.heidihealth.com/)；读取于 2026-08-31 |
| 招聘系统 | Ashby，board slug 为 `heidihealth.com.au`；2026-08-31 有 85 个在线岗位 | [Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| 站点语言/地区 | 22 个 locale 路径：`en-au`、`en-us`、`en-gb`、`en-ca`、`en-nz`、`en-ie`、`en-sg`、`en-hk`、`en-my`、`en-za`、`de-de`、`de-ch`、`de-be`、`de-lu`、`fr-fr`、`fr-ca`、`fr-ch`、`fr-be`、`fr-lu`、`es-es`、`es-mx`、`es-ar`、`it-it`、`ja-jp` | [heidihealth.com/en-au](https://www.heidihealth.com/en-au) 页脚；读取于 2026-08-31 |
| 公开社交账号 | X `@tryheidi`（页面 `twitter:site` meta 标签写的是 `@heidi_health`）、LinkedIn `heidihealth`、Instagram `tryheidi`、Facebook `tryheidi`、YouTube | [heidihealth.com/en-au](https://www.heidihealth.com/en-au)；读取于 2026-08-31 |

### 品牌与法律实体

| 名称 | 类型 | 司法辖区 / 期间 | 来源中写明的关系 | 出处 |
|---|---|---|---|---|
| Heidi | 当前公开品牌 | 全球；澳洲商号自 2022-05-17 起注册 | 所有产品界面使用的品牌 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871)、[heidihealth.com/en-au](https://www.heidihealth.com/en-au) |
| HEIDI HEALTH TRADING PTY LTD | 法律主体 | 澳大利亚（维州），ABN 自 2021-04-28 起有效 | Scribe 服务条款中的签约方，隐私政策中的数据控制者 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=84649783871)、[Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use) |
| OSCER ENTERPRISES PTY LTD | 法律主体 | 澳大利亚（维州），ABN 自 2017-08-01 起有效 | 在隐私政策中被列为 Heidi 集团主体之一；未公布持股关系 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=57620824900)、[Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Oscer | 旧品牌 | 澳大利亚；商号于 2021-07-27 注册 | "Formerly called Oscer" —— 同一业务，同为 Kelly、Mussa、Liu 三人 | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)、[Blackbird 组合页](https://www.blackbird.vc/portfolio/heidi-health) |
| Heidi Health Ltd | 关联主体 | 英国 | 隐私政策中列为集团主体 | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Heidi Health Canada Inc | 关联主体 | 加拿大安大略省 | 隐私政策中列为集团主体 | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| Heidi Health Corp | 关联主体 | 美国特拉华州 | 隐私政策中列为集团主体 | [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) |
| AutoMedica | 被收购公司 | 英国；2026-02-24 公布 | "AutoMedica's evidence-led AI framework and regulatory relationships will underpin Heidi's Evidence capabilities"；交易条款未披露 | [Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence) |

Blackbird 的组合页记录该机构于 **2021 年** 在种子轮投资，当时公司还叫 Oscer，做的是 "changing the way students learn clinical reasoning with innovative tools like AI virtual patients"（[Blackbird](https://www.blackbird.vc/portfolio/heidi-health)；访问于 2026-08-31）。所查资料中没有任何来源说明澳、英、加、美四个主体之间的持股关系。

---

## 产品

### 产品构成与功能板块

- **Scribe** —— 环境式病历文书产品："Heidi captures the encounter as it happens and writes notes that sound like you, not a generic template"，包含诊前准备、"in 110+ languages" 的转写、生成转诊信与患者宣教材料、一键回写 EHR、自动套用编码与任务（[Scribe](https://www.heidihealth.com/en-au/scribe)；访问于 2026-08-31）。
- **Evidence** —— 带引用的临床问答："Open the citation behind any answer and read the source yourself"，内置评分量表 "show their working"，可按个人与团队设定优先来源，CPD 自动记录（[Evidence](https://www.heidihealth.com/en-au/evidence)；访问于 2026-08-31）。2026-02-24 上线，具名内容合作方为 **HealthPathways、EMGuidance、MIMS、Vidal、NICE、BMJ Group**（[Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence)）。
- **Dictate** —— 桌面端按住说话的听写功能，可直接输入到 "your EHR, a referral letter, Outlook, any application on your computer"，"clinical vocabulary built in more than 90 languages"（[Dictate](https://www.heidihealth.com/en-au/product/dictate)；访问于 2026-08-31）。桌面应用当时版本为 **2.9.0，发布于 2026-08-31**，覆盖 Windows（.EXE/.MSI）与 macOS（Apple Silicon 与 Intel）。
- **Remote** —— 硬件："a 21-gram wearable mic, fully offline, with on-device encryption"，夹式佩戴，在线离线均可工作，通过 "an encrypted wireless connection" 与配对设备连接，音频 "encrypted at rest on Heidi Remote and … automatically deleted once synchronised"（[Scribe](https://www.heidihealth.com/en-au/scribe)、[Hardware](https://www.heidihealth.com/en-au/hardware)；访问于 2026-08-31）。2026 年 3 月上市（[Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/)；2026-03-24）。
- **Comms** —— "an AI partner for healthcare teams to coordinate patient communications across calls, bookings, reminders and follow-ups"，与 Evidence 一同于 2026 年 2 月公布（[Heidi Progress Notes — "Evidence, Comms, and more customisations"](https://www.heidihealth.com/en-au/changelog)；2026-02-25）。站点导航中没有独立的 Comms 产品页 —— `/en-us/comms` 返回的是兜底页面（2026-08-31 核查）。
- **Templates** —— 公开的模板库与 "Template Community"（[Templates](https://www.heidihealth.com/en-au/templates)）。
- **集成** —— 一则招聘启事这样描述集成面："SMART on FHIR launches inside the chart, structured write-back into Epic, Cerner, Athena, MEDITECH Expanse, Veradigm, Best Practice. HL7 ADT feeds for patient demographics"，另有正在重建的 "Integration Marketplace"（[Technical Program Manager, Integrations](https://jobs.ashbyhq.com/heidihealth.com.au/3ec2c152-3983-4471-834a-60c8e1f6c993)；发布于 2026-08-04）。

公开的客户端最低要求：Windows 10 及以上 / macOS 13.1 及以上、最新 Chromium 内核浏览器（Chrome、Edge）、Android 8.0、iOS 17.0，带宽最低 10 Mbps、推荐 20 Mbps（[System Requirements](https://www.heidihealth.com/en-au/system-requirements)；访问于 2026-08-31）。

### 商业化

公开四档：**Free**、**Clinician**、**Practice**，以及 "Talk to us" 的企业版，按 "per user / month" 计费，可选按月或按年，付费个人与团队方案提供 14 天试用。价格按 locale 在客户端渲染，2026-08-31 服务端返回的 HTML 中不含价格；功能对比表则完整公开（[Pricing](https://www.heidihealth.com/en-au/pricing)；读取于 2026-08-31）。

公开的功能分档：Free 含 "Unlimited transcription"、标准模板、任务管理，以及受限的 Ask Heidi、高级模板与患者/会话关联。Clinician 增加文档与会话共享、编码、会话状态、免费助理账号、优先与高级证据源、个人证据库、以及在问诊中直接调用 Evidence。Practice 增加团队模板共享、1:1 模板配置、组织级证据库、集中计费、优先支持、团队管理、引导式上线、专属客户成功与 SSO。"EHR integration add-on" 作为付费加购项列在 Practice 与企业版列；"Service availability" 与 "Custom terms & hosting" 仅企业版提供（[Pricing](https://www.heidihealth.com/en-au/pricing)）。

### 公开规模变化

| 日期 | 原文口径 | 出处 |
|---|---|---|
| 2023-10-25 | 澳大利亚 "more than 100 general practitioners in about 30 clinics" | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/) |
| 2024-02 | Scribe 上线 | [Heidi — A 轮追加](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) |
| 2025-03-06 | 自上线累计 "over 20 million patient interactions globally"；截至 2025 年 3 月 "over 1 million consults every week"；覆盖五个国家 | [Heidi — A 轮追加](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) |
| 2025-10-05 | 18 个月内 "73 million patient visits" 与 "18 million hours"；"over two million patient visits each week"；"110 languages"；"116 countries"；"200+ specialties" | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b) |
| 2026-02-24 | "over 100 million clinical interactions supported globally"；"2.4 million consults per week"；"110 languages from 190 countries" | [Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence) |
| 2026-03-24 | 累计 "118 million clinical sessions"；每周 "2.5 million patient interactions"；英国："1 in 2 GPs"、每月 "1.5 million monthly patient consultations" | [Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/) |
| 2026-03-10 | "more than 2.7 million visits a week" | [R1 RCM 新闻室](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations) |
| 2026-08-31 | "2.5 million patient sessions supported each week"、"190 countries"、"400+ employees"；招聘页："47M hours saved since launch"、"500+"；企业页："62.9M hours saved by clinicians since launch"、"61.7% Activation Rate (Enterprise)"、"200+ Specialties Supported" | [Media Room](https://www.heidihealth.com/en-au/about-us/media)、[Careers](https://www.heidihealth.com/en-au/careers)、[Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) |

### 已公布的客户与合作方

| 客户 / 合作方 | 公开口径 | 日期 | 出处 |
|---|---|---|---|
| Beth Israel Lahey Health（美国） | "89% note satisfaction, 74% less after-hours admin. 6,000+ providers across 14 hospitals and 175 primary care practices" | 访问于 2026-08-31 | [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) |
| Modality Partnership（英国 NHS） | "360+ GPs, largest ambient AI rollout in UK primary care … 53 sites, benefiting almost half a million patients" | 访问于 2026-08-31 | [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) |
| ForHealth（澳）、Tamaki Health（新西兰） | 分别被称为 "the largest multi-disciplinary healthcare network in Australia" 与 "the largest primary healthcare provider in New Zealand" | 2025-03-06 | [Heidi — A 轮追加](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) |
| OneCare Vermont（美国） | 合作 "to reduce administrative burden for primary care practices across Vermont" | 2025-09-25 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| Vim（美国） | "Partner to Accelerate Innovation at the Point of Care" | 2025-10-15 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| R1 RCM（美国） | 战略合作：Heidi 用户可在诊疗现场看到 "payer policy information, prior authorization rules and insurance eligibility information"；病历 "optimized to ensure accurate coding and billing" | 2026-03-10 | [R1 RCM 新闻室](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations) |
| The Royal Children's Hospital（澳） | 部署 "so paediatricians can focus on patients, not paperwork" | 2026-06-03 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| QHR Technologies / Accuro EMR（加拿大） | "AI documentation into Accuro EMR" 的集成 | 2026-06-16 | [Media Room](https://www.heidihealth.com/en-au/about-us/media) |
| 安大略省五个试点（加拿大） | "333 active clinicians"、"111,770 patient visits"、每个试点三个月、"13 minutes saved per visit"、"25,098+ clinical hours" 折合 "$2.51 million"；Guelph Wellington OHT、Mississauga Health PCN、Kawartha Lakes OHT、Ottawa Institute of CBT、South Georgian Bay Provider Care Network | 2026-07-22 | [Newswire 新闻稿](https://www.newswire.ca/news-releases/more-patients-less-paperwork-heidi-s-ai-scribe-returns-an-estimated-2-51m-in-clinical-time-893435988.html)、[Canadian Healthcare Technology](https://www.canhealth.com/2026/07/22/heidi-ai-scribes-save-13-minutes-per-visit/) |
| 首页展示的 logo | Bupa、University of Queensland、The Ohio State University、Beth Israel Lahey Health、Swiss Medical Network、Eucalyptus、Greencross Vets、QLD Children's Hospital、Sue Ryder、Tamaki Health | 访问于 2026-08-31 | [heidihealth.com](https://www.heidihealth.com/) |

企业页 FAQ 中有两条采纳率口径："60-80% adoption within the first month, far exceeding just 20-40% average seen with other AI scribes"，以及 "My Emergency Doctor … achieving 77% adoption within just 3 weeks"（[Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise)；访问于 2026-08-31）。两条都是公司自己的表述。

### 公司自述的计划

- B 轮资金用途："expand headcount, office locations, and local support in USA, UK, and Canada"，以及 "build adoption in France, Spain, Germany, Ireland, South Africa, Singapore, and Hong Kong"（[Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)；2025-10-05）。
- 反复出现在招聘启事与新闻稿中的使命表述："halve the time it takes to deliver world-class care"（2026-06 的启事）与 "double the world's healthcare capacity and strengthen the human connection at its heart"（2026-08 的启事）（[Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837)、[Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)）。
- 伦敦设有做 0→1 新产品的 "New Bets" 小组："Scribe already powers millions of patient visits a week, and Evidence and Remote are scaling behind it. Your job … is to build what comes next"（[Backend Software Engineer - New Bets](https://jobs.ashbyhq.com/heidihealth.com.au/68074198-b723-4db9-af97-5f33392593f4)；发布于 2026-08-21）。

---

## 创始人

公司自己的页面具名三位联合创始人（[Careers](https://www.heidihealth.com/en-au/careers)、[Media Room](https://www.heidihealth.com/en-au/about-us/media)；访问于 2026-08-31）：

| 姓名 | 职务 | 来源中的履历事实 |
|---|---|---|
| Dr. Thomas Kelly | 联合创始人兼 CEO | 公司自己的新闻稿称其为 "CEO and co-founder of Heidi, and former vascular surgical resident"（[Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)；2025-03-06）。TechCrunch 称其为血管外科医生，2021 年创办公司（[TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)）；Blackbird 组合页把动机描述为他做住院医时见到的 "incorrect, delayed or missed diagnoses"（[Blackbird](https://www.blackbird.vc/portfolio/heidi-health)）。 |
| Yu Liu | 联合创始人兼 CTO | 公司页面与 TechCrunch 2023 年报道中均列为联合创始人。 |
| Waleed Mussa | 联合创始人兼 CFO | 公司页面与 TechCrunch 2023 年报道中均列为联合创始人。 |

Kelly 本人对创业动机的表述："That's why I founded Heidi – to free doctors from non-clinical work so they can focus on their patients and enjoy fulfilling careers in medicine"（[Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)；2025-03-06）。

### 主要管理层

公司官网除三位创始人外没有管理层页面 —— `/about-us/people` 返回的内容与 `/careers` 相同（2026-08-31 核查）。其他高管出现在公司自己的新闻稿与招聘启事中：

| 姓名 | 职务 | 来源中写明的过往职务 | 出处 |
|---|---|---|---|
| Paul Williamson | Chief Revenue Officer | 前 Plaid Head of Revenue | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)；2025-10-05 |
| Dr. Simon Kos | Chief Medical Officer | 前微软 Chief Medical Officer | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)；2025-10-05 |
| Jessie Young | President, North America | 未写明 | [Head of Engineering, North America](https://jobs.ashbyhq.com/heidihealth.com.au/adfea4ea-f501-4513-9b59-45b12774ee1d)；发布于 2026-06-16 |

招聘板显示的在招职能分布：GTM（35）、工程（24）、产品（11）、市场（6）、法务/监管与合规（2）、People（1）、客户体验（1），另有 5 个 "Expression of Interest" 岗位（[Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)；读取于 2026-08-31）。启事中出现的工程子团队：Engineering、Engineering R&D、Engineering Service Delivery、Clinical AI R&D、Data、IT。

---

## 融资

| 日期 | 轮次 | 金额 | 投资方 | 累计 | 出处 |
|---|---|---|---|---|---|
| 2021 年（仅到年） | 种子轮 | 500 万澳元 | Blackbird（领投） | — | [Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/)、[Blackbird](https://www.blackbird.vc/portfolio/heidi-health) |
| 2023-10-25 | A 轮 | 1,000 万澳元（约 640 万美元） | Blackbird（领投）、Hostplus、Vesta、Wormhole Capital、Archangel Ventures、Possible Ventures、Daniel Ventures | 1,500 万澳元 | [TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/) |
| 2025-03-06 | "Series A follow-on" / "top-up" | 1,660 万美元（报道折合 2,680 万澳元） | Headline（领投）、Local Globe、Anthology（Menlo Ventures 与 Anthropic）、Blackbird、HESTA、Possible Ventures、Archangel Ventures | 3,680 万澳元 | [Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)、[Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/) |
| 2025-10-05 | B 轮 | 6,500 万美元（报道折合 9,800 万澳元），估值 4.65 亿美元（7.04 亿澳元） | Point72 Private Investments（领投）、Blackbird、Headline、Latitude（Phoenix Court 旗下成长基金） | 9,660 万美元 | [Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)、[TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/)、[SmartCompany](https://www.smartcompany.com.au/startupsmart/heidi-health-98-million-raise-valuation-704-million/) |

表格之外的事实：

- 公司自己把 2025 年 3 月这一轮称为 "Series A follow-on investment"；Startup Daily 称之为对 2023 年 10 月 A 轮的 "top-up"（[Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)、[Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/)）。
- **Anthology** 在 Heidi 自己的新闻稿中被描述为 "Menlo Ventures and Anthropic" 的载体，参与了 2025 年 3 月这一轮；它没有出现在公司今天在 Media Room 上列出的投资方名单里（[Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)、[Media Room](https://www.heidihealth.com/en-au/about-us/media)）。
- 澳大利亚养老金机构 **HESTA** 与 **Hostplus** 分别出现在 2025 年与 2023 年的轮次中，也不在当前投资方名单里（[TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)、[Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)）。
- B 轮公布时同时宣布的是两位高管入职（Williamson、Kos），而不是产品发布（[Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)）。
- **AutoMedica** 收购（2026-02-24 公布）是查到的唯一一笔收购，条款未披露（[Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence)）。
- 2026-08-31 检索的资料中，2025 年 10 月 B 轮之后没有新轮次。2026 年 8 月发布的招聘启事仍写 "Backed by nearly $100 million in funding"（[Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48)）。

---

## 工程

### 技术栈与平台

**由可观测的公开资产确认**（响应头与页面读取于 2026-08-31）：

- 市场站点、状态页（`status.heidihealth.com`）与 Web 应用（`scribe.heidihealth.com`）均为 **Next.js on Vercel**（`server: Vercel`、`x-powered-by: Next.js`）。
- **Sanity** 作为 CMS（市场页的资源域名为 `cdn.sanity.io`）。
- **Intercom** 承载支持与帮助中心（`support.heidihealth.com`，前置 Cloudflare）；**Vanta** 承载 Trust Center；**Ashby** 承载招聘；站点上有 **Google Tag Manager**。
- **跨平台桌面应用**：Windows（.EXE 与 .MSI）与 macOS（Apple Silicon 与 Intel 两个构建），版本 2.9.0，发布于 2026-08-31；另有 Android 与 iOS 客户端（[Dictate](https://www.heidihealth.com/en-au/product/dictate)、[System Requirements](https://www.heidihealth.com/en-au/system-requirements)）。

**在当前招聘启事中被描述为团队正在构建与运行的东西**（属于招聘证据，不等于独立确认）：

- **桌面端**："Heidi's cross-platform desktop applications using Tauri, Rust, and Next.js, shipping production-grade software on macOS and Windows (Linux a plus)"，以及 "high-performance Rust components powering real-time audio capture, transcription pipelines, local state management"（[Senior Software Engineer - Desktop App](https://jobs.ashbyhq.com/heidihealth.com.au/738c99ed-0a85-467f-821c-1beae5565148)；2026-08-26）。
- **后端**："high-performance backend systems using Python"；"Solid experience with MongoDB and Redis for data management"；"message queue systems for real-time data processing"（[Senior Backend Engineer - UK](https://jobs.ashbyhq.com/heidihealth.com.au/76723d60-69ac-4368-a97d-4ce125d3c822)；2026-06-05）。更新的启事把 "Python services" 与 "React/TypeScript front ends" 并列（[Backend Software Engineer - New Bets](https://jobs.ashbyhq.com/heidihealth.com.au/68074198-b723-4db9-af97-5f33392593f4)；2026-08-21）。
- **前端**："Advanced proficiency with React and Next.js (SSR/SSG/ISR…)"、monorepo 工具链（"Turborepo, Nx, Bazel"）、设计系统与 Storybook、微前端与 module federation、用 "Playwright, Cucumber" 做 TDD/BDD（[Staff Frontend Solution Architect](https://jobs.ashbyhq.com/heidihealth.com.au/c6b7c2b6-5b9b-47b4-8e65-ba866225c95f)；2026-08-05）。
- **三家云，按岗位分**：GCP（"Compute Engine, managed instance groups, GKE… VPCs, peering, Private Service Connect, Cloud DNS"）、Azure（"preferably Azure"）、AWS（"Strong experience operating cloud infrastructure at scale (AWS preferred)"）（[Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48)、[Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837)、[Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)）。
- **平台**：Kubernetes 与容器、Terraform 与 Helm、Docker、GitOps 与 monorepo 构建系统、canary/蓝绿发布，加分项为 "MongoDB Atlas, Redis, or Postgres cloud deployments"（[Senior Software Engineer - Developer Experience](https://jobs.ashbyhq.com/heidihealth.com.au/99ef4d45-fcaf-4d53-b2db-9acd8a740be3)；2026-05-07）。
- **可观测性**：Datadog、Prometheus、Grafana、ELK；SLO 与 error budget（[Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)）。
- **模型**："our ASR, note generation, Evidence, and Dictate models" 由内部 model team 拥有；企业侧的目标写作 "better economics than relying solely on closed-source models such as Claude, Gemini, and OpenAI"，路径是微调 "open-weight language models" 并做 "cloud or on-prem deployment"（[Senior LLMOps Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/4f287875-c13f-483c-af50-d48f7d637d73)、[Senior AI Models Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/f2a33fd0-e4bc-4e0b-84e3-c136a32af0ab)）。TechCrunch 报道其采用 "model-agnostic approach, building on proprietary models and external systems like Google Gemini"（[TechCrunch](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/)；2025-10-05）。
- **本地化**：Crowdin 或 Smartling 接入发布流水线；XLIFF/JSON/XML 内容格式；"AI-assisted translation pipelines … with human-in-the-loop review"（[Senior Localisation Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/ea5b66c6-c1d5-48e5-b985-129fc01d02cc)；2026-08-19）。
- **AI 辅助开发是明确要求**："Prototype with AI-assisted tools like Claude Code and Cursor to ship in days, then harden what works into production-grade code"；"You build with AI tools (Cursor, Claude Code, whatever ships faster) and can show what you've made with them"（[Senior Software Engineer - RPA](https://jobs.ashbyhq.com/heidihealth.com.au/797ab212-3cc6-4dd0-8646-908241fc8f34)、[Backend Software Engineer - New Bets](https://jobs.ashbyhq.com/heidihealth.com.au/68074198-b723-4db9-af97-5f33392593f4)）。

**只作为候选人要求或加分项出现、未被确认在生产中使用**：Ansible、GitHub Advanced Security、Snyk、Trivy、service mesh、Karpenter、Linkerd、dbt、Databricks、Looker、Tableau、Omni、Mixpanel、Amplitude、Statsig、C#、FlaUI、Selenium。

### 系统

- **环境式转写与病历生成** —— Web、桌面与移动端的实时音频采集、转写与结构化病历生成（[Scribe](https://www.heidihealth.com/en-au/scribe)）。
- **面向无 API 的 EHR 的自研 RPA 引擎** —— "Most EHRs don't offer us an API… we build our own automation engine that works the EHR the way a person would: reading the interface, mapping the fields and pushing structured data into the record."。启事明确写了不用第三方平台的判断："We looked hard at the vendor RPA platforms and decided against building on someone else's engine as they were either too slow, too fragile for patient data, and we weren't comfortable that they could guarantee determinism… AI helps us set automations up fast; deterministic code is what runs in production."。列出的组件包括 "UI-automation flows (accessibility-tree mapping, templated field entry, structured write-back)"、患者匹配与校验逻辑、工作队列、重试与异常处理（[Senior Software Engineer - RPA](https://jobs.ashbyhq.com/heidihealth.com.au/797ab212-3cc6-4dd0-8646-908241fc8f34)；2026-08-19）。
- **集成平台** —— 覆盖 Scribe、Comms 与 Evidence 的共用集成框架，以及面向客户的 Integration Marketplace；SMART on FHIR、结构化 EHR 回写、HL7 ADT 数据流、基于预约数据的诊前准备（[Technical Program Manager, Integrations](https://jobs.ashbyhq.com/heidihealth.com.au/3ec2c152-3983-4471-834a-60c8e1f6c993)；2026-08-04）。
- **模型平台与 LLMOps** —— 部署健康看板、"complete session-to-model lineage"、跨多步 LLM 流水线的分布式追踪、从 Intercom 工单与 CSAT 反哺训练数据的闭环，以及 "per-model P&L… revenue against inference cost for every model deployment"（[Senior LLMOps Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/4f287875-c13f-483c-af50-d48f7d637d73)；2026-08-10）。
- **Platform/SRE** —— 一支 "owns production" 的核心团队：Kubernetes 集群、云基础设施、on-call、事故响应、SLO 与容量规划（[Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)；2026-08-04）。
- **开发者平台** —— 全公司通用的构建系统、CI/CD 流水线、Docker 镜像、IDE 插件与 CLI 工具、环境脚手架、密钥管理与自动化开通（[Senior Software Engineer - Developer Experience](https://jobs.ashbyhq.com/heidihealth.com.au/99ef4d45-fcaf-4d53-b2db-9acd8a740be3)；2026-05-07）。
- **Forward-deployed 工程** —— 一条具名的交付模式："EMR integrations, SSO, SCIM provisioning, data pipelines, and security configuration"，工程师驻场（[Forward Deployed Engineer - UK](https://jobs.ashbyhq.com/heidihealth.com.au/02ad14b7-a9bb-45e3-a90f-631179f86d8d)；2026-06-05）。
- **本地化平台** —— 支撑 110 种语言在 Web 与移动端交付的流水线与工具（[Senior Localisation Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/ea5b66c6-c1d5-48e5-b985-129fc01d02cc)）。
- **设计控制与质量体系** —— 一个坐在工程团队里、但汇报给 Legal & Regulatory Affairs 的岗位，负责在敏捷环境中落地 "IEC 62304 (software lifecycle), ISO 14971 (risk management), and ISO 13485 (quality management systems)"，并 "Support external ISO 13485 and Notified Body audits"（[Design Quality Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/31e03395-c3a1-46c3-955c-ed9f50c2e8d7)；2026-08-12）。

### 招聘所需技术背景

**必需项**，按岗位族（[Ashby 招聘板](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)；读取于 2026-08-31）：

- SRE 与平台："7+ years in SRE, DevOps, platform, or operations-heavy engineering roles, including experience formally leading or managing a team"；on-call 与线上排障；亲自定义并承担 SLO、error budget 与容量规划，"not just familiarity with the concepts"。GCP 平台岗要求 "3–7+ years in cloud or platform engineering" 且有 GCP 生产经验。
- 后端："5+ years of backend development experience"，含安全与版本管理的 API 设计、第三方系统集成、数据建模。
- 桌面端："5+ years"，系统级编程（"Rust preferred; C++ or Go acceptable"），桌面应用打包与更新。
- 前端："6+ years"，在高增长 SaaS 中跨多团队扩展前端架构。
- LLMOps："the last 2–3 years hands-on in an LLMOps role, building the observability, tracing, evaluation, and feedback systems around production LLMs and owning them through real incidents"，并明确写明这类经验 "most likely in the US or China, where LLMOps practice runs deepest"。
- RPA：UI 自动化生产经验（"Playwright, accessibility-tree frameworks like FlaUI, or an RPA platform you've since outgrown"），Python 为主语言，"deterministic-systems instincts: queues, retries, idempotency and exception handling"。
- Forward deployed："4+ years in a forward deploy, implementation engineering, or customer-facing technical role"；"REST APIs, SAML/OIDC, SCIM, and ideally FHIR/HL7"。
- 0→1："3+ years shipping production software"，Python + React/TypeScript 全栈，"prompting, retrieval, embeddings, evaluation"。

**加分项**：健康科技、创业公司或受监管行业经验；多云（AWS + Azure）；生产环境 GKE/Kubernetes；"Knowledge of ISO 27001 / HIPAA / APRA-style compliance"；进入 LLMOps 之前有后端、数据平台或 ML 基础设施底子；RPA 岗位除 Python 外会 C# 或 TypeScript。

### 行业领域

- **临床文书与医保编码。** 专设的 Clinical Coding Specialist 岗位要求 "HIMAA certification in Clinical Coding or equivalent"、"Expert-level knowledge of ICD-10-AM/ACHI and Australian Coding Standards (ACS)"、AR-DRG 分类以及 MBS / Medicare Australia 计费要求，工作方式是 "directly with our engineering team to embed your expertise into automated systems"（[Clinical Coding Specialist (Australia)](https://jobs.ashbyhq.com/heidihealth.com.au/0ac1835a-8faa-446c-b0b2-a581ca21e50c)；2026-06-01）。
- **EHR/EMR 的真实行为。** 集成岗要求候选人理解 "how a real EMR write-back actually works — encounter IDs, appointment IDs, patient context, addendum vs edit, side-by-side comparison, sectional mapping"，覆盖 Epic、Cerner、Athena、MEDITECH Expanse、Veradigm 与 Best Practice（[Technical Program Manager, Integrations](https://jobs.ashbyhq.com/heidihealth.com.au/3ec2c152-3983-4471-834a-60c8e1f6c993)）。
- **医疗器械软件监管。** Design Quality Engineer 岗位必需 IEC 62304、ISO 14971、ISO 13485 与 "SaMD Experience: Prior experience working on Software as a Medical Device (SaMD)"（[Design Quality Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/31e03395-c3a1-46c3-955c-ed9f50c2e8d7)）。
- **分区域的健康数据合规。** 公司按区域发布合规页：英国（DCB0129、DTAC、DSPT、Cyber Essentials、ICO 注册、Data Protection Act；"all our data is locally hosted within the UK"）、HIPAA（向 covered entity 提供 BAA；"all our data is locally hosted within the United States"），另有加拿大、GDPR 与澳大利亚隐私原则页面（[Compliance — UK](https://www.heidihealth.com/en-au/compliance/uk)、[Compliance — HIPAA](https://www.heidihealth.com/en-au/compliance/hipaa)；访问于 2026-08-31）。隐私政策写有 "Data localization solutions for customers located in Australia, Canada, US, UK and EU"（[Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy)）。
- **数据处理口径。** 安全页写 "As soon as Heidi transcribes, the audio disappears" 与 "Heidi doesn't use any of your data to train our AI"；隐私政策对 Scribe 写 "No patient data is used to train, develop, or improve any of our AI models"，对 Evidence 则写 "Queries may be reviewed and used in de-identified form to improve the platform, but PHI will not be used for model training"（[Safety](https://www.heidihealth.com/en-au/safety)、[Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy)）。

### 工作条件

| 项目 | 内容 | 出处 |
|---|---|---|
| 到岗政策 | 墨尔本/悉尼岗位写 "Flexible hybrid working environment, with **3 days in the office**"；招聘页只写 "Work where you do your best thinking" | [Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48)、[Careers](https://www.heidihealth.com/en-au/careers) |
| 明确要求坐班的岗位 | "This role is in-office in San Francisco. We believe in the energy and focus of being in the room together." | [Head of Engineering, North America](https://jobs.ashbyhq.com/heidihealth.com.au/adfea4ea-f501-4513-9b59-45b12774ee1d) |
| 远程岗位 | 85 个岗位中只有 2 个标 "Remote"（均面向美国），其余都写明城市 | [Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| 时区预期 | "You'll be working across a significant timezone gap with our product and engineering teams in Australia" | [Head of Engineering, North America](https://jobs.ashbyhq.com/heidihealth.com.au/adfea4ea-f501-4513-9b59-45b12774ee1d) |
| 异地办公 | "Work from anywhere for up to 1 month" | [Careers](https://www.heidihealth.com/en-au/careers) |
| 育儿假 | "26 weeks for primary carers and 18 weeks for secondary carers, globally. Your equity continues to vest throughout." | [Careers](https://www.heidihealth.com/en-au/careers) |
| 临床假 | "10 days per year to help our clinicians maintain accreditation… Available where ongoing accreditation is required." | [Careers](https://www.heidihealth.com/en-au/careers) |
| 生育支持 | "A one-time direct payment to support employees through IVF, egg freezing or sperm freezing" | [Careers](https://www.heidihealth.com/en-au/careers) |
| 学习预算 | 招聘页写 "$1,000 per year"，招聘启事写 "$500 per annum" —— 见 `备注` | [Careers](https://www.heidihealth.com/en-au/careers)、[Senior Product Analyst](https://jobs.ashbyhq.com/heidihealth.com.au/5d352f63-74c2-458c-b40d-0666881f263f) |
| 居家办公补贴 | "A one-off $500" | [Careers](https://www.heidihealth.com/en-au/careers) |
| 健身 | "Special corporate rates at Anytime Fitness in Melbourne, Sydney tbc"；更早的启事写 "Discounted corporate gym memberships" | [Senior Product Analyst](https://jobs.ashbyhq.com/heidihealth.com.au/5d352f63-74c2-458c-b40d-0666881f263f)、[Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837) |
| 期权 | "Become an owner, with shares (equity) in the company"；"Equity from day one" | [Senior DevOps Engineer - GCP](https://jobs.ashbyhq.com/heidihealth.com.au/7a30be9f-ba82-48a6-8f6c-b226ad2d1c48)、[Forward Deployed Engineer - UK](https://jobs.ashbyhq.com/heidihealth.com.au/02ad14b7-a9bb-45e3-a90f-631179f86d8d) |
| 公开薪资区间 | 85 个岗位中 13 个公开区间，全部是美国岗位或悉尼岗位。工程：Pre-sales Solutions Engineer - US（Remote）$160K–$200K + 期权。产品：Senior Product Designer（旧金山）$170K–$200K；Deployed PM, Health Systems（旧金山与悉尼）$170K–$220K；Head of Implementation（旧金山）$180K–$250K；Head of Product, North America（旧金山）$255K–$300K。澳大利亚与英国的工程岗位均未公开区间。 | [Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)；读取于 2026-08-31 |
| 招聘流程 | 五轮：recruiter chat、行为面、"Live Challenge — a practical assignment on a real problem you could tackle in-role"、与资深员工的终面、offer | [Careers](https://www.heidihealth.com/en-au/careers) |
| 应届与实习 | 一个实习岗（Commercial Specialist，墨尔本）与一个 "Expression of Interest — Heidi Entry Program"（墨尔本）；工程岗普遍要求 3 年以上至 7 年以上经验 | [Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| 工作语言 | 所查的 85 个岗位与所有产品界面均为英文；未公布语言政策 | [Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true) |
| 关于节奏的自述 | "We achieve in 6 months what it takes our competitors 4 years to do"（2026-06 启事）；"Ship, measure, go again. A button today, a workflow tomorrow. More iterations beat better planning."（2026-08 启事） | [Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837)、[Senior AI Models Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/f2a33fd0-e4bc-4e0b-84e3-c136a32af0ab) |

---

## 备注

### 未公开披露

2026-08-31 检索范围：`heidihealth.com`（从澳洲页脚可达的全部 locale 路径、`robots.txt` 与 sitemap index）、Ashby 招聘板及其 API、`trust.heidihealth.com`、`support.heidihealth.com`、`status.heidihealth.com`、ABN Lookup、GitHub API、npm registry，以及英文网络检索：

- **收入、ARR 或任何财务数字。** 所查来源均未公布收入、毛利、烧钱速度或客户合同金额。
- **工程博客或任何技术写作。** 博客是产品、SEO 与医生教育内容；没有一篇讲模型结构、评测方法或准确率口径的依据。
- **开源。** GitHub 组织 `Heidi-Health` 存在（创建于 2024-07-26，更新于 2024-10-14），但**公开仓库为 0**，没有 description、website、email 或 location；`heidihealth`、`heidiai`、`tryheidi`、`heidi-ai`、`oscer`、`oscerhealth` 均不是 GitHub 组织；GitHub 用户搜索 "heidihealth" 返回 0 条；未找到任何第一方 npm 包（[GitHub API](https://api.github.com/orgs/heidi-health)；读取于 2026-08-31）。
- **澳大利亚与英国岗位的薪资区间。** 13 个公开区间全部是美国岗位，外加两个悉尼产品岗。
- **Vanta Trust Center 的内容。** 该页在客户端渲染，对非浏览器客户端不返回任何认证清单、子处理者清单或文档索引；下文的认证口径来自市场页而非 Trust Center（[trust.heidihealth.com](https://trust.heidihealth.com/)；读取于 2026-08-31）。
- **各区域的云服务商与数据驻留细节。** 隐私政策写 "Data localization solutions for customers located in Australia, Canada, US, UK and EU"，合规页写英国与美国数据 "locally hosted"，但没有任何来源说明哪个区域跑在哪家云上。招聘启事在不同岗位里分别提到 AWS、GCP 与 Azure。
- **具名的子处理者。** 隐私政策只写 "third party service providers"、"evidence source partners and content licensors" 与 "third-party analytics tools"，未点名。
- **数据保留期限。** "We only keep your information for as long as you want it or are lawfully required to keep it" —— 没有给出期限（[Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy)）。
- **医疗器械注册/许可。** 安全页与合规页都没有声称取得 TGA（ARTG）、FDA 或 MHRA 的许可或注册；公司自己的口径是符合隐私、安全与 NHS 评估框架。2026-08-31 对 TGA ARTG 的查询未能完成，因此本文对 ARTG 不作任何方向的结论。Design Quality Engineer 岗位说明 IEC 62304 / ISO 14971 / ISO 13485 的工作正在进行中，而非已完成。
- **价格。** `en-au`、`en-us` 与 `en-gb` 定价页的价格均由客户端拉取，服务端 HTML 中没有；套餐与功能结构则完整公开。
- **管理层或团队页面。** `/about-us/people` 返回的是招聘页；公司自己的站点上只具名三位创始人。
- **2026-08-31 无法读取的来源：** Fierce Healthcare（HTTP 403）、Capital Brief（HTTP 403）、Business News Australia（HTTP 403）、Bloomberg（付费墙）、Crunchbase 与 PitchBook（需登录）。

### 不同来源之间的不一致

- **人数，同一天两个值。** 媒体页 "400+ employees around the world"，招聘页 "500+ Heidis"（[Media Room](https://www.heidihealth.com/en-au/about-us/media)、[Careers](https://www.heidihealth.com/en-au/careers)；均访问于 2026-08-31）。
- **节省工时，同一天三个值。** 招聘页 "47M Hours saved since launch"，企业页 "62.9M … saved by clinicians since launch"，B 轮新闻稿的 18 个月 "18 million hours"（并且在 2026 年 6 月的招聘启事里仍在沿用）（[Careers](https://www.heidihealth.com/en-au/careers)、[Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise)、[Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)）。
- **国家数。** 2025 年 10 月的新闻稿与直到 2026 年 6 月发布的招聘启事写 "116 countries"；媒体页写 "190 countries"，2026 年 8 月的启事写 "190+ countries"（[Heidi — Series B](https://www.heidihealth.com/en-us/blog/heidi-series-b)、[Senior Product Analyst](https://jobs.ashbyhq.com/heidihealth.com.au/5d352f63-74c2-458c-b40d-0666881f263f)、[Media Room](https://www.heidihealth.com/en-au/about-us/media)、[Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)）。
- **2026 年三个月内的每周量。** "2.4 million consults per week"（2026-02-24）、"more than 2.7 million visits a week"（2026-03-10）、"2.5 million patient sessions"（媒体页，2026-08-31），以及 2026-08-31 首页实时计数器显示的 2,740,338（[Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence)、[R1 RCM](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations)、[Media Room](https://www.heidihealth.com/en-au/about-us/media)、[heidihealth.com/en-au](https://www.heidihealth.com/en-au)）。
- **成立年份。** TechCrunch 在 2023 与 2025 两篇报道中都写 2021 年；若干二手资料写 2019 年；前身主体 OSCER ENTERPRISES PTY LTD 的 ABN 自 2017-08-01 起有效，HEIDI HEALTH TRADING PTY LTD 自 2021-04-28 起（[TechCrunch](https://techcrunch.com/2023/10/25/heidi-health/)、[ABN Lookup — Oscer](https://abr.business.gov.au/ABN/View?abn=57620824900)、[ABN Lookup — Heidi](https://abr.business.gov.au/ABN/View?abn=84649783871)）。
- **学习预算。** 招聘页写 "$1,000 per year"，2026 年 5 至 6 月发布的招聘启事写 "$500 per annum"（[Careers](https://www.heidihealth.com/en-au/careers)、[Senior Software Engineer - Developer Experience](https://jobs.ashbyhq.com/heidihealth.com.au/99ef4d45-fcaf-4d53-b2db-9acd8a740be3)）。
- **在招岗位数。** 站点页脚写 "Open Roles 10+"，同一天 Ashby 招聘板上有 85 个岗位（[Careers](https://www.heidihealth.com/en-au/careers)、[Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)）。
- **博客日期。** 文章页显示的是修改日期而非发布日期：A 轮追加的新闻稿页面显示 "June 26, 2026"，而其结构化数据的 `datePublished` 是 2025-03-03，第三方报道则定在 2025-03-06；"Relief, on repeat" 一文页面显示 July 31, 2026，而 `datePublished` 为 2026-07-07（[Heidi](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care)、[Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/)、[Heidi — Relief, on repeat](https://www.heidihealth.com/en-au/blog/introducing-relief-on-repeat)）。
- **2025 年 3 月这一轮的澳元折算。** Startup Daily 正文写 2,680 万澳元、标题写 2,700 万澳元；Business News Australia 标题写 2,570 万澳元（其正文无法读取，HTTP 403）（[Startup Daily](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/)）。
- **X 账号。** 站点页脚链接 `twitter.com/tryheidi`，而页面的 `twitter:site` meta 标签写的是 `@heidi_health`。

### 其他

- **在招岗位里仍留着过期的公司简介。** 一则 2026-06-25 发布的启事开头仍写 "our most recent $16.6MM round of funding" 与 "In just 12 months, 20 million patient consults were supported by Heidi, and we're now powering more than 1 million consults every week" —— 这些是 2025 年 3 月新闻稿的口径，已被 2025 年 10 月的 B 轮取代（[Senior DevOps Engineer - Azure](https://jobs.ashbyhq.com/heidihealth.com.au/5a1ed103-241b-4b4e-bc20-23f14f1e3837)）。
- **三套公司价值观同时在线。** "Live Forever / Practice Ownership / Move Fast, Fix Faster / Get Better"（招聘页）、"Build to Last / Own Your Practice / Move Fast, Stay Steady / Make Others Better"（2026 年 5–6 月启事）、"Live Forever / Practice Ownership / Small Cuts Heal Faster / Make others better"（另一批 2026 年 6 月启事），加上 2026 年 8 月启事里六条的 "How we show up"。
- **公司自己把商业模式描述为 freemium、由医生自下而上驱动。** "We found product-market fit with a freemium medical scribe that clinicians love"；定价页 FAQ 有一条标题是 "Why is there a free version of Heidi forever?"；CEO 对 Forbes 说 "We will never, ever monetise our free users by selling their data"（[Lead Site Reliability Engineer](https://jobs.ashbyhq.com/heidihealth.com.au/cde90d57-737b-4305-8dab-703ea685c1b8)、[Pricing](https://www.heidihealth.com/en-au/pricing)、[Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/)）。
- **产品线在 2026 年约半年内从一个扩到四个**：Evidence 与 Comms 于 2026-02-24/25 公布，Remote 在 2026 年 3 月，Dictate 自 2026-06-29 起可用；月度更新日志 "Progress Notes" 至少自 2026 年 1 月起持续（[Heidi — Evidence launch](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence)、[Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/)、[Heidi — Relief, on repeat](https://www.heidihealth.com/en-au/blog/introducing-relief-on-repeat)、[Changelog](https://www.heidihealth.com/en-au/changelog)）。
- **招聘重心偏商业侧。** GTM（35）加市场（6）合计 41 个，工程 24 个；六个市场岗中有三个是驻菲律宾马卡蒂市的 SEO 岗（[Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)）。
- **明确放行 AI 爬虫。** `robots.txt` 除 `*` 之外，另给 `ChatGPT-User`、`GPTBot` 与 `Google-Extended` 单独写了 `Allow: /`（[robots.txt](https://www.heidihealth.com/robots.txt)；读取于 2026-08-31）。
- **有公开状态页** `status.heidihealth.com`，企业页把 "Service availability" 列为企业版专属承诺；没有公布 SLA 数字（[Pricing](https://www.heidihealth.com/en-au/pricing)、[status.heidihealth.com](https://status.heidihealth.com/)）。

---

## 资料来源

**官方**

- [heidihealth.com/en-au](https://www.heidihealth.com/en-au) · [robots.txt](https://www.heidihealth.com/robots.txt) · [sitemap index](https://www.heidihealth.com/sitemap-index.xml) · [status.heidihealth.com](https://status.heidihealth.com/) · [support.heidihealth.com](https://support.heidihealth.com/) · [trust.heidihealth.com](https://trust.heidihealth.com/)
- 产品 —— [Scribe](https://www.heidihealth.com/en-au/scribe) · [Evidence](https://www.heidihealth.com/en-au/evidence) · [Dictate](https://www.heidihealth.com/en-au/product/dictate) · [Remote / Hardware](https://www.heidihealth.com/en-au/hardware) · [Templates](https://www.heidihealth.com/en-au/templates) · [Pricing](https://www.heidihealth.com/en-au/pricing) · [Enterprise](https://www.heidihealth.com/en-au/solutions/enterprise) · [System Requirements](https://www.heidihealth.com/en-au/system-requirements) · [Changelog（"Progress Notes"）](https://www.heidihealth.com/en-au/changelog)
- 公司 —— [Media Room](https://www.heidihealth.com/en-au/about-us/media) · [Careers](https://www.heidihealth.com/en-au/careers) · [Customer Spotlight](https://www.heidihealth.com/en-au/customers) · [Blog](https://www.heidihealth.com/en-au/blog)
- 安全与合规 —— [Safety](https://www.heidihealth.com/en-au/safety) · [HIPAA](https://www.heidihealth.com/en-au/compliance/hipaa) · [UK](https://www.heidihealth.com/en-au/compliance/uk) · [Canada](https://www.heidihealth.com/en-au/compliance/canada) · [GDPR](https://www.heidihealth.com/en-au/compliance/gdpr) · [APP（澳新）](https://www.heidihealth.com/en-au/compliance/app)
- 法律文件 —— [Privacy Policy](https://www.heidihealth.com/en-au/legal/privacy-policy) · [Heidi Scribe Terms of Use](https://www.heidihealth.com/en-au/legal/heidi-scribe-terms-of-use) · [Scribe Usage Policy](https://www.heidihealth.com/en-au/legal/scribe-usage-policy) · [UK GDPR Compliance Policy](https://www.heidihealth.com/en-au/legal/ukgdpr-compliance-policy) · [Accessibility Statement](https://www.heidihealth.com/en-au/legal/accessibility-statement)
- 招聘 —— [Ashby 招聘板](https://jobs.ashbyhq.com/heidihealth.com.au) · [Ashby 招聘板 API](https://api.ashbyhq.com/posting-api/job-board/heidihealth.com.au?includeCompensation=true)

**公司公告**（由新到旧）

- [Introducing: Relief, on repeat](https://www.heidihealth.com/en-au/blog/introducing-relief-on-repeat) —— 2026-07-07
- [More Patients, Less Paperwork: Heidi's AI Scribe Returns an Estimated $2.51M in Clinical Time](https://www.newswire.ca/news-releases/more-patients-less-paperwork-heidi-s-ai-scribe-returns-an-estimated-2-51m-in-clinical-time-893435988.html) —— 2026-07-22
- [Heidi and QHR Technologies integrate AI documentation into Accuro EMR](https://www.heidihealth.com/en-au/about-us/media) —— 2026-06-16
- [The Royal Children's Hospital deploys Heidi](https://www.heidihealth.com/en-au/about-us/media) —— 2026-06-03
- [Heidi Evidence launches, acquires AutoMedica](https://www.heidihealth.com/en-au/blog/heidi-launches-evidence) —— 2026-02-24
- [Building the AI Care Partner for Every Clinician](https://www.heidihealth.com/en-us/blog/ai-care-partner-for-every-clinician) —— 2025-10-31
- [Heidi Secures $65 Million USD in Series B Funding](https://www.heidihealth.com/en-us/blog/heidi-series-b) —— 2025-10-05
- [Heidi Health secures USD $16.6M in funding](https://www.heidihealth.com/en-us/blog/heidi-health-secures-usd-16-6m-in-funding-to-free-up-clinicians-to-focus-on-patient-care) —— 2025-03-06（页面显示的是修改日期）

**合作方与登记机关**

- [ABN Lookup — HEIDI HEALTH TRADING PTY LTD](https://abr.business.gov.au/ABN/View?abn=84649783871) · [ABN Lookup — OSCER ENTERPRISES PTY LTD](https://abr.business.gov.au/ABN/View?abn=57620824900)
- [R1 RCM — R1 and Heidi Announce Strategic Partnership](https://www.r1rcm.com/newsroom/r1-and-heidi-announce-strategic-partnership-to-improve-revenue-capture-for-physician-groups-and-healthcare-organizations) —— 2026-03-10
- [Blackbird 组合页 — Heidi Health](https://www.blackbird.vc/portfolio/heidi-health)
- [GitHub API — 组织 `Heidi-Health`](https://api.github.com/orgs/heidi-health)

**第三方报道**

- [Forbes Australia — Australian AI startup Heidi Health launches its first hardware device](https://www.forbes.com.au/news/entrepreneurs/australian-ai-startup-heidi-health-launches-its-first-hardware-device/) —— 2026-03-24
- [Canadian Healthcare Technology — Heidi AI scribes save 13 minutes per visit](https://www.canhealth.com/2026/07/22/heidi-ai-scribes-save-13-minutes-per-visit/) —— 2026-07-22
- [TechCrunch — Heidi Health raises $65M Series B led by Steve Cohen's Point72](https://techcrunch.com/2025/10/05/heidi-health-raises-65m-series-b-led-by-steve-cohens-point72/) —— 2025-10-05
- [SmartCompany — Heidi Health's $98 million raise skyrockets its valuation to $704 million](https://www.smartcompany.com.au/startupsmart/heidi-health-98-million-raise-valuation-704-million/) —— 2025-10-06
- [Startup Daily — GP administration startup Heidi Health tops up Series A with another $27 million](https://www.startupdaily.net/topic/gp-administration-startup-heidi-health-tops-up-series-a-with-another-27-million/) —— 2025-03-04
- [TechCrunch — Blackbird backs Heidi Health's AI platform for overworked doctors](https://techcrunch.com/2023/10/25/heidi-health/) —— 2023-10-25
