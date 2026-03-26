# Get a page test schedule

`GET /zones/{zone_id}/speed_api/schedule/{url}`

Retrieves the test schedule for a page in a specific region.

## Parameters

- **zone_id** (string, required) [path]: 
- **url** (string, required) [path]: 
- **region** (string, optional) [query]: 

## Response

### 200

Page test schedule.

- **result** (object, optional): The test schedule.

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
