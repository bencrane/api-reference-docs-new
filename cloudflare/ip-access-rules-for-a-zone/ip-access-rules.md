# List IP Access rules

`GET /zones/{zone_id}/firewall/access_rules/rules`

Fetches IP Access rules of a zone. You can filter the results using several optional parameters.

## Parameters

- **zone_id** (string, required) [path]: 
- **mode** (string, optional) [query]: 
- **configuration.target** (string, optional) [query]: 
- **configuration.value** (string, optional) [query]: 
- **notes** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 

## Response

### 200

List IP Access rules response.

- **result** (array, optional): 

### 4XX

List IP Access rules response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
