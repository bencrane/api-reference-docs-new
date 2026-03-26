# Update a Warp Connector Tunnel

`PATCH /accounts/{account_id}/warp_connector/{tunnel_id}`

Updates an existing Warp Connector Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): A user-friendly name for a tunnel.
- **tunnel_secret** (string, optional): Sets the password required to run a locally-managed tunnel. Must be at least 32 bytes and encoded as a base64 string.

## Response

### 200

Update a Warp Connector Tunnel response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A Warp Connector Tunnel that connects your origin to Cloudflare's edge.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update a Warp Connector Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
