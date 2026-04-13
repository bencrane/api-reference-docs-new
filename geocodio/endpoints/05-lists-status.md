# Check List Status | Geocodio API

## Overview

View the metadata and processing status for a single uploaded geocoding list. Use the list ID returned when the list was created.

## Endpoint

```
GET https://api.geocod.io/v1.12/lists/{id}
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The list ID (path parameter) |
| `api_key` | string | Yes | Your Geocodio API key |
| `page` | integer | No | The page number to show |

## Example Request

```bash
curl "https://api.geocod.io/v1.12/lists/42?api_key=YOUR_API_KEY"
```

## Status Values

| State | Description |
|-------|-------------|
| `PROCESSING` | The list is currently being geocoded |
| `COMPLETED` | Processing is finished and the list is ready for download |

## Example Response (Just Started)

```json
{
  "id": 42,
  "fields": [],
  "file": {
    "estimated_rows_count": 39809,
    "filename": "bigger_list.csv"
  },
  "status": {
    "state": "PROCESSING",
    "progress": 1,
    "message": "Processing",
    "time_left_description": "Estimating time to complete",
    "time_left_seconds": null
  },
  "download_url": null,
  "expires_at": "2021-09-23T18:23:29.000000Z"
}
```

## Example Response (In Progress)

```json
{
  "id": 42,
  "fields": [],
  "file": {
    "estimated_rows_count": 39809,
    "filename": "bigger_list.csv"
  },
  "status": {
    "state": "PROCESSING",
    "progress": 12.82,
    "message": "Geocoding",
    "time_left_description": "17 min. left",
    "time_left_seconds": 1072
  },
  "download_url": null,
  "expires_at": "2021-09-23T18:23:29.000000Z"
}
```

## Example Response (Completed)

```json
{
  "id": 42,
  "fields": [],
  "file": {
    "estimated_rows_count": 39809,
    "filename": "bigger_list.csv"
  },
  "status": {
    "state": "COMPLETED",
    "progress": 100,
    "message": "Completed",
    "time_left_description": null,
    "time_left_seconds": null
  },
  "download_url": "https://api.geocod.io/v1.12/lists/42/download",
  "expires_at": "2021-09-23T18:23:29.000000Z"
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | The list ID |
| `fields` | string[] | Requested field appends |
| `file.estimated_rows_count` | integer | Estimated number of rows in the uploaded file |
| `file.filename` | string | Original filename |
| `status.state` | string | Current processing state (`PROCESSING` or `COMPLETED`) |
| `status.progress` | number | Processing progress as a percentage (0-100) |
| `status.message` | string | Human-readable status message |
| `status.time_left_description` | string | Estimated time remaining, or `null` |
| `status.time_left_seconds` | integer | Estimated seconds remaining, or `null` |
| `download_url` | string | URL to download results when completed, or `null` |
| `expires_at` | string | ISO 8601 timestamp when the data will be automatically deleted |
