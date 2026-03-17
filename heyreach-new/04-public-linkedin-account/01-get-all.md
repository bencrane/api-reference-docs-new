# GET GetById

**Endpoint:** `https://api.heyreach.io/api/public/li_account/GetById?accountId=<integer>`

Get a LinkedIn account by id.

### Headers

| Header | Value |
|---|---|
| `X-API-KEY` | `<string>` — API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Accept` | `text/plain` |

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `accountId` | integer | Yes | Id of the account to be returned |

### Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/li_account/GetById?accountId=%3Cinteger%3E' \
--header 'X-API-KEY: <string>' \
--header 'Accept: text/plain'
```

### Example Response

```json
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
```