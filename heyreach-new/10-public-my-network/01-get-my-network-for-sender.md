# POST GetMyNetworkForSender

**Endpoint:** `https://api.heyreach.io/api/public/MyNetwork/GetMyNetworkForSender`

Gets paginated list of the network for the specified sender.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `pageNumber` | integer | Page number for pagination |
| `pageSize` | integer | Number of records per page |
| `senderId` | number | The id of the sender account for which to retrieve the network |

## Body (raw JSON)

```json
{
  "pageNumber": 0,
  "pageSize": 100,
  "senderId": 1234
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/MyNetwork/GetMyNetworkForSender' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "pageNumber": 0,
  "pageSize": 100,
  "senderId": 1234
}'
```

## Example Response

```json
{
  "totalCount": 40,
  "items": [
    {
      "linkedin_id": "6259333",
      "profileUrl": "https://www.linkedin.com/in/john-doe-1",
      "firstName": "John",
      "lastName": "Doe",
      "headline": null,
      "imageUrl": "https://media.licdn.com/dms/image/v2/764806400&v=beta&t=AqQ71ae2Oq7OGFRFL_j_6ihM5d0QSL_uiJIJmPuTD7w",
      "location": "USA",
      "companyName": "Army",
      "companyUrl": null,
      "position": "Senior Software Developer",
      "about": null,
      "connections": 0,
      "followers": 0,
      "emailAddress": null,
      "enrichedEmailAddress": null,
      "customEmailAddress": null
    },
    {
      "linkedin_id": "2207777",
      "profileUrl": "https://www.linkedin.com/in/john-doe-2",
      "firstName": "John",
      "lastName": "Doe",
      "headline": null,
      "imageUrl": "https://media.licdn.com/dms/image/v2/_u_5b-ik7oUwKDvZDJ1nvoioIMx0-vpJRXE",
      "location": null,
      "companyName": null,
      "companyUrl": null,
      "position": null,
      "about": null,
      "connections": 0,
      "followers": 0,
      "emailAddress": null,
      "enrichedEmailAddress": null,
      "customEmailAddress": null
    }
  ]
}
```