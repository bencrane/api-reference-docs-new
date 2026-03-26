# List User Agent Blocking rules

`GET /zones/{zone_id}/firewall/ua_rules`

Fetches User Agent Blocking rules in a zone. You can filter the results using several optional parameters.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **description** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **user_agent** (string, optional) [query]: 
- **paused** (boolean, optional) [query]: 

## Response

### 200

List User Agent Blocking rules response

- **result** (array, optional): 

### 4XX

List User Agent Blocking rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
