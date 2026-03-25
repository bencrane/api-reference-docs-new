# Get File API Reference

## Endpoint

**Method:** GET
**URL:** `https://api.vapi.ai/file/{id}`

## Description

Retrieves a specific file by its unique identifier from the Vapi API.

## Parameters

### Path Parameters
- **id** (required, string): The unique identifier for the file to retrieve

### Header Parameters
- **Authorization** (required, string): Your API key from the Dashboard

## Response Schema

The endpoint returns a File object with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| id | string | Unique file identifier |
| orgId | string | Organization identifier |
| object | string | Always "file" |
| status | string | One of: processing, done, failed |
| name | string | User-defined file name for reference |
| originalName | string | Original filename |
| bytes | number | File size in bytes |
| purpose | string | File purpose designation |
| mimetype | string | File MIME type |
| key | string | Storage key |
| path | string | Storage path |
| bucket | string | Storage bucket |
| url | string | File URL |
| parsedTextUrl | string | URL of parsed text content |
| parsedTextBytes | number | Size of parsed text in bytes |
| metadata | object | Custom metadata object |
| createdAt | string | ISO 8601 creation timestamp |
| updatedAt | string | ISO 8601 last update timestamp |

## Python SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
response = client.files.get(id="id")
```
