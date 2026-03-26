# Delete Peer

`DELETE /accounts/{account_id}/secondary_dns/peers/{peer_id}`

Delete Peer.

## Parameters

- **peer_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Peer response.

_Empty object_

### 4XX

Delete Peer response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
