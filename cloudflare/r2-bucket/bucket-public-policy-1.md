# Update r2.dev Domain of Bucket

`PUT /accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed`

Updates state of public access over the bucket's R2-managed (r2.dev) domain.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

- **enabled** (boolean, required): Whether to enable public bucket access at the r2.dev domain.

## Response

### 200

Update Managed Subdomain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Update Managed Subdomain response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
