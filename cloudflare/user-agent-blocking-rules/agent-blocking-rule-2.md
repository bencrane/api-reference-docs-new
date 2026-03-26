# Get a User Agent Blocking rule

`GET /zones/{zone_id}/firewall/ua_rules/{ua_rule_id}`

Fetches the details of a User Agent Blocking rule.

## Parameters

- **ua_rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a User Agent Blocking rule response

- **result** (object, optional): 

### 4XX

Get a User Agent Blocking rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
