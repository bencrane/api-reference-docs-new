# Delete Campaign

Delete an existing campaign. You need only supply the unique identifier that was returned upon campaign creation. Deleting a campaign also deletes any associated mail pieces that have been created but not sent. A campaign's `send_date` matches its associated mail pieces' `send_date`s.

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Description |
|---|---|---|
| `cmp_id` (required) | string `^cmp_[a-zA-Z0-9]+$` | id of the campaign |

## Responses

### 200 — Deleted the campaign.

#### Response Schema: `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string `^cmp_[a-zA-Z0-9]+$` | Unique identifier prefixed with `cmp_`. |
| `deleted` | boolean | True if the resource has been successfully deleted. |

## Request Samples

### CURL

```bash
curl -X DELETE https://api.lob.com/v1/campaigns/cmp_e05ee61ff80764b \
  -u <YOUR API KEY>:
```

## Response Samples

### 200

```json
{
  "id": "cmp_e05ee61ff80764b",
  "deleted": true
}
```