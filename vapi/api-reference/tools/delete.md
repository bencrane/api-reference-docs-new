# Delete Tool API Reference

## Endpoint

**DELETE** `https://api.vapi.ai/tool/{id}`

## Description

Removes a tool from your Vapi account. This operation permanently deletes the specified tool resource.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the tool to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200 OK)

```json
Content-Type: application/json
```

The response returns the deleted tool object.

## Example Request

```bash
curl -X DELETE "https://api.vapi.ai/tool/tool_abc123" \
  -H "Authorization: YOUR_API_KEY"
```

## Notes

- This is a destructive operation and cannot be undone
- The tool ID must exist in your account
- Ensure proper authorization credentials are provided in the header
