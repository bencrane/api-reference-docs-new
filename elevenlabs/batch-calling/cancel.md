# Cancel Batch Calling Job

## Overview
This endpoint allows you to cancel a running batch call operation. When invoked, it sets all recipients in the batch to a cancelled status.

## Endpoint Details
- **Method:** POST
- **URL:** `https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/cancel`

## Parameters

### Path Parameter
- **batch_id** (required, string): The identifier for the batch calling job to cancel

### Header Parameter
- **xi-api-key** (optional, string): API authentication key

## Response

### Success Response (200)
Returns a `BatchCallResponse` object containing:
- id, name, agent_id, agent_name
- created_at_unix, scheduled_time_unix, last_updated_at_unix
- status (will be "cancelled")
- total_calls_dispatched, total_calls_scheduled, total_calls_finished
- phone_number_id, phone_provider
- retry_count, ringing_timeout_secs
- timezone, target_concurrency_limit
- whatsapp_params (if applicable)

### Error Response (422)
Validation errors returned in HTTPValidationError format with error details and location information.

## Server Endpoints
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples
Code implementations provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the basic POST request to cancel a batch with the specified batch_id.
