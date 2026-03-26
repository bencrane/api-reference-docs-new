# Delete Zero Trust certificate

`DELETE /accounts/{account_id}/gateway/certificates/{certificate_id}`

Delete a gateway-managed Zero Trust certificate. You must deactivate the certificate from the edge (inactive) before deleting it.

## Parameters

- **certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Deletes Zero Trust certificate response.

_Empty object_

### 4XX

Deletes Zero Trust certificate response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
