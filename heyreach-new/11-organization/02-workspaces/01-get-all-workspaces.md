# GET GetAllWorkspaces

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/workspaces?Offset=9109&Limit=66`

List all workspaces in your organization.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Workspace API Key |
| `Accept` | `text/plain` | |

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Offset` | integer | Number of records to skip (for pagination) |
| `Limit` | integer | Maximum number of records to return |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/workspaces?Offset=9109&Limit=66' \
--header 'X-API-KEY;' \
--header 'Accept: text/plain'
```

## Example Response

```json
{
  "totalCount": 2724,
  "items": [
    {
      "workspaceId": 4395,
      "workspaceName": "string",
      "seatsLimit": 4371,
      "usedSeats": 9646
    },
    {
      "workspaceId": 6265,
      "workspaceName": "string",
      "seatsLimit": 2637,
      "usedSeats": 9005
    }
  ]
}
```