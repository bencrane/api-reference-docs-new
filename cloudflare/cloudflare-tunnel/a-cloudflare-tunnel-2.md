# Get a Cloudflare Tunnel

`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}`

Fetches a single Cloudflare Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Response

### 200

Get a Cloudflare Tunnel response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A Cloudflare Tunnel that connects your origin to Cloudflare's edge.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get a Cloudflare Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
