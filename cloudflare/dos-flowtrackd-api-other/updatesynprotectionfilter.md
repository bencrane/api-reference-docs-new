# Update SYN Protection filter.

`PATCH /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}`

Update a SYN Protection filter specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **filter_id** (string, required) [path]: The UUID of the filter to update.

## Request Body

- **expression** (string, optional): The new filter expression. Optional.
- **mode** (string, optional): The new mode for the filter. Optional. Must be one of 'enabled', 'disabled', 'monitoring'.

## Response

### 200

Update SYN Protection filter response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update SYN Protection filter failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
