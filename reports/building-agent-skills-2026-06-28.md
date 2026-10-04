---
title: "Building Agent Skills in 2026: Progressive Disclosure as a Design Pattern"
date: 2026-06-28
type: special
url: https://luisgonzalezbernal.com/reports/reports/building-agent-skills-2026-06-28.html
summary: "What a Skill is · Skills vs. tools · The three-tier disclosure model · How to author one · The context-tax discipline · Security"
tags: [agents, security]
reading_time_minutes: 7
---
Agent Engineering · Special Report

# Building *Agent Skills* in 2026: Progressive Disclosure as a Design Pattern

28 Jun 2026

What a Skill is · Skills vs. tools · The three-tier disclosure model · How to author one · The context-tax discipline · Security

## Executive Summary

In December 2025 Anthropic released the **SKILL.md** format; within weeks OpenAI, Google, GitHub and Cursor adopted it. That speed is the story: agent **Skills** became the first mainstream, cross-vendor implementation of **progressive disclosure** — the discipline of loading the right context at the right moment instead of stuffing everything into the prompt.

A Skill is deceptively simple — a folder with a markdown file (YAML frontmatter + instructions) plus optional scripts, templates and data. The depth is in *how it loads*: the agent reads only a Skill's name and description at startup (~80 tokens median), pulls in the full body (275–8,000 tokens) only when it's relevant, and touches scripts/references only during execution. That tiering is what makes a library of dozens of capabilities feasible without drowning the context window.

This report covers what Skills are, how they differ from tools, the disclosure model, a battle-tested authoring process, and the operational discipline (the "context tax") that separates a useful Skill library from an expensive one.

## Part I

## What a Skill Is — and Isn't

A Skill packages **instructions, metadata and optional resources** (scripts, templates) that an agent invokes automatically when relevant. Concretely, it's a directory containing a `SKILL.md` with YAML frontmatter and markdown, plus anything else the task needs.

The crucial conceptual move is **Skills vs. Tools**:

|  | Tool | Skill |
| --- | --- | --- |
| **What it does** | Executes an action and returns a result | Injects procedural knowledge & modifies how the agent works |
| **Shape** | A function with a schema | A folder of instructions + resources |
| **Effect on context** | Adds a result to context | Enables progressive disclosure of know-how |
| **Analogy** | A power tool | The craftsman's playbook for using it |

> *📌 Takeaway:* Tools let an agent *do* things; Skills teach it *how and when*. A skill is "just markdown," but the folder can carry scripts, templates, data and images — the agent reads them, runs them, and uses them to do real work.

### Why it standardized so fast

A universal, plain-text, vendor-neutral format (SKILL.md) made Skills portable across agents overnight. By March 2026 the ecosystem spanned official, verified third-party, and thousands of community Skills — all on the same format.

Sources: [Agent Skills — Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) [Progressive Disclosure as a Pattern](https://www.newsletter.swirlai.com/p/agent-skills-progressive-disclosure)

## Part II

## The Three-Tier Disclosure Model

Progressive disclosure loads information in tiers by relevance. This is the engine that makes Skills scale:

| Tier | Loaded when | What loads | Token cost |
| --- | --- | --- | --- |
| **1. Discovery** | Always (startup) | Name + description only | ~80 tokens median / skill |
| **2. Activation** | When the model judges it relevant | Full instruction body | 275–8,000 tokens |
| **3. Execution** | Only during the task | Scripts, templates, reference files | On demand |

The payoff: an agent can carry a **lightweight index** of many capabilities and pay the full cost of only the one it actually uses. Models also simply *perform better* when they get relevant information at the right moment — which is why context engineering is now considered as critical as prompt engineering.

### Design implication

Your Skill's **description** is the most important line you write — it's the only thing the agent sees until activation. A vague description means the Skill never triggers; a precise, trigger-rich one means it fires exactly when needed.

Sources: [Progressive Disclosure in Skill Design](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agent-skill-design) [State of Context Engineering 2026](https://www.newsletter.swirlai.com/p/state-of-context-engineering-in-2026)

## Part III

## How to Author a Skill That Actually Triggers

The most effective authoring loop documented in 2026 is **Claude-to-Claude development**: one instance ("Claude A") helps you design and refine the Skill; another instance ("Claude B"), with the Skill loaded, tests it on real tasks. You watch where B struggles, succeeds, or makes unexpected choices, and feed that back to A.

The repeatable recipe:

1. **Do the task without a Skill first.** As you work, you naturally supply context, preferences and procedure — notice what you provide *repeatedly*.
2. **Extract the reusable pattern** from that repeated context. That pattern is the Skill.
3. **Write a precise, trigger-rich description** (Tier 1) so the agent discovers it at the right time.
4. **Keep the body concise and well-structured** (Tier 2); push scripts, long references and templates into separate files (Tier 3).
5. **Test with real tasks, not test scenarios** (Claude B). Iterate on actual failure modes.

> *⚠️ Common failure:* authoring from imagination instead of from real, repeated work. Skills written for hypothetical scenarios are either never triggered or over-broad. The strongest Skills are crystallized from tasks you've actually done by hand.

### Structure for disclosure

A good Skill front-loads the "when to use me" in the description, keeps the body lean and procedural, and offloads heavy material (reference docs, code, datasets) to files the agent only reads at execution time. Design the file layout around the three tiers, not around documentation neatness.

Sources: [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) [Complete Guide to Building Skills](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

## Part IV

## The Context Tax — Operating a Skill Library

Skills are not free even when unused: every loaded Skill's Tier-1 index consumes tokens whether it helps or not. The 2026 rule of thumb is blunt:

- **8–12 well-chosen Skills** cover most of a senior developer's day.
- Beyond that, you start **paying context tax** — index bloat that crowds out useful context and can degrade triggering accuracy.
- Run a **monthly skill audit**: delete anything you haven't triggered in 30 days.

Treat a Skill library like a dependency list, not a junk drawer. More Skills is not more capability past the point where the index noise makes the agent worse at choosing.

### The discipline

Curate ruthlessly. A small library of sharp, well-described, real-task Skills beats a large one of speculative ones — both for token cost and for the agent's ability to pick the right Skill at the right moment.

Sources: [10 Must-Have Skills (and the audit rule)](https://medium.com/engineering-playbook/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-0bb577fbb440) [9 Tips for Building Skills](https://medium.com/@tahirbalarabe2/9-tips-for-building-claude-agent-skills-3bca85c47a26)

## Part V

## Security — The Part People Skip

Because a Skill can ship **executable scripts** that the agent will run, a Skill is also an **attack surface**. The same properties that make Skills powerful (auto-discovery, code execution, third-party sharing) make a malicious or compromised Skill dangerous. Research in 2026 explicitly frames Skill architecture alongside **acquisition and security** as co-equal concerns.

- **Provenance:** treat third-party Skills like dependencies — review the scripts before installing.
- **Least privilege:** a Skill should only reach the tools and data its task needs.
- **Auditability:** know which Skill ran, when, and what it executed.

> *📌 Bottom line:* "It's just markdown" is true until the markdown points at a script. Govern Skill acquisition the way you govern packages.

### Where this is heading

Skills sit alongside memory and protocols (like MCP) as the externalized building blocks of agent systems — the durable knowledge and capability layer that outlives any single model. Expect Skill registries, signing/verification, and capability scoping to mature next.

Sources: [Agent Skills: Architecture, Acquisition, Security](https://arxiv.org/html/2602.12430v3) [Externalization in LLM Agents](https://arxiv.org/pdf/2604.08224)

## In Numbers

-  Tier-1 index cost / skill (median) **~80 tok**

-  Tier-2 body when activated **275–8K tok**

-  Sweet spot for a daily library **8–12**

-  Audit cadence (delete if untriggered) **30 days**

## Watch

-   SKILL.md stays the cross-vendor standard; registries and signing emerge next

-   Skill descriptions become the highest-leverage thing you write (Tier-1 discovery)

-   Context tax pushes teams toward small, audited libraries over sprawling ones

-   Skill security (provenance, least privilege) becomes a real governance topic

 Sources: Agent Skills — Claude Platform Docs (platform.claude.com) · Skill Authoring Best Practices (platform.claude.com) · The Complete Guide to Building Skills (resources.anthropic.com) · Agent Skills: Progressive Disclosure (swirlai.com) · State of Context Engineering 2026 (swirlai.com) · Progressive Disclosure in Skill Design (mindstudio.ai) · 9 Tips for Building Skills (medium.com) · 10 Must-Have Skills + audit rule (medium.com) · Agent Skills: Architecture, Acquisition, Security (arXiv:2602.12430) · Externalization in LLM Agents (arXiv:2604.08224)
