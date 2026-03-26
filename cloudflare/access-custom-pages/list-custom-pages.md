# List custom pages

`GET /accounts/{account_id}/access/custom_pages`

List custom pages

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List custom pages response

_Empty object_

### 4XX

List custom pages response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
