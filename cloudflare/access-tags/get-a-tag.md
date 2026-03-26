# Get a tag

`GET /accounts/{account_id}/access/tags/{tag_name}`

Get a tag

## Parameters

- **account_id** (string, required) [path]: 
- **tag_name** (string, required) [path]: 

## Response

### 200

Get a tag response

_Empty object_

### 4XX

Get a tag response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
