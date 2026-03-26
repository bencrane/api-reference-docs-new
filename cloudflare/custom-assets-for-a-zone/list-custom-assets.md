# List custom assets

`GET /zones/{zone_identifier}/custom_pages/assets`

Fetches all the custom assets at the zone level.

## Parameters

- **zone_identifier** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List custom assets response

- **result** (array, optional): 

### 4XX

List custom assets response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
