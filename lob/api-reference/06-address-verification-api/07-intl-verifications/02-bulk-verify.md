# Bulk Verify (International)

Verify a list of international (except US or US territories) addresses with a live API key. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

## AUTHORIZATIONS

`basicAuth`

## REQUEST BODY SCHEMA

`application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `addresses` | Array of objects (`multiple_components_intl`) [ 1 .. 20 ] items | Yes | Array of international address objects to verify. |

## Responses

### 200 — Returns an array of international verification objects.

#### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

#### RESPONSE SCHEMA: `application/json`

| Field | Required | Description |
|---|---|---|
| `addresses` | Yes | Array of `intl_verification` (object) or `error` (object). |
| `errors` | Yes | Indicates whether any errors occurred during the verification process. |

### default — Error

---

## Endpoint

`POST /bulk/intl_verifications`

## Request Sample

**Content type:** `application/json`

```json
{
  "addresses": [
    {
      "recipient": "John Doe",
      "primary_line": "370 Water St",
      "secondary_line": "",
      "city": "Summerside",
      "state": "Prince Edwards Island",
      "postal_code": "C1N 1C4",
      "country": "CA"
    },
    {
      "recipient": "Jane Doe",
      "primary_line": "UL. DOLSKAYA 1",
      "secondary_line": "",
      "city": "MOSCOW",
      "state": "MOSCOW G",
      "postal_code": "115569",
      "country": "RU"
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
      "id": "intl_ver_c7cb63d68f8d6",
      "recipient": null,
      "primary_line": "370 WATER ST",
      "secondary_line": "",
      "last_line": "SUMMERSIDE PE C1N 1C4",
      "country": "CA",
      "coverage": "SUBBUILDING",
      "deliverability": "deliverable",
      "status": "LV4",
      "components": {},
      "object": "intl_verification"
    }
  ],
  "errors": false
}
```