---
title: "AI Adoption in Engineering Teams: What the Evidence Says"
date: 2026-05-20
type: special
url: https://luisgonzalezbernal.com/reports/reports/ai-engineering-adoption-frameworks-2026-en.html
summary: "Controlled studies of productivity · How to measure it · Code quality and security · How teams and roles change · Governance and adoption"
tags: [research, coding, business]
reading_time_minutes: 10
---
AI Engineering · Special Report

# *AI Adoption* in Engineering Teams: What the Evidence Says

20 May 2026 · Updated 7 Oct 2026

Controlled studies of productivity · How to measure it · Code quality and security · How teams and roles change · Governance and adoption

## Key findings

1. **Experienced developers were slower with AI, and did not notice.** In a randomized trial, AI tools increased task time by 19%.[1] Afterwards, the same developers estimated that AI had saved them 20%.[1]
2. **Speed gains move effort instead of removing it.** In a survey of 415 practitioners, faster work was offset by more code review and the load of checking AI output.[8]
3. **Maintainability showed no clear harm in a controlled test.** In a two-phase experiment with 151 participants, code built with AI was no harder for others to evolve.[4]
4. **Agent code churns more.** Across about 110,000 open-source pull requests, agent contributions showed more churn over time than human code.[9]
5. **Generated code still carries security flaws.** Security weaknesses appeared in 29.5% of Python and 24.2% of JavaScript snippets from AI tools in real projects.[15]
6. **The delivery metrics went the wrong way.** The 2024 DORA report, with more than 39,000 respondents, links AI adoption to lower software delivery performance.[37]

## Part I

## What controlled studies find

The most careful study gives the most uncomfortable result. Sixteen experienced open-source developers completed 246 tasks in projects they knew well.[1] Each task was randomly assigned to allow or forbid AI tools.[1] With AI, tasks took 19% longer.[1] The authors checked 20 possible causes and conclude that the slowdown is unlikely to come mainly from the experiment design.[1]

*[Forecast and perceived time savings against the measured 19 percent slowdown]*

*Experts and developers expected AI to save time; the randomized trial measured a 19% slowdown. Source 1.*

Other studies are more positive but less strict. In one experiment, AI cut median completion time by 30.7%.[4] That figure came from the observational phase, and the randomized phase found any gains "at most small and highly uncertain".[4] A GitHub-authored study of 934,533 Copilot users found that developers accept nearly 30% of suggestions.[20] Acceptance is higher among less experienced developers.[20]

How developers use the tool also matters. In a field study, moderate use of either code suggestions or chat improved task time and reduced workload.[33] Excessive or combined use reduced those benefits.[33]

## Part II

## How to measure the impact

Two frameworks dominate. DORA tracks four delivery metrics: deployment frequency, lead time for changes, change failure rate and time to restore service.[35] SPACE adds five dimensions: satisfaction, performance, activity, collaboration and efficiency.[35] DORA measures deployment efficiency, not developer experience, and fits within a slice of SPACE.[34]

| Practice | What the sources say |
| --- | --- |
| Start from pain points | The first step is to ask developers which problems they want solved[34] |
| Use surveys and system data | Neither is enough alone; surveys show what system data cannot[35,36] |
| Avoid dashboards of everything | Measuring every SPACE dimension means focusing on nothing[34] |
| Do not rank individuals by PRs | PR throughput is a system-health signal, not a measure of a person[34] |
| Do not compare teams with DORA | The DORA team warned against team-by-team evaluation[37] |

Pull request outcomes mislead for agents too. Of rejected agent PRs, only 35.7% reflected clear agent failures.[21] The rest came from workflow constraints or had no visible reason.[21] The 2024 DORA report lists benefits of AI, such as flow and job satisfaction.[37] It also reports lower delivery performance and less time on valuable work.[37]

## Part III

## Code quality and security

The quality picture is mixed. A controlled test found no systematic maintainability advantage or harm for code built with AI.[4] AI-generated code tends to be simpler and more repetitive, with more unused constructs and hardcoded debugging.[32] In the wild, agent pull requests show more churn over time than human code.[9] In 1,210 merged agent bug fixes, code smells dominated the new issues.[10] Merge success did not reliably reflect quality after the merge.[10]

- **29.5%** of AI-generated Python snippets in real projects had security weaknesses

733 snippets, 43 CWE categories[15]

- **27.25%** of Copilot suggestions were vulnerable in a replication, down from 36.54%

Python, newer Copilot and CodeQL[22]

- **55.5%** of the security issues fixed when Copilot Chat saw static-analysis warnings

Same study[15]

Security is improving but not solved. Newer Copilot versions still suggested insecure code.[22] In a small user study, Copilot accompanied more secure solutions on harder problems and made no difference on easier ones.[16] Feeding static-analysis warnings back to the model is a cheap fix that works.[15]

## Part IV

## How teams and roles change

The work moves from writing code to reviewing and governing it. Developers now spend more time reviewing code than writing it.[18] One analysis describes the shift as supervising, validating and governing systems of humans, agents, tools and evidence gates.[23]

Review cannot be handed to agents alone. Pull requests reviewed only by code review agents merged 45.20% of the time, against 68.37% for human review.[3] Most of that automated feedback was low-signal.[3] The authors advise that review agents should support human reviewers, not replace them.[3]

For juniors, the deployment choice decides. One model of organizations finds that automation leads firms to hire fewer, more skilled workers.[7] Augmentation lets firms relax entry-level requirements.[7] The authors attribute the decline in junior employment to that choice, not to generative AI itself.[7]

Several agents on one codebase need coordination. With a shared, append-only coordination log, the share of work that redid a teammate's task fell from 78% to 0%.[24] Useful throughput more than tripled.[24]

## Part V

## Governance and adoption

Adoption is cultural as much as technical. Organizational support and peer learning play key roles in getting value from AI.[14] A culture of sharing AI practices and tips is a key motive for adoption.[2] Benefits vary with task complexity, personal usage patterns and team adoption.[14]

Governance often comes from failures. A 12-week case study of agentic development describes "governance conversion".[6] Fast agentic work exposes recurring failures, and engineers turn them into lasting controls.[6] Speed-focused adoption can build hidden technical debt and accountability gaps; bounded autonomy can preserve quality, security and trust.[23]

Compliance is part of tool selection. Rules such as the EU AI Act and NIST AI RMF are hard to turn into technical criteria.[25] Knock-out criteria can stop teams from choosing a capable model with unacceptable compliance risk.[25] For MCP, practitioners value cross-system work, but fragmentation and hard fault diagnosis slow adoption.[26]

## What I would do

1. **Measure before you believe.** Perceived speed is not measured speed. Run a small trial on real tasks before you scale.
2. **Budget for review.** The time AI saves in writing moves into review and verification. Plan capacity for it.
3. **Use SPACE as a lens, not a dashboard.** Pick a few metrics tied to the pain points developers name, and combine surveys with system data.
4. **Keep humans in code review.** Use review agents to assist, and gate merges on tests and static analysis, not on agent approval.
5. **Feed security warnings back to the model.** Run static analysis on every AI change and return the warnings for a fix.
6. **Choose augmentation for juniors.** Give them AI as a tool that extends what they can do, not a reason not to hire them.

*— Luis González*

## Method and limits

This report replaces a May 2026 version that cited no sources. It was rebuilt on 7 October 2026 with the reports research pipeline. The pipeline found 136 search results across arXiv, Hacker News, GitHub, Wikipedia and Semantic Scholar. It read 40 sources in full, and 37 gave usable evidence. An open model (NaN: deepseek-v4-flash) read each source on its own. It extracted 239 claims, each with a verbatim quote, and none had to be discarded. Claude wrote the synthesis from that evidence and checked every cited figure against its source. The conclusions in "What I would do" are mine.

- **No general web search.** The run had no web-search key. Vendor reports and company case studies are under-represented; 33 of the 37 sources are research papers. The DORA report is cited through its Wikipedia summary.
- **Fast-moving tools.** Several studies used 2023–2025 tools. Results for current agents may differ.
- **Preprints.** Most papers are arXiv preprints, not peer-reviewed. Their figures are as reported and were not reproduced.

## Sources

1. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity — Becker et al. (METR), arXiv, Jul 2025 — [arxiv.org/abs/2507.09089](https://arxiv.org/abs/2507.09089)
2. AI Tool Use and Adoption in Software Development by Individuals and Organizations: A Grounded Theory Study — Li et al., arXiv, Jun 2024 — [arxiv.org/abs/2406.17325](https://arxiv.org/abs/2406.17325)
3. From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests — Chowdhury et al., arXiv, Apr 2026 — [arxiv.org/abs/2604.03196](https://arxiv.org/abs/2604.03196)
4. Echoes of AI: Investigating the Downstream Effects of AI Assistants on Software Maintainability — Borg et al., arXiv, Jul 2025 — [arxiv.org/abs/2507.00788](https://arxiv.org/abs/2507.00788)
5. Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering — Davis et al., arXiv, Jul 2026 — [arxiv.org/abs/2607.01087](https://arxiv.org/abs/2607.01087)
6. Generative AI and Organizational Structure in the Knowledge Economy — Xu et al., arXiv, May 2025 — [arxiv.org/abs/2506.00532](https://arxiv.org/abs/2506.00532)
7. The Fast and Spurious: Developer Productivity with GenAI — Afroz et al., arXiv, Oct 2025 — [arxiv.org/abs/2510.24265](https://arxiv.org/abs/2510.24265)
8. Investigating Autonomous Agent Contributions in the Wild: Activity Patterns and Code Change over Time — Popescu et al., arXiv, Apr 2026 — [arxiv.org/abs/2604.00917](https://arxiv.org/abs/2604.00917)
9. Beyond Bug Fixes: Post-Merge Code Quality Issues in Agent-Generated Pull Requests — Cynthia, Muttakin, Roy, arXiv, Jan 2026 — [arxiv.org/abs/2601.20109](https://arxiv.org/abs/2601.20109)
10. The SPACE of AI: Real-World Lessons on AI's Impact on Developers — Houck et al., arXiv, Jul 2025 — [arxiv.org/abs/2508.00178](https://arxiv.org/abs/2508.00178)
11. Security Weaknesses of Copilot-Generated Code in GitHub Projects: An Empirical Study — Fu et al., arXiv, 2025 — [arxiv.org/abs/2310.02059](https://arxiv.org/abs/2310.02059)
12. A User-centered Security Evaluation of Copilot — Asare, Nagappan, Asokan, arXiv, Aug 2023 — [arxiv.org/abs/2308.06587](https://arxiv.org/abs/2308.06587)
13. Assessing Consensus of Developers' Views on Code Readability — Sergeyuk et al., arXiv, Jul 2024 — [arxiv.org/abs/2407.03790](https://arxiv.org/abs/2407.03790)
14. Sea Change in Software Development: Economic and Productivity Analysis of the AI-Powered Developer Lifecycle — Dohmke, Iansiti, Richards, arXiv, Jun 2023 — [arxiv.org/abs/2306.15033](https://arxiv.org/abs/2306.15033)
15. Why Are Agentic Pull Requests Merged or Rejected? An Empirical Study — Peralta et al., arXiv, May 2026 — [arxiv.org/abs/2605.22534](https://arxiv.org/abs/2605.22534)
16. Assessing the Security of GitHub Copilot Generated Code — A Targeted Replication Study — Majdinasab et al., arXiv, Nov 2023 — [arxiv.org/abs/2311.11177](https://arxiv.org/abs/2311.11177)
17. From Code-Centric to Intent-Centric Software Engineering — De La Cruz, arXiv, May 2026 — [arxiv.org/abs/2605.11027](https://arxiv.org/abs/2605.11027)
18. Before the Pull Request: Mining Multi-Agent Coordination — Sarkar, arXiv, Jun 2026 — [arxiv.org/abs/2606.19616](https://arxiv.org/abs/2606.19616)
19. Operationalizing Regulations into Code: Governance and Compliance in LLM Selection for Software Engineering — Quintino, Moura, Calegário, arXiv, Aug 2026 — [arxiv.org/abs/2608.27703](https://arxiv.org/abs/2608.27703)
20. Understanding How Enterprises Adopt the Model Context Protocol for LLM-Driven Software Engineering — Chen et al., arXiv, Jun 2026 — [arxiv.org/abs/2606.09182](https://arxiv.org/abs/2606.09182)
21. Evaluating Human- and AI-Generated Code Quality Based on Code Smell — Guo et al., 2026 — [semanticscholar.org](https://www.semanticscholar.org/paper/17d5906f0a5f201f8f1ae742e736d713317b84a6)
22. Developers' Experience with Generative AI — First Insights from an Empirical Mixed-Methods Field Study — Brandebusemeyer et al., arXiv, Dec 2025 — [arxiv.org/abs/2512.19926](https://arxiv.org/abs/2512.19926)
23. Space Framework, PRs per Engineer, AI Research — Brian Houck (Microsoft), DX podcast, Dec 2024 — [getdx.com](https://getdx.com/podcast/developer-productivity-at-microsoft/)
24. A new way to measure developer productivity — from the creators of DORA and SPACE — Gergely Orosz, The Pragmatic Engineer, May 2023 — [newsletter.pragmaticengineer.com](https://newsletter.pragmaticengineer.com/p/developer-productivity-a-new-framework)
25. Developer experience — Wikipedia — [en.wikipedia.org/wiki/Developer_experience](https://en.wikipedia.org/wiki/Developer_experience)
26. DevOps Research and Assessment — Wikipedia — [en.wikipedia.org/wiki/DevOps_Research_and_Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)
