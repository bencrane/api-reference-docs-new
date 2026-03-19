# Create Export

Campaign Exports can help you understand exactly which records in a campaign could not be created. By initiating and retrieving an export, you will get row-by-row errors for your campaign. For a step-by-step walkthrough of creating a campaign and exporting failures, see our Campaigns Guide.

Create an export file associated with an upload.

**Method:** `POST /uploads/{upl_id}/exports`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upl_id` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | ID of the upload |

## Request Body Schema

Content type: `application/json`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `type` | string | No | Enum: `"all"` `"failures"` `"successes"` |

## Responses

### 200 - Successful Response

**Response Schema:** `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string (Message) | **Yes** | Default: `"Export is processing"`. Value: `"Export is processing"` |
| `exportId` | string (Export ID) | **Yes** | Unique identifier for the export. |

### 4XX - Create Export Error

## Request Samples

### Payload

```json
{
  "type": "all"
}
```

## Response Samples

### 200

```json
{
  "message": "Export is processing",
  "exportId": "ex_2dafd758ed3da9c43"
}
```