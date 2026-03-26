# Create a Warp Connector Tunnel

`POST /accounts/{account_id}/warp_connector`

Creates a new Warp Connector Tunnel in an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ha** (boolean, optional): Indicates that the tunnel will be created to be highly available. If omitted, defaults to false.
- **name** (string, required): A user-friendly name for a tunnel.

## Response

### 200

Create a Warp Connector Tunnel response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): A Warp Connector Tunnel that connects your origin to Cloudflare's edge.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create a Warp Connector Tunnel response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
