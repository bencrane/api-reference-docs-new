# List account rulesets

`GET /accounts/{account_id}/rulesets`

Fetches all rulesets at the account level.

## Parameters

- **account_id** (string, required) [path]: 
- **cursor** (string, optional) [query]: 
- **per_page** (string, optional) [query]: 

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
