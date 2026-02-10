# Example: Thought Leadership Blog Series

## Scenario

A B2B SaaS company wants to establish authority in the "AI for HR" space by publishing a 6-part thought leadership blog series over 3 months.

## Project Charter Inputs

- **Company**: TalentAI (HR automation platform)
- **Audience**: HR Directors and CHROs at mid-market companies (500-5000 employees)
- **Goal**: 500 organic visits/month within 6 months, position CEO as industry voice
- **Tone**: Authoritative but accessible, data-driven, forward-looking
- **Competitor content**: Workday blog (corporate), Lattice resources (tactical)

## Team Execution

### Phase 1: Research (Coordinator + Research Specialist)
- Analyze top 50 HR tech articles by engagement
- Identify content gaps competitors aren't covering
- Map audience pain points from LinkedIn discussions and G2 reviews
- Output: Research brief with 6 topic recommendations

### Phase 2: Content Planning (Coordinator + Content Drafter)
- Define 6-part series arc: problem → landscape → solution → implementation → results → future
- Create detailed outline per article (H2s, key points, data needs)
- Plan internal linking strategy across all 6 posts
- Output: Content calendar with outlines

### Phase 3: Drafting (Content Drafter + Humanizer)
- Draft each article (1500-2000 words)
- Humanizer removes AI patterns, adds conversational elements
- Include proprietary data or unique angles per article
- Output: 6 draft articles

### Phase 4: Review (Content Critic + Fact Checker + Format Specialist)
- Critic reviews for argument strength, flow, and originality
- Fact checker verifies all statistics, quotes, and claims
- Format specialist optimizes for SEO (meta descriptions, headers, alt text)
- Output: 6 publication-ready articles with SEO metadata

## Deliverables

```
shared-workspace/artifacts/content-creation/
├── research-brief.md
├── content-calendar.md
├── blog-01-ai-hiring-crisis.md
├── blog-02-landscape-analysis.md
├── blog-03-automation-approach.md
├── blog-04-implementation-playbook.md
├── blog-05-roi-case-studies.md
├── blog-06-future-of-hr-tech.md
└── seo-metadata.md
```

## Cost Estimate

| Phase | Model Mix | Tokens | Cost |
|-------|-----------|--------|------|
| Research | Sonnet (research), Haiku (summarization) | ~120K | $12 |
| Planning | Sonnet | ~80K | $8 |
| Drafting | Opus (drafts), Sonnet (humanizing) | ~300K | $35 |
| Review | Sonnet (critique), Haiku (fact-check) | ~150K | $15 |
| **Total** | | **~650K** | **~$70** |

## Quality Metrics

- Readability: Flesch-Kincaid grade 10-12 (professional but accessible)
- Originality: <5% overlap with top 10 competing articles
- SEO: Target keyword in H1, meta description under 160 chars, 3-5 internal links
- Engagement proxy: Each article answers a specific question from audience research
