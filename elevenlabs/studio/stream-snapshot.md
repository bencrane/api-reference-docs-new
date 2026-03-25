# Stream Studio Project Audio

**Endpoint:** POST `https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/stream`

## Overview

This API endpoint enables streaming audio output from an ElevenLabs Studio project snapshot. The request accepts an optional parameter to convert audio to MPEG format.

## Request Details

**Path Parameters:**
- `project_id` (required): The Studio project identifier
- `project_snapshot_id` (required): The snapshot identifier within the project

**Headers:**
- `Content-Type: application/json`
- `xi-api-key` (optional): Authentication header

**Request Body:**
- `convert_to_mpeg` (boolean, optional, default: false): Whether to convert audio to MPEG format

## Response

**Success (200):** Returns audio data as binary stream in `application/octet-stream` format

**Error (422):** Returns validation error details in JSON format

## Implementation Examples

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. The TypeScript SDK approach is straightforward:

```typescript
const client = new ElevenLabsClient();
await client.studio.projects.snapshots.stream("project_id", "project_snapshot_id", {});
```

All examples follow a consistent pattern: POST request with optional conversion parameters, targeting the ElevenLabs API servers across multiple regional endpoints (US, EU, India).
