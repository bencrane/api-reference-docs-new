# List All Links

Retrieves a list of shortened links. The list is sorted by creation date, with the most recently created appearing first.

**Method:** `GET /links`

## Authorization

`basicAuth`

## Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `limit` | integer [1..100] | No | Default: `10`. Example: `limit=10`. How many results to return. |
| `before/after` | object or object | No | `before` and `after` are both optional but only one of them can be in the query at a time. |
| `campaign_id` | string or null (campaign_id) `^(cmp|camp)_[a-zA-Z0-9]+$` | No | Filters resources created by the provided campaign id, prefixed with `cmp_`. In the case of snap packs, booklets, and letters with size `us_legal`, however, the campaign id is prefixed with `camp_` instead of `cmp_`. |
| `domain_id` | string `^(dom)_[a-zA-Z0-9]+$` | No | Filters links by the provided domain id. |

## Responses

### 200 - Returns the deleted link object.

**Response Schema:** `application/json`

| Field | Type | Description |
|---|---|---|
| `object` | string (object) | Value is resource type. |
| `next_url` | string or null | Url of next page of items in list. |
| `previous_url` | string or null | Url of previous page of items in list. |
| `count` | integer (count) | Number of resources in a set. |
| `total_count` | integer | Indicates the total number of records. Provided when the request specifies an "include" query parameter. |
| `data` | Array of objects (link_response) | List of links. |

### default - Error

## Request Samples

### cURL

```bash
curl -X GET "https://api.lob.com/v1/links?limit=2" \
  -u <YOUR_LIVE_API_KEY>:
```

## Response Samples

### 200

```json
{
  "object": "string",
  "next_url": "string",
  "previous_url": "string",
  "count": 0,
  "total_count": 0,
  "data": [
    {
      "id": "string",
      "title": "string",
      "domain_id": "string",
      "redirect_link": "string",
      "short_link": "string",
      "metadata": {},
      "created_at": "string",
      "updated_at": "string"
    }
  ]
}
```