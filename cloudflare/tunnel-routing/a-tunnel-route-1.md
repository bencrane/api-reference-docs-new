# Delete a tunnel route

`DELETE /accounts/{account_id}/teamnet/routes/{route_id}`

Deletes a private network route from an account.


## Parameters

- **route_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete a tunnel route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete a tunnel route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
