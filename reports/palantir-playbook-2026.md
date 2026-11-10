---
title: "What AI Startups Stole From Palantir's Playbook"
date: 2026-05-29
type: special
url: https://luisgonzalezbernal.com/reports/reports/palantir-playbook-2026.html
summary: "The playbook · Who copies it · The economics · Ontology platforms · Why deployments fail"
tags: [business, funding]
reading_time_minutes: 13
---
Market Analysis · Special Report

# What AI Startups Stole From *Palantir's Playbook*

29 May 2026 · Updated 10 Nov 2026

The playbook · Who copies it · The economics · Ontology platforms · Why deployments fail

## Key findings

1. **The model labs bought the playbook.** OpenAI launched a Deployment Company with more than $4 billion of initial investment to embed forward deployed engineers (FDEs) in customers.[21] Its founding acquisition, Tomoro, brought roughly 150 FDEs and deployment specialists.[21] Anthropic launched a services company with about $1.5 billion committed and bought Fractional AI.[29]
2. **Big tech followed.** AWS put $1 billion into a dedicated FDE organization, and Google Cloud and Microsoft made similar moves.[16] FDE job postings rose 800–1000% in a year.[35]
3. **The original still works.** Palantir's Q3 2026 revenue grew 96% to $2.313 billion.[4] US commercial revenue grew 148% to $984 million, with a 47% GAAP operating margin.[4]
4. **Most copies take the engineers, not the platform.** a16z says Palantir works because a real platform sits under the bespoke work.[35] Copying only the embedded engineers produces thousands of bespoke deployments that are hard to maintain.[35] OpenAI's Deployment Company has announced no software product; in October 2026 it was hiring a lead for internal products.[23]
5. **Margin is the price of the model.** Compiled benchmarks put AI products at 45% gross margin in 2025, against an 80% SaaS median.[34] ServiceNow went from 63.2% at IPO to 79% in 2024.[31]
6. **Deployment is the bottleneck, but not only for lack of people.** MIT NANDA found 95% of organizations get zero return from GenAI.[2] It names learning as the core barrier, not infrastructure, regulation or talent.[2] External partnerships succeed twice as often as internal builds.[2]

## Part I

## The playbook, as Palantir describes it

Palantir has two big engineering roles. "Devs" build the product; "Deltas", its forward deployed software engineers, deploy it for one customer each.[30] Palantir sums it up as "one capability, many customers" against "one customer, many capabilities".[30] Deltas sit in Business Development and are mandated to achieve technical outcomes.[30]

Deltas work with Deployment Strategists, known as Echos. In theory Echos are more like product managers and Deltas more technical; in practice both roles blend.[26] Palantir built the model in the early 2010s, when intelligence customers could not disclose their needs through normal product discovery.[32] By 2016, FDEs outnumbered traditional software engineers.[32]

The field work feeds the product. Deltas contribute code back to the core platform when a missing feature blocks a customer outcome.[30] One account calls this loop the "gravel road to paved highway": custom work becomes standard product features.[32] Without that discipline, the same source says, the model becomes unscalable custom work.[32]

*[Palantir's loop turns field work into platform features; a copy without a platform turns field work into bespoke deployments to maintain]*

*The difference between the original and most copies. Built from sources 30, 32 and 35.*

The sale starts small. Contracts begin with a bootcamp and limited licenses, and grow use case by use case if value is proven.[35] Over time the revenue mix tilts toward software subscription rather than services.[35] In an AIP Bootcamp, participants go from zero to a use case in one to five days.[19] Pricing is a fixed fee, with no traditional SKUs.[35]

Under the bootcamp sits the ontology. It maps datasets, virtual tables and models to business objects such as plants and orders.[18] It also defines the actions that people and AI agents may take.[18] Since June 2026, an Ontology MCP server exposes object types, actions and functions as tools for agents.[18]

- **$2.313B** Q3 2026 revenue, up 96% year over year

Palantir, SEC filing[4]

- **+148%** US commercial revenue growth, to $984 million

Q3 2026[4]

- **47%** GAAP operating margin

Q3 2026[4]

## Part II

## Who is copying it

The largest copies come from the model labs and the consultancies that serve them. Most of them were announced in 2026.

| Who | What they did | Signal |
| --- | --- | --- |
| OpenAI | Deployment Company that embeds FDEs inside customers[21] | $4B+ committed; $14B post-money valuation[23] |
| OpenAI ← Tomoro | Founding acquisition of an applied AI firm[21] | About 150 FDEs and deployment specialists[38] |
| OpenAI ← Northslope | Firm founded by former Palantir FDEs[23] | Took the FDE count into the hundreds[23] |
| Anthropic | Services company with Blackstone, Hellman & Friedman and Goldman Sachs[29] | About $1.5B committed; acquired Fractional AI[29] |
| Accenture ← Faculty | Bought a UK AI-native services and products firm, founded in 2014[12,13] | 400+ AI professionals; reported $1B headline price[12,29] |
| AWS, Google Cloud, Microsoft | Dedicated FDE or AI-deployment organizations[16] | AWS: $1B into its FDE organization[16] |
| H Company | Pivot toward FDEs under a former Palantir France CEO[42] | CEO change in June 2025[42] |

The labs say why. OpenAI calls deployment, not model capability, the binding constraint on enterprise value.[21] Its engagements start with a diagnostic, pick a few priority workflows, then put FDEs inside the organization.[21] Anthropic's FDEs embed with strategic customers and build MCP servers, sub-agents and agent skills.[10] They also codify repeatable deployment patterns and feed them back to product.[10]

Smaller companies copy the role too. Ramp built an FDE team of about 15 engineers in pods.[37] Decagon uses human Agent Product Managers to implement its support agents.[31] At the time of a16z's analysis, 22 of 311 open OpenAI roles were FDE or solutions engineering.[31]

## Part III

## The economics: margin for moat, or consulting by another name

The case for the model is a16z's "trading margin for moat". At IPO, ServiceNow and Workday had gross margins of 63.2% and 54.1%.[31] By 2024 they reached 79% and 75%.[31] a16z tells AI startups to grow total gross profit, not to optimize for an 80% gross margin.[31] It even suggests selling services at cost.[31]

The current numbers are far from software margins. Compiled benchmarks put AI products at 45% gross margin in 2025, with 53% expected in 2026.[34] An FDE is expensive. Anthropic advertises £225,000 to £255,000 a year for one in London.[10] One analysis models a fully loaded frontier-lab FDE at $845K a year.[34]

Deal size decides whether that cost pays. In one illustrative model, $3M–15M enterprise contracts cover an FDE 2.5 to 6 times.[34] Deals under $500K cover well under half of one.[34] That is a model, not measured data, but it explains why FDEs go to the largest accounts.

The firms that were bought look like good services businesses. One estimate puts Tomoro at about £225k revenue per head, with margins above 40%.[29] Faculty's reported price was about 15 times its run-rate revenue.[29] The buyers paid for teams and clients, not for models or research.[29]

So is it consulting? Palantir's Deltas say no: consultants deliver one-time analyses, while Deltas deploy existing software products.[30] That defence needs a product. TBR expects Palantir to remain an exception, not the template for an industrywide shift.[33] For vendors, it says, FDE support is likely a loss leader paid for by software or cloud consumption.[33] Systems integrators cannot recover it that way and must bill it as services.[33]

## Part IV

## The ontology: what competitors offer

Palantir's platform is several products. Foundry handles data operations and the ontology; AIP connects generative AI on top of it.[24] Gotham serves defense and intelligence, and Apollo delivers software to any environment, even air-gapped ones.[24] No single product replaces all four equally well.[24]

The ontology itself is hard to swap. Palantir's ontology and the open W3C standards (OWL, RDF, SHACL) are not supersets of each other.[18] OWL lacks permissioned actions, and Foundry is not built around open-world inference.[18] One user-built converter found that 7 of 22 Palantir property types had no counterpart in any published standard.[18] Moving the data out does not move its meaning or logic.[24]

| Platform | What it is |
| --- | --- |
| Microsoft Fabric IQ | Ontology preview: a virtual semantic layer over source systems, generated from Power BI models[11] |
| Stardog | RDF/OWL knowledge graph with query-time reasoning and data virtualization[22] |
| d.AP | AI context platform with ontology-guided context assembly for agents[25] |
| eccenca Corporate Memory | Knowledge graph platform for semantic integration, modeling and governance[25] |
| Neo4j | Property-graph platform, no formal semantics layer on top[22,25] |

The gaps are specific. Stardog's documentation describes single-node-sized datasets with no sharding.[22] Its own docs flag that its LLM agent output can contain hallucinations.[22] Formal inference, context selection and action authorization are distinct capabilities; a platform can do one well and not the others.[25] Databricks and Microsoft Fabric now ship semantic or ontology features, but none is a one-for-one replacement.[18]

In defense the gap is wider. In May 2026, a NATO admiral said there is currently no competitor for Palantir.[39]

## Part V

## Why deployments fail, and what FDEs fix

The failure rate explains the demand. MIT NANDA found that 95% of organizations get zero return from $30–40 billion of GenAI investment.[2] Of organizations that evaluated enterprise tools, 20% reached a pilot and 5% reached production.[2] Gartner predicts that over 40% of agentic AI projects will be canceled by the end of 2027.[14]

The causes are integration and learning. Pilots fail through brittle workflows, lack of contextual learning and misalignment with operations.[2] Projects stall on messy data, integration problems and lack of internal ownership.[35] Lightweight, wrapper-like integrations of core workflows often make agents break.[31] Research on enterprise agents finds the same gap: models lack domain-specific process knowledge, so plans and execution become unstable.[9]

FDEs answer part of this. Externally sourced tools reach deployment about twice as often as internal builds.[36] Successful buyers demand deep customization and measurable outcomes.[2] Mid-market organizations often reach full implementation within 90 days; large enterprises scale up least.[36]

But people are not the whole answer. MIT names learning as the core barrier, not talent: most systems do not retain feedback or improve.[2] An engineer on site can wire a workflow. Only a platform that keeps what the engineer learned makes the next deployment cheaper.

## What I would do

1. **Start with a bootcamp, not a transformation.** Prove one workflow on the customer's own data in days. Expand only use case by use case.
2. **Do not hire FDEs before you have a product to feed.** Each engagement must leave a reusable piece behind. Measure the share of field work that becomes product every quarter.
3. **Match the model to the deal size.** Put FDEs on large accounts. Below about $500K a year, use lighter onboarding and templates.
4. **Choose an ontology platform by capability.** Decide if you need inference, context for agents or authorized actions. No platform does all three like Foundry.
5. **Build for learning, not only for the launch.** Capture corrections and feedback in the platform, so the system improves after the engineer leaves.

*— Luis González*

## Method and limits

This report replaces the version of 29 May 2026, which cited no sources in the text. It was rebuilt on 10 November 2026 with the reports research pipeline. I screened 35 web results from 5 TinyFish queries by hand. The pipeline added results from Hacker News, arXiv and Wikipedia: 85 in total. It read 47 sources, and 43 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 245 claims with verbatim quotes and discarded 10 whose quote was not in the source. Claude wrote the synthesis from that evidence and checked every cited figure against its source. The conclusions in "What I would do" are mine.

- **Removed claims.** The old version said that Palantir starts with contracts above $25 million and that GraphRAG cuts hallucinations by 40–60%. No source in the pack supports either claim; a16z describes small initial contracts. Market sizes, a 12–18 month window and per-company revenue figures without sources were also removed.
- **Estimates, not filings.** Tomoro's revenue, the Faculty multiple and the FDE cost model are analysts' estimates or illustrations. Only the Palantir figures come from an SEC filing.
- **Secondary reports.** Anthropic's services company and the AWS figure come from one secondary source each. FDE hiring growth comes from a16z's summary of job-posting data.
- **Vendor sources.** The platform comparison relies on vendors describing themselves and their competitors.

## Sources

2. The GenAI Divide: State of AI in Business 2025 — MIT NANDA — Aug 2025 — [mlq.ai/media/quarterly_decks/v0.1_State_of_AI…](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)
4. Palantir Reports Q3 2026 results — SEC exhibit 99.1 — Nov 2026 — [sec.gov/Archives/edgar/data/1321655/000132165…](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000045/a2026q3ex991pressrelease.htm)
9. Routine: A Structural Planning Framework for LLM Agent System in Enterprise — Jul 2025 — [arxiv.org/abs/2507.14447](https://arxiv.org/abs/2507.14447)
10. Forward Deployed Engineer — Anthropic — [job-boards.greenhouse.io/anthropic/jobs/54230…](http://job-boards.greenhouse.io/anthropic/jobs/5423029008)
11. What Is Ontology (Preview)? — Microsoft Fabric — Oct 2026 — [learn.microsoft.com/en-us/fabric/iq/ontology/…](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)
12. Accenture to Acquire Faculty to Scale AI Capabilities — Jan 2026 — [newsroom.accenture.com/news/2026/accenture-to…](https://newsroom.accenture.com/news/2026/accenture-to-acquire-faculty-to-scale-ai-capabilities)
13. Accenture Completes Acquisition of Faculty — Mar 2026 — [newsroom.accenture.com/news/2026/accenture-compl](https://newsroom.accenture.com/news/2026/accenture-completes-acquisition-of-faculty)
14. Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 — Gartner, Inc., Jun 2025 — [gartner.com/en/newsroom/press-releases/2025-0…](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
16. Palantir touts forward deployed engineers, reports record revenue — Channel Dive — Matt Ashare, Channel Dive, Aug 2026 — [channeldive.com/news/palantir-forward-deploye…](https://www.channeldive.com/news/palantir-forward-deployed-engineers-ai-revenue-spike/827139/)
18. Palantir Ontology Explained: How It Works in Foundry — Fluree — Kevin Doubleday (Fluree), Oct 2026 — [flur.ee/blog/palantir-ontology-explained](https://flur.ee/blog/palantir-ontology-explained)
19. Deploying Full Spectrum AI in Days: How AIP Bootcamps Work — Palantir — Oct 2023 — [blog.palantir.com/deploying-full-spectrum-ai-…](https://blog.palantir.com/deploying-full-spectrum-ai-in-days-how-aip-bootcamps-work-21829ec8d560)
21. OpenAI launches DeployCo to help businesses build — OpenAI — May 2026 — [openai.com/index/openai-launches-the-deployme…](https://openai.com/index/openai-launches-the-deployment-company/)
22. Stardog Knowledge Graph Platform: Claims vs. Its Docs — Atlan — Emily Winks / Atlan, Sep 2026 — [atlan.com/know/ai-agent/knowledge-graph/what-…](https://atlan.com/know/ai-agent/knowledge-graph/what-is-stardog/)
23. OpenAI Deployment Company (DeployCo): FDE Profile — Plank — Jul 2026 — [joinplank.com/research/openai-deployment-company](https://joinplank.com/research/openai-deployment-company)
24. The 8 Best Palantir Competitors & Alternatives — Stardog — Sep 2026 — [stardog.com/blog/best-palantir-competitors-al…](https://www.stardog.com/blog/best-palantir-competitors-alternatives/)
25. 8 Stardog Alternatives in 2026 — Digetiers — Julius Hollmann / digetiers, Aug 2026 — [digetiers.com/en/insights/library/stardog-alt…](https://www.digetiers.com/en/insights/library/stardog-alternatives)
26. A Day in the Life of a Palantir Deployment Strategist — Mar 2022 — [blog.palantir.com/a-day-in-the-life-of-a-pala…](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96)
29. OpenAI's Tomoro Acquisition: Revenue, Valuation & AI services M&A — Aventis — Filip Drazdou, Aventis Advisors, May 2026 — [aventis-advisors.com/ai-services-ma-2026](https://aventis-advisors.com/ai-services-ma-2026/)
30. Dev versus Delta: Demystifying engineering roles at Palantir — Apr 2019 — [blog.palantir.com/dev-versus-delta-demystifyi…](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87)
31. Trading Margin for Moat: Why the Forward Deployed Engineer Is the Hottest Job in Startups — a16z — Joe Schmidt (Andreessen Horowitz), Jun 2025 — [a16z.com/services-led-growth](https://a16z.com/services-led-growth/)
32. How Palantir Invented the Forward Deployed Engineer Model — R&D, FDE Academy, Nov 2026 — [fde.academy/blog/how-palantir-invented-the-fo…](https://fde.academy/blog/how-palantir-invented-the-forward-deployed-engineer-model)
33. Forward-deployed Engineers: The Last Mile of the AI Value Chain — TBR — Alex Demeule, Senior Analyst, Technology Business Research (TBR), Jul 2026 — [tbri.com/special-reports/forward-deployed-eng…](https://tbri.com/special-reports/forward-deployed-engineers-the-last-mile-of-the-ai-value-chain/)
34. The Economics of the Forward Deployed Engineer Model — Shivank Agrawal / Scaler, Nov 2026 — [scaler.com/topics/the-economics-of-the-forwar…](https://www.scaler.com/topics/the-economics-of-the-forward-deployed-engineer/)
35. The Palantirization of everything — a16z — Marc Andrusko (Andreessen Horowitz / a16z), Jan 2026 — [a16z.com/the-palantirization-of-everything](https://a16z.com/the-palantirization-of-everything/)
36. The AI Divide — DX — Justin Reock / DX, Dec 2025 — [getdx.com/blog/the-ai-divide](https://getdx.com/blog/the-ai-divide/)
37. What are Forward Deployed Engineers, and why are they so in demand? (2025) — Gergely Orosz / The Pragmatic Engineer, Aug 2025 — [newsletter.pragmaticengineer.com/p/forward-de…](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)
38. OpenAI Forms New Joint Venture and Acquires Tomoro — Cooley — Jun 2026 — [cooleyma.com/deals/openai-forms-new-joint-ven…](https://cooleyma.com/deals/openai-forms-new-joint-venture-openai-deployment-company-and-acquires-tomoro/)
39. Palantir — Wikipedia — [en.wikipedia.org/wiki/Palantir](https://en.wikipedia.org/wiki/Palantir)
42. H (company) — Wikipedia — [en.wikipedia.org/wiki/H_%28company%29](https://en.wikipedia.org/wiki/H_%28company%29)
