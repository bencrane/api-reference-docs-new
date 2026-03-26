# Get analytics summary

`GET /zones/{zone_id}/spectrum/analytics/events/summary`

Retrieves a list of summarised aggregate metrics over a given time period.

## Parameters

- **zone_id** (string, required) [path]: 
- **dimensions** (string, optional) [query]: 
- **sort** (string, optional) [query]: 
- **until** (string, optional) [query]: 
- **metrics** (string, optional) [query]: 
- **filters** (string, optional) [query]: 
- **since** (string, optional) [query]: 

## Response

### 200

Get analytics summary response

- **result** (object, optional): 

### 4xx

Get analytics summary response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
