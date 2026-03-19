# Delete Upload

Delete an existing upload. You need only supply the unique identifier that was returned upon upload creation.

**Method:** `DELETE /uploads/{upl_id}`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upl_id` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | id of the upload |

## Responses

### 204 - Successful Response

## Request Samples

### cURL

```bash
curl -X DELETE https://api.lob.com/v1/uploads/upl_71be866e430b11e9 \
  -u <YOUR API KEY>:
```