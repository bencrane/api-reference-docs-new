# Delete Load Balancer

`DELETE /zones/{zone_id}/load_balancers/{load_balancer_id}`

Delete a configured load balancer.

## Parameters

- **zone_id** (string, required) [path]: 
- **load_balancer_id** (string, required) [path]: 


## Response

### 200

Delete Load Balancer response.

- **result** (object, optional): 

### 4XX

Delete Load Balancer response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
