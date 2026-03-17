# DELETEDeleteLeadsFromListByProfileUrl

## Endpoint

```
DELETE https://api.heyreach.io/api/public/list/DeleteLeadsFromListByProfileUrl
```

Deletes the specified leads from a lead list by LinkedIn profile URL.

**NOTE:** This endpoint will return OK (200) even if the leads are not found in the list. If leads are not found in the list, they will be returned in the response in the field `notFoundInList`, which will consist only the `username`, not the whole URL (see example response).

## Headers

| Header | Value | Description |
|---|---|---|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `"X-API-KEY: {API_KEY}"` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body (raw JSON)

```json
{
  "listId": 3672,
  "profileUrls": [
    "https://www.linkedin.com/in/john-doe/",
    "https://www.linkedin.com/in/jane-doe/"
  ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `listId` | `integer` | Yes | The ID of the list |
| `profileUrls` | `string[]` | Yes | Array of LinkedIn URLs of the leads to be deleted |

## Example Request

```bash
curl --location --request DELETE 'https://api.heyreach.io/api/public/list/DeleteLeadsFromListByProfileUrl' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "listId": 3672,
  "profileUrls": [
    "https://www.linkedin.com/in/john-doe/",
    "https://www.linkedin.com/in/jane-doe/"
  ]
}'
```

## Example Response

```json
{
  "notFoundInList": [
    "jane-doe"
  ]
}
```