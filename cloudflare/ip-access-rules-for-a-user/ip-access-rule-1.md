# Delete an IP Access rule

`DELETE /user/firewall/access_rules/rules/{rule_id}`

Deletes an IP Access rule at the user level.

Note: Deleting a user-level rule will affect all zones owned by the user.

## Parameters

- **rule_id** (string, required) [path]: 


## Response

### 200

Delete an IP Access rule response.

- **result** (object, optional): 

### 4XX

Delete an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
