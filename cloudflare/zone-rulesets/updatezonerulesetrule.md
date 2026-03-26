# Update a zone ruleset rule

`PATCH /zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}`

Updates an existing rule in a zone ruleset.

## Parameters

- **rule_id** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **position** (object, optional): 

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
