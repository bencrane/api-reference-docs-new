# List Monitors

`GET /accounts/{account_id}/load_balancers/monitors`

List configured monitors for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Monitors response.

- **result** (array, optional): 

### 4XX

List Monitors response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
