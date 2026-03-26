# List Site ACLs

`GET /accounts/{account_id}/magic/sites/{site_id}/acls`

Lists Site ACLs associated with an account.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Response

### 200

List Site ACLs response

- **result** (array, optional): 

### 4XX

List Site ACLs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
