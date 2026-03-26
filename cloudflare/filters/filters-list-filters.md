# List filters

`GET /zones/{zone_id}/filters`

> **Deprecated**

Fetches filters in a zone. You can filter the results using several optional parameters.

## Parameters

- **zone_id** (string, required) [path]: 
- **paused** (string, optional) [query]: 
- **expression** (string, optional) [query]: 
- **description** (string, optional) [query]: 
- **ref** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **id** (string, optional) [query]: 

## Response

### 200

List filters response

- **result** (array, optional): 

### 4XX

List filters response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
