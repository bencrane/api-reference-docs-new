# Delete rule

`DELETE /accounts/{account_id}/mnm/rules/{rule_id}`

Delete a network monitoring rule for account.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete rule response

- **result** (object, optional): 

### 4XX

Delete rule response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
