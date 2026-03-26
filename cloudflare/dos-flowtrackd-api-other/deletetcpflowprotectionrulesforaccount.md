# Delete all TCP Flow Protection rules.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules`

Delete all TCP Flow Protection rules for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Response

### 200

Delete all TCP Flow Protection rules response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete all TCP Flow Protection rules failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
