# Get a Cloudflare Tunnel management token

`POST /accounts/{account_id}/cfd_tunnel/{tunnel_id}/management`

Gets a management token used to access the management resources (i.e. Streaming Logs) of a tunnel.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Request Body

- **resources** (array, required): 

## Response

### 200

Get a Cloudflare Tunnel management token response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (string, optional): The Tunnel Token is used as a mechanism to authenticate the operation of a tunnel.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Cloudflare API response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
