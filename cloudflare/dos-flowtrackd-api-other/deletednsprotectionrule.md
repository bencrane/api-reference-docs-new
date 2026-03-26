# Delete DNS Protection rule.

`DELETE /accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}`

Delete a DNS Protection rule specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **rule_id** (string, required) [path]: The UUID of the DNS Protection rule to delete.

## Response

### 200

Delete DNS Protection rule response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete DNS Protection rule failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
