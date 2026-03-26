# Get configuration

`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations`

Gets the configuration for a remotely-managed tunnel

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Response

### 200

Get configuration response

- **result** (object, optional): Cloudflare Tunnel configuration

### 4XX

Get configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
