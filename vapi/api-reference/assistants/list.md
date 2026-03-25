# List Assistants API Reference

## Endpoint

**GET** `https://api.vapi.ai/assistant`

Retrieve a list of all assistants configured in your Vapi account.

## Description

This endpoint allows you to fetch assistants with optional filtering by creation and modification timestamps. Results can be paginated using the limit parameter.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | number | No | "This is the maximum number of items to return. Defaults to 100." |
| `createdAtGt` | string (date-time) | No | "This will return items where the createdAt is greater than the specified value." |
| `createdAtLt` | string (date-time) | No | "This will return items where the createdAt is less than the specified value." |
| `createdAtGe` | string (date-time) | No | "This will return items where the createdAt is greater than or equal to the specified value." |
| `createdAtLe` | string (date-time) | No | "This will return items where the createdAt is less than or equal to the specified value." |
| `updatedAtGt` | string (date-time) | No | "This will return items where the updatedAt is greater than the specified value." |
| `updatedAtLt` | string (date-time) | No | "This will return items where the updatedAt is less than the specified value." |
| `updatedAtGe` | string (date-time) | No | "This will return items where the updatedAt is greater than or equal to the specified value." |
| `updatedAtLe` | string (date-time) | No | "This will return items where the updatedAt is less than or equal to the specified value." |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard (dashboard.vapi.ai)." |

## Response

**Status Code:** 200 OK

**Content Type:** application/json

**Response Body:** An array of Assistant objects containing full assistant configuration details, including transcriber settings, voice provider configurations, and other assistant parameters.

## Reference

Full API documentation: https://docs.vapi.ai/api-reference/assistants/list
