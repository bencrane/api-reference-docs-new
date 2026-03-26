# Update protection status.

`PATCH /accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status`

Update the protection status of the account.

## Parameters

- **account_id** (string, required) [path]: The account ID.

## Request Body

- **enabled** (boolean, required): Enables or disables protection.

## Response

### 200

Update protection status response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update protection status failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
