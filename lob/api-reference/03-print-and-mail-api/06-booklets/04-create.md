# Booklets - Create

Creates a new booklet.

## Authorization
`basicAuth`

## HTTP Request
```
POST /booklets
```

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `idempotency_key` | string (<= 256 characters) | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide. Example: `026e7634-24d7-486c-a0bb-4a17fd0eebc5` |

## Header Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Idempotency-Key` | string (<= 256 characters) | A string of no longer than 256 characters that uniquely identifies this resource. Example: `026e7634-24d7-486c-a0bb-4a17fd0eebc5` |

## Request Body (`application/json`)

### Required Fields

| Property | Type | Description |
|----------|------|-------------|
| `to` | adr_id (string) or inline_address | Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using the US Address Verification engine (if it is a US address). Non-US addresses will be standardized into uppercase only. If a US address does not meet your account's US Mail strictness setting, the request will fail. |
| `from` | adr_id (string) or inline_address | Must either be an address ID or an inline object with correct address parameters. Must be a US address unless using a custom_envelope. All addresses will be standardized into uppercase without being modified by verification. |
| `file` | html_string (string) or tmpl_id (string) or remote_file_url (string) or string (booklet_file) | HTML merge variables should not include delimiting whitespace. All pages of a supplied PDF file must be sized per the size attribute, while supplied HTML will be rendered and trimmed to as many size pages as necessary. See pricing for extra costs incurred. |
| `use_type` | string or null (booklet_use_type) | Enum: `"marketing"`, `"operational"`, `null`. The use type for each mailpiece. Null use_type is only allowed if an account default use_type is selected in Account Settings. |
| `pages` | integer (booklet_pages) | Total number of pages in a booklet, where four pages make up one sheet. Must always be in increments of four. For 8.375x5.375 inch booklets: 8, 12, 16, 20, 24, 28, or 32 pages. |
| `size` | string (booklet_size) | Default: `"8.375x5.375"`. Specifies the size of the booklet. |

### Optional Fields

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `description` | string or null (resource_description) | — | An internal description that identifies this resource. Max 255 characters. |
| `metadata` | object (metadata) | — | Up to 20 key-value pairs. Keys max 40 chars, values max 500 chars. Cannot contain `"` and `\`. Nested objects not supported. |
| `mail_type` | string | `"usps_first_class"` | Enum: `"usps_first_class"`, `"usps_standard"`. `usps_standard` is cheaper but less predictable and slower. Cannot be used with 4x6 postcards or postcards sent outside the US. |
| `merge_variables` | object or null (merge_variables) | — | Merge variable payload for dynamic content rendering. Max 25,000 characters. Variable names cannot contain whitespace or special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `` ` ``, `{`, `\|`, `}`, `~`. |
| `send_date` | string or string (send_date) | — | ISO 8601 timestamp, up to 180 days in the future. Overrides the default cancellation window. Until the send_date has passed, the mailpiece can be canceled. Defaults to UTC if no time zone specified. |
| `print_speed` | string or null | `"core"` | Value: `"core"`. `core` = 2 production business days. |
| `billing_group_id` | string (billing_group_id) | — | Optional billing group ID to tag usage. Requires special activation. |
| `qr_code` | object (qr_code) | — | Customize and place a QR code on the creative at the required position. |
| `fsc` | boolean | `false` | Beta feature. Contact support@lob.com or your account contact. Not available for A4 and us_legal letter size. |
| `source_material` | string (booklet_source_material) | `"60# Gloss Text"` | Defines the material used. For 8.375x5.375 inch booklets, the default is 60# Gloss Text. |

## Response (200) - Returns a booklet object

### Response Headers

| Header | Type | Description |
|--------|------|-------------|
| `ratelimit-limit` | integer | The rate limit for a given endpoint. Example: `150` |
| `ratelimit-remaining` | integer | The number of requests remaining in the current window. Example: `100` |
| `ratelimit-reset` | integer | The time at which the rate limit window resets in UTC epoch seconds. Example: `1528749846` |

### Response Schema (`application/json`)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `to` | address_us or address_intl (address) | Yes | Recipient address object |
| `carrier` | string | Yes | Default: `"USPS"` |
| `id` | string (booklet_id) | Yes | Unique identifier prefixed with `ord_`. Pattern: `^ord_[0-9a-f]{26}$` |
| `from` | address_us or address_intl (address) | Yes | Sender address object |
| `use_type` | string or null (booklet_use_type) | Yes | Enum: `"marketing"`, `"operational"`, `null` |
| `tracking_events` | Array of objects (tracking_event_normal) | No | An array of tracking events ordered by ascending time. |
| `description` | string or null (resource_description) | No | Max 255 characters. |
| `metadata` | object (metadata) | No | Up to 20 key-value pairs. Max 500 characters total. |
| `merge_variables` | object or null (merge_variables) | No | Max 25,000 characters. |
| `send_date` | string or string (send_date) | No | ISO 8601 timestamp. |
| `mail_type` | string (mail_type) | No | Default: `"usps_first_class"`. Enum: `"usps_first_class"`, `"usps_standard"`. |
| `thumbnails` | Array of objects (thumbnail) | No | |
| `expected_delivery_date` | string \<date\> | No | YYYY-MM-DD format. |
| `date_created` | string \<date-time\> | No | ISO 8601 timestamp. |
| `date_modified` | string \<date-time\> | No | ISO 8601 timestamp. |
| `deleted` | boolean | No | Only returned if successfully deleted. |
| `url` | string (signed_link) | No | Signed HTTPS link, expires in 30 days. |
| `template_id` | string | No | Pattern: `^tmpl_[a-zA-Z0-9]+$` |
| `template_version_id` | string | No | Pattern: `^vrsn_[a-zA-Z0-9]+$` |
| `campaign_id` | string or null (campaign_id) | No | Pattern: `^(cmp|camp)_[a-zA-Z0-9]+$` |
| `size` | string (booklet_size) | No | Default: `"8.375x5.375"` |
| `pages` | integer (booklet_pages) | No | Must be in increments of four. |
| `fsc` | boolean | No | Default: `false`. Beta feature. |
| `status` | string (status) | No | Enum: `"processed"`, `"rendered"`, `"failed"`. |
| `source_material` | string (booklet_source_material) | No | Default: `"60# Gloss Text"` |
| `failure_reason` | object or null | No | Reason for failure if rendering failed. |
| `object` | string | No | Default: `"booklet"` |

## Request Sample (Payload)

```json
{
  "description": "demo",
  "to": {
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
  },
  "from": {
    "name": "Harry",
    "address_line1": "210 King St",
    "address_line2": "# 6100",
    "address_city": "San Francisco",
    "address_state": "CA",
    "address_zip": "94107"
  },
  "file": "<html style='padding-top: 3in; margin: .5in;'>HTML Booklet for {{name}}</html>",
  "mail_type": "usps_first_class",
  "merge_variables": {
    "name": "Harry"
  },
  "metadata": {
    "spiffy": "true"
  },
  "send_date": "2017-11-01T00:00:00.000Z",
  "use_type": "marketing",
  "qr_code": {
    "position": "relative",
    "redirect_url": "https://www.lob.com",
    "width": "2",
    "top": "2",
    "right": "2",
    "pages": "1-2,4-5"
  },
  "fsc": true,
  "size": "8.375x5.375",
  "print_speed": "core"
}
```

## Response Sample (200)

```json
{
  "id": "ord_0d6a16a3fff6318ac8f8008dc1",
  "description": "April Campaign",
  "metadata": {},
  "to": {
    "id": "adr_d3489cd64c791ab5",
    "description": null,
    "name": "HARRY ZHANG",
    "company": null,
    "phone": null,
    "email": null,
    "address_line1": "210 KING ST STE 6100",
    "address_line2": null,
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": {},
    "date_created": "2017-09-05T15:54:53.264Z",
    "date_modified": "2017-09-05T15:54:53.264Z",
    "deleted": true,
    "object": "address"
  },
  "from": {
    "id": "adr_b8fb5acf3a2b55db",
    "description": null,
    "name": "LEORE AVIDAR",
    "company": null,
    "phone": null,
    "email": null,
    "address_line1": "210 KING ST STE 6100",
    "address_line2": null,
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": {},
    "date_created": "2017-09-05T15:54:53.264Z",
    "date_modified": "2017-09-05T15:54:53.264Z",
    "deleted": true,
    "object": "address"
  },
  "mail_type": "usps_first_class",
  "url": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d.pdf?version=v1&expires=1618512040&signature=qvyCqXI1ndBvc4AjvG8FlirqLXEcfmYo4sDrRtabaXMOsX88to9G3K49uIk_aqevvZXe8HoRYD_nWydbQHqaCA",
  "carrier": "USPS",
  "tracking_number": null,
  "tracking_events": [],
  "thumbnails": [
    {
      "small": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_small_1.png?version=v1&expires=1618512040&signature=-bipeUHP-hAMcCBSrWM0ZH1VwRdSPNVGGZN9hAZKr6Lh4ly6uxvratVd5LXJCK_zOEMYk_mTWASt0ge7OY6SDA",
      "medium": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_medium_1.png?version=v1&expires=1618512040&signature=ryxN7bsXGtw_GRFSP3Cs3A3IYjxZi3cW9BHDCNgMt6p3nobVmsc_iFHt2e-S7ndAXhhN7nP-MQVov3bt3r37BQ",
      "large": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_large_1.png?version=v1&expires=1618512040&signature=kBrm00xkyCkJNJRHxH8HshFaebtOxnzjVWOs1VVmGMuw8H6OBNcMAMxt9s49K0jlpHoh3Nr9uSncEZMQaaNjAg"
    }
  ],
  "merge_variables": {
    "name": "Harry"
  },
  "size": "8.375x5.375",
  "pages": 8,
  "source_material": "60# Gloss Text",
  "expected_delivery_date": "2021-03-24",
  "date_created": "2021-03-16T18:40:40.504Z",
  "date_modified": "2021-03-16T18:40:40.504Z",
  "send_date": "2021-03-16T18:45:40.493Z",
  "use_type": "marketing",
  "fsc": false,
  "sla": "2",
  "object": "booklet"
}
```