# Create a new Evaluation

`POST /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations`

Creates a new AI Gateway.

## Parameters

- **gateway_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **dataset_ids** (array, required): 
- **evaluation_type_ids** (array, required): 
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
