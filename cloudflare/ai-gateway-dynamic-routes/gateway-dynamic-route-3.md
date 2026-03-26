# Update an AI Gateway Dynamic Route.

`PATCH /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}`

Update an AI Gateway Dynamic Route.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Request Body

- **name** (string, required): 

## Response

### 200

Success

- **route** (object): 
- **success** (boolean): 

### 400

Input Error

- **route** (object): 
- **success** (boolean):
