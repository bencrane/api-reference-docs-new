# Deletes security.txt

`DELETE /zones/{zone_id}/security-center/securitytxt`

Removes the security.txt file configuration for a zone. The /.well-known/security.txt endpoint will no longer be served.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

The request was successful.

_Empty object_

### 4XX

A client error occurred.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
