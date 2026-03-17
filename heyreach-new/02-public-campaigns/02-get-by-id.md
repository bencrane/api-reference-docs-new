# GET GetById

**Endpoint:** `https://api.heyreach.io/api/public/campaign/GetById?campaignId=<long>`

Get a Campaign by id.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Accept` | `text/plain` | |

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `campaignId` | `<long>` | Yes | |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/campaign/GetById?campaignId=%3Clong%3E' \
--header 'X-API-KEY: <string>' \
--header 'Accept: text/plain'
```

## Example Response

```json
{
  "id": 274079,
  "name": "My First Campaign",
  "creationTime": "2025-12-01T08:06:15.463169Z",
  "linkedInUserListName": "LinkedIn Ad BF Leads",
  "linkedInUserListId": 123456,
  "campaignAccountIds": [
    113298
  ],
  "status": "IN_PROGRESS",
  "progressStats": {
    "totalUsers": 9,
    "totalUsersInProgress": 8,
    "totalUsersPending": 0,
    "totalUsersFinished": 1,
    "totalUsersFailed": 0,
    "totalUsersManuallyStopped": 0,
    "totalUsersExcluded": 0
  },
  "excludeInOtherCampaigns": false,
  "excludeHasOtherAccConversations": false,
  "excludeContactedFromSenderInOtherCampaign": false,
  "excludeListId": null,
  "organizationUnitId": 12345
}
```