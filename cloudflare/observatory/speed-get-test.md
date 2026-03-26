# Get a page test result

`GET /zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}`

Retrieves the result of a specific test.

## Parameters

- **zone_id** (string, required) [path]: 
- **url** (string, required) [path]: 
- **test_id** (string, required) [path]: 

## Response

### 200

Page test result.

- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
