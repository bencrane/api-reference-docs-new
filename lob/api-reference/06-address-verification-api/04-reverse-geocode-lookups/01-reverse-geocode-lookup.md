# Reverse Geocode Lookup

Reverse geocode a valid US location with a live API key.

## AUTHORIZATIONS

`basicAuth`

## QUERY PARAMETERS

### `size`
- **Type:** integer [ 1 .. 50 ]
- **Default:** `5`
- **Example:** `size=5`

Determines the number of locations returned. Possible values are between 1 and 50 and any number higher will be rounded down to 50. Default size is a list of 5 reverse geocoded locations.

## REQUEST BODY SCHEMA

`application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `latitude` | number or null (float) [ -90 .. 90 ] | Yes | A positive or negative decimal indicating the geographic latitude of the address, specifying the north-to-south position of a location. This should be input with `longitude` to pinpoint locations on a map. |
| `longitude` | number or null (float) [ -180 .. 180 ] | Yes | A positive or negative decimal indicating the geographic longitude of the address, specifying the north-to-south position of a location. This should be input with `latitude` to pinpoint locations on a map. |

## Responses

### 200 — Returns a zip lookup object if a valid zip was provided.

#### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string (`^us_reverse_geocode_[a-zA-Z0-9_]+$`) | Unique identifier prefixed with `us_reverse_geocode_`. |
| `addresses` | Array of objects | List of addresses. |
| `object` | string | Default: `"us_reverse_geocode_lookup"`. Value is resource type. |

### default — Error

---

## Endpoint

`POST /us_reverse_geocode_lookups`

## Request Sample

**Content type:** `application/json`

```json
{
  "latitude": 37.7749,
  "longitude": 122.4194
}
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "us_reverse_geocode_8a013f3e",
  "addresses": [
    {
      "components": {},
      "location_analysis": {}
    },
    {
      "components": {},
      "location_analysis": {}
    }
  ]
}
```