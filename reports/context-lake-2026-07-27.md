---
title: "Context Lakes: What Multi-Agent Systems Need to Share"
date: 2026-07-27
type: special
url: https://luisgonzalezbernal.com/reports/reports/context-lake-2026-07-27.html
summary: "The definition · Why vectors and per-agent memory don't add up · What exists and what it measures · The failures shared context prevents · What is still open"
tags: [agents, research, memory]
reading_time_minutes: 12
---
Memory & Knowledge · Special Report

# *Context Lakes*: What Multi-Agent Systems Need to Share

27 Jul 2026 · Updated 4 Oct 2026

The definition · Why vectors and per-agent memory don't add up · What exists and what it measures · The failures shared context prevents · What is still open

## Key findings

1. **"Context Lake" is a theoretical system class, not yet a product category.** The term comes from a January 2026 position paper that defines it by three requirements — native semantic operations, transactional consistency over all decision-relevant state, and bounds on staleness under load — and proves no existing system class meets them.[8]
2. **Fragmented context breaks policy, measurably.** Across eight frontier models in multi-agent workflows, violation rates ranged from 14% to 98% when the facts needed to respect a policy sat in different agents' private contexts.[17]
3. **Managing context is itself a failure surface.** Over 1,323 episodes, policy violations rose from 0% with the rule in context to 30% after compaction, and up to 59% for some models; pinning the constraint outside compaction brought it back to 0%.[20]
4. **Sharing is harder than remembering.** A memory engine that scores 97.4% on a single-user benchmark fell to 18% top-1 on provenance conflicts when every agent shared one store.[4] A multi-user framework classified what to share 96.0% of the time but got only 58.8% of memory operations strictly right.[22]
5. **The headline benchmarks measure the wrong thing for this problem.** Memory systems report 0.9169 on LoCoMo and 93.0% on LongMemEval-S,[12] but those are single-user conversational recall tests, and multi-hop association is largely unmeasured.[24]
6. **Better models do not fix it.** In a coordination benchmark with partial information, stronger reasoning did not reliably improve coordination and smaller open-weight models often matched frontier ones.[29]

## Part I

## What a context lake is — and is not yet

The term is precise and recent. Xiaowei Jiang's position paper argues that AI agents are becoming the primary consumers of data, making concurrent, irreversible decisions, and that data systems built for human analysis cycles become correctness bottlenecks in that regime.[8] When several agents act on shared resources, their actions interact before anything can reconcile them, so guarantees that apply after the decision come too late.[8]

From that the paper derives the Context Lake as a *necessary* system class with three requirements: semantic operations as native capabilities, transactional consistency over all decision-relevant state, and operational envelopes that bound staleness and degradation under load. Its Composition Impossibility Theorem claims that independently evolving systems — a vector store here, a database there — cannot be composed to provide that coherence while staying what they are.[8]

It is worth being exact about the status: the paper describes itself as a position paper that sets out the theoretical foundation and the invariants a system must guarantee, not as an implementation or a benchmark.[8] Neighbouring terms are converging on the same idea from the enterprise side — "Governed Enterprise Memory", designed so knowledge can be reused across tasks and agents under organizational policy[1] — and from practice, where one analytics company describes a useful context store as a map of business definitions, terminology, entity relationships, event taxonomies, runbooks and known failure modes.[32]

## Part II

## Why vectors and per-agent memory don't add up

The case against "just use a vector database" is consistent across sources. Relational systems answer which records match a predicate and vector systems which items are nearest a query; neither was built for recall weighted by cue and provenance over long sessions.[4] Vector databases keep metadata as flat attributes, which cannot express the hierarchies used to organise code, documents and agent memories.[13] And for questions that cross systems — joining users to organisations, requests to traces, behaviour across millions of events — a vector store is a weak foundation.[32]

Gluing stores together has its own cost: memory systems that combine separate vector and graph databases fragment the information and pay cross-database I/O latency.[6] Vector and graph memories also flatten what happens in a multi-agent run — agents, tools, documents, errors, evidence — into embeddings or pairwise traces, which limits sharing, tracing and revision.[9] Connecting more tools does not solve it either: two MCP servers expose two sets of capabilities, but they do not create a shared identity model or reconcile timestamps, permissions and conflicting definitions.[32]

Per-agent memory frameworks have the mirror problem. Most assume a single user and a single context and overlook knowledge transfer under changing, asymmetric permissions,[11] and existing memory layers treat memory as passive storage that each agent queries on its own.[15]

| Approach | What it is good at | What it misses for shared agent state |
| --- | --- | --- |
| Vector database | Nearest-neighbour retrieval of documents | Joins across systems, hierarchy, provenance and time[32,13,4] |
| Vector + graph stores side by side | Semantic and relational recall | Fragmented memory and cross-database latency[6] |
| Per-agent memory frameworks | Personal, long-term conversational recall | Sharing under changing permissions; memory is passive[11,15] |
| Context Lake (as defined) | Semantic operations, transactional consistency, bounded staleness | A theoretical target, not yet an implementation[8] |

## Part III

## What exists today, and what it measures

Most of what implements shared or temporal context is research code from the last nine months, and the numbers it reports are mostly about recall, speed and cost.

- **97.7%** less KV-cache memory for 15 agents sharing one compressed pool

PolyKV, Llama-3-8B, +0.57% perplexity[3]

- **5.4×** faster retrieval from one memory-native store

Mandol, under 10 QPS concurrent load[6]

- **80%** fewer input tokens than Mem0

MemMachine, matched conditions[12]

| System | Idea | What it reports |
| --- | --- | --- |
| AkasicMEM | Governed enterprise memory on a unified vector–graph–relational database; policies re-evaluated at retrieval[1] | Authorization continuity across derived memories[1] |
| Mandol | One store fusing key-value, vector and graph structures, no LLM in retrieval[6] | Best overall accuracy on LoCoMo and LongMemEval among compared systems; 5.4× retrieval, 4.8× insertion speedups[6] |
| MemMachine | Stores whole episodes to reduce lossy extraction[12] | 0.9169 on LoCoMo; 93.0% on LongMemEval-S[12] |
| MAGE | A temporal hypergraph of agents, messages, tools, errors, decisions and evidence[9] | Outperforms memory baselines (no figure in the abstract)[9] |
| Collaborative Memory / AIM | Private and shared memory tiers with access control and provenance[11,22] | 96.0% visibility classification, 58.8% strict operation accuracy[22] |
| Graphiti-based projects | Bi-temporal facts: valid-from and valid-until on every fact[2,10] | Small open-source repositories; interest, not adoption[2] |

The temporal point is the easiest to see in practice. Asked for a company's current CTO, a plain vector search returns both the 2018 and the 2022 chunk and leaves the model to guess; a bi-temporal graph filters by validity and returns only the current fact.[5] One local memory layer for coding agents makes the sharing point concrete: every integration writes to the same vault, so a decision captured in a Claude Code session is visible when another agent picks up the project.[33]

Industry is arriving from the data side. Altertable reports that its lakehouse — Postgres, logs, traces, product events and company knowledge — became the shared context layer behind its agents, which start from "a shared, queryable picture of the business" rather than a set of disconnected tools.[32]

## Part IV

## The failures shared context is meant to prevent

The strongest evidence for a shared, governed context layer is not a benchmark win but a catalogue of failures. **Context-fragmented violations** are policy breaches where each agent's action looks safe locally but the set breaks a rule, because the facts needed to see it are in different departments' contexts; eight frontier models showed violation rates of 14% to 98%, worse on cross-domain flows.[17] The same study concludes that self-avoidance is unreliable and that enforcement belongs in a layer above individual agents.[17]

**Governance decay** is the time dimension of the same problem: rules an agent obeys while they are visible can be silently removed by summarisation, and violations rose from 0% to 30% after compaction across 1,323 episodes. An adversarial variant that nudges the summariser to drop a policy defeated every model evaluated; pinning constraints outside compaction restored 0%.[20]

Sharing without isolation fails too. A provenance-conflict suite scored 18% top-1 when all cases shared one store versus 100% with per-case isolation, which its authors call a ceiling rather than deployment evidence.[4] And knowledge that persists in memory can leak when it is derived and reused under changing users and policies, which is why one enterprise design requires source restrictions to survive every derivation.[1]

Coordination failures persist even when communication works: agents fail because they do not track their peers' roles, knowledge or intentions,[28] and errors propagate across agents and rounds in ways that are hard to diagnose.[18] Earlier transactional work named the same gaps — context loss and missing transactional safeguards — and showed standalone models frequently violate interdependent constraints.[21]

Finally, the memory layer is a production system with production failures. One open-source memory layer's consolidation step silently destroyed its entity graph and all fact history, with no error, warning or test.[14] Another found that switching storage backends gave operators a green health check over an empty namespace.[10]

## Part V

## What is still open

- **Evidence for the full thesis.** The defining paper is a position paper; the systems that exist each cover part of it — governance, temporal facts, unified storage — and none is evaluated against all three requirements.[8,1]
- **Benchmarks.** Memory benchmarks mostly test single-hop recall,[24] and the first public dataset for multi-user memory operations shows strict accuracy at 58.8%.[22]
- **Compression that keeps what matters.** Truncation and summarisation are irreversible,[23] and implicit compression into embeddings that works on single-shot tasks fails on multi-step coding agents.[31]
- **Coordination itself.** One benchmark's authors conclude multi-agent coordination remains a fundamentally unsolved challenge for current models.[29]
- **Adoption.** Outside research, the signals are early: a vendor's own write-up and small open-source projects with no stars yet.[32,2]

## What I would do

1. **Don't buy a "context lake"; build the three properties on what you run.** Postgres with pgvector already hosts several of the reference implementations. Add the properties one at a time and measure each.
2. **Make facts bi-temporal first.** Valid-from and valid-until on every fact is the cheapest change with the clearest payoff: agents stop arguing with stale truths.
3. **Pin policies outside the context window.** Treat constraints as state the summariser cannot touch, and test that they survive compaction.
4. **Enforce above the agents, not in their prompts.** A central check on cross-agent actions catches what no single agent can see.
5. **Evaluate on the problem you have.** If several agents or users share memory, test sharing, conflicts and permissions — not only LoCoMo-style recall.
6. **Test the memory layer like a database.** Data-loss tests on consolidation, health checks that know whether the data is there, migrations that cannot silently point at an empty store.

*— Luis González*

## Method and limits

This report replaces a July 2026 version that cited no sources. It was rebuilt on 4 October 2026 with the reports research pipeline: 174 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar; 40 sources read in full; 33 with usable evidence. Each source was read on its own by an open model (NaN: deepseek-v4-flash), which extracted 231 claims, each with a verbatim quote; 2 claims whose quote did not appear in the source were discarded. The synthesis was written by Claude from that evidence, every cited figure was checked against its source, and the conclusions in "What I would do" are mine.

- **No general web search.** The run had no web-search key, so vendor documentation and product pages (Zep, Letta, Mem0, Tacnode and others) are under-represented; 27 of the 33 sources are research papers.
- **Preprints.** Most papers are recent arXiv preprints, not peer-reviewed; their figures are as reported by their authors and were not reproduced.
- **Different benchmarks.** Figures from different papers use different benchmarks and setups and are not directly comparable.

## Sources

1. AkasicMEM: Governed Enterprise Memory for Agents — Bae et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.25563](https://arxiv.org/abs/2609.25563)
2. claw-zep: self-hosted temporal knowledge platform on Graphiti — GitHub, Jun 2026 — [github.com/guoliangdi/claw-zep](https://github.com/guoliangdi/claw-zep)
3. PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference — Patel, Joshi, arXiv, Apr 2026 — [arxiv.org/abs/2604.24971](https://arxiv.org/abs/2604.24971)
4. FluctlightDB: A Memory Model of Data for AI Agents — Ganesh S, arXiv, Jul 2026 — [arxiv.org/abs/2608.12365](https://arxiv.org/abs/2608.12365)
5. graphiti-zep-agent: temporal knowledge graph agent — GitHub, Sep 2026 — [github.com/shivanshinigam/graphiti-zep-agent](https://github.com/shivanshinigam/graphiti-zep-agent)
6. Mandol: An Agglomerative Agent Memory System for Long-Term Conversations — Zhang et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.29778](https://arxiv.org/abs/2606.29778)
7. Context Lake: A System Class Defined by Decision Coherence — Xiaowei Jiang, arXiv, Jan 2026 — [arxiv.org/abs/2601.17019](https://arxiv.org/abs/2601.17019)
8. Diachronic Hypergraphs for Orchestrated Multi-Agent Multimodal Memory Curation (MAGE) — Feng et al., arXiv, Aug 2026 — [arxiv.org/abs/2608.29678](https://arxiv.org/abs/2608.29678)
9. L9 Graphiti Memory — GitHub, Oct 2026 — [github.com/Quantum-L9/l9-graphiti-memory](https://github.com/Quantum-L9/l9-graphiti-memory)
10. Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control — Rezazadeh et al., arXiv, May 2025 — [arxiv.org/abs/2505.18279](https://arxiv.org/abs/2505.18279)
11. MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents — Wang et al., arXiv, Apr 2026 — [arxiv.org/abs/2604.04853](https://arxiv.org/abs/2604.04853)
12. Directory-Aware Query and Maintenance in Vector Databases — Wang et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.16903](https://arxiv.org/abs/2606.16903)
13. GENOME: auditable memory layer for AI agents — GitHub, Sep 2026 — [github.com/NORTHTEKDevs/genome](https://github.com/NORTHTEKDevs/genome)
14. HyphaeDB: A Living Knowledge Topology for Agent-First Memory — Halaharvi, arXiv, Jun 2026 — [arxiv.org/abs/2606.28781](https://arxiv.org/abs/2606.28781)
15. Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems — Wu, Gong, arXiv, Apr 2026 — [arxiv.org/abs/2604.22879](https://arxiv.org/abs/2604.22879)
16. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems — Qi et al., arXiv, May 2026 — [arxiv.org/abs/2605.14892](https://arxiv.org/abs/2605.14892)
17. Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents — Chen, arXiv, Jun 2026 — [arxiv.org/abs/2606.22528](https://arxiv.org/abs/2606.22528)
18. SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning — Chang, Geng, arXiv, Mar 2025 — [arxiv.org/abs/2503.11951](https://arxiv.org/abs/2503.11951)
19. AIM: A Privacy-Aware Interoperable Memory Framework for Multi-Agent Multi-User LLM Systems — Johnson et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.12320](https://arxiv.org/abs/2609.12320)
20. ACE: Pluggable Adaptive Context Elasticizer across Agents — Liao et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.31564](https://arxiv.org/abs/2606.31564)
21. Profile-Graph Memory for LLM Agents (MemHop) — Zhu, arXiv, Jun 2026 — [arxiv.org/abs/2607.19359](https://arxiv.org/abs/2607.19359)
22. ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures — Ishfaq, Melo, arXiv, Sep 2026 — [arxiv.org/abs/2609.16986](https://arxiv.org/abs/2609.16986)
23. CRAFT: Grounded Multi-Agent Coordination Under Partial Information — Nath et al., arXiv, Mar 2026 — [arxiv.org/abs/2603.25268](https://arxiv.org/abs/2603.25268)
24. On Problems of Implicit Context Compression for Software Engineering Agents — Gelvan et al., arXiv, May 2026 — [arxiv.org/abs/2605.11051](https://arxiv.org/abs/2605.11051)
25. Lakehouse as Context Store — Sylvain Utard, Altertable, Jul 2026 — [altertable.ai/blog/2026-07-15-lakehouse-as-context-store](https://altertable.ai/blog/2026-07-15-lakehouse-as-context-store)
26. ClawMem: on-device memory for coding agents — GitHub, Mar 2026 — [github.com/yoloshii/ClawMem](https://github.com/yoloshii/ClawMem)
