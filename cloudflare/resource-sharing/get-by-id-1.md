# Get share recipient by ID

`GET /accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}`

Get share recipient by ID.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **recipient_id** (string, required) [path]: 
- **include_resources** (boolean, optional) [query]: Include resources in the response.

## Response

### 200

Get account share recipient response.

_Empty object_

### 4XX

Get account share recipient response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Get account share recipient response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
