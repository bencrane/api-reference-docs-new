# Get current aggregated analytics

`GET /zones/{zone_id}/spectrum/analytics/aggregate/current`

Retrieves analytics aggregated from the last minute of usage on Spectrum applications underneath a given zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **appID** (string, optional) [query]: 
- **colo_name** (string, optional) [query]: 

## Response

### 200

Get current aggregated analytics response

- **result** (array, optional): 

### 4xx

Get current aggregated analytics response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
