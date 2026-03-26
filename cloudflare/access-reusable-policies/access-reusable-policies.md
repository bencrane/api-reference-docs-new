# List Access reusable policies

`GET /accounts/{account_id}/access/policies`

Lists Access reusable policies.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List Access reusable policies response.

_Empty object_

### 4XX

List Access reusable policies response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
