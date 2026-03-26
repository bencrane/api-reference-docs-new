# List a zone entry point ruleset's versions

`GET /zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions`

Fetches the versions of a zone entry point ruleset.

## Parameters

- **ruleset_phase** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

A rulesets response.

- **errors** (enum, optional):  Values: ``
- **messages** (array, optional): A list of warning messages.
- **result** (array, optional): A list of rulesets. The returned information will not include the rules in each ruleset.
- **success** (enum, optional):  Values: `true`
- **result_info** (object, optional): Information to navigate the results.

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
