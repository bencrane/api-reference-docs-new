# List Available Plans

`GET /zones/{zone_id}/available_plans`

Lists available plans the zone can subscribe to.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Available Plans response

- **result** (array, optional): 

### 4XX

List Available Plans response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
