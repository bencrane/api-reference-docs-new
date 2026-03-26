# Delete trigger

`DELETE /accounts/{account_id}/builds/triggers/{trigger_uuid}`

Remove a CI/CD trigger

## Parameters

- **account_id** (string, required) [path]: 
- **trigger_uuid** (string, required) [path]: 

## Response

### 200

Operation successful

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 404

Resource not found

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
