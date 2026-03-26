# Monitor Group Details

`GET /accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}`

Fetch a single configured monitor group.

## Parameters

- **monitor_group_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Monitor Group Details response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Monitor Group Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
