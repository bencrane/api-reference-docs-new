# List mTLS certificates

`GET /zones/{zone_id}/access/certificates`

Lists all mTLS certificates.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List mTLS certificates response

_Empty object_

### 4XX

List mTLS certificates response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
