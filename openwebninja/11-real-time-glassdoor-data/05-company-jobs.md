# Company Jobs

`GET /company-jobs`

Get jobs posted by a specific company with filtering support and additional options available on Glassdoor.

## Query Parameters

| Parameter | Type | Required | Constraints | Default | Description |
|-----------|------|----------|-------------|---------|-------------|
| `company_id` | string | Yes | — | `1138` | Glassdoor company ID or name (e.g. `9079` / e.g. `Amazon`). |
| `page` | integer | No | — | `1` | The page to return (each page includes up to 10 job listings). |
| `sort` | string (enum) | No | — | `MOST_RELEVANT` | Return reviews in a specific sort order. |
| `job_function` | string (enum) | No | — | `ANY` | Return interviews for a specific job function. |
| `location` | string | No | — | — | The location for which to get interviews (e.g. `San-Francisco`). |
| `location_type` | string (enum) | No | — | `ANY` | Specify the type of the location you are looking to get salary estimation for additional accuracy. |
| `max_age_days` | number | No | min: 0, max: 1000 | `0` | Maximum age of jobs to return in days (e.g. jobs posted in the last `max_age_days` days). By default, returns jobs posted anytime. |
| `domain` | string (enum) | No | — | `www.glassdoor.com` | The Glassdoor domain to use. |

### `sort` enum values

```
MOST_RELEVANT
MOST_RECENT
```

### `job_function` enum values

```
ANY
ADMINISTRATIVE
ARTS_AND_DESIGN
BUSINESS
CONSULTING
... (show all values)
```

### `location_type` enum values

```
ANY
CITY
STATE
COUNTRY
```

### `domain` enum values

```
www.glassdoor.com
www.glassdoor.co.uk
www.glassdoor.com.ar
www.glassdoor.com.au
www.glassdoor.be
... (show all values)
```

## Responses

**`200` — Successful Response** (`application/json`)

## Request Example

```shell
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-jobs?company_id=1138' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`, truncated)

```json
{
  "job_id": 1009852466268,
  "job_title": "Sr. Manager, Internal Tools & Operations, WW Marketplace Platforms & Technologies",
  "company_name": "Apple",
  "company_logo": "https://media.glassdoor.com/sql/1138/apple-squarelogo-1595530154096.png",
  "location_name": "Cupertino, CA",
  "job_link": "https://www.glassdoor.com/job-listing/sr-manager-internal-tools-operations-ww-marketplace-platforms-technologies-apple-JV_IC1147422_KO0,74_KE75,80.htm?jl=1009852466268",
  "easy_apply": false,
  "age_in_days": 0,
  "is_sponsored": false,
  "is_sponsored_employer": false,
  "salary_currency": "USD",
  "salary_period": "ANNUAL",
  "salary_min": 191400,
  "salary_max": 288000,
  "salary_source": "EMPLOYER_PROVIDED"
}
```
