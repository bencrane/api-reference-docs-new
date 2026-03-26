# Create an account ruleset rule

`POST /accounts/{account_id}/rulesets/{ruleset_id}/rules`

Adds a new rule to an account ruleset. The rule will be added to the end of the existing list of rules in the ruleset by default.

## Parameters

- **ruleset_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

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
