# Delete GRE Tunnel

`DELETE /accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}`

Disables and removes a specific static GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

## Parameters

- **gre_tunnel_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the response body will be presented using the new object format. Defaults to false.


## Response

### 200

Delete GRE Tunnel response

- **result** (object, optional): 

### 4XX

Delete GRE Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
