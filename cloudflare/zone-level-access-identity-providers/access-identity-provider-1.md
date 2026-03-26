# Delete an Access identity provider

`DELETE /zones/{zone_id}/access/identity_providers/{identity_provider_id}`

Deletes an identity provider from Access.

## Parameters

- **identity_provider_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 202

Delete an Access identity provider response

_Empty object_

### 4XX

Delete an Access identity provider response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
