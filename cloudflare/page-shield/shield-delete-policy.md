# Delete a Page Shield policy

`DELETE /zones/{zone_id}/page_shield/policies/{policy_id}`

Delete a Page Shield policy by ID.

## Parameters

- **zone_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 204

Delete a Page Shield policy response

### 4XX

Delete a Page Shield policy response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
