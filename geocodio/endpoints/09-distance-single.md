# Single Origin Distance | Geocodio API

## Overview

Calculate driving distance, driving time, and straight-line (great-circle/haversine) distance from a single origin to one or more destinations. Useful for finding the nearest locations to a given point. Supports up to 100 destinations per request.

To use the Distance API, you must enable access on an API key level via the Geocodio dashboard.

## Endpoint

```
GET https://api.geocod.io/v1.12/distance
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `origin` | string | Yes | The origin location (coordinate string, coordinate with ID, or geocodable address) |
| `destinations[]` | string[] | Yes | Array of destination locations (max 100 per request) |
| `api_key` | string | Yes | Your Geocodio API key |
| `mode` | string | No | `driving` or `straightline`. Default: `straightline` |
| `units` | string | No | `miles` or `km`. Default: `miles` |
| `max_results` | integer | No | Maximum number of destinations to return |
| `max_distance` | number | No | Filter out destinations beyond this distance (in specified units) |
| `min_distance` | number | No | Filter out destinations closer than this distance (in specified units) |
| `max_duration` | integer | No | Filter out destinations with travel time exceeding this value in seconds (driving mode only) |
| `min_duration` | integer | No | Filter out destinations with travel time below this value in seconds (driving mode only) |
| `order_by` | string | No | Sort destinations by `distance` or `duration`. Default: `distance` |
| `sort_order` | string | No | `asc` or `desc`. Default: `asc` |

## Location Formats

| Format | Example | Description |
|--------|---------|-------------|
| Coordinate string | `"38.8977,-77.0365"` | Latitude and longitude separated by a comma |
| Coordinate with ID | `"38.8977,-77.0365,DC"` | Includes a custom identifier returned in the response |
| Coordinate object | `{"lat": 38.8977, "lng": -77.0365, "id": "DC"}` | JSON object with `lat`, `lng`, and optional `id` |
| Address string | `"1600 Pennsylvania Ave NW, Washington DC"` | A geocodable address (geocoded automatically) |

When addresses are used, the geocoding result is included in the response under a `geocode` property and the lookup counts toward your geocoding credits.

## Calculation Modes

| Mode | Description | Duration Returned | Credit Multiplier |
|------|-------------|-------------------|-------------------|
| `straightline` | Great-circle distance (haversine) | No | 1x |
| `driving` | Driving distance and time via road networks | Yes | 2x |

## Example Request

```bash
curl "https://api.geocod.io/v1.12/distance?origin=38.8977,-77.0365,WhiteHouse&destinations[]=38.8895,-77.0353,WashingtonMonument&destinations[]=38.9072,-77.0369,DupontCircle&mode=driving&api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "mode": "driving",
  "origin": {
    "query": "38.8977,-77.0365,WhiteHouse",
    "id": "WhiteHouse",
    "location": [38.8977, -77.0365]
  },
  "destinations": [
    {
      "query": "38.8895,-77.0353,WashingtonMonument",
      "id": "WashingtonMonument",
      "location": [38.8895, -77.0353],
      "distance_miles": 0.6,
      "distance_km": 1.0,
      "duration_seconds": 180
    },
    {
      "query": "38.9072,-77.0369,DupontCircle",
      "id": "DupontCircle",
      "location": [38.9072, -77.0369],
      "distance_miles": 1.2,
      "distance_km": 1.9,
      "duration_seconds": 420
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

- Batch size is the total number of calculations (origins x destinations). Maximum 100 for this endpoint.
- The `driving` mode uses 2x the lookup credits of `straightline` mode.
- For larger calculations, use the distance matrix or distance jobs endpoints.
