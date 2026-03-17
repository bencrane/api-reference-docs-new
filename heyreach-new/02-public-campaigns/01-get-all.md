# PublicCampaigns

Methods for working with HeyReach campaigns. Filter, pause, resume, and manage leads inside your campaigns.

---

## POST GetAll

**Endpoint:** `https://api.heyreach.io/api/public/campaign/GetAll`

Get a paginated collection of all campaigns. Get up to 100 campaigns per request.

### Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `{{HR_API_KEY}}` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

### Body (raw JSON)

```json
{
  "offset": 0,
  "keyword": "my campaign name",
  "statuses": ["DRAFT", "IN_PROGRESS", "PAUSED", "FINISHED", "CANCELED", "FAILED", "STARTING", "SCHEDULED"],
  "accountIds": [123, 2, 5],
  "limit": 10
}
```

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/campaign/GetAll' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "offset": "<integer>",
  "keyword": "<string>",
  "statuses": [
    null,
    null
  ],
  "accountIds": [
    "<integer>",
    "<integer>"
  ],
  "limit": "<integer>"
}'
```

### Example Response

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