# Get quota and availability

`GET /zones/{zone_id}/speed_api/availabilities`

Retrieves quota for all plans, as well as the current zone quota.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Page test availability.

- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
