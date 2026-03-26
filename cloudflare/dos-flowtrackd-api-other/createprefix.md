# Create prefix.

`POST /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes`

Create a prefix for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Request Body

- **comment** (string, required): A comment describing the prefix.
- **excluded** (boolean, required): Whether to exclude the prefix from protection.
- **prefix** (string, required): The prefix to add in CIDR format.

## Response

### 200

Create prefix response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
