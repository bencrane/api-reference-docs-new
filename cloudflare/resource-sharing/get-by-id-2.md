# Get share resource by ID

`GET /accounts/{account_id}/shares/{share_id}/resources/{resource_id}`

Get share resource by ID.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **resource_id** (string, required) [path]: 

## Response

### 200

Get account share resource response.

_Empty object_

### 4XX

Get account share resource response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Get account share resource response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
