# Single Address Geocoding | Geocodio API

## Overview

Forward geocode a single address into geographic coordinates (latitude and longitude). Geocodio parses the address and appends additional information such as the city, state, and ZIP code. Results are ordered with the most accurate locations first.

## Endpoint

```
GET https://api.geocod.io/v1.12/geocode
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | Yes* | The address to geocode |
| `api_key` | string | Yes | Your Geocodio API key |
| `country` | string | No | Country to geocode in. Default is inferred from query, with a fallback to USA |
| `fields` | string | No | Additional data appends to request |
| `limit` | integer | No | Maximum number of results to return. Default is no limit. Set to `0` for no limit |
| `format` | string | No | JSON output format. Currently `"simple"` is the only alternative value |

*Required unless using alternative component parameters.

## Alternative Component Parameters

Instead of `q`, you can pass the address as individual components. This is recommended when the address is already parsed into separate fields.

| Parameter | Type | Description |
|-----------|------|-------------|
| `street` | string | E.g. `1600 Pennsylvania Ave NW` |
| `street2` | string | E.g. `Apt 204` |
| `city` | string | E.g. `Washington` |
| `county` | string | E.g. `Arlington` |
| `state` | string | E.g. `DC` |
| `postal_code` | string | E.g. `20500` |
| `country` | string | E.g. `Canada`, `Mexico` (default to USA) |

## Distance Parameters

When `destinations[]` is provided, each geocoded result includes a `destinations` array with distance and duration to each destination.

| Parameter | Type | Description |
|-----------|------|-------------|
| `destinations[]` | string[] | Array of destination locations. Each can be a coordinate string (`"lat,lng"` or `"lat,lng,id"`) or a geocodable address |
| `distance_mode` | string | `driving` (road network, includes duration) or `straightline` (great-circle, no duration). Default: `straightline` |
| `distance_units` | string | `miles` or `km`. Default: `miles` |
| `distance_max_results` | integer | Maximum number of destinations to return per geocoded result |
| `distance_max_distance` | number | Filter out destinations beyond this distance (in specified units) |
| `distance_min_distance` | number | Filter out destinations closer than this distance (in specified units) |
| `distance_max_duration` | integer | Filter out destinations with travel time exceeding this value in seconds (driving mode only) |
| `distance_min_duration` | integer | Filter out destinations with travel time below this value in seconds (driving mode only) |
| `distance_order_by` | string | Sort destinations by `distance` or `duration`. Default: `distance` |
| `distance_sort_order` | string | `asc` or `desc`. Default: `asc` |

## Examples

### Geocode using `q` parameter

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2c+Arlington+VA&api_key=YOUR_API_KEY"
```

### Geocode using individual address components

```bash
curl "https://api.geocod.io/v1.12/geocode?street=1109+N+Highland+St&city=Arlington&state=VA&api_key=YOUR_API_KEY"
```

### Geocode with distance calculation

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2c+Arlington+VA&destinations[]=38.8977,-77.0365,WhiteHouse&destinations[]=38.8895,-77.0353,WashingtonMonument&distance_mode=driving&api_key=YOUR_API_KEY"
```

### Geocode with unit/suite number

```bash
curl "https://api.geocod.io/v1.12/geocode?q=2800+Clarendon+Blvd+Suite+R500+Arlington+VA+22201&api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "input": {
    "address_components": {
      "number": "1109",
      "predirectional": "N",
      "street": "Highland",
      "suffix": "St",
      "formatted_street": "N Highland St",
      "city": "Arlington",
      "state": "VA",
      "zip": "22201",
      "country": "US"
    },
    "formatted_address": "1109 N Highland St, Arlington, VA 22201"
  },
  "results": [
    {
      "address_components": {
        "number": "1109",
        "predirectional": "N",
        "street": "Highland",
        "suffix": "St",
        "formatted_street": "N Highland St",
        "city": "Arlington",
        "county": "Arlington County",
        "state": "VA",
        "zip": "22201",
        "country": "US"
      },
      "address_lines": [
        "1109 N Highland St",
        "",
        "Arlington, VA 22201"
      ],
      "formatted_address": "1109 N Highland St, Arlington, VA 22201",
      "location": {
        "lat": 38.886665,
        "lng": -77.094733
      },
      "accuracy": 1,
      "accuracy_type": "rooftop",
      "source": "Virginia GIS Clearinghouse",
      "stable_address_key": "gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3"
    }
  ]
}
```

## Example Response with Distances

```json
{
  "input": {
    "address_components": {
      "number": "1109",
      "predirectional": "N",
      "street": "Highland",
      "suffix": "St",
      "formatted_street": "N Highland St",
      "city": "Arlington",
      "state": "VA",
      "zip": "22201",
      "country": "US"
    },
    "formatted_address": "1109 N Highland St, Arlington, VA 22201"
  },
  "results": [
    {
      "address_components": {
        "number": "1109",
        "predirectional": "N",
        "street": "Highland",
        "suffix": "St",
        "formatted_street": "N Highland St",
        "city": "Arlington",
        "county": "Arlington County",
        "state": "VA",
        "zip": "22201",
        "country": "US"
      },
      "formatted_address": "1109 N Highland St, Arlington, VA 22201",
      "location": {
        "lat": 38.886665,
        "lng": -77.094733
      },
      "accuracy": 1,
      "accuracy_type": "rooftop",
      "source": "Virginia GIS Clearinghouse",
      "destinations": [
        {
          "query": "38.8977,-77.0365,WhiteHouse",
          "id": "WhiteHouse",
          "location": [38.8977, -77.0365],
          "distance_miles": 3.8,
          "distance_km": 6.1,
          "duration_seconds": 720
        },
        {
          "query": "38.8895,-77.0353,WashingtonMonument",
          "id": "WashingtonMonument",
          "location": [38.8895, -77.0353],
          "distance_miles": 4.2,
          "distance_km": 6.8,
          "duration_seconds": 780
        }
      ]
    }
  ]
}
```

## Simple Format Response

When `format` is set to `simple`, a minimal JSON structure is returned with only the best-matched result. The `fields` parameter is still supported but the `limit` parameter has no effect.

```json
{
  "address": "1109 N Highland St, Arlington, VA 22201",
  "lat": 38.886665,
  "lng": -77.094733,
  "accuracy": 1,
  "accuracy_type": "rooftop",
  "source": "Arlington"
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

## Unit/Suite Number Handling

When a secondary address component is provided (apartment, suite, unit, etc.), Geocodio attempts to return unit-specific coordinates. If unit-level data is available, the unit-specific result is returned first with `match_type` set to `"unit"`, followed by the building-level result with `match_type` set to `"building_centroid"`.

The `secondaryunit` value is standardized based on USPS records for US addresses. For example, `#R500` is outputted as `Ste R500`.

To verify that a unit number is valid per USPS, request the `zip4` field append and check the `exact_match` value.

## Notes

- The `input` object in the response is cross-referenced with `results` for accuracy. It is not a one-for-one parsing of the original input.
- Results are always ordered with the most accurate locations first. It is safe to pick the first result.
- Geocodio supports geocoding of addresses, cities, and ZIP codes in various formats.
- See the Distance section for dedicated distance endpoints if you need distance calculations without geocoding.
