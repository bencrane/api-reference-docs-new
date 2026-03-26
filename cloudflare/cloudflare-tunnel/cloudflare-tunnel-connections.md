# Clean up Cloudflare Tunnel connections

`DELETE /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections`

Removes a connection (aka Cloudflare Tunnel Connector) from a Cloudflare Tunnel independently of its current state. If no connector id (client_id) is provided all connectors will be removed. We recommend running this command after rotating tokens.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 
- **client_id** (string, optional) [query]: 

## Request Body

_Empty object_

## Response

### 200

Clean up Cloudflare Tunnel connections response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Clean up Cloudflare Tunnel connections response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
