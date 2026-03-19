# Create

Creates a new check with the provided properties.

**AUTHORIZATIONS:** basicAuth

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `idempotency_key` | string ≤ 256 characters | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide. Example: `026e7634-24d7-486c-a0bb-4a17fd0eebc5` |

## Header Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Idempotency-Key` | string ≤ 256 characters | A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide. Example: `026e7634-24d7-486c-a0bb-4a17fd0eebc5` |

## Request Body Schema: application/json

One of: words at check bottom / image at check bottom

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string ≤ 400 characters | **Required** | Max of 400 characters to be included at the bottom of the check page. |
| `bank_account` | string `^bank_[a-zA-Z0-9]+$` | **Required** | The id for a verified bank account. |
| `to` | adr_id (string) or inline_address_us_chk | **Required** | Must either be an address ID or an inline object with correct address parameters. Checks cannot be sent internationally (`address_country` must be US). The total string of the sum of `address_line1` and `address_line2` must be no longer than 50 characters combined. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine, and returned back with an ID. Depending on your Print & Mail Edition, addresses may also be run through National Change of Address (NCOALink). If an address used does not meet your account's US Mail Strictness Setting, the request will fail. |
| `from` | adr_id (string) or address_editable_us | **Required** | Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification. |
| `amount` | number \<float\> ≤ 999999.99 | **Required** | The payment amount to be sent in US dollars. Amounts will be rounded to two decimal places. |
| `use_type` | string or null | **Required** | The use type for each mailpiece. Can be one of `marketing`, `operational`, or `null`. Null `use_type` is only allowed if an account default use_type is selected in Account Settings. Enum: `"marketing"` `"operational"` `null` |
| `description` | string or null ≤ 255 characters | Optional | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `metadata` | object ≤ 500 characters | Optional | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. Nested objects are not supported. |
| `merge_variables` | object or null ≤ 25000 characters | Optional | You can input a merge variable payload object to your template or QR code redirect URLs to render dynamic content. For example, if you have a template like: `{{variable_name}}`, pass in `{"variable_name": "Harry"}` to render Harry. Must be valid JSON. Max length 25,000 characters. Variable names cannot contain whitespace or special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `` ` ``, `{`, `|`, `}`, `~`. |
| `send_date` | string or string (send_date) | Optional | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default cancellation window applied to the mailpiece. Until the `send_date` has passed, the mailpiece can be canceled. If a date in the format `2017-11-01` is passed, it will evaluate to midnight UTC of that date (`2017-11-01T00:00:00.000Z`). If a datetime is passed, that exact time will be used. A `send_date` passed with no time zone will default to UTC, while a `send_date` passed with a time zone will be converted to UTC. |
| `mail_type` | string Default: `"usps_first_class"` | Optional | Checks must be sent `usps_first_class`. |
| `memo` | string or null ≤ 40 characters | Optional | Text to include on the memo line of the check. |
| `check_number` | integer [1..500000000] | Optional | An integer that designates the check number. If `check_number` is not provided, checks created from a new `bank_account` will start at 10000 and increment with each check created with the `bank_account`. A provided `check_number` overrides the defaults. Subsequent checks created with the same `bank_account` will increment from the provided check number. |
| `logo` | string or string | Optional | Accepts a remote URL or local file upload to an image to print (in grayscale) in the upper-left corner of your check. Image requirements: RGB or CMYK, square, minimum size: 100px x 100px, transparent background, png or jpg. |
| `check_bottom` | html_string / tmpl_id / remote_file_url / local_file_path | Optional | The artwork to use on the bottom of the check page. Notes: HTML merge variables should not include delimiting whitespace. PDF, PNG, and JPGs must be sized at 8.5"x11" at 300 DPI, while supplied HTML will be rendered and trimmed to fit on a 8.5"x11" page. The check bottom will always be printed in black & white. Must conform to the template. |
| `attachment` | html_string / tmpl_id / remote_file_url / local_file_path | Optional | A document to include with the check. Notes: HTML merge variables should not include delimiting whitespace. All pages of PDF, PNG, and JPGs must be sized at 8.5"x11" at 300 DPI, while supplied HTML will be rendered and trimmed to as many 8.5"x11" pages as necessary. If a PDF is provided, it must be 6 pages or fewer. The attachment will be printed double-sided in black & white and will be included in the envelope after the check page. |
| `billing_group_id` | string | Optional | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. |
| `print_speed` | string or null Default: `"core"` | Optional | A string designating the mail speed type: `core` - 2 production business days. |

## Responses

**200** - Returns a check object

### Response Headers

| Header | Type | Description |
|--------|------|-------------|
| `ratelimit-limit` | integer | The rate limit for a given endpoint. Example: `150` |
| `ratelimit-remaining` | integer | The number of requests remaining in the current window. Example: `100` |
| `ratelimit-reset` | integer | The time at which the rate limit window resets in UTC epoch seconds. Example: `1528749846` |

### Response Schema: application/json

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `bank_account` | object (bank_account) | **Required** | |
| `id` | string (chk_id) `^chk_[a-zA-Z0-9]+$` | **Required** | Unique identifier prefixed with `chk_`. |
| `amount` | number \<float\> ≤ 999999.99 | **Required** | The payment amount to be sent in US dollars. |
| `to` | object (to_address_us_chk) | **Required** | |
| `url` | string (signed_link) | **Required** | A signed link served over HTTPS. The link returned will expire in 30 days to prevent mis-sharing. Each time a GET request is initiated, a new signed URL will be generated. |
| `carrier` | string Default: `"USPS"` | **Required** | |
| `date_created` | string \<date-time\> | **Required** | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string \<date-time\> | **Required** | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `use_type` | string or null | **Required** | The use type for each mailpiece. Enum: `"marketing"` `"operational"` `null` |
| `description` | string or null ≤ 255 characters | Optional | An internal description that identifies this resource. |
| `metadata` | object ≤ 500 characters | Optional | Metadata key-value pairs. |
| `merge_variables` | object or null ≤ 25000 characters | Optional | Merge variable payload object. |
| `send_date` | string or string (send_date) | Optional | |
| `mail_type` | string Default: `"usps_first_class"` | Optional | Checks must be sent `usps_first_class`. |
| `memo` | string or null ≤ 40 characters | Optional | Text on the memo line. |
| `check_number` | integer [1..500000000] | Optional | The check number. |
| `message` | string ≤ 400 characters | Optional | Max of 400 characters at the bottom of the check page. |
| `from` | object (address_us) | Optional | |
| `check_bottom_template_id` | string `^tmpl_[a-zA-Z0-9]+$` | Optional | The unique ID of the HTML template used for the check bottom. |
| `attachment_template_id` | string `^tmpl_[a-zA-Z0-9]+$` | Optional | The unique ID of the HTML template used for the attachment. |
| `check_bottom_template_version_id` | string `^vrsn_[a-zA-Z0-9]+$` | Optional | The unique ID of the specific version of the HTML template used for the check bottom. |
| `attachment_template_version_id` | string `^vrsn_[a-zA-Z0-9]+$` | Optional | The unique ID of the specific version of the HTML template used for the attachment. |
| `thumbnails` | Array of objects (thumbnail) | Optional | |
| `expected_delivery_date` | string \<date\> | Optional | A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`. |
| `tracking_events` | Array of objects or null | Optional | An array of tracking_event objects ordered by ascending time. Will not be populated for checks created in test mode. |
| `status` | string (status) | Optional | A string describing the PDF render status: `processed` - rendering in progress. `rendered` - PDF successfully rendered. `failed` - rendering process has failed. Enum: `"processed"` `"rendered"` `"failed"` |
| `failure_reason` | object or null | Optional | An object describing the reason for failure if the resource failed to render. |
| `object` | string Default: `"check"` | Optional | Value is resource type. |
| `deleted` | boolean | Optional | Only returned if the resource has been successfully deleted. |

**default** - Error

## Request

```
POST /checks
```

### Request Body Example

```json
{
  "description": "Demo Check",
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
    "name": "Leore Avidar",
    "address_line1": "210 King St",
    "address_line2": "# 6100",
    "address_city": "San Francisco",
    "address_state": "CA",
    "address_zip": "94107-1741"
  },
  "bank_account": "bank_8cad8df5354d33f",
  "amount": 22.5,
  "memo": "rent",
  "logo": "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/check_logo.png",
  "check_bottom": "tmpl_23668b406d5afef",
  "merge_variables": {
    "name": "Harry"
  },
  "metadata": {
    "memo": "rafting trip"
  },
  "attachment": "./cool.pdf",
  "send_date": "2017-11-01T00:00:00.000Z",
  "use_type": "operational",
  "mail_type": "usps_first_class",
  "check_number": 10001,
  "print_speed": "core"
}
```

## Response Example

**200**

```json
{
  "id": "chk_534f10783683daa0",
  "description": "Demo Check",
  "metadata": {},
  "check_number": 10062,
  "memo": "rent",
  "amount": 22.5,
  "url": "https://lob-assets.com/checks/chk_534f10783683daa0.pdf?expires=1540372221&signature=Ty3IV2bGPEoQfrdraYHlNYTaarnHLXb",
  "to": {
    "id": "adr_bae820679f3f536b",
    "description": "Harry - Office",
    "name": "HARRY ZHANG",
    "company": "LOB",
    "email": "harry@lob.com",
    "phone": "5555555555",
    "address_line1": "210 KING ST STE 6100",
    "address_line2": "",
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": {},
    "date_created": "2018-12-08T03:08:43.446Z",
    "date_modified": "2018-12-08T03:08:43.446Z",
    "object": "address",
    "recipient_moved": false
  },
  "from": {
    "id": "adr_b8fb5acf3a2b55db",
    "name": "LEORE AVIDAR",
    "address_line1": "210 KING ST STE 6100",
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": {},
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "object": "address"
  },
  "bank_account": {
    "id": "bank_8cad8df5354d33f",
    "description": "Test Bank Account",
    "metadata": {},
    "routing_number": "322271627",
    "account_number": "123456789",
    "signatory": "John Doe",
    "bank_name": "J.P. MORGAN CHASE BANK, N.A.",
    "verified": true,
    "account_type": "company",
    "date_created": "2015-11-06T19:24:24.440Z",
    "date_modified": "2015-11-06T19:41:28.312Z",
    "object": "bank_account",
    "signature_url": "https://lob-assets.com/bank-accounts/asd_asdfghjkqwertyui.pdf?expires=1234567890&signature=aksdf"
  },
  "carrier": "USPS",
  "tracking_events": [],
  "thumbnails": [
    {
      "small": "https://lob-assets.com/checks/chk_534f10783683daa0_thumb_small_1.png?expires=1540372221&signature=ShhPpH74wYkNiAj7Il9B6q8ZKkzlGd4",
      "medium": "https://lob-assets.com/checks/chk_534f10783683daa0_thumb_medium_1.png?expires=1540372221&signature=tmIOq6aAyKgzAECp7STj1rvJuMS5Svd",
      "large": "https://lob-assets.com/checks/chk_534f10783683daa0_thumb_large_1.png?expires=1540372221&signature=04nLEwE9d2qgQJNgJYWSOgPnU0FZbEv"
    }
  ],
  "merge_variables": {
    "name": "Harry"
  },
  "expected_delivery_date": "2017-09-12",
  "mail_type": "usps_first_class",
  "date_created": "2017-09-05T17:47:53.896Z",
  "date_modified": "2017-09-05T17:47:53.896Z",
  "send_date": "2017-09-05T17:47:53.896Z",
  "object": "check",
  "message": "pancakes are good",
  "check_bottom_template_id": "tmpl_a",
  "attachment_template_id": "tmpl_a",
  "check_bottom_template_version_id": "vrsn_a",
  "attachment_template_version_id": "vrsn_a",
  "use_type": "operational",
  "sla": "2",
  "deleted": true
}
```