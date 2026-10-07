---
title: "Agent Memory: What Works, What It Costs, What Breaks"
date: 2026-06-28
type: special
url: https://luisgonzalezbernal.com/reports/reports/ai-agent-memory-2026-06-28.html
summary: "Types of memory · Frameworks and their numbers · How memory is measured · Cost against long context · Poisoning and other failures"
tags: [memory, research]
reading_time_minutes: 12
---
Memory & Knowledge · Special Report

# *Agent Memory*: What Works, What It Costs, What Breaks

28 Jun 2026 · Updated 7 Oct 2026

Types of memory · Frameworks and their numbers · How memory is measured · Cost against long context · Poisoning and other failures

## Key findings

1. **In an independent test, plain RAG did as well as the memory frameworks.** Mem0, RAG and full context reached 77% to 81% on LoCoMo; Graphiti and cognee reached 55% to 56%.[8] RAG matched the top group at 8.4 times lower total cost than mem0.[8]
2. **The standard benchmark has a scoring bug.** The LoCoMo reference implementation leaves 23% of its corpus unscorable by construction.[29] Most published evaluations come from the framework providers themselves.[8]
3. **No architecture wins everywhere.** A test of 12 memory systems across 11 datasets found that the best structure depends on the bottleneck of the workload.[2]
4. **Precision beats volume.** Sending the whole conversation did worse than mem0's compressed memory.[8] Mem0 reports 91% lower p95 latency and over 90% lower token cost than full context.[4]
5. **Long-range recall separates the strategies.** On LoCoMo, windows, summaries and entity graphs scored at most 0.005 Recall@5 on distant turns.[11] A key-value store reached 0.573.[11]
6. **Memory is an attack surface that persists.** One attack poisoned Claude Code's memory and succeeded across sessions 81.7% of the time.[28] A prompt-level defense gave limited protection once the memory was poisoned.[28]

## Part I

## What agent memory is

Agent memory started as simple retrieval. It is now a data management system: it stores, retrieves, updates, consolidates and governs information while the agent runs.[2] One analysis splits it into four modules: representation and storage, extraction, retrieval and routing, and maintenance.[2] Another treats it as a lifecycle, not a store. The lifecycle runs from deciding what to remember to compacting context to a budget.[21]

The research uses a few distinctions. Memory can be short-term or long-term, knowledge or experience, structured or unstructured.[30] Many systems borrow the cognitive split into semantic, episodic and procedural memory.[19,27] The simple approaches all lose something. Sliding windows, summaries, embedding RAG and flat fact extraction cut token cost but cause information loss, drift or hallucination about the user.[18]

| Design | How it works | Example |
| --- | --- | --- |
| Extracted facts | An LLM extracts salient facts, then decides to add, update, delete or ignore each one[4,34] | Mem0 |
| Temporal knowledge graph | Entities and relations per user, with validity ranges on facts[23,37] | Zep / Graphiti |
| Tiered memory | Core memory in context and archival memory in a database; the agent edits its own memory with tools[36] | MemGPT / Letta |
| Experience memory | Complete procedural traces, including failures, retrieved for reuse[3] | APEX-EM |

*[The memory lifecycle: write, store, retrieve, act, and maintain; poisoning enters at write and security must be anchored at store]*

*The memory lifecycle. Poisoning attacks write through untrusted inputs; the security survey argues defenses must start at storage time, not at retrieval. Sources 2, 9 and 33.*

## Part II

## The frameworks and their numbers

Each framework reports strong results on its own evaluation. Most of these papers come from the companies that sell the systems.

| System | Self-reported result |
| --- | --- |
| Mem0 | 26% relative gain over OpenAI's memory on an LLM-judge metric; the graph variant adds about 2%[4] |
| Zep | 94.8% against 93.4% for MemGPT on Deep Memory Retrieval; up to 18.5% higher accuracy on LongMemEval[23] |
| Synthius-Mem | 94.37% on LoCoMo[18] |
| Maximem Synap | 92% on LongMemEval and 93.2% on LoCoMo[21] |

An independent testbed gives a different picture. It compared mem0, Graphiti and cognee with RAG and full-context baselines.[8] Mem0, RAG and full context reached 77% to 81%. Graphiti and cognee reached only 55% to 56%.[8] The gap came from incomplete retrieval, not from failed reasoning.[8]

Small differences need large tests. One reimplementation of Mem0 used 100 questions, which gives a confidence interval of about ±8 points.[34] Its author notes that checking the paper's 2-point gap between Mem0 and its graph variant needs about 2,000 questions.[34]

## Part III

## How memory is measured, and how well

LongMemEval tests five abilities: extraction, multi-session reasoning, temporal reasoning, knowledge updates and abstention.[1] On its 500 questions, commercial assistants and long-context LLMs lost 30% accuracy over sustained interactions.[1]

The benchmarks have known defects. A structural review of LoCoMo, LongMemEval and five other evaluations found that none measures continuity.[29] The median evaluation covers 1 of 7 required properties.[29] The authors' own system scored 8.8% on LoCoMo and 96% on their benchmark. They read the 87-point divergence as proof that the two tests measure different things.[29]

Other critiques point the same way. Evaluations mostly use end-to-end metrics and treat the system as a black box.[2] Memory benchmarks are limited to short synthetic dialogues, even as context windows reach millions of tokens.[25] One study shows that a common setup measures retrieval, not forgetting: it saturates at about 0.98.[16]

Newer benchmarks test agents in real environments. LongMemEval-V2 has 451 questions over histories of up to 115M tokens.[6] There, a coding-agent memory scored 72.5%, against 48.5% for the strongest RAG baseline.[6] In building information models, general-purpose memory retrieved relevant context but stored project knowledge as fragments.[31]

## Part IV

## What memory costs against long context

- **8.4×** lower total cost of ownership for RAG than for mem0, at the same accuracy

Independent cloud-edge testbed[8]

- **91%** lower p95 latency for Mem0 than for full context

Mem0 paper[4]

- **5,100** tokens of memory for a key-value store, against about 300 for windowing

AgentMemBench[11]

Keeping everything in context gets expensive fast. Naive accumulation grows token cost quadratically with conversation length.[21] Crude summaries make cost linear but cause an accuracy cliff.[21] Long-term memory lets an agent recall only the details a task needs.[10]

Memory also has a serving cost. Production systems inject retrieved memory into the prompt, so the engine prefills the same content again and again.[14] Precomputing each fact's KV state cut time-to-first-token by 72-79% on LoCoMo.[14] Accuracy was 60.3%, against 63.3% for Mem0.[14] Another method refreshes only 10-30% of the cache and still matches full recompute.[7]

Two cautions apply. Network constraints between edge and cloud did not change retrieval quality and added only 4% to 5% latency.[8] And memory does not help every model: in one agent, its benefits depended on the backbone and the budget.[27]

## Part V

## What breaks in production

### Poisoning

Persistent memory turns one bad write into lasting influence over the agent.[9] Agents that write and retrieve memory more aggressively are more exploitable.[9] Existing prompt injection defenses do not cover these attacks.[9]

| Attack | Target | Reported success |
| --- | --- | --- |
| GhostWriter | Tool-using personal agents | About 98% injection, about 60% activation[10] |
| PMPA | Claude Code and OpenClaw | 81.7% cross-session success on Claude Code[28] |
| SHADOWMERGE | Graph memory (Mem0) | 93.8% average attack success[15] |
| eTAMP | Web agents, through a manipulated page | Up to 32.5% on GPT-5-mini[12] |

Stronger models are not safer. GPT-5.2 was substantially vulnerable despite better task performance.[12] Agents under stress, such as dropped clicks or garbled text, were up to 8 times more susceptible.[12] There is a counterpoint: in health-record agents, existing legitimate memories reduced attack effectiveness dramatically.[20]

The defenses that work bind origin at write time. Defenses based on content or lineage can be bypassed by laundering, with up to 68% attack success.[22] An origin-bound design reached 0% across eight frontier models.[22] A survey reaches the same conclusion: security must start at storage time, with provenance, versioning and retention policy.[33]

### Shared memory, staleness and forgetting

When several agents share memory, four failures appear: unauthorized leakage, stale propagation, contradiction persistence and provenance collapse.[13] A live production study found two real bugs. Sub-tenant scope was bypassed on direct reads by id.[13] A duplicate filter rejected contradictory writes before the contradiction detector could see them.[13]

Time is a common weak point. One reimplementation reports that OpenAI's memory fell below 15% on temporal questions because timestamps were missing.[34] Forgetting is hard too. Similarity and recency are the wrong signals, because the decision happens before the future question is known.[16] A learned value over seven factors kept 0.770 of gold evidence, against 0.368 for recency.[16]

## What I would do

1. **Start with plain RAG over extracted facts.** Add a graph or a framework only if it beats that baseline on your own data.
2. **Do not trust leaderboard numbers.** Build an evaluation from your own conversations, large enough to detect the differences you care about.
3. **Put a timestamp and a validity range on every fact.** Temporal questions fail first when time is missing.
4. **Treat every memory write as untrusted input.** Record its origin at write time, and do not let web pages or tool outputs write memory without a policy.
5. **Decide forgetting on purpose.** Use soft deletes with history, and score what to keep by more than recency.
6. **Measure cost per conversation.** Track tokens and p95 latency, and reuse KV state if you serve your own models.

*— Luis González*

## Method and limits

This report replaces a June 2026 version with 8 sources, whose benchmark figures came mostly from the vendors. It was rebuilt on 7 October 2026 with the reports research pipeline. The pipeline found 157 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar. It read 39 sources in full, and 38 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 275 claims, each with a verbatim quote. 3 claims whose quote did not appear in the source were discarded. Claude wrote the synthesis from that evidence and checked every cited figure against its source. The conclusions in "What I would do" are mine.

- **No general web search.** The run had no web-search key. Product documentation for Mem0, Zep, Letta, A-MEM and LangMem is under-represented; 33 of the 38 sources are research papers.
- **Vendor-authored papers.** The Mem0 and Zep papers come from the companies behind them. Only one source in the pack compares frameworks independently.
- **Preprints.** Most papers are arXiv preprints, not peer-reviewed. Their figures are as reported and were not reproduced.

## Sources

1. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory — Wu et al., arXiv, Oct 2024 — [arxiv.org/abs/2410.10813](https://arxiv.org/abs/2410.10813)
2. Are We Ready For An Agent-Native Memory System? — Zhou et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.24775](https://arxiv.org/abs/2606.24775)
3. APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay — Banerjee, Moshtaghi, Chadha, arXiv, Mar 2026 — [arxiv.org/abs/2603.29093](https://arxiv.org/abs/2603.29093)
4. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — Chhikara et al., arXiv, Apr 2025 — [arxiv.org/abs/2504.19413](https://arxiv.org/abs/2504.19413)
5. LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues — Wu et al., arXiv, 2026 — [arxiv.org/abs/2605.12493](https://arxiv.org/abs/2605.12493)
6. AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems — Pandey et al., arXiv, 2026 — [arxiv.org/abs/2607.21604](https://arxiv.org/abs/2607.21604)
7. Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models — Wolff, Bennati, arXiv, Jan 2026 — [arxiv.org/abs/2601.07978](https://arxiv.org/abs/2601.07978)
8. From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents — Dash et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.04329](https://arxiv.org/abs/2606.04329)
9. When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents — Torres, Shrestha, Misra, arXiv, Jul 2026 — [arxiv.org/abs/2607.06595](https://arxiv.org/abs/2607.06595)
10. AgentMemBench: A Systematic Benchmark for Evaluating Long-Term Memory Management Strategies in Conversational AI Agents — Cherif, arXiv, 2026 — [arxiv.org/abs/2608.00009](https://arxiv.org/abs/2608.00009)
11. Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents — Zou et al., arXiv, Apr 2026 — [arxiv.org/abs/2604.02623](https://arxiv.org/abs/2604.02623)
12. Governed Shared Memory for Multi-Agent LLM Systems — Margalit et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.24535](https://arxiv.org/abs/2606.24535)
13. InferScale: GPU-Native KV Injection for Personalized LLM Serving — Li, Pandey, arXiv, Jul 2026 — [arxiv.org/abs/2607.27090](https://arxiv.org/abs/2607.27090)
14. ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts — Luo et al., arXiv, May 2026 — [arxiv.org/abs/2605.09033](https://arxiv.org/abs/2605.09033)
15. Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory — Chen, Cheng, arXiv, Jun 2026 — [arxiv.org/abs/2606.12945](https://arxiv.org/abs/2606.12945)
16. Synthius-Mem: Brain-Inspired Hallucination-Resistant Persona Memory — Gadzhiev, Kislov, arXiv, Apr 2026 — [arxiv.org/abs/2604.11563](https://arxiv.org/abs/2604.11563)
17. AdMem: Advanced Memory for Task-solving Agents — Wang et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.06787](https://arxiv.org/abs/2606.06787)
18. Memory Poisoning Attack and Defense on Memory Based LLM-Agents — Devarangadi Sunil et al., arXiv, Jan 2026 — [arxiv.org/abs/2601.05504](https://arxiv.org/abs/2601.05504)
19. Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems — Dadhich, arXiv, Jul 2026 — [arxiv.org/abs/2607.21503](https://arxiv.org/abs/2607.21503)
20. Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority — Louck, arXiv, Jun 2026 — [arxiv.org/abs/2606.24322](https://arxiv.org/abs/2606.24322)
21. Zep: A Temporal Knowledge Graph Architecture for Agent Memory — Rasmussen et al., arXiv, Jan 2025 — [arxiv.org/abs/2501.13956](https://arxiv.org/abs/2501.13956)
22. MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization — Zhang et al., arXiv, Mar 2026 — [arxiv.org/abs/2603.25973](https://arxiv.org/abs/2603.25973)
23. SimSkill: A Self-Evolving LLM Agent for Skill and Knowledge Accumulation in Traffic Simulation — Liu et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.03753](https://arxiv.org/abs/2609.03753)
24. When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents — Huang, Zhang, Jia, arXiv, Sep 2026 — [arxiv.org/abs/2609.13889](https://arxiv.org/abs/2609.13889)
25. ATANT v1.1: Positioning Continuity Evaluation Against Memory, Long-Context, and Agentic-Memory Benchmarks — Tanguturi, arXiv, Apr 2026 — [arxiv.org/abs/2604.10981](https://arxiv.org/abs/2604.10981)
26. Graph-based Agent Memory: Taxonomy, Techniques, and Applications — Yang et al., arXiv, Feb 2026 — [arxiv.org/abs/2602.05665](https://arxiv.org/abs/2602.05665)
27. IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval — Du et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.26072](https://arxiv.org/abs/2607.26072)
28. A Survey on Long-Term Memory Security in LLM Agents — Lin et al., arXiv, 2026 — [arxiv.org/abs/2604.16548](https://arxiv.org/abs/2604.16548)
29. memoir: a reimplementation of Mem0's long-term memory — GitHub, Jul 2026 — [github.com/devchaen/memoir](https://github.com/devchaen/memoir)
30. LLMs as Operating Systems: Agent Memory (course notes, Letta) — GitHub, Jan 2025 — [github.com/ksm26/LLMs-as-Operating-Systems-Agent-Memory](https://github.com/ksm26/LLMs-as-Operating-Systems-Agent-Memory)
31. Zep memory provider for an agent harness — GitHub, Apr 2026 — [github.com/ruter/zep](https://github.com/ruter/zep)
