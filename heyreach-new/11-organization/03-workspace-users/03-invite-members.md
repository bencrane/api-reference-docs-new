# POST InviteMembers

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/users/invite/members`

Invite one or multiple users in your organization. Specify the relevant permissions for each invited user. The invitation emails will not be sent, only an invitation URL is generated. You can send this URL to the relevant user in order to register them to HeyReach.

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
  "workspaceIds": [
    8731,
    1166
  ],
  "permissions": {
    "viewLinkedInSenders": false,
    "manageLinkedInSendersSettings": false,
    "viewLeadLists": false,
    "importEditManageLeadLists": false,
    "viewMyNetwork": false,
    "viewCampaigns": false,
    "editManageCampaigns": false,
    "viewLinkedInSenderInboxes": false,
    "replyFromLinkedInSenderInboxes": false,
    "viewIntegrations": false,
    "manageIntegrations": false,
    "exportDataToCRMs": false,
    "viewNotifications": false,
    "manageNotifications": false
  },
  "emails": [
    "string",
    "string"
  ]
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/users/invite/members' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data-raw '{
  "inviterEmail": "admin@example.com",
  "workspaceIds": [
    8731,
    1166
  ],
  "permissions": {
    "viewLinkedInSenders": false,
    "manageLinkedInSendersSettings": false,
    "viewLeadLists": false,
    "importEditManageLeadLists": false,
    "viewMyNetwork": false,
    "viewCampaigns": false,
    "editManageCampaigns": false,
    "viewLinkedInSenderInboxes": false,
    "replyFromLinkedInSenderInboxes": false,
    "viewIntegrations": false,
    "manageIntegrations": false,
    "exportDataToCRMs": false,
    "viewNotifications": false,
    "manageNotifications": false
  },
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