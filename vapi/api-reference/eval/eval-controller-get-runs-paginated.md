# List Eval Runs - API Reference

## Endpoint

**GET** `https://api.vapi.ai/eval/run`

Retrieves a paginated list of evaluation runs from your organization.

## Description

This endpoint returns evaluation runs with support for filtering, sorting, and pagination. You can filter by creation and update timestamps, control the sort order, and limit the number of results returned.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Filter by evaluation run ID |
| `page` | number | No | "This is the page number to return. Defaults to 1." |
| `sortOrder` | string | No | "This is the sort order for pagination. Defaults to 'DESC'." Valid values: `ASC`, `DESC` |
| `limit` | number | No | "This is the maximum number of items to return. Defaults to 100." |
| `createdAtGt` | string (date-time) | No | Returns items where createdAt is greater than specified value |
| `createdAtLt` | string (date-time) | No | Returns items where createdAt is less than specified value |
| `createdAtGe` | string (date-time) | No | Returns items where createdAt is greater than or equal to specified value |
| `createdAtLe` | string (date-time) | No | Returns items where createdAt is less than or equal to specified value |
| `updatedAtGt` | string (date-time) | No | Returns items where updatedAt is greater than specified value |
| `updatedAtLt` | string (date-time) | No | Returns items where updatedAt is less than specified value |
| `updatedAtGe` | string (date-time) | No | Returns items where updatedAt is greater than or equal to specified value |
| `updatedAtLe` | string (date-time) | No | Returns items where updatedAt is less than or equal to specified value |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | **Yes** | API key from your Dashboard |

## Response

**Status Code:** 200

**Schema:** `EvalRunPaginatedResponse`

Returns a paginated collection of evaluation runs with metadata for the mock conversation evaluation type.
