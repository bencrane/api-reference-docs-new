# List short-lived certificate CAs

`GET /zones/{zone_id}/access/apps/ca`

Lists short-lived certificate CAs and their public keys.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List short-lived certificate CAs response

_Empty object_

### 4XX

List short-lived certificate CAs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
