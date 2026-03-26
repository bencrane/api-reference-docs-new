# Get a zone entry point ruleset

`GET /zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint`

Fetches the latest version of the zone entry point ruleset for a given phase.

## Parameters

- **ruleset_phase** (string, required) [path]: 
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
