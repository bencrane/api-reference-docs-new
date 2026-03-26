# List account stores (System)

`GET /system/accounts/{account_tag}/stores`

Lists all stores in an account that are managed by the calling service.
Only returns stores where managed_by matches the authenticated service.


## Parameters

- **account_tag** (string, required) [path]: Account tag identifier (e.g., '12a6ed19f349896cfbd6694ba3de8d31').
This is the account's external tag identifier, not the numeric account ID.

- **direction** (string, optional) [query]: Direction to sort objects
- **page** (integer, optional) [query]: Page number
- **per_page** (integer, optional) [query]: Number of objects to return per page
- **order** (string, optional) [query]: Order secrets by values in the given field

## Response

### 200

List account stores response

- **result** (array, optional): 

### 4XX

List account stores response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
