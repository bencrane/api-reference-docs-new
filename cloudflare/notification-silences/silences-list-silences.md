# List Silences

`GET /accounts/{account_id}/alerting/v3/silences`

Gets a list of silences for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Silences response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (array, optional): 

### 4XX

List Silences response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
