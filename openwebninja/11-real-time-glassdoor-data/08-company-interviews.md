# Company Interviews

`GET /company-interviews`

Get interviews made by the company, including questions, difficulty, outcome, and more data about interviews.

## Query Parameters

| Parameter | Type | Required | Constraints | Default | Description |
|-----------|------|----------|-------------|---------|-------------|
| `company_id` | string | Yes | — | — | Company ID. |
| `page` | number | No | — | `1` | The reviews page to return (each page includes up to 10 results). |
| `page_size` | number | No | min: 1, max: 100 | `10` | Maximum interview results to return in each page. **Note:** when `page > 1000`, only 5 items are returned per page (higher `page_size` values are overridden) — this is due to Glassdoor's behavior. |
| `sort` | string (enum) | No | — | `POPULAR` | Return interviews in a specific sort order. |
| `job_function` | string (enum) | No | — | `ANY` | Return interviews for a specific job function. |
| `job_title` | string | No | — | — | Return interviews with job title matching a search query. |
| `location` | string | No | — | — | The location for which to get interviews (e.g. `San-Francisco`). |
| `location_type` | string (enum) | No | — | `ANY` | Specify the type of the location you are looking to get salary estimation for additional accuracy. |
| `received_offer_only` | boolean | No | — | — | Only return interviews that resulted in an offer to the candidate. |
| `domain` | string (enum) | No | — | `www.glassdoor.com` | The Glassdoor domain to use. |

### `sort` enum values

```
POPULAR
MOST_RECENT
OLDEST
EASIEST
MOST_DIFFICULT
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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-interviews?company_id=1138' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`, truncated)

```json
{
  "status": "OK",
  "request_id": "3040ccad-c557-4b37-83d3-451459447a71",
  "parameters": {
    "domain": "www.glassdoor.com",
    "location_type": "ANY",
    "page": 1,
    "sort": "RELEVANCE",
    "received_offer_only": false
  },
  "data": {
    "interviews": [
      {
        "interview_id": 103064613,
        "job_title": "Software Engineer",
        "location": "Waterloo, ON",
        "review_datetime": "2026-03-06T06:01:11.547Z",
        "interview_datetime": null,
        "process_description": "The process typically starts with an Online Assessment (OA) — 2 coding questions (LeetCode Medium/Hard) plus a behavioral MCQ section within 60 minutes. Followed by a 45-minute technical phone screen with live coding.\n",
        "difficulty": "average",
        "experience": "positive",
        "outcome": "accept_offer",
        "duration_days": null,
        "is_current_employee": true,
        "helpful_count": 0,
        "not_helpful_count": 0,
        "advice": null,
        "declined_reason": null,
        "negotiation_description": null,
        "questions": [
          "Can you overlook small, but important, errors in your work"
        ]
      }
    ],
    "total_count": 25276,
    "filtered_count": 25276,
    "page_count": 2528,
    "current_page": 1,
    "newest_review_date": "2026-03-06T15:49:26.527Z",
    "interview_question_count": 25889,
    "interview_difficulty": 3.4,
    "interview_experience_counts": {
      "POSITIVE": 15645,
      "NEGATIVE": 3134,
      "NEUTRAL": 5848
    },
    "interview_obtained_channel_counts": {
      "RECRUITER": 3355,
      "OTHER": 379,
      "EMPLOYEE_REFERRAL": 3187,
      "COLLEGE": 1306,
      "IN_PERSON": 258,
      "APPLIED_ONLINE": 8404,
      "STAFFING_AGENCY": 238
    }
  }
}
```
