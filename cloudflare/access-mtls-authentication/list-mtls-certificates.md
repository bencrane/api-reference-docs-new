# List mTLS certificates

`GET /accounts/{account_id}/access/certificates`

Lists all mTLS root certificates.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List mTLS certificates response

_Empty object_

### 4XX

List mTLS certificates response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
