> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Company Search

> Find companies matching precise ICP criteria. Build ABM lists and power dynamic prospecting workflows.

The **Company Search** endpoint (`POST /v2/search/companies`) lets you find companies matching precise criteria.

Use it to:

* Build ABM target lists from scratch
* Identify ICP-matching accounts by industry, size, and geography
* Power dynamic prospecting workflows without static lists

**Paid plans**: Unlimited — included in your flat monthly subscription.

***

## How It Works

You send a `POST` request with a `company` object containing your filters. All filters are **optional** and combined with **AND** logic. Within each filter, multiple values use **OR** logic.

The API returns a paginated list of company profiles matching your criteria.

***

## Request Parameters

| Parameter     | Type      | Required | Description                                                                |
| :------------ | :-------- | :------- | :------------------------------------------------------------------------- |
| `company`     | `object`  | Yes      | Filter object. All nested fields are optional and combined with AND logic. |
| `max_results` | `integer` | No       | Number of companies to return. Default: `10`. Max: `25`.                   |
| `cursor`      | `string`  | No       | Pagination cursor from a previous response. Pass to get the next page.     |

### Company Filter Fields

| Field              | Type    | Description                                                                         | Example                    |
| :----------------- | :------ | :---------------------------------------------------------------------------------- | :------------------------- |
| `keywords.include` | `array` | Keywords that must appear in the company profile                                    | `["SaaS", "B2B"]`          |
| `keywords.exclude` | `array` | Keywords to exclude                                                                 | `["agency", "consulting"]` |
| `industry.include` | `array` | Industry names (must use [normalized values](/guide/reference/field-normalization)) | `["Software Development"]` |
| `hq.country_code`  | `array` | HQ country codes (2-letter ISO, e.g., `"US"`)                                       | `["FR", "DE"]`             |
| `employee_range`   | `array` | Employee count ranges                                                               | `["51-200", "201-500"]`    |

<Warning>
  Industry values are **case-sensitive and normalized**. Passing `"Tech"` instead of `"Computer Software"` or `"SaaS"` instead of `"Software Development"` will return 0 results. See the [Field Normalization reference](/guide/reference/field-normalization) for accepted values.
</Warning>

***

## Example Request

Find SaaS companies with 51-500 employees headquartered in France or Germany:

<CodeGroup>
  ```javascript Node.js theme={null}
  const result = await blitzRequest("POST", "/v2/search/companies", {
    company: {
      keywords: { include: ["SaaS"] },
      industry: { include: ["Software Development"] },
      hq: { country_code: ["FR", "DE"] },
      employee_range: ["51-200", "201-500"],
    },
    max_results: 25,
  });

  for (const company of result.results) {
    console.log(`${company.name} — ${company.industry}`);
    console.log(`  LinkedIn: ${company.linkedin_url}`);
    console.log(`  Employees: ${company.employee_count}`);
  }
  ```

  ```python Python theme={null}
  result = blitz_request("POST", "/v2/search/companies", {
      "company": {
          "keywords": { "include": ["SaaS"] },
          "industry": { "include": ["Software Development"] },
          "hq": { "country_code": ["FR", "DE"] },
          "employee_range": ["51-200", "201-500"],
      },
      "max_results": 25,
  })

  for company in result["results"]:
      print(f"{company['name']} — {company['industry']}")
      print(f"  LinkedIn: {company['linkedin_url']}")
      print(f"  Employees: {company['employee_count']}")
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.blitz-api.ai/v2/search/companies" \
    -H "Content-Type: application/json" \
    -H "x-api-key: YOUR_API_KEY" \
    -d '{
      "company": {
        "keywords": { "include": ["SaaS"] },
        "industry": { "include": ["Software Development"] },
        "hq": { "country_code": ["FR", "DE"] },
        "employee_range": ["51-200", "201-500"]
      },
      "max_results": 25
    }'
  ```
</CodeGroup>

***

## Response Schema

```json  theme={null}
{
  "results_length": 25,
  "cursor": "eyJwYWdlIjoy...",
  "results": [
    {
      "name": "Acme Corp",
      "linkedin_url": "https://www.linkedin.com/company/acme-corp",
      "website": "acme.com",
      "industry": "Software Development",
      "employee_count": 120,
      "hq": {
        "city": "Paris",
        "country": "France",
        "country_code": "FR"
      }
    }
  ]
}
```

| Field                      | Type      | Description                                                                                                   |
| :------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------ |
| `results_length`           | `integer` | Number of results in this page.                                                                               |
| `cursor`                   | `string`  | Pass this value in the next request to get the following page. `null` if no more results.                     |
| `results[].name`           | `string`  | Company name.                                                                                                 |
| `results[].linkedin_url`   | `string`  | Company LinkedIn URL. Use this as input for Waterfall ICP, Employee Finder, and Company Enrichment endpoints. |
| `results[].website`        | `string`  | Company website domain.                                                                                       |
| `results[].industry`       | `string`  | Normalized industry name.                                                                                     |
| `results[].employee_count` | `integer` | Approximate employee count.                                                                                   |
| `results[].hq`             | `object`  | Headquarters location (city, country, country\_code).                                                         |

***

## Pagination

The API supports cursor-based pagination. Each response includes a `cursor` field. Pass it in the next request to get the following page.

```json  theme={null}
// First request
{ "company": { ... }, "max_results": 25 }

// Response includes: "cursor": "eyJwYWdl..."

// Next page request
{ "company": { ... }, "cursor": "eyJwYWdl...", "max_results": 25 }
```

When `cursor` is `null` in the response, you've reached the last page.

***

## Recommended Workflow

Use Company Search as the first step in your ABM pipeline:

<Steps>
  <Step title="Find ICP-matching companies">
    Use Company Search to build a list of target accounts matching your ICP filters.
  </Step>

  <Step title="Extract LinkedIn URLs">
    The `linkedin_url` field in the response is your key for all downstream enrichment.
  </Step>

  <Step title="Find decision-makers">
    Pass each `linkedin_url` to the [Waterfall ICP Search](/guide/concepts/waterfall-logic) to find the right contacts.
  </Step>

  <Step title="Enrich and sync">
    Enrich contacts with verified emails and sync to your CRM or outreach tool.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).