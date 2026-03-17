# PATCH UpdateWorkspace

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/workspaces/:workspaceId`

Update a given workspace in your organization.

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
  "workspaceName": "string",
  "seatsLimit": {
    "value": 9730
  }
}
```

## Example Request

```bash
curl --location --request PATCH 'https://api.heyreach.io/api/public/management/organizations/workspaces/3642' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "workspaceName": "string",
  "seatsLimit": {
    "value": 9730
  }
}'
```

## Example Response

```json
{
  "workspaceId": 9419,
  "workspaceName": "string",
  "seatsLimit": 2983,
  "usedSeats": 9967
}
```