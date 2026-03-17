# POST InviteAdmins

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/users/invite/admins`

Invite one or multiple users as admins in your organization. The invitation emails will not be sent, only an invitation URL is generated. You can send this URL to the relevant user in order to register them to HeyReach.

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
  ]
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/users/invite/admins' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data-raw '{
  "inviterEmail": "admin@example.com",
  "emails": [
    "string",
    "string"
  ]
}'
```

## Example Response

```json
[
  {
    "success": true,
    "errorCode": "WorkspaceDoesNotExists",
    "errorMessage": "string",
    "invitationId": 5337,
    "invitationStatus": "Unknown",
    "invitationUrl": "string",
    "invitationExpirationTime": "1963-11-08T00:06:36.607Z",
    "emailAddress": "string"
  },
  {
    "success": true,
    "errorCode": "MemberExistsAsAdmin",
    "errorMessage": "string",
    "invitationId": 4677,
    "invitationStatus": "Unknown",
    "invitationUrl": "string",
    "invitationExpirationTime": "1993-11-23T11:25:45.256Z",
    "emailAddress": "string"
  }
]
```