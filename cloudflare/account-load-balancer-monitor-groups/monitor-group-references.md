# List Monitor Group References

`GET /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}/references`

Get the list of resources that reference the provided monitor group.

## Parameters

- **monitor_group_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List Monitor Group References response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): List of resources that reference a given monitor group.

### 4XX

List Monitor Group References response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
