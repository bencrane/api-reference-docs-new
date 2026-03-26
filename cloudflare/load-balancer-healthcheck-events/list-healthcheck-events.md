# List Healthcheck Events

`GET /user/load_balancing_analytics/events`

List origin health changes.

## Parameters

- **until** (string, optional) [query]: 
- **pool_name** (string, optional) [query]: 
- **origin_healthy** (string, optional) [query]: 
- **pool_id** (string, optional) [query]: 
- **since** (string, optional) [query]: 
- **origin_name** (string, optional) [query]: 
- **pool_healthy** (boolean, optional) [query]: 

## Response

### 200

List Healthcheck Events response.

- **result** (array, optional): 

### 4XX

List Healthcheck Events response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
