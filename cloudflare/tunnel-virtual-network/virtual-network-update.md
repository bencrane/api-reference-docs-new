# Update a virtual network

`PATCH /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}`

Updates an existing virtual network.

## Parameters

- **account_id** (string, required) [path]: 
- **virtual_network_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Optional remark describing the virtual network.
- **is_default_network** (boolean, optional): If `true`, this virtual network is the default for the account.
- **name** (string, optional): A user-friendly name for the virtual network.

## Response

### 200

Update a virtual network response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update a virtual network response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
