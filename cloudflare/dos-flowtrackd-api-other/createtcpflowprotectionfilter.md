# Create a TCP Flow Protection filter.

`POST /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters`

Create a TCP Flow Protection filter for an account.

## Parameters

- **account_id** (string, required) [path]: The ID of the account.

## Request Body

- **expression** (string, required): The filter expression.
- **mode** (string, required): The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'.

## Response

### 200

Create TCP Flow Protection filter response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create TCP Flow Protection filter failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
