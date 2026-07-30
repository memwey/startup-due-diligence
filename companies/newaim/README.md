# New Aim

**English** | [简体中文](README.zh-CN.md)

> Notes compiled from publicly available sources. Last updated: 2026-07-30.
> Every figure is linked to the source it came from and dated. Verify against primary sources before relying on them.

## TL;DR

New Aim is a Melbourne e-commerce company that imports consumer goods — mostly furniture, bedding, appliances, outdoor and fitness products — sells them under 31 of its own brands through more than 30 Australian retail channels, and operates the warehousing, freight and software that other retailers plug into ([about page](https://www.newaim.com.au/about-us), accessed 2026-07-30). It calls the model "business-to-many" (B2M). The company dates itself to 2005; founder Fung Lam says the business "started as an eBay store in 2003" ([Stockland release, 2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)). It has three business units: direct e-commerce operations, the **Dropshipzone** B2B2C marketplace, and **AirOxy**, an AI analytics product ([Business News Australia, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)).

- **Revenue is on the public record as dated statutory bands**, because the company files under the Modern Slavery Act: A$250–300M (FY20), 300–350M (FY21), 350–400M (FY22, FY23, FY24), and **300–350M (FY25)** ([register entries](https://modernslaveryregister.gov.au/statements/?q=new+aim)). The last audited figure to reach the press was FY21: **A$39M net profit on A$343M revenue**, with pre-tax profit over A$62M ([The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)).
- **No external equity has been disclosed in 21 years.** CEO Alex Ji: "We have always been self-funded in growing the business and have never taken any external equity" ([2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)). Macquarie was mandated in 2022 to raise up to A$100M; no completion has been announced. The company is "contemplating a potential ASX listing".
- **Headcount is about 400**, "from Melbourne, Australia to Guangzhou, China" ([careers page](https://www.newaim.com.au/careers)), of which the in-house IT and data team is **about 70** ([2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)).
- **The stack is unusually well documented for a private company**, because two cloud vendors published case studies. New Aim ran on-premises, migrated everything to **Alibaba Cloud** (ECS, ApsaraDB RDS for MySQL, CEN, CDN, OSS), then migrated to **Google Cloud** from March 2024 — Compute Engine, Anthos, Cloud SQL, Firestore, BigQuery, Cloud VPN, Cloud Armor, Vertex AI ([Alibaba Cloud case study](https://www.alibabacloud.com/en/customers/new-aim), [Google Cloud case study](https://cloud.google.com/customers/new-aim)). The internal platform is called **AimCore** and runs on BigQuery.
- **Two Federal Court judgments turn on how New Aim handled supplier data.** It lost at first instance in [2025] FCA 747 partly because it gave employees no work phones and no supplier-confidentiality agreement, then won on appeal in **[2026] FCAFC 49** (2026-04-20) on a narrower case about 17 named suppliers ([13 Wentworth Chambers](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/), [IP Law Watch, 2025-07-21](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)).

---

## Basic

| Item | Detail | Source |
|---|---|---|
| Public brand | New Aim | [homepage](https://www.newaim.com.au/), accessed 2026-07-30 |
| Legal name (current) | **NEW AIM LTD**, entity type "Australian Public Company" | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432), record extracted 2026-07-30 |
| Legal name (recent) | "New Aim Pty Ltd", described as "an Australian proprietary company" in the FY25 statutory filing signed 2025-12-19, and in the AirOxy Terms of Use last updated 2025-10-29 | [FY25 Modern Slavery Statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/), [AirOxy Terms of Use](https://airoxy.ai/home/terms_of_use) |
| ABN / ACN | ABN 50 115 804 432; ACN 115 804 432 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432), [terms and conditions](https://www.newaim.com.au/terms-and-conditions) |
| ABN status | Active from 2005-09-02; GST registered from 2005-10-01; ABN last updated 2026-07-01 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432) |
| Registered business name | `dropshipzone`, registered from 2023-08-04 | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432) |
| Founded | Company dates itself to 2005; IBISWorld gives an incorporation date of 2005-08-22; the founder dates the eBay business to 2003 | [about page](https://www.newaim.com.au/about-us), [IBISWorld](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/), [Stockland, 2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion) |
| Head office | 16-18 Cato St, Hawthorn East VIC 3123; 03 9376 0841; info@newaim.com.au. The Hawthorn HQ opened in July 2021 | [contact page](https://www.newaim.com.au/contact-us), [news, July 2021](https://www.newaim.com.au/news) |
| Founders | Fung Lam (Co-Founder & Executive Director) and Cecilia Chiu (Co-Founder & COO); **Werner Liu** is named as a co-investor at founding and as a joint AFR Young Rich List entrant, and exited in 2021 | [about page](https://www.newaim.com.au/about-us), [CEO Magazine, 2019-12](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/), [The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) |
| Headcount | "more than 400 employees from Melbourne, Australia to Guangzhou, China"; IBISWorld reports 386 in 2025 including subsidiaries; LinkedIn shows a 201–500 band | [careers page](https://www.newaim.com.au/careers), [IBISWorld](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/), [LinkedIn](https://au.linkedin.com/company/new-aim) |
| IT and data team | About 70 people, as of 2025-09 | [Business News Australia, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| Warehouse space | ~70,000 sqm (site pages, accessed 2026-07-30); "more than 110,000 sqm" as of 2026-02; "more than 120,000 square metres" as of 2026-05 | [about page](https://www.newaim.com.au/about-us), [Best Managed Companies page](https://www.newaim.com.au/best-managed-companies), [BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| Channels | "more than 40 channels" on the about page; "more than 30 leading retail channels" in 2026 | [about page](https://www.newaim.com.au/about-us), [BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| Product range | "more than 6,000 active SKUs across over 450 product lines" on the about page; "over 7,000 SKUs covering over 400 different sub-categories" as of 2025-09 | [about page](https://www.newaim.com.au/about-us), [BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| Suppliers | "Today, in 2024, we have more than 400 suppliers"; The Australian reported "more than 400 factories in China" in 2022 | [technology page](https://www.newaim.com.au/technology), [The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| Total raised | No external equity round has been announced. See `Funding` | [BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| Engineering working language | Not stated on any company surface. The China subsidiary "supports IT and procurement functions"; the site publishes English and Simplified Chinese | [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/), [zh-CN about page](https://www.newaim.com.au/zh-cn/about-us) |
| Certifications | None published. See `Notes` | — |

Awards and rankings, each as dated by its source:

| Date | Recognition | Source |
|---|---|---|
| [2018-10](https://www.afr.com/work-and-careers/careers/financial-review-fast-100-2018-the-full-list-20181030-h179hx) | AFR Fast 100, no. 82; ~A$120M turnover in 2017–18, 44.3% average annual growth | company [news](https://www.newaim.com.au/news) citing AFR |
| [2019-09](https://www.afr.com/policy/economy/australia-s-top-500-private-companies-revealed-20190902-p52n8c) | AFR / IBISWorld Top 500 Private Companies debut, no. 349 | company [news](https://www.newaim.com.au/news) |
| [2020-02](https://www.afr.com/work-and-careers/management/fast-100-and-fast-starters-winners-revealed-20200219-p54269) | AFR Fast 100, no. 49; company valued at A$280M with 44% four-year CAGR | company [news](https://www.newaim.com.au/news) |
| 2020, 2021, 2022, 2023 | FT / Statista High-Growth Companies Asia-Pacific, four consecutive years; ranked second in Australia by revenue growth in the 2023 list | [FT 2023](https://www.ft.com/high-growth-asia-pacific-ranking-2023), company [news](https://www.newaim.com.au/news) |
| 2021-11 | AFR Young Rich List: Fung Lam no. 6, estimated net worth A$1.02bn | company [news](https://www.newaim.com.au/news) citing [AFR](https://www.afr.com/young-rich) |
| 2022-09 / 2024-09 | The Australian / IBISWorld Top 500 Private Companies: no. 193 (2022), no. 282 (2024) | [2022 PDF](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a434bf99103902761316fdd_The-Australian-Top-500-Private-Companies_2022.pdf), company [news](https://www.newaim.com.au/news) |
| 2023-11 | Fung Lam wins the Henry Ngai Medium to Large Business category, Ethnic Business Awards | company [news](https://www.newaim.com.au/news) |
| [2026-02-27](https://www.deloitte.com/au/en/about/press-room/deloitte-best-managed-companies-awards-270226.html) | One of nine winners of Deloitte Private's Australia's 2025 Best Managed Companies | Deloitte press release |
| 2026-04 | Asia-Pacific Stevie Award for organisational excellence, Macao | company [news](https://www.newaim.com.au/news) |

The company frames the market it operates in as structurally polarised: co-founder Cecilia Chiu writes that Australia's "$69 billion (2024)" e-commerce market is splitting between platforms that control demand and businesses that control fulfilment infrastructure, squeezing the middle ([BNA, 2025-12-19](https://www.businessnewsaustralia.com/blog/the-growing-divide-in-australia-s-e-commerce-market)). This is the company's own framing, published as sponsored member content.

### Identity and legal entities

| Name | Type | Relationship and period | Source |
|---|---|---|---|
| NEW AIM LTD | Australian public company, ACN 115 804 432 | Current registered entity name and the operator of `newaim.com.au` | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432), [terms](https://www.newaim.com.au/terms-and-conditions) |
| New Aim Pty Ltd | Former registered name, same ACN | Used in the FY25 statutory filing signed 2025-12-19 and in the AirOxy terms updated 2025-10-29; the site footer said "New Aim Pty Ltd" as recently as [2025-12-14](http://web.archive.org/web/20251214072201/https://www.newaim.com.au/careers/) and says "New Aim Ltd" now | [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/), [AirOxy terms](https://airoxy.ai/home/terms_of_use) |
| New Aim Hong Kong Co., Limited ("HKNA") | Hong Kong holding company | Incorporated 2022-01-01 as a wholly owned holding company | [FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| Guangzhou New Aim E-commerce Co., Ltd ("GZNA") | Chinese company | Wholly owned subsidiary of HKNA; employs staff in China supporting **IT and procurement** | [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| Predecessor China services entity | Separate legal entity, not named | Before FY22 it provided exclusive services to New Aim including IT and procurement under a services agreement; it was wound up in FY21/22 and its workforce transferred to GZNA | [FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| Dropshipzone | Marketplace brand | A registered business name of the same ABN since 2023-08-04. The Google Cloud release calls it New Aim's "subsidiary B2B2C marketplace"; the Dropshipzone privacy statement says New Aim Ltd "owns and operates" it and its API documentation carries the same ABN | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432), [Google Cloud, 2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers), [DSZ privacy statement](https://www.dropshipzone.com.au/privacy_statement) |
| OzPlaza / OzPlaza.living | eBay store | "Owned and operated by New Aim"; became the second Australian eBay seller to pass one million feedback entries in 2018 | [Internet Retailing, 2018-09](https://internetretailing.com.au/aussie-seller-cracks-ebay-benchmark/) |
| AirOxy | Product brand | Operated under New Aim's own ACN; terms name New Aim Pty Ltd | [AirOxy terms](https://airoxy.ai/home/terms_of_use) |

The change from `Pty Ltd` to `Ltd` is a change of company type on the same ACN, not a new entity. No company release, filing, or media report found on 2026-07-30 announces or explains it; see `Notes`.

---

## Product

### Three business units

Alex Ji describes New Aim as comprising three units: its original direct e-commerce operations covering the whole supply chain, the Dropshipzone platform, and AirOxy ([BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)). The statutory filings describe the same business as four models ([FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)):

| Model | What it is |
|---|---|
| Dropshipzone | New Aim's B2B marketplace. New Aim is both the operator and a supplier on it; third-party "DSZ Suppliers" contract directly with retailers and fulfil their own orders |
| Online marketplaces | Direct-to-consumer selling through Amazon, eBay, Big W, Kogan, Bunnings, Myer, Barbeques Galore and Kmart (FY25 list) |
| D2C brand websites | Standalone sites for the in-house brands |
| Dropshipping partnerships | New Aim holds inventory and fulfils orders on behalf of a retailer, who contracts with the consumer |

### In-house brands

31 brands are listed on the [brands page](https://www.newaim.com.au/brands) (accessed 2026-07-30): 5-Star Chef, Alba, Alfresco, Alpha, Aqua Buddy, Artiss, Cefito, Devanti, Emajin, Embellir, Everfit, Gardeon, Giantz, Giselle Bedding, Glacio, Green Fingers, Grillz, i.Pet, Instahut, Jingle Jollys, Keezi, Leier, Livemor, Lockmaster, Prime Turf, Rigo, Seamanship, Ul-tech, Wanderlite, Weisshorn, Zenses. The FY24 statutory filing lists eleven of these with their own D2C domains — `artiss.com.au`, `cefito.com.au`, `devanti.com.au`, `everfit.com.au`, `gardeon.com.au`, `gisellebedding.com.au`, `jinglejollys.com.au`, `ipet-au.com`, `keezi.com.au`, `rigokids.com.au`, `weisshorn.com.au` — plus `artissin.com.au` and `cosyclub.com.au` in FY22 ([FY24](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/), [FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)).

### Dropshipzone

Launched in Melbourne in 2012 and founded by Cecilia Chiu ([about page](https://www.dropshipzone.com.au/about_us), [BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)). It transitioned from a wholesale-style platform to a marketplace in **October 2022**, after which DSZ Suppliers contract directly with retailers — a change the company itself described as reducing its own oversight of those suppliers' labour practices ([FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)).

- **Commercial terms:** free to sign up, no upfront costs, subscription fees or membership fees; no minimum order quantities; an active ABN or ACN, a company name and a link to an online store are required, with approval typically inside 2 business days ([FAQ](https://www.dropshipzone.com.au/faq), accessed 2026-07-30).
- **Catalogue:** "Over 100,000 products available for resale" ([homepage](https://www.dropshipzone.com.au/), accessed 2026-07-30) across 19 categories.
- **Published policies:** Supplier Service Level Agreement, Mandatory Injury Reporting, Product Safety Recalls, Ethical Sourcing, Banned Products, Price Comparison, Price Gouging, and Product Category Eligibility ([policy page](https://www.dropshipzone.com.au/policy)).
- **Shopify app:** launched **2020-05-15**, free to install, rated 4.4 from 14 reviews, developer address 16-18 Cato St ([Shopify App Store](https://apps.shopify.com/newaim_app), accessed 2026-07-30).
- **Retailer API:** ten public endpoints under `api.dropshipzone.com.au` — auth, category list, category products, product by SKU, product search, stock, shipping cost, zone mapping, and place order. Access tokens expire in 15 minutes; the documented throttle is 60 requests/minute and 600/hour. The documentation was generated with apidoc 0.23.0 on **2021-07-07** and is versioned 1.0.1 ([apidoc](https://www.dropshipzone.com.au/apidoc/index.html), [api_data.json](https://www.dropshipzone.com.au/apidoc/api_data.json)).
- A separate **Supplier API** was announced in [August 2022](https://www.retailbiz.com.au/online-retailing/dropshipzone-delivers-new-api-for-data-integration/) as "a first for Aussie suppliers"; no public documentation for it was found.

### AirOxy

Described by the company as an AI-powered analytics and marketplace-intelligence platform, built out of AimCore's technology and running on Google Cloud ([Google Cloud, 2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)). It piloted at the Online Retailer show in **July 2024**; Alex Ji says the first public version was released "at the end of last year", i.e. end of 2024 ([BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)). It was shown at the Google Cloud Summit in Sydney in July 2025 ([company news](https://www.newaim.com.au/news)).

Published feature areas ([airoxy.ai](https://airoxy.ai/), accessed 2026-07-30): sourcing price trend history, product rating, top selling, keyword recommendations, and a channel overview across Australian marketplaces, plus an AI chat assistant. The application's own route table additionally exposes AI content writing, AI image generation, product discovery, and competitor tracking with lowest-price export.

Pricing as displayed on 2026-07-30 ([plans page](https://airoxy.ai/home/plans)):

| Plan | Price | Product list | AI chat | AI images | AI content writer | Teams |
|---|---|---|---|---|---|---|
| Starter | A$29/month | up to 500 | 300/month | 10 credits/month | 20/month | 1 |
| Business | A$79/month | up to 2,000 | 3,000/month | 20 credits/month | 100/month | 1 |
| Enterprise | Contact us | up to 20,000 combined | 30,000/month | 300 credits/month | 500/month | 10, soft ceiling |

All plans state profitability and margin analysis, sourcing from all major Australian marketplaces, and integration with Dropshipzone and Shopify. Payment is Stripe-only and AirOxy states it does not receive or store card details. Model-training opt-out is by email request ([Terms of Use, last updated 2025-10-29](https://airoxy.ai/home/terms_of_use)).

### Reported scale over time

| Date | Reported figure | Source |
|---|---|---|
| 2013 | One leased warehouse of 11,000 sqm | [The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| 2016 | 5,000 sqm at Stockland's Brooklyn Distribution Centre, later grown to 65,000 sqm | [Stockland, 2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion) |
| 2018-09 | OzPlaza.living becomes the second Australian eBay seller past 1M feedback entries, one of 83 worldwide; 99.4% positive | [Internet Retailing](https://internetretailing.com.au/aussie-seller-cracks-ebay-benchmark/), [CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/) |
| As of 2020 | 250+ employees, 66,000 sqm warehouse, annual turnover in excess of A$300M | [Alibaba Cloud case study](https://www.alibabacloud.com/en/customers/new-aim) |
| FY21 (to 2021-06-30) | A$343M revenue, A$39M net profit, pre-tax profit over A$62M, per the ASIC-lodged financial report | [The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) |
| 2021 | ~4 million parcels delivered; more than 100 employees in China | [The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| FY21 | "more than 4 million products" shipped | [about page](https://www.newaim.com.au/about-us) |
| 2022-08 | Integrated with 35 online marketplaces and retailer channels across Australia and NZ; drop-ship division about one-third of revenue | [The Australian](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf), [The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| 2023-09 | New 31,500 sqm distribution centre, 32,000 pallet capacity, 150m canopy, AGVs and sort-bot systems, 5 Star Green Star target | [company news](https://www.newaim.com.au/news), [Stockland](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion) |
| 2024-09 | 2,500+ active retailers on Dropshipzone; reaches more than one in two Australian households | [Google Cloud](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) |
| 2025-09 | 30+ channels, 7,000+ SKUs, 400+ sub-categories, ~400 staff of whom ~70 in IT and data | [BNA](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 2026-02 | "more than 110,000 sqm of self-managed warehousing", "over five million units annually", "thousands of retail and SME partners" | [Best Managed Companies page](https://www.newaim.com.au/best-managed-companies) |
| 2026-05 | "more than 120,000 square metres of self-managed warehousing", "over 8,000 standard shipping containers in 2025", "around four million units annually", delivered to "more than 70% of Australian homes" | [BNA](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| Accessed 2026-07-30 | "Since 2005, we've delivered products to more than 60% of Australian households"; "1 in 2 Aussies own a New Aim product"; "Top 10 in Aussie ecommerce" | [about page](https://www.newaim.com.au/about-us), [homepage](https://www.newaim.com.au/) |

### Announced customers and partners

| Date | Party | Detail |
|---|---|---|
| FY22 | Harvey Norman, Coles, Costco, Mosaic Brands, Zanui, Big W, David Jones, Kitchen Warehouse | Bespoke dropshipping arrangements ([FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)) |
| FY24 | Harvey Norman, Coles, Costco, David Jones, Kitchen Warehouse, Everything Caravan & Camping, Lasoo, Ineda, Baby Bunting | Dropshipping partners; Mosaic Brands, Zanui and Big W no longer listed ([FY24 statement](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/)) |
| FY25 | Amazon, eBay, Big W, Kogan, Bunnings, Myer, Barbeques Galore, **Kmart** | Marketplace list; Catch, Mydeal, WooliesX and Mysale drop out of the list versus FY24 ([FY25](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/), [FY24](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/)) |
| [2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) | Google Cloud | Cloud consolidation and co-development of AirOxy; customers named include Bunnings, Woolworths, Big W, Baby Bunting |
| [2025-06](https://www.rmit.edu.au/news/ccsri/enhance-ai-driven-ecommerce-solutions) | RMIT University | Research partnership with RMIT's Cyber Security Research & Innovation Centre and CSIRO's Data61 on supply chain optimisation, dynamic pricing and personalisation, on "privacy-by-design" principles |
| 2025-10 | Hugo Cross-Border | Partnership on cross-border sellers entering Australia ([company news](https://www.newaim.com.au/news)) |
| 2025-11 | Monash University | Gold sponsor of the 2025 Australian Undergraduate Business Case Competition, whose case study was built on the Dropshipzone model ([Monash](https://www.monash.edu/business/news/2025/bright-ideas-shine-at-global-business-challenge)) |
| 2023-10 | Stockland | Lease at 90 Melbourne Drive, Truganina (Melbourne Business Park); relationship began 2016 at Brooklyn DC ([Stockland](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)) |

### Stated plans

At the 20th anniversary gala in September 2025 the company named four growth engines: expanding its D2C e-commerce footprint, globalising the Dropshipzone marketplace, upgrading its proprietary AI-driven intelligence, and building "a unified, one-stop e-commerce ecosystem" ([company news](https://www.newaim.com.au/news)). In November 2025 at a Shenzhen summit it launched **New Aim 360**, described as an end-to-end enablement ecosystem integrating supply chain logistics, Channel-as-a-Service, AirOxy AI and after-sales support, and said over 100 companies approached it there ([company news](https://www.newaim.com.au/news)). Alex Ji frames AirOxy as analogous to AWS emerging from Amazon's internal systems, and says the company is "contemplating a potential ASX listing" while weighing several options ([BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)).

---

## Founder

| Name | Role | Career facts stated | Source |
|---|---|---|---|
| **Fung Lam** | Co-Founder & Executive Director; CEO until 2025-06-01 | IT graduate. Began buying goods in bulk from two-dollar discount shops and reselling on eBay, using eBay "from probably 2003"; founded New Aim in 2005 after graduating from university, with Werner Liu. Gained full control of the company in 2021 after a legal battle with co-owner Werner Liu. Born ~1982 (described as 40 in 2022) | [The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf), [The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf), [CEO Magazine, 2019-12](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/) |
| **Cecilia Chiu** | Co-Founder & COO; previously Chief Strategy Officer, and titled CSO in 2023–24 award notices | Founded Dropshipzone in 2012 and is described as an early adopter of dropshipping in Australia. Described a "15-year journey in ecommerce" in 2022. States that she and her husband co-founded New Aim; Fung Lam separately describes his wife's involvement in the business | [about page](https://www.newaim.com.au/about-us), [BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html), [Power Retail, 2022-07](https://powerretail.com.au/20-questions-with-cecilia-chiu-co-founder-of-new-aim/), [BNA, 2025-12-19](https://www.businessnewsaustralia.com/blog/the-growing-divide-in-australia-s-e-commerce-market), [CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/) |
| **Werner Liu** | Former co-owner and, per AFR, former executive director | Invested in New Aim with Fung Lam when both were university graduates. Ranked jointly 19th with Fung Lam on the 2020 AFR Young Rich List at A$273M, both described as founders and executive directors. Parted ways with Lam in 2021; The Australian reported he would receive about A$101M. He is not named on any current New Aim page | [CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/), [The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf), [Being Asian Australian summary of the 2020 AFR Young Rich List](https://beingasianaustralian.net/2020/12/24/at-least-14-asian-australians-listed-on-the-afr-young-rich-list/) |

### Selected leadership

Current leadership as listed on the [about page](https://www.newaim.com.au/about-us) (accessed 2026-07-30): **Alex Ji** (CEO), **Cecilia Chiu** (COO), **Stephen Xiao** (CFO), **Carrie Hu** (CIO), **Christine Peng** (CPO — rendered 首席人力官, Chief People Officer, on the [Chinese page](https://www.newaim.com.au/zh-cn/about-us)).

**Alex (Yiming) Ji**, CEO from **2025-06-01** ([announcement](https://www.newaim.com.au/new-chapter-new-aim)):

- Joined New Aim in 2021 as Chief Information Officer, then Chief Operating Officer, with the CTO title added to the COO role in September 2024 ([company news](https://www.newaim.com.au/news)).
- Before New Aim, senior data science leadership roles at **NAB, Vocus Group and Sportsbet**; visiting professor at Soochow University.
- Bachelor of Computer Science (Hons), software engineering and AI specialisation, Northwestern Polytechnical University; PhD in Information Sciences and Engineering, The Australian National University.
- CIO50 Australia awardee in 2023 and ranked no. 7 in 2024 ([CIO50 2024](https://www.cio.com/article/3568346/australias-leading-it-executives-honoured-at-cio50-2024-awards.html), [awardee profile](https://www.cio.com/awardee/3558026/alex-ji.html)).

**Carrie Hu** was promoted to CPO and the Executive Leadership Team in September 2024, won the CIO50 2024 "Next CIO Award", and won Digital Transformation Leader of the Year at the 2023 Women in Digital Awards for work including Dropshipzone ([company news](https://www.newaim.com.au/news)). She is listed as **CIO** on the about page but bylined as **CTO** on a June 2026 article ([BNA, 2026-06-09](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human)); see `Notes`.

**David Huang** is quoted as "Chief Operating Officer, New Aim" in the undated Alibaba Cloud case study and is not named on any current company page ([Alibaba Cloud](https://www.alibabacloud.com/en/customers/new-aim), accessed 2026-07-30).

The about page lists the functions the company organises around: Buying; Human Resource & Admin; Finance & Legal; Customer Service & Quality Management; Warehouse; IT; Channels; Category. The FY25 filing lists Australian functions as brand, channel, finance, HR, data and analytics, digital product delivery, logistics and quality management ([FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)).

---

## Funding

No external equity round has ever been announced. The company's position, stated by its CEO in September 2025: "We have always been self-funded in growing the business and have never taken any external equity to do this... Every year we put our profits back into the business to continue growing" ([BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)).

| Date | Event | Amount | Detail | Source |
|---|---|---|---|---|
| 2021 | Founder buyout | ~A$101M to Werner Liu | Fung Lam gained full control after a legal battle with co-owner Werner Liu; The Australian understood the borrowing to fund the settlement raised concerns about debt levels and that advisory firm **McGrathNicol** was called in | [The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) |
| 2022-08 | Capital-raising mandate | up to A$100M sought, "about A$50m–A$100m for an undisclosed stake" | Macquarie appointed; teaser dubbed **Project Hawkeye**, describing New Aim as "Retail's best kept secret" and projecting ~A$400M revenue in FY23; likely to target private equity | [The Australian, 2022-08-15](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf), [company news](https://www.newaim.com.au/news) |
| 2025-09 | Potential ASX listing | — | "Contemplating a potential ASX listing"; several options being weighed to support the AirOxy rollout | [BNA, 2025-09-29](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html) |
| 2026-07-30 | Company type | — | The ABN register now records the entity as an **Australian Public Company** named NEW AIM LTD; the FY25 filing signed 2025-12-19 still described it as a proprietary company | [ABN Lookup](https://abr.business.gov.au/ABN/View?abn=50115804432), [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |

No completion, withdrawal, or outcome of the 2022 Macquarie mandate was found in any public source on 2026-07-30.

### Revenue on the statutory record

Each Modern Slavery Act statement declares an annual-revenue band for its reporting period. This is the only continuous, dated, first-party revenue series available:

| Period | Declared annual revenue | Statement | Source |
|---|---|---|---|
| FY20 (2019-07-01 – 2020-06-30) | A$250–300M | #2022-2472 | [register](https://modernslaveryregister.gov.au/statements/11261/) |
| FY21 | A$300–350M | #2022-2473 | [register](https://modernslaveryregister.gov.au/statements/11270/) |
| FY22 | A$350–400M | #2022-2476 | [register](https://modernslaveryregister.gov.au/statements/11271/) |
| FY23 | A$350–400M | #2023-2889 | [register](https://modernslaveryregister.gov.au/statements/16116/) |
| FY24 | A$350–400M | #2024-3204 | [register](https://modernslaveryregister.gov.au/statements/21077/) |
| FY25 (2024-07-01 – 2025-06-30) | **A$300–350M** | #2025-3497 | [register](https://modernslaveryregister.gov.au/statements/26345/) |

IBISWorld separately reports A$356,565,000 total revenue for "2025" and A$320,514,000 for "2024", and 386 employees in 2025 including all subsidiaries ([IBISWorld](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/)). Those figures do not line up with the register's period-by-period bands in the same order; see `Notes`.

---

## Engineering

### Technology stack and platforms

New Aim publishes no stack page. The items below are confirmed by vendor case studies, the companies' own releases, published API documentation, HTTP response headers, and a package published under a company email address — each labelled by evidence type.

| Item | Detail | Evidence |
|---|---|---|
| Cloud, current | **Google Cloud**, migration begun **March 2024**. Two stages complete by late 2024, moving the warehouse and order management system and the Dropshipzone business | Confirmed — [Google Cloud case study](https://cloud.google.com/customers/new-aim), [Google Cloud release, 2024-09-11](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) |
| Google Cloud products named | Compute Engine (with Local SSD and Persistent Disk), **Anthos** for the enterprise container platform, **Cloud SQL** and **Firestore** for databases, **BigQuery** for the data warehouse, Cloud VPN, Cloud Armor, Vertex AI | Confirmed — [Google Cloud case study](https://cloud.google.com/customers/new-aim) |
| Generative AI | Models tested and selected from the **Model Garden on Vertex AI**, used in AirOxy for pricing insights, market trends and product-image optimisation | Confirmed — [Google Cloud release](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers) |
| Cloud, previous | **Alibaba Cloud** — Elastic Compute Service, **ApsaraDB RDS for MySQL**, Cloud Enterprise Network, CDN, Object Storage Service. New Aim "successfully migrated all of its systems onto Alibaba Cloud" from a majority on-premises estate | Confirmed — [Alibaba Cloud case study](https://www.alibabacloud.com/en/customers/new-aim), undated; accessed 2026-07-30 |
| Reason for the move | The Google Cloud case study says New Aim's "previous infrastructure service provider exited the market". Alibaba Cloud notified affected customers from December 2023 and ceased Australian data-centre operations on 2024-09-30 | Inference — the exiting provider is not named in any source reviewed ([Alibaba Cloud notice](https://www.alibabacloud.com/en/notice/notice_on_the_ceasing_operation_of_alibaba_cloud_data_centers_in_australia_and_india_351)) |
| Availability | Service uptime improved from **97% to 99%**; infrastructure incident response reduced from hours to 15 minutes | Confirmed — [Google Cloud case study](https://cloud.google.com/customers/new-aim) |
| Corporate site | Webflow, published from a `newaim-stagging-domain.webflow` project, served through Cloudflare | Confirmed — [response headers and page source](https://www.newaim.com.au/), accessed 2026-07-30 |
| Dropshipzone frontend | **Next.js** (`X-Powered-By: Next.js`, `/_next/static/` asset paths). Its `robots.txt` still disallows Magento-era paths (`/downloader/`, `/catalogsearch/`, `/catalog/product_compare/`, `LICENSE_AFL.txt`), and some category URLs exist in both `.html` and clean forms | Confirmed — [headers](https://www.dropshipzone.com.au/), [robots.txt](https://www.dropshipzone.com.au/robots.txt), accessed 2026-07-30 |
| Dropshipzone API | REST over JSON at `api.dropshipzone.com.au`; token auth with 15-minute expiry; documented rate limits of 60/min and 600/hour enforced at an "API Gateway"; docs built with apidoc 0.23.0, generated 2021-07-07 | Confirmed — [api_project.json](https://www.dropshipzone.com.au/apidoc/api_project.json), [api_data.json](https://www.dropshipzone.com.au/apidoc/api_data.json) |
| AirOxy frontend | A Vite-built single-page app on **nginx**; React, React Router, Redux and MUI, with PapaParse for CSV. **Amplitude** analytics with autocapture and session replay, the latter enabled lazily off the public landing routes | Confirmed — [airoxy.ai](https://airoxy.ai/) page source and JS bundle, accessed 2026-07-30 |
| AirOxy backend hosts | `api.airoxy.com.au` and `identity.airoxy.com.au` (a separate identity service); **Stripe** billing portal; **Firebase** services including Remote Config, Installations and the `vertexai-preview` SDK; an **Azure Blob Storage** account named `airoxyproductlensdev` | Confirmed — string references in the published [AirOxy JS bundle](https://airoxy.ai/app-75bf66c1.js), accessed 2026-07-30 |
| Frontend tooling published publicly | `@airoxy/create-react` on npm — "an react scaffold using react react-router and redux", CLI `airoxy-create-react`, 11 versions between 2024-02-23 and 2024-02-29, maintainer email `jack.pan@newaim.com.au` | Confirmed — [npm](https://registry.npmjs.org/@airoxy/create-react) |
| Integrations offered | Shopify and Magento, with "a two-way flow of information" | Company statement — [technology page](https://www.newaim.com.au/technology) |
| Internal HR/ATS platform | Employment Hero is used for job postings and, per the FY25 filing, as the "employee management platform" delivering training | Confirmed — [careers page](https://www.newaim.com.au/careers) links, [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| Warehouse automation hardware | AGVs and sort-bot systems at the 2023 distribution centre; RF scanning for order fulfilment | Company statement — [company news, 2023-09](https://www.newaim.com.au/news), [homepage](https://www.newaim.com.au/) |
| Job-posting requirement | "Programming languages such as Java, Python, or similar" for the Software Engineer role | Hiring-only mention — [LinkedIn posting, expired](https://au.linkedin.com/jobs/view/software-engineer-at-new-aim-4405094003), summarised from search results 2026-07-30 |

### Systems

| System | What it does | Source |
|---|---|---|
| **AimCore** | The proprietary operating platform, described as embedded across the value chain and integrating procurement, inbound freight, warehouse allocation, replenishment, picking, dispatch and aftersales into "one decision engine". It runs on a BigQuery data warehouse analysing product sourcing, logistics and warehousing data | [BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation), [Google Cloud case study](https://cloud.google.com/customers/new-aim) |
| Warehouse and order management | A tailored warehouse management system plus order management systems integrated by the in-house IT team; a fully automated instant relay between order placement and picking | [technology page](https://www.newaim.com.au/technology) |
| Warehouse optimisation | Put-away simulation to reduce forklift travel and maximise cubic efficiency; replenishment algorithms prioritising channels with the strictest service levels; wave planning for pick routes | [BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| **Postage Optimiser** / Last-Mile Postage Optimiser (LPO) | Dispatching algorithms that select carrier and service by parcel size, postcode and courier across a courier network; last-mile routing described as using historical data, AI and machine learning. Cecilia Chiu described choosing "the lowest rate across five to six courier companies" | [technology page](https://www.newaim.com.au/technology), [CIO50 2023 citation in company news](https://www.newaim.com.au/news), [The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf) |
| Multi-channel data platform | A data platform consolidating datasets from 40 sales channels, cited in Alex Ji's 2023 CIO50 award | [company news, 2023-07](https://www.newaim.com.au/news) |
| Forecasting and demand planning | Sales and budget forecasting tied to live cash flow; warehouse capacity and S&OP planning that "thinks in CBM, not just units, across multiple sites"; a model-tuning workbench letting buyers inject qualitative signals into quantitative forecasts with a human-in-the-loop confirmation step before writing to plan; a natural-language data agent that answers planner questions such as why a sub-category's Days Of Stock slipped | [BNA, 2026-06-09](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human) |
| **AirOxy** decision engine | Stated to process "more than 100 million data points across pricing, search behaviour, category rankings and competitor activity" as a closed-loop engine feeding pricing, inventory allocation and channel strategy | [BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation) |
| **Dropshipzone** marketplace | Catalogue management, fulfilment, and integration with major retail platforms for SME retailers; product/inventory/order sync and shipping-fee calculation through the Shopify app and the retailer API | [BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation), [Shopify app](https://apps.shopify.com/newaim_app) |
| AI customer service | Natural language processing to classify and categorise messages, drive autoreplies and accelerate responses; stated to resolve "up to 30% of New Aim product and customer queries" | [technology page](https://www.newaim.com.au/technology) |
| AR virtual showrooms | Described as in progress for homewares ranges | [technology page](https://www.newaim.com.au/technology) |

### Technical background sought

Only three roles were listed on the [careers page](https://www.newaim.com.au/careers) on 2026-07-30: **Staff Software Engineer** (dated 05-02-2026), **Quality Control Officer** (05-02-2026), and **Warehouse Picker & Packer – Derrimut/Truganina** (15-06-2025). Both LinkedIn links for the first two resolve to LinkedIn's `expired_jd_redirect`, so the postings could not be read; the warehouse link goes to an Employment Hero listing.

The only engineering role text recoverable on 2026-07-30 is a **Software Engineer** posting, also expired, indexed as: Hawthorn East VIC 3123, on-site, permanent, full-time; design, develop, test, implement and maintain software applications, backend services, platform integrations and system components supporting New Aim's e-commerce platform; at least 1 year of relevant experience; experience with programming languages such as Java, Python or similar ([Employment Hero listing](https://employmenthero.com/jobs/position/new-aim-software-engineer-lj7cb/) and [LinkedIn posting](https://au.linkedin.com/jobs/view/software-engineer-at-new-aim-4405094003), both returning 404 or an expiry redirect on 2026-07-30; text from search-result indexing and therefore **unconfirmed**).

Archived snapshots of the careers page show how rarely engineering roles appear on it: warehouse, forklift and channel-growth roles in [March 2025](http://web.archive.org/web/20250315202431/https://www.newaim.com.au/careers/), warehouse roles only in [October 2025](http://web.archive.org/web/20251006230929/https://www.newaim.com.au/careers/), and quality-control plus warehouse roles in [December 2025](http://web.archive.org/web/20251214072201/https://www.newaim.com.au/careers/). The February 2026 Staff Software Engineer listing is the first engineering role visible on the page across the snapshots reviewed.

### Industry domain

- **Big and bulky e-commerce.** The company defines big and bulky as products over 10 kilograms and states the category "cannot be easily automated", requiring more warehouse space, higher-touch handling, tighter inventory control and greater freight exposure ([BNA, 2026-05-01](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)).
- **Australian marketplace and omnichannel integration** — reconciling catalogue, inventory, pricing and freight rules across 30–40 distinct retailer and marketplace channels.
- **China sourcing and cross-border supply chain.** Most in-house brand product is manufactured in China; the group holds a Hong Kong holding company and a Guangzhou subsidiary handling IT and procurement ([FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)).
- **Modern slavery, ethical sourcing and product-safety compliance.** New Aim is a reporting entity under the Modern Slavery Act 2018 (Cth) and has filed six statements; it runs a Timber Due Diligence policy, an Ethical Sourcing Policy, supplier questionnaires, and from FY25 a management-level Risk Committee, with a unified ESG and supplier-compliance platform designed in FY25 for FY26 rollout ([FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)).
- **Australian Privacy Principles** under the Privacy Act 1988 (Cth), with disclosure to related bodies corporate in Hong Kong and China ([privacy policy](https://www.newaim.com.au/privacy-policy)).
- **Trade-secret and confidentiality law.** Two Federal Court proceedings have turned on whether New Aim's China supplier identities were confidential and on how it managed employee access to them; see `Notes`.

### Working conditions

| Item | Detail | Source |
|---|---|---|
| Open roles | Three as of 2026-07-30: Staff Software Engineer, Quality Control Officer, Warehouse Picker & Packer. Two of the three links no longer resolve | [careers page](https://www.newaim.com.au/careers) |
| Locations | Head office 16-18 Cato St, Hawthorn East VIC 3123; warehouses in Derrimut, Laverton North and Truganina in Melbourne's west; offices in Guangzhou, China | [contact page](https://www.newaim.com.au/contact-us), [Employment Hero listing](https://employmenthero.com/jobs/position/new-aim-warehouse-picker-packer-monday-to-wednesday-osc0j/), [careers page](https://www.newaim.com.au/careers) |
| Office policy | The recoverable Software Engineer posting was **on-site**, permanent, full-time. No remote or hybrid policy is published anywhere on the company site | Unconfirmed posting text; [careers page](https://www.newaim.com.au/careers) |
| Labour hire, Australia | ~40% of total warehouse workers were engaged through four labour-hire agencies in FY22, one of them Sidekicker. In **FY25 New Aim states it did not use labour hire providers in Australia at all** | [FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/), [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| Visa holders | In FY22, approximately **47%** of New Aim's own warehouse employees held working visas; the company completed VEVO checks before commencement and committed to providing documents in workers' own languages | [FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| China workforce | In FY22, fewer than 2% of the China customer-service team were agency workers, via two agencies, paid above the Guangzhou legislated minimum. In FY25, no agency workers were engaged and ~4% of the China workforce was temporary staff | [FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/), [FY25](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| COVID-era arrangements | In FY22, office staff worked remotely per Victorian government requirements; warehouse workers were on site as essential workers | [FY22 statement](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/) |
| Training | Modern slavery training delivered annually to staff in Australia and China through the employee management platform | [FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) |
| Salary, equity, visa sponsorship, turnover, interview process, benefits | Not published for any role | [careers page](https://www.newaim.com.au/careers) |

Two employee-experience facts are on the record from the litigation rather than from company material: as at the period in dispute, New Aim **did not provide employees with work mobile phones**, did not restrict how supplier contact details were stored on personal devices, did not require deletion on departure, and had no mandatory confidentiality agreement covering supplier information ([IP Law Watch, 2025-07-21](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)). The Full Court later found that the identities of 17 specific suppliers were nonetheless confidential and were protected by white-labelling and employee access restrictions ([13 Wentworth Chambers on [2026] FCAFC 49](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)).

---

## Notes

### Not publicly disclosed

Search scope for the findings below (2026-07-30): `www.newaim.com.au` including `robots.txt` (which returns an empty 200) and every page linked from its navigation and footer — home, about-us, technology, brands (both pagination pages), careers, news, partnerships, contact-us, terms-and-conditions, privacy-policy, new-chapter-new-aim, best-managed-companies — plus the `zh-cn` mirrors; `sitemap.xml` returns 404; the `engineering`, `tech`, `blog`, `developers`, `docs`, `api`, `status`, `careers`, `jobs` and `shop` subdomains do not resolve; `www.dropshipzone.com.au` including `robots.txt`, `sitemap.xml`, `about_us`, `press`, `faq`, `policy`, `privacy_statement` and the `apidoc` bundle; `airoxy.ai` including its landing page, plans page, terms of use and published JavaScript bundle; the Australian Business Register; the Australian Modern Slavery Register (all six statements); the Deloitte Private and Google Cloud press rooms; the Google Cloud and Alibaba Cloud customer case studies; GitHub organisation and user searches for `newaim`, `new-aim`, `newaim-it`, `dropshipzone`, `airoxy` and `aimcore`; npm searches for `airoxy` and `dropshipzone`; the Shopify App Store; LinkedIn's company page and the two job links on the careers page; and English and Chinese searches for New Aim funding, the ASX listing, Guangzhou New Aim, New Aim Hong Kong, Werner Liu, and New Aim engineering hiring.

- **No engineering blog, technical article, or architecture material of any kind.** There is no engineering or tech subdomain, no blog on the corporate site, and no conference talk write-up. The published technical detail all comes from the two cloud vendors' case studies and three sponsored articles the company placed with Business News Australia.
- **No open-source presence.** No GitHub organisation exists under any New Aim, Dropshipzone, AirOxy or AimCore name; a `newaim-it` GitHub user account created 2025-06-02 has zero public repositories. The single public artefact is one npm package, `@airoxy/create-react`, last published 2024-02-29.
- **No security certification is named anywhere** — no ISO 27001, SOC 2, PCI DSS, IRAP or equivalent — and there is no security page, trust centre, subprocessor list or status page on any of the three product domains. Cloud Armor is the only named security control.
- **No public documentation for the Dropshipzone Supplier API** announced in August 2022, and no API documentation at all for AirOxy or AimCore. The retailer API documentation on the site was generated in July 2021 and its footer copyright reads "©2012-2020".
- **No salary band, equity, visa-sponsorship statement, interview process, turnover figure, or remote/hybrid policy** is published for any role, including the current Staff Software Engineer opening.
- **No engineering headcount by function or location.** The only breakdown found is "about 70" in IT and data out of about 400, from a media interview, and the statutory statements' description of the Guangzhou subsidiary as supporting "IT and procurement".
- **No audited financial statements are published.** New Aim lodges reports with ASIC — one was quoted for FY21 — but no annual report, balance sheet, or profit figure after FY21 was found in any public source. The Modern Slavery Register bands are the only continuous first-party revenue series.
- **The change of company type from `Pty Ltd` to `Ltd` is unexplained.** No release, filing, or article found announces it, states its date, or connects it to the ASX listing the CEO said the company was contemplating.
- **The 2022 Macquarie mandate has no publicly reported outcome.** Nothing found states whether the raise completed, was withdrawn, or was replaced.
- **No valuation has been disclosed by the company.** The A$280M figure is AFR's 2020 Fast 100 appraisal; Fung Lam's A$1.02bn 2021 Young Rich List entry is an estimate of personal net worth based on his ownership, not a company valuation.
- **Ownership is not disclosed.** No company page or filing found states the current shareholding after the 2021 Werner Liu exit.
- **Neither the current name of the CIO/CTO role nor any CTO is unambiguously identified**; see below.

### Inconsistencies across sources

- **Warehouse space, three live figures.** ~70,000 sqm on the [about](https://www.newaim.com.au/about-us) and [technology](https://www.newaim.com.au/technology) pages, still displayed on 2026-07-30, versus "more than 110,000 sqm" on the company's own [February 2026 page](https://www.newaim.com.au/best-managed-companies) and "more than 120,000 square metres" in [May 2026](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation). Google Cloud says "several warehouses over 100,000 sqm".
- **Units shipped:** "over five million units annually" ([2026-02](https://www.newaim.com.au/best-managed-companies)) versus "around four million units annually" ([2026-05](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)) — the later figure is lower.
- **Household reach:** "more than 60% of Australian households" ([about page](https://www.newaim.com.au/about-us)), "1 in 2 Aussies own a New Aim product" ([homepage](https://www.newaim.com.au/)), "more than one in two households" ([Google Cloud, 2024](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)), and "more than 70% of Australian homes" ([2026-05](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)).
- **Channels:** "more than 40 channels" ([about page](https://www.newaim.com.au/about-us)) versus "more than 30 leading retail channels" ([2026-05](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)) and "over 30 online marketplaces" ([Google Cloud, 2024](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)); 35 in [August 2022](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf) and "more than 40" in [October 2023](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion).
- **SKUs:** 6,000+ across 450+ product lines ([about page](https://www.newaim.com.au/about-us)) versus 7,000+ across 400+ sub-categories ([2025-09](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)); 6,500+ in [2019](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/). Dropshipzone separately advertises "over 100,000 products", which includes third-party supplier listings.
- **Revenue for FY24 and FY25 do not reconcile between sources.** The register declares FY24 at A$350–400M and FY25 at A$300–350M; IBISWorld publishes A$356.6M for "2025" and A$320.5M for "2024" — the same two magnitudes in the opposite year order. IBISWorld may label reports by publication year rather than financial year; neither source states which.
- **Self-funding versus the 2022 raise.** The CEO states the company has "never taken any external equity" ([2025-09](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)). Both statements can be true if the Macquarie process did not complete, but no source confirms that, and The Australian's report of borrowing to fund the 2021 founder settlement and of McGrathNicol being engaged is not addressed anywhere in company material.
- **Carrie Hu's title.** Listed as **CIO** on the [about page](https://www.newaim.com.au/about-us) and 首席信息官 on the [Chinese page](https://www.newaim.com.au/zh-cn/about-us); bylined **"CTO from New Aim"** on [2026-06-09](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human); promoted to **CPO** in September 2024 and called **Chief Product Officer** in the October 2024 CIO50 item ([company news](https://www.newaim.com.au/news)). Separately, Christine Peng holds "CPO" on the about page, rendered as Chief People Officer in Chinese.
- **Alex Ji's title in the same October 2024 news item** is given both as "Our CIO & COO, Alex Ji" and, in the adjacent item, as expanding "his role of COO to also combine CTO" ([company news](https://www.newaim.com.au/news)).
- **Cecilia Chiu's title** appears as COO on the current about page, Chief Strategy Officer in the Google Cloud case study and 2022 press, and CSO in 2023–24 award notices ([about page](https://www.newaim.com.au/about-us), [Google Cloud case study](https://cloud.google.com/customers/new-aim), [company news](https://www.newaim.com.au/news)).
- **Founding date:** 2005 per the company and 2005-08-22 per IBISWorld, with the ABN active from 2005-09-02, against Fung Lam's own "started as an eBay store in 2003" ([Stockland, 2023-10-24](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)) and "eBay only started in 1999, and I was using it from probably 2003" ([The Australian, 2022-03-25](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf)).
- **How many founders.** The current about page names two co-founders, Fung Lam and Cecilia Chiu. CEO Magazine describes Fung Lam investing in New Aim "with Werner Liu", and the 2020 AFR Young Rich List entry listed Lam and Liu jointly as "founders and executive directors". Werner Liu appears on no current company page.
- **Dropshipzone's corporate status:** the Google Cloud release calls it a "subsidiary B2B2C marketplace", while the ABN register records `dropshipzone` as a business name of New Aim's own ABN and the Dropshipzone privacy statement says New Aim Ltd owns and operates it. No separate Dropshipzone legal entity was found.
- **AirOxy pricing versus its own FAQ.** The [plans page](https://airoxy.ai/home/plans) lists A$29 and A$79 monthly tiers while the landing-page FAQ on the same site says "AirOxy is free for a limited time!" (both accessed 2026-07-30).
- **Deloitte award year labelling.** The company's [news page](https://www.newaim.com.au/news) files the award under February 2026 as "Australia's 2025 Best Managed Companies"; Deloitte's release naming New Aim is dated [2026-02-27](https://www.deloitte.com/au/en/about/press-room/deloitte-best-managed-companies-awards-270226.html) and also calls it the 2025 cohort.

### Other

- **The litigation record is the most detailed independent account of how New Aim operates.** *New Aim Pty Ltd v Leung* concerns a former employee alleged to have disclosed the identity and contact details of New Aim's Chinese product suppliers to competitors, pleaded as breach of contract, breach of confidence, and contravention of s 183 of the Corporations Act 2001 (Cth). The sequence:
  - **[2022] FCA 722** — the primary judge rejected New Aim's expert evidence in its entirety after findings about how the solicitors prepared the report ([KHQ Lawyers](https://www.khq.com.au/blog/2023/08/28/new-aim-full-court-clarity-expert-evidence/)).
  - **[2023] FCAFC 67** — the Full Court unanimously overturned that decision and ordered a retrial before a different judge, holding that practitioner involvement in drafting expert evidence is not objectionable in itself ([KHQ Lawyers](https://www.khq.com.au/blog/2023/08/28/new-aim-full-court-clarity-expert-evidence/), [Mondaq](https://www.mondaq.com/australia/disclosure-electronic-discovery-privilege/1322382/expert-evidence-new-aim-pty-ltd-v-leung-2023-fcafc-67)).
  - **[2025] FCA 747** (*No 4*) — on retrial the Court held that the identity and contact details of all New Aim's suppliers as at January 2021 lacked the necessary quality of confidence, noting that employees were not given work phones, that storage of supplier contacts on personal devices was unrestricted, that deletion on departure was not required, and that no confidentiality agreement specific to supplier information was in place ([IP Law Watch, 2025-07-21](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)).
  - **[2026] FCAFC 49** (2026-04-20, Moshinsky, Thawley and Button JJ) — the Full Court allowed New Aim's appeal on a narrower case concerning **17 specific suppliers**, holding that their identity and contact details were confidential, that they were reliable current suppliers suitable to the Australian market whose identification "would require substantial effort and time", that New Aim protected the information through white-labelling and employee access restrictions, and that Mr Leung breached both his contractual confidentiality obligation and s 183. Claims against two competitor respondents were remitted ([13 Wentworth Chambers](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)). A costs judgment followed as **[2026] FCAFC 79** on 2026-06-01.
- **The company's public technical writing is placed as sponsored content.** Three of the four Business News Australia items cited here are labelled "Member news brought to you by" New Aim or one of its executives; the September 2025 listing story is a journalist-written article by Nick Nichols. The technical detail in the sponsored items is the most specific the company has published anywhere.
- **The corporate site was rebuilt in 2024 and migrated platforms.** The brand identity was refreshed in October 2024 with Christopher Doyle & Co ([Mumbrella](https://mumbrella.com.au/new-aim-refreshes-brand-identity-855087)); archived pages show a WordPress site as recently as December 2025, and the live site is Webflow. Older URLs such as `/about_us/` and `/careers/` are still referenced from the AirOxy terms of use and from third-party pages.
- **Statutory supplier-mix figures moved materially between FY22 and FY25.** DSZ suppliers rose from ~17% to ~24% of total suppliers, Australian operational-support vendors fell from ~33% to ~25%, China operational-support vendors rose from ~5% to ~7%, and in-house-brand product suppliers fell from ~45% to ~42% ([FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/), [FY25](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)).
- **Supplier questionnaire coverage jumped in FY25:** questionnaires issued to ~96% of first-tier suppliers with ~46% responding, described by the company as a nine-fold increase on FY24. Roughly one third of product suppliers supply timber products, all assessed under the Timber Due Diligence policy ([FY25 statement](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/)).
- **The eBay business remains a named channel after 21 years.** OzPlaza was described in 2019 as accounting for about a quarter of revenue ([CEO Magazine](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)); eBay is still listed as a marketplace in the FY25 filing.
- **An `airoxyproductlensdev` Azure Blob Storage host appears in the published AirOxy bundle**, alongside the Google Cloud-only positioning in the 2024 release. The name suggests a development environment for a "product lens" feature; no company material mentions Azure or a feature by that name.

---

## Resources

Every link below was checked on 2026-07-30. Four sources returned HTTP 403 to automated requests while remaining human-accessible, and their content was therefore not independently verified here: the four `ft.com` High-Growth Asia-Pacific ranking pages, the Monash University AUBCC item, and the Mumbrella brand-identity article. `austlii.edu.au` and `judgments.fedcourt.gov.au` both refuse automated access, so the four judgments are cited through law-firm and barristers' case notes rather than the judgment text; the AFR and The Australian articles are paywalled, and the two articles from The Australian are cited from the PDF copies New Aim hosts on its own CDN.

**Official**

- [New Aim — www.newaim.com.au](https://www.newaim.com.au/) · [About Us](https://www.newaim.com.au/about-us) · [Technology](https://www.newaim.com.au/technology) · [Brands](https://www.newaim.com.au/brands) · [Careers](https://www.newaim.com.au/careers) · [News](https://www.newaim.com.au/news) · [Partnerships](https://www.newaim.com.au/partnerships) · [Contact](https://www.newaim.com.au/contact-us)
- [Terms and Conditions](https://www.newaim.com.au/terms-and-conditions) · [Privacy Policy](https://www.newaim.com.au/privacy-policy)
- [CEO transition announcement — Fung Lam hands over to Alex Ji, effective 2025-06-01](https://www.newaim.com.au/new-chapter-new-aim)
- [Best Managed Companies page, February 2026](https://www.newaim.com.au/best-managed-companies)
- [Chinese-language site](https://www.newaim.com.au/zh-cn/about-us) (ZH)
- [Dropshipzone](https://www.dropshipzone.com.au/) · [About](https://www.dropshipzone.com.au/about_us) · [Press](https://www.dropshipzone.com.au/press) · [FAQ](https://www.dropshipzone.com.au/faq) · [Marketplace policies](https://www.dropshipzone.com.au/policy) · [Privacy statement](https://www.dropshipzone.com.au/privacy_statement) · [robots.txt](https://www.dropshipzone.com.au/robots.txt)
- [Dropshipzone API documentation](https://www.dropshipzone.com.au/apidoc/index.html) · [api_data.json](https://www.dropshipzone.com.au/apidoc/api_data.json) · [api_project.json](https://www.dropshipzone.com.au/apidoc/api_project.json)
- [AirOxy](https://airoxy.ai/) · [Plans](https://airoxy.ai/home/plans) · [Terms of Use, last updated 2025-10-29](https://airoxy.ai/home/terms_of_use)
- [Dropshipzone Shopify app, launched 2020-05-15](https://apps.shopify.com/newaim_app)
- [npm — @airoxy/create-react](https://registry.npmjs.org/@airoxy/create-react)
- [LinkedIn — New Aim](https://au.linkedin.com/company/new-aim)

**Statutory filings and registries**

- [ABN Lookup — NEW AIM LTD, ABN 50 115 804 432](https://abr.business.gov.au/ABN/View?abn=50115804432)
- [Australian Modern Slavery Register — New Aim statements](https://modernslaveryregister.gov.au/statements/?q=new+aim)
- [FY25 statement PDF](https://modernslaveryregister.gov.au/statements/yczA8cUKpTPqZDt/pdf/) · [FY24](https://modernslaveryregister.gov.au/statements/EYGKd5LS8DZJJ45/pdf/) · [FY22](https://modernslaveryregister.gov.au/statements/LxKwvVqIVnCwncY/pdf/)
- Register entries: [FY20](https://modernslaveryregister.gov.au/statements/11261/) · [FY21](https://modernslaveryregister.gov.au/statements/11270/) · [FY22](https://modernslaveryregister.gov.au/statements/11271/) · [FY23](https://modernslaveryregister.gov.au/statements/16116/) · [FY24](https://modernslaveryregister.gov.au/statements/21077/) · [FY25](https://modernslaveryregister.gov.au/statements/26345/)

**Vendor case studies and press releases**

- [Google Cloud — New Aim case study](https://cloud.google.com/customers/new-aim)
- [Google Cloud press release, 2024-09-11 — New Aim Taps Google Cloud](https://www.googlecloudpresscorner.com/2024-09-11-New-Aim-Taps-Google-Cloud-to-Democratise-Access-to-Generative-AI-and-Big-Data-for-Australian-Retailers)
- [Alibaba Cloud — New Aim case study](https://www.alibabacloud.com/en/customers/new-aim) (undated; accessed 2026-07-30)
- [Alibaba Cloud — notice on ceasing operation of Australian and Indian data centers](https://www.alibabacloud.com/en/notice/notice_on_the_ceasing_operation_of_alibaba_cloud_data_centers_in_australia_and_india_351)
- [Stockland media release, 2023-10-24 — Melbourne Business Park lease](https://www.stockland.com.au/media-centre/media-releases/2023/october/growth-for-melbourne-business-park-with-new-aim-e-commerce-expansion)
- [RMIT University, 2025-06 — AI-driven e-commerce research partnership](https://www.rmit.edu.au/news/ccsri/enhance-ai-driven-ecommerce-solutions)
- [Deloitte Australia, 2026-02-27 — Best Managed Companies awards](https://www.deloitte.com/au/en/about/press-room/deloitte-best-managed-companies-awards-270226.html)
- [Monash University, 2025 — AUBCC case competition](https://www.monash.edu/business/news/2025/bright-ideas-shine-at-global-business-challenge)
- [iTWire, 2024-09 — New Aim taps Google Cloud](https://itwire.com/business-it-news/data/new-aim-taps-google-cloud-to-democratise-access-to-generative-ai-and-big-data-for-australian-retailers) · [IT Brief](https://itbrief.com.au/story/new-aim-leverages-google-cloud-to-boost-ai-in-ecommerce)

**Third-party coverage and profiles**

- [Business News Australia, 2025-09-29 — New Aim eyes potential listing to drive plans for a new AI-driven retail ecosystem (journalist-written)](https://www.businessnewsaustralia.com/articles/new-aim-potential-listing-online-ecommerce-ecosystem.html)
- [Business News Australia, 2026-05-01 — How New Aim engineered Australia's largest big and bulky e-commerce operation (sponsored member news)](https://www.businessnewsaustralia.com/blog/how-new-aim-engineered-australia-s-largest-big-and-bulky-e-commerce-operation)
- [Business News Australia, 2026-06-09 — The next customer on your website won't be human, by Carrie Ruan Hu (sponsored member news)](https://www.businessnewsaustralia.com/blog/the-next-customer-on-your-website-won-t-be-human)
- [Business News Australia, 2025-12-19 — The growing divide in Australia's e-commerce market, by Cecilia Chiu (sponsored member news)](https://www.businessnewsaustralia.com/blog/the-growing-divide-in-australia-s-e-commerce-market)
- [The Australian, 2022-08-15 — Macquarie seeks $100m for 'retail's best kept secret' (PDF hosted by New Aim)](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43543b37bf9feedeeab91a_The-Australian-100m-aim-for-%E2%80%98retails-best-kept-secret.pdf)
- [The Australian, 2022-03-25 — Fung Lam's New Aim is changing Australian retail (PDF hosted by New Aim)](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a43548e6bf58fb88142db59_The-Australian-%E2%80%93-Fung-Lams-New-Aim-is-changing-Australian-retail.pdf)
- [The Australian / IBISWorld Top 500 Private Companies 2022 (PDF hosted by New Aim)](https://cdn.prod.website-files.com/6a206336a6ba902f217f8873/6a434bf99103902761316fdd_The-Australian-Top-500-Private-Companies_2022.pdf)
- [CEO Magazine, December 2019 — Fung Lam interview](https://www.theceomagazine.com/executive-interviews/retail-wholesale/fung-lam/)
- [Power Retail, 2022-07 — 20 questions with Cecilia Chiu](https://powerretail.com.au/20-questions-with-cecilia-chiu-co-founder-of-new-aim/) · [Power Retail, 2022-10 — 'Become a Superman'](https://powerretail.com.au/become-a-superman-tips-for-success-from-one-of-australias-richest-men/)
- [Internet Retailing, 2018-09 — Aussie seller cracks eBay benchmark](https://internetretailing.com.au/aussie-seller-cracks-ebay-benchmark/)
- [Retailbiz, 2022-08 — Dropshipzone delivers new API for data integration](https://www.retailbiz.com.au/online-retailing/dropshipzone-delivers-new-api-for-data-integration/)
- [Mumbrella, 2024-10 — New Aim refreshes brand identity](https://mumbrella.com.au/new-aim-refreshes-brand-identity-855087)
- [CIO Australia — CIO50 2024 awards](https://www.cio.com/article/3568346/australias-leading-it-executives-honoured-at-cio50-2024-awards.html) · [Alex Ji awardee profile](https://www.cio.com/awardee/3558026/alex-ji.html)
- [IBISWorld — New Aim Pty Ltd company profile](https://www.ibisworld.com/australia/company/new-aim-pty-ltd/450509/)
- [FT / Statista High-Growth Companies Asia-Pacific 2023](https://www.ft.com/high-growth-asia-pacific-ranking-2023) · [2022](https://www.ft.com/high-growth-asia-pacific-ranking-2022) · [2021](https://www.ft.com/high-growth-asia-pacific-ranking-2021) · [2020](https://www.ft.com/high-growth-asia-pacific-ranking-2020)
- [AFR Fast 100 2020](https://www.afr.com/work-and-careers/management/fast-100-and-fast-starters-winners-revealed-20200219-p54269) · [Fast 100 2018](https://www.afr.com/work-and-careers/careers/financial-review-fast-100-2018-the-full-list-20181030-h179hx) · [Top 500 Private Companies 2019](https://www.afr.com/policy/economy/australia-s-top-500-private-companies-revealed-20190902-p52n8c) · [Young Rich List](https://www.afr.com/young-rich)

**Litigation**

- [13 Wentworth Chambers — New Aim Pty Ltd v Leung [2026] FCAFC 49 (2026-04-20, Moshinsky, Thawley and Button JJ)](https://13wentworth.com.au/new-aim-pty-ltd-v-leung-2026-fcafc-49-20-april-2026-moshinsky-thawley-and-button-jj/)
- [IP Law Watch, 2025-07-21 — New Aim misses the mark: New Aim Pty Ltd v Leung (No 4) [2025] FCA 747](https://www.iplawwatch.com/2025/07/21/new-aim-misses-the-mark-federal-court-clarifies-what-constitutes-confidential-information/)
- [KHQ Lawyers, 2023-08-28 — New Aim: Full Court provides clarity on expert evidence ([2023] FCAFC 67, [2022] FCA 722)](https://www.khq.com.au/blog/2023/08/28/new-aim-full-court-clarity-expert-evidence/)
- [Mondaq — Expert evidence: New Aim Pty Ltd v Leung [2023] FCAFC 67](https://www.mondaq.com/australia/disclosure-electronic-discovery-privilege/1322382/expert-evidence-new-aim-pty-ltd-v-leung-2023-fcafc-67)
- [Victorian Bar Commercial Bar Association digest — New Aim Pty Ltd v Leung](https://www.vicbar.com.au/Web/Web/Contents/Associations/Commercial/Digest/new-aim-pty-ltd-v-leung.aspx)

**Web archive**

- [Careers page, archived 2025-12-14](http://web.archive.org/web/20251214072201/https://www.newaim.com.au/careers/) · [2025-10-06](http://web.archive.org/web/20251006230929/https://www.newaim.com.au/careers/) · [2025-03-15](http://web.archive.org/web/20250315202431/https://www.newaim.com.au/careers/)
