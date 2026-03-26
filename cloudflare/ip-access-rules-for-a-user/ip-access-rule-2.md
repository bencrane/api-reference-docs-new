# Update an IP Access rule

`PATCH /user/firewall/access_rules/rules/{rule_id}`

Updates an IP Access rule defined at the user level. You can only update the rule action (`mode` parameter) and notes.

## Parameters

- **rule_id** (string, required) [path]: 

## Request Body

- **mode** (string, optional): The action to apply to a matched request. Values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`
- **notes** (string, optional): An informative summary of the rule, typically used as a reminder or explanation.

## Response

### 200

Update an IP Access rule response.

- **result** (object, optional): 

### 4XX

Update an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
