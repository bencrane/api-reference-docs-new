# List Health Checks

`GET /zones/{zone_id}/healthchecks`

List configured health checks.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: Page number of paginated results.
- **per_page** (number, optional) [query]: Maximum number of results per page. Must be a multiple of 5.

## Response

### 200

List Health Checks response

- **result** (array, optional): 

### 4XX

List Health Checks response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
