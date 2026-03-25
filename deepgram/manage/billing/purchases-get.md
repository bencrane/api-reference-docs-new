# List Project Purchases
Source: https://developers.deepgram.com/reference/manage/billing/purchases/get

## Endpoint

**GET** `https://api.deepgram.com/v1/projects/:project_id/purchases`

## Description

Returns the original purchased amount on an order transaction.

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
| limit | double | Optional | Number of results to return per page. Default 10. Range [1, 1000] |

## Example Request

```python
import requests

url = "https://api.deepgram.com/v1/projects/project_id/purchases"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

## Response

**200** - Retrieved

A list of purchases for a specific project.

```json
{
  "orders": [
    {
      "order_id": "025e19ba-b6d9-4a04-9f99-4fe715aca5f1",
      "expiration": "2026-03-04T00:00:00Z",
      "created": "2023-02-21T21:13:40.014373Z",
      "amount": 150,
      "units": "usd",
      "order_type": "promotional"
    }
  ]
}
```

### Response Fields

- **orders** (list of objects)
  - **order_id** (string)
  - **expiration** (string, datetime)
  - **created** (string, datetime)
  - **amount** (number)
  - **units** (string)
  - **order_type** (string)

## Errors

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request Error |
