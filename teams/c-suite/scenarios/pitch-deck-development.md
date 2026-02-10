# Scenario: Developing an Investor Pitch Deck with Supporting Materials

## Context

A startup needs to create a compelling investor pitch deck backed by rigorous supporting materials. The deck must tell a coherent story from problem to solution to market to traction to team to ask. This scenario produces both the slide-by-slide content and the supporting data that allows founders to answer deep-dive questions in investor meetings.

## Trigger

The user is preparing for investor meetings and needs:
- A 10-12 slide pitch deck with content and speaker notes
- Supporting materials for due diligence questions
- Financial summary that matches the full model
- Competitive positioning that can withstand investor scrutiny

CONFIG.local.md specifies `pitch_deck: true` with fundraising details.

## Team Configuration

| Agent | Role in Scenario | Priority |
|-------|-----------------|----------|
| CEO / Strategy Lead | Owns the narrative arc, writes executive summary, crafts the ask | Primary |
| CFO / Finance | Provides financial slides (metrics, projections, use of proceeds) | Primary |
| CMO / Marketing | Provides market slides (TAM/SAM/SOM, competitive landscape, positioning) | Primary |
| CTO / Product | Provides product slides (solution, demo flow, roadmap) | Supporting |
| VP Sales | Provides business model slides (pricing, revenue model, traction) | Supporting |
| COO / Operations | Provides team slide (org, hiring plan, key hires) | Supporting |
| General Counsel | Reviews claims for accuracy, flags legal risks in deck language | Minimal |

## Workflow

### Phase 1: Narrative Design (~10 min)
- CEO defines the pitch narrative arc: what is the one story this deck tells?
- CEO identifies the 3 strongest proof points (market data, traction, team)
- CEO outlines the slide structure (10-12 slides)
- CEO assigns each specialist their slide content responsibilities

### Phase 2: Content Creation (~25-35 min, parallel)
- CMO produces market analysis content:
  - TAM/SAM/SOM with bottom-up methodology and visual format
  - Competitive landscape positioning map
  - Customer pain point data with quotes or statistics
- CFO produces financial content:
  - 3 key financial metrics for the financials slide
  - Use of proceeds breakdown (pie chart format)
  - Revenue projection summary (chart format)
  - Unit economics highlights (CAC, LTV, LTV:CAC)
- CTO produces product content:
  - Solution description with key feature highlights
  - Demo flow outline (screenshot placeholders with captions)
  - Technology differentiation summary
- VP Sales produces business model content:
  - Revenue model explanation (how the business makes money)
  - Pricing tier summary
  - Pipeline or traction metrics
- COO produces team content:
  - Founder backgrounds (relevant experience, not resumes)
  - Key advisors and their contributions
  - Planned hires and what they unlock

### Phase 3: Narrative Integration (~15 min)
- CEO assembles all content into the pitch narrative
- CEO ensures each slide answers one question and advances the story
- CEO resolves any inconsistencies between slides (numbers, messaging, positioning)
- CEO writes speaker notes for each slide (what to say, not what is on the slide)
- CEO crafts "The Ask" slide: amount, use of proceeds, milestones it unlocks

### Phase 4: Review and Stress Testing (~10 min)
- All specialists review the assembled deck from their domain
- CFO verifies all numbers match the financial model
- CMO verifies market claims are defensible
- General Counsel flags any claims that could create legal exposure
- VP Sales confirms business model description matches the sales strategy
- Team identifies the 5 hardest questions investors will ask and drafts answers

### Phase 5: Final Polish (~5 min)
- CEO locks the deck content and speaker notes
- CEO produces an investor FAQ document (10-15 anticipated questions with answers)
- CEO creates a one-page executive summary for email introductions

### Phase 6: Artifact Generation (~15 min)
- CEO produces pitch deck content in Google Slides (or markdown outline)
- CEO produces executive summary as standalone document
- CEO produces investor FAQ
- CFO produces supporting financial summary one-pager

## Expected Outputs

- Pitch deck content (10-12 slides with speaker notes):
  - Cover: company name, tagline, logo placeholder
  - Problem: market pain with data points
  - Solution: product description and key value proposition
  - Product: demo flow with screenshot placeholders
  - Market: TAM/SAM/SOM with methodology
  - Business Model: revenue model, pricing, unit economics
  - Traction: milestones achieved or planned
  - Competition: positioning map with differentiation
  - Team: founder backgrounds and key hires
  - Financials: 3 key metrics and revenue projection
  - The Ask: amount, use of proceeds, milestones
- Executive summary (1-page, for email introductions)
- Investor FAQ (10-15 questions with prepared answers)
- Financial summary one-pager (key metrics backing the deck)

## Estimated Cost

| Phase | Agents | Est. Tokens | Est. Cost |
|-------|--------|-------------|-----------|
| Narrative Design | 1 (CEO) | ~25K | ~$3.75 |
| Content Creation | 5-6 parallel | ~200K | ~$14.00 |
| Narrative Integration | 1 (CEO) | ~50K | ~$7.50 |
| Review / Stress Testing | 6-7 parallel | ~60K | ~$5.50 |
| Final Polish | 1 (CEO) | ~20K | ~$3.00 |
| Artifact Generation | 3-4 | ~45K | ~$4.50 |
| **Total** | | **~400K** | **~$38.25** |

Add 20% buffer: **~$46 effective total**.

## Investor Question Preparation

The team prepares answers for these common investor challenges:
- "Why now? What has changed that makes this the right time?"
- "How do you know customers will pay for this?"
- "What happens if [biggest competitor] builds this feature?"
- "Walk me through your unit economics."
- "How did you arrive at your market size?"
- "What is your unfair advantage?"
- "How will you use the money and what milestones will it achieve?"
- "What is the biggest risk to this business?"
- "Why is this team the right team to build this?"
- "What does your pipeline look like today?"
