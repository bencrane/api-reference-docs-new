# List Workers

`GET /accounts/{account_id}/workers/workers`

List all Workers for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: Current page.
- **per_page** (integer, optional) [query]: Items per-page.
- **order_by** (string, optional) [query]: Property to sort results by.
- **order** (string, optional) [query]: Sort direction.

## Response

### 200

List Workers success.

- **result** (array, optional): 

### 401

Authentication required or insufficient permissions.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 500

Internal Server Error - An unexpected server error occurred.

- **errors** (array, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
