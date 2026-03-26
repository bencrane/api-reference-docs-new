# Update a User Agent Blocking rule

`PUT /zones/{zone_id}/firewall/ua_rules/{ua_rule_id}`

Updates an existing User Agent Blocking rule.

## Parameters

- **ua_rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **configuration** (object, required): The rule configuration.
- **description** (string, optional): An informative summary of the rule. This value is sanitized and any tags will be removed.
- **id** (string, required): The unique identifier of the resource.
- **mode** (string, required): The action to apply to a matched request. Values: `block`, `challenge`, `whitelist`, `js_challenge`, `managed_challenge`
- **paused** (boolean, optional): When true, indicates that the rule is currently paused.

## Response

### 200

Update a User Agent Blocking rule response

- **result** (object, optional): 

### 4XX

Update a User Agent Blocking rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
