# Get SYN Protection filter.

`GET /accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}`

Get a SYN Protection filter specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **filter_id** (string, required) [path]: The UUID of the filter to retrieve.

## Response

### 200

Get SYN Protection filter response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get SYN Protection filter failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
