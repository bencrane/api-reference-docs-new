# Delete a share resource

`DELETE /accounts/{account_id}/shares/{share_id}/resources/{resource_id}`

Deletion is not immediate, an updated share resource object with a new status will be returned.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **resource_id** (string, required) [path]: 

## Response

### 200

Share resource deleted.

_Empty object_

### 4XX

Delete share resource failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Delete share resource failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
