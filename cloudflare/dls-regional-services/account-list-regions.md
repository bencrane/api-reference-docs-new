# List Regions

`GET /accounts/{account_id}/addressing/regional_hostnames/regions`

List all Regional Services regions available for use by this account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List regions response

- **result** (array, optional): 

### 4XX

Failure to list regions

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
