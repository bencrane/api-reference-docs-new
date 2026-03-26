# List Monitor Groups

`GET /accounts/{account_id}/load_balancers/monitor_groups`

List configured monitor groups.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Monitor Groups response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List Monitor Groups response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
