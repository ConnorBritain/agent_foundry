# Scenario: Social Media Campaign

This scenario defines the flow for producing a multi-platform social media campaign with consistent messaging adapted to each platform's constraints and conventions.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Content Type** | Social media campaign (10-20 posts across platforms) |
| **Validated After** | Phase 5 |
| **Primary Agents** | Coordinator, Research Specialist, Content Drafter, Humanizer, Content Critic, Format Specialist |
| **Estimated Duration** | ~40-60 minutes (hybrid mode) |
| **Estimated Cost** | ~$15-25 (default config) |

---

## Success Path: Multi-Platform Product Announcement Campaign

### Preconditions

- Content brief specifies the announcement, target audience, and campaign goals
- Platform targets are defined (LinkedIn, X/Twitter, Instagram, etc.)
- Brand voice guidelines are configured
- Key messaging points and hashtags are provided

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Define campaign vision: core message, platform adaptations, posting cadence | Campaign brief with per-platform requirements and messaging hierarchy |
| 2 | Research Specialist | Gather supporting data: industry context, competitor campaigns, trending topics | Research brief with relevant statistics and trending angles |
| 3 | Content Drafter | Draft all posts per platform, maintaining unified messaging | 10-20 posts adapted to each platform's voice and constraints |
| 4 | Humanizer | Review all posts for AI patterns; ensure natural, platform-native voice | Revised posts that sound like a real social media manager wrote them |
| 5 | Content Critic | Check brand voice consistency across all posts | Brand compliance report across the full campaign |
| 6 | Format Specialist | Format for each platform: character limits, hashtags, mentions, media placeholders | Platform-ready posts with metadata |

### Platform-Specific Validation

| Platform | Constraint | Validated |
|----------|-----------|-----------|
| LinkedIn | Posts under 3,000 characters, professional tone | [ ] |
| X/Twitter | Posts under 280 characters, concise and punchy | [ ] |
| Instagram | Caption under 2,200 characters, hashtag strategy (20-30) | [ ] |
| Facebook | Posts under 500 words, engagement-focused | [ ] |

### Validation Criteria

- [ ] Core message is consistent across all platforms
- [ ] Each post is adapted to its platform's conventions (not copy-pasted)
- [ ] AI pattern score < 3 per 1,000 words across all posts combined
- [ ] Brand voice is consistent across all posts
- [ ] Character limits respected for each platform
- [ ] Hashtag strategy is present and relevant
- [ ] Campaign has clear calls to action

---

## Edge Case: Platform-Specific Tone Conflict

### Preconditions

- Brand voice is formal and authoritative
- Target platforms include X/Twitter (casual) and LinkedIn (professional)

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Defines tone ranges per platform within brand guidelines | LinkedIn: formal authority; X/Twitter: accessible authority |
| 2 | Content Drafter | Adapts messaging for each platform's tone range | Same core message, different expression per platform |
| 3 | Content Critic | Verifies each post stays within its platform's tone range | Compliance report per platform |

### Validation Criteria

- [ ] Core message is identical across platforms
- [ ] Tone adaptation does not distort the brand voice
- [ ] Each post feels native to its platform

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator / Editor** | Campaign strategy, messaging hierarchy, platform assignments |
| **Research Specialist** | Industry context, trending topics, competitor campaign analysis |
| **Content Drafter** | Platform-specific post drafting with unified messaging |
| **Humanizer** | Pattern elimination, platform-native voice enforcement |
| **Content Critic** | Brand consistency across all posts |
| **Format Specialist** | Platform formatting, character limits, hashtag and media metadata |
