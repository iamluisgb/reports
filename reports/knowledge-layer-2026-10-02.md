---
title: "The Knowledge Layer for Agents: Ontologies, Graphs and Where ML Fits"
date: 2026-10-02
type: special
url: https://luisgonzalezbernal.com/reports/reports/knowledge-layer-2026-10-02.html
summary: "What the layer is · GraphRAG versus vector RAG · Accuracy on enterprise data · Operational ontologies and actions · Where ML goes · Graphs in root cause analysis"
tags: [research, memory]
reading_time_minutes: 15
---
Memory & Knowledge · Special Report

# The *Knowledge Layer* for Agents: Ontologies, Graphs and Where ML Fits

2 Oct 2026 · Updated 5 Oct 2026

What the layer is · GraphRAG versus vector RAG · Accuracy on enterprise data · Operational ontologies and actions · Where ML goes · Graphs in root cause analysis

## Key findings

1. **Grounding helps most where the model knows least.** In 1,800 runs, ontology-coupled agents beat ungrounded agents on metric accuracy.[5] The lift in Vietnam-localized domains was 2x the lift in English domains.[5]
2. **A knowledge graph over SQL raises accuracy on enterprise questions.** Earlier benchmark work moved accuracy from 16% to 54% with a knowledge graph.[24] Adding ontology-based checks raised it to 72%, with an error rate of 20%.[24]
3. **GraphRAG gains are smaller than reported.** An unbiased evaluation of 3 GraphRAG methods found gains "much more moderate" than earlier claims.[27] Other studies report that GraphRAG often underperforms vanilla RAG on real tasks.[17]
4. **A typed ontology is also a guard.** On 1,072 BIRD questions, queries over typed ontology worlds scored 67.5% against 63.5% for direct SQL.[8] The same write chain stopped 20/20 hallucinated actions with zero false positives.[8]
5. **Most of the value is in joins across systems.** In a manufacturing graph, blocking 24 cross-system tools cut recall from 1.00 to 0.31.[9] 69% of the signals needed cross-system graph joins.[9]
6. **Graphs plus agents already work in operations.** A root cause system at Kuaishou has run in production for over six months.[11] It cut average diagnosis time by 77.3%.[11]

## Part I

## Four words for one layer

Ontology, knowledge graph, semantic layer and context layer name parts of one structure. The ontology is the blueprint: the type system of objects, links, actions and rules.[41] The knowledge graph is that blueprint filled with live instances.[41] A knowledge graph describes entities and their relationships, and a reasoner can derive new knowledge from it.[42]

The graph does not need its own database. A virtual knowledge graph answers queries from an existing relational database or data lake.[42] A set of mappings connects the source data to the graph structure and ontology.[42] The standards come from the Semantic Web: RDF and OWL encode meaning together with the data.[39]

The semantic layer brings the business vocabulary. One framework for data warehouses joins schema metadata with meaning taken from documentation, ETL scripts and business glossaries.[29] It reports better entity disambiguation, catalog enrichment and cross-system understanding.[29]

For agents, the layer must do more than retrieval. One practitioner write-up says the ontology is not a store of chunks for the prompt.[41] It is a live layer that many systems read and write at the same time.[41] Research frameworks say the same in formal terms. Enterprise systems today constrain what goes into an agent, but not what comes out.[5] An ontology layer can validate outputs and turn generation into a generate-verify-correct pipeline.[20]

*[Agents read the knowledge layer through typed queries and write through validated actions; ML proposes changes from the side]*

*How the parts fit: the ontology types the graph, agents read and write through it, and ML proposes changes that checks or people promote. Built from sources 41, 42, 20 and 16.*

## Part II

## GraphRAG versus vector RAG

GraphRAG retrieves facts along a graph instead of a list of similar chunks.[1] The evidence on its value is mixed. A systematic comparison found distinct strengths for RAG and for GraphRAG across tasks.[1] Combining the two gave consistent improvements.[1]

Evaluation is the weak point. GraphRAG methods are tuned to knowledge-graph QA benchmarks with few question patterns.[3] Common evaluations use unrelated questions and biased LLM judges.[27] With those flaws removed, the gains of 3 methods were much more moderate.[27]

The clearest gain is on multi-hop questions. These need facts from two or more passages, and flat top-k retrieval often finds only one.[37] In one public benchmark on HotpotQA, GraphRAG raised supporting-fact recall from 0.81 to 0.98.[37] In climate science, a hybrid of vector search and GraphRAG reported 177% more contextual recall than classical RAG.[28]

| Situation | What the evidence says |
| --- | --- |
| Multi-hop questions across passages | Graph retrieval finds the second fact that flat top-k misses[37] |
| Concepts spread across many articles | Hybrid local and global retrieval beats isolated text spans[28] |
| Relations computable from data (coordinates) | Explicit graph edges add little[23] |
| Different question patterns | Each needs its own traversal; a fixed strategy falls short[3] |
| Many real-world tasks | GraphRAG often underperforms vanilla RAG[17] |

## Part III

## Accuracy on enterprise data

Here the evidence for ontologies is stronger. The question is how well an LLM answers business questions over company data.

- **16% → 72%** accuracy from Text-to-SQL to an ontology-backed graph

Allemang and Sequeda, chat-with-the-data benchmark[24]

- **2x** ontology lift in Vietnam-localized domains over English ones

1,800 runs, three LLMs[5]

- **4%** accuracy on arithmetic business questions, against 93% on simple aggregations

219 questions on real sales data[10]

Plain Text-to-SQL breaks on hard questions. On real sales data at LG Electronics, one model scored 93% on simple aggregations.[10] It fell to 4% on arithmetic reasoning and 31% on grouped rankings.[10] The common errors were wrong arithmetic logic, incomplete filters and wrong grouping.[10]

Part of the problem is the schema. Real schemas can have hundreds of columns, and only a few matter for one question.[7] Focusing generation on the relevant part of the schema improves accuracy.[7]

A semantic model helps more. Question answering over a knowledge graph of the SQL database is more accurate than answering on SQL directly.[24] In that work, 8% of answers were an honest "I don't know".[24] Other systems report high scores on their own benchmarks: 94.7% on supply-chain root cause tasks[13] and 89.47% for a 4B-parameter ontology model.[25] Typed ontology worlds add a smaller but tested gain: +4.0 points on BIRD, with significance reported.[8]

The ontology study gives the most useful rule. The value of grounding is inversely proportional to how well the model's training data covers the domain.[5] Your internal terms are exactly what the model has not seen.

## Part IV

## Operational ontologies: how agents act

An operational ontology adds actions to the types. Palantir's model is one central ontology that joins data, logic, actions and security.[41] Its agents write back by design: an action is a transactional edit of the ontology.[41] Microsoft splits the work. Its data agents are read-only, and separate operations agents take actions.[41]

One documentation synthesis describes the write path step by step. The agent proposes an action. The system validates the action logic and the security scopes. A person can confirm it. The commit is one transaction, visible at once to every reader, and change data capture sends it back to the source systems.[41]

Open-source reimplementations show the parts. They mirror Foundry's object types, link types, action types and functions.[40] One adds OWL and SHACL export, because Foundry's ontology is proprietary and cannot export to W3C standards.[40] Another runs every action through resolve, validate, execute and record.[34] It keeps an append-only action log and an approval gate that returns approved, denied or pending.[34] A supply-chain example gives the AI agent its own restricted role.[35] Its MCP layer exposes approved capabilities but no autonomous critical writes.[35]

Research adds a simulation step. In VirtualSet, actions run first in a simulated world, and changes need external approval before they become real.[8] Agents reach these layers through tools: one manufacturing graph exposes 287 MCP tools as a SPARQL semantic layer.[9]

Two cautions apply. Vendor claims in this area are self-descriptions, not independent benchmarks.[41] The reimplementations are simulations on synthetic data and do not run on Foundry.[38]

## Part V

## Where machine learning goes

Machine learning belongs at the edges of the layer: it builds, extends and scores. The canonical model stays under deterministic checks and human review.

### Building the graph

LLMs moved knowledge graph construction from rules and statistics to generative methods.[19] The classic pipeline has three steps: ontology engineering, knowledge extraction and knowledge fusion.[19] On 80 annotated industrial reports, schema-guided prompting improved extraction quality significantly.[15] The models were open and local, from 7B to 32B parameters.[15] LLMs can also suggest OWL models at least as good as those of novice modellers.[21]

### Can the ontology update itself?

The instances can, under checks. One pipeline extracts entities and relations, validates them against SHACL and OWL constraints, and updates the graph continuously.[20] Another resolves mentions to canonical entities and builds the graph incrementally with deduplication.[30] The schema is different. Fine-tuned models can build the taxonomic backbone of an ontology,[14] but the authors of one pipeline recommend that people evaluate generated graphs.[16]

### Predicting links

Knowledge graph reasoning is often framed as link prediction, tested on datasets such as FB15k-237.[31] Graph neural networks and representation learning widened the use of knowledge graphs beyond search and recommendation.[42] A predicted link is a suggestion, not a fact. The pattern in the sources is consistent: a model proposes, and deterministic code or an expert decides.[6,16]

## Part VI

## Graphs in root cause analysis

AIOps is where graph ML already pays. Root cause analysis must correlate failures across telemetry inside service dependency graphs.[18] Supervised graph neural networks are the state of the art for finding the faulty component and the fault type.[4]

| System | How it uses the graph | Reported result |
| --- | --- | --- |
| KRCA | Causal graph from anomalous metrics, then agents verify causality[11] | AC@1 of 0.88 and 0.79; 77.3% less diagnosis time in production[11] |
| GALA+ | Service dependencies bound the agent's exploration[18] | More than 25 points AC@1 over the best LLM baseline[18] |
| CHASE | Message passing over a multimodal invocation graph[2] | Up to 36.2% average gain on A@1[2] |
| Cascaded GNN | Splits large service graphs into communities[4] | Accuracy like centralized GNNs, near-constant latency as graphs grow[4] |

### Is correlation on a full graph deterministic?

No, and the sources show why. Topology bounds the search, but it does not choose the cause. A causal graph learned from logs stays fixed and cannot learn from expert diagnoses.[6] EvoCause lets an LLM propose graph edits while code checks them.[6] At test time, the refined graph alone gives transparent predictions without an LLM call.[6] Names carry meaning too: anonymous alarm identifiers lowered Node F1 by 6.12 points.[6]

The best designs keep a deterministic check on the verdict. In one Kubernetes agent, graph and tool operations collect evidence, bound the search and check proposed verdicts.[12] It raised root-cause F1 from 0.6087 to 0.9130 on 23 scenarios.[12] Without scenario hints it kept 0.6958, and its authors call the gain benchmark-coupled.[12] A wide evaluation of microservice methods found that no single method is best in all situations.[22]

## What I would do

1. **Model the ontology before you buy a graph database.** Start with the object types and actions your agents need. Serve them as a virtual graph over the databases you already run.
2. **Put the ontology in the write path.** Every agent action is a typed action: validated, logged in append-only form, and behind an approval gate for anything critical.
3. **Ground first where the model knows least.** Internal terms, local markets and your own metrics give the biggest lift. Generic knowledge gives the smallest.
4. **Use GraphRAG for multi-hop questions only, and measure it.** Test it against plain vector RAG on your own questions before you adopt it.
5. **Let ML propose, never commit.** Extraction and link prediction write suggestions. Deterministic checks or a person promote them into the graph.
6. **In operations, use the topology to bound the search.** Keep a deterministic check on every verdict, and track diagnosis time, not only accuracy.

*— Luis González*

## Method and limits

This report replaces two earlier versions. "Ontologies, Graph Knowledge, Semantic Layer & Context Layer" (2 October 2026) listed 53 sources but cited none in the text. "Ontologies, Graph ML & AIOps" (1 October 2026) had no sources; its address now redirects here. The merged report was rebuilt on 5 October 2026 with the reports research pipeline. The pipeline found 227 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar. It read 46 sources in full, and 44 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 298 claims, each with a verbatim quote. 7 claims whose quote did not appear in the source were discarded. Claude wrote the synthesis from that evidence and checked every cited figure against its source. The conclusions in "What I would do" are mine.

- **No general web search.** The run had no web-search key. Official documentation from Palantir, Microsoft and semantic-layer vendors is missing. Palantir's design is described through one documentation synthesis and open-source reimplementations.
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
11. KRCA: An Efficient Root Cause Analysis System in Hyper-scale Microservice Systems via Agentic AI — Jiang et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.01788](https://arxiv.org/abs/2607.01788)
12. Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents — Kuvshinova, Jin, arXiv, Jun 2026 — [arxiv.org/abs/2606.08590](https://arxiv.org/abs/2606.08590)
13. Hypergraph Enterprise Agentic Reasoner over Heterogeneous Business Systems — Wang et al., arXiv, May 2026 — [arxiv.org/abs/2605.14259](https://arxiv.org/abs/2605.14259)
14. End-to-End Ontology Learning with Large Language Models — Lo et al., arXiv, Oct 2024 — [arxiv.org/abs/2410.23584](https://arxiv.org/abs/2410.23584)
15. LLM-Guided Ontology-Driven Knowledge Graph Construction from Unstructured Text — Belfadel et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.31663](https://arxiv.org/abs/2609.31663)
16. From human experts to machines: An LLM supported approach to ontology and knowledge graph construction — Kommineni, König-Ries, Samuel, arXiv, Mar 2024 — [arxiv.org/abs/2403.08345](https://arxiv.org/abs/2403.08345)
17. When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation — Xiang et al., arXiv, Jun 2025 — [arxiv.org/abs/2506.05690](https://arxiv.org/abs/2506.05690)
18. GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices — Tian et al., arXiv, Aug 2026 — [arxiv.org/abs/2608.08968](https://arxiv.org/abs/2608.08968)
19. LLM-empowered knowledge graph construction: A survey — Bian, arXiv, Oct 2025 — [arxiv.org/abs/2510.20345](https://arxiv.org/abs/2510.20345)
20. Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning — Salovskii, Gorshkova, arXiv, Apr 2026 — [arxiv.org/abs/2604.20795](https://arxiv.org/abs/2604.20795)
21. Knowledge Graph Construction-Based Semantic Web Application for Ontology Development — Thota et al., 2025 — [semanticscholar.org](https://www.semanticscholar.org/paper/772ca9590757a60938e349c5c78a6306665cc465)
22. CausalRCA: Causal Graph-Augmented Retrieval for Root Cause Analysis in Microservice Systems — Kou et al., 2026 — [semanticscholar.org](https://www.semanticscholar.org/paper/8f9bdd7024f51802322642b58132233dc2da9f0e)
23. A Systematic Comparison of RAG Architectures for Geographic POI Question Answering Using OpenStreetMap Data — Otsuka, 2026 — [semanticscholar.org](https://www.semanticscholar.org/paper/28bf587adc26e4bbd1987f1e19d66b8c87dd752d)
24. Increasing the LLM Accuracy for Question Answering: Ontologies to the Rescue! — Allemang, Sequeda, arXiv, May 2024 — [arxiv.org/abs/2405.11706](https://arxiv.org/abs/2405.11706)
25. Construct, Align, and Reason: Large Ontology Models for Enterprise Knowledge Management — Zhang, Zhu, arXiv, Jan 2026 — [arxiv.org/abs/2602.00029](https://arxiv.org/abs/2602.00029)
26. How Significant Are the Real Performance Gains? An Unbiased Evaluation Framework for GraphRAG — Zeng et al., arXiv, 2025 — [arxiv.org/abs/2506.06331](https://arxiv.org/abs/2506.06331)
27. Beyond Vector Search: Comparing Classical RAG with Hybrid GraphRAG for Climate Science Q&A — Naiff, Alves, Pinto, arXiv, Aug 2026 — [arxiv.org/abs/2608.28766](https://arxiv.org/abs/2608.28766)
28. Toward a Hybrid Ontology Framework for Semantic Data Understanding in AI-Augmented Data Warehousing — Sridharan et al., 2025 — [semanticscholar.org](https://www.semanticscholar.org/paper/29c2301457458a4ebbd6a6445e9af355ee4d7df1)
29. graph-rag-agent: GraphRAG with private-domain deep search — GitHub, Nov 2025 — [github.com/1517005260/graph-rag-agent](https://github.com/1517005260/graph-rag-agent)
30. AutoKG: LLMs for knowledge graph construction and reasoning — Zhu et al. (zjunlp), GitHub, Jan 2025 — [github.com/zjunlp/AutoKG](https://github.com/zjunlp/AutoKG)
31. actionTypesR: executable ontology actions — GitHub, May 2026 — [github.com/CathalByrneGit/actionTypesR](https://github.com/CathalByrneGit/actionTypesR)
32. operational-ontology: a lightweight operational ontology inspired by Foundry — GitHub, Aug 2026 — [github.com/Aryan1718/operational-ontology](https://github.com/Aryan1718/operational-ontology)
33. graph-versus-vector: GraphRAG and vector RAG benchmark — GitHub, Sep 2026 — [github.com/GeenccMustafa/graph-versus-vector](https://github.com/GeenccMustafa/graph-versus-vector)
34. financial-ontology: payment settlement control system — GitHub, Sep 2026 — [github.com/nick-stafford/financial-ontology](https://github.com/nick-stafford/financial-ontology)
35. Semantic Web — Wikipedia — [en.wikipedia.org/wiki/Semantic_Web](https://en.wikipedia.org/wiki/Semantic_Web)
36. foundry-ontology-open: open implementation of Foundry's ontology architecture — GitHub, Jul 2026 — [github.com/cloudbadal007/foundry-ontology-open](https://github.com/cloudbadal007/foundry-ontology-open)
37. ontology-ingestion-layer: research notes on Palantir and Microsoft ontologies — Gabriel Cha, GitHub, Jul 2026 — [github.com/gabrielchasukjin/ontology-ingestion-layer](https://github.com/gabrielchasukjin/ontology-ingestion-layer)
38. Knowledge graph — Wikipedia — [en.wikipedia.org/wiki/Knowledge_graph](https://en.wikipedia.org/wiki/Knowledge_graph)
