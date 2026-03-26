# Get mTLS certificate

`GET /accounts/{account_id}/mtls_certificates/{mtls_certificate_id}`

Fetches a single mTLS certificate uploaded to your account. To get a certificate issued by the Cloudflare managed CA, use the [Client Certificate Details endpoint](/api/resources/client_certificates/methods/get/).

## Parameters

- **mtls_certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get mTLS certificate response

- **result** (object, optional): 

### 4XX

Get mTLS certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
