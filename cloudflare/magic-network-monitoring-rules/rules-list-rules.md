# List rules

`GET /accounts/{account_id}/mnm/rules`

Lists network monitoring rules for account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List rules response

- **result** (array, optional): 

### 4XX

List rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
