# Get Gateway Log Response

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response`

Retrieves the response payload for an AI Gateway log entry.

## Parameters

- **id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Returns the response body from a specific log

Type: object

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
