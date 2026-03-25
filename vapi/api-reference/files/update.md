# Update File API Reference

## Endpoint

**Method:** `PATCH`
**URL:** `https://api.vapi.ai/file/{id}`
**Content-Type:** `application/json`

## Description

This endpoint allows you to update an existing file's metadata, specifically its name for reference purposes.

## Parameters

### Path Parameters
- **id** (required, string): The unique identifier for the file to update

### Header Parameters
- **Authorization** (required, string): Your API Key from the Dashboard at dashboard.vapi.ai

## Request Body

The request accepts a JSON object with the following schema:

```json
{
  "name": "string"
}
```

**UpdateFileDTO Properties:**
- **name** (string): A reference name for the file, used for your own organizational purposes

## Response

**Status Code:** `200 OK`

Returns a File object with the following structure:

```json
{
  "object": "file",
  "status": "processing|done|failed",
  "name": "string",
  "originalName": "string",
  "bytes": 0,
  "purpose": "string",
  "mimetype": "string",
  "key": "string",
  "path": "string",
  "bucket": "string",
  "url": "string",
  "parsedTextUrl": "string",
  "parsedTextBytes": 0,
  "metadata": {},
  "id": "string",
  "orgId": "string",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
client.files.update(id="id")
```
