# Peer Details

`GET /accounts/{account_id}/secondary_dns/peers/{peer_id}`

Get Peer.

## Parameters

- **peer_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Peer Details response.

_Empty object_

### 4XX

Peer Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
