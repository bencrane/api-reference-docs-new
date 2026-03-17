# POST Pause

**Endpoint:** `https://api.heyreach.io/api/public/campaign/Pause?campaignId=<long>`

Pauses the specified campaign.

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
curl --location --request POST 'https://api.heyreach.io/api/public/campaign/Pause?campaignId=%3Clong%3E' \
--header 'X-API-KEY: <string>' \
--header 'Accept: text/plain'
```

## Example Response

```json
{
  "totalCount": "<integer>",
  "items": [
    {
      "id": "<long>",
      "name": "<string>",
      "creationTime": "<dateTime>",
      "linkedInUserListName": "<string>",
      "linkedInUserListId": "<long>",
      "campaignAccountIds": [
        "<integer>",
        "<integer>"
      ],
      "status": null,
      "progressStats": {
        "totalUsers": "<integer>",
        "totalUsersInProgress": "<integer>",
        "totalUsersPending": "<integer>",
        "totalUsersFinished": "<integer>",
        "totalUsersFailed": "<integer>"
      },
      "excludeAlreadyMessagedGlobal": "<boolean>",
      "excludeAlreadyMessagedCampaignAccounts": "<boolean>",
      "excludeFirstConnectionCampaignAccounts": "<boolean>",
      "excludeFirstConnectionGlobal": "<boolean>",
      "excludeNoProfilePicture": "<boolean>",
      "excludeListId": "<long>"
    },
    {
      "id": "<long>",
      "name": "<string>",
      "creationTime": "<dateTime>",
      "linkedInUserListName": "<string>",
      "linkedInUserListId": "<long>",
      "campaignAccountIds": [
        "<integer>",
        "<integer>"
      ],
      "status": null,
      "progressStats": {
        "totalUsers": "<integer>",
        "totalUsersInProgress": "<integer>",
        "totalUsersPending": "<integer>",
        "totalUsersFinished": "<integer>",
        "totalUsersFailed": "<integer>"
      },
      "excludeAlreadyMessagedGlobal": "<boolean>",
      "excludeAlreadyMessagedCampaignAccounts": "<boolean>",
      "excludeFirstConnectionCampaignAccounts": "<boolean>",
      "excludeFirstConnectionGlobal": "<boolean>",
      "excludeNoProfilePicture": "<boolean>",
      "excludeListId": "<long>"
    }
  ]
}
```