# Evidence — AI agent memory: architectures, frameworks and trade-offs

Generated 2026-10-05 · searched: 157 · candidates: 39 · web_search: False · read: 39 · sources_with_evidence: 38 · claims: 275 · quotes_dropped_as_unverified: 3

## q1. What types of memory do LLM agents use, and what taxonomies does the research propose?

- **[1] LLM-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses.**
  > Recent large language model (LLM)-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses.
- **[1] LongMemEval is designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention.**
  > We introduce LongMemEval, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention.
- **[1] The paper presents a unified framework that breaks long-term memory design into three stages: indexing, retrieval, and reading.**
  > We then present a unified framework that breaks down the long-term memory design into three stages: indexing, retrieval, and reading.
- **[1] The paper proposes memory design optimizations including session decomposition for value granularity, fact-augmented key expansion for indexing, and time-aware query expansion for refining the search scope.**
  > Built upon key experimental insights, we propose several memory design optimizations including session decomposition for value granularity, fact-augmented key expansion for indexing, and time-aware query expansion for refining the search scope.
- **[2] Agent memory has evolved from simple retrieval-augmented mechanisms into a data management system supporting persistent storage, retrieval, update, consolidation, and dynamic lifecycle governance during agent execution.**
  > Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution.
- **[2] The paper proposes an analytical framework decomposing agent memory into four core modules: memory representation and storage, extraction, retrieval and routing, and maintenance.**
  > We propose an analytical framework that decomposes agent memory into four core modules: memory representation and storage, extraction, retrieval and routing, and maintenance.
- **[3] APEX-EM is a non-parametric experience memory that stores complete procedural-episodic traces in a typed Procedural Knowledge Graph (PKG) and retrieves them through semantic search, structural-signature matching over abstract operation sequences, and graph traversal.**
  > We introduce \textbf{APEX-EM}, a non-parametric experience memory that stores complete procedural-episodic traces in a typed Procedural Knowledge Graph (PKG) and retrieves them through three channels: semantic search, structural-signature matching over abstract operation sequences, and graph traversal.
- **[3] APEX-EM uses a Plan-Retrieve-Generate-Iterate-Ingest (PRGII) workflow that quality-gates and commits experiences, indexes both successes and failures, and does not change model weights during deployment.**
  > A Plan-Retrieve-Generate-Iterate-Ingest (PRGII) workflow produces, quality-gates, and commits experiences, indexing both successes and failures so the agent learns what to reuse and what to avoid. No weights change during deployment.
- **[4] Mem0 is proposed as a scalable memory-centric architecture that dynamically extracts, consolidates, and retrieves salient information from ongoing conversations.**
  > We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations.
- **[4] An enhanced Mem0 variant uses graph-based memory representations to capture complex relational structures among conversational elements.**
  > Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements.
- **[5] Existing agent memory architectures such as Generative Agents, MemGPT, and A-MEM treat memory as text streams or knowledge graphs, while embodied agents require memory searchable simultaneously by meaning, space, and time.**
  > Current agent memory architectures, such as Generative Agents, MemGPT, and A-MEM, treat memory as text streams or knowledge graphs, but embodied agents require memory that is simultaneously searchable by meaning, space, and time.
- **[5] eMEM uses a multi-index architecture with SQLITE for structured storage, hnswlib for approximate nearest-neighbour semantic search, and an R-tree for spatial queries, unified behind a single graph model.**
  > eMEM fills this gap with a multi-index architecture (SQLITE for structured storage, hnswlib for approximate nearest neighbour semantic search, and an R-tree for spatial queries) unified behind a single graph model.
- **[5] eMEM uses a tiered consolidation pipeline that transforms raw perceptual observations into compressed summaries, mirroring hippocampal-neocortical consolidation in biological systems.**
  > A tiered consolidation pipeline transforms raw perceptual observations into compressed summaries, mirroring hippocampal-neocortical consolidation in biological systems.
- **[5] eMEM exposes ten agent-facing recall tools for LLM tool calling, including concept-to-location resolution and cross layer recall.**
  > Ten agent-facing recall tools expose memory retrieval primitives, including concept-to-location resolution and cross layer recall, as first-class operations for LLM tool calling.
- **[7] Memory-augmented LLM agents maintain context across hundreds of interactions using agentic memory systems that curate retrieved content with LLM-generated metadata such as summaries, keywords, and tags.**
  > Memory-augmented LLM agents maintain context across hundreds of interactions through agentic memory systems that actively curate retrieved content with LLM-generated metadata such as summaries, keywords, and tags.
- **[8] The paper treats long-term memory as fundamental to LLM-based agents in the Internet of Agents, where distributed multi-agent systems span cloud and edge networks.**
  > Long-term memory (LTM) is fundamental to large language model (LLM)-based agents in the emerging Internet of Agents (IoA), where distributed multi-agent systems (DMAS) span cloud and edge networks.
- **[8] The paper compares frameworks spanning vector, graph, and hybrid memory architectures, naming mem0, Graphiti, and cognee, alongside RAG and full-context baselines on LoCoMo.**
  > Three venture capital-funded frameworks spanning vector, graph, and hybrid architectures, namely mem0, Graphiti, and cognee, are compared alongside retrieval-augmented generation (RAG) and full-context baselines on the LoCoMo benchmark under unconstrained and constrained network scenarios.
- **[9] Memory is described as a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance.**
  > Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance.
- **[10] Long-term memory agents tend to fall into two distinct domains: conversational agents and action-planning agents.**
  > Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents.
- **[11] The paper proposes a taxonomy of five memory management strategies for conversational agents: in-context windowing (ICW), external key-value store (EKV), graph-based episodic memory (GEM), compression-based summarisation (CBS), and web-augmented memory (WAM).**
  > We present AgentMemBench, a unified, reproducible benchmark evaluating five memory management strategies under identical conditions: in-context windowing (ICW), external key-value store (EKV), graph-based episodic memory (GEM), compression-based summarisation (CBS), and web-augmented memory (WAM).
- **[12] Agent memory stores past interactions to personalize future tasks, creating a persistent attack surface spanning websites and sessions.**
  > Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions.
- **[13] The paper proposes systems-level memory primitives: scoped retrieval, temporal supersession, provenance tracking, and policy-governed memory propagation.**
  > To address these, we define explicit systems-level primitives: scoped retrieval, temporal supersession, provenance tracking, and policy-governed memory propagation.
- **[14] LLMs are deployed with persistent personalized context such as accumulated memory profiles or long conversation histories that are shared across a user's requests.**
  > Large language models are increasingly deployed with persistent personalized context, such as accumulated memory profiles or long conversation histories, that is shared across a user's many requests.
- **[15] Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a poisoning surface where injected relations can later be retrieved and influence behavior.**
  > Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an attacker can inject a crafted relation into graph memory so that it is later retrieved and influences agent behavior.
- **[15] Existing agent-memory poisoning attacks mainly target flat textual records and are ineffective in graph-based memory because malicious relations often fail to be extracted, merged into the target anchor neighborhood, or retrieved for the victim query.**
  > Existing agent-memory poisoning attacks mainly target flat textual records and are ineffective in graph-based memory because malicious relations often fail to be extracted, merged into the target anchor neighborhood, or retrieved for the victim query.
- **[16] The paper proposes a multi-factor memory value function over seven interpretable factors drawn from cognitive psychology: emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history; a single scalar controls encoding depth, forget risk, and retrieval rank.**
  > We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank.
- **[17] HORMA organizes experience into a file-system-like hierarchical structure in which summarized entities are linked to raw trajectories, enabling efficient access without losing detailed information.**
  > In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information.
- **[17] HORMA decomposes working memory into two stages: structured memory construction and navigation-based retrieval.**
  > HORMA decomposes working memory into two stages: structured memory construction and navigation-based retrieval.
- **[18] The paper identifies current LLM agent memory approaches as sliding windows, summarization, embedding-based RAG, and flat fact extraction, and says each reduces token cost but introduces catastrophic information loss, semantic drift, or uncontrolled hallucination about the user.**
  > Current approaches to memory for LLM agents -- sliding windows, summarization, embedding-based RAG, and flat fact extraction -- each reduce token cost but introduce catastrophic information loss, semantic drift, or uncontrolled hallucination about the user.
- **[18] Synthius-Mem uses a persona extraction pipeline that decomposes conversations into six cognitive domains: biography, experiences, preferences, social circle, work, and psychometrics; it consolidates and deduplicates per domain and retrieves structured facts via CategoryRAG at 21.79 ms latency.**
  > Instead of retrieving what was said, Synthius-Mem extracts what is known about the person: a full persona extraction pipeline decomposes conversations into six cognitive domains (biography, experiences, preferences, social circle, work, psychometrics), consolidates and deduplicates per domain, and retrieves structured facts via CategoryRAG at 21.79 ms latency.
- **[19] AdMem proposes a unified automatic memory framework combining semantic, episodic, and procedural memory, with bi-level short-term and long-term stores.**
  > We introduce a unified and automatic memory framework that integrates semantic, episodic, and procedural memory in a bi-level design combining short-term and long-term stores.
- **[19] Prior memory approaches mainly focus on storing factual information.**
  > Prior memory approaches aim to resolve the situation, but mainly focus on storing factual information.
- **[19] Recent procedural memory work improves task reuse but often reduces to replaying past successes without addressing failure cases or online scalability.**
  > Recent work on procedural memory improves task reuse, yet often reduces to replaying past successes without addressing failure cases or online scalability.
- **[21] The paper argues agent memory should be treated as a lifecycle rather than merely a store, spanning remembering, extraction and structuring, choosing per-data-type stores, consolidation and forgetting with provenance, relevance, anticipation, and budgeted compaction.**
  > Actively managing what an agent holds in mind is a lifecycle, not merely a store: it spans deciding what to remember, extracting and structuring it, choosing the right store per data type, consolidating and forgetting while preserving provenance, deciding what is relevant now, anticipating what is needed next, and compacting context to a budget without losing what matters.
- **[21] In production, agent context management must operate across an organizational scope hierarchy rather than for only a single user.**
  > In serious production this operates not over a single user but across an organizational scope hierarchy.
- **[21] The paper names the discipline Agentic Context Management (ACM) and decomposes it into five primitives: architecting, ingesting, scoping, anticipating, and compacting and consolidation.**
  > We name this discipline Agentic Context Management (ACM) and decompose it into five primitives: architecting, ingesting, scoping, anticipating, and compacting &consolidation.
- **[23] The paper contrasts existing RAG frameworks for LLM agents, limited to static document retrieval, with enterprise needs for dynamic knowledge integration from ongoing conversations and business data.**
  > While existing retrieval-augmented generation (RAG) frameworks for large language model (LLM)-based agents are limited to static document retrieval, enterprise applications demand dynamic knowledge integration from diverse sources including ongoing conversations and business data.
- **[24] The survey proposes modeling an LLM agent's state as a dynamic graph, with memories among other components represented as typed nodes, edges, and subgraphs updated via schema-constrained rewrites.**
  > We model agent state as a dynamic graph, where memories, tools, skills, workflows, and inter-agent relations are represented as typed nodes, edges, and subgraphs updated through schema-constrained rewrites.
- **[24] The survey organizes dynamic-graph-based methods for self-evolving agents into four taxonomies: node/feature evolution, edge/topology evolution, subgraph activation, and cross-component co-evolution.**
  > Based on this formulation, we organize existing dynamic-graph-based methods for self-evolving agents into four taxonomies: node/feature evolution, edge/topology evolution, subgraph activation, and cross-component co-evolution.
- **[24] The survey says it maps nine dynamic-graph-learning subfields to agent-evolution capabilities, including adaptations and possible failure modes.**
  > Building on this taxonomy, we propose dynamic graph learning as reusable infrastructure for self-evolving agents and map nine dynamic-graph-learning subfields to agent-evolution capabilities, discussing their adaptations and possible failure modes.
- **[24] The survey argues that existing graph-agent surveys treat graphs as support structures for agent functions rather than evolving substrates.**
  > Existing graph-agent surveys typically treat graphs as support structures for agent functions rather than as evolving substrates, while self-evolving-agent surveys focus on agent-level mechanisms and rarely discuss graph topology evolution.
- **[24] The survey states that the coupling between evolving agent state and dynamic graph topology remains underexplored.**
  > Thus, the coupling between evolving agent state and dynamic graph topology remains underexplored.
- **[24] The survey describes LLM-based agents as self-evolving systems that persist across interactions and maintain memories, tools, skills, workflows, and inter-agent coordination.**
  > Large language model (LLM)-based agents are increasingly becoming self-evolving systems that persist across interactions, maintain memories, use tools, acquire skills, refine workflows, and coordinate with other agents.
- **[27] SimSkill consolidates experience into episodic, procedural, and semantic memory.**
  > SimSkill continually identifies capability gaps, generates and solves environment-grounded tasks, verifies solutions through an action--critic loop, and consolidates experience into episodic, procedural, and semantic memory.
- **[27] Through autonomous exploration, SimSkill builds a library of reusable skills and knowledge spanning major stages of the traffic-simulation workflow.**
  > Through autonomous exploration, it builds a library of reusable skills and knowledge spanning major stages of the traffic-simulation workflow.
- **[27] SimSkill illustrates a natural-language-centered design paradigm for LLM-based agent systems, with control logic, operating principles, and accumulated knowledge expressed in natural language.**
  > More broadly, SimSkill illustrates a natural-language-centered design paradigm for LLM-based agent systems. Its high-level control logic, operating principles, and accumulated knowledge are expressed in natural language, while an LLM integrates them with executable tools and code to realize precise and reproducible execution.
- **[29] ATANT v1.0 defined continuity as a system property with 7 required properties and introduced a 10-checkpoint, LLM-free evaluation methodology validated on a 250-story corpus.**
  > ATANT v1.0 ([arXiv:2604.06710](https://arxiv.org/abs/2604.06710)) defined continuity as a system property with 7 required properties and introduced a 10-checkpoint, LLM-free evaluation methodology validated on a 250-story corpus.
- **[30] The survey proposes a taxonomy of agent memory across three dimensions: short-term versus long-term memory, knowledge versus experience memory, and non-structural versus structural memory, plus a graph-based implementation view.**
  > First, we introduce a taxonomy of agent memory, including short-term vs. long-term memory, knowledge vs. experience memory, non-structural vs. structural memory, with an implementation view of graph-based memory.
- **[30] The survey argues that graph structure is powerful for agent memory because it can model relational dependencies, organize hierarchical information, and support efficient retrieval.**
  > Among diverse paradigms, graph stands out as a powerful structure for agent memory due to the intrinsic capabilities to model relational dependencies, organize hierarchical information, and support efficient retrieval.
- **[30] The survey describes memory as a core module for LLM-based agents on long-horizon complex tasks such as multi-turn dialogue, game playing, and scientific discovery, enabling knowledge accumulation, iterative reasoning, and self-evolution.**
  > Memory emerges as the core module in the Large Language Model (LLM)-based agents for long-horizon complex tasks (e.g., multi-turn dialogue, game playing, scientific discovery), where memory can enable knowledge accumulation, iterative reasoning and self-evolution.
- **[31] The paper evaluates representative vector-, graph-, and file-based memory systems.**
  > We evaluate representative vector-, graph-, and file-based memory systems.
- **[33] The source proposes a Memory Lifecycle Framework as a taxonomy organizing attacks, defenses, and cross-phase dependencies along six lifecycle phases and four security objectives.**
  > To systematically characterize this landscape, we propose a Memory Lifecycle Framework that organizes attacks, defenses, and their cross-phase dependencies along two axes: six lifecycle phases (Write, Store, Retrieve, Execute, Share &Propagate, Forget &Rollback) and four security objectives (Integrity, Confidentiality, Availability, Governance).
- **[35] The project implements a global bi-temporal model with valid_from, valid_until, version and source fields supporting snapshots, backtracking and conflict resolution.**
  > 全局双时序模型（valid_from/valid_until/version/source）：快照/回溯/冲突消解
- **[35] The system includes an 'OpenHuman' three-layer memory tree architecture with online Markdown editing and Obsidian export.**
  > OpenHuman 记忆树三层架构 + Markdown 在线编辑 + Obsidian 导出
- **[36] MemGPT's key ideas include two-tier memory systems and converting agent states into prompts.**
  > 3.   🧩 **MemGPT Concepts**: Understand the key ideas behind MemGPT, including two-tier memory systems and how agent states are converted into prompts.
- **[36] Letta provides core and archival memory for LLM agents.**
  > 2.   🛠️ **Using Letta Framework**: Explore Letta’s features for adding memory capabilities to LLMs, including core and archival memory.
- **[36] Letta agents can have self-editing memory using tool-calling and multi-step reasoning.**
  > 1.   🔄 **Agent Memory Management**: Build agents with self-editing memory, utilizing tool-calling and multi-step reasoning.
- **[36] Multi-agent collaboration in Letta involves sharing memory blocks and exchanging messages.**
  > 4.   🤝 **Multi-Agent Collaboration**: Learn to implement collaborative agents by sharing memory blocks and exchanging messages.
- **[36] Conversation memory control manages expanding conversations by summarizing and moving less relevant information to a searchable database.**
  > *   🔍 **Conversation Memory Control**: Manage expanding conversations by summarizing and moving less relevant information to a searchable database, ensuring smooth context flow.
- **[36] Letta supports persistent fact storage for names, dates, and preferences, and task-specific memory that swaps context-relevant information from a database in real time.**
  > *   📂 **Persistent Fact Storage**: Save and edit details like names, dates, and preferences for future interactions.
*   📑 **Task-Specific Memory**: Develop agents capable of swapping context-relevant information in real-time from a database for tasks like research.
- **[37] Zep is described as a context engineering platform that builds temporal knowledge graphs from conversations and business data, providing persistent, cross-session memory.**
  > Persistent, cross-session memory powered by [Zep](https://www.getzep.com/) — a context engineering platform that builds temporal knowledge graphs from conversations and business data.
- **[38] The repository categorizes Zep under topics including ai-agents, apis-json, context-engineering, crewai, graph-rag, knowledge-graph, langchain, llamaindex, llms, memory, personalization, retrieval, and temporal-graph.**
  > [ai-agents](https://github.com/topics/ai-agents)[apis-json](https://github.com/topics/apis-json)[context-engineering](https://github.com/topics/context-engineering)[crewai](https://github.com/topics/crewai)[graph-rag](https://github.com/topics/graph-rag)[knowledge-graph](https://github.com/topics/knowledge-graph)[langchain](https://github.com/topics/langchain)[llamaindex](https://github.com/topics/llamaindex)[llms](https://github.com/topics/llms)[memory](https://github.com/topics/memory)[personalization](https://github.com/topics/personalization)[retrieval](https://github.com/topics/retrieval)[temporal-graph](https://github.com/topics/temporal-graph)

## q2. How do the main memory frameworks (Mem0, Zep/Graphiti, Letta/MemGPT, A-MEM, LangMem) work and what do they report?

- **[2] The study evaluates 12 representative memory systems and two reference baselines across five benchmark workloads spanning 11 datasets.**
  > Under this framework, we evaluate 12 representative memory systems and two reference baselines across five benchmark workloads spanning 11 datasets.
- **[3] On held-out BigCodeBench transfer with a shared GPT-4o backbone, APEX-EM gains +7.6 pp over the no-memory baseline, which is 3.3 times MemRL's +2.3 pp under the identical setup.**
  > On held-out BigCodeBench transfer with a shared GPT-4o backbone, APEX-EM gains +7.6\,pp over the no-memory baseline, 3.3×MemRL's +2.3\,pp under the identical setup.
- **[3] On Lifelong Agent Bench with a shared GPT-4o-mini backbone, APEX-EM gains +1.4 pp for OS and +1.0 pp for DB cumulative success.**
  > On Lifelong Agent Bench with a shared GPT-4o-mini backbone, it gains +1.4\,pp (OS) and +1.0\,pp (DB) cumulative success.
- **[3] On KGQAGen-10k, frozen memory transfers to a blind 1,079-question test split at 73.7% versus 42.0% with no memory, approaching an oracle given the ground-truth subgraph at 84.9%.**
  > On KGQAGen-10k, frozen memory transfers to a blind 1{,}079-question test split at 73.7\% versus 42.0\% with no memory, approaching an oracle handed the ground-truth subgraph (84.9\%).
- **[3] Component analysis shows no single mechanism dominates: teacher feedback is negligible for code but adds +10.3 pp on structured queries, structural signatures give 3.3 times the transfer of semantic-only retrieval, and within-epoch iteration recovers most of the gain when rich feedback is unavailable.**
  > Component analysis shows no single mechanism dominates: teacher feedback is negligible for code but adds +10.3\,pp on structured queries, structural signatures give 3.3×the transfer of semantic-only retrieval, and within-epoch iteration recovers most of the gain when rich feedback is unavailable.
- **[4] Mem0 reports 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory reports around 2% higher overall score than the base configuration.**
  > Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base configuration.
- **[5] The paper cites Generative Agents, MemGPT, and A-MEM as current agent memory architectures that treat memory as text streams or knowledge graphs.**
  > Current agent memory architectures, such as Generative Agents, MemGPT, and A-MEM, treat memory as text streams or knowledge graphs, but embodied agents require memory that is simultaneously searchable by meaning, space, and time.
- **[6] The paper proposes two memory methods: AgentRunbook-R, an efficient RAG-based memory with knowledge pools for raw state observations, events, and strategy notes, and AgentRunbook-C, which stores trajectories as files and invokes a coding agent to gather evidence in an augmented sandbox.**
  > We propose a suite of two memory methods: AgentRunbook-R, an efficient RAG-based memory with knowledge pools for raw state observations, events, and strategy notes, and AgentRunbook-C, which stores trajectories as files and invokes a coding agent to gather evidence in an augmented sandbox.
- **[8] Mem0, RAG, and full-context reach 77% to 81% accuracy, while Graphiti and cognee reach only 55% to 56%; the gap is driven by retrieval incompleteness rather than reasoning failure.**
  > Two clusters emerge: mem0, RAG, and full-context reach 77% to 81% accuracy, while Graphiti and cognee reach only 55% to 56%, a gap driven by retrieval incompleteness rather than reasoning failure.
- **[8] Compression precision rather than context volume determines LTM accuracy, and full-context forwarding underperforms mem0 despite supplying the entire conversation for each question.**
  > Compression precision rather than context volume determines LTM accuracy, as full-context forwarding underperforms mem0 despite supplying the entire conversation for each question.
- **[11] The study additionally evaluates two published memory systems, MemGPT/Letta and HippoRAG, against the same benchmark harness and releases code, environment, and result artefacts for reproducibility.**
  > We additionally evaluate two published memory systems (MemGPT/Letta, HippoRAG) against the same harness, and release all code, environment, and result artefacts for full reproducibility.
- **[13] The primitives are implemented in MemClaw, described as a production multi-tenant memory service, and evaluated via ArgusFleet, a reproducible harness testing four governance dimensions; the study measures a live production service rather than a baseline comparison.**
  > These primitives are implemented in MemClaw, a production multi-tenant memory service, and evaluated via ArgusFleet, a reproducible harness testing four governance dimensions. Rather than a baseline comparison, this study measures a live production service, emphasizing real-world architectural insights and negative results.
- **[14] Production memory systems including Mem0, MemGPT, and Zep retrieve a relevant subset of memory and inject it into the prompt, causing repeated prefilling of the same content.**
  > Production memory systems (e.g., Mem0, MemGPT, and Zep) retrieve a relevant subset of this memory and inject it into the prompt, forcing the serving engine to repeatedly prefill the same content.
- **[14] InferScale precomputes each memory fact's KV representation, stores it with a semantic embedding on the GPU, retrieves relevant facts at serving time, and injects their KV directly into vLLM's paged cache.**
  > InferScale precomputes each memory fact's KV representation, stores it alongside a semantic embedding on the GPU, retrieves relevant facts at serving time, and injects their KV directly into vLLM's paged cache.
- **[14] Chunked RoPE stores keys before rotation and applies their serving-time positions during injection to support dynamically assembled memories under rotary position embeddings.**
  > To support dynamically assembled memories under rotary position embeddings, we introduce Chunked RoPE, which stores keys before rotation and applies their serving-time positions during injection.
- **[14] Context-Window Encoding encodes each memory fact with a small window of preceding conversation context while caching only the target fact's KV.**
  > We mitigate this with Context-Window Encoding, which encodes each memory fact together with a small window of preceding conversation context while caching only the target fact's KV.
- **[15] SHADOWMERGE is evaluated on Mem0 and three public real-world datasets: PubMedQA, WebShop, and ToolEmu.**
  > We evaluate SHADOWMERGE on Mem0 and three public real-world datasets: PubMedQA, WebShop, and ToolEmu.
- **[17] The source compares HORMA only to existing methods in general and does not name or report results for Mem0, Zep/Graphiti, Letta/MemGPT, A-MEM, or LangMem.**
  > Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks.
- **[18] On LoCoMo, which the paper describes as ACL 2024 with 10 conversations and 1,813 questions, Synthius-Mem reports 94.37% accuracy, exceeding MemMachine at 91.69% and human performance at 87.9 F1.**
  > On the LoCoMo benchmark (ACL 2024, 10 conversations, 1,813 questions), Synthius-Mem achieves 94.37% accuracy, exceeding all published systems including MemMachine (91.69%, adversarial score is not reported) and human performance (87.9 F1).
- **[18] Synthius-Mem reports core memory fact accuracy of 98.64%.**
  > Core memory fact accuracy reaches 98.64%.
- **[19] AdMem uses a multi-agent architecture with actor, memory, and critic agents for automatic memory generation, reward annotation, and adaptive retrieval.**
  > A multi-agent architecture with actor, memory, and critic agents enables automatic memory generation, reward annotation, and adaptive retrieval.
- **[19] Long-term memory in AdMem is managed through reward-based evaluation, merging, and pruning to support scalability and continual improvement.**
  > Long-term memory is managed through reward-based evaluation, merging, and pruning, ensuring scalability and continual improvement.
- **[21] The paper describes a reference implementation, Maximem Synap, that realizes the five primitives as a multi-tenant service and reports 92% on LongMemEval and 93.2% on LoCoMo under the configuration detailed in Section 6.**
  > We describe a reference implementation, Maximem Synap, that realizes the five primitives as a multi-tenant service and reports 92% on LongMemEval and 93.2% on LoCoMo under the configuration detailed in Section 6.
- **[23] Zep is presented as a memory layer service for AI agents that outperforms MemGPT in the Deep Memory Retrieval (DMR) benchmark.**
  > We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark.
- **[23] Zep's core component Graphiti is a temporally aware knowledge graph engine that synthesizes unstructured conversational data and structured business data while maintaining historical relationships.**
  > Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships.
- **[23] The paper reports Zep's results are especially pronounced on enterprise-critical tasks such as cross-session information synthesis and long-term context maintenance.**
  > These results are particularly pronounced in enterprise-critical tasks such as cross-session information synthesis and long-term context maintenance, demonstrating Zep's effectiveness for deployment in real-world applications.
- **[27] SimSkill improved verified success by up to 25 percentage points, and ablations showed complementary contributions from procedural and semantic memory.**
  > It improves verified success by up to 25 percentage points, and ablations show complementary contributions from procedural and semantic memory.
- **[30] The survey analyzes graph-based agent memory techniques according to a life cycle comprising memory extraction, storage, retrieval, and evolution.**
  > Second, according to the life cycle of agent memory, we systematically analyze the key techniques in graph-based agent memory, covering memory extraction for transforming the data into the contents, storage for organizing the data efficiently, retrieval for retrieving the relevant contents from memory to support reasoning, and evolution for updating the contents in the memory.
- **[34] This project is a from-scratch learning reimplementation of the Mem0 paper's long-term memory architecture (arXiv:2504.19413).**
  > **나를 기억하는 회고 컴패니언** — Mem0 논문([arXiv:2504.19413](https://arxiv.org/abs/2504.19413))의 장기 기억 아키텍처를 학습 목적으로 재구현한 개인 프로젝트입니다.
- **[34] The implementation follows the paper's Algorithm 1: retrieve top-s similar memories and use an LLM tool call to select ADD/UPDATE/DELETE/NOOP, with s=10 and tool_choice="required".**
  > | Tool call 기반 4연산 (Algorithm 1) | `pipeline/update.py` | s=10, `tool_choice="required"` |
- **[34] Graph memory (Mem0g) uses two-stage extraction from entities to relations, resolves nodes with similarity ≥ t=0.85, and marks conflicts as invalid without physical deletion, preserving temporal data.**
  > | Mem0ᵍ 2단계 추출 (엔티티→관계) | `graph/pipeline.py` | 취향 그래프: (사용자)-[prefers]->(디카페인) |
| 노드 해소 (유사도 ≥ t) | `GraphMemory._resolve_node` | t=0.85 |
| 충돌 감지 → invalid 표시 | LLM update resolver | 물리 삭제 없음, temporal 보존 |
- **[35] claw-zep is described as a fully self-hosted temporal knowledge platform built on Graphiti, providing a time-series knowledge graph and time-aware long-term memory for AI agents, enterprise knowledge bases and risk deduction.**
  > claw-zep is a fully self-hosted temporal knowledge platform built on Graphiti. It provides Palantir-grade dynamic time-series knowledge graph and time-aware long-term memory for AI Agents, enterprise knowledge bases and risk deduction.
- **[35] It wraps Graphiti scheduling with LLM extraction plus an offline heuristic fallback, distributing output across three stores: Kuzu, Chroma and PG (PostgreSQL).**
  > Graphiti 调度封装（LLM 抽取 + 离线启发式降级）→ 三库分发（Kuzu/Chroma/PG）
- **[35] Retrieval is hybrid, chaining temporal search, vector search, graph-link traversal and memory-tree weighting, combined with causal reasoning described as Palantir-style.**
  > 混合检索（时序→向量→图谱链路→记忆树加权）+ Palantir 因果推演
- **[36] Letta is an open-source framework for memory-enhanced LLM agents, taught by Letta co-founders and based on MemGPT research.**
  > Welcome to the "LLMs as Operating Systems: Agent Memory" course! 🧠 Learn how to build agents with long-term, persistent memory using **Letta**, an open-source framework for memory-enhanced LLM agents. This course is taught by **Charles Packer** and **Sarah Wooders**, co-founders of Letta, and is based on the innovative ideas presented in the MemGPT research paper.
- **[37] The Zep provider persists every conversation turn to Zep's knowledge graph via sync_turn.**
  > Persists every conversation turn to Zep's knowledge graph via `sync_turn`
- **[37] The prefetch hook calls thread.get_user_context() each turn, returning a context block containing a user summary and the most relevant facts ready to inject into the system prompt.**
  > The `prefetch` hook calls `thread.get_user_context()` each turn, which returns a context block containing a user summary and the most relevant facts — ready to inject into the system prompt.
- **[37] The Zep provider exposes zep_search and zep_add tools so the agent can query and write to the graph.**
  > Exposes `zep_search` and `zep_add` tools so the agent can query and write to the graph
- **[37] The Zep provider mirrors built-in MEMORY.md writes to Zep for unified knowledge.**
  > Mirrors built-in `MEMORY.md` writes to Zep for unified knowledge
- **[37] Zep automatically extracts entities, relationships, and facts from conversations, building a temporal knowledge graph per user.**
  > Zep automatically extracts entities, relationships, and facts from conversations, building a temporal knowledge graph per user.
- **[38] Zep is a context engineering and agent memory platform that assembles relevant context from chat history, business data, and user interactions for AI agents.**
  > Zep is a context engineering and agent memory platform that assembles relevant context from chat history, business data, and user interactions for AI agents.
- **[38] Zep builds a temporal knowledge graph per user that evolves as new facts arrive, automatically extracting entities (text cut off at 'entitie').**
  > It builds a temporal knowledge graph per user that evolves as new facts arrive, automatically extracts entitie
- **[38] The profile is an independent, third-party profile of a company's publicly available API surface, maintained by API Evangelist, and is not the company's own API.**
  > This is not our API. This repository is an independent, third-party profile of a company's publicly available API surface, maintained by API Evangelist.

## q3. How is agent memory evaluated (LoCoMo, LongMemEval, others) and how reliable are those benchmarks?

- **[1] LongMemEval includes 500 curated questions embedded within freely scalable user-assistant chat histories, and commercial chat assistants and long-context LLMs show a 30% accuracy drop on memorizing information across sustained interactions.**
  > With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, LongMemEval presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions.
- **[1] The paper states that long-term memory capabilities in sustained interactions remain underexplored.**
  > However, their long-term memory capabilities in sustained interactions remain underexplored.
- **[1] Extensive experiments show the proposed optimizations greatly improve both memory recall and downstream question answering on LongMemEval.**
  > Extensive experiments show that these optimizations greatly improve both memory recall and downstream question answering on LongMemEval.
- **[1] The LongMemEval benchmark and code are publicly available.**
  > Our benchmark and code are publicly available at [this https URL].
- **[2] Existing evaluations still benchmark agent memory mainly through end-to-end task success metrics such as F1 and BLEU, while treating the underlying system as a monolithic black box.**
  > Despite this evolution, existing evaluations still benchmark agent memory mainly through end-to-end task success metrics (e.g., F1, BLEU), while treating the underlying system as a monolithic black box.
- **[2] The paper's end-to-end evaluation finds that no single architecture dominates across all scenarios; effectiveness depends on how well the memory structure aligns with the workload bottleneck.**
  > Our extensive end-to-end evaluation shows that no single architecture dominates across all scenarios; instead, effectiveness depends heavily on how well the memory structure aligns with the workload bottleneck.
- **[2] Through fine-grained ablation studies, the paper quantifies effects on representation fidelity, retrieval precision, update correctness, and long-horizon stability.**
  > Furthermore, through fine-grained ablation studies, we quantify their individual effects on representation fidelity, retrieval precision, update correctness, and long-horizon stability.
- **[3] The paper evaluates APEX-EM on five benchmarks: BigCodeBench, KGQAGen-10k, HLE, Lifelong Agent Bench, and ALFWorld.**
  > We evaluate on five benchmarks: BigCodeBench, KGQAGen-10k, HLE, Lifelong Agent Bench, and ALFWorld.
- **[3] Because prior work uses different backbones, the authors base their claims on same-backbone comparisons that hold model capability fixed.**
  > Because prior work uses different backbones, we base our claims on same-backbone comparisons that hold model capability fixed.
- **[4] Mem0 is evaluated on the LOCOMO benchmark against six baseline categories: established memory-augmented systems, RAG with varying chunk sizes and k-values, a full-context approach, an open-source memory solution, a proprietary model system, and a dedicated memory management platform.**
  > Through comprehensive evaluations on LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and k-values, (iii) a full-context approach that processes the entire conversation history, (iv) an open-source memory solution, (v) a proprietary model system, and (vi) a dedicated memory management platform.
- **[4] The methods are reported to consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain.**
  > Empirical results show that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain.
- **[5] The authors introduce eMEM-Bench v1, constructed over ProcTHOR-10K scenes for embodied memory evaluation.**
  > In addition we introduce eMEM-Bench v1, a benchmark we construct over ProcTHOR-10K scenes for embodied memory evaluation.
- **[5] The benchmark is organised around eight cognitive-psychology paradigms, and the authors claim surface-task benchmarks like LoCoMo or OpenEQA cannot provide the same level of diagnostic.**
  > The benchmark is organised explicitly around eight cognitive-psychology paradigms (DRM lures, pattern separation, pattern completion, source monitoring, context-dependent retrieval, long-horizon interference, serial position, and a foil augmented retention curve), each chosen so that the result is interpretable against the broader memory-systems literature in humans and prior agent-memory systems; a level of diagnostic that surface-task benchmarks like LoCoMo or OpenEQA cannot provide.
- **[5] eMEM scores 80.8 weighted mean over 988 probes, with a flat retention curve at ceiling from 1 h to 1 yr of simulated delay on room-unique items, and a pure RAG baseline loses 30 pt on context dependent retrieval and 29 pt on DRM lure rejection.**
  > eMEM scores 80.8 weighted mean over 988 probes, with a flat retention curve at ceiling from 1 h to 1 yr of simulated delay on room-unique items. We show that a pure RAG baseline (the flat_rag ablation) loses 30 pt on context dependent retrieval and 29 pt on DRM lure rejection, isolating the contribution of multi-layer storage and consolidation respectively.
- **[6] The paper introduces LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems help agents acquire the experience needed in customized web environments.**
  > LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can help agents acquire the experience needed to become knowledgeable colleagues in customized environments.
- **[6] LME-V2 contains 451 manually curated questions covering five core memory abilities for web agents: static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness.**
  > LME-V2 contains 451 manually curated questions covering five core memory abilities for web agents: static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness.
- **[6] Questions are paired with history trajectories containing up to 500 trajectories and 115M tokens.**
  > Questions are paired with history trajectories containing up to 500 trajectories and 115M tokens.
- **[6] The evaluation uses a context gathering formulation where memory systems consume history trajectories and return compact evidence for downstream question answering.**
  > We use a context gathering formulation: memory systems consume history trajectories and return compact evidence for downstream question answering.
- **[6] AgentRunbook-C achieves 72.5% average accuracy, outperforming the strongest RAG baseline (48.5%) and the off-the-shelf coding agent baseline (69.3%).**
  > Experiments show that AgentRunbook-C achieves the best performance with 72.5% average accuracy, outperforming the strongest RAG baseline (48.5%) and the off-the-shelf coding agent baseline (69.3%).
- **[6] Existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience.**
  > However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience.
- **[7] Evaluation used two long-horizon agentic memory benchmarks, long-term dialogue and agentic applications, across four open-source LLMs spanning 3B to 32B parameters.**
  > Across four open-source LLMs spanning 3B to 32B parameters and two long-horizon agentic memory benchmarks (long-term dialogue and agentic applications), AgentKVShift achieves near full recompute performance while refreshing only 10-30% of the cache, outperforming baselines at the same recompute ratio.
- **[8] Existing evaluations are typically published by framework providers and focus on token usage and latency, rarely accounting for system-level cost or deployment in distributed multi-agent systems.**
  > Existing evaluations are typically published by framework providers and focus on token usage and latency, rarely accounting for system-level cost or deployment in DMAS.
- **[9] The paper designs MPBench, a benchmark for evaluating memory poisoning attacks.**
  > Furthermore, we design MPBench -- a benchmark for evaluating memory poisoning attacks, and show that agents designed to write and retrieve memory more aggressively are more exploitable.
- **[11] The benchmark assesses strategies across three public datasets—LoCoMo, MultiDoc2Dial, and MSC—using Recall@k, MRR, nDCG@k, Answer F1, LLM-judge Faithfulness, Memory Footprint, and Latency over 491 annotated question turns.**
  > All are assessed across three public datasets covering long-term multi-session dialogue (LoCoMo), task-oriented document grounding (MultiDoc2Dial), and persona-grounded multi-session chat (MSC), using Recall@k, MRR, nDCG@k, Answer F1, an LLM-judge Faithfulness score, Memory Footprint, and Latency over 491 annotated question turns.
- **[11] Generation and judging both use Qwen2.5-7B-Instruct in 4-bit with greedy decoding for determinism.**
  > Generation and judging both use Qwen2.5-7B-Instruct (4-bit), with greedy decoding for determinism.
- **[11] The results report that EKV dominates on every quality axis, with macro Recall@5 of 0.792, MRR 0.677, F1 0.156, and Faithfulness 0.354.**
  > Our results show that (1) EKV dominates on every quality axis (macro Recall@5 0.792, MRR 0.677, F1 0.156, Faithfulness 0.354);
- **[11] On LoCoMo with long-range gold turns, ICW, WAM, GEM, and CBS retrieve almost nothing (Recall@5 <= 0.005), while EKV alone reaches 0.573, suggesting recency windows, summaries, and entity graphs collapse at long horizons.**
  > (2) long-range recall is decisive: on LoCoMo, where the gold turn lies many sessions back, ICW, WAM, GEM, and CBS retrieve almost nothing (Recall@5 <= 0.005) while EKV alone reaches 0.573, showing that recency windows, summaries, and entity graphs collapse at long horizons and only dense retrieval scales;
- **[11] CBS is the runner-up on retrieval with 0.556.**
  > (3) CBS is the runner-up on retrieval (0.556);
- **[12] The experiments in the paper were conducted on (Visual)WebArena.**
  > Our experiments on (Visual)WebArena reveal two key findings.
- **[13] In provenance evaluation, the system reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency.**
  > Provenance: Successfully reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency.
- **[14] Across three open-weight models on LoCoMo, at k=50 InferScale reduces TTFT by 72-79% (3.6-4.8x), achieves 60.3% accuracy versus 63.3% for Mem0 without serving-time recomputation, and delivers 3.7-4.5x throughput under concurrent load.**
  > Across three open-weight models on LoCoMo, InferScale keeps TTFT nearly constant as the retrieval budget increases: at k=50 it reduces TTFT by 72-79% (3.6-4.8x), achieves 60.3% accuracy versus 63.3% for Mem0 without serving-time recomputation, and delivers 3.7-4.5x the throughput under concurrent load.
- **[16] On LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at approximately 0.98, which the authors say measures retrieval rather than forgetting.**
  > We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting.
- **[16] In a realistic blind regime, a learned multi-factor value retains 0.770 ± 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model.**
  > In the realistic blind regime, a learned multi-factor value retains 0.770 \pm 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model.
- **[16] A controlled synthetic task with planted confounds shows the learner recovers a separating weighting with 1.00 retention, whereas uniform weighting fails with 0.62 retention.**
  > A controlled synthetic task with planted confounds confirms the learner recovers a separating weighting (1.00 retention) where uniform weighting fails (0.62).
- **[17] HORMA is evaluated across ALFWorld, LoCoMo, and LongMemEval, improving task performance under constrained context budgets and requiring at most 22.17% of baseline token usage in long conversation tasks.**
  > Across ALFWorld, LoCoMo, and LongMemEval, HORMA improves task performance under constrained context budgets while requiring at most 22.17% of the baseline token usage in long conversation tasks.
- **[18] The paper reports adversarial robustness, described as a hallucination resistance metric that no competing system reports, reaching 99.55%.**
  > Adversarial robustness, the hallucination resistance metric that no competing system reports, reaches 99.55%.
- **[19] AdMem reports experiments across various environments showing improved robustness and success on long multi-turn tasks versus existing baselines.**
  > Experiments across various environments show that our approach improves robustness and success on long multi-turn tasks compared to existing baselines.
- **[21] The paper states that existing benchmarks do not yet capture latency, token efficiency, and context-rot resistance, and points toward decision-level and organization-level context.**
  > We close with dimensions existing benchmarks do not yet capture, latency, token efficiency, and context-rot resistance, and the frontier of decision-level and organization-level context the category points toward.
- **[22] The paper releases a benchmark, harness, and machine-checked TLA+ models to support reproducibility.**
  > We release the benchmark, harness, and machine-checked TLA+ models to support reproducibility.
- **[23] In the DMR benchmark, which the MemGPT team established as its primary evaluation metric, Zep scores 94.8% versus 93.4%.**
  > In the DMR benchmark, which the MemGPT team established as their primary evaluation metric, Zep demonstrates superior performance (94.8% vs 93.4%).
- **[23] Zep is also evaluated on LongMemEval, described as a more challenging benchmark reflecting enterprise use cases through complex temporal reasoning tasks.**
  > Beyond DMR, Zep's capabilities are further validated through the more challenging LongMemEval benchmark, which better reflects enterprise use cases through complex temporal reasoning tasks.
- **[24] The survey discusses five types of graph-aware evaluation and governance protocols from a dynamic-graph perspective, complementing end-task evaluation.**
  > Finally, we discuss five types of graph-aware evaluation and governance protocols from a dynamic-graph perspective, which complement end-task evaluation.
- **[25] MemoryCD is introduced as the first large-scale, user-centric, cross-domain memory benchmark derived from lifelong real-world behaviors in the Amazon Review dataset.**
  > We introduce \textsc{MemoryCD}, the first large-scale, user-centric, cross-domain memory benchmark derived from lifelong real-world behaviors in the Amazon Review dataset.
- **[25] Existing memory datasets rely on scripted personas to generate synthetic user data, whereas MemoryCD tracks authentic user interactions across years and multiple domains.**
  > Unlike existing memory datasets that rely on scripted personas to generate synthetic user data, \textsc{MemoryCD} tracks authentic user interactions across years and multiple domains.
- **[25] The paper constructs a multi-faceted long-context memory evaluation pipeline using 14 state-of-the-art LLM base models, 6 memory method baselines, 4 personalization tasks, and 12 diverse domains.**
  > We construct a multi-faceted long-context memory evaluation pipeline of 14 state-of-the-art LLM base models with 6 memory method baselines on 4 distinct personalization tasks over 12 diverse domains to evaluate an agent's ability to simulate real user behaviors in both single and cross-domain settings.
- **[25] The benchmark is designed to evaluate an agent's ability to simulate real user behaviors in both single-domain and cross-domain settings.**
  > to evaluate an agent's ability to simulate real user behaviors in both single and cross-domain settings.
- **[25] The analysis reports that existing memory methods are far from user satisfaction in various domains and offers the first testbed for cross-domain life-long personalization evaluation.**
  > Our analysis reveals that existing memory methods are far from user satisfaction in various domains, offering the first testbed for cross-domain life-long personalization evaluation.
- **[25] LLM context windows have expanded to million-token scales, but benchmarks for evaluating memory remain limited to short-session synthetic dialogues.**
  > Recent advancements in Large Language Models (LLMs) have expanded context windows to million-token scales, yet benchmarks for evaluating memory remain limited to short-session synthetic dialogues.
- **[25] The paper was published as a workshop paper in Lifelong Agent at ICLR 2026.**
  > Comments:Published as a workshop paper in Lifelong Agent @ ICLR 2026
- **[27] SimSkill was evaluated on two held-out benchmarks across three backbone LLMs, with each result independently verified.**
  > We evaluate SimSkill on two held-out benchmarks across three backbone LLMs, with each result independently verified.
- **[29] The paper positions ATANT against a set of memory evaluations: LOCOMO, LongMemEval, BEAM, MemoryBench, Zep's evaluation suite, Letta/MemGPT's evaluations, and RULER.**
  > a recurring reviewer and practitioner question has concerned not the framework itself but its relationship to a wider set of memory evaluations: LOCOMO, LongMemEval, BEAM, MemoryBench, Zep's evaluation suite, Letta/MemGPT's evaluations, and RULER.
- **[29] Structural analysis shows none of these benchmarks measures continuity as defined in ATANT v1.0; median coverage is 1 of 7 required properties, mean coverage is 0.43 with partial credit at 0.5, and no eval covers more than 2 properties.**
  > We show by structural analysis that none of these benchmarks measures continuity as defined in v1.0: of the 7 required properties, the median existing eval covers 1 property, the mean covers 0.43 when partial credit is scored at 0.5, and no eval covers more than 2.
- **[29] The paper identifies methodological defects specific to each benchmark, including an empty-gold scoring bug in the LOCOMO reference implementation that renders 23% of its corpus unscorable by construction.**
  > We provide a cell-by-cell property-coverage matrix, identify methodological defects specific to each benchmark (including an empty-gold scoring bug in the LOCOMO reference implementation that renders 23% of its corpus unscorable by construction), and publish our reference implementation's LOCOMO score (8.8%) alongside the structural reason that number is uninformative about continuity.
- **[29] The authors' reference implementation scores 8.8% on LOCOMO and 96% on ATANT cumulative-scale, an 87-point divergence, which they present as evidence the benchmarks measure different properties.**
  > We publish our 8.8% LOCOMO score alongside our 96% ATANT cumulative-scale score as a calibration pair: the 87-point divergence is evidence that the two benchmarks measure different properties, not that one system is an order of magnitude better than another.
- **[29] The paper claims no existing benchmark can adjudicate continuity, and conflating them with continuity evaluation has led the field to under-invest in the properties ATANT v1.0 names.**
  > The claim is that none of them can adjudicate continuity, and conflating them with continuity evaluation has led the field to under-invest in the properties v1.0 names.
- **[30] The survey summarizes open-sourced libraries and benchmarks that support the development and evaluation of self-evolving agent memory.**
  > Third, we summarize the open-sourced libraries and benchmarks that support the development and evaluation of self-evolving agent memory.
- **[31] Existing evaluations of long-term memory for LLM agents largely test conversational recall in open-domain or persona-grounded settings, and the authors argue a stronger test is whether an agent can reuse prior-session information while acting over a live, structured, domain-specific environment.**
  > Long-term memory is becoming a core capability of LLM-based agents, but existing evaluations largely test conversational recall in open-domain or persona-grounded settings. We argue that a stronger test is whether an agent can reuse information from prior sessions while acting over a live, structured, domain-specific environment.
- **[31] The paper introduces IFCMemoryBench, a benchmark for evaluating long-term memory in LLM-based BIM information retrieval.**
  > We introduce IFCMemoryBench, a benchmark for evaluating long-term memory in LLM-based BIM information retrieval.
- **[31] IFCMemoryBench contains 143 multi-session tasks across 19 projects and 4,016 prior sessions, derived from incomplete-information questions in IFC-Bench v2.**
  > IFCMemoryBench contains 143 multi-session tasks across 19 projects and 4,016 prior sessions, derived from incomplete-information questions in IFC-Bench v2.
- **[34] The project evaluates on a Korean retrospective scenario set of 5 personas × 20 questions = 100 questions, with 25 each for single-hop, temporal, multi-hop, and preference, using LLM-as-a-Judge (paper Appendix A) and reporting J with 95% confidence intervals.**
  > 한국어 회고 시나리오 **페르소나 5개 × 20문항 = 100문항** (single-hop / temporal / multi-hop / preference 각 25개). 시나리오별로 다른 user_id로 주입해 격리를 겸사겸사 검증하며, 세션 주입 → 답변 생성 → LLM-as-a-Judge(논문 부록 A) 채점 → 유형별·시나리오별 J + 95% 신뢰구간 + 오답 목록 + 지연 리포트를 출력합니다:
- **[34] For 100 questions, the 95% CI is about ±8 percentage points, sufficient only for patterns, and verifying the paper's Mem0 vs Mem0g 2%p difference requires LOCOMO scale (~2,000 questions).**
  > 100문항 기준 표본 95% CI는 약 ±8%p — "유형별 난이도 패턴이 논문과 일치한다" 수준의 주장이 가능한 규모입니다. 논문의 Mem0 vs Mem0ᵍ 2%p 차이 검증에는 LOCOMO 규모(~2,000문항)가 필요합니다.
- **[38] The profile is assembled from publicly reachable material (company website, developer portal, documentation, public specifications, public repositories, public status/pricing/changelog pages) with no credentials and no breaching of systems.**
  > Everything here is assembled from material a member of the public can reach with a browser and no credentials — the company's own website, developer portal and documentation, the specifications it publishes for public use (OpenAPI, AsyncAPI, JSON Schema, apis.json, llms.txt and similar), its public repositories, and its public status, pricing and changelog pages.
- **[38] The Kin Score and Agent Readiness rating are independently calculated scores of public API artifacts against a published rubric; they are not certifications, endorsements, security assessments, or audits, and they score artifacts, not software quality, safety, or security.**
  > The Kin Score and Agent Readiness rating are independently calculated scores of a company's public API artifacts, produced by API Evangelist against a published rubric. They are not certifications, endorsements, security assessments, or audits, and they score published artifacts — not the quality, safety, or security of the software.

## q4. What are the costs: tokens, latency and storage of memory versus long context windows?

- **[2] The paper reports cost-performance trade-offs under realistic workloads and finds localized maintenance is more cost-efficient than global reorganization.**
  > Finally, we reveal cost-performance trade-offs under realistic workloads, showing localized maintenance is more cost-efficient than global reorganization.
- **[4] Mem0 reports markedly reduced computational overhead compared to the full-context method.**
  > Beyond accuracy gains, we also markedly reduce computational overhead compared to full-context method.
- **[4] Mem0 reports 91% lower p95 latency and more than 90% token cost savings.**
  > In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, offering a compelling balance between advanced reasoning capabilities and practical deployment constraints.
- **[6] Coding agent based memory methods have high latency costs, though AgentRunbook-C advances the accuracy-latency Pareto frontier.**
  > Despite the strong performance gains, coding agent based methods have high latency costs. While AgentRunbook-C advances the accuracy-latency Pareto frontier, substantial room for improvement remains.
- **[7] Every retrieval in these agentic memory systems triggers a full re-encoding of structured memory units into Key-Value states, which dominates prefill latency.**
  > From an inference cost standpoint, every retrieval triggers a full re-encoding of these structured memory units into Key-Value (KV) states, which dominates prefill latency.
- **[7] AgentKVShift refreshes only 10-30% of the cache while achieving near full recompute performance, and requires up to 5x lower recompute than prior reuse methods that need 45-55% refresh to reach similar performance.**
  > Across four open-source LLMs spanning 3B to 32B parameters and two long-horizon agentic memory benchmarks (long-term dialogue and agentic applications), AgentKVShift achieves near full recompute performance while refreshing only 10-30% of the cache, outperforming baselines at the same recompute ratio. It requires up to 5x lower recompute to reach this near-full performance, which prior reuse methods only attain at 45-55% refresh.
- **[7] AgentKVShift delivers prefill speedups of 2-3.5x over no-KV-reuse on a single A100.**
  > In this regime, AgentKVShift delivers prefill speedups of 2-3.5x over no-KV-reuse on a single A100.
- **[7] AgentKVShift orthogonally composes with KV cache quantization, retaining over 2x the F1 of prior reuse methods under aggressive 2- and 4-bit settings.**
  > AgentKVShift orthogonally composes with KV cache quantization, retaining over 2x the F1 of prior reuse methods under aggressive 2- and 4-bit settings.
- **[7] Existing training-free KV reuse methods were designed for RAG-style raw passages but degrade on structured agentic memories.**
  > Existing training-free KV reuse methods mitigate this by selectively recomputing a small fraction of tokens, but were designed for RAG-style raw passages and degrade on structured agentic memories.
- **[7] AgentKVShift estimates a shared memory-level offset from a small probe set to correct every reused token by a single weighted correction, and unlike prior reuse methods it also corrects tokens it does not recompute rather than leaving the rest of the cache stale.**
  > Estimating this offset from a small probe set allows us to correct every reused token by a single weighted correction. Unlike prior reuse methods which decide which tokens to recompute and leave the rest of the cache stale, AgentKVShift also corrects the tokens it does not recompute, turning the refresh budget into useful signal across the entire chunk.
- **[8] The RAG baseline matches the upper cluster at 8.4 times lower total cost of ownership than mem0, and both are the only non-dominated backends on the Pareto frontier.**
  > The RAG baseline matches the upper cluster at 8.4 times lower total cost of ownership (TCO) than mem0, and both are the only non-dominated backends on the Pareto frontier.
- **[8] Latency and bandwidth constraints and jitter leave retrieval quality unchanged for every backend, while vector-based LTM incurs a 4% to 5% latency penalty under edge-cloud constraints.**
  > Latency and bandwidth constraints as well as jitter leave retrieval quality unchanged for every backend, while vector-based LTM incurs a modest latency penalty of 4% to 5% under edge-cloud constraints.
- **[8] The paper's independent reproducible testbed evaluates accuracy, latency, CPU time, peak RAM, disk I/O, and network usage in a simulated cloud-edge environment.**
  > These gaps are addressed with an independent reproducible testbed that evaluates accuracy, latency, CPU time, peak RAM, disk I/O and network usage in a simulated cloud-edge environment.
- **[10] Long-term memory lets an agent recall specific details relevant to the current task, reducing the need for large context windows.**
  > When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows.
- **[11] EKV's recall advantage carries a memory footprint cost of about 5,100 tokens versus about 300 tokens for ICW/WAM, an explicit accuracy-efficiency trade-off.**
  > (5) EKV's recall advantage carries a footprint cost (~5,100 vs ~300 tokens for ICW/WAM), an explicit accuracy-efficiency trade-off.
- **[13] The paper concludes that long-context retrieval alone is insufficient for production multi-agent memory, and that governed shared memory demands explicit systems-level abstractions and live evaluation.**
  > Conclusion: Long-context retrieval alone is insufficient for production multi-agent memory. Governed shared memory demands explicit systems-level abstractions, and live evaluation is vital to expose enforcement and pipeline-ordering failures missed by design-only treatments.
- **[14] As the retrieval budget grows, time-to-first-token increases even though the underlying memory is reused across requests.**
  > As the retrieval budget grows, time-to-first-token (TTFT) increases even though the underlying memory is reused across requests.
- **[14] Reusable KV state decouples memory-conditioned serving latency from retrieved-context size while preserving application quality.**
  > Reusable KV state thus decouples memory-conditioned serving latency from retrieved-context size while preserving application quality.
- **[16] Long-running LLM agents accumulate interaction histories far larger than any context window, forcing decisions about what to encode deeply, forget, and retrieve under a fixed memory budget.**
  > Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget.
- **[16] The substrate is open-source and all experiments run on a single CPU with no API calls.**
  > The substrate is open-source; all experiments run on a single CPU with no API calls.
- **[17] The paper says LLM agents are stateless in long-horizon tasks, requiring all task-relevant information in growing input contexts, which causes degraded reasoning quality, increased inference cost, and higher latency, motivating efficient working memory.**
  > Large language model (LLM) agents struggle with long-horizon tasks due to their inherent statelessness, requiring all task-relevant information to be encoded in growing input contexts. The resulting degraded reasoning quality, increased inference cost, and higher latency necessitate efficient working memory mechanisms.
- **[17] HORMA's navigation module uses a lightweight reinforcement-learning-trained agent to select minimal yet sufficient context while traversing the hierarchy, reducing latency along the critical execution path.**
  > The navigation module retrieves task-relevant context by traversing the hierarchy using a lightweight agent trained with reinforcement learning to select minimal yet sufficient context, thereby reducing latency along the critical execution path.
- **[18] Synthius-Mem claims to reduce token consumption by about 5x compared with full-context replay while achieving higher accuracy.**
  > Synthius-Mem reduces token consumption by ~5x compared to full-context replay while achieving higher accuracy.
- **[21] The paper makes an economic case that naive context accumulation grows token cost quadratically with conversation length, crude summarization makes cost linear but causes an accuracy cliff, and only validated compaction achieves linear cost while preserving fidelity.**
  > We then make the economic case: naive context accumulation grows token cost quadratically in conversation length, crude summarization buys linear cost at the price of an accuracy cliff, and only validated compaction achieves linear cost with preserved fidelity.
- **[23] On LongMemEval, Zep reports accuracy improvements of up to 18.5% while reducing response latency by 90% compared with baseline implementations.**
  > In this evaluation, Zep achieves substantial results with accuracy improvements of up to 18.5% while simultaneously reducing response latency by 90% compared to baseline implementations.
- **[26] The paper states that long-horizon LLM inference makes the KV cache the dominant GPU memory consumer and makes per-token attention increasingly expensive.**
  > Long-horizon LLM inference turns the key--value (KV) cache into the dominant GPU memory consumer and makes per-token attention increasingly expensive.
- **[26] CONF-KV keeps memory footprint near a fixed 512-token sliding window while staying within 1.5--2.1 perplexity points of full KV across four model families and generated lengths up to 4K.**
  > Across four model families and generated lengths up to 4K, CONF-KV stays near the footprint of a fixed 512-token sliding window while remaining within 1.5--2.1 perplexity points of full KV.
- **[26] On Needle-in-a-Haystack up to 32K tokens, CONF-KV reaches 91.4% retrieval accuracy versus 53.8% for sliding windows and 80.6% for H2O; on 75 VisualWebArena tasks it retains 95.3% of full-KV success at 2.8 times lower peak memory.**
  > On Needle-in-a-Haystack up to 32K tokens, CONF-KV reaches 91.4% retrieval accuracy versus 53.8% for sliding windows and 80.6% for H2O; on 75 VisualWebArena tasks it retains 95.3% of full-KV success at 2.8 times lower peak memory.
- **[26] CONF-KV combines blockwise online-softmax attention, mixed FP16/INT8 storage, and a pyramidal per-layer budget variant.**
  > We combine the policy with blockwise online-softmax attention, mixed FP16/INT8 storage, and a pyramidal per-layer budget variant.
- **[26] CONF-KV uses the next-token distribution as a scalar confidence score to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when confident.**
  > We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident.
- **[26] Within each budget, tokens are ranked by accumulated attention mass and recency, with a protected recent window preserving local coherence.**
  > Within each budget, tokens are ranked by a composite of accumulated attention mass and recency, while a protected recent window preserves local coherence.
- **[27] The benefits of SimSkill's memory are backbone- and budget-dependent; memory does not improve every model or uniformly reduce inference cost.**
  > Its benefits remain backbone- and budget-dependent, as memory does not improve every model or uniformly reduce inference cost.
- **[32] The paper identifies KV cache size growing linearly with sequence length and being retained throughout decoding as a dominant memory bottleneck that makes full GPU caching prohibitively expensive without compression.**
  > Large language models increasingly operate over long contexts, where the KV cache becomes a dominant memory bottleneck: its size grows linearly with sequence length and must be retained throughout decoding, making full GPU caching prohibitively expensive without compression.
- **[32] Existing KV cache compression methods are described as struggling to balance efficiency and faithful context preservation: token eviction discards information, while semantic grouping fixes compression decisions at prefill time and cannot recover token-level detail once a compressed span becomes relevant.**
  > Existing KV cache compression methods struggle to balance efficiency with faithful context preservation. Token eviction discards information, while semantic grouping fixes compression decisions at prefill time; neither can recover token-level detail from a compressed span once it becomes relevant during generation.
- **[32] SeKV organizes context into entropy-guided semantic spans stored across a GPU-CPU memory hierarchy without discarding information, keeping a lightweight summary vector on GPU and a low-rank SVD basis on CPU for on-demand token-level reconstruction.**
  > As a solution, we propose SeKV, a resolution-adaptive semantic KV cache that organizes context into entropy-guided semantic spans and stores them across a GPU-CPU memory hierarchy without discarding information. Each span keeps a lightweight summary vector on GPU for coarse routing and a low-rank SVD basis on CPU for on-demand token-level reconstruction.
- **[32] SeKV enables adaptive token-level reconstruction while keeping the base LLM frozen and adds fewer than 0.05% trainable parameters.**
  > SeKV enables adaptive token-level reconstruction while keeping the base LLM fully frozen and adding fewer than 0.05% trainable parameters.
- **[32] Across four benchmarks, SeKV improves over the strongest semantic compression baseline by 5.9% on average while reducing GPU memory by 53.3% versus full KV caching at 128K context.**
  > Across four benchmarks, SeKV improves over the strongest semantic compression baseline by 5.9% on average while reducing GPU memory by 53.3% versus full KV caching at 128K context.
- **[34] An asynchronous write queue separates extraction/update to minimize response latency, and disabling graph memory saves LLM calls/cost per turn.**
  > *   `MEMOIR_ASYNC_WRITE=1` — 쓰기(추출·갱신)를 백그라운드 큐로 분리 (Phase 3, 응답 지연 최소화)
*   `MEMOIR_GRAPH_ENABLED=0` — 그래프 메모리 끄기 (턴당 LLM 호출·비용 절감)
- **[35] A Phase A storage refactor moves to a single PostgreSQL instance with AGE and pgvector, adding a STORAGE_BACKEND switch with values kuzu_chroma or postgres, idempotent initialization of the pgvector extension, an HNSW vector table and an AGE graph, with automatic degradation when extensions are missing.**
  > refactor(storage): Phase A — 单 PG(AGE+pgvector) 基础设施 + STORAGE_BACKEND 开关 - core/config: 新增 storage_backend(kuzu_chroma|postgres) 开关 + AGE/pgvector 配置 - core/adapters/pg_init: 幂等初始化 pgvector 扩展+向量表(HNSW) 与 AGE 图，缺失自动降级
- **[36] Letta claims context-window optimization reduces costs and improves processing speed.**
  > *   📋 **Efficient Context Optimization**: Optimize LLM context window usage to reduce costs and improve processing speed.
- **[37] The provider warms the Zep user cache between turns for low-latency retrieval.**
  > Warms the Zep user cache between turns for low-latency retrieval

## q5. What goes wrong with agent memory in production: forgetting, staleness, contradictions, privacy, poisoning?

- **[2] Critical system-level concerns including operational costs, architectural trade-offs across memory modules, and robustness under dynamic knowledge updates remain insufficiently explored.**
  > As a result, critical system-level concerns, including operational costs, architectural trade-offs across memory modules, and robustness under dynamic knowledge updates, remain insufficiently explored.
- **[4] Fixed context windows are described as posing fundamental challenges for maintaining consistency over prolonged multi-session dialogues.**
  > Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues.
- **[9] Persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can have long-term influence over agent behavior.**
  > However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term influence over agent behavior.
- **[9] The paper identifies four memory write channels and nine structural vulnerabilities in model capabilities, system prompt design, and agent system architecture.**
  > We identify four memory write channels and nine structural vulnerabilities in model capabilities, system prompt design, and agent system architecture that make these channels exploitable.
- **[9] Based on the identified vulnerabilities, the paper develops a taxonomy of six classes of memory poisoning attacks.**
  > Based on these vulnerabilities, we develop a taxonomy of six classes of memory poisoning attacks.
- **[9] Agents designed to write and retrieve memory more aggressively are more exploitable.**
  > Furthermore, we design MPBench -- a benchmark for evaluating memory poisoning attacks, and show that agents designed to write and retrieve memory more aggressively are more exploitable.
- **[9] Existing prompt injection defenses fail to cover memory poisoning attacks.**
  > We also show that existing prompt injection defenses fail to cover memory poisoning attacks.
- **[9] The paper presents a systematic study of memory poisoning in LLM-based agents.**
  > We present a systematic study of memory poisoning in LLM-based agents.
- **[10] Personal assistant agents sit at the convergence of two domains, handle sensitive information while interacting with untrusted information sources, and create previously unaccounted security vulnerabilities.**
  > Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities.
- **[10] The paper introduces GhostWriter, an attack vector that exploits current memory subsystems in tool-using personal agents to poison their memory store.**
  > In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store.
- **[10] GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent, and activation, in which the poisoned memory is retrieved.**
  > GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved.
- **[10] GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents.**
  > We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents.
- **[10] The attack is possible due to the lack of security-focused memory governance.**
  > This attack is possible due to the lack of security-focused memory governance.
- **[10] The paper proposes Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen.**
  > In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen.
- **[12] The paper introduces eTAMP, described as the first attack achieving cross-session, cross-site compromise without direct memory access.**
  > We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access.
- **[12] A single contaminated observation can silently poison an agent's memory and later activate on different websites, bypassing permission-based defenses.**
  > A single contaminated observation (e.g., viewing a manipulated product page) silently poisons an agent's memory and activates during future tasks on different websites, bypassing permission-based defenses.
- **[12] eTAMP achieves attack success rates up to 32.5% on GPT-5-mini, 23.4% on GPT-5.2, and 19.5% on GPT-OSS-120B.**
  > First, eTAMP achieves substantial attack success rates: up to 32.5% on GPT-5-mini, 23.4% on GPT-5.2, and 19.5% on GPT-OSS-120B.
- **[12] The paper reports Frustration Exploitation: environmental stress can increase attack success rates by up to 8 times when agents struggle with dropped clicks or garbled text.**
  > Second, we discover Frustration Exploitation: agents under environmental stress become dramatically more susceptible, with ASR increasing up to 8 times when agents struggle with dropped clicks or garbled text.
- **[12] More capable models are not necessarily more secure; GPT-5.2 shows substantial vulnerability despite superior task performance.**
  > Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance.
- **[12] The rise of AI browsers such as OpenClaw, ChatGPT Atlas, and Perplexity Comet is cited as underscoring the need for defenses against environment-injected memory poisoning.**
  > With the rise of AI browsers like OpenClaw, ChatGPT Atlas, and Perplexity Comet, our findings underscore the urgent need for defenses against environment-injected memory poisoning.
- **[13] The paper identifies four foundational failure modes for multi-agent shared memory: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.**
  > This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.
- **[13] Propagation evaluation demonstrated high intra-fleet visibility with zero cross-fleet leakage; under strong write mode, write-to-visible latency was optimized to a single search round-trip.**
  > Propagation: Demonstrated high intra-fleet visibility with zero cross-fleet leakage. Under strong write mode, write-to-visible latency was optimized to a single search round-trip.
- **[13] A production issue found asymmetric scope enforcement: tenant isolation held, but sub-tenant scope was initially bypassed on direct GET-by-id requests for agent-scoped credentials.**
  > Asymmetric Scope Enforcement: Tenant isolation held, but sub-tenant scope was initially bypassed on direct GET-by-id requests for agent-scoped credentials (disclosed and remediated during the study).
- **[13] A pipeline ordering conflict can cause a synchronous near-duplicate gate to prematurely reject contradictory writes before the asynchronous contradiction detector evaluates them.**
  > Pipeline Ordering Conflict: While contradiction supersession works for admitted writes, a synchronous near-duplicate gate can prematurely reject contradictory writes before the asynchronous contradiction detector can evaluate them.
- **[15] The attack's key insight is that a poisoned relation can share the same query-activated anchor and canonicalized relation channel as benign evidence while carrying a conflicting value.**
  > Its key insight is that a poisoned relation can share the same query-activated anchor and canonicalized relation channel as benign evidence while carrying a conflicting value.
- **[15] The attack pipeline, AIR, converts the conflict into an ordinary interaction that can be extracted, merged, and retrieved by the graph-memory system.**
  > To realize this, we design AIR, a pipeline that converts the conflict into an ordinary interaction that can be extracted, merged, and retrieved by the graph-memory system.
- **[15] SHADOWMERGE achieves 93.8% average attack success rate, improving the best baseline by 50.3 absolute points, with negligible impact on unrelated benign tasks.**
  > SHADOWMERGE achieves 93.8% average attack success rate, improving the best baseline by 50.3 absolute points, while having negligible impact on unrelated benign tasks.
- **[15] Mechanism studies show SHADOWMERGE overcomes three key limitations of existing agent-memory poisoning attacks, and defense analysis shows representative input-side defenses are insufficient to mitigate it.**
  > Mechanism studies show that SHADOWMERGE overcomes the three key limitations of existing agent-memory poisoning attacks, and defense analysis shows that representative input-side defenses are insufficient to mitigate it.
- **[15] The authors responsibly disclosed the findings to affected graph-memory vendors and open sourced SHADOWMERGE.**
  > We have responsibly disclosed our findings to affected graph-memory vendors and open sourced SHADOWMERGE.
- **[16] Production systems use semantic similarity or recency to make memory decisions, but these are mis-specified for the forgetting decision, which happens at consolidation time before the future query is known.**
  > Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known.
- **[16] The learned weights are interpretable: reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is down-weighted for the forgetting decision.**
  > The learned weights are interpretable -- reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is correctly down-weighted for the forgetting decision.
- **[17] The paper says existing approaches rely on lossy compression or similarity-based retrieval, which often fail to capture temporal structure and causal dependencies required for multi-step agentic tasks.**
  > However, existing approaches either rely on lossy compression or similarity-based retrieval, which often fail to capture temporal structure and causal dependencies required for multi-step agentic tasks.
- **[17] HORMA's construction module iteratively refines experience structuring by distinguishing failures caused by missing information from failures caused by misleading or overloaded context.**
  > The construction module iteratively refines how experiences are structured by distinguishing between failures caused by missing information and those caused by misleading or overloaded context.
- **[18] The paper states that providing AI agents with reliable long-term memory that does not hallucinate remains an open problem.**
  > Providing AI agents with reliable long-term memory that does not hallucinate remains an open problem.
- **[19] LLM tool-using agents remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge.**
  > Large Language Models (LLMs) show promise as tool-using agents but remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge.
- **[20] LLM agents with persistent memory are vulnerable to memory poisoning attacks, where adversaries inject malicious instructions through query-only interactions that corrupt long-term memory and influence future responses.** (also [22])
  > Large language model agents equipped with persistent memory are vulnerable to memory poisoning attacks, where adversaries inject malicious instructions through query only interactions that corrupt the agents long term memory and influence future responses.
- **[20] The MINJA memory injection attack was reported to achieve over 95% injection success rate and 70% attack success rate under idealized conditions.**
  > Recent work demonstrated that the MINJA (Memory Injection Attack) achieves over 95 % injection success rate and 70 % attack success rate under idealized conditions.
- **[20] The paper systematically evaluates memory poisoning attacks and defenses in EHR agents, varying initial memory state, number of indication prompts, and retrieval parameters.**
  > This work addresses these gaps through systematic empirical evaluation of memory poisoning attacks and defenses in Electronic Health Record (EHR) agents. We investigate attack robustness by varying three critical dimensions: initial memory state, number of indication prompts, and retrieval parameters.
- **[20] Experiments on GPT-4o-mini, Gemini-2.0-Flash, and Llama-3.1-8B-Instruct using MIMIC-III clinical data show that realistic conditions with pre-existing legitimate memories dramatically reduce attack effectiveness.**
  > Our experiments on GPT-4o-mini, Gemini-2.0-Flash and Llama-3.1-8B-Instruct models using MIMIC-III clinical data reveal that realistic conditions with pre-existing legitimate memories dramatically reduce attack effectiveness.
- **[20] The paper proposes and evaluates two defenses: Input/Output Moderation using composite trust scoring across multiple orthogonal signals, and Memory Sanitization with trust-aware retrieval using temporal decay and pattern-based filtering.**
  > We then propose and evaluate two novel defense mechanisms: (1) Input/Output Moderation using composite trust scoring across multiple orthogonal signals, and (2) Memory Sanitization with trust-aware retrieval employing temporal decay and pattern-based filtering.
- **[20] Effective memory sanitization requires careful trust threshold calibration to avoid both overly conservative rejection of all entries and insufficient filtering that misses subtle attacks.**
  > Our defense evaluation reveals that effective memory sanitization requires careful trust threshold calibration to prevent both overly conservative rejection (blocking all entries) and insufficient filtering (missing subtle attacks), establishing important baselines for future adaptive defense mechanisms.
- **[20] The paper claims its findings provide insights for securing memory-augmented LLM agents in production environments.**
  > These findings provide crucial insights for securing memory-augmented LLM agents in production environments.
- **[21] Production AI agent failures are more often caused by an inability to manage reasoning context, such as conversation histories, prompts, tool definitions, and tool outputs, than by poor reasoning; agents accumulate history and incur growing token costs, producing missing recalls within and across conversations.**
  > Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations.
- **[22] Existing defenses base a memory item's authority on either its content or its derivation history, and the paper shows both signals are malleable.**
  > Existing defenses base a memory item's authority to act on either its content (detection or trust-scoring) or its derivation history (lineage). We show that both signals are malleable.
- **[22] An attacker can launder an untrusted origin through three LLM-agent-specific channels: the agent's own summarization, a trusted-tool echo, and manufactured corroboration.**
  > An attacker can launder an untrusted origin through three channels specific to LLM agents: the agent's own summarization, a trusted-tool echo, and manufactured corroboration.
- **[22] The paper formalizes malleability for the memory write-retrieve-act pipeline and proves a machine-checked separation theorem: no content- or lineage-based defense is sound under laundering, write-time origin binding is necessary, and non-malleable origin-bound authority with Sybil-resistant corroboration-gated elevation is sufficient.**
  > We formalize malleability for the memory write-retrieve-act pipeline and prove a machine-checked separation theorem. No content- or lineage-based defense is sound under laundering (T1), write-time origin binding is necessary (T2), and non-malleable origin-bound authority with Sybil-resistant corroboration-gated elevation is sufficient (T3).
- **[22] The TMA-NM construction instantiates non-malleable information-flow control for LLM-agent memory.**
  > Our construction, TMA-NM (Tamper-evident Memory Authority, Non-Malleable), instantiates non-malleable information-flow control (IFC) for LLM-agent memory.
- **[22] A cross-defense, cross-attack, and cross-model benchmark over eight frontier models shows existing defenses fail where the theory predicts, with up to 68% laundering attack-success, while TMA-NM reaches 0% attack success on direct and laundering attacks across all models and channels at full legitimate utility.**
  > A cross-defense, cross-attack, and cross-model benchmark over eight frontier models shows that existing defenses fail exactly where the theory predicts (up to 68% laundering attack-success), while TMA-NM reaches 0% attack success on both direct and laundering attacks across all models and channels, at full legitimate utility.
- **[28] Harness design integrates memory, tool use, and runtime control into LLM-based agents, but also introduces security and privacy risks because malicious instructions from external sources may be written into persistent memory and persist across sessions.**
  > Harness design has transformed the development of LLM-based agents by integrating memory, tool use, and runtime control. However, this design also introduces security and privacy risks because malicious instructions from external sources may be written into persistent memory and persist across sessions.
- **[28] The paper proposes PMPA, a Persistent Memory Poisoning Attack against harness-based agents, which embeds malicious instructions into benign external sources and induces the victim agent to write them into persistent memory without directly accessing the agent framework.**
  > To study this risk, we propose PMPA, a Persistent Memory Poisoning Attack against harness-based agents. PMPA embeds malicious instructions into benign external sources and induces the victim agent to write them into persistent memory without directly accessing to the agent framework.
- **[28] Once poisoned memory is stored, it can be retrieved in later sessions, triggering additional malicious actions and causing privacy leakage.**
  > Once stored, the poisoned memory can be retrieved in later sessions, triggering additional malicious actions and causing privacy leakage.
- **[28] PMPA was evaluated on OpenClaw and Claude Code across different backbone LLMs, input modalities, and trigger scenarios.**
  > We evaluate PMPA on OpenClaw and Claude Code across different backbone LLMs, input modalities, and trigger scenarios.
- **[28] Across all settings, PMPA achieved average Injection Success Rate and Cross-session Attack Success Rate of 73.7% and 55.5% on OpenClaw, and 66.9% and 81.7% on Claude Code, while preserving benign task performance on both systems.**
  > Across all settings, PMPA achieves average Injection Success Rate (ISR) and Cross-session Attack Success Rate (C-ASR) of 73.7%/ 55.5% on OpenClaw and 66.9%/ 81.7% on Claude Code, while preserving benign task performance on both systems.
- **[28] A targeted prompt-level defense reduced memory injection in many settings but provided limited protection once the persistent memory had been poisoned.**
  > We further evaluate a targeted prompt-level defense and find that it can reduce memory injection in many settings, but provides limited protection once the persistent memory has been poisoned.
- **[30] The survey identifies critical challenges and future research directions for graph-based agent memory.**
  > Finally, we identify critical challenges and future research directions.
- **[31] Current general-purpose memory systems often retrieve topically relevant context but store project knowledge as incomplete or fragmented facts.**
  > Analysis shows that current general-purpose memory systems often retrieve topically relevant context but store project knowledge as incomplete or fragmented facts.
- **[31] The results reveal a domain-transfer gap in agent memory and suggest that reliable professional agents require domain-aware memory representations linking conversations, project knowledge, and structured model entities.**
  > These results reveal a domain-transfer gap in agent memory and suggest that reliable professional agents require domain-aware memory representations linking conversations, project knowledge, and structured model entities.
- **[33] Writable, cross-session persistent memory in LLM agents creates a qualitatively different threat landscape from conventional input-centric security, characterized by persistence, statefulness, and propagation.**
  > The emergence of writable, cross-session persistent memory in LLM agents introduces a qualitatively different threat landscape from conventional input-centric security concerns, characterized by three properties: persistence, statefulness, and propagation.
- **[33] The source argues formal security guarantees are needed at the system level and proposes Verifiable Memory Governance (VMG), a framework of five architectural primitives for auditable, recoverable control over memory state.**
  > This analysis in turn exposes the need for formal security guarantees at the system level, motivating Verifiable Memory Governance (VMG), a framework of five architectural primitives that specifies what verifiable mechanisms a long-term-memory system must provide to maintain auditable, recoverable control over its memory state.
- **[33] The source concludes that robust Long-Term Memory (LTM) security cannot be retrofitted only at retrieval or execution time; it must be anchored in storage-time provenance, versioning, and policy-aware retention from the outset.**
  > Our analysis indicates that robust Long-Term Memory (LTM) security cannot be retrofitted at retrieval or execution time alone, but must be anchored in storage-time provenance, versioning, and policy-aware retention from the outset.
- **[33] The source's memory security taxonomy includes Integrity, Confidentiality, Availability, and Governance objectives, and includes a Forget & Rollback phase in the memory lifecycle.**
  > To systematically characterize this landscape, we propose a Memory Lifecycle Framework that organizes attacks, defenses, and their cross-phase dependencies along two axes: six lifecycle phases (Write, Store, Retrieve, Execute, Share &Propagate, Forget &Rollback) and four security objectives (Integrity, Confidentiality, Availability, Governance).
- **[34] Tests cover duplicate facts becoming NOOP, contradictions causing soft DELETE excluded from retrieval but preserved, UPDATE merging with audit history, hallucinated memory_id safely falling back to NOOP, and user_id isolation.**
  > *   중복 사실 → NOOP (중복 방지)
*   모순 정보 → soft DELETE, 검색 제외 + 데이터 보존
*   UPDATE → 병합 + ADD→UPDATE 감사 이력
*   LLM이 존재하지 않는 memory_id 지목(환각) → 안전한 NOOP 폴백
*   user_id 격리 — 다른 사용자 메모리가 검색·갱신 후보에 절대 노출되지 않음
- **[34] The paper's OpenAI memory collapsed to J<15% on temporal questions due to missing timestamps, so the implementation normalizes Korean relative time expressions to absolute dates in extraction.**
  > 원 논문과 달리 **한국어 상대 시간 정규화**("지지난주", "재작년" → 절대 날짜)를 추출 단계에 내장했습니다. 논문에서 OpenAI 메모리가 temporal 질문에서 J<15%로 폭락한 원인이 타임스탬프 누락이었기 때문에, 시간 정보 보존을 1급 요구사항으로 다룹니다.
- **[35] The platform provides multi-tenancy, project isolation, button-level RBAC and full-chain auditing.**
  > 多租户 + 项目隔离 + RBAC（按钮级）+ 全链路审计
- **[35] Rate limiting uses a per-tenant Redis fixed window that returns HTTP 429 when over limit and fails open when Redis is unavailable; a real Redis test of 7 requests against a limit of 5 let 5 through and rejected 2.**
  > 限流中间件(api/middlewares/ratelimit)：per-tenant Redis 固定窗口，超限 429， Redis 不可用 fail-open。真 Redis 验证：7 请求@限5 → 5 放行 2 拒绝
- **[37] Facts in Zep include temporal validity ranges so the agent can reason about what is current versus outdated.**
  > Facts include temporal validity ranges so the agent can reason about what's current vs. outdated.

## Sources

1. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory — Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu (academic, 2024-10-14, quality 1.0) — https://arxiv.org/abs/2410.10813
2. Are We Ready For An Agent-Native Memory System? — Wei Zhou, Xuanhe Zhou, Shaokun Han, Hongming Xu, Guoliang Li, Zhiyu Li, Feiyu Xiong, Fan Wu (academic, 2026-06-23, quality 1.0) — https://arxiv.org/abs/2606.24775
3. APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay — Pratyay Banerjee, Masud Moshtaghi, Ankit Chadha (academic, 2026-03-31, quality 1.0) — https://arxiv.org/abs/2603.29093
4. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav (academic, 2025-04-28, quality 1.0) — https://arxiv.org/abs/2504.19413
5. eMEM: A Hybrid Spatio-Temporal Memory System For Embodied Agents — A. Haroon Rasheed, Maria Kabtoul (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2606.03374
6. LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues — Di Wu et al. (arXiv) (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2605.12493
7. AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems — Nilesh Prasad Pandey et al. (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2607.21604
8. Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models — Benedict Wolff, Jacopo Bennati (academic, 2026-01-12, quality 1.0) — https://arxiv.org/abs/2601.07978
9. From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents — Pritam Dash, Tongyu Ge, Aditi Jain, Tanmay Shah, Zhiwei Shang (academic, 2026-06-03, quality 1.0) — https://arxiv.org/abs/2606.04329
10. When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents — George Torres, Sharad Shrestha, Satyajayant Misra (academic, 2026-07-06, quality 1.0) — https://arxiv.org/abs/2607.06595
11. AgentMemBench: A Systematic Benchmark for Evaluating Long-Term Memory Management Strategies in Conversational AI Agents — Ahmed Cherif (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2608.00009
12. Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents — Wei Zou, Mingwen Dong, Miguel Romero Calvo, Shuaichen Chang, Jiang Guo, Dongkyu Lee, Xing Niu, Xiaofei Ma, Yanjun Qi, Jiarong Jiang (academic, 2026-04-03, quality 1.0) — https://arxiv.org/abs/2604.02623
13. Governed Shared Memory for Multi-Agent LLM Systems — Yanki Margalit, Nurit Cohen-Inger, Erni Avram, Ran Taig, Oded Margalit (academic, 2026-06-23, quality 1.0) — https://arxiv.org/abs/2606.24535
14. InferScale: GPU-Native KV Injection for Personalized LLM Serving — Peter Li, Prashant Pandey (academic, 2026-07-29, quality 1.0) — https://arxiv.org/abs/2607.27090
15. ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts — Yang Luo, Zifeng Kang, Tiantian Ji, Xinran Liu, Yong Liu, Shuyu Li, Lingyun Peng (academic, 2026-05-09, quality 1.0) — https://arxiv.org/abs/2605.09033
16. Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory — Zhibao Chen, Qian Cheng (academic, 2026-06-11, quality 1.0) — https://arxiv.org/abs/2606.12945
17. Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents — Hao-Lun Hsu, Nikki Lijing Kuang, Boyi Liu, Zhewei Yao, Yuxiong He (academic, 2026-06-10, quality 1.0) — https://arxiv.org/abs/2606.11680
18. Synthius-Mem: Brain-Inspired Hallucination-Resistant Persona Memory Achieving 94.4% Memory Accuracy and 99.6% Adversarial Robustness on LoCoMo — Artem Gadzhiev and Andrew Kislov (academic, 2026-04-13, quality 1.0) — https://arxiv.org/abs/2604.11563
19. AdMem: Advanced Memory for Task-solving Agents — Runzhe Wang, Huilin Lu, Shengjie Liu, Li Dong, Jason Zhu (academic, 2026-06-05, quality 1.0) — https://arxiv.org/abs/2606.06787
20. Memory Poisoning Attack and Defense on Memory Based LLM-Agents — Balachandra Devarangadi Sunil, Isheeta Sinha, Piyush Maheshwari, Shantanu Todmal, Shreyan Mallik, Shuchi Mishra (academic, 2026-01-09, quality 1.0) — https://arxiv.org/abs/2601.05504
21. Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems — Gaurav Dadhich (academic, 2026-07-23, quality 1.0) — https://arxiv.org/abs/2607.21503
22. Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees — Yedidel Louck (academic, 2026-06-23, quality 1.0) — https://arxiv.org/abs/2606.24322
23. Zep: A Temporal Knowledge Graph Architecture for Agent Memory — Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, Daniel Chalef (academic, 2025-01-20, quality 1.0) — https://arxiv.org/abs/2501.13956
24. Self-Evolving Agents as Dynamic Graph Transformation: A Survey and New Perspective — Yuanyuan Xu, Wenjie Zhang, Yin Chen, Xuemin Lin, Ying Zhang (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2608.18104
25. MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization — Weizhi Zhang, Xiaokai Wei, Wei-Chieh Huang, Zheng Hui, Chen Wang, Michelle Gong, Philip S. Yu (academic, 2026-03-26, quality 1.0) — https://arxiv.org/abs/2603.25973
26. CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM — Yubo Li; Yidi Miao (academic, 2026-05-24, quality 1.0) — https://arxiv.org/abs/2605.24786
27. SimSkill: A Self-Evolving LLM Agent for Skill and Knowledge Accumulation in Traffic Simulation — Qi Liu, Qinzheng Wang, Can Li, Yiming Bie, Wanjing Ma (academic, 2026-09-03, quality 1.0) — https://arxiv.org/abs/2609.03753
28. When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents — Shuhuai Huang, Jingfeng Zhang, Hong Jia (academic, 2026-09-15, quality 1.0) — https://arxiv.org/abs/2609.13889
29. ATANT v1.1: Positioning Continuity Evaluation Against Memory, Long-Context, and Agentic-Memory Benchmarks — Samuel Sameer Tanguturi (academic, 2026-04-19, quality 1.0) — https://arxiv.org/abs/2604.10981
30. Graph-based Agent Memory: Taxonomy, Techniques, and Applications — Chang Yang and 17 other authors (academic, 2026-02-05, quality 1.0) — https://arxiv.org/abs/2602.05665
31. IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval — Changyu Du, Alexander Vosseler, Filippo Mazza, André Borrmann (academic, 2026-07-13, quality 1.0) — https://arxiv.org/abs/2607.26072
32. SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference — Amirhossein Abaskohi, Giuseppe Carenini, Peter West, Yuhang He (academic, 2026-06-30, quality 1.0) — https://arxiv.org/abs/2606.31145
33. A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle — Zehao Lin, Xixuan Hao, Renyu Fu, Shaobo Cui, Kai Chen, Chunyu Li, Zhiyu Li, Feiyu Xiong (academic, 2026-09-23, quality 1.0) — https://arxiv.org/abs/2604.16548
34. devchaen/memoir — devchaen (primary, 2026-07-14, quality 0.4) — https://github.com/devchaen/memoir
35. guoliangdi/claw-zep — guoliangdi (primary, 2026-06-26, quality 0.4) — https://github.com/guoliangdi/claw-zep
36. ksm26/LLMs-as-Operating-Systems-Agent-Memory — ksm26 (GitHub repository); course by Charles Packer and Sarah Wooders (other, 2025-01-17, quality 0.3) — https://github.com/ksm26/LLMs-as-Operating-Systems-Agent-Memory
37. ruter/zep — Ruter Lyu (GitHub user ruter) (other, 2026-04-14, quality 0.3) — https://github.com/ruter/zep
38. api-evangelist/zep — API Evangelist (Kin Lane) (other, 2026-10-04, quality 0.3) — https://github.com/api-evangelist/zep
