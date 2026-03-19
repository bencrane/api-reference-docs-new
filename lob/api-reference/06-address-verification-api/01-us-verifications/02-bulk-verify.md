# Bulk Verify

Verify a list of US or US territory addresses with a live API key. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

## AUTHORIZATIONS

`basicAuth`

## QUERY PARAMETERS

### `case`
- **Type:** string
- **Default:** `"upper"`
- **Enum:** `"upper"` `"proper"`

Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only affects `recipient`, `primary_line`, `secondary_line`, `urbanization`, and `last_line`. Default casing is `upper`.

## REQUEST BODY SCHEMA

`application/json`

### `addresses` (required)
Array of US verification object with `city` and `state` (object) or US verification object with `zip_code` (object) (`multiple_components`) **[ 1 .. 20 ] items**

## Responses

### 200
Returns a list of US verification objects.

#### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

#### RESPONSE SCHEMA: `application/json`

| Field | Required | Description |
|---|---|---|
| `addresses` | Yes | Array of `us_verification` (object) or `error` (object) |
| `errors` | Yes | Indicates whether any errors occurred during the verification process. |

### default
Error

---

## Request Sample

**Content type:** `application/json`

```json
{
  "addresses": [
    {
      "primary_line": "210 King Street",
      "city": "San Francisco",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "recipient": "Walgreens",
      "primary_line": "Ave Wilson Churchill 123",
      "secondary_line": "",
      "urbanization": "URB FAIR OAKS",
      "city": "RIO PIEDRAS",
      "state": "PR",
      "zip_code": "00926"
    }
  ]
}
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "addresses": [
    {
      "id": "us_ver_c7cb63d68f8d6",
      "recipient": "LOB.COM",
      "primary_line": "210 KING ST",
      "secondary_line": "",
      "urbanization": "",
      "last_line": "SAN FRANCISCO CA 94107-1702",
      "deliverability": "deliverable",
      "valid_address": true,
      "components": {},
      "deliverability_analysis": {},
      "lob_confidence_score": {},
      "object": "us_verification"
    }
  ],
  "errors": false
}
```