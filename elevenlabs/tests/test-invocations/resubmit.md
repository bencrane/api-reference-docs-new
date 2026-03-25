# Resubmit Test Invocation API Documentation

## Endpoint Overview

**POST** `https://api.elevenlabs.io/v1/convai/test-invocations/{test_invocation_id}/resubmit`

This endpoint allows you to "resubmit specific test runs from a test invocation."

## Path Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `test_invocation_id` | string | Yes | The identifier for a test invocation returned when tests execute |

## Request Headers

| Header | Type | Required |
|--------|------|----------|
| `xi-api-key` | string | No |
| `Content-Type` | string | Yes (application/json) |

## Request Body

The request requires a JSON payload with these properties:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `test_run_ids` | array[string] | Yes | List of test run IDs to resubmit |
| `agent_id` | string | Yes | Agent ID to resubmit tests for |
| `branch_id` | string | No | Branch ID for test execution; uses agent default if omitted |
| `agent_config_override` | object | No | Configuration overrides for testing; uses agent defaults if not provided |

## Response

**Status 200: Successful Response**
- Returns a JSON object (any type)

**Status 422: Validation Error**
- Returns HTTPValidationError schema with validation details

## Available API Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
