# Delete scheduled page test

`DELETE /zones/{zone_id}/speed_api/schedule/{url}`

Deletes a scheduled test for a page.

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
