# Salary Estimate

`GET /salary-estimation`

Get salary estimates by job title and location.

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `job_title` | string | Yes | — | The job title for which to get salary estimation (e.g. `marketing assistant`). |
| `location` | string | Yes | — | The location for which to get salary estimation (e.g. `san-francisco, us`). |
| `location_type` | string (enum) | No | `ANY` | Specify the type of the location you are looking to get salary estimation for additional accuracy. |
| `years_of_experience` | string (enum) | No | `ALL` | Get job estimation for a specific experience level range (years). |
| `domain` | string (enum) | No | `www.glassdoor.com` | The Glassdoor domain to use. |

### `location_type` enum values

```
ANY
CITY
STATE
COUNTRY
```

### `years_of_experience` enum values

```
ALL
LESS_THAN_ONE
ONE_TO_THREE
FOUR_TO_SIX
SEVEN_TO_NINE
TEN_TO_FOURTEEN
ABOVE_FIFTEEN
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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/salary-estimation?job_title=software%20developer&location=new%20york' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`)

```json
{
  "Example": {
    "value": {
      "status": "OK",
      "request_id": "929e52f0-323e-4aa3-b2dd-39e63fae3530",
      "parameters": {
        "job_title": "software developer",
        "location": "new york",
        "location_type": "ANY",
        "domain": "www.glassdoor.com",
        "years_of_experience": null
      },
      "data": {
        "location": "New York City, NY",
        "job_title": "Software Developer",
        "min_salary": 128117.25,
        "max_salary": 218872.06,
        "median_salary": 166275.36,
        "min_base_salary": 94192.41,
        "max_base_salary": 155545.69,
        "median_base_salary": 121042.24,
        "min_additional_pay": 33924.84,
        "max_additional_pay": 63326.37,
        "median_additional_pay": 45233.12,
        "salary_period": "YEAR",
        "salary_currency": "USD",
        "salary_count": 213898,
        "salaries_updated_at": "2024-06-06T23:59:59.000Z",
        "link": "https://www.glassdoor.com/Salaries/company-salaries.htm?suggestCount=0&suggestChosen=false&sc.keyword=Software%20Developer&locT=C&locId=1132348",
        "confidence": "CONFIDENT"
      }
    }
  }
}
```
