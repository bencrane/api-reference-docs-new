# Retrieve Export

Retrieves the details of an existing export. You need only supply the unique export identifier that was returned upon export creation. If you try retrieving an export immediately after creating one (i.e., before we're done processing the export), you will get back an export object with `state = in_progress`.

**Method:** `GET /uploads/{upl_id}/exports/{ex_id}`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upl_id` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | ID of the upload |
| `ex_id` | string (ex_id) `^ex_[a-zA-Z0-9]+$` | **Yes** | ID of the export |

## Responses

### 200 - Returns an export object

**Response Schema:** `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string (ex_id) `^ex_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `ex_`. |
| `dateCreated` | string \<date-time\> | **Yes** | A timestamp in ISO 8601 format of the date the export was created. |
| `dateModified` | string \<date-time\> | **Yes** | A timestamp in ISO 8601 format of the date the export was last modified. |
| `deleted` | boolean | **Yes** | Returns as `true` if the resource has been successfully deleted. |
| `s3Url` | string | **Yes** | The URL for the generated export file. |
| `state` | string | **Yes** | Enum: `"in_progress"` `"failed"` `"succeeded"`. The state of the export file, which can be `in_progress`, `failed` or `succeeded`. |
| `type` | string | **Yes** | Enum: `"all"` `"failures"` `"successes"`. The export file type, which can be `all`, `failures` or `successes`. |
| `uploadId` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `upl_`. |

## Request Samples

### cURL

```bash
curl https://api.lob.com/v1/uploads/upl_71be866e430b11e9/exports/ex_6a94fe68fd151e0f8 \
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