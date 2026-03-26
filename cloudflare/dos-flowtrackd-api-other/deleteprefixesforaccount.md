# Delete all prefixes.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes`

Delete all prefixes for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Response

### 200

Delete all prefixes response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete all prefixes failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
