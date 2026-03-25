# Update Workspace Webhook

## Endpoint Details

The Update Workspace Webhook is a PATCH endpoint located at:
```
PATCH https://api.elevenlabs.io/v1/workspace/webhooks/{webhook_id}
```

## Purpose

This API allows you to "Update the specified workspace webhook" by modifying its configuration settings.

## Request Parameters

**Path Parameter:**
- `webhook_id` (string, required): The unique identifier for the webhook

**Header:**
- `xi-api-key` (string, optional): Authentication key

**Request Body:**
The endpoint accepts a JSON object with the following properties:
- `is_disabled` (boolean, required): Whether to disable or enable the webhook
- `name` (string, required): The display name of the webhook for identification purposes
- `retry_enabled` (boolean, optional): Whether to enable automatic retries for transient failures

## Response

**Success (200):**
Returns an object with a `status` field indicating "ok" upon successful completion.

**Validation Error (422):**
Returns validation error details if the request is malformed.

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples

Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to update a webhook with `isDisabled: false` and a custom name.
