# List QR Codes

Returns a list of your QR codes. The QR codes are returned sorted by scan date, with the most recently scanned QR codes appearing first.

**Method:** `GET /qr_code_analytics`

## Authorization

`basicAuth`

## Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `limit` | integer [1..100] | No | Default: `10`. Example: `limit=10`. How many results to return. |
| `offset` | integer | No | Default: `0`. An integer that designates the offset at which to begin returning results. Defaults to 0. |
| `include` | Array of strings | No | Request that the response include the total count by specifying `include=["total_count"]`. |
| `date_created` | object (date_filter) | No | Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. |
| `scanned` | boolean | No | Filter list of responses to only include QR codes with at least one scan event. |
| `resource_ids` | Array of arrays <= 100 items | No | Default: `[]`. Filter by the resource ID. |

## Responses

### 200 - Returns a list of QR Codes and their analytics.

**Response Schema:** `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `object` | string (object) | No | Value is resource type. |
| `count` | integer (count) | No | Number of resources in a set. |
| `total_count` | integer | No | Indicates the total number of records. Provided when the request specifies an "include" query parameter. |
| `scanned_count` | integer | No | Indicates the number of QR Codes out of `count` that were scanned at least once. |
| `data` | Array of objects (qr_code_scans) | No | List of QR code analytics. |

## Request Samples

### Shell

```bash
curl -X GET "https://api.lob.com/v1/qr_code_analytics?limit=2&scanned=true" \
  -u <YOUR API KEY>:
```

## Response Samples

### 200

```json
{
  "data": [
    {
      "resource_id": "ltr_d5a5a89da9106f8",
      "date_created": "2019-07-27T23:49:01.511Z",
      "number_of_scans": 2,
      "scans": []
    },
    {
      "resource_id": "psc_d5a5a89da9106f8",
      "date_created": "2022-09-27T23:49:01.511Z",
      "number_of_scans": 1,
      "scans": []
    }
  ],
  "object": "list",
  "count": 2,
  "scanned_count": 2,
  "total_count": 2
}
```