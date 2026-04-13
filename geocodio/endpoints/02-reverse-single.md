# Single Reverse Geocoding | Geocodio API

## Overview

Convert a single latitude/longitude coordinate pair into a street address. Geocodio finds matching streets and determines the closest house number. This endpoint can return up to 5 possible matches ranked by accuracy score.

## Endpoint

```
GET https://api.geocod.io/v1.12/reverse
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | Yes | Latitude/longitude pair, comma-separated (e.g. `38.9002898,-76.9990361`) |
| `api_key` | string | Yes | Your Geocodio API key |
| `fields` | string | No | Additional data appends to request |
| `limit` | integer | No | Maximum number of results to return. Default is no limit. Set to `0` for no limit |
| `format` | string | No | JSON output format. `"simple"` is the only alternative value |
| `skipGeocoding` | boolean | No | When set to `true` (or empty value), skips reverse geocoding and applies field appends directly to the coordinates. The `fields` parameter is required when using this option. See [Skip Geocoding](12-skip-geocoding.md) |

### Distance Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `destinations[]` | string[] | Array of destination locations for distance calculation |
| `distance_mode` | string | `driving` or `straightline`. Default: `straightline` |
| `distance_units` | string | `miles` or `km`. Default: `miles` |
| `distance_max_results` | integer | Maximum number of destinations to return per result |
| `distance_max_distance` | number | Maximum distance filter (in specified units) |
| `distance_min_distance` | number | Minimum distance filter (in specified units) |
| `distance_max_duration` | integer | Maximum duration filter in seconds (driving mode only) |
| `distance_min_duration` | integer | Minimum duration filter in seconds (driving mode only) |
| `distance_order_by` | string | Sort destinations by `distance` or `duration`. Default: `distance` |
| `distance_sort_order` | string | `asc` or `desc`. Default: `asc` |

## Example Request

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.9002898,-76.9990361&api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "results": [
    {
      "address_components": {
        "number": "508",
        "street": "H",
        "suffix": "St",
        "postdirectional": "NE",
        "formatted_street": "H St NE",
        "city": "Washington",
        "county": "District of Columbia",
        "state": "DC",
        "zip": "20002",
        "country": "US"
      },
      "address_lines": [
        "508 H St NE",
        "",
        "Washington, DC 20002"
      ],
      "formatted_address": "508 H St NE, Washington, DC 20002",
      "location": {
        "lat": 38.900432,
        "lng": -76.999031
      },
      "accuracy": 1,
      "accuracy_type": "rooftop",
      "source": "City of Washington"
    },
    {
      "address_components": {
        "number": "510",
        "street": "H",
        "suffix": "St",
        "postdirectional": "NE",
        "formatted_street": "H St NE",
        "city": "Washington",
        "county": "District of Columbia",
        "state": "DC",
        "zip": "20002",
        "country": "US"
      },
      "address_lines": [
        "510 H St NE",
        "",
        "Washington, DC 20002"
      ],
      "formatted_address": "510 H St NE, Washington, DC 20002",
      "location": {
        "lat": 38.900429,
        "lng": -76.998965
      },
      "accuracy": 0.9,
      "accuracy_type": "rooftop",
      "source": "City of Washington"
    }
  ]
}
```

## Simple Format Response

When `format` is set to `simple`, only basic information for the best-matched result is returned. The `fields` parameter is still supported but `limit` has no effect.

```json
{
  "address": "508 H St NE, Washington, DC 20002",
  "lat": 38.900432,
  "lng": -76.999031,
  "accuracy": 1,
  "accuracy_type": "rooftop",
  "source": "Statewide"
}
```

When no results are found:

```json
{
  "address": null,
  "lat": null,
  "lng": null,
  "accuracy": null,
  "accuracy_type": null,
  "source": null
}
```

## Notes

- A geographic coordinate consists of latitude followed by longitude, separated by a comma (e.g. `38.9002898,-76.9990361`).
- Geocodio does not guarantee a valid house number -- it returns the closest approximation.
- Unit-level reverse geocoding is supported: after finding a rooftop-level match, Geocodio searches for the nearest unit within proximity and enhances the result with unit-level data when available.
