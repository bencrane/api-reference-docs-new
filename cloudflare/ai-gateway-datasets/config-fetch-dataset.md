# Fetch a Dataset

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}`

Retrieves details for a specific AI Gateway dataset.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Returns a single object if found

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
