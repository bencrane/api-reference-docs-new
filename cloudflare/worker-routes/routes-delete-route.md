# Delete Route

`DELETE /zones/{zone_id}/workers/routes/{route_id}`

Deletes a route.

## Parameters

- **route_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete Route response.

_Empty object_

### 4XX

Delete Route response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
