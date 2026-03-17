# PublicInbox

Methods for working with the HeyReach Inbox. Get and filter conversations and send messages from any of your accounts.

---

## POST GetConversationsV2

**Endpoint:** `https://api.heyreach.io/api/public/inbox/GetConversationsV2`

Get a paginated collection of LinkedIn conversations. Get up to 100 lists per request.

### Body Parameters

- **filters**
  - `linkedInAccountIds` (int[]): The ids of the LinkedIn senders
  - `campaignIds` (int[])
  - `searchString` (string, optional)
  - `leadLinkedInId` (string, optional) — The LinkedIn ID of the lead. You can find this ID as "linkedin_id" in the response of many of our endpoints, for example in the `/api/public/lead/GetLead` endpoint.
  - `leadProfileUrl` (string, optional) — The linkedin URL of the lead
  - `tags` — Case-insensitive list of lead's tags. Only the conversations of the leads that have at least one of the tags will be exported.
  - `seen` (boolean, optional)

### Headers

| Header | Value |
|---|---|
| `X-API-KEY` | `<string>` — API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` |
| `Accept` | `text/plain` |

### Body (raw JSON)

```json
{
    "filters": {
        "linkedInAccountIds": [],
        "campaignIds": [],
        "searchString": "",
        "leadLinkedInId": "",
        "leadProfileUrl": "https://www.linkedin.com/in/john_doe/",
        "tags": [
            "Lead tag1",
            "Lead Tag2"
        ],
        "seen": null
    },
    "offset": 0,
    "limit": 10
}
```

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/inbox/GetConversationsV2' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "filters": {
    "linkedInAccountIds": [],
    "campaignIds": [],
    "searchString": "string",
    "leadLinkedInId": "string",
    "leadProfileUrl": "string",
    "tags": [
        "Lead tag1",
        "Lead Tag2"
    ],
    "seen": null | true | false
  },
  "offset": 0,
  "limit": 10
}'
```

### Example Response

```json
{
  "totalCount": 1,
  "items": [
    {
      "id": "string",
      "read": true,
      "groupChat": true,
      "blockedByMe": true,
      "blockedByParticipant": true,
      "lastMessageAt": "2025-03-28T12:00:19.007Z",
      "lastMessageText": "string",
      "lastMessageType": "TEXT",
      "lastMessageSender": "ME",
      "totalMessages": 0,
      "linkedInAccountId": 0,
      "correspondentProfile": {
        "id": "string",
        "linkedin_id": "string",
        "profileUrl": "string",
        "firstName": "string",
        "lastName": "string",
        "headline": "string",
        "imageUrl": "string",
        "location": "string",
        "companyName": "string",
        "companyUrl": "string",
        "position": "string",
        "about": "string",
        "connections": 0,
        "followers": 0,
        "tags": [
          "string"
        ],
        "emailAddress": "string",
        "customFields": [
          {
            "name": "string",
            "value": "string"
          }
        ]
      },
      "linkedInAccount": {
        "id": 0,
        "emailAddress": "string",
        "firstName": "string",
        "lastName": "string",
        "isActive": true,
        "activeCampaigns": 0,
        "authIsValid": true,
        "isValidNavigator": true,
        "isValidRecruiter": true
      },
      "messages": [
        {
          "createdAt": "2025-03-28T12:00:19.007Z",
          "body": "string",
          "subject": "string",
          "postLink": "string",
          "isInMail": true,
          "sender": "ME"
        }
      ]
    }
  ]
}
```