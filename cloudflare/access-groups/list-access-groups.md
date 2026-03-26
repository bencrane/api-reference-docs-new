# List Access groups

`GET /accounts/{account_id}/access/groups`

Lists all Access groups.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **search** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List Access groups response

_Empty object_

### 4XX

List Access groups response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
