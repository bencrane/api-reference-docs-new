# Create a new AI Gateway Dynamic Route Version.

`POST /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions`

Create a new AI Gateway Dynamic Route Version.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Request Body

- **elements** (array, required): 

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
