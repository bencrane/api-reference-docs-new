# Delete File API Reference

## Endpoint
**Method:** DELETE
**URL:** `https://api.vapi.ai/file/{id}`

## Description
Removes a file from the Vapi system. The operation returns the deleted file's details upon successful completion.

## Parameters

### Path Parameters
- **id** (required, string): The unique identifier of the file to remove

### Header Parameters
- **Authorization** (required, string): Your API key from the Vapi Dashboard

## Response

**Status:** 200 OK

**Response Schema:** File object with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| id | string | Unique file identifier |
| object | string | Always "file" |
| status | string | Current state: processing, done, or failed |
| name | string | User-defined file name for reference |
| originalName | string | Original uploaded filename |
| bytes | number | File size in bytes |
| purpose | string | Intended use of the file |
| mimetype | string | File's MIME type |
| url | string | File's storage location |
| parsedTextUrl | string | URL of extracted text |
| createdAt | string | ISO 8601 creation timestamp |
| updatedAt | string | ISO 8601 last modified timestamp |
| orgId | string | Organization identifier |

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
client.files.delete(id="id")
```
