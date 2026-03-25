# List Campaigns API Reference

## Endpoint

**GET** `https://api.vapi.ai/campaign`

## Description

Retrieves a paginated list of campaigns with optional filtering and sorting capabilities.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Filter by campaign ID |
| `status` | string | No | Filter by status: `scheduled`, `in-progress`, or `ended` |
| `page` | number | No | Page number for pagination (defaults to 1) |
| `sortOrder` | string | No | Sort order: `ASC` or `DESC` (defaults to `DESC`) |
| `limit` | number | No | Max items per page (defaults to 100) |
| `createdAtGt` | string (date-time) | No | Items created after this timestamp |
| `createdAtLt` | string (date-time) | No | Items created before this timestamp |
| `createdAtGe` | string (date-time) | No | Items created on or after this timestamp |
| `createdAtLe` | string (date-time) | No | Items created on or before this timestamp |
| `updatedAtGt` | string (date-time) | No | Items updated after this timestamp |
| `updatedAtLt` | string (date-time) | No | Items updated before this timestamp |
| `updatedAtGe` | string (date-time) | No | Items updated on or after this timestamp |
| `updatedAtLe` | string (date-time) | No | Items updated on or before this timestamp |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | API key from Dashboard |

## Response

**Status Code:** 200

**Content-Type:** application/json

**Schema:** `CampaignPaginatedResponse`

The response returns paginated campaign data with filtering applied based on query parameters.

## Reference

Full documentation: https://docs.vapi.ai/api-reference/campaigns/campaign-controller-find-all
