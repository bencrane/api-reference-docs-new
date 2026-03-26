# List Peers

`GET /accounts/{account_id}/secondary_dns/peers`

List Peers.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Peers response.

_Empty object_

### 4XX

List Peers response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
