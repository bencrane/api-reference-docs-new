# Company Reviews

`GET /company-reviews`

Get company (employer) reviews from Glassdoor, with filters, sort option, and pagination support.

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `company_id` | string | Yes | `9079` | Glassdoor company ID. |
| `page` | integer | No | `1` | The reviews page to return (each page includes up to 10 results). |
| `sort` | string (enum) | No | `POPULAR` | Return reviews in a specific sort order. |
| `query` | string | No | — | Return reviews matching a search query. |
| `language` | string (enum) | No | `en` | Return reviews written in a specific language. |
| `employment_statuses` | string (enum) | No | — | Return reviews written by employees with a specific job type. |
| `only_current_employees` | string | No | `false` | Only return reviews written by current employees (at the time of writing). |
| `extended_rating_data` | boolean | No | `false` | Include extended company rating data such as rating breakdown and rating distributions. |
| `domain` | string (enum) | No | `www.glassdoor.com` | The Glassdoor domain to use. |

### `sort` enum values

```
POPULAR
MOST_RECENT
HIGHEST_RATING
LOWEST_RATING
```

### `language` enum values

```
en
fr
nl
de
pt
es
it
```

### `employment_statuses` enum values

```
REGULAR
INTERN
PART_TIME
CONTRACT
FREELANCE
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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-reviews?company_id=9079' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`, truncated)

```json
{
  "...": "...",
  "review_link": "https://www.glassdoor.com/Reviews/Employee-Review--RVW96264030.htm",
  "job_title": "Staff Software Engineer",
  "review_datetime": "2025-03-29T15:55:35.210Z",
  "employment_status": "REGULAR",
  "is_current_employee": true,
  "years_of_employment": 9,
  "location": "Sunnyvale, CA",
  "helpful_count": 0,
  "not_helpful_count": 0,
  "business_outlook_rating": "POSITIVE",
  "career_opportunities_rating": 5,
  "ceo_rating": "APPROVE",
  "compensation_and_benefits_rating": 5,
  "culture_and_values_rating": 5,
  "diversity_and_inclusion_rating": 5,
  "recommend_to_friend_rating": "POSITIVE",
  "senior_management_rating": 5,
  "work_life_balance_rating": 5,
  "language": "eng",
  "page_count": 5764,
  "rating": 4.4,
  "review_count": 61951,
  "filtered_review_count": 57635,
  "rated_review_count": 61951
}
```
