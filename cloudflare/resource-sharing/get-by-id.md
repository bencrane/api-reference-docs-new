# Get account share by ID

`GET /accounts/{account_id}/shares/{share_id}`

Fetches share by ID.

## Parameters

- **account_id** (string, required) [path]: 
- **share_id** (string, required) [path]: 
- **include_resources** (boolean, optional) [query]: Include resources in the response.
- **include_recipient_counts** (boolean, optional) [query]: Include recipient counts in the response.

## Response

### 200

Get account share response.

_Empty object_

### 4XX

Get account share response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.

### 5XX

Get account share response failure.

- **errors** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
