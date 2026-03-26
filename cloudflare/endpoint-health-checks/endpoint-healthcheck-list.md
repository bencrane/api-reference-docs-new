# List Endpoint Health Checks

`GET /accounts/{account_id}/diagnostics/endpoint-healthchecks`

List Endpoint Health Checks.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Endpoint Health Checks for account.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Endpoint Health Check response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
