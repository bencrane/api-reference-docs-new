# Buckslips — Delete

Delete an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

## AUTHORIZATIONS

`basicAuth`

## PATH PARAMETERS

| Parameter | Type | Required | Description |
|---|---|---|---|
| `buckslip_id` | string (`^bck_[a-zA-Z0-9]+$`) | Yes | id of the buckslip. |

## Responses

### 200 — Deleted the buckslip.

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Description |
|---|---|---|
| `id` | string (`^bck_[a-zA-Z0-9]+$`) | Unique identifier prefixed with `bck_`. |
| `deleted` | boolean | Only returned if the resource has been successfully deleted. |

### default — Error

---

## Endpoint

`DELETE /buckslips/{buckslip_id}`

## Request Sample

```shell
curl -X DELETE https://api.lob.com/v1/buckslips/bck_7a6d73c5c8457fc \
  -u <YOUR API KEY>:
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "buckslip_123456789",
  "deleted": true
}
```