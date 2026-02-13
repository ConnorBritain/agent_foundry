# Target Avatars

User profiles for Sforza, ordered by priority for v1. Each avatar defines who they are, what they need, which templates serve them, what they'd pay, and what makes them stay.

---

## Primary Avatar: Solo Founder / Operator

**Who**: Technical or semi-technical person building a business alone or with a tiny team. Has ideas, execution bottleneck. Currently uses Claude, ChatGPT, or Cursor for individual tasks but can't coordinate multiple workstreams.

**Pain**: "I know what I need to build but I can't do strategy, development, content, and marketing simultaneously. Each one blocks the others."

**Use case**: Build a SaaS from idea to launch. Go from business plan to market research to MVP to landing page to launch.

**Templates**: Business Builder (full), Research Brief (discovery), Campaign Planner (launch)

**Budget tolerance**: $100-500/project in orchestrator fees (separate from their Claude subscription)

**Decision frequency**: High. These users want control. They'll engage with the Decision Queue 5-10x per project run.

**Retention driver**: Template velocity. Each completed project reveals the next one. "Your Research Brief is done -- the next step is usually the Business Builder template."

**Why they stay**: The templates compound. Their first Research Brief informs their Business Builder, which feeds their Campaign Planner. Leaving means starting over.

**Acquisition channel**: Developer communities, indie hacker forums, Twitter/X, open-source awareness.

---

## Secondary Avatar: Agency Operator

**Who**: Runs a small agency (1-10 people) delivering client work. Needs to produce deliverables faster without hiring more people.

**Pain**: "I'm trading hours for dollars and I can't scale. Every new client means more hours."

**Use case**: Client deliverables at scale. Research reports, strategy decks, content calendars, competitive analyses -- templated workflows they run per client.

**Templates**: Research Brief (client discovery), Campaign Planner (client launches), Content Engine (ongoing)

**Budget tolerance**: $50-200/client engagement. They'll pass the cost through or absorb it as margin improvement.

**Decision frequency**: Medium. They'll set up the template, make high-level decisions, but want agents to handle the details.

**Retention driver**: Per-client ROI. If Sforza saves them 10 hours per client at $150/hr, $50 in orchestrator fees is a no-brainer.

**Why they stay**: It's built into their workflow. Each new client gets a Sforza project. Leaving means restructuring their entire delivery process.

**Acquisition channel**: Agency newsletters, productivity tool communities, word of mouth from other operators.

---

## Tertiary Avatar: Key Employee / New Hire

**Who**: Someone starting a new role who needs to ramp up fast. Needs a structured plan for their first 90 days, onboarding research, or a deep dive into their new industry.

**Pain**: "I need to learn everything about this company/industry/role in two weeks, not two months."

**Use case**: Structured onboarding. Industry research, competitive landscape, role-specific playbooks.

**Templates**: Research Brief, Onboarding Playbook (future template)

**Budget tolerance**: $50-100 one-time. Often expensed to employer.

**Decision frequency**: Low-medium. They want the deliverable more than the process.

**Retention driver**: Low for this use case alone. But it's an excellent top-of-funnel: they experience Sforza, then recommend it to their company or use it for their own side projects.

**Acquisition channel**: LinkedIn, professional development communities, HR/L&D recommendations.

---

## Emerging Avatar: Researcher / Analyst

**Who**: Academic, market researcher, policy analyst, or anyone who needs to synthesize large amounts of information into structured analysis.

**Pain**: "Literature reviews take weeks. Competitive analyses are tedious. I need to cover more ground faster."

**Use case**: Literature review, market analysis, policy brief, technical survey.

**Templates**: Research Brief (core), Research Deep Dive (future, multi-phase)

**Budget tolerance**: $50-150/study.

**Decision frequency**: High. They care about methodology, source selection, and analytical framing.

**Retention driver**: Quality of output. If the research is genuinely useful, they'll use it repeatedly.

**Acquisition channel**: Academic communities, research tool marketplaces, professional associations.

---

## Future Avatar: Content Creator

**Who**: YouTuber, podcaster, newsletter writer, or social media operator who needs a content pipeline.

**Pain**: "Creating content for 4 platforms simultaneously is a full-time job on top of my full-time job."

**Use case**: Multi-platform content calendar. Script writing, social posts, newsletter drafts, show notes.

**Templates**: Content Engine (future)

**Budget tolerance**: $100/month ongoing.

**Decision frequency**: Medium. They want creative control over direction but not execution details.

**Retention driver**: Ongoing need. Content creation never stops. Monthly template runs become habitual.

**Acquisition channel**: Creator communities, YouTube, podcast networks.

---

## Future Avatar: Parent / Life Planner

**Who**: Anyone planning a complex life event: wedding, move, home renovation, estate planning.

**Pain**: "This wedding has 400 tasks and I don't know what I don't know."

**Use case**: Structured planning for complex life events with research, vendor comparison, timeline management.

**Templates**: Event Coordinator, Life Planner (future)

**Budget tolerance**: $20-50 one-time. Price-sensitive but high willingness to pay for reduced stress.

**Decision frequency**: High. These are personal decisions -- they want to be involved in every choice.

**Retention driver**: Low for individual events. But life events chain: wedding to house hunting to renovation to baby planning. Template velocity across life stages.

**Acquisition channel**: Lifestyle blogs, Reddit, Pinterest, event planning communities.

---

## Avatar Selection for v1

**Optimize for**: Solo founder / operator.

**Why**: Highest willingness to pay, most complex use case (tests the full platform), broadest template needs, and most likely to generate word-of-mouth. They're building businesses -- if Sforza helps them succeed, they'll tell everyone.

**But**: The architecture must never assume this is the only user. Templates are the abstraction layer that lets one engine serve all avatars. The Research Brief template serves every single avatar above.

## Avatar Anti-Patterns

**Don't target**:
- Enterprise teams (v1 can't handle multi-human collaboration)
- Non-technical users who can't set up BYOLLM (until we have a hosted offering)
- People who want a chatbot (Sforza isn't a conversation tool, it's a work tool)
- "AI curious" tire-kickers with no specific goal (the Decision Queue requires engagement -- passive users churn)
