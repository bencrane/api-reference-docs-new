# List Page Rules

`GET /zones/{zone_id}/pagerules`

Fetches Page Rules in a zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **status** (string, optional) [query]: 

## Response

### 200

List Page Rules response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Page Rules response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
