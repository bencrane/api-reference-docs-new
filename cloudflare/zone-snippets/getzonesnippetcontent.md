# Get a zone snippet content

`GET /zones/{zone_id}/snippets/{snippet_name}/content`

Fetches the content of a snippet belonging to the zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **snippet_name** (string, required) [path]: 

## Response

### 200

Return snippet content.

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
