# Delete Link

Delete the shortened link.

**Method:** `DELETE /links/{link_id}`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `link_id` | string | **Yes** | Unique identifier for a link. |

## Responses

### 200 - Returns the deleted short link object

**Response Schema:** `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for a link. |
| `deleted` | boolean | Only returned if the link was successfully deleted. |

### default - Error

## Response Samples

### 200

```json
{
  "id": "string",
  "deleted": true
}
```