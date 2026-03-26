# List store secrets (System)

`GET /system/accounts/{account_tag}/stores/{store_id}/secrets`

Lists all secrets in a store managed by the calling service.
Returns 404 if the store doesn't exist or is not managed by the authenticated service.


## Parameters

- **account_tag** (string, required) [path]: Account tag identifier (e.g., '12a6ed19f349896cfbd6694ba3de8d31').
This is the account's external tag identifier, not the numeric account ID.

- **store_id** (string, required) [path]: 
- **direction** (string, optional) [query]: Direction to sort objects
- **page** (integer, optional) [query]: Page number
- **per_page** (integer, optional) [query]: Number of objects to return per page
- **search** (string, optional) [query]: Search secrets using a filter string, filtering across name and comment
- **order** (string, optional) [query]: Order secrets by values in the given field
- **scopes** (array, optional) [query]: Only secrets with the given scopes will be returned

## Response

### 200

List store secrets response

- **result** (array, optional): 

### 4XX

List store secrets response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
