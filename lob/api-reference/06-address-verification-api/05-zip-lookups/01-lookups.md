# Zip Lookups

Find a list of cities, states and associated information about a US ZIP code.

## Lookups

Returns information about a ZIP code.

### AUTHORIZATIONS

`basicAuth`

### REQUEST BODY SCHEMA

`application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `zip_code` | string (`^\d{5}$`) | Yes | A 5-digit ZIP code. |

### Responses

#### 200 — Returns a zip lookup object if a valid zip was provided.

##### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

##### RESPONSE SCHEMA: `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `zip_code` | string (`^\d{5}$`) | Yes | A 5-digit ZIP code. |
| `id` | string (`^us_zip_[a-zA-Z0-9]+$`) | Yes | Unique identifier prefixed with `us_zip_`. |
| `cities` | Array of objects (`zip_lookup_city`) | Yes | An array of city objects containing valid cities for the `zip_code`. Multiple cities will be returned if more than one city is associated with the input ZIP code. |
| `zip_code_type` | string | Yes | Enum: `"standard"`, `"po_box"`, `"unique"`, `"military"`, `""`. A description of the ZIP code type. For more detailed information about each ZIP code type, see US Verification Details. |
| `object` | string | Yes | Default: `"us_zip_lookup"`. Value is resource type. |

#### default — Error

---

### Endpoint

`POST /us_zip_lookups`

### Request Sample

**Content type:** `application/json`

```json
{
  "zip_code": "94107"
}
```

### Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "us_zip_c7cb63d68f8d6",
  "cities": [
    {
      "city": "SAN FRANCISCO",
      "state": "CA",
      "county": "SAN FRANCISCO",
      "county_fips": "06075",
      "preferred": true
    }
  ],
  "zip_code_type": "standard",
  "object": "us_zip_lookup",
  "zip_code": "94107"
}
```