---
title: "Ontologies, Graph Knowledge, Semantic Layer & Context Layer (2025–2026)"
date: 2026-10-02
type: special
url: https://luisgonzalezbernal.com/reports/reports/knowledge-layer-2026-10-02.html
summary: "Ontologies · GraphRAG · Semantic layer · Context layer · Convergence and adoption (2025–2026)"
tags: [agents, memory]
reading_time_minutes: 14
---
Knowledge Engineering · Special Report

# Ontologies, Graph Knowledge, *Semantic* & Context Layer

2 Oct 2026

Ontologies · GraphRAG · Semantic layer · Context layer · Convergence and adoption (2025–2026)

## Executive Summary

**The story of the year is convergence.** Ontologies, knowledge graphs, semantic layer and context layer have stopped being four silos and are fusing into a single architectural layer — the *knowledge layer* / *intelligence layer* — that the major data platforms already sell as a product.

**The semantic layer became agent infrastructure.** With reproducible data: dbt measured **98.2–100%** accuracy versus **84–90%** for pure text-to-SQL, with the critical difference that the semantic layer *fails with an error* while text-to-SQL "fails with a plausible but incorrect number".

**Semantic interoperability took a historic step.** Open Semantic Interchange became **Apache Ossie** (ASF incubation, July 2026), with a vendor-neutral specification for metrics, dimensions and ontologies.

**GraphRAG matured and deflated.** Benchmarks no longer sell it as universally superior: it wins on complex reasoning and global queries, but *loses on simple facts* against vector RAG. The winning pattern is **hybrid** (vector + graph + reranker).

**Ontology engineering was automated with LLMs** — but with a plot twist: at KGC 2026 the consensus is that the ontology is not the LLM's *output* but its **harness** (a declarative constraint). The standards keep pace: RDF 1.2, SHACL 1.2 and SPARQL-RL (Datalog rules for RDF, WD October 2026).

**The term of the year is "context graph"**: not yet another knowledge graph, but the record of *decision traces* (exceptions, precedents, approvals) that lets agents learn from prior work.

## Part I

## Landscape: four layers converging

The structural move of the period is that data platforms "compile" semantics into a governed context graph. The pattern repeating across Databricks, Snowflake, Microsoft, Google, AWS, Neo4j, Palantir, Graphwise and Stardog is a five-layer stack:

| Layer | What it provides |
| --- | --- |
| **1. Governed data assets** | OneLake, Unity Catalog, BigQuery, S3: identity, permissions and lineage |
| **2. Semantic layer** | Metrics, dimensions and entities: the mandatory starting point (Forrester) |
| **3. Ontology + knowledge graph** | Types, relations and rules: gives meaning and enables reasoning |
| **4. Context graph / memory** | Decision traces, state and precedent: consistent agents that improve |
| **5. Orchestration and retrieval** | GraphRAG, agentic retrieval, MCP/A2A with governance at query time |

*[Five-layer knowledge layer stack]*

*The five-layer stack repeating across Databricks, Snowflake, Microsoft, Google, AWS, Neo4j, Palantir, Graphwise and Stardog.*

> *📌 Takeaway:* the business case for convergence is **semantic duplication**: if every agent carries its own definition of "active customer", the company ends up with ten private copies of itself drifting in silence.

*[Semantic duplication versus shared substrate]*

*Lighter agents on a shared, governed substrate: the *knowledge layer* thesis versus semantic duplication.*

## Part II

## Ontologies and knowledge modeling

### W3C standards: the most active year in a decade

**RDF 1.2** is the first significant evolution of the RDF data model since 2014. It introduces **triple terms** (triples as first-class objects, with new reification) and the native `rdf:JSON` datatype, bridging RDF with JSON-LD.

**SHACL 1.2** is no longer just validation: it incorporates **declarative inference rules** for the first time. The verified primary document is **SPARQL 1.2 RL (SPARQL-RL)**, Working Draft of October 1, 2026: a **Datalog**-style rules language for RDF, with recursion, negation as failure and **stratification** to guarantee deterministic results.

**YAML-LD 1.0** published its first Working Draft (2026): conventions for serializing Linked Data in YAML, with media type `application/ld+yaml`, compatible with JSON-LD 1.1 and RDF 1.2.

*[2025-2026 standards timeline]*

*The milestones that structure the period: portable semantics (Apache Ossie) and agentic transport (MCP) converge in the second half of 2026.*

### LLMs and ontologies: from generators to constraints

Research in the period automates ontology engineering, but the consensus at the field's reference conference (**KGC 2026**) is nuanced: **LLMs fail as naive generators** (tangled hierarchies, inconsistent taxonomies, anti-patterns). The ontology becomes the **harness** — a declarative constraint — within which the LLM works.

### Empirical finding

In ontology learning, **model architecture and lineage can matter more than parameter count**. The quality jump concentrates between 9B and 27B; non-taxonomic relation extraction remains hard at every scale.

Sources: [KGC 2026](https://www.knowledgegraph.tech/) [When Does Bigger Help? (arXiv:2608.31118)](https://arxiv.org/abs/2608.31118)

## Part III

## Graph knowledge and GraphRAG

### The economics changed

GraphRAG's main historical barrier was indexing cost. **LazyGraphRAG** (Microsoft Research) defers all LLM usage to query time: indexing cost identical to vector RAG and **0.1%** of full GraphRAG, with **>700×** lower query cost for global queries. In parallel, **LightRAG** (EMNLP 2025 Findings) delivers 70–90% of GraphRAG quality at a fraction of the cost, and **FalkorDB** shipped a production-grade GraphRAG SDK.

### The benchmark verdict

**GraphRAG-Bench** (arXiv:2506.05690, v3 Feb 2026) answers "is GraphRAG actually effective?" with systematic evidence: **basic RAG matches or beats GraphRAG on simple fact retrieval**, while GraphRAG excels at complex reasoning, contextual summarization and creative generation. For multi-hop, approaches like **StepChain GraphRAG** combine question decomposition with BFS traversal over the graph.

### Hybrid is the standard

The 2026 consensus is that **none is universally better**. The winning architecture combines vector search (recall) + graph traversal (reasoning) + a reranker, fused with RRF. GraphRAG and LightRAG *do not replace* vector retrieval: they still use embeddings and ANN over nodes and communities, and add traversal.

*[Which retrieval layer to use by question type]*

*The year's decision is not "graph or no graph", but picking the layer by question type.*

> *⚠️ Nuance:* AWS demonstrated on managed infrastructure that GraphRAG's "global search" may not be optimal for thematic questions, and that methodology can be chosen per query over the same graph.

### Temporal memory and agentic GraphRAG

A different kind of graph is consolidating for **agent memory**: temporal graphs with timestamps and `supersedes` relations that prioritize the most current knowledge (Graphiti/Zep, Mem0). And the dominant pattern for agents is **exposing the graph as tools** via MCP with intent routing and *failure-aware routing*.

## Part IV

## Semantic layer

### From BI accessory to agent context

In 12 months the discourse moved from "semantic layer for dashboards" to "semantic layer as the agents' context layer". Gartner formalized it as a business decision: without governed semantics, agents hallucinate metrics. All three hyper-scalers and the independent vendors shipped governed semantics capabilities + MCP interfaces.

### Apache Ossie: the interoperability standard

Open Semantic Interchange (Snowflake, dbt, Salesforce, Google and 17 partners) became **Apache Ossie (Incubating)** on July 10, 2026, to avoid lock-in and provide neutral governance. Verified data: the repository opened in November 2025; the coalition grew from 17 to **over 50 organizations**; there are three working groups (**Metric Language, Catalog and Ontology**); the YAML/JSON specification for metrics, dimensions, relations and now **ontology** did not change with the renaming.

### Warehouse-native

| Platform | Development |
| --- | --- |
| **Snowflake** | Semantic Views GA + Semantic View Autopilot (Feb 2026): automates creation and maintenance |
| **Databricks** | Unity Catalog Business Semantics GA (Apr 2026): declarative Metric Views with materialization and query rewriting |
| **Google Looker** | The governed semantic layer feeds Gemini Enterprise via A2A, with multi-tenant security |

### dbt and the quantitative evidence

dbt's benchmark (April 2026, ACME Insurance dataset, 11 questions × 20 runs) is the most citable evidence of the year, and it was **verified directly against the primary source**:

| Model | Text-to-SQL | Semantic Layer |
| --- | --- | --- |
| Claude Sonnet 4.6 | 90.0% | **98.2%** |
| GPT-5.3 Codex | 84.1% | **100.0%** |

General text-to-SQL improved from 32.7% (2023) to 64.5% (2026). With just **3 additional dbt models** all 11 questions were covered. The operational takeaway: semantic layer for KPIs/audit/board reporting (fails explicitly), text-to-SQL for ad-hoc exploration.

*[Text-to-SQL versus semantic layer accuracy]*

*dbt benchmark (April 2026, 11 questions × 20 runs). The semantic layer turns a silent failure into an explicit error.*

### Semantic layer + ontology convergence

Ossie's **Ontology** working group, with **RelationalAI**, extended the specification to support **ontological semantics** beyond the dimensional model: entities, relations and constraints that enable multi-hop reasoning. It's the transition from "dimensional model for dashboards" to "executable ontology for agents".

## Part V

## Context layer and context engineering

### A formal discipline

Context engineering consolidated as a first-class discipline: curating the smallest set of high-signal tokens, treating context as a finite resource. LangChain contributed the operational taxonomy **write / select / compress / isolate**. The foundational empirical evidence is **context rot** (Chroma, Jul 2025): 18 frontier models degrade non-uniformly as input grows, even on trivial tasks.

### Long-horizon techniques

Anthropic formalized three techniques for tasks that exceed the window: **compaction** (summarize and restart), **structured note-taking** (external memory, `NOTES.md`) and **sub-agents** with clean context. The API exposes primitives: *context editing*, *memory tool* (`/memories`) and *server-side compaction*. Product memory evolved toward automatic temporal maintenance — the paradigmatic case is ChatGPT's **"Dreaming"**.

### Protocols: convergence under the Agentic AI Foundation

### MCP 2026-07-28 (verified against primary source)

The largest revision to date: **stateless protocol core** (`initialize`/`initialized` and `Mcp-Session-Id` removed), **Multi Round-Trip Requests (MRTR)**, header-based routing (`Mcp-Method`, `Mcp-Name`), cacheable lists, an extensions framework (Tasks, MCP Apps, Enterprise Managed Authorization), auth hardening and 12-month deprecation windows.

Sources: [MCP 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

**A2A**: v1.0, >150 organizations, complementary to MCP (MCP = tool/data access; A2A = agent-to-agent coordination). **AGENTS.md**: an open format adopted by >60,000 projects, donated to the Linux Foundation. The **AAIF** (Agentic AI Foundation), co-founded by OpenAI, Anthropic and Block, provides neutral governance for MCP and A2A.

### The triple layer

The distinction the market used to conflate is now articulated: the **knowledge graph** stores the world model ("how are things connected?"), the **semantic layer** defines what things mean ("what does this data mean?") and the **context layer** retrieves the right fragment at inference time ("what does the model need to know now?").

*[Knowledge graph, semantic layer and context layer]*

*Three different questions, three different layers: the graph stores the model, the semantic layer the meaning, the context layer the right fragment at the right time.*

## Part VI

## Convergence and enterprise adoption

### The "knowledge layer" as a concept

Neo4j formalized the **knowledge layer** as a shared, governed substrate with three components — **ontology** (living map), **enterprise data** (grounding) and **memory** (decision traces) — with the OBSL (ontology-based semantic layer) as the entry point. The thesis: "lighter agents on a smarter shared substrate".

### "Context graph", the term of the year

Foundation Capital described it as the accumulated record of **decision traces** (exceptions, overrides, precedents, cross-system approvals) that today lives in Slack and people's heads, not in warehouses (which sit on the *read path*, not the *write path* of the commit). Neo4j defines it as three-layer agent memory: long-term (= knowledge graph), short-term (conversation/state) and reasoning (decision traces, tool calls, evidence).

### The platforms

| Platform | Bet |
| --- | --- |
| **Microsoft IQ** | Fabric IQ (data + BI + ontology in preview, imports RDF/OWL), Foundry IQ (managed knowledge layer), Work IQ, Web IQ |
| **Google Knowledge Catalog** | Dataplex evolving toward a "dynamic context graph"; Gemini enrichment and access-control-aware search |
| **AWS** | Managed GraphRAG on Bedrock Knowledge Bases and Neptune Analytics |
| **Palantir** | The most mature ontology-first case: the Ontology as a digital operating system, AIP connecting LLMs and agents |

### Why projects fail

The 2026 diagnosis is that failure is **organizational and maintenance-related**, not technological:

- **Ontology drift**: the ontology silently drifts away from reality and results degrade invisibly.
- **"Boil the ocean"**: ontologies taking 6+ months with zero queries in production (one biotech spent 2 years building with zero active users).
- **Skills gap**: ~67% of abandoned enterprise KG projects cited lack of internal graph expertise; <15% make it from pilot to scale.
- **Underestimating maintenance**: reconciling entities ("Microsoft Corp" vs "Microsoft"), re-extracting and updating communities is the real cost, not the framework.

## In Numbers

-  dbt Semantic Layer vs text-to-SQL (Sonnet 4.6) **98.2% vs 90.0%**

-  Databricks Genie Ontology (first attempt) **84.5%**

-  Snowflake Cortex (ontology + GraphRAG) **50% → 78.2%**

-  LazyGraphRAG · indexing cost **0.1%**

-  AI adopters with KGs in production (2025) **~27%**

-  KG projects abandoned for lack of expertise **~67%**

## Conclusions

**1. Semantics became infrastructure, not a project.** Anyone building serious agents in 2026 doesn't choose between semantic layer, graph and context: they combine them into one governed layer.

**2. The architectural "winner" is hybrid and question-type-dependent.** Vector RAG for simple facts; graph for multi-hop and global queries; semantic layer for certified metrics; context graph for precedent and memory.

**3. Standards are finally converging** on two fronts: portable semantics (Apache Ossie) and neutral agentic transport (MCP/A2A under the Linux Foundation).

**4. LLM automation cheapened construction, not governance.** The bottleneck moved from "how to build it" to "how to maintain it and who owns the meaning".

**5. For a team starting today:** begin with the semantic layer (Forrester), adopt GraphRAG incrementally as multi-hop needs arise, and plan ontology governance and maintenance explicitly from day one.

## Watch

-   Apache Ossie: consolidation of the ontology specification and the semantic query spec

-   The semantic gap: whether KG adoption stops being flat in 2026–2027

-   Agentic GraphRAG: intent routing and failure-aware routing as the dominant pattern

-   Context graphs: from buzzword to governed decision-trace infrastructure

-   Independent evidence: most numbers are still internal vendor benchmarks

## Uncertainty & Limitations

**Source verification:** of 198 cited URLs, 169 returned 200, 28 returned 403 (exist but block bots) and 1 returned 404 (fixed). Critical claims were validated against primary sources (dbt, Apache Ossie, MCP, Databricks, LazyGraphRAG, W3C SPARQL-RL, Neo4j).

**2026 preprints without individual verification:** several works with 2026 arXiv identifiers were included from the subagents and were not checked one by one.

**Internal vendor benchmarks:** Databricks, Snowflake and dbt figures come from their own benchmarks with partially published methodology.

**Paywalled analysts:** Gartner and Forrester are cited from press releases or summary blogs; the full reports are not publicly verifiable.

**Out-of-window data point:** LazyGraphRAG dates to November 2024; it is cited as a foundational antecedent, not as an advance of the period.

## Sources

1. W3C — What's New in RDF 1.2: [https://www.w3.org/TR/rdf12-new/](https://www.w3.org/TR/rdf12-new/)
2. W3C — RDF 1.2 Concepts: [https://www.w3.org/TR/rdf12-concepts/](https://www.w3.org/TR/rdf12-concepts/)
3. W3C — SPARQL 1.2 RL (SPARQL-RL): [https://www.w3.org/TR/sparql12-rl/](https://www.w3.org/TR/sparql12-rl/)
4. W3C — SHACL 1.2 Core: [https://www.w3.org/TR/shacl12-core/](https://www.w3.org/TR/shacl12-core/)
5. W3C — YAML-LD 1.0: [https://www.w3.org/TR/yaml-ld-10/](https://www.w3.org/TR/yaml-ld-10/)
6. KGC 2026: [https://www.knowledgegraph.tech/](https://www.knowledgegraph.tech/)
7. Microsoft Research — LazyGraphRAG: [microsoft.com/…/lazygraphrag](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost)
8. Microsoft Research — Project GraphRAG: [microsoft.com/…/graphrag](https://www.microsoft.com/en-us/research/project/graphrag)
9. LightRAG (EMNLP 2025 Findings): [arXiv:2410.05779](https://arxiv.org/abs/2410.05779)
10. FalkorDB — GraphRAG SDK 1.0: [falkordb.com/…/graphrag-sdk](https://www.falkordb.com/blog/graphrag-sdk-knowledge-graph)
11. AWS — Unified Knowledge Graph RAG on AWS: [aws.amazon.com/…/unified-kg-rag](https://aws.amazon.com/blogs/opensource/unified-knowledge-graph-rag-on-aws-graphrag-and-lightrag-on-one-stack)
12. GraphRAG-Bench (arXiv:2506.05690): [arXiv:2506.05690](https://arxiv.org/abs/2506.05690)
13. Neo4j — What is GraphRAG: [neo4j.com/…/what-is-graphrag](https://neo4j.com/blog/genai/what-is-graphrag)
14. GraphRAG Pattern Catalog: [graphrag.com](https://graphrag.com)
15. Neo4j — The knowledge layer for enterprise AI: [neo4j.com/…/enterprise-knowledge-layer](https://neo4j.com/blog/agentic-ai/enterprise-knowledge-layer/)
16. StepChain GraphRAG (arXiv:2510.02827): [arXiv:2510.02827](https://arxiv.org/html/2510.02827v1)
17. Neo4j — Graphiti, knowledge graph memory: [neo4j.com/…/graphiti](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/)
18. Agentic GraphRAG (arXiv:2605.18770): [arXiv:2605.18770](https://arxiv.org/html/2605.18770v1)
19. dbt Labs — Semantic Layer vs. Text-to-SQL: 2026 Benchmark: [docs.getdbt.com/…/semantic-layer-vs-text-to-sql-2026](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026)
20. Apache Ossie — Enters Apache Incubator: [ossie.apache.org/…/ossie-enters-apache-incubator](https://ossie.apache.org/updates/ossie-enters-apache-incubator/)
21. Apache Ossie — Repository: [github.com/apache/ossie](https://github.com/apache/ossie)
22. Snowflake — Overview of semantic views: [docs.snowflake.com/…/views-semantic](https://docs.snowflake.com/en/user-guide/views-semantic/overview)
23. Snowflake Engineering — Ontology-grounded Cortex Agents: [snowflake.com/…/ontology-grounded-cortex-agents](https://www.snowflake.com/en/blog/engineering/ontology-grounded-cortex-agents/)
24. Databricks — Genie One, Genie Agents, and Genie Ontology: [databricks.com/…/genie-ontology](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents)
25. Databricks — Unity Catalog Business Semantics (GA): [databricks.com/…/redefining-semantics](https://www.databricks.com/blog/redefining-semantics-data-layer-future-bi-and-ai)
26. Google Cloud — Introducing the Google Cloud Knowledge Catalog: [cloud.google.com/…/knowledge-catalog](https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog)
27. Google Cloud — Looker's semantic layer governs Gemini Enterprise: [cloud.google.com/…/looker-gemini-enterprise](https://cloud.google.com/blog/products/business-intelligence/integrating-looker-and-gemini-enterprise)
28. Cube — Semantic Layer for AI Agents: [cube.dev/…/semantic-layer-for-ai-agents-2026](https://cube.dev/articles/semantic-layer-for-ai-agents-2026)
29. RelationalAI — Ontological Semantics to OSI: [relational.ai/…/ontological-semantics-osi](https://www.relational.ai/post/bringing-ontological-semantics-to-open-semantic-interchange-osi)
30. Gartner — Lack of Semantics Causes Inaccurate AI Agents: [gartner.com/…/lack-of-semantics](https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-says-lack-of-semantics-causes-inaccurate-artificial-intelligence-agents-and-wasted-spending)
31. Forrester — Build Meaning Before Machines: [forrester.com/…/build-meaning-before-machines](https://www.forrester.com/blogs/build-meaning-before-machines-why-semantics-ontologies-and-knowledge-graphs-matter-for-agentic-ai/)
32. Anthropic — Effective context engineering for AI agents: [anthropic.com/…/effective-context-engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
33. LangChain — Context Engineering: [langchain.com/…/context-engineering-for-agents](https://www.langchain.com/blog/context-engineering-for-agents)
34. Chroma — Context Rot: [trychroma.com/research/context-rot](https://www.trychroma.com/research/context-rot)
35. MCP Blog — The 2026-07-28 Specification: [blog.modelcontextprotocol.io/posts/2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
36. Linux Foundation — A2A Protocol Surpasses 150 Organizations: [linuxfoundation.org/…/a2a-150-organizations](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
37. AGENTS.md: [agents.md](https://agents.md/)
38. OpenAI — Agentic AI Foundation: [openai.com/index/agentic-ai-foundation](https://openai.com/index/agentic-ai-foundation/)
39. Anthropic — Memory tool: [platform.claude.com/…/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
40. OpenAI — Dreaming: Better memory for ChatGPT: [openai.com/index/chatgpt-memory-dreaming](https://openai.com/index/chatgpt-memory-dreaming/)
41. Microsoft Learn — What is Foundry IQ?: [learn.microsoft.com/…/foundry-iq](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq)
42. Microsoft Learn — What is Fabric IQ?: [learn.microsoft.com/fabric/iq/overview](https://learn.microsoft.com/en-us/fabric/iq/overview)
43. Foundation Capital — Context graphs: [foundationcapital.com/…/context-graphs](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity)
44. AWS — Build GraphRAG with Bedrock Knowledge Bases: [aws.amazon.com/…/graphrag-bedrock](https://aws.amazon.com/blogs/machine-learning/build-graphrag-applications-using-amazon-bedrock-knowledge-bases/)
45. Palantir — AIP architecture overview: [palantir.com/docs/…/aip-architecture](https://palantir.com/docs/foundry/architecture-center/aip-architecture/)
46. Graphwise — Merger (SWC + Ontotext): [graphwise.ai/…/merger](https://graphwise.ai/blog/graphwise-merger-swc-ontotext/)
47. Stardog — Knowledge Graph-Powered Semantic Layer: [stardog.com](https://www.stardog.com/)
48. A Survey of Context Engineering for LLMs (arXiv:2507.13334): [arXiv:2507.13334](https://arxiv.org/abs/2507.13334)
49. A-MEM: Agentic Memory for LLM Agents (arXiv:2502.12110): [arXiv:2502.12110](https://arxiv.org/abs/2502.12110)
50. Gartner — 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026: [gartner.com/…/40-percent-enterprise-apps](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
51. SiliconANGLE — 2026 data predictions: [siliconangle.com/…/2026-data-predictions](https://siliconangle.com/2026/01/18/2026-data-predictions-scaling-ai-agents-via-contextual-intelligence/)

Report generated with a multi-agent deep research pipeline (5 parallel subagents, 198 sources, URL integrity verification). Detailed per-area sources are in the research repository.
