# Get an mTLS certificate

`GET /accounts/{account_id}/access/certificates/{certificate_id}`

Fetches a single mTLS certificate.

## Parameters

- **certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get an mTLS certificate response

_Empty object_

### 4XX

Get an mTLS certificate response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
