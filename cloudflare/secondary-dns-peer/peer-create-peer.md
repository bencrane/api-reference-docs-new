# Create Peer

`POST /accounts/{account_id}/secondary_dns/peers`

Create Peer.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): The name of the peer.

## Response

### 200

Create Peer response.

_Empty object_

### 4XX

Create Peer response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
