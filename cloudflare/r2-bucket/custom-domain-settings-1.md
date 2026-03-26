# Configure Custom Domain Settings

`PUT /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}`

Edit the configuration for a custom domain on an existing R2 bucket.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **domain** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

- **ciphers** (array, optional): An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
- **enabled** (boolean, optional): Whether to enable public bucket access at the specified custom domain.
- **minTLS** (string, optional): Minimum TLS Version the custom domain will accept for incoming connections. If not set, defaults to previous value. Values: `1.0`, `1.1`, `1.2`, `1.3`

## Response

### 200

Edit Custom Domain Configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Edit Custom Domain Configuration response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
