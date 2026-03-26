# Delete all SYN Protection filters.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters`

Delete all SYN Protection filters for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Response

### 200

Delete all SYN Protection filters response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete all SYN Protection filters failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
