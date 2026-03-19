# Upload File

Upload an audience file and associate it with an upload.

**Method:** `POST /uploads/{upl_id}/file`

## Authorization

`basicAuth`

## Path Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upl_id` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | ID of the upload |

## Request Body Schema

Content type: `multipart/form-data`

| Parameter | Type | Description |
|---|---|---|
| `file` | string \<binary\> | The audience file to upload |

## Responses

### 202 - Successful Response

### 422 - Validation Error

## Request Samples

### cURL

```bash
curl -X POST https://api.lob.com/v1/uploads/upl_71be866e430b11e9/file \
  -u <YOUR API KEY>: \
  -F file=@<YOUR FILE NAME HERE>
```

## Response Samples

### 202

```json
{
  "message": "File uploaded successfully",
  "filename": "string"
}
```