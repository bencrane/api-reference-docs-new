# List Access identity providers

`GET /accounts/{account_id}/access/identity_providers`

Lists all configured identity providers.

## Parameters

- **account_id** (string, required) [path]: 
- **scim_enabled** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List Access identity providers response

_Empty object_

### 4XX

List Access identity providers response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
