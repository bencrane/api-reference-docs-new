# GET GetWorkspaceApiKeys

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/api-keys/workspaces/:workspaceId`

Get Public API, Make, Zapier, N8N and other relevant integration keys for a given workspace.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Workspace API Key |
| `Accept` | `text/plain` | |

## Path Variables

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workspaceId` | integer | Yes | |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/api-keys/workspaces/5421' \
--header 'X-API-KEY;' \
--header 'Accept: text/plain'
```

## Example Response

```json
{
  "apiKeys": {
    "publicApi": "string",
    "n8N": "string",
    "make": "string",
    "zapier": "string",
    "mcp": "string"
  }
}
```