# Put configuration

`PUT /accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations`

Adds or updates the configuration for a remotely-managed tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Request Body

- **config** (object, optional): The tunnel configuration and ingress rules.

## Response

### 200

Put configuration response

- **result** (object, optional): Cloudflare Tunnel configuration

### 4XX

Put configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
