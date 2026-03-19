# Update a Link

Update any of the properties of a shortened link.

**Method:** `PATCH /links/{link_id}`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `link_id` | string | **Yes** | Unique identifier for a link. |

## Request Body Schema

Content types: `application/json`, `application/x-www-form-urlencoded`, `multipart/form-data`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `redirect_link` | string (redirect_link) | **Yes** | The original target URL. |
| `title` | string | No | The title of the URL. |
| `metadata` | object (metadata) <= 500 characters `[^"\\]{0,500}` | No | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. See Metadata for more information. |

## Responses

### 200 - Returns the updated link.

**Response Schema:** `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier prefixed with `lnk_`. |
| `title` | string | The title of the URL. |
| `domain_id` | string | A unique identifier for the registered domain. |
| `redirect_link` | string (redirect_link) | The original target URL. |
| `short_link` | string | The shortened URL for the associated original URL. |
| `metadata` | object (metadata) <= 500 characters `[^"\\]{0,500}` | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. See Metadata for more information. |
| `created_at` | string | The date and time the link was created. |
| `updated_at` | string | The date and time the link was last updated. |

### default - Error

## Request Samples

### Payload

```json
{
  "resource_id": "ltr_133"
}
```

## Response Samples

### 200

```json
{
  "id": "string",
  "title": "string",
  "domain_id": "string",
  "redirect_link": "string",
  "short_link": "string",
  "metadata": {
    "property1": "string",
    "property2": "string"
  },
  "created_at": "string",
  "updated_at": "string"
}
```