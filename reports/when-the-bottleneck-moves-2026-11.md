---
title: "When the bottleneck moves: how engineering teams reorganise around agents"
date: 2026-11-26
type: special
url: https://luisgonzalezbernal.com/reports/reports/when-the-bottleneck-moves-2026-11.html
summary: "The measured queue · The artifact that carries intent · Review by risk · Tiny teams and their platform · The numbers that do not survive"
tags: [agents, research, coding]
reading_time_minutes: 24
---
AI Engineering · Special Report

# When the *Bottleneck Moves*

26 Nov 2026

The measured queue · The artifact that carries intent · Review by risk · Tiny teams and their platform · The numbers that do not survive

## Key findings

1. **Code output rose. Final output barely moved. Review absorbed the difference.** After firms adopt coding agents, lines of code rise 44.0% and pull requests 35.7%, while resolved Jira issues rise 13.7%. Time from review submission to merge rises 56.1%.[23]
2. **The queue grows even in companies that ship well.** At Meta, significant lines per human-landed diff rose 105.9% year over year, and the share of diffs receiving timely review fell.[4] Median review time rose 5x across 22,000 developers, and 31.3% more pull requests merged with no review at all.[51]
3. **Teams that improved did not buy better agents. They moved intent into an artifact.** Microsoft Digital found that faster individuals did not lift the team, then made a living specification the primary artifact.[40] AWS replaced sprints with bolts and epics with units of work.[56]
4. **A specification improves attribution, not detection.** In a controlled drift review, an approved baseline left recall flat. It raised the share of findings tied to a named requirement from 0.00 to 0.81. The review took 48.4 minutes against 26.7.[46]
5. **The review gate is being split by risk.** Meta's risk-scored funnel cut median time to close by over 330% and review wall time by 35%.[4] Netflix reports 32% more pull requests with no Sev 1 incident on a core service.[47]
6. **Most alarming quality numbers are a volume effect, and they fade when you normalise.** Post-merge issue counts for agent PRs largely disappear once normalised by code churn.[28] GitClear's own data shows heavy AI users out-producing others 4–10x but gaining 25% against their own past.[54]

## Part I

## The queue is the measurement

The argument about AI and engineering has been an argument about speed. The evidence says the interesting quantity is not speed. It is the size of the queue in front of the reviewer, and the time a change spends waiting there.

The strongest measurement uses telemetry from an engineering analytics platform. It covers 445 million work events for 720,542 workers at 655 firms, from January 2021 to August 2026.[23] It compares firms that adopted assistants and agents at different times. That design separates adoption from the general trend, which surveys cannot do.

Code output rises sharply after agent adoption: 44.0% more lines, 36.0% more commits, 35.7% more pull requests opened. Final output does not follow. Resolved Jira issues rise 13.7%, and resolved epics 18.0%.[23] The gap has a name in the data: the review stage.

Submission to merge rises 56.1%. Waiting in the backlog rises 59.9%. Active review rises 58.5%. The share of changes that receive at least one comment rises 13.1%, and comments per change rise 38.6%.[23] The authors estimate that coding productivity rose 73.7% while review productivity fell 7.0%, and that firms moved labour from coding (−22.7%) to review (43.4%).[23] They find no detectable employment effect.

Meta published the same shape from inside. Significant lines of code per human-landed diff rose 105.9% year over year. Per-developer diff volume rose 51%, and agentic AI accounted for more than 80% of that growth. The share of diffs receiving timely review declined, which widened the gap between code supply and reviewer capacity.[4]

Vendor telemetry agrees on direction, and it is worth reading with its own warning in mind. Across 22,000 developers, median review time rose 5x and 31.3% more pull requests merged with no review. Code churn, measured as deleted to added lines per quarter, rose 861%.[51] One number in that report is structural rather than alarming. Agentic review already covers 25% of pull requests, while AI agents open less than 1% of them.[51] The agent arrived in the review lane before it arrived in the authoring lane.

The queue also explains numbers that look like contradictions. A matched study of about 800 developers found no change in cycle time and a 41% rise in bugs per pull request.[58] A vendor panel finds a median 7.8% gain in pull-request throughput. Two-thirds of the developers who reach peak time savings lose them in later quarters.[55] Neither result is about models. Both are about a system whose downstream stage did not change.

Individual measurement is even less reliable than it looks. In a randomised trial, 16 experienced maintainers allowed to use AI took 19% longer on 246 real issues. They had forecast a 24% gain, and after the slowdown they still believed they had gained 20%.[2] The gap between felt speed and measured speed is the reason this report leans on telemetry wherever telemetry exists.

Surveys complete the picture from the developer's side. In 2026, 73% of respondents use coding assistants or agents daily, and 48% trust the output only when they can easily validate it.[45] DORA reports 90% adoption, over 80% reporting a productivity gain, and 30% reporting little or no trust in generated code.[39] High adoption and low delegation are not a contradiction. They are the behaviour you would expect from people waiting in a queue.

## Part II

## Intent needs a file, not a prompt

If review is the constraint, the useful question is what a reviewer checks against. A prompt disappears when the session closes. A specification does not. The research literature has started calling this the contract between humans and agents.[17]

Microsoft Digital arrived there after a measured failure, not a theory. Its engineers got faster as individuals, and the team did not. The organisation then made a living specification the primary artifact, version-controlled beside the code, with acceptance tests written before implementation.[40] Product managers stopped owning the plan and started owning the specification.[40]

AWS reached the same place from the process side. Its method replaces sprints with bolts measured in hours or days, and epics with units of work. Each phase stores plans, requirements and design artifacts in the repository, so context survives between sessions.[56] The pattern is the same in both companies: the artifact outlives the conversation.

Adoption in the field is messier than the vendor pages suggest, and one study measures the mess. It interviewed 21 practitioners, eight of them tool makers, and analysed 266 repositories drawn from a corpus of 470,795 specification files across 73,030 public repositories.[15] Practitioners said specifications should capture intent, and many also filled them with implementation detail. Most used them selectively, mainly for new features. They reported more reliable agent behaviour alongside more planning and review cost.[15] The team benefit, the authors conclude, depends on the practice becoming shared rather than personal.[15]

What does the specification actually buy? A controlled study of drift review answers with an uncomfortable result. Reviewers with an approved baseline did not find more bugs. Their recall was flat. What changed was attribution. The share of findings tied to a named requirement went from 0.00 to 0.81, and the review took 48.4 minutes against 26.7.[46] The study's own recommendation is a targeting rule. Spend specification discipline on hard, multi-constraint work built by a capable but imperfect model, and skip it for prototypes.[46]

Practitioners who ship daily describe the same economics from the other side. Code written from the reviewer's own detailed specification is cheaper to review, because the goal and the approach are already settled.[69] Kent Beck runs the loop from a plan file, taking one unmarked test at a time and refusing code beyond what makes it pass.[71] Charity Majors argues that lines of code are the wrong artifact to review. Architecture diagrams should carry intent, and code should be regenerated from them.[64]

Three companies turned that idea into repository practice. OpenAI keeps a roughly 100-line AGENTS.md as a table of contents, not an encyclopedia. The real knowledge sits in a structured documentation tree. Linters and a maintenance agent keep it current.[43] Netflix wrote 45 architecture decision records for people and for agents, each with context, decision, pattern, anti-pattern and notes for AI use. Its AGENTS.md works like robots.txt for more than 300 documents.[47] Stripe, working at monorepo scale, avoids global rules and scopes context to directories and file patterns that attach as the agent walks the tree.[60]

Anthropic's own guidance draws the line that most teams miss. Project facts that code cannot reveal belong in CLAUDE.md. Procedures belong in skills. Anything that must always happen belongs in a hook or CI, not in prose.[41] That distinction between deterministic and probabilistic instruction is the difference between a harness and a wish.

## Part III

## The gate splits by risk, and the human moves outside the loop

No team in this evidence set solved the queue by reviewing faster. They changed what a human is asked to look at, and what arrives with it.

Meta's formulation is the clearest. In the older model the engineer drives every step. In the newer one the agent runs plan, implement, build, test and correct. The engineer sets the goal, watches the run and intervenes on drift. Approval arrives with evidence: build status, test outcomes and a recorded verification session.[42] Their success metric is not code volume but verified, production-ready outcomes that build, pass tests and survive review.[42] With that in place, Forum reached feature parity with Facebook Groups in eight weeks.[42]

The same company applied the idea to security. Generated tests run against risky diffs, and an ensemble of judges filters false positives. Engineers review criteria and aggregate outcomes, not every output. Of those approached, 589 engineers engaged, with a 60% true-positive rate. In the first half of 2026 the system caught 74 serious privacy bugs before they landed and lowered privacy incidents by 20%.[38]

Meta also shows how to automate the low-risk tail without pretending it is safe. Its review funnel classifies diffs by authorship and source, applies eligibility gates, static heuristics and a machine-learned diff risk score, then escalates. Relaxing the risk threshold from the 25th to the 50th percentile raised the approve rate to 60.31%. Median time to close fell by over 330% and median review wall time by 35%.[4]

The economic case for that split is visible in one small company's numbers. It tightened tests, observability, linting and type checking, and set an 85% unit-coverage floor. Its merged pull requests then rose from 353 to 684, a 94% increase. Median merge time was 26h for human-reviewed pull requests against 1h for those without human review.[49] The gate is where the hours are. Their engineers began reviewing the AI review rather than reading every diff.[49]

Netflix built the same thing with better manners. Its review agent compares each pull request against the documentation and the decision records. The first version left 23 comments on a single pull request, starting with praise. It now posts only verified blockers, each with evidence, a proposed fix and the rule it breaks. A label lets an agent push the fix itself.[47]

Google Cloud's team took the cultural route because the technical one was not enough. It stopped correcting style on disposable agent-written code and moved review to architectural blueprints. It approves pull requests conditionally, subject to tests passing, which removed twelve-hour waits across time zones. Every pull request now carries a generated summary of what changes, where it may break and how risky it is.[70] It also set quiet hours so approval requests stop at the end of the day, and weekly sessions to share what agents found.[70]

Those rituals exist because review fatigue is measurable. Across 400 reviewers and 11,429 reviews of agent-authored pull requests, the approval rate rose from 30.1% to 36.8%. The cumulative gap reached 14.5 percentage points between the first and tenth decile of experience. Review latency rose 3.5x while inline comments fell 22%.[29] The authors read that as habituation under load, not as calibrated trust.[29] A gate that approves more while inspecting less is not a gate.

## Part IV

## Tiny teams are a platform decision

The organisational claim that travels furthest is the smallest team. AWS reports that projects which once needed 30 to 40 people now run with six to eight.[50] Three cases make it concrete. The Amazon Quick desktop app was built by about six engineers and reached 200 internal users in six weeks and 10,000 in ten weeks.[50] The Bedrock inference engine was rebuilt by six engineers in 76 days, against an expectation of 30 developers over 12 to 18 months.[50] A cross-platform notification feature estimated at four weeks shipped in a day and a half.[50]

AWS also supplies the distinction that matters. Its internal measurement reports a median 4.5x productivity gain, with some teams above 10x, for teams that restructured their workflows around AI. Teams that only added tools to the existing way of working did not see the same result.[50] That is the whole thesis of this report in one sentence, from a company selling the tools.

Gartner projects that 60% of organisations will adopt smaller engineering teams at scale by 2029, up from 15% in 2026. It describes teams of 4-5 members, some of 2-3. Each combines product, a design role covering user and agent experience, and at least one AI-native engineer. It adds that tiny teams depend on platform engineering for standardised, automated workflows.[37] Its warning is the one organisations skip: cutting junior hiring hollows out the pipeline, and that bill arrives around 2028.[37]

Shopify is the clearest case of the platform underneath. Its agent works only in public Slack channels, so every session becomes a searchable transcript. In a 30-day window it ran 59,918 sessions across 5,170 channels, touched the work of more than 7,000 people, and merged 3,536 coauthored pull requests. One in eight merged pull requests company-wide is coauthored by it.[68] The monorepo holds code plus skills, conventions, intent documents and AGENTS.md files, so each solved problem leaves a reusable trace.[68]

The role changes are real, and the numbers are smaller than the headlines. Block created an AI Champions programme, and within three months AI-authored code rose 69%, reported time savings rose 37% and automated pull requests rose 21x. About 95% of its engineers use AI, and the second-largest group runs 3-5 agents in parallel.[67] Coinbase measured 5,068 merged pull requests across 461 repositories from one internal tool. Its users merged 3.5x more pull requests per engineer, 39.6 against 11.4. It states plainly that those users were probably already the high-output engineers.[62]

Zapier offers the most honest headline number in the set. Zapier reports an 11% increase in developer productivity in 2025 from Cursor, Claude Code and Copilot. Nearly all of its team, 97%, uses AI daily. AI fluency is assessed for 100% of candidates.[72] Eleven per cent is what a disciplined company reports when it measures rather than estimates.

Two practitioners describe where the coordination work moves. Will Larson watched deploy frequency rise from about 6 per week to 200-400 per week. Daily use of agent tooling went from roughly 25% to 100% in two months, without a mandate. His conclusion: first-pass code is nearly free, working code is not, and slop pull requests are cheap but actively harmful.[65] Team Topologies reframes the design unit as stewardship of a value flow. Teams become long-lived stewards that promote only the smallest, highest-quality changes. Agent context is treated like human cognitive load.[63]

## Part V

## The numbers that do not survive contact with normalisation

The counter-evidence is real, and part of it is weaker than it sounds. Separating the two is the most useful thing this report can do.

Start with the scariest figures. Vendor telemetry reports bugs per developer up 54% and an incidents-to-pull-request ratio that more than tripled under high adoption.[51] A large-scale post-merge study tested that claim properly. It analysed 1,210 merged agent-generated bug-fix pull requests. The raw differences between agents largely disappear after normalising by code churn. The extra issues came from bigger pull requests, not worse code.[28] Another measurement of real repositories reaches a similar conclusion. In the field, differences between AI-assisted and human-written code are rather small, in contrast to laboratory results.[32]

Duplication is the finding that does survive. GitClear reports block duplication rising from 40.3 to 73.0 per million changed lines between 2023 and 2026, an 81% increase. Within-commit copy and paste rose 41%, and two-week churn rose 15%.[54] Moved and refactored code fell from 21% in 2022 to 3.8% in 2026, and copy and paste rose from 9.4% to 15.7%.[54] Function connectivity fell 35%, from 343 method calls per thousand changed lines to 223.[54] Its own correction matters too. Heavy AI users out-produce non-users by 4-10x, but against their own past the gain is 25%. Most of that gap predates AI.[54]

Security evidence is consistent across independent tests. Veracode tested more than 100 models on four languages. 45% of samples failed security tests with OWASP Top 10 weaknesses, and Java reached 72%.[53] Package hallucination is measured at at least 5.2% for commercial models and 21.7% for open-source models, across 576,000 generated samples. That produced 205,474 unique package names an attacker could register.[21]

No dashboard shows how the human signal degrades. The curl project ended its long-running bug bounty after the share of confirmed reports fell from above 15% to below 5%. In better times it had paid over 100,000 USD and confirmed 87 vulnerabilities.[66] According to the report, inbound volume rose sharply while neighbouring programmes stayed flat or declined.[66] Verification debt names the underlying problem: the gap between what was released and what has been demonstrated to be safe under production-like conditions.[73]

Agent output also churns more. Across roughly 110,000 open-source pull requests, agent contributions are associated with more churn over time than human-authored code.[10] And a benchmark built on product requirement documents found the highest complete-delivery rate at 14.0%, across 11 model and scaffold configurations. Agents build components well and requirements poorly.[12] That is the strongest argument for the specification: not quality of code, but completeness of intent.

One structural finding comes from the same working paper that measured the queue. It found that 79.1% of firms adopted AI review tools. Humans still wrote nearly all reviews and comments.[23] Its interviews describe what happens after an outage: new rules required senior approval for AI-generated code, and the bottleneck grew.[23] When the process reacts to failures by adding gates, the queue lengthens without the risk falling.

## Part VI

## Where throughput rose without losing stability

The thesis needs one test it could fail. If adding agents always cost stability, the story would be about volume alone. A handful of documented cases moved both numbers in the right direction, and they share a shape.

Netflix Commerce increased pull requests 32% year over year. It reported no Sev 1 incidents in 2026 on a core service, and its developer NPS rose from -3 to +25 over three quarters.[47] Duckbill lifted merged pull requests 94% after tightening tests, types, linting and coverage.[49] Meta shipped Forum to parity in eight weeks. Separately, an autonomous stress loop fixed a memory issue during development, roughly halving memory use and page faults.[42] AWS reports a median 4.5x for repurposed workflows.[50]

DORA finds the same pattern at the level of teams rather than companies. It describes AI as an amplifier that magnifies the strengths of high-performing organisations and the dysfunctions of struggling ones.[39] Two of its cases are concrete. An Adidas pilot found loosely coupled teams with fast feedback loops gaining 20% to 30% on commits, pull requests and feature velocity. A happiness measure rose 50%.[39] At Booking.com, training developers to give assistants more explicit instructions and context produced up to 30% more merge requests.[39] Both interventions are about clarity of intent, not model choice.

The cost side is not denied by any of this. DORA's ROI work describes an initial productivity dip, and asks leaders to budget for it as a tuition cost before returns arrive. It also argues that the greatest returns come from reducing rework rather than from generating more code.[59] That is the same conclusion the queue data reaches from a different direction.

One study complicates the blame narrative in a useful way. The study covers 11,048 closed agentic pull requests. Only 35.7% of rejected ones were clear agent failures. Workflow constraints drove 31.2%, and 33.1% had no observable rationale at all.[22] Among merged agentic pull requests, 15.4% required explicit reviewer involvement through feedback or direct commits.[22] Merge and rejection rates, in other words, are a poor proxy for how good the agent is. They mostly measure how well the team absorbs it.

*[Five delivery stages with review marked as the constraint, and three levers that widen it]*

*The constraint sits at review. The levers that relieve it act on the artifact, the gate and the evidence, not on generation. Figures from parts I to III.*

## What I would do

1. **Measure the queue before touching the process.** Take 90 days of deployments. Compute the five delivery metrics split by author kind, plus median review wait and the share of pull requests merged with no review. Without that baseline every later claim is an impression.
2. **Put the limit where the constraint is.** Cap diff size for agent-authored changes, and label authorship from the bot identity rather than a human's good will. A gate on batch size is cheaper than a second reviewer.
3. **Write the spec where it pays, and only there.** Multi-constraint, long-lived, regulated work gets a versioned specification with acceptance criteria a reviewer can cite. Prototypes and one-shot scripts do not. Expect the review to take longer and to be worth more.
4. **Split the gate by risk.** Human review for public API, authentication, permissions, non-additive schema, design system and the agent's own skills. Automated review with a coverage floor for the rest, and a generated risk summary on every pull request so the human starts where it matters.
5. **Attach evidence, not approvals.** What reaches a human should carry test results, a verification session and the list of deviations. Keep the deterministic parts — linters, type checks, spend caps, quiet hours — in the harness, not in a prompt.
6. **Treat the repository as a product for a second reader.** A short AGENTS.md as a map, decision records written for people and agents, and a CI check that the documentation still matches the code. Add maintenance agents that open small refactors, so entropy is paid continuously.

*— Luis González*

## Method and limits

This report draws on 44 sources published between July 2024 and November 2026. They include research papers, company engineering blogs, two DORA studies and their ROI analysis, vendor telemetry, developer surveys and practitioner writing. Every figure cited in the text was checked against its source, and each claim carries the number of the source it comes from. The full evidence — sources, extracted claims and verbatim quotes — is public in the [evidence pack](https://github.com/iamluisgb/reports/tree/master/data/research/engineering-work-bottleneck). The recommendations in "What I would do" are mine.

- **Vendor figures measure vendor customers.** The largest telemetry sets come from companies that sell engineering analytics, so their samples are self-selected. Where a number came from a vendor I say so, and I prefer the independent study when the two disagree.
- **No randomised trial of organisational design exists.** The strongest causal evidence is about individual speed. Claims about teams, rituals and artifacts come from company reports describing what worked, which is useful and not controlled.
- **Some quality scares are a volume effect.** Two studies find that most of the excess defects in agent code disappear after normalising by change size. The duplication signal does not disappear, and I treat the two differently.
- **Specification research is young.** The largest practice study rests on 21 interviews and public repositories, and the conceptual paper presents itself as a first step, not a validated theory. They support decisions to test, not settled conclusions.

## Sources

2. METR: measuring the impact of early-2025 AI on experienced developers — Joel Becker, Nate Rush, Beth Barnes, David Rein / METR, 2025-07-10 — [metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev…](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
4. Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency — Chris Adams et al. (arXiv), 2026-08-24 — [arxiv.org/abs/2605.30208](https://arxiv.org/abs/2605.30208)
10. Investigating Autonomous Agent Contributions in the Wild — arxiv.org, 2026-04-01 — [arxiv.org/abs/2604.00917](https://arxiv.org/abs/2604.00917)
12. When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories — arxiv.org, 2026-10-20 — [arxiv.org/abs/2610.26394](https://arxiv.org/abs/2610.26394)
15. Spec-Driven Development as Prescribed and as Practiced — arxiv.org, 2026-08-25 — [arxiv.org/abs/2608.25202](https://arxiv.org/abs/2608.25202)
17. Spec-Driven Development for Agentic Software Engineering — arxiv.org, 2026-09-02 — [arxiv.org/abs/2609.00252](https://arxiv.org/abs/2609.00252)
21. We Have a Package for You: package hallucinations across LLMs (USENIX 2025) — arxiv.org, 2024-06-12 — [arxiv.org/abs/2406.10279](https://arxiv.org/abs/2406.10279)
22. Why Are Agentic Pull Requests Merged or Rejected — Sien Reeve O. Peralta et al. (arXiv, MSR 2026), 2026-05-21 — [arxiv.org/abs/2605.22534](https://arxiv.org/abs/2605.22534)
23. Chen & Stratton: AI in the Firm, Bottlenecks in Software Production — Fiona Chen and James Stratton (Harvard University), 2026-11-21 — [fion.ac/jellyfish.pdf](https://fion.ac/jellyfish.pdf)
28. Beyond Bug Fixes: post-merge code quality issues — Shamse Tasnim Cynthia, Al Muttakin, Banani Roy, 2026-01-27 — [arxiv.org/abs/2601.20109](https://arxiv.org/abs/2601.20109)
29. Habituation at the Gate: rising approval and declining scrutiny in review of agent code — arxiv.org, 2026-08-24 — [arxiv.org/abs/2606.22721](https://arxiv.org/abs/2606.22721)
32. A Large-Scale Comprehensive Measurement of AI-Generated Code in Real-World Repositories A Large-Scale Comprehensive Measurement of AI-Generated Code in Real-World Repositories — arxiv.org, 2026-03-28 — [arxiv.org/abs/2603.27130](https://arxiv.org/abs/2603.27130)
37. Gartner: 60% of organisations adopt smaller engineering teams by 2029 — Gartner, Inc., 2026-07-07 — [gartner.com/en/newsroom/press-releases/2026-07-07-gartner…](https://www.gartner.com/en/newsroom/press-releases/2026-07-07-gartner-predicts-60-percent-of-organizations-will-adopt-smaller-software-engineering-teams-by-2029)
38. Meta: catching bugs before they land, JiTTests at full scale — engineering.fb.com, 2026-10-29 — [engineering.fb.com/2026/10/29/security/catching-bugs-befo…](https://engineering.fb.com/2026/10/29/security/catching-bugs-before-they-land-jittestings-human-on-the-loop-approach-at-full-scale/)
39. DORA: State of AI-assisted Software Development 2025 — DORA / Google Cloud, 2025-09-23 — [services.google.com/fh/files/misc/2025_state_of_ai_assist…](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
40. Microsoft Digital: spec-driven development at Microsoft — Neil Orint and David Hirning / Microsoft, 2026-09-03 — [microsoft.com/insidetrack/blog/engineering-the-frontier-f…](https://www.microsoft.com/insidetrack/blog/engineering-the-frontier-firm-sharing-our-ai-native-approach-to-software-development/)
41. Anthropic: Claude Code best practices — Anthropic (Claude Code Docs), 2026-11-26 — [anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)
42. Meta: how Meta built Forum with AI-native engineering — Meta Engineering (Shengbo Guo et al.), 2026-10-15 — [engineering.fb.com/2026/10/15/ml-applications/how-meta-bu…](https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/)
43. OpenAI: harness engineering, leveraging Codex in an agent-first world — Ryan Lopopolo / OpenAI, 2026-02-11 — [openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)
45. Stack Overflow Developer Survey 2026: AI — Stack Overflow, 2026-07-01 — [survey.stackoverflow.co/2026/ai](https://survey.stackoverflow.co/2026/ai)
46. When Spec-Driven Development Pays off (GAISS 2026) — Nitin Garg / InfoQ, 2026-09-10 — [infoq.com/articles/when-spec-driven-development-pays-off/](https://www.infoq.com/articles/when-spec-driven-development-pays-off/)
47. Netflix at QCon SF: retrofitting the SDLC for AI coding agents — Andrew Hoblitzell (InfoQ), 2026-11-23 — [infoq.com/news/2026/11/netflix-sdlc-ai-coding-agents/](https://www.infoq.com/news/2026/11/netflix-sdlc-ai-coding-agents/)
49. The Pragmatic Engineer: what is happening with code reviews — Gergely Orosz, 2026-09-08 — [newsletter.pragmaticengineer.com/p/what-is-happening-with…](https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews)
50. GeekWire: how agentic AI is rewiring Amazon teams — Todd Bishop, GeekWire, 2026-06-16 — [geekwire.com/2026/how-agentic-ai-is-rewiring-amazons-team…](https://www.geekwire.com/2026/how-agentic-ai-is-rewiring-amazons-teams-and-upending-its-traditions/)
51. Faros AI Engineering Report 2026: The Acceleration Whiplash — Faros AI, 2026-04-09 — [pages.faros.ai/hubfs/AI%5FEngineering%5FReport%5F2026%5FT…](https://pages.faros.ai/hubfs/AI%5FEngineering%5FReport%5F2026%5FThe%5FAcceleration%5FWhiplash%5FFaros.pdf)
53. Veracode: GenAI code security report — Jens Wessling / Veracode, 2025-07-30 — [veracode.com/blog/genai-code-security-report](https://veracode.com/blog/genai-code-security-report)
54. GitClear: the AI code quality maintainability gap — GitClear, 2026-06-01 — [gitclear.com/the_ai_code_quality_maintainability_gap](https://gitclear.com/the_ai_code_quality_maintainability_gap)
55. DX: the AI efficiency plateau — Brian Houck / DX, 2026-05-27 — [getdx.com/blog/the-ai-efficiency-plateau](https://getdx.com/blog/the-ai-efficiency-plateau)
56. AWS: AI-Driven Development Life Cycle (AI-DLC) — Raja SP on AWS DevOps Blog (Amazon Web Services), 2025-07-31 — [aws.amazon.com/blogs/devops/ai-driven-development-life-cy…](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)
58. Uplevel: GenAI developers, no delivery gain and higher bug rate — Uplevel (Lauren Lang), 2024-09-16 — [uplevelteam.com/blog/genai-developers](https://uplevelteam.com/blog/genai-developers)
59. DORA: ROI of AI-assisted Software Development — Google Cloud / DORA, 2026-04-22 — [cloud.google.com/resources/content/dora-roi-of-ai-assiste…](https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development)
60. Stripe: minions, one-shot end-to-end coding agents, part 2 — Alistair Gray / Stripe, 2026-02-19 — [stripe.dev/blog/minions-stripes-one-shot-end-to-end-codin…](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2)
62. Coinbase: engineers as orchestrators of agent fleets — Alessandro Rodi, Adam Wolf (Coinbase), 2026-05-11 — [coinbase.com/blog/coding-had-a-concurrency-problem-how-mu…](https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it)
63. Team Topologies: stewardship of value flow — Matthew Skelton / Team Topologies, 2026-08-18 — [teamtopologies.com/news-blogs-newsletters/team-topologies…](https://teamtopologies.com/news-blogs-newsletters/team-topologies-for-the-ai-age-stewardship-of-value-flow)
64. Charity Majors: AI demands more engineering discipline — Charity Majors, 2026-06-15 — [charity.wtf/p/ai-demands-more-engineering-discipline](https://charity.wtf/p/ai-demands-more-engineering-discipline)
65. Will Larson: revised rules of engineering leadership — Will Larson, 2026-06-15 — [lethain.com/revised-rules-of-engineering-leadership](https://lethain.com/revised-rules-of-engineering-leadership)
66. curl: the end of the bug bounty — Daniel Stenberg, 2026-01-26 — [daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bo…](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/)
67. Block: AI-assisted development — Angie Jones / Block Engineering, 2026-01-18 — [engineering.block.xyz/blog/ai-assisted-development-at-blo…](https://engineering.block.xyz/blog/ai-assisted-development-at-block)
68. Shopify: Under the River — Burke Libbey, Javier Moreno, River (Shopify Engineering), 2026-05-28 — [shopify.engineering/under-the-river](https://shopify.engineering/under-the-river)
69. Simon Willison: parallel coding agents — Simon Willison, 2025-10-05 — [simonwillison.net/2025/Oct/5/parallel-coding-agents](https://simonwillison.net/2025/Oct/5/parallel-coding-agents)
70. Google Cloud: when AI writes the code, who reviews it — Lee Boonstra, Google Cloud Office of the CTO, 2026-04-28 — [cloud.google.com/transform/when-ai-writes-the-code-who-re…](https://cloud.google.com/transform/when-ai-writes-the-code-who-reviews-it-cto-google-cloud)
71. Kent Beck: augmented coding beyond the vibes — Kent Beck, 2025-06-25 — [newsletter.kentbeck.com/p/augmented-coding-beyond-the-vib…](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)
72. Zapier: AI fluency in hiring, Chief People & AI Transformation Officer — Wade Foster, 2025-10-29 — [zapier.com/blog/ai-transformation-leader/](https://zapier.com/blog/ai-transformation-leader/)
73. Communications of the ACM: verification debt — CACM, 2026-01-16 — [cacm.acm.org/blogcacm/verification-debt-when-generative-a…](https://cacm.acm.org/blogcacm/verification-debt-when-generative-ai-speeds-change-faster-than-proof/)
