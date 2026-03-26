# List tokens.

`GET /accounts/{account_id}/ai-search/tokens`

List tokens.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 
- **order_by** (string, optional) [query]: Order By Column Name
- **order_by_direction** (string, optional) [query]: Order By Direction

## Response

### 200

List objects

- **result** (array): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):
