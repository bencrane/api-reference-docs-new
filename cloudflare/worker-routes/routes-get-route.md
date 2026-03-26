# Get Route

`GET /zones/{zone_id}/workers/routes/{route_id}`

Returns information about a route, including URL pattern and Worker.

## Parameters

- **route_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get Route response.

_Empty object_

### 4XX

Get Route response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
