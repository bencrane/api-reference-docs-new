# Delete prefix.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}`

Delete the prefix for an account given a UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **prefix_id** (string, required) [path]: The UUID of the prefix to delete.

## Response

### 200

Delete prefix response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
