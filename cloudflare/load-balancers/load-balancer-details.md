# Load Balancer Details

`GET /zones/{zone_id}/load_balancers/{load_balancer_id}`

Fetch a single configured load balancer.

## Parameters

- **zone_id** (string, required) [path]: 
- **load_balancer_id** (string, required) [path]: 

## Response

### 200

Load Balancer Details response.

- **result** (object, optional): 

### 4XX

Load Balancer Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
