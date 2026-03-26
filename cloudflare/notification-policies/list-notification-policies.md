# List Notification policies

`GET /accounts/{account_id}/alerting/v3/policies`

Get a list of all Notification policies.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List Notification policies response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (array, optional): 

### 4XX

List Notification policies response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
