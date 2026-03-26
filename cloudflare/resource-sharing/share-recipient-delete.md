# Delete a share recipient

`DELETE /accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}`

Deletion is not immediate, an updated share recipient object with a new status will be returned.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **recipient_id** (string, required) [path]: 

## Response

### 200

Share recipient deleted.

_Empty object_

### 4XX

Delete share recipient failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Delete share recipient failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
