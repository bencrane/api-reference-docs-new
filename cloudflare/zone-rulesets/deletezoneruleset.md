# Delete a zone ruleset

`DELETE /zones/{zone_id}/rulesets/{ruleset_id}`

Deletes all versions of an existing zone ruleset.

## Parameters

- **ruleset_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 204

An empty response.

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
