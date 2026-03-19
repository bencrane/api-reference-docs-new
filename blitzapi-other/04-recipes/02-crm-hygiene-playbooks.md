> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# CRM Hygiene Playbooks

> Dynamic enrichment and automated cleaning workflows.

Data decay is inevitable, but manual cleaning is obsolete. With BlitzAPI's **Unlimited Model**, RevOps teams can shift from "Annual Cleaning" to **"Continuous Hygiene"**.

Instead of buying static lists, you can build **Dynamic Playbooks** that trigger exactly when you need them.

***

## Playbook 1: The "Dynamic Account" Enrichment

*(The "Surgical Strike" Approach)*

**The Scenario**: A Sales Rep is working a high-priority Account in Salesforce/HubSpot. The account has potential, but the Rep lacks the *right* contacts (e.g., the VP of Sales is missing).

**The Solution**: Instead of asking the Rep to go to LinkedIn and manually copy-paste data, you give them an **"Enrich Now" button** in the CRM.

<Steps>
  <Step title="1. Trigger (The Button)">
    The Rep clicks a button in the CRM (via a Webhook/Flow). The CRM account must have either a **Company LinkedIn URL** or a **Company Domain** stored.
  </Step>

  <Step title="2. Resolve the Company LinkedIn URL">
    BlitzAPI requires a **Company LinkedIn URL** as its primary matching key — a domain alone is not a reliable identifier.

    * **If the CRM already stores the LinkedIn URL**: use it directly as `company_linkedin_url`.
    * **If only a domain is available**: first call `POST /v2/enrichment/domain-to-linkedin` to resolve the domain into a LinkedIn URL, then pass the result to the next step.
  </Step>

  <Step title="3. The Waterfall Search">
    Send the Company LinkedIn URL to BlitzAPI's **Waterfall ICP** endpoint (`POST /v2/search/waterfall-icp-keyword`).

    * *Example query*: "Find the VP Sales or CRO in the US for this company."
  </Step>

  <Step title="4. Automatic Sync">
    BlitzAPI returns the matched contact's LinkedIn URL and profile. Pass it to the enrichment endpoints to retrieve the **Verified Email** and/or **Phone**. The automation creates the Contact in the CRM and assigns it to the Rep instantly.
  </Step>
</Steps>

***

## Playbook 2: The "Pre-Send" Safety Net

*(The Anti-Bounce Shield)*

**The Scenario**: You are about to enroll 5,000 leads into a cold email sequence. Some data is old; some emails might be "Catch-All".

**The Solution**: An automated gatekeeper that validates every email *before* it enters the sequence.

<Steps>
  <Step title="1. Batch Export">
    Your automation tool (n8n/Make) pulls the list of emails.
  </Step>

  <Step title="2. Strict Validation">
    Pass every email through `POST /v2/utilities/email/validate`.

    * BlitzAPI checks: Syntax, DNS, and performs a live SMTP handshake.
  </Step>

  <Step title="3. Routing">
    * **Valid**: Enrolled in Sequence A (Aggressive).
    * **Catch-All**: Enrolled in Sequence B (Manual/LinkedIn).
    * **Invalid**: Marked as "Do Not Contact" in CRM.
  </Step>
</Steps>

<Card title="Tech Enabler: Email Validation" icon="shield-check" href="/api-reference">
  Use `POST /v2/utilities/email/validate` to filter out risks before they hurt your domain reputation.
</Card>

***

## ⚡ Scaling with Low-Code (n8n, Make, Clay)

The true power of BlitzAPI is unleashed when combined with automation platforms. Because our plans are **Unlimited**, you can run massive loops without worrying about "burning credits."

> **RevOps Insight**: With the Unlimited Plan, you can set up a "Weekend Job" in n8n that scans your entire CRM, re-validates every email, and updates job titles, ensuring your team walks in on Monday to a pristine database.

***

## Ready to build?

<CardGroup cols={2}>
  <Card title="Get your API Key" icon="key" href="https://app.blitz-api.ai">
    Start building your dynamic playbooks today.
  </Card>

  <Card title="See Integration Guides" icon="puzzle-piece" href="/guide/integrations/clay">
    Copy-paste recipes for your favorite automation tools.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).