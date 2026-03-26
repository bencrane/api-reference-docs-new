# Get allowlist prefix.

`GET /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}`

Get an allowlist prefix specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **prefix_id** (string, required) [path]: The UUID of the allowlist prefix.

## Response

### 200

Get allowlist prefix response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get allowlist prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
