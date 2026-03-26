# List core web vital metrics trend

`GET /zones/{zone_id}/speed_api/pages/{url}/trend`

Lists the core web vital metrics trend over time for a specific page.

## Parameters

- **zone_id** (string, required) [path]: 
- **url** (string, required) [path]: 
- **region** (string, required) [query]: 
- **deviceType** (string, required) [query]: 
- **start** (string, required) [query]: 
- **end** (string, optional) [query]: 
- **tz** (string, required) [query]: The timezone of the start and end timestamps.
- **metrics** (string, required) [query]: A comma-separated list of metrics to include in the results.

## Response

### 200

Page trend.

- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
