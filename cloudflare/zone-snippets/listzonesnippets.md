# List zone snippets

`GET /zones/{zone_id}/snippets`

Fetches all snippets belonging to the zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 

## Response

### 200

A snippets response.

- **errors** (array, optional):  Values: ``
- **messages** (array, optional): Contain warning messages.
- **result** (array, optional): Contain snippets.
- **success** (boolean, optional):  Values: `true`
- **result_info** (object, optional): Additional information to navigate the results.

### 4XX

Return a failure response.

- **errors** (array, optional): Lists error messages.
- **messages** (array, optional): Contain warning messages.
- **result** (object, optional):  Values: ``
- **success** (boolean, optional):  Values: `false`

### 5XX

Return a failure response.

- **errors** (array, optional): Lists error messages.
- **messages** (array, optional): Contain warning messages.
- **result** (object, optional):  Values: ``
- **success** (boolean, optional):  Values: `false`
