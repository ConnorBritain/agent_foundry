# Recruitment & HR Team Template

A 6-agent team for end-to-end people operations -- from defining your culture and writing job descriptions to onboarding new hires, managing performance, and designing compensation packages. This template treats people operations as a strategic function, not an administrative afterthought.

## What This Team Does

The Recruitment & HR Team operates as a full-service People department. It covers the entire employee lifecycle: attracting talent, hiring well, onboarding effectively, building culture intentionally, managing performance fairly, and compensating competitively. Each agent owns a distinct domain but collaborates through structured handoffs to ensure nothing falls through the cracks.

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| Coordinator / Head of People | Opus 4.6 | People strategy, culture design, org development |
| Talent Acquisition Specialist | Sonnet 4.5 | Job design, sourcing, interviewing, offer negotiation |
| Onboarding & Enablement Manager | Sonnet 4.5 | Day 1 through Quarter 1 plans, learning paths, buddy system |
| Culture & Engagement Specialist | Sonnet 4.5 | Values, team rituals, feedback systems, psychological safety |
| Performance Management Specialist | Sonnet 4.5 | OKRs, reviews, career ladders, succession planning |
| Compensation & Benefits Analyst | Haiku 4.5 | Salary benchmarking, equity, benefits, pay equity |

## What It Produces

- **People Strategy** -- Mission-aligned talent philosophy, hiring plan, retention strategy, org design
- **Hiring Infrastructure** -- Job descriptions, interview scorecards, sourcing playbooks, offer templates
- **Onboarding Program** -- Pre-boarding checklist, Day 1/Week 1/Month 1/Quarter 1 plans, buddy matching
- **Culture & Engagement Framework** -- Values documentation, team rituals, feedback loops, eNPS tracking
- **Performance Management System** -- OKR templates, review cycles, career ladders, calibration process
- **Compensation & Benefits Package** -- Salary bands, equity guidelines, benefits menu, total rewards statements

## Quick Start

1. **Configure your context**
   ```bash
   cp CONFIG.md my-config.md
   # Edit my-config.md with your company details
   ```

2. **Review the orchestration plan**
   ```
   See ORCHESTRATION.md for the 4-phase execution plan
   ```

3. **Deploy agents**
   ```
   See deployment-guide.md for MCP setup and phase execution
   ```

4. **Run a scenario**
   ```
   See scenarios/ for end-to-end workflow examples
   ```

## When to Use This Template

**Use it when:**
- You are building a People function from scratch (seed through Series B)
- You need to hire 5+ people in the next quarter and want a repeatable process
- Your culture is "vibes-based" and you want to operationalize it
- Performance reviews are inconsistent, unfair, or nonexistent
- You are losing people and do not understand why
- Compensation decisions are ad hoc and you suspect pay inequity
- You are scaling from 10 to 50+ people and need systems before chaos arrives

**Do not use it when:**
- You have a mature, well-functioning HR department with established processes
- You need only a single function (e.g., just compensation analysis) -- use a single-agent setup instead
- You are a solo founder with no plans to hire in the next 6 months

## Estimated Cost

| Configuration | Total Tokens | Estimated Cost |
|--------------|-------------|----------------|
| Default | ~780K | ~$78 |
| Budget | ~520K | ~$40 |
| Premium | ~1.1M | ~$130 |

See `cost-analysis.md` for a detailed phase-by-phase breakdown.

## File Structure

```
teams/recruitment-hr/
  README.md                          # This file
  TEAM_SPEC.md                       # Detailed team architecture
  MODEL_CONFIGS.md                   # Model selection and configurations
  CONFIG.md                          # Team configuration template
  ORCHESTRATION.md                   # 4-phase orchestration plan
  cost-analysis.md                   # Token usage and cost estimates
  deployment-guide.md                # Setup and deployment instructions
  agents/
    coordinator/AGENTS.md            # Head of People system prompt
    talent-acquisition/AGENTS.md     # Talent Acquisition system prompt
    onboarding-enablement/AGENTS.md  # Onboarding Manager system prompt
    culture-engagement/AGENTS.md     # Culture Specialist system prompt
    performance-management/AGENTS.md # Performance Specialist system prompt
    compensation-benefits/AGENTS.md  # Comp & Benefits system prompt
  mcp-servers/
    lever.json                       # Lever ATS integration
    bamboohr.json                    # BambooHR HRIS integration
    README.md                        # MCP server documentation
  scenarios/
    hire-to-productive.md            # End-to-end hiring scenario
    retention-intervention.md        # Flight risk detection and response
    performance-review-cycle.md      # Full review cycle scenario
  examples/
    startup-hiring-blitz.md          # Rapid hiring example
    remote-culture-building.md       # Distributed team culture example
    performance-management-framework.md  # Performance system example
```

## Key Design Decisions

1. **Coordinator uses Opus 4.6** -- People strategy requires synthesizing competing priorities, reading between the lines of organizational dynamics, and making judgment calls that affect every person in the company. This demands the strongest reasoning model.

2. **Compensation uses Haiku 4.5** -- Salary benchmarking and benefits analysis are data-heavy but structurally predictable. Haiku handles the pattern matching and calculation efficiently at lower cost.

3. **Four operational agents use Sonnet 4.5** -- Talent acquisition, onboarding, culture, and performance management all require substantial creativity and contextual judgment, but within well-defined domains. Sonnet provides the right balance of capability and cost.

4. **Sequential foundation, parallel execution** -- Phase 1 runs sequentially because culture and strategy must be defined before hiring, onboarding, or performance systems can be designed coherently. Phases 2-4 run in parallel because each agent's domain is sufficiently independent.

5. **Paranoia about mis-hires** -- The Talent Acquisition agent is explicitly designed to be skeptical. A bad hire at a 20-person company is a 5% cultural infection. The system biases toward false negatives (passing on good candidates) over false positives (hiring bad ones).

## Prerequisites

- Claude API access with Opus 4.6, Sonnet 4.5, and Haiku 4.5 models
- MCP server framework configured
- Git repository for version-controlled deliverables
- Optional: Lever/Greenhouse API access for ATS integration
- Optional: BambooHR/Gusto API access for HRIS integration
