# Delete TCP Flow Protection filter.

`DELETE /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}`

Delete a TCP Flow Protection filter specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **filter_id** (string, required) [path]: The UUID of the filter to delete.

## Response

### 200

Delete TCP Flow Protection filter response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete TCP Flow Protection filter failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
