# Retrieve Creative

Retrieves the details of an existing creative. You need only supply the unique creative identifier that was returned upon creative creation.

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `crv_id` | string (crv_id) `^crv_[a-zA-Z0-9]+$` | **Yes** | id of the creative. Example: `crv_2a3b096c409b32c` |

## Responses

### 200 - Returns a creative object

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

### cURL

```bash
curl https://api.lob.com/v1/creatives/crv_2a3b096c409b32c \
  -u <YOUR API KEY>:
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