# Delete a Warp Connector Tunnel

`DELETE /accounts/{account_id}/warp_connector/{tunnel_id}`

Deletes a Warp Connector Tunnel from an account.

## Parameters

- **account_id** (string, required) [path]: 
- **tunnel_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Delete a Warp Connector Tunnel response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A Warp Connector Tunnel that connects your origin to Cloudflare's edge.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete a Warp Connector Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
