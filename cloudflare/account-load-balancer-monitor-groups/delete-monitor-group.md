# Delete Monitor Group

`DELETE /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}`

Delete a configured monitor group.

## Parameters

- **monitor_group_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete Monitor Group response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 412

Precondition Failed - Monitor group is in use by one or more pools

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 4XX

Delete Monitor Group response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
