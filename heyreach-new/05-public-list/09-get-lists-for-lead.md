# POSTGetListsForLead

## Endpoint

```
POST https://api.heyreach.io/api/public/list/GetListsForLead
```

Retrieves the lists associated with a specific lead.

**Remark:** The response will include lead lists that match the provided lead details such as email, LinkedIn ID, or profile URL.

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "email": "john_doe@example.com",
  "linkedinId": "121313fsdf234",
  "profileUrl": "https://www.linkedin.com/in/john_doe/",
  "offset": 0,
  "limit": 100
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | No | The email address of the lead |
| `linkedinId` | `string` | No | The LinkedIn ID of the lead |
| `profileUrl` | `string` | No | The LinkedIn profile URL of the lead, e.g. `https://www.linkedin.com/in/john_doe/` |
| `offset` | `integer` | No | The number of records to skip (for pagination) |
| `limit` | `integer` | No | The maximum number of records to return |

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/list/GetListsForLead' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "email": "",
  "linkedinId": "",
  "profileUrl": "https://www.linkedin.com/in/john_doe/",
  "offset": 0,
  "limit": 100
}'
```

## Example Response

```json
{
  "totalCount": 2,
  "items": [
    {
      "listId": 3457,
      "listName": "Veterans in USA"
    },
    {
      "listId": 3468,
      "listName": "Rich and Famous"
    }
  ]
}
```