# List WARP Connector Tunnel connections

`GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections`

Fetches connection details for a WARP Connector Tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Response

### 200

List WARP Connector Tunnel connections response

- **result** (array, optional): 

### 4XX

List WARP Connector connections response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
