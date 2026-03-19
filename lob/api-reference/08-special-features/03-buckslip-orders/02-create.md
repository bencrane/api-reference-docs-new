# Create

Creates a new buckslip order given information.

**AUTHORIZATIONS:** basicAuth

## PATH PARAMETERS

| Parameter | Type | Description |
|-----------|------|-------------|
| `buckslip_id` (required) | string (buckslip_id) `^bck_[a-zA-Z0-9]+$` | The ID of the buckslip to which the buckslip orders belong. |

## REQUEST BODY SCHEMA

`application/json` | `application/x-www-form-urlencoded` | `multipart/form-data`

| Field | Type | Description |
|-------|------|-------------|
| `quantity` (required) | integer [5000 .. 10000000] | The quantity of buckslips in the order (minimum 5,000). |

## Responses

### 200
Buckslip order created successfully

**RESPONSE SCHEMA:** application/json

| Field | Type | Description |
|-------|------|-------------|
| `date_created` (required) | string \<date-time\> (date_created) | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` (required) | string \<date-time\> (date_modified) | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` (required) | string (object) | Value is resource type. |
| `deleted` | boolean (deleted) | Only returned if the resource has been successfully deleted. |
| `id` | string (bo_id) `^bo_[a-zA-Z0-9]+$` | Unique identifier prefixed with `bo_`. |
| `buckslip_id` | string (buckslip_id) `^bck_[a-zA-Z0-9]+$` | Unique identifier prefixed with `bck_`. |
| `status` | string | Enum: `"pending"` `"printing"` `"available"` `"cancelled"` `"depleted"` — The status of the buckslip order. |
| `quantity_ordered` | number (Default: 0) | The quantity of buckslips ordered. |
| `unit_price` | number (Default: 0) | The unit price for the buckslip order. |
| `inventory` | number (Default: 0) | The inventory of the buckslip order. |
| `cancelled_reason` | string | The reason for cancellation. |
| `availability_date` | string \<date-time\> | A timestamp in ISO 8601 format of the date the resource was created. |
| `expected_availability_date` | string \<date-time\> | The fixed deadline for the buckslips to be printed. |

### default
Error

## Request samples

**Payload** — Content type: application/json

```json
{
  "quantity": 10000
}
```

**CURL**

```bash
curl https://api.lob.com/v1/buckslips/bck_6afffd19045076c/orders/ \
  -u <YOUR API KEY>: \
  -d '{"quantity": 10000}'
```

## Response samples

**200** — Content type: application/json

```json
{
  "id": "bo_e0f8a0562a06bea7f",
  "buckslip_id": "bck_6afffd19045076c",
  "status": "available",
  "quantity_ordered": 10000,
  "unit_price": 0.75,
  "cancelled_reason": "No longer needed",
  "availability_date": "2021-10-12T21:41:48.326Z",
  "expected_availability_date": "2021-11-04T21:03:18.871Z",
  "date_created": "2021-10-07T21:03:18.871Z",
  "date_modified": "2021-10-16T01:00:30.144Z",
  "object": "buckslip_order"
}
```