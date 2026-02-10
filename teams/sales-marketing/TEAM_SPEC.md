# Sales & Marketing Team Specification

## Team Architecture Overview

The Sales & Marketing team is a 7-agent system designed for complete go-to-market execution. The architecture follows a hub-and-spoke model: one strategic coordinator orchestrates six specialist agents, each responsible for a distinct domain within the revenue generation lifecycle.

The team operates in four sequential phases, with heavy parallelism within phases 2 and 3. This structure mirrors how high-performing marketing organizations work: strategy sets direction, specialists build in parallel, execution generates data, and analysis drives iteration.

---

## Team Composition

### 1. Coordinator / VP Marketing (1x Opus 4.6)

**Role**: Strategic leader and orchestrator for the entire go-to-market operation.

**Responsibilities**:
- Define GTM strategy including target segments, positioning, and competitive differentiation
- Orchestrate agent workflows, resolve conflicts, and ensure alignment across all functions
- Own the marketing budget and allocate spend across channels based on performance data
- Drive campaign planning with clear objectives, timelines, and success criteria
- Obsess over unit economics: CAC, LTV, payback period, and marginal returns by channel
- Build attribution frameworks that connect marketing activities to revenue outcomes
- Make resource allocation decisions based on data, not intuition
- Conduct cross-functional reviews to ensure sales, marketing, and success are aligned

**Why Opus 4.6**: Strategic planning, cross-functional coordination, and complex tradeoff decisions (budget allocation, channel mix optimization) require the strongest reasoning capabilities. The coordinator must synthesize inputs from all specialists and make high-stakes decisions that affect the entire team's output.

**Key Outputs**:
- GTM strategy document
- Marketing budget allocation
- Campaign briefs and objectives
- Cross-functional alignment documents
- Quarterly planning recommendations

---

### 2. Demand Generation Specialist (1x Sonnet 4.5)

**Role**: Growth marketer responsible for filling the top of the funnel with qualified leads.

**Responsibilities**:
- Design and manage paid advertising campaigns across Google Ads, Meta Ads, and LinkedIn Ads
- Build SEO/SEM strategy including keyword research, content optimization, and technical SEO recommendations
- Create landing pages, ad creative, and conversion-optimized funnels
- Implement lead scoring criteria in collaboration with the Pipeline Manager
- Run systematic A/B tests on every element: headlines, CTAs, landing pages, ad creative, audiences
- Maintain strict budget discipline with daily spend monitoring and automatic pause rules
- Optimize for cost per qualified lead (CPQL), not vanity metrics like impressions or clicks
- Design and execute email nurture sequences for leads not yet sales-ready

**Key Outputs**:
- Campaign briefs with targeting, creative, and budget specifications
- Landing page wireframes and copy
- Ad creative variations for testing
- Email nurture sequences
- SEO content briefs and keyword maps
- Weekly performance reports with optimization recommendations

---

### 3. Sales Enablement Manager (1x Sonnet 4.5)

**Role**: Empowers the sales team with tools, content, and training to close deals effectively.

**Responsibilities**:
- Create pitch decks that tell compelling stories, not feature dumps
- Build battle cards for every major competitor with positioning, weaknesses, and handling strategies
- Write demo scripts that focus on customer problems and value delivery
- Develop ROI calculators and business case templates for enterprise deals
- Create objection handling guides organized by objection category and buyer persona
- Design sales training curricula for new hire onboarding and ongoing skill development
- Build email templates and sequences for outbound prospecting
- Maintain a content library organized by funnel stage, persona, and use case

**Key Outputs**:
- Pitch deck (master version + persona-specific variants)
- Competitive battle cards
- Demo scripts with branching paths based on persona
- ROI calculator / business case template
- Objection handling playbook
- Sales email templates and sequences
- New hire sales onboarding guide

---

### 4. Pipeline Manager (1x Sonnet 4.5)

**Role**: Owns the health and velocity of the sales pipeline from MQL through closed-won.

**Responsibilities**:
- Define pipeline stages with clear entry/exit criteria and required activities
- Ensure CRM hygiene: complete records, accurate stages, timely updates, proper tagging
- Track deal velocity metrics: time in stage, conversion rates, average deal size, win rate
- Build forecasting methodology and improve forecast accuracy over time
- Coach on stuck deals: identify blockers, suggest next actions, escalate when needed
- Design and run pipeline review cadences (weekly, monthly, quarterly)
- Create pipeline reports and dashboards for leadership visibility
- Implement automated alerts for deals that are stale, at risk, or missing information

**Key Outputs**:
- Pipeline stage definitions with entry/exit criteria
- CRM configuration specifications
- Forecast methodology and templates
- Pipeline review cadence and agenda templates
- Deal scoring model
- Automated alert rules
- Pipeline health dashboard specifications

---

### 5. Customer Success Manager (1x Sonnet 4.5)

**Role**: Owns the post-sale customer journey from onboarding through expansion.

**Responsibilities**:
- Design onboarding sequences that drive time-to-first-value under 7 days
- Build customer health scoring models using product usage, engagement, and support data
- Create expansion and upsell playbooks triggered by usage milestones and health indicators
- Develop churn prevention workflows with early warning signals and intervention strategies
- Design and run Quarterly Business Reviews (QBRs) with templates and preparation guides
- Build customer segmentation models for resource allocation (high-touch, mid-touch, tech-touch)
- Create customer advocacy programs: case studies, references, reviews, community
- Track and improve NPS, CSAT, and customer effort scores

**Key Outputs**:
- Onboarding playbook with day-by-day sequences
- Customer health scoring model
- Expansion/upsell playbook with triggers and talk tracks
- Churn prevention workflow
- QBR template and preparation guide
- Customer segmentation framework
- Advocacy program design

---

### 6. Growth Analyst (1x Sonnet 4.5)

**Role**: Data analyst who transforms marketing and sales data into actionable insights.

**Responsibilities**:
- Build multi-touch attribution models that fairly credit marketing touchpoints
- Run cohort analysis to understand customer behavior, retention, and LTV by segment
- Design and analyze A/B tests with proper statistical rigor (sample sizes, significance, power)
- Calculate and track CAC, LTV, payback period, and unit economics by channel and segment
- Monitor channel performance and identify when channels are saturating or underperforming
- Create dashboards that tell stories, not just display numbers
- Find leverage points: the 20% of activities driving 80% of results
- Provide data-backed recommendations for budget reallocation and strategy shifts

**Key Outputs**:
- Attribution model specification and implementation guide
- Cohort analysis reports
- A/B test designs with hypothesis, metrics, sample size, and duration
- CAC/LTV calculations by channel, segment, and cohort
- Channel performance dashboards
- Experiment results with statistical analysis
- Budget reallocation recommendations with expected impact

---

### 7. Brand & Messaging Specialist (1x Haiku 4.5)

**Role**: Ensures clarity, consistency, and resonance across all customer-facing communications.

**Responsibilities**:
- Define brand positioning: who you are, who you serve, why you are different, why it matters
- Create the messaging hierarchy: tagline, value propositions, proof points, feature-benefit mapping
- Translate features into benefits and benefits into outcomes that customers care about
- Ensure messaging consistency across all channels, agents, and touchpoints
- Develop persona-specific messaging variants that speak to each buyer's priorities
- Create brand voice and tone guidelines
- Review and refine all customer-facing content for clarity and persuasiveness
- Build a messaging library that all agents reference for consistency

**Why Haiku 4.5**: Messaging tasks are well-scoped, pattern-based (feature-to-benefit translation, consistency checks), and high-volume. Haiku provides excellent quality for these structured creative tasks at significantly lower cost.

**Key Outputs**:
- Brand positioning statement
- Messaging hierarchy document
- Value proposition framework (per persona)
- Feature-benefit-outcome mapping
- Brand voice and tone guidelines
- Messaging library / reference document

---

## Team Deliverables Summary

### Strategy Layer
| Deliverable | Owner | Collaborators |
|------------|-------|---------------|
| GTM Strategy | Coordinator | All agents |
| Target Persona Profiles | Coordinator | Brand & Messaging |
| Competitive Analysis | Coordinator | Sales Enablement |
| Marketing Budget Allocation | Coordinator | Growth Analyst |

### Demand Generation Layer
| Deliverable | Owner | Collaborators |
|------------|-------|---------------|
| Campaign Designs | Demand Generation | Coordinator, Brand & Messaging |
| Landing Pages & Funnels | Demand Generation | Brand & Messaging |
| SEO/SEM Strategy | Demand Generation | Growth Analyst |
| Email Nurture Sequences | Demand Generation | Brand & Messaging |
| Ad Creative & Copy | Demand Generation | Brand & Messaging |

### Sales Enablement Layer
| Deliverable | Owner | Collaborators |
|------------|-------|---------------|
| Pitch Deck | Sales Enablement | Brand & Messaging, Coordinator |
| Battle Cards | Sales Enablement | Coordinator |
| Demo Scripts | Sales Enablement | Brand & Messaging |
| ROI Calculator | Sales Enablement | Growth Analyst |
| Objection Handling Guide | Sales Enablement | Pipeline Manager |

### Pipeline & CRM Layer
| Deliverable | Owner | Collaborators |
|------------|-------|---------------|
| CRM Configuration | Pipeline Manager | Growth Analyst |
| Stage Definitions | Pipeline Manager | Sales Enablement |
| Forecast Methodology | Pipeline Manager | Growth Analyst |
| Pipeline Dashboards | Pipeline Manager | Growth Analyst |
| Deal Scoring Model | Pipeline Manager | Growth Analyst |

### Customer Success Layer
| Deliverable | Owner | Collaborators |
|------------|-------|---------------|
| Onboarding Playbook | Customer Success | Sales Enablement |
| Health Scoring Model | Customer Success | Growth Analyst |
| Expansion Playbook | Customer Success | Pipeline Manager |
| Churn Prevention Workflow | Customer Success | Growth Analyst |
| QBR Templates | Customer Success | Coordinator |

### Analytics Layer
| Deliverable | Owner | Collaborators |
|------------|-------|---------------|
| Attribution Model | Growth Analyst | Coordinator, Demand Generation |
| Cohort Analysis | Growth Analyst | Customer Success |
| Channel Performance Dashboard | Growth Analyst | Demand Generation |
| Experiment Framework | Growth Analyst | Demand Generation |
| Unit Economics Report | Growth Analyst | Coordinator |

---

## Inter-Agent Communication

### Data Flow

```
Brand & Messaging ──→ [Messaging Library] ──→ All Agents
                                                  │
Coordinator ──→ [Strategy Brief] ──→ All Agents   │
                                                   │
Demand Gen ──→ [Lead Data] ──→ Pipeline Manager    │
                                  │                │
Pipeline Manager ──→ [Deal Data] ──→ Growth Analyst
                                  │
Customer Success ──→ [Health Data] ──→ Growth Analyst
                                       │
Growth Analyst ──→ [Insights] ──→ Coordinator ──→ All Agents
```

### Shared Artifacts

All agents read from and write to a shared workspace with the following structure:

```
workspace/
├── strategy/
│   ├── gtm-strategy.md
│   ├── personas/
│   ├── competitive-analysis.md
│   └── budget-allocation.md
├── messaging/
│   ├── positioning.md
│   ├── value-props.md
│   ├── messaging-hierarchy.md
│   └── brand-voice.md
├── demand-gen/
│   ├── campaigns/
│   ├── landing-pages/
│   ├── email-sequences/
│   └── seo-strategy.md
├── sales-enablement/
│   ├── pitch-deck.md
│   ├── battle-cards/
│   ├── demo-scripts/
│   ├── roi-calculator.md
│   └── objection-handling.md
├── pipeline/
│   ├── stage-definitions.md
│   ├── crm-config.md
│   ├── forecast-methodology.md
│   └── scoring-model.md
├── customer-success/
│   ├── onboarding-playbook.md
│   ├── health-scoring.md
│   ├── expansion-playbook.md
│   ├── churn-prevention.md
│   └── qbr-template.md
└── analytics/
    ├── attribution-model.md
    ├── dashboards/
    ├── experiments/
    └── unit-economics.md
```

### Conflict Resolution

When agents produce conflicting recommendations (e.g., demand gen wants aggressive spend while the analyst shows diminishing returns), the Coordinator resolves by:

1. Reviewing the data from both agents
2. Applying the strategic framework (CAC target, payback period constraint)
3. Making a decision with documented rationale
4. Communicating the decision and reasoning to all affected agents

---

## Quality Gates

Each phase has quality gates that must pass before the team proceeds:

### Phase 1 Gates
- [ ] GTM strategy covers all required sections (market, personas, positioning, channels, metrics)
- [ ] Messaging framework is internally consistent and persona-specific
- [ ] Analytics plan covers attribution, KPIs, and dashboard requirements
- [ ] Budget allocation sums to total budget with channel-level justification

### Phase 2 Gates
- [ ] Campaign designs include targeting, creative, budget, and success criteria
- [ ] Sales enablement materials cover all personas and competitive scenarios
- [ ] CRM stages have clear entry/exit criteria and required activities
- [ ] Onboarding sequence has day-by-day timeline with success milestones

### Phase 3 Gates
- [ ] All campaigns have A/B test variants and statistical plans
- [ ] Pipeline reports show real-time accuracy within 10% of actuals
- [ ] Customer health scores correlate with actual churn/expansion outcomes
- [ ] Dashboards answer the top 10 questions leadership asks

### Phase 4 Gates
- [ ] Analysis includes statistical significance for all test results
- [ ] Budget recommendations are backed by marginal CAC analysis
- [ ] All playbooks are updated with learnings from execution
- [ ] Next cycle strategy reflects data-driven insights, not assumptions
