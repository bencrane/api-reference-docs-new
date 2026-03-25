# Stream Archive With Studio Project Audio

**Endpoint:** POST `https://api.elevenlabs.io/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive`

**Purpose:** "Returns a compressed archive of the Studio project's audio."

## Required Parameters

- **project_id** (path): The Studio project identifier, obtainable via the List projects endpoint
- **project_snapshot_id** (path): The specific snapshot identifier for the project
- **xi-api-key** (header, optional): API authentication credential

## Response

**Success (200):** Returns binary archive data in `application/octet-stream` format

**Error (422):** Returns validation error details in JSON format

## Available API Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Implementation Examples

Code examples are provided across multiple languages: TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each demonstrates the same core functionality—initiating an archive download request with appropriate authentication and project identifiers.

The TypeScript SDK usage: `client.studio.projects.snapshots.streamArchive(project_id, snapshot_id)`

The Python SDK usage: `client.studio.projects.snapshots.stream_archive(project_id, project_snapshot_id)`
