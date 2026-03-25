# Delete Studio Project

**Endpoint:** `DELETE https://api.elevenlabs.io/v1/studio/projects/{project_id}`

This API operation removes a Studio project from your account.

## Key Parameters

- **project_id** (required, path): The identifier for the project you wish to delete. You can retrieve available project IDs via the List projects endpoint.
- **xi-api-key** (optional, header): Authentication key for the request.

## Response Format

A successful deletion returns a 200 status with this structure:
```json
{
  "status": "ok"
}
```

The status field confirms successful deletion. Any errors return a 500 status with error details.

## Available Endpoints

The API supports four regional servers:
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## Implementation Examples

The documentation provides code samples in TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the deletion of a project with ID `21m00Tcm4TlvDq8ikWAM`.

## Error Handling

Validation errors (422 status) return detailed error information including location, message, and error type for debugging purposes.
