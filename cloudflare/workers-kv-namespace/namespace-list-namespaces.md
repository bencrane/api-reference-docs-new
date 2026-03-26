# List Namespaces

`GET /accounts/{account_id}/storage/kv/namespaces`

Returns the namespaces owned by an account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List Namespaces response.

- **result** (array, optional): 

### 4XX

List Namespaces response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
