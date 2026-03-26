# List Zone Lockdown rules

`GET /zones/{zone_id}/firewall/lockdowns`

Fetches Zone Lockdown rules. You can filter the results using several optional parameters.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **description** (string, optional) [query]: 
- **modified_on** (string, optional) [query]: 
- **ip** (string, optional) [query]: 
- **priority** (string, optional) [query]: 
- **uri_search** (string, optional) [query]: 
- **ip_range_search** (string, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **created_on** (string, optional) [query]: 
- **description_search** (string, optional) [query]: 
- **ip_search** (string, optional) [query]: 

## Response

### 200

List Zone Lockdown rules response

- **result** (array, optional): 

### 4XX

List Zone Lockdown rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
