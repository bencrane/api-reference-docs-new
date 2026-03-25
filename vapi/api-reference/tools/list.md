# List Tools API Reference

## Endpoint

**GET** `https://api.vapi.ai/tool`

## Description

Retrieves a list of tools configured in your Vapi account with optional filtering by creation and modification timestamps.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | number | No | Maximum items to return; defaults to 100 |
| `createdAtGt` | string (date-time) | No | Items where createdAt exceeds specified value |
| `createdAtLt` | string (date-time) | No | Items where createdAt is below specified value |
| `createdAtGe` | string (date-time) | No | Items where createdAt is greater than or equal |
| `createdAtLe` | string (date-time) | No | Items where createdAt is less than or equal |
| `updatedAtGt` | string (date-time) | No | Items where updatedAt exceeds specified value |
| `updatedAtLt` | string (date-time) | No | Items where updatedAt is below specified value |
| `updatedAtGe` | string (date-time) | No | Items where updatedAt is greater than or equal |
| `updatedAtLe` | string (date-time) | No | Items where updatedAt is less than or equal |

### Header Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

**Status Code:** 200

**Content-Type:** application/json

Returns an array of tool objects. Each tool contains comprehensive configuration including:

- Basic properties (id, name, description)
- Function parameters and schema definitions
- Server configuration for API requests
- Message templates for different states
- Error handling and retry policies
- Variable extraction plans
- Transfer and rejection configurations

## Example Request

```bash
curl -X GET "https://api.vapi.ai/tool?limit=10" \
  -H "Authorization: YOUR_API_KEY"
```

## Example Response

```json
[
  {
    "id": "tool-123",
    "name": "Get Customer Info",
    "description": "Retrieves customer information from database",
    "async": false,
    "function": {
      "name": "getCustomerInfo",
      "description": "Fetch customer details",
      "parameters": {
        "type": "object",
        "properties": {
          "customerId": {
            "type": "string",
            "description": "Unique customer identifier"
          }
        },
        "required": ["customerId"]
      }
    }
  }
]
```
