# Create

Creates a new card given information.

**AUTHORIZATIONS:** basicAuth

## REQUEST BODY SCHEMA

`application/json`

| Field | Type | Description |
|-------|------|-------------|
| `front` (required) | remote_file_url (string) or local_file_path (string) | A PDF template for the front of the card. |
| `description` | string or null (card_description) \<= 255 characters | Description of the card. |
| `size` | string (Default: `"2.125x3.375"`) | Enum: `"3.375x2.125"` `"2.125x3.375"` — The size of the card. |
| `back` | remote_file_url (string) or local_file_path (string) (Default: `"https://s3.us-west-2.amazonaws.com/public.lob.com/assets/card_blank_horizontal.pdf"`) | A PDF template for the back of the card. |

## Responses

### 200
Card created successfully

**RESPONSE SCHEMA:** application/json

| Field | Type | Description |
|-------|------|-------------|
| `date_created` (required) | string \<date-time\> (date_created) | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` (required) | string \<date-time\> (date_modified) | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` (required) | string (Default: `"card"`, Value: `"card"`) | Value is resource type. |
| `description` (required) | string or null (card_description) \<= 255 characters | Description of the card. |
| `id` (required) | string (card_id) `^card_[a-zA-Z0-9]+$` | Unique identifier prefixed with `card_`. |
| `url` (required) | string \<uri\> [1 .. 2083] characters | The signed link for the card. |
| `auto_reorder` (required) | boolean (Default: false) | True if the cards should be auto-reordered. |
| `reorder_quantity` (required) | integer or null | The number of cards to be reordered. |
| `raw_url` (required) | string \<uri\> [1 .. 2083] characters | The raw URL of the card. |
| `front_original_url` (required) | string \<uri\> [1 .. 2083] characters | The original URL of the front template. |
| `back_original_url` (required) | string \<uri\> [1 .. 2083] characters | The original URL of the back template. |
| `thumbnails` (required) | Array of objects (thumbnail) | |
| `available_quantity` (required) | integer (Default: 0) | The available quantity of cards. |
| `pending_quantity` (required) | integer (Default: 0) | The pending quantity of cards. |
| `status` (required) | string | Enum: `"processed"` `"rendered"` — The status of the card. |
| `orientation` (required) | string (Default: `"horizontal"`) | Enum: `"horizontal"` `"vertical"` — The orientation of the card. |
| `threshold_amount` (required) | integer (Default: 0) | The threshold amount of the card. |
| `deleted` | boolean (deleted) | Only returned if the resource has been successfully deleted. |
| `size` | string (Default: `"2.125x3.375"`) | Enum: `"3.375x2.125"` `"2.125x3.375"` — The size of the card. |

### default
Error

## Request samples

**Payload** — Content type: application/json

```json
{
  "description": "Test card",
  "front": "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf",
  "back": "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf",
  "size": "2.125x3.375"
}
```

## Response samples

**200** — Content type: application/json

```json
{
  "id": "card_7a6d73c5c8457fc",
  "account_id": "fa9ea650fc7b31a89f92",
  "description": "Test card",
  "url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
  "size": "2.125x3.375",
  "auto_reorder": false,
  "reorder_quantity": null,
  "raw_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "front_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "back_original_url": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "thumbnails": [
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_1.png?version=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_1.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQxXAw"
    },
    {
      "small": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_small_2.png?version=v1&expires=1636910992&signature=IWsmPa_ULlv2yyqjX564d_YfHHY_M7i9YxDnw-WXDr2jtOFcArmRZQbnHeE9g_rYxnddJbgosuv8-c2utiu7Cg",
      "medium": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_medium_2.png?version=v1&expires=1636910992&signature=zxK7VKGiTvz5Ywrkaydd0v3GcYf58R7A08J4tNfI7-aiNODDcTF3l0MqY13n9Pyc8RXSdD0XVBY-OpbA1VM-Ag",
      "large": "https://lob-assets.com/cards/card_c51ae96f5cebf3e_thumb_large_2.png?version=v1&expires=1636910992&signature=r0OFUhh315ZwN0raMZdIwJd2oCIEYsz0BABaMxIuO1PKTD0ckGWrhcGdzk2dlWQ6vSvp0CUQ5k1RXGqkIIqkDw"
    }
  ],
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
```