---
title: "The Knowledge Layer for Agents: Ontologies, Graphs and Where ML Fits"
date: 2026-10-02
type: special
url: https://luisgonzalezbernal.com/reports/reports/knowledge-layer-2026-10-02.html
summary: "What the layer is · GraphRAG versus vector RAG · Accuracy on enterprise data · Cases in production · Operational ontologies and actions · Where ML goes · Graphs in root cause analysis · Tools and standards"
tags: [memory, research]
reading_time_minutes: 29
---
Memory & Knowledge · Special Report

# The *Knowledge Layer* for Agents: Ontologies, Graphs and Where ML Fits

2 Oct 2026 · Updated 11 Nov 2026

What the layer is · GraphRAG versus vector RAG · Accuracy on enterprise data · Cases in production · Operational ontologies and actions · Where ML goes · Graphs in root cause analysis · Tools and standards

## Key findings

1. **A semantic layer is worth more than a better model.** In a vendor test of seven LLMs on 410 business questions, the semantic layer added 20 to 31 points to every model.[66] Switching models moved accuracy by at most 17.6 points.[66] An independent paired benchmark found +17 to +23 points, and model choice within a tier made no significant difference.[17]
2. **A knowledge graph over SQL raises accuracy on enterprise questions.** In the authors' first benchmark, a knowledge graph moved accuracy from 16% to 54%.[28] Ontology-based checks then raised it to 72%, a figure that includes 8% honest "I don't know" answers.[28] The error rate was 20%.[28]
3. **Grounding helps most where the model knows least.** In a controlled test of 1,800 runs across five industries and three LLMs, ontology-coupled agents gave more accurate metrics than ungrounded agents.[5] The lift was twice as large in Vietnam-localized domains as in English ones.[5] Your internal terms are the same case: the model has not seen them.
4. **GraphRAG costs far more and gains less than reported.** One benchmark measured 377 times as many prompt tokens per question as plain vector RAG.[45] An unbiased evaluation of 3 GraphRAG methods found gains "much more moderate" than earlier claims.[32]
5. **The platforms keep a person in the write path.** Palantir's AIP Logic applies ontology edits automatically or stages them for human review.[67] Microsoft's ontology agent proposes changes for review under a proposal-first model.[41] Read-time access controls do not cover the model's output or the edits it composes.[67]
6. **Real deployments report gains in time, not only accuracy.** At LinkedIn, a knowledge graph built from past support tickets cut median resolution time by 28.6% over about six months.[26] At Kuaishou, a graph-based root cause system cut diagnosis time by 77.3%.[12]
7. **Most of the value is in joins across systems.** In a manufacturing graph, blocking 24 cross-system tools cut recall from 1.00 to 0.31.[9] 69% of the signals needed cross-system graph joins.[9]
8. **Graphs plus agents already work in operations.** A root cause system at Kuaishou has run in production for over six months.[12] It cut average diagnosis time by 77.3%.[12]

## Part I

## Four words for one layer

Ontology, knowledge graph, semantic layer and context layer name parts of one structure. The ontology is the blueprint: the type system of objects, links, actions and rules.[92] The knowledge graph is that blueprint filled with live instances.[92] A knowledge graph describes entities and their relationships, and a reasoner can derive new knowledge from it.[93]

The graph does not need its own database. A virtual knowledge graph answers queries from an existing relational database or data lake.[93] A set of mappings connects the source data to the graph structure and ontology.[93] The standards come from the Semantic Web: RDF and OWL encode meaning together with the data.[90]

The vendors now describe the same layer. Microsoft defines its Fabric IQ ontology as a machine-understandable business representation bound to live enterprise data.[41] It is a virtual layer: source data stays in its owning system.[38] Palantir calls its ontology the "nouns" and "verbs" of operational processes, legible to humans and agents.[37]

The semantic layer brings the business vocabulary. One framework for data warehouses joins schema metadata with meaning taken from documentation, ETL scripts and business glossaries.[35] It reports better entity disambiguation, catalog enrichment and cross-system understanding.[35]

For agents, the layer must do more than retrieval. One practitioner write-up says the ontology is not a store of chunks for the prompt.[92] It is a live layer that many systems read and write at the same time.[92] Research frameworks say the same in formal terms. Enterprise systems today constrain what goes into an agent, but not what comes out.[5] An ontology layer can validate outputs and turn generation into a generate-verify-correct pipeline.[23]

### Semantic layer, context layer: where the line falls

Practitioners now separate two layers. A semantic layer is a governed set of metric, dimension and entity definitions between the warehouse and its tools.[47] A context layer is the business knowledge an agent reads before it answers.[47] It bundles semantic models, documentation, lineage, glossary terms, example queries and unstructured knowledge, often served over MCP.[47] In most stacks, the semantic layer is one input to the context layer.[47]

DataHub lists what the context layer must carry: semantics, operational state and provenance.[59] Semantics covers ontologies and knowledge graphs that link data, metrics, rules, security, ownership and policies.[59] Operational state is the current status of entities and processes.[59] Provenance tracks lineage, decisions, actions and outcomes across agent runs.[59]

A small example shows why definitions matter. Asked how many active vendors exist, one agent found three defensible answers: 25, 24 and 21.[47] With a governed definition served over MCP, it returned 25 and cited its source column. It also flagged an ERP field that disagreed in 6 of 34 vendors.[47] The same source warns that a semantic layer computes whatever definition is encoded, even a wrong one.[47]

The effect can be large. OpenAI's internal data agent serves roughly 4,000 of its 5,000 employees daily.[49] With the full context stack, one complex question took 1 minute 22 seconds instead of over 22 minutes.[49]

*[Agents read the knowledge layer through typed queries and write through validated actions; ML proposes changes from the side]*

*How the parts fit: the ontology types the graph, agents read and write through it, and ML proposes changes that checks or people promote. Built from sources 92, 93, 23 and 19.*

## Part II

## GraphRAG versus vector RAG

GraphRAG retrieves facts along a graph instead of a list of similar chunks.[1] The evidence on its value is mixed. A systematic comparison found distinct strengths for RAG and for GraphRAG across tasks.[1] Combining the two gave consistent improvements.[1]

Evaluation is the weak point. GraphRAG methods are tuned to knowledge-graph QA benchmarks with few question patterns.[3] Common evaluations use unrelated questions and biased LLM judges.[32] With those flaws removed, the gains of 3 methods were much more moderate.[32]

The clearest gain is on multi-hop questions. These need facts from two or more passages, and flat top-k retrieval often finds only one.[87] In one public benchmark on HotpotQA, GraphRAG raised supporting-fact recall from 0.81 to 0.98.[87] In climate science, a hybrid of vector search and GraphRAG reported 177% more contextual recall than classical RAG.[33]

The cost gap is large. GraphRAG indexing costs roughly 300x to 2,000x a vector index, because an LLM reads every chunk at least twice.[45] At query time, one benchmark measured 331,375 prompt tokens per question for global search, against 879 for vector RAG.[45] On fact retrieval over novels, reranked vector RAG scored 60.92 against 49.29 for Microsoft GraphRAG.[45] On complex reasoning, GraphRAG won: 50.93 against 42.93.[45]

Cheaper graph methods are narrowing the cost gap. Microsoft's LazyGraphRAG has indexing costs equal to vector RAG and 0.1% of full GraphRAG.[75] On global queries, it matches GraphRAG Global Search in quality at more than 700 times lower query cost.[75] LightRAG indexes a 500-page corpus in about 3 minutes for roughly $0.50.[77] It reaches 70–90% of GraphRAG's performance at 1/100th of the cost.[77]

Much of the gap closes without a graph. A hybrid of dense vectors, BM25 keyword search and a reranker closes most of it.[45] Where a graph does help, the gain is modest. In financial news, two-hop graph retrieval raised entity recall by 6.4%, and mean latency rose 22.6%.[11]

| Situation | What the evidence says |
| --- | --- |
| Multi-hop questions across passages | Graph retrieval finds the second fact that flat top-k misses[87] |
| Concepts spread across many articles | Hybrid local and global retrieval beats isolated text spans[33] |
| Relations computable from data (coordinates) | Explicit graph edges add little[27] |
| Different question patterns | Each needs its own traversal; a fixed strategy falls short[3] |
| Direct factual lookups in one chunk | Vector RAG is enough; a graph adds cost without accuracy[77] |
| Many real-world tasks | GraphRAG often underperforms vanilla RAG[20] |

## Part III

## Accuracy on enterprise data

Here the evidence is stronger. The question is how well an LLM answers business questions over company data.

- **+17 to +23** points of accuracy from a 4 KB semantic-layer document, across three models

Paired benchmark, 100 questions[17]

- **29 vs 14.6** points gained from a semantic layer against points gained from a model upgrade

AtScale, vendor test, 410 questions[66]

- **16% → 72%** accuracy, in two steps: a knowledge graph over SQL, then ontology-based checks

Allemang and Sequeda[28]

Plain Text-to-SQL breaks on hard questions. On real sales data at LG Electronics, one model scored 93% on simple aggregations.[10] It fell to 4% on arithmetic reasoning and 31% on grouped rankings.[10] The common errors were wrong arithmetic logic, incomplete filters and wrong grouping.[10]

Part of the problem is the schema. Real schemas can have hundreds of columns, and only a few matter for one question.[7] Focusing generation on the relevant part of the schema improves accuracy.[7]

A semantic layer helps more than a better model. In one paired benchmark, each model ran with the schema only, then with a 4 KB document of measures, conventions and disambiguation rules.[17] Accuracy rose from 45.5–50.5% to 67.7–68.7%.[17] The document explained essentially all of the significant variance; model choice within tier did not.[17] The authors say explicit semantics change what the model is asked to do, not how capable it is.[17]

Vendor tests point the same way, with larger numbers. In AtScale's test, adding the layer to GPT-5 raised accuracy from 21.5% to 50.5%; switching to Gemini raised it only to 36.1%.[66] Schema documentation alone was not enough. Without the layer, the model scored about half as well.[66] Snowflake reported 78% for Cortex Analyst against 57% for a plain LLM on four BIRD subsets.[61] Each vendor measured its own product.

Better models do close part of the gap. In dbt Labs' test, newer models nearly doubled text-to-SQL accuracy, from 32.7% to 64.5%.[74] Within the semantic layer's scope, both tested models were correct 100% of the time.[74] A research agent that reasons over a curated semantic layer reached 94.15% execution accuracy on Spider2-snow.[31] A deterministic compiler turns its intermediate queries into SQL.[31]

Semantic layers also govern access. In Cube's design, row-level and role-based restrictions are applied when the query is compiled.[58] An agent therefore cannot build a cross-tenant query.[58] Databricks says its Metric Views compile each metric into deterministic SQL, whichever tool or agent asks.[52] Cube recommends known-answer evaluations: ambiguous wording, subtle joins, empty results and denied access.[58]

The failure mode matters as much as the score. When a semantic layer cannot answer, it returns an error; failed text-to-SQL can return a plausible but wrong answer.[74] The limit is scope: the layer answers only what has been modelled.[74] In dbt's test, adding 3 models let it answer every benchmark question.[74]

A knowledge graph helps in the same way. Question answering over a knowledge graph of the SQL database is more accurate than answering on SQL directly.[28] In that work, 8% of answers were an honest "I don't know".[28] Other systems report high scores on their own benchmarks: 94.7% on supply-chain root cause tasks[14] and 89.47% for a 4B-parameter ontology model.[29] Typed ontology worlds add a smaller but tested gain: +4.0 points on BIRD, with significance reported.[8]

The ontology study gives the most useful rule. The value of grounding is inversely proportional to how well the model's training data covers the domain.[5] Your internal terms are exactly what the model has not seen.

## Part IV

## Cases in production

Most evidence in this field comes from benchmarks. A few deployments report results from real use; they are collected here.

| Where | What was built | Reported result |
| --- | --- | --- |
| LinkedIn customer service | Knowledge graph built from past issue tickets; queries retrieve related sub-graphs[26] | Median per-issue resolution time down 28.6% over about six months[26] |
| Kuaishou operations | Causal graph from anomalous metrics; agents verify causality[12] | 77.3% less average diagnosis time; over six months in production[12] |
| Snowflake, internal | Semantic views as a context layer for agents[56] | More than 5,600 employees ran over 320,000 queries in July 2025[56] |
| OpenAI, internal | Data agent with a full context stack[49] | One complex question: 1 min 22 s instead of over 22 min[49] |
| Zep (agent memory) | Temporal knowledge graph of conversations and business data[34] | Up to 18.5% higher accuracy and 90% lower latency on LongMemEval[34] |

LinkedIn's case is the clearest. Plain RAG treated past tickets as flat text and lost their structure and links.[26] The graph kept both, and on benchmarks the method beat the baseline by 77.6% in MRR.[26] The production gain, 28.6% faster resolution, came from about six months with the customer service team.[26]

Memory is a second use. Zep's Graphiti engine combines conversations and structured business data in one graph and keeps historical relationships.[34] Because it keeps that history, an agent can see how a fact changed over time.[34]

The vendors' own claims are harder to weigh. Databricks says Genie, its data agent, no longer hallucinates metrics when built on Metric Views.[52] That is a product statement, not a measured result.

## Part V

## Operational ontologies: how agents act

An operational ontology adds actions to the types. Palantir's ontology joins data, logic, action and security in one representation.[37] An action is a single transaction that changes properties of one or more objects.[71] AIP logs every action taken by people or AI agents, and role-, marking- and purpose-based controls govern each one.[37]

Agents write through the same path, with a choice. AIP Logic functions can apply ontology edits automatically or stage them for human review.[67] The model cannot see data the user is not allowed to read.[67] But read-time access controls do not extend to the model's output or to the edits it composes.[67] The write path needs its own checks.

Microsoft takes a similar line. With a shared ontology, Fabric agents can monitor live data, detect anomalies and take governed action.[41] Its ontology agent proposes changes for review under a proposal-first model.[41] Custom agents connect to the ontology through the Model Context Protocol.[42]

The details of a write are less tidy than the diagrams. A writeback webhook can succeed in the external system while the ontology change fails.[71] Reverting an action does not revert side effects such as notifications or webhooks.[71] Automate action effects run at least once, not exactly once.[71] Palantir documents an action log, read and write authorizations, and consistency and isolation for action types.[43]

Open-source reimplementations show the parts. They mirror Foundry's object types, link types, action types and functions.[91] One adds OWL and SHACL export, because Foundry's ontology is proprietary and cannot export to W3C standards.[91] Another runs every action through resolve, validate, execute and record.[80] It keeps an append-only action log and an approval gate that returns approved, denied or pending.[80] A supply-chain example gives the AI agent its own restricted role.[81] Its MCP layer exposes approved capabilities but no autonomous critical writes.[81]

Research adds a simulation step. In VirtualSet, actions run first in a simulated world, and changes need external approval before they become real.[8] Agents reach these layers through tools: one manufacturing graph exposes 287 MCP tools as a SPARQL semantic layer.[9]

Two cautions apply. The vendor documents describe the design; they do not measure it. The reimplementations are simulations on synthetic data and do not run on Foundry.[88]

## Part VI

## Where machine learning goes

Machine learning belongs at the edges of the layer: it builds, extends and scores. The canonical model stays under deterministic checks and human review.

### Building the graph

LLMs moved knowledge graph construction from rules and statistics to generative methods.[22] The classic pipeline has three steps: ontology engineering, knowledge extraction and knowledge fusion.[22] On 80 annotated industrial reports, schema-guided prompting improved extraction quality significantly.[18] The models were open and local, from 7B to 32B parameters.[18] Another evaluation constrains extraction with an explicit ontology of six entity types and 96 relation types.[36] LLMs can also suggest OWL models at least as good as those of novice modellers.[24]

### Can the ontology update itself?

The instances can, under checks. One pipeline extracts entities and relations, validates them against SHACL and OWL constraints, and updates the graph continuously.[23] Another resolves mentions to canonical entities and builds the graph incrementally with deduplication.[39] The schema is different. Fine-tuned models can build the taxonomic backbone of an ontology,[15] but the authors of one pipeline recommend that people evaluate generated graphs.[19] The vendors build the same gate. Snowflake uses agents that infer table relationships and suggest edits to a semantic model.[61] Microsoft's ontology agent proposes changes for review.[41] In research, AgentOnto updates its ontology with confirmed feedback, and a real deployment showed practical value.[16]

Building a graph has a known shape. One guide describes five stages: scope, ontology and schema design, extraction, entity resolution, and validation before agents query it.[55] TigerGraph adds that schema design must come before ingestion.[65] Retrofitting a schema at enterprise scale means full re-extraction and typically takes months.[65]

Extraction is now cheap; resolution is not. For 10,000 documents and about 5M tokens, one estimate puts extraction at 80–200 USD, one-off.[72] Exact normalization catches 60–70% of duplicate entities, and embedding similarity another 20–25%.[72] Linking graph entities to operational records such as CRM IDs rarely works fully automatically.[72] Atlan names entity resolution and ontology alignment as the hard parts where enterprise builds stall.[55] It recommends a SHACL validation gate, and modelling iteratively rather than authoring a full OWL ontology first.[55]

Graph quality depends on steps a database licence does not supply: extraction accuracy, entity resolution and deduplication.[45] Practitioners report that the hardest part is the ontology design itself: which entity types matter and how granular to go.[77]

### Predicting links

Knowledge graph reasoning is often framed as link prediction, tested on datasets such as FB15k-237.[48] Graph neural networks and representation learning widened the use of knowledge graphs beyond search and recommendation.[93] A predicted link is a suggestion, not a fact. The pattern in the sources is consistent: a model proposes, and deterministic code or an expert decides.[6,19]

## Part VII

## Graphs in root cause analysis

AIOps is where graph ML already pays. Root cause analysis must correlate failures across telemetry inside service dependency graphs.[21] Supervised graph neural networks are the state of the art for finding the faulty component and the fault type.[4] A review of five years of RCA research names two main threads: dynamic causal discovery and fusion of metrics, logs and traces.[30]

| System | How it uses the graph | Reported result |
| --- | --- | --- |
| KRCA | Causal graph from anomalous metrics, then agents verify causality[12] | AC@1 of 0.88 and 0.79; 77.3% less diagnosis time in production[12] |
| GALA+ | Service dependencies bound the agent's exploration[21] | More than 25 points AC@1 over the best LLM baseline[21] |
| CHASE | Message passing over a multimodal invocation graph[2] | Up to 36.2% average gain on A@1[2] |
| Cascaded GNN | Splits large service graphs into communities[4] | Accuracy like centralized GNNs, near-constant latency as graphs grow[4] |

### Is correlation on a full graph deterministic?

Vendors say yes. Dynatrace contrasts correlation-based AI, probabilistic and human-verified, with causal AI, fact-based and automated.[64] Its analysis combines topological context with metric data.[64] It merges connected anomalies into a single problem to reduce alert load.[44] The research gives a more careful answer. Topology bounds the search, but it does not choose the cause. A causal graph learned from logs stays fixed and cannot learn from expert diagnoses.[6] EvoCause lets an LLM propose graph edits while code checks them.[6] At test time, the refined graph alone gives transparent predictions without an LLM call.[6] Names carry meaning too: anonymous alarm identifiers lowered Node F1 by 6.12 points.[6]

The best designs keep a deterministic check on the verdict. In one Kubernetes agent, graph and tool operations collect evidence, bound the search and check proposed verdicts.[13] It raised root-cause F1 from 0.6087 to 0.9130 on 23 scenarios.[13] Without scenario hints it kept 0.6958, and its authors call the gain benchmark-coupled.[13] A wide evaluation of microservice methods found that no single method is best in all situations.[25]

## Part VIII

## The map: tools and standards

The layer is built from parts that different vendors sell. This map lists the main options in each part, with links to keep researching.

### Semantic layers

| Tool | What it is | Link |
| --- | --- | --- |
| dbt Semantic Layer (MetricFlow) | Metrics, dimensions and entities defined once; MetricFlow generates the SQL deterministically[74] | [docs.getdbt.com](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl) |
| Cube Core | Open-source semantic layer (Apache 2.0) exposed over SQL, REST and GraphQL, and to agents over MCP[82,58] | [github.com/cube-js/cube](https://github.com/cube-js/cube) |
| Snowflake semantic views | Objects that translate business language into physical schemas, queryable with standard SQL[56] | [snowflake.com](https://www.snowflake.com/en/blog/snowflake-internal-context-layer-for-ai-agents/) |
| Databricks Unity Catalog metric views | Metrics defined once, queried from SQL, notebooks, dashboards and Genie agents; core open-sourced in Apache Spark[40,52] | [docs.databricks.com](https://docs.databricks.com/aws/en/uc-semantics/metric-views/) |
| AtScale | Semantic layer as a governed shared dictionary of business metrics[66] | [atscale.com](https://www.atscale.com/) |
| Microsoft Fabric IQ ontology | Ontology (preview) bound to live data; virtual layer over source systems[38,41] | [learn.microsoft.com](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview) |

### Ontology and knowledge graph platforms

| Platform | What it is | Link |
| --- | --- | --- |
| Palantir Foundry Ontology | Data, logic, action and security in one representation; actions logged and governed[37] | [palantir.com](https://www.palantir.com/platforms/ontology/) |
| Stardog | Semantic knowledge graph; its Voicebox turns plain-language questions into SPARQL over the graph and virtual sources[53] | [stardog.com](https://www.stardog.com/) |
| Neo4j | Property-graph database; GraphRAG follows relationships instead of similarity[62] | [neo4j.com](https://neo4j.com/) |
| Fluree | Knowledge graph that combines graph traversal, BM25 and vector search in one governed query[53] | [flur.ee](https://flur.ee/) |
| TigerGraph | Graph database; its guide sets five stages for a production knowledge graph with LLMs[65] | [tigergraph.com](https://www.tigergraph.com/) |

### GraphRAG and graph memory

| Tool | What it is | Link |
| --- | --- | --- |
| Microsoft GraphRAG | LLM extraction of entities and relationships, plus community reports[45] | [github.com/microsoft/graphrag](https://github.com/microsoft/graphrag) |
| LazyGraphRAG | Indexing at vector-RAG cost, 0.1% of full GraphRAG[75] | [microsoft.com/research](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) |
| LightRAG | 70–90% of GraphRAG's performance at 1/100th of the cost[77] | [github.com/HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) |
| Graphiti / Zep | Temporal knowledge graph engine for agent memory[34,89] | [github.com/getzep/graphiti](https://github.com/getzep/graphiti) |

### A standard for portability

Definitions locked in one tool are a known problem. The Open Semantic Interchange (OSI) specification defines a vendor-neutral model for data sets, metrics, dimensions, relationships and contexts.[68] Its v1.0 shipped on 27 January 2026 under Apache 2.0.[50] The dbt team positions it as the way definitions move between tools such as Snowflake and Tableau without being re-authored.[79]

OSI carries meaning only. It has no execution engine, and its v1.0 core does not codify access policy.[50] Adoption is still shallow: many of its 50-plus backers have joined, but fewer ship a lossless reader and writer.[50] Converters exist for dbt MetricFlow, GoodData, Salesforce and Apache Polaris.[50]

## What I would do

1. **Build the semantic layer before you change models.** Define your metrics, entities and rules once. In every test I read, that gave more accuracy than a better model.
2. **Write definitions before you index documents.** Agree the meaning of each business term and publish it where agents can read it. More context about an undecided term makes an agent more confidently wrong.
3. **Model the ontology before you buy a graph database.** Start with the object types and actions your agents need. Serve them as a virtual graph over the databases you already run.
4. **Put the ontology in the write path.** Every agent action is a typed action: validated, logged in append-only form, and behind an approval gate for anything critical. Check what the model writes, not only what it reads.
5. **Ground first where the model knows least.** Internal terms, local markets and your own metrics give the biggest lift. Generic knowledge gives the smallest.
6. **Use GraphRAG for multi-hop questions only, and measure it.** Test it against hybrid vector RAG with a reranker on your own questions. Count the tokens as well as the accuracy.
7. **Let ML propose, never commit.** Extraction and link prediction write suggestions. Deterministic checks or a person promote them into the graph.
8. **In operations, use the topology to bound the search.** Keep a deterministic check on every verdict, and track diagnosis time, not only accuracy.

*— Luis González*

## Method and limits

This report draws on an evidence pack of 97 sources published between 2019 and November 2026; 78 are cited below. They include research papers (most of them), official product documentation from Palantir, Microsoft, Databricks and Dynatrace, vendor benchmarks, and practitioner writing. Every figure in the text was checked against its source. The full evidence, with each source's extracted claims and verbatim quotes, is public in the [evidence pack](https://github.com/iamluisgb/reports/tree/master/data/research/knowledge-layer). This edition, updated on 11 November 2026, replaces earlier versions of 2 and 5 October. The recommendations in "What I would do" are mine.

- **Vendor benchmarks.** The dbt, AtScale and Snowflake figures measure each vendor's own product. Only one paired benchmark is independent; its direction matches theirs.
- **Few production numbers.** Most results come from benchmarks, often built by the authors. The production cases in Part IV are the exception, and each is reported by the company that built it.
- **Preprints.** Many papers are arXiv preprints, not yet peer-reviewed. Their figures are as reported.
- **Documentation, not measurement.** Palantir and Microsoft documents describe how the platforms work, not how well. Fabric IQ ontology is in preview.

## Sources

1. RAG vs. GraphRAG: A Systematic Evaluation and Key Insights — Han et al., arXiv, Feb 2025 — [arxiv.org/abs/2502.11371](https://arxiv.org/abs/2502.11371)
2. CHASE: A Causal Hypergraph based Framework for Root Cause Analysis in Multimodal Microservice Systems — Zhao et al., arXiv, Jun 2024 — [arxiv.org/abs/2406.19711](https://arxiv.org/abs/2406.19711)
3. PolyG: Adaptive Graph Traversal for Diverse GraphRAG Questions — Liu et al., arXiv, Apr 2025 — [arxiv.org/abs/2504.02112](https://arxiv.org/abs/2504.02112)
4. A Cascaded Graph Neural Network for Joint Root Cause Localization and Analysis in Edge Computing Environments — Fernando, Rodriguez, Buyya, arXiv, Mar 2026 — [arxiv.org/abs/2603.01447](https://arxiv.org/abs/2603.01447)
5. Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems — Luong Tuan, Sanyal, arXiv, Apr 2026 — [arxiv.org/abs/2604.00555](https://arxiv.org/abs/2604.00555)
6. EvoCause: LLM-Guided Evolution of Causal Graphs for Root Cause Analysis — Zan et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.27290](https://arxiv.org/abs/2607.27290)
7. Extractive Schema Linking for Text-to-SQL — Glass et al., arXiv, Jan 2025 — [arxiv.org/abs/2501.17174](https://arxiv.org/abs/2501.17174)
8. VirtualSet: Typed Ontology Worlds as an LLM Generation Target for Grounded Queries and Guarded Decisions — Zhang, arXiv, Jul 2026 — [arxiv.org/abs/2607.18821](https://arxiv.org/abs/2607.18821)
9. Semantic Graph Unification for Industrial Digital Threads — Chethan, arXiv, Aug 2026 — [arxiv.org/abs/2608.24918](https://arxiv.org/abs/2608.24918)
10. Fact-Consistency Evaluation of Text-to-SQL Generation for Business Intelligence Using Exaone 3.5 — Choi, arXiv, Apr 2025 — [arxiv.org/abs/2505.00060](https://arxiv.org/abs/2505.00060)
11. Graph-Augmented Retrieval for Cross-Entity Financial Sentiment Analysis: A Comparative Study — Rajan Bastakoti, Sagar Bhetwal, Nirajan Acharya, Gaurav Kumar Gupta, May 2026 — [arxiv.org/abs/2606.00062](https://arxiv.org/abs/2606.00062)
12. KRCA: An Efficient Root Cause Analysis System in Hyper-scale Microservice Systems via Agentic AI — Jiang et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.01788](https://arxiv.org/abs/2607.01788)
13. Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents — Kuvshinova, Jin, arXiv, Jun 2026 — [arxiv.org/abs/2606.08590](https://arxiv.org/abs/2606.08590)
14. Hypergraph Enterprise Agentic Reasoner over Heterogeneous Business Systems — Wang et al., arXiv, May 2026 — [arxiv.org/abs/2605.14259](https://arxiv.org/abs/2605.14259)
15. End-to-End Ontology Learning with Large Language Models — Lo et al., arXiv, Oct 2024 — [arxiv.org/abs/2410.23584](https://arxiv.org/abs/2410.23584)
16. AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics — Dayan Pan, Bincheng Zuo, Xiaojian Wang, Daogang Zhang, Jingyuan Wang, Oct 2026 — [arxiv.org/abs/2610.23317](https://arxiv.org/abs/2610.23317)
17. Semantic Layers for Reliable LLM-Powered Data Analytics: A Paired Benchmark of Accuracy and Hallucination Across Three Frontier Models — Michael Rumiantsau and Ivan Fokeev, Apr 2026 — [arxiv.org/abs/2604.25149](https://arxiv.org/abs/2604.25149)
18. LLM-Guided Ontology-Driven Knowledge Graph Construction from Unstructured Text — Belfadel et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.31663](https://arxiv.org/abs/2609.31663)
19. From human experts to machines: An LLM supported approach to ontology and knowledge graph construction — Kommineni, König-Ries, Samuel, arXiv, Mar 2024 — [arxiv.org/abs/2403.08345](https://arxiv.org/abs/2403.08345)
20. When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation — Xiang et al., arXiv, Jun 2025 — [arxiv.org/abs/2506.05690](https://arxiv.org/abs/2506.05690)
21. GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices — Tian et al., arXiv, Aug 2026 — [arxiv.org/abs/2608.08968](https://arxiv.org/abs/2608.08968)
22. LLM-empowered knowledge graph construction: A survey — Bian, arXiv, Oct 2025 — [arxiv.org/abs/2510.20345](https://arxiv.org/abs/2510.20345)
23. Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning — Salovskii, Gorshkova, arXiv, Apr 2026 — [arxiv.org/abs/2604.20795](https://arxiv.org/abs/2604.20795)
24. Knowledge Graph Construction-Based Semantic Web Application for Ontology Development — Thota et al., 2025 — [semanticscholar.org](https://www.semanticscholar.org/paper/772ca9590757a60938e349c5c78a6306665cc465)
25. CausalRCA: Causal Graph-Augmented Retrieval for Root Cause Analysis in Microservice Systems — Kou et al., 2026 — [semanticscholar.org](https://www.semanticscholar.org/paper/8f9bdd7024f51802322642b58132233dc2da9f0e)
26. Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering — LinkedIn — Apr 2024 — [arxiv.org/abs/2404.17723](https://arxiv.org/abs/2404.17723)
27. A Systematic Comparison of RAG Architectures for Geographic POI Question Answering Using OpenStreetMap Data — Otsuka, 2026 — [semanticscholar.org](https://www.semanticscholar.org/paper/28bf587adc26e4bbd1987f1e19d66b8c87dd752d)
28. Increasing the LLM Accuracy for Question Answering: Ontologies to the Rescue! — Allemang, Sequeda, arXiv, May 2024 — [arxiv.org/abs/2405.11706](https://arxiv.org/abs/2405.11706)
29. Construct, Align, and Reason: Large Ontology Models for Enterprise Knowledge Management — Zhang, Zhu, arXiv, Jan 2026 — [arxiv.org/abs/2602.00029](https://arxiv.org/abs/2602.00029)
30. Research on fault diagnosis and root cause analysis based on full stack observability — Hou, arXiv, Sep 2025 — [arxiv.org/abs/2509.12231](https://arxiv.org/abs/2509.12231)
31. A Semantic-Layer-Mediated Agent for Natural Language to SQL — Ha Jeong Kim, Saksonita Khoeurn, Ye Ji Yoon, Jun 2026 — [arxiv.org/abs/2606.31041](https://arxiv.org/abs/2606.31041)
32. How Significant Are the Real Performance Gains? An Unbiased Evaluation Framework for GraphRAG — Zeng et al., arXiv, 2025 — [arxiv.org/abs/2506.06331](https://arxiv.org/abs/2506.06331)
33. Beyond Vector Search: Comparing Classical RAG with Hybrid GraphRAG for Climate Science Q&A — Naiff, Alves, Pinto, arXiv, Aug 2026 — [arxiv.org/abs/2608.28766](https://arxiv.org/abs/2608.28766)
34. Zep: A Temporal Knowledge Graph Architecture for Agent Memory — Jan 2025 — [arxiv.org/abs/2501.13956](https://arxiv.org/abs/2501.13956)
35. Toward a Hybrid Ontology Framework for Semantic Data Understanding in AI-Augmented Data Warehousing — Sridharan et al., 2025 — [semanticscholar.org](https://www.semanticscholar.org/paper/29c2301457458a4ebbd6a6445e9af355ee4d7df1)
36. Large Language Models for Knowledge Graph Extraction — Markus Ilves, Eduard Barbu, Jaan Übi (University of Tartu), May 2026 — [aclanthology.org/2026.kallm-1.21.pdf](https://aclanthology.org/2026.kallm-1.21.pdf)
37. AIP architecture overview — Palantir documentation — [palantir.com/docs/foundry/architecture-center…](https://palantir.com/docs/foundry/architecture-center/aip-architecture/)
38. What Is Ontology (Preview)? — Microsoft Fabric — Oct 2026 — [learn.microsoft.com/en-us/fabric/iq/ontology/…](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)
39. graph-rag-agent: GraphRAG with private-domain deep search — GitHub, Nov 2025 — [github.com/1517005260/graph-rag-agent](https://github.com/1517005260/graph-rag-agent)
40. Unity Catalog metric views — Databricks docs — Oct 2026 — [docs.databricks.com/aws/en/uc-semantics/metri…](https://docs.databricks.com/aws/en/uc-semantics/metric-views/)
41. What is Fabric IQ? — Microsoft — Sep 2026 — [learn.microsoft.com/en-us/fabric/iq/overview](https://learn.microsoft.com/en-us/fabric/iq/overview)
42. Agent Integration Options for Ontology (Preview) — Microsoft — Sep 2026 — [learn.microsoft.com/en-us/fabric/iq/ontology/…](https://learn.microsoft.com/en-us/fabric/iq/ontology/concepts-agent-integration)
43. Action types • Overview — Palantir — [palantir.com/docs/foundry/action-types/overview](https://palantir.com/docs/foundry/action-types/overview/)
44. Root cause analysis — Dynatrace Docs — Feb 2023 — [docs.dynatrace.com/docs/dynatrace-intelligenc…](https://docs.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis)
45. GraphRAG vs Vector RAG: The 1000x Index Bill Is the Small Part — Rajesh Beri / THE D*AI*LY BRIEF, Oct 2026 — [beri.net/article/graphrag-vs-vector-rag-index…](https://www.beri.net/article/graphrag-vs-vector-rag-indexing-query-cost-lightrag-lazygraphrag-2026)
47. Context Layer vs Semantic Layer: What AI Agents Need — Noel Gomez / Datacoves, Nov 2026 — [datacoves.com/post/context-layer-vs-semantic-…](https://datacoves.com/post/context-layer-vs-semantic-layer)
48. AutoKG: LLMs for knowledge graph construction and reasoning — Zhu et al. (zjunlp), GitHub, Jan 2025 — [github.com/zjunlp/AutoKG](https://github.com/zjunlp/AutoKG)
49. What Is a Context Layer? A Definitive Guide for Enterprise AI — Julius Hollmann / digetiers, Jul 2026 — [digetiers.com/en/insights/library/what-is-a-c…](https://www.digetiers.com/en/insights/library/what-is-a-context-layer)
50. Apache Ossie (Open Semantic Interchange) Explained — Nilesh Kumar (Colrows), Aug 2026 — [colrows.com/blogs/open-semantic-interchange](https://colrows.com/blogs/open-semantic-interchange/)
52. Unity Catalog Business Semantics: Now GA and Open — Databricks — Apr 2026 — [databricks.com/blog/redefining-semantics-data…](https://www.databricks.com/blog/redefining-semantics-data-layer-future-bi-and-ai)
53. Best Enterprise Knowledge Graph Software in 2026 — Fluree — Jun 2026 — [flur.ee/blog/enterprise-kg-buyers-guide-2026](https://flur.ee/blog/enterprise-kg-buyers-guide-2026)
55. Knowledge Graph Construction for AI — Atlan — Emily Winks (Atlan), Jul 2026 — [atlan.com/know/ai-agent/knowledge-graph/knowl…](https://atlan.com/know/ai-agent/knowledge-graph/knowledge-graph-construction-for-ai/)
56. Building a Context Layer for AI Agents — Snowflake — Aniruth Narayanan / Snowflake, Aug 2026 — [snowflake.com/en/blog/snowflake-internal-cont…](https://www.snowflake.com/en/blog/snowflake-internal-context-layer-for-ai-agents/)
58. Semantic Layer for AI Agents (2026) — Cube — Oct 2026 — [cube.dev/articles/semantic-layer-for-ai-agent…](https://cube.dev/articles/semantic-layer-for-ai-agents-2026)
59. Context Layer Components for AI Agents — DataHub — Shirshanka Das (DataHub), Jun 2026 — [datahub.com/blog/context-layer-components](https://datahub.com/blog/context-layer-components/)
61. Agentic Semantic Model Improvement — Snowflake — Tom Zayats (Snowflake), Mar 2025 — [snowflake.com/en/blog/engineering/agentic-sem…](https://www.snowflake.com/en/blog/engineering/agentic-semantic-model-text-to-sql/)
62. Vector RAG vs. GraphRAG: Which retrieval do you need? — Neo4j — Enzo Htet, Neo4j, Sep 2026 — [neo4j.com/blog/agentic-ai/vector-rag-vs-graphrag](https://neo4j.com/blog/agentic-ai/vector-rag-vs-graphrag/)
64. What is causal AI? — Dynatrace — Bipin Singh / Dynatrace, Oct 2024 — [dynatrace.com/news/blog/what-is-causal-ai-det…](https://www.dynatrace.com/news/blog/what-is-causal-ai-deterministic-ai/)
65. Knowledge Graph with LLMs: Enterprise AI Guide — TigerGraph — Paige Leidig / TigerGraph, Jun 2026 — [tigergraph.com/blog/how-to-build-knowledge-gr…](https://www.tigergraph.com/blog/how-to-build-knowledge-graph-with-llms-for-enterprise-ai/)
66. Semantic Layer vs. a Better LLM for Text-to-SQL — AtScale — Ryan Siegler (AtScale); reviewed by Dave Mariani, Oct 2026 — [atscale.com/blog/semantic-layer-text-to-sql-a…](https://www.atscale.com/blog/semantic-layer-text-to-sql-accuracy/)
67. AIP Logic • Overview — Palantir documentation — [palantir.com/docs/foundry/logic/overview](https://palantir.com/docs/foundry/logic/overview/)
68. Open Semantic Interchange (OSI) Specification Finalized — Snowflake — Jan 2026 — [snowflake.com/en/blog/open-semantic-interchan…](https://www.snowflake.com/en/blog/open-semantic-interchanges-specs-finalized/)
71. When a Palantir Action Succeeds, What Has Changed? — dvdmaru, Aug 2026 — [dvdmaru.com/articles/palantir-ontology-02-act…](https://dvdmaru.com/articles/palantir-ontology-02-actions-en/)
72. Entity extraction with LLMs — from document to knowledge graph — Till Freitag, May 2026 — [till-freitag.com/en/blog/entity-extraction-ll…](https://till-freitag.com/en/blog/entity-extraction-llm-knowledge-graph-en)
74. Semantic Layer vs. Text-to-SQL: 2026 Benchmark Update — dbt Labs — Jason Ganz and Benoit Perigaud (dbt Labs), Apr 2026 — [docs.getdbt.com/blog/semantic-layer-vs-text-t…](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026)
75. LazyGraphRAG: Setting a new standard for quality and cost — Microsoft Research — Nov 2024 — [microsoft.com/en-us/research/blog/lazygraphra…](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
77. Graph RAG in 2026: What Actually Works in Production — Paperclipped, Mar 2026 — [paperclipped.de/en/blog/graph-rag-production](https://www.paperclipped.de/en/blog/graph-rag-production/)
79. What the Open Semantic Interchange (OSI) spec means — dbt Labs — Dave Connors (dbt Labs), Jan 2026 — [getdbt.com/blog/the-osi-spec-updates](https://www.getdbt.com/blog/the-osi-spec-updates)
80. actionTypesR: executable ontology actions — GitHub, May 2026 — [github.com/CathalByrneGit/actionTypesR](https://github.com/CathalByrneGit/actionTypesR)
81. operational-ontology: a lightweight operational ontology inspired by Foundry — GitHub, Aug 2026 — [github.com/Aryan1718/operational-ontology](https://github.com/Aryan1718/operational-ontology)
82. cube-js/cube: open-source semantic layer — [github.com/cube-js/cube](https://github.com/cube-js/cube)
87. graph-versus-vector: GraphRAG and vector RAG benchmark — GitHub, Sep 2026 — [github.com/GeenccMustafa/graph-versus-vector](https://github.com/GeenccMustafa/graph-versus-vector)
88. financial-ontology: payment settlement control system — GitHub, Sep 2026 — [github.com/nick-stafford/financial-ontology](https://github.com/nick-stafford/financial-ontology)
89. getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents — [github.com/getzep/graphiti](https://github.com/getzep/graphiti)
90. Semantic Web — Wikipedia — [en.wikipedia.org/wiki/Semantic_Web](https://en.wikipedia.org/wiki/Semantic_Web)
91. foundry-ontology-open: open implementation of Foundry's ontology architecture — GitHub, Jul 2026 — [github.com/cloudbadal007/foundry-ontology-open](https://github.com/cloudbadal007/foundry-ontology-open)
92. ontology-ingestion-layer: research notes on Palantir and Microsoft ontologies — Gabriel Cha, GitHub, Jul 2026 — [github.com/gabrielchasukjin/ontology-ingestion-layer](https://github.com/gabrielchasukjin/ontology-ingestion-layer)
93. Knowledge graph — Wikipedia — [en.wikipedia.org/wiki/Knowledge_graph](https://en.wikipedia.org/wiki/Knowledge_graph)
