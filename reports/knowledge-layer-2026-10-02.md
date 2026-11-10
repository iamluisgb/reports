---
title: "The Knowledge Layer for Agents: Ontologies, Graphs and Where ML Fits"
date: 2026-10-02
type: special
url: https://luisgonzalezbernal.com/reports/reports/knowledge-layer-2026-10-02.html
summary: "What the layer is · GraphRAG versus vector RAG · Accuracy on enterprise data · Operational ontologies and actions · Where ML goes · Graphs in root cause analysis"
tags: [research, memory]
reading_time_minutes: 21
---
Memory & Knowledge · Special Report

# The *Knowledge Layer* for Agents: Ontologies, Graphs and Where ML Fits

2 Oct 2026 · Updated 10 Nov 2026

What the layer is · GraphRAG versus vector RAG · Accuracy on enterprise data · Operational ontologies and actions · Where ML goes · Graphs in root cause analysis

## Key findings

1. **A semantic layer is worth more than a better model.** In a vendor test of seven LLMs on 410 business questions, the semantic layer added 20 to 31 points to every model.[57] Switching models moved accuracy by at most 17.6 points.[57] An independent paired benchmark found +17 to +23 points, and model choice within a tier made no significant difference.[17]
2. **A knowledge graph over SQL raises accuracy on enterprise questions.** In the authors' first benchmark, a knowledge graph moved accuracy from 16% to 54%.[27] Ontology-based checks then raised it to 72%, a figure that includes 8% honest "I don't know" answers.[27] The error rate was 20%.[27]
3. **Grounding helps most where the model knows least.** In a controlled test of 1,800 runs across five industries and three LLMs, ontology-coupled agents gave more accurate metrics than ungrounded agents.[5] The lift was twice as large in Vietnam-localized domains as in English ones.[5] Your internal terms are the same case: the model has not seen them.
4. **GraphRAG costs far more and gains less than reported.** One benchmark measured 377 times as many prompt tokens per question as plain vector RAG.[42] An unbiased evaluation of 3 GraphRAG methods found gains "much more moderate" than earlier claims.[31]
5. **The platforms keep a person in the write path.** Palantir's AIP Logic applies ontology edits automatically or stages them for human review.[58] Microsoft's ontology agent proposes changes for review under a proposal-first model.[38] Read-time access controls do not cover the model's output or the edits it composes.[58]
6. **Most of the value is in joins across systems.** In a manufacturing graph, blocking 24 cross-system tools cut recall from 1.00 to 0.31.[9] 69% of the signals needed cross-system graph joins.[9]
7. **Graphs plus agents already work in operations.** A root cause system at Kuaishou has run in production for over six months.[12] It cut average diagnosis time by 77.3%.[12]

## Part I

## Four words for one layer

Ontology, knowledge graph, semantic layer and context layer name parts of one structure. The ontology is the blueprint: the type system of objects, links, actions and rules.[78] The knowledge graph is that blueprint filled with live instances.[78] A knowledge graph describes entities and their relationships, and a reasoner can derive new knowledge from it.[79]

The graph does not need its own database. A virtual knowledge graph answers queries from an existing relational database or data lake.[79] A set of mappings connects the source data to the graph structure and ontology.[79] The standards come from the Semantic Web: RDF and OWL encode meaning together with the data.[76]

The vendors now describe the same layer. Microsoft defines its Fabric IQ ontology as a machine-understandable business representation bound to live enterprise data.[38] It is a virtual layer: source data stays in its owning system.[36] Palantir calls its ontology the "nouns" and "verbs" of operational processes, legible to humans and agents.[35]

The semantic layer brings the business vocabulary. One framework for data warehouses joins schema metadata with meaning taken from documentation, ETL scripts and business glossaries.[33] It reports better entity disambiguation, catalog enrichment and cross-system understanding.[33]

For agents, the layer must do more than retrieval. One practitioner write-up says the ontology is not a store of chunks for the prompt.[78] It is a live layer that many systems read and write at the same time.[78] Research frameworks say the same in formal terms. Enterprise systems today constrain what goes into an agent, but not what comes out.[5] An ontology layer can validate outputs and turn generation into a generate-verify-correct pipeline.[23]

*[Agents read the knowledge layer through typed queries and write through validated actions; ML proposes changes from the side]*

*How the parts fit: the ontology types the graph, agents read and write through it, and ML proposes changes that checks or people promote. Built from sources 78, 79, 23 and 19.*

## Part II

## GraphRAG versus vector RAG

GraphRAG retrieves facts along a graph instead of a list of similar chunks.[1] The evidence on its value is mixed. A systematic comparison found distinct strengths for RAG and for GraphRAG across tasks.[1] Combining the two gave consistent improvements.[1]

Evaluation is the weak point. GraphRAG methods are tuned to knowledge-graph QA benchmarks with few question patterns.[3] Common evaluations use unrelated questions and biased LLM judges.[31] With those flaws removed, the gains of 3 methods were much more moderate.[31]

The clearest gain is on multi-hop questions. These need facts from two or more passages, and flat top-k retrieval often finds only one.[74] In one public benchmark on HotpotQA, GraphRAG raised supporting-fact recall from 0.81 to 0.98.[74] In climate science, a hybrid of vector search and GraphRAG reported 177% more contextual recall than classical RAG.[32]

The cost gap is large. GraphRAG indexing costs roughly 300x to 2,000x a vector index, because an LLM reads every chunk at least twice.[42] At query time, one benchmark measured 331,375 prompt tokens per question for global search, against 879 for vector RAG.[42] On fact retrieval over novels, reranked vector RAG scored 60.92 against 49.29 for Microsoft GraphRAG.[42] On complex reasoning, GraphRAG won: 50.93 against 42.93.[42]

Much of the gap closes without a graph. A hybrid of dense vectors, BM25 keyword search and a reranker closes most of it.[42] Where a graph does help, the gain is modest. In financial news, two-hop graph retrieval raised entity recall by 6.4%, and mean latency rose 22.6%.[11]

| Situation | What the evidence says |
| --- | --- |
| Multi-hop questions across passages | Graph retrieval finds the second fact that flat top-k misses[74] |
| Concepts spread across many articles | Hybrid local and global retrieval beats isolated text spans[32] |
| Relations computable from data (coordinates) | Explicit graph edges add little[26] |
| Different question patterns | Each needs its own traversal; a fixed strategy falls short[3] |
| Direct factual lookups in one chunk | Vector RAG is enough; a graph adds cost without accuracy[66] |
| Many real-world tasks | GraphRAG often underperforms vanilla RAG[20] |

## Part III

## Accuracy on enterprise data

Here the evidence is stronger. The question is how well an LLM answers business questions over company data.

- **+17 to +23** points of accuracy from a 4 KB semantic-layer document, across three models

Paired benchmark, 100 questions[17]

- **29 vs 14.6** points gained from a semantic layer against points gained from a model upgrade

AtScale, vendor test, 410 questions[57]

- **16% → 72%** accuracy, in two steps: a knowledge graph over SQL, then ontology-based checks

Allemang and Sequeda[27]

Plain Text-to-SQL breaks on hard questions. On real sales data at LG Electronics, one model scored 93% on simple aggregations.[10] It fell to 4% on arithmetic reasoning and 31% on grouped rankings.[10] The common errors were wrong arithmetic logic, incomplete filters and wrong grouping.[10]

Part of the problem is the schema. Real schemas can have hundreds of columns, and only a few matter for one question.[7] Focusing generation on the relevant part of the schema improves accuracy.[7]

A semantic layer helps more than a better model. In one paired benchmark, each model ran with the schema only, then with a 4 KB document of measures, conventions and disambiguation rules.[17] Accuracy rose from 45.5–50.5% to 67.7–68.7%.[17] The document explained essentially all of the significant variance; model choice within tier did not.[17] The authors say explicit semantics change what the model is asked to do, not how capable it is.[17]

Vendor tests point the same way, with larger numbers. In AtScale's test, adding the layer to GPT-5 raised accuracy from 21.5% to 50.5%; switching to Gemini raised it only to 36.1%.[57] Schema documentation alone was not enough. Without the layer, the model scored about half as well.[57] Snowflake reported 78% for Cortex Analyst against 57% for a plain LLM on four BIRD subsets.[52] Each vendor measured its own product.

Better models do close part of the gap. In dbt Labs' test, newer models nearly doubled text-to-SQL accuracy, from 32.7% to 64.5%.[64] Within the semantic layer's scope, both tested models were correct 100% of the time.[64] A research agent that reasons over a curated semantic layer reached 94.15% execution accuracy on Spider2-snow.[30] A deterministic compiler turns its intermediate queries into SQL.[30]

The failure mode matters as much as the score. When a semantic layer cannot answer, it returns an error; failed text-to-SQL can return a plausible but wrong answer.[64] The limit is scope: the layer answers only what has been modelled.[64] In dbt's test, adding 3 models let it answer every benchmark question.[64]

A knowledge graph helps in the same way. Question answering over a knowledge graph of the SQL database is more accurate than answering on SQL directly.[27] In that work, 8% of answers were an honest "I don't know".[27] Other systems report high scores on their own benchmarks: 94.7% on supply-chain root cause tasks[14] and 89.47% for a 4B-parameter ontology model.[28] Typed ontology worlds add a smaller but tested gain: +4.0 points on BIRD, with significance reported.[8]

The ontology study gives the most useful rule. The value of grounding is inversely proportional to how well the model's training data covers the domain.[5] Your internal terms are exactly what the model has not seen.

## Part IV

## Operational ontologies: how agents act

An operational ontology adds actions to the types. Palantir's ontology joins data, logic, action and security in one representation.[35] An action is a single transaction that changes properties of one or more objects.[61] AIP logs every action taken by people or AI agents, and role-, marking- and purpose-based controls govern each one.[35]

Agents write through the same path, with a choice. AIP Logic functions can apply ontology edits automatically or stage them for human review.[58] The model cannot see data the user is not allowed to read.[58] But read-time access controls do not extend to the model's output or to the edits it composes.[58] The write path needs its own checks.

Microsoft takes a similar line. With a shared ontology, Fabric agents can monitor live data, detect anomalies and take governed action.[38] Its ontology agent proposes changes for review under a proposal-first model.[38] Custom agents connect to the ontology through the Model Context Protocol.[39]

The details of a write are less tidy than the diagrams. A writeback webhook can succeed in the external system while the ontology change fails.[61] Reverting an action does not revert side effects such as notifications or webhooks.[61] Automate action effects run at least once, not exactly once.[61] Palantir documents an action log, read and write authorizations, and consistency and isolation for action types.[40]

Open-source reimplementations show the parts. They mirror Foundry's object types, link types, action types and functions.[77] One adds OWL and SHACL export, because Foundry's ontology is proprietary and cannot export to W3C standards.[77] Another runs every action through resolve, validate, execute and record.[68] It keeps an append-only action log and an approval gate that returns approved, denied or pending.[68] A supply-chain example gives the AI agent its own restricted role.[69] Its MCP layer exposes approved capabilities but no autonomous critical writes.[69]

Research adds a simulation step. In VirtualSet, actions run first in a simulated world, and changes need external approval before they become real.[8] Agents reach these layers through tools: one manufacturing graph exposes 287 MCP tools as a SPARQL semantic layer.[9]

Two cautions apply. The vendor documents describe the design; they do not measure it. The reimplementations are simulations on synthetic data and do not run on Foundry.[75]

## Part V

## Where machine learning goes

Machine learning belongs at the edges of the layer: it builds, extends and scores. The canonical model stays under deterministic checks and human review.

### Building the graph

LLMs moved knowledge graph construction from rules and statistics to generative methods.[22] The classic pipeline has three steps: ontology engineering, knowledge extraction and knowledge fusion.[22] On 80 annotated industrial reports, schema-guided prompting improved extraction quality significantly.[18] The models were open and local, from 7B to 32B parameters.[18] Another evaluation constrains extraction with an explicit ontology of six entity types and 96 relation types.[34] LLMs can also suggest OWL models at least as good as those of novice modellers.[24]

### Can the ontology update itself?

The instances can, under checks. One pipeline extracts entities and relations, validates them against SHACL and OWL constraints, and updates the graph continuously.[23] Another resolves mentions to canonical entities and builds the graph incrementally with deduplication.[37] The schema is different. Fine-tuned models can build the taxonomic backbone of an ontology,[15] but the authors of one pipeline recommend that people evaluate generated graphs.[19] The vendors build the same gate. Snowflake uses agents that infer table relationships and suggest edits to a semantic model.[52] Microsoft's ontology agent proposes changes for review.[38] In research, AgentOnto updates its ontology with confirmed feedback, and a real deployment showed practical value.[16]

Graph quality depends on steps a database licence does not supply: extraction accuracy, entity resolution and deduplication.[42] Practitioners report that the hardest part is the ontology design itself: which entity types matter and how granular to go.[66]

### Predicting links

Knowledge graph reasoning is often framed as link prediction, tested on datasets such as FB15k-237.[45] Graph neural networks and representation learning widened the use of knowledge graphs beyond search and recommendation.[79] A predicted link is a suggestion, not a fact. The pattern in the sources is consistent: a model proposes, and deterministic code or an expert decides.[6,19]

## Part VI

## Graphs in root cause analysis

AIOps is where graph ML already pays. Root cause analysis must correlate failures across telemetry inside service dependency graphs.[21] Supervised graph neural networks are the state of the art for finding the faulty component and the fault type.[4] A review of five years of RCA research names two main threads: dynamic causal discovery and fusion of metrics, logs and traces.[29]

| System | How it uses the graph | Reported result |
| --- | --- | --- |
| KRCA | Causal graph from anomalous metrics, then agents verify causality[12] | AC@1 of 0.88 and 0.79; 77.3% less diagnosis time in production[12] |
| GALA+ | Service dependencies bound the agent's exploration[21] | More than 25 points AC@1 over the best LLM baseline[21] |
| CHASE | Message passing over a multimodal invocation graph[2] | Up to 36.2% average gain on A@1[2] |
| Cascaded GNN | Splits large service graphs into communities[4] | Accuracy like centralized GNNs, near-constant latency as graphs grow[4] |

### Is correlation on a full graph deterministic?

Vendors say yes. Dynatrace contrasts correlation-based AI, probabilistic and human-verified, with causal AI, fact-based and automated.[55] Its analysis combines topological context with metric data.[55] It merges connected anomalies into a single problem to reduce alert load.[41] The research gives a more careful answer. Topology bounds the search, but it does not choose the cause. A causal graph learned from logs stays fixed and cannot learn from expert diagnoses.[6] EvoCause lets an LLM propose graph edits while code checks them.[6] At test time, the refined graph alone gives transparent predictions without an LLM call.[6] Names carry meaning too: anonymous alarm identifiers lowered Node F1 by 6.12 points.[6]

The best designs keep a deterministic check on the verdict. In one Kubernetes agent, graph and tool operations collect evidence, bound the search and check proposed verdicts.[13] It raised root-cause F1 from 0.6087 to 0.9130 on 23 scenarios.[13] Without scenario hints it kept 0.6958, and its authors call the gain benchmark-coupled.[13] A wide evaluation of microservice methods found that no single method is best in all situations.[25]

## What I would do

1. **Build the semantic layer before you change models.** Define your metrics, entities and rules once. In every test I read, that gave more accuracy than a better model.
2. **Model the ontology before you buy a graph database.** Start with the object types and actions your agents need. Serve them as a virtual graph over the databases you already run.
3. **Put the ontology in the write path.** Every agent action is a typed action: validated, logged in append-only form, and behind an approval gate for anything critical. Check what the model writes, not only what it reads.
4. **Ground first where the model knows least.** Internal terms, local markets and your own metrics give the biggest lift. Generic knowledge gives the smallest.
5. **Use GraphRAG for multi-hop questions only, and measure it.** Test it against hybrid vector RAG with a reranker on your own questions. Count the tokens as well as the accuracy.
6. **Let ML propose, never commit.** Extraction and link prediction write suggestions. Deterministic checks or a person promote them into the graph.
7. **In operations, use the topology to bound the search.** Keep a deterministic check on every verdict, and track diagnosis time, not only accuracy.

*— Luis González*

## Method and limits

This report replaces two earlier versions. "Ontologies, Graph Knowledge, Semantic Layer & Context Layer" (2 October 2026) listed 53 sources but cited none in the text. "Ontologies, Graph ML & AIOps" (1 October 2026) had no sources; its address now redirects here. The merged report was rebuilt on 5 October 2026 with the reports research pipeline. The pipeline found 227 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar. It read 46 sources in full, and 44 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 298 claims, each with a verbatim quote. 7 claims whose quote did not appear in the source were discarded. Claude wrote the synthesis from that evidence and checked every cited figure against its source. On 10 November 2026 the research was run again with general web search. I screened 36 web results from 8 TinyFish queries by hand and added them to the specialised sources. The run also kept 14 sources from the October run. The run found 281 search results and read 87 sources; Of these, 83 gave usable evidence. The model extracted 549 claims with verbatim quotes and discarded 27 whose quote was not in the source. GitHub repositories were read from their README. The conclusions in "What I would do" are mine.

- **Vendor benchmarks.** The dbt, AtScale and Snowflake figures measure each vendor's own product. Only one paired benchmark is independent, and its direction matches theirs.
- **Documentation, not measurement.** Palantir and Microsoft documents describe how the platforms work. They give no accuracy or safety figures. Fabric IQ ontology is in preview.
- **Author-built benchmarks.** Several results come from benchmarks the authors built themselves. One paper calls its own result verification, not independent validation.
- **Preprints.** Most papers are arXiv preprints, not peer-reviewed. Their figures are as reported and were not reproduced.

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
26. A Systematic Comparison of RAG Architectures for Geographic POI Question Answering Using OpenStreetMap Data — Otsuka, 2026 — [semanticscholar.org](https://www.semanticscholar.org/paper/28bf587adc26e4bbd1987f1e19d66b8c87dd752d)
27. Increasing the LLM Accuracy for Question Answering: Ontologies to the Rescue! — Allemang, Sequeda, arXiv, May 2024 — [arxiv.org/abs/2405.11706](https://arxiv.org/abs/2405.11706)
28. Construct, Align, and Reason: Large Ontology Models for Enterprise Knowledge Management — Zhang, Zhu, arXiv, Jan 2026 — [arxiv.org/abs/2602.00029](https://arxiv.org/abs/2602.00029)
29. Research on fault diagnosis and root cause analysis based on full stack observability — Hou, arXiv, Sep 2025 — [arxiv.org/abs/2509.12231](https://arxiv.org/abs/2509.12231)
30. A Semantic-Layer-Mediated Agent for Natural Language to SQL — Ha Jeong Kim, Saksonita Khoeurn, Ye Ji Yoon, Jun 2026 — [arxiv.org/abs/2606.31041](https://arxiv.org/abs/2606.31041)
31. How Significant Are the Real Performance Gains? An Unbiased Evaluation Framework for GraphRAG — Zeng et al., arXiv, 2025 — [arxiv.org/abs/2506.06331](https://arxiv.org/abs/2506.06331)
32. Beyond Vector Search: Comparing Classical RAG with Hybrid GraphRAG for Climate Science Q&A — Naiff, Alves, Pinto, arXiv, Aug 2026 — [arxiv.org/abs/2608.28766](https://arxiv.org/abs/2608.28766)
33. Toward a Hybrid Ontology Framework for Semantic Data Understanding in AI-Augmented Data Warehousing — Sridharan et al., 2025 — [semanticscholar.org](https://www.semanticscholar.org/paper/29c2301457458a4ebbd6a6445e9af355ee4d7df1)
34. Large Language Models for Knowledge Graph Extraction — Markus Ilves, Eduard Barbu, Jaan Übi (University of Tartu), May 2026 — [aclanthology.org/2026.kallm-1.21.pdf](https://aclanthology.org/2026.kallm-1.21.pdf)
35. AIP architecture overview — Palantir documentation — [palantir.com/docs/foundry/architecture-center…](https://palantir.com/docs/foundry/architecture-center/aip-architecture/)
36. What Is Ontology (Preview)? — Microsoft Fabric — Oct 2026 — [learn.microsoft.com/en-us/fabric/iq/ontology/…](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)
37. graph-rag-agent: GraphRAG with private-domain deep search — GitHub, Nov 2025 — [github.com/1517005260/graph-rag-agent](https://github.com/1517005260/graph-rag-agent)
38. What is Fabric IQ? — Microsoft — Sep 2026 — [learn.microsoft.com/en-us/fabric/iq/overview](https://learn.microsoft.com/en-us/fabric/iq/overview)
39. Agent Integration Options for Ontology (Preview) — Microsoft — Sep 2026 — [learn.microsoft.com/en-us/fabric/iq/ontology/…](https://learn.microsoft.com/en-us/fabric/iq/ontology/concepts-agent-integration)
40. Action types • Overview — Palantir — [palantir.com/docs/foundry/action-types/overview](https://palantir.com/docs/foundry/action-types/overview/)
41. Root cause analysis — Dynatrace Docs — Feb 2023 — [docs.dynatrace.com/docs/dynatrace-intelligenc…](https://docs.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis)
42. GraphRAG vs Vector RAG: The 1000x Index Bill Is the Small Part — Rajesh Beri / THE D*AI*LY BRIEF, Oct 2026 — [beri.net/article/graphrag-vs-vector-rag-index…](https://www.beri.net/article/graphrag-vs-vector-rag-indexing-query-cost-lightrag-lazygraphrag-2026)
45. AutoKG: LLMs for knowledge graph construction and reasoning — Zhu et al. (zjunlp), GitHub, Jan 2025 — [github.com/zjunlp/AutoKG](https://github.com/zjunlp/AutoKG)
52. Agentic Semantic Model Improvement — Snowflake — Tom Zayats (Snowflake), Mar 2025 — [snowflake.com/en/blog/engineering/agentic-sem…](https://www.snowflake.com/en/blog/engineering/agentic-semantic-model-text-to-sql/)
55. What is causal AI? — Dynatrace — Bipin Singh / Dynatrace, Oct 2024 — [dynatrace.com/news/blog/what-is-causal-ai-det…](https://www.dynatrace.com/news/blog/what-is-causal-ai-deterministic-ai/)
57. Semantic Layer vs. a Better LLM for Text-to-SQL — AtScale — Ryan Siegler (AtScale); reviewed by Dave Mariani, Oct 2026 — [atscale.com/blog/semantic-layer-text-to-sql-a…](https://www.atscale.com/blog/semantic-layer-text-to-sql-accuracy/)
58. AIP Logic • Overview — Palantir documentation — [palantir.com/docs/foundry/logic/overview](https://palantir.com/docs/foundry/logic/overview/)
61. When a Palantir Action Succeeds, What Has Changed? — dvdmaru, Aug 2026 — [dvdmaru.com/articles/palantir-ontology-02-act…](https://dvdmaru.com/articles/palantir-ontology-02-actions-en/)
64. Semantic Layer vs. Text-to-SQL: 2026 Benchmark Update — dbt Labs — Jason Ganz and Benoit Perigaud (dbt Labs), Apr 2026 — [docs.getdbt.com/blog/semantic-layer-vs-text-t…](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026)
66. Graph RAG in 2026: What Actually Works in Production — Paperclipped, Mar 2026 — [paperclipped.de/en/blog/graph-rag-production](https://www.paperclipped.de/en/blog/graph-rag-production/)
68. actionTypesR: executable ontology actions — GitHub, May 2026 — [github.com/CathalByrneGit/actionTypesR](https://github.com/CathalByrneGit/actionTypesR)
69. operational-ontology: a lightweight operational ontology inspired by Foundry — GitHub, Aug 2026 — [github.com/Aryan1718/operational-ontology](https://github.com/Aryan1718/operational-ontology)
74. graph-versus-vector: GraphRAG and vector RAG benchmark — GitHub, Sep 2026 — [github.com/GeenccMustafa/graph-versus-vector](https://github.com/GeenccMustafa/graph-versus-vector)
75. financial-ontology: payment settlement control system — GitHub, Sep 2026 — [github.com/nick-stafford/financial-ontology](https://github.com/nick-stafford/financial-ontology)
76. Semantic Web — Wikipedia — [en.wikipedia.org/wiki/Semantic_Web](https://en.wikipedia.org/wiki/Semantic_Web)
77. foundry-ontology-open: open implementation of Foundry's ontology architecture — GitHub, Jul 2026 — [github.com/cloudbadal007/foundry-ontology-open](https://github.com/cloudbadal007/foundry-ontology-open)
78. ontology-ingestion-layer: research notes on Palantir and Microsoft ontologies — Gabriel Cha, GitHub, Jul 2026 — [github.com/gabrielchasukjin/ontology-ingestion-layer](https://github.com/gabrielchasukjin/ontology-ingestion-layer)
79. Knowledge graph — Wikipedia — [en.wikipedia.org/wiki/Knowledge_graph](https://en.wikipedia.org/wiki/Knowledge_graph)
