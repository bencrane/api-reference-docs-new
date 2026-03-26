# Get logs RayIDs

`GET /zones/{zone_id}/logs/rayids/{ray_id}`

The `/rayids` api route allows lookups by specific rayid. The rayids route will return zero, one, or more records (ray ids are not unique).

## Parameters

- **zone_id** (string, required) [path]: 
- **ray_id** (string, required) [path]: 
- **fields** (string, optional) [query]: 
- **timestamps** (string, optional) [query]: 

## Response

### 200

Get logs RayIDs response

Type: object

### 4XX

Get logs RayIDs response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
