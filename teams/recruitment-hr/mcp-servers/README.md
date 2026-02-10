# MCP Server Configurations

This directory contains MCP server configuration files for external service integrations used by the Recruitment & HR team. Each configuration defines the connection parameters, available capabilities, and required credentials for a specific service.

## Services

### Lever (Applicant Tracking System)

**Config file:** `lever.json`

Lever is the team's applicant tracking system (ATS). It manages the full hiring pipeline from job postings through offer letters.

**Capabilities:**
- `postings` -- Create, update, and manage job postings
- `candidates` -- Search, create, and manage candidate profiles
- `applications` -- Track candidate applications and pipeline stage
- `interviews` -- Schedule interviews, manage feedback, and view scorecards
- `offers` -- Create, send, and track offer packages

**Prerequisites:**
1. A Lever account with API access enabled (requires Lever Super Admin or an API-enabled role)
2. Generate an API key from Lever Settings > Integrations and API > API Credentials
3. Set the environment variable:
   ```bash
   export LEVER_API_KEY="your-lever-api-key"
   ```

**Used by:**
- **Talent Acquisition Specialist** -- Primary user. Manages postings, candidate pipeline, interview scheduling, and offer creation.
- **Coordinator** -- Read access for pipeline dashboards and hiring velocity reporting.
- **Onboarding & Enablement Manager** -- Read access to accepted candidate profiles for pre-boarding preparation.

**Rate Limits:**
- Lever enforces rate limits per API key. Standard tier allows 10 requests per second. If the team processes high candidate volumes, consider requesting a rate limit increase from Lever support.

**API Documentation:** [https://hire.lever.co/developer/documentation](https://hire.lever.co/developer/documentation)

---

### BambooHR (Human Resource Information System)

**Config file:** `bamboohr.json`

BambooHR is the team's HRIS. It serves as the system of record for employee data, time-off tracking, performance records, and organizational reporting.

**Capabilities:**
- `employees` -- Create, update, and query employee records (personal info, job details, compensation)
- `time-off` -- Manage PTO requests, balances, and policies
- `performance` -- Access performance review data, goal tracking, and assessment records
- `reports` -- Generate and retrieve standard and custom reports

**Prerequisites:**
1. A BambooHR account with API access enabled
2. Generate an API key from BambooHR > Account > API Keys
3. Identify your BambooHR subdomain (the `companyname` in `companyname.bamboohr.com`)
4. Set the environment variables:
   ```bash
   export BAMBOOHR_API_KEY="your-bamboohr-api-key"
   export BAMBOOHR_SUBDOMAIN="your-company-subdomain"
   ```

**Used by:**
- **Coordinator** -- Full access for organizational reporting, headcount analysis, and people strategy data.
- **Onboarding & Enablement Manager** -- Write access for creating new employee records and onboarding task tracking.
- **Performance Management Specialist** -- Read/write access for performance review records, goal tracking, and career ladder data.
- **Compensation & Benefits Analyst** -- Read access for compensation data, benefits enrollment, and pay equity audit data.
- **Culture & Engagement Specialist** -- Read access for engagement survey integration and team structure data.

**Rate Limits:**
- BambooHR allows up to 200 requests per minute per API key. Bulk data exports should use the reporting endpoint rather than individual record queries.

**API Documentation:** [https://documentation.bamboohr.com/reference](https://documentation.bamboohr.com/reference)

---

## Setup Checklist

Before running the Recruitment & HR team, verify the following:

- [ ] Lever account is active with API access enabled
- [ ] `LEVER_API_KEY` environment variable is set and valid
- [ ] BambooHR account is active with API access enabled
- [ ] `BAMBOOHR_API_KEY` environment variable is set and valid
- [ ] `BAMBOOHR_SUBDOMAIN` environment variable matches your BambooHR subdomain
- [ ] API keys have appropriate permission scopes for the operations each agent needs
- [ ] Rate limits have been reviewed and are sufficient for expected usage volume

## Security Notes

- Never commit API keys to version control. Use environment variables or a secrets manager.
- Rotate API keys quarterly or immediately if a compromise is suspected.
- Apply the principle of least privilege: if an agent only needs read access, do not provide write-capable credentials.
- BambooHR contains sensitive PII (Social Security numbers, addresses, compensation data). Ensure API access logs are monitored and access is audited regularly.
- Lever contains candidate PII subject to data protection regulations (GDPR, CCPA). Ensure data handling practices comply with applicable laws.

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| 401 Unauthorized | Invalid or expired API key | Regenerate the key and update the environment variable |
| 403 Forbidden | Insufficient permissions on the API key | Check the key's permission scope in the service admin panel |
| 429 Too Many Requests | Rate limit exceeded | Implement request throttling or request a rate limit increase |
| Connection timeout | Network or firewall issue | Verify outbound HTTPS access to the service URLs |
| Empty response | Incorrect subdomain (BambooHR) | Verify `BAMBOOHR_SUBDOMAIN` matches your actual subdomain |
