# Read tokens.

`GET /accounts/{account_id}/ai-search/tokens/{id}`

Read tokens.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Returns a single object if found

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
