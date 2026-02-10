# MCP Server Configuration

This directory contains the Model Context Protocol (MCP) server configurations used by the Content Creation Team agents to interact with external services.

---

## Overview

Each JSON file defines an MCP server connection that agents use to perform operations against external APIs. The configurations specify the service endpoint, capabilities, and required credentials.

| MCP Server | Config File | Used By | Purpose |
|-----------|-------------|---------|---------|
| WordPress | `wordpress.json` | Format Specialist | Publish content, manage posts, upload media |
| Google Docs | `google-docs.json` | Format Specialist | Create and format documents for collaborative review |

The Research Specialist also uses a web search MCP server, but this is configured at the platform level (not team-specific) since multiple teams share search capabilities.

---

## Prerequisites

Before running the team, you must have accounts and API credentials for each service you plan to use. Both MCP servers are optional -- the team can output content as local Markdown files without any external publishing service.

### WordPress

**Required environment variables:**
- `WORDPRESS_URL` -- Your WordPress site URL (e.g., `https://blog.example.com`)
- `WORDPRESS_USERNAME` -- WordPress username with editor or administrator role
- `WORDPRESS_APP_PASSWORD` -- Application password for REST API access

**How to obtain:**

1. Log in to your WordPress admin panel
2. Go to **Users > Profile**
3. Scroll to **Application Passwords**
4. Enter a name (e.g., "content-creation-team") and click **Add New Application Password**
5. Copy the generated password (it will not be shown again)

**What this MCP server provides:**
- **Posts:** Create draft posts, update existing posts, publish posts
- **Media:** Upload featured images and inline media
- **Categories/Tags:** Assign categories and tags to posts
- **SEO:** Set Yoast SEO fields (meta description, focus keyword) if Yoast is installed
- **Excerpts:** Set custom excerpts

**Verification:**

```bash
# Verify WordPress REST API is accessible
curl -s "https://your-site.com/wp-json/wp/v2/posts?per_page=1" | head -c 200

# Verify authentication works
curl -s -u "username:app-password" "https://your-site.com/wp-json/wp/v2/posts?per_page=1&status=draft" | head -c 200
```

---

### Google Docs

**Required environment variables:**
- `GOOGLE_DOCS_CREDENTIALS` -- Path to a Google service account JSON key file

**How to obtain:**

1. Go to https://console.cloud.google.com
2. Create a new project (or select an existing one)
3. Enable the **Google Docs API** and **Google Drive API**
4. Go to **IAM & Admin > Service Accounts**
5. Click **Create Service Account**
6. Name it (e.g., "content-creation-team")
7. Grant the role **Editor** on the project
8. Click **Keys > Add Key > Create New Key > JSON**
9. Download the JSON file and save it securely
10. Share the target Google Drive folder with the service account email address

**What this MCP server provides:**
- **Documents:** Create new Google Docs, update content, apply formatting
- **Formatting:** Apply heading styles, bold, italic, links, lists
- **Sharing:** Set document permissions for collaborative review
- **Export:** Export documents as PDF, DOCX, or plain text

**Verification:**

```bash
# Verify the credentials file exists and is valid JSON
cat "$GOOGLE_DOCS_CREDENTIALS" | python3 -c "import json,sys; json.load(sys.stdin); print('Valid JSON')"
```

---

## Environment Variable Summary

Set all required environment variables before running the team:

```bash
# Required - Web Search (for Research Specialist)
export SEARCH_API_KEY=""                    # Brave Search or equivalent API key

# Optional - WordPress Publishing
export WORDPRESS_URL=""                     # WordPress site URL
export WORDPRESS_USERNAME=""                # WordPress username
export WORDPRESS_APP_PASSWORD=""            # Application password

# Optional - Google Docs Publishing
export GOOGLE_DOCS_CREDENTIALS=""           # Path to service account JSON
```

---

## Verification Checklist

Run this checklist before starting the team:

```bash
# 1. Web Search (Required)
echo "Search API: ${SEARCH_API_KEY:+SET}"

# 2. WordPress (Optional)
echo "WordPress URL: ${WORDPRESS_URL:+SET}"
echo "WordPress User: ${WORDPRESS_USERNAME:+SET}"
echo "WordPress Pass: ${WORDPRESS_APP_PASSWORD:+SET}"

# 3. Google Docs (Optional)
echo "Google Docs Creds: ${GOOGLE_DOCS_CREDENTIALS:+SET}"
```

The Search API key must show "SET". WordPress and Google Docs are optional depending on your target platform.

---

## Security Notes

- **Never commit credentials** to the repository. All environment variables should be set in your shell, `.env.local` (gitignored), or a secrets manager.
- **Use application passwords** for WordPress, not your main account password.
- **Scope service accounts narrowly.** The Google service account should only have access to the specific Drive folder used for content output.
- **Rotate API keys regularly.** If a key is exposed, revoke it immediately and generate a new one.
- **WordPress application passwords can be revoked** from the user profile page without affecting the main account password.
