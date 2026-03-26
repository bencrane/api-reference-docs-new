# List Namespaces

`GET /accounts/{account_id}/workers/durable_objects/namespaces`

Returns the Durable Object namespaces owned by an account.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: Current page.
- **per_page** (integer, optional) [query]: Items per-page.

## Response

### 200

List Namespaces response.

- **result** (array, optional): 

### 4XX

List Namespaces response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
