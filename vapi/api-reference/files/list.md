# List Files API Reference

## Endpoint

**Method:** GET
**URL:** `https://api.vapi.ai/file`

## Description

Retrieves a list of all files in your Vapi account.

## Authentication

**Header Parameter:** `Authorization` (required)
Include your API Key from the Dashboard in the Authorization header using bearer token scheme.

## Parameters

| Name | Location | Type | Required | Description |
|------|----------|------|----------|-------------|
| Authorization | header | string | Yes | "Retrieve your API Key from Dashboard" |

## Response Schema

Returns an array of File objects with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| id | string | Unique identifier for the file |
| object | string | Enum: `file` |
| status | string | Enum: `processing`, `done`, `failed` |
| name | string | Name of the file for your own reference |
| originalName | string | Original filename |
| bytes | number | File size in bytes |
| purpose | string | Intended use of the file |
| mimetype | string | MIME type of the file |
| url | string | File access URL |
| parsedTextUrl | string | URL to parsed text version |
| parsedTextBytes | number | Size of parsed text in bytes |
| orgId | string | Unique identifier for the org that this file belongs to |
| createdAt | string | ISO 8601 date-time string of when the file was created |
| updatedAt | string | ISO 8601 date-time string of when the file was last updated |

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
client.files.list()
```
