# Tracking Events Webhook

Information about tracking events.

## Authorization

`basicAuth`

## Responses

### 200 - Returns a `tracking_event` object to the specified server.

**Response Schema:** `application/json`

One of: **tracking_event_normal** | **tracking_event_certified**

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (evnt_id) `^evnt_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `evnt_`. |
| `date_created` | string \<date-time\> (date_created) | **Yes** | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string \<date-time\> (date_modified) | **Yes** | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string | **Yes** | Default: `"tracking_event"`. Value is resource type. |
| `type` | string | **Yes** | Value: `"normal"`. Non-Certified postcards, self mailers, letters, checks and snap packs. |
| `name` | string | **Yes** | Enum: `"Mailed"` `"In Transit"` `"In Local Area"` `"Processed for Delivery"` `"Delivered"` `"Re-Routed"` `"Returned to Sender"` `"International Exit"`. Name of tracking event (for normal postcards, self mailers, letters, checks and snap packs): `Mailed` - The mailpiece has been handed off to and accepted by USPS and is en route. Note this data is only available in Enterprise editions of Lob. Contact Sales if you want access to this feature. `In Transit` - The mailpiece is being processed at the entry/origin facility. `In Local Area` - The mailpiece is being processed at the destination facility. `Processed for Delivery` - The mailpiece has been greenlit for delivery at the recipient's nearest postal facility. The mailpiece should reach the mailbox within 1 business day of this tracking event. `Delivered` - The mail piece has been delivered to the recipient's address. The final scan is generated when the mail carrier's GPS unit leaves the delivery area. `Re-Routed` - The mailpiece is re-routed due to recipient change of address, address errors, or USPS relabeling of barcode/ID tag area. `Returned to Sender` - The mailpiece is being returned to sender due to barcode, ID tag area, or address errors. `International Exit` - The mail piece has been processed to ship to a destination abroad. This is typically the last scan a US-originated international mail piece will receive from the USPS. |
| `time` | string \<date-time\> | No | A timestamp in ISO 8601 format of the date USPS registered the event. |
| `details` | object or null | No | Value: `null`. Will be `null` for `type=normal` events. |
| `location` | string or null | No | The zip code in which the scan event occurred. Null for `Mailed` events. |

## Response Samples

### 200 (normal)

```json
{
  "id": "evnt_9e84094c9368cfb",
  "type": "normal",
  "name": "In Local Area",
  "details": null,
  "location": "72231",
  "time": "2016-06-30T15:51:41.000Z",
  "date_created": "2016-06-30T17:41:59.771Z",
  "date_modified": "2016-06-30T17:41:59.771Z",
  "object": "tracking_event"
}
```