# POSTGetLeadsFromList

## Endpoint

```
POST https://api.heyreach.io/api/public/list/GetLeadsFromList
```

Get a paginated collection of leads from a lead list. Get up to 1000 leads per request.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "listId": 123,
  "offset": 0,
  "keyword": "",
  "leadProfileUrl": "https://www.linkedin.com/in/john-doe/",
  "leadLinkedInId": "121313fsdf234",
  "limit": 10,
  "createdFrom": "2024-10-06T17:34:00+02:00",
  "createdTo": "2024-10-07T17:34:00+02:00"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `listId` | `<long>` | Yes | The id of the lead list |
| `offset` | `<integer>` | No | Pagination offset |
| `keyword` | `<string>` | No | A search term to filter leads by name or other relevant fields |
| `leadProfileUrl` | `string` | No | The LinkedIn profile URL of the lead, e.g. `https://www.linkedin.com/in/john-doe/` |
| `leadLinkedInId` | `string` | No | The LinkedIn ID of the lead. Found as `linkedin_id` in responses of many endpoints, e.g. `/api/public/lead/GetLead` |
| `limit` | `<integer>` | No | Number of leads to return (max 1000) |
| `createdFrom` | `string` (ISO 8601) | No | Start date/time for filtering leads by creation timestamp. Only leads created on or after this date will be included |
| `createdTo` | `string` (ISO 8601) | No | End date/time for filtering leads by creation timestamp. Only leads created before or at this date will be included |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/GetLeadsFromList' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "listId": "<long>",
  "offset": "<integer>",
  "keyword": "<string>",
  "leadProfileUrl": "string",
  "leadLinkedInId": "string",
  "limit": "<integer>"
}'
```

## Example Response

```json
{
  "totalCount": "<integer>",
  "items": [
    {
      "profileUrl": "<string>",
      "firstName": "<string>",
      "lastName": "<string>",
      "headline": "<string>",
      "imageUrl": "<string>",
      "location": "<string>",
      "companyName": "<string>",
      "companyUrl": "<string>",
      "position": "<string>",
      "about": "<string>",
      "connections": "<integer>",
      "followers": "<integer>",
      "tags": [
        "<string>",
        "<string>"
      ],
      "emailAddress": "<string>",
      "customFields": [
        {
          "name": "<string>",
          "value": "<string>"
        },
        {
          "name": "<string>",
          "value": "<string>"
        }
      ]
    },
    {
      "profileUrl": "<string>",
      "firstName": "<string>",
      "lastName": "<string>",
      "headline": "<string>",
      "imageUrl": "<string>",
      "location": "<string>",
      "companyName": "<string>",
      "companyUrl": "<string>",
      "position": "<string>",
      "about": "<string>",
      "connections": "<integer>",
      "followers": "<integer>",
      "tags": [
        "<string>",
        "<string>"
      ],
      "emailAddress": "<string>",
      "customFields": [
        {
          "name": "<string>",
          "value": "<string>"
        },
        {
          "name": "<string>",
          "value": "<string>"
        }
      ]
    }
  ]
}
```