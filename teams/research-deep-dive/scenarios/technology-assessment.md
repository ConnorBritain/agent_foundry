# Scenario: Evaluating Emerging Technologies for Adoption

This scenario defines the end-to-end flow for assessing an emerging technology to determine whether a company should adopt it, and if so, what the adoption roadmap should look like. The output balances technical depth with strategic business judgment.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Research Mode** | Mixed (Market + Academic) |
| **Validated After** | Phase 4 |
| **Primary Agents** | Lead Researcher, Source Analyst, Data Synthesizer, Fact Checker, Report Writer |
| **Estimated Duration** | ~90-120 minutes (hybrid mode) |
| **Estimated Cost** | ~$30-50 (default config) |

---

## Context

A technology or strategy team is evaluating whether to adopt an emerging technology (e.g., AI agents, blockchain, edge computing, quantum computing). The assessment must go beyond hype to evaluate technical maturity, real-world adoption, business value, implementation risks, and total cost of ownership. The output should support a build vs buy vs partner decision.

## Trigger

User provides a technology assessment brief specifying:
- The technology or technology category to evaluate
- The company's current tech stack and capabilities
- Specific use cases being considered
- Budget and timeline constraints for potential adoption
- Risk tolerance (early adopter vs fast follower vs laggard)

---

## Team Configuration

| Agent | Role in This Scenario |
|-------|----------------------|
| Lead Researcher | Decomposes the assessment into sub-questions: maturity, adoption landscape, use cases, risks, costs, build-vs-buy |
| Source Analyst | Discovers academic papers, industry analyses, vendor documentation, case studies, community discussions, and Gartner/Forrester reports |
| Data Synthesizer | Builds maturity assessment framework, maps adoption curve, constructs cost-benefit analysis, creates risk matrix |
| Fact Checker | Verifies vendor claims, case study outcomes, benchmark figures, and adoption statistics |
| Report Writer | Produces the technology assessment report, executive briefing, and adoption roadmap |

---

## Workflow

### Phase 1: Research Design (~15 min)
- Lead Researcher decomposes the assessment into sub-questions:
  - Technology maturity: Where is this on the adoption curve? What is production-ready vs experimental?
  - Adoption landscape: Who is using it? What results are they reporting? What are the failure cases?
  - Use case fit: How well does this technology address the company's specific use cases?
  - Implementation risks: Technical complexity, talent availability, vendor lock-in, security implications
  - Cost analysis: Total cost of ownership including implementation, maintenance, and opportunity cost
  - Build vs buy vs partner: Which approach makes sense given the company's resources and timeline?
- Defines data sources: academic papers for maturity, case studies for real-world results, vendor docs for capabilities

### Phase 2: Data Collection (~30-40 min)
- Source Analyst searches academic databases (arXiv, IEEE) for maturity and capability data
- Source Analyst searches industry sources for adoption case studies and benchmark data
- Source Analyst gathers vendor documentation, pricing, and capability claims
- Source Analyst finds community discussions (Stack Overflow, Reddit, HN) for practitioner sentiment
- Source Analyst identifies analyst reports (Gartner, Forrester) on the technology category
- Source Analyst documents what claims are vendor marketing vs independently verified

### Phase 3: Analysis and Synthesis (~25-35 min)
- Lead Researcher integrates academic and industry findings to assess true maturity level
- Data Synthesizer builds maturity assessment framework (experimental -> early adoption -> mainstream -> commodity)
- Data Synthesizer constructs risk matrix: probability x impact for key adoption risks
- Data Synthesizer creates cost-benefit analysis with explicit assumptions
- Data Synthesizer develops build vs buy vs partner decision framework
- Fact Checker verifies vendor performance claims against independent benchmarks and case studies

### Phase 4: Deliverable Production (~20-25 min)
- Report Writer produces comprehensive technology assessment report
- Report Writer creates executive briefing with adoption recommendation
- Report Writer drafts adoption roadmap with milestones and decision gates
- Lead Researcher reviews all deliverables for analytical rigor
- Coordinator performs final quality gate

---

## Expected Outputs

| Deliverable | Format | Description |
|------------|--------|-------------|
| Technology assessment report | Markdown (15-20 pages) | Comprehensive analysis: maturity, adoption, use cases, risks, costs, recommendation |
| Executive briefing | Markdown (2-3 pages) | Standalone summary with adopt/defer/reject recommendation |
| Maturity assessment | Markdown with tables | Current maturity level, readiness gaps, timeline to production readiness |
| Risk matrix | Markdown table | Key risks with probability, impact, and mitigation strategies |
| Build vs buy analysis | Markdown with tables | Cost comparison, timeline comparison, capability comparison across approaches |
| Adoption roadmap | Markdown | Phased plan with milestones, decision gates, and success criteria |
| Source database | Markdown table | All sources with credibility assessments |

---

## Estimated Cost

| Phase | Agent(s) | Est. Tokens | Est. Cost |
|-------|----------|------------|-----------|
| Research Design | Lead Researcher | ~30K | ~$4.50 |
| Data Collection | Source Analyst | ~100K | ~$6.00 |
| Analysis & Synthesis | Lead Researcher + Data Synthesizer + Fact Checker | ~120K | ~$7.50 |
| Deliverable Production | Report Writer + Lead Researcher | ~80K | ~$5.00 |
| **Total** | | **~330K** | **~$23-40** |

---

## Edge Case: Technology Is Too Early for Reliable Assessment

When the technology is so nascent that reliable data is scarce:
- Source Analyst documents the absence of production case studies and peer-reviewed evaluations
- Data Synthesizer adjusts confidence levels to reflect limited evidence
- Report Writer frames the assessment as a "technology watch" rather than an adoption recommendation
- Lead Researcher recommends a follow-up assessment timeline (e.g., re-evaluate in 6-12 months)

## Edge Case: Conflicting Vendor Claims

When vendors make performance claims that contradict each other or independent benchmarks:
- Source Analyst gathers both vendor claims and independent benchmarks
- Fact Checker verifies each claim against its methodology (benchmark conditions, test environment)
- Data Synthesizer presents reconciled view with explanation for discrepancies
- Report Writer flags unverified vendor claims separately from independently confirmed data

---

## Validation Criteria

- [ ] Maturity assessment distinguishes between vendor marketing and independent evidence
- [ ] Case studies include both successes and failures (no survivorship bias)
- [ ] Cost analysis includes total cost of ownership, not just licensing/subscription fees
- [ ] Risk matrix covers technical, organizational, and market risks
- [ ] Build vs buy analysis uses consistent criteria and realistic cost estimates
- [ ] Adoption roadmap includes decision gates where the company can pivot or stop
- [ ] Vendor claims are cross-referenced against independent benchmarks
- [ ] Limitations are documented (emerging technology data is inherently uncertain)
