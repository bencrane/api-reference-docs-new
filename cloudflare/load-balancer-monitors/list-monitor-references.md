# List Monitor References

`GET /user/load_balancers/monitors/{monitor_id}/references`

Get the list of resources that reference the provided monitor.

## Parameters

- **monitor_id** (string, required) [path]: 

## Response

### 200

List Monitor References response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): List of resources that reference a given monitor.

### 4XX

List Monitor References response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
