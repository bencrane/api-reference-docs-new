# Update a share

`PUT /accounts/{account_id}/shares/{share_id}`

Updating is not immediate, an updated share object with a new status will be returned.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The name of the share.

## Response

### 200

Share updated.

_Empty object_

### 4XX

Update share failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Update share failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
