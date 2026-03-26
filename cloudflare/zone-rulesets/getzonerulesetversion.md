# Get a zone ruleset version

`GET /zones/{zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}`

Fetches a specific version of a zone ruleset.

## Parameters

- **ruleset_version** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

A ruleset response.

- **errors** (enum, optional):  Values: ``
- **messages** (array, optional): A list of warning messages.
- **result** (object, optional): 
- **success** (enum, optional):  Values: `true`

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
