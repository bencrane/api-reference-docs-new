# Get Gateway Log Request

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request`

Retrieves the original request payload for an AI Gateway log entry.

## Parameters

- **id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Returns the request body from a specific log

Type: object

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
