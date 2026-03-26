# List an account ruleset version's rules by tag

`GET /accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}`

Fetches the rules of a managed account ruleset version for a given tag.

## Parameters

- **rule_tag** (string, required) [path]: 
- **ruleset_version** (string, required) [path]: 
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
