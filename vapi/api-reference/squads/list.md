# List Squads API Reference

## Endpoint

**GET** `https://api.vapi.ai/squad`

## Description

Retrieves a list of squads with optional filtering and pagination capabilities.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | number | No | "maximum number of items to return. Defaults to 100" |
| `createdAtGt` | string (date-time) | No | "return items where the createdAt is greater than the specified value" |
| `createdAtLt` | string (date-time) | No | "return items where the createdAt is less than the specified value" |
| `createdAtGe` | string (date-time) | No | "return items where the createdAt is greater than or equal to the specified value" |
| `createdAtLe` | string (date-time) | No | "return items where the createdAt is less than or equal to the specified value" |
| `updatedAtGt` | string (date-time) | No | "return items where the updatedAt is greater than the specified value" |
| `updatedAtLt` | string (date-time) | No | "return items where the updatedAt is less than the specified value" |
| `updatedAtGe` | string (date-time) | No | "return items where the updatedAt is greater than or equal to the specified value" |
| `updatedAtLe` | string (date-time) | No | "return items where the updatedAt is less than or equal to the specified value" |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

**Status Code:** 200

**Content-Type:** application/json

**Schema:** Array of Squad objects

The response returns an array where each item conforms to the Squad schema definition.

---

**Note:** Complete Squad schema definitions and additional implementation details are available in the full OpenAPI specification referenced in the source document.
