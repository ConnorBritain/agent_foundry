# MCP Server Configurations

This directory contains Model Context Protocol (MCP) server configurations for the external services used by the Sales & Marketing agent team. Each JSON file defines a connection to a specific platform, including its capabilities, required credentials, and API documentation.

---

## Prerequisites

Before any agent can interact with these services, the following must be completed:

1. **Accounts**: Active accounts on each platform with API access enabled
2. **Environment variables**: All required environment variables set in the execution environment
3. **API permissions**: Sufficient permissions granted to the API keys/tokens for the operations the agents will perform
4. **Rate limits**: Awareness of each platform's rate limits to avoid throttling during execution

---

## HubSpot

**Config file**: `hubspot.json`

**What it provides**: CRM data access including contacts, companies, deals, marketing campaigns, and analytics. This is the primary system of record for the Pipeline Manager and a key data source for the Growth Analyst.

**Required environment variables**:

| Variable | Description | How to obtain |
|----------|-------------|---------------|
| `HUBSPOT_API_KEY` | Private app access token for the HubSpot API | HubSpot account > Settings > Integrations > Private Apps > Create a private app. Grant scopes: `crm.objects.contacts.read`, `crm.objects.contacts.write`, `crm.objects.deals.read`, `crm.objects.deals.write`, `crm.objects.companies.read`, `marketing.campaigns.read`, `analytics.read` |

**Capabilities used by agents**:

| Capability | Used By | Purpose |
|------------|---------|---------|
| `contacts` | Pipeline Manager, Demand Generation | Create, read, and update contact records; manage lead scoring properties |
| `deals` | Pipeline Manager, Growth Analyst | Track deal stages, values, and velocity; generate forecasts |
| `companies` | Pipeline Manager, Customer Success | Associate contacts to accounts; track account-level health |
| `campaigns` | Demand Generation, Growth Analyst | Track campaign performance; associate contacts with campaigns |
| `analytics` | Growth Analyst, Coordinator | Pull funnel metrics, conversion rates, and attribution data |

**Setup steps**:
1. Log in to HubSpot and navigate to Settings > Integrations > Private Apps
2. Create a new private app with the scopes listed above
3. Copy the access token and set it as `HUBSPOT_API_KEY` in your environment
4. Verify access by running: `curl -H "Authorization: Bearer $HUBSPOT_API_KEY" https://api.hubspot.com/crm/v3/objects/contacts?limit=1`

---

## Google Ads

**Config file**: `google-ads.json`

**What it provides**: Paid search campaign management including campaign creation, ad group configuration, keyword management, and performance reporting. This is the primary tool for the Demand Generation Specialist's search campaigns.

**Required environment variables**:

| Variable | Description | How to obtain |
|----------|-------------|---------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Developer token for Google Ads API access | Google Ads account > Tools & Settings > API Center > Apply for developer token. Production access requires Basic or Standard tier approval. |
| `GOOGLE_ADS_CUSTOMER_ID` | The Google Ads customer ID (without dashes) | Google Ads account > top-right corner shows the customer ID in format XXX-XXX-XXXX. Remove dashes for the environment variable. |

**Capabilities used by agents**:

| Capability | Used By | Purpose |
|------------|---------|---------|
| `campaigns` | Demand Generation | Create and manage search, display, and remarketing campaigns |
| `ad-groups` | Demand Generation | Organize ads by theme and targeting within campaigns |
| `keywords` | Demand Generation | Manage keyword lists, match types, and negative keywords |
| `performance` | Growth Analyst, Demand Generation | Pull impression, click, conversion, and cost data for analysis |

**Setup steps**:
1. Ensure you have a Google Ads account with active billing
2. Navigate to Tools & Settings > API Center and apply for a developer token
3. For testing, use the test account developer token (limited functionality)
4. For production, apply for Basic access (requires approval, typically 1-3 business days)
5. Set `GOOGLE_ADS_DEVELOPER_TOKEN` and `GOOGLE_ADS_CUSTOMER_ID` in your environment
6. If using a manager account (MCC), set the customer ID to the MCC account and specify client customer IDs in requests

**Additional authentication**: Google Ads API also requires OAuth 2.0 credentials. Set up a Google Cloud project with the Google Ads API enabled, create OAuth credentials, and complete the OAuth flow to obtain refresh tokens. Store these as `GOOGLE_ADS_CLIENT_ID`, `GOOGLE_ADS_CLIENT_SECRET`, and `GOOGLE_ADS_REFRESH_TOKEN`.

---

## LinkedIn Ads

**Config file**: `linkedin-ads.json`

**What it provides**: B2B advertising campaign management including campaign creation, creative management, and performance analytics. This is a primary channel for the Demand Generation Specialist when targeting by job title, company, and industry.

**Required environment variables**:

| Variable | Description | How to obtain |
|----------|-------------|---------------|
| `LINKEDIN_ACCESS_TOKEN` | OAuth 2.0 access token for the LinkedIn Marketing API | LinkedIn Developer Portal > Create an app > Request access to Marketing API program > Complete OAuth 2.0 flow to obtain token. Tokens expire every 60 days and must be refreshed. |

**Capabilities used by agents**:

| Capability | Used By | Purpose |
|------------|---------|---------|
| `campaigns` | Demand Generation | Create and manage sponsored content, message ads, and text ads campaigns |
| `creatives` | Demand Generation | Upload and manage ad creatives (images, carousel cards, video) |
| `analytics` | Growth Analyst, Demand Generation | Pull impression, click, conversion, lead, and cost data |

**Setup steps**:
1. Create a LinkedIn Developer application at https://www.linkedin.com/developers/
2. Request access to the Marketing API program (requires a LinkedIn Campaign Manager account)
3. Add the following OAuth scopes: `r_ads`, `r_ads_reporting`, `rw_ads`, `r_organization_social`
4. Complete the OAuth 2.0 three-legged flow to obtain an access token
5. Set `LINKEDIN_ACCESS_TOKEN` in your environment
6. Note: LinkedIn access tokens expire every 60 days. Implement token refresh logic or manually rotate tokens on a schedule.

**Important notes**:
- LinkedIn Marketing API access requires approval and may take several business days
- Rate limits are stricter than other platforms (approximately 100 requests per day for some endpoints)
- Campaign Manager account must have an active ad account with billing configured
- For testing, use LinkedIn's sandbox environment before pointing at production data

---

## Adding New Services

To add a new MCP server configuration:

1. Create a new JSON file in this directory following the naming convention: `service-name.json`
2. Use this schema:

```json
{
  "name": "service-name",
  "type": "rest",
  "url": "https://api.example.com",
  "capabilities": ["capability-1", "capability-2"],
  "required_env": ["ENV_VAR_1", "ENV_VAR_2"],
  "documentation": "https://docs.example.com/api"
}
```

3. Update this README with setup instructions, required permissions, and which agents use the service
4. Add the environment variables to your execution environment before running the agent team

---

## Security Notes

- Never commit API keys, tokens, or secrets to version control
- Use environment variables or a secrets manager for all credentials
- Rotate tokens on the schedule recommended by each platform (LinkedIn: 60 days)
- Grant minimum required permissions -- do not use admin-level API keys when read-only access suffices
- Audit API access logs periodically to verify agents are only accessing expected endpoints
- When running in CI/CD, use pipeline-level secrets rather than repository-level secrets
