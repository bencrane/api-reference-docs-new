# Create a tunnel route (CIDR Endpoint)

`POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`

> **Deprecated**

Routes a private network through a Cloudflare Tunnel. The CIDR in `ip_network_encoded` must be written in URL-encoded format.

## Parameters

- **ip_network_encoded** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Optional remark describing the route.
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
