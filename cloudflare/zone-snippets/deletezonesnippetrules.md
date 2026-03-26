# Delete zone snippet rules

`DELETE /zones/{zone_id}/snippets/snippet_rules`

Deletes all snippet rules belonging to the zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

A snippet rules response.

- **errors** (array, optional):  Values: ``
- **messages** (array, optional): Contain warning messages.
- **result** (array, optional): Lists snippet rules.
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
