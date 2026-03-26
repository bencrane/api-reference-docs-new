# Delete mTLS certificate

`DELETE /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}`

Deletes the mTLS certificate unless the certificate is in use by one or more Cloudflare services.

## Parameters

- **mtls_certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete mTLS certificate response

- **result** (object, optional): 

### 4XX

Delete mTLS certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
