# List share resources by share ID

`GET /accounts/{account_id}/shares/{share_id}/resources`

List share resources by share ID.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **status** (string, optional) [query]: Filter share resources by status.
- **resource_type** (string, optional) [query]: Filter share resources by resource_type.
- **page** (integer, optional) [query]: Page number.
- **per_page** (integer, optional) [query]: Number of objects to return per page.

## Response

### 200

List account share resources response.

_Empty object_

### 4XX

List account share resources response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

List account share resources response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
