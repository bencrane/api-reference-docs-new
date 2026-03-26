# Get prefix.

`GET /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}`

Get a prefix specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **prefix_id** (string, required) [path]: The UUID of the prefix.

## Response

### 200

Get prefix response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
