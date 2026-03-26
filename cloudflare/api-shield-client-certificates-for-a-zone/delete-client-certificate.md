# Revoke Client Certificate

`DELETE /zones/{zone_id}/client_certificates/{client_certificate_id}`

Set a API Shield mTLS Client Certificate to pending_revocation status for processing to revoked status.

## Parameters

- **zone_id** (string, required) [path]: 
- **client_certificate_id** (string, required) [path]: 

## Response

### 200

Revoke Client Certificate Response

- **result** (object, optional): 

### 4XX

Revoke Client Certificate Response Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
