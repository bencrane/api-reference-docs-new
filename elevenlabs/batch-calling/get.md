# Get batch call information

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}`

This endpoint retrieves detailed information about a batch call, including all recipients and their statuses.

## Parameters

- **batch_id** (path, required): String identifier for the batch call
- **xi-api-key** (header, optional): API authentication key

## Response

Returns a `BatchCallDetailedResponse` object containing:

- **id**: Batch call identifier
- **name**: Batch call name
- **agent_id**: Associated agent identifier
- **status**: Current batch status (pending, in_progress, completed, failed, cancelled)
- **phone_provider**: Telephony provider (twilio or sip_trunk)
- **created_at_unix**: Creation timestamp
- **scheduled_time_unix**: Scheduled execution time
- **timezone**: Batch timezone
- **total_calls_dispatched**: Number of calls sent out
- **total_calls_scheduled**: Number of calls queued
- **total_calls_finished**: Number of completed calls
- **last_updated_at_unix**: Last update timestamp
- **telephony_call_config**: Configuration including ringing timeout
- **target_concurrency_limit**: Maximum simultaneous calls
- **recipients**: Array of call recipient objects with individual statuses

## HTTP Status Codes

- **200**: Successful retrieval
- **422**: Validation error

## SDK Examples

Available implementations in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift are provided for easy integration across platforms.
