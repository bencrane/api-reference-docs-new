# Company Salaries

`GET /company-salaries`

Get salary estimation in a specific company by job title and location (optional).

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `company_id` | string | Yes | — | Company ID. |
| `job_title` | string | Yes | — | The job title for which to get salary estimation. |
| `location` | string | No | — | The location for which to get salary estimation (e.g. `San-Francisco`). |
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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-salaries?company_id=1138&job_title=software%20developer' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`)

```json
{
  "Example": {
    "value": {
      "status": "OK",
      "request_id": "ea717f23-8342-4ac4-95db-b7799ed38b2a",
      "parameters": {
        "job_title": "software developer",
        "company_id": 1138,
        "domain": "www.glassdoor.com",
        "location_type": "ANY",
        "years_of_experience": null
      },
      "data": {
        "location": "United States",
        "job_title": "Software Developer",
        "company_id": 1138,
        "company_name": "Apple",
        "min_salary": 142375.78,
        "max_salary": 213814.23,
        "median_salary": 173933.37,
        "min_base_salary": 129428.36,
        "max_base_salary": 189645.71,
        "median_base_salary": 156670.14,
        "min_additional_pay": 12947.42,
        "max_additional_pay": 24168.52,
        "median_additional_pay": 17263.23,
        "salary_period": "YEAR",
        "salary_currency": "USD",
        "confidence": "CONFIDENT",
        "salary_count": 1171
      }
    }
  }
}
```

