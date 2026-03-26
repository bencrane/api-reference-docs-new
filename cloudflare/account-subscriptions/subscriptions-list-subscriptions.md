# List Subscriptions

`GET /accounts/{account_id}/subscriptions`

Lists all of an account's subscriptions.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Subscriptions response

- **result** (array, optional): 

### 4XX

List Subscriptions response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
