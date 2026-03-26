# Create Bucket

`POST /accounts/{account_id}/r2/buckets`

Creates a new R2 bucket.

## Parameters

- **account_id** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

- **locationHint** (string, optional): Location of the bucket. Values: `apac`, `eeur`, `enam`, `weur`, `wnam`, `oc`
- **name** (string, required): Name of the bucket.
- **storageClass** (string, optional): Storage class for newly uploaded objects, unless specified otherwise. Values: `Standard`, `InfrequentAccess`

## Response

### 200

Create Bucket response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A single R2 bucket.
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Create Bucket response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
