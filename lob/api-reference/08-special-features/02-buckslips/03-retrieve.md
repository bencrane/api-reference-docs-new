# Buckslips — Retrieve

Retrieves the details of an existing buckslip. You need only supply the unique customer identifier that was returned upon buckslip creation.

## AUTHORIZATIONS

`basicAuth`

## PATH PARAMETERS

| Parameter | Type | Required | Description |
|---|---|---|---|
| `buckslip_id` | string (`^bck_[a-zA-Z0-9]+$`) | Yes | id of the buckslip. |

## Responses

### 200 — Returns a buckslip object.

#### RESPONSE SCHEMA: `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (`^bck_[a-zA-Z0-9]+$`) | Yes | Unique identifier prefixed with `bck_`. |
| `description` | string or null (<= 255 chars) | Yes | Description of the buckslip. |
| `url` | string (uri) [ 1 .. 2083 ] chars | Yes | The signed link for the buckslip. |
| `raw_url` | string (uri) [ 1 .. 2083 ] chars | Yes | The raw URL of the buckslip. |
| `front_original_url` | string (uri) [ 1 .. 2083 ] chars | Yes | The original URL of the front template. |
| `back_original_url` | string (uri) [ 1 .. 2083 ] chars | Yes | The original URL of the back template. |
| `thumbnails` | Array of objects (`thumbnail`) | Yes | Thumbnail images of the buckslip. |
| `size` | string | No | Default: `"8.75x3.75"`. The size of the buckslip. |
| `auto_reorder` | boolean | Yes | Default: `false`. True if the buckslips should be auto-reordered. |
| `reorder_quantity` | integer or null | Yes | The number of buckslips to be reordered. |
| `threshold_amount` | integer | Yes | Default: `0`. The threshold amount of the buckslip. |
| `available_quantity` | number | Yes | Default: `0`. The available quantity of buckslips. |
| `allocated_quantity` | number | Yes | Default: `0`. The allocated quantity of buckslips. |
| `onhand_quantity` | number | Yes | Default: `0`. The onhand quantity of buckslips. |
| `pending_quantity` | number | Yes | Default: `0`. The pending quantity of buckslips. |
| `projected_quantity` | number | Yes | Default: `0`. The sum of pending and onhand quantities of buckslips. |
| `buckslip_orders` | Array of objects (`buckslip_order`) | Yes | An array of buckslip orders that are associated with the buckslip. |
| `stock` | string | Yes | Enum: `"text"`, `"cover"`. The stock of the buckslip. |
| `weight` | string | Yes | Value: `"80#"`. The weight of the buckslip. |
| `finish` | string | Yes | Enum: `"gloss"`, `"matte"`. The finish of the buckslip. |
| `status` | string | Yes | Enum: `"processed"`, `"rendered"`, `"failed"`. The status of the buckslip. |
| `deleted` | boolean | No | Only returned if the resource has been successfully deleted. |
| `date_created` | string (date-time) | Yes | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string (date-time) | Yes | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string | Yes | Default: `"buckslip"`. Value is resource type. |

### default — Error

---

## Endpoint

`GET /buckslips/{buckslip_id}`

## Request Sample

```shell
curl https://api.lob.com/v1/buckslips/bck_7a6d73c5c8457fc \
  -u <YOUR API KEY>:
```

## Response Sample (200)

**Content type:** `application/json`

```json
{
  "id": "bck_7a6d73c5c8457fc",
  "account_id": "fa9ea650fc7b31a89f92",
  "description": "Test buckslip",
  "url": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e.pdf?version=v1&expires=1636910992&signature=mnsDH2DAxdkN9VibdlLMxJC86sME5WYDqkNtmvGwdNsAaUWfbnv0rJhJ1mR8Ol4uxQq61j5wYZ0r3s-lBkQfDA",
  "size": "8.75x3.755",
  "auto_reorder": false,
  "reorder_quantity": null,
  "threshold_amount": 0,
  "raw_url": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "front_original_url": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "back_original_url": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_raw.pdf?version=v1&expires=1636910992&signature=-bZo31FMAp2vmNaZKyXn_Qa4APqwtNinw76FrQ7uyQejFZw6VBQQYfoiQ642iXh0H2K5i2aOo8_BAkt3UJdVDw",
  "thumbnails": [
    {
      "small": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_thumb_small_1.png?version=v1&expires=1636910992&signature=mrv8JDvpZK4I8WUGH0tPdtK-My5oes0Ltj_gL7BDw96SpCTTeZFHkz81SzclyFP9dQRtlsvAsjcuGcTBvCvOCg",
      "medium": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_thumb_medium_1.png?version=v1&expires=1636910992&signature=VgL_2Ckm_kxKiWGgWtdNoy9HHOn8dGYSVOn7UqyCbwdbVlUtx28TRN4Bo8Iru3n0keKp9He0YhKT1ILotznMDA",
      "large": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_thumb_large_1.png?version=v1&expires=1636910992&signature=FKSzymA13j-CQ0uk20cGHZTzT3vimzNBYrgp-xifLFg4mMdo1BZALR5O0aF_jVhsX614hKP35ONdYl47TQxXAw"
    },
    {
      "small": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_thumb_small_2.png?version=v1&expires=1636910992&signature=IWsmPa_ULlv2yyqjX564d_YfHHY_M7i9YxDnw-WXDr2jtOFcArmRZQbnHeE9g_rYxnddJbgosuv8-c2utiu7Cg",
      "medium": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_thumb_medium_2.png?version=v1&expires=1636910992&signature=zxK7VKGiTvz5Ywrkaydd0v3GcYf58R7A08J4tNfI7-aiNODDcTF3l0MqY13n9Pyc8RXSdD0XVBY-OpbA1VM-Ag",
      "large": "https://lob-assets.com/buckslips/bck_c51ae96f5cebf3e_thumb_large_2.png?version=v1&expires=1636910992&signature=r0OFUhh315ZwN0raMZdIwJd2oCIEYsz0BABaMxIuO1PKTD0ckGWrhcGdzk2dlWQ6vSvp0CUQ5k1RXGqkIIqkDw"
    }
  ],
  "available_quantity": 0,
  "allocated_quantity": 0,
  "onhand_quantity": 0,
  "pending_quantity": 0,
  "projected_quantity": 0,
  "buckslip_orders": [],
  "stock": "text",
  "weight": "80#",
  "finish": "gloss",
  "status": "rendered",
  "mode": "test",
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "object": "buckslip"
}
```