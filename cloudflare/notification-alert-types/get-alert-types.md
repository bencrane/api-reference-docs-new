# Get Alert Types

`GET /accounts/{account_id}/alerting/v3/available_alerts`

Gets a list of all alert types for which an account is eligible.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get Alert Types response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`
- **result** (object, optional): 

### 4XX

Get Alert Types response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
