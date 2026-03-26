# Delete Route

`DELETE /accounts/{account_id}/magic/routes/{route_id}`

Disable and remove a specific Magic static route.

## Parameters

- **route_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Route response

- **result** (object, optional): 

### 4XX

Delete Route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
