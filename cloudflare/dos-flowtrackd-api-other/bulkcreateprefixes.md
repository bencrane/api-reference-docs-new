# Create multiple prefixes.

`POST /accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/bulk`

Create multiple prefixes for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Request Body

Array of object

## Response

### 200

Create multiple prefixes response.

- **result** (array, optional): 

### 4XX

Create multiple prefixes failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
