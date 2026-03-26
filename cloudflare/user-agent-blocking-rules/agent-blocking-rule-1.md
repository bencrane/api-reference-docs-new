# Delete a User Agent Blocking rule

`DELETE /zones/{zone_id}/firewall/ua_rules/{ua_rule_id}`

Deletes an existing User Agent Blocking rule.

## Parameters

- **ua_rule_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 


## Response

### 200

Delete a User Agent Blocking rule response

- **result** (object, optional): 

### 4XX

Delete a User Agent Blocking rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
