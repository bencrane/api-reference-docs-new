# Delete a zone snippet

`DELETE /zones/{zone_id}/snippets/{snippet_name}`

Deletes a snippet belonging to the zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **snippet_name** (string, required) [path]: 

## Response

### 200

Return a null response.

- **errors** (array, optional):  Values: ``
- **messages** (array, optional): Contain warning messages.
- **result** (object, optional):  Values: ``
- **success** (boolean, optional):  Values: `true`

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
