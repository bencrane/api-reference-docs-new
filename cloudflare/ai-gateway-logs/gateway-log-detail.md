# Get Gateway Log Detail

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}`

Retrieves detailed information for a specific AI Gateway log entry.

## Parameters

- **id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Returns the log details

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
