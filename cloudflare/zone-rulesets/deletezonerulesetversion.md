# Delete a zone ruleset version

`DELETE /zones/{zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}`

Deletes an existing version of a zone ruleset.

## Parameters

- **ruleset_version** (string, required) [path]: 
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
