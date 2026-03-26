# Delete a service token

`DELETE /zones/{zone_id}/access/service_tokens/{service_token_id}`

Deletes a service token.

## Parameters

- **service_token_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete a service token response

_Empty object_

### 4XX

Delete a service token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
