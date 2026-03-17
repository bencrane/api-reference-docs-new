# POST CreateWorkspaceApiKeys

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/api-keys/workspaces/:workspaceId`

Generate new API/Integration (Make, Zapier, N8N etc.) keys in a given workspace.

Available API key types: `PUBLIC`, `N8N`, `MAKE`, `ZAPIER`, `MCP`.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Workspace API Key |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Path Variables

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workspaceId` | integer | Yes | |

## Body (raw JSON)

```json
{
  "apiKeyType": "PUBLIC|N8N|MAKE|ZAPIER|MCP"
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/api-keys/workspaces/5421' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "apiKeyType": "ZAPIER"
}'
```

## Example Response

```json
{
  "key": "string",
  "previousKeyStatus": "Deactivated"
}
```