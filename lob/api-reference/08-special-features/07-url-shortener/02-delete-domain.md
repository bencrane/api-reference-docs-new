# Delete a Domain

Delete a registered domain. This operation can only be performed if all associated links with the domain are deleted.

**Method:** `DELETE /domains/{domain_id}`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `domain_id` | string | **Yes** | Unique identifier for a domain. |

## Responses

### 200 - Returns the deleted link object.

**Response Schema:** `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for a domain. |
| `deleted` | boolean | Only returned if the domain was successfully deleted. |

### default - Error

## Response Samples

### 200

```json
{
  "id": "string",
  "deleted": true
}
```