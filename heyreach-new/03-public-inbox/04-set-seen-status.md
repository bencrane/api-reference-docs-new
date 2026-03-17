# POST GetAll

**Endpoint:** `https://api.heyreach.io/api/public/li_account/GetAll`

Get a paginated collection of all LinkedIn accounts. Get up to 100 accounts per request.

### Headers

| Header | Value |
|---|---|
| `X-API-KEY` | `<string>` — API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` |
| `Accept` | `text/plain` |

### Body (raw JSON)

```json
{
  "offset": 0,
  "keyword": "My account name",
  "limit": 10
}
```

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/li_account/GetAll' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "offset": "<integer>",
  "keyword": "<string>",
  "limit": "<integer>"
}'
```

### Example Response

```json
{
  "totalCount": "<integer>",
  "items": [
    {
      "id": "<integer>",
      "emailAddress": "<string>",
      "firstName": "<string>",
      "lastName": "<string>",
      "isActive": "<boolean>",
      "activeCampaigns": "<integer>",
      "authIsValid": "<boolean>",
      "isValidNavigator": "<boolean>",
      "isValidRecruiter": "<boolean>"
    },
    {
      "id": "<integer>",
      "emailAddress": "<string>",
      "firstName": "<string>",
      "lastName": "<string>",
      "isActive": "<boolean>",
      "activeCampaigns": "<integer>",
      "authIsValid": "<boolean>",
      "isValidNavigator": "<boolean>",
      "isValidRecruiter": "<boolean>"
    }
  ]
}
```