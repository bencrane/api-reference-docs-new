# Create a new AI Gateway Dynamic Route Deployment.

`POST /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments`

Create a new AI Gateway Dynamic Route Deployment.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Request Body

- **version_id** (string, required): 

## Response

### 200

Success

- **result** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
