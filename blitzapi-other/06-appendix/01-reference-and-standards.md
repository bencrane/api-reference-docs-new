> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference & Standards

> Endpoint index, country codes, data logic, and performance details.

This section covers technical standards and logic details to help you build reliable integrations with BlitzAPI.

## 📋 Endpoint Index

All v2 endpoints at a glance. Base URL: `https://api.blitz-api.ai`. All endpoints use `POST` except `key-info`.

| Endpoint                            | Method | Description                                                       | Plan   |
| :---------------------------------- | :----- | :---------------------------------------------------------------- | :----- |
| `/v2/account/key-info`              | `GET`  | Check API key validity and rate limit                             | Any    |
| `/v2/search/waterfall-icp-keyword`  | `POST` | Find decision-makers via cascade hierarchy (cached data, \<600ms) | Leads+ |
| `/v2/search/employee-finder`        | `POST` | Search employees by role and seniority level                      | Leads+ |
| `/v2/search/companies`              | `POST` | Find companies by filters (industry, size, location, keywords)    | Leads+ |
| `/v2/enrichment/email`              | `POST` | LinkedIn profile URL → verified work email                        | Email+ |
| `/v2/enrichment/phone`              | `POST` | LinkedIn profile URL → phone number (**US only**)                 | Phone  |
| `/v2/enrichment/email-to-person`    | `POST` | Work email → full person profile                                  | Leads+ |
| `/v2/enrichment/phone-to-person`    | `POST` | Phone number → full person profile                                | Leads+ |
| `/v2/enrichment/company`            | `POST` | Company LinkedIn URL → full company profile                       | Leads+ |
| `/v2/enrichment/domain-to-linkedin` | `POST` | Website domain → Company LinkedIn URL                             | Leads+ |
| `/v2/enrichment/linkedin-to-domain` | `POST` | Company LinkedIn URL → verified email domain                      | Leads+ |
| `/v2/utilities/email/validate`      | `POST` | Validate email deliverability via SMTP handshake                  | Leads+ |
| `/v2/utilities/current-date`        | `POST` | Get current server date/time for a timezone                       | Any    |

<Info>
  Search endpoints require a **Company LinkedIn URL** as input (not a domain). If you only have a domain, use `/v2/enrichment/domain-to-linkedin` first.
</Info>

***

## 🌍 Country Codes (LinkedIn)

All BlitzAPI search endpoints use **2-letter country codes** following the ISO 3166-1 alpha-2 standard (consistent with LinkedIn). Using the wrong format (e.g., `USA` instead of `US`) will return 0 results. See the [Field Normalization reference](/guide/reference/field-normalization#country-codes) for the full list.

<Tip>
  Use `"WORLD"` to search globally without geographic restriction.
</Tip>

<Accordion title="Common Country Codes List">
  | Country            | Code |
  | :----------------- | :--- |
  | **United States**  | `US` |
  | **United Kingdom** | `GB` |
  | **France**         | `FR` |
  | **Canada**         | `CA` |
  | **Germany**        | `DE` |
  | **Australia**      | `AU` |
  | **India**          | `IN` |
  | **Brazil**         | `BR` |
  | **Singapore**      | `SG` |

  [*For a full list of supported codes, refer to the Microsoft LinkedIn Documentation.*](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/country-codes)
</Accordion>

***

## 📧 Email Logic: Matching vs. Guessing

A common misconception is that enrichment APIs "guess" emails (permutations like `first.last@domain.com`). **BlitzAPI does not do this.**

### How we work

1. **Identity Matching**: We match the LinkedIn profile against a massive dataset of known, verified identities.
2. **No Permutations**: We only return an email if we have a concrete record of it linked to that specific individual.
3. **Freshness Guarantee**:

* We do not serve stale data.
* Every email in our database is re-validated **at least once every 30 days**.
* If an email bounces during our internal checks, it is immediately removed from the circulation.

This approach ensures a significantly lower bounce rate compared to "pattern-matching" tools.

***

## 🚦 Rate Limits & Latency

To ensure stability for all users:

* **Concurrency**: All plans include **5 concurrent requests per second** (RPS). Use the `max_requests_per_seconds` field from `/v2/account/key-info` to get your exact limit.
* **Burst**: Short bursts above the limit may be queued, but sustained overage returns `429 Too Many Requests`.
* **Retry on 429**: Wait at least 60 seconds before retrying after a server-side `429`. Client-side rate limiting should prevent this.

**Recommended Client Timeouts:**

| Endpoint Type                                  | Recommended Timeout |
| :--------------------------------------------- | :------------------ |
| Waterfall ICP, Employee Finder, Company Search | 10 seconds          |
| Email/Phone Validation                         | 20 seconds          |
| Enrichment (email, phone, company)             | 10 seconds          |

**Error Codes:**

| Code  | Meaning               | Solution                                                              |
| :---- | :-------------------- | :-------------------------------------------------------------------- |
| `401` | Unauthorized          | Missing or invalid `x-api-key` header.                                |
| `402` | Payment Required      | Account limit reached. Upgrade your plan.                             |
| `404` | Not Found             | API key does not exist.                                               |
| `429` | Too Many Requests     | Exceeded rate limit. Implement client-side rate limiting (max 5 RPS). |
| `500` | Internal Server Error | Transient server error. Retry with exponential backoff.               |


Built with [Mintlify](https://mintlify.com).