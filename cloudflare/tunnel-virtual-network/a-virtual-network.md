# Create a virtual network

`POST /accounts/{account_id}/teamnet/virtual_networks`

Adds a new virtual network to an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Optional remark describing the virtual network.
- **is_default** (boolean, optional): If `true`, this virtual network is the default for the account.
- **is_default_network** (boolean, optional): If `true`, this virtual network is the default for the account.
- **name** (string, required): A user-friendly name for the virtual network.

## Response

### 200

Create a virtual network response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create a virtual network response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
