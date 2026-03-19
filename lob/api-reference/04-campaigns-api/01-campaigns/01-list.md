# List Campaigns

Returns a list of your campaigns. The campaigns are returned sorted by creation date, with the most recently created campaigns appearing first.

## Authorization

`basicAuth`

## Query Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `limit` | integer [1..100] | 10 | How many results to return. |
| `include` | Array of strings | — | Request that the response include the total count by specifying `include=["total_count"]`. |
| `before/after` | object or object | — | `before` and `after` are both optional but only one of them can be in the query at a time. |

## Responses

### 200

A dictionary with a data property that contains an array of up to `limit` campaigns. Each entry in the array is a separate campaign. The previous and next page of campaigns can be retrieved by calling the endpoint contained in the `previous_url` and `next_url` fields in the API response respectively. If no more campaigns are available beyond the current set of returned results, the `next_url` field will be empty.

#### Response Schema: `application/json`

| Field | Type | Description |
|---|---|---|
| `object` | string | Value is resource type. |
| `next_url` | string or null | Url of next page of items in list. |
| `previous_url` | string or null | Url of previous page of items in list. |
| `count` | integer | Number of resources in a set. |
| `total_count` | integer | Indicates the total number of records. Provided when the request specifies an "include" query parameter. |
| `data` | Array of objects (campaign) | List of campaigns. |

## Request Samples

### CURL

```bash
curl https://api.lob.com/v1/campaigns \
  -u <YOUR API KEY>:
```

## Response Samples

### 200

```json
{
  "data": [
    {
      "id": "cmp_e05ee61ff80764b",
      "billing_group_id": "bg_fe3079dcdd80e5ae",
      "name": "My Campaign",
      "description": "My Campaign's description",
      "schedule_type": "immediate",
      "send_date": null,
      "target_delivery_date": null,
      "cancel_window_campaign_minutes": 60,
      "metadata": {},
      "use_type": "marketing",
      "is_draft": true,
      "deleted": false,
      "creatives": [],
      "uploads": [],
      "auto_cancel_if_ncoa": false,
      "date_created": "2017-09-05T17:47:53.767Z",
      "date_modified": "2017-09-05T17:47:53.767Z",
      "object": "campaign"
    }
  ],
  "object": "list",
  "previous_url": null,
  "next_url": null,
  "count": 1
}
```