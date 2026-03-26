# Base image

`GET /accounts/{account_id}/images/v1/{image_id}/blob`

Fetch base image. For most images this will be the originally uploaded file. For larger images it can be a near-lossless version of the original.

## Parameters

- **image_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Base image response. Returns uploaded image data.

### 4XX

Base image response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
