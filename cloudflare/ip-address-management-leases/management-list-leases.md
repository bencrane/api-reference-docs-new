# List Leases

`GET /accounts/{account_id}/addressing/leases`

List all leases owned by the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Leases response

- **result** (array, optional): 

### 4XX

List Leases response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
