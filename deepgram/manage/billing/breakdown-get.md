# Get Project Billing Breakdown
Source: https://developers.deepgram.com/reference/manage/billing/breakdown/get

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/billing/breakdown`

## Description

Retrieves the billing summary for a specific project, with various filter options or by grouping options.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |

## Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start | string (date) | Optional | Start date of the requested date range. Format accepted is YYYY-MM-DD |
| end | string (date) | Optional | End date of the requested date range. Format accepted is YYYY-MM-DD |
| accessor | string | Optional | Filter for requests where a specific accessor was used |
| deployment | enum | Optional | Filter for requests where a specific deployment was used. Allowed values: `hosted`, `beta`, `self-hosted` |
| tag | string | Optional | Filter for requests where a specific tag was used |
| line_item | string | Optional | Filter requests by line item (e.g. streaming::nova-3) |
| grouping | list of enums | Optional | Group billing breakdown by one or more dimensions. Allowed values: `accessor`, `deployment`, `line_item`, `tags` |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/billing/breakdown"

querystring = {
    "accessor": "12345678-1234-1234-1234-123456789012",
    "deployment": "hosted",
    "tag": "tag1",
    "line_item": "streaming::nova-3",
    "grouping": "[\"deployment\",\"line_item\"]"
}

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

## Response

**200** - Retrieved

Billing breakdown response.

```json
{
  "start": "2025-01-16",
  "end": "2025-01-23",
  "resolution": {
    "units": "day",
    "amount": 1
  },
  "results": [
    {
      "dollars": 0.25,
      "grouping": {
        "start": "2025-01-16",
        "end": "2025-01-16",
        "accessor": "123456789012345678901234",
        "deployment": "hosted",
        "line_item": "streaming::nova-3",
        "tags": [
          "tag1",
          "tag2"
        ]
      }
    }
  ]
}
```

### Response Fields

- **start** (string, date) - Start date of the billing summary period
- **end** (string, date) - End date of the billing summary period
- **resolution** (object)
  - **units** (string)
  - **amount** (number)
- **results** (list of objects)
  - **dollars** (number)
  - **grouping** (object)

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
