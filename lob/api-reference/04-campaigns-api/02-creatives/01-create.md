# Create Creative

Creates a new creative with the provided properties.

## Authorization

`basicAuth`

## Header Parameters

| Parameter | Type | Description |
|---|---|---|
| `x-lang-output` | string | Enum: `"native"` `"match"`. `native` - Translate response to the native language of the country in the request. `match` - match the response to the language in the request. Default response is in English. |

## Request Body Schema

Content types: `application/json`, `application/x-www-form-urlencoded`, `multipart/form-data`

One of: **Postcard Creative** | **Letter Creative** | **Self Mailer Creative**

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `front` | `tmpl_id` (string) or `local_file_path` (string) (crv_front) | **Yes** | The artwork to use as the front of your postcard. Notes: HTML merge variables should not include delimiting whitespace. PDF, PNG, and JPGs must be sized at 4.25"x6.25", 6.25"x9.25", or 6.25"x11.25" at 300 DPI, while supplied HTML template will be rendered to the specified `size`. See here for HTML examples. |
| `back` | `tmpl_id` (string) or `local_file_path` (string) (crv_back) | **Yes** | The artwork to use as the back of your postcard creative. Notes: HTML merge variables should not include delimiting whitespace. PDF, PNG, and JPGs must be sized at 4.25"x6.25", 6.25"x9.25", or 6.25"x11.25" at 300 DPI, while supplied HTML template will be rendered to the specified `size`. Be sure to leave room for address and postage information by following the templates provided (4x6, 6x9, 6x11). See here for HTML examples. |
| `campaign_id` | string (Campaign id) `^cmp_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `cmp_`. |
| `resource_type` | string | **Yes** | Value: `"postcard"`. Mailpiece type for the creative. |
| `details` | object (writable) | **Yes** | Properties that the postcards in your Creative should have. See the `qr_code` attribute below to add a QR code to your creative. |
| `from` | `adr_id` (string) or address_editable_us (object) | No | Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification. |
| `description` | string or null (resource_description) <= 255 characters | No | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `metadata` | object (metadata) <= 500 characters `[^"\\]{0,500}` | No | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. See Metadata for more information. |

## Responses

### 200 - Creative created successfully

**Response Schema:** `application/json`

One of: **Postcard Creative** | **Letter Creative** | **Self Mailer Creative**

| Field | Type | Required | Description |
|---|---|---|---|
| `resource_type` | string | **Yes** | Value: `"postcard"`. Mailpiece type for the creative. |
| `details` | object (returned) | **Yes** | Properties that the postcards in your Creative should have. See the `qr_code` attribute below to add a QR code to your creative. |
| `date_created` | string \<date-time\> (date_created) | **Yes** | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string \<date-time\> (date_modified) | **Yes** | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string | **Yes** | Default: `"creative"`. Value is resource type. |
| `id` | string (crv_id) `^crv_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `crv_`. |
| `description` | string or null (resource_description) <= 255 characters | **Yes** | An internal description that identifies this resource. Must be no longer than 255 characters. |
| `from` | `adr_id` (string) or address_editable_us (object) | **Yes** | Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification. |
| `metadata` | object (metadata) <= 500 characters `[^"\\]{0,500}` | **Yes** | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. See Metadata for more information. |
| `template_preview_urls` | object (Template Preview URLs) | **Yes** | Preview URLs associated with a creative's artwork asset(s) if the creative uses HTML templates as assets. An empty object will be returned if no `template_preview`s have been generated. |
| `template_previews` | Array of objects (Template Previews) | **Yes** | A list of template preview objects if the creative uses HTML template(s) as artwork asset(s). An empty array will be returned if no `template_preview`s have been generated for the creative. |
| `campaigns` | Array of objects (campaign_list) | **Yes** | Array of campaigns associated with the creative ID. |
| `deleted` | boolean | **Yes** | Only returned if the resource has been successfully deleted. |

### default - Error

## Request Samples

### Payload

```json
{
  "campaign_id": "cmp_e05ee61ff80764b",
  "resource_type": "postcard",
  "description": "Our 4x6 postcard creative",
  "details": {}
}
```

## Response Samples

### 200

```json
{
  "id": "crv_2a3b096c409b32c",
  "description": "Our 4x6 postcard creative",
  "from": "adr_210a8d4b0b76d77b",
  "resource_type": "postcard",
  "details": {},
  "metadata": {},
  "template_preview_urls": {},
  "template_previews": [],
  "campaigns": [],
  "date_created": "2017-09-05T17:47:53.767Z",
  "date_modified": "2017-09-05T17:47:53.767Z",
  "object": "creative"
}
```