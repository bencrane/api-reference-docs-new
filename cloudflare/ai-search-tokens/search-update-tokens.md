# Update tokens.

`PUT /accounts/{account_id}/ai-search/tokens/{id}`

Update tokens.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Request Body

- **cf_api_id** (string, required): 
- **cf_api_key** (string, required): 
- **legacy** (boolean, optional): 
- **name** (string, required): 

## Response

### 200

Returns the updated Object

- **result** (object): 
- **success** (boolean): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
