# Get the default device settings profile

`GET /accounts/{account_id}/devices/policy`

Fetches the default device settings profile for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get the default device settings profile response.

- **result** (object, optional): 

### 4XX

Get the default device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
