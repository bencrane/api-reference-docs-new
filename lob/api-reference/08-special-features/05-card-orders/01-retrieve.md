# Card Orders — Retrieve

Retrieves the card orders associated with the given card id.

## AUTHORIZATIONS

`basicAuth`

## PATH PARAMETERS

| Parameter | Type | Required | Description |
|---|---|---|---|
| `card_id` | string (`^card_[a-zA-Z0-9]+$`) | Yes | The ID of the card to which the card orders belong. |

## QUERY PARAMETERS

| Parameter | Type | Default | Description |
|---|---|---|---|
| `limit` | integer [ 1 .. 100 ] | `10` | How many results to return. |
| `offset` | integer | `0` | An integer that designates the offset at which to begin returning results. |

## Responses

### 200 — Returns the card orders associated with the given card id.

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Description |
|---|---|---|
| `object` | string | Value is resource type. |
| `next_url` | string or null | Url of next page of items in list. |
| `previous_url` | string or null | Url of previous page of items in list. |
| `count` | integer | Number of resources in a set. |
| `total_count` | integer | Indicates the total number of records. Provided when the request specifies an "include" query parameter. |
| `data` | Array of objects (`card_order`) | List of card orders. |

### default — Error

---

## Endpoint

`GET /cards/{card_id}/orders`

## Request Sample

```shell
curl https://api.lob.com/v1/cards/card_6afffd19045076c/orders/ \
  -u <YOUR API KEY>:
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "data": [
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
  ],
  "object": "list",
  "next_url": null,
  "previous_url": null,
  "count": 1
}
```