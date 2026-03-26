# Get a virtual network

`GET /accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}`

Get a virtual network.

## Parameters

- **account_id** (string, required) [path]: 
- **virtual_network_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Optional remark describing the virtual network.
- **is_default_network** (boolean, optional): If `true`, this virtual network is the default for the account.
- **name** (string, optional): A user-friendly name for the virtual network.

## Response

### 200

A virtual network response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

A virtual network response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
