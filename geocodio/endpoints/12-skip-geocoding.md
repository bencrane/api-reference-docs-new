# Skip Geocoding (Field Data from Coordinates) | Geocodio API

## Overview

The `skipGeocoding` parameter allows you to skip the reverse geocoding step entirely and apply field appends directly to supplied coordinates. This is useful when:

- You already have geocoded coordinates and only need field append data (e.g. timezone, census, congressional districts) without paying for the geocoding lookup again.
- You have coordinates that do not correspond to a street address (e.g. a point in a national park or body of water) and want to determine what geographic boundaries they fall within.

When `skipGeocoding` is set, no geocoding lookup is billed -- only field appends are counted.

## Endpoint

This feature is used via the reverse geocoding endpoint with the `skipGeocoding` query parameter.

```
GET https://api.geocod.io/v1.12/reverse
```

For batch requests:

```
POST https://api.geocod.io/v1.12/reverse
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | Yes | Latitude/longitude pair, comma-separated (e.g. `38.9002898,-76.9990361`) |
| `skipGeocoding` | boolean | Yes | Set to `true` or include as an empty-value parameter |
| `fields` | string | Yes | Required when using `skipGeocoding`. The field appends to request (e.g. `timezone`, `census`, `cd`) |
| `api_key` | string | Yes | Your Geocodio API key |

## Example Request

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.9002898,-76.9990361&skipGeocoding&fields=timezone&api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "results": [
    {
      "location": {
        "lat": 38.9002898,
        "lng": -76.9990361
      },
      "accuracy_type": "coordinate",
      "fields": {
        "timezone": {
          "name": "America/New_York",
          "utc_offset": -5,
          "observes_dst": true,
          "abbreviation": "EST",
          "source": "\u00a9 IANA Time Zone Database"
        }
      }
    }
  ]
}
```

## Response Structure

The response when using `skipGeocoding` is simplified compared to a standard reverse geocoding response:

| Field | Type | Description |
|-------|------|-------------|
| `location.lat` | number | The latitude from the input |
| `location.lng` | number | The longitude from the input |
| `accuracy_type` | string | Always set to `"coordinate"` |
| `fields` | object | The requested field append data |

No address components or address data is returned.

## Notes

- The `fields` parameter is required when using `skipGeocoding`.
- `skipGeocoding` is supported for both single and batch reverse geocoding requests.
- Only field appends are billed; no geocoding lookup charges apply.
