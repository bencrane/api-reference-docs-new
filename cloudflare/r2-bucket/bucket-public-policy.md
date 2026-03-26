# Get r2.dev Domain of Bucket

`GET /accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed`

Gets state of public access over the bucket's R2-managed (r2.dev) domain.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

Get Managed Subdomain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Get Managed Subdomain response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
