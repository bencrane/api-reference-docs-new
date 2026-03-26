# Read instances.

`GET /accounts/{account_id}/ai-search/instances/{id}`

Read instances.

## Parameters

- **id** (string, required) [path]: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **account_id** (string, required) [path]: 

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
