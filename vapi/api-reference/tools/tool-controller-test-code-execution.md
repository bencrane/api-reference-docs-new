# Test Code Tool Execution API Reference

## Endpoint

**POST** `https://api.vapi.ai/tool/code/test`

## Description

This endpoint allows you to test the execution of a code tool, returning results along with execution metrics and any generated logs.

## Authentication

- **Type:** Bearer Token
- **Header:** `Authorization`
- **Required:** Yes
- **Details:** "Retrieve your API Key from Dashboard"

## Request Parameters

| Parameter | Location | Type | Required | Description |
|-----------|----------|------|----------|-------------|
| Authorization | Header | string | Yes | API key for authentication |

## Response Schema

The endpoint returns a 200 status with the following structure:

```json
{
  "success": boolean,
  "result": {},
  "error": string,
  "logs": string,
  "executionTimeMs": number
}
```

### Response Fields

- **success**: Boolean indicating whether execution completed successfully
- **result**: Object containing the execution output
- **error**: String describing any error that occurred
- **logs**: String containing output logs from execution
- **executionTimeMs**: Numeric value (double) representing execution duration in milliseconds

## SDK Example

```python
from vapi import Vapi

client = Vapi(token="YOUR_TOKEN_HERE")
client.tools.tool_controller_test_code_execution()
```
