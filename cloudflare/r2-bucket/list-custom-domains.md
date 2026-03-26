# List Custom Domains of Bucket

`GET /accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom`

Gets a list of all custom domains registered with an existing R2 bucket.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

List Custom Domains response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

List Custom Domains response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
