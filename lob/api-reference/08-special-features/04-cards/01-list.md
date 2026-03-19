# List

Returns a list of your cards. The cards are returned sorted by creation date, with the most recently created addresses appearing first.

**AUTHORIZATIONS:** basicAuth

## QUERY PARAMETERS

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | integer [1 .. 100] | 10 | How many results to return. |
| `before/after` | object or object | — | `before` and `after` are both optional but only one of them can be in the query at a time. |
| `include` | Array of strings | — | Request that the response include the total count by specifying `include=["total_count"]`. |

## Responses

### 200
Returns a list of card objects

**RESPONSE SCHEMA:** application/json

| Field | Type | Description |
|-------|------|-------------|
| `object` | string (object) | Value is resource type. |
| `next_url` | string or null | Url of next page of items in list. |
| `previous_url` | string or null | Url of previous page of items in list. |
| `count` | integer (count) | Number of resources in a set. |
| `total_count` | integer | Indicates the total number of records. Provided when the request specifies an "include" query parameter. |
| `data` | Array of objects (card) | List of cards. |

### default
Error

## Request samples

**CURL**

```bash
curl -X GET "https://api.lob.com/v1/cards?limit=2" \
  -u <YOUR API KEY>:
```

## Response samples

**200** — Content type: application/json

```json
{
  "data": [
    {
      "id": "card_7a6d73c5c8457fc",
      "account_id": "fa9ea650fc7b31a89f92",
      "description": null,
      "url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
      "size": "2.125x3.375",
      "auto_reorder": false,
      "reorder_quantity": null,
      "raw_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
      "front_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
      "back_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
      "thumbnails": [],
      "available_quantity": 10000,
      "pending_quantity": 0,
      "countries": null,
      "status": "rendered",
      "mode": "test",
      "orientation": "horizontal",
      "threshold_amount": 0,
      "date_created": "2021-03-24T22:51:42.838Z",
      "date_modified": "2021-03-24T22:51:42.838Z",
      "send_date": "2021-03-24T22:51:42.838Z",
      "object": "card"
    }
  ],
  "object": "list",
  "previous_url": null,
  "next_url": null,
  "count": 1
}
```