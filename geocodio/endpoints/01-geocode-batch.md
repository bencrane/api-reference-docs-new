# Batch Forward Geocoding | Geocodio API

## Overview

Geocode up to 10,000 addresses in a single request. Batch geocoding removes the overhead of multiple HTTP requests and is significantly faster for bulk operations. Results can be submitted as a JSON array or a JSON object with custom keys.

## Endpoint

```
POST https://api.geocod.io/v1.12/geocode
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |
| `fields` | string | No | Additional field appends to request |
| `limit` | integer | No | Maximum number of results to return per address. Default is no limit. Set to `0` for no limit |
| `destinations[]` | string[] | No | Array of destination locations for distance calculation |
| `distance_mode` | string | No | `driving` or `straightline`. Default: `straightline` |
| `distance_units` | string | No | `miles` or `km`. Default: `miles` |
| `distance_max_results` | integer | No | Maximum number of destinations to return per geocoded result |
| `distance_max_distance` | number | No | Maximum distance filter (in specified units) |
| `distance_min_distance` | number | No | Minimum distance filter (in specified units) |
| `distance_max_duration` | integer | No | Maximum duration filter in seconds (driving mode only) |
| `distance_min_duration` | integer | No | Minimum duration filter in seconds (driving mode only) |
| `distance_order_by` | string | No | Sort destinations by `distance` or `duration`. Default: `distance` |
| `distance_sort_order` | string | No | `asc` or `desc`. Default: `asc` |

## Request Body

The POST body can be either a JSON array of address strings or a JSON object with custom keys.

### JSON Array Format

Pass an array of address strings. Results are guaranteed to be returned in the same order as requested.

```json
[
  "1109 N Highland St, Arlington VA",
  "525 University Ave, Toronto, ON, Canada",
  "4410 S Highway 17 92, Casselberry FL",
  "15000 NE 24th Street, Redmond WA",
  "17015 Walnut Grove Drive, Morgan Hill CA"
]
```

### JSON Object Format

Pass an object with custom keys for each address. This is useful for matching results back to your existing data.

```json
{
  "FID1": "1109 N Highland St, Arlington VA",
  "FID2": "525 University Ave, Toronto, ON, Canada",
  "FID3": "4410 S Highway 17 92, Casselberry FL",
  "FID4": "15000 NE 24th Street, Redmond WA",
  "FID5": "17015 Walnut Grove Drive, Morgan Hill CA"
}
```

### JSON Object with Component Parameters

You can also pass addresses as individual components instead of strings.

```json
{
  "1": {
    "street": "1109 N Highland St",
    "city": "Arlington",
    "state": "VA"
  },
  "2": {
    "city": "Toronto",
    "country": "CA"
  }
}
```

### Accepted Address Components

| Parameter | Description |
|-----------|-------------|
| `street` | E.g. `1600 Pennsylvania Ave NW` |
| `street2` | E.g. `Apt 204` |
| `city` | E.g. `Washington` |
| `county` | E.g. `Arlington` |
| `state` | E.g. `DC` |
| `postal_code` | E.g. `20500` |
| `country` | E.g. `Canada`, `Mexico` (default to USA) |

## Understanding Lookup Counts

Each address counts as one lookup, and each field append counts as an additional lookup per address.

```
Total Lookups = Number of Addresses x (1 + Number of Fields)
```

Examples within the 10,000 limit:
- 10,000 addresses, no fields = 10,000 lookups
- 5,000 addresses, 1 field = 10,000 lookups (5,000 x 2)
- 2,500 addresses, 3 fields = 10,000 lookups (2,500 x 4)

Examples exceeding the limit:
- 10,000 addresses, 1 field = 20,000 lookups (exceeds limit)
- 6,000 addresses, 2 fields = 18,000 lookups (exceeds limit)

For requests exceeding 10,000 lookups, split into multiple batches or use the Lists API.

## Example Request

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '["1109 N Highland St, Arlington VA", "525 University Ave, Toronto, ON, Canada", "4410 S Highway 17 92, Casselberry FL", "15000 NE 24th Street, Redmond WA", "17015 Walnut Grove Drive, Morgan Hill CA"]' \
  "https://api.geocod.io/v1.12/geocode?api_key=YOUR_API_KEY"
```

## Example Response (JSON Array)

When the request body is a JSON array, the response contains a `results` array where each element has a `query` and `response` pair.

```json
{
  "results": [
    {
      "query": "1109 N Highland St, Arlington VA",
      "response": {
        "input": {
          "address_components": {
            "number": "1109",
            "predirectional": "N",
            "street": "Highland",
            "suffix": "St",
            "formatted_street": "N Highland St",
            "city": "Arlington",
            "state": "VA",
            "country": "US"
          },
          "formatted_address": "1109 N Highland St, Arlington, VA"
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
              "lat": 38.886672,
              "lng": -77.094735
            },
            "accuracy": 1,
            "accuracy_type": "rooftop",
            "source": "Arlington"
          }
        ]
      }
    },
    {
      "query": "525 University Ave, Toronto, ON, Canada",
      "response": {
        "input": {
          "address_components": {
            "number": "525",
            "street": "University",
            "suffix": "Ave",
            "formatted_street": "University Ave",
            "city": "Toronto",
            "state": "ON",
            "country": "CA"
          },
          "formatted_address": "525 University Ave, Toronto, ON"
        },
        "results": [
          {
            "address_components": {
              "number": "525",
              "street": "University",
              "suffix": "Ave",
              "formatted_street": "University Ave",
              "city": "Toronto",
              "state": "ON",
              "country": "CA"
            },
            "address_lines": [
              "525 University Ave",
              "",
              "Toronto, ON M5G"
            ],
            "formatted_address": "525 University Ave, Toronto, ON",
            "location": {
              "lat": 43.656258,
              "lng": -79.388223
            },
            "accuracy": 1,
            "accuracy_type": "rooftop",
            "source": "City of Toronto Open Data"
          }
        ]
      }
    }
  ]
}
```

## Example Response (JSON Object)

When the request body is a JSON object, the response `results` is an object keyed by your custom keys.

```json
{
  "results": {
    "FID1": {
      "query": "1109 N Highland St, Arlington VA",
      "response": {
        "input": {
          "address_components": {
            "number": "1109",
            "predirectional": "N",
            "street": "Highland",
            "suffix": "St",
            "formatted_street": "N Highland St",
            "city": "Arlington",
            "state": "VA",
            "country": "US"
          },
          "formatted_address": "1109 N Highland St, Arlington, VA"
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
              "lat": 38.886672,
              "lng": -77.094735
            },
            "accuracy": 1,
            "accuracy_type": "rooftop",
            "source": "Arlington"
          }
        ]
      }
    },
    "FID2": { "..." : "..." },
    "FID3": { "..." : "..." }
  }
}
```

## Notes

- Geocoding 10,000 lookups takes approximately 600 seconds. Adjust your HTTP timeout accordingly.
- When using a JSON array, results are returned in the same order as the input.
- For very large lists, consider using the Lists API instead of the batch endpoint.
