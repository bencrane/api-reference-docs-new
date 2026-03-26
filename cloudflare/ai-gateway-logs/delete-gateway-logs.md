# Delete Gateway Logs

`DELETE /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs`



## Parameters

- **account_id** (string, required) [path]: 
- **gateway_id** (string, required) [path]: 
- **order_by** (string, optional) [query]: 
- **order_by_direction** (string, optional) [query]: 
- **filters** (array, optional) [query]: 
- **limit** (integer, optional) [query]: 

## Response

### 200

Returns if the delete was successful

- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
