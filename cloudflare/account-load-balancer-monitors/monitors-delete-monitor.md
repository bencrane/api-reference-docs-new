# Delete Monitor

`DELETE /accounts/{account_id}/load_balancers/monitors/{monitor_id}`

Delete a configured monitor.

## Parameters

- **monitor_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Monitor response.

- **result** (object, optional): 

### 4XX

Delete Monitor response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
