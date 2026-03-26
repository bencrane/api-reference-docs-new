# Reactivate Client Certificate

`PATCH /zones/{zone_id}/client_certificates/{client_certificate_id}`

If a API Shield mTLS Client Certificate is in a pending_revocation state, you may reactivate it with this endpoint.

## Parameters

- **zone_id** (string, required) [path]: 
- **client_certificate_id** (string, required) [path]: 

## Request Body

- **reactivate** (boolean, optional): 

## Response

### 200

Reactivate Client Certificate Response

- **result** (object, optional): 

### 4XX

Reactivate Client Certificate Response Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
