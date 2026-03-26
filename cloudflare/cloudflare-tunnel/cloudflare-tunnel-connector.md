# Get Cloudflare Tunnel connector

`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}`

Fetches connector and connection details for a Cloudflare Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 
- **connector_id** (string, required) [path]: 

## Response

### 200

Get Cloudflare Tunnel connector response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A client (typically cloudflared) that maintains connections to a Cloudflare data center.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get Cloudflare Tunnel connector response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
