# Delete a Page Rule

`DELETE /zones/{zone_id}/pagerules/{pagerule_id}`

Deletes an existing Page Rule.

## Parameters

- **pagerule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete a Page Rule response

_Empty object_

### 4XX

Delete a Page Rule response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
