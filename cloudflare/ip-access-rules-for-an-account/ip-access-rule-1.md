# Delete an IP Access rule

`DELETE /accounts/{account_id}/firewall/access_rules/rules/{rule_id}`

Deletes an existing IP Access rule defined at the account level.

Note: This operation will affect all zones in the account.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete an IP Access rule response.

_Empty object_

### 4XX

Delete an IP Access rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
