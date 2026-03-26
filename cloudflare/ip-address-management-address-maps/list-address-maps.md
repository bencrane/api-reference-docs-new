# List Address Maps

`GET /accounts/{account_id}/addressing/address_maps`

List all address maps owned by the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Address Maps response

- **result** (array, optional): 

### 4XX

List Address Maps response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
