---
title: "What the World's Best Websites Are Doing in the AI Era (2026)"
date: 2026-10-03
type: special
url: https://luisgonzalezbernal.com/reports/reports/world-class-websites-2026-10-03.html
summary: "Performance · Rendering architecture · Agent-readable web · WebMCP & ACP · Design systems as API · Design craft · Accessibility · 59 sources"
tags: [agents, coding]
reading_time_minutes: 38
---
Web Engineering · Special Report

# What the World's *Best Websites* Are Doing in the AI Era

3 Oct 2026

Performance · Rendering architecture · Agent-readable web · WebMCP & ACP · Design systems as API · Design craft · Accessibility · 59 sources

## Executive Summary

**The structural shift of 2026 is that the user is no longer the only audience of a website.** The best teams build for three consumers at once — people, AI agents and regulators — and they have reorganised performance, design and infrastructure around that. This is not a list of new frameworks: it is a change in who the site is for.

**Performance is a contract, not a feature.** Only **55.9%** of origins pass all three Core Web Vitals (CrUX, May 2026, 18.4M origins) and the real bottleneck is LCP at 68.6%, not INP at 86.6%.[4] If your site fails, it almost certainly fails on loading.

**Less JavaScript — but with an architecture chosen on purpose.** Single-page apps are still how most teams ship (84%), against 61% SSR and 44% SSG; partial hydration reaches 25% and islands only 14%. React Server Components have been used by 45% of respondents and only a third of those rate the experience positively.[2] When the API is good adoption follows; when it demands rebuilding the app, it stalls.

**The web started serving markdown to whoever asks for it.** Content negotiation (`Accept: text/markdown` on the same URL) plus a hierarchical `sitemap.md` is the pragmatic replacement for `llms.txt` — which, for all the noise, is requested by roughly **0.1%** of AI-bot traffic and does not correlate with more citations.[12,31,33]

**The interface is becoming invocable tools.** **WebMCP** — a W3C draft co-authored by Google and Microsoft — lets a page *declare* what its forms do instead of forcing an agent to guess by simulating clicks, and it keeps the human in the loop with `toolactivated` / `toolcancel` events.[19,20]

**Checkout became an open protocol.** The **Agentic Commerce Protocol**, co-created by Stripe, OpenAI and Meta, defines agentic checkout, carts and feeds, delegated payment and delegated OAuth — with over a million Shopify merchants on the path to buying inside ChatGPT, and a one-line activation if you already run Stripe.[14,15]

**The design system became an API for agents.** Seventeen of twenty audited open-source design systems now ship an official MCP server, and Coinbase measured a **22.5% average cut in token cost** — alongside better design-system adherence — from giving agents component context instead of letting them improvise.[22,23]

**Accessibility stopped being a good practice in June 2025.** The European Accessibility Act has been enforceable since 28 June 2025 against EN 301 549 and WCAG 2.1 AA, and WCAG 2.2 is now ISO/IEC 40500:2025. Meanwhile **95.9%** of the top million home pages still carry detectable WCAG failures, and low-contrast text alone appears on 83.9% of them.[24,25,58]

**And the part the conference talks leave out:** the very move that makes a site machine-readable is what removes the human click. AI Overviews correlate with a **58%** drop in click-through rate for top-ranking pages, and a randomised experiment found that forcing users into AI Mode cut outbound clicks by 18.8 points *without* improving satisfaction.[35,36]

## Part I

## Four layers, two of which are new

Until recently a website had two audiences: the person and the search engine. In 2026 there are four layers of work, and the bottom two did not exist before. The teams with an edge are not investing in being *read* by machines — they are investing in being *executed* and *billed* by them.

*[Diagram: four layers of an agent-native web on a single rail — discover, understand, act, measure and monetise, with the 2026 break halfway down]*

*The four layers of work on a website in 2026, on one rail. The break comes halfway down: layers 3 and 4 did not exist before.[14,17,19]*

The first two layers are an evolution of what already existed: discovery and format. The novelty is the third and fourth — declaring tools so an agent can act, and measuring or charging for what each bot consumes.

## Part II

## Performance: still optimising against a bar almost nobody clears

The performance conversation has not changed in 2026. What changed is that it is now budgeted, and that the failure has moved to one very specific place.

| Core Web Vital | Good threshold | Origins passing (CrUX, May 2026) |
| --- | --- | --- |
| All three together | — | **55.9%** |
| LCP — largest contentful paint | ≤ 2.5 s | **68.6%** — the real bottleneck |
| CLS — cumulative layout shift | ≤ 0.1 | 81.3% |
| INP — interaction to next paint | ≤ 200 ms | 86.6% — the easiest to pass |

*[Bar chart: percentage of origins passing each Core Web Vital in 2026]*

*If your site fails Core Web Vitals, it almost certainly fails on LCP: most already pass INP and CLS. Loading, not interactivity, is where you lose.[4]*

### Two details that separate a good team from an excellent one

- **INP is no longer fixed where it used to break.** Measured on mobile, the cost of an interaction sits almost entirely in the *presentation* phase — 47 ms of a 49 ms median, or **96%** of the stack. Optimising the handler does not move the needle: you have to reduce the repaint cost, which scales with DOM size.[3]
- **Interactivity improved at the price of executing more JavaScript.** While INP got better, Total Blocking Time rose **58%**: the work was sliced into shorter tasks, not removed.[5]

### The elephant in the room: page weight

The median mobile page weighed **2.56 MB** in 2025, with 632 KB of JavaScript and 911 KB of images on the home page. The median mobile home page has grown **202.8%** since 2015, when it was 845 KB.[6,8]

Platform adoption, on the other hand, is going well: *variable fonts* are used by 41.3% of mobile sites and 72% of sites now serve their fonts from their own origin.[8,6] The same logic holds in CSS — `:has()` is used by 83.7% of respondents and is also the best-rated feature (51.8% positive), with `aspect-ratio` at 81.3% and CSS Nesting at 70.6%. Where the brake is browser support rather than enthusiasm, the list is explicit: anchor positioning is the number one feature developers avoid for compatibility reasons even while being the fastest-growing in usage (+15 points).[34]

In short: serious teams stopped asking the CDN for performance and started asking their own build decisions — and stopped polyfilling what the browser already knows how to do.

## Part III

## Architecture: three schools, no winner

The most honest data point of 2026 is not which framework people use, but how far declared adoption trails the noise. Single-page applications remain the dominant way teams ship to production.

*[Chart: rendering patterns used in production, per State of React 2025]*

*Rendering patterns used in production, share of respondents.[2]*

The adoption numbers do not follow the hype. Server Components have been used by 45% of respondents but only a third rate them positively; Suspense — which solves a smaller problem with a much better developer experience — has the highest adoption *and* satisfaction. When the API is good, adoption follows. When it demands redesigning the application, it stays at the 14% of islands.[2] Meanwhile `shadcn/ui` went from 20% to 56% usage in two years, the fastest rise in the ecosystem.[1]

| School | How it works | Where it wins |
| --- | --- | --- |
| **Islands** (Astro) | Static HTML by default; hydration is explicit per component via `client:load / idle / visible / only`. Server Islands mix edge-cached HTML with per-request fragments on the same page. | Content-heavy sites that need a little interactivity, not a lot. |
| **Server Components** (React, Next.js) | The server serialises React trees and promises; the client hydrates only what is marked `use client`. Smaller bundles, simpler data fetching. | Full-stack applications willing to change their mental model. |
| **Local-first** (Linear) | The database the UI reads lives in the browser, in IndexedDB. Mutations apply locally and reconcile in the background over WebSocket. | Interactive products where perceived latency is the product. |

> **The pattern all three share:** none of them tries to be fast — they try to *remove the perceived wait*. Linear states it outright: the key is hiding network requests from the user, and the fewer loading states the better. Astro does it by shipping no JavaScript where none was needed. Measured by the user, speed is how quickly the interface reacts, not how quickly the server answers.[9,27]

And if you cannot afford any of the three: optimistic updates with TanStack Query or SWR get surprisingly close — apply the change locally, validate in the background, roll back only if it fails. It is the highest return per hour you can buy.[9]

## Part IV

## The machine-readable web: the uncomfortable truth about `llms.txt`

Two things get mixed up constantly, and 2026's data is brutal about the difference: *publishing* something for agents is not the same as an agent *consuming* it.

*[Chart: 9.3% of the top 1,000 publish llms.txt against 0.1% of AI-bot requests asking for it]*

*Publishing llms.txt versus being asked for it: share of the top 1,000 sites against share of AI-bot requests.[31,32,33]*

9.3% of the Tranco top 1,000 publish an `llms.txt` — up from 0.3% in June 2025 — and in a broader sample 28% of domains do. But roughly **0.1%** of AI-bot requests ask for the file, below the traffic of a random blog post; of 515 million LLM-bot events across GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot and Google-Extended, only **408** targeted it. And sites that have it do not get cited more: 6.8 citations on average versus 6.7 without, p = 0.85. No major AI lab has confirmed that its crawler reads the file. Google has explicitly rejected the standard.[31,32,33]

| Signal | What 2026 shows |
| --- | --- |
| Publishers adopting it | Real and growing: 9.3% of the top 1,000, 8.3% of the top 10,000 (Sep 2026). |
| Crawlers requesting it | ~0.1% of AI-bot requests; 408 hits in 515M events. Statistically negligible. |
| Effect on citations | None measurable: 6.8 vs 6.7, p = 0.85. |
| Web Almanac | Only 2.1% of pages serve a valid `llms.txt`; `GPTBot` appears in 4.5% of `robots.txt` files (2.6% in 2024). |

### What does work

**Content negotiation.** The same URL returns markdown when the client sends `Accept: text/markdown`. It needs no site-specific knowledge from the agent and works for any client that sends the right header. Vercel ships it on its blog and changelog and serves a recursive `sitemap.md` that preserves hierarchy and titles — something a flat XML sitemap cannot express — plus `<link rel="alternate">` in the head as a discovery path for agents that send no header at all.[12]

> **Practical read for a team with no time to waste:** ship content negotiation and an explicit per-bot policy in `robots.txt`. Publish `llms.txt` only if your content is technical documentation and you generate it automatically — it costs nothing — but do not count it as a visibility strategy. Nobody has promised you it will be read.[12,31,33]

## Part V

## The machine-actionable web: from reading the web to operating it

This is the big change of 2026. Until now an agent "used" a website by simulating clicks and reading the DOM: slow, brittle and blind. The standard that is emerging turns that into a tool call.

### WebMCP — the page declares its own tools

A W3C draft specification, co-authored by Google and Microsoft, exposes `navigator.modelContext` in the browser. Instead of an agent inspecting a button to infer what it does, **the site declares its purpose**. There are two routes: a *declarative* one, adding `toolname` and `tooldescription` attributes to an ordinary `<form>` — no new JavaScript, just semantic HTML — and an *imperative* one, registering tools with a name, description and input schema in JavaScript.[19,20]

The browser brings the form into focus and fills it, and fires `toolactivated` / `toolcancel` events, so **the human still sees what is happening and can cancel it**. It has been in origin trial since Chrome 149, after landing in Canary 146 in February 2026.[20]

### ACP — the agentic commerce protocol

*[Diagram: purchase flow under the Agentic Commerce Protocol between user, agent, merchant and payment provider]*

*A purchase under the Agentic Commerce Protocol, between user, agent, merchant and payment provider.[14,15]*

ACP is an open standard created by Stripe, OpenAI and Meta. It defines agentic checkout (cart, fulfilment, payment), carts and product feeds, delegated payment, delegated authentication over OAuth 2.0, and order webhooks. The merchant accepts or declines the order, processes payment through its existing provider, and handles fulfilment and support exactly as before: **the merchant stays merchant of record**.[14,15]

- More than a million Shopify merchants — Glossier, SKIMS, Spanx, Vuori among them — are on the path to checkout inside ChatGPT, with direct purchases already live for Etsy sellers in the US.[15]
- If a merchant already processes payments with Stripe, enabling agentic payments can be as little as one line of code; otherwise the Shared Payment Token API or the Delegated Payments Spec keep its existing processor.[15]
- Stripe's Link wallet has 300 million users and around a million merchants, and since September 2026 it is wired into AI assistants from Meta, xAI and Instinct.[16]

### And the billing layer: if a bot consumes, can it pay?

Cloudflare's **Pay Per Crawl** is in private beta: for each AI crawler you decide *allow*, *charge* or *block*. The mechanics are elegant — the request gets an `HTTP 402 Payment Required` with a `crawler-price` header, the crawler retries by signing the request with **Web Bot Auth** and confirming with `crawler-exact-price`, and the response comes back with `crawler-charged`. Cloudflare acts as merchant of record with monthly settlement through Stripe. Always-free paths: `robots.txt`, `sitemap.xml`, `security.txt` and `crawlers.json`, and error responses are never billed.[17,18]

> **Do not block blindly.** The console itself warns that marking a search-engine crawler as *block* or *charge* can damage your SEO, because you fall out of the index. It is a business dial, not a panic button.[17]

## Part VI

## Design systems became infrastructure for agents

If an agent is going to write your UI, it needs your system — not a prompt full of adjectives. Leading teams publish tokens, rules and examples as versioned artefacts next to the code.

| What they publish | Who already does | What it buys |
| --- | --- | --- |
| **Design-system MCP server** | 17 of 20 audited open-source systems | The agent receives components, styles and variables instead of inventing them.[21,23] |
| **Official agent skills** | 17 systems; 14 publish `llms.txt` | Design and naming rules that are machine-readable, inside the repository.[23] |
| **Code Connect** (Figma → real components) | Carbon and Primer are the two in the audit | The agent uses your production component instead of reimplementing it.[23] |
| **A public design file** | Vercel (`design.md`) | Any agent, in any environment, loads your brand judgement from a URL.[10] |
| **Skill + linters + review loop** | Vercel (`product-design`) | Accepted decisions live in the repo as code and changes are reviewed against them.[11] |

Vercel's `design.md` is worth studying for one detail: it documents the **class names and tokens** of a public stylesheet, but the agent *never reads the CSS* — the browser loads it at render time. That leaves the whole context window for design judgement instead of spending it on style code. The file was built over more than 200 evaluation runs, with a model judge writing critiques for each round.[10]

And the number that justifies it: Coinbase Design System tested Code Connect against coding agents and found better design-system adherence with a **22.5% average reduction in token cost**.[22]

> **The transferable lesson:** agents do not invent states your components do not have — they *amplify what is documented*. Coverage, completeness and constraints stop being bureaucracy and become load-bearing. An incomplete design system does not produce incomplete UI; it produces invented UI.[23]

## Part VII

## The best designs, and why they are the best

In 2026 any model produces a plausible interface in seconds. That has not raised the average: it has made it visible. And there is an inconvenient data point to put in front of everything else — **the web was already homogenising before AI**. Taste Labs analysed more than two million websites going back a decade and that is exactly the finding that complicates the story. AI accelerated something that was already happening.[50]

*[Ladder diagram: five levels of interface craft, from hierarchy to invisible detail]*

*The first four rungs can be copied. The fifth is what separates: details nobody sees until they are missing, and where taste accumulates instead of leaking away.[45,48,54]*

### Who won in 2025 and 2026

Awards are not an objective measure of quality, but they are a verifiable list of what a jury of practitioners considers the ceiling of the year. Two citations and one oddity: the same site won both the jury vote and the public vote.

- **Awwwards Site of the Year 2025 — Lando Norris (OFF+BRAND).** An F1 driver's platform: dynamic interactions, bold visuals, 3D. It also took the Users' Choice award, which rarely coincides with the jury's.[38,39]
- **Developer Site of the Year 2025 — Messenger (abeto).** A small studio taking the technical category ahead of the large agencies.[38]
- **E-commerce of the Year 2025 — Scout Motors.** Designing a car brand from scratch buys you permission to ignore every e-commerce convention.[38]
- **Webby 2026, Best Home Page — The Renaissance Edition (Shopify).** Only the home page is judged, so it is pure front-page design with no product behind it to hide behind.[41]
- **Webby 2026, Cultural Institutions — National Gallery Imaginarium (Fabrique & Q42).** The hard part of cultural design is not turning an archive into a PDF with a menu.[41]
- **Webby 2026, Best Visual Design · Function — The Way**, a meditation app. The category is *function*: it rewards the design that sustains use, not the one that decorates.[40]

### The specific detail that makes each one a reference

"It looks nice" is not an argument. Each of these rests on a concrete decision, opposed to convention, that can be measured and copied. This is the part actually worth learning from them.

| System | The measurable detail | Why it works |
| --- | --- | --- |
| **Vercel** Geist | Radius 0 across the whole system, **zero** `box-shadow` — elevation is carried by 1 px hairlines — a 16 px body, 100–150 ms `ease-out` motion, and a single accent colour on under 1% of the surface.[55] | Lifting with a border instead of a shadow keeps the interface flat and legible at any density: nothing floats, nothing competes. And giving up bold forces hierarchy to come from size and space — which is what the eye reads best anyway.[43] |
| **Stripe** | Headlines at **weight 300** with negative tracking (−1.4 px at 56 px), the `ss01` stylistic set on every text element, tabular numerals (`tnum`) for financial data, multi-layer blue-tinted shadows at `rgba(50,50,93,0.25)`, and deep navy `#061b31` instead of black in headings.[44] | It is the opposite of the bold hero headline: whispered authority instead of shouted. The shadow's blue comes from the brand palette, so even elevation is on-brand. And tabular numerals are not aesthetics — they are how columns of money line up.[44] |
| **Linear** | A near-black canvas, a four-step surface ladder, 1 px hairlines, a single lavender accent, negative tracking in the type scale, and monospace reserved for identifiers. Its command menu — the app's central component — groups hundreds of actions ordered by the view you are in.[53] In the redesign the same theme generator was applied to the base palette so it could ship **very high contrast themes** (30 and 100) for accessibility.[46] | Technical density without noise: it reads like software documentation, which is exactly what it wants to look like. And contrast as a *system token* rather than a patch is how accessibility stops eroding.[46] |
| **Craft** (app) | They wrote their own components, layout system and animations instead of using SwiftUI and AutoLayout, and share a single codebase across iOS, iPad, macOS and Vision (about 99% common).[47] | Their thesis is the most useful of all: **one engineering culture is not enough**. With a UI-dominant culture (Apple) you get a delightful product and a weak backend; with a backend-dominant culture (Amazon, Google) you get excellent systems and less comfortable UIs. You need both.[47] |

*[Comparison: a conventional bold headline on black against Stripe's light headline in navy]*

*Typography is not a font catalogue, it is the product's voice set to a specific value. Both extremes are defensible; what is not is the default middle.[44,55]*

### Five things that genuinely make a design good

- **Hierarchy before ornament.** You are not decorating a canvas, you are deciding what is seen and in what order: size, contrast, spacing, position. When it fails, no amount of polish rescues it — and it is the most widespread failure on the web: 83.9% of the top million home pages have low-contrast text, and the average number of detected accessibility errors per page rose to 56.1 in 2026 after years of improvement.[58,57]
- **Typography is a voice, not a font.** The two best examples go to opposite extremes and both work: Stripe at weight 300 for headlines, Vercel banning weight 700 from the entire system. The constraint *is* the signature.[44,42,59]
- **Motion is physics, not decoration.** A timed animation assumes the world will wait for it to finish; real things have no assigned duration, they have weight and speed. That difference is what separates an interface that feels alive from one that feels fake.[56] And exits should be subtler than entrances: what leaves does not deserve the same attention as what arrives.[48]
- **Restraint: good design is a refusal mechanism.** Taste also comes from omission — what you cut, which font you avoided, which slogan you did not choose.[51] It is what Geist formalises with its "no"s: no radius, no shadows, no gradients, no second brand colour.[55]
- **Optical alignment, not geometric.** Padding next to an icon should be slightly smaller so the eye reads it as centred. And underneath, the detail nobody sees: Linear added safety areas to its contextual menus so you can move the cursor **diagonally** into a submenu without it vanishing on the way — previously you had to draw an upside-down "L" with the mouse, and they found that unacceptable because those seconds add up over a day.[48,45]

> **Why this matters more now than three years ago.** When everyone has the same tools, judgement is what separates. AI is excellent at compressing the beginning of the creative process — ideation, exploration, technical chores — and useless at replacing judgement at the end. One excellent image beats a thousand correct ones.[49] The real risk is not producing something ugly; it is landing in *the middle*, described as "visual elevator music" — the point where nothing is good or bad and which is more unforgivable than failing. Models cannot feel when something is off, because they are doing pattern completion at scale, remixing what already exists.[52] The mechanism, in one sentence: models generate details at scale but cannot make taste-informed trade-offs — and every detail delegated without the designer's judgement is a place where taste leaks out of the system.[54]

> **The link with Part VI.** This is an engineering matter, not a matter of sensibility: if your design system is the API agents consume,[21] your design decisions no longer deploy at the speed of a team — they replicate at the speed of a machine. A bad contrast token, or a hierarchy rule that was never written down, now propagates into every artefact your agents generate. Good taste stopped being an adjective and became an infrastructure requirement.

## Part VIII

## Accessibility: it stopped being a good practice in June 2025

This is the part most teams still file under "nice to have". It is not.

The **European Accessibility Act** (Directive (EU) 2019/882) was transposed into national law from 28 June 2022 and has been **enforceable since 28 June 2025**. The harmonised technical standard is EN 301 549, which for web and mobile references **WCAG 2.1 level AA** as the operative baseline. Market surveillance authorities in each member state can impose penalties, corrective orders and market restrictions.[24]

The technical bar is also rising on its own: WCAG 2.2 was approved as international standard **ISO/IEC 40500:2025** on 21 October 2025. Conformance with 2.2 implies 2.1 and 2.0, and criterion 4.1.1 *Parsing* was removed. The W3C now recommends 2.2 and is working on updating EN 301 549.[25,26]

> **How it is actually enforced.** The early cases do not ask whether you meet fifty-odd success criteria. They ask two things: *did you know you had the problem?* and *did you take reasonable steps?* The risk is not having issues — it is having no visibility into them. As with GDPR, 2025 was the year of internal routines and paper trails; 2026 starts being the year of accountability.[24]

And the starting point of the real web: **95.9%** of the top million home pages have detectable WCAG 2 A/AA failures — up from 94.8% a year earlier, reversing six years of small improvements — with 56.1 errors per page on average. Six error types account for 96% of everything detected: low-contrast text on 83.9% of pages, missing image alt text on 53.1%, missing form input labels on 51%, empty links on 46.3%, empty buttons on 30.6% and a missing document language on 13.5%. Average page complexity rose 14.3% in a single year, and the report ties the error increase directly to it.[58]

Contrast is the standout: it lost nearly five points year on year and is now the most common failure by a wide margin. A plausible reading is that alt text and `lang` improved because linters and CMS fields nag about them at authoring time, while contrast is decided by a design token that no linter sees until the page renders.[58]

## Part IX

## Generative UI: the teams doing it well are doing it boring

The "chatbot in a sidebar" is being replaced by interfaces the agent composes at runtime. But the industry has split into three patterns, and only two are defensible in production.

| Pattern | How it works | Verdict |
| --- | --- | --- |
| **Static / component-based** | The agent decides *when* a pre-built component appears and *with what data*. It never controls layout or styling. | Safe. Brand consistency and security intact. Dashboards, cards, forms, booking widgets.[29] |
| **Declarative / schema-driven** | The agent returns a **structured description** (JSON: rows, cards, lists, forms) and your frontend interprets it with its own primitives. | The pattern that scales: less backend↔render coupling and a consistent visual system across many compositions.[29,30] |
| **Open-ended / full generation** | The agent generates markup or UI code at runtime. | Fragile. **LLM-generated code running in your users' browsers.** The industry flags it as unsuitable for production.[29,30] |

> **The concrete anti-pattern.** You ask the model for a chunk of HTML, inject it into the page and call it an adaptive interface. That HTML bypasses the component system, the accessibility rules, the analytics conventions, permissions, approval workflows and the application's state model. And if the model decided a `shutdownInstances` function should exist, you now have a new attack surface. It works in the demo; it is not architecture.[30]

The pragmatic rule taking hold: **start constrained, expand with structure, embed only where the leverage is clear**. The interface can adapt to the user's goal while the system stays testable, the design system stays intact and permissions stay deterministic.[29,30]

## Part X

## Eight examples, and why they are good

These are not "the prettiest websites". They are cases where one concrete decision explains the outcome, and where the evidence is published.

### Linear

*Why: they removed the network from the user's perception, and chose that on day one.*

The database the UI reads lives **in the browser**, in IndexedDB. A mutation applies locally and reconciles over WebSocket in the background: there is no spinner because there is nothing to wait for. The co-founder wrote the sync engine as the first lines of code. The second pillar is just as deliberate: four build-pipeline rewrites (Parcel → Rollup → Vite → Rolldown) with one stated goal — ship less JavaScript and CSS.

- **Measured result:** 50% less code shipped, 30% smaller after compression, cold-cache loads 10–30% faster, time to first paint of the active-issues view down 59% on Safari, memory down 70–80%.[9]
- **Non-obvious details:** critical CSS inlined to paint the shell with no extra request; every dependency in its own chunk so bumping one does not invalidate the whole vendor bundle; and "render first, authenticate second" — paint what you have and let the first real request return a 401 if the session went stale.[9]
- **Honest trade-off:** roughly 21 MB of minified JavaScript, aggressively split into hundreds of route-level chunks. And its marketing site is static Next.js: they do not apply the same dogma to everything.[9]

### Vercel

*Why: they turned their design judgement into context any agent can load.*

A team that calls itself agent-native and proves it with artefacts rather than manifestos: a **`product-design` skill** that lives in the repository next to the code it governs (with `AGENTS.md`, `SKILL.md`, `references/` and `exemplars/`), linters that enforce the rules automatically, and a review loop that gathers evidence from Slack, Figma and GitHub and prepares guideline updates. Their rules are concrete and checkable, of the kind "destructive CTAs follow Verb + Noun, never Confirm or OK".[11]

- **`design.md`:** one public file any agent loads from a URL, built on seven real document types (usage and performance report, renewal proposal, benchmark, interactive planning page, build-versus-buy brief, security governance brief, deck) and refined over more than 200 evaluation runs with a model judge.[10]
- **Agent-friendly by default:** their blog returns markdown when you send `Accept: text/markdown`, with a hierarchical `sitemap.md` and `link rel="alternate"` as a fallback discovery path.[12]
- **Infrastructure with the same thesis:** server-side feature flags by default ("zero impact on page performance"), sandboxes to validate their own agents' patches, and customers like Gamma running AI pipelines (Tiptap inside JSDOM, in serverless functions) without reinventing release engineering.[37]

### Stripe

*Why: they are defining the protocol by which an agent spends money.*

Stripe is not adapting its site to agents: it is writing the standard. **ACP** (with OpenAI and Meta) defines agentic checkout, carts and feeds, delegated payment, delegated authentication over OAuth 2.0 and order webhooks. In September 2026 they published how they design *Checkout* for agents — using **WebMCP** to speed up purchases from the browser — and expanded **Link** (300M users, ~1M merchants) into assistants from Meta, xAI and Instinct.[14,16,13]

- **The layer holding it up:** their own data plane, a high-performance distributed proxy built because traffic passed 1.6% of global GDP and the service mesh could not cope. Stated target: 99.9995% reliability.[13]
- **Why design matters here:** when the payer is an agent, the page that decides whether something gets bought is the same one as with a human. They moved product, protocol and infrastructure at the same problem simultaneously.[13,15]

### Shopify ⇄ ChatGPT Instant Checkout

*Why: they accepted that the storefront may not be theirs.*

More than a million Shopify merchants on the path to checkout inside ChatGPT, with direct purchases already live for Etsy sellers in the US. The interesting architectural decision is not technical but about control: the **merchant stays merchant of record** — fulfilment, returns, support and the customer relationship are theirs; only the surface where the click happens changes.[15]

### Figma + Coinbase Design System

*Why: they measured that giving the agent context is cheaper than letting it improvise.*

Figma's MCP server sends the agent the file's components, styles and variables, and can also **scan your code and generate a rules file** for the system (tokens, libraries, hierarchies, naming) that acts as system-level guidance. Accessibility and interaction annotations travel with the design and land in the generated code.[21]

- **The measurement:** Coinbase — better design-system adherence and a 22.5% average cut in token cost using Code Connect.[22]
- **State of the art:** an audit of 20 open-source systems and 6 platforms logged 187 AI affordances and 157 techniques: 17 with an official MCP server, 17 with agent skills, 14 publishing `llms.txt`.[23]

### Cloudflare

*Why: they put a price on a resource nobody knew how to measure.*

AI Crawl Control turns bot traffic into a per-crawler decision — allow, charge or block — with tracking of `robots.txt` health and detection of who violates your directives. Pay Per Crawl uses `HTTP 402` plus `crawler-price` and requests signed with Web Bot Auth, with Cloudflare as merchant of record and monthly settlement through Stripe.[17,18]

- **The elegant part:** it does not break the web — it reuses existing status codes and headers, leaves `robots.txt`, `sitemap.xml`, `security.txt` and `crawlers.json` free, and never bills error responses.[17]

### Content-first sites on Astro

*Why: the best JavaScript is the JavaScript you do not ship.*

Static HTML by default, **0 KB of JavaScript** except what you explicitly mark with `client:*`, and hydration scheduled on browser signals: `visible` uses `IntersectionObserver`, `idle` uses `requestIdleCallback`. **Server Islands** let you mix edge-cached HTML with per-request fragments: a marketing page can be static for everyone while carrying a per-user fragment rendered on the fly.[27,28]

- **Careful with the benchmarks:** the comparative bundle numbers in circulation (roughly 9 KB versus several hundred) come from secondary sources and should be read as an order of magnitude, not a reproducible measurement.[28]
- **The real trap:** props are JSON-serialised across the boundary, so a `Date` arrives as a string. The JavaScript saving is paid for with discipline in the props contract.[27]

### Google Search — the counterexample

*Why it is the warning, not the model: they optimised the answer and destroyed the click.*

The most instructive case of 2026 is not a beautiful website, it is a shift in incentives. AI Overviews correlate with a **58%** reduction in click-through rate for top-ranking pages, against 34.5% measured in April 2025, and Pew found that only 8% of users click traditional results when an overview is present, versus 15% when it is not. Chartbeat, tracking more than 2,500 news sites, measured a 33% decline in Google search referrals during 2025. Penske Media filed an antitrust suit, the European Publishers Council filed a formal complaint with the Commission, and a third of surveyed publishers say they will block AI Overviews once the tools allow it.[35]

- **The causal experiment:** 1,100 US Chrome users (March 2026, UPenn + Northeastern). Hiding the overviews raised outbound clicks by **8.8 points**; forcing AI Mode cut them by **18.8 points**. News-site clicks fell 12.5 points, Reddit 21.2 and Wikipedia 9.9.[36]
- **Why it is a warning:** the traffic loss came *without* a better experience. Satisfaction, usefulness, sense of control and perceived personalisation all fell, and use of rival search engines rose 11.2 points.[36]

## Part XI

## The part conference talks leave out

Every new layer — agents, protocols, per-crawl billing — rests on the same web that AI is draining of economic incentive. The teams ahead have it in their balance sheet, not their blog.

**The structural tension:** your site must be machine-readable to exist in AI answers, and that same readability is what lets the user skip your site. It is not an optimisation problem, it is a conflict of incentives.[35,36]

**The three responses in the field:** charge for access (Pay Per Crawl);[17] design for the agent and be present where the purchase happens (ACP);[14] and raise the switching cost — a product with local data and near-zero latency is not replaced by a summary.[9]

## Part XII

## What I would do if this landed on my desk

Ordered by impact over effort. The first six are this week's work.

### Week one — decisions, not projects

- **Measure where you actually lose.** Origin-level CrUX, not Lighthouse. If you fail, it is almost certainly LCP: images, TTFB, render-blocking resources. Do not touch the event handler.[4,3]
- **Declare a per-bot policy** in `robots.txt`: search engines (always allow, or you lose the index), training bots, user agents. An explicit, versioned dial.[17]
- **Add content negotiation** — `Accept: text/markdown` → markdown — plus a hierarchical `sitemap.md`. This is the part of "machine-readable" with a real return.[12]
- **Fix the three accessibility failures everyone has:** visible focus indicator, AA contrast, meaningful `alt`. With the EAA in force, having no visibility is worse than having issues.[8,24]
- **Publish your design tokens** as a machine-consumable package, not as a Figma file.[21,23]
- **Audit your logs for agents:** what share of your traffic is GPTBot, ClaudeBot or PerplexityBot? If you do not know, you cannot decide about charging or caching.[17]

### Quarter — the structural bets

- **Choose an explicit rendering strategy** and write it down: islands for content[27], RSC for full-stack apps[2], or local-first for interactive products[9]. What does not work is cross-dogma: the same pattern for a blog, a dashboard and a collaborative editor.
- **Put a byte budget in CI.** Median mobile page: 2.56 MB with 632 KB of JavaScript. If it is not gated, it only grows.[6,8]
- **Write generative UI in constrained mode:** a component catalogue plus structured payloads. Never HTML or code generated at runtime in the user's browser.[29,30]
- **Turn design judgement into a repository artefact** (`AGENTS.md` + skill + linters + examples). It is what lets an agent write code that passes your review.[11,10]
- **Evaluate WebMCP only if you have clear task flows** (book, check status, open a ticket). Declarative on existing forms is the cheap route; it is an origin trial, so treat it as progressive enhancement.[19,20]
- **Decide your position on agentic commerce before a partner imposes it.** ACP is open: if you sell, the question is not whether an agent will try to buy, but whether your backend and your PSP can answer.[14,15]

## Sources

1. State of React 2025 — Conclusion — [2025.stateofreact.com/en-US/conclusion](https://2025.stateofreact.com/en-US/conclusion)
2. What's Next for React in 2026 (Telerik) — [telerik.com/blogs/whats-next-react-2026](https://www.telerik.com/blogs/whats-next-react-2026)
3. The State of Web Vitals — Q2 2026 — [corewebvitals.io/state-of-cwv](https://www.corewebvitals.io/state-of-cwv)
4. Core Web Vitals 2026: How You Compare to the Market — [insightland.org/blog/core-web-vitals-2026-how-you-compare-to-the-market](https://insightland.org/blog/core-web-vitals-2026-how-you-compare-to-the-market)
5. Web Almanac 2025 — Performance — [almanac.httparchive.org/en/2025/performance](https://almanac.httparchive.org/en/2025/performance)
6. Web Almanac 2025 — Page Weight — [almanac.httparchive.org/en/2025/page-weight](https://almanac.httparchive.org/en/2025/page-weight)
7. Web Almanac 2025 — Generative AI — [almanac.httparchive.org/en/2025/generative-ai](https://almanac.httparchive.org/en/2025/generative-ai)
8. HTTP Archive 2025 Web Almanac (CSS-Tricks) — [css-tricks.com/http-archive-2025-web-almanac](https://css-tricks.com/http-archive-2025-web-almanac)
9. How's Linear so fast? A technical breakdown — [performance.dev/how-is-linear-so-fast-a-technical-breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)
10. Vercel — How our agents build on-brand pages with design.md — [vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md)
11. Vercel — Teaching agents product design — [vercel.com/blog/teaching-agents-product-design-at-vercel](https://vercel.com/blog/teaching-agents-product-design-at-vercel)
12. Vercel — Making agent-friendly pages with content negotiation — [vercel.com/blog/making-agent-friendly-pages-with-content-negotiation](https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation)
13. Stripe Dot Dev — Blog — [stripe.dev/blog](https://stripe.dev/blog)
14. Stripe Docs — Agentic Commerce Protocol (ACP) — [docs.stripe.com/agentic-commerce/acp](https://docs.stripe.com/agentic-commerce/acp)
15. OpenAI — Buy it in ChatGPT: Instant Checkout and ACP — [openai.com/index/buy-it-in-chatgpt](https://openai.com/index/buy-it-in-chatgpt)
16. CeFPro — Stripe Expands Link Wallet Into Agentic AI Commerce — [connect.cefpro.com/article/view/stripe-expands-link-wallet-into-agentic-ai-commerce](https://connect.cefpro.com/article/view/stripe-expands-link-wallet-into-agentic-ai-commerce)
17. Cloudflare Docs — Pay Per Crawl — [developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl)
18. Cloudflare Blog — Introducing pay per crawl — [blog.cloudflare.com/introducing-pay-per-crawl](https://blog.cloudflare.com/introducing-pay-per-crawl)
19. Chrome for Developers — WebMCP — [developer.chrome.com/docs/ai/webmcp](https://developer.chrome.com/docs/ai/webmcp)
20. Chrome for Developers — WebMCP Declarative API — [developer.chrome.com/docs/ai/webmcp/declarative-api](https://developer.chrome.com/docs/ai/webmcp/declarative-api)
21. Figma — Design Systems and AI: Why MCP Servers Are The Unlock — [figma.com/blog/design-systems-ai-mcp](https://www.figma.com/blog/design-systems-ai-mcp)
22. Figma Blog — AI (Code Connect / Coinbase case) — [figma.com/blog/ai](https://www.figma.com/blog/ai)
23. Figmalion — Topics: Design Systems (State of AI in Design Systems, July 2026) — [figmalion.com/topics/design-systems](https://figmalion.com/topics/design-systems)
24. GetWCAG — Complete European Accessibility Act (EAA) Guide 2026 — [getwcag.com/en/what-is-european-accessibility-act-eaa](https://getwcag.com/en/what-is-european-accessibility-act-eaa)
25. W3C — WCAG 2.2 approved as ISO/IEC 40500:2025 — [w3.org/press-releases/2025/wcag22-iso-pas](https://www.w3.org/press-releases/2025/wcag22-iso-pas)
26. W3C — Web Content Accessibility Guidelines (WCAG) 2.2 — [w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22)
27. Astro Docs — Islands architecture — [docs.astro.build/en/concepts/islands](https://docs.astro.build/en/concepts/islands)
28. Astro vs Next.js 2026 (benchmarks) — [tech-insider.org/astro-vs-nextjs-2026](https://tech-insider.org/astro-vs-nextjs-2026)
29. CopilotKit — The Developer's Guide to Generative UI in 2026 — [copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026)
30. InfoWorld — A smarter, structured approach to generative UI — [infoworld.com/article/4210616/a-better-approach-to-generative-ui.html](https://www.infoworld.com/article/4210616/a-better-approach-to-generative-ui.html)
31. Rankability — llms.txt adoption research report (Sep 2026) — [rankability.com/blog/llms-txt-adoption](https://www.rankability.com/blog/llms-txt-adoption)
32. llms.txt Explained: Format, Spec, and Real Adoption Data (2026) — [ayautomate.com/blog/llms-txt](https://www.ayautomate.com/blog/llms-txt)
33. Does llms.txt Actually Work? What the 2026 Data Shows — [llms-txt.io/blog/state-of-llms-txt-2026](https://llms-txt.io/blog/state-of-llms-txt-2026)
34. State of CSS 2026 — Awards — [2026.stateofcss.com/tr-TR/awards](https://2026.stateofcss.com/tr-TR/awards)
35. TNW — Google's AI Overviews killed 58% of publisher clicks — [thenextweb.com/news/google-ai-overviews-publisher-links-search-traffic](https://thenextweb.com/news/google-ai-overviews-publisher-links-search-traffic)
36. Search Engine Land — Google AI Mode cuts clicks without boosting satisfaction — [searchengineland.com/google-ai-mode-cuts-clicks-satisfaction-study-490494](https://searchengineland.com/google-ai-mode-cuts-clicks-satisfaction-study-490494)
37. Vercel — Gamma builds design-first agents — [vercel.com/blog/gamma-builds-design-first-agents-with-vercel](https://vercel.com/blog/gamma-builds-design-first-agents-with-vercel)
38. Awwwards — Annual Awards 2025 (winners) — [awwwards.com/annual-awards-2025](https://www.awwwards.com/annual-awards-2025)
39. Awwwards — Site of the Year 2025: Lando Norris — [awwwards.com/annual-awards-2025/site-of-the-year](https://www.awwwards.com/annual-awards-2025/site-of-the-year)
40. The Webby Awards — 30th Annual Webby Awards announce 2026 winners — [webbyawards.com/press/press-releases/30th-annual-webby-awards-announce-2026-winners](https://www.webbyawards.com/press/press-releases/30th-annual-webby-awards-announce-2026-winners)
41. Webby Awards 2026 — Websites and Mobile Sites winners — [winners.webbyawards.com/winners/websites-and-mobile-sites](https://winners.webbyawards.com/winners/websites-and-mobile-sites)
42. Vercel — Geist Design System: Typography — [vercel.com/geist/typography](https://vercel.com/geist/typography)
43. Vercel — Geist Design System — [vercel.com/geist/introduction](https://vercel.com/geist/introduction)
44. Open Design — Stripe design system (DESIGN.md + preview) — [opendesigner.io/zh/design-systems/stripe](https://opendesigner.io/zh/design-systems/stripe)
45. Linear — Invisible details: building contextual menus — [linear.app/blog/invisible-details](https://linear.app/blog/invisible-details)
46. Linear — How we redesigned the Linear UI — [linear.app/now/how-we-redesigned-the-linear-ui](https://linear.app/now/how-we-redesigned-the-linear-ui)
47. The Pragmatic Engineer — Design-first software engineering: Craft — [newsletter.pragmaticengineer.com/p/design-first-software-engineering](https://newsletter.pragmaticengineer.com/p/design-first-software-engineering)
48. Details that make interfaces feel better (Jakub K.) — [jakub.kr/writing/details-that-make-interfaces-feel-better](https://jakub.kr/writing/details-that-make-interfaces-feel-better)
49. Adobe — AI in design: why taste is the true differentiator — [adobe.com/express/learn/blog/ai-in-design-recommendations](https://www.adobe.com/express/learn/blog/ai-in-design-recommendations)
50. Taste Labs — Kill the slop (taste as AI's next frontier) — [tastelabs.com/blog/kill-the-slop](https://tastelabs.com/blog/kill-the-slop)
51. Taste Is a Moat: Why AI Can't Replicate Judgment — [collinwilkins.com/articles/taste-is-a-moat](https://collinwilkins.com/articles/taste-is-a-moat)
52. Adobe Design — Taste over haste — [adobe.design/ideas/taste-over-haste](https://adobe.design/ideas/taste-over-haste)
53. Linear — New command menu (changelog) — [linear.app/changelog/2019-12-18-new-command-menu](https://linear.app/changelog/2019-12-18-new-command-menu)
54. UX Collective — The Inversion Error (taste as judgment) — [uxdesign.cc/oh-but-theres-one-more-thing-edb9fbd79c95](https://uxdesign.cc/oh-but-theres-one-more-thing-edb9fbd79c95)
55. design-engine — Vercel system analysis — [github.com/Bil0000/design/blob/main/systems/vercel/system.md](https://github.com/Bil0000/design/blob/main/systems/vercel/system.md)
56. Kousik Dutta — Motion Is Not Decoration, It Is Physics — [kousikdutta.com/journal](http://kousikdutta.com/journal)
57. Modern UI Design: A Practical Craft Guide for 2026 — [artofstyleframe.com/blog/modern-ui-design-craft-guide](https://artofstyleframe.com/blog/modern-ui-design-craft-guide)
58. WebAIM — The WebAIM Million: 2026 report on the accessibility of the top 1,000,000 home pages — [webaim.org/projects/million](https://webaim.org/projects/million)
59. design-bites — vercel.com DESIGN.md (typography, three-weight rule) — [github.com/educlopez/design-bites/blob/main/design-mds/vercel.com/DESIGN.md](https://github.com/educlopez/design-bites/blob/main/design-mds/vercel.com/DESIGN.md)

Every figure in this report is drawn from the numbered sources above. Where the industry repeats a number without a primary source (comparative framework bundle sizes, "X% of searches start on AI platforms"), it is flagged as an order of magnitude or omitted. Coverage of design-system internals for Stripe and Vercel comes from third-party system analyses except Vercel's Geist documentation, which is first-party; the award descriptions are those of the awarding bodies.
