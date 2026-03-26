# Upload mTLS certificate

`POST /accounts/{account_id}/mtls_certificates`

Upload a certificate that you want to use with mTLS-enabled Cloudflare services, such as Bring Your Own CA (BYO-CA) for mTLS. To create certificates issued by the Cloudflare managed CA, use the [Create Client Certificate endpoint](/api/resources/client_certificates/methods/create/).

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ca** (boolean, required): Indicates whether the certificate is a CA or leaf certificate.
- **certificates** (string, required): The uploaded root CA certificate.
- **name** (string, optional): Optional unique name for the certificate. Only used for human readability.
- **private_key** (string, optional): The private key for the certificate. This field is only needed for specific use cases such as using a custom certificate with Zero Trust's block page.

## Response

### 200

Upload mTLS certificate response

- **result** (object, optional): 

### 4XX

Upload mTLS certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
