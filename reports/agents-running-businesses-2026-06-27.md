---
title: "Can Agents Run a Business? What the Evidence Shows"
date: 2026-06-27
type: special
url: https://luisgonzalezbernal.com/reports/reports/agents-running-businesses-2026-06-27.html
summary: "Agents given a business to run · Results in support and operations · How business agents are built · Reliability over long horizons · Why projects fail"
tags: [agents, research]
reading_time_minutes: 10
---
Autonomous Business Agents · Special Report

# Can Agents Run a *Business*? What the Evidence Shows

27 Jun 2026 · Updated 7 Oct 2026

Agents given a business to run · Results in support and operations · How business agents are built · Reliability over long horizons · Why projects fail

## Key findings

1. **Given a whole business, agents mostly lose money.** In a simulated market of eight companies over 500 days, most LLM CEO agents had negative mean returns.[11] In a marketplace benchmark, even the best of 15 models fell behind human-designed strategies.[12]
2. **Narrow support work already pays.** At Nubank, A/B tests of a card-delivery agent showed a 37-point gain in transactional NPS and a 29-point gain in self-service.[5] On most use cases, AI satisfaction came within a few points of expert human agents.[5]
3. **Building a business agent is still hard for agents.** Asked to deliver a customer-service agent for a client, the best configuration passed 23.9% of simulations.[14] An expert reference reached 82.2%.[14]
4. **Long horizons break agents.** On long terminal tasks, the best of 15 models passed 15.2%, and the mean was 4.3%.[23] Frontier models had the highest meltdown rates, up to 19%.[6]
5. **Leaderboards measure the wrong thing.** Across three enterprise benchmarks, the agent explained less than 3% of the variance in results; the agent-task fit explained 7-23%.[27]
6. **Many projects will be cancelled.** Gartner predicts that over 40% of agentic AI projects will be cancelled by the end of 2027.[34] The reasons are cost, unclear value and weak risk controls.[34]

## Part I

## What happens when an agent runs a business

Researchers now give agents whole businesses in simulation. The results are poor and highly variable.

Vending-Bench asks an agent to run a vending machine: stock, orders, prices and daily fees, over more than 20M tokens per run.[22] Claude 3.5 Sonnet and o3-mini made a profit in most runs.[22] But every model had runs that derailed. Agents misread delivery schedules, forgot orders or fell into "meltdown" loops.[22] The failures did not correlate with a full context window.[22]

Harder tests give worse results. Business Arena runs a cross-border shop on real alibaba.com sourcing data.[12] Across 15 frontier models, final net worth varied ninefold.[12] In CEO Arena, eight LLM CEOs competed in a shared market for 500 simulated days. Most had negative mean returns, and private gains could come with market losses.[11] In EcoGym, no single model led in all three economies.[26]

Office work shows the same split. In TheAgentCompany, a simulated software company, the best agent completed 30% of tasks on its own.[29] Many simple tasks were solved; difficult long-horizon tasks were not.[29]

Simulated economies of agents also behave oddly. In a town of 100 agents, a 12x demand shock raised business revenue 4.62x.[16] Wages barely moved, and only 0.3% of 3,981 menu items were ever repriced.[16] Swapping the LLM changed every outcome; deleting the agents' memory changed none detectably.[16]

*[Evidence by level of autonomy: narrow support pays, workflows with human gates work in pilots, whole businesses fail in simulation]*

*What the evidence shows at each level of autonomy. Sources 5, 19, 31, 15, 11 and 12.*

## Part II

## Results in support and operations

The strongest results come from narrow deployments with measurement built in.

| Deployment | Measured result |
| --- | --- |
| Nubank, five support use cases | +37 points transactional NPS and +29 points self-service in card delivery[5] |
| OlaMind, customer service | +23.67% issue resolution and -6.6% human transfers in online A/B tests[19] |
| Global bank, three workflows | 88% citation precision and 1.6% hallucination in credit memos; analyst effort from 27.4 to 2.9 hours per document[31] |
| Vigil, ByteDance cloud on-call support | Deployed for over ten months alongside human analysts[20] |

The Nubank team draws one lesson above the rest: the quality of the evaluation pipeline sets the speed of iteration.[5] Its offline simulation metrics correlated with online outcomes.[5] Vigil takes a different role. It assists after a human has taken over, and it learns from cases that humans resolve.[20]

## Part III

## How business agents are built

The designs that work keep the agent inside explicit limits. One rule appears in practice: the LLM decides what should happen, and deterministic code decides what is allowed.[36]

Agentic ERP is a good example. Role-aligned agents run end-to-end workflows on a production ERP backend, under a human-in-the-loop harness tiered by risk.[15] A Planner, Executor, Reflector and Responder separate generation from evaluation.[15] In a simulated year, it had zero stockouts, while the rule-based baseline had hundreds.[15]

Governance is part of the architecture. Queen-Bee compiles a task specification that specialized agents run with constrained tool access.[8] On 59 enterprise-style tasks, it reached 0.964 task success with zero governance failures.[8] The authors call this prototype evidence, not a production study.[8] A healthcare company runs nine autonomous agents behind four layers of defense: kernel isolation, credential proxies, egress allowlists and labels on untrusted content.[3]

Topology matters as much as the model. In fault-injection tests, iterative closed-loop designs neutralized over 40% of the faults that collapsed linear workflows.[1] Stronger foundation models did not improve robustness uniformly.[1]

## Part IV

## Reliability over long horizons

- **15.2%** best pass rate on long terminal tasks; the mean across 15 models was 4.3%

Long-Horizon-Terminal-Bench[23]

- **19%** meltdown rate for frontier models, the highest of all tiers

10 models, 23,392 episodes[6]

- **13.8%** of rollouts showed reward hacking on ultra-long software tasks

SWE-Marathon[9]

Agents now complete short, well-specified tasks on their own.[23] Long tasks are a different matter. Frontier coding agents solve fewer than 30% of SWE-Marathon tasks.[9] The common failures are poor self-verification, claims that the task is infeasible, and stopping too early.[9]

Reliability is not the same as capability. Capability and reliability rankings diverge at long horizons.[6] Frontier models melt down most because they try ambitious multi-step strategies.[6] Decay also depends on the domain: in software engineering, one degradation score fell from 0.90 to 0.44, while document processing stayed nearly flat.[6]

Evaluations themselves can mislead. Designs that look most reliable in training replicate worst on held-out tasks.[27] The same agent can succeed in one run and fail in the next with identical inputs.[28] One fix is training on critiques: it beat GPT-OSS-120B by over 10% pass^4 on retail tasks.[4]

## Part V

## Why projects fail

Gartner calls most agentic AI projects early experiments, mostly driven by hype and often misapplied.[34] An enterprise evaluation framework frames the problem as measurement. Public benchmarks ask what a model can do. A deployment decision asks whether a workflow is fit, reliable, safe and worth scaling on local data.[31]

Multi-agent systems fail in recognizable ways. A taxonomy built from over 1,600 traces finds 14 failure modes in 3 groups: system design, inter-agent misalignment and task verification.[17] Their gains on popular benchmarks are often minimal.[17] Because agents coordinate in natural language, errors spread silently without raising exceptions.[1]

Some errors cannot be undone. Refunding the wrong purchase is a single action that causes irreversible failure, so it must be stopped before it runs.[4] Security adds risk. Agents with memory can be turned into persistent "zombies" through poisoned web content, and per-session prompt filters do not stop it.[24] Voice agents can perform the actions of common scams on their own.[13]

Security numbers need care too. One audit re-scored the same traces with a corrected harness. The reported attack success fell from 21.7% to 1.2%.[18]

## What I would do

1. **Do not hand an agent the whole business.** Pick one narrow workflow with a clear outcome, such as one support use case.
2. **Build the evaluation before the agent.** Offline simulations that predict online results are what make iteration fast.
3. **Keep the rules in code.** Let the model propose. Let deterministic code and a risk-tiered approval decide what runs.
4. **Stop irreversible actions before they happen.** Refunds, payments and record changes go through a check or a person.
5. **Test reliability, not only capability.** Run the same task many times, and watch long runs for meltdowns.
6. **Measure business effect from day one.** If the pilot cannot show value against a gate, stop it early.

*— Luis González*

## Method and limits

This report replaces a June 2026 version that cited no sources. It was rebuilt on 7 October 2026 with the reports research pipeline. The pipeline found 150 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar. It read 40 sources in full, and 39 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 264 claims, each with a verbatim quote, and none had to be discarded. Claude wrote the synthesis from that evidence and checked every cited figure against its source. The conclusions in "What I would do" are mine.

- **No general web search.** The run had no web-search key. Company case studies and press coverage are missing, including Klarna and Anthropic's Project Vend. Figures in the earlier version about them had no source and were removed.
- **Mostly simulations.** Most evidence on whole-business autonomy comes from simulated markets, not real companies.
- **Preprints.** Most papers are arXiv preprints, not peer-reviewed. Their figures are as reported and were not reproduced.

## Sources

1. MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems — Jia et al., arXiv, Feb 2026 — [arxiv.org/abs/2602.19843](https://arxiv.org/abs/2602.19843)
2. Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare — Maiti, arXiv, Mar 2026 — [arxiv.org/abs/2603.17419](https://arxiv.org/abs/2603.17419)
3. CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents — Saeidi et al., arXiv, Aug 2026 — [arxiv.org/abs/2608.30147](https://arxiv.org/abs/2608.30147)
4. Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework — Gupta et al., arXiv, 2026 — [arxiv.org/abs/2606.08867](https://arxiv.org/abs/2606.08867)
5. Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents — Khanal, Tao, Zhou, arXiv, Mar 2026 — [arxiv.org/abs/2603.29231](https://arxiv.org/abs/2603.29231)
6. Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration — Zhang, Liaotian, arXiv, Jun 2026 — [arxiv.org/abs/2606.06545](https://arxiv.org/abs/2606.06545)
7. SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work? — Desai et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.07682](https://arxiv.org/abs/2606.07682)
8. CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets — Yan et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.34821](https://arxiv.org/abs/2609.34821)
9. Business Arena: Benchmarking LLM Agents in a Realistic Marketplace — Pan et al., arXiv, Aug 2026 — [arxiv.org/abs/2608.08621](https://arxiv.org/abs/2608.08621)
10. Voice-Enabled AI Agents can Perform Common Scams — Fang, Bowman, Kang, arXiv, Oct 2024 — [arxiv.org/abs/2410.15650](https://arxiv.org/abs/2410.15650)
11. τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction — Shi et al., arXiv, Sep 2026 — [arxiv.org/abs/2609.04611](https://arxiv.org/abs/2609.04611)
12. Agentic ERP: Multi-Agent Large Language Model Architecture for Autonomous Enterprise Resource Planning — Liu et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.17331](https://arxiv.org/abs/2607.17331)
13. But How Would AI Agents Run a Town's Economy? — Regmi, Pudasaini, Pun, arXiv, Sep 2026 — [arxiv.org/abs/2609.11108](https://arxiv.org/abs/2609.11108)
14. Why Do Multi-Agent LLM Systems Fail? — Cemri et al., arXiv, 2025 — [arxiv.org/abs/2503.13657](https://arxiv.org/abs/2503.13657)
15. Silent Failures in Agentic Security Evaluation — Shaw, arXiv, Sep 2026 — [arxiv.org/abs/2609.32691](https://arxiv.org/abs/2609.32691)
16. Benchmarking and Learning Real-World Customer Service Dialogue — Gao et al., arXiv, Oct 2025 — [arxiv.org/abs/2510.22143](https://arxiv.org/abs/2510.22143)
17. Help Without Being Asked: A Deployed Proactive Agent System for On-Call Support — Liu, He, Zhang, arXiv, 2026 — [arxiv.org/abs/2604.09579](https://arxiv.org/abs/2604.09579)
18. Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents — Backlund, Petersson, arXiv, Feb 2025 — [arxiv.org/abs/2502.15840](https://arxiv.org/abs/2502.15840)
19. Long-Horizon-Terminal-Bench — Li et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.08964](https://arxiv.org/abs/2607.08964)
20. Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections — Yang et al., arXiv, 2026 — [arxiv.org/abs/2602.15654](https://arxiv.org/abs/2602.15654)
21. EcoGym: Evaluating LLMs for Long-Horizon Plan-and-Execute in Interactive Economies — Hu et al., arXiv, Feb 2026 — [arxiv.org/abs/2602.09514](https://arxiv.org/abs/2602.09514)
22. Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations — Srinivasan, arXiv, Aug 2026 — [arxiv.org/abs/2608.11323](https://arxiv.org/abs/2608.11323)
23. InconLens: Interactive Visual Diagnosis of Behavioral Inconsistencies in LLM-based Agentic Systems — Yan et al., arXiv, Mar 2026 — [arxiv.org/abs/2603.28106](https://arxiv.org/abs/2603.28106)
24. TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks — Xu et al., arXiv, Dec 2024 — [arxiv.org/abs/2412.14161](https://arxiv.org/abs/2412.14161)
25. EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise — Ali, Siddiqui, Zahid, arXiv, Sep 2026 — [arxiv.org/abs/2609.21841](https://arxiv.org/abs/2609.21841)
26. Gartner Predicts over 40% of Agentic AI Projects Will Be Canceled by End of 2027 — Gartner, Jun 2025 — [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
27. enterprise-ai-rag-agent: RAG, memory, tools and deterministic decisioning — GitHub, Oct 2026 — [github.com/Pradeep-1612/enterprise-ai-rag-agent](https://github.com/Pradeep-1612/enterprise-ai-rag-agent)
