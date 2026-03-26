# List Routes

`GET /zones/{zone_id}/workers/routes`

Returns routes for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Routes response.

_Empty object_

### 4XX

List Routes response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
