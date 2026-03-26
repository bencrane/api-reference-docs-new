# List all AI Gateway Dynamic Route Deployments.

`GET /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments`

List all AI Gateway Dynamic Route Deployments.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Success

- **data** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
