# List Chats API Reference

## Endpoint

**GET** `https://api.vapi.ai/chat`

## Description

Retrieves a paginated list of chats with optional filtering and sorting capabilities.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Unique identifier to filter by specific chat |
| `assistantId` | string | No | Filter by assistant identifier |
| `assistantIdAny` | string | No | "Filter by multiple assistant IDs. Provide as comma-separated values" |
| `squadId` | string | No | Squad identifier for filtering |
| `sessionId` | string | No | Session identifier for filtering |
| `previousChatId` | string | No | Filter by prior chat identifier |
| `page` | number | No | "Page number to return. Defaults to 1" |
| `sortOrder` | string (ASC/DESC) | No | "Sort order for pagination. Defaults to 'DESC'" |
| `limit` | number | No | "Maximum number of items to return. Defaults to 100" |
| `createdAtGt` | string (date-time) | No | Items where createdAt exceeds specified value |
| `createdAtLt` | string (date-time) | No | Items where createdAt is less than specified value |
| `createdAtGe` | string (date-time) | No | Items where createdAt is greater than or equal to value |
| `createdAtLe` | string (date-time) | No | Items where createdAt is less than or equal to value |
| `updatedAtGt` | string (date-time) | No | Items where updatedAt exceeds specified value |
| `updatedAtLt` | string (date-time) | No | Items where updatedAt is less than specified value |
| `updatedAtGe` | string (date-time) | No | Items where updatedAt is greater than or equal to value |
| `updatedAtLe` | string (date-time) | No | Items where updatedAt is less than or equal to value |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

**Status Code:** 200 OK

**Response Schema:** `ChatPaginatedResponse`

The response returns a paginated collection of chat objects with metadata for navigation.

## Reference

Full documentation available at: https://docs.vapi.ai/api-reference/chats/list
