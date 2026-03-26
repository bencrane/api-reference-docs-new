# Trigger a manual failover for a WARP Connector Tunnel

`PUT /accounts/{account_id}/warp_connector/{tunnel_id}/failover`

Triggers a manual failover for a specific WARP Connector Tunnel, setting the specified client as the active connector. The tunnel must be configured for high availability (HA) and the client must be linked to the tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Request Body

- **client_id** (string, required): UUID of the Cloudflare Tunnel connector.

## Response

### 200

Manual failover response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Manual failover response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
