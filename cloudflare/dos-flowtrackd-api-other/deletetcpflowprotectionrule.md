# Delete TCP Flow Protection rule.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}`

Delete a TCP Flow Protection rule specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **rule_id** (string, required) [path]: The UUID of the TCP Flow Protection rule to delete.

## Response

### 200

Delete TCP Flow Protection rule response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete TCP Flow Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
