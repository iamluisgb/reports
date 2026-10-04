---
title: "Ontologies, Graph ML & AIOps: Where the ML Actually Goes"
date: 2026-10-01
type: special
url: https://luisgonzalezbernal.com/reports/reports/ontology-graph-ml-aiops-2026-10-01.html
summary: "Palantir ontology · Governance · Link prediction · AIOps layers · The determinism question · Foundry mapping · 5 diagrams · Reading list"
tags: [models, memory]
reading_time_minutes: 11
---
Data Architecture · Special Report

# Ontologies, *Graph ML* & AIOps: Where the ML Actually Goes

01 Oct 2026

Palantir ontology · Governance · Link prediction · AIOps layers · The determinism question · Foundry mapping · 5 diagrams · Reading list

## 01 · Foundation

## The principle that explains everything

Palantir sells neither a database nor a dashboard. It sells an **operational ontology layer over data that never leaves your network**. Three core ideas:

- **Radical security-first** — the platform deploys *inside* the customer's infrastructure (air-gapped for Gotham, VPC for Foundry). Every object carries *provenance* and *ACLs at the property/row level*, not table level. Two analysts see "the same" Maduro with different attributes.
- **The ontology is the product** — not documentation: the runtime.
- **Operational loop** — you don't just read data; you *act* on the real world via Actions, and the result flows back into the system.

*[Palantir platform pipeline: sources to apps, with writeback loop]*

### Pipeline, layer by layer

- **1. Ingestion** — connectors for everything (Kafka, S3, JDBC, APIs, OSINT feeds; Gotham adds intel formats).
- **2. Pipelines** — immutable lakehouse-style datasets, Spark transforms, versioned, full lineage, inherited ACLs. RAW → CLEAN layers.
- **3. Ontology** — three sub-layers:

  - *Semantic*: Objects, typed Links, Properties (bound to clean datasets).
  - *Kinetic*: Actions — validated, permissioned mutations with writeback.
  - *Dynamic*: models/simulations operating over the ontology.

- **4. Apps** — Gotham (Graph, Map, Mission Command) for defense/intel; Foundry (Workshop, Contour, Quiver) for enterprise; AIP on top: LLMs constrained to registered Functions/Actions.
- **5. Apollo** — continuous delivery *of the platform itself* into air-gapped environments.

>  **Gotham vs Foundry in one line:** same substrate (data hub + ontology + Apollo). They differ in app packaging, deployment environments, and compliance. Foundry is Gotham that crossed to the commercial market.

## 02 · Governance

## Does the ontology update itself?

Both — but in different layers. The distinction is exactly what makes Palantir work: **the system flows; the contract does not.**

| Layer | Updates automatically? | Governance |
| --- | --- | --- |
| Schema (types, links, actions) | No | Humans, via branching + release (Ontology Manager). Granular edit permissions. A schema change is a deployment. |
| Instances (objects, values) | Yes — every pipeline run | Source data + ACLs. Each write carries provenance of which transform wrote it and when. |
| Entity resolution / merges | Semi-auto | Auto-merge above confidence threshold; below it, a human review queue. Matchers and thresholds are human-tuned. |
| ML-predicted relations | Suggested automatically | Live in a `predicted` state with confidence score; promoted to the canonical graph only on human approval. |

*[Instance layer flows freely, suggestion layer is gated by human review]*

>  **Why not let the system invent entities?** The ontology is the *operational contract*: if the `Person` object changes shape, Workshop apps, validated Actions, and AIP agents break. A self-mutating schema means nobody can trust what breaks tomorrow — same reason you don't let an LLM invent its own tool schema in production.

## 03 · Graph ML

## Link prediction & scoring — what it's for

The intuition: real-world graph edges are **not randomly distributed** — homophily, triadic closure, repeated structural roles. GNNs/embeddings (node2vec, TransE/RotatE, GraphSAGE, temporal GATs) compress that structure; the "missing" edges tend to be the most similar pairs in that space.

### Use cases, most mature first

- **Intelligence / OSINT** — filling the graph where no explicit data exists: shared addresses, phones, co-occurring events → predicted `ASSOCIATE_OF` with evidence list. Also *bridge nodes* (the obscure freight forwarder between an exporter and a sanctioned entity) and *temporal prediction* of future relationships as early warning.
- **Fraud & financial crime** — collusion rings visible as structural patterns (stars, cycles) that row-level classifiers miss; sanctions/KYC beneficial ownership behind shell layers.
- **Health / biotech** — drug repurposing via predicted `treats` edges on Drug–Disease–Protein graphs; DDI prediction before clinical reports.
- **Recommendation / search** — "people also bought"; knowledge-graph completion so semantic search never returns empty just because an edge wasn't recorded.
- **Cybersecurity** — alert triage via graph proximity instead of static signatures; supply-chain risk from dependency/maintainer graph position.

>  **The limit — and why predictions stay suggestions:** a high score can mean "real undocumented relationship" *or* "dataset bias" (surveillance feeds cover watched actors more, so the model predicts more links for the already-watched — a surveillance feedback loop). The model sees structure, not evidence. That separation is the difference between an investigation system and one that automates accusations.

## 04 · Mechanics

## From a graph to ML-ready data

A graph isn't directly consumable — you must **vectorize**. Three levels:

*[Input graph vectorized three ways into an embedding matrix feeding downstream tasks]*

1. **Node features** — properties (age, type, country) encoded one-hot/normalized → classic tabular ML. Ignores structure.
2. **Topological features** — degree, clustering coefficient, centralities (PageRank, betweenness), community ID (Louvain/Leiden), k-hop counts. Computed with Neo4j GDS / NetworkX / igraph. Now a simple classifier sees structural patterns.
3. **Embeddings** — node2vec/DeepWalk (random walks → word2vec) or GNNs (GraphSAGE, GAT: aggregate neighbor embeddings over 2–3 hops). Output: an `N × d` matrix feeding classification, link prediction, clustering, or GraphRAG context.

>  **Training data comes from the graph itself:** existing edges are the positives; sampled unconnected pairs are the negatives (*negative sampling*).

## 05 · Application

## AIOps: where ML pays, layer by layer

| Layer | Value | Risk | Maturity | Notes |
| --- | --- | --- | --- | --- |
| Dedup / correlation / suppression | ★★★★★ | Low | High | Embeddings + temporal co-occurrence → event graph → community detection. 4,000 alerts → 1 incident. Unsupervised; failure is benign. |
| Change correlation | ★★★★★ | Low | High | 80% of incidents follow a deploy/config change. Almost trivial ML, highest value per unit of effort. If your v1 lacks this, it's misdesigned. |
| Anomaly detection | ★★★★ | Medium — false positives | High | STL/Prophet for seasonal baselines; time-series foundation models (Chronos, TimesFM, Moirai) for zero-shot multivariate. Precision beats recall: a pager that cries wolf 3× is dead. |
| RCA via dependency graph | ★★★★★ | High — stale topology | Medium | Project anomalous nodes onto the service graph → random walk with restart / Bayesian propagation → ranked root causes. The moat is graph freshness, not the model. CMDBs are rotten: infer topology from traces/flows. |
| LLM synthesis | ★★★★ | Low | Med-high | Incident timeline consolidation, RCA drafts, semantic runbook retrieval, natural-language querying with restricted tools. Not for primary detection. |
| LLM as detector | ★ | — | Hype | Expensive, slow, less precise than a dynamic threshold. Don't. |

### Reference architecture

*[Layered AIOps architecture from signals to human decision, with feedback loop]*

>  **The pattern (same as Gotham):** classic ML detects, the graph correlates, the LLM synthesizes, the human decides. AIOps products fail when they invert the order — asking the LLM to do the first three layers.

## 06 · The hard question

## "If I have the full graph, isn't correlation deterministic?"

Partly right — and the right part matters: **if** the graph were complete, fresh, and signals mapped cleanly to nodes, correlation would be graph traversal + time window. Dynatrace Davis sells exactly that as "deterministic causal inference". But that *if* breaks in four places, and each break is where ML enters:

1. **The graph is never complete or fresh.** Declared topology (CMDB, IaC) is the desired state; reality has undeclared dependencies (DNS, shared NTP, that lambda writing to that queue). Inferring real topology from traces/flows is statistical — there is no deterministic way to discover an undeclared edge.
2. **The signal→node mapping is noisy.** Input is 4,000 strings, not nodes. Mapping `timeout in payment-svc` + `upstream 504` + an anonymous nginx log to the same node is entity extraction: deterministic for formatted data, ML for the rest.
3. **Connectivity doesn't distinguish cause from coincidence.** During a traffic spike the LB, gateway and Kafka all touch half the system — everything is "connected". Traversal yields dozens of plausible causal paths. You must *weight* edges (probability that a failure here produces *that* signal there), and those conditionals aren't in the topology: *they're learned from data*. Known structure + estimated parameters = a graphical model.
4. **"Anomalous" is statistical by definition.** The graph says what connects to what, not whether a latency spike is an incident or legitimate 9am traffic. That's baseline modeling.

*[Clean declared topology versus messy observed reality with undeclared dependencies]*

>  **The honest design:** determinism where there is structure (topology, causal inference, propagation rules); statistics where there is uncertainty (edge weights, anomaly detection, text→entity mapping).

 ML doesn't replace "connecting nodes" — it prices the connections and cleans the input. If your system were as observable and deterministic as the ideal graph, you wouldn't need AIOps: you'd have production tests. **ML exists because what you observe is noisy, not because the system is.**

## 07 · Product mapping

## Does Foundry do any of this?

Not turnkey AIOps like Dynatrace — but it is precisely the **substrate** where that layered stack gets built (Palantir sells this pattern to industrials as "intelligent operations"):

| AIOps layer | In Foundry |
| --- | --- |
| Streaming ingestion | Data Connection (Kafka, Kinesis, OPC-UA) + Pipeline Builder |
| Log templating / normalization | Spark transforms; output = ontology *Objects*, not loose rows |
| Time-series storage | Chronograph (native TS service inside Foundry) |
| Anomaly detection | Models in the Model Repository; predictions **written back as object properties** (`pump-42.anomalyScore = 0.93`) |
| Event clustering → incidents | Pipelines over materialized event objects; community detection batch/streaming |
| Dependency graph | The ontology *is* the dependency graph (Service/Database objects, typed links) — populated from CMDB or inferred; you choose how much to trust it |
| RCA / propagation | Ontology functions + graph analytics; the root-cause ranking is just another model writing a property |
| LLM synthesis | AIP: agents whose only action surface is registered Functions/Actions — no direct lake access |
| Operational writeback | Actions: "create ticket", "change setpoint", "escalate" — with ACLs and audit trail |
| Feedback loop | Every Action/decision becomes data → labels for retraining |

### Differentiators — and what Foundry does *not* give you

- **ML predictions are first-class ontology citizens** — scored values live as properties with provenance, ACLs and versioning. The object knows which values are measured and which are predicted (the suggestion-vs-evidence separation again).
- **Closed loop with Actions** — detection is half; acting with permissions and audit, feeding results back, is the other half. AIOps without writeback is dashboards.
- **Not an APM** — no Datadog-depth trace ingestion or runtime auto-discovery. Observability is your problem to bring. The "fresh graph" remains your ingestion problem.
- **No pre-cooked algorithms** — the STL, the GNN, the RCA random walk: you implement or import them. Foundry is the contract (ontology + provenance + permissions + loop), not the models.
- **Cost/fit** — overkill unless the use case is real industrial operations (plant, grid, supply chain), not monitoring a 20-service SaaS.

## 08 · Books

## Reading list, layer by layer

### Graphs & GNNs

- **Graph Machine Learning** — Sartori, Ferraro et al. (Packt, 2nd ed. 2025). Best on-ramp; PyTorch Geometric.
- **Machine Learning on Graphs** — Palowitch, Tsitsulin, Perozzi (O'Reilly 2024). Better theory/practice balance; great "when NOT to use GNNs" chapter.
- **Graph Representation Learning** — Hamilton. Free at graphtutorials.com. The academic standard, denser.
- **Mining of Massive Datasets** — Leskovec, Rajaraman, Ullman. Free at mmds.org. Best-written link analysis chapter (PageRank).

### Knowledge graphs & ontologies

- **Knowledge Graphs: Fundamentals, Techniques, and Applications** — Hogan et al. (MIT Press 2021, free at kgbook). KG completion, TransE/RotatE, entity linking.
- **Semantic Web for the Working Ontologist** — Allemang & Hendler. If touching OWL/RDFS seriously.

### Entity resolution (the 80% of the real effort)

- **Entity Resolution and Information Quality** — Talburt. Old but unmatched on matching/dedupe/merge at scale.
- Paper: *An Introduction to Entity Resolution* (Papadakis et al.); libraries: **splink**, **recordlinkage**.

### KG × LLMs

- **Knowledge Graphs and LLMs in Action** — Negro, Futia, Kůs, Montagna (Manning). The glue layer: KG construction from structured/unstructured data, LLM-assisted extraction, GraphRAG, text-to-Cypher, agentic retrieval with guardrails. Authors from GraphAware (production, not tutorials); forewords by Maxime Labonne and Khalifeh AlJadda.

### Intelligence analysis (the "why")

- **Structured Analytic Techniques for Intelligence Analysis** — Heuer & Pherson. ACH, link analysis as discipline, biases. What Palantir FDEs know that ML engineers don't.
- **Psychology of Intelligence Analysis** — Heuer. Free from the CIA. Short and brutal on why human-in-the-loop isn't decoration.
- **OSINT Techniques** — Bazzell (10th ed.). If OSINT ingestion is the draw.

### SRE foundations

- **Designing Data-Intensive Applications** — Kleppmann. Provenance, lineage, immutability — half of what Foundry does.
- **Streaming Systems** — Akidau et al. The real-time ingestion layer.

>  **If you only read three:** DDIA → Palowitch (ML on Graphs) → Heuer & Pherson. Pipeline, graph, human analysis — the Palantir sandwich: data → graph → analyst.     Compiled from a working session · October 2026 · Diagrams: inline SVG.
