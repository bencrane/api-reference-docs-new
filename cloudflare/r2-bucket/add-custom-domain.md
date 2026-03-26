# Attach Custom Domain To Bucket

`POST /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom`

Register a new custom domain for an existing R2 bucket.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

- **ciphers** (array, optional): An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
- **domain** (string, required): Name of the custom domain to be added.
- **enabled** (boolean, required): Whether to enable public bucket access at the custom domain. If undefined, the domain will be enabled.
- **minTLS** (string, optional): Minimum TLS Version the custom domain will accept for incoming connections. If not set, defaults to 1.0. Values: `1.0`, `1.1`, `1.2`, `1.3`
- **zoneId** (string, required): Zone ID of the custom domain.

## Response

### 200

Add Custom Domain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Add Custom Domain response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
