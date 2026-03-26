# Delete a tunnel route (CIDR Endpoint)

`DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`

> **Deprecated**

Deletes a private network route from an account. The CIDR in `ip_network_encoded` must be written in URL-encoded format. If no virtual_network_id is provided it will delete the route from the default vnet. If no tun_type is provided it will fetch the type from the tunnel_id or if that is missing it will assume Cloudflare Tunnel as default. If tunnel_id is provided it will delete the route from that tunnel, otherwise it will delete the route based on the vnet and tun_type.


## Parameters

- **ip_network_encoded** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **virtual_network_id** (string, optional) [query]: 
- **tun_type** (string, optional) [query]: 
- **tunnel_id** (string, optional) [query]: 

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
