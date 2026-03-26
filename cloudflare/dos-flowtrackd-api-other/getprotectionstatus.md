# Get protection status.

`GET /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status`

Get the protection status of the account.

## Parameters

- **account_id** (string, required) [path]: The account ID.

## Response

### 200

Get protection status response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get protection status failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
