# Delete an mTLS certificate

`DELETE /accounts/{account_id}/access/certificates/{certificate_id}`

Deletes an mTLS certificate.

## Parameters

- **certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete an mTLS certificate response

_Empty object_

### 4XX

Delete an mTLS certificate response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
