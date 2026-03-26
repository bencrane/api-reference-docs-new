# Get Bucket

`GET /accounts/{account_id}/r2/buckets/{bucket_name}`

Gets properties of an existing R2 bucket.

## Parameters

- **account_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

Get Bucket response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A single R2 bucket.
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Get Bucket response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
