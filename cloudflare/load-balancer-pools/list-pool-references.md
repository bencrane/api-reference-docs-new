# List Pool References

`GET /user/load_balancers/pools/{pool_id}/references`

Get the list of resources that reference the provided pool.

## Parameters

- **pool_id** (string, required) [path]: 

## Response

### 200

List Pool References response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): List of resources that reference a given pool.

### 4XX

List Pool References response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
