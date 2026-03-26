# Put Local Uploads Configuration

`PUT /accounts/{account_id}/r2/buckets/{bucket_name}/local-uploads`

Set the local uploads configuration for a bucket. When enabled, object's data is written to the nearest region first, then asynchronously replicated to the bucket's primary region.

## Parameters

- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): Whether to enable local uploads for this bucket.

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
