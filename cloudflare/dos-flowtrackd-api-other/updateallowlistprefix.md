# Update allowlist prefix.

`PATCH /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}`

Update an allowlist prefix specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **prefix_id** (string, required) [path]: The UUID of the allowlist prefix to update.

## Request Body

- **comment** (string, optional): A comment describing the allowlist prefix. Optional.
- **enabled** (boolean, optional): Whether to enable the allowlist prefix into effect. Optional.

## Response

### 200

Update allowlist prefix response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update allowlist prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
