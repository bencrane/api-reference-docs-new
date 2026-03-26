# Get a Warp Connector Tunnel

`GET /accounts/{account_id}/warp_connector/{tunnel_id}`

Fetches a single Warp Connector Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Response

### 200

Get a Warp Connector Tunnel response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A Warp Connector Tunnel that connects your origin to Cloudflare's edge.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get a Warp Connector Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
