# Upload File API Reference

## Endpoint
**Method:** POST
**URL:** `https://api.vapi.ai/file`
**Content-Type:** `multipart/form-data`

## Description
This endpoint allows you to upload a file for use with the Knowledge Base feature.

## Parameters

### Headers
- **Authorization** (required): Your API Key from the Dashboard
  - Type: `string`

### Request Body
The request uses `multipart/form-data` encoding:
- **file** (required): The file to upload
  - Type: `binary`
  - Description: The File you want to upload for use with the Knowledge Base.

## Response Schema

### Success Response (201)
Returns a File object with these properties:

| Property | Type | Description |
|----------|------|-------------|
| object | string | Enum: "file" |
| status | string | Enum: "processing", "done", "failed" |
| name | string | File name for reference |
| originalName | string | Original filename |
| bytes | number | File size in bytes |
| purpose | string | File purpose |
| mimetype | string | MIME type |
| id | string | Unique file identifier |
| orgId | string | Organization identifier |
| createdAt | date-time | ISO 8601 creation timestamp |
| updatedAt | date-time | ISO 8601 last update timestamp |
| url | string | File URL |
| parsedTextUrl | string | Parsed text URL |
| key | string | Storage key |
| path | string | File path |
| bucket | string | Storage bucket |

### Error Response (400)
Returns an error for invalid files.

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
client.files.create(file="example_file")
```
