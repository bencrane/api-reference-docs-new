# Delete a Web Analytics rule

`DELETE /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}`

Deletes an existing rule from a Web Analytics ruleset.

## Parameters

- **account_id** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 
- **rule_id** (string, required) [path]: 

## Response

### 200

Deleted Web Analytics rule identifier.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
