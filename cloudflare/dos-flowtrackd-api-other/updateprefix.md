# Update prefix.

`PATCH /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}`

Update a prefix specified by the given UUID.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.
- **prefix_id** (string, required) [path]: The UUID of the prefix to update.

## Request Body

- **comment** (string, optional): A new comment for the prefix. Optional.
- **excluded** (boolean, optional): Whether to exclude the prefix from protection. Optional.

## Response

### 200

Update prefix response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
