# Evidence — Context Lake: the shared-state layer for multi-agent systems

Generated 2026-10-04 · searched: 174 · candidates: 40 · web_search: False · read: 40 · sources_with_evidence: 33 · claims: 231 · quotes_dropped_as_unverified: 2

## q1. What is a context lake, who coined the term, and how is it defined?

- **[1] The paper defines Governed Enterprise Memory as agent memory designed around a combined scope and presents AkasicMEM as its realization.**
  > We define Governed Enterprise Memory as agent memory designed around this combined scope and present AkasicMEM as its realization.
- **[8] The source lists Xiaowei Jiang as the author of the paper.**
  > Authors:[Xiaowei Jiang](https://arxiv.org/search/cs?searchtype=author&query=Jiang,+X)
- **[8] The paper derives Context Lake as a necessary system class with three requirements: native semantic operations, transactional consistency over all decision-relevant state, and operational envelopes bounding staleness and degradation under load.**
  > From this impossibility result, we derive Context Lake as a necessary system class with three requirements: (1) semantic operations as native capabilities, (2) transactional consistency over all decision-relevant state, and (3) operational envelopes bounding staleness and degradation under load.
- **[32] The article defines a useful context store as having a 'map' component containing business definitions, internal terminology, entity relationships, event taxonomies, product documentation, runbooks, and known failure modes.**
  > A useful context store has two parts.

The first is a **map**: business definitions, internal terminology, entity relationships, event taxonomies, product documentation, runbooks, and known failure modes.

## q2. How does shared context for agents differ from vector databases, data lakes, feature stores and per-agent memory frameworks?

- **[1] Agent memory is intended to let enterprise agents retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge.**
  > Agent memory enables enterprise agents to retain knowledge acquired during work and reuse it across tasks and agents, turning execution experience into persistent organizational knowledge.
- **[1] Shared context for agents requires both source-memory integration, so enterprise sources and accumulated memory can be used together, and memory governance, so shared memory remains subject to organizational policies throughout its lifecycle.**
  > Realizing this potential requires both source--memory integration, through which enterprise sources and accumulated memory can be utilized together, and memory governance, through which shared memory remains subject to organizational policies throughout its lifecycle.
- **[3] The standard paradigm allocates a separate KV cache per agent, while PolyKV writes a compressed cache once and injects it into N independent agent contexts via HuggingFace DynamicCache objects.**
  > Rather than allocating a separate KV cache per agent -- the standard paradigm -- PolyKV writes a compressed cache once and injects it into N independent agent contexts via HuggingFace DynamicCache objects.
- **[4] The paper argues relational and vector models were not built for cue-driven, provenance-weighted recall across long sessions, and proposes treating long-term agent memory as a distinct data model with its own write and read semantics.**
  > The relational model asked which records match a predicate; the vector model asked which vectors lie nearest a query. Neither was built for cue-driven, provenance-weighted recall across long sessions. We propose treating long-term agent memory as a distinct data model -- with its own write semantics (encoding, separation, consolidation, provenance) and read semantics (cue-driven activation across a linked memory graph) -- and present FluctlightDB, an embedded engine that implements this contract via experience() and activate().
- **[5] Graphiti filters invalid_at != null to return Aisha Okonkwo as the valid present CTO.**
  > Graphiti-->>User: Filters invalid_at != null → Returns "Aisha Okonkwo" (Valid Present)
- **[5] Graphiti filters valid_at <= 2020-06-01 to return Leon Müller as the historical CTO fact.**
  > Graphiti-->>User: Filters valid_at <= 2020-06-01 → Returns "Leon Müller" (Historical Fact)
- **[6] Existing agent memory systems rely on heterogeneous vector and graph databases, which fragment memory information and cause high cross-database I/O latency.**
  > Existing agent memory systems rely on heterogeneous vector and graph databases, which fragment memory information and cause high cross-database I/O latency.
- **[6] Mandol uses an agglomerative semantic data structure combining SemanticMap and SemanticGraph that natively fuses key-value, vector, and graph structures and provides unified hybrid retrieval operators to eliminate cross-database I/O.**
  > (2) an agglomerative semantic data structure combining SemanticMap and SemanticGraph, which natively fuses key-value, vector, and graph structures and provides unified hybrid retrieval operators to eliminate cross-database I/O;
- **[8] The paper claims no existing system class satisfies Decision Coherence, and that independently advancing systems cannot be composed to provide it while preserving their native system classes.**
  > We show that no existing system class satisfies this requirement and prove through the Composition Impossibility Theorem that independently advancing systems cannot be composed to provide Decision Coherence while preserving their native system classes.
- **[8] The paper states that traditional data systems designed for human analysis cycles become correctness bottlenecks under the operating regime of AI agents.**
  > Traditional data systems designed for human analysis cycles become correctness bottlenecks under this operating regime.
- **[9] Multi-agent memory should preserve and transfer evidence, role-specific context, decisions, procedures, and experience across interactions, not only outcomes.**
  > Memory must preserve and transfer evidence, role specific context, decisions, procedures, and experience across interactions, not only outcomes.
- **[9] Vector and graph memories flatten multi-agent structures into embeddings or dyadic traces, obscuring events involving agents, tools, documents, errors, and evidence.**
  > Vector and graph memories flatten these structures into embeddings or dyadic traces, obscuring events involving agents, tools, documents, errors, and evidence.
- **[11] Persistent memory has been shown to enhance single-agent performance, but most approaches assume a monolithic, single-user context and overlook knowledge transfer across users under dynamic, asymmetric permissions.**
  > While persistent memory has been shown to enhance single-agent performance, most approaches assume a monolithic, single-user context-overlooking the benefits and challenges of knowledge transfer across users under dynamic, asymmetric permissions.
- **[12] MemMachine is an open-source memory system for personalized AI agents that integrates short-term, long-term episodic, and profile memory, stores entire conversational episodes, and reduces lossy LLM-based extraction.**
  > We present MemMachine, an open-source memory system that integrates short-term, long-term episodic, and profile memory within a ground-truth-preserving architecture that stores entire conversational episodes and reduces lossy LLM-based extraction.
- **[13] Vector databases typically manage metadata as flat scalar attributes, which limits their ability to express hierarchical directory semantics commonly used to organize code repositories, enterprise documents, and agent memories.**
  > Vector databases typically manage metadata as flat scalar attributes, which limits their ability to express hierarchical directory semantics commonly used to organize code repositories, enterprise documents, and agent memories.
- **[13] Directory-scoped retrieval and structural updates in vector databases are often implemented as application-layer workarounds, making recursive scope resolution expensive and directory maintenance difficult to keep consistent.**
  > As a result, directory-scoped retrieval and structural updates are often implemented as application-layer workarounds, making recursive scope resolution expensive and directory maintenance difficult to keep consistent.
- **[14] GENOME claims deterministic bi-temporal belief-state and an MCP server for any client, alongside zero-LLM-call local ingest and Mem0-comparable answer accuracy at much lower ingest cost.**
  > Zero-LLM-call local ingest (~10ms/msg, air-gapped); matches Mem0 on answer accuracy at ~1000x lower ingest cost; deterministic bi-temporal belief-state; MCP server for any client. Honest LoCoMo/LongMemEval benchmarks.
- **[15] Existing vector databases and agent memory frameworks treat memory as passive storage that agents query explicitly, and no system propagates knowledge between agents through the memory layer itself.**
  > Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly. No system propagates knowledge between agents through the memory layer itself.
- **[15] HyphaeDB reinterprets the HNSW graph topology, the core data structure of every modern vector database, not as a search optimization but as a communication fabric for multi-agent AI systems.**
  > We introduce HyphaeDB, an agent-native memory infrastructure that reinterprets the Hierarchical Navigable Small World (HNSW) graph topology the data structure at the core of every modern vector database not as a search optimization, but as a communication fabric for multi-agent AI systems.
- **[22] Existing agentic memory systems generally operate at the individual-user level and restrict the public knowledge that could be shared across users to improve downstream responses.** (also [22])
  > Existing agentic memory systems address this limitation but generally operate at the individual-user level, restricting the public knowledge that could be shared across users to improve downstream responses.
- **[22] AIM classifies information as either private, scoped to one user and inaccessible to others, or public, accessible to all users, and enforces index-level access controls so private memories are retrievable only by their owner.**
  > AIM dynamically classifies information as private, scoped to one user and inaccessible to others, or public, accessible to all users. It enforces index-level access controls so that private memories are retrievable only by their owner, protecting sensitive data while allowing beneficial shared knowledge to improve coordination and consistency.
- **[24] Profile expansion uses substring-matched traversal of entity names in LLM-written profile narratives as a minimal alternative to explicit knowledge-graph construction.**
  > Second, we present Profile-Graph Memory (ProGraph), a two-layer memory architecture combining (i) profile expansion -- substring-matched traversal of entity names that naturally appear in LLM-written profile narratives, a minimal alternative to explicit knowledge-graph construction -- and (ii) compression residuals -- exact dates, quantities, and named items co-extracted with each profile update at zero extra API cost.
- **[25] The paper concludes that representational accuracy is distinct from recall and that human-AI alignment depends on how accurately the user is represented.**
  > We conclude that representational accuracy is distinct from recall and that human-AI alignment is dependent on how accurately the user is represented.
- **[25] The reference implementation compresses a person's data into interpretive patterns that are served as context to a language model.**
  > Our reference implementation aggressively compresses a person's data into interpretive patterns, served as context to a language model.
- **[26] CICL ranks retrieved files, tests, traces, rules, and memories by their expected effect on an agent's next action rather than by semantic similarity alone.**
  > We study decision-aware context selection: ranking retrieved files, tests, traces, rules, and memories by their expected effect on an agent's next action rather than by semantic similarity alone.
- **[26] CICL builds an instance context graph, estimates decision-oriented utility for candidate units, and compresses selected evidence into typed memory cards.**
  > We present the Counterfactual-Inspired Context Layer (CICL), which builds an instance context graph, estimates decision-oriented utility for candidate units, and compresses selected evidence into typed memory cards.
- **[26] The same selection schema can be instantiated with hosted LLM judges, local surrogates, or lightweight rankers, making the selection protocol auditable across model choices.**
  > The same schema can be instantiated with hosted LLM judges, local surrogates, or lightweight rankers, making the selection protocol auditable across model choices.
- **[32] The article argues vector databases can retrieve documents but are weak for joining users to organizations, correlating requests with traces, filtering by deployment, or aggregating behavior across millions of events.**
  > A vector database can retrieve relevant documents, but it is a weak foundation for joining users to organizations, correlating requests with traces, filtering by deployment, or aggregating behavior across millions of events.
- **[32] MCP servers for Postgres and logs expose capabilities but do not create shared identity models, map internal feature names to product events and backend services, or reconcile timestamps, permissions, deployment versions, or conflicting definitions.**
  > An MCP server for Postgres and an MCP server for logs expose two sets of capabilities. They do not create a shared identity model between users in Postgres and sessions in the logs. They do not establish that an internal feature name corresponds to three product events and a particular backend service. They do not reconcile timestamps, permissions, deployment versions, or conflicting definitions.
- **[33] ClawMem is an on-device memory layer for Claude Code, OpenClaw, Hermes, and AI agents, with retrieval-augmented search, hooks, and an MCP server in a single local system, and no API keys or cloud dependencies.**
  > **On-device memory for Claude Code, OpenClaw, Hermes, and AI agents.** Retrieval-augmented search, hooks, and an MCP server in a single local system. No API keys, no cloud dependencies.
- **[33] ClawMem's hybrid architecture combines multi-signal retrieval including BM25, vector search, reciprocal rank fusion, query expansion, and cross-encoder reranking with composite scoring and multi-graph traversal over semantic, temporal, and causal graphs.**
  > The hybrid architecture combines [QMD](https://github.com/tobi/qmd)-derived multi-signal retrieval (BM25 + vector search + reciprocal rank fusion + query expansion + cross-encoder reranking), [SAME](https://github.com/sgx-labs/statelessagent)-inspired composite scoring (recency decay, confidence, content-type half-lives, co-activation reinforcement), [MAGMA](https://arxiv.org/abs/2501.13956)-style intent classification with multi-graph traversal (semantic, temporal, and causal beam search), and [A-MEM](https://arxiv.org/abs/2510.02178) self-evolving memory notes that enrich documents with keywords, tags, and causal links between entries.

## q3. Which systems implement shared or temporal context for agents today, and what do they claim or measure?

- **[1] AkasicMEM implements authorization continuity through transitive lineage, policy composition during memory formation, and policy re-evaluation during retrieval.**
  > AkasicMEM realizes authorization continuity through transitive lineage, policy composition during memory formation, and policy re-evaluation during retrieval.
- **[1] AkasicMEM is built on GraphAI's AkasicDB, a unified vector-graph-relational database whose storage and execution substrate enables joint optimization and execution of the underlying operations.**
  > It is built on GraphAI's AkasicDB, a unified vector--graph--relational database whose storage and execution substrate enables the underlying operations of these mechanisms to be jointly optimized and executed.
- **[2] The repository describes claw-zep as a fully self-hosted temporal knowledge platform built on Graphiti, providing time-aware long-term memory for AI agents, enterprise knowledge bases and risk deduction.**
  > claw-zep is a fully self-hosted temporal knowledge platform built on Graphiti. It provides Palantir-grade dynamic time-series knowledge graph and time-aware long-term memory for AI Agents, enterprise knowledge bases and risk deduction.
- **[2] The initial release describes claw-zep as a private, autonomous temporal knowledge middle platform based on Graphiti kernel extension, benchmarked against Zep and Palantir, with a global dual-time model using valid_from/valid_until/version/source for snapshot/backtracking/conflict resolution, Graphiti scheduling wrapper with LLM extraction and offline heuristic fallback distributing to Kuzu/Chroma/PG, an OpenHuman memory tree three-layer architecture, hybrid retrieval from temporal to vector to graph chain to memory tree weighting, multi-tenant/project isolation/RBAC/audit, and OpenClaw cloud memory plugin plus mobile SDK.**
  > feat: claw-zep 私有化时序知识中台首次发布 基于 Graphiti 内核扩展的私有化、自主可控时序知识中台，对标 Zep + Palantir： - 全局双时序模型（valid_from/valid_until/version/source）：快照/回溯/冲突消解 - Graphiti 调度封装（LLM 抽取 + 离线启发式降级）→ 三库分发（Kuzu/Chroma/PG） - OpenHuman 记忆树三层架构 + Markdown 在线编辑 + Obsidian 导出 - 混合检索（时序→向量→图谱链路→记忆树加权）+ Palantir 因果推演 - 多租户 + 项目隔离 + RBAC（按钮级）+ 全链路审计 - OpenClaw 云端记忆插件 + 龙虾移动端 SDK - React18+TS+AntD5+Cytoscape 全套管理后台 - docker-compose 一键编排（后端/前端/Kuzu/Chroma/PostgreSQL/Redis/MinIO/Celery）
- **[2] A later storage refactor added a single PostgreSQL infrastructure using AGE and pgvector with a STORAGE_BACKEND switch, idempotent initialization of pgvector extension and HNSW vector table plus AGE graph, and changed docker-compose to remove Chroma and use an AGE+pgvector PostgreSQL image with STORAGE_BACKEND=postgres.**
  > refactor(storage): Phase A — 单 PG(AGE+pgvector) 基础设施 + STORAGE_BACKEND 开关 - core/config: 新增 storage_backend(kuzu_chroma|postgres) 开关 + AGE/pgvector 配置 - core/adapters/pg_init: 幂等初始化 pgvector 扩展+向量表(HNSW) 与 AGE 图，缺失自动降级 - main: postgres 后端启动时初始化扩展 - deploy/postgres: AGE+pgvector 的 PG16 镜像(Dockerfile + init SQL)，base tag 可 ARG 覆盖 - docker-compose: 去掉 Chroma 服务，postgres 改用 AGE+pgvector 镜像，STORAGE_BACKEND=postgres - requirements/.env.example: 加 pgvector 与新配置项 旧 kuzu_chroma 后端保留，默认值不变，演进期不破坏现有可运行版本。
- **[2] A worldmonitor integration provides a push SDK and ingest contract, and an end-to-end test with real PostgreSQL pushed 2 records, generated 3 entities with cross-record same-name deduplication, generated 2 relation chains, and passed graph visualization verification.**
  > feat(integration): Phase E — worldmonitor 推送 SDK + 直灌契约文档 - integrations/worldmonitor/claw_ingest_sdk.py：同步推送 SDK， record/entity/relation 构造 helper + 自动分批 + whoami 校验 - docs/INGEST_CONTRACT.md：bulk 契约(鉴权/字段语义/时序/批量/一致性) + worldmonitor 侧改造建议(抽取模板 + material_suppliers/signals 映射) + SDK 示例 端到端验证(真 PG)：SDK→运行中后端→server PG，推 2 records 生成 3 实体(跨 record 同名去重)+2 关系链路，graph 可视化校验 PASS。
- **[2] A governance/operations phase added per-tenant Redis fixed-window rate limiting returning 429 when exceeded and fail-open if Redis is unavailable, verified with 7 requests against a limit of 5 resulting in 5 allowed and 2 rejected, plus metrics, deep readiness checks, backup scripts, and entity attribute persistence.**
  > feat(ops): Phase G — 限流 + 可观测 + 备份 + 实体属性持久化 - 限流中间件(api/middlewares/ratelimit)：per-tenant Redis 固定窗口，超限 429， Redis 不可用 fail-open。真 Redis 验证：7 请求@限5 → 5 放行 2 拒绝 - 可观测：MetricsMiddleware + /metrics(Prometheus 文本) + /health/ready 深度就绪检查 (postgres/redis/pgvector/age) - 备份：scripts/backup.sh(pg_dump 全库含 AGE+pgvector + 对象存储 + 保留期) - 补 Phase F 缺口：实体 attributes 持久化(GraphEntityMeta.attributes_json)， 贯通 orchestrator/bulk/可视化。demo risk_level 现可查可视(high/medium 显示在材料节点) - docs/OPERATIONS.md 运维手册 真 PG 验证：/health/ready 全绿、/metrics 正常、限流强制、attributes 入图谱可视化。
- **[3] PolyKV is a system where multiple concurrent inference agents share one asymmetrically compressed KV cache pool.**
  > We present PolyKV, a system in which multiple concurrent inference agents share a single, asymmetrically compressed KV cache pool.
- **[3] PolyKV uses asymmetric compression: keys are int8-quantized q8_0 to preserve softmax stability, while values use TurboQuant MSE with FWHT rotation followed by 3-bit Lloyd-Max quantization with centroids tuned to N(0,1).**
  > Compression is asymmetric: Keys are quantized at int8 (q8_0) to preserve softmax stability, while Values are compressed using TurboQuant MSE -- a Fast Walsh-Hadamard Transform (FWHT) rotation followed by 3-bit Lloyd-Max quantization with centroids tuned to N(0,1).
- **[3] PolyKV was evaluated across two model scales, SmolLM2-1.7B-Instruct and Llama-3-8B-Instruct, three context lengths from 600 to 7,194 tokens, and up to 15 concurrent agents.**
  > We evaluate across two model scales (SmolLM2-1.7B-Instruct and Llama-3-8B-Instruct), three context lengths (600-7,194 tokens), and up to 15 concurrent agents.
- **[3] PolyKV reports a stable 2.91x compression ratio across all configurations.**
  > PolyKV achieves a stable 2.91x compression ratio across all configurations.
- **[3] On Llama-3-8B with 15 agents sharing a 4K-token context, PolyKV reduces KV cache memory from 19.8 GB to 0.45 GB, a 97.7% reduction, with +0.57% perplexity degradation and mean BERTScore F1 of 0.928.**
  > On Llama-3-8B with 15 agents sharing a 4K-token context, PolyKV reduces KV cache memory from 19.8 GB to 0.45 GB -- a 97.7% reduction -- while maintaining only +0.57% perplexity degradation and a mean BERTScore F1 of 0.928.
- **[3] PolyKV reports that PPL delta does not grow with agent count and improves as context length increases, becoming -0.26% at 1,851 coherent tokens.**
  > PPL delta does not grow with agent count and improves as context length increases, inverting to -0.26% at 1,851 coherent tokens.
- **[4] The authors say FluctlightDB does not claim novelty over Mem0, Zep, or HippoRAG-style memory layers, positioning it as an embedded engine contract beneath them.**
  > We do not claim novelty over Mem0, Zep, or HippoRAG-style memory layers, only an embedded engine contract beneath them.
- **[4] On LoCoMo, the native-Rust CHORUS stack reaches 96.8% at k=150 for raw evidence recall, 72.6% at k=5, and 85% end-to-end QA at k=15 on date-stamped context.**
  > On LoCoMo (official evidence-recall; 10 conversations, 1,982 gold spans), our native-Rust CHORUS stack reaches 96.8% at k=150 as raw evidence recall with no neighbor expansion, on an internally reproduced July 2026 run; at k=5 it still yields 72.6%, while end-to-end QA over date-stamped context reaches 85% at k=15 (retrieval-bound).
- **[4] On LongMemEval-S, official session_recall@8 is 97.6% (488/500) and end-to-end QA with the reader/judge stack is 97.4% (487/500).**
  > On LongMemEval-S (500 questions), official session_recall@8 is 97.6% (488/500) and end-to-end QA with our reader/judge stack is 97.4% (487/500) -- different protocols from vendor leaderboard figures we cite for context only.
- **[4] On BEIR SciFact, CHORUS/PRISM edges Chroma on nDCG@10 (0.646 vs. 0.645) and Recall@10 (0.792 vs. 0.783).**
  > On BEIR SciFact (shared MiniLM embeddings, same harness), CHORUS/PRISM edges Chroma on nDCG@10 (0.646 vs. 0.645) and Recall@10 (0.792 vs. 0.783).
- **[5] The repository describes itself as a temporal knowledge graph agent using Graphiti (Zep) + LangGraph + Gemini for context, perception and decision for AI agents.**
  > Temporal knowledge graph agent using Graphiti (Zep) + LangGraph + Gemini — context, perception and decision for AI agents
- **[5] The source positions its temporal knowledge graph for AI agents as covering context, perception and memory.**
  > 🧠 TEMPORAL KNOWLEDGE GRAPH FOR AI AGENTS (CONTEXT | PERCEPTION | MEMORY)
- **[5] A commit message says the project implements a local Graphiti zero-cost temporal KG stack with Ollama, Neo4j, and LangGraph agent memory.**
  > docs & core: implement local Graphiti zero-cost temporal KG stack with Ollama, Neo4j, and LangGraph agent memory; add rich visual README
- **[6] Mandol is proposed as an agglomerative memory system that consolidates fragmented memory representations and storage into a unified memory-native architecture.**
  > We propose Mandol, an agglomerative memory system that consolidates fragmented memory representations and storage into a unified memory-native architecture.
- **[6] Mandol uses a hierarchical memory model with a basic layer for raw memory information and a high-level abstract layer that agglomerates basic memories into traceable abstract memories, both represented as structured semantic graphs.**
  > Its core components include: (1) a hierarchical memory model that organizes memory into a basic layer representing raw memory information and a high-level abstract layer that agglomerates basic memories into traceable abstract memories, both uniformly represented as structured semantic graphs;
- **[6] Mandol includes a quantitative query mechanism with query-adaptive routing, quantitative denoising and conflict resolution, and token-constrained context generation, all without involving LLMs during retrieval.**
  > (3) a quantitative query mechanism with query-adaptive routing, quantitative denoising and conflict resolution, and token-constrained context generation, all without involving LLMs during retrieval.
- **[6] Experiments on LoCoMo and LongMemEval show that Mandol achieves the best overall accuracy among representative agent memory systems.**
  > Experiments on two widely used long-term conversation benchmarks, LoCoMo and LongMemEval, show that Mandol achieves the best overall accuracy among representative agent memory systems.
- **[6] Mandol obtains a 5.4x retrieval speedup and a 4.8x insertion speedup under 10 QPS concurrent load while maintaining low latency on consumer-grade hardware.**
  > For performance comparison, Mandol also obtains a 5.4x retrieval speedup and a 4.8x insertion speedup under 10 QPS concurrent load, while still maintaining low latency on consumer-grade hardware.
- **[7] ConsistWorld is a multi-agent world model that generates camera-controlled video streams of a static scene from one shared image.**
  > We present ConsistWorld, a multi-agent world model that generates camera-controlled video streams of a static scene from one shared image.
- **[7] ConsistWorld formulates consistency as routing evidence from committed multi-agent history and concurrently generated peer views to the tokens being generated.**
  > We formulate consistency as routing evidence from committed multi-agent history and concurrently generated peer views to the tokens being generated.
- **[7] Pose Conditioned Memory Retrieval selects relevant historical observations from all agents, recovering evidence beyond the recent context window.**
  > Pose Conditioned Memory Retrieval selects relevant historical observations from all agents, recovering evidence beyond the recent context window.
- **[7] Visibility-Gated Peer Sharing regulates current peer information according to estimated historical coverage and current-view overlap.**
  > Visibility-Gated Peer Sharing regulates current peer information according to estimated historical coverage and current-view overlap.
- **[7] The two mechanisms determine which historical observations enter the context and where concurrent peer information contributes, supporting long-term recall and coordinated exploration.**
  > Together, they determine which historical observations enter the context and where concurrent peer information contributes, supporting long-term recall and coordinated exploration.
- **[7] Both mechanisms use camera geometry and maintain a bounded active context for a fixed agent count and retrieval budget.**
  > Both mechanisms use camera geometry and maintain a bounded active context for a fixed agent count and retrieval budget.
- **[7] Experiments on evidence sharing cases and generalization across video length and agent number show ConsistWorld achieves strong cross-time and cross-agent consistency while preserving competitive generation quality.**
  > Experiments on evidence sharing cases and video length and agent number generalizations show that ConsistWorld achieves a strong cross-time and cross-agent consistency while preserving competitive generation quality.
- **[9] MAGE is presented as a hypergraph-based multimodal database designed as a memory engine for multi-agent systems.**
  > We present MAGE, a hypergraph based multimodal database designed as a memory engine for MAS.
- **[9] MAGE stores agents, messages, tools, errors, procedures, documents, entities, decisions, and evidence in a heterogeneous temporal hypergraph, preserving high-order collaborative events as reusable memory.**
  > MAGE stores agents, messages, tools, errors, procedures, documents, entities, decisions, and evidence in a heterogeneous temporal hypergraph, preserving high order collaborative events as reusable memory.
- **[9] MAGE supports decision-driven updates, role-aware retrieval, validation, lifecycle management, and budget-bounded context packing.**
  > It supports decision driven updates, role aware retrieval, validation, lifecycle management, and budget bounded context packing.
- **[9] Experiments claim MAGE outperforms various memory baselines.**
  > Experiments show MAGE outperforms on various memory baselines.
- **[10] L9 Graphiti Memory is described as a bi-temporal knowledge graph memory subsystem for autonomous agents using Zep Cloud transport.**
  > L9 Graphiti Memory — bi-temporal knowledge graph memory subsystem for autonomous agents (Zep Cloud transport)
- **[10] The system provides MemoryService.rebuild_projection and l9-memory rebuild-projection to re-project active records with no live link, dry run by default, without touching canonical state.**
  > Add MemoryService.rebuild_projection and l9-memory rebuild-projection, re-projecting active records with no live link. MAINTAIN to apply, dry run by default, never touches canonical state.
- **[10] Graphiti exposes no deactivation primitive, so retire and erase both call delete_episode.**
  > Graphiti exposes no deactivation primitive, so retire and erase both call delete_episode.
- **[10] ProjectionAdapter.retirement_mode is NATIVE or WITHDRAW; Graphiti is WITHDRAW and NullProjection is NATIVE.**
  > ProjectionAdapter.retirement_mode is NATIVE or WITHDRAW. Graphiti is WITHDRAW, NullProjection is NATIVE.
- **[10] The project reports validation evidence including 1059 tests passed, 16 skipped, 24 local checks, and an identical candidate digest before and after.**
  > Validation: pytest 1059 passed / 16 skipped (CI shape); ruff check clean; mypy src/l9_graphite_memory clean; bash scripts/validate_release.sh self-contained: 24 local checks evidenced, candidate digest identical before and after (016a3df9…).
- **[11] The paper introduces Collaborative Memory, a framework for multi-user, multi-agent environments with asymmetric, time-evolving access controls encoded as bipartite graphs linking users, agents, and resources.**
  > We introduce Collaborative Memory, a framework for multi-user, multi-agent environments with asymmetric, time-evolving access controls encoded as bipartite graphs linking users, agents, and resources.
- **[11] The system maintains two memory tiers: private memory visible only to the originating user, and shared memory with selectively shared fragments.**
  > Our system maintains two memory tiers: (1) private memory-private fragments visible only to their originating user; and (2) shared memory-selectively shared fragments.
- **[11] Each memory fragment carries immutable provenance attributes, including contributing agents, accessed resources, and timestamps, to support retrospective permission checks.**
  > Each fragment carries immutable provenance attributes (contributing agents, accessed resources, and timestamps) to support retrospective permission checks.
- **[11] Granular read policies enforce current user-agent-resource constraints and project existing memory fragments into filtered transformed views.**
  > Granular read policies enforce current user-agent-resource constraints and project existing memory fragments into filtered transformed views.
- **[11] Write policies determine fragment retention and sharing, applying context-aware transformations to update the memory.**
  > Write policies determine fragment retention and sharing, applying context-aware transformations to update the memory.
- **[11] The read and write policies may be designed conditioned on system, agent, and user-level information.**
  > Both policies may be designed conditioned on system, agent, and user-level information.
- **[12] MemMachine uses contextualized retrieval that expands nucleus matches with surrounding context to improve recall when relevant evidence spans multiple dialogue turns.**
  > MemMachine uses contextualized retrieval that expands nucleus matches with surrounding context, improving recall when relevant evidence spans multiple dialogue turns.
- **[12] MemMachine reaches 0.9169 on LoCoMo using gpt4.1-mini and 93.0 percent accuracy on LongMemEvalS, with retrieval-stage optimizations outperforming ingestion-stage gains.**
  > Across benchmarks, MemMachine achieves strong accuracy-efficiency tradeoffs: on LoCoMo it reaches 0.9169 using gpt4.1-mini; on LongMemEvalS (ICLR 2025), a six-dimension ablation yields 93.0 percent accuracy, with retrieval-stage optimizations -- retrieval depth tuning (+4.2 percent), context formatting (+2.0 percent), search prompt design (+1.8 percent), and query bias correction (+1.4 percent) -- outperforming ingestion-stage gains such as sentence chunking (+0.8 percent).
- **[12] GPT-5-mini exceeds GPT-5 by 2.6 percent when paired with optimized prompts, making it the most cost-efficient setup.**
  > GPT-5-mini exceeds GPT-5 by 2.6 percent when paired with optimized prompts, making it the most cost-efficient setup.
- **[12] A companion Retrieval Agent adaptively routes queries among direct retrieval, parallel decomposition, or iterative chain-of-query strategies, achieving 93.2 percent on HotpotQA-hard and 92.6 percent on WikiMultiHop under randomized-noise conditions.**
  > A companion Retrieval Agent adaptively routes queries among direct retrieval, parallel decomposition, or iterative chain-of-query strategies, achieving 93.2 percent on HotpotQA-hard and 92.6 percent on WikiMultiHop under randomized-noise conditions.
- **[13] The paper formalizes two core operators: Directory-Semantic Query (DSQ) for hierarchically scoped retrieval, and Directory-Semantic Maintenance (DSM) for structural updates.**
  > We formalize two core operators: Directory-Semantic Query (DSQ) for hierarchically scoped retrieval, and Directory-Semantic Maintenance (DSM) for structural updates.
- **[13] The paper evaluates three implementation strategies: query-time path expansion (PE-Online), ingestion-time path expansion (PE-Offline), and a Trie-based Hierarchical Index (TrieHI).**
  > We then evaluate three implementation strategies: query-time path expansion (PE-Online), ingestion-time path expansion (PE-Offline), and a Trie-based Hierarchical Index (TrieHI).
- **[13] The analysis exposes fundamental limitations of expansion-based designs: flattening the hierarchy incurs high recursive-query latency in PE-Online and unscalable write amplification during structural changes in both expansion strategies.**
  > Our analysis exposes the fundamental limitations of expansion-based designs: flattening the hierarchy incurs high recursive-query latency in PE-Online and unscalable write amplification during structural changes in both expansion strategies.
- **[13] TrieHI keeps the directory topology as a native prefix tree, enabling efficient recursive retrieval through tree traversal and reducing maintenance cost through topological node manipulation.**
  > In contrast, TrieHI keeps the directory topology as a native prefix tree, enabling efficient recursive retrieval through tree traversal and reducing maintenance cost through topological node manipulation.
- **[13] The paper benchmarks these design points within ByteDance's Viking vector search engine and releases two large-scale datasets, WIKI-Dir and ARXIV-Dir, to support future research on directory-semantic vector search.**
  > We benchmark these design points within ByteDance's Viking vector search engine and release two large-scale datasets, WIKI-Dir and ARXIV-Dir, to support future research on directory-semantic vector search.
- **[13] TrieHI has been integrated into OpenViking, an open-source context database for AI agents, where it supports filesystem-style context organization and directory-recursive retrieval.**
  > Finally, TrieHI has been integrated into OpenViking, an open-source context database for AI agents, where it supports filesystem-style context organization and directory-recursive retrieval.
- **[14] GENOME is an auditable memory layer for AI agents with zero-LLM-call local ingest at about 10ms per message, air-gapped operation, accuracy matching Mem0 at about 1000x lower ingest cost, bi-temporal belief-state, an MCP server, LoCoMo/LongMemEval benchmarks, and an Apache-2.0 open-source license.**
  > Title: GitHub - NORTHTEKDevs/genome: Auditable memory layer for AI agents: zero-LLM-call local ingest (~10ms/msg, air-gapped), matches Mem0 on accuracy at ~1000x lower ingest cost, bi-temporal belief-state, MCP server. Honest LoCoMo/LongMemEval benchmarks. Open source (Apache-2.0).
- **[15] In HyphaeDB, agents are nodes in vector space with persistent positions; knowledge propagates via a gossip protocol through the graph's neighbor structure with energy-based attenuation; emergent behaviors include contradiction detection, pattern crystallization, and consensus formation.**
  > In HyphaeDB, agents are nodes in the vector space with persistent positions, knowledge propagates via a gossip protocol through the graph's neighbor structure with energy-based attenuation, and emergent behaviors contradiction detection, pattern crystallization, and consensus formation arise from the combination of topology, propagation dynamics, and local interaction rules.
- **[15] The HyphaeDB architecture is built on three primitives: knowledge nodes, topology edges, and memory diffs, with a multi-layer abstraction hierarchy and promotion via emergent consensus.**
  > We present the architecture built on three primitives (knowledge nodes, topology edges, and memory diffs), a multi-layer abstraction hierarchy with promotion via emergent consensus, and theoretical analysis grounding the system in small-world network theory, epidemic broadcast protocols, and swarm intelligence.
- **[15] HyphaeDB provides a reference implementation on PostgreSQL with pgvector and describes a concrete deployment in Swarm-Driven Development, a multi-agent software engineering methodology.**
  > We provide a reference implementation on PostgreSQL with pgvector and describe a concrete deployment in Swarm-Driven Development, a multi-agent software engineering methodology.
- **[15] The authors claim HyphaeDB is the first system to combine navigable small world topology with gossip-based knowledge propagation for multi-agent coordination.**
  > HyphaeDB represents, to our knowledge, the first system to combine navigable small world topology with gossip-based knowledge propagation for multi-agent coordination.
- **[16] The paper provides basic experimental validation of key mechanisms, demonstrating the effectiveness of LSS.**
  > We provide basic experimental validation of key mechanisms, demonstrating the effectiveness of LSS.
- **[17] The paper proposes Distributed Sentinel, a distributed zero-trust enforcement architecture using a Semantic Taint Token (STT) Protocol and lightweight sidecar proxies to propagate security state across organizational boundaries without exposing raw cross-domain data, enabling Counterfactual Graph Simulation for cross-domain policy verification.**
  > We propose Distributed Sentinel, a distributed zero-trust enforcement architecture that introduces the Semantic Taint Token (STT) Protocol. Through lightweight sidecar proxies, our system propagates security state across organizational boundaries without exposing raw cross-domain data, enabling Counterfactual Graph Simulation for cross-domain policy verification.
- **[17] The authors construct PhantomEcosystem, a benchmark with 9 categories of realistic cross-agent violation scenarios and adversarially balanced safe controls.**
  > We construct PhantomEcosystem, a comprehensive benchmark comprising 9 categories of realistic cross-agent violation scenarios with adversarially balanced safe controls.
- **[17] On the PhantomEcosystem benchmark, Distributed Sentinel achieves F1 = 0.95 with 106ms end-to-end latency, 16ms verification and 90ms entity extraction on A100, compared to 0.85 F1 for prompt-based filtering and 0.65 for rule-based DLP.**
  > On this benchmark, Distributed Sentinel achieves F1 = 0.95 with 106ms end-to-end latency (16ms verification + 90ms entity extraction on A100), compared to 0.85 F1 for prompt-based filtering and 0.65 for rule-based DLP.
- **[19] VerifyMAS is a hypothesis verification framework for agent failure attribution that formulates and verifies failure hypotheses against full trajectories rather than directly predicting faulty agents and error types.**
  > To address these challenges, we propose VerifyMAS, a hypothesis verification framework for agent failure attribution. Instead of directly predicting faulty agents and error types, VerifyMAS formulates and verifies failure hypotheses against full trajectories.
- **[19] VerifyMAS decomposes attribution into trajectory-level error validation and fine-grained agent localization, capturing global failure patterns while reducing the search space.**
  > This verification-based approach decomposes attribution into trajectory-level error validation and fine-grained agent localization, providing an error-first attribution approach that captures global failure patterns while substantially reducing the search space.
- **[19] VerifyMAS uses a hypothesis-based data construction strategy grounded in a structured error taxonomy and fine-tunes a specialized LLM verifier for trajectory-level failure verification and agent attribution.**
  > We further introduce a hypothesis-based data construction strategy grounded in a structured error taxonomy and fine-tune a specialized LLM verifier model for trajectory-level failure verification and agent attribution.
- **[19] Experiments on Aegis-Bench and Who&When show VerifyMAS improves diverse backbone models, including open-source Qwen and API-based GPT models, outperforming prior methods without sacrificing inference efficiency for long multi-agent trajectories.**
  > Experiments on Aegis-Bench and Who&When show that VerifyMAS consistently improves diverse backbone models, including open-source Qwen and API-based GPT models, outperforming prior methods without sacrificing inference efficiency for long multi-agent trajectories.
- **[20] The paper introduces ConstraintRot, a benchmark of long-horizon agent scenarios with deterministic tool-call grading, and measures compaction-induced violations across seven model families.**
  > We introduce ConstraintRot, a benchmark of long-horizon agent scenarios with deterministic tool-call grading, and measure compaction-induced violations across seven model families.
- **[21] SagaLLM integrates the Saga transactional pattern with persistent memory, automated compensation, and independent validation agents.**
  > SagaLLM bridges this gap by integrating the Saga transactional pattern with persistent memory, automated compensation, and independent validation agents.
- **[21] SagaLLM claims significant improvements in consistency, validation accuracy, and adaptive coordination under uncertainty.**
  > In contrast, SagaLLM achieves significant improvements in consistency, validation accuracy, and adaptive coordination under uncertainty, establishing a robust foundation for real-world, scalable LLM-based multi-agent systems.
- **[21] SagaLLM uses LLM generative reasoning to automate state tracking, dependency analysis, log schema generation, and recovery orchestration.**
  > It leverages LLMs' generative reasoning to automate key tasks traditionally requiring hand-coded coordination logic, including state tracking, dependency analysis, log schema generation, and recovery orchestration.
- **[22] AIM is a unified, privacy-aware memory framework that enables multi-agent, multi-user LLM systems to persistently manage private and shared memory.**
  > We introduce AIM (Agentic Interoperable Memory), a unified, privacy-aware memory framework that enables multi-agent, multi-user LLM systems to persistently manage private and shared memory.
- **[22] MUMBench is a dataset of multi-user interactions containing private and shareable information across four domains, and the authors describe it as the first public dataset designed to evaluate retrieval, creation, update, and deletion in a multi-user environment.**
  > We also introduce MUMBench (Multi-User Memory Benchmark), a dataset of multi-user interactions containing private and shareable information across four domains. To our knowledge, MUMBench is the first public dataset designed to evaluate multiple memory operations, including retrieval, creation, update, and deletion, in a multi-user environment.
- **[22] Across three independent runs on MUMBench, AIM achieves 96.0% visibility classification accuracy, 58.8% strict operation accuracy, and 70.5% state-aware operation accuracy.**
  > Across three independent runs on MUMBench, AIM achieves 96.0% visibility classification accuracy, 58.8% strict operation accuracy, and 70.5% state-aware operation accuracy.
- **[23] ACE is proposed as a plug-and-play module that elastically orchestrates historical step information into the agent's context at each decision step.**
  > To address these limitations, we propose the Adaptive Context Elasticizer (ACE), a plug-and-play module that elastically orchestrates historical step information into the agent's context at each decision step.
- **[23] ACE uses a lossless message maintenance layer storing raw messages and compressed abstractions for each historical step, plus a context orchestration layer that assigns each step an elastic type of raw, abstract, or drop based on the current task state.**
  > ACE maintains a lossless message maintenance layer that stores both raw messages and compressed abstractions for each historical step, while a context orchestration layer adaptively assigns each step an elastic type as raw, abstract, or drop, at every decision step based on the current task state.
- **[23] ACE's reversible design is intended to ensure the main LLM always receives a compact yet information-rich context.**
  > This reversible design ensures that the main LLM always receives a compact yet information-rich context.
- **[23] ACE was adapted to four agent frameworks—ReAct, DeepAgent, WebThinker, and MiroFlow—without training or architectural modifications.**
  > We adapt ACE to four diverse agent frameworks, including ReAct, DeepAgent, WebThinker, and MiroFlow, without training or architectural modifications.
- **[23] The paper reports that ACE consistently outperforms truncation and summarization baselines and brings consistent performance gains across all four agent frameworks.**
  > Experiments show that ACE consistently outperforms truncation and summarization baselines, and brings consistent performance gains across all four agent frameworks.
- **[24] ProGraph is a two-layer memory architecture for LLM agents that combines profile expansion and compression residuals.**
  > Second, we present Profile-Graph Memory (ProGraph), a two-layer memory architecture combining (i) profile expansion -- substring-matched traversal of entity names that naturally appear in LLM-written profile narratives, a minimal alternative to explicit knowledge-graph construction -- and (ii) compression residuals -- exact dates, quantities, and named items co-extracted with each profile update at zero extra API cost.
- **[24] ProGraph averages 80.1% on MemHop and 78.4% on LoCoMo, exceeding FullContext by 11.3 percentage points on LoCoMo and outperforming Mem0, A-Mem, HippoRAG, and RAG on both benchmarks.**
  > ProGraph averages 80.1% on MemHop (matching the FullContext reference) and 78.4% on LoCoMo (exceeding FullContext by 11.3pp), outperforming Mem0, A-Mem, HippoRAG, and RAG on both.
- **[24] Removing profile expansion reduces MemHop performance by 22.6 percentage points, not co-extracting compression residuals reduces LoCoMo precision recall by 8.6 percentage points, and cross-effects are under 3 percentage points.**
  > Third, a full-grid ablation shows cross-benchmark mechanism specialization: profile expansion drives multi-hop reasoning (-22.6pp on MemHop when removed) while compression residuals drive precision recall (-8.6pp on LoCoMo when not co-extracted), with cross-effects under 3pp within a single architecture.
- **[24] MemHop is a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios with per-hop evidence annotations.**
  > First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations.
- **[25] The paper evaluates a Behavioral Specification alongside full raw corpus, full extracted facts, and four commercial memory systems: Mem0, Letta, Supermemory, and Zep.**
  > We test it independently and in composition with a range of context conditions: full raw corpus, full extracted facts, and four commercial memory systems (Mem0, Letta, Supermemory, Zep).
- **[25] Across 14 public-domain autobiographical corpora, the Specification lifted representational accuracy in aggregate and nearly eliminated model hedging.**
  > Across 14 public-domain autobiographical corpora, the Specification lifts representational accuracy in aggregate and nearly eliminates model hedging.
- **[25] The Specification recovers most of what the raw corpus delivers at about 25 times less context cost.**
  > It recovers most of what the raw corpus delivers, at ~25x less context cost.
- **[25] The lift is greatest on interpretation-required questions, where an interpretive layer enables model behavior that extracted facts or raw corpus do not.**
  > Lift is greatest on interpretation-required questions, where providing an interpretive layer enables model behavior that extracted facts or raw corpus do not.
- **[26] On 50 SWE-bench Verified file-retrieval instances, Qwen3.6-Plus reranking of BM25 top-50 candidates improves hit@1 from 0.58 to 0.78 and MRR@10 from 0.634 to 0.790, with all 2,500 judgments parseable.**
  > On 50 SWE-bench Verified file-retrieval instances, Qwen3.6-Plus reranking of BM25 top-50 candidates improves hit@1 from 0.58 to 0.78 and MRR@10 from 0.634 to 0.790, with all 2,500 judgments parseable.
- **[26] In selected-then-compressed mode, memory cards save 44.93 tokens per query while preserving selected evidence.**
  > In selected-then-compressed mode, memory cards save 44.93 tokens per query while preserving selected evidence.
- **[27] AgenticRepair orchestrates three specialized LLM subagents to engineer contexts, which are then embedded into the memory of a dedicated repair subagent for context-conditioned patch synthesis.**
  > AgenticRepair orchestrates three specialized LLM subagents to engineer the contexts, which are then embedded into the memory of a dedicated repair subagent for context-conditioned patch synthesis.
- **[27] Evaluated on SEC-Bench with 300 real-world instances and sanitizer-based patch verification, AgenticRepair achieves a 73% success rate and outperforms the strongest baseline by 29%.**
  > Evaluated on SEC-Bench comprising 300 real-world instances with sanitizer-based patch verification, AgenticRepair achieves a 73% success rate, substantially outperforming the strongest baseline by 29%.
- **[30] HyMem is a hierarchical framework that separates an agent's context into distinct functional layers, organizing context by function to separate high-level planning from execution and complex analysis.**
  > To address this challenge, we propose HyMem, a hierarchical framework that explicitly separates the agent's context into distinct functional layers. HyMem organizes context by function to separate high-level planning from execution and complex analysis.
- **[30] HyMem uses an isolated reasoning module that handles complex subtasks without adding intermediate reasoning traces to the persistent planning context, and a memory management module that preserves task progress across context refreshes through structured summaries.**
  > Its isolated reasoning module handles complex subtasks without adding intermediate reasoning traces to the persistent planning context, while its memory management module preserves task progress across context refreshes through structured summaries.
- **[30] On GAIA and Browsecomp-plus with DeepSeek-V4, HyMem achieves average Pass@1 scores of 66.7% and 61.3%, outperforming the strongest baseline by 6.1 and 4.7 percentage points, respectively.**
  > Experiments on GAIA and Browsecomp-plus show that, with DeepSeek-V4, HyMem achieves average Pass@1 scores of 66.7% and 61.3%, outperforming the strongest baseline by 6.1 and 4.7 percentage points, respectively.
- **[32] Altertable says its production context store connects to Postgres, ingests logs/traces and product events, and uploads company knowledge such as product documentation, internal definitions, runbooks, and interpretive context.**
  > Our production Postgres database is connected to Altertable. Logs and traces are ingested into it. Product events land there too. We also upload company knowledge: product documentation, internal definitions, runbooks, and the context our team uses to interpret what the data means.
- **[32] Altertable's agent, accessible through Ask Agent and a Slack bot, starts with a shared, queryable picture of the business rather than a collection of disconnected tools.**
  > The agent is accessible through our "Ask Agent" feature and a Slack bot, but the chat surface is the least interesting part. What matters is that the agent does not begin with a collection of disconnected tools. It begins with a shared, queryable picture of the business.
- **[33] ClawMem routes all integration paths to the same local SQLite vault, so a decision captured in a Claude Code session is immediately available when an OpenClaw or Hermes agent picks up the same project.**
  > All paths write to the same local SQLite vault. A decision captured during a Claude Code session shows up immediately when an OpenClaw or Hermes agent picks up the same project.
- **[33] ClawMem preserves authorship time so ranking recency and temporal queries run on when content was actually written, not when it was mined, and includes a metadata-only backfill-dates lane for earlier vaults.**
  > Imports preserve **authorship time** (v0.27.0): ranking recency and temporal queries run on when content was actually written, so historical conversations mined today don't rank as fresh — with a metadata-only `--backfill-dates` lane for vaults mined earlier

## q4. What failures in multi-agent systems come from inconsistent or missing shared context, and what is the evidence?

- **[1] When enterprise-source information persists in memory, repeated derivation and reuse under changing principals and policies can bypass source restrictions and result in information leakage.**
  > These requirements interact when information from enterprise sources persists in memory. As this information is repeatedly derived and reused under changing principals and policies, source restrictions may be bypassed, resulting in information leakage.
- **[1] Preventing leakage requires authorization continuity, in which source restrictions remain effective throughout source-to-memory and memory-to-memory derivation and reuse.**
  > Preventing such leakage requires authorization continuity, under which source restrictions remain effective throughout source-to-memory and memory-to-memory derivation and reuse.
- **[4] A graded provenance-conflict suite with n=50 scores 18% top-1 when all pairs share one brain, versus 100% under per-case isolation, which the authors label a ceiling rather than deployment evidence.**
  > A graded provenance-conflict suite (n=50) scores 18% top-1 when all pairs share one brain versus 100% under per-case isolation (ceiling, not deployment evidence).
- **[5] In the source's Vector RAG comparison, a query for the current CTO of NovaTech returns a 2018 chunk (Leon) and a 2022 chunk (Aisha), causing LLM confusion.**
  > VectorRAG-->>User: Returns 2018 chunk (Leon) & 2022 chunk (Aisha) → LLM Confused!
- **[6] Common RAG-style retrieval methods tend to introduce noise, miss correlated clues, and lack token budget control, degrading LLM accuracy and efficiency.**
  > For retrieval, common RAG-style methods tend to introduce noise, miss correlated clues, and lack token budget control, degrading LLM accuracy and efficiency.
- **[7] Extending autoregressive video world models to multiple agents requires consistency across independently controlled views and temporal gaps under causal streaming.**
  > Extending them to multiple agents requires consistency across independently controlled views and temporal gaps under causal streaming.
- **[8] The paper states that when multiple agents operate over shared resources, their actions interact before reconciliation is possible, and post-decision correctness guarantees fail to prevent conflicts.**
  > When multiple agents operate over shared resources, their actions interact before reconciliation is possible. Correctness guarantees that apply after the decision window therefore fail to prevent conflicts.
- **[8] The paper states that AI agents are increasingly the primary consumers of data, operating continuously to make concurrent, irreversible decisions.**
  > AI agents are increasingly the primary consumers of data, operating continuously to make concurrent, irreversible decisions.
- **[9] Vector and graph memory flattening limits knowledge sharing, tracing, reuse, revision, and orchestration in multi-agent systems.**
  > This limits knowledge sharing, tracing, reuse, revision, and orchestration.
- **[9] Each agent in a multi-agent system operates within a knowledge boundary defined by its observations, context, and resources.**
  > Multi-agent systems solve tasks through collaboration, tool use, multimodal reasoning, and orchestration, but each agent operates within a knowledge boundary defined by its observations, context, and resources.
- **[10] Changing store_backend to a different store can initialize cleanly, report healthy, hold zero records, and make prior data invisible; adopting the shared backend can yield a green health check over an empty namespace.**
  > changing store_backend points at a different store, which initializes clean, reports healthy, and holds zero records. Nothing is destroyed, but the running system cannot see the prior data. An operator adopting the shared backend gets a green health check over an empty namespace.
- **[10] If governance reversed an archive decision, the record returned to ACTIVE in canonical state while remaining invisible to projection-backed search.**
  > If governance reversed an archive decision the record returned to ACTIVE in canonical state while staying invisible to projection-backed search.
- **[12] The paper states that LLM agents require persistent memory for personalization, factual continuity, and long-horizon reasoning, but standard context-window and RAG pipelines degrade over multi-session interactions.**
  > Large Language Model (LLM) agents require persistent memory to maintain personalization, factual continuity, and long-horizon reasoning, yet standard context-window and retrieval-augmented generation (RAG) pipelines degrade over multi-session interactions.
- **[14] A past ScopeEpochs bug caused any tenant's write to invalidate every other tenant's cached query, breaking the cache in the multi-tenant workload it was built for.**
  > ScopeEpochs bumped a global counter on every mutation and folded it into every scoped lookup, so any tenant's write invalidated every other tenant's cached query. The cache stopped working in exactly the multi-tenant workload the per-scope epoch was built for.
- **[14] GENOME's MCP forget operation previously had no relevance floor, so any query deleted its nearest neighbour; it now uses min_score with a default 0.5 cosine threshold and refuses below it.**
  > - MCP forget: Memory.search has no relevance floor, so any query deleted its nearest neighbour. forget now takes min_score (default 0.5 cosine), refuses below it, and reports the best candidate.
- **[16] Scaling the number of agents often amplifies context pressure, coordination errors, and system drift.**
  > However, scaling the number of agents often amplifies context pressure, coordination errors, and system drift.
- **[16] Building robust multi-agent systems requires more than prompt tuning or increased model intelligence; it requires architecture-focused engineering discipline to manage complexity under uncertainty.**
  > It is well known that building robust MAS requires more than prompt tuning or increased model intelligence. It necessitates engineering discipline focused on architecture to manage complexity under uncertainty.
- **[16] Agentic software is characterized by runtime generation and evolution under uncertainty.**
  > We characterize agentic software by a core property: \emph{runtime generation and evolution under uncertainty}.
- **[17] The paper identifies and formalizes Context-Fragmented Violations (CFVs), which are policy breaches where individual agent actions look locally safe but collectively violate organizational policies because critical policy facts are siloed in different departments' private contexts.**
  > We identify and formalize a novel security risk: Context-Fragmented Violations (CFVs) - a class of policy breaches where individual agent actions appear locally safe and reasonable, yet collectively violate organizational policies because critical policy facts are siloed in different departments private contexts.
- **[17] Existing prompt-based alignment mechanisms and monolithic interceptors are poorly matched to violations spanning contextual islands.**
  > Existing prompt-based alignment mechanisms and monolithic interceptors are poorly matched to violations that span contextual islands.
- **[17] Evaluation of eight frontier LLMs in execution-oriented multi-agent workflows with per-agent domain world models found substantial violation rates of 14-98%, with cross-domain data flows showing systematically higher violation rates than same-domain flows.**
  > To empirically validate the need for external enforcement, we evaluate eight frontier LLMs in execution-oriented multi-agent workflows with per-agent domain world models. All models exhibit substantial violation rates (14-98%), with cross-domain data flows showing systematically higher violation rates than same-domain flows.
- **[18] LLM-based autonomous agents remain limited when tasks require sustained coordination across roles, tools, and environments.**
  > LLM-based autonomous agents have demonstrated strong capabilities in reasoning, planning, and tool use, yet remain limited when tasks require sustained coordination across roles, tools, and environments.
- **[18] Tighter coordination in multi-agent systems amplifies the risk that errors propagate across agents and interaction rounds, producing failures that are difficult to diagnose and rarely lead to structural self-improvement.**
  > Multi-agent systems address this through structured collaboration among specialized agents, but tighter coordination also amplifies a less explored risk: errors can propagate across agents and interaction rounds, producing failures that are difficult to diagnose and rarely translate into structural self-improvement.
- **[19] In LLM multi-agent systems, unreliable agents are a key bottleneck to system-level reliability.**
  > Large language model-driven multi-agent systems (LLM-MAS) excel at complex tasks, yet unreliable agents remain a key bottleneck to system-level reliability.
- **[19] Existing failure attribution approaches such as direct prediction of agent-error pairs and agent-first failure attribution rely on local agent logs and miss global failures that only appear over full interaction trajectories, including cross-step inconsistencies and inter-agent coordination errors.**
  > Automatic failure attribution is therefore critical, but existing approaches, such as direct prediction of agent-error pairs and agent-first failure attribution, rely on local logs of agents and miss global failures that only manifest over full interaction trajectories, such as cross-step inconsistencies and inter-agent coordination errors.
- **[19] Directly predicting failures creates a large combinatorial search space that hinders fine-grained attribution.**
  > Moreover, directly predicting failures induces a large combinatorial search space, hindering fine-grained attribution.
- **[20] The paper argues that context compaction, summarization, or eviction is a safety-critical failure surface because in-context governance constraints that agents obey while visible can be silently removed, causing the same agent to perform prohibited tool actions later in a session.**
  > Modern LLM agents increasingly rely on context compaction, summarization, or eviction to keep long-running sessions within a token budget. We show that this context-management layer is a safety-critical failure surface: in-context governance constraints that agents reliably obey while visible can be silently removed by compaction, causing the same agent to perform prohibited tool actions later in the session.
- **[20] The paper names this compaction-induced safety failure mode Governance Decay.**
  > We call this failure mode Governance Decay.
- **[20] Across 1,323 episodes, policy violation rises from 0% with the policy in full context to 30% after compaction, reaching 59% for some models; when the constraint survives the summary violation remains 0%, but when it is dropped violation reaches 38%.**
  > Across 1,323 episodes, violation rises from 0% with the policy in full context to 30% after compaction, reaching 59% for some models; when the constraint survives the summary, violation remains 0%, but when it is dropped, violation reaches 38%.
- **[21] The paper identifies four foundational limitations of current LLM-based planning systems: unreliable self-validation, context loss, lack of transactional safeguards, and insufficient inter-agent coordination.**
  > This paper introduces SagaLLM, a structured multi-agent architecture designed to address four foundational limitations of current LLM-based planning systems: unreliable self-validation, context loss, lack of transactional safeguards, and insufficient inter-agent coordination.
- **[21] Recent frameworks often fail to ensure consistency, rollback, or constraint satisfaction across distributed workflows.**
  > While recent frameworks leverage LLMs for task decomposition and multi-agent communication, they often fail to ensure consistency, rollback, or constraint satisfaction across distributed workflows.
- **[21] Empirical evaluations across planning domains show that standalone LLMs frequently violate interdependent constraints or fail to recover from disruptions.**
  > Empirical evaluations across planning domains demonstrate that standalone LLMs frequently violate interdependent constraints or fail to recover from disruptions.
- **[22] Traditional LLMs are scoped to individual user sessions, limiting their knowledge to a single conversation and preventing them from learning user preferences that evolve over time.**
  > Traditional large language models (LLMs) are scoped to individual user sessions, limiting their knowledge to a single conversation and preventing them from learning user preferences that evolve over time.
- **[26] Controlled diagnostics show CICL identifies action-critical evidence: removing the top-utility semantic unit reduces F1 from 0.245 to 0.000.**
  > Controlled diagnostics show that CICL identifies action-critical evidence: removing the top-utility semantic unit reduces F1 from 0.245 to 0.000.
- **[27] The paper identifies three critical gaps: code-structure context, runtime-execution context, and commit-history context.**
  > We identify three critical gaps: code-structure context capturing cross-file data flows and memory operation patterns, runtime-execution context revealing crash semantics and memory origins, and commit-history context recovering how fragile code patterns were introduced.
- **[27] The paper states that vulnerability repair demands richer program context than general bug repair, and that existing agentic approaches do not engineer this context.**
  > However, vulnerability repair demands richer program context than general bug repair - context that security engineers routinely assemble in practice but that existing agentic approaches do not engineer.
- **[28] LLM-based multi-agent systems can fail even when communication succeeds because agents do not correctly track their peers' roles, knowledge, or intentions.**
  > LLM-based multi-agent systems can fail even when communication succeeds because agents do not correctly track their peers' roles, knowledge, or intentions.
- **[28] The paper investigates inter-agent misalignment cases labelled FC2 in MAST-Data and converts them into functional partner-state reasoning items using four explicit convertibility criteria.**
  > We investigate whether such inter-agent misalignment cases, labelled FC2 in MAST-Data, can be converted into functional partner-state reasoning items. ToMAS applies four explicit convertibility criteria to diagnosed execution traces.
- **[28] A full conversion pass over 242 eligible non-AG2 training traces produced 39 CLEAN items.**
  > A full conversion pass over 242 eligible non-AG2 training traces produced 39 CLEAN items.
- **[28] In an 18-trace reliability pilot, two annotators achieved 94.4% raw agreement and Cohen's kappa = 0.92.**
  > In an 18-trace reliability pilot, two annotators achieved 94.4% raw agreement and Cohen's kappa = 0.92.
- **[28] ToMAS provides a preliminary rubric and pipeline for converting diagnosed coordination failures into trainable partner-state reasoning items and identifies requirements for a conclusive matched-domain evaluation.**
  > ToMAS provides a preliminary rubric and pipeline for converting diagnosed coordination failures into trainable partner-state reasoning items and identifies the requirements for a conclusive matched-domain evaluation.
- **[29] The paper introduces CRAFT, a multi-agent benchmark for evaluating pragmatic communication in large language models under strict partial information.**
  > We introduce CRAFT, a multi-agent benchmark for evaluating pragmatic communication in large language models under strict partial information.
- **[29] In CRAFT, multiple agents have complementary but incomplete views and must coordinate through natural language to build a shared 3D structure that no single agent can fully observe.**
  > In this setting, multiple agents with complementary but incomplete views must coordinate through natural language to construct a shared 3D structure that no single agent can fully observe.
- **[29] The paper provides a diagnostic framework that decomposes failures into spatial grounding, belief modeling and pragmatic communication errors, with a taxonomy of behavioral failure profiles for frontier and open-weight models.**
  > We formalize this problem as a multi-sender Bounded Pragmatic Speaker problem and provide a diagnostic framework that decomposes failures into spatial grounding, belief modeling and pragmatic communication errors, including a taxonomy of behavioral failure profiles in both frontier and open-weight models.
- **[29] Across 8 open-weight and 7 frontier models including reasoning models, stronger reasoning ability did not reliably improve coordination, smaller open-weight models often matched or outperformed frontier systems, and improved individual communication did not guarantee successful collaboration.**
  > Across a diverse set of models, including 8 open-weight and 7 frontier including reasoning models, we find that stronger reasoning ability does not reliably translate to better coordination: smaller open-weight models often match or outperform frontier systems, and improved individual communication does not guarantee successful collaboration.
- **[31] LLM-based software engineering agents have a critical bottleneck: context length limitations cause failures on complex, long-horizon tasks.**
  > LLM-based Software Engineering agents face a critical bottleneck: context length limitations cause failures on complex, long-horizon tasks.
- **[32] The article says when questions cross systems, agents must discover tools, understand schemas/APIs, move identifiers, paginate, retry, and reconstruct relationships; this becomes slow, expensive, and brittle when rediscovered every investigation.**
  > When a question crosses several systems, the agent still has to discover which tools to call, understand different schemas and APIs, move identifiers between them, paginate through results, retry failed requests, and reconstruct relationships that were never represented explicitly.

At that point, the model is not primarily reasoning about the business. It is rebuilding data integration at inference time.

That can work for occasional tasks. It becomes slow, expensive, and brittle when the same relationships must be rediscovered for every investigation.
- **[32] The article states better models do not fix missing relationships between identifiers, conflicting business definitions, or stale copies; fragmentation remains in every request.**
  > Better models do not fix missing relationships between identifiers. They do not resolve conflicting business definitions or make stale copies current. They may become better at navigating fragmented systems, but the fragmentation remains part of every request.
- **[33] ClawMem detects contradictions between new and prior decisions and auto-decays superseded ones only when a contradiction judge is configured; otherwise the feature is disabled, though a merge-time contradiction gate blocks cross-observation contradictions before they land.**
  > **Detects contradictions** between new and prior decisions, auto-decaying superseded ones — when a contradiction **judge** is configured (`CLAWMEM_JUDGE_*`, v0.29.0; disabled otherwise) (with an additional merge-time contradiction gate in the consolidation worker that blocks cross-observation contradictions before they land, v0.7.1)
- **[33] ClawMem guards against cross-entity merges during consolidation by comparing entity anchors before merging similar observations, specifically preventing Alice-decided-X from merging into Bob-decided-X.**
  > **Guards against cross-entity merges** during consolidation — name-aware dual-threshold merge safety compares entity anchors before merging similar observations, preventing "Alice decided X" from merging into "Bob decided X" (v0.7.1)
- **[33] ClawMem prevents context bleed in derived insights by validating every draft through an anti-contamination wrapper with deterministic entity contamination check, LLM validator, and dedupe before writing cross-session deductive observations.**
  > **Prevents context bleed in derived insights** — the Phase 3 deductive synthesis pipeline validates every draft against an anti-contamination wrapper (deterministic entity contamination check + LLM validator + dedupe) before writing cross-session deductive observations (v0.7.1)

## q5. What are the criticisms, open problems and adoption signals for context layers in agent systems?

- **[1] Existing approaches address source-memory integration, memory governance, and authorization continuity individually, but do not treat them as combined core design targets across the memory lifecycle.**
  > Existing approaches address these concerns individually, but do not treat source--memory integration, memory governance, and authorization continuity as combined core design targets across the memory lifecycle.
- **[2] The repository shows 0 forks and 0 stars.** (also [5])
  > *   [Fork 0](https://github.com/login?return_to=%2Fguoliangdi%2Fclaw-zep)
*   [Star 0](https://github.com/login?return_to=%2Fguoliangdi%2Fclaw-zep)
- **[2] The repository page lists 1 branch and 0 tags.**
  > [**1**Branch](https://github.com/guoliangdi/claw-zep/branches)[**0**Tags](https://github.com/guoliangdi/claw-zep/tags)
- **[2] The repository history lists 10 commits.**
  > [10 Commits](https://github.com/guoliangdi/claw-zep/commits/main/)
- **[3] The authors claim no prior work combines a single shared, lossy-compressed KV pool with multi-reader concurrent agent access.**
  > To our knowledge, no prior work combines a single shared, lossy-compressed KV pool with multi-reader concurrent agent access.
- **[4] The engine, harnesses, and frozen JSON are MIT-licensed, and installing the native package is claimed to re-run the published numbers.**
  > Engine, harnesses and frozen JSON are MIT; pip install "fluctlightdb[native]" re-runs the published numbers.
- **[4] The authors position the work as no new neuroscience or transformer, but a missing layer of the data stack released for others to re-run and contest.**
  > We claim no new neuroscience and no new transformer: a missing layer of the data stack, released for others to re-run and contest.
- **[5] The repository shows 4 commits.**
  > [4 Commits](https://github.com/shivanshinigam/graphiti-zep-agent/commits/main/)
- **[8] The paper describes itself as a position paper that establishes the theoretical foundation for Context Lakes, identifies why existing architectures fail, and specifies what systems must guarantee for AI agents to operate constructively at scale.**
  > This position paper establishes the theoretical foundation for Context Lakes, identifies why existing architectures fail, and specifies what systems must guarantee for AI agents to operate constructively at scale.
- **[8] The paper formalizes architectural invariants, enforcement boundaries, and admissibility conditions required for correctness in collective agent systems.**
  > We formalize the architectural invariants, enforcement boundaries, and admissibility conditions required for correctness in collective agent systems.
- **[10] The project identifies documentation as the only guard for backend transition safety and states that documentation is not a guard.**
  > Documentation was the only guard, and documentation is not a guard.
- **[11] The framework claims safe, efficient, and interpretable cross-user knowledge sharing, with provable adherence to asymmetric, time-varying policies and full auditability of memory operations.**
  > Our framework enables safe, efficient, and interpretable cross-user knowledge sharing, with provable adherence to asymmetric, time-varying policies and full auditability of memory operations.
- **[12] Compared to Mem0, MemMachine uses roughly 80 percent fewer input tokens under matched conditions.**
  > Compared to Mem0, MemMachine uses roughly 80 percent fewer input tokens under matched conditions.
- **[12] MemMachine is presented as an open-source memory system.**
  > We present MemMachine, an open-source memory system that integrates short-term, long-term episodic, and profile memory within a ground-truth-preserving architecture that stores entire conversational episodes and reduces lossy LLM-based extraction.
- **[14] GENOME is now open source under the Apache License 2.0.**
  > GENOME is now open source under the Apache License 2.0.
- **[14] A consolidation bug silently destroyed the entity graph and all fact history by ranking entity and entity-fact records with the same access/recency fitness used for episodic memories and deleting the lowest scorers.**
  > DATA LOSS - consolidate() ranked entity and entity-fact records by the same access/recency fitness used for episodic memories and deleted the lowest scorers. Combining the temporal knowledge graph with consolidation silently destroyed the entity graph and all fact history: no error, no warning, no test covering it.
- **[14] The REST server initially lacked a trust policy and provenance field, so every HTTP write was untagged, nothing could be quarantined, and the memory firewall was unreachable for service and TypeScript SDK users.**
  > The REST server was the third entry point and nobody looked: create_app built its Memory with no trust policy and AddRequest had no provenance field, so every HTTP write was untagged, nothing could ever be quarantined, and the firewall was unreachable for anyone running GENOME as a service or through the TypeScript SDK.
- **[15] The paper identifies as an open gap that no existing system propagates knowledge between agents through the memory layer itself.**
  > No system propagates knowledge between agents through the memory layer itself.
- **[16] The paper proposes a three-layer engineering framework whose first layer is View/Context Engineering to manage the execution environment and maintain task-relevant Views.**
  > we introduce design principles under a three-layer engineering framework: \emph{View/Context Engineering} to manage the execution environment and maintain task-relevant Views, \emph{Structure Engineering} to organize dynamic binding over artifacts and agents, and \emph{Evolution Engineering} to govern the lifecycle of self-rewriting artifacts.
- **[16] The paper claims its abstractions improve the designability, scalability, and evolvability of agentic infrastructure.**
  > Together, these abstractions improve the \emph{designability}, \emph{scalability}, and \emph{evolvability} of agentic infrastructure.
- **[16] LSS design patterns are presented as semantic control blocks that stabilize fluid, inference-mediated interactions while preserving agent adaptability.**
  > Building on this framework, we develop LSS design patterns as semantic control blocks that stabilize fluid, inference-mediated interactions while preserving agent adaptability.
- **[17] The paper concludes that self-avoidance is unreliable and that multi-agent security benefits from a centralized enforcement layer operating above individual agents.**
  > These results indicate that self-avoidance is unreliable and that multi-agent security benefits from a centralized enforcement layer operating above individual agents.
- **[18] Existing surveys cover individual agent capabilities, multi-agent collaboration, or agent self-evolution separately, leaving the causal dependencies among them unexamined.**
  > Existing surveys cover individual agent capabilities, multi-agent collaboration, or agent self-evolution separately, leaving the causal dependencies among them unexamined.
- **[18] The survey identifies open challenges at stage boundaries and proposes a cross-stage research agenda for closed-loop multi-agent systems that can diagnose failures, reorganize structures, and refine agent behaviors.**
  > Beyond synthesizing existing work, we identify open challenges at stage boundaries and propose a cross-stage research agenda for closed-loop multi-agent systems capable of continuously diagnosing failures, reorganizing structures, and refining agent behaviors, extending current coordination frameworks toward more self-organizing forms of collective intelligence.
- **[18] The survey aims to provide a systematic reference and conceptual roadmap toward autonomous, self-improving multi-agent intelligence by bridging previously fragmented research threads.**
  > By bridging these previously fragmented research threads, this survey aims to offer both a systematic reference and a conceptual roadmap toward autonomous, self-improving multi-agent intelligence.
- **[18] The survey organizes its review around four causally linked stages called the LIFE progression: Lay the capability foundation, Integrate agents through collaboration, Find faults through attribution, and Evolve through autonomous self-improvement.**
  > This survey provides a unified review organized around four causally linked stages, which we term the LIFE progression: Lay the capability foundation, Integrate agents through collaboration, Find faults through attribution, and Evolve through autonomous self-improvement.
- **[18] For each stage, the survey provides taxonomies and formally characterizes dependencies between adjacent stages, showing that each stage depends on and constrains the next.**
  > For each stage, we provide systematic taxonomies and formally characterize the dependencies between adjacent stages, revealing how each stage both depends on and constrains the next.
- **[20] The paper studies a Compaction-Eviction Attack in which adversarial in-context content biases the summarizer to omit a legitimate policy, and reports that optimized injections defeat every evaluated model.**
  > We further study a Compaction-Eviction Attack, in which adversarial in-context content biases the summarizer to omit a legitimate policy, and show that optimized injections defeat every evaluated model.
- **[20] The paper proposes Constraint Pinning, a training-free mitigation that quarantines governance constraints from lossy compaction and restores violation to 0% in its benchmark.**
  > Finally, we propose Constraint Pinning, a simple training-free mitigation that quarantines governance constraints from lossy compaction and restores violation to 0% in our benchmark.
- **[20] The paper concludes that context management should be treated as a first-class governance surface for deployed LLM agents.**
  > These results identify context management as a first-class governance surface for deployed LLM agents.
- **[21] SagaLLM relaxes strict ACID guarantees but ensures workflow-wide consistency and recovery through modular checkpointing and compensable execution.**
  > Although SagaLLM relaxes strict ACID guarantees, it ensures workflow-wide consistency and recovery through modular checkpointing and compensable execution.
- **[23] The paper states that growing agentic task complexity increases trajectory lengths, challenging LLM agents with fixed context windows.**
  > The increasing complexity of agentic tasks has led to rapidly growing trajectory lengths, which poses significant challenges for large language model (LLM) based agents with fixed context windows.
- **[23] Existing context management methods such as truncation and summarization are inflexible and irreversible, because discarded or compressed information cannot be recovered later when it becomes relevant.**
  > Existing context management techniques, such as truncation and summarization, suffer from inherent inflexibility and irreversibility: once information is discarded or compressed, it cannot be recovered even when it becomes critically relevant in later decision steps.
- **[24] Current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured.**
  > Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured.
- **[24] The authors release MemHop, ProGraph, and baseline implementations.**
  > We release MemHop, ProGraph, and baseline implementations.
- **[25] On recall-required questions, the interpretive layer can interfere rather than help.**
  > Conversely, on recall-required questions, this layer can interfere rather than help.
- **[27] The ablation study confirms that the three context facets are mutually complementary and that multi-agent scaffolding and base-model capacity each play an essential role.**
  > Our ablation study confirms that the three context facets are mutually complementary, and that multi-agent scaffolding and base-model capacity each play an essential role.
- **[27] The paper concludes that multi-faceted program context engineering is a promising design direction for agentic vulnerability repair.**
  > Collectively, these findings establish multi-faceted program context engineering as a promising design direction for agentic vulnerability repair.
- **[29] The paper concludes that multi-agent coordination remains a fundamentally unsolved challenge for current language models.**
  > These results suggest that multi-agent coordination remains a fundamentally unsolved challenge for current language models.
- **[30] Existing methods address context problems through compression or retrieval on a single, flat context, which does not clearly separate different types of context information and often leads to degraded reasoning.**
  > Most existing methods address this issue through compression or retrieval applied to a single, flat context, which does not clearly separate different types of context information and often leads to degraded reasoning.
- **[30] LLM agents often perform poorly on complex, long-horizon tasks because their context becomes increasingly cluttered over time.**
  > Large language model (LLM) agents often perform poorly on complex, long-horizon tasks because their context becomes increasingly cluttered over time.
- **[31] Implicit context compression via an In-Context Autoencoder, which stores context as continuous embeddings rather than discrete tokens, works on single-shot common-knowledge and code-understanding tasks but fails on multi-step agentic coding tasks.**
  > One promising solution is to encode context as continuous embeddings rather than discrete tokens, enabling denser information storage. We apply the recently proposed In-Context Autoencoder for this purpose. While the method performs well on single-shot common-knowledge and code-understanding tasks, our experiments demonstrate that it fails on multi-step agentic coding tasks.
- **[31] The paper investigates why implicit context compression fails for software engineering agents and discusses possible contributing factors.**
  > In this paper, we explore this phenomenon and discuss possible factors contributing to this failure.
- **[32] Altertable reports that it found a second role for its lakehouse: it became the shared context layer behind Altertable's agentic features.**
  > Most teams adopt a lakehouse to store and query analytical data. We found a second role for ours: it became the shared context layer behind Altertable’s agentic features.

## Sources

1. AkasicMEM: Governed Enterprise Memory for Agents — Jeongmin Bae, Yongjae Kim, Kyoung Hur, Donghyoung Han, Min-Soo Kim (academic, 2026-09-22, quality 1.0) — https://arxiv.org/abs/2609.25563
2. guoliangdi/claw-zep — guoliangdi (primary, 2026-06-26, quality 1.0) — https://github.com/guoliangdi/claw-zep
3. PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference — Ishan Patel, Ishan Joshi (academic, 2026-04-27, quality 1.0) — https://arxiv.org/abs/2604.24971
4. FluctlightDB: A Memory Model of Data for AI Agents — Ganesh S (academic, 2026-07-10, quality 1.0) — https://arxiv.org/abs/2608.12365
5. shivanshinigam/graphiti-zep-agent — shivanshinigam (primary, 2026-09-17, quality 1.0) — https://github.com/shivanshinigam/graphiti-zep-agent
6. Mandol: An Agglomerative Agent Memory System for Long-Term Conversations — Yuhan Zhang, Zhiyuan Guo, Ziheng Zeng, Wei Wang, Wentao Wu, Lijie Xu (academic, 2026-06-29, quality 1.0) — https://arxiv.org/abs/2606.29778
7. ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models — Qianxun Xu, Xianfang Zeng, Xinyao Liao, Wei Cheng, Gang Yu, Chi Zhang (academic, 2026-09-18, quality 1.0) — https://arxiv.org/abs/2609.22641
8. Context Lake: A System Class Defined by Decision Coherence — Xiaowei Jiang (academic, 2026-01-15, quality 1.0) — https://arxiv.org/abs/2601.17019
9. Diachronic Hypergraphs for Orchestrated Multi-Agent Multimodal Memory Curation — Yichao Feng, Ran Zhang, Haoran Luo, Zhenghong Lin, Carl Yang, Anh Tuan Luu (academic, 2026-08-30, quality 1.0) — https://arxiv.org/abs/2608.29678
10. Quantum-L9/l9-graphiti-memory — Quantum-L9 (primary, 2026-10-03, quality 1.0) — https://github.com/Quantum-L9/l9-graphiti-memory
11. Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control — Alireza Rezazadeh, Zichao Li, Ange Lou, Yuying Zhao, Wei Wei, Yujia Bao (academic, 2025-05-23, quality 1.0) — https://arxiv.org/abs/2505.18279
12. MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents — Shu Wang, Edwin Yu, Oscar Love, Tom Zhang, Tom Wong, Steve Scargall, Charles Fan (academic, 2026-04-06, quality 1.0) — https://arxiv.org/abs/2604.04853
13. Directory-Aware Query and Maintenance in Vector Databases — Mengzhao Wang et al. (academic, 2026-06-15, quality 1.0) — https://arxiv.org/abs/2606.16903
14. NORTHTEKDevs/genome — NORTHTEKDevs (primary, 2026-09-04, quality 1.0) — https://github.com/NORTHTEKDevs/genome
15. HyphaeDB: A Living Knowledge Topology for Agent-First Memory — Krishna Halaharvi (academic, 2026-06-27, quality 1.0) — https://arxiv.org/abs/2606.28781
16. Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems — Weihao Zhang, Yitong Zhou, Huanyu Qu, Hongyi Li (academic, 2026-03-16, quality 1.0) — https://arxiv.org/abs/2603.15690
17. Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems — Jie Wu, Ming Gong (academic, 2026-04-24, quality 1.0) — https://arxiv.org/abs/2604.22879
18. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems — Shihao Qi et al. (academic, 2026-05-14, quality 1.0) — https://arxiv.org/abs/2605.14892
19. VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems — Hezhe Qiao, Hanghang Tong, Ee-Peng Lim, Bing Liu, Guansong Pang (academic, 2026-05-17, quality 1.0) — https://arxiv.org/abs/2605.17467
20. Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents — Shiyang Chen (academic, 2026-06-21, quality 1.0) — https://arxiv.org/abs/2606.22528
21. SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning — Edward Y. Chang and Longling Geng (academic, 2025-03-15, quality 1.0) — https://arxiv.org/abs/2503.11951
22. AIM: A Privacy-Aware Interoperable Memory Framework for Multi-Agent Multi-User LLM Systems — Zachary Johnson et al. (academic, 2026-09-14, quality 1.0) — https://arxiv.org/abs/2609.12320
23. ACE: Pluggable Adaptive Context Elasticizer across Agents — Ning Liao et al. (academic, 2026-06-30, quality 1.0) — https://arxiv.org/abs/2606.31564
24. Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles — Shengtong Zhu (academic, 2026-06-01, quality 1.0) — https://arxiv.org/abs/2607.19359
25. Beyond Recall: Behavioral Specification as an Interpretive Layer for AI Personalization — Aarik Gulaya (academic, 2026-05-27, quality 1.0) — https://arxiv.org/abs/2605.28969
26. Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents — Xinyu Guan, Qianyang Zhao, Yuming Deng (academic, 2026-09-22, quality 1.0) — https://arxiv.org/abs/2606.08151
27. AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair — Michael Fu, Qiyue Mei, Patanamon Thongtanunam, Kla Tantithamthavorn (academic, 2026-07-31, quality 1.0) — https://arxiv.org/abs/2607.29422
28. ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures — Muhammad Ashar Ishfaq, Glaucia Melo (academic, 2026-09-15, quality 1.0) — https://arxiv.org/abs/2609.16986
29. CRAFT: Grounded Multi-Agent Coordination Under Partial Information — Abhijnan Nath, Hannah VanderHoeven, Nikhil Krishnaswamy (academic, 2026-03-26, quality 1.0) — https://arxiv.org/abs/2603.25268
30. HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation — XinQi Wang, Jinwei Xiao, Sijia Cui, Hongming Zhang, Yanna Wang, Qingyang Zhang, Bo Xu (academic, 2026-08-16, quality 1.0) — https://arxiv.org/abs/2608.15703
31. On Problems of Implicit Context Compression for Software Engineering Agents — Kirill Gelvan, Igor Slinko, Felix Steinbauer, Egor Bogomolov, Florian Kofler, Yaroslav Zharov (academic, 2026-05-11, quality 1.0) — https://arxiv.org/abs/2605.11051
32. Lakehouse as Context Store — Sylvain Utard / Altertable (vendor, 2026-07-15, quality 0.6) — https://altertable.ai/blog/2026-07-15-lakehouse-as-context-store
33. Show HN: ClawMem – Open-source agent memory with SOTA local GPU retrieval — yoloshii (GitHub repo owner) (vendor, 2026-03-22, quality 0.6) — https://github.com/yoloshii/ClawMem
