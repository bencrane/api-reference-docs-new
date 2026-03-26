# Create a Cloudflare Tunnel

`POST /accounts/{account_id}/cfd_tunnel`

Creates a new Cloudflare Tunnel in an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **config_src** (string, optional): Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel on the Zero Trust dashboard. Values: `local`, `cloudflare`
- **name** (string, required): A user-friendly name for a tunnel.
- **tunnel_secret** (string, optional): Sets the password required to run a locally-managed tunnel. Must be at least 32 bytes and encoded as a base64 string.

## Response

### 200

Create a Cloudflare Tunnel response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A Cloudflare Tunnel that connects your origin to Cloudflare's edge.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create a Cloudflare Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
