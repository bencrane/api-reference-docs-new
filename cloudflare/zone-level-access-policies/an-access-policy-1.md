# Delete an Access policy

`DELETE /zones/{zone_id}/access/apps/{app_id}/policies/{policy_id}`

Delete an Access policy.

## Parameters

- **policy_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 202

Delete an Access policy response

_Empty object_

### 4XX

Delete an Access policy response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
