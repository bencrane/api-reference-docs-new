# Delete an account ruleset version

`DELETE /accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}`

Deletes an existing version of an account ruleset.

## Parameters

- **ruleset_version** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 204

An empty response.

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
