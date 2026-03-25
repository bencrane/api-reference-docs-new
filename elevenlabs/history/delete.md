# Delete History Item

**Endpoint:** `DELETE https://api.elevenlabs.io/v1/history/{history_item_id}`

This API endpoint removes a specific history item using its unique identifier.

## Key Details

**Purpose:** "Delete a history item by its ID"

**Required Parameter:**
- `history_item_id` (path): The identifier of the history item to remove. You can retrieve available items via the Get generated items endpoint.

**Optional Parameter:**
- `xi-api-key` (header): API authentication key

## Response Structure

A successful deletion returns:
```json
{
  "status": "ok"
}
```

The status field confirms whether the deletion succeeded. On failure, an HTTP 500 error is returned with details.

## Available Server Endpoints

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## Implementation Examples

The documentation provides code samples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each demonstrates the fundamental pattern: sending a DELETE request to the endpoint with the target history item ID.
