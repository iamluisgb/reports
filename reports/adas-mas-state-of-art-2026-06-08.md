---
title: "Automated Design of Agentic Systems & Multi-Agent Algorithms: State of the Art 2025-2026"
date: 2026-06-08
type: special
url: https://luisgonzalezbernal.com/reports/reports/adas-mas-state-of-art-2026-06-08.html
summary: "ADAS, Meta Agent Search, LLM-MAS Orchestration & Production Deployment"
tags: [agents]
reading_time_minutes: 26
---
ADAS / Multi-Agent Systems · Special Report

# Automated Design of *Agentic Systems* & Multi-Agent Algorithms: State of the Art 2025-2026

08 Jun 2026

ADAS, Meta Agent Search, LLM-MAS Orchestration & Production Deployment

## Executive Summary

The period between mid-2025 and mid-2026 marks a paradigm shift in how agentic AI systems are conceived, designed, and deployed. Two formerly distinct research threads — **Automated Design of Agentic Systems (ADAS)** and **Multi-Agent Systems (MAS) orchestration algorithms** — have converged into a unified engineering discipline with direct production implications.

**ADAS** emerged as a formal research area with the publication of "Automated Design of Agentic Systems" (Hu, Lu, Clune — ICLR 2025, arXiv:2408.08435). The central insight is deceptively simple: instead of hand-engineering individual agents through prompt crafting and tool selection, a **meta-agent** can iteratively discover agent architectures by programming them as executable Python code. Because the search space is Turing-complete — any agentic system that can be expressed in code is theoretically discoverable — this approach fundamentally breaks the ceiling of manual design. The companion work **AgentSquare** (Shang et al., ICLR 2025, arXiv:2410.06153) formalizes this as modular evolution over four canonical building blocks (Planning, Reasoning, Tool Use, Memory), achieving a 17.2% average performance improvement over hand-crafted agents across coding, science, and math benchmarks.

On the MAS side, the integration of Large Language Models into multi-agent topologies has produced three dominant collaboration paradigms: **multi-stage pipelines** (serial decomposition), **collective decision-making** (debate, voting, consensus), and **self-refine** (iterative self-correction). The 2026 survey on RL for LLM-based MAS via orchestration traces (arXiv:2605.02801) formalizes the decision space into five sub-problems — when to spawn agents, whom to delegate to, how to communicate, how to aggregate results, and when to stop — each amenable to reinforcement learning from temporal interaction graphs.

Production deployment has reached a tipping point. **Semantic Router DSL** (arXiv:2603.27299) provides declarative per-request routing. PayPal's approach translates DSL specifications into Kubernetes artifacts with NetworkPolicy and ConfigMap resources. The SLEAN framework and Cisco's AI Security Framework (arXiv:2512.12921) address observability and attack surface management respectively. The open-source ecosystem — LangGraph, CrewAI, MetaGPT/MGX, ChatDev 2.0 — provides production-grade tooling, while AutoGen's maintenance status and transition to Microsoft Agent Framework signals consolidation.

**The thesis of this report:** ADAS is not merely an optimization technique for agent design — it is the beginning of agents becoming first-class citizens in software engineering, designing their own successors. The convergence with MAS orchestration algorithms means that the "intelligence infrastructure" of 2026-2027 will be designed, deployed, and evolved by the systems it comprises.

## Part I — ADAS Deep Analysis

## 1. The Evolution from Manual to Automated Design

The history of agentic system design can be decomposed into three distinct epochs, each characterized by a different locus of design intelligence:

### 1.1 Epoch I: Prompt Engineering (2022-2023)

The first generation of LLM-based agents relied on **prompt engineering** — the manual crafting of system prompts, few-shot examples, and chain-of-thought templates. Frameworks like LangChain and the original AutoGPT treated agents as "LLM + prompt + tool." The design space was bounded by human cognitive capacity: a single engineer could reason about perhaps 5-10 interacting prompt components before losing coherence. The fundamental limitation was that the agent's architecture was fixed; only the instructions were variable.

### 1.2 Epoch II: Tool-Augmented Agents (2023-2024)

The introduction of function calling APIs (OpenAI, Anthropic) and tool registries expanded the design space to include **tool selection and composition**. Agents could now reason about which tools to invoke, in what order, and how to interpret results. ReAct (Reasoning + Acting) and subsequent frameworks enabled dynamic tool-use strategies. However, the meta-level design decisions — which tools to include, how to structure the agent's reasoning loop, what memory architecture to use — remained manual. Engineers were essentially performing meta-design by hand, choosing from a palette of pre-defined architectural patterns.

### 1.3 Epoch III: Code-Driven Automated Design (2025-present)

ADAS represents the third epoch, where the agent's *entire architecture* — including its reasoning loop, tool integration strategy, memory structure, and inter-agent communication protocol — is expressed as executable code and discovered through systematic search. The critical insight from Hu et al. is that code is Turing-complete: any agentic system that can be computed can, in principle, be written as a Python function. This transforms the agent design problem from a constrained optimization over a fixed set of architectural templates into an **unconstrained program synthesis problem**.

> **The Turing-complete argument:** If the search space is Python code (or any Turing-complete language), then the set of discoverable agent architectures includes every possible computational procedure. The only constraints are the evaluator's ability to measure quality and the search algorithm's ability to navigate the space efficiently. This is not merely a theoretical statement — it has empirical consequences, as demonstrated by ADAS outperforming hand-designed agents on multiple benchmarks.

## 2. Meta Agent Search: Algorithm and Architecture

### 2.1 Algorithmic Formulation

The Meta Agent Search algorithm operates at the intersection of program synthesis and evolutionary optimization. Its formal structure is as follows:

```
Algorithm: Meta Agent Search
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Input:
  - Benchmark tasks T = {t₁, t₂, ..., tₙ}
  - Evaluation function E: Agent × Task → Score
  - Performance threshold θ
  - Maximum iterations T_max

1. Initialize:
   archive ← ∅
   meta_agent ← LLM with meta-instructions:
     "Given the archive of previously discovered agents,
      write a Python function implementing a new agent
      that may outperform all existing agents on the
      benchmark tasks."

2. For each iteration t = 1, 2, ..., T_max:
   a. Prompt meta_agent with current archive contents
   b. meta_agent generates candidate_agent (Python code)
   c. Execute candidate_agent on each task in T
   d. Score ← E(candidate_agent, T)
   e. If Score > θ OR Score > max(scores in archive):
        archive ← archive ∪ {candidate_agent}
      (Archive is sorted by performance, size bounded)

3. Return best_agent from archive
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The algorithm's elegance lies in its recursive structure: the meta-agent is itself an LLM that reads code (the archive), reasons about what to write next, and generates new code. Each iteration's output becomes input for future iterations, creating an **open-ended improvement loop**. The archive serves as both a memory mechanism (preventing redundant exploration) and a curriculum (each new candidate is conditioned on the best discoveries so far).

### 2.2 Three Key Components

The ADAS framework decomposes into three interacting components, each with distinct engineering challenges:

**Component 1: Search Space (Code).** The search space is the set of all valid Python programs that implement agent behavior. Unlike neural architecture search (NAS), where the search space is parameterized by discrete architectural choices (number of layers, kernel sizes, attention heads), ADAS's search space is the full space of Python programs. This has two consequences: (a) the space is vastly larger than any parameterized design space, but (b) it is also more expressive, enabling discovery of fundamentally novel architectures rather than interpolation within a fixed set of templates. The meta-agent generates code with access to standard Python libraries, API wrappers for LLM calls, and utility functions — the same toolkit a human engineer would use.

**Component 2: Search Algorithm (Meta-Agent).** The meta-agent functions as both the search operator and the heuristic guidance. It is prompted to read the archive (which contains the source code and performance metrics of previously discovered agents), identify patterns in high-performing designs, and synthesize novel candidates that incorporate promising features while exploring new directions. This is analogous to **cultural evolution**: each generation of agents has access to the full "cultural record" of previous discoveries. The meta-agent's quality directly determines search efficiency — a more capable foundation model (e.g., GPT-4-class vs. GPT-3.5-class) produces better candidate agents per iteration.

**Component 3: Performance Evaluator.** The evaluator executes each candidate agent on a benchmark suite and scores its performance. This component must handle: (a) sandboxed execution to prevent harmful code from affecting the host system; (b) timeout enforcement to prevent infinite loops; (c) deterministic task evaluation (unit tests, comparison to reference solutions); and (d) multi-dimensional scoring (accuracy, latency, token usage). The evaluator's design is critical because it determines the fitness landscape that the search algorithm navigates.

## 3. AgentSquare: Modular Evolution

AgentSquare (Shang et al., ICLR 2025) takes a complementary approach to ADAS by imposing a structured decomposition of the agent design space into four canonical modules:

| Module | Responsibility | Design Choices |
| --- | --- | --- |
| **Planning** | Task decomposition, strategy formulation | Zero-shot planning, chain-of-thought, tree-of-thought, iterative refinement |
| **Reasoning** | Logical inference, evidence evaluation | Deductive, abductive, analogical, causal reasoning patterns |
| **Tool Use** | External API calls, code execution, search | Single-tool, multi-tool orchestration, tool-augmented reasoning |
| **Memory** | Context management, history retrieval | Short-term buffer, long-term retrieval, episodic + semantic stores |

### 3.1 Evolutionary Module Recombination

AgentSquare employs a **genetic-algorithm-inspired** approach where each agent is represented as a genotype of four module slots. The evolutionary operators are:

- **Mutation:** Random modification of a single module (e.g., swapping a planning strategy)
- **Crossover:** Combining modules from two parent agents into a new child
- **Selection:** Tournament selection based on benchmark performance

### 3.2 In-Context Surrogate Models

A key innovation in AgentSquare is the use of **in-context surrogate models** for performance prediction. Instead of evaluating every candidate agent on the full benchmark suite (which is computationally expensive), AgentSquare trains the LLM to predict agent performance from the module descriptions alone. This surrogate model serves as a cheap proxy for the actual evaluator, enabling the evolutionary search to explore a larger fraction of the design space per compute budget. The surrogate is updated iteratively as ground-truth performance data accumulates, creating a feedback loop between predicted and actual performance.

### 3.3 Empirical Results

AgentSquare demonstrates a **17.2% average performance gain** over hand-crafted agents across the GAIA benchmark suite. More importantly, the discovered agents exhibit **cross-domain transferability**: agents optimized for coding tasks show improved performance on scientific reasoning and mathematical problem-solving, suggesting that the evolutionary process discovers general architectural principles rather than domain-specific heuristics.

## 4. Critique: Inefficiencies of Meta Agents

The work "Inefficiencies of Meta Agents for Agent Design" (arXiv:2510.06711) provides a rigorous critical analysis of the ADAS paradigm, identifying several fundamental limitations:

**Finding 1: Evolutionary > Context Expansion.** The authors demonstrate that evolutionary search (as in AgentSquare) is more sample-efficient than simply expanding the context window of the meta-agent with more archive examples. This suggests that the meta-agent's ability to generalize from past discoveries has a fundamental ceiling — adding more examples to the prompt yields diminishing returns, while structured evolutionary operations maintain search efficiency.

**Finding 2: Low Behavioral Diversity.** Meta agents tend to converge on a narrow set of behavioral patterns. Despite the Turing-complete search space, the meta-agent's generation process is biased by the foundation model's training distribution, producing candidates that cluster around familiar architectural motifs. This "mode collapse" is analogous to the diversity collapse observed in GAN training.

**Finding 3: Economic Viability Threshold.** The analysis estimates that ADAS requires **15,000+ evaluation examples** to achieve economically viable improvements over manual design. Below this threshold, the computational cost of running the search (meta-agent inference + candidate evaluation) exceeds the cost of a skilled engineer manually designing the agent. This has significant implications for production deployment: ADAS is currently viable only for organizations with large-scale agent fleets where the amortized design cost per agent is justified.

## 5. MASPOB: Bandit-Based Prompt Optimization

MASPOB (Multi-Agent System Prompt Optimization via Bandits, arXiv:2603.02630) addresses three critical challenges in optimizing multi-agent systems:

**Sample Efficiency.** Multi-agent systems have combinatorially large configuration spaces (each agent's prompt × each agent's role × the communication topology). MASPOB uses multi-armed bandit algorithms to efficiently explore this space, treating each configuration as an "arm" and allocating evaluation budget to the most promising configurations using upper confidence bound (UCB) exploration.

**Topology Coupling.** In MAS, the performance of one agent depends on the behavior of others — the agents are coupled through their interactions. MASPOB models this coupling explicitly, recognizing that optimizing agent A's prompt in isolation may be suboptimal when agent B's behavior changes. The bandit framework naturally handles this by treating the joint configuration as the decision unit.

**Combinatorial Explosion.** For a system with N agents, each with K possible prompt configurations, the search space is K^N. MASPOB employs a **hierarchical decomposition** that optimizes individual agent prompts within a fixed topology first, then searches over topologies, reducing the effective search space from exponential to polynomial.

## Part II — MAS Algorithms Deep Analysis

## 1. LLM Integration in MAS Topologies

### 1.1 Role Specialization Patterns

The integration of LLMs into multi-agent systems has produced several distinct role specialization patterns. The survey by Chen et al. (arXiv:2412.17481) identifies three primary architectures:

**Hierarchical Decomposition.** A "manager" agent decomposes tasks and delegates subtasks to "worker" agents. Each worker has a specialized role (e.g., code writer, tester, reviewer). The manager monitors progress and handles inter-worker coordination. This mirrors the organizational structure of software engineering teams and is the dominant pattern in MetaGPT and ChatDev.

**Peer-to-Peer Collaboration.** Agents interact as equals, each contributing their expertise to a shared problem. Debate-based systems (Du et al., 2023) exemplify this pattern: multiple agents independently solve a problem, then critique each other's solutions until consensus emerges. The advantage is robustness to individual agent failures; the disadvantage is the communication overhead grows quadratically with agent count.

**Hub-and-Spoke Orchestration.** A central orchestrator agent maintains a global state and routes subtasks to specialized agents on demand. The orchestrator decides which agent to invoke, when to aggregate results, and when to terminate. This is the pattern adopted by production systems like OpenAI Codex and Anthropic Claude Code, where the LLM serves as the central decision-making hub coordinating tool use, code generation, and verification.

### 1.2 Distributed Reasoning Architectures

Beyond role specialization, LLM-based MAS enable distributed reasoning patterns that have no direct analog in classical multi-agent systems:

**Chain-of-Thought Distribution.** Different agents handle different reasoning steps in a chain. For example, Agent 1 performs problem decomposition, Agent 2 generates intermediate inferences, Agent 3 validates logical consistency, and Agent 4 produces the final answer. This "reasoning pipeline" distributes the cognitive load across multiple models, potentially enabling specialization in different reasoning modalities (e.g., one model optimized for mathematical reasoning, another for natural language understanding).

**Ensemble Reasoning.** Multiple agents independently solve the same problem, and a meta-agent aggregates results through voting, averaging, or learned selection. This leverages the "wisdom of crowds" effect observed in LLM ensembles, where diversity of reasoning paths increases the probability of finding correct solutions.

### 1.3 Simulation Frameworks

Two notable simulation frameworks have emerged for studying LLM-based MAS dynamics:

**AgentVerse** provides a configurable environment for simulating multi-agent interactions with controllable agent populations, communication topologies, and task environments. It enables systematic study of emergent behaviors — phenomena like cooperation, competition, and information cascading — as a function of system parameters.

**Generative Agents** (Park et al.) demonstrates that LLM-based agents with persistent memory can exhibit socially plausible behaviors in simulated environments, including relationship formation, information diffusion, and collective decision-making. The key architectural insight is the separation of *observation* (perceiving the environment), *reflection* (abstracting from observations), and *planning* (generating future actions) into distinct cognitive modules.

## 2. Collaboration Mechanisms Taxonomy

### 2.1 Multi-Stage Pipeline

The simplest collaboration paradigm is the **serial pipeline**, where agents process a task in a fixed sequence. Each agent receives the output of the previous agent and produces input for the next. This pattern is effective for tasks that naturally decompose into sequential stages (e.g., requirements → design → implementation → testing → deployment). The pipeline's simplicity enables straightforward error handling (each stage can validate its inputs) and performance optimization (stages can be parallelized across independent subtasks).

The ChatDev 2.0 framework exemplifies this pattern with its "virtual software company" architecture: a CEO agent initiates projects, a CTO agent designs architecture, programmer agents write code, and tester agents verify. The pipeline is configurable through YAML files, making it accessible to non-developers.

### 2.2 Collective Decision-Making

**Debate-based systems** employ multiple agents arguing for different positions, with a judge agent (or majority vote) determining the consensus. This approach has been shown to reduce hallucination rates by 15-30% compared to single-agent baselines, as the adversarial dynamic forces agents to justify their claims.

**Voting mechanisms** extend debate to more formal aggregation: each agent produces a solution, and the system selects the solution with the most support. Variants include weighted voting (where agents with better track records receive higher weights) and liquid democracy (where agents can delegate their vote to more capable agents).

**Consensus protocols** go further, requiring all agents to converge on a single answer through iterative negotiation. This is computationally expensive but produces the highest-quality outputs for high-stakes decisions.

### 2.3 Self-Refine Framework

The self-refine paradigm treats a single agent (or the system as a whole) as both the generator and critic of its own output. The agent produces an initial solution, critiques it against defined criteria, and iteratively improves until convergence or a budget limit. When applied in multi-agent settings, different agents can serve as specialized critics (e.g., a "security reviewer" agent, a "performance reviewer" agent, a "correctness reviewer" agent), each providing feedback from their domain of expertise.

### 2.4 Communication Content: Natural Language vs. Custom Protocols

A critical design decision in MAS is the format of inter-agent communication. **Natural language** communication (as used in AutoGen, CrewAI) is flexible and human-interpretable but verbose and ambiguous. **Structured protocols** (JSON schemas, function signatures) are precise but less flexible. Production systems are converging on a **hybrid approach**: natural language for high-level reasoning and coordination, structured protocols for data exchange and tool invocations.

## 3. Multi-Agent Deep Reinforcement Learning (MADRL) Advances

### 3.1 Partial Observability Resolution

In LLM-based MAS, each agent typically has access only to its local context (its own history and received messages). This partial observability creates information asymmetries that can lead to suboptimal collective behavior. MADRL approaches address this through: (a) **attention-based message aggregation**, where agents learn to extract relevant information from partial histories; (b) **shared belief states**, where a centralized critic maintains a global representation that is distilled into local observations; and (c) **communication learning**, where agents learn what information to share and when.

### 3.2 Dynamic Communication Protocols

Static communication topologies (e.g., all-to-all, ring, tree) are insufficient for LLM-based MAS where the optimal communication structure depends on the task. MADRL enables agents to learn: **when to communicate** (sparse communication reduces overhead), **whom to communicate with** (targeted communication is more informative than broadcast), and **what to communicate** (compressing information to relevant content). Leader-follower topologies emerge naturally when some agents are consistently more informative than others.

### 3.3 Credit Assignment: Token-Level to Team-Level

One of the most challenging problems in MADRL for LLM-based MAS is credit assignment — determining which agent's contribution led to a successful (or failed) outcome. The 2026 survey identifies a spectrum of credit assignment granularities:

- **Token-level:** Attributing outcome quality to individual tokens generated by specific agents (finest granularity, but requires per-token reward models)
- **Turn-level:** Attributing outcomes to individual agent interactions (medium granularity, used in debate-based systems)
- **Task-level:** Attributing outcomes to the overall system configuration (coarsest granularity, simplest to implement)
- **Team-level:** Attributing outcomes to collaborative subgroups (used in hierarchical MAS where teams of agents handle subtasks)

### 3.4 Eight Reward Families for Orchestration

The orchestration traces survey (arXiv:2605.02801) identifies eight reward signal families that can be used to train MAS orchestration policies:

| # | Reward Family | Source | Granularity |
| --- | --- | --- | --- |
| 1 | **Task Completion** | Final answer correctness | Binary or continuous |
| 2 | **Process Quality** | Reasoning chain validity | Step-level |
| 3 | **Efficiency** | Token usage, latency | System-level |
| 4 | **Collaboration Quality** | Information exchange utility | Interaction-level |
| 5 | **Robustness** | Performance under perturbation | System-level |
| 6 | **Safety** | Harmful output prevention | Output-level |
| 7 | **Alignment** | Conformity to guidelines | Output-level |
| 8 | **User Satisfaction** | Human feedback signals | Session-level |

## 4. Orchestration Traces: The Five Sub-Decisions

The 2026 survey on RL for LLM-based MAS through orchestration traces (arXiv:2605.02801) provides the most comprehensive formalization of the MAS orchestration problem. It decomposes the orchestrator's role into five interdependent sub-decisions:

**Sub-Decision 1: When to Spawn.** The orchestrator must determine whether the current task requires additional agents or can be handled by existing ones. This is a resource allocation problem with implications for latency (spawning is expensive) and capability (more agents may enable better solutions). The optimal spawning policy depends on task complexity, current agent utilization, and the diminishing returns of additional parallelism.

**Sub-Decision 2: Whom to Delegate To.** Given a set of available agents, the orchestrator must select the most appropriate agent(s) for each subtask. This is a routing problem that requires maintaining estimates of each agent's capabilities, current workload, and historical performance on similar tasks. In production systems, this is often implemented as a semantic router that matches task embeddings to agent capability descriptions.

**Sub-Decision 3: How to Communicate.** The orchestrator must determine the communication format, channel, and content for each inter-agent message. This includes decisions about: message verbosity (full context vs. compressed summaries), communication timing (synchronous vs. asynchronous), and communication topology (direct vs. through the orchestrator).

**Sub-Decision 4: How to Aggregate.** When multiple agents produce partial results, the orchestrator must combine them into a coherent output. Aggregation strategies range from simple (majority vote, concatenation) to sophisticated (learned fusion, debate-and-judge). The choice depends on the degree of overlap between agent outputs and the cost of conflict resolution.

**Sub-Decision 5: When to Stop.** The orchestrator must determine when the system's output is "good enough" or when further computation yields diminishing returns. This is essentially a **halting problem** with no optimal solution in general, requiring heuristics based on output stability (convergence of answers across iterations), resource budgets (token/latency limits), and quality thresholds (passing verification tests).

## 5. Industrial Evidence: Production MAS Deployments

**Kimi Agent Swarm (Moonshot AI).** Kimi's agent swarm architecture deploys hundreds of specialized agents in parallel, each handling different aspects of user queries (web search, document analysis, code execution, creative writing). The system employs a hub-and-spoke orchestration with a routing agent that classifies incoming requests and dispatches them to appropriate agent clusters. The key engineering challenge is maintaining consistency across agents that may share context.

**OpenAI Codex.** Codex operates as a single-agent system with extensive tool use, but its architecture reveals MAS principles: the agent maintains a planning module (task decomposition), an execution module (code generation and testing), and a verification module (result validation). The "conversation" between these modules effectively creates an implicit multi-agent system, where different cognitive functions compete and cooperate within a single LLM call chain.

**Anthropic Claude Code.** Claude Code extends the single-agent paradigm with a structured tool ecosystem that functions as a virtual agent team. Each tool (file editor, terminal, web search, browser) operates semi-autonomously, with the LLM serving as the orchestrator. The system's performance on SWE-bench and similar benchmarks demonstrates that this "tools as agents" pattern can rival explicit multi-agent architectures for software engineering tasks.

## Part III — Convergence and Practical Implementation

## 1. How ADAS and MAS Converge

The convergence of ADAS and MAS manifests in three concrete ways:

**ADAS designs MAS configurations.** The meta-agent in ADAS can generate not just single-agent architectures but entire multi-agent systems. The search space includes agent-to-agent communication protocols, delegation hierarchies, and aggregation strategies. This means ADAS is a tool for *automated MAS engineering* — discovering optimal multi-agent topologies for specific task domains.

**MAS provides the fitness evaluation for ADAS.** Multi-agent evaluation environments (where multiple agents collaborate or compete on complex tasks) provide richer fitness signals for ADAS than single-agent benchmarks. A candidate agent's ability to integrate into an existing multi-agent system — to communicate effectively, to complement other agents' capabilities, to avoid redundancy — is a dimension of quality that single-agent evaluation cannot capture.

**Orchestration traces bridge the gap.** The orchestration traces framework (arXiv:2605.02801) provides the formal machinery to represent MAS configurations as data structures amenable to optimization. By encoding the five sub-decisions (spawn, delegate, communicate, aggregate, stop) as learnable policies, orchestration traces make MAS configurations accessible to ADAS-style search. This creates a closed loop: ADAS discovers orchestration policies, MAS evaluates them, and the results feed back into ADAS.

## 2. Framework Comparison

| Framework | Architecture | Paradigm | Open Source | Production Ready |
| --- | --- | --- | --- | --- |
| **LangGraph** | State graph (nodes = agents/functions, edges = conditional transitions) | Low-level orchestration with fine-grained control flow | Yes | Yes — Klarna, Replit, LinkedIn |
| **CrewAI** | Role-based (agents with roles, goals, backstories) | Multi-agent crews with hierarchical or sequential task execution | Yes | Yes — cloud deployment, enterprise tier |
| **AutoGen** | Conversational (agents communicate via message passing) | Multi-agent debate and collaborative problem-solving | Yes → Maintenance mode | Migrating to Microsoft Agent Framework |
| **MetaGPT / MGX** | SOP-based (Standard Operating Procedures define agent workflows) | Virtual software company with defined roles (PM, architect, engineer, QA) | Yes | Yes — mgx.dev production service |
| **ChatDev 2.0** | Zero-code (YAML config files, visual editor) | Config-driven multi-agent with role templates | Yes | Yes — simplified deployment |
| **Semantic Router DSL** | Declarative (DSL → inference routing rules) | Per-request routing to optimal model/agent | — | Yes — production LLM routing |

### 2.1 Framework Selection Criteria

The choice of framework depends on the deployment context and engineering maturity:

**LangGraph** is preferred when developers need maximum control over agent execution flow. Its state-graph paradigm allows explicit modeling of conditional transitions, loops, and parallel execution paths. This makes it suitable for complex workflows where the orchestration logic cannot be expressed as a simple pipeline. The trade-off is higher implementation complexity — developers must design the graph structure themselves.

**CrewAI** is preferred when the use case maps naturally to a team of specialists with defined roles. Its role-based abstraction (each agent has a role, goal, and backstory) provides a higher-level interface that reduces implementation time. The cloud deployment option eliminates infrastructure management concerns.

**MetaGPT/MGX** is preferred for software engineering workflows where the SOP-based architecture provides natural alignment with software development processes. The mgx.dev production service demonstrates that this paradigm can scale to enterprise workloads.

**Semantic Router DSL** is preferred for production LLM inference routing where the primary concern is latency and cost optimization rather than complex multi-agent collaboration. Its declarative approach enables operations teams to modify routing rules without code changes.

## 3. SRE Perspective: Production Considerations

### 3.1 Observability

Operating MAS in production requires comprehensive observability across multiple dimensions:

**Orchestration Flow Tracing.** Every inter-agent interaction must be logged with timestamps, agent identifiers, message content, and latency metrics. The OpenTelemetry framework provides a natural fit, with custom span attributes for agent-specific metrics (tokens consumed, tools invoked, reasoning steps). The key challenge is that MAS generates far more trace data than single-agent systems — a 10-agent system with all-to-all communication produces O(N²) traces per task, compared to O(N) for independent agents.

**Token-Level Metrics.** For cost management and performance optimization, organizations must track token consumption per agent, per task type, and per orchestration pattern. This enables identification of inefficient communication patterns (e.g., agents exchanging redundant information) and optimization of prompt engineering to reduce token overhead.

**Anomaly Detection.** MAS introduces new failure modes that single-agent systems don't exhibit: communication loops (agents sending messages back and forth without progress), information cascading (errors propagating through the agent network), and deadlocks (agents waiting for each other indefinitely). Monitoring systems must detect these patterns and trigger circuit breakers.

### 3.2 Scalability

**Parallel Agent Execution.** Modern orchestration frameworks support concurrent agent execution, but resource management becomes critical. Each agent typically requires an LLM inference call, and with token-per-second pricing, uncontrolled parallelism can cause exponential cost growth. Production deployments require: (a) concurrency limits per agent pool; (b) priority queues for high-importance tasks; (c) resource budgets per workflow; and (d) automatic scaling based on queue depth and latency SLAs.

**State Management.** MAS state is distributed across multiple agents, each maintaining its own context window. Synchronizing state across agents — particularly for shared memory systems — requires careful engineering. The choice between centralized state (a single shared store) and decentralized state (each agent maintains its own, synchronized via messages) involves trade-offs between consistency and latency.

### 3.3 Security

Cisco's "Integrated AI Security and Safety Framework" (arXiv:2512.12921) provides a comprehensive taxonomy of attack surfaces in AI agent systems. For MAS specifically, the framework identifies:

**Inter-Agent Injection Attacks.** A malicious or compromised agent can inject adversarial messages into the agent network, influencing the behavior of other agents. This is analogous to data poisoning in distributed ML but operates at the semantic level. Mitigations include message authentication, content filtering, and trust-weighted aggregation.

**Orchestration Manipulation.** An attacker who can influence the orchestrator's routing decisions can direct tasks to compromised agents, bypass security checks, or prevent legitimate agents from receiving tasks. This requires securing the orchestration layer with access controls, audit logging, and anomaly detection.

**Data Exfiltration via Agent Communication.** In systems where agents handle sensitive data, inter-agent communication channels can be exploited to exfiltrate information. The Cisco framework recommends implementing data loss prevention (DLP) policies at the agent communication layer, with automatic redaction of sensitive content from inter-agent messages.

### 3.4 Declarative Orchestration: PayPal's Approach

PayPal's "Declarative LLM Agent Orchestration" (arXiv:2512.19769) presents a production-proven approach to managing MAS at scale:

**DSL → Kubernetes Artifacts.** Orchestration workflows are defined in a domain-specific language (DSL) that abstracts away infrastructure concerns. The DSL compiler translates workflow definitions into Kubernetes-native artifacts: Deployment objects for agent pods, Services for inter-agent communication, ConfigMaps for agent configurations, and NetworkPolicies for communication access control.

**Infrastructure as Code for MAS.** The DSL approach ensures that MAS configurations are version-controlled, testable, and reproducible. Changes to orchestration logic follow the same CI/CD pipeline as application code, with automated testing of workflow behavior before deployment. This addresses a critical gap in current MAS frameworks, where orchestration logic is typically embedded in application code and difficult to manage operationally.

**NetworkPolicy for Agent Isolation.** By generating Kubernetes NetworkPolicies from DSL specifications, PayPal ensures that agents can only communicate with authorized peers. This provides defense-in-depth: even if an agent is compromised, the network policy prevents it from communicating with unauthorized agents or accessing restricted resources.

## References

## Primary Sources

1. Hu, S., Lu, C., Clune, J. "Automated Design of Agentic Systems." *ICLR 2025*. [arXiv:2408.08435](https://arxiv.org/abs/2408.08435) — Foundational ADAS paper introducing Meta Agent Search.
2. Shang, Y. et al. "AgentSquare: Automatic LLM Agent Search in Modular Design Space." *ICLR 2025*. [arXiv:2410.06153](https://arxiv.org/abs/2410.06153) — Modular evolutionary agent design with 4 canonical modules.
3. "Inefficiencies of Meta Agents for Agent Design." [arXiv:2510.06711](https://arxiv.org/abs/2510.06711) — Critical analysis of ADAS limitations including diversity collapse and economic viability thresholds.
4. "MASPOB: Multi-Agent System Prompt Optimization via Bandits." [arXiv:2603.02630](https://arxiv.org/abs/2603.02630) — Bandit-based approach to MAS prompt optimization addressing sample efficiency and topology coupling.
5. "Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces." [arXiv:2605.02801](https://arxiv.org/abs/2605.02801) — 2026 survey formalizing the five sub-decisions of MAS orchestration and eight reward families.
6. Chen, S. et al. "A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application." [arXiv:2412.17481](https://arxiv.org/abs/2412.17481) — Comprehensive survey of LLM-based MAS architectures and applications.
7. "A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges." *Springer 2024*. [Springer Link](https://link.springer.com/article/10.1007/s44336-024-00009-2) — Infrastructure-focused survey covering deployment challenges.
8. "Declarative LLM Agent Orchestration." [arXiv:2512.19769](https://arxiv.org/abs/2512.19769) — PayPal's DSL-based approach to production MAS orchestration on Kubernetes.
9. Cisco "Integrated AI Security and Safety Framework." [arXiv:2512.12921](https://arxiv.org/abs/2512.12921) — Attack surface taxonomy and security framework for AI agent systems.
10. "Semantic Router DSL for Production LLM Inference Routing." [arXiv:2603.27299](https://arxiv.org/abs/2603.27299) — Declarative routing for production LLM inference systems.

## GitHub Repositories

- **ADAS (Meta Agent Search):** [github.com/ShengranHu/ADAS](https://github.com/ShengranHu/ADAS)
- **AutoGen (Microsoft):** [github.com/microsoft/autogen](https://github.com/microsoft/autogen)
- **CrewAI:** [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- **LangGraph (LangChain):** [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- **MetaGPT:** [github.com/geekan/MetaGPT](https://github.com/geekan/MetaGPT)
- **ChatDev:** [github.com/OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev)

---

This report was compiled on 08 June 2026 by the AI Research Intelligence team. All cited papers are from peer-reviewed venues (ICLR 2025, Springer 2024) or published on arXiv with version stamps. Framework assessments reflect publicly available information as of the report date. No proprietary or confidential data was used in this analysis.

Sources: ICLR 2025 proceedings, arXiv CS.AI (2024-2026), NVIDIA Developer Blog, OpenBMB/ChatDev GitHub, AutoGen documentation, MetaGPT whitepaper, Google DeepMind ADAS research notes. Full reference list above.
