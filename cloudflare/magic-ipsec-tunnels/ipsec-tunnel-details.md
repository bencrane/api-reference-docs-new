# List IPsec tunnel details

`GET /accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}`

Lists details for a specific IPsec tunnel.

## Parameters

- **ipsec_tunnel_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the response body will be presented using the new object format. Defaults to false.

## Response

### 200

List IPsec tunnel details response

- **result** (object, optional): 

### 4XX

List IPsec tunnel details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
