# Add script secret

`PUT /accounts/{account_id}/workers/scripts/{script_name}/secrets`

Add a secret to a script.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Put script secret binding success.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): A secret value accessible through a binding.

### 4XX

Put script secret binding failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
