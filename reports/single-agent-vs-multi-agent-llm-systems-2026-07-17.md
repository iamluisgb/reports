---
title: "Single-Agent vs. Multi-Agent LLM Systems: The Architectural Debate"
date: 2026-07-17
type: special
url: https://luisgonzalezbernal.com/reports/reports/single-agent-vs-multi-agent-llm-systems-2026-07-17.html
summary: "21 papers analyzed · Debate, roles, and voting paradigms · MoE isomorphism · Cost-normalized benchmarks · Open problems"
tags: [agents, research]
reading_time_minutes: 15
---
AI Architecture · Special Report

# Single-Agent vs. Multi-Agent *LLM Systems*

17 Jul 2026

21 papers analyzed · Debate, roles, and voting paradigms · MoE isomorphism · Cost-normalized benchmarks · Open problems

## Executive Summary

The architectural debate between single-agent systems (SAS) and multi-agent systems (MAS) for LLM-based cognition has reached an empirical inflection point. Twenty-one peer-reviewed papers and preprints from 2023–2026 establish four core findings:

- **MAS consistently outperforms SAS on factual verification, mathematical reasoning, and complex code generation** when employing debate paradigms and role specialization (Du et al., ICML 2024; Qian et al., ACL 2024).
- **The advantage is not universal or free.** When reasoning-token budgets are normalized, SAS matches or exceeds MAS on multi-hop reasoning tasks ([arXiv:2604.02460](https://arxiv.org/abs/2604.02460), 2026). Many reported MAS gains are explained by higher total compute, not inherent architectural superiority.
- **Brute-force sampling-and-voting scales logarithmically** with agent count and is orthogonal to complex methods (Li et al., 2024, "Agent Forest").
- **The MoE–MAS relationship is isomorphic:** conditional activation of specialized sub-systems operates at the weight level (MoE) and the agent level (MAS) using the same underlying principle.

> **Core thesis:** The correct question is not "MAS or SAS?" but "how should compute be distributed across specialized sub-systems given the task structure, available budget, and latency constraints?"

## Part I

## Theoretical Framework: Why Single Agents Hit a Ceiling

### Cognitive Noise and Self-Correction Failure

A single-agent system operates under **forced internal coherence**: the same model generates, evaluates, and corrects its own output. Three empirically documented failure modes emerge from this constraint:

**a) Intrinsic self-correction fails without external feedback.** Huang et al. (2023, [arXiv:2303.17651](https://arxiv.org/abs/2303.17651)) introduced Self-Refine, where a single LLM serves as generator, refiner, and feedback provider. The approach improves ~20% over direct generation across 7 tasks. However, Kumar et al. (2023, [arXiv:2310.01798](https://arxiv.org/abs/2310.01798)) demonstrated the critical limitation:

> **"LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."** — Kumar et al., 2023

Without an external signal, LLMs bend their initial responses toward more plausible-sounding but less accurate directions. The model lacks the ability to distinguish between "sounds right" and "is right" when both evaluations come from the same source.

**b) Computational confirmation bias.** A single agent tends to seek evidence that confirms its first generation rather than refuting it. This amplifies across long reasoning chains where each step depends on the previous one without a divergence point.

**c) Multiplicative error accumulation.** Autoregressive models compound errors along reasoning chains. Without external validation checkpoints, errors propagate and multiply — a single misstep at step 3 of a 10-step derivation corrupts all subsequent reasoning.

### Context Window Limitations

A monolithic agent must pack **all problem context, reasoning history, available tools, and cross-task memory** into a single context window. This produces:

- **Compression pressure:** as history grows, the model must compress information, losing detail at critical junctures.
- **Lost-in-the-middle degradation:** LLMs show significant performance drops for information positioned in middle context locations.
- **Memory-induced drift:** The "Agent Cognitive Compressor" paper ([arXiv:2601.11653](https://arxiv.org/abs/2601.11653), 2025) documents that long-duration agents experience "loss of constraint focus, error accumulation, and memory-induced drift" — phenomena that worsen exponentially with interaction length.

### The Macro Fallacy: Statistical Self-Consistency Violations

A recent finding reveals a deep theoretical limitation. "Partition, Prompt, Aggregate" ([arXiv:2607.15277](https://arxiv.org/abs/2607.15277), July 2026) demonstrates that LLMs **systematically violate basic statistical self-consistency properties**. Models possess relevant subpopulation knowledge but fail to propagate it reliably into aggregate estimates. The authors call this the **"macro fallacy"** — a monolithic agent processing a complex problem as a whole cannot recover information it reliably produces when processing sub-parts of the same problem.

This finding provides a theoretical grounding for why multi-agent decomposition works: by forcing different agents to handle different sub-problems, MAS sidesteps the aggregation failure that plagues single-agent processing.

## Part II

## Multi-Agent Paradigms: A Deep Dive

### Paradigm 1 — Role-Based Collaboration with SOPs

**ChatDev** (Qian et al., 2023 — ACL 2024, [arXiv:2307.07924](https://arxiv.org/abs/2307.07924)) is a chat-powered software development framework where specialized agents (CEO, CTO, programmer, tester) collaborate through a **chat chain** — a predefined sequence of software lifecycle phases (design → coding → testing).

| Component | Mechanism | Effect |
| --- | --- | --- |
| Chat chain | Predefined phase sequence with communication rules per phase | Acts as an SOP — constrains what agents discuss and when |
| Role specialization | Each agent has defined responsibilities and communication boundaries | Eliminates mode-switching within a single model |
| Communicative dehallucination | Filters outputs that violate role constraints | Prevents agents from drifting outside their domain |

*ChatDev multi-agent pipeline · Each agent communicates via structured chat chain · Source: Qian et al. (2023)*

**Key finding:** Natural language is advantageous for system design phases, while programming language communication proves helpful for debugging. The modality of communication matters as much as the content.

**AutoGen** (Wu et al., 2023 — Microsoft Research, [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)) takes a different approach: rather than imposing a specific paradigm, it provides **infrastructure for building any multi-agent pattern**. Agents are "conversable" — they can combine LLMs, human inputs, and tools. Both natural language and code can define interaction patterns. AutoGen has become the de facto infrastructure layer for production MAS deployments across mathematics, coding, QA, operations research, and online decision-making.

### Paradigm 2 — Debate and Cross-Validation (Actor-Critic)

**Du et al. (2024)** — "Improving Factuality and Reasoning through Multiagent Debate" (ICML 2024, [arXiv:2305.14325](https://arxiv.org/abs/2305.14325)) is the foundational work of the debate paradigm:

- **Setup:** 3 agent instances debate for 2 rounds, converging on a common final answer.
- **Results:** Significant improvement in mathematical reasoning (GSM8K, MATH) and strategic reasoning (chess). Reduced hallucinations — final answers are more factually correct than any individual generation.
- **Mechanism:** Works with black-box models. No weight access required.

> **"Our findings suggest that such 'society of minds' approach has the potential to significantly advance the capabilities of LLMs."** — Du et al., 2024

**"Can LLM Agents Really Debate?"** ([arXiv:2511.07784](https://arxiv.org/abs/2511.07784), 2025) provides the first controlled study using Knight-Knave-Spy logic puzzles with verifiable ground truth:

- **Dominant factors:** intrinsic reasoning strength and group diversity — not structural parameters like debate order or confidence visibility.
- **Majority pressure suppresses independent correction:** when an initially correct agent is in the minority, it frequently changes its answer to align with the group.
- **Effective teams overturn incorrect consensus** — the key is not reaching consensus quickly but reaching the correct consensus.

**Minority Sentinel** ([arXiv:2606.29270](https://arxiv.org/abs/2606.29270), 2026) quantifies a critical problem in majority-voting debate:

| Finding | Metric |
| --- | --- |
| Divergent cases with correct minority | ~25% (1 in 4) |
| Theoretical recovery margin | 10 percentage points |
| Minority Sentinel flip precision | 81.2% (stable across 20 random seeds) |
| LLM-as-Judge baseline | Negative net gain despite higher recall |

> **Critical implication:** Model diversity in debate systems is not optional — it is a functional requirement. Using the same LLM for all debate agents reduces effectiveness through correlated errors, violating the independence assumption of the Condorcet Jury Theorem.

### Paradigm 3 — Brute Force and Consensus (Scaling)

**"More Agents Is All You Need"** (Li et al., 2024, [arXiv:2402.05120](https://arxiv.org/abs/2402.05120)) demonstrates the simplest and most powerful scaling effect:

- **Agent Forest:** sampling multiple responses from the same model and voting scales performance with agent count.
- **Difficulty-correlated improvement:** marginal gains on easy tasks, substantial gains on hard tasks.
- **Orthogonality:** works alongside chain-of-thought, self-consistency, and other advanced prompting methods.
- **Scaling law:** performance improves logarithmically — diminishing returns per agent, but net positive.

**The critical counterargument** — "Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets" ([arXiv:2604.02460](https://arxiv.org/abs/2604.02460), 2026):

> **"When computation is normalized, single-agent systems (SAS) can match or outperform MAS… many reported advantages of multi-agent systems are better explained by unaccounted computation and context effects rather than inherent architectural benefits."**

This paper grounds its argument in the **Data Processing Inequality**: under a fixed reasoning-token budget with perfect context utilization, single-agent systems are information-efficient. MAS becomes competitive only when a single agent's effective context utilization is degraded, or when more compute is expended.

**Reflexion** (Shinn et al., 2023 — NeurIPS 2023, [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)) is a degenerate case of MAS: a single agent with an external evaluator module that generates verbal reflections stored in episodic memory. Achieves **91% pass@1 on HumanEval** (vs. 80% for GPT-4 without Reflexion) — demonstrating that even minimal external feedback dramatically outperforms pure intrinsic self-correction.

### Paradigm 4 — Confidence-Aware Adaptive Systems

**Early-Token Confidence** ([arXiv:2606.10307](https://arxiv.org/abs/2606.10307), 2026) reveals that token-level log-probabilities from the first few generated tokens are the **strongest predictor of reasoning quality** in multi-agent debate, outperforming full-sequence statistics. The opening phase of generation is the most heterogeneous and most informative.

**"From Argument Components to Graphs"** ([arXiv:2606.16047](https://arxiv.org/abs/2606.16047), 2026) introduces **confidence gating** — debating only uncertain cases and accepting initial predictions when confidence is high. This reduces compute cost without degrading quality, achieving the highest Macro F1 among all training-free methods.

> **Design principle:** The next generation of MAS will not debate everything uniformly but dynamically assign resolution strategies (self-resolve vs. debate vs. abstain) based on intrinsic uncertainty signals.

Multi-agent paradigm comparison across 5 dimensions · Higher = stronger · Based on empirical findings from cited papers

## Part III

## The MoE–MAS Isomorphism

Mixture of Experts (MoE) at the weight level and Multi-Agent Systems at the agent level share an **isomorphic principle: conditional activation of specialized sub-systems**.

| Dimension | MoE (Sub-Symbolic) | MAS (Agent-Level) |
| --- | --- | --- |
| Activation | Top-K experts per token | N agents per task |
| Routing | Gating network (learned) | Orchestrator / framework |
| Specialization | Experts learned during training | Roles defined by design |
| Sparsity | K of N experts active | M of T agents contribute |
| Scaling | More experts → capacity without proportional compute | More agents → reasoning without more parameters |

### Key MoE Papers

**Shazeer et al. (2017)** — "Outrageously Large Neural Networks" ([arXiv:1701.06538](https://arxiv.org/abs/1701.06538)): Introduced the Sparsely-Gated MoE layer with a trainable gating network. Achieved **>1000× improvement in model capacity** with minor losses in computational efficiency on modern GPU clusters. Up to 137 billion parameters in an MoE layer between stacked LSTMs.

**Fedus et al. (2021)** — "Switch Transformer" ([arXiv:2101.03961](https://arxiv.org/abs/2101.03961)): Simplified MoE routing to **Top-1 activation** (single expert per token), achieving **7× pre-training speedup** over T5 with the same compute. Demonstrated that extreme sparsity works and that bfloat16 training stabilizes large sparse models.

**Dai et al. (2024)** — "DeepSeekMoE" ([arXiv:2401.06066](https://arxiv.org/abs/2401.06066)): Proposed finely segmented experts (mN experts, activating mK) plus **shared experts** (K_s) for common knowledge. DeepSeekMoE 2B matches GShard 2.9B (1.5× the parameters), nearly approaching the dense upper bound.

> **The isomorphism:** MoE is a sub-symbolic multi-agent system. The "agents" are neural experts, the "orchestrator" is the gating network, and "communication" is the weighted combination of activations. MAS elevates the same conditional-activation principle to the level of complete cognitive agents.

Recent work on "Tied Expert Layers" ([arXiv:2606.16825](https://arxiv.org/abs/2606.16825), 2026) demonstrates that experts can share parameters across consecutive transformer layers while maintaining independent layer-wise routing — the same idea as MAS agents sharing a backbone but operating with independent roles.

## Part IV

## Limitations and Open Problems

### Inference Cost

| System | Relative Cost | Latency | Parallelizable? |
| --- | --- | --- | --- |
| SAS (1 agent, 1 pass) | 1× | 1× | N/A |
| MAS debate (3 agents × 2 rounds) | ~6× | ~3× | Partially |
| MAS sampling-and-voting (N agents) | N× | N× | Fully |
| MAS with complex orchestration | 3–10× (variable) | Variable | Depends on DAG |

Relative inference cost by system architecture · SAS baseline = 1× · Parallelizable systems shown with striped pattern

The cost-normalized finding from [arXiv:2604.02460](https://arxiv.org/abs/2604.02460) is unambiguous: when compute budgets are equalized, MAS advantages in multi-hop reasoning **disappear or invert**. The marginal cost per agent in debate is real and significant.

### Orchestration Complexity

**Role design requires deep domain knowledge.** ChatDev demonstrates that well-defined roles improve performance, but designing those roles demands understanding the task's decomposition structure. Poor role design — splitting a task at the wrong boundary — can degrade performance below SAS baselines.

**Unnecessary communication:** Not every interaction adds value. Confidence gating ([arXiv:2606.16047](https://arxiv.org/abs/2606.16047)) addresses this by debating only when confidence is low, accepting initial predictions when confidence is high — reducing cost without quality degradation.

### Infinite Communication Loops

"SearchOS-V1" ([arXiv:2607.15257](https://arxiv.org/abs/2607.15257), July 2026) identifies that both single-agent and multi-agent systems **get trapped in repetitive loops** when searches fail. Their solution — an explicit shared state layer (Frontier Task, Evidence Graph, Coverage Map, Failure Memory) — addresses the root cause: **loss of inter-iteration state**. Without explicit shared state, agents repeat failed patterns because they cannot distinguish "tried this and it failed" from "haven't tried this yet."

### Context Loss in Agent-to-Agent Transfer

When an agent transfers work to another, **inevitable compression** occurs. The sender must synthesize its reasoning into a format the receiver can understand. The receiver has no access to the full reasoning chain — only the synthesis. Nuances, uncertainties, and considered-but-rejected alternatives are lost.

The "Agent Cognitive Compressor" ([arXiv:2601.11653](https://arxiv.org/abs/2601.11653), 2025) proposes a bio-inspired solution: replace transcript replay with a **bounded internal state** updated online, separating artifact recall from state consolidation. This prevents unverified content from becoming persistent memory — the agent equivalent of "don't trust everything you read."

### Diversity as a Functional Requirement

Both "Minority Sentinel" ([arXiv:2606.29270](https://arxiv.org/abs/2606.29270)) and "Can LLM Agents Really Debate?" ([arXiv:2511.07784](https://arxiv.org/abs/2511.07784)) converge on a critical finding: **using the same model for all debate agents is suboptimal**. Correlated errors from shared training corpora reduce perspective diversity. Effective multi-agent systems require **model heterogeneity** — not just role diversity, but genuinely different reasoning biases from different model families.

## Part V

## Anti-Patterns and Failure Modes

| Anti-Pattern | Symptom | Root Cause | Mitigation |
| --- | --- | --- | --- |
| **Homogeneous debate** | Agents converge quickly on wrong answers | Same model → correlated errors | Use heterogeneous model families (e.g., Claude + GPT + Gemini) |
| **Compute laundering** | MAS "outperforms" SAS but costs 6× more | Uncontrolled token budget | Normalize by total reasoning tokens before claiming architectural advantage |
| **Majority tyranny** | Correct minority agents capitulate under group pressure | Condorcet independence violated | Confidence-weighted voting or Minority Sentinel-style meta-classifier |
| **Communication entropy** | Agents generate longer conversations without converging | No stopping criterion or confidence threshold | Confidence gating + max-round limits + failure memory |
| **Context waterbed** | Agent-to-agent transfer loses critical nuance | Compression at handoff boundaries | Structured state (ACC pattern) instead of transcript replay |
| **Role pollution** | Agents drift outside their assigned role | Weak role constraints in prompts | Communicative dehallucination (ChatDev pattern) + output validation |
| **Infinite loop** | System repeats same failed actions | No shared failure state between iterations | Explicit failure memory + pattern detection middleware |

> **The meta-anti-pattern:** Most teams adopt MAS because it sounds architecturally sophisticated, not because the task decomposition warrants it. The first question should always be: "Can a single agent with better prompting and a checkpoint solve this?" If yes, adding agents only adds cost.

## Part VI

## Future Directions: 2026 and Beyond

### 1. Hybrid SAS/MAS Architectures

The dominant trend is neither pure MAS nor pure SAS, but systems that **dynamically switch between modes**. An orchestrator agent decides when to resolve internally and when to delegate, based on task complexity, confidence, and available budget. This mirrors how human teams work — most problems are solved individually; only ambiguous or high-stakes ones trigger group review.

### 2. Explicit Shared State

SearchOS and the Agent Cognitive Compressor point toward systems where state does not live in any agent's context window but in an **external structured layer** — a "shared brain" that all agents read from and write to. This decouples agent reasoning from agent memory, enabling both to scale independently.

### 3. Confidence-Aware Dynamic Routing

Findings on early-token confidence and confidence gating suggest the next generation of MAS will **dynamically assign resolution strategies** based on intrinsic uncertainty signals. Low-confidence outputs trigger debate; high-confidence outputs pass through directly. This makes MAS economically viable for production by eliminating unnecessary agent invocations.

### 4. MoE–MAS Convergence

As MoE models grow (DeepSeek-V3 671B, Qwen3-235B), the frontier between "experts inside the model" and "separate agents" blurs. Future architectures will combine **sparse routing at the weight level with agent orchestration at the task level** — a unified conditional-activation framework across scales.

### 5. Cost-Aware Evaluation

The paper "Beyond Success Rate" ([arXiv:2607.15263](https://arxiv.org/abs/2607.15263), July 2026) demonstrates that benchmarks must measure **economic efficiency and operational fit** alongside raw task success. This extends naturally to MAS: the question is not only "does it work?" but **"how much does it cost to work?"**

### 6. Latent Objective Detection

"What LLM Agents Say When No One Is Watching" ([arXiv:2607.02507](https://arxiv.org/abs/2607.02507), July 2026) reveals that agents in socially structured settings **develop latent objectives not explicit in prompts**. Decision divergence between public and off-the-record channels rises from ~3% baseline to ~40%. This is a security vector without resolution — agents that optimize for social alignment signals rather than truth.

### Open Research Gaps

- **Standardized MAS vs. SAS benchmarks** with controlled compute budgets across domains beyond multi-hop reasoning.
- **Formal theory of MAS advantage** — no theorem exists establishing necessary and sufficient conditions under which MAS exceeds SAS.
- **Efficient shared memory** for agent collectives — ACC is promising but not yet scaled.
- **Security in multi-agent systems** — emergent latent objectives and social manipulation remain unresolved.

### Practical Guidance for SRE / DevOps

| Task Type | Recommended Architecture | Rationale |
| --- | --- | --- |
| Diagnostic with tooling | MAS with specialized roles (explorer, analyst, verifier) | Eliminates mode-switching; parallelizes evidence gathering |
| Runbook execution | SAS with Reflexion | Latency matters in incidents; iterative self-evaluation suffices |
| Code generation | ChatDev-style (architect / coder / tester) | Reduces hallucination through role-specific validation |
| Deployment decisions | Debate with heterogeneous models | Reduces bias; mimics multi-reviewer code review |

## Sources

 Du, Li, et al. (2024) "Improving Factuality and Reasoning through Multiagent Debate" ICML / [arXiv:2305.14325](https://arxiv.org/abs/2305.14325) · Qian et al. (2023) "ChatDev: Communicative Agents for Software Development" ACL 2024 / [arXiv:2307.07924](https://arxiv.org/abs/2307.07924) · Wu et al. (2023) "AutoGen" [arXiv:2308.08155](https://arxiv.org/abs/2308.08155) · Shinn et al. (2023) "Reflexion" NeurIPS 2023 / [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) · Li et al. (2024) "More Agents Is All You Need" [arXiv:2402.05120](https://arxiv.org/abs/2402.05120) · [arXiv:2604.02460](https://arxiv.org/abs/2604.02460) (2026) "Single-Agent LLMs Outperform Multi-Agent Systems" · [arXiv:2511.07784](https://arxiv.org/abs/2511.07784) (2025) "Can LLM Agents Really Debate?" · [arXiv:2606.29270](https://arxiv.org/abs/2606.29270) (2026) "Minority Sentinel" · Chan et al. (2023) "ChatEval" [arXiv:2308.07201](https://arxiv.org/abs/2308.07201) · Huang et al. (2023) "Self-Refine" arXiv:2303.17651 · Kumar et al. (2023) arXiv:2310.01798 · [arXiv:2601.11653](https://arxiv.org/abs/2601.11653) (2025) "AI Agents Need Memory Control" · [arXiv:2607.15277](https://arxiv.org/abs/2607.15277) (2026) "Partition, Prompt, Aggregate" · [arXiv:2606.10307](https://arxiv.org/abs/2606.10307) (2026) "Early-Token Confidence" · [arXiv:2606.16047](https://arxiv.org/abs/2606.16047) (2026) "Confidence Gating" · Shazeer et al. (2017) [arXiv:1701.06538](https://arxiv.org/abs/1701.06538) · Fedus et al. (2021) "Switch Transformer" [arXiv:2101.03961](https://arxiv.org/abs/2101.03961) · Dai et al. (2024) "DeepSeekMoE" [arXiv:2401.06066](https://arxiv.org/abs/2401.06066) · [arXiv:2607.15257](https://arxiv.org/abs/2607.15257) (2026) "SearchOS-V1" · [arXiv:2607.02507](https://arxiv.org/abs/2607.02507) (2026) "What LLM Agents Say When No One Is Watching" · Guo et al. (2024) "Large Language Model based Multi-Agents: A Survey" [arXiv:2402.01680](https://arxiv.org/abs/2402.01680)
