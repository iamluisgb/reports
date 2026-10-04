---
title: "Enterprise AI Agent Security — Deep Research Report"
date: 2026-06-02
type: special
url: https://luisgonzalezbernal.com/reports/reports/enterprise-ai-agent-security-2026-06-02.html
summary: "OpenShell, NemoClaw, Hermes Agent, and the new runtime security layer for autonomous agents"
tags: [agents, security, regulation, business]
reading_time_minutes: 13
---
Agent Security · Special Report

# Enterprise AI Agent Security

02 Jun 2026

OpenShell, NemoClaw, Hermes Agent, and the new runtime security layer for autonomous agents

## Executive Summary

In 2026, the enterprise AI agent market crossed an inflection point. OpenClaw became the most-starred software project on GitHub (376K+ stars). Hermes Agent hit 177K stars in under 3 months and became the most-used agent on OpenRouter. But with this adoption came a hard wall: **enterprise IT security**.

The fundamental problem is that autonomous agents — long-running, tool-wielding, file-system-accessible — are exactly the kind of software that keeps security teams awake. They call APIs, write files, run code, execute shell commands, and interact with sensitive infrastructure. A compromised agent is a breach vector.

NVIDIA's response, announced at Computex 2025 and GTC 2026, is the **NVIDIA Agent Toolkit**: a layered security architecture built around **OpenShell**, **NemoClaw**, and partnerships with security leaders like Cisco, CrowdStrike, Google, and Microsoft Security. This is not a single product — it is an ecosystem play that wraps agent runtimes in policy-enforced sandboxes, injects credential management, and integrates with enterprise security stacks at the infrastructure layer.

This report maps the landscape: the architectures, the players, the security models, and which enterprises are deploying what.

## 1. The Problem: Why Agents Need a New Security Model

Unlike traditional SaaS or microservice architectures, autonomous AI agents present **three unique security challenges**:

| Challenge | Description | Traditional Mitigation | Why It Fails |
| --- | --- | --- | --- |
| **Long-lived autonomy** | Agents run 24/7, not request-response. They act on their own initiative. | Auth per request (OAuth, API keys) | An agent might execute 1000+ actions in a session. Per-request auth doesn't scale to agentic loops. |
| **Tool access surface** | Agents call arbitrary APIs, run shell commands, read/write filesystems. | Role-based access control | RBAC assumes known actions. Agents discover and compose actions dynamically. |
| **Data exfiltration risk** | Agents process sensitive data. Output channels (code, files, network) are attack vectors. | DLP policies, egress filters | DLP at the network layer can't distinguish between legitimate agent output and exfiltration. |

The industry's answer: move security to the **runtime layer**, not the application layer. A containerized sandbox with policy-enforced egress, credential injection, and audit trails — deployed *around* the agent, not *inside* it.

## 2. NVIDIA OpenShell — The Agent Runtime Security Layer

**OpenShell** ([github.com/NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)) is an open-source runtime that wraps AI agents in a policy-enforced sandbox. In NVIDIA's words: *"the safe, private runtime for autonomous AI agents."* It is currently in alpha (single-player mode) but is clearly positioned as the foundational security layer for the agent ecosystem.

### Architecture

OpenShell has four architectural components:

| Component | Role |
| --- | --- |
| **Gateway** | Control-plane API that coordinates sandbox lifecycle and acts as the auth boundary. Routes inference requests, manages sandbox creation/destruction. |
| **Sandbox** | Isolated runtime (Docker/Podman/MicroVM/Kubernetes) with container supervision. Each sandbox runs a complete agent environment with CLI tools (Python, Node, git, gh, networking utilities). |
| **Policy Engine** | Enforces filesystem, network, and process constraints via declarative YAML policies. Operates from the application layer down to the kernel. Blocks unauthorized file access, data exfiltration, and uncontrolled network activity. |
| **Privacy Router** | Privacy-aware LLM routing. Strips caller credentials from outbound requests, injects backend credentials, and forwards to the managed model. Sensitive context stays on sandbox compute. |

### How the Policy Engine Works

Every outbound connection from the sandbox is intercepted by the policy engine, which does exactly one of three things:

1. **Allows** — the destination and binary match a policy block. Traffic passes through.
2. **Routes for inference** — strips caller credentials, injects backend credentials, forwards to the managed model. No API key leakage.
3. **Denies** — blocks the request and logs it. Policy violations are auditable.

Policies can be hot-reloaded at runtime — the `openshell policy set` command applies a YAML policy file to a running sandbox without restarting anything. Example:L7-enforced access control on API endpoints:

```
# Allow read-only GitHub API access
sandbox$ openshell policy set demo --policy policy.yaml --wait
sandbox$ curl -sS https://api.github.com/zen
Anything added dilutes everything else.
sandbox$ curl -sS -X POST https://api.github.com/repos/.../issues -d '{...}'
{"error":"policy_denied","detail":"POST not permitted by policy"}
```

### Microsoft Security Integration

OpenShell plugs directly into Microsoft's enterprise security stack. NVIDIA is collaborating with Cisco, CrowdStrike, Google, Microsoft Security, and TrendAI to build OpenShell compatibility with their cyber- and AI-security tools. This means OpenShell policies can be authored and enforced through existing enterprise security consoles — the security team doesn't need to learn a new system.

## 3. NVIDIA NemoClaw — Deploying Secure Agents in One Command

**NemoClaw** is NVIDIA's reference implementation for deploying secure autonomous agents. It's both a blueprint and a turnkey solution: a single shell command deploys OpenClaw + OpenShell + NVIDIA Nemotron models with hardened defaults for networking, data access, and security.

Three installation paths:

```
# Hermes agent with NemoClaw
curl -fsSL https://www.nvidia.com/nemoclaw.sh | NEMOCLAW_AGENT=hermes bash

# OpenClaw with NemoClaw
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash

# Install an agent via natural language
"Help me install nvidia.com/nemoclaw"
```

### Key Features

- **Run agents more safely** — OpenShell-powered privacy, security, and inference controls baked in by default.
- **Any coding agent** — Supports local open models (NVIDIA Nemotron), cloud frontier models, or a model router that gives you both under defined privacy/security controls.
- **Deploy anywhere** — RTX Spark laptops, GeForce RTX PCs, RTX PRO workstations, DGX Spark/Station, or cloud. NemoClaw agents run on the same hardware stack that enterprises already have.
- **WSL2 support** — Windows Subsystem for Linux, bringing NemoClaw to Windows developers.

### Relationship to OpenShell

NemoClaw *includes* OpenShell from the start. You don't deploy an agent and then add OpenShell later — it's part of the default installation. This is critical for enterprise adoption: the security layer is not an afterthought, it is the foundation.

## 4. Hermes Agent — The Memory-Centric Agent Architecture

**Hermes Agent** ([github.com/nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)) by Nous Research is the fastest-growing agent framework in the world, crossing 177K GitHub stars and becoming the most-used agent on OpenRouter in 2026.

Its key differentiators for enterprise use:

| Capability | Description |
| --- | --- |
| **Self-Evolving Skills** | Hermes writes and refines its own skills. Each time it encounters a complex task or receives feedback, it saves learnings as a skill. This is already a core part of how the agent improves over time. |
| **Contained Sub-Agents** | Short-lived, isolated workers with focused context and tool sets. Runs with smaller context windows — ideal for local models (e.g., Qwen 3.6 35B fits in 20GB). |
| **Reliability by Design** | Nous Research curates and stress-tests every skill, tool, and plugin. The result: reliable operation even with 30B-parameter local models. |
| **Model-Agnostic** | Works with any provider or model. Ships with LM Studio and Ollama support out of the box. |

### Hermes + NVIDIA + OpenShell

The critical integration: Hermes Agent now runs inside OpenShell via NemoClaw. The `NEMOCLAW_AGENT=hermes` install path sets up Hermes with OpenShell's security controls from the first run.

From the NVIDIA blog (May 2026): *"Run self-improving Hermes agents with NVIDIA NemoClaw, combining Nous Research's skills-and-memory loop with OpenShell runtime controls. Developers can build always-on agents that learn from experience, reuse successful workflows, and operate with stronger privacy, security, and inference guardrails."*

The same Hermes setup that runs on a laptop — with the same skills, same memory, same workflows — runs inside any enterprise IT environment through OpenShell. The agent code does not change. The security layer is handled at the runtime.

## 5. The "Claw" Ecosystem — OpenClaw, NanoClaw, PicoClaw

The "claw" family of autonomous agents has exploded into a massive open-source ecosystem. Each variant targets a different deployment profile:

| Project | Stars | Language | Key Differentiator | Enterprise Security |
| --- | --- | --- | --- | --- |
| **OpenClaw** | 376K | TypeScript | The original. 100+ channels, 430K LOC. Self-hosted, persistent AI assistant. | App-level security. Community hardening via NVIDIA contributions. Now NemoClaw adds OpenShell. |
| **NanoClaw** | 29.6K | TypeScript | Lightweight OpenClaw alternative. Per-agent Docker containers. Uses Anthropic Claude SDK natively. | Container-level isolation. Credential injection via OneCLI Agent Vault. ~17K LOC vs OpenClaw's 430K. |
| **PicoClaw** | 29.3K | Go | Runs on minimal hardware (<10MB RAM). Single binary. | Minimal by design. Edge deployment security (physical isolation). |
| **clawsec** | 1K | Various | Security audit suite for the entire claw ecosystem. | Security scanning, vulnerability detection, best-practice enforcement for all claw variants. |

### NanoClaw's Security Model

NanoClaw (nanocoai/nanoclaw) takes a different approach from OpenShell: rather than wrapping agents in a policy sandbox, it isolates each agent session in its own Docker container by default. Each container gets its own SQLite databases (inbound/outbound), its own filesystem, and credentials injected via OneCLI Agent Vault — the host never passes raw API keys into the container.

The "grishahq/nanoClaw" Python variant takes this further with a 6-layer security model: FileGuard (filesystem isolation), ShellSandbox (command sandboxing), PromptGuard (prompt injection detection), SessionBudget (rate/cost limits), AuditLog (full traceability), and SecurityDoctor (continuous health monitoring).

**Key insight:** Security patterns across the ecosystem converge on the same principles — isolation, policy enforcement, credential injection, and audit — but implement them at different layers (container vs. runtime vs. application).

## 6. Enterprise Adoption — Who Is Using What

NVIDIA announced a broad coalition of enterprise software platforms working with the Agent Toolkit at GTC 2026. Here is a breakdown of who is doing what:

| Company | Integration | Security Angle |
| --- | --- | --- |
| **Adobe** | Agent Toolkit for creativity & marketing agents | Secure multi-agent runtime for long-running creative workflows |
| **Atlassian** | Rovo AI agent strategy | OpenShell for Jira & Confluence AI agents |
| **Box** | Enterprise agents using Box file system | Secure, governed access to enterprise file storage |
| **Cisco** | AI Defense integration with OpenShell | Network-level controls and guardrails for agent actions |
| **Cohesity** | Gaia AI platform + OpenShell | AI resilience and data protection for agent workflows |
| **CrowdStrike** | Secure-by-Design AI Blueprint | Falcon platform protection embedded into agent architectures + agentic MDR |
| **IQVIA** | IQVIA.ai agentic platform (150+ agents deployed, 19/20 top pharma) | Life sciences compliance — patient records, regulated data |
| **LangChain** | AI-Q + OpenShell + Nemotron integration | 1B+ download framework integrating NVIDIA security into agent orchestration |
| **Microsoft** | Security primitives integration with OpenShell | Enterprise security console integration for policy authoring |
| **Palantir** | Sovereign AI OS + Nemotron | Sovereign AI — agents on classified/sovereign infrastructure |
| **Red Hat** | Red Hat AI Factory + OpenShell | Enterprise container platform as the foundation for secure agents |
| **Salesforce** | Agentforce + Nemotron + Slack orchestration | Reference architecture for enterprise agent deployment with Slack as control plane |
| **SAP** | Joule Studio + NeMo | Enterprise business process agents with governed data access |
| **ServiceNow** | AI Specialists (90% ticket autonomy) + AI-Q | Autonomous workforce with governance, audit, and escalation |
| **Dell, HP, Lenovo, ASUS** | Hardware shipping with OpenShell pre-loaded | Hardware-rooted secure agent deployments on RTX/Spark systems |

**Real-world outcomes from the field:**

- **ServiceNow:** AI specialists using Apriel + Nemotron models resolve 90% of tickets autonomously — with full audit trails enforced by OpenShell policies.
- **IQVIA:** 150+ agents deployed across 19 of the top 20 pharma companies, handling regulated patient data under compliance frameworks.
- **CrowdStrike:** Falcon platform now protects AI agent architectures at the runtime layer — MDR for agents, not just endpoints.

## 7. The Emerging Enterprise Agent Security Stack

Consolidating what we've learned, a clear security stack is emerging for enterprise agent deployments:

| Layer | Technology | What It Enforces |
| --- | --- | --- |
| **Hardware Root of Trust** | NVIDIA RTX Spark, DGX Spark, RTX PRO | Dedicated compute for always-on agents. Data stays local. No cloud egress for sensitive workloads. |
| **Runtime Sandbox** | OpenShell (Docker/Podman/MicroVM/K8s) | Container isolation with policy-enforced egress. Filesystem, network, and process constraints. |
| **Policy Engine** | OpenShell declarative YAML policies | L7 access control. Which APIs, methods, and data the agent can touch. Hot-reloadable. |
| **Credential Management** | NVIDIA Privacy Router / OneCLI Agent Vault | Credential injection, not exposure. Strip caller creds, inject backend creds at the proxy layer. |
| **Model Routing** | NVIDIA Nemotron + Frontier model router | Sensitive queries → local open models. Complex queries → frontier models. Policy-driven routing. |
| **Enterprise Security Integration** | Cisco AI Defense, CrowdStrike Falcon, Microsoft Security, TrendAI | Existing SOC tools can author, enforce, and monitor agent policies. No new security tool needed. |
| **Agent Framework** | Hermes Agent, OpenClaw, NanoClaw | Self-evolving skills, memory, sub-agents. Runs unchanged inside the secure runtime. |

**The fundamental insight:** Security is handled at the runtime layer, not the application layer. The agent code — whether Hermes, OpenClaw, or NanoClaw — doesn't need to change. OpenShell policies govern what the agent can do, what it can access, and where its data goes. This means the same agent that runs on a developer's laptop today can run inside a Fortune 500's IT environment tomorrow — no code changes, just policy configuration.

## 8. The Bigger Picture — What This Changes

From Shann Holmberg's tweet that started this research: the biggest blocker on enterprise agent work has always been *"your AI stack is amazing but our IT won't let us touch it."* OpenShell + NemoClaw + Hermes is the answer to that objection.

Three structural shifts this enables:

1. **Security review is now handled at the runtime layer.** The conversation changes from "prove your agent is secure" to "configure the runtime policy for this agent." The agent framework and the security layer decouple.
2. **Same stack, any client.** A marketing agent builder doesn't rebuild their workflow for each client's compliance requirements. OpenShell adapts to the client's IT stack; the agent stays the same.
3. **Enterprise IT becomes an enabler, not a blocker.** With OpenShell integrating into Microsoft Security, Cisco AI Defense, and CrowdStrike, the security team gets visibility and control without slowing down deployment.

For builders in this space — whether deploying vertical marketing agents, engineering copilots, or internal tooling — this removes the single hardest barrier to enterprise revenue.

## Anti-Patterns

## How Agent Security Deployments Fail

| ANTI-PATTERN | WHY IT FAILS | WHAT TO DO INSTEAD |
| --- | --- | --- |
| "We'll add security after the POC" | Runtime security retrofitted onto a working agent means rewriting tool calls, re-plumbing the execution sandbox, and re-training the team. The POC becomes production before security ships. | Deploy OpenShell or equivalent from day one. The policy engine starts permissive (allow-all) and tightens — not the reverse. |
| Over-trusting agent autonomy without policy guardrails | Agents that can read, write, and execute without policy boundaries will eventually do something catastrophic. "Eventually" is usually sooner than expected. | Define explicit policy boundaries per tool: read-only by default, write with approval, execute with human-in-the-loop for production systems. |
| Building custom security per agent instead of using a unified runtime | Every team builds their own guardrails. Inconsistencies emerge. Security review becomes impossible because there's no single policy plane. | Standardize on one runtime security layer (OpenShell, NemoClaw, or equivalent). All agents go through the same policy engine regardless of framework. |
| Policy engine too permissive ("allow-all for now") | The "temporary" allow-all policy becomes permanent. No one wants to tighten policies because something might break. The agent effectively runs unsandboxed. | Set a hard deadline (2 weeks) for tightening from allow-all. Use policy templates per agent type (data-reader, code-executor, external-caller). |
| Treating agent memory as untrusted input | Memory poisoning: if an attacker can inject into the agent's memory store, they control future behavior across sessions. Most teams don't sanitize memory reads. | Treat memory as untrusted input. Validate retrieved memories before injection into context. Use signed memory entries for high-trust operations. |

> **Key insight:** The most dangerous anti-pattern is treating agent security as a feature to add later. The teams that succeed treat the runtime security layer as *infrastructure* — it exists before the first agent is deployed, and every agent is built assuming it's there.

## Sources

- [NVIDIA OpenShell GitHub](https://github.com/NVIDIA/OpenShell)
- [NVIDIA NemoClaw](https://www.nvidia.com/nemoclaw)
- [NVIDIA Agent Toolkit Press Release (GTC 2026)](https://nvidianews.nvidia.com/news/ai-agents)
- [NVIDIA Nemotron Labs: What OpenClaw Means for Every Organization](https://blogs.nvidia.com/blog/what-openclaw-agents-mean-for-every-organization/)
- [NVIDIA RTX AI Garage: Hermes on DGX Spark](https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/)
- [NVIDIA: What is Agentic AI?](https://blogs.nvidia.com/blog/what-is-agentic-ai/)
- [Hermes Agent — Nous Research](https://github.com/nousresearch/hermes-agent)
- [NanoClaw](https://github.com/nanocoai/nanoclaw)
- [Shann Holmberg tweet on OpenShell + Hermes](https://x.com/shannholmberg/status/2061368566256189656)
- [NVIDIA: Securing Autonomous AI Agents with OpenShell](https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell/)
- [Cisco AI Defense + OpenShell](https://blogs.cisco.com/ai/securing-enterprise-agents-with-nvidia-and-cisco-ai-defense)
- [Cohesity + OpenShell](https://www.cohesity.com/blogs/cohesity-taps-nvidia-openshell-to-build-ai-resilience/)
- [CrowdStrike Secure-by-Design AI Blueprint](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-nvidia-unveil-secure-by-design-ai-blueprint-for-ai-agents/)
- [Box + OpenShell](https://blog.box.com/box-teams-nvidia-enable-and-deploy-autonomous-ai-agents-safely-nvidia-openshell)
