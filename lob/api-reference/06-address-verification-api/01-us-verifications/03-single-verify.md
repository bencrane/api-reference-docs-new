# Single Verify

Verify a US or US territory address with a live API key. The address can be in components (e.g. `primary_line` is "210 King Street", `zip_code` is "94107") or as a single string (e.g. "210 King Street 94107"), but not as both. Requests using a test API key validate required fields but return empty values unless specific `primary_line` values are provided. See the US Verifications Test Environment for details.

## AUTHORIZATIONS

`basicAuth`

## QUERY PARAMETERS

### `case`
- **Type:** string
- **Default:** `"upper"`
- **Enum:** `"upper"` `"proper"`

Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. "PO BOX") and proper-cased (e.g. "PO Box"), respectively. Only affects `recipient`, `primary_line`, `secondary_line`, `urbanization`, and `last_line`. Default casing is `upper`.

## REQUEST BODY SCHEMA: `application/json`

One of `multiple_components` / `single_line_address`

Any of: US verification object with `city` and `state` / US verification object with `zip_code`

### Required Fields

| Field | Type | Description |
|---|---|---|
| `city` | string (<= 200 chars) | The name of the city. `city` and `state` are required if no `zip_code` is passed. |
| `state` | string (<= 50 chars) | The ISO 3166-2 two letter code or subdivision name for the state. `city` and `state` are required if no `zip_code` is passed. |
| `primary_line` | string (<= 200 chars) | The primary delivery line (usually the street address) of the address. Combination of: `primary_number`, `street_predirection`, `street_name`, `street_suffix`, `street_postdirection`, `secondary_designator`, `secondary_number`, `pmb_designator`, `pmb_number`. |

### Optional Fields

| Field | Type | Description |
|---|---|---|
| `recipient` | string or null (<= 500 chars) | The intended recipient, typically a person's or firm's name. |
| `secondary_line` | string (<= 200 chars) | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long. |
| `urbanization` | string (<= 200 chars) | Only present for addresses in Puerto Rico. An urbanization refers to an area, sector, or development within a city. See USPS documentation for clarification. |
| `zip_code` | string (`^\d{5}((-)?\d{4})?$`) | Required if `city` and `state` are not passed in. If included, must be formatted as a US ZIP or ZIP+4 (e.g. `94107`, `941072282`, `94107-2282`). |

## Responses

### 200 — Returns a US verification object.

#### RESPONSE HEADERS

| Header | Type | Example | Description |
|---|---|---|---|
| `ratelimit-limit` | integer | `150` | The rate limit for a given endpoint. |
| `ratelimit-remaining` | integer | `100` | The number of requests remaining in the current window. |
| `ratelimit-reset` | integer | `1528749846` | The time at which the rate limit window resets in UTC epoch seconds. |

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string (`^us_ver_[a-zA-Z0-9_]+$`) | Unique identifier prefixed with `us_ver_`. |
| `recipient` | string or null (<= 500 chars) | The intended recipient, typically a person's or firm's name. |
| `primary_line` | string (<= 200 chars) | The primary delivery line (usually the street address) of the address. Combination of: `primary_number`, `street_predirection`, `street_name`, `street_suffix`, `street_postdirection`, `secondary_designator`, `secondary_number`, `pmb_designator`, `pmb_number`. |
| `secondary_line` | string (<= 200 chars) | The secondary delivery line of the address. This field is typically empty but may contain information if `primary_line` is too long. |
| `urbanization` | string (<= 200 chars) | Only present for addresses in Puerto Rico. An urbanization refers to an area, sector, or development within a city. See USPS documentation for clarification. |
| `last_line` | string | Combination of: City (`city`), State (`state`), ZIP code (`zip_code`), ZIP+4 (`zip_code_plus_4`). |
| `deliverability` | string | Enum: `"deliverable"`, `"deliverable_unnecessary_unit"`, `"deliverable_incorrect_unit"`, `"deliverable_missing_unit"`, `"undeliverable"`. Summarizes the deliverability of the `us_verification` object. |
| `valid_address` | boolean | This field indicates whether an address was found in a more comprehensive address dataset that includes sources from the USPS, open source mapping data, and proprietary mail delivery data. A valid address may contradict the `deliverability` field since an address can be a real valid location but the USPS may not deliver to that address. |
| `components` | object (`us_components`) | A nested object containing a breakdown of each component of an address. |
| `deliverability_analysis` | object (`deliverability_analysis`) | A nested object containing a breakdown of the deliverability of an address. |
| `lob_confidence_score` | object (`lob_confidence_score`) | Lob Confidence Score is a nested object that provides a numerical value between 0-100 of the likelihood that an address is deliverable based on Lob's mail delivery data to over half of US households. |
| `object` | string | Default: `"us_verification"`. Value is resource type. |

### Deliverability Values

| Value | Description |
|---|---|
| `deliverable` | The address is deliverable by the USPS. |
| `deliverable_unnecessary_unit` | The address is deliverable, but the secondary unit information is unnecessary. |
| `deliverable_incorrect_unit` | The address is deliverable to the building's default address but the secondary unit provided may not exist. There is a chance the mail will not reach the intended recipient. |
| `deliverable_missing_unit` | The address is deliverable to the building's default address but is missing secondary unit information. There is a chance the mail will not reach the intended recipient. |
| `undeliverable` | The address is not deliverable according to the USPS. |

### default — Error

---

## Endpoint

`POST /us_verifications`

## Request Sample

**Content type:** `application/json`

```json
{
  "primary_line": "210 King Street",
  "city": "San Francisco",
  "state": "CA",
  "zip_code": "94107"
}
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "us_ver_c7cb63d68f8d6",
  "recipient": "LOB.COM",
  "primary_line": "210 KING ST",
  "secondary_line": "",
  "urbanization": "",
  "last_line": "SAN FRANCISCO CA 94107-1702",
  "deliverability": "deliverable",
  "valid_address": true,
  "components": {
    "primary_number": "210",
    "street_predirection": "",
    "street_name": "KING",
    "street_suffix": "ST",
    "street_postdirection": "",
    "secondary_designator": "",
    "secondary_number": "",
    "pmb_designator": "",
    "pmb_number": "",
    "extra_secondary_designator": "",
    "extra_secondary_number": "",
    "city": "SAN FRANCISCO",
    "state": "CA",
    "zip_code": "94107",
    "zip_code_plus_4": "1702",
    "zip_code_type": "standard",
    "delivery_point_barcode": "941071702108",
    "address_type": "commercial",
    "record_type": "street",
    "default_building_address": false,
    "county": "SAN FRANCISCO",
    "county_fips": "06075",
    "carrier_route": "C032",
    "carrier_route_type": "city_delivery",
    "po_box_only_flag": "N",
    "latitude": 37.77597542841264,
    "longitude": -122.3929557343685
  },
  "deliverability_analysis": {
    "dpv_confirmation": "Y",
    "dpv_cmra": "N",
    "dpv_vacant": "N",
    "dpv_active": "Y",
    "dpv_inactive_reason": "",
    "dpv_throwback": "N",
    "dpv_non_delivery_day_flag": "N",
    "dpv_non_delivery_day_values": "",
    "dpv_no_secure_location": "N",
    "dpv_door_not_accessible": "N",
    "dpv_footnotes": [
      "AA",
      "BB"
    ],
    "ews_match": false,
    "lacs_indicator": "",
    "lacs_return_code": "",
    "suite_return_code": ""
  },
  "lob_confidence_score": {
    "score": 100,
    "level": "high"
  },
  "object": "us_verification"
}
```