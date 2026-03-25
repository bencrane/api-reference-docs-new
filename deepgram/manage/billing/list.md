# Get Project Balances
Source: https://developers.deepgram.com/reference/manage/billing/list

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/balances`

## Description

Generates a list of outstanding balances for the specified project.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/balances"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A list of outstanding balances.

```json
{
  "balances": [
    {
      "balance_id": "bal_9f8d7c6a2b3e4f1d",
      "amount": 1250.75,
      "units": "USD",
      "purchase_order_id": "po_20240427_001"
    }
  ]
}
```

### Response Fields

- **balances** (list of objects)
  - **balance_id** (string) - The unique identifier of the balance
  - **amount** (double) - The amount of the balance
  - **units** (string) - The units of the balance
  - **purchase_order_id** (string) - Description or reference of the purchase

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
