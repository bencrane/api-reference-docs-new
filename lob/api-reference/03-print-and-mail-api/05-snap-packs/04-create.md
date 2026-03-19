# Create

Creates a new snap_pack given information.

**AUTHORIZATIONS:** basicAuth

## QUERY PARAMETERS

| Parameter | Type | Description |
|-----------|------|-------------|
| idempotency_key | string <= 256 characters | Example: `idempotency_key=026e7634-24d7-486c-a0bb-4a17fd0eebc5`. A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide. |

## HEADER PARAMETERS

| Parameter | Type | Description |
|-----------|------|-------------|
| Idempotency-Key | string <= 256 characters | Example: `026e7634-24d7-486c-a0bb-4a17fd0eebc5`. A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide. |

## REQUEST BODY SCHEMA: application/json

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| to | adr_id (string) or inline_address | required | Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your Print & Mail Edition, US addresses may also be run through National Change of Address Linkage (NCOALink). Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account's US Mail strictness setting, the request will fail. |
| inside | html_string (string) or tmpl_id (string) or remote_file_url (string) or local_file_path (string) | required | The artwork to use as the inside of your snap pack. Notes: HTML merge variables should not include delimiting whitespace. PDF, PNG, and JPGs must be sized at 8.5"x11" at 300 DPI, while supplied HTML will be rendered to the specified size. Be sure to leave room for address and postage information by following the 8.5x11 snap pack template. |
| outside | html_string (string) or tmpl_id (string) or remote_file_url (string) or local_file_path (string) | required | The artwork to use as the outside of your snap pack. Notes: HTML merge variables should not include delimiting whitespace. PDF, PNG, and JPGs must be sized at 6"x18" at 300 DPI, while supplied HTML will be rendered to the specified size. |
| use_type | string or null (snap_pack_use_type) | required | Enum: `"marketing"` `"operational"` `null`. The use type for each mailpiece. Can be one of marketing, operational, or null. Null use_type is only allowed if an account default use_type is selected in Account Settings. |
| description | string or null (resource_description) <= 255 characters | | An internal description that identifies this resource. Must be no longer than 255 characters. |
| metadata | object (metadata) <= 500 characters `[^"\\]{0,500}` | | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. |
| mail_type | string (mail_type) | | Default: `"usps_first_class"` Enum: `"usps_first_class"` `"usps_standard"`. A string designating the mail postage type: `usps_first_class` - (default), `usps_standard` - a cheaper option which is less predictable and takes longer to deliver. usps_standard cannot be used with 4x6 postcards or for any postcards sent outside of the United States. |
| merge_variables | object or null (merge_variables) <= 25,000 characters | | You can input a merge variable payload object to your template or QR code redirect URLs to render dynamic content. For example, if you have a template like: `{{variable_name}}`, pass in `{"variable_name": "Harry"}` to render Harry. merge_variables must be an object. Any type of value is accepted as long as the object is valid JSON; you can use strings, numbers, booleans, arrays, objects, or null. The max length of the object is 25,000 characters. Your variable names cannot contain any whitespace or any of the following special characters: `!`, `"`, `#`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `;`, `<`, `=`, `>`, `@`, `[`, `\`, `]`, `^`, `` ` ``, `{`, `|`, `}`, `~`. |
| send_date | string or string (send_date) | | A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default cancellation window applied to the mailpiece. Until the send_date has passed, the mailpiece can be canceled. If a date in the format `2017-11-01` is passed, it will evaluate to midnight UTC of that date (`2017-11-01T00:00:00.000Z`). If a datetime is passed, that exact time will be used. A send_date passed with no time zone will default to UTC, while a send_date passed with a time zone will be converted to UTC. |
| print_speed | string or null | | Default: `"core"` Value: `"core"`. A string designating the mail speed type: `core` - 2 production business days. |
| size | string (snap_pack_size) | | Default: `"8.5x11"` Value: `"8.5x11"`. Specifies the size of the snap pack. |
| from | adr_id (string) or address_editable_us | | Required if to address is international. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification. |
| billing_group_id | string (billing_group_id) | | An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See Billing Group API for more information. |
| color | boolean | | Default: `false`. Set this key to `true` if you would like to print in color. Set to `false` if you would like to print in black and white. |
| qr_code | object (qr_code) | | Customize and place a QR code on the creative at the required position. |

## Responses

**200** Returns a snap_pack object

### RESPONSE HEADERS

| Header | Type | Description |
|--------|------|-------------|
| ratelimit-limit | integer | Example: `150`. The rate limit for a given endpoint. |
| ratelimit-remaining | integer | Example: `100`. The number of requests remaining in the current window. |
| ratelimit-reset | integer | Example: `1528749846`. The time at which the rate limit window resets in UTC epoch seconds. |

### RESPONSE SCHEMA: application/json

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| to | (address_us or address_intl) (address) | required | |
| carrier | string | required | Default: `"USPS"` Value: `"USPS"` |
| id | string (snap_pack_id) `^ord_[0-9a-f]{26}$` | required | Unique identifier prefixed with `ord_`. |
| url | string (signed_link) | required | A signed link served over HTTPS. The link returned will expire in 30 days to prevent mis-sharing. Each time a GET request is initiated, a new signed URL will be generated. |
| use_type | string or null (snap_pack_use_type) | required | Enum: `"marketing"` `"operational"` `null`. The use type for each mailpiece. Can be one of marketing, operational, or null. Null use_type is only allowed if an account default use_type is selected in Account Settings. |
| description | string or null (resource_description) <= 255 characters | | An internal description that identifies this resource. Must be no longer than 255 characters. |
| metadata | object (metadata) <= 500 characters `[^"\\]{0,500}` | | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. |
| mail_type | string (mail_type) | | Default: `"usps_first_class"` Enum: `"usps_first_class"` `"usps_standard"`. |
| merge_variables | object or null (merge_variables) <= 25,000 characters | | Merge variable payload object for rendering dynamic content. |
| send_date | string or string (send_date) | | A timestamp in ISO 8601 format specifying when to send the letter off for production. |
| print_speed | string or null (print_speed) | | Default: `"core"` Value: `"core"`. `core` - 2 production business days. |
| size | string (snap_pack_size) | | Default: `"8.5x11"` Value: `"8.5x11"`. Specifies the size of the snap pack. |
| thumbnails | Array of objects (thumbnail) | | |
| expected_delivery_date | string \<date\> (expected_delivery_date) | | A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its send_date. |
| date_created | string \<date-time\> (date_created) | | A timestamp in ISO 8601 format of the date the resource was created. |
| date_modified | string \<date-time\> (date_modified) | | A timestamp in ISO 8601 format of the date the resource was last modified. |
| deleted | boolean (deleted) | | Only returned if the resource has been successfully deleted. |
| from | address obj with `name` defined (object) or address obj with `company` defined (object) (address_us) | | |
| outside_template_id | string or null `^tmpl_[a-zA-Z0-9]+$` | | The unique ID of the HTML template used for the outside of the snap pack. |
| inside_template_id | string or null `^tmpl_[a-zA-Z0-9]+$` | | The unique ID of the HTML template used for the inside of the snap pack. |
| outside_template_version_id | string or null `^vrsn_[a-zA-Z0-9]+$` | | The unique ID of the specific version of the HTML template used for the outside of the snap pack. |
| inside_template_version_id | string or null `^vrsn_[a-zA-Z0-9]+$` | | The unique ID of the specific version of the HTML template used for the inside of the snap pack. |
| object | string | | Default: `"snap_pack"` Value: `"snap_pack"`. Value is resource type. |
| tracking_events | Array of objects (tracking_event_normal) | | An array of tracking events ordered by ascending time. Not populated in test mode. |
| fsc | boolean | | Default: `false`. Contact support@lob.com or your account contact to learn more. Not available for snap_pack currently. |
| status | string (status) | | Enum: `"processed"` `"rendered"` `"failed"`. A string describing the PDF render status. |
| campaign_id | string or null (campaign_id) `^(cmp|camp)_[a-zA-Z0-9]+$` | | Denotes resources created by the provided campaign id, prefixed with `cmp_`. In the case of snap packs, booklets, and letters with size us_legal, however, the campaign id is prefixed with `camp_` instead of `cmp_`. |
| failure_reason | object or null | | An object describing the reason for failure if the resource failed to render. |
| color | boolean (color) | | Set this key to `true` if you would like to print in color. Set to `false` if you would like to print in black and white. |

**default** Error

## Request

```
POST /snap_packs
```

### Python Example

```python
snap_pack_editable = SnapPackEditable(
  description = "Demo Snap Pack job",
  _from = "adr_210a8d4b0b76d77b",
  inside = "<html style='padding: 1in; font-size: 50;'>Inside HTML for {{name}}</html>",
  outside = "<html style='padding: 1in; font-size: 20;'>Outside HTML for {{name}}</html>",
  to = AddressEditable(
    name = "Harry Zhang",
    address_line1 = "210 King St",
    address_line2 = "# 6100",
    address_city = "San Francisco",
    address_state = "CA",
    address_zip = "94107",
  ),
  merge_variables = MergeVariables(
    name = "Harry",
  ),
  use_type = "marketing",
  fsc = true,
  print_speed = "core"
)

with ApiClient(configuration) as api_client:
  api = SnapPacksApi(api_client)

try:
  created_snap_pack = api.create(snap_pack_editable)
except ApiException as e:
  print(e)
```

## Response Example

**200**

```json
{
  "id": "ord_0d6a16a3fff6318ac8f8008dc1",
  "description": "April Campaign",
  "to": {
    "id": "adr_bae820679f3f536b",
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
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "deleted": true,
    "object": "address"
  },
  "from": {
    "id": "adr_210a8d4b0b76d77b",
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
    "date_created": "2017-09-05T17:47:53.767Z",
    "date_modified": "2017-09-05T17:47:53.767Z",
    "deleted": true,
    "object": "address"
  },
  "url": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d.pdf?version=v1&expires=1618512040&signature=qvyCqXI1ndBvc4AjvG8FlirqLXEcfmYo4sDrRtabaXMOsX88to9G3K49uIk_aqevvZXe8HoRYD_nWydbQHqaCA",
  "outside_template_id": "tmpl_a3cb937f26d7eec",
  "inside_template_id": "tmpl_a3cb937f26d7eec",
  "inside_template_version_id": "vrsn_bfdf70893b00a85",
  "outside_template_version_id": "vrsn_bfdf70893b00a85",
  "carrier": "USPS",
  "tracking_events": [],
  "thumbnails": [
    {
      "small": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_small_1.png?version=v1&expires=1618512040&signature=-bipeUHP-hAMcCBSrWM0ZH1VwRdSPNVGGZN9hAZKr6Lh4ly6uxvratVd5LXJCK_zOEMYk_mTWASt0ge7OY6SDA",
      "medium": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_medium_1.png?version=v1&expires=1618512040&signature=ryxN7bsXGtw_GRFSP3Cs3A3IYjxZi3cW9BHDCNgMt6p3nobVmsc_iFHt2e-S7ndAXhhN7nP-MQVov3bt3r37BQ",
      "large": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_large_1.png?version=v1&expires=1618512040&signature=kBrm00xkyCkJNJRHxH8HshFaebtOxnzjVWOs1VVmGMuw8H6OBNcMAMxt9s49K0jlpHoh3Nr9uSncEZMQaaNjAg"
    },
    {
      "small": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_small_2.png?version=v1&expires=1618512040&signature=3gTgU7Fd3KoT_vNlQnTGptRps5ZgnkhSnPrAwk7L98higIzSwfKoLvuu_DIpMM48dHbxckKT9waR8euJ4KSDBQ",
      "medium": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_medium_2.png?version=v1&expires=1618512040&signature=Ue1lw5CMj7KRx6cMQL8xPeazaHCdJzWcACd1w3acuYPnWkVIpSt62OIO7hAtpAQK9xm1dhhlFj0rqRZMdRMMBA",
      "large": "https://lob-assets.com/order-creatives/ord_0d6a16a3fff6318ac8f8008dc1_comp_a20fd48ba4efda76ee827400d_thumb_large_2.png?version=v1&expires=1618512040&signature=cICc7HEm1xG_eyM4a_wtvPk2FqoLRmtgGa29kJisWnMIYBL0OkyzG4ZCYGMhp-5cZpJlSpXfTgGKh_Qmeo1TDw"
    }
  ],
  "merge_variables": {
    "name": null
  },
  "size": "8.5x11",
  "mail_type": "usps_first_class",
  "expected_delivery_date": "2021-03-24",
  "date_created": "2021-03-16T18:40:40.504Z",
  "date_modified": "2021-03-16T18:40:40.504Z",
  "send_date": "2021-03-16T18:45:40.493Z",
  "use_type": "marketing",
  "fsc": false,
  "color": false,
  "sla": "2",
  "object": "snap_pack"
}
```