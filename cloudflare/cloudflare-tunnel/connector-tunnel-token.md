# Get a Warp Connector Tunnel token

`GET /accounts/{account_id}/warp_connector/{tunnel_id}/token`

Gets the token used to associate warp device with a specific Warp Connector tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Response

### 200

Get a Warp Connector Tunnel token response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (string, optional): The Tunnel Token is used as a mechanism to authenticate the operation of a tunnel.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get a Warp Connector Tunnel token response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
