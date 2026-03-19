# Identity Validation

Validates whether a given name is associated with an address.

## AUTHORIZATIONS

`basicAuth`

## REQUEST BODY SCHEMA: `application/json`

One of `recipient_input` / `company_input`

Any of: Address object with `city` and `state` / Address object with `zip_code`

### Required Fields

| Field | Type | Description |
|---|---|---|
| `city` | string (<= 200 chars) | The name of the city. `city` and `state` are required if no `zip_code` is passed. |
| `state` | string (<= 50 chars) | The ISO 3166-2 two letter code or subdivision name for the state. `city` and `state` are required if no `zip_code` is passed. |
| `recipient` | string or null (<= 500 chars) | The intended recipient, typically a person's or firm's name. |
| `primary_line` | string (<= 200 chars) | The primary delivery line (usually the street address) of the address. Combination of: `primary_number`, `street_predirection`, `street_name`, `street_suffix`, `street_postdirection`, `secondary_designator`, `secondary_number`, `pmb_designator`, `pmb_number`. |

### Optional Fields

| Field | Type | Description |
|---|---|---|
| `secondary_line` | string (<= 200 chars) | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long. |
| `urbanization` | string (<= 200 chars) | Only present for addresses in Puerto Rico. An urbanization refers to an area, sector, or development within a city. See USPS documentation for clarification. |
| `zip_code` | string (`^\d{5}((-)?\d{4})?$`) | Required if `city` and `state` are not passed in. If included, must be formatted as a US ZIP or ZIP+4 (e.g. `94107`, `941072282`, `94107-2282`). |

## Responses

### 200 — Returns the likelihood a given name is associated with an address.

#### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

#### RESPONSE SCHEMA: `application/json`

One of `recipient_validation` / `company_validation`

| Field | Type | Description |
|---|---|---|
| `id` | string (`^id_validation_[a-zA-Z0-9_]+$`) | Unique identifier prefixed with `id_validation_`. |
| `recipient` | string or null (<= 500 chars) | The name of the person whose identity is being validated. |
| `primary_line` | string (<= 200 chars) | The primary delivery line (usually the street address) of the address. Combination of: `primary_number`, `street_predirection`, `street_name`, `street_suffix`, `street_postdirection`, `secondary_designator`, `secondary_number`, `pmb_designator`, `pmb_number`. |
| `secondary_line` | string (<= 200 chars) | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long. |
| `urbanization` | string (<= 200 chars) | Only present for addresses in Puerto Rico. An urbanization refers to an area, sector, or development within a city. See USPS documentation for clarification. |
| `last_line` | string | Combination of: City (`city`), State (`state`), ZIP code (`zip_code`), ZIP+4 (`zip_code_plus_4`). |
| `score` | number or null (float) [ 0 .. 100 ] | Default: `null`. A numerical score between 0 and 100 that represents the likelihood the provided name is associated with a physical address. |
| `confidence` | string | Enum: `"high"`, `"medium"`, `"low"`, `""`. Indicates the likelihood the recipient name and address match based on a custom internal calculation. |
| `object` | string | Default: `"id_validation"`. Value is resource type. |

### Confidence Values

| Value | Description |
|---|---|
| `high` | Has a Lob confidence score greater than 70. |
| `medium` | Has a Lob confidence score between 40 and 70. |
| `low` | Has a Lob confidence score less than 40. |
| `""` | No tracking data exists for this address. |

### default — Error

---

## Endpoint

`POST /identity_validation`

## Request Sample

**Content type:** `application/json`

```json
{
  "recipient": "Larry Lobster",
  "primary_line": "210 King St.",
  "secondary_line": "",
  "city": "San Francisco",
  "state": "CA",
  "zip_code": "94107"
}
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "id_validation_8a013f3e",
  "recipient": "LARRY LOBSTER",
  "primary_line": "210 KING ST.",
  "secondary_line": "",
  "urbanization": "",
  "last_line": "SAN FRANCISCO CA 94107-1728",
  "score": 100,
  "confidence": "high",
  "object": "id_validation"
}
```