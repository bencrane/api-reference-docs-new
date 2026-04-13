# Distance Jobs (Async) | Geocodio API

## Overview

Create and manage asynchronous distance matrix jobs for large-scale distance calculations exceeding the synchronous limits. Jobs are processed in the background and results can be downloaded when complete. Maximum job size is 50,000 calculations (origins x destinations). Results are automatically deleted 72 hours after processing completes.

To use the Distance API, you must enable access on an API key level via the Geocodio dashboard.

---

## Create a Distance Job

### Endpoint

```
POST https://api.geocod.io/v1.12/distance-jobs
```

### URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |

### Request Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | A name for this distance matrix job (max 255 characters) |
| `origins` | array/integer | Yes | Array of origin locations, or an integer list ID from a previously uploaded spreadsheet |
| `destinations` | array/integer | Yes | Array of destination locations, or an integer list ID from a previously uploaded spreadsheet |
| `distance_mode` | string | No | `driving` or `straightline`. Default: `straightline` |
| `units` | string | No | `miles` or `km`. Default: `miles` |
| `max_results` | integer | No | Maximum number of destinations to return per origin |
| `max_distance` | number | No | Maximum distance filter (in specified units) |
| `min_distance` | number | No | Minimum distance filter (in specified units) |
| `max_duration` | integer | No | Maximum duration filter in seconds (driving mode only) |
| `min_duration` | integer | No | Minimum duration filter in seconds (driving mode only) |
| `order_by` | string | No | Sort destinations by `distance` or `duration`. Default: `distance` |
| `sort_order` | string | No | `asc` or `desc`. Default: `asc` |
| `fields` | string | No | Comma-separated list of data fields to append to geocoded results |
| `callback_url` | string | No | URL to receive a webhook notification when the job completes |

### Example Request

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Store to Customer Distances",
    "origins": [
      {"lat": 38.8977, "lng": -77.0365, "id": "Store1"},
      {"lat": 40.7128, "lng": -74.0060, "id": "Store2"}
    ],
    "destinations": [
      "39.80,-89.66,Customer1",
      "41.8781,-87.6298,Customer2",
      "34.0522,-118.2437,Customer3"
    ],
    "distance_mode": "driving",
    "max_results": 2,
    "order_by": "distance"
  }' \
  "https://api.geocod.io/v1.12/distance-jobs?api_key=YOUR_API_KEY"
```

### Example: Using List IDs

You can reference previously uploaded spreadsheets by their list ID instead of providing inline coordinates:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Warehouse Distances",
    "origins": 123,
    "destinations": 456,
    "distance_mode": "driving"
  }' \
  "https://api.geocod.io/v1.12/distance-jobs?api_key=YOUR_API_KEY"
```

### Example Response

```json
{
  "identifier": "abc123xyz",
  "name": "Store to Customer Distances",
  "status": "ENQUEUED",
  "created_at": "2026-01-06T10:30:00Z",
  "origins_type": "coordinates",
  "origins_count": 2,
  "destinations_type": "coordinates",
  "destinations_count": 3,
  "distance_mode": "driving",
  "total_calculations": 6,
  "calculations_completed": 0,
  "progress": 0,
  "is_expired": false
}
```

---

## Check Job Status

### Endpoint

```
GET https://api.geocod.io/v1.12/distance-jobs/{identifier}
```

### URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifier` | string | Yes | The job identifier returned when the job was created |
| `api_key` | string | Yes | Your Geocodio API key |

### Job Status Values

| Status | Description |
|--------|-------------|
| `ENQUEUED` | Job is waiting to be processed |
| `PROCESSING` | Job is currently being processed |
| `COMPLETED` | Job is complete, results available for download |
| `FAILED` | Job processing failed |

### Example Request

```bash
curl "https://api.geocod.io/v1.12/distance-jobs/abc123xyz?api_key=YOUR_API_KEY"
```

### Example Response (Processing)

```json
{
  "identifier": "abc123xyz",
  "name": "Store to Customer Distances",
  "status": "PROCESSING",
  "created_at": "2026-01-06T10:30:00Z",
  "origins_type": "coordinates",
  "origins_count": 2,
  "destinations_type": "coordinates",
  "destinations_count": 3,
  "distance_mode": "driving",
  "total_calculations": 6,
  "calculations_completed": 4,
  "progress": 66.67,
  "status_message": "Processing distance calculations",
  "time_left": "1 minute",
  "is_expired": false
}
```

### Example Response (Completed)

```json
{
  "identifier": "abc123xyz",
  "name": "Store to Customer Distances",
  "status": "COMPLETED",
  "created_at": "2026-01-06T10:30:00Z",
  "origins_type": "coordinates",
  "origins_count": 2,
  "destinations_type": "coordinates",
  "destinations_count": 3,
  "distance_mode": "driving",
  "total_calculations": 6,
  "calculations_completed": 6,
  "progress": 100,
  "download_url": "https://api.geocod.io/v1.12/distance-jobs/abc123xyz/download",
  "is_expired": false
}
```

---

## List All Distance Jobs

### Endpoint

```
GET https://api.geocod.io/v1.12/distance-jobs
```

### URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |
| `page` | integer | No | Page number for pagination (default: 1) |

### Example Request

```bash
curl "https://api.geocod.io/v1.12/distance-jobs?api_key=YOUR_API_KEY"
```

### Example Response

```json
{
  "data": [
    {
      "identifier": "abc123xyz",
      "name": "Store to Customer Distances",
      "status": "COMPLETED",
      "created_at": "2026-01-06T10:30:00Z",
      "total_calculations": 6,
      "progress": 100,
      "is_expired": false
    }
  ],
  "links": {
    "first": "https://api.geocod.io/v1.12/distance-jobs?page=1",
    "last": "https://api.geocod.io/v1.12/distance-jobs?page=1",
    "prev": null,
    "next": null
  },
  "meta": {
    "current_page": 1,
    "last_page": 1,
    "per_page": 20,
    "total": 1
  }
}
```

---

## Download Job Results

### Endpoint

```
GET https://api.geocod.io/v1.12/distance-jobs/{identifier}/download
```

### URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifier` | string | Yes | The job identifier |
| `api_key` | string | Yes | Your Geocodio API key |

### Example Request

```bash
curl "https://api.geocod.io/v1.12/distance-jobs/abc123xyz/download?api_key=YOUR_API_KEY" \
  -o results.json
```

Results are only available when the job status is `COMPLETED`. The response format matches the distance matrix endpoint. Results expire 72 hours after processing completes.

---

## Delete a Distance Job

### Endpoint

```
DELETE https://api.geocod.io/v1.12/distance-jobs/{identifier}
```

### URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `identifier` | string | Yes | The job identifier |
| `api_key` | string | Yes | Your Geocodio API key |

### Example Request

```bash
curl -X DELETE "https://api.geocod.io/v1.12/distance-jobs/abc123xyz?api_key=YOUR_API_KEY"
```

### Example Response

```json
{
  "message": "Distance matrix job deleted successfully"
}
```
