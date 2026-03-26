# Search Workers

`GET /accounts/{account_id}/workers/scripts-search`

Search for Workers in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **id** (string, optional) [query]: 
- **order_by** (string, optional) [query]: 
- **page** (integer, optional) [query]: Current page.
- **per_page** (integer, optional) [query]: Items per page.

## Response

### 200

Search Workers success.

- **result** (array, optional): 

### 4XX

Search Workers failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
