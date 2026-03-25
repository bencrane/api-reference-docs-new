# List Project Billing Fields
Source: https://developers.deepgram.com/reference/manage/billing/fields/get

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/billing/fields`

## Description

Lists the accessors, deployment types, tags, and line items used for billing data in the specified time period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to know what filters are available.

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

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/billing/fields"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A list of billing fields for a specific project.

```json
{
  "accessors": [
    "12345678-1234-1234-1234-123456789012",
    "87654321-4321-4321-4321-210987654321"
  ],
  "deployments": [
    "hosted",
    "self-hosted"
  ],
  "tags": [
    "dev",
    "production"
  ],
  "line_items": {
    "streaming::nova-3": "Nova - 3 (Stream)",
    "sync::aura-2": "Aura -2 (Sync)"
  }
}
```

### Response Fields

- **accessors** (list of strings) - List of accessor UUIDs for the time period
- **deployments** (list of enums) - List of deployment types for the time period. Allowed values: `hosted`, `beta`, `self-hosted`, `dedicated`
- **tags** (list of strings) - List of tags for the time period
- **line_items** (map from strings to strings) - Map of line item names to human-readable descriptions for the time period

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
