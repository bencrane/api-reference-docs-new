# Get a list

`GET /accounts/{account_id}/rules/lists/{list_id}`

Fetches the details of a list.

## Parameters

- **list_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get a list response.

_Empty object_

### 4XX

Get a list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
