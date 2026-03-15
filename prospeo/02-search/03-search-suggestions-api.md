# Search Suggestions API

## Job and Location Suggestions

This endpoint allows you to retrieve suggestions for job titles or locations to use in your search filters.

Use this endpoint to find valid values for the `person_location`, `company_location`, or `person_job_title` filters when using our Search Person or Search Company APIs.

This endpoint is FREE and does not consume any credits.

## Rate limit

This endpoint has a special rate limit of 15 requests/second per account. This rate limit is the same across all plans (FREE, STARTER, GROWTH, PRO).

## Endpoint

* **URL:** `https://api.prospeo.io/search-suggestions`
* **Method:** `POST`
* **Headers:**
  * `X-KEY: your_api_key`
  * `Content-Type: application/json`

## Parameters

You must provide exactly one of the following parameters. Providing both or neither will result in an error.

| Parameter | Example value | Description |
|-----------|--------------|-------------|
| `location_search` (optional) | `united states` | A search query to find location suggestions. Minimum 2 characters. |
| `job_title_search` (optional) | `software engineer` | A search query to find job title suggestions. Minimum 2 characters. |

## Request examples

### Location search

```bash
curl --location 'https://api.prospeo.io/search-suggestions' \
--header 'X-KEY: your_api_key' \
--header 'Content-Type: application/json' \
--data '{
    "location_search": "united states"
}'
```

### Job title search

```bash
curl --location 'https://api.prospeo.io/search-suggestions' \
--header 'X-KEY: your_api_key' \
--header 'Content-Type: application/json' \
--data '{
    "job_title_search": "software engineer"
}'
```

## Response: Location search

When searching for locations, the response will contain an array of location suggestions with their type.

```json
{
    "error": false,
    "location_suggestions": [
        {"name": "United States", "type": "COUNTRY"},
        {"name": "California, United States", "type": "STATE"},
        {"name": "Los Angeles, California, United States", "type": "CITY"},
        {"name": "Greater Los Angeles Area", "type": "ZONE"}
    ],
    "job_title_suggestions": null
}
```

### Location types

| Type | Description | Examples |
|------|-------------|----------|
| `COUNTRY` | Countries | "United States", "France", "Germany" |
| `STATE` | States, provinces, or regions | "California", "Ontario", "Bavaria" |
| `CITY` | Cities | "New York", "Paris", "Tokyo" |
| `ZONE` | Metropolitan or greater areas | "Greater Toronto Area", "San Francisco Bay Area" |

## Response: Job title search

When searching for job titles, the response will contain an array of job title suggestions as plain strings.

```json
{
    "error": false,
    "location_suggestions": null,
    "job_title_suggestions": [
        "software engineer",
        "senior software engineer",
        "software engineering manager",
        "software developer",
        "lead software engineer"
    ]
}
```

Job title suggestions return up to 25 results, ordered by popularity (most common titles first).

## Response details

| Property | Type | Description |
|----------|------|-------------|
| `error` | boolean | Indicates if an error has occurred. If `false`, the request was successful. If `true`, an error has occurred and a `error_code` property will be present. See below. |
| `location_suggestions` | list \| null | Contains location suggestions when using `location_search`. Each item has a `name` and `type` property. `null` when searching for job titles. |
| `job_title_suggestions` | list \| null | Contains job title suggestions when using `job_title_search`. Returns plain strings. `null` when searching for locations. |

## Error codes

| HTTP code | `error_code` property | Meaning |
|-----------|----------------------|---------|
| 400 | `INVALID_REQUEST` | Invalid request. Either: you must provide exactly one of `location_search` or `job_title_search` (not both, not neither), or the search query must be at least 2 characters. |
| 401 | `INVALID_API_KEY` | Invalid API key, check your `X-KEY` header. |
| 429 | `RATE_LIMITED` | You hit the rate limit (15 requests/second). |
| 400 | `INTERNAL_ERROR` | An error occurred on our side, please contact the support. |