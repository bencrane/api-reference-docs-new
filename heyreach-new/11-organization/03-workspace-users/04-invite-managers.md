# POST InviteManagers

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/users/invite/managers`

Invite one or multiple users as managers in your organization. Manager users are special kind of users that exist outside your organization and are invited to specific workspaces. These users will not be part of your organization and only have access to the specified workspaces. These users are automatically added to your workspace and don't need to register.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Workspace API Key |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "inviterEmail": "admin@example.com",
  "emails": [
    "string",
    "string"
  ],
  "workspaceIds": [
    6519,
    3651
  ]
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/users/invite/managers' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data-raw '{
  "inviterEmail": "admin@example.com",
  "emails": [
    "string",
    "string"
  ],
  "workspaceIds": [
    6519,
    3651
  ]
}'
```

## Example Response

```json
[
  {
    "workspaces": [
      {
        "workspaceId": 5937,
        "success": true,
        "errorCode": "Success",
        "errorMessage": "string"
      },
      {
        "workspaceId": 2957,
        "success": true,
        "errorCode": "UnknownError",
        "errorMessage": "string"
      }
    ],
    "invitationId": 7510,
    "invitationStatus": "Pending",
    "invitationUrl": "string",
    "invitationExpirationTime": "2011-12-31T22:55:45.978Z",
    "emailAddress": "string"
  },
  {
    "workspaces": [
      {
        "workspaceId": 9214,
        "success": true,
        "errorCode": "UnknownError",
        "errorMessage": "string"
      },
      {
        "workspaceId": 1177,
        "success": false,
        "errorCode": "WorkspaceDoesNotExists",
        "errorMessage": "string"
      }
    ],
    "invitationId": 8662,
    "invitationStatus": "Revoked",
    "invitationUrl": "string",
    "invitationExpirationTime": "1947-11-19T13:31:07.591Z",
    "emailAddress": "string"
  }
]
```