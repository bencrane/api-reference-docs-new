# List GRE Tunnel Details

`GET /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}`

Lists informtion for a specific GRE tunnel.

## Parameters

- **gre_tunnel_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the response body will be presented using the new object format. Defaults to false.

## Response

### 200

List GRE Tunnel Details response

- **result** (object, optional): 

### 4XX

List GRE Tunnel Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
