# Patch Gateway Log

`PATCH /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}`

Updates metadata for an AI Gateway log entry.

## Parameters

- **id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **feedback** (number, optional): 
- **metadata** (object, optional): 
- **score** (number, optional): 

## Response

### 200

Returns the log details

- **result** (object): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
