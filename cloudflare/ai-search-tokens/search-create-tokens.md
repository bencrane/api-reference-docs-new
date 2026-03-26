# Create new tokens.

`POST /accounts/{account_id}/ai-search/tokens`

Create a new tokens.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **cf_api_id** (string, required): 
- **cf_api_key** (string, required): 
- **legacy** (boolean, optional): 
- **name** (string, required): 

## Response

### 201

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):
