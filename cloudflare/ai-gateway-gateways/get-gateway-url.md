# Get Gateway URL

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/url/{provider}`

Retrieves the endpoint URL for an AI Gateway.

## Parameters

- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **provider** (string, required) [path]: 

## Response

### 200

Returns the log details

- **result** (string): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
