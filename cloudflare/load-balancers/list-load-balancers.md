# List Load Balancers

`GET /zones/{zone_id}/load_balancers`

List configured load balancers.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Load Balancers response.

- **result** (array, optional): 

### 4XX

List Load Balancers response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
