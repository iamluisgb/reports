---
title: "What AI Startups Stole From Palantir's Playbook"
date: 2026-05-29
type: special
url: https://luisgonzalezbernal.com/reports/reports/palantir-playbook-2026.html
summary: "The playbook · The market map · What an FDE does · The economics · Ontology platforms · Why deployments fail"
tags: [business, funding]
reading_time_minutes: 21
---
Market Analysis · Special Report

# What AI Startups Stole From *Palantir's Playbook*

29 May 2026 · Updated 11 Nov 2026

The playbook · The market map · What an FDE does · How to run an engagement · The economics · Ontology platforms · Why deployments fail

## Key findings

1. **The model labs bought the playbook.** OpenAI launched a Deployment Company with more than $4 billion of initial investment to embed forward deployed engineers (FDEs) in customers.[42] Its founding acquisition, Tomoro, brought roughly 150 FDEs and deployment specialists.[42] Anthropic launched a services company with about $1.5 billion committed and bought Fractional AI.[61]
2. **Big tech followed.** AWS put $1 billion into a dedicated FDE organization, and Google Cloud and Microsoft made similar moves.[32] FDE job postings rose 800–1000% in a year.[73]
3. **The original still works.** Palantir's Q3 2026 revenue grew 96% to $2.313 billion.[5] US commercial revenue grew 148% to $984 million, with a 47% GAAP operating margin.[5] In Q2 2026 it closed 220 deals of at least $1 million, and net dollar retention was 157%.[2]
4. **The playbook is now an industry.** Salesforce committed to a team of 1,000 FDEs.[56] Accenture and Google Cloud plan a 1,000-person FDE workforce for Gemini Enterprise.[21] Salesforce's FDE partner network covers over 30 firms, including Accenture, Deloitte and PwC.[44]
5. **Most copies take the engineers, not the platform.** a16z says Palantir works because a real platform sits under the bespoke work.[73] Copying only the embedded engineers produces thousands of bespoke deployments that are hard to maintain.[73] OpenAI's Deployment Company has announced no software product; in October 2026 it was hiring a lead for internal products.[47]
6. **Pricing is moving to outcomes.** Sierra charges per AI-resolved case and makes human escalations free, so it loses revenue when its agent fails.[72] AWS says its FDE deployments are tied to business results, not billable hours.[18]
7. **The craft is converging on one engagement shape.** Playbooks agree on diagnosis, scoping, a prototype on real data, evals, production and handoff.[77,35] OpenAI aims for 20% reusable components in a first engagement and 50% in the next two or three.[40]
8. **Margin is the price of the model.** Compiled benchmarks put AI products at 45% gross margin in 2025, against an 80% SaaS median.[70] ServiceNow went from 63.2% at IPO to 79% in 2024.[64]
9. **Deployment is the bottleneck, but not only for lack of people.** MIT NANDA found 95% of organizations get zero return from GenAI.[3] It names learning as the core barrier, not infrastructure, regulation or talent.[3] External partnerships succeed twice as often as internal builds.[3]

## Part I

## The playbook, as Palantir describes it

Palantir has two big engineering roles. "Devs" build the product; "Deltas", its forward deployed software engineers, deploy it for one customer each.[62] Palantir sums it up as "one capability, many customers" against "one customer, many capabilities".[62] Deltas sit in Business Development and are mandated to achieve technical outcomes.[62]

Deltas work with Deployment Strategists, known as Echos. In theory Echos are more like product managers and Deltas more technical; in practice both roles blend.[54] Palantir built the model in the early 2010s, when intelligence customers could not disclose their needs through normal product discovery.[66] By 2016, FDEs outnumbered traditional software engineers.[66]

The field work feeds the product. Deltas contribute code back to the core platform when a missing feature blocks a customer outcome.[62] One account calls this loop the "gravel road to paved highway": custom work becomes standard product features.[66] Without that discipline, the same source says, the model becomes unscalable custom work.[66]

*[Palantir's loop turns field work into platform features; a copy without a platform turns field work into bespoke deployments to maintain]*

*The difference between the original and most copies. Built from sources 52, 55 and 60.*

The engagement has stages. Deltas embed with a customer for 6 to 18 months to put Foundry and AIP into production.[48] Each is paired with an Echo, and work runs through three phases: Acquire, Expand and Scale.[48] Palantir absorbs the pilot costs and develops early use cases at a loss before it reaches positive contribution margin.[48] Contracts are custom, with no published list prices.[48]

The sale starts small. Contracts begin with a bootcamp and limited licenses, and grow use case by use case if value is proven.[73] Over time the revenue mix tilts toward software subscription rather than services.[73] In an AIP Bootcamp, participants go from zero to a use case in one to five days.[39] Pricing is a fixed fee, with no traditional SKUs.[73] By February 2024, Palantir had run more than 560 bootcamps across 465 organizations.[48]

Under the bootcamp sits the ontology. It maps datasets, virtual tables and models to business objects such as plants and orders.[38] It also defines the actions that people and AI agents may take.[38] Since June 2026, an Ontology MCP server exposes object types, actions and functions as tools for agents.[38]

- **$2.313B** Q3 2026 revenue, up 96% year over year

Palantir, SEC filing[5]

- **+148%** US commercial revenue growth, to $984 million

Q3 2026[5]

- **157%** net dollar retention

Q2 2026[2]

- **220** deals of at least $1 million in one quarter; 73 of at least $10 million

Q2 2026[2]

The ontology now reaches the public sector at scale. Palantir cites the USDA using AIP to turn hundreds of fragmented legacy systems into a single governed ontology.[2]

## Part II

## Who is copying it: the market map

The copies fall into five groups: model labs, hyperscalers and platforms, consultancies, FDE-native startups, and Palantir's own ecosystem. The tables give one signal per company and a link to research further.

### Model labs and their deployment arms

| Company | What they did | Signal | Link |
| --- | --- | --- | --- |
| OpenAI Deployment Company | Embeds FDEs inside customers to redesign workflows[42] | $4B+ committed; $14B post-money; 19 partner firms[47,42] | [openai.com](https://openai.com/index/openai-launches-the-deployment-company/) |
| Tomoro (now part of OpenAI) | Applied AI consulting and engineering firm[42] | About 150 FDEs; Supercell support system cut cost per ticket by 90%[80,47] | [tomoro.ai](https://tomoro.ai) |
| Northslope (now part of OpenAI) | AI applications on Palantir AIP, Foundry and Gotham; founded by former Palantir FDEs; acquired by OpenAI's Deployment Company[27,47] | Revenue up nearly 7x in a year; Palantir's first Vanguard: Elite partner[27] | [northslope.com](https://www.northslope.com/) |
| Ode (Anthropic, Blackstone, Hellman & Friedman) | Embeds small teams of applied AI engineers; Claude-first, not Claude-exclusive[29] | About $1.5B committed; launched with about 100 engineers[61,29] | [blackstone.com](https://www.blackstone.com/news/press/the-ai-native-enterprise-services-firm-backed-by-anthropic-blackstone-and-hellman-friedman-announces-acquisition-of-fractional-ai/) |
| Fractional AI (now part of Ode) | Applied AI services firm founded in 2024[16] | Founding operational centerpiece of Ode[16] | [fractional.ai](https://www.fractional.ai/) |
| Anthropic Applied AI | FDEs embedded with strategic customers[11] | Builds MCP servers, sub-agents and agent skills[11] | [anthropic.com](https://www.anthropic.com/careers) |

### Hyperscalers and software platforms

| Company | What they did | Signal | Link |
| --- | --- | --- | --- |
| AWS | Forward Deployed Engineering organization; pods of five to six engineers plus agents[18,28] | $1B investment; customers include the NFL, the NBA and Southwest Airlines[18] | [aboutamazon.com](https://www.aboutamazon.com/news/aws/aws-1-billion-forward-deployed-ai-engineers) |
| Salesforce | FDEs for Agentforce, plus an FDE partner network[56,44] | Team of 1,000 FDEs; partners drove one-third of successful Agentforce implementations[56,44] | [salesforce.com](https://www.salesforce.com/news/stories/salesforce-launches-forward-deployed-engineer-partner-network-announcement/) |
| Google Cloud | FDE programs through partners for Gemini Enterprise[21,15] | Accenture group with a 1,000-person FDE workforce[21] | [accenture.com](https://newsroom.accenture.com/news/2026/accenture-and-google-cloud-deepen-partnership-with-formation-of-new-accenture-gemini-enterprise-business-group) |
| Microsoft | AI-deployment organization; FDE practice with Accenture[32,28] | Organization staffed with thousands[32] | [microsoft.com](https://www.microsoft.com) |

### Consultancies and integrators

| Company | What they did | Signal | Link |
| --- | --- | --- | --- |
| Accenture ← Faculty | Bought a UK AI-native services and products firm, founded in 2014[22,23] | 400+ AI professionals; reported $1B headline price[22,61] | [faculty.ai](https://faculty.ai) |
| Cognizant | Gemini Enterprise practice with FDEs embedded in client environments[15] | Google Cloud Diamond partner[15] | [cognizant.com](https://news.cognizant.com/2026-04-22-Cognizant-Google-Cloud-Diamond-Partnership-Gemini-Enterprise-Practice) |
| Fujitsu | Global Forward Deployed Engineering partner of Palantir[48] | New AIP and Foundry agreement, September 2026[48] | [fujitsu.com](https://www.fujitsu.com) |
| Sigmoid | FDEs paired with prebuilt production agents; one engineer orchestrates many agents[59] | Says it has used the model for a decade[59] | [sigmoid.com](https://www.sigmoid.com/forward-deployed-engineering/) |

### FDE-native startups

| Company | What they do | Signal | Link |
| --- | --- | --- | --- |
| Distyl AI | Enterprise AI firm founded in 2022 by former Palantir employees[31] | Valued at $1.8B in September 2025[31] | [distyl.ai](https://distyl.ai) |
| Invisible Technologies | Platform plus FDEs; starts with one workflow and expands[82] | $134M revenue in 2024[36] | [invisibletech.ai](https://invisibletech.ai) |
| Sierra | Customer-service agents; forward-deployed agent engineers own the last mile[72] | Paid per resolved case; contracts start around $150,000 a year[72] | [sierra.ai](https://sierra.ai) |
| Decagon | Support agents implemented by human Agent Product Managers[64] | Sizable implementation team[64] | [decagon.ai](https://decagon.ai) |
| H Company | Pivot toward FDEs under a former Palantir France CEO[86] | CEO change in June 2025[86] | [hcompany.ai](https://www.hcompany.ai) |
| Ramp | Fintech with an FDE team for enterprise customers[65] | Grew from 2 to 16 FDEs; 7 were former founders[65] | [ramp.com](https://builders.ramp.com/post/forward-deployed-engineering) |

### Palantir's own ecosystem

Palantir's alumni are a source of copies in their own right. One public dataset counts 335 former Palantir employees who became founders.[30] Their companies include Anduril, valued at $30.5 billion, and ElevenLabs, valued at $6.6 billion.[30] Another count found 39 alumni startups that raised more than $6 billion.[33] Palantir also markets partners that put AI FDEs at the center of their work, under its Vanguard: Elite label.[57]

The labs say why they copy. OpenAI calls deployment, not model capability, the binding constraint on enterprise value.[42] Ode's thesis is that the moat is process rewiring, not tokens.[29] Anthropic's CFO said enterprise demand for Claude is outpacing any single delivery model.[29]

## Part III

## What an FDE actually does

The job is integration more than invention. In Plank's census of 904 FDE job descriptions, 51% ask for API integration work and 27% for data pipelines.[55] At a startup, FDEs map customer data into the product, build customer-specific workflows, run evaluations on customer data and roll out to production.[55]

The role is not a sales engineer. A solutions engineer helps win the deal before signature; an FDE delivers production code after it and is accountable for whether it works.[55] Anthropic's FDE role lists MCP servers, sub-agents and agent skills as deliverables, with 25–50% travel to customer sites.[11] At Salesforce, some FDEs work in pods of one deployment strategist and two engineers.[56]

The people are often builders. At Ramp, 7 of its 16 FDEs were former founders.[65] Palantir describes its Deltas as spending a couple of days most weeks at customer premises.[62]

The signs that a company needs FDEs are specific. The product works in demos, but each customer needs engineering to run it in their systems.[55] Deals close, but deployments stall or never go live.[55] Pilots succeed but do not turn into production contracts.[55]

## Part IV

## The FDE playbook: an engagement, step by step

Practitioner playbooks use different names but agree on the shape. One lists six phases: discovery, MVP scoping, prototyping on real data, an evaluation framework, production, and continuous improvement.[77] Another uses four: understand, build, validate, and deploy and transfer.[35] An engagement usually takes weeks to a few months, not days.[81]

*[An FDE engagement in six phases, from diagnosis to handoff, with field work fed back into the product]*

*The common shape of an engagement. Timings from AWS, Per Aspera and Perspective AI; reuse targets from OpenAI. Built from sources 17, 40, 50, 77 and 79.*

### 1. Diagnose and scope

OpenAI's engagements start with a diagnostic and then pick a few priority workflows with customer leadership.[42] Its FDE team targets problems worth tens of millions to low billions.[40] Discovery should end with a specific, falsifiable definition of success, not a mission statement.[77] The FDE names what is out of scope for phase one and gets the customer to agree before building.[77]

Two scoping mistakes recur. Teams under pressure skip discovery and build the wrong thing fast.[50] And they do not decide early whether the work is a prototype or a production build.[35] Overengineering a prototype wastes time; underengineering production creates a liability.[35] OpenAI names its most significant anti-pattern: generalizing too early, before understanding specific customer problems.[40]

### 2. Prototype on real data

The prototype runs on the customer's actual, messy data from day one, so integration problems surface early.[77] One playbook aims for a live demo within 10 days, with real data as the specification.[79] AWS runs a 45-minute ideation, a 45-hour validation and a 45-day path to production.[17]

The state of the art favours simple designs. Anthropic recommends the simplest solution first, which may mean no agent at all.[14] Workflows with predefined code paths suit well-defined tasks; agents suit tasks that need flexibility.[14] The most successful implementations used simple, composable patterns, not complex frameworks.[14] Tools need care too: too many or overlapping tools distract agents.[20] Replacing raw IDs with meaningful names improved retrieval precision.[20]

### 3. Evaluate before you trust it

Evals are where the field has moved most. Hamel Husain's rule is error analysis first: read real conversations in a spreadsheet, then write tests for the failures you saw.[67] Generic metrics such as coherence often miss what matters for a use case.[67] He recommends binary pass/fail judgements over 1–5 ratings.[71]

Anthropic describes three kinds of graders: code-based, model-based and human.[12] Teams without evals find problems only in production, and need weeks of testing when a new model arrives.[12] Teams with evals can upgrade in days.[12] Sierra turns annotated failures into regression tests and runs every customer's suite before a platform upgrade.[72]

Evals also mark progress with the customer. In one OpenAI telecom engagement, the key eval rose from around 60% to 80%, then above 90%, over six months.[13] In a semiconductor engagement, OpenAI's FDEs built labeled sets of human debugging sessions of about 20 actions each.[40]

### 4. Ship, then stay for adoption

Building is often the short part. At Morgan Stanley, the core pipeline worked in six to eight weeks.[40] Adoption took four more months of piloting and evaluation, and reached 98% of advisors.[40] The first two to three weeks after go-live reveal the edge cases and shape user trust.[77] Salesforce's FDEs stay after launch to monitor agents and fix production-only issues.[44] Anthropic advises sandboxed testing and guardrails, because agent errors compound.[14]

### 5. Hand over

A good engagement ends with the customer able to run it. AWS customers keep the systems, runbooks, architecture documents and trained internal champions.[17] Their engineers move from observers to co-builders to autonomous operators.[17] One playbook sets the handoff within 120 days of go-live, with documentation, coaching and transfer to customer success.[50] Another moves ownership at cutover, after gates such as single sign-on, a migration dry-run and training.[43]

### 6. Feed the product

This is the step that separates the model from consulting. By day 90, an engagement should merge at least one generalized feature into the core product.[50] OpenAI aims for 20% reusable components in a first engagement and 50% in the next two or three.[40] It removed roughly 90% of custom code per project as it standardized workflows.[13] In one case, the first deployment took two months and the extension to a second team took one day.[13]

AWS builds the same asset in its partner programme: a reusable harness of domain ontologies, evaluation frameworks, MCP servers and a context graph.[63] FDE teams are measured on what returns to the product, not on billable hours.[50] OpenAI funds its FDEs as bets on future product revenue and can refuse lucrative but misaligned work.[40]

### How engagements are sold

The commercial formats follow the phases. One AWS partner sells a fixed-price assessment that ends in a working proof of concept on customer data.[51] It then sells a fixed-price production outcome with an optional success bonus, and a monthly retainer for operation.[51]

## Part V

## The economics: margin for moat, or consulting by another name

The case for the model is a16z's "trading margin for moat". At IPO, ServiceNow and Workday had gross margins of 63.2% and 54.1%.[64] By 2024 they reached 79% and 75%.[64] a16z tells AI startups to grow total gross profit, not to optimize for an 80% gross margin.[64] It even suggests selling services at cost.[64]

The current numbers are far from software margins. Compiled benchmarks put AI products at 45% gross margin in 2025, with 53% expected in 2026.[70] An FDE is expensive. Anthropic advertises £225,000 to £255,000 a year for one in London.[11] One analysis models a fully loaded frontier-lab FDE at $845K a year.[70]

Who pays for the engineers varies. Palantir absorbs pilot costs upfront rather than billing time and materials.[48] Salesforce offers its FDE program free to selected nominated customers, and plans to sell it later.[56] AWS frames its deployments around shared goals and business results, not billable hours.[18]

Deal size decides whether that cost pays. In one illustrative model, $3M–15M enterprise contracts cover an FDE 2.5 to 6 times.[70] Deals under $500K cover well under half of one.[70] That is a model, not measured data, but it explains why FDEs go to the largest accounts. CRV reaches the same conclusion: the unit economics work only at high deal sizes.[68]

### Outcome pricing

Some companies tie price to results. Sierra charges a pre-negotiated rate per AI-resolved case, about $1.50, and human escalations are free.[72] Every failed resolution therefore costs Sierra revenue and compute.[72] Fin AI lists $0.99 per successful resolution.[78] Demand is ahead of contracts: 76% of enterprise CX buyers are open to outcome pricing, but only 5% were contracted on it.[78]

Outcome pricing makes the vendor accountable until the customer can use the product.[72] It also squeezes margins, so Sierra is trying to productize the last mile with tools that build agents from procedures and transcripts.[72]

The firms that were bought look like good services businesses. One estimate puts Tomoro at about £225k revenue per head, with margins above 40%.[61] Faculty's reported price was about 15 times its run-rate revenue.[61] The buyers paid for teams and clients, not for models or research.[61]

So is it consulting? Palantir's Deltas say no: consultants deliver one-time analyses, while Deltas deploy existing software products.[62] That defence needs a product. TBR expects Palantir to remain an exception, not the template for an industrywide shift.[69] For vendors, it says, FDE support is likely a loss leader paid for by software or cloud consumption.[69] Systems integrators cannot recover it that way and must bill it as services.[69]

CRV gives a simple test for drift into services. Custom engineering effort per customer should decline over time.[68] If one-off systems do not generalize back into the product, the model becomes services work.[68]

## Part VI

## The ontology: what competitors offer

Palantir's platform is several products. Foundry handles data operations and the ontology; AIP connects generative AI on top of it.[49] Gotham serves defense and intelligence, and Apollo delivers software to any environment, even air-gapped ones.[49] No single product replaces all four equally well.[49]

The ontology itself is hard to swap. Palantir's ontology and the open W3C standards (OWL, RDF, SHACL) are not supersets of each other.[38] OWL lacks permissioned actions, and Foundry is not built around open-world inference.[38] One user-built converter found that 7 of 22 Palantir property types had no counterpart in any published standard.[38] Moving the data out does not move its meaning or logic.[49]

| Platform | What it is | Link |
| --- | --- | --- |
| Palantir Foundry Ontology | Semantic objects, properties and links plus kinetic actions and functions[53] | [palantir.com](https://www.palantir.com/platforms/ontology/) |
| Microsoft Fabric IQ | Ontology preview: a virtual semantic layer over source systems, generated from Power BI models[19] | [learn.microsoft.com](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview) |
| Stardog | RDF/OWL knowledge graph; a virtual graph engine federates queries across 20+ databases without ETL[45,46] | [stardog.com](https://www.stardog.com/) |
| d.AP (Digetiers) | AI context platform with ontology-guided context assembly for agents[52] | [digetiers.com](https://www.digetiers.com/) |
| eccenca Corporate Memory | Ontology-first knowledge graph for integration, modeling and governance[52,46] | [eccenca.com](https://eccenca.com/) |
| Graphwise (GraphDB) | RDF database for packaged semantic search and GraphRAG[46,52] | [graphwise.ai](https://graphwise.ai/) |
| Fluree | Verifiable knowledge graph with an immutable ledger and triple-level access control[46] | [flur.ee](https://flur.ee/) |
| Neo4j | Property-graph platform without native ontology reasoning[46,45] | [neo4j.com](https://neo4j.com/) |
| Amazon Neptune | Managed graph service, three query languages across two graph models[46] | [aws.amazon.com/neptune](https://aws.amazon.com/neptune/) |
| Timbr | Semantic layer positioned as an alternative to both Palantir and Stardog[60] | [timbr.ai](https://timbr.ai/) |

The gaps are specific. Stardog's documentation describes single-node-sized datasets with no sharding.[45] Its own docs flag that its LLM agent output can contain hallucinations.[45] Formal inference, context selection and action authorization are distinct capabilities; a platform can do one well and not the others.[52] Databricks and Microsoft Fabric now ship semantic or ontology features, but none is a one-for-one replacement.[38]

Competitors attack the lock-in. Stardog says Foundry's ontology is confined to Foundry, cannot relate separate ontologies, and requires adopting the full ecosystem.[53] That is a competitor's view, but the portability gap above supports it.

In defense the gap is wider. In May 2026, a NATO admiral said there is currently no competitor for Palantir.[83]

## Part VII

## Why deployments fail, and what FDEs fix

The failure rate explains the demand. MIT NANDA found that 95% of organizations get zero return from $30–40 billion of GenAI investment.[3] Of organizations that evaluated enterprise tools, 20% reached a pilot and 5% reached production.[3] Gartner predicts that over 40% of agentic AI projects will be canceled by the end of 2027.[24]

The causes are integration and learning. Pilots fail through brittle workflows, lack of contextual learning and misalignment with operations.[3] Projects stall on messy data, integration problems and lack of internal ownership.[73] Lightweight, wrapper-like integrations of core workflows often make agents break.[64] Research on enterprise agents finds the same gap: models lack domain-specific process knowledge, so plans and execution become unstable.[10]

Vendors see the same pattern. Salesforce says most businesses can build a proof of concept, but few can scale pilots into systems the business runs on.[44] A March 2025 study found that 88% of AI proofs of concept never reached wide-scale deployment.[82] Salesforce's FDEs stay after launch to monitor agent behavior and fix production-only issues.[44]

FDEs answer part of this. Externally sourced tools reach deployment about twice as often as internal builds.[74] Successful buyers demand deep customization and measurable outcomes.[3] Mid-market organizations often reach full implementation within 90 days; large enterprises scale up least.[74]

But people are not the whole answer. MIT names learning as the core barrier, not talent: most systems do not retain feedback or improve.[3] An engineer on site can wire a workflow. Only a platform that keeps what the engineer learned makes the next deployment cheaper.

## What I would do

A template for any forward deployed engagement, in the order I would follow it.

**Before I arrive**

1. **Pick one problem worth paying for, and write success as a number that can fail.** List what is out of scope and get the customer's sponsor to agree to it in writing.
2. **Decide if it is a prototype or a production build.** Say it out loud on day one. It changes how much engineering each week needs.

**Weeks 1–2**

1. **Work on the customer's real data from the first day.** Have a live demo on their data within two weeks. Use it as the specification.
2. **Build the simplest thing that could work.** A fixed workflow before an agent; a few clear tools before many. Add autonomy only where the data shows it pays.
3. **Read the outputs before writing metrics.** Do error analysis in a spreadsheet, then write a pass/fail test for each failure you found. Keep them as the regression suite for every model change.

**Weeks 3–8**

1. **Ship with governance, not after it.** Permissions, approval for writes and an audit log from the first release. An agent that can act must be checked on what it writes, not only on what it reads.
2. **Stay for adoption.** Be there for the first weeks after go-live. Adoption takes longer than the build, so plan for it and measure use, not delivery.

**By day 90–120**

1. **Hand over a system, not a person.** Runbooks, evals and trained internal champions. The customer's engineers should go from watching to operating.
2. **Send one reusable piece back to the product.** A connector, an ontology type or an eval set. Track custom hours per new customer; they must fall with each engagement.

**How to charge**

1. **Price the phase, not the hours.** A fixed-price diagnostic with a demo, a fixed-price production outcome with a success bonus, and a retainer to operate and extend it.

*— Luis González*

## Method and limits

This report draws on an evidence pack of 87 sources published mostly between 2019 and November 2026; 70 are cited below. They include Palantir's SEC filings and business updates, and announcements from OpenAI, AWS, Salesforce, Accenture and others. Practitioner playbooks, evaluation guides from Anthropic and others, analyst writing, press and research papers complete the pack. Every figure in the text was checked against its source. The full evidence, with each source's extracted claims and verbatim quotes, is public in the [evidence pack](https://github.com/iamluisgb/reports/tree/master/data/research/palantir-playbook). This edition, updated on 11 November 2026, replaces the version of 29 May 2026. The recommendations in "What I would do" are mine.

- **Company statements.** Most signals in the market map are what each company says about itself. Only Palantir's figures come from audited filings.
- **Estimates.** Tomoro's revenue, the Faculty multiple and the FDE cost model are analysts' estimates or illustrations, not reported numbers.
- **Secondary reports.** Some figures, such as Ode's committed capital and Sierra's price per resolution, come from one secondary source each.
- **A moving market.** Most deals in this report were announced in 2026. Valuations and headcounts change quickly.

## Sources

2. Business Update Q2 2026 — Palantir — Aug 2026 — [investors.palantir.com/files/Palantir%20-%20Q…](https://investors.palantir.com/files/Palantir%20-%20Q2%202026%20Business%20Update.pdf)
3. The GenAI Divide: State of AI in Business 2025 — MIT NANDA — Aug 2025 — [mlq.ai/media/quarterly_decks/v0.1_State_of_AI…](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)
5. Palantir Reports Q3 2026 results — SEC exhibit 99.1 — Nov 2026 — [sec.gov/Archives/edgar/data/1321655/000132165…](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000045/a2026q3ex991pressrelease.htm)
10. Routine: A Structural Planning Framework for LLM Agent System in Enterprise — Jul 2025 — [arxiv.org/abs/2507.14447](https://arxiv.org/abs/2507.14447)
11. Forward Deployed Engineer — Anthropic — [job-boards.greenhouse.io/anthropic/jobs/54230…](http://job-boards.greenhouse.io/anthropic/jobs/5423029008)
12. Demystifying evals for AI agents — Anthropic — Jan 2026 — [anthropic.com/research/demystifying-evals-for…](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
13. What FDE means at OpenAI — Colin Jarvis, OpenAI, Oct 2026 — [openai.com/index/forward-deployed-engineering…](https://openai.com/index/forward-deployed-engineering-means/)
14. Building effective AI agents — Anthropic — Dec 2024 — [anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)
15. Cognizant Establishes Dedicated Gemini Enterprise Practice — Apr 2026 — [news.cognizant.com/2026-04-22-Cognizant-Googl…](https://news.cognizant.com/2026-04-22-Cognizant-Google-Cloud-Diamond-Partnership-Gemini-Enterprise-Practice)
16. The AI-Native Enterprise Services Firm Backed by Anthropic, Blackstone, and Hellman & Friedman Announces Acquisition of Fractional AI — May 2026 — [blackstone.com/news/press/the-ai-native-enter…](https://www.blackstone.com/news/press/the-ai-native-enterprise-services-firm-backed-by-anthropic-blackstone-and-hellman-friedman-announces-acquisition-of-fractional-ai/)
17. AWS Forward-Deployed Engineering: FDE Profile — Plank — Jul 2026 — [joinplank.com/research/aws-fde](https://joinplank.com/research/aws-fde)
18. AWS invests $1 billion in forward deployed AI engineers — Amazon — Francessca Vasquez, Vice President of Frontier AI Engineering and Services, AWS, Jun 2026 — [aboutamazon.com/news/aws/aws-1-billion-forwar…](https://www.aboutamazon.com/news/aws/aws-1-billion-forward-deployed-ai-engineers)
19. What Is Ontology (Preview)? — Microsoft Fabric — Oct 2026 — [learn.microsoft.com/en-us/fabric/iq/ontology/…](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)
20. Writing effective tools for AI agents — Anthropic — Sep 2025 — [anthropic.com/research/writing-tools-for-agents](https://www.anthropic.com/research/writing-tools-for-agents)
21. Accenture and Google Cloud Deepen Partnership — Accenture — Sep 2026 — [newsroom.accenture.com/news/2026/accenture-an…](https://newsroom.accenture.com/news/2026/accenture-and-google-cloud-deepen-partnership-with-formation-of-new-accenture-gemini-enterprise-business-group)
22. Accenture to Acquire Faculty to Scale AI Capabilities — Jan 2026 — [newsroom.accenture.com/news/2026/accenture-to…](https://newsroom.accenture.com/news/2026/accenture-to-acquire-faculty-to-scale-ai-capabilities)
23. Accenture Completes Acquisition of Faculty — Mar 2026 — [newsroom.accenture.com/news/2026/accenture-compl](https://newsroom.accenture.com/news/2026/accenture-completes-acquisition-of-faculty)
24. Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 — Gartner, Inc., Jun 2025 — [gartner.com/en/newsroom/press-releases/2025-0…](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
27. Northslope: $22 Million Series A — Pulse 2.0 — Amit Chowdhry, Pulse 2.0, Jan 2026 — [pulse2.com/northslope-22-million-series-a-rai…](https://pulse2.com/northslope-22-million-series-a-raised-to-scale-palantir-native-and-mission-specific-ai-applications/)
28. AWS funnels $1B into forward deployed engineering hub — CIO Dive — Makenzie Holland / CIO Dive, Jun 2026 — [ciodive.com/news/aws-creates-forward-deployed…](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
29. Anthropic, Blackstone launch $1.5B Ode enterprise services firm — AI Weekly — Alexis Dufresne / AI News Weekly, Jul 2026 — [aiweekly.co/alerts/anthropic-blackstone-launc…](https://aiweekly.co/alerts/anthropic-blackstone-launch-15b-ode-enterprise-services-firm)
30. 9 startups from Palantir alumni you need to know — Fast Company — David Lidsky / Fast Company, Jan 2026 — [fastcompany.com/91480910/9-startups-from-pala…](https://www.fastcompany.com/91480910/9-startups-from-palantir-alumni-you-need-to-know)
31. Enterprise AI consultancy Distyl AI's valuation soars to $1.8B — SiliconANGLE — Mike Wheatley, SiliconANGLE, Sep 2025 — [siliconangle.com/2025/09/22/enterprise-ai-con…](https://siliconangle.com/2025/09/22/enterprise-ai-consultancy-distyl-ais-valuation-soars-1-8b-bumper-funding-round/)
32. Palantir touts forward deployed engineers, reports record revenue — Channel Dive — Matt Ashare, Channel Dive, Aug 2026 — [channeldive.com/news/palantir-forward-deploye…](https://www.channeldive.com/news/palantir-forward-deployed-engineers-ai-revenue-spike/827139/)
33. The Palantir Mafia — Business Insider — May 2025 — [businessinsider.com/palantir-mafia-former-emp…](https://www.businessinsider.com/palantir-mafia-former-employees-startups-anduril-2025-3)
35. The forward deployed engineer: From handoff to ownership — Modus Create — Nov 2026 — [moduscreate.com/blog/forward-deployed-enginee…](https://www.moduscreate.com/blog/forward-deployed-engineering)
36. $100M Fundraise to Power the Next Gen of AI Infrastructure — Invisible — Sep 2025 — [invisibletech.ai/blog/invisible-technologies-…](https://invisibletech.ai/blog/invisible-technologies-raises-100-million)
38. Palantir Ontology Explained: How It Works in Foundry — Fluree — Kevin Doubleday (Fluree), Oct 2026 — [flur.ee/blog/palantir-ontology-explained](https://flur.ee/blog/palantir-ontology-explained)
39. Deploying Full Spectrum AI in Days: How AIP Bootcamps Work — Palantir — Oct 2023 — [blog.palantir.com/deploying-full-spectrum-ai-…](https://blog.palantir.com/deploying-full-spectrum-ai-in-days-how-aip-bootcamps-work-21829ec8d560)
40. OpenAI: Forward Deployed Engineering for Enterprise LLM Deployments — ZenML LLMOps database — [zenml.io/llmops-database/forward-deployed-eng…](https://www.zenml.io/llmops-database/forward-deployed-engineering-for-enterprise-llm-deployments)
42. OpenAI launches DeployCo to help businesses build — OpenAI — May 2026 — [openai.com/index/openai-launches-the-deployme…](https://openai.com/index/openai-launches-the-deployment-company/)
43. How to Structure a Forward Deployed Engineering Team — Quivly — Arushi Jain (Quivly), Oct 2026 — [quivly.ai/blog/structure-forward-deployed-eng…](https://www.quivly.ai/blog/structure-forward-deployed-engineering-team)
44. Salesforce Launches the Forward Deployed Engineering Partner Network — Apr 2026 — [salesforce.com/news/stories/salesforce-launch…](https://www.salesforce.com/news/stories/salesforce-launches-forward-deployed-engineer-partner-network-announcement/)
45. Stardog Knowledge Graph Platform: Claims vs. Its Docs — Atlan — Emily Winks / Atlan, Sep 2026 — [atlan.com/know/ai-agent/knowledge-graph/what-…](https://atlan.com/know/ai-agent/knowledge-graph/what-is-stardog/)
46. Best Enterprise Knowledge Graph Software in 2026 — Fluree — Kevin Doubleday (Fluree), Jun 2026 — [flur.ee/blog/enterprise-kg-buyers-guide-2026](https://flur.ee/blog/enterprise-kg-buyers-guide-2026)
47. OpenAI Deployment Company (DeployCo): FDE Profile — Plank — Jul 2026 — [joinplank.com/research/openai-deployment-company](https://joinplank.com/research/openai-deployment-company)
48. Palantir Technologies: FDE Profile — Plank — JoinPlank, Oct 2026 — [joinplank.com/research/palantir](https://joinplank.com/research/palantir)
49. The 8 Best Palantir Competitors & Alternatives — Stardog — Sep 2026 — [stardog.com/blog/best-palantir-competitors-al…](https://www.stardog.com/blog/best-palantir-competitors-alternatives/)
50. How to Structure, Run, and Scale an FDE Function in 2026 — Perspective AI — Jun 2026 — [getperspective.ai/blog/the-forward-deployed-e…](https://getperspective.ai/blog/the-forward-deployed-engineer-playbook-how-to-structure-run-and-scale-an-fde-function-in-2026)
51. Innovative Solutions Launches Forward Deployed Services — Jul 2026 — [innovativesol.com/innovative-solutions-launch…](https://innovativesol.com/innovative-solutions-launches-forward-deployed-services/)
52. 8 Stardog Alternatives in 2026 — Digetiers — Julius Hollmann / digetiers, Aug 2026 — [digetiers.com/en/insights/library/stardog-alt…](https://www.digetiers.com/en/insights/library/stardog-alternatives)
53. Best Knowledge Graph Tools & Platforms for 2026 — Stardog — Oct 2026 — [stardog.com/blog/best-knowledge-graph-softwar…](https://www.stardog.com/blog/best-knowledge-graph-software-tools-platforms/)
54. A Day in the Life of a Palantir Deployment Strategist — Mar 2022 — [blog.palantir.com/a-day-in-the-life-of-a-pala…](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96)
55. When does an AI startup need forward-deployed engineers? — Plank — Anusheel Bhushan, co-founder of Plank, Oct 2026 — [joinplank.com/fde/guides/when-ai-startups-nee…](https://joinplank.com/fde/guides/when-ai-startups-need-fdes)
56. Today's Hottest Role: Forward Deployed Engineer — Salesforce — Laura Hilgers / Salesforce, Nov 2025 — [salesforce.com/blog/forward-deployed-engineer](https://www.salesforce.com/blog/forward-deployed-engineer/)
57. Palantir Vanguard: Elite — [palantir.com/partnerships/elite](https://www.palantir.com/partnerships/elite/)
59. Forward Deployed Engineering and AI Agents — Sigmoid — Sep 2026 — [sigmoid.com/forward-deployed-engineering](https://www.sigmoid.com/forward-deployed-engineering/)
60. Timbr vs. Palantir vs. Stardog — Timbr.ai — [timbr.ai/ufaqs/timbr-vs-palantir-vs-stardog-h…](https://timbr.ai/ufaqs/timbr-vs-palantir-vs-stardog-how-were-different/)
61. OpenAI's Tomoro Acquisition: Revenue, Valuation & AI services M&A — Aventis — Filip Drazdou, Aventis Advisors, May 2026 — [aventis-advisors.com/ai-services-ma-2026](https://aventis-advisors.com/ai-services-ma-2026/)
62. Dev versus Delta: Demystifying engineering roles at Palantir — Apr 2019 — [blog.palantir.com/dev-versus-delta-demystifyi…](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87)
63. Introducing Forward Deployed Engineering for Partners — AWS — Amazon Web Services (AWS); Chandra Pinapala, Erik Farr, Karthik Sonti, Jun 2026 — [aws.amazon.com/blogs/apn/introducing-forward-…](https://aws.amazon.com/blogs/apn/introducing-forward-deployed-engineering-for-partners-winning-the-future-of-enterprise-ai/)
64. Trading Margin for Moat: Why the Forward Deployed Engineer Is the Hottest Job in Startups — a16z — Joe Schmidt (Andreessen Horowitz), Jun 2025 — [a16z.com/services-led-growth](https://a16z.com/services-led-growth/)
65. Forward Deployed Engineering — Ramp Builders Blog — Leo Mehr (Ramp Builders Blog), Aug 2025 — [builders.ramp.com/post/forward-deployed-engin…](https://builders.ramp.com/post/forward-deployed-engineering)
66. How Palantir Invented the Forward Deployed Engineer Model — R&D, FDE Academy, Nov 2026 — [fde.academy/blog/how-palantir-invented-the-fo…](https://fde.academy/blog/how-palantir-invented-the-forward-deployed-engineer-model)
67. Evals: Doing Error Analysis Before Writing Tests — Hamel Husain — Dec 2024 — [hamel.dev/notes/llm/officehours/erroranalysis…](https://hamel.dev/notes/llm/officehours/erroranalysis.html)
68. Forward Deployed Engineer: When Startups Should Hire One — CRV — May 2026 — [crv.com/content/forward-deployed-engineer](https://www.crv.com/content/forward-deployed-engineer)
69. Forward-deployed Engineers: The Last Mile of the AI Value Chain — TBR — Alex Demeule, Senior Analyst, Technology Business Research (TBR), Jul 2026 — [tbri.com/special-reports/forward-deployed-eng…](https://tbri.com/special-reports/forward-deployed-engineers-the-last-mile-of-the-ai-value-chain/)
70. The Economics of the Forward Deployed Engineer Model — Shivank Agrawal / Scaler, Nov 2026 — [scaler.com/topics/the-economics-of-the-forwar…](https://www.scaler.com/topics/the-economics-of-the-forward-deployed-engineer/)
71. AI Evals: Everything You Need to Know — Hamel Husain — Sep 2026 — [hamel.dev/blog/posts/evals-faq](https://hamel.dev/blog/posts/evals-faq/)
72. The Sierra Playbook: What They Actually Do Differently — Falk Gottlob, Aug 2026 — [falkster.com/blog/the-sierra-playbook](https://falkster.com/blog/the-sierra-playbook)
73. The Palantirization of everything — a16z — Marc Andrusko (Andreessen Horowitz / a16z), Jan 2026 — [a16z.com/the-palantirization-of-everything](https://a16z.com/the-palantirization-of-everything/)
74. The AI Divide — DX — Justin Reock / DX, Dec 2025 — [getdx.com/blog/the-ai-divide](https://getdx.com/blog/the-ai-divide/)
77. The Forward Deployed Engineer Playbook Explained — FDE Academy — R&D, FDE Academy, Jun 2026 — [fde.academy/blog/forward-deployed-engineer-pl…](https://fde.academy/blog/forward-deployed-engineer-playbook)
78. Outcome-Based Pricing Models: Examples — CX Foundation — Charlie Mitchell / CX Foundation, Aug 2026 — [cxfoundation.com/blog/outcome-based-pricing](https://cxfoundation.com/blog/outcome-based-pricing)
79. How to Build Your 1st Forward Deployed Engineering Team — Per Aspera — Sep 2025 — [peraspera.us/forward-deployed](https://peraspera.us/forward-deployed/)
80. OpenAI Forms New Joint Venture and Acquires Tomoro — Cooley — Jun 2026 — [cooleyma.com/deals/openai-forms-new-joint-ven…](https://cooleyma.com/deals/openai-forms-new-joint-venture-openai-deployment-company-and-acquires-tomoro/)
81. The Forward Deployed Engineer Lifecycle — InterviewBit — Varsity on Behalf of CEP IIT Delhi, Sep 2026 — [interviewbit.com/varsity/blog/the-forward-dep…](https://www.interviewbit.com/varsity/blog/the-forward-deployed-engineer-lifecycle/)
82. Report: Invisible Business Breakdown & Founding Story — Contrary Research — Oct 2026 — [research.contrary.com/company/invisible](https://research.contrary.com/company/invisible)
83. Palantir — Wikipedia — [en.wikipedia.org/wiki/Palantir](https://en.wikipedia.org/wiki/Palantir)
86. H (company) — Wikipedia — [en.wikipedia.org/wiki/H_%28company%29](https://en.wikipedia.org/wiki/H_%28company%29)
