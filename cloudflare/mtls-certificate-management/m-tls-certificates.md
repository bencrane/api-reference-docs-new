# List mTLS certificates

`GET /accounts/{account_id}/mtls_certificates`

Lists all mTLS certificates uploaded to your account, such as Bring Your Own CA (BYO-CA) for mTLS. To list certificates issued by the Cloudflare managed CA, use the [List Client Certificates endpoint](/api/resources/client_certificates/methods/list/).

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List mTLS certificates response

- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List mTLS certificates response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
