# Remove Custom Domain From Bucket

`DELETE /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}`

Remove custom domain registration from an existing R2 bucket.

## Parameters

- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **domain** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

Delete Custom Domain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Delete Custom Domain response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
