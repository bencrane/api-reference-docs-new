# Get raw response

`GET /accounts/{account_id}/urlscanner/v2/responses/{response_id}`

Returns the raw response of the network request. Find the `response_id` in the `data.requests.response.hash`.

## Parameters

- **response_id** (string, required) [path]: Response hash.
- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Get the raw response by its hash.

### 400

Invalid input.

- **errors** (array): 
- **message** (string): 
- **status** (integer): Status code.
