# Delete all SYN Protection rules.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules`

Delete all SYN Protection rules for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Response

### 200

Delete all SYN Protection rules response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete all SYN Protection rules failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
