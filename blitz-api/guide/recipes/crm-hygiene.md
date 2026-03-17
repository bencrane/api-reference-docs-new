# CRM Hygiene Playbooks

## Overview
These automated data enrichment and cleaning workflows use BlitzAPI's Unlimited Model, enabling RevOps teams to shift from annual database maintenance to continuous hygiene processes.

## Playbook 1: Dynamic Account Enrichment

**Purpose:** Instantly enrich account records with missing contact data

### Workflow Steps

1. **Trigger:** Sales rep triggers enrichment via CRM button (Webhook/Flow)

2. **Domain Resolution:** System resolves company domain to LinkedIn URL
   ```
   POST /v2/enrichment/domain-to-linkedin
   { "domain": "stripe.com" }
   ```

3. **Contact Discovery:** Waterfall search queries to locate specific roles
   ```
   POST /v2/search/waterfall-icp-keyword
   ```

4. **Profile Enrichment:** BlitzAPI returns LinkedIn profile, which feeds enrichment endpoints for verified contact details

5. **CRM Update:** Automation creates and assigns contact in CRM

### Flow Diagram
```
CRM Button Click
    ↓
Domain → LinkedIn URL
    ↓
Waterfall ICP Search
    ↓
Email/Phone Enrichment
    ↓
Create Contact in CRM
```

## Playbook 2: Pre-Send Email Validation

**Purpose:** Filter risky emails before cold email campaigns launch

### Workflow Steps

1. **Export:** Export lead list via automation platform

2. **Validate:** Validate each email using SMTP checks
   ```
   POST /v2/utilities/email/validate
   ```
   Checks include: syntax, DNS, SMTP handshake

3. **Route:** Based on validation results:
   - **Valid:** Add to outreach sequence
   - **Invalid/Risky:** Move to "Do Not Contact" status

### Validation Response
```json
{
  "email": "john@acme.com",
  "valid": true,
  "deliverable": true,
  "catch_all": false,
  "disposable": false
}
```

## Key Technical Components

| Component | Description |
|-----------|-------------|
| **API Endpoints** | Domain-to-LinkedIn, Waterfall Search, Email Validation |
| **Compatible Platforms** | n8n, Make, Clay |
| **Advantage** | Unlimited-plan scaling without credit limitations |

## Implementation Tips

1. **Start with high-value accounts** - Focus on strategic accounts first
2. **Set up error handling** - Catch API failures gracefully
3. **Log all enrichments** - Track what data was added/updated
4. **Schedule regular runs** - Weekly hygiene passes work well

## Resources
- Documentation index: https://docs.blitz-api.ai/llms.txt
- API dashboard: https://app.blitz-api.ai
