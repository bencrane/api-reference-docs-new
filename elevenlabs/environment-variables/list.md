# List Environment Variables

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/environment-variables`

## Overview

This API endpoint retrieves all environment variables for a workspace with optional filtering capabilities.

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cursor` | string | No | Pagination cursor from previous response |
| `page_size` | integer | No | Number of items to return (1-100); default is 100 |
| `label` | string | No | Filter by exact label match |
| `environment` | string | No | Filter variables by environment; response values limited to specified environment |
| `type` | string | No | Filter by variable type (string, secret, auth_connection) |
| `xi-api-key` | string (header) | No | API authentication key |

## Response Codes

- **200:** Successful response with environment variables list
- **400:** Invalid environment filter provided
- **422:** Validation error in request parameters

## Response Schema

The successful response contains:

- `environment_variables`: Array of environment variable objects
- `next_cursor`: Pagination cursor for next page (optional)
- `has_more`: Boolean indicating additional results exist

## Variable Types

The API supports three variable types:
- `string`: Standard text variables
- `secret`: Sensitive credential variables
- `auth_connection`: Authentication connection references

## SDK Examples

Implementation examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to construct requests with filtering and pagination parameters.
