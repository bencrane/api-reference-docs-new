# Get WARP Connector Tunnel connector

`GET /accounts/{account_id}/warp_connector/{tunnel_id}/connectors/{connector_id}`

Fetches connector and connection details for a WARP Connector Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 
- **connector_id** (string, required) [path]: 

## Response

### 200

Get WARP Connector Tunnel connector response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A WARP Connector client that maintains a connection to a Cloudflare data center.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get WARP Connector Tunnel connector response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
