# List application and application type mappings

`GET /accounts/{account_id}/gateway/app_types`

List all application and application type mappings.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List application and application type mappings response.

_Empty object_

### 4XX

List application and application type mappings response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
