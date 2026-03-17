# Get Current Date and Time

## Overview
This utility endpoint retrieves the server's current date and time, particularly useful for troubleshooting timezone-related issues.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/utilities/current-date` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `region` | string | Timezone identifier (e.g., "America/New_York") |

**Example:**
```json
{
  "region": "America/New_York"
}
```

## Response

### Success (200 OK)

| Field | Type | Description |
|-------|------|-------------|
| `datetime` | string | Current date/time in specified timezone |
| `timestamp` | integer | Unix timestamp |
| `timezone` | string | Timezone identifier |
| `timezone_name` | string | Human-readable timezone description |

**Example:**
```json
{
  "datetime": "2026-01-08 12:00:00 -05:00",
  "timestamp": 1736385600,
  "timezone": "America/New_York",
  "timezone_name": "(GMT-05:00) New York"
}
```

## Error Responses

| Status | Description |
|--------|-------------|
| **422 Unprocessable Entity** | Missing required fields (INVALID_INPUT code) |
| **500 Internal Server Error** | Server-side issue with timestamp |

## Authentication
Provide your API key via the `x-api-key` header. Obtain keys at https://app.blitz-api.ai
