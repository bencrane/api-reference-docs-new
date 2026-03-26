# Generate Pre Shared Key (PSK) for IPsec tunnels

`POST /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate`

Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes. After a PSK is generated, the PSK is immediately persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a safe place.

## Parameters

- **ipsec_tunnel_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Generate Pre Shared Key (PSK) for IPsec tunnels response

- **result** (object, optional): 

### 4XX

Generate Pre Shared Key (PSK) for IPsec tunnels response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
