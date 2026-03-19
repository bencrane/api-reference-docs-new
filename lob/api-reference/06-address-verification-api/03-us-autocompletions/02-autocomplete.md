# Autocomplete

Given an address prefix consisting of a partial primary line, as well as optional input of city, state, and zip code, this functionality returns up to 10 full US address suggestions. Not all of them will turn out to be valid addresses; they'll need to be verified.

## AUTHORIZATIONS

`basicAuth`

## QUERY PARAMETERS

### `case`
- **Type:** string
- **Default:** `"upper"`
- **Enum:** `"upper"` `"proper"`

Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only affects `primary_line`, `city`, and `state`. Default casing is `upper`.

### `valid_addresses`
- **Type:** boolean
- **Default:** `false`
- **Enum:** `true` `false`

Possible values are `true` and `false`. If false, not all of the suggestions in the response will be valid addresses; they'll need to be verified in order to determine the deliverability. The `valid_addresses` flag will greatly reduce the number of keystrokes needed before reaching an intended address.

## REQUEST BODY SCHEMA

`application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `address_prefix` | string | Yes | Only accepts numbers and street names in an alphanumeric format. |
| `city` | string | No | An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `state` | string | No | An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. |
| `zip_code` | string | No | An optional ZIP Code input used to filter suggestions. Matches partial entries. |
| `geo_ip_sort` | boolean | No | If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. |

## Responses

### 200 — Returns a US autocompletion object.

#### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string (`^us_auto_[a-zA-Z0-9]+$`) | Unique identifier prefixed with `us_auto_`. |
| `suggestions` | Array of objects ([ 0 .. 10 ] items) | An array of objects representing suggested addresses. |
| `object` | string | Default: `"us_autocompletion"`. Value is resource type. |

### default — Error

---

## Endpoint

`POST /us_autocompletions`

## Request Sample

**Content type:** `application/json`

```json
{
  "address_prefix": "185 B",
  "city": "San Francisco",
  "state": "CA",
  "zip_code": "94107",
  "geo_ip_sort": false
}
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "us_auto_a3ac97bcfbb2460ab20c",
  "suggestions": [
    {
      "primary_line": "185 BAYSIDE VILLAGE PL",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BRANNAN ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BONIFACIO ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BLAIR TER",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BLUXOME ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "210 KING ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    },
    {
      "primary_line": "185 BRYANT ST",
      "city": "SAN FRANCISCO",
      "state": "CA",
      "zip_code": "94107"
    }
  ],
  "object": "us_autocompletion"
}
```