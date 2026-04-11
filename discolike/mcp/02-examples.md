# MCP Usage Examples

## Find companies similar to your best customers

**Prompt:**
> Find 20 B2B SaaS companies similar to figma.com and miro.com, with 50–200 employees, based in the US or UK.

**Tool called:** `discover-similar-companies`

```json
{
  "domain": ["figma.com", "miro.com"],
  "country": ["US", "GB"],
  "employee_range": "50,200",
  "max_records": 20
}
```

Returns a ranked list of companies with similarity scores, domains, descriptions, employee counts, and digital footprint scores.

---

## Describe your ideal customer in plain English

**Prompt:**
> I'm looking for mid-market e-commerce platforms in Europe that offer headless commerce or composable storefronts. Find me 50 matches.

**Tool called:** `discover-similar-companies`

```json
{
  "icp_prompt": "mid-market e-commerce platforms in Europe that offer headless commerce or composable storefronts",
  "max_records": 50
}
```

The `icp_prompt` parameter uses an LLM to automatically extract filters (Europe → country codes, mid-market → employee range), generate search text, and suggest example domains — all from one natural language description.

---

## Look up a contact by name

**Prompt:**
> Find John Smith at Salesforce

**Tool called:** `match-contacts`

```json
{
  "name": "John Smith",
  "company_name": "Salesforce"
}
```

Returns matching contacts with name, title, company, and domain. This is a lightweight text match with **no credits consumed** — useful for quick lookups before enrichment.

---

## Get a full company profile

**Prompt:**
> Give me the full business profile for stripe.com — address, social links, employee count, everything.

**Tool called:** `business-profile`

```json
{
  "domain": "stripe.com"
}
```

Returns company name, operating status, HQ address, phone numbers, public emails, social profiles (LinkedIn, Twitter, GitHub), business description, industry classifications, employee count range, digital footprint score (1–800), and last update date.

---

## Find decision-makers at target accounts

**Prompt:**
> Find VPs and directors of marketing at hubspot.com, mailchimp.com, klaviyo.com, brevo.com, and customer.io. Only people with validated emails.

**Tool called:** `search-contacts`

```json
{
  "domain": ["hubspot.com", "mailchimp.com", "klaviyo.com", "brevo.com", "customer.io"],
  "seniority": "vp",
  "department": "Marketing",
  "has_email": true,
  "email_validated": true,
  "max_records": 50,
  "results_by_company": 5
}
```

Returns up to 5 contacts per company with names, titles, validated email addresses, LinkedIn profiles, and similarity scores.

---

## Check what technologies a company uses

**Prompt:**
> What technologies and vendors does notion.so use?

**Tool called:** `vendor-and-technology-data`

```json
{
  "domain": "notion.so",
  "match": "client"
}
```

Returns detected vendors and technologies — analytics tools, payment processors, CDNs, marketing platforms, and more. Each entry includes the implementation FQDN where the vendor was detected.

---

## Read a company's website content

**Prompt:**
> What does linear.app do? Pull their website text so we can understand their positioning.

**Tool called:** `extract-website-text`

```json
{
  "domain": "linear.app"
}
```

Returns up-to-date homepage text from 65M+ business websites — results are instant. Free for any domain you've already discovered in the last 90 days. Useful for analyzing a company's positioning, product description, or messaging when discovery filters alone aren't enough.

---

## Check where a domain redirects

**Prompt:**
> Does www.heroku.com redirect somewhere? Show me all known redirects.

**Tool called:** `domain-redirects`

```json
{
  "filters": {
    "domain": "heroku.com",
    "match": "from"
  }
}
```

Returns redirect mappings — useful for understanding domain consolidations, brand changes, and aliases. Use `match: "from"` to see where a domain redirects to, or `match: "to"` to find domains that redirect to it.

---

## Enrich a list of domains in bulk

**Prompt:**
> I have these 5 domains — get me firmographic data and growth trends for all of them: stripe.com, plaid.com, brex.com, ramp.com, mercury.com

**Tool called:** `append-data`

```json
{
  "filters": {
    "domains": ["stripe.com", "plaid.com", "brex.com", "ramp.com", "mercury.com"],
    "dataset": ["bizdata", "growth"]
  }
}
```

Enriches up to 100 domains per call with one or more datasets: `bizdata` (firmographics), `growth` (quarterly trends), `redirects` (redirect mappings), or `domain_status` (active/parked/expired). More efficient than calling single-domain tools in a loop.

---

## Tag and organize saved queries

**Prompt:**
> Tag my "US fintech prospects" query as "fintech" and "outbound-q2", then show me all queries tagged "fintech".

**Tools called:** `add-tags-to-query`, then `list-saved-queries`

```json
{
  "input": {
    "query_id": "abc123",
    "tags": ["fintech", "outbound-q2"]
  }
}
```

Tags are free-form labels for organizing saved queries. Related tools:

- `list-tags` — see all tags in your organization
- `remove-tags-from-query` — remove tags from a query
- `get-domains-by-tags` — pull all domains from queries matching specific tags (supports `match: "any"` or `match: "all"`)

---

## Pull domains across tagged queries

**Prompt:**
> Give me every domain from queries tagged "fintech" or "payments".

**Tool called:** `get-domains-by-tags`

```json
{
  "input": {
    "tags": ["fintech", "payments"],
    "match": "any"
  }
}
```

Returns deduplicated domains from all saved queries that match the specified tags. Use `match: "all"` to require every tag, or `match: "any"` (default) for a union.

---

## Research companies with DiscoGen

**Prompt:**
> For each of these domains, tell me if they offer a free trial and what their pricing model is: notion.so, linear.app, clickup.com, monday.com, asana.com

**Tool called:** `run-discogen`

```json
{
  "query": "Does this company offer a free trial? What is their pricing model (freemium, free trial, demo only, contact sales)?",
  "domains": ["notion.so", "linear.app", "clickup.com", "monday.com", "asana.com"],
  "context_mode": "website",
  "web_search": false
}
```

With ≤10 domains, results return directly — no polling needed. DiscoGen auto-detects the response format and returns structured answers per domain.

---

## Run DiscoGen on a large list (async)

**Prompt:**
> Check which of these 200 companies are hiring for AI/ML roles right now.

**Tool called:** `run-discogen`, then `get-discogen-status`

```json
{
  "query": "Is this company currently hiring for AI or machine learning roles?",
  "domains": ["... 200 domains ..."],
  "context_mode": "domain",
  "web_search": true
}
```

With >10 domains, the tool returns a `task_id`. Poll with `get-discogen-status` until status is `"completed"`.

---

## Qualify contacts with DiscoGen

**Prompt:**
> For these contacts, check if they're a decision-maker for developer tools purchases.

**Tool called:** `run-discogen-personas`

```json
{
  "query": "Based on this person's title and seniority, are they likely a decision-maker for purchasing developer tools?",
  "persona_ids": [12345, 12346, 12347],
  "context_mode": "company"
}
```

Uses contact profile + employer company data to evaluate each person. Returns structured yes/no answers with reasoning.

---

## Check your account and usage

**Prompt:**
> What's my current plan and how many credits have I used this month?

**Tools called:** `account-status` and `usage-statistics` (no parameters needed).

Returns your subscription tier, rate limits, credit balance, and a breakdown of API usage for the current billing period.

---

## Cost reference

| Tool | Plan | Cost |
|------|------|------|
| `account-status` | Any | Free |
| `usage-statistics` | Any | Free |
| `count-matching-domains` | Starter+ | Free |
| `count-contacts` | Starter+ | Free |
| `match-contacts` | Starter+ | Free |
| `bulk-match-contacts` | Starter+ | Free (credits if `enrich: true`) |
| `list-saved-queries` | Starter+ | Free |
| `save-mcp-query` | Starter+ | Free |
| `save-exclusion-list` | Starter+ | Free |
| `list-tags` | Starter+ | Free |
| `add-tags-to-query` | Starter+ | Free |
| `remove-tags-from-query` | Starter+ | Free |
| `get-domains-by-tags` | Starter+ | Free |
| `discover-similar-companies` | Starter+ | Credits |
| `business-profile` | Starter+ | Credits |
| `digital-footprint-score` | Starter+ | Credits |
| `growth-metrics` | Starter+ | Credits |
| `extract-website-text` | Starter+ | Credits |
| `search-contacts` | Starter+ | Credits |
| `contact-lookup` | Starter+ | Credits |
| `append-data` | Starter+ | Credits |
| `run-discogen` | Starter+ | Credits + LLM API cost |
| `run-discogen-personas` | Starter+ | Credits + LLM API cost |
| `get-discogen-status` | Starter+ | Free |
| `cancel-discogen` | Starter+ | Free |
| `list-discogen-integrations` | Starter+ | Free |
| `match-company-to-domain` | Team+ | Credits |
| `domain-redirects` | Team+ | Credits |
| `vendor-and-technology-data` | Team+ | Credits |
| `segment-domains` | Pro+ | Credits |
| `subsidiaries-and-parent-companies` | Enterprise | Credits |
| `public-company-links` | Enterprise | Credits |

Tools marked "Credits" only charge for new domains or contacts — anything you've already discovered in the last 90 days is free.

For the full list of tools, see the [Tools Reference](/v1/docs/mcp/tools/).
