> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Recipe: Account Breakthrough

> Stop Spray & Pray. Penetrate strategic accounts with surgical precision.

**The Challenge**: You have a list of 500 "Dream Accounts" (ICP) in your CRM.

**The Old Way**: Your SDRs spend days manually searching LinkedIn, copying random emails, and hitting "Send" to whoever they find.

**The Blitz Way**: Automate the entire breakthrough process. Identify the buying committee, verify their data, and enroll them in sequences---instantly.

This playbook demonstrates how to build an **Account Breakthrough Engine** using BlitzAPI.

***

## 🛠️ The Stack

* **Orchestrator**: n8n or Make (to glue everything together).
* **Data Engine**: BlitzAPI (Waterfall ICP + Validation).
* **Source of Truth**: HubSpot / Salesforce (Input).
* **Execution**: Smartlead / Lemlist (Cold Email).

***

## 🗺️ The Workflow

We will move from a "Target Account List" to "Active Conversations" in up to 5 automated steps.

<Note>
  BlitzAPI's **Waterfall ICP** endpoint takes a `company_linkedin_url` as its primary input — not a domain. A LinkedIn URL is the only reliable company identifier in our dataset. See Step 1 for how to handle both cases.
</Note>

<Steps>
  <Step title="0. Resolve the Company LinkedIn URL (if needed)">
    Your CRM account record must provide a **Company LinkedIn URL** to run the Waterfall search.

    * **If the CRM stores the LinkedIn URL directly**: use it as-is — skip to Step 1.
    * **If only a domain is stored** (e.g., `stripe.com`): call `POST /v2/enrichment/domain-to-linkedin` first to resolve it into a Company LinkedIn URL.

    ```json  theme={null}
    POST /v2/enrichment/domain-to-linkedin
    { "domain": "stripe.com" }
    ```

    This returns the canonical `company_linkedin_url` to use in the next step.
  </Step>

  <Step title="1. Input: The Target List">
    Your workflow pulls the target accounts from your CRM. For each account, you now have a `company_linkedin_url` (either stored directly or resolved in Step 0).
  </Step>

  <Step title="2. The 'Waterfall' Penetration">
    We don't just want *any* contact. We want the **Economic Buyer** first, then the **Champion**.

    Send the `company_linkedin_url` to BlitzAPI with a strict priority hierarchy:

    1. **Tier 1**: C-Level & VPs (The Decision Makers).
    2. **Tier 2**: Directors (The Champions).
    3. **Tier 3**: Managers (The Entry Points).
  </Step>

  <Step title="3. The Safety Gate (Validation)">
    Every profile found is passed through BlitzAPI's **Email Validation** (`POST /v2/utilities/email/validate`).

    * **Valid**: Sync to CRM & Smartlead immediately.
    * **Catch-All**: Route to a manual review list (optional) or secondary sequence.
    * **Invalid**: Discarded automatically to protect domain reputation.
  </Step>

  <Step title="4. Contextual Sync">
    Push data back to the CRM with context tags:

    * `Tag: Tier 1 - Decision Maker`
    * `Tag: Tier 2 - Champion`

    This allows Smartlead/Lemlist to send **different scripts** to the VP (Strategic value) vs. the Manager (Operational pain).
  </Step>
</Steps>

***

## 🧠 The "Waterfall" Configuration

This is the brain of the operation. By setting `max_results: 5`, we ensure we penetrate the account with multiple touchpoints without spamming the entire directory.

**Endpoint**: `POST /v2/search/waterfall-icp-keyword`

```json  theme={null}
{
 "company_linkedin_url": "https://www.linkedin.com/company/target-account",
 "cascade": [
   {
     "include_title": ["Chief Revenue Officer", "CRO", "VP Sales", "Head of Growth"],
     "location": ["US", "GB"],
     "include_headline_search": false
   },
   {
     "include_title": ["Sales Director", "Director of Business Development"],
     "location": ["US", "GB"],
     "include_headline_search": true
   },
   {
     "include_title": ["Sales Manager", "Account Executive Team Lead"],
     "location": ["US", "GB"],
     "include_headline_search": false
   }
 ],
 "max_results": 5
}
```

<Note>
  **Pro Tip**: Notice the `max_results: 5`. BlitzAPI will fill these 5 slots starting from the top of your cascade. If it finds 5 C-Levels, it stops there. If it only finds 1 C-Level, it fills the remaining 4 slots with Directors. **You always get the best possible seniority mix.**
</Note>

***

## 🚀 Why the "Unlimited Model" Enables This

Running this strategy with traditional "Per Credit" providers is prohibitively expensive. Enriching 5 contacts per company across 1,000 accounts = **5,000 credits**.

With BlitzAPI's **Unlimited Plan**:

* **Cost**: Included in your flat monthly fee.
* **Risk**: Zero. You can run this on 100,000 accounts if you want.
* **Refresh**: You can re-run this playbook every quarter to catch new hires (Job Changes) without worrying about the bill.

<CardGroup cols={2}>
  <Card title="Start Building in n8n" icon="bolt" href="/guide/integrations/n8n">
    See our n8n templates to orchestrate this flow.
  </Card>

  <Card title="Start Building in Clay" icon="table" href="/guide/integrations/clay">
    Prefer spreadsheets? Run this logic inside Clay.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).