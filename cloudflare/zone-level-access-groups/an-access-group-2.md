# Get an Access group

`GET /zones/{zone_id}/access/groups/{group_id}`

Fetches a single Access group.

## Parameters

- **group_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get an Access group response

_Empty object_

### 4XX

Get an Access group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
