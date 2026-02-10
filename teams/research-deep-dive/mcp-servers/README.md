# MCP Server Configuration

This directory contains the Model Context Protocol (MCP) server configurations used by the Research Deep Dive Team agents to interact with external services.

---

## Overview

Each JSON file defines an MCP server connection that agents use to perform operations against external APIs. The configurations specify the service endpoint, capabilities, and required credentials.

| MCP Server | Config File | Used By | Purpose |
|-----------|-------------|---------|---------|
| Brave Search | `brave-search.json` | Primary Researcher | Web source discovery, general research queries |
| arXiv | `arxiv.json` | Primary Researcher | Academic paper search and metadata retrieval |

Additional MCP servers may be configured at the platform level (not team-specific) for services shared across teams, such as Google Docs, Notion, and Crunchbase.

---

## Prerequisites

Before running the team, you must have accounts and API credentials for each service you plan to use. The Brave Search server is required for all research modes. The arXiv server is recommended for academic mode.

### Brave Search (Required)

**Required environment variables:**
- `SEARCH_API_KEY` -- Brave Search API key for web source discovery

**How to obtain:**

1. Go to https://brave.com/search/api/
2. Sign up for a free account (2,000 queries/month on the free tier)
3. Navigate to the API section and copy your API key

**What this MCP server provides:**
- **Web search:** Full-text web search with result snippets
- **News search:** Recent news articles on the research topic
- **Filtering:** Date range filtering, domain filtering, language filtering
- **Summarization:** Search result summaries for quick relevance assessment

**Verification:**

```bash
# Verify the API key is set
echo "Search API: ${SEARCH_API_KEY:+SET}"

# Test a search query
curl -s -H "X-Subscription-Token: $SEARCH_API_KEY" \
  "https://api.search.brave.com/res/v1/web/search?q=test&count=1" | head -c 200
```

---

### arXiv (Optional, Recommended for Academic Mode)

**Required environment variables:**
- None required for basic access (arXiv API is freely accessible)
- `ARXIV_API_KEY` -- Optional, for higher rate limits

**How to obtain:**

1. arXiv API is freely accessible at https://export.arxiv.org/api/
2. For rate limit increases, see https://info.arxiv.org/help/api/index.html
3. Rate limit: 1 request per 3 seconds (default)

**What this MCP server provides:**
- **Paper search:** Search by title, author, abstract, category, date range
- **Metadata retrieval:** Title, authors, abstract, categories, DOI, publication date
- **Full text access:** Links to PDF and HTML versions of papers
- **Citation data:** Related papers and references

**Verification:**

```bash
# Test an arXiv API query (no key required)
curl -s "http://export.arxiv.org/api/query?search_query=all:machine+learning&max_results=1" | head -c 500
```

---

## Mode-Specific MCP Servers

These servers are not included in this directory but can be configured at the platform level:

### Academic Mode
| Server | Purpose | Config Location |
|--------|---------|----------------|
| PubMed / NCBI | Medical and biomedical literature | Platform-level |
| Google Scholar | Broad academic search | Platform-level |
| Zotero / Mendeley | Citation management | Platform-level |

### Market/Competitive Mode
| Server | Purpose | Config Location |
|--------|---------|----------------|
| Crunchbase | Company data and funding | Platform-level |
| SimilarWeb | Web traffic analysis | Platform-level |
| Google Sheets | Market sizing models | Platform-level |

### Product/UX Mode
| Server | Purpose | Config Location |
|--------|---------|----------------|
| Google Analytics | User behavior data | Platform-level |
| Linear | Feature backlog management | Platform-level |

### Output Delivery (All Modes)
| Server | Purpose | Config Location |
|--------|---------|----------------|
| Google Docs | Document creation and formatting | Platform-level |
| Notion | Report creation and collaboration | Platform-level |

---

## Environment Variable Summary

Set all required environment variables before running the team:

```bash
# Required - Web Search (for Primary Researcher)
export SEARCH_API_KEY=""                    # Brave Search API key

# Optional - Academic Mode
export ARXIV_API_KEY=""                     # arXiv API key (for higher rate limits)
export PUBMED_API_KEY=""                    # PubMed API key
export ZOTERO_API_KEY=""                    # Zotero citation management

# Optional - Market Mode
export CRUNCHBASE_API_KEY=""               # Crunchbase company data
export SIMILARWEB_API_KEY=""               # SimilarWeb traffic analysis

# Optional - Output Delivery
export GOOGLE_DOCS_CREDENTIALS=""          # Path to Google service account JSON
export NOTION_API_KEY=""                   # Notion integration token
```

---

## Verification Checklist

Run this checklist before starting the team:

```bash
# 1. Web Search (Required)
echo "Search API: ${SEARCH_API_KEY:+SET}"

# 2. arXiv (Optional, recommended for academic mode)
echo "arXiv: ${ARXIV_API_KEY:+SET (or using default rate limit)}"

# 3. Market Mode Services (Optional)
echo "Crunchbase: ${CRUNCHBASE_API_KEY:+SET}"
echo "SimilarWeb: ${SIMILARWEB_API_KEY:+SET}"

# 4. Output Delivery (Optional)
echo "Google Docs: ${GOOGLE_DOCS_CREDENTIALS:+SET}"
echo "Notion: ${NOTION_API_KEY:+SET}"
```

The Search API key must show "SET". All other keys are optional depending on your research mode.

---

## Security Notes

- **Never commit credentials** to the repository. All environment variables should be set in your shell, `.env.local` (gitignored), or a secrets manager.
- **Respect rate limits.** The arXiv API is rate-limited to 1 request per 3 seconds. The MCP server handles this automatically, but excessive parallel requests may be throttled.
- **Scope API keys narrowly.** Use read-only API keys where available. The research team does not need write access to external services.
- **Rotate API keys regularly.** If a key is exposed, revoke it immediately and generate a new one.
- **Monitor usage.** Brave Search free tier is limited to 2,000 queries/month. Deep research can consume significant quota.
