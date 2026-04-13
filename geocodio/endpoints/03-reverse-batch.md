# Batch Reverse Geocoding | Geocodio API

## Overview

Reverse geocode up to 10,000 coordinate pairs in a single request. Batch reverse geocoding removes the overhead of multiple HTTP requests and is significantly faster for bulk operations.

## Endpoint

```
POST https://api.geocod.io/v1.12/reverse
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |
| `fields` | string | No | Additional field appends to request |
| `limit` | integer | No | Maximum number of results to return per coordinate. Default is no limit. Set to `0` for no limit |
| `destinations[]` | string[] | No | Array of destination locations for distance calculation |
| `distance_mode` | string | No | `driving` or `straightline`. Default: `straightline` |
| `distance_units` | string | No | `miles` or `km`. Default: `miles` |
| `distance_max_results` | integer | No | Maximum number of destinations to return per result |
| `distance_max_distance` | number | No | Maximum distance filter (in specified units) |
| `distance_min_distance` | number | No | Minimum distance filter (in specified units) |
| `distance_max_duration` | integer | No | Maximum duration filter in seconds (driving mode only) |
| `distance_min_duration` | integer | No | Minimum duration filter in seconds (driving mode only) |
| `distance_order_by` | string | No | Sort destinations by `distance` or `duration`. Default: `distance` |
| `distance_sort_order` | string | No | `asc` or `desc`. Default: `asc` |
| `skipGeocoding` | boolean | No | When set to `true`, skips reverse geocoding and applies field appends directly to the coordinates. Requires `fields` parameter |

## Request Body

Post a JSON array of coordinate strings. Each coordinate is a latitude/longitude pair separated by a comma.

```json
[
  "35.9746000,-77.9658000",
  "32.8793700,-96.6303900",
  "33.8337100,-117.8362320",
  "35.4171240,-80.6784760"
]
```

## Example Request

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '["35.9746000,-77.9658000","32.8793700,-96.6303900","33.8337100,-117.8362320","35.4171240,-80.6784760"]' \
  "https://api.geocod.io/v1.12/reverse?api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "results": [
    {
      "query": "35.9746000,-77.9658000",
      "response": {
        "results": [
          {
            "address_components": {
              "number": "101",
              "predirectional": "W",
              "street": "Washington",
              "suffix": "St",
              "formatted_street": "W Washington St",
              "city": "Nashville",
              "county": "Nash County",
              "state": "NC",
              "zip": "27856",
              "country": "US"
            },
            "address_lines": [
              "101 W Washington St",
              "",
              "Nashville, NC 27856"
            ],
            "formatted_address": "101 W Washington St, Nashville, NC 27856",
            "location": {
              "lat": 35.974357,
              "lng": -77.966064
            },
            "accuracy": 1,
            "accuracy_type": "rooftop",
            "source": "NC Geographic Information Coordinating Council"
          }
        ]
      }
    },
    {
      "query": "32.8793700,-96.6303900",
      "response": {
        "results": [
          {
            "address_components": {
              "number": "3034",
              "predirectional": "S",
              "street": "1st",
              "suffix": "St",
              "formatted_street": "S 1st St",
              "city": "Garland",
              "county": "Dallas County",
              "state": "TX",
              "zip": "75041",
              "country": "US"
            },
            "address_lines": [
              "3034 S 1st St",
              "",
              "Garland, TX 75041"
            ],
            "formatted_address": "3034 S 1st St, Garland, TX 75041",
            "location": {
              "lat": 32.879386,
              "lng": -96.630471
            },
            "accuracy": 1,
            "accuracy_type": "rooftop",
            "source": "City of Garland"
          }
        ]
      }
    }
  ]
}
```

## Notes

- You can batch reverse geocode up to 10,000 coordinates at a time.
- Field appends count as lookups. Keep the overall number of lookups at 10,000 or below.
- Each result includes the original `query` coordinate string alongside the `response` for easy matching.
