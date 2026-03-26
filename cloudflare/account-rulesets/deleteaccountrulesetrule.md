# Delete an account ruleset rule

`DELETE /accounts/{account_id}/rulesets/{ruleset_id}/rules/{rule_id}`

Deletes an existing rule from an account ruleset.

## Parameters

- **rule_id** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

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
