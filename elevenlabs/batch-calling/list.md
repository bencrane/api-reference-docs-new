# List Workspace Batch Calling Jobs

## Overview
This endpoint retrieves all batch calling jobs for your current workspace using a GET request to `https://api.elevenlabs.io/v1/convai/batch-calling/workspace`.

## Query Parameters
- **limit** (integer, optional): Maximum number of results to return. Default is 100.
- **last_doc** (string, optional): Pagination cursor for retrieving subsequent result sets.
- **xi-api-key** (header, optional): API authentication key.

## Response Structure
The successful response returns a `WorkspaceBatchCallsResponse` containing:

- **batch_calls**: Array of batch call objects, each including:
  - Identifiers (id, phone_number_id, agent_id, agent_name)
  - Configuration (phone_provider, whatsapp_params, telephony_call_config)
  - Metadata (name, timezone, created_at_unix, scheduled_time_unix)
  - Call metrics (total_calls_dispatched, total_calls_scheduled, total_calls_finished)
  - Status information (status, retry_count, last_updated_at_unix)
  - Concurrency settings (target_concurrency_limit)

- **next_doc**: Pagination token for additional results
- **has_more**: Boolean indicating whether more records exist

## Status Values
Batch calls can have these statuses: pending, in_progress, completed, failed, or cancelled.

## Code Examples
The documentation provides SDK implementations across multiple languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the same basic call with optional limit and pagination parameters.
