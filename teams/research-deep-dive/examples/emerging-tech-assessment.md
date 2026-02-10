# Example: Assessing Web3/Blockchain Technology for E-Commerce

## Scenario

A mid-market e-commerce company ($50M ARR, 200 employees) is being asked by its board to evaluate blockchain and Web3 technologies for potential adoption. The CTO is skeptical but wants a rigorous, evidence-based assessment rather than a hype-driven or dismissal-driven answer. The research should cover real use cases, actual adoption outcomes, costs, risks, and a clear recommendation.

## Project Charter Inputs

- **Company:** ShopStream (e-commerce platform for DTC brands, $50M ARR)
- **Research Question:** Should ShopStream adopt blockchain/Web3 technologies for any part of its platform, and if so, which use cases have the strongest business case?
- **Research Type:** Mixed (Market + Academic)
- **Domain:** Technology (Blockchain/Web3 applied to E-Commerce)
- **Use Cases Under Consideration:**
  - Supply chain transparency and provenance tracking
  - Loyalty programs and tokenized rewards
  - Payment processing with cryptocurrency
  - NFT-based digital receipts or product authentication
  - Decentralized identity for customer accounts
- **Target Audience:** CTO, CEO, and board of directors
- **Constraints:** $45 budget, include both academic and industry evidence, explicit build-vs-buy analysis

## Team Execution

### Phase 1: Research Design (Lead Researcher, ~15 min)
- Decomposes the assessment into sub-questions per use case:
  1. **Supply chain provenance:** What is the maturity? Who has deployed it? What were the results? What does it cost?
  2. **Tokenized loyalty:** Are there production deployments? How do costs compare to traditional loyalty programs?
  3. **Crypto payments:** What is merchant adoption? What are conversion rates? What are regulatory requirements?
  4. **NFT authentication:** Is there consumer demand? What are the costs vs traditional authentication?
  5. **Decentralized identity:** What is the maturity? How does UX compare to traditional auth?
- Cross-cutting questions:
  - What is the real total cost of ownership (not just transaction fees)?
  - What talent is required, and what is the hiring market like?
  - What are the regulatory risks, especially for a company operating in the US and EU?
  - Which use cases have evidence of positive ROI in production?
- Defines success criteria: each use case gets an adopt/defer/reject recommendation with evidence

### Phase 2: Data Collection (Source Analyst, ~40 min)
- Academic sources (arXiv, IEEE, ACM): 14 papers on blockchain in supply chain, 8 on tokenized incentives, 5 on decentralized identity
- Industry case studies: Walmart (supply chain), Starbucks (loyalty), Shopify (crypto payments), LVMH (authentication)
- Analyst reports: Gartner Hype Cycle for Blockchain, Forrester blockchain maturity assessment, McKinsey blockchain value analysis
- Vendor documentation: 6 blockchain-as-a-service providers (AWS Managed Blockchain, Azure Blockchain, Hyperledger, Polygon, Solana, Algorand)
- Community discussions: Reddit r/CryptoCurrency, r/ecommerce, Hacker News threads, developer forums
- Regulatory sources: EU MiCA regulation, US SEC guidance, state-level crypto regulations
- Total sources: 58 (14 academic, 12 case studies, 8 analyst reports, 6 vendor docs, 10 regulatory, 8 community)
- Key finding during collection: most "success stories" are pilot programs, not production deployments at scale

### Phase 3: Analysis and Synthesis (Lead Researcher + Data Synthesizer + Fact Checker, ~35 min)
- Lead Researcher synthesizes across use cases and identifies a clear maturity gradient:
  - **Most mature:** Supply chain provenance (real production deployments, measurable ROI in food safety)
  - **Moderately mature:** Crypto payments (Shopify, BitPay integrations exist, but <2% of e-commerce transactions)
  - **Early stage:** Tokenized loyalty (Starbucks Odyssey launched then scaled back, limited evidence of superiority over traditional)
  - **Experimental:** NFT authentication (luxury brands piloting, no evidence of consumer demand in mid-market)
  - **Pre-production:** Decentralized identity (standards still evolving, UX significantly worse than traditional auth)

- Data Synthesizer builds maturity assessment table:

  | Use Case | Maturity | Production Deployments | Evidence of ROI | Recommendation |
  |----------|----------|----------------------|-----------------|----------------|
  | Supply chain provenance | Early mainstream | Walmart, Carrefour, Nestlé | Yes (food safety compliance) | DEFER -- evaluate when DTC supply chain complexity justifies cost |
  | Crypto payments | Early adoption | Shopify, Overstock | Mixed (low volume, high fraud risk) | REJECT for now -- <2% demand, regulatory uncertainty |
  | Tokenized loyalty | Experimental | Starbucks (scaled back) | No clear evidence | REJECT -- traditional loyalty programs are more cost-effective |
  | NFT authentication | Experimental | LVMH (luxury only) | No evidence for mid-market | REJECT -- no consumer demand signal outside luxury |
  | Decentralized identity | Pre-production | No production at scale | No | REJECT -- standards immature, poor UX |

- Data Synthesizer constructs cost-benefit analysis for the most promising use case (supply chain provenance):
  - Implementation cost: $200K-500K (build) vs $50K-150K/year (BaaS provider)
  - Ongoing cost: $3K-10K/month for transaction fees and node operation
  - Benefit: Compliance automation, consumer trust (hard to quantify for DTC brands)
  - Break-even: Requires $500K+ annual compliance cost savings or measurable conversion lift
  - Conclusion: Not cost-justified for ShopStream's current supply chain complexity

- Data Synthesizer builds risk matrix covering technical, regulatory, talent, and market risks
- Fact Checker verifies: 31 claims checked, 26 VERIFIED, 3 OUTDATED (updated with current data), 2 INACCURATE (Starbucks Odyssey status corrected -- program was restructured, not simply "successful")

### Phase 4: Deliverable Production (Report Writer, ~25 min)
- Produces 20-page technology assessment report with per-use-case analysis
- Creates 3-page executive briefing with clear REJECT/DEFER recommendations
- Includes maturity assessment table with evidence ratings
- Writes build-vs-buy analysis for the supply chain use case (the only DEFER)
- Documents the "re-evaluate" triggers: when should ShopStream revisit this assessment?
- Includes a 1-page "board-ready" summary that addresses the board's original question directly

## Deliverables

```
output/
  executive-briefing.md                -- 3-page summary with per-use-case recommendations
  blockchain-assessment-report.md     -- 20-page comprehensive technology assessment
  maturity-assessment.md              -- Per-use-case maturity analysis with evidence
  cost-benefit-analysis.md            -- Detailed cost analysis for supply chain provenance
  risk-matrix.md                      -- Technical, regulatory, talent, and market risks
  build-vs-buy-analysis.md            -- Supply chain provenance: build vs BaaS comparison
  re-evaluation-triggers.md           -- Conditions that should trigger reassessment
  board-summary.md                    -- 1-page board-ready answer to the original question
  source-database.md                  -- 58 sources with credibility assessments
  methodology-notes.md                -- Research protocol and methodology documentation
```

## Cost Estimate

| Phase | Model Mix | Tokens | Cost |
|-------|-----------|--------|------|
| Research Design | Opus (Lead Researcher) | ~35K | $5.25 |
| Data Collection | Sonnet (Source Analyst) | ~110K | $6.60 |
| Analysis & Synthesis | Opus (Lead Researcher) + Sonnet (Data Synthesizer) + Haiku (Fact Checker) | ~130K | $9.00 |
| Deliverable Production | Sonnet (Report Writer) | ~90K | $5.40 |
| **Total** | | **~365K** | **~$26** |

## Expected Outcomes

- CTO has evidence-based ammunition for the board conversation: "We evaluated all 5 use cases rigorously. None have a positive business case for us today."
- Board receives a credible, non-dismissive assessment that shows the team took the question seriously
- Supply chain provenance is flagged for re-evaluation if ShopStream enters regulated product categories or supply chain complexity increases significantly
- The company avoids a potentially costly blockchain pilot that industry evidence suggests would not deliver ROI
- Re-evaluation triggers are documented so the team knows when to revisit without doing ad-hoc reassessments
- Follow-up identified: if ShopStream expands into food or supplements, re-run the supply chain provenance assessment with category-specific data
