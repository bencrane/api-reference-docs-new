# Update a Dataset

`PUT /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}`

Updates an existing AI Gateway dataset.

## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Request Body

- **enable** (boolean, required): 
- **filters** (array, required): 
- **name** (string, required): 

## Response

### 200

Returns the updated Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean): 

### 404

Not Found

- **errors** (array): 
- **success** (boolean):
