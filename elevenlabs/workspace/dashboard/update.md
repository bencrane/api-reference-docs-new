# Update Convai Dashboard Settings

## Endpoint Overview

This API endpoint allows you to modify Convai dashboard settings at the workspace level using a PATCH request to `https://api.elevenlabs.io/v1/convai/settings/dashboard`.

## Request Details

**Method:** PATCH
**Content-Type:** application/json
**Required Header:** xi-api-key (optional in header)

## Request Body

The request accepts a JSON object with a `charts` array property. Each chart item supports three types:

1. **call_success** - Requires `type` and `name`
2. **criteria** - Requires `type`, `name`, and `criteria_id`
3. **data_collection** - Requires `type`, `name`, and `data_collection_id`

## Response

**Success (200):** Returns a GetConvAiDashboardSettingsResponseModel containing the updated charts array configuration.

**Validation Error (422):** Returns HTTPValidationError with detailed validation failure information.

## Available SDK Examples

Code samples are provided for:
- TypeScript/JavaScript
- Python
- Go
- Ruby
- Java
- PHP
- C#
- Swift

Each example demonstrates updating dashboard settings with an empty configuration object `{}`.

## Server Endpoints

The API is available across multiple regional endpoints including standard US, EU residency, and India residency servers.
