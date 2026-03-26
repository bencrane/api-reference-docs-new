# List Available Rate Plans

`GET /zones/{zone_id}/available_rate_plans`

Lists all rate plans the zone can subscribe to.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Available Rate Plans response

- **result** (array, optional): 

### 4XX

List Available Rate Plans response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
