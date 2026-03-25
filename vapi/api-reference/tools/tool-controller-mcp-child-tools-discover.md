# Discover MCP Child Tools - API Reference

## Endpoint

**Method:** POST
**URL:** `https://api.vapi.ai/tool/{id}/mcp-children`

## Description

This endpoint discovers available child tools within a Model Context Protocol (MCP) parent tool, returning an array of MCP tools associated with the specified tool ID.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the parent tool |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | API Key from the Vapi Dashboard |

## Response Schema

**Status Code:** 200
**Content Type:** application/json

The response returns an array of `McpTool` objects with the following structure:

```json
[
  {
    "id": "string",
    "orgId": "string",
    "createdAt": "2024-01-01T00:00:00Z",
    "updatedAt": "2024-01-01T00:00:00Z",
    "server": {
      "url": "string",
      "timeoutSeconds": 20,
      "headers": {},
      "backoffPlan": {
        "type": "fixed|exponential",
        "maxRetries": 0,
        "baseDelaySeconds": 1
      }
    },
    "messages": [
      {
        "type": "request-start|request-complete|request-failed|request-response-delayed",
        "content": "string"
      }
    ],
    "metadata": {
      "protocol": "sse|shttp"
    },
    "rejectionPlan": {
      "conditions": []
    }
  }
]
```

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.tools.tool_controller_mcp_child_tools_discover(id="tool_id")
```

## Key Response Fields

- **id:** Unique identifier for each child tool
- **orgId:** Organization ownership identifier
- **createdAt/updatedAt:** ISO 8601 timestamps
- **server:** Webhook configuration details
- **messages:** Assistant messages during tool execution
- **metadata:** Protocol configuration (SSE or Streamable HTTP)
- **rejectionPlan:** Conditional logic for rejecting tool calls
