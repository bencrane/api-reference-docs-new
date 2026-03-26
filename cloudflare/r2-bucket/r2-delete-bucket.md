# Delete Bucket

`DELETE /accounts/{account_id}/r2/buckets/{bucket_name}`

Deletes an existing R2 bucket.

## Parameters

- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

Delete Bucket response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete Bucket response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
