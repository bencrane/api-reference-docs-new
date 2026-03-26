# Create scheduled page test

`POST /zones/{zone_id}/speed_api/schedule/{url}`

Creates a scheduled test for a page.

## Parameters

- **zone_id** (string, required) [path]: 
- **url** (string, required) [path]: 
- **region** (string, optional) [query]: 
- **frequency** (string, optional) [query]: The frequency of the scheduled test. Defaults to WEEKLY for free plans, DAILY for paid plans.

## Response

### 200

Page test schedule.

- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
