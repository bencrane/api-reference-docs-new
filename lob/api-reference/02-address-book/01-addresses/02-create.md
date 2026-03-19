# Create Address

Creates a new address given information.

**AUTHORIZATIONS:** basicAuth

**POST** `/addresses`

## Request Body Schema: application/json

One of `address_editable_us` or `address_editable_intl`. Any of address obj with `name` defined or address obj with `company` defined.

### Required Fields

| Field | Type | Description |
|---|---|---|
| `name` | string or null <= 40 characters | Either name or company is required, you may also add both. Must be no longer than 40 characters. If both name and company are provided, they will be printed on two separate lines above the rest of the address. |
| `address_line1` | string <= 64 characters | The primary number, street name, and directional information. |
| `address_city` | string <= 200 characters | |
| `address_state` | string `^[a-zA-Z]{2}$` | 2 letter state short-name code. |
| `address_zip` | string `^\d{5}(-\d{4})?$` | Must follow the ZIP format of 12345 or ZIP+4 format of 12345-1234. |

### Optional Fields

| Field | Type | Description |
|---|---|---|
| `address_line2` | string or null <= 64 characters | An optional field containing any information which can't fit into line 1. |
| `description` | string or null <= 255 characters | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `company` | string or null <= 40 characters | Either name or company is required, you may also add both. Must be no longer than 40 characters. If both name and company are provided, they will be printed on two separate lines above the rest of the address. This field can be used for any secondary recipient information which is not part of the actual mailing address (Company Name, Department, Attention Line, etc). |
| `phone` | string or null <= 40 characters | Must be no longer than 40 characters. |
| `email` | string or null <= 100 characters | Must be no longer than 100 characters. |
| `address_country` | string | Default: `"US"`. Value: `"US"`. |
| `metadata` | object (metadata) <= 500 characters `[^"\\]{0,500}` | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. See Metadata for more information. |

## Responses

### 200

Echos the writable fields of a newly created address object.

**Response Headers:**

| Header | Type | Description |
|---|---|---|
| `ratelimit-limit` | integer | The rate limit for a given endpoint. Example: 150 |
| `ratelimit-remaining` | integer | The number of requests remaining in the current window. Example: 100 |
| `ratelimit-reset` | integer | The time at which the rate limit window resets in UTC epoch seconds. Example: 1528749846 |

**Response Schema:** application/json

One of `address_us` or `address_intl`. Any of address obj with `name` defined or address obj with `company` defined.

| Field | Type | Description |
|---|---|---|
| `name` | string or null <= 40 characters | **required.** Either name or company is required, you may also add both. |
| `date_created` | string \<date-time\> | **required.** A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string \<date-time\> | **required.** A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string | **required.** Default: `"address"`. Value is resource type. |
| `id` | string `^adr_[a-zA-Z0-9]+$` | **required.** Unique identifier prefixed with `adr_`. |
| `address_line1` | string <= 64 characters | **required.** The primary number, street name, and directional information. |
| `address_city` | string <= 200 characters | **required.** |
| `address_state` | string `^[a-zA-Z]{2}$` | **required.** 2 letter state short-name code. |
| `address_zip` | string `^\d{5}(-\d{4})?$` | **required.** Must follow the ZIP format of 12345 or ZIP+4 format of 12345-1234. |
| `deleted` | boolean | Only returned if the resource has been successfully deleted. |
| `description` | string or null <= 255 characters | An internal description that identifies this resource. |
| `company` | string or null <= 40 characters | Either name or company is required, you may also add both. |
| `phone` | string or null <= 40 characters | Must be no longer than 40 characters. |
| `email` | string or null <= 100 characters | Must be no longer than 100 characters. |
| `address_line2` | string or null <= 64 characters | An optional field containing any information which can't fit into line 1. |
| `address_country` | string = 13 characters | Value: `"UNITED STATES"`. Full name of country. |
| `metadata` | object (metadata) <= 500 characters | Use metadata to store custom information for tagging and labeling back to your internal systems. |
| `recipient_moved` | boolean or null | Only returned for accounts on certain Print & Mail Editions. Value is `true` if the address was altered because the recipient filed for a National Change of Address Linkage (NCOALink), `false` if the NCOALink check was run but no altered address was found, and `null` if the NCOALink check was not run. The NCOALink check does not happen for non-US addresses, for non-deliverable US addresses, or for addresses created before the NCOALink feature was added to your account. |

### default

Error

**Response Schema:** application/json

| Field | Type | Description |
|---|---|---|
| `error` | object | **required** |

## Request Samples

```json
{
  "description": "Harry - Office",
  "name": "Harry Zhang",
  "company": "Lob",
  "email": "harry@lob.com",
  "phone": "5555555555",
  "address_line1": "210 King St",
  "address_line2": "# 6100",
  "address_city": "San Francisco",
  "address_state": "CA",
  "address_zip": "94107",
  "address_country": "US"
}
```

## Response Samples

### 200

```json
{
  "id": "adr_d3489cd64c791ab5",
  "description": "Harry - Office",
  "name": "HARRY ZHANG",
  "company": "LOB",
  "phone": "5555555555",
  "email": "harry@lob.com",
  "address_line1": "210 KING ST STE 6100",
  "address_city": "SAN FRANCISCO",
  "address_state": "CA",
  "address_zip": "94107",
  "address_country": "UNITED STATES",
  "metadata": {},
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "address"
}
```