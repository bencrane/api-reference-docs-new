# Card Orders — Create

Creates a new card order given information.

## AUTHORIZATIONS

`basicAuth`

## PATH PARAMETERS

| Parameter | Type | Required | Description |
|---|---|---|---|
| `card_id` | string (`^card_[a-zA-Z0-9]+$`) | Yes | The ID of the card to which the card orders belong. |

## REQUEST BODY SCHEMA

`application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `quantity` | integer [ 10000 .. 10000000 ] | Yes | The quantity of cards in the order (minimum 10,000). |

## Responses

### 200 — Card order created successfully.

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (`^co_[a-zA-Z0-9]+$`) | No | Unique identifier prefixed with `co_`. |
| `card_id` | string (`^card_[a-zA-Z0-9]+$`) | No | Unique identifier prefixed with `card_`. |
| `status` | string | No | Enum: `"pending"`, `"printing"`, `"available"`, `"cancelled"`, `"depleted"`. The status of the card order. |
| `inventory` | number | No | Default: `0`. The inventory of the card order. |
| `quantity_ordered` | number | No | Default: `0`. The quantity of cards ordered. |
| `unit_price` | number | No | Default: `0`. The unit price for the card order. |
| `cancelled_reason` | string | No | The reason for cancellation. |
| `availability_date` | string (date-time) | No | A timestamp in ISO 8601 format of the date the resource was created. |
| `expected_availability_date` | string (date-time) | No | The fixed deadline for the cards to be printed. |
| `date_created` | string (date-time) | Yes | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string (date-time) | Yes | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string | Yes | Value is resource type. |
| `deleted` | boolean | No | Only returned if the resource has been successfully deleted. |

### default — Error

---

## Endpoint

`POST /cards/{card_id}/orders`

## Request Sample

**Content type:** `application/json`

```json
{
  "quantity": 10000
}
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "co_e0f8a0562a06bea7f",
  "card_id": "card_6afffd19045076c",
  "status": "available",
  "inventory": 9500,
  "quantity_ordered": 10000,
  "unit_price": 0.75,
  "cancelled_reason": "No longer needed",
  "availability_date": "2021-10-12T21:41:48.326Z",
  "expected_availability_date": "2021-11-04T21:03:18.871Z",
  "date_created": "2021-10-07T21:03:18.871Z",
  "date_modified": "2021-10-16T01:00:30.144Z",
  "object": "card_order"
}
```