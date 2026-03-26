# Delete SYN Protection filter.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}`

Delete a SYN Protection filter specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **filter_id** (string, required) [path]: The UUID of the filter to delete.

## Response

### 200

Delete SYN Protection filter response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete SYN Protection filter failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
