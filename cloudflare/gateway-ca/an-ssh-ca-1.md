# Delete an SSH Certificate Authority (CA)

`DELETE /accounts/{account_id}/access/gateway_ca/{certificate_id}`

Deletes an SSH Certificate Authority.

## Parameters

- **certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete an SSH Certificate Authority (CA) response

_Empty object_

### 4XX

Delete an SSH Certificate Authority (CA) response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
