# List Site WANs

`GET /accounts/{account_id}/magic/sites/{site_id}/wans`

Lists Site WANs associated with an account.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Response

### 200

List Site WANs response

- **result** (array, optional): 

### 4XX

List Site WANs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
