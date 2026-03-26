# Delete Endpoint Health Check

`DELETE /accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}`

Delete Endpoint Health Check.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (string, required) [path]: 

## Response

### 200

Endpoint Health Checks response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Endpoint Health Check failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
