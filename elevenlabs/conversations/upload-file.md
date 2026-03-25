# Upload Conversation File

## Endpoint Overview

The ElevenLabs API provides a file upload endpoint for conversations at `POST https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}/files`.

### Purpose

This endpoint allows you to "upload an image or PDF file for a conversation. Returns a unique file ID" that can subsequently be referenced within the conversation context.

## Request Details

**Method:** POST
**Content-Type:** multipart/form-data

### Parameters

- **conversation_id** (path, required): String identifier for the conversation
- **xi-api-key** (header, optional): API authentication key
- **file** (form data, required): Binary image or PDF file to upload

## Response

**Success (200):** Returns a JSON object containing:
```json
{
  "file_id": "string"
}
```

**Validation Error (422):** Returns HTTP validation error details

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

**TypeScript/JavaScript:**
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
const client = new ElevenLabsClient();
await client.conversationalAi.conversations.files.create("conversation_id", {});
```

**Python:**
```python
from elevenlabs import ElevenLabs
client = ElevenLabs()
client.conversational_ai.conversations.files.create(
    conversation_id="conversation_id",
    file="example_file",
)
```

The documentation also includes implementation examples in Go, Ruby, Java, PHP, C#, and Swift, demonstrating multipart form-data construction for the file upload request.
