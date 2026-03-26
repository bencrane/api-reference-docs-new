# List service tokens

`GET /accounts/{account_id}/access/service_tokens`

Lists all service tokens.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **search** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List service tokens response

_Empty object_

### 4XX

List service tokens response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
