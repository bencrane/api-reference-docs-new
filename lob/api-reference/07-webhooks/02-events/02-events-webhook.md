# Events Webhook

Information about an event.

## Authorization

`basicAuth`

## Responses

### 200 - Returns an `event` object to the specified server.

**Response Schema:** `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string `^evt_[a-zA-Z0-9_]+$` | **Yes** | Unique identifier prefixed with `evt_`. |
| `body` | object | **Yes** | The body of the associated resource as they were at the time of the event, i.e. the postcard object, the letter object, the check object, the address object, or the bank account object. For `.deleted` events, the body matches the response for the corresponding delete endpoint for that resource (e.g. the postcard delete response). |
| `reference_id` | string | **Yes** | Unique identifier of the related resource for the event. |
| `event_type` | object (event_type) | **Yes** | The type of event that occurred. |
| `date_created` | string \<date-time\> (date_created) | **Yes** | A timestamp in ISO 8601 format of the date the resource was created. |
| `object` | string | **Yes** | Default: `"event"`. Value is resource type. |

## Response Samples

### 200

```json
{
  "event_type": {
    "resource": "postcards",
    "enabled_for_test": true,
    "id": "postcard.created",
    "object": "event_type"
  },
  "reference_id": "psc_d2d10a2e9cba991c",
  "id": "evt_d95ff8ffd2b5cfb4",
  "date_created": "2016-12-04T22:50:08.180Z",
  "body": {
    "id": "psc_d2d10a2e9cba991c",
    "description": "Test Postcard",
    "metadata": {},
    "to": {
      "id": "adr_8e783523dd7f0e70",
      "description": "Test Recipient Address",
      "name": "Harry Zhang",
      "company": "LOB",
      "phone": null,
      "email": null,
      "address_line1": "123 TEST ST",
      "address_line2": "UNIT 1",
      "address_city": "SAN FRANCISCO",
      "address_state": "CA",
      "address_zip": "94107",
      "address_country": "UNITED STATES",
      "metadata": {},
      "date_created": "2016-12-04T10:51:51.844Z",
      "date_modified": "2016-12-04T10:51:51.844Z",
      "object": "address"
    },
    "from": {
      "id": "adr_d2e26faf793ed422",
      "description": "Test Sender Address",
      "name": "Harry Zhang",
      "company": "LOB",
      "phone": null,
      "email": null,
      "address_line1": "123 TEST ST",
      "address_line2": "UNIT 1",
      "address_city": "SAN FRANCISCO",
      "address_state": "CA",
      "address_zip": "94107",
      "address_country": "UNITED STATES",
      "metadata": {},
      "date_created": "2016-12-04T10:51:51.845Z",
      "date_modified": "2016-12-04T10:51:51.845Z",
      "object": "address"
    },
    "url": "https://lob-assets.com/postcards/psc_d2d10a2e9cba991c.pdf?expires=1540372221&signature=dNE8OtbDymujUxBIMYle4H1cv1aZNFk",
    "front_template_id": null,
    "back_template_id": null,
    "carrier": "USPS",
    "tracking_events": [],
    "thumbnails": [
      {},
      {}
    ],
    "merge_variables": null,
    "mail_type": "usps_first_class",
    "size": "4x6",
    "expected_delivery_date": "2016-12-09",
    "date_created": "2016-12-04T10:51:51.843Z",
    "date_modified": "2016-12-04T10:51:51.843Z",
    "send_date": "2016-12-04T10:56:51.843Z",
    "object": "postcard"
  },
  "object": "event"
}
```