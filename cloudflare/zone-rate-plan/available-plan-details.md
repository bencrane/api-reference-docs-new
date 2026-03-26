# Available Plan Details

`GET /zones/{zone_id}/available_plans/{plan_identifier}`

Details of the available plan that the zone can subscribe to.

## Parameters

- **plan_identifier** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Available Plan Details response

- **result** (object, optional): 

### 4XX

Available Plan Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
