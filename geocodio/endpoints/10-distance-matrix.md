# Distance Matrix | Geocodio API

## Overview

Calculate driving distance, driving time, and straight-line distance between multiple origins and multiple destinations (many-to-many). Useful for route optimization, coverage analysis, and logistics planning. The matrix size (origins x destinations) is limited to 10,000 calculations per request.

To use the Distance API, you must enable access on an API key level via the Geocodio dashboard.

## Endpoint

```
POST https://api.geocod.io/v1.12/distance-matrix
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |

## Request Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `origins` | array | Yes | Array of origin locations |
| `destinations` | array | Yes | Array of destination locations |
| `mode` | string | No | `driving` or `straightline`. Default: `straightline` |
| `units` | string | No | `miles` or `km`. Default: `miles` |
| `max_results` | integer | No | Maximum number of destinations to return per origin |
| `max_distance` | number | No | Maximum distance filter (in specified units) |
| `min_distance` | number | No | Minimum distance filter (in specified units) |
| `max_duration` | integer | No | Maximum duration filter in seconds (driving mode only) |
| `min_duration` | integer | No | Minimum duration filter in seconds (driving mode only) |
| `order_by` | string | No | Sort destinations by `distance` or `duration`. Default: `distance` |
| `sort_order` | string | No | `asc` or `desc`. Default: `asc` |

Origins and destinations accept the same location formats as the single origin distance endpoint: coordinate strings, coordinate strings with IDs, coordinate objects, and address strings.

## Example Request

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "origins": [
      "38.8977,-77.0365,DC",
      "40.7128,-74.0060,NYC"
    ],
    "destinations": [
      "39.80,-89.66,Springfield",
      "41.8781,-87.6298,Chicago"
    ],
    "mode": "driving"
  }' \
  "https://api.geocod.io/v1.12/distance-matrix?api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "mode": "driving",
  "results": [
    {
      "origin": {
        "query": "38.8977,-77.0365,DC",
        "id": "DC",
        "location": [38.8977, -77.0365]
      },
      "destinations": [
        {
          "query": "39.80,-89.66,Springfield",
          "id": "Springfield",
          "location": [39.80, -89.66],
          "distance_miles": 699.2,
          "distance_km": 1125.3,
          "duration_seconds": 36540
        },
        {
          "query": "41.8781,-87.6298,Chicago",
          "id": "Chicago",
          "location": [41.8781, -87.6298],
          "distance_miles": 695.2,
          "distance_km": 1118.9,
          "duration_seconds": 36000
        }
      ]
    },
    {
      "origin": {
        "query": "40.7128,-74.0060,NYC",
        "id": "NYC",
        "location": [40.7128, -74.0060]
      },
      "destinations": [
        {
          "query": "39.80,-89.66,Springfield",
          "id": "Springfield",
          "location": [39.80, -89.66],
          "distance_miles": 876.5,
          "distance_km": 1410.6,
          "duration_seconds": 45900
        },
        {
          "query": "41.8781,-87.6298,Chicago",
          "id": "Chicago",
          "location": [41.8781, -87.6298],
          "distance_miles": 790.1,
          "distance_km": 1271.5,
          "duration_seconds": 41400
        }
      ]
    }
  ]
}
```

## Response Headers

| Header | Description |
|--------|-------------|
| `X-BILLABLE-DISTANCE-CALCULATIONS` | Number of distance calculations billed for this request |
| `X-BILLABLE-LOOKUPS-COUNT` | Number of geocode lookups performed (only present if addresses were geocoded) |

## Notes

- The matrix size limit is 10,000 calculations (origins x destinations) per request.
- For larger matrices, use the asynchronous distance jobs endpoint.
- The `driving` mode uses 2x the lookup credits of `straightline` mode.
