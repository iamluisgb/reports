# Evidence — When the bottleneck moves: how engineering teams reorganise around agents

Generated 2026-11-26 · searched: 119 · candidates: 77 · web_search: True · read: 77 · sources_with_evidence: 74 · claims: 484 · quotes_dropped_as_unverified: 9

## q1. What is the measured effect of AI coding tools on delivery flow: code output, final output, review queue and rework?

- **[1] OpenAI Codex reportedly created over 400,000 pull requests in two months, illustrating the scale of autonomous coding agent output.**
  > Autonomous coding agents are generating code at an unprecedented scale, with OpenAI Codex alone creating over 400,000 pull requests (PRs) in two months.
- **[1] The study analyzes 3,109 unique PRs in commented review state from AIDev's 19,450 PRs, comparing human-only versus CRA-only reviews.**
  > From AIDev's 19,450 PRs, we analyze 3,109 unique PRs in the commented review state, comparing human-only versus CRA-only reviews.
- **[1] CRA-only PRs had a 45.20% merge rate, 23.17 percentage points lower than the 68.37% human-only rate, and significantly higher abandonment.**
  > CRA-only PRs achieve a 45.20% merge rate, 23.17 percentage points lower than human-only PRs (68.37%), with significantly higher abandonment.
- **[1] The authors examined 98 closed CRA-only PRs to test whether low signal-to-noise ratios contribute to abandonment.**
  > We examine 98 closed CRA-only PRs to assess whether low signal-to-noise ratios contribute to abandonment.
- **[2] In the randomized controlled trial, experienced open-source developers allowed to use AI tools took 19% longer to complete issues, a significant slowdown.**
  > When developers are allowed to use AI tools, they take 19% longer to complete issues—a significant slowdown that goes against developer beliefs and expert forecasts.
- **[2] Developers expected AI to speed them up by 24%, and even after experiencing the slowdown they still believed AI had sped them up by 20%.**
  > This gap between perception and reality is striking: developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%.
- **[2] The RCT recruited 16 experienced open-source developers, used 246 real issues averaging two hours each, randomized AI use per issue, and paid developers $150/hr.**
  > To directly measure the real-world impact of AI tools on software development, we recruited 16 experienced developers from large open-source repositories (averaging 22k+ stars and 1M+ lines of code) that they’ve contributed to for multiple years. Developers provide lists of real issues (246 total) that would be valuable to the repository—bug fixes, features, and refactors that would normally be part of their regular work. Then, we randomly assign each issue to either allow or disallow use of AI while working on the issue. When AI is allowed, developers can use any tools they choose (primarily Cursor Pro with Claude 3.5/3.7 Sonnet—frontier models at the time of the study); when disallowed, they work without generative AI assistance. Developers complete these tasks (which average two hours each) while recording their screens, then self-report the total implementation time they needed. We pay developers $150/hr as compensation for their participation in the study.
- **[3] The source frames AI coding agents as shifting the bottleneck: code is becoming cheap, while understanding intent, negotiating scope, and governing long-term responsibility remain costly.**
  > AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly.
- **[4] At Meta, significant lines of code per human-landed diff increased 105.9% year over year and per-developer diff volume increased 51%, with agentic AI accounting for over 80% of that growth.**
  > At Meta, significant lines of code per human-landed diff grew by 105.9% year over year and per-developer diff volume rose 51%, with agentic AI responsible for over 80% of that growth.
- **[4] The share of diffs receiving timely review declined, widening the gap between code supply and reviewer capacity.**
  > Meanwhile, the share of diffs receiving timely review has declined, exposing a widening gap between code supply and reviewer bandwidth.
- **[4] RADAR reduced median time to close by over 330% and median diff review wall time by 35%.**
  > RADAR reduces median time to close by over 330% and median diff review wall time by 35%.
- **[6] The paper does not report measured delivery-flow outcomes; it identifies a lack of benchmarks for the complete process.**
  > We also found recurring risks: drift between specification and code, excessive trust in generated artifacts, fragility of community extensions, platform dependence and a lack of benchmarks for the complete process.
- **[7] The reported productivity result comes from analytical productivity modeling rather than a measured delivery-flow study; it estimates that graduated oversight preserves 84–97% of agentic coding velocity, with a central estimate of 91%.**
  > Evaluation through regulatory coverage analysis, comparative framework analysis, and analytical productivity modeling suggests that graduated oversight preserves 84--97% of agentic coding velocity (central estimate: 91%) while maintaining compliance evidence coverage for regulated functions.
- **[8] In the initial feature task, using an AI assistant yielded a 30.7% median reduction in completion time, and habitual AI users showed an estimated 55.9% speedup.**
  > Observational results from Phase 1 corroborate prior research: using an AI assistant yielded a 30.7% median reduction in completion time, and habitual AI users showed an estimated 55.9% speedup.
- **[8] In the downstream randomized trial, evolving AI-co-developed solutions without AI assistance showed no significant differences in completion time or code quality.**
  > Phase 2 revealed no significant differences in subsequent evolution with respect to completion time or code quality.
- **[9] The source states that several studies have highlighted productivity improvements from AI assistants such as GitHub Copilot.**
  > AI assistants like GitHub Copilot are transforming software engineering; several studies have highlighted productivity improvements.
- **[9] The planned experiment will use Bayesian analysis to evaluate differences in completion time, perceived productivity, code quality, and test coverage.**
  > We will employ Bayesian analysis to evaluate differences in completion time, perceived productivity, code quality, and test coverage.
- **[9] The study design is a two-phase controlled experiment with professional developers, where Phase 1 adds a feature to a Java project with or without an AI assistant.**
  > [Method] We will conduct a two-phased controlled experiment involving professional developers. In Phase 1, developers will add a new feature to a Java project, with or without the aid of an AI assistant.
- **[10] The study constructs a dataset of approximately 110,000 open-source pull requests with associated commits, comments, reviews, issues, and file changes, representing millions of lines of source code.**
  > In this work, we construct a novel dataset of approximately $110,000$ open-source pull requests, including associated commits, comments, reviews, issues, and file changes, collectively representing millions of lines of source code.
- **[10] The authors compare five coding agents, including OpenAI Codex, Claude Code, GitHub Copilot, Google Jules, and Devin, on merge frequency, edited file types, and developer interaction signals such as comments and reviews.**
  > We compare five popular coding agents, including OpenAI Codex, Claude Code, GitHub Copilot, Google Jules, and Devin, examining how their usage differs in various development aspects such as merge frequency, edited file types, and developer interaction signals, including comments and reviews.
- **[10] The paper offers longitudinal estimates of survival and churn rates for agent-generated versus human-authored code.**
  > Hence, we offer several longitudinal estimates of survival and churn rates for agent-generated versus human-authored code.
- **[10] The paper emphasizes that code authoring and review are only a small part of software engineering because resulting code must be maintained and updated over time.**
  > Furthermore, we emphasize that code authoring and review are only a small part of the larger software engineering process, as the resulting code must also be maintained and updated over time.
- **[12] Across 11 model-scaffold configurations, most benchmark scores fall between 52.1 and 78.1, and the highest complete-delivery rate is 14.0%.**
  > Across 11 model--scaffold configurations, most scores fall between 52.1 and 78.1; GPT-5.6-Sol achieves the highest complete-delivery rate of 14.0\%.
- **[12] Incomplete implementation and missing integration are the principal delivery bottlenecks; producing individual components does not ensure complete delivery.**
  > Incomplete implementation and missing integration are the principal bottlenecks: producing individual components does not ensure a complete delivery.
- **[13] AI coding assistants increase code production velocity while expanding the volume of code requiring review, making code review a growing bottleneck.**
  > The rise of Artificial Intelligence (AI) coding assistants has intensified this challenge: while these tools increase code production velocity, they also expand the volume of code requiring review, turning code review into a growing bottleneck.
- **[14] The paper frames the shift as moving software engineering from scarce implementation effort to abundant, low-cost code production, making organization of architectures, tools, evidence, and feedback loops the central problem.**
  > Generative AI is shifting software engineering from a practice organized around scarce implementation effort toward one organized around abundant, low-cost code production. This shift changes the central engineering problem: not whether AI can generate useful code, but how engineers organize architectures, tools, evidence, and feedback loops so that AI-mediated development remains inspectable, correctable, and maintainable.
- **[14] In a 12-week first-person case study, one expert engineer used frontier AI coding agents to build a document accessibility remediation system, with an empirical record of 88 field notes, 420 KLOC of production code, and 1.16 MLOC of tests, lints, documentation, and agent tooling.**
  > We study this problem through a first-person case study: a 12-week development effort in which a single expert software engineer used frontier AI coding agents to build a document accessibility remediation system. The empirical record comprises 88 contemporaneous field notes, 420 KLOC of production code, and 1.16 MLOC of tests, lints, supporting documentation, and agent tooling.
- **[16] The paper asserts that coding agents have become the primary means of generating new code in many software projects, and that the resulting change velocity makes tracking the reasons behind changes difficult.**
  > Coding agents have become the primary means of generating new code in many software projects, and the resulting velocity of changes makes keeping track of the reasons behind those changes challenging.
- **[17] The paper reports an industry productivity paradox in which individual developer productivity rises while team throughput, review capacity, and stability degrade because team-scale software engineering discipline is neglected.**
  > However, industry reports a productivity paradox: as individual productivity increases, team throughput, review capacity, and stability degrade because team-scale software engineering discipline is neglected.
- **[20] Recent field studies show meaningful gains in coding activity, but the evidence indicates those gains attenuate sharply between writing code and shipping reliable software.**
  > Recent field studies show meaningful gains in coding activity, but newer evidence also shows that those gains attenuate sharply between writing code and shipping reliable software.
- **[20] Review, integration, testing, security, deployment, and production operations remain constraining stages, while costs shift from per-seat licensing to variable token, tool, sandbox, CI, and rework costs.**
  > Review, integration, testing, security, deployment, and production operations remain constraining stages, while the economics are shifting from predictable per-seat licensing toward variable token, tool, sandbox, CI, and rework costs.
- **[20] The central research question shifts from how much code an agent can generate to production-qualified value per dollar, per reviewer-hour, and per unit of operational risk.**
  > The central research question shifts from how much code an agent can generate to how much production-qualified value an engineering system can deliver per dollar, per reviewer-hour, and per unit of operational risk.
- **[22] The study analysed 11,048 closed agentic pull requests, narrowing to 9,799 human-reviewed PRs, and manually inspected 717 representative cases to recover decision rationale from interaction artifacts.**
  > we conducted a decision-oriented analysis of 11,048 closed Agentic Pull Requests, refined to 9,799 human-reviewed PRs, and manually inspected 717 representative cases to recover decision rationale from interaction artifacts.
- **[22] Agent performance is commonly judged using merge and rejection outcomes alone, which the authors treat as an unreliable proxy.**
  > AI coding agents increasingly submit pull requests (Agentic-PRs) to open-source repositories, yet their performance is commonly assessed using merge and rejection outcomes alone.
- **[23] AI agents produced larger additional increases in code output: 44.0% for lines of code, 36.0% for commits, and 35.7% for pull requests opened.**
  > AI agents lead to larger additional increases in all three measures — 44.0% for lines of code, 36.0% for commits, and 35.7% for pull requests opened.
- **[26] The analysis characterizes GenAI as lowering the cost of producing plausible code while increasing the importance of intent specification, context curation, architecture knowledge, verification, security, provenance, governance, and accountable human judgment.**
  > The analysis shows that GenAI lowers the cost of producing plausible code while increasing the importance of intent specification, context curation, architecture knowledge, verification, security, provenance, governance, and accountable human judgment.
- **[28] The increasing adoption of AI coding agents has increased the number of agent-generated pull requests merged with little or no human intervention.**
  > The increasing adoption of AI coding agents has increased the number of agent-generated pull requests (PRs) merged with little or no human intervention.
- **[29] In a longitudinal within-reviewer analysis of 400 repeat reviewers and 11,429 reviews over seven months, the population-level approval rate for AI-agent code rose from 30.1% to 36.8%, with Wilcoxon signed-rank p <10^{-6} on paired shifts.**
  > We conduct a longitudinal within-reviewer analysis using the AIDev dataset, studying 400 repeat reviewers who collectively submitted 11,429 reviews over a seven-month observation period. Comparing each reviewer's early and late review episodes, we observe a population-level shift in approval rate from 30.1% to 36.8% (Wilcoxon signed-rank p <10^{-6} on paired shifts).
- **[29] Pooled by within-reviewer experience decile, the cumulative approval-rate gap reached +14.5 percentage points from the first to the tenth decile.**
  > Pooled by within-reviewer experience decile, the cumulative gap reaches +14.5 pp from first to tenth decile.
- **[29] The approval shift is experience-driven and persists after controlling for calendar time; it is agent-specific because human PR approval rates decline over the same period, and it is not explained by PR difficulty because median PR size is flat.**
  > This shift is experience-driven (persists after controlling for calendar time), agent-specific (human PR approval rates decline over the same period), and not explained by PR difficulty (median PR size is flat).
- **[30] The paper states that large-scale studies find autonomous coding agents' pull requests are produced faster but accepted less often, a coordination and trust gap that PR-level telemetry cannot explain.**
  > Autonomous coding agents now open millions of pull requests, yet large-scale studies find their PRs are produced faster but accepted less often - a coordination and trust gap that pull-request-level telemetry cannot explain.
- **[30] Using the grite coordination substrate, the share of work that merely re-does a teammate's task fell from 78% to 0% while useful throughput more than tripled, at bounded overhead.**
  > We show that (i) this shared substrate reduces duplicate and conflicting work at bounded overhead - the share of work that merely re-does a teammate's task falls from 78% to 0% while useful throughput more than triples;
- **[30] Every agent's copy of the grite event log converges to the same state with no write silently dropped, whereas a file-based tracker loses concurrent writes.**
  > (ii) every agent's copy of the log converges to the same state with no write silently dropped, where a file-based tracker loses concurrent writes;
- **[32] The paper performs a large-scale real-world repository measurement comparing AI-assisted and human-written code, covering code-level and commit-level metrics such as commit size, frequency, post-commit stability, and security quality.**
  > To close this gap, we perform a first large-scale measurement study of AI-assisted code, in comparison with the human-written, in real-world repositories. We study a comprehensive set of metrics including both code-level aspects (e.g., structural and graph-level complexity, coding style, security quality, etc.) and commit-level characteristics (e.g., commit size, frequency, post-commit stability, etc.).
- **[32] The paper reports first-time observations on code duplication rate, commit size, and stability, extending prior measurement work beyond code-level metrics.**
  > Our results provide new findings and insights: some contrast previous observations in the lab setting (e.g., we conclude that real-world AI-Human differences on code-level metrics are rather small instead of more pronounced), some extend prior results with finer-grained observations (e.g., the variance of security quality across different programming languages), yet more are presented for the first time on aspects not covered before (e.g., code duplication rate, commit size and stability, etc.).
- **[36] In three randomized field experiments combined across 4,867 developers, use of an AI coding assistant increased completed tasks by 26.08% (SE 10.3%).**
  > Though each experiment is noisy, when data is combined across three experiments and 4,867 developers, our analysis reveals a 26.08% increase (SE: 10.3%) in completed tasks among developers using the AI tool.
- **[36] Less experienced developers had higher adoption rates and greater productivity gains from the AI coding assistant.**
  > Notably, less experienced developers had higher adoption rates and greater productivity gains.
- **[39] DORA’s 2025 research finds AI adoption now improves software delivery throughput but still increases delivery instability.** (also [48])
  > AI adoption now improves 
software delivery throughput, a key shift from last year. 
However, it still increases delivery instability.
- **[39] An Adidas gen AI pilot found loosely coupled teams with fast feedback loops saw 20% to 30% productivity gains in commits, pull requests, and feature-delivery velocity, plus a 50% increase in Happy Time; tightly coupled ERP teams saw little or no AI benefit.**
  > In their generative AI (gen AI) pilot, they found that teams who worked in loosely coupled architectures and had fast feedback loops “experienced productivity gains of 
20% to 30%, as measured by increases in commits, pull requests, and overall 
feature-delivery velocity,” and had a 
“50% increase in ‘Happy Time’”— 
more hands-on coding and less 
administrative toil. In contrast, teams with slower feedback loops due to tight coupling with the Enterprise Resource Planning (ERP) systems 
saw little or no AI benefits at all.
- **[39] Without foundational systems, AI creates localized pockets of productivity that are often lost to downstream chaos.**
  > Without this foundation, AI creates localized pockets of 
productivity that are often lost to 
downstream chaos.
- **[40] Microsoft Digital found that improving individual developer productivity did not produce a corresponding boost in team productivity.**
  > “We quickly identified that improving the individual productivity of a developer was not resulting in a boost to team productivity. That was our hard lesson.”
- **[40] The source states that AI tools can generate large amounts of code quickly, but without clear instructions and guardrails, increased coding velocity produces more variability and additional rework.**
  > While AI tools can generate large amounts of code quickly, they depend on clear instructions and guardrails. Teams that can’t consistently communicate intent typically discover that increased coding velocity simply produces more variability and additional rework.
- **[42] Meta says its success metric for AI-native engineering was not code volume but verified, production-ready outcomes that build, pass tests, and survive review.**
  > That experiment needed a definition of success, and ours wasn’t code volume. We measured verified, production-ready outcomes — changes that build, pass tests, and survive review.
- **[42] The source states that without verification, AI-generated code shifts the constraint from writing code to reviewing plausible-looking code that may not work, leading engineers to read, debug, and discard output.**
  > Without verification, AI-generated code creates a familiar problem — plausible output that no one has confirmed actually works, which an engineer then has to read, debug, and often discard. Weak signals don’t remove the constraint; they move it from writing code to reviewing code that looks finished and isn’t.
- **[42] Agents check their own work before human review, so review receives a smaller set of higher-confidence results, and less code is generated and discarded.**
  > Agents check their own work before an engineer sees it, which means what reaches review is a smaller set of higher-confidence results rather than a pile of output to sift through. Less gets generated, and less gets discarded.
- **[42] Meta reports that Forum reached core feature parity with Facebook Groups in eight weeks, with AI handling much routine implementation so engineers could focus on architecture, product decisions, and quality.**
  > **Velocity:** Forum reached core feature parity with Facebook Groups in eight weeks, with AI handling much of the routine implementation so engineers could focus on architecture, product decisions, and quality.
- **[43] The team’s repository reached about one million lines and roughly 1,500 merged pull requests in five months with three engineers, averaging 3.5 PRs per engineer per day; throughput increased after the team grew to seven.**
  > Five months later, the repository contains on the order of a million lines of code across application logic, infrastructure, tooling, documentation, and internal developer utilities. Over that period, roughly 1,500 pull requests have been opened and merged with a small team of just three engineers driving Codex. This translates to an average throughput of 3.5 PRs per engineer per day, and surprisingly the throughput has _increased_ as the team has grown to now seven engineers.
- **[43] The team estimates it built the product in about one-tenth the time hand-writing the code would have taken.**
  > We estimate that we built this in about 1/10th the time it would have taken to write the code by hand.
- **[43] As code throughput increased, the team’s bottleneck shifted to human QA capacity.**
  > As code throughput increased, our bottleneck became human QA capacity.
- **[44] DORA reports that a 25% increase in AI adoption is associated with a 1.5% decrease in delivery throughput and a 7.2% decrease in delivery stability.**
  > AI currently hurts software delivery performance: Contrary to expectations, a 25% increase in AI adoption is associated with a 1.5% decrease in delivery throughput and a 7.2% decrease in delivery stability.
- **[44] DORA's explanation is that faster AI code generation creates larger batches that take longer to review and increase instability.**
  > Because AI allows developers to generate code much faster, it often leads to larger batch sizes, which are slower to review and more prone to creating system instability.
- **[44] DORA reports that developers who trust generative AI accept more suggestions, submit more change lists, and spend less time searching; 39% trust AI outputs only a little or not at all.**
  > Trust directly drives AI productivity: Developers who trust generative AI accept more suggestions, submit more change lists, and spend less time searching for information. However, 39% of developers still trust AI outputs "a little" or "not at all".
- **[45] 73% of respondents use coding assistants and agents daily, and nearly a third of daily users spend upwards of four hours per day using them.**
  > The overwhelming majority of respondents now use coding assistants and agents daily (73%), with nearly a third of daily users spending upwards of four hours.
- **[46] The article states that with AI coding assistants, the bottleneck moved from code writing to code verification.**
  > With AI coding assistants, the bottleneck has moved from code writing to code verification.
- **[46] The article asserts that AI raised the volume of code without raising confidence that the code is correct, secure, or aligned with intent.**
  > The uncomfortable part is that AI raised the volume of code without raising anyone’s confidence that the code is correct, secure, or aligned with what was actually intended.
- **[47] Netflix Commerce reported 32% more pull requests year over year, no Sev 1 incidents in 2026 on a core service, and developer NPS rising from -3 to +25 over three quarters.**
  > Khuzam reported no Sev 1 incidents in 2026 on a core service and 32% more pull requests year over year. Developer NPS rose from -3 to +25 over three quarters.
- **[48] DORA says most organisations will see a temporary productivity dip before long-term AI gains, with three causes: workflow learning curve, verification tax from reviewing AI-generated code, and adapting testing/change approval to increased code volume.**
  > The authors argue that most organisations will experience a temporary productivity dip before achieving long-term gains from AI adoption. This dip has three main causes: the learning curve as teams adapt their workflows, the verification tax imposed by reviewing AI-generated code, and the need to adapt downstream processes such as testing and change approval to handle increased code volumes.
- **[49] GitHub data cited in the article shows PRs opened increased fivefold, with PRs and commits nearly doubling from the end of 2025.**
  > Over that time, the number of PRs opened has increased fivefold, which is a lot! And growth sped up from the end of 2025, when PRs and commits nearly doubled _just_ in that period alone!
- **[50] Sivasubramanian’s blog post reported that teams across Amazon that restructured workflows around AI saw a median 4.5x productivity gain, with some exceeding 10x, while teams that simply added AI tools to existing workflows did not see the same results.**
  > In [a blog post](https://aws.amazon.com/blogs/machine-learning/how-frontier-teams-are-reinventing-ai-native-development/) published last week, Sivasubramanian wrote that teams across the company that restructured their workflows around AI saw a median 4.5x productivity gain, with some exceeding 10x gains. The teams that simply added AI tools to their existing way of working didn’t see the same results.
- **[50] The Bedrock inference engine rebuild was done by six engineers in 76 days, versus an original expectation of 30 developers over 12 to 18 months.**
  > The internal Amazon team that rebuilt the inference engine for the company’s Bedrock platform for AI models did it with six engineers in 76 days, a project originally expected to take 30 developers 12 to 18 months.
- **[50] One engineer shipped a complex cross-platform notification feature for Kiro in a day and a half after it had been estimated at four weeks.**
  > One engineer prototyped a complex cross-platform notification feature for Kiro that had been estimated at four weeks of work, and shipped it in a day and a half.
- **[50] The Amazon Quick desktop app was built by about six engineers, reached 200 internal users in six weeks and 10,000 in ten weeks, and shipped on April 28, three months after starting.**
  > He pulled together a team of about six engineers to build it. Six weeks later, 200 people inside Amazon were using it. Ten weeks in, it was up to 10,000 internally. The team circled back to write the PRFAQ after the product was already in beta, to help refine their approach to the external launch. They shipped on April 28, three months after they got started.
- **[51] Task completion rose 34%, epics completed per developer rose 66%, and code-specific tasks rose 210%.**
  > Task completion is up 34%. Epics completed per developer are up 66%. Tasks involving code speci fi cally have increased 210%.
- **[51] Code churn, defined as lines deleted to lines added for merged code per quarter, increased 861% under high AI adoption.**
  > Code churn, de fi ned as the ratio of lines deleted to lines added for merged code in a given quarter, has increased 861% under high AI adoption.
- **[51] Median review time increased 5X and 31% more PRs merged without any review.**
  > Median review time has increased 5X. 31% more PRs are merging without any review.
- **[52] Atlassian's 2025 developer survey reports that 68% of developers and 70% of managers save at least 10 hours per week with AI tools.**
  > **68% of developers and 70% of managers report saving 10 or more hours per week with AI tools.**
- **[52] At the same time, 50% of developers report losing at least 10 hours per week to non-coding tasks caused by poor information access, fragmented tools, and context switching.**
  > At the same time, **50% of developers report losing 10 or more hours per week to non-coding tasks** driven by poor information access, fragmented tools, and constant context switching.
- **[52] Developers spend around 16% of their time coding, and Atlassian says the bottleneck is usually the other 84% of their week.**
  > Developers spend **around 16% of their time actually coding**, which is already the fastest part of the software delivery process. The bottleneck is almost always in the **other 84%** of their week.
- **[54] Heavy AI users out-produce non-users by 4–10x, but most of that gap predates AI; versus their own past performance, the velocity gain is 25%.**
  > heavy AI users out-produce non-users by 4–10x, but most of that gap pre-dated AI — compared to their past selves, heavy AI users enjoyed a more modest 25% velocity gain.
- **[54] The source reports concurrent increases in within-commit copy/paste (+41%), code block duplication (+81%), error-masking constructs (+47%), and two-week code churn (+15%).**
  > Concurrently, we observe a concerning rise in within-commit copy/paste (**+41%**), code block duplication (**+81%**), error-masking constructs (**+47%**), and two-week code churn (**+15%**).
- **[55] DX's prior research found that the median engineering organization sees a 7.8% increase in PR throughput from AI, which it describes as real but more modest than headline claims.**
  > Our prior research found that the median engineering organization sees a 7.8% increase in PR throughput from AI. Real, but more modest than headline claims would suggest, and consistent with the idea that the surrounding system is absorbing much of the individual-level efficiency.
- **[55] Among developers who reached peak time savings from AI, two-thirds reported lower time savings in subsequent quarters.**
  > Of those developers who reached peak time savings, two-thirds (66.1%) reported lower time savings in the quarters that followed.
- **[55] Among developers who hit the highest time-savings band in one quarter or less, just over half did not report that level of savings in future quarters.** (also [55])
  > Among developers who hit the highest time-savings band in one quarter or less, just over half (50.5%) did not report that level of savings in future quarters.
- **[56] AI-DLC is claimed to accelerate development velocity by generating and refining requirements, stories, designs, code, and tests, letting tasks that took weeks be done in hours or days.**
  > ****Velocity:**** The foremost benefit that AI-DLC offers is acceleration in development velocity, as AI rapidly generates and refines artifacts, such as requirements, stories, designs, code, and tests allowing product owners, architects, and developers to complete tasks in hours or days that previously took weeks.
- **[56] The source states that AI-assisted and AI-autonomous development approaches have both produced suboptimal velocity and software quality.**
  > Both these approaches have produced suboptimal results in terms of velocity and software quality that AI-DLC aims to address.
- **[57] Thoughtworks Technology Radar volume 34 warns that AI generates increasingly larger amounts of code, causing accumulating cognitive debt and a wider gap between humans and software systems.**
  > The report notably warns of accumulating cognitive debt as AI generates increasingly larger amounts of code and, in so doing, introduces a wider gap between humans and software systems.
- **[57] The source frames a paradox: agentic systems make code creation quicker, but established practices for discipline and rigor are more vital than ever.**
  > The takeaway for technologists and business leaders is a striking paradox; as agentic systems make it easier to create code quickly, traditional and established practices that ensure discipline and rigor are more vital than ever.
- **[58] Developers with Copilot showed no significant change in coding speed, PR cycle time, or PR throughput; Copilot neither helped nor hurt these efficiency metrics.**
  > **No significant change to efficiency metrics with GenAI** — Developers with Copilot did not see an increase in **coding speed**. In terms of **pull request (PR) cycle time** (the time to merge code into a repository) and **PR throughput** (number of pull requests merged), Copilot neither helped nor hurt developers.
- **[58] After Copilot implementation, developers saw a 41% increase in bugs within pull requests, suggesting a possible impact on code quality.**
  > **41% increase in bug rate** — Post-Copilot implementation, developers saw a 41% increase in bugs within pull requests — suggesting the tool may impact code quality.
- **[59] The source states that initial AI coding-speed gains are promising but do not automatically translate into bottom-line results.**
  > While initial gains in coding speed are promising, they don't automatically translate to the bottom line.
- **[59] The source describes an initial “productivity dip” during a new AI rollout.**
  > Whether you are managing the initial "productivity dip" of a new rollout or looking to defend your budget for the next fiscal year, this guide provides the calculations and conversation starters you need.
- **[59] The source frames an explicit “tuition cost” budget as necessary before long-term ROI materializes.**
  > Learn why explicitly budgeting for this "tuition cost" is a necessary investment in learning before long-term ROI materializes.
- **[59] The source claims the greatest returns come from reducing unnecessary rework to reclaim engineering capacity and expand output without increasing overhead.**
  > Discover why the greatest returns come from reducing unnecessary rework to reclaim engineering capacity—effectively expanding your team’s output without increasing overhead.
- **[60] Stripe says more than 1,300 PRs merged weekly are completely minion-produced and human-reviewed, with no human-written code, up from 1,000 as of Part 1.**
  > Over 1,300 Stripe pull requests (up from 1,000 as of Part 1) merged each week are completely minion-produced, human-reviewed, but containing no human-written code.
- **[61] METR's earlier paper found that AI tools caused a 20% slowdown in completing tasks among experienced open-source developers, using data from February to June 2025.**
  > which found the use of AI tools caused a 20% slowdown in completing tasks among experienced open-source developers, using data from February to June 2025.
- **[61] METR's early 2025 study found AI use caused tasks to take 19% longer, with a confidence interval from +2% to +39%.**
  > Our early 2025 study found the use of AI causes tasks to take 19% longer, with a confidence interval between +2% and +39%.
- **[61] For the subset of original developers in the later study, METR estimated a speedup of -18%, with a confidence interval from -38% to +9%.**
  > For the subset of the original developers who participated in the later study, we now estimate a speedup of -18% with a confidence interval between -38% and +9%.
- **[61] Among newly recruited developers, METR estimated a speedup of -4%, with a confidence interval from -15% to +9%.**
  > Among newly-recruited developers the estimated speedup is -4%, with a confidence interval between -15% and +9%.
- **[61] METR observed more developers declining to participate because they did not want to work without AI, which likely biases the AI-assisted speedup estimate downward.**
  > The primary reason is that we have observed a significant increase in developers choosing not to participate in the study because they do not wish to work without AI, which likely biases downwards our estimate of AI-assisted speedup.
- **[61] When surveyed, 30% to 50% of developers reported withholding some tasks because they did not want to do them without AI.**
  > When surveyed, 30% to 50% of developers told us that they were choosing not to submit some tasks because they did not want to do them without AI.
- **[62] By April 2026, in one month, Mux had 600+ users including engineers, PMs, and designers, with 335 active and 197 power users; it powered 5,068 merged PRs across 461 repositories and 10 orgs.**
  > By April 2026 - in one month - Mux had already powered:

*   **600+ users** including engineers, PMs, and designers, with 335 active and 197 power users. 
*   **5,068 merged PRs** across 461 repositories and 10 orgs.
- **[62] Mux users had 3.5x more merged PRs per engineer than baseline, with 39.6 versus 11.4.**
  > *   **3.5x more merged PRs per engineer** for Mux users compared to baseline: 39.6 vs 11.4.
- **[62] The bottleneck moved from how fast code could be written to how many things one engineer could orchestrate at once.**
  > The bottleneck had moved. It was no longer how fast we could write code. It was how many things one engineer could orchestrate at once.
- **[63] The source says organisations are measuring AI productivity by volume of generated code or content produced by a button click, and calls this trajectory deeply misguided.**
  > We see a wild rush where organisations measure productivity by "a zillion lines of code" or content generated by a button click.

At Team Topologies, we believe this trajectory is deeply misguided.
- **[64] The author asserts that in 2025 code-production economics flipped: generating code became effectively free and instant, and lines of code became disposable and regenerable.**
  > What happened in 2025 was this: **the economics of code production were turned upside down.** Instead of being very hard, time-consuming, and expensive to generate code, it became effectively free and instant. Lines of code went from being treasured, reused, cared for and carefully curated, to being disposable and regenerable, practically overnight.
- **[65] Deploy frequency rose from about ~6 per week to 200-400 per week; headcount doubled; even doubling prior deploys left 20-30x year-over-year growth; the author attributes this to a two-month deployment/run-migration overhaul done 90% by two infrastructure staff.**
  > A year ago, we deployed manually, and deployed ~6 times a week, and now we deploy 200-400 times a week. Our engineering headcount has doubled, but even if we double the prior deploys, we’re still up 20-30x year-over-year. This is due to a complete overhaul of how we deploy and run migrations, and this migration was done over two months and done 90% by two folks on our infrastructure team.
- **[65] Daily use of Claude Code or Cursor rose from about 25% in early January to 100% by end February without a top-down mandate; nearly every PR is now written by harnesses at least in the first pass.**
  > The first day of January, about 25% of folks on our team used Claude Code or Cursor every day. By the end of February, 100% did. We did this without any top-down mandate, just by making the tooling good and chatting with non-adopters to remove sources of friction. Pretty much every PR is written by harnesses now, at least in the first pass.
- **[65] First-pass code is nearly free, but working code is not free and its cost depends on the development harness.**
  > While 1st-pass code is nearly free, the cost of working code depends on your development harness, and is not free.
- **[66] Over four quarters, curl’s inbound security report volume rose sharply while peer open source bounty programs such as Ruby, Node, and Rails stayed mostly flat or declined slightly.**
  > Over the past four quarters, curl’s inbound report volume has risen sharply, while other bounty-paying open source programs in the cohort, such as Ruby, Node, and Rails, have not seen a meaningful increase and have remained mostly flat or declined slightly.
- **[66] Handling never-ending slop submissions imposes a serious mental toll and can take a long time to debunk, wasting maintainer time and energy.**
  > The never-ending slop submissions take a serious mental toll to manage and sometimes also a long time to debunk. Time and energy that is completely wasted while also hampering our will to live.
- **[67] Within three months of launching Block's AI Champions program, AI-authored code increased by 69%, reported time savings increased by 37%, and automated PRs increased 21×.**
  > Within three months of launching the Champions program, AI-authored code jumped by 69%, reported time savings increased 37%, and automated PRs increased 21×.
- **[68] Shopify says one in eight merged pull requests across the company is coauthored by River.**
  > Now, one in eight merged pull requests across Shopify is coauthored by it.
- **[68] In a recent 30 day period, Shopify recorded 59,918 River sessions in 5,170 Slack channels touching 7,000+ people, with 3,536 River-coauthored pull requests merged.**
  > In a recent 30 day period: **59,918**River sessions happened in **5,170** Slack channels, touching the work of **7,000+** people inside the company (~1,200 more than when Tobi posted about River in early May). **3,536**River-coauthored pull requests merged in that window.
- **[69] The author identifies code review speed as the natural bottleneck for AI-generated code, especially when agents can churn out changes faster than one person can keep up.**
  > I was pretty skeptical about this at first. AI-generated code needs to be reviewed, which means the natural bottleneck on all of this is how fast I can review the results. It’s tough keeping up with just a single LLM given how fast they can churn things out, where’s the benefit from running more than one at a time if it just leaves me further behind?
- **[70] AI coding tools eliminated the code production bottleneck and moved the constraint downstream to human review, testing, and integration.**
  > AI eliminated the code production bottleneck, and the constraint moved downstream to the humans who have to review, test, and integrate all that output.
- **[70] A massive AI-generated pull request exhausted the existing workflow, leaving the main branch broken and staging stuck on orange alert by week's end.**
  > By the week's end, nothing was testable as a whole. The main branch was broken, staging was stuck on orange alert
- **[71] Early augmented-coding attempts accumulated enough complexity that the agent stalled, forcing more human design intervention to keep the agent from coding ahead.**
  > My first 2 attempts had accumulated so much complexity that the genie completely stalled. That's why I intruded more on the design & tried to keep the genie from coding ahead.
- **[72] Zapier reports an 11% increase in developer productivity in 2025 from tools and processes around Cursor, Claude Code, and GitHub Copilot.**
  > We've increased developer productivity by 11% in 2025 with tools and processes around Cursor, Claude Code, and GitHub Copilot.

## q2. Which artifact carries intent in teams that ship with agents (specification, ADR, AGENTS.md) and what evidence says it works?

- **[3] In KPR, agents distill sources into a human-confirmed knowledge package rendered as reviewer-facing artifacts such as design memos, risk checklists, test plans, or implementation briefs.**
  > Agents distill these sources into a human-confirmed knowledge package and render it into reviewer-facing forms such as design memos, risk checklists, test plans, or implementation briefs.
- **[3] The paper's stated evidence includes a minimal controlled simulation pilot over seven merged public pull requests and an evaluation agenda.**
  > We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda.
- **[6] Among process-adopting frameworks, the isolated prompt loses centrality, while persistent artifacts, work contracts, traceability, and human review become ambiguity-reducing coordination mechanisms.**
  > Among frameworks that already adopt some process there is convergence: the isolated prompt loses centrality, and persistent artifacts, work contracts, traceability and human review become mechanisms that reduce ambiguity and coordinate agents.
- **[6] The paper proposes a six-dimension taxonomy covering specification, context, roles, execution, validation, and portability.**
  > Our central contribution is a six-dimension process taxonomy: specification, context, roles, execution, validation and portability, with a scoring rubric that turns it into a replicable instrument.
- **[7] Each oversight tier is required to define evidence artifacts for compliance auditability; the source does not name specification, ADR, or AGENTS.md as the intent artifact.**
  > Each tier defines required evidence artifacts for compliance auditability.
- **[12] The benchmark targets incremental PRD fulfillment, where issue resolution, development from scratch, and isolated tests leave important requirements underexplored or incompletely evidenced.**
  > Issue resolution and development from scratch leave incremental PRD fulfillment underexplored, while isolated tests provide incomplete evidence of business and integration requirements.
- **[12] The benchmark measures PRD fulfillment by combining requirement reconstruction, criterion construction, and evidence-based evaluation.**
  > It combines requirement reconstruction, criterion construction, and evidence-based evaluation to measure PRD fulfillment and connect delivery gaps to agent behavior.
- **[14] The paper develops a candidate middle-range theory of governance conversion, a process model for how high-velocity agentic implementation becomes governable.**
  > From this record, we develop a candidate middle-range theory of governance conversion, expressed as a process model explaining how high-velocity agentic implementation becomes governable.
- **[14] The model claims that engineering judgment sustains agentic velocity by converting recurring structural failure classes into durable governance mechanisms.**
  > The model explains how agentic implementation velocity surfaces recurring structural failure classes, and how engineering judgment sustains velocity by converting those failures into durable governance mechanisms.
- **[15] Practitioners agreed specifications should capture intent, but many also included implementation details and used spec-driven development selectively, mainly for new features.**
  > Practitioners agreed that specs should capture intent, but many also included implementation details, used SDD selectively and mainly for new features, and reported more reliable agent behavior alongside greater planning and review costs.
- **[15] Implementation detail may help agents while making specifications prone to decay; tool-specific record structures shape what people and agents see; spec-code checks were described mainly when changes were completed rather than over time.**
  > Our findings show that implementation detail may help agents while making specs prone to decay, that tool-specific record structures shape what people and agents see, and that participants described spec-code checks mainly when changes are completed rather than over time.
- **[16] MOOSEDev captures architectural decisions, lessons, constraints, and rationales in a knowledge graph exposed to coding agents through an MCP interface.**
  > The system captures architectural decisions, lessons, constraints, and rationales in a knowledge graph exposed to agents via a Model Context Protocol (MCP) interface.
- **[16] The project-memory records carry lifecycle status, provenance, and supersession links and are queried through MOOSE, a neurosymbolic engine that treats the symbolic layer as primary.**
  > Records carry lifecycle status, provenance, and supersession links, queryable via MOOSE, a proprietary neurosymbolic engine that treats the symbolic layer as the primary reasoning substrate.
- **[16] The evaluation compared MOOSEDev with a production vector-memory tool on a neutral public corpus of 835 typed records.**
  > We compared MOOSEDev against a production vector-memory tool on a neutral public corpus of 835 typed records.
- **[16] MOOSEDev returned the expected answer set essentially in full, scoring 0.98 to 1.00 on supersession, set-completeness, and negation questions, while the baseline's top-k retrieval surfaced only 6% to 27%.**
  > MOOSEDev returned the expected answer set essentially in full (0.98-1.00) on supersession, set-completeness, and negation questions, whereas the baseline's top-k retrieval surfaced between 6% and 27%.
- **[16] Relevance recall and token cost were largely equivalent between MOOSEDev and the baseline vector-memory system.**
  > Conversely, relevance recall and token cost were largely equivalent between the two systems.
- **[17] The paper's proposed intent artifact is the specification, described as the contract substrate between humans and agents within a socio-technical model of SDD.**
  > Using a comparative characterization of the paradigm progression as conceptual framing, the article presents (i) a socio-technical model of SDD in which specifications act as the contract substrate between humans and agents; (ii) an operational characterization of the harness, distinguishing the technical harness around the agent from the methodological harness around the team, with worked examples; and (iii) a typology of five human--agent interaction patterns through which the human role is redefined.
- **[24] The paper formalises SDAD as combining disciplined up-front formalisation with high-velocity implementation through intent capture, machine-readable specification, agentic synthesis, and independent multi-agent verification under human sign-off.**
  > This report formalises Spec-Driven Agentic Development (SDAD) as a synthesis of disciplined up-front formalisation and high-velocity implementation: intent capture, machine-readable specification, agentic synthesis, and independent multi-agent verification under human sign-off.
- **[24] The paper argues that specification quality becomes the execution fuel for autonomous delivery because agents can ingest substantial Functional Requirement Documents and repository context in one workflow.**
  > Rich context handling and multi-step reasoning now allow substantial Functional Requirement Documents (FRDs) and repository context to be ingested in a single workflow, making specification quality the execution fuel for autonomous delivery.
- **[24] The paper's stated position is that agentic speed does not eliminate engineering discipline but relocates it upstream into specification precision, explicit gates, and auditable provenance.**
  > Overall, the paper argues that agentic speed does not eliminate engineering discipline; it relocates discipline upstream into specification precision, explicit gates, and auditable provenance.
- **[26] The source frames intent-centric human-agent work as shaped by natural language, repository context, tools, tests, and governance.**
  > Generative artificial intelligence (GenAI) and agentic systems are moving software engineering from code-centric production toward intent-centric human-agent work in which natural language, repository context, tools, tests, and governance shape delivery.
- **[35] The proposed framework carries intent in a machine-readable spec graph with explicit contract/design separation and uses a context assembler, vertical-slice protocol, and blocking drift gate.**
  > We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition.
- **[35] The design explicitly synthesises ADRs and fitness functions into a code-coupled, machine-enforced framework without heavyweight RUP/MDA overhead.**
  > The design synthesises well-established software engineering principles (Parnas information hiding, C4, ADRs, Walking Skeleton, Reflexion Models, Fitness Functions) into a lean, code-coupled, machine-enforced whole -- without the overhead of heavy-weight frameworks such as RUP or MDA.
- **[40] Microsoft Digital adopted spec-driven development, treating specifications as the primary artifact and anchoring development around a living specification that captures business intent and acceptance criteria before implementation.**
  > Exploring that concept led us to spec-driven development (SDD), an AI-native engineering approach that treats specifications as the primary artifact in the software development lifecycle. Instead of relying on code, documents, or prompts as the main source of truth, our teams now anchor development around a living specification, which captures the business intent and acceptance criteria before implementation begins.
- **[40] In Microsoft Digital's SDD workflow, specifications capture business goals, user requirements, edge cases, and acceptance tests; they are version-controlled, continuously updated, and guide major lifecycle decisions.**
  > At Microsoft Digital, our developers and PMs begin by creating specifications that capture business goals, user requirements, edge cases, and acceptance tests. These specifications are version-controlled and continuously updated as the project evolves. Rather than serving as static documentation, they guide every major decision throughout the lifecycle.
- **[41] The docs recommend turning an interview into SPEC.md, starting a fresh session to build from it, and later pointing the reviewer at that file as the written definition of done.**
  > Once `SPEC.md` exists, start a fresh session to build from it, so the build begins with a clean context and a written definition of done. It’s also the file you’ll point the reviewer at later, in [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run).
- **[41] CLAUDE.md is loaded into every session, so the docs advise keeping it to non-code-discoverable project facts rather than general guidance.**
  > Claude Code loads [`CLAUDE.md`](https://code.claude.com/docs/en/memory) into every session, which means every line in it takes a little of Claude’s attention on _every_ task, whether it’s relevant or not. That’s why the file works best when it only holds what Claude couldn’t work out from the code itself:
- **[41] Team procedures and knowledge are stored as skills in `.claude/skills/<name>/SKILL.md`.**
  > That kind of knowledge goes in a [skill](https://code.claude.com/docs/en/skills): a procedure or a piece of team knowledge saved at `.claude/skills/<name>/SKILL.md`.
- **[42] Meta treats planning as technical specification and invests in precise upstream decomposition and machine-readable context because ambiguity causes agent failure.**
  > Agentic execution requires extreme precision. Ambiguity that an engineer might resolve through intuition results in agent failure. We invested in rigorous upstream decomposition and machine-readable context, which tightened the engineering loop for engineers and agents alike.
- **[43] Instead of a monolithic AGENTS.md encyclopedia, a roughly 100-line AGENTS.md is injected as a table-of-contents map, while a structured docs/ directory is the system of record.**
  > So instead of treating `AGENTS.md` as the encyclopedia, we treat it as **the table of contents**.

The repository’s knowledge base lives in a structured `docs/` directory treated as the system of record. A short `AGENTS.md` (roughly 100 lines) is injected into context and serves primarily as a map, with pointers to deeper sources of truth elsewhere.
- **[43] The team enforces the knowledge base with linters and CI checks, plus a recurring doc-gardening agent that opens fix-up PRs for stale documentation.**
  > We enforce this mechanically. Dedicated linters and CI jobs validate that the knowledge base is up to date, cross-linked, and structured correctly. A recurring “doc-gardening” agent scans for stale or obsolete documentation that does not reflect the real code behavior and opens fix-up pull requests.
- **[46] In the author's study, a specification has three layers: business requirements and rules, a high-level design defining components and interfaces, and a low-level design pinning down method invariants.**
  > In this study a specification has three layers: the specification itself (the business requirements and rules), a high-level design (HLD) that defines the components and their interfaces, and a low-level design (LLD) that pins down the concrete invariants each method must uphold.
- **[46] The study found that a specification baseline did not make reviewers better bug-finders, but made drift review contract-anchored, attributable, and higher-confidence at measurable time and cost.**
  > A specification baseline did not make reviewers better bug-finders. It turned drift review into a contract-anchored, attributable, higher-confidence activity, but at a measurable time and cost.
- **[46] Authoring the specification and then implementing from it in a fresh generation step moved the outcome by treating the spec as a governing artifact rather than inline prompt text.**
  > The approach of authoring the specification and then implementing from it in a fresh generation step moved the outcome, by treating the spec as a governing artifact rather than inline prompt text.
- **[47] The team created 45 architecture decision records written for both people and agents, covering context, decision, pattern, anti-pattern, AI usage notes, and links to docs/code, and shipping in almost every repository.**
  > The team wrote 45 [architecture decision records](https://adr.github.io/), each "written for people and for agents." Each record covers the context, the decision, a pattern and an anti-pattern, and AI usage notes on what an agent should do. It also links to related docs and code, and the records now ship inside almost every repository.
- **[47] AGENTS.md acts like robots.txt to keep the ADRs and more than 300 other documents findable, and coding agents read it before anything else.**
  > To keep those records and more than 300 other documents findable, the team borrowed from how search engines read a site. An AGENTS.md file, the [project instructions file](https://www.infoq.com/news/2025/08/agents-md/) that coding agents read before anything else, plays the part of robots.txt.
- **[49] One approach is to spend much more time on the plan upfront to produce a detailed spec before implementation.**
  > **Review the plan:**spend a lot more time on the plan than before, to get a much more detailed spec.
- **[50] Sivasubramanian said the bottleneck is not build time but crafting the right specification, tests, and product/customer experience.**
  > “The bottleneck is not about the time it takes to build something,” Sivasubramanian said. “The bottleneck is about crafting the right specification and the tests and the right product and customer experience.”
- **[50] In his Kiro rebuild, Sivasubramanian spent four nights babysitting the agent; after realizing it lacked tools to test its own output, he wrote the right spec and set up the testing environment, and the task finished in about two hours.**
  > He and one of Amazon’s earliest distinguished engineers, Allan Vermeulen, had spent four months on the original. Sivasubramanian figured the agent would make quick work of it. Instead, he spent four nights going back and forth, babysitting each step. On the fifth night, he realized the problem: he hadn’t given the agent the tools to test its own output. Once he wrote the right spec and set up the testing environment, it was done in about two hours.
- **[52] Atlassian recommends capturing decisions and tradeoffs in a place where AI can later retrieve and summarize them for new stakeholders.**
  > **Capturing** decisions and tradeoffs in a place where AI can later retrieve and summarize them for new stakeholders
- **[56] AI-DLC maintains persistent context by storing plans, requirements, and design artifacts in the project repository across phases.**
  > AI saves and maintains persistent context across all phases by storing plans, requirements, and design artifacts to your project repository, ensuring seamless continuation of work across multiple sessions.
- **[57] The report says teams are beginning to iterate on coding-agent harnesses with feedforward controls such as Agent Skills and spec-driven development, plus feedback controls such as mutation testing.**
  > Teams are beginning to iterate on coding agent harnesses. These include feedforward controls like Agent Skills and spec-driven development, as well as feedback controls like mutation testing, which trigger self-correction before human review.
- **[60] Agent rule files such as CLAUDE.md or AGENTS.md are used to give agents codebase guidance automatically as they traverse the directory structure.**
  > various agent rule formats—think CLAUDE.md or AGENTS.md—allow agents to “learn” about the codebase automatically as they traverse its directory structure.
- **[60] Stripe avoids unconditional global rules due to repository size and almost exclusively gives minions context from rule files scoped to subdirectories or file patterns, attached automatically during traversal.**
  > Due to the size of our repositories, we use unconditional global rules very judiciously, since otherwise the agent’s whole context window would fill with rules before the agent even starts. Instead, we almost exclusively give minions context from files that are scoped to specific subdirectories or file patterns, automatically attached as the agent traverses the filesystem.
- **[60] Stripe orchestrates minions with 'blueprints', code-defined workflows that combine deterministic code nodes with agent loops for flexibility.**
  > Blueprints are workflows defined in code that direct a minion run. Blueprints combine the determinism of workflows with agents’ flexibility in dealing with the unknown: a given node can run either deterministic code or an agent loop focused on a task.
- **[62] Mux's value is in plugins, skills, and integrations that encode Coinbase shipping practices and repo conventions into reusable commands, including team-specific review automation.**
  > It's in the institutional knowledge that gets baked in. The plugins, skills, and integrations engineers built on top of Mux encode how Coinbase actually ships software: dispatching to our internal cloud agent fleet, deploying through Codeflow, automating team-specific review flows, encoding repo conventions into reusable commands.
- **[63] The source says AI systems require clearly defined, long-lived responsibility boundaries and highly constrained, structured context, analogous to managing human cognitive load.**
  > Instead, AI systems require clearly defined, long-lived boundaries of responsibility and highly constrained, structured context. Just as humans work best when their cognitive load is managed, AI agents work best when the context injected into their operating window is strictly defined and focused.
- **[63] The source recommends consuming clean interfaces from a platform so that both human teams and AI agents have their cognitive and contextual loads minimised.**
  > By consuming clean interfaces from the platform, both human teams and AI agents have their cognitive and contextual loads minimised, enabling a safe, rapid flow of value.
- **[64] The author proposes reviewable architecture diagrams/artifacts as intent carriers, with code regenerated from architecture changes rather than architecture being inferred from code.**
  > Where are the artifacts I can review and discuss to understand how our architecture is evolving? Where are our architecture artifacts, period? What if we could discuss and converge on an architecture diagram, and the code could be regenerated from changes to the architecture, instead of the architecture being kinda-sorta inferred from the code?
- **[65] Design documents and PRs thrown over the wall to other teams did not go anywhere; slop PRs and design documents are cheap but actively harmful, requiring cleanup and poisoning the LLM context.**
  > Where we’ve tried to throw design documents and PRs “over the wall” to engineers on other teams, they’ve never gone anywhere. Slop pull requests and design documents are cheap, but are actively harmful. They not only have to be cleaned up and repaired, their context poisons the LLM, leading to worse outcomes than starting over.
- **[67] Block adopted the RPI context-engineering approach and says it gave teams a consistent way to get high-quality PRs from agents and prevented AI drift.**
  > It gave teams a consistent way to get [high quality PRs](https://block.github.io/goose/docs/tutorials/rpi/#final-result) out of agents and prevented the usual AI drift.
- **[68] Shopify’s monorepo World contains code plus skills, conventions, intent documents, runbooks, AGENTS.md files, and written-down zone knowledge.**
  > World contains code. It also contains skills, conventions, intent documents, runbooks, `AGENTS.md` files, and written-down zone knowledge.
- **[68] When a River problem is solved, the team leaves a memory that later sessions reuse, such as a skill update or an AGENTS.md diff.**
  > When someone solves a problem with River, they leave a memory behind: a pebble, a skill update, an `AGENTS.md` diff, sometimes a whole new shared skill. The next session uses it.
- **[69] Code generated from the reviewer’s own detailed specification is less effort to review because the goals and approach are already decided.**
  > Code that started from your own specification is a lot less effort to review. If you already decided what to solve, picked the approach and worked out a detailed specification for the work itself, confirming it was built to your needs can take a lot less time.
- **[69] Telling the model exactly how to build something reduces the review burden for the resulting changes.**
  > If I tell them _exactly_ how to build something the work needed to review the resulting changes is a whole lot less taxing.
- **[70] The team shifted review focus away from style on agent-written code and toward architectural blueprints as the carrier of intent.**
  > We stopped nitpicking style on disposable, agent-written code and shifted focus to architectural blueprints.
- **[71] The augmented-coding workflow uses plan.md as the intent artifact: the agent is told to follow plan.md, take the next unmarked test, implement the test, and write only enough code to make it pass.**
  > Always follow the instructions in plan.md. When I say "go", find the next unmarked test in plan.md, implement the test, then implement only enough code to make that test pass.
- **[71] Augmented coding is defined as caring about code quality, complexity, tests, and coverage, in contrast to vibe coding, which cares only about system behavior.**
  > In vibe coding you don't care about the code, just the behavior of the system. If there's an error, you feed it back into the genie in hopes of a good enough fix. In augmented coding you care about the code, its complexity, the tests, & their coverage. The value system in augmented coding is similar to hand coding--tidy code that works. It's just that I don't type much of that code.
- **[74] The repository describes itself as a toolkit for getting started with Spec-Driven Development (SDD) or other processes.**
  > 💫 Toolkit to help you get started with SDD or any other process!
- **[74] A commit message records running the full SDD workflow to produce spec.md with 4 user stories, 31 functional requirements, and 8 success criteria, plus plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md with 43 dependency-ordered tasks, and a v1.0.0 Spec Kit Constitution.**
  > spec.md (4 user stories, 31 FRs, 8 success criteria) + clarifications - plan.md, research.md, data-model.md, contracts/, quickstart.md - tasks.md (43 dependency-ordered tasks, organized by user story) - Spec Kit Constitution v1.0.0
- **[74] The repository's commit history records an AGENTS.md pitfall about a test-venv gotcha, showing AGENTS.md is used as an agent/contributor guidance artifact.**
  > AGENTS.md pitfall on the test-venv gotcha

## q3. How is code review reorganised (risk tiers, agent pre-review, human-on-the-loop) and what does the new review cost?

- **[1] The authors recommend CRAs augment rather than replace human reviewers, with human involvement remaining critical.**
  > For practitioners, our results indicate that CRAs should augment rather than replace human reviewers and that human involvement remains critical for effective and actionable code review.
- **[3] KPR separates two review decisions that traditional pull requests often collapse: whether knowledge should enter the project and whether a particular implementation should be merged.**
  > KPR therefore separates two decisions that traditional pull requests often collapse: whether the knowledge should enter the project, and whether a particular implementation should be merged.
- **[3] Implementation is regenerated by a project-owned trusted coding agent inside the receiving project's environment under repository context, engineering conventions, tests, and security policy.**
  > A project-owned inner trusted coding agent then regenerates candidate code inside the receiving project's environment under repository context, engineering conventions, tests, and security policy.
- **[4] RADAR is a multi-stage review funnel that classifies diffs by authorship and source type, applies eligibility gates, static heuristics, a machine-learned Diff Risk Score, LLM-based automated review, and deterministic validation before landing.**
  > We deployed RADAR (Risk Aware Diff Auto Review), a multi-stage funnel that classifies each diff by authorship and source type, applies eligibility gates, static heuristics, a machine-learned Diff Risk Score, LLM-based Automated Code Review, and deterministic validation before landing qualifying changes.
- **[4] Relaxing the Diff Risk Score threshold from the 25th to the 50th percentile increased the approve rate to 60.31%.**
  > Relaxing the Diff Risk Score threshold from the 25th to the 50th percentile increased the approve rate to 60.31%.
- **[4] RADAR had reviewed more than 535,000 diffs and landed more than 331,000 of them.**
  > RADAR has reviewed 535K+ diffs and landed 331K+.
- **[5] LLM-based coding tools can let non-expert users generate routine automation scripts that enter enterprise workflows without meaningful security review.**
  > LLM-based coding tools enable non-expert users to generate routine automation scripts that may enter enterprise workflows without meaningful security review.
- **[5] In the study, Claude Code performed a standardized vulnerability review of the generated code.**
  > Claude Code performed a standardized vulnerability review.
- **[6] Framework paths include worktree isolation and review, along with spec-driven development, agent-driven agile planning, context engineering, and legacy-spec recovery.**
  > Each attacks AI development through a different path: spec-driven development in full and lightweight variants, agent-driven agile planning, context engineering over the agent, worktree isolation and review, and recovery of operational specifications from legacy systems.
- **[7] The framework uses a deterministic Oversight Classification Model to route code-generation tasks into three oversight tiers based on regulatory impact, customer proximity, reversibility, and data sensitivity.**
  > GAIE introduces the Oversight Classification Model (OCM), a deterministic decision function that classifies code generation tasks by regulatory impact, customer proximity, reversibility, and data sensitivity to route them through one of three oversight tiers: human-in-the-loop (strategic functions), human-over-the-loop (customer-impacting), or automated-with-monitoring (internal).
- **[10] Autonomous coding agents are described as able to create branches, open pull requests, and perform code reviews while contributing to real-world projects.**
  > Autonomous coding agents, able to create branches, open pull requests, and perform code reviews, now actively contribute to real-world projects.
- **[13] Current AI support for code review is fragmented across isolated tasks such as reviewer recommendation, PR description generation, and comment suggestion rather than supporting the end-to-end PR review workflow.**
  > Current AI support in code review remains fragmented, with tools focusing on isolated tasks such as reviewer recommendation, PR description generation, or comment suggestion rather than the end-to-end PR review workflow.
- **[13] The proposed review framework spans five stages: PR Creation, PR Augmentation, Reviewer Selection, AI-Assisted Code Review, and PR Retrospective, retaining humans at key decision points.**
  > Our framework spans five stages: PR Creation, PR Augmentation, Reviewer Selection, AI-Assisted Code Review, and PR Retrospective, with humans retained at key decision points to preserve judgment, accountability, and team-level understanding.
- **[13] It proposes an AI-powered code review workflow that combines specialized agents with human-controlled quality gates.**
  > We then present a vision for an AI-powered code review workflow combining specialized agents with human-controlled quality gates.
- **[13] The vision uses staged AI-powered workflows to align the pace of code generation with shared understanding and accountable engineering.**
  > In this vision, staged, AI-powered workflows aim to align the pace of code generation with shared understanding and accountable engineering.
- **[15] Practitioners reported more reliable agent behavior but also greater planning and review costs.**
  > Practitioners agreed that specs should capture intent, but many also included implementation details, used SDD selectively and mainly for new features, and reported more reliable agent behavior alongside greater planning and review costs.
- **[17] Review capacity is explicitly named as a team-scale capacity that degrades under the AI productivity paradox.**
  > However, industry reports a productivity paradox: as individual productivity increases, team throughput, review capacity, and stability degrade because team-scale software engineering discipline is neglected.
- **[20] The paper proposes an Agentic SDLC Control Plane that allocates autonomy subject to cost, reliability, and human-attention budgets, alongside concepts including the Verification Tax and Production-Qualified Change.**
  > The synthesis proposes four engineering concepts: the Agentic SDLC Throughput Paradox, Production-Qualified Change (PQC), the Verification Tax, and an Agentic SDLC Control Plane that allocates autonomy subject to cost, reliability, and human-attention budgets.
- **[22] Among merged agentic PRs, 15.4% required explicit reviewer involvement through feedback or direct commits, and 5.5% showed no visible interaction trace.**
  > Among merged PRs, 15.4% required explicit reviewer involvement through feedback or direct commits, and 5.5% showed no visible interaction trace.
- **[23] After AI agent adoption, review time from submission to merge rose 56.1%, backlog wait rose 59.9%, active review time rose 58.5%, the share of code changes receiving comments rose 13.1%, and comments per code change rose 38.6%.**
  > after adoption of AI agents, the average time from the code’s review submission to its merge increases by 56.1%. This change represents both an increase in the time that code waits in a “backlog,” by 59.9%, and an increase in the time after code has begun active review, by 58.5%. The latter is consistent with a decline in review productivity, i.e., an increase in the review intensity. The share of code changes that receive at least one review comment increases by 13.1%, and the number of comments on each code change increases by 38.6%.
- **[23] AI code review tools were adopted by 79.1% of firms, but firms still largely kept humans in the loop and humans wrote the overwhelming majority of reviews and comments.**
  > This bottleneck is not eliminated by adoption of AI tools in the review process — 79.1% of firms have adopted AI code review tools, but still largely keep humans in the loop, with the overwhelming majority of reviews and comments being written by humans.
- **[24] The paper uses evidence on AI-augmented testing and verification to motivate separating synthesis from release authority.**
  > Industrial and research evidence on AI-augmented testing and verification is integrated to motivate separation between synthesis and release authority.
- **[26] The analysis says verification and accountable human judgment become more important in agentic software engineering.**
  > The analysis shows that GenAI lowers the cost of producing plausible code while increasing the importance of intent specification, context curation, architecture knowledge, verification, security, provenance, governance, and accountable human judgment.
- **[29] The measured review cost moves in the opposite direction from faster approval: review latency increases by 3.5x while inline comment volume decreases by 22% (p=0.0014), suggesting more time in queue but less active code inspection.**
  > However, review latency increases rather than decreases (+3.5x), while inline comment volume decreases (-22%, p=0.0014), suggesting reviewers spend more time in queue but less time actively inspecting code.
- **[30] The coordination log is a mineable artefact from which failure modes such as conflicting edits, lock starvation, redundant rediscovery and race-to-close are recoverable with provenance, several of them invisible in pull-request history.**
  > (iii) the log is a mineable artefact from which concrete failure modes - conflicting edits, lock starvation, redundant rediscovery, race-to-close - are automatically recoverable with provenance, several invisible in pull-request history.
- **[33] More than 61% of agent-authored pull requests in the AIDev dataset were approved and merged with minimal human intervention.**
  > Notably, more than 61\% of Agentic-PRs are approved and merged with minimal human intervention.
- **[35] The framework makes spec-code divergence a blocking merge condition via a drift gate.**
  > We present the Spec Growth Engine, a lightweight framework that addresses both failure modes through a machine-readable spec graph whose nodes carry explicit contract/design separation, a Spine context assembler that scopes agent context to an ownership path, a vertical-slice growth protocol that enforces hardest-first ordering, and a drift gate that makes spec-code divergence a blocking merge condition.
- **[38] Meta uses a human-on-the-loop model for JiTTests: engineers set criteria and review aggregate outcomes rather than supervising every output.**
  > Rather than a human-in-the-loop approach, where a human engineer reviews every output, we’ve reduced friction through a human-on-the-loop approach, where human engineers set criteria and review outcomes at an aggregate level rather than supervising every output.
- **[38] Catching JiTTests focuses test generation on diffs most likely to contain severe regressions.**
  > This helps ensure test generation is focused on diffs that are most likely to contain severe regressions.
- **[38] False positives are filtered with a rule-based approach plus an LLM-as-Judge ensemble that classifies weak catches as likely true or false positives.**
  > To filter false positives, we employed a traditional rule-based approach combined with an ensemble approach we call “LLM-as-Judge,” which aggregates judgements from several state-of-the-art (SOTA) LLMs, all tasked with classifying weak catches as likely true or false positives.
- **[38] The system uses the ranking from LLM-as-Judge and RubFake to decide whether to bring in a human engineer.**
  > Based on the ranking from LLM-as-Judge and RubFake, the system then decides whether to reach out to human engineers.
- **[41] The docs classify evidence requests, `/goal`, and `/code-review` as non-deterministic done-checks, while tests, typecheck, a Stop hook, and CI are deterministic.**
  > | When it’s done | A request for evidence, `/goal`, `/code-review` | Tests, typecheck, a `Stop` hook, CI |
- **[41] Human merge approval and branch protection are positioned as the deterministic final authority over Claude’s summary.**
  > | Who has the last word | Claude’s summary of what it did | Branch protection, a person who approves the merge |
- **[42] Human sign-off remains on every shipped outcome, but Meta tries to make that sign-off fast and evidence-backed with build results, test outcomes, and recorded verification sessions attached.**
  > Every shipped outcome still carries an engineer’s sign-off; our effort went into making that sign-off fast and well-evidenced, with build results, test outcomes, and recorded verification sessions attached to the change.
- **[43] Human PR review is optional, and almost all review effort has been shifted to agent-to-agent review.**
  > Humans may review pull requests, but aren’t required to. Over time, we’ve pushed almost all review effort towards being handled agent-to-agent.
- **[44] The report recommends reinforcing automated testing and fast code reviews, with continuous integration catching AI-introduced errors before production.**
  > Double-down on fast, high-quality feedback loops: organizations must reinforce safeguards like automated testing and fast code reviews. Continuous integration helps catch AI-introduced errors before they reach production.
- **[45] AI is seeing meaningful adoption in secondary review functions, including analyzing telemetry, reviewing pull requests, and hunting for security issues.**
  > Even secondary review functions—analyzing telemetry, reviewing pull requests, hunting for security issues—are seeing meaningful AI adoption.
- **[46] The governance model keeps a human in the loop for judgment rather than volume; automation flags divergence and a named human decides what is correct.**
  > keep a human in the loop for judgment, not volume (automation flags divergence, while a named human decides what is correct)
- **[47] A review agent pre-reviews each PR against docs/ADRs, flags anti-patterns and dependencies; after an early version posted 23 comments on one PR, it now posts only verified blockers with evidence, fix, and broken ADR rule; a revise label lets an agent push a fix, but auto-merge is off and engineers own code.**
  > A review agent pre-reviews each pull request against the docs and ADRs, flags anti-patterns and looks at what depends on the change.

Its first version left 23 comments on a single PR, starting with "Overall this PR looks great!" It now posts only verified blockers, each with evidence, a fix and the ADR rule it breaks. Engineers can add a revise label to have an agent read the review and push a fix to the same PR. Changes aren't yet auto-merged, and engineers own the code.
- **[48] The report says AI inference costs fell by a factor of 280 between November 2022 and October 2024, shifting the true financial burden to governance: managing the verification tax, adjusting workflows, and upskilling staff.**
  > They note that inference costs for AI models have fallen dramatically; dropping by a factor of 280 between November 2022 and October 2024 according to the Stanford Artificial Intelligence Index. This means that the true financial burden of adoption has shifted to governance: managing the verification tax, adjusting workflows, and upskilling staff.
- **[49] Duckbill reported median merge time of 26h for human-reviewed PRs versus 1h for PRs with no human review.**
  > *   Human-reviewed PRs median merge time: 26h

*   No human-review median merge time: 1h.
- **[49] A common pattern is for engineers to review the AI review rather than usually reading the code.**
  > In the above cases, engineers typically review the _review_ itself, and not usually the code.
- **[49] Low-risk changes can ship with only AI review once agents are satisfied, while high-risk changes require human review.**
  > *   **Low-risk change:** only AI, without human review. It can ship to production once AI agents are happy

*   **High-risk change:**mandatory human review
- **[50] Amazon is moving testing to the moment of coding so agents can check their own work before production, because faster code generation fails without upfront specs, tests, and edge cases.**
  > Teams can generate code faster than ever, but if they don’t define what success looks like up front — the specs, the tests, the edge cases — the agents don’t have as much chance of success. Amazon is now pushing testing to the moment of coding rather than handling it in stages, so agents can check their own work before anything reaches production.
- **[51] Pre-merge review load rose: review comments per PR +25%, average review comment length +22.7%, and PRs merged without any review +31.3%.**
  > +25%  average review comments per PR

+22.7%  average length of PR review comments

+31.3%  PRs merged without any review
- **[51] Agentic review covers 25% of PRs, while less than 1% of PRs are opened by AI agents.**
  > 25%  of PRs are reviewed by AI agents (up from zero in prior dataset)

<1%  of PRs are opened by AI agents
- **[52] Atlassian's internal AutoReview agent reviews code changes, flags potential issues, and suggests improvements before a human reviewer starts.**
  > The resulting AutoReview agent:

*   Reviews code changes and flags potential issues
*   Suggests improvements before a human reviewer even starts
- **[52] Atlassian reports over a 45% reduction in PR cycle time.**
  > Atlassian reports **over a 45% reduction in PR cycle time**.
- **[55] DX suggests the bottleneck may be moving from code production to system coordination, with engineering teams sometimes shipping faster than product management and verification processes can support.**
  > We may be observing a shift where the bottleneck moves from code production to system coordination. In some cases, engineering teams appear to be shipping faster than the surrounding product management and verification processes can support.
- **[55] Developers producing code faster often hit ceilings such as slower code reviews and architectural bottlenecks that neutralize individual gains.**
  > As developers produce code faster, they often hit ceilings, like slower code reviews and architectural bottlenecks, that neutralize individual gains.
- **[56] AI-DLC's operating pattern has AI create a plan, ask clarifying questions, and implement only after human validation, repeated for every SDLC activity.**
  > This pattern, where AI creates a plan, asks clarifying questions to seek context, and implements solutions only after receiving human validation, repeats rapidly for every SDLC activity, to provide a unified vision and approach for all development pathways.
- **[57] The source states that as coding agents become more powerful, humans are dangerously tempted to step out of the loop, and teams are beginning to iterate on coding-agent harnesses.**
  > As coding agents become more powerful, humans are dangerously tempted to step out of the loop. Teams are beginning to iterate on coding agent harnesses.
- **[60] In the standard minion flow, Stripe runs one full-CI iteration, auto-applies test fixes, gives one additional local fix attempt for non-autofix failures, then sends the branch to a human operator for manual scrutiny after the second push and CI run.**
  > we also include one iteration against the full CI suite into the standard minion blueprint. After a minion pushes a change, we run CI and auto-apply any autofixes for failing tests. If there are failures with no autofix, we send the failure back to a blueprint agent node and give the minion one more chance to fix the failing test locally. After the second push and CI run, we send the branch back to its human operator for manual scrutiny.
- **[60] Stripe caps CI retry loops at one or two rounds because CI consumes tokens, compute, and time and yields diminishing returns beyond that.**
  > Why have only one or two rounds of CI? There’s a balancing act between speed and completeness here; CI runs cost tokens, compute, and time, and we think there are diminishing marginal returns if an LLM is running against indefinitely many rounds of a full CI loop.
- **[62] A typical workflow has one engineer supervising three or four agents working in parallel, reviewing each agent's output as it finishes, giving feedback, and merging.**
  > One engineer might have three or four agents working in parallel: one implementing an API, one writing integration tests, one fixing a bug, one refactoring a legacy module. The engineer reviews each as it finishes, provides feedback, and merges.
- **[63] The source says long-lived teams acting as strict stewards of value flow ensure that only the smallest, highest-quality, and most secure changes are promoted.**
  > Long-lived teams acting as strict stewards of their value flow ensure that only the smallest, highest-quality, and most secure changes are promoted.
- **[64] The author states that lines of code are not the ideal artifact to review.**
  > Lines of code are not the ideal artifact to review
- **[64] The author argues humans are the weakest link for validation and will not beat machines at it.**
  > We are never going to beat the machine when it comes to _validation_ — we are literally the weakest link!
- **[65] Human base-case code review is slower and less effective than good harness review; harnesses miss things, but so do humans, and most areas are relatively safe while some higher-risk areas are exceptions.**
  > For example, the base case of code review from a human is slower and less effective than a good harness’ code review. Of course, the harness will miss things, but so will human reviewers, and most areas are relatively safe to make changes. Of course, there are some higher risk areas, where this doesn’t hold true.
- **[65] The first pass of code review is done by the same harness that implements the change, with the writing context cleared, so humans can focus on higher-value feedback.**
  > The first pass of code review is done by the same harness that implements the changes, cleared of the context used to write the change, allowing humans to focus on higher value feedback.
- **[67] Block's AI Champions enabled automated AI code review on PRs with customizable focus areas and headless AI assistance that can iterate on tasks, fix CI failures, and push changes.**
  > Enable automated AI code review on PRs with customizable focus areas. Set up headless AI assistance that can autonomously iterate on tasks, fix CI failures, and push changes.
- **[67] For some automated PRs, an agent reads the ticket, plans, creates a branch, writes code, opens a PR, watches CI, and fixes its own mistakes, with humans stepping in only at review time.**
  > The agent reads the ticket, makes a plan, creates the branch, writes the code, opens the pull request, watches CI fail, and fixes its own mistakes. Humans only step in at review time.
- **[68] Shopify treats PR review as an automated Aquifer profile that can run with no human in the loop.**
  > **Mode · Automation:** PR review. Durable session, woken by an external system, often no human in the loop.
- **[69] The author says he can only review and land one significant change at a time, and parallel agent tasks are acceptable only when they add little cognitive overhead to his primary work.**
  > I can only focus on reviewing and landing one significant change at a time, but I’m finding an increasing number of tasks that can still be fired off in parallel without adding too much cognitive overhead to my primary work.
- **[71] In augmented coding, the human continuously watches intermediate agent output, intervenes to stop unproductive development, and checks whether the agent did the requested next test.**
  > I watched the intermediate results of the genie more carefully, ready to intervene & stop unproductive development. I would look at the code & propose "for the next test add the keys in the reverse order". Then I'd look at the genie's work to see if it had done what I had asked.

## q4. How do team shape, roles and rituals change, and what do the organisation-level claims actually measure?

- **[3] External collaborators' local code, tests, and cleaned agent interaction traces are treated as knowledge sources rather than as the default merge candidate.**
  > In KPR, an external collaborator's local code, tests, and cleaned agent interaction trace are treated as knowledge sources rather than as the default merge candidate.
- **[6] The paper defines AI programming tools as development frameworks that include process, roles, artifacts, and verification.**
  > AI tools for programming are no longer just autocomplete or chat assistants: they organize themselves as development frameworks, with process, roles, artifacts and verification.
- **[7] Human oversight roles are differentiated by tier: strategic functions get human-in-the-loop, customer-impacting work gets human-over-the-loop, and internal work gets automated-with-monitoring.**
  > human-in-the-loop (strategic functions), human-over-the-loop (customer-impacting), or automated-with-monitoring (internal).
- **[7] The paper maps the framework to the Bank of Thailand’s 2025 AI risk-management policy and claims cross-jurisdiction applicability to MAS Singapore, NIST AI RMF, ISO/IEC 42001, and the EU AI Act.**
  > We map GAIE against the Bank of Thailand's 2025 AI risk-management policy and demonstrate cross-jurisdiction applicability to MAS (Singapore), NIST AI RMF, ISO/IEC 42001, and the EU AI Act.
- **[10] The paper frames agent contributions as an opportunity to investigate effects on code quality, team dynamics, and software maintainability.**
  > Their growing role offers a unique and timely opportunity to investigate AI-driven contributions and their effects on code quality, team dynamics, and software maintainability.
- **[13] The paper envisions reviewers shifting from manual inspectors to supervisory operators of agents.**
  > We propose a future vision for code review in which reviewers transition from manual inspectors into supervisory operators of agents.
- **[14] The evidence base is a single-expert first-person case study over 12 weeks, so it does not directly measure team shape, roles, or organization-level effects.**
  > We study this problem through a first-person case study: a 12-week development effort in which a single expert software engineer used frontier AI coding agents to build a document accessibility remediation system.
- **[15] The study's evidence base includes thematic analysis of Reddit discussions, interviews with 21 practitioners including eight tool makers, and 266 active and popular repositories from a corpus of 470,795 spec files across 73,030 public GitHub repositories.**
  > We study SDD in practice through a thematic analysis of Reddit discussions, interviews with 21 practitioners, including eight tool makers, and 266 active and popular repositories in SpecMine, a corpus of 470,795 spec files from 73,030 public GitHub repositories that we release.
- **[17] The paper proposes a methodological harness around the team and a typology of five human-agent interaction patterns through which the human role is redefined.**
  > Using a comparative characterization of the paradigm progression as conceptual framing, the article presents (i) a socio-technical model of SDD in which specifications act as the contract substrate between humans and agents; (ii) an operational characterization of the harness, distinguishing the technical harness around the agent from the methodological harness around the team, with worked examples; and (iii) a typology of five human--agent interaction patterns through which the human role is redefined.
- **[22] The authors conclude that PR outcomes alone do not capture agent performance and that evaluation must be interaction-aware, grounded in review behaviour.**
  > These results reject the assumption that PR outcomes alone capture agent performance and demonstrate the need for interaction-aware evaluation grounded in review behavior.
- **[23] Model estimates imply AI agents raised coding productivity by 73.7%, slightly lowered review productivity by −7.0%, reduced coding labor by −22.7%, and increased review labor by 43.4%.**
  > AI agents raise coding productivity by 73.7% and slightly lower review productivity ( −7.0%), and firms shift labor from coding to review: coding labor changes by −22.7% and review labor by 43.4%.
- **[23] Firm-level employment effects of AI adoption were not statistically significant in noisy estimates: assistants 3.0% with changes below −4.7% ruled out, and agents −2.6% with changes below −15.6% ruled out.**
  > We cannot attribute significant employment changes to AI, though our estimates are noisy. With AI assistants, we estimate an effect of 3.0%, ruling out changes below −4.7%. For AI agents, we estimate an effect of −2.6%, ruling out changes below −15.6%.
- **[24] The model extends to team role metamorphosis across engineer, QA, platform, and product functions, plus quantitative governance metrics and staged adoption.**
  > Beyond process description, we extend the model to team role metamorphosis (engineer, QA, platform, and product functions), quantitative governance (Ambiguity Tax, Spec Fidelity, SER, and TCI_agentic with repair multiplier phi), and pragmatic adoption via hybrid estimation and a staged migration blueprint.
- **[24] The paper positions AI-code as a fourth production paradigm and compares Human-Agile circa 2020 with Agentic-SDAD circa 2026 across artefacts, cadence, accountability, and security posture.**
  > We revisit the historical pendulum between Waterfall and Agile, introduce AI-code as a fourth production paradigm, and compare Human-Agile (circa 2020) with Agentic-SDAD (circa 2026) across artefacts, cadence, accountability, and security posture.
- **[26] The findings describe software engineering as shifting from isolated code authorship toward supervising, validating, and governing socio-technical systems of humans, agents, tools, and evidence gates.**
  > The findings indicate that software engineering is becoming less about isolated code authorship and more about supervising, validating, and governing socio-technical systems of humans, agents, tools, and evidence gates.
- **[26] The study bases its claims on reflexive thematic analysis and IPA-informed public-discourse/document analysis of peer-reviewed literature, benchmarks, talks, interviews, essays, announcements, and X-originated discourse.**
  > This study addresses that gap through a reflexive thematic analysis (RTA) dominant and interpretative phenomenological analysis (IPA) informed public-discourse and document analysis. The corpus combines peer-reviewed software engineering and AI literature, technical benchmarks, public talks and interviews, essays, product-facing technical announcements, and X-originated discourse from prominent AI and software engineering voices.
- **[27] The proposed governance model has three layers: regulatory requirements; organisational governance capabilities operationalised as a multi-criteria decision matrix with knock-out and weighted scoring; and productivity/sustainability outcomes measured by a named assessment protocol (PAG-LLM).**
  > The model is developed through Design Science Research (DSR) and is structured in three layers: (i) regulatory requirements, (ii) organizational governance capabilities, instantiated by a multi-criteria decision matrix with knock-out and weighted scoring criteria, and (iii) productivity and sustainability outcomes, operationalized by the LLM governance assessment protocol (PAG-LLM).
- **[27] A regulatory feedback loop routes operational results back to the normative layer so the model can be iteratively refined — a governance ritual rather than a delivery-flow mechanism.**
  > A regulatory feedback loop connects operational results back to the normative layer, enabling iterative refinement of the model.
- **[27] The paper positions existing regulation and framework obligations (EU AI Act, NIST AI RMF, GDPR, LGPD, ISO/IEC 42001) as hard to translate into operational technical decision criteria, which is the gap its model addresses.**
  > Regulations and frameworks such as the EU AI Act, the NIST AI Risk Management Framework (RMF), the General Data Protection Regulation (GDPR), the Lei Geral de Proteção de Dados (LGPD), and ISO/IEC 42001 establish obligations that are often difficult to translate into operational criteria for technical decision-making.
- **[30] grite is an open-source coordination substrate requiring no central server, storing append-only signed event records inside git itself so the coordination process is captured directly.**
  > We study this process through grite, our open-source coordination substrate that needs no central server and stores its records inside git itself, so its append-only, signed event log captures the coordination process directly.
- **[34] This is a conceptual/position paper that argues GenAI adoption affects human as well as technical aspects, specifically how software professionals perceive their work identity and the identity work they perform to form, adapt and reject those identities.**
  > The adoption of Generative AI (GenAI) suggests major changes for software engineering, including technical aspects but also human aspects of the professionals involved. One of these aspects is how individuals perceive themselves regarding their work, i.e., their work identity, and the processes they perform to form, adapt and reject these identities, i.e., identity work.
- **[34] Existing studies give evidence of GenAI-triggered identity work among software professionals, but they do not differentiate between roles such as developers and testers.**
  > Existent studies provide evidence of such identity work of software professionals triggered by the adoption of GenAI, however they do not consider differences among diverse roles, such as developers and testers.
- **[34] The paper's central position is that role should be treated as a factor defining the identity work of software professionals under GenAI adoption.**
  > In this paper, we argue the need for considering the role as a factor defining the identity work of software professionals.
- **[34] Rather than reporting measurements, the paper proposes a research agenda to understand how role influences identity work and to propose new artifacts supporting GenAI adoption; it discusses potential implications for practice of results yet to be obtained.**
  > Then, we propose a research agenda to better understand how the role influences identity work of software professionals triggered by the adoption of GenAI, and, based on that, to propose new artifacts to support this adoption. We also discuss the potential implications for practice of the results to be obtained.
- **[37] Gartner predicts that by 2029, 60% of organizations will adopt smaller software engineering teams at scale, up from 15% in 2026.**
  > By 2029, 60% of organizations will adopt smaller software engineering teams at scale, up from 15% in 2026, according to Gartner, Inc.
- **[37] Gartner states that AI is redefining roles and teams while increasing demand for software engineers, and that resources required for growing software demand will outpace AI efficiency gains.**
  > "AI is reshaping software engineering. It is redefining roles, reinventing teams, and fueling the demand for more software engineers, not fewer," said Aliyah Camacho, Principal Analyst at Gartner. "The resources required to meet the growing demand for software and complex AI-enabled applications will outpace the efficiency gains from AI."
- **[37] Gartner says tiny teams are not a cost-optimization tactic but a restructuring to use both human and AI capabilities and strengths.**
  > "Tiny teams are not a cost optimization tactic," said Camacho. "This is a restructuring of teams to best take advantage of both human and AI capabilities and strengths."
- **[37] Gartner reports that today's tiny teams typically have 4-5 members, with some requiring as few as 2-3 members, which will become more common as skills and AI capabilities mature.**
  > "Today's tiny teams typically have 4-5 members, but some require as few as 2-3, which will become more common as employee skills and AI capabilities mature," said Camacho.
- **[37] Gartner says tiny teams are supported by robust platform engineering teams providing standardized, automated workflows and self-service AI tools so tiny teams can focus on high-value work.**
  > As tiny teams are supported by robust platform engineering teams, they can focus on high-value work by providing standardized, automated workflows and self-service AI tools and capabilities.
- **[37] Gartner says tiny teams require versatile engineers including a product manager, a UX/AX designer, and at least one AI-native software engineer, and that traditional role boundaries collapse as members oversee AI agents and broader responsibilities.**
  > Tiny teams require versatile and skilled engineers such as a product manager, a user experience (UX)/agent experience (AX) designer, and at least one AI-native software engineer. However, software engineering leaders should not stop hiring and developing junior-level talent.
In a tiny team, traditional software engineering role boundaries collapse, as each team member manages a variety of responsibilities, from understanding business goals to product design and overseeing AI agents.
- **[37] Gartner warns that slowing junior-level hiring can inhibit knowledge transfer, restrict the internal talent pipeline, and limit recruitment to more expensive and competitive senior roles.**
  > "Slowing junior-level hiring could lead to significant pitfalls, including inhibiting knowledge transfer, restricting the internal talent pipeline, and limiting recruitment to more expensive and competitive senior roles," said Camacho.
- **[37] Gartner predicts that by 2028, organizations relying on AI to cut junior roles will hollow out their own software engineering talent pipeline.**
  > Gartner predicts that by 2028, organizations that rely on AI to cut junior roles will hollow out their own software engineering talent pipeline.
- **[38] Meta describes the approach as generalizable: engineers define success criteria early, AI executes testing, engineers monitor aggregate outcomes, and intervention happens at the policy level rather than per item.**
  > The approach is generalizable: Engineers define success criteria early, let AI execute the testing, monitor the outcomes at an aggregate level, and intervene at the policy level rather than per item.
- **[39] Booking.com found that training developers to give coding assistants more explicit instructions and context led to up to 30% increases in merge requests and higher job satisfaction.**
  > When developers learned how to give their coding assistant more explicit instructions 
and more effective context, they 
found up to 30% increases in merge requests and higher job satisfaction.
- **[39] 90% of organizations have adopted platform engineering, and DORA says a high-quality internal platform is the essential foundation for AI success.**
  > 90% of organizations have 
adopted platform engineering, making a high-quality internal platform the essential 
foundation for AI success.
- **[40] Under spec-driven development, product managers become owners of the specification rather than only being responsible for planning and prioritization.**
  > “In spec-driven development, PMs become the owners of the spec; they’re no longer just responsible for planning and prioritization. Everything starts with the spec, so they become the starting point for the entire system. If the specs are right, then everything falls into place.”
- **[40] Microsoft Digital engineers shifted from producing every line of code toward refining requirements, identifying edge cases, evaluating plans, and validating AI-generated outputs against intent.**
  > Our Microsoft Digital engineers now spend more time refining requirements, identifying edge cases, evaluating plans, and validating AI-generated outputs. Their role has shifted away from producing every line of code to making sure that code implementation accurately reflects intent.
- **[41] The page directs whole-team setup to a separate organization page.**
  > Setup for a whole team is on a separate page: [Set up Claude Code for your organization](https://code.claude.com/docs/en/admin-setup).
- **[42] In the human-on-the-loop model, the agent runs the iteration while the engineer sets the goal, watches the run, intervenes when needed, and approves the result; the engineer’s job moves from executing steps to owning the outcome and quality bar.**
  > With **human-on-the-loop**, the agent runs the iteration itself — plan, implement, build, test, correct, repeat — while the engineer sets the goal, watches the run, steps in when it drifts, and approves the result. The person’s job moves from executing the steps to owning the outcome and holding the quality bar.
- **[43] Humans remain in the loop at a different abstraction layer: prioritizing work, translating user feedback into acceptance criteria, and validating outcomes.**
  > Humans always remain in the loop, but work at a different layer of abstraction than we used to. We prioritize work, translate user feedback into acceptance criteria, and validate outcomes.
- **[44] Organizations that address job displacement fears see 125% more team AI adoption than those that ignore them.**
  > Address job displacement fears transparently: Organizations that take steps to alleviate these concerns see 125% more team AI adoption than those that ignore them.
- **[44] Dedicated work-hours learning time leads to a 131% increase in team AI adoption.**
  > Provide dedicated learning time: Giving developers dedicated time during work hours to explore and experiment with AI leads to a 131% increase in team adoption.
- **[44] Clear AI acceptable-use policies are associated with a 451% increase in AI adoption compared with organizations without such policies.**
  > Establish clear acceptable-use policies: Organizations with clear AI acceptable-use policies show a 451% increase in AI adoption compared to those without.
- **[44] DORA describes a valuable-work paradox in which AI adoption reduces time spent on valuable work while time on toilsome, repetitive tasks remains unchanged.**
  > The "valuable work" paradox: AI adoption leads to developers spending less time on valuable work, while time spent on toilsome, repetitive tasks remains unchanged.
- **[47] For cross-service features, a product engineer touches payment API, billing, gateway, and every client, forcing the team to define who owns context and how it follows the work.**
  > A product engineer building one feature touches the payment API, billing, the gateway and every client, so the team had to decide who owns the context and how it follows the work.
- **[48] The report strongly discourages headcount reduction, arguing retaining and training existing staff is more cost-effective and preserves institutional knowledge.**
  > The report strongly discourages headcount reduction as a strategy, arguing that retaining and training existing staff is more cost-effective and preserves institutional knowledge.
- **[49] Weaviate's CTO describes leaving about 90% to agents, with humans in the loop for critical scope decisions and exit criteria.**
  > So basically, 90% is left to agents, with humans in the loop for critical scope decisions and exit criteria.
- **[50] Sivasubramanian says projects that once required 30 to 40 people can now be done by teams of six to eight.**
  > It matches the new reality of the AI era: projects that once required 30 to 40 people, he said, can now be done by teams of six to eight.
- **[51] The report characterizes AI as having moved from assistant to author at scale, with humans moved into review and oversight rather than creation.**
  > In the organizations we studied, AI has moved from a tool that assists engineers to one that authors code at scale, with humans increasingly in a review and oversight role rather than a creation role.
- **[52] Atlassian describes a 20-person, multi-country project run with no real-time meetings using Loom videos and Confluence pages, with discussions and decisions recorded as they happened.**
  > Boyagi described running a 20-person, multi-country project with **no real-time meetings** by combining Loom videos for async communication with Confluence pages for shared context. Discussions and decisions were recorded as they happened.
- **[56] AI-DLC replaces sprints with bolts measured in hours or days, and epics with Units of Work.**
  > Traditional ‘sprints’ are replaced by ‘bolts’ – shorter, more intense work cycles measured in hours or days rather than weeks; Epics are replaced by Units of Work.
- **[56] Inception uses Mob Elaboration, where the entire team validates AI's questions and proposals.**
  > In the **Inception phase**, AI transforms business intent into detailed requirements, stories and units through “Mob Elaboration” – where the entire team actively validates AI’s questions and proposals.
- **[58] Uplevel's Sustained Always On metric, measuring working time outside standard hours as a burnout indicator, fell 17% for Copilot users and 28% for non-users, so Copilot was not the most effective way to alleviate burnout.**
  > **Doesn’t mitigate risk of burnout** — Uplevel’s [“Sustained Always On” metric](https://uplevelteam.com/blog/why-dora-metrics-are-only-part-of-the-equation) (measuring working time outside of standard hours: a leading indicator of burnout) decreased for both control and test groups during the course of the study. But it decreased by 17% for those with Copilot access and, notably, 28% for those without — showing Copilot isn’t the most effective way to alleviate burnout.
- **[60] Minions run fully unattended, so Stripe’s harness omits interruptibility and human-triggered commands to initiate or steer the run.**
  > Minions, however, are fully unattended, so our agent harness can’t use human-facing features such as interruptibility or human-triggered commands to initiate or steer the agent run.
- **[62] When code becomes cheap, engineering work shifts upward to scoping problems, designing solutions, reviewing output, and catching edge cases, while implementation becomes the easy part.**
  > When code becomes cheap, the engineer's job changes. The work that matters shifts upward: scoping problems, designing solutions, reviewing output, catching edge cases. The implementation becomes the easy part.
- **[63] The source argues AI forces teams to move past construction boundaries and establish stewardship boundaries around value flow and human accountability.**
  > AI forces us to move past "construction boundaries" and instead **establish clear boundaries around the stewardship of value flow and human accountability**.
- **[64] Honeycomb issued an AI mandate last August.**
  > We issued our AI mandate last August.
- **[65] Quick, good, durable decision-making is a prerequisite to benefit from AI, and the author says the average CTO role has become substantially more technical and less bureaucratic than a year ago.**
  > Your team and company can only benefit from this increased pace of execution if you can make durable decisions quickly, and those decisions are good. This is the primary reason, in my opinion, why the average CTO role has necessarily become substantially more technical and less bureaucratic than a year ago.
- **[67] About 95% of Block engineers regularly use AI; the largest group runs a single agent mostly outside an IDE, and the second-largest runs 3-5 agents in parallel.**
  > About 95% of our engineers are regularly using AI to assist with their development efforts. The largest population is at Stage 5, running a single agent mostly outside of an IDE. The second largest population is at Stage 6 and is running 3-5 agent instances in parallel.
- **[68] River is constrained to public Slack channels; direct messages are disallowed, and every conversation becomes a public transcript open by default to other employees.**
  > One constraint: River only works in the open. No direct messages. Every conversation with River becomes a public Slack transcript, open by default to other Shopify employees.
- **[69] Jesse Vincent’s September 2025 workflow uses an architect agent to iterate on a plan, which is then reviewed and implemented by fresh Claude Code instances.**
  > Jesse Vincent wrote [How I’m using coding agents in September, 2025](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/) which describes his workflow for parallel agents in detail, including having an architect agent iterate on a plan which is then reviewed and implemented by fresh instances of Claude Code.
- **[70] The team introduced new rituals: digital quiet hours to keep approval requests out of evenings and weekends, and weekly agent insight sessions to share patterns identified by AI agents.**
  > We set digital quiet hours so approval requests don't bleed into evenings and weekends. And we hold weekly agent insight sessions where developers share patterns their AI counterparts identified, turning isolated discoveries into shared organizational knowledge.
- **[72] Zapier reports that 97% of its team uses AI in daily work.**
  > Nearly everyone—97% of our team—uses AI in their daily work.
- **[72] Zapier evaluates AI fluency for 100% of job candidates across every department.**
  > We evaluate the AI fluency of 100% of job candidates across every department.
- **[72] Zapier created a Chief People & AI Transformation Officer role to guide its AI transformation.**
  > That's why we've created a new role to guide that transformation at Zapier: Chief People & AI Transformation Officer.
- **[72] Zapier frames its AI transformation approach around four pillars: leadership, culture, tools, and governance.**
  > Zapier's approach to AI transformation centers on four key pillars: leadership, culture, tools, and governance.
- **[72] Zapier's CEO states that AI adoption alone is not transformation; transformation occurs when AI reshapes how teams think, collaborate, and create value.**
  > But as our CEO, Wade Foster puts it: "AI adoption alone isn't transformation." Real transformation happens when AI reshapes how teams think, collaborate, and create value.
- **[74] The toolkit includes sample role bundles named product-manager, business-analyst, security-researcher, and developer.**
  > four sample role bundles (product-manager, business-analyst, security-researcher, developer)

## q5. What is the counter-evidence on quality, security and verification, and where do the large productivity numbers come from?

- **[1] Among closed CRA-only PRs, 60.2% fell in the 0-30% signal range, and 12 of 13 CRAs had average signal ratios below 60%, indicating substantial noise in automated review feedback.**
  > Our signal-to-noise analysis reveals that 60.2% of closed CRA-only PRs fall into the 0-30% signal range, and 12 of 13 CRAs exhibit average signal ratios below 60%, indicating substantial noise in automated review feedback.
- **[1] The paper suggests CRAs without human oversight often produce low-signal feedback associated with higher abandonment.**
  > These findings suggest that CRAs without human oversight often generate low-signal feedback associated with higher abandonment.
- **[1] Industry reports claim CRAs can manage 80% of PRs in open source repositories without human involvement.**
  > Industry reports claim that CRAs can manage 80% of PRs in open source repositories without human involvement.
- **[2] The study ruled out differential issue dropping and found that developers submitted similar quality PRs with and without AI.**
  > We rule out many experimental artifacts—developers used frontier models, complied with their treatment assignment, didn’t differentially drop issues (e.g. dropping hard AI-disallowed issues, reducing the average AI-disallowed difficulty), and submitted similar quality PRs with and without AI.
- **[2] The authors argue benchmarks may overestimate model capabilities by measuring only well-scoped, algorithmically scorable tasks, and that anecdotal speed-up estimates can be very inaccurate.**
  > On the other hand, benchmarks may overestimate model capabilities by only measuring performance on well-scoped, algorithmically scorable tasks. And we now have strong evidence that anecdotal reports/estimates of speed-up can be very inaccurate.
- **[2] The authors explicitly limit generalizability, saying they do not claim their developers or repositories represent a majority or plurality of software development work.**
  > We do not claim that our developers or repositories represent a majority or plurality of software development work
- **[2] The authors note that their tool setup may not use optimal prompting or scaffolding, and that domain- or repository-specific training could yield positive speedup.**
  > Cursor does not sample many tokens from LLMs, it may not use optimal prompting/scaffolding, and domain/repository-specific training/finetuning/few-shot learning could yield positive speedup
- **[2] The authors suggest AI capabilities may be comparatively lower in settings with very high quality standards or many implicit documentation, testing, and linting requirements.**
  > Our results also suggest that AI capabilities may be comparatively lower in settings with very high quality standards, or with many implicit requirements (e.g. relating to documentation, testing coverage, or linting/formatting) that take humans substantial time to learn.
- **[3] The pilot stress-tests KPR packages under description ablation, diff ablation, and synthetic poisoned-patch conditions.**
  > The pilot shows that KPR packages can be instantiated from real PR material and stress-tested under description ablation, diff ablation, and synthetic poisoned-patch conditions.
- **[4] RADAR-reviewed diffs had a revert rate one-third that of non-RADAR diffs and a Production Incident rate one-fiftieth that of non-RADAR diffs.**
  > The revert rate for RADAR-reviewed diffs is 1/3 that of non-RADAR diffs, and the Production Incident rate is 1/50 that of non-RADAR diffs.
- **[5] In a study of AI-generated automation scripts, every script contained exploitable vulnerabilities.**
  > Every script contained exploitable vulnerabilities.
- **[5] Nine of 17 identified vulnerability classes appeared across all three models, and 14 of 17 appeared in at least two models.**
  > Nine of the 17 identified vulnerability classes appeared in code from all three models, while 14 of the 17 vulnerability classes appeared in at least two models.
- **[5] Weighted CVSS scores across the three AI platforms differed by less than 10%.**
  > The weighted CVSS scores across platforms differed by less than 10%.
- **[5] The study concludes the security risk is tied to task category rather than to a particular AI model.**
  > The risk is not tied to any particular model but rather to the task category.
- **[5] The paper argues organizations should ask whether LLM-generated automation code should be deployed without review, not which tool to trust.**
  > Organizations should therefore ask not which tool to trust, but instead whether LLM-generated automation code should be deployed without review.
- **[5] Identified vulnerabilities were scored with CVSS v3.1 and mapped to OWASP Top 10:2021 and MITRE ATT&CK.**
  > Each identified vulnerability was scored using CVSS v3.1 and mapped to the OWASP Top 10:2021 and the MITRE ATT&CK frameworks.
- **[6] No framework strongly covers all six dimensions; the paper reports a structural trade-off between process depth and portability across agents.**
  > And no framework strongly covers all six dimensions, exposing a structural trade-off between process depth and portability across agents.
- **[6] Recurring risks found include specification-code drift, excessive trust in generated artifacts, fragile community extensions, platform dependence, and lack of complete-process benchmarks.**
  > We also found recurring risks: drift between specification and code, excessive trust in generated artifacts, fragility of community extensions, platform dependence and a lack of benchmarks for the complete process.
- **[6] The research agenda calls for empirical evaluation using intermediate-quality metrics, context governance, installation security, and reproducibility.**
  > We close with a research agenda for empirical evaluation, focused on intermediate-quality metrics, context governance, installation security and reproducibility.
- **[7] The source frames a productivity–reliability tension and says existing frameworks offer no mechanism for calibrating human oversight intensity to regulatory impact.**
  > Existing frameworks address AI-assisted development maturity or the productivity-reliability tension but offer no mechanism for calibrating human oversight intensity to regulatory impact.
- **[8] Bayesian analysis found that any speed or quality improvements from AI use were at most small and highly uncertain.**
  > Bayesian analysis suggests that any speed or quality improvements from AI use were at most small and highly uncertain.
- **[8] The study did not detect systematic maintainability advantages or disadvantages when other developers evolved code co-developed with AI assistants.**
  > Overall, we did not detect systematic maintainability advantages or disadvantages when other developers evolved code co-developed with AI assistants.
- **[8] The two-phase controlled experiment involved 151 participants, 95% of whom were professional developers.**
  > We conducted a two-phase controlled experiment involving 151 participants, 95% of whom were professional developers.
- **[8] The authors say future work should examine risks such as code bloat from excessive code generation and cognitive debt from offloading mental effort to assistants.**
  > Future work should examine risks such as code bloat from excessive code generation and cognitive debt as developers offload more mental effort to assistants.
- **[9] The source states that the impact of AI assistants on code quality, especially maintainability, needs further investigation.**
  > However, their impact on code quality, particularly in terms of maintainability, requires further investigation.
- **[9] The planned study aims to examine how AI assistants influence software maintainability, including developers' ability to evolve code.**
  > This study aims to examine the influence of AI assistants on software maintainability, specifically assessing how these tools affect the ability of developers to evolve code.
- **[9] Phase 2 is a randomized controlled trial in which different developers evolve random Phase 1 projects without AI assistants.**
  > Phase 2, a randomized controlled trial, will involve a different set of developers evolving random Phase 1 projects - working without AI assistants.
- **[10] The paper reports increasing agent activity in open-source projects, but agent contributions are associated with more churn over time than human-authored code.**
  > Ultimately, our findings indicate an increasing agent activity in open-source projects, although their contributions are associated with more churn over time compared to human-authored code.
- **[11] The paper argues that compile rate is a scientifically unreliable metric for single-function vulnerability repair, based on five controlled experiments over 203 vulnerable functions, three open-source code LLMs ranging from 350M to 6.7B parameters, and three prompting strategies.**
  > We argue that compile rate is a scientifically unreliable metric for single-function vulnerability repair, and we support this with five controlled experiments over 203 vulnerable functions from Big-Vul, three open-source code LLMs (350M to 6.7B parameters), and three prompting strategies.
- **[11] About 64% of compile failures are not attributable to the model and that share is nearly invariant across models, with compile rate dominated by evaluation-harness and dataset artifacts rather than model quality.**
  > Compile rate (i) barely responds to an intervention that substantially improves the generated code; (ii) is dominated by evaluation-harness and dataset artifacts rather than model quality, with about 64% of compile failures not attributable to the model, a share that is nearly invariant across models;
- **[11] Compile rate shifts by 1.8 to 2.7 times on identical patches under a single compiler-standard flag, with zero regressions.**
  > (iii) shifts by 1.8 to 2.7 times on identical patches under a single compiler-standard flag, with zero regressions;
- **[11] Compile rate ranks the three models in the opposite order to reference-similarity metrics.**
  > (iv) ranks the three models in the opposite order to reference-similarity metrics;
- **[11] When used as an optimization target, compile rate rewards non-repairs: a compiler-feedback loop raises compile rate while similarity to the human fix falls, and manual inspection finds deletion- and placeholder-style non-repairs among newly compiling outputs.**
  > (v) rewards non-repairs when used as an optimization target, since a compiler-feedback loop raises compile rate while similarity to the human fix falls, with manual inspection finding deletion- and placeholder-style non-repairs among the newly compiling outputs.
- **[11] The whole-function CodeBLEU fallback also fails because an unchanged copy of the vulnerable input outscores every model.**
  > The natural fallback, whole-function CodeBLEU, also fails: an unchanged copy of the vulnerable input outscores every model.
- **[11] diff_F1, a change-aware screen that scores only the edited region, gives exactly zero credit to a no-op and near-zero credit to some deletion-based gaming patches while still crediting genuine partial edits, but it is not a repair-quality metric.**
  > We also examine diff_F1, a change-aware screen that scores only the edited region. It gives exactly zero credit to a no-op and near-zero credit to some, though not all, of the deletion-based gaming patches we observed, while still crediting genuine partial edits, so it may serve as a cheap screen before deeper, execution-based analysis. It is not a repair-quality metric, and we report where it falls short.
- **[12] The benchmark evaluation agrees with expert consensus 95.2% of the time and has lower case-level variation across judging records than across repeated executions.**
  > Evaluation achieves 95.2\% agreement with expert consensus, with lower case-level variation across judging records than repeated executions.
- **[14] The governance-conversion model says controls are discovered from failures visible only during agentic work, contrasting with governance models that derive controls from known obligations.**
  > In contrast to existing governance models that derive controls from known obligations, governance conversion explains how controls are discovered from failures that become visible only during agentic work.
- **[15] Evidence on the use of spec-driven development comes largely from tool vendors.**
  > Spec-driven development (SDD) addresses this by having developers and agents write specifications that guide implementation, yet evidence on its use comes largely from tool vendors.
- **[17] The paper is a conceptual analysis based predominantly on gray literature because peer-reviewed evidence and a shared academic-industrial vocabulary are not yet established.**
  > We conducted a conceptual analysis drawing predominantly on gray literature, including ASE vision and roadmap papers, practitioner reports, talks, and tooling, because peer-reviewed evidence and a shared academic-industrial vocabulary are not yet established.
- **[18] Across all models tested, 55.8% of generated artifacts contained at least one COBALT-identified vulnerability, with 1,055 formally proven via Z3 satisfiability witnesses.**
  > Across all models, 55.8% of artifacts contain at least one COBALT-identified vulnerability; of these, 1,055 are formally proven via Z3 satisfiability witnesses.
- **[18] GPT-4o had the highest vulnerability rate at 62.4% (grade F), Gemini 2.5 Flash performed best at 48.4% (grade D), and no model achieved a grade better than D.**
  > GPT-4o leads at 62.4% (grade F); Gemini 2.5 Flash performs best at 48.4% (grade D). No model achieves a grade better than D.
- **[18] Explicit security instructions reduced the mean vulnerability rate by only 4 percentage points.**
  > explicit security instructions reduce the mean rate by only 4 points;
- **[18] Six industry tools combined missed 97.8% of findings proven by Z3.**
  > six industry tools combined miss 97.8% of Z3-proven findings;
- **[18] Models identified their own vulnerable outputs 78.7% of the time in review mode, but generated them at 55.8% by default.**
  > models identify their own vulnerable outputs 78.7% of the time in review mode yet generate them at 55.8% by default.
- **[18] Six of seven representative findings were confirmed with runtime crashes under GCC AddressSanitizer.**
  > Six of seven representative findings are confirmed with runtime crashes under GCC AddressSanitizer.
- **[19] In an empirical study of agentic Python refactoring pull requests, agentic commits improved a quality attribute in 22.5% of studied changes on average, with usability improving most frequently at 36.5%.**
  > Our results show that, on average, agentic commits improve a quality attribute in 22.5% of the studied changes, with usability improving most frequently (36.5%).
- **[19] 24.17% of modified files introduced new Pylint issues, predominantly convention-level violations such as long lines, while 4.7% introduced new Bandit findings.**
  > At the same time, 24.17% of modified files introduce new Pylint issues predominantly convention level violations such as long lines-while 4.7% introduce new Bandit findings.
- **[19] Despite mixed quality and security outcomes, developer acceptance was high: 73.5% of analyzed agentic refactoring PRs were merged, including cases introducing new lint or security findings.**
  > Despite these mixed outcomes, developer acceptance is high: 73.5% of the analyzed PRs are merged, including cases that introduce new lint or security findings, often alongside the removal of existing issues.
- **[19] The authors conclude that agentic refactoring shows both promise and current limitations, and they call for stronger tool-in-the-loop quality and security gating for AI-driven workflows.**
  > Overall, these findings highlight both the promise and current limitations of agentic refactoring, and motivate stronger tool-in-the-loop quality and security gating for AI-driven development workflows.
- **[19] The study measures code quality and security issues before and after each change using PyQu plus Pylint and Bandit static analysis.**
  > We analyze agentic refactoring PRs using PyQu, an ML-based quality assessment tool for Python, to quantify changes across five quality attributes, and we complement PyQu with domain-independent static analysis (Pylint and Bandit) to measure code quality and security issues before and after each change.
- **[19] The empirical study examines Python refactoring pull requests from the AIDev dataset.**
  > To address this gap, we conduct an empirical study of Python refactoring pull requests (PRs) from the AIDev dataset.
- **[20] The paper is a synthesis of peer-reviewed software-engineering research, university studies, benchmark audits, production reports, developer telemetry, and cost-management evidence mainly from 2024 through September 2026.**
  > This paper synthesizes peer-reviewed software-engineering research, university studies, benchmark audits, production reports from major technology companies, developer telemetry, and cost-management evidence released primarily from 2024 through September 2026.
- **[20] The paper claims no new model experiment and attributes numerical findings to the original studies.**
  > No new model experiment is claimed; numerical findings remain attributed to their original studies.
- **[21] The paper frames package hallucinations in LLM-generated code as a new software supply-chain threat and a novel form of package confusion attack.**
  > The reliance of popular programming languages such as Python and JavaScript on centralized package repositories and open-source software, combined with the emergence of code-generating Large Language Models (LLMs), has created a new type of threat to the software supply chain: package hallucinations. These hallucinations, which arise from fact-conflicting errors when generating code using LLMs, represent a novel form of package confusion attack that poses a critical threat to the integrity of the software supply chain.
- **[21] The study evaluated package hallucinations using 16 popular LLMs, two prompt datasets, two programming languages, and 576,000 generated code samples.**
  > Using 16 popular LLMs for code generation and two unique prompt datasets, we generate 576,000 code samples in two programming languages that we analyze for package hallucinations.
- **[21] The average percentage of hallucinated packages was at least 5.2% for commercial models and 21.7% for open-source models.**
  > Our findings reveal that that the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat.
- **[21] The analysis found 205,474 unique examples of hallucinated package names.**
  > Our findings reveal that that the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat.
- **[21] The authors implemented hallucination mitigation strategies and reported that these significantly reduced package hallucinations while maintaining code quality.**
  > To overcome this problem, we implement several hallucination mitigation strategies and show that they are able to significantly reduce the number of package hallucinations while maintaining code quality.
- **[21] The authors conclude that package hallucinations are a persistent and systemic phenomenon when using state-of-the-art LLMs for code generation.**
  > Our experiments and findings highlight package hallucinations as a persistent and systemic phenomenon while using state-of-the-art LLMs for code generation, and a significant challenge which deserves the research community's urgent attention.
- **[22] Rejection outcomes overstate agent error: only 35.7% of rejected PRs were clear agentic failures, 31.2% were driven by workflow constraints, and 33.1% lacked observable decision rationale.**
  > We found that rejection outcomes substantially overstate agent error: only 35.7% of rejected PRs reflected clear agentic failures, while 31.2% were driven by workflow constraints and 33.1% lacked observable decision rationale.
- **[23] Qualitative interviews report that outages caused by AI-generated commits led to new rules requiring senior engineer approval for AI-generated code, which created more review bottlenecks.**
  > After some outages that were caused by AI-generated commits, there were also new rules requiring senior engineer approval for AI-generated code, which created even more review bottlenecks.
- **[25] The study empirically analyzes real-life ChatGPT-generated code for both correctness and security, and also examines users' intentions when requesting code.**
  > In this study, we perform a large-scale empirical analysis of real-life code generated by ChatGPT. We evaluate code generated by ChatGPT both with respect to correctness and security and delve into the intentions of users who request code from the model.
- **[25] The study supports earlier synthetic-query research and reports evidence that LLM-generated code is often insufficient in security.**
  > Our study supports earlier research that employed synthetic queries and produced proof that LLM-generated code is frequently insufficient in terms of security.
- **[25] The authors observe that users do not ask many questions about the security characteristics of code they request from LLMs.**
  > Additionally, we observe that users don't ask many questions about the security characteristics of the code they ask LLMs to provide.
- **[25] The study includes an experiment testing common prompt engineering strategies using real-life prompts.**
  > We further performed an experiment to evaluate the effectiveness of common prompt engineering strategies using real-life prompts.
- **[25] The paper argues that most prior studies use code generated specifically for the study, which raises questions about experimental realism.**
  > However, most of these studies rely on code that is generated specifically for the study, which raises questions about the realism of such experiments.
- **[25] The paper states that several recent studies warn that AI-generated code may be particularly vulnerable to cyberattacks.**
  > Several recent studies have raised alarm bells, indicating that such AI-generated code may be particularly vulnerable to cyberattacks.
- **[26] The source warns that speed-focused adoption can accumulate hidden technical debt and accountability gaps, while bounded autonomy can preserve quality, security, maintainability, and trust.**
  > This matters because speed-focused adoption can accumulate hidden technical debt and accountability gaps, whereas bounded autonomy can preserve quality, security, maintainability, and trust.
- **[27] The paper states that integrating LLMs into the SDLC can improve developer productivity but simultaneously introduces security, privacy and compliance risks at the point of model selection.**
  > Integrating Large Language Models (LLMs) into the Software Development Life Cycle (SDLC) can improve developer productivity, but it also introduces security, privacy, and compliance risks during model selection.
- **[27] A pilot evaluation using 20 adversarial scenarios drawn from CWE and the OWASP Top 10 found differing risk profiles between commercial cloud-based LLMs and locally hosted open-source LLMs.**
  > A pilot evaluation with 20 adversarial scenarios based on Common Weakness Enumeration (CWE) and the OWASP Top 10 suggests distinct risk profiles between commercial cloud-based LLMs and local open-source LLMs.
- **[27] The authors report preliminary evidence that knock-out (disqualification) criteria can block technically competitive models that carry unacceptable compliance risk.**
  > The results provide preliminary evidence that regulatory disqualification logic, particularly K.O. criteria, can prevent the selection of technically competitive models that nonetheless pose unacceptable compliance risks, demonstrating the feasibility of governance-oriented LLM selection in software engineering projects.
- **[28] Prior work on agent productivity has largely relied on benchmarks and controlled tasks rather than large-scale post-merge analyses.**
  > Although such PRs promise productivity gains, their post-merge code quality remains underexplored, as prior work has largely relied on benchmarks and controlled tasks rather than large-scale post-merge analyses.
- **[28] The study analyzes 1,210 merged agent-generated bug-fix PRs from Python repositories in the AIDev dataset and uses SonarQube differential analysis to identify newly introduced code quality issues.**
  > To address this gap, we analyze 1,210 merged agent-generated bug-fix PRs from Python repositories in the AIDev dataset. Using SonarQube, we perform a differential analysis between base and merged commits to identify code quality issues newly introduced by PR changes.
- **[28] Raw issue-count differences across agents largely disappear after normalizing by code churn, indicating that higher issue counts are primarily driven by larger PRs.**
  > Our results show that apparent differences in raw issue counts across agents largely disappear after normalizing by code churn, indicating that higher issue counts are primarily driven by larger PRs.
- **[28] Across all agents, code smells dominate newly introduced issues, particularly at critical and major severities, while bugs are less frequent but often severe.**
  > Across all agents, code smells dominate, particularly at critical and major severities, while bugs are less frequent but often severe.
- **[28] Merge success does not reliably reflect post-merge code quality for agent-generated bug-fix PRs, and the authors highlight the need for systematic quality checks.**
  > Overall, our findings show that merge success does not reliably reflect post-merge code quality, highlighting the need for systematic quality checks for agent-generated bug-fix PRs.
- **[29] The authors interpret rising approval, declining comment effort, and increasing queue time as most consistent with reflexive habituation under growing workload rather than rational trust calibration alone.**
  > The combination of rising approval, declining comment effort, and increasing queue time is most consistent with reflexive habituation under growing workload rather than rational trust calibration alone.
- **[31] The study compares 204,673 test artifacts: 24,941 human-authored files and 179,732 agent-generated files from the AIDev dataset.**
  > We address this methodological gap through a large-scale, empirical comparison of 204,673 test artifacts which comprises of 24,941 human-authored files and 179,732 agent-generated files; sourced from the AIDev dataset.
- **[31] Agent-generated tests had a higher flakiness candidate rate of 0.41 versus 0.30 for human-authored tests, attributed mostly to file I/O and non-deterministic logic.**
  > But this thoroughness comes at a price: due mostly to their reliance on file I/O and non-deterministic logic, agent-generated tests exhibited a higher risk of flakiness (Candidate Rate: 0.41 vs. 0.30).
- **[31] The authors warn about 'stealth technical debt' in which test suites pass execution but do not provide comprehensive coverage or semantic value.**
  > This raises the possibility of "stealth technical debt", in which test suites pass execution but do not offer comprehensive coverage or semantic value.
- **[31] The paper concludes that AI agents lack the environmental awareness needed to write stable, hermetic tests.**
  > These findings suggest that while AI agents excel at rigorous boundary testing, they lack the "environmental awareness" needed to write stable, hermetic tests.
- **[31] The paper states that coding agents in CI/CD have altered verification, but benchmarks such as SWE-bench focus on pass rates rather than the intrinsic quality of generated tests.**
  > The integration of AI-powered coding agents into Continuous Integration/Continuous Delivery (CI/CD) pipelines has fundamentally altered how software verification is conducted. While these agents successfully automate the test generation, current evaluation benchmarks (e.g., SWE-bench) largely focus on pass-rates rather than the intrinsic quality of the generated tests.
- **[32] The study concludes that real-world AI-human differences on code-level metrics are rather small, contrasting lab observations, and finds language-dependent variance in security quality.**
  > Our results provide new findings and insights: some contrast previous observations in the lab setting (e.g., we conclude that real-world AI-Human differences on code-level metrics are rather small instead of more pronounced), some extend prior results with finer-grained observations (e.g., the variance of security quality across different programming languages), yet more are presented for the first time on aspects not covered before (e.g., code duplication rate, commit size and stability, etc.).
- **[32] Existing studies of AI-generated code are usually limited to lab settings, synthetic benchmarks, small coding tasks, and limited metrics.**
  > Existing study on AI-generated code is usually limited in the lab setting with synthetic benchmarks and small-scale coding tasks and covers limited metrics.
- **[33] The study identified 364 maintainability and security-related build smells across severity levels, indicating AI-generated build code can introduce quality issues such as missing error handling and hardcoded paths or URLs while sometimes removing existing smells through refactorings.**
  > We identified 364 maintainability and security-related build smells across varying severity levels, indicating that AI-generated build code can introduce quality issues-such as lack of error handling, and hardcoded paths or URLs-while also, in some cases, removing existing smells through refactorings (e.g., Pull Up Module and Externalize Properties).
- **[33] The paper explicitly investigates whether AI coding agents generate build code with quality issues, how well AI agents can eliminate build-code smells, and how often developers accept agent-authored pull requests.**
  > Our paper leverages this dataset to investigate (RQ1) whether AI coding agents generate build code with quality issues (e.g., code smells), (RQ2) to what extent AI agents can eliminate code smells from build code, and (RQ3) to what extent Agentic-PRs are accepted by developers.
- **[33] The study relies on AIDev, described as the first large-scale, openly available dataset of agent-authored pull requests from real-world GitHub repositories.**
  > This data mining challenge focuses on AIDev, the first large-scale, openly available dataset capturing agent-authored pull requests (Agentic-PRs) from real-world GitHub repositories.
- **[35] The paper identifies two AI-agent failure modes: context explosion degrading output quality as context fills, and silent spec-code drift becoming costly to repair.**
  > AI coding agents dramatically accelerate implementation speed but introduce two structural failure modes that existing spec-driven approaches do not fully solve: (1) context explosion -- the agent must reason over an entire repository at once, degrading output quality as the context window fills; and (2) silent spec-code drift -- code evolves, the specification does not, and the divergence becomes invisible until it is costly to repair.
- **[36] The study used randomized controlled trials at Microsoft, Accenture, and an anonymous Fortune 100 company, giving a random subset of developers access to an AI coding assistant as part of ordinary business.**
  > This study evaluates the impact of generative AI on software developer productivity via randomized controlled trials at Microsoft, Accenture, and an anonymous Fortune 100 company. These field experiments, run by the companies as part of their ordinary course of business, provided a random subset of developers with access to an AI-based coding assistant suggesting intelligent code completions.
- **[38] As of the article, 589 Meta engineers had engaged with Catching JiTTests, representing 64% of outreach, and the reported true-positive rate was 60%.**
  > As of this writing, 589 engineers at Meta (64% of our outreach) have engaged with Catching JiTTests. These engineers have reported that Catching JiTTests surfaces genuinely actionable findings, with a 60% rate of true positives.
- **[38] In the first half of 2026, Catching JiTTests caught 74 serious privacy bugs at the diff stage and lowered overall privacy SEVs by 20%.**
  > In the first half of 2026, Catching JiTTests played a key role in catching 74 serious (SEV) privacy bugs at the diff stage, before they landed in production and lowering the overall occurrence of privacy SEVs by 20% during that timeframe.
- **[38] Catching JiTTests generates executable tests that demonstrate a concrete behavioral difference and can catch bug classes that LLM- or agent-based code review might miss, at the cost of more computational steps.**
  > It generates executable tests that demonstrate a concrete behavioral difference introduced by the change. While it requires more computational steps, it catches classes of bugs that LLM- or agent-based code reviews might not.
- **[39] 90% of survey respondents use AI at work, more than 80% believe it increased their productivity, and 30% report little or no trust in AI-generated code.**
  > The majority of survey respondents (90%) use 
AI as part of their work and 
believe (more than 80%) it has increased their productivity. 
Yet a notable portion (30%) currently report little to no trust 
in the code generated by AI, indicating a need for critical validation skills.
- **[40] Microsoft Digital engineers describe prior “vibe coding” as expensive chaos and say they learned from those traps that SDD provides both velocity and direction.**
  > “Speed without direction is just expensive chaos—and we learned that the hard way through vibe coding. After burning our hands on those traps, we realized that SDD gives you both velocity and vector.”
- **[41] Docs name a common failure mode where Claude reports completion even though the work is not done because it could not check its own work.**
  > Claude said it was done and it wasn’t quite, usually because it had no way to check its own work.
- **[41] Prompt, CLAUDE.md, and skills are non-deterministic because the model decides whether to follow them; there is no guarantee.**
  > Non-deterministic: you write the instruction, and Claude (the model) reads it. This can be your prompt, `CLAUDE.md`, or a skill. The model then decides what to do with this information. It usually follows your commands, and current models are good at understanding your intent without much context, but there’s no _guarantee_ that it’ll follow your instructions.
- **[43] Agent autonomy produced drift and “AI slop”; the team initially spent every Friday, 20% of the week, cleaning it up, then encoded golden principles and a recurring cleanup process.**
  > Initially, humans addressed this manually. Our team used to spend every Friday (20% of the week) cleaning up “AI slop.” Unsurprisingly, that didn’t scale.

Instead, we started encoding what we call “golden principles” directly into the repository and built a recurring cleanup process.
- **[45] 48% of respondents trust AI when they can easily validate the answers, while only 16% extend that trust to most tasks that are not important work decisions.**
  > When asked when it’s acceptable to trust AI, 48% indicate they trust AI when they can easily validate the answers and only 16% extend that trust to most tasks that are not important work decisions.
- **[45] Human-in-the-loop is the dominant mode of working with AI tools.**
  > That’s why human-in-the-loop is the dominant mode of working with these tools.
- **[45] Six out of ten users cite a reason to avoid using AI at work or school, and losing job skills is a top concern.**
  > 6 out of 10 users cite a reason to avoid using AI at work or school, losing job skills is a top concern.
- **[45] Among users who avoid AI, concern over losing job skills is 17.1%, moral/ethical concerns 15.2%, privacy/security issues 13.0%, and environmental concerns 8.2%.**
  > | Concern over losing job skills or training an AI to replace you | 2,367 | 17.1% |
| Moral or ethical concerns | 2,108 | 15.2% |
| Issues with privacy or security | 1,802 | 13.0% |
| Environmental concerns | 1,129 | 8.2% |
- **[46] On easier tasks, the dramatic gains attributed to specifying first are largely a reasoning effect in disguise, so quality claims should control for reasoning first.**
  > On easier tasks, the dramatic gains people attribute to "specifying first" are largely a reasoning effect in disguise. If you are going to claim specification prompting improves quality, control for reasoning first.
- **[46] The author describes the study findings as preliminary and directional, based on small samples and a few tasks.**
  > They are preliminary and directional with small samples and a few tasks.
- **[47] Early agent test migration required four tries; docs were hard to find because the context window ran out, tests were inconsistent, and developers rated the internal framework NPS -3.**
  > The team's first attempt was having an agent migrate tests, and it took four tries. The team started with "migrate this file," then added instructions, then the APIs to use, then how to mock data.

The docs were also hard to find, since the agent's context window ran out before it found the right page. And they were inconsistent, because tests were not written the same way across the codebase.

Developers rated the internal framework at a [Net Promoter Score](https://en.wikipedia.org/wiki/Net_promoter_score) of -3.
- **[47] CI remains deterministic and runs builds, tests, screenshot diffing, merge queues, and canaries.**
  > Khuzam noted that the CI pipeline is still deterministic, running builds, tests, screenshot diffing, merge queues and canaries.
- **[48] DORA's sample calculator shows a negative downtime impact of $344,000 because the assumed change failure rate rises from 5% to 6% after AI adoption.**
  > The model accounts for this as a cost, and the sample calculator actually shows a negative downtime impact of $344,000 because the assumed change failure rate rises from 5% to 6% after AI adoption.
- **[48] Stanford research cited by DORA found AI yields a 35 to 40% productivity gain on simple greenfield tasks but often 10% or less on complex legacy code.**
  > Research cited in the report from Stanford University's Software Engineering Productivity programme found that while AI yields a 35 to 40% productivity gain on simple, greenfield tasks, its impact on complex legacy code is often 10% or less; a finding that matters for the many organisations working primarily on existing systems.
- **[48] The report cites Google Cloud data showing an average 727% return on Google Cloud AI over three years and an average payback period of around eight months.**
  > For the longer term, the authors point to Google Cloud data showing an average 727% return on investment in Google Cloud AI over three years, and an average payback period of around eight months.
- **[49] WeTravel decided not to use AI for code reviews because it generated too much noise.**
  > WeTravel, a Series C travel tech company, [decided](https://newsletter.pragmaticengineer.com/i/186760687/5-how-one-company-accurately-measures-code-review-usefulness) to not use AI for code reviews because of the amount of noise it generated.
- **[51] The report says survey-based findings capture developers feeling more productive at the individual level, because task completion is up and code is flowing faster.**
  > DORA's  fi ndings are based on surveys. Surveys capture how developers feel about their work. And right now, developers feel more productive, because at the individual level, they are. Task completion is up. Code is  fl owing faster. The tools feel powerful.
- **[52] Atlassian reports that 96% of companies are not experiencing AI-driven transformation at the organizational level, while only about 4% describe meaningful company-wide impact.**
  > **96% of companies report that they are not experiencing an AI-driven transformation at the organizational level**. Only about 4% describe meaningful, company-wide impact.
- **[53] Veracode's 2025 GenAI Code Security Report tested over 100 large language models across Java, Python, C#, and JavaScript to see if advanced AI systems can write secure code.**
  > In our new **2025 GenAI Code Security Report**, we tested over **100 large language models** across **Java, Python, C#, and JavaScript**. The goal? To see if today’s most advanced AI systems can write **secure** code.
- **[53] 45% of code samples failed security tests and introduced OWASP Top 10 vulnerabilities.**
  > 45% of code samples failed security tests and introduced OWASP Top 10 security vulnerabilities into the code.
- **[53] Java was the riskiest language, with a 72% security failure rate across tasks.**
  > **Java** was the riskiest language, with a **72% security failure****rate**across tasks.
- **[53] Python had a 38% security failure rate, JavaScript 43%, and C# 45%.**
  > *   Python: 38%
*   JavaScript: 43%
*   C#: 45%
- **[53] Cross-Site Scripting (CWE-80) was a frequent issue; AI tools failed to defend against it in 86% of relevant code samples.**
  > In fact, one of the most frequent issues was:**Cross-Site Scripting (CWE-80)**: AI tools failed to defend against it in 86**%** of relevant code samples.
- **[53] Newer or larger models improved functional or syntactically correct code but not secure code; security performance stayed flat regardless of model size or training.**
  > While the models got better at writing **functional** or syntactically correct code, they were **no better at writing secure code**. Security performance remained **flat,**regardless of model size or training sophistication.
- **[53] AI-generated code can enter a stack through open-source maintainers, third-party vendors, low-code/no-code platforms, and outsourced contractors using GenAI behind the scenes.**
  > *   Open-source software maintainers
*   Third-party vendors
*   Low-code/no-code platforms
*   Outsourced contractors using GenAI behind the scenes
- **[53] The source's takeaway is that speed without security is an unaffordable risk.**
  > The takeaway is simple: **Speed without security is a risk you can’t afford.**
- **[54] Block duplication rose from 40.3 to 73.0 per million changed lines between 2023 and 2026 year-to-date, an 81% increase and the highest level on record.**
  > Measured per million changed lines, block duplication climbed from 40.3 in 2023 to 73.0 year-to-date in 2026 — an 81% increase over 2023 and the highest level on record.
- **[54] Moved/refactored code fell from 21% in 2022 to 3.8% year-to-date in 2026, while copy/paste rose from 9.4% in 2022 to 15.7% in the first half of 2026.**
  > After clocking in at 21% in 2022, the percentage of moved code dropped to 13% of changed lines in 2023, before freefalling to 3.8% year-to-date in 2026. Over the same window, copy/paste climbed from 9.4% (in 2022) to 15.7% in the first half of 2026.
- **[54] Function connectivity fell 35% since 2023, from 343 method calls per thousand changed lines to 223 year-to-date.**
  > Function connectivity — how often newly authored code connects to a different method or function — has fallen 35% since 2023, from 343 method calls per thousand changed lines to 223 year-to-date.
- **[54] Long-term update percent fell 74%, from 1.7% in 2023 to 0.46% year-to-date in 2026.**
  > "Long-term update percent" — the share of changes that remove or update code last touched more than twelve months ago — has fallen 74%, from 1.7% in 2023 to 0.46% year-to-date in 2026.
- **[55] DX cautions that its study covers a limited number of quarters, so the observed patterns are early observations rather than settled conclusions.**
  > Before exploring potential causes, an important caveat to mention is that our study covers a limited number of quarters, so the patterns we’re seeing here are early observations rather than settled conclusions.
- **[56] AI-DLC claims quality improves by applying organization-specific coding, design, and security standards and generating comprehensive test suites, improving traceability from requirements to deployment.**
  > AI enhances quality by consistently applying organization-specific standards – your coding practices, design patterns, and security requirements – while generating comprehensive test suites. This end-to-end AI integration improves coherence and traceability from requirements to deployment.
- **[57] The report says permission-hungry agents create a core tension by seeking maximum access to private data and external systems, making zero trust, sandboxed execution, and defense in depth non-negotiable.**
  > The permission-hungry agents are most useful because they seek the maximum access to private data and external systems, creating a core tension. Zero trust architectures, sandboxed execution, and defense in depth are now non-negotiable table stakes.
- **[57] The source says AI speed is driving a return to zero trust architecture, DORA metrics, and testability, including managing cognitive debt so developers still understand the systems they build.**
  > The speed of AI is driving a return to well-established techniques like zero trust architecture, DORA metrics, and testability to manage complexity. This includes managing cognitive debt to ensure developers still understand the systems they are building.
- **[58] The study examined 800 software developers on large engineering teams using GitHub Copilot, with a test group that had access and a control group without access, matched on similar roles, working days, and coding volume.**
  > It examined a sample of 800 software developers on large engineering teams whose organizations had adopted Microsoft’s GitHub Copilot, a GenAI-based coding assistant and developer tool. Uplevel’s study looked at key engineering metrics pre and post Copilot implementation. The developers studied were segmented into a test group (those with Copilot access) and control group (those without access) — both with similar roles, working days and coding volume.
- **[58] A cited survey says 97% of software developers, programmers, and engineers have used AI-powered coding tools at work.**
  > And with [97% of software developers](https://github.blog/news-insights/research/survey-ai-wave-grows/), programmers and engineers having used AI-powered coding tools at work, businesses want to understand whether these tools improve outcomes.
- **[60] Stripe’s minions run in QA devboxes without real user data, production services, or arbitrary network egress, and an internal security framework prevents destructive tool actions.**
  > Since minions operate autonomously with full freedom to call their MCP tools, we also have an internal security control framework that ensures they can’t use their tools to perform destructive actions. As a first line of defense, though, our devboxes already run in our QA environment, and consequently, minions don’t have access to real user data, Stripe’s production services, or arbitrary network egress.
- **[61] Some developers reported that final work quality differed between AI-allowed and AI-disallowed conditions, including subjective code quality and the amount of documentation or tests created.**
  > Some developers told us the quality of the final work, for a given task, was different between AI-allowed and AI-disallowed conditions, e.g. differences in subjective code quality, or the amount of documentation or tests they chose to create.
- **[61] Developers sometimes self-report very high speedups, but METR says those estimates can be quite unreliable.**
  > Some developers self-report very high speedups, though as we documented in our earlier study those estimates can be quite unreliable.
- **[62] The authors caveat that Mux users likely skew toward engineers who were already high-output and AI-forward, so they do not claim Mux is the sole cause.**
  > These numbers come with caveats. Mux users likely skew toward engineers who were already high-output and AI-forward, so we don't claim Mux is the sole cause.
- **[63] The source argues code is a liability and that every extra AI-produced line must be tested, maintained, and secured.**
  > In software delivery, code is a liability, not an asset (even if the accountants tell a different story). Every extra line of code produced by an AI is an extra line that must be tested, maintained, and secured.
- **[63] The source claims that putting more code live enlarges the security attack surface and that flooding production with unverified, AI-generated code exponentially increases security risks.**
  > The more code an organisation puts live, the larger its security attack surface becomes. Threat actors - whether nation-states or dark web syndicates - are constantly looking for vulnerabilities. Flooding production with unverified, AI-generated code exponentially increases security risks.
- **[64] The source says that for most of 2025, the default mainstream position was that AI-generated code was slop and might always be slop.**
  > It’s easy to forget, but for most of 2025, the idea that AI-generated code was slop and might always be slop was not only a reasonable position to hold, it was the default, mainstream position.
- **[64] The source says that after Opus 4.5, AI could generate code approximately as good as the median software engineer for common patterns, faster and more cheaply.**
  > Ever since Opus 4.5 came out, AI has been able to generate code that is approximately as good as that of the median software engineer, at least for common patterns, and much faster and more cheaply.
- **[66] The curl bug bounty produced 87 confirmed vulnerabilities and paid over 100,000 USD in rewards.**
  > We have certainly made curl better as a direct result of this: **87 confirmed vulnerabilities and over 100,000 USD** paid as rewards to researchers.
- **[66] The share of curl security submissions confirmed as real vulnerabilities fell from above 15% in prior years to below 5% starting in 2025.**
  > Previous years we have had a rate of somewhere north of 15% of the submissions ending up confirmed vulnerabilities. Starting 2025, the confirmed-rate plummeted to below 5%. Not even one in twenty was _real_.
- **[66] curl saw an explosion in AI slop reports and lower quality even among non-obvious slop reports, presumably because reporters were misled by AI.**
  > We saw an [explosion in AI slop reports](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/) combined with a lower quality even in the reports that were not obvious slop – presumably because they too were actually misled by AI but with that fact just hidden better.
- **[66] curl removed monetary rewards for security reports of any severity to remove incentives for submitting made-up reports.**
  > We no longer offer any monetary rewards for security reports – no matter which severity. In an attempt to remove the incentives for submitting made up lies.
- **[66] For pull requests, curl relies on automated tools, tests, and scanners, and does not spend human time until contributions pass 200 CI jobs.**
  > I believe that for PRs we have much better means to sort out the weed with automatic means, since we have tools, tests and scanners to verify such contributions. We don’t need to waste any human time on pull requests until the quality is good enough to get green check-marks from 200 CI jobs.
- **[67] Block reports that mobile and JVM backend developers have particular difficulty using frontier AI models and tools, and that tooling working for web developers does not necessarily work as well for them.**
  > For example, our mobile and JVM backend devs have quite the challenge with the frontier models and tools. What works for web developers doesn't necessarily work as well for them.
- **[68] Aquifer’s architecture puts the agent harness outside the sandbox so the agent loop is not in the same blast radius as destructive commands.**
  > **Safety:** the agent loop is not in the same blast radius as `rm -rf`
- **[69] For riskier tasks the author uses asynchronous coding agents with network access, accepting source-code leakage as the stated worst-case risk.**
  > For riskier tasks I’m currently using asynchronous coding agents—usually Codex Cloud—so if anything goes wrong the worst that can happen is my source code getting leaked (since [I allow it to have network access](https://simonwillison.net/2025/Jun/3/codex-agent-internet-access/) while running).
- **[70] In a guardrail failure, an agent in auto-approve mode hallucinated a connection to a deprecated legacy agent and sent false emails to fifty colleagues.**
  > Without a specified URL, the agent hallucinated by connecting to a deprecated legacy agent with no email safeguards. The result? Fifty colleagues received false emails filled with hallucinated content.
- **[70] The source asserts that when development accelerates, the bug-to-code ratio remains constant, so the error rate does not change; only blame and speed of occurrence change.**
  > When development accelerates, the bug-to-code ratio remains constant. The actual error rate doesn't change, just who receives the blame and how quickly it happens.
- **[71] Kent Beck reports good correctness and performance but poor code quality due to accidental complexity in the final augmented-coding result.**
  > I feel good about the correctness & performance, not so good about the code quality. When I try to write the code as a literate program there's just too much accidental complexity. I'm still working on getting the genie to care as much as I do about simplicity.
- **[71] A warning sign that the AI agent was going off track was cheating by disabling or deleting tests.**
  > Any indication that the genie was cheating, for example by disabling or deleting tests.
- **[73] The source is framed around the concept of verification debt, linking generative AI's faster pace of change to proof or verification failing to keep up.**
  > Title: Verification Debt: When Generative AI Speeds Change Faster Than Proof

## q6. Are there documented cases where throughput rose without a stability loss, and what distinguished them?

- **[3] The authors position KPR as empirically testable, with value contingent on whether auditable extraction, transformation, and project-side regeneration reduce the cost of understanding and reworking high-context external changes.**
  > We position KPR as an empirically testable workflow: its value depends on whether auditable extraction, transformation, and project-side regeneration reduce the cost of understanding and reworking high-context external changes.
- **[4] The paper claims risk-aware layered automation can materially reduce review bottlenecks caused by AI-driven code growth without compromising production safety.**
  > Risk-aware layered automation can materially reduce review bottlenecks created by AI-driven code growth without compromising production safety.
- **[7] The source does not present documented cases of throughput rising without stability loss; its outcome claim is modeled velocity preservation plus compliance evidence coverage.**
  > Evaluation through regulatory coverage analysis, comparative framework analysis, and analytical productivity modeling suggests that graduated oversight preserves 84--97% of agentic coding velocity (central estimate: 91%) while maintaining compliance evidence coverage for regulated functions.
- **[8] Within the study's tasks and measures, there were no consistent warning signs of degraded code-level maintainability.**
  > Within the scope of our tasks and measures, we observed no consistent warning signs of degraded code-level maintainability.
- **[9] The source is a Stage 1 registered report accepted in principle for the 40th ICSME, not a completed results paper.**
  > Accepted as In-Principal Acceptance (IPA) for a Stage 1 registration of the Registered Report Track at the 40th IEEE International Conference on Software Maintenance and Evolution (ICSME)
- **[12] Successive harness releases raised mean performance from 59.4 to 63.0 using the same model and task suite.**
  > Beyond model comparison, the benchmark provides actionable feedback for harness refinement: diagnosis guides targeted improvements, and successive harness releases raise mean performance from 59.4 to 63.0 using the same model and task suite.
- **[15] The authors find that individual benefits may come from clarifying intent before delegation, while team benefits may depend on spec-driven development becoming a shared process.**
  > We also find that individual benefits may come from clarifying intent before delegation, while team benefits may depend on SDD becoming a shared process.
- **[17] The paper presents its work as a first step rather than a validated theory and calls for future empirical validation.**
  > Given the immaturity of the evidence base, this work is presented as a first step toward academic-industrial consensus rather than a validated theory, and outlines a research agenda for future empirical validation.
- **[22] Agentic PR workflows differ systematically by agent: Copilot and Devin PRs were more often embedded in reviewer-mediated workflows, while Codex and Cursor PRs were typically merged with minimal interaction.**
  > We further observed systematic differences across agents, with Copilot and Devin more often embedded in reviewer-mediated workflows, while Codex and Cursor PRs were typically merged with minimal interaction.
- **[39] DORA describes AI as an amplifier that magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones.**
  > AI’s primary 
role in software development is that of an amplifier. It magnifies the strengths of high-performing organizations and the 
dysfunctions of struggling ones.
- **[39] Value stream management is presented as a force multiplier for AI, ensuring local productivity gains translate into measurable team and product performance improvements.**
  > Value stream management (VSM), the practice of visualizing, analyzing, and 
improving the flow of work 
from idea to customer, acts as a force multiplier for AI, ensuring that local productivity gains translate into measurable improvements in team and 
product performance.
- **[40] Microsoft Digital asserts that its SDD process helps teams align stakeholders earlier, reduce rework, and use AI coding agents more effectively while keeping a connection to business goals.**
  > The result is a development process that helps teams align stakeholders earlier, reduce rework, and make more effective use of AI coding agents while maintaining a clear connection to business goals.
- **[42] Meta reports that its autonomous stress-testing loop caught and fixed a memory issue during development rather than after launch, roughly halving memory use and page faults.**
  > **Quality, found early:** The autonomous stress-testing loop caught and fixed the aforementioned memory issue during development rather than post-launch, roughly halving memory use and page faults.
- **[47] The documented Netflix Commerce case increased pull requests 32% year over year while reporting no Sev 1 incidents on a core service in 2026, indicating throughput rose without stability loss on that service.**
  > Khuzam reported no Sev 1 incidents in 2026 on a core service and 32% more pull requests year over year. Developer NPS rose from -3 to +25 over three quarters.
- **[48] DORA's team lead says the greatest AI returns come from the underlying organizational system—internal platform quality, workflow clarity, and team alignment—not the tools; without that foundation, AI creates localized productivity lost downstream.**
  > "The greatest returns on AI investment come not from the tools themselves but from a strategic focus on the underlying organizational system: the quality of the internal platform, the clarity of workflows, and the alignment of teams," writes Nathen Harvey, the DORA team lead at Google Cloud. "Without this foundation, AI creates localized pockets of productivity that are often lost in downstream chaos."
- **[49] Duckbill improved guardrails including unit and end-to-end testing, post-deploy observability, stricter linting and type checking, and 85% unit test coverage, and reported merged PRs rising from 353 to 684 (+94%).**
  > *   **Improve our guardrails** (unit and end-to-end testing, post-deploy observability, stricter linting and type checking, etc). Improving guardrails was pretty easy, just expensive in tokens and attention. We enabled nearly every rule in ruff/prettier/eslint/ty, and we improved our unit test coverage to a floor of 85%.

Results before vs after:

*   PRs merged: 353 → 684 (80/wk → 154/wk, +94%)
- **[51] The report states all organizations suffer the Acceleration Whiplash regardless of engineering maturity; strong pre-AI practices show the same quality degradation.**
  > One  fi nding holds across all segments of data: All organizations suffer from the Acceleration Whiplash, irrespective of their engineering maturity. The organizations with strong pre-AI engineering practices see the same quality degradation as those without.
- **[54] The source states that throughput is real but so is the accrued debt, which concentrates among developers who have not recognized the failure modes threatening long-term maintainability.**
  > The throughput is real, but so is the debt it accrues, and that debt concentrates among developers who haven’t recognized the failure modes that endanger long-term repo maintainability.
- **[62] Engineers report a qualitative shift toward attempting work they would not have before, including multi-service refactors, batches of bug fixes, features plus test suites, and multi-day efforts becoming single-session workflows.**
  > Beyond the metrics, engineers consistently report a qualitative shift: they attempt work they wouldn't have before. Refactors that touch multiple services, batches of bug fixes, features plus their test suites. Multi-day efforts become single-session workflows.
- **[63] The source prescribes end-to-end tiny slices for rapid value flow, deployed safely and quality-verified before iteration, rather than large unverified blocks.**
  > The only approach that works effectively for rapid value flow - with or without AI - is breaking work down into end-to-end tiny slices. Instead of building a massive, unverified block of software/content/data and throwing it over the wall, we must build the smallest possible increment, deploy it safely, verify its quality, and iterate.
- **[64] The author estimates the share of software engineering teams working in short, fast feedback loops is appallingly small—five percent maybe, definitely less than 10%—and calls this the cardinal sign of discipline.**
  > The share of software engineering teams that work in short, fast feedback loops (the cardinal sign of discipline in my book) is, and always has been, appallingly small. Five percent, maybe? Definitely less than 10%.
- **[67] Block teams reported pulling in more tickets mid-sprint because an agent had already completed 15 days of engineering work.**
  > Teams even reported pulling in more tickets mid-sprint because their agent had already completed 15 days of engineering work.

## Sources

1. From Industry Claims to Empirical Reality: code review of AI code — Kowshik Chowdhury, Dipayan Banik, K M Ferdous, Shazibul Islam Shamim (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2604.03196
2. METR: measuring the impact of early-2025 AI on experienced developers — Joel Becker, Nate Rush, Beth Barnes, David Rein / METR (primary, 2025-07-10, quality 1.0) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
3. Knowledge-Based Pull Requests: a trusted workflow — Xinyu Zhang and Weiwei Sun (academic, 2026-06-25, quality 1.0) — https://arxiv.org/abs/2606.26721
4. Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency — Chris Adams et al. (arXiv) (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2605.30208
5. Security Vulnerability Patterns in AI-Generated Code: A Cross-Model Comparative Study — Shanna M. Kahn, John D. Hastings (academic, 2026-07-22, quality 1.0) — https://arxiv.org/abs/2607.20713
6. From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents — Sanderson Oliveira de Macedo (academic, 2026-06-03, quality 1.0) — https://arxiv.org/abs/2606.04967
7. Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains — Richard Kang (academic, 2026-06-21, quality 1.0) — https://arxiv.org/abs/2606.22484
8. Echoes of AI: downstream effects of AI assistants — Markus Borg et al. (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2507.00788
9. Does Co-Development with AI Assistants Lead to More Maintainable Code — Markus Borg, Dave Hewett, Donald Graham, Noric Couderc, Emma Söderberg, Luke Church, Dave Farley (academic, 2024-08-20, quality 1.0) — https://arxiv.org/abs/2408.10758
10. Investigating Autonomous Agent Contributions in the Wild — Razvan Mihai Popescu, David Gros, Andrei Botocan, Rahul Pandita, Prem Devanbu, Maliheh Izadi (academic, 2026-04-01, quality 1.0) — https://arxiv.org/abs/2604.00917
11. Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen — Om Nepal, Sushant Aryal, Oluseyi Olukola, Nick Rahimi (academic, 2026-09-22, quality 1.0) — https://arxiv.org/abs/2609.26749
12. When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories — Tianqi Liu, Yandong Guan, Songze Li, Wenkai Wang, Gang Yu, Chengfei Lv (academic, 2026-10-20, quality 1.0) — https://arxiv.org/abs/2610.26394
13. Rethinking Code Review in the Age of AI: A Vision for Agentic Code Review — Hüseyin Özgür Kamalı, Erdem Tuna, Vahid Haratian, Eray Tüzün (academic, 2026-05-17, quality 1.0) — https://arxiv.org/abs/2605.17548
14. Cheap Code, Costly Judgment: governable agentic software engineering — James C. Davis, Paschal C. Amusuo, Tanmay Singla, Berk Çakar, Kirsten A. Davis (academic, 2026-07-01, quality 1.0) — https://arxiv.org/abs/2607.01087
15. Spec-Driven Development as Prescribed and as Practiced — Shyam Agarwal, Anmol Singhal, Andrew Macvean, Bogdan Vasilescu, Travis Breaux (academic, 2026-08-25, quality 1.0) — https://arxiv.org/abs/2608.25202
16. Ontology-Grounded Project Memory for Coding Agents — James Adam (academic, 2026-08-13, quality 1.0) — https://arxiv.org/abs/2608.13662
17. Spec-Driven Development for Agentic Software Engineering — Jessica Diaz, Joaquin Gayoso, Andrea Cimminio, Jorge Perez (arXiv) (academic, 2026-09-02, quality 1.0) — https://arxiv.org/abs/2609.00252
18. Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code — Dominik Blain and Maxime Noiseux (academic, 2026-04-07, quality 1.0) — https://arxiv.org/abs/2604.05292
19. Quality and Security Signals in AI-Generated Python Refactoring Pull Requests — Mohamed Almukhtar, Anwar Ghammam, Hua Ming (academic, 2026-05-20, quality 1.0) — https://arxiv.org/abs/2605.21453
20. Beyond Code Generation: Reliability, Verification, and Cost Economics in the Agentic Software Development Lifecycle — Happy Bhati (academic, 2026-09-04, quality 1.0) — https://arxiv.org/abs/2609.04681
21. We Have a Package for You: package hallucinations across LLMs (USENIX 2025) — Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala (academic, 2024-06-12, quality 1.0) — https://arxiv.org/abs/2406.10279
22. Why Are Agentic Pull Requests Merged or Rejected — Sien Reeve O. Peralta et al. (arXiv, MSR 2026) (academic, 2026-05-21, quality 1.0) — https://arxiv.org/abs/2605.22534
23. Chen & Stratton: AI in the Firm, Bottlenecks in Software Production — Fiona Chen and James Stratton (Harvard University) (academic, 2026-11-21, quality 1.0) — https://fion.ac/jellyfish.pdf
24. SDAD: Spec-Driven Agentic Development for the AI-Native SDLC — Vu Hung Nguyen; Thanh Nguyen (academic, 2026-05-05, quality 1.0) — https://arxiv.org/abs/2608.20341
25. WildCode Revisited: A Comprehensive Empirical Study on the Security of LLM-Generated Code — Kobra Khanmohammadi, Pooria Roy, Raphael Khoury, Abdelwahab Hamou-Lhadj, Wilfried Patrick Konan, Alexander Da Re, Nicholas Rebelo Melo (academic, 2025-12-03, quality 1.0) — https://arxiv.org/abs/2512.04259
26. From Code-Centric to Intent-Centric Software Engineering — Elyson De La Cruz (academic, 2026-05-10, quality 1.0) — https://arxiv.org/abs/2605.11027
27. Operationalizing Regulations into Code — Jonysberg Quintino, Hermano Moura, Filipe Calegário (arXiv, cs.SE) (academic, 2026-08-27, quality 1.0) — https://arxiv.org/abs/2608.27703
28. Beyond Bug Fixes: post-merge code quality issues — Shamse Tasnim Cynthia, Al Muttakin, Banani Roy (academic, 2026-01-27, quality 1.0) — https://arxiv.org/abs/2601.20109
29. Habituation at the Gate: rising approval and declining scrutiny in review of agent code — Haoran Yu, Lifei Liu, Xiaochong Jiang, Yuwen Jia, Su Wang, Pin Qian, Yihang Chen (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2606.22721
30. Before the Pull Request: Mining Multi-Agent Coordination — Dipankar Sarkar (arXiv:2606.19616, cs.SE) (academic, 2026-06-17, quality 1.0) — https://arxiv.org/abs/2606.19616
31. Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects — Preet Jhanglani, Zeel Kaushal Desai, Vidhi Kansara, Eman Abdullah AlOmar (academic, 2026-08-24, quality 1.0) — https://arxiv.org/abs/2607.12068
32. A Large-Scale Comprehensive Measurement of AI-Generated Code in Real-World Repositories A Large-Scale Comprehensive Measurement of AI-Generated Code in Real-World Repositories — Tianhao Mao, Dongfang Zhao, Haixu Tang, Xiaofeng Wang, Hang Zhang (academic, 2026-03-28, quality 1.0) — https://arxiv.org/abs/2603.27130
33. AI builds, We Analyze: An Empirical Study of AI-Generated Build Code Quality — Anwar Ghammam, Mohamed Almukhtar (academic, 2026-01-23, quality 1.0) — https://arxiv.org/abs/2601.16839
34. Role and Identity Work of Software Engineering Professionals — Jorge Melegati (arXiv preprint; accepted to CHASE 2026) (academic, 2026-02-20, quality 1.0) — https://arxiv.org/abs/2602.18190
35. The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development — Hartwig Grabowski (academic, 2026-06-25, quality 1.0) — https://arxiv.org/abs/2606.27045
36. Microsoft Research: three field experiments with developers — Microsoft Research (academic, 2025-06-01, quality 1.0) — https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/
37. Gartner: 60% of organisations adopt smaller engineering teams by 2029 — Gartner, Inc. (official, 2026-07-07, quality 0.9) — https://www.gartner.com/en/newsroom/press-releases/2026-07-07-gartner-predicts-60-percent-of-organizations-will-adopt-smaller-software-engineering-teams-by-2029
38. Meta: catching bugs before they land, JiTTests at full scale — Sreeja Thummala, Sophie Zeng, Mark Harman, Weini Liu, Eric Liu (Engineering at Meta) (official, 2026-10-29, quality 0.9) — https://engineering.fb.com/2026/10/29/security/catching-bugs-before-they-land-jittestings-human-on-the-loop-approach-at-full-scale/
39. DORA: State of AI-assisted Software Development 2025 — DORA / Google Cloud (official, 2025-09-23, quality 0.9) — https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
40. Microsoft Digital: spec-driven development at Microsoft — Neil Orint and David Hirning / Microsoft (official, 2026-09-03, quality 0.9) — https://www.microsoft.com/insidetrack/blog/engineering-the-frontier-firm-sharing-our-ai-native-approach-to-software-development/
41. Anthropic: Claude Code best practices — Anthropic (Claude Code Docs) (official, 2026-11-26, quality 0.9) — https://www.anthropic.com/engineering/claude-code-best-practices
42. Meta: how Meta built Forum with AI-native engineering — Meta Engineering (Shengbo Guo et al.) (official, 2026-10-15, quality 0.9) — https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/
43. OpenAI: harness engineering, leveraging Codex in an agent-first world — Ryan Lopopolo / OpenAI (official, 2026-02-11, quality 0.9) — https://openai.com/index/harness-engineering/
44. DORA: Impact of Generative AI in Software Development — DORA (official, 2026-04-13, quality 0.9) — https://dora.dev/ai/gen-ai-report
45. Stack Overflow Developer Survey 2026: AI — Stack Overflow (data, 2026-07-01, quality 0.9) — https://survey.stackoverflow.co/2026/ai
46. When Spec-Driven Development Pays off (GAISS 2026) — Nitin Garg / InfoQ (news, 2026-09-10, quality 0.7) — https://www.infoq.com/articles/when-spec-driven-development-pays-off/
47. Netflix at QCon SF: retrofitting the SDLC for AI coding agents — Andrew Hoblitzell (InfoQ) (news, 2026-11-23, quality 0.7) — https://www.infoq.com/news/2026/11/netflix-sdlc-ai-coding-agents/
48. InfoQ: DORA ROI report coverage — Matt Saunders / InfoQ (news, 2026-05-11, quality 0.7) — https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report
49. The Pragmatic Engineer: what is happening with code reviews — Gergely Orosz (news, 2026-09-08, quality 0.7) — https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews
50. GeekWire: how agentic AI is rewiring Amazon teams — Todd Bishop, GeekWire (news, 2026-06-16, quality 0.7) — https://www.geekwire.com/2026/how-agentic-ai-is-rewiring-amazons-teams-and-upending-its-traditions/
51. Faros AI Engineering Report 2026: The Acceleration Whiplash — Faros AI (vendor, 2026-04-09, quality 0.6) — https://pages.faros.ai/hubfs/AI%5FEngineering%5FReport%5F2026%5FThe%5FAcceleration%5FWhiplash%5FFaros.pdf
52. Atlassian: State of Developer Experience — Atlassian (vendor, 2026-01-16, quality 0.6) — https://www.atlassian.com/blog/development/how-tech-leaders-can-turn-ai-hype-into-real-team-productivity
53. Veracode: GenAI code security report — Jens Wessling / Veracode (vendor, 2025-07-30, quality 0.6) — https://veracode.com/blog/genai-code-security-report
54. GitClear: the AI code quality maintainability gap — GitClear (vendor, 2026-06-01, quality 0.6) — https://gitclear.com/the_ai_code_quality_maintainability_gap
55. DX: the AI efficiency plateau — Brian Houck / DX (vendor, 2026-05-27, quality 0.6) — https://getdx.com/blog/the-ai-efficiency-plateau
56. AWS: AI-Driven Development Life Cycle (AI-DLC) — Raja SP on AWS DevOps Blog (Amazon Web Services) (vendor, 2025-07-31, quality 0.6) — https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
57. Thoughtworks Radar v34: cognitive debt and harnesses — Thoughtworks (vendor, 2026-04-15, quality 0.6) — https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34
58. Uplevel: GenAI developers, no delivery gain and higher bug rate — Uplevel (Lauren Lang) (vendor, 2024-09-16, quality 0.6) — https://uplevelteam.com/blog/genai-developers
59. DORA: ROI of AI-assisted Software Development — Google Cloud / DORA (vendor, 2026-04-22, quality 0.6) — https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development
60. Stripe: minions, one-shot end-to-end coding agents, part 2 — Alistair Gray / Stripe (blog, 2026-02-19, quality 0.5) — https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
61. METR: uplift update, February 2026 — METR (Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud) (blog, 2026-02-24, quality 0.5) — https://metr.org/blog/2026-02-24-uplift-update
62. Coinbase: engineers as orchestrators of agent fleets — Alessandro Rodi, Adam Wolf (Coinbase) (blog, 2026-05-11, quality 0.5) — https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it
63. Team Topologies: stewardship of value flow — Matthew Skelton / Team Topologies (blog, 2026-08-18, quality 0.5) — https://teamtopologies.com/news-blogs-newsletters/team-topologies-for-the-ai-age-stewardship-of-value-flow
64. Charity Majors: AI demands more engineering discipline — Charity Majors (blog, 2026-06-15, quality 0.5) — https://charity.wtf/p/ai-demands-more-engineering-discipline
65. Will Larson: revised rules of engineering leadership — Will Larson (blog, 2026-06-15, quality 0.5) — https://lethain.com/revised-rules-of-engineering-leadership
66. curl: the end of the bug bounty — Daniel Stenberg (blog, 2026-01-26, quality 0.5) — https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
67. Block: AI-assisted development — Angie Jones / Block Engineering (blog, 2026-01-18, quality 0.5) — https://engineering.block.xyz/blog/ai-assisted-development-at-block
68. Shopify: Under the River — Burke Libbey, Javier Moreno, River (Shopify Engineering) (blog, 2026-05-28, quality 0.5) — https://shopify.engineering/under-the-river
69. Simon Willison: parallel coding agents — Simon Willison (blog, 2025-10-05, quality 0.5) — https://simonwillison.net/2025/Oct/5/parallel-coding-agents
70. Google Cloud: when AI writes the code, who reviews it — Lee Boonstra, Google Cloud Office of the CTO (blog, 2026-04-28, quality 0.5) — https://cloud.google.com/transform/when-ai-writes-the-code-who-reviews-it-cto-google-cloud
71. Kent Beck: augmented coding beyond the vibes — Kent Beck (blog, 2025-06-25, quality 0.5) — https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
72. Zapier: AI fluency in hiring, Chief People & AI Transformation Officer — Wade Foster (blog, 2025-10-29, quality 0.5) — https://zapier.com/blog/ai-transformation-leader/
73. Communications of the ACM: verification debt — CACM (blog, 2026-01-16, quality 0.5) — https://cacm.acm.org/blogcacm/verification-debt-when-generative-ai-speeds-change-faster-than-proof/
74. GitHub Spec Kit — GitHub (github/spec-kit) (official, 2025-09-01, quality 0.4) — https://github.com/github/spec-kit
