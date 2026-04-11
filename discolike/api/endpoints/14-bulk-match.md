# Bulk Match API [Team]

## Overview

The Bulk Match API enables matching a CSV file of company names to domain profiles through asynchronous processing, returning one best match per row.

## Endpoint

```
POST https://api.discolike.com/v1/bulkmatch
```

## Parameters

Submit CSV data using `Content-Type: multipart/form-data` with these optional fields:

| Parameter | Description |
|-----------|-------------|
| name_column | Column with company names (required) |
| country_column | Column with country codes |
| state_column | Column with state codes |
| city_column | Column with city names |
| zip_code_column | Column with zip codes |
| phone_column | Column with phone numbers |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| status | String | `in_progress`, `completed`, or `failed` |
| progress | Integer | Progress percentage |
| results | Array | BizData profiles with `input:` prefix |
| match_confidence | Integer | Match confidence 0-100 |

## Example Request

```bash
curl --form file='@data.csv' \
  "https://api.discolike.com/v1/bulkmatch?name_column=name" \
  -H "x-discolike-key: API_KEY"
```

## Initial Response

```json
{ "task_id": "e362cb75-35e2-4006-a239-3d87a7472872" }
```

## Check Status

```bash
curl "https://api.discolike.com/v1/bulkmatch/status/{task_id}" \
  -H "x-discolike-key: API_KEY"
```

```json
{ "status": "in_progress", "progress": 30 }
```

## Final Response

```json
{
  "status": "completed",
  "progress": 100,
  "results": [
    {
      "input:name": "acme software",
      "domain": "acmesoftware.com",
      "match_confidence": 100,
      "name": "Acme Software Inc"
    }
  ]
}
```
