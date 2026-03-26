# Get SYN Protection rule.

`GET /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}`

Get a SYN Protection rule specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **rule_id** (string, required) [path]: The UUID of the SYN Protection rule.

## Response

### 200

Get SYN Protection rule response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get SYN Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
