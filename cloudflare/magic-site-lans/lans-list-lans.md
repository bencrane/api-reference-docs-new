# List Site LANs

`GET /accounts/{account_id}/magic/sites/{site_id}/lans`

Lists Site LANs associated with an account.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Response

### 200

List Site LANs response

- **result** (array, optional): 

### 4XX

List Site LANs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
