# MCP Server Configuration

This directory contains the Model Context Protocol (MCP) server configurations used by the Research Deep Dive Team agents to interact with external data sources and search services.

---

## Overview

Each JSON file defines an MCP server connection that agents use to discover and retrieve research sources. The configurations specify the service endpoint, capabilities, and required credentials.

| MCP Server | Config File | Used By | Purpose |
|-----------|-------------|---------|---------|
| Brave Search | `brave-search.json` | Source Analyst, Fact Checker | Web source discovery, company research, news search |
| arXiv | `arxiv.json` | Source Analyst | Academic paper search, pre-print discovery, citation metadata |

Additional search capabilities (PubMed, Google Scholar, patent databases) can be configured at the platform level. The two servers above are the team-specific configurations that cover the majority of research use cases.

---

## Prerequisites

Before running the team, you must have accounts and API credentials for each search service you plan to use. The Brave Search MCP server is required for all research modes. The arXiv MCP server is optional but strongly recommended for academic and technology research.

### Brave Search (Required)

**Required environment variables:**
- `BRAVE_API_KEY` -- Brave Search API key for web and news search

**How to obtain:**

1. Go to https://brave.com/search/api/
2. Sign up for a free account (2,000 queries/month) or paid plan
3. Navigate to the API dashboard and copy your API key

**What this MCP server provides:**
- **Web search:** General source discovery across the open web
- **News search:** Recent news articles and press coverage
- **Structured results:** Titles, URLs, descriptions, and publication dates
- **Filtering:** Date range, domain inclusion/exclusion, result type

**Rate limits:**
- Free tier: 1 query/second, 2,000 queries/month
- Paid tiers: Higher limits based on plan

**Verification:**

```bash
# Verify the API key is set
echo "Brave API: ${BRAVE_API_KEY:+SET}"

# Test a search query
curl -s -H "Accept: application/json" \
  -H "X-Subscription-Token: ${BRAVE_API_KEY}" \
  "https://api.search.brave.com/res/v1/web/search?q=test&count=1" | head -c 200
```

---

### arXiv (Optional, Recommended for Academic Mode)

**Required environment variables:**
- None required (arXiv API is freely accessible)
- `ARXIV_API_KEY` -- Optional, for higher rate limits

**How to obtain:**

1. arXiv API is freely accessible at https://export.arxiv.org/api/
2. For rate limit increases, see https://info.arxiv.org/help/api/index.html
3. Default rate limit: 1 request per 3 seconds (unauthenticated)

**What this MCP server provides:**
- **Paper search:** Search across all arXiv categories (cs, stat, econ, physics, math, etc.)
- **Metadata retrieval:** Title, authors, abstract, categories, submission date, DOI
- **Full text access:** Links to PDF and HTML versions of papers
- **Citation data:** Reference lists and related papers

**Verification:**

```bash
# Test arXiv API access (no key required)
curl -s "http://export.arxiv.org/api/query?search_query=all:AI+agents&max_results=1" | head -c 500
```

---

## Mode-Specific MCP Servers

These servers are not included in this directory but can be configured at the platform level:

### Academic Mode
| Server | Purpose | Config Location |
|--------|---------|----------------|
| PubMed / NCBI | Medical and biomedical literature | Platform-level |
| Google Scholar | Broad academic search | Platform-level |
| Semantic Scholar | Citation graph and influence metrics | Platform-level |

### Market/Competitive Mode
| Server | Purpose | Config Location |
|--------|---------|----------------|
| Crunchbase | Company data and funding intelligence | Platform-level |
| SimilarWeb | Web traffic and competitive benchmarking | Platform-level |
| Google Sheets | Market sizing model output | Platform-level |

### Output Delivery (All Modes)
| Server | Purpose | Config Location |
|--------|---------|----------------|
| Google Docs | Document creation and formatting | Platform-level |
| Notion | Report creation and collaboration | Platform-level |

---

## Agent-Server Mapping

| Agent | Brave Search | arXiv | Notes |
|-------|-------------|-------|-------|
| Lead Researcher | Indirect | Indirect | Directs Source Analyst, does not search directly |
| Source Analyst | Primary | Academic mode | Executes all search queries for the team |
| Data Synthesizer | -- | -- | Works with collected findings only |
| Fact Checker | Verification | -- | Verifies source URLs and checks claim accuracy |
| Report Writer | -- | -- | Works with synthesis outputs only |

---

## Environment Variable Summary

Set all required environment variables before running the team:

```bash
# Required - Web Search (for Source Analyst)
export BRAVE_API_KEY=""                    # Brave Search API key

# Optional - Academic Mode
export ARXIV_API_KEY=""                    # arXiv API key (for higher rate limits)
export PUBMED_API_KEY=""                   # PubMed/NCBI access
export SEMANTIC_SCHOLAR_API_KEY=""         # Semantic Scholar API

# Optional - Market Mode
export CRUNCHBASE_API_KEY=""              # Crunchbase company data
export SIMILARWEB_API_KEY=""             # SimilarWeb traffic analysis

# Optional - Output Delivery
export GOOGLE_DOCS_CREDENTIALS=""         # Path to Google service account JSON
export NOTION_API_KEY=""                  # Notion integration token
```

---

## Verification Checklist

Run this checklist before starting the team:

```bash
# 1. Web Search (Required)
echo "Brave API: ${BRAVE_API_KEY:+SET}"

# 2. arXiv (Optional, recommended for academic mode)
echo "arXiv: ${ARXIV_API_KEY:-FREE_TIER}"

# 3. Market Mode Services (Optional)
echo "Crunchbase: ${CRUNCHBASE_API_KEY:+SET}"
echo "SimilarWeb: ${SIMILARWEB_API_KEY:+SET}"

# 4. Output Delivery (Optional)
echo "Google Docs: ${GOOGLE_DOCS_CREDENTIALS:+SET}"
echo "Notion: ${NOTION_API_KEY:+SET}"
```

The Brave API key must show "SET". All other keys are optional depending on your research mode and depth requirements.

---

## Security Notes

- **Never commit credentials** to the repository. All environment variables should be set in your shell, `.env.local` (gitignored), or a secrets manager.
- **Respect rate limits.** The arXiv API is rate-limited to 1 request per 3 seconds. The MCP server handles this automatically.
- **Monitor API usage.** Brave Search free tier has a 2,000 query/month limit. A typical research study uses 50-200 queries depending on depth.
- **Scope API keys narrowly.** Use read-only API keys where available. The research team does not need write access to external services.
- **Rotate API keys regularly.** If a key is exposed, revoke it immediately and generate a new one.
- **arXiv terms of use.** arXiv API access is subject to their terms of service. Do not bulk-download papers or exceed rate limits.
