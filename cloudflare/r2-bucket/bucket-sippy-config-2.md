# Enable Sippy

`PUT /accounts/{account_id}/r2/buckets/{bucket_name}/sippy`

Sets configuration for Sippy for an existing R2 bucket.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

One of: Variant 1, Variant 2, Variant 3

## Response

### 200

Set Sippy Configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Get Sippy Configuration response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
