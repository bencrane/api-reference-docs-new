# Create a tunnel route

`POST /accounts/{account_id}/teamnet/routes`

Routes a private network through a Cloudflare Tunnel.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Optional remark describing the route.
- **network** (string, required): The private IPv4 or IPv6 range connected by the route, in CIDR notation.
- **tunnel_id** (string, required): UUID of the tunnel.
- **virtual_network_id** (string, optional): UUID of the virtual network.

## Response

### 200

Create a tunnel route response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create a tunnel route response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
