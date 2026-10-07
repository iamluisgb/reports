---
title: "AI-Native Design: Autonomy, Trust and the Limits of Chat"
date: 2026-07-17
type: special
url: https://luisgonzalezbernal.com/reports/reports/ai-native-design-patterns-2026-07-17.html
summary: "Guidelines and patterns · Choosing the level of autonomy · What builds appropriate trust · Chat against generated interfaces · What product teams report"
tags: [research, coding]
reading_time_minutes: 9
---
Product Design · Special Report

# *AI-Native Design*: Autonomy, Trust and the Limits of Chat

17 Jul 2026 · Updated 7 Oct 2026

Guidelines and patterns · Choosing the level of autonomy · What builds appropriate trust · Chat against generated interfaces · What product teams report

## Key findings

1. **Explanations make users trust wrong answers too.** In a pre-registered experiment with 308 people, explanations increased reliance on both correct and incorrect LLM answers.[15] Sources and visible inconsistencies reduced reliance on incorrect ones.[15]
2. **A high confidence score can lower accuracy.** In clinical decision support, high confidence scores raised trust but led to overreliance and worse diagnoses.[11]
3. **Adapting to the user's trust works.** Giving supporting or counter-explanations according to the user's trust cut inappropriate reliance by up to 38% and raised accuracy by 20%.[19]
4. **Generated interfaces beat chat.** Interfaces generated for the task outperformed chat consistently, with up to 72% higher human preference.[7]
5. **Partial automation is often the rational end state.** Because near-perfect accuracy is disproportionately expensive, full automation is often not the cheapest option.[16]
6. **Autonomy is a design decision.** Researchers propose treating an agent's autonomy separately from its capability.[14] A capable agent can be deliberately limited because of risk and reversibility.[28]

## Part I

## Guidelines and patterns

Designers have guidelines, but research on how they are used is thin.[26] In interviews with 31 designers and product managers, practitioners used the People + AI Guidebook for design problems, education and cross-team communication.[26] They wanted more help in early ideation and problem framing, to avoid AI product failures.[26]

Real collaboration is still rare. A review of 105 articles on AI-assisted decisions found interactions dominated by simple paradigms, with little truly interactive functionality.[10] How information is presented matters as much as what is presented, such as the order of recommendations.[10]

Domain pattern libraries help. A healthcare study identified 12 design patterns for organizing what an AI interface shows clinicians.[6] In a workshop with 14 UI designers, the patterns helped them ground designs in user needs and generate more alternatives.[6]

Interfaces can also cause harm. Anthropomorphic, deceptive and immersive interfaces affect human-AI interaction in ways that risk evaluations tend to overlook.[13]

## Part II

## Choosing the level of autonomy

An agent's autonomy should be a deliberate design decision, separate from its capability and environment.[14] One framework defines five levels by the user's role: operator, collaborator, consultant, approver and observer.[14] A governance framework adds a second axis. Allowed autonomy depends on risk, oversight and accountability; capability is what the agent can technically do.[28]

*[Five levels of agent autonomy by the user's role, from operator to observer; allowed autonomy is set by risk, separately from capability]*

*Five levels of autonomy defined by the user's role, with the allowed level chosen apart from capability. Sources 14 and 28.*

Economics points to the middle levels. Higher accuracy costs more and more: good performance may be cheap, but near-perfect accuracy is disproportionately expensive.[16] Partial automation, where humans keep the residual tasks, is often the long-run equilibrium.[16] Simple tasks see high substitution; complex tasks favor limited automation.[16]

Static settings do not fit how people work. Developers' autonomy preferences shift across tasks and over time, so fixed permission files fall short.[9] Hedwig, a coding agent, learns guidelines from developer decisions.[9] It reduces friction where it has earned trust and tightens oversight on unfamiliar work.[9] Practice shows the stakes. Honeycomb doubled its pull requests with AI while incidents rose 1.5x.[32]

## Part III

## What builds appropriate trust

The goal is appropriate reliance: trusting the AI when it is right and not when it is wrong. Users often accept incorrect LLM answers despite warnings.[1] Low trust leads to under-reliance and high trust to over-reliance.[19]

| Design choice | Effect on reliance |
| --- | --- |
| Explanations | Increase reliance on correct and incorrect answers alike[15] |
| Sources, visible inconsistencies | Less reliance on incorrect answers[15] |
| Feature-based explanations | No better decisions, more overreliance[17] |
| Example-based explanations | Better decisions than feature-based ones[17] |
| High confidence scores | More trust, more overreliance, lower accuracy[11] |
| Uncertainty per relation | Less independent verification by users[1] |
| Explanations adapted to trust | Up to 38% less inappropriate reliance[19] |

Positive friction helps. Explanations or confirmations can reduce overreliance.[2] In one dialogue agent, self-correction raised joint goal accuracy from 67.13 to 70.51. A confirmation turn when the model was uncertain gave a similar gain.[2] Forced pauses can also promote deliberation.[19]

The user's own self-assessment matters too. People who overestimate their performance tend to under-rely on AI.[4] A tutorial that showed AI fallibility helped them, but could hurt people who underestimated themselves.[4]

## Part IV

## Chat against generated interfaces

Most LLM systems still use a linear request-response format, which is inefficient for dense or exploratory tasks.[7] When LLMs generate an interface for the task, users prefer it: up to 72% higher preference than chat.[7]

Chat is fragile for analysis. Chatbots for what-if analysis misread intent and give inconsistent results as conversations go on.[12] An alternative translates questions into a declarative specification that compiles into an interactive interface.[12] On 405 questions, 52.42% of specifications were correct without help, and targeted repairs raised success to 80.42%.[12]

For writing, chat ignores context. It neglects implicit writing context and user intent, and gives users little control.[21] Conversation still has a place. On the move, conversational interfaces have potential, but they do not yet give a task performance advantage.[27] Language interfaces also assume users can produce explicit input, which fails for some users with impairments.[24]

## Part V

## What product teams report

This is the weakest part of the evidence. Without general web search, the run found almost nothing that AI-native product teams wrote about their own design. The practitioner evidence that did appear is anecdotal but consistent.

Tessl's software factory peaked at 850 pull requests in a week, with 85 to 90% handled by agents end to end.[32] HumanLayer trusted AI to write the plan and skip the code; after four months the codebase was unusable.[32] AWS's Marc Brooker read up to 4,000 postmortems and concluded that tests and specs are the real work.[32]

Smaller products show common moves. They embed the agent in tools teams already use, such as Slack, Jira, Linear and Figma.[30] They add approval steps before launch.[30] And they keep a few human decision gates in a long agent workflow.[34]

## What I would do

1. **Set the autonomy level per action.** Decide it from risk and reversibility, write it down, and keep it apart from what the model can do.
2. **Plan for partial automation.** Automate the routine path and design the human's residual work as a first-class screen, not an error state.
3. **Show sources, not only explanations.** Explanations raise trust in wrong answers; sources and visible doubts help users catch them.
4. **Do not lead with a confidence number.** Ask for confirmation where the model is uncertain instead.
5. **Generate an interface for dense tasks.** Keep chat for open questions; use forms, tables and controls for analysis and repeated work.
6. **Let autonomy grow with earned trust.** Start narrow, widen where the record is good, and measure overreliance, not only satisfaction.

*— Luis González*

## Method and limits

This report replaces a July 2026 version that cited 2 sources and was built mostly on product observation. It was rebuilt on 7 October 2026 with the reports research pipeline. The pipeline found 131 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar. It read 40 sources in full, and 35 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 220 claims, each with a verbatim quote. 3 claims whose quote did not appear in the source were discarded. Claude wrote the synthesis from that evidence and checked every cited figure against its source. The conclusions in "What I would do" are mine.

- **No general web search.** The run had no web-search key. Writing by Ramp, Linear, Notion and Vercel about their own design did not appear. The earlier version's claims about these products had no source and were removed.
- **Lab studies.** Most trust findings come from controlled experiments, often in medicine or decision tasks. Effects in a product may differ.
- **Preprints.** Most papers are arXiv preprints, not peer-reviewed. Their figures are as reported and were not reproduced.

## Sources

1. Not All Uncertainty Is Equal: How Uncertainty Granularity Shapes Human Verification in LLM-Assisted Decision Making — Villavicencio, Pan, Wang, arXiv, May 2026 — [arxiv.org/abs/2605.28571](https://arxiv.org/abs/2605.28571)
2. Know Your Mistakes: Towards Preventing Overreliance on Task-Oriented Conversational AI Through Accountability Modeling — Dey et al., arXiv, Jan 2025 — [arxiv.org/abs/2501.10316](https://arxiv.org/abs/2501.10316)
3. Knowing About Knowing: An Illusion of Human Competence Can Hinder Appropriate Reliance on AI Systems — He, Kuiper, Gadiraju, arXiv, Jan 2023 — [arxiv.org/abs/2301.11333](https://arxiv.org/abs/2301.11333)
4. Design Patterns of Human-AI Interfaces in Healthcare — Sheng et al., arXiv, Jul 2025 — [arxiv.org/abs/2507.12721](https://arxiv.org/abs/2507.12721)
5. Generative Interfaces for Language Models — Chen et al., arXiv, Aug 2025 — [arxiv.org/abs/2508.19227](https://arxiv.org/abs/2508.19227)
6. Hedwig: Dynamic Autonomy for Coding Agents Under Local Oversight — Shukla et al., arXiv, May 2026 — [arxiv.org/abs/2605.11495](https://arxiv.org/abs/2605.11495)
7. Human-AI collaboration is not very collaborative yet: A taxonomy of interaction patterns in AI-assisted decision making — Gomez et al., arXiv, Oct 2023 — [arxiv.org/abs/2310.19778](https://arxiv.org/abs/2310.19778)
8. Explainability and AI Confidence in Clinical Decision Support Systems — Rezaeian, Bayrak, Asan, arXiv, Jan 2025 — [arxiv.org/abs/2501.16693](https://arxiv.org/abs/2501.16693)
9. Bridging Natural Language and Interactive What-If Interfaces via LLM-Generated Declarative Specification — Gathani et al., arXiv, Apr 2026 — [arxiv.org/abs/2604.07652](https://arxiv.org/abs/2604.07652)
10. Characterizing and modeling harms from interactions with design patterns in AI interfaces — Ibrahim, Rocher, Valdivia, arXiv, Apr 2024 — [arxiv.org/abs/2404.11370](https://arxiv.org/abs/2404.11370)
11. Levels of Autonomy for AI Agents — Feng, McDonald, Zhang, arXiv, Jun 2025 — [arxiv.org/abs/2506.12469](https://arxiv.org/abs/2506.12469)
12. Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies — Kim et al., arXiv, Feb 2025 — [arxiv.org/abs/2502.08554](https://arxiv.org/abs/2502.08554)
13. Economics of Human and AI Collaboration: When is Partial Automation More Attractive than Full Automation? — Li et al., arXiv, 2026 — [arxiv.org/abs/2603.29121](https://arxiv.org/abs/2603.29121)
14. Understanding the Role of Human Intuition on Reliance in Human-AI Decision-Making with Explanations — Chen et al., arXiv, Jan 2023 — [arxiv.org/abs/2301.07255](https://arxiv.org/abs/2301.07255)
15. Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance — Srinivasan, Thomason, arXiv, 2025 — [arxiv.org/abs/2502.13321](https://arxiv.org/abs/2502.13321)
16. VISAR: A Human-AI Argumentative Writing Assistant with Visual Programming and Rapid Draft Prototyping — Zhang et al., arXiv, Apr 2023 — [arxiv.org/abs/2304.07810](https://arxiv.org/abs/2304.07810)
17. EEG-Based Brain-LLM Interface for Human Preference Aligned Generation — Zhang et al., arXiv, Mar 2026 — [arxiv.org/abs/2603.16897](https://arxiv.org/abs/2603.16897)
18. Investigating How Practitioners Use Human-AI Guidelines: A Case Study on the People + AI Guidebook — Yildirim et al., arXiv, Jan 2023 — [arxiv.org/abs/2301.12243](https://arxiv.org/abs/2301.12243)
19. Situational impairment due to walking with conversational versus graphical interfaces — Marentakis, Balic, Audio Mostly, Sep 2024 — [semanticscholar.org](https://www.semanticscholar.org/paper/12e11f3fe970d798006447d519e25cad4e85149c)
20. Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels — Zheng et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.23438](https://arxiv.org/abs/2607.23438)
21. Quell: AI QA agent across Linear, Vercel, Jira, Netlify and Figma — Quellit (product page), May 2025 — [quellit.ai](https://www.quellit.ai/)
22. Levels of AI agent autonomy: learning from self-driving cars — AI Native Dev (Tessl), Oct 2025 — [ainativedev.io](https://ainativedev.io/news/the-5-levels-of-ai-agent-autonomy-learning-from-self-driving-cars)
23. great-pm: product-management agents with human decision gates — GitHub, Sep 2026 — [github.com/VandanaAjayDubey111/great-pm](https://github.com/VandanaAjayDubey111/great-pm)
