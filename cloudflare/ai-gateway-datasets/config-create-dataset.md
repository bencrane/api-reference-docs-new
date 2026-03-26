# Create a new Dataset

`POST /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets`

Creates a new AI Gateway.

## Parameters

- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **enable** (boolean, required): 
- **filters** (array, required): 
- **name** (string, required): 

## Response

### 200

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):
