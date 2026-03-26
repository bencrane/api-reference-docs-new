# List Cloudflare Tunnel connections

`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections`

Fetches connection details for a Cloudflare Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Response

### 200

List Cloudflare Tunnel connections response

- **result** (array, optional): 

### 4XX

List Cloudflare Tunnel connections response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
