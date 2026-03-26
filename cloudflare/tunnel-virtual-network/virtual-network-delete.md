# Delete a virtual network

`DELETE /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}`

Deletes an existing virtual network.

## Parameters

- **virtual_network_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a virtual network response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete a virtual network response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
