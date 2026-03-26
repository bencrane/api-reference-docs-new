# Get a Page Shield policy

`GET /zones/{zone_id}/page_shield/policies/{policy_id}`

Fetches a Page Shield policy by ID.

## Parameters

- **zone_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 200

Get a Page Shield policy response

- **result** (object, optional): 

### 4XX

Get a Page Shield policy response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
