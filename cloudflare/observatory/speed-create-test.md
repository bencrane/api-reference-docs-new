# Start page test

`POST /zones/{zone_id}/speed_api/pages/{url}/tests`

Starts a test for a specific webpage, in a specific region.

## Parameters

- **zone_id** (string, required) [path]: 
- **url** (string, required) [path]: 

## Request Body

- **region** (object, optional): 

## Response

### 200

Page test details.

- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
