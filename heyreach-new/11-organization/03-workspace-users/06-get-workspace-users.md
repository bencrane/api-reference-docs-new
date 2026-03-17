# POST GetWorkspaceUsers

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/users/workspaces/:workspaceId`

Get all users in a given workspace along with their role and permissions.

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
  "offset": 895,
  "role": "Admin",
  "invitationStatus": [
    "Accepted",
    "Pending"
  ],
  "limit": 38
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/users/workspaces/5421' \
--header 'X-API-KEY;' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "offset": 895,
  "role": "Admin",
  "invitationStatus": [
    "Accepted",
    "Pending"
  ],
  "limit": 38
}'
```

## Example Response

```json
{
  "totalCount": 1040,
  "items": [
    {
      "workspaceId": 9178,
      "organizationPermissions": {
        "userDeactivate": false,
        "manageWorkspace": false,
        "manageWorkspaceMembers": false,
        "viewBilling": false,
        "manageBlling": false,
        "manageBillingDetails": false,
        "accessBillingInvoiceHistoy": false
      },
      "workspacePermissions": {
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
      "userDetails": {
        "userId": 5497,
        "name": "string",
        "surname": "string",
        "email": "string",
        "roles": [
          "string",
          "string"
        ]
      },
      "userInvitation": {
        "invitationId": 1916,
        "invitationStatus": "Accepted",
        "invitationUrl": "string",
        "expirationTime": "2011-01-09T19:33:34.216Z"
      }
    },
    {
      "workspaceId": 7874,
      "organizationPermissions": {
        "userDeactivate": false,
        "manageWorkspace": false,
        "manageWorkspaceMembers": false,
        "viewBilling": false,
        "manageBlling": false,
        "manageBillingDetails": false,
        "accessBillingInvoiceHistoy": false
      },
      "workspacePermissions": {
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
      "userDetails": {
        "userId": 8221,
        "name": "string",
        "surname": "string",
        "email": "string",
        "roles": [
          "string",
          "string"
        ]
      },
      "userInvitation": {
        "invitationId": 5704,
        "invitationStatus": "Pending",
        "invitationUrl": "string",
        "expirationTime": "2006-06-07T07:59:17.346Z"
      }
    }
  ]
}
```