# List device settings profiles

`GET /accounts/{account_id}/devices/policies`

Fetches a list of the device settings profiles for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List device settings profiles response.

- **result** (array, optional): 

### 4XX

List device settings profiles response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
