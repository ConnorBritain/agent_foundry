# Example: Researching the AI Agent Market Landscape

## Scenario

A seed-stage startup is building an AI agent orchestration platform and needs to understand the current market landscape before finalizing its positioning and go-to-market strategy. The founding team needs defensible market sizing, a clear picture of existing players, and identification of underserved segments they can target.

## Project Charter Inputs

- **Company:** AgentForge (pre-launch AI agent orchestration startup)
- **Research Question:** What is the current size, structure, and growth trajectory of the AI agent market, and where are the biggest gaps for a new entrant?
- **Research Type:** Market/Competitive
- **Domain:** Technology (AI/ML)
- **Geographic Scope:** Global, with emphasis on North America and Europe
- **Target Audience:** Founding team and seed investors
- **Constraints:** Public data only, no proprietary databases, $40 budget

## Team Execution

### Phase 1: Research Design (Lead Researcher, ~15 min)
- Decomposes the primary question into sub-questions:
  1. How large is the AI agent market today, and what is the projected growth rate?
  2. Who are the major players and what segments do they serve?
  3. What are the primary use cases driving adoption?
  4. Where are the gaps: underserved segments, missing capabilities, unmet needs?
  5. What are the barriers to entry and competitive moats?
  6. How is the market funded: VC activity, corporate investment, open source?
- Defines success criteria: TAM/SAM/SOM with at least 2 independent sizing approaches, 10+ competitors profiled, 3+ identified market gaps
- Prioritizes sub-questions 1, 2, and 4 as highest impact for the startup's positioning decision

### Phase 2: Data Collection (Source Analyst, ~35 min)
- Searches for market sizing data from analyst firms (Gartner, IDC, CB Insights, Grand View Research)
- Gathers competitor information: product pages, pricing, Crunchbase funding data, G2 reviews
- Discovers academic papers on AI agent architectures and benchmarks (arXiv: cs.AI, cs.MA)
- Collects VC funding data: recent rounds in AI agent companies, investor thesis posts
- Finds community discussions: Reddit r/MachineLearning, Hacker News, Twitter/X AI discourse
- Documents 47 sources total: 8 analyst reports, 15 competitor data points, 12 academic papers, 7 funding reports, 5 community discussions
- Gap identified: No reliable market sizing specific to "AI agent orchestration" as a subcategory

### Phase 3: Analysis and Synthesis (Lead Researcher + Data Synthesizer + Fact Checker, ~30 min)
- Lead Researcher identifies that the market is segmented into: single-agent platforms, multi-agent orchestration, vertical-specific agents, and agent infrastructure
- Data Synthesizer builds TAM/SAM/SOM model:
  - TAM: Global AI software market ($150B by 2027, multiple sources agree within 15%)
  - SAM: AI agent and autonomous AI segment ($12-18B by 2027, 2 independent estimates)
  - SOM: Multi-agent orchestration for mid-market companies ($800M-1.2B, bottom-up estimate)
- Data Synthesizer maps 15 competitors across a positioning matrix (horizontal vs vertical, SMB vs enterprise)
- Data Synthesizer identifies 3 market gaps:
  1. No dominant multi-agent orchestration platform for non-technical users
  2. Limited solutions for regulated industries (healthcare, finance) with compliance built in
  3. Open-source agent frameworks lack production-grade monitoring and cost management
- Fact Checker verifies 23 statistical claims: 19 VERIFIED, 2 OUTDATED (pre-2025 data), 2 INACCURATE (corrected)

### Phase 4: Deliverable Production (Report Writer, ~25 min)
- Produces 18-page market analysis report with all sections
- Creates 3-page executive briefing suitable for investor conversations
- Includes TAM/SAM/SOM model with sensitivity analysis on key assumptions
- Builds competitive landscape table covering 15 players across consistent dimensions
- Documents all 47 sources with credibility assessments

## Deliverables

```
output/
  executive-summary.md                  -- 3-page standalone briefing for investors
  ai-agent-market-report.md            -- 18-page comprehensive market analysis
  tam-sam-som-model.md                 -- Market sizing with dual approach and sensitivity analysis
  competitive-landscape.md             -- 15 competitor profiles with comparison matrix
  market-gaps-analysis.md              -- 3 identified gaps with evidence and opportunity sizing
  source-database.md                   -- 47 sources with credibility tiers
  methodology-notes.md                 -- Research protocol and methodology documentation
```

## Cost Estimate

| Phase | Model Mix | Tokens | Cost |
|-------|-----------|--------|------|
| Research Design | Opus (Lead Researcher) | ~30K | $4.50 |
| Data Collection | Sonnet (Source Analyst) | ~90K | $5.40 |
| Analysis & Synthesis | Opus (Lead Researcher) + Sonnet (Data Synthesizer) + Haiku (Fact Checker) | ~120K | $8.50 |
| Deliverable Production | Sonnet (Report Writer) | ~80K | $4.80 |
| **Total** | | **~320K** | **~$23** |

## Expected Outcomes

- Founding team has a defensible market size to include in pitch deck
- Clear positioning identified: multi-agent orchestration for mid-market, non-technical users
- Investor conversations can reference specific market gaps and the startup's fit
- Competitive landscape reveals that most competitors are developer-focused, validating the no-code/low-code opportunity
- Research gaps documented: need follow-up study on customer willingness to pay and feature priorities
