# Retrieve Line Item Report

Retrieves the line item data for each row from the csv file associated with the upload id record. NOTE: This endpoint is currently feature flagged. Please reach out to Lob's support team if you would like access to this API endpoint.

**Method:** `GET /uploads/{upl_id}/report`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upl_id` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | ID of the upload |

## Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `status` | string | No | Enum: `"Validated"` `"Failed"` `"Processing"`. The status of line items to filter and retrieve. By default all line items are returned. |
| `limit` | integer [1..100] | No | Default: `100`. Example: `limit=10`. How many results to return. |
| `offset` | integer | No | Default: `0`. An integer that designates the offset at which to begin returning results. Defaults to 0. |

## Responses

### 200 - Returns a report object

**Response Schema:** `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | Array of objects | **Yes** | Line item data. |
| `count` | integer (count) | **Yes** | Number of resources in a set. |
| `total_count` | integer | **Yes** | Indicates the total number of records. Provided when the request specifies an "include" query parameter. |
| `next_url` | string or null | No | Url of next page of items in list. |
| `prev_url` | string or null | No | Url of previous page of items in list. |

### 404 - Not Found Error

## Request Samples

### cURL

```bash
curl https://api.lob.com/v1/uploads/upl_71be866e430b11e9/report \
  -u <YOUR API KEY>:
```

## Response Samples

### 200

```json
{
  "id": "ex_6a94fe68fd151e0f8",
  "dateCreated": "2021-07-06T22:51:42.838Z",
  "dateModified": "2022-07-06T22:51:42.838Z",
  "deleted": false,
  "s3Url": null,
  "state": "in_progress",
  "type": "failures",
  "uploadId": "upl_71be866e430b11e9"
}
```