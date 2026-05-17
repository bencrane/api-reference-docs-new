# Job Search

`GET /job-search`

Search for jobs with various filters and options as available on `https://www.glassdoor.com/Job/index.htm`.

## Query Parameters

| Parameter | Type | Required | Constraints | Default | Description |
|-----------|------|----------|-------------|---------|-------------|
| `query` | string | Yes | — | — | Search query. |
| `location` | string | Yes | — | — | Location to search in. |
| `location_type` | string (enum) | No | — | `ANY` | Specify the type of the location you are looking to get salary estimation for additional accuracy. |
| `limit` | number | No | min: 1, max: 100 | `10` | The maximum number of results to return in a single response. Use with `cursor` to paginate through larger result sets. |
| `cursor` | string | No | — | — | A pagination token returned in the API response. Pass this value into the next request to retrieve the following page of job results. If omitted, the first page is returned. |
| `easy_apply_only` | boolean | No | — | — | Only return jobs with easy apply. |
| `remote_only` | string | No | — | — | Only return remote jobs. |
| `min_company_rating` | string | No | — | — | Minimum job employer company rating. |
| `domain` | string (enum) | No | — | `www.glassdoor.com` | The Glassdoor domain to use. |

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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/job-search?query=front%20end%20developer&location=new%20york' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`, truncated)

```json
{
  "Example": {
    "value": {
      "status": "OK",
      "request_id": "4aa573ab-19d3-4013-a4ef-d027dbea58e5",
      "parameters": {
        "query": "front end developer",
        "location": "new york",
        "location_type": "ANY",
        "domain": "www.glassdoor.com",
        "min_company_rating": "ANY",
        "easy_apply_only": false,
        "remote_only": false,
        "page": 1
      },
      "data": {
        "total_count": 341,
        "jobs": [
          {
            "job_id": 1009880541411,
            "job_title": "Front End Developer",
            "company_id": 1950127,
            "company_name": "Sumitomo Group",
            "company_logo": "https://media.glassdoor.com/sql/1950127/sumitomo-group-squarelogo-1603119057507.png",
            "location_name": "New York, NY",
            "location_id": 1132348,
            "location_type": "CITY",
            "job_link": "https://www.glassdoor.com/job-listing/front-end-developer-sumitomo-mitsui-banking-corporation-JV_IC1132348_KO0,19_KE20,55.htm?jl=1009880541411",
            "easy_apply": false,
            "age_in_days": 7,
            "is_sponsored": false,
            "is_sponsored_employer": false,
            "rating": 4.1,
            "salary_currency": "USD",
            "salary_period": "ANNUAL",
            "salary_min": 85000,
            "salary_median": 127500,
            "salary_max": 170000,
            "salary_source": "EMPLOYER_PROVIDED"
          }
        ],
        "cursor": "AAoAAYEACgAAAAAAAAAAAAAAAk1jCn8AGwEAALMZXqkFTjzQ0yEB5f5ztiOeI5J5O9rvwAAA"
      }
    }
  }
}
```
