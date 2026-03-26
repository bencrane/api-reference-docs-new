# Create allowlist prefix.

`POST /accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist`

Create an allowlist prefix for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Request Body

- **comment** (string, required): An comment describing the allowlist prefix.
- **enabled** (boolean, required): Whether to enable the allowlist prefix into effect.
- **prefix** (string, required): The allowlist prefix to add in CIDR format.

## Response

### 200

Create allowlist prefix response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create allowlist prefix failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
