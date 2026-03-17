# POST CreateWorkspace

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/workspaces`

Create new workspace in your organization.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Workspace API Key |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "workspaceName": "string",
  "seatsLimit": null
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/workspaces' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "workspaceName": "string",
  "seatsLimit": null
}'
```

## Example Response

```json
{
  "workspaceId": 147,
  "workspaceName": "string",
  "seatsLimit": 8114
}
```