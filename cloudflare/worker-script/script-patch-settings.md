# Patch Settings

`PATCH /accounts/{account_id}/workers/scripts/{script_name}/settings`

Patch metadata or config, such as bindings or usage model.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 


## Response

### 200

Patch settings.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch settings failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
