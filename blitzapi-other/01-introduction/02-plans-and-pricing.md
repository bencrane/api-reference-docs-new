> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Welcome to BlitzAPI

> High-performance B2B data infrastructure for Growth & Revenue teams.

**BlitzAPI** provides a programmable interface to access **verified B2B data** from a proprietary LinkedIn-based dataset covering 380M+ contacts worldwide. We enable Growth Engineers and RevOps teams to build automated lead pipelines at scale — no scrapers to maintain, no static databases to manage.

<img src="https://mintcdn.com/blitzapi-6cafe00d/lMjF8LYneijS3EL2/images/blitzapi-cover.png?fit=max&auto=format&n=lMjF8LYneijS3EL2&q=85&s=d1958a5b2afb5169cae2020ed05bc559" alt="BlitzAPI - B2B Data Enrichment" style={{ width:"100%" }} width="1536" height="1024" data-path="images/blitzapi-cover.png" />

***

## ⚡ Core Logic: Waterfall ICP

BlitzAPI’s most popular feature is the **Waterfall ICP Search**. It solves a common engineering challenge: mapping a target account to a specific decision-maker without manual filtering.

Instead of retrieving a raw list of employees, you define a **priority hierarchy**. The API executes a cascading search until it matches your criteria.

<Steps>
  <Step title="1. Define the Cascade">
    You configure a JSON rule: *"First, look for the CEO in the US. If not found, look for the VP of Sales. If not found, look for a Sales Director."*
  </Step>

  <Step title="2. Intelligent Routing">
    The API queries our proprietary dataset in priority order, stopping as soon as your criteria are matched.
  </Step>

  <Step title="3. Structured Output">
    You receive the single most relevant decision-maker for that company, ready for enrichment.
  </Step>
</Steps>

<Card title="Read the Waterfall Logic Docs" icon="stairs" href="/guide/concepts/waterfall-logic">
  See how to construct hierarchical queries to maximize relevance.
</Card>

***

## ♾️ Flat-Rate Unlimited

BlitzAPI is a **flat monthly subscription — no per-request fees, no overage surprises**. Choose the plan that unlocks the APIs you need.

| Plan                        | Price    | Includes                                                                  |
| :-------------------------- | :------- | :------------------------------------------------------------------------ |
| **Unlimited Leads**         | \$399/mo | Waterfall ICP, Company Search, Employee Finder, Domain→LinkedIn, and more |
| **Unlimited Email**         | \$499/mo | Everything above + Email Enrichment (62M+ emails, 97% accuracy)           |
| **Unlimited Phone Numbers** | \$599/mo | Everything above + Phone Enrichment (US only, +40M mobile numbers)        |

<Card title="See full plan comparison" icon="receipt" href="/guide/concepts/pricing-unlimited">
  Detailed feature matrix, use case guide, and free trial info.
</Card>

***

## What do you want to build?

Select the documentation path that matches your technical goal.

<CardGroup cols={2}>
  <Card title="Quick Start" icon="bolt" href="/guide/getting-started/quickstart">
    Get your API Key and execute your first enrichment request via cURL.
  </Card>

  <Card title="Full Workflow" icon="rotate" href="/guide/recipes/enrichment-workflow">
    Learn how to chain Search, Enrichment, and Validation into a single automated pipeline.
  </Card>

  <Card title="Pricing & Limits" icon="server" href="/guide/concepts/pricing-unlimited">
    Technical details on rate limits (RPS), concurrency, and fair use policies.
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference">
    Interactive OpenAPI documentation to test endpoints and view schema definitions.
  </Card>
</CardGroup>

***

## Supported Integrations

BlitzAPI acts as the data engine behind your existing stack.

| Category            | Compatible Tools               |
| :------------------ | :----------------------------- |
| **Orchestrators**   | n8n, Make (Integromat), Zapier |
| **Data Operations** | Clay, Airtable, Google Sheets  |
| **CRM & Sales**     | HubSpot, Salesforce, Pipedrive |
| **Outreach**        | Smartlead, Instantly, Lemlist  |

<Note>
  **Building a custom integration?** Our API is platform-agnostic. As long as your tool can make an HTTP POST request, it works with BlitzAPI.
</Note>


Built with [Mintlify](https://mintlify.com).