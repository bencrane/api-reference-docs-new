# List firewall rules

`GET /zones/{zone_id}/firewall/rules`

> **Deprecated**

Fetches firewall rules in a zone. You can filter the results using several optional parameters.

## Parameters

- **zone_id** (string, required) [path]: 
- **description** (string, optional) [query]: 
- **action** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **id** (string, optional) [query]: 
- **paused** (boolean, optional) [query]: 

## Response

### 200

List firewall rules response

- **result** (array, optional): 

### 4XX

List firewall rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
