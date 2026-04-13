# Show All Lists | Geocodio API

## Overview

Retrieve a paginated list of all geocoding lists that have been created. Lists are ordered by recency, showing 15 per page.

## Endpoint

```
GET https://api.geocod.io/v1.12/lists
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |

## Example Request

```bash
curl "https://api.geocod.io/v1.12/lists?api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "current_page": 1,
  "data": [
    {
      "id": 48,
      "fields": [],
      "file": {
        "estimated_rows_count": 24,
        "filename": "sample_list.csv"
      },
      "status": {
        "state": "COMPLETED",
        "progress": 100,
        "message": "Completed",
        "time_left_description": null,
        "time_left_seconds": null
      },
      "download_url": "https://api.geocod.io/v1.12/lists/48/download",
      "expires_at": "2021-09-23T12:09:09.000000Z"
    }
  ],
  "first_page_url": "https://api.geocod.io/v1.12/lists?page=1",
  "from": 1,
  "next_page_url": "https://api.geocod.io/v1.12/lists?page=2",
  "path": "https://api.geocod.io/v1.12/lists",
  "per_page": 15,
  "prev_page_url": null,
  "to": 15
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `current_page` | integer | Current page number |
| `data` | array | Array of list objects |
| `first_page_url` | string | URL to the first page |
| `from` | integer | Starting record index on this page |
| `next_page_url` | string | URL to the next page, or `null` if on the last page |
| `path` | string | Base URL path |
| `per_page` | integer | Number of records per page (15) |
| `prev_page_url` | string | URL to the previous page, or `null` if on the first page |
| `to` | integer | Ending record index on this page |

Each list object in the `data` array contains the same fields as the single list status response (see [Check List Status](05-lists-status.md)).
