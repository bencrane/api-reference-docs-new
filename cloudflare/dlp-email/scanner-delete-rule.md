# Delete email scanner rule

`DELETE /accounts/{account_id}/dlp/email/rules/{rule_id}`

Removes a DLP email scanning rule. The rule will no longer be applied to email messages.

## Parameters

- **account_id** (string, required) [path]: 
- **rule_id** (string, required) [path]: 

## Response

### 200

Delete Email Scanner Rule response.

- **result** (object, optional): 

### 4XX

Delete Email Scanner Rule failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
