# Update a Web Analytics rule

`PUT /accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}`

Updates a rule in a Web Analytics ruleset.

## Parameters

- **account_id** (string, required) [path]: 
- **ruleset_id** (string, required) [path]: 
- **rule_id** (string, required) [path]: 

## Request Body

- **host** (string, optional): 
- **inclusive** (boolean, optional): Whether the rule includes or excludes traffic from being measured.
- **is_paused** (boolean, optional): Whether the rule is paused or not.
- **paths** (array, optional): 

## Response

### 200

Updated Web Analytics rule.

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
