# Get Silence

`GET /accounts/{account_id}/alerting/v3/silences/{silence_id}`

Gets a specific silence for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **silence_id** (string, required) [path]: 

## Response

### 200

Get Silence response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (object, optional): 

### 4XX

Get Silence response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
