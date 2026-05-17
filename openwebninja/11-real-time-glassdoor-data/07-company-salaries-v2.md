# Company Salaries v2

`GET /company-salaries-v2`

Get and Search Company Data, Jobs, Employer Reviews, Salaries, Interviews, and More from Glassdoor in Real-Time (unofficial API).

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `company_id` | string | Yes | — | Glassdoor company ID or name (e.g. `9079` / e.g. `Amazon`). |
| `location` | string | No | — | The location for which to get salary estimation (e.g. `San Francisco`). |
| `location_type` | string (enum) | No | `ANY` | Specify the type of the location you are looking to get salary estimation for additional accuracy. |
| `job_title` | string | No | — | The job title for which to get salary estimation. |
| `page` | number | No | `1` | The salaries page to return (each page includes up to 10 results). |
| `sort` | string (enum) | No | `MOST_SALARIES` | Return salaries in a specific sort order. |
| `domain` | string (enum) | No | `www.glassdoor.com` | The Glassdoor domain to use. |

### `location_type` enum values

```
ANY
CITY
STATE
COUNTRY
```

### `sort` enum values

```
MOST_SALARIES
HIGH_TO_LOW
MOST_RECENT
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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-salaries-v2?company_id=1138' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`, truncated)

```json
{
  "Example": {
    "value": {
      "status": "OK",
      "request_id": "a20f2401-51da-4fb3-9e5d-b0984841ffcb",
      "parameters": {
        "domain": "www.glassdoor.com",
        "location_type": "ANY",
        "page": 1,
        "sort": "MOST_SALARIES"
      },
      "data": {
        "company_id": 1138,
        "location": "United States",
        "job_title_count": 8179,
        "most_recent": "2025-12-01T07:08:09.543",
        "num_pages": 815,
        "salaries": [
          {
            "job_title": "Software Developer, Applications",
            "job_title_id": 3901037,
            "salary_currency": "USD",
            "salary_count": 6630,
            "salary_period": "YEAR",
            "min_salary": 179413.01,
            "median_salary": 265546.47,
            "max_salary": 406010.22,
            "min_base_salary": 130344.31,
            "median_base_salary": 180945.27,
            "max_base_salary": 251190.02,
            "min_additional_pay": 49068.7,
            "median_additional_pay": 84601.2,
            "max_additional_pay": 154820.2,
            "min_cash_bonus": 10567.87,
            "median_cash_bonus": 18220.46,
            "max_cash_bonus": 33343.45,
            "min_stock_bonus": 38500.83,
            "median_stock_bonus": 66380.74,
            "max_stock_bonus": 121476.76
          }
        ]
      }
    }
  }
}
```
