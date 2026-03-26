# List ACLs

`GET /accounts/{account_id}/secondary_dns/acls`

List ACLs.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List ACLs response.

_Empty object_

### 4XX

List ACLs response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
