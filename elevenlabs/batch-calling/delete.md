# Delete Batch Calling Job

## Overview
The ElevenLabs API provides an endpoint to permanently remove a batch calling job via a DELETE request to `https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}`.

## Key Details
- **Endpoint**: DELETE `/v1/convai/batch-calling/{batch_id}`
- **Purpose**: "Permanently delete a batch call and all recipient records. Conversations remain in history."
- **Required Parameter**: `batch_id` (path parameter, string type)
- **Optional Header**: `xi-api-key`

## Response Codes
- **200**: Successful deletion
- **422**: Validation error with detailed error information

## Implementation Examples

The documentation provides code samples across multiple languages:

**TypeScript/JavaScript**: Uses the ElevenLabs SDK with `client.conversationalAi.batchCalls.delete("batch_id")`

**Python**: Implements deletion through `client.conversational_ai.batch_calls.delete(batch_id="batch_id")`

**Raw HTTP**: Direct DELETE requests can be made using Go, Ruby, Java, PHP, C#, and Swift with standard HTTP libraries

## Important Note
While the batch calling job and recipient records are deleted, conversation histories remain accessible in the system's history records.
