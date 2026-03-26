# Get analytics by time

`GET /zones/{zone_id}/spectrum/analytics/events/bytime`

Retrieves a list of aggregate metrics grouped by time interval.

## Parameters

- **zone_id** (string, required) [path]: 
- **dimensions** (string, optional) [query]: 
- **sort** (string, optional) [query]: 
- **until** (string, optional) [query]: 
- **metrics** (string, optional) [query]: 
- **filters** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **time_delta** (string, required) [query]: 

## Response

### 200

Get analytics by time response

- **result** (object, optional): 

### 4xx

Get analytics by time response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
