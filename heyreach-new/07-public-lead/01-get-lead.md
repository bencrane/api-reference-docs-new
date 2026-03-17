# POST GetLead

**Endpoint:** `https://api.heyreach.io/api/public/lead/GetLead`

Gets Lead Details.

This endpoint retrieves the details of a specific lead based on their LinkedIn profile URL. The response will provide detailed information about the lead that matches the specified profile URL.

## Headers

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | `<string>` | API key header using this scheme. Example: `X-API-KEY: {API_KEY}` |
| `Content-Type` | `application/json` | |
| `Accept` | `text/plain` | |

## Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `profileUrl` | string | Yes | The LinkedIn profile URL of the lead |

## Body (raw JSON)

```json
{
  "profileUrl": "https://www.linkedin.com/in/john_doe/"
}
```

## Example Request

```bash
curl --location 'https://api.heyreach.io/api/public/lead/GetLead' \
--header 'X-API-KEY: <string>' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--data '{
  "profileUrl": "https://www.linkedin.com/in/john_doe/"
}'
```

## Example Response

```json
{
  "linkedin_id": "63456789",
  "imageUrl": "https://media.licdn.com/dms/image/v2/some_url",
  "firstName": "John",
  "lastName": "Doe",
  "fullName": "John Doe",
  "location": "Texas",
  "summary": "",
  "companyName": "Marines",
  "companyUrl": "https://www.linkedin.com/company/marines",
  "position": "Director of Marines",
  "industry": null,
  "about": null,
  "username": "john_doe",
  "emailAddress": null,
  "connections": 0,
  "followers": 0,
  "experiences": "[]",
  "education": "[]",
  "profileUrl": "https://www.linkedin.com/in/john_doe",
  "enrichedEmailAddress": "john_doe@example.com",
  "headline": null,
  "emailEnrichments": [
    "john_doe@example.com"
  ]
}
```