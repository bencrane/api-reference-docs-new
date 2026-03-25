# List Workspace Groups

## Endpoint Overview

The `GET https://api.elevenlabs.io/v1/workspace/groups` endpoint retrieves all groups configured in your ElevenLabs workspace.

## Key Details

**Description:** "Get all groups in the workspace"

**Authentication:** Optional `xi-api-key` header parameter

**Response:** Returns a 200 status with an object containing workspace group data, or 422 for validation errors.

## Response Schema

Each group object includes:
- `name` (string, required)
- `id` (string, required)
- `members` (array of strings, required)
- `permissions` (array of permission enums)
- `group_usage_limit` (integer or "unlimited")
- `character_count` (integer)
- `scim_external_id` (string)

## Available Permissions

The API supports 27 distinct permission types including text-to-speech, voice cloning, workspace analytics, user management, and AI features.

## Implementation Examples

Code samples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating straightforward GET requests to the endpoint with optional API key authentication.
