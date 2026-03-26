# Update a share resource

`PUT /accounts/{account_id}/shares/{share_id}/resources/{resource_id}`

Update is not immediate, an updated share resource object with a new status will be returned.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **resource_id** (string, required) [path]: 

## Request Body

- **meta** (object, required): Resource Metadata.

## Response

### 200

Share resource updated.

_Empty object_

### 4XX

Update share resource failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Update share resource failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
