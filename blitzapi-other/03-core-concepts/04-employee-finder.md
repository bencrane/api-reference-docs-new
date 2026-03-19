> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Employee Finder

> Search employees at a company by role, seniority, department, and location. With pagination.

The **Employee Finder** endpoint (`POST /v2/search/employee-finder`) lets you search for employees within a specific company using structured filters: job level, department, geography, and more.

Unlike [Waterfall ICP Search](/guide/concepts/waterfall-logic) which uses a priority cascade to find the *best* contact, Employee Finder returns *all matching employees* with pagination — ideal for broad team mapping and multi-threaded outreach.

**Paid plans**: Unlimited — included in your flat monthly subscription.

***

## When to Use Employee Finder vs. Other Endpoints

| Use Case                                                 | Best Endpoint                                    |
| :------------------------------------------------------- | :----------------------------------------------- |
| Find the *single best* decision-maker at a company       | [Waterfall ICP](/guide/concepts/waterfall-logic) |
| Map *all* VPs and Directors in the Sales department      | **Employee Finder**                              |
| Build a buying committee with strict priority order      | [Waterfall ICP](/guide/concepts/waterfall-logic) |
| Export the full engineering team for hiring intelligence | **Employee Finder**                              |
| Get paginated results across large companies             | **Employee Finder**                              |

***

## Request Parameters

### Top-Level Parameters

| Parameter               | Type     | Required | Default     | Description                                                                                               |
| :---------------------- | :------- | :------- | :---------- | :-------------------------------------------------------------------------------------------------------- |
| `company_linkedin_url`  | `string` | Yes      | —           | The full LinkedIn URL of the target company.                                                              |
| `country_code`          | `array`  | No       | `["WORLD"]` | Filter by country (2-letter ISO codes). Use `["WORLD"]` for global.                                       |
| `continent`             | `array`  | No       | —           | Filter by continent. See [accepted values](/guide/reference/field-normalization#continents).              |
| `sales_region`          | `array`  | No       | —           | Filter by sales region. See [accepted values](/guide/reference/field-normalization#sales-regions).        |
| `job_level`             | `array`  | No       | —           | Filter by seniority level. See [accepted values](/guide/reference/field-normalization#job-levels).        |
| `job_function`          | `array`  | No       | —           | Filter by department/function. See [accepted values](/guide/reference/field-normalization#job-functions). |
| `min_connections_count` | `number` | No       | `0`         | Minimum LinkedIn connections (0–500). Useful to filter out inactive profiles.                             |
| `max_results`           | `number` | No       | `50`        | Results per page. Min: `1`, Max: `50`.                                                                    |
| `page`                  | `number` | No       | `1`         | Page number for pagination. Starts at `1`.                                                                |

<Warning>
  All filter values (`job_level`, `job_function`, `sales_region`, `continent`) are **case-sensitive enums**. Passing `"vp"` instead of `"VP"` or `"sales"` instead of `"Sales & Business Development"` will silently return 0 results. Copy-paste from the [Field Normalization reference](/guide/reference/field-normalization).
</Warning>

***

## Example Request

Find all Directors and VPs in Sales & Marketing at OpenAI, in North America:

<CodeGroup>
  ```json cURL theme={null}
  curl -X POST "https://api.blitz-api.ai/v2/search/employee-finder" \
    -H "Content-Type: application/json" \
    -H "x-api-key: YOUR_API_KEY" \
    -d '{
      "company_linkedin_url": "https://www.linkedin.com/company/openai",
      "job_level": ["VP", "Director"],
      "job_function": ["Sales & Business Development", "Advertising & Marketing"],
      "sales_region": ["NORAM"],
      "max_results": 10,
      "page": 1
    }'
  ```

  ```javascript Node.js theme={null}
  const result = await blitzRequest("POST", "/v2/search/employee-finder", {
    company_linkedin_url: "https://www.linkedin.com/company/openai",
    job_level: ["VP", "Director"],
    job_function: ["Sales & Business Development", "Advertising & Marketing"],
    sales_region: ["NORAM"],
    max_results: 10,
    page: 1,
  });

  console.log(`Page ${result.page} of ${result.total_pages}`);
  for (const person of result.results) {
    console.log(`${person.full_name} — ${person.headline}`);
    console.log(`  LinkedIn: ${person.linkedin_url}`);
  }
  ```

  ```python Python theme={null}
  result = blitz_request("POST", "/v2/search/employee-finder", {
      "company_linkedin_url": "https://www.linkedin.com/company/openai",
      "job_level": ["VP", "Director"],
      "job_function": ["Sales & Business Development", "Advertising & Marketing"],
      "sales_region": ["NORAM"],
      "max_results": 10,
      "page": 1,
  })

  print(f"Page {result['page']} of {result['total_pages']}")
  for person in result["results"]:
      print(f"{person['full_name']} — {person['headline']}")
      print(f"  LinkedIn: {person['linkedin_url']}")
  ```
</CodeGroup>

***

## Response Schema

```json  theme={null}
{
  "company_linkedin_url": "https://www.linkedin.com/company/openai",
  "max_results": 10,
  "results_length": 10,
  "page": 1,
  "total_pages": 24,
  "results": [
    {
      "first_name": "Jane",
      "last_name": "Doe",
      "full_name": "Jane Doe",
      "nickname": null,
      "civility_title": "Ms",
      "headline": "VP of Sales at OpenAI",
      "about_me": "Experienced sales leader...",
      "location": {
        "city": "San Francisco",
        "state_code": "CA",
        "country_code": "US",
        "continent": "North America"
      },
      "linkedin_url": "https://www.linkedin.com/in/janedoe",
      "connections_count": 2500,
      "profile_picture_url": "https://media.licdn.com/...",
      "experiences": [
        {
          "job_title": "VP of Sales",
          "company_linkedin_url": "https://www.linkedin.com/company/openai",
          "company_linkedin_id": "88888888",
          "job_description": "Leading the global sales team...",
          "job_start_date": "2024-01-15",
          "job_end_date": null,
          "job_is_current": true,
          "job_location": {
            "city": "San Francisco",
            "state_code": "CA",
            "country_code": "US"
          }
        }
      ],
      "education": [
        {
          "school_name": "Stanford University",
          "degree": "MBA",
          "field_of_study": "Business Administration",
          "start_date": "2016-09-01",
          "end_date": "2018-06-01"
        }
      ],
      "skills": ["Sales Strategy", "B2B", "SaaS"],
      "certifications": []
    }
  ]
}
```

### Top-Level Response Fields

| Field                  | Type     | Description                                                           |
| :--------------------- | :------- | :-------------------------------------------------------------------- |
| `company_linkedin_url` | `string` | The company queried.                                                  |
| `max_results`          | `number` | The `max_results` value you sent.                                     |
| `results_length`       | `number` | Number of results on this page.                                       |
| `page`                 | `number` | Current page number.                                                  |
| `total_pages`          | `number` | Total number of pages available. Use to know when to stop paginating. |
| `results`              | `array`  | Array of person profiles.                                             |

### Person Fields (`results[]`)

| Field                 | Type             | Description                                                         |
| :-------------------- | :--------------- | :------------------------------------------------------------------ |
| `first_name`          | `string \| null` | First name.                                                         |
| `last_name`           | `string \| null` | Last name.                                                          |
| `full_name`           | `string \| null` | Full display name.                                                  |
| `nickname`            | `string \| null` | Nickname / preferred name.                                          |
| `civility_title`      | `string \| null` | Title (e.g., "Mr", "Ms", "Dr").                                     |
| `headline`            | `string \| null` | LinkedIn headline.                                                  |
| `about_me`            | `string \| null` | LinkedIn "About" section text.                                      |
| `location`            | `object`         | Person location: `city`, `state_code`, `country_code`, `continent`. |
| `linkedin_url`        | `string`         | Person LinkedIn URL. Use this as input for email/phone enrichment.  |
| `connections_count`   | `number \| null` | LinkedIn connections count.                                         |
| `profile_picture_url` | `string \| null` | URL to the profile picture.                                         |
| `experiences`         | `array`          | Work history (see below).                                           |
| `education`           | `array \| null`  | Education history (see below).                                      |
| `skills`              | `array \| null`  | List of skills (strings).                                           |
| `certifications`      | `array \| null`  | List of certifications. Each entry has `name`, `authority`, `url`.  |

### Experience Fields (`results[].experiences[]`)

| Field                  | Type              | Description                                         |
| :--------------------- | :---------------- | :-------------------------------------------------- |
| `job_title`            | `string \| null`  | Job title.                                          |
| `company_linkedin_url` | `string \| null`  | Company LinkedIn URL.                               |
| `company_linkedin_id`  | `string \| null`  | Company LinkedIn numeric ID.                        |
| `job_description`      | `string \| null`  | Job description text.                               |
| `job_start_date`       | `string \| null`  | Start date (format: `YYYY-MM-DD`).                  |
| `job_end_date`         | `string \| null`  | End date (`null` if current role).                  |
| `job_is_current`       | `boolean \| null` | Whether this is the current role.                   |
| `job_location`         | `object`          | Job location: `city`, `state_code`, `country_code`. |

### Education Fields (`results[].education[]`)

| Field            | Type     | Description                       |
| :--------------- | :------- | :-------------------------------- |
| `school_name`    | `string` | Name of the school or university. |
| `degree`         | `string` | Degree obtained.                  |
| `field_of_study` | `string` | Field of study / major.           |
| `start_date`     | `string` | Start date.                       |
| `end_date`       | `string` | End date.                         |

<Note>
  **Key difference from Waterfall ICP**: Employee Finder return person fields **directly** in `results[]`. Waterfall ICP nests them inside `results[].person`. Plan your parsing logic accordingly.
</Note>

***

## Pagination

Employee Finder supports page-based pagination. Each response includes `page` and `total_pages`.

```javascript  theme={null}
// Paginate through all results
let page = 1;
let totalPages = 1;

do {
  const result = await blitzRequest("POST", "/v2/search/employee-finder", {
    company_linkedin_url: "https://www.linkedin.com/company/openai",
    job_level: ["VP", "Director"],
    max_results: 50,
    page: page,
  });

  totalPages = result.total_pages;

  for (const person of result.results) {
    console.log(`${person.full_name} — ${person.headline}`);
  }

  page++;
} while (page <= totalPages);
```

***

## Combining with Enrichment

Employee Finder returns LinkedIn profile URLs but **not** emails or phone numbers. Chain with enrichment endpoints to complete the data:

<Steps>
  <Step title="Search employees">
    Use Employee Finder to get `linkedin_url` for each matching person.
  </Step>

  <Step title="Enrich emails">
    Pass each `linkedin_url` to `POST /v2/enrichment/email` to get verified work emails.
  </Step>

  <Step title="Enrich phones (US only)">
    Pass each `linkedin_url` to `POST /v2/enrichment/phone` for direct mobile numbers.
  </Step>

  <Step title="Validate and sync">
    Validate emails via `POST /v2/utilities/email/validate`, then sync clean data to your CRM.
  </Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Waterfall ICP Search" icon="ranking-star" href="/guide/concepts/waterfall-logic">
    Need the *single best* contact? Use Waterfall instead.
  </Card>

  <Card title="Field Normalization" icon="list-check" href="/guide/reference/field-normalization">
    Full list of accepted values for job\_level, job\_function, and sales\_region.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).