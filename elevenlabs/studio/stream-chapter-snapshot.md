# Stream Chapter Audio

**Endpoint:** POST `https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}/stream`

## Overview

This API endpoint retrieves audio from a chapter snapshot. To find available snapshots, use the GET endpoint for listing chapter snapshots.

## Path Parameters

- **project_id** (required): The project identifier. Use the List projects endpoint to discover available projects.
- **chapter_id** (required): The chapter identifier. Use the List project chapters endpoint to find chapters.
- **chapter_snapshot_id** (required): The snapshot identifier. Use the List project chapter snapshots endpoint to locate snapshots.

## Headers

- **xi-api-key** (optional): API authentication header

## Request Body

The request accepts a JSON object with one optional parameter:

- **convert_to_mpeg** (boolean, default: false): Converts the returned audio to MPEG format

## Response

**Success (200):** Returns streaming audio data in `application/octet-stream` format (binary)

**Error (422):** Returns validation error details

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each demonstrates posting to the endpoint with an empty request body.
