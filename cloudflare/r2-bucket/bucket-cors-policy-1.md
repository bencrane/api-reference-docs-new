# Get Bucket CORS Policy

`GET /accounts/{account_id}/r2/buckets/{bucket_name}/cors`

Get the CORS policy for a bucket.

## Parameters

- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

Success Response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Error Response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
