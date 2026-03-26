# Delete all page tests

`DELETE /zones/{zone_id}/speed_api/pages/{url}/tests`

Deletes all tests for a specific webpage from a specific region. Deleted tests are still counted as part of the quota.

## Parameters

- **zone_id** (string, required) [path]: 
- **url** (string, required) [path]: 
- **region** (string, optional) [query]: 

## Response

### 200

Number of deleted tests.

- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
