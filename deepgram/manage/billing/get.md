# Get a Project Balance
Source: https://developers.deepgram.com/reference/manage/billing/get

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/balances/:balance_id`

## Description

Retrieves details about the specified balance.

## Authentication

- **Authorization**: Token
- Use `Authorization: Token <API_KEY>`
- Example: `Authorization: Token 12345abcdef`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project_id | string | Required | The project ID |
| balance_id | string | Required | The balance ID |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/balances/balance_id"

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

A specific balance.

```json
{
  "balance_id": "bal_9f8d7c6b5a4e3d2c1b0a",
  "amount": 12500,
  "units": "minutes",
  "purchase_order_id": "po_20240615_00123"
}
```

### Response Fields

- **balance_id** (string) - The unique identifier of the balance
- **amount** (double, defaults to 0) - The amount of the balance
- **units** (string) - The units of the balance, such as "USD"
- **purchase_order_id** (string) - Description or reference of the purchase

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
