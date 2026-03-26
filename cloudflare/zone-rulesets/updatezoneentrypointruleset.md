# Update a zone entry point ruleset

`PUT /zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint`

Updates a zone entry point ruleset, creating a new version.

## Parameters

- **ruleset_phase** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An informative description of the ruleset.
- **id** (object, optional): 
- **last_updated** (string, optional): The timestamp of when the ruleset was last modified.
- **name** (string, optional): The human-readable name of the ruleset.
- **version** (object, optional): 
- **rules** (array, optional): The list of rules in the ruleset.

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
