# List mTLS certificate associations

`GET /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations`

Lists all active associations between the certificate and Cloudflare services.

## Parameters

- **mtls_certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List mTLS certificate associations response

- **result** (array, optional): 

### 4XX

List mTLS certificate associations response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
