# Account Breakthrough Recipe

## Overview
This workflow automates the process of identifying and engaging key decision-makers within target accounts using BlitzAPI's data enrichment capabilities.

## Core Challenge & Solution

**Problem:** Manual prospecting across 500 strategic accounts is inefficient.

**Solution:** Automate the entire breakthrough process. Identify the buying committee, verify their data, and enroll them in sequences—instantly.

## Technology Stack

| Component | Tool |
|-----------|------|
| Orchestrator | n8n or Make |
| Data Engine | BlitzAPI (Waterfall ICP + Validation) |
| CRM | HubSpot/Salesforce |
| Execution | Smartlead/Lemlist |

## Workflow Steps

### Step 0: Domain Resolution (if needed)
If you only have company domains, resolve them to LinkedIn URLs:

```json
POST /v2/enrichment/domain-to-linkedin
{
  "domain": "stripe.com"
}
```

**Response:**
```json
{
  "found": true,
  "company_linkedin_url": "https://www.linkedin.com/company/stripe"
}
```

### Step 1: Pull Target Accounts
Extract accounts from CRM via API or export.

### Step 2: Execute Contact Discovery
Use tiered contact discovery (C-Level → Directors → Managers):

```json
POST /v2/search/waterfall-icp-keyword
{
  "company_linkedin_url": "https://www.linkedin.com/company/stripe",
  "cascade": [
    {
      "include_title": ["CFO", "VP Finance", "Chief Financial Officer"],
      "exclude_title": ["assistant", "intern"],
      "location": ["US"],
      "include_headline_search": false
    },
    {
      "include_title": ["Finance Director", "Controller"],
      "exclude_title": ["assistant"],
      "location": ["US"],
      "include_headline_search": true
    },
    {
      "include_title": ["Finance Manager", "Accounting Manager"],
      "exclude_title": ["junior", "associate"],
      "location": ["US"],
      "include_headline_search": true
    }
  ],
  "max_results": 5
}
```

### Step 3: Validate Emails
For each contact found, validate their email address:

```json
POST /v2/utilities/email/validate
{
  "email": "jane.doe@stripe.com"
}
```

Discard invalid emails to protect sender reputation.

### Step 4: Sync to CRM
Push verified contacts with role-based tags:
- Tag by seniority level (C-Level, Director, Manager)
- Tag by function (Finance, Sales, Marketing)
- Tag by account tier (Strategic, Enterprise, Mid-Market)

## Complete Flow Diagram

```
Target Account List
        ↓
Domain → LinkedIn (if needed)
        ↓
Waterfall ICP Search
        ↓
Email Enrichment
        ↓
Email Validation
        ↓
Filter Invalid
        ↓
Sync to CRM with Tags
        ↓
Enroll in Sequences
```

## Key Advantage
Unlimited plan eliminates per-credit costs, enabling frequent list refreshes without budget constraints. Run this workflow daily, weekly, or on-demand without worrying about API costs.

## Best Practices

1. **Cascade Design:** Start specific, get broader. CMO → VP Marketing → Marketing Director
2. **Location Strategy:** Start with target region, expand to WORLD in later tiers
3. **Exclusions:** Always exclude assistants, interns, and junior roles
4. **Max Results:** Use 3-5 per account to build multi-threaded outreach
