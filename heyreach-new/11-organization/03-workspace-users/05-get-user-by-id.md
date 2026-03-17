# GET GetUserById

**Endpoint:** `https://api.heyreach.io/api/public/management/organizations/users/:userId`

Get information about a given user.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | Workspace API Key |
| `Accept` | `text/plain` | |

## Path Variables

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `userId` | integer | Yes | |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/management/organizations/users/5421' \
--header 'X-API-KEY;' \
--header 'Accept: text/plain'
```

## Example Response

```json
{
  "userDetails": {
    "userId": 1846,
    "name": "string",
    "surname": "string",
    "email": "string",
    "roles": [
      "string",
      "string"
    ]
  },
  "organizationPermissions": {
    "userDeactivate": false,
    "manageWorkspace": false,
    "manageWorkspaceMembers": false,
    "viewBilling": false,
    "manageBlling": false,
    "manageBillingDetails": false,
    "accessBillingInvoiceHistoy": false
  },
  "workspacesPermissions": [
    {
      "workspaceName": "string",
      "workspaceId": 8053,
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
      }
    },
    {
      "workspaceName": "string",
      "workspaceId": 781,
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
      }
    }
  ]
}
```