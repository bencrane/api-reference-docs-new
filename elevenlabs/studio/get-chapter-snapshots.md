# List Chapter Snapshots

## Endpoint Overview

The List Chapter Snapshots endpoint retrieves metadata for all snapshots associated with a specific chapter within a project.

**Request Method:** GET
**URL:** `https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots`

## Purpose

This API call "gets information about all the snapshots of a chapter." Snapshots are automatically generated whenever a chapter undergoes conversion, and each one can be downloaded as audio.

## Required Parameters

- **project_id** (path): The project identifier. You can obtain available projects via the List Projects endpoint.
- **chapter_id** (path): The chapter identifier. Available chapters can be retrieved using the List Project Chapters endpoint.

## Optional Parameters

- **xi-api-key** (header): API key for authentication

## Response Schema

The endpoint returns a `ChapterSnapshotsResponse` object containing:

- **snapshots**: Array of chapter snapshot objects, each including:
  - `chapter_snapshot_id`: Unique snapshot identifier
  - `project_id`: Associated project ID
  - `chapter_id`: Associated chapter ID
  - `created_at_unix`: Creation timestamp (Unix format)
  - `name`: Snapshot name

## HTTP Status Codes

- **200**: Successful response with snapshot data
- **422**: Validation error

## Server Locations

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

**TypeScript:**
```typescript
const client = new ElevenLabsClient();
await client.studio.projects.chapters.snapshots.list("21m00Tcm4TlvDq8ikWAM", "21m00Tcm4TlvDq8ikWAM");
```

**Python:**
```python
client = ElevenLabs()
client.studio.projects.chapters.snapshots.list(
    project_id="21m00Tcm4TlvDq8ikWAM",
    chapter_id="21m00Tcm4TlvDq8ikWAM",
)
```

**Go, Ruby, Java, PHP, C#, and Swift** examples are also provided in the original documentation.
